# Vega — sähköjärjestelmän nykytila (lähtötilanne)

> **Tila:** Runko, aloitettu 2026-10-22. Tiedossa on vain alla oleva, enimmäkseen vuoden 2017
> blogista. **⚠ tarkista** -merkityt kohdat pitää tarkistaa veneellä. Täydennä tietojen karttuessa.

## 1. DC-järjestelmä

| Kohde | Arvo | Lähde |
|---|---|---|
| Järjestelmäjännite | 24 V **⚠ tarkista** (päätelty 24 V:n hydrauliikan varapumpusta) | [blogi 2018-11-12] |
| Käyttöakut | 2 kpl (tyyppi ja kapasiteetti **⚠ ei tiedossa**) | [blogi 2017-04-10] |
| Käynnistysakut | 2 kpl (tyyppi ja kapasiteetti **⚠ ei tiedossa**) | [blogi 2017-04-10] |
| Akkujen sijainti | Kannen alla telineessä konehuoneen styyrpuurin puolella | [blogi 2017-04-10] |
| Koneen laturi | 65 A | [blogi 2017-07-04] |
| Lataus maasähköstä | **⚠ ei tiedossa** | |

## 2. AC-järjestelmä

| Kohde | Arvo | Lähde |
|---|---|---|
| Generaattori | Tila varattu konehuoneen paapuurin puolelle; **⚠ tarkista**, onko asennettu | [blogi 2017-04-19] |
| Maasähkö | **⚠ ei tiedossa** | |
| Invertteri | **⚠ ei tiedossa** | |

## 3. Suuret DC-kuormat

| Kuorma | Teho / virta | Huomiot | Lähde |
|---|---|---|---|
| Hydrauliikan varapumppu (ohjauksen vara) | 2,5 kW, 24 V (~100 A tai yli) | 65 A:n laturi ei jaksa syöttää sitä pitkään | [blogi 2017-07-04] |
| PTO-kytkimen toimilaite (suunnitteilla) | **⚠ ei tiedossa** | Jos mekaaninen kytkin ohjataan 24 V:n toimilaitteella | [hydraulics/design/p2-pump-options.md](../hydraulics/design/p2-pump-options.md) |
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

- [ ] Vahvista 24 V:n DC-jännite
- [ ] Akkujen tyypit ja kapasiteetit (käyttö ja käynnistys)
- [ ] Latauslähteet: laturi(t), maasähkölaturi, aurinkopaneelit
- [ ] Generaattori ja maasähkö: asennettu vai suunnitteilla?
- [ ] Pääkeskus ja jakelun rakenne
- [ ] Mitkä hydrauliikan toiminnot tarvitsevat sähköohjausta (solenoidiventtiilit, PTO-kytkimen toimilaite, anturit), ja miltä PDM-lähdöiltä
