# Hydrauliikan hankintalista

> **Tila:** päivitetty 2026-11-13 (P1: päätetty vaihtoehto B, ryhmän 3 pumppu 30C20X146 ja vanha tukilaakeri, rivit 6.5–6.9); 2026-11-12 (PVE-liittimien GDM-kiinnitysruuvit M3 × 35, rivi 4.17); 2026-11-05 (P1:n tukilaakeri, kannake ja mahdollinen akseli, rivit 6.5–6.7); 2026-11-03 (PVG 32 saapui, rungon koodit tulkittu: pumppumoduuli 157B5111, peruslohkot 157B6200 ilman PVLP-paikkoja; karat liikkuvat ja palaavat keskelle); 2026-11-02 (PVG 32 ostettu, 200 € + rahti 39,90 €; PVE-liittimet mukana); 2026-11-01 (PVH57 ostettu, 150 €); koottu 2026-10-28 (P2 = Vickers PVH57, venttiileinä Danfoss PVG 32, päätökset 2026-10-27). Luvut ja koodit ovat lähdedokumenteista; tarkemmat perustelut
> linkeissä. Hinnat ovat jälleenmyyjien hintoja tai arvioita, ja ne on merkitty. Päivitä lista, kun
> osa ostetaan, löytyy veneeltä tai suunnitelma muuttuu.
> Arkistoitujen varavaihtoehtojen (FXDC + LS-purku, LS + on/off) osia ei ole listalla. Ne tulevat
> ajankohtaisiksi vain, jos PVG 32 osoittautuu koestuksessa korjauskelvottomaksi, ks.
> [arkisto](design/archive/p2-fxdc-ls-unloading.md#tarvittavat-osat-pumpun-lisäksi-minimi).

**Tila-sarake:** ✅ olemassa tai sovittu · 🛒 hankitaan · 🔍 todennäköisesti olemassa, tarkista
veneellä · ❓ ehdollinen (tarve selviää tarkistuksesta tai päätöksestä) · ⏳ myöhemmin

## 1. P2-pumppu ja voimansiirto

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 1.1 | Vickers PVH57C-LAF-1S-10-C12V-31 | 1 | 57,4 cm³, LS-säädin, pyörimissuunta L | ✅ ostettu ja noudettu 2026-11-01 | 150 € [omistaja 2026-11-01] | [päätös 2026-10-27](../decisions.md), [p2-variable-pump](design/p2-variable-pump.md) |
| 1.2 | HRC 150 -kytkimen napa: pumpun puolelle **F**; PTO:n puolelle **F tai H** (aiemmin suunniteltu F [omistaja 2026-11-01]; **H suositeltava**, jos avain mahtuu) | 2 | Taper Lock -holkeille. **H PTO:lla:** napa on akselin päässä, joten pesän ja navan väliin jää noin 26 mm (PTO-akselin vapaa pituus noin 60 mm − napa 33,5 mm, mitattu [Advance 300-WXT03](../datasheets/README.md) -piirustuksesta). Holkkiruuvit kiristetään siitä välistä, joten PTO:n napaa voi säätää pumppu paikallaan **⚠ mittaa, mahtuuko kuusiokoloavain**. Kumielementin vaihtoon napaa pitää todennäköisesti vetää noin elementin leveyden (40,5 mm) verran, joten pumppua pitää silti siirtää noin 15 mm. Siksi kannakkeen jalkaan tehdään akselin suuntainen säätövara noin 20 mm **⚠ tarkista kytkimestä**. FH:n kokonaispituus on sama kuin FF:n, 107,5 mm. Kaksi samaa osaa: yksi tilauskoodi (esim. HRC150F). F-napa voidaan asentaa lähelle vaihteiston laakeria, mikä pienentää ulokekuormaa. Holkkiruuvit kiristetään kytkimen puolelta ennen pumpun asennusta, joten PTO:n navan irrotus vaatii myöhemmin pumpun siirtämistä taaksepäin. Pumpun puolella navan ulkopinta jää noin 12 mm:n päähän kannakelevystä (pumpun akseli 56 mm laipasta, napa 33,5 mm, levy 10 mm) [laskelma], joten H-navan holkkiruuvit jäisivät levyn puolelle. **F (holkki sisäpuolelta)** on luontevampi; kummallakin tyypillä napa kiristetään ennen kuin pumppu työnnetään paikalleen **⚠ tarkista tila** | 🛒 | noin 19 € + ALV / kpl | [p2-variable-pump](design/p2-variable-pump.md#tarvittavat-osat-pumpun-lisäksi-minimi) |
| 1.3 | HRC 150 -elastinen välikappale | 1 | | 🛒 | noin 10 £ + ALV | sama |
| 1.4 | Taper Lock 2012 -holkki 48 mm, kiilaura | 1 | PTO:n puoli; kiilaura 14 mm. Syvyys vaihtelee: [Martin](https://www.applied.com/c-martin-2012-48mm/p/100792325) 14 × 3,8 mm (= DIN 6885:n navan ura), [Dunlop](https://www.bearingboys.co.uk/2012-Taper-Bushes/201248-Taper-Bush-Dunlop-2367-p) 14 × 3,3 mm (matala). PTO-akselin ura on 5,5 mm syvä [datalehti Advance 300-WXT03], joten 14 × 9 -kiila nousee 3,5 mm akselin pinnasta: **3,8 mm:n ura sopii** (0,3 mm välys), **3,3 mm:n urassa kiila pohjaa 0,2 mm** ja sitä pitää hioa. **Valitse 14 × 3,8 mm** (esim. Martin) tai tarkista ostettavan holkin uran syvyys **⚠ mittaa myös itse kiila** | 🛒 | arviolta 10–25 € | sama |
| 1.5 | Taper Lock 2012 -holkki 1 1/4", kiilaura | 1 | pumpun puoli; tuumaholkki, kiilaura 5/16" (= pumpun kiila 7,93 mm). Ei metristä 32 mm:n holkkia: 31,75 mm:n akseli jäisi väljäksi. Kiristys valmistajan pakkausohjeen mukaan (2012: tyypillisesti 2 × 7/16" BSW, noin 31 Nm **⚠ tarkista pakkauksesta**) | 🛒 | arviolta 10–25 € | sama |
| 1.6 | Pumppukannake SAE C -laipalle | 1 | 10 mm:n teräslevy, laserleikkaus ja hitsaus; laippa: keskitys Ø127 mm, reikäneliö 114,5 mm, reiät Ø14,2–14,5 [Eatonin luettelo s. 21]; **ei Ø125** (se on metrinen M-laippa). Valmis Eaton FB-C4-10 (02-143419) sopisi, mutta se on poistunut valikoimasta (Danfoss 2026-11-01), eikä hintaa löytynyt; mallina ks. [FB-C4-10](design/p2-variable-pump.md#eatonin-jalkakannake-fb-c4-10) | 🛒 omistajat suunnittelevat | **⚠ ei tiedossa** | [päätös 2026-10-23](../decisions.md) |
| 1.7 | Kytkimen suojakotelo | 1 | pyörivän kytkimen suoja | 🛒 | **⚠ ei tiedossa** | [p2-variable-pump](design/p2-variable-pump.md#asennusjärjestys) |
| 1.8 | Pumpun ulkoiset O-renkaat (portit, laipat, säädin) | sarja | vaihdetaan liitäntöjä tehtäessä; mitat **⚠ ei tiedossa** | 🛒 | **⚠ ei tiedossa** | [p2-variable-pump](design/p2-variable-pump.md#tiivistesarja) |
| 1.9 | Akselitiiviste | 1 | vain, jos vuotaa koeajossa; koko tiivistesarjaa 02-102244 (noin 853 $) ei tarvita | ❓ | **⚠ ei tiedossa** | sama |
| 1.10 | Pumpun koeajo hydrauliikkakorjaamolla | – | suositus ennen asennusta | ❓ | **⚠ ei tiedossa** | sama |

## 2. P2:n imulinja (säiliö → pumppu, 50 mm)

Järjestys säiliöltä pumpulle: **muhvi → 90°:n kulma → palloventtiili → letkukara → letku → pumpun
imulaippa** [omistaja 2026-10-28]. Säiliö on tyhjä ja auki öljynvaihdon aikana, joten muhvi
hitsataan silloin. Muhvi tehdään **uuteen kohtaan**, jotta vanha 32 mm:n ulosotto jää P1:lle
([p1-steering-pump](design/p1-steering-pump.md)).

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 2.1 | Säiliöön hitsattava muhvi, 50 mm:n linjalle | 1 | kierre palloventtiilin mukaan (esim. 2" BSP **⚠ tarkista** venttiilistä); ulosotto vähintään 50 mm minimiöljypinnan alle eikä paluiden lähelle; säiliö puhdistetaan ennen hitsausta ja sen jälkeen, ks. [puhdistus](#säiliön-puhdistus-hitsauksen-yhteydessä) | 🛒 | **⚠ ei tiedossa** | [omistaja 2026-10-28] |
| 2.2 | 90°:n kulmaliitin muhvin ja palloventtiilin väliin | 1 | täysi sisähalkaisija; mieluiten pitkäsäteinen, koska imupuolen marginaali on pieni [arvio] | 🛒 | **⚠ ei tiedossa** | [omistaja 2026-10-28] |
| 2.3 | Täysiaukkoinen palloventtiili 50 mm (2V0) | 1 | auki ajossa | 🔍 | – | [omistaja 2026-10-28] |
| 2.4 | Letkukara 50 mm:n imuletkulle | 1 | palloventtiilin kierteeseen | 🛒 | **⚠ ei tiedossa** | [omistaja 2026-10-28] |
| 2.5 | Imuletku 50 mm | **⚠ pituus** (noin 3 m) | imuun soveltuva, ei painu kasaan alipaineessa | 🛒 **⚠ tarkista**, onko olemassa | **⚠ ei tiedossa** | [päätös 2026-10-23](../decisions.md) |
| 2.6 | Letkunkiristimet, ruostumattomat | 4 | kaksi kumpaankin päähän | 🛒 | pieni | [arvio] |
| 2.7 | Pumpun imuliitin: 2" SAE code 61 -laippa, O-rengas, pultit 1/2-13 UNC ja letkukara 50 mm:n letkuun | 1 | 2" code 61 [Eatonin luettelo s. 21–22]; ei supistusta | 🛒 | **⚠ ei tiedossa** | [p2-variable-pump](design/p2-variable-pump.md#tarvittavat-osat-pumpun-lisäksi-minimi) |
| 2.8 | Mittausvälikappale letkun ja pumpun imulaipan väliin: lyhyt Ø50-teräsputki (noin 100–150 mm), jossa hitsattu 1/4" BSP -muhvi kyljessä, tai valmis 2":n T-kappale 1/4":n sivuaukolla | 1 | mahdollisimman lähellä pumppua, jotta mittaus sisältää koko linjan häviöt; BSPP ja tiivistealuslevy, ei kartiokierrettä (imupuolen vuoto imee ilmaa) | 🛒 | **⚠ ei tiedossa** | [pressure-monitoring](design/pressure-monitoring.md#imupaineen-mittaus) |
| 2.9 | 1/4" BSP -T-kappale mittausaukkoon | 1 | anturi 2B1 ja mittarin letku samaan aukkoon | 🛒 | pieni | [arvio] |
| 2.10 | Imupaineanturi 2B1, −1…+1 bar, 4–20 mA | 1 | Signal K:hon; varoitus alle 0 bar | 🛒 päätetty | noin 40–150 € [arvio] | [päätös 2026-10-23](../decisions.md) |
| 2.11 | Kaksoispainemittari (vakuumi ja paine) −1…+1,5 bar, glyseriinitäytteinen, Ø63 mm, takaliitäntä | 1 | 2G2, P2:n imupaine ilman sähköä; mittaritauluun, ks. [kiinnitys](#imupuolen-kaksoispainemittarit) | 🛒 päätetty | noin 15–40 € [arvio] | [pressure-monitoring](design/pressure-monitoring.md#imupaineen-mittaus), [päätös 2026-10-28](../decisions.md) |

## 3. P2:n paine-, vuoto- ja LS-linjat

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 3.1 | Painelähdön 1" SAE code 61 -laippa, pultit 3/8-16 UNC ja supistus 3/4":n letkuun | 1 | 1" code 61 [Eatonin luettelo s. 21–22] | 🛒 | **⚠ ei tiedossa** | [p2-variable-pump](design/p2-variable-pump.md#tarvittavat-osat-pumpun-lisäksi-minimi) |
| 3.2 | Painelinja 3/4", 3–4 m | 1 | nykyinen P2:n painelinja; päät sovitetaan PVG:n P-porttiin | 🔍 **⚠ tarkista** kunto ja painearvo | – | [current-system §5](current-system.md#5-avoimet-kysymykset) |
| 3.3 | Sovite PVG 32:n P-porttiin | 1 | **G 3/4** (pumppumoduuli 157B5111, 16 mm syvä) [datalehti PVG 32 s. 20] | 🛒 | **⚠ ei tiedossa** | [aux-circuit-ls-clean-sheet](design/aux-circuit-ls-clean-sheet.md#mitä-keulapotkuri-tarvitsee-pvh57n-ja-tämän-venttiilin-lisäksi) |
| 3.4 | LS-letku 1/4" ja liittimet | 1 | PVG:n LS (G 1/4) → pumpun LS-portti (9/16-18 UNF O-rengas, SAE -6) | 🛒 | **⚠ ei tiedossa** | sama |
| 3.5 | Kotelovuotoletku vähintään noin 1/2" | 1 | ylimmästä vuotoportista (3/4-16 UNF O-rengas, SAE -8) suoraan säiliöön öljypinnan alle, ei paluulinjaan | 🛒 | **⚠ ei tiedossa** | [p2-variable-pump](design/p2-variable-pump.md#asennusjärjestys) |
| 3.6 | Keulapotkurin (U11) vuotolinja 1/4" | 1 | tehdään uusiksi suoraan säiliöön öljypinnan alle | 🛒 | **⚠ ei tiedossa** | [omistaja 2026-10-27] |
| 3.7 | Säiliön läpiviennit tai muhvit vuotolinjoille (3.5 ja 3.6) | 1–2 | putki öljypinnan alle; tehdään samalla kertaa kuin muhvi 2.1 | 🛒 **⚠ tarkista**, voiko käyttää olemassa olevia aukkoja | **⚠ ei tiedossa** | [arvio] |

## Säiliön puhdistus hitsauksen yhteydessä

Muhvi 2.1 ja mahdolliset läpiviennit 3.7 hitsataan säiliöön, jossa on ollut öljyä. Ohje perustuu
yleiseen hitsaus- ja hydrauliikkakäytäntöön, ei säiliön valmistajan ohjeeseen [arvio]. Hitsaus
öljyä sisältäneeseen säiliöön on tulityötä: säiliö pidetään auki ja tuuletettuna, ja paikalla on
sammutin ja palovartija.

**Ennen hitsausta:**

1. Valuta öljy pois ja imeytä loput imeytysliinoilla.
2. Pese sisäpinnat **vesiohenteisella emäksisellä rasvanpoistoaineella** (esim. konepesuun
   tarkoitettu teollisuuspesuaine) lämpimällä vedellä ja harjalla, ja huuhtele puhtaalla vedellä.
   Isoille pinnoille tämä on halvin ja turvallisin keino.
3. Kuivaa heti paineilmalla tai lämpöpuhaltimella, myös saumat ja nurkat. Teräs ruostuu nopeasti.
4. Puhdista hitsauskohta paljaaksi metalliksi sisältä ja ulkoa noin 50–100 mm:n matkalta.
   Pistemäiseen rasvanpoistoon käy kloorittoman jarrunpuhdistimen (esim. CRC Brakleen) pieni määrä;
   anna sen haihtua kokonaan ja tuuleta muutama minuutti ennen hitsausta.

**Ei ennen hitsausta:**

- **Ei kloorattua jarrun- tai osienpuhdistinta.** Hitsauskaari hajottaa kloorihiilivetyjen höyryt
  myrkylliseksi fosgeeniksi. Tarkista ainesosat pullosta tai käyttöturvallisuustiedotteesta: jos
  niissä on *tetrachloroethylene*, *perchloroethylene* tai *dichloromethane*, ainetta ei käytetä.
  Brakleenista on sekä kloorillinen että klooriton versio; Euroopassa myytävä on käsittääkseni
  klooriton **⚠ tarkista** pullosta.
- **Ei koko säiliön pesua liuottimilla** (jarrunpuhdistin, bensiini, tinneri, asetoni). Höyryt
  ovat ilmaa raskaampia ja jäävät säiliön pohjalle, jossa kipinä voi sytyttää ne räjähdysmäisesti.
  Hydrauliöljyn leimahduspiste on korkea, joten öljyjäämät ovat pienempi riski kuin liuotinhöyryt.

**Hitsauksen jälkeen** (nyt vaarallisinta ovat metallihiukkaset, jotka kulkeutuisivat uudelle
PVH57:lle):

1. Poista hitsausroiskeet, kuona ja hiomapöly harjalla ja kaapimella, sitten imurilla. Magneetti
   muovipussin sisällä kerää teräspölyn.
2. Tarkista hitsin takapuoli. Jos säiliö on maalattu sisältä (**⚠ ei tiedossa**), hio palanut maali
   pois; maalaa uudelleen vain öljynkestävällä säiliömaalilla. Jarrunpuhdistin voi pehmentää maalia,
   joten kokeile sitä ensin pieneen kohtaan.
3. Pyyhi nukkaamattomalla liinalla, ei trasselilla eikä puuvillarätillä. Liuotinpyyhintään käy
   klooriton jarrunpuhdistin tai isopropanoli, kun säiliö on jäähtynyt; tuuleta ennen täyttöä.
4. Huuhtele seinät ja pohja muutamalla litralla öljyä (huuhteluöljy 8.1 tai HVLP 32) ja tyhjennä.
   Huuhteluun käytetty erä ei palaa järjestelmään. Öljy poistaa veden ja pesuainejäämät ja jättää
   suojaavan öljykalvon.
5. Tarkista taskulampulla: puhtaalla liinalla pyyhitty pinta ei saa enää värjätä liinaa.
6. Täytä suodattimen läpi. Käyttöönotto jatkuu huuhtelupäätöksen mukaan: koeajot huuhteluöljyllä
   uuden suodatinelementin läpi, sitten elementin ja öljyn vaihto
   ([päätös 2026-10-27](../decisions.md), [hydraulic-oil](design/hydraulic-oil.md)). Tavoite on
   puhtausluokka 16/14/12.

Tarvikkeet: imeytysliinat, vesiohenteinen rasvanpoistoaine, nukkaamattomat liinat, klooriton
jarrunpuhdistin, sammutin. Hinnat **⚠ ei tiedossa**, pieniä [arvio].

## 4. Venttiilipöytä Danfoss PVG 32 ja ohjaus

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 4.1 | Danfoss PVG 32, 5 lohkoa (käytetty) | 1 | 1 × PVEH 157B4024, 4 × PVEO 157B4224 | ✅ ostettu 2026-11-02, saapui 2026-11-03 | 200 € + rahti 39,90 € (pyyntö 400 €) [omistaja 2026-11-02] | [aux-circuit-ls-clean-sheet](design/aux-circuit-ls-clean-sheet.md#ostettu-venttiili-danfoss-pvg-32-5-lohkoa-torifi) |
| 4.2 | Porttitulpat (muovi tai teräs) | sarja | kuljetukseen ja puhdistukseen; osa porteista on nyt auki | 🛒 | pieni | sama, [Puhdistus ja koestus](design/aux-circuit-ls-clean-sheet.md#puhdistus-ja-koestus) |
| 4.3 | Sovitteet A/B-portit (G 1/2) → keulapotkurin 1/2":n letkut | 2 | letkut valmiina | 🛒 | **⚠ ei tiedossa** | sama |
| 4.4 | Sovite T-portti (G 3/4) → paluukeräin | 1 | | 🛒 | **⚠ ei tiedossa** | sama |
| 4.5 | Painemittari 2G1 M-porttiin (G 1/4) | 1 | analoginen | 🔍 nykyinen mittari, **⚠ tarkista** mittausalue ja kunto | – | [pressure-monitoring](design/pressure-monitoring.md) |
| 4.6 | Kiinnitysteline tai -levy konehuoneeseen | 1 | venttiili noin 22–23 kg [laskelma]; paikka **⚠** | 🛒 | **⚠ ei tiedossa** | [schematic](schematic.md#avoimia-kohtia-kaaviossa) |
| 4.7 | Potentiometrijoystick keulapotkurille | 1 | samasta 24 V:n syötöstä; signaali 0,25–0,75 × U. Suositus JH-D202X-R2 5K (jousipalautus; yksi akseli uraohjaimella) ja 2 × 2,4 kΩ:n sarjavastukset; Danfoss PVREL liian kallis [omistaja 2026-11-02] | 🛒 | noin 11–23 $ kpl (eBay, Abra 2026-11-02); kaksi kappaletta (varaosa). Vertailu: PVREL 155U2605 426,56 € + ALV | [bow-thruster-control](design/bow-thruster-control.md#joystick-ehdokkaat-haettu-2026-11-02) |
| 4.8 | PVE-liittimet Hirschmann DIN 4-napainen ja johdotus | 2–5 | lohkot 1–3 ensin. Liittimet tulevat venttiilin mukana [omistaja 2026-11-02]; **jokaisessa viidessä PVE:ssä on oma Hirschmann GDM -liitin johtoineen** [omistaja 2026-11-03, kuvista]. Johdotus hankitaan | ✅ liittimet mukana; 🛒 johdotus | liittimet kaupassa mukana; johdotus **⚠ ei tiedossa** | sama |
| 4.9 | Hätäseisrele PVE:iden 24 V:n syöttöön | 1 | | 🛒 | **⚠ ei tiedossa** | sama |
| 4.10 | Koestus hydrauliikkakorjaamon koepenkissä | – | vaihtoehtona oma koestus | ❓ | **⚠ ei tiedossa** | [Puhdistus ja koestus](design/aux-circuit-ls-clean-sheet.md#puhdistus-ja-koestus) |
| 4.16 | Käsivivut PVM-kantoihin (kokeiluun M8-kierretanko tai oma 3D-tulostettu vipu; käyttöön metallinen) | 1–5 | kierre todennäköisesti M8 **⚠ mittaa** | 🛒 oma valmistus | pieni; valmis Danfoss-vipu **⚠ ei tiedossa** | [pvg32-lever](design/pvg32-lever.md) |
| 4.17 | Kiinnitysruuvit PVE:iden Hirschmann GDM -liittimiin, **M3 × 35** (keskiruuvi), ja tarvittaessa liitintiivisteet | 1–5 **⚠ tarkista**, montako puuttuu tai on huonoja | GDM = DIN 43650 / EN 175301-803 muoto A [omistaja 2026-11-12]. Alkuperäinen Hirschmann **734363001** (GDM 3011 RF-1, ruostumaton) tai rautakaupan ruostumaton M3 × 35 (A2/A4) ja pieni aluslaatta. Kiristä vain sen verran, että tiiviste puristuu: Danfoss varoittaa ylikiristyksestä ja vaatii tiivisteen liittimen alle. Kovettuneet tai haljenneet tiivisteet vaihdetaan samalla; PVE:iden tiivistesarja 157B4997 (Series 4 -dokumentista, sopivuus sarjan 0 PVE:ihin **⚠ tarkista**) | 🛒 | pieni [arvio] | [Bürklin 734363001](https://www.buerklin.com/en/central-screw-stainless-steel-m3-x-35/p/51f4961), [Danfoss PVE -asennusohje](https://assets.danfoss.com/documents/33172/AN152886482922en-000503.pdf), [datasheets](../datasheets/README.md) |

**Ehdolliset PVG 32:n osat.** Rungon koodit tulkittu 2026-11-03: pumppumoduuli **157B5111** (suljettu keskiasento, sopii) ja peruslohkot **157B6200** (ei PVLP-paikkoja eikä LS A/B -rajoittimia), ks. [Mitä koodit kertovat](design/aux-circuit-ls-clean-sheet.md#mitä-koodit-kertovat-2026-11-03). Karat selviävät kokoonpanokoodista 157N5531 ja kunnon tarkistuksesta:

| # | Osa | Milloin tarvitaan | Hinta | Lähde |
|---|---|---|---|---|
| 4.11 | Keulapotkurin lohkon kara 40 l/min, avoin keskiasento (esim. 157B7102) | jos nykyinen kara on vääränlainen | noin 116 SGD + verot | [aux-circuit-ls-clean-sheet](design/aux-circuit-ls-clean-sheet.md#mitä-keulapotkuri-tarvitsee-pvh57n-ja-tämän-venttiilin-lisäksi) |
| 4.12 | Keulapotkurin iskuventtiilit: **Marchesini VAU 1/2" (V0450), jousi 80–300 bar** keulaan moottorin lähelle (suositus [arvio]); imuventtiilillinen VAUAC, jos PVEH-lohkon kara on suljettu; vaihtoehtona peruslohko 157B6230 + 2 × PVLP (esim. 157B2280) | peruslohkossa 157B6200 ei ole PVLP-paikkoja; pätevä henkilö hyväksyy asetuksen | 80–300 barin 1/2":lle ei löytynyt listahintaa (2026-11-04). Vertailuksi VAU 1/2" 30–180 bar noin 70 € alv 0 % ([Partao](https://partao.com/granit-85034008-oleodinamica-marchesini-double-pressure-limiting-valve-vau-1-2-bsp-30-180-bar.html)), 10–180 bar 94,35 £ ja 1/4" 80–300 bar noin 62 £ ([Flowfit](https://flowfitonline.com/products/hydraulic-dual-cross-line-relief-valve-vau-1-4-80-300-bar-standard)); kysy Suomesta (esim. Salhydro; SixTekiä ei enää ole [omistaja 2026-11-04]) | [aux-circuit-ls-clean-sheet](design/aux-circuit-ls-clean-sheet.md#mitä-koodit-kertovat-2026-11-03) |
| 4.13 | Tiivistesarja PVAS 157B8005 | jos lohkopino avataan; karat liikkuvat vapaasti [omistaja 2026-11-03], joten luultavasti ei tarvita, ellei peruslohkoja vaihdeta | **⚠ ei tiedossa** | sama |
| 4.14 | Pumppumoduuli, suljettu keskiasento 157B5111 | **ei tarvita**: nykyinen on rungon leiman perusteella 157B5111 [päättely 2026-11-03]; varmistetaan koestuksessa | – | sama |
| 4.15 | PVPX 24 V, 157B4238 | **ei mahdollinen** nykyisessä pumppumoduulissa (ei PVPX-paikkaa), ei tarvita | – | sama |

## 5. Paluu, suodatus ja jäähdytys

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 5.1 | Paluukeräin: 1":n T-liittimet, supistusnipat ja tiivistealuslevyt (BSPP, esim. Dowty) | 2–3 T:tä | venttiilipöydän lähelle; ei vesijohto-osia | 🛒 | **⚠ ei tiedossa** | [oil-cooling](design/oil-cooling.md#paluiden-yhdistäminen) |
| 5.2 | Paluuletku 1" | noin 5 m | keräin → jäähdytin → suodatin | 🛒 | **⚠ ei tiedossa** | [omistaja 2026-10-26] |
| 5.3 | Supistukset 1" → 3/4" jäähdyttimen liitäntöihin | 2 | | ❓ jos jäähdytin asennetaan | **⚠ ei tiedossa** | [oil-cooling](design/oil-cooling.md#paluulinjan-letkukoko) |
| 5.4 | Bowman EC100 -öljynjäähdytin | 1 | | ✅ omistajilla varalla (asennus päättämättä) | – | [oil-cooling](design/oil-cooling.md) |
| 5.5 | Jäähdyttimen ohitusventtiili 3–4 bar (3V1) | 1 | rinnakkain jäähdyttimen kanssa | ❓ jos jäähdytin asennetaan | **⚠ ei tiedossa** | [oil-cooling](design/oil-cooling.md#paluulinja-asennus) |
| 5.6 | Sinkkianodi EC100:aan | 1 | tarkistetaan ennen käyttöönottoa | ❓ | **⚠ ei tiedossa** | sama |
| 5.7 | Merivesihaara: letkut, T-liittimet, virtauksenrajoitin 30–40 l/min (3V3) ja kuristus päälinjaan (3V4) | sarja | rajoittimen tyyppi päättämättä | ❓ jos jäähdytin asennetaan | **⚠ ei tiedossa** | [oil-cooling](design/oil-cooling.md#merivesi) |
| 5.8 | Paluusuodatin: OMTF171F10NA1 (lasikuitu, 157 l/min), linjasuodatin tai lasikuituelementti nykyiseen runkoon | 1 | nykyinen selluloosaelementti ei riitä puhtausluokkaan 16/14/12; ratkeaa säiliön kannen mittauksilla | 🛒 malli päättämättä | OMTF171F10NA1 84,70 £ sis. ALV | [p2-variable-pump](design/p2-variable-pump.md#paluusuodattimen-vaihto-omtf171f10na1) |
| 5.9 | Suodatinelementti | 2 | yksi käyttöönoton huuhteluun, toinen öljynvaihdon jälkeen | 🛒 | **⚠ ei tiedossa** | [päätös 2026-10-27](../decisions.md) |
| 5.10 | Paluupaineen mittari 3G1 ja mittausliitin keräimeen | 1 | ehdotus | ❓ | **⚠ ei tiedossa** | [oil-cooling](design/oil-cooling.md#paluiden-yhdistäminen) |

## 6. P1 (ohjauspiiri)

Ohjauspiirin venttiilit (RPF3, orbitroli, vastaventtiilit, hätäohitus) ovat olemassa. Imulinja
siirretään P2:n vanhaan 32 mm:n letkuun ja ulosottoon.

**P1 vaihdetaan uuteen pumppuun:** vanhaan Salami 2PE16D-P28P1:een ei saa uutta akselia
[omistaja 2026-11-12]. P1 oli ennen tandemina vanhan ryhmän 3 P2:n perässä, joten se tarvitsee oman
tukilaakerin ja kannakkeen [omistaja 2026-11-05]. Vaihtoehtojen vertailu:
[p1-steering-pump](design/p1-steering-pump.md#uuden-p1n-kierrostilavuus).

**Päätetty 2026-11-13: vaihtoehto B** ([päätösloki](../decisions.md)): ryhmän 3 pumppu 20 cm³ ja
vanha ryhmän 3 tukilaakeri ja kannake, koska mitat täsmäävät (pulttijako 98,4 × 128,1 mm, ohjuri
Ø50,8 mm, kartio 1:8, kiila 4 mm) [omistaja 2026-11-13]. Imulinja pidetään noin 3,2 metrissä.
Vaihtoehto A (ryhmän 2 pumppu, uusi tukilaakeri ja kannake) hylätty; rivit 6.5–6.7 yliviivattu.

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 6.1 | 32 mm:n imuletku, säiliöulosotto ja täysiaukkoinen palloventtiili | – | P2:n nykyinen imulinja | ✅ | – | [omistaja 2026-10-28] |
| 6.2 | ~~Letkukara 32 mm ja 3/4" BSP -liitin P1:n imuaukkoon~~ | – | **ei tarvita:** uuden P1:n imu- ja painelaipat otetaan vanhasta P2:sta [omistaja 2026-11-13]; P2:n vanha 32 mm:n imuletku kuuluu samaan laippaan (**⚠ tarkista**, että laipan letkuliitin sopii). Painelaipan kierre ja ohjauspiirin 1/2":n painelinja: sovite tarvittaessa (**⚠ tarkista**) | ✅ | – | [omistaja 2026-11-13] |
| 6.3 | Mittausliitäntä 1G2:lle imupuolelle: 1/4" BSP -mittausaukko imulaipassa tai välikappale laipan ja letkun väliin | 1 | 3/4":n T-kappale ei enää käy, koska pumppu on laippaliitäntäinen; ratkaisu **⚠ tarkista** laipasta | 🛒 | pieni | [pressure-monitoring](design/pressure-monitoring.md#imupaineen-mittaus) |
| 6.4 | Kaksoispainemittari (vakuumi ja paine) −1…+1,5 bar, glyseriinitäytteinen, Ø63 mm, takaliitäntä | 1 | 1G2, kiinteä, mittaritauluun; pelkkä −1…0 bar:n alipainemittari ei näyttäisi pysähdyksissä olevaa pientä ylipainetta (öljypinta vähintään 1 m pumpun yläpuolella) | 🛒 päätetty | noin 15–40 € [arvio] | sama, [pressure-monitoring](design/pressure-monitoring.md#imupaineen-mittaus), [päätös 2026-10-28](../decisions.md) |
| 6.5 | ~~**A:** uusi P1-pumppu, ryhmä 2, 16,6 cm³, kartioakseli 1:8, eurooppalainen laippa, myötäpäivään (esim. Salami 2PE16D-P28P1)~~ | 1 | myyjä ja hinta auki; kysely Fluiconnectolle 2026-11-06 | ❌ hylätty 2026-11-13 | **⚠ ei tiedossa** | [omistaja 2026-11-12], [p1-steering-pump](design/p1-steering-pump.md#uuden-p1n-kierrostilavuus) |
| 6.6 | ~~**A:** tukilaakeri ryhmän 2 pumpulle (esim. SU2-tyyppi), lähtöakseli kiilalla hihnapyörälle~~ | 1 | pumppulaippa eurooppalainen 71,5 × 96, keskitys Ø36,5 | ❌ hylätty 2026-11-13 | noin 95–100 € (EP-hydrauliikka, hakutulos 2026-11-06, **⚠ tarkista**) | [p1-steering-pump](design/p1-steering-pump.md#tukilaakeri-kannake-ja-käyttöakseli) |
| 6.7 | ~~**A:** uraholkki ryhmä 2, 14 hammasta, 1:8-kartioreikä, kiila 3,2 mm~~ | 1 | pumpun ja tukilaakerin väliin | ❌ hylätty 2026-11-13 | noin 7–16 € (hakutulokset 2026-11-06, **⚠ tarkista**) | sama |
| 6.8 | **Uusi P1-pumppu (päätetty 2026-11-13)**, ryhmä 3, 20 cm³, kartioakseli 1:8 ja 4 mm:n kiila, pulttijako 98,4 × 128,1, ohjuri Ø50,8, myötäpäivään, **laippaliitännät, max 250 bar** [omistaja 2026-11-13]: [Hydrauliikkakauppa.fi 30C20X146](https://www.hydrauliikkakauppa.fi/tuote/hammaspyorapumppu-3-sarja-25-cm%c2%b3-laippaliitanta/) (valmistaja ⚠ ei tiedossa) | 1 | ei 25 cm³:n versiota (imu kylmänä yli rajan). laipat vanhasta P2:sta [omistaja 2026-11-13] | 🛒 päätetty | **240 €** (191,24 € alv 0 %), varastossa [Hydrauliikkakauppa.fi 2026-11-12] | [datasheets](../datasheets/README.md), [p1-steering-pump](design/p1-steering-pump.md#vaihtoehto-ryhmän-3-pumppu-20-cm³) |
| 6.9 | Kannake ja tukilaakeri P1:lle | 1 | vanha ryhmän 3 tukilaakeri ja kannake, mitat täsmäävät [omistaja 2026-11-13]; hihnapyörä ja uraholkki vanhat; uraholkki käytetty vain noin 100 h [omistaja 2026-11-13], kunto ja sopivuus **⚠ tarkista** | ✅ | – | [päätös 2026-11-13](../decisions.md) |

## Imupuolen kaksoispainemittarit

**Päätetty 2026-10-28:** kiinteät kaksoispainemittarit 1G2 (P1) ja 2G2 (P2) mittaritauluun ([päätös 2026-10-28](../decisions.md)). Toteutus:

- **Mittauspiste pumpun imuliittimeen** (rivit 2.8 ja 6.3), ei säiliön päähän: vain siinä mittaus
  sisältää letkun, kulman ja palloventtiilin häviöt, eli juuri sen paineen, jonka pumppu näkee.
- **Mittaria ei kiinnitetä suoraan liittimeen**, vaan seinään tai pieneen mittaritauluun luettavaan
  paikkaan ja yhdistetään 1/4":n mittausletkulla (rivit 7.5 ja 7.6). Pumppu ja letku tärisevät,
  PTO:n kytkimen vieressä mittaria on vaikea ja vaarallista lukea käydessä, ja letku suojaa mittaria
  iskuilta. Molemmat imumittarit voivat olla samassa taulussa, myös 2G1:n ja 1G1:n vieressä.
- **Mittausletku täytetään öljyllä** (ilmataan mittarin päästä), ja kaikki liitokset tiivistetään
  huolella: imupuolen vuoto imee ilmaa pumppuun.
- Imupuolella ei tarvita paineiskun vaimenninta.

## 7. Anturit ja mittaus

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 7.1 | Öljyn lämpötila-anturi 3B1 | 1 | varoitus 65 °C, hälytys 70 °C → ESP32 / Signal K | 🛒 päätetty | **⚠ ei tiedossa** | [päätös 2026-10-23](../decisions.md) |
| 7.2 | P2:n lähtöpaineanturi 2B2, 0–400 bar | 1 | ehdotus, prioriteetti 1 | ❓ | **⚠ ei tiedossa** | [pressure-monitoring](design/pressure-monitoring.md#suositus) |
| 7.3 | Ohjauspaineen anturi 1B2, 0–250 bar | 1 | ehdotus | ❓ | **⚠ ei tiedossa** | sama |
| 7.4 | Mittausliittimet (1T1, 2T1, 2T2, 3G2) ja kannettava mittari | 4 + 1 | ehdotus; P1:n imupuolelle (1T2) kiinteä mittari pikaliittimen sijaan, koska pikaliittimen tiiviys alipaineessa on epävarma | ❓ | noin 5–15 € / kpl [arvio] | sama |
| 7.5 | Mittausletku 1/4" (esim. Minimess-mittausletku tai ohut hydrauliletku) ja liittimet | 2 | 1G2:lle ja 2G2:lle; pituus mittaritaulun paikan mukaan **⚠**, suositus enintään noin 3 m; taulu imuaukkojen korkeudelle, koska 1 m:n korkeusero muuttaa lukemaa noin 0,085 bar, ks. [pressure-monitoring](design/pressure-monitoring.md#imupaineen-mittaus) | 🛒 päätetty | **⚠ ei tiedossa** | [päätös 2026-10-28](../decisions.md) |
| 7.6 | Mittaritaulu tai kiinnityslevy (Ø63 mm:n mittareille) | 1 | 1G2 ja 2G2; luettavaan paikkaan konehuoneessa, paikka **⚠ ei päätetty**; 1G1 ja 2G1 voi siirtää samaan tauluun | 🛒 päätetty | **⚠ ei tiedossa** | [päätös 2026-10-28](../decisions.md) |

## 8. Öljy

| # | Osa | Määrä | Tiedot | Tila | Hinta | Lähde |
|---|---|---|---|---|---|---|
| 8.1 | Huuhteluöljy | – | nykyinen Teboil Hydraulic Lift 32 | ✅ | – | [päätös 2026-10-27](../decisions.md) |
| 8.2 | HVLP 32 (esim. Teboil Hydraulic Oil 32S), 20 l | 4 | 80 l täyttö koeajojen jälkeen; tuote päättämättä | 🛒 | noin 420 € (104,90 € / 20 l) | [hydraulic-oil](design/hydraulic-oil.md) |

## 9. Myöhemmin: ankkurivinssi ja painepesuri

| # | Osa | Tiedot | Tila |
|---|---|---|---|
| 9.1 | Ankkurivinssin moottori Danfoss OMP 160 (151-0031) | olemassa [omistaja 2026-10-27] | ✅ |
| 9.2 | Vinssin jarruventtiili | kuorman pito | ⏳ |
| 9.3 | Vinssilohkon paineraja: moottorin päälle laipoitettava kaksoisristivirtausventtiili, esim. [Marchesini VAU 1/2" DE OMP/OMR-moottoreille, 30–180 bar (Flowfit)](https://www.flowfitonline.com/products/dual-cross-line-relief-valve-30-180-bar-for-danfoss-omp-omr-motors-vau-1-2-de-standard) (suositus [arvio]; säätöalueen sopivuus OMP 160:n paine-eroon **⚠ tarkista**), tai peruslohkon vaihto malliin 157B6203/6233 (LS A/B -rajoittimet) | peruslohko 157B6200 ilman rajoittimia (2026-11-03); asetus OMP 160:n mukaan **⚠** | ⏳ |
| 9.4 | Vinssin ja pesurin letkut ja liittimet | | ⏳ |
| 9.5 | Painepesuri | malli **⚠ ei tiedossa** | ⏳ |

## Pois jäävät osat (voi myydä)

PVG 32 -ratkaisussa nämä jäävät käyttämättä: CETOP-pohjalaatta (Flowfit NG6), BAV-713, VPR3,
Rexroth OD15 ja 2/2-patruunaventtiili, Marchesini VMP. Jos PVG 32:n koestus epäonnistuu,
osa niistä tarvitaan varavaihtoehdoissa, joten **ne kannattaa myydä vasta, kun PVG 32 on koestettu**.

Lisäksi vanha P2 (Salami 3PB33D) ja vanha P1 (Salami 2PE16D-P28P1, akseli katkaistu) jäävät käyttämättä [omistaja 2026-11-05, 2026-11-12]. Vanha ryhmän 3 tukilaakeri jää käyttöön uuden P1:n kanssa (päätös 2026-11-13).

## Ennen tilaamista selvitettävät

- [x] PVG 32:n rungon koodit: pumppumoduuli 157B5111 (P G 3/4), peruslohkot 157B6200 (ei PVLP-paikkoja) [datalehti PVG 32, 2026-11-03] (rivit 3.3, 4.12, 4.14, 4.15)
- [ ] PVG 32:n kokoonpanokoodi 157N5531: karat (rivi 4.11)
- [x] PVH57:n laippa- ja porttikoot: imu 2", lähtö 1" (SAE code 61), vuoto 3/4-16 UNF, LS 9/16-18 UNF [Eatonin luettelo V-PUPI-TM008-E1 s. 20–22, 2026-10-28]; tarkista pumpusta ennen tilausta
- [ ] Veneellä: 50 mm:n palloventtiili ja sen kierre (2.1–2.4), 50 mm:n imuletku ja sen pituus (2.5), nykyisen 3/4":n painelinjan kunto (3.2), 2G1:n mittausalue (4.5), säiliön vapaat aukot vuotolinjoille (3.7)
- [ ] Veneellä: onko säiliö maalattu sisältä, ja onko käytettävä jarrunpuhdistin klooriton ([puhdistus](#säiliön-puhdistus-hitsauksen-yhteydessä))
- [x] P1: vaihtoehto B, mitat täsmäävät (päätös 2026-11-13)
- [x] Uuden P1:n liitännät: laippa, laipat vanhasta P2:sta; max 250 bar [omistaja 2026-11-13]
- [ ] Uraholkin kunto ja 1G2:n mittausliitäntä imulaippaan (6.3, 6.9)
- [ ] Taper Lock -holkkien koodit ja HRC 150:n napatyyppi (1.2–1.5)
- [ ] Jäähdyttimen asennus ja paluusuodattimen malli (5.3–5.9)
- [x] Imupuolelle kiinteät kaksoispainemittarit molempiin pumppuihin, mittaritauluun (päätös 2026-10-28)
- [ ] Mittaritaulun paikka konehuoneessa ja mittausletkujen pituus (7.5–7.6); siirretäänkö 1G1 ja 2G1 samaan tauluun
