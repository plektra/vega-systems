# Working on the Vega systems repository

This repository documents and designs the systems of Vega, a 1912 steel tug (16.15 m) being
refitted by two owners. It's documentation and engineering, not software: Markdown, YAML data and,
later, small calculation scripts.

## Who you're working with

- **Contributors may not know git or development tools.** Many sessions come from Claude Code on
  the web or mobile. Handle all git work for them. Explain what you did in one plain sentence, with
  no jargon ("I saved your changes and opened a pull request: <link>").
- **Reply in the language the user writes in** (often Finnish). **Write repository files in English**
  so they stay consistent.
- **The owners decide.** Recommend clearly, but record their decisions as made, including trade-offs
  they accept, e.g. "about 90 % thrust accepted for cost".
- **Cost matters.** Prefer solutions that reuse existing parts, and say when a cheaper option is good
  enough.

## Repository layout

```
vessel/       shared facts (particulars, engine, gearbox, electrical basics). Single source of truth.
hydraulics/   current-system.md, requirements.md, loads.yaml, design/, img/
electrics/    current-system.md, … (same pattern as hydraulics)
decisions.md  decision log for all systems, newest first
```

- **A new system** (e.g. `fuel/`, `water/`, `ventilation/`, `heating/`) gets its own folder, laid out
  like `hydraulics/`: README.md, current-system.md, then requirements and design notes as needed.
  Add it to the root README table.
- **A fact used by more than one system** goes in `vessel/README.md`. System docs link to it rather
  than copying it.
- **Option studies and comparisons** go in `<system>/design/<topic>.md`.

## Documentation rules

1. **Cite every fact's source** in a Source column or inline: `[owner YYYY-MM-DD]` (told by an owner),
   `[blog YYYY-MM-DD]` (plektra.github.io), `[datasheet <product>]` with a URL, or `[calc]` for your
   own calculation.
2. **Never invent numbers.** Mark unknown values `**⚠ unknown**` and uncertain ones `**⚠ verify**`. If
   you estimate, say it's an estimate and list the assumptions (oil grade, efficiencies, lengths).
3. **When new information arrives,** update every place it affects: the system doc, `vessel/` if it's
   shared, `loads.yaml`, requirements, design notes and open-question checklists (tick `[x]` when
   answered). Update the doc's status line and date.
4. **Check earlier conclusions against new facts.** If a new fact invalidates an earlier calculation
   or recommendation, fix it and say so plainly. Don't leave stale numbers behind.
5. **Record decisions** in `decisions.md` (date, system, decision, why, link), and reflect them in the
   affected docs.
6. **Units:** SI with bar, L/min, cm³ (displacement), Nm, kW, °C, mm. Give conversions only where a
   datasheet uses other units.
7. **Product links:** link datasheets by URL. Don't commit vendor PDFs. Owners' own photos and
   drawings go in `<system>/img/`.
8. **Scanned PDFs:** many datasheets are scans. If text extraction fails, render the pages to images
   and read them, then say which values were read visually.
9. **Safety-critical functions** (steering, anchoring, load holding, anything that can trap a person)
   need explicit failure-mode notes. Remind the owners that a qualified person should review them
   before building.

## Engineering assumptions in use

These apply unless a doc says otherwise. Change them here if the owners decide differently.

- Hydraulic oil ISO VG 46 (grade not yet confirmed); density 870 kg/m³.
- Gear pump volumetric efficiency 92 %, mechanical efficiency 90 %.
- Engine idle 800 rpm per the 2018 blog. **Not yet measured; could be 650–700 rpm.** See
  `vessel/README.md`.

## Git workflow (do this for the user)

- **Never commit directly to `main`.** Work on a branch; Claude Code on the web already gives each
  session one.
- **Start from the latest `main`.** If the branch is behind, update it before editing.
- **Keep commits and pull requests small,** one topic each. Write commit messages and PR descriptions
  in English. Start the PR description with a plain-language summary that a non-technical owner can
  approve from a phone.
- **Never force-push.** Never delete or overwrite someone else's content without asking.
- **If there's a merge conflict, keep both people's information** and ask the user only when the two
  versions contradict each other.
- When the user says "save", "tallenna" or "done", use the `/save` skill.

## Skills in this repository

| Skill | Use it when the user… |
|---|---|
| `/save` | wants to save or finish: commits, pushes and opens a pull request |
| `/add-info` | gives new facts, measurements, photos or datasheet values |
| `/log-decision` | says something has been decided |
| `/open-questions` | asks what's still open or missing, or what to do next |
