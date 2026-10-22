# Vega — Vessel overview

Shared facts that more than one system depends on. System-specific details live in each system's
folder (e.g. [hydraulics](../hydraulics/), [electrics](../electrics/)).

Sources: `[perustiedot]` and `[blog YYYY-MM-DD]` refer to the Plektra blog
(<https://plektra.github.io>, repo `plektra/plektra.github.io`); `[owner YYYY-MM-DD]` is information
given directly by the owners.

## Vessel

| Parameter | Value | Source |
|---|---|---|
| Name | Vega | |
| Type | Steel-hulled tug, converted to leisure use | [perustiedot] |
| Builder / year | Borgå Mekaniska Verkstad, 1912 | [perustiedot] |
| Length | 16.15 m | [perustiedot] |
| Beam | 4.16 m | [perustiedot] |
| Draft | 1.97 m | [perustiedot] |
| Displacement | **⚠ unknown** | |
| Home port | Laivalahti, Helsinki (has also operated on Saimaa) | [perustiedot], [blog 2017-07-04] |
| Helm | Single wheel, centre of the bridge | [blog 2017-04-19] |
| Rudder | Single rudder; dimensions **⚠ unknown** | |
| Bow thruster | Side-Power SH240-U11 (hydraulic), 250 mm tunnel, installed 2017 | [blog 2018-11-12] |

## Power train

| Item | Value | Source |
|---|---|---|
| Main engine | Caterpillar 3126B, 420 hp, installed 2012 | [perustiedot] |
| Engine speed range | Idle (see below) – ~2500 rpm, cruise ~1800 rpm | [blog 2018-11-12] |
| Flywheel / housing | SAE 11-1/2 flywheel, probably SAE #3 housing, with an adapter to SAE 14 | [blog 2021-02-08] |
| Gearbox (original) | Masson RSD200 (1976), removed | [blog 2019-01-24] |
| Gearbox | Advance 300, ~5.4:1, **installed and aligned** (2026) | [blog 2021-02-08], [owner 2026-10-21] |
| Gearbox PTO | 1:1, driven from the input shaft (turns in neutral), no built-in clutch, rated 0.044 kW/rpm (≈ 420 Nm), Ø48 mm keyed shaft | [owner 2026-10-21] |
| Shaft bearing | New bearing block for the propeller shaft | [owner 2026-10-21] |
| Engine status | Being remounted and aligned to the gearbox (October 2026) | [owner 2026-10-21] |
| Engine mounting | Gearbox and engine both rigidly mounted to the hull | [blog 2021-02-08] |
| Propeller | Right-handed | [blog 2019-01-24] |

### Engine idle speed

The blog quotes about 800 rpm idle [blog 2018-11-12]. **There's no official 3126B marine low-idle
figure among the sources found online** (searched 2026-10-22):

- A 3126B spec sheet on Scribd shows **700 rpm low idle**, but it's unclear which rating that applies
  to. ([source](https://www.scribd.com/document/832207648/3126B))
- An owner of twin 3126B marine engines reports idle at **about 680 rpm**, dropping to about 540 rpm
  with a "low-RPM" switch. ([source](https://forums.ybw.com/threads/low-rpm-toggle-switch.584153))
- Other Cat marine engines have a **programmable low idle of 550–750 rpm**, set in the ECM with the
  Cat ET service tool.
  ([source](https://www.cat.com/en_US/products/new/power-systems/marine-power-systems/commercial-propulsion-engines/18408926.html))

**⚠ Measure the actual idle once the engine is running**, e.g. from the engine data in Signal K.
Pump sizing on the PTO depends on it directly; see
[hydraulics/design/p2-pump-options.md](../hydraulics/design/p2-pump-options.md). A Cat dealer can
probably raise the programmed low idle if needed.

## Electrical basics

Details in [electrics/current-system.md](../electrics/current-system.md).

| Item | Value | Source |
|---|---|---|
| DC system voltage | 24 V (inferred from the 24 V emergency pump) **⚠ verify** | [blog 2018-11-12] |
| Engine alternator | 65 A | [blog 2017-07-04] |
