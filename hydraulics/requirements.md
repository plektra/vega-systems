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
| Päivitetty | 2026-10-25 (tulevat kuormat, autopilotti) |

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
| Vaihteiston PTO: välitys / suurin momentti / kytkin | 1:1 / 0,044 kW/rpm ≈ 420 Nm / ei kytkintä; pumppu pyörii aina, PVH57 valmiustilassa ajon aikana (päätös 2026-10-27; aiemmin BPV-ohitusventtiili) | – / Nm / – |
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

Omistajien lista mahdollisesti tulevista laitteista [omistaja 2026-10-25]:

**Piiri 1, ohjauspiiri** (P1 hihnavedolla, varalla sähköpumppu P3)

| ID | Toiminto | Tila | Kriittisyys | Huomiot |
|---|---|---|---|---|
| STR | Ohjaus, orbitroli | olemassa | kriittinen | Orbitroli HKUS 160/4 + sylinteri ZS60350100 |
| STR | Autopilotti | mahdollinen | kriittinen | Ohjaa peräsintä **suuntaventtiileillä** samassa piirissä orbitrolin rinnalla (ei erillistä autopilottipumppua) [omistaja 2026-10-25]. Kytkentäperiaate ja vikatilat: [§10.3](#103-autopilotin-liitäntä-ohjauspiiriin) |

**Piiri 2, apupiiri** (P2 PTO:lta, CETOP 3 -pohjalaatta: 1 paikka käytössä, 3 vapaana)

| ID | Toiminto | Tila | Kriittisyys | Huomiot |
|---|---|---|---|---|
| BTH | Keulapotkuri | olemassa | korkea | Side-Power SH240-U11, 264 bar × 33,8 l/min; pohjalaatan paikka 1 (BAV-713) |
| WLS | Ankkurivinssi | mahdollinen | korkea | Hydraulimoottori olemassa, tiedot puuttuvat. Kuorman pito vaaditaan (§7). Ks. [p2-variable-pump § Ankkurivinssi](design/p2-variable-pump.md#ankkurivinssi-ja-muut-kuormat-samassa-kytkennässä) |
| PWW | Painepesuri | mahdollinen | matala | Hydraulimoottorilla käytetty pesuri; laite ei vielä valittu. **Jatkuva kuorma**, joten öljyn lämpö ratkaisee (ks. [oil-cooling](design/oil-cooling.md)); käytetään satamassa tyhjäkäynnillä |
| DAV | Nosturi / jollan daavitti | epätodennäköinen | keskitaso | Kuorman pito vaaditaan (kuormanpitoventtiilit, §7) |

Kolme mahdollista apupiirin kuormaa mahtuu pohjalaatan kolmeen vapaaseen paikkaan, joten
pohjalaattaa ei tarvitse vaihtaa [laskelma]. Kaikki saavat enintään saman virtauksen ja paineen kuin
keulapotkuri (noin 34 l/min, 250 bar).

## 6. Käyttötilanteet (samanaikaisuus)

> Pumpun mitoituksen ratkaisee pahin *realistinen* kuormien yhdistelmä, ei kaikkien summa.

| Tilanne | Kuvaus | Samanaikaiset kuormat | Kesto | Kone käy? |
|---|---|---|---|---|
| S1 Satamamanööverit | Laituriin tulo, ahtaat käännökset | STR, BTH | TBD | kyllä |
| S2 Ankkurointi | Ankkurin lasku ja nosto | WLS, STR, BTH | TBD | TBD |
| S3 Matka-ajo | Pitkäkestoinen ohjaus | STR | tunteja | kyllä |
| S4 Hätätilanne | Päätehonlähde menetetty | STR (vähintään) | TBD | ei |
| S5 Pesu satamassa | Kannen tai rungon pesu painepesurilla | PWW (STR lepotilassa) | TBD, mahdollisesti pitkä | kyllä, tyhjäkäynti |

**Mitoittava tilanne:** TBD (todennäköisesti S1 tai S2)

## 7. Turvallisuus, varmennus ja vikatilanteet

> Päätä jokaiselle kriittiselle toiminnolle, mitä tapahtuu, kun pumppu, tehonlähde, letku tai
> ohjaus pettää. Tässä kohdassa ihmisen insinöörinharkinta on tärkeintä.

| Toiminto | Vika | Vaadittu toiminta | Varakeino |
|---|---|---|---|
| Ohjaus | Pumpun tai tehon menetys | TBD | Hätäpinna / sähköinen varapumppu / orbitroli käsipumppuna |
| Ohjaus | Letkun tai liittimen repeämä | TBD | Sulkuventtiilit, erilliset piirit |
| Autopilotti | Venttiili jää auki tai ohjain antaa väärän käskyn (peräsin ajaa ääriasentoon) | Peräsimen ohjaus palaa heti ruorille: autopilotin kelojen virta katkeaa, ja jousi palauttaa venttiilin keskiasentoon | Ruorilla autopilotin pääkytkin (katkaisee kelojen virran, ei pelkkä ohjelmallinen pois-tila); hätäohitus 1V3 |
| Autopilotti | Peräsinkulma-anturin vika | Autopilotti kytkeytyy pois ja hälyttää | Käsiohjaus orbitrolilla |
| Ankkurivinssi | Tehon menetys ankkurin ollessa puoliksi ylhäällä | Kuorman pito (jarru / jarruventtiili) | Käsinosto |
| Nosturi / daavitti | Letkun repeämä tai tehon menetys kuorma ylhäällä | Kuorma ei saa pudota: kuormanpitoventtiilit suoraan sylinterissä | Kuorman lasku käsin avattavalla venttiilillä |
| Painepesuri | Letkun tai pesupistoolin vika | Pesuri pysähtyy, kun suuntaventtiili palaa keskelle | |
| Keulapotkuri | Ylikuorma / ylikuumeneminen | TBD | Paineenrajoitus, lämpösuoja |
| Kaikki | Matala öljynpinta | Hälytys, sitten ei-kriittisten kuormien suojapysäytys | |
| Kaikki | Korkea öljyn lämpötila | Suositeltu käyttölämpötila 40–60 °C (Sleipner); varoitus ~65 °C, hälytys ~70 °C (HV 32 -öljy ohenee 70 °C:n yläpuolella alle Salamin ohjauspumpun 12 cSt:n minimin; Parker F1:n raja 75 °C) | Öljynjäähdytin, kierroslukitus |

- **Hätäpysäytyksen periaate:** TBD
- **Kuormien prioriteetti** (mitkä pudotetaan ensin, kun teho ei riitä): TBD
- **Keulapotkurin iskuventtiilit:** Sleipner suosittelee vahvasti iskuventtiilejä 10–15 % valitun
  maksimipaineen yläpuolelle (suojaa, jos potkurit jumittuvat) [ohje Sleipner 2746 35 2025]. **Ei lisätä**
  (päätös 2026-10-23): BAV-713:n kelluva keskiasento ja VMP 250 bar rajaavat painepiikit.
- **Paineenrajoitus / suurin järjestelmäpaine:** apupiiri 250 bar (päätetty; ~90 %:n keulapotkuriteho
  hyväksytty kustannussyistä). Ohjauspiiri TBD.
- **Suojaus tahattomalta liikkeeltä:** TBD

## 8. Asennuksen rajoitteet

| Kohde | Rajoite |
|---|---|
| Tila voimayksikölle / säiliölle | TBD (paikka, P×L×K) |
| Säiliön sijainti suhteessa pumppuihin | Säiliön öljypinta vähintään 1 m P1:n ja P2:n imuaukkojen yläpuolella [omistaja 2026-10-26]. Ratkaiseva on öljypinnan korkeus, ei säiliöliitännän; imuletku laskee koko matkan säiliöltä pumpulle ilman ilmaa kerääviä yläkohtia. |
| Painobudjetti | TBD kg |
| Putki- ja letkuvedot | Keulapotkurin A/B-linjat: 1/2" letku, asennettu (CETOP → keula). Muut TBD (laipiolävistykset, palo-osastot). |
| Huollettavuus | TBD (suodattimet, tarkastuslasi, ilmauspisteet) |
| Öljynjäähdytin | Bowman EC100 tai EC80 (varalla, malli ⚠ tarkista), merivesi koneen merivesipiiristä, yhteiseen paluulinjaan ohitusventtiilin kanssa; ks. [oil-cooling.md](design/oil-cooling.md) |

## 9. Öljy, puhtaus ja huolto

| Kohde | Vaatimus |
|---|---|
| Öljytyyppi | Mineraalipohjainen **HVLP** (DIN 51524-3 / ISO 11158 HV); HEES ei tarpeen. **Päätetty 2026-10-23**, ks. [hydraulic-oil.md](design/hydraulic-oil.md) |
| Viskositeettiluokka | Suositus **HVLP 32** (DIN 51524-3), VI ≥ 150, mieluiten > 180, Parker HF-0; esim. Teboil Hydraulic Oil 32S. Ainoa luokka, joka pysyy kaikkien komponenttien rajoissa 0 °C:sta noin 72 °C:seen (P1:n 12 cSt:n minimi). **Päätetty 2026-10-23**, ks. [hydraulic-oil.md](design/hydraulic-oil.md) |
| Puhtaustavoite | Herkimmän komponentin mukaan: P2 on PVH57 (päätös 2026-10-27), joten **16/14/12** (250 bar) [Eaton PVH s. 31]. (F1-61:llä olisi riittänyt 20/18/13.) Ks. [paperisuodattimen riittävyys](design/p2-variable-pump.md#riittääkö-nykyinen-paperisuodatin) |
| Suodatus | Paluusuodatin säiliön kannella; nykyinen OMTF112C10NA2 ei riitä PVH57:lle; ehdokas OMTF171F10NA1. Suodattava huohotin **⚠ päättämättä** |
| Huoltoväli | TBD |
| Vuotojen keräys | TBD |

## 10. Valvonta, ohjaus ja integrointi

> Integrointi Vegan nykyiseen järjestelmään: Signal K -palvelin, NMEA 2000 -nodet ja ESP32
> PDM -kortit. Signal K:ssa ei ole vakiopolkuja hydrauliikalle, joten alla olevat polut ovat ehdotus.

### 10.1 Anturit

| Mittaus | Paikka | Alue | Ehdotettu Signal K -polku | Hälytys / raja |
|---|---|---|---|---|
| Ohjauspaine (1B2, ehdotus) | Piiri 1, RPF3:n CF-lähtö (1G1:n rinnalla) | 0–250 bar | `hydraulics.steering.pressure` | Normaali < 50 bar; hälytys TBD. Ks. [pressure-monitoring.md](design/pressure-monitoring.md) |
| Öljyn lämpötila | Säiliö / paluu | 0–100 °C | `hydraulics.<system>.temperature` | Varoitus ~65 °C, hälytys ~70 °C. **Päätetty 2026-10-23** |
| Öljynpinta | Säiliö | % | `hydraulics.<system>.level` | TBD |
| Suodattimen paine-ero | Paluusuodatin | kytkin / bar | `hydraulics.<system>.filter.clogged` | TBD |
| P2:n lähtöpaine (2B2, ehdotus, prioriteetti 1) | PVH57:n painelähtö | 0–400 bar | `hydraulics.<system>.pump.pressure` | Valmiustila noin 20 bar; hälytys, jos paine pysyy korkeana, kun mitään toimintoa ei käytetä (LS-purku jumissa). Ks. [pressure-monitoring.md](design/pressure-monitoring.md) |
| Imupaine | P2:n imuaukko | −1…+1 bar | `hydraulics.<system>.pump.inletPressure` | Varoitus alle 0 bar (PVH57 mobiili: 2400 rpm imupaineella 0 bar), hälytys alle ~−0,2 bar. **Päätetty 2026-10-23.** P1: mittaus käyttöönotossa, ei kiinteää anturia |
| Peräsinkulma | Peräsinakseli | ± ° | `steering.rudderAngle` (vakio) | |

### 10.2 Ohjaus

- **Ohjauspaikat:** TBD (ohjauspisteet, langattomat kaukosäätimet, MFD, autopilotti)
- **Ohjauselektroniikka:** TBD (ESP32 PDM -lähdöt solenoideille ja kytkimen toimilaitteelle, CAN/N2K)
- **Autopilotin liitäntä:** solenoidiventtiiliohjaus ohjauspiirissä [omistaja 2026-10-25]; autopilotin
  merkki TBD. Ks. [§10.3](#103-autopilotin-liitäntä-ohjauspiiriin).
- **Lukitukset:**
  - Keulapotkuri käytettävissä vain alle noin 1000 rpm:ssä.
  - ~~BPV-lukitukset~~: BPV:tä ei tule, P2 on PVH57 (päätös 2026-10-27). LS-purun ohjausjärjestys
    riippuu venttiilikokoonpanosta, ks. [p2-variable-pump](design/p2-variable-pump.md#suositus-kaksitiekompensoitu-virtauksensäätö-ja-ls-purku)
    ja [LS + on/off: kierroslukitus](design/aux-circuit-ls-onoff.md#tarvitaanko-kierroslukitus). **⚠ päätetään kokoonpanon kanssa**.
  - Muut TBD.

### 10.3 Autopilotin liitäntä ohjauspiiriin

> Lisätty 2026-10-25. Ehdotus, ei päätetty. Autopilotti on turvallisuuskriittinen: pätevän henkilön
> pitää tarkistaa kytkentä ennen rakentamista.

Omistajat haluavat autopilotin ohjaavan peräsintä suuntaventtiileillä ohjauspiirin omalla öljyllä,
ei erillisellä autopilottipumpulla [omistaja 2026-10-25].

**Nykyinen orbitroli sopii tähän.** HKUS 160/4 on avoimen keskiasennon malli ilman
kuormantakaisinkytkentää [datalehti HKUS]. Lepoasennossa sylinterin liitännät ovat siis kiinni, joten
autopilotti voi liikuttaa sylinteriä ilman että ruori pyörii mukana.

**Autopilotille erotetaan pieni oma virtaus orbitrolin edestä** [laskelma]. Avoimen keskiasennon
orbitroli päästää RPF3:n 20 l/min:n virtauksen lepoasennossa matalalla paineella säiliöön, joten
suoraan sen rinnalle kytketty venttiili ei saisi painetta. Siksi RPF3:n CF-lähdön ja orbitrolin väliin
tulee toinen, pieni kolmitievirtauksensäätöventtiili (prioriteettiventtiili, samaa tyyppiä kuin RPF3):

```
RPF3 CF ── pieni prioriteettiventtiili ── CF noin 1–2 l/min ── 4/3 autopilottiventtiili (suljettu keskiasento) ── A/B → T-liittimet sylinterilinjoihin
                                       └─ EF loput ─────────── orbitrolin P (käsiohjaus kuten nyt)
autopilottiventtiilin T ── säiliöön (ei orbitrolin T-linjaan, jonka raja on 25 bar)
```

- Kun autopilotti ei ohjaa, sen venttiili on keskellä ja kiinni. Prioriteettiventtiili ohjaa silloin
  kaiken öljyn orbitrolille, ja käsiohjaus toimii kuten nyt.
- Kun autopilotti ohjaa, se saa pienen vakiovirtauksen paineesta riippumatta, ja loput menevät
  orbitrolille. Käsiohjaus toimii siis edelleen, mutta se ottelee autopilottia vastaan, kunnes
  autopilotti kytketään pois.
- **Autopilotin haaraan tarvitaan oma paineenrajoitus** (enintään sylinterin ja letkujen
  painearvo), koska orbitrolin sisäinen paineenrajoitus ei suojaa sitä. Peräsimen ollessa
  ääriasennossa rajoittimen yli menee vain pieni virtaus, joten lämpöä syntyy vähän (noin 1,5 l/min ×
  100 bar ≈ 0,25 kW hetkellisesti; paine on esimerkki) [laskelma].
- Virtaa **ei kannata kuristaa pelkällä kuristimella** RPF3:n perässä. Silloin lähes koko 20 l/min
  menisi paineenrajoittimen yli ja lämpenisi (esim. 20 l/min × 100 bar ≈ 3 kW aina, kun autopilotti
  ohjaa) [laskelma].

**Autopilotin virtauksen mitoitus** [laskelma]. Sylinterin (Ø 60 / Ø 35 mm, isku 100 mm) tilavuus on
männän puolella noin 283 cm³ ja varren puolella noin 187 cm³. RPF3:n täydellä 20 l/min:n virtauksella
peräsin kääntyisi laidasta laitaan alle sekunnissa, mikä on autopilotille aivan liian nopeaa.
Esimerkiksi noin 12 sekunnin kääntöaika vastaa noin 1,4 l/min:n virtausta (oletus: koko 100 mm:n isku
käytössä, **⚠ tarkista**; sopiva kääntöaika valitaan autopilotin mukaan). Vaihtoehtona on
proportionaalinen venttiili, jos autopilotti osaa ohjata sitä.

**Tarvittavat lisäosat** (arvio, malleja ei valittu): pieni kolmitievirtauksensäätöventtiili (noin
1–2 l/min, näin pienen kiinteän virtauksen mallien saatavuus **⚠ tarkista**; vaihtoehtona säädettävä),
4/3-solenoidiventtiili suljetulla keskiasennolla (24 V, pieni virtaus, esim. CETOP 3),
paineenrajoitusventtiili, kaksi T-liitintä sylinterilinjoihin, peräsinkulma-anturi (§10.1), autopilotin ohjausyksikkö, joka
osaa ohjata solenoidiventtiiliä, sekä pääkytkin ruoriin.

**Toimii vain, kun ohjauspiirissä on öljyä:** kone käy (P1) tai sähköinen varapumppu P3 on päällä.

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
