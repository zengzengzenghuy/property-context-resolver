"""Top-level extractor pipeline."""

from __future__ import annotations

from pathlib import Path
from typing import Iterator, Optional

from .identity import IdentityResolver
from .models import Event, Fact
from .sources import bank, emails, pdfs, stammdaten


SOURCES = [
    ("stammdaten", stammdaten.extract, False),  # no incremental for stammdaten
    ("bank", bank.extract, True),
    ("emails", emails.extract, True),
    ("invoices", pdfs.extract_invoices, True),
    ("letters", pdfs.extract_letters, True),
]

# Sources whose `extract()` accepts a `resolver` kwarg for at-extraction-time
# identity resolution (e.g. einheit_nr → EH-XXX from email bodies).
_RESOLVER_SOURCES = {"emails"}


def extract_all(
    root: Path,
    *,
    include_incremental: bool = False,
    resolver: Optional[IdentityResolver] = None,
) -> Iterator[tuple[str, Event, list[Fact]]]:
    """Yield (source_name, event, facts) tuples across all connectors.

    Per Sprint.md, incremental/ is the surgical-update fixture and is excluded from
    the v1 engine run unless include_incremental=True.
    """
    for name, fn, supports_incr in SOURCES:
        kwargs: dict = {}
        if supports_incr:
            kwargs["include_incremental"] = include_incremental
        if name in _RESOLVER_SOURCES and resolver is not None:
            kwargs["resolver"] = resolver
        for event, facts in fn(root, **kwargs):
            yield name, event, facts
