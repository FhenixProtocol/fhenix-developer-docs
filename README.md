# Fhenix Developer Documentation

Official documentation for Fhenix - the privacy-preserving blockchain platform that enables developers to build confidential smart contracts using Fully Homomorphic Encryption (FHE).

## About This Documentation

This repository contains the complete developer documentation for Fhenix, including:

- **Get Started** - Introduction to Fhenix and CoFHE, compatibility, support, and builder programs
- **Client SDK** - `@cofhe/sdk` for encrypting inputs, managing Access Control Permissions, and decrypting outputs, plus the Hardhat and Foundry plugins
- **FHE library** - `FHE.sol`, the Solidity library for working with encrypted data in smart contracts
- **Tutorials** - Step-by-step guides for building FHE-enabled applications
- **Deep Dive** - Technical architecture details, CoFHE components, and data flows

## Development

This documentation is built using [Mintlify](https://mintlify.com/). To preview the documentation locally:

### Prerequisites

Install the [Mintlify CLI](https://www.npmjs.com/package/mint):

```bash
npm i -g mint
```

### Running Locally

Run the following command at the root of the documentation directory:

```bash
mint dev
```

The documentation will be available at `http://localhost:3000`.

## Project Structure

```
fhenix-developer-docs/
├── get-started/          # Introduction and getting started guides
├── client-sdk/           # @cofhe/sdk, Hardhat plugin, and Foundry plugin docs
├── fhe-library/          # Solidity FHE library documentation
├── tutorials/            # Step-by-step tutorials
├── deep-dive/            # Architecture and technical deep dives
├── images/               # Images referenced from pages
├── scripts/              # Structure linter (lint-docs.py)
├── styles/               # Vale prose rules
├── STYLE.md              # Writing style guide, binding for all pages
└── docs.json             # Mintlify configuration
```

## Publishing Changes

Changes pushed to the default branch are automatically deployed to production through the Mintlify GitHub app integration.

## Contributing

We welcome contributions to improve the documentation. When making changes:

1. Read `STYLE.md` before writing; it is binding for all pages
2. Test locally using `mint dev`
3. Run the linters on the pages you changed: `python3 scripts/lint-docs.py <files>` and `vale <files>`
4. Ensure all links and navigation work correctly
5. Submit a pull request with a clear description of your changes

## Links

- [Fhenix Website](https://www.fhenix.io/)
- [Fhenix Blog](https://www.fhenix.io/blog)
- [GitHub Organization](https://github.com/fhenixprotocol/)
- [Discord Community](https://discord.com/invite/FuVgxrvJMY)
- [Twitter/X](https://x.com/fhenix)

## Troubleshooting

- If your dev environment isn't running: Run `mint update` to ensure you have the most recent version of the CLI
- If a page loads as a 404: Make sure you are running in the folder with `docs.json`

## Resources

- [Mintlify Documentation](https://mintlify.com/docs)
- [CoFHE documentation live site](https://cofhe-docs.fhenix.zone)

## Support

For questions and support:
- Join our [Telegram Support Channel](https://t.me/+OEO4CItQYh8xYzNh)
- Visit our [Discord](https://discord.com/invite/FuVgxrvJMY)
- Check the [Support and Feedback](get-started/introduction/support-and-feedback.mdx) documentation
