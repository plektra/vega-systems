# Vegan kulutus- ja vaihto-osat

> **Tämä tiedosto on generoitu** tiedostosta [consumables.yaml](consumables.yaml) komennolla
> `python3 maintenance/render.py`. Älä muokkaa taulukoita käsin: muuta YAML-tiedostoa ja aja
> komento uudelleen. Päivitetty 2026-11-05.

Lista kaikista kuluvista ja määräajoin vaihdettavista osista ja nesteistä järjestelmittäin:
malli, mitat, määrä, vaihtoväli, edellinen vaihto ja seuraava ajankohta. Tuntemattomat tiedot
on merkitty **⚠ ei tiedossa**, ja ne täydennetään veneellä tai huolto-ohjeista.

## Näin päivität

Kerro Claudelle, mitä teit, esimerkiksi:

- *"Vaihdoin moottoriöljyn ja suodattimen tänään, tuntimittari 1234 h."*
- *"Tuntimittari näyttää nyt 1310 h."*
- *"P1:n hihnat ovat Optibelt SPA 1250."*

Claude kirjaa vaihdon historiaan, laskee seuraavan ajankohdan ja päivittää tämän taulukon.
Seuraava vaihto lasketaan edellisestä vaihdosta: tunnit tuntimittarin lukemasta ja päivä
kalenterivälistä, ja kumpi tahansa täyttyy ensin.

**Tuntimittari:** **⚠ ei tiedossa**. Kirjaa lukema, jotta tunteihin sidotut vaihdot voidaan laskea.

Merkit: 🔴 myöhässä · 🟡 erääntyy 30 vuorokauden tai 50 tunnin sisällä · ✅ ajallaan.

## Seuraavaksi erääntyvät

Ei myöhässä olevia eikä pian erääntyviä kohteita (kirjattujen vaihtojen perusteella).

## Pääkone CAT 3126B

| Kohde | Työ | Tuote / osanumero | Mitat | Määrä | Väli | Edellinen | Seuraava | Lähde |
|---|---|---|---|---|---|---|---|---|
| **Moottoriöljy** <br>`ENG-OIL` | vaihto | Cat DEO 15W-40 tai 10W-30 (datalehden mukaan) | – | 25 l | 500 h | – | ei kirjattua vaihtoa | [datalehti 3126B Marine Propulsion](https://www.dieselpartsdirect.com/caterpillar-3126b-marine-engine-propulsion) |
| **Moottorin öljynsuodatin** <br>`ENG-OIL-FILTER` | vaihto | Cat Advanced Efficiency -öljynsuodatin `1R-1807` | – | 1 kpl | 500 h | – | ei kirjattua vaihtoa | [datalehti Cat RV -suositus](https://manuals.plus/m/773fe17dac841d3dca87ad0e1415726efb6a59dcd371ccde6054a51755135a1c.pdf) |
| **Koneen polttoainesuodatin** <br>`ENG-FUEL-FILTER` | vaihto | **⚠ ei tiedossa** | – | – | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | – |
| **Polttoaineen esisuodatin / vedenerotin** <br>`ENG-FUEL-PREFILTER` | vaihto | **⚠ ei tiedossa** | – | – | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | – |
| **Koneen ilmansuodatin** <br>`ENG-AIR-FILTER` | vaihto | **⚠ ei tiedossa** | – | – | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | – |
| **Koneen jäähdytysneste** <br>`ENG-COOLANT` | vaihto | **⚠ ei tiedossa** | – | – | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | – |
| **Merivesipumpun impelleri** <br>`ENG-IMPELLER` | vaihto | **⚠ ei tiedossa** | – | 1 kpl | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | [vessel/README](../vessel/README.md#voimansiirto) |
| **Lämmönvaihtimen sinkkianodit** <br>`ENG-HX-ANODES` | tarkistus | **⚠ ei tiedossa** | – | – | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | – |
| **Laturin hihna** <br>`ENG-ALT-BELT` | vaihto | **⚠ ei tiedossa** | – | – | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | – |
| **Ohjauspumpun P1 kiilahihnat** <br>`ENG-P1-BELTS` | vaihto | Optibelt Super X-Power | Profiili ja pituus ⚠ ei tiedossa; hihnapyörä 180 mm, välitys 1:1,24 | 2 kpl, vaihdetaan parina | **⚠ ei tiedossa** | – | Kireys ja kunto tarkistetaan P1:n asennuksen yhteydessä | [blogi 2017-07-04], [hydraulics/current-system](../hydraulics/current-system.md) |

**Huomiot**

- `ENG-OIL`: 25 l ilman suodatinta, 500 h datalehden mukaan (⚠ tarkista koneen käyttö- ja huolto-ohjeesta). Vuosittainen väli ⚠ ei tiedossa; alle 1000 h vuodessa kalenteriväli voi tulla vastaan ensin. Vaihdetaan suodattimen kanssa.
- `ENG-OIL-FILTER`: Osanumero on Caterpillarin suositus 3126/3126B/C7-koneille matkailuautokäytössä, ei merimoottorin luettelosta: ⚠ tarkista koneen sarjanumerolla Cat-jälleenmyyjältä tai nykyisestä suodattimesta. Vaihdetaan öljyn kanssa.
- `ENG-FUEL-FILTER`: Malli ja väli ⚠ ei tiedossa; luetaan nykyisestä suodattimesta tai huolto-ohjeesta.
- `ENG-FUEL-PREFILTER`: Onko erillinen esisuodatin asennettu, ⚠ tarkista. Malli ja väli ⚠ ei tiedossa.
- `ENG-AIR-FILTER`: Malli ja väli ⚠ ei tiedossa.
- `ENG-COOLANT`: Tyyppi, määrä ja vaihtoväli ⚠ ei tiedossa. Pakkaskestävyys tarkistetaan ennen talvea.
- `ENG-IMPELLER`: Pumppu on koneen etupään omassa voimanulosotossa. Impellerin malli ja vaihtoväli ⚠ ei tiedossa. Varaimpelleri veneeseen kannattaa, koska jäähdytys pysähtyy ilman sitä.
- `ENG-HX-ANODES`: Onko koneen lämmönvaihtimessa anodeja ja montako, ⚠ tarkista.
- `ENG-ALT-BELT`: 65 A:n laturi. Hihnan tyyppi ja koko ⚠ ei tiedossa.
- `ENG-P1-BELTS`: Ohjauksen ainoa konevetoinen pumppu, joten varahihnasarja kannattaa pitää veneessä (P3 on varalla, jos hihna katkeaa). Hihnat luistivat aiemmin vain keulapotkurin kuormalla, joka siirtyy PTO:lle.

## Vaihteisto Advance 300

| Kohde | Työ | Tuote / osanumero | Mitat | Määrä | Väli | Edellinen | Seuraava | Lähde |
|---|---|---|---|---|---|---|---|---|
| **Vaihteistoöljy (Advance 300)** <br>`GBX-OIL` | vaihto | **⚠ ei tiedossa** | – | – | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | – |

**Huomiot**

- `GBX-OIL`: Öljytyyppi, määrä ja vaihtoväli ⚠ ei tiedossa: käyttöohje puuttuu (ks. datasheets/README.md). Tieto haetaan vaihteiston kilvestä tai jälleenmyyjältä.

## Hydrauliikka

| Kohde | Työ | Tuote / osanumero | Mitat | Määrä | Väli | Edellinen | Seuraava | Lähde |
|---|---|---|---|---|---|---|---|---|
| **Hydrauliöljy** <br>`HYD-OIL` | vaihto | HVLP 32 (DIN 51524-3, VI ≥ 150), esim. Teboil Hydraulic Oil 32S | – | 80 l; 4 × 20 l | **⚠ ei tiedossa** | – | Käyttöönotto: koeajot vanhalla öljyllä (Teboil Hydraulic Lift 32) uuden suodatinelementin läpi, sitten öljyn ja elementin vaihto (päätös 2026-10-27) | [blogi 2017-07-04], [päätös 2026-10-23](../decisions.md), [päätös 2026-10-27](../decisions.md) |
| **Paluusuodattimen elementti** <br>`HYD-RETURN-FILTER` | vaihto | Nykyinen runko OMT OMTF112C10NA2 (10 µm, selluloosa) `CR112C10R` | – | 2 kpl käyttöönottoon (huuhtelu + öljynvaihdon jälkeen) | **⚠ ei tiedossa** | – | Käyttöönotossa kahdesti, ks. HYD-OIL | [jälleenmyyjä Phoenix Hydraulics], [hydraulics/current-system](../hydraulics/current-system.md) |
| **Öljynjäähdyttimen sinkkianodi (Bowman EC100)** <br>`HYD-COOLER-ANODE` | tarkistus | **⚠ ei tiedossa** | – | 1 kpl | **⚠ ei tiedossa** | – | Tarkistetaan ennen käyttöönottoa, jos jäähdytin asennetaan | [hydraulics/procurement](../hydraulics/procurement.md) 5.6 |

**Huomiot**

- `HYD-OIL`: Säiliö Flowfit 100 l. Öljy tyhjennetään myös letkuista, sylinteristä ja orbitrolista. Vaihtoväli käyttöönoton jälkeen ⚠ ei tiedossa (ei päätetty).
- `HYD-RETURN-FILTER`: Suodatinmalli voi vaihtua (OMTF171F10NA1 tai lasikuituelementti, hydraulics/procurement.md 5.8), jolloin osanumero päivitetään. Ohitusventtiili 1,7 bar: vaihda, kun painemittari lähestyy ohitusrajaa lämpimällä öljyllä. Vaihtoväli muuten ⚠ ei tiedossa.
- `HYD-COOLER-ANODE`: Jäähdyttimen asennus on päättämättä.

## Keulapotkuri Side-Power SH240-U11

| Kohde | Työ | Tuote / osanumero | Mitat | Määrä | Väli | Edellinen | Seuraava | Lähde |
|---|---|---|---|---|---|---|---|---|
| **Keulapotkurin anodi** <br>`BT-ANODE` | vaihto | Side-Power SH240 | – | 1 kpl | 12 kk | – | Joka kausi tai kun puolet on kulunut | [ohje Sleipner 6572 6 2025] |
| **Keulapotkurin vaihteiston öljynpinta** <br>`BT-GEAR-OIL` | tarkistus | EP 90 | – | – | 12 kk | – | Ennen jokaista kautta | [ohje Sleipner 6572 6 2025] |
| **Potkurien ja vaihteiston antifouling** <br>`BT-ANTIFOULING` | vaihto | **⚠ ei tiedossa** | – | – | 12 kk | – | Ennen jokaista kautta | [ohje Sleipner 6572 6 2025] |

**Huomiot**

- `BT-ANODE`: Anodin osanumero ⚠ ei tiedossa.
- `BT-GEAR-OIL`: Öljysäiliön määrä ⚠ ei tiedossa.
- `BT-ANTIFOULING`: Ei anodiin, tiivisteisiin eikä akseliin. Samalla tarkistetaan vuodot, potkurit ja tunneli.

## Sähkö

| Kohde | Työ | Tuote / osanumero | Mitat | Määrä | Väli | Edellinen | Seuraava | Lähde |
|---|---|---|---|---|---|---|---|---|
| **Käynnistysakut** <br>`EL-START-BATT` | tarkistus | **⚠ ei tiedossa** | – | 2 kpl | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | [electrics/current-system](../electrics/current-system.md) |
| **Hakuvalon polttimo** <br>`EL-SEARCHLIGHT-BULB` | varaosa | Philips 24 V 250 W halogeeni (projektori- ja piirtoheitinpolttimo) | Pystypolttimo, kaksi ohutta nastaa; kannan tyyppi ⚠ ei tiedossa | 1 kpl | – | – | Rikkoutuessa | [omistaja 2026-10-31], [electrics/design/searchlight-deicing](../electrics/design/searchlight-deicing.md) |

**Huomiot**

- `EL-START-BATT`: Tyyppi, kapasiteetti ja ikä ⚠ ei tiedossa (luetaan tyyppikilvistä). Ylläpitolataus CTEK MULTI XT 14000.

## Runko ja potkuriakseli

| Kohde | Työ | Tuote / osanumero | Mitat | Määrä | Väli | Edellinen | Seuraava | Lähde |
|---|---|---|---|---|---|---|---|---|
| **Rungon ja potkuriakselin anodit** <br>`HULL-ANODES` | tarkistus | **⚠ ei tiedossa** | – | – | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | – |
| **Potkuriakselin tiiviste** <br>`SHAFT-SEAL` | tarkistus | **⚠ ei tiedossa** | – | – | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | – |

**Huomiot**

- `HULL-ANODES`: Anodien määrä, paikat ja mallit ⚠ ei tiedossa.
- `SHAFT-SEAL`: Tiivisteen tyyppi (esim. tiivistenaru tai mekaaninen tiiviste) ⚠ ei tiedossa.

## Ankkurivinssi

| Kohde | Työ | Tuote / osanumero | Mitat | Määrä | Väli | Edellinen | Seuraava | Lähde |
|---|---|---|---|---|---|---|---|---|
| **Ankkurivinssin nauhajarrun kitkapinta** <br>`WINCH-BRAKE` | tarkistus | **⚠ ei tiedossa** | – | – | **⚠ ei tiedossa** | – | ei kirjattua vaihtoa | [hydraulics/current-system](../hydraulics/current-system.md) |

**Huomiot**

- `WINCH-BRAKE`: Turvallisuuskriittinen: jarru pitää ankkurin, vaikka vetoketju katkeaa. Kitkapinnan materiaali ja kulumisraja ⚠ ei tiedossa.
