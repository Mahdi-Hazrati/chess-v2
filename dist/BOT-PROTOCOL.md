# Chess V2 bot protocol — faultline-swarm/3

This is a custom variant, not UCI. Standard chess engines need an adapter and an implementation of these rules. The pure module at ./engine.js works in browsers, workers and Node.js.

```js
import {initial, actions, play, chooseAction} from './engine.js';
let state = initial();
const observation = actions(state);
state = play(state, chooseAction(state, {depth: 1, seed: 42}).action.id);
```

Browser integration:

```js
const obs = window.ChessV2.getObservation();
// version, revision, state, legalActions
window.ChessV2.submitAction(chosenActionId, obs.revision);
```

Use local match mode and pause autoplay before external submission. IDs are opaque strings; choose one from legalActions. Stale revisions and illegal IDs are rejected. The dialog supports manual submission against the current position. No remote bot transport is configured.

Board keys are axial q,r with max(abs(q),abs(r),abs(q+r)) <= 6: 127 cells. File is q+6 (A–M); rank is r+7. G7 is 0,0. Colors: w=White, b=Black.

Unit fields: t (type), c (color), parts (recoverable ingredients), optional cargo (Courier passenger). Types: p Pawn, n Knight, b Bishop, r Rook, q Queen, k King, w Warden, a Archbishop, c Chancellor, e Bee, h Hive, v Hornet, m Mimic, t Anchor, u Courier, s Bastion, l Lancer.

State includes flux, reserves, walls, gates, guards, royal exchange availability, swarm, ply, winner and reason. `core` is the current occupant's color or null, not persistent ownership. Nexus has no passive income.

Actions: move, swarm, finish, fuse, deploy, wall, gate, split, load, unload, exchange, guard, harvest, recall, reforge, pass. Read their fields from the supplied legal list. `play` validates; `apply` assumes an already-legal generated action.

IMPORTANT: a non-capturing Bee move can leave state.turn unchanged and state.swarm set. Complete one optional swarm action or finish. This does not increment ply a second time. Guard reactions resolve inside the action; they do not require another submission. King capture ends play immediately.

The Bot interface exports an observation. Save, load & test exports a different replayable match format, chess-v2-match/1. Match imports validate every action from the initial position before replacement. Do not interchange these formats. Batch tests use separate states and report a 120-turn cap as unfinished. Built-in search is heuristic; Tactical uses an eight-candidate two-ply beam and excludes construction from opponent reply generation. Swarm continuation is handled as an additional action, not an enemy reply.

The PDF rulebook and online guide are the full player-facing specification.
