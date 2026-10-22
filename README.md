# Vega systems

Design and documentation for the systems of **Vega**, a 1912 steel tug being refitted for leisure
use. One repository holds every system, so the systems can reference each other.

| Folder | What's in it |
|---|---|
| [vessel/](vessel/) | Shared facts: vessel particulars, engine, gearbox, electrical basics |
| [hydraulics/](hydraulics/) | Steering, bow thruster, windlass: current system, requirements, design studies |
| [electrics/](electrics/) | Batteries, charging, distribution, links to the monitoring and control electronics |
| [decisions.md](decisions.md) | Every decision made so far, and why |
| [CLAUDE.md](CLAUDE.md) | Working rules for Claude. Humans can read it too. |

## How to contribute without knowing git

You don't need git, a terminal or any developer tools. Everything works by chatting with Claude in
the browser or on your phone.

### One-time setup

1. Create a free account at [github.com](https://github.com) and ask Lari to invite you to this
   repository.
2. Open [claude.ai/code](https://claude.ai/code), or **Code** in the Claude mobile app, and connect
   your GitHub account when asked.
3. Choose this repository.

### Every time

1. **Start a new session** for each topic, e.g. "steering cylinder measurements" or "battery bank".
2. **Talk normally**, in Finnish or English. For example:
   - *"I measured the steering cylinder: bore 63 mm, rod 32 mm, stroke 250 mm."*
   - *"What's still open on the hydraulics?"* (or type `/open-questions`)
   - *"We decided to buy the Borelli 30502 clutch."* (or `/log-decision`)
   - *"Compare these two pumps: <link>"*
3. **When you're done, say "save"** (or "tallenna", or type `/save`). Claude saves your changes and
   creates a *pull request*: a proposed change that waits for approval. You get a link.
4. **Approve it:** open the link and press **Merge pull request**. Lari can do this too. Until it's
   merged, the change isn't part of the main documents.

### Tips

- **One topic per session** keeps changes small and avoids clashes when two people edit at once.
- **Claude records where every number came from.** Say whether you measured it, read it from a
  datasheet, or are guessing.
- **Photos and PDFs:** on the GitHub website, open the system's folder, choose
  **Add file → Upload files**, and upload into its `img/` folder. Then tell Claude about them.
- **Nothing is lost.** Every change is kept in the history and can be undone. Just ask Claude.

## Related repositories

The onboard electronics (Signal K, NMEA 2000 nodes, ESP32 power distribution boards) live in
separate repositories under [github.com/plektra](https://github.com/plektra). See
[electrics/current-system.md](electrics/current-system.md).
