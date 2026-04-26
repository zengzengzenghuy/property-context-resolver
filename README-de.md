# property-context-resolver

<p align="center">
  <img src="./logo.png" alt="buena-context-buddy logo" width="50%" />
</p>

🌐 **Sprache:** [English](./README.md) · **Deutsch** · [中文](./README-cn.md)

Verwandelt das Chaos der Hausverwaltungs-Artefakte — E-Mails, eingescannte
Briefe, Lieferantenrechnungen, Kontoauszüge, Stammdaten-CSVs — in eine
auditierbare `context.md` pro Liegenschaft und pro Einheit, mit chirurgischen
Updates, die menschliche Bearbeitungen über Läufe hinweg erhalten.

Die Demo-Liegenschaft ist `LIE-001` (WEG Immanuelkirchstraße 26, Berlin) mit
einem Flagship-Mieter im Mahnverfahren (`MIE-001`).

## Warum das für Hausverwalter zählt

- **Ein auditierbares Dossier pro Liegenschaft.** Stammdaten, E-Mails, Briefe,
  Rechnungen, Kontoauszüge → eine `context.property.<ID>.md` + eine
  `context.unit.<EH>.md` pro Einheit. Identitäten (`Eigentümer` /
  `MietEig` / `Kontakt`) werden über E-Mail, IBAN, Einheit-Nr. aufgelöst.
- **Chirurgische Updates, keine Voll-Regeneration.** Der Merger schreibt nur
  innerhalb der `<!-- auto:NAME -->`-Blöcke — handgepflegte Notizen und
  WEG-Beschlüsse bleiben Lauf für Lauf erhalten.
- **Signal-First mit Beweis.** Deterministische Filter pro Sektion lassen
  nur relevante Fakten zum LLM; jede gerenderte Zeile zitiert ihre Quelle
  als klickbare GitHub-URL. Der Rechtsstand bleibt aktuell via TavilyOracle
  (§ 247 BGB Basiszinssatz, BGB-Novellen, Berliner Mietspiegel).

## Was es macht

Die Pipeline liest ein `raw/`-Verzeichnis ein, löst Identitäten quellenüber-
greifend auf, dedupliziert und erkennt Konflikte zwischen Fakten, gleicht das
Zahlungsbuch eines Mieters mit dem Mietvertrag ab und rendert ein Markdown-
Dossier pro Liegenschaft + pro Einheit im `spine-v2-split`-Schema. Jeder Fakt
trägt eine Quellenangabe zurück zur Originaldatei (standardmäßig eine GitHub-
Blob-URL, automatisch erkannt aus `git remote`), sodass jede Zeile in
`context.md` byte-genau auditierbar ist.

Ein zweiter Lauf — der LLM-**Summarizer** — verarbeitet deterministisch vor-
gefilterte „Signal"-Payloads (Anomalien, Konflikte, Posten mit Fristen) und
emittiert dreisätzige deutsche Zusammenfassungen innerhalb dedizierter
`<!-- auto:*.summary -->`-Blöcke. Die Zusammenfassungen folgen der
**Signal-First Property Management Philosophy**: Jede nicht-leere Zusammen-
fassung enthält genau vier Elemente (Sachverhalt, Vertragsklausel, gesetzliche
Pflicht, Frist) und beginnt mit einem Triage-Tag (`[Emergency]` / `[Routine]`
/ `[Administrative]`).

## Architektur

```
raw/                            extractor/                            out/
─────                           ──────────                            ─────
stammdaten/  ─┐                                                       events.jsonl
emails/      ─┤   SourceLoader → NoiseFilter → FactExtractor          facts.jsonl
briefe/      ─┼─►        │             │             │           ┌──► llm_cache/
rechnungen/  ─┤          ▼             ▼             ▼           │    summary.json
bank/        ─┘   (Event, [Fact])  (Filterregeln) (Identitäts-   │
                                                    Anreicherung)│
                                       │                         │
                                       ▼                         │
                                   FactStore                     │
                                   (append-only,                 │
                                    JSONL-Audit-Log,             │  context.property.LIE-001.md
                                    Konflikterkennung)           │  context.unit.EH-XXX.md
                                       │                         │      ▲
                                       ▼                         │      │
                              DunningReconciler ─► ┐             │      │
                              PropertyAggregator ─►├─► dunning.* │      │
                                                   │   operations.*     │
                                       │           │   Fakten           │
                                       ▼                                │
                                PropertyMerger / UnitMerger ────────────┘
                                     │       (Block-Registry: blocks.py)
                                     ▼
                                Summarizer ◄── GEMINI_API_KEY (Standard)
                                (Signal-First, gecached) │  ANTHROPIC_API_KEY (Fallback)
                                     │
                                     │  ◄── TavilyOracle (optional)
                                     │       Live-EZB-Basiszinssatz · § BGB
                                     │       Novellen-Hinweise · Mietspiegel-
                                     │       Aktualitätsprüfung
                                     ▼
                                  Supabase (optionaler Mirror, no-op ohne Keys)
```

### Komponenten

| #   | Modul                                                      | Rolle                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `extractor/sources/*`                                      | Ein Connector pro Quellenart (stammdaten / emails / briefe / rechnungen / bank). Liefert `(Event, [Fact])`.                                                                                                                                                                                                                                                                                                                                                       |
| 2   | `extractor/identity.py`                                    | `IdentityResolver` — exakter Match auf E-Mail/IBAN/einheit_nr/Telefon, danach Fuzzy-Namensvergleich (`difflib`, Schwelle 0.86).                                                                                                                                                                                                                                                                                                                                   |
| 3   | `extractor/engine.py::NoiseFilter`                         | Verwirft Auto-ACKs und andere Nicht-Signal-Events. Aktuell Stub; Erweiterung um Quoted-Reply- / Signatur-Stripping geplant.                                                                                                                                                                                                                                                                                                                                       |
| 4   | `extractor/engine.py::FactExtractor`                       | Reichert jeden Fakt mit Identität an. Hooks für LLM-basierte Anreicherung (aktuell leer).                                                                                                                                                                                                                                                                                                                                                                         |
| 5   | `extractor/engine.py::FactStore`                           | Index nach `(entity_id, key)`-Buckets, append-only-Dedup, Konflikterkennung am Confidence-Floor 0.7, Tie-Break auf confidence > observed_at > Quellenpriorität > extracted_at. JSONL-Roundtrip.                                                                                                                                                                                                                                                                   |
| 6   | `extractor/engine.py::DunningReconciler`                   | Mieter-spezifischer Abgleich des Zahlungsbuchs gegen `kaltmiete + nk_vorauszahlung`. Emittiert `dunning.*`-Fakten (mahnstufe, months_overdue, offener_betrag, verzugszinsen), verankert in § 286 / § 288 BGB.                                                                                                                                                                                                                                                     |
| 7   | `extractor/aggregator.py`                                  | `PropertyAggregator` — emittiert `operations.*`-Fakten auf `LIE-001` aus dem Status der Einheiten (Vermietet/Leerstand/Eigennutzung-Zähler, aktive Mahnverfahren, ausstehende Übergaben). Siehe `engine.aggregation-rules.md` §5.1.                                                                                                                                                                                                                               |
| 8   | `extractor/merger.py` + `blocks.py`                        | `PropertyMerger` / `UnitMerger` — chirurgisches Update der `<!-- auto:NAME -->`-Blöcke. Jeder Block ist eine `(store, ctx) -> str`-Renderfunktion, registriert in `PROPERTY_BLOCKS` / `UNIT_BLOCKS`. Alles außerhalb der Auto-Blöcke bleibt zwischen Läufen unangetastet.                                                                                                                                                                                         |
| 9   | `extractor/summarizer.py`                                  | LLM-Zusammenfassung für `<!-- auto:*.summary -->`-Blöcke. Bevorzugt Gemini (`GEMINI_API_KEY`), fällt auf Anthropic Claude (`ANTHROPIC_API_KEY`) zurück. Signal-First-Philosophie im System-Prompt; vorgefilterte Signal-Payloads deterministisch in `blocks.py` aufgebaut. Datei-gecached unter `out/llm_cache/summary.json`. No-op, wenn kein Provider-Key gesetzt ist.                                                                                          |
| 10  | `extractor/section_summary.py` + `extractor/raw_loader.py` | Factory `make_section_summary(filter, include_raw=...)` für die meisten `*.summary`-Blöcke; `raw_loader.gather_excerpts` löst `source_ref`-URLs zurück zu begrenzten lokalen Auszügen (`.eml` / `.pdf.txt` / Bankzeilen / Stammdaten-Fragmente), damit das LLM-Payload echten Inhalt enthält, nicht nur Fakten.                                                                                                                                                   |
| 11  | `extractor/tavily.py`                                      | `TavilyOracle` — optionale Schicht für rechtliche/zeitliche Faktenprüfung. Eingebunden in `DunningReconciler` (Live-EZB-Basiszinssatz überschreibt den hartkodierten Wert von 3,5pp), `Summarizer` (scannt die Ausgabe nach `§ BGB`-Zitaten und hängt `[!WARNING] Tavily Legal Alert` an, wenn Novellen gefunden werden) und `PropertyAggregator` (emittiert `operations.context_outdated`, wenn ein neuerer Mietspiegel existiert). No-op ohne `TAVILY_API_KEY`. |
| 12  | `extractor/sb.py`                                          | `SupabaseSink` — spiegelt das gerenderte Markdown unter `spine-v2-split` nach Supabase. No-op, wenn die Keys nicht gesetzt sind.                                                                                                                                                                                                                                                                                                                                  |

### Wichtige Designentscheidungen

- **JSONL-Audit-Log statt Postgres.** Der Fact-Store ist append-only;
  Wieder-Beobachtung hängt eine neue Zeile an. `latest()` und `conflicts()`
  arbeiten auf dem In-Memory-Index, der aus dem Log aufgebaut wird.
  Reproduzierbar ohne DB.
- **GitHub-Blob-URLs als `source_ref`.** Automatisch erkannt aus
  `git remote` + aktuellem Branch; Fallback auf absoluten lokalen Pfad
  außerhalb eines Git-Repos, sodass die Pipeline nie bricht. Override via
  `--source-ref-base` oder `SOURCE_REF_BASE`.
- **Chirurgische Markdown-Updates.** Der Merger schreibt nur innerhalb der
  `<!-- auto:NAME -->` ... `<!-- /auto:NAME -->`-Blöcke. Freier Prosa-Text,
  menschliche Notizen und `## Human Notes`-Abschnitte bleiben über Läufe
  hinweg erhalten.
- **PDFs laufen über einen Pre-OCR-Cache.** `scripts/preocr.py` schreibt
  `<file>.pdf.txt`-Geschwisterdateien; die Engine liest diese zuerst und
  fällt nur bei Bedarf auf live `pdfminer.six` zurück. Der Cache ist in
  Git eingecheckt, sodass die Engine ohne installiertes `pdfminer.six`
  reproduzierbar bleibt.
- **Das LLM macht Prosa, nicht Filtern.** Der Summarizer sieht nie Rohdaten —
  Salience-Extraktoren in `blocks.py` (z. B. `_dunning_signal()`) filtern
  vor nach Confidence-Floor, Key-Allowlist, Aktualität und Anomalie-Status.
  Das LLM produziert ≤3 deutsche Sätze mit den vier Trifecta-Elementen
  (Sachverhalt / Vertrag / Gesetz / Frist) und behält
  `[(label)](url)`-Zitate bei.
- **Single-Property-Scope.** `PROPERTY_ID = "LIE-001"` ist hartkodiert in
  `extractor/models.py`. Keine Multi-Tenancy, keine Authentifizierung,
  keine Vector-DB.

## Tavily-Integration

Tavily ist als „Legal & Temporal Oracle" eingebunden, damit die Pipeline
keine Empfehlungen auf Basis veralteter Gesetze oder hartkodierter Finanz-
konstanten ausliefert. Alle drei Hooks sind no-op, wenn `TAVILY_API_KEY`
nicht gesetzt ist.

### 1. Der `TavilyOracle`-Client (`extractor/tavily.py`)

Schlanker Wrapper um `tavily.TavilyClient` mit `search_depth="advanced"` und
`include_answer=True`, plus In-Process-Query-Cache. Singleton-Zugriff:
`get_oracle()`.

### 2. Dynamischer EZB-Basiszinssatz (Mahnwesen)

`DunningReconciler.__post_init__` (`extractor/engine.py:410`) ruft
`oracle.get_ecb_base_rate()` auf und überschreibt den hartkodierten
`ECB_BASE_PP = 3.5`, wenn ein Live-Wert zurückkommt — so spiegelt
`verzugszinsen_eur` den aktuellen Satz nach § 247 BGB wider.

### 3. Hinweise auf Gesetzes-Novellen (Summarizer)

Nachdem das LLM einen `<!-- auto:*.summary -->`-Block gerendert hat, scannt
`Summarizer.summarize()` (`extractor/summarizer.py:228`) die Ausgabe nach
`§ <n> <Gesetz>`-Zitaten und fragt Tavily, ob diese in den letzten 12 Monaten
geändert wurden. Der erste Treffer wird als
`> [!WARNING] **Tavily Legal Alert (§ N BGB):** ...`-Callout unter die
Zusammenfassung gehängt.

### 4. Aktualitätswächter für den Kontext (Aggregator)

`PropertyAggregator.emit_for_property` (`extractor/aggregator.py:164`) ruft
`oracle.check_mietspiegel("Berlin", year-1)` auf und emittiert
`operations.context_outdated`, wenn ein neuerer Mietspiegel existiert — so
zeigt das Property-Dashboard veraltete lokale Referenzen an.

## Build

Erfordert Python 3.11+. Optionale System-Abhängigkeit: `tesseract` (nur, wenn
OCR-Fallback für gescannte PDFs gewünscht ist — für das mitgelieferte Korpus
dank Pre-OCR-Cache nicht nötig).

```bash
# 1. Python-Abhängigkeiten installieren
pip install -r requirements.txt

# 2. Secrets in .env hinterlegen (alle Einträge optional — Module degradieren sauber)
cat > .env <<'EOF'
GEMINI_API_KEY=...                      # Standard-LLM für Summary-Blöcke
ANTHROPIC_API_KEY=sk-ant-api03-...      # Fallback-LLM, wenn GEMINI_API_KEY fehlt
TAVILY_API_KEY=tvly-...                 # aktiviert Live-EZB-Satz + Novellen-Hinweise
SUPABASE_URL=https://...supabase.co     # aktiviert den Supabase-Mirror
SUPABASE_SERVICE_KEY=eyJhbGc...
EOF

# 3. PDF-Text-Cache (neu) bauen — nur nötig, wenn der PDF-Bestand sich ändert
python scripts/preocr.py raw/
```

`pdfminer.six` ist die einzige zwingende Runtime-Abhängigkeit; alles andere
(`pytesseract`, `pdf2image`, `pypdf`, `supabase`, `python-dotenv`,
`anthropic`) ist optional — abhängige Module sind no-op, wenn Imports
fehlschlagen oder Env-Variablen fehlen.

## Ausführung

End-to-End-Pipeline:

```bash
# Standardmäßiger v1-Lauf — nur Archiv, keine inkrementellen Delta-Drops
python run.py raw/

# Referenzdatum fixieren, damit gesetzliche Fristen (§ 288 BGB Verzugszinsen etc.)
# deterministisch berechnet werden — fließt auch in den LLM-Summary-Prompt ein
python run.py raw/ --today 2026-04-25

# Zweiter Lauf mit Delta-Drops zur Demonstration der chirurgischen Updates
# (lädt zuerst out/facts.jsonl, sodass die Historie in die Konflikterkennung eingeht)
python run.py raw/ --include-incremental --today 2026-04-25
```

Outputs:

```
out/
  events.jsonl                  eine Zeile pro Source-Event
  facts.jsonl                   das vollständige append-only-Faktenlog
  llm_cache/summary.json        deterministischer Cache der LLM-Summary-Outputs
  raw_bundle.txt                Konkatenation des Rohtexts zur Inspektion
context.property.LIE-001.md     Dossier auf Liegenschafts-Ebene
context.unit.EH-XXX.md          Dossier pro Einheit (eines pro Einheit)
```

Der erste Lauf scaffoldet die Markdown-Dateien aus
`context.property.template.md` / `context.unit.template.md`. Folgeläufe
aktualisieren nur die Bodies der Auto-Blöcke — alles außerhalb dieser Blöcke
(inkl. eines manuell gepflegten `## Human Notes`-Abschnitts) bleibt erhalten.

### Neuen Auto-Block nach dem ersten Lauf hinzufügen

Der Merger **scaffoldet** neue Blöcke nur in eine frische Datei. Wenn du
einen neuen Block in `PROPERTY_BLOCKS` / `UNIT_BLOCKS` registrierst, nachdem
die Dateien bereits gerendert wurden, lösche die betroffenen Dateien, damit
sie aus dem Template neu scaffolden:

```bash
rm context.unit.*.md context.property.*.md
python run.py raw/ --today 2026-04-25
```

### Tests

```bash
python -m unittest tests.test_factstore -v       # ein Modul, ausführlich
python -m unittest discover tests                # alles
```

Stdlib `unittest`, kein zusätzlicher Runner. Die Testdatei verwendet oben
einen `make_fact()`-Helper — beim Hinzufügen neuer Cases dieses Muster kopieren.

## Konfiguration

| Variable                                | Verwendet von             | Effekt, wenn nicht gesetzt                                                                          |
| --------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------- |
| `GEMINI_API_KEY`                        | `extractor/summarizer.py` | aktiviert Gemini-Summaries; fehlt sie, wird auf `ANTHROPIC_API_KEY` zurückgegriffen.                |
| `ANTHROPIC_API_KEY`                     | `extractor/summarizer.py` | aktiviert Claude-Summaries; wird verwendet, wenn `GEMINI_API_KEY` fehlt.                            |
| `TAVILY_API_KEY`                        | `extractor/tavily.py`     | aktiviert Live-Prüfung rechtlicher/zeitlicher Fakten; fehlt sie, gelten die hartkodierten Defaults. |
| `SUPABASE_URL` + `SUPABASE_SERVICE_KEY` | `extractor/sb.py`         | Supabase-Mirror wird übersprungen; lokales Markdown wird trotzdem geschrieben.                      |
| `SOURCE_REF_BASE`                       | `extractor/source_ref.py` | Auto-Erkennung aus `git remote` + aktuellem Branch; Fallback auf lokalen absoluten Pfad.            |

CLI-Flags von `run.py`:

| Flag                    | Standard       | Zweck                                                                 |
| ----------------------- | -------------- | --------------------------------------------------------------------- |
| `raw`                   | (erforderlich) | Pfad zum `raw/`-Korpus.                                               |
| `--out`                 | `out`          | Output-Verzeichnis für `events.jsonl` / `facts.jsonl` / `llm_cache/`. |
| `--repo-root`           | `cwd`          | Wo `context.{property,unit}.*.md` geschrieben werden.                 |
| `--include-incremental` | aus            | Walked `raw/incremental/` (das Fixture für den zweiten Lauf).         |
| `--source-ref-base`     | (auto-erkannt) | Überschreibt die GitHub-Blob-Basis für Zitate.                        |
| `--today`               | Systemdatum    | Referenzdatum für Mahnzinsen + LLM-Rechtsfristen.                     |

## Repo-Layout

```
raw/                           unveränderliches Input-Korpus
extractor/                     die Engine
  models.py                    Event- + Fact-Dataclasses, JsonlWriter
  identity.py                  IdentityResolver
  source_ref.py                lokaler Pfad → GitHub-Blob-URL
  engine.py                    SourceLoader / NoiseFilter / FactExtractor
                               / FactStore / DunningReconciler / format_value
  aggregator.py                PropertyAggregator (engine.aggregation-rules.md §5.1)
  merger.py                    PropertyMerger + UnitMerger (chirurgische Updates)
  blocks.py                    Block-Render-Registry (PROPERTY_BLOCKS / UNIT_BLOCKS)
  section_summary.py           generische make_section_summary(...)-Factory
  raw_loader.py                source_ref → begrenzte lokale Auszüge für LLM-Payloads
  summarizer.py                Gemini-Standard / Claude-Fallback LLM-Wrapper, datei-gecached
  tavily.py                    TavilyOracle — Live-EZB-Satz, § BGB Novellen-Hinweise,
                               Mietspiegel-Aktualitätsprüfung (no-op ohne TAVILY_API_KEY)
  sb.py                        Supabase-Mirror
  extract.py                   Fan-out über Source-Connectors
  sources/                     ein Connector pro Quellenart (stammdaten/emails/
                               briefe/rechnungen/bank)
  cli.py                       `python -m extractor.cli ingest`
context.property.template.md   Markdown-Skelett pro Liegenschaft
context.unit.template.md       Markdown-Skelett pro Einheit
engine.aggregation-rules.md    PropertyAggregator §5.1 Spezifikation
scripts/preocr.py              Pre-OCR-Cache-Builder
scripts/upload_raw_bundle.py   lädt out/raw_bundle.txt nach Supabase hoch
supabase/                      Schema- + Edge-Function-Scaffold für den Mirror
run.py                         End-to-End-Treiber
tests/test_factstore.py        Stdlib-unittest — FactStore + format_value
tests/test_dunning.py          DunningReconciler Zinsen + Mahnstufen-Abdeckung
tests/test_merger.py           PropertyMerger / UnitMerger chirurgische Updates
```

## Weiterführende Lektüre

- **`CLAUDE.md`** — operative Hinweise, Konventionen und Fallstricke (das _Wie_).
- **`engine.aggregation-rules.md`** — `PropertyAggregator` §5.1 Spezifikation.
