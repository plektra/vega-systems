# Ohjauspumppu P1: imulinja ja muutokset P2-remontin yhteydessä

> **Tila:** selvitys 2026-10-23. **Päätetty 2026-10-23: kohdat 1, 3, 4 ja 5** (32 mm:n imulinja,
> täysiaukkoinen palloventtiili, HVLP 32 -öljy, imupaineen mittaus käyttöönotossa); kohta 6: välitystä ei muuteta. **Päätetty 2026-11-13: uusi P1 on ryhmän 3 pumppu 20 cm³ (30C20X146), ja vanha ryhmän 3 tukilaakeri ja kannake käytetään** (kohta 7, [Uuden P1:n kierrostilavuus](#uuden-p1n-kierrostilavuus)). Imulaskelmat alla on tehty vanhalle 16,6 cm³:n pumpulle; 20 cm³:n arvio on erikseen. **2026-11-05:** P1 tarvitsee uuden ryhmän 2 tukilaakerin ja kannakkeen, mahdollisesti myös uuden käyttöakselin (ks. [kohta 7](#tukilaakeri-kannake-ja-käyttöakseli)) [omistaja 2026-11-05]. Imulinjan mitat [omistaja 2026-10-23],
> laskelmat [laskelma]. 2026-10-28: 32 mm:n täysiaukkoinen palloventtiili on jo olemassa P2:n nykyisessä imulinjassa säiliön ulosotolla ja jää P1:lle [omistaja 2026-10-28]. 2026-10-26: öljypinta vähintään 1 m pumppujen yläpuolella [omistaja], joten laskelman oletus pätee. Ohjaus on turvallisuuskriittinen: **pätevän henkilön pitää tarkistaa
> ohjauspiirin muutokset ennen rakentamista.**

Liittyy: [current-system §3.3](../current-system.md#33-piiri-1--ohjaus),
[P2:n selvitys](archive/p2-pump-options.md), [öljynjäähdytys](oil-cooling.md).

## Lähtötiedot

| Kohde | Arvo | Lähde |
|---|---|---|
| Pumppu | **Uusi (päätös 2026-11-13): ryhmän 3 hammaspyöräpumppu 30C20X146, 20 cm³, max 3000 rpm, kartio 1:8 ja 4 mm:n kiila**, **laippaliitännät, max 250 bar** [omistaja 2026-11-13]; imu- ja painelaipat otetaan vanhasta P2:sta [omistaja 2026-11-13]; imupaineraja ja pienin viskositeetti **⚠ ei tiedossa**. Vanha: Salami 2PE16D-P28P1, 16,6 cm³, max 3000 rpm (akseli katkaistu, ei korjata) | [datalehti Hydrauliikkakauppa.fi 2026-11-12], [datalehti Salami 2PE] |
| Aiempi asennus | Tandemina vanhan kiinteätilavuuksisen P2:n (Salami 3PB33D, ryhmä 3) perässä samalla akselilla; tukilaakeri oli P2:n (ryhmä 3) | [omistaja 2026-11-05] |
| Käyttöakseli | Katkaistu tandem-käyttöä varten; uusi akseli mahdollisesti tarpeen | [omistaja 2026-11-05] |
| Veto | 2 kiilahihnaa, kone:pumppu 1:1,24 | [blogi 2017-07-04] |
| Koneen kierrosalue | 700 (tyhjäkäynti, ei mitattu) – 2400 rpm | [omistaja 2026-10-22] |
| Pienin sallittu imupaine | **0,7 bar abs ≈ −0,3 bar ylipainetta** | [datalehti Salami 2PE] |
| Pienin viskositeetti | 12 cSt | [datalehti Salami 2PE] |
| Nykyinen imulinja | **25 mm:n sisähalkaisija, 320 cm** | [omistaja 2026-10-23] |
| Mahdollinen pidempi linja | enintään 5 m | [omistaja 2026-10-23] |
| Säiliön öljypinta suhteessa P1:een | **vähintään 1 m P1:n ja P2:n yläpuolella** (laskelmassa 1 m) | [omistaja 2026-10-26] |
| P1:n imuaukon koko | **3/4"** (≈ 19 mm) | [omistaja 2026-10-23] |

**Koko pumpun tuotto kulkee imuletkun läpi:** RPF3 palauttaa ylimäärän säiliöön, joten imuvirtaus
kasvaa suoraan kierrosten mukana.

| Koneen rpm | P1 rpm | Imuvirtaus | Nopeus 25 mm:n letkussa | Nopeus 32 mm:n letkussa |
|---|---|---|---|---|
| 700 | 870 | 14,4 l/min | 0,49 m/s | 0,30 m/s |
| 1000 | 1240 | 20,6 l/min | 0,70 m/s | 0,43 m/s |
| 1800 | 2230 | 37,1 l/min | 1,26 m/s | 0,77 m/s |
| 2400 | 2980 | 49,4 l/min | **1,68 m/s** | 1,02 m/s |

Imulinjan tavallinen suositus on enintään noin 1 m/s (Parkerin raja F1:lle on sama).

## Imupaine P1:n imuaukolla

Laskelma 2026-10-23 [laskelma]: samat oletukset kuin [P2:n imulaskelmassa](archive/p2-pump-options.md#imupuoli-letkun-koko-ja-pituus-sekä-öljylaatu):
laminaarivirtaus, liitinhäviöt K ≈ 2,5, tiheys 870 kg/m³, säiliön öljypinta 1 m pumpun yläpuolella
(+0,085 bar). Imuvirtaus teoreettinen (100 %). Pumpun sisäiset häviöt eivät ole mukana.
**Mukana 3/4":n imuaukon liitin** [omistaja 2026-10-23]: oletettu 0,1 m Ø19 mm ja supistus
K ≈ 1 (arvio). Virtausnopeus aukossa on 2400 rpm:llä noin 2,9 m/s. Suluissa arvo ilman liitintä.
Bar ylipainetta; **Salamin raja −0,3 bar**, lihavoidut alittavat sen.

| Imulinja ja öljy | 700 rpm, 5 °C | 1000 rpm, 5 °C | 1800 rpm, 5 °C | 2400 rpm, 5 °C | 2400 rpm, 20 °C | 2400 rpm, 40 °C |
|---|---|---|---|---|---|---|
| 25 mm, 3,2 m (nykyinen letku), VG 46 | −0,21 | **−0,34** | **−0,70** | **−0,98** (−0,86) | **−0,33** | −0,10 |
| 25 mm, 3,2 m, HV 32 | −0,05 | −0,11 | −0,29 (−0,24) | **−0,43** (−0,35) | −0,18 | −0,07 |
| 25 mm, 5 m, VG 46 | **−0,36** | **−0,56** | **−1,09** | **−1,49** | **−0,51** | −0,16 |
| 25 mm, 5 m, HV 32 | −0,12 | −0,21 | **−0,46** | **−0,66** | −0,28 | −0,11 |
| 32 mm, 3,2 m, VG 46 | −0,04 | −0,10 | −0,26 | **−0,39** | −0,11 | −0,01 |
| **32 mm, 3,2 m, HV 32** | +0,03 | 0,00 | −0,08 | −0,15 (−0,08) | −0,05 | 0,00 |
| 32 mm, 5 m, VG 46 | −0,10 | −0,18 | **−0,40** | **−0,58** | −0,18 | −0,04 |
| **32 mm, 5 m, HV 32** | 0,00 | −0,04 | −0,15 | −0,24 (−0,16) | −0,08 | −0,01 |

**Jos säiliön öljypinta on samalla korkeudella kuin P1**, kaikki arvot ovat noin 0,08 bar
huonompia. Silloin 25 mm × 3,2 m alittaa rajan kylmällä HV 32:lla jo noin 1800 rpm:llä (−0,37),
ja 32 mm × 5 m HV 32:lla on 2400 rpm:llä ja 5 °C:ssa juuri rajalla (−0,32). 32 mm × 3,2 m pysyy
silloinkin rajan sisällä (−0,24).

**Hihnavälityksen pienentäminen 1:1,15:een** (avoin kysymys kierrosrajan vuoksi) parantaa imua
vain vähän: 25 mm × 3,2 m, HV 32, 2400 rpm, 5 °C: noin 0,03–0,04 bar. Se ei korvaa isompaa letkua.

### Johtopäätökset

- **25 mm × 3,2 m riittää lämpimällä öljyllä** kaikilla kierroksilla ja HV 32 -öljyllä kylmänä
  noin 1800 rpm:iin asti, rajan tuntumassa (−0,29). Kylmällä öljyllä täysillä kierroksilla pumppu
  kavitoi (ulina, kuluminen). VG 46 -öljyllä raja tulee kylmänä vastaan jo noin 1000 rpm:llä.
- **25 mm × 5 m ei riitä:** kylmällä öljyllä kavitaatio alkaa tavallisilla ajokierroksilla.
- **32 mm riittää 5 metriin asti HV 32 -öljyllä**, kun säiliö on noin 1 m pumpun yläpuolella. Jos
  säiliö on pumpun tasolla, pidä linja lyhyenä (≈ 3 m).
- **3/4":n imuaukko on linjan kapein kohta.** Siihen ei voi vaikuttaa, mutta sen häviö pysyy
  pienenä, kun supistus tehdään suoraan pumpun aukolla: suora 3/4" BSP -nippa ja letkun supistus
  aukon kohdalla. **Ei 3/4":n letkua, kulmaliitintä tai pitkää putkea imuaukon jälkeen.**
- Virtausnopeuden suositus (≤ 1 m/s) täyttyy 32 mm:n letkulla koko kierrosalueella, 25 mm:n letkulla
  vain noin 1400 koneen rpm:ään asti.

## Ehdotus: P1:n muutokset P2-remontin yhteydessä

P2:n muutoksissa säiliöön tehdään joka tapauksessa uusi 50 mm:n imu-ulosotto, öljy vaihdetaan ja
paluulinjat kootaan uudelleen jäähdyttimen kautta. Samalla kannattaa tehdä nämä P1:n muutokset,
koska säiliö on silloin tyhjä ja auki.

| # | Muutos | Miksi | Kustannus |
|---|---|---|---|
| 1 | **P1:n imulinjaksi 32 mm (1-1/4"). Käytetään P2:n nykyinen 32 mm:n imuletku (noin 3 m) ja sen säiliöulosotto, kun P2 siirtyy 50 mm:n linjaan.** | Kylmäkäynnistyksen kavitaatioriski poistuu, ja linja saa pidentyä 5 metriin. Osat ovat jo olemassa. **⚠ Edellyttää**, että P2:n 50 mm:n ulosotto tehdään uuteen kohtaan eikä vanhaa suurentamalla; muuten P1 tarvitsee oman 32 mm:n ulosoton. | Pieni: suora 32 mm → 3/4" BSP -liitin suoraan P1:n imuaukkoon |
| 2 | Jos 32 mm ei sovi, **pidä nykyinen 25 mm:n linja enintään 3,2 m:n pituisena** ja käytä HV 32 -öljyä. Älä kierrä konetta yli noin 1800 rpm:n, ennen kuin öljy on lämmennyt (noin 20 °C). | Riittää ilman uusia osia, mutta jättää kylmäkäytölle rajoituksen | Ei mitään |
| 3 | **Täysiaukkoinen palloventtiili** P1:n imu-ulosottoon, ja ulosotto vähintään 50 mm minimiöljypinnan alle eikä paluiden lähelle | Kuristava venttiili tai ilmaa imevä ulosotto syö koko marginaalin | Ei uutta osaa: P2:n nykyisessä imulinjassa säiliön ulosotolla on jo 32 mm:n täysiaukkoinen palloventtiili, joka jää P1:lle [omistaja 2026-10-28] |
| 4 | **HV 32 -öljy** koko järjestelmään (jo suositeltu P2:n takia) | Suurin yksittäinen parannus P1:n imuun kylmänä. Huom. HV 32 ohenee noin 70 °C:ssa alle P1:n 12 cSt:n minimin, joten lämpötilahälytys 70 °C pysyy ([vaatimukset](../requirements.md)). | Öljy vaihdetaan joka tapauksessa |
| 5 | **Imupaineen tarkistus käyttöönotossa:** kiinteä kaksoispainemittari 1G2 (−1…+1,5 bar) mittaritaulussa, mittauspiste P1:n imuaukolla (päätös 2026-10-28; aiemmin alipainemittari −1…0 bar), ja koeajo kylmänä 700 ja 1800 rpm:llä | Laskelma perustuu oletettuun säiliön korkeuteen ja liitinhäviöihin. Mittaus kertoo todellisen marginaalin. | Mittari ~20–40 € (arvio) |
| 6 | **Hihnavälitys:** ~~pienennetäänkö 1:1,15:een~~ **ei muuteta** (päätös 2026-10-23) | P1 pyörii nyt 2400 rpm:llä noin 2980 rpm (raja 3000). Imun kannalta muutos on pieni. | Hihnapyörä |
| 7 | **Hihnaveto, tukilaakeri ja kannake:** ~~uusi ryhmän 2 tukilaakeri ja kannake~~. **Päätetty 2026-11-13:** P1 vaihdetaan ryhmän 3 pumppuun (20 cm³), jolloin **vanha ryhmän 3 tukilaakeri ja kannake käyvät** (mitat täsmäävät [omistaja 2026-11-13]). Hihnojen kireys tarkistetaan yhdelle pumpulle. | Hammaspyöräpumpun akseli ei kestä hihnan sivukuormaa ilman tukilaakeria. Ohjauksen ainoa pumppu, hihnan katkeaminen = ohjaus vain hätäjärjestelmillä | Pumppu 240 €; tukilaakeri ja kannake olemassa |

**Päätetty 2026-10-23: 1 + 3 + 4 + 5** ([päätösloki](../../decisions.md)).
Alkuperäinen suositus: Kohta 1 maksaa lähes vain liittimet, koska letku, säiliön ulosotto ja
sen palloventtiili vapautuvat P2:lta [omistaja 2026-10-28]. Säiliön öljypinta on vähintään 1 m P1:n yläpuolella [omistaja 2026-10-26].

### Tukilaakeri, kannake ja käyttöakseli

Lähtötiedot [omistaja 2026-11-05]:

- P1 oli alun perin asennettu **tandemina** vanhan kiinteätilavuuksisen P2:n (Salami 3PB33D-P38P2)
  perään samalle akselille. Hihnaveto ja tukilaakeri olivat P2:n päässä.
- Vanha P2 oli **ryhmän 3** pumppu ja P1 on **ryhmän 2**, joten vanha tukilaakeri ei sovi P1:lle.
  P1 tarvitsee **uuden tukilaakerin ja sille kannakkeen**.
- P1:n **käyttöakseli on katkaistu** tandem-käyttöä varten, joten se tarvitsee mahdollisesti
  **uuden käyttöakselin**. Tyyppikoodin mukainen kartioakseli 1:8 [datalehti Salami 2PE] ei siis
  välttämättä vastaa pumpun nykyistä akselia (**⚠ tarkista** pumpusta).
- Salami-pumppujen maahantuojana on ainakin aiemmin toiminut **Fluiconnecto**
  (**⚠ tarkista**, onko edelleen).

**Salamin 2PE-luettelon mukaan** [datalehti Salami 2PE -luettelo E0.120.0219.02.00IM04, 2026-11-06]:

- **Akseli on samaa kappaletta vetävän hammaspyörän kanssa.** Uusi akseli tarkoittaa siis uutta
  vetävää hammaspyörää, ei erillistä akselia. Etukantta ja tiivisteitä ei tarvitse vaihtaa
  [omistaja 2026-11-06].
- **Suorat kiila-akselit** (omistajien toive 2026-11-06):

  | Koodi | Akseli | Kiila | Suurin vääntö | Laippa | Laakeroitu laippa |
  |---|---|---|---|---|---|
  | 28 (nykyinen) | kartio 1:8 | – | 130 Nm | P1 | **CP** |
  | **82** | 5/8" SAE A, Ø15,88 mm | 3,97 × 3,97 × 12,7 mm | **70 Nm** | **P1** tai S2 | CS (SAE A) |
  | **85** | 3/4" SAE A, Ø19,05 mm | 4,78 × 4,78 × 12,7 mm | 130 Nm | vain S2 (SAE A) | CS |

- **Vääntötarve** [laskelma, mekaaninen hyötysuhde 90 %]: orbitrolin paineenrajoituksen
  enimmäisasetuksella 170 bar noin **50 Nm**, normaalilla alle 50 barin työpaineella alle 15 Nm.
  Akseli 82 (70 Nm) riittää, kunhan piirin paine ei voi nousta yli noin 230 barin.
- **Salamin oma laakeroitu laippa** (outrigger bearing) korvaa pumpun etulaipan, ja hihnapyörä
  tulee suoraan pumpun akselille. Eurooppalaisella laipalla (CP) se on saatavana vain
  kartioakselille 28; kiila-akselille tarvitaan SAE A -laippa (CS). Luettelon esimerkki:
  1700 N:n säteiskuorma 7,5 mm:n päässä laipasta, 2000 rpm → noin 1000 h ([laskelma] hihnan
  voimista **⚠ ei tehty**).
- **Erillinen ryhmän 2 tukilaakeriyksikkö ja uraholkki sopivat akselille 28.** Akseli 28:
  kartio 1:8, Ø16,6 mm, kierre M12 × 1,25, Woodruff-kiila 3,165 × 6,5 mm [datalehti Salami 2PE s. 14].
  Myynnissä olevat ryhmän 2 uraholkit on tehty juuri tälle akselille: 14 hammasta ulkona,
  1:8-kartioreikä ja 3,2 mm:n kiila, tukilaakerien SU2/C ja SU2/D väliin
  ([Kailatec](https://kauppa.kailatec.fi/tuote/hammaspyorapumpun-ja-tukilaakerin-valinen-hammaspyora/),
  [Lakeuden Hydro](https://www.lakeudenhydro.fi/fi/hydrauliikkakomponentit/hydraulipumput/c/1/),
  [HTL B-2CA](https://www.htluk.co.uk/Products/002c000c0001/B-2CA); hakutuloksista 2026-11-06,
  sivuja ei luettu). Tukilaakereiden pumppulaippa on eurooppalainen (71,5 × 96, keskitys Ø36,5)
  ([EP-hydrauliikka](https://www.ep-hydrauliikka.fi/tuote/tukilaakeri-2-sarjan-pumpulle)), ja se
  vastaa Salamin P1-laippaa. **Suora kiila-akseli (82 tai 85) ei sovi uraholkkiin.** Kiila-akseli
  on tukilaakerin lähtöpuolella, ja hihnapyörä tulee siihen.
- **Vaihtoehto:** erillinen laakeripukki ja joustava kytkin (Salami suosittaa Oldham-kytkintä).
  Silloin pumpun akselille ei tule sivukuormaa, ja akselin 82 ja nykyisen P1-laipan voi pitää.

Ehdotus:

1. Selvitä pumpusta, onko akselin pää kartio, ura vai lyhennetty, ja sopiiko se ryhmän 2
   tukilaakerin kytkentään.
2. Pyydä Fluiconnectolta (tai muulta Salami-myyjältä) tarjous **ryhmän 2 tukilaakerista** (ja
   sopivasta akselista tai kytkimestä) sekä **vertailuksi uudesta 2PE16-pumpusta** valmiilla
   akselilla. Jos akseli pitää vaihtaa, pumpun purku ja koestus voi tulla lähes uuden pumpun
   hintaiseksi; hinnat **⚠ ei tiedossa**.
3. Kannake tehdään tai sovitetaan uudelle tukilaakerille. Vanhan kannakkeen voi ehkä muokata,
   jos sen kiinnitys koneeseen sopii (**⚠ tarkista** veneellä).
4. Vanha ryhmän 3 tukilaakeri jää käyttämättä (voi myydä, jos sille ei löydy käyttöä).

### Uuden P1:n kierrostilavuus

Vanhaan pumppuun ei saa uutta akselia, joten P1 vaihdetaan uuteen [omistaja 2026-11-12].
Laskelma nykyisellä välityksellä 1:1,24 [laskelma; tyhjäkäynti 700 rpm on arvio, volumetrinen
hyötysuhde 92 %, kierrosrajat datalehti Salami 2PE s. 6]:

| Koko | Suurin kierrosluku | Tuotto, kone 700 rpm (P1 870 rpm) | Tuotto, kone 2400 rpm (P1 2980 rpm) | Virtausnopeus 32 mm:n imuletkussa 2400 rpm:llä |
|---|---|---|---|---|
| 2PE 13,8 | 3500 rpm | 11,0 l/min | 37,8 l/min | 0,78 m/s |
| **2PE 16 (16,6 cm³)** | 3000 rpm | **13,3 l/min** | 45,4 l/min | 0,94 m/s |
| 2PE 19 (19,4 cm³) | 3000 rpm | 15,5 l/min | 53,1 l/min | 1,10 m/s |

- **Suositus ryhmän 2 pumpuksi: 16,6 cm³** (ei valittu; ks. ryhmän 3 vaihtoehto alla). Tyhjäkäynnillä 13,3 l/min riittää pyörittämään
  orbitrolia (158,4 cm³/r) noin 80 kierrosta minuutissa, ja kaikki imu- ja kierroslaskelmat
  pysyvät ennallaan.
- 19,4 cm³ toisi tyhjäkäynnille noin 2 l/min lisää, mutta imuletkun virtausnopeus ylittää
  suosituksen 1 m/s suurilla kierroksilla, kierrosraja on sama 3000 rpm, ja jatkuva paine on
  220 bar. Hyöty on pieni.
- 13,8 cm³ antaisi kierrosmarginaalia (raja 3500 rpm), mutta tyhjäkäynnin tuotto putoaa noin
  11 l/min:iin ja ohjaus hidastuu satamassa.
- Orbitrolin nimellisvirtaus 16 l/min saavutettaisiin tyhjäkäynnillä vasta noin 20 cm³:llä, jota
  2PE-sarjassa ei ole 3000 rpm:n rajalla.
- Akseliksi kartio 1:8 (Salamin koodi 28) ja eurooppalainen laippa, jotta ryhmän 2 tukilaakeri ja
  uraholkki sopivat. Muunkin valmistajan ryhmän 2 pumppu käy, jos koko, akseli, laippa,
  pyörimissuunta ja suurin kierrosluku (≥ 3000 rpm) täsmäävät.

#### Vaihtoehto: ryhmän 3 pumppu 20 cm³ (valittu 2026-11-13)

**Päätetty 2026-11-13: tämä vaihtoehto ([päätösloki](../../decisions.md)).** Vanhan P2:n laippa ja akseli täsmäävät [omistaja 2026-11-13].

Pienin ryhmän 3 koko on noin 20 cm³ (Salami 3PE-21: 20,6 cm³, 3000 rpm [datalehti Salami 2PE -luettelo s. 7]).
Etu: **vanha ryhmän 3 tukilaakeri ja kannake voivat sopia**, jos vanhan P2:n laippa ja akseli ovat
eurooppalaista ryhmän 3 standardia (**⚠ tarkista** vanhasta pumpusta: pulttijako 98,4 × 128,1 mm,
ohjuri Ø50,8 mm, kartio 1:8, kiila 4 mm).

Ehdokas: [Hydrauliikkakauppa.fi 30C20X146](https://www.hydrauliikkakauppa.fi/tuote/hammaspyorapumppu-3-sarja-25-cm%c2%b3-laippaliitanta/), 20 cm³, 3000 rpm, kartio 1:8 ja 4 mm:n kiila,
pulttijako 98,4 × 128,1, ohjuri Ø50,8; 240 € (alv 0 %: 191,24 €), varastossa [datalehti
Hydrauliikkakauppa.fi 2026-11-12]. Valmistaja, paineet ja imuaukon koko **⚠ ei tiedossa**.

| Koko | Tuotto, kone 700 rpm | Tuotto, kone 2400 rpm | Imuletkun nopeus (32 mm) | Imupaine kylmänä (5 °C), 32 mm × 3,2 m, HVLP 32 |
|---|---|---|---|---|
| 2PE 16,6 cm³ | 13,3 l/min | 45 l/min | 0,94 m/s | −0,15 bar |
| **3-sarja 20 cm³** | **16,0 l/min** | 55 l/min | 1,14 m/s | noin −0,22 bar (arvio) |
| 3-sarja 25 cm³ | 20,0 l/min | 68 l/min | 1,41 m/s | noin −0,33 bar (arvio), **yli Salamin −0,3 barin rajan** |

[laskelma: välitys 1:1,24, volumetrinen hyötysuhde 92 %; imupaine skaalattu 16,6 cm³:n laskelmasta,
oletuksena sama 3/4":n imuaukko, joten ryhmän 3 isommalla aukolla tulos on parempi. Ryhmän 3
pumpun oma imupaineraja **⚠ ei tiedossa**.]

- **20 cm³ sopii:** orbitrolin nimellisvirtaus 16 l/min täyttyy tyhjäkäynnillä, ja imu pysyy rajan
  sisällä 3,2 m:n letkulla. Imulinjaa ei pidä pidentää 5 metriin.
- **25 cm³ on liian suuri:** imu menee kylmänä suurilla kierroksilla rajan yli, ja ohjaus ei
  tarvitse lisää virtausta.

### Vikatilanteet (ohjaus)

| Vika | Seuraus | Suoja |
|---|---|---|
| Imulinjan kavitaatio (kylmä öljy, liian pieni tai pitkä letku, kiinni jäänyt palloventtiili) | Ohjaus raskas tai nykivä, pumppu kuluu, pahimmillaan pumppu rikkoutuu | 32 mm:n linja, HV 32, täysiaukkoinen venttiili, imupainemittaus käyttöönotossa |
| Imulinjan palloventtiili unohtuu kiinni | P1 käy kuivana ja rikkoutuu, ohjaus menetetään | Venttiilin asennonosoitin tai lukitus auki-asentoon, käynnistyksen tarkistuslista |
| Hihnan katkeaminen | Ohjaus vain orbitrolilla käsipumppuna (raskas) tai hätäpinnalla | Varahihna, P3-varapumppu (kytkentä **⚠ tarkista**) |
| Tukilaakeri tai kannake pettää, tai akselikytkentä irtoaa | Hihna löystyy tai pumppu pysähtyy; sivukuorma voi rikkoa P1:n akselin tai laakerit; ohjaus menetetään | Oikean ryhmän (2) tukilaakeri, jäykkä kannake, akselin ja kytkennän tarkistus; P3-varapumppu; pätevän henkilön tarkistus ennen käyttöönottoa |

## Avoimet kysymykset

- [x] P1:n imuaukon koko: 3/4" [omistaja 2026-10-23]
- [x] Säiliön öljypinnan korkeus suhteessa P1:n imuaukkoon: vähintään 1 m [omistaja 2026-10-26]
- [x] P2:n vanha 32 mm:n imuletku mahtuu P1:lle; pumpun päähän tarvitaan uusi letkukara/letkuliitin [omistaja 2026-10-23]
- [x] Päätös: P1:n imulinja 32 mm (2026-10-23)
- [x] 32 mm:n täysiaukkoinen palloventtiili: on jo P2:n nykyisessä imulinjassa säiliön ulosotolla, jää P1:lle [omistaja 2026-10-28]
- [ ] Säiliö: P2:n 50 mm:n ulosotto uuteen kohtaan, jotta vanha 32 mm:n ulosotto jää P1:lle
- [ ] Hankinta: uusi 32 mm:n letkukara + 3/4" BSP -liitin P1:n imuaukkoon (vanhaan letkuun) ja 3/4" T-kappale 1/4"-sivuaukolla mittausta varten (ks. [pressure-monitoring](pressure-monitoring.md#imupaineen-mittaus)) ja kaksoispainemittari 1G2 (−1…+1,5 bar) mittaritauluun, ks. [hankintalista](../procurement.md)
- [x] Hihnavälitys pysyy 1:1,24 (päätös 2026-10-23)
- [x] Tukilaakeri: vanha oli ryhmän 3 P2:n, ei sovi P1:lle; tarvitaan uusi ryhmän 2 tukilaakeri ja kannake [omistaja 2026-11-05]
- [x] ~~P1:n käyttöakseli: katkaistu tandem-käyttöä varten; tukilaakeriyksikön uraholkkiin sopii alkuperäinen **akseli 28** (kartio 1:8, kiila 3,2 mm); suora kiila-akseli ei sovi (2026-11-06). Tarvitaan vetävä hammaspyörä akselilla 28~~ uusi pumppu (päätös 2026-11-13)
- [x] Tukilaakeri: vanha ryhmän 3 tukilaakeri käytetään (päätös 2026-11-13)
- [x] ~~Tarjous vetävästä hammaspyörästä (akseli 28), vertailuksi uudesta 2PE16D-P28P1:stä sekä ryhmän 2 tukilaakerista ja uraholkista: kysely lähetetty Fluiconnectolle 2026-11-06 [omistaja 2026-11-06]. **Vanhaan pumppuun ei saa uutta akselia, joten hankitaan uusi P1** [omistaja 2026-11-12], ks. [Uuden P1:n kierrostilavuus](#uuden-p1n-kierrostilavuus)~~ ei tarvita (päätös 2026-11-13)
- [x] Kannake: vanha käytetään (päätös 2026-11-13)
- [x] Uuden P1:n liitännät ja paine: laippaliitännät, laipat vanhasta P2:sta; max 250 bar, riittää orbitrolin paineenrajoitukselle (enintään 170 bar) [omistaja 2026-11-13]
- [ ] Uuden P1:n imupaineraja ja pienin viskositeetti: kysy myyjältä
- [ ] P1:n painelinja: jos käytetään vanha 3/4":n P-linja, tarvitaan sovitenippa [omistaja 2026-11-13]; linja on myös suunniteltu P2:lle ([hankintalista 3.2 ja 6.10](../procurement.md))
- [ ] Imupaineen mittauspiste 1G2 imulaippaan (mittausaukko tai välikappale), kun 3/4":n T-kappaletta ei enää käytetä
- [ ] Vanhan tukilaakerin uraholkki: tarkista kunto ja sopivuus uuden pumpun akseliin (kartio 1:8, kiila 4 mm). Käytetty vain noin 100 h [omistaja 2026-11-13]
