# Vega — Current Hydraulic System (as-built baseline)

> **Status:** Reconstructed from the Plektra blog (2016–2021), plus an owner update in October 2026
> (see §0). Items marked **⚠ verify** need checking on board.
>
> **The hydraulic system is fully disassembled right now** (October 2026). Sections 3.1–3.5 describe
> the last assembled configuration (2017–2018). Some of those parts will be reused.

## 0. Current status (owner update, 2026-10-21)

| Item | Status |
|---|---|
| Gearbox | Advance 300 is **fitted and aligned** to the propeller shaft, with a new shaft bearing block |
| Main engine | Being remounted and aligned to the gearbox |
| Hydraulics | **All disassembled**, both pumps removed. Nothing will be reassembled until the engine is aligned. |
| Planned: steering pump | Small fixed-displacement pump (P1, 16.6 cm³) goes back on the front of the engine, driven by the two belts as before. **Dedicated to steering only.** |
| Planned: auxiliary pump | Large pump **driven directly from the Advance 300 PTO** |
| Advance 300 PTO | **1:1 ratio, driven from the input shaft** (turns whenever the engine runs, in gear or neutral). **No clutch** built in. Rated **0.044 kW/rpm**, which is a constant torque limit of **≈ 420 Nm** (35 kW at 800 rpm, 110 kW at 2500 rpm). Output is a **plain 48 mm keyed shaft**, with no pump flange. |
| Planned: PTO drive line | PTO shaft → **flexible HRC 150 coupling** → clutch → P2. The clutch and pump sit on **their own mount fixed to the hull**, so the PTO shaft carries no overhung weight or side load. |
| Planned: PTO clutch | A clutch between the coupling and P2, so the pump only turns when needed. Type not chosen yet. |
| Thruster hoses | **Mostly done:** 1/2" **SAE 100R2AT / EN 853** hoses, rated 300 bar per owner, from the CETOP valves to the bow thruster. A and B lines are **8.5 m each**. |
| P2 pressure line | 3/4" hose from the pump to the valves. The move to the PTO needs **3–4 m** of hose. |
| P2 suction line | **32 mm ID** hose (≈ 1-1/4", DN32), about **3 m** to the new pump position; tank oil level about 1 m above the pump inlet |
| Auxiliary return line | 3/4" hose, **< 0.5 m**, from the valve block to the tank (through the return filter) |
| Decision: system pressure | **Keep the 250 bar class.** About 90 % thruster power is accepted to keep costs down. |

### Planned drive configuration

```
                 ┌── twin V-belts, 1:1.24 ── P1 16.6 cm³ ── steering circuit (Orbitrol + cylinder)
 CAT 3126B ──────┤
  (front)        │
                 └── flywheel ── Advance 300 ── propeller shaft
                                    │
                                    └── PTO 1:1, Ø48 keyed ── HRC 150 ── clutch ── P2 (size ⚠) ── auxiliary circuit
                                                                 └──── own hull mount ────┘
                                                                                    (thruster, windlass, …)
```

### What this means for the design

1. **P1 on the belts is a sound choice.** Steering runs at low pressure (normally < 50 bar), about
   15 L/min at idle. The belts carried this load without trouble in 2017–2018.
2. **The existing 33.5 cm³ pump is too small for the 1:1 PTO.** At 800 rpm idle it gives about
   25 L/min (92 % volumetric efficiency). That falls short of the 26.2 L/min the thruster needs for
   60 % power, and well short of the 33.8 L/min for 100 %. The 2018 blog post already noted that a
   1:1 drive would mean buying new pumps.

   | Idle rpm (PTO 1:1) | Displacement needed for 33.8 L/min | Flow at 2500 rpm | Torque at 264 bar |
   |---|---|---|---|
   | 800 | **46 cm³** | 106 L/min | 214 Nm |
   | 900 | 41 cm³ | 94 L/min | 190 Nm |
   | 1000 | 37 cm³ | 85 L/min | 172 Nm |

   *Assumes 92 % volumetric and 90 % mechanical efficiency. These are first estimates; the sizing
   library will replace them.*
3. **The input-shaft PTO turns in neutral.** That's what harbour thruster use needs.
4. **The PTO rating is about twice what's needed.** 0.044 kW/rpm works out to about 420 Nm. A 46 cm³
   pump at 264 bar needs about 215 Nm (51 %), or 18 kW of shaft power at 800 rpm. Even a 300 bar
   relief setting only needs 244 Nm (58 %), so pressure spikes have headroom.
5. **System pressure: 250 bar class, ~90 % thrust target (decided).** Full thruster power would
   need 264 bar at the motor plus line losses. The owner accepts roughly 90 % thrust to keep the
   pump and valves in the common 250 bar class and save cost. With the actual line lengths, a
   250 bar relief gives about 85–89 % thrust when warm; see item 9.
6. **The planned clutch deals with heat while cruising.** Without it, a ~46 cm³ pump would push
   about 106 L/min at 2500 rpm through the flow control all the time, which is roughly 1 kW or more
   of heat with no cooler. With the clutch disengaged, P2 doesn't turn at all.
7. **Requirements for the clutch (first draft):**
   - **Torque rating.** The steady load is about 215 Nm at 264 bar with a 46 cm³ pump. A gear pump
     with a relief valve gives pressure peaks, so plan for a service factor of about 1.5–2, i.e. a
     clutch rated for roughly **320–430 Nm**. The PTO limit is about 420 Nm, so a clutch rated for
     around 320–420 Nm fits under it, and anything much above the PTO rating adds nothing.
   - **Engagement.** Engage only at idle. An interlock on engine rpm (from N2K / Signal K) could
     block engagement above about 1000 rpm.
   - **Engage with the pump unloaded.** Keep the existing normally-open 2/2 unloading valve. Engage
     the clutch with the valve open (pump flowing freely to tank), then close the valve. This cuts
     the shock on the clutch, the PTO and the pump shaft.
   - **Type.** The PTO is a bare keyed shaft and the assembly sits on its own mount, so the clutch
     has to be a **shaft-to-shaft unit**, not one that bolts to an SAE pump flange. Typical options:
     - an electromagnetic shaft clutch in its own bearing housing, with a pump bracket on the
       output side;
     - a short jackshaft in two bearings carrying an electromagnetic clutch, with the pump on an
       SAE-flange bracket at the end;
     - a stand-alone hydraulic or mechanical "clutch PTO" unit, which has a shaft input and an SAE
       pump pad output.
   - **Control.** An electromagnetic clutch draws current and needs an output channel, which an
     ESP32 PDM channel could provide.
   - **Coupling sizing.** Check the HRC 150 element and hub against the 48 mm bore, the PTO shaft's
     key, and torque. As far as I recall, HRC 150 is rated around 600 Nm nominal, which would be
     enough, and its maximum bore depends on the hub type (F/H taper-lock vs B). **⚠ Verify both
     in the manufacturer's catalogue.**
   - **Alignment.** The gearbox is rigidly mounted to the hull (blog 2021-02-08), and so is the new
     clutch/pump mount. So the HRC only has to take up small installation misalignment and the
     hull flexing, not engine movement. Align the clutch input to the PTO shaft within the
     coupling's allowed offset and angle, and recheck after sea trials.
   - **Space.** The coupling, clutch, bearing housing and pump in a row add length. Check this
     against the hull, the gearbox and the propeller shaft bearing.
8. **The existing 1/2" thruster hoses are adequate.** At 33.8 L/min the oil moves at about
   4.5 m/s in a 12.7 mm bore, inside the usual 3–6 m/s guideline for pressure lines. Estimated
   pressure loss per metre of hose (straight hose only, ISO VG 46 assumed):

   | Oil temperature | Viscosity | Loss per metre | Loss for 2 × 8.5 m (A + B lines) |
   |---|---|---|---|
   | 5 °C (cold start) | ~380 cSt | ~2.9 bar | ~50 bar |
   | 20 °C | ~130 cSt | ~1.0 bar | ~17 bar |
   | 40 °C | 46 cSt | ~0.35 bar | ~6 bar |
   | 60 °C | ~21 cSt | ~0.30 bar | ~5 bar |

   *Straight hose only; fittings add a little more.* The hoses are SAE 100R2AT / EN 853. The
   standard's minimum working pressure for 1/2" (-08) is about 275 bar (4000 psi), and the owner
   reports 300 bar for this hose. Either way it's above the 250 bar relief setting.
   - **The return line (3/4", < 0.5 m) is negligible:** under 0.3 bar even with cold oil. The return
     filter will be the main loss on the tank side.
   - **The P2 pressure line (3/4", 3–4 m) is not a concern.** At 37 L/min (idle) the oil moves at
     about 2.2 m/s and loses under 1 bar when warm. At 106 L/min (2500 rpm, clutch engaged) it's
     about 6 m/s and 1.5–2.5 bar, which is acceptable.
   - **Use hose rather than tube for long thruster runs.** The 15×2 precision tube used elsewhere
     has an 11 mm bore. At this flow that's about 5.9 m/s and roughly twice the loss of the hose.
9. **Expected thruster thrust is about 85–89 % when the oil is warm, slightly under the 90 % target.**
   The relief valve caps pressure at the manifold at 250 bar. Losses in the valve, hoses and return
   line come out of that, so the motor gets less. Propeller torque rises with the square of speed,
   so the thruster settles at a lower speed, and the excess flow goes over the relief valve.

   | Oil temperature | Propeller speed | Thrust | Power |
   |---|---|---|---|
   | 5 °C | ~86 % | ~74 % | ~64 % |
   | 20 °C | ~92 % | ~84 % | ~77 % |
   | 40 °C | ~94 % | ~88 % | ~82 % |

   *Assumes about 6 bar loss per valve path (P→A and B→T), the measured line lengths, and about
   1.5 bar for the return filter. With 4–10 bar per valve path the warm result ranges from 85 to 89 %. **⚠ Get the
   BAV-713 pressure-drop curve** to tighten this.*

   The cheapest way to reach a true ~90 % is to set the relief to about **260–265 bar**, provided
   the new pump and the CETOP valves are rated for it. The hoses (300 bar) already are. Check this
   when choosing the pump; many gear pumps are rated around 250 bar continuous and 280 bar peak.
10. **P2 suction line: the owner confirmed 32 mm ID (≈ 1-1/4"), which is adequate.** Use the 1-1/4"
   column in the inlet-pressure table below. The 1" analysis is kept for reference.

   *Original analysis, which assumed a 1" (3 m) line: fine when warm but marginal with cold oil.* Oil moves at
   about 1.2 m/s at idle (46 cm³, 800 rpm), which is at the usual ~1.2 m/s limit for suction.
   Estimated hose loss alone, before the tank outlet, ball valve and fittings:

   | Oil temperature | 800 rpm (37 L/min) | 1000 rpm (46 L/min) | 1200 rpm (55 L/min) |
   |---|---|---|---|
   | 5 °C | ~0.60 bar | ~0.75 bar | ~0.90 bar |
   | 20 °C | ~0.21 bar | ~0.26 bar | ~0.31 bar |
   | 40 °C | ~0.07 bar | ~0.09 bar | ~0.11 bar |

   Gear pumps typically need inlet pressure no lower than about −0.2 to −0.3 bar gauge. **Check the
   chosen pump's datasheet.** With cold oil the hose alone takes more than that, so cold starts
   risk cavitation, which is noisy and wears the pump. Ways to reduce the risk, cheapest first:
   - **Flooded suction:** keep the tank oil level above the pump inlet. Each metre of head gives
     about +0.085 bar.
   - **Use 1-1/4" suction hose.** Laminar loss scales with 1/D⁴, so this cuts the loss to about 40 %
     (≈ 0.25 bar at 5 °C, idle). The tank muffs are 1", so it needs an adapter at the tank or a
     larger muff.
   - **Choose a higher-VI or thinner oil** (HV 32/46 multigrade). This mainly helps cold starts.
   - **Operating rule:** don't engage the clutch, or hold off running the thruster hard, until the
     oil has warmed.

   **With the tank oil level about 1 m above the pump inlet (owner, 2026-10-21)**, the tank adds about
   +0.085 bar. Estimated pump inlet pressure, including about K = 2.5 of fitting losses (tank outlet,
   ball valve, elbows):

   | Oil temperature | 1" at 800 rpm | 1" at 1000 rpm | 1-1/4" at 800 rpm | 1-1/4" at 1000 rpm |
   |---|---|---|---|---|
   | 5 °C | −0.53 bar | −0.69 bar | −0.17 bar | −0.23 bar |
   | 15 °C | −0.22 bar | −0.30 bar | −0.04 bar | −0.07 bar |
   | 20 °C | −0.14 bar | −0.20 bar | −0.01 bar | −0.03 bar |
   | 40 °C | 0.00 bar | −0.03 bar | +0.05 bar | +0.04 bar |

   **Departure is the critical case.** The thruster is needed right after the engine starts, when
   the oil is at engine room temperature. With the clutch disengaged, only the steering circuit
   warms the shared tank. On a Finnish summer day (15–20 °C), 1" sits right at the typical −0.2 bar
   limit. In spring and autumn it's well below. **Recommendation:** make the new 3 m suction hose
   **1-1/4"**, since it's being made anyway. That keeps the inlet within about −0.2 bar down to about
   5 °C. Adding HV-grade oil gives more margin.

   At 2500 rpm the flow would reach about 3.5 m/s in a 1" line, so the clutch should still disengage
   automatically above roughly 1000–1200 rpm.
11. **If the engine is revved while the clutch is engaged,** pump flow rises with rpm (about 106 L/min
   at 2500 rpm). The flow control valve and the return line must handle that, or the clutch must be
   disengaged automatically above a set rpm. Check the rated inlet flow of the VPR3 (35 L/min
   regulated).
>
> Sources are cited as `[blog YYYY-MM-DD]` and refer to posts in `plektra.github.io/_posts/`.

## 1–2. Vessel and power train

Moved to the shared [vessel overview](../vessel/README.md), which also covers the electrical basics
used by other systems.

## 3. Hydraulic system overview

The original "tractor" system (belt-driven pump with integral tank, Orbitrol, directional valve
and a leaking cylinder) was replaced in 2017 by a **two-circuit design** [blog 2017-04-01]:

- **Circuit 1 — Steering:** small pump → priority flow control → Orbitrol → steering cylinder.
  Only the rudder is on this circuit, by design, for safety.
- **Circuit 2 — Auxiliary:** large pump → flow control → unloading valve → CETOP 3 manifold →
  bow thruster (and later the windlass and other loads).
- **Emergency:** 24 V electric pump, which feeds the steering circuit through a check valve.
- **Gearbox clutch hydraulics** are a separate circuit and out of scope here.

![Hydraulic schematic v3, 2018](img/hydraulics-v3-2018.png)

*Schematic v3 from the blog (Finnish labels: virtauksensäätö = flow control,
suuntaventtiili = directional valve, pohjalaatta = subplate, paineenrajoitus = relief valve).*

### 3.1 Pump drive (as of 2018)

| Item | Value | Source |
|---|---|---|
| Drive | V-belts (Optibelt Super X-Power) from the crankshaft, through a support bearing unit to two tandem pumps | [blog 2017-07-04] |
| Pulley / ratio | 180 mm pulley; engine:pump = 1:1.24 | [blog 2017-07-04] |
| Pump mounting | 10 mm steel bracket bolted to the engine block, 10.9 bolts | [blog 2017-07-04] |
| **Known limitation** | Belts slip above **~160 bar** on the auxiliary pump (~9 kW). Not safe for continuous use. | [blog 2018-11-12] |
| Planned fix (2018) | Pumps moved to the front of the engine on a cardan shaft (1:1), so new pumps would be needed | [blog 2018-11-12] |
| Planned fix (2021) | Drive the large pump from the PTO on the new gearbox | [blog 2021-02-08] |
| Decision (2026) | P1 on the front belts (steering only); P2 on the gearbox PTO. The front cardan idea has been dropped. | owner 2026-10-21 |

### 3.2 Pumps

| Pump | Make | Displacement | Rating (schematic) | Flow @ 800 / 1800 / 2500 rpm engine* | Feeds |
|---|---|---|---|---|---|
| P1 | Salami, gear | 16.6 cm³/rev | 250 bar, 16–40 L/min | 16.5 / 37.1 / 51.5 L/min | Steering |
| P2 | Salami, gear (group 3) | 33.5 cm³/rev | 250 bar, 30–80 L/min | 33.2 / 74.8 / 103.8 L/min | Auxiliary |
| P3 | Recovered from an old power pack; motor 24 V, 2.5 kW | **⚠ unknown** | | | Emergency steering |

\* Calculated with the 1:1.24 belt ratio and 100 % volumetric efficiency. At 2500 rpm engine speed
the pumps turn at ~3100 rpm, and both flows are above the ratings on the schematic.
**⚠ Check the pumps' maximum allowed speed** if the belt drive is still in use.

### 3.3 Circuit 1 — Steering

| Component | Spec | Notes |
|---|---|---|
| Flow control | RPF3, priority flow 20 L/min, excess to tank | At idle the pump gives ~16.5 L/min, so all of it reaches the Orbitrol |
| Steering unit | Orbitrol "160/4" (presumably 160 cm³/rev) **⚠ verify** type (open/closed centre, load reaction) | |
| Cylinder | Double-acting; bore / rod / stroke **⚠ unknown** | Fitted to the original hole near the rudder stock. Doesn't quite reach hard over to port, and the hole is slightly oversized. Might be replaced with a longer cylinder [blog 2017-07-04] |
| Emergency bypass | Hand valve across A–B at the cylinder, for steering with a removable emergency tiller | [blog 2017-07-04] |
| Working pressure | Normally < 50 bar | [blog 2017-07-04] |
| Relief setting | **⚠ unknown** | |
| Emergency supply | P3 via check valve into the RPF3 inlet | Planned in 2017. **⚠ verify** it's installed. The 65 A alternator can't sustain it for long. |
| Bleeding | No bleed screws; cylinder ports face sideways | Hard to bleed [blog 2017-07-04] |

### 3.4 Circuit 2 — Auxiliary

| Component | Spec | Notes |
|---|---|---|
| Flow control | VPR3, pressure-compensated, 35 L/min, excess to tank | |
| Unloading valve | 2/2 solenoid, normally open, teed after the VPR3 | De-energised means P2 flow goes to tank at low pressure. Energised means flow goes to the manifold. |
| Manifold | CETOP 3, 4-station subplate, relief valve set to 250 bar. **Relief valve rated up to 300 bar, 80 L/min** (owner 2026-10-22). | 1 station used, 3 spare (windlass etc.) |
| Thruster valve | BAV-713 4/3 solenoid, A-B-T open centre (motor freewheels in neutral) | |
| Pressure gauge | P-line before the subplate | Not shown on the schematic |
| Bow thruster | Side-Power SH240-U11 | Motor case drain goes to tank |
| Thruster demand | 100 %: 264 bar × 33.8 L/min (≈ 14.9 kW hydraulic); 60 %: 158 bar × 26.2 L/min (≈ 6.9 kW) | Manufacturer data [blog 2018-11-12] |
| Achieved (belt drive) | ~160–170 bar, which was enough to turn the boat at the quay | [blog 2018-11-12] |
| Windlass | Has a hydraulic motor; specs **⚠ unknown**, not yet connected (2018) | [blog 2017-04-01] |

### 3.5 Reservoir, fluid and piping

| Item | Value | Source |
|---|---|---|
| Reservoir | Flowfit 100 L steel, mounted on 50×50×5 angle brackets on the frames | [blog 2017-04-01] |
| Oil fill | 80 L | [blog 2017-07-04] |
| Oil type / grade | **⚠ unknown** | |
| Suction lines | 2017 plan: 2 × 1" (engine pumps) and 1 × 3/4" (electric pump), each with a ball valve. **2026: the P2 outlet matches its 32 mm hose.** | [blog 2017-04-10], owner 2026-10-21 |
| Tank-top components | Flow control valves, return filter, filler/breather cap | [blog 2017-04-10] |
| Return filter | Has a pressure gauge; it's hard to read in its current position | [blog 2017-04-10] |
| Hard piping | 15×2 precision steel tube for long runs, hoses elsewhere | [blog 2017-04-01] |
| Oil cooler | None in either circuit **⚠ verify** | |
| Daily fuel tank | 150 L, located below the hydraulic reservoir | [blog 2017-04-19] |
| Main supplier | SixTek (hydrauliikkapumppu.fi) | [blog 2017-04-01] |

## 4. Known issues and lessons learned

1. **The belt drive can't carry full thruster power.** It slips at about 160 bar, while the
   thruster needs about 15 kW at 264 bar. This is the main reason to redesign the drive.
2. **Fixed-displacement pumps on a variable-speed engine.** Flow scales with engine rpm, and the
   excess is throttled to tank. That wastes power and heats the oil, and there's no cooler.
3. **Steering cylinder geometry.** It doesn't reach hard over to port, and the mounting hole is
   oversized.
4. **Bleeding is difficult.** There are no bleed points, and the cylinder ports face sideways.
5. **Emergency electric pump.** A 2.5 kW motor at 24 V draws roughly 100+ A, which the 65 A
   alternator can't sustain.
6. **Return filter gauge** is in a poor position for reading.

## 5. Open questions (current state, 2026)

- [x] Pump drive: P1 on the front belts, P2 on the gearbox PTO (planned; all disassembled now)
- [x] Advance 300 installed and aligned
- [x] Advance 300 PTO: 1:1, input shaft (turns in neutral), no clutch built in
- [x] Advance 300 PTO rating: 0.044 kW/rpm (≈ 420 Nm)
- [x] Advance 300 PTO output: Ø48 mm keyed shaft, no flange; HRC 150 coupling to a hull-mounted clutch + pump
- [x] Thruster pressure: 250 bar class, ~90 % thrust accepted
- [ ] HRC 150: torque rating, maximum bore and hub type for 48 mm (catalogue)
- [x] Thruster hoses: 1/2", 300 bar, A and B 8.5 m each
- [x] P2 pressure line: 3/4" hose, 3–4 m
- [x] P2 suction line: 1", about 3 m
- [x] Return line from the CETOP T port to the tank: 3/4", < 0.5 m
- [x] Tank oil level about 1 m above the P2 inlet (flooded suction)
- [x] Suction hose: 32 mm ID (≈ 1-1/4"), adequate per item 10
- [x] Suction connection at the tank: outlet matches the 32 mm hose (no 1" restriction)
- [ ] Chosen pump's minimum inlet pressure (datasheet)
- [ ] Hydraulic oil grade (HV 32/46 recommended)
- [ ] BAV-713 pressure drop at ~34 L/min (P→A, B→T)
- [ ] Relief: stay at 250 bar (~85–89 % thrust) or ~260–265 bar (~90 %) if the pump and valves allow
- [ ] Clutch: shaft-to-shaft electromagnetic vs jackshaft + clutch vs stand-alone clutch PTO unit
- [ ] PTO clutch: type (electromagnetic / hydraulic), torque rating, mounting space
- [ ] P2: new pump of about 40–46 cm³ (the 33.5 cm³ Salami is too small at 1:1; see §0)
- [ ] Engine idle rpm after the refit, and whether a raised "thruster idle" is acceptable
- [ ] Is the windlass connected? What are its motor make, model and displacement?
- [ ] Is the emergency electric pump connected?
- [ ] Steering cylinder bore / rod / stroke, tiller arm length, rudder area and type
- [ ] Orbitrol model (open/closed centre, load-reacting?) and any autopilot
- [ ] Relief settings on circuit 1
- [ ] Hydraulic oil type and grade
- [ ] DC system voltage, house bank capacity, generator
- [ ] Any changes since 2021 that the blog doesn't cover
- [ ] What's wrong with the current system or missing from it, i.e. why redesign now?
