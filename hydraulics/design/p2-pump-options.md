# Apupiirin pumppu (P2) ja PTO-kytkin — vaihtoehdot

> **Tila:** Vaihtoehtoselvitys, päivitetty 2026-10-22 (tyhjäkäynti 700 rpm). Ei vielä päätöstä.
> Tausta: [current-system.md §0](../current-system.md). Hinnat ovat karkeita suuntaa-antavia
> arvioita; pyydä tarjoukset ennen päätöstä.

## Yhteenveto ja alustava suositus

- **Kytkin:** Borelli **30501 tai 30502** (sarja 30500, yhteen suuntaan pyörivä PTO:n
  pyörimissuunnan mukaan), ryhmän 3 pumppulaipalla, toimittaja Salhydro. Nimellismomentti 580 Nm,
  joten paineenrajoitus voi olla 250 barissa reilulla marginaalilla. Varavaihtoehto: Flowfitin /
  Borellin 30300-kokoonpano ja paineenrajoitus noin 230 bariin. Kauko-ohjaukseen push-pull-vaijeri
  tai toimilaite ja rajakytkin.
- **Pumppu:**
  1. **Oletus: A**, ryhmän 3 hammaspyöräpumppu **51 cm³** (esim. VNK3-3-51, 250 bar jatkuva /
     300 bar huippu), joka antaa 700 rpm:n tyhjäkäynnillä noin 88 % työntövoimasta. Halvin, sopii
     kaikkiin nykyisiin osiin, ja kytkin poistaa suurimman tehottomuuden. 51 cm³ on VNK3-sarjan
     suurin koko, joka on 250 bar jatkuva; 60 cm³ on vain 200 bar.
  2. **Varteenotettava ehdokas: C**, vinoakselimäntäpumppu (kuorma-auton PTO- tai kippipumppu).
     **Käytetty Parker F1-061 on myynnissä 100 eurolla** (ks.
     [Ehdokas: Parker F1-061](#ehdokas-parker-f1-061-käytettynä-torifi)). 61 cm³ ja 350 bar
     jatkuva, ei vuotolinjaa: 250 barissa sama ~88 % kuin A:lla, ja 280 barissa noin 99 % työntövoima, kun venttiilien
     ja keulapotkurimoottorin painearvot on varmistettu.
  3. **E harkitaan uudelleen** vain, jos keulapotkurin tai vinssin proportionaalinen ohjaus tai
     useat samanaikaiset kuormat tulevat vaatimuksiksi.
- **Flowfitin 43 cm³:n kokoonpano ei enää sovi:** 700 rpm:llä se antaisi vain noin 67 %
  työntövoimasta, eikä sen 185 Nm:n kytkin kestä 51 cm³:n pumppua 250 barissa (~225 Nm).
- **Ennen ostoja:** vahvista tyhjäkäynti mittaamalla ja selvitä Salhydrolta spline-sovite ryhmän 3
  pumpulle.

## Kiinteät reunaehdot

| Reunaehto | Arvo |
|---|---|
| Veto | Advance 300:n PTO, 1:1 ensiöakselilta, Ø48 kiila-akseli, HRC 150 -joustokytkin, kytkin, pumppu omalla runkoalustalla |
| PTO:n momenttiraja | ≈ 420 Nm (0,044 kW/rpm) |
| Koneen kierrokset keulapotkuria käytettäessä | Tyhjäkäynti, ~700 rpm [omistaja 2026-10-22, ei mitattu]; kytkin lukittu pois yli ~1000–1200 rpm:n |
| Mitoittava kuorma | Side-Power SH240: 264 bar × 33,8 l/min (100 %). Hyväksytty: ~90 % työntövoimasta. |
| Paineluokka | 250 bar (kustannuspäätös); letkut 300 bar; paineenrajoitusventtiili Marchesini VMP 3/4": 350 bar, 90 l/min, jousi todennäköisesti 80–300 bar |
| Tulevat kuormat | Ankkurivinssi (moottori olemassa, tiedot puuttuvat), 3 vapaata CETOP 3 -paikkaa |
| Imu | 32 mm, 3 m, säiliö noin 1 m imuaukon yläpuolella |

## Käyttöjakso: miksi hyötysuhteella on vähemmän väliä kuin luulisi

Kytkin irrottaa P2:n aina, kun apupiirin kuormia ei käytetä, joten pumppu pyörii vain keulapotkurin
ja ankkurivinssin käytön aikana. Yleensä se tarkoittaa lyhyitä jaksoja satamassa.

Arvioitu lämpökuorma keulapotkurin käytön aikana (46 cm³:n hammaspyöräpumppu, 800 rpm, 250 bar,
öljy 40 °C; 51 cm³ 700 rpm:llä antaa käytännössä saman akselitehon, noin 16,5 kW):

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

**Tyhjäkäynti on omistajan mukaan noin 700 rpm** [omistaja 2026-10-22]; blogissa mainittu 800 rpm
oli yläkanttiin. Tyhjäkäynti on ohjelmoitavissa moottorinohjaimeen, ks.
[alustiedot](../../vessel/README.md#tyhjäkäyntikierrokset). Keulapotkurin työntövoima 250 barin
paineenrajoituksella, lämmin öljy:

| Tyhjäkäynti | 43 cm³ | 46 cm³ | 51 cm³ | 60 cm³ |
|---|---|---|---|---|
| 600 rpm | ~49 % | ~56 % | ~69 % | ~88 % |
| 650 rpm | ~58 % | ~66 % | ~81 % | ~88 % |
| **700 rpm (nykyinen)** | ~67 % | ~77 % | **~88 %** | ~88 % |
| 750 rpm | ~77 % | ~88 % | ~88 % | ~88 % |
| 800 rpm | ~88 % | ~88 % | ~88 % | ~88 % |

**700 rpm:n tyhjäkäynnillä 43 cm³:n pumppu antaa vain noin kaksi kolmasosaa työntövoimasta.**
51 cm³:n pumppu riittää. Se tarvitsee 250 barilla noin 225 Nm, mikä sulkee pois 185 Nm:n
Borelli/Flowfit 30300:n ja puoltaa Borellin 30500:aa. VNK3-sarjassa on 51 cm³:n koko (250 bar
jatkuva, 300 bar huippu, enintään 2800 rpm). VNK3:n 60 cm³ on vain 200 bar jatkuva, joten se ei sovi.

Muut keinot, jos halutaan pienempi pumppu: tyhjäkäynnin nosto 800 rpm:iin moottorinohjaimesta
(Caterpillar-huolto) tai kierrosten nosto käsin keulapotkuria käytettäessä. **⚠ Vahvista
tyhjäkäynti mittaamalla ennen pumpun ostoa.**

## Paineenrajoituksen nostaminen yli 250 barin

Paineenrajoitusventtiili on **Marchesini VMP 3/4"**: enintään 350 bar ja 90 l/min, jousi
todennäköisesti 80–300 bar [datalehti VMP, omistaja 2026-10-22]. Letkut ovat 300 bar, joten kumpikaan
ei estä korkeampaa asetusta (280 bar mahtuu 80–300 barin jousialueeseen).
Työntövoima-arviot **700 rpm:n tyhjäkäynnillä**, lämmin öljy:

| Paineenrajoitus | 51 cm³ (32,8 l/min) | Momentti 51 cm³ | 56 cm³ (36,1 l/min) | Momentti 56 cm³ |
|---|---|---|---|---|
| 250 bar | ~88 % | ~225 Nm | ~88 % | ~248 Nm |
| 260 bar | ~92 % | ~234 Nm | ~92 % | ~257 Nm |
| 270 bar | ~94 % (virtaus rajoittaa) | ~244 Nm | ~95 % | ~267 Nm |
| 280 bar | ~94 % (virtaus rajoittaa) | ~253 Nm | ~99 % | ~277 Nm |

- **51 cm³:n pumpulla 260 barin asetus nostaa työntövoiman noin 92 %:iin**, mutta sen yli virtaus
  loppuu. Täyteen tehoon tarvittaisiin noin 56 cm³ ja 280 bar, mikä vaatii pumpun, joka on luokiteltu
  280 bariin jatkuvasti (esim. vinoakselipumppu C).
- **Momentti:** enintään noin 280 Nm. Se sopii Borellin 30500:lle (580 Nm) ja PTO:lle (420 Nm), mutta
  **ei** 30300:lle (185 Nm) eikä Brevinin IM1:lle (190 Nm).
- **Mikä vielä rajoittaa painetta:**
  - **Pumppu:** VNK3 ryhmä 3 (43 ja 51 cm³) on 250 bar jatkuva ja 300 bar huippu. 260–280 barin käyttö
    nojaa huippuarvoon keulapotkurin käyttöjaksoissa. Kysy, kattaako huippuarvo ajoittaisen käytön,
    tai valitse pumppu, joka on 280 bar jatkuva.
  - **Venttiilit:** BAV-713 (fluiconnecto BAV-IC3-713) on 350 bar ✅. Teräksinen CETOP 3 -pohjalaatta on
    tyypillisesti 250–350 bar, painearvo **⚠ vahvista Flowfitilta**. Patruunaventtiili (350 bar) ja VMP
    (350 bar) ✅.
  - **Keulapotkurin moottori:** Side-Power SH240:n hydraulimoottorin suurin paine. **⚠ Tarkista.**
- **VMP:n 90 l/min riittää.** Paineenrajoitus on VPR3:n (35 l/min) jälkeen, joten se ei koskaan näe
  pumpun koko tuottoa.

## Ehdokas: Parker F1-061 käytettynä (tori.fi)

Ilmoitus: <https://www.tori.fi/recommerce/forsale/item/45212646>, hinta **100 €** (tarkistettu
2026-10-22). Ilmoituksen teksti: *"Hyväkuntoinen vähän käytetty mäntäpumppu. Pyörimissuunta helppo
vaihtaa. Mukaan holkki akseliin jolla helppo rakentaa veto. Parker mäntäpumppu / kippipumppu."*

**Tyyppikilpi:** `F1-061-R---000`, osanumero **3781060** [omistaja 2026-10-22, myyjältä].

### Tiedot

Lähteet: Parkerin asennus- ja käyttöönotto-ohje *HY30-8201-INST/EU, Series F1/F2/T1*
([PDF](https://pzip.ru/downloads/parker/HY30-8201-INST_EU.pdf?sku=3781060), luettu kuvina ja tekstinä)
sekä jälleenmyyjän tuotesivu osanumerolle 3781060 ([pzip.ru](https://pzip.ru/catalog/parker/3781060)).
Parkerin varsinaista F1-luetteloa ei saatu luettua.

| Kohde | Arvo | Lähde |
|---|---|---|
| Kierrostilavuus | **61 cm³/r** (F1-61) **⚠ tarkista** Parkerin luettelosta | jälleenmyyjä |
| Paine | 350 bar jatkuva (SAE) / 400 bar (ISO) | jälleenmyyjä, Parker |
| Kierrosnopeus | enintään noin 2600 rpm 350 barin jatkuvalla paineella | jälleenmyyjä (Parkerin teksti) |
| Pyörimissuunta | **R** = oikea eli myötäpäivään akselin päästä katsottuna. **Vaihdettavissa:** päätykappaleen pultit auki, päätykappale 180° käännettynä takaisin, pultit 80–100 Nm. | ohje s. 4 |
| Laippa ja akseli | **ISO-malli:** kuorma-auton ISO 7653 -laippa ja **DIN 5462 B8×32×36** -hammasakseli (8 uraa) | jälleenmyyjä |
| Vuotolinja | **Ei tarvita.** *"Fixed displacement pumps don't need an external drain line as they are internally drained."* (Erillinen ohituslinja tarvitaan vain, jos pumppuun asennetaan Parkerin BPV-ohitusventtiili.) | ohje s. 11 |
| Imuliitin | Parker suosittelee imuliittimeksi **vähintään 38 mm (1½")**, kun tuotto on enintään 60 l/min. Nopeustaulukon mukaan 32 mm:n letkussa 50 l/min on 1,0 m/s. | ohje s. 4 |
| Öljy | HLP (DIN 51524) tai biohajoavat esterit. Suositeltu viskositeetti 20–30 cSt; käytön rajat 10–400 cSt; käynnistyksessä enintään 4000 cSt. Öljyn lämpötila enintään 75 °C. | ohje s. 11 |
| Akselin voitelu | Jos voimanulosoton holkki on tiivistetty, hammasakseli rasvataan lämmönkestävällä rasvalla ennen käyttöönottoa ja säännöllisesti | ohje |
| Pienin sallittu imupaine | **⚠ ei tiedossa** (ei ohjeessa) | |

### Sopivuus Vegaan [laskelma]

Oletukset: 61 cm³, volumetrinen hyötysuhde 95 %, mekaaninen 95 %, tyhjäkäynti 700 rpm.

| Tarkistus | Arvio |
|---|---|
| Tuotto 700 rpm:llä | noin 40,6 l/min, enemmän kuin keulapotkurin 33,8 l/min ✅ |
| Työntövoima, paineenrajoitus 250 bar | noin 88 % (paine rajoittaa) |
| Työntövoima, paineenrajoitus 280 bar | **noin 99 %**; pumppu kestää tämän reilusti ✅ |
| Momentti 250 / 280 barissa | noin 255 / 286 Nm: Borelli 30500 (580 Nm) ja PTO (420 Nm) riittävät; Flowfit/Borelli 30300 (185 Nm) ei |
| Lämpö | Ylimääräiset ~7–9 l/min menevät paineenrajoituksen yli, noin 3–4 kW lisälämpöä vain keulapotkurin käytön ajan; lyhyissä jaksoissa harmitonta |
| Imulinja | Nykyinen 32 mm:n letku: noin 0,9 m/s 700 rpm:llä, mikä on Parkerin taulukon mukaan hyväksyttävää. Pumpun päähän kannattaa silti Parkerin suosittelema 38 mm:n imuliitin. 1000 rpm:llä nopeus olisi noin 1,2 m/s, joten kytkimen kierroslukitus (~1000 rpm) on tarpeen. |
| Kylmä öljy | ISO VG 46 on 5 °C:ssa noin 380 cSt, eli lähellä pumpun 400 cSt:n käyttörajaa. **HV 32 -öljy** (noin 200–250 cSt 5 °C:ssa) antaisi marginaalia. |
| Pyörimissuunta | Pumpun suunta (akselin päästä katsottuna) pitää sovittaa PTO:n suuntaan (PTO-akselin päästä katsottuna). Koska suunnan voi vaihtaa, tämä ei ole riski. **⚠ Tarkista PTO:n pyörimissuunta.** |
| Kiinnitys | ISO 7653 -laippa ja 8×32×36-hammasakseli **eivät sovi suoraan** Borellin 30500:een (toisiossa 48×44-sisähammastus ja ryhmä-/SAE-laipat). Tarvitaan sovitelaippa ja -holkki, joko Salhydrolta/Borellilta tai teetettynä. Myyjän holkki on luultavasti 8×32×36-sisähammastettu holkki, josta voi tehdä vedon. **⚠ Selvitä holkin mitat.** |

**Arvio:** pumppu sopii hyvin. 100 eurolla se kannattaa ostaa, jos kunto on hyvä (ei vuotoa
akselitiivisteestä, ei välystä akselissa). Suurin avoin asia on kiinnitys Borellin 30500
-kytkimeen.

**Kysy vielä myyjältä:** holkin mitat (hammastus, ulkohalkaisija, kiila), kunto ja miksi pumppu
irrotettiin.

## Käyttäytyminen eri kierroksilla (Parker F1-061)

Laskelma 2026-10-22 [laskelma]: Parker F1-061 (61 cm³) PTO:lla 1:1, nykyiset venttiilit (VPR3 35 l/min,
2/2-vapaakiertoventtiili, paineenrajoitus 250 bar), öljy ISO VG 46, säiliö 80 l ilman jäähdytintä.
VPR3:n oletetaan olevan kolmitieventtiili, joka ohjaa ylimäärän säiliöön lähes kuormapaineessa
(vahvistettu: Marchesini VPR3 on kolmitie-etusijaventtiili, ylimäärä B-portista [datalehti VPR3]).
VPR3:n suurin tulovirtaus on 60 / 80 / 120 / 200 l/min koon 3/8" / 1/2" / 3/4" / 1" mukaan.
**⚠ Tarkista asennetun VPR3:n koko**: 1800 rpm:n noin 104 l/min vaatii 3/4":n tai 1":n venttiilin.

**1. Kytkin irti (normaali ajo).** P2 ei pyöri. Vain hihnavetoinen ohjauspumppu P1 on käynnissä:
1000 rpm:llä ~19 l/min, joka menee kokonaan orbitrolille (RPF3:n raja 20 l/min); 1800 rpm:llä
~34 l/min, josta ~14 l/min menee matalalla paineella säiliöön (noin 0,2–0,5 kW, harmitonta). P1
pyörii silloin noin 2230 rpm.

**2. Kytkin päällä, keulapotkuri ei käytössä** (2/2-venttiili auki, öljy kiertää matalalla paineella):

| | 700 rpm | 1000 rpm | 1800 rpm |
|---|---|---|---|
| Pumpun tuotto | 41 l/min | 58 l/min | 104 l/min |
| Lämpö öljyyn | ~0,7 kW | ~1 kW | ~2 kW |
| Imuvirtaus 32 mm:n letkussa | 0,9 m/s | 1,3 m/s | 2,3 m/s |

**3. Keulapotkuri käytössä:**

| | 700 rpm | 1000 rpm | 1800 rpm |
|---|---|---|---|
| Työntövoima | ~88 % | ~88 % | ~88 % |
| Akseliteho PTO:lta | ~19 kW | ~27 kW | ~49 kW |
| Lämpö öljyyn | ~8 kW | ~16 kW | **~38 kW** |
| Öljyn lämpeneminen (80 l) | ~3,6 °C/min | ~7 °C/min | **~17 °C/min** |

- **Työntövoima ei kasva kierrosten mukana:** VPR3 rajaa keulapotkurin virtauksen 35 l/min:iin ja
  paineenrajoitus paineen 250 bariin. Ylimäärä muuttuu lämmöksi.
- 1800 rpm:llä öljy nousisi 40 °C:sta yli Parkerin 75 °C:n rajan parissa minuutissa.
- Momentti pysyy noin 260 Nm:ssä (PTO 420 Nm, Borelli 30500 580 Nm). 49 kW mahtuu kytkimen 60 kW:n
  ja PTO:n 79 kW:n (1800 rpm) rajoihin.
- **⚠ Tarkista,** kestävätkö VPR3 ja paluusuodatin noin 104 l/min.

**Johtopäätös: keulapotkuria käytetään vain tyhjäkäynnillä, ja se varmistetaan kierroslukituksella**
(ESP32 PDM ja Signal K):

1. PTO-kytkin päälle vain alle noin 1000 rpm:ssä.
2. Yli noin 1000 rpm:ssä keulapotkurin venttiili estetään ja 2/2-venttiili avataan automaattisesti.
   Pumppu siirtyy vapaakiertoon, ja lämpö putoaa noin 1–2 kW:iin. Toimii ilman kytkimen toimilaitettakin.
3. Hälytys, jos kytkin on päällä yli noin 1200 rpm:ssä (vaatii kytkimeen rajakytkimen).

## Imupuoli: letkun koko ja pituus sekä öljylaatu

Laskelma 2026-10-22 [laskelma]: imupaine Parker F1-061:n imuaukolla, bar ylipainetta. Säiliö noin 1 m
pumpun yläpuolella (+0,085 bar), liitinhäviöt K ≈ 2,5. Pumpun sisäiset häviöt eivät ole mukana.
Tyypillinen raja on noin −0,2 bar; F1:n oma raja **⚠ ei tiedossa**.

| Imulinja ja öljy | 700 rpm, 5 °C | 1000 rpm, 5 °C | 1800 rpm, 5 °C | 1800 rpm, 20 °C |
|---|---|---|---|---|
| 32 mm, 3 m, VG 46 | −0,20 | **−0,33** | **−0,68** | **−0,22** |
| 32 mm, 3 m, VG 32 | −0,09 | −0,17 | **−0,40** | −0,13 |
| 38 mm, 3 m, VG 46 | −0,06 | −0,12 | **−0,30** | −0,07 |
| 38 mm, 3 m, VG 32 | 0,00 | −0,04 | −0,16 | −0,02 |
| **38 mm, 2 m, VG 32** | **+0,03** | **0,00** | −0,09 | 0,00 |
| 38 mm, 2 m, HV 32 | +0,04 | +0,02 | −0,05 | +0,01 |

- **38 mm:n letku vaikuttaa eniten:** nopeus putoaa noin 30 % ja kylmän öljyn häviö lähes puolittuu.
  Se vastaa myös Parkerin suosittelemaa imuliitintä (38 mm enintään 60 l/min:lle).
- **VG 32 toiseksi eniten:** 5 °C:ssa noin 230 cSt (VG 46 noin 380 cSt).
- **2 m:n pituus 3 m:n sijaan** auttaa vähän, koska liittimien häviöt pysyvät samoina.

**Öljyn viskositeetti** [laskelma, Walther-yhtälö]:

| Öljy | 0 °C | 5 °C | 20 °C | 40 °C | 60 °C | 75 °C |
|---|---|---|---|---|---|---|
| VG 46 | ~577 cSt | ~382 | ~134 | 46 | ~21 | ~12,8 |
| VG 32 | ~336 | ~229 | ~86 | 32 | ~15 | **~9,7** |
| HV 32 | ~236 | ~171 | ~75 | 32 | ~16,5 | ~11,0 |

Parkerin rajat F1:lle: käytössä 10–400 cSt, suositus 20–30 cSt, käynnistyksessä enintään 4000 cSt,
öljy enintään 75 °C. VG 32 alittaa 10 cSt:n 75 °C:ssa; **HV 32 pysyy rajoissa sekä kylmänä että
kuumana**.

**Suositus:**
- **38 mm:n imulinja** niin lyhyenä kuin asennus sallii, ja 38 mm:n imuliitin pumppuun. Jos säiliön
  ulosotto ja palloventtiili jäävät 32 mm:ksi, lyhyt kavennus tuo vain pienen lisähäviön; uutta
  tehdessä kannattaa valita 38 mm ja täysiaukkoinen palloventtiili.
- **HV 32 -öljy.** **⚠ Tarkista** ohjauspumpun, orbitrolin ja Side-Powerin moottorin öljyvaatimukset.
- Imupuolen parannus ei vähennä keulapotkurin käytön lämpökuormaa korkeilla kierroksilla, joten
  kierroslukitus tarvitaan silti. Lämpökuorma ja jäähdytys: [oil-cooling.md](oil-cooling.md).

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
| Tuotto 700 rpm:n tyhjäkäynnillä | 43 cm³ × 700 × 0,92 ≈ **27,7 l/min** (100 %:lle tarvitaan 33,8). Työntövoima vain **noin 67 %**. ❌ (800 rpm:llä se olisi ollut 31,6 l/min ja ~88 %.) |
| Pumpun paine | 250 bar nimellinen ✅ |
| Kierrosnopeudet | Koneen 2500 rpm alittaa pumpun 2800 ja kytkimen 2700 rpm ✅ |
| PTO:n momentti (420 Nm) | ✅ Reilu marginaali |
| **Kytkimen momentti 250 barissa** | 250 bar × 43 cm³ / 2π = 171 Nm teoreettisesti, **~190 Nm** 90 %:n mekaanisella hyötysuhteella. **Juuri 185 Nm:n nimellisarvon kohdalla tai hieman yli.** ⚠ |
| Kytkimen momentti 200 barissa (Flowfitin arvo) | 137–152 Nm, noin 80 % nimellisestä. Todennäköisesti syy, miksi Flowfit ilmoittaa kokoonpanolle 200 bar. |
| Joustokytkin | HRC 150, napa 48 mm (PTO) ja 28 mm (kytkin). Momentti ≤ 190 Nm. Tarkista napatyypit. |
| Ohjaus | Vipu kytkimessä, eli kytkentä vaatii käynnin konehuoneessa tai push-pull-vaijerin / toimilaitteen. Ei asentotietoa; Signal K -näyttöön tai kierroslukitukseen tarvitaan rajakytkin. |

*Alla oleva taulukko on laskettu 800 rpm:n tyhjäkäynnillä; 700 rpm:llä 43 cm³:n pumppu jää kaikilla
asetuksilla noin 67 %:iin.*

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

- **Kytkentä vain alle 420 rpm:ssä, eli ei koneen käydessä.** 3126B:n tyhjäkäynti on noin 700 rpm.
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

- [ ] Vahvista tyhjäkäynti mittaamalla (omistajan mukaan ~700 rpm; ratkaisee pumpun koon)
- [x] Parker F1-061: tyyppikilpi F1-061-R---000, osanumero 3781060; vuotolinjaa ei tarvita
- [ ] Parker F1-061 (tori.fi, 100 €): holkin mitat, kunto; ostopäätös
- [ ] F1-061: ISO 7653 -laipan ja 8×32×36-akselin sovitus Borellin 30500:een (sovitelaippa ja -holkki)
- [ ] F1-061: pienin sallittu imupaine (Parkerin F1-luettelo)
- [ ] PTO:n pyörimissuunta (pumpun suunta sovitetaan siihen)
- [x] VPR3: kolmitie-etusijaventtiili; suurin tulovirtaus koon mukaan 60–200 l/min [datalehti VPR3]
- [ ] Asennetun VPR3:n koko; paluusuodattimen virtausluokitus (~104 l/min 1800 rpm:llä)
- [ ] Ohjauspumpun, orbitrolin ja Side-Power SH240:n öljyvaatimukset (HV 32 käy?)
- [ ] Imulinja 38 mm ja mahdollisimman lyhyt; säiliön ulosotto ja palloventtiili 38 mm, täysiaukkoinen
- [ ] Salhydro: spline-sovite 30500:n ja ryhmän 3 pumpun väliin, vipuvoima, hinta ja toimitusaika 30501/30502 + Gr.3-laippa
- [ ] PTO:n pyörimissuunta (30501 vai 30502)
- [ ] Ankkurivinssin moottorin tiedot ja odotettu käyttöaika (pitkät jaksot muuttavat lämpötilannetta)
- [ ] Side-Power SH240:n hydraulimoottorin suurin paine (jos paineenrajoitusta nostetaan)
- [x] BAV-713 350 bar, VMP 350 bar, 2/2-patruunaventtiili 350 bar
- [ ] CETOP 3 -pohjalaatan painearvo (teräs; Flowfit)
- [ ] Hyväksyykö CAT 3126B:n elektroniikka ulkoisen kierrostenkorotussignaalin? (vaihtoehto B)
