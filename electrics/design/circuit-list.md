# Piirilista

> **Tila:** Luonnos, aloitettu 2026-10-31. Ei päätöstä. Rakenne, sulaketyyppi ja PDM:n rooli on
> päätetty ([dc-distribution.md](dc-distribution.md), [decisions.md](../../decisions.md)); tämä lista
> jakaa kuormat piireihin. Suurin osa laitteista on valitsematta, joten virrat ovat osin **arvioita**
> ([loads.yaml](../loads.yaml)). Johdonsuojien ja kaapelien koot ovat alustavia, ja ne tarkistetaan,
> kun laitteet valitaan ja kaapelireitit mitataan. **Pätevän sähköasentajan pitää tarkastaa lista
> ennen rakentamista**, erityisesti tärkeät kuormat ja 230 V:n puoli.

Tunnukset: `PJ` pääjakelu, `KA` käynnistysakut, `TK` tärkeiden kuormien kisko, `KS` komentosillan
alakeskus, `KH` konehuoneen alakeskus, `AC` 230 V ([dc-distribution.md 4.4](dc-distribution.md#44-piirien-tunnukset)).
Sama tunnus tulee kaapelin merkintään, keskuksen kylttiin ja `loads.yaml`:iin (kenttä `circuit`).

## Mitoitusperiaatteet [laskelma]

- **Virta** = teho / 24 V. Arvioidut tehot on merkitty (**⚠ arvio**).
- **Johdonsuoja:** talojohdonsuoja, jonka datalehdessä on DC-arvo (esim. Schneider iC60N, C-käyrä;
  päätös 2026-10-31). Koko on vähintään laitteen virta ja enintään kaapelin kuormitettavuus.
  Moottoreille (pumput, puhaltimet) valitaan yksi koko suurempi käynnistysvirran takia.
- **Kaapeli:** pienin koko 1,5 mm² mekaanisen kestävyyden vuoksi. 1,5 mm² riittää 10 %:n
  häviöllä, kun virta on enintään 10 A ja kaapeli enintään noin 10 m pitkä (2 · 10 m · 10 A ·
  0,0175 / 1,5 mm² ≈ 2,3 V). 16 A:n johdonsuojan piireihin vähintään 2,5 mm². Tärkeille kuormille
  ja elektroniikalle 3 %:n häviö ([dc-distribution.md 4.2](dc-distribution.md#42-jännitehäviö-ja-kaapelin-koko-laskelma)).
  Kuormitettavuus tarkistetaan kaapelivalmistajan taulukosta (**⚠ tarkista**).
- **PDM-kanava** ([ESP32-PDM design-notes](https://github.com/plektra/ESP32-PDM/blob/main/docs/design-notes.md)):
  `6050` = BTT6050 noin 3,5–4 A, `6010` = BTT6010 noin 8 A, `hc` = suurivirtakortti `pdm-hc2`
  noin 8–20 A. Yli 8 A:n kuormat jaetaan mieluummin kahteen `6010`-kanavaan kuin viedään
  `hc`-kortille, koska `hc`-kortti on kalliimpi.

## Pääjakelu (PJ) ja käynnistysakut (KA)

| Tunnus | Lähtö | Virta | Suoja | Kaapeli | Huomiot |
|---|---|---|---|---|---|
| PJ-00 | Käyttöakuston pääsulake | – | Class T | akuston mukaan | [house-battery.md](house-battery.md) |
| PJ-01 | Invertterilaturi | noin 160 A, huippu yli 300 A | MEGA, ANL tai MRBF valmistajan ohjeen mukaan | valmistajan ohjeen mukaan | Laite valitsematta |
| PJ-02 | Ohjauksen varapumppu P3 | noin 100 A, käynnistysvirta **⚠ ei tiedossa** | MEGA tai ANL, kestettävä käynnistysvirta | vähintään 16 mm² (3 m) | **Turvallisuuskriittinen** ([dc-distribution.md 3](dc-distribution.md#3-tärkeät-kuormat-ja-vikatilanteet)) |
| PJ-03 | Toinen laturi | 150–175 A | laturin ohjeen mukaan | vähintään 35 mm² (3 m) | Tuleva |
| PJ-04 | KS-alakeskuksen syöttö | mitoitus noin 60 A | 60 A | vähintään 25 mm² (6 m) | |
| PJ-05 | KH-alakeskuksen syöttö | mitoitus noin 40 A | 40 A | vähintään 4–6 mm² (2 m), kuormitettavuus ratkaisee | Kaikki KH:n kuormat yhtä aikaa noin 50 A; käytännössä eivät käy yhtä aikaa (**⚠ arvio**) |
| PJ-06 | TK:n syöttö käyttöakustolta (ideaalidiodi) | noin 40–45 A | 50 A | pituuden mukaan | Pilssipumput yhtä aikaa noin 38 A |
| PJ-07–08 | Varalähdöt | – | – | – | Aurinkosäädin, kolmas akku |
| KA-01 | Käynnistinmoottori | **⚠ ei tiedossa** | **⚠ tarkista**, saako käynnistyskaapelin jättää ilman sulaketta | nykyinen | Pysyy ennallaan |
| KA-02 | Koneen ohjausyksikkö | **⚠ ei tiedossa** | **⚠ ei tiedossa** | nykyinen | **Veneellä:** mistä saa nyt virtansa |
| KA-03 | TK:n syöttö käynnistysakuilta (ideaalidiodi, pääkytkimen ohi) | noin 40–45 A | 50 A akun vieressä | pituuden mukaan | |
| KA-04 | Hätärinnankytkin käyttöakustoon | – | – | järeä | Normaalisti auki ([dc-distribution.md 3.2](dc-distribution.md#32-hätärinnankytkin)) |

## Tärkeiden kuormien kisko (TK)

Ei PDM:ää eikä pääkytkintä. Kisko saa virran kummaltakin akustolta (PJ-06, KA-03).

| Tunnus | Kuorma | Virta | Johdonsuoja | Kaapeli (alustava) | Kytkin | Huomiot |
|---|---|---|---|---|---|---|
| TK-01 | Pilssipumppu 1 (SEAFLO 3500 GPH) | 8,0 A, enintään 12,5 A | 16 A | 6 mm² (8 m, 3 %) | **ei kytkintä** (kohokytkin) | Käynnistysvirta **⚠ ei tiedossa**. PDM:n pakotettu käyttö rinnan kohokytkimen kanssa, ks. alla |
| TK-02 | Pilssipumppu 2 | sama | 16 A | 6 mm² | ei kytkintä | |
| TK-03 | Pilssipumppu 3 | sama | 16 A | 6 mm² | ei kytkintä | |
| TK-04 | Kulkuvalot ja mastovalo | 0,4 A (10 W) | 2 A | 1,5 mm² | komentosillan paneeli | |
| TK-05 | Ankkurivalo | 0,2 A (5 W) | 2 A | 1,5 mm² | komentosillan paneeli | |
| TK-06 | VHF Sailor RT2048 | **⚠ ei tiedossa** | laitteen ohjeen mukaan | 3 %:n häviöllä, luultavasti 2,5 mm² | komentosillan paneeli | Lähetysvirta käyttöohjeesta |
| TK-07 | Pilssi- ja ylävesihälytys | alle 1 A (**⚠ arvio**) | 2 A | 1,5 mm² | ei kytkintä | Laite valitsematta |
| TK-08 | Kaasuhälytin (**ehdotus**) | noin 0,1 A (**⚠ arvio**) | 2 A | 1,5 mm² | ei kytkintä | Avoin kysymys, tuleeko TK:lle |

**Pilssipumppujen pakotettu käyttö:** ESP32-PDM:n suurivirtakanava kytketään rinnan kohokytkimen
kanssa ([dc-distribution.md 3](dc-distribution.md#3-tärkeät-kuormat-ja-vikatilanteet)). Kanavan
syötön pitää tulla TK:lta, jotta pakotettu käyttö toimii myös, kun käyttöakusto on irti.
Kytkentä **⚠ tarkista** ESP32-PDM-projektin kanssa.

## Komentosillan alakeskus (KS)

| Tunnus | Kuorma | Virta | Johdonsuoja | Kaapeli (alustava) | PDM-kanava | Huomiot |
|---|---|---|---|---|---|---|
| KS-01 | Sisävalaistus, keula | noin 4,2 A (100 W, **⚠ arvio** jaosta) | 6 A | 1,5 mm² | 6010 | 200 W jaettu kahteen piiriin (ehdotus) |
| KS-02 | Sisävalaistus, perä | noin 4,2 A | 6 A | 1,5 mm² | 6010 | |
| KS-03 | Kansivalaistus, keula | noin 4,2 A | 6 A | 1,5 mm² | 6010 | 200 W jaettu kahteen kanavaan, jotta `hc`-korttia ei tarvita |
| KS-04 | Kansivalaistus, perä | noin 4,2 A | 6 A | 1,5 mm² | 6010 | |
| KS-05 | Työvalo eteen | 4,2 A (100 W) | 6 A | 1,5 mm² | 6010 | |
| KS-06 | Työvalo taakse | 4,2 A (100 W) | 6 A | 1,5 mm² | 6010 | |
| KS-07 | Hakuvalo | 10,4 A (250 W), käynnistysvirta noin 100–160 A | 16 A, C- tai D-käyrä **⚠ tarkista** käynnistysvirtaa vasten | 2,5 mm² (3 m) | hc tai rele | Käynnistysvirta: [searchlight-deicing.md](searchlight-deicing.md#3-ohjaus-ja-kytkentä) |
| KS-08 | Navigointitietokone ja näyttö | **⚠ ei tiedossa** | laitteen mukaan | 3 % | 6010 | |
| KS-09 | AIS, luokka B | noin 0,1 A (3 W, **⚠ arvio**) | 2 A | 1,5 mm² | 6050 | |
| KS-10 | Tutka | **⚠ ei tiedossa** | valmistajan ohjeen mukaan | 3 %, mastoon | 6010 tai hc | Laite valitsematta |
| KS-11 | Atlas-kirkasnäkölasi (oma invertteri) | **⚠ ei tiedossa** | laitteen mukaan | | 6010 | |
| KS-12 | Tuulilasinpyyhkijät | **⚠ ei tiedossa** | laitteen mukaan | | 6010 | Moottori: käynnistysvirta |
| KS-13 | FM-radio (12 V:n muunnin) | alle 1 A (**⚠ arvio**) | 2 A | 1,5 mm² | 6050 | |
| KS-14 | Tuulilasin huurunpoistopuhallin | **⚠ ei tiedossa** | laitteen mukaan | | 6010 | |

KS:n kuormat yhtä aikaa: valot noin 35 A (sisä-, kansi- ja työvalot sekä hakuvalo) ja elektroniikka, eli
PJ-04:n 60 A riittää (**⚠ arvio**, tarkistetaan, kun tutka ja navigointitietokone valitaan).

## Konehuoneen alakeskus (KH)

| Tunnus | Kuorma | Virta | Johdonsuoja | Kaapeli (alustava) | PDM-kanava | Huomiot |
|---|---|---|---|---|---|---|
| KH-01 | Käyttövesipumppu | noin 6,3 A (150 W, **⚠ arvio**) | 10 A | 1,5 mm² | 6010 | Painekytkin pumpussa |
| KH-02 | Harmaavesisumpun pumppu | noin 5 A (120 W, **⚠ arvio**) | 10 A | 1,5 mm² | 6010 | Uimurikytkin |
| KH-03 | Lämmityksen kiertovesipumppu | noin 1,3 A (30 W, **⚠ arvio**) | 2 A | 1,5 mm² | 6050 | |
| KH-04 | Polttoaineen siirtopumppu | noin 4,2 A (100 W, **⚠ arvio**) | 10 A | 1,5 mm² | 6010 | Tyyppikilpi **⚠ tarkista** |
| KH-05 | Savukaasujen poistopuhallin | noin 2,1 A (50 W, **⚠ arvio**) | 4 A | 1,5 mm² | 6050 | |
| KH-06 | Konehuoneen LED-valaistus | noin 2,1 A (50 W, **⚠ arvio**) | 4 A | 1,5 mm² | 6050 | |
| KH-07 | Puhallinkonvektorit (5 tilaa, harkinnassa) | 5 × 0,8 A (5 × 20 W, **⚠ arvio**) | 2 A kukin | 1,5 mm² | 5 × 6050 | Kanava tilaa kohden, jos ohjataan lämpötilan mukaan ([heating/](../../heating/current-system.md)) |
| KH-08 | Hydrauliikan ohjaus: PVE-syöttö hätäseis-releen kautta | **⚠ ei tiedossa** | datalehden mukaan | | ei (rele) | [hydraulics/schematic.md](../../hydraulics/schematic.md) |
| KH-09 | Septi-WC:n maseraattori | noin 12,5 A (300 W, **⚠ arvio**) | 16 A | 2,5 mm², pituus **⚠ ei tiedossa** | ei (WC:n oma painike) | Paikka auki; valmistajan ohje |
| KH-10 | Septin hätätyhjennyspumppu | noin 12,5 A (300 W, **⚠ arvio**) | 16 A | 2,5 mm² | ei (oma kytkin) | Vain hätään; ei etäkäynnistystä |
| KH-11 | Kaasun magneettiventtiili (**ehdotus**) | noin 0,6 A (15 W, **⚠ arvio**) | 2 A | 1,5 mm² | ei (kaasuhälyttimen ohjaus) | Venttiili sulkeutuu, kun virta katkeaa |

**Jatkuvasti päällä olevat** ([dc-distribution.md 2.3](dc-distribution.md#23-konehuoneen-alakeskus-kh)):
oma ryhmä, jonka voi sammuttaa yhdellä johdonsuojalla talveksi. Nämä eivät ole PDM:n takana, koska
Signal K ohjaa PDM:iä, eikä ohjaimen virtaa kannata kytkeä sen omalla laitteella.

| Tunnus | Kuorma | Virta | Johdonsuoja | Huomiot |
|---|---|---|---|---|
| KH-20 | Mean Well DDR-240B-24 (NUC, NMEA 2000 -väylä, 4G-modeemi, PoE-kamerat, mastokamera) | nykyinen kuorma noin 2–3 A (**⚠ arvio**); täydellä 240 W:n teholla noin 11 A | datalehden mukaan **⚠ tarkista** | |
| KH-21 | Mean Well DDR-15G-5 (Raspberry Pi 5, Signal K) | alle 1 A | 2 A | |
| KH-22 | ESP32-PDM-korttien syötöt | kanavien mukaan | jokaiselle kortille oma suoja | Kortin syöttö mitoitetaan sen kanavien yhteisvirralle |

## 230 V (AC)

Kaikki piirit **30 mA:n vikavirtasuojan** takana ja invertterilaturin AC-lähdössä
([dc-distribution.md 6](dc-distribution.md#6-230-vn-jakelu)). **Kiinteät 230 V:n asennukset tekee tai
tarkastaa sähköalan ammattilainen.**

| Tunnus | Piiri | Teho | Johdonsuoja (ehdotus) | Huomiot |
|---|---|---|---|---|
| AC-01 | Sähkökiuas | 2,3 kW | 16 A, kiukaan ohjeen mukaan **⚠ tarkista** | Kuormanhallinta: kontaktori PDM:ltä |
| AC-02 | Jääkaappi | noin 100 W (**⚠ arvio**) | 10 A | Oma piiri |
| AC-03 | Yhdistetty mikro- ja sähköuuni | arviolta 2–3 kW | 16 A | Malli valitsematta |
| AC-04 | Keittiön pistorasiat (vedenkeitin, kahvinkeitin) | enintään noin 3 kW | 16 A | |
| AC-05 | Muut pistorasiat (televisio, laturit) | alle 0,5 kW | 10 A | |
| AC-06 | Ilmanvaihtokone, liesituuletin, poistoilmapuhallin | noin 0,2 kW | 10 A | |
| AC-07 | Öljylämmityksen poltin | alle 230 W | 10 A | |
| AC-08 | Vedenlämmittimen vastus (harkinnassa) | 3 kW | 16 A | Vain maasähköllä; kontaktori tai invertterilaturin maasähkölähtö |

## PDM-kanavien tarve [laskelma, ⚠ arvio]

| | 6050 | 6010 | hc |
|---|---|---|---|
| KS | 2 | 10 (tutka ja hakuvalo mukaan lukematta) | 1 (hakuvalo, ellei rele) |
| KH | 3 + 5 puhallinkonvektoria | 3 | – |
| Pilssipumppujen pakotettu käyttö | – | – | 3 |
| **Yhteensä** | **noin 10** | **noin 13** | **noin 4** |

Neljän kanavan kortteja tarvitaan noin 6 ja suurivirtakortteja (2 kanavaa) noin 2. Ilman
puhallinkonvektoreita 4-kanavaisia kortteja riittää noin 5. Jokaiseen kanavaan tulee lisäksi
johdonsuoja (päätös 2026-10-31).

## Avoimet kysymykset

- [ ] Kaapelireittien pituudet; kaapelikoot lasketaan uudelleen mitatuilla pituuksilla
- [ ] Keskusten paikat (KS:n paikka ei vielä tiedossa [omistaja 2026-10-31])
- [ ] Jaetaanko sisävalaistus ja kansivalaistus kahteen piiriin, kuten ehdotettu?
- [ ] VHF:n, tutkan, navigointitietokoneen, pyyhkijöiden, kirkasnäkölasin ja huurunpoiston virrat, kun laitteet valitaan
- [ ] Hakuvalo: PDM:n suurivirtakanava vai rele, ja johdonsuojan käyrä käynnistysvirtaa vasten
- [ ] Pilssipumppujen käynnistysvirta: riittääkö 16 A C-käyrällä?
- [ ] Mean Well DDR-240B-24:n tulon suojaus datalehdestä
- [ ] Koneen ohjausyksikön syöttö (veneellä)
- [ ] Tuleeko kaasuhälytin TK:lle (TK-08)?
- [ ] Maseraattori-WC:n ja hätätyhjennyspumpun paikat ja valmistajan sulakesuositukset
