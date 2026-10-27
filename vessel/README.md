# Vega — alustiedot

Usean järjestelmän tarvitsemat yhteiset tiedot. Järjestelmäkohtaiset tiedot ovat kunkin
järjestelmän kansiossa ([hydraulics](../hydraulics/), [electrics](../electrics/)).

Lähteet: `[perustiedot]` ja `[blogi VVVV-KK-PP]` viittaavat Plektra-blogiin
(<https://plektra.github.io>, repo `plektra/plektra.github.io`); `[omistaja VVVV-KK-PP]` on
omistajien suoraan antama tieto.

## Alus

| Parametri | Arvo | Lähde |
|---|---|---|
| Nimi | Vega | |
| Tyyppi | Teräsrunkoinen hinaaja, muutettu vapaa-ajan käyttöön | [perustiedot] |
| Rakentaja / vuosi | Borgå Mekaniska Verkstad, 1912 | [perustiedot] |
| Pituus | 16,15 m | [perustiedot] |
| Leveys | 4,16 m | [perustiedot] |
| Syväys | 1,97 m | [perustiedot] |
| Uppouma | **⚠ ei tiedossa** | |
| Kotisatama | Laivalahti, Helsinki (ollut myös Saimaalla) | [perustiedot], [blogi 2017-07-04] |
| Ohjauspaikka | Yksi ruori, komentosillan keskellä | [blogi 2017-04-19] |
| Peräsin | Yksi peräsin; mitat **⚠ ei tiedossa** | |
| Keulapotkuri | Side-Power SH240-U11 (hydraulinen), 250 mm:n tunneli, asennettu 2017 | [blogi 2018-11-12] |
| Koneen käyttötunnit vuodessa | alle 1000 h | [omistaja 2026-10-23] |

## Voimansiirto

| Kohde | Arvo | Lähde |
|---|---|---|
| Pääkone | Caterpillar 3126B, asennettu 2012. Teho **säädetty 350 hv:hen** (vahvistettu; blogin 420 hv on mallin nimellisteho) | [perustiedot], [omistaja 2026-10-22], [omistaja 2026-10-27] |
| Kampiakselin pyörimissuunta | **Vastapäivään vauhtipyörän päästä katsottuna** (eli myötäpäivään koneen etupäästä katsottuna); Caterpillarin vakiosuunta | [datalehti 3126B Marine Propulsion](https://www.dieselpartsdirect.com/documents/caterpillar-specs/cat-3126b-propulsion.pdf) |
| Kierrosalue | Tyhjäkäynti (ks. alla) – **suurin noin 2400 rpm** (350 hv:n säädöllä), matka ~1800 rpm | [blogi 2018-11-12], [omistaja 2026-10-22] |
| Vauhtipyörä / kytkinkoppa | SAE 11-1/2 -vauhtipyörä, luultavasti SAE #3 -koppa, sovitelaippa SAE 14:ään | [blogi 2021-02-08] |
| Vaihteisto (alkuperäinen) | Masson RSD200 (1976), poistettu | [blogi 2019-01-24] |
| Vaihteisto | Advance 300, ~5,4:1, **asennettu ja linjattu** (2026) | [blogi 2021-02-08], [omistaja 2026-10-21] |
| Vaihteiston PTO | 1:1, ensiöakselilta (pyörii vapaalla), ei omaa kytkintä, 0,044 kW/rpm (≈ 420 Nm), Ø48 mm:n kiila-akseli. **Akseli osoittaa perään**, pyörii koneeseen nähden vastakkaiseen suuntaan → PTO-pumppu **L**, ks. [Pyörimissuunnat](#pyörimissuunnat) | [omistaja 2026-10-21], [omistaja 2026-10-23], [omistaja 2026-10-24] |
| Akselin laakeri | Uusi laakeripukki potkuriakselille | [omistaja 2026-10-21] |
| Koneen tilanne | Asennetaan takaisin ja linjataan vaihteistoon (lokakuu 2026) | [omistaja 2026-10-21] |
| Koneen kiinnitys | Sekä vaihteisto että kone jäykästi runkoon | [blogi 2021-02-08], [omistaja 2026-10-23] |
| Potkuri | Oikeakätinen | [blogi 2019-01-24] |
| Merivesipumppu (impelleri) | Koneen etupään omassa voimanulosotossa, kiinteä välitys (suhde **⚠ ei tiedossa**). Tuotto noin **70 l/min koneen 650 rpm:llä** verkkohaun mukaan, **⚠ vahvistamatta**. Kiinteällä välityksellä tuotto kasvaa suunnilleen koneen kierrosten suhteessa: arvio ~75 l/min 700 rpm, ~110 l/min 1000 rpm, ~190 l/min 1800 rpm. | [omistaja 2026-10-22, verkkohaun perusteella], [laskelma] |
| Merivesipiirin jäähdyttimet | Pääkoneen lämmönvaihdin ja merivaihteen (Advance 300) oma öljynjäähdytin samassa merivesipiirissä | [omistaja 2026-10-22] |

### Pyörimissuunnat

- **Kone:** CAT 3126B:n kampiakseli pyörii **vastapäivään vauhtipyörän päästä katsottuna**
  ("Rotation (from flywheel end): Counterclockwise"). Sama arvo on 3126B:n merimoottorin
  datalehdessä ja Caterpillarin huoltotiedoissa (haettu 2026-10-24). Kyse on tyyppitiedosta; Vegan
  koneen suuntaa ei ole erikseen katsottu, mutta vastakkaiseen suuntaan pyöriviä 3126B-koneita ei
  löytynyt.
- **PTO:** pyörii **koneeseen nähden vastakkaiseen suuntaan** [omistaja 2026-10-23], eli
  myötäpäivään, kun katsotaan samasta suunnasta kuin vauhtipyörää (perästä keulaan päin).
  Advance 300:n käyttöohjetta ei ole, joten tätä ei ole vahvistettu datalehdestä.
- **PTO-pumpun suunta** [laskelma]: pumppu ja PTO ovat vastakkain, joten pumpun suunta omasta
  akselinpäästään katsottuna on päinvastainen kuin PTO:n suunta PTO-akselin päästä katsottuna.
  Tulos riippuu siitä, mihin suuntaan PTO-akseli osoittaa. **PTO-akseli osoittaa perään**
  [omistaja 2026-10-24], joten **PTO-pumpun pitää olla L** (vastapäivään pumpun akselin päästä
  katsottuna):

  | PTO-akseli osoittaa | PTO akselin päästä katsottuna | Pumppu akselin päästä katsottuna |
  |---|---|---|
  | **perään** (pumppu PTO:n takana) ✅ Vega | myötäpäivään | **vastapäivään = L** |
  | **keulaan** (pumppu PTO:n edessä, koneen puolella) | vastapäivään | **myötäpäivään = R** |

  PTO:n pyörimissuunta koneeseen nähden on omistajan tieto eikä datalehdestä. **Ennen
  kiinteäsuuntaisen pumpun (Sunfab, OMFB) ostoa** se kannattaa varmistaa: merkitse PTO-akseliin
  teippiliuska ja katso perästä päin, pyöriikö akseli myötäpäivään, kun konetta pyöritetään käsin
  tai käynnistetään hetkeksi (vaihde vapaalla).
  Pumppujen R/L-merkintä tarkoittaa valmistajasta riippumatta suuntaa **pumpun akselin päästä
  katsottuna**; tarkista se silti kunkin pumpun datalehdestä.

### Tyhjäkäyntikierrokset

**Tyhjäkäynti on noin 700 rpm** [omistaja 2026-10-22]. **Laskelmissa oletetaan 700 rpm, eikä sitä mitata** (päätös 2026-10-23).
Vuoden 2018 blogissa mainittu noin 800 rpm oli siis yläkanttiin. 700 rpm sopii myös verkosta
löytyneisiin tietoihin (haettu 2026-10-22):

- Scribdissä olevassa 3126B:n esitteessä on **700 rpm**, mutta on epäselvää, mihin teholuokkaan se
  liittyy. ([lähde](https://www.scribd.com/document/832207648/3126B))
- Kahden 3126B:n omistaja kertoo tyhjäkäynnin olevan **noin 680 rpm**, ja "low-RPM"-kytkimellä noin
  540 rpm. ([lähde](https://forums.ybw.com/threads/low-rpm-toggle-switch.584153))
- Muissa Caterpillarin merimoottoreissa tyhjäkäynti on **ohjelmoitavissa 550–750 rpm:iin**
  moottorinohjaimesta Cat ET -huoltotyökalulla.
  ([lähde](https://www.cat.com/en_US/products/new/power-systems/marine-power-systems/commercial-propulsion-engines/18408926.html))

PTO-pumpun mitoitus riippuu tyhjäkäynnistä suoraan: 700 rpm:llä tarvitaan noin 51 cm³:n pumppu, ks.
[hydraulics/design/archive/p2-pump-options.md](../hydraulics/design/archive/p2-pump-options.md#herkkyys-tyhjäkäyntikierroksille).
Vahvista lukema mittaamalla, kun kone käy, esim. Signal K:n moottoritiedoista. Caterpillar-huolto
voi todennäköisesti nostaa ohjelmoitua tyhjäkäyntiä tarvittaessa.

## Sähköjärjestelmän perustiedot

Tarkemmin: [electrics/current-system.md](../electrics/current-system.md).

| Kohde | Arvo | Lähde |
|---|---|---|
| DC-jännite | 24 V (vahvistettu) | [blogi 2018-11-12], [omistaja 2026-10-27] |
| Koneen laturi | 65 A | [blogi 2017-07-04] |
