# AC-sähkön lähde: hydrauligeneraattori, dieselgeneraattori vai akusto ja invertteri

> **Tila:** Selvitys, aloitettu 2026-10-28, päivitetty 2026-10-31 (Timco SS2200i varalataukseen päätetty, kohta D; kaasuliesi, yhdistetty mikro- ja sähköuuni, septi-WC polttavan WC:n tilalle; akustotarve laskettu uudelleen). Ei päätöstä. Hinnat puuttuvat; ne tarkistetaan
> tarjouksista ennen päätöstä.

## 1. Tarve

| Kohde | Arvo | Lähde |
|---|---|---|
| Milloin AC-sähköä tarvitaan | Ajossa ja ankkurissa | [omistaja 2026-10-28] |
| Generaattori | Ei asennettu; tila varattu konehuoneen paapuurin puolelle | [omistaja 2026-10-28], [blogi 2017-04-19] |
| Sähkökiuas (**päätetty** 2026-10-29; ankkurissa suurin energiankuluttaja) | 2,3 kW, päällä kerrallaan noin 2 h. Puukiuas ei mahdu saunaan | [omistaja 2026-10-28], [omistaja 2026-10-29] |
| Muut AC-kuormat | Jääkaappi (noin 130 l ja pakastelokero), laturit (esim. kannettava tietokone), kahvinkeitin, vedenkeitin, yhdistetty mikro- ja sähköuuni, liesituuletin, poistoilmapuhallin, ilmanvaihtokone, televisio, öljylämmityksen poltin (alle 1 A), vedenlämmittimen sähkövastus 3 kW. **Vain jääkaappi on olemassa. Päätetty: sähkökiuas (2026-10-29), kaasuliesi ja yhdistetty mikro- ja sähköuuni (2026-10-31); jätteet polttava WC hylätty, tilalle septi-WC maseraattorilla (24 V) [omistaja 2026-10-31];** muut ovat harkinnassa, eikä kaikkia välttämättä asenneta. Tehot: [loads.yaml](../loads.yaml) | [omistaja 2026-10-28] |
| Maasähkö | Kotilaiturissa 15 A:n sulake (≈ 3,45 kVA, jos 1-vaiheinen 230 V; vaiheiden määrä **⚠ tarkista**) | [omistaja 2026-10-28] |
| Erotusmuuntaja | Airlink WM5002, 230/230 V, 5000 VA; olemassa, ei kytketty, ks. kohta 2.6 | [omistaja 2026-10-28] |
| Kuinka monta vuorokautta ankkurissa ilman ajoa | **Enintään alle vuorokausi** | [omistaja 2026-10-29] |
| DC-jännite | 24 V | [vessel/README.md](../../vessel/README.md#sähköjärjestelmän-perustiedot) |

Kokonaistarve on alle 10 kVA. Kiuas on suurin energiankuluttaja ankkurissa; ilmanvaihtokone,
lämmityksen poltin ja sähköinen ruoanlaitto kuluttavat yhdessä vähän sitä vähemmän (ks. kohta 2.1).

Koska vain jääkaappi on olemassa, laitevalinnat ovat vielä auki. **Jokainen sähkölaite kasvattaa
akustoa, ja juuri nyt on halvin hetki valita laitteet energiankulutuksen perusteella.**

## 2. Kiukaan energiatarve akustosta [laskelma]

Oletukset: kiuas ottaa täyttä tehoa koko kaksi tuntia (yläraja; termostaatti katkoo lämpenemisen
jälkeen, joten todellinen kulutus on todennäköisesti pienempi), invertterin hyötysuhde 90 %,
LiFePO4-akuston käytettävissä oleva osuus 80 %, jännite 24 V.

**Todennäköinen kulutus on ylärajaa pienempi** [omistaja 2026-10-29]: termostaatti katkoo
vastukset, kun sauna on lämmin. Arvio (**⚠ arvio**, mitataan käytössä): lämpeneminen noin 1 h
täydellä teholla (2,3 kWh) ja sen jälkeen noin 1 h keskimäärin noin 60 %:n teholla (≈ 1,4 kWh),
yhteensä **noin 3,7 kWh** eli akustosta noin **4,1 kWh** (yläraja 5,1 kWh). Lämpenemisaika ja
termostaatin käyttösuhde riippuvat saunan koosta ja eristyksestä. Alla olevat mitoitukset on
laskettu ylärajalla, joten niissä on noin 1 kWh:n varmuusvara saunavuoroa kohden. Todellisen
kulutuksen näkee invertterilaturin tai akkumonitorin tiedoista ensimmäisillä saunakerroilla.

| Suure | Arvo |
|---|---|
| Energia kiukaalle | 2,3 kW × 2 h = 4,6 kWh |
| Energia akustosta | 4,6 / 0,9 ≈ 5,1 kWh |
| Akkuvirta kiukaan ollessa päällä | 2300 / 0,9 / 24 ≈ 106 A |
| Kiukaan vaatima kapasiteetti | 5,1 kWh / 24 V ≈ 213 Ah käytettävissä → ≈ 265 Ah nimelliskapasiteettia |
| Akusto | Muut kuormat ja 24 V:n kuormat mukaan lukien noin 16 kWh (≈ 630 Ah @ 25,6 V); saunapäivänä käytössä noin 76–83 % (päivitetty 2026-10-31), ks. [house-battery.md](house-battery.md) |
| Invertteri | Noin 3,5 kW, ks. kohta 2.2 |

### 2.1 Koko ankkurivuorokauden energiatarve [laskelma]

Laskelma on **yläraja**: siinä ovat mukana kaikki harkinnassa olevat laitteet. **Päivitetty 2026-10-31:**
liesi on kaasuliesi, ja uunin tilalle tulee yhdistetty mikro- ja sähköuuni [omistaja 2026-10-31]. Pelkkä olemassa
oleva jääkaappi vie noin 0,8 kWh/vrk (≈ 0,9 kWh akustosta, arvio).

Vain kiukaan, vedenlämmittimen (3 kW) ja polttimen virran (alle 1 A) arvot ovat omistajalta. Muiden
laitteiden tehot ja kaikki käyttöajat ovat **arvioita** tyypillisistä kodinkoneista
([loads.yaml](../loads.yaml)); ne pitää korvata laitteiden tyyppikilpien arvoilla. Poistoilmapuhallin
puuttuu summasta, koska sen käyttöaikaa ei tiedetä. Vedenlämmittimen vastus on jätetty pois, ks.
kohta 4.

| Kuormaryhmä | kWh/vrk (arvio) |
|---|---|
| Sähkökiuas, 2 h | 4,6 (yläraja; todennäköisesti noin 3,7) |
| Ruoanlaitto: yhdistetty mikro- ja sähköuuni, vedenkeitin, kahvinkeitin, liesituuletin (liesi kaasulla) | 1,6 (aiemmin 3,1 sähköliedellä) |
| Ilmanvaihtokone, 24 h | 1,2 |
| Öljylämmityksen poltin, 6 h lämmityskaudella | 1,2 |
| Jääkaappi | 0,8 |
| Televisio ja laturit | 0,5 |
| **Yhteensä AC** | **≈ 9,9** (aiemmin 11,4) |
| **Akustosta** (invertterin hyötysuhde 90 %) | **≈ 11,0 kWh** (aiemmin 12,7) |
| Ilman kiuasta, akustosta | ≈ 5,9 kWh (aiemmin 7,5) |

**Summasta puuttuvat 24 V:n kuormat.** Jätteet polttava WC on hylätty [omistaja 2026-10-31]; sen
tilalle tulee septi-WC 24 V:n maseraattorilla ja septitankin hätätyhjennyspumppu, joiden kulutus on
hyvin pieni (noin 0,01 kWh/vrk, **⚠ arvio**). Polttava WC olisi vienyt arviolta 4–8 kWh/vrk.

- **24 V:n kuormat** (konehuoneen ja komentosillan laitteet, ks. [loads.yaml](../loads.yaml),
  `dc_loads`). Ne otetaan akustosta suoraan ilman invertteriä. Arvioiduilla tehoilla ne kuluttavat
  lämmityskaudella ankkurissa yhteensä **noin 2,3 kWh/vrk** (**⚠ arvio**; 2026-10-31 lisätty
  maseraattori-WC, kaasuhälytin ja kaasun magneettiventtiili, yhteensä noin 0,1 kWh). Suurin osa kuluu jatkuvasti
  käyviin laitteisiin: kiertovesipumppu (noin 0,7 kWh, jos se käy koko vuorokauden), Intel NUC
  (Frigate, noin 0,4 kWh), Raspberry Pi 5 (Signal K, noin 0,2 kWh) kolme valvontakameraa (noin 0,4 kWh) ja AIS (noin 0,1 kWh),
  sekä valaistukseen (ankkurivalo ja sisävalot, noin 0,3 kWh). VHF:n kuuntelu ankkurissa ja
  NMEA 2000 -laitteet puuttuvat (**⚠ ei tiedossa**). Se lisää akustotarvetta noin 110 Ah (litium,
  80 % käytettävissä) [laskelma]. Alla olevissa Ah-luvuissa sitä ei ole mukana.

| Akustotarve yhdelle ankkurivuorokaudelle, 24 V | Litium (LiFePO4), 80 % käytettävissä | Lyijy (AGM tai geeli), 50 % käytettävissä |
|---|---|---|
| Saunan kanssa | ≈ 540 Ah (≈ 13,8 kWh nimellistä; aiemmin 660 Ah) | ≈ 860 Ah (≈ 22 kWh nimellistä) |
| Ilman saunaa | ≈ 290 Ah (≈ 7,4 kWh nimellistä; aiemmin 390 Ah) | ≈ 460 Ah (≈ 11,8 kWh nimellistä) |

Suositukset ja Ah-luvut muualla tässä dokumentissa koskevat **litiumakustoa**. Lyijyakusto ei sovi
tähän käyttöön (**⚠ arviot**, tarkistetaan valittujen akkujen datalehdistä):

- **Lataus ajossa:** lyijyakku ottaa täyttä virtaa vastaan vain noin 80 %:n varaustilaan asti, ja
  loppu latautuu tuntien hitaalla vaiheella. Parin tunnin ajo ei siksi täytä lyijyakustoa. Jos
  akustoa käytetään vain 50–80 %:n välillä, käytettävissä on noin 30 %, ja saunavuorokausi
  vaatisi noin 1800 Ah.
- **Suuret virrat:** kiukaan noin 106 A ja invertterin noin 230 A pienentävät lyijyakun
  käytettävissä olevaa kapasiteettia (Peukertin ilmiö). Litiumilla vaikutus on vähäinen.
- **Paino:** 25 kWh lyijyä painaa arviolta 600–800 kg, ja 16 kWh litiumia noin 150–200 kg.

### 2.2 Huipputeho ja invertteri [laskelma]

**Päivitetty 2026-10-31:** liesi on kaasuliesi, joten suurin keittiön sähkökuorma on yhdistetty
mikro- ja sähköuuni (arviolta noin 2–3 kW yhdistelmätoiminnoissa, **⚠ tarkista** valitusta mallista)
[omistaja 2026-10-31]. Aiempi oletus "liesi ja uuni yhdessä enintään noin 3 kW" [omistaja 2026-10-28]
koski sähköliettä. Uuni, jääkaappi, ilmanvaihto, liesituuletin ja laturit tekevät yhteensä noin
2,3–3,3 kW (**⚠ arvio**), mikä mahtuu 3,5 kW:n invertteriin. Yli 3,5 kW mennään, jos samaan aikaan
on päällä toinen suuri laite: vedenkeitin (arvio 2 kW), kahvinkeitin (arvio 1 kW), kiuas (2,3 kW) tai
vedenlämmittimen vastus (3 kW). Siksi joko **käyttötapa** (ei saunaa ja uunia yhtä aikaa) tai
**kuormanhallinta**, joka pudottaa kiukaan ja vedenlämmittimen pois, kun keittiökuorma on suuri.
Kaasuliesi pienentää huippua, mutta ei poista tarvetta noin 3,5 kW:n invertterille, koska kiuas ja
uuni ovat edelleen sähköllä. Pienempi (noin 3 kVA) invertteri riittäisi, jos kiuasta ja uunia tai
vedenkeitintä ei koskaan käytetä yhtä aikaa.
Kuormanhallinnan voisi tehdä omilla ESP32-PDM-moduuleilla ([current-system.md](../current-system.md#4-valvonta-verkot-ja-tehonjako)).
3,5 kW:n invertteri ottaa 24 V:n akustosta täydellä teholla noin 160 A, mikä vaatii järeät kaapelit
ja sulakkeet.

#### Ehdokas: Mastervolt Mass Combi Ultra 24/3500-100 (230 V)

Omistajien harkitsema invertterilaturi [omistaja 2026-10-28]. Arvot ovat jälleenmyyjiltä, koska
valmistajan sivu ei avautunut (**⚠ tarkista** datalehdestä), ks.
[datasheets](../../datasheets/README.md#sähköjärjestelmä).

| Ominaisuus | Arvo | Mitä se tarkoittaa Vegalle [laskelma] |
|---|---|---|
| Invertteri | 3500 W jatkuva @ 40 °C, huippu 7000 W | Kiuas (2,3 kW), jääkaappi, ilmanvaihto, televisio ja laturit yhtä aikaa onnistuvat. Myös yhdistetty mikro- ja sähköuuni (arviolta 2–3 kW) pienkuormineen mahtuu. Ei riitä, jos uunin lisäksi päällä on vedenkeitin tai kiuas. |
| Akkuvirta | – | 3500 W:lla noin 160 A (hyötysuhde 92 %, **⚠ arvio**), huipussa yli 300 A. Akuston BMS:n, kaapeleiden ja sulakkeen pitää kestää se. |
| Laturi | 100 A @ 28,5 V (≈ 2,9 kW) | Maasähköstä tai generaattorista täysi ankkurivuorokausi (≈ 13,3 kWh 24 V:n kuormineen, päivitetty 2026-10-31) latautuu noin 4,5–5 tunnissa. Täysi lataus ottaa verkosta arviolta noin 3,1 kW eli noin 13,5 A (hyötysuhde noin 92 %, **⚠ arvio**), joten 15 A:n maasähköllä sille ja muille kuormille ei jää yhtä aikaa tilaa; Power Assist ja tulovirran raja hoitavat tämän. |
| Power Assist | on | Rajoittaa maasähkön tai generaattorin kuormaa ja täydentää akuilta. Mahdollistaa pienemmän generaattorin. **Kotilaiturin 15 A:lla tulovirran raja asetetaan noin 14 A:iin** [laskelma]; laturi hidastaa ensin, ja suuret kuormat (esim. kiuas ja vedenlämmitin yhtä aikaa, noin 23 A) saavat loput akustosta invertterin rajoissa. |
| Rinnankytkentä | enintään 10 kpl | Toisen yksikön voi lisätä myöhemmin (yhteensä 7000 W); kaasuliedellä (päätetty 2026-10-31) tarve on epätodennäköinen. |
| Hinta | 3 126 € ([SVB24](https://www.svb24.com/en/mastervolt-mass-combi-ultra-charger-inverter-24-v-3500-w-100-a.html)); 3 549 £ sis. ALV ([Chas the Boat, UK](https://shop.chastheboat.co.uk/products/mass-combi-ultra-inverter-charger-24-3500-100-38023500)) | Haettu 2026-10-28 |

**Arvio:** laite sopii Vegalle, kun kiuasta tai vedenkeitintä ei käytetä yhtä aikaa uunin kanssa
(liesi on kaasulla, päätetty 2026-10-31). Se on samaa sarjaa kuin Mastervolt Alpha -laturit, mutta yhteensopivuus
(MasterBus) **⚠ tarkista**.

#### Muut invertterilaturivaihtoehdot (haettu 2026-10-29)

Hinnat verkkokaupoista, sis. ALV; tekniset arvot jälleenmyyjien sivuilta (**⚠ tarkista**
valmistajan datalehdestä).

| Malli | Jatkuva teho | Huippu | Laturi | AC-tulo | Väylä | Hinta |
|---|---|---|---|---|---|---|
| Mastervolt Mass Combi Ultra 24/3500-100 | 3500 W @ 40 °C | 7000 W | 100 A + apulaturi 10 A | – | MasterBus | ≈ 3 126 € (SVB24; ALV **⚠ tarkista**) |
| Mastervolt Mass Combi Pro 24/3500-100 ([SVB24](https://www.svb24.com/en/mastervolt-mass-combi-pro-charger-inverter-24-v-3500-w-100-a.html), [Nautiradar, PT](https://www.nautiradar.pt/en/products/mastervolt/mass-combi-pro-24-3500-100-inverter-charger-combi)) | 3500 W @ 40 °C | **⚠ tarkista** | 100 A | – | MasterBus | ≈ 2 807 € (SVB24); 4 089 € sis. ALV (PT) |
| Mastervolt CombiMaster 24/3000-60 ([Comptoir Nautique](https://en.comptoirnautique.com/inverter-charger-combinations/37694-mastervolt-combimaster-24-3000-60-230-v-0816882021886.html), [SVB24](https://www.svb24.com/en/mastervolt-combimaster-inverter-charger-24-v-3000-va-60-a.html)) | 2600 W @ 40 °C | 3900 W / 30 s | 60 A | 25 A, tulovirta säädettävä ≤ 13 A, Power Assist | MasterBus | 1 328–1 600 € |
| Victron MultiPlus-II 24/3000/70-32 ([Europe Solar Store](https://www.europe-solarstore.com/victron-multiplus-ii-24-3000-70-32-230v-gx.html)) | 2400 W (3000 VA) | 5500 W | 70 A | 32 A, PowerAssist | VE.Bus (GX-laite) | ≈ 1 259 €; GX-versio ≈ 1 518 € |
| Victron MultiPlus-II 24/5000/120-50 (PMP242505010) ([etronixcenter](https://etronixcenter.com/en/8173170-sl105-victron-energy-victron-energy-multiplus-ii-24-5000-120-50-230v-pmp242505010-8719076052913.html), [pkys](https://shop.pkys.com/multiplus-ii-24vdc-230vac-5kva), [Solartopstore](https://www.solartopstore.com/products/victron-multiplus-ii-24-5000-120-50-230v), [solartech.eu](https://solartech.eu/en/p/inverter-24v-5000va-victron-energy-multiplus-ii-24-5000-120-50/), [Voelkner](https://www.voelkner.de/products/9515853/Victron-Energy-Wechselrichter-5000W-24V-230V-integrierter-Laderegler.html), [Herzmarine](https://herzmarine.com/?p=2453)) | 5000 VA (W-arvo **⚠ tarkista**) | **⚠ ei tiedossa** | 120 A | 50 A, PowerAssist | VE.Bus (GX-laite) | ≈ 1 700–2 400 € (1 401 € ilman ALV:tä etronixcenterissä). Hintavertailusivun 1 429 € ([solaranlage-tipps.de](https://www.solaranlage-tipps.de/wechselrichter/victron-multiplus-ii-24-5000-120-50-230v-5000w-wechselrichter-120a-ladegeraet-all-in-one), Offgridtec) ei vahvistunut kaupan sivulta. Suomalaista kauppaa ei löytynyt; EU-verkkokauppa perii kuluttajalta Suomen ALV:n 25,5 % |

**Mastervoltin edullisemmat mallit:** Mass Combi Pro on Mastervoltin mukaan Mass Combi Ultra ilman
aurinkopaneelituloa ja apulaturia ([Mastervolt](https://www.mastervolt.com/products/mass-combi-24v/));
teho ja laturi ovat samat, ja samassa kaupassa (SVB24) se on noin 320 € halvempi. Ultran 10 A:n
apulaturilla voisi pitää käynnistysakut ladattuina maasähköllä; Pron kanssa siihen tarvitaan muu
ratkaisu. Generaattorin hylkääminen ei vaikuta Ultran ja Pron väliseen valintaan. **Halvin sopiva
Mastervolt on CombiMaster 24/3000-60** (≈ 1 344–1 600 €), jos 2600 W riittää eli kiuasta ja uunia ei
käytetä ankkurissa yhtä aikaa (liesi on kaasulla 2026-10-31); sen säädettävä tulovirta (≤ 13 A) sopii kotilaiturin
15 A:n maasähköön.

**Muut valmistajat (haettu 2026-10-29; euromääräisiä hintoja ei löytynyt):**

| Malli | Teho | Laturi | Hinta | Huomio |
|---|---|---|---|---|
| Sterling ProCombi S 24 V / 3500 W ([Beacons and Lightbars, UK](https://www.beaconsandlightbars.co.uk/product/sterling-power-products-ltd-sterling-power-pcs243500-procombi-s-24v-3500w-sine-inverter-charger-pn-17869)) | 3500 W, siniaalto | **⚠ ei tiedossa** | 1 499 £ | 30 A:n läpikytkentärele, irrotettava ohjauspaneeli. BMS-/väyläliitäntää ei löytynyt |
| Sterling ProCombi Q ([Sterling](https://sterling-power.com/collections/inverters-and-combi-inverter-chargers/pro-combi-q)) | enintään 2500 W | – | – | **Ei suositella:** modifioitu (kvasi-)siniaalto ei sovi kaikille laitteille |
| WhisperPower WPC 24 V / 3500 VA – 90 A ([WhisperPower](https://www.whisperpower.com/wpc-24-v-3500-va-90-a)) | 3000 VA jatkuva, 3500 VA / 30 min | 90 A | noin 3 000 USD | 28 kg |
| WhisperPower WP Combi 24 V / 3000 W / 60 A ([JPC Direct, UK](https://www.whisperpowerspareparts.co.uk/product/wp-combi-24v-3000w-60a-230v-50hz-inverter-charger-61124360/)) | 3000 W | 60 A | 2 226 £; poistomyynnissä noin 1 500 USD | |
| WhisperPower Supreme Combi 24 V / 3000 W ([WhisperPower](https://www.whisperpower.com/supreme-combi-24-v-3000-w-50-a)) | 3000 W | 10–50 A | **⚠ ei tiedossa** | |
| Dolphin Charger | – | – | – | Valmistaa vain akkulatureita, ei invertterilatureita; sopisi vain erillisen invertterin pariksi |

**Arvio:** mikään näistä ei ole hinnaltaan ja teholtaan Victron MultiPlus-II 24/5000:aa edullisempi.
Sterling ProCombi S 3500 on lähin, mutta BMS-ohjaus ja väylä puuttuvat. Erillinen invertteri ja
akkulaturi (esim. Dolphin) on mahdollinen, mutta silloin menetetään PowerAssist ja automaattinen
maasähkön läpikytkentä.

**MultiPlus vai Quattro:** Quattro-II:ssa on **kaksi AC-tuloa** (esim. maasähkö ja generaattori),
ja laite valitsee automaattisesti käytössä olevan lähteen; MultiPlus-II:ssa on yksi. Muuten
samankokoiset mallit vastaavat toisiaan (Quattro-II 24/5000/120-50/50: laturi 120 A, kaksi 50 A:n
tuloa). Hinta samassa kaupassa: Quattro-II 2 339 € ja MultiPlus-II 2 085 €
([Voelkner, Quattro-II](https://www.voelkner.de/products/9518773/Victron-Energy-Wechselrichter-Quattro-II-24-5000-120-50-50-5000W-24V-230V-integrierter-Laderegler.html)),
muualla Quattro-II 2 289 € ([Solarkontor](https://solarkontor.de/en/products/victron-quattro-ii-24-5000-120-50-50-230v)).
**Vegalle riittää MultiPlus**, koska generaattoria ei ole; jos sellainen myöhemmin tulee, maasähkön
ja generaattorin väliin riittää erillinen vaihtokytkin.

**Vegan kuormia vasten** [laskelma]: kiuas (2,3 kW) toimii kaikilla. Liesi on kaasulla (päätetty 2026-10-31), joten keittiön
suurin sähkökuorma on yhdistetty mikro- ja sähköuuni (arviolta 2–3 kW); kiuas ja uuni yhtä aikaa
(≈ 4,5–5 kW) vaativat kaikilla kuormanhallintaa. Laiturissa PowerAssist / Power Assist täydentää 15 A:n maasähköä
kaikissa.

**Victron-vaihtoehdon erot:**
- **Signal K:** Victronin GX-laite (esim. Cerbo GX, hinta **⚠ ei tiedossa**) toimii Venus
  OS:llä, joka tukee Signal K:ta ja NMEA 2000:ta. Sopii omistajien olemassa olevaan
  Signal K -järjestelmään ([current-system.md](../current-system.md#4-valvonta-verkot-ja-tehonjako)).
- **BMS:** GX-laite voi ohjata Victronin latureita CAN-väylään kytketyn BMS:n mukaan (DVCC).
  Tuettujen BMS:ien lista **⚠ tarkista** ennen akuston valintaa.
- **Laturin säädin:** Alpha Pro III ei saa Victronin tapahtumia, joten BMS-ohjaus tehdään
  Reg on -johtimen kautta, tai säätimeksi valitaan CAN-väylään liittyvä Wakespeed WS500
  (650–820 USD, ks. kohta 2.5).

### 2.3 Lataus ajossa [laskelma]

Oletus: laturi antaa lämpimänä noin 75 % nimellisvirrastaan 28 V:n latausjännitteellä (**⚠ arvio**).

| Laturit | Latausteho (arvio) | Kiukaan energian (5,1 kWh) palautus |
|---|---|---|
| Nykyinen 65 A | ≈ 1,4 kW | ≈ 3,7 h ajoa |
| Nykyinen 65 A ja toinen 150 A | ≈ 4,5 kW | ≈ 1,1 h ajoa |
| Nykyinen 65 A ja toinen 200 A | ≈ 5,6 kW | ≈ 0,9 h ajoa |

Koko ankkurivuorokauden (≈ 12,7 kWh) palautus vie 65 A:n ja 200 A:n latureilla noin 2,3 h ajoa ja
65 A:n ja 150 A:n latureilla noin 2,8 h.

Litiumakusto vaatii latureille sopivan latauksensäädön (ulkoinen säädin tai DC-DC-laturi) ja
laturin lämpötilan valvonnan, koska litium ottaa virtaa vastaan täydellä teholla pitkään.

### 2.4 Litiumakuston hintataso (haettu 2026-10-28)

Verkkokauppojen hinnat; ne vaihtelevat, ja osa sivuista voi olla vanhentuneita. Hinnat ovat vain
akuista tai kennoista; mukana eivät ole BMS, kotelointi, sulakkeet, kaapelointi ja asennus.

| Taso | Esimerkki ja lähde | Hinta | ≈ €/kWh | 650 Ah (≈ 16,6 kWh) | 400 Ah (≈ 10 kWh) |
|---|---|---|---|---|---|
| Merkkiakku | Victron LiFePO4 25,6 V / 200 Ah Smart-a, 5,12 kWh, 56 kg, tarvitsee erillisen BMS:n ([Solarkontor, DE](https://solarkontor.de/en/products/victron-smart-a-lithium-ionen-200-ah-batterie-lifepo4-25-6v)) | 2 190 € sis. ALV (DE) | ≈ 430 | ≈ 7 000 € (3–4 akkua) | ≈ 4 400 € (2 akkua) |
| Edullinen valmisakku | LiTime, Power Queen, Vatrer 24 V / 200 Ah, sisäinen BMS ([LiTime](https://www.litime.com/products/24v-200ah-lifepo4-lithium-battery), [Power Queen](https://ipowerqueen.com/products/power-queen-24v-200ah-lifepo4-battery), [Vatrer](https://www.vatrerpower.com/products/vatrer-24v-200ah-trolling-motor-lifepo4-lithium-battery)) | 765–900 USD, USA, ilman ALV:tä ja rahtia | ≈ 150–175 USD | ≈ 2 500–2 900 USD + ALV ja rahti | ≈ 1 500–1 800 USD + ALV ja rahti |
| Omat kennot (8S) | EVE MB31 3,2 V / 314 Ah ([Akkula.fi](https://akkula.fi/tuote/eve-mb31-grade-a-lifepo4-314ah-32v-1kwh-prismaattinen-akkukenno-ruuviliitoksin/)) | 129,95 €/kenno | ≈ 130 | ≈ 2 100 € (16 kennoa, 628 Ah) | ≈ 1 050 € (8 kennoa, 314 Ah) |

Huomioita:

- **LiFePO4-akkua ei saa ladata pakkasella.** Jos akusto on veneessä talvella tai alkukeväällä
  kylmässä, tarvitaan lämmitys tai BMS, joka estää latauksen alle 0 °C:ssa.
- **Omista kennoista koottu akusto** on selvästi halvin, mutta BMS, kotelointi ja sulakkeet pitää
  mitoittaa ja rakentaa itse. Selvitä vakuutusyhtiöltä, hyväksyykö se itse kootun akuston.
- Edullisten valmisakkujen hinnat ovat USA:n verkkokaupoista; EU-hintaa ei tarkistettu.

### 2.5 Toisen laturin hintataso (haettu 2026-10-28)

24 V:n veneilylatureissa 200 A on harvinainen koko; tavallisia ovat 110–175 A. Verkkokauppojen
hinnat, jotka voivat olla vanhentuneita:

| Laturi | Lähde | Hinta | Huomio |
|---|---|---|---|
| Mastervolt Alpha 24/150 Evo ja Alpha Pro III -säädin (48624152) | [Nauticsale](https://www.nauticsale.com/en/mastervolt-alpha-alternator-24-150-iv-incl-alpha-p.html); [Alter Marine, EE](https://www.marine.ee/en/a/alpha-24-150-evo-kit-c-w-alpha-pro-iii) | **2 862 € sis. ALV**; 2 933 € (EE, ei varastossa) | säädin mukana. Aiempi 1 476 €:n hinta ([Blue Bottle Marine](https://www.bluebottlemarine.com/products/mastervolt-alpha-24-150-evo-kit-c-w-alpha-pro-iii.html)) oli luultavasti valuuttamuunnos Australian dollarin hinnasta 2 399 AUD, eikä se ole EU-hinta |
| Mastervolt Alpha 24/150 MB | [Philippi, DE](https://www.philippi-online.de/en/?p=34174) | 2 420 € sis. ALV | säädin **⚠ tarkista**, onko mukana |
| Alpha Pro III -säädin erikseen (45513000) | [Del City, US](https://delcity.net/store/Charge-Regulator/p_960412.h_960414) | noin 330–450 USD, ilman ALV:tä | akun lämpötila-anturi mukana |
| Laturin lämpötila-anturi 41500400 | [Zoro, US](https://zoro.com/mastervolt-alternator-temperature-sensor-41500400/i/G703077252) | noin 17–26 USD | lisävaruste |
| Prestolite 24 V / 175 A | [SEIMI, FR](https://www.seimi-equipements-marine.com/en/electricity/alternators-regulators/alternators/prestolite-alternator-24-175-a/pdt_2563) | 1 304 € sis. ALV | ulkoinen säädin erikseen |
| DelStar 24 V / 200 A | [Bermantec](https://bermantec.com/shop/products/alternators-spare-parts/marine-alternators/delstar-alternator-24v-for-mastervolt-pad-mount-1170-20201/) | hinta ei näkyvissä; toisella myyjällä noin 4 600 USD | ainoa löydetty 24 V / 200 A |
| Ulkoinen säädin: Wakespeed WS500 | [invertersrus](https://invertersrus.com/product-category/inverter-brands/wakespeed/) | 650–820 USD | litiumille sopiva |
| Ulkoinen säädin: Balmar MC-618 | [eMarine](https://emarineinc.com/balmar-mc-618-ms-12v.html) | 367 USD (12 V:n versio) | 24 V:n versio **⚠ tarkista** |

Lisäksi tarvitaan kiinnike ja hihna CAT 3126B:n etupäähän, kaapelit ja sulake (hinta
**⚠ ei tiedossa**). 150–175 A:n laturi ottaa koneelta arviolta 5–7 kW, joten **tarkista, kestääkö
hihnaveto sen** (usein tarvitaan leveä moniurahihna).

**Johtopäätös [laskelma]:** 150–175 A riittää. 200 A:n laturi lyhentäisi täyden ankkurivuorokauden
latausta vain noin 2,8 tunnista 2,3 tuntiin, mutta 24 V:n 200 A:n laturit maksavat moninkertaisesti.
Mastervoltin laturi ja säädin maksavat EU:ssa noin **2 900 €**. Prestolite 175 A ja erillinen säädin (Alpha Pro III tai Wakespeed) maksaisivat arviolta **1 700–2 100 €**. Hinnoissa ei ole kiinnikettä, hihnaa, kaapeleita eikä asennusta (**⚠ arvio**, haettu 2026-10-28).

#### Alpha 24/150 Evo, Alpha Pro III ja Mass Combi Ultra yhdessä (haettu 2026-10-28)

- **Yhteensopivuus:** Alpha Pro III -säädin ja Mass Combi Ultra ovat molemmat MasterBus-laitteita
  ([Alpha Pro III](https://www.mastervolt.com/products/alpha-pro-mb-charge-regulator1/alpha-pro-iii/),
  [Mass Combi Ultra](https://www.mastervolt.com/products/mass-combi-ultra/)), joten ne voivat olla
  samassa väylässä ja näkyä samassa näytössä. Sähköisesti ne eivät tarvitse yhteyttä: Combi lataa
  maasähköltä, laturi ajossa, samaan akustoon.
- **Säädin tarvitaan.** Litium ottaa täyttä virtaa vastaan pitkään, ja ilman ulkoista säädintä
  laturi ylikuumenee. Alpha Pro III: 12/24 V, kenttävirta 20 A, litiumprofiili säädettävin
  jännittein, akun lämpötila-anturi (6 m) ja laturin lämpötilan valvonta, MasterBus
  ([Mastervolt Polska](https://mastervoltpolska.pl/en/mastervolt-alpha-pro-iii-masterbus-12-24v-20a-field-current-id291.html)).
  Valitse versio **"including charge regulator"** ([Alpha 24/150 Evo](https://www.mastervolt.com/products/alternators-24v/alpha-24-150-evo-including-charge-regulator/)).
- **⚠ BMS:n katkaisu on laturille vaarallinen.** Jos litiumakuston BMS katkaisee latauksen laturin
  ladatessa, jännitepiikki voi rikkoa laturin ja elektroniikan. Säätimen pitää saada tieto BMS:ltä
  ja sammuttaa kenttävirta ensin. Alpha Pro III lukee Mastervoltin omaa MLI Ultra -akkua
  MasterBusin kautta; muun valmistajan akun tai omista kennoista kootun akuston kanssa tarvitaan
  BMS:n ohjauslähtö säätimen sallintatuloon (**⚠ tarkista** Alpha Pro III:n ohjeesta) tai
  CAN-yhteensopiva säädin (esim. Wakespeed WS500).
  **BMS-viestin vastaanotto** ([käyttöohje Alpha Pro III, 10000021727_03](https://www.emarinesolutions.com.au/assets/files/10000021727_01-manualAlphaPro-EN.pdf);
  omistajien toimittama PDF, versio _03, teksti poimittu PDF:stä): Alpha Evo -laturissa itsessään
  ei ole tuloa BMS:lle; ohjaus tapahtuu Alpha Pro III -säätimen kautta. Tapoja on kaksi:

  1. **MasterBus-tapahtuma "Stop charge"** (ohje 6.3.7): *"This event pauses the charging process
     and forces the field current to 0%. This event is used in combination with the stop charge
     event of Lithium-ion batteries. When charging can be resumed, the process continues from this
     point forward."* Tapahtuman voi lähettää mikä tahansa MasterBus-laite: Mastervoltin MLI Ultra
     -akku suoraan, tai muun valmistajan BMS:n relekosketin MasterBusin digitaalitulomoduulin
     kautta (**⚠ tarkista** sopiva Mastervoltin moduuli). Sama tapahtuma voidaan luultavasti
     ohjata myös Mass Combi Ultralle (**⚠ tarkista**), jolloin yksi BMS-signaali pysäyttää
     molemmat laturit. **Suositeltava tapa:** säädin pysyy päällä ja jatkaa latausta, kun BMS
     sallii.
  2. **Reg on -johdin** (ruskea, ohje 4.2.2): *"The 'reg on' wire should be interrupted with a relay
     or an ungrounded oil pressure switch."* Johdin menee 2 A:n sulakkeen kautta ladattavan akun
     plusnapaan ja on samalla säätimen jännitteenmittaus (ero akun napoihin enintään 0,01 V, ohje
     5.5.3). BMS:n "lataus sallittu" -relekoskettimen voi kytkeä sarjaan virtalukon tai
     öljynpainekytkimen kanssa. Tällöin säädin sammuu kokonaan. Koskettimen pitää olla laadukas,
     jotta mittaus ei vääristy.

  Kummassakin tavassa signaalin pitää tulla **ennen** kuin BMS irrottaa akuston (BMS:n
  ennakkovaroituslähtö tai viive katkaisuun).

  **Muuta käyttöohjeesta:**
  - Akkutyypit: Flooded, Gel, AGM, Lithium-ion ja User defined (valitaan MasterBusin kautta).
    Lithium-ion (MLI) -profiili 24 V:lla: bulk ja absorptio 28,5 V, kellunta 27,0 V, paluu
    bulkkiin 26,5 V [ohjeen 12 V:n arvot × 2]. Muun valmistajan LiFePO4:lle käytetään User defined
    -asetusta akun valmistajan arvoilla (säätöalue 16–32 V).
  - Säätimessä on yksi lämpötilatulo. Litium ei tarvitse akun lämpötilakompensointia, joten tulo
    voidaan käyttää **laturin lämpötila-anturille** (41500400, lisävaruste): ensimmäisessä rajassa
    teho pienenee, toisessa lataus loppuu (ohje 5.4). Ohjeen mukaan anturi ei kuitenkaan
    täysin suojaa laturia, koska se mittaa koteloa eikä käämejä.
  - **Power curve** (ohje 5.3) rajoittaa kenttävirran 20 %:iin alle valitun laturin kierrosluvun,
    mikä estää hihnan luistamista tyhjäkäynnillä (700 rpm).
  - Säädin on N-tyypin (negatiivinen kenttäohjaus) latureille, ja se tarvitsee kaksi
    MasterBus-päätevastusta väylän päihin.

  **Sterling Alternator Protection Device (APD24)**
  ([sterling-power.com](https://sterling-power.com/products/alternator-open-circuit-protection-device);
  haettu 2026-10-28): rinnankytkettävä suojalaite, joka leikkaa laturin jännitepiikin, kun kuorma
  katoaa äkillisesti. Ei kulje päävirtaa, joten ohut johdotus riittää; 90 × 90 × 60 mm, 0,25 kg.
  Leikkausjännitettä ja energiankestoa ei löytynyt (**⚠ ei tiedossa**). **Arvio:** halpa
  lisäsuoja laturille, mutta ei korvaa BMS:n ohjausta säätimelle: se ei estä tilannetta, jossa
  laturi jatkaa lataamista ilman akkua ja DC-kuormat jäävät laturin varaan, eikä se kerro
  säätimelle, miksi BMS katkaisi. **Suositus: molemmat** – BMS:n ohjaus säätimelle ensisijaisena
  ja APD24 varasuojana. Älä sekoita samannimiseen Sterling Pro Protect A -tuotteeseen, joka
  kytketään laturin ja akun väliin.
- **Nykyinen 65 A:n laturi** kannattaa jättää lataamaan käynnistysakkuja; uusi laturi lataa
  käyttöakustoa.
- **Signal K:** MasterBusista NMEA 2000:aan tarvitaan liitäntälaite (**⚠ tarkista** saatavuus).

### 2.6 Olemassa oleva erotusmuuntaja: Airlink WM5002

Vegalla on erotusmuuntaja, jota ei ole vielä kytketty [omistaja 2026-10-28]. Arvot on luettu
valmistajan datalehden ([datalehti Airlink WM5002](https://airlinktransformers.com/product/datasheet-pdf/enclosed-isolating-transformer-wm5002))
sivun kuvasta, ks. [datasheets](../../datasheets/README.md#sähköjärjestelmä).

| Ominaisuus | Arvo |
|---|---|
| Tyyppikilpi | **WM5002 MCB**, Safety Isolating Transformer, 5000 VA, EN 61558-2-23, Made in UK ([omistajan kuva 2026-10-28](../img/isolation-transformer-wm5002-plate.jpg)) |
| Ensiön johtimet | 0–230 V: sininen (0) – ruskea (230 V) [tyyppikilpi] |
| Toision johtimet | 115–0–115 V: **musta – vihreä (keskipiste) – punainen** [tyyppikilpi] |
| Kuvaus | "5000VA 230v to 230v CTE Hardwired" [datalehti] |
| Teho | 5000 VA |
| Ensiö | 230 V, 22 A, ruuviliittimet (PA220, 3-napainen) |
| Toisio | 230 V, **CTE** (keskipiste maadoitettu), ruuviliittimet |
| Ensiön suojaus | Painettava johdonsuoja SP30 |
| Kytkentävirran rajoitus | **SL35 30 A surge limiter** (pehmokäynnistys) |
| Kotelo | P6, teollisuus, lattia- tai seinäasennus, **IP23** |
| Mitat, paino | 454 × 384 × 305 mm (k × p × l), 25 kg |
| Jännitteensäätö | 0,02 (≈ 2 %) |
| Standardi | Turvaerotusmuuntaja EN 61558-2-23 (tuotetyyppi) ja EN 61558-2-6 (vaatimustenmukaisuusvakuutus); eristysluokka A, 105 °C |

**Käyttö Vegalla:** muuntaja kytketään maasähkön tuloliittimen ja Mass Combin AC-tulon väliin.
Se erottaa veneen sähköverkon maasähköverkosta. **Teräsrunkoisessa veneessä tämä on tärkeää:**
ilman erotusta laiturin suojamaa yhdistää rungon muihin veneisiin ja laiturin rakenteisiin, ja
rungon ja niiden välillä voi kulkea galvaanista ja vuotovirtaa, joka syövyttää runkoa ja anodeja.
Erotusmuuntaja on tähän paras ratkaisu (galvaaninen erotin on halvempi mutta heikompi).

- **Teho riittää:** 5000 VA on enemmän kuin kotilaiturin 15 A:n maasähkö (≈ 3,45 kVA) [laskelma].
  Mass Combin Power Assist rajoittaa maasähkövirran asetettuun arvoon.
- **Kytkentävirta on rajoitettu** (SL35-pehmokäynnistin), joten laiturin johdonsuojan ei pitäisi
  laueta muuntajaa kytkettäessä.
- **Kotelo IP23** suojaa vain tippuvalta vedeltä. Asenna kuivaan paikkaan, ei pilssin tai
  merivesiputkien lähelle. 25 kg vaatii tukevan kiinnityksen, joka kestää aallokon.
- **⚠ CTE-toisio on ongelma veneessä.** CTE tarkoittaa, että toision keskipiste on maadoitettu:
  kummankin lähtöjohtimen jännite maahan on 115 V, eikä kumpikaan ole nolla. Muuntaja on tehty
  työmaakäyttöön. Veneen 230 V:n verkko olettaa yhden johtimen olevan nolla (sininen) ja vaihe-
  ja nollajohtimen olevan erotettu toisistaan; yksinapaiset johdonsuojat ja kytkimet jättäisivät
  CTE-verkossa toisen johtimen jännitteiseksi (115 V maahan). Mass Combin siirtorele ja
  vikavirtasuojat on myös suunniteltu nolla–vaihe-verkkoon (**⚠ tarkista** Mastervoltilta).
  **Airlinkin vastaus** [omistaja 2026-10-28, Airlinkin sähköposti]: *"The 'CTE' indicates that
  it has a centre-tapped output which is connected to ground, hence the label reads 115-0-115V. If
  you only require an untapped 230V output, you just disconnect the 0V (Green) output terminal from
  its link to the ground connection."* Eli kun toision keskipisteen (0 V, vihreä liitin) ja maan
  välinen silta irrotetaan, lähtö on maasta erotettu 230 V. **CTE ei siis estä muuntajan käyttöä.**

  **Pelkkä sillan irrotus jättää lähdön kellumaan** (kumpikaan johdin ei ole maadoitettu). Silloin
  ensimmäinen eristysvika ei laukaise vikavirtasuojaa, vaan jää huomaamatta. Veneen verkossa
  (ISO 13297 -tyyppinen ratkaisu) toision **toinen pää kytketään suojamaahan**, jolloin siitä tulee
  nolla [laskelma/yleinen käytäntö, **⚠ tarkista** sähköasentajalta]. **Kysy Airlinkiltä vielä,**
  saako toision pään maadoittaa (pitäisi onnistua turvaerotusmuuntajassa, mutta vahvista).

  **Kytkentäehdotus tyyppikilven mukaan** (ei vielä hyväksytty; sähköasentaja tarkistaa):
  vihreän keskipisteliittimen maasilta irrotetaan, ja vihreä jää kytkemättä; musta = nolla (N),
  joka sillataan veneen suojamaahan; punainen = vaihe (L) → Mass Combin AC-tulo. Kumpi pää
  valitaan nollaksi, on sähköisesti yhdentekevää, kunhan valinta merkitään.

  **Kytkennän haitat ja huomioitavat** (yleinen tieto ja arviot, **⚠ tarkista** sähköasentajalta):

  1. **Laiturin vikavirtasuoja ei suojaa veneen verkkoa.** Se näkee vain maasähkökaapelin ja
     muuntajan ensiön. Toisiopuolelle tarvitaan oma vikavirtasuoja (30 mA) ja johdonsuoja
     heti muuntajan jälkeen.
  2. **Muuntajan kotelo on eristettävä rungosta.** Kotelo ja ensiön suojamaa kytketään laiturin
     suojamaahan. Jos teräskotelo on kiinni teräsrungossa, laiturin suojamaa yhdistyy runkoon ja
     erotus menetetään. Tarvitaan eristetyt kiinnikkeet. Onko käämien välissä maadoitettava
     suojavaippa, **⚠ ei tiedossa**.
  3. **Tyhjäkäyntihäviö.** Muuntaja ottaa virtaa ja lämpenee myös ilman kuormaa, arviolta
     50–100 W (noin 1–2 % 5 kVA:sta, **⚠ arvio**), eli noin 1–2 kWh vuorokaudessa, kun se on
     kytkettynä maasähköön. Lämpö jää asennustilaan.
  4. **Jännite laskee hieman kuormitettuna** (säätö 2 % datalehden mukaan). Mass Combin tulo
     sallii 184–275 V, joten tämä ei haittaa.
  5. **Nollan ja suojamaan silta saa olla vain yhdessä paikassa kerrallaan.** Maasähköllä silta
     on muuntajan toisiolla. Mass Combi tekee invertterikäytössä oman siltansa sisäisellä
     releellä (**⚠ tarkista** Mastervoltin ohjeesta), eikä toinen kiinteä silta saa jäädä
     rinnalle. Myöhemmin asennettava generaattori ei kulje muuntajan kautta, joten sen syötön
     silta suunnitellaan erikseen.
  6. **Kokoa ja painoa:** 25 kg ja 454 × 384 × 305 mm, IP23 eli kuiva paikka.

  **Sijoitus:** luultavasti konehuoneeseen, tarkka paikka vielä auki [omistaja 2026-10-28].
  Konehuoneessa huomioitavaa (**⚠ arvio**, tarkistetaan paikan päällä):
  - **Lämpö:** konehuone on ajossa kuuma. Datalehti ei kerro, missä ympäristön lämpötilassa
    5000 VA on mitoitettu (eristysluokka A, 105 °C), joten kuumassa tilassa jatkuvaa
    kuormitettavuutta voi joutua pienentämään. Maasähköllä kone ei yleensä käy, mikä helpottaa.
    Valitse viileä paikka, jossa ilma kiertää kotelon ympäri.
  - **Vesi ja kosteus:** IP23 ei kestä roiskeita. Pidä kaukana pilssistä, merivesipumpusta,
    -putkista ja -letkuista sekä akselitiivisteestä, ja mieluiten koneen yläpuolisella tasolla.
  - **Kiinnitys:** 25 kg eristetyillä kiinnikkeillä rungosta (ks. kohta 2), ja kiinnityksen
    pitää kestää aallokko ja tärinä.
  - **Lyhyet kaapelit:** mahdollisimman lähelle maasähkön tuloliitintä ja Mass Combia.
  - **Huoltoon pääsy:** ensiön johdonsuojan pitää olla kuitattavissa.

  **Hyödyt samasta kytkennästä:** ei galvaanista yhteyttä laiturin maahan (runko ja anodit
  säästyvät), laiturin väärä napaisuus ei haittaa, ja maasähkön vikavirrat eivät kulje rungon
  kautta. Kelluvaan lähtöön verrattuna ensimmäinen eristysvika laukaisee vikavirtasuojan heti
  eikä jää piileväksi.
- **Maadoitus (ISO 13297 -tyyppinen ratkaisu):** toision nolla kytketään veneen suojamaahan ja
  runkoon, toisiolle tulee oma vikavirtasuoja, eikä laiturin suojamaata kytketä runkoon.

⚠ **Turvallisuus:** 230 V:n maasähkö ja muuntaja voivat aiheuttaa hengenvaarallisen sähköiskun.
Kytkennän ja maadoituksen saa tehdä ja tarkastaa vain pätevä sähköasentaja ennen käyttöönottoa.

## 3. Vaihtoehdot

| | A. Laturi, akusto ja invertteri | B. Dieselgeneraattori | C. Hydrauligeneraattori |
|---|---|---|---|
| Sähköä ajossa | ✅ | ✅ | ✅ |
| Kiuas ankkurissa | ✅ yksi ankkurivuorokausi latausta kohden, jos akusto on noin 660 Ah | ✅ rajoittamatta | ❌ vaatii pääkoneen käymään |
| Monta päivää ankkurissa ilman ajoa | ❌ akusto loppuu | ✅ | ❌ |
| Käyttää olemassa olevia osia | osittain: 24 V:n järjestelmä | ❌ | ✅ PVH57 (P2) |
| Asennus | laturin kiinnike, kaapelit, akusto, invertteri | polttoaine-, pakokaasu- ja merivesiputket, ilmanvaihto, äänieristys | letkut, venttiili, generaattori |
| Melu ankkurissa | ei | kyllä | pääkone käy |
| Huolto | vähäinen | oma kone huollettavaksi | vähäinen |
| Hinta | akusto ks. 2.4, laturi ks. 2.5, invertterilaturi ks. 2.2 | **⚠ ei tiedossa**, todennäköisesti kallein | **⚠ ei tiedossa** |

### C. Hydrauligeneraattori

Säätötilavuuspumppu PVH57 sopisi vakiovirtaukseen
([p2-variable-pump.md](../../hydraulics/design/p2-variable-pump.md)), mutta vaihtoehto ei sovi
Vegan tarpeeseen:

- **Ei sähköä ankkurissa ilman pääkonetta.** 350 hv:n CAT 3126B:n käyttäminen tyhjäkäynnillä
  kiukaan takia kuluttaa polttoainetta ja kuluttaa konetta pitkässä kevyessä käytössä
  (nokeentuminen, "wet stacking") (**⚠ arvio**, kulutusta ei ole mitattu).
- **Kilpailee keulapotkurin kanssa** samasta P2-virtauksesta.
- **Lisää lämpöä hydrauliöljyyn:** kokonaishyötysuhteella noin 70–75 % (**⚠ arvio**) 3 kW:n
  sähkötehosta noin 1 kW menee öljyyn, ja 10 kVA:sta noin 3–4 kW. Se pitää ottaa mukaan
  öljynjäähdytykseen ([oil-cooling.md](../../hydraulics/design/oil-cooling.md)).

### B. Dieselgeneraattori

Ainoa vaihtoehto, joka antaa sähköä rajoittamatta useana päivänä ilman ajoa. Kun generaattorin
rinnalla on akusto ja invertteri, generaattoria ei tarvitse ajaa jatkuvasti: se käy esim. saunan ja
ruoanlaiton ajan ja lataa samalla akustoa, ja yöt mennään akuilla. Silloin noin 6 kVA:n kone riittää
(**⚠ arvio**, tarkistetaan, kun tyyppikilpien tehot tiedetään). Tila on valmiina, mutta
asennus vaatii oman polttoaine-, pakokaasu- ja merivesijärjestelmän.

#### Pieni noin 3 kW:n varageneraattori (selvitys 2026-10-29)

Omistajien kysymys: riittäisikö varalle pieni noin 3 kW:n dieselgeneraattori, kun ankkurissa ollaan
enintään vuorokausi [omistaja 2026-10-29].

| Malli | Teho | Hinta | Lähde |
|---|---|---|---|
| Fischer Panda 4000s Neo PMS | 3,0 kW jatkuva, 3,4 kW enintään, 230 V | 6 815 € + ALV (8 314 € sis. ALV, ES) | [Manel Service](https://www.manelservice.com/en/marine-generator-sets/9781-fischer-panda-4000s-neo-pms-sea-generating-set-4-kva-36-kw.html) |
| WhisperPower Piccolo 4 / 3,5 kVA | noin 3–3,5 kW, 230 V | **⚠ ei tiedossa** (tarjouspyyntö) | [WhisperPower 3,5 kVA](https://www.whisperpower.com/diesel-generators/3-5-kva-generator) |

**Toimiiko 3 kW** [laskelma, **⚠ arviot**]:
- **Kiuas (2,3 kW) toimii suoraan generaattorilta.** Uuni ja kiuas yhtä aikaa eivät, mutta
  invertterilaturin PowerAssist täydentää akuilta.
- **Lataus:** invertterilaturin tulovirta rajoitetaan noin 11–12 A:iin, jolloin laturiin menee
  noin 2,5 kW ja täysi ankkurivuorokausi (≈ 12,3 kWh 24 V:n kuormineen, päivitetty 2026-10-31) latautuu noin 5 tunnissa.
- **Polttoaine:** sama diesel kuin pääkoneella, eli bensiiniä ei tarvitse säilyttää veneessä.
- **Asennus:** oma polttoaineen otto, märkäpakoputki, merivesiotto, äänieristys ja nollan ja
  suojamaan silta generaattorin syötölle (ei erotusmuuntajan kautta).

**Arvio:** kiinteä merigeneraattori maksaa jo ilman asennusta noin 8 300 € (Fischer Panda 4000s Neo), asennettuna selvästi enemmän (ks. kohta 4.2), mikä on
paljon varajärjestelmälle, jota tarvitaan vain, kun ankkuripäivän jälkeen ei ole maasähköä eikä
ajoa. Kannattaa ensin katsoa, kuinka usein tyhjäkäyntilatausta todella tarvitaan. Jos harvoin,
pääkone riittää varalle. Kannettava diesel- tai bensiinigeneraattori olisi halvempi, mutta
kannella käytettynä melu, häkä ja polttoaineen säilytys pitää ratkaista erikseen (**⚠ ei
selvitetty**).

### D. Kannettava bensiiniaggregaatti varalataukseen (selvitetty 2026-10-31)

Kysymys [omistaja 2026-10-31]: edullinen kannettava bensiinikäyttöinen invertteriaggregaatti, jolla
akustoa voi tarvittaessa ladata ankkurissa. **Päätetty 2026-10-31: hankitaan Timco SS2200i Supersilent
varalataukseen** [omistaja 2026-10-31, [decisions.md](../../decisions.md)]. Ehdot ja tarkistettavat asiat alla.

| Malli | Teho | Hinta (haettu 2026-10-31) |
|---|---|---|
| Stanley SIG 2000-1 | 1,8 kW jatkuva, 2,0 kW huippu, tankki 10 l | 369 € ([Motonet](https://www.motonet.fi/fi/tuote/7013840/STANLEY-SIG-2000-1-aggregaatti-invertteri-4-tahti-2000-W--2-x-230-V)) |
| Ducar D2500iS | 2,0 kW jatkuva, 2,2 kW huippu | noin 470 € ([Taloon](https://www.taloon.com/aggregaatti-ducar-d2500is-invertteri-malli-2200-2000-w-98cc-4-tahti-2xusb)) |
| Timco 2000i | 1,6 kW jatkuva, 2,2 kW huippu | noin 360–420 € ([Netrauta](https://www.netrauta.fi/aggregaatti-timco-2000i-inventteri-digitaalinen-sis-usb-liitanta), [Taloon](https://www.taloon.com/aggregaatti-timco-2000i-inventteri-digitaalinen-sis-usb-liitanta)) |
| Timco SS2200i Supersilent | 1,8 kW jatkuva, 2,2 kW huippu; 52–63 dB(A) 7 m:ssä; tankki 3,5 l, noin 4 h 75 %:n kuormalla (≈ 0,9 l/h [laskelma]) | 549 € ([Netrauta](https://www.netrauta.fi/aggregaatti-timco-ss2200i-supersilent), [Taloon](https://www.taloon.com/aggregaatti-timco-ss2200i-supersilent)) |
| Timco IG3600i | 3,6 kW (jatkuvaa tehoa ei ilmoitettu **⚠ tarkista**); tankki 7 l, noin 4,5 h täydellä kuormalla (≈ 1,6 l/h); noin 22 kg | 749 € ([Netrauta](https://www.netrauta.fi/aggregaatti-timco-ig3600i-3-600-w-digitaalinen)) |
| Timco IR3000SPG | 3 kW jatkuva, sähköstartti | noin 990 € ([Netrauta](https://www.netrauta.fi/sahkokaynnisteinen-aggregaatti-timco-ir3000spg-digitaalinen)) |
| Honda EU22i | 1,8 kW jatkuva, 2,2 kW huippu; kulutus noin 1,1–1,2 l/h täydellä teholla; noin 53 dB(A) 7 m:ssä neljäsosateholla | noin 1 500–1 690 € ([Taloon](https://www.taloon.com/invertterigeneraattori-honda-eu22i), [Hintaopas](https://hintaopas.fi/s/230v-generaattori/)) |

Honda-arvot ovat jälleenmyyjiltä ([Counties Honda](https://www.countieshonda.co.nz/eu22i), [Rosebud Mowers](https://www.rosebudmowers.com.au/products/honda-eu22-2200w-4-stroke-generator)), **⚠ tarkista** käyttöohjeesta.

Timcon arvot ovat jälleenmyyjien sivuilta (haettu 2026-10-31), ei valmistajan datalehdestä. **Noin 3 kW:n
malli** kattaisi kiukaan kokonaan ilman akustoa, mutta painaa enemmän ja maksaa noin kaksinkertaisesti.
Timco 2000i:llä (1,6 kW) lataus on noin 1,3 kWh tunnissa, ja neljän tunnin sauna veisi akustosta noin
4 kWh [laskelma].

**Mitä noin 1,8 kW:n aggregaatti antaa** [laskelma, **⚠ arviot**]:

- **Lataus:** invertterilaturin tulovirran raja asetetaan aggregaatin tehon alle (noin 7 A eli
  noin 1,6 kW). Akustoon menee noin 1,5 kWh tunnissa (laturin hyötysuhde noin 92 %). Esimerkiksi
  5 kWh:n vaje latautuu noin 3,5 tunnissa ja vie bensiiniä noin 4 l.
- **Sauna aggregaatin käydessä:** Power Assist / PowerAssist ottaa aggregaatilta noin 1,6 kW ja
  akustolta loput kiukaan 2,3 kW:sta, eli akustosta noin 0,8 kW (invertterin hyötysuhde 90 %).
  **Neljän tunnin sauna veisi akustosta vain noin 3 kWh** (ilman aggregaattia yläraja 10,2 kWh), ja
  koko saunapäivä noin 11,5 kWh eli noin 70 % 16 kWh:n akustosta. Aggregaatti korvaisi siis
  kolmannen akun pitkää saunaa varten ([house-battery.md](house-battery.md#herkkyys-sauna-4-h-ankkurissa-laskelma-2026-10-31)).
- **Kytkentä:** maasähköpistokkeeseen kuten laituri: pistoke → erotusmuuntaja WM5002 →
  invertterilaturi. Moni invertteriaggregaatti on "kelluva" (nolla ei ole maadoitettu);
  erotusmuuntajan takana veneen oma maadoitus ei riipu siitä, mutta yhteensopivuus valitun
  invertterilaturin kanssa **⚠ tarkista**. Tulovirran raja on voitava asettaa noin 7 A:iin
  (**⚠ tarkista** valitusta laitteesta).

**Turvallisuus:**

- **Häkä (CO):** aggregaatti käytetään vain avokannella, pakokaasu poispäin luukuista, ikkunoista ja
  tuuletusaukoista. Ei koskaan sisätiloissa, konehuoneessa tai suljetussa avotilassa. Makuutiloihin
  häkävaroitin; se on suositeltava joka tapauksessa öljylämmittimen ja kaasulieden takia.
- **Bensiinin säilytys:** bensiinihöyry on ilmaa raskaampaa ja kerääntyy pilssiin; teräsrunko ei
  päästä sitä ulos. Bensiini ja aggregaatti säilytetään vain kannella tai kannen kaapissa, joka
  tuulettuu ja valuu ulos laidan yli, ei koskaan sisätiloissa. Muuten veneen sähkölaitteet
  (talojohdonsuojat, releet) eivät ole syttymissuojattuja (ISO 8846), ja tämä pitäisi arvioida
  uudelleen.
- **Tankkaus** vain kylmään koneeseen ja kannella. Vakuutusyhtiön kanta bensiinin säilytykseen
  **⚠ tarkista**.

**Verrattuna muihin:** halvin malli (noin 370 €) on halvempi kuin kolmas akku (kennot noin 1 040 € ja
BMS) ja paljon halvempi kuin dieselgeneraattori (noin 8 300 € ja asennus). Pääkoneen tyhjäkäynti
on ilmainen, mutta 350 hv:n kone tyhjäkäynnillä on äänekkäämpi ja nokeentuu pitkässä
tyhjäkäynnissä. Aggregaatin haittoja ovat bensiinin säilytys, melu ankkurissa ja pienen koneen
huolto (bensiini vanhenee seistessään).

## 4. Suositus (ei päätös)

Akusto ja invertteri tarvitaan joka tapauksessa, koska jääkaappi käy ankkurissa myös yöllä, eikä
generaattoria haluta ajaa yöllä. **Akuston ja invertterin koko ratkeaa vasta, kun päätetään, mitkä
laitteet asennetaan ja ovatko ne sähköllä toimivia.** Alla olevat koot koskevat tilannetta, jossa
kaikki harkinnassa olevat laitteet asennetaan sähköisinä. **Koska ankkurissa ollaan enintään alle
vuorokausi ajamatta** [omistaja 2026-10-29], ajo ja maasähkö riittävät lataukseen, eikä
dieselgeneraattoria tarvita.

1. **Vaihe 1: vaihtoehto A.** Toinen 24 V:n laturi (150–175 A, ks. kohta 2.5) pääkoneeseen, noin 3,5 kW:n invertteri
   (ks. kohta 2.2), ja litiumakusto, joka **kestää yhden ankkurivuorokauden saunoineen**
   [laskelma, 24 V, 80 % käytettävissä, invertteri 90 %]:
   - päätetyt laitteet (kaasuliesi, yhdistetty mikro- ja sähköuuni, septi-WC; 2026-10-31), muut
     harkitut laitteet sähköisinä ja 24 V:n kuormat (noin 2,3 kWh/vrk) mukaan lukien: akustosta
     noin 12,3–13,3 kWh saunapäivänä. **Noin 16 kWh eli noin 630 Ah @ 25,6 V** riittää, ja
     saunapäivänä käytetään noin 76–83 % (aiemmin 85–93 % sähköliedellä).
     80 %:n käytöllä tarve olisi noin 15,4–16,6 kWh, eli 16 kWh on sopiva koko eikä sitä kannata
     pienentää (päivitetty 2026-10-31).

   Mitoitus ja itse kootut kennovaihtoehdot: [house-battery.md](house-battery.md).

   Ajo lataa täyden vuorokauden kulutuksen noin 2–2,5 tunnissa. Iso akusto parantaa samalla ohjauksen
   2,5 kW:n sähköisen varapumpun käyttöaikaa ([current-system.md](../current-system.md#3-suuret-dc-kuormat)).
2. **Dieselgeneraattoria ei suositella,** koska ankkurissa ollaan enintään alle vuorokausi ajamatta
   [omistaja 2026-10-29]. **Päätös on omistajien mukaan vielä auki** [omistaja 2026-10-29], joten
   paapuurin tila pidetään varattuna.

   **Varalataus pääkoneella tyhjäkäynnillä** [omistaja 2026-10-29]: jos ankkuripäivän jälkeen ei
   ole maasähköä eikä ajoa riittävästi, akusto ladataan käyttämällä konetta tyhjäkäynnillä
   riittävän pitkään. Huomioitavaa (**⚠ arviot**, tarkistetaan):
   - **Laturin tuotto tyhjäkäynnillä on rajallinen.** Laturin kierrokset = koneen kierrokset ×
     hihnapyörien välityssuhde (**⚠ ei tiedossa**). Esim. välityksellä 2,5 laturi pyörii 700 rpm:llä
     noin 1 750 rpm, jolloin 150 A:n laturi antaa tyypillisesti vain osan nimellisvirrastaan.
     Tarkista valitun laturin virtakäyrä datalehdestä. Alpha Pro III:n Power curve -asetus (20 %
     kenttävirtaa alle asetetun kierrosluvun) pitää asettaa niin, ettei se turhaan rajoita
     latausta tyhjäkäynnillä.
   - **Nosta kierroksia** esimerkiksi 1 000–1 200 rpm:iin, jos mahdollista: laturin tuotto kasvaa,
     ja lataus lyhenee.
   - **Kevyt kuorma koneelle:** 5–7 kW laturikuorma on 350 hv:n koneelle hyvin kevyt. Satunnainen
     tyhjäkäyntilataus on hyväksyttävä, mutta toistuva pitkä tyhjäkäynti voi nokeennuttaa konetta.
   - **Laturin lämpö:** matalilla kierroksilla laturin oma tuuletin jäähdyttää heikommin, joten
     laturin lämpötila-anturi (41500400) on suositeltava.
   - **Polttoaineenkulutus tyhjäkäynnillä:** **⚠ ei tiedossa**; voidaan lukea myöhemmin koneen
     tiedoista Signal K:sta.
3. **Hydrauligeneraattoria ei suositella** Vegan tarpeeseen.
4. **Vedenlämmittimen 3 kW:n vastusta ei kannata käyttää akustolta.** Yksi tunti vie noin 3,3 kWh
   akustosta. Käytä sitä maasähköllä tai generaattorilla. Jos lämmittimessä on koneen
   jäähdytysvesikierukka, vesi lämpenee ajossa ilmaiseksi.

**Halvempia vaihtoehtoja:** kaasuliesi on päätetty (2026-10-31), ja se pienensi kulutusta noin
1,5 kWh/vrk. Suurin kuorma on nyt kiuas (4,6 kWh/vrk), joka on päätetty (puukiuas ei mahdu). Lisäsäästöä
saa enää ilmanvaihtokoneen ja polttimen valinnasta (yhteensä noin 2,4 kWh/vrk).

### 4.1 Halvin toimiva kokoonpano [laskelma, hinnat haettu 2026-10-28]

Ehdotus, ei päätös. Hinnat kohdista 2.2, 2.4 ja 2.5; sis. ALV, ellei toisin mainita.

| Osa | Halvin toimiva | Hinta | Mastervolt-kokonaisuus | Hinta |
|---|---|---|---|---|
| Erotusmuuntaja | Olemassa oleva WM5002 | 0 € (+ vikavirtasuoja, kiinnikkeet) | sama | 0 € |
| Akusto | 16 × EVE MB31 314 Ah, 8S2P (≈ 16 kWh), ks. [house-battery.md](house-battery.md); 8 × EVE MB56 628 Ah olisi ≈ 950–1 200 €, jos saatavilla | ≈ 2 080 € | 2 × Victron 25,6 V / 200 Ah (≈ 10 kWh) | ≈ 4 380 € |
| BMS, kotelo, sulakkeet | Oma kokoonpano; BMS:ssä latauksenesto ennen katkaisua | **⚠ ei tiedossa** | Victronin erillinen BMS | **⚠ ei tiedossa** |
| Toinen laturi ja säädin | Prestolite 24 V / 175 A ja Alpha Pro III | ≈ 1 304 € + 330–450 USD | Alpha 24/150 Evo ja Alpha Pro III | ≈ 2 862 € |
| Invertterilaturi | Mass Combi Ultra 24/3500-100 | ≈ 3 126 € | sama | ≈ 3 126 € |
| Laturin varasuoja | Sterling APD24 | **⚠ ei tiedossa** | sama | **⚠ ei tiedossa** |
| **Tiedossa olevat yhteensä** | | **≈ 6 900 €** (MB56:lla ≈ 6 000 €) | | **≈ 10 400 €** |
| **Ilman invertterilaturia** (generaattorivertailuun) | | **≈ 3 700 €** (MB56:lla ≈ 2 600–2 900 €) | | **≈ 7 200 €** |

**Vertailu generaattoriin** [laskelma]: myös generaattorivaihtoehto tarvitsee akuston ja
invertterilaturin, koska jääkaappi käy yöllä akuilta ja generaattori lataa akustoa invertterilaturin
kautta (ks. kohta B). Vaihtoehtojen todellinen hintaero on siksi **toinen laturi ja säädin
(≈ 1 600 €) vastaan generaattori (Fischer Panda 4000s Neo ≈ 8 300 € sis. ALV) ja sen asennus**.
Generaattorin kanssa akusto voisi olla jonkin verran pienempi, jos generaattori ajetaan saunan
ajan, mutta yön kulutus ja aamun tarve pitää silti kattaa akuilta. Ilman invertterilaturia
laskettu summa on vertailukelpoinen vain, jos generaattorivaihtoehdon hintaan lasketaan mukaan
myös akusto.

Lisäksi molemmissa: laturin kiinnike ja hihna, DC-kaapelit ja -sulakkeet, MasterBus-kaapelit,
asennus. Ehdot halvimmalle:

- **Prestoliten kenttäohjaus pitää olla N-tyyppiä** (negatiivinen), jotta Alpha Pro III sopii
  (**⚠ tarkista**). Muuten säätimeksi tarvitaan toinen malli.
- **Omista kennoista koottu akusto:** BMS:n valinta ja kokoaminen vaativat osaamista, ja
  vakuutusyhtiöltä kannattaa varmistaa, hyväksyykö se itse kootun akuston.
- **Invertterilaturi on suurin yksittäinen kustannus.** Victron MultiPlus-II 24/5000/120-50
  (≈ 1 700–2 400 €) antaa enemmän tehoa kuin Mass Combi Ultra noin puoleen hintaan, mutta
  tarvitsee GX-laitteen (hinta **⚠ ei tiedossa**); MultiPlus-II 24/3000 (≈ 1 259 €) on
  halvin, jos kiuasta ja uunia ei käytetä yhtä aikaa ankkurissa (liesi on kaasulla 2026-10-31). Vertailu kohdassa 2.2.
  Victronin kanssa MasterBus-tapahtuma "Stop charge" ei toimi, ja laturin BMS-ohjaus tehdään Reg
  on -johtimen kautta tai Wakespeed-säätimellä.
- **~~Vaihe 0 ilman toista laturia~~ ei enää riitä,** koska sähkökiuas on päätetty (2026-10-29):
  yksi saunavuoro vie akustosta noin 5,1 kWh, jonka nykyinen 65 A:n laturi palauttaisi vasta
  noin 3,7 tunnin ajossa. Toinen laturi tarvitaan, jos ankkurissa saunotaan ilman maasähköä.
  Jos saunotaan aluksi vain laiturissa maasähköllä, toisen laturin voi lisätä myöhemmin.
- **Kaasuliesi on päätetty** (2026-10-31), joten ruoanlaiton suurin säästö on jo käytetty.
  16 kWh:n akusto jää nyt saunapäivänäkin noin 80 %:n käyttöön.

### 4.2 Koko järjestelmän hinta: ilman generaattoria ja generaattorin kanssa [laskelma]

Kaksi täydellistä kokoonpanoa samoilla hinnoilla (kohdat 2.2, 2.4, 2.5 ja B; sis. ALV). Molemmissa
on sama akusto ja sama invertterilaturi, koska jääkaappi ja 24 V:n kuormat käyvät yöllä akuilta, ja
generaattorikin lataa akustoa invertterilaturin kautta. **Oletus:** generaattori korvaa toisen
laturin; ajossa lataa vain nykyinen 65 A:n laturi, ja generaattori hoitaa loput ankkurissa.

| Osa | Ilman generaattoria | Generaattorin kanssa |
|---|---|---|
| Akusto 16 × EVE MB31, ≈ 16 kWh | ≈ 2 080 € | ≈ 2 080 € |
| Invertterilaturi Mass Combi Ultra 24/3500-100 | ≈ 3 126 € | ≈ 3 126 € |
| Toinen laturi Prestolite 175 A ja Alpha Pro III | ≈ 1 650 € (säädin 330–450 USD ≈ 350 €, **⚠ arvio** kurssista) | – |
| Generaattori Fischer Panda 4000s Neo PMS, 3 kW | – | ≈ 8 314 € |
| Generaattorin asennus: polttoaine, märkäpakoputki, merivesiotto, äänieristys | – | **⚠ ei tiedossa** |
| **Yhteensä** | **≈ 6 900 €** | **≈ 13 500 € + generaattorin asennus** |

Molemmista puuttuvat samat osat: BMS, kotelo ja sulakkeet, kaapelit sekä asennus (**⚠ ei
tiedossa**). Ne eivät muuta lukujen eroa. MB56-kennoilla molemmat ovat noin 900–1 100 € halvempia.

**Ero on noin 6 600 € ja generaattorin asennus.** Jos generaattori tulee toisen laturin lisäksi
(ajossa nopea lataus ja varalla generaattori), generaattorin kanssa noin 15 200 € + asennus.

## 5. Avoimet kysymykset

- [x] Muut AC-kuormat: lista saatu [omistaja 2026-10-28], ks. [loads.yaml](../loads.yaml)
- [ ] Jääkaapin teho ja energiankulutus tyyppikilvestä; muiden laitteiden tehot, kun ne valitaan
- [ ] Onko vedenlämmittimessä koneen jäähdytysvesikierukka?
- [x] Jätteet polttava WC: hylätty; tilalle septi-WC maseraattorilla ja septin hätätyhjennyspumppu [omistaja 2026-10-31]
- [ ] 24 V:n kuormien tehot, kun laitteet valitaan (ks. [loads.yaml](../loads.yaml), `dc_loads`)
- [x] Mitkä laitteet ovat olemassa: vain jääkaappi [omistaja 2026-10-28]
- [x] Liesi: kaasuliesi; uuni: yhdistetty mikro- ja sähköuuni [omistaja 2026-10-31] (kiuas: sähkö, päätetty 2026-10-29)
- [ ] Yhdistetyn mikro- ja sähköuunin malli ja teho (arvio 2–3 kW)
- [ ] Mitkä muut harkinnassa olevista laitteista asennetaan, ja onko vedenlämmitin sähköllä vai esim. koneen jäähdytysvedellä?
- [x] Kuinka monta vuorokautta ollaan ankkurissa ajamatta: enintään alle vuorokausi [omistaja 2026-10-29]
- [ ] Kuinka pitkä ajo on tyypillisesti ankkuripäivän jälkeen (riittääkö noin 2,5 h lataukseen)?
- [ ] Dieselgeneraattori: päätös auki [omistaja 2026-10-29]
- [x] Kannettava bensiiniaggregaatti varalataukseen: Timco SS2200i [omistaja 2026-10-31]
- [ ] Aggregaatin ja bensiinin säilytyspaikka kannella (tuulettuva, laidan yli valuva kaappi) ja käyttöpaikka (pakokaasut poispäin aukoista)
- [ ] Häkävaroittimet makuutiloihin
- [ ] Maasähköpistokkeen ja aggregaatin välinen johto ja liitin (aggregaatin pistorasia → veneen maasähköpistoke)
- [ ] Voiko valitun invertterilaturin tulovirran rajan asettaa noin 7 A:iin, ja toimiiko se kelluvan nollan aggregaatin kanssa?
- [ ] Laturin hihnapyörien välityssuhde ja valitun laturin virtakäyrä: paljonko se lataa 700 rpm:llä ja 1 000–1 200 rpm:llä?
- [x] Maasähkö: kotilaiturissa 15 A [omistaja 2026-10-28]
- [ ] Onko kotilaiturin maasähkö 1-vaiheinen 230 V, ja onko siinä vikavirtasuoja?
- [x] Erotusmuuntaja WM5002: datalehti saatu (pehmokäynnistys on, SL35) [datalehti Airlink WM5002]
- [x] WM5002:n CTE-toisio: keskipisteen maasilta irrotetaan, jolloin lähtö on 230 V [omistaja 2026-10-28, Airlinkin sähköposti]
- [ ] Saako WM5002:n toision toisen pään maadoittaa nollaksi (Airlink, sähköasentaja)?
- [ ] WM5002:n tarkka sijoituspaikka konehuoneessa (kuiva, IP23, 25 kg, eristetyt kiinnikkeet)
- [ ] Tyyppikilven malli on **WM5002 MCB**: onko ensiön suojana MCB-johdonsuoja datalehden SP30-painikesuojan sijaan? (**⚠ tarkista** kotelon sisältä)
- [x] Mahtuuko konehuoneeseen noin 16 kWh:n litiumakusto: kyllä, etenkin jos generaattorille ei tarvitse varata tilaa [omistaja 2026-10-29], ks. [house-battery.md](house-battery.md) (käynnistysakkujen tarkistus: [current-system.md](../current-system.md#5-avoimet-kysymykset))
- [ ] Mahtuuko toinen laturi koneen etupäähän, millainen kiinnike tarvitaan, ja kestääkö hihnaveto 5–7 kW
- [x] Pystyykö Alpha Pro III ottamaan vastaan BMS:n viestin: kyllä, MasterBus "Stop charge" -tapahtuma tai Reg on -johdin [käyttöohje Alpha Pro III]
- [ ] Akuston ja BMS:n valinta: MLI Ultra (suora MasterBus) vai muu BMS ja MasterBusin digitaalitulomoduuli; BMS:ssä ennakkovaroitus ennen katkaisua
- [ ] Voiko Mass Combi Ultra ottaa vastaan saman "Stop charge" -tapahtuman?
- [ ] Hinnat vaihtoehdoille A ja B (akusto, laturi ja invertterilaturi haettu, ks. kohdat 2.2, 2.4 ja 2.5; kiinnike ja generaattori puuttuvat)
