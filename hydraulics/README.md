# Hydrauliikka

Ohjaus, keulapotkuri, ankkurivinssi ja tulevat hydrauliset kuormat.

| Tiedosto | Sisältö |
|---|---|
| [schematic.md](schematic.md) | **Kaavio** suunnitellusta järjestelmästä (ohjaus, apupiiri, paluu ja jäähdytys) |
| [current-system.md](current-system.md) | Lähtötilanne, nykyinen remonttitilanne (§0), vaikutukset suunnitteluun, avoimet kysymykset |
| [requirements.md](requirements.md) | Vaatimuspohja, osittain täytetty |
| [loads.yaml](loads.yaml) | Kuormarekisteri: kunkin hydraulisen kuorman luvut (koneluettava) |
| [design/p2-pump-options.md](design/p2-pump-options.md) | Apupiirin pumppu ja veto: päätetty kokoonpano (F1-61, BPV, Spidex) ja taustavertailu |
| [design/p1-steering-pump.md](design/p1-steering-pump.md) | Ohjauspumpun imulinja (25 mm, 3,2 m) ja ehdotetut P1:n muutokset P2-remontin yhteydessä |
| [design/oil-cooling.md](design/oil-cooling.md) | Öljyn lämpökuorma ja jäähdytys (Bowman EC100) |
| [img/](img/) | Kaaviot ja kuvat |

## Tilanne lyhyesti

Kaikki hydrauliikka on purettuna, kun konetta linjataan uuteen Advance 300 -vaihteistoon.
Suunnitelmassa on kaksi piiriä:

- **Ohjaus:** 16,6 cm³:n hammaspyöräpumppu koneen etupäästä hihnavedolla, syöttää orbitrolia ja
  ohjaussylinteriä.
- **Apupiiri:** Parker F1-61 -mäntäpumppu (59,5 cm³) vaihteiston PTO:lta Spidex-kynsikytkimellä,
  ilman PTO-kytkintä; ajon aikana pumppu kiertää tyhjänä BPV-ohitusventtiilin kautta. Syöttää keulapotkuria (myöhemmin myös ankkurivinssiä) CETOP 3
  -pohjalaatan kautta. Paineenrajoitus 250 bar, noin 90 %:n työntövoima hyväksytty.

Päätös 2026-10-23: F1-61 + BPV-F1 käsiohituksella, Spidex 48/60 -kytkin, 50 mm:n imulinja ja
BPV:n vuotolinja säiliöön, ks. [design/p2-pump-options.md](design/p2-pump-options.md#päätetty-kokoonpano-2026-10-23).
Hankinta myöhemmin.
