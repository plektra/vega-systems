# Vega — Current Electrical System (as-built baseline)

> **Status:** Skeleton, started 2026-10-22. Only the facts below are known so far, mostly from the
> 2017 blog. Items marked **⚠ verify** need checking on board. Add to this as information comes in.

## 1. DC system

| Item | Value | Source |
|---|---|---|
| System voltage | 24 V **⚠ verify** (inferred from the 24 V emergency hydraulic pump) | [blog 2018-11-12] |
| House batteries | 2 × (type, capacity **⚠ unknown**) | [blog 2017-04-10] |
| Start batteries | 2 × (type, capacity **⚠ unknown**) | [blog 2017-04-10] |
| Battery location | Hung below the deck on the starboard side of the engine room | [blog 2017-04-10] |
| Engine alternator | 65 A | [blog 2017-07-04] |
| Charging from shore | **⚠ unknown** | |

## 2. AC system

| Item | Value | Source |
|---|---|---|
| Generator | Space reserved on the port side of the engine room; **⚠ verify** whether one is installed | [blog 2017-04-19] |
| Shore power | **⚠ unknown** | |
| Inverter | **⚠ unknown** | |

## 3. Large DC loads

| Load | Power / current | Notes | Source |
|---|---|---|---|
| Emergency hydraulic pump (steering backup) | 2.5 kW, 24 V (~100+ A) | The 65 A alternator can't sustain it for long | [blog 2017-07-04] |
| Bow thruster | — | Hydraulic, driven from the gearbox PTO; no electrical load except its valve solenoids | [blog 2018-11-12] |

## 4. Monitoring, networking and power distribution

The electronics are developed in separate repositories under
[github.com/plektra](https://github.com/plektra). They may be moved into this monorepo later.

| Item | Repository / location | Notes |
|---|---|---|
| Signal K server | `signalk-server`, `signalk-grafana`, `mainorg-signalk-datasource` | Data hub; Grafana dashboards |
| NMEA 2000 nodes | `plektra/vega-n2k-node1` … `node3`, `vega-n2k-node-bootstrap` | ESP32-based N2K nodes |
| Power distribution (PDM) | `ESP32-PDM`, `ESP32-PDM-v1/v2/4x4/base` (KiCad) | ESP32 power distribution modules; candidates for driving hydraulic solenoids and the PTO clutch actuator |
| Provisioning | `plektra/vega-ansible` | Configuration of the onboard computers |
| Other | `yarrboard-hardware`, `frothfet`, `esp32-can-hat`, `SH-ESP32-hardware` | Related hardware projects |

## 5. Open questions

- [ ] Confirm the 24 V DC system voltage
- [ ] Battery types and capacities (house and start)
- [ ] Charging sources: alternator(s), shore charger, solar
- [ ] Generator and shore power: installed or planned?
- [ ] Main switchboard and distribution layout
- [ ] Which hydraulic functions need electrical control (solenoid valves, PTO clutch actuator, sensors), and from which PDM outputs
