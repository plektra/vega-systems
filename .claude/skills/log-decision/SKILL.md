---
name: log-decision
description: Record a decision about Vega's systems in decisions.md and update the affected documents. Use when the user says something has been decided, chosen, bought, ordered or rejected.
---

# Log a decision

1. **Confirm the decision in one sentence** and, if it isn't clear, **why** it was made (cost,
   availability, performance, safety, an accepted trade-off). Ask only if the reason or scope really
   is unclear.
2. **Add a row at the top of the table in `decisions.md`:** date (today), system, decision, why, and a
   link to the doc with the details.
3. **If it replaces an earlier decision,** don't delete the old row. Add "(replaces YYYY-MM-DD)" to
   the new one.
4. **Update the affected docs:** mark the option as chosen in design notes, update
   `current-system.md` (plans and open questions), and update requirements or `loads.yaml` if values
   change.
5. **Check the consequences.** Does the decision create new requirements or open questions (ratings
   to confirm, parts to order, interfaces to other systems)? Add them as unchecked items in the right
   open-question list, and tell the user.
6. **Summarise** in the user's language, and suggest `/save` if they're finished.
