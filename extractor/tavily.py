"""Tavily search client for legal and temporal fact-checking."""

import os
import re
from typing import Optional

try:
    from tavily import TavilyClient
except ImportError:
    TavilyClient = None  # type: ignore

class TavilyOracle:
    """Wrapper for Tavily search to fetch up-to-date legal and temporal facts."""
    
    def __init__(self) -> None:
        api_key = os.environ.get("TAVILY_API_KEY")
        if TavilyClient and api_key:
            self.client = TavilyClient(api_key=api_key)
        else:
            self.client = None
        self._cache: dict[str, Optional[str]] = {}

    @property
    def enabled(self) -> bool:
        return self.client is not None

    def ask(self, query: str) -> Optional[str]:
        """Performs a search and returns a direct answer."""
        if not self.enabled:
            return None
        if query in self._cache:
            return self._cache[query]
        try:
            response = self.client.search(query, search_depth="advanced", include_answer=True, max_results=3)
            answer = response.get("answer")
            self._cache[query] = answer
            return answer
        except Exception:
            self._cache[query] = None
            return None

    def get_ecb_base_rate(self) -> Optional[float]:
        """Fetch the current ECB base rate (Basiszinssatz nach § 247 BGB)."""
        answer = self.ask("Wie hoch ist der aktuelle Basiszinssatz der Deutschen Bundesbank?")
        if not answer:
            return None
        # Naive extraction of a percentage like 3.12 or 3,12
        match = re.search(r'(-?\d+[,.]\d{1,2})\s*%', answer)
        if match:
            val_str = match.group(1).replace(',', '.')
            try:
                return float(val_str)
            except ValueError:
                pass
        return None

    def check_legal_citation(self, citation: str) -> Optional[str]:
        """Check if a legal citation has recent amendments."""
        answer = self.ask(f"Gibt es in den letzten 12 Monaten wichtige Änderungen oder Novellen zu {citation}?")
        if answer and ("ja" in answer.lower() or "geändert" in answer.lower() or "novelle" in answer.lower()):
             return answer
        return None

    def check_mietspiegel(self, city: str, current_year: int) -> bool:
        """Check if there's a newer Mietspiegel."""
        answer = self.ask(f"Gibt es einen offiziellen Mietspiegel für {city} der neuer ist als {current_year}?")
        if answer and str(current_year + 1) in answer:
            return True
        return False

# Singleton
_ORACLE: Optional[TavilyOracle] = None

def get_oracle() -> TavilyOracle:
    """Lazy-init singleton."""
    global _ORACLE
    if _ORACLE is None:
        _ORACLE = TavilyOracle()
    return _ORACLE
