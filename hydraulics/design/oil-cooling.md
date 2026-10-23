# Hydrauliöljyn lämpökuorma ja jäähdytys

> **Tila:** Selvitys, päivitetty 2026-10-23. Ei vielä päätöstä. Laskelmat ovat arvioita [laskelma]; oletukset
> on kerrottu kunkin taulukon yhteydessä. Tausta: [current-system.md](../current-system.md),
> [p2-pump-options.md](p2-pump-options.md).

## Yhteenveto

- **Suurin lämmönlähde on ylimääräinen virtaus, joka kuristetaan korkeassa paineessa:** VPR3
  ohjaa ylimäärän säiliöön lähes kuormapaineessa, ja loput menee paineenrajoituksen yli. Määrä
  kasvaa koneen kierrosten mukana, mutta keulapotkurin työntövoima ei kasva.
- **Säiliö ja letkut luovuttavat itsestään vain noin 0,5 kW**, joten pienetkin jatkuvat kuormat
  nostavat öljyn pitkällä matkalla korkealle.
- **Varalla oleva Bowman EC100** kestää 92 l/min ja jäähdyttää merivedellä noin 7–9 kW. Se
  riittää kaikkiin jatkuviin kuormiin ja keulapotkurin käyttöön tyhjäkäynnillä. **⚠ Malli voi olla
  myös EC80** (noin puolet tehosta, noin 3,5–4,5 kW), ks. [Malli](#malli-ec100-vai-ec80--tarkista).
- **Suositus:** EC100 kaikkien piirien yhteiseen paluulinjaan ohitusventtiilin kanssa, merivesi
  koneen merivesipiiristä. Lisäksi kierroslukitus ja öljyn lämpötila-anturi.

## Mistä lämpö tulee

Kaikki teho, jota toimilaitteet eivät muuta työksi, päätyy öljyyn:
**lämpö (kW) = virtaus (l/min) × painehäviö (bar) / 600**.

1. **Ylimääräinen virtaus korkeassa paineessa:** apupiirin VPR3:n ylimäärä ja paineenrajoituksen
   ylitys. Esimerkiksi 23 l/min × 255 bar ≈ 10 kW.
2. **Komponenttien häviöt:** pumppu, venttiilit, letkut ja keulapotkurin moottori, yhteensä
   muutamia kilowatteja keulapotkurin käydessä.
3. **Ohjauspiiri:** orbitrolin läpivirtaus ja RPF3:n ylimäärä, jatkuvasti noin 0,2–0,7 kW.

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
| **Päätetty ratkaisu (2026-10-23):** ajossa BPV:n ohitus, pumppu kiertää tyhjänä | **⚠ ei tiedossa** (Parker ei ilmoita ohitustilan lämpöä); mitataan ensimmäisellä kaudella |

Viimeisessä tapauksessa lämpeneminen on hidasta: 40 → 75 °C noin 1 tunnissa (kuorman mukaan
45–90 min), 20 → 75 °C noin 1,5 tunnissa. Kytkimen unohtuminen päälle koko matkan ajaksi
ylikuumentaa öljyn, mutta lyhyt hetki ei.

Parker F1:n **BPV-ohitusventtiili** pienentäisi viimeisen tapauksen lämpökuormaa ja läpivirtausta
huomattavasti, koska öljy kiertää silloin pumpun päätykappaleessa eikä koko piirin kautta (tarkka
luku **⚠ ei tiedossa**), ks.
[p2-pump-options.md](p2-pump-options.md#lisävaruste-parker-bpv-f1--ohitusventtiili).

## Bowman EC100 -jäähdytin (omistajilla varalla; malli ⚠ EC100 vai EC80)

Omistajien tiedot [omistaja 2026-10-22]: Bowman EC100 -sarjan öljynjäähdytin, **pronssiset
päätykannet** (marine-versio), ollut aiemmin käytössä **Masson-vaihteiston öljynjäähdyttimenä**.
Putket ovat kunnossa ja puhtaat. Sinkkianodi voidaan vaihtaa tarvittaessa.

Valmistajan tiedot ([Bowman EC Series Product Profile](https://ej-bowman.com/wp-content/uploads/2023/05/EC-Series-Product-Profile.pdf),
s. 1–2, luettu kuvana ja tekstinä):

| Kohde | EC100 |
|---|---|
| Suurin öljyvirtaus (vaippapuoli) | **92 l/min** |
| Painehäviö öljypuolella (ISO 46) | 0,09 bar / 25 l/min · 0,17 bar / 35 l/min · 0,26 bar / 45 l/min · 0,44 bar / 60 l/min |
| Jäähdytysteho, öljy 60 °C sisään, vesi 30 °C 40 l/min | 4,1 kW / 20 · 5,0 kW / 30 · 5,8 kW / 40 · 6,5 kW / 50 l/min öljyä |
| Jäähdytysteho, öljy 70 °C sisään, vesi 25 °C 50 l/min | 6,5 kW / 20 · 8,1 kW / 30 · 9,4 kW / 40 · 10,5 kW / 50 l/min öljyä |
| Merivesivirtaus, 3-vetoinen | vähintään 25 l/min, enintään 50 l/min (1-vetoinen 85–170, 2-vetoinen 40–80) |
| Vesipuolen painehäviö | 0,05 bar / 25 l/min · 0,19 bar / 50 l/min |
| Liitännät | öljy 3/4" BSP, vesi 3/4" BSP |
| Materiaalit | putket 90/10-kupronikkeli, vaippa alumiini, marine-päätykannet pronssi |
| Mitat ja paino | runko Ø84 mm, pituus noin 260 mm, 3,2 kg |
| Öljypuolen paineluokka | **⚠ ei ilmoitettu esitteessä**; asennetaan vain matalapaineiselle paluupuolelle |

**Teho Vegalla** [laskelma]: esitteen arvot on mitattu 25–30 °C:n vedellä. Kun säiliön öljy on
50–60 °C ja merivesi noin 15 °C, teho on suunnilleen lämpötilaeron suhteessa suurempi: **noin
7–9 kW 40 l/min:n öljyvirtauksella**. Se riittää:

- ✅ kaikkiin jatkuviin kuormiin (ohjaus, kytkin päällä tyhjäkäynnillä, ankkurivinssi);
- ✅ käytännössä jatkuvaan keulapotkurin käyttöön tyhjäkäynnillä (~8 kW);
- ❌ ei keulapotkurin käyttöön 1000–1800 rpm:llä (16–38 kW), joten kierroslukitus tarvitaan silti.

### Malli: EC100 vai EC80? **⚠ tarkista**

Omistajat eivät ole varmoja, onko varalla oleva jäähdytin EC100 vai pienempi EC80
[omistaja 2026-10-23]. Bowmanin luettelo samoilla ehdoilla (ISO VG 37 -öljy, öljy ulos 50 °C,
öljyn painehäviö 1 bar, vesi sisään 25 °C, veden painehäviö 0,5 bar)
([EC Series Product Profile](https://ej-bowman.com/wp-content/uploads/2023/05/EC-Series-Product-Profile.pdf), luettu tekstinä):

| | EC80 | EC100 |
|---|---|---|
| Jäähdytysteho, merivesiversio (-3875-) | **4 kW** | **8 kW** |
| Jäähdytysteho, makean veden versio (-1425-) | 4 kW | 9 kW |
| Suurin öljyvirtaus | 80 l/min | 92 l/min |
| Suurin merivesivirtaus | 50 l/min | 50 l/min |
| Öljytilavuus | 0,26 l | 0,49 l |
| **Pituus (A)** | **174 mm** | **260 mm** |
| **Öljyliitäntä** | **1/2" BSP** | **3/4" BSP** |
| Paino | 2,4 kg | 3,2 kg |
| Tyyppikilven koodi | EC 80-xxxx-**1** | EC100-xxxx-**2** |

**Tunnistus:** mitta päästä päähän (noin 17 vai 26 cm) ja öljyliitäntöjen koko riittävät.
Tyyppikilven koodin numero kertoo samalla vesiversion (esim. 3875 = merivesi).

**Jos se on EC80** [laskelma, arvio]: teho Vegalla noin puolet EC100:sta eli **noin 3,5–4,5 kW**.
Se riittää:

- ✅ jatkuviin kuormiin (ohjaus matka-ajossa noin 0,5 kW, BPV:n ohitus);
- ✅ tavallisiin keulapotkurimanöövereihin tyhjäkäynnillä (1–2 min, noin 8 kW): öljy lämpenee
  hitaammin kuin ilman jäähdytintä;
- ❌ ei pitkään jatkuvaan keulapotkurin käyttöön: 8 kW:n kuormalla öljy lämpenee edelleen,
  noin puolta hitaammin kuin ilman jäähdytintä.

Vegan käytössä (satamamanööverit lyhyitä, matka-ajossa P2 ohituksella) EC80 todennäköisesti
riittää, mutta EC100 antaa marginaalia. Uusi merivesi-EC100 maksaa noin **⚠ ei tiedossa**.

## Asennustapa: paluulinja vai erillinen piiri

| | Paluulinjaan (suositus) | Erillinen sivuvirtapiiri sähköpumpulla |
|---|---|---|
| Lisäosat | ohitusventtiili jäähdyttimen rinnalle | sähköpumppu ja moottori, linjat, sulake, ohjaus |
| Virtaus jäähdyttimen läpi | vaihtelee kuorman mukaan, noin 15–60 l/min | tasainen, esim. 20–30 l/min |
| Sähkönkulutus | ei mitään | noin 0,2–0,4 kW, 24 V:lla noin 10–15 A |
| Kylmä käynnistys | ohitusventtiili suojaa jäähdytintä | pumpun voi pitää pois päältä kunnes öljy lämpenee |
| Lisähyöty | — | samaan piiriin voi lisätä hienosuodattimen |
| Haitat | jäähdytin on mukana jokaisessa paluuvirrassa | lisää osia ja vikaantumiskohtia; tarvitsee silti meriveden |

Koska EC100 kestää 92 l/min ja painehäviö on alle 0,5 bar, **paluulinja on yksinkertaisempi ja
riittää**. Erillinen piiri kannattaa vain, jos halutaan samalla sivuvirtasuodatus tai jäähdytys myös
koneen ollessa sammutettuna (vaatisi oman merivesipumpun).

## Paluulinja-asennus

1. **Kaikki paluut yhteen linjaan:** VPR3:n ylimäärä, 2/2-venttiili, BAV-713:n T, RPF3:n ylimäärä ja
   orbitrolin T → EC100 → paluusuodatin → säiliö. **Myös U11:n vuotolinja on kytketty paluulinjaan**
   [omistaja 2026-10-23]: jos se liittyy ennen jäähdytintä ja ohitusventtiiliä, moottorin kotelo saa
   saman vastapaineen (kylmänä jopa 3–4 bar + suodatin); kotelon raja **⚠ ei tiedossa**. Vuotolinja
   kannattaa liittää suodattimen jälkeen tai suoraan säiliöön. Normaalisti virtaus on noin 15–60 l/min. 1800 rpm:llä
   kytkin päällä virtaus olisi noin 125 l/min, ja ylimäärä kulkee ohitusventtiilin kautta.
2. **Ohitusventtiili** (takaiskuventtiili) jäähdyttimen rinnalle, avautuu noin 3–4 barissa. Suojaa
   jäähdytintä kylmältä, paksulta öljyltä ja virtapiikeiltä.
3. **Merivesi** koneen merivesipiiristä **rinnakkaishaarana, jonka virtaus on rajoitettu**, ks.
   [Merivesi](#merivesi). EC100 (3-vetoinen) tarvitsee 25–50 l/min.
4. **Liian kylmä öljy:** 5-asteinen merivesi voi keväällä pitää öljyn kylmänä. Tarvittaessa
   merivesipuolelle käsiventtiili tai öljypuolelle termostaattinen ohitus (ohittaa jäähdyttimen alle
   noin 40–45 °C:ssa).
5. **Sinkkianodi** tarkistetaan ja vaihdetaan tarvittaessa ennen käyttöönottoa.

## Merivesi

Koneen merivesipumppu on koneen etupään omassa voimanulosotossa kiinteällä välityksellä. Sen tuotto
on verkkohaun mukaan noin **70 l/min koneen 650 rpm:llä** [omistaja 2026-10-22, verkkohaun perusteella;
**⚠ vahvistamatta**]. Kiinteällä välityksellä tuotto kasvaa suunnilleen koneen kierrosten
suhteessa: noin 75 l/min tyhjäkäynnillä (700 rpm), noin 110 l/min 1000 rpm:llä ja noin 190 l/min
1800 rpm:llä [laskelma].

Samassa merivesipiirissä ovat jo **pääkoneen lämmönvaihdin ja merivaihteen (Advance 300) oma
öljynjäähdytin** [omistaja 2026-10-22].

**Koko merivesivirtaus ei voi kulkea EC100:n läpi**, jos se on 3-vetoinen: suurin sallittu
merivesivirtaus on silloin 50 l/min (2 m/s; ylitys kuluttaa putkia eroosiolla). 2-vetoisella raja on
80 l/min ja 1-vetoisella 170 l/min, joten sarjakytkentä ei riitä millään versiolla 1800 rpm:llä.
**⚠ Tarkista vetojen määrä tyyppikilvestä.**

**Ratkaisu: EC100 rinnakkaishaaraan, jonka virtaus rajoitetaan.**

- Haara otetaan merivesilinjasta ja palautetaan siihen **ennen koneen lämmönvaihdinta**. Koko
  merivesi kulkee silti koneen jäähdytyksen kautta, joten koneen jäähdytys ei heikkene. Hydrauliikan
  lämpö nostaa meriveden lämpötilaa vain noin 1–2 °C (8 kW, 70 l/min).
- Haaran virtaus rajoitetaan joko
  - **vakiovirtausventtiilillä** (merivettä kestävä pronssinen virtauksenrajoitin, esim. noin
    30–40 l/min): virtaus pysyy sopivana kaikilla kierroksilla; tai
  - **käsiventtiilillä tai kuristuslaipalla**, joka säädetään niin, että virtaus on suurimmilla
    käyttökierroksilla enintään noin 50 l/min. Tyhjäkäynnillä virtaus jää silloin noin 20 l/min:iin,
    mikä on alle 3-vetoisen suositellun minimin (25 l/min) ja heikentää tehoa jonkin verran. Kylmällä
    merivedellä teho riittää silti tavallisiin kuormiin.
- Haaran rinnalle päälinjaan tarvitaan pieni painehäviö (esim. venttiili tai kuristus), jotta osa
  virtauksesta ohjautuu haaraan. EC100:n painehäviö on noin 0,05 bar 25 l/min:llä ja noin 0,19 bar
  50 l/min:llä.
- **Merivaihteen jäähdytin saa edelleen koko virtauksen:** EC100-haara sijoitetaan päälinjaan
  niin, että sekä merivaihteen jäähdytin että koneen lämmönvaihdin ovat haaran ulkopuolella. Haara
  voi olla ennen tai jälkeen merivaihteen jäähdyttimen; EC100:n lämpö (enintään noin 8 kW) nostaa
  meriveden lämpötilaa vain noin 1–2 °C, mikä ei haittaa kumpaakaan.
- **Haaraa ei kytketä merivaihteen jäähdyttimen rinnalle**, vaikka sen painehäviö ajaisi virtausta
  haaraan ilman erillistä kuristusta: se veisi vettä merivaihteen jäähdytykseltä.
- Merivaihteen jäähdyttimen vaatima merivesivirtaus kannattaa tarkistaa Advance 300:n ohjeesta.
  **⚠ Tarkista.**

**Merivesivirtauksen varmistaminen:** Caterpillar-huolto tai varaosakirja (merivesipumpun malli ja
välitys), tai mittaus esim. läpivirtausmittarilla. Letkun irrottamista ja ämpärimittausta käyvällä
koneella ei suositella, koska kone jää silloin ilman jäähdytystä.

## Valvonta

- **Öljyn lämpötila-anturi** (päätetty 2026-10-23) säiliöön tai paluulinjaan Signal K:hon: varoitus noin 65 °C, hälytys
  noin 70 °C. Raja tulee ohjauspumpusta: Salamin 2PE vaatii vähintään 12 cSt, ja HV 32 ohenee
  sen alle noin 70 °C:n yläpuolella (Parker F1:n oma raja on 75 °C). Ensimmäisen kauden mittaukset
  näyttävät todelliset lämpötilat.
- **Paluulinjan vastapaine** (jäähdytin, ohitusventtiili, suodatin) pitää pysyä alle 25 barin, joka
  on orbitrolin (HKUS 160/4) T-linjan suurin jatkuva paine. 3–4 barin ohitusventtiilillä tämä täyttyy
  reilusti.
- **Kierroslukitus** (päivitetty 2026-10-23: PTO-kytkimen sijaan BPV-ohitusventtiili, ks. [requirements.md §10.2](../requirements.md)). Alkuperäinen muotoilu: kytkin päälle vain alle noin
  1000 rpm:ssä; sen yli keulapotkurin venttiili estetään ja vapaakiertoventtiili avataan; hälytys,
  jos kytkin on päällä yli noin 1200 rpm:ssä.

## Avoimet kysymykset

- [ ] Onko varalla oleva jäähdytin EC100 vai EC80 (pituus 26 vs. 17 cm, öljyliitäntä 3/4" vs. 1/2"), ja tyyppikilven koko koodi (vesiversio, vedot)
- [x] Koneen merivesipumpun tuotto: noin 70 l/min 650 rpm:llä [omistaja 2026-10-22]
- [x] 650 rpm on koneen kierrosluku; pumppu on koneen etupään voimanulosotossa kiinteällä välityksellä
- [ ] Vahvista merivesipumpun tuotto (verkkohaun arvo ~70 l/min 650 rpm) ja välityssuhde
- [ ] Merivaihteen (Advance 300) jäähdyttimen vaatima merivesivirtaus
- [ ] Rinnakkaishaaran virtauksenrajoitus: vakiovirtausventtiili vai säädettävä venttiili
- [x] Merivaihde jäähdytetään samasta merivesipiiristä omalla lämmönvaihtimellaan
- [ ] Paluulinjojen yhdistäminen ja ohitusventtiilin valinta
- [ ] Tarvitaanko termostaattinen ohitus kylmän meriveden aikaan
