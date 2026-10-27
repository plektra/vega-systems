# Apupiiri alusta alkaen: säätötilavuuspumppu ja proportionaalinen LS-lohkoventtiili

> **Tila:** **PÄÄTETTY YKKÖSVAIHTOEHTO 2026-10-27:** apupiiri rakennetaan PVH57:llä ja käytetyllä Danfoss PVG 32:lla
> ([Ehdokas](#ehdokas-danfoss-pvg-32-5-lohkoa-torifi)); kaupat toteutumassa [omistaja 2026-10-27]. Varavaihtoehdot: [LS + on/off](aux-circuit-ls-onoff.md)
> ja [FXDC + LS-purku](p2-variable-pump.md#suositus-kaksitiekompensoitu-virtauksensäätö-ja-ls-purku). Ajatuskoe 2026-10-25, päivitetty 2026-10-26 ja 2026-10-27
> (PVG 32 -ehdokas, tarjous, puhdistus, paino). Pumppu PVH57 päätetty 2026-10-27 (F1-61
> [arkistoitu](archive/p2-pump-options.md)). PVH57:n käyttö olemassa olevien
> venttiilien kanssa on selvitetty tiedostossa [p2-variable-pump](p2-variable-pump.md). Tässä
> kysytään, miten apupiiri rakennettaisiin, jos olemassa olevia venttiileitä ei tarvitsisi käyttää
> uudelleen [omistaja 2026-10-25, kysymys].
> Sama ilman proportionaalista venttiilipöytää, on/off-venttiileillä: [aux-circuit-ls-onoff](aux-circuit-ls-onoff.md).
>
> PVG 32:n arvot on 2026-10-26 tarkistettu Danfossin teknisestä ohjeesta 520L0344 (ks.
> [Ehdokas](#ehdokas-danfoss-pvg-32-5-lohkoa-torifi)); muut lohkoventtiilin arvot ovat yleistietoa (**⚠ tarkista**). Pätevän
> henkilön pitää tarkistaa kytkentä, säätöarvot ja erityisesti ankkurivinssin kuorman pito ennen
> rakentamista.

## Selkokielinen yhteenveto

- Nykyinen rakenne (pumppu → virtauksensäätö VPR3 → vapaakiertoventtiili → CETOP-pohjalaatta →
  on/off-venttiilit) on tehty **kiinteälle pumpulle**. Säätötilavuuspumpulle luonteva rakenne on
  **kuormantunteva (LS) järjestelmä**, jossa pumppu ja venttiilit on tehty toimimaan yhdessä.
- Venttiilien LS-linja kertoo pumpulle suurimman kuorman paineen. Pumppu pitää paineen noin 20 bar
  sen yläpuolella ja tuottaa vain sen, mitä venttiilit päästävät läpi.
- **Kun mitään ei käytetä, pumppu lepää itsestään** noin 20 barissa lähes ilman tuottoa. Ohitus-,
  purku- ja vapaakiertoventtiileitä ei tarvita.
- Yksi proportionaalinen LS-lohkoventtiili (esim. Danfoss PVG 32) korvaa CETOP-pohjalaatan,
  BAV-713:n, VPR3:n, OD15:n, VMP:n ja BPV:n. Keulapotkuri ja vinssi saavat **portaattoman** ohjauksen.
- **Kannattaa,** jos vähintään kaksi toteutuu: portaaton keulapotkuri, ankkurivinssi, pitkäkestoinen
  painepesu. Muuten nykyinen suunnitelma on halvempi ja riittää.

## Kaavio

```
                                    ┌───────── proportionaalinen LS-lohkoventtiili (esim. Danfoss PVG 32) ─────────┐
PTO 1:1 ─ HRC150 ─ PVH57 (LS) ──P──►│ tulomoduuli: paineenrajoitin (varaventtiili), LS-rajoitin, P-mittari          │
                    │   ▲           │ 1. keulapotkuri  A/B  – moottorikara (A,B→T keskellä), isku-/imuventtiilit    │──► keula (1/2", olemassa)
                    │   └── LS ─────│ 2. ankkurivinssi A/B  – moottorikara, jarrun avaus; jarruventtiili moottorilla │──► vinssi
                    │               │ 3. painepesuri   A    – yksisuuntainen, virtaus rajattu                        │──► pesuri
                    │               │ 4. varapaikka (daavitti, myöhemmin)                                           │
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

Esimerkkinä Danfoss PVG 32 sähköisellä ohjauksella (PVE). Se on yleinen työkoneissa, joten
käytettyjä on saatavilla. Jokaisessa lohkossa on oma painekompensaattori, joten jokainen kuorma
saa asetetun virtauksensa paineesta riippumatta, kunhan pumpun tuotto riittää.

| Lohko | Kuorma | Kara ja lisät |
|---|---|---|
| 1 | Keulapotkuri | Moottorikara: keskellä A ja B ovat yhteydessä säiliöön, joten potkuri pyörii vapaasti kuten BAV-713:lla ([päätös 2026-10-23](../../decisions.md)). Isku- ja imuventtiilit A/B-portteihin. Karan koko noin 40 l/min **⚠ tarkista karavalikoima**. Portaaton työntö ilman lisäosia; **⚠ tarkista, sopiiko SH240 portaattomaan ohjaukseen**. |
| 2 | Ankkurivinssi | Moottorikara, portaaton nopeus. **Kuorman pito vinssin omalla jarrulla ja moottoriin asennetulla jarruventtiilillä, ei venttiilin karalla.** Vinssin moottorin tiedot **⚠ ei tiedossa** ([loads.yaml](../loads.yaml)). |
| 3 | Painepesuri | Yksisuuntainen, virtaus rajattu pesurimoottorin tarpeeseen (**⚠ ei tiedossa**, laitetta ei valittu) |
| 4 | Varapaikka | Daavitti tai muu myöhemmin; lohkoja voi lisätä jälkikäteen |

- **Käsivivut:** jokaisessa lohkossa on käsivipu, jolla vinssiä ja potkuria voi käyttää, vaikka
  sähköohjaus pettäisi.
- **Ohjaus:** ESP32 PDM ohjaa PVE-yksiköitä (jänniteohjaus tai CAN-malli **⚠ tarkista**).
  Keulapotkurille joystick tai keinukytkin, vinssille kytkin. Tilat Signal K:hon.
- **Lukitus ohjelmassa:** pesuria voi käyttää vain, kun keulapotkuri ja vinssi ovat pois päältä.
  Tyhjäkäynnillä 38 l/min ei riitä kahdelle kuormalle yhtä aikaa, ja silloin suurimman paineen
  kuorma (keulapotkuri) jäisi vajaaksi [arvio].

### 3. Paluu, suodatus ja jäähdytys

- **Suodatus:** mäntäpumppu vaatii puhtausluokan 16/14/12 yli 210 barissa (17/15/13 140–210 barissa) [Eatonin PVH-luettelo s. 31,
  ks. [p2-variable-pump](p2-variable-pump.md#tekniset-tiedot)]. Nykyinen paluusuodatin
  OMTF112C10NA2 (10 µm, arviolta selluloosa nominaalinen) ei riitä sellaisenaan [omistaja 2026-10-26], ks.
  [p2-variable-pump](p2-variable-pump.md#kumpi-on-monimutkaisempi-f1-61-vai-pvh57). Ehdotus:
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
| Kara jumittuu auki | PVE:n vikavalvonta antaa vikasignaalin **⚠ tarkista malli**. Hätäpysäytys katkaisee PVE:iden virran. Varaventtiili rajaa paineen. |
| Pumpun säädin jumittuu täydelle tuotolle | Tulomoduulin paineenrajoitin rajaa paineen; tilanne vastaa kiinteää pumppua (lämpöä), lämpötila-anturi hälyttää. |
| Kotelovuotolinja tukkeutuu | Akselitiiviste voi vaurioitua; siksi vuotolinja on oma letkunsa. |
| Vinssi kuormassa ja hydrauliikka menetetään | Jarruventtiili ja vinssin jarru pitävät kuorman. **Pätevä henkilö tarkistaa ennen rakentamista.** |

## Mikä muuttuu nykysuunnitelmaan verrattuna

- **Poistuu:** CETOP-pohjalaatta, BAV-713, VPR3, OD15, VMP ja BPV-ohitusventtiili, sekä
  PVH57-selvityksen 2/2-, 3/2- ja FXDC-ratkaisut, joita tarvitaan vanhojen osien kanssa.
- **Säilyy:** säiliö, 50 mm:n imu, kytkin ja kannake, keulapotkurin 1/2":n letkut, jäähdytin.
- **Mahdollisuus, joka vaatii omistajien päätöksen:** PVG 32:n P-portin paineluokka on 350 bar
  (PVSI-päätylevyllä; PVS-päätylevyllä 300 bar) [datalehti PVG 32 s. 12], ja PVH-luettelon mukaan LS-järjestelmän paineenrajoitin voi olla 280 bar. Silloin
  keulapotkuri pääsisi lähemmäs täyttä työntöä nykyisen noin 85–88 %:n sijaan. Edellyttää, että
  pumpun säätöalue sallii sen (C-jousi 70–250 bar, **⚠ tarkista Danfossilta**) ja muuttaisi
  250 barin päätöstä (2026-10-21).

## Kustannukset

- LS-lohkoventtiilin hinta uutena **⚠ ei tiedossa** (arviolta useita satoja euroja lohkolta [arvio]).
  Käytetty 5-lohkoinen PVG 32 on myynnissä 400 €:lla; omistaja tarjosi 200 € (2026-10-27), ks. [Ehdokas](#ehdokas-danfoss-pvg-32-5-lohkoa-torifi).
- Ratkaisu jättää käyttämättä toimivia osia, jotka on jo hankittu.

## Suositus

**Päätös 2026-10-27:** PVH57 + PVG 32 valittiin ykkösvaihtoehdoksi ([decisions.md](../../decisions.md)).

Teknisesti paras ratkaisu on **PVH57 ja proportionaalinen LS-lohkoventtiili**, jos tavoitteena on
vähintään kaksi seuraavista: portaaton keulapotkuri, ankkurivinssi, pitkäkestoinen painepesu. Jos
tavoitteena on edelleen on/off-keulapotkuri ja mahdollisesti vinssi, (arkistoitu) F1-61
ohitusventtiilillä tai [PVH57:n pienin muutos](p2-variable-pump.md#suositus-kaksitiekompensoitu-virtauksensäätö-ja-ls-purku)
on halvempi ja riittää.

## Ehdokas: Danfoss PVG 32, 5 lohkoa (tori.fi)

> Lisätty 2026-10-26. Tiedot luettu ilmoituksen kuvista ja Danfossin teknisestä ohjeesta
> *PVG 32 Proportional Valve Group, Technical Information 520L0344*
> ([PDF](https://imdl.gatech.edu/jfrankel/docs/Sauer-Danfoss/520L0344_PVG32.pdf)), jäljempänä
> [datalehti PVG 32]. **Päätetty ykkösvaihtoehdoksi 2026-10-27; kaupat toteutumassa.**

Ilmoitus: <https://www.tori.fi/recommerce/forsale/item/46493298>, **400 €, tee tarjous** (tarkistettu
2026-10-26). Ilmoituksen teksti: *"Danfors pvg 32 venttiilipöytä. Tienhoitoautosta purettu. Karojen
ja kelojen tyypistä ei tarkempaa tietoa."*

### Mitä venttiilistä tiedetään

Kuvista luetut arvot on merkitty *kuvasta*; merkinnät ovat likaisia ja osin epäselviä.

| Kohde | Tieto | Lähde |
|---|---|---|
| Tyyppi | *Danfoss Proportional Valve Type PVG 32* (valukilpi) | kuvasta |
| Lohkot | **5 työlohkoa**, pumppumoduuli ja päätylevy | kuvasta |
| Kokoonpanokoodi | **157N553(8 tai B)** rungossa [omistaja 2026-10-26; kuvankäsittelyllä vahvistettu, N näyttää aidolta]. Todennäköisesti koko venttiilin kokoonpanokoodi (Danfossilla on 157N-alkuisia kokonaisia suuntaventtiileitä, esim. 157N-5754, [parttarget](https://www.parttarget.com/Danfoss-Fluid-Power-Inc_nsn-parts_D-961428_7WXP2126-010.html)) **⚠ tarkista**. Varavaihtoehto: luettu väärin, ja kyse on pumppumoduulista 157B5938 (PVPV, suljettu keskiasento, G 1", 350 bar) | kuvasta, [datalehti PVG 32] s. 22 |
| Ohjausyksiköt (PVE) | Lohko 1: **157B4024 = PVEH 24 V** (proportionaalinen, vikavalvonta); lohkot 2–3: **157B4224 = PVEO 24 V** (on/off); lohkot 4–5 epäselviä, todennäköisesti PVEO. Kaikki vanhaa sarjaa 0. | kuvasta, [Kramp: PVE cross reference](https://documents.kramp.com/PVE_cross_reference_EN.pdf) |
| Käsiohjaus | Toisella puolella käsivipujen kannat ilman vipuja **⚠ tarkista** | kuvasta |
| Karat | **⚠ ei tiedossa**; selviää kokoonpanokoodista | – |
| Pumppumoduuli | Autossa kytkettynä **säätötilavuuspumppuun** [myyjä 2026-10-27] → todennäköisesti **suljetun keskiasennon** malli, joka sopii PVH57:lle. Moduulin oma koodi (157B5…) **⚠ tarkista** rungosta. Kuvassa kyljessä liitin, todennäköisesti käytössä ollut LS-portti; ylhäällä P- ja T-portit, M-portti ja tulpattu lisäportti; etupinnalla todennäköisesti paineenrajoittimen säätöruuvi | [myyjä 2026-10-27], kuvasta |
| Paino | **noin 22–23 kg** [laskelma]: PVP 3,1 kg + 5 × PVB 3,05 kg + 4 × PVEO 0,6 kg + PVEH noin 1 kg **⚠ arvio** + päätylevy, kiristyspultit ja vipujen kannat noin 1 kg **⚠ arvio** | Danfossin tekninen ohje (ranskankielinen BC152886483664fr, hakutuloksen ote), [paro.nl: PVEO 157B4228](https://paro.nl/library/components/danfoss/157b4228-pvg32-pveo) |
| Kunto | likainen, **osa porteista auki ilman tulppia** → puhdistus ja koestus välttämättömiä | kuvasta |
| Toiminta purettaessa | **Ei kokeiltu:** auton keulapumpun kardaani oli rikki, kun auto tuli purkuun, joten venttiiliä ei voitu ajaa. Toimintakunto ja vuodot **⚠ ei tiedossa** | [myyjä 2026-10-27] |
| Käyttö autossa | Hiekoittimessa oli nopeudensäätö → todennäköisesti se oli ainoa portaaton toiminto ja PVEH-lohko, muut on/off. Sopii kuvista luettuun (1 × PVEH, 4 × PVEO) | [myyjä 2026-10-27] |
| Säilytys | sisällä purkamisen jälkeen; irrotuksen kesto **⚠ ei tiedossa** | [myyjä 2026-10-27] |

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

Pumppumoduuli on todennäköisesti suljetun keskiasennon malli, koska venttiili oli autossa
kytkettynä säätötilavuuspumppuun [myyjä 2026-10-27]. Varmistetaan moduulin koodista; jos se
osoittautuu avoimen keskiasennon malliksi, moduuli vaihdetaan (esim. 157B5111, G 3/4, suljettu
keskiasento, pilottiöljy PVE:ille **⚠ tarkista** Danfossin ohjeesta) **⚠ hinta ei tiedossa**.

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
| Painelinja pumpulta P-porttiin | P-portti moduulin mukaan G 1/2", G 3/4" tai G 1" [s. 20–22] |
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
| Isku- ja imuventtiilit PVLP keulapotkurin A/B-porttiin | **Suositus,** jos lohkossa on niille paikat: Sleipner vaatii iskuventtiilit 10–15 % maksimipaineen yläpuolelle, ja imuventtiili estää kavitaation potkurin pyöriessä vapaasti. Esim. PVLP 280 bar = 157B2280 [s. 27] **⚠ hinta ei tiedossa**. Pätevä henkilö arvioi. |
| Pumpun paine-ero (PVH57 noin 20 bar) | riittää luultavasti lohkojen kompensaattoreille ja PVE:iden pilottiöljylle **⚠ tarkista Danfossilta** |
| Tiivisteet ja puhdistus | PVAS 157B8005, jos venttiili avataan; puhdistus ja koestus hydrauliikkaliikkeessä |

**Sähkö ja ohjaus** [datalehti PVG 32 s. 15–18]:

| Asia | Arvo tai ratkaisu |
|---|---|
| PVE:n käyttöjännite | 22–30 V (24 V käy) |
| PVEH:n ohjaussignaali | **suhteellinen käyttöjännitteeseen:** keskiasento 0,5 × U, täysi 0,25 × U tai 0,75 × U |
| Ohjain | **potentiometrijoystick samasta syötöstä** antaa signaalin suoraan ilman elektroniikkaa; vaihtoehtona ESP32 skaalatulla analogialähdöllä |
| Liitin | Hirschmann DIN, 4-napainen (syöttö, signaali, maa, vikasignaali) |
| Vikavalvonta | PVEH pysäyttää karan, jos signaali on alueen 15–85 % ulkopuolella (myös johdon katketessa); vikasignaali Signal K:hon hälytykseksi |
| Pääkytkin / hätäseis | rele katkaisee PVE:iden syötön → jouset palauttavat karat keskelle |
| (valinnainen) PVPX 24 V, 157B4238 | sähköinen LS-purku: pumppu valmiustilaan sähkökatkossa; vaatii PVPX-paikan pumppumoduulissa **⚠ tarkista** [s. 29] |

**Käyttöönotto** (pätevä henkilö hyväksyy arvot):

1. Venttiili puhdistetaan, kara tarkistetaan ja PVLP:t lisätään tarvittaessa.
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
2. **Tarkistus purkamatta**
   - Kansi auki PVE:n tai käsivivun puolelta lohko kerrallaan: karan pitää liikkua käsin molempiin
     suuntiin ja palata jousella keskelle. Jäykkä kara viittaa likaan tai ruosteeseen.
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

### Arvio

400 € on kohtuullinen, jos lohkot ja PVEH ovat kunnossa: yksi uusi PVEH maksaa enemmän kuin koko
venttiili. Venttiili sopii vain PVH57-reittiin (suljetun keskiasennon moduulilla). Ennen tarjousta
selvitetään kokoonpanokoodilla pumppumoduulin tyyppi ja karat sekä kysytään myyjältä, toimiko PVEH
purettaessa.

**Päivitys 2026-10-27:** Myyjä ei päässyt kokeilemaan venttiiliä (keulapumpun kardaani rikki), joten
toimintakunnosta ja vuodoista ei ole tietoa. Sisäsäilytys pienentää ruostumisen ja karojen
jumiutumisen riskiä, mutta auki olleiden porttien kautta sisään on voinut päästä likaa. Omistaja
tarjosi **200 €** perustellen riskillä, että venttiili joutuu kierrätykseen [omistaja 2026-10-27].
Tarjous on perusteltu: pelkkä PVEH-yksikkö on uutena noin 670 € + ALV, ja karat sekä PVE:t voi
koestaa ja tarvittaessa vaihtaa yksitellen. Myyjän mukaan venttiili oli kytkettynä
säätötilavuuspumppuun, joten pumppumoduulin vaihto ei todennäköisesti ole tarpeen
[myyjä 2026-10-27]. Odottaa myyjän vastausta tarjoukseen.

## Avoimet kysymykset

- [ ] Omistajat: onko keulapotkurin portaaton ohjaus tavoite (sama kysymys kuin [p2-variable-pump](p2-variable-pump.md#avoimet-kysymykset))
- [x] Käytetyn PVG 32:n hinta ja saatavuus: 5 lohkoa, 1 × PVEH ja 4 × PVEO, 400 € (tori.fi 2026-10-26), ks. [Ehdokas](#ehdokas-danfoss-pvg-32-5-lohkoa-torifi)
- [x] PVG 32:n datalehti: paineluokka, karat, PVLP, PVE-signaali luettu ohjeesta 520L0344
- [ ] Danfossin jälleenmyyjä: kokoonpanokoodi 157N553(8/B) → pumppumoduulin tyyppi (todennäköisesti suljettu keskiasento, koska autossa oli säätötilavuuspumppu [myyjä 2026-10-27]; varmistetaan moduulin koodista), peruslohkot (PVLP-paikat, LS A/B -vaihtoventtiili), karat
- [x] Myyjä: toimiko venttiili purettaessa → ei kokeiltu (kardaani rikki); säilytetty sisällä; hiekoittimessa nopeudensäätö (todennäköisesti PVEH-lohko) [myyjä 2026-10-27]
- [ ] Myyjä: hyväksyykö 200 €:n tarjouksen; mitä muut lohkot ohjasivat; porttien tulppaus kuljetukseen
- [ ] Danfoss: riittääkö PVH57:n noin 20 barin paine-ero PVG 32:n kompensaattoreille ja PVE:iden pilottiöljylle; sopiiko sarjan 4/7 PVE sarjan 0 lohkoon
- [ ] Pätevä henkilö: PVLP-isku- ja imuventtiilien tarve ja asetus keulapotkurille
- [ ] Danfossin PVG 32 -huolto-ohje: kiristyspulttien ja PVE-ruuvien momentit, purkujärjestys; PVAS 157B8005:n hinta; korjaamon koestuksen hinta
- [ ] Sleipner: sopiiko SH240 portaattomaan ohjaukseen proportionaaliventtiilillä
- [ ] Ankkurivinssin moottori, jarru ja jarruventtiili
- [ ] Painepesurin hydraulimoottorin virtaus ja paine
