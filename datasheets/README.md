# Datalehdet

Hakemisto Vegan järjestelmissä käytetyistä ja arvioiduista komponenttien datalehdistä,
käyttöohjeista ja tuotesivuista.

- **Repoon ei tallenneta valmistajien PDF:iä.** Repo on julkinen, ja datalehdet ovat valmistajien
  tekijänoikeuden alaisia. Tähän kirjataan linkki, mistä tiedosto löytyy, ja tärkeimmät arvot.
- **Omat kopiot** voi tallentaa omalle koneelle kansioon `datasheets/local/`. Git ei vie sitä
  GitHubiin (ks. `.gitignore`), joten kopiot eivät näy muille eivätkä Claude Coden verkkoversiolle.
- **Skannatut PDF:t:** moni datalehti on skannattu. Merkintä *kuvana* tarkoittaa, että arvot on luettu
  sivujen kuvista.
- **Uusi datalehti:** lisää rivi oikeaan taulukkoon ja linkki dokumenttiin, jossa sitä käytetään.

## Pääkone ja voimansiirto

| Komponentti | Dokumentti | Tärkeimmät tiedot | Käytetään |
|---|---|---|---|
| Caterpillar 3126B | [Esite, Scribd](https://www.scribd.com/document/832207648/3126B) | Tyhjäkäynti 700 rpm (teholuokka epäselvä) | [vessel](../vessel/README.md#tyhjäkäyntikierrokset) |
| Caterpillar merimoottorit (vertailu) | [cat.com, tuotesivu](https://www.cat.com/en_US/products/new/power-systems/marine-power-systems/commercial-propulsion-engines/18408926.html) | Ohjelmoitava tyhjäkäynti 550–750 rpm | [vessel](../vessel/README.md#tyhjäkäyntikierrokset) |
| Advance 300 -merivaihde | [advance-gearboxes.eu](https://www.advance-gearboxes.eu/advance-gearboxes/medium-heavy-duty-gearboxes/advance-300-5441/) | Välitys ~5,4:1. PTO 1:1, 0,044 kW/rpm ja Ø48 kiila-akseli on saatu omistajilta, ei tästä. **⚠ Käyttöohje puuttuu** (PTO:n pyörimissuunta, jäähdyttimen merivesivirtaus). | [vessel](../vessel/README.md) |

## Hydrauliikka: pumput

| Komponentti | Dokumentti | Tärkeimmät tiedot | Käytetään |
|---|---|---|---|
| **Parker F1-061-R---000 (3781060)** | [Asennus- ja käyttöönotto-ohje HY30-8201 (pzip.ru)](https://pzip.ru/downloads/parker/HY30-8201-INST_EU.pdf?sku=3781060) | Ei vuotolinjaa; pyörimissuunnan vaihto (päätykappale 180°, 80–100 Nm); imuliitin ≥ 38 mm ≤ 60 l/min:lle; viskositeetti 10–400 cSt (suositus 20–30), käynnistys ≤ 4000 cSt; öljy ≤ 75 °C | [p2-pump-options](../hydraulics/design/p2-pump-options.md#ehdokas-parker-f1-061-käytettynä-torifi) |
| Parker F1-061 (3781060) | [Jälleenmyyjän tuotesivu (pzip.ru)](https://pzip.ru/catalog/parker/3781060) | 350–400 bar; DIN 5462 B8×32×36 -akseli; ISO | sama |
| **Parker Truck Hydraulics -luettelo MSG30-8200/UK** (GPA/GP1, F1, T1, F2, F3, F4, VP1, BPV) | [PDF (dzwigi.net.pl)](https://cdn.dzwigi.net.pl/b/v2/3781800/Document/MSG30-8200-UK-6758536ce15df.pdf); F1-sivut 22–29 [erikseen](https://cdn.dzwigi.net.pl/b/v2/3784050/Document/Parker_MSG30-8200_UK-022-029.pdf) | F1-61 (378 1060 = F1-61-R): **59,5 cm³**, 400 bar, itseimevä ≤ 2400 rpm, lyhytsuljettuna ≤ 2700 rpm, 378 Nm teor.; **imupaine ≥ 1,0 bar abs**; imulinja ≤ 1,0 m/s; imuliitin tilattava erikseen, F1-41…-61:lle suositus Ø50 (378 0636 / 0364 / 0979); suodatus ISO 4406 20/18/13; BPV s. 65–66. Muut sarjat: F1-51 itseimevä 2450 rpm; T1 kevyeen kippikäyttöön; F3/F4 paineilmakytkin (5–10 bar); VP1-045…-128 LS + BPV-VP1 379 8799; BPV-L 378 1487 (linjaan, 250 l/min) | [p2-pump-options](../hydraulics/design/p2-pump-options.md#tiedot), [muut Parkerin pumput](../hydraulics/design/p2-pump-options.md#muut-parkerin-pumput-ja-kuorman-purku-selvitys-2026-10-23) |
| **Parker BPV-F1/T1 -datalehti** | [paro.nl](https://paro.nl/library//storage/datasheets/Parker/UK/Parker_BPV-F1-BPV-T1_uk.pdf/datasheet.html) | F1-25…-61 ja T1-81: 378 4179 / 7201 / 7202, liitin 50 Nm; **F1-81/-101 ja T1-121: 378 4180 / 7203 / 7204, liitin 100 Nm (eri venttiili)**; 350/400 bar, 14 W | [p2-pump-options](../hydraulics/design/p2-pump-options.md#tiedot) |
| Hydrauliöljyt HVLP 32 (tuotesivut) | [Teboil 32S](https://www.am-asennus.fi/tuote/teboil-hydraulic-oil-32s-20l/), [Valvoline Ultramax HVLP 32](https://www.am-asennus.fi/tuote/valvoline-ultramax-hvlp-32-hydrauliikkaoljy-20l), [Motox 32 Universal HVLP](https://www.motonet.fi/tuote/motox-32-universal-hvlp-hydraulic-oil-1-l-hydraulioljy?product=59-6100), [Neste 46 Super](https://neste.fi/tuote/neste-hydraulic-46-super_en) | Teboil 32S: DIN 51524-3 HVLP, Parker HF-0, 104,90 €/20 l; Valvoline: VI 144, 6,2 cSt 100 °C:ssa, 97,90 €/20 l; Neste 46 Super VI > 185 (haettu 2026-10-23) | [hydraulic-oil](../hydraulics/design/hydraulic-oil.md) |
| Parker F1 -sarja | [Parker, tuotesivu](https://ph.parker.com/us/en/axial-piston-fixed-pumps-series-f1) | 350 bar jatkuva / 400 bar (ISO); ≤ 2600 rpm 350 barissa. **⚠ F1-luettelo (koko datalehti) puuttuu**, mm. pienin imupaine. | sama |
| Parker BPV-F1 -asennusohje MSG30-8227-INST/UK/DE (2023) | [PDF (dzwigi.net.pl)](https://cdn.dzwigi.net.pl/b/v2/3781080/Document/Broszura-informacyjna-Bypass-Valves-BPV-dla-F1-T1-675832260051b.pdf) | **Vuotolinja pakollinen**, suoraan säiliöön öljypinnan alle; vuotoliitinsarja 378 3039 mukana; kiristykset 50 / 20–25 / 46 / 8 Nm; käsiohitus (kone sammuksiin ensin) | [p2-pump-options](../hydraulics/design/p2-pump-options.md#lisävaruste-parker-bpv-f1--ohitusventtiili) |
| **Parker BPV-F1-25 -ohitusventtiili** (F1-25…-61) | [Parker HY30-8200/PL s. 47–48 (dzwigi.net.pl)](https://cdn.dzwigi.net.pl/b/v2/3787424/Document/zawory%20bocznikowe%20BPV%20Parker.pdf) (puolaksi, osin *kuvana*); [MSG30-8200/UK s. 60 (paro.nl)](https://paro.nl/library//storage/datasheets/Parker/UK/Parker_BPV-F1-BPV-T1_uk.pdf/datasheet.html); [hinnat (dzwigi.net.pl)](https://dzwigi.net.pl/en/sklep/4957-bpv.html) | Jännitteettömänä ohitus (painelähtö → imu), jännitteellisenä syöttää piiriin; vaihto vain alle 20 barissa; vuotolinja (BSP 1/4") säiliöön; 350/400 bar; 24 VDC 14 W; 24 VDC: 378 7201 / 378 4179 (vanha 378 1401); ~1814 PLN + ALV | [p2-pump-options](../hydraulics/design/p2-pump-options.md#lisävaruste-parker-bpv-f1--ohitusventtiili) |
| VNK3 ryhmän 3 hammaspyöräpumppu (Flowfit) | Flowfitin datalehti, ks. kytkinkokoonpano alla (s. 1–2, *kuvana*) | 43 ja 51 cm³: 250 bar jatkuva / 300 huippu; 60 cm³: 200 / 250 bar | [p2-pump-options](../hydraulics/design/p2-pump-options.md) |
| Sunfab SCP (SAE) | [Sunfab, luettelo](https://www.sunfab.com/media/ocuftr3s/3106en2110scp-012-108-sae.pdf) | SCP 064: 63,5 cm³; 350–400 bar; 1900 rpm jatkuva | vertailu |
| Casappa Polaris PLP30 | [Hydraspecma, PLP30.61D](https://www.hydraspecma.com/store/no/en/find/item/03599158) | 61 cm³: vain 160 bar jatkuva | vertailu |
| Marzocchi GHP | [Marzocchi, luettelo](https://pdf.directindustry.com/pdf/marzocchi-pompe/gear-pumps-ghp/14767-576302.html) | GHP3-sarja; 63 cm³:n painearvoa ei saatu | vertailu |

## Hydrauliikka: kytkimet ja voimanulosotto

| Komponentti | Dokumentti | Tärkeimmät tiedot | Käytetään |
|---|---|---|---|
| **Borelli 30300 / 30500 mekaaniset kytkimet** | [Salhydro, luettelo HPFM.pdf](https://files.salhydro.fi/files/PDF/HPFM.pdf) (*kuvana*) | 30300: 185 Nm, Ø28; **30500: 580 Nm, 60 kW, Ø42 j6 kiila 12×8×60, toisio 48×44 DIN 5482**; kytkentä ≤ 1800 rpm (molempiin suuntiin ≤ 1000) | [p2-pump-options](../hydraulics/design/p2-pump-options.md#borellin-mekaaniset-kytkimet-salhydron-luettelo-hpfmpdf) |
| Flowfit ZZ009520 (kytkin 30300 + VNK3 43 cm³) | [Flowfit, tuotesivu](https://www.flowfitonline.com/products/group-3-mechanical-clutch-pump-assembly-43cc-77-4-l-min); [datalehti](https://www.flowfitonline.com/uploads/PDFproducts/Mech%20Clutch%20Assemblies%20Group%203%20PDF.pdf) (*kuvana*) | Kokoonpano 200 bar; kytkin 185 Nm | [p2-pump-options](../hydraulics/design/p2-pump-options.md#flowfit-zz009520-ryhmän-3-mekaaninen-kytkin--ja-pumppukokoonpano-43-cm³) |
| Flowfit sähkömagneettiset kytkimet | [ECPA1.pdf](https://www.flowfitonline.com/uploads/PDFproducts/ECPA1.pdf) (*kuvana*) | Suurin sarja 30990/30991: 160 Nm nimellinen, 210 Nm staattinen; hihnapyöräensiö | [p2-pump-options](../hydraulics/design/p2-pump-options.md#sähkömagneettiset-kytkimet-flowfitin-valikoima) |
| **Spidex-kynsikytkimet (R+L Hydraulics, Salhydro)** | [Spidex & Dentex -luettelo](https://files.salhydro.fi/files/products/Spidex_ja_Dentex_tekniset_tiedot.pdf); [uritetut navat](https://www.salhydro.fi/en/product/spidex-hubs-for-splined-shaft) | 48/60: TKN 310 / 525 / 655 Nm (92 Sh A / 98 Sh A / 64 Sh D), ≤ 5600 rpm, L 140 mm; navat SPI-48A-KL-A8X32X36 (ISO 14 B8×32×36) ja SPI-48A-ST-D48H7; käyttökertoimet s. 7, siirtymät s. 16 | [p2-pump-options](../hydraulics/design/p2-pump-options.md#veto-ptolta-suoraan-f1-61lle-bpv-vaihtoehto-ei-kytkintä) |
| Salhydro EPH-8-36 | [tuotesivu](https://www.salhydro.fi/en/product/hydraulic-components/pumps-and-power-units/mechanical-transmission/axles-and-joints/eph-ferrule-iso-14) | ISO 14 B8×32×36 -uritettu holkki, Ø60 × 50 mm | sama |
| Brevini IM1 | [hydrauliikkakauppa.fi](https://www.hydrauliikkakauppa.fi/wp-content/uploads/2020/09/Mekaaninen-Irrotuskytkin-40kW-IM1.pdf) (*kuvana*) | 190 Nm max; kytkentä ≤ 420 rpm | [p2-pump-options](../hydraulics/design/p2-pump-options.md#brevini-im1-hydrauliikkakauppafi) |

## Hydrauliikka: toimilaitteet, venttiilit ja muut

| Komponentti | Dokumentti | Tärkeimmät tiedot | Käytetään |
|---|---|---|---|
| Side-Power SH240/250TC-U11 -keulapotkuri | [Side-Power, tuotesivu](https://side-power.com/produkt/20443/sh240/); omistajien datalehti `sh-spec-sheet-v1-0-0-2017-lr-qvktgqi.pdf` | Ks. omistajien datalehdet. Asennusohje ks. omistajien datalehdet. **⚠ Moottorin U11 suurin sallittu paine ei ilmoitettu suoraan.** | [current-system](../hydraulics/current-system.md) |
| **Bowman EC100 -öljynjäähdytin** | [Bowman, EC Series Product Profile](https://ej-bowman.com/wp-content/uploads/2023/05/EC-Series-Product-Profile.pdf) (*kuvana*) | Öljy ≤ 92 l/min; 0,44 bar / 60 l/min; 4–10 kW esitteen ehdoilla; merivesi 3-vetoinen 25–50 l/min; 3/4" BSP | [oil-cooling](../hydraulics/design/oil-cooling.md#bowman-ec100--jäähdytin-omistajilla-varalla) |
| BAV-713 | ks. omistajien datalehdet (`Teollisuusventtiilit.pdf`) | 60 l/min, 350 bar; painehäviö puuttuu | [current-system §3.4](../hydraulics/current-system.md) |
| HRC 150 -joustokytkin | — | **⚠ Datalehti puuttuu** (nimellismomentti, suurin reikä napatyypeittäin) | [current-system](../hydraulics/current-system.md) |

## Omistajien datalehdet (`datasheets/local/`)

Omistajien omat PDF-kopiot nykyisen järjestelmän osista [omistaja 2026-10-22]. Tiedostot ovat vain
Larin koneella (eivät GitHubissa); arvot on poimittu tähän.

| Tiedosto | Komponentti | Tärkeimmät tiedot | Käytetään |
|---|---|---|---|
| `pumppu-2PE16D-P28P1.pdf` | **Salami 2PE16D-P28P1**, ohjauspumppu P1 (ryhmä 2, E-sarja; kartioakseli 1:8, laippa P1) | 16,6 cm³; 250 bar jatkuva / 280 ajoittainen / 300 huippu; **max 3000 rpm**, min 400 rpm. Käyttöehdot: imupaine 0,7–2,5 bar abs., viskositeetti ≥ 12 cSt (suositus 17–65, käynnistys ≤ 800), öljy −15…+85 °C (s. 2 ja 7, *kuvana*) | [current-system §3.2](../hydraulics/current-system.md) |
| `pumppu-3PB33D-P38P2.pdf` | Salami 3PB33D-P38P2, vanha apupiirin pumppu P2 (ryhmä 3) | 33,5 cm³; korvataan uudella (arvoja ei poimittu) | [current-system §3.2](../hydraulics/current-system.md) |
| `virtauksensaato-VPR3.pdf` | **Marchesini VPR3**, kolmitie-prioriteettiventtiili (apupiiri) | Ylimäärä B-portista; suurin tulovirtaus / säädetty virtaus: 3/8" 60/50, 1/2" 80/60, **3/4" 120/100**, 1" 200/170 l/min; 350 bar (*kuvana*) | [current-system §3.4](../hydraulics/current-system.md), [p2-pump-options](../hydraulics/design/p2-pump-options.md) |
| `virtauksensaato-RPF3.pdf` | **Marchesini RPF3**, kolmitie-virtauksensäätö, ylimäärä säiliöön (ohjauspiiri) | Suurin tulovirtaus / säädetty: 3/8" 50/30, 1/2" 85/50 l/min; 350 bar | [current-system §3.3](../hydraulics/current-system.md) |
| `4.2-VMP.pdf` | **Marchesini VMP 3/4"** (V0720), paineenrajoitusventtiili (apupiiri), linjaan asennettava | Suurin virtaus **90 l/min**, 350 bar; G3/4; jousivaihtoehdot 10–50, 20–100, 10–180 (vakio), 50–250, 80–300 bar; 50 bar/kierros 80–300-jousella; paino 1,47 kg (*kuvana*) | [current-system §3.4](../hydraulics/current-system.md), [p2-pump-options](../hydraulics/design/p2-pump-options.md#paineenrajoituksen-nostaminen-yli-250-barin) |
| `patruunaventtiili-2:2.pdf` | **Bosch Rexroth OD15-X-17-Y-S0**, 2/2-patruunaventtiili, jännitteettömänä auki, esiohjattu istukka: apupiirin vapaakiertoventtiili, joka **kytkee paineen CETOP-pohjalaatalle** keulapotkuria käytettäessä [omistaja 2026-10-22] | 350 bar (koepaine 420); 2–70 l/min; viskositeetti 20–380 cSt; öljy −20…+80 °C; suodatus ISO 4406 19/17/14; kela erikseen (20 W) | [current-system §3.4](../hydraulics/current-system.md) |
| `orbitroli-hkus_160-4.pdf` | **M+S Hydraulic HKUS 160/4** -ohjausyksikkö | 158,4 cm³/r; avoin keskiasento, ei kuormantakaisinkytkentää; sisäänrakennettu paineenrajoitus (asetus 80–170 bar) ja iskuventtiilit (140–220 bar); nimellisvirtaus 16 l/min (100 rpm); **T-linjan suurin jatkuva paine 25 bar**; liitännät G1/2 | [current-system §3.3](../hydraulics/current-system.md), [oil-cooling](../hydraulics/design/oil-cooling.md) |
| `cetop-3-manifolds-ng6-with-relief-valve.pdf` | **Flowfit CETOP 3 / NG6 -rinnakkaispohjalaatta**, 4-paikkainen (apupiiri) | Rinnankytketty, paineenrajoitusventtiilin kavitetti (P→T) ja mittariliitäntä; P ja T 1/2" BSP, A ja B 3/8" BSP, G 1/4" BSP; 4 paikkaa: pituus 247,7 mm, 8,21 kg; materiaali teräs [omistaja 2026-10-22]. **Painearvoa ei ilmoitettu.** (*kuvana*) | [current-system §3.4](../hydraulics/current-system.md) |
| `Teollisuusventtiilit.pdf` | Fluiconnecto (Manuli) -luettelo "Teollisuusventtiilit", s. 238–254 (Atos- ja fluiconnecto-venttiilit) | **BAV-IC3-713** (s. 239): suoraan ohjattu 4/3, NG6 / CETOP 03, keskiasento A-B-T yhdistetty / P suljettu; **60 l/min, 350 bar**; kelat BAV-SPC3 12/24 VDC; pituus 214 mm. Painehäviökäyrää ei ole. (*kuvana*) | [current-system §3.4](../hydraulics/current-system.md) |
| `sh-spec-sheet-v1-0-0-2017-lr-qvktgqi.pdf` | **Side-Power SH Series Product Specification v1.0.0 (2017)**, keulapotkuri SH240/250TC-U11 | Työntövoima 220 kg kevyt / 200 kg raskas käyttö; 14,9 kW; tunneli 250 mm; kaksi vastakkain pyörivää potkuria; vaihteisto pronssia, EP 90 -öljykylpy; joustokytkin. U11: 60 % 26,2 l/min × 158 bar, 80 % 30,2 × 211, 100 % 33,8 × 264. Ei käyttöjaksorajaa. Moottorin suurinta painetta ei ilmoitettu. | [current-system §3.4](../hydraulics/current-system.md), [loads.yaml](../hydraulics/loads.yaml) |
| `im-sh-100160240-2746-35-2025.pdf` | **Sleipner SH100/160/240 -asennusohje** 2746 35 2025 | SH240: työntövoima **240 kg kevyt / 220 kg raskas käyttö**, 14,9 kW, käyttöaika jatkuva. Vaatimukset: öljynsuodatin, öljynjäähdytin (öljy < 75 °C, suositus 40–60 °C), venttiilin virtaus- ja painerajat keulapotkurin rajoissa, **iskuventtiilit 10–15 % maksimipaineen yläpuolelle**, ohjaus S-Linkillä. U11: A/B 3/4" BSP, vuotolinja 1/4" BSP pakollinen. U8/U10 taulukossa 275 bariin. | [current-system §3.6](../hydraulics/current-system.md) |
| `um-sh-6572-6-2025.pdf` | **Sleipner SH -käyttöohje** 6572 6 2025 | Samat suorituskykyarvot kuin asennusohjeessa; käyttöaika jatkuva. SH320:n U11-moottori rajattu 274 bariin (tukee U11:n ~275 barin ylärajaa). Kausihuolto: vuodot, potkurit ja tunneli, antifouling, anodin vaihto joka kausi, vaihteiston EP 90 -öljysäiliön taso. | [current-system §3.6](../hydraulics/current-system.md) |
| `hyd_tank.pdf` | Flowfit Weldless Steel Tanks -luettelo (säiliö) | Saumattomat terässäiliöt 6–… l; 100 l tyypit A, B ja C (s. 14–16) | [current-system §3.5](../hydraulics/current-system.md) |
| `tukilaakeri_25604-4.pdf` | Tukilaakeri 25604-4 (hihnavedon tukilaakeri, luettelo "Supporti") | Pumppuun laipoitettava tukilaakeri hihna- tai ketjuvedon säteiskuormille, hammastettu puolikytkin; käyttöikä 3500 h 1500 rpm:llä; rasva DIN 51502 MPF 1K-20 | [current-system §3.1](../hydraulics/current-system.md) (P1:n hihnaveto) |

## Puuttuvat datalehdet

- [ ] Advance 300 -merivaihteen käyttöohje (PTO, jäähdytys)
- [x] Parker F1 -luettelo (MSG30-8200/UK)
- [x] Parker BPV-F1 -ohitusventtiili (HY30-8200/PL s. 47)
- [x] BPV-F1:n asennusohje MSG30-8227-INST
- [ ] BPV-F1:n ohitusasennon painehäviö (ei julkaistu; kysy Parkerilta)
- [ ] Teboil Hydraulic Oil 32S:n ja Neste Hydraulic 32 Superin tuotetiedotteet (VI, leikkauskestävyys)
- [ ] Sleipnerin hydraulijärjestelmän käyttöohje HS 6468 (öljysuositus; vanha linkki 404)
- [x] Side-Power SH -sarjan tuote-esite (suorituskyky)
- [x] Sleipner SH240 -asennusohje (2025)
- [x] Sleipner SH -käyttöohje (2025)
- [ ] U11-moottorin suurin sallittu paine (ohjeiden perusteella ~275 bar; vahvistus Sleipneriltä)
- [x] VPR3, RPF3, 2/2-vapaakiertoventtiili, orbitroli, ohjauspumppu (omistajien datalehdet)
- [x] Paineenrajoitusventtiili (Marchesini VMP 3/4")
- [x] CETOP 3 -pohjalaatta (Flowfit NG6, 4-paikkainen)
- [x] BAV-713 (fluiconnecto BAV-IC3-713)
- [ ] BAV-713:n painehäviökäyrä
- [ ] CETOP 3 -pohjalaatan painearvo (ei Flowfitin mittapiirustuksessa)
- [ ] HRC 150 -joustokytkin
- [ ] Caterpillar 3126B -merimoottorin tekniset tiedot (merivesipumppu, tyhjäkäynti)
