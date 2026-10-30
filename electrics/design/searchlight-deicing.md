# Hakuvalon jäänpoisto

> **Tila:** Selvitys, aloitettu 2026-10-30, päivitetty 2026-10-30 (ESP32-PDM-repon päätökset 16 ja 19; lasin paksuus). Ei päätöstä. Hakuvalon malli, polttimon tyyppi ja
> ohjaustapa ovat **⚠ ei tiedossa**, ja ne ratkaisevat, mikä vaihtoehto sopii. Hinnat ja tehot on
> haettu verkosta, eikä niitä ole tarkistettu valmistajilta.

Tavoite: hakuvalon pitää toimia myös syksyllä ja keväällä, kun etulasiin ja kääntömekanismiin
tarttuu jäätä, räntää tai jäätyvää roisketta. Lähtötiedot: hakuvalo on olemassa mutta asentamatta,
24 V, 500 W (noin 21 A) [omistaja 2026-10-29]. Sijainniksi on kaapelilaskelmissa oletettu maston
huippu ([dc-distribution.md 4.2](dc-distribution.md)), **⚠ tarkista**.

**Liittyy ESP32-PDM-repoon** ([plektra/ESP32-PDM](https://github.com/plektra/ESP32-PDM)):

- **Päätös 16 (auki):** *"an edge heater ring is not enough for de-icing; a film-type heater is
  preferred, but cost must be reviewed before deciding"*, eli reunaan asennettava lämmitinrengas ei
  riitä jäänpoistoon, kalvolämmitin on parempi, mutta kustannus pitää tarkistaa ennen päätöstä
  ([decisions.md](https://github.com/plektra/ESP32-PDM/blob/main/docs/decisions.md)) [ESP32-PDM 2026-10-30].
  Perustelua ei ole kirjattu.
- **Päätös 19 (ehdotus):** noin 21 A:n hakuvalo vaatii suurivirtaiseen `pdm-hc2`-korttiin
  pienemmän resistanssin MOSFETit (ehdokas onsemi NTMFS5C612NL). **Halogeenin käynnistysvirta**
  on noin 10–15-kertainen kymmenien millisekuntien ajan, joten kortin 80 A:n nopea
  oikosulkulaukaisu katkaisisi kylmän 500 W:n polttimon. Vaihtoehdot: LED-hakuvalo tai nopean
  laukaisun poisto MOSFETien pulssikestoisuuden (SOA) tarkistuksen jälkeen
  ([design-notes.md §4a](https://github.com/plektra/ESP32-PDM/blob/main/docs/design-notes.md)) [ESP32-PDM 2026-10-30].
- PDM:n laiteohjelmistoon on suunniteltu **lämmittimen termostaattitoiminto**, ja veneeltä
  pyydetään mittaamaan **etulasin halkaisija ja paksuus** ([CONTINUE-FROM-HERE.md](https://github.com/plektra/ESP32-PDM/blob/main/docs/CONTINUE-FROM-HERE.md)).

Halogeeni vai LED ratkaisee siis sekä jäänpoiston että PDM-kortin osavalinnan.

## 1. Ensin pitää tietää polttimon tyyppi

Jäätyykö lasi ylipäätään käytön aikana, riippuu siitä, missä lampun hukkalämpö syntyy:

| Polttimo | Mihin hukkalämpö menee | Pysyykö etulasi sulana valon palaessa? |
|---|---|---|
| **Halogeeni** (tai ksenon) | Lähes kaikki 500 W:sta on lämpöä, ja se säteilee heijastimesta suoraan etulasiin | **Kyllä, käytännössä.** Polttimo sulattaa lasin itse, kun valo on päällä [laskelma, perustelu alla] |
| **LED** | Lämpö johdetaan LEDien takana olevaan jäähdytysrivoitukseen | **Ei.** Etulasi on lähes ulkoilman lämpöinen, ja jää ja huurre jäävät lasiin |

**Perustelu halogeenille [laskelma, arvio]:** halogeenipolttimon näkyvän valon hyötysuhde on
luokkaa 2–3 % sähkötehosta (yleinen tieto halogeenilampuista, **⚠ tarkista**), joten noin 480 W
500 W:sta on lämpöä. Sen rinnalla jäänpoistoon tarvittava teho on pieni (kohdat B ja C: kymmeniä watteja).
**Tekniikan vertailua:** Carlisle & Finchin halogeenihakuvaloissa jäänestolämmitin on vain
*moottoroidun jalustan* sisällä, ei etulasissa ([19" halogen searchlight](https://carlislefinch.com/searchlights/19-inch-halogen-searchlight/),
[10" LED -datalehti](https://carlislefinch.com/wp-content/uploads/2024/03/10-inch-LED-7.Pg-C.pdf)).
Sama valmistaja ei siis lämmitä halogeenimallien lasia erikseen.

500 W 24 V:lla viittaa halogeeniin, sillä 500 W:n LED-hakuvalot ovat harvinaisia; tämä on
**päättely, ei tieto (⚠ tarkista tyyppikilvestä)**.

**Kaksi eri ongelmaa:**

1. **Etulasin jää ja huurre** – valo ei pääse läpi.
2. **Kääntömekanismin jäätyminen** – kauko-ohjatun valon moottorit ja laakerit jumittuvat, tai
   käsikäyttöisen valon kahva ja kitkajarru jäätyvät.

## 2. Vaihtoehdot

### A. Ilman lämmitintä: suojahuppu, esilämmitys ja pinnoite (halvin)

- **Suojahuppu** (kangas tai muovi) lasin eteen, kun valoa ei käytetä. Huppu pitää lasin ja
  usein myös nivelen kuivana. Hinta muutamia kymmeniä euroja, voi tehdä itse **⚠ arvio**.
- **Kääntäminen pois tuulesta / lasi alaspäin** pysäköintiasennossa vähentää roiskeen
  tarttumista, jos jalusta sen sallii **⚠ tarkista mallista**.
- **Halogeenivalo päälle hetki ennen tarvetta:** lasi sulaa itsestään. Kuinka kauan paksun jään
  sulaminen kestää, on **⚠ ei tiedossa**; kokeillaan veneellä.
- **Vettä hylkivä lasipinnoite** (tuulilasien sadepinnoitteiden tapaan) vähentää jään
  tarttumista, mutta ei estä jäätymistä. Apukeino, ei ratkaisu.

**Varoitus lämpöshokista:** jos paksusti jäätyneeseen lasiin sytytetään 500 W:n halogeeni, lasi
lämpenee epätasaisesti. Hakuvalojen etulasit ovat yleensä karkaistuja (esim. Den Haan Rotterdam
ilmoittaa "hardened front glass", toiminta −25 °C:seen asti:
[DHR 230DS](https://www.dhr.nl/sites/default/files/userfiles/Producten/Searchlights/Downloads/A00DOC-ZL0003%20-%20RevB.pdf)),
mutta oman valon lasin kestävyys on **⚠ tarkista** valmistajalta.

### B. Lämmitin jalustaan tai runkoon (kääntömekanismin jäänesto)

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
- Tarvitaan vain, jos valo on **kauko-ohjattu** tai jos jäätyvä kahva/nivel haittaa käsikäyttöä.

### C. Etulasin lämmitys (tarpeen lähinnä LED-valossa)

| Tapa | Miten | Teho **⚠ arvio** | Huomiot |
|---|---|---|---|
| **C1. Lämmitin lasin reunaan** | Silikonilämmitysnauha tai PTC-elementti lasin kehyksen sisäpuolelle | noin 10–30 W | Halvin ja yksinkertaisin. Lämpö kulkee reunoilta, joten lasin keskusta sulaa viimeisenä. **ESP32-PDM:n päätöksen 16 mukaan reunarengas ei riitä jäänpoistoon** (ks. yllä); lasin halkaisija ja paksuus ratkaisevat, ulottuuko reunalämpö keskelle. Valon tiiviys (IP) on palautettava avauksen jälkeen |
| **C2. Läpinäkyvä lämmityskalvo lasin sisäpintaan** (ITO tai metalliverkko) | Kalvo liimataan lasiin ja kytketään 24 V:iin | mitoitetaan pinta-alan mukaan | Bopla ilmoittaa kalvolleen enintään 3000 W/m², +85 °C ja läpäisyn enintään 93 % ([Bopla, transparente Folienheizung](https://www.bopla.de/fileadmin/user_upload/Transparente_Folienheizung-EN_web.pdf)); 24 V:n valmista liimakalvoa ei löytynyt. **Ei sovi halogeenivaloon**, koska lasi kuumenee yli 85 °C:n **⚠ tarkista**. Läpäisy vähentää valoa muutaman prosentin |
| **C3. Valmis lämmitetyllä ikkunalla varustettu valo** | Esim. **Glamox SL1IR / SL2IR** (LED + lämpökamera, lämmitetty ikkuna) ([SL1IR](https://citimarinestore.com/en/glamox-marine-lightning/22177-glamox-sl1ir-led-searchlight-with-thermal-night-vision.html), [SL2IR](https://citimarinestore.com/en/glamox-marine-lightning/22171-glamox-sl2ir-led-searchlight-with-integrated-thermal-camera.html)) | **⚠ ei tiedossa** | Kallis, ja nykyinen valo jäisi käyttämättä. SL2IR:n jännite ei selvinnyt. Mukana lämpökamera, josta voi olla hyötyä muutenkin |

**Etulasin paksuus on noin 5 mm** [omistaja 2026-10-30]; halkaisija **⚠ ei tiedossa**.

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
tunkeutumismatkan päässä. Jos lasin halkaisija on esim. 200 mm (säde 100 mm), reunarengas
sulattaa tuulessa vain noin 2–4 cm leveän kehän, ja keskusta jää jäähän. Tämä tukee
ESP32-PDM:n päätöstä 16: lämpö on tuotava koko lasin pinnalle (kalvo, C2).

Lasin pinta-alan laskemiseen tarvitaan etulasin halkaisija (**⚠ ei tiedossa**). Esimerkki:
Ø 200 mm:n lasi on 0,031 m²; 500 W/m² antaisi noin 16 W [laskelma, oletettu halkaisija].

## 3. Ohjaus ja kytkentä

- **Halogeenin käynnistysvirta:** kylmän 500 W:n halogeenipolttimon hetkellinen virta on noin
  10–15 × 21 A eli noin 200–300 A kymmenien millisekuntien ajan [ESP32-PDM design-notes §4a,
  laskelma]. Puolijohdekytkin tai sulake on mitoitettava sen mukaan (ks. PDM:n päätös 19).

- **Kytkin komentosillalle** (KS-alakeskus, [dc-distribution.md 2.2](dc-distribution.md#22-komentosillan-alakeskus-ks))
  ja merkkivalo. Lämmitin ei saa jäädä huomaamatta päälle ankkurissa.
- **Automaatio:** ESP32-PDM voi kytkeä lämmittimen, kun ulkolämpötila on alle noin +3 °C ja vene
  on ajossa (tieto Signal K:sta). Lämpötilaraja on **⚠ arvio**.
- **Kaapeli:** 0,8 A:n lämmitin ei muuta hakuvalon kaapelin kokoa (21 A, 2,5–10 mm²,
  [dc-distribution.md 4.2](dc-distribution.md)). Jos lämmitin halutaan päälle ilman valoa, se
  tarvitsee oman johtimen mastoon: 1,5 mm² riittää mekaanisen kestävyyden vuoksi [laskelma].
- **Paloturvallisuus:** lämmitin ja sen johdot pitää kiinnittää niin, etteivät ne osu
  halogeenipolttimoon tai heijastimeen. Liimanauhat ja silikonimatot eivät kestä polttimon
  läheisyyttä.

## 4. Suositus (alustava)

1. **Selvitä ensin hakuvalon malli, polttimo ja ohjaustapa** tyyppikilvestä (valokuva riittää).
2. **Jos valo on halogeeni ja käsikäyttöinen:** erillistä lämmitintä ei luultavasti tarvita.
   Suojahuppu ja valon sytyttäminen hetkeä ennen tarvetta riittävät (vaihtoehto A, kustannus
   pieni). Kokeillaan ensimmäisenä pakkasajona.
3. **Jos valo on kauko-ohjattu:** lisäksi 20 W:n PTC-lämmitin jalustaan (vaihtoehto B, osan hinta
   **⚠ ei tiedossa**, arviolta kymmeniä euroja).
4. **Jos valo on LED:** lisäksi lasin lämmitys. ESP32-PDM:n päätöksen 16 mukaan reunarengas
   (C1) ei riitä, joten lähtökohta on kalvolämmitin (C2), kunhan sen hinta on selvitetty. Uusi
   lämmitetty valo (C3) vasta viimeisenä, koska nykyinen valo on jo olemassa.
5. **Halogeenin etu:** lasia ei tarvitse lämmittää erikseen. **Haitta:** suuri käynnistysvirta
   PDM-kortille (päätös 19). Valinta kannattaa tehdä yhdessä PDM:n kanssa.

## 5. Avoimet kysymykset

- [ ] Hakuvalon valmistaja ja malli (tyyppikilpi tai valokuva)
- [ ] Polttimo: halogeeni, ksenon vai LED?
- [ ] Ohjaus: käsikäyttöinen kahvalla vai kauko-ohjattu (moottorit)?
- [ ] Sijainti: maston huippu vai komentosillan katto?
- [x] Etulasin paksuus: noin 5 mm [omistaja 2026-10-30]
- [ ] Etulasin halkaisija ja materiaali (karkaistu lasi vai muovi); pyydetty myös ESP32-PDM-repossa
- [x] Miksi reunarengas ei riitä (ESP32-PDM:n päätös 16): lasi johtaa lämpöä huonosti, ja reunan lämpö ulottuu vain noin 1–2 cm (kohta C, laskelma)
- [ ] Kalvolämmittimen hinta (ESP32-PDM:n päätös 16)
- [ ] Kuinka paljon Vegalla ajetaan pakkasella tai jäätyvässä roiskeessa (kuukaudet)?
- [ ] Kestääkö etulasi lämpöshokin, kun jäätyneeseen lasiin sytytetään valo (valmistajalta)
