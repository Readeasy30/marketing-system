# Wholelychit Repository Master Map

Last reviewed: 2026-06-05

This file is the master control map for Wholelychit repositories so GitHub work stays organized and repo purposes do not get mixed together.

## First rule: do not mix repo purposes

When Gerry names a repository, stay inside that repository unless he clearly asks for cross-repo comparison or coordination.

Dashboard/feed activity is not the same as a broken website, broken workflow, or production error.

Examples:

- A GitHub dashboard item such as someone starring a repository is account/feed activity.
- A GitHub Actions failure is a workflow/build issue inside the named repository.
- A Cloudflare Pages failure is a deployment/hosting issue for a website repository.
- A personal investment repository is not a marketing project.

## Command center rule

`Wholelychit/marketing-system` is the command center for marketing, SEO, campaign planning, launch planning, content calendars, monetization ideas, reusable prompts, Codex production rules, cross-site review systems, and blocker logs.

Website code stays inside each website repository.

Personal investment or trading research does not belong in the marketing workflow.

## Active public/business website repositories

| Priority | Repository | Brand / Domain | Purpose | Current direction |
|---:|---|---|---|---|
| 1 | `Wholelychit/readeasy30.com` | ReadEasy30 | Reading practice for children, adults, ESL learners, and struggling readers | Protect stable non-React version, improve lessons, add assessment/progression, build trust pages, prepare printable resources. |
| 2 | `Wholelychit/matheasy30.com` | MathEasy30 | Calm math learning and practice | Keep simple static stack, stabilize app flow, support worksheets and confidence-building practice. |
| 3 | `Wholelychit/my-petneeds` | PetNeeds.ai | Pet information, pet categories, safety-aware pet guidance | Build trustworthy pet portal, common Q&A, rare/household pet sections, safe affiliate/local ad planning later. |
| 4 | `Wholelychit/restaurantaibot.com` | restaurantaibot.com / RestaurantAIbot | Restaurant discovery and restaurant-owner AI growth platform | Build owner value, local pages, lead capture, demo-safe AI/restaurant tools, local ad planning later. |
| 5 | `Wholelychit/slotsfreeusa.com` | SlotsFreeUSA | Free slots entertainment and review content | Keep compliance, honest risk language, beginner guides, Lucky Lou character content, future ad/affiliate planning with disclosure. |
| 6 | `Wholelychit/bransonblastusa.com` | BransonBlastUSA | Branson visitor and local marketing site | Confirm deployment, add attractions/shows/restaurants/lake content, prepare local advertiser readiness later. |
| 7 | `Wholelychit/my-ozarkwebmasters` | Ozark Webmasters | Possible local web services / agency brand | Park or develop later after core websites stabilize. |

## Command center / planning repository

| Repository | Purpose | Use rule |
|---|---|---|
| `Wholelychit/marketing-system` | Central marketing, SEO, content, campaign, launch, monetization-planning, avatar/video, and review-control system | Use for cross-site planning only. Do not put live website code here. Do not use it for personal investment repo marketing. |

## Personal investment / research repository

| Repository | Purpose | Boundary rule |
|---|---|---|
| `Wholelychit/spx-tastytrade-autotrader` | Private personal SPX/Tastytrade research, backtesting, paper review, 60-market-day study notes, and staged broker-readiness planning | This is not a marketing repo, not a public campaign repo, and not part of website monetization work. Keep private, safety-first, paper-review-first, and no live broker execution unless explicitly approved after study and manual review. |

## Support / tool / template repositories

| Repository | Purpose | Use rule |
|---|---|---|
| `Wholelychit/bubbles-ai-guide` | Bubbles reading coach guide/personality and future ReadEasy30 AI support | Support ReadEasy30 coaching tone and safety. Do not replace the main ReadEasy30 website. |
| `Wholelychit/llm-chat-app-template` | Cloudflare Workers AI chat app template | Reference only. Do not use to convert simple static sites unless a rebuild is clearly approved. |
| `Wholelychit/chanfana-openapi-template` | Cloudflare/OpenAPI template | Reference only. Use only when an API is actually needed. |
| `Wholelychit/privacy` | Privacy/documentation review repo | Review safely. Do not add tracking, ads, payments, accounts, keys, or risky production changes. |
| `Wholelychit/refined-github-` | GitHub/browser helper or setup review repo | Treat as utility/setup review. Do not mix with website builds. |
| `Wholelychit/claude.yml` | Claude workflow/config helper repo | Treat as configuration/support only. Do not mix with website content or investment work. |

## Standard files for every public website repo

Every public site should eventually include or verify:

1. `README.md` — purpose, tech stack, live domain, next actions.
2. `AGENTS.md` — AI/Codex file-work rules.
3. `AGENT-INSTRUCTIONS.md` — repo-specific guardrails.
4. `LOCKED-CHECKPOINT.md` — stable state when the repo has fragile working progress.
5. `FILE-MANAGEMENT.md` — file rules when the repo grows.
6. `PROJECT-STATUS.md` — current state, blockers, next queue.
7. `CONTENT-PLAN.md` — page/content roadmap.
8. `SEO-CHECKLIST.md` — title, meta, internal links, schema, sitemap, robots.
9. `LAUNCH-CHECKLIST.md` — public launch readiness.
10. Legal pages and footer links before public promotion.

These public-website rules do not apply to `spx-tastytrade-autotrader` as marketing rules. That repository uses safety, review, backtest, paper-trading, and broker-readiness rules instead.

## Standard launch checks for every public website

1. Homepage title is clear.
2. Meta description exists and fits the site promise.
3. Canonical URL is correct.
4. Navigation is simple and working.
5. Footer includes Terms, Privacy, Advertising/Affiliate disclosure, AI Disclaimer where needed, and Community Rules where needed.
6. `robots.txt` exists.
7. `sitemap.xml` exists.
8. Mobile layout works.
9. Main user action works.
10. No private keys, tokens, payment setup, live ads, or tracking scripts are added without explicit approval.

## Performance rules for public websites

Use these rules on public website repositories:

1. Mobile first.
2. Simple HTML/CSS/JS unless the site truly needs a framework.
3. No unnecessary animations, scripts, popups, or trackers.
4. Compress images before upload.
5. Use clear page titles and meta descriptions.
6. Add internal links between related pages.
7. Keep consumer language around a 7th to 9th grade reading level.
8. Test homepage, mobile layout, navigation, footer links, and core user action after each major change.

## Monetization map for public/business websites only

| Site | Best first monetization | Later monetization |
|---|---|---|
| ReadEasy30 | Printable resources, parent guides, tutor/school outreach | Subscription, assessment reports, sponsored education resources. |
| MathEasy30 | Printable worksheets, parent guides | Subscription, school/tutor partnerships. |
| PetNeeds.ai | Affiliate product paths, local vet/store listings, sponsored guides | Display ads, newsletter, local marketplace. |
| restaurantaibot.com | Restaurant lead generation, owner pages, monthly AI marketing service | Sponsored listings, menu/content services, local ads. |
| SlotsFreeUSA | Display ads, compliant affiliate offers, email list | Sponsored reviews where legal and disclosed. |
| BransonBlastUSA | Local visitor content and advertiser readiness | Local sponsorships, listings, travel/visitor partnerships. |

Do not add `spx-tastytrade-autotrader` to this monetization map. It is personal investment/research, not a public/business website.

## Do-not-repeat rule

Before editing any public website site, check:

1. README.md.
2. AGENTS.md.
3. AGENT-INSTRUCTIONS.md if present.
4. LOCKED-CHECKPOINT.md if present.
5. FILE-MANAGEMENT.md if present.
6. PROJECT-STATUS.md if present.
7. Current homepage and core files.
8. The exact file being changed.

For `spx-tastytrade-autotrader`, check its README, safety files, project status, locked checkpoint, risk controls, manual-review checklist, and broker-readiness checklist before changing anything.

## Current command-center files

- `REPOSITORY-MASTER-MAP.md` — all repos and boundaries.
- `CODEX-PRODUCTION-WORKFLOW.md` — how Codex should work across repos.
- `FILE-MANAGEMENT.md` — direct-file rules and anti-duplication system.
- `TIME-MANAGEMENT.md` — how sessions should avoid wasted loops.
- `WEBSITE-PRIORITY-LIST.md` — current public website build order.
- `PROMPT-LIBRARY.md` — reusable prompts for review/build work.
- `CROSS-SITE-LAUNCH-CHECKLIST.md` — launch checks before promotion.
- `REVIEW-FIX-LOOP.md` — standing review/fix process.
- `LEGAL-PAGE-INSTRUCTIONS.md` — shared legal/footer guidance.
