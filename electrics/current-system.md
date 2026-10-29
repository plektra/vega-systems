# Vega — sähköjärjestelmän nykytila (lähtötilanne)

> **Tila:** Runko, aloitettu 2026-10-22, päivitetty 2026-10-29 (suunnitellut 24 V:n kuluttajat, polttava WC). Tiedossa on vain alla oleva, enimmäkseen vuoden 2017
> blogista. **⚠ tarkista** -merkityt kohdat pitää tarkistaa veneellä. Täydennä tietojen karttuessa.

## 1. DC-järjestelmä

| Kohde | Arvo | Lähde |
|---|---|---|
| Järjestelmäjännite | 24 V (vahvistettu) | [blogi 2018-11-12], [omistaja 2026-10-27] |
| Käyttöakut | 2 kpl (tyyppi ja kapasiteetti **⚠ ei tiedossa**) | [blogi 2017-04-10] |
| Käynnistysakut | 2 kpl (tyyppi ja kapasiteetti **⚠ ei tiedossa**) | [blogi 2017-04-10] |
| Akkujen sijainti | Kannen alla telineessä konehuoneen styyrpuurin puolella | [blogi 2017-04-10] |
| Koneen laturi | 65 A | [blogi 2017-07-04] |
| Lataus maasähköstä | **⚠ ei tiedossa** | |

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

### 3.1 Suunnitellut 24 V:n kuluttajat konehuoneessa

Lähes kaikki ovat vielä toteuttamatta, ainoastaan suunniteltuja, eikä laitteita ole valittu
[omistaja 2026-10-29]. Mitkä niistä ovat jo olemassa: **⚠ tarkista**. Arvioidut tehot ja
käyttöajat: [loads.yaml](loads.yaml) (`dc_loads`).

| Kuluttaja | Teho | Huomiot |
|---|---|---|
| Valvontakamera | **⚠ ei tiedossa** (arvio noin 5 W) | Päällä jatkuvasti, myös ankkurissa |
| Polttoaineen siirtopumppu | **⚠ ei tiedossa** (arvio noin 100 W) | Satunnainen käyttö |
| Harmaavesisumppu ja -pumppu | **⚠ ei tiedossa** (arvio noin 120 W) | Uimurikytkin |
| Savukaasujen poistopuhallin | **⚠ ei tiedossa** (arvio noin 50 W) | Hitsauskaasujen ym. tilapäiseen poistoon konehuoneesta; ei ankkurikuorma [omistaja 2026-10-29] |
| Käyttövesipumppu | **⚠ ei tiedossa** (arvio noin 150 W) | Painevesipumppu |
| Vesikiertoisen lämmityksen kiertovesipumppu | **⚠ ei tiedossa** (arvio noin 30 W) | Käy lämmityskaudella jatkuvasti, joten se on DC-kuormista suurin energiankuluttaja |
| Valaistus | **⚠ ei tiedossa** (arvio noin 50 W, LED) | |
| Hydrauliikan ohjaus | **⚠ ei tiedossa** | PDM, PVE-ohjausyksiköt, BAV-713:n kelat ja anturit, ks. [hydraulics/schematic.md](../hydraulics/schematic.md) |

Yhteensä arviolta noin 1 kWh/vrk lämmityskaudella [laskelma], ks.
[design/ac-power-source.md](design/ac-power-source.md#21-koko-ankkurivuorokauden-energiatarve-laskelma).
Polttoaineen siirtopumppu ja kiertovesipumppu liittyvät myös tuleviin polttoaine- ja
lämmitysjärjestelmiin, joille ei vielä ole omaa kansiota.

## 4. Valvonta, verkot ja tehonjako

Elektroniikkaa kehitetään erillisissä repoissa osoitteessa
[github.com/plektra](https://github.com/plektra). Ne voidaan myöhemmin siirtää tähän repoon.

| Kohde | Repo / sijainti | Huomiot |
|---|---|---|
| Signal K -palvelin | `signalk-server`, `signalk-grafana`, `mainorg-signalk-datasource` | Tietokeskus; Grafana-näkymät |
| NMEA 2000 -nodet | `plektra/vega-n2k-node1` … `node3`, `vega-n2k-node-bootstrap` | ESP32-pohjaiset N2K-nodet |
| Tehonjako (PDM) | `ESP32-PDM`, `ESP32-PDM-v1/v2/4x4/base` (KiCad) | ESP32-tehonjakomoduulit; ehdokkaita hydrauliikan solenoidien ja PTO-kytkimen toimilaitteen ohjaukseen |
| Asennusautomaatio | `plektra/vega-ansible` | Veneen tietokoneiden konfigurointi |
| Muut | `yarrboard-hardware`, `frothfet`, `esp32-can-hat`, `SH-ESP32-hardware` | Liittyviä laitteistoprojekteja |

## 5. Avoimet kysymykset

- [x] Vahvista 24 V:n DC-jännite: 24 V [omistaja 2026-10-27]
- [ ] Akkujen tyypit ja kapasiteetit (käyttö ja käynnistys)
- [ ] Latauslähteet: laturi(t), maasähkölaturi, aurinkopaneelit
- [x] Generaattori: ei asennettu [omistaja 2026-10-28]; vaihtoehdot selvityksessä [design/ac-power-source.md](design/ac-power-source.md)
- [x] Maasähkö: kotilaiturissa 15 A [omistaja 2026-10-28]
- [ ] Pääkeskus ja jakelun rakenne
- [ ] Mitkä suunnitelluista 24 V:n kuluttajista ovat jo olemassa, ja niiden tehot, kun laitteet valitaan
- [x] Mihin savukaasujen poistopuhallin liittyy: hitsauskaasujen ym. tilapäiseen poistoon [omistaja 2026-10-29]
- [ ] Ohjataanko 24 V:n kuluttajia PDM-lähdöiltä (esim. kamera, pumput, valaistus)?
- [ ] Mitkä hydrauliikan toiminnot tarvitsevat sähköohjausta (solenoidiventtiilit, PTO-kytkimen toimilaite, anturit), ja miltä PDM-lähdöiltä
