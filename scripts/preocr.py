"""Pre-OCR pass: cache `.txt` next to every PDF in raw/briefe and raw/rechnungen.

Per Sprint.md: try `pdfminer.six` first — many "scans" are actually digital PDFs
with a real text layer. Fall back to `pytesseract` only on PDFs where pdfminer
returns empty/near-empty text.

Usage:
    python scripts/preocr.py raw/
    python scripts/preocr.py raw/ --force         # ignore mtime, redo all
    python scripts/preocr.py raw/ --no-ocr        # skip pytesseract fallback

Outputs `<pdf>.pdf.txt` siblings. The pipeline reads these in pdfs.py.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


# Threshold below which we consider pdfminer's output "empty" and try OCR.
_MIN_TEXT_CHARS = 40


@dataclass
class Result:
    path: Path
    method: str          # "cached" | "pdfminer" | "ocr" | "skipped" | "failed"
    chars: int = 0
    error: Optional[str] = None


# ---------- extractors ----------

def _pdfminer_text(path: Path) -> Optional[str]:
    try:
        from pdfminer.high_level import extract_text  # type: ignore
    except ImportError:
        return None
    try:
        return extract_text(str(path)) or ""
    except Exception:
        return None


def _ocr_text(path: Path) -> Optional[str]:
    """OCR fallback. Requires pytesseract + pdf2image + system poppler + tesseract."""
    try:
        import pytesseract  # type: ignore
        from pdf2image import convert_from_path  # type: ignore
    except ImportError:
        return None
    try:
        images = convert_from_path(str(path), dpi=200)
    except Exception as e:
        # Most likely cause: poppler not installed
        print(f"  ocr: convert_from_path failed: {e}", file=sys.stderr)
        return None
    pages: list[str] = []
    for img in images:
        try:
            pages.append(pytesseract.image_to_string(img, lang="deu+eng"))
        except Exception as e:
            print(f"  ocr: tesseract failed on {path.name}: {e}", file=sys.stderr)
            return None
    return "\n".join(pages)


# ---------- driver ----------

def _is_fresh(pdf: Path, txt: Path) -> bool:
    return txt.exists() and txt.stat().st_mtime >= pdf.stat().st_mtime


def process_pdf(pdf: Path, *, force: bool, allow_ocr: bool) -> Result:
    txt = pdf.with_suffix(pdf.suffix + ".txt")  # <name>.pdf.txt

    if not force and _is_fresh(pdf, txt):
        return Result(pdf, "cached", chars=txt.stat().st_size)

    text = _pdfminer_text(pdf)
    if text is not None and len(text.strip()) >= _MIN_TEXT_CHARS:
        txt.write_text(text, encoding="utf-8")
        return Result(pdf, "pdfminer", chars=len(text))

    if allow_ocr:
        ocr = _ocr_text(pdf)
        if ocr and len(ocr.strip()) >= _MIN_TEXT_CHARS:
            txt.write_text(ocr, encoding="utf-8")
            return Result(pdf, "ocr", chars=len(ocr))

    if text is None:
        return Result(pdf, "failed", error="pdfminer.six not installed")
    return Result(pdf, "skipped", error=f"only {len(text.strip())} chars from pdfminer")


def walk_pdfs(root: Path) -> list[Path]:
    pdfs: list[Path] = []
    for kind in ("briefe", "rechnungen"):
        d = root / kind
        if d.exists():
            pdfs.extend(sorted(d.rglob("*.pdf")))
    inc = root / "incremental"
    if inc.exists():
        for day in sorted(inc.glob("day-*")):
            for kind in ("briefe", "rechnungen"):
                kd = day / kind
                if kd.exists():
                    pdfs.extend(sorted(kd.rglob("*.pdf")))
    return pdfs


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="preocr")
    p.add_argument("raw", help="path to raw/ directory")
    p.add_argument("--force", action="store_true", help="redo even if .txt is newer than .pdf")
    p.add_argument("--no-ocr", action="store_true", help="skip pytesseract OCR fallback")
    p.add_argument("--limit", type=int, default=None, help="process at most N PDFs (smoke test)")
    args = p.parse_args(argv)

    root = Path(args.raw).resolve()
    pdfs = walk_pdfs(root)
    if args.limit:
        pdfs = pdfs[: args.limit]

    counts = {"cached": 0, "pdfminer": 0, "ocr": 0, "skipped": 0, "failed": 0}
    samples: dict[str, str] = {}
    for i, pdf in enumerate(pdfs, 1):
        r = process_pdf(pdf, force=args.force, allow_ocr=not args.no_ocr)
        counts[r.method] += 1
        if r.method not in samples:
            samples[r.method] = f"{r.path.name} ({r.chars} chars{', ' + r.error if r.error else ''})"
        if i % 50 == 0:
            print(f"  ... {i}/{len(pdfs)}")

    print(f"\nProcessed {len(pdfs)} PDFs:")
    for k in ("cached", "pdfminer", "ocr", "skipped", "failed"):
        if counts[k]:
            print(f"  {k:<10} {counts[k]:>5}    e.g. {samples.get(k, '')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
