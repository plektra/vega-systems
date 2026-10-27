# Hydrauliikka

Ohjaus, keulapotkuri, ankkurivinssi ja tulevat hydrauliset kuormat.

| Tiedosto | Sisältö |
|---|---|
| [schematic.md](schematic.md) | **Kaaviot**: ISO 1219 -arkit 1–3 (ohjaus, apupiiri PVH57 + PVG 32, paluu ja jäähdytys; luonnos) osaluetteloineen sekä lohkokaaviot |
| [current-system.md](current-system.md) | Lähtötilanne, nykyinen remonttitilanne (§0), vaikutukset suunnitteluun, avoimet kysymykset |
| [requirements.md](requirements.md) | Vaatimuspohja, osittain täytetty |
| [loads.yaml](loads.yaml) | Kuormarekisteri: kunkin hydraulisen kuorman luvut (koneluettava) |
| [design/archive/p2-pump-options.md](design/archive/p2-pump-options.md) | 🗄 **Arkistoitu 2026-10-27.** Parker F1-61 -vaihtoehto (BPV, Spidex) ja pumppuvertailu; taustaksi (imu- ja kierroslukulaskelmat yhä viitekäytössä) |
| [design/archive/schematic-sheet-2-f1-61.md](design/archive/schematic-sheet-2-f1-61.md) | 🗄 **Arkistoitu 2026-10-27.** Kaavion arkki 2 F1-61 + BPV -kokoonpanolle (kuvat kansiossa `img/archive/`) |
| [design/p2-variable-pump.md](design/p2-variable-pump.md) | P2 säätötilavuuspumppuna: Vickers PVH57 (tori.fi), LS-ohjaus, kaksitiekompensoitu virtauksensäätö, osalista; **pumppu päätetty 2026-10-27** (FXDC-kytkentä varavaihtoehto) |
| [design/aux-circuit-ls-clean-sheet.md](design/aux-circuit-ls-clean-sheet.md) | **Ykkösvaihtoehto (päätös 2026-10-27):** apupiiri PVH57:llä ja Danfoss PVG 32 -proportionaaliventtiilipöydällä; ehdokasventtiilin tiedot, puhdistus ja koestus |
| [design/aux-circuit-ls-onoff.md](design/aux-circuit-ls-onoff.md) | Ajatuskoe: apupiiri alusta alkaen PVH57:llä, LS-signaalilla kuormilta ja on/off-venttiileillä (ilman venttiilipöytää); varavaihtoehto |
| [design/p1-steering-pump.md](design/p1-steering-pump.md) | Ohjauspumpun imulinja (päätetty 32 mm) ja P1:n muutokset P2-remontin yhteydessä |
| [design/hydraulic-oil.md](design/hydraulic-oil.md) | Hydrauliöljyn valinta: komponenttien rajat, HV 32 / VG 46 / HV 46 -vertailu, tuotteet (päätetty HVLP 32) |
| [design/pressure-monitoring.md](design/pressure-monitoring.md) | Painemittaus: nykyiset mittarit ja ehdotus digitaalisista antureista (Signal K / NMEA 2000) ja mittausliittimistä |
| [design/oil-cooling.md](design/oil-cooling.md) | Öljyn lämpökuorma ja jäähdytys (Bowman EC100 tai EC80; päättämättä) |
| [img/](img/) | Kaaviot ja kuvat |

## Tilanne lyhyesti

Hydraulipumput on irrotettu, kun konetta linjataan uuteen Advance 300 -vaihteistoon; muu
järjestelmä (säiliö, venttiilit, orbitroli, sylinteri, letkut) on paikallaan.
Suunnitelmassa on kaksi piiriä:

- **Ohjaus:** 16,6 cm³:n hammaspyöräpumppu koneen etupäästä hihnavedolla, syöttää orbitrolia ja
  ohjaussylinteriä.
- **Apupiiri:** Vickers PVH57 -säätötilavuuspumppu (57,4 cm³, LS-säädin) vaihteiston PTO:lta
  HRC 150 -joustokytkimellä, ilman PTO-kytkintä; ajon aikana pumppu on valmiustilassa noin 20 barissa.
  Syöttää keulapotkuria (myöhemmin myös ankkurivinssiä). Paineenrajoitus 250 bar, noin 90 %:n
  työntövoima hyväksytty.

**Päätös 2026-10-27:** P2 on PVH57 (kaupat sovittu), kytkin HRC 150, 50 mm:n imulinja ja
kotelovuotolinja säiliöön, ks. [design/p2-variable-pump.md](design/p2-variable-pump.md). Apupiirin
venttiileiksi **Danfoss PVG 32** (ykkösvaihtoehto, päätös 2026-10-27, kaupat toteutumassa), ks.
[design/aux-circuit-ls-clean-sheet.md](design/aux-circuit-ls-clean-sheet.md); varalla
[LS + on/off](design/aux-circuit-ls-onoff.md) ja FXDC + LS-purku. Aiempi alustava suunnitelma (Parker F1-61 + BPV) on
[arkistoitu](design/archive/p2-pump-options.md).
