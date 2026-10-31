# Tarkistuslista veneelle: sähköjärjestelmä

> **Tila:** Laadittu 2026-10-31 avoimista kysymyksistä. Kun kohta on tehty, kerro tulos Claudelle
> (esim. `/add-info`), niin se kirjataan oikeisiin dokumentteihin ja kohta rastitetaan sekä tänne että
> alkuperäiseen listaan.

**Ota mukaan:** puhelin (kuvat), mittanauha, yleismittari, pihtivirtamittari (DC, vähintään 100 A),
muistiinpanot. **Valokuva riittää** tyyppikilvistä ja merkinnöistä; kuvia ei tallenneta repoon ilman
lupaa, ja omat kuvat kuuluvat kansioon `electrics/img/`.

**Turvallisuus:** irrota akut ja maasähkö ennen kuin avaat kytkentöjä. Älä mittaa resistanssia
jännitteisestä piiristä. Konehuoneessa varo pyöriviä osia, kun kone käy.

## 1. Tärkein: estää eniten muuta työtä

- [ ] **Kaapelireittien pituudet** metreinä, yhteen suuntaan (kaapelikoot ja piirilista):
  - [ ] akut → komentosillan alakeskuksen mahdollinen paikka
  - [ ] komentosilta → maston juuri ja maston huippu
  - [ ] komentosilta → katto (hakuvalo, noin 3 m arvio)
  - [ ] akut → keula ja asuintilat (sisävalot, pumput)
  - [ ] akut → kukin pilssipumppu (3 kpl)
  - [ ] akut → septi-WC:n ja maseraattorin mahdollinen paikka
  - [ ] akut → P3:n moottori
  - Lähde: [dc-distribution.md 8](design/dc-distribution.md#8-avoimet-kysymykset), [circuit-list.md](design/circuit-list.md#avoimet-kysymykset)
- [ ] **Keskusten paikat:** mihin komentosillan alakeskus (DIN-kotelo noin 14 johdonsuojalle ja PDM-korteille) mahtuu?
  Onko veneellä vanha keskus tai kaapelointia, jota voi käyttää uudelleen? Kuva ja mitat.
- [ ] **Akuston paikka konehuoneessa:** kaksi 8S-akkua ja tila kolmannelle (kennot kukin noin
  574 × 174 × 207 mm, noin 45 kg, ilman koteloa). Mittaa vapaa tila ja kuvaa paikka.
  ([house-battery.md](design/house-battery.md))
- [ ] **Invertterilaturin paikka:** Victron MultiPlus-II 24/5000 (koko ja paino **⚠ tarkista**
  datalehdestä), lähellä akkuja, kuiva paikka. Samalla erotusmuuntajan WM5002 paikka (25 kg, IP23).

## 2. Mittaukset

- [ ] **Resistanssi akun miinuksen ja rungon välillä**, kun kaikki kuormat ja maasähkö on irrotettu.
  Lähes nolla = yhteys on olemassa. Selvitä, kulkeeko yhteys vain koneen kautta (käynnistin, laturi).
  ([dc-distribution.md 5](design/dc-distribution.md#5-miinus-ja-teräsrunko))
- [ ] **P3:n virta pihtivirtamittarilla**, kone käy:
  - [ ] tyhjäkierrossa (ruoria ei käännetä)
  - [ ] ruoria käännettäessä ääriasentoon
  - [ ] käynnistyshetken huippu, jos mittari näyttää sen
  ([dc-distribution.md 3.3](design/dc-distribution.md#33-p3-käynnistysakuilta-päätetty-2026-10-31))
- [ ] **Käynnistysakkujen lepojännite**, kun CTEK on ollut irti muutaman tunnin.
- [ ] **Hakuvalon etulasin halkaisija** tarkemmin (arvio noin 350 mm).

## 3. Tyyppikilvet ja merkinnät (valokuva)

- [ ] **Käynnistysakut:** tyyppi (märkä, AGM), kapasiteetti Ah, kylmäkäynnistysvirta CCA, ikä;
  kytkentä (luultavasti 2 × 12 V sarjassa). Riittävätkö P3:lle?
- [ ] **P3:n moottori:** teho, virta, käynnistysvirta jos ilmoitettu; pumpun merkinnät.
- [ ] **Nykyinen laturi (65 A):** merkinnät; **hihnapyörien halkaisijat** laturissa ja koneessa
  (välityssuhde: paljonko laturi tuottaa 700 rpm:llä).
- [ ] **Koneen etupää:** mahtuuko toinen laturi (150–175 A), ja mihin kiinnike tulisi? Kuvat ja
  mitat. ([ac-power-source.md 2.5](design/ac-power-source.md#25-toisen-laturin-hintataso-haettu-2026-10-28))
- [ ] **Hakuvalon polttimo:** merkintä polttimon kyljessä (luultavasti EHJ / A1/223, kanta G6.35).
- [ ] **Polttoaineen siirtopumppu:** teho tai virta.
- [ ] **Jääkaappi:** teho ja energiankulutus (kWh/vrk).
- [ ] **WM5002:n sisältä:** onko ensiön suojana MCB-johdonsuoja vai SP30-painikesuoja?

## 4. Selvitettävät kytkennät

- [ ] **Mistä koneen ohjausyksikkö saa virtansa** (käynnistysakut, pääkytkin, sulake)?
- [ ] **Pilssipumput:** sijainnit, nykyinen syöttö (suoraan akulta pääkytkimen ohi?) ja
  sulakekoot.
- [ ] **Onko käynnistin ja laturi maadoitettu koneen runkoon** (vai eristettyä mallia)?
- [ ] **Mitä Mean Well DDR-240B-24 syöttää** nykyisin (NUC, NMEA 2000, modeemi, kamerat)?

## 5. Myöhemmin, käytössä

- [ ] Hakuvalo: ensimmäisellä pakkasajolla kuinka nopeasti halogeeni sulattaa lasin ja jäätyykö
  katon läpivienti ([searchlight-deicing.md](design/searchlight-deicing.md#5-avoimet-kysymykset)).
- [ ] Sauna: todellinen kulutus akkumonitorista ensimmäisillä kerroilla (arvio 3,7 kWh / 2 h).

Lisäksi kotilaiturilla: onko maasähkö 1-vaiheinen 230 V, ja onko siinä vikavirtasuoja?
