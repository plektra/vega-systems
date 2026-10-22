# Apupiirin pumppu (P2) ja PTO-kytkin — vaihtoehdot

> **Tila:** Vaihtoehtoselvitys, päivitetty 2026-10-22. Ei vielä päätöstä.
> Tausta: [current-system.md §0](../current-system.md). Hinnat ovat karkeita suuntaa-antavia
> arvioita; pyydä tarjoukset ennen päätöstä.

## Yhteenveto ja alustava suositus

- **Kytkin:** Borelli **30501 tai 30502** (sarja 30500, yhteen suuntaan pyörivä PTO:n
  pyörimissuunnan mukaan), ryhmän 3 pumppulaipalla, toimittaja Salhydro. Nimellismomentti 580 Nm,
  joten paineenrajoitus voi olla 250 barissa reilulla marginaalilla. Varavaihtoehto: Flowfitin /
  Borellin 30300-kokoonpano ja paineenrajoitus noin 230 bariin. Kauko-ohjaukseen push-pull-vaijeri
  tai toimilaite ja rajakytkin.
- **Pumppu:**
  1. **Oletus: A**, ryhmän 3 hammaspyöräpumppu, **koko tyhjäkäynnin mukaan: 43 cm³ (800 rpm) …
     51 cm³ (700 rpm)**. Halvin, sopii kaikkiin nykyisiin osiin, ja kytkin poistaa suurimman
     tehottomuuden.
  2. **Kannattaa pyytää tarjous: C**, ~45–47 cm³:n vinoakselimäntäpumppu (kuorma-auton PTO-pumppu),
     mieluiten käytetty. Jos se ei maksa paljon enempää kuin A, se on hiljaisempi, häviöt ovat
     pienemmät, ja täyteen työntövoimaan voi myöhemmin päästä nostamalla paineenrajoitusta.
  3. **E harkitaan uudelleen** vain, jos keulapotkurin tai vinssin proportionaalinen ohjaus tai
     useat samanaikaiset kuormat tulevat vaatimuksiksi.
- **Ennen ostoja:** mittaa koneen todellinen tyhjäkäynti ja selvitä Salhydrolta spline-sovite
  ryhmän 3 pumpulle.

## Kiinteät reunaehdot

| Reunaehto | Arvo |
|---|---|
| Veto | Advance 300:n PTO, 1:1 ensiöakselilta, Ø48 kiila-akseli, HRC 150 -joustokytkin, kytkin, pumppu omalla runkoalustalla |
| PTO:n momenttiraja | ≈ 420 Nm (0,044 kW/rpm) |
| Koneen kierrokset keulapotkuria käytettäessä | Tyhjäkäynti, ~800 rpm (ei mitattu, voi olla 650–700); kytkin lukittu pois yli ~1000–1200 rpm:n |
| Mitoittava kuorma | Side-Power SH240: 264 bar × 33,8 l/min (100 %). Hyväksytty: ~90 % työntövoimasta. |
| Paineluokka | 250 bar (kustannuspäätös); letkut 300 bar, paineenrajoitusventtiili enintään 300 bar / 80 l/min |
| Tulevat kuormat | Ankkurivinssi (moottori olemassa, tiedot puuttuvat), 3 vapaata CETOP 3 -paikkaa |
| Imu | 32 mm, 3 m, säiliö noin 1 m imuaukon yläpuolella |

## Käyttöjakso: miksi hyötysuhteella on vähemmän väliä kuin luulisi

Kytkin irrottaa P2:n aina, kun apupiirin kuormia ei käytetä, joten pumppu pyörii vain keulapotkurin
ja ankkurivinssin käytön aikana. Yleensä se tarkoittaa lyhyitä jaksoja satamassa.

Arvioitu lämpökuorma keulapotkurin käytön aikana (46 cm³:n hammaspyöräpumppu, 800 rpm, 250 bar,
öljy 40 °C):

| Kohde | Arvo |
|---|---|
| Akseliteho sisään | ~17 kW |
| Keulapotkurimoottorin teho | ~11 kW |
| Lämpö öljyyn | **~6 kW** (pumppu, venttiilit, letkut, ~2 l/min paineenrajoituksen yli) |
| Öljyn lämpeneminen, 80 l, ei jäähdytintä | ~2,7 K jokaista jatkuvan käytön minuuttia kohden |

Tavallinen manööveri on 1–2 minuuttia ajoittaista käyttöä, mikä nostaa lämpötilaa noin 3–5 K. Se on
harmitonta. Yli 5 minuutin yhtäjaksoinen käyttö nostaa yli 13 K, ja Side-Power-moottorilla on joka
tapauksessa omat käyttöjaksorajansa. **Lämpö ei ole syy luopua vakiotilavuuspumpusta, kun
kuormana on vain keulapotkuri.** Se voi olla syy, jos ankkurivinssi on pitkään käytössä, tai jos
kuormia käytetään ilman kytkintä.

## Pumppuvaihtoehdot

### A. Ulkohammaspyöräpumppu, vakiotilavuus (perusratkaisu)

Vuoden 2017 ratkaisu, suurennettuna 1:1-PTO:lle.

- **Plussat:** halvin (noin 200–500 €). Kestävä ja sietää likaisempaa öljyä. Yksinkertainen ja helppo
  hankkia Suomesta (samaa tyyppiä kuin Salami-pumput). Toimii nykyisen VPR3:n,
  2/2-vapaakiertoventtiilin ja CETOP-pohjalaatan kanssa sellaisenaan.
- **Miinukset:** tuotto sidottu kierroksiin, ylimäärä kuristetaan tai menee paineenrajoituksen yli.
  Kokonaishyötysuhde noin 80–85 %. Äänekkäämpi kuin mäntäpumput. Ryhmän 3 pumput ovat tyypillisesti
  250 bar jatkuva / 280–300 bar huippu, joten 250 barin luokan yli ei ole varaa.
- **Sopivuus:** vastaa kustannustietoista linjaa. Kytkin hoitaa suurimman heikkouden eli hukkavirtauksen
  ajon aikana.

### B. Pienempi hammaspyöräpumppu (~37 cm³) ja korotettu "keulapotkurityhjäkäynti" ~1000 rpm

- **Plussat:** halvempi ja pienempi pumppu, vähemmän hukkavirtausta, jos kytkin on päällä
  korkeammilla kierroksilla. Pienempi momentti (~172 Nm).
- **Miinukset:** jonkun pitää nostaa kierroksia ennen keulapotkurin käyttöä. Unohtaminen antaa noin
  25 % vähemmän virtausta, eli heikomman työntövoiman juuri manööverissä. Korkeammat kierrokset
  satamassa ovat myös äänekkäämpiä, ja potkuri työntää enemmän, jos vaihde on päällä.
- **Sopivuus:** kannattaa vain automaattisella kierrosten nostolla, esim. keulapotkurin
  aktiivisignaali koneen kaasulle. Selvitä, onko 3126B:n elektroniikassa sopiva sisääntulo.
  **⚠ Tarkista.**

### C. Vinoakselimäntäpumppu, vakiotilavuus (kuorma-auton PTO-pumppu)

Tyypillisiä merkkejä: Parker F1/F2, Sunfab SC, Danfoss/Hydro Leduc ym., kokoluokka noin 40–47 cm³.

- **Plussat:** hyötysuhde noin 90–95 %, hiljainen, kompakti, tehty PTO-käyttöön. Paineluokka noin
  **350–400 bar**, joten paineenrajoitus voisi olla 265–280 bar ja työntövoima ~100 % ilman että
  pumppu rasittuu. Paljon käytettyjä tarjolla kuorma-auto- ja nosturipuolelta. 47 cm³ 280 barilla on
  noin 230 Nm, mikä sopii PTO:lle.
- **Miinukset:** kalliimpi kuin hammaspyöräpumppu (noin 700–1500 € uutena). Vaatii puhtaampaa öljyä
  (tavoite noin ISO 4406 18/16/13). Laippa on yleensä kuorma-autojen ISO 7653 -mallia, joten
  runkoalustalle tarvitaan sovitelevy. Edelleen vakiotilavuus, joten tuotto kierrosten suhteen
  käyttäytyy kuten A:ssa.
- **Ennen paineen nostoa tarkista:** CETOP-venttiilien P/A/B-arvot, BAV-713:n arvot ja Side-Power-moottorin
  suurin paine. Letkut (300 bar) riittävät.
- **Sopivuus:** paras päivitys, jos halutaan täysi työntövoima ja pienemmät häviöt muuttamatta piiriä.

### D. Säätötilavuuksinen aksiaalimäntäpumppu, painekompensoitu (PC)

- **Plussat:** pienentää tilavuuttaan niin, että tuottaa vain käytetyn virtauksen. Mitään ei mene
  paineenrajoituksen yli, eikä virtauksensäätöventtiilissä synny kuristushäviötä. VPR3 voisi
  jäädä tarpeettomaksi.
- **Miinukset:** noin 1500–3000 €. Ilman virtaustarvetta pumppu on silti täydessä säätöpaineessa
  (250 bar), joten vuotolinja vuotaa ja pumppu lämpenee tyhjäkäynnillä. Kytkin tarvitaan edelleen.
  Vaatii vuotolinjan säiliöön ja puhtaampaa öljyä. Isompi ja painavampi.
- **Sopivuus:** heikko tällä käyttöjaksolla. Säästöt syntyvät lähinnä pitkissä käyttöjaksoissa.

### E. Kuormantunteva (LS) säätöpumppu ja proportionaaliset LS-venttiilit (esim. lohkoventtiili)

- **Plussat:** monipuolisin järjestelmä. Pumppu toimii noin 20–30 bar suurimman kuormapaineen
  yläpuolella ja noin 20–30 barissa, kun mitään ei käytetä. Keulapotkurin ja vinssin
  **proportionaalinen** ohjaus. Virtauksen jako, kun useita kuormia on käytössä yhtä aikaa.
  Laajennettavissa daavittiin ym. Riittävän tehokas toimimaan ilman kytkintä, vaikka kytkin on silti
  järkevä.
- **Miinukset:** kallein. Pumppu ja LS-venttiilipaketti noin 3000–6000 € tai enemmän. **Korvaa
  nykyisen CETOP-pohjalaatan, BAV-713:n, VPR3:n ja 2/2-venttiilin.** Vaatii LS-signaalilinjan,
  puhtaamman öljyn ja vaativamman käyttöönoton. SH240:n ohjaus on nyt on/off; proportionaalinen
  työntövoima vaatii oman proportionaaliventtiilin ja ohjaimen.
- **Sopivuus:** harkitaan vain, jos proportionaalinen ohjaus tai monet samanaikaiset kuormat tulevat
  tavoitteiksi. Se on laajuuden muutos, ei pelkkä pumpun vaihto.

### F. Tandem-hammaspyöräpumppu (esim. 25 + 20 cm³), toinen osa vapaakierrolla

- **Plussat:** molemmat osat syöttävät keulapotkuria tyhjäkäynnillä. Toinen osa voi syöttää vinssiä
  omana piirinään tai kierrättää matalalla paineella säiliöön. Halvat osat.
- **Miinukset:** enemmän venttiileitä ja putkitusta. Kytkin hoitaa jo suurimman osan
  hyötysuhdeedusta. Pidempi pumppukokonaisuus.
- **Sopivuus:** kiinnostava vain, jos vinssi tarvitsee oman virtauksensa keulapotkurin käydessä.

### Ei toteuttamiskelpoinen: sähköinen voimayksikkö keulapotkurille

Noin 15 kW hydraulista tehoa on noin 750 A 24 voltilla. Se vaatisi oman AC-generaattorin tai erittäin
suuren akuston. Hydraulinen PTO-veto on syy, miksi SH240 valittiin. (Pieni sähköpumppu on silti
järkevä **ohjauksen varajärjestelmänä**, noin 2,5 kW, kuten 2017 suunniteltiin.)

## Herkkyys tyhjäkäyntikierroksille

800 rpm:n tyhjäkäynti on vuoden 2018 blogista. Verkkolähteiden mukaan 3126B:n merikäytön
tyhjäkäynti voi olla noin **650–700 rpm**, ja se on ohjelmoitavissa moottorinohjaimeen. Ks.
[alustiedot](../../vessel/README.md#tyhjäkäyntikierrokset). Keulapotkurin työntövoima 250 barin
paineenrajoituksella, lämmin öljy:

| Tyhjäkäynti | 43 cm³ | 46 cm³ | 51 cm³ | 60 cm³ |
|---|---|---|---|---|
| 600 rpm | ~49 % | ~56 % | ~69 % | ~88 % |
| 650 rpm | ~58 % | ~66 % | ~81 % | ~88 % |
| 700 rpm | ~67 % | ~77 % | **~88 %** | ~88 % |
| 750 rpm | ~77 % | **~88 %** | ~88 % | ~88 % |
| 800 rpm | **~88 %** | ~88 % | ~88 % | ~88 % |

**Jos tyhjäkäynti on noin 700 rpm, 43 cm³:n pumppu antaa vain noin kaksi kolmasosaa
työntövoimasta.** 51 cm³:n pumppu riittää 700 rpm:iin asti. Se tarvitsee 250 barilla noin 225 Nm,
mikä sulkee pois 185 Nm:n Borelli/Flowfit 30300:n ja puoltaa Borellin 30500:aa. VNK3-sarjassa on
51 cm³:n koko (250 bar, enintään 2800 rpm). Muut keinot: tyhjäkäynnin nosto moottorinohjaimesta tai
kierrosten nosto käsin keulapotkuria käytettäessä. **⚠ Mittaa todellinen tyhjäkäynti ennen pumpun
ostoa.**

## Paineenrajoituksen nostaminen yli 250 barin

CETOP-pohjalaatan paineenrajoitusventtiili on **enintään 300 bar ja 80 l/min**
[omistaja 2026-10-22], ja letkut ovat 300 bar, joten ne eivät estä korkeampaa asetusta.
Työntövoima-arviot 800 rpm:n tyhjäkäynnillä, lämmin öljy:

| Paineenrajoitus | 43 cm³ (31,6 l/min) | 46 cm³ (33,9 l/min) | 51 cm³ (37,5 l/min) | Momentti, 46 cm³ |
|---|---|---|---|---|
| 250 bar | ~88 % | ~88 % | ~88 % | ~203 Nm |
| 260 bar | ~88 % (virtaus rajoittaa) | ~92 % | ~92 % | ~211 Nm |
| 270 bar | ~88 % (virtaus rajoittaa) | ~95 % | ~95 % | ~220 Nm |
| 280 bar | ~88 % (virtaus rajoittaa) | ~99 % | ~99 % | ~228 Nm |

- **Korkeampi paine auttaa vain, jos tyhjäkäynnillä on enemmän virtausta.** Se tarkoittaa 46–51 cm³:n
  pumppua 43:n sijaan tai noin 900 rpm:ää keulapotkuria käytettäessä.
- **Momentti:** enintään noin 250 Nm (51 cm³, 280 bar). Se sopii Borellin 30500:lle (580 Nm) ja PTO:lle
  (420 Nm), mutta **ei** 30300:lle (185 Nm) eikä Brevinin IM1:lle (190 Nm).
- **Mikä vielä rajoittaa painetta:**
  - **Pumppu:** VNK3 ryhmä 3 (43 ja 51 cm³) on 250 bar jatkuva ja 300 bar huippu. 260–280 barin käyttö
    nojaa huippuarvoon keulapotkurin käyttöjaksoissa. Kysy, kattaako huippuarvo ajoittaisen käytön,
    tai valitse pumppu, joka on 280 bar jatkuva.
  - **Venttiilit:** BAV-713 ja CETOP-pohjalaatta. CETOP 3 -osat ovat usein 315–350 bar, mutta
    **⚠ tarkista**.
  - **Keulapotkurin moottori:** Side-Power SH240:n hydraulimoottorin suurin paine. **⚠ Tarkista.**
- **80 l/min riittää.** Paineenrajoitus on VPR3:n (35 l/min) jälkeen, joten se ei koskaan näe pumpun
  koko tuottoa.

## Kytkinvaihtoehdot

### Flowfit ZZ009520: ryhmän 3 mekaaninen kytkin- ja pumppukokoonpano, 43 cm³

[Group 3 Mechanical Clutch & Pump Assembly, 43cc, 77.4 L/min](https://www.flowfitonline.com/products/group-3-mechanical-clutch-pump-assembly-43cc-77-4-l-min),
noin 526 £ + ALV (lokakuu 2026). Tiedot tuotesivulla linkitetystä Flowfitin datalehdestä
(skannattu 3-sivuinen PDF, luettu kuvina). *(sivu)*-merkityt tiedot ovat tuotesivun tiivistelmästä,
eikä niitä luettu sanatarkasti.

| Kohde | Arvo | Lähde |
|---|---|---|
| Kokoonpanon arvot | 200 bar työpaine, 30 kW, 77,4 l/min 1800 rpm:llä | *(sivu)* |
| Pumppu | VNK3, ryhmä 3, hammaspyöräpumppu, 43 cm³, eurooppalainen laippa | datalehti s. 1 |
| Pumpun paine | **250 bar nimellinen, 300 bar huippu** | datalehti s. 1 |
| Pumpun kierrosnopeus | 2000 nimellinen, 2800 max, 400 min rpm | datalehti s. 1 |
| Kytkin | Flowfit-sarja 30300, **mekaaninen, vipukäyttöinen** (OFF/ON, vivun liike ±10°) | datalehti s. 3 |
| Kytkimen arvot | **Nimellismomentti 18,5 daNm = 185 Nm**, max 2700 rpm, max 40 kW, aksiaalikuorma 160 daN | datalehti s. 3 |
| Kytkimen ensiö | **Ø28 j6 -akseli, kiila 8×7×40** (UNI 6607-69) | datalehti s. 3 |
| Kytkimen toisio | 35×31 DIN 5482 -sisähammastus (ryhmä 3) | datalehti s. 3 |
| Kytkimen voitelu | SAE 90 -vaihteistoöljy; vaihto 60–80 h jälkeen, sitten 12 kk tai 1500 h välein | *(sivu)* |
| Kytkentä | Suuntaventtiili vapaakierrolla, enintään 1800 rpm | *(sivu)* |
| Pyörimissuunta | Myötäpäivään vakiona; vastapäivään pyynnöstä. Molempiin suuntiin toimivia versioita on. | *(sivu)*, datalehti s. 3 |

| Tarkistus | Tulos |
|---|---|
| Tuotto 800 rpm:n tyhjäkäynnillä | 43 cm³ × 800 × 0,92 ≈ **31,6 l/min** (100 %:lle tarvitaan 33,8). 250 barissa virtaus- ja paineraja osuvat yhteen, noin 88 % työntövoima, sama kuin 46 cm³:llä. **Virtaus kuitenkin rajoittaa, joten paineenrajoituksen nosto ei auta.** ✅ 250 barissa |
| Pumpun paine | 250 bar nimellinen ✅ |
| Kierrosnopeudet | Koneen 2500 rpm alittaa pumpun 2800 ja kytkimen 2700 rpm ✅ |
| PTO:n momentti (420 Nm) | ✅ Reilu marginaali |
| **Kytkimen momentti 250 barissa** | 250 bar × 43 cm³ / 2π = 171 Nm teoreettisesti, **~190 Nm** 90 %:n mekaanisella hyötysuhteella. **Juuri 185 Nm:n nimellisarvon kohdalla tai hieman yli.** ⚠ |
| Kytkimen momentti 200 barissa (Flowfitin arvo) | 137–152 Nm, noin 80 % nimellisestä. Todennäköisesti syy, miksi Flowfit ilmoittaa kokoonpanolle 200 bar. |
| Joustokytkin | HRC 150, napa 48 mm (PTO) ja 28 mm (kytkin). Momentti ≤ 190 Nm. Tarkista napatyypit. |
| Ohjaus | Vipu kytkimessä, eli kytkentä vaatii käynnin konehuoneessa tai push-pull-vaijerin / toimilaitteen. Ei asentotietoa; Signal K -näyttöön tai kierroslukitukseen tarvitaan rajakytkin. |

| Paineenrajoitus | Työntövoima | Momentti | Suhteessa 185 Nm:iin |
|---|---|---|---|
| 200 bar (Flowfitin arvo) | ~70 % | 137–152 Nm | ✅ sisällä |
| 230 bar | ~81 % | 157–175 Nm | ✅ sisällä (≈ 95 %) |
| 250 bar | ~88 % | 171–190 Nm | ⚠ rajalla tai hieman yli |

### Borellin mekaaniset kytkimet (Salhydron luettelo HPFM.pdf)

Lähde: <https://files.salhydro.fi/files/PDF/HPFM.pdf>, Borellin "Mechanical couplings" -luettelo
(10 skannattua sivua, luettu kuvina). Salhydro on suomalainen jälleenmyyjä.

**Flowfitin 30300 on Borellin 30300.** Osanumerot, piirustukset ja arvot ovat samat: mekaaninen
**kynsikytkin** ("coupling with front teeth"), vipukäyttöinen, 185 Nm nimellinen. Luettelossa on myös
**isompi sarja 30500** pumppuryhmille 3,5 ja 4:

| Kohde | 30300 (Flowfitin kokoonpano) | **30500** |
|---|---|---|
| Nimellismomentti | 18,5 daNm = **185 Nm** | 58 daNm = **580 Nm** |
| Suurin kierrosnopeus | 2700 rpm | 2700 rpm |
| Suurin teho | 40 kW | 60 kW |
| Aksiaalikuorma | 160 daN | 260 daN |
| Ensiöakseli | Ø28 j6, kiila 8×7×40 | **Ø42 j6, kiila 12×8×60**, pituus 70 mm |
| Toisio | 35×31 DIN 5482 -sisähammastus | 48×44 DIN 5482 -sisähammastus |
| Pumppulaipat | Gr.2–3, Gr.2/3 Bosch, SAE A, SAE B | Gr.2, **Gr.3 (30401)**, Gr.3.5, Gr.4, **Gr.3 Bosch (30417)**, SAE A/B/C, muita |
| Koko | ~151 mm pitkä | ~226 mm pitkä, runko Ø166 |
| Versiot | 30300 molempiin suuntiin / 30301 oikea / 30302 vasen | 30500 molempiin suuntiin / 30501 oikea / 30502 vasen |

Molempien sarjojen yleisohje (luettelo s. 3, sanatarkasti): *"When coupling with hydraulic pumps we
recommend to engage and disengage the pump when the directional valve is in exhaust position at a
speed not over 1800 R.P.M. In the reversible position the max engagement and disengagement speed is
1000 R.P.M."* Eli kytkentä ja irrotus suuntaventtiilin ollessa vapaakierrolla, enintään 1800 rpm
(molempiin suuntiin toimivalla 1000 rpm). Voitelu SAE 90, vaihto 12 kk välein. Käyttölämpötila
−10…+80 °C.

| Tarkistus (30500) | Tulos |
|---|---|
| Momentti, 43–51 cm³ 250 barissa (171–225 Nm) | ✅ 580 Nm nimellinen, noin **2,6–3-kertainen** marginaali. 300 barin huiputkin (noin 230–270 Nm) mahtuvat reilusti. |
| PTO:n raja (≈ 420 Nm) | Kytkin on nyt PTO:ta vahvempi, joten **paineenrajoitusventtiili** suojaa PTO:ta. 250 bar × 51 cm³ ≈ 225 Nm, eli kunnossa. |
| Kierrosnopeus ja teho | ✅ 2700 rpm ja 60 kW, tarve 2500 rpm ja noin 18–20 kW |
| Ensiöakseli | ✅ Ø42, kiila. HRC 150 -navat 48 mm (PTO) ja 42 mm (kytkin). Tarkista napatyypit. |
| Pumpun kiinnitys | Gr.3- (30401) ja Gr.3 Bosch (30417) -laipat löytyvät. ⚠ **Toision hammastus on kuitenkin 48×44, isompi kuin ryhmän 3 pumpun akseli.** Kysy Salhydrolta tai Borellilta, mikä sovitusholkki käy laipan 30401 tai 30417 kanssa ryhmän 3 pumpulle (35×31-hammastus tai 1:8-kartio). |
| Kytkentä | Samat säännöt kuin 30300:ssa: kuormittamattomana, enintään 1800 rpm (molempiin suuntiin toimivalla 1000 rpm). Valitse **yhteen suuntaan toimiva versio** (oikea tai vasen), niin raja on 1800 rpm. Kytkentä tyhjäkäynnillä 2/2-venttiilin ollessa auki täyttää kummankin. |
| Kauko-ohjaus | Sama vipu kuin 30300:ssa; push-pull-vaijeri tai toimilaite ja rajakytkin. Vipuvoimaa ei ole selvästi ilmoitettu (piirustuksessa 631 / 472 daN, mikä ei todennäköisesti ole käsivoima); kysy. |
| Koko | Noin 75 mm pidempi kuin 30300. Tarkista tila runkoalustalla. |

**30500 ratkaisee 250 barin momenttikysymyksen.** Paineenrajoitus voi pysyä 250 barissa (noin 88 %
työntövoima) reilulla marginaalilla.

### Brevini IM1 (hydrauliikkakauppa.fi)

Lähde: <https://www.hydrauliikkakauppa.fi/wp-content/uploads/2020/09/Mekaaninen-Irrotuskytkin-40kW-IM1.pdf>,
Brevini Fluid Powerin IM1-datalehti (2 sivua, luettu kuvina). Suomalainen toimittaja.

| Kohde | Brevini IM1 | Vertailu Borelli 30300 / 30500 |
|---|---|---|
| Tyyppi | Vipukäyttöinen mekaaninen kytkin moottorin ja pumpun väliin | sama periaate |
| **Suurin momentti** | **19 daNm = 190 Nm** (*maksimi*, ei nimellisarvo) | 30300: 185 Nm *nimellinen*; 30500: 580 Nm nimellinen |
| Suurin kierrosnopeus | 2700 rpm | sama |
| **Suurin kytkentänopeus** | **420 rpm** (molempiin suuntiin 300 rpm), pumppu kuormittamattomana | 1800 rpm (molempiin suuntiin 1000) |
| Ensiöakseli | Ø28 j6, kiila A8×7×40, pituus 48 mm; säteiskuorma noin 3 kN asti | 30300 sama Ø28; 30500 Ø42 |
| Toisio | Z18 35×31 DIN 5482, ryhmän 3 hammastettu pumppu sopii suoraan | |
| Laipat | Gr.2–3, SAE A, SAE B | |
| Voitelu | 0,5 l CLP 150 (ISO VG 150), vaihto 12 kk välein | SAE 90 |
| Tilauskoodi | IM1-C-**D**/**S**/**R**-**2/3**/SA/SB (D = myötäpäivään, S = vastapäivään, R = molempiin) | |

- **Kytkentä vain alle 420 rpm:ssä, eli ei koneen käydessä.** 3126B:n tyhjäkäynti on noin 650–800 rpm.
  Pumppu pitäisi kytkeä **koneen ollessa sammutettuna** ennen käynnistystä ja irrottaa vasta
  sammutuksen jälkeen. Kytkentä satamaan tultaessa tai vinssin käyttö ankkurissa vaatisi koneen
  sammuttamisen. ❌
- **190 Nm maksimi** vs. 171–190 Nm 250 barissa on aivan rajalla, eikä painepiikeille jää varaa. ❌
- **Johtopäätös:** ei parempi kuin 30300, ja hankalampi käyttää. Breviniltä voi löytyä isompia kokoja
  samasta luettelon osasta (tiedostonimessä "40kW", sivu on osa 2.03); kysy, ja tarkista silloin myös
  kytkentänopeus.

### Sähkömagneettiset kytkimet (Flowfitin valikoima)

Lähde: Flowfitin tekninen PDF `ECPA1.pdf`, 12 sivua, skannattu ja luettu kuvina. Kolme samanrakenteista
sarjaa:

| Sarja (12 V / 24 V) | Nimellismomentti | Staattinen (max) | Dynaaminen 500 / 1000 rpm | 24 V:n kela | Hihnapyörä | Paino |
|---|---|---|---|---|---|---|
| 30901 / 30903 | 78 Nm | 125 Nm | 85 / 70 Nm | 1,26 A, 30 W | Ø153, 2 × A | 5,5 kg |
| 30929 / 30930 | 118 Nm | 140 Nm | 125 / 110 Nm | 1,26 A, 30 W | Ø153, 2 × A | 5,5 kg |
| **30990 / 30991** | **160 Nm** | **210 Nm** | **145 / 120 Nm** | 1,95 A, 47 W | Ø186, 2 × A | 8 kg |

- Toisio 35×31 DIN 5482 -sisähammastus; laipat Gr.2 Bosch, Gr.3, Gr.3 Bosch, SAE A ja SAE B. Isoimman
  sarjan 24 V:n ryhmän 3 versio on **29-30993**.
- **Kaikki arvot 20 °C:ssa.** 120 °C:ssa suorituskyky on **20 % pienempi**.
- Kytkentä 25 ms, vähintään 20 s kytkentöjen välillä. Luisto enintään 5 s (tuotesivu).
- Suurin kierrosnopeus 5000 rpm. Kaikki toimivat molempiin suuntiin.
- **Ensiö on kiilahihnapyörä (kytkimen roottori), ei akseli.** Tehty hihnavetoon kampiakselilta.

| Tarkistus | Tulos |
|---|---|
| Momentti, 43 cm³ 250 barissa (171–190 Nm) | **Yli isoimman sarjan 160 Nm:n nimellisarvon.** Kylmänä alle 210 Nm:n staattisen arvon, mutta kuumana (−20 % → 168 Nm) rajalla. **Ei parempi kuin 185 Nm:n mekaaninen kytkin.** ❌ |
| Veto PTO:n Ø48-akselilta | ❌ **Ei akseliliitäntää.** Vaatisi hihnavedon PTO:lta tai erikoissovitteen hihnapyörään. Hihnaveto toisi takaisin vuoden 2018 ongelman: kaksi A-hihnaa ei kanna noin 17 kW 800 rpm:llä. |
| Kauko-ohjaus ja lukitus | ✅ Tämä on pääetu: 24 V, noin 2 A, ohjattavissa ohjauspaikalta tai ESP32 PDM -kanavalta, helppo kierroslukitus. |

**Johtopäätös:** mikään Flowfitin sähkömagneettisista kytkimistä ei sovi tähän. Ne ovat mekaanista
30300:aa heikompia ja tehty hihnavetoon.

**Muita sähkömagneettisia vaihtoehtoja (selvittämättä):**
- **Teolliset akselilta akselille -sähkömagneettikytkimet** (esim. Warner Electric, Ogura, Kendrion/INTORQ,
  Mayr), 24 V DC, yli 250 Nm. Todennäköisesti kalliimpia kuin koko Flowfit-kokoonpano.
- **Hydraulisesti tai pneumaattisesti ohjatut monilevy-PTO-kytkimet** (meri- ja teollisuuskäyttö).
  Kestäviä ja kauko-ohjattavia solenoidiventtiilillä. Yleensä kallein vaihtoehto.

### Mekaanisen kytkimen kauko-ohjaus

Mekaaninen kytkin on löydetyistä vaihtoehdoista edullisin momenttiinsa nähden. Sitä voi ohjata
kauempaa:
- **push-pull-vaijerilla** ohjauspaikalle tai konehuoneen ovelle (halpa, kuten kaasuvaijeri);
- **24 V:n lineaaritoimilaitteella** ja **rajakytkimellä** asentotiedoksi. Se mahdollistaa ESP32 PDM
  -ohjauksen, Signal K -näytön ja kierroslukituksen (kytkentä vain alle noin 1000 rpm:n, hälytys
  jos päällä rajan yli).

## Pumppuvaihtoehtojen vertailu

| | A. Hammaspyörä 43–51 cc | B. Hammaspyörä 37 cc + kierrokset | C. Vinoakseli | D. Säätö PC | E. Kuormantunteva | F. Tandem |
|---|---|---|---|---|---|---|
| Pumpun hinta (suuntaa-antava) | € | € | €€ | €€€ | €€€€ (venttiileineen) | €–€€ |
| Muutokset piiriin | ei | kierrosohjaus | sovitelaippa; ehkä venttiilien arvot | vuotolinja; VPR3 valinnainen | uusi venttiilipaketti | lisäventtiilit |
| Työntövoima 250 barin luokassa | ~88 % | ~88 % (jos kierrokset nostetaan) | ~88 %, **~100 % 280 barissa** | ~90 % | ~90 % | ~88 % |
| Hyötysuhde käytön aikana | ~80–85 % | ~80–85 % | ~90–95 % | ~88–92 % | paras | ~80–85 % |
| Öljyn puhtausvaatimus | sietää | sietää | kohtalainen | tiukka | tiukka | sietää |
| Proportionaalinen ohjaus | ei | ei | ei | ei | **kyllä** | ei |
| Sopivuus nykyiseen linjaan | **hyvä** | kohtalainen | **hyvä** | heikko | laajuuden muutos | tilanteen mukaan |

## Avoimet kysymykset

- [ ] Koneen todellinen tyhjäkäynti (ratkaisee pumpun koon)
- [ ] Salhydro: spline-sovite 30500:n ja ryhmän 3 pumpun väliin, vipuvoima, hinta ja toimitusaika 30501/30502 + Gr.3-laippa
- [ ] PTO:n pyörimissuunta (30501 vai 30502)
- [ ] Ankkurivinssin moottorin tiedot ja odotettu käyttöaika (pitkät jaksot muuttavat lämpötilannetta)
- [ ] Side-Power SH240:n hydraulimoottorin suurin paine (jos paineenrajoitusta nostetaan)
- [ ] CETOP 3 -pohjalaatan, venttiilien ja BAV-713:n painearvot
- [ ] Hyväksyykö CAT 3126B:n elektroniikka ulkoisen kierrostenkorotussignaalin? (vaihtoehto B)
