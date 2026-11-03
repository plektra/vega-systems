# Arkisto: PVG 32 -apupiiri ennen ostoa (ajatuskoe, suositus ja hinta-arvio)

> **🗄 Arkistoitu 2026-11-03.** Siirretty tiedostosta
> [aux-circuit-ls-clean-sheet.md](../aux-circuit-ls-clean-sheet.md), kun PVG 32 oli valittu
> (2026-10-27), ostettu (2026-11-02) ja vastaanotettu (2026-11-03). Tässä ovat alkuperäinen tilarivi,
> ajatuskokeen yhteenveto, vertailu silloiseen suunnitelmaan, kustannukset, suositus ja ennen
> tarjousta tehty arvio. Teksti on sellaisenaan, eikä sitä päivitetä.

## Alkuperäinen otsikko ja tila

# Apupiiri alusta alkaen: säätötilavuuspumppu ja proportionaalinen LS-lohkoventtiili

> **Tila:** **PÄÄTETTY YKKÖSVAIHTOEHTO 2026-10-27:** apupiiri rakennetaan PVH57:llä ja käytetyllä Danfoss PVG 32:lla
> ([Ehdokas](../aux-circuit-ls-clean-sheet.md#ostettu-venttiili-danfoss-pvg-32-5-lohkoa-torifi)); **ostettu 2026-11-02, 200 € + rahti 39,90 €** [omistaja 2026-11-02]; **saapui 2026-11-03**, rungon merkinnät luettu ([Vastaanotto](../aux-circuit-ls-clean-sheet.md#vastaanotto-2026-11-03-rungon-merkinnät)); **koodit tulkittu 2026-11-03 ohjeesta 520L0344: peruslohkoissa 157B6200 ei ole isku-/imuventtiilien paikkoja eikä LS A/B -rajoittimia** ([Mitä koodit kertovat](../aux-circuit-ls-clean-sheet.md#mitä-koodit-kertovat-2026-11-03)). **Kaikkien viiden lohkon karat liikkuvat käsin vapaasti molempiin suuntiin ja palaavat jousella keskelle** [omistaja 2026-11-03]. Varavaihtoehdot: [LS + on/off](aux-circuit-ls-onoff.md)
> ja [FXDC + LS-purku](p2-fxdc-ls-unloading.md#suositus-kaksitiekompensoitu-virtauksensäätö-ja-ls-purku). Ajatuskoe 2026-10-25, päivitetty 2026-10-26 ja 2026-10-27
> (PVG 32 -ehdokas, tarjous, puhdistus, paino). Pumppu PVH57 päätetty 2026-10-27 (F1-61
> [arkistoitu](p2-pump-options.md)). PVH57:n käyttö olemassa olevien
> venttiilien kanssa on selvitetty tiedostossa [p2-variable-pump](../p2-variable-pump.md). Tässä
> kysytään, miten apupiiri rakennettaisiin, jos olemassa olevia venttiileitä ei tarvitsisi käyttää
> uudelleen [omistaja 2026-10-25, kysymys].
> Sama ilman proportionaalista venttiilipöytää, on/off-venttiileillä: [aux-circuit-ls-onoff](aux-circuit-ls-onoff.md).
>
> PVG 32:n arvot on 2026-10-26 tarkistettu Danfossin teknisestä ohjeesta 520L0344 (ks.
> [Ehdokas](../aux-circuit-ls-clean-sheet.md#ostettu-venttiili-danfoss-pvg-32-5-lohkoa-torifi)); muut lohkoventtiilin arvot ovat yleistietoa (**⚠ tarkista**). Pätevän
> henkilön pitää tarkistaa kytkentä, säätöarvot ja erityisesti ankkurivinssin kuorman pito ennen
> rakentamista.


## Selkokielinen yhteenveto

- Nykyinen rakenne (pumppu → virtauksensäätö VPR3 → vapaakiertoventtiili → CETOP-pohjalaatta →
  on/off-venttiilit) on tehty **kiinteälle pumpulle**. Säätötilavuuspumpulle luonteva rakenne on
  **kuormantunteva (LS) järjestelmä**, jossa pumppu ja venttiilit on tehty toimimaan yhdessä.
- Venttiilien LS-linja kertoo pumpulle suurimman kuorman paineen. Pumppu pitää paineen noin 20 bar
  sen yläpuolella ja tuottaa vain sen, mitä venttiilit päästävät läpi.
- **Kun mitään ei käytetä, pumppu lepää itsestään** noin 20 barissa lähes ilman tuottoa. Ohitus-,
  purku- ja vapaakiertoventtiileitä ei tarvita.
- Yksi proportionaalinen LS-lohkoventtiili (esim. Danfoss PVG 32) korvaa CETOP-pohjalaatan,
  BAV-713:n, VPR3:n, OD15:n, VMP:n ja BPV:n. Keulapotkuri ja vinssi saavat **portaattoman** ohjauksen.
- **Kannattaa,** jos vähintään kaksi toteutuu: portaaton keulapotkuri, ankkurivinssi, pitkäkestoinen
  painepesu. Muuten nykyinen suunnitelma on halvempi ja riittää.

## Mikä muuttuu nykysuunnitelmaan verrattuna

- **Poistuu:** CETOP-pohjalaatta, BAV-713, VPR3, OD15, VMP ja BPV-ohitusventtiili, sekä
  PVH57-selvityksen 2/2-, 3/2- ja FXDC-ratkaisut, joita tarvitaan vanhojen osien kanssa.
- **Säilyy:** säiliö, 50 mm:n imu, kytkin ja kannake, keulapotkurin 1/2":n letkut, jäähdytin.
- **Mahdollisuus, joka vaatii omistajien päätöksen:** PVG 32:n P-portin paineluokka on 350 bar
  (PVSI-päätylevyllä; PVS-päätylevyllä 300 bar) [datalehti PVG 32 s. 12], ja PVH-luettelon mukaan LS-järjestelmän paineenrajoitin voi olla 280 bar. Silloin
  keulapotkuri pääsisi lähemmäs täyttä työntöä nykyisen noin 85–88 %:n sijaan. Edellyttää, että
  pumpun säätöalue sallii sen (C-jousi 70–250 bar, **⚠ tarkista Danfossilta**) ja muuttaisi
  250 barin päätöstä (2026-10-21).

## Kustannukset

- LS-lohkoventtiilin hinta uutena **⚠ ei tiedossa** (arviolta useita satoja euroja lohkolta [arvio]).
  Käytetty 5-lohkoinen PVG 32 on myynnissä 400 €:lla; omistaja tarjosi 200 € (2026-10-27), ks. [Ehdokas](../aux-circuit-ls-clean-sheet.md#ostettu-venttiili-danfoss-pvg-32-5-lohkoa-torifi).
- Ratkaisu jättää käyttämättä toimivia osia, jotka on jo hankittu.

## Suositus

**Päätös 2026-10-27:** PVH57 + PVG 32 valittiin ykkösvaihtoehdoksi ([decisions.md](../../../decisions.md)).

Teknisesti paras ratkaisu on **PVH57 ja proportionaalinen LS-lohkoventtiili**, jos tavoitteena on
vähintään kaksi seuraavista: portaaton keulapotkuri, ankkurivinssi, pitkäkestoinen painepesu. Jos
tavoitteena on edelleen on/off-keulapotkuri ja mahdollisesti vinssi, (arkistoitu) F1-61
ohitusventtiilillä tai [PVH57:n pienin muutos](p2-fxdc-ls-unloading.md#suositus-kaksitiekompensoitu-virtauksensäätö-ja-ls-purku)
on halvempi ja riittää.

## Arvio ennen tarjousta


400 € on kohtuullinen, jos lohkot ja PVEH ovat kunnossa: yksi uusi PVEH maksaa enemmän kuin koko
venttiili. Venttiili sopii vain PVH57-reittiin (suljetun keskiasennon moduulilla). Ennen tarjousta
selvitetään kokoonpanokoodilla pumppumoduulin tyyppi ja karat sekä kysytään myyjältä, toimiko PVEH
purettaessa.

**Päivitys 2026-10-27:** Myyjä ei päässyt kokeilemaan venttiiliä (keulapumpun kardaani rikki), joten
toimintakunnosta ja vuodoista ei ole tietoa. Sisäsäilytys pienentää ruostumisen ja karojen
jumiutumisen riskiä, mutta auki olleiden porttien kautta sisään on voinut päästä likaa. Omistaja
tarjosi **200 €** perustellen riskillä, että venttiili joutuu kierrätykseen [omistaja 2026-10-27].
Tarjous on perusteltu: pelkkä PVEH-yksikkö on uutena noin 670 € + ALV, ja karat sekä PVE:t voi
koestaa ja tarvittaessa vaihtaa yksitellen. Myyjän mukaan venttiili oli kytkettynä
säätötilavuuspumppuun, joten pumppumoduulin vaihto ei todennäköisesti ole tarpeen
[myyjä 2026-10-27].

**Päivitys 2026-11-02:** Kaupat tehty: **200 € + rahti 39,90 €**, yhteensä 239,90 €. PVE-liittimet tulevat venttiilin mukana [omistaja 2026-11-02].
Kun venttiili saapuu, tulpataan avoimet portit heti, luetaan pumppumoduulin ja peruslohkojen koodit
sekä tarkistetaan karojen liike käsin ennen koestusta ([Puhdistus ja koestus](../aux-circuit-ls-clean-sheet.md#puhdistus-ja-koestus)).

