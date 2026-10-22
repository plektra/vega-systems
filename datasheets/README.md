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
| Parker F1-061 (3781060) | [Jälleenmyyjän tuotesivu (pzip.ru)](https://pzip.ru/catalog/parker/3781060) | 61 cm³; 350–400 bar; DIN 5462 B8×32×36 -akseli; ISO | sama |
| Parker F1 -sarja | [Parker, tuotesivu](https://ph.parker.com/us/en/axial-piston-fixed-pumps-series-f1) | 350 bar jatkuva / 400 bar (ISO); ≤ 2600 rpm 350 barissa. **⚠ F1-luettelo (koko datalehti) puuttuu**, mm. pienin imupaine. | sama |
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
| Brevini IM1 | [hydrauliikkakauppa.fi](https://www.hydrauliikkakauppa.fi/wp-content/uploads/2020/09/Mekaaninen-Irrotuskytkin-40kW-IM1.pdf) (*kuvana*) | 190 Nm max; kytkentä ≤ 420 rpm | [p2-pump-options](../hydraulics/design/p2-pump-options.md#brevini-im1-hydrauliikkakauppafi) |

## Hydrauliikka: toimilaitteet, venttiilit ja muut

| Komponentti | Dokumentti | Tärkeimmät tiedot | Käytetään |
|---|---|---|---|
| Side-Power SH240-U11 -keulapotkuri | [Side-Power, tuotesivu](https://side-power.com/produkt/20443/sh240/) | 100 %: 264 bar × 33,8 l/min; 60 %: 158 bar × 26,2 l/min (blogin mukaan). **⚠ Asennusohje puuttuu** (moottorin suurin paine, käyttöjakso, öljyvaatimukset). | [current-system](../hydraulics/current-system.md) |
| **Bowman EC100 -öljynjäähdytin** | [Bowman, EC Series Product Profile](https://ej-bowman.com/wp-content/uploads/2023/05/EC-Series-Product-Profile.pdf) (*kuvana*) | Öljy ≤ 92 l/min; 0,44 bar / 60 l/min; 4–10 kW esitteen ehdoilla; merivesi 3-vetoinen 25–50 l/min; 3/4" BSP | [oil-cooling](../hydraulics/design/oil-cooling.md#bowman-ec100--jäähdytin-omistajilla-varalla) |
| BAV-713, CETOP 3 -pohjalaatta | — | **⚠ Datalehdet puuttuvat** (BAV-713:n painehäviö, painearvot) | [current-system](../hydraulics/current-system.md) |
| HRC 150 -joustokytkin | — | **⚠ Datalehti puuttuu** (nimellismomentti, suurin reikä napatyypeittäin) | [current-system](../hydraulics/current-system.md) |

## Omistajien datalehdet (`datasheets/local/`)

Omistajien omat PDF-kopiot nykyisen järjestelmän osista [omistaja 2026-10-22]. Tiedostot ovat vain
Larin koneella (eivät GitHubissa); arvot on poimittu tähän.

| Tiedosto | Komponentti | Tärkeimmät tiedot | Käytetään |
|---|---|---|---|
| `pumppu-2PE16D-P28P1.pdf` | **Salami 2PE16D-P28P1**, ohjauspumppu P1 (ryhmä 2, E-sarja; kartioakseli 1:8, laippa P1) | 16,6 cm³; 250 bar jatkuva / 280 ajoittainen / 300 huippu; **max 3000 rpm**, min 400 rpm. Käyttöehdot: imupaine 0,7–2,5 bar abs., viskositeetti ≥ 12 cSt (suositus 17–65, käynnistys ≤ 800), öljy −15…+85 °C (s. 2 ja 7, *kuvana*) | [current-system §3.2](../hydraulics/current-system.md) |
| `pumppu-3PB33D-P38P2.pdf` | Salami 3PB33D-P38P2, vanha apupiirin pumppu P2 (ryhmä 3) | 33,5 cm³; korvataan uudella (arvoja ei poimittu) | [current-system §3.2](../hydraulics/current-system.md) |
| `virtauksensaato-VPR3.pdf` | **Marchesini VPR3**, kolmitie-etusijaventtiili (apupiiri) | Ylimäärä B-portista; suurin tulovirtaus / säädetty virtaus: 3/8" 60/50, 1/2" 80/60, **3/4" 120/100**, 1" 200/170 l/min; 350 bar (*kuvana*) | [current-system §3.4](../hydraulics/current-system.md), [p2-pump-options](../hydraulics/design/p2-pump-options.md) |
| `virtauksensaato-RPF3.pdf` | **Marchesini RPF3**, kolmitie-virtauksensäätö, ylimäärä säiliöön (ohjauspiiri) | Suurin tulovirtaus / säädetty: 3/8" 50/30, 1/2" 85/50 l/min; 350 bar | [current-system §3.3](../hydraulics/current-system.md) |
| `4.2-VMP.pdf` | **Marchesini VMP 3/4"** (V0720), paineenrajoitusventtiili (apupiiri), linjaan asennettava | Suurin virtaus **90 l/min**, 350 bar; G3/4; jousivaihtoehdot 10–50, 20–100, 10–180 (vakio), 50–250, 80–300 bar; 50 bar/kierros 80–300-jousella; paino 1,47 kg (*kuvana*) | [current-system §3.4](../hydraulics/current-system.md), [p2-pump-options](../hydraulics/design/p2-pump-options.md#paineenrajoituksen-nostaminen-yli-250-barin) |
| `patruunaventtiili-2:2.pdf` | **Bosch Rexroth OD15-X-17-Y-S0**, 2/2-patruunaventtiili, jännitteettömänä auki, esiohjattu istukka. Asennettu **CETOP 3 -pohjalaattaan** [omistaja 2026-10-22]; todennäköisesti vapaakiertoventtiili (paineenrajoitus on erillinen VMP) **⚠ tarkista** | 350 bar (koepaine 420); 2–70 l/min; viskositeetti 20–380 cSt; öljy −20…+80 °C; suodatus ISO 4406 19/17/14; kela erikseen (20 W) | [current-system §3.4](../hydraulics/current-system.md) |
| `orbitroli-hkus_160-4.pdf` | **M+S Hydraulic HKUS 160/4** -ohjausyksikkö | 158,4 cm³/r; avoin keskiasento, ei kuormantakaisinkytkentää; sisäänrakennettu paineenrajoitus (asetus 80–170 bar) ja iskuventtiilit (140–220 bar); nimellisvirtaus 16 l/min (100 rpm); **T-linjan suurin jatkuva paine 25 bar**; liitännät G1/2 | [current-system §3.3](../hydraulics/current-system.md), [oil-cooling](../hydraulics/design/oil-cooling.md) |
| `hyd_tank.pdf` | Flowfit Weldless Steel Tanks -luettelo (säiliö) | Saumattomat terässäiliöt 6–… l; 100 l tyypit A, B ja C (s. 14–16) | [current-system §3.5](../hydraulics/current-system.md) |
| `tukilaakeri_25604-4.pdf` | Tukilaakeri 25604-4 (hihnavedon tukilaakeri, luettelo "Supporti") | Pumppuun laipoitettava tukilaakeri hihna- tai ketjuvedon säteiskuormille, hammastettu puolikytkin; käyttöikä 3500 h 1500 rpm:llä; rasva DIN 51502 MPF 1K-20 | [current-system §3.1](../hydraulics/current-system.md) (P1:n hihnaveto) |

## Puuttuvat datalehdet

- [ ] Advance 300 -merivaihteen käyttöohje (PTO, jäähdytys)
- [ ] Parker F1 -luettelo (pienin sallittu imupaine, tarkka kierrostilavuus)
- [ ] Side-Power SH240-U11 -asennusohje
- [x] VPR3, RPF3, 2/2-vapaakiertoventtiili, orbitroli, ohjauspumppu (omistajien datalehdet)
- [x] Paineenrajoitusventtiili (Marchesini VMP 3/4")
- [ ] BAV-713 ja CETOP 3 -pohjalaatta
- [ ] HRC 150 -joustokytkin
- [ ] Caterpillar 3126B -merimoottorin tekniset tiedot (merivesipumppu, tyhjäkäynti)
