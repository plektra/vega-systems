# Apupiiri alusta alkaen: säätötilavuuspumppu ja proportionaalinen LS-lohkoventtiili

> **Tila:** ajatuskoe 2026-10-25, **ei päätetty**. Päätetty kokoonpano on yhä F1-61 tai vastaava
> ohitusventtiilillä ([p2-pump-options](p2-pump-options.md)). PVH57:n käyttö olemassa olevien
> venttiilien kanssa on selvitetty tiedostossa [p2-variable-pump](p2-variable-pump.md). Tässä
> kysytään, miten apupiiri rakennettaisiin, jos olemassa olevia venttiileitä ei tarvitsisi käyttää
> uudelleen [omistaja 2026-10-25, kysymys].
> Sama ilman proportionaalista venttiilipöytää, on/off-venttiileillä: [aux-circuit-ls-onoff](aux-circuit-ls-onoff.md).
>
> Lohkoventtiilin arvot ovat yleistietoa, **ei luettu datalehdestä** (**⚠ tarkista**). Pätevän
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
PTO 1:1 ─ Spidex ─ PVH57 (LS) ──P──►│ tulomoduuli: paineenrajoitin (varaventtiili), LS-rajoitin, P-mittari          │
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

- Veto ja imu kuten nyt on päätetty: Spidex 48/60, oma kannake (SAE C -laippa, noin 36 kg
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

- **Suodatus:** mäntäpumppu vaatii puhtausluokan 17/15/13 (140–210 bar) [Eatonin PVH-luettelo s. 31,
  ks. [p2-variable-pump](p2-variable-pump.md#tekniset-tiedot)]. Nykyinen paluusuodatin
  OMTF112C10NA2 (10 µm, arviolta selluloosa nominaalinen) ei riitä sellaisenaan [omistaja 2026-10-26], ks.
  [p2-variable-pump](p2-variable-pump.md#kumpi-on-monimutkaisempi-f1-61-vai-pvh57). Ehdotus:
  lasikuituinen paluusuodatin 10 µm
  tukkeumaosoittimella, säiliöön 3 µm:n huohotin, öljyn lisäys suodattimen kautta [arvio].
- **Jäähdytys:** EC100 (tai EC80) paluulinjaan termostaattiohituksella
  ([oil-cooling](oil-cooling.md)). Lämpökuorma pienenee selvästi: esim. pesuri jatkuvasti noin
  30 l/min × noin 25 bar säätövaraa ≈ 1,3 kW sekä moottorin häviöt [arvio]. Vertailuksi nykyisen
  suunnitelman ylimäärän kuristus keulapotkuria käytettäessä 1800 rpm:llä on noin 38 kW
  ([p2-pump-options](p2-pump-options.md#käyttäytyminen-eri-kierroksilla-parker-f1-061)).
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
- **Säilyy:** säiliö, 50 mm:n imu, Spidex ja kannake, keulapotkurin 1/2":n letkut, jäähdytin.
- **Mahdollisuus, joka vaatii omistajien päätöksen:** PVG 32:n paineluokka on 350 bar
  **⚠ tarkista**, ja PVH-luettelon mukaan LS-järjestelmän paineenrajoitin voi olla 280 bar. Silloin
  keulapotkuri pääsisi lähemmäs täyttä työntöä nykyisen noin 85–88 %:n sijaan. Edellyttää, että
  pumpun säätöalue sallii sen (C-jousi 70–250 bar, **⚠ tarkista Danfossilta**) ja muuttaisi
  250 barin päätöstä (2026-10-21).

## Kustannukset

- LS-lohkoventtiilin hinta **⚠ ei tiedossa** (uutena arviolta useita satoja euroja lohkolta,
  käytettynä huomattavasti halvempi [arvio]).
- Ratkaisu jättää käyttämättä toimivia osia, jotka on jo hankittu.

## Suositus

Teknisesti paras ratkaisu on **PVH57 ja proportionaalinen LS-lohkoventtiili**, jos tavoitteena on
vähintään kaksi seuraavista: portaaton keulapotkuri, ankkurivinssi, pitkäkestoinen painepesu. Jos
tavoitteena on edelleen on/off-keulapotkuri ja mahdollisesti vinssi, nykyinen F1-61
ohitusventtiilillä tai [PVH57:n pienin muutos](p2-variable-pump.md#suositus-kaksitiekompensoitu-virtauksensäätö-ja-ls-purku)
on halvempi ja riittää.

## Avoimet kysymykset

- [ ] Omistajat: onko keulapotkurin portaaton ohjaus tavoite (sama kysymys kuin [p2-variable-pump](p2-variable-pump.md#avoimet-kysymykset))
- [ ] Käytetyn PVG 32:n (tai vastaavan LS-lohkoventtiilin) hinta ja saatavuus 3–4 lohkolla ja PVE-ohjauksella
- [ ] PVG 32:n datalehti: paineluokka, moottorikarat noin 40 l/min, isku- ja imuventtiilit, PVE-ohjaussignaali, vaadittu pumpun LS-paine-ero
- [ ] Sleipner: sopiiko SH240 portaattomaan ohjaukseen proportionaaliventtiilillä
- [ ] Ankkurivinssin moottori, jarru ja jarruventtiili
- [ ] Painepesurin hydraulimoottorin virtaus ja paine
