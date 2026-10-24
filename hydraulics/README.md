# Hydrauliikka

Ohjaus, keulapotkuri, ankkurivinssi ja tulevat hydrauliset kuormat.

| Tiedosto | Sisältö |
|---|---|
| [schematic.md](schematic.md) | **Kaaviot**: ISO 1219 -arkit 1–3 (ohjaus, apupiiri, paluu ja jäähdytys; luonnos) osaluetteloineen sekä lohkokaaviot |
| [current-system.md](current-system.md) | Lähtötilanne, nykyinen remonttitilanne (§0), vaikutukset suunnitteluun, avoimet kysymykset |
| [requirements.md](requirements.md) | Vaatimuspohja, osittain täytetty |
| [loads.yaml](loads.yaml) | Kuormarekisteri: kunkin hydraulisen kuorman luvut (koneluettava) |
| [design/p2-pump-options.md](design/p2-pump-options.md) | Apupiirin pumppu ja veto: päätetty kokoonpano (F1-61, BPV, Spidex), taustavertailu ja muut Parkerin pumput (F1-51 vaihtoehtona) |
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
- **Apupiiri:** Parker F1-61 -mäntäpumppu (59,5 cm³) vaihteiston PTO:lta Spidex-kynsikytkimellä,
  ilman PTO-kytkintä; ajon aikana pumppu kiertää tyhjänä BPV-ohitusventtiilin kautta. Syöttää keulapotkuria (myöhemmin myös ankkurivinssiä) CETOP 3
  -pohjalaatan kautta. Paineenrajoitus 250 bar, noin 90 %:n työntövoima hyväksytty.

Päätös 2026-10-23: F1-61 + BPV-F1 käsiohituksella, Spidex 48/60 -kytkin, 50 mm:n imulinja ja
BPV:n vuotolinja säiliöön, ks. [design/p2-pump-options.md](design/p2-pump-options.md#päätetty-kokoonpano-2026-10-23).
Hankinta myöhemmin. **2026-10-24:** Torin F1-61:n kauppa peruuntui; myös vastaavat Sunfab-, OMFB/Hyva- ja
Rexroth-pumput omalla ohitusventtiilillään käyvät, ks. [vaihtoehdot](design/p2-pump-options.md#vaihtoehtoiset-pumput-muilta-valmistajilta-selvitys-2026-10-24).
