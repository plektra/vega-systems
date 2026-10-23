# Vega — hydrauliikan nykytila (lähtötilanne)

> **Tila:** Koottu Plektra-blogista (2016–2021) ja omistajien antamista tiedoista lokakuussa 2026
> (ks. §0). Päivitetty 2026-10-22: tyhjäkäynti 700 rpm, pumppusuositus 51 cm³. Kohdat, joissa on merkintä **⚠ tarkista**, pitää tarkistaa veneellä.
>
> **Hydraulijärjestelmä on tällä hetkellä kokonaan purettuna** (lokakuu 2026). Luvut 3.1–3.5
> kuvaavat viimeisintä koottua kokoonpanoa (2017–2018). Osa niiden osista käytetään uudelleen.
>
> Lähteet: `[blogi VVVV-KK-PP]` viittaa blogikirjoituksiin (`plektra.github.io/_posts/`),
> `[omistaja VVVV-KK-PP]` omistajien antamiin tietoihin.

## 0. Nykytilanne (omistajien päivitys 2026-10-21)

| Kohde | Tila |
|---|---|
| Vaihteisto | Advance 300 on **asennettu ja linjattu** potkuriakseliin, ja akselille on uusi laakeripukki |
| Pääkone | Asennetaan takaisin ja linjataan vaihteistoon |
| Hydrauliikka | **Kokonaan purettu**, molemmat pumput irrotettu. Mitään ei kootaan ennen kuin kone on linjattu. |
| Suunnitelma: ohjauspumppu | Pieni vakiotilavuuspumppu (P1, 16,6 cm³) palaa koneen etupäähän, kahden kiilahihnan vetämänä kuten ennenkin. **Vain ohjaukselle.** |
| Suunnitelma: apupiirin pumppu | Iso pumppu **suoraan Advance 300:n voimanulosotosta (PTO)** |
| Advance 300:n PTO | **Välitys 1:1, käyttö ensiöakselilta** (pyörii aina kun kone käy, myös vapaalla). **Ei omaa kytkintä.** Nimellisteho **0,044 kW/rpm**, eli vakiomomenttiraja **≈ 420 Nm** (35 kW 800 rpm:llä, 110 kW 2500 rpm:llä). Ulostulo on **sileä Ø48 mm:n kiila-akseli** ilman pumppulaippaa. |
| Suunnitelma: PTO-voimansiirto | PTO-akseli → **HRC 150 -joustokytkin** → kytkin → P2. Kytkin ja pumppu ovat **omalla, runkoon kiinnitetyllä alustalla**, joten PTO-akselille ei tule pumpun painoa eikä sivukuormaa. |
| Suunnitelma: PTO-kytkin | Kytkin joustokytkimen ja P2:n väliin, jotta pumppu pyörii vain tarvittaessa. Ehdokas: Borelli 30500 -sarja, ks. [p2-pump-options.md](design/p2-pump-options.md). |
| Keulapotkurin letkut | **Pääosin valmiit:** 1/2" **SAE 100R2AT / EN 853** -letkut, omistajien mukaan 300 bar, CETOP-venttiileiltä keulapotkurille. A- ja B-linjat **8,5 m kumpikin**. |
| P2:n painelinja | 3/4" letku pumpulta venttiileille. PTO-sijoitus vaatii **3–4 m** letkua. |
| P2:n imulinja | **32 mm:n sisähalkaisija** (≈ 1-1/4", DN32), noin **3 m** uudelle pumpun paikalle. Säiliön öljypinta on noin 1 m pumpun imuaukon yläpuolella. |
| Apupiirin paluulinja | 3/4" letku, **< 0,5 m**, venttiililohkolta säiliöön (paluusuodattimen kautta) |
| Päätös: järjestelmäpaine | **Pysytään 250 barin luokassa.** Noin 90 %:n keulapotkuriteho hyväksytään kustannusten vuoksi. |

### Suunniteltu voimansiirto

```
                 ┌── 2 kiilahihnaa, 1:1,24 ── P1 16,6 cm³ ── ohjauspiiri (orbitroli + sylinteri)
 CAT 3126B ──────┤
  (etupää)       │
                 └── vauhtipyörä ── Advance 300 ── potkuriakseli
                                    │
                                    └── PTO 1:1, Ø48 kiila ── HRC 150 ── kytkin ── P2 (koko ⚠) ── apupiiri
                                                                └──── oma runkoalusta ────┘   (keulapotkuri, ankkurivinssi, …)
```

### Mitä tämä tarkoittaa suunnittelulle

1. **P1 hihnavetoisena on hyvä ratkaisu.** Ohjaus toimii pienellä paineella (normaalisti < 50 bar),
   noin 13 l/min 700 rpm:n tyhjäkäynnillä. Hihnat kantoivat tämän kuorman ongelmitta 2017–2018.
2. **Nykyinen 33,5 cm³:n pumppu on liian pieni 1:1-PTO:lle.** 700 rpm:n tyhjäkäynnillä
   [omistaja 2026-10-22] se antaa noin 22 l/min (volumetrinen hyötysuhde 92 %). Se jää alle
   keulapotkurin 60 %:n tehon tarpeen (26,2 l/min) ja selvästi alle 100 %:n tarpeen (33,8 l/min).
   Blogissa todettiin jo 2018, että 1:1-veto tarkoittaa uusia pumppuja.

   | Tyhjäkäynti (PTO 1:1) | Kierrostilavuus 33,8 l/min:lle | Tuotto 2500 rpm:llä | Momentti 264 barilla |
   |---|---|---|---|
   | **700 rpm** (omistajan mukaan) | **52 cm³** | 120 l/min | 245 Nm |
   | 800 rpm | 46 cm³ | 106 l/min | 214 Nm |
   | 1000 rpm | 37 cm³ | 85 l/min | 172 Nm |

   *Oletukset: volumetrinen hyötysuhde 92 %, mekaaninen 90 %.* Käytännössä 250 barin
   paineenrajoituksella **51 cm³:n pumppu** riittää noin 88 %:n työntövoimaan 700 rpm:llä, ks.
   [p2-pump-options.md](design/p2-pump-options.md#herkkyys-tyhjäkäyntikierroksille).
3. **Ensiöakselin PTO pyörii vapaalla.** Juuri sitä keulapotkurin satamakäyttö vaatii.
4. **PTO:n nimellisarvossa on reilusti varaa.** 0,044 kW/rpm vastaa noin 420 Nm. 51 cm³:n pumppu
   250 barilla tarvitsee noin 225 Nm (54 %), eli noin 16,5 kW akselitehoa 700 rpm:llä (PTO:n raja
   700 rpm:llä 30,8 kW). Jopa 280 barin paineenrajoitus vaatisi vain noin 253 Nm (60 %), joten
   painepiikeille jää varaa.
5. **Järjestelmäpaine: 250 barin luokka, tavoite ~90 % työntövoimasta (päätetty).** Täysi teho
   vaatisi moottorilla 264 bar plus linjahäviöt. Omistajat hyväksyvät noin 90 %:n työntövoiman,
   jotta pumppu ja venttiilit voidaan valita yleisestä 250 barin luokasta. Todellisilla
   letkupituuksilla 250 barin paineenrajoitus antaa lämpimänä noin 85–89 %, ks. kohta 9.
6. **Kytkin estää öljyn lämpenemisen ajon aikana.** Ilman sitä ~51 cm³:n pumppu pumppaisi
   2500 rpm:llä noin 117 l/min jatkuvasti virtauksensäätöventtiilin läpi, mikä tuottaa noin 1 kW tai
   enemmän lämpöä, eikä öljynjäähdytintä ole. Kun kytkin on irti, P2 ei pyöri lainkaan.
7. **Kytkimen vaatimukset:**
   - **Momentti.** Jatkuva kuorma on noin 190–225 Nm 250 barilla (43–51 cm³). Hammaspyöräpumppu ja
     paineenrajoitusventtiili aiheuttavat painepiikkejä, joten kytkimessä pitää olla selvästi
     varaa. Kytkintä, joka on PTO:n omaa 420 Nm:ä paljon vahvempi, ei tarvita. Vertailu ehdokkaista
     on tiedostossa [p2-pump-options.md](design/p2-pump-options.md).
   - **Kytkentä.** Vain tyhjäkäynnillä. Kierroslukulukitus (N2K / Signal K) voi estää kytkennän
     noin 1000 rpm:n yläpuolella.
   - **Kytke pumppu kuormittamattomana.** Pidetään nykyinen jännitteettömänä auki oleva
     2/2-vapaakiertoventtiili. Kytkin kytketään venttiilin ollessa auki (pumppu kierrättää vapaasti
     säiliöön), ja venttiili suljetaan vasta sitten. Tämä vähentää kytkimen, PTO:n ja pumpun
     akselin iskukuormaa.
   - **Tyyppi.** PTO on sileä kiila-akseli ja kokoonpano on omalla alustallaan, joten kytkimen pitää
     olla **akselilta akselille** -tyyppinen, ei pumppulaippaan pultattava. Sähkömagneettiset
     vaihtoehdot on selvitetty tiedostossa [p2-pump-options.md](design/p2-pump-options.md).
   - **Ohjaus.** Mekaaninen vipukytkin voidaan kauko-ohjata push-pull-vaijerilla tai 24 V:n
     toimilaitteella, ja asennon voi tunnistaa rajakytkimellä (ESP32 PDM, Signal K).
   - **Joustokytkimen mitoitus.** Tarkista HRC 150:n elementti ja navat 48 mm:n reiälle, PTO-akselin
     kiilalle ja momentille. Muistini mukaan HRC 150:n nimellismomentti on noin 600 Nm, mikä
     riittäisi, ja suurin reikä riippuu napatyypistä (F/H taper-lock vai B). **⚠ Tarkista molemmat
     valmistajan luettelosta.**
   - **Linjaus.** Vaihteisto on kiinnitetty jäykästi runkoon [blogi 2021-02-08], kuten myös uusi
     kytkin- ja pumppualusta. HRC:n tarvitsee siis ottaa vastaan vain pienet asennusvirheet ja
     rungon joustot, ei koneen liikkeitä. Linjaa kytkimen ensiöakseli PTO-akseliin joustokytkimen
     sallimien säteis- ja kulmavirheiden sisään, ja tarkista uudelleen koeajon jälkeen.
   - **Tila.** Joustokytkin, kytkin ja pumppu peräkkäin vievät pituutta. Tarkista tila suhteessa
     runkoon, vaihteistoon ja potkuriakselin laakeriin.
8. **Nykyiset 1/2":n keulapotkuriletkut riittävät.** 33,8 l/min:llä öljyn nopeus 12,7 mm:n letkussa on
   noin 4,5 m/s, eli painelinjojen tavanomaisen 3–6 m/s:n ohjearvon sisällä. Arvioitu painehäviö
   letkumetriä kohden (vain suora letku, oletuksena ISO VG 46):

   | Öljyn lämpötila | Viskositeetti | Häviö / metri | Häviö 2 × 8,5 m (A + B) |
   |---|---|---|---|
   | 5 °C (kylmäkäynnistys) | ~380 cSt | ~2,9 bar | ~50 bar |
   | 20 °C | ~130 cSt | ~1,0 bar | ~17 bar |
   | 40 °C | 46 cSt | ~0,35 bar | ~6 bar |
   | 60 °C | ~21 cSt | ~0,30 bar | ~5 bar |

   *Vain suora letku; liittimet lisäävät hieman.* Letkut ovat SAE 100R2AT / EN 853. Standardin
   vähimmäistyöpaine 1/2":lle (-08) on noin 275 bar (4000 psi), ja omistajien mukaan näiden letkujen
   merkintä on 300 bar. Kummin tahansa se on yli 250 barin paineenrajoituksen.
   - **Paluulinjan (3/4", < 0,5 m) häviö on merkityksetön:** alle 0,3 bar kylmälläkin öljyllä.
     Säiliön puolella suurin häviö on paluusuodatin.
   - **P2:n painelinja (3/4", 3–4 m) ei ole ongelma.** Noin 33–37 l/min:llä (tyhjäkäynti) nopeus on
     noin 2,1 m/s ja häviö alle 1 bar lämpimänä. Noin 117 l/min:llä (2500 rpm, kytkin päällä) nopeus on noin
     7 m/s ja häviö noin 2–3 bar, mikä on hyväksyttävää.
   - **Käytä pitkissä keulapotkurilinjoissa letkua, älä putkea.** Muualla käytetyn 15×2-tarkkuusputken
     sisähalkaisija on 11 mm. Tällä virtauksella nopeus olisi noin 5,9 m/s ja häviö noin kaksinkertainen
     letkuun verrattuna.
9. **Keulapotkurin odotettu työntövoima lämpimällä öljyllä on noin 85–89 %, hieman alle 90 %:n
   tavoitteen.** Paineenrajoitusventtiili rajaa paineen pohjalaatalla 250 bariin. Venttiilin,
   letkujen ja paluulinjan häviöt vähennetään siitä, joten moottori saa vähemmän. Potkurin momentti
   kasvaa nopeuden neliössä, joten potkuri asettuu hieman pienemmälle kierrosnopeudelle ja ylimääräinen
   virtaus menee paineenrajoituksen yli.

   | Öljyn lämpötila | Potkurin kierrosnopeus | Työntövoima | Teho |
   |---|---|---|---|
   | 5 °C | ~86 % | ~74 % (~180 kg) | ~64 % |
   | 20 °C | ~92 % | ~84 % (~200 kg) | ~77 % |
   | 40 °C | ~94 % | ~88 % (~210 kg) | ~82 % |

   *Oletukset: noin 6 barin häviö venttiilin kummallakin reitillä (P→A ja B→T), mitatut
   letkupituudet ja noin 1,5 bar paluusuodattimessa. 4–10 barin venttiilihäviöillä lämmin tulos on
   85–89 %. **⚠ Hanki BAV-713:n painehäviökäyrä** tarkentamaan tätä.* Kilot on laskettu asennusohjeen
   240 kg:n suurimmasta työntövoimasta (kevyt käyttö).

   **Malli vahvistettu valmistajan taulukolla:** Side-Powerin mukaan 80 %:n työntövoimaan tarvitaan
   30,2 l/min ja 211 bar, eli virtaus 89 % ja paine 80 % täydestä. Tämä vastaa tässä käytettyä oletusta,
   että potkurin momentti ja työntövoima kasvavat kierrosnopeuden neliössä [datalehti Side-Power SH Series v1.0.0 2017].

   Täyden ~90 %:n saavuttaminen vaatii korkeamman paineenrajoituksen ja enemmän virtausta
   tyhjäkäynnillä, ks. [p2-pump-options.md](design/p2-pump-options.md#paineenrajoituksen-nostaminen-yli-250-barin).
10. **P2:n imulinja: omistajat vahvistivat 32 mm:n sisähalkaisijan (≈ 1-1/4"), mikä riittää.**
    Säiliön ulosotto on samaa kokoa, joten linjassa ei ole 1":n kuristusta. Arvioitu paine pumpun
    imuaukolla 51 cm³:n pumpulla, kun säiliön öljypinta on noin 1 m pumpun yläpuolella (+0,085 bar)
    ja liitinhäviöt ovat noin K = 2,5 (säiliön ulosotto, palloventtiili, kulmat):

    | Öljyn lämpötila | 700 rpm (tyhjäkäynti) | 1000 rpm |
    |---|---|---|
    | 5 °C | **−0,15 bar** | −0,26 bar |
    | 15 °C | −0,03 bar | −0,09 bar |
    | 20 °C | 0,00 bar | −0,04 bar |
    | 40 °C | +0,05 bar | +0,03 bar |

    Hammaspyöräpumput vaativat yleensä, että imupaine on vähintään noin −0,2…−0,3 bar (ylipaine).
    **Tarkista valitun pumpun datalehdestä.** 32 mm:n linja pysyy tämän sisällä tyhjäkäynnillä noin
    5 °C:een asti. (1":n linjalla vastaava arvo olisi ollut noin −0,5 bar, joten 32 mm oli oikea
    valinta.) Kylmänä kannattaa silti kytkeä pumppu tyhjäkäynnillä.
    Lähtö satamasta on kriittisin tilanne: keulapotkuria tarvitaan heti käynnistyksen jälkeen, kun
    öljy on konehuoneen lämpöistä. HV-luokan öljy antaa lisää marginaalia.

    2500 rpm:llä virtaus olisi niin suuri, että kytkimen pitää silti irrota automaattisesti noin
    1000–1200 rpm:n yläpuolella.

    **Päivitys 2026-10-23:** Parkerin F1-luettelon mukaan imupaineen pitää olla vähintään 1,0 bar
    absoluuttista (noin 0 bar ylipainetta), ja F1-61:lle suositellaan 50 mm:n imuliitintä. Nykyinen
    32 mm:n linja ei täytä tätä kylmällä öljyllä edes tyhjäkäynnillä (noin −0,2 bar 5 °C:ssa VG 46:lla).
    **Uusi suositus: 50 mm:n imulinja ja HV 32 -öljy.** Tämä koskee myös päätöslokin 2026-10-22
    merkintää, jonka perusteena oli −0,2 barin raja. **⚠ Omistajien päätettävä.**

    **Päivitys 2026-10-22:** Parker F1-061:llä (59,5 cm³) imuvirtaus on suurempi. **Suositus: 38 mm:n
    imulinja mahdollisimman lyhyenä (~2 m) ja HV 32 -öljy**, jolloin imupaine pysyy noin 0 barissa
    vielä 1000 rpm:llä ja 5 °C:ssa. Vertailu ja kierroslukuanalyysi:
    [p2-pump-options.md](design/p2-pump-options.md#imupuoli-letkun-koko-ja-pituus-sekä-öljylaatu).
11. **Jos konetta kierretään kytkimen ollessa päällä,** pumpun tuotto kasvaa kierrosten mukana (noin
    117 l/min 2500 rpm:llä 51 cm³:n pumpulla). Virtauksensäätöventtiilin ja paluulinjan pitää kestää se, tai kytkimen
    pitää irrota automaattisesti tietyn kierrosluvun yläpuolella. Tarkista VPR3:n suurin sallittu
    tulovirtaus (säädetty 35 l/min).

## 1–2. Alus ja voimansiirto

Siirretty yhteiseen [alustiedostoon](../vessel/README.md), jossa on myös muiden järjestelmien
tarvitsemat sähköjärjestelmän perustiedot.

## 3. Hydraulijärjestelmän yleiskuvaus

Alkuperäinen "traktorijärjestelmä" (hihnavetoinen pumppu omalla säiliöllään, orbitroli,
suuntaventtiili ja vuotava sylinteri) korvattiin 2017 **kahden piirin järjestelmällä**
[blogi 2017-04-01]:

- **Piiri 1 — Ohjaus:** pieni pumppu → etusijavirtauksen säätö → orbitroli → ohjaussylinteri.
  Piirissä on tarkoituksella vain peräsin, turvallisuussyistä.
- **Piiri 2 — Apupiiri:** iso pumppu → virtauksensäätö → vapaakiertoventtiili → CETOP 3 -pohjalaatta
  → keulapotkuri (myöhemmin myös ankkurivinssi ja muut kuormat).
- **Varajärjestelmä:** 24 V:n sähköpumppu, joka syöttää ohjauspiiriä vastaventtiilin kautta.
- **Vaihteiston kytkinhydrauliikka** on erillinen piiri, eikä se kuulu tähän.

![Hydraulikaavio v3, 2018](img/hydraulics-v3-2018.png)

*Kaavio v3 blogista (2018). Suunniteltu uusi kokoonpano: [schematic.md](schematic.md).*

### 3.1 Pumppujen veto (tilanne 2018)

| Kohde | Arvo | Lähde |
|---|---|---|
| Veto | Kiilahihnat (Optibelt Super X-Power) kampiakselilta tukilaakeriyksikön kautta kahdelle peräkkäiselle pumpulle | [blogi 2017-07-04] |
| Hihnapyörä / välitys | 180 mm:n hihnapyörä; kone:pumppu = 1:1,24 | [blogi 2017-07-04] |
| Pumppujen kiinnitys | 10 mm:n teräskannake pultattuna koneeseen, 10.9-pultit | [blogi 2017-07-04] |
| **Tunnettu rajoitus** | Hihnat luistavat apupumpulla yli **~160 barin** (~9 kW). Ei turvallinen jatkuvaan käyttöön. | [blogi 2018-11-12] |
| Suunniteltu korjaus (2018) | Pumput koneen eteen kardaaniakselilla (1:1), mikä vaatisi uudet pumput | [blogi 2018-11-12] |
| Suunniteltu korjaus (2021) | Iso pumppu uuden vaihteiston PTO:lle | [blogi 2021-02-08] |
| Päätös (2026) | P1 etupään hihnoille (vain ohjaus), P2 vaihteiston PTO:lle. Etupään kardaaniajatuksesta luovuttiin. | [omistaja 2026-10-21] |

### 3.2 Pumput

| Pumppu | Merkki | Kierrostilavuus | Arvot (kaavio) | Tuotto koneen 800 / 1800 / 2500 rpm:llä* | Syöttää |
|---|---|---|---|---|---|
| P1 | Salami **2PE16D-P28P1** (ryhmä 2, kartioakseli 1:8, laippa P1) | 16,6 cm³/r | 250 bar jatkuva / 280 ajoittainen / 300 huippu; **max 3000 rpm**, min 400 rpm [datalehti Salami 2PE] | 16,5 / 37,1 / 51,5 l/min | Ohjaus |
| P2 | Salami **3PB33D-P38P2**, hammaspyörä (ryhmä 3) | 33,5 cm³/r | 250 bar, 30–80 l/min | 33,2 / 74,8 / 103,8 l/min | Apupiiri (liian pieni PTO:lle, ks. §0) |
| P3 | Vanhasta voimayksiköstä; moottori 24 V, 2,5 kW | **⚠ ei tiedossa** | | | Varaohjaus |

\* Laskettu hihnavälityksellä 1:1,24 ja 100 %:n volumetrisella hyötysuhteella. Koneen 2500 rpm:llä
pumput pyörivät noin 3100 rpm. **P1:n (2PE16D) suurin sallittu kierrosnopeus on 3000 rpm**
[datalehti Salami 2PE], eli hihnavetoisena koneen kierrokset saavat olla enintään noin **2420 rpm**.
Koneen suurin kierrosluku on noin **2400 rpm** [omistaja 2026-10-22], jolloin P1 pyörii noin 2980 rpm:
**juuri ja juuri rajan sisällä**. Jos hihnapyöriä uusitaan, välitystä kannattaa hieman pienentää
(esim. 1:1,15 → noin 2760 rpm) marginaalin saamiseksi; ohjaukselle riittää silti noin 12 l/min
tyhjäkäynnillä. (Tämän dokumentin muut 2500 rpm:n laskelmat ovat varovaisia arvioita, jotka pätevät
myös 2400 rpm:llä.) Salamin 2PE-sarjan käyttöehdot: imupaine 0,7–2,5 bar absoluuttista,
viskositeetti vähintään 12 cSt (suositus 17–65 cSt, käynnistys enintään 800 cSt), öljy −15…+85 °C
(NBR-tiivisteet).

### 3.3 Piiri 1 — Ohjaus

| Komponentti | Tiedot | Huomiot |
|---|---|---|
| Virtauksensäätö | RPF3 (Marchesini, kolmitie, ylimäärä suoraan säiliöön), asetus 20 l/min. Suurin tulovirtaus 50 l/min (3/8") tai 85 l/min (1/2"), 350 bar [datalehti RPF3]; koko **⚠ tarkista** | Tyhjäkäynnillä pumppu antaa ~16,5 l/min, joten kaikki menee orbitrolille |
| Ohjausyksikkö | **M+S Hydraulic HKUS 160/4**: 158,4 cm³/r, avoin keskiasento, ei kuormantakaisinkytkentää; **sisäänrakennettu paineenrajoitus** (asetus 80–170 bar) ja iskuventtiilit (140–220 bar); nimellisvirtaus 16 l/min; **T-linjan suurin jatkuva paine 25 bar** [datalehti HKUS] | Paluulinjan vastapaine (esim. öljynjäähdytin ja sen ohitusventtiili) pitää pysyä alle 25 barin |
| Sylinteri | Kaksitoiminen; männän ja varren halkaisija sekä iskunpituus **⚠ ei tiedossa** | Kiinnitetty alkuperäiseen reikään lähellä peräsinakselia. Ei aivan yllä paapuurin ääriasentoon, ja reikä on hieman väljä. Saatetaan vaihtaa pidempään [blogi 2017-07-04]. |
| Hätäohitus | Käsiventtiili A- ja B-linjan välissä sylinterin vieressä, irrotettavaa hätäpinnaa varten | [blogi 2017-07-04] |
| Työpaine | Normaalisti < 50 bar | [blogi 2017-07-04] |
| Paineenrajoitus | Orbitrolin sisäänrakennettu paineenrajoitus; asetusarvo **⚠ tarkista** (tehdasvaihtoehdot 80–170 bar) | [datalehti HKUS] |
| Varasyöttö | P3 vastaventtiilin kautta RPF3:n tuloon | Suunniteltu 2017. **⚠ Tarkista**, onko asennettu. 65 A:n laturi ei jaksa syöttää sitä pitkään. |
| Ilmaus | Ei ilmausruuveja; sylinterin liitännät sivuilla | Vaikea ilmata [blogi 2017-07-04] |

### 3.4 Piiri 2 — Apupiiri

| Komponentti | Tiedot | Huomiot |
|---|---|---|
| Virtauksensäätö | VPR3 (Marchesini, kolmitie-etusijaventtiili), asetus 35 l/min, ylimäärä B-portista säiliöön. Suurin tulovirtaus 60 / 80 / 120 / 200 l/min (3/8" / 1/2" / 3/4" / 1"), 350 bar [datalehti VPR3] | Koko **⚠ tarkista**: 1/2" kestää vain 80 l/min |
| Vapaakiertoventtiili (keulapotkurin päälle/pois) | Bosch Rexroth OD15-X-17-Y-S0 -patruunaventtiili, 2/2, jännitteettömänä auki, esiohjattu istukka; 350 bar, 2–70 l/min [datalehti RE 18323-07]. **Kytkee paineen CETOP-pohjalaatalle** [omistaja 2026-10-22]. Todennäköisesti asennettu **pohjalaatan paineenrajoitusventtiilin kavitettiin** (P→T): auki se purkaa pohjalaatan P-kanavan säiliöön, kiinni paine nousee pohjalaatalla. **⚠ Vahvista.** | Jännitteettömänä P2:n tuotto menee matalalla paineella säiliöön; jännitteellisenä venttiili sulkeutuu ja paine menee BAV-713:lle. Ohjataan päälle aina, kun keulapotkuria käytetään kumpaan tahansa suuntaan. |
| Pohjalaatta | **Flowfit CETOP 3 / NG6, 4-paikkainen, rinnankytketty**, paineenrajoitusventtiilin paikalla (kavitetti P→T) ja painemittariliitännällä. Liitännät: **P ja T 1/2" BSP, A ja B 3/8" BSP**, G (mittari) 1/4" BSP. Pituus 247,7 mm, paino 8,21 kg. **Materiaali teräs** [omistaja 2026-10-22]. Painearvoa ei ilmoitettu; teräksiset CETOP 3 -pohjalaatat on tyypillisesti luokiteltu noin 250–350 bariin **⚠ vahvista Flowfitilta** [datalehti Flowfit CETOP 3]. | 1 paikka käytössä (BAV-713), 3 vapaana (ankkurivinssi ym.). A/B-liitännät ovat 3/8", vaikka keulapotkurin letkut ovat 1/2": pieni lisähäviö, sisältyy venttiilihäviön arvioon. |
| Paineenrajoitusventtiili | **Marchesini VMP 3/4"** (V0720), suoratoiminen istukkaventtiili, asetettu 250 bariin. Suurin virtaus **90 l/min**, suurin paine 350 bar. Jousi todennäköisesti 80–300 bar (vastaa aiemmin mainittua 300 baria), 50 bar / kierros [datalehti VMP, omistaja 2026-10-22] | Aiemmin kirjattu "300 bar, 80 l/min" korjattu datalehden mukaan |
| Keulapotkurin suuntaventtiili | **fluiconnecto (Manuli) BAV-IC3-713**, suoraan ohjattu 4/3-solenoidiventtiili, NG6 / CETOP 03, pohjalaatassa; **valitsee pyörimissuunnan** [omistaja 2026-10-22]. Keskiasennossa A, B ja T yhdistetty, P suljettu (moottori pyörii vapaasti). Suurin virtaus **60 l/min**, suurin paine **350 bar**; kelat BAV-SPC3, 12 tai 24 VDC (**⚠ tarkista** jännite) [datalehti fluiconnecto, Teollisuusventtiilit s. 239] | Painehäviökäyrää ei ole luettelossa |
| Painemittari | P-linjassa ennen pohjalaattaa | Ei näy kaaviossa |
| Keulapotkuri | **Side-Power SH240/250TC-U11**: 250 mm:n tunneli, kaksi vastakkain pyörivää potkuria, hydraulimoottori U11. Työntövoima enintään **240 kg** (kevyt käyttö) / **220 kg** (raskas käyttö) [ohje Sleipner 2746 35 2025]; vanhemmassa esitteessä 220 / 200 kg. Hydraulinen teho 14,9 kW, **käyttöaika jatkuva**. Vaihteisto pronssia, öljykylpy omasta säiliöstä (EP 90, säiliö vesilinjan yläpuolelle); joustokytkin moottorin ja vetoakselin välissä. U11:n liitännät: A ja B 3/4" BSP, **vuotolinja 1/4" BSP pakollinen** (ylempi vuotoliitäntä; moottorin kotelo täytetään öljyllä ennen käynnistystä). Vain suorakierteiset liittimet, mieluiten pehmeätiivisteiset; ei kierreteippiä tai -tiivistettä. | Moottorin vuotolinja säiliöön |
| Keulapotkurin tarve (U11) | 60 %: 26,2 l/min × 158 bar · 80 %: 30,2 l/min × 211 bar · **100 %: 33,8 l/min × 264 bar** (≈ 14,9 kW hydraulista) [datalehti Side-Power SH Series v1.0.0 2017] | Prosentit ovat osuus suurimmasta työntövoimasta (100 % ≈ 240 kg asennusohjeen mukaan) |
| Saavutettu (hihnaveto) | ~160–170 bar, mikä riitti kääntämään aluksen laiturissa | [blogi 2018-11-12] |
| Ankkurivinssi | Hydraulimoottori olemassa; tiedot **⚠ ei tiedossa**, ei vielä kytketty (2018) | [blogi 2017-04-01] |

### 3.5 Säiliö, öljy ja putkisto

| Kohde | Arvo | Lähde |
|---|---|---|
| Säiliö | Flowfit 100 l, saumaton teräs (Flowfit Weldless Steel Tanks, tyyppi A/B/C **⚠ tarkista**), 50×50×5-kulmarautakannakkeilla kaariin | [blogi 2017-04-01], [datalehti Flowfit] |
| Öljymäärä | 80 l | [blogi 2017-07-04] |
| Öljyn tyyppi ja luokka | **⚠ ei tiedossa** | |
| Imulinjat | Suunnitelma 2017: 2 × 1" (konepumput) ja 1 × 3/4" (sähköpumppu), kussakin palloventtiili. **2026: P2:n ulosotto on 32 mm:n letkun kokoinen.** | [blogi 2017-04-10], [omistaja 2026-10-22] |
| Säiliön kannen komponentit | Virtauksensäätöventtiilit, paluusuodatin, täyttö- ja huohotinkorkki | [blogi 2017-04-10] |
| Paluusuodatin | Painemittarillinen; nykyisessä paikassa vaikea lukea | [blogi 2017-04-10] |
| Putkitus | Pitkät vedot 15×2-tarkkuusteräsputkella, muuten letkut | [blogi 2017-04-01] |
| Öljynjäähdytin | Ei kummassakaan piirissä. **Varalla Bowman EC100** (pronssiset päätykannet, ex-Masson-vaihteisto, putket kunnossa), suunniteltu yhteiseen paluulinjaan, ks. [oil-cooling.md](design/oil-cooling.md) | [omistaja 2026-10-22] |
| Päivätankki (polttoaine) | 150 l, hydraulisäiliön alla | [blogi 2017-04-19] |
| Päätoimittaja | SixTek (hydrauliikkapumppu.fi) | [blogi 2017-04-01] |

### 3.6 Valmistajan vaatimukset keulapotkurin hydrauliikalle [ohje Sleipner 2746 35 2025]

Asennusohjeen mukaan, kun käytössä ei ole Sleipnerin omaa hydraulijärjestelmää:

| Vaatimus | Vegan tilanne |
|---|---|
| Öljynsuodatin | Paluusuodatin on olemassa ✅ |
| **Öljynjäähdytin niin, että öljy pysyy alle 75 °C:n**; suositeltu käyttölämpötila **40–60 °C** | Suunnitteilla Bowman EC100, ks. [oil-cooling.md](design/oil-cooling.md) |
| Venttiilin virtaus- ja painerajat keulapotkurin rajoissa | VPR3 35 l/min ja VMP 250 bar; U11:n 100 %: 33,8 l/min ja 264 bar ✅ |
| **Iskuventtiilit (shock valve) 10–15 % valitun maksimipaineen yläpuolelle**, suojaamaan järjestelmää, jos potkurit jumittuvat | **Puuttuu.** BAV-713:ssa ei ole iskuventtiileitä. Lisättävä esim. A/B-linjojen ristiinkytketty iskuventtiililohko (CETOP 3 -välilevy). |
| Vuotolinja säiliöön (1/4" BSP, pakollinen) | Olemassa ✅ |
| Ohjaukseen Sleipnerin S-Link-järjestelmä | **Poikkeaa:** Vegalla oma ohjaus solenoidiventtiileillä. Voi vaikuttaa takuuseen; toiminnallisesti tavallinen ratkaisu. |

Moottorin suurinta sallittua painetta ei ilmoiteta suoraan. Asennus- ja käyttöohjeen taulukoissa
U-sarjan moottorit on kuitenkin kaikkialla rajattu **274–275 bariin**: SH240:n U8 ja U10 sekä isomman
SH320:n **U11** (sama moottori kuin Vegalla) saavuttavat suurimman työntövoimansa 274 barissa
[ohje Sleipner 2746 35 2025, ohje Sleipner 6572 6 2025]. U11:n yläraja on siis käytännössä noin
**275 bar** **⚠ vahvista Sleipneriltä**. 280 barin paineenrajoituksella moottorille jäisi linjahäviöiden
jälkeen noin 260–265 bar, eli rajan alle.

**Huolto ennen jokaista kautta** [ohje Sleipner 6572 6 2025]: tarkista vuodot keulapotkurin ympäriltä,
potkurien ja tunnelin kunto ja kiinnitys, puhdista kasvusto, maalaa potkurit ja vaihteisto
antifouling-maalilla (ei anodia, tiivisteitä eikä akselia), **vaihda anodi** joka kausi tai kun puolet
on kulunut, ja tarkista vaihteiston öljysäiliön (EP 90) öljynpinta. Vastakkain pyörivissä malleissa on
vasen- ja oikeakätinen potkuri.

## 4. Tunnetut ongelmat ja opit

1. **Hihnaveto ei kanna keulapotkurin täyttä tehoa.** Hihnat luistavat noin 160 barissa, kun
   keulapotkuri tarvitsee noin 15 kW 264 barilla. Tämä on pääsyy voimansiirron uusimiseen.
2. **Vakiotilavuuspumput vaihtelevalla kierrosluvulla.** Tuotto seuraa koneen kierroksia, ja ylimäärä
   kuristetaan säiliöön. Se tuhlaa tehoa ja lämmittää öljyä, eikä jäähdytintä ole.
3. **Ohjaussylinterin geometria.** Ei yllä paapuurin ääriasentoon, ja kiinnitysreikä on väljä.
4. **Ilmaus on hankalaa.** Ilmauspisteitä ei ole, ja sylinterin liitännät ovat sivuilla.
5. **Sähköinen varapumppu.** 2,5 kW:n moottori ottaa 24 V:lla noin 100 A tai enemmän, mitä 65 A:n
   laturi ei jaksa.
6. **Paluusuodattimen painemittari** on huonosti luettavassa paikassa.

## 5. Avoimet kysymykset

Ratkaistut:

- [x] Pumppujen veto: P1 etupään hihnoille, P2 vaihteiston PTO:lle (suunniteltu; nyt purettuna)
- [x] Advance 300 asennettu ja linjattu
- [x] Advance 300:n PTO: 1:1, ensiöakseli (pyörii vapaalla), ei omaa kytkintä
- [x] Advance 300:n PTO:n nimellisarvo: 0,044 kW/rpm (≈ 420 Nm)
- [x] PTO:n ulostulo: Ø48 mm:n kiila-akseli ilman laippaa; HRC 150 -joustokytkin runkoon kiinnitetylle kytkimelle ja pumpulle
- [x] Keulapotkurin paine: 250 barin luokka, ~90 % hyväksytty
- [x] Keulapotkurin letkut: 1/2", 300 bar, A ja B 8,5 m kumpikin
- [x] P2:n painelinja: 3/4" letku, 3–4 m
- [x] P2:n imulinja: 32 mm, noin 3 m, säiliön ulosotto samaa kokoa
- [x] Paluulinja CETOP:n T-liitännästä säiliöön: 3/4", < 0,5 m
- [x] Säiliön öljypinta noin 1 m P2:n imuaukon yläpuolella
- [x] Paineenrajoitusventtiili: Marchesini VMP 3/4", enintään 90 l/min, 350 bar, jousi 80–300 bar (todennäköisesti)

Avoimet:

- [ ] Koneen tyhjäkäynti: omistajan mukaan noin 700 rpm [omistaja 2026-10-22]; **vahvista mittaamalla** ennen pumpun ostoa
- [ ] P2:n koko: **51 cm³** hammaspyöräpumppu 700 rpm:n tyhjäkäynnillä (33,5 cm³:n Salami on liian pieni), tai käytetty Parker F1-061 -vinoakselipumppu (~60 cm³, tori.fi 100 €), ks. [p2-pump-options.md](design/p2-pump-options.md#ehdokas-parker-f1-061-käytettynä-torifi)
- [ ] PTO-kytkin: Borelli 30501/30502 (51 cm³:n pumppu vaatii noin 225 Nm, joten 185 Nm:n 30300 ei riitä); spline-sovite, vipuvoima, hinta
- [ ] HRC 150: nimellismomentti, suurin reikä ja napatyyppi 48 mm:lle ja kytkimen akselille (luettelo) — jälleenmyyjien mukaan 600 Nm, taper-holkki 2012 enintään 50 mm; napavaihtoehdot F1-61:lle ks. [p2-pump-options](design/p2-pump-options.md#veto-ptolta-suoraan-f1-61lle-bpv-vaihtoehto-ei-kytkintä)
- [ ] Valitun pumpun pienin sallittu imupaine (datalehti)
- [ ] Hydrauliöljyn tyyppi ja luokka (suositus **HV 32**, ks. [p2-pump-options.md](design/p2-pump-options.md#imupuoli-letkun-koko-ja-pituus-sekä-öljylaatu))
- [x] BAV-713: fluiconnecto BAV-IC3-713, 60 l/min, 350 bar
- [ ] BAV-713:n painehäviö ~34 l/min:llä (P→A, B→T): ei luettelossa; kysy toimittajalta tai mittaa
- [ ] BAV-713:n kelojen jännite (12 vai 24 VDC)
- [ ] Keulapotkurin iskuventtiilit (Sleipnerin vaatimus): A/B-iskuventtiililohko ja asetus
- [ ] U11-moottorin suurin sallittu paine: ohjeiden taulukoiden perusteella noin 275 bar; vahvista Sleipneriltä
- [ ] Paineenrajoitus: pysytäänkö 250 barissa, vai noustaanko 260–280 bariin (vaatii pumpun, venttiilien ja keulapotkurimoottorin arvot)
- [ ] Onko ankkurivinssi kytketty? Moottorin merkki, malli ja kierrostilavuus
- [ ] Onko sähköinen varapumppu kytketty?
- [ ] Ohjaussylinterin männän ja varren halkaisija ja iskunpituus, ohjausvarren pituus, peräsimen pinta-ala ja tyyppi
- [ ] Orbitrolin malli (avoin/suljettu keskiasento, kuormantakaisinkytkentä) ja mahdollinen autopilotti
- [x] Orbitroli: M+S HKUS 160/4, sisäänrakennettu paineenrajoitus
- [ ] Orbitrolin paineenrajoituksen asetusarvo
- [ ] VPR3:n ja RPF3:n koko (kierreliitäntä): VPR3 1/2" kestäisi vain 80 l/min
- [x] Koneen suurin kierrosluku noin 2400 rpm → P1 noin 2980 rpm (raja 3000 rpm), riittää niukasti
- [ ] Pienennetäänkö P1:n hihnavälitystä marginaalin saamiseksi (esim. 1:1,15)
- [x] Venttiilien tehtävät: Rexrothin 2/2-patruunaventtiili kytkee paineen CETOP-pohjalaatalle, BAV-713 ohjaa suuntaa [omistaja 2026-10-22]
- [x] CETOP-pohjalaatta: Flowfit NG6, 4-paikkainen, rinnankytketty, P/T 1/2", A/B 3/8"
- [ ] Onko 2/2-patruunaventtiili pohjalaatan paineenrajoitusventtiilin kavitetissa?
- [x] Pohjalaatan materiaali: teräs
- [ ] Pohjalaatan painearvo Flowfitilta (rajoittaako 280 barin vaihtoehtoa?)
- [ ] VMP:n jousialue (80–300 bar?) ja nykyinen asetus
- [ ] Öljynjäähdytys: Bowman EC100 paluulinjaan, merivesi koneen piiristä (ks. [oil-cooling.md](design/oil-cooling.md#avoimet-kysymykset))
- [ ] Muutokset vuoden 2021 jälkeen, joita blogi ei kata
