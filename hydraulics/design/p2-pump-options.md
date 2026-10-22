# P2 (auxiliary circuit) pump options

> **Status:** Option study, draft 2026-10-21. No decision yet.
> Context: [current-system.md §0](../current-system.md). Prices are rough indications only; get
> quotes before deciding.

## Fixed constraints

| Constraint | Value |
|---|---|
| Drive | Advance 300 PTO, 1:1 from the input shaft, Ø48 keyed, HRC 150 coupling, clutch, pump on its own hull mount |
| PTO torque limit | ≈ 420 Nm (0.044 kW/rpm) |
| Engine speed while thrusting | ~800 rpm idle (clutch interlocked off above ~1000–1200 rpm) |
| Design load | Side-Power SH240: 264 bar × 33.8 L/min at 100 %. Accepted: ~90 % thrust. |
| Pressure class | 250 bar (cost decision); hoses rated 300 bar |
| Future loads | Windlass (motor fitted, specs unknown), 3 spare CETOP 3 stations |
| Suction | 32 mm, 3 m, tank about 1 m above the inlet |

## Duty cycle: why efficiency matters less than it seems

The clutch disconnects P2 whenever no auxiliary load is in use, so the pump only turns during
thruster and windlass use. That's usually short bursts in harbour.

Estimated heat during a thruster run with a 46 cm³ gear pump at 800 rpm, 250 bar and 40 °C oil:

| Item | Value |
|---|---|
| Shaft power in | ~17 kW |
| Thruster motor output | ~11 kW |
| Heat into the oil | **~6 kW** (pump, valves, hoses, ~2 L/min over the relief valve) |
| Oil temperature rise, 80 L, no cooler | ~2.7 K per minute of continuous thrusting |

Typical manoeuvring is 1–2 minutes of intermittent use, which adds about 3–5 K. That's harmless.
A long continuous run of 5 minutes or more adds over 13 K, and the Side-Power motor has its own
duty-cycle limits anyway. **Heat is not a reason to leave the fixed pump for thruster-only use.**
It does become one if the windlass runs for long periods, or if loads ever run without the clutch.

## Options

### A. External gear pump, fixed displacement, ~46 cm³ (baseline)

The 2017 design, sized up for the 1:1 PTO.

- **Pros:** cheapest option (roughly €200–500). Robust and tolerant of dirty oil. Simple and
  easy to source in Finland (the same types as the Salami pumps). Works with the existing VPR3,
  2/2 unloading valve and CETOP manifold unchanged.
- **Cons:** flow is tied to rpm, with the excess throttled or sent over the relief valve. About
  80–85 % overall efficiency. Noisier than piston pumps. Group-3 pumps are typically rated about
  250 bar continuous and 280 bar peak, so there's no headroom above the 250 bar class.
- **Fit:** matches the cost-managed brief. The clutch takes care of the main weakness, which is
  wasted flow while cruising.

### B. Smaller gear pump (~37 cm³) plus a raised "thruster idle" of ~1000 rpm

- **Pros:** a cheaper and smaller pump, and less wasted flow if the clutch is ever engaged at higher
  rpm. Lower torque (~172 Nm).
- **Cons:** someone has to raise the engine speed before using the thruster. Forgetting gives about
  25 % less flow, which means weaker thrust exactly when manoeuvring. Higher rpm in harbour is also
  noisier, and the propeller pushes harder if the boat is in gear.
- **Fit:** only worth it with an automatic rpm raise, e.g. a thruster-active signal to the engine
  throttle. Find out whether the 3126B's electronic control has a usable input. **⚠ Check.**

### C. Bent-axis piston pump, fixed displacement (truck PTO pump)

Typical makes: Parker F1/F2, Sunfab SC, Danfoss/Hydro Leduc and similar, in sizes around 40–47 cm³.

- **Pros:** about 90–95 % efficient, quiet, compact, designed for PTO duty. Rated about
  **350–400 bar**, so it can run the relief at 265–280 bar and give ~100 % thrust without being
  stressed. Widely available second-hand from the truck and crane market. 47 cm³ at 280 bar is about
  230 Nm, which is fine for the PTO.
- **Cons:** costs more than a gear pump (roughly €700–1500 new). Needs cleaner oil (target about ISO
  4406 18/16/13). Mounting flanges are usually ISO 7653 truck pattern, so it needs an adapter plate on
  the hull mount. Still fixed displacement, so the flow-versus-rpm behaviour is the same as A.
- **Before raising pressure, check:** the CETOP valves' P/A/B ratings, the BAV-713 rating, and the
  Side-Power motor's maximum pressure. The hoses (300 bar) are fine.
- **Fit:** the best upgrade if you want full thrust and lower losses without changing the circuit.

### D. Variable-displacement axial piston pump, pressure-compensated (PC)

- **Pros:** reduces its displacement to deliver only the flow being used, so nothing is dumped over
  the relief valve and there's no throttling loss in a flow-control valve. Could eventually make the
  VPR3 unnecessary.
- **Cons:** costs about €1500–3000. With no flow demand it still sits at full compensator pressure
  (250 bar), so the case drain leaks and the pump runs hot when idling. You'd still want the clutch.
  Needs a case drain line to tank and cleaner oil. Bigger and heavier.
- **Fit:** weak for this duty cycle. Its savings mostly come when loads run for long periods.

### E. Load-sensing (LS) variable pump plus proportional LS valves (e.g. a sectional mobile valve)

- **Pros:** the most capable system. The pump runs at about 20–30 bar above the highest load
  pressure and idles at about 20–30 bar when nothing is used. **Proportional** control of the
  thruster and windlass. Flow sharing when several loads run at once. Expandable to a davit or other
  loads. Efficient enough to run without a clutch, although keeping it is still sensible.
- **Cons:** the most expensive option. Pump plus LS valve bank roughly €3000–6000 or more. **Replaces
  the existing CETOP manifold, BAV-713, VPR3 and 2/2 valve.** Needs an LS signal line, cleaner oil
  and more complex commissioning. The Side-Power SH240 control is on/off today; proportional
  thrust needs its own proportional valve and driver.
- **Fit:** worth considering only if proportional control or many simultaneous loads become goals.
  That's a scope change, not a pump swap.

### F. Tandem gear pump (e.g. 25 + 20 cm³) with one section unloaded

- **Pros:** both sections deliver for the thruster at idle. One section can feed the windlass on its
  own circuit, or be unloaded to tank at low pressure to cut waste. Cheap parts.
- **Cons:** more valves and plumbing. The clutch already covers most of the efficiency benefit.
  Longer pump assembly.
- **Fit:** interesting only if the windlass ends up needing its own flow while the thruster runs.

### Not viable: electric power pack for the thruster

About 15 kW hydraulic is about 750 A at 24 V. That needs a dedicated AC generator or a very large
battery bank. Hydraulic PTO drive is the reason the SH240 was chosen. (A small electric pack still
makes sense as **emergency steering backup** at about 2.5 kW, as planned in 2017.)

## Candidate under evaluation: Flowfit ZZ009520 (option A with a mechanical clutch)

[Group 3 Mechanical Clutch & Pump Assembly, 43cc, 77.4 L/min](https://www.flowfitonline.com/products/group-3-mechanical-clutch-pump-assembly-43cc-77-4-l-min),
about £526 + VAT (October 2026). Data comes from the Flowfit datasheet PDF linked on the product
page, which is a scanned 3-page PDF read visually. Items marked *(page)* come from a summary of the
product page and weren't read verbatim.

| Item | Value | Source |
|---|---|---|
| Assembly rating | 200 bar working, 30 kW absorbed, 77.4 L/min at 1800 rpm | *(page)* |
| Pump | VNK3 group 3 gear pump, 43 cm³, European flange | datasheet p.1 |
| Pump pressure | **250 bar rated, 300 bar peak** | datasheet p.1 |
| Pump speed | 2000 rated, 2800 max, 400 min rpm | datasheet p.1 |
| Clutch | Flowfit series 30300 **mechanical clutch, lever-operated** (OFF/ON, ±10° lever travel) | datasheet p.3 |
| Clutch rating | **Nominal torque 18.5 daNm = 185 Nm**, max 2700 rpm, max 40 kW, axial load 160 daN | datasheet p.3 |
| Clutch input | **Ø28 j6 shaft, 8×7×40 key** (UNI 6607-69) | datasheet p.3 |
| Clutch output | 35×31 DIN 5482 internal spline (group 3) | datasheet p.3 |
| Clutch lubrication | SAE 90 gear oil; change after the first 60–80 h, then every 12 months or 1500 h | *(page)* |
| Engagement | With the directional valve in the unloaded position, at no more than 1800 rpm | *(page)* |
| Rotation | Clockwise as supplied; anticlockwise on request. Reversible clutch variants exist (30300/30311/30312). | *(page)*, datasheet p.3 |

### Fit against the Vega requirements

| Check | Result |
|---|---|
| Flow at 800 rpm idle | 43 cm³ × 800 × 0.92 ≈ **31.6 L/min** against 33.8 for 100 %. At 250 bar the flow and pressure limits happen to coincide, giving about 88 % thrust, the same as a 46 cm³ pump. **But a 43 cm³ pump is flow-limited at idle, so raising the relief above 250 bar gains nothing** (see "Raising the relief above 250 bar" below). ✅ at 250 bar |
| Pump pressure | 250 bar rated. ✅ |
| Pump and clutch speed | 2500 rpm engine is under the 2800 (pump) and 2700 (clutch) limits. ✅ |
| PTO torque (420 Nm) | ✅ Large margin. |
| **Clutch torque at the 250 bar relief** | 250 bar × 43 cm³ / 2π = 171 Nm theoretical, **~190 Nm** with 90 % mechanical efficiency. That's **at or just over the 185 Nm nominal rating.** ⚠ |
| Clutch torque at 200 bar (Flowfit's assembly rating) | 137–152 Nm, about 80 % of nominal. This is probably why Flowfit rates the assembly at 200 bar. |
| Coupling | HRC 150 with a 48 mm hub on the PTO and a 28 mm hub on the clutch input. Torque ≤ 190 Nm. Check that both bores fit the chosen hub types. |
| Control | Manual lever on the unit, so engaging it means a trip to the engine room, or adding a push-pull cable or actuator. The clutch has no position feedback; a limit switch would be needed for any Signal K indication or rpm interlock. |

### Thrust vs relief setting with this assembly (warm oil, 800 rpm)

| Relief | Thrust | Torque at relief | vs clutch 185 Nm |
|---|---|---|---|
| 200 bar (Flowfit rating) | ~70 % | 137–152 Nm | ✅ within |
| 230 bar | ~81 % | 157–175 Nm | ✅ within (≈ 95 %) |
| 250 bar | ~88 % | 171–190 Nm | ⚠ at or just above |

### Ways forward

1. **Ask Flowfit** whether the 30300 clutch's 185 Nm *nominal* rating allows the short, intermittent
   peaks of thruster duty at 250 bar. That keeps the 88 % thrust and the low price.
2. **Set the relief to ~230 bar.** That stays within the clutch rating, gives ~81 % thrust, and needs
   no extra cost.
3. **Use a heavier clutch with the same pump.** Look for an electromagnetic or mechanical clutch rated
   at 250 Nm or more. Flowfit also lists an electromagnetic clutch and pump category. That would also
   allow remote engagement and an rpm interlock.
4. A smaller pump such as 39 cm³ would stay within 185 Nm at 250 bar (155–172 Nm). But at 800 rpm it
   gives only ~28.7 L/min, which makes thrust flow-limited, so it needs a ~900 rpm thruster idle. Not
   better than option 2.

## Borelli mechanical couplings (Salhydro catalogue HPFM.pdf)

Source: <https://files.salhydro.fi/files/PDF/HPFM.pdf>, the Borelli "Mechanical couplings" catalogue
(10 scanned pages, read visually). Salhydro is a Finnish distributor, so this would be sourced
locally.

**The Flowfit 30300 is a Borelli 30300.** The part numbers, drawings and ratings are identical: a
mechanical **dog clutch** ("coupling with front teeth"), lever-operated, 185 Nm nominal.
The catalogue also has a **larger series, 30500**, for pump groups 3.5 and 4:

| Item | 30300 (Flowfit assembly) | **30500** |
|---|---|---|
| Nominal torque | 18.5 daNm = **185 Nm** | 58 daNm = **580 Nm** |
| Max speed | 2700 rpm | 2700 rpm |
| Max power | 40 kW | 60 kW |
| Axial load | 160 daN | 260 daN |
| Input shaft | Ø28 j6, key 8×7×40 | **Ø42 j6, key 12×8×60**, 70 mm long |
| Output | 35×31 DIN 5482 internal spline | 48×44 DIN 5482 internal spline |
| Pump flanges | Gr.2–3, Gr.2/3 Bosch, SAE A, SAE B | Gr.2, **Gr.3 (30401)**, Gr.3.5, Gr.4, **Gr.3 Bosch (30417)**, SAE A/B/C, others |
| Size | ~151 mm long | ~226 mm long, Ø166 housing |
| Versions | 30300 reversible / 30301 right / 30302 left | 30500 reversible / 30501 right / 30502 left |

General rules for both series (catalogue p.3, verbatim): *"When coupling with hydraulic pumps we
recommend to engage and disengage the pump when the directional valve is in exhaust position at a
speed not over 1800 R.P.M. In the reversible position the max engagement and disengagement speed is
1000 R.P.M."* Lubrication: SAE 90, changed every 12 months. Working temperature −10 to +80 °C.

### Fit of the 30500 against Vega

| Check | Result |
|---|---|
| Torque, 43–46 cm³ at 250 bar (171–215 Nm) | ✅ 580 Nm nominal, about **2.7–3×** margin. Even 300 bar peaks (about 230–245 Nm) are well inside. |
| PTO limit (≈ 420 Nm) | The clutch is now stronger than the PTO. The **relief valve** is what protects the PTO. 250 bar × 46 cm³ ≈ 215 Nm, so that's fine. |
| Speed and power | ✅ 2700 rpm and 60 kW, against 2500 rpm and about 18 kW |
| Input shaft | ✅ Ø42 keyed. HRC 150 hubs would be 48 mm (PTO) and 42 mm (clutch). Check the hub types. |
| Pump mounting | Gr.3 (30401) and Gr.3 Bosch (30417) flanges are listed, so the existing pump types fit. ⚠ **But the output spline is 48×44, larger than a group-3 pump shaft.** Ask Salhydro or Borelli which spline adapter or sleeve goes with flange 30401 or 30417 for a group-3 pump (35×31 spline or 1:8 taper). |
| Engagement | Same rules as the 30300: unloaded, at no more than 1800 rpm (1000 rpm if reversible). Use a **right or left (non-reversible) version** to get the 1800 rpm limit. Engaging at idle with the 2/2 valve open meets either. |
| Remote operation | Same lever as the 30300; a push-pull cable or actuator plus a limit switch still apply. The lever force isn't stated clearly (the drawing shows 631 / 472 daN, which is probably not a hand force); ask. |
| Size | About 75 mm longer than the 30300. Check the space on the hull mount. |

**It solves the 250 bar torque question.** With the 30500, the relief can stay at 250 bar
(about 88 % thrust), with plenty of margin and no need to ask Flowfit about short peaks.

## Sensitivity to engine idle speed

The 800 rpm idle comes from the 2018 blog. Online sources suggest the 3126B marine low idle may be
about **650–700 rpm**, programmable in the ECM. See the
[vessel overview](../../vessel/README.md#engine-idle-speed). Thruster thrust at a 250 bar relief, warm
oil:

| Idle | 43 cm³ | 46 cm³ | 51 cm³ | 60 cm³ |
|---|---|---|---|---|
| 600 rpm | ~49 % | ~56 % | ~69 % | ~88 % |
| 650 rpm | ~58 % | ~66 % | ~81 % | ~88 % |
| 700 rpm | ~67 % | ~77 % | **~88 %** | ~88 % |
| 750 rpm | ~77 % | **~88 %** | ~88 % | ~88 % |
| 800 rpm | **~88 %** | ~88 % | ~88 % | ~88 % |

**If idle is about 700 rpm, the 43 cm³ pump gives only about two-thirds thrust.** A 51 cm³ pump
covers idle down to 700 rpm. At 250 bar it needs about 225 Nm, which rules out the 185 Nm
Borelli/Flowfit 30300 and points to the Borelli 30500. The VNK3 range has a 51 cm³ size (250 bar
rated, 2800 rpm max). Alternatives are to have the low idle raised in the ECM, or to raise rpm by
hand when thrusting. **⚠ Measure the real idle before buying the pump.**

## Raising the relief above 250 bar

The CETOP manifold relief valve is rated **up to 300 bar and 80 L/min** (owner, 2026-10-22), and the
hoses are 300 bar, so neither of those stops a higher setting. Thrust estimates at 800 rpm idle,
warm oil:

| Relief | 43 cm³ (31.6 L/min) | 46 cm³ (33.9 L/min) | 51 cm³ (37.5 L/min) | Torque, 46 cm³ |
|---|---|---|---|---|
| 250 bar | ~88 % | ~88 % | ~88 % | ~203 Nm |
| 260 bar | ~88 % (flow-limited) | ~92 % | ~92 % | ~211 Nm |
| 270 bar | ~88 % (flow-limited) | ~95 % | ~95 % | ~220 Nm |
| 280 bar | ~88 % (flow-limited) | ~99 % | ~99 % | ~228 Nm |

- **More pressure only helps with more flow at idle.** That means a 46–51 cm³ pump instead of 43,
  or about 900 rpm idle while thrusting.
- **Torque:** at most about 250 Nm (51 cm³, 280 bar). That's fine for the Borelli 30500 (580 Nm) and
  the PTO (420 Nm), but **not** for the 30300 (185 Nm) or the Brevini IM1 (190 Nm).
- **What still limits the pressure:**
  - **Pump:** the VNK3 group 3 (43 and 51 cm³) is rated 250 bar continuous and 300 bar peak.
    Running at 260–280 bar means relying on its peak rating during thruster bursts. Ask whether the
    peak rating covers intermittent duty, or choose a pump rated for 280 bar continuous.
  - **Valves:** the BAV-713 thruster valve and the CETOP subplate. CETOP 3 parts are often rated
    315–350 bar, but **⚠ verify**.
  - **Thruster motor:** the Side-Power SH240 hydraulic motor's maximum pressure. **⚠ verify.**
- **The 80 L/min rating is fine.** The relief sits after the VPR3 (35 L/min), so it never sees full
  pump flow.

## Brevini IM1 mechanical clutch (hydrauliikkakauppa.fi)

Source: <https://www.hydrauliikkakauppa.fi/wp-content/uploads/2020/09/Mekaaninen-Irrotuskytkin-40kW-IM1.pdf>,
the Brevini Fluid Power IM1 datasheet (2 pages, read visually). Finnish supplier.

| Item | Brevini IM1 | Compared with Borelli 30300 / 30500 |
|---|---|---|
| Type | Manual-lever mechanical clutch, motor/engine to pump | same idea |
| **Max torque** | **19 daNm = 190 Nm** (a *maximum*, not a nominal rating) | 30300: 185 Nm *nominal*; 30500: 580 Nm nominal |
| Max speed | 2700 rpm | same |
| **Max engagement speed** | **420 rpm** (300 rpm reversible), pump unloaded | 1800 rpm (1000 reversible) |
| Input shaft | Ø28 j6, key A8×7×40, 48 mm long; radial load chart up to about 3 kN | 30300 the same Ø28; 30500 Ø42 |
| Output | Z18 35×31 DIN 5482 spline, so a group-3 splined pump fits directly | |
| Flanges | Gr.2–3, SAE A, SAE B | |
| Lubrication | 0.5 L CLP 150 (ISO VG 150), changed every 12 months | SAE 90 |
| Ordering code | IM1-C-**D**/**S**/**R**-**2/3**/SA/SB (D = clockwise, S = anticlockwise, R = reversible) | |

### Fit against Vega

- **Engagement at 420 rpm or below means it can't be engaged with the engine running.** The 3126B
  idles at about 800 rpm. The pump would have to be engaged **with the engine stopped**, before
  starting, and disengaged after stopping. It couldn't be engaged on approach to a harbour or for
  the windlass at anchor without shutting the engine down. ❌ for a thruster that's needed on
  arrival.
- **190 Nm max** against 171–190 Nm at 250 bar is right at the limit, with no margin for pressure
  peaks. Similar to the 30300, but this one is a *maximum* rating, so it's actually tighter. ❌
- **Conclusion:** no better than the Flowfit/Borelli 30300, and worse to operate. Brevini may make
  larger sizes in the same catalogue section (the filename says "40kW", and the page is section
  2.03). Ask the supplier for a larger size, and check its engagement speed too.

## Electromagnetic clutch options (Flowfit range)

Source: the Flowfit technical PDF `ECPA1.pdf`, 12 pages, scanned and read visually. Flowfit sells
three series, all of the same design.

| Series (12 V / 24 V) | Nominal torque | Static (max) torque | Dynamic torque at 500 / 1000 rpm | 24 V coil | Pulley | Weight |
|---|---|---|---|---|---|---|
| 30901 / 30903 | 78 Nm | 125 Nm | 85 / 70 Nm | 1.26 A, 30 W | Ø153, 2 × A-section | 5.5 kg |
| 30929 / 30930 | 118 Nm | 140 Nm | 125 / 110 Nm | 1.26 A, 30 W | Ø153, 2 × A-section | 5.5 kg |
| **30990 / 30991** | **160 Nm** | **210 Nm** | **145 / 120 Nm** | 1.95 A, 47 W | Ø186, 2 × A-section | 8 kg |

Common to all three series:
- **Output** is a 35×31 DIN 5482 internal spline. Flanges are available for Group 2 Bosch,
  Group 3, Group 3 Bosch, SAE A and SAE B. The 24 V Group 3 version of the largest series is
  **29-30993**.
- **All data is at 20 °C.** At 120 °C performance is **20 % lower**.
- Engagement takes 25 ms, with at least 20 s between engagements. Slipping must not last more than
  5 s (product page).
- Max speed 5000 rpm. All are reversible.
- **Input is a V-belt pulley (the clutch rotor), not a shaft.** These are built for belt drive from
  the engine crank, like truck and tractor auxiliary pumps.

### Fit against Vega

| Check | Result |
|---|---|
| Torque with a 43 cm³ pump at 250 bar (171–190 Nm) | **Over the 160 Nm nominal rating** of the largest series. Under the 210 Nm static rating when cold, but at the limit of the 168 Nm hot rating (−20 %). **No better than the 185 Nm mechanical clutch.** ❌ |
| Torque at 200–230 bar (137–175 Nm) | Above nominal from about 220 bar upward. |
| Drive from the PTO's Ø48 keyed shaft | ❌ **No shaft input.** You'd need either (a) a belt drive from a pulley on the PTO, or (b) a custom adapter bolted to the pulley rotor, which isn't a supported configuration. A belt drive brings back the 2018 problem: two A-section belts can't carry about 17 kW at 800 rpm. |
| Remote engagement and interlock | ✅ This is the main advantage: 24 V at about 2 A, switched from the helm or an ESP32 PDM channel, with an easy rpm interlock. |

**Conclusion:** none of the Flowfit electromagnetic clutches suits this installation. They're
weaker than the mechanical 30300 and designed for belt drive.

### Electromagnetic alternatives worth investigating (outside the Flowfit range)

- **Industrial shaft-to-shaft electromagnetic clutch modules**, i.e. a bearing-mounted clutch with an
  input shaft and an output shaft or flange. Examples: Warner Electric, Ogura, Kendrion/INTORQ and
  Mayr. They come in 24 V DC sizes above 250 Nm. Check the actual ratings and prices in the
  datasheets; they're likely to cost more than the whole Flowfit assembly.
- **Hydraulically or pneumatically actuated multi-disc PTO clutches**, as used on marine and
  industrial power take-offs. These are robust and can be engaged remotely with a solenoid valve.
  They're usually the most expensive option.

### Keep the mechanical clutch but add remote control

The 30300 mechanical clutch has the best torque per pound of the options found. It can be operated
remotely with:
- a **push-pull cable** to a lever at the helm or the engine room door (cheap, like a throttle
  cable);
- a **24 V linear actuator** on the lever, plus a **limit switch** for "engaged" feedback. That
  gives an ESP32 PDM output, Signal K indication, and the rpm interlock (engage only below about
  1000 rpm, alarm if engaged above the limit).

## Comparison

| | A. Gear 46 cc | B. Gear 37 cc + rpm | C. Bent-axis fixed | D. Variable PC | E. Load-sensing | F. Tandem gear |
|---|---|---|---|---|---|---|
| Approx. pump cost | € | € | €€ | €€€ | €€€€ (with valves) | €–€€ |
| Circuit changes | none | rpm control | adapter flange; maybe relief/valve ratings | case drain; VPR3 optional | new valve bank | extra valves |
| Thrust at 250 bar class | ~88 % | ~88 % (if rpm raised) | ~88 %, **~100 % at 280 bar** | ~90 % | ~90 % | ~88 % |
| Efficiency while thrusting | ~80–85 % | ~80–85 % | ~90–95 % | ~88–92 % | best | ~80–85 % |
| Oil cleanliness needed | tolerant | tolerant | moderate | strict | strict | tolerant |
| Proportional control | no | no | no | no | **yes** | no |
| Fit with current brief | **good** | fair | **good** | weak | scope change | situational |

## Preliminary recommendation

**Clutch (updated 2026-10-22):** Borelli **30501 or 30502** (series 30500, non-reversible to suit
the PTO rotation) with a group-3 pump flange. It's rated 580 Nm, which allows a 250 bar relief with a
large margin. Fallback: the Flowfit/Borelli 30300 assembly with the relief at about 230 bar. Add a
push-pull cable or actuator with a limit switch for remote engagement.

**Pump:**

1. **Default: A**, a ~46 cm³ group-3 gear pump. It's the cheapest, it works with all the parts
   you already have, and the clutch removes the main inefficiency.
2. **Worth a quote: C**, a ~45–47 cm³ bent-axis truck pump, ideally second-hand. If it costs not
   much more than A, it brings lower losses, quieter running, and the option to reach full thrust
   later by raising the relief (after checking the valve and motor ratings).
3. **Revisit E** only if proportional thruster or windlass control, or several simultaneous loads,
   become requirements.

## Open questions

- [ ] Windlass motor specs and expected run time. Long runs change the heat picture.
- [ ] Side-Power SH240 hydraulic motor maximum pressure (for option C at 265–280 bar)
- [ ] CETOP 3 subplate, valve and BAV-713 pressure ratings
- [ ] Does the CAT 3126B electronic control accept an external rpm-raise input? (option B)
- [ ] Shaft and flange of the chosen pump vs the clutch output (keyed / spline, SAE A/B or ISO 7653)
