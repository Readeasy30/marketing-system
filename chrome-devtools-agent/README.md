# Chrome DevTools Agent System

This folder is the shared Chrome DevTools for agents QA system for Wholelychit websites.

Use this system to test live sites and local previews with a browser-aware agent before shipping changes.

## Why this lives here

Chrome DevTools agent instructions are shared across projects, so the reusable workflow belongs in `Wholelychit/marketing-system`.

Each website repository should keep only a small repo-local `DEVTOOLS-QA.md` file with its own buttons, pages, and test notes.

## Do not place MCP machine config in website repos

Do not commit local MCP config files, tokens, browser profile paths, personal Chrome settings, or machine-specific setup into website repositories.

Allowed in website repos:

- `DEVTOOLS-QA.md`
- manual test checklists
- button-flow notes
- performance findings
- accessibility findings
- SEO findings
- safe Codex tasks created from QA results

Not allowed in website repos unless directly approved:

- private keys
- API keys
- auth tokens
- live tracking
- live ads
- payment setup
- personal browser profile data
- machine-specific MCP settings

## Current first targets

1. `Wholelychit/readeasy30.com`
2. `Wholelychit/matheasy30.com`

These should be checked first because both have learning-app buttons, mobile flows, and learner-facing interactions.

## Main files

- `CHROME-DEVTOOLS-QA-WORKFLOW.md` — reusable testing workflow.
- `CODEX-DEVTOOLS-QA-PROMPT.md` — copy-ready prompt for Codex or another coding agent.

## Standard result

After DevTools QA, create safe repo tasks only:

- fix broken buttons
- fix console errors
- fix mobile layout issues
- fix accessibility labels
- fix slow images/scripts
- fix broken links
- update SEO metadata
- update manual test notes

Do not redesign unless Gerry directly asks for a redesign.
