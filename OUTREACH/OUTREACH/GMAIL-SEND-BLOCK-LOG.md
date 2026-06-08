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
