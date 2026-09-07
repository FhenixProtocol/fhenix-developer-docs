# Diagram columns

Every sequence diagram on the site draws its columns from one list of components,
in one order. This page records which diagram uses which column. It is generated
from the pages themselves, so it always matches what is published.

The rule behind it lives in [STYLE.md](STYLE.md), under "Sequence diagram lanes".

## The columns

1. Your app
2. Client SDK
3. Your contract
4. TaskManager
5. ZK Verifier
6. Compute pipeline
7. Teecryptor
8. CT Server
9. CommitmentRegistry

Columns 5 to 7 are the swap group: a page shows whichever of them it is about.
They stay in that order because it is the order a value meets them, which is
verified as an input, computed, then decrypted.

## The matrix

`on` means the flow reaches that component. A blank means it does not.

| Component | Encryption flow | FHE operation flow | Decryption flow | ZK Verifier | Teecryptor | CommitmentRegistry | Total |
|---|---|---|---|---|---|---|---|
| Your app | on |  | on | on |  |  | 3/6 |
| Client SDK | on |  | on | on | on |  | 4/6 |
| Your contract | on | on | on | on |  |  | 4/6 |
| TaskManager | on | on | on | on | on |  | 5/6 |
| ZK Verifier | on |  |  | on |  |  | 2/6 |
| Compute pipeline | on | on |  | on |  | on | 4/6 |
| Teecryptor |  |  | on |  | on | on | 3/6 |
| CT Server | on |  | on | on | on | on | 5/6 |
| CommitmentRegistry | on | on | on | on | on | on | 6/6 |
| **Active columns** | **8** | **4** | **7** | **8** | **5** | **4** | |

`CommitmentRegistry` is the only component every flow reaches, because every
ciphertext is anchored there. `CT Server` is absent from the FHE operation flow
for a real reason: the FHE Engine writes the ciphertext store directly, while the
ZK Verifier and Teecryptor go through CT Server over HTTP.

## For the design pass

Mermaid cannot dim a single column, so the published diagrams show only the
columns each flow uses. A designed version that puts all nine columns on every
diagram greys the rest by hand. This is what each page would grey:

| Diagram | Active | Greyed | Source |
|---|---|---|---|
| [Encryption flow](https://cofhe-docs.fhenix.zone/deep-dive/data-flows/encryption-request-flow) | 8 | Teecryptor | [mdx](https://github.com/FhenixProtocol/fhenix-developer-docs/blob/main/deep-dive/data-flows/encryption-request-flow.mdx) |
| [FHE operation flow](https://cofhe-docs.fhenix.zone/deep-dive/data-flows/fhe-operation-request-flow) | 4 | Your app, Client SDK, ZK Verifier, Teecryptor, CT Server | [mdx](https://github.com/FhenixProtocol/fhenix-developer-docs/blob/main/deep-dive/data-flows/fhe-operation-request-flow.mdx) |
| [Decryption flow](https://cofhe-docs.fhenix.zone/deep-dive/data-flows/decryption-request-flow) | 7 | ZK Verifier, Compute pipeline | [mdx](https://github.com/FhenixProtocol/fhenix-developer-docs/blob/main/deep-dive/data-flows/decryption-request-flow.mdx) |
| [ZK Verifier](https://cofhe-docs.fhenix.zone/deep-dive/cofhe-components/zk-verifier) | 8 | Teecryptor | [mdx](https://github.com/FhenixProtocol/fhenix-developer-docs/blob/main/deep-dive/cofhe-components/zk-verifier.mdx) |
| [Teecryptor](https://cofhe-docs.fhenix.zone/deep-dive/cofhe-components/teecryptor) | 5 | Your app, Your contract, ZK Verifier, Compute pipeline | [mdx](https://github.com/FhenixProtocol/fhenix-developer-docs/blob/main/deep-dive/cofhe-components/teecryptor.mdx) |
| [CommitmentRegistry](https://cofhe-docs.fhenix.zone/deep-dive/cofhe-components/commitment-registry) | 4 | Your app, Client SDK, Your contract, TaskManager, ZK Verifier | [mdx](https://github.com/FhenixProtocol/fhenix-developer-docs/blob/main/deep-dive/cofhe-components/commitment-registry.mdx) |

Two pages carry five greys against four live columns. Worth deciding whether the
greyed treatment suits every diagram, or only the ones that stay dense.

## Intro pages are different on purpose

They collapse the whole coprocessor into a single `CoFHE` column. A reader meeting
the system for the first time does not need nine components to follow the story.

| Page | Columns |
|---|---|
| [What is CoFHE](https://cofhe-docs.fhenix.zone/get-started/introduction/what-is-cofhe) | Your app, Client SDK, Your contract, CoFHE |
| [Mental model](https://cofhe-docs.fhenix.zone/client-sdk/introduction/mental-model) | Your app, Client SDK, Your contract, Host chain, CoFHE |

## Diagrams outside the vocabulary

| Diagram | Type | Why it stays outside |
|---|---|---|
| [Key management](https://cofhe-docs.fhenix.zone/deep-dive/cofhe-components/key-management) | sequence | A boot ceremony, not a request. Its actors have no counterpart. |
| [Compute pipeline](https://cofhe-docs.fhenix.zone/deep-dive/cofhe-components/compute-pipeline) | flowchart | The internal structure of one component. |
| [Architecture overview](https://cofhe-docs.fhenix.zone/deep-dive/cofhe-components/overview) | flowchart | The whole system at once, not a single flow. |
| [Commitment version lifecycle](https://cofhe-docs.fhenix.zone/deep-dive/cofhe-components/commitment-registry) | state | A state machine for the version tag. |

## Regenerating

```bash
python3 scripts/diagram-columns.py > DIAGRAMS.md
```

Run it after adding, removing, or renaming any diagram column.
