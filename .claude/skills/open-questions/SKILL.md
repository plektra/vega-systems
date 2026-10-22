---
name: open-questions
description: Summarise what is still open, unknown or undecided across Vega's systems, and suggest what to do next. Use when the user asks what's missing, what's open, what to measure on board, or what to work on next.
---

# Summarise open questions

1. **Collect the open items:** unchecked `- [ ]` items, `⚠ unknown` and `⚠ verify` markers, and
   `TBD` values in all `*.md` and `*.yaml` files. If the user named a system, limit the search to
   that folder and `vessel/`.
2. **Group them by what the user would do:**
   - **Measure or check on board**, e.g. cylinder dimensions, idle rpm, hose markings;
   - **Ask a supplier or check a datasheet**, e.g. ratings, prices, adapters;
   - **Decide**: choices waiting for the owners;
   - **Calculate or write up**: things Claude can do now.
3. **Put the items that block the most other work first.** Briefly say why each matters (one line),
   with a link to the file.
4. **Keep it short:** about 10 items maximum, then offer the rest. Reply in the user's language. Don't
   change any files.
