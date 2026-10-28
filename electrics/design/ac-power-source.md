# AC-sähkön lähde: hydrauligeneraattori, dieselgeneraattori vai akusto ja invertteri

> **Tila:** Selvitys, aloitettu 2026-10-28. Ei päätöstä. Hinnat puuttuvat; ne tarkistetaan
> tarjouksista ennen päätöstä.

## 1. Tarve

| Kohde | Arvo | Lähde |
|---|---|---|
| Milloin AC-sähköä tarvitaan | Ajossa ja ankkurissa | [omistaja 2026-10-28] |
| Generaattori | Ei asennettu; tila varattu konehuoneen paapuurin puolelle | [omistaja 2026-10-28], [blogi 2017-04-19] |
| Suurin ankkurissa käytettävä laite | Sähkökiuas 2,3 kW, päällä kerrallaan noin 2 h | [omistaja 2026-10-28] |
| Muut AC-kuormat | **⚠ ei tiedossa** | |
| Maasähkö | **⚠ ei tiedossa** | |
| Kuinka monta vuorokautta ankkurissa ilman ajoa | **⚠ ei tiedossa** | |
| DC-jännite | 24 V | [vessel/README.md](../../vessel/README.md#sähköjärjestelmän-perustiedot) |

Kokonaistarve on alle 10 kVA. Kiuas on suurin yksittäinen kuorma, ja se mitoittaa ankkuriajan
energiatarpeen.

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
| Ehdotettu akusto | **noin 300–400 Ah 24 V LiFePO4** (≈ 7–10 kWh), jotta muillekin kuormille jää varaa |
| Invertteri | jatkuva teho **vähintään 3 kW** (kiuas ja pieni marginaali) |

### Lataus ajossa [laskelma]

Oletus: laturi antaa lämpimänä noin 75 % nimellisvirrastaan 28 V:n latausjännitteellä (**⚠ arvio**).

| Laturit | Latausteho (arvio) | Kiukaan energian (5,1 kWh) palautus |
|---|---|---|
| Nykyinen 65 A | ≈ 1,4 kW | ≈ 3,7 h ajoa |
| Nykyinen 65 A ja toinen 150 A | ≈ 4,5 kW | ≈ 1,1 h ajoa |
| Nykyinen 65 A ja toinen 200 A | ≈ 5,6 kW | ≈ 0,9 h ajoa |

Litiumakusto vaatii latureille sopivan latauksensäädön (ulkoinen säädin tai DC-DC-laturi) ja
laturin lämpötilan valvonnan, koska litium ottaa virtaa vastaan täydellä teholla pitkään.

## 3. Vaihtoehdot

| | A. Laturi, akusto ja invertteri | B. Dieselgeneraattori | C. Hydrauligeneraattori |
|---|---|---|---|
| Sähköä ajossa | ✅ | ✅ | ✅ |
| Kiuas ankkurissa | ✅ yksi saunavuoro latausta kohden | ✅ rajoittamatta | ❌ vaatii pääkoneen käymään |
| Monta päivää ankkurissa ilman ajoa | ❌ akusto loppuu | ✅ | ❌ |
| Käyttää olemassa olevia osia | osittain: 24 V:n järjestelmä | ❌ | ✅ PVH57 (P2) |
| Asennus | laturin kiinnike, kaapelit, akusto, invertteri | polttoaine-, pakokaasu- ja merivesiputket, ilmanvaihto, äänieristys | letkut, venttiili, generaattori |
| Melu ankkurissa | ei | kyllä | pääkone käy |
| Huolto | vähäinen | oma kone huollettavaksi | vähäinen |
| Hinta | **⚠ ei tiedossa** | **⚠ ei tiedossa**, todennäköisesti kallein | **⚠ ei tiedossa** |

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

Ainoa vaihtoehto, joka antaa kiukaalle sähköä rajoittamatta useana päivänä ilman ajoa. Kiukaalle
ja pienille kuormille riittäisi noin 4–6 kVA:n kone (**⚠ arvio**). Tila on valmiina, mutta
asennus vaatii oman polttoaine-, pakokaasu- ja merivesijärjestelmän.

## 4. Suositus (ei päätös)

1. **Vaihe 1: vaihtoehto A.** Toinen 24 V:n laturi (150–200 A) pääkoneeseen, noin 300–400 Ah:n
   LiFePO4-akusto ja vähintään 3 kW:n invertteri. Yksi saunavuoro ankkurissa onnistuu, ja noin tunnin
   ajo lataa sen takaisin. Iso akusto parantaa samalla ohjauksen 2,5 kW:n sähköisen varapumpun
   käyttöaikaa ([current-system.md](../current-system.md#3-suuret-dc-kuormat)), jota nykyinen
   65 A:n laturi ei jaksa syöttää.
2. **Vaihe 2 tarvittaessa: pieni dieselgeneraattori** paapuurin puolelle varattuun tilaan, jos
   ankkurissa ollaan usein monta vuorokautta ajamatta. Pidä tila varattuna.
3. **Hydrauligeneraattoria ei suositella** Vegan tarpeeseen.

Halvin tapa lämmittää sauna on puukiuas, joka ei kuormita sähköjärjestelmää lainkaan. Se kannattaa
huomioida, jos sähkökiuas ei ole jo päätetty.

## 5. Avoimet kysymykset

- [ ] Muut AC-kuormat ankkurissa ja ajossa (liesi, vedenlämmitin, jääkaappi, työkalut)
- [ ] Kuinka monta vuorokautta ollaan tyypillisesti ankkurissa ajamatta?
- [ ] Onko maasähköä laiturissa?
- [ ] Nykyisten akkujen tyyppi ja kapasiteetti; mahtuuko konehuoneeseen 300–400 Ah:n litiumakusto
- [ ] Mahtuuko toinen laturi koneen etupäähän, ja millainen kiinnike tarvitaan
- [ ] Hinnat vaihtoehdoille A ja B
