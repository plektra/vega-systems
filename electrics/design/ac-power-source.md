# AC-sähkön lähde: hydrauligeneraattori, dieselgeneraattori vai akusto ja invertteri

> **Tila:** Selvitys, aloitettu 2026-10-28, päivitetty 2026-10-28 (AC-kuormien lista; vain jääkaappi olemassa). Ei päätöstä. Hinnat puuttuvat; ne tarkistetaan
> tarjouksista ennen päätöstä.

## 1. Tarve

| Kohde | Arvo | Lähde |
|---|---|---|
| Milloin AC-sähköä tarvitaan | Ajossa ja ankkurissa | [omistaja 2026-10-28] |
| Generaattori | Ei asennettu; tila varattu konehuoneen paapuurin puolelle | [omistaja 2026-10-28], [blogi 2017-04-19] |
| Sähkökiuas (harkinnassa; ankkurissa suurin energiankuluttaja) | 2,3 kW, päällä kerrallaan noin 2 h | [omistaja 2026-10-28] |
| Muut AC-kuormat | Jääkaappi (noin 130 l ja pakastelokero), laturit (esim. kannettava tietokone), kahvinkeitin, vedenkeitin, liesi, uuni, liesituuletin, poistoilmapuhallin, ilmanvaihtokone, televisio, öljylämmityksen poltin (alle 1 A), vedenlämmittimen sähkövastus 3 kW. **Vain jääkaappi on olemassa;** muut ovat harkinnassa, eikä kaikkia välttämättä asenneta. Tehot: [loads.yaml](../loads.yaml) | [omistaja 2026-10-28] |
| Maasähkö | **⚠ ei tiedossa** | |
| Kuinka monta vuorokautta ankkurissa ilman ajoa | **⚠ ei tiedossa** | |
| DC-jännite | 24 V | [vessel/README.md](../../vessel/README.md#sähköjärjestelmän-perustiedot) |

Kokonaistarve on alle 10 kVA. Kiuas on suurin energiankuluttaja ankkurissa, mutta sähköruoanlaitto,
ilmanvaihtokone ja lämmityksen poltin kuluttavat yhdessä lähes yhtä paljon (ks. kohta 2.1).

Koska vain jääkaappi on olemassa, laitevalinnat ovat vielä auki. **Jokainen sähkölaite kasvattaa
akustoa, ja juuri nyt on halvin hetki valita laitteet energiankulutuksen perusteella.**

## 2. Kiukaan energiatarve akustosta [laskelma]

Oletukset: kiuas ottaa täyttä tehoa koko kaksi tuntia (yläraja; termostaatti katkoo lämpenemisen
jälkeen, joten todellinen kulutus on todennäköisesti pienempi), invertterin hyötysuhde 90 %,
LiFePO4-akuston käytettävissä oleva osuus 80 %, jännite 24 V.

| Suure | Arvo |
|---|---|
| Energia kiukaalle | 2,3 kW × 2 h = 4,6 kWh |
| Energia akustosta | 4,6 / 0,9 ≈ 5,1 kWh |
| Akkuvirta kiukaan ollessa päällä | 2300 / 0,9 / 24 ≈ 106 A |
| Kiukaan vaatima kapasiteetti | 5,1 kWh / 24 V ≈ 213 Ah käytettävissä → ≈ 265 Ah nimelliskapasiteettia |
| Akusto | Muut kuormat mukaan lukien noin 400–650 Ah, ks. kohdat 2.1 ja 4 |
| Invertteri | Kiukaalle yksin riittäisi 3 kW; muiden kuormien kanssa noin 5 kW, ks. kohta 2.2 |

### 2.1 Koko ankkurivuorokauden energiatarve [laskelma]

Laskelma on **yläraja**: siinä ovat mukana kaikki harkinnassa olevat laitteet. Pelkkä olemassa
oleva jääkaappi vie noin 0,8 kWh/vrk (≈ 0,9 kWh akustosta, arvio).

Vain kiukaan, vedenlämmittimen (3 kW) ja polttimen virran (alle 1 A) arvot ovat omistajalta. Muiden
laitteiden tehot ja kaikki käyttöajat ovat **arvioita** tyypillisistä kodinkoneista
([loads.yaml](../loads.yaml)); ne pitää korvata laitteiden tyyppikilpien arvoilla. Poistoilmapuhallin
puuttuu summasta, koska sen käyttöaikaa ei tiedetä. Vedenlämmittimen vastus on jätetty pois, ks.
kohta 4.

| Kuormaryhmä | kWh/vrk (arvio) |
|---|---|
| Sähkökiuas, 2 h | 4,6 |
| Ruoanlaitto: liesi, uuni, vedenkeitin, kahvinkeitin, liesituuletin | 3,1 |
| Ilmanvaihtokone, 24 h | 1,2 |
| Öljylämmityksen poltin, 6 h lämmityskaudella | 1,2 |
| Jääkaappi | 0,8 |
| Televisio ja laturit | 0,5 |
| **Yhteensä AC** | **≈ 11,4** |
| **Akustosta** (invertterin hyötysuhde 90 %) | **≈ 12,7 kWh** |
| Ilman kiuasta, akustosta | ≈ 7,5 kWh |

| Akustotarve yhdelle ankkurivuorokaudelle, 24 V | Litium (LiFePO4), 80 % käytettävissä | Lyijy (AGM tai geeli), 50 % käytettävissä |
|---|---|---|
| Saunan kanssa | ≈ 660 Ah (≈ 16 kWh nimellistä) | ≈ 1060 Ah (≈ 25 kWh nimellistä) |
| Ilman saunaa | ≈ 390 Ah (≈ 9,4 kWh nimellistä) | ≈ 630 Ah (≈ 15 kWh nimellistä) |

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

Kiuas yksin mahtuu 3 kW:n invertteriin, mutta ruoanlaitossa kuormat osuvat päällekkäin: esim. liesi
(arvio 3 kW) ja vedenkeitin (arvio 2 kW) ovat yhdessä noin 5 kW. **Invertterin pitää olla noin 5 kW**
(**⚠ arvio**, tarkistetaan tyyppikilvistä), tai sitten tarvitaan kuormanhallinta, joka estää
suurten kuormien yhtäaikaisen käytön (esim. kiuas ja vedenlämmitin pois, kun liesi on päällä).
Kuormanhallinnan voisi tehdä omilla ESP32-PDM-moduuleilla ([current-system.md](../current-system.md#4-valvonta-verkot-ja-tehonjako)).
5 kW:n invertteri ottaa 24 V:n akustosta noin 230 A, mikä vaatii järeät kaapelit ja sulakkeet.

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
| Mastervolt Alpha 24/150 Evo ja Alpha Pro III -säädin | [Blue Bottle Marine](https://www.bluebottlemarine.com/products/mastervolt-alpha-24-150-evo-kit-c-w-alpha-pro-iii.html) | 1 476 € | säädin mukana |
| Mastervolt Alpha 24/150 MB | [Philippi, DE](https://www.philippi-online.de/en/?p=34174) | 2 420 € sis. ALV | säädin **⚠ tarkista**, onko mukana |
| Prestolite 24 V / 175 A | [SEIMI, FR](https://www.seimi-equipements-marine.com/en/electricity/alternators-regulators/alternators/prestolite-alternator-24-175-a/pdt_2563) | 1 304 € sis. ALV | ulkoinen säädin erikseen |
| DelStar 24 V / 200 A | [Bermantec](https://bermantec.com/shop/products/alternators-spare-parts/marine-alternators/delstar-alternator-24v-for-mastervolt-pad-mount-1170-20201/) | hinta ei näkyvissä; toisella myyjällä noin 4 600 USD | ainoa löydetty 24 V / 200 A |
| Ulkoinen säädin: Wakespeed WS500 | [invertersrus](https://invertersrus.com/product-category/inverter-brands/wakespeed/) | 650–820 USD | litiumille sopiva |
| Ulkoinen säädin: Balmar MC-618 | [eMarine](https://emarineinc.com/balmar-mc-618-ms-12v.html) | 367 USD (12 V:n versio) | 24 V:n versio **⚠ tarkista** |

Lisäksi tarvitaan kiinnike ja hihna CAT 3126B:n etupäähän, kaapelit ja sulake (hinta
**⚠ ei tiedossa**). 150–175 A:n laturi ottaa koneelta arviolta 5–7 kW, joten **tarkista, kestääkö
hihnaveto sen** (usein tarvitaan leveä moniurahihna).

**Johtopäätös [laskelma]:** 150–175 A riittää. 200 A:n laturi lyhentäisi täyden ankkurivuorokauden
latausta vain noin 2,8 tunnista 2,3 tuntiin, mutta 24 V:n 200 A:n laturit maksavat moninkertaisesti.
Laturi ja säädin maksavat noin **1 500–2 500 €** ilman kiinnikettä ja asennusta (**⚠ arvio**).

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
| Hinta | akusto ks. 2.4, laturi ks. 2.5, invertteri **⚠ ei tiedossa** | **⚠ ei tiedossa**, todennäköisesti kallein | **⚠ ei tiedossa** |

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

## 4. Suositus (ei päätös)

Akusto ja invertteri tarvitaan joka tapauksessa, koska jääkaappi käy ankkurissa myös yöllä, eikä
generaattoria haluta ajaa yöllä. **Akuston ja invertterin koko ratkeaa vasta, kun päätetään, mitkä
laitteet asennetaan ja ovatko ne sähköllä toimivia.** Alla olevat koot koskevat tilannetta, jossa
kaikki harkinnassa olevat laitteet asennetaan sähköisinä. Ratkaistava on lisäksi, riittääkö ajo
lataukseen vai tarvitaanko dieselgeneraattori.

1. **Vaihe 1: vaihtoehto A.** Toinen 24 V:n laturi (150–175 A, ks. kohta 2.5) pääkoneeseen, noin 5 kW:n invertteri
   tai kuormanhallinta, ja litiumakusto. Akuston koko riippuu ankkuripäivistä:
   - **noin 400 Ah**, jos saunotaan vain ajopäivinä tai satamassa maasähköllä;
   - **noin 650 Ah**, jos halutaan yksi täysi ankkurivuorokausi saunoineen ilman ajoa.

   Ajo lataa täyden vuorokauden kulutuksen noin 2,5 tunnissa. Iso akusto parantaa samalla ohjauksen
   2,5 kW:n sähköisen varapumpun käyttöaikaa ([current-system.md](../current-system.md#3-suuret-dc-kuormat)).
2. **Vaihe 2: noin 6 kVA:n dieselgeneraattori** paapuurin puolelle varattuun tilaan, jos ankkurissa
   ollaan usein yli vuorokausi ajamatta. Silloin akusto voi jäädä noin 400 Ah:iin. Pidä tila varattuna.
3. **Hydrauligeneraattoria ei suositella** Vegan tarpeeseen.
4. **Vedenlämmittimen 3 kW:n vastusta ei kannata käyttää akustolta.** Yksi tunti vie noin 3,3 kWh
   akustosta. Käytä sitä maasähköllä tai generaattorilla. Jos lämmittimessä on koneen
   jäähdytysvesikierukka, vesi lämpenee ajossa ilmaiseksi.

**Halvempia vaihtoehtoja**, jos akusto kasvaa liian kalliiksi: sähköruoanlaitto (noin 3 kWh/vrk) ja
kiuas (4,6 kWh/vrk) ovat suurimmat kuormat. Kaasu- tai dieselliesi ja puukiuas pienentäisivät
akuston noin kolmasosaan.

## 5. Avoimet kysymykset

- [x] Muut AC-kuormat: lista saatu [omistaja 2026-10-28], ks. [loads.yaml](../loads.yaml)
- [ ] Jääkaapin teho ja energiankulutus tyyppikilvestä; muiden laitteiden tehot, kun ne valitaan
- [ ] Onko vedenlämmittimessä koneen jäähdytysvesikierukka?
- [x] Mitkä laitteet ovat olemassa: vain jääkaappi [omistaja 2026-10-28]
- [ ] Mitkä harkinnassa olevista laitteista asennetaan, ja ovatko liesi, kiuas ja vedenlämmitin sähkökäyttöisiä vai esim. kaasu-, diesel- tai puulämmitteisiä?
- [ ] Kuinka monta vuorokautta ollaan tyypillisesti ankkurissa ajamatta?
- [ ] Onko maasähköä laiturissa?
- [ ] Nykyisten akkujen tyyppi ja kapasiteetti; mahtuuko konehuoneeseen 400–650 Ah:n litiumakusto
- [ ] Mahtuuko toinen laturi koneen etupäähän, millainen kiinnike tarvitaan, ja kestääkö hihnaveto 5–7 kW
- [ ] Hinnat vaihtoehdoille A ja B (akuston ja laturin hintataso haettu, ks. kohdat 2.4 ja 2.5; invertteri, kiinnike ja generaattori puuttuvat)
