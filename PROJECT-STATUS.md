# Project Status

Last updated: 2026-05-31

This file tracks the safe marketing-system queue for Wholelychit projects.

## Current Workflow Decision

Codex is the primary workflow for routine repository edits.

The ChatGPT GitHub connector is secondary and should be used only for small reads, checks, reviews, or emergency single-file edits when Codex is unavailable.

## Active Portfolio Plan

The current locked marketing direction is the Wholelychit multi-site portfolio plan.

Sites covered:

1. SlotsFreeUSA
2. RestaurantAIbot / Resturants.ai
3. ReadEasy30
4. MathEasy30
5. PetNeeds.ai
6. BransonBlastUSA

## Avatar and Video System Added

Decision locked:

- Marketing repo stores reusable avatar and video systems.
- Each website repo stores final site-specific avatar personality, final dialogue, placement plan, and embed notes.
- Large final videos should usually be hosted outside GitHub through an approved video platform.

New files added:

- `avatar-system/README.md`
- `avatar-system/AVATAR-WORKFLOW.md`
- `avatar-system/AVATAR-PERSONALITY-TEMPLATE.md`
- `avatar-system/AVATAR-DIALOGUE-LIBRARY.md`
- `avatar-system/AVATAR-EMBED-TEMPLATE.md`
- `video-system/README.md`
- `video-system/SHORT-VIDEO-SCRIPT-TEMPLATE.md`
- `video-system/CANVA-VIDEO-CHECKLIST.md`
- `prompt-library/AVATAR-PROMPT.md`
- `prompt-library/VIDEO-SCRIPT-PROMPT.md`

## BransonBlastUSA Note

Repo identified as `Wholelychit/bransonblastusa.com`.

Misspelled `branssonblastusa.com` repo was not found.

BransonBlastUSA should use the shared avatar/video system from this repo, then store final site-specific avatar files in its own repo.

## Current Safe Queue

1. Keep this repo as the marketing control center.
2. Use `avatar-system/` and `video-system/` as the reusable avatar/video source of truth.
3. Put finished avatar/video implementation files inside each website repo.
4. Build BransonBlastUSA site-specific avatar files next.
5. Continue BransonBlastUSA static repo repair: `script.js`, `robots.txt`, `sitemap.xml`, status files, and CSS completion if needed.
6. Keep ReadEasy30 worksheet promotion as the active first education launch.
7. Record blockers instead of stopping.

## Blockers

- One active avatar embed HTML template write was blocked by connector safety checks.
- A safe markdown planning template was created instead.
- Manual browser QA is still required after public deployment.

## Notes

Build practical systems Gerry can reuse across multiple websites. Keep language direct, simple, and action-based.
