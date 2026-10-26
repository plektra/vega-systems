# Apupiiri alusta alkaen: säätötilavuuspumppu, LS ja on/off-venttiilit

> **Tila:** ajatuskoe 2026-10-26, **ei päätetty**. Päätetty kokoonpano on yhä F1-61 tai vastaava
> ohitusventtiilillä ([p2-pump-options](p2-pump-options.md)). Tässä kysytään, miten apupiiri
> rakennettaisiin alusta alkaen säätötilavuuspumpulla **ilman proportionaalista venttiilipöytää**
> [omistaja 2026-10-26, kysymys]. Vertailukohdat: PVH57 olemassa olevilla venttiileillä
> ([p2-variable-pump](p2-variable-pump.md)) ja PVH57 proportionaalisella LS-lohkoventtiilillä
> ([aux-circuit-ls-clean-sheet](aux-circuit-ls-clean-sheet.md)).
>
> Luvut ovat arvioita, ellei toisin merkitä. Pätevän henkilön pitää tarkistaa kytkentä,
> säätöarvot ja erityisesti ankkurivinssin kuorman pito ennen rakentamista.

## Selkokielinen yhteenveto

- Rakenne on **kuormantunteva (LS) järjestelmä, jossa on tavalliset on/off-magneettiventtiilit.**
  Pumpun LS-signaali otetaan vaihtoventtiileillä suoraan kuormien A/B-linjoista.
- **Pumppu tietää itse, milloin sitä tarvitaan.** Kun mikään venttiili ei ole päällä, keskiasento
  yhdistää A- ja B-linjat säiliöön, LS-linja tyhjenee ja pumppu jää noin 20 barin valmiustilaan.
  LS-purkuventtiiliä (2/2), 3/2-valintaventtiiliä ja ohjelman ohjausjärjestystä ei tarvita.
- **Keulapotkurilinjassa ei ole kuristinta,** joten pumppu nousee suoraan 250 bariin ja työntövoima
  pysyy päätetyssä noin 85–88 %:ssa ([päätös 2026-10-21](../../decisions.md)).
- **Vinssi ja painepesuri saavat oman kompensoidun virtauksensäätönsä,** ja pumppu pitää paineen vain
  noin 20 bar kuorman yläpuolella. Öljyyn syntyy vähän lämpöä millä tahansa kierroksilla.
- **Kustannus on lähellä halvinta reittiä:** CETOP-pohjalaatta, BAV-713, VMP, letkut, säiliö ja
  jäähdytin käyvät tähän sellaisinaan. Portaatonta ohjausta ei saada.

## Kaavio

```
PTO ─ Spidex ─ PVH57 (LS-säädin, 250 bar) ──P──┬─ varaventtiili ~270 bar ──► T
        │   ▲                                  ├─ 1 keulapotkuri: FXDC ~36 l/min ─ 4/3 on/off, A,B→T keskellä ─► keula
        │   │                                  ├─ 2 vinssi:       FXDC (vinssin virtaus) ─ 4/3 on/off, A,B→T ─ jarruventtiili ─► moottori
        │   │                                  └─ 3 pesuri:       FXDC (pesurin virtaus) ─ on/off ─► moottori
        │   └── LS ◄── vaihtoventtiilit (suurin A/B-paine kaikista lohkoista) + vuotokuristin Ø0,8 ─► T
        └── kotelovuoto, oma letku öljypinnan alle ──► säiliö
```

Ohjauspiiri (P1, orbitroli) pysyy erillään kuten nyt ([päätös 2017-04](../../decisions.md)).

## Osat ja perustelut

| # | Osa | Tehtävä | Huom. |
|---|---|---|---|
| 1 | PVH57, LS-säädin, painekompensaattori 250 bar | Tuottaa vain sen, mitä kuormat ottavat; tyhjäkäynnillä noin 38 l/min [laskelma, ks. [p2-variable-pump](p2-variable-pump.md#sopivuus-vegaan-laskelma)] | Veto, kannake, 50 mm:n imu ja kotelovuoto kuten [p2-variable-pump](p2-variable-pump.md#tarvittavat-osat-pumpun-lisäksi-minimi) |
| 2 | 4/3 on/off -suuntaventtiilit, keskiasennossa A,B→T | Keskellä potkuri pyörii vapaasti, vinssin jarruventtiili sulkeutuu ja LS-linja tyhjenee | Keulapotkurille käy nykyinen BAV-713 |
| 3 | Vaihtoventtiilit A/B-linjoista ja lohkojen välillä LS-porttiin | Tuo suurimman kuorman paineen pumpun säätimelle | Pieniä linjamallisia vaihtoventtiileitä, malli **⚠ valitsematta** |
| 4 | Vuotokuristin noin Ø0,8 mm LS-linjasta säiliöön | Varmistaa, että LS-linja tyhjenee ja pumppu palaa valmiustilaan | |
| 5 | Kaksitiekompensoitu virtauksensäätö (Sun FXDC) lohkoittain | Keulapotkurilla vain ylikierrossuoja; vinssillä ja pesurilla pitää nopeuden vakiona myös yhtäaikaisessa käytössä | FXDC ja runko DAW/S, ks. [vaihtoehdot](p2-variable-pump.md#kaksitiekompensoidun-virtauksensäätöventtiilin-vaihtoehdot). Asennus välilaattana tai linjarunkona **⚠ tarkista** |
| 6 | Varaventtiili (nykyinen VMP) noin 270 bariin | Rajaa paineen, jos pumpun säädin jumittuu | Pätevä henkilö säätää |
| 7 | Vinssin jarruventtiili moottorilla ja vinssin oma jarru | Kuorman pito | Vinssin tiedot **⚠ ei tiedossa** ([loads.yaml](../loads.yaml)) |
| 8 | Jäähdytin termostaattiohituksella, paluusuodatin 10 µm | Mäntäpumppu vaatii puhtausluokan 17/15/13 | Ks. [oil-cooling](oil-cooling.md) |

**Miksi keulapotkurille ylikierrossuoja:** 250 barissa moottori ottaa itse noin 33 l/min
(interpoloitu Sleipnerin taulukosta [datalehti Side-Power SH Series v1.0.0 2017]), joten
virtausta ei tarvitse rajata normaalikäytössä. Jos potkuri imee ilmaa, sen kuorma katoaa, ja
suurilla kierroksilla pumppu antaisi sille paljon enemmän öljyä. FXDC noin 36 l/min estää
ryntäyksen ja aiheuttaa normaalikäytössä vain pienen painehäviön [arvio].

**Miksi vinssille ja pesurille kompensoitu virtauksensäätö eikä pelkkä kuristin:** kun keulapotkuri
pitää pumpun 250 barissa, matalan paineen kuorman kuristimen yli olisi suuri paine-ero. Se veisi
virtauksen potkurilta. FXDC pitää asetetun virtauksen paine-erosta riippumatta. Jos vinssiä ja
pesuria ei koskaan käytetä keulapotkurin kanssa yhtä aikaa, halvempi säädettävä kuristin riittää.

## Miten 250 bar ja 20 barin marginaali sopivat yhteen

PVH57:n säätimessä on kaksi karaa, jotka säätävät samaa iskunpituutta [M-2210-S s. 6, ks.
[p2-variable-pump](p2-variable-pump.md#miten-ls-linjaa-käytetään)]:

1. **LS-kara** yrittää pitää pumpun lähtöpaineen noin 20 bar LS-portin painetta korkeampana.
2. **Paineenrajoitin** pienentää iskua niin, ettei lähtöpaine ylitä 250 baria.

Pumppu tottelee sitä, joka vaatii pienempää tuottoa. **Pumpun paine on siis kuorman paine + 20 bar
tai 250 bar, kumpi on pienempi.**

- **LS-paine ei ole pumpun tuottama erillinen paine.** Se on mittaussignaali: kuorman oma paine,
  joka tuodaan vaihtoventtiileillä A- tai B-linjasta säätimelle. Mikään paine ei nouse 250 barin
  yli.
- **Keulapotkurilla:** täyteen työntöön tarvittaisiin 264 bar, joten LS-kara pyytäisi noin
  284 bar. Paineenrajoitin pysäyttää pumpun 250 bariin, ja pumppu säätää iskun juuri sille
  virtaukselle, jolla 250 bar säilyy (noin 33 l/min). Paine-ero pumpun ja moottorin välillä on
  silloin vain FXDC:n, BAV-713:n ja letkujen todellinen häviö, arviolta muutama bar
  (**⚠ ei mitattu**) [arvio].
- **Siksi keulapotkurilinjassa ei saa olla kuristinta.** Kuristinvaihtoehdossa
  ([p2-variable-pump](p2-variable-pump.md#vaihtoehto-aito-kuormantunto-säädettävällä-kuristimella))
  virtaus rajattiin kuristimella, joka tarvitsi 20 barin paine-eron, ja moottori sai vain noin
  230 bar (työntövoima noin 80 %).
- **Yhtäaikaisessa käytössä:** kun keulapotkuri pitää pumpun 250 barissa, vinssin FXDC:n yli on
  250 bar miinus vinssin paine, ja FXDC pitää vinssin nopeuden asetuksessa. Ongelma tulee vain, jos
  vinssikin tarvitsee lähes 250 baria. Silloin FXDC:n yli ei jää sen tarvitsemaa pienintä
  paine-eroa (**⚠ ei tiedossa**), ja vinssi hidastuu.

## Vertailu

| | PVH57 + vanhat venttiilit ([p2-variable-pump](p2-variable-pump.md)) | PVG-venttiilipöytä ([aux-circuit-ls-clean-sheet](aux-circuit-ls-clean-sheet.md)) | **LS + on/off (tämä)** |
|---|---|---|---|
| Ohjauslogiikka | 2/2 (ja 3/2) oikeassa järjestyksessä | PVE-ohjaimet | **ei mitään, pelkät kytkimet** |
| Vika "2/2 jää kiinni", noin 10 kW lämpöä | mahdollinen | ei | **ei** |
| Lämpö vinssillä | 3–11 kW ilman 3/2:ta | pieni | **pieni** |
| Keulapotkurin työntövoima | noin 85–88 % | noin 85–88 % (enemmän, jos paine nostetaan) | noin 85–88 % |
| Portaaton ohjaus | ei | kyllä | ei |
| Kustannus | pienin | suurin | lähellä pienintä |

**Poistuu nykysuunnitelmasta:** VPR3, OD15, BPV sekä PVH57-selvityksen 2/2- ja 3/2-ratkaisut.
**Säilyy:** CETOP-pohjalaatta, BAV-713, VMP, säiliö, 50 mm:n imu, Spidex ja kannake, letkut ja
jäähdytin. **Uutta:** kolme FXDC:tä runkoineen (FXDC noin 83–89 $ USA:ssa 2026-10-25,
valurautaisen DAW/S-rungon hinta **⚠ ei tiedossa**), muutama vaihtoventtiili, vuotokuristin ja
vinssin jarruventtiili.

## Vikatilat

| Vika | Mitä tapahtuu |
|---|---|
| Sähkökatko | Venttiilit palaavat keskelle, LS-linja tyhjenee ja pumppu menee valmiustilaan. Keulapotkuri pysähtyy ja pyörii vapaasti; vinssin jarru ja jarruventtiili pitävät. |
| Suuntaventtiili jumittuu auki | Kuorma jää käyntiin. Hätäpysäytys katkaisee kelojen virran; jos kara ei palaa, pumpun kierrokset tai imulinjan palloventtiili ovat ainoa keino **⚠ pätevä henkilö arvioi**. |
| LS-linjan vuotokuristin tukkeutuu | Pumppu voi jäädä venttiilien palattua keskelle hetkeksi korkeaan paineeseen; keskiasennon A,B→T-yhteys tyhjentää linjan silti. |
| Pumpun säädin jumittuu täydelle tuotolle | Varaventtiili rajaa paineen; tilanne vastaa kiinteää pumppua (lämpöä), ja lämpötila-anturi hälyttää. |
| Kotelovuotolinja tukkeutuu | Akselitiiviste voi vaurioitua; siksi vuotolinja on oma letkunsa. |
| Vinssi kuormassa ja hydrauliikka menetetään | Jarruventtiili ja vinssin jarru pitävät kuorman, ei pumppu eikä venttiilin kara. **Pätevä henkilö tarkistaa ennen rakentamista.** |

## Avoimet kysymykset

- [ ] Salhydro: Sun FXDC:n pienin paine-ero, jolla se vielä pitää asetusvirtauksen (vinssi ja pesuri saavat vain noin 20 bar)
- [ ] Lohkokohtaisen FXDC:n asennus CETOP-pohjalaatalle: välilaatta (malli) vai linjarunko kunkin aseman letkuun
- [ ] Danfoss: PVH57:n kierrosraja (2400 rpm) yhtäaikaisessa käytössä, kun 38 l/min ei riitä kahdelle kuormalle tyhjäkäynnillä
- [ ] Sleipner: SH240:n suurin sallittu virtaus ylikierrossuojan asetusta varten
- [ ] Vaihtoventtiilien malli ja liitäntäkoko
- [ ] Ankkurivinssin moottori, jarru ja jarruventtiili; painepesurin hydraulimoottorin virtaus ja paine ([loads.yaml](../loads.yaml))
