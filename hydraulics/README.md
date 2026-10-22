# Hydrauliikka

Ohjaus, keulapotkuri, ankkurivinssi ja tulevat hydrauliset kuormat.

| Tiedosto | Sisältö |
|---|---|
| [current-system.md](current-system.md) | Lähtötilanne, nykyinen remonttitilanne (§0), vaikutukset suunnitteluun, avoimet kysymykset |
| [requirements.md](requirements.md) | Vaatimuspohja, osittain täytetty |
| [loads.yaml](loads.yaml) | Kuormarekisteri: kunkin hydraulisen kuorman luvut (koneluettava) |
| [design/p2-pump-options.md](design/p2-pump-options.md) | Apupiirin pumpun ja PTO-kytkimen vaihtoehdot sekä arvioidut tuote-ehdokkaat |
| [img/](img/) | Kaaviot ja kuvat |

## Tilanne lyhyesti

Kaikki hydrauliikka on purettuna, kun konetta linjataan uuteen Advance 300 -vaihteistoon.
Suunnitelmassa on kaksi piiriä:

- **Ohjaus:** 16,6 cm³:n hammaspyöräpumppu koneen etupäästä hihnavedolla, syöttää orbitrolia ja
  ohjaussylinteriä.
- **Apupiiri:** uusi ryhmän 3 hammaspyöräpumppu vaihteiston PTO:lta HRC-joustokytkimen ja
  mekaanisen kytkimen kautta, syöttää keulapotkuria (myöhemmin myös ankkurivinssiä) CETOP 3
  -pohjalaatan kautta. Paineenrajoitus 250 bar, noin 90 %:n työntövoima hyväksytty.

Koneen noin 700 rpm:n tyhjäkäynnillä apupiiriin tarvitaan noin 51 cm³:n pumppu ja sen momentin
(~225 Nm) kestävä kytkin; suositus on Borelli 30500 -sarja.
