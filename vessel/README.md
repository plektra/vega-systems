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
| Koneen tiedonsiirto | Koneessa ei todennäköisesti ole tiedonsiirtoväylää (J1939) eikä ohjainyksikköä (ECU) [omistaja 2026-11-08]. Kone on omistajan käsityksen mukaan **MUI** eli mekaanisilla yksikköinjektoreilla ja mekaanisella säätimellä [omistaja 2026-11-08]. **⚠ tarkista** koneen tyyppikilvestä (sarjanumeron etuliite / arrangement-numero), koska 3126- ja 3126B-koneissa on yleensä elektronisesti ohjattu HEUI-ruiskutus, ja MUI on tyypillisempi edeltäjälle 3116:lle [arvio, yleistieto]. Vauhtipyörän kotelossa on valmis paikka kierrosanturille (magneettianturi), mutta anturia ei ole asennettu [omistaja 2026-11-08]. Koneen tiedot NMEA 2000:aan omilla antureilla, ks. [nmea2000-network](../electrics/design/nmea2000-network.md#33-kone-ja-vaihteisto) | [omistaja 2026-11-08] |
| Kampiakselin pyörimissuunta | **Vastapäivään vauhtipyörän päästä katsottuna** (eli myötäpäivään koneen etupäästä katsottuna); Caterpillarin vakiosuunta | [datalehti 3126B Marine Propulsion](https://www.dieselpartsdirect.com/documents/caterpillar-specs/cat-3126b-propulsion.pdf) |
| Kierrosalue | Tyhjäkäynti (ks. alla) – **suurin noin 2400 rpm** (350 hv:n säädöllä), matka ~1800 rpm | [blogi 2018-11-12], [omistaja 2026-10-22] |
| Vauhtipyörä / kytkinkoppa | SAE 11-1/2 -vauhtipyörä, **SAE No. 3 -vauhtipyörän kotelo** (vahvistettu manuaalista), sovitelaippa SAE 14:ään. **Käynnistyshammaskehässä 126 hammasta** (kierrosanturin laskukerroin) | [blogi 2021-02-08], [omistaja 2026-11-08, koneen manuaali] |
| Vaihteisto (alkuperäinen) | Masson RSD200 (1976), poistettu | [blogi 2019-01-24] |
| Vaihteisto | Advance 300, ~5,4:1, **asennettu ja linjattu** (2026). Huolto-ohjeen perusteella **malli 300 välityksellä 5,5:1** (todellinen 5,44:1, siirtokyky **0,125 kW/rpm**), koska akseliväli 264 mm on mallin 300 (D300A:n 355 mm) **⚠ tarkista** tyyppikilvestä. Tulokierrokset 750–2500 rpm. Siirtokyky riittää: 350 hv = 261 kW, ja vaihteisto kestää 0,125 × 2400 = 300 kW [laskelma]. Vakiomomenttina raja on noin 1190 Nm, joten **⚠ tarkista** koneen huippumomentti 350 hv:n säädöllä. Rakenne: 3 akselia, märät hydrauliset monilevykytkimet, hammas-kumipalakytkin koneeseen. Paino 700 kg. Tuloakselin suunta: Z300 vastapäivään / Y300 myötäpäivään lähtöpäästä katsottuna; kone pyörii vastapäivään vauhtipyörän päästä, joten Vegan vaihteen pitäisi olla **Z300** [laskelma] **⚠ tarkista** vaihteiston kilvestä (nuoli tulopäässä) | [blogi 2021-02-08], [omistaja 2026-10-21], [manuaali Advance 300, s. 32, 36–37, 42, 58] |
| Vaihteiston PTO | 1:1, ensiöakselilta (pyörii vapaalla), ei omaa kytkintä, 0,044 kW/rpm (≈ 420 Nm; vahvistettu huolto-ohjeesta, s. 65, jossa myös hihnavedon säteisvoima enintään 70 kgf ilman tukilaakeria), **Ø48h7-akseli, kiilaura 14 N9, uran syvyys 5,5 mm** (kiila 14 × 9, DIN 6885), vapaa pituus noin 60 mm ja kiilaura noin 44 mm (mitattu piirustuksesta); akselin keskiö noin 105 mm tuloakselin alapuolella ja noin 160 mm lähtöakselin yläpuolella (mitattu piirustuksesta **⚠ tarkista veneellä**). **Akseli osoittaa perään**, pyörii koneeseen nähden vastakkaiseen suuntaan → PTO-pumppu **L**, ks. [Pyörimissuunnat](#pyörimissuunnat) | [omistaja 2026-10-21], [omistaja 2026-10-23], [omistaja 2026-10-24], [datalehti Advance 300-WXT03], [manuaali Advance 300, s. 65] |
| Vaihteiston suuntaventtiili | **Advance Q06** -hydrauliohjausyksikkö (Q06-01B-00): vivulla AHEAD/STOP/ASTERN, venttiili kääntyy 45°. Viivemäntä nostaa kytkinpaineen nimellisarvoon vähitellen, ja **kytkeytymisaika on noin 3–6 s** normaalissa öljyn lämmössä. Aikaa säädetään kuristusruuvilla: sisään kiertämällä kytkeytyminen nopeutuu ja ulos kiertämällä hidastuu. **Suunnanvaihto tehdään 500–800 rpm:n tulokierroksilla**, joten tyhjäkäynti 700 rpm on alueella. **Kierroksia nostetaan vasta, kun painemittari on noussut nimellisarvoon.** Lisäulosotot paineantureille ja ulkoiselle ohjaukselle ovat M14×1,5 (tulpattu), painemittari 0–2,5 MPa. Venttiilistä on saatavana myös samanmittainen solenoidiversio. Kytkinpaine 1,2–1,4 MPa (ks. seuraava rivi); vaihteiston ohjeen mukaan nousuaika on 2–5 s ja vaihto kestää enintään 10 s | [omistaja 2026-11-13], [manuaali Advance Q06, s. 5–7] |
| Vaihteiston hydrauliikka ja öljy | Oma sykloidipumppu BB-B32A tuloakselin päässä, esisuodatin ja rakosuodatin, jäähdytin, ohitusventtiili. **Kytkinpaine 1,2–1,4 MPa** (12–14 bar), STOP-asennossa **0,3–0,6 MPa**, voitelupaine 0,05–0,3 MPa. Paine nousee kytkinpaineeseen 2–5 s:ssa. Tehtaalla koestettu 1500 rpm:llä; jos paine ei ole 1,2–1,4 MPa, sitä säädetään Q06:n säätöaluslaatoilla. **Öljy SAE 30** (API CC/SD; tropiikissa SAE 40), **20 kg** (noin 23 l [laskelma, tiheys 0,88]), öljyn lämpötila enintään 80 °C. **Jäähdytysvesi vähintään 3 t/h (50 l/min).** Pakkasella seisovan vaihteiston jäähdytin tyhjennetään. Sallittu kallistus 10° pituus- ja 15° sivusuunnassa. Huolto: ks. [maintenance](../maintenance/consumables.yaml) | [manuaali Advance 300, s. 36, 38–39, 41–42, 54–55] |
| Vaihteen ja kierrosten ohjaus | Ohjaamosta **yhdellä vivulla vaijereilla**: sama vipu ohjaa vaihteen asentoa (Q06:n ohjausvipu) ja koneen kierroksia. Valmistaja hyväksyy vaijeriohjauksen ohjaamosta, kunhan ohjauspöydän AHEAD/STOP/ASTERN vastaavat venttiilin asentoja. **Vaihto valmistajan ohjeen mukaan:** kierrokset alas, 2–3 s STOP-asennossa, sitten vaihto; kierroksia nostetaan vasta, kun kytkinpaine on noussut. Hätäajo hydrauliikan vikaantuessa: eteenpäinkytkin lukitaan mekaanisesti kolmella tapilla φ8 × 75 mm ja M10-ruuveilla takakannen alta, vipu STOP-asentoon ja enintään 80 % kierroksilla. Ohjaamossa ei ole vaihteen asennon eikä kytkinpaineen näyttöä. Anturi-idea: [nmea2000-network](../electrics/design/nmea2000-network.md#vaihteen-paineanturit-lisätty-2026-11-13) | [omistaja 2026-11-13], [manuaali Advance 300, s. 53] |
| Akselin laakeri | Uusi laakeripukki potkuriakselille | [omistaja 2026-10-21] |
| Koneen tilanne | Asennetaan takaisin ja linjataan vaihteistoon (lokakuu 2026) | [omistaja 2026-10-21] |
| Koneen kiinnitys | Sekä vaihteisto että kone jäykästi runkoon. Koneen **elastiset kannakkeet vaihdettiin kiinteisiin merivaihteen vaihdon yhteydessä**. Linjaus kannattaa tarkistaa uudelleen vesillelaskun jälkeen (runko muuttaa muotoaan nostettuna) ja ensimmäisten käyttötuntien jälkeen, ja kannakepultit kiristää uudelleen. Caterpillarin asennusohjeen kanta 3126B:n kiinteään asennukseen **⚠ tarkista** | [blogi 2021-02-08], [omistaja 2026-10-23], [omistaja 2026-11-09] |
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
  Huolto-ohje vahvistaa tämän: PTO on vastaakselin (transmission shaft) jatke, ja vastaakseli pyörii
  tuloakseliin nähden vastakkaiseen suuntaan [manuaali Advance 300, s. 37, 65].
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
