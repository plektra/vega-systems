# Painemittaus: analogiset mittarit, digitaaliset anturit ja mittausliittimet

> **Tila:** ehdotus 2026-10-23, päivitetty 2026-10-26 ja **2026-11-03 (mittauspisteet päivitetty PVH57:lle ja PVG 32:lle; BPV-perustelut poistettu)** sekä 2026-11-09 (anturien valinta ja asennus), ei päätetty; imupuolen mittarit 1G2 ja 2G2 päätetty 2026-10-28. Nykyiset mittarit [omistaja 2026-10-23]. Hinnat ovat
> arvioita.

Liittyy: [vaatimukset §10.1](../requirements.md#101-anturit), [kaaviot](../schematic.md),
[PVG 32](aux-circuit-ls-clean-sheet.md). Alkuperäinen 2B2:n perustelu koski F1-61:n BPV:tä
([arkisto](archive/p2-pump-options.md#lisävaruste-parker-bpv-f1--ohitusventtiili)).

## Nykytila

| Tunnus | Paikka | Tyyppi | Lähde |
|---|---|---|---|
| 1G1 | Piiri 1: P-linjan alussa heti kolmitievirtauksensäätöventtiilin (RPF3) CF-lähdön jälkeen, eli orbitrolin P-paine | analoginen | [omistaja 2026-10-23] |
| 2G1 | Piiri 2: CETOP-pohjalaatalle tuleva P-linja (vanha kokoonpano); **siirretään PVG 32:n pumppumoduulin M-porttiin (G 1/4)** | analoginen | [omistaja 2026-10-23] |
| 3Z2:n mittari | Paluusuodattimen painemittari, olemassa; nykyisessä paikassa huonosti luettavissa | analoginen | [blogi 2017-04-10], [omistaja 2026-10-23] |

## Kolme mittaustapaa

| Tapa | Mitä se on | Hinta (arvio) | Milloin |
|---|---|---|---|
| **Analoginen mittari** | Glyseriinitäytteinen Ø63 mm, kiinteästi linjassa. Näkyy ilman sähköä. | noin 15–40 € / kpl | Paikat, joita katsotaan käytön aikana |
| **Digitaalinen anturi** | Paineanturi 4–20 mA (tai 0,5–4,5 V) → ESP32 → Signal K → NMEA 2000 (PGN 130314 *Actual Pressure*). Hälytykset ja lokitus. | noin 40–150 € / kpl + johdotus | Paikat, joita ohjauslogiikka tarvitsee tai joita halutaan valvoa jatkuvasti |
| **Mittausliitin** (esim. Minimess M16×2) | Pikaliitin, johon kytketään kannettava mittari tarvittaessa | noin 5–15 € / kpl + yksi kannettava mittari | Vianhaku ja käyttöönotto: halpa tapa saada monta mittauspistettä |

4–20 mA kestää pitkät kaapelit ja häiriöt ja paljastaa katkenneen johdon (alle 4 mA). Anturin
ylipainekesto vähintään 2 × mittausalue; analogisiin mittareihin vaimennin (snubber) paineiskuja
vastaan.

## Ehdotetut mittauspisteet

| Tunnus | Paikka | Tyyppi | Alue | Miksi | Prioriteetti |
|---|---|---|---|---|---|
| **2B2** | **P2:n lähtö** (PVH57:n painelinja tai PVG 32:n P-linja) | **digitaalinen** | 0–400 bar | Valmiustilan (noin 20 bar) ja vedon valvonta: jos paine jää lohkoa ohjattaessa matalaksi, veto tai LS-linja on vialla, ja ESP32 antaa hälytyksen; pumpun kuorma ja lokitus | **1** |
| **1B2** | Piiri 1: sama kohta kuin 1G1 (T-liitin mittarin rinnalle) | **digitaalinen** | 0–250 bar | Ohjauspaineen seuranta ja lokitus, orbitrolin paineenrajoituksen säätö, ohjauksen vikojen havaitseminen; tarvitaan myös, jos autopilotti tulee | **2** |
| 2B1 | P2:n imuaukko | digitaalinen | −1…+1 bar | [päätetty 2026-10-23] | päätetty |
| 3B1 | Säiliö / paluu, lämpötila | digitaalinen | 0–100 °C | [päätetty 2026-10-23] | päätetty |
| 1G1 | RPF3:n CF-lähtö | analoginen | 0–160 tai 0–250 bar | olemassa | – |
| 2G1 | PVG 32:n M-portti (pumppumoduuli) | analoginen | 0–400 bar | olemassa, siirretään; käyttöönoton säädöt ([p2-variable-pump](p2-variable-pump.md#säätö-käyttöönotossa-ilman-virtausmittaria)) | – |
| 3G2 | Paluulinja ennen jäähdytintä | analoginen tai mittausliitin | 0–25 bar | Orbitrolin T-linjan raja 25 bar; näyttää jäähdyttimen ohitusventtiilin avautumisen kylmällä öljyllä | 3 |
| 3Z2 | Paluusuodattimen mittari | analoginen, **olemassa**; siirretään näkyvämmäksi vain tarvittaessa | – | Suodattimen tukkeutuminen | – |
| 1T1 | P1:n lähtö ennen vastaventtiiliä 1V7 | mittausliitin | 0–250 bar | Vianhaku: pumppu vai RPF3; P3:n testaus erikseen | 4 |
| 1G2 | P1:n imuaukko (3/4":n T-kappale) | analoginen kaksoispainemittari mittaritaulussa, 1/4":n mittausletku | −1…+1,5 bar | Kiinteä imupaineen seuranta; korvaa 1T2:n (pikaliitin käyttöönoton mittaukseen) [päätös 2026-10-28](../../decisions.md) | päätetty |
| 2G2 | P2:n imuaukko (mittausvälikappale, sama aukko kuin 2B1) | analoginen kaksoispainemittari mittaritaulussa, 1/4":n mittausletku | −1…+1,5 bar | Imupaine ilman sähköä 2B1:n rinnalla [päätös 2026-10-28](../../decisions.md) | päätetty |
| 2T1, 2T2 | Keulapotkurin A- ja B-linjat PVG 32:n lohkossa 1 | mittausliittimet | 0–400 bar | Vianhaku: potkurin paine kumpaankin suuntaan, moottorin ja venttiilin kunto | 4 |
| 1T3, 1T4 | Ohjaussylinterin A- ja B-linjat | mittausliittimet | 0–250 bar | Vianhaku: sylinterin ja orbitrolin iskuventtiilien vuodot | 5 (valinnainen) |

## Imupaineen mittaus

Imupuolella paine on noin −0,3…+0,1 bar, joten tavallinen painemittari ei kelpaa, eikä
imulinjassa ole valmiita mittausliitäntöjä: PVH57:n imulaipan mittausaukosta ei ole tietoa
(**⚠ tarkista pumpusta**), ja Salamin P1:ssä on pelkkä 3/4":n imuaukko.

**Liitäntä:** imuletkun ja pumpun väliin lyhyt **välikappale, jossa on 1/4" BSP -sivuaukko**:

- **P1 (32 mm):** uuden letkukaran ja 3/4" BSP -liittimen väliin 3/4" BSP -T-kappale, jonka
  sivuhaarassa 1/4" BSP -supistus. Kaikki vakio-osia.
- **P2 (50 mm):** lyhyt teräsputki (Ø50, noin 100–150 mm) letkukaroilla tai letkuliittimellä
  molemmissa päissä ja siihen hitsattu 1/4" BSP -hitsausmuhvi; tai valmis 2" T-kappale
  1/4"-sivuaukolla. Asennetaan Parkerin imuliittimen ja letkun väliin.

**Päätetty 2026-10-28:** kummallekin pumpulle kiinteä kaksoispainemittari (1G2, 2G2) mittaritauluun 1/4":n mittausletkulla; mittauspiste pumpun imuliittimessä. Osat: [hankintalista](../procurement.md#imupuolen-kaksoispainemittarit).

**Mittausletkun pituus ja korkeus** [laskelma, öljyn tiheys 870 kg/m³]:

- Letkussa ei virtaa öljyä, joten **pituus ei vaikuta lukemaan**, vain lukema asettuu hitaammin.
  Ehdoton pituusraja tulee lähinnä valmiiden mittausletkujen pituuksista ja siitä, että pitkä letku
  on vaikea ilmata ja siinä on enemmän liitoksia. Käytännön suositus [arvio]: **enintään noin 3 m**.
- **Korkeusero vaikuttaa:** öljypatsas on noin **0,085 bar metriä kohden**. Jos mittari on 1 m
  mittauspisteen yläpuolella, se näyttää noin 0,085 bar todellista pienempää (enemmän alipainetta),
  ja 1 m alapuolella saman verran suurempaa. Imupuolen mittausalueella (noin −0,3…0 bar) tämä on
  merkittävä, joten **mittaritaulu mahdollisimman lähelle pumppujen imuaukkojen korkeutta**, tai
  korkeusero kirjataan tauluun korjauksena.
- Jos mittari on mittauspisteen yläpuolella, letkuun jäänyt ilma nousee mittarille ja vaimentaa
  lukemaa; ilmaa mittarin päästä. Imupuolella vuotava mittariliitos imee ilmaa linjaan.

**Mittausletkujen ilmaus** (1G2, 2G2) [arvio, yleinen käytäntö]:

1. **Reititys:** letku nousee tasaisesti mittauspisteeltä mittarille, ilman välissä olevia
   kohoumia, joihin ilma jää loukkuun. Ilma kerääntyy silloin mittarin päähän, josta se poistetaan.
2. **Esitäyttö:** täytä letku HVLP 32:lla ennen kytkemistä (suppilo tai ruisku), ja kytke ensin
   mittauspisteen pää.
3. **Ilmaus säiliön paineella, kone sammutettuna:** öljypinta on vähintään 1 m pumppujen
   yläpuolella, joten imulinjassa on pysähdyksissä pieni ylipaine. Kun imulinjan palloventtiili on
   auki, avaa mittarin liitintä taulun päästä puoli kierrosta ja anna öljyn valua liinaan, kunnes
   kuplia ei tule; kiristä. **Ei koskaan pumpun käydessä:** silloin imupuolella on alipaine, ja
   avattu liitin imee ilmaa pumppuun.
4. **Tarkistus:** kone sammutettuna mittarin pitää näyttää öljypinnan korkeutta vastaavaa pientä
   ylipainetta, noin 0,085 bar metriä kohden (≥ 1 m → noin +0,09 bar tai enemmän, korjattuna
   mittarin ja mittauspisteen korkeuserolla). Käynnistyksen jälkeen neulan pitää liikkua heti ja
   tasaisesti; hidas tai vaimea lukema kertoo letkuun jääneestä ilmasta.
5. Ilmaus tehdään käyttöönotossa järjestelmän täytön jälkeen ja aina, kun mittausletku on ollut
   irti.

**Ohjeita:**

- **Mahdollisimman lähelle pumpun imuaukkoa**, palloventtiilin ja muiden liittimien jälkeen, koska
  mittauksen pitää sisältää koko linjan häviöt.
- **Sivuaukko putken kyljessä**, ei alapuolella (lika) eikä yläpuolella (ilmataskut). Suora
  putkiosuus ennen aukkoa antaa tasaisemman lukeman.
- **Tiiviys on tärkeämpää kuin painepuolella:** imupuolen vuoto ei tiputa öljyä vaan imee ilmaa,
  joka aiheuttaa kavitaatiota ja melua. Käytä suorakierteisiä (BSPP) liittimiä tiivistealuslevyllä
  tai O-renkaalla, ei kartiokierrettä tai kierreteippiä.
- **Mittari:** yhdistelmämittari (vakuumi ja paine) **−1…+1,5 bar**, glyseriinitäytteinen, Ø63 mm;
  tai digitaalinen anturi samalla alueella (−1…+1 bar, 4–20 mA), kuten päätetty 2B1. Paineenmittaus
  ilmoitetaan ylipaineena (0 bar = ilmanpaine): PVH57:n raja 2400 rpm:llä on 0 bar ja Salamin
  0,7 bar abs noin −0,3 baria.
- **Mittausliitin:** jos imupuolelle halutaan pikaliitin (1T2), tarkista, että liitin on tiivis myös
  alipaineessa (**⚠ tarkista valmistajalta**). Muuten kiinteä mittari tai anturi on varmempi.

## Anturien valinta ja asennus (lisätty 2026-11-09)

**Riittävätkö halvat (esim. Aliexpressin) 4–20 mA -anturit?** Kyllä valvontaan, kun asennus tehdään
alla kuvatulla tavalla. Anturit 2B2, 1B2 ja 2B1 ovat valvontaa, lokitusta ja hälytyksiä varten, ja
analogiset mittarit 1G1, 2G1, 1G2 ja 2G2 jäävät rinnalle. Anturin vika vie siis vain lukeman tai
antaa väärän hälytyksen. Ainoa ohjaava toiminto on 2B2:n vedon valvonta, joka voi katkaista PVE:iden
virran. Väärä lukema pysäyttää silloin keulapotkurin tai vinssin eikä käynnistä mitään, mikä on
turvallinen vikasuunta. [arvio]

**Halpojen anturien todelliset riskit** [arvio, yleinen kokemus; ei mitattu]:

| Riski | Mitä se tarkoittaa Vegalla |
|---|---|
| Rungon tai kalvon vuoto tai halkeama 250–280 barissa | **Merkittävin riski.** 1B2:n vuoto vie ohjauksen, ja kuumaan koneeseen suihkuava öljy on palovaara. Valmistuslaatua ei voi tietää etukäteen. |
| Paineiskut ja väsyminen | Venttiilin sulkeutuminen tai keulapotkurin pysähtyminen voi nostaa paineen hetkellisesti yli paineenrajoituksen asetuksen. Halvan anturin ylipainekesto on usein vain 1,5–2 × mittausalue, ja ohut kalvo väsyy painevaihtelusta. |
| Kierre ja tiivistys | "G1/4" voi olla NPT- tai kartiokierre ilman tiivistepintaa. Imupuolella (2B1) vuoto imee ilmaa. |
| Tarkkuus ja lämpöryömintä | Luvattu ±0,5 % on käytännössä usein ±1–2 % mittausalueesta. 2B2:lle ja 1B2:lle tämä riittää. 2B1:llä (−1…+1 bar, varoitus 0 bar) ero on noin ±0,02–0,05 bar, mikä on rajoilla mutta käyttökelpoinen, kun nollapiste tarkistetaan. |
| Kosteus ja korroosio | Liittimen ilmoitettu IP65 ei aina pidä paikkaansa veneen konehuoneessa. |

**Ostokriteerit:**

- Ruostumaton runko ja **hitsattu metallikalvo** (ei keraamista kalvoa), suora **BSPP-kierre**
  tiivistealuslevyllä tai O-renkaalla.
- **Ylipainekesto vähintään 2 × mittausalue ja murtopaine ilmoitettu.** 2B2: 0–400 bar, 1B2:
  0–250 bar (ylipainekesto ≥ 500 bar). Jos myyjä ei kerro murtopainetta, älä osta.
- 2-johtiminen 4–20 mA, syöttöjännitealue, joka kattaa noden S2 24 V:n silmukat.

**Asennus:**

- **Kuristin (snubber, noin 0,5–0,8 mm:n reikä) anturin eteen.** Se vaimentaa paineiskut ja rajoittaa
  vuotoa, jos anturi hajoaa. **1B2:ssa pakollinen.** [arvio]
- **Sulkuventtiili tai mittausliitin anturin haaraan**, jotta rikkinäisen anturin voi eristää ja
  vaihtaa ajon aikana. **Ohjauspiirin (1B2) haara on turvallisuuskriittinen: pätevän henkilön pitää
  tarkistaa se ennen rakentamista.**
- **Lukeminen nodessa S2:** mittavastus noin 150 Ω (4–20 mA → noin 0,6–3 V) ja erillinen AD-muunnin
  (esim. ADS1115), koska ESP32:n oma AD-muunnin on epälineaarinen. **Alle 3,8 mA tai yli 20,5 mA
  tulkitaan anturiviaksi eikä paineeksi.** [arvio] Ks. [nmea2000-network 3.11](../../electrics/design/nmea2000-network.md#311-nodejako-lisätty-2026-11-08).
- **Käyttöönotossa** lukemat verrataan analogisiin mittareihin. 2B1:n nollapiste tarkistetaan kone
  sammutettuna: säiliön öljypatsaan pitää näkyä pienenä ylipaineena (noin +0,09 bar, kun öljypinta on
  1 m pumpun yläpuolella), ks. kohta [Imupaineen mittaus](#imupaineen-mittaus).

**Hintaluokat** [arvio, hintoja ei tarkistettu]:

| Vaihtoehto | Hinta / kpl | Milloin |
|---|---|---|
| Nimetön anturi (Aliexpress) | noin 15–30 € | Valvontakohdat (2B2, 2B1), kun kuristin ja sulkuventtiili ovat paikallaan |
| Kiinalainen teollisuusmerkki, jolla on oikea datalehti (murtopaine, kalvon materiaali) | noin 30–60 € | Hyvä kompromissi |
| Merkkianturi (esim. Danfoss MBS 3000, WIKA A-10, Trafag), myös käytettynä tai ylijäämänä | noin 60–150 € | 1B2, jos ohjauspiiriin halutaan varma anturi |

**Suositus:** halpa tai datalehdellinen kiinalainen anturi kohtiin 2B2 ja 2B1. Kohtaan 1B2 kelpaa
sama anturi, jos haaraan asennetaan kuristin ja sulkuventtiili. Muuten kannattaa ottaa merkkianturi.
Kolmen anturin hintaero on noin 100–300 € [arvio]. **Ei päätetty.**

## Suositus

1. **Digitaalinen anturi 2B2 P2:n lähtöön.** Se valvoo keulapotkuria ja vinssiä: jos paine jää
   lohkon ollessa ohjattuna alle rajan, veto tai LS-linja on todennäköisesti vialla, ja ESP32
   antaa hälytyksen tai katkaisee PVE:iden virran (sama logiikka kuin arkistoidussa
   [on/off-vaihtoehdossa](archive/aux-circuit-ls-onoff.md#painevalvonta-arvio)).
2. **Digitaalinen anturi 1B2 ohjauspiiriin** nykyisen mittarin 1G1 rinnalle.
3. **Mittausliittimet** kohtiin 1T1, 2T1, 2T2 ja 3G2 (imupuolella kiinteät mittarit 1G2 ja 2G2, päätös 2026-10-28) sekä yksi kannettava mittari: halvin tapa
   saada vianhakuun kattava mittaus.
4. Paluusuodattimen nykyinen mittari riittää; siirto näkyvämmäksi tarvittaessa.

Analogiset 1G1 ja 2G1 jäävät, jotta paineen näkee myös ilman sähköä tai Signal K:ta.

## Avoimet kysymykset

- [ ] Hyväksytäänkö ehdotus (2B2, 1B2, mittausliittimet, 3G2)?
- [ ] Anturien malli ja liitäntä (4–20 mA vai 0,5–4,5 V). Valintaperusteet: [Anturien valinta ja asennus](#anturien-valinta-ja-asennus-lisätty-2026-11-09); mallia ei ole valittu. ESP32-PDM:ssä ei ole 4–20 mA -tuloja, joten anturit tulevat hydrauliikan omaan anturinodeen S2 (ehdotus 2026-11-08, [nmea2000-network 3.11](../../electrics/design/nmea2000-network.md#311-nodejako-lisätty-2026-11-08))
- [ ] Signal K -polut ja NMEA 2000 -lähetys (PGN 130314, paineen lähdeluokka ⚠ tarkista)
- [ ] 1G1:n ja 2G1:n mittausalueet ja kunto
