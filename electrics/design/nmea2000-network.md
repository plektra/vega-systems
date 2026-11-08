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

> **Mihin nodeen mikäkin anturi ja ohjaus tulee:** kohta [3.11 Nodejako](#311-nodejako-lisätty-2026-11-08).

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
| N-04 | Itse toteutettu monitoiminäyttö | komentosillan kattopaneeli | Signal K:n kautta (Ethernet); oma N2K-liitäntä valinnainen (kohta 5.6a); toteutus [bridge-mfd](bridge-mfd.md) | – | omistajan lista | [omistaja 2026-11-08] |
| N-07 | Navigointitietokone ja noin 20":n näyttö, OpenCPN | komentosilta (paikka **⚠**) | Signal K:n kautta (Ethernet); valinnaisesti oma erotettu N2K-liitäntä (kohta 3.13) | lukee sijainnin, suunnan, AIS:n, syvyyden ja tuulen; voi lähettää reittipisteet autopilotille (129283, 129284, 129285) | omistajan suunnitelma | [omistaja 2026-11-08] |
| N-06 | Monitoiminäyttö Simrad NSS7 evo3 tai NSS9 evo3 (luultavasti) | komentosillan kattopaneeli | N2K Micro-C, 1 LEN; syöttö omasta 24 V:n piiristä (10–31,2 V); Ethernet tutkalle | kuuntelee navigointi- ja moottoritietoja, ohjaa autopilottia, jos Simrad-yhteensopiva | omistajan lista | [omistaja 2026-11-08], [datalehti Simrad NSS evo3](https://simrad-yachting.com/simrad/series/nss-evo3) |
| N-05 | Väylän valvontanode (jännite väylän kaukaisessa päässä, virheet) | runkoväylän pää | node | 127751 (DC-jännite/virta) tai Signal K | ehdotus | kohta 5.6 |

### 3.2 Navigointi

| Tunnus | Laite | Sijainti | Liitäntä | PGN:t / tieto | Tila | Lähde |
|---|---|---|---|---|---|---|
| N-10 | **GNSS/RTK: Unicore UM982 ja kaksi antennia** [omistaja 2026-11-08]: sijainti, nopeus, aika ja **suunta (heading)** antennien välisestä vektorista; suuntatarkkuus 0,1° (RMS) 1 m:n antennivälillä, päivitys 20 Hz [datalehti Unicore UM982](https://en.unicore.com/uploads/file/UM982_User%20Manual_EN_R1.7.pdf) | moduuli komentosillan katon alla, antennit katolla | oma GNSS-node **S7** (UART → N2K, kohta 3.11) | 129025, 129026, 129029, 126992, **127250 (true heading), 127251 (kääntymisnopeus)**, 127257 (pituuskallistus) | omistajan suunnitelma | [omistaja 2026-11-08] |
| N-11 | AIS, luokka B | komentosilta, antenni mastossa | N2K (useimmissa B-luokan laitteissa myös 0183/USB) | 129038, 129039, 129040, 129794, 129809, 129810 | omistajan lista | [omistaja 2026-10-29] |
| N-12 | Tuulianturi | masto | N2K (pudotus mastoon) | 130306 | omistajan lista | [omistaja 2026-10-29] |
| N-13 | Peräsinkulma-anturi | peräsinakseli | N2K tai node (potentiometri / Hall → ESP32) | 127245 | omistajan lista; autopilotti tarvitsee | [omistaja 2026-10-29], [hydraulics §10.1](../../hydraulics/requirements.md#101-anturit) |
| N-14 | Kompassi / suunta-anturi | – | – | 127250 | **UM982 korvaa** (N-10, kaksi antennia). Erillinen magneettinen suunta-anturi vain varalle, jos autopilotin halutaan toimivan GNSS-katkossa (ehdotus) | [omistaja 2026-11-08] |
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
| – | Ohjauslähdöt: PVEH:n sallintarele (keulapotkuri); PVEO vinssille ja painepesurille (myöhemmin, päälle/pois) | PDM-lähtö tai suora kytkin | 127502 | suunniteltu | [schematic](../../hydraulics/schematic.md) |

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

### 3.10 Omat vai valmiit laitteet (lisätty 2026-11-08)

**Periaate [arvio]:** valmis laite, kun kyse on anturin fysiikasta, mekaniikasta, säänkestosta tai
viranomaisvaatimuksista; oma laite, kun valmista ei ole tai kun kyse on Vegan omasta logiikasta.
Välimuotona avoin valmis ESP32-laitteisto (Hat Labs), johon tehdään vain oma ohjelmisto.

| Laiteryhmä | Suositus | Perustelu |
|---|---|---|
| Tuulianturi, kaiku ja loki | **valmis** N2K-laite | kalibrointi, säänkesto ja anturitekniikka; valmiit ovat edullisia verrattuna omaan työhön |
| GNSS ja suunta | **oma: UM982-moduuli, kaksi antennia ja oma node S7** [omistaja 2026-11-08] | RTK-tarkkuus ja GNSS-suunta (ei magneettista poikkeamaa teräsrungossa) edullisemmin kuin valmiina; vaatii oman N2K-ohjelmiston (kohta 3.11) |
| AIS (lähettävä, luokka B) | **valmis**, pakollisesti | lähettävän AIS-laitteen pitää olla tyyppihyväksytty |
| Autopilotti ja sen peräsinkulma-anturi | **valmis**, samaa järjestelmää (esim. Simradin, jos NSS valitaan) | turvallisuuskriittinen; peräsinkulma-anturi tulee yleensä autopilotin mukana |
| Simrad NSS, Cerbo GX, JK-BMS | valmis (päätetty tai suunniteltu) | – |
| Koneen anturit (kierrokset, öljynpaine, jäähdytysneste) | **välimuoto: Hat Labs HALMET** (ESP32, resistiiviset ja jännitetulot sekä pulssitulot, oma N2K-liitäntä, SensESP-ohjelmisto) ([docs](https://docs.hatlabs.fi/halmet/)); valmis vaihtoehto **Actisense EMU-1** (tukee magneettianturia, ±3…±60 V, 4–50 000 Hz; syöttö 9–35/40 V; noin 450–650 £/$, lisäksi Actisense-sovitin asetuksiin) ([Force 4](https://force4.co.uk/item/Actisense/EMU-1-Engine-Monitoring-Unit/ANJ), [Navstore](https://navstore.com/products/actisense-emu-1-engine-monitoring-unit-nmea-2000)) | HALMET on todennäköisesti selvästi halvempi ja sopii Signal K -ympäristöön; sopiiko sen pulssitulo suoraan passiiviselle magneettianturille, **⚠ tarkista** HALMETin laitteistodokumentaatiosta (muuten MAX9924-sovitin, ks. 3.3). **Hinta: HALMET 40,16 €, toistaiseksi loppuunmyyty; vaihtoehto SH-ESP32 32,63 €** [omistaja 2026-11-08], eli noin kymmenesosa EMU-1:n hinnasta. SH-ESP32:ssa ei ole valmiita anturitulojen sovituksia, joten anturien liitäntäpiirit (jännitejakajat, pulssitulon sovitin) tehdään itse lisäkortille [arvio] |
| Säiliöt (polttoaine, vesi, harmaa- ja septivesi) | **HALMET** (resistiiviset ja jänniteanturit) tai valmiit N2K-säiliöanturit | sama kortti voi lukea koneen ja säiliöiden anturit, jos ne ovat lähellä toisiaan |
| Lämpötilat, kosteus, kuivakoskettimet (pilssi- ja kaasuhälyttimet), jännitteet | **omat nodet** (nykyiset node1 ja node2, tai Hat Labs SH-ESP32 / HALMET -pohja) | yksinkertaisia ja halpoja; valmiit N2K-laitteet maksavat moninkertaisesti |
| Hydrauliikan anturit ja valvonta | **oma** (ESP32-PDM tai oma node) | valmista tuotetta ei ole; Vegan oma logiikka ja hälytysrajat |
| Tehonjako ja kytkimet | **oma ESP32-PDM** (päätetty 2026-10-31) | jo pitkällä omana projektina |

**SH-ESP32 vai oma vastaava kortti (lisätty 2026-11-08)? Suositus [arvio]: SH-ESP32 ja tarvittaessa oma
lisäkortti (HAT) anturien sovitukseen.**

- SH-ESP32 (32,63 € [omistaja 2026-11-08]) tarjoaa valmiina sen, mikä omassa kortissa on työläintä
  ja riskialtteinta: 8–32 V:n syötön ylijännitesuojineen, erotetun CAN-liitännän (ISO1050), ESD-
  ja EMC-suunnittelun (README: suunniteltu olemaan häiritsemättä VHF:ää ja GPS:ää) sekä valmiin
  ohjelmistotuen (SensESP, NMEA2000-kirjasto) ja dokumentaation ([SH-ESP32-hardware](https://github.com/hatlabs/SH-ESP32-hardware)).
- Oma ohjainkortti maksaisi piirilevytehtaalla osina ehkä saman verran tai vähemmän, mutta
  suunnittelu, prototyypit ja testaus vievät viikkoja, ja virheet näkyvät vasta veneessä. ESP32-PDM:n
  kokemus näyttää, kuinka paljon pelkkä syöttö-, CAN- ja suojaussuunnittelu vaatii.
- **Vegan omat tarpeet** (MAX9924-kierrostulo, 4–20 mA -tulot, jännitejakajat, releet) tehdään
  **SH-ESP32:n päälle tulevalle lisäkortille**. Hat Labs julkaisee siihen valmiin KiCad-pohjan
  (`SH-ESP-HAT-Blank`, `SH-ESP-HAT-Proto`). Lisäkortti on yksinkertainen, eikä siinä ole syöttöä
  eikä CAN-väylää.
- **Oma täysi kortti kannattaa vasta,** jos nodeja tarvitaan kymmeniä, kotelo tai liittimet eivät
  sovi, tai jos ESP32-PDM:n jaetuista piirilevylohkoista (ohjain, syöttö, CAN) halutaan tehdä
  anturinode samalla suunnittelulla. Silloin ESP32-PDM:n 24 V:n väyläkysymys (kohta 5.1) pitää
  ratkaista ensin.
- **Huom. syöttö ja maadoitus (kohta 5.5a):** SH-ESP32:n ohjainpuoli saa virtansa omasta
  8–32 V:n tulostaan, ja vain CAN-puoli on erotettu. Akkuun tai runkoon kytketyt anturit:
  syöttö veneen 24 V:sta (oikea tapa). Kelluvat anturit: syöttö voidaan ottaa myös väylästä
  (NET-S ja NET-C), jolloin erotus ohitetaan, mikä on hyväksyttävää vain, jos mikään anturi ei
  koske runkoon [arvio].

**Omien laitteiden hinta ei ole vain osien hinta [arvio]:**

- **Ylläpito ja henkilöriippuvuus.** Omat laitteet tarvitsevat ohjelmistopäivitykset, dokumentaation
  ja varaosat. Molempien omistajien pitää pystyä vaihtamaan viallinen node, myös sen, joka ei ole
  rakentanut sitä. Siksi kannattaa käyttää **yhtä yhteistä node-alustaa** (sama kortti, sama
  ohjelmistopohja, esim. SensESP ja NMEA2000-kirjasto) eikä tehdä jokaiselle mittaukselle omaa
  piirilevyä. Pidä vähintään yksi valmiiksi ohjelmoitu varanode.
- **Sertifiointi.** Omat laitteet eivät ole NMEA-sertifioituja. Vakio-PGN:t näkyvät yleensä myös
  kaupallisissa näytöissä, mutta Simradin kanssa se **⚠ tarkista** käytännössä (esim. lämpötilat ja
  kytkinpankit). Hydrauliikan kaltaiset Vega-kohtaiset tiedot näytetään omalla näytöllä Signal K:n
  kautta ([bridge-mfd](bridge-mfd.md)).
- **Laatu.** Omissa laitteissa samat säännöt kuin valmiissa: erotettu CAN-puoli (kohta 5.5a),
  Micro-C-liitin koteloon, yksilöllinen tunnus ja instanssit (kohta 5.5), käänteisnapaisuus- ja
  ylijännitesuojaus.

### 3.11 Nodejako (lisätty 2026-11-08)

Ehdotus [arvio], ei päätetty. **Periaatteet:**

1. **Sijainnin mukaan:** node on lähellä antureitaan, jolloin anturijohdot ovat lyhyitä ja vain
   NMEA 2000 -kaapeli kulkee pitkälti.
2. **Toiminnot erillään:** hydrauliikalla, koneella ja sähköllä on omat nodensa, jotta esimerkiksi
   hyttinoden vika tai ohjelmistopäivitys ei vie hydrauliikan valvontaa.
3. **Syöttö maadoituksen mukaan** (kohta 5.5a): *väylä* = kelluvat anturit, syöttö väylästä;
   *24 V* = runkoon tai akkuun kytketyt anturit tai 4–20 mA, syöttö veneen 24 V:sta omalla
   sulakkeella, CAN-puoli erotettu.
4. **Alusta:** HALMET koneelle ja säiliöille, SH-ESP32 muille, tarvittaessa oma lisäkortti
   (kohta 3.10). **ESP32-PDM:ssä ei ole 4–20 mA- eikä vapaita analogiatuloja** (vain 4 kytkintuloa,
   NTC ja oma syöttöjännite, [ESP32-PDM ARCHITECTURE](https://github.com/plektra/ESP32-PDM/blob/main/docs/ARCHITECTURE.md)),
   joten PDM:t hoitavat lähdöt ja paneelikytkimet, eivätkä ne lue antureita.

Sijainnit, joita ei vielä tiedetä (säiliöt, keittiö, hytit, ohjausventtiilien paikka), on merkitty
**⚠**. Jako tarkistetaan, kun keskusten paikat päätetään.

#### Omat anturinodet

| Node | Alusta | Sijainti | Syöttö | Anturit ja tulot | Ohjaukset ja lähdöt | Tila |
|---|---|---|---|---|---|---|
| **S1 Kone** (N-03) | HALMET (tai SH-ESP32 ja lisäkortti) | konehuone, koneen kylki | 24 V (koneen anturit ovat koneen rungossa) | kierrokset (magneettianturi, 126 hammasta); öljynpaine; jäähdytysnesteen lämpötila; vaihteiston öljynpaine ja -lämpötila (N-20); merivesivirtauksen tai impellerin hälytys (N-20); pakokaasun lämpötila (N-20, termopari vaatii vahvistimen lisäkortille); päivätankin pinta (N-40), jos tankki on konehuoneessa **⚠** | – | ehdotus |
| **S2 Hydrauliikka** | SH-ESP32 ja oma lisäkortti (4 × 4–20 mA, digitaalitulot) | konehuone, hydrauliikkasäiliön ja PVG 32:n lähellä **⚠** | 24 V (4–20 mA -silmukat) | 3B1 öljyn lämpötila; 2B1 P2:n imupaine; 2B2 P2:n lähtöpaine; 1B2 ohjauspaine; öljynpinta; suodattimen paine-erokytkin; PVEH:n vikasignaali; P3-varapumpun käynti (kontaktorin apukosketin) | – (lähdöt hydrauliikan PDM:llä, alla) | ehdotus |
| **S3 Sähkö** (node2 uudistettuna tai SH-ESP32) | node2 / SH-ESP32 | konehuone, pääjakelu (PJ) | 24 V **TK-kiskosta**, jotta mittaus toimii, vaikka käyttöakusto kytkeytyy irti | käynnistysakkujen jännite (N-22); TK-kiskon molempien syöttöjen jännitteet (N-23); pilssi- ja ylävesihälyttimen kosketin (N-24), jos pilssi on lähellä **⚠**; akkujen lämpötilat (DS18B20) | – | ehdotus; node2 olemassa |
| **node1** (N-30) | oma (ISO1044) | konehuone | nykyinen | konehuoneen lämpötila, kosteus ja ilmanpaine; kotelon lämpötila; Raspberry Pi:n virran tila | releet (3 × DC, AC); Pi:n sammutus | olemassa |
| **S4 Komentosilta** | SH-ESP32 | komentosilta, kattopaneelin takana | 24 V (joystickin potentiometri saa syöttönsä PVEH:n 24 V:sta, joten se viittaa akun miinukseen) | keulapotkurin joystickin asento (jännitejakajan kautta, [bow-thruster-control 4](../../hydraulics/design/bow-thruster-control.md#4-suositus-arvio-suora-joystick-ja-esp32-pdm-valvojana)); komentosillan lämpötila; ulkolämpötila (N-32); NMEA 2000 -väylän jännite tällä väylän päässä (N-05); kattopaneelin sivunvaihtopainikkeet (USB HID omalle näytölle, [bridge-mfd 4.3](bridge-mfd.md#43-käyttö)) | hälytyssummeri | ehdotus |
| **S5 Asuintilat ja lämmitys** | SH-ESP32 | asuintilojen keskellä **⚠** | väylä (kelluvat anturit) | hyttien ja salongin lämpötilat (1-Wire-ketju, N-31); lämmityksen meno- ja paluuveden lämpötila; savu- ja häkävaroittimien koskettimet (N-34); kaasuhälyttimen kosketin ja magneettiventtiilin tila (N-33), jos keittiö on lähellä **⚠** | – (puhallinkonvektorit KH-07 PDM:llä) | ehdotus |
| **S6 Säiliöt** | HALMET | säiliöiden lähellä **⚠**; yhdistetään S1:een tai S5:een, jos säiliöt ovat lähellä | 24 V (säiliöanturit ovat yleensä runkoon kytkettyjä vastusantureita) | käyttövesi (N-41); harmaavesisumppu ja septi (N-42); polttoaine (N-40), jos ei S1:ssä | – | ehdotus |
| **S7 GNSS** (korvaa node3:n kokeilun) | SH-ESP32 (UART UM982:lle) | komentosilta, katon alla antennien lähellä | 24 V (antennien koaksiaalivaippa on moduulin maassa, ja antennit kiinnitetään teräskattoon) | UM982: sijainti, nopeus, aika, suunta, kääntymisnopeus; RTK-korjaukset (RTCM) sisään verkon kautta | – | omistajan suunnitelma |

#### ESP32-PDM-kortit (lähdöt ja paneelikytkimet)

| Kortti | Sijainti | Lähdöt ([piirilista](circuit-list.md)) | Tulot |
|---|---|---|---|
| PDM KS-1…3 (4-kanavaiset) | komentosilta, alle 10 m kattopaneelista | KS-01…KS-14 (valot, AIS, FM-radio, pyyhkijät, huurunpoisto, navigointitietokone) | kattopaneelin kytkimet |
| PDM KH-1…3 (4-kanavaiset) | konehuone, KH | KH-01…KH-07 (pumput, puhaltimet, valaistus, puhallinkonvektorit) | konehuoneen kytkimet |
| PDM hc-1…2 (suurivirta) | lähellä TK-kiskoa | pilssipumppujen pakotettu käyttö (N-25: lähtö näkee myös kohokytkimen käynnistämän pumpun) | – |
**Hydrauliikka ei tarvitse omaa PDM-korttia** [korjattu 2026-11-08]. Keulapotkurin
proportionaaliventtiiliä (PVEH) ohjataan suoraan analogisesti joystickilla
([bow-thruster-control 4](../../hydraulics/design/bow-thruster-control.md#4-suositus-arvio-suora-joystick-ja-esp32-pdm-valvojana)),
eikä BAV-713:a enää ole (PVG 32, päätös 2026-10-27). Sähköisiä lähtöjä jää vähän:

- **PVEH:n sallintareleen kela** (pieni virta): yksi 6050-kanava KH-kortilta. PDM voi vain pudottaa
  sallinnan hälytyksestä, ei ohjata potkuria.
- **PVEO vinssille ja painepesurille** (myöhemmin, päälle/pois): suoraan kytkimillä
  ([kaavio 2A1](../../hydraulics/schematic.md)) tai kahdella KH-kanavalla, jos ne halutaan etäohjaukseen
  ja valvontaan.

KH-kortteihin (3 × 4 = 12 kanavaa, tarve noin 11 puhallinkonvektorit mukaan lukien,
[piirilista](circuit-list.md#pdm-kanavien-tarve-laskelma--arvio)) mahtuu sallintarele. Neljäs KH-kortti tarvitaan vasta,
jos sekä puhallinkonvektorit että molemmat PVEO:t tulevat PDM:lle [laskelma].

#### Suoraan väylään liittyvät valmiit laitteet

| Laite | Sijainti |
|---|---|
| Signal K -palvelin (Pi 5 + CAN HAT), Cerbo GX MK2 | konehuone |
| Simrad NSS evo3, AIS, autopilotin ohjausyksikkö ja paneeli | komentosilta / kattopaneeli |
| UM982:n kaksi GNSS-antennia (node S7:n kautta) | katto |
| Tuulianturi | masto |
| (Magneettinen suunta-anturi, vain varalle, ehdotus) | lähellä painopistettä **⚠** |
| Kaiku ja loki (ehdotus) | pohja |
| Peräsinkulma-anturi (autopilotin mukana) | peräsinakseli |

**Yhteensä [arvio]:** 6–7 omaa anturinodea, noin 8 PDM-korttia ja 8–10 valmista laitetta, eli
noin 25 väylälaitetta. Raja on 50 laitetta (kohta 5.2), ja väylävirran arvio (kohta 3.9) pysyy
noin 1,5 A:ssa.

### 3.12 GNSS ja suunta: UM982 (lisätty 2026-11-08)

Omistajien suunnitelma: GNSS/RTK toteutetaan **Unicore UM982** -moduulilla ja kahdella antennilla
[omistaja 2026-11-08].

- **Mitä se antaa:** sijainnin, nopeuden ja ajan sekä **suunnan** kahden antennin välisestä
  vektorista. Suuntatarkkuus on 0,1° (RMS) 1 m:n antennivälillä ja päivitystaajuus 20 Hz
  [datalehti Unicore UM982](https://en.unicore.com/uploads/file/UM982_User%20Manual_EN_R1.7.pdf). GNSS-suunta on tosisuunta, johon teräsrunko ja sähkökaapelit eivät vaikuta, joten
  erillistä magneettikompassia ei tarvita autopilotille eikä tutkan karttapäällykselle (N-14).
  Suunta toimii myös ilman RTK-korjauksia [arvio].
- **Antennit:** komentosillan katolle, keskelle kattoa, **kölilinjan suuntaisesti noin 1,5–2,0 m:n
  päähän toisistaan** [omistaja 2026-11-08]. Suuntatarkkuus paranee suunnilleen antennivälin
  suhteessa: 0,1° / 1 m vastaa noin **0,05–0,07°** 1,5–2,0 m:n välillä [laskelma, oletus:
  käänteinen verrannollisuus]. Antennien tarkka väli mitataan ja syötetään moduulille. Pidä erillään
  tutkan säteestä sekä VHF- ja AIS-antenneista [arvio]. **Antennien pitää tukea myös Galileo
  E6 -taajuutta** (HAS, alla); kaikki L1/L2/L5-antennit eivät tue, **⚠ tarkista** antennin
  datalehdestä.
- **Moduulikortti:** ehdokas [AliExpress 1005007998167643](https://www.aliexpress.com/item/1005007998167643.html)
  [omistaja 2026-11-08]; tiedot **⚠ ei tiedossa** (sivu ei avautunut 2026-11-08).
- **Moduulin sähköiset tiedot** [datalehti UM982 User Manual R1.3 (kiinankielinen, 2023-09), omistajan PDF
  2026-11-08, luettu tekstinä]:
  - syöttö VCC **3,0–3,6 V** (tyyp. 3,3 V), aaltoisuus enintään 50 mV; virta tyyp. 180 mA, enintään
    300 mA; teho 600 mW (kahdella antennilla 10 Hz sijainti, RTK ja suunta). Käynnistyksessä
    syöksyvirta, nousuaika 100 µs–1 ms ja monotoninen; seuraava käynnistys aikaisintaan 500 ms
    virran katkeamisen jälkeen.
  - **3 × UART, LVTTL 3,3 V** (sopii suoraan ESP32:n tuloihin); I²C, SPI ja CAN ovat varattuja
    eivätkä toimi. Tilalähdöt PVT_STAT, RTK_STAT ja ERR_STAT, lisäksi PPS ja EVENT.
  - datamuodot NMEA 0183 ja Unicoren omat; korjaukset RTCM 3.x sisään; päivitys 20 Hz.
  - **aktiiviset antennit:** LNA-vahvistus 18–36 dB (tyyp. 30 dB); antennien syöttö (ANT_BIAS)
    tuodaan moduulin ulkopuolelta, ja valmistaja suosittelee sille **erillistä jännitekiskoa** ja
    ESD- ja TVS-suojausta, jotta antennijohdon ylijännite ei rikkoisi moduulia.
  - lämpötila −40…+85 °C.
  - Noden S7 (SH-ESP32) 3,3 V:n kisko ei välttämättä riitä 300 mA:n lisäkuormaan, **⚠ tarkista**;
    oma 3,3 V:n regulaattori ja antennien syöttö lisäkortille, ellei valmis UM982-kortti sisällä niitä.
- **⚠ E6-tuki riippuu moduulin versiosta.** R1.3-ohjeen signaalilistassa Galileo on vain E1, E5a ja
  E5b (pääantenni) sekä E1 ja E5b (sivuantenni), **ei E6:ta**. Uudemmat ohjeet (R1.7, R1.9) ja
  Unicoren tuotesivu mainitsevat E6:n ja E6-HAS:n. Ennen ostoa varmistetaan myyjältä, että kortin
  UM982 ja laiteohjelmisto tukevat E6:ta ja HAS:ia. R1.3:n PPP-tarkkuus (vaaka 5 cm, pysty 10 cm,
  konvergenssi 20 min) koskee todennäköisesti BeiDoun B2b-PPP:tä, joka toimii vain Aasian ja
  Tyynenmeren alueella [arvio, **⚠ tarkista**].
- **Tarkkuuskorjaukset: Galileo E6-HAS** [omistaja 2026-11-08]. Galileo High Accuracy Service on
  maksuton, ja korjaukset tulevat suoraan satelliiteista E6-B-signaalissa, joten nettiyhteyttä ei
  tarvita. Initial Service (käytössä 24.1.2023 alkaen): vaakatarkkuus alle 20 cm (95 %), pystytarkkuus
  alle 40 cm, alkujakso (konvergenssi) noin 300 s ([GSC: Galileo HAS](https://gsc-europa.eu/galileo/services/galileo-high-accuracy-service-has),
  [EUSPA](https://www.euspa.europa.eu/newsroom-events/news/have-you-met-has)). UM982 tukee E6-HAS:ia;
  E6 otetaan käyttöön signaaliryhmällä `CONFIG SIGNALGROUP 3 6` (oletus on 4/5), ja tuki voi riippua
  laiteohjelmistosta, **⚠ tarkista** versio ([Unicore UM982](https://en.unicore.com/products/um982),
  [ArduSimple: UM982:n asetukset](https://www.ardusimple.com/how-to-configure-unicore-um980-um981-um982)).
  Myös se, toimiiko kahden antennin suuntalaskenta samalla signaaliryhmällä, **⚠ tarkista**.
  - HAS on PPP-ratkaisu, ei RTK: tarkkuus on desimetrien eikä senttien luokkaa, mikä riittää hyvin
    navigointiin ja ankkurivahtiin [arvio]. Senttitason RTK vaatisi NTRIP-korjaukset verkon kautta
    (Maanmittauslaitoksen FINPOS-RTK vain tutkimukseen ja testaukseen, [MML](https://www.maanmittauslaitos.fi/en/finpos/rtk);
    kaupalliset verkot tai RTK2Go), joita ei nyt suunnitella.
- **Vikatilat:** GNSS-katkos (esim. sillan alla, häirintä) vie sijainnin ja suunnan yhtä aikaa.
  Autopilotti kytkeytyy silloin pois ja hälyttää. Jos autopilotin halutaan jatkavan katkon yli,
  tarvitaan magneettinen varasuunta-anturi (N-14). Simrad saa sijainnin samasta lähteestä; erillinen
  varavastaanotin (esim. AIS-laitteen oma GPS) **⚠ tarkista**.

### 3.13 Navigointitietokone ja OpenCPN (lisätty 2026-11-08)

Komentosillalle tulee navigointitietokone, jossa on noin 20":n näyttö ja ohjelmistona
lähtökohtaisesti OpenCPN [omistaja 2026-11-08]. Komentosillalla on siis kolme näyttöä:

| Näyttö | Tehtävä | Tiedot |
|---|---|---|
| Navigointitietokone, noin 20", OpenCPN | reittisuunnittelu ja pääkartta (iso näyttö) | Signal K tai oma N2K-liitäntä |
| Simrad NSS evo3 (kattopaneeli) | kartta ja mittarit, autopilotin ohjaus | suoraan N2K:sta |
| Oma monitoiminäyttö (kattopaneeli) | kamerat, hydrauliikka, sähkö, hälytykset, PDM-ohjaus | Signal K ([bridge-mfd](bridge-mfd.md)) |

**Tietojen reitti [arvio]:**

- **Ensisijaisesti Signal K:n kautta:** OpenCPN lukee Signal K -palvelimen tietovirran
  (NMEA 0183 TCP:llä tai Signal K -yhteydellä) Ethernetin yli. Kaikki väylän ja nodejen
  tiedot ovat silloin käytettävissä, eikä OpenCPN:ää tarvitse liittää väylään.
- **Vaihtoehto: oma erotettu N2K-liitäntä,** jos navigoinnin halutaan toimivan, vaikka
  konehuoneen Pi tai verkko on alhaalla. OpenCPN 5.8 ja uudemmat lukevat NMEA 2000:ta suoraan
  (Linuxissa SocketCAN-liitännällä tai Actisense-sovittimella) (**⚠ tarkista** käytössä olevasta
  versiosta). Sovittimen pitää olla erotettu (kohta 5.4), esim. samanlainen kuin Pi:n CAN HAT.
  Simrad on joka tapauksessa riippumaton varanavigointi.
- **Autopilotti:** OpenCPN voi lähettää aktiivisen reitin tai reittipisteen autopilotille
  (N2K 129283/129284/129285 tai NMEA 0183 APB/RMB Signal K:n kautta). Se, ottaako valittava
  autopilotti ohjauksen näistä vastaan, **⚠ tarkista** autopilotin valinnan yhteydessä.

**Laitteisto [arvio]:** tietokone ja näyttö valitsematta. Huomioitavaa: 24 V:n syöttö (useimmat
näytöt ja minitietokoneet ovat 12 V tai 19 V → DC-DC-muunnin), näytön kirkkaus ja himmennys
yöajoon (kuten [bridge-mfd 4.4](bridge-mfd.md#44-näyttölaite)), ja tietokone, joka kestää virran
katkeamisen (SSD, automaattinen käynnistys). Navigointitietokoneen ja oman monitoiminäytön voi
myöhemmin toteuttaa samalla tietokoneella, mutta erillisinä ne varmistavat toisiaan.

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

### 5.6a Komentosillan kattopaneeli (lisätty 2026-11-08)

Paneeliin ruorin yläpuolelle tulevat radiot, PDM:ien käyttökytkimet ja kaksi monitoiminäyttöä
[omistaja 2026-11-08] ([current-system 3.5](../current-system.md#35-komentosillan-kattopaneeli-lisätty-2026-11-08)).

- **Runkoväylä paneelin taakse [arvio].** Paneeli on komentosillan laitteiden keskus, joten
  runkoväylä kannattaa kuljettaa sen kautta ja liittää NSS ja mahdolliset muut komentosillan laitteet
  lyhyillä pudotuksilla T-kappaleista paneelin takana. Jos runkoväylä päättyy komentosillalle,
  päätevastus tulee paneelin taakse (tai mastoon, jos tuulianturin linja jatkuu sinne).
- **Kaksi näyttöä varmistavat toisiaan [arvio].** Simrad lukee navigointitiedot (GNSS, AIS, tuuli,
  suunta, syvyys) suoraan N2K:sta, joten se toimii, vaikka Signal K -palvelin (Pi) tai oma näyttö
  kaatuu. Oma näyttö taas näyttää Signal K:n tiedot (hydrauliikka, sähkö, hälytykset, PDM-ohjaus),
  joita Simrad ei näytä. Jos oma näyttö halutaan toimimaan ilman Pi:tä, se tarvitsee oman
  CAN-liitännän väylään (erotettu, kuten Pi:n HAT).
- **Simrad saa virtansa omasta sulakepiiristään** (24 V, 3–5 A), ei väylästä; väylästä se ottaa vain
  1 LEN.
- **PDM:ien paneelikytkimet:** ESP32-PDM:n paneelikaapeli on enintään 10 m, suojattu
  monijohdinkaapeli ja vain kuivakoskettimet ([ESP32-PDM README](https://github.com/plektra/ESP32-PDM)).
  Komentosillan PDM:t (KS) kannattaa siis sijoittaa alle 10 m:n päähän paneelista.
- **Kaapelit paneeliin:** N2K-runko tai -pudotus, Ethernet (Simrad tutkalle ja omalle näytölle;
  tarvittaessa kytkin), 24 V:n syötöt (näytöt, radiot), VHF:n ja FM:n koaksiaalit, PDM-
  paneelikaapelit. **N2K ja paneelikaapelit erilleen VHF:n koaksiaalista** (ESP32-PDM:n
  asennusohje).
- **Lämpö:** kaksi näyttöä (noin 20 W kumpikin, arvio) ja VHF lähetyksessä umpinaisessa
  kattopaneelissa → tuuletus paneelin taakse.
- **Huolto:** paneelin pitää aueta tai irrota, jotta liittimiin ja T-kappaleisiin pääsee käsiksi.

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
6. **Lisättäväksi listaan harkintaan:** kaiku. Suunnan antaa UM982 (kaksi antennia); erillinen
   magneettinen suunta-anturi vain varalle. Omistajat päättävät.

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
- [ ] Navigointitietokone (N-07): tietokone, näyttö ja paikka; liittyykö OpenCPN väylään suoraan vai vain Signal K:n kautta
- [ ] Nodejaon sijainnit (kohta 3.11): säiliöt, keittiö (kaasuhälytin), hytit, PVG 32 ja hydrauliikkasäiliö, pilssihälytin
- [ ] Laitteiden mallit ja LEN-arvot: GNSS (valmis vai `node3`), AIS B, tuulianturi,
  peräsinkulma-anturi, polttoainemittarit.
- [x] Suunta-anturi: UM982 kahdella antennilla antaa suunnan [omistaja 2026-11-08]
- [ ] Tuleeko kaiku listaan (N-15), ja tarvitaanko magneettinen varasuunta-anturi autopilotille?
- [x] UM982:n antennit: komentosillan katolle keskelle, kölilinjan suuntaisesti noin 1,5–2,0 m:n välein [omistaja 2026-11-08]
- [x] Tarkkuuskorjaukset: Galileo E6-HAS [omistaja 2026-11-08]
- [ ] **UM982: varmista myyjältä E6- ja HAS-tuki** (R1.3-ohjeessa ei E6:ta); kortin 3,3 V:n syöttö ja antennien syöttö
- [ ] UM982: moduulikortin malli (ehdokas [AliExpress 1005007998167643](https://www.aliexpress.com/item/1005007998167643.html) [omistaja 2026-11-08]; sivu ei avautunut istunnosta, joten liitännät, antennit, syöttö ja hinta **⚠ ei tiedossa**), laiteohjelmiston E6-HAS-tuki ja signaaliryhmä 3 6 kahden antennin suunnan kanssa; E6-taajuutta tukevat antennit
- [ ] Simrad NSS7 vai NSS9 evo3; tarvitseeko oma monitoiminäyttö oman CAN-liitännän (toimii ilman Pi:tä)?
- [ ] Kattopaneelin mitat ja komentosillan PDM:ien paikka (paneelikaapeli enintään 10 m)
- [ ] VHF Sailor RT2048:n liitäntä (NMEA 0183 vai N2K) ja tarvitseeko se GPS-sijainnin DSC:lle.
- [ ] `node2`:n nykyinen mittauskohde, kun käyttöakut on purettu.
- [ ] Instanssitaulukon paikka ja numerointi (kohta 5.5).
