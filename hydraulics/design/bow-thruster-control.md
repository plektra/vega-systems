# Keulapotkurin portaaton ohjaus: PVEH:n ohjauselektroniikka

> **Tila:** selvitys ja suositus 2026-11-02 (joystick-ehdokkaat lisätty samana päivänä), ei päätetty; sallintarele pidetään suunnitelmassa toistaiseksi (päätös 2026-11-08). Turvallisuuskriittinen: pätevän henkilön
> pitää tarkistaa sallintaketju, kytkentä ja vikatilat ennen käyttöönottoa.

Liittyy: [PVG 32 -selvitys: sähkö ja ohjaus](aux-circuit-ls-clean-sheet.md#ostettu-venttiili-danfoss-pvg-32-5-lohkoa-torifi),
[käsivipu (PVM)](pvg32-lever.md), [vaatimukset §10.2](../requirements.md#102-ohjaus),
[sähköjärjestelmä: ESP32-PDM](../../electrics/current-system.md#4-valvonta-verkot-ja-tehonjako).

## 1. Lähtötilanne

- Keulapotkuri (Side-Power SH240-U11) ohjataan **PVG 32:n lohkosta 1, jossa on PVEH 157B4024
  (24 V, sarja 0)** [päätös 2026-10-27], [kuvasta, ks. PVG 32 -selvitys](aux-circuit-ls-clean-sheet.md#ostettu-venttiili-danfoss-pvg-32-5-lohkoa-torifi).
  Venttiili on ostettu, ja PVE-liittimet tulevat sen mukana [omistaja 2026-11-02].
- P2 on PVH57 ilman PTO-kytkintä; ajossa pumppu on valmiustilassa noin 20 barissa
  [päätös 2026-10-23], [päätös 2026-10-27].
- Vegan DC-jännite on 24 V ([vessel/README.md](../../vessel/README.md)).

## 2. Mitä PVEH tarvitsee

PVEH:ssa on oma säätöelektroniikka ja karan asentoanturi (suljettu säätö). **Se ei tarvitse
erillistä venttiilivahvistinta tai PWM-virtaohjainta**, toisin kuin paljaat proportionaalikelat.
Se tarvitsee vain syötön ja ohjausjännitteen, jota kara seuraa.

| Asia | Arvo | Lähde |
|---|---|---|
| Syöttö U | 22–30 V (Vegan 24 V käy) | [datalehti PVG 32 520L0344 s. 15–18](../../datasheets/README.md) |
| Ohjaussignaali | **suhteessa syöttöön:** keskiasento 0,5 × U, täysi isku 0,25 × U (suunta 1) tai 0,75 × U (suunta 2) | sama |
| Vikavalvonta | kara pysähtyy ja vikasignaali aktivoituu, jos signaali on alueen 15–85 % × U ulkopuolella (myös johdon katketessa) | sama |
| Liitin | Hirschmann DIN, 4-napainen: syöttö, signaali, maa, vikasignaali. Vegan PVE:issä **Hirschmann GDM** (DIN 43650 / EN 175301-803 muoto A), kiinnitysruuvi M3 × 35 [omistaja 2026-11-03, 2026-11-12], ks. [hankintalista 4.17](../procurement.md) | sama |
| Signaalitulon impedanssi | **⚠ ei tiedossa** (vaikuttaa potentiometrin arvoon) | tarkista 520L0344:stä |
| Virrankulutus | **⚠ ei tiedossa** | sama |
| Vikanastan tyyppi ja kuormitettavuus | **⚠ ei tiedossa** | sama |
| Kelpaako PWM suoraan signaaliksi | **⚠ ei tiedossa** | sama |
| Reaktioajat (keski → täysi, täysi → keski) | **⚠ ei tiedossa** | sama |
| Sarjan 0 PVEH:n nastajärjestys | **⚠ tarkista** liittimestä tai Danfossin ohjeesta | |

### Tärkein sudenkuoppa: signaalin on seurattava syöttöjännitettä

24 V:n järjestelmän jännite vaihtelee, latauksessa noin 28,8 V. Jos ohjain antaa kiinteät 12 V
"keskiasennoksi", venttiili näkee 0,417 × U eli kara on noin (0,5 − 0,417) / 0,25 ≈ **kolmanneksen
iskusta auki, ja potkuri pyörii itsestään** [laskelma]. Siksi ESP32:n kiinteä 0–3,3 V:n DAC ja
vahvistin eivät sellaisenaan kelpaa, vaan signaali tehdään PVEH:n omasta syötöstä.

## 3. Vaihtoehdot

| | A. Potentiometrijoystick suoraan | B. ESP32-PDM antaa signaalin | C. CAN-ohjattu PVE |
|---|---|---|---|
| Periaate | joystickin potentiometri samasta 24 V:n syötöstä kuin PVEH; liukuja suoraan signaalinastaan | ESP32:n PWM ohjaa pientä puolisiltaa, jonka käyttöjännite on PVE:n syöttö; RC-suodin tasoittaa lähdön → pulssisuhde × U | PVE vaihdetaan CAN-väyläiseen malliin |
| Seuraa syöttöä | itsestään | itsestään (pulssisuhde 25–75 %) | – |
| Toimii ilman ohjelmistoa | ✅ | ❌ | ❌ |
| Rampit, kuollut alue, useampi ohjauspaikka, kaukosäädin, autopilotti | ❌ (vain joystickin mekaniikka) | ✅ | ✅ |
| Kustannus | joystick ja muutama vastus | oma piirilevylohko ja ohjelmisto | uusi PVE; pelkkä PVEH uutena noin 670 € + ALV ([PVG 32 -selvitys](aux-circuit-ls-clean-sheet.md)), CAN-malli **⚠ hinta ei tiedossa** |
| Arvio | **suositus perusohjaukseksi** | lisätään myöhemmin tarvittaessa | ei tarvita |

Vaihtoehdossa B ESP voisi myös mitata syöttöjännitteen ja korjata kiinteää lähtöä sen mukaan, mutta
se on huonompi tapa: ohjelmistovirhe tai mittausvirhe avaa karan.

### Potentiometrin kytkentä (vaihtoehto A)

```
+24 V (PVE:n sallittu syöttö) ── R_s ──┬── potentiometri R_p ──┬── R_s ── 0 V
                                        └──── liukuja ──► PVEH signaali
```

- **R_s = R_p / 2 kummassakin päässä** rajaa liukujan alueen 0,25–0,75 × U [laskelma]. Esimerkki:
  5 kΩ:n potentiometri ja 2 × 2,4 kΩ → noin 0,245–0,755 × U.
- Ilman sarjavastuksia ääriasento menisi yli 85 %:n ja venttiili menisi vikatilaan.
- Jos potentiometrin pään johto katkeaa, signaali menee 0:aan tai U:hun, ja vikavalvonta pysäyttää
  karan.
- Potentiometrin arvon pitää olla selvästi pienempi kuin PVEH:n signaalitulon impedanssi
  (**⚠ ei tiedossa**), muuten keskiasento siirtyy.
- Joystickin pitää olla **jousipalautteinen**, jotta irti päästetty ohjain palaa keskelle.
- **10 kΩ:n potentiometri (esim. JH-D202X-R4) käy myös:** sarjavastukset 2 × 5,1 kΩ → noin
  0,252–0,748 × U, virta noin 1,2 mA [laskelma]. Lähdön sisäinen vastus keskellä on noin 5 kΩ
  (5 kΩ:n versiolla noin 2,5 kΩ), joten keskiasento on herkempi PVEH:n tulon kuormitukselle. Testi:
  mittaa keskiasennon jännite ilman PVEH:ta ja PVEH kytkettynä; ero alle noin 1 % × U on riittävä
  [arvio]. Jos hinta on sama, 5 kΩ on hieman varmempi.

## 4. Suositus [arvio]: suora joystick ja ESP32-PDM valvojana

```
Hätäseis ── hydrauliikan pääkytkin ── sallintarele (ESP32-PDM voi pudottaa) ──► PVEH:n 24 V:n syöttö
                                                                                │
                                         joystick (potentiometri + R_s) ◄───────┘
                                                │
                                                └── liukuja ──► PVEH signaali
PVEH vikasignaali ──► ESP32-PDM tulo ──► Signal K (hälytys)
joystickin liukuja (jakajan kautta) ──► ESP32 ADC ──► Signal K (käyttötieto)
```

- **Joystick ohjaa PVEH:ta suoraan johdotettuna.** Keulapotkuri toimii, vaikka ohjelmisto tai
  PDM olisi rikki.
- **Sallintaketjussa ovat hätäseis ja hydrauliikan pääkytkin.** PTO-kytkintä ei ole, eikä
  kierroslukitusta tarvita: PVH57 tuottaa vain tarvittavan virtauksen (keulapotkurilla noin
  35 l/min), ja koneen 2400 rpm on pumpun rajoissa, ks.
  [p2-variable-pump](p2-variable-pump.md#sopivuus-vegaan-laskelma).
- **ESP32-PDM voi lisäksi pudottaa sallinnan** hälytyksistä (esim. öljyn lämpötila tai imupaine,
  [vaatimukset §10.1](../requirements.md#101-anturit)). Se on lisäsuoja, ei ainoa suoja.
- **Sallintareleen kytkentä [arvio, lisätty 2026-11-08]:** PVEH:n syöttö kulkee releen
  **lepokoskettimen (NC)** kautta. PDM katkaisee syötön *vetämällä* releen (kela jännitteiseksi),
  eli releellä ei ohjata potkuria päälle. Silloin PDM:n vika, uudelleenkäynnistys tai ohjelmistopäivitys
  ei pysäytä potkuria, ja PDM:n suojaus on vain lisä. Hätäseis ja pääkytkin katkaisevat syötön
  suoraan sarjassa releestä riippumatta. Haittapuoli: jos kelan johto katkeaa, PDM ei pysty
  katkaisemaan; PDM:n lähdön virranmittaus paljastaa katkenneen kelan (ei virtaa, kun lähtö on päällä).
  Releen koskettimen pitää kestää PVEH:n virta (**⚠ tarkista** PVEH:n datalehdestä); kelan virta on
  tyypillisesti kymmeniä milliampeereja, joten pieni PDM-kanava riittää. Jos PDM:n suojausta ei
  haluta, rele jätetään kokonaan pois. **Pätevän henkilön tarkistettava.**
- **Sallintareleen logiikka ja riippuvuus väylästä [arvio, lisätty 2026-11-08]:** hälytystiedot
  (öljyn lämpötila 3B1, imupaine 2B1) tulevat anturinodelta S2 NMEA 2000 -väylän kautta PDM:lle
  ([nmea2000-network 3.11](../../electrics/design/nmea2000-network.md#311-nodejako-lisätty-2026-11-08)).
  Potkurin *toiminta* ei siis riipu väylästä, mutta *katkaisupäätös* riippuu. Siksi:
  1. **Puuttuva, vanhentunut tai alueen ulkopuolinen arvo** (anturivika, alle 4 mA, node
     kadonnut väylältä) antaa vain hälytyksen, ei katkaisua.
  2. **Ei katkaisua käytön aikana:** kun joystick on poikkeutettu (asento S4:ltä tai PVEH:n
     tilasta), PDM vain hälyttää. Sallinta pudotetaan vasta, kun joystick on keskellä, eli uusi käyttö
     estetään, mutta käynnissä oleva liike ei katkea. Jos joystickin asentotieto puuttuu, ei katkaista.
  3. **Viive ja hystereesi:** raja-arvon pitää ylittyä yhtäjaksoisesti (esim. 10–30 s, **⚠ arvio**).
  4. **Ohituskytkin ruorissa** (merkitty, esim. kääntökytkin kelan johtoon), jolla automaattinen
     katkaisu ohitetaan.
  Yksinkertaisin vaihtoehto on jättää automaattinen katkaisu kokonaan pois ja vain hälyttää:
  öljyn kuumeneminen muutamassa minuutissa on vähemmän vaarallista kuin potkurin katoaminen
  rantautumisessa. Omistajat päättävät.

#### Toteutus: ei katkaisua joystickin ollessa käännettynä [arvio, lisätty 2026-11-08]

**Ensisijainen: johdotettu lukitus ilman ohjelmistoa.** Katkaisun voi *aloittaa* vain, kun
joystick on keskellä, ja katkaisu pysyy päällä releen omalla pitokoskettimella:

```
PDM-lähtö (24 V) ──┬── joystickin keskiasentokytkin (kiinni vain keskellä) ──┬──► releen K1 kela ── 0 V
                   └── K1:n sulkeutuva apukosketin (pitopiiri) ─────────────┘

Hätäseis ── pääkytkin ── K1:n avautuva kosketin (NC) ── ohituskytkin rinnalla ──► PVEH 24 V
```

- **Rele K1 on kaksinapainen:** yksi avautuva kosketin (NC) PVEH:n syötölle ja yksi sulkeutuva
  (NO) pitopiirille.
- **Toiminta:** PDM kytkee lähtönsä päälle, kun hälytys on voimassa. Jos joystick on käännettynä,
  keskiasentokytkin on auki, kelaan ei tule virtaa, ja potkuri toimii. Kun joystick palaa keskelle,
  kela saa virran, NC-kosketin katkaisee PVEH:n syötön, ja NO-kosketin pitää kelan päällä, vaikka
  joystickia käännettäisiin taas. Katkaisu päättyy vasta, kun PDM kytkee lähtönsä pois.
- **Riippumaton väylästä ja ohjelmistosta:** ohjelmistovirhe, väylä tai anturinode S4 eivät voi
  katkaista potkuria kesken liikkeen, koska keskiasentokytkin estää sen fyysisesti.
- **Keskiasentokytkin:** suositeltu JH-D202X-R2 -joystick ei sisällä sellaista. Vaihtoehdot:
  mikrokytkin, jota joystickin varsi painaa keskiasennossa (sopii suunniteltuun 3D-tulostettuun
  uraohjaimeen), joystick jossa kytkin on valmiina (esim. Danfoss PVREL 155U2605, kallis), tai
  ikkunavertailija joystickin signaalista (lisäelektroniikkaa, ei suositeltu). Kytkimen
  sulkeutumisalueen pitää olla PVEH:n kuolleen alueen sisällä (**⚠ tarkista** PVEH:n datalehdestä).
- **Vikatilat:** keskiasentokytkin jumittuu auki → PDM ei pysty katkaisemaan, potkuri toimii (hälytys
  jää). Jumittuu kiinni → katkaisu voi tapahtua kesken käytön, kuten ilman lukitusta; ohituskytkin
  palauttaa toiminnan. K1:n pitokosketin jumittuu kiinni → katkaisu ei vapaudu PDM:n käskystä;
  ohituskytkin palauttaa toiminnan.

**Toissijainen: ohjelmistotarkistus PDM:ssä.**

- Anturinode S4 mittaa joystickin liukujan jännitteen ja syöttöjännitteen ja laskee niiden suhteen
  (keskiasento 0,5; PVEH:n ohjausalue 0,25–0,75). Se lähettää asennon väylään, esim. NMEA 2000:n
  keulapotkuriviestillä 128006 *Thruster Control Status* (kenttien käyttö **⚠ tarkista**) ja
  Signal K:hon.
- PDM kytkee lähtönsä vain, kun (1) hälytysehto on voimassa viiveen yli, (2) S4:n tuore viesti
  (alle noin 1 s vanha) kertoo joystickin olleen keskellä (esim. 0,5 ± 0,03, **⚠ arvio**) vähintään
  noin 2 s ja (3) ohituskytkin ei ole päällä. Puuttuva tai vanha asentotieto → ei katkaisua, vain
  hälytys.
- **Sallinnan palautus** (PDM-lähtö pois) tehdään myös vasta joystickin ollessa keskellä, jotta
  potkuri ei käynnisty nykäyksellä, jos joystick on palautushetkellä käännettynä. Miten PVEH toimii,
  kun syöttö palaa signaalin ollessa keskiasennon ulkopuolella, **⚠ tarkista** PVEH:n datalehdestä.
- Ohjelmistotarkistus on lisäkerros; johdotettu lukitus estää katkaisun kesken käytön, vaikka
  ohjelmisto toimisi väärin.

**Hankintoihin tämän myötä:** kaksinapainen 24 V:n rele (NC + NO), keskiasennon mikrokytkin ja
merkitty ohituskytkin. **Pätevän henkilön tarkistettava ennen rakentamista.**
- ESP32 lukee vikanastan ja joystickin asennon ja vie ne Signal K:hon. Joystickin jännite pitää
  jakaa ESP:n ADC-alueelle; suhteellisuuden vuoksi myös syöttöjännite mitataan.
- **Käsivipu (PVM)** on varaohjaus veneen sisällä, jos sähköohjaus pettää, ks.
  [pvg32-lever.md](pvg32-lever.md).
- **Kaksi ohjauspaikkaa tai kaukosäädin myöhemmin:** kahta potentiometria ei voi kytkeä rinnan.
  Tarvitaan valintarele (vain yksi paikka kerrallaan) tai vaihtoehto B. Ohjauspaikkojen määrä on
  vielä auki ([vaatimukset §10.2](../requirements.md#102-ohjaus)).

### Joystick-ehdokkaat (haettu 2026-11-02)

| Ehdokas | Ominaisuudet | Hinta ja saatavuus | Arvio |
|---|---|---|---|
| **JH-D202X-R2 5K** (yleinen kiinalainen teollisuusjoystick) | 2 akselia, kummassakin 5 kΩ:n potentiometri, **jousipalautus keskelle**; myydään nimellä "sealed", IP-luokka **⚠ ei tiedossa**; potentiometrin teho **⚠ tarkista** (24 V:lla ja 2 × 2,4 kΩ:n sarjavastuksilla virta noin 2,4 mA ja teho potentiometrissa noin 30 mW [laskelma]) | **noin 11–23 $ kpl** ([eBay](https://www.ebay.de/itm/397463974050), [Abra 22,52 $](https://abra-electronics.com/electromechanical/switches/arcade-game-switches/2d-2-axis-joystick-potentiometer-5k.html)); tukkuna noin 5 $ ([ship4wd](https://sourcing.ship4wd.com/product/two-dimensional-rocker-potentiometer-2d-joysticks-jh-d202x-r2r4-5k10k-optional-neutral-packaging)) | **Suositus kustannussyistä.** Käytetään yhtä akselia; liike rajataan yhteen suuntaan uraohjaimella (esim. 3D-tulostettu levy, jossa vain paapuuri–styyrpuuri-ura). Sarjavastukset §3:n mukaan. Ei keskiasentokytkintä. Ohjauspaikalla katon alla tai kumisuojan kanssa. Kannattaa ostaa kaksi (varaosa) |
| Danfoss PVREL 155U2605 | Danfossin oma potentiometriohjain PVE-venttiileille: yksi proportionaalinen toiminto, **jousipalautus keskelle, keskiasentokytkin**, IP65 paneelin yläpuolella; sarjan tiedot: syöttö 11–30 V, lähtö 0,25–0,75 (× syöttö **⚠ tarkista**), aaltoisuus enintään 5 %, virrankulutus < 80 (yksikkö puuttuu sivulta, todennäköisesti mA **⚠ tarkista**) | **426,56 € + ALV** (516,14 € sis. ALV), varastossa, toimitus EU-varastosta ([Technotrade](https://eshop.technotrade.cz/en/joystick-pvrel-155U2605)) | Teknisesti helpoin (ei sarjavastuksia, keskiasentokytkin sallintaketjuun), mutta **omistajien mielestä liian kallis** [omistaja 2026-11-02]. Hydrauvisionilla halvempi, noin 338 € + ALV (hakutuloksen ote) |
| Danfoss PVREL 155U2601 | jousipalautus, ei keskiasentokytkintä | 309,90 € + ALV, **poistunut** ([Technotrade](https://eshop.technotrade.cz/en/joystick-pvrel-155U2601)) | halvempi, jos jostain löytyy; kysy korvaava malli |
| Danfoss PVREL 155U2602 | jousipalautus ja kitkajarru, ei keskiasentokytkintä; syöttö 11–30 V, lähtö 0,25–0,75, IP67 (Hydraspecma) tai IP44 (Findynamica) **⚠ ristiriita** | 591,30 € + ALV ([Findynamica](https://www.findynamica.nl/en/shop/product/joystick-pvrel-2-way-spring-returnfriction-brake-155u2602)); Suomessa [Hydraspecma](https://www.hydraspecma.com/store/fi/en/find/item/155U2602/joystick-46), hinta ei näy | kitkajarru ei sovi keulapotkurille (ohjain ei palaa itse keskelle) |
| Matend MKF-PJS02 (kiinalainen teollisuusjoystick) | 1 tai 2 akselia, jousipalautus, potentiometri 5 tai 10 kΩ, < 36 V, IP65 paneelin yläpuolella, ±25° ([Matend](https://www.matend.com/product/mkf-pjs02-potentiometer-joystick-single-dual-axis-spring-return/)) | **⚠ ei tiedossa** (vain tarjouspyyntö) | edullinen vaihtoehto; tarvitsee sarjavastukset (§3) eikä keskiasentokytkintä ole mainittu |
| Muut teollisuusjoystickit: APEM, Megatron 829, Sentop JP50A, RS PRO 1730770 | yksiakselisia potentiometrijoystickeja, IP65 | APEM 1-akselinen noin 138 $ (yhden jälleenmyyjän sivu, päiväys epäselvä); muut **⚠ ei tiedossa** | vertailukohtia; tarkista jousipalautus ja potentiometrin arvo |
| Käytetty Danfoss PVRE, PVREL tai PVRES | hae osanumeroilla (155U26xx, 162F13xx) tori.fi:stä ja eBaysta | **⚠ ei tiedossa**; uusi PVRES 1x noin 590–690 € + ALV | voi olla edullisin, jos löytyy |

**Hall-anturijoystickit** [haettu 2026-11-02]: ei kuluvaa liukukoskettinta (esim. Matend MKF-PJS02:
Hall yli 5 milj., potentiometri yli 2 milj. liikettä). Tavallisissa Hall-joystickeissa syöttö on
kuitenkin 5 V ja lähtö noin 0,5–4,5 V, joka ei seuraa PVEH:n syöttöä, joten ne eivät käy suoraan.
Suoraan käyvät vain PVE-lähdölliset mallit, esim. Danfoss JS1-H (PVE-versio: 9–36 V, lähtö
0,25–0,75 × U, kaksi rinnakkaista anturia) ja Danfoss JS120 / Penny & Giles JC120 25–75 %:n lähdöllä
([Danfoss JS1 -datalehti](https://www.alldatasheet.net/html-pdf/1814565/DANFOSS/JS1/1028/3/JS1.html),
[JS120](https://manualshive.com/en/manual/danfoss/js120/3470777?page=11)); hinta **⚠ ei tiedossa**,
todennäköisesti PVREL:n luokkaa [arvio]. Halpa 5 V:n Hall-joystick sopii vaihtoehtoon B (ESP32
tekee signaalin). Vikatila: yhden anturin Hall-elektroniikka voi jäädä antamaan väärää mutta
sallitulla alueella olevaa arvoa, jota PVEH:n vikavalvonta ei huomaa; JS1-H:n kaksi anturia
suojaavat tältä. **Arvio:** potentiometrijoystick riittää keulapotkurin käyttömäärille; Hall
harkitaan, jos ohjaus siirretään ESP32:lle.

Halvat 2-akseliset harrastejoystickit (muutama euro) eivät sovi: ne eivät ole tiiviitä, ja niiden
jousi ja mekaniikka eivät kestä veneen ohjauspaikalla [arvio].

**Suositus [arvio]:** JH-D202X-R2 5K, yhden akselin uraohjain ja kaksi sarjavastusta: noin
20–40 € kotelointeineen **⚠ arvio**. PVREL on teknisesti valmiimpi, mutta omistajien mielestä liian
kallis [omistaja 2026-11-02]. Koska keskiasentokytkintä ei ole, hätäseis on tärkein suoja jumittunutta
ohjainta vastaan (§5). Ennen asennusta mitataan potentiometrin arvo ja keskiasennon jännite 24 V:lla
ja noin 28 V:lla.

**Vielä halvempi, mutta ei portaaton:** jousipalautteinen keinukytkin (ON–OFF–ON) ja vastusjakaja.
Keskellä kaksi samanarvoista vastusta R antaa 0,5 × U; kytkin kytkee alempaan tai ylempään
vastukseen rinnalle R/2:n, jolloin signaali on 0,25 × U tai 0,75 × U [laskelma]. Tämä on käytännössä
nykyisen on/off-ohjauksen kaltainen; välinopeuksia saa lisäämällä kytkinasentoja.

## 5. Vikatilat

| Vika | Seuraus | Suoja |
|---|---|---|
| Sähkökatko tai hätäseis | Jouset palauttavat karan keskelle; potkuri pysähtyy ja pyörii vapaasti avoimen keskiasennon kautta | Sallintaketju katkaisee PVEH:n syötön |
| Joystickin tai signaalijohdon katkos | Signaali alueen 15–85 % ulkopuolella → kara pysähtyy, vikasignaali | PVEH:n vikavalvonta; hälytys Signal K:hon |
| Joystick jumittuu taipuneena | Potkuri jää pyörimään | Hätäseis; käyttäjä näkee potkurin toiminnan. Harkitse joystickia, jossa on keskiasentokytkin sallintaketjussa **⚠ ei päätetty** |
| Signaali ei seuraa syöttöä (väärä kytkentä, kiinteä lähde) | Kara aukeaa osittain ilman ohjausta | Kytkentä aina PVEH:n omasta syötöstä; käyttöönotossa tarkistetaan keskiasento kahdella syöttöjännitteellä |
| PVEH:n sisäinen vika, kara jumissa | Potkuri pyörii tai ei pyöri | Vikasignaali, hätäseis, venttiilin paineenrajoitin rajaa paineen |
| ESP32-PDM vikaantuu | Valvonta ja hälytykset puuttuvat; perusohjaus toimii | Sallintareleen kytkentä niin, ettei PDM:n vika estä hätäseisiä **⚠ suunnittele** |
| NMEA 2000 -väylä, anturinode S2 tai anturi vikaantuu (lisätty 2026-11-08) | Lepokosketinkytkennällä potkuri toimii; PDM ei saa hälytystietoja eikä katkaise. **Vaara on väärä katkaisu:** viallinen anturi tai virheellinen arvo voisi pysäyttää potkurin kesken rantautumisen | Ks. alla *Sallintareleen logiikka* |

## 6. Käyttöönotto

1. Mittaa sarjan 0 PVEH:n nastajärjestys ja tarkista arvot 520L0344:stä (§2:n avoimet rivit).
2. Kokeile PVEH 24 V:lla ja potentiometrilla ilman painetta: kara liikkuu, keskiasento pitää ja
   vikasignaali toimii (myös [PVG 32 -selvityksen koestus](aux-circuit-ls-clean-sheet.md#puhdistus-ja-koestus)).
3. Tarkista, että keskiasento pysyy 24 V:lla ja noin 28 V:lla.
4. Paineen kanssa: ensin pieni ohjaus, sitten täysi, kuten PVG 32 -selvityksen käyttöönotossa.

## 7. Avoimet kysymykset

- [ ] PVEH 520L0344: signaalitulon impedanssi, virrankulutus, vikanastan tyyppi, PWM-signaalin
      kelpoisuus, reaktioajat
- [ ] Sarjan 0 PVEH:n (157B4024) nastajärjestys
- [ ] Joystickin valinta: ehdokkaat kirjattu (suositus JH-D202X-R2 5K, noin 11–23 $; PVREL liian kallis [omistaja 2026-11-02]); omistajat päättävät. Tarkista PVREL:n datalehdestä lähdön suhteellisuus syöttöön, liitäntä ja keskiasentokytkimen kuormitettavuus
- [ ] Ohjauspaikkojen määrä ja sijainnit ([vaatimukset §10.2](../requirements.md#102-ohjaus))
- [ ] Sallintareleen ja hätäseisin kytkentä sekä ESP32-PDM:n rooli siinä (pätevä henkilö tarkistaa)
- [x] Sallintarele pidetään suunnitelmassa toistaiseksi (lepokosketin, katkaisulogiikka yllä) [päätös 2026-11-08](../../decisions.md)
- [ ] Omistajat: lopullisesti automaattinen katkaisu vai pelkkä hälytys (rele pois)?
- [ ] Sallintareleen malli: kaksinapainen (NC + NO), koskettimen virta PVEH:n mukaan (**⚠ tarkista** PVEH:n datalehdestä), kela 24 V; ohituskytkimen malli ja merkintä
- [ ] Joystickin keskiasentokytkin: mikrokytkin uraohjaimeen; kytkimen sulkeutumisalue PVEH:n kuolleen alueen sisällä
- [ ] PVEH:n toiminta, kun syöttö palaa signaalin ollessa keskiasennon ulkopuolella (datalehti)
- [ ] Omistajat: perusohjaus suoralla joystickilla (suositus) vai heti ESP32-signaalilla
