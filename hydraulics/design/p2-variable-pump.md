# P2 säätötilavuuspumppuna: Vickers PVH57 ja LS-ohjaus

> **Tila:** selvitys 2026-10-25, korjattu 2026-10-25 (VPR3:n B-porttia ei saa tulpata), **ei päätetty**. Päätetty kokoonpano on yhä F1-61 tai vastaava
> ohitusventtiilillä ([p2-pump-options](p2-pump-options.md)). Tässä arvioidaan, sopisiko
> käytetty Vickers PVH57 -säätötilavuuspumppu P2:ksi, ja mitä se vaatisi.
> Pätevän henkilön pitää tarkistaa säätöarvot, LS-kytkentä, kannake ja ohjauslogiikka ennen
> rakentamista.

## Selkokielinen yhteenveto

**Ongelma, joka halutaan ratkaista.** Nykyinen suunnitelma (Parker F1-61) on *kiinteätilavuuksinen*
pumppu: se tuottaa aina kierroksia vastaavan määrän öljyä (700 rpm:llä noin 38 l/min, 1800 rpm:llä
noin 102 l/min). Keulapotkuri tarvitsee noin 34 l/min. Ylimäärä on pakko päästää säiliöön:

- *Kun keulapotkuria ei käytetä,* ohitusventtiili (BPV) kierrättää koko tuoton matalalla
  paineella. Lämpöä syntyy vähän.
- *Kun keulapotkuria käytetään korkeilla kierroksilla,* VPR3 päästää potkurille 35 l/min ja
  laskee loput säiliöön lähes täydessä paineessa. 1800 rpm:llä tämä on noin 38 kW lämpöä
  [laskelma, ks. [p2-pump-options](p2-pump-options.md#käyttäytyminen-eri-kierroksilla-parker-f1-061)].

**Mitä PVH57 tekee toisin.** Säätötilavuuspumppu pienentää itse iskuaan, joten se tuottaa vain sen
öljyn, joka menee läpi. Ylimäärää ei synny, eikä sitä tarvitse kuristaa lämmöksi.

**Miten pumppua ohjataan.** Pumpussa on pieni ohjausliitäntä, LS-portti. Sitä voi ajatella
pumpun "ohjauslankana":

| Tila | Mitä tehdään | Mitä pumppu tekee |
|---|---|---|
| Lepo (myös sähkökatko) | pieni 2/2-magneettiventtiili on jännitteetön ja auki, LS-portti on yhteydessä säiliöön | pyörii noin 20 barissa lähes ilman tuottoa; lämpöä vähän |
| Keulapotkuri käytössä | 2/2 saa jännitteen ja sulkeutuu, sitten BAV-713 ohjataan suuntaan | nostaa paineen 250 bariin; uusi kaksitie-virtauksensäätöventtiili päästää potkurille noin 34 l/min, ja pumppu tuottaa vain sen verran |

Lämpöä syntyy keulapotkuria käytettäessä arviolta 2–3 kW 38 kW:n sijaan [laskelma, ks. alla].

**Mikä muuttuu piirissä:**

- **VPR3 poistetaan.** Kolmitieventtiilinä se laskee ylimäärän B-portista säiliöön, ja silloin
  pumppu ajaa täydellä tuotolla matalassa paineessa. B-porttia ei myöskään saa tulpata (ks.
  [VPR3:n portit](#vpr3n-portit-ja-miksi-se-ei-kelpaa)). Tilalle tulee kaksitie-virtauksensäätöventtiili
  (esim. Sun FXDC), jossa ei ole ylimääräporttia lainkaan.
- **OD15-vapaakiertoventtiili poistetaan.** Sen tehtävän (paine pohjalaatalle päälle ja pois)
  hoitaa LS-linjan pieni 2/2-magneettiventtiili.
- **Uudet osat:** SAE C -kannake, toinen kytkinnapa (1,25":n kiila-akseli), kotelovuotoletku
  säiliöön, 2/2-magneettiventtiili ja kuristin LS-linjaan.
- **Ennallaan:** CETOP-pohjalaatta, BAV-713, VMP, letkut, säiliö, suodatin ja jäähdytin.

**Hinta ja tila:** pumppu 190 €, mutta kannake, napa, liittimet ja FXDC tulevat lisäksi (ks.
[kustannusvertailu](#kustannusvertailu-arvio)). Mitään ei ole päätetty. F1-61 ohitusventtiilillä on
edelleen voimassa oleva suunnitelma.

## Ehdokas: Vickers PVH57C-LAF-1S-10-C12V-31 (tori.fi)

Ilmoitus: <https://www.tori.fi/recommerce/forsale/item/45217879>, **190 € tai tarjous** (tarkistettu
2026-10-25). Ilmoituksen teksti: *"Käyttämätön Vickers säätötilavuuspumppu. 57 cm3,
pyörimisuunta vastapäivään. Pumpun perään voidaan kytkeä toinen pumppu."*

- **Tyyppikilpi** (ilmoituksen kuvasta): Model Code `PVH57C LAF 1S 10 C12V 31`, Part No.
  **02-159964**, Made in U.S.A.
- **Kunto kuvien perusteella:** maalattu uudelleen tai kauttaaltaan (maalia kilven reunoilla ja
  pulttien kannoissa), ruostepilkkuja säädinlohkossa ja rungossa. Portit tulpattu. Akselissa ja
  tiivistepinnoissa ei näy vaurioita. "Käyttämätön" voi tarkoittaa varastossa ollutta tai
  kunnostettua. **⚠ Kysy alkuperä, varastointiaika ja pyöriikö akseli käsin tasaisesti.**

### Tyyppikoodi

Lähde: Vickersin huolto-ohje *M-2210-S, PVH Piston Pumps Including Controls* (rev. 2/93), s. 3
([PDF](https://hydraulicsonline.com/wp-content/uploads/2019/12/Eaton-Vickers-PVH-Series.pdf), luettu
tekstinä).

| Osa | Merkitys |
|---|---|
| PVH **57** | Suurin kierrostilavuus **57,4 cm³** |
| **C** | SAE C -nelireikälaippa (SAE J744-127-4); mobiiliversio (teollisuusversiossa QI) |
| **L** | **Vasen eli vastapäivään** akselin päästä katsottuna → **sopii Vegaan** ([vessel: Pyörimissuunnat](../../vessel/README.md#pyörimissuunnat)) |
| **A** | Läpivetopumppu, takana SAE A -laippa toiselle pumpulle |
| **F** | Pääliitännät SAE-nelireikälaipoilla |
| **1** | SAE C -suora akseli kiilalla, Ø 1,25" = 31,75 mm (J744-32-1) |
| **S** | Yksinkertainen akselitiiviste |
| **10** | Rakennenumero |
| **C** | Paineenrajoittimen säätöalue 70–250 bar |
| **12** | Tehdasasetus **120 bar** |
| **V** | Kuormantunto (LS), paine-ero 20 bar (säädettävissä 17–30 bar) |
| **31** | Säätimen rakennenumero |

### Tekniset tiedot

Lähde: Eatonin luettelo *Industrial & Mobile Variable Displacement Piston Pumps* V-PUPI-TM008-E1
(10/2013) ([PDF](https://www.appliedfluidpower.com/media/wysiwyg/PDFs/PVH_Series.pdf), skannattu,
s. 7, 8 ja 31 luettu kuvina). Pumppu on **mobiiliversio**: teollisuusversiossa on aina lisäkoodi
Q250 tai Q140, eikä tässä koodissa ole lisäkoodia.

| Kohde | Arvo | Lähde |
|---|---|---|
| Kierrostilavuus | 57,4 cm³ | luettelo s. 7 |
| Nimellispaine | 250 bar (LS-järjestelmässä paineenrajoitin voi olla 280 bar) | s. 7 |
| **Suurin kierrosluku, mobiili** | **2000 rpm** imupaineella −0,17 bar (127 mm Hg), **2400 rpm** imupaineella 0 bar, **3000 rpm** imupaineella +0,48 bar | s. 7 |
| Suurin kierrosluku, teollisuus (vertailu) | 1500 / 1800 / 1800 rpm | s. 7 |
| Tuotto 250 barissa ja 2400 rpm:llä | 134 l/min (mobiili) | s. 7 |
| Teho paineenrajoituksella, nollatuotto | noin 10 kW 1800 rpm:llä ja 250 barissa (luettu kuvaajasta *Input power, cutoff* karkeasti) **⚠ tarkista** | s. 8 |
| Öljy | viskositeetti 16–40 cSt optimi, kylmäkäynnistys ≤ 5000 cSt, hetkellisesti ≤ 104 °C | s. 31 |
| Puhtaus (säätötilavuuksinen mäntäpumppu) | 18/16/14 (≤ 140 bar), **17/15/13 (140–210 bar)**, 16/14/12 (yli 210 bar) | s. 31 |
| Asennus | vaakaan, suora veto joustavalla kytkimellä; linjaus asennuspiirustuksen toleransseihin | s. 31 |
| Paino | noin 36 kg (jälleenmyyjät) **⚠ tarkista** | jälleenmyyjät |
| Imuaukko | 2 1/2" SAE-laippa (jälleenmyyjät) **⚠ tarkista pumpusta** | jälleenmyyjät |
| Kotelovuoto | pakollinen vuotolinja säiliöön | M-2210-S |

### Sopivuus Vegaan [laskelma]

Oletukset: volumetrinen hyötysuhde 95 %, mekaaninen 90 %, tyhjäkäynti 700 rpm.

| Tarkistus | Tulos |
|---|---|
| Tuotto 700 rpm:llä | noin 38 l/min, enemmän kuin keulapotkurin 33,8 l/min ✅ |
| Momentti 250 barissa | noin 254 Nm; PTO noin 420 Nm ✅; Spidex 98 Sh A (525 Nm) riittää (tarve kertoimilla noin 430 Nm) ✅ |
| Pyörimissuunta | L ✅ |
| Kierrosluku | koneen 2400 rpm on tasan mobiiliversion rajalla, kun imupaine on vähintään 0 bar. Säiliö on noin 1 m pumpun yläpuolella ja imulinja 50 mm. Täydellä iskulla 2400 rpm:llä (noin 138 l/min) imupaine olisi kylmällä öljyllä arviolta 0…−0,03 bar. **Vegan käytössä täyttä iskua ei tule korkeilla kierroksilla**: ajossa pumppu on valmiustilassa ja keulapotkuria käytettäessä virtaus on rajattu noin 35 l/minuun. Luettelo ei kerro, saako pienemmällä iskulla pyöriä nopeammin **⚠ kysy Danfossilta**. |
| Laippa ja akseli | SAE C ja kiila-akseli: **ei ISO 7653 eikä 8×32×36**, joten kannake ja Spidexin pumppunapa ovat eri kuin F1-suunnitelmassa |
| Paino | noin 36 kg (F1-61 8,5 kg): kannake mitoitetaan uudelleen |

## Miten LS-linjaa käytetään

C**V-säädin pitää pumpun lähtöpaineen noin 20 bar LS-portin painetta korkeampana, ja paineenrajoitin
kääntää pumpun nollatuotolle asetuspaineessa. Huolto-ohjeen mukaan LS-linjaa voi käyttää pumpun
etäohjaukseen ja purkuun [M-2210-S s. 6].

### VPR3:n portit ja miksi se ei kelpaa

Marchesini VPR3 [datalehti VPR3]: **E** = tulo pumpulta, **P** = säädetty prioriteettivirtaus
toimilaitteelle (käsipyörä), **B** = ylimäärä. Datalehden kytkentäohje: *"Connect B to the tank or
to a second actuator"* eli B kytketään aina säiliöön tai toiselle toimilaitteelle
([Salhydro, VPR3-2015](https://www.salhydro.fi/files/PDF/VPR3-2015.pdf)). **B-porttia ei saa
tulpata** [omistaja 2026-10-25]; datalehti ei anna tulppausta käyttötavaksi. Siksi:

- **B säiliöön:** ylimäärä valuu matalassa paineessa, pumppu ei saavuta paineenrajoittimen asetusta
  ja ajaa täydellä tuotolla. Korkeilla kierroksilla tulisi sama lämpö kuin F1-61:llä.
- **B toiselle toimilaitteelle:** Vegassa ei ole toista kuluttajaa, jolle ylimäärä voisi mennä.
- **B tulpattuna** (ei sallittu): vaikka E→P näyttää kaaviossa pelkältä kuristimelta, se ei
  rajoittaisi virtausta itse, eikä käsipyörän asetusta ole kalibroitu tähän käyttöön.

**VPR3 ei siis sovi PVH57:n kanssa millään kytkennällä,** ja se korvataan kaksitieventtiilillä.

### Suositus: kaksitiekompensoitu virtauksensäätö ja LS-purku

```
PTO ─ Spidex ─ PVH57 ─ 2-tie kompensoitu virtauksensäätö ~34 l/min ─ CETOP P (VMP) ─ BAV-713 ─ keulapotkuri
                │  │
                │  └─ LS-portti ─┬─ kuristin Ø0,8 ─ pumpun lähtö
                │                └─ 2/2-magneettiventtiili (NO) ─ säiliö
                └─ kotelovuoto ─ oma letku säiliöön öljypinnan alle
```

- **2/2 jännitteetön (auki):** LS-portti on yhteydessä säiliöön, ja pumppu on noin 20 barin
  valmiustilassa lähes nollatuotolla. Sama tila syntyy sähkökatkossa.
- **2/2 jännitteellinen (kiinni):** LS saa paineen pumpun lähdöstä kuristimen kautta, ja pumppu
  toimii painekompensoituna 250 barissa. Kaksitieventtiili rajaa virtauksen noin 34 l/minuun
  kuorman paineesta ja kierroksista riippumatta.
- **Työntövoima** pysyy arviolta 85–88 %:ssa, koska moottori saa 250 bar miinus venttiilin pienin
  painehäviö (tyypillisesti muutama bar) [arvio].
- **Lämpö keulapotkurin käytössä 1800 rpm:llä** on arviolta 2–3 kW (35 l/min × (250 − kuorman paine),
  kun kuorma on noin 200 bar). F1-61:llä se on noin 38 kW, ks.
  [p2-pump-options](p2-pump-options.md#käyttäytyminen-eri-kierroksilla-parker-f1-061) [laskelma].
- **Ohjausjärjestys:** 2/2 kiinni → BAV-713 suunta. Pois: BAV-713 keskelle → 2/2 auki. **2/2:n
  pitää olla auki aina, kun BAV-713 on keskellä.** Muuten pumppu seisoo 250 barissa nollatuotolla,
  mikä kuluttaa luettelon kuvaajan mukaan noin 10 kW.

### Vaihtoehto: aito kuormantunto säädettävällä kuristimella

> **Korjattu 2026-10-25:** aiempi versio ehdotti VPR3:n B-portin tulppaamista. Se ei ole sallittua
> (ks. yllä), joten vaihtoehto toteutetaan erillisellä kaksiporttisella kuristimella VPR3:n tilalla.

VPR3:n tilalle asennetaan säädettävä kaksiporttinen kuristin (neulaventtiili, esim. Marchesini
VRFB **⚠ tarkista koko ja painearvo**), ja LS-signaali otetaan kuristimen jälkeen pohjalaatan
P-linjasta (esim. mittariliitäntä G 1/4") Ø0,8 mm:n kuristimen kautta. Pumppu pitää kuristimen yli
20 barin paine-eron, joten virtaus pysyy vakiona: **pumppu hoitaa painekompensoinnin**, joten
kuristin ei tarvitse omaa kompensaattoria. Kuristin säädetään niin, että virtaus on noin 34 l/min
20 barin paine-erolla. LS-linjaan tarvitaan silti 2/2-purkuventtiili, jotta pumppu lepää, kun
BAV-713 on keskellä.

- **Plussat:** halvempi kuin FXDC; pienimmät häviöt osakuormalla (esim. vinssi).
- **Miinus:** 17–20 bar paineenrajoittimen 250 barista kuluu säätövaraan, ja moottori saa enintään
  noin 230 bar. **Työntövoima arviolta noin 80 %** (noin 4 % / 10 bar aiemman taulukon perusteella),
  mikä alittaa hyväksytyn noin 90 %:n kompromissin. C-jousen yläraja on 250 bar.

### Kaksitiekompensoidun virtauksensäätöventtiilin vaihtoehdot

| Venttiili | Tiedot | Huom. |
|---|---|---|
| **Sun Hydraulics FXDC** (korvaa FXDA:n) | 2-porttinen, kiinteä kuristin, painekompensoitu; 45 l/min, sarja 2, pesä T-5A, **350 bar**; asetus valitaan valmiista vaihtoehdoista, `L`/`K` antaa ±25 %:n hienosäädön; tehdasasetus ±10 % (`L`, `K`) tai ±15 % (`X`) [Sunin tuotesivu](https://www.sunhydraulics.com/model/FXDC) | **Suositus.** Tarvitsee 3/4":n linjarungon T-5A-pesälle. Toimittaja Salhydro (Suomi). **⚠ Kysy, mikä asetusvaihtoehto kattaa 34 l/min.** |
| Hansa-Flex HK V270 5 - 3/4 | 2-tie, painekompensoitu, G 3/4", 15–80 l/min säädettävä, **250 bar** [Hansa-Flex](https://shop.hansa-flex.com/en_GB/es_ES/componentes-hidr%C3%A1ulicos/v%C3%A1lvulas/flow-control-valves/flow-control-valves-for-pipeline-installation/hk-v270-5---3-4/p/HKV2705-3-4) | Yksinkertaisin asentaa, mutta painearvo on tasan pumpun asetuksessa, eikä VMP:tä voi asettaa yläpuolelle venttiilin arvoa ylittämättä |
| Bosch Rexroth 2FRM 10-3X/50L | 2-tie, painekompensoitu, enintään 50 l/min, 315 bar, NG10-alilaatta (ISO 6263) [jälleenmyyjä](https://hydraulicpartsusa.com/products/bosch-rexroth/2f-flow-control-valves/2FRM10-3X50LB) | Vaatii erillisen NG10-alilaatan |

**Ei sovi:** Sun FRDA (prioriteettiportti enintään 210 bar), Marchesini VPR3 / RFP3 (kolmitie,
B-portti pakko kytkeä, ks. yllä), Rexroth 2FRM 6 (enintään 32 l/min). Marchesini VRFB ei käy
suositusratkaisuun, koska siinä ei ole painekompensointia; kuormantuntovaihtoehdossa se käy, koska
pumppu kompensoi.

## Tarvittavat osat pumpun lisäksi (minimi)

Olemassa olevat osat säilyvät: CETOP-pohjalaatta, VMP, BAV-713, letkut, säiliö, suodatin, jäähdytin.

| # | Osa | Huom. |
|---|---|---|
| 1 | Spidex 48/60 PTO-napa (48 H7 + kiila) ja hammaskehä 98 Sh A | sama kuin F1-suunnitelmassa |
| 2 | Spidex/Rotex 48 -pumppunapa 1,25":n (31,75 mm) kiilareiällä | vakio-osana tuumareiällä tai esiporattuna ja sorvattuna **⚠ tarkista saatavuus** |
| 3 | Kannake SAE C -nelireikälaipalle | pumppu noin 36 kg; mitat asennuspiirustuksesta (Eaton M-2206-S) **⚠** |
| 4 | Imuliitin: SAE-laippa, O-rengas, pultit ja supistus 50 mm:n letkuun | laipan koko pumpusta **⚠** |
| 5 | Painelähdön SAE-laippa ja liitin 3/4":n painelinjaan | koko pumpusta **⚠** |
| 6 | Kotelovuotolinja (vähintään noin 1/2") ylimmästä vuotoportista säiliöön öljypinnan alle | korvaa BPV:n vuotolinjan |
| 7 | 2/2-magneettiventtiili, auki jännitteettömänä, suoraan toimiva, 24 V | LS-purku; ainoa uusi magneettiventtiili |
| 8 | Kuristin noin Ø0,8 mm, T-haara ja 1/4":n letkut LS-linjaan | |
| 9 | Kaksitiekompensoitu virtauksensäätöventtiili noin 34 l/min (esim. Sun FXDC linjarungossa) | VPR3:n tilalle |

**Poistuu tai muuttuu:**
- **VPR3 poistetaan** (B-porttia ei saa tulpata, ks. [VPR3:n portit](#vpr3n-portit-ja-miksi-se-ei-kelpaa)).
- **Rexroth OD15 -vapaakiertoventtiili poistetaan.** Jännitteettömänä se on auki säiliöön. Jos LS:n
  2/2 on samaan aikaan kiinni, pumppu nostaa paineen 250 bariin ja virtauksensäätöventtiilin
  34 l/min valuu OD15:n kautta säiliöön lähes koko paineella (arviolta 34 l/min × 250 bar ≈ 14 kW
  lämpöä) [laskelma]. Sen tehtävän hoitaa LS:n 2/2. OD15 on esiohjattu (2–70 l/min), joten se ei
  luultavasti sovi itse LS-linjan pieneen virtaukseen.
- **Ei tarvita:** BPV-F1 (noin 430 € + ALV), Parkerin Ø50-imuliitin eikä 8×32×36-uritettu napa.
- **Säädöt:** paineenrajoitin 120 → 250 bar pumpun säätöruuvista (mittari 2G1); VMP
  varaventtiiliksi paineenrajoittimen yläpuolelle, esim. noin 270 bariin (pätevä henkilö
  hyväksyy); kotelo täytetään öljyllä ennen ensimmäistä käynnistystä.

## Vikatilat

- **Kela tai sähkö pettää:** LS on yhteydessä säiliöön, pumppu on valmiustilassa ja keulapotkuri
  ei toimi. Tilanne on turvallinen.
- **2/2 juuttuu kiinni BAV-713:n ollessa keskellä:** pumppu seisoo 250 barissa nollatuotolla,
  ja öljyyn menee arviolta noin 10 kW 1800 rpm:llä. Öljyn lämpötila- ja paineanturi havaitsevat
  tämän.
- **Paineenrajoitin jumittuu täydelle tuotolle:** VMP rajoittaa paineen, ja tilanne on sama kuin
  vakiotilavuuspumpulla (lämpöä).
- **Kotelovuotolinja tukkeutuu:** akselitiiviste voi vaurioitua. Linja viedään omana letkunaan
  säiliöön, ei yhteiseen paluulinjaan.

## Kustannusvertailu (arvio)

| | F1-61-reitti | PVH57-reitti |
|---|---|---|
| Pumppu | käytetty 100–300 € | 190 € (tori.fi) |
| Tyhjäkierto | BPV-F1 noin 430 € + ALV | 2/2-magneettiventtiili ja kuristin, arviolta 100–200 € |
| Virtauksen rajoitus | VPR3 (olemassa) | Sun FXDC ja linjarunko **⚠ hinta ei tiedossa** |
| Kytkimen pumppunapa | 8×32×36-uritettu, noin 134 € | 1,25":n kiilareikä **⚠** |
| Muuta | – | SAE-laippaliittimet, vuotoletku, järeämpi kannake, mahdollisesti tiivistesarja |

## Avoimet kysymykset

- [ ] Myyjältä: alkuperä, varastointiaika, kunnostettu vai ei, pyöriikö akseli käsin tasaisesti, onko säädin koskematon (tehdasasetus 120 bar)
- [ ] Danfoss (Vickers): saako PVH57-mobiilia pyörittää yli 2400 rpm pienemmällä iskulla; valmiustilan häviöteho; kotelon suurin paine
- [ ] Eaton M-2206-S (PVH57:n asennuspiirustus): laipan mitat, imu-, paine- ja vuotoporttien koot ja paikat
- [ ] Salhydro: Sun FXDC:n asetusvaihtoehto 34 l/min:lle ja 3/4":n linjarunko T-5A-pesälle, hinta
- [ ] Spidex/Rotex 48 -napa 1,25":n kiilareiällä: saatavuus ja hinta
- [ ] Paluusuodattimen suodatusaste vs. 17/15/13
- [x] Voiko VPR3:n B-portin tulpata: **ei**, B kytketään aina säiliöön tai toiselle toimilaitteelle [omistaja 2026-10-25], [datalehti VPR3]
- [ ] Omistajat: PVH57 vai F1-61 tai vastaava ohitusventtiilillä
