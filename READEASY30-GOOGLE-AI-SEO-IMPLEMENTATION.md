# ReadEasy30 Google + AI SEO Implementation Plan

This file turns the Google/YouTube/AI search strategy into practical repo work for `Wholelychit/readeasy30.com`.

## Goal

Make ReadEasy30 easier for Google, YouTube, and AI answer systems to understand as a trustworthy free reading-practice site.

No spam. No fake backlinks. No keyword stuffing. No mass AI page publishing.

## Gemini Review Notes

Useful ideas to keep:

- use clear schema markup
- keep semantic HTML heading order clean
- add direct Q&A blocks to important pages
- use precise words for the site, audience, and learning tools
- embed videos only when they are useful and loaded responsibly
- keep sitemap and robots files current

Use caution with:

- "programmatic" content pages. Only create pages that solve a real reader/helper problem and are reviewed.
- automated minification/build pipelines. ReadEasy30 is intentionally simple static HTML/CSS/JS, so avoid adding build tools unless truly needed.
- broad sameAs links. Add only official profiles that actually exist and are controlled by Wholelychit/ReadEasy30.

## First Site: ReadEasy30

Repository: `Wholelychit/readeasy30.com`

Live site: https://readeasy30.com/

Current strengths:

- clear product purpose
- calm no-shame positioning
- lesson app
- worksheet pages
- ESL/adult/parent support pages
- sitemap and robots files
- homepage EducationalApplication schema

Main opportunity:

Make every important page answer one search question clearly and connect to the next best page.

## Repo Tasks Codex Can Implement

### 1. Add Page-Level SEO Checklist

Create or update a repo checklist file that says every public page needs:

- unique title
- meta description
- canonical URL
- one H1
- clear intro answer
- useful internal links
- footer navigation
- sitemap inclusion
- calm, plain-language copy

### 2. Strengthen Homepage Schema

Review `index.html` schema and consider adding:

- `WebSite`
- `Organization`
- `EducationalApplication`

Only add `sameAs` if official social profiles exist.

### 3. Add FAQ Blocks To High-Intent Pages

Add short FAQ sections to:

- `reading-comprehension-practice.html`
- `phonics-practice-for-beginners.html`
- `adult-reading-practice-without-shame.html`
- `esl-reading-practice.html`
- `printable-reading-worksheets.html`
- `parent-tutor-guide.html`

Each FAQ should answer real questions in plain language.

### 4. Improve Internal Links

Each major page should link to:

- `app.html`
- `printable-reading-worksheets.html` when relevant
- one related help page
- `parent-tutor-guide.html` when relevant

### 5. Add Video-Ready Sections

Prepare pages for future YouTube videos without embedding placeholder videos.

Use sections like:

- "Video idea: How to use this page"
- "When a video is ready, place it here"

Do not publish empty embeds.

### 6. Add VideoObject Schema Later

Only add video schema after a real video exists with:

- title
- description
- upload date
- thumbnail URL
- embed URL
- transcript or page summary

### 7. Keep Static Performance Simple

Do not add React, Vite, Next.js, or a build step.

Use simple improvements:

- optimized images
- lazy loading for future videos/images
- small CSS changes
- no unnecessary third-party scripts

### 8. Monthly Search Console Review

When Search Console data is available, improve pages with:

- impressions but low clicks
- ranking positions 8-30
- unclear titles
- weak meta descriptions
- thin intros

## First Implementation Batch

Batch 1 should be small and safe:

1. Add `SEO-PAGE-CHECKLIST.md` to `readeasy30.com`.
2. Add FAQ sections to `esl-reading-practice.html` and `adult-reading-practice-without-shame.html`.
3. Verify those pages are in `sitemap.xml`.
4. Add or improve internal links back to `app.html` and `parent-tutor-guide.html`.
5. Do not touch the lesson engine.

## First YouTube Video Ideas

### Video 1

Title: How ReadEasy30 Helps You Practice Reading 30 Minutes a Day

Landing page: `https://readeasy30.com/`

Description opening:

ReadEasy30 is free calm reading practice for learners who need short stories, simple questions, worksheets, and a no-shame daily routine.

### Video 2

Title: Reading Practice for Adults Without Shame

Landing page: `https://readeasy30.com/adult-reading-practice-without-shame.html`

Description opening:

A calm explanation of how adults can practice reading with simple passages, useful questions, and steady support.

### Video 3

Title: ESL Reading Practice With Simple Everyday English

Landing page: `https://readeasy30.com/esl-reading-practice.html`

Description opening:

Use ReadEasy30 to practice everyday English reading with short passages, vocabulary help, and simple comprehension questions.

## Success Measures

Track monthly:

- indexed pages
- Google impressions
- clicks
- click-through rate
- average position trend
- page updates completed
- internal links added
- videos published
- pages with FAQ sections

## Non-Negotiable Safety Rules

- Do not promise instant reading success.
- Do not publish large batches of AI pages without review.
- Do not add fake testimonials.
- Do not add tracking, ads, accounts, or payments without review.
- Do not add browser auto-click scripts.
