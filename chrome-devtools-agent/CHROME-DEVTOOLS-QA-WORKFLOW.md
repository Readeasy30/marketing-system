# Chrome DevTools QA Workflow

Use this workflow for ReadEasy30, MathEasy30, and other Wholelychit sites before and after safe site updates.

## Goal

Find real browser problems that normal file review can miss.

## Run order

| Step | Check | What to look for | Safe output |
|---|---|---|---|
| 1 | Open homepage | Page loads, no obvious broken layout | Note pass/fail |
| 2 | Open app page | App loads and buttons are visible | Note broken controls |
| 3 | Console | JavaScript errors, missing files, blocked resources | Create safe bug task |
| 4 | Network | 404 files, slow images, heavy scripts | Fix paths or compress later |
| 5 | Mobile viewport | Buttons readable, no side scroll, no clipped content | Create CSS/mobile task |
| 6 | Accessibility | Labels, button names, heading order, color contrast | Create accessibility task |
| 7 | Lighthouse/Core Web Vitals | LCP, CLS, INP, performance, SEO | Create prioritized fix list |
| 8 | Link click test | Navigation, footer, CTA buttons, lesson buttons | Fix broken links/buttons |
| 9 | Form/input test | Answer boxes, clear/reset buttons, progress controls | Fix app behavior only |
| 10 | Final notes | Summarize exactly what changed or what is blocked | Update repo-local `DEVTOOLS-QA.md` |

## ReadEasy30 button flow

Check these pages first:

| Page | URL | Required checks |
|---|---|---|
| Homepage | `https://readeasy30.com/` | Start buttons, nav, footer, mobile layout |
| Lesson app | `https://readeasy30.com/app.html` | Read aloud, check answers, clear answers, prev/next, reset, day selector |
| Campaign page | `https://readeasy30.com/free-reading-and-math-practice.html` | ReadEasy30 and MathEasy30 links |
| Worksheets | `https://readeasy30.com/printable-reading-worksheets.html` | worksheet links and mobile readability |

## MathEasy30 button flow

Check these pages first:

| Page | URL | Required checks |
|---|---|---|
| Homepage | `https://matheasy30.com/` | Start buttons, nav, footer, mobile layout |
| Lesson app | `https://matheasy30.com/app.html` | answer buttons/inputs, clear/reset, prev/next, lesson navigation |
| Campaign page | `https://matheasy30.com/free-reading-and-math-practice.html` | ReadEasy30 and MathEasy30 links |
| Worksheets | `https://matheasy30.com/printable-math-worksheets.html` | worksheet links and mobile readability |

## Safety rules

Do not use DevTools findings as an excuse to redesign.

Allowed fixes:

- broken links
- missing labels
- visible console errors
- missing files
- bad mobile spacing
- oversized images
- SEO metadata problems
- button bugs
- small JavaScript behavior repairs

Do not add without direct approval:

- tracking scripts
- live ads
- payment tools
- public AI chat tools
- user accounts
- uploads
- API keys
- browser profile data
- MCP config with tokens
- framework conversions

## Report format

Use this table in results:

| Repo | Page | Issue | Severity | Fix file | Status |
|---|---|---|---|---|---|
| readeasy30.com | app.html | Example button issue | High | app.js | Planned |

## Done definition

DevTools QA is done when:

1. Homepage and app page were checked on desktop and mobile viewport.
2. Console and Network were checked.
3. Important buttons were clicked.
4. Lighthouse or DevTools performance insight was reviewed.
5. Findings were recorded in the website repo.
6. Safe fixes were turned into Codex tasks or committed directly.
