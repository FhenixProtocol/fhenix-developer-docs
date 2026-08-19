# Documentation Style Guide

This guide defines how we write content for cofhe-docs.fhenix.zone. It covers language only, not visual design. Every page, new or rewritten, should follow it. When an existing page conflicts with this guide, the guide wins.

The goal: docs that read like they were written by an engineer who understands the system and respects the reader's time. Our readers are developers with sharp eyes. They notice filler, they notice hedging, and they notice text that no human would write.

## Voice

- Write in second person. "You call `decryptForView`", not "the developer calls" or "one calls".
- Use active voice. "The FHE Engine computes the result", not "the result is computed".
- Use present tense for how the system works. "The SDK sends the request", not "the SDK will send".
- State facts plainly. If something is true, say it without softening. If something is uncertain or planned, say that explicitly. Never present a planned behavior as a current one.
- Be direct about limits and trade-offs. "FHE operations add gas overhead" builds more trust than hiding it.
- Explain the why in one short sentence when a rule would otherwise look arbitrary. Then stop.

## Sentences and paragraphs

- One idea per sentence. If a sentence needs three commas, split it.
- Lead with the point. The first sentence of a page, section, or paragraph carries its conclusion. Details follow.
- Keep paragraphs to 2-4 sentences. Prefer a list when you are enumerating.
- Cut every word that does not add meaning. "In order to" is "to". "It is important to note that" is nothing.
- Vary sentence length. A short sentence after a long one lands the point. A page of same-length sentences reads machine-made.
- Anticipate the reader's next question and answer it where it arises, not three sections later. If a step commonly confuses people, say so and resolve it on the spot.

## Words

Use the words developers actually use. Plain beats fancy, always.

Do not use these (and their relatives):

| Avoid | Use instead |
|---|---|
| leverage, utilize | use |
| seamless, effortless | (delete, or describe the actual behavior) |
| robust, powerful, cutting-edge, blazing | (delete) |
| delve, dive into | look at, see, read |
| comprehensive | complete, full |
| in order to | to |
| via | through, with (or keep "via" only for transport, for example "via HTTPS") |
| aforementioned, thereof, hereby | (rewrite) |
| simply, just, easily | (delete; if it were simple you would not need to say it) |
| Note that, It should be noted | (delete, or use a Note component) |

Marketing language belongs on the landing site, not in technical pages. One descriptive adjective per page is usually one too many.

## Punctuation and symbols

- No em dashes (—). Rewrite with a comma, a period, a colon, or parentheses.
- No decorative Unicode: no arrows (→) in prose, no checkmarks or crosses (✅ ❌), no sparkle characters. In tables, use words: "Shipped", "In progress", "Planned".
- Use straight quotes and apostrophes.
- Use the Oxford comma.
- Exclamation marks: at most one per tab, and preferably zero.

## Terminology

Define a term at its first use on a page, in a short parenthetical or half sentence, even when a glossary page exists. Readers land on pages from search; no page gets to assume the reader arrived in order.

One name per thing, used consistently. Canonical names:

| Term | Notes |
|---|---|
| CoFHE | The coprocessor as a whole. Not COFHE, not Cofhe. |
| Teecryptor | The TEE decryption service. Capitalized as a product name. |
| FHE Engine | The service that executes FHE operations. |
| FheOS Server | The service that verifies and queues incoming work. It does not execute FHE operations. |
| ZK Verifier | The input proof verification service. |
| TaskManager, CommitmentRegistry, ACL | Contract names, written as in the source. |
| `FHE.sol` | The Solidity library, in backticks when referring to the file or API. |
| `@cofhe/sdk` | The client SDK package, in backticks. "the SDK" after first mention on a page. |
| Threshold Network | The future MPC decryption network. Always framed as planned, never as current. |
| onchain, offchain | One word, no hyphen. |
| ciphertext, plaintext | One word. |
| handle | A reference to an encrypted value held by a contract. Do not mix with "hash" in prose; `ctHash` appears only as the code identifier. |
| testnet, mainnet | Lowercase. |

Do not use internal names in public docs: no hostnames, no GCP project names, no environment names (staging, rehearsal), no deployment bundle names like "aggregator", and no internal feature flags.

## Facts and claims

- Every technical claim must be true against the current code and the deployed system. If you cannot verify it, do not write it.
- Separate current from future. Current behavior lives in component and flow pages. Future work lives in the future plans page, clearly labeled.
- Security properties get extra care: only describe a control as active if it is enforced. Overstating a guarantee is worse than omitting it.
- Version numbers and package names must match what is published right now.

## Page structure

- Frontmatter: a short `title` and a one-sentence `description` that says what the page covers.
- Open with 1-3 sentences that tell the reader what this page explains and when they need it. No throat-clearing, no history lessons.
- Headings are short noun phrases in sentence case: "How decryption works", not "How Does The Decryption Process Work?".
- Order sections by what the reader needs first: what it is, how it works, how to use it, edge cases, reference.
- Use Mintlify components with intent: `<Note>` for things easy to miss, `<Warning>` for things that break, `<Tip>` for optional improvements, `<Steps>` for real sequences. A page full of callouts has none.
- Link the first mention of another concept to its page. Do not re-link the same target repeatedly in one page.

## Code samples

- Every sample must compile or run against the currently published versions. If it would not run when pasted, it does not ship.
- Show imports and setup once per page, then keep later snippets focused.
- Comments in samples explain why, not what. No numbered "step 1, step 2" comments; the surrounding text does that.
- Use realistic names (`counter`, `balance`, `vote`), not `foo` and `bar`.

## Diagrams

- While a page is in rewrite, diagrams are Mermaid blocks that encode the correct current flow. They are the source material for the designed SVG that replaces them.
- Actor names in diagrams use the canonical terminology above and must match the page text exactly.
- A diagram shows one flow. If it needs a legend to be understood, split it.

## Review checklist

Before a page ships, scan it for:

1. Any claim you could not defend with a line of code or a config entry.
2. Em dashes, decorative Unicode, and words from the avoid list.
3. Future behavior described in present tense.
4. A code sample that was not actually run or compiled.
5. Internal names (hosts, projects, environments, flags).
6. Sentences that make you read them twice. Rewrite those first.
