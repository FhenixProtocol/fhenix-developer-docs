#!/usr/bin/env python3
"""Generate DIAGRAMS.md, the column matrix for every sequence diagram on the site.

The matrix is read from the .mdx files, never hand-maintained, so it cannot drift
from the diagrams it describes. Regenerate with:

    python3 scripts/diagram-columns.py > DIAGRAMS.md
"""
import re
import sys
from pathlib import Path

REPO = "https://github.com/FhenixProtocol/fhenix-developer-docs/blob/main/"
PREVIEW = "https://cofhe-docs.fhenix.zone/"

COLUMNS = [
    "Your app", "Client SDK", "Your contract", "TaskManager",
    "ZK Verifier", "Compute pipeline", "Teecryptor",
    "CT Server", "CommitmentRegistry",
]

# Diagrams that share the column vocabulary, in reading order.
REQUEST_FLOWS = [
    ("Encryption flow", "deep-dive/data-flows/encryption-request-flow"),
    ("FHE operation flow", "deep-dive/data-flows/fhe-operation-request-flow"),
    ("Decryption flow", "deep-dive/data-flows/decryption-request-flow"),
    ("ZK Verifier", "deep-dive/cofhe-components/zk-verifier"),
    ("Teecryptor", "deep-dive/cofhe-components/teecryptor"),
    ("CommitmentRegistry", "deep-dive/cofhe-components/commitment-registry"),
]

# Intro pages collapse the coprocessor into one column, per STYLE.md.
INTRO = [
    ("What is CoFHE", "get-started/introduction/what-is-cofhe"),
    ("Mental model", "client-sdk/introduction/mental-model"),
]

# Diagrams outside the vocabulary, with the reason they stay outside.
OUTSIDE = [
    ("Key management", "deep-dive/cofhe-components/key-management",
     "sequence", "A boot ceremony, not a request. Its actors have no counterpart."),
    ("Compute pipeline", "deep-dive/cofhe-components/compute-pipeline",
     "flowchart", "The internal structure of one component."),
    ("Architecture overview", "deep-dive/cofhe-components/overview",
     "flowchart", "The whole system at once, not a single flow."),
    ("Commitment version lifecycle", "deep-dive/cofhe-components/commitment-registry",
     "state", "A state machine for the version tag."),
]


def participants(slug):
    """Return the participant labels of a page's sequence diagram, in order."""
    text = Path(slug + ".mdx").read_text()
    for block in re.findall(r"```mermaid\n(.*?)```", text, re.S):
        if "sequenceDiagram" not in block:
            continue
        return [
            (m.group(2) or m.group(1)).strip()
            for m in re.finditer(
                r"^\s*participant\s+(\S+)(?:\s+as\s+(.*))?$", block, re.M
            )
        ]
    raise SystemExit(f"no sequence diagram found in {slug}.mdx")


def main():
    used = {name: set(participants(slug)) for name, slug in REQUEST_FLOWS}
    out = []
    w = out.append

    w("# Diagram columns")
    w("")
    w("Every sequence diagram on the site draws its columns from one list of components,")
    w("in one order. This page records which diagram uses which column. It is generated")
    w("from the pages themselves, so it always matches what is published.")
    w("")
    w("The rule behind it lives in [STYLE.md](STYLE.md), under \"Sequence diagram lanes\".")
    w("")
    w("## The columns")
    w("")
    for i, c in enumerate(COLUMNS, 1):
        w(f"{i}. {c}")
    w("")
    w("Columns 5 to 7 are the swap group: a page shows whichever of them it is about.")
    w("They stay in that order because it is the order a value meets them, which is")
    w("verified as an input, computed, then decrypted.")
    w("")
    w("## The matrix")
    w("")
    w("`on` means the flow reaches that component. A blank means it does not.")
    w("")
    heads = [n for n, _ in REQUEST_FLOWS]
    w("| Component | " + " | ".join(heads) + " | Total |")
    w("|---|" + "---|" * (len(heads) + 1))
    for c in COLUMNS:
        cells = ["on" if c in used[n] else "" for n in heads]
        w(f"| {c} | " + " | ".join(cells) + f" | {sum(1 for x in cells if x)}/{len(heads)} |")
    w("| **Active columns** | " + " | ".join(f"**{len(used[n])}**" for n in heads) + " | |")
    w("")
    w("`CommitmentRegistry` is the only component every flow reaches, because every")
    w("ciphertext is anchored there. `CT Server` is absent from the FHE operation flow")
    w("for a real reason: the FHE Engine writes the ciphertext store directly, while the")
    w("ZK Verifier and Teecryptor go through CT Server over HTTP.")
    w("")
    w("## For the design pass")
    w("")
    w("Mermaid cannot dim a single column, so the published diagrams show only the")
    w("columns each flow uses. A designed version that puts all nine columns on every")
    w("diagram greys the rest by hand. This is what each page would grey:")
    w("")
    w("| Diagram | Active | Greyed | Source |")
    w("|---|---|---|---|")
    for name, slug in REQUEST_FLOWS:
        grey = [c for c in COLUMNS if c not in used[name]]
        w(f"| [{name}]({PREVIEW}{slug}) | {len(used[name])} | "
          f"{', '.join(grey) if grey else 'none'} | [mdx]({REPO}{slug}.mdx) |")
    w("")
    w("Two pages carry five greys against four live columns. Worth deciding whether the")
    w("greyed treatment suits every diagram, or only the ones that stay dense.")
    w("")
    w("## Intro pages are different on purpose")
    w("")
    w("They collapse the whole coprocessor into a single `CoFHE` column. A reader meeting")
    w("the system for the first time does not need nine components to follow the story.")
    w("")
    w("| Page | Columns |")
    w("|---|---|")
    for name, slug in INTRO:
        w(f"| [{name}]({PREVIEW}{slug}) | " + ", ".join(participants(slug)) + " |")
    w("")
    w("## Diagrams outside the vocabulary")
    w("")
    w("| Diagram | Type | Why it stays outside |")
    w("|---|---|---|")
    for name, slug, kind, why in OUTSIDE:
        w(f"| [{name}]({PREVIEW}{slug}) | {kind} | {why} |")
    w("")
    w("## Regenerating")
    w("")
    w("```bash")
    w("python3 scripts/diagram-columns.py > DIAGRAMS.md")
    w("```")
    w("")
    w("Run it after adding, removing, or renaming any diagram column.")

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
