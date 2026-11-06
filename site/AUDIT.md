# Onitama intro: code, UI and rules audit

Audited 2026-11-06 against app source `084853d692473a67c60e9cafe8a9975d685555aa`. Scope is `site/` plus Pages input-watch paths. No app behavior, dependencies, account or credentials changed.

## Design read

An explanatory introduction to a shared-table strategy game, preserving the real app’s scroll-paper, stone-ink serif type, existing brush logo, beige mat and red/blue player signals. Variance 5, motion 1, density 4. Native CSS is an adaptation of actual app tokens, not a newly invented design system. Actual product appearance takes precedence over a generic dual-theme requirement; this introduction remains light like the app. No decorative animation or extra dependency.

## Real app opened

Opened the live Vercel app in shared Ego workspace9/p4. Switched EN, started Standard, selected a Red student and its offered Rooster card, moved to a highlighted destination; verified Blue turn and used-card exchange. Selected Blue student/Crab and played another legal move, returning turn to Red. Opened AI Settings without enabling it. Returned to pack selection, added Wind, began a real variant and inspected the central neutral spirit and separate move patterns. No paid model, key, device permission or private user data was used.

`board-current.png`, `move-current.png`, `packs-current.png` and `wind-current.png` are genuine app captures. UI animations were allowed to settle before final capture. Hero is a CSS crop; no synthetic board is presented as a screenshot. The separate source-data movement diagram is explicitly labelled as such.

## Code examined

- `OnitamaLanding.tsx`, `CardPackSelection.tsx`, `GameHeader.tsx`: EN/Chinese selection, six packs, new deal, shared browser play, AI switch and music. There is no remote room/matchmaking interface.
- `public/pack/onitama_cards_*.json`, `dataLoader.ts`: actual card patterns, bilingual names, counts, random five-card selection, starting player by waiting-card color. Wind selection requires at least three wind cards among five, and may contain more. Pack counts and diagram records are extracted at build time.
- `gameManager.ts`: player-relative coordinates, legal destinations, landing captures, card exchange and turn switch; master capture or own master reaching opposing temple wins. Wind movement can have a piece phase then spirit phase, exchanging with students and excluding masters; Dual cards separate master/student patterns.
- `MoveGrid.tsx`: actual 5×5 pattern rendering with center, relative coordinate highlights and player direction. `site/cards.js` adapts this small diagram using real JSON; it is not a full game and has no persistence.
- `gameController.ts`, `aiService.ts`, `ai/aiFactory.ts`, `aiRestrictions.ts`: local game-search algorithms, Blue AI option, normal-pack compatibility. Wind/Dual disable AI. No online LLM integration is claimed.
- `ai/winProbability.ts`: logistic mapping from heuristic search scores, so the advantage display is described as an estimate rather than calibrated odds.
- `gamePersistence.ts` has utilities, but no active imports were found; no resume/history/export UI is promised. Refresh starts the landing flow again.
- `globals.css`, `gameAestheticConfig.tsx`, `GameBoard.tsx`, `MoveCards.tsx`: source palette, surfaces, red/blue signals, symbols and serif aesthetics.

## Primary research and boundaries

Read [Arcane Wonders’ Onitama product/rules overview](https://www.arcanewonders.com/eu/product/onitama/) for the five-card exchange and two victory paths, plus indexed official rulebook extracts. The publisher’s base PDF is unusually large (45MB) and could not be fully parsed by the web fetcher. The page links the publisher overview and official [Wind rulebook](https://www.arcanewonders.com/eu/wp-content/uploads/sites/6/2024/06/Onitama_Way_of_the_Wind.pdf). Wind-specific explanation is intentionally sourced from this app’s implementation rather than claiming exact tabletop expansion parity. No unsupported skill/learning benefit or engine-strength claim.

## Validation

Python standard-library build creates EN and `zh/`. Local asset/link checker: two pages, zero issues. JS syntax and diff whitespace checks pass. Browser controls/mobile review recorded below after final screenshots.

- Desktop intro opened at root local server; no horizontal overflow (`scrollWidth === innerWidth ===1468`). Actual hero and movement diagram visually reviewed.
- Tested Crab selection and Blue perspective: correct name, three destinations and rotated direction; the other two patterns are extracted from the same validated pack records.
- Final capture uses the settled selected-piece/highlight screen rather than a mid-exchange frame; caption and maintenance instructions describe selection accurately.
- A browser-owned location permission prompt then paused the entire shared Ego workspace. Browser work stopped immediately and was handed to the coordinating agent. Final EN/Chinese 390px viewport review remains pending that user-controlled prompt; no mobile pass is claimed here.

Coordinating review completed after the permission prompt was handled: English and Chinese pages at an actual 390×844 target viewport both had `scrollWidth === innerWidth === 390`, no broken loaded images, and were visually reviewed. Desktop hero and content were also reviewed. The pending mobile check is complete.
