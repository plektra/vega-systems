# Vega — hydraulijärjestelmän vaatimukset

> **Tila:** Pohja, osittain täytetty. Täydennä `TBD`-kohdat ja poista ohjetekstit (rivit, jotka
> alkavat `>`), kun kukin luku on selvä.
>
> Kuormarekisteri [`loads.yaml`](loads.yaml) on kuormakohtaisten lukujen ensisijainen lähde. Tämä
> dokumentti kuvaa niiden ympärillä olevat tilanteet, ehdot ja rajoitteet.

| Kenttä | Arvo |
|---|---|
| Vastuuhenkilö | TBD |
| Versio | 0.1 |
| Päivitetty | TBD |

---

## 1. Laajuus ja tavoitteet

> Yksi kappale: mihin hydraulijärjestelmää käytetään, mikä on rajattu pois, ja mitä "valmis"
> tarkoittaa (konsepti, yksityiskohtainen suunnitelma, rakennusvalmis).

- **Tarkoitus:** TBD
- **Kuuluu laajuuteen:** TBD
- **Ei kuulu laajuuteen:** TBD
- **Lopputulos:** TBD (konsepti / yksityiskohtainen / rakennusvalmis)
- **Uusi vai muutos:** Nykyisen kahden piirin järjestelmän uudistus. Lähtötilanne on tiedostossa
  [current-system.md](current-system.md).

## 2. Aluksen tiedot

Perustiedot ovat tiedostossa [vessel/README.md](../vessel/README.md). Tähän kootaan hydrauliikan
mitoitukseen vaikuttavat arvot.

| Parametri | Arvo | Yksikkö | Huomiot |
|---|---|---|---|
| Alustyyppi | Teräshinaaja (1912), vapaa-ajan käyttö | | |
| Kokonaispituus | 16,15 | m | |
| Vesilinjan pituus | TBD | m | |
| Leveys | 4,16 | m | |
| Syväys | 1,97 | m | |
| Uppouma (lastattuna) | TBD | t | |
| Suurin nopeus | TBD | kn | Vaikuttaa peräsimen momenttiin |
| Matkanopeus | TBD | kn | |
| ISO 12217 -suunnitteluluokka | TBD | | A / B / C / D |
| Luokitus / lippuvaltion säännöt | TBD | | Vapaa-ajan, kaupallinen, luokituslaitos |
| Toiminta-alue | Suomenlahti (Helsinki); ollut myös Saimaalla | | Murtovesi ja makea vesi |
| Miehistö / käyttötapa | TBD | | Pienellä miehistöllä? Vaikuttaa automaatioon ja hälytyksiin |

### 2.1 Peräsimen tiedot

| Parametri | Arvo | Yksikkö |
|---|---|---|
| Peräsimien määrä | 1 | |
| Peräsimen pinta-ala | TBD | m² |
| Peräsimen tyyppi | TBD | lapa / kölin varassa / tasapainotettu |
| Tasapainotussuhde | TBD | % |
| Suurin peräsinkulma | TBD | ° kumpaankin suuntaan |
| Vaadittu aika ääriasennosta toiseen | TBD | s |
| Peräsinakselin halkaisija | TBD | mm |
| Peräsimen suurin momentti (laskettu tai rakentajalta) | TBD | kNm |

## 3. Käyttöympäristö

| Parametri | Min | Max | Yksikkö | Huomiot |
|---|---|---|---|---|
| Konehuoneen lämpötila | TBD | TBD | °C | |
| Meriveden lämpötila | TBD | TBD | °C | Öljynjäähdyttimen kapasiteetti |
| Staattinen kallistus | | TBD | ° | Säiliön imuaukon pitää pysyä öljyn alla |
| Dynaaminen keinunta | | TBD | ° | |
| Trimmi | TBD | TBD | ° | |
| Tärinä / iskut | | TBD | | Kiinnitysten ja letkujen valinta |
| Suurin melu asuintiloissa | | TBD | dB(A) | Voimayksikön sijoitus ja eristys |

## 4. Tehonlähteet

> Kaikki mahdolliset hydraulitehon lähteet. Arkkitehtuurin valinta (koneen PTO, sähköinen
> voimayksikkö vai molemmat) riippuu tästä luvusta.

### 4.1 Pääkone ja voimanulosotot

| Parametri | Arvo | Yksikkö |
|---|---|---|
| Koneen merkki ja malli | Caterpillar 3126B, säädetty 350 hv (**⚠ tarkista**) | |
| Koneiden määrä | 1 | |
| Tyhjäkäynti / suurin | ~700 (**⚠ tarkista** mittaamalla) / ~2400 (matka ~1800) | rpm |
| Käytettävissä olevat voimanulosotot | Etupään hihnat → ohjauspumppu P1 (vain pienelle teholle; luisti yli ~9 kW:lla). Advance 300:n PTO → apupiirin pumppu P2. | |
| Vaihteiston PTO: välitys / suurin momentti / kytkin | 1:1 / 0,044 kW/rpm ≈ 420 Nm / ei omaa kytkintä; erillinen kytkin suunniteltu PTO:n ja pumpun väliin | – / Nm / – |
| Pyöriikö vaihteiston PTO vapaalla? | kyllä (ensiöakselilta) | |
| Tarvitaanko hydrauliikkaa koneen ollessa sammutettuna? | TBD | kyllä / ei: ankkurointi, satama |

### 4.2 Sähköjärjestelmä

Tarkemmat tiedot: [electrics/current-system.md](../electrics/current-system.md).

| Parametri | Arvo | Yksikkö |
|---|---|---|
| DC-jännite | 24 (vahvistamatta) | V |
| Koneen laturi | 65 | A |
| Käyttöakuston kapasiteetti | TBD | Ah |
| Hydrauliikalle käytettävissä oleva jatkuva DC-virta | TBD | A |
| Generaattori (AC) | TBD | kVA, V, Hz |
| Maasähkö | TBD | A, V, Hz |

## 5. Hydrauliset kuormat (yhteenveto)

> Tarkat luvut ovat tiedostossa [`loads.yaml`](loads.yaml). Tämä taulukko on pikakatsaus.

| ID | Toiminto | Laajuudessa | Kriittisyys | Huomiot |
|---|---|---|---|---|
| STR | Ohjaus / autopilotti | kyllä | kriittinen | Nykyinen: orbitroli + sylinteri, oma piiri |
| BTH | Keulapotkuri | kyllä | korkea | Nykyinen: Side-Power SH240-U11, 264 bar × 33,8 l/min |
| STH | Peräpotkuri | TBD | korkea | |
| WLS | Ankkurivinssi | kyllä (vahvistamatta) | korkea | Hydraulimoottori olemassa, tiedot puuttuvat |
| CAP | Spiira / kiinnitysvinssi | TBD | keskitaso | |
| STB | Vakaimet | TBD | keskitaso | |
| DAV | Jollan daavitti / nosturi | TBD | keskitaso | |
| PAS | Maihinnousuramppi / uimataso | TBD | matala | |
| EXISTING | Muut integroitavat laitteet | TBD | | |

## 6. Käyttötilanteet (samanaikaisuus)

> Pumpun mitoituksen ratkaisee pahin *realistinen* kuormien yhdistelmä, ei kaikkien summa.

| Tilanne | Kuvaus | Samanaikaiset kuormat | Kesto | Kone käy? |
|---|---|---|---|---|
| S1 Satamamanööverit | Laituriin tulo, ahtaat käännökset | STR, BTH | TBD | kyllä |
| S2 Ankkurointi | Ankkurin lasku ja nosto | WLS, STR, BTH | TBD | TBD |
| S3 Matka-ajo | Pitkäkestoinen ohjaus | STR | tunteja | kyllä |
| S4 Hätätilanne | Päätehonlähde menetetty | STR (vähintään) | TBD | ei |

**Mitoittava tilanne:** TBD (todennäköisesti S1 tai S2)

## 7. Turvallisuus, varmennus ja vikatilanteet

> Päätä jokaiselle kriittiselle toiminnolle, mitä tapahtuu, kun pumppu, tehonlähde, letku tai
> ohjaus pettää. Tässä kohdassa ihmisen insinöörinharkinta on tärkeintä.

| Toiminto | Vika | Vaadittu toiminta | Varakeino |
|---|---|---|---|
| Ohjaus | Pumpun tai tehon menetys | TBD | Hätäpinna / sähköinen varapumppu / orbitroli käsipumppuna |
| Ohjaus | Letkun tai liittimen repeämä | TBD | Sulkuventtiilit, erilliset piirit |
| Ankkurivinssi | Tehon menetys ankkurin ollessa puoliksi ylhäällä | Kuorman pito (jarru / jarruventtiili) | Käsinosto |
| Keulapotkuri | Ylikuorma / ylikuumeneminen | TBD | Paineenrajoitus, lämpösuoja |
| Kaikki | Matala öljynpinta | Hälytys, sitten ei-kriittisten kuormien suojapysäytys | |
| Kaikki | Korkea öljyn lämpötila | Suositeltu käyttölämpötila 40–60 °C (Sleipner); varoitus ~65 °C, hälytys ~70 °C (HV 32 -öljy ohenee 70 °C:n yläpuolella alle Salamin ohjauspumpun 12 cSt:n minimin; Parker F1:n raja 75 °C) | Öljynjäähdytin, kierroslukitus |

- **Hätäpysäytyksen periaate:** TBD
- **Kuormien prioriteetti** (mitkä pudotetaan ensin, kun teho ei riitä): TBD
- **Keulapotkurin iskuventtiilit:** Sleipner suosittelee vahvasti iskuventtiilejä 10–15 % valitun
  maksimipaineen yläpuolelle (suojaa, jos potkurit jumittuvat) [ohje Sleipner 2746 35 2025]. Lisättävä.
- **Paineenrajoitus / suurin järjestelmäpaine:** apupiiri 250 bar (päätetty; ~90 %:n keulapotkuriteho
  hyväksytty kustannussyistä). Ohjauspiiri TBD.
- **Suojaus tahattomalta liikkeeltä:** TBD

## 8. Asennuksen rajoitteet

| Kohde | Rajoite |
|---|---|
| Tila voimayksikölle / säiliölle | TBD (paikka, P×L×K) |
| Säiliön sijainti suhteessa pumppuihin | Säiliön öljypinta noin 1 m P2:n imuaukon yläpuolella |
| Painobudjetti | TBD kg |
| Putki- ja letkuvedot | Keulapotkurin A/B-linjat: 1/2" letku, asennettu (CETOP → keula). Muut TBD (laipiolävistykset, palo-osastot). |
| Huollettavuus | TBD (suodattimet, tarkastuslasi, ilmauspisteet) |
| Öljynjäähdytin | Bowman EC100 (varalla), merivesi koneen merivesipiiristä, yhteiseen paluulinjaan ohitusventtiilin kanssa; ks. [oil-cooling.md](design/oil-cooling.md) |

## 9. Öljy, puhtaus ja huolto

| Kohde | Vaatimus |
|---|---|
| Öljytyyppi | TBD (mineraali HLP / HVLP, tai ympäristöystävällinen HEES, ISO 15380) |
| Viskositeettiluokka | Suositus **HV 32** (kylmäkäynnistykset ja PTO-pumpun imupuoli; pysyy Parker F1:n 10–400 cSt:n rajoissa), vahvistamatta |
| Puhtaustavoite | TBD (ISO 4406 -koodi herkimmän komponentin mukaan) |
| Suodatus | TBD (paluu / paine / sivuvirta) |
| Huoltoväli | TBD |
| Vuotojen keräys | TBD |

## 10. Valvonta, ohjaus ja integrointi

> Integrointi Vegan nykyiseen järjestelmään: Signal K -palvelin, NMEA 2000 -nodet ja ESP32
> PDM -kortit. Signal K:ssa ei ole vakiopolkuja hydrauliikalle, joten alla olevat polut ovat ehdotus.

### 10.1 Anturit

| Mittaus | Paikka | Alue | Ehdotettu Signal K -polku | Hälytys / raja |
|---|---|---|---|---|
| Järjestelmäpaine | Pumpun lähtö | TBD bar | `hydraulics.<system>.pressure` | TBD |
| Öljyn lämpötila | Säiliö / paluu | 0–100 °C | `hydraulics.<system>.temperature` | Varoitus ~65 °C, hälytys ~70 °C |
| Öljynpinta | Säiliö | % | `hydraulics.<system>.level` | TBD |
| Suodattimen paine-ero | Paluusuodatin | kytkin / bar | `hydraulics.<system>.filter.clogged` | TBD |
| PTO-kytkimen asento | Kytkin | päällä/pois | `hydraulics.<system>.clutch.engaged` | Hälytys, jos päällä yli ~1200 rpm |
| Imupaine | P2:n imuaukko | −1…+1 bar | `hydraulics.<system>.pump.inletPressure` | Hälytys alle ~−0,2 bar |
| Peräsinkulma | Peräsinakseli | ± ° | `steering.rudderAngle` (vakio) | |

### 10.2 Ohjaus

- **Ohjauspaikat:** TBD (ohjauspisteet, langattomat kaukosäätimet, MFD, autopilotti)
- **Ohjauselektroniikka:** TBD (ESP32 PDM -lähdöt solenoideille ja kytkimen toimilaitteelle, CAN/N2K)
- **Autopilotin liitäntä:** TBD (autopilotin merkki, suunnanvaihtopumppu vai solenoidiventtiiliohjaus)
- **Lukitukset:**
  - PTO-kytkimen kytkentä vain alle noin 1000 rpm:ssä ja vapaakiertoventtiilin ollessa auki.
  - Yli noin 1000 rpm:ssä keulapotkurin venttiili estetään ja 2/2-vapaakiertoventtiili avataan automaattisesti (rajaa lämpökuorman ~1–2 kW:iin; ks. [p2-pump-options.md](design/p2-pump-options.md#käyttäytyminen-eri-kierroksilla-parker-f1-061)).
  - Hälytys, jos kytkin on päällä yli noin 1200 rpm:ssä.
  - Jos P2:ksi tulee Parker F1 ja siihen BPV-ohitusventtiili: BPV:n tilaa saa vaihtaa vain alle 20 barissa (2/2-venttiili ensin auki), ja yli noin 1000 rpm:ssä BPV ohitusasentoon. Ks. [p2-pump-options.md](design/p2-pump-options.md#lisävaruste-parker-bpv-f1--ohitusventtiili).
  - Muut TBD.

## 11. Standardit ja määräykset

> Rastita soveltuvat. Tarkista kunkin voimassa oleva painos ennen kuin luotat siihen.

- [ ] ISO 10592 — Pienalukset: hydrauliset ohjausjärjestelmät
- [ ] ISO 4413 — Hydraulinen voimansiirto: yleiset säännöt ja turvallisuusvaatimukset
- [ ] ISO 1219-1 / -2 — Fluidivoimansiirron piirrosmerkit ja kaaviot
- [ ] ISO 4406 — Hydrauliöljyn puhtauskoodit
- [ ] ISO 15380 — Ympäristöystävälliset hydraulinesteet
- [ ] ISO 10133 / ISO 13297 — Pienalusten DC- ja AC-sähköjärjestelmät
- [ ] Huvivenedirektiivi 2013/53/EU (jos CE-merkitty)
- [ ] Luokituslaitoksen säännöt: TBD
- [ ] Lippuvaltion / kaupallisen liikenteen säännöt: TBD
- [ ] Valittujen laitteiden valmistajien asennusohjeet

## 12. Todentaminen ja hyväksyntä

| Vaatimus | Todentamistapa | Hyväksymiskriteeri |
|---|---|---|
| Aika ääriasennosta toiseen | Koeajo | ≤ TBD s suurimmalla nopeudella |
| Ankkurivinssin nostonopeus | Satamakoe | ≥ TBD m/min työkuormalla |
| Keulapotkurin jatkuva käyttö | Satamakoe | TBD min ilman että öljy ylittää TBD °C |
| Öljyn suurin lämpötila (mitoittava tilanne) | Laskelma, sitten koe | ≤ TBD °C |
| Painekoe | Penkissä / asennettuna | TBD × suurin työpaine, TBD min |
| Melu asuintiloissa | Mittaus | ≤ TBD dB(A) |

## 13. Oletukset ja avoimet kysymykset

| # | Kohde | Tyyppi | Vastuu | Tila |
|---|---|---|---|---|
| 1 | Peräsimen ja ohjaussylinterin mitat | kysymys | | avoin |
| 2 | Koneen tyhjäkäynti: omistajan mukaan noin 700 rpm, vahvistetaan mittaamalla | mittaus | | osittain |
