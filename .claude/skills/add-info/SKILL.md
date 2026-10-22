---
name: add-info
description: Record new facts, measurements, photos, prices or datasheet values about Vega's systems in the right documents. Use when the user reports something they measured, read, bought, changed on board, or found in a datasheet or link.
---

# Add new information

1. **Work out what the information is about** (which system, which component) and **where it came
   from**:
   - the owner measured or saw it → `[owner YYYY-MM-DD]` with today's date;
   - a datasheet or web page → `[datasheet <name>]` with the URL;
   - an estimate → say so.

   If the source or unit isn't clear, ask one short question.
2. **Find every place it belongs.** Search the repo for the component and related terms. Usually:
   - `<system>/current-system.md`: tables, the status section, open-question checklist;
   - `vessel/README.md` if other systems use it too (engine, gearbox, voltages, dimensions);
   - `<system>/loads.yaml` for load numbers (keep it valid YAML);
   - `<system>/requirements.md` and `<system>/design/*.md` where the value feeds a calculation or
     comparison.
3. **Update them.** Replace `⚠ unknown` or `⚠ verify` with the value and source. Tick answered
   questions `[x]`. Update the status date.
4. **Check the consequences.** If the new value changes an earlier calculation, conclusion or
   recommendation, recalculate (state your assumptions), update the text, and tell the user plainly
   what changed. Example: "The idle is 700 rpm, not 800, so the 43 cm³ pump now gives about 67 %
   thrust instead of 88 %."
5. **For a datasheet link,** read it, including scanned PDFs (render the pages to images if text
   extraction fails). Record the key ratings with the URL, and check them against the current
   design.
6. **Summarise for the user** in their language: what you recorded, where, and any consequences. If
   they're finished, suggest `/save`.
