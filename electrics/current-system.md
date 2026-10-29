# Vega — sähköjärjestelmän nykytila (lähtötilanne)

> **Tila:** Runko, aloitettu 2026-10-22, päivitetty 2026-10-29 (24 V:n kuluttajat, komentosillan laitteet, NMEA 2000 -laitteet, polttava WC). Tiedossa on vain alla oleva, enimmäkseen vuoden 2017
> blogista. **⚠ tarkista** -merkityt kohdat pitää tarkistaa veneellä. Täydennä tietojen karttuessa.

## 1. DC-järjestelmä

| Kohde | Arvo | Lähde |
|---|---|---|
| Järjestelmäjännite | 24 V (vahvistettu) | [blogi 2018-11-12], [omistaja 2026-10-27] |
| Käyttöakut | **Ei ole.** Vanhat isot käyttöakut (2 kpl) on purettu pois | [blogi 2017-04-10], [omistaja 2026-10-29] |
| Käynnistysakut | 2 kpl (tyyppi ja kapasiteetti **⚠ ei tiedossa**). **Syöttävät nyt myös kaikki 24 V:n kuormat** (valaistus, tietokoneet, modeemi, NMEA 2000 ym.) | [blogi 2017-04-10], [omistaja 2026-10-29] |
| Akkujen sijainti | Kannen alla telineessä konehuoneen styyrpuurin puolella | [blogi 2017-04-10] |
| Koneen laturi | 65 A | [blogi 2017-07-04] |
| Lataus maasähköstä | **CTEK MULTI XT 14000**, käytössä käynnistysakkujen ylläpitolataukseen (ainoat jäljellä olevat akut). 24 V, latausjännite 28,8 V, enintään 14 A (≈ 400 W), akuille noin 28–300 Ah (ylläpitolataus enintään noin 500 Ah); vain lyijyakuille (märkä, MF, GEL, Ca/Ca, AGM), litiumtilaa ei mainita. Mitä akkuja se lataa (käyttö, käynnistys vai molemmat): **⚠ tarkista** | [omistaja 2026-10-29], [datalehti CTEK MULTI XT 14000](../datasheets/README.md#sähköjärjestelmä) |

**Huomio [laskelma]:** koska käyttöakkuja ei ole, jatkuvasti päällä olevat laitteet (Raspberry Pi,
NUC, 4G-modeemi, NMEA 2000, valvontakamera) purkavat käynnistysakkuja noin 30 W:lla eli noin 0,7 kWh vuorokaudessa
(**⚠ arvio**, ks. kohta 3.1). Ilman maasähköä tai ajoa käynnistysakut tyhjenevät muutamassa
vuorokaudessa (kapasiteetti **⚠ ei tiedossa**), ja lyijyakun syväpurku lyhentää sen ikää. Kun
uusi käyttöakusto tulee, nämä kuormat siirretään sille ja käynnistysakut erotetaan (esim.
erotusrele tai DC-DC-laturi). Siihen asti kone kannattaa varmistaa esim. alijännitekatkaisulla
tai sillä, että CTEK on kytkettynä.

**Pilssipumput ovat turvallisuuskriittisiä.** Kolme pilssipumppua (noin 12 A kukin) ottaa virtansa
nyt käynnistysakuilta. Jos jatkuvat kuormat tyhjentävät akut, pilssipumput eivät toimi.
Alijännitekatkaisu saa siksi katkaista vain muut kuormat, ei pilssipumppuja. Pilssipumput
kytketään suoraan akulle pääkytkimen ohi omilla sulakkeillaan. Vikatilanteet ja kytkennät on
hyvä tarkastuttaa pätevällä sähköasentajalla.

## 2. AC-järjestelmä

| Kohde | Arvo | Lähde |
|---|---|---|
| Generaattori | **Ei asennettu.** Tila varattu konehuoneen paapuurin puolelle | [omistaja 2026-10-28], [blogi 2017-04-19] |
| AC-sähkön tarve | Ajossa ja ankkurissa. Suurin ankkurikuorma 2,3 kW:n sähkökiuas (päätetty 2026-10-29), kerrallaan noin 2 h. Olemassa on vain jääkaappi; muut AC-laitteet ovat harkinnassa, myös jätteet polttava WC [omistaja 2026-10-29]: [loads.yaml](loads.yaml). Vaihtoehdot: [design/ac-power-source.md](design/ac-power-source.md) | [omistaja 2026-10-28] |
| Maasähkö | Kotilaiturissa 15 A:n sulake (≈ 3,45 kVA, jos 1-vaiheinen 230 V; vaiheiden määrä **⚠ tarkista**) | [omistaja 2026-10-28] |
| Invertteri | **⚠ ei tiedossa**; ehdokas Mastervolt Mass Combi Ultra 24/3500-100, ks. [design/ac-power-source.md](design/ac-power-source.md) | [omistaja 2026-10-28] |
| Erotusmuuntaja | Sijoitus luultavasti konehuoneeseen, paikka auki [omistaja 2026-10-28]. Airlink WM5002 MCB ([tyyppikilpi](img/isolation-transformer-wm5002-plate.jpg)), 230 V → 115–0–115 V (musta–vihreä–punainen), 5000 VA, IP23, 25 kg. **Olemassa, ei kytketty.** CTE-toisio muutetaan 230 V:ksi irrottamalla keskipisteen maasilta (Airlink); toision nollan maadoitus vielä varmistettava, ks. [design/ac-power-source.md](design/ac-power-source.md#26-olemassa-oleva-erotusmuuntaja-airlink-wm5002) | [omistaja 2026-10-28], [datasheets](../datasheets/README.md#sähköjärjestelmä) |

## 3. Suuret DC-kuormat

| Kuorma | Teho / virta | Huomiot | Lähde |
|---|---|---|---|
| Hydrauliikan varapumppu (ohjauksen vara) | 2,5 kW, 24 V (~100 A tai yli) | 65 A:n laturi ei jaksa syöttää sitä pitkään | [blogi 2017-07-04] |
| ~~PTO-kytkimen toimilaite~~ | – | Ei tarpeen: PTO-kytkintä ei tule (päätös 2026-10-23), P2 on PVH57 (päätös 2026-10-27) | [hydraulics/design/archive/p2-pump-options.md](../hydraulics/design/archive/p2-pump-options.md) |
| Keulapotkuri | — | Hydraulinen, PTO-vetoinen; sähkökuormana vain venttiilien solenoidit | [blogi 2018-11-12] |
| Pilssipumput, 3 kpl (**olemassa**) | 24 V, noin 12 A kukin täydellä teholla (≈ 290 W; kaikki yhtä aikaa noin 36 A) **⚠ tarkista** tyyppikilvestä | Kohokytkimet; käyvät vain tarvittaessa. Sijainnit ja syöttötapa **⚠ ei tiedossa** | [omistaja 2026-10-29] |

### 3.1 Suunnitellut 24 V:n kuluttajat konehuoneessa

**Olemassa ovat yleisvalaistus (LED-nauhat), polttoaineen siirtopumppu, Raspberry Pi 5, Intel NUC ja 4G-modeemi**; muut ovat
suunniteltuja, eikä laitteita ole valittu [omistaja 2026-10-29]. Arvioidut tehot ja
käyttöajat: [loads.yaml](loads.yaml) (`dc_loads`).

| Kuluttaja | Teho | Huomiot |
|---|---|---|
| Valvontakamera | **⚠ ei tiedossa** (arvio noin 5 W) | Ei vielä asennettu; oma kamera tulee sekä konehuoneeseen että komentosillalle [omistaja 2026-10-29]. Päällä jatkuvasti, myös ankkurissa |
| Polttoaineen siirtopumppu (**olemassa**) | **⚠ ei tiedossa** (arvio noin 100 W) | Käytetään vain siirrettäessä polttoainetta bunkkereista päivätankkiin tai pesukierrossa; ei ankkurikuorma. Polttoainejärjestelmä on keskeneräinen, eikä bunkkereita tällä hetkellä ole [omistaja 2026-10-29] |
| Harmaavesisumppu ja -pumppu | **⚠ ei tiedossa** (arvio noin 120 W) | Uimurikytkin |
| Savukaasujen poistopuhallin | **⚠ ei tiedossa** (arvio noin 50 W) | Hitsauskaasujen ym. tilapäiseen poistoon konehuoneesta; ei ankkurikuorma [omistaja 2026-10-29] |
| Käyttövesipumppu | **⚠ ei tiedossa** (arvio noin 150 W) | Painevesipumppu |
| Vesikiertoisen lämmityksen kiertovesipumppu | **⚠ ei tiedossa** (arvio noin 30 W) | Käy lämmityskaudella jatkuvasti, joten se on DC-kuormista suurin energiankuluttaja |
| Yleisvalaistus, LED-nauhat (**olemassa**) | **⚠ ei tiedossa** (arvio noin 50 W) | Teho nauhojen pituudesta ja W/m-arvosta [omistaja 2026-10-29] |
| Raspberry Pi 5 (**olemassa**) | **⚠ ei tiedossa** (arvio noin 7 W, muuntimen häviöineen noin 8 W) | Signal K -palvelin; päällä jatkuvasti. Syöttö **Mean Well DDR-15G-5** (24 V → 5 V, 3 A, 15 W) [omistaja 2026-10-29]. Pi 5 tarvitsee täyteen USB-virtaan 5 A:n lähteen; 3 A:n syötöllä se rajaa USB-porttien yhteisvirran noin 600 mA:iin [laskelma, Raspberry Pi -dokumentaation mukaan **⚠ tarkista**]. Riittää, jos USB:ssä on vain kevyitä laitteita (esim. CAN- tai N2K-sovitin) |
| Intel NUC (**olemassa**) | **⚠ ei tiedossa** (arvio noin 15 W, muuntimen häviöineen noin 17 W; malli ei tiedossa) | Frigate-kameratallennin; päällä jatkuvasti. Syöttö **Mean Well DDR-240B-24** (24 V → vakautettu 24 V, 10 A, 240 W; tulo 16,8–33,6 V) [omistaja 2026-10-29]. Sama muunnin syöttää myös mm. **NMEA 2000 -väylän**, 4G-modeemin ja komentosillan PoE-kameran [omistaja 2026-10-29]. NMEA 2000 -standardin väyläjännite on nimellisesti 12 V (laitteiden on toimittava noin 9–16 V:lla; **⚠ tarkista** standardista), mutta kaikki Vegan väylälaitteet toimivat 9–32 V:lla, joten 24 V on niille sopiva [omistaja 2026-10-29]. Uutta väylälaitetta valittaessa tarkista, että se sietää 24 V. NUC:n malli jätetään toistaiseksi selvittämättä, koska keskitytään sähköjärjestelmään [omistaja 2026-10-29] |
| 4G-modeemi Teltonika RUT240 (**olemassa**) | Noin 1–2 W käytössä, enintään noin 4,2 W [datalehti Teltonika RUT240] | Päällä jatkuvasti; tulo 9–30 VDC. Syöttö **Mean Well DDR-240B-24**:n vakautetusta 24 V:sta [omistaja 2026-10-29], joten akuston latausjännite ei vaikuta siihen |
| Hydrauliikan ohjaus | **⚠ ei tiedossa** | PDM, PVE-ohjausyksiköt, BAV-713:n kelat ja anturit, ks. [hydraulics/schematic.md](../hydraulics/schematic.md) |

Raspberry Pi ja NUC voidaan myöhemmin yhdistää yhdeksi tietokoneeksi; elektroniikka suunnitellaan
erikseen [omistaja 2026-10-29].

Konehuoneen kuluttajat yhteensä arviolta noin 1,5 kWh/vrk lämmityskaudella [laskelma]; kaikki 24 V:n
kuormat (myös kohdat 3.2 ja 3.3) noin 2 kWh/vrk, ks.
[design/ac-power-source.md](design/ac-power-source.md#21-koko-ankkurivuorokauden-energiatarve-laskelma).
Polttoaineen siirtopumppu ja kiertovesipumppu liittyvät myös tuleviin polttoaine- ja
lämmitysjärjestelmiin, joille ei vielä ole omaa kansiota.

### 3.2 Komentosillalta ohjattavat 24 V:n laitteet

Tehot ovat omistajan ilmoittamia enimmäistehoja [omistaja 2026-10-29]. Tarkemmat tiedot ja
käyttöaika-arviot: [loads.yaml](loads.yaml) (`dc_loads`).

| Laite | Enimmäisteho | Tila | Huomiot |
|---|---|---|---|
| Kulkuvalot | 10 W | **toteutettu** | |
| Ankkurivalo | 5 W | **toteutettu** | Ankkurissa yöllä |
| Sisävalaistus | 200 W | **toteutettu** | Tyypillinen käyttö arviolta noin 50 W |
| Kansivalaistus | 200 W | suunniteltu | |
| Työvalo eteen | 100 W | suunniteltu | |
| Työvalo taakse | 100 W | suunniteltu | |
| Hakuvalo | 500 W (≈ 21 A) | **olemassa, ei asennettu** | |
| Navigointitietokone ja oma näyttö | **⚠ ei tiedossa** | suunniteltu | |
| Valvontakamera | **⚠ ei tiedossa** (arvio noin 5 W) | **toteutettu** | Komentosillan oma kamera; konehuoneeseen tulee erillinen (kohta 3.1) [omistaja 2026-10-29]. PoE, syöttö **Mean Well DDR-240B-24**:ltä [omistaja 2026-10-29] |
| Tutka | **⚠ ei tiedossa** | suunniteltu | |
| Atlas, pyörivä kirkasnäkölasi | **⚠ ei tiedossa** | suunniteltu | Oman invertterin kautta |
| Pyyhkijät | **⚠ ei tiedossa** | suunniteltu | |
| FM-radio | **⚠ ei tiedossa** | **toteutettu** | Tavallinen autoradio 24 V → 12 V -muuntimella (malli **⚠ ei tiedossa**) |
| VHF Sailor RT2048 | **⚠ ei tiedossa** | **toteutettu** | Käyttöjännite ja virrankulutus datalehdestä **⚠ tarkista** |

Valot yhtä aikaa täysillä (kulku-, ankkuri-, sisä- ja kansivalot, työvalot ja hakuvalo) ottavat
enintään noin 1,1 kW eli noin 46 A [laskelma]. Ankkurissa valaistus kuluttaa arviolta noin
0,3 kWh vuorokaudessa (ankkurivalo 10 h, sisävalot noin 50 W 5 h; **⚠ arvio**).

### 3.3 NMEA 2000 -väylän laitteet

Suunnitellut väylälaitteet [omistaja 2026-10-29]. Ne saavat virtansa väylästä, eli
DDR-240B-24:n vakautetusta 24 V:sta, joten jokaisen pitää sietää 24 V (ks. kohta 3.1).
Väylävirta ilmoitetaan LEN-lukuna (1 LEN = 50 mA); laitteiden LEN-arvot **⚠ ei tiedossa**.

| Laite | Huomiot |
|---|---|
| Polttoainemittari(t) | Polttoainejärjestelmä on keskeneräinen |
| Peräsimen asentoanturi | Liittyy ohjaukseen ja autopilottiin, ks. [hydraulics/requirements.md](../hydraulics/requirements.md) |
| Tuulimittari | |
| GPS/GNSS | |

### 3.4 Maston ja katon varustelu

Mastoon ja osittain komentosillan katolle tuleva varustelu [omistaja 2026-10-29]. Lista on
kaapeloinnin ja kiinnitysten suunnittelua varten; laitteiden tehot ovat kohdissa 3.2 ja 3.3.

| Varuste | Sijainti | Sähkö / kaapeli | Huomiot |
|---|---|---|---|
| VHF-antenni | masto | koaksiaali VHF:lle (Sailor RT2048) | |
| FM-antenni | masto | koaksiaali FM-radiolle | |
| AIS-antenni | masto | koaksiaali AIS-laitteelle | AIS-laitetta ei ole listattu: vastaanotin vai lähettävä (luokka B)? **⚠ ei tiedossa** |
| GPS/GNSS-antenni | luultavasti katto | NMEA 2000 (kohta 3.3) tai koaksiaali | |
| Mastovalo | masto | 24 V | Kuuluuko kulkuvalojen 10 W:iin? **⚠ tarkista** |
| Ankkurivalo | masto | 24 V, enintään 5 W | Olemassa (kohta 3.2) |
| Kulkuvalot | katto | 24 V | Olemassa (kohta 3.2) |
| Työvalot eteen ja taakse | masto | 24 V, 2 × enintään 100 W | |
| Kamera | masto | PoE (Ethernet) | Kolmas kamera komentosillan ja konehuoneen lisäksi? **⚠ tarkista** |
| Tutka | masto | 24 V + data | Malli valitsematta; kaapeli mallin mukaan |
| Tuulianturi | masto | NMEA 2000 (kohta 3.3) | |

Mastoon menee siis ainakin kolme koaksiaalikaapelia, 24 V:n syötöt valoille ja tutkalle,
Ethernet kameralle ja mahdollisesti tutkalle sekä NMEA 2000 -pudotus tuulianturille. Kaapeleiden
läpivientien koko ja mahdollinen jakorasia mastossa kannattaa suunnitella kerralla.

## 4. Valvonta, verkot ja tehonjako

Elektroniikkaa kehitetään erillisissä repoissa osoitteessa
[github.com/plektra](https://github.com/plektra). Ne voidaan myöhemmin siirtää tähän repoon.

| Kohde | Repo / sijainti | Huomiot |
|---|---|---|
| Signal K -palvelin | `signalk-server`, `signalk-grafana`, `mainorg-signalk-datasource` | Tietokeskus; Grafana-näkymät. Pyörii konehuoneen Raspberry Pi 5:llä [omistaja 2026-10-29] |
| Kameratallennin (Frigate) | konehuoneen Intel NUC | Valvontakameran tallennus [omistaja 2026-10-29] |
| NMEA 2000 -nodet | `plektra/vega-n2k-node1` … `node3`, `vega-n2k-node-bootstrap` | ESP32-pohjaiset N2K-nodet |
| Tehonjako (PDM) | `ESP32-PDM`, `ESP32-PDM-v1/v2/4x4/base` (KiCad) | ESP32-tehonjakomoduulit; ehdokkaita hydrauliikan solenoidien ja PTO-kytkimen toimilaitteen ohjaukseen |
| Asennusautomaatio | `plektra/vega-ansible` | Veneen tietokoneiden konfigurointi |
| Muut | `yarrboard-hardware`, `frothfet`, `esp32-can-hat`, `SH-ESP32-hardware` | Liittyviä laitteistoprojekteja |

## 5. Avoimet kysymykset

- [x] Vahvista 24 V:n DC-jännite: 24 V [omistaja 2026-10-27]
- [ ] **Veneellä seuraavalla käynnillä:** käynnistysakkujen tyyppikilvet (tyyppi, esim. märkä tai AGM; kapasiteetti Ah; kylmäkäynnistysvirta CCA; ikä tai valmistuspäivä), kytkentä (luultavasti 2 × 12 V sarjassa **⚠ tarkista**) ja lepojännite, kun CTEK on ollut irti muutaman tunnin. Valokuva kilvistä riittää. (Käyttöakut purettu [omistaja 2026-10-29])
- [ ] Latauslähteet: laturi(t), maasähkölaturi, aurinkopaneelit (maasähköstä nyt CTEK MULTI XT 14000 ylläpitolataukseen [omistaja 2026-10-29])
- [x] Mitä akkuja CTEK lataa: käynnistysakkuja, koska käyttöakkuja ei ole [omistaja 2026-10-29]
- [ ] Jääkö CTEK käynnistysakkujen ylläpitolataukseen, kun uusi (litium)käyttöakusto hankitaan?
- [x] Generaattori: ei asennettu [omistaja 2026-10-28]; vaihtoehdot selvityksessä [design/ac-power-source.md](design/ac-power-source.md)
- [x] Maasähkö: kotilaiturissa 15 A [omistaja 2026-10-28]
- [ ] Pääkeskus ja jakelun rakenne
- [x] Mitkä 24 V:n kuluttajista ovat olemassa: LED-nauhavalaistus, polttoaineen siirtopumppu, Raspberry Pi 5 ja Intel NUC [omistaja 2026-10-29]
- [x] Raspberry Pi 5:n ja NUC:n syöttö: Mean Well DDR-15G-5 ja DDR-240B-24 [omistaja 2026-10-29]
- [ ] NUC:n malli ja sallittu tulojännite (jätetty toistaiseksi, [omistaja 2026-10-29])
- [x] Kumpi muunnin syöttää kumpaakin konetta: DDR-15G-5 → Pi, DDR-240B-24 → NUC (ja NMEA 2000 -väylä) [omistaja 2026-10-29]
- [x] Sietävätkö NMEA 2000 -väylän laitteet 24 V: kyllä, kaikki ovat 9–32 V [omistaja 2026-10-29]
- [ ] Mitä muuta DDR-240B-24 syöttää, ja paljonko se kuormittaa muunninta
- [x] Valvontakamerat: komentosillan kamera on olemassa, konehuoneeseen tulee oma [omistaja 2026-10-29]
- [x] Komentosillan kameran PoE-syöttö: DDR-240B-24 [omistaja 2026-10-29]
- [ ] AIS-laite: vastaanotin vai lähettävä (luokka B), malli ja virrankulutus
- [ ] Mastokamera: kolmas kamera vai jompikumpi aiemmista?
- [ ] Mastovalo: erillinen valo vai osa kulkuvaloja (10 W)?
- [ ] VHF Sailor RT2048:n ja FM-radion muuntimen virrankulutus; NMEA 2000 -laitteiden LEN-arvot
- [ ] **Veneellä:** pilssipumppujen tyyppikilvet (virta), sijainnit ja syöttö: suoraan akulta pääkytkimen ohi omalla sulakkeella?
- [x] 4G-modeemin (RUT240) syöttö: DDR-240B-24:n kautta [omistaja 2026-10-29]
- [ ] Siirtopumpun teho tyyppikilvestä ja LED-nauhojen teho; muiden tehot, kun laitteet valitaan
- [x] Mihin savukaasujen poistopuhallin liittyy: hitsauskaasujen ym. tilapäiseen poistoon [omistaja 2026-10-29]
- [ ] Ohjataanko 24 V:n kuluttajia PDM-lähdöiltä (esim. kamera, pumput, valaistus)?
- [ ] Mitkä hydrauliikan toiminnot tarvitsevat sähköohjausta (solenoidiventtiilit, PTO-kytkimen toimilaite, anturit), ja miltä PDM-lähdöiltä
