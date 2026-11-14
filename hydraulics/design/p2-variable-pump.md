# P2: Vickers PVH57 (pumppu, kytkin, kannake, suodatus ja asennus)

> **Tila:** **PÄÄTETTY 2026-10-27: P2 on Vickers PVH57**; **ostettu ja noudettu 2026-11-01, 150 €**
> [omistaja 2026-11-01]. Venttiileinä **Danfoss PVG 32** (päätös 2026-10-27, ostettu 2026-11-02),
> ks. [aux-circuit-ls-clean-sheet](aux-circuit-ls-clean-sheet.md). Päivitetty 2026-11-03: dokumentti
> rajattu pumppuun ja sen asennukseen PVG 32:n kanssa; vertailu F1-61:een ja FXDC + LS-purku -reitti
> on siirretty arkistoon ([archive/p2-fxdc-ls-unloading](archive/p2-fxdc-ls-unloading.md)), samoin
> F1-61-selvitys ([archive/p2-pump-options](archive/p2-pump-options.md)). Pumpun tiedot: selvitys
> 2026-10-25, asennusmitat ja porttikoot Eatonin luettelosta 2026-10-28, keskitys Ø127 ja Eatonin
> jalkakannake 2026-11-01. 2026-11-14: [kannakkeen paikka](#kannakkeen-paikka-kuorikytkin-ja-konepeti-2026-11-14): pumpun alle tuleva jalka ei mahdu potkuriakselin kuorikytkimen takia; selvitetään kiinnitystä vasemmalta konepetiin.
> Pätevän henkilön pitää tarkistaa säätöarvot, LS-kytkentä, kannake ja ohjauslogiikka ennen
> rakentamista.

## Selkokielinen yhteenveto

- **Pumppu:** Vickers PVH57 on säätötilavuuspumppu. Se pienentää itse iskuaan ja tuottaa vain sen
  öljyn, joka kuormille menee. Ylimäärää ei kuristeta lämmöksi, joten korkeat kierrokset eivät
  lämmitä öljyä samalla tavalla kuin kiinteällä pumpulla.
- **Ohjaus:** pumpun LS-portti kytketään PVG 32:n LS-porttiin. Kun kaikki PVG:n karat ovat
  keskellä, LS-signaali on yhteydessä säiliöön ja pumppu lepää valmiustilassa noin 20 barissa
  lähes ilman tuottoa. Kun jotain lohkoa ohjataan, pumppu nostaa paineen noin 20 bar kuorman
  painetta korkeammaksi, enintään 250 bariin. Erillistä purkuventtiiliä tai kuristinta ei tarvita.
- **Voimansiirto:** PTO → HRC 150 -joustokytkin (Taper Lock 2012 -holkit 48 mm ja 1 1/4") → pumppu
  omalla SAE C -kannakkeella runkoon. PTO-kytkintä ei ole, joten pumppu pyörii aina koneen kanssa.
- **Pois jäävät:** VPR3, Rexroth OD15, CETOP-pohjalaatta, BAV-713 ja VMP (PVG 32 korvaa ne), sekä
  F1-61-reitin BPV ja Spidex.
- **Avoinna:** kannakkeen suunnittelu ja pumpun mittaus, kytkimen holkit, paluusuodattimen vaihto
  lasikuituun (PVH57 vaatii puhtausluokan 16/14/12 yli 210 barissa) ja Danfossin vastaukset
  (pyöritys yli 2400 rpm, valmiustilan häviöteho).

## Pumppu: Vickers PVH57C-LAF-1S-10-C12V-31 (ostettu tori.fi:stä)

Ilmoitus: <https://www.tori.fi/recommerce/forsale/item/45217879>, **190 € tai tarjous** (tarkistettu
2026-10-25). Ilmoituksen teksti: *"Käyttämätön Vickers säätötilavuuspumppu. 57 cm3,
pyörimisuunta vastapäivään. Pumpun perään voidaan kytkeä toinen pumppu."*

- **Tyyppikilpi** (ilmoituksen kuvasta): Model Code `PVH57C LAF 1S 10 C12V 31`, Part No.
  **02-159964**, Made in U.S.A.
- **Kunto kuvien perusteella:** maalattu uudelleen tai kauttaaltaan (maalia kilven reunoilla ja
  pulttien kannoissa), ruostepilkkuja säädinlohkossa ja rungossa. Portit tulpattu. Akselissa ja
  tiivistepinnoissa ei näy vaurioita. "Käyttämätön" voi tarkoittaa varastossa ollutta tai
  kunnostettua.
- **Myyjän vastaukset** [myyjä 2026-10-25, omistajan välittämä]: akseli pyörii ilman ääniä;
  pumppu on säilytetty koko ajan lämpimässä tallissa; sisällä on öljyt, eikä ruostetta ole.
  Muuta myyjältä ei kysytä [omistaja 2026-10-25]: alkuperä, varastointiaika ja kunnostus jäävät
  tuntemattomiksi, ja säätimen asetus mitataan käyttöönotossa.

### Ikä ja siihen liittyvät riskit

**Valmistusvuosi ei ole tiedossa** **⚠ ei tiedossa**. Kilven tiedoista sitä ei voi lukea, ja
päivämääräkoodia ei ole tunnistettu. Arvio perustuu rakennenumeroon:

- Koodin **10** on rakennenumero. Huolto-ohje M-2210-S (rev. 2/93) kattaa sen.
- Vickersin huolto-ohjeessa, jonka revisio on 11/1997, kuvataan jo PVH57/63:n **rakenne 11**
  ([manualmachine.com](https://manualmachine.com/eaton/pvh63/350146-user-manual/), hakutuloksen
  tiivistelmä, ei luettu kokonaan).
- Kilvessä lukee pelkkä *Vickers* eikä Eaton. Tämä ei rajaa ikää, koska Eaton (osti Vickersin 1999)
  ja nyt Danfoss käyttävät Vickers-nimeä yhä.

Pumppu on siis **todennäköisesti 1980-luvun lopulta tai 1990-luvulta**, noin 25–40 vuotta vanha
[arvio]. Tarkemmin sen voi tarvittaessa kysyä Danfossilta sarjanumeron perusteella.

**Riskit, jotka liittyvät ikään eivätkä käyttöön:**

| Riski | Miksi | Mitä tehdään |
|---|---|---|
| Tiivisteiden vanheneminen | Akselitiiviste ja O-renkaat (nitriili) kovettuvat ja halkeilevat vuosikymmenten varastoinnissa, vaikka pumppua ei olisi käytetty | **Vaihda akselitiiviste ja O-renkaat ennen asennusta**, ks. [Tiivistesarja](#tiivistesarja) |
| Sisäinen korroosio | Jos pumppu on varastoitu ilman öljyä, sylinteriporaukset, männät ja säätimen karat voivat ruostua. Ruostepilkut säädinlohkossa ulkopuolella viittaavat kosteuteen | Katso porttien sisään, pyöritä akselia käsin; säätimen karan pitää liikkua vapaasti |
| Laakerit | Pitkä seisonta ilman pyörimistä voi jättää laakereihin kosteus- tai seisontajälkiä | Akselin pitää pyöriä käsin tasaisesti ilman kohtia, joissa se tarttuu tai rahisee |
| Säädin | Kara voi jumittua lakkaan tai ruosteeseen, jolloin pumppu ei palaa valmiustilaan | Tarkista käyttöönotossa paine ja valmiustila mittarilla 2G1 |
| Varaosat | Vanha rakenne voi poiketa nykyisestä | **PVH-sarjaa myydään yhä** (Danfoss/Vickers), ja PVH57:n tiiviste-, laakeri- ja mäntäsarjoja on saatavilla jälleenmyyjiltä ([hydraulic-supply.com](https://www.hydraulic-supply.com/877423.html)) **⚠ varmista sopivuus rakenteelle 10** |

### Tiivistesarja

Lähteet: hakutulosten tiivistelmät 2026-10-25; sivuja ei saatu avattua tästä ympäristöstä, joten
**⚠ tarkista koodi ja hinta toimittajalta** pumpun osanumerolla 02-159964 ja tyyppikoodilla.

| Koodi | Mitä | Lähde |
|---|---|---|
| **02-102244** (vanha koodi **02-102260**, myös C1AC14) | PVH57/63:n tiivistesarja. Vickersin huoltotiedote M-2206-S (PVH57/63, **rakenne 11**, rev. 11/1997) viittaa siihen: *"Available in double shaft seal kit 02-102244"*; erillinen akselitiiviste 513439 mainitaan kaksoistiivisteversiolle. Hinta noin **853 $** (Motion, tarjouspyyntö) | [M-2206-S (paro.nl)](https://paro.nl/library//storage/datasheets/Eaton/PVH57_M-2206-S22175617.pdf/datasheet.html), [Motion](https://www.motion.com/products/sku/01283726), [hydraulic-supply.com](https://www.hydraulic-supply.com/02-102244.html) |
| 02-346217 | Danfossin sivulla PVM-sarjan alla ("PVM series code B"); jälleenmyyjä mainitsee PVQ63:n. **Ei luultavasti tämän pumpun sarja.** | [Danfoss PowerSource](https://powersource.danfoss.com/products/pumps/industrial-pumps/medium-duty-open-circuit-piston-pumps/pvm-series-code-b-pumps/p/02-346217) |

- **Epävarmuus:** Vegan pumppu on **rakenne 10** ja yksinkertaisella akselitiivisteellä (`S`).
  Löydetty tieto koskee rakennetta 11, ja sarjasta puhutaan kaksoistiivisteen yhteydessä. Kysy
  Danfossin jälleenmyyjältä, sopiiko 02-102244 rakenteelle 10.
- **Hinta on noin nelinkertainen pumpun hintaan nähden.** Halvempi vaihtoehto: jos pumppu pyörii
  käsin tasaisesti ja sisältä on puhdas, vaihdetaan vain akselitiiviste ja ulkoiset O-renkaat
  (portit, laipat, säädin), jotka saa mitoilla tavallisina osina. Mitat tiivisteistä tai
  osaluettelosta **⚠ ei tiedossa**. Tämän arvioi hydrauliikkakorjaamo.
- **Mitä voi vaihtaa avaamatta pumppua** [arvio yleisen mäntäpumppurakenteen perusteella,
  **⚠ tarkista huolto-ohjeesta M-2210-S**]:
  - *Ilman purkua:* porttien ja laippojen O-renkaat, tulppien O-renkaat ja säätimen O-renkaat
    (säädin irrotetaan omilla ruuveillaan, mäntäryhmä ei aukea). Akselitiiviste vaihdetaan
    monissa mäntäpumpuissa ulkopuolelta kiilan ja lukkorenkaan irrotuksen jälkeen; PVH:n osalta
    tämä on tarkistamatta.
  - *Vaatii purun:* rungon ja venttiililohkon välinen tiiviste ja muut sisäiset tiivisteet.
  - **Avattua liitosta ei koota vanhoilla tiivisteillä.** Ne ovat painuneet muotoonsa ja vuotavat
    helposti uudelleen asennettuina. Jos pumppu avataan, liitoksen kaikki tiivisteet vaihdetaan.
    Avaamattomat sisäiset tiivisteet jätetään rauhaan: ne ovat suojassa, ja liikuttamaton tiiviste
    pitää yleensä paremmin kuin liikutettu.

**Arvio (päivitetty 2026-10-25 myyjän vastausten jälkeen):** ikä ei sinänsä estä käyttöä, koska
sarjaa valmistetaan yhä ja osia saa. Myyjän mukaan pumppu on säilytetty lämpimässä, sisällä on
öljyt eikä ruostetta, ja akseli pyörii äänettömästi. Silloin sisäisen korroosion ja laakerivaurion
riski on pieni, eikä pumppua ole syytä avata. **Koko tiivistesarjaa (02-102244) ei tarvita.**
Tiivisteiden ikä on yhä riski: akselitiiviste ja ulkoiset O-renkaat voivat olla kovettuneet, vaikka
pumppu on ollut öljyssä. Tarkista ostaessa, ettei akselitiivisteen ympärillä ole öljyä ja että
tiivisteen huuli ei ole halkeillut, ja vaihda ulkoiset O-renkaat liitäntöjä tehdessä. Akselitiiviste
vaihdetaan, jos se vuotaa koeajossa. Hydrauliikkakorjaamon kannattaa koeajaa pumppu ennen
asennusta.

### Tyyppikoodi

Lähde: Vickersin huolto-ohje *M-2210-S, PVH Piston Pumps Including Controls* (rev. 2/93), s. 3
([PDF](https://hydraulicsonline.com/wp-content/uploads/2019/12/Eaton-Vickers-PVH-Series.pdf), luettu
tekstinä).

| Osa | Merkitys |
|---|---|
| PVH **57** | Suurin kierrostilavuus **57,4 cm³** |
| **C** | SAE C -nelireikälaippa (SAE J744-127-4); mobiiliversio (teollisuusversiossa QI) |
| **L** | **Vasen eli vastapäivään** akselin päästä katsottuna → **sopii Vegaan** ([vessel: Pyörimissuunnat](../../vessel/README.md#pyörimissuunnat)) |
| **A** | Läpivetopumppu, takana SAE A -laippa toiselle pumpulle |
| **F** | Pääliitännät SAE-nelireikälaipoilla |
| **1** | SAE C -suora akseli kiilalla, Ø 1,25" = 31,75 mm (J744-32-1) |
| **S** | Yksinkertainen akselitiiviste |
| **10** | Rakennenumero |
| **C** | Paineenrajoittimen säätöalue 70–250 bar |
| **12** | Tehdasasetus **120 bar** |
| **V** | Kuormantunto (LS), paine-ero 20 bar (säädettävissä 17–30 bar) |
| **31** | Säätimen rakennenumero |

### Tekniset tiedot

Lähde: Eatonin luettelo *Industrial & Mobile Variable Displacement Piston Pumps* V-PUPI-TM008-E1
(10/2013) ([PDF](https://www.appliedfluidpower.com/media/wysiwyg/PDFs/PVH_Series.pdf), skannattu,
s. 7, 8 ja 31 luettu kuvina; asennusmitat s. 20–22 luettu kuvina 2026-10-28). Pumppu on **mobiiliversio**: teollisuusversiossa on aina lisäkoodi
Q250 tai Q140, eikä tässä koodissa ole lisäkoodia.

| Kohde | Arvo | Lähde |
|---|---|---|
| Kierrostilavuus | 57,4 cm³ | luettelo s. 7 |
| Nimellispaine | 250 bar (LS-järjestelmässä paineenrajoitin voi olla 280 bar) | s. 7 |
| **Suurin kierrosluku, mobiili** | **2000 rpm** imupaineella −0,17 bar (127 mm Hg), **2400 rpm** imupaineella 0 bar, **3000 rpm** imupaineella +0,48 bar | s. 7 |
| Suurin kierrosluku, teollisuus (vertailu) | 1500 / 1800 / 1800 rpm | s. 7 |
| Tuotto 250 barissa ja 2400 rpm:llä | 134 l/min (mobiili) | s. 7 |
| Teho paineenrajoituksella, nollatuotto | noin 10 kW 1800 rpm:llä ja 250 barissa (luettu kuvaajasta *Input power, cutoff* karkeasti) **⚠ tarkista** | s. 8 |
| Öljy | viskositeetti 16–40 cSt optimi, kylmäkäynnistys ≤ 5000 cSt, hetkellisesti ≤ 104 °C | s. 31 |
| Puhtaus (säätötilavuuksinen mäntäpumppu) | 18/16/14 (≤ 140 bar), **17/15/13 (140–210 bar)**, 16/14/12 (yli 210 bar) | s. 31 |
| Asennus | **akseli vaakaan** (*"Mounting attitude should be horizontal"*); pystyasennus vain erikoisversiona (lisäkoodi `057`, ylimääräinen vuotoportti), jota tässä pumpussa ei ole. Suora veto joustavalla kytkimellä; linjaus asennuspiirustuksen toleransseihin. **Kiertoasento akselin ympäri:** luettelo ei määrää sitä. **Korjaus 2026-10-28:** pääportit ovat venttiililohkon **päällä ja pohjassa**, eivät kyljissä. Luettelon piirustuksessa (oletettavasti R-pumppu) säädin on ylhäällä, 1":n lähtö päällä (näkymä A-A) ja 2":n imu pohjassa (alin näkymä on pohjakuva). Omistajan pumpussa (L) säädinpuolella ylhäällä on laippaportti, jota omistaja pitää imuna [omistaja 2026-10-28, kuva]: L-pumpun venttiililohko on eri osa kuin R-pumpun (M-2206-S s. 2), joten portit voivat olla toisin päin **⚠ tarkista reikäväleistä** (imu 77,8 × 42,9 mm, lähtö 52,4 × 26,2 mm). Vuotolinja aina **ylemmästä** vuotoportista, jotta kotelo pysyy täynnä | s. 21, 30, 31; M-2206-S |
| Paino | noin 36 kg (jälleenmyyjät) **⚠ tarkista** | jälleenmyyjät |
| Imuaukko | **2" SAE J518 code 61** -nelireikälaippa (reikäväli 77,77 × 42,88 mm, kierre `F`-mallissa 1/2-13 UNC; `M`-mallissa M12). **Korjaus:** jälleenmyyjien 2 1/2" oli väärin. Imu on venttiililohkon päällä tai pohjassa (ks. Asennus) **⚠ tarkista pumpusta** | s. 21–22 (*kuvana*) |
| Painelähtö | **1" SAE J518 code 61** -laippa (reikäväli 52,37 × 26,19 mm, kierre 3/8-16 UNC / M10×1,5) | s. 21–22 |
| LS-portti | SAE O-rengasportti 9/16-18 UNF (3/8":n putkelle); painemittariportti M10 (tulpattu) | s. 21 |
| Asennuslaippa | SAE C nelireikä: keskitysolake Ø127,00/126,95 mm, reiät Ø14,15–14,53 mm, reikäneliö 2 × 57,25 = **114,5 mm**; pumpun pituus laipasta takapäähän noin 293 mm (mitta C). **Ø125 mm ei koske tätä pumppua** (2026-11-01): se on metrinen lisävaihtoehto ISO 3019/2-125B4HW (laippakoodi **M**, vain N-akselin kanssa; reikäneliö 2 × 56,57 = 113,1 mm, reiät Ø14,00–14,37). Tämän pumpun koodissa laippa on **C** = SAE J744-127-4, siis **Ø127** [Eaton TM008 s. 29; M-2206-S s. 8]. Ks. [Eatonin jalkakannake FB-C4-10](#eatonin-jalkakannake-fb-c4-10) | s. 21–22, 29 |
| Akseli (koodi 1) | SAE C suora kiila (J744-32-1): **Ø31,75 mm**, kiila 7,93 mm, kiila-akselin pituus laipasta 56,0 mm | s. 20 |
| Säätöruuvit | painesäädin noin 28 bar/kierros; LS-paine-ero noin 14 bar/kierros (tehdasasetus 20 bar) | s. 21; M-2206-S s. 8 |
| Kotelovuoto | pakollinen vuotolinja säiliöön. Vuotoportti 3/4-16 UNF SAE O-rengas (1/2":n putkelle); luettelon piirustuksessa **kaksi**: alhaalla ja ylhäällä ("optional drain port"). Onko ylempi portti tässä pumpussa avattu, **⚠ tarkista pumpusta** | s. 21; M-2210-S |
| Käyttöönotto | kotelo täytetään öljyllä jonkin portin kautta ennen käynnistystä; ilmaus avaamalla lähtöliitintä; 5–10 min kuormittamatta, öljy ei saa olla maitoista | M-2206-S s. 7 |

### Sopivuus Vegaan [laskelma]

Oletukset: volumetrinen hyötysuhde 95 %, mekaaninen 90 %, tyhjäkäynti 700 rpm.

| Tarkistus | Tulos |
|---|---|
| Tuotto 700 rpm:llä | noin 38 l/min, enemmän kuin keulapotkurin 33,8 l/min ✅ |
| Momentti 250 barissa | noin 254 Nm; PTO noin 420 Nm ✅; HRC 150 (noin 600 Nm **⚠ vahvista**) riittää (tarve kertoimilla noin 430 Nm) ✅ |
| Pyörimissuunta | L ✅ |
| Kierrosluku | koneen 2400 rpm on tasan mobiiliversion rajalla, kun imupaine on vähintään 0 bar. Säiliö on noin 1 m pumpun yläpuolella ja imulinja 50 mm. Täydellä iskulla 2400 rpm:llä (noin 138 l/min) imupaine olisi kylmällä öljyllä arviolta 0…−0,03 bar. **Vegan käytössä täyttä iskua ei tule korkeilla kierroksilla**: ajossa pumppu on valmiustilassa ja keulapotkuria käytettäessä virtaus on rajattu noin 35 l/minuun. Luettelo ei kerro, saako pienemmällä iskulla pyöriä nopeammin **⚠ kysy Danfossilta**. |
| Laippa ja akseli | SAE C ja kiila-akseli: **ei ISO 7653 eikä 8×32×36**. Kannake suunnitellaan PVH57:lle; kytkimeksi HRC 150 kartioholkeilla (päätös 2026-10-27) [omistaja 2026-10-25, 2026-10-27] |
| Paino | noin 36 kg (F1-61 8,5 kg): kannake mitoitetaan tälle painolle ja tärinälle; reaktiomomentti noin 254 Nm on lähes sama kuin F1-61:llä (noin 250 Nm) [laskelma] |

### Eatonin jalkakannake FB-C4-10

Lisätty 2026-11-01. Lähde: Eaton V-PUPI-TM008-E1 s. 30 (*mitat luettu kuvasta*) ja
[Hydraulic Parts Source](https://www.hydparts.com/itemdetail/V-02-143419R).

Eatonin valmis jalkakannake *"Model FB-C4-10 Foot Mounting Kit for All PVH Pumps"*, **osanumero
02-143419**. Sarjaan kuuluvat kannake ja neljä ruuvia pumpun kiinnitykseen; sitä ei toimiteta
pumpun mukana. Kannake on SAE C -nelireikälaipalle, joten se sopii tähän pumppuun.

| Mitta | Arvo |
|---|---|
| Keskitysreikä | Ø127,05–127,15 mm (pumpun olake Ø126,95–127,00) |
| Pumpun kiinnitys | 4 × 1/2-13 UNC -kierre läpi, reikäneliö 114,5 mm (2 × 57,25) |
| Akselin keskiön korkeus jalan pohjasta | 174,75 mm |
| Jalan kiinnitysreiät | 4 × Ø11,0 läpi, upotus Ø37,0 × 1,0 mm; reikävälit 228,0 ja 101,8 mm **⚠ tarkista** (tulkittu kuvasta) |
| Jalan paksuus | 20,5 mm |
| Laippalevyn paksuus | noin 23 mm **⚠ tarkista** (tulkittu kuvasta) |
| Saatavuus ja hinta | **Poistunut valikoimasta**: *"This product has been discontinued and is no longer available"* ([Danfoss PowerSource 02-143419](https://powersource.danfoss.com/products/p/02-143419), luettu 2026-11-01). Hintaa ei löytynyt mistään; [Hydraulic Parts Source](https://www.hydparts.com/itemdetail/V-02-143419R) näyttää hinnan vain kirjautuneille, ja eBay, Motion ja Applied estivät automaattiset haut. Käytettynä voi löytyä eBaystä **⚠ ei tarkistettu**. Vertailuksi kaksireikäinen FB-C-10 (422584) noin 990 $ (Motion, hakutuloksen tiivistelmä) |
| Ulkomitat ja paino (Danfoss) | korkeus 10,64" ≈ 270 mm, pituus 10,47" ≈ 266 mm, leveys 8,15" ≈ 207 mm; **29 lb ≈ 13 kg** |

Muiden valmistajien SAE C -jalkakannakkeet (2/4 reikää) maksavat noin 35–80 $ (esim. [Dalton](http://www.daltonhydraulic.com/hydraulic-pumps/mounting-brackets), [Splitez](https://www.splitez.com/engine_pump_adapters.html); hakutulosten tiivistelmistä, sopivuus SAE C:hen **⚠ tarkista**) tai Australiassa noin 424 AUD ([hydraulic.online](https://www.hydraulic.online/Foot-Mount-SAE-A-B-or-C-Mount-Motors-Or-Pumps-p355993370), SAE C -vaihtoehto, 7 kg). Niiden akselin keskiö on yleensä matalalla (esim. LDI FM400: 4,312" ≈ 109,5 mm), joten ne tuskin osuvat PTO:n korkeudelle ilman välialustaa. FB-C4-10 on poistunut valikoimasta. Siksi omistajien oma
laserleikattu kannake ([päätös 2026-10-23](../../decisions.md)) on edelleen järkevämpi.
FB-C4-10:n mitat kelpaavat kuitenkin malliksi: keskitysreiän toleranssi, 1/2-13 UNC -kiinnitys
ja levyn paksuus (Eatonilla noin 20–23 mm, meillä 10 mm:n teräslevy jäykisteineen).
Laserleikattu reikä ei yleensä osu suoraan 0,1 mm:n toleranssiin: leikkaa reikä hieman
pienemmäksi ja avarra se, tai pyydä leikkaajalta mittatarkka reikä **⚠ tarkista leikkaajalta**.

### Kannakkeen paikka: kuorikytkin ja konepeti (2026-11-14)

**Tilanne [omistaja 2026-11-14]:** potkuriakseli (Ø90) liittyy merivaihteen lähtöakseliin
kuorikytkimellä (vähintään noin Ø160 **⚠ mittaa**) samassa kohdassa pituussuunnassa kuin pumppu.
Omistajan FreeCAD-mallissa potkuriakselin keskiö on noin 203 mm sivussa ja 155 mm alempana kuin
pumpun akseli, perästä katsottuna oikealla. Konepeti jatkuu pumpun kohdalle; sen yläpinta on noin
240 mm PTO-akselin alapuolella, ja PTO:n alla pedissä on kaukalo vaihteiston öljypohjalle
([vessel](../../vessel/README.md)).

**Seuraus [laskelma]:** pumpun alle tuleva jalka ja pukit eivät mahdu. Ø160-kytkimellä luonnoksen
pohjalevyn reunaan jäisi noin 13 mm ja sivutukeen noin 8 mm, ja oikean puolen pukit osuisivat
kytkimen kohdalle. Pumppu itse mahtuu: sen rungosta ja pulttikuvion ympärille rajatusta
laippalevystä (x ≈ −85 mm) kytkimeen jää noin 55–58 mm.

**Selvitettävä ratkaisu:** kannake kiinnitetään **perästä katsottuna pumpun vasemmalle puolelle**,
poispäin kytkimestä [omistajan ehdotus 2026-11-14]. SAE C -laippa sallii pumpun pitämisen nykyisessä
asennossa. Koska peti on 240 mm akselin alapuolella ja kaukalo on pumpun alla, kannake on
**kulmapilari** konepedin vasemmalle reunalle kaukalon viereen:

- laippalevy jatkuu alas ja vasemmalle pedin yläpintaan (pumpun paino ja reaktiomomentti
  vaikuttavat levyn tasossa, joten levy on niille jäykkä);
- pumpun vasemmalle sivulle pitkittäinen pystylevy laipasta taaksepäin (vähintään noin 150 mm,
  pumpun painopisteen yli), joka kantaa keikkumisen eteen ja taakse;
- jalkalevy pedin päälle, 4 × M12 8.8 ja Ø15-reiät, pulttien väli pituussuunnassa mahdollisimman suuri.

Kuormat pulteille [laskelma, oletukset: pumppu ja kannake 46 kg, kolminkertainen isku,
reaktiomomentti 254 Nm, painopiste noin 150 mm pulttilinjasta sivussa, pulttiväli sivusuunnassa
noin 90 mm]: momentti noin 450 Nm → noin 2,5 kN vetoa pulttia kohti. M12 8.8:n esikiristysvoima on
noin 38 kN, joten pultit riittävät. Kapea jalka pedin päällä on jäykkyyden heikoin kohta, joten
jalan pituus ja rivat ratkaisevat. Mitoitus tehdään, kun kaukalon reuna ja pedin leveys on mitattu.
Pätevän henkilön pitää tarkistaa lopullinen kannake.

### Riittääkö 10 mm:n teräslevy [laskelma]

Lisätty 2026-11-01. Karkea arvio. Pätevän henkilön pitää tarkistaa lopullinen kannake.

**Oletukset:** L-kannake, jossa on pystylevy (pumpun laippa) ja jalkalevy runkoon. Pystylevy on
10 mm, S235 ja 200 mm leveä. Akselin keskiö on 175 mm jalan pohjasta (kuten FB-C4-10:ssä).
Pumppu painaa 36 kg **⚠ punnitse**, ja sen painopiste on noin 150 mm laipan takana **⚠ arvio**
(pumpun pituus noin 293 mm).

| Kuorma | Tulos |
|---|---|
| Pumpun paino, staattinen | taivutusmomentti noin 53 Nm pystylevyn juuressa → jännitys noin **16 MPa**; S235:n myötöraja 235 MPa ✅. Kolminkertaisellakin iskukuormalla (aallot, telakointi) noin 48 MPa ✅ |
| Väsyminen hitsissä | noin 16 MPa yhden g:n tärinää kohti. Kuormaa kantavan pienahitsin väsymisraja on luokkaa 25–35 MPa, joten jatkuva tärinä yli noin ±1,5 g on riski ilman ripoja **⚠ arvio** |
| Reaktiomomentti 254 Nm (250 bar) | vaikuttaa levyn tasossa: jännitys noin 4 MPa ✅. Pultteihin tulee leikkausvoimaa noin 0,8 kN pulttia kohti ✅; keskitysolake kantaa sen pääosin |
| Taipuma | noin 0,2 mm akselin kohdalla. Linjaus tehdään pumppu paikallaan, joten taipuma ei haittaa ✅ |
| **Ominaistaajuus ilman ripoja** | noin **15 Hz** (pumppu keikkuu eteen ja taakse). **Koneen 1. kertaluku on 700–2400 rpm = 12–40 Hz**, joten kannake resonoisi käyttöalueella ❌ |
| Ominaistaajuus kahdella 10 mm:n kolmiorivalla (noin 150 × 150 mm) | levyn jäykkyys kasvaa noin 300-kertaiseksi. Käytännössä taajuus jää liitosten ja jalkalevyn joustojen takia alemmaksi, mutta selvästi yli 120 Hz:n (6-sylinterisen sytytystaajuus 2400 rpm:llä) **⚠ arvio** ✅ |

**Johtopäätös:** 10 mm riittää lujuudeltaan, jos kannakkeessa on **jäykisteet**. Pelkkä
10 mm:n L-levy on liian joustava: se resonoisi koneen kierrosalueella, ja tärinä rikkoisi hitsit
ja kuluttaisi kytkintä. Siksi:

- Tee pystylevyn kummallekin sivulle kolmiorivat, jotka ulottuvat jalkalevyyn (Eatonin
  FB-C4-10:ssä on keskellä ripa, ja sen seinät ovat noin 20–23 mm).
- Kiinnitä jalkalevy runkoon pulteilla ripojen ja pystylevyn läheltä, jotta jalkalevy ei
  taivu.
- Pumpun kiinnitys: 4 × M12 (tai 1/2-13 UNC) läpi levystä muttereilla, **lujuusluokka 8.8
  riittää**: puristusvoima noin 38 kN pulttia kohti (μ = 0,12), kitkalla kantava leikkaus noin
  5,8 kN pulttia kohti, kun tarve on noin 0,8 kN leikkausta ja noin 0,7 kN vetoa (kolminkertainen
  isku) → varmuus noin seitsenkertainen; kiristys noin 80 Nm **⚠ tarkista taulukosta**. **Kovat
  aluslaatat** ISO 7089 M12 (Ø24, 200 HV) molemmin puolin, **ei jousilaattoja**: väljässä
  Ø14,15–14,53 reiässä M12:n kanta (tukipinta noin Ø16,6) painaisi noin 50 mm²:lle noin 750 MPa,
  laatan kanssa noin 290 mm² ja noin 130 MPa; jousilaatta (DIN 127, poistettu standardeista)
  litistyy jo muutamassa kilonewtonissa eikä lukitse esikiristettyä pulttia, vaan painumallaan
  vähentää esikiristystä. Jos laatta ei mahdu, ISO 7092 (Ø20) **⚠ tarkista pumpusta**. Lukitus
  keskilujalla kierrelukitteella (esim. Loctite 243), lukkomutterilla tai Nord-Lock-laatoilla. **Ei M14:ää:** laipan reiät
  Ø14,15–14,53 jättäisivät vain noin 0,2 mm välystä. 10 mm:n levyyn ei kannata tehdä kierteitä.
- Nykyiset pumput on kiinnitetty 10 mm:n teräskannakkeella koneeseen [blogi 2017-07-04], mutta
  ne ovat paljon kevyempiä (F1-61 8,5 kg), joten vertailukohta ei kata PVH57:ää.

### Pumpun kohdistus

Lisätty 2026-11-01 [omistajan ehdotus 2026-11-01, arvio]. Kohdistus tehdään kahdessa vaiheessa:
ensin kannakkeen paikka tulostetulla sovitteella, sitten lopullinen linjaus oikealla pumpulla.

**HRC 150:n sallimat virheet:** säteissuuntainen siirtymä 0,4 mm, kulmavirhe 1°, aksiaalinen
0,9 mm (Fennerin HRC-taulukko [Scribdissä](https://www.scribd.com/document/430712108/HRC-Coupling),
kulmavirhe [Kramp HRCB150FTL](https://kramp.com/shop-ro/en/p/hub-gg-hrc-150-tl-2012-f--HRCB150FTL);
toissijaisia lähteitä **⚠ tarkista valmistajan luettelosta**). Tavoitteeksi noin puolet näistä:
**siirtymä ≤ 0,2 mm** ja kulmavirhe ≤ 0,5°, jolloin elastinen välikappale kestää pitkään.

1. **Kannakkeen paikka tulostetulla sovitteella (karkea, ±0,5 mm riittää).** Sovitteessa on
   holkki PTO-akselille (sisähalkaisija 48 mm), keskitysolake Ø127 kannakkeen reikään ja
   pituus, joka vastaa kytkimen ja pumpun akselin mittaa (laipan pinnasta PTO-akselin päähän).
   Aksiaalinen mitta ei ole kriittinen, koska Taper Lock -navat liukuvat akselilla ennen
   kiristystä; molempien akselien pitää vain mennä napaan riittävän syvälle (holkki 2012
   ≈ 32 mm, pumpun kiila-akseli 56 mm laipasta).
   - **Mitoitus [laskelma, HRC150 Dunlopin luettelosta]:** navat eivät kosketa toisiaan; niiden
     sisäpintojen väli on elementin leveys **G = 40,5 mm** (L 107,5 − 2 × C 33,5). Jos kumpikin
     napa asennetaan akselinsa pään tasalle, pumpun napa ulottuu 56 mm:n päähän pumpun
     laippapinnasta, ja **PTO-akselin pää on noin 56 + 40,5 = 96,5 mm laippapinnasta**. Tämä
     on sovitteen pituus keskitysolakkeen laippapinnasta PTO-akselin päähän. Navan voi siirtää
     akselilla taaemmas, joten mitta saa vaihdella sen mukaan, paljonko akselia jää navan
     taakse. PTO-akselin vapaa pituus on piirustuksen mukaan noin 60 mm (mitattu mittakaavasta,
     [Advance 300-WXT03](../../datasheets/README.md)), joten 33,5 mm:n napa mahtuu sille ja säätövaraa jää noin 25 mm **⚠ tarkista pumpun akselin pituus ja PTO-akselin vapaa pituus veneellä**.
   - Tulosta holkki ja keskitysolake erikseen ja yhdistä ne suoralla putkella tai tangolla.
     Pitkä tuloste kieroutuu ja taipuu. Tulosta reiät hieman ahtaiksi ja sovita ne
     viilaamalla tai hiomalla.
   - Pyöritä sovitetta PTO-akselin ympäri ja katso, heittääkö Ø127-olake. Heitto kertoo
     tulostusvirheestä.
2. **Hitsaa ensin, kohdista vasta sitten.** Hitsaus vetää enemmän kuin 0,2 mm. Hitsaa runkoon
   kiinnitysalustat (pukit), ja pulttaa kannake niihin. Kannakkeen jalkaan **pitkittäiset
   reiät** sivusuuntaiseen säätöön ja korkeuden säätöön **välilevyt** (ruostumattomat
   säätölevyt, esim. 0,1–1 mm).
3. **Lopullinen linjaus oikealla pumpulla.** Pumppu paikallaan, kytkinnavat akseleilla ilman
   elastista välikappaletta. Pumpun paino ja kannakkeen taipuma ovat silloin mukana, joten
   taipuma kompensoituu välilevyillä.
   - Säteissuuntainen siirtymä: viivain tai mittakello napojen ulkokehää vasten neljässä
     kohdassa (ylä, ala, sivut).
   - Kulmavirhe: napojen välin erotus neljässä kohdassa rakotulkilla.
   - Kiristä pultit, mittaa uudelleen ja tarkista linjaus koeajon jälkeen.
4. **Taipuma:** laskettu 0,2 mm koskee ripoja vailla olevaa 10 mm:n levyä. Rivoilla se jää
   noin sadasosamillimetreihin [laskelma]. Kummassakin tapauksessa vaiheen 3 linjaus kattaa sen.

## Miten LS-linjaa käytetään

CV-säädin pitää pumpun lähtöpaineen noin 20 bar LS-portin painetta korkeampana, ja paineenrajoitin
kääntää pumpun nollatuotolle asetuspaineessa [M-2210-S s. 6].

**Kytkentä PVG 32:n kanssa** (päivitetty 2026-11-03): 1/4":n LS-letku PVG 32:n pumppumoduulin
LS-portista (G 1/4) pumpun LS-porttiin (9/16-18 UNF O-rengas, SAE -6). PVG 32:n pumppumoduuli on
suljetun keskiasennon malli 157B5111, joka on tarkoitettu säätötilavuuspumpulle
([aux-circuit-ls-clean-sheet](aux-circuit-ls-clean-sheet.md#mitä-koodit-kertovat-2026-11-03)).

| Tila | PVG 32 | Pumppu |
|---|---|---|
| Lepo, sähkökatko, hätäseis | kaikki karat keskellä (jouset), LS-kanava yhteydessä säiliöön | valmiustila noin 20 bar, lähes nollatuotto |
| Lohkoa ohjataan | lohkon LS-signaali kulkee pumpulle (suurin kuormapaine valitaan) | kuorman paine + noin 20 bar, enintään 250 bar |
| Kuorma jumittuu | LS = kuorman paine | pumppu nousee 250 bariin ja kääntyy nollatuotolle |

Erillistä LS-purkuventtiiliä (2/2), kuristinta tai virtauksensäätöventtiiliä ei tarvita: PVG 32:n
peruslohkojen kompensaattorit rajaavat kunkin lohkon virtauksen karan koon mukaan. PVPX-purkuventtiiliä
ei voi lisätä nykyiseen pumppumoduuliin, eikä sitä tarvita.

Riittääkö noin 20 barin paine-ero PVG 32:n kompensaattoreille ja PVE:iden pilottiöljylle,
**⚠ tarkista Danfossilta** (ohjeessa 520L0344 käyrät 10 ja 20 barin paine-erolle).

## Tarvittavat osat pumpun lisäksi (minimi)

Venttiilit ovat Danfoss PVG 32 ([aux-circuit-ls-clean-sheet](aux-circuit-ls-clean-sheet.md)); sen liitännät ja osat ovat [hankintalistassa](../procurement.md). Letkut, säiliö ja jäähdytin säilyvät.

| # | Osa | Huom. |
|---|---|---|
| 1 | **HRC 150 -joustokytkin** (päätös 2026-10-27): kaksi napaa Taper Lock -holkeille (F tai H asennuksen mukaan) ja elastinen välikappale | ks. alla |
| 2 | Taper Lock 2012 -kartioholkit: **48 mm** (PTO) ja **1 1/4"** (pumppu, 31,75 mm), kiilaurat | vakio-osia, ei koneistusta; **⚠ tarkista** koodit ja 48 mm:n holkin kiilauran syvyys |
| 3 | Kannake SAE C -nelireikälaipalle | ei vielä tehty; tapa: 10 mm:n teräslevy, laserleikkaus ja hitsaus. Pumppu noin 36 kg; laippa Ø127 mm:n keskitys ja 114,5 mm:n reikäneliö, ks. [tekniset tiedot](#tekniset-tiedot) |
| 4 | Imuliitin: 2" SAE code 61 -laippa (UNC-pultit), O-rengas ja letkuliitin 50 mm:n letkuun | 2" = 50,8 mm, joten supistusta ei tarvita |
| 5 | Painelähdön 1" SAE code 61 -laippa (3/8-16 UNC) ja supistus 3/4":n painelinjaan | |
| 6 | Kotelovuotolinja (vähintään noin 1/2") ylimmästä vuotoportista säiliöön öljypinnan alle | ei yhteiseen paluulinjaan |

**Rivit 1–2: HRC 150 kartioholkeilla** (selvitys ja päätös 2026-10-27; korvaa PVH57-reitissä Spidexin). PVH57:n
akseli on lieriömäinen kiila-akseli, joten Spidexin etu (valmis 8×32×36-napa F1-61:lle) ei enää
päde. HRC 150:n H- tai F-napaan käy **Taper Lock 2012 -kartioholkki** (reikä 14–50 mm), jota saa
vakiona sekä **48 mm:n** (PTO) että **1 1/4":n** (pumppu) kiilaurallisena: ei koneistusta
[jälleenmyyjät, **⚠ tarkista** holkkikoodit; 48 mm:n holkissa kiilaura voi olla matala].
Momentti noin 600 Nm (nimellinen, **⚠ vahvista**), tarve kertoimilla noin 430 Nm ✅ [laskelma].
Hinnat: napa noin 19 € + ALV ([atlantis-pt](https://atlantis-pt.abstore.pl/couplings-semi-coupling-hub-hrc-150,c225,p263,en.html)),
elastinen osa noin 10 £ + ALV ([Cromwell](https://cromwell.co.uk/shop/bearings-and-transmissions/couplings/hrc150i-coupling-insert/p/DUN6956364E)),
holkit **⚠ hinta ei tiedossa** (arviolta 10–25 € kpl). Yhteensä arviolta **noin 80–120 € + ALV**
eli selvästi halvempi kuin Spidex (noin 215 € + ALV ja pumppunapa, jonka saatavuus 1,25":n
reiällä on epävarma). HRC 150 on halkaisijaltaan isompi (150 mm vs. 105 mm), mikä otetaan
huomioon kannakkeessa.

**Poistuu tai muuttuu:**
- **VPR3, Rexroth OD15, CETOP-pohjalaatta, BAV-713 ja VMP jäävät pois;** PVG 32 korvaa ne
  (päätös 2026-10-27). Niitä ei kannata myydä ennen kuin PVG 32 on koestettu ([hankintalista](../procurement.md#pois-jäävät-osat-voi-myydä)).
- **Ei tarvita:** BPV-F1, Parkerin Ø50-imuliitin, 8×32×36-uritettu napa eikä FXDC-reitin
  2/2-magneettiventtiili, kuristin ja virtauksensäätöventtiili ([arkisto](archive/p2-fxdc-ls-unloading.md)).
- **Säädöt:** pumpun paineenrajoitin 120 → 250 bar pumpun säätöruuvista; PVG 32:n pumppumoduulin
  paineenrajoitin on kilven mukaan noin 280 bar ja toimii varaventtiilinä; kotelo täytetään öljyllä
  ennen ensimmäistä käynnistystä.

## Asennusjärjestys

> Lisätty 2026-10-25, päivitetty 2026-11-03 PVG 32:lle [arvio]. Pätevän henkilön pitää tarkistaa
> kannake, LS-kytkentä ja ohjauslogiikka ennen rakentamista.

1. **Pumpun tarkistus ennen asennusta.** Akselitiivisteen ympärillä ei saa olla öljyä, ja
   akselin pitää pyöriä käsin tasaisesti. Ulkoiset O-renkaat vaihdetaan liitäntöjä tehtäessä.
   Hydrauliikkakorjaamon koeajo kannattaa (ks. [Tiivistesarja](#tiivistesarja)).
2. **Kannake ja kytkin.** Kannake 10 mm:n teräslevystä laserleikkaamalla ja hitsaamalla SAE C
   -reikäkuviolle ja noin 36 kg:n pumpulle **⚠ tarkista paino**. HRC 150 (päätös 2026-10-27): navat
   ja Taper Lock 2012 -holkit 48 mm (PTO) ja 1 1/4" (pumppu) sekä elastinen välikappale. Linjaus
   kytkimen sallimiin rajoihin ([current-system §0](../current-system.md)) ja suojakotelo
   pyörivälle kytkimelle. Laipan mitat ks. [tekniset tiedot](#tekniset-tiedot); tarkista mitat
   pumpusta ennen leikkausta. Keskitysreikä **Ø127**, ei Ø125 (Eatonin oma kannake:
   Ø127,05–127,15). Mallina voi käyttää [FB-C4-10:n mittoja](#eatonin-jalkakannake-fb-c4-10).
   Kohdistus ks. [Pumpun kohdistus](#pumpun-kohdistus).
3. **Imulinja.** 50 mm:n letku 2":n SAE code 61 -laipalla pumpun imuaukkoon (2" = 50,8 mm, ei
   supistusta); palloventtiili säilyy linjassa. Säiliön päässä: hitsattava muhvi →
   90°:n kulma → palloventtiili → letkukara [omistaja 2026-10-28], ks. [hankintalista](../procurement.md).
4. **Kotelovuoto.** Ylimmästä vuotoportista oma letku (vähintään noin 1/2") säiliöön öljypinnan
   alle. **Ei yhteiseen paluulinjaan.**
5. **Painelinja.** Pumpun 1":n SAE-laipasta 3/4":n letku PVG 32:n P-porttiin (G 3/4). VPR3, OD15,
   CETOP-pohjalaatta, BAV-713 ja VMP irrotetaan.
6. **LS-linja.** 1/4":n letku PVG 32:n LS-portista (G 1/4) pumpun LS-porttiin (9/16-18 UNF).
7. **Sähköt ja ohjaus:** PVE:iden 24 V:n syöttö hätäseisreleen kautta; keulapotkurin PVEH
   joystickilla ja vinssin PVEO kytkimillä, ks. [bow-thruster-control](bow-thruster-control.md).
8. **Öljy.** Järjestelmä huuhdellaan ja täytetään HVLP 32:lla ([päätös 2026-10-23](../../decisions.md));
   käyttöönoton huuhteluun käytetään vanhaa öljyä (päätös 2026-10-27). **Pumpun kotelo täytetään
   öljyllä ennen ensimmäistä käynnistystä.** Imulinjan palloventtiili auki ennen käynnistystä.
   Täyttö- ja ilmausjärjestys: [commissioning](../commissioning.md).
9. **Käyttöönotto ja säädöt** mittarilla 2G1, ks. [seuraava luku](#säätö-käyttöönotossa-ilman-virtausmittaria).
   Pumpun paineenrajoittimen tehdasasetus on 120 bar, joten se nostetaan 250 bariin ennen
   keulapotkurin täyttä käyttöä.

## Säätö käyttöönotossa ilman virtausmittaria

> Lisätty 2026-10-25, päivitetty 2026-11-03 PVG 32:lle [arvio]. Pätevän henkilön pitää hyväksyä
> säätöjärjestys ja -arvot.

Säädöt tehdään painemittarilla **2G1**, joka on PVG 32:n pumppumoduulin M-portissa
([schematic](../schematic.md), [pressure-monitoring](pressure-monitoring.md)).

| Säätö | Miten | Mittari |
|---|---|---|
| **Valmiustila (LS-paine-ero, noin 20 bar)** | Kaikki PVG:n karat keskellä: 2G1 näyttää valmiustilan paineen. Tehdasasetus; säädetään vain, jos lukema poikkeaa selvästi. | 2G1 |
| **Pumpun paineenrajoitin 120 → 250 bar** | Ohjataan varalohkoa (4 tai 5), jonka A- ja B-portit on tulpattu: LS saa täyden paineen ilman virtausta, ja pumppu nousee asetuspaineeseensa. Säädetään pumpun säätöruuvista. Jakso pidetään lyhyenä [arvio]. | 2G1 |
| **PVG 32:n pumppumoduulin paineenrajoitin (noin 280 bar)** | Kilven mukaan tehdasasetus noin 280 bar; ei säädetä. Asetuksen tarkistus vaatii pumpun hetkellistä nostoa sen yläpuolelle, joten se tehdään korjaamon koepenkillä tai **pätevä henkilö tekee sen**. | 2G1 |
| **Keulapotkurin virtaus** | Keulapotkuria ajetaan täydellä ohjauksella, ja 2G1:n lukema muunnetaan virtaukseksi Sleipnerin taulukolla (alla). Lohkon virtaus riippuu karan koosta (tavoite 40 l/min:n kara, **⚠ tarkista nykyinen kara**). | 2G1 |

**Painemittari toimii virtausmittarina,** koska keulapotkurin moottorin paine ja virtaus kulkevat
yhdessä: potkurin momentti kasvaa kierrosnopeuden neliössä. Sleipnerin taulukko U11:lle
[datalehti Side-Power SH Series v1.0.0 2017]:

| Paine moottorilla | Virtaus | Työntövoima |
|---|---|---|
| 158 bar | 26,2 l/min | 60 % |
| 211 bar | 30,2 l/min | 80 % |
| 264 bar | 33,8 l/min | 100 % |

- 250 barissa moottori ottaa arviolta noin 33 l/min (interpoloitu) [laskelma].
- 2G1 näyttää paineen pumppumoduulissa; moottorilla paine on PVG 32:n peruslohkon (kompensaattori
  ja kara) ja letkujen häviön verran pienempi **⚠ häviö ei tiedossa** (ohjeen 520L0344 s. 37
  käyrät ovat kuvina).
- **Ankkurivinssin** nopeus tarkistetaan sekuntikellolla ketjun nopeudesta, kun vinssi on kytketty.
- **Varmistus tarvittaessa:** virtauksen voi mitata ämpärillä ja sekuntikellolla vapaasta
  paluuletkusta (34 l/min täyttää 20 l:n astian noin 35 sekunnissa). Letku pitää kiinnittää
  tukevasti ja tehdä matalalla paineella; tätä ei yleensä tarvita.

## Vikatilat

> Päivitetty 2026-11-03 PVG 32:lle [arvio]. Keulapotkurin ja vinssin ohjauksen vikatilat:
> [aux-circuit-ls-clean-sheet](aux-circuit-ls-clean-sheet.md), [bow-thruster-control](bow-thruster-control.md).

- **Sähkökatko tai hätäseis:** PVE:t menettävät virran, jouset palauttavat karat keskelle, LS on
  yhteydessä säiliöön ja pumppu menee valmiustilaan. Keulapotkuri pysähtyy ja pyörii vapaasti.
  Tilanne on turvallinen. (Karojen paluu keskelle todettu käsin 2026-11-03.)
- **LS-letku irtoaa tai katkeaa:** pumpun LS-portti on yhteydessä ilmaan tai pilssiin, joten pumppu
  jää valmiustilaan ja kuormat eivät saa painetta. Öljyä vuotaa vähän [arvio].
- **Kara jumittuu auki:** kuorma jatkaa liikettä; hätäseis ei auta, jos kara on mekaanisesti jumissa.
  Kara palautetaan käsivivulla tai kone sammutetaan. PVEH:n vikavalvonta antaa hälytyksen.
- **Pumpun säädin jumittuu täydelle tuotolle:** PVG 32:n pumppumoduulin paineenrajoitin (noin
  280 bar) rajaa paineen, ja koko tuotto menee sen yli lämmöksi. Öljyn lämpötila- ja paineanturi
  havaitsevat tämän.
- **Ankkurivinssi ja sähkökatko:** kara palaa keskelle ja vinssi pysähtyy. Ankkurin pidon hoitaa
  vinssin jarru tai jarruventtiili, ei pumppu.
- **Kotelovuotolinja tukkeutuu:** akselitiiviste voi vaurioitua. Linja viedään omana letkunaan
  säiliöön, ei yhteiseen paluulinjaan.

## Paluusuodattimen vaihto: OMTF171F10NA1

Omistajan ehdotus [omistaja 2026-10-26]: nykyisen OMTF112C10NA2:n tilalle saman sarjan
suurempi OMTF171F10NA1 lasikuituelementillä. Tiedot ovat jälleenmyyjien sivuilta (hakutuloksista;
sivuja tai OMT:n luetteloa ei saatu auki 2026-10-26), ks. [datasheets](../../datasheets/README.md).

| | Nykyinen OMTF112C10NA2 | OMTF112F10NA2 (vertailu) | **Ehdokas OMTF171F10NA1** |
|---|---|---|---|
| Elementti | selluloosa 10 µm, nominaalinen **⚠ tarkista** | lasikuitu 10 µm absoluuttinen | **lasikuitu** (epäorgaaninen kuitu) 10 µm absoluuttinen; vaihtoelementti CR171F10R |
| Virtaus, Phoenix | 100 l/min | 55 l/min | **157 l/min** |
| Virtaus, Oudshoorn | 150 l/min | 71–80 l/min (sivulla kaksi arvoa) | **200 l/min** |
| Liitäntä | 1" BSP | 1" BSP | **1 1/4" BSP** |
| Kannen reikä | Ø 86 mm | Ø 86 mm | **Ø 129 mm** |
| Upotussyvyys säiliöön | 150 mm | 150 mm | **244 mm** |
| Ohitusventtiili | 1,7 bar (Phoenix) / 3 bar (Oudshoorn) | sama | 1,7 bar (Phoenix) / 3 bar (Oudshoorn) **⚠ tarkista** |
| Pulttijako, pulttien määrä ja koko | **⚠ ei tiedossa** | sama | **⚠ ei tiedossa** |
| Korkeus kannen yläpuolella | **⚠ ei tiedossa** | sama | **⚠ ei tiedossa** |
| Hinta | noin 29 £ (Phoenix) | – | **84,70 £ ALV:n kanssa** (Phoenix 2026-10-26); elementin hinta **⚠ ei tiedossa** |

Jälleenmyyjien virtausarvot eroavat toisistaan, mutta ero on johdonmukainen (Phoenixin arvot noin
65–75 % Oudshoornin arvoista); erot johtuvat todennäköisesti eri painehäviö- tai
viskositeettioletuksista [arvio]. Vertailussa käytetään Phoenixin pienempiä arvoja.

**Virtaus riittää reilusti.** Suodattimen läpi kulkee apupiirin noin 33–38 l/min ja P1:n paluu
14–37 l/min, yhteensä enintään noin 75 l/min 1800 rpm:llä [laskelma, luvut tästä dokumentista ja
arkistoitu [p2-pump-options](archive/p2-pump-options.md)]. OMTF171F10NA1:llä marginaali on noin kaksinkertainen
(157 l/min), mikä on hyödyllistä kylmäkäynnistyksessä, kun öljy on paksua ja ohitusventtiili
avautuu helpommin [arvio]. Saman runkokoon lasikuituversio OMTF112F10NA2 (55 l/min) olisi liian
pieni, joten **runkokoon suurentaminen on perusteltu**.

**Paluulinja:** yhteinen paluulinja on 3/4" (myös EC100:n öljyliitännät ovat 3/4" BSP,
[oil-cooling](oil-cooling.md)), joten linjaa ei tarvitse suurentaa koko matkalta: riittää
supistus 3/4" → 1 1/4" BSP suodattimen liittimellä [arvio]. 75 l/min:n virtauksella 3/4":n
letkussa (sisähalkaisija noin 19 mm) nopeus on noin 4,4 m/s [laskelma], yli paluulinjan tavallisen
suositusarvon (noin 2–3 m/s) [yleistieto]; lyhyellä (< 0,5 m) linjalla painehäviö on silti pieni (ks.
[current-system §3](../current-system.md)). Jos paluulinja kootaan uudelleen jäähdyttimen kanssa,
1":n letku jäähdyttimeltä suodattimelle on halpa parannus [arvio].

**Säiliön kansi ja syvyys (mitattava veneellä):**

- **Reikä:** Ø 86 → Ø 129 mm eli säde kasvaa 21,5 mm. Avarrus onnistuu esim. reikäsahalla tai
  plasmaleikkurilla; vanhat pulttireiät eivät todennäköisesti osu uuteen laippaan, joten uudet
  reiät porataan ja kierteytetään tai tehdään läpipultein. Pulttijakoa ei löytynyt; sen saa OMT:n
  luettelosta, jälleenmyyjien STEP-tiedostoista tai suoraan suodattimen rungosta mittaamalla.
  Vanhat reiät jäävät mahdollisesti laipan tiivisteen alle tai tulpataan.
- **Tila kannella:** uuden laipan ulkohalkaisija **⚠ ei tiedossa** (selvästi yli 129 mm). Tarkista,
  ettei se osu virtauksensäätöventtiileihin, täyttö- ja huohotinkorkkiin tai kannakkeisiin, ja että
  painemittari saadaan samalla luettavampaan suuntaan ([current-system §4](../current-system.md)).
- **Upotussyvyys 244 mm** (nykyinen 150 mm): suodattimen alapään pitää olla öljypinnan alla myös
  pienimmällä öljymäärällä (muuten paluuöljy vaahtoaa ja sekoittaa ilmaa), mutta se ei saa osua
  pohjaan tai väliseinään, eikä paluuvirta saa suuntautua suoraan imu-ulosottoihin (P2:n 50 mm,
  P1:n 32 mm). **Säiliön syvyys kannesta pohjaan 365 mm** [omistaja 2026-10-27]. Suodattimen alapää jää
  siis noin 120 mm pohjan yläpuolelle, eli pohjaan se ei osu. Öljypinnan pitää pienimmälläkin
  öljymäärällä olla selvästi yli 120 mm pohjasta. Jos 100 litraa vastaa koko 365 mm:n syvyyttä
  (suora säiliö), 1 cm öljyä on noin 2,7 l, ja 80 litran täytöllä pinta on noin 290 mm pohjasta
  [laskelma, arvio]. Upotukselle jää silloin noin 170 mm, ja pienemmälläkin öljymäärällä (esim.
  60 l, noin 220 mm) noin 100 mm. **Syvyyden puolesta OMTF171 sopii** [arvio]. Tarkista vielä
  öljypinnan todellinen korkeus ja se, ettei suodattimen alapää suuntaa paluuvirtaa imu-ulosottoihin
  tai osu väliseinään.
- **Kannen paksuus ja jäykkyys** suuremman reiän ympärillä **⚠ tarkista** (säiliön tyyppi A/B/C
  ei ole tiedossa).

**Muut vaikutukset:** ohitusventtiilin asetus (1,7 tai 3 bar) lisää paluulinjan vastapainetta
enintään saman verran; orbitrolin T-linjan 25 barin raja ei ole vaarassa. U11:n vuotolinja
tehdään uusiksi suoraan säiliöön [omistaja 2026-10-27], joten vastapaine ei vaikuta sen koteloon.

**Suositus:** OMTF171F10NA1 sopii, jos säiliön mitat sallivat. Halvempaa saman rungon
vaihtoehtoa ei ole: OMTF112:n lasikuituelementti on liian pieni Vegan virralle. Jos kannessa ei ole
tilaa, ks. [linjasuodatin](#vaihtoehto-linjasuodatin-paluulinjaan-nykyinen-suodatin-jää).

### Vaihtoehto: linjasuodatin paluulinjaan, nykyinen suodatin jää

Omistajan huomio [omistaja 2026-10-26]: kannessa ei välttämättä ole tilaa isommalle suodattimelle,
ja uusi kansi pitäisi luultavasti teettää laserleikattuna. Vaihtoehtona nykyinen OMTF112C10NA2 jää
paikalleen, ja yhteiseen paluulinjaan lisätään linjamallinen lasikuitusuodatin. Malli ja hinta
**⚠ valitsematta**; luvut ovat arvioita.

**Paikka:** yhteiseen paluulinjaan jäähdyttimen (EC100) jälkeen ja ennen kannen suodatinta:

```
apupiirin paluu ─┐
                 ├─ EC100 (+ ohitus 3–4 bar) ─ UUSI linjasuodatin 10 µm lasikuitu ─ OMTF112C10NA2 ─ säiliö
orbitrolin T ────┘
U11:n ja PVH57:n vuotolinjat ─────────────────────────────────────────────────────────────── suoraan säiliöön
```

- **P1:n paluu kulkee aina uuden suodattimen läpi,** kun kone käy (vanhalla 16,6 cm³:n P1:llä 14–37 l/min, uudella 20 cm³:n P1:llä noin 16–55 l/min [laskelma 2026-11-13],
  [p1-steering-pump](p1-steering-pump.md)). Se puhdistaa säiliön öljyä jatkuvasti, vaikka PVH57
  olisi valmiustilassa lähes ilman virtausta [arvio].
- **Nykyinen suodatin jää toiseksi vaiheeksi** halvalla selluloosaelementillä. Siitä on hyötyä
  myös, jos linjasuodattimen ohitusventtiili aukeaa kylmällä öljyllä.
- **Vuotolinjat (U11 ja PVH57:n kotelo) suoraan säiliöön,** ei suodattimien läpi: kotelot eivät
  kestä paluulinjan vastapainetta.

**Mitoitus [arvio]:** 10 µm absoluuttinen lasikuitu, beta-arvo ilmoitettu (vähintään 200);
virtauskesto noin 100 l/min tai enemmän (yhteinen virta enintään noin 75 l/min, ks. yllä);
liitäntä 3/4"–1" BSP; sisäänrakennettu ohitusventtiili ja tukkeumaosoitin; tila elementin vaihtoon
kupin alla (tyypillisesti 10–15 cm) ja kiinnityskannake.

**Vastapaine:** kylmällä öljyllä jäähdyttimen ohitus (3–4 bar), linjasuodatin ja kannen suodatin
(ohitus 1,7 tai 3 bar) voivat nostaa paluupaineen noin 5–8 bariin [arvio]. Orbitrolin T-linjan
25 barin raja ei ole vaarassa; keulapotkurin paine-ero pienenee lämpimällä öljyllä vain noin
1 bar [arvio].

| | Uusi kanteen asennettava (OMTF171F10NA1) | Linjasuodatin, nykyinen jää |
|---|---|---|
| Säiliön kansi | reikä Ø 86 → Ø 129 mm, uudet pulttireiät; kansi ehkä uusittava (laserleikkaus) | ei muutoksia |
| Upotussyvyys | 244 mm; säiliön syvyys 365 mm riittää [arvio] | ennallaan (150 mm) |
| Virtauskesto | 157 l/min (Phoenix) | valitaan noin 100 l/min tai enemmän |
| Suodatusvaiheita | yksi | kaksi (lasikuitu + nykyinen) |
| Paluulinjan vastapaine | pienempi | hieman suurempi (yksi suodatin lisää) |
| Tila | kannella | paluulinjan varrella, kannake ja tila elementin vaihtoon |
| Hinta | 84,70 £ + mahdollinen uusi kansi **⚠ ei tiedossa** | suodatin **⚠ ei tiedossa** (arviolta 100–250 €) + liittimet |
| Huolto | yksi elementti | kaksi elementtiä |

**Suositus [arvio]:** jos kanteen mahtuu Ø 129 mm:n reikä ja 244 mm:n upotus ilman uutta kantta,
OMTF171F10NA1 on yksinkertaisempi (yksi suodatin, pienempi vastapaine). Jos kansi pitäisi
uusia, linjasuodatin on todennäköisesti halvempi ja nopeampi. Kumpikin valinta ratkeaa veneellä
tehtävillä mittauksilla (ks. avoimet kysymykset).

### Riittääkö nykyinen paperisuodatin?

Vaatimus riippuu pumpusta [luettelot, ks. [p2-pump-options](archive/p2-pump-options.md) ja
[Tekniset tiedot](#tekniset-tiedot)]:

| Pumppu | Puhtausvaatimus (ISO 4406) | Nykyinen OMTF112C10NA2 (selluloosa 10 µm nominaalinen) |
|---|---|---|
| F1-61 (arkistoitu vaihtoehto, vertailuksi) | 20/18/13 [Parker MSG30-8200 s. 80] | todennäköisesti olisi riittänyt [arvio] |
| **PVH57 (päätetty), 250 bar** | 16/14/12 [Eaton s. 31] | **ei riitä** [arvio]: vaatimus on noin 2–3 luokkaa tiukempi (jokainen luokka kaksinkertaistaa hiukkasmäärän) |

**Yleiset puhtausohjeet** (laadittu alun perin F1-61:lle, pätevät myös PVH57:llä lasikuituelementin lisäksi) [arvio]:

- järjestelmä huuhdellaan ja uusi HVLP 32 lisätään suodattimen kautta (uusi öljy ei tynnyristä
  ole tavallisesti edes luokassa 20/18/13 [yleistieto]),
- huohotinkorkki vaihdetaan suodattavaan (esim. 3 µm), koska suurin osa liasta tulee säiliöön
  ilman mukana [yleistieto],
- elementti vaihdetaan käyttöönoton jälkeen (kokoamisessa syntynyt lika) ja sitten painemittarin
  mukaan,
- öljystä otetaan näyte hiukkaslaskentaan (ISO 4406) muutaman kymmenen käyttötunnin jälkeen;
  hinta **⚠ ei tiedossa**. Näyte kertoo varmasti, riittääkö suodatin.

Vegan käyttö keventää vaatimusta: P2 on suurimman osan ajasta valmiustilassa matalalla paineella,
ja suurpaineinen käyttö (keulapotkuri, vinssi) on lyhytaikaista. Se ei kuitenkaan muuta
valmistajan vaatimusta [arvio].

**Auttaako tiheämpi elementin vaihto (esim. 100 h välein)?** Ei puhtausluokkaan [arvio,
yleistieto]. Paperielementti ei ole ongelma siksi, että se kuluisi, vaan siksi, että se päästää läpi
suuren osan 10 µm:n ja sitä pienemmistä hiukkasista jo uutena: nominaalisen selluloosaelementin
erotusaste (beta-arvo) 10 µm:llä on tyypillisesti vain noin 2 (noin puolet hiukkasista jää
kiinni yhdellä läpikululla), lasikuituelementin 200 tai enemmän (yli 99,5 %) [yleistieto].
PVH57:n vaatimus koskee nimenomaan pieniä, 4 ja 6 µm:n hiukkasia (luvut 16 ja 14), joita
paperielementti juuri päästää läpi. Öljyn puhtaus asettuu tasolle, jonka määräävät elementin
erotusaste ja säiliöön tulevan lian määrä, ei vaihtoväli. Uusi paperielementti suodattaa jopa
hieman huonommin kuin osittain likaantunut [yleistieto].

Vaihtoväli ratkaisee vain sen, ettei elementti tukkeudu: tukkeutunut elementti avaa
ohitusventtiilin, ja silloin öljy kulkee kokonaan suodattamatta. Lisäksi vesi ja kuuma öljy
heikentävät selluloosaa. **Suositus:** vaihto ensimmäisten käyttötuntien jälkeen, sitten
painemittarin (tai tukkeumaosoittimen) mukaan ja vähintään kerran vuodessa [arvio]. Vegan kone
käy alle 1000 h vuodessa ([vessel](../../vessel/README.md), [omistaja 2026-10-23]), joten 100 tunnin
väli tarkoittaisi enimmillään noin 10 elementtiä vuodessa ilman puhtaushyötyä [laskelma].

**PVH57:n kanssa** halvin välivaihe olisi lasikuituelementti nykyiseen runkoon, jos se sopii
(`F10`-elementti CR112F10R samaan runkoon **⚠ tarkista**). Elementin virta 55 l/min (Phoenix)
tai 71–80 l/min (Oudshoorn) jää kuitenkin tiukaksi: tyhjäkäynnillä suodattimen läpi kulkee noin
35 + 16,5 ≈ 52 l/min ja kylmällä öljyllä painehäviö kasvaa [laskelma]. Siksi
suositus on OMTF171F10NA1 tai [linjasuodatin](#vaihtoehto-linjasuodatin-paluulinjaan-nykyinen-suodatin-jää)
nykyisen rinnalle.

## Avoimet kysymykset

- [x] Myyjältä: pyöriikö akseli tasaisesti (pyörii ilman ääniä), säilytys (lämmin talli), onko sisällä öljyä ja ruostetta (öljyt sisällä, ei ruostetta) [myyjä 2026-10-25]
- [x] ~~Myyjältä: alkuperä, varastointiaika, kunnostettu vai ei, onko säädin koskematon~~ ei kysytä enempää [omistaja 2026-10-25]; tarkistetaan paikan päällä ja koeajossa (säätimen asetus mitataan käyttöönotossa)
- [ ] Valmistusvuosi (sarjanumero kilvestä; myyjältä ei kysytä, Danfossilta voi kysyä tarvittaessa)
- [ ] Tiivistesarja: sopiiko 02-102244 (vanha 02-102260) rakenteelle 10 ja yksinkertaiselle akselitiivisteelle, hinta Suomesta; vaihtoehtona pelkän akselitiivisteen ja O-renkaiden mitat
- [ ] Danfoss (Vickers): saako PVH57-mobiilia pyörittää yli 2400 rpm pienemmällä iskulla; valmiustilan häviöteho; kotelon suurin paine
- [x] PVH57:n asennusmitat: laippa, imu 2", lähtö 1", vuoto 3/4-16 UNF, LS 9/16-18 UNF [Eatonin luettelo V-PUPI-TM008-E1 s. 20–22, 2026-10-28]. M-2206-S on osaluettelo eikä sisällä mittoja.
- [ ] Pumpusta (pumppu nyt omistajilla 2026-11-01): kumpi pääportti on imu (2" = reikäväli 77,8 × 42,9 mm, 1" = 52,4 × 26,2 mm), onko ylempi vuotoportti avattu, paino
- [ ] Veneellä kannakkeen paikkaa varten: kuorikytkimen halkaisija pultinkantoineen, pituus ja etäisyys vaihteiston takapinnasta; kaukalon vasemman reunan etäisyys PTO-akselista sivusuunnassa ja pedin yläpinnan leveys sen vasemmalla puolella; pedin ainepaksuus ja ylettyykö pultteihin alta; vaihteiston vasemman kiinnitysjalan ja putkien paikka
- [ ] Pumpun paino vaa'alla (kannakkeen laskelma olettaa 36 kg) ja painopisteen paikka laipasta, esim. tasapainottamalla pyöröraudan päällä
- [ ] Pumpusta: keskitysolakkeen halkaisija työntömitalla. Koodin mukaan pitäisi olla **127,0 mm** (SAE C); 125,0 mm tarkoittaisi metristä M-laippaa. Samalla reikäneliö: 114,5 mm (SAE C) vai 113,1 mm (ISO)
- [ ] Pumpun kilvestä sarjanumero ja akselin mitat (halkaisija 1 1/4", kiilaura) kytkimen holkkien tilausta varten
- [x] Akselikytkin PVH57:lle: HRC 150 + Taper Lock 2012 -holkit (päätös 2026-10-27)
- [ ] HRC 150: valmistajan luettelosta nimellismomentti, sallitut linjausvirheet ja pituus kannakkeen suunnitteluun; F- vai H-navat asennustilan mukaan
- [ ] Taper Lock 2012 -holkit 48 mm ja 1 1/4": koodit, hinta ja kiilauran syvyys 48 mm:n holkissa (PTO-akselin kiila)
- [x] Paluusuodattimen suodatusaste vs. 16/14/12 (aiemmin 17/15/13): nykyinen OMTF112C10NA2 on 10 µm, arviolta selluloosa nominaalinen, **ei riitä** sellaisenaan [omistaja 2026-10-26]
- [x] ~~Lasikuituelementti: virtauskesto, kun P1:n paluu kulkee samasta suodattimesta~~ OMTF112F10 (55 l/min) liian pieni; ehdokas OMTF171F10NA1 (157 l/min), ks. [Paluusuodattimen vaihto](#paluusuodattimen-vaihto-omtf171f10na1)
- [ ] Sopiiko lasikuituelementti CR112F10R nykyiseen OMTF112C10NA2:n runkoon
- [ ] Öljynäytteen hiukkaslaskenta (ISO 4406) käyttöönoton jälkeen: mistä ja hinta
- [ ] OMTF171F10NA1: beta-arvo, ohitusventtiilin asetus (1,7 vai 3 bar), pulttijako ja laipan ulkohalkaisija (OMT:n luettelo tai STEP-tiedosto), elementin CR171F10R hinta
- [ ] Linjasuodatin (jos kansi ei salli OMTF171:tä): malli, beta-arvo, virtauskesto noin 100 l/min, hinta; paikka ja kannake paluulinjassa
- [ ] Omistajat: uusi kanteen asennettava suodatin vai linjasuodatin (ratkeaa kannen mittauksilla)
- [x] Säiliön syvyys kannesta pohjaan: 365 mm [omistaja 2026-10-27]
- [ ] Veneellä: öljypinnan etäisyys kannesta pienimmällä öljymäärällä, imu-ulosottojen ja mahdollisen väliseinän paikka suodattimen kohdalla, tila kannella Ø 129 mm:n reiälle ja laipalle, nykyisten pulttireikien jako
- [x] Omistajat: apupiirin venttiilikokoonpano PVH57:lle → **PVG 32** (päätös 2026-10-27; ostettu 2026-11-02)
- [ ] Danfoss: riittääkö PVH57:n noin 20 barin LS-paine-ero PVG 32:n kompensaattoreille ja PVE:iden pilottiöljylle
