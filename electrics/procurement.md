# Sähköjärjestelmän hankintalista

> **Tila:** Koottu 2026-10-31 päätöksistä ja selvityksistä. Hinnat ovat jälleenmyyjien hintoja
> (haettu 2026-10-28…31) tai arvioita, ja ne on merkitty. Dollarit ja punnat on muunnettu arviolla
> noin 0,9 €/USD ja 1,15–1,2 €/GBP. Päivitä lista, kun osa ostetaan, löytyy veneeltä tai suunnitelma
> muuttuu. Perustelut ovat linkeissä.

**Tila-sarake:** ✅ olemassa tai ostettu · 🛒 hankitaan · 🔍 tarkista ensin (ks. "Ennen tilausta") ·
❓ ehdollinen · ⏳ myöhemmin

**Turvallisuus:** akusto, BMS-kytkennät, pääsulakkeet, P3:n syöttö, tärkeiden kuormien kisko ja 230 V:n
asennus tarkastutetaan pätevällä sähköasentajalla ennen käyttöönottoa.

## 1. Käyttöakusto

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 1.1 | EVE MB31 314 Ah, LiFePO4 | 16 | kaksi 8S-akkua, noin 16 kWh; Grade A, mittausraportti | 🔍 | 129,95 €/kpl → **≈ 2 080 €** (Akkula 2026-10-28) | [päätös 2026-10-31](../decisions.md), [house-battery](design/house-battery.md) |
| 1.2 | JK-PB2A16S20P (BMS) | 2 | 8S, 200 A, kaksi kuivakosketinta, CAN | 🔍 | **⚠ ei tiedossa** (Nkon) | [inverter-bms 5.1](design/inverter-bms.md#51-ennen-tilausta-tarkistettu-2026-10-31) |
| 1.3 | Joustavat kuparikiskot, nikkelöity | 14 + varaa | kennojen väliin (7/akku), jos myyjän kiskot ovat jäykkiä | ❓ | **⚠ ei tiedossa** | [house-battery 3](design/house-battery.md#3-mitä-itse-koottu-akusto-vaatii-kennojen-lisäksi) |
| 1.4 | Class T -pääsulake ja pidike | 2 | akkukohtainen, akun navan lähelle; koko invertterin ja kuormien mukaan | 🛒 | **⚠ ei tiedossa** | [dc-distribution 4](design/dc-distribution.md#4-sulakkeet-ja-kaapelit) |
| 1.5 | Akkukohtainen pääkytkin | 2 | vähintään noin 300 A | 🛒 | **⚠ ei tiedossa** | [house-battery 3.1](design/house-battery.md#31-kotelointi-selvitetty-2026-10-31) |
| 1.6 | Kotelon materiaalit: FR4-päätylevyt, kierretangot, FR4-eristelevyt 0,5–1 mm, kansi, läpivientikumit | 2 sarjaa | oma kotelo; mitat kun paikka ja puristusvoima tiedetään | ⏳ | **⚠ ei tiedossa** | [päätös 2026-10-31](../decisions.md) |
| 1.7 | Kiinnityskehikko runkoon (teräs, hitsattu) | 1 | tila myös kolmannelle akulle | ⏳ | **⚠ ei tiedossa** | sama |
| 1.8 | Kolmas 8S-akku (8 × MB31 ja BMS) | – | optio, ei hankita nyt | ⏳ | noin 1 040 € ja BMS | [päätös 2026-10-31](../decisions.md) |

## 2. Invertterilaturi, valvonta ja lataus

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 2.1 | Victron MultiPlus-II 24/5000/120-50 230V (PMP242505010) | 1 | 4 kW, laturi 120 A, PowerAssist | 🔍 | **≈ 1 700–2 400 €** | [päätös 2026-10-31](../decisions.md), [ac-power-source 2.2](design/ac-power-source.md#22-huipputeho-ja-invertteri-laskelma) |
| 2.2 | Victron **Cerbo GX MK2** (omistaja pitää hyvänä ajatuksena 2026-11-08) | 1 | BMS-CAN-portti (ei Cerbo-S GX); VE.Can-portti 1 galvaanisesti erotettu NMEA 2000:lle, ks. [nmea2000-network 4](design/nmea2000-network.md#4-väylät-erillään). MK2:n hinta ja BMS-CAN-portti **⚠ tarkista** | 🛒 | noin 290–340 USD ≈ **260–310 €** | [inverter-bms 3.1](design/inverter-bms.md#31-mihin-cerbo-gx-tarvitaan-lisätty-2026-10-31) |
| 2.3 | Näyttö Cerbo GX:lle (esim. GX Touch) | 1 | valinnainen; puhelin tai Signal K riittää | ❓ | **⚠ ei tiedossa** | – |
| 2.4 | CAN-kaapeli JK → Cerbo GX (BMS-CAN) | 1–2 | johdinjärjestys tarkistettava | 🛒 | **⚠ ei tiedossa** | [inverter-bms](design/inverter-bms.md) |
| 2.5 | Timco SS2200i Supersilent | 1 | 1,8 kW, varalataus avokannelta | 🛒 | **549 €** | [päätös 2026-10-31](../decisions.md) |
| 2.6 | Aggregaatin liitosjohto maasähköpistokkeeseen | 1 | aggregaatin 230 V:n pistorasiasta veneen maasähkötuloon | 🛒 | **⚠ ei tiedossa** | [ac-power-source D](design/ac-power-source.md#d-kannettava-bensiiniaggregaatti-varalataukseen-selvitetty-2026-10-31) |
| 2.7 | Aggregaatin ja bensiinin säilytyskaappi kannella | 1 | tuulettuva, valuu laidan yli | 🛒 | **⚠ ei tiedossa** | sama |
| 2.8 | Erotusmuuntaja Airlink WM5002 | 1 | olemassa, ei kytketty | ✅ | – | [ac-power-source 2.6](design/ac-power-source.md#26-olemassa-oleva-erotusmuuntaja-airlink-wm5002) |
| 2.9 | Toinen laturi 24 V / 150–175 A (esim. Prestolite 175 A) | 1 | mahtuuko koneen etupäähän **⚠ tarkista** | ⏳ | noin 1 304 € (Prestolite) | [ac-power-source 2.5](design/ac-power-source.md#25-toisen-laturin-hintataso-haettu-2026-10-28) |
| 2.10 | Säädin: Mastervolt Alpha Pro III (45513000) | 1 | päätetty 2026-10-31; molempien JK:iden kuivakoskettimet sarjassa Reg on -johtimeen; laturin kenttäohjaus N-tyyppinen **⚠ tarkista** | ⏳ | 330–450 USD ≈ 300–405 € | [päätös 2026-10-31](../decisions.md), [inverter-bms 5.2](design/inverter-bms.md#52-toisen-laturin-säädin-alpha-pro-iii-vai-wakespeed-ws500-selvitetty-2026-10-31) |
| 2.11 | Laturin lämpötila-anturi 41500400 (Alpha Pro III) | 1 | | ⏳ | noin 17–26 USD | sama |
| 2.12 | Sterling APD24 (laturin varasuoja) | 1 | | 🛒 | **⚠ ei tiedossa** | [ac-power-source](design/ac-power-source.md) |
| 2.13 | Laturin kiinnike ja hihna | 1 | CAT 3126B:n etupää, 5–7 kW | ⏳ | **⚠ ei tiedossa** | sama |

## 3. Jakelu ja suojaus

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 3.1 | Talojohdonsuoja, jonka datalehdessä on DC-arvo (esim. Schneider iC60N, C-käyrä) | noin 32 | 2–16 A piirilistan mukaan; DC-arvo tarkistettava | 🔍 | 6–9 €/kpl → **≈ 190–290 €** | [päätös 2026-10-31](../decisions.md), [circuit-list](design/circuit-list.md) |
| 3.2 | Suljettu DIN-kotelo (IP-luokka) | 3 | KS, KH ja TK | 🛒 | 30–60 €/kpl **⚠ arvio** | [dc-distribution 4.5](design/dc-distribution.md#45-sulakkeiden-hintavertailu-haettu-2026-10-31) |
| 3.3 | Suurten lähtöjen sulakkeet ja pidikkeet (MEGA, ANL tai MRBF) | noin 6 | invertteri, P3, toinen laturi, KS-, KH- ja TK-syötöt | 🛒 | **⚠ ei tiedossa** | [circuit-list](design/circuit-list.md) |
| 3.4 | Plus- ja miinuskiskot pääjakeluun | 1 sarja | | 🛒 | **⚠ ei tiedossa** | [dc-distribution 2.1](design/dc-distribution.md#21-pääjakelu-pj-konehuone) |
| 3.5 | Ideaalidiodi: Victron Argo FET 100-2 | 2 | yksi kummallekin akustolle, lähtö TK-kiskoon; käyttötapa tarkistettava Victronilta | 🔍 | 109 €/kpl → **≈ 220 €** | [dc-distribution 3.4](design/dc-distribution.md#34-tärkeiden-kuormien-kiskon-osat-selvitetty-2026-10-31) |
| 3.6 | Hätärinnankytkin: Victron Battery Switch ON/OFF 275A | 1 | normaalisti auki, merkitään | 🛒 | noin 33–37 € | sama |
| 3.7 | Vipukytkimet komentosillan paneeliin | noin 4 | kulkuvalot, ankkurivalo, VHF, hakuvalon rele | 🛒 | **⚠ ei tiedossa** | [circuit-list](design/circuit-list.md) |
| 3.8 | ESP32-PDM-kortit | noin 6 + 2 | 4-kanavaiset ja suurivirtakortit; oma projekti | ⏳ | **⚠ ei tiedossa** | [circuit-list](design/circuit-list.md#pdm-kanavien-tarve-laskelma-arvio) |
| 3.9 | Tinattu venekaapeli (eri poikkipinnat) ja kaapelikengät | – | koot mitattujen pituuksien mukaan | ⏳ | **⚠ ei tiedossa** | [dc-distribution 4.2](design/dc-distribution.md#42-jännitehäviö-ja-kaapelin-koko-laskelma) |
| 3.10 | 230 V: vikavirtasuoja 30 mA, johdonsuojat, kotelo | 1 sarja | sähköurakoitsija | ⏳ | **⚠ ei tiedossa** | [dc-distribution 6](design/dc-distribution.md#6-230-vn-jakelu) |

## 4. Kuormiin liittyvät

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 4.1 | Hakuvalon rele, 24 V, vähintään noin 30 A, hehkulamppukuorma | 1 | | 🛒 | **⚠ ei tiedossa** (autorele arviolta 10–20 €) | [päätös 2026-10-31](../decisions.md), [searchlight-deicing](design/searchlight-deicing.md#3-ohjaus-ja-kytkentä) |
| 4.2 | Hakuvalon varapolttimot A1/223 (EHJ), 24 V 250 W, G6.35 | 3–4 | nykyinen polttimo Philips 7748S [omistaja 2026-11-03]; käyttöikä 50 h | 🔍 | noin 9,38 £/kpl (BLT Direct) | [searchlight-deicing](design/searchlight-deicing.md) |
| 4.3 | Hakuvalon suojahuppu | 1 | | 🛒 | muutamia kymmeniä euroja **⚠ arvio** | sama |
| 4.4 | Häkävaroitin makuutiloihin | 2–3 | öljylämmitin, kaasuliesi, aggregaatti | 🛒 | **⚠ ei tiedossa** | [ac-power-source D](design/ac-power-source.md#d-kannettava-bensiiniaggregaatti-varalataukseen-selvitetty-2026-10-31) |
| 4.5 | Kaasuhälytin ja kaasun magneettiventtiili | 1 | suositus; kaasuasennuksen osana | ❓ | **⚠ ei tiedossa** | [loads.yaml](loads.yaml) |
| 4.8 | Pilssi- ja ylävesihälytin Rule 32ALA (24 V) | 1 | TK-07; lisäksi kosketin NMEA 2000 -nodeen | 🛒 | noin 98–124 € | [dc-distribution 3.4](design/dc-distribution.md#34-tärkeiden-kuormien-kiskon-osat-selvitetty-2026-10-31) |
| 4.6 | Maseraattori-WC ja septin hätätyhjennyspumppu (24 V) | 1 + 1 | päätetty; mallit valitsematta | ⏳ | **⚠ ei tiedossa** | [päätös 2026-10-31](../decisions.md) |
| 4.7 | Yhdistetty mikro- ja sähköuuni | 1 | päätetty; malli valitsematta | ⏳ | **⚠ ei tiedossa** | sama |

## Yhteenveto: tiedossa olevat hinnat [laskelma, ⚠ arvio]

| Ryhmä | Hinta |
|---|---|
| Kennot (1.1) | ≈ 2 080 € |
| MultiPlus-II 24/5000 ja Cerbo GX (2.1–2.2) | ≈ 1 960–2 710 € |
| Aggregaatti (2.5) | 549 € |
| Johdonsuojat ja DIN-kotelot (3.1–3.2) | ≈ 280–470 € |
| Tärkeiden kuormien kisko: diodit, hätärinnankytkin, ylävesihälytin (3.5, 3.6, 4.8) | ≈ 350–380 € |
| **Yhteensä tiedossa olevat** | **≈ 5 220–6 190 €** |
| Toinen laturi, Alpha Pro III ja anturi (2.9–2.11, myöhemmin) | ≈ 1 620–1 730 € |

Puuttuu: JK-BMS:t, Class T -sulakkeet, pääkytkimet, suuret sulakkeet, kaapelit, kotelot ja
kiinnitykset sekä asennus. Ne ovat arviolta useita satoja euroja (**⚠ arvio**).

## Ennen tilausta selvitettävät

- [ ] **MultiPlus-II 24/5000:** pienin tulovirran raja PowerAssistin kanssa (tavoite alle noin 7,5 A
  Timco SS2200i:lle). Kysy Victron-jälleenmyyjältä ([inverter-bms 5.1](design/inverter-bms.md#51-ennen-tilausta-tarkistettu-2026-10-31))
- [ ] **JK-PB2A16S20P:** hinta, laitteistoversio, CAN-nopeus ja Victron-protokolla
- [ ] **MB31:** hinta, Grade A -todistus, mittausraportti, napatyyppi; EVE:n datalehdestä puristusvoima ja kiristysmomentti
- [ ] **Johdonsuojat:** valitun mallin DC-arvo datalehdestä
- [ ] **Akuston ja invertterilaturin paikka** veneellä ([tarkistuslista](boat-checklist.md)) ennen kennojen ja kotelon tilausta
- [x] **Hakuvalon polttimon tyyppi:** Philips 7748S, EHJ / A1/223, G6.35 [omistaja 2026-11-03]
- [ ] **Vakuutusyhtiön kanta** itse koottuun akustoon ja bensiinin säilytykseen

**Voi tilata jo nyt:** Timco SS2200i (2.5) ja Cerbo GX (2.2). Kennot kannattaa tilata vasta, kun
paikka ja kotelo ovat valmiit, jotta niitä ei säilytetä pitkään kytkemättöminä.
