# Vega — sähköjärjestelmän nykytila (lähtötilanne)

> **Tila:** Runko, aloitettu 2026-10-22, päivitetty 2026-10-28 (generaattori ei asennettu, AC-tarve). Tiedossa on vain alla oleva, enimmäkseen vuoden 2017
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
| AC-sähkön tarve | Ajossa ja ankkurissa. Suurin ankkurikuorma 2,3 kW:n sähkökiuas, kerrallaan noin 2 h. Olemassa on vain jääkaappi; muut AC-laitteet ovat harkinnassa: [loads.yaml](loads.yaml). Vaihtoehdot: [design/ac-power-source.md](design/ac-power-source.md) | [omistaja 2026-10-28] |
| Maasähkö | **⚠ ei tiedossa** | |
| Invertteri | **⚠ ei tiedossa**; ehdokas Mastervolt Mass Combi Ultra 24/3500-100, ks. [design/ac-power-source.md](design/ac-power-source.md) | [omistaja 2026-10-28] |
| Erotusmuuntaja | Airlink WM5002, 230/230 V CTE, 5000 VA, IP23, 25 kg. **Olemassa, ei kytketty.** CTE-toisio pitää selvittää ennen käyttöä, ks. [design/ac-power-source.md](design/ac-power-source.md#26-olemassa-oleva-erotusmuuntaja-airlink-wm5002) | [omistaja 2026-10-28], [datasheets](../datasheets/README.md#sähköjärjestelmä) |

## 3. Suuret DC-kuormat

| Kuorma | Teho / virta | Huomiot | Lähde |
|---|---|---|---|
| Hydrauliikan varapumppu (ohjauksen vara) | 2,5 kW, 24 V (~100 A tai yli) | 65 A:n laturi ei jaksa syöttää sitä pitkään | [blogi 2017-07-04] |
| ~~PTO-kytkimen toimilaite~~ | – | Ei tarpeen: PTO-kytkintä ei tule (päätös 2026-10-23), P2 on PVH57 (päätös 2026-10-27) | [hydraulics/design/archive/p2-pump-options.md](../hydraulics/design/archive/p2-pump-options.md) |
| Keulapotkuri | — | Hydraulinen, PTO-vetoinen; sähkökuormana vain venttiilien solenoidit | [blogi 2018-11-12] |

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
- [ ] Maasähkö: onko laiturissa?
- [ ] Pääkeskus ja jakelun rakenne
- [ ] Mitkä hydrauliikan toiminnot tarvitsevat sähköohjausta (solenoidiventtiilit, PTO-kytkimen toimilaite, anturit), ja miltä PDM-lähdöiltä
