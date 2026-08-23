#!/usr/bin/env python3
"""Stamp the shared Mermaid init directive into every mermaid block.

The house theme lives in scripts/mermaid-theme.json. This script inserts the
matching %%{init: ...}%% directive as the first line of every ```mermaid block
in the docs, replacing any existing init line, so all diagrams share one style
and the theme can be changed in one file.

Usage:
  python3 scripts/sync-mermaid-theme.py          # rewrite files in place
  python3 scripts/sync-mermaid-theme.py --check  # exit 1 if any block is out of date
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEME_FILE = ROOT / "scripts" / "mermaid-theme.json"
SKIP_DIRS = {"local", "node_modules", ".git", "snippets"}

BLOCK_RE = re.compile(r"(```mermaid[ \t]*\n)(.*?)(```)", re.DOTALL)
INIT_RE = re.compile(r"^%%\{init:.*\}%%\s*\n", re.DOTALL)


def directive() -> str:
    theme = json.loads(THEME_FILE.read_text())
    return "%%{init: " + json.dumps(theme, separators=(", ", ": ")) + "}%%\n"


def sync_text(text: str, init_line: str) -> str:
    def repl(m: re.Match) -> str:
        body = INIT_RE.sub("", m.group(2), count=1)
        return m.group(1) + init_line + body + m.group(3)

    return BLOCK_RE.sub(repl, text)


def main() -> int:
    check = "--check" in sys.argv
    init_line = directive()
    stale = []
    for path in sorted(ROOT.rglob("*.mdx")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        original = path.read_text()
        updated = sync_text(original, init_line)
        if updated != original:
            if check:
                stale.append(path.relative_to(ROOT))
            else:
                path.write_text(updated)
                print(f"updated {path.relative_to(ROOT)}")
    if check and stale:
        for p in stale:
            print(f"stale mermaid theme: {p}")
        print("Run: python3 scripts/sync-mermaid-theme.py")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
