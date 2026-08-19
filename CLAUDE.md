# Working on the CoFHE docs

This repo is the Mintlify site behind cofhe-docs.fhenix.zone. It documents the live CoFHE system for external developers.

## The one rule that matters

STYLE.md is binding for all content. Read it before writing or editing any page. If a page you touch conflicts with STYLE.md, fix the page.

## Facts

- Never write a technical claim you have not verified against the current source of the relevant repo (cofhe, cofhesdk, teecryptor, zee-k-verifier) or the published packages. Docs drift is the failure mode this project exists to fix.
- Current behavior and future plans never mix. Future work lives in `deep-dive/research/future-plans.mdx`, labeled as such.
- The TEE (Teecryptor) is the current decryption architecture. The Threshold Network is a future plan only.
- No internal names: hostnames, cloud project names, environment names, deployment bundle names, feature flags.

## Mechanics

- Navigation lives in `docs.json`. A page not referenced there is invisible; check it when adding, renaming, or removing pages.
- Renaming or removing a page requires a redirect entry.
- Diagrams are Mermaid blocks in the page (see STYLE.md, Diagrams). Do not add or edit SVGs; designed SVGs come from the design pass and keep their Mermaid source in the repo.
- Code samples must compile or run against the currently published versions before they ship.

## Workflow

- Work is tracked in the Jira DOC project, one epic per site tab. Ticket summaries start with `[page-slug]`.
- Commit messages: single line, `[DOCS] <area>/<page-slug>: summary`.
- One page per commit on rewrite branches, so commits can be cherry-picked individually.
