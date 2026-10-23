# Ohjauspumppu P1: imulinja ja muutokset P2-remontin yhteydessä

> **Tila:** selvitys 2026-10-23. **Päätetty 2026-10-23: kohdat 1, 3, 4 ja 5** (32 mm:n imulinja,
> täysiaukkoinen palloventtiili, HVLP 32 -öljy, imupaineen mittaus käyttöönotossa); kohta 6: välitystä ei muuteta; kohta 7 avoinna. Imulinjan mitat [omistaja 2026-10-23],
> laskelmat [laskelma]. Ohjaus on turvallisuuskriittinen: **pätevän henkilön pitää tarkistaa
> ohjauspiirin muutokset ennen rakentamista.**

Liittyy: [current-system §3.3](../current-system.md#33-piiri-1--ohjaus),
[P2:n selvitys](p2-pump-options.md), [öljynjäähdytys](oil-cooling.md).

## Lähtötiedot

| Kohde | Arvo | Lähde |
|---|---|---|
| Pumppu | Salami 2PE16D-P28P1, 16,6 cm³, max 3000 rpm | [datalehti Salami 2PE] |
| Veto | 2 kiilahihnaa, kone:pumppu 1:1,24 | [blogi 2017-07-04] |
| Koneen kierrosalue | 700 (tyhjäkäynti, ei mitattu) – 2400 rpm | [omistaja 2026-10-22] |
| Pienin sallittu imupaine | **0,7 bar abs ≈ −0,3 bar ylipainetta** | [datalehti Salami 2PE] |
| Pienin viskositeetti | 12 cSt | [datalehti Salami 2PE] |
| Nykyinen imulinja | **25 mm:n sisähalkaisija, 320 cm** | [omistaja 2026-10-23] |
| Mahdollinen pidempi linja | enintään 5 m | [omistaja 2026-10-23] |
| Säiliön öljypinta suhteessa P1:een | **⚠ ei tiedossa**; laskelmassa oletettu noin 1 m yläpuolella (kuten P2) | oletus |
| P1:n imuaukon koko | **3/4"** (≈ 19 mm) | [omistaja 2026-10-23] |

**Koko pumpun tuotto kulkee imuletkun läpi:** RPF3 palauttaa ylimäärän säiliöön, joten imuvirtaus
kasvaa suoraan kierrosten mukana.

| Koneen rpm | P1 rpm | Imuvirtaus | Nopeus 25 mm:n letkussa | Nopeus 32 mm:n letkussa |
|---|---|---|---|---|
| 700 | 870 | 14,4 l/min | 0,49 m/s | 0,30 m/s |
| 1000 | 1240 | 20,6 l/min | 0,70 m/s | 0,43 m/s |
| 1800 | 2230 | 37,1 l/min | 1,26 m/s | 0,77 m/s |
| 2400 | 2980 | 49,4 l/min | **1,68 m/s** | 1,02 m/s |

Imulinjan tavallinen suositus on enintään noin 1 m/s (Parkerin raja F1:lle on sama).

## Imupaine P1:n imuaukolla

Laskelma 2026-10-23 [laskelma]: samat oletukset kuin [P2:n imulaskelmassa](p2-pump-options.md#imupuoli-letkun-koko-ja-pituus-sekä-öljylaatu):
laminaarivirtaus, liitinhäviöt K ≈ 2,5, tiheys 870 kg/m³, säiliön öljypinta 1 m pumpun yläpuolella
(+0,085 bar). Imuvirtaus teoreettinen (100 %). Pumpun sisäiset häviöt eivät ole mukana.
**Mukana 3/4":n imuaukon liitin** [omistaja 2026-10-23]: oletettu 0,1 m Ø19 mm ja supistus
K ≈ 1 (arvio). Virtausnopeus aukossa on 2400 rpm:llä noin 2,9 m/s. Suluissa arvo ilman liitintä.
Bar ylipainetta; **Salamin raja −0,3 bar**, lihavoidut alittavat sen.

| Imulinja ja öljy | 700 rpm, 5 °C | 1000 rpm, 5 °C | 1800 rpm, 5 °C | 2400 rpm, 5 °C | 2400 rpm, 20 °C | 2400 rpm, 40 °C |
|---|---|---|---|---|---|---|
| 25 mm, 3,2 m (nykyinen letku), VG 46 | −0,21 | **−0,34** | **−0,70** | **−0,98** (−0,86) | **−0,33** | −0,10 |
| 25 mm, 3,2 m, HV 32 | −0,05 | −0,11 | −0,29 (−0,24) | **−0,43** (−0,35) | −0,18 | −0,07 |
| 25 mm, 5 m, VG 46 | **−0,36** | **−0,56** | **−1,09** | **−1,49** | **−0,51** | −0,16 |
| 25 mm, 5 m, HV 32 | −0,12 | −0,21 | **−0,46** | **−0,66** | −0,28 | −0,11 |
| 32 mm, 3,2 m, VG 46 | −0,04 | −0,10 | −0,26 | **−0,39** | −0,11 | −0,01 |
| **32 mm, 3,2 m, HV 32** | +0,03 | 0,00 | −0,08 | −0,15 (−0,08) | −0,05 | 0,00 |
| 32 mm, 5 m, VG 46 | −0,10 | −0,18 | **−0,40** | **−0,58** | −0,18 | −0,04 |
| **32 mm, 5 m, HV 32** | 0,00 | −0,04 | −0,15 | −0,24 (−0,16) | −0,08 | −0,01 |

**Jos säiliön öljypinta on samalla korkeudella kuin P1**, kaikki arvot ovat noin 0,08 bar
huonompia. Silloin 25 mm × 3,2 m alittaa rajan kylmällä HV 32:lla jo noin 1800 rpm:llä (−0,37),
ja 32 mm × 5 m HV 32:lla on 2400 rpm:llä ja 5 °C:ssa juuri rajalla (−0,32). 32 mm × 3,2 m pysyy
silloinkin rajan sisällä (−0,24).

**Hihnavälityksen pienentäminen 1:1,15:een** (avoin kysymys kierrosrajan vuoksi) parantaa imua
vain vähän: 25 mm × 3,2 m, HV 32, 2400 rpm, 5 °C: noin 0,03–0,04 bar. Se ei korvaa isompaa letkua.

### Johtopäätökset

- **25 mm × 3,2 m riittää lämpimällä öljyllä** kaikilla kierroksilla ja HV 32 -öljyllä kylmänä
  noin 1800 rpm:iin asti, rajan tuntumassa (−0,29). Kylmällä öljyllä täysillä kierroksilla pumppu
  kavitoi (ulina, kuluminen). VG 46 -öljyllä raja tulee kylmänä vastaan jo noin 1000 rpm:llä.
- **25 mm × 5 m ei riitä:** kylmällä öljyllä kavitaatio alkaa tavallisilla ajokierroksilla.
- **32 mm riittää 5 metriin asti HV 32 -öljyllä**, kun säiliö on noin 1 m pumpun yläpuolella. Jos
  säiliö on pumpun tasolla, pidä linja lyhyenä (≈ 3 m).
- **3/4":n imuaukko on linjan kapein kohta.** Siihen ei voi vaikuttaa, mutta sen häviö pysyy
  pienenä, kun supistus tehdään suoraan pumpun aukolla: suora 3/4" BSP -nippa ja letkun supistus
  aukon kohdalla. **Ei 3/4":n letkua, kulmaliitintä tai pitkää putkea imuaukon jälkeen.**
- Virtausnopeuden suositus (≤ 1 m/s) täyttyy 32 mm:n letkulla koko kierrosalueella, 25 mm:n letkulla
  vain noin 1400 koneen rpm:ään asti.

## Ehdotus: P1:n muutokset P2-remontin yhteydessä

P2:n muutoksissa säiliöön tehdään joka tapauksessa uusi 50 mm:n imu-ulosotto, öljy vaihdetaan ja
paluulinjat kootaan uudelleen jäähdyttimen kautta. Samalla kannattaa tehdä nämä P1:n muutokset,
koska säiliö on silloin tyhjä ja auki.

| # | Muutos | Miksi | Kustannus |
|---|---|---|---|
| 1 | **P1:n imulinjaksi 32 mm (1-1/4"). Käytetään P2:n nykyinen 32 mm:n imuletku (noin 3 m) ja sen säiliöulosotto, kun P2 siirtyy 50 mm:n linjaan.** | Kylmäkäynnistyksen kavitaatioriski poistuu, ja linja saa pidentyä 5 metriin. Osat ovat jo olemassa. **⚠ Edellyttää**, että P2:n 50 mm:n ulosotto tehdään uuteen kohtaan eikä vanhaa suurentamalla; muuten P1 tarvitsee oman 32 mm:n ulosoton. | Pieni: suora 32 mm → 3/4" BSP -liitin suoraan P1:n imuaukkoon |
| 2 | Jos 32 mm ei sovi, **pidä nykyinen 25 mm:n linja enintään 3,2 m:n pituisena** ja käytä HV 32 -öljyä. Älä kierrä konetta yli noin 1800 rpm:n, ennen kuin öljy on lämmennyt (noin 20 °C). | Riittää ilman uusia osia, mutta jättää kylmäkäytölle rajoituksen | Ei mitään |
| 3 | **Täysiaukkoinen palloventtiili** P1:n imu-ulosottoon, ja ulosotto vähintään 50 mm minimiöljypinnan alle eikä paluiden lähelle | Kuristava venttiili tai ilmaa imevä ulosotto syö koko marginaalin | Pieni |
| 4 | **HV 32 -öljy** koko järjestelmään (jo suositeltu P2:n takia) | Suurin yksittäinen parannus P1:n imuun kylmänä. Huom. HV 32 ohenee noin 70 °C:ssa alle P1:n 12 cSt:n minimin, joten lämpötilahälytys 70 °C pysyy ([vaatimukset](../requirements.md)). | Öljy vaihdetaan joka tapauksessa |
| 5 | **Imupaineen tarkistus käyttöönotossa:** alipainemittari (−1…0 bar) P1:n imuaukolle, ja koeajo kylmänä 700 ja 1800 rpm:llä | Laskelma perustuu oletettuun säiliön korkeuteen ja liitinhäviöihin. Mittaus kertoo todellisen marginaalin. | Mittari ~20–40 € (arvio) |
| 6 | **Hihnavälitys:** ~~pienennetäänkö 1:1,15:een~~ **ei muuteta** (päätös 2026-10-23) | P1 pyörii nyt 2400 rpm:llä noin 2980 rpm (raja 3000). Imun kannalta muutos on pieni. | Hihnapyörä |
| 7 | **Hihnaveto ja kannake:** vanha kannake kantoi kahta pumppua peräkkäin. Kun vanha P2 poistuu hihnoilta, tarkistetaan kannakkeen ja tukilaakerin kiinnitys ja hihnojen kireys yhdelle pumpulle. | Ohjauksen ainoa pumppu, hihnan katkeaminen = ohjaus vain hätäjärjestelmillä | Työtä |

**Päätetty 2026-10-23: 1 + 3 + 4 + 5** ([päätösloki](../../decisions.md)).
Alkuperäinen suositus: Kohta 1 maksaa lähes vain liittimet, koska letku ja säiliön ulosotto
vapautuvat P2:lta. Ennen sitä pitää mitata säiliön öljypinnan korkeus suhteessa P1:een.

### Vikatilanteet (ohjaus)

| Vika | Seuraus | Suoja |
|---|---|---|
| Imulinjan kavitaatio (kylmä öljy, liian pieni tai pitkä letku, kiinni jäänyt palloventtiili) | Ohjaus raskas tai nykivä, pumppu kuluu, pahimmillaan pumppu rikkoutuu | 32 mm:n linja, HV 32, täysiaukkoinen venttiili, imupainemittaus käyttöönotossa |
| Imulinjan palloventtiili unohtuu kiinni | P1 käy kuivana ja rikkoutuu, ohjaus menetetään | Venttiilin asennonosoitin tai lukitus auki-asentoon, käynnistyksen tarkistuslista |
| Hihnan katkeaminen | Ohjaus vain orbitrolilla käsipumppuna (raskas) tai hätäpinnalla | Varahihna, P3-varapumppu (kytkentä **⚠ tarkista**) |

## Avoimet kysymykset

- [x] P1:n imuaukon koko: 3/4" [omistaja 2026-10-23]
- [ ] Säiliön öljypinnan korkeus suhteessa P1:n imuaukkoon
- [x] P2:n vanha 32 mm:n imuletku mahtuu P1:lle; pumpun päähän tarvitaan uusi letkukara/letkuliitin [omistaja 2026-10-23]
- [x] Päätös: P1:n imulinja 32 mm (2026-10-23)
- [ ] Säiliö: P2:n 50 mm:n ulosotto uuteen kohtaan, jotta vanha 32 mm:n ulosotto jää P1:lle
- [ ] Hankinta: uusi 32 mm:n letkukara + 3/4" BSP -liitin P1:n imuaukkoon (vanhaan letkuun) ja 3/4" T-kappale 1/4"-sivuaukolla mittausta varten (ks. [pressure-monitoring](pressure-monitoring.md#imupaineen-mittaus)), 32 mm:n täysiaukkoinen palloventtiili (jos nykyinen on 25 mm), alipainemittari (−1…0 bar)
- [x] Hihnavälitys pysyy 1:1,24 (päätös 2026-10-23)
