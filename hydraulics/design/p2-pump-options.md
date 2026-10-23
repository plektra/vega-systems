# Apupiirin pumppu (P2) ja PTO-kytkin — vaihtoehdot

> **Tila:** **Päätetty 2026-10-23** ([decisions.md](../../decisions.md)): P2 on Parker F1-61, veto PTO:lta
> Spidex 48/60 -kynsikytkimellä ilman PTO-kytkintä, BPV-F1-ohitusventtiili käsiohituksella
> (378 4179), 50 mm:n imulinja ja BPV:n vuotolinja säiliöön. Hankinta myöhemmin. Alla oleva
> vertailu on säilytetty taustaksi.
> Tausta: [current-system.md §0](../current-system.md). Hinnat ovat karkeita suuntaa-antavia
> arvioita; pyydä tarjoukset ennen päätöstä.

## Päätetty kokoonpano (2026-10-23)

```
PTO 1:1, Ø48 kiila ── Spidex 48/60 (98 Sh A) ── Parker F1-61 + BPV-F1 (käsiohitus) ── 3/4" ── VPR3 ── CETOP
                       └──────── oma kannake runkoon ────────┘
säiliö ── 50 mm imulinja ── imuliitin Ø50 BPV:n päällä
BPV:n vuotoliitäntä 1/4" ── oma letku säiliöön öljypinnan alle
```

| Osa | Valinta | Lisätiedot |
|---|---|---|
| Pumppu | Parker F1-61-R (378 1060), 59,5 cm³, käytetty (tori.fi) | [Ehdokas: Parker F1-061](#ehdokas-parker-f1-061-käytettynä-torifi) |
| Veto | Spidex 48/60: napa SPI-48A-KL-A8X32X36 (pumppu), napa SPI-48A-ST-D48H7 (PTO), hammaskehä 98 Sh A (tai 64 Sh D) | [Veto PTO:lta](#veto-ptolta-suoraan-f1-61lle-bpv-vaihtoehto-ei-kytkintä) |
| Tyhjäkierto | Parker BPV-F1, 24 VDC, **käsiohituksella 378 4179** | [BPV-F1](#lisävaruste-parker-bpv-f1--ohitusventtiili) |
| Imu | 50 mm:n letku mahdollisimman lyhyenä, Parkerin Ø50-imuliitin (esim. suora 378 0636 / 45° 378 0364 / 90° 378 0979) | [Imupuoli](#imupuoli-letkun-koko-ja-pituus-sekä-öljylaatu) |
| Vuotolinja | BPV:n 1/4"-vuotoliitäntä (liitin 378 3039 mukana) → oma letku säiliöön öljypinnan alle | [BPV-F1](#lisävaruste-parker-bpv-f1--ohitusventtiili) |
| Kannake | Pumppu ISO 7653 -laipalla (Ø80) omaan runkoon kiinnitettyyn kannakkeeseen; kytkimelle suojakotelo | [Veto PTO:lta](#veto-ptolta-suoraan-f1-61lle-bpv-vaihtoehto-ei-kytkintä) |

**Toimintatilat:** ajossa BPV:n kela on jännitteetön (ohitus) ja pumppu kiertää tyhjänä. Keulapotkuria
varten (tyhjäkäynnillä): 2/2-venttiili auki → BPV:n kela päälle → 2/2-venttiili kiinni →
BAV-713. Pois päältä päinvastaisessa järjestyksessä. BPV:n tilaa vaihdetaan vain alle 20 barissa.

**Vikatilat (turvallisuus):**
- *Sähkökatko tai kelan vika:* BPV ohittaa, keulapotkuri ei toimi (kuten nykyinen 2/2-venttiili).
  Käsiohituksella pumpun saa syöttämään: **kone sammutetaan ensin**, ruuvi pohjaan. Käsiohitus
  palautetaan heti korjauksen jälkeen, koska sen ollessa päällä pumppu syöttää aina ja vain
  2/2-venttiili ja kierroslukitus suojaavat piiriä.
- *BPV jää syöttöasentoon:* korkeilla kierroksilla koko tuotto kulkee piirin läpi (lämpö, VPR3:n ja
  suodattimen virtaus). Öljyn lämpötila- ja paineanturi havaitsevat tämän.
- *Pyörivä kytkin:* akseli pyörii aina koneen käydessä, joten kiinteä suojakotelo on pakollinen.
- Pätevän henkilön pitää tarkistaa kannake, linjaus, suojaus ja ohjauslogiikka ennen käyttöönottoa.

## Yhteenveto ja alustava suositus (ennen päätöstä)

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
     [Ehdokas: Parker F1-061](#ehdokas-parker-f1-061-käytettynä-torifi)). 59,5 cm³ ja 350 bar
     jatkuva, ei vuotolinjaa: 250 barissa sama ~88 % kuin A:lla, ja 280 barissa noin 99 % työntövoima, kun venttiilien
     ja keulapotkurimoottorin painearvot on varmistettu.
     Lisävarusteena saa sähköohjatun **BPV-F1-ohitusventtiilin** (noin 430 € + ALV), joka purkaa
     pumpun tyhjäkiertoon ja voisi korvata PTO-kytkimen, ks.
     [Lisävaruste: BPV-F1](#lisävaruste-parker-bpv-f1--ohitusventtiili).
  3. **E harkitaan uudelleen** vain, jos keulapotkurin tai vinssin proportionaalinen ohjaus tai
     useat samanaikaiset kuormat tulevat vaatimuksiksi.
- **Flowfitin 43 cm³:n kokoonpano ei enää sovi:** 700 rpm:llä se antaisi vain noin 67 %
  työntövoimasta, eikä sen 185 Nm:n kytkin kestä 51 cm³:n pumppua 250 barissa (~225 Nm).
- **Ennen ostoja:** vahvista tyhjäkäynti mittaamalla ja selvitä Salhydrolta spline-sovite ryhmän 3
  pumpulle.

## Kiinteät reunaehdot

| Reunaehto | Arvo |
|---|---|
| Veto | Advance 300:n PTO, 1:1 ensiöakselilta, Ø48 kiila-akseli → Spidex 48/60 → F1-61 omalla kannakkeella (päätös 2026-10-23; aiemmin HRC 150 ja kytkin) |
| PTO:n momenttiraja | ≈ 420 Nm (0,044 kW/rpm) |
| Koneen kierrokset keulapotkuria käytettäessä | Tyhjäkäynti, ~700 rpm [omistaja 2026-10-22, ei mitattu]; kytkin lukittu pois yli ~1000–1200 rpm:n |
| Mitoittava kuorma | Side-Power SH240: 264 bar × 33,8 l/min (100 %). Hyväksytty: ~90 % työntövoimasta. |
| Paineluokka | 250 bar (kustannuspäätös); letkut 300 bar; paineenrajoitusventtiili Marchesini VMP 3/4": 350 bar, 90 l/min, jousi todennäköisesti 80–300 bar |
| Tulevat kuormat | Ankkurivinssi (moottori olemassa, tiedot puuttuvat), 3 vapaata CETOP 3 -paikkaa |
| Imu | **50 mm** (päätös 2026-10-23; aiemmin 32 mm, 3 m), säiliö noin 1 m imuaukon yläpuolella |

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
harmitonta. Yli 5 minuutin yhtäjaksoinen käyttö nostaa yli 13 K. Side-Powerin mukaan hydraulinen SH-malli on
tarkoitettu juuri pitkiin käyttöjaksoihin, eikä luettelossa ole käyttöjaksorajaa, joten rajan asettaa
öljyn lämpötila. **Lämpö ei ole syy luopua vakiotilavuuspumpusta, kun
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
sekä Parkerin luettelo *MSG30-8200/UK Truck Hydraulics*
([PDF, dzwigi.net.pl](https://cdn.dzwigi.net.pl/b/v2/3781800/Document/MSG30-8200-UK-6758536ce15df.pdf),
luettu tekstinä; F1-sivut 22–29 myös kuvina). Luettelon mukaan osanumero 378 1060 on **F1-61-R**
(ISO-malli).

| Kohde | Arvo | Lähde |
|---|---|---|
| Kierrostilavuus | **59,5 cm³/r** (F1-61; nimessä oleva 61 on kokoluokka). Suurin teoreettinen tuotto 143 l/min. | luettelo s. 23 |
| Paine | 400 bar suurin käyttöpaine (ISO-malli, luettelo); 350 bar jatkuva (jälleenmyyjä) | luettelo s. 23, jälleenmyyjä |
| Kierrosnopeus | **Suurin itseimevä kierrosluku 2400 rpm** (imupaine 1,0 bar abs, mineraaliöljy 30 cSt). **Lyhytsuljettuna (matala paine, esim. BPV:n ohitusasennossa) 2700 rpm.** | luettelo s. 23 |
| Momentti ja teho | Teoreettinen momentti 378 Nm (400 barissa); suurin ottoteho 83 kW enintään 6 s minuutissa | luettelo s. 23 |
| Pyörimissuunta | **R** = oikea eli myötäpäivään akselin päästä katsottuna. **Vaihdettavissa:** päätykappaleen pultit auki, päätykappale 180° käännettynä takaisin, pultit 80–100 Nm. | ohje s. 4 |
| Laippa ja akseli | **ISO-malli:** kuorma-auton ISO 7653 -laippa ja **DIN 5462 B8×32×36** -hammasakseli (8 uraa) | jälleenmyyjä |
| Vuotolinja | **Ei tarvita.** *"Fixed displacement pumps don't need an external drain line as they are internally drained."* (Erillinen vuotolinja voidaan tarvita vain, jos pumppuun asennetaan Parkerin BPV-ohitusventtiili, ks. [Lisävaruste: BPV-F1](#lisävaruste-parker-bpv-f1--ohitusventtiili).) | ohje s. 11 |
| Imuliitin | ISO-mallin imuaukossa ei ole kierrettä: **imuliitin (suora, 45°, 90° tai 135°, puristuskappaleet ja O-rengas) tilataan erikseen.** Luettelo suosittelee F1-41…-61:lle **50 mm:n (2") liitintä**: suora 378 0636, 45° 378 0364, 90° 378 0979. Saatavana myös 45° Ø40 (378 1062) ja Ø45 (378 0975) sekä 90° Ø45 (378 0976). Asennusohjeen mukaan vähintään 38 mm, kun tuotto on enintään 60 l/min. **⚠ Kysy myyjältä, tuleeko imuliitin mukana.** | luettelo s. 62; ohje s. 4 |
| Imulinjan virtausnopeus | **enintään 1,0 m/s** (painelinja enintään 5,0 m/s) | luettelo s. 15–16 |
| Painelähtö | BSP 3/4" | luettelo s. 25 |
| Öljy | HLP (DIN 51524) tai biohajoavat esterit. Suositeltu viskositeetti 20–30 cSt; käytön rajat 10–400 cSt; käynnistyksessä enintään 4000 cSt. Öljyn lämpötila enintään 75 °C. | ohje s. 11 |
| Akselin voitelu | Jos voimanulosoton holkki on tiivistetty, hammasakseli rasvataan lämmönkestävällä rasvalla ennen käyttöönottoa ja säännöllisesti | ohje |
| Pienin sallittu imupaine | **1,0 bar absoluuttista eli noin 0 bar ylipainetta.** *"Contact Parker Hannifin if the inlet (suction) pressure is believed to be less than 1.0 bar (absolute); insufficient inlet pressure can cause noise and pump damage because of cavitation."* | luettelo s. 14 |
| Suodatus | ISO 4406 -puhtausluokka 20/18/13 | luettelo s. 80 |

### Sopivuus Vegaan [laskelma]

Oletukset: 59,5 cm³ (päivitetty 2026-10-23, aiemmin 61), volumetrinen hyötysuhde 95 %, mekaaninen 95 %, tyhjäkäynti 700 rpm.

| Tarkistus | Arvio |
|---|---|
| Tuotto 700 rpm:llä | noin 39,6 l/min, enemmän kuin keulapotkurin 33,8 l/min ✅ |
| Työntövoima, paineenrajoitus 250 bar | noin 88 % (paine rajoittaa) |
| Työntövoima, paineenrajoitus 280 bar | **noin 99 %**; pumppu kestää tämän reilusti ✅ |
| Momentti 250 / 280 barissa | noin 249 / 279 Nm: Borelli 30500 (580 Nm) ja PTO (420 Nm) riittävät; Flowfit/Borelli 30300 (185 Nm) ei |
| Lämpö | Ylimääräiset ~5–6 l/min menevät paineenrajoituksen yli, noin 2–3 kW lisälämpöä vain keulapotkurin käytön ajan; lyhyissä jaksoissa harmitonta |
| Imulinja | Nykyinen 32 mm:n letku: noin 0,86 m/s 700 rpm:llä, alle Parkerin 1,0 m/s:n rajan, mutta 1000 rpm:llä 1,2 m/s. Parkerin 1,0 bar abs:n imupainevaatimus ei täyty 32 mm:n linjalla kylmällä öljyllä. **Suositus: 50 mm:n imuliitin ja -linja**, ks. [Imupuoli](#imupuoli-letkun-koko-ja-pituus-sekä-öljylaatu). |
| Kylmä öljy | ISO VG 46 on 5 °C:ssa noin 380 cSt, eli lähellä pumpun 400 cSt:n käyttörajaa. **HV 32 -öljy** (noin 200–250 cSt 5 °C:ssa) antaisi marginaalia. |
| Pyörimissuunta | Pumpun suunta (akselin päästä katsottuna) pitää sovittaa PTO:n suuntaan (PTO-akselin päästä katsottuna). Koska suunnan voi vaihtaa, tämä ei ole riski. **⚠ Tarkista PTO:n pyörimissuunta.** |
| Kiinnitys | ISO 7653 -laippa ja 8×32×36-hammasakseli **eivät sovi suoraan** Borellin 30500:een (toisiossa 48×44-sisähammastus ja ryhmä-/SAE-laipat). Tarvitaan sovitelaippa ja -holkki, joko Salhydrolta/Borellilta tai teetettynä. Myyjän holkki on luultavasti 8×32×36-sisähammastettu holkki, josta voi tehdä vedon. **⚠ Selvitä holkin mitat.** |

**Arvio:** pumppu sopii hyvin. 100 eurolla se kannattaa ostaa, jos kunto on hyvä (ei vuotoa
akselitiivisteestä, ei välystä akselissa). Suurin avoin asia on kiinnitys Borellin 30500
-kytkimeen.

**Kysy vielä myyjältä:** holkin mitat (hammastus, ulkohalkaisija, kiila), kunto ja miksi pumppu
irrotettiin.

## Käyttäytyminen eri kierroksilla (Parker F1-061)

Laskelma 2026-10-22 [laskelma] 61 cm³:llä; todellinen 59,5 cm³ antaa noin 2,5 % pienemmät virtaukset ja lämmöt (esim. 1800 rpm:llä noin 102 l/min eikä 104), johtopäätökset eivät muutu. Parker F1-061 PTO:lla 1:1, nykyiset venttiilit (VPR3 35 l/min,
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

## Lisävaruste: Parker BPV-F1 -ohitusventtiili

Parker myy F1-pumpun päätykappaleen päälle asennettavan sähköohjatun ohitusventtiilin
(**BPV-F1-25**, sopii kokoihin F1-25, -41, -51 ja **-61**). Omistaja nosti sen esiin 2026-10-23
vaihtoehdoksi kavitaation ja lämpenemisen estämiseen korkeilla kierroksilla [omistaja 2026-10-23].

Lähde: Parkerin luettelo *HY30-8200/PL, Hydraulika do samochodów ciężarowych*, s. 47 (BPV-F1) ja
s. 48 (BPV-F2:n toimintaperiaate), puolankielinen, luettu tekstinä ja kuvina
([PDF, dzwigi.net.pl](https://cdn.dzwigi.net.pl/b/v2/3787424/Document/zawory%20bocznikowe%20BPV%20Parker.pdf)).
Ajantasaiset tiedot Parkerin asennusohjeesta *MSG30-8227-INST/UK/DE* (2023)
([PDF, dzwigi.net.pl](https://cdn.dzwigi.net.pl/b/v2/3781080/Document/Broszura-informacyjna-Bypass-Valves-BPV-dla-F1-T1-675832260051b.pdf),
luettu tekstinä ja kuvina) ja luettelosta *MSG30-8200/UK* s. 65–66 (ks. F1-osion lähteet); tilausnumerot myös
([paro.nl](https://paro.nl/library//storage/datasheets/Parker/UK/Parker_BPV-F1-BPV-T1_uk.pdf/datasheet.html))
ja hinta jälleenmyyjältä ([dzwigi.net.pl](https://dzwigi.net.pl/en/sklep/4957-bpv.html)).

### Tiedot

| Kohde | Arvo | Lähde |
|---|---|---|
| Käyttötarkoitus | Pumppu, jota ajetaan jatkuvasti suoraan koneelta (kardaani tai PTO). Ohitus kytketään päälle siirtoajossa, kun kone käy suurilla kierroksilla eikä järjestelmää ole mitoitettu pumpun koko tuotolle. *"Zawór bocznikowy BPV znacznie redukuje straty mocy podczas transportu"* (vähentää tehohäviöitä huomattavasti). | HY30-8200/PL s. 47 |
| Toiminta | Ohitusasennossa venttiili **yhdistää pumpun painepuolen sen imupuoleen**, ja järjestelmän ja säiliön kautta kulkee vain pieni öljymäärä. Parkerin mukaan tämä estää pumpun kavitaation ja suuren lämmöntuoton, joita suuri virtaus muuten aiheuttaisi. (Sanottu suoraan BPV-F2:sta; BPV-F1:n kaavio on sama.) | s. 47–48 |
| Ohjaus | Kela jännitteellisenä esiohjattu takaiskuventtiili on kiinni, ja pumppu syöttää järjestelmää. **Jännitteettömänä ohitus on päällä** eli pumppu kiertää tyhjänä. | s. 47 |
| Kytkentäehto | *"Zawór musi włączać się i wyłączać … przy ciśnieniu układu w stanie bezobciążeniowym (poniżej 20 barów)"*: venttiiliä saa vaihtaa asennosta toiseen **vain kuormittamattomana, alle 20 barin paineessa**. | s. 47 |
| Vuotolinja | **Pakollinen.** *"Drain line must be installed!"*, *"You need to use this connector otherwise the bypass valve will not work."* Vuotolinja kulkee venttiilin vuotoliitännästä suoraan säiliöön ja päättyy öljypinnan alapuolelle; se varmistaa jäähdytysvirtauksen ohitusasennossa. (Vanha HY30-8200/PL vaati sitä vain, jos järjestelmän kautta kulkee alle 5 l/min.) | MSG30-8227 s. 2–3; MSG30-8200 s. 65 |
| Vuotoliitäntä | BSP 1/4", tulpattu. Vuotoliitinsarja **378 3039 tulee venttiilin mukana** F1-61:lle (378 1640 vain F1-25:lle). Itse vuotoletku ei sisälly. | MSG30-8227 s. 3 |
| Paine | 350 bar jatkuva, 400 bar ajoittainen (sama kuin pumpulla) | s. 47 |
| Kela | 24 VDC, **14 W** (vanha luettelo 17 W). Kela CCS024HSN, patruunaventtiili DSH081NX3285. Deutsch DT -naarasliitin mukana, kaapeli ei. | MSG30-8200 s. 66; MSG30-8227 s. 3; jälleenmyyjä |
| Asennus | Venttiilirunko kiinnitetään päätykappaleen päälle: banjoliitin painelähtöön, välikeholkki imuaukkoon ja imuliitin venttiilirungon päälle kahdella kuusiokoloruuvilla ja puristuskappaleella. Kiristys: painelähdön liitin **50 ± 10 Nm ensin**, sitten ruuvit 20–25 Nm; patruunaventtiili 46 ± 3 Nm, kelan mutteri 8 ± 1 Nm. Symmetrinen, voidaan kääntää 180° ja sopii kummallekin pyörimissuunnalle. Painelähtö BSP 3/4"; ulkomitat noin 109 × 103 mm. **Imuliitin ei sisälly** (sama kuin pumpulle, ks. yllä); lisäpuristuskappalesarja BPV:lle 378 2439. | MSG30-8227 s. 3–6; MSG30-8200 s. 62, 66 |
| Käsiohitus | Mallissa 378 4179. Jos kela tai kaapeli vikaantuu, venttiilin voi kääntää käsin syöttöasentoon: **kone sammutetaan ensin**, suojakuppi pois, lukkomutteri auki (13 mm) ja ruuvi pohjaan (4 mm kuusiokoloavain). Ruuvi palautetaan korjauksen jälkeen, muuten pumppu voi vaurioitua. | MSG30-8227 s. 5 |
| Tilausnumerot, 24 VDC | **378 7201** (ilman käsiohitusta) ja 378 4179 (käsiohituksella, korvaa 378 7461). Vanha 378 1401. 12 VDC -versiot 378 7202 / 378 1318. O-rengassarja 378 0641. **Nämä sopivat F1-25…-61:lle (ja T1-81:lle), painelähdön liitin 50 Nm.** F1-81:lle ja -101:lle on **eri venttiili**: 378 4180 (käsiohituksella) ja 378 7203 / 378 7204 (24 / 12 VDC), painelähdön liitin 100 Nm, rungon mitat suuremmat (piirustuksessa 105 × 110 mm vs. 103 × 109 mm). **F1-101:n BPV ei siis sovi F1-61:een** (tarkistettu 2026-10-23, kun Torissa oli F1-101 + BPV). | MSG30-8200 s. 66; HY30-8200/PL s. 47; [datalehti Parker BPV-F1/T1](https://paro.nl/library//storage/datasheets/Parker/UK/Parker_BPV-F1-BPV-T1_uk.pdf/datasheet.html) |
| Hinta (uusi) | 378 7201: **1813,71 PLN + ALV** (saatavilla 2 kpl); 378 4179: 1896,18 PLN + ALV (ei saatavilla). Noin **430 € + ALV** (oletus 4,25 PLN/€). | jälleenmyyjä, haettu 2026-10-23 |

Suurin kierrosluku ohitusasennossa: F1-61 kestää lyhytsuljettuna (matalalla paineella) **2700 rpm**
[luettelo MSG30-8200/UK s. 23], joten koneen 1800 rpm on selvästi rajan alla. Ohitusasennon
painehäviötä ja lämpöä, ja sitä, kuinka paljon öljyä vuotolinjan kautta kulkee, **ei ilmoiteta
missään Parkerin julkaisussa** **⚠ ei tiedossa** (kysyttävä Parkerilta tai mitattava).

### Mitä BPV muuttaisi Vegalla [laskelma, arvio]

**1. Kytkin päällä korkeilla kierroksilla (kytkin unohtunut tai pumppu ilman kytkintä).** Nykyisellä
2/2-vapaakiertoventtiilillä pumpun koko tuotto (1800 rpm:llä noin 104 l/min) kulkee imuletkun,
VPR3:n, paluusuodattimen ja jäähdyttimen kautta. Imupaine on silloin kylmällä öljyllä −0,3…−0,7 bar,
VPR3:n ja suodattimen virtauskesto on epävarma, ja lämpöä tulee noin 2 kW. BPV:n ollessa
ohitusasennossa öljy kiertää pumpun päätykappaleessa, joten:

- **imuletkun virtaus putoaa muutamaan l/min:iin**, eikä imupuolen kavitaatioriskiä enää ole
  (imupuolen taulukon 1000–1800 rpm:n rivit menettävät merkityksensä tässä tilassa);
- VPR3:n, paluusuodattimen ja EC100:n ei tarvitse kestää 104 l/min:ää;
- lämpökuorma pienenee Parkerin mukaan huomattavasti. Tarkkaa lukua ei ole, koska ohitusasennon
  painehäviötä ei ilmoiteta. **⚠ ei tiedossa**

**2. Keulapotkuri käytössä korkeilla kierroksilla:** BPV ei auta. Ylimäärä menee edelleen VPR3:n ja
paineenrajoituksen yli (1000 rpm:llä ~16 kW, 1800 rpm:llä ~38 kW). **Keulapotkurin kierroslukitus
tarvitaan edelleen.**

**3. Voisiko BPV korvata PTO-kytkimen?** Tähän käyttöön Parker on venttiilin tehnyt: kuorma-auton
pumppu on kytketty pysyvästi, ja BPV purkaa sen ajon ajaksi. Vegalla se tarkoittaisi:

| | Borelli 30500 -kytkin + 2/2-venttiili (nykyinen suunnitelma) | BPV ilman kytkintä | Kytkin **ja** BPV |
|---|---|---|---|
| Pumppu pyörii ajossa | ei | **aina, kun kone käy** (laakerien ja akselitiivisteen kuluminen, pieni tyhjäkäyntihäviö) | ei |
| Imupuolen kavitaatio korkeilla kierroksilla | ei (kytkin irti); riski, jos kytkin unohtuu päälle | ei (ohitus) | ei |
| Ohjaus | mekaaninen vipu tai vaijeri, kauko-ohjaukseen toimilaite ja rajakytkin | 24 V:n kela (14 W) suoraan ESP32 PDM:ltä | molemmat |
| Kytkentäehto | kytkin vain alle ~1000 rpm:ssä | venttiili vain alle 20 barissa, kaikilla kierroksilla | molemmat |
| Kiinnitys | pumppu ISO 7653 -sovitelaipalla 30500:aan | pumppu sovitelaipalla suoraan PTO:hon (joustokytkin tai holkki) | kuten kytkimellä |
| Hinta | kytkin + sovitteet, **⚠ tarjous Salhydrolta puuttuu** | BPV noin 430 € + ALV, käytettynä halvempi | molemmat |
| Kun sähköt katkeavat | kytkin pysyy asennossaan | ohitus päälle, pumppu kiertää tyhjänä | ohitus päälle |

- **Sähkökatko:** BPV on jännitteettömänä ohitusasennossa, joten sähkökatko pysäyttää keulapotkurin.
  Sama tapahtuu jo nyt, koska 2/2-vapaakiertoventtiili on jännitteettömänä auki. Uutta vikatilaa ei
  synny, mutta keulapotkuri ei ole käytettävissä sähkökatkon aikana kummassakaan ratkaisussa.
  Ohjaus (P1) ei ole BPV:n varassa.
- **Vikatila: BPV jää kiinni (ei ohita).** Ilman kytkintä pumppu syöttäisi koko tuoton piiriin
  korkeilla kierroksilla, kuten nykyisessä suunnitelmassa unohtuneen kytkimen kanssa. 2/2-venttiili
  aukeaa yhä, joten paine pysyy matalana, mutta imupuoli ja lämpö ovat samassa tilanteessa kuin
  taulukossa yllä. **Öljyn lämpötila- ja imupaineanturi tarvitaan silti.**
- **Pumppu pyörii jatkuvasti:** F1-61 kestää ohitusasennossa 2700 rpm, joten kierrosluku ei rajoita.
  Laakerien ja akselitiivisteen käyttöikää Parker ei ilmoita. Omistajien arvio: pumppu kestää
  pitkään, koska se on tehty kuorma-autojen PTO-asennuksiin, joissa se pyörii aina moottorin mukana
  [omistaja 2026-10-23]. Vegan kone käy alle 1000 h vuodessa [omistaja 2026-10-23]; raskaassa
  liikenteessä vuotuiset käyttötunnit ovat tyypillisesti suuremmat (arvio). Ohitusasennossa pumppu
  pyörii lisäksi kuormittamattomana, joten kulumisen ei arvioida ratkaisevan valintaa.
- **Ohjausjärjestys** 20 barin rajan vuoksi:
  - *Päälle:* 2/2-venttiili auki (paine alle 20 bar) → BPV:n kela päälle → 2/2-venttiili kiinni →
    keulapotkurin venttiili.
  - *Pois:* keulapotkurin venttiili keskelle → 2/2-venttiili auki → BPV:n kela pois.
  - Ohjain hoitaa järjestyksen. Paineanturi pumpun lähdössä on hyvä varmistus.
- **Vuotolinja (pakollinen):** BPV:n 1/4":n vuotoliitännästä oma letku suoraan säiliöön, öljypinnan
  alapuolelle, ei yhteiseen paluulinjaan. Parkerin nykyiset ohjeet vaativat sen aina.
- **Imuliitin:** sama 50 mm:n imuliitin kiinnittyy BPV:n päälle, joten imulinjan suositus ei muutu.
  Ohitusasennossa imulinjan virtaus on pieni, joten imupaineen raja koskee vain syöttötilaa
  (tyhjäkäynti, keulapotkuri).

**Arvio:** BPV ratkaisee kavitaation ja suuren läpivirtauksen kaikissa tilanteissa, joissa
keulapotkuria ei käytetä. **Varteenotettavin käyttö on korvata sillä PTO-kytkin**, jos F1-61
ostetaan: sähköinen ohjaus on yksinkertaisempi kuin mekaanisen kytkimen kauko-ohjaus, ja
kierroslukitus koskee silloin vain keulapotkurin venttiiliä. Jatkuvasti pyörivän pumpun kuluminen
ei omistajien arvion mukaan ole este (alle 1000 h vuodessa, ks. yllä). Vertailu vaatii vielä
Salhydron tarjouksen kytkimestä ja sovitteista. Kytkimen kanssa BPV on lisävarmistus unohtunutta kytkintä vastaan,
mutta 430 €:lla se on silloin kallis varmistus verrattuna kierroslukitukseen ja hälytykseen.
Hammaspyöräpumppuun (vaihtoehto A) BPV:tä ei saa; sille vastaava ratkaisu olisi kytkin.

### Veto PTO:lta suoraan F1-61:lle (BPV-vaihtoehto, ei kytkintä)

Selvitys 2026-10-23. Ketju: **PTO:n Ø48-kiila-akseli → joustokytkin → F1-61:n hammasakseli**.
Pumppu laipoitetaan omaan, runkoon kiinnitettyyn kannakkeeseen, joten kytkin välittää vain
momentin. Parker ei salli pumpun akselille säteis- eikä aksiaalikuormaa: *"No external radial or
axial shaft loads are allowed on the pump shaft"* [luettelo MSG30-8200/UK s. 79].

**Mitoittava momentti** [laskelma]: 59,5 cm³, mekaaninen hyötysuhde 95 %: noin 249 Nm 250 barissa ja
279 Nm 280 barissa. Dieselvetoisen hydraulipumpun käyttökertoimella noin 2 (arvio; tarkista
kytkinvalmistajan taulukosta) tarve on noin 500–560 Nm.

**Suositus: valmis Spidex-kynsikytkin (koko 48/60), ei koneistusta** [selvitys 2026-10-23].
Salhydro myy R+L Hydraulicsin Spidex-kytkimen napoja suoraan kuorma-auton pumppuakselille
(*"DIN 5462, ISO 14 = B 8 x 32 x 36 (typical truck pump shaft)"*). Spidex on samaa kynsikytkintyyppiä
kuin KTR Rotex, ja osat ovat keskenään vaihtokelpoisia
([Salhydro, uritetut navat](https://www.salhydro.fi/en/product/spidex-hubs-for-splined-shaft);
[lieriöakselin navat](https://www.salhydro.fi/en/product/hydraulic-components/pumps-and-power-units/mechanical-transmission/spidex-hubs-for-cylindrical-shaft);
[Spidex-luettelo](https://files.salhydro.fi/files/products/Spidex_ja_Dentex_tekniset_tiedot.pdf), luettu tekstinä).

| Osa | Koodi (Salhydro) | Tiedot |
|---|---|---|
| Pumpun napa | **SPI-48A-KL-A8X32X36** | uritus B8×32×36, teräs, Ø105 mm |
| PTO:n napa | **SPI-48A-ST-D48H7** | reikä 48 H7, teräs, Ø105 mm. A-navan suurin reikä on juuri 48 mm. Kiilaura DIN 6885 luettelon vakiona **⚠ varmista tilatessa** |
| Hammaskehä (elastinen välikappale) | Spidex 48/60, **98 Sh A** tai 64 Sh D | koodi **⚠ Salhydrolta** |

Spidex 48/60:n arvot [luettelo s. 9, 11 ja 16]:

| Hammaskehä | Nimellismomentti TKN | Suurin TKmax | Suurin kierrosluku |
|---|---|---|---|
| 92 Sh A (vakio) | 310 Nm | 620 Nm | 5600 rpm |
| **98 Sh A** | **525 Nm** | **1050 Nm** | 5600 rpm |
| 64 Sh D | 655 Nm | 1310 Nm | 5600 rpm |

- Pituus A/A-navoilla 140 mm, navat 56 mm kumpikin, napojen väli 28 mm.
- Sallitut virheet 1000 rpm:llä: aksiaalinen 2,1 mm, säteis 0,44 mm, kulma 1,2°. Säteis- ja
  kulmavirhe kerrotaan 0,7:llä 40–60 °C:ssa.
- **Mitoitus** luettelon menetelmällä [laskelma]: TN 279 Nm (280 bar) × K1 noin 1,3 (hydraulipumppu
  1,0 luettelon mukaan, korotettu dieselvedon vuoksi, arvio) × K2 1,0 (alle 100 käynnistystä
  tunnissa) × K3 1,3 (konehuone noin 50 °C, vakiohammaskehä) ≈ **470 Nm**. 98 Sh A:n 525 Nm riittää,
  64 Sh D antaa lisävaraa. Vakiokehä 92 Sh A (310 Nm) ei riitä.
- Pienempi koko 42/55 (SPI-42A-KL-A8X32X36, sintraterästä, ja SPI-42B-GG-D48H7) riittäisi vain
  64 Sh D -kehällä (TKN 560 Nm); 98 Sh A (450 Nm) jää 280 barissa alle tarpeen.
- Pumpun napa lukitaan akselin pään M12-pultilla ja aluslevyllä; PTO-napa kiilalla ja
  pidätysruuvilla.
- **Hinta:** Salhydro ei näytä hintoja (tarjouspyyntö). Halvimmat löydetyt hinnat Euroopasta
  (haettu 2026-10-23, ALV 0 %, ilman rahteja). Saman kokoluokan Spidex 48/60-, KTR Rotex 48- ja SIT
  Trasco 48/60 -osat ovat valmistajien mukaan keskenään vaihtokelpoisia **⚠ varmista sovitus
  ennen asennusta**:

  | Osa | Tuote | Hinta ALV 0 % | Myyjä, toimitus |
  |---|---|---|---|
  | Pumpun napa (8×32×36) | KTR Rotex 48 ST napa 1.3, DIN ISO 14 8×32×36, KTR 020485044032, pituus 45 mm | **134,39 €** | [Mercateo](https://www.mercateo.com/p/1955-2000343706/KTR_ROTEX_48_ST_Nabe_1_3_P004301_DIN_ISO_14_8x32x36_DIN5462_Aussenbund_ueb.html?viewOptions=secureMode), ei varastossa, noin 20 pv; vain yritysasiakkaille. Toinen tarjous 142,84 €. Halvempaa ei löytynyt. |
  | PTO:n napa (48 H7 + kiilaura) | SIT Trasco GRMP48/60AF48, valurauta, valmis 48 H7 -reikä, kiilaura DIN 6885 | **61,80 €** | [tyma.eu](https://www.tyma.eu/products/trasco-48-60-grmp-grmp48-60af48-hub-type-a-d-48h7-cast-iron/) (Tšekki), noin 3 viikkoa |
  | Hammaskehä 98 Sh A | Spidex 48/60 punainen 98° (HV71007010) | **19,00 €** | [BJ-Gear](https://shop.bj-gear.com/en_eur/spidex-spider-48-red-98-shore-a) (Tanska), varastossa |
  | – vaihtoehto | Trasco AR48/60R 98 Sh A; AR48/60V 64 Sh D | 19,32 € / 28,98 € | [tyma.eu](https://www.tyma.eu/products/trasco-48-60-ar48-60r-elastic-spider-98-shore-a-red-polyurethane/) |

  **Yhteensä noin 215 € + ALV 25,5 % ≈ 270 €** ja rahdit [laskelma]. Kahdesta kaupasta (Mercateo ja
  tyma.eu, kehä samasta kaupasta kuin PTO:n napa) noin 216 € + ALV. BJ-Gearin Spidex-napa A 48/60
  (77 €) on ilmoitettu vain reikäalueella 19–48 mm, joten se on todennäköisesti esiporattu ja
  vaatisi sorvausta ja kiilauran.
  **⚠ Pyydä vertailuksi tarjous Salhydrolta** (kotimainen toimitus, sama tuoteperhe).

  **Kuluttajana ja yhdestä paikasta** (selvitys 2026-10-23): verkosta ei löytynyt kauppaa, joka myy
  kaikki kolme osaa kuluttajalle ja toimittaa Suomeen. Mercateo myy vain yrityksille. Saksalainen
  tefa24.de myy kuluttajille (Rotex 48 -napa 48 H7 + kiilaura 135,37 €, kehä 98 Sh A 17,93 €,
  64 Sh D 27,61 €, hinnat sis. Saksan ALV:n), mutta 8×32×36-napaa siellä on vain koossa 42, eikä
  kauppa toimita Suomeen. Suomalaisista verkkokaupoista (hydraulics.fi, koneosakeskus.fi,
  hydrauliikkakauppa.fi) ei löytynyt 8×32×36-napaa eikä koon 48/60 osia. **Suositus: tarjous
  Salhydrolta kaikista kolmesta Spidex-osasta, vertailuksi hydrauliikkakauppa.fi** (kuluttajille
  myyvä verkkokauppa, hankkii valikoiman ulkopuolisia osia tilauksesta). Vertailuhinta Euroopasta
  osina noin 270 € sis. ALV 25,5 % + rahdit.

**Muut vaihtoehdot:**
- **HRC 150 + valmis uritettu holkki:** Salhydron **EPH-8-36** on valmis B8×32×36-uritettu holkki
  (Ø60 × 50 mm) hitsattavaksi navan sisään. HRC 150:n B-napaan (esiporattu) sorvataan Ø60-reikä ja
  holkki hitsataan tai kiinnitetään siihen. Tämä on yksinkertaisempaa työtä kuin urituksen
  avartaminen, mutta vaatii silti konepajaa. Kannattaa vain, jos HRC 150 on jo hankittu. HRC 150:n
  momentti jälleenmyyjien mukaan 600 Nm
  ([BEP, HRC-luettelo](https://bepltd.com/cdn/shop/files/HRC-COUPLING.pdf)) **⚠ vahvista**.
- **Myyjän holkki** HRC:n B-napaan samaan tapaan, jos mitat sopivat. **⚠ Selvitä holkin mitat.**
- **Urituksen avartaminen HRC-napaan** koneistamolla: toimii, mutta todennäköisesti kallein.

**Pumpun kannake (runkoalusta):**
- ISO 7653 -laippa: keskitys **Ø80 mm** (akseli 0/−0,013, kannakkeen reikä Ø80 H8), **4 × Ø13 mm:n
  reikää** M12-pulteille. Reikäjako on luettu mittapiirroksesta kuvana **⚠ tarkista pumpusta**
  [luettelo s. 24].
- Pumppu painaa 8,5 kg, ja BPV ja imuliitin tulevat sen päälle. Imu- ja vuotoletkun on mahduttava.
- **Linjaus:** pumpun akseli PTO-akselin kanssa samaan linjaan HRC:n sallimien säteis-, kulma- ja
  aksiaalivirheiden sisään **⚠ arvot Fennerin luettelosta**. Tarkista uudelleen koeajon jälkeen.
- **Akselien väli:** Spidex 48/60 vie 140 mm (HRC 150 noin 107,5–129,5 mm), joten PTO-akselin pään ja
  pumpun laipan väli on suunniteltava sen mukaan. **⚠ Mittaa PTO-akselin pituus ja tila.**

**Huolto ja turvallisuus:**
- Pumpun uritus rasvataan lämmönkestävällä rasvalla ennen käyttöönottoa ja vähintään kerran
  vuodessa [luettelo s. 79].
- **Pyörivä kytkin vaatii kiinteän suojakotelon.** Ilman kytkintä akseli pyörii aina, kun kone käy,
  ja se voi tarttua vaatteisiin tai käteen.
- Pumpun pyörimissuunta (R/L) sovitetaan PTO:n pyörimissuuntaan. **⚠ Tarkista PTO:n suunta.**
- Pätevän henkilön pitää tarkistaa kannake, linjaus ja suojaus ennen käyttöönottoa.

**Jos kytkin pidetään** (Borelli 30500), HRC 150 tulee PTO:n ja kytkimen Ø42-ensiöakselin väliin, ja
pumppu laipoitetaan kytkimen toisioon sovitelaipalla ja -holkilla (ks. [Kiinnitys](#sopivuus-vegaan-laskelma)).

## Imupuoli: letkun koko ja pituus sekä öljylaatu

Laskelma 2026-10-23 [laskelma]: imupaine Parker F1-61:n imuaukolla, bar ylipainetta. Kierrostilavuus
59,5 cm³ (koko imuvirtaus kulkee letkun kautta). Säiliö noin 1 m pumpun yläpuolella (+0,085 bar),
liitinhäviöt K ≈ 2,5, laminaarivirtaus. Pumpun sisäiset häviöt eivät ole mukana.

**Parkerin raja: imupaine vähintään 1,0 bar absoluuttista eli noin 0 bar ylipainetta** (luettelo
MSG30-8200/UK s. 14; alle tämän pitää kysyä Parkerilta). Aiemmin tässä käytetty −0,2 bar oli
yleinen nyrkkisääntö, ja se on Parkerin vaatimusta väljempi. Negatiiviset luvut alla alittavat
Parkerin rajan.

| Imulinja ja öljy | 700 rpm, 5 °C | 1000 rpm, 5 °C | 1800 rpm, 5 °C | 1800 rpm, 20 °C |
|---|---|---|---|---|
| 32 mm, 3 m (vanha letku), VG 46 | −0,19 | **−0,32** | **−0,66** | **−0,21** |
| 32 mm, 3 m, VG 32 | −0,08 | −0,16 | **−0,38** | −0,12 |
| 38 mm, 3 m, VG 46 | −0,05 | −0,12 | **−0,29** | −0,06 |
| 38 mm, 3 m, VG 32 | 0,00 | −0,04 | −0,15 | −0,02 |
| 38 mm, 2 m, VG 32 | +0,03 | 0,00 | −0,08 | +0,01 |
| 38 mm, 2 m, HV 32 | +0,04 | +0,02 | −0,05 | +0,01 |
| 50 mm, 3 m, VG 46 | +0,04 | +0,02 | −0,04 | +0,04 |
| **50 mm, 3 m, HV 32** | **+0,06** | **+0,05** | **+0,02** | **+0,05** |
| 50 mm, 2 m, HV 32 | +0,07 | +0,06 | +0,04 | +0,06 |

Virtausnopeus (Parkerin raja 1,0 m/s): 32 mm 0,86 / 1,23 / 2,22 m/s, 38 mm 0,61 / 0,87 / 1,57 m/s ja
50 mm 0,35 / 0,51 / 0,91 m/s (700 / 1000 / 1800 rpm).

- **50 mm:n linja täyttää Parkerin vaatimukset kaikilla kierroksilla** HV 32 -öljyllä, ja
  tyhjäkäynnillä myös kylmällä VG 46:lla. Parker suosittelee F1-61:lle juuri 50 mm:n imuliitintä.
- **38 mm** riittää tyhjäkäynnillä vain lyhyenä ja ohuemmalla öljyllä. 1800 rpm:llä se ei riitä.
- **32 mm:n nykyinen linja ei täytä Parkerin vaatimusta** kylmällä öljyllä edes tyhjäkäynnillä.
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
- **50 mm:n imulinja** (päivitetty 2026-10-23, aiemmin 38 mm) ja Parkerin 50 mm:n imuliitin
  pumppuun, linja niin lyhyenä kuin asennus sallii. Jos säiliön ulosotto ja palloventtiili jäävät
  32 mm:ksi, lyhyt kavennus tuo pienen lisähäviön; uutta tehdessä kannattaa valita 50 mm ja
  täysiaukkoinen palloventtiili. 38 mm on vähimmäisratkaisu, jos keulapotkuria käytetään vain
  tyhjäkäynnillä ja pumppu irrotetaan (kytkin tai BPV) korkeammilla kierroksilla.
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
- [x] P2:ksi valittu Parker F1-61 (päätös 2026-10-23)
- [ ] Parker F1-061 (tori.fi, 100 €): kunto, holkin mitat, imuliitin mukana?; osto
- [x] ~~F1-061: sovitus Borellin 30500:een~~ ei tarpeen, PTO-kytkimestä luovuttu (päätös 2026-10-23)
- [x] F1-061: pienin sallittu imupaine 1,0 bar abs (≈ 0 bar ylipainetta) [luettelo MSG30-8200/UK s. 14]
- [x] F1-61: kierrostilavuus 59,5 cm³; suurin itseimevä kierrosluku 2400 rpm, lyhytsuljettuna 2700 rpm [luettelo s. 23]
- [x] F1-61: jatkuvasti pyörivän pumpun kuluminen; omistajien arvio: kestää (kuorma-autokäyttöön tehty, Vega alle 1000 h/v) [omistaja 2026-10-23]
- [x] BPV-F1: vuotoliitinsarja 378 3039 tulee venttiilin mukana; vuotolinja on pakollinen [MSG30-8227]
- [ ] BPV-F1: ohitusasennon painehäviö ja lämpö (ei julkaistu; kysy Parkerilta tai mittaa)
- [ ] Tuleeko tori.fi-pumpun mukana imuliitin (ISO-mallissa ei kierreimuaukkoa)?
- [ ] Veto ilman kytkintä: tarjous Salhydrolta Spidex 48/60 -osista (SPI-48A-KL-A8X32X36, SPI-48A-ST-D48H7, hammaskehä 98 Sh A); onko HRC 150 jo hankittu?
- [ ] PTO-akselin pituus ja tila PTO:n ja pumppukannakkeen välillä
- [ ] Imulinjan suurentaminen 50 mm:iin: säiliön ulosotto ja palloventtiili
- [x] Vegan koneen käyttötunnit: alle 1000 h vuodessa [omistaja 2026-10-23]
- [x] BPV-F1 vai PTO-kytkin: BPV valittu (päätös 2026-10-23)
- [ ] **BPV:n ohitustilan lämpö ajossa** (tunteja 1000–1800 rpm:llä): ei julkaistu; kysy Parkerilta, mittaa öljyn lämpötila ensimmäisellä kaudella
- [ ] Pumppukannakkeen suunnittelu: ISO 7653 -laippa, linjaus PTO-akseliin, Spidex-kytkimen 140 mm, suojakotelo
- [ ] Säiliöön liitännät: 50 mm:n imu-ulosotto ja palloventtiili, vuotolinjan paluu öljypinnan alle
- [ ] PTO:n pyörimissuunta (pumpun suunta sovitetaan siihen)
- [x] VPR3: kolmitie-etusijaventtiili; suurin tulovirtaus koon mukaan 60–200 l/min [datalehti VPR3]
- [ ] Asennetun VPR3:n koko; paluusuodattimen virtausluokitus (~104 l/min 1800 rpm:llä)
- [ ] Ohjauspumpun, orbitrolin ja Side-Power SH240:n öljyvaatimukset (HV 32 käy?)
- [ ] Imulinja 50 mm (päivitetty, aiemmin 38 mm) ja mahdollisimman lyhyt; säiliön ulosotto ja palloventtiili täysiaukkoinen
- [x] ~~Salhydro: Borelli 30501/30502 -tarjous~~ ei tarpeen (päätös 2026-10-23)
- [ ] Ankkurivinssin moottorin tiedot ja odotettu käyttöaika (pitkät jaksot muuttavat lämpötilannetta)
- [ ] Side-Power SH240:n hydraulimoottorin suurin paine (jos paineenrajoitusta nostetaan)
- [x] BAV-713 350 bar, VMP 350 bar, 2/2-patruunaventtiili 350 bar
- [ ] CETOP 3 -pohjalaatan painearvo (teräs; Flowfit)
- [ ] Hyväksyykö CAT 3126B:n elektroniikka ulkoisen kierrostenkorotussignaalin? (vaihtoehto B)
