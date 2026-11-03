# Hydrauliikka

Ohjaus, keulapotkuri, ankkurivinssi ja tulevat hydrauliset kuormat.

| Tiedosto | Sisältö |
|---|---|
| [schematic.md](schematic.md) | **Kaaviot**: ISO 1219 -arkit 1–3 (ohjaus, apupiiri PVH57 + PVG 32, paluu ja jäähdytys; luonnos) osaluetteloineen sekä lohkokaaviot |
| [procurement.md](procurement.md) | **Hankintalista**: kaikki tarvittavat osat, tila (olemassa, hankitaan, ehdollinen) ja tunnetut hinnat |
| [current-system.md](current-system.md) | Lähtötilanne, nykyinen remonttitilanne (§0), vaikutukset suunnitteluun, avoimet kysymykset |
| [requirements.md](requirements.md) | Vaatimuspohja, osittain täytetty |
| [loads.yaml](loads.yaml) | Kuormarekisteri: kunkin hydraulisen kuorman luvut (koneluettava) |
| [design/p2-variable-pump.md](design/p2-variable-pump.md) | **P2 = Vickers PVH57** (päätetty 2026-10-27, ostettu 2026-11-01): pumpun tiedot ja kunto, LS-kytkentä PVG 32:een, HRC 150 -kytkin, kannake, asennus, käyttöönoton säädöt, vikatilat ja paluusuodatin |
| [design/aux-circuit-ls-clean-sheet.md](design/aux-circuit-ls-clean-sheet.md) | **Apupiirin venttiilit: Danfoss PVG 32** (päätetty 2026-10-27, ostettu 2026-11-02): lohkot ja kuormat, rungon koodit, keulapotkurin ja vinssin vaatimukset, puhdistus ja koestus |
| [design/bow-thruster-control.md](design/bow-thruster-control.md) | Keulapotkurin portaaton ohjaus: PVEH:n ohjaussignaali, potentiometrijoystick, ESP32-PDM valvojana, sallintaketju ja vikatilat (suositus, ei päätetty) |
| [design/pvg32-lever.md](design/pvg32-lever.md) | PVG 32:n käsivipu (PVM): valmisosat, kiinnitys (todennäköisesti M8) ja oman tai 3D-tulostetun vivun suunnittelu |
| [design/p1-steering-pump.md](design/p1-steering-pump.md) | Ohjauspumpun imulinja (päätetty 32 mm) ja P1:n muutokset P2-remontin yhteydessä |
| [design/hydraulic-oil.md](design/hydraulic-oil.md) | Hydrauliöljyn valinta: komponenttien rajat, HV 32 / VG 46 / HV 46 -vertailu, tuotteet (päätetty HVLP 32) |
| [design/pressure-monitoring.md](design/pressure-monitoring.md) | Painemittaus: nykyiset mittarit ja ehdotus digitaalisista antureista (Signal K / NMEA 2000) ja mittausliittimistä |
| [design/oil-cooling.md](design/oil-cooling.md) | Öljyn lämpökuorma (PVH57 + PVG 32) ja jäähdytys Bowman EC100:lla (päättämättä) |
| [img/](img/) | Kaaviot ja kuvat |

### Arkisto

Vanhentuneet selvitykset säilytetään taustaksi kansiossa [design/archive/](design/archive/)
(kuvat kansiossa `img/archive/`). Niitä ei päivitetä.

| Tiedosto | Sisältö |
|---|---|
| [p2-pump-options.md](design/archive/p2-pump-options.md) | 🗄 2026-10-27. Parker F1-61 -vaihtoehto (BPV, Spidex) ja pumppuvertailu; imu- ja kierroslukulaskelmat yhä viitekäytössä |
| [schematic-sheet-2-f1-61.md](design/archive/schematic-sheet-2-f1-61.md) | 🗄 2026-10-27. Kaavion arkki 2 F1-61 + BPV -kokoonpanolle |
| [p2-fxdc-ls-unloading.md](design/archive/p2-fxdc-ls-unloading.md) | 🗄 2026-11-03. PVH57 vanhoilla venttiileillä: FXDC + LS-purku, VPR3:n sopimattomuus, F1-61-vertailu (varavaihtoehto) |
| [aux-circuit-ls-onoff.md](design/archive/aux-circuit-ls-onoff.md) | 🗄 2026-11-03. Apupiiri LS:llä ja on/off-venttiileillä ilman venttiilipöytää (varavaihtoehto) |
| [aux-circuit-pvg32-pre-purchase.md](design/archive/aux-circuit-pvg32-pre-purchase.md) | 🗄 2026-11-03. PVG 32 -ajatuskoe ennen ostoa: vertailu, suositus ja hinta-arvio |
| [oil-cooling-f1-61.md](design/archive/oil-cooling-f1-61.md) | 🗄 2026-11-03. Öljyn lämpökuorma F1-61:llä, VPR3:lla ja BPV:llä |
| [current-system-2026-10.md](design/archive/current-system-2026-10.md) | 🗄 2026-11-03. Nykytilan vanhentuneet kohdat: 32 mm:n P2-imu, F1-61-päivitykset, BAV-713- ja CETOP-kysymykset, päivityshistoria |

## Tilanne lyhyesti (2026-11-03)

Hydraulipumput on irrotettu, kun konetta linjataan uuteen Advance 300 -vaihteistoon; muu
järjestelmä (säiliö, venttiilit, orbitroli, sylinteri, letkut) on paikallaan.
Suunnitelmassa on kaksi piiriä:

- **Ohjaus:** 16,6 cm³:n hammaspyöräpumppu P1 koneen etupäästä hihnavedolla, syöttää orbitrolia ja
  ohjaussylinteriä; imulinja 32 mm.
- **Apupiiri:** Vickers PVH57 -säätötilavuuspumppu (57,4 cm³, LS-säädin; **ostettu 2026-11-01**)
  vaihteiston PTO:lta HRC 150 -joustokytkimellä, ilman PTO-kytkintä; 50 mm:n imulinja ja
  kotelovuotolinja säiliöön. Venttiileinä **Danfoss PVG 32** (5 lohkoa, 1 × PVEH ja 4 × PVEO;
  **ostettu 2026-11-02**, karat käsin kunnossa 2026-11-03). Ajon aikana pumppu on valmiustilassa
  noin 20 barissa. Syöttää keulapotkuria (portaaton PVEH-lohko) ja myöhemmin ankkurivinssiä ja
  painepesuria. Paineenrajoitus 250 bar, noin 90 %:n työntövoima hyväksytty.

**Seuraavaksi:** pumppukannakkeen suunnittelu ja pumpun mittaus, PVG 32:n puhdistus ja koestus,
keulapotkurin isku-/imuventtiilit ja vinssin paineraja (PVG 32:n lohkoissa ei paikkoja),
paluusuodattimen vaihto lasikuituun, öljynjäähdyttimen asennus. Päätökset:
[decisions.md](../decisions.md).
