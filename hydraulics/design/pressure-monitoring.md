# Painemittaus: analogiset mittarit, digitaaliset anturit ja mittausliittimet

> **Tila:** ehdotus 2026-10-23, päivitetty 2026-10-26 (2B2:n käyttö vaihtoehdossa C), ei päätetty. Nykyiset mittarit [omistaja 2026-10-23]. Hinnat ovat
> arvioita.

Liittyy: [vaatimukset §10.1](../requirements.md#101-anturit), [kaaviot](../schematic.md),
[P2:n BPV](p2-pump-options.md#lisävaruste-parker-bpv-f1--ohitusventtiili).

## Nykytila

| Tunnus | Paikka | Tyyppi | Lähde |
|---|---|---|---|
| 1G1 | Piiri 1: P-linjan alussa heti kolmitievirtauksensäätöventtiilin (RPF3) CF-lähdön jälkeen, eli orbitrolin P-paine | analoginen | [omistaja 2026-10-23] |
| 2G1 | Piiri 2: CETOP-pohjalaatalle tuleva P-linja | analoginen | [omistaja 2026-10-23] |
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
| **2B2** | **P2:n lähtö BPV:n painelähdössä** (ennen VPR3:a) | **digitaalinen** | 0–400 bar | **BPV:n tilaa saa vaihtaa vain alle 20 barissa**: ohjauslogiikka (ESP32) tarvitsee tämän mittauksen. Lisäksi pumpun kuorma, VMP:n säätö ja vikojen havaitseminen. | **1** |
| **1B2** | Piiri 1: sama kohta kuin 1G1 (T-liitin mittarin rinnalle) | **digitaalinen** | 0–250 bar | Ohjauspaineen seuranta ja lokitus, orbitrolin paineenrajoituksen säätö, ohjauksen vikojen havaitseminen; tarvitaan myös, jos autopilotti tulee | **2** |
| 2B1 | P2:n imuaukko | digitaalinen | −1…+1 bar | [päätetty 2026-10-23] | päätetty |
| 3B1 | Säiliö / paluu, lämpötila | digitaalinen | 0–100 °C | [päätetty 2026-10-23] | päätetty |
| 1G1 | RPF3:n CF-lähtö | analoginen | 0–160 tai 0–250 bar | olemassa | – |
| 2G1 | CETOP-pohjalaatan P | analoginen | 0–400 bar | olemassa | – |
| 3G2 | Paluulinja ennen jäähdytintä | analoginen tai mittausliitin | 0–25 bar | Orbitrolin T-linjan raja 25 bar; näyttää jäähdyttimen ohitusventtiilin avautumisen kylmällä öljyllä | 3 |
| 3Z2 | Paluusuodattimen mittari | analoginen, **olemassa**; siirretään näkyvämmäksi vain tarvittaessa | – | Suodattimen tukkeutuminen | – |
| 1T1 | P1:n lähtö ennen vastaventtiiliä 1V7 | mittausliitin | 0–250 bar | Vianhaku: pumppu vai RPF3; P3:n testaus erikseen | 4 |
| 1T2 | P1:n imuaukko | mittausliitin (alipaine) | −1…0 bar | Päätetty mittaus käyttöönotossa | päätetty |
| 2T1, 2T2 | Keulapotkurin A- ja B-linjat pohjalaatalla | mittausliittimet | 0–400 bar | Vianhaku: potkurin paine kumpaankin suuntaan, moottorin ja venttiilin kunto | 4 |
| 1T3, 1T4 | Ohjaussylinterin A- ja B-linjat | mittausliittimet | 0–250 bar | Vianhaku: sylinterin ja orbitrolin iskuventtiilien vuodot | 5 (valinnainen) |

## Imupaineen mittaus

Imupuolella paine on noin −0,3…+0,1 bar, joten tavallinen painemittari ei kelpaa, eikä
imulinjassa ole valmiita mittausliitäntöjä: Parkerin imuliittimessä ja BPV-venttiilissä ei ole
mittausaukkoa (asennusohje MSG30-8227 mainitsee vain vuotoliitännän), ja Salamin P1:ssä on pelkkä
3/4":n imuaukko.

**Liitäntä:** imuletkun ja pumpun väliin lyhyt **välikappale, jossa on 1/4" BSP -sivuaukko**:

- **P1 (32 mm):** uuden letkukaran ja 3/4" BSP -liittimen väliin 3/4" BSP -T-kappale, jonka
  sivuhaarassa 1/4" BSP -supistus. Kaikki vakio-osia.
- **P2 (50 mm):** lyhyt teräsputki (Ø50, noin 100–150 mm) letkukaroilla tai letkuliittimellä
  molemmissa päissä ja siihen hitsattu 1/4" BSP -hitsausmuhvi; tai valmis 2" T-kappale
  1/4"-sivuaukolla. Asennetaan Parkerin imuliittimen ja letkun väliin.

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
  ilmoitetaan ylipaineena (0 bar = ilmanpaine): Parkerin raja 1,0 bar abs vastaa noin 0 baria ja
  Salamin 0,7 bar abs noin −0,3 baria.
- **Mittausliitin:** jos imupuolelle halutaan pikaliitin (1T2), tarkista, että liitin on tiivis myös
  alipaineessa (**⚠ tarkista valmistajalta**). Muuten kiinteä mittari tai anturi on varmempi.

## Suositus

1. **Digitaalinen anturi 2B2 P2:n lähtöön.** BPV:n vaihtoehto (alle 20 bar) kannattaa varmistaa
   ohjauslogiikassa mittauksella, ei pelkällä toimintajärjestyksellä. **Vaihtoehdossa C**
   (PVH57, LS ja on/off-venttiilit) BPV:tä ei ole, mutta sama anturi valvoo keulapotkuria: jos
   paine jää venttiilin ollessa päällä alle rajan, veto on todennäköisesti katkennut, ja ESP32
   katkaisee venttiilin virran ([aux-circuit-ls-onoff](aux-circuit-ls-onoff.md#painevalvonta-arvio)).
2. **Digitaalinen anturi 1B2 ohjauspiiriin** nykyisen mittarin 1G1 rinnalle.
3. **Mittausliittimet** kohtiin 1T1, 1T2, 2T1, 2T2 ja 3G2 sekä yksi kannettava mittari: halvin tapa
   saada vianhakuun kattava mittaus.
4. Paluusuodattimen nykyinen mittari riittää; siirto näkyvämmäksi tarvittaessa.

Analogiset 1G1 ja 2G1 jäävät, jotta paineen näkee myös ilman sähköä tai Signal K:ta.

## Avoimet kysymykset

- [ ] Hyväksytäänkö ehdotus (2B2, 1B2, mittausliittimet, 3G2)?
- [ ] Anturien malli ja liitäntä (4–20 mA vai 0,5–4,5 V; ESP32 PDM -kortin tulot)
- [ ] Signal K -polut ja NMEA 2000 -lähetys (PGN 130314, paineen lähdeluokka ⚠ tarkista)
- [ ] 1G1:n ja 2G1:n mittausalueet ja kunto
