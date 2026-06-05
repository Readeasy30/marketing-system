# Brevo Import Lock — 2026-06-05

Project: ReadEasy30 + MathEasy30 outreach

## Lock status

Brevo import using the raw workbook is **blocked**.

Do not keep trying to drag this raw file into Brevo:

```text
readeasy30_matheasy30_daily_outreach_mail_list_180.xlsx
```

## Why it is blocked

The raw 180 workbook is the master outreach tracker. It is not guaranteed to be a clean Brevo contact-import file.

Brevo needs a clean contact file where every importable row has a valid email address in a clearly named email column.

The raw workbook includes mixed contact routes, including contact pages and rows that may not have direct email addresses.

## Correct next file

Create a clean Brevo import file named:

```text
readeasy30_matheasy30_brevo_import.csv
```

For the future 300/day version, create:

```text
readeasy30_matheasy30_brevo_import_300.csv
```

## Required CSV columns

```text
Email
Organization
Segment
Website
Source URL
Status
Notes
```

## Required extraction rule

Start from:

```text
readeasy30_matheasy30_daily_outreach_mail_list_180.xlsx
```

Extract only rows where the public email column is filled.

Rename the email field to:

```text
Email
```

Do not import rows that only have contact-form URLs into Brevo as email contacts.

## Brevo import rule

Use Brevo only after the clean CSV is made.

Do not drag the raw tracker workbook again.

## Sender lock

Use:

```text
free@readeasy30.com
```

Do not use `wholelychit@gmail.com` as the campaign sender unless Gerry says it is a temporary backup.

## Current target lock

Daily target after Brevo approval:

```text
300/day
```

Current recovered list:

```text
180 rows
```

Additional needed for 300/day:

```text
120 rows
```

## Next safe action

Upload the actual workbook into ChatGPT or provide the local file so a clean CSV can be produced.

If the file cannot be uploaded, manually export only rows with public email addresses from the workbook into a CSV with the required columns above.

## Do not continue until

- clean CSV exists,
- sender identity is confirmed,
- Brevo accepts the file,
- one test send passes,
- suppression/do-not-contact handling is active.
