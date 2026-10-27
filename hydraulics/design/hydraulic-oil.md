# Hydrauliöljyn valinta

> **Tila:** selvitys 2026-10-23, päivitetty 2026-10-27 (nykyinen öljy tunnistettu; huuhtelu vanhalla öljyllä päätetty). **Päätetty 2026-10-23: HVLP 32** (tuote valitaan VI:n perusteella). Viskositeetit [laskelma, Walther-yhtälö],
> komponenttien rajat datalehdistä, tuotetiedot jälleenmyyjien sivuilta (haettu 2026-10-23).

Liittyy: [vaatimukset §9](../requirements.md#9-öljy-puhtaus-ja-huolto),
[P1:n imulinja](p1-steering-pump.md), [P2:n imupuoli](archive/p2-pump-options.md#imupuoli-letkun-koko-ja-pituus-sekä-öljylaatu),
[öljynjäähdytys](oil-cooling.md).

**Järjestelmässä nyt oleva öljy: Teboil Hydraulic Lift 32**: ISO VG 32, DIN 51524-3 (HVLP),
ISO 6743-4 HV [omistaja 2026-10-27]. Öljy on **noin 7 vuotta vanhaa, käyttöä alle 200 tuntia**
[omistaja 2026-10-27]. Kunto (vesi, epäpuhtaudet) on **⚠ ei tiedossa**, ja VI:tä ei löytynyt (Teboilin sivua
ei saatu auki). Tämän selvityksen "VG 46" on vanhojen laskelmien oletus, ei
veneessä oleva öljy.

**Mitä tästä seuraa [arvio]:** nykyinen öljy on **samaa luokkaa kuin päätetty HVLP 32**. Uusi öljy
(esim. Teboil Hydraulic Oil 32S) on siis yhteensopiva, eikä huuhtelua tarvita öljylaadun
vaihtumisen takia. Vaihdon perusteeksi jäävät öljyn tuntematon ikä, polymeerien hajoaminen
(HV-öljy ohenee vanhetessaan), mahdollinen vesi ja epäpuhtaudet sekä uudet pumput (PVH57 vaatii
puhtaan öljyn). Halvempi vaihtoehto on ottaa näyte ja jättää huuhtelu pois, jos öljy on kirkas
eikä siinä ole vettä: tyhjennetään säiliö ja letkut ja täytetään uudella, tai säästetään
huuhteluun varattu noin 20 l (noin 100 €). **Päätetty 2026-10-27:** vanha öljy
on kirkasta [omistaja 2026-10-27], ja sitä käytetään käyttöönoton huuhteluöljynä (kohta 2 alla).

**Iän ja tuntien perusteella [arvio]:** alle 200 tuntia on vähän, joten polymeerien hajoaminen ja
kuluminen ovat todennäköisesti vähäisiä. Seitsemän vuoden seisonnan riski on lähinnä
**kosteus** (lämpötilavaihtelut tiivistävät vettä säiliöön huohottimen kautta) ja lisäaineiden
vanheneminen. Siksi ehdotus:

1. **Näyte ennen päätöstä:** säiliön pohjalta lasipurkkiin. Kirkas ja vaalea öljy on hyvä merkki;
   samea tai maitomainen kertoo vedestä, ja pohjalle laskeutuva vesi tai sakka näkyy vuorokaudessa.
   Pohjan vesi lasketaan joka tapauksessa pois. Laboratorioanalyysi (vesi ppm, ISO 4406) antaa
   varmuuden; hinta **⚠ ei tiedossa**.
2. **Jos öljy on kirkasta (✅ valittu 2026-10-27):** vanha öljy kelpaa **käyttöönoton huuhteluöljyksi**. Uudet pumput ajetaan
   sisään ja letkut huuhdellaan vanhalla öljyllä uuden suodattimen läpi, ja sen jälkeen öljy
   vaihdetaan uuteen ja suodatinelementti vaihdetaan. Erillistä 20 litran huuhteluöljyä ei tarvita.
3. **Jos öljy on sameaa tai siinä on vettä:** toimitaan voimassa olevan päätöksen mukaan, eli
   tyhjennys, huuhtelu ja uusi öljy.

## Merkinnät

| Merkintä | Merkitys |
|---|---|
| ISO VG 32 / 46 | Viskositeettiluokka (ISO 3448): 32 / 46 cSt ±10 % 40 °C:ssa |
| HM (DIN: HLP) | Tavallinen kulumista estävä hydrauliöljy, viskositeetti-indeksi (VI) noin 95–110 (DIN 51524-2) |
| HV (DIN: HVLP) | HM + polymeeriset VI-parantajat, VI tyypillisesti noin 140–160+ (DIN 51524-3, ISO 11158 HV) |

HV-öljy on kylmänä ohuempi ja kuumana paksumpi kuin saman luokan HM-öljy. Haittana polymeerit
hajoavat käytössä, ja öljy ohenee vähitellen kohti HM-öljyä. Siksi kannattaa valita
leikkauskestävä laatu ja vaihtaa öljy ajallaan.

## Komponenttien viskositeettirajat

| Komponentti | Pienin | Suurin (käyttö) | Lähde |
|---|---|---|---|
| P1 Salami 2PE | **12 cSt** (suositus 17–65) | käynnistys 800 cSt | [datalehti Salami 2PE] |
| **P2 Vickers PVH57** (päätös 2026-10-27) | **⚠ ei tiedossa** (optimi 16–40 cSt) | kylmäkäynnistys ≤ 5000 cSt; öljy hetkellisesti ≤ 104 °C | [Eaton V-PUPI-TM008-E1 s. 31], ks. [p2-variable-pump](p2-variable-pump.md#tekniset-tiedot) |
| ~~P2 Parker F1~~ (arkistoitu) | 10 cSt (suositus 20–30) | **400 cSt**, käynnistys 4000; öljy ≤ 75 °C | [datalehti Parker HY30-8201] |
| Rexroth 2/2-venttiili | 20 cSt | **380 cSt** | [datalehti RE 18323-07] |
| Orbitroli HKUS | noin 10 cSt | noin 300 cSt; öljy ≤ 80 °C | M+S-ohjausyksiköiden yleistiedot [LöSi-luettelo](https://loesi.de/wp-content/uploads/2023/08/Hydrostatische-Lenkeinheiten_katalog_de-1.pdf); **⚠ tarkista** HKUS:n omasta datalehdestä |
| Sleipner-keulapotkuri | ei viskositeettirajaa | öljy alle 75 °C, suositus 40–60 °C | [ohje Sleipner 2746 35 2025] |

Sleipnerin omien hydraulijärjestelmien käyttöohje (HS 6468) näyttää hakutuloksen tiivistelmän
mukaan suosittavan mineraaliöljyä ISO 11158 HV / DIN 51524-3 HVLP, oletuksena VG 46 ja kylmiin
oloihin VG 32. Ohjetta ei saatu auki (linkki 404), joten **⚠ tarkista**. Vegalla on oma järjestelmä,
ja keulapotkurin ohje asettaa vain lämpötilarajan.

## Öljyjen vertailu [laskelma]

Walther-yhtälö (ASTM D341). HV 32 ja VG 46 kuten [P2:n imulaskelmassa](archive/p2-pump-options.md#imupuoli-letkun-koko-ja-pituus-sekä-öljylaatu);
HV 46 oletuksella VI noin 150 (7,9 cSt 100 °C:ssa). Imupaine P1:llä: 32 mm × 3,2 m, 3/4":n imuaukko,
säiliö 1 m pumpun yläpuolella, ks. [p1-steering-pump.md](p1-steering-pump.md).

| Öljy | 0 °C | 5 °C | 20 °C | 60 °C | 70 °C | 75 °C | 12 cSt:n raja (P1) | P1 2400 rpm, 5 °C |
|---|---|---|---|---|---|---|---|---|
| VG 32 (HM) | 336 | 229 | 86 | 15,2 | 11,2 | 9,7 | ~68 °C | −0,22 bar |
| **HV 32** (VI ~145) | **237** | **172** | 76 | 16,5 | 12,5 | 11,0 | **~72 °C** | **−0,15 bar** |
| VG 46 (HM) | 577 ❌ | 382 ❌ | 134 | 20,6 | 14,9 | 12,8 | ~78 °C | −0,39 bar ❌ |
| HV 46 (VI ~150) | 420 ❌ | 295 | 119 | 22,2 | 16,4 | 14,3 | ~82 °C | −0,29 bar (rajalla) |

❌ = ylittää Rexrothin 380 cSt:n tai F1:n 400 cSt:n rajan tai alittaa Salamin imurajan (−0,3 bar).

- **HV 32 on ainoa, joka pysyy kaikkien komponenttien rajoissa 0 °C:sta noin 72 °C:seen,** ja sillä
  on paras imumarginaali (P1 ja P2).
- **HV 32:n heikkous on kuuma pää.** P1:n 12 cSt:n minimi tulee vastaan noin 72 °C:ssa, VG 46:lla
  vasta noin 78 °C:ssa. Öljynjäähdytysselvityksen mukaan matka-ajossa öljy on noin 55–60 °C, mutta
  kuumassa konehuoneessa 65–70 °C. Siksi jäähdytin ja 70 °C:n hälytys ([vaatimukset §7](../requirements.md))
  kuuluvat HV 32:n kanssa yhteen. Korkeampi VI nostaa rajaa.
- **HV 46** on kuumana turvallisin, mutta alle noin 5 °C:n käynnistyksessä se ylittää venttiilin ja
  F1:n rajat, ja P1:n imu on rajalla.
- **VG 46 (HM)** on huonoin: jo 5 °C:ssa se on Rexrothin venttiilin rajalla, ja P1 kavitoi kylmänä.
- Kuumana kaikkien öljyjen ohentuminen lisää hammaspyöräpumpun ja keulapotkurin moottorin sisäistä
  vuotoa: tuotto ja työntövoima laskevat muutaman prosentin, ja kuluminen kasvaa hieman.

## Saatavilla olevat HVLP 32 -öljyt (20 l)

Haettu 2026-10-23; hinnat sis. ALV 25,5 %.

| Tuote | Luokitus | VI | Hinta | Huom. | Lähde |
|---|---|---|---|---|---|
| **Teboil Hydraulic Oil 32S** | DIN 51524-3 HVLP; Parker Denison HF-0/1/2 | **⚠ ei tiedossa** | 104,90 € | Varastossa | [AM-Asennus](https://www.am-asennus.fi/tuote/teboil-hydraulic-oil-32s-20l/) |
| Neste Hydraulic 32 Super | HVLP-sarja | **⚠ ei tiedossa** (46 Superilla > 185) | **⚠ ei tiedossa** | Jos VI on yli 180, kuumana paras | [Neste 46 Super](https://neste.fi/tuote/neste-hydraulic-46-super_en) |
| Valvoline Ultramax HVLP 32 | DIN 51524-3; Parker HF-0 | 144 (6,2 cSt 100 °C:ssa), jähmepiste −48 °C | 97,90 € | Loppu varastosta | [AM-Asennus](https://www.am-asennus.fi/tuote/valvoline-ultramax-hvlp-32-hydrauliikkaoljy-20l) |
| Motox 32 Universal HVLP | ISO 11158 HV | **⚠ ei tiedossa** | 6,99 €/l | Vain 1 l:n astia | [Motonet](https://www.motonet.fi/tuote/motox-32-universal-hvlp-hydraulic-oil-1-l-hydraulioljy?product=59-6100) |

80 litraa maksaa noin 420 € (4 × 20 l Teboil 32S). Biohajoavat öljyt (HEES) eivät ole tarpeen
yksityisaluksessa, ja ne ovat kalliimpia.

## Suositus

1. **HVLP 32 (DIN 51524-3), VI vähintään noin 150, mieluiten yli 180, ja Parker HF-0 -hyväksyntä.**
   Pyydä Teboil 32S:n ja Neste Hydraulic 32 Superin tuotetiedotteet ja valitse se, jonka VI on
   korkeampi ja jonka leikkauskestävyys on ilmoitettu. Teboil 32S on turvallinen oletus, ja sitä
   on saatavilla.
2. **Koko öljy vaihdetaan käyttöönoton jälkeen** (päätös 2026-10-27). Vanha, kirkas öljy toimii
   ensin huuhteluöljynä uuden suodatinelementin läpi, ja sillä ajetaan **vähintään koeajot** [omistaja 2026-10-27]. Sen jälkeen öljy tyhjennetään säiliön lisäksi
   letkuista, sylinteristä ja orbitrolista, ja suodatinelementti vaihdetaan.
3. **HV 46 vain, jos öljynjäähdytin jää pois** tai venettä käytetään vain lämpimänä kautena. Silloin
   kylmäkäynnistyksessä ajetaan tyhjäkäynnillä, kunnes öljy on yli noin 10 °C.

## Avoimet kysymykset

- [x] Mitä öljyä järjestelmässä nyt on: Teboil Hydraulic Lift 32 (HVLP, ISO VG 32) [omistaja 2026-10-27]
- [x] Nykyisen öljyn ikä: noin 7 vuotta, alle 200 tuntia [omistaja 2026-10-27]
- [x] Nykyisen öljyn kunto: kirkasta [omistaja 2026-10-27]
- [ ] Hydraulic Lift 32:n VI (tuotetiedote)
- [x] Huuhtelu: vanhalla öljyllä käyttöönotossa, ei erillistä huuhteluöljyä (päätös 2026-10-27)
- [x] Milloin huuhteluöljy vaihdetaan: vanhalla öljyllä ajetaan **vähintään koeajot** ennen vaihtoa [omistaja 2026-10-27]
- [ ] Tarvitaanko käyttöönotossa erillinen suodatinelementti, joka vaihdetaan samalla
- [ ] Teboil 32S:n ja Neste Hydraulic 32 Superin VI ja leikkauskestävyys (tuotetiedotteet)
- [ ] Orbitrolin HKUS 160/4 viskositeettialue omasta datalehdestä
- [ ] Sleipnerin öljysuositus (HS 6468 -ohje) keulapotkurijärjestelmälle
- [x] Päätös öljystä: HVLP 32, VI ≥ 150 (2026-10-23)
- [ ] Tuotteen valinta (Teboil 32S tai Neste Hydraulic 32 Super) ja määrä: 80 l täyttö (huuhtelu vanhalla öljyllä, päätös 2026-10-27)
