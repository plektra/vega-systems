---
name: save
description: Save the session's changes to GitHub as a pull request. Use when the user says "save", "tallenna", "done", "valmis", or asks to submit or share their changes.
---

# Save changes as a pull request

The user may not know git. Do every step yourself and report the result in one or two plain
sentences, in the user's language.

1. **Check what changed** (`git status`, `git diff`). If nothing changed, say so and stop.
2. **Check the changes for consistency:** sources cited, `⚠ verify` markers where values are
   uncertain, open-question checklists and `decisions.md` updated, links between files still
   working. Fix small problems; mention anything bigger.
3. **Make sure you're not on `main`.** If you are, create a branch named after the topic, e.g.
   `hydraulics/steering-cylinder-data`.
4. **Bring in the latest `main`** (`git fetch origin main`, then merge or rebase it). If there are
   conflicts, keep both people's information; ask the user only if the two versions contradict each
   other.
5. **Commit** with a short English message describing the topic, e.g. "Add steering cylinder
   dimensions". End the message with the attribution lines your instructions give, if any.
6. **Push the branch** (never force-push) **and open a pull request** against `main`:
   - Title: the same short summary.
   - Body: first a **plain-language summary** of what changed and why, a few bullets that an owner
     can approve from a phone. Then any numbers that changed (old → new), and any open questions this
     raised.
   - If you can't open the pull request yourself, tell the user to press the **Create PR** button in
     the Claude Code interface.
7. **Tell the user:** "Saved. Your changes are waiting for approval here: <link>. Open it and press
   *Merge pull request* to make them part of the main documents."
