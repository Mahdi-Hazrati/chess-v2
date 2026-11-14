# Chess V2

A classical, game-first chess variant on a 127-cell hexagonal board. Capture the opposing King to win. Familiar chess pieces meet Bees, fusion, reserves, terrain and the central Nexus.

Website release **1.2.0** · Rules edition **3** · No runtime dependencies or backend.

[راهنمای فارسی](README.fa.md) · [Full rules](dist/guide.html) · [Bot protocol](dist/BOT-PROTOCOL.md)

## Run locally

Install Node.js 20 or newer, extract this archive, and open a terminal in the `chess-v2` folder:

```sh
npm run preview
```

Open http://127.0.0.1:4173/ . No `npm install` or build step is needed. Do not double-click index.html: ES modules and module workers require HTTP. Alternatively serve the `dist` folder with an HTTP server. The included server binds only to localhost and is for development.

## Deploy to GitHub Pages

1. Create or select a GitHub repository with Pages available. Use a public repository unless your plan supports Pages for private repositories.
2. Put the **contents** of `chess-v2/` at repository root. Include `.github/workflows/pages.yml` and `dist/.nojekyll`; some file managers hide dotfiles.
3. Push the files to the `main` branch.
4. Open repository **Settings → Pages → Build and deployment → Source → GitHub Actions**.
5. Open **Actions → Verify and deploy Chess V2 → Run workflow**, selecting `main`. Later pushes to `main` deploy automatically. Pull requests run checks without deploying.
6. Wait for both `verify` and `deploy` jobs to succeed. The deployment environment reports your exact Pages URL.

Only `dist/` is published. All assets, module imports, workers, PDF links and navigation use relative paths, so a repository URL such as `https://YOUR-NAME.github.io/YOUR-REPO/` works without editing a base URL. Never put secrets in `dist` or this repository. No secrets are required by this workflow. If using a different default branch, update the workflow's push and pull_request branch filters.

The release includes configuration for Pages; it has not been deployed to your GitHub account. A missing Pages source setting can cause Configure Pages to fail. Set the source above and rerun. If JS loads as HTML, confirm that the uploaded artifact contains the contents of `dist`, not a nested source folder. Hard-refresh after replacing files.

## Play and learn

- **Play:** White moves first. Click your piece, then a highlighted destination. Solid marks indicate moves and outlined marks captures. The King may move into danger; there is no checkmate rule.
- **Learn:** sixteen interactive, validated positions teach movement, Bee swarms, fusion/splitting, reinforcements, Guards, Nexus, Courier transport, Royal Exchange, Anchors, Mimics, walls, gates and King capture. Lessons preserve your live match; Return to my game restores it with bots paused.
- **Pieces:** all seventeen roles, their symbols and movement summaries. Clicking a piece also shows its role and legal destinations.
- **Turn actions:** Move, Fuse, Deploy, Ability, Guard, Wall, Gate and Nexus. Follow the contextual instruction; a choice dialog handles alternate forms or destinations. Pass earns one flux. A Bee's optional second step can be declined with Finish swarm.
- **Bots:** play White against a practice bot, share the board locally, request one bot action, or watch both sides autoplay. Quick uses one-ply evaluation; Tactical uses a limited two-ply search. Autoplay pauses when the tab is hidden.
- **Board controls:** flip, zoom, coordinates, all-token physical notation, and Focus board. Tab enters the board once; arrow keys move between cells and Enter/Space selects. Home selects the center.
- **Files & tools:** download a replayable match, validate/load a backup, export bot observations, or run three separate bot games. Undo reverses one action and pauses bots.

Your live match and lesson completion are saved in this browser's local storage. Clearing browser data removes them; download backups to retain games or move them to another device. Save files are validated by replaying every action before replacement. Import is limited to 5 MB and 5,000 actions. There is no account, cloud synchronization, telemetry or remote multiplayer service.

## Complete rules and physical edition

The searchable `dist/guide.html` includes the complete rules and all seventeen piece profiles. The ten-page `dist/Chess-V2-Rulebook.pdf` is a printable reference. Rules cover movement, promotion, capture, fusion recipes, component recovery, reserves, flux, walls, gates, Guards, Royal Exchange, Nexus powers, special units and draws.

`dist/Chess-V2-Print-and-Play.pdf` contains nine pages: a single A3 board, four tiled A4 board sections, White and Black token sheets, markers/flux tracks, and exact starting setup plus tracking sheet. Print at **100% scale** and check the 50 mm reference. For A4, cut the four 180 mm squares and join 1–2 over 3–4. Use real chess pieces for the familiar roles and the optional printed discs for new roles; All tokens matches the physical codes. Keep fused ingredients off-board and track them and Courier passengers on paper. All game information is public.

The game has 17 roles: Pawn, Knight, Bishop, Rook, Queen, King, Bee, Hive, Hornet, Mimic, Anchor, Courier, Warden, Archbishop, Chancellor, Bastion and Lancer. Their physical codes and full behavior are in the guide. Coordinates are A–M and 1–13, with Nexus G7; only the 127 hexes shown exist.

## Project structure

| Path | Purpose |
| --- | --- |
| `dist/index.html`, `style.css`, `app.js` | Play UI and state coordination |
| `dist/engine.js` | Pure rules, legal actions, game state and bot search |
| `dist/bot-worker.js` | Search and batch testing outside the UI thread |
| `dist/pieces.js`, `role-info.js` | Original SVG silhouettes, token codes, descriptions |
| `dist/lessons.js` | Isolated interactive scenarios |
| `dist/persistence.js` | Validated replay save format |
| `dist/guide.html`, `guide.css`, `guide.js` | Searchable static documentation |
| `docs/rulebook.json` | Canonical player-guide text |
| `docs/make_rulebook.py`, `make_print_kit.py` | Rebuild printable PDFs |
| `scripts/build-guide.mjs` | Rebuild HTML guide |
| `scripts/check-site.mjs` | Syntax, links, anchors, PDF and subpath checks |
| `tests.mjs`, `tests/release.test.mjs` | Rules, legal bot play, lessons and saves |
| `.github/workflows/pages.yml` | Verify and publish `dist` |

## Development and verification

```sh
npm test
npm run check
npm run verify
npm run docs
```

`verify` runs 41 tests plus static checks. `docs` rebuilds the HTML guide from the rule text and piece definitions. After editing rulebook.json, regenerate both HTML and PDF so they remain aligned. PDF generation is optional for ordinary development and requires Python 3 with ReportLab:

```sh
python -m pip install reportlab
python docs/make_rulebook.py
python docs/make_print_kit.py
```

Committed PDFs are already usable; Python is not needed for deployment. Before shipping a rules change: add a focused engine test, update rules and lessons, regenerate docs, run verify, and inspect the rendered PDFs. Check tutorial completion/return, bot pause/resume, import/export, and touch/keyboard flows in your target browsers.

## Bots and compatibility

See `dist/BOT-PROTOCOL.md`. `window.ChessV2.getObservation()` returns a versioned state and legal actions; `submitAction(id, revision)` rejects stale or illegal submissions. Use local-player mode and pause autoplay for external control. `window.Faultline` is retained as a compatibility alias. The rules identifier `faultline-swarm/3` intentionally remains stable: renaming the product does not change its engine protocol. Standard UCI chess engines cannot play this variant without implementing its rules and an adapter. No remote bot transport is included.

## Release scope

This is a complete static release for local play, practice bots, learning and physical play. Bot strength is heuristic, not grandmaster level. Competitive balance is experimental; the bounded batch test reports unfinished games honestly. There is no matchmaking, online multiplayer, rating server, anti-cheat service, clock or threefold-repetition claim. Test coverage verifies behavior, not competitive balance. The site uses modern ES modules, SVG, localStorage, dialogs and Web Workers; serve it with HTTP(S) in a current browser.

No third-party font, image CDN or package is required at runtime. Piece drawings are original SVG code. No open-source license has been selected in this package; choose an appropriate license before offering third-party redistribution rights.


## Credits

Concept and game design: **Mahdi Hazrati (مهدی حضرتی)**.

Release 1.1 gives every new role an original classical silhouette. In Play, instructions and explanatory panels are hidden; Match settings and Notation open on demand. Learn retains the interactive guidance. The physical kit keeps optional lettered tokens for easy printing.

The `dist/piece-assets/` directory contains all 34 standalone SVGs (17 roles in White and Black) for printing, fabrication references or reuse.

Release 1.2 redesigns the website around a centered, frameless board, compact action index and reserve rail. Match settings, Notation and Files & tools remain available on demand. The rulebook uses the same editorial typography. No game rules changed.
