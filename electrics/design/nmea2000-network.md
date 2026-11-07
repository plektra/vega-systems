# NMEA 2000 ja CAN-väylät: laiteluettelo ja luotettava väylä

> **Tila:** Selvitys ja laiteluettelon ensimmäinen versio, aloitettu 2026-11-07, päivitetty 2026-11-08 (Pi:n CAN-HAT, ei koneen väylää, Cerbo GX MK2, 12 V harkinnassa). **Mitään ei ole
> päätetty.** Luettelossa on omistajien kertomat laitteet, muiden dokumenttien jo suunnittelemat
> anturit ja Clauden ehdotukset; sarake *Tila* kertoo, kumpi on kyseessä. Luettelo täydentyy, kun
> laitteita valitaan.
>
> Liittyy: [current-system.md 3.3 ja 4](../current-system.md#33-nmea-2000--väylän-laitteet),
> [inverter-bms.md](inverter-bms.md) (BMS-CAN), [dc-distribution.md](dc-distribution.md) (syöttö),
> [circuit-list.md](circuit-list.md) (KH-20), [hydraulics/requirements.md §10](../../hydraulics/requirements.md#10-valvonta-ohjaus-ja-integrointi),
> [ESP32-PDM](https://github.com/plektra/ESP32-PDM).

## 1. Yhteenveto

1. **Laiteluettelo (kohta 3):** väylään on tulossa noin 25–30 laitetta tai mittauspistettä:
   navigointi, kone, sähkö, hydrauliikka, säiliöt, olosuhteet ja PDM-ohjaus. Suurin osa
   antureista ei liity väylään suoraan, vaan omien ESP32-nodejen ja PDM-korttien kautta.
2. **⚠ Tärkein havainto: 24 V:n väyläjännite ja ESP32-PDM eivät sovi yhteen.** Väylää syötetään
   nyt 24 V:lla (DDR-240B-24, [omistaja 2026-10-29]). ESP32-PDM-kortti on kuitenkin suunniteltu
   standardin 9–16 V:n väylälle: sen CAN-puolen syötössä on TVS-diodi SMAJ18CA, joka alkaa johtaa
   noin 20 V:n jännitteellä ([ESP32-PDM design-notes §8.3](https://github.com/plektra/ESP32-PDM/blob/main/docs/design-notes.md)
   "no operating voltage above 16 V on NMEA 2000") [laskelma]. 24 V:n väylällä diodi oikosulkee
   syötön tai palaa. **Suositus [arvio]: syötetään runkoväylä 12 V:lla erotetulla 24→12 V
   -muuntimella** (kohta 5.1). Silloin käyvät kaikki kaupalliset N2K-laitteet ja PDM sellaisenaan.
   Omistaja harkitsee 12 V:n syöttöä turvallisempana vaihtoehtona [omistaja 2026-11-08]; ei vielä
   päätetty.
3. **Väyliä on kaksi, eikä niitä yhdistetä suoraan** (kohta 4): NMEA 2000 (250 kbit/s) ja
   Victronin BMS-CAN (500 kbit/s, JK-BMS ↔ Cerbo GX). Pääkoneessa ei todennäköisesti ole
   tiedonsiirtoväylää eikä ohjainyksikköä; kone on ilmeisesti mekaanisilla yksikköinjektoreilla (MUI)
   [omistaja 2026-11-08], joten koneen tiedot tulevat omista
   antureista ESP32-noden kautta.
4. **Turvallisuuskriittinen toiminta ei saa riippua väylästä.** Ohjaus, keulapotkurin perusohjaus,
   pilssipumppujen kohokytkimet, kulkuvalot ja hätäseis toimivat ilman N2K:ta. Väylä tuo
   valvonnan, hälytykset ja etäohjauksen (kohta 6).
5. **Luotettavuus syntyy perusasioista** (kohta 5): yksi suora runkoväylä, päätevastus vain
   kummassakin päässä, yksi syöttöpiste omalla sulakkeella, valmiit Micro-C-kaapelit märissä
   tiloissa, jokaiselle laitteelle oma yksilöllinen tunnus ja instanssi sekä Signal K:n valvonta
   katoavista laitteista.

## 2. Lähtötilanne

| Kohde | Tieto | Lähde |
|---|---|---|
| Väylän syöttö | Mean Well DDR-240B-24, vakautettu 24 V; sama muunnin syöttää NUC:n, 4G-modeemin ja PoE-kamerat (piiri KH-20) | [omistaja 2026-10-29], [circuit-list](circuit-list.md) |
| Väylälaitteiden jännitekesto | "Kaikki Vegan väylälaitteet toimivat 9–32 V:lla" (koskee nykyisiä laitteita, ei ESP32-PDM:ää, ks. kohta 1) | [omistaja 2026-10-29] |
| Signal K -palvelin | Raspberry Pi 5, konehuone [omistaja 2026-10-29]. Väylään **eristetyllä Waveshare 2-CH CAN HAT -kortilla** (kaksi kanavaa, MCP2515 + SN65HVD230/SI65HVD230, digitaalinen erotin ja erotettu DC/DC-muunnin CAN-puolelle, jumpperilla kytkettävä 120 Ω:n päätevastus, SocketCAN `can0`/`can1`; eristysjännitettä ei kerrota) | [omistaja 2026-11-08], [datalehti Waveshare 2-CH CAN HAT](https://www.waveshare.com/wiki/2-CH_CAN_HAT) |
| Omat N2K-nodet | `vega-n2k-node1` ja `node2` (ESP32, erotettu CAN-piiri ISO1044, regulaattori LM7805; NMEA2000-kirjasto ttlappalainen). `node3` on keskeneräinen GNSS-node (Quectel-moduuli NMEA 0183:lla, ei vielä N2K:ta) | [vega-n2k-node1…3, koodi luettu 2026-11-07] |
| Runkoväylän pituus, reitti, kaapeli, liittimet, päätevastukset | **⚠ ei tiedossa** | – |
| Nykyisten laitteiden LEN-arvot | **⚠ ei tiedossa** | – |

## 3. Laiteluettelo

**Tunnukset:** `N-xx` = NMEA 2000 -laite tai -node. Mittaukset, jotka kulkevat noden tai PDM:n
kautta, on merkitty noden alle. Mittausten tunnukset (2B1, 3B1 jne.) ovat
[hydrauliikan kaaviosta](../../hydraulics/schematic.md).

**Liitäntä:** *N2K* = valmis NMEA 2000 -laite; *node* = anturi oman ESP32-noden kautta; *PDM* =
ESP32-PDM-kortin tulo tai lähtö; *GW* = yhdyskäytävä toisesta väylästä; *0183* = NMEA 0183
-sarjaliitäntä muuntimen kautta.

**Tila:** *olemassa*, *omistajan lista* (omistaja on maininnut laitteen), *suunniteltu* (toisessa
dokumentissa suunniteltu tai päätetty), *ehdotus* (Clauden ehdotus, ei omistajien listalla).

**PGN:t** ovat tavallisia NMEA 2000 -viestejä kyseiselle tiedolle (**⚠ tarkista**, kun laite
valitaan). Hydrauliikalle ei ole vakioviestejä, joten se kulkee paineen ja lämpötilan yleisviesteillä
tai Signal K:n kautta.

### 3.1 Väylän infrastruktuuri ja yhdyskäytävät

| Tunnus | Laite | Sijainti | Liitäntä | PGN:t / tieto | Tila | Lähde |
|---|---|---|---|---|---|---|
| N-01 | Signal K -palvelin (Raspberry Pi 5) ja Waveshare 2-CH CAN HAT (eristetty) | konehuone | N2K kanavalla `can0`; toinen kanava vapaana (varalla tai väylän testaukseen) | kuuntelee kaikkea; lähettää tarvittaessa (esim. hälytykset, kytkinkomennot 127502) | olemassa (liitäntä auki) | [omistaja 2026-10-29] |
| N-02 | Victron Cerbo GX, VE.Can-portti | konehuone | N2K (VE.Can → NMEA 2000 -kaapeli) | akut 127506/127508, invertteri ja lataus; vaihtoehtoisesti tiedot Signal K:hon verkon (MQTT) kautta, jolloin N2K-liitäntää ei tarvita | suunniteltu (Cerbo päätetty 2026-10-31) | [decisions 2026-10-31](../../decisions.md), [inverter-bms](inverter-bms.md) |
| N-03 | Koneen anturinode (ESP32): kierrokset, öljynpaine, jäähdytysnesteen lämpötila, käyttötunnit | konehuone | node | 127488, 127489 | ehdotus; koneessa ei todennäköisesti ole väylää [omistaja 2026-11-08], joten J1939-yhdyskäytävää (esim. Maretron J2K100) ei tarvita | [omistaja 2026-11-08] |
| N-04 | Navigointitietokone ja näyttö (OpenCPN tms.) | komentosilta | Signal K:n kautta (verkko), ei omaa N2K-liitäntää | – | omistajan lista | [current-system 3.2](../current-system.md#32-komentosillalta-ohjattavat-24-vn-laitteet) |
| N-05 | Väylän valvontanode (jännite väylän kaukaisessa päässä, virheet) | runkoväylän pää | node | 127751 (DC-jännite/virta) tai Signal K | ehdotus | kohta 5.6 |

### 3.2 Navigointi

| Tunnus | Laite | Sijainti | Liitäntä | PGN:t / tieto | Tila | Lähde |
|---|---|---|---|---|---|---|
| N-10 | GPS/GNSS-vastaanotin | luultavasti katto | N2K, tai oma `node3` (Quectel, 0183 → N2K) | 129025, 129026, 129029, 126992 (aika) | omistajan lista; node3 keskeneräinen | [omistaja 2026-10-29], [vega-n2k-node3] |
| N-11 | AIS, luokka B | komentosilta, antenni mastossa | N2K (useimmissa B-luokan laitteissa myös 0183/USB) | 129038, 129039, 129040, 129794, 129809, 129810 | omistajan lista | [omistaja 2026-10-29] |
| N-12 | Tuulianturi | masto | N2K (pudotus mastoon) | 130306 | omistajan lista | [omistaja 2026-10-29] |
| N-13 | Peräsinkulma-anturi | peräsinakseli | N2K tai node (potentiometri / Hall → ESP32) | 127245 | omistajan lista; autopilotti tarvitsee | [omistaja 2026-10-29], [hydraulics §10.1](../../hydraulics/requirements.md#101-anturit) |
| N-14 | Kompassi / suunta-anturi (heading, kallistus) | lähellä painopistettä, kaukana teräksestä ja kaapeleista | N2K | 127250, 127251, 127257 | **ehdotus**: autopilotti ja tutkan karttapäällys tarvitsevat suunnan. Teräsrungossa magneettikompassi vaatii kalibroinnin; GNSS-kompassi (kaksi antennia) ei välitä rungosta **⚠ arvio** | – |
| N-15 | Kaiku ja loki (syvyys, nopeus vedessä, veden lämpötila) | pohja | N2K (anturimoduuli) | 128267, 128259, 130316 | **ehdotus** | – |
| N-16 | Autopilotin ohjausyksikkö | komentosilta / konehuone | N2K (suunta, peräsinkulma, reitti) | 127237, 127245, 127250, 129283, 129284 | omistajan lista (mahdollinen); malli auki | [hydraulics §10.3](../../hydraulics/requirements.md#103-autopilotin-liitäntä-ohjauspiiriin) |
| N-17 | VHF Sailor RT2048 | komentosilta | **⚠ tarkista** liitäntä (todennäköisesti NMEA 0183: sijainti DSC:lle sisään) | 0183 GPS sisään | olemassa | [current-system 3.2](../current-system.md#32-komentosillalta-ohjattavat-24-vn-laitteet) |
| – | Tutka | masto | yleensä Ethernet; suunta N2K:sta | – | omistajan lista | [current-system 3.4](../current-system.md#34-maston-ja-katon-varustelu) |

### 3.3 Kone ja vaihteisto

| Tunnus | Mittaus | Paikka | Liitäntä | PGN:t / tieto | Tila | Lähde |
|---|---|---|---|---|---|---|
| (N-03) | Kierrokset: **vauhtipyörän kotelossa on valmis paikka magneettianturille, mutta anturia ei ole** [omistaja 2026-11-08]; suositus [arvio] asentaa siihen magneettinen tai Hall-kierrosanturi, joka laskee käynnistyshammaskehän hampaita (hammaskehässä **126 hammasta**, SAE No. 3 -kotelo [omistaja 2026-11-08, koneen manuaali]; anturipaikan kierteen koko **⚠ ei tiedossa**). Taajuus = 126 × rpm / 60: käynnistyksessä noin 150 rpm → noin 315 Hz, tyhjäkäynti 700 rpm → 1 470 Hz, suurin 2400 rpm → 5 040 Hz [laskelma]; ESP32:n pulssilaskuri (PCNT) riittää hyvin. Varavaihtoehto laturin W-liitäntä (epätarkempi, riippuu hihnasta ja välityksestä); öljynpaine ja jäähdytysnesteen lämpötila (omat anturit; nykyisten mittarien anturien rinnalle kytkeminen voi vääristää mittarien lukemia **⚠ tarkista**), käyttötunnit laskettuna kierroksista. Polttoaineen kulutus vain erillisellä virtausmittarilla | CAT 3126B | node | 127488, 127489 | ehdotus | [omistaja 2026-11-08] |
| N-20 | Koneen ja vaihteiston lisäanturit: vaihteiston öljynpaine ja -lämpötila, pakosarjan tai pakokaasun lämpötila, merivesivirtaus / impellerihälytys | konehuone | node | 127493, 130312/130316 | ehdotus | – |
| (N-30) | Konehuoneen lämpötila ja kosteus (BME280) | konehuone | `node1` | 130311 | olemassa | [vega-n2k-node1] |

Kierroslukitusta hydrauliikka ei enää tarvitse (PVH57, [requirements §10.2](../../hydraulics/requirements.md#102-ohjaus)),
mutta kierrokset ovat hyödyllisiä lokitukseen ja hydrauliikan vianetsintään.

#### Kierrosanturin valinta (lisätty 2026-11-08)

Vauhtipyörän kotelon tyhjään anturipaikkaan, 126 hammasta (ks. yllä).

| | **A. Passiivinen magneettianturi (VR, magnetic pickup)** (suositus [arvio]) | B. Aktiivinen Hall-anturi (gear tooth sensor) |
|---|---|---|
| Johtimet ja syöttö | 2 johdinta, ei syöttöä; anturi tuottaa itse vaihtojännitteen | 3 johdinta, syöttö (tyypillisesti 5–24 V) |
| Signaali | siniaalto, jonka amplitudi kasvaa kierrosten mukana (hitaalla pieni) | kanttiaalto, toimii myös hyvin hitaalla |
| Liitäntä ESP32:een | tarvitsee VR-rajapintapiirin, esim. **MAX9924** (mukautuva kynnys ja nollakohdan tunnistus, −40…+125 °C) ([Analog Devices](https://www.analog.com/en/products/max9924)); piirin syöttö 4,5–5,5 V, joten lähtö sovitetaan ESP32:n 3,3 V:iin **⚠ tarkista** datalehdestä | avokollektorilähtö ja ylösvetovastus suoraan ESP32:n tuloon |
| Maadoitus (kohta 5.5a) | kelluva, joten node voi saada virtansa väylästä | anturin miinus voi yhdistyä runkoon, jos kotelo on kytketty siihen sisäisesti **⚠ tarkista**; muuten noden virta 24 V:sta |
| Kestävyys | yksinkertaisin ja kestävin, yleinen dieselmoottoreissa ja aggregaateissa | elektroniikkaa anturin kärjessä; lämpöluokka tarkistettava |

**Kierre:** SAE-vauhtipyörän kotelon anturipaikoissa yleinen kierre on **5/8"-18 UNF**, mutta
Vegan kotelon kierre **⚠ ei tiedossa** (mitataan tai luetaan tulpasta). Esimerkkejä 5/8"-18 UNF
-magneettiantureista: Murphy (Enovation Controls) MP-sarja
([Enovation](https://enovationcontrols.com/products/magnetic-pickups/)), aggregaattien
varaosa-anturit kuten GAC MSP6728C ([Fridayparts](https://www.fridayparts.com/msp6728c-magnetic-speed-pickup-sensor-engine-pick-up-5-8-18-unf-2a-threaded)).
Hintoja **⚠ ei tarkistettu**. Tarkista myös anturin pituus: kärjen pitää ulottua hampaisiin
lukkomutterin kanssa.

**Asennus (Murphyn ohjeen mukaan):** kierretään sisään, kunnes kärki koskettaa hampaan
päätä (kone pysähdyksissä), avataan 1/4–3/4 kierrosta ja lukitaan mutterilla. 5/8"-18:lla
noin 1/2 kierrosta antaa noin 0,7 mm:n välin
([Murphy / Enovation](https://support.enovationcontrols.com/hc/en-us/articles/115001361834-MP-Series-Magnetic-Pickups-Speed-Time-Sensors-Instruments);
taulukon arvot **⚠ tarkista** ohjeesta). Väli valitaan niin, että jännite riittää käynnistyskierroksilla.
Pyöräytä konetta koko kierros ennen käynnistystä, ettei kärki osu heittävään hampaaseen.

**Kaapeli:** suojattu parikaapeli, suojavaippa maahan vain noden päässä; erillään käynnistysmoottorin
ja laturin kaapeleista.

### 3.4 Sähköjärjestelmä

| Tunnus | Laite / mittaus | Paikka | Liitäntä | PGN:t / tieto | Tila | Lähde |
|---|---|---|---|---|---|---|
| N-21 | Akkumittaus (INA226 ja 0,15 mΩ:n shuntti, DS18B20-lämpötila) | akusto | `node2` | 127508, 127506 | olemassa (käyttöakut purettu, joten mittauskohde **⚠ tarkista**) | [vega-n2k-node2] |
| (N-02) | Käyttöakusto (2 × 8S, JK-BMS), MultiPlus-II, lataus | konehuone | Cerbo GX:n kautta | 127506, 127508, 127509 tms. | suunniteltu | [inverter-bms](inverter-bms.md) |
| N-22 | Käynnistysakkujen jännite ja hälytys (myös P3:n käydessä) | käynnistysakut | node tai PDM:n VBAT_SENSE | 127508 | suunniteltu (avoin kysymys) | [dc-distribution](dc-distribution.md#8-avoimet-kysymykset) |
| N-23 | Tärkeiden kuormien kiskon (TK) molempien syöttöjen jännite (diodivian havaitseminen) | PJ / TK | node | 127751 | suunniteltu | [dc-distribution 3](dc-distribution.md#3-tärkeät-kuormat-ja-vikatilanteet) |
| N-24 | Pilssi- ja ylävesihälytin Rule 32ALA, kosketin | pilssi | node, digitaalitulo | Signal K -hälytys (127501 tila) | suunniteltu | [procurement 4.8](../procurement.md) |
| N-25 | Pilssipumppujen käynti ja käyntiaika (3 kpl) | pilssi | PDM (pakotetun käytön lähtö näkee jännitteen) | 127501 / Signal K | suunniteltu | [dc-distribution 3](dc-distribution.md#3-tärkeät-kuormat-ja-vikatilanteet) |
| N-26 … | ESP32-PDM-kortit, noin 6 + 2 kpl (valot, pumput, puhaltimet, hydrauliikan kelat) | KS, KH | N2K (CAN-piiri CA-IS3050G, erotettu; LEN 1) | 127501/127502 (kytkinpankki), virrat ja viat | suunniteltu (PDM päätetty 2026-10-31) | [procurement 3.8](../procurement.md), [ESP32-PDM](https://github.com/plektra/ESP32-PDM) |
| N-27 | Maasähkö (jännite, virta, onko kytketty) | maasähkön tulo | Cerbo GX (MultiPlus-II:n AC-tulo) | 127503 tms. | ehdotus | – |
| – | Laturin säädin Alpha Pro III | konehuone | ei väylää (Reg on -johdin) | – | päätetty | [decisions 2026-10-31](../../decisions.md) |

### 3.5 Hydrauliikka

Kaikki hydrauliikan mittaukset menevät ESP32-PDM:lle tai omalle nodelle, joka lähettää ne
väylään ja Signal K:hon ([pressure-monitoring](../../hydraulics/design/pressure-monitoring.md),
[requirements §10.1](../../hydraulics/requirements.md#101-anturit)).

| Tunnus | Mittaus | Alue / signaali | PGN:t / tieto | Tila | Lähde |
|---|---|---|---|---|---|
| 3B1 | Öljyn lämpötila | 0–100 °C; varoitus 65 °C, hälytys 70 °C | 130316 | suunniteltu (päätetty 2026-10-23) | [decisions](../../decisions.md) |
| 2B1 | P2:n imupaine | −1…+1 bar, 4–20 mA | 130314 | suunniteltu (päätetty 2026-10-23) | sama |
| 2B2 | P2:n lähtöpaine | 0–400 bar, 4–20 mA | 130314 | ehdotus, prioriteetti 1 | [pressure-monitoring](../../hydraulics/design/pressure-monitoring.md#suositus) |
| 1B2 | Ohjauspaine | 0–250 bar | 130314 | ehdotus | sama |
| – | Öljynpinta, suodattimen paine-ero | % / kytkin | 127505 / 127501 | auki (TBD) | [requirements §10.1](../../hydraulics/requirements.md#101-anturit) |
| – | PVEH:n vikasignaali, joystickin asento | digitaali / analogia | Signal K | suunniteltu | [bow-thruster-control](../../hydraulics/design/bow-thruster-control.md) |
| – | Ohjauslähdöt: PVEO, BAV-713:n kelat, PVEH:n sallintarele | PDM-lähdöt | 127502 | suunniteltu | [schematic](../../hydraulics/schematic.md) |

**Keulapotkurin ohjaus ei kulje väylän kautta.** Joystick ohjaa PVEH:ta suoraan johdotettuna;
PDM vain valvoo ja voi pudottaa sallinnan ([bow-thruster-control 4](../../hydraulics/design/bow-thruster-control.md#4-suositus-arvio-suora-joystick-ja-esp32-pdm-valvojana)).

### 3.6 Säiliöt

| Tunnus | Mittaus | Liitäntä | PGN | Tila | Lähde |
|---|---|---|---|---|---|
| N-40 | Polttoainemittari(t): päivätankki, myöhemmin bunkkerit | N2K tai node (vastusanturi / painesensori) | 127505 | omistajan lista; polttoainejärjestelmä kesken | [omistaja 2026-10-29] |
| N-41 | Käyttövesi | node | 127505 | ehdotus | – |
| N-42 | Harmaavesisumppu ja septi (täyttöaste, hälytys ennen täyttymistä) | node | 127505 | ehdotus | [loads.yaml](../loads.yaml) |

### 3.7 Olosuhteet, lämmitys ja turvallisuus

| Tunnus | Mittaus / laite | Liitäntä | PGN | Tila | Lähde |
|---|---|---|---|---|---|
| N-30 | `node1`: konehuoneen lämpötila, kosteus ja ilmanpaine (BME280); kotelon lämpötila (DS18B20); kolmen DC-releen ja AC-releen tila; Raspberry Pi:n virran tila ja sammutus | node | 130311, 130312, 127501, 127502 | olemassa | [vega-n2k-node1] |
| N-31 | Tilojen lämpötilat (hytit, komentosilta), lämmityksen menovesi | node(t), DS18B20 | 130312 / 130316 | ehdotus | [heating](../../heating/current-system.md) |
| N-32 | Ulkolämpötila (hakuvalon jäänpoiston automatiikka tarvitsee) | node | 130312 | ehdotus | [searchlight-deicing](searchlight-deicing.md) |
| N-33 | Kaasuhälytin ja kaasun magneettiventtiilin tila | node, digitaalitulo | Signal K -hälytys | ehdotus (suositus jo dc-distributionissa) | [current-system 5](../current-system.md#5-avoimet-kysymykset) |
| N-34 | Savu- ja häkävaroittimet, konehuoneen palohälytys | node, digitaalitulo | Signal K -hälytys | ehdotus | – |

### 3.8 Ohjaimet ja käyttöliittymät

| Laite | Ohjaa | Liitäntä | Tila |
|---|---|---|---|
| PDM-korttien paneelikytkimet (komentosilta, konehuone) | valot, pumput, puhaltimet | suoraan PDM:n tuloihin; toimivat ilman väylää | suunniteltu |
| Signal K / puhelin / navigointitietokone | PDM-lähdöt etänä (127502), hälytysten kuittaus | verkko → Signal K → N2K | suunniteltu |
| Keulapotkurin joystick | PVEH | suora johdotus, ei väylää | suositus |
| Autopilotin ohjauspaneeli | autopilotti | N2K | omistajan lista (mahdollinen) |
| Hydrauliikan hätäseis | PVE-syöttö | johdotettu, ei väylää | suunniteltu |

### 3.9 Väylävirran arvio (LEN)

1 LEN = 50 mA. Tiedossa vain ESP32-PDM: LEN 1 (49,3 mA, mitataan prototyypistä)
[ESP32-PDM ARCHITECTURE]. Nodeista 1–3 ja kaupallisista laitteista LEN **⚠ ei tiedossa**.

**Karkea arvio [arvio]:** 8 PDM:ää (8 LEN), noin 6 omaa nodea (oletus 2 LEN kpl, 12 LEN),
GNSS, tuuli, peräsinkulma, kompassi, kaiku ja polttoainemittari (oletus 1–3 LEN kpl, noin
10 LEN) → noin 30 LEN ≈ **1,5 A**. AIS ja autopilotti otetaan yleensä omasta syötöstä. Micro-C-
kaapeli kestää 3 A syöttöpisteen kummallekin puolelle ([Actisense](https://actisense.com/news/3-fundamentals-of-designing-an-nmea-2000-network/)),
joten yksi syöttöpiste riittää. Lasketaan uudelleen, kun laitteet valitaan.

## 4. Väylät erillään

| Väylä | Nopeus | Laitteet | Liitos muihin |
|---|---|---|---|
| **NMEA 2000** | 250 kbit/s | kohdan 3 laitteet, PDM:t, nodet, Signal K | – |
| **BMS-CAN** (Victron) | 500 kbit/s | 2 × JK-BMS ↔ Cerbo GX:n BMS-CAN-portti | Cerbo GX välittää tiedot Signal K:hon ja tarvittaessa VE.Can/N2K:hon |
| ~~J1939~~ | – | ei käytössä: koneessa ei todennäköisesti ole väylää [omistaja 2026-11-08] | – |
| ~~PVE-CAN~~ | – | ei käytössä: PVEH ohjataan jännitteellä | – |

**Miksi erillään [arvio]:**
- BMS-CAN on eri nopeudella ja eri protokollalla; JK-BMS:n liittäminen N2K-runkoon kaataisi koko
  väylän. Akun suojaus ei saa riippua navigointiväylän kunnosta, eikä päinvastoin.
- Jos koneessa sittenkin on J1939-väylä, se on koneen ohjauksen väylä, eikä sitä liitetä N2K:hon
  suoraan, vaan vain kuuntelevan yhdyskäytävän kautta (esim. Maretron J2K100).
- Jos joskus tulee CAN-ohjattu PVE, se laitetaan omaan väylään tai yhdyskäytävän taakse.

**Cerbo GX ja N2K:**
- **Alkuperäisen Cerbo GX:n VE.Can-portit eivät ole galvaanisesti erotettuja; Cerbo GX MK2:ssa
  (2024) portti 1 on erotettu** ([Victron Marine Integration Guide](https://www.victronenergy.com/media/pg/Cerbo_GX/en/connecting-supported-non-victron-products.html),
  [Victron VE.Can ja NMEA 2000](https://www.victronenergy.com/live/ve.can:nmea-2000:start)).
  Kun Cerbo tilataan, kannattaa valita **MK2** ja kytkeä N2K porttiin 1. **Omistaja pitää MK2:ta
  hyvänä ajatuksena** [omistaja 2026-11-08]; hankintalistan rivi 2.2 on päivitetty MK2:ksi
  (**⚠ tarkista** hinta, saatavuus ja että MK2:ssa on edelleen BMS-CAN-portti).
- **VE.Can → NMEA 2000 -kaapelissa on irrotettava sulake.** Sulake paikallaan Victron syöttää
  N2K-väylää akkujännitteellä, eli Vegassa 24 V:lla. **Sulake poistetaan**, ja väylä saa virtansa
  omasta syötöstään (kohta 5.1).
- Vaihtoehto: Cerbo GX:ää ei liitetä N2K:hon lainkaan, vaan Victronin tiedot luetaan Signal K:hon
  verkon kautta. Se on yksinkertaisin ja poistaa maadoitussilmukan riskin; N2K-liitäntä tarvitaan
  vain, jos jokin N2K-näyttö haluaa akkutiedot suoraan.

## 5. Luotettavan väylän suunnitteluperiaatteet

### 5.1 Väylän jännite ja syöttö

**Ongelma:** NMEA 2000 on 12 V:n järjestelmä (laitteiden pitää toimia noin 9–16 V:lla, **⚠ tarkista**
standardista). 24 V:lla toimivat vain laitteet, joiden datalehti sen sallii, eikä 24 V:n syöttö
ole N2K-käytäntö. Lisäksi ESP32-PDM on suunniteltu enintään 16 V:n väylälle (kohta 1).

| | **A. Väylälle 12 V erotetulla 24→12 V -muuntimella** (suositus [arvio]) | B. Pidetään 24 V |
|---|---|---|
| Kaupalliset N2K-laitteet | kaikki käyvät | vain 9–32 V:n laitteet; jokainen tarkistettava |
| ESP32-PDM | sellaisenaan | CAN-puolen TVS-diodi (SMAJ18CA) ja jännitemarginaalit suunniteltava uudelleen, LEN-laskelmat ja F3-suoja tarkistettava |
| Omat nodet 1–2 | toimivat (LM7805) | toimivat (LM7805 enintään 35 V); häviöteho kasvaa, **⚠ tarkista** lämpeneminen |
| Erotus | muunnin erottaa väylän miinuksen akun miinuksesta (yksi yhteyspiste, kohta 5.4) | sama syöttö kuin NUC:lla ja kameroilla; häiriöt ja viat yhteisiä |
| Lisäkustannus | muunnin ja sulake, arviolta muutamia kymmeniä euroja (**⚠ ei tiedossa**) | PDM:n uudelleensuunnittelu |

**Ehdokkaita muuntimeksi** (**⚠ tarkista** datalehdestä: erotus, tulojännitealue vähintään noin
18–32 V, jännitteen alenema koneen käynnistyksessä):
- **Victron Orion-Tr 24/12-9 (erotettu)**: sopii samaan Victron-kokonaisuuteen.
- **Mean Well DDR-60G-12** tai vastaava DIN-kiskomuunnin, samaa sarjaa kuin nykyiset DDR-15G-5 ja
  DDR-240B-24.

Teho riittää: kohdan 3.9 arviolla noin 1,5 A × 12 V ≈ 20 W [laskelma].

**Syötön paikka:** väylä on jatkuvasti päällä oleva kuorma, joten se kytketään jatkuvien kuormien
ryhmään ([dc-distribution](dc-distribution.md)) omalla sulakkeellaan (N2K-käytännössä noin 3 A
Micro-C:lle, **⚠ tarkista** valitun syöttö-T:n ohjeesta). Ei PDM-lähdön taakse: PDM:t ohjataan
väylän kautta, joten väylä ei saa olla niiden varassa. Harkitaan TK-kiskoa, jos pilssihälytys
kulkee väylän kautta (kohta 6).

### 5.2 Topologia

- **Yksi suora runkoväylä** (ei tähteä, ei haarautuvaa runkoa). Laitteet liitetään T-kappaleilla
  lyhyillä pudotuksilla.
- **Päätevastus 120 Ω vain runkoväylän kummassakin päässä**, T-kappaleen sivuun, ei pudotuksen
  päähän eikä laitteeseen ([Actisense](https://actisense.com/news/3-fundamentals-of-designing-an-nmea-2000-network/),
  [Garmin](https://www8.garmin.com/manuals/webhelp/GUID-1415AAD0-FE63-42A6-8F8D-DB713D616122/EN-US/GUID-BE4F5395-A9B1-4A50-A028-CC0D77AFB288.html)).
  Tarkistus: virrat pois, CAN-H–CAN-L-vastus mitattuna ≈ **60 Ω**. Jos lukema on noin 120 Ω,
  yksi päätevastus puuttuu; noin 40 Ω tarkoittaa, että vastuksia on yksi liikaa.
- **Rajat Micro-C-kaapelilla:** runkoväylä enintään 100 m, yksi pudotus enintään 6 m, pudotuksia
  yhteensä enintään 78 m, enintään 50 laitetta ([Actisense](https://actisense.com/news/3-fundamentals-of-designing-an-nmea-2000-network/),
  [Garmin](https://www8.garmin.com/manuals/webhelp/GUID-1415AAD0-FE63-42A6-8F8D-DB713D616122/EN-US/GUID-D30B8240-E352-4F53-89CD-3E7DFD78FCAF.html)).
  16-metrisessä Vegassa rajat eivät tule vastaan, mutta mastopudotus kannattaa mitata (tuulianturi
  mastossa, **⚠ tarkista** pituus; yli 6 m:n pudotuksen tilalle runkoväylän jatke mastoon ja
  päätevastus maston huipulle).
- **Ehdotettu reitti [arvio]:** konehuone (Signal K, Cerbo, PDM:t, nodet, syöttöpiste) →
  komentosilta (PDM:t, GNSS, AIS, autopilotti, näytöt) → masto (tuuli). Laitteita on noin
  puolet kummassakin päässä, joten syöttö sopii konehuoneen ja komentosillan väliin. Reitti
  piirretään, kun keskusten paikat päätetään ([dc-distribution 8](dc-distribution.md#8-avoimet-kysymykset)).

### 5.3 Kaapelit ja liittimet

- **Valmiit NMEA 2000 Micro-C -kaapelit (M12, 5-napainen, suojavaippa ja drain) ja T-kappaleet**
  konehuoneessa, kannella ja mastossa. Ne ovat tiiviitä ja yhteensopivia; märkä tila ja tärinä
  ovat tavallisimmat vikojen syyt.
- **Omat laitteet koteloon Micro-C-paneeliliittimellä**, jolloin kotelon sisällä riittävät
  ruuviliittimet (ESP32-PDM:n J4 on 4-napainen ilman suojaa, ja se on tarkoituksella tehty niin).
- Ei kierrettyjä jatkoksia eikä ruuviliitinrimoja kannella tai pilssin lähellä. Jos runkoa
  jatketaan kaapelilla, käytetään valmiita päitä tai asennettavia Micro-C-liittimiä.
- Pidä erillään VHF:n koaksiaalista ja suurvirtakaapeleista (ESP32-PDM:n asennusohje).
- Pudotus enintään 6 m (ESP32-PDM:n asennusohje).

### 5.4 Maadoitus ja erotus

- **Väylän miinus ja suojavaippa yhdistetään runkoon / akun miinukseen vain yhdessä kohdassa,
  syöttöpisteessä** (sama periaate kuin ESP32-PDM:n ohjeessa). Erotettu muunnin (kohta 5.1) tekee
  tästä hallittua.
- **Laitteiden pitää olla erotettuja.** Omat nodet (ISO1044) ja ESP32-PDM (CA-IS3050G) ovat.
  Erottamattomat laitteet, kuten alkuperäisen Cerbo GX:n VE.Can, yhdistävät väylän miinuksen
  oman syöttönsä miinukseen. Silloin akun miinusvirta voi kulkea väylän kautta (maadoitussilmukka),
  mikä aiheuttaa häiriöitä ja pahimmillaan kuumentaa väylän ohuita johtimia [arvio].
- Signal K -palvelimen CAN-liitäntä on erotettu: Waveshare 2-CH CAN HAT, jossa digitaalinen
  erotin ja erotettu DC/DC-muunnin [omistaja 2026-11-08], [datalehti Waveshare 2-CH CAN HAT](https://www.waveshare.com/wiki/2-CH_CAN_HAT).
  Kortin `G`-liitin on erotettu maa; se kytketään väylän miinukseen (NET-C), ei Pi:n maahan.
- **Kortin 120 Ω:n päätevastus (jumpperi)** on päällä vain, jos Pi on runkoväylän päässä. Jos Pi
  liitetään pudotuksella keskeltä väylää, jumpperi otetaan pois, muuten väylässä on kolme
  päätevastusta (mittaus noin 40 Ω, kohta 5.2).
- Kortti liitetään 4-napaisella ruuviliittimellä; se pitää viedä koteloon Micro-C-
  paneeliliittimellä ja lyhyellä pudotuksella kuten omat nodet (kohta 5.3). Väylänopeus asetetaan
  250 kbit/s (`ip link set can0 up type can bitrate 250000`); wikin esimerkeissä on 1 Mbit/s.

### 5.5 Osoitteet, instanssit ja ohjelmisto

- **Jokaisella laitteella oma yksilöllinen numero** (NAME / unique number). Omissa nodeissa se
  on nyt kovakoodattu (`SetDeviceInformation(1…)`, `(2…)`); PDM:issä ja uusissa nodeissa se
  kannattaa johtaa ESP32:n MAC-osoitteesta, jotta kaksi samalla ohjelmalla flashattua korttia
  eivät riitele osoitteesta.
- **Laitteen toimintoluokka oikein:** `node2` ilmoittaa olevansa lämpötila-anturi (function 130),
  vaikka se lähettää akkutietoja; oikea olisi akkuluokka (**⚠ tarkista** koodi NMEA:n
  luokkataulukosta). Ei estä toimintaa, mutta näytöt ja Signal K näyttävät laitteen oudosti.
- **Instanssitaulukko.** Samaa tietotyyppiä lähettävät laitteet erotetaan instanssilla: akut
  (127508 battery instance), lämpötilat (130312 instance + source), säiliöt (127505), kytkinpankit
  (127501/127502 bank instance). `node1` käyttää jo kytkinpankkeja 1 ja 2, joten PDM:t saavat
  muut numerot. **Ehdotus:** perustetaan taulukko (esim. tähän dokumenttiin tai
  `electrics/n2k-instances.yaml`), kun ensimmäiset PDM:t otetaan käyttöön.
- **Väyläkuorma:** 250 kbit/s riittää hyvin, kun omat laitteet lähettävät hitaita arvoja
  (lämpötilat, säiliöt) noin 1–10 s:n välein ja vain nopeat (kierrokset, peräsinkulma, suunta)
  tiheämmin. Tavoite alle noin 30–40 %:n kuorma [arvio]; mitataan Signal K:sta tai
  CAN-analysaattorilla.
- **Ohjelmistopäivitykset (OTA)** eivät saa jättää nodea lähettämään jatkuvasti; CAN-piirien
  TXD-aikakatkaisu (CA-IS3050G 2–8 ms) estää yhtä laitetta jumittamasta väylää pysyvästi.

### 5.5a Nodejen virransyöttö (lisätty 2026-11-08)

**Perussääntö [arvio]: anturinode ottaa virtansa väylästä**, eli samasta Micro-C-pudotuksesta,
jossa data kulkee. Erillistä syöttöä ei tarvita, ja väylän yksi sulake ja yksi maadoituspiste
pysyvät hallittuina. Rajoja on kaksi: väylän virta (kohta 3.9) ja maadoitus.

**Maadoitus ratkaisee.** Väylästä syötetyn noden maa on väylän miinus (NET-C). Jos noden anturi
on kytketty runkoon, koneeseen tai akun miinukseen, väylän miinus yhdistyy runkoon toisesta
kohdasta, ja syntyy maadoitussilmukka (kohta 5.4).

| Noden tyyppi | Syöttö | Esimerkit |
|---|---|---|
| **Anturit kelluvat** (eivät koske runkoon eikä akun miinukseen) | **väylästä** | DS18B20 ja BME280 (node1, tilojen lämpötilat), kaksijohtiminen magneettinen kierrosanturi, tuulianturi, potentiometrinen peräsinkulma-anturi, kuivakoskettimet (pilssihälytin, kaasuhälytin) |
| **Anturit viittaavat akun miinukseen tai runkoon** | **veneen 24 V:sta, ja CAN-puoli erotettu** (erotettu CAN-piiri, jonka väyläpuoli saa virtansa väylästä) | akun jännite ja shuntti (node2), käynnistysakkujen ja TK-kiskon jännitteet, koneen yksijohtimiset paine- ja lämpötila-anturit (runko maana), ESP32-PDM |
| **Paljon virtaa tai korkea jännite** | **veneen 24 V:sta** | 4–20 mA -anturit, jotka tarvitsevat yleensä vähintään noin 10–12 V silmukkajännitettä (12 V:n väylällä marginaali on pieni, **⚠ tarkista** anturin datalehdestä), lämmitetyt anturit, releitä ohjaavat nodet |

- **ESP32-PDM toimii jo näin:** ohjain ja lähdöt saavat virtansa akulta, ja vain erotettu CAN-puoli
  saa virtansa väylästä (LEN 1).
- **node1 ja node2:ssa on erotettu CAN-piiri (ISO1044).** Mistä niiden ohjainpuoli saa virtansa,
  **⚠ tarkista** kytkentäkaaviosta. node2 mittaa akkua, joten sen ohjainpuolen pitää saada virtansa
  akulta, ei väylästä.
- **Koneen anturinode N-03:** jos öljynpaine- ja lämpötila-anturit ovat yksijohtimisia ja niiden
  maa on koneen runko, node syötetään 24 V:sta erotetulla CAN-puolella. Jos anturit ovat
  kaksijohtimisia ja eristettyjä, väyläsyöttö riittää.
- Veneen 24 V:sta syötetty node tarvitsee oman sulakkeen, ja se kytketään jatkuvien kuormien
  ryhmään tai PDM-lähtöön. PDM-lähtö käy vain, jos noden saa sammuttaa.

### 5.6 Valvonta

- Signal K seuraa jokaisen laitteen heartbeat-viestiä (126993) ja hälyttää, kun laite katoaa.
- Väylän jännite mitataan **runkoväylän kaukaisesta päästä** (N-05); alenema kertoo huonosta
  liitoksesta tai liian suuresta kuormasta ennen kuin laitteet alkavat temppuilla.
- Väylän virheet (error frames, bus-off) lokiin: MCP2515 ja SocketCAN näyttävät virhelaskurit
  ja bus-off-tilan (`ip -details -statistics link show can0`), joten Signal K tai erillinen
  skripti voi hälyttää niistä [arvio, **⚠ tarkista** käytännössä].

## 6. Vikatilanteet

Väylä ei itse ole turvallisuuskriittinen, mutta sen kautta kulkee hälytyksiä ja ohjausta, joten
vikojen vaikutukset kirjataan. **Pätevän henkilön pitää tarkistaa hälytys- ja ohjausketjut ennen
käyttöönottoa.**

| Vika | Mitä tapahtuu | Mikä toimii silti / suojaus |
|---|---|---|
| Runkoväylä oikosulussa (CAN-H–CAN-L) tai poikki | Koko väylä tai osa siitä hiljenee: navigointitiedot, hälytykset Signal K:hon ja PDM:ien etäohjaus | PDM:ien paneelikytkimet toimivat ilman väylää (ESP32-PDM:n päätös 17); keulapotkuri, ohjaus, pilssipumppujen kohokytkimet ja hätäseis ovat johdotettuja. Signal K hälyttää kadonneista laitteista |
| Väylän syötön sulake palaa tai muunnin vikaantuu | Kaikki väylästä virtansa ottavat laitteet sammuvat (GNSS, tuuli, peräsinkulma, nodet) | Laitteet, joilla on oma syöttö (AIS, autopilotti, VHF), toimivat; autopilotti menettää peräsinkulman ja suunnan → kytkeytyy pois ja hälyttää, käsiohjaus orbitrolilla ([requirements](../../hydraulics/requirements.md)). Väylän jännitteen valvonta (N-05) |
| Päätevastus puuttuu tai on liikaa | Satunnaisia virheitä, laitteet katoavat ja palaavat | Tarkistus 60 Ω:n mittauksella käyttöönotossa ja muutosten jälkeen |
| Yksi laite lähettää jatkuvasti (jumi) | Väylä tukkeutuu | CAN-piirin TXD-aikakatkaisu; laite irrotetaan pudotuksesta |
| Kosteus liittimessä | Häiriöitä, korroosio, oikosulku | Micro-C-liittimet, tippalenkit, ei liitoksia pilssiin |
| Pilssi- tai ylävesihälytys kulkee vain väylän kautta | Väylävika estää etähälytyksen | Rule 32ALA:n paikallinen summeri toimii ilman väylää ([dc-distribution 3.4](dc-distribution.md#34-tärkeiden-kuormien-kiskon-osat-selvitetty-2026-10-31)); harkitse lisäksi 4G-modeemin digitaalituloa tai Cerbo GX:n relettä hälytykseen ilman N2K:ta |
| BMS-CAN katkeaa | Cerbo ei saa BMS:n rajoja | Victron pysäyttää latauksen (DVCC); JK:n kuivakosketin pysäyttää laturin ([decisions 2026-10-31](../../decisions.md)) — ei riipu N2K:sta |
| Maadoitussilmukka erottamattoman laitteen kautta | Häiriöitä; virtaa väylän miinusjohtimessa | Vain erotettuja laitteita; Cerbo GX MK2 portti 1; yksi maadoituspiste |
| 24 V:n jännite päätyy 12 V:n väylälle (esim. VE.Can-kaapelin sulake paikallaan) | 12 V:n laitteet ja PDM:n TVS-diodi voivat vaurioitua | Sulake pois VE.Can-kaapelista, merkintä kaapeliin; väylän jännitteen valvonta |

## 7. Suositus [arvio]

1. **Väylälle oma 12 V:n syöttö erotetulla 24→12 V -muuntimella** omalla sulakkeellaan jatkuvien
   kuormien ryhmästä. Nykyinen 24 V:n syöttö DDR-240B-24:stä poistetaan väylältä, ennen kuin
   ensimmäinen ESP32-PDM liitetään.
2. **Kaksi erillistä väylää:** N2K ja BMS-CAN. Koneen tiedot omalla anturinodella (N-03), koska
   koneessa ei todennäköisesti ole väylää.
3. **Cerbo GX MK2** alkuperäisen sijaan (omistaja kannattaa 2026-11-08), ja VE.Can-kaapelin sulake pois;
   tai Victron-tiedot Signal K:hon verkon kautta ilman N2K-liitäntää.
4. **Yksi suora runkoväylä** konehuoneesta komentosillalle (ja mastoon), valmiit Micro-C-kaapelit,
   päätevastukset päihin, syöttö keskelle.
5. **Instanssitaulukko ja yksilölliset tunnukset** omille nodeille ja PDM:ille ennen kuin niitä on
   enemmän kuin pari.
6. **Lisättäväksi listaan harkintaan:** kompassi / suunta-anturi (autopilotti ja tutka tarvitsevat)
   ja kaiku. Omistajat päättävät.

## 8. Avoimet kysymykset

- [ ] **Omistajat:** väylän jännite 12 V (suositus) vai 24 V? Jos 24 V, ESP32-PDM:n CAN-puoli
  pitää suunnitella uudelleen (kerrotaan ESP32-PDM-projektille). Omistaja harkitsee 12 V:ta
  [omistaja 2026-11-08].
- [ ] **Veneellä:** nykyisen runkoväylän reitti, pituus, kaapelityyppi, liittimet, päätevastusten
  paikat (mittaus 60 Ω) ja mitä laitteita siinä nyt on.
- [x] Miten Signal K -palvelin (Pi 5) liittyy väylään: eristetty Waveshare 2-CH CAN HAT [omistaja 2026-11-08]
- [ ] Pi:n paikka väylässä (pää vai keskellä) ja CAN HAT:n päätevastusjumpperin asento; HAT:n virrankulutus Pi:n 3 A:n syötöstä (DDR-15G-5) **⚠ ei tiedossa**
- [x] Onko CAT 3126B:ssä J1939-liitäntä: tuskin, eikä koneessa ole ohjainyksikköä (ECU); ilmeisesti
  MUI eli mekaaniset yksikköinjektorit [omistaja 2026-11-08] → omat anturit (N-03). Tyyppi
  **⚠ tarkista** tyyppikilvestä, ks. [vessel](../../vessel/README.md)
- [x] Kierrosanturin paikka: vauhtipyörän kotelossa on valmis paikka, anturia ei ole [omistaja 2026-11-08]
- [x] Käynnistyshammaskehän hampaat: 126 (SAE No. 3 -kotelo) [omistaja 2026-11-08, koneen manuaali]
- [ ] **Veneellä:** anturipaikan kierteen koko (kuva ja mitta tai tulpan merkinnät) ja etäisyys hampaisiin; niistä
  valitaan anturi
- [ ] Koneen anturit: omat
  öljynpaine- ja lämpötila-anturit vai nykyisten mittarien anturit
- [ ] Mastopudotuksen pituus tuulianturille (alle 6 m?).
- [x] Cerbo GX vai Cerbo GX MK2: MK2 hyvä ajatus [omistaja 2026-11-08]
- [ ] Liitetäänkö Cerbo N2K:hon (MK2:n portti 1) vai vain verkon kautta Signal K:hon.
- [ ] Muunnin 24→12 V: malli, hinta ja erotus (ehdokkaat kohdassa 5.1).
- [ ] Laitteiden mallit ja LEN-arvot: GNSS (valmis vai `node3`), AIS B, tuulianturi,
  peräsinkulma-anturi, polttoainemittarit.
- [ ] Tuleeko kompassi / suunta-anturi ja kaiku listaan (ehdotus N-14, N-15)?
- [ ] VHF Sailor RT2048:n liitäntä (NMEA 0183 vai N2K) ja tarvitseeko se GPS-sijainnin DSC:lle.
- [ ] `node2`:n nykyinen mittauskohde, kun käyttöakut on purettu.
- [ ] Instanssitaulukon paikka ja numerointi (kohta 5.5).
