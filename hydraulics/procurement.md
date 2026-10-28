# Hydrauliikan hankintalista

> **Tila:** koottu 2026-10-28; imupuolen mittaus ja säiliön puhdistusohje hitsaukseen täydennetty samana päivänä suunnitelmadokumenteista (P2 = Vickers PVH57, venttiileinä Danfoss PVG 32,
> ykkösvaihtoehto 2026-10-27). Luvut ja koodit ovat lähdedokumenteista; tarkemmat perustelut
> linkeissä. Hinnat ovat jälleenmyyjien hintoja tai arvioita, ja ne on merkitty. Päivitä lista, kun
> osa ostetaan, löytyy veneeltä tai suunnitelma muuttuu.
> Varavaihtoehtojen (FXDC + LS-purku, LS + on/off) osia ei ole listalla. Ne tulevat ajankohtaisiksi
> vain, jos PVG 32:n kauppa kaatuu, ks. [p2-variable-pump](design/p2-variable-pump.md#tarvittavat-osat-pumpun-lisäksi-minimi).

**Tila-sarake:** ✅ olemassa tai sovittu · 🛒 hankitaan · 🔍 todennäköisesti olemassa, tarkista
veneellä · ❓ ehdollinen (tarve selviää tarkistuksesta tai päätöksestä) · ⏳ myöhemmin

## 1. P2-pumppu ja voimansiirto

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 1.1 | Vickers PVH57C-LAF-1S-10-C12V-31 | 1 | 57,4 cm³, LS-säädin, pyörimissuunta L | ✅ kaupat sovittu | 190 € | [päätös 2026-10-27](../decisions.md), [p2-variable-pump](design/p2-variable-pump.md) |
| 1.2 | HRC 150 -kytkimen napa (F tai H asennustilan mukaan) | 2 | Taper Lock -holkeille | 🛒 | noin 19 € + ALV / kpl | [p2-variable-pump](design/p2-variable-pump.md#tarvittavat-osat-pumpun-lisäksi-minimi) |
| 1.3 | HRC 150 -elastinen välikappale | 1 | | 🛒 | noin 10 £ + ALV | sama |
| 1.4 | Taper Lock 2012 -holkki 48 mm, kiilaura | 1 | PTO:n puoli; **⚠ tarkista** koodi ja kiilauran syvyys | 🛒 | arviolta 10–25 € | sama |
| 1.5 | Taper Lock 2012 -holkki 1 1/4", kiilaura | 1 | pumpun puoli; **⚠ tarkista** koodi | 🛒 | arviolta 10–25 € | sama |
| 1.6 | Pumppukannake SAE C -laipalle | 1 | 10 mm:n teräslevy, laserleikkaus ja hitsaus; laipan mitat Eatonin piirustuksesta **⚠** | 🛒 omistajat suunnittelevat | **⚠ ei tiedossa** | [päätös 2026-10-23](../decisions.md) |
| 1.7 | Kytkimen suojakotelo | 1 | pyörivän kytkimen suoja | 🛒 | **⚠ ei tiedossa** | [p2-variable-pump](design/p2-variable-pump.md#asennusjärjestys) |
| 1.8 | Pumpun ulkoiset O-renkaat (portit, laipat, säädin) | sarja | vaihdetaan liitäntöjä tehtäessä; mitat **⚠ ei tiedossa** | 🛒 | **⚠ ei tiedossa** | [p2-variable-pump](design/p2-variable-pump.md#tiivistesarja) |
| 1.9 | Akselitiiviste | 1 | vain, jos vuotaa koeajossa; koko tiivistesarjaa 02-102244 (noin 853 $) ei tarvita | ❓ | **⚠ ei tiedossa** | sama |
| 1.10 | Pumpun koeajo hydrauliikkakorjaamolla | – | suositus ennen asennusta | ❓ | **⚠ ei tiedossa** | sama |

## 2. P2:n imulinja (säiliö → pumppu, 50 mm)

Järjestys säiliöltä pumpulle: **muhvi → 90°:n kulma → palloventtiili → letkukara → letku → pumpun
imulaippa** [omistaja 2026-10-28]. Säiliö on tyhjä ja auki öljynvaihdon aikana, joten muhvi
hitsataan silloin. Muhvi tehdään **uuteen kohtaan**, jotta vanha 32 mm:n ulosotto jää P1:lle
([p1-steering-pump](design/p1-steering-pump.md)).

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 2.1 | Säiliöön hitsattava muhvi, 50 mm:n linjalle | 1 | kierre palloventtiilin mukaan (esim. 2" BSP **⚠ tarkista** venttiilistä); ulosotto vähintään 50 mm minimiöljypinnan alle eikä paluiden lähelle; säiliö puhdistetaan ennen hitsausta ja sen jälkeen, ks. [puhdistus](#säiliön-puhdistus-hitsauksen-yhteydessä) | 🛒 | **⚠ ei tiedossa** | [omistaja 2026-10-28] |
| 2.2 | 90°:n kulmaliitin muhvin ja palloventtiilin väliin | 1 | täysi sisähalkaisija; mieluiten pitkäsäteinen, koska imupuolen marginaali on pieni [arvio] | 🛒 | **⚠ ei tiedossa** | [omistaja 2026-10-28] |
| 2.3 | Täysiaukkoinen palloventtiili 50 mm (2V0) | 1 | auki ajossa | 🔍 | – | [omistaja 2026-10-28] |
| 2.4 | Letkukara 50 mm:n imuletkulle | 1 | palloventtiilin kierteeseen | 🛒 | **⚠ ei tiedossa** | [omistaja 2026-10-28] |
| 2.5 | Imuletku 50 mm | **⚠ pituus** (noin 3 m) | imuun soveltuva, ei painu kasaan alipaineessa | 🛒 **⚠ tarkista**, onko olemassa | **⚠ ei tiedossa** | [päätös 2026-10-23](../decisions.md) |
| 2.6 | Letkunkiristimet, ruostumattomat | 4 | kaksi kumpaankin päähän | 🛒 | pieni | [arvio] |
| 2.7 | Pumpun imuliitin: SAE-laippa, O-rengas, pultit ja letkukara tai supistus 50 mm:n letkuun | 1 | laipan koko pumpusta **⚠** | 🛒 | **⚠ ei tiedossa** | [p2-variable-pump](design/p2-variable-pump.md#tarvittavat-osat-pumpun-lisäksi-minimi) |
| 2.8 | Mittausvälikappale letkun ja pumpun imulaipan väliin: lyhyt Ø50-teräsputki (noin 100–150 mm), jossa hitsattu 1/4" BSP -muhvi kyljessä, tai valmis 2":n T-kappale 1/4":n sivuaukolla | 1 | mahdollisimman lähellä pumppua, jotta mittaus sisältää koko linjan häviöt; BSPP ja tiivistealuslevy, ei kartiokierrettä (imupuolen vuoto imee ilmaa) | 🛒 | **⚠ ei tiedossa** | [pressure-monitoring](design/pressure-monitoring.md#imupaineen-mittaus) |
| 2.9 | 1/4" BSP -T-kappale mittausaukkoon | 1 | anturi 2B1 ja mittarin letku samaan aukkoon | 🛒 | pieni | [arvio] |
| 2.10 | Imupaineanturi 2B1, −1…+1 bar, 4–20 mA | 1 | Signal K:hon; varoitus alle 0 bar | 🛒 päätetty | noin 40–150 € [arvio] | [päätös 2026-10-23](../decisions.md) |
| 2.11 | Kaksoispainemittari (vakuumi ja paine) −1…+1,5 bar, glyseriinitäytteinen, Ø63 mm, takaliitäntä | 1 | 2G2, P2:n imupaine ilman sähköä; mittaritauluun, ks. [kiinnitys](#imupuolen-kaksoispainemittarit) | 🛒 päätetty | noin 15–40 € [arvio] | [pressure-monitoring](design/pressure-monitoring.md#imupaineen-mittaus), [päätös 2026-10-28](../decisions.md) |

## 3. P2:n paine-, vuoto- ja LS-linjat

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 3.1 | Painelähdön SAE-laippa ja liitin 3/4":n letkuun | 1 | koko pumpusta **⚠** | 🛒 | **⚠ ei tiedossa** | [p2-variable-pump](design/p2-variable-pump.md#tarvittavat-osat-pumpun-lisäksi-minimi) |
| 3.2 | Painelinja 3/4", 3–4 m | 1 | nykyinen P2:n painelinja; päät sovitetaan PVG:n P-porttiin | 🔍 **⚠ tarkista** kunto ja painearvo | – | [current-system §5](current-system.md#5-avoimet-kysymykset) |
| 3.3 | Sovite PVG 32:n P-porttiin | 1 | portti pumppumoduulin mukaan G 1/2, G 3/4 tai G 1 | 🛒 | **⚠ ei tiedossa** | [aux-circuit-ls-clean-sheet](design/aux-circuit-ls-clean-sheet.md#mitä-keulapotkuri-tarvitsee-pvh57n-ja-tämän-venttiilin-lisäksi) |
| 3.4 | LS-letku 1/4" ja liittimet | 1 | PVG:n LS (G 1/4) → pumpun LS-portti (koko **⚠**) | 🛒 | **⚠ ei tiedossa** | sama |
| 3.5 | Kotelovuotoletku vähintään noin 1/2" | 1 | ylimmästä vuotoportista suoraan säiliöön öljypinnan alle, ei paluulinjaan | 🛒 | **⚠ ei tiedossa** | [p2-variable-pump](design/p2-variable-pump.md#asennusjärjestys) |
| 3.6 | Keulapotkurin (U11) vuotolinja 1/4" | 1 | tehdään uusiksi suoraan säiliöön öljypinnan alle | 🛒 | **⚠ ei tiedossa** | [omistaja 2026-10-27] |
| 3.7 | Säiliön läpiviennit tai muhvit vuotolinjoille (3.5 ja 3.6) | 1–2 | putki öljypinnan alle; tehdään samalla kertaa kuin muhvi 2.1 | 🛒 **⚠ tarkista**, voiko käyttää olemassa olevia aukkoja | **⚠ ei tiedossa** | [arvio] |

## Säiliön puhdistus hitsauksen yhteydessä

Muhvi 2.1 ja mahdolliset läpiviennit 3.7 hitsataan säiliöön, jossa on ollut öljyä. Ohje perustuu
yleiseen hitsaus- ja hydrauliikkakäytäntöön, ei säiliön valmistajan ohjeeseen [arvio]. Hitsaus
öljyä sisältäneeseen säiliöön on tulityötä: säiliö pidetään auki ja tuuletettuna, ja paikalla on
sammutin ja palovartija.

**Ennen hitsausta:**

1. Valuta öljy pois ja imeytä loput imeytysliinoilla.
2. Pese sisäpinnat **vesiohenteisella emäksisellä rasvanpoistoaineella** (esim. konepesuun
   tarkoitettu teollisuuspesuaine) lämpimällä vedellä ja harjalla, ja huuhtele puhtaalla vedellä.
   Isoille pinnoille tämä on halvin ja turvallisin keino.
3. Kuivaa heti paineilmalla tai lämpöpuhaltimella, myös saumat ja nurkat. Teräs ruostuu nopeasti.
4. Puhdista hitsauskohta paljaaksi metalliksi sisältä ja ulkoa noin 50–100 mm:n matkalta.
   Pistemäiseen rasvanpoistoon käy kloorittoman jarrunpuhdistimen (esim. CRC Brakleen) pieni määrä;
   anna sen haihtua kokonaan ja tuuleta muutama minuutti ennen hitsausta.

**Ei ennen hitsausta:**

- **Ei kloorattua jarrun- tai osienpuhdistinta.** Hitsauskaari hajottaa kloorihiilivetyjen höyryt
  myrkylliseksi fosgeeniksi. Tarkista ainesosat pullosta tai käyttöturvallisuustiedotteesta: jos
  niissä on *tetrachloroethylene*, *perchloroethylene* tai *dichloromethane*, ainetta ei käytetä.
  Brakleenista on sekä kloorillinen että klooriton versio; Euroopassa myytävä on käsittääkseni
  klooriton **⚠ tarkista** pullosta.
- **Ei koko säiliön pesua liuottimilla** (jarrunpuhdistin, bensiini, tinneri, asetoni). Höyryt
  ovat ilmaa raskaampia ja jäävät säiliön pohjalle, jossa kipinä voi sytyttää ne räjähdysmäisesti.
  Hydrauliöljyn leimahduspiste on korkea, joten öljyjäämät ovat pienempi riski kuin liuotinhöyryt.

**Hitsauksen jälkeen** (nyt vaarallisinta ovat metallihiukkaset, jotka kulkeutuisivat uudelle
PVH57:lle):

1. Poista hitsausroiskeet, kuona ja hiomapöly harjalla ja kaapimella, sitten imurilla. Magneetti
   muovipussin sisällä kerää teräspölyn.
2. Tarkista hitsin takapuoli. Jos säiliö on maalattu sisältä (**⚠ ei tiedossa**), hio palanut maali
   pois; maalaa uudelleen vain öljynkestävällä säiliömaalilla. Jarrunpuhdistin voi pehmentää maalia,
   joten kokeile sitä ensin pieneen kohtaan.
3. Pyyhi nukkaamattomalla liinalla, ei trasselilla eikä puuvillarätillä. Liuotinpyyhintään käy
   klooriton jarrunpuhdistin tai isopropanoli, kun säiliö on jäähtynyt; tuuleta ennen täyttöä.
4. Huuhtele seinät ja pohja muutamalla litralla öljyä (huuhteluöljy 8.1 tai HVLP 32) ja tyhjennä.
   Huuhteluun käytetty erä ei palaa järjestelmään. Öljy poistaa veden ja pesuainejäämät ja jättää
   suojaavan öljykalvon.
5. Tarkista taskulampulla: puhtaalla liinalla pyyhitty pinta ei saa enää värjätä liinaa.
6. Täytä suodattimen läpi. Käyttöönotto jatkuu huuhtelupäätöksen mukaan: koeajot huuhteluöljyllä
   uuden suodatinelementin läpi, sitten elementin ja öljyn vaihto
   ([päätös 2026-10-27](../decisions.md), [hydraulic-oil](design/hydraulic-oil.md)). Tavoite on
   puhtausluokka 16/14/12.

Tarvikkeet: imeytysliinat, vesiohenteinen rasvanpoistoaine, nukkaamattomat liinat, klooriton
jarrunpuhdistin, sammutin. Hinnat **⚠ ei tiedossa**, pieniä [arvio].

## 4. Venttiilipöytä Danfoss PVG 32 ja ohjaus

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 4.1 | Danfoss PVG 32, 5 lohkoa (käytetty) | 1 | 1 × PVEH 157B4024, 4 × PVEO 157B4224 | 🛒 tarjous 200 €, odottaa myyjää | 200 € (pyyntö 400 €) | [aux-circuit-ls-clean-sheet](design/aux-circuit-ls-clean-sheet.md#ehdokas-danfoss-pvg-32-5-lohkoa-torifi) |
| 4.2 | Porttitulpat (muovi tai teräs) | sarja | kuljetukseen ja puhdistukseen; osa porteista on nyt auki | 🛒 | pieni | sama, [Puhdistus ja koestus](design/aux-circuit-ls-clean-sheet.md#puhdistus-ja-koestus) |
| 4.3 | Sovitteet A/B-portit (G 1/2) → keulapotkurin 1/2":n letkut | 2 | letkut valmiina | 🛒 | **⚠ ei tiedossa** | sama |
| 4.4 | Sovite T-portti (G 3/4) → paluukeräin | 1 | | 🛒 | **⚠ ei tiedossa** | sama |
| 4.5 | Painemittari 2G1 M-porttiin (G 1/4) | 1 | analoginen | 🔍 nykyinen mittari, **⚠ tarkista** mittausalue ja kunto | – | [pressure-monitoring](design/pressure-monitoring.md) |
| 4.6 | Kiinnitysteline tai -levy konehuoneeseen | 1 | venttiili noin 22–23 kg [laskelma]; paikka **⚠** | 🛒 | **⚠ ei tiedossa** | [schematic](schematic.md#avoimia-kohtia-kaaviossa) |
| 4.7 | Potentiometrijoystick keulapotkurille | 1 | samasta 24 V:n syötöstä; signaali 0,25–0,75 × U | 🛒 | **⚠ ei tiedossa** | [aux-circuit-ls-clean-sheet](design/aux-circuit-ls-clean-sheet.md) |
| 4.8 | PVE-liittimet Hirschmann DIN 4-napainen ja johdotus | 2–5 | lohkot 1–3 ensin | 🛒 **⚠ tarkista**, tulivatko liittimet venttiilin mukana | **⚠ ei tiedossa** | sama |
| 4.9 | Hätäseisrele PVE:iden 24 V:n syöttöön | 1 | | 🛒 | **⚠ ei tiedossa** | sama |
| 4.10 | Koestus hydrauliikkakorjaamon koepenkissä | – | vaihtoehtona oma koestus | ❓ | **⚠ ei tiedossa** | [Puhdistus ja koestus](design/aux-circuit-ls-clean-sheet.md#puhdistus-ja-koestus) |

**Ehdolliset PVG 32:n osat.** Tarve selviää kokoonpanokoodista 157N553(8/B) ja kunnon tarkistuksesta:

| # | Osa | Milloin tarvitaan | Hinta | Lähde |
|---|---|---|---|---|
| 4.11 | Keulapotkurin lohkon kara 40 l/min, avoin keskiasento (esim. 157B7102) | jos nykyinen kara on vääränlainen | noin 116 SGD + verot | [aux-circuit-ls-clean-sheet](design/aux-circuit-ls-clean-sheet.md#mitä-keulapotkuri-tarvitsee-pvh57n-ja-tämän-venttiilin-lisäksi) |
| 4.12 | PVLP-isku- ja imuventtiilit lohkon 1 A/B-portteihin (esim. 157B2280, 280 bar), 2 kpl | suositus, jos lohkossa on paikat; pätevä henkilö arvioi | **⚠ ei tiedossa** | sama |
| 4.13 | Tiivistesarja PVAS 157B8005 | jos lohkopino avataan | **⚠ ei tiedossa** | sama |
| 4.14 | Pumppumoduuli, suljettu keskiasento (esim. 157B5111) | vain, jos nykyinen on avoimen keskiasennon malli (epätodennäköistä) | **⚠ ei tiedossa** | sama |
| 4.15 | PVPX 24 V, 157B4238 | valinnainen sähköinen LS-purku | **⚠ ei tiedossa** | sama |

## 5. Paluu, suodatus ja jäähdytys

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 5.1 | Paluukeräin: 1":n T-liittimet, supistusnipat ja tiivistealuslevyt (BSPP, esim. Dowty) | 2–3 T:tä | venttiilipöydän lähelle; ei vesijohto-osia | 🛒 | **⚠ ei tiedossa** | [oil-cooling](design/oil-cooling.md#paluiden-yhdistäminen) |
| 5.2 | Paluuletku 1" | noin 5 m | keräin → jäähdytin → suodatin | 🛒 | **⚠ ei tiedossa** | [omistaja 2026-10-26] |
| 5.3 | Supistukset 1" → 3/4" jäähdyttimen liitäntöihin | 2 | | ❓ jos jäähdytin asennetaan | **⚠ ei tiedossa** | [oil-cooling](design/oil-cooling.md#paluulinjan-letkukoko) |
| 5.4 | Bowman EC100 -öljynjäähdytin | 1 | | ✅ omistajilla varalla (asennus päättämättä) | – | [oil-cooling](design/oil-cooling.md) |
| 5.5 | Jäähdyttimen ohitusventtiili 3–4 bar (3V1) | 1 | rinnakkain jäähdyttimen kanssa | ❓ jos jäähdytin asennetaan | **⚠ ei tiedossa** | [oil-cooling](design/oil-cooling.md#paluulinja-asennus) |
| 5.6 | Sinkkianodi EC100:aan | 1 | tarkistetaan ennen käyttöönottoa | ❓ | **⚠ ei tiedossa** | sama |
| 5.7 | Merivesihaara: letkut, T-liittimet, virtauksenrajoitin 30–40 l/min (3V3) ja kuristus päälinjaan (3V4) | sarja | rajoittimen tyyppi päättämättä | ❓ jos jäähdytin asennetaan | **⚠ ei tiedossa** | [oil-cooling](design/oil-cooling.md#merivesi) |
| 5.8 | Paluusuodatin: OMTF171F10NA1 (lasikuitu, 157 l/min), linjasuodatin tai lasikuituelementti nykyiseen runkoon | 1 | nykyinen selluloosaelementti ei riitä puhtausluokkaan 16/14/12; ratkeaa säiliön kannen mittauksilla | 🛒 malli päättämättä | OMTF171F10NA1 84,70 £ sis. ALV | [p2-variable-pump](design/p2-variable-pump.md#paluusuodattimen-vaihto-omtf171f10na1) |
| 5.9 | Suodatinelementti | 2 | yksi käyttöönoton huuhteluun, toinen öljynvaihdon jälkeen | 🛒 | **⚠ ei tiedossa** | [päätös 2026-10-27](../decisions.md) |
| 5.10 | Paluupaineen mittari 3G1 ja mittausliitin keräimeen | 1 | ehdotus | ❓ | **⚠ ei tiedossa** | [oil-cooling](design/oil-cooling.md#paluiden-yhdistäminen) |

## 6. P1 (ohjauspiiri)

Ohjauspiirin venttiilit (RPF3, orbitroli, vastaventtiilit, hätäohitus) ovat olemassa. Imulinja
siirretään P2:n vanhaan 32 mm:n letkuun ja ulosottoon.

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 6.1 | 32 mm:n imuletku, säiliöulosotto ja täysiaukkoinen palloventtiili | – | P2:n nykyinen imulinja | ✅ | – | [omistaja 2026-10-28] |
| 6.2 | Letkukara 32 mm ja 3/4" BSP -liitin P1:n imuaukkoon | 1 | | 🛒 | pieni | [p1-steering-pump](design/p1-steering-pump.md#avoimet-kysymykset) |
| 6.3 | 3/4":n T-kappale, jossa 1/4":n sivuaukko | 1 | letkukaran ja P1:n imuaukon väliin; BSPP ja tiivistealuslevy | 🛒 | pieni | sama |
| 6.4 | Kaksoispainemittari (vakuumi ja paine) −1…+1,5 bar, glyseriinitäytteinen, Ø63 mm, takaliitäntä | 1 | 1G2, kiinteä, mittaritauluun; pelkkä −1…0 bar:n alipainemittari ei näyttäisi pysähdyksissä olevaa pientä ylipainetta (öljypinta vähintään 1 m pumpun yläpuolella) | 🛒 päätetty | noin 15–40 € [arvio] | sama, [pressure-monitoring](design/pressure-monitoring.md#imupaineen-mittaus), [päätös 2026-10-28](../decisions.md) |

## Imupuolen kaksoispainemittarit

**Päätetty 2026-10-28:** kiinteät kaksoispainemittarit 1G2 (P1) ja 2G2 (P2) mittaritauluun ([päätös 2026-10-28](../decisions.md)). Toteutus:

- **Mittauspiste pumpun imuliittimeen** (rivit 2.8 ja 6.3), ei säiliön päähän: vain siinä mittaus
  sisältää letkun, kulman ja palloventtiilin häviöt, eli juuri sen paineen, jonka pumppu näkee.
- **Mittaria ei kiinnitetä suoraan liittimeen**, vaan seinään tai pieneen mittaritauluun luettavaan
  paikkaan ja yhdistetään 1/4":n mittausletkulla (rivit 7.5 ja 7.6). Pumppu ja letku tärisevät,
  PTO:n kytkimen vieressä mittaria on vaikea ja vaarallista lukea käydessä, ja letku suojaa mittaria
  iskuilta. Molemmat imumittarit voivat olla samassa taulussa, myös 2G1:n ja 1G1:n vieressä.
- **Mittausletku täytetään öljyllä** (ilmataan mittarin päästä), ja kaikki liitokset tiivistetään
  huolella: imupuolen vuoto imee ilmaa pumppuun.
- Imupuolella ei tarvita paineiskun vaimenninta.

## 7. Anturit ja mittaus

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 7.1 | Öljyn lämpötila-anturi 3B1 | 1 | varoitus 65 °C, hälytys 70 °C → ESP32 / Signal K | 🛒 päätetty | **⚠ ei tiedossa** | [päätös 2026-10-23](../decisions.md) |
| 7.2 | P2:n lähtöpaineanturi 2B2, 0–400 bar | 1 | ehdotus, prioriteetti 1 | ❓ | **⚠ ei tiedossa** | [pressure-monitoring](design/pressure-monitoring.md#suositus) |
| 7.3 | Ohjauspaineen anturi 1B2, 0–250 bar | 1 | ehdotus | ❓ | **⚠ ei tiedossa** | sama |
| 7.4 | Mittausliittimet (1T1, 2T1, 2T2, 3G2) ja kannettava mittari | 4 + 1 | ehdotus; P1:n imupuolelle (1T2) kiinteä mittari pikaliittimen sijaan, koska pikaliittimen tiiviys alipaineessa on epävarma | ❓ | noin 5–15 € / kpl [arvio] | sama |
| 7.5 | Mittausletku 1/4" (esim. Minimess-mittausletku tai ohut hydrauliletku) ja liittimet | 2 | 1G2:lle ja 2G2:lle; pituus mittaritaulun paikan mukaan **⚠**, suositus enintään noin 3 m; taulu imuaukkojen korkeudelle, koska 1 m:n korkeusero muuttaa lukemaa noin 0,085 bar, ks. [pressure-monitoring](design/pressure-monitoring.md#imupaineen-mittaus) | 🛒 päätetty | **⚠ ei tiedossa** | [päätös 2026-10-28](../decisions.md) |
| 7.6 | Mittaritaulu tai kiinnityslevy (Ø63 mm:n mittareille) | 1 | 1G2 ja 2G2; luettavaan paikkaan konehuoneessa, paikka **⚠ ei päätetty**; 1G1 ja 2G1 voi siirtää samaan tauluun | 🛒 päätetty | **⚠ ei tiedossa** | [päätös 2026-10-28](../decisions.md) |

## 8. Öljy

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 8.1 | Huuhteluöljy | – | nykyinen Teboil Hydraulic Lift 32 | ✅ | – | [päätös 2026-10-27](../decisions.md) |
| 8.2 | HVLP 32 (esim. Teboil Hydraulic Oil 32S), 20 l | 4 | 80 l täyttö koeajojen jälkeen; tuote päättämättä | 🛒 | noin 420 € (104,90 € / 20 l) | [hydraulic-oil](design/hydraulic-oil.md) |

## 9. Myöhemmin: ankkurivinssi ja painepesuri

| # | Osa | Tiedot | Tila |
|---|---|---|---|
| 9.1 | Ankkurivinssin moottori Danfoss OMP 160 (151-0031) | olemassa [omistaja 2026-10-27] | ✅ |
| 9.2 | Vinssin jarruventtiili | kuorman pito | ⏳ |
| 9.3 | Vinssilohkon paineraja: LS A/B -rajoitin PVB-lohkossa (tai lohkon vaihto) ja PVLP:t, tai moottorin päälle kaksoisristivirtausventtiili | riippuu lohkon 2 koodista | ⏳ |
| 9.4 | Vinssin ja pesurin letkut ja liittimet | | ⏳ |
| 9.5 | Painepesuri | malli **⚠ ei tiedossa** | ⏳ |

## Pois jäävät osat (voi myydä)

PVG 32 -ratkaisussa nämä jäävät käyttämättä: CETOP-pohjalaatta (Flowfit NG6), BAV-713, VPR3,
Rexroth OD15 ja 2/2-patruunaventtiili, Marchesini VMP. Jos PVG 32:n kauppa tai kunto ei onnistu,
osa niistä tarvitaan varavaihtoehdoissa, joten **ne kannattaa myydä vasta, kun PVG 32 on koestettu**.

## Ennen tilaamista selvitettävät

- [ ] PVG 32:n kokoonpanokoodi 157N553(8/B): kara, pumppumoduuli, PVLP-paikat ja P-portin koko (rivit 3.3, 4.11–4.14)
- [ ] PVH57:n laippa- ja porttikoot (Eaton M-2206-S): imu-, paine-, vuoto- ja LS-portit (rivit 2.7, 3.1, 3.4, 3.5)
- [ ] Veneellä: 50 mm:n palloventtiili ja sen kierre (2.1–2.4), 50 mm:n imuletku ja sen pituus (2.5), nykyisen 3/4":n painelinjan kunto (3.2), 2G1:n mittausalue (4.5), säiliön vapaat aukot vuotolinjoille (3.7)
- [ ] Veneellä: onko säiliö maalattu sisältä, ja onko käytettävä jarrunpuhdistin klooriton ([puhdistus](#säiliön-puhdistus-hitsauksen-yhteydessä))
- [ ] Taper Lock -holkkien koodit ja HRC 150:n napatyyppi (1.2–1.5)
- [ ] Jäähdyttimen asennus ja paluusuodattimen malli (5.3–5.9)
- [x] Imupuolelle kiinteät kaksoispainemittarit molempiin pumppuihin, mittaritauluun (päätös 2026-10-28)
- [ ] Mittaritaulun paikka konehuoneessa ja mittausletkujen pituus (7.5–7.6); siirretäänkö 1G1 ja 2G1 samaan tauluun
