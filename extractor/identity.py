"""IdentityResolver — name | email | IBAN | phone | address → canonical_id.

Reads stammdaten directly (JSON preferred, CSV fallback) and builds:
- exact-match indexes on email, IBAN, phone digits, einheit_nr, address tuple
- a name index for fuzzy matching via difflib

Canonical ids:
    LIE-001 (liegenschaft), HAUS-NN (gebaeude), EH-NNN (einheit),
    EIG-NNN (eigentuemer), MIE-NNN (mieter), DL-NNN (dienstleister)
"""

from __future__ import annotations

import csv
import json
import re
import unicodedata
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable, Optional


@dataclass(frozen=True)
class Identity:
    canonical_id: str
    entity_type: str           # eigentuemer | mieter | dienstleister | einheit | liegenschaft | verwalter
    confidence: float          # 1.0 = exact, <1.0 = fuzzy
    matched_on: str            # "email" | "iban" | "name" | "address" | "einheit_nr" | "phone" | "verwalter_email"
    display_name: Optional[str] = None


# ---------- normalization helpers ----------

def _strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c))


def norm_name(s: str) -> str:
    s = _strip_accents(s.lower())
    s = re.sub(r"\b(herr|frau|firma|gmbh|ag|kg|e\.k\.|co\.|ltd\.?)\b", " ", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def norm_email(s: str) -> str:
    return s.strip().lower()


def norm_iban(s: str) -> str:
    return re.sub(r"\s+", "", s).upper()


def norm_phone(s: str) -> str:
    return re.sub(r"\D+", "", s or "")


def norm_addr(street: str, plz: str = "", ort: str = "") -> tuple[str, str, str]:
    return (
        re.sub(r"\s+", " ", _strip_accents((street or "").lower()).strip()),
        (plz or "").strip(),
        re.sub(r"\s+", " ", _strip_accents((ort or "").lower()).strip()),
    )


def _ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


# ---------- resolver ----------

class IdentityResolver:
    """Build once, query many. Stateless after construction."""

    def __init__(self, raw_root: Path):
        self.raw_root = Path(raw_root)
        self._stamm = self._load_stammdaten()

        # Exact-match indexes
        self._by_email: dict[str, Identity] = {}
        self._by_iban: dict[str, Identity] = {}
        self._by_phone: dict[str, Identity] = {}
        self._by_einheit_nr: dict[str, Identity] = {}
        self._by_address: dict[tuple[str, str, str], Identity] = {}

        # Fuzzy: list of (normalized_name, Identity) pairs
        self._names: list[tuple[str, Identity]] = []

        self._build()

    # --- load ---

    def _load_stammdaten(self) -> dict[str, Any]:
        json_path = self.raw_root / "stammdaten" / "stammdaten.json"
        if json_path.exists():
            return json.loads(json_path.read_text(encoding="utf-8"))
        # CSV fallback
        d: dict[str, Any] = {
            "liegenschaft": {},
            "gebaeude": [],
            "einheiten": _read_csv(self.raw_root / "stammdaten" / "einheiten.csv"),
            "eigentuemer": _read_csv(self.raw_root / "stammdaten" / "eigentuemer.csv"),
            "mieter": _read_csv(self.raw_root / "stammdaten" / "mieter.csv"),
            "dienstleister": _read_csv(self.raw_root / "stammdaten" / "dienstleister.csv"),
        }
        # Coerce einheit_ids list field
        for o in d["eigentuemer"]:
            if isinstance(o.get("einheit_ids"), str):
                o["einheit_ids"] = [v for v in o["einheit_ids"].split(";") if v]
        return d

    # --- build ---

    def _add(self, ident: Identity, *, name: Optional[str] = None,
             email: Optional[str] = None, iban: Optional[str] = None,
             phone: Optional[str] = None, einheit_nr: Optional[str] = None,
             address: Optional[tuple[str, str, str]] = None) -> None:
        if email:
            self._by_email[norm_email(email)] = ident
        if iban:
            self._by_iban[norm_iban(iban)] = ident
        if phone:
            p = norm_phone(phone)
            if p and len(p) >= 6:  # avoid garbage
                self._by_phone[p] = ident
        if einheit_nr:
            self._by_einheit_nr[einheit_nr.strip().upper().replace(" ", "")] = ident
        if address and address[0]:
            self._by_address[address] = ident
        if name:
            n = norm_name(name)
            if n:
                self._names.append((n, ident))

    def _build(self) -> None:
        # liegenschaft + verwalter
        lie = self._stamm.get("liegenschaft") or {}
        if lie:
            lid = Identity(lie.get("id", "LIE-001"), "liegenschaft", 1.0, "id",
                           display_name=lie.get("name"))
            self._add(
                lid,
                name=lie.get("name"),
                address=norm_addr(lie.get("strasse", ""), lie.get("plz", ""), lie.get("ort", "")),
                iban=lie.get("weg_bankkonto_iban"),
            )
            # verwalter as a separate entity
            verw = Identity("VERWALTER", "verwalter", 1.0, "verwalter_email",
                            display_name=lie.get("verwalter"))
            self._add(
                verw,
                name=lie.get("verwalter"),
                email=lie.get("verwalter_email"),
                phone=lie.get("verwalter_telefon"),
                iban=lie.get("verwalter_iban"),
                address=norm_addr(lie.get("verwalter_strasse", ""), lie.get("verwalter_plz", ""),
                                  lie.get("verwalter_ort", "")),
            )
            # ruecklage IBAN also points at the WEG
            if lie.get("ruecklage_iban"):
                self._by_iban[norm_iban(lie["ruecklage_iban"])] = lid

        # einheiten
        for u in self._stamm.get("einheiten", []):
            ident = Identity(u["id"], "einheit", 1.0, "id",
                             display_name=f"{u.get('einheit_nr')} ({u.get('lage')})")
            self._add(ident, einheit_nr=u.get("einheit_nr"))

        # eigentuemer
        for o in self._stamm.get("eigentuemer", []):
            display = o.get("firma") or f"{o.get('vorname','')} {o.get('nachname','')}".strip()
            ident = Identity(o["id"], "eigentuemer", 1.0, "id", display_name=display)
            self._add(
                ident,
                name=display,
                email=o.get("email"),
                iban=o.get("iban"),
                phone=o.get("telefon"),
                address=norm_addr(o.get("strasse", ""), o.get("plz", ""), o.get("ort", "")),
            )

        # mieter
        for t in self._stamm.get("mieter", []):
            display = f"{t.get('vorname','')} {t.get('nachname','')}".strip()
            ident = Identity(t["id"], "mieter", 1.0, "id", display_name=display)
            self._add(
                ident,
                name=display,
                email=t.get("email"),
                iban=t.get("iban"),
                phone=t.get("telefon"),
            )

        # dienstleister
        for d in self._stamm.get("dienstleister", []):
            display = d.get("firma") or d.get("ansprechpartner") or d["id"]
            ident = Identity(d["id"], "dienstleister", 1.0, "id", display_name=display)
            self._add(
                ident,
                name=d.get("firma"),
                email=d.get("email"),
                iban=d.get("iban"),
                phone=d.get("telefon"),
                address=norm_addr(d.get("strasse", ""), d.get("plz", ""), d.get("ort", "")),
            )
            if d.get("ansprechpartner"):
                # Contact-person name also resolves to the vendor
                self._names.append((norm_name(d["ansprechpartner"]), ident))

    # --- lookups ---

    def by_email(self, email: Optional[str]) -> Optional[Identity]:
        if not email:
            return None
        # Strip "Display Name <a@b>" wrappers
        if m := re.search(r"<([^>]+)>", email):
            email = m.group(1)
        return self._by_email.get(norm_email(email))

    def by_iban(self, iban: Optional[str]) -> Optional[Identity]:
        if not iban:
            return None
        return self._by_iban.get(norm_iban(iban))

    def by_phone(self, phone: Optional[str]) -> Optional[Identity]:
        if not phone:
            return None
        return self._by_phone.get(norm_phone(phone))

    def by_einheit_nr(self, nr: Optional[str]) -> Optional[Identity]:
        if not nr:
            return None
        return self._by_einheit_nr.get(nr.strip().upper().replace(" ", ""))

    def by_address(self, street: str, plz: str = "", ort: str = "") -> Optional[Identity]:
        return self._by_address.get(norm_addr(street, plz, ort))

    def by_name(self, name: Optional[str], *, threshold: float = 0.86) -> Optional[Identity]:
        """Exact normalized match first, then fuzzy via difflib."""
        if not name:
            return None
        q = norm_name(name)
        if not q:
            return None
        # Exact
        for n, ident in self._names:
            if n == q:
                return ident
        # Fuzzy
        best: Optional[tuple[float, Identity]] = None
        for n, ident in self._names:
            r = _ratio(q, n)
            if r >= threshold and (best is None or r > best[0]):
                best = (r, ident)
        if best is None:
            return None
        score, ident = best
        return Identity(ident.canonical_id, ident.entity_type, round(score, 3),
                        "name_fuzzy", ident.display_name)

    def resolve(
        self,
        *,
        email: Optional[str] = None,
        iban: Optional[str] = None,
        phone: Optional[str] = None,
        einheit_nr: Optional[str] = None,
        name: Optional[str] = None,
        address: Optional[tuple[str, str, str]] = None,
    ) -> Optional[Identity]:
        """Try strong signals first, then weaker ones. Returns the first hit."""
        for fn, kwargs in (
            (self.by_email, {"email": email}),
            (self.by_iban, {"iban": iban}),
            (self.by_einheit_nr, {"nr": einheit_nr}),
            (self.by_phone, {"phone": phone}),
        ):
            r = fn(**kwargs)
            if r:
                return r
        if address:
            r = self.by_address(*address)
            if r:
                return r
        return self.by_name(name)


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


__all__ = ["IdentityResolver", "Identity", "norm_email", "norm_iban", "norm_name", "norm_phone", "norm_addr"]
