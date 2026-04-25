"""Extractor layer: sources → events → facts."""

from .models import Event, Fact, JsonlWriter

__all__ = ["Event", "Fact", "JsonlWriter"]
