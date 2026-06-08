GMAIL SEND-BLOCK LOG

A record of any send/draft that Gmail blocked or filtered. The purpose of this
log is **diagnosis, not evasion.** A block means the mail looked like
unsolicited bulk mail to Google. The response is always to slow down and raise
quality — never to work around the filter (that burns the domain and the account).

## What a block is telling you
- Sending too much, too fast, from a channel not meant for it (consumer Gmail).
- List or content reads as bulk/promotional rather than personal and wanted.
- Authentication missing or weak (no SPF/DKIM/DMARC on the sending domain).

## The fix (see EMAIL-READY-CONTACT-STANDARDS.md)
1. Send from your own authenticated domain, not consumer Gmail.
2. Warm up: start ~20–30/day, climb gradually.
3. Keep the list to verified, relevant, public contacts only.
4. Make each message personal enough that recipients want it (low complaints).
5. If blocks continue, **stop and reduce volume** until they clear.

## Log
| Date | Recipient type (segment / bucket) | What was attempted | Block / filter message | Action taken |
|---|---|---|---|---|
| | | | | |

> Do not record full private recipient addresses here — segment/bucket is enough
> for diagnosis. If the same block recurs, the action is **pause and fix**, not retry.
Tell me when done → FILE #6 (last one).You said: donedone5:02 PMClaude responded: FILE 6 of 6: EMAIL-READY-CONTACT-STANDARDS.Retrieved final outreach file for deliveryRetrieved final outreach file for deliveryFILE 6 of 6: EMAIL-READY-CONTACT-STANDARDS.md (LAST OUTREACH FILE)
Create new file → filename: OUTREACH/EMAIL-READY-CONTACT-STANDARDS.md → Paste this:
markdown# EMAIL-READY CONTACT STANDARDS

What it takes for a contact to move from "found" to "email-ready," plus the
domain setup that makes email actually land. This is what converts the queue
from contact-form prospects into a clean, deliverable email list.

## A contact is email-ready ONLY if ALL are true
1. The email address is **published by the organization on its own official site.**
2. It is an organizational/role address (e.g. info@, programs@), not a private personal one.
3. The org's segment and a real reason it'd want these resources are recorded.
4. It is **not** opted out and **not** Blocked/no-contact.
5. The contact page URL where it was verified is saved in the tracker.

If any is false → it stays Contact-form only, Directory/source only, Hold, or Blocked.
**Never** promote a guessed, scraped, or pattern-built address to email-ready.

## Sending-domain setup (do this before scaling email)
Send from your own domain (readeasy30.com), not consumer Gmail. Add these DNS
records at your DNS host (Cloudflare → DNS → Records):

- **SPF** (TXT, name `@`): `v=spf1 include:_spf.google.com ~all`
  *(adjust the `include:` to match whatever service actually sends your mail)*
- **DKIM** (TXT, name `google._domainkey`): generated inside your mail provider's
  admin console; paste the value it gives you.
- **DMARC** (TXT, name `_dmarc`): start at
  `v=DMARC1; p=none; rua=mailto:postmaster@readeasy30.com`,
  then tighten to `p=quarantine` after ~1–2 weeks of clean reports.

> Exact records depend on which provider sends your mail. Confirm the provider,
> then finalize the `include:` and DKIM values.

## Warmup ramp (new or cold sending domain)
- Week 1: ~20–30/day · Week 2: ~50–75/day · Week 3+: increase only while
  bounces and spam complaints stay near zero. Back off immediately if they rise.

## Every email must include (compliance — general guidance, not legal advice)
- A truthful subject line (no bait).
- Real sender name and organization.
- A valid physical mailing address.
- A one-line, no-friction way to opt out, honored immediately.

## Keep the list clean
- Remove hard bounces promptly.
- Suppress every opt-out permanently.
- Re-verify a contact page before re-use if it's been months.
Tell me when done. Then VIDEO-SYSTEM files (5 files left).Haiku 4.5 Extended
