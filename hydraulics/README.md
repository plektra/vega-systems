# Hydraulics

Steering, bow thruster, windlass and future hydraulic loads.

| File | What it is |
|---|---|
| [current-system.md](current-system.md) | As-built baseline, current refit status (§0), design implications, open questions |
| [requirements.md](requirements.md) | Requirements template, partly filled in |
| [loads.yaml](loads.yaml) | Load register: numbers for each hydraulic load (machine-readable) |
| [design/p2-pump-options.md](design/p2-pump-options.md) | Auxiliary pump and PTO clutch options, with candidate products evaluated |
| [img/](img/) | Schematics and photos |

## Current state in one paragraph

Everything hydraulic is disassembled while the engine is realigned to the new Advance 300 gearbox.
The plan has two circuits:
- **Steering:** a 16.6 cm³ gear pump, belt-driven from the front of the engine, feeding the
  Orbitrol and steering cylinder.
- **Auxiliary:** a new group-3 gear pump driven from the gearbox PTO through an HRC coupling and a
  mechanical clutch, feeding the bow thruster (and later the windlass) through the CETOP 3 manifold.
  Relief at 250 bar, about 90 % thrust accepted.

The clutch choice (Borelli 30500 recommended) and the pump size (43–51 cm³) depend on the engine's
real idle speed.
