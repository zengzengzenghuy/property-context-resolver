"""LLM summarizer for `context.<unit|property>.md` auto-blocks.

Implements the user's "Signal-First Property Management Philosophy". Salience
extraction lives in `blocks.py` (deterministic Python — confidence floor,
recency window, anomaly-only). This module asks Claude to render the already-
filtered signal as a 3-sentence German summary anchored in the Trifecta of
Truth: Contract / Law / Timeline.

The LLM is intentionally NOT a noise filter — by the time `summarize()` is
called the input is curated. The model's only job is prose.

Graceful degradation: when `ANTHROPIC_API_KEY` is unset, when `anthropic` is
not installed, or when the API call raises, the summarizer returns the
caller-supplied `fallback` so the pipeline still produces a valid context.md.

Cache: every call is keyed by SHA256 of (model, system prompt, payload) and
persisted to `out/.summary_cache.json`, so re-running on unchanged data is
free (and deterministic, despite the LLM).
"""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass

try:
    from anthropic import Anthropic
except ImportError:  # pragma: no cover - optional dep
    Anthropic = None  # type: ignore[assignment]

try:
    import google.generativeai as genai
except ImportError:  # pragma: no cover - optional dep
    genai = None  # type: ignore[assignment]


DEFAULT_ANTHROPIC_MODEL = "claude-haiku-4-5-20251001"
DEFAULT_GEMINI_MODEL = "gemini-1.5-flash-latest"
DEFAULT_MAX_TOKENS = 400
DEFAULT_CACHE_PATH = Path("out/llm_cache/summary.json")


# Encodes the user's Signal-First philosophy. Kept long deliberately so the
# `cache_control` directive engages once Anthropic's prompt-cache minimum is
# met — this prompt is sent once per block render and the system text never
# changes within a run.
SYSTEM_PROMPT = """\
You are an expert German property manager (Verwalter) writing concise summaries
that go inside auto-blocks in `context.<unit|property>.md` files. Your audience
is another senior property manager scanning many properties at once — they need
the signal, not the noise.

Your output follows the Signal-First Property Management Philosophy. Every
non-empty summary anchors itself to the Trifecta of Truth: Contract, Law,
Logic. You do not react to emotion, history, or speculation — only to the
contract, the statute, and the timeline.

GOLDEN RULE OF SUMMARIZATION
Every non-empty summary contains exactly these four elements, in this order:
  1. The specific issue (financial discrepancy / physical defect / behavioral complaint).
  2. The contractual anchor (Mietvertrag clause, Stammdaten value, or Hausordnung rule).
  3. The legal obligation (BGB §, HeizkostenV §, BetrKV §, BGH ruling — whichever applies).
  4. The timeline (date occurred, date reported, legal deadline).

OUTPUT FORMAT (strict)
- Prefix with a triage tag in brackets:
  - `[Emergency]` — threat to life, safety, or severe property damage
    (active flood, no heat in winter, structural collapse, gas leak).
  - `[Routine]` — standard operational issue (Mahnstufe 1, broken microwave,
    minor repair, lightbulb).
  - `[Administrative]` — paperwork, ledger, NK-Abrechnung query, address change.
- Maximum 3 sentences. Hard cap.
- Output language: German.
- Preserve `[(label)](url)` Markdown citations from the `references` input
  where they support a claim — they are the audit trail. Cite at most twice.
- If `signal` is empty, null, or all values are nominal/expected: respond with
  exactly `_no issue_` and nothing else.
- Forbidden: emotional adjectives, apologies that imply fault, gut-feel
  exceptions ("normalerweise", "kulanz"), invented facts, IDs not in input,
  speculation about tenant motivation.
- Do NOT use Markdown headings, code fences, or preamble. Output is the body
  text only — it will be inserted directly into a Markdown file.

INPUT FORMAT
You receive a JSON object with keys:
- `section` — which block this summary is for (e.g. "dunning", "tickets.critical").
- `signal` — pre-filtered facts already deemed salient by deterministic rules.
  Do NOT re-filter; assume every entry matters.
- `references` — list of `{"label": ..., "url": ...}`. Cite via `[(label)](url)`.
- `today` — reference date for legal deadlines (ISO YYYY-MM-DD).

EXAMPLES

Example 1 — input:
{"section": "dunning",
 "signal": {"MIE-001": {"dunning.mahnstufe": 1, "dunning.months_overdue_count": 4,
   "dunning.offener_betrag_eur": 6704.0, "dunning.verzugszinsen_eur": 85.87,
   "lease.kaltmiete_eur": 1403.0, "lease.nk_vorauszahlung_eur": 273.0,
   "dunning.last_payment_date": "2025-12-01"}},
 "references": [{"label": "bank", "url": "https://example/bank.csv#TX-01"}],
 "today": "2026-04-25"}

Example 1 — output:
[Routine] Mieter MIE-001 ist seit vier Monaten im Verzug; offener Betrag 6.704,00 EUR \
zzgl. 85,87 EUR Verzugszinsen, letzte Zahlung 2025-12-01 [(bank)](https://example/bank.csv#TX-01). \
Vertraglich geschuldet sind monatlich 1.676,00 EUR (Kaltmiete 1.403,00 EUR + NK 273,00 EUR). \
Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB (Basiszins + 5pp); Mahnstufe 1, nächster Schritt: 2. Mahnung nach 14 Tagen.

Example 2 — input:
{"section": "dunning", "signal": {}, "references": [], "today": "2026-04-25"}

Example 2 — output:
_no issue_

Respond with JUST the markdown body. No headers, no code fences, no preamble.
"""


@dataclass
class Summarizer:
    """LLM client wrapper (Anthropic or Gemini). No-op when API keys are unset."""

    provider: Optional[str] = None  # "anthropic" | "gemini"
    client: Optional[Any] = None
    model: str = ""
    max_tokens: int = DEFAULT_MAX_TOKENS
    cache_path: Path = field(default_factory=lambda: DEFAULT_CACHE_PATH)
    _cache: dict[str, str] = field(default_factory=dict)
    _cache_loaded: bool = False

    @classmethod
    def from_env(cls, cache_path: Optional[Path] = None) -> "Summarizer":
        anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
        gemini_key = os.environ.get("GEMINI_API_KEY")

        if genai and gemini_key:
            genai.configure(api_key=gemini_key)
            return cls(
                provider="gemini",
                client=genai,
                model=os.environ.get("GEMINI_MODEL", DEFAULT_GEMINI_MODEL),
                cache_path=cache_path or DEFAULT_CACHE_PATH,
            )

        if Anthropic and anthropic_key:
            return cls(
                provider="anthropic",
                client=Anthropic(api_key=anthropic_key),
                model=os.environ.get("ANTHROPIC_MODEL", DEFAULT_ANTHROPIC_MODEL),
                cache_path=cache_path or DEFAULT_CACHE_PATH,
            )

        return cls(cache_path=cache_path or DEFAULT_CACHE_PATH)

    @property
    def enabled(self) -> bool:
        return self.client is not None

    def summarize(
        self,
        signal: dict[str, Any],
        *,
        section: str,
        fallback: str,
        references: Optional[list[dict[str, str]]] = None,
        today: Optional[str] = None,
    ) -> str:
        """Return an LLM-generated summary, or `fallback` if unavailable.

        The signal is the *already-filtered* salience payload. Cached on disk
        by SHA256 of inputs, so re-runs on unchanged data make no API calls.
        """
        if not self.enabled:
            return fallback

        payload: dict[str, Any] = {
            "section": section,
            "signal": signal,
            "references": references or [],
        }
        if today:
            payload["today"] = today

        key = self._key(payload)
        cached = self._lookup(key)
        if cached is not None:
            return cached

        try:
            if self.provider == "anthropic":
                resp = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    system=[{
                        "type": "text",
                        "text": SYSTEM_PROMPT,
                        "cache_control": {"type": "ephemeral"},
                    }],
                    messages=[{
                        "role": "user",
                        "content": json.dumps(payload, ensure_ascii=False, sort_keys=True),
                    }],
                )
                text = resp.content[0].text.strip() if resp.content else ""
            elif self.provider == "gemini":
                model = self.client.GenerativeModel(
                    model_name=self.model,
                    system_instruction=SYSTEM_PROMPT,
                )
                resp = model.generate_content(
                    json.dumps(payload, ensure_ascii=False, sort_keys=True),
                    generation_config={"max_output_tokens": self.max_tokens},
                )
                text = resp.text.strip()
            else:
                return fallback

            # -- Tavily Integration: Legal Fact-Checking --
            from .tavily import get_oracle
            import re
            oracle = get_oracle()
            if oracle.enabled and text:
                # Find citations like "§ 288 BGB" or "§286 BGB"
                citations = set(re.findall(r'§\s*\d+[a-z]?\s+[A-Z][a-zA-Z]+', text))
                for cit in citations:
                    alert = oracle.check_legal_citation(cit)
                    if alert:
                        text += f"\n\n> [!WARNING] **Tavily Legal Alert ({cit}):** {alert}"
                        break # One alert is enough to flag the block

            out = text or fallback
        except Exception:
            return fallback

        self._store(key, out)
        return out

    # ---------- cache ----------

    def _key(self, payload: dict[str, Any]) -> str:
        h = hashlib.sha256()
        h.update(self.model.encode("utf-8"))
        h.update(b"\x00")
        h.update(SYSTEM_PROMPT.encode("utf-8"))
        h.update(b"\x00")
        h.update(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        return h.hexdigest()

    def _ensure_loaded(self) -> None:
        if self._cache_loaded:
            return
        if self.cache_path.exists():
            try:
                self._cache = json.loads(self.cache_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                self._cache = {}
        self._cache_loaded = True

    def _lookup(self, key: str) -> Optional[str]:
        self._ensure_loaded()
        return self._cache.get(key)

    def _store(self, key: str, value: str) -> None:
        self._ensure_loaded()
        self._cache[key] = value
        try:
            self.cache_path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.cache_path.with_suffix(self.cache_path.suffix + ".tmp")
            tmp.write_text(
                json.dumps(self._cache, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            tmp.replace(self.cache_path)
        except OSError:
            pass


# ---------- module-level singleton ----------

_GLOBAL: Optional[Summarizer] = None


def get_summarizer() -> Summarizer:
    """Lazy-init singleton — block render fns reach for this."""
    global _GLOBAL
    if _GLOBAL is None:
        _GLOBAL = Summarizer.from_env()
    return _GLOBAL


def configure(summarizer: Summarizer) -> None:
    """Override the singleton (used by `run.py` to plumb a custom cache path)."""
    global _GLOBAL
    _GLOBAL = summarizer


__all__ = ["Summarizer", "get_summarizer", "configure", "SYSTEM_PROMPT"]
