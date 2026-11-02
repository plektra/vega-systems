# PVG 32:n käsivipu (PVM): valmisosat ja oman vivun suunnittelu

> **Tila:** selvitys 2026-11-02. Ostetusta PVG 32:sta puuttuvat käsivivut, mutta vipujen kannat
> ovat paikallaan (ilmoituksen kuvista, **⚠ tarkista** vastaanotossa). Tavoite on suunnitella oma
> vipu, ensin karojen kokeiluun ilman painetta ja tarvittaessa myöhemmin käsiohjaukseksi
> [omistaja 2026-11-02]. Danfossin PDF:iä ei päästy lukemaan suoraan (verkkorajoitus), joten arvot
> ovat hakutulosten otteista; tarkista ne alkuperäisestä ohjeesta tai mittaamalla.

## Selkokielinen yhteenveto

- Danfossin käsivipu on kaksiosainen: **vivun kanta** (alumiini- tai valurautavalu, kiinni karan
  päässä olevassa PVM-moduulissa) ja **vipu** (tanko ja musta nuppi), joka **kierretään kantaan
  pohjaan asti**.
- Kannan kierre on hakutulosten mukaan todennäköisesti **M8, vähintään 10 mm syvä** (tuuma-mallissa
  5/16-18) **⚠ mittaa**. Siihen käy M8-kierretanko tai oma vipu, jossa on M8-pultti tai -kierretanko.
- Karan liike on ±7 mm ja vivun säätöalue noin ±19,5°. Voima on pieni (todennäköisesti noin 2 Nm
  momentti, eli 200 mm:n vivulla noin 11 N), joten **3D-tulostettu vipu riittää kokeiluun**.
- Valmis vipu kannattaa ostaa, jos käsiohjausta käytetään paineen alla tai turvallisuuskriittisesti.

## Valmisosat

| Koodi | Mikä | Lähde |
|---|---|---|
| 157B3171 | PVM, alumiininen vivun kanta ja vipu 22,5°, rajoitusruuvein (ruuveilla rajoitetaan karan liikettä ja siten suurinta virtausta); toimitetaan pultteineen | [Hydrastore 157B3171](https://www.hydrastore.co.uk/product/157b3171), [Hydrokit](https://www.hydrokit.com/en/produit/spool-valves/distribution-pvg-danfoss/pvg-32/manual-control-hydraulic-index-cover-pvm/pvm-manual-control-lever-xrp16779-xpr998.html) |
| 157B3191 | kanta ja vipu 22,5°, listauksessa ilman rajoitusruuveja | [paro.nl, PVG-ohjausmoduulit](https://paro.nl/library/search/hydraulic-integrated-circuits/modular-valve-systems/sectional/series-pvg/actuation-modules?page=7) |
| 157B3174 / 157B3194 | 37,5°:n kanta (lähteet ristiriidassa siitä, kumpi koodi sisältää kannan) **⚠ tarkista** | [paro.nl 157B3194](https://paro.nl/library/components/danfoss/157b3194-pvm-aluminium-lever-base-37-50) |
| 157B3161, 157B3184 | valurautainen kanta; anodisoitu alumiinikanta (molemmat rajoitusruuvein) | [paro.nl 157B3161](https://paro.nl/library/components/danfoss/157b3161-pvm-cast-iron-lever-base-and-lever-adj-screws), [paro.nl 157B3184](https://paro.nl/library/components/danfoss/157b3184-pvm-anodized-aluminium-lever-base-and-lever-adj-screws) |
| 11107587 | uudempi vipu ja yhdystanko kiristimellä (PVG 32 ja PVG 100) | [Holstein Hydraulik](https://www.holsteinhydraulik.com/en/Danfoss-11107587-Danfoss-Lever-with-clamp-for-PVG-32) |

Hinnat **⚠ ei tiedossa**. Varaosaluettelossa nuppi (mukana mutteri) ja kanta (mukana
lukitusruuvi) ovat erillisiä osia [PVG 32 Service Parts Manual](http://www.grouphes.com/wc/hes/Danfoss/PVG/DanfossPVG32ServicePartsManual.pdf).

## Mitat ja arvot oman vivun suunnitteluun

| Kohde | Arvo | Lähde |
|---|---|---|
| Vivun kiinnitys kantaan | kierre, vipu kierretään **pohjaan asti** ("Håndtaget skal skrues helt i bund") | [Asennusohje PVG 32](https://documents.kramp.com/PVG32_Instal_Guide_EN.pdf) (hakutuloksen ote) |
| Kierre | **M8, vähintään 10 mm** (tai 5/16-18 UNC) **⚠ mittaa**: sama merkintä esiintyy otteissa myös muun liitännän yhteydessä | [Danfoss Service and Parts Manual](https://assets.danfoss.com/documents/latest/604124/AX284661889190en-000404.pdf) (ote) |
| Kannan kulma | 22,5° tai 37,5° (vivun kallistus neutraalissa asennossa) **⚠ tarkista kannasta** | yllä olevat koodit |
| Vivun säätöalue | ±19,5° | [datalehti PVG 32] 520L0344 |
| Karan liike | ±7 mm, proportionaalialue ±4,8 mm (kelluntakaralla 8 mm) | [datalehti PVG 32] |
| Käyttömomentti karan liikkeelle lähtöön | **noin 2,2 ± 0,2 Nm** (PVM + PVE) yhdessä versiossa, **22 Nm** toisessa. 22 Nm tarkoittaisi 200 mm:n vivulla noin 110 N, mikä on epätodennäköisen raskas; 2,2 Nm (noin 11 N) on uskottavampi **⚠ tarkista** | [manualslib](https://www.manualslib.com/manual/1567379/Danfoss-Pvg-32.html), [roydisa.es](https://www.roydisa.es/wp-content/uploads/2012/12/danfoss-distribuidores-proporcionales.pdf) |
| Vivun pituus | **⚠ ei tiedossa**; mittapiirroksessa on noin 165 mm:n mitta, jonka kohde ei selvinnyt | [520L0344 (pvglobal)](https://pvglobal.com.sg/img/cms/technical_information/520l0344%20PVG32%20Technical%20Information.pdf) |

## Oman vivun suunnittelu

**Mittaa ensin kannasta** (kun venttiili on saapunut): kierteen koko ja syvyys (M8-pultti tai
kierremitta), kannan kierrereiän kulma ja kannan ulkomitat. Merkitse samalla, onko kannassa
rajoitusruuvit.

**Kokeiluvipu (ilman painetta):**
- M8-kierretanko tai M8 × 60–80 -pultti kierrettynä kantaan pohjaan, lukitusmutteri kantaa vasten.
  Halvin ja riittää karojen kokeiluun.
- **3D-tulostettu nuppi tai vipu:** PETG tai ASA (kestää lämpöä ja öljyä paremmin kuin PLA). M8-kierre
  tulostetun osan **sisään valetulla tai lämpöholkilla** (M8-lämpöholkki tai painettu M8-mutteri),
  ei tulostettua kierrettä. Vivun runkona M8-kierretanko, jonka päälle tulostettu nuppi: tanko kantaa
  taivutuksen, muovi vain otteen.
- Pituus noin 150–200 mm riittää: 2,2 Nm:n momentti vaatii silloin noin 11–15 N [laskelma]. Jos
  momentti onkin 22 Nm, voima on 110–150 N, mikä taivuttaa muovivivun; terästanko kestää.

**Käyttövipu (paineen alla):**
- Terästanko (M8, ruostumaton A4 kosteaan konehuoneeseen) ja tulostettu tai valmis nuppi. Kokonaan
  muovinen vipu voi katketa, jolloin venttiiliä ei voi ohjata käsin.
- Käsiohjaus on keulapotkurin ja ankkurivinssin varaohjaus, ja ankkurivinssi on turvallisuuskriittinen
  (kuorman pito). Vivun murtuminen tai tahaton liike (esim. vipuun nojaaminen) pitää huomioida:
  vipujen paikka ja suojaus niin, ettei niihin osu vahingossa **⚠ pätevä henkilö tarkistaa**.

## Avoimet kysymykset

- [ ] Vastaanotossa: onko kaikissa viidessä lohkossa vivun kanta; kannan kierre, syvyys ja kulma (22,5° vai 37,5°)
- [ ] Lue PVM-osio alkuperäisestä Danfossin ohjeesta (asennusohje tai varaosaluettelo): kierre, vivun pituus, käyttömomentti
- [ ] Tarvitaanko käsiohjausta käytössä vai vain koestuksessa (vaikuttaa siihen, tehdäänkö käyttövipu vai riittääkö kokeiluvipu)
