"""Resolve local paths to GitHub blob URLs for source_ref citations.

Per the architecture (Tech Stack: "context.md files live in git"), every fact
carries a citation back to its source. Those citations need to resolve in the
GitHub UI, not on a contributor's laptop. This module:

1. Auto-detects the GitHub blob base from `git remote get-url origin` and the
   current branch on first use.
2. Lets callers override via the `SOURCE_REF_BASE` env var or `configure()`.
3. Maps an absolute or repo-relative `Path` to `<base>/<rel>` and appends an
   optional fragment.

If we're outside a git repo or origin isn't a GitHub URL, we fall back to the
local absolute path so the pipeline still runs.
"""

from __future__ import annotations

import os
import re
import subprocess
from functools import lru_cache
from pathlib import Path
from typing import Optional


_HTTPS_REMOTE = re.compile(r"^https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/.]+)(?:\.git)?/?$")
_SSH_REMOTE = re.compile(r"^git@github\.com:(?P<owner>[^/]+)/(?P<repo>[^/.]+?)(?:\.git)?$")


_override: Optional[tuple[str, Path]] = None  # (base, repo_root)


def configure(base: Optional[str], repo_root: Optional[Path] = None) -> None:
    """Override the autodetected base. Call once before extraction starts."""
    global _override
    if base is None:
        _override = None
        return
    base = base.rstrip("/")
    root = (repo_root or _detect_repo_root() or Path.cwd()).resolve()
    _override = (base, root)


@lru_cache(maxsize=1)
def _detect_repo_root() -> Optional[Path]:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return Path(out.stdout.strip()).resolve()


@lru_cache(maxsize=1)
def _detect_origin_owner_repo() -> Optional[tuple[str, str]]:
    try:
        out = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True, text=True, check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    url = out.stdout.strip()
    for rx in (_HTTPS_REMOTE, _SSH_REMOTE):
        if m := rx.match(url):
            return m.group("owner"), m.group("repo")
    return None


@lru_cache(maxsize=1)
def _detect_branch() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, check=True,
        )
        b = out.stdout.strip()
        return b if b and b != "HEAD" else "main"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "main"


@lru_cache(maxsize=1)
def _autodetect() -> Optional[tuple[str, Path]]:
    if env := os.environ.get("SOURCE_REF_BASE"):
        return env.rstrip("/"), _detect_repo_root() or Path.cwd().resolve()
    repo_root = _detect_repo_root()
    if repo_root is None:
        return None
    owner_repo = _detect_origin_owner_repo()
    if owner_repo is None:
        return None
    owner, repo = owner_repo
    base = f"https://github.com/{owner}/{repo}/blob/{_detect_branch()}"
    return base, repo_root


def for_path(path: Path | str, fragment: Optional[str] = None) -> str:
    """Map a local artifact path to its GitHub blob URL (or fall back to abs path)."""
    p = Path(path).resolve()
    cfg = _override or _autodetect()
    if cfg is None:
        out = str(p)
    else:
        base, repo_root = cfg
        try:
            rel = p.relative_to(repo_root).as_posix()
            out = f"{base}/{rel}"
        except ValueError:
            out = str(p)
    if fragment:
        out = f"{out}#{fragment}"
    return out
