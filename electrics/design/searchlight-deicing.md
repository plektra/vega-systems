# Hakuvalon jäänpoisto

> **Tila:** Selvitys, aloitettu 2026-10-30, päivitetty 2026-10-31 (polttimo on Philipsin 250 W:n projektorihalogeeni, ei 500 W; aiemmin 2026-10-30: valo on halogeeni,
> käsikäyttöinen ja komentosillan katolla; lasin halkaisija noin 350 mm; jäänpoisto siirretty
> ESP32-PDM:stä tähän; etulasi on lasia; runko ja halogeeni säilyvät, LED hylätty). **Päätetty
> 2026-10-30:** halogeeni ja vaihtoehto A. Hinnat ja tehot on haettu verkosta, eikä niitä ole tarkistettu
> valmistajilta.

**Jatka tästä (2026-10-30):** **päätetty:** vanha runko säilyy, polttimo pysyy halogeenina, ja
LED-vaihto jätetään pois [omistaja 2026-10-30, [decisions.md](../../decisions.md)]. Jäänpoisto
hoidetaan ilman lämmitintä (A): suojahuppu, lasi pois tuulesta ja valo päälle hetkeä ennen
tarvetta. Kokeillaan ensimmäisellä pakkasajolla. Seuraavaksi: (1) varmista polttimon merkinnästä tyyppi (luultavasti
EHJ / A1/223, kanta G6.35) ja hanki varapolttimoita, koska polttimon käyttöikä on vain noin 50 h; (2) halogeenin käynnistysvirta PDM-kortilla
(ESP32-PDM:n päätös 19) tai releellä; (3) suojahuppu. Kaikki avoimet kysymykset: kohta 5.

Tavoite: hakuvalon pitää toimia myös syksyllä ja keväällä, kun etulasiin ja kääntömekanismiin
tarttuu jäätä, räntää tai jäätyvää roisketta. LED-vaihdolla haettiin myös kirkkaampaa keilaa, mutta
vanha runko halutaan säilyttää, joten LED jätettiin pois (kohta D).

**Lähtötiedot:**

| Tieto | Arvo | Lähde |
|---|---|---|
| Jännite ja teho | 24 V, **250 W** (noin 10,4 A [laskelma]); aiemmin kirjattu 500 W oli virhe | [omistaja 2026-10-31] |
| Tila | olemassa, ei asennettu | [omistaja 2026-10-29] |
| Valmistaja ja malli | ei tyyppikilpeä; hyvin vanha, todennäköisesti valmistettu Neuvostoliitossa vuosikymmeniä sitten | [omistaja 2026-10-30] |
| Polttimo | **Philipsin 24 V:n 250 W:n halogeeni, jota käytetään projektoreissa ja piirtoheittimissä** [omistaja 2026-10-31]; pystyssä oleva polttimo, jonka kaksi ohutta nastaa menevät kantaan [omistaja 2026-10-30]. Todennäköisesti **Philips 7748XHP** eli ANSI **EHJ** / LIF **A1/223**, kanta **G6.35**: 3400 K, noin 10 000 lm, käyttöikä noin 50 h ([datalehti Philips 7748XHP](https://old.effex.ee/certificate/7748xhp.pdf)). Tyyppi **⚠ tarkista** polttimon merkinnästä | [omistaja 2026-10-31], [datalehti Philips 7748XHP] |
| Runko | säilytetään: sopii aluksen vanhaan tyyliin ja muotokieleen | [omistaja 2026-10-30] |
| Sijainti | komentosillan katto | [omistaja 2026-10-30] |
| Ohjaus | käsikäyttöinen: valaisinta käännetään katon läpi tulevalla vivulla | [omistaja 2026-10-30] |
| Etulasin paksuus | noin 5 mm | [omistaja 2026-10-30] |
| Etulasin halkaisija | noin 350 mm, **arvio**; omistaja mittaa tarkemmin | [omistaja 2026-10-30] |
| Etulasin materiaali | lasi, oletettavasti karkaistu: lasi on kestänyt halogeenin lämmön käytössä vuosikymmeniä (päättely, ei merkintää lasissa) | [omistaja 2026-10-30] |

**ESP32-PDM:** jäänpoisto ei enää kuulu ESP32-PDM-projektiin, vaan sitä käsitellään vain tässä
selvityksessä (ESP32-PDM:n päätös 16 on merkitty siirretyksi) [ESP32-PDM 2026-10-30]. PDM:ään
liittyy edelleen **päätös 19 (ehdotus):** päätös tehtiin noin 21 A:n (500 W) hakuvalolle. Polttimo on
kuitenkin 250 W eli noin 10,4 A [omistaja 2026-10-31], joten vaatimukset keventyvät (ks. kohta 3).
Alkuperäinen perustelu: hakuvalo vaatii suurivirtaiseen
`pdm-hc2`-korttiin pienemmän resistanssin MOSFETit (ehdokas onsemi NTMFS5C612NL). **Halogeenin
käynnistysvirta** on noin 10–15-kertainen kymmenien millisekuntien ajan, joten kortin 80 A:n nopea
oikosulkulaukaisu katkaisisi kylmän 500 W:n polttimon (250 W:lla käynnistysvirta on noin 100–160 A, ks. kohta 3). Vaihtoehdot: LED-hakuvalo tai nopean
laukaisun poisto MOSFETien pulssikestoisuuden (SOA) tarkistuksen jälkeen
([design-notes.md §4a](https://github.com/plektra/ESP32-PDM/blob/main/docs/design-notes.md)) [ESP32-PDM 2026-10-30].
Halogeeni vai LED ratkaisee siis sekä jäänpoiston että PDM-kortin osavalinnan.

## 1. Polttimon tyyppi ratkaisee

Jäätyykö lasi ylipäätään käytön aikana, riippuu siitä, missä lampun hukkalämpö syntyy:

| Polttimo | Mihin hukkalämpö menee | Pysyykö etulasi sulana valon palaessa? |
|---|---|---|
| **Halogeeni** (Vegan nykyinen) | Lähes kaikki 250 W:sta on lämpöä, ja se säteilee heijastimesta suoraan etulasiin | **Kyllä, käytännössä.** Polttimo sulattaa lasin itse, kun valo on päällä [laskelma, perustelu alla] |
| **LED** | Lämpö johdetaan LEDien takana olevaan jäähdytysrivoitukseen | **Ei.** Etulasi on lähes ulkoilman lämpöinen, ja jää ja huurre jäävät lasiin |

**Perustelu halogeenille [laskelma, arvio]:** halogeenipolttimon näkyvän valon hyötysuhde on
luokkaa 2–3 % sähkötehosta (yleinen tieto halogeenilampuista, **⚠ tarkista**), joten noin 245 W
250 W:sta on lämpöä. Jos lasi pidettäisiin sulana erillisellä lämmittimellä, Ø 350 mm:n lasiin
tarvittaisiin noin 15–50 W (kohta C4). Polttimon hukkalämpö on siis noin 5–15-kertainen (päivitetty 2026-10-31: polttimo on 250 W eikä 500 W; johtopäätös pysyy).
**Tekniikan vertailua:** Carlisle & Finchin halogeenihakuvaloissa jäänestolämmitin on vain
*moottoroidun jalustan* sisällä, ei etulasissa ([19" halogen searchlight](https://carlislefinch.com/searchlights/19-inch-halogen-searchlight/),
[10" LED -datalehti](https://carlislefinch.com/wp-content/uploads/2024/03/10-inch-LED-7.Pg-C.pdf)).
Sama valmistaja ei siis lämmitä halogeenimallien lasia erikseen.

**Kaksi eri ongelmaa:**

1. **Etulasin jää ja huurre:** valo ei pääse läpi.
2. **Kääntömekanismin jäätyminen:** Vegan valossa kääntövipu tulee katon läpi. Vipu ja sen laakeri
   ovat komentosillan sisällä lämpimässä, joten jäätymisvaara on lähinnä katon läpivienti ja
   valaisimen nivel katon päällä **⚠ tarkista veneellä**.

## 2. Vaihtoehdot

### A. Ilman lämmitintä: suojahuppu, esilämmitys ja pinnoite (halvin, suositus halogeenille)

- **Suojahuppu** (kangas tai muovi) lasin eteen, kun valoa ei käytetä. Huppu pitää lasin ja
  usein myös nivelen kuivana. Hinta muutamia kymmeniä euroja, voi tehdä itse **⚠ arvio**.
- **Kääntäminen pois tuulesta / lasi alaspäin** pysäköintiasennossa vähentää roiskeen
  tarttumista, jos jalusta sen sallii **⚠ tarkista veneellä**.
- **Halogeenivalo päälle hetki ennen tarvetta:** lasi sulaa itsestään. Kuinka kauan paksun jään
  sulaminen kestää, on **⚠ ei tiedossa**; kokeillaan veneellä.
- **Vettä hylkivä lasipinnoite** (tuulilasien sadepinnoitteiden tapaan) vähentää jään
  tarttumista, mutta ei estä jäätymistä. Apukeino, ei ratkaisu. Sopii Vegan valoon, koska etulasi
  on lasia [omistaja 2026-10-30].

**Varoitus lämpöshokista:** jos paksusti jäätyneeseen lasiin sytytetään 250 W:n halogeeni, lasi
lämpenee epätasaisesti. Nykyaikaisten hakuvalojen etulasit ovat yleensä karkaistuja (esim. Den
Haan Rotterdam ilmoittaa "hardened front glass", toiminta −25 °C:seen asti:
[DHR 230DS](https://www.dhr.nl/sites/default/files/userfiles/Producten/Searchlights/Downloads/A00DOC-ZL0003%20-%20RevB.pdf)).
Vegan valon etulasi on lasia ja oletettavasti karkaistu, koska se on kestänyt halogeenin lämmön
käytössä vuosikymmeniä [omistaja 2026-10-30]. Valmistajan tietoa ei ole, ja lämpöshokin kesto
paksusti jäätyneessä lasissa on yhä varmistamatta. Kohtuullinen varovaisuus riittää: jos jäätä on
paljon, poista paksuin kerros ensin käsin. Tarkista, onko lasissa halkeamia tai lohkeamia
reunoissa, sillä vaurio heikentää karkaistua lasia.

### B. Lämmitin jalustaan tai runkoon (kääntömekanismin jäänesto)

**Vegalle luultavasti tarpeeton:** valo on käsikäyttöinen, ja kääntövipu ja sen laakeri ovat
komentosillan sisällä. Jos katon läpivienti tai valaisimen nivel jäätyy kiinni, lämmitin voidaan
lisätä myöhemmin.

Valmistajien oma tapa: termostaatilla ohjattu lämmitin jalustassa (Carlisle & Finch, ks. yllä;
valmistajan 24 V:n DC-lämmitintä ei löytynyt, sivuilla mainitaan vain 115 VAC ja 230 VAC).

Jälkiasennuksena sopii **itsesäätyvä PTC-lämmitin**, joka ei tarvitse erillistä termostaattia
eikä ylilämpösuojaa. Esimerkki: **DBK Enclosures FG14756.1**, 20 W, 24 V AC/DC, 40 × 8,5 × 35 mm,
VDE/UL/CSA ([RS 299-5893](https://uk.rs-online.com/web/p/heating-elements/2995893)). Kiinnitys on
tarkistettava datalehdestä; liimakiinnitystä ei mainita.

- Virta 20 W / 24 V ≈ **0,8 A** [laskelma]; mahtuu hakuvalon omaan piiriin tai pieneen
  omaan sulakkeeseen.
- Energia: jos lämmitin on päällä 8 h ajovuorokaudessa, 0,16 kWh; koko vuorokauden 0,48 kWh
  [laskelma]. Ankkurissa se kannattaa kytkeä pois.

### C. Etulasin lämmitys (tarpeen vain, jos valo vaihdetaan LEDiin)

| Tapa | Miten | Teho **⚠ arvio** | Huomiot |
|---|---|---|---|
| **C1. Lämmitin lasin reunaan** | Silikonilämmitysnauha tai PTC-elementti lasin kehyksen sisäpuolelle | noin 10–30 W | Halvin ja yksinkertaisin, mutta **ei riitä**: Ø 350 mm:n lasissa reunan lämpö ulottuu vain muutaman senttimetrin päähän (laskelma alla). Valon tiiviys (IP) on palautettava avauksen jälkeen |
| **C2. Läpinäkyvä lämmityskalvo lasin sisäpintaan** (ITO tai metalliverkko) | Kalvo liimataan lasiin ja kytketään 24 V:iin | noin 50 W Ø 350 mm:n lasiin (500 W/m²) [laskelma] | Bopla ilmoittaa kalvolleen enintään 3000 W/m², +85 °C ja läpäisyn enintään 93 % ([Bopla, transparente Folienheizung](https://www.bopla.de/fileadmin/user_upload/Transparente_Folienheizung-EN_web.pdf)); 24 V:n valmista liimakalvoa ei löytynyt. **Ei sovi halogeenivaloon**, koska lasi kuumenee yli 85 °C:n **⚠ tarkista**. Läpäisy vähentää valoa muutaman prosentin. Hinta **⚠ ei tiedossa** |
| **C3. Valmis lämmitetyllä ikkunalla varustettu valo** | Esim. **Glamox SL1IR / SL2IR** (LED + lämpökamera, lämmitetty ikkuna) ([SL1IR](https://citimarinestore.com/en/glamox-marine-lightning/22177-glamox-sl1ir-led-searchlight-with-thermal-night-vision.html), [SL2IR](https://citimarinestore.com/en/glamox-marine-lightning/22171-glamox-sl2ir-led-searchlight-with-integrated-thermal-camera.html)) | **⚠ ei tiedossa** | Kallis, ja nykyinen valo jäisi käyttämättä. SL2IR:n jännite ei selvinnyt. Mukana lämpökamera, josta voi olla hyötyä muutenkin |

**Etulasi:** paksuus noin 5 mm, halkaisija noin 350 mm (arvio) [omistaja 2026-10-30]. Pinta-ala
π · 0,175² ≈ **0,096 m²** [laskelma].

**Miksi reunarengas ei riitä [laskelma, arvio]:** lasi johtaa lämpöä huonosti, joten reunalta
tuleva lämpö ehtii karata lasin ulkopintaan ennen kuin se kulkee kauas keskelle. Lämmön
tunkeutumismatka reunasta on noin 1/m, jossa m = √(h / (k · t)):

| Ulkopinnan lämmönsiirto h | m | Tunkeutumismatka 1/m |
|---|---|---|
| 10 W/(m²·K), tyyni | noin 45 1/m | noin 22 mm |
| 30 W/(m²·K), tuuli ja roiske | noin 77 1/m | noin 13 mm |

Oletukset: lasin lämmönjohtavuus k ≈ 1,0 W/(m·K), paksuus t = 5 mm, lämpö karkaa vain
ulkopinnasta (sisäpuolen ilma ja polttimon lämpö jätetty huomiotta), h-arvot ovat arvioita.
Reunan lämpötilaero on noin 1/e eli noin 37 % jäljellä 1/m:n päässä reunasta, ja noin 5 % kolmen
tunkeutumismatkan päässä. Ø 350 mm:n lasissa (säde 175 mm) reunarengas sulattaa tuulessa vain
noin 2–4 cm leveän kehän, ja noin 27–31 cm:n keskusta jää jäähän. Lämpö on tuotava koko lasin
pinnalle (puhallin C4 tai kalvo C2). Sama johtopäätös oli ESP32-PDM:n päätöksessä 16 ennen kuin
aihe siirrettiin tähän.

### C4. Pieni lämpöpuhallin rungon sisällä (LED-valo)

Puhallin puhaltaa lämmintä ilmaa etulasin **sisäpintaan**. Toisin kuin reunarengas, se lämmittää
koko lasin pinnan, koska 5 mm:n lasi on lämmölle ohut seinä: sen lämpövastus on noin
0,005 m²·K/W eli vain noin kuudesosa pinnan ilmavastuksesta (noin 0,033 m²·K/W, kun h ≈ 30 W/(m²·K))
[laskelma, oletukset kuten yllä]. Puhallin mahtuu omistajan arvion mukaan runkoon niin, ettei se
peitä liikaa valokeilaa [omistaja 2026-10-30].

**Tarvittava ilman lämpötila lasin sisäpinnalla, jotta ulkopinta pysyy 0 °C:ssa [laskelma, arvio]:**

| Olosuhde | Lasin läpi kulkeva lämpö | Ilma lasin sisäpinnalla | Teho Ø 350 mm:n lasiin |
|---|---|---|---|
| −5 °C, tuuli (h ulkona 30) | noin 150 W/m² | noin +6 °C | noin 15 W |
| −10 °C, kova tuuli ja roiske (h ulkona 50) | noin 500 W/m² | noin +19 °C | noin 50 W |

Oletukset: sisäpinnan h ≈ 30 W/(m²·K) puhaltimen kanssa, lasin halkaisija noin 350 mm (arvio).
**Lisäksi osa tehosta karkaa metallirungon kautta**, joten lämmittimen kokonaisteho on arviolta
**50–100 W** (aiemmin 20–40 W, kun lasin oletettiin olevan Ø 200 mm). Yksi 20–40 W:n
kytkinkaappipuhallin ei siis riitä kovimpiin olosuhteisiin; tarvitaan esim. 50 W:n elementti ja
puhallin tai kaksi puhallinta. Ilmavirta kannattaa suunnata suoraan lasiin. Paksun jään
sulattaminen vie selvästi enemmän; tämä on jäätymisen estoon, ei jäälohkareen sulattamiseen.
Virta 50–100 W / 24 V ≈ 2–4 A [laskelma].

**LEDin oma hukkalämpö:** LED-valon sähkötehosta suurin osa on lämpöä LEDien takana
(osuus **⚠ tarkista** valitun valon datalehdestä). Jos sama puhallin kierrättää rungon sisällä
ilmaa jäähdytysrivoituksesta lasille, valo pitää lasinsa sulana palaessaan lähes ilmaiseksi, ja
erillistä lämmitintä tarvitaan vain, kun valo on sammuksissa. Tämä onnistuu, jos runko on
suljettu ja rivoitus on sen sisällä; jos rivoitus on ulkona, lämpö menee ulkoilmaan.

**Valmiita 24 V:n PTC-lämpöpuhaltimia** (kytkinkaappeihin):

| Tuote | Tiedot | Lähde |
|---|---|---|
| Omega FCH -sarja | 20 W ja 40 W, 24 V AC/DC, PTC-keraaminen vastus, puhallin voi käydä ilman lämmitystä, käyttö enintään +70 °C | [Omega, kotelolämmittimet](https://www.omega.com/en-us/industrial-heaters/duct-and-enclosures-heaters/c/enclosure-heaters?view=list), [FCH](https://www.omega.co.uk/pptst/fch-fgc0.html) |
| DBK (Cirrus-tyyppi) | 20 W, puhaltimelle oma piiri (24 V DC); RS:n listaama malli on 12 V DC, 72 × 27 × 27 mm | [RS 415-2931](https://uk.rs-online.com/web/p/products/4152931) |
| DBK FG14756.1 / 50 W -malli | 20 W tai 50 W, 24 V AC/DC, ilman puhallinta (johtuminen); voidaan yhdistää erilliseen pieneen 24 V:n puhaltimeen | [RS 299-5893](https://uk.rs-online.com/web/p/heating-elements/2995893), [RS 299-5900](https://uk.rs-online.com/web/p/heating-elements/2995900) |

Hinnat **⚠ ei tiedossa**.
**Ei sovi halogeenivalon runkoon:** puhaltimet on tarkoitettu enintään noin +70 °C:seen, ja
halogeenivalon runko kuumenee sisältä tätä kuumemmaksi **⚠ tarkista**.

Puhallin pitää myös rungon sisäilman kuivana, mikä vähentää lasin sisäpuolen huurtumista.

### D. Halogeeni vai LED

> **Päätetty 2026-10-30: halogeeni säilyy, LED hylätty.** Vanha runko säilytetään, koska se sopii
> aluksen vanhaan tyyliin ja muotokieleen [omistaja 2026-10-30]. Kirkkaampi keila olisi
> todennäköisesti vaatinut kokonaan uuden LED-valon, joten LED jätetään toistaiseksi pois. Alla
> oleva vertailu jää taustatiedoksi.

**Tavoite: kirkkaampi ja pidemmälle kantava keila** [omistaja 2026-10-30]. Kantaman ratkaisee
keilan keskikohdan **valovoima (kandela, cd)**, ei wattimäärä eikä lumenit. Valovoima riippuu
valolähteen kirkkaudesta ja koosta suhteessa heijastimeen tai linssiin: mitä pienempi ja
kirkkaampi valolähde, sitä kapeampi ja pidemmälle kantava keila [yleinen optiikka].

- **250 W:n projektorihalogeeni (noin 10 000 lm) Ø 350 mm:n heijastimessa on jo luultavasti voimakas valo.** Sen valovoima
  on **⚠ ei tiedossa**; se mitataan ennen kuin LED-vaihtoehtoja verrataan (alla).
- **LED-polttimo vanhaan heijastimeen ei todennäköisesti lisää kantamaa.** Heijastin on muotoiltu
  pienelle hehkulangalle, ja LED-sirujen valoa säteilevä pinta on eri kokoinen, eri muotoinen ja
  säteilee eri suuntiin. Tulos on yleensä leveämpi ja lyhyempi keila **⚠ tarkista**
  polttimon valmistajan keilatiedoista. Neuvostovalmisteiseen kantaan valmista polttimoa voi olla
  myös vaikea löytää.
- **Kirkkaampi keila saadaan varmimmin kokonaan uudella LED-hakuvalolla,** jonka optiikka on
  suunniteltu LEDeille ja jonka valovoima on ilmoitettu datalehdessä. Vertailukohtia alla
  (Golight, Luminell). Silloin myös jäänpoisto valitaan valon mukaan: osassa malleista on
  lämmitetty ikkuna (C3); muuten lasi lämmitetään (C4 tai C2).
- **Nykyisen valon valovoiman mittaus:** puhelimen luksimittarisovellus (tai luksimittari) keilan
  keskelle tunnetulle etäisyydelle d, pimeällä. Valovoima I = E · d², jossa E on luksit.
  Esimerkki: 40 lx 50 m:n päässä → 40 · 50² = 100 000 cd [laskelma, esimerkkiluvut].
  Etäisyyden pitää olla vähintään noin 10–20 m, jotta keila on muodostunut **⚠ arvio**; mittaa
  useasta kohdasta ja ota suurin arvo. Puhelinsovellusten tarkkuus on karkea, mutta riittää
  vertailuun.

- **Energiatehokkuus:** LED tuottaa samalla teholla moninkertaisesti valoa (yleinen tieto,
  luokkaa 3–5 ×, **⚠ tarkista** valittavista malleista). Esimerkiksi 50–80 W:n LED voi antaa
  saman valovirran kuin 250 W:n halogeeni, eli noin 2–3 A eikä 10,4 A [laskelma, arvio].
- **Kantama riippuu valovoimasta (kandela), ei watteista.** Halogeenin pieni hehkulanka ja
  paraboloidiheijastin antavat kapean ja pitkän keilan; LEDin keila riippuu sen optiikasta.
  Valmistajien väitteitä: Golight Stryker LED 410 000 cd (noin 1 280 m) vs. halogeeni 200 000 cd
  (noin 890 m) ([CCJ](https://www.ccjdigital.com/products/product/14938704/golights-remote-control-searchlights)).
  Järeä LED-esimerkki: Luminell SLX D G3, enintään 500 W, 24 V DC (22–30 V), 1 luxin kantama
  enintään 2 000 m ([citimarinestore](https://citimarinestore.com/en/glamox-marine-lightning/22186-luminell-slx-d-g3-searchlight-modules.html)).
  Vertaa kandeloita datalehdistä.
- **LED-polttimo nykyiseen runkoon:** esim. Den Haan Rotterdamin hakuvaloihin myydään
  LED-polttimoita alkaen 369 € ([Toplicht](https://www.toplicht.de/en/commercial-shipping/search-lights/3542/led-bulbs-for-searchlights-dhr)).
  Ne on tehty DHR:n omiin runkoihin. Vegan valo on vanha neuvostovalmisteinen, joten
  sopivan LED-polttimon löytyminen riippuu kannasta (**⚠ ei tiedossa**, omistaja selvittää).
  Halogeeniheijastimeen sovitettu LED ei välttämättä anna yhtä kapeaa keilaa **⚠ tarkista**.
- **PDM-kortti:** LED poistaisi käynnistysvirtaongelman (ESP32-PDM:n päätös 19); 2–3 A mahtuu
  kevyempään kanavaan.
- **Jäänpoisto:** halogeeni sulattaa lasin itse; LED tarvitsee lämpöpuhaltimen (C4, arviolta
  50–100 W) tai kalvon (C2, noin 50 W), ellei uudessa valossa ole valmiiksi lämmitettyä ikkunaa.
- **Ulkonäkö:** uusi LED-valo korvaa vanhan valaisimen. Säilytetäänkö vanha valaisin, on omistajien
  päätös (**⚠ ei tiedossa**).

## 3. Ohjaus ja kytkentä

- **Halogeenin käynnistysvirta:** kylmän 250 W:n halogeenipolttimon hetkellinen virta on noin
  10–15 × 10,4 A eli noin **100–160 A** kymmenien millisekuntien ajan [ESP32-PDM design-notes §4a,
  laskelma; päivitetty 2026-10-31, aiemmin 200–300 A 500 W:lle]. Tämä on lähellä `pdm-hc2`-kortin
  80 A:n nopeaa laukaisua, joten ongelma pienenee mutta ei poistu. Puolijohdekytkin tai sulake on mitoitettava sen mukaan (ks. PDM:n päätös 19).
- **Kytkin komentosillalle** (KS-alakeskus, [dc-distribution.md 2.2](dc-distribution.md#22-komentosillan-alakeskus-ks))
  ja merkkivalo. Jos lämmitin lisätään, se ei saa jäädä huomaamatta päälle ankkurissa.
- **Automaatio (vain jos lämmitin lisätään):** ESP32-PDM:n kanava voi kytkeä lämmittimen, kun
  ulkolämpötila on alle noin +3 °C ja vene on ajossa (tieto Signal K:sta). Lämpötilaraja on
  **⚠ arvio**. Termostaattitoimintoa ei ole enää ESP32-PDM:n suunnitelmissa; se pitää tarvittaessa
  pyytää sieltä erikseen.
- **Kaapeli:** valo on komentosillan katolla, joten kaapeli KS-alakeskukselta on lyhyt (noin 3 m,
  **⚠ arvio**) eikä mene mastoon. 10,4 A:lla riittää 1,5 mm² (10 %:n häviö) tai 2,5 mm²
  täydelle valoteholle (3 %:n häviö; halogeenin valovirta laskee jyrkästi jännitteen mukana) [laskelma,
  [dc-distribution.md 4.2](dc-distribution.md)]. Lämmittimen oma johdin katolle: 1,5 mm² riittää
  [laskelma].
- **Paloturvallisuus:** lämmitin ja sen johdot pitää kiinnittää niin, etteivät ne osu
  halogeenipolttimoon tai heijastimeen. Liimanauhat ja silikonimatot eivät kestä polttimon
  läheisyyttä.

## 4. Suositus

1. **Halogeeni ilman lämmitintä** (vaihtoehto A, päätetty 2026-10-30): suojahuppu, lasi pois tuulesta
   pysäköintiasennossa ja valo päälle hetkeä ennen tarvetta. Kustannus muutamia kymmeniä euroja.
   Kokeillaan ensimmäisellä pakkasajolla: kuinka nopeasti jää sulaa ja jäätyykö katon läpivienti.
2. **Jalustan lämmitin (B) luultavasti tarpeeton,** koska vipu ja laakeri ovat komentosillan
   sisällä. Lisätään vain, jos koeajo osoittaa nivelen jäätyvän.
3. **Halogeenin käynnistysvirta** (noin 100–160 A kymmenien millisekuntien ajan, 250 W) pitää hoitaa:
   joko ESP32-PDM:n `pdm-hc2`-kortilla (päätös 19: järeämmät MOSFETit ja nopean laukaisun poisto
   SOA-tarkistuksen jälkeen) tai kytkemällä valo releellä, jota PDM ohjaa. Tämä on nyt ESP32-PDM:n
   ratkaistava, koska LED-vaihtoehto on hylätty.
4. **Varapolttimot:** kun tyyppi on varmistettu polttimon merkinnästä (luultavasti EHJ / A1/223,
   G6.35), hanki useampi varapolttimo. Projektoripolttimon käyttöikä on vain noin 50 h, ja
   Philips-merkkisiä näyttää olevan enää vähän saatavilla. Saman tyypin muita merkkejä myydään
   noin 10 £:lla ([BLT Direct](https://www.bltdirect.com/products/a1-223-24v-250w-projector-lamp)),
   valovirta noin 8 500 lm **⚠ tarkista**.

Jos LED-vaihto otetaan myöhemmin uudelleen esiin, lasi pitää lämmittää erikseen (C4 noin 50–100 W
tai C2 noin 50 W), ja kirkkaampi keila vaatii todennäköisesti uuden valon (kohta D).

**Turvallisuus:** hakuvalo ei ole ohjauksen kaltainen turvallisuuskriittinen järjestelmä, mutta
250 W:n halogeeni on palovaara, jos lämmittimen johdot tai suojahuppu koskettavat kuumaa runkoa.
Älä jätä huppua valon päälle, kun valo palaa.

## 5. Avoimet kysymykset

- [x] Hakuvalon valmistaja ja malli: ei tyyppikilpeä; vanha, todennäköisesti neuvostovalmisteinen [omistaja 2026-10-30]
- [x] Polttimo: halogeeni [omistaja 2026-10-30]
- [x] Polttimo: Philipsin 24 V:n 250 W:n projektori- ja piirtoheitinhalogeeni [omistaja 2026-10-31] (aiemmin kirjattu 500 W oli virhe)
- [ ] Polttimon tarkka tyyppi merkinnästä (luultavasti EHJ / A1/223, kanta G6.35; aiempi arvio GY9.5) ja varapolttimoiden hankinta (käyttöikä noin 50 h)
- [ ] Projektoreissa polttimoa jäähdyttää yleensä puhallin. Kestääkö polttimo pitkän käytön hakuvalon rungossa ilman puhallinta? **⚠ tarkista** datalehdestä ja käytössä
- [x] Ohjaus: käsikäyttöinen, vipu katon läpi [omistaja 2026-10-30]
- [x] Sijainti: komentosillan katto [omistaja 2026-10-30]
- [x] Etulasin paksuus: noin 5 mm [omistaja 2026-10-30]
- [ ] Etulasin halkaisija: noin 350 mm (arvio) [omistaja 2026-10-30]; mitataan tarkemmin
- [x] Etulasin materiaali: lasi, oletettavasti karkaistu (kestänyt käytössä vuosikymmeniä) [omistaja 2026-10-30]
- [x] Miksi reunarengas ei riitä: lasi johtaa lämpöä huonosti, ja reunan lämpö ulottuu vain noin 1–2 cm (kohta C, laskelma)
- [x] Mahtuuko lämpöpuhallin runkoon: omistajan arvion mukaan mahtuu peittämättä liikaa valokeilaa [omistaja 2026-10-30]
- [ ] Jäätyykö katon läpivienti tai valaisimen nivel (koeajo pakkasella)
- [ ] Kuinka nopeasti halogeeni sulattaa jäätyneen lasin (koeajo)
- [x] Halogeeni vai LED: halogeeni säilyy, LED hylätty [omistaja 2026-10-30]
- [x] Säilytetäänkö vanha valaisin: kyllä, sopii aluksen tyyliin [omistaja 2026-10-30]
- [ ] Halogeenin käynnistysvirta (noin 100–160 A, 250 W): PDM-kortti (ESP32-PDM:n päätös 19) vai rele?
- [ ] Suojahupun teko tai hankinta
- [ ] Kuinka paljon Vegalla ajetaan pakkasella tai jäätyvässä roiskeessa (kuukaudet)?
- [ ] Kestääkö etulasi lämpöshokin paksusti jäätyneenä: lasi oletettavasti karkaistu ja kestänyt käytössä vuosikymmeniä [omistaja 2026-10-30]; varmistuu koeajossa, tarkista lasi halkeamien varalta
