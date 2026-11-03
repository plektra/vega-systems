# Arkisto: öljyn lämpökuorma F1-61-kokoonpanolla

> **🗄 Arkistoitu 2026-11-03.** Siirretty tiedostosta [oil-cooling.md](../oil-cooling.md), kun P2:ksi
> valittiin Vickers PVH57 (2026-10-27) ja venttiileiksi Danfoss PVG 32. Laskelmat koskevat
> kiinteää Parker F1-61 -pumppua, VPR3:a, BPV-ohitusventtiiliä ja PTO-kytkintä. Teksti on
> sellaisenaan, eikä sitä päivitetä.

## Lämpökuormat ja lämpeneminen

Oletukset: Parker F1-061 (laskettu 61 cm³:llä; todellinen 59,5 cm³ antaa noin 2,5 % pienemmät lämmöt) PTO:lla 1:1, paineenrajoitus 250 bar, 80 l öljyä, säiliön ja
letkujen teräs mukana lämpökapasiteetissa, ei jäähdytintä. Ks. myös
[p2-pump-options.md](p2-pump-options.md#käyttäytyminen-eri-kierroksilla-parker-f1-061).

**Keulapotkuri käytössä:**

| Koneen kierrokset | Lämpö | 40 → 60 °C | 40 → 75 °C (Parker F1:n raja) |
|---|---|---|---|
| 700 rpm | ~8 kW | ~5,5 min | ~10 min |
| 1000 rpm | ~16 kW | ~3 min | ~5 min |
| 1800 rpm | ~38 kW | ~1 min | ~2 min |

Tavallinen 1–2 minuutin manööveri tyhjäkäynnillä nostaa öljyä noin 4–7 °C.

**Jatkuvat kuormat.** Säiliö ja letkut luovuttavat konehuoneeseen arviolta noin 20–25 W/°C
(säiliön pinta noin 1,7 m², letkut noin 0,5 m², luonnollinen konvektio). Tasapainolämpötilat 35 °C:n
konehuoneessa:

| Jatkuva kuorma | Öljyn tasapainolämpötila |
|---|---|
| Ohjauspumppu matka-ajossa (~0,5 kW) | noin 55–60 °C (40–45 °C:n konehuoneessa 65–70 °C) |
| Kytkin päällä tyhjäkäynnillä, keulapotkuri ei käytössä (~0,7 kW) | noin 65 °C |
| Kytkin päällä 1800 rpm:llä, vapaakierto auki (~2 kW) | **yli 100 °C** |
| ~~Alustava ratkaisu (2026-10-23): ajossa BPV:n ohitus~~ → PVH57 valmiustilassa (2026-10-27) | **⚠ ei tiedossa** (Parker ei ilmoita ohitustilan lämpöä); mitataan ensimmäisellä kaudella |

Viimeisessä tapauksessa lämpeneminen on hidasta: 40 → 75 °C noin 1 tunnissa (kuorman mukaan
45–90 min), 20 → 75 °C noin 1,5 tunnissa. Kytkimen unohtuminen päälle koko matkan ajaksi
ylikuumentaa öljyn, mutta lyhyt hetki ei.

Parker F1:n **BPV-ohitusventtiili** pienentäisi viimeisen tapauksen lämpökuormaa ja läpivirtausta
huomattavasti, koska öljy kiertää silloin pumpun päätykappaleessa eikä koko piirin kautta (tarkka
luku **⚠ ei tiedossa**), ks.
[p2-pump-options.md](p2-pump-options.md#lisävaruste-parker-bpv-f1--ohitusventtiili).


## Paluiden yhdistäminen: alkuperäinen taulukko

| Paluu | F1-61-reitti | PVH57-reitti (LS + on/off) |
|---|---|---|
| CETOP-pohjalaatan T (BAV-713, VMP) | kyllä | kyllä |
| VPR3:n B (ylimäärä) | kyllä | ei (VPR3 poistuu) |
| OD15 / 2/2-vapaakiertoventtiili | kyllä | ei |
| P1: RPF3:n ylimäärä ja orbitrolin T | kyllä | kyllä |
| **Ei paluulinjaan:** U11:n vuotolinja, PVH57:n kotelovuoto, BPV:n vuotolinja | suoraan säiliöön öljypinnan alle | sama |


## Kierroslukitus: alkuperäinen muotoilu

- **Kierroslukitus** (päivitetty 2026-10-23: PTO-kytkimen sijaan BPV-ohitusventtiili, ks. [requirements.md §10.2](../../requirements.md)). Alkuperäinen muotoilu: kytkin päälle vain alle noin
  1000 rpm:ssä; sen yli keulapotkurin venttiili estetään ja vapaakiertoventtiili avataan; hälytys,
  jos kytkin on päällä yli noin 1200 rpm:ssä.

