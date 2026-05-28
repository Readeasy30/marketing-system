# Wholelychit Starter Template Plan

Last updated: 2026-05-28

## Purpose

Future Wholelychit repositories should start from a simple reusable template so the same setup work does not have to be repeated.

The starter should support Codex-first editing, basic SEO, launch checks, and safe production workflow from day one.

## Recommended Starter Repo Name

`Wholelychit/wholelychit-site-starter`

Use this as the future template for simple static websites unless a project clearly needs a different stack.

## Default Tech Stack

Use the simplest working stack by default:

- HTML
- CSS
- JavaScript
- GitHub repository
- Cloudflare or GitHub Pages deployment when appropriate

Do not use React, Vite, Next.js, TypeScript, or build tools unless the project already requires them.

## Required Root Files

Every future site repo should include:

- `README.md`
- `AGENTS.md`
- `AGENT-INSTRUCTIONS.md`
- `PROJECT-STATUS.md`
- `CODEX-WORKFLOW.md`
- `robots.txt`
- `sitemap.xml`
- `SEO-CHECKLIST.md`
- `LAUNCH-CHECKLIST.md`
- `REVIEW-CHECKLIST.md`
- `DEPLOYMENT-NOTES.md`
- `CONTENT-PLAN.md`
- `STYLE-GUIDE.md`

## Recommended Website Files

For simple static sites, start with:

- `index.html`
- `css/style.css`
- `js/main.js`
- `images/README.md`
- `affiliate-disclosure.html` when affiliate links may be used
- `privacy.html` when forms, analytics, ads, or user data may be used
- `terms.html` when the site gives advice, reviews, or monetized content

## Codex-First Files

### `AGENTS.md`

Purpose: short command rules for AI/Codex work.

Must say:

- Codex is the main repo-editing workflow.
- Do not ask Gerry to manually paste, create, replace, or update repo files.
- Make safe repo edits directly.
- Commit useful safe changes.
- Stop only for real blockers.
- Keep stack stable.
- Avoid framework migration unless the repo already uses that framework.

### `PROJECT-STATUS.md`

Purpose: current status, blockers, and next safe queue.

Must include:

- current workflow decision
- current active queue
- completed work
- safe work allowed
- blockers
- next actions

### `CODEX-WORKFLOW.md`

Purpose: explain why Codex is primary and how future repo work should proceed.

Must include:

- why Codex is used
- why ChatGPT connector write popups are confusing
- what Codex should do directly
- what Codex should not do without approval
- how to continue safe work across Wholelychit repos

## Starter README Sections

A good starter `README.md` should include:

1. Project name
2. Purpose
3. Live URL
4. Tech stack
5. File map
6. Current status
7. Safe build queue
8. Deployment notes
9. Codex workflow note
10. Important blocker rules

## Basic SEO Checklist

Every new repo should start with:

- clear page title
- meta description
- canonical URL
- mobile viewport tag
- one main H1
- simple navigation
- footer with important links
- `robots.txt`
- `sitemap.xml`
- image alt text
- internal links
- plain-language page copy

## Launch Checklist

Before launch, verify:

- homepage loads
- mobile layout works
- links work
- footer links work
- canonical URL is correct
- robots.txt is correct
- sitemap.xml is correct
- no private keys are present
- no broken placeholder text remains
- no live ad or tracking scripts are added without approval
- affiliate/privacy/legal pages exist if needed

## Review Checklist

For every safe Codex work session:

1. Read current instructions first.
2. Keep the existing stack.
3. Make safe direct edits.
4. Commit useful changes.
5. Record blockers in `PROJECT-STATUS.md`.
6. Continue until safe queue is complete or a real blocker appears.

## Future Use

When starting a new Wholelychit website repo, create it from this starter pattern first. Then customize only the project name, domain, audience, homepage copy, SEO details, and content plan.

This keeps every repo clean, repeatable, and ready for Codex-first production work.
