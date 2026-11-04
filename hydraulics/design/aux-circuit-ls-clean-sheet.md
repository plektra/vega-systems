# Apupiiri: Vickers PVH57 ja Danfoss PVG 32

> **Tila:** **päätetty 2026-10-27** (PVH57 + PVG 32); PVG 32 **ostettu 2026-11-02** (200 € + rahti
> 39,90 €) ja **saapui 2026-11-03**. Rungon koodit tulkittu 2026-11-03 Danfossin ohjeesta 520L0344
> ([Mitä koodit kertovat](#mitä-koodit-kertovat-2026-11-03)): pumppumoduuli 157B5111 sopii
> sellaisenaan, mutta **peruslohkoissa 157B6200 ei ole isku-/imuventtiilien paikkoja eikä
> LS A/B -rajoittimia**. **Kaikkien viiden lohkon karat liikkuvat käsin vapaasti ja palaavat
> jousella keskelle** [omistaja 2026-11-03]. Päivitetty 2026-11-03: ennen ostoa kirjoitettu
> vertailu, suositus ja hinta-arvio siirretty arkistoon
> ([archive/aux-circuit-pvg32-pre-purchase](archive/aux-circuit-pvg32-pre-purchase.md));
> arkistoidut varavaihtoehdot: [LS + on/off](archive/aux-circuit-ls-onoff.md) ja
> [FXDC + LS-purku](archive/p2-fxdc-ls-unloading.md). Pumppu: [p2-variable-pump](p2-variable-pump.md).
>
> PVG 32:n arvot ovat Danfossin teknisestä ohjeesta 520L0344, jäljempänä [datalehti PVG 32].
> Pätevän henkilön pitää tarkistaa kytkentä, säätöarvot ja erityisesti ankkurivinssin kuorman pito
> ja keulapotkurin painepiikkisuojaus ennen rakentamista.

## Selkokielinen yhteenveto

- Apupiiri on **kuormantunteva (LS) järjestelmä**: PVG 32:n LS-linja kertoo pumpulle suurimman
  kuorman paineen, ja PVH57 pitää paineen noin 20 bar sen yläpuolella ja tuottaa vain sen, mitä
  lohkot päästävät läpi.
- **Kun mitään ei käytetä, pumppu lepää itsestään** noin 20 barissa lähes ilman tuottoa. Ohitus-,
  purku- ja vapaakiertoventtiileitä ei tarvita.
- PVG 32 korvaa CETOP-pohjalaatan, BAV-713:n, VPR3:n, OD15:n ja VMP:n. Keulapotkuri saa
  **portaattoman** ohjauksen PVEH-lohkosta, vinssi ja pesuri ohjataan on/off-lohkoilla (PVEO,
  molempiin suuntiin, kun kara on kaksitoiminen).
- **Vielä ratkaistava:** keulapotkurin isku- ja imuventtiilit sekä vinssin paineraja (lohkoissa ei
  paikkoja, ks. [Mitä koodit kertovat](#mitä-koodit-kertovat-2026-11-03)), lohkojen karat
  (koodi 157N5531), puhdistus ja koestus, käsivivut ([pvg32-lever](pvg32-lever.md)) ja ohjaus
  ([bow-thruster-control](bow-thruster-control.md)).

## Kaavio

```
                                    ┌──────────────── Danfoss PVG 32, 5 lohkoa (157N5531) ─────────────────────────┐
PTO 1:1 ─ HRC150 ─ PVH57 (LS) ──P──►│ pumppumoduuli 157B5111: paineenrajoitin ~280 bar (varaventtiili), M-mittari   │
                    │   ▲           │ 1. keulapotkuri  A/B  – PVEH, moottorikara (A,B→T keskellä)                   │──► (isku/imu linjaan) ──► keula
                    │   └── LS ─────│ 2. ankkurivinssi A/B  – PVEO, moottorikara; jarruventtiili ja paineraja moott. │──► vinssi
                    │               │ 3. painepesuri   A    – PVEO, yksisuuntainen                                   │──► pesuri
                    │               │ 4.–5. varalla (PVEO), A/B tulpattu                                            │
                    │               └──────────────────────────── T ────────────────────────────────────────────────┘
                    │                                             │
                    │                          jäähdytin EC100 + termostaattiohitus
                    │                                             │
                    │                          paluusuodatin 10 µm, tukkeumaosoitin
                    │                                             ▼
                    └── kotelovuoto, oma letku öljypinnan alle ──► SÄILIÖ (huohotin 3 µm) ── 50 mm imu, palloventtiili ── PVH57
```

## Osat ja perustelut

### 1. Pumppu: PVH57, LS-säädin (V), suoraan PTO:lta

- Veto ja imu kuten nyt on päätetty: HRC 150 -joustokytkin kartioholkeilla (päätös 2026-10-27), oma kannake (SAE C -laippa, noin 36 kg
  **⚠ tarkista**), 50 mm:n imulinja, säiliö noin 1 m pumpun yläpuolella
  ([p2-variable-pump](p2-variable-pump.md#sopivuus-vegaan-laskelma)).
- Paineenrajoitin (painekompensaattori) 250 bar päätöksen 2026-10-21 mukaisesti.
- Tuotto 700 rpm:llä noin 38 l/min [laskelma: 57,4 cm³ × 700 rpm × 0,95], enemmän kuin
  keulapotkurin 33,8 l/min.
- Kotelovuoto omalla letkullaan säiliöön öljypinnan alle.

### 2. Venttiilit: yksi proportionaalinen LS-lohkoventtiili

Danfoss PVG 32 sähköisellä ohjauksella (PVE), ostettu käytettynä. Jokaisessa peruslohkossa
(157B6200) on oma painekompensaattori, joten jokainen kuorma saa karan mukaisen virtauksensa
paineesta riippumatta, kunhan pumpun tuotto riittää [datalehti PVG 32 s. 23].

| Lohko | Kuorma | Kara ja lisät |
|---|---|---|
| 1 | Keulapotkuri | Moottorikara: keskellä A ja B ovat yhteydessä säiliöön, joten potkuri pyörii vapaasti kuten BAV-713:lla. **Isku- ja imuventtiilit eivät mahdu peruslohkoon** (157B6200): kaksoisristivirtausventtiili linjaan tai lohkon vaihto, ks. [Mitä koodit kertovat](#mitä-koodit-kertovat-2026-11-03). Karan koko noin 40 l/min; nykyinen kara **⚠ tarkista** (157N5531). Portaaton työntö ilman lisäosia; **⚠ tarkista, sopiiko SH240 portaattomaan ohjaukseen**. |
| 2 | Ankkurivinssi | Moottorikara, portaaton nopeus. **Kuorman pito vinssin omalla jarrulla ja moottoriin asennetulla jarruventtiilillä, ei venttiilin karalla.** Moottori **Danfoss OMP 160 (151-0031)** [omistaja 2026-10-27], kierrostilavuus noin 155,7 cm³ **⚠ tarkista**. Teoreettinen momentti noin **25 Nm / 10 bar** (155,7 × Δp / 20π) ja nopeus noin **6,4 rpm / l/min** (esim. 20 l/min → noin 130 rpm) [laskelma, ei hyötysuhteita]. **OMP:n suurin paine-ero on selvästi alle järjestelmän 250 barin ⚠ tarkista datalehdestä**, joten vinssille tarvitaan oma paineraja: suositus moottorin päälle kaksoisristivirtausventtiili, koska peruslohkossa ei ole LS A/B -rajoittimia (2026-11-03). ([loads.yaml](../loads.yaml)) |
| 3 | Painepesuri | Yksisuuntainen, virtaus rajattu pesurimoottorin tarpeeseen (**⚠ ei tiedossa**, laitetta ei valittu) |
| 4–5 | Varalla | PVEO-lohkot; A/B tulpattu. Daavitti tai muu myöhemmin, tai lohkot poistetaan pinosta (PVAS 4 lohkolle 157B8004). Varalohkoa käytetään pumpun paineenrajoittimen säätöön ([p2-variable-pump](p2-variable-pump.md#säätö-käyttöönotossa-ilman-virtausmittaria)). |

- **Käsivivut:** jokaisessa lohkossa on vivun kanta (PVM), mutta vivut puuttuvat; niillä vinssiä ja
  potkuria voi käyttää, vaikka sähköohjaus pettäisi, ks. [pvg32-lever](pvg32-lever.md).
- **Ohjaus:** PVEH 157B4024 on jänniteohjattu (signaali 0,25–0,75 × syöttöjännite), PVEO:t
  157B4224 on/off-kytkimillä [datalehti PVG 32 s. 15–18]. Keulapotkurille joystick, vinssille
  kytkin; ESP32 PDM valvoo, tilat Signal K:hon, ks. [bow-thruster-control](bow-thruster-control.md).
- **Lukitus ohjelmassa:** pesuria voi käyttää vain, kun keulapotkuri ja vinssi ovat pois päältä.
  Tyhjäkäynnillä 38 l/min ei riitä kahdelle kuormalle yhtä aikaa, ja silloin suurimman paineen
  kuorma (keulapotkuri) jäisi vajaaksi [arvio].

### 3. Paluu, suodatus ja jäähdytys

- **Suodatus:** mäntäpumppu vaatii puhtausluokan 16/14/12 yli 210 barissa (17/15/13 140–210 barissa) [Eatonin PVH-luettelo s. 31,
  ks. [p2-variable-pump](p2-variable-pump.md#tekniset-tiedot)]. Nykyinen paluusuodatin
  OMTF112C10NA2 (10 µm, arviolta selluloosa nominaalinen) ei riitä sellaisenaan [omistaja 2026-10-26], ks.
  [p2-variable-pump](p2-variable-pump.md#riittääkö-nykyinen-paperisuodatin). Ehdotus:
  lasikuituinen paluusuodatin 10 µm (ehdokas OMTF171F10NA1, ks.
  [paluusuodattimen vaihto](p2-variable-pump.md#paluusuodattimen-vaihto-omtf171f10na1))
  tukkeumaosoittimella, säiliöön 3 µm:n huohotin, öljyn lisäys suodattimen kautta [arvio].
- **Jäähdytys:** EC100 (tai EC80) paluulinjaan termostaattiohituksella
  ([oil-cooling](oil-cooling.md)). Lämpökuorma pienenee selvästi: esim. pesuri jatkuvasti noin
  30 l/min × noin 25 bar säätövaraa ≈ 1,3 kW sekä moottorin häviöt [arvio]. Vertailuksi nykyisen
  suunnitelman ylimäärän kuristus keulapotkuria käytettäessä 1800 rpm:llä on noin 38 kW
  ([p2-pump-options](archive/p2-pump-options.md#käyttäytyminen-eri-kierroksilla-parker-f1-061)).
- **Kierroslukitusta ei tarvita lämmön takia,** koska pumppu ei tuota ylimäärää millään
  kierroksilla. Karat rajaavat virtauksen noin 40 l/minuun, joten pumpun 2400 rpm:n imuraja ei tule
  vastaan [arvio; **⚠ kysy Danfossilta** pienen iskun kierrosrajasta, ks. p2-variable-pump].

### 4. Mittaukset

Sama ajatus kuin [pressure-monitoring](pressure-monitoring.md):

- pumpun lähtöpaine ja LS-paine (niiden ero kertoo pumpun säätimen ja venttiilien kunnon)
- öljyn lämpötila (varoitus noin 65 °C, hälytys noin 70 °C), imupaine ja suodattimen tukkeuma.

## Vikatilat

| Vika | Mitä tapahtuu |
|---|---|
| Sähkökatko | Jouset palauttavat PVE-karat keskelle. Keulapotkuri pysähtyy ja pyörii vapaasti, vinssin jarru pitää, pumppu jää lepoon. Käsivivut toimivat edelleen. |
| Kara jumittuu auki | PVEH:n (lohko 1) vikavalvonta antaa vikasignaalin; PVEO:issa vikavalvontaa ei ole. Hätäpysäytys katkaisee PVE:iden virran, mutta mekaanisesti jumissa oleva kara palautetaan käsivivulla. Pumppumoduulin paineenrajoitin rajaa paineen. |
| Pumpun säädin jumittuu täydelle tuotolle | Tulomoduulin paineenrajoitin rajaa paineen; tilanne vastaa kiinteää pumppua (lämpöä), lämpötila-anturi hälyttää. |
| Kotelovuotolinja tukkeutuu | Akselitiiviste voi vaurioitua; siksi vuotolinja on oma letkunsa. |
| Vinssi kuormassa ja hydrauliikka menetetään | Jarruventtiili ja vinssin jarru pitävät kuorman. **Pätevä henkilö tarkistaa ennen rakentamista.** |

## Avoin mahdollisuus: paine yli 250 barin

PVG 32:n P-portin paineluokka on 350 bar (PVSI-päätylevyllä; PVS-päätylevyllä 300 bar)
[datalehti PVG 32 s. 12], ja PVH-luettelon mukaan LS-järjestelmän paineenrajoitin voi olla 280 bar.
Silloin keulapotkuri pääsisi lähemmäs täyttä työntöä nykyisen noin 85–89 %:n sijaan. Edellyttää,
että pumpun säätöalue sallii sen (C-jousi 70–250 bar, **⚠ tarkista Danfossilta**), että
päätylevy on PVSI tai pumppumoduulin 280 bar jää varaventtiiliksi riittävän kauas, ja se muuttaisi
250 barin päätöstä (2026-10-21). **Omistajien päätettävä**; ei suositella ennen ensimmäistä kautta.

## Ostettu venttiili: Danfoss PVG 32, 5 lohkoa (tori.fi)

> Lisätty 2026-10-26. Tiedot luettu ilmoituksen kuvista ja Danfossin teknisestä ohjeesta
> *PVG 32 Proportional Valve Group, Technical Information 520L0344*
> ([PDF](https://imdl.gatech.edu/jfrankel/docs/Sauer-Danfoss/520L0344_PVG32.pdf)), jäljempänä
> [datalehti PVG 32]. **Päätetty 2026-10-27; ostettu 2026-11-02 (200 € + rahti 39,90 €); saapui 2026-11-03.**

Ilmoitus: <https://www.tori.fi/recommerce/forsale/item/46493298>, **400 €, tee tarjous** (tarkistettu
2026-10-26). Ilmoituksen teksti: *"Danfors pvg 32 venttiilipöytä. Tienhoitoautosta purettu. Karojen
ja kelojen tyypistä ei tarkempaa tietoa."*

### Mitä venttiilistä tiedetään

Kuvista luetut arvot on merkitty *kuvasta*; merkinnät ovat likaisia ja osin epäselviä.

| Kohde | Tieto | Lähde |
|---|---|---|
| Tyyppi | *Danfoss Proportional Valve Type PVG 32* (valukilpi) | kuvasta |
| Lohkot | **5 työlohkoa**, pumppumoduuli ja päätylevy | kuvasta |
| Kokoonpanokoodi | **157N5531** pumppumoduulin valukilven No.-kentässä [omistaja 2026-11-03, luettu venttiilistä]. Aiempi lukema ilmoituksen kuvista oli 157N553(8 tai B) [omistaja 2026-10-26]. **Koko venttiiliryhmän numero (PVG No.)**, jonka Danfoss antaa tilatulle kokoonpanolle uusintatilauksia varten [datalehti PVG 32 s. 66]. Koodista selviävät karat ja muut osat Danfossilta tai jälleenmyyjältä; julkisista ohjeista sitä ei voi purkaa | [omistaja 2026-11-03] |
| Ohjausyksiköt (PVE) | Lohko 1: **157B4024 = PVEH 24 V** (proportionaalinen, vikavalvonta); **neljä muuta: 157B4224 = PVEO 24 V** (on/off), vahvistettu lähikuvista 2026-11-03 [omistaja 2026-11-03]. Kaikki vanhaa sarjaa 0. | kuvasta, [Kramp: PVE cross reference](https://documents.kramp.com/PVE_cross_reference_EN.pdf) |
| Käsiohjaus | Toisella puolella käsivipujen kannat ilman vipuja **⚠ tarkista** | kuvasta |
| Karat | **⚠ ei tiedossa**; selviää kokoonpanokoodista 157N5531 Danfossilta tai karan päästä, jos lohko avataan | – |
| Pumppumoduuli | **157B5111: suljettu keskiasento, sisäinen pilottiöljy PVE:ille, P = G 3/4** (rungon leima 511?, ks. [Mitä koodit kertovat](#mitä-koodit-kertovat-2026-11-03)); sopii PVH57:lle. Myyjän mukaan autossa kytkettynä **säätötilavuuspumppuun** [myyjä 2026-10-27], mikä tukee tulkintaa. Kuvassa kyljessä liitin, todennäköisesti käytössä ollut LS-portti; ylhäällä P- ja T-portit, M-portti ja tulpattu lisäportti; etupinnalla todennäköisesti paineenrajoittimen säätöruuvi | [myyjä 2026-10-27], kuvasta |
| Paino | **noin 23–24 kg** [laskelma, päivitetty 2026-11-03]: PVP 3,0 kg + 5 × PVB 3,1 kg + 4 × PVEO 0,6 kg + PVEH 1,0 kg + päätylevy 0,5 kg (PVS) tai 1,7 kg (PVSI) + PVAS 0,45 kg, lisäksi vipujen kannat **⚠ arvio** | [datalehti PVG 32 s. 64–65] |
| Kunto | likainen, **osa porteista auki ilman tulppia** → puhdistus ja koestus välttämättömiä | kuvasta |
| Karojen käsitarkistus | **Kaikkien viiden lohkon karat liikkuvat ongelmitta molempiin suuntiin**, kun niitä liikutetaan lenkkiavaimella vivun kannasta [omistaja 2026-11-03]. Karat eivät ole jumissa eivätkä tunnu ruostuneilta, joten pinoa ei tarvitse avata karojen takia. **Karat palaavat jousella keskelle molemmista suunnista**, kun vipu päästetään [omistaja 2026-11-03], joten keskitysjouset toimivat: sähkökatkossa tai hätäseisissä karat palaavat keskelle, kuten vikatilojen kuvauksessa oletetaan. Käsiliike ei kerro, onko kara kaksi- vai yksitoiminen (karan isku on mekaanisesti sama); se selviää koodista 157N5531 tai painekokeessa | [omistaja 2026-11-03] |
| Toiminta purettaessa | **Ei kokeiltu:** auton keulapumpun kardaani oli rikki, kun auto tuli purkuun, joten venttiiliä ei voitu ajaa. Toimintakunto ja vuodot **⚠ ei tiedossa** | [myyjä 2026-10-27] |
| Käyttö autossa | Hiekoittimessa oli nopeudensäätö → todennäköisesti se oli ainoa portaaton toiminto ja PVEH-lohko, muut on/off. Sopii kuvista luettuun (1 × PVEH, 4 × PVEO) | [myyjä 2026-10-27] |
| Pumppumoduulin paineasetus | Valukilven **PVP-kenttä: 28? bar**, viimeinen numero kulunut → todennäköisesti **280 bar**, eli sama kuin tässä suunniteltu noin 280 barin asetus. Varmistetaan koestuksessa | [omistaja 2026-11-03, kuvasta] |
| Säilytys | sisällä purkamisen jälkeen; irrotuksen kesto **⚠ ei tiedossa** | [myyjä 2026-10-27] |

### Vastaanotto 2026-11-03: rungon merkinnät

Venttiili saapui 2026-11-03 [omistaja 2026-11-03]. Merkinnät luettiin omistajan valokuvista;
osa leimoista on kuluneita, joten epäselvät merkit on merkitty `?`.

| Kohta | Merkintä | Tulkinta | Kuva |
|---|---|---|---|
| Valukilpi | *PROPORTIONAL VALVE TYPE PVG 32*; No. **157N5531**, Date **161** (valussa tekstit *No.* ja *Date*, leimat niiden vieressä), PVP **28? BAR** | No. on kokoonpanokoodi (ks. yllä), Date on valmistusajan koodi [omistaja 2026-11-03]; pumppumoduulin paineenrajoitin todennäköisesti **280 bar** **⚠ tarkista koestuksessa** | [kuva](../img/pvg32-nameplate.jpg) |
| PVEH | **24 VDC, 157B4024, 091**; Hirschmann GDM -liitin (kannessa *14 A GDM*) | PVEH 24 V, kuten aiemmin luettu | [kuva](../img/pvg32-pveh-157b4024.jpg), [liitin](../img/pvg32-pveh-connector.jpg) |
| PVEO × 4 | **24 VDC, 157B4224**, alarivit **101, 091, 111, 111**; Hirschmann GDM -liittimet (kannessa *12 B GDM*) | kaikki neljä PVEO 24 V. **Yhden PVEO:n (101) pyöreä kupu kotelon keskellä on rikki** (muissa ehjä): kotelon tiiviys **⚠ tarkista**, ettei vettä tai likaa pääse sisään | [kuva](../img/pvg32-pveo-row.jpg) |
| PVE-liittimet | jokaisessa viidessä PVE:ssä oma liitin johtoineen | liittimiä ei tarvitse hankkia (procurement 4.8) | samat |
| Peruslohkot (PVB) | pistemerkintä **A 6200 / 161**, sama ainakin kolmessa lohkossa | **157B6200: paineenkompensaattori, A/B = G 1/2, ei isku-/imuventtiilien paikkoja, ei LS A/B -rajoittimia** [datalehti PVG 32 s. 23–24, 64]. Kahden muun lohkon leima **⚠ tarkista** | [kuva](../img/pvg32-pvb-stamps.jpg) |
| Pumppumoduuli (PVP)? | pistemerkintä **511? / 161** (luettu 5114 tai 5111) isossa kuusiokolotulpallisessa päädyssä | **157B5111** [päättely]: ohjeen sarjassa 157B511x on vain 5110–5113, joten 5114 ei ole mahdollinen. Suljettu keskiasento, pilottiöljy PVE:ille, P = G 3/4, ei PVPX-paikkaa [datalehti PVG 32 s. 20, 65]. Viimeinen numero on kulunut; 5110 (avoin keskiasento) erotetaan koestuksessa: suljetun keskiasennon moduulissa pumpun virta ei kulje tankkiin karojen ollessa keskellä | [kuva](../img/pvg32-pvp-stamp.jpg) |
| Pääty | valumerkinnät **P** ja **LS**; LS-kohdan vieressä kierreliitin | Kilpi (PVG 32, No., Date, PVP) on pumppumoduulin päädyssä. Jos P/LS-pääty on pinon **toisessa** päässä, se on päätylevy: ohut PVS (0,5 kg, enintään 300 bar) tai paksu PVSI (1,7 kg, enintään 350 bar) [datalehti PVG 32 s. 28, 64]. Kumpikin riittää 280 barin asetukselle. **⚠ tarkista**, kummassa päässä | [kuva](../img/pvg32-end-p-ls.jpg) |
| Työporttien puoli (yläkuva) | Jokaisessa viidessä lohkossa näkyy vain **A- ja B-portti** (kaksi riviä), ei muita tulppia tai venttiilejä. Porttien käyttö autossa (vasemmalta, pumppumoduuli oikealla isojen kulmaliittimien päässä): lohko vasemmalla A ja B nipat; 2. ja 3. A nippa, **B tulpattu kuusiokolotulpalla**; 4. ja 5. A kulmaliitin, B nippa. PVE-liittimistä vasemmanpuoleinen on muista poikkeava harmaa [omistaja 2026-11-03, kuvasta] | Muiden tulppien puuttuminen sopii tulkintaan 157B6200 (ei PVLP-paikkoja) [arvio; PVLP-paikan sijaintia ei ole tarkistettu ohjeen mittakuvasta]. **Tulpatut B-portit lohkoissa 2–3 viittaavat siihen, että niissä voi olla yksitoimiset karat** [arvio]: vinssille kannattaa valita lohko, jonka molemmat portit olivat autossa käytössä. **Harmaa liitin kuuluu PVEH:lle** (157B4024 kilvessä) [omistaja 2026-11-04], joten **PVEH on pumppumoduulista kauimmaisessa lohkossa** (5. pumppumoduulista lukien), ei ensimmäisessä. Dokumenttien "lohko 1 = keulapotkuri" tarkoittaa siis PVEH-lohkoa; numerointi tarkistetaan kytkentäkuviin | [kuva](../img/pvg32-top-ports.jpg) |

- **"161" toistuu** kilvessä, pumppumoduulissa ja peruslohkoissa, ja PVE:issä on vastaavat
  kolminumeroiset merkinnät (091–111). Kilvessä 161 on *Date*-kentässä [omistaja 2026-11-03], joten ne ovat valmistusajan koodeja. Siitä päätellen
  PVE:t on tehty ennen kokoonpanoa ja venttiili on koottu kerralla eikä lohkoja ole vaihdettu
  myöhemmin [arvio; päivämäärämuotoa ei ole tarkistettu Danfossilta].
- **Todennäköinen muoto on viikko + vuoden viimeinen numero** [päättely]: PVE:t viikoilla 09–11 ja
  kokoonpano viikolla 16 samana vuonna, mikä sopii järjestykseen. Vuosi on 1991 tai 2001: vuoden 2001
  ohjeessa 520L0344 24 V:n PVEH on jo 157B4028 ja PVEO 157B4228 [s. 26], joten tämän venttiilin
  157B4024 ja 157B4224 ovat vanhempia koodeja, mikä viittaa vuoteen **1991** **⚠ tarkista**. Venttiili
  on siis 25–35 vuotta vanha: **tiivisteet (PVAS ja PVE:iden O-renkaat) kannattaa vaihtaa**, jos pino
  avataan.
- **Kilven paineasetus sopii suunnitelmaan:** PVP-moduulin noin 280 bar on noin 30 bar PVH57:n
  250 barin yläpuolella, joten asetusta ei todennäköisesti tarvitse muuttaa [laskelma; kilven luku
  osin kulunut].

### Mitä koodit kertovat (2026-11-03)

Rungon leimat tulkittiin Danfossin ohjeesta 520L0344 (luettu tekstinä 2026-11-03)
[datalehti PVG 32 s. 20–29, 64–66].

| Moduuli | Koodi | Mitä se on | Mitä se tarkoittaa Vegalle |
|---|---|---|---|
| Koko venttiili | 157N5531 | Danfossin venttiiliryhmälle antama numero (PVG No.) | Karat ja kokoonpano selviävät vain Danfossilta tai jälleenmyyjältä |
| Pumppumoduuli (PVP) | 157B5111 (leima 511?) | suljettu keskiasento säätötilavuuspumpulle, sisäinen pilottiöljy PVE:ille, P = G 3/4, T = G 3/4, LS ja M = G 1/4; ei PVPX-paikkaa | **Sopii PVH57:lle sellaisenaan.** Pilottiöljyä varten ei tarvita lisäosia. P-porttiin G 3/4 -sovite. PVPX ei ole mahdollinen ilman moduulin vaihtoa (157B5113), eikä sitä tarvita |
| Peruslohkot (PVB) | 157B6200 (leima A 6200, ainakin 3 lohkoa) | paineenkompensaattori (virta ei riipu kuormasta), A/B = G 1/2; **ei isku-/imuventtiilien paikkoja, ei LS A/B -rajoittimia** | Portaaton ohjaus toimii. **PVLP-venttiileitä ei voi lisätä, eikä vinssin painerajaa voi tehdä lohkossa** (ks. alla) |
| PVEH | 157B4024 | 24 V proportionaalinen, sarja 0 | vanhempi koodi kuin vuoden 2001 ohjeen 157B4028 |
| PVEO × 4 | 157B4224 | 24 V on/off, sarja 0 | vanhempi koodi kuin ohjeen 157B4228 |

**Mitä tämä muuttaa suunnitelmassa** (korjaa aiemmat suositukset, jotka olettivat lohkoissa olevan
paikat):

- **Keulapotkurin isku- ja imuventtiilit eivät mahdu lohkoon 1.** Vaihtoehdot:
  1. Kaksoisristivirtausventtiili (dual cross-over relief) imuventtiileillä letkulinjaan tai
     moottorin päälle. Ei muutoksia venttiilipöytään. **Suositus [arvio]**, koska se on luultavasti
     halvin ja sama ratkaisu käy vinssille. Hinta **⚠ ei tiedossa**. Venttiilin runko pitää olla
     **terästä ja vähintään noin 300–350 barin** luokkaa ja virran noin 35–40 l/min: Rexroth VSDI-30
     **ei kelpaa** (alumiinirunko, käyttöpaine enintään 210 bar, enintään 30 l/min, vaikka jousi
     35 antaa 100–350 bar) [datalehti Rexroth RE 18308-15]. **Paras ehdokas (2026-11-04): Marchesini VAU 1/2" (V0450)**: G 1/2, enintään 70 l/min, enintään 350 bar, **runko sinkitty teräs**, jousi 80–300 bar (50 bar/kierros) tai 50–250 bar; kaksi ristiinkytkettyä paineenrajoitinta, joiden purkuöljy menee toiseen linjaan; asennus lähelle moottoria [datalehti Marchesini VAU 5.1]. Marchesinia on Vegalla ennestään (VMP, VPR3, RPF3). Imuventtiilitön perusmalli; myös imuventtiilillinen VAUAC on olemassa (jousivaihtoehdot **⚠ tarkista**). Muita ehdokkaita (2026-11-04, **⚠ tarkista**
     datalehdestä ennen tilausta): Oudshoorn DCROMP/R40 (1/2" BSPP, 40 l/min, teräsrunko S40
     400 bar, jousi enintään 350 bar; laipoitettavissa myös OMP/OMR-moottoriin, sopisi siis vinssin
     OMP 160:lle) ja VBDC teräsrungolla (350 bar, 35 l/min) [hakutulokset].
  2. Lohkon 1 peruslohkon vaihto malliin **157B6230** (sama kuin 6200, mutta paikat PVLP:ille) ja
     2 × PVLP. Kara ja PVEH siirretään vanhasta lohkosta. Vaatii pinon avaamisen ja PVAS-sarjan.
     Hinta **⚠ ei tiedossa**.
- **Vinssin (OMP 160) painerajaa ei voi tehdä LS A/B -rajoittimella nykyisessä lohkossa.** Aiempi
  ensisijainen suositus ei toteudu ilman lohkon vaihtoa. Vaihtoehdot:
  1. **Moottorin päälle kaksoisristivirtausventtiili** (aiempi varavaihtoehto), asetettuna OMP 160:n
     sallitun paine-eron mukaan. Jumitilanteessa koko virta kulkee venttiilin yli ja öljy lämpenee,
     mikä on lyhytaikaisesti hyväksyttävää. **Suositus [arvio]**, koska venttiilipöytään ei tarvita
     muutoksia.
  2. Vinssilohkon peruslohkon vaihto malliin **157B6203** (LS A/B -rajoittimet) tai **157B6233**
     (rajoittimet ja PVLP-paikat). Teknisesti parempi (ei lämpöä jumitilanteessa), mutta vaatii
     käytetyn tai uuden peruslohkon ja pinon avaamisen. Hinta **⚠ ei tiedossa**.
- PVLP ei kelpaa painerajaksi: Danfossin mukaan se on vain painepiikkejä varten, ja pysyvään
  rajoitukseen käytetään LS A/B -rajoittimella varustettua peruslohkoa [datalehti PVG 32 s. 38].
- **Pätevän henkilön pitää hyväksyä** keulapotkurin ja vinssin painerajat ja venttiilien asetukset
  ennen käyttöä; vinssi ja keulapotkuri ovat turvallisuuskriittisiä.

### PVG 32:n rakenne: mitä voi vaihtaa

- **Lohkoja voi vaihtaa, poistaa ja lisätä.** Pino pysyy koossa kiristyspulteilla; pultit ja
  tiivisteet ostetaan sarjana lohkojen määrän mukaan (PVAS: 4 lohkoa 157B8004, 5 lohkoa 157B8005)
  [datalehti PVG 32 s. 28–29].
- **Karat ovat vaihdettavia** [s. 3], ja **samat karat käyvät on/off- ja proportionaaliohjaukseen**:
  karataulukot ovat yhteiset kaikille sähkö- ja käsiohjauksille; omat karat on vain hydrauliselle
  ohjaukselle, mekaaniselle lukitukselle ja kellunta-asennolle [s. 56–62].
- **On/off muutetaan proportionaaliseksi vaihtamalla PVE:** PVEO → PVEM (keskitaso) tai PVEH
  (tarkka, vikavalvonta). Kara pysyy samana. Uusi PVEH 11166817 noin 670 € + ALV
  ([hydraulic-stock](https://www.hydraulic-stock.com/Product/hydraulic-valves-and-distributors/spare-parts-of-distributors-danfoss/electrohydraulic-actuators/PVG32-Elektrinis-aktuatorius-PVEH-11-32-V-DIN-Danfoss-11166817-PVEH32-S7-1x4DIN-H), 2026-10-25).
  **⚠ Tarkista,** sopiiko sarjan 4/7 PVE sarjan 0 lohkoon (liitin ja signaali).
- Vegalle riittää yksi proportionaalinen lohko: **keulapotkuri PVEH-lohkoon**, vinssi ja pesuri
  PVEO-lohkoihin.

### Mitä keulapotkuri tarvitsee PVH57:n ja tämän venttiilin lisäksi

Pumppumoduuli on rungon leiman perusteella **157B5111**: suljettu keskiasento, sisäinen
pilottiöljy PVE:ille, P = G 3/4 [datalehti PVG 32 s. 20; päivitetty 2026-11-03]. Se sopii PVH57:lle
sellaisenaan. Myyjän tieto säätötilavuuspumpusta [myyjä 2026-10-27] tukee tätä. Varmistetaan koestuksessa.

```
PTO ─ HRC150 ─ PVH57 ──P──► PVG 32 [pumppumoduuli ─ lohko 1 (PVEH): keulapotkuri ─ lohkot 2–5 ─ päätylevy]
                │   ▲                                  │ A/B 1/2" (olemassa)
                │   └──── LS 1/4" ─────────────────────┘ └──► keulapotkuri
                └─ kotelovuoto ─► säiliö         T ─► jäähdytin ─► paluusuodatin ─► säiliö
```

Venttiilin kuormantunto korvaa PVH57-selvityksen apuventtiilit: **FXDC, LS-linjan 2/2,
Ø0,8 mm:n kuristin ja VMP jäävät pois**, samoin CETOP-pohjalaatta, BAV-713, VPR3 ja OD15.

**Pumpun puoli** (sama kuin muissa PVH57-reiteissä, ks. [p2-variable-pump](p2-variable-pump.md#asennusjärjestys)):
HRC 150 ja Taper Lock 2012 -holkit 48 mm / 1 1/4" (päätös 2026-10-27), kannake SAE C -laipalle, 50 mm:n imu, kotelovuotoletku.

**Venttiilin liitännät:**

| Osa | Huom. |
|---|---|
| Painelinja pumpulta P-porttiin | **P-portti G 3/4** (157B5111, 16 mm syvä) [s. 20] |
| **LS-letku 1/4"** venttiilin LS-liitännästä (G 1/4) pumpun LS-porttiin | korvaa kuristimen ja 2/2:n |
| Sovitteet A/B-portit (G 1/2) → nykyiset 1/2":n keulapotkuriletkut | letkut valmiina |
| Paluulinja T-portista (G 3/4) jäähdyttimelle ja suodattimelle | T-portin suurin paine 25 bar staattinen / 40 bar dynaaminen [s. 12] |
| Painemittari venttiilin M-liitäntään (G 1/4) | mittarin 2G1 paikka |
| Kiinnitys konehuoneeseen | teline tai levy |

**Venttiilin sisällä tarkistettavat:**

| Osa | Toimenpide |
|---|---|
| Kara keulapotkurin lohkossa | Tarvitaan **40 l/min, avoin keskiasento** (A ja B kuristettuina säiliöön): 157B7102 (lohko ilman LS A/B -vaihtoventtiiliä) tai 157B7122 / 157B7132 (vaihtoventtiilin kanssa) [s. 56]. Suljettu keskiasento (esim. 157B7002) ei käy, koska se lukitsisi moottorin. Hinta noin 116 SGD + verot ([PV Global](https://www.pvglobal.com.sg/pvg32/133-157b7002-pvbs32-main-spool.html), 2026-10-25). |
| Pumppumoduulin paineenrajoitin | sisäänrakennettu; asetetaan **noin 30 bar pumpun asetuksen yläpuolelle**, eli noin 280 bariin [s. 5]. Korvaa VMP:n. |
| Isku- ja imuventtiilit keulapotkurin A/B-linjoihin | Sleipner vaatii iskuventtiilit 10–15 % maksimipaineen yläpuolelle, ja imuventtiili estää kavitaation potkurin pyöriessä vapaasti. **Peruslohkossa 157B6200 ei ole PVLP-paikkoja** [s. 23, päivitetty 2026-11-03], joten suositus on letkulinjaan tai moottorin päälle asennettava kaksoisristivirtausventtiili imuventtiileillä; vaihtoehtona peruslohkon vaihto malliin 157B6230 ja PVLP:t (esim. 157B2280) ([Mitä koodit kertovat](#mitä-koodit-kertovat-2026-11-03)). **⚠ hinta ei tiedossa**. Pätevä henkilö arvioi. |
| Vinssilohkon paineraja (OMP 160) | **Päivitys 2026-11-03: peruslohkot ovat 157B6200 ilman LS A/B -rajoittimia ja PVLP-paikkoja, joten suositus on nyt moottorin päälle asennettava kaksoisristivirtausventtiili tai peruslohkon vaihto malliin 157B6203/6233** ([Mitä koodit kertovat](#mitä-koodit-kertovat-2026-11-03)). Alkuperäinen suositus [arvio]: LS A/B -paineenrajoitus vinssin peruslohkossa (PVB). Rajoitin katkaisee lohkon LS-signaalin säädettyyn paineeseen, joten pumppu nostaa painetta vinssille vain siihen asti eikä täysi virta kulje paineenrajoituksen yli: ei lämpöä, vaikka vinssi jumittuu. Asetetaan OMP 160:n suurimman jatkuvan paine-eron mukaan (**⚠ datalehdestä**). Vaatii peruslohkon, jossa on LS A/B -rajoittimet (**⚠ tarkista** lohkon 2 koodista ja datalehden 520L0344 vaihtoehdoista); muuten käytetty peruslohko vaihdetaan. **Lisäksi PVLP-iskuventtiilit** lohkon A/B-portteihin, jos paikat ovat: ne leikkaavat painepiikit (ketjun nykäys, pysäytys). **Varavaihtoehto:** moottorin päälle asennettava kaksoisristivirtausventtiili (dual cross-over relief), jonka läpi koko virta kulkee jumitilanteessa (lyhytaikaisesti hyväksyttävä). Jarruventtiili ei korvaa painerajaa. |
| Pumpun paine-ero (PVH57 noin 20 bar) | riittää luultavasti lohkojen kompensaattoreille ja PVE:iden pilottiöljylle **⚠ tarkista Danfossilta** |
| Tiivisteet ja puhdistus | PVAS 157B8005, jos venttiili avataan; puhdistus ja koestus hydrauliikkaliikkeessä |

**Sähkö ja ohjaus** [datalehti PVG 32 s. 15–18]:

| Asia | Arvo tai ratkaisu |
|---|---|
| PVE:n käyttöjännite | 22–30 V (24 V käy) |
| PVEH:n ohjaussignaali | **suhteellinen käyttöjännitteeseen:** keskiasento 0,5 × U, täysi 0,25 × U tai 0,75 × U |
| Ohjain | **potentiometrijoystick samasta syötöstä** antaa signaalin suoraan ilman elektroniikkaa; vaihtoehtona ESP32, jonka lähtö seuraa syöttöjännitettä. Selvitys ja suositus: [bow-thruster-control.md](bow-thruster-control.md) |
| Liitin | Hirschmann DIN, 4-napainen (syöttö, signaali, maa, vikasignaali) |
| Vikavalvonta | PVEH pysäyttää karan, jos signaali on alueen 15–85 % ulkopuolella (myös johdon katketessa); vikasignaali Signal K:hon hälytykseksi |
| Pääkytkin / hätäseis | rele katkaisee PVE:iden syötön → jouset palauttavat karat keskelle |
| (ei käytössä) PVPX 24 V, 157B4238 | sähköinen LS-purku; **pumppumoduulissa 157B5111 ei ole PVPX-paikkaa** [s. 20], joten se vaatisi moduulin 157B5113. Ei tarvita: sähkökatkossa karat palaavat keskelle ja LS-signaali purkautuu |

**Käyttöönotto** (pätevä henkilö hyväksyy arvot):

1. Venttiili puhdistetaan ja kara tarkistetaan; isku- ja imuventtiilit (kaksoisristivirtausventtiili tai vaihdettu peruslohko) asennetaan.
2. Huuhtelu ja täyttö HVLP 32:lla; pumpun kotelo täytetään ennen käynnistystä.
3. Valmiustila (noin 20 bar) venttiilin painemittarista.
4. Pumpun paineenrajoitin 120 → 250 bar, venttiilin paineenrajoitin noin 280 bar.
5. Keulapotkuri ensin pienellä ohjauksella, sitten täydellä: täydellä mittarin pitäisi näyttää lähes 250 bar.

**Vikatilat:** sähkökatkossa tai hätäseisissä karat palaavat jousilla keskelle ja potkuri pysähtyy
pyörien vapaasti avoimen keskiasennon kautta. PVEH:n vika pysäyttää lohkon ja antaa hälytyksen.
Pätevän henkilön pitää tarkistaa paineasetukset, PVLP-tarve ja ohjauksen kytkentä ennen käyttöä.

### Puhdistus ja koestus

> Lisätty 2026-10-27. Yleinen hydrauliikkaventtiilien kunnostustapa [arvio], ei Danfossin
> huolto-ohjeesta. Kiristysmomentit ja purkujärjestys tarkistetaan Danfossin huolto-ohjeesta
> **⚠ ei vielä luettu**. Tavoite on PVH57:n puhtausluokka 16/14/12, joten sisälle ei saa päästää likaa.

**Järjestys: ulkopuoli → tarkistus purkamatta → purku vain tarvittaessa → koestus.**

1. **Ulkopuoli ennen avaamista**
   - Tulppaa kaikki portit (muovi- tai terästulpat; teippi vain hätävarana). Osa porteista on nyt auki.
   - Irrota PVE:t (muutama ruuvi lohkoa kohden), merkitse lohkot ja suojaa liittimet.
   - Pese harjalla ja liuotinpesuaineella tai petrolilla, huuhtele varovasti ja kuivaa paineilmalla
     heti. **Ei painepesuria** (vesi ja lika karan tiivisteiden ohi). Pinoa ei liuoteta, koska
     nitriilitiivisteet turpoavat voimakkaista liuottimista.
2. **Tarkistus purkamatta** (päivitetty 2026-11-02)
   - **Ensin käsivivun kannasta, mitään avaamatta:** kanta on kiinni karassa, joten karaa voi
     liikuttaa vivulla tai lyhyellä tangolla. PVE:t voivat olla paikallaan; ilman painetta ja sähköä
     ne eivät estä käsiliikettä, mutta liike voi tuntua hieman jäykältä [arvio PVG-sarjan rakenteesta]
     **⚠ tarkista huolto-ohjeesta**. Portit tulpattuina ja venttiili ulkoa pestynä.
   - Vivuksi kelpaa koestukseen ilman painetta pultti tai kierretanko kannan kiinnitykseen, tai
     3D-tulostettu vipu (PETG, kierre lämpöholkilla tai läpipultilla). Kierre todennäköisesti M8
     **⚠ mittaa**; mitat ja valmisosat: [pvg32-lever](pvg32-lever.md). Käytössä paineen alla käytetään
     metallista vipua.
   - Jos jostain lohkosta puuttuu käsivivun kanta, irrotetaan vain sen lohkon PVE (muutama ruuvi) ja
     liikutetaan karaa sen päästä. Lohkopino pysyy kiinni, joten tiivistesarjaa ei tarvita; PVE:n alla
     oleva O-rengas tarkistetaan. Työ tehdään puhtaassa paikassa.
   - Tulkinta: kevyt liike ja paluu keskelle → koestukseen; jäykkä mutta palaa → likaa tai ruostetta,
     huuhtelu tai lohkon purku; ei palaa tai jumissa → lohko puretaan (kohta 3).
   - Portit taskulampulla: ruskea vesijäämä tai ruoste → venttiili puretaan.
   - Pumppumoduulin paineenrajoittimen asetukseen ei kosketa; jos se irrotetaan, kierrokset lasketaan.
3. **Purku vain tarvittaessa**
   - Lohkojen järjestys ja suunta merkitään (1–5). Pino aukeaa kiristyspulteista; tiivistesarja
     **PVAS 157B8005** (5 lohkoa) vaihdetaan aina, kun pino avataan [datalehti PVG 32 s. 28–29].
   - Kara pidetään oman lohkonsa kanssa: karat ovat vaihdettavia [s. 3], mutta kuluneet kara ja
     pesä ovat sovittuneet toisiinsa. Kevyt pintaruoste kiillotetaan hienolla hiomakankaalla
     (yli 1000) öljyn kanssa; syvät naarmut tai kuopat → uusi kara.
   - Osat pestään puhtaassa petrolissa, kuivataan nukkaamattomalla liinalla ja paineilmalla ja
     voidellaan heti HVLP 32:lla.
   - Kiristyspulttien ja PVE-ruuvien momentit Danfossin huolto-ohjeesta **⚠ ei tiedossa**; liian
     kova kiristys voi jumittaa karat.
4. **Koestus**
   - Paras: hydrauliikkakorjaamon koepenkki (vuodot, karat, paineenrajoittimen asetus), hinta
     **⚠ ei tiedossa**.
   - Oma: PVEH:n toiminta 24 V:lla ja potentiometrilla ilman painetta (kara liikkuu, vikasignaali);
     ensimmäinen ajo matalalla paineella ja paine nostetaan vaiheittain.
   - Piiri huuhdellaan ennen käyttöönottoa; paluusuodatin vaihdetaan ensimmäisten käyttötuntien jälkeen.

**Kustannussuositus:** ulkopesu ja karojen käsitarkistus ensin. Jos karat liikkuvat vapaasti ja
portit ovat sisältä puhtaat, suoraan koestukseen ilman purkua; puretaan vain ongelmalohkot.

**Päivitys 2026-11-03:** Käsitarkistus tehty: kaikki viisi karaa liikkuvat vapaasti molempiin
suuntiin ja palaavat jousella keskelle [omistaja 2026-11-03]. Jos portit ovat sisältä puhtaat,
venttiili menee koestukseen purkamatta, eikä tiivistesarjaa PVAS 157B8005 tarvita nyt.

### Hinta

Ostettu **200 € + rahti 39,90 €** (ilmoitushinta 400 €) [omistaja 2026-11-02]; PVE-liittimet tulivat
mukana. Uusi PVEH yksinään maksaa noin 670 € + ALV. Ennen ostoa tehty arvio ja tarjouksen
perustelut: [arkisto](archive/aux-circuit-pvg32-pre-purchase.md).

## Avoimet kysymykset

- [ ] Omistajat: keulapotkurin ohjaimen valinta (portaaton PVEH-ohjaus joystickilla, ks. [bow-thruster-control](bow-thruster-control.md))
- [x] Käytetyn PVG 32:n hinta ja saatavuus: 5 lohkoa, 1 × PVEH ja 4 × PVEO, 400 € (tori.fi 2026-10-26), ks. [Ostettu venttiili](#ostettu-venttiili-danfoss-pvg-32-5-lohkoa-torifi)
- [x] PVG 32:n datalehti: paineluokka, karat, PVLP, PVE-signaali luettu ohjeesta 520L0344
- [ ] Danfossin jälleenmyyjä: kokoonpanokoodi (PVG No.) **157N5531** [omistaja 2026-11-03] → karat (erityisesti lohko 1: avoin keskiasento?) ja kahden lukemattoman peruslohkon tyyppi. Pumppumoduuli ja peruslohkot selvisivät rungon leimoista 2026-11-03
- [x] Myyjä: toimiko venttiili purettaessa → ei kokeiltu (kardaani rikki); säilytetty sisällä; hiekoittimessa nopeudensäätö (todennäköisesti PVEH-lohko) [myyjä 2026-10-27]
- [x] Myyjä: hyväksyykö 200 €:n tarjouksen → kaupat tehty 200 € + rahti 39,90 € [omistaja 2026-11-02]
- [x] Myyjä: tulivatko PVE-liittimet mukana → kyllä [omistaja 2026-11-02]; kunto ja määrä tarkistetaan vastaanotossa
- [x] Myyjä: mitä muut lohkot ohjasivat → ei kysytä enempää [omistaja 2026-11-02]; lohkojen karat ja toiminnot selvitetään vastaanotossa koodeista ja koestuksessa
- [x] Vastaanotto: koodit luettu rungosta 2026-11-03 (peruslohkot A 6200, pumppumoduuli 511?, kilpi PVP 28? bar), ks. [Vastaanotto](#vastaanotto-2026-11-03-rungon-merkinnät)
- [ ] Tulppaa avoimet portit ja tarkista kuljetusvauriot
- [x] Karojen liike käsin: kaikki viisi liikkuvat vapaasti molempiin suuntiin [omistaja 2026-11-03]
- [x] Karat palaavat jousella keskelle molemmista suunnista [omistaja 2026-11-03]
- [ ] Porttien sisäpuoli taskulampulla (ruoste, vesijäämä)
- [ ] Mitkä karat ovat kaksitoimisia (vinssi tarvitsee kaksitoimisen): koodista 157N5531 tai painekokeessa
- [x] Danfossin ohje 520L0344: peruslohko 157B6200 = kompensaattori, ei PVLP-paikkoja eikä LS A/B -rajoittimia; pumppumoduuli 157B5111 = suljettu keskiasento, pilottiöljy, P G 3/4, ei PVPX:ää (2026-11-03), ks. [Mitä koodit kertovat](#mitä-koodit-kertovat-2026-11-03)
- [x] PVEH on pumppumoduulista kauimmaisessa lohkossa [omistaja 2026-11-04]
- [ ] Mitkä karat ovat kaksitoimisia (lohkoissa 2–3 B-portti tulpattu autossa)
- [ ] Lue leimat kahdesta muusta peruslohkosta (onko kaikissa A 6200) ja katso, kummassa päässä P/LS-valumerkinnät ovat (kilven pää = pumppumoduuli); PVS vai PVSI
- [ ] Omistajat: keulapotkurin isku-/imuventtiilit ja vinssin paineraja: kaksoisristivirtausventtiilit moottoreille (suositus) vai peruslohkojen vaihto (157B6230 / 157B6203–6233); hinnat selvitettävä
- [ ] Rikkinäinen kupu PVEO:ssa (merkintä 101): vaihdetaanko kansi/tulppa vai koko PVEO; käytetään varalohkossa
- [ ] Danfoss: riittääkö PVH57:n noin 20 barin paine-ero PVG 32:n kompensaattoreille ja PVE:iden pilottiöljylle (ohjeessa käyrät 10 ja 20 barin paine-erolle [s. 35–36]; pilottiöljy tulee pumppumoduulin 157B5111 sisältä); sopiiko sarjan 4/7 PVE sarjan 0 lohkoon
- [ ] Pätevä henkilö: PVLP-isku- ja imuventtiilien tarve ja asetus keulapotkurille
- [x] Vinssilohkon peruslohkon koodi: 157B6200, ei LS A/B -rajoittimia eikä PVLP-paikkoja (2026-11-03)
- [ ] OMP 160:n suurin jatkuva ja hetkellinen paine-ero vinssin painerajan asetusta varten
- [ ] Danfossin PVG 32 -huolto-ohje: kiristyspulttien ja PVE-ruuvien momentit, purkujärjestys; PVAS 157B8005:n hinta; korjaamon koestuksen hinta
- [ ] Sleipner: sopiiko SH240 portaattomaan ohjaukseen proportionaaliventtiilillä
- [ ] Ankkurivinssin moottori (Danfoss OMP 160 (151-0031) [omistaja 2026-10-27]): paineraja vinssilohkolle (OMP:n raja alle järjestelmän 250 barin ⚠), jarruventtiili
- [ ] Painepesurin hydraulimoottorin virtaus ja paine
