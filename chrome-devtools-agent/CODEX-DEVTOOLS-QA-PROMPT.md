# Codex Prompt — Chrome DevTools QA

Use this prompt when running a Chrome DevTools browser-aware QA pass for ReadEasy30 or MathEasy30.

```text
Review this live HTML/CSS/JS website with Chrome DevTools for agents.

Do not redesign.
Do not convert to React, Vite, Next.js, TypeScript, or build tools.
Do not add tracking, ads, payment tools, API keys, public AI tools, accounts, uploads, or private credentials.

Check:
1. Console errors
2. Network 404s and missing files
3. Mobile layout problems
4. Lighthouse/Core Web Vitals issues
5. SEO metadata and canonical URL
6. Accessibility labels and button names
7. Broken links
8. App buttons and form/input behavior
9. Slow images/scripts
10. Footer and navigation links

Click every important button.
Test desktop and mobile viewport.
Record findings in DEVTOOLS-QA.md.
Fix only safe bugs.
Commit useful safe fixes in clear stages.
Report in a table:

| Page | Issue | Severity | Fix | File | Status |
|---|---|---|---|---|---|
```

## ReadEasy30 target URLs

```text
https://readeasy30.com/
https://readeasy30.com/app.html
https://readeasy30.com/free-reading-and-math-practice.html
https://readeasy30.com/printable-reading-worksheets.html
```

## MathEasy30 target URLs

```text
https://matheasy30.com/
https://matheasy30.com/app.html
https://matheasy30.com/free-reading-and-math-practice.html
https://matheasy30.com/printable-math-worksheets.html
```
