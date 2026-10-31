# Käyttöakusto: koko ja itse kootut LiFePO4-kennot

> **Tila:** Selvitys, aloitettu 2026-10-29, päivitetty 2026-10-31 (kaasuliesi, yhdistetty mikro- ja sähköuuni, polttava WC hylätty; tarve laskettu uudelleen). Ei päätöstä. Kennojen hinnat ja saatavuus vaihtelevat;
> tarkista ennen tilausta.

Vanhat käyttöakut on purettu, ja nyt kaikki 24 V:n kuormat ottavat virtansa käynnistysakuilta
[omistaja 2026-10-29], ks. [current-system.md](../current-system.md#1-dc-järjestelmä). Tämä
selvitys mitoittaa uuden käyttöakuston kaikilla tähän mennessä listatuilla kuormilla ja vertaa
itse koottavia kennovaihtoehtoja. Invertteri, laturit ja AC-kuormat:
[ac-power-source.md](ac-power-source.md).

## 1. Tarve yhdelle ankkurivuorokaudelle [laskelma]

Ankkurissa ollaan enintään alle vuorokausi ajamatta [omistaja 2026-10-29], joten akusto mitoitetaan
yhdelle ankkurivuorokaudelle. Ajo ja maasähkö lataavat sen.

Oletukset: AC-kuormat [loads.yaml](../loads.yaml) (`loads`) ja
[ac-power-source.md, kohta 2.1](ac-power-source.md#21-koko-ankkurivuorokauden-energiatarve-laskelma),
invertterin hyötysuhde 90 %. 24 V:n kuormat (`dc_loads`) noin 2,3 kWh/vrk lämmityskaudella,
otetaan akustosta suoraan. Kaikki laitteiden tehot ja käyttöajat ovat osin arvioita (**⚠ arvio**).

**Päivitetty 2026-10-31:** liesi on kaasuliesi, uuni yhdistetty mikro- ja sähköuuni, ja polttava WC
on hylätty (tilalle septi-WC 24 V:n maseraattorilla) [omistaja 2026-10-31]. Nykyinen suunnitelma on
rivit **E–G**. Rivit A–D ovat aiempia vertailuja (24 V:n kuormat niissä 2,2 kWh).

| Tilanne | AC akustosta | 24 V | **Akustosta yhteensä** |
|---|---|---|---|
| **E. Nykyinen suunnitelma, kiuas ylärajalla (4,6 kWh)** | 11,0 kWh | 2,3 kWh | **≈ 13,3 kWh** |
| **F. Kuten E, kiukaan todennäköinen kulutus (3,7 kWh)** | 10,0 kWh | 2,3 kWh | **≈ 12,3 kWh** |
| **G. Päivä ilman saunaa** | 5,9 kWh | 2,3 kWh | **≈ 8,2 kWh** |
| A. Kaikki harkitut laitteet sähköisinä, kiuas ylärajalla (4,6 kWh) | 12,7 kWh | 2,2 kWh | **≈ 14,9 kWh** |
| B. Kuten A, kiukaan todennäköinen kulutus (3,7 kWh) | 11,7 kWh | 2,2 kWh | **≈ 13,9 kWh** |
| C. Kuten B, mutta kaasu- tai dieselliesi (ruoanlaitto pois sähköstä) | 8,3 kWh | 2,2 kWh | **≈ 10,5 kWh** |
| D. Päivä ilman saunaa, muuten kuten A | 7,5 kWh | 2,2 kWh | **≈ 9,7 kWh** |

**Jätteet polttava WC** olisi lisännyt arviolta 4–8 kWh vuorokaudessa; se on hylätty [omistaja
2026-10-31]. Septi-WC:n maseraattori ja hätätyhjennyspumppu ovat mukana 24 V:n kuormissa (noin
0,01 kWh/vrk, **⚠ arvio**).

### Nimelliskapasiteetti

LiFePO4-akuston nimellisjännite on 8 kennolla sarjassa (8S) 25,6 V. Taulukossa on kaksi
käyttöastetta: 80 % (aiempien laskelmien oletus, pitkä ikä) ja 90 % (sallittu satunnaisesti,
esim. saunapäivinä; LiFePO4 kestää sen hyvin, kun BMS katkaisee ajoissa).

| Tilanne | Nimellistä, 80 % käytössä | Ah @ 25,6 V | Nimellistä, 90 % käytössä | Ah @ 25,6 V |
|---|---|---|---|---|
| A | 18,6 kWh | ≈ 730 Ah | 16,6 kWh | ≈ 650 Ah |
| B | 17,4 kWh | ≈ 680 Ah | 15,4 kWh | ≈ 600 Ah |
| C | 13,1 kWh | ≈ 510 Ah | 11,7 kWh | ≈ 460 Ah |
| D | 12,1 kWh | ≈ 470 Ah | 10,8 kWh | ≈ 420 Ah |
| A + polttava WC (8 kWh; hylätty 2026-10-31) | ≈ 30 kWh | ≈ 1 160 Ah | ≈ 26 kWh | ≈ 1 030 Ah |
| **E** | **16,6 kWh** | **≈ 650 Ah** | **14,8 kWh** | **≈ 580 Ah** |
| **F** | **15,4 kWh** | **≈ 600 Ah** | **13,7 kWh** | **≈ 530 Ah** |
| **G** | 10,3 kWh | ≈ 400 Ah | 9,1 kWh | ≈ 360 Ah |

**Johtopäätös (päivitetty 2026-10-31):** noin **16 kWh (≈ 628 Ah @ 25,6 V)** riittää täyteen
saunapäivään nykyisellä suunnitelmalla. Saunapäivänä akustoa käytetään noin 76–83 % (F–E), ja
päivänä ilman saunaa noin 51 % (G) [laskelma]. Aiemmin sähköliedellä saunapäivän käyttö oli
noin 85–93 %. Koko pysyy samana, mutta varmuusvara kasvoi. Pienempi akusto ei kannata, koska
kennovaihtoehdot antavat valmiiksi noin 16 kWh, ja 80 %:n käytöllä tarve on noin 15,4–16,6 kWh.
Polttava WC on hylätty, joten akuston kasvatusta sitä varten ei tarvita.

### Herkkyys: sauna 4 h ankkurissa [laskelma, 2026-10-31]

Jos saunavuoro pidennetään kahdesta neljään tuntiin (kysymys [omistaja 2026-10-31], ei päätös).
Oletukset kuten yllä: yläraja = kiuas täydellä teholla koko ajan; todennäköinen = 1 h täysi teho ja
sen jälkeen noin 60 % (termostaatti), **⚠ arvio**.

| | Kiuas 2 h | Kiuas 4 h |
|---|---|---|
| Kiukaan energia, yläraja / todennäköinen | 4,6 / 3,7 kWh | 9,2 / 6,4 kWh |
| Saunapäivä akustosta yhteensä, yläraja (E) | ≈ 13,3 kWh | **≈ 18,4 kWh** |
| Saunapäivä akustosta yhteensä, todennäköinen (F) | ≈ 12,3 kWh | **≈ 15,3 kWh** |
| 16 kWh:n akuston käyttö, yläraja / todennäköinen | 83 % / 76 % | **yli 100 % / 95 %** |
| Akusto 80 %:n käytöllä, yläraja / todennäköinen | 16,6 / 15,4 kWh | **23 / 19 kWh** (≈ 900 / 750 Ah) |
| Lataus ajossa (noin 6,7 kW, molemmat laturit) | noin 2–2,5 h | noin 3 h |
| Lataus maasähköllä (noin 2,9 kW) | noin 4,5–5 h | noin 6,5 h |

**Johtopäätös:** 16 kWh ei riitä neljän tunnin saunaan. Todennäköisellä kulutuksella akusto
tyhjenisi lähes loppuun (95 %), jolloin ohjauksen sähköiselle varapumpulle P3 ei jäisi varaa.
Vaihtoehdot:

1. **Akusto noin 24 kWh** (24 × MB31, 8S3P eli kolmas 8S-akku): kennoja noin 1 040 € lisää
   (8 × 129,95 €, Akkula 2026-10-28), lisäksi kolmas BMS (**⚠ ei tiedossa**), noin 45 kg ja
   noin 0,02 m³ kennoja (ilman koteloa). Kattaa ylärajankin noin 76 %:n käytöllä.
2. **Pääkone tyhjäkäynnillä saunan loppuajan:** toinen laturi tuottaa tyhjäkäynnillä vain osan
   nimellisvirrastaan (välityssuhde **⚠ ei tiedossa**, ks. [ac-power-source.md 4](ac-power-source.md#4-suositus-ei-päätös)).
   Esimerkiksi 80 A × 28 V ≈ 2,2 kW kattaisi lähes koko kiukaan tehon (**⚠ arvio**).
3. **Pitkä sauna vain maasähköllä tai ajopäivän päätteeksi,** ankkurissa 2 h. Ei lisäkustannusta.
4. **Kannettava bensiiniaggregaatti (noin 1,8 kW) saunan aikana** (**päätetty 2026-10-31: Timco SS2200i**): akustosta kuluu neljän tunnin
   saunaan vain noin 3 kWh, ja saunapäivä jää noin 70 %:iin 16 kWh:sta. Hinta noin 370–1 700 €;
   bensiinin säilytys ja häkä pitää hoitaa, ks. [ac-power-source.md, kohta D](ac-power-source.md#d-kannettava-bensiiniaggregaatti-varalataukseen-selvitetty-2026-10-31).

Invertteri ei muutu: teho on sama, vain aika pitenee. Kiukaan noin 106 A on 16 kWh:n akustolle
noin 0,17 C, joten neljän tunnin käyttö ei rasita kennoja. **Päätetty 2026-10-31:** optio kolmannesta 8S-akusta (noin 24 kWh yhteensä) pidetään auki
[omistaja 2026-10-31]. Saunan pituudesta ei ole päätetty. Varalataukseen hankitaan Timco SS2200i
(päätös 2026-10-31), jolla neljän tunnin sauna onnistuu 16 kWh:n akustolla (noin 70 %:n käyttö), joten
kolmatta akkua ei sitä varten todennäköisesti tarvita. Siksi akusto kootaan kahtena
erillisenä 8S-akkuna, ja konehuoneesta varataan tila kolmannelle akulle sekä pääjakeluun lähtö
(PJ-07) ja BMS-ohjaukselle valmius.

## 2. Itse kootut kennot

Molemmat alla olevat vaihtoehdot antavat **8S, 628 Ah, noin 16,1 kWh**. Kennot ovat
prismaattisia LiFePO4-kennoja ilman suojauksia; BMS on pakollinen.

| | **8 × EVE MB56 (8S1P)** | **16 × EVE MB31 (8S2P)** |
|---|---|---|
| Kenno | 3,2 V, 628 Ah, 2,01 kWh | 3,2 V, 314 Ah, 1,0 kWh |
| Mitat (kenno) | 352,3 × 71,7 × 205 mm | 173,7 × 71,7 × 204,6 mm (napoineen 207,2 mm) |
| Paino (kenno) | noin 11,4–11,5 kg | noin 5,4–5,6 kg |
| Kennot yhteensä | noin 92 kg | noin 90 kg |
| Kennopaketti ilman koteloa | noin 574 × 352 × 207 mm | noin 574 × 348 × 207 mm (kaksi 8 kennon riviä) |
| Syklit (valmistajan mukaan, 25 °C, 70 % jäljellä) | noin 8 000 | 8 000 |
| Jatkuva virta 0,5 C | noin 314 A | 157 A/kenno → 314 A (2P) |
| Hinta kennoilta | noin 119–150 €/kenno → **≈ 950–1 200 €**; usein loppu varastosta | 129,95 €/kenno (Akkula.fi) → **≈ 2 080 €** |
| Kytkennät | 7 sarjakiskoa, 8-kanavainen BMS | 2P-rinnankytkennät kennotasolla (tai kaksi erillistä 8S-akkua), enemmän kiskoja ja liitoksia |
| Lähteet | [Nkon](https://www.nkon.nl/en/eve-mb56-prismatic-628ah-lifepo4-3-2v-grade-a-single-stud-2.html), [Fogstar](https://www.fogstar.co.uk/collections/all/products/eve-mb56-3-2v-628ah-lifepo4-cell), [Gobel Power](https://www.gobelpower.com/eu-stock-eve-mb56-32v-628ah-lifepo4-battery-cell-8000-cycles_p242.html), [Notebookcheck](https://www.notebookcheck.net/2-kWh-for-around-175-EVE-s-new-MB56-cells-coming-soon.1117006.0.html) | [Akkula.fi](https://akkula.fi/tuote/eve-mb31-grade-a-lifepo4-314ah-32v-1kwh-prismaattinen-akkukenno-ruuviliitoksin/), [18650 Battery Store](https://www.18650batterystore.com/en-gb/products/eve-mb31-grade-a-cells-3-2v-lifepo4-314ah-battery), [lifepo4.com.au](https://lifepo4.com.au/shop/cells-lifepo4/eve/automotive-grade/314ah-mb31/eve-mb31-314ah-3-2v-lfp-a) |

Arvot ovat jälleenmyyjien sivuilta (haettu 2026-10-29, Akkula 2026-10-28); **⚠ tarkista** EVE:n
datalehdistä ennen tilausta. MB31:n latausalue on 0 (tai 2) – 60 °C, purku −30…60 °C.

**Virtojen riittävyys** [laskelma]: 3,5 kW:n invertteri ottaa noin 160 A, 24 V:n kuormat
hetkellisesti enintään noin 50–90 A (valot noin 46 A, pilssipumput enintään noin 38 A, jos ne ovat
käyttöakustolla) ja hydrauliikan varapumppu noin 100 A. Kaikki yhtä aikaa noin 300–350 A, mikä on
628 Ah:n akustolle noin 0,5 C, eli kennojen jatkuvan virran rajalla. Tavallisessa käytössä virrat
ovat selvästi pienempiä.

### Suositus (ei päätös)

- **Edullisin: 8 × EVE MB56.** Puolet halvempi kuin MB31-ratkaisu ja vähemmän liitoksia, mutta
  saatavuus on epävarma, ja Alibaba-tyyppisten myyjien kennojen aitous kannattaa varmistaa.
  Osta tunnetulta eurooppalaiselta myyjältä (esim. Nkon) ja pyydä kennojen mittausraportti.
- **Varmin saatavuus: 16 × EVE MB31** suomalaisesta kaupasta. Kytke mieluiten **kahdeksi
  erilliseksi 8S-akuksi, kummallakin oma BMS ja sulake.** Silloin yhden BMS:n katkaisu ei
  pimennä koko venettä, ja akustoa voi kasvattaa myöhemmin kolmannella akulla. Lisäkustannus on toinen BMS.
- **Kasvatus myöhemmin:** jos iso kuorma tulee, 24 kWh:iin pääsee 24 × MB31 (8S3P, mieluiten
  kolmena erillisenä 8S-akkuna). MB56:lla 8S-akkuja saa vain 8 kennon erinä (16 tai 32 kWh);
  aiempi maininta "12 × MB56" oli virhe (korjattu 2026-10-31). Varaa tilaa ja sulakkeille yksi lisälähtö jo nyt.

## 3. Mitä itse koottu akusto vaatii kennojen lisäksi

Hinnat **⚠ ei tiedossa**; selvitetään, kun kennot ja BMS valitaan.

| Osa | Vaatimus Vegalla |
|---|---|
| BMS | 8S, LiFePO4. Jatkuva virta vähintään noin 300 A, tai releohjattu BMS, joka katkaisee kontaktoreilla. **Erilliset lähdöt latauksen estolle ja kuormien katkaisulle**, jotta laturin säädin (Alpha Pro III, Reg on / MasterBus "Stop charge") ja invertterilaturi saavat varoituksen ennen kuin BMS katkaisee, ks. [ac-power-source.md](ac-power-source.md). **Latauksen esto alle 0 °C:ssa.** Mieluiten CAN-, NMEA 2000- tai Signal K -liitäntä valvontaan |
| Kennojen väliset liitokset | **Kuparikiskot, ei kaapeleita** kennojen välillä. MB31:ssä on jälleenmyyjien mukaan yksi M6-napa (hitsattu pultti tai kierrereikä, malli **⚠ tarkista** ostettavasta erästä), ja kennon mukana tulee yleensä nikkelöity kuparikisko. Veneessä mieluiten **joustavat (laminoidut) kiskot**, jotka sietävät tärinää ja kennojen turpoamista. Kiristysmomentti jälleenmyyjien mukaan enintään noin 5–6 Nm ([Gobel Power](https://www.gobelpower.com/eu-stock-grade-a-eve-32v-314ah-mb31-rechargeable-lifepo4-battery-cell_p193.html?cPath=0), [Wistek](https://wis-tek.com/products/eve-mb31-3-2v-314ah-grade-a-brand-new-lifepo4-battery-prismatic-cell-wistekusa-stock)), **⚠ tarkista** EVE:n datalehdestä. Kaapelia käytetään vain kennorivien välillä, jos kiskot eivät ylety, ja akun pääliitännöissä |
| Kennojen puristus | Prismaattiset kennot pitää puristaa kehikossa valmistajan ohjeen mukaan (arvo **⚠ ei tiedossa**, EVE:n datalehdestä) |
| Pääsulake | Class T -sulake tai vastaava, jonka katkaisukyky riittää LiFePO4:n oikosulkuvirralle, mahdollisimman lähelle akun napaa |
| Kotelo ja kiinnitys | Noin 100–110 kg kennoineen, kiinni rungossa niin, ettei se liiku kallistuksissa. Ilmanvaihto ja suoja vedeltä |
| Lämmitys | Jos vene on käytössä kylmänä vuodenaikana, lämmityskalvo tai muu ratkaisu, jotta latautuminen on mahdollista |
| Käynnistysakkujen erotus | Erotusrele tai DC-DC-laturi; käynnistysakut pysyvät lyijyakkuina, ja CTEK voi jatkaa niiden ylläpitolatausta, ks. [current-system.md](../current-system.md#1-dc-järjestelmä) |
| Akkumonitori | Shuntti, joka mittaa todellisen kulutuksen; sillä arviot voi korvata mitatuilla |

**Pilssipumput eivät saa jäädä käyttöakuston BMS:n taakse,** koska BMS voi katkaista akuston
kokonaan (alijännite, ylilämpö, vika). Turvallisinta on syöttää ne käynnistysakuilta tai molemmilta
akustoilta diodien tai erotusreleen kautta, kukin omalla sulakkeellaan pääkytkimen ohi.
Pilssipumppujen ja akuston kytkennät kannattaa tarkastuttaa pätevällä sähköasentajalla ennen
käyttöönottoa.

Itse koottu akusto: selvitä vakuutusyhtiöltä, hyväksyykö se sen.

## 4. Laajennettavuus: aurinkopaneelit ja maasähkölaturi

Kumpikin onnistuu, kun akusto ja BMS suunnitellaan alusta asti useammalle laturille.

**Tärkein periaate: BMS:n pitää pystyä pysäyttämään jokainen laturi.** Kun latureita on useita
(koneen laturi(t), invertterilaturi, aurinkosäädin, maasähkölaturi), jokaisen pitää ottaa vastaan
BMS:n latauksen esto (väylä, kuten MasterBus tai CAN, tai ohjausjohdin), ennen kuin BMS katkaisee
akuston. Valitse BMS, jossa on riittävästi lähtöjä, tai vedä yhteinen latauksen estosignaali,
johon kaikki laturit kytketään. Varaa myös DC-jakoon ja sulakkeisiin lähdöt tuleville latureille.

### Aurinkopaneelit

- **Mass Combi Ultrassa on oma aurinkopaneelitulo** (Pro-mallissa ei,
  ks. [ac-power-source.md](ac-power-source.md#muut-invertterilaturivaihtoehdot-haettu-2026-10-29)).
  Tulon teho- ja jännitealue **⚠ tarkista** datalehdestä. Muuten tarvitaan erillinen 24 V:n
  MPPT-säädin, jossa on LiFePO4-profiili ja BMS-ohjaus.
- **Tuotto Suomessa** (**⚠ arvio**): kesällä aurinkoisena päivänä noin 3–5 kWh jokaista
  asennettua kilowattia (kWp) kohti, keväällä ja syksyllä selvästi vähemmän, talvella lähes nolla.
  Esim. 400 Wp kattaa kesäpäivänä noin 1,2–2 kWh eli suuren osan 24 V:n kuormista (noin
  2,2 kWh/vrk). Saunaan ja sähköruoanlaittoon se ei riitä, mutta vähentää ajon tai maasähkön
  tarvetta ja pitää akuston täynnä laiturissa.
- **Paikka on rajallinen:** katolle tulevat GNSS-antenni ja kulkuvalot, ja mastoon antennit,
  tutka ja kamera (ks. [current-system.md](../current-system.md#34-maston-ja-katon-varustelu)).
  Paneelien paikka, varjostus ja kiinnitys **⚠ ei tiedossa**.

### Litiumakkujen maasähkölaturi

- **Invertterilaturi on jo maasähkölaturi** (Mass Combi Ultra 100 A). Erillistä laturia ei
  tarvita, jos invertterilaturi hankitaan.
- **Erillinen 24 V:n LiFePO4-laturi** (esim. 15–30 A, jossa on LiFePO4-profiili ja ohjaustulo
  BMS:lle) sopii, jos hankinnat tehdään **vaiheittain**: ensin akusto, BMS ja pieni maasähkölaturi,
  invertterilaturi myöhemmin. Myöhemmin se voi jäädä varalaturiksi. Hinta **⚠ ei tiedossa**.
- **Nykyinen CTEK MULTI XT 14000 ei sovi litiumille** (vain lyijyakuille), mutta jää
  käynnistysakkujen ylläpitolataukseen.

## 5. Avoimet kysymykset

- [x] Tuleeko jätteet polttava WC: ei, tilalle septi-WC maseraattorilla [omistaja 2026-10-31]; noin 16 kWh riittää
- [x] Liesi: kaasuliesi; uuni: yhdistetty mikro- ja sähköuuni [omistaja 2026-10-31]
- [x] Mahtuuko akusto konehuoneeseen: kyllä, etenkin jos generaattorille ei tarvitse varata tilaa (paapuurin puoli) [omistaja 2026-10-29]
- [ ] Akuston tarkka paikka konehuoneessa; riippuu osin generaattoripäätöksestä. Varataan tila myös kolmannelle 8S-akulle (noin 574 × 174 × 207 mm kennoja, noin 45 kg, ilman koteloa) [laskelma]
- [ ] Saunan pituus ankkurissa: 2 h vai 4 h? Ratkaisee, hankitaanko kolmas akku
- [ ] Kennot: MB56 (halvempi, saatavuus epävarma) vai MB31 (kaksi erillistä akkua)?
- [ ] BMS:n valinta (releohjattu vai MOSFET, latauksen eston lähdöt, valvontaliitäntä)
- [ ] Kennojen puristusvoima EVE:n datalehdestä
- [ ] MB31:n napatyyppi (hitsattu M6-pultti vai kierrereikä), kiristysmomentti ja kiskojen poikkipinta EVE:n datalehdestä; joustavat kiskot erikseen, jos myyjän kiskot ovat jäykkiä
- [ ] Vakuutusyhtiön kanta itse koottuun akustoon
- [ ] Aurinkopaneelit: tuleeko niitä, ja mihin ne mahtuisivat ilman varjostusta?
- [ ] Hankitaanko vaiheittain (ensin akusto ja pieni maasähkölaturi, invertterilaturi myöhemmin)?
