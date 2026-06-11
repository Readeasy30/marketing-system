# Avatar Workflow

Use this workflow before adding avatars or videos to any Wholelychit website.

## Core decision

Marketing repo = reusable avatar system.

Website repo = site-specific avatar implementation.

## Step 1 — Choose the avatar job

Every avatar needs one main job.

Examples:

- Help visitors choose what to do next.
- Explain the site in plain language.
- Build trust before a visitor clicks a link.
- Guide a learner through a lesson.
- Help a local business owner understand the offer.

Avoid avatars that talk too much. The avatar should help, not interrupt.

## Step 2 — Set the site voice

Use the correct voice for the website.

- ReadEasy30: slow, calm, patient, no shame.
- MathEasy30: clear, simple, confidence-building.
- PetNeeds.ai: warm, careful, pet-safe, not a veterinarian replacement.
- SlotsFreeUSA: fun, adult, simple, risk-honest.
- BransonBlastUSA: upbeat, local, useful, trip-friendly.
- RestaurantAIbot / restaurantaibot.com: practical, local, owner-focused.

## Step 3 — Build the short script first

Start with a 20 to 40 second message.

Structure:

1. Friendly greeting
2. One-sentence site promise
3. What the visitor can do next
4. Clear button or next action

## Step 4 — Create the video outside GitHub

Use Canva, HeyGen, YouTube, Cloudflare Stream, or another approved tool.

Do not store large video files in GitHub unless there is a clear production reason.

## Step 5 — Store only the useful files in the website repo

Each website repo can have:

```text
avatar/
  avatar-personality.md
  avatar-dialogue.md
  avatar-placement-plan.md
videos/
  video-plan.md
  scripts.md
```

## Step 6 — Add the embed safely

Add only safe placeholder embed code first.

Do not add:

- API keys
- secret tokens
- live tracking
- live ad scripts
- payment tools
- public AI chat tools
- upload systems

## Step 7 — Test on mobile first

Check:

- The avatar does not cover buttons.
- The video does not autoplay with sound.
- The page still loads fast.
- The visitor can close or ignore the avatar.
- The site remains usable without video.

## Best first use

Start with one helpful explainer video per site before adding a full interactive avatar.

Recommended order:

1. BransonBlastUSA trip buddy intro
2. SlotsFreeUSA Lucky Lou intro
3. PetNeeds.ai pet helper intro
4. ReadEasy30 Bubbles parent/learner intro
5. RestaurantAIbot owner offer intro
