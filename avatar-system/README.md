# Avatar System

This folder is the reusable avatar command center for Wholelychit websites.

## Rule

The marketing repo stores the reusable system, templates, and prompt library.

Each website repo stores its own finished avatar personality, final dialogue, embed notes, and page placement.

## Why this split works

- One shared workflow prevents repeated work.
- Each website keeps its own voice and audience fit.
- Large video files should not be stored in GitHub unless there is a clear reason.
- Finished videos should usually be hosted through YouTube, Canva, Cloudflare Stream, HeyGen, or another video platform, then embedded on the website.

## Website avatar direction

| Website | Avatar Role | Tone |
|---|---|---|
| ReadEasy30 | Bubbles reading coach | Calm, patient, no-shame, confidence-building |
| MathEasy30 | Math practice helper | Simple, encouraging, step-by-step |
| PetNeeds.ai | Pet care helper | Warm, practical, family-safe, vet-aware |
| SlotsFreeUSA | Lucky Lou slot guide | Fun, clear, adult, risk-honest |
| BransonBlastUSA | Branson trip buddy | Friendly, local, useful, upbeat |
| RestaurantAIbot / restaurantaibot.com | Restaurant growth assistant | Trustworthy, local, business-focused |

## Folder map

- `AVATAR-WORKFLOW.md` — how to design and deploy avatars without repeating work
- `AVATAR-PERSONALITY-TEMPLATE.md` — copy and adapt inside each website repo
- `AVATAR-DIALOGUE-LIBRARY.md` — reusable starter dialogue by website type
- `AVATAR-EMBED-TEMPLATE.html` — safe placeholder embed structure

## Stop points

Do not add live API keys, tracking scripts, payment tools, public AI chat tools, or upload systems without direct approval.
