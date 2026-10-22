# Vega Hydraulic System — Requirements

> **Status:** Draft template. Fill in `TBD` fields and delete guidance notes (lines starting with `>`)
> once each section is settled.
>
> The load register in [`loads.yaml`](loads.yaml) is the source of truth for per-load numbers.
> This document holds the context, scenarios and constraints around them.

| Field | Value |
|---|---|
| Document owner | TBD |
| Revision | 0.1 |
| Last updated | TBD |

---

## 1. Scope and goals

> One paragraph: what the hydraulic system is for, what is explicitly out of scope, and what
> "done" means (learning exercise, concept design, build-ready design).

- **Purpose:** TBD
- **In scope:** TBD
- **Out of scope:** TBD
- **Deliverable:** TBD (concept / detailed design / build-ready)
- **New build or retrofit:** Retrofit / redesign of the existing two-circuit system. The baseline is in
  [current-system.md](current-system.md).

## 2. Vessel particulars

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| Vessel type | Steel tug (1912), leisure use | | See [current-system.md](current-system.md) |
| Length overall (LOA) | 16.15 | m | |
| Length of waterline (LWL) | TBD | m | |
| Beam | 4.16 | m | |
| Draft | 1.97 | m | |
| Displacement (loaded) | TBD | t | |
| Max speed | TBD | kn | Drives rudder torque |
| Cruising speed | TBD | kn | |
| ISO 12217 design category | TBD | | A / B / C / D |
| Classification / flag regime | TBD | | Recreational, commercial, class society |
| Operating area | Gulf of Finland (Helsinki); has also operated on Saimaa | | Brackish and fresh water |
| Crew / operating mode | TBD | | Short-handed? Shapes automation and alarm needs |

### 2.1 Rudder data (if steering is in scope)

| Parameter | Value | Unit |
|---|---|---|
| Number of rudders | 1 | |
| Rudder area (each) | TBD | m² |
| Rudder type | TBD | spade / skeg-hung / balanced |
| Balance ratio | TBD | % |
| Max rudder angle (hard over) | TBD | ° each side |
| Required hard-over to hard-over time | TBD | s |
| Rudder stock diameter | TBD | mm |
| Max rudder torque (calculated or from builder) | TBD | kNm |

## 3. Operating environment

| Parameter | Min | Max | Unit | Notes |
|---|---|---|---|---|
| Engine room ambient temperature | TBD | TBD | °C | |
| Seawater temperature | TBD | TBD | °C | Cooling capacity for oil coolers |
| Static heel | | TBD | ° | Reservoir suction must stay covered |
| Dynamic roll | | TBD | ° | |
| Trim | TBD | TBD | ° | |
| Vibration / shock | | TBD | | Mounting and hose selection |
| Max noise in accommodation | | TBD | dB(A) | Power pack placement and isolation |

## 4. Power sources

> List every possible source of hydraulic power. The architecture choice (engine PTO vs electric
> power pack vs both) depends heavily on this section.

### 4.1 Main engine(s) / PTO

| Parameter | Value | Unit |
|---|---|---|
| Engine make / model | Caterpillar 3126B, 420 hp | |
| Number of engines | 1 | |
| Idle / max rpm | ~800 / ~2500 (cruise ~1800) | rpm |
| PTO available (front crank / gearbox / SAE pad) | Front crank belts → steering pump P1 (good for low power only; slipped above ~9 kW). Advance 300 gearbox PTO → auxiliary pump P2. | |
| Gearbox PTO ratio / max torque / clutched? | 1:1 / 0.044 kW/rpm ≈ 420 Nm / no clutch built in; separate clutch planned between PTO and pump | – / Nm / – |
| Gearbox PTO turns in neutral? | yes (driven from the input shaft) | |
| PTO max torque / power | TBD | Nm / kW |
| Is hydraulic power needed with engine(s) off? | TBD | yes / no — anchoring under sail, harbour |

### 4.2 Electrical

| Parameter | Value | Unit |
|---|---|---|
| DC system voltage | 24 (to be confirmed) | V |
| Engine alternator | 65 | A |
| House bank capacity | TBD | Ah |
| Max continuous DC draw available for hydraulics | TBD | A |
| Generator (AC) | TBD | kVA, V, Hz |
| Shore power | TBD | A, V, Hz |

## 5. Hydraulic loads (summary)

> Detailed numbers live in [`loads.yaml`](loads.yaml). Keep this table as a quick overview.

| ID | Function | In scope | Criticality | Notes |
|---|---|---|---|---|
| STR | Steering / autopilot | yes | critical | Existing: Orbitrol + cylinder, dedicated circuit |
| BTH | Bow thruster | yes | high | Existing: Side-Power SH240-U11, 264 bar × 33.8 L/min |
| STH | Stern thruster | TBD | high | |
| WLS | Anchor windlass | yes (to be confirmed) | high | Existing hydraulic motor, specs unknown |
| CAP | Capstan / warping winch | TBD | medium | |
| STB | Stabilisers (fins / gyro) | TBD | medium | |
| DAV | Tender davit / crane | TBD | medium | |
| PAS | Passerelle / swim platform | TBD | low | |
| SWL | Sail winches / furlers | TBD | medium | Sailing vessels |
| KEL | Lifting keel / centreboard | TBD | high | |
| EXISTING | Existing equipment to integrate | TBD | | Retrofit only |

## 6. Operating scenarios (simultaneity)

> Pump sizing is set by the worst *realistic* combination of loads, not the sum of all of them.
> List the scenarios and which loads run at the same time in each.

| Scenario | Description | Simultaneous loads | Duration | Engine running? |
|---|---|---|---|---|
| S1 Harbour manoeuvring | Docking, tight turns | STR, BTH, STH | TBD | TBD |
| S2 Anchoring | Dropping / recovering anchor | WLS, STR, BTH | TBD | TBD |
| S3 Passage | Long-duration steering at sea | STR, STB | hours | TBD |
| S4 Tender launch | At anchor | DAV | TBD | TBD |
| S5 Emergency | Main power source lost | STR (minimum) | TBD | no |

**Design-driving scenario:** TBD

## 7. Safety, redundancy and failure behaviour

> For each critical function, decide what happens when the pump, power source, a hose or the
> controller fails. This is the part where human engineering judgement matters most.

| Function | Failure | Required behaviour | Backup means |
|---|---|---|---|
| Steering | Hydraulic pump / power loss | TBD | Emergency tiller / second pump / manual helm pump |
| Steering | Hose / fitting rupture | TBD | Isolation valves, separate circuits |
| Windlass | Power loss with anchor partly up | Hold load (brake / counterbalance valve) | Manual recovery |
| Thrusters | Overload / overheating | TBD | Relief valve, thermal cut-out |
| All | Low oil level | Alarm, then protective shutdown of non-critical loads | |
| All | High oil temperature | Alarm at TBD °C, shutdown at TBD °C | |

- **Emergency stop philosophy:** TBD
- **Load priority** (which loads get shed first when demand exceeds supply): TBD
- **Relief / max system pressure:** Auxiliary circuit 250 bar (decided; ~90 % thruster power accepted for
  cost). Steering circuit TBD.
- **Protection against unintended movement** (davit, passerelle, keel): TBD

## 8. Installation constraints

| Item | Constraint |
|---|---|
| Space for power unit / reservoir | TBD (location, L×W×H) |
| Reservoir location relative to pumps | TBD (flooded suction preferred) |
| Weight budget | TBD kg |
| Pipe / hose routing | Thruster A/B lines: 1/2" hose, already installed (CETOP → bow). Rest TBD (bulkhead penetrations, fire zones). |
| Access for service | TBD (filters, sight glass, bleed points) |
| Oil cooler | TBD (seawater / keel cooler / air) |

## 9. Fluid, cleanliness and maintenance

| Item | Requirement |
|---|---|
| Fluid type | TBD (mineral HLP / HVLP, or environmentally acceptable HEES per ISO 15380) |
| Viscosity grade | TBD (ISO VG 32 / 46) |
| Target cleanliness | TBD (ISO 4406 code, set by the most sensitive component) |
| Filtration | TBD (return / pressure / offline) |
| Service interval | TBD |
| Spill containment | TBD |

## 10. Monitoring, control and integration

> Integration with the existing Vega stack: Signal K server, NMEA 2000 nodes and ESP32 PDM
> boards. Signal K has no standard hydraulics paths, so the paths below are a proposal.

### 10.1 Sensors

| Measurement | Location | Range | Proposed Signal K path | Alarm / limit |
|---|---|---|---|---|
| System pressure | Pump outlet | TBD bar | `hydraulics.<system>.pressure` | TBD |
| Oil temperature | Reservoir / return | TBD °C | `hydraulics.<system>.temperature` | TBD |
| Oil level | Reservoir | % | `hydraulics.<system>.level` | TBD |
| Filter differential pressure | Return filter | switch / bar | `hydraulics.<system>.filter.clogged` | TBD |
| Pump running / hours | Power pack | bool / h | `hydraulics.<system>.pump.runTime` | |
| Rudder angle | Rudder stock | ± ° | `steering.rudderAngle` (standard) | |

### 10.2 Control

- **Control interfaces:** TBD (helm stations, wireless remotes, MFD, autopilot)
- **Control electronics:** TBD (proportional valve drivers, ESP32 PDM outputs, CAN/N2K)
- **Autopilot interface:** TBD (autopilot make, reversing pump vs solenoid valve drive)
- **Interlocks:** TBD (e.g. no windlass with chain locker hatch open, no passerelle underway)

## 11. Standards and regulations

> Tick the ones that apply. Check the current edition of each before relying on it.

- [ ] ISO 10592 — Small craft: hydraulic steering systems
- [ ] ISO 4413 — Hydraulic fluid power: general rules and safety requirements
- [ ] ISO 1219-1 / -2 — Fluid power graphical symbols and circuit diagrams
- [ ] ISO 4406 — Hydraulic fluid cleanliness coding
- [ ] ISO 15380 — Environmentally acceptable hydraulic fluids
- [ ] ISO 10133 / ISO 13297 — Small craft DC / AC electrical systems
- [ ] Recreational Craft Directive 2013/53/EU (if CE marked)
- [ ] Class society rules: TBD
- [ ] Flag state / commercial code: TBD
- [ ] Manufacturer installation requirements for selected equipment

## 12. Verification and acceptance

| Requirement | Verification method | Acceptance criterion |
|---|---|---|
| Hard-over to hard-over time | Sea trial | ≤ TBD s at max speed |
| Windlass recovery speed | Harbour test | ≥ TBD m/min at working load |
| Thruster continuous run | Harbour test | TBD min without exceeding TBD °C |
| Max oil temperature (design scenario) | Simulation, then trial | ≤ TBD °C |
| Pressure test | Bench / installed | TBD × max working pressure for TBD min |
| Noise in accommodation | Measurement | ≤ TBD dB(A) |

## 13. Assumptions and open questions

| # | Item | Type | Owner | Status |
|---|---|---|---|---|
| 1 | Vessel type, size and loads still to be confirmed | question | | open |
