# Frankie Onitama / Project guide

[← README](../README.md)

Complete setup, behavior and technical notes. Unless stated otherwise, run commands from the repository root.

A browser implementation of Onitama: a 5×5 strategy board where movement cards rotate between players.

## Features

- Play using movement cards and a shared exchange card.
- Choose card packs, including variants with Wind Spirit mechanics.
- Move pieces using the board UI, with touch interaction and audio.

## Getting started

```sh
npm ci
npm run dev
```

Open the local URL printed by Next.js.

## Project notes

Built with Next.js, React, TypeScript, Tailwind CSS, Motion and Howler.js. Game rules and state live in `src/utils/`, interfaces in `src/components/`, and card packs and piece symbols in `public/`. See [architecture](../ARCHITECTURE.md) for implementation details.

## Development

```sh
npm run build
```

Use local play to check card exchange, move legality, winning conditions and touch input.

Banner sources and update instructions: [README artwork](readme/README.md).
