# Arkisto: hydrauliikan nykytilan vanhentuneet kohdat (lokakuu 2026)

> **🗄 Arkistoitu 2026-11-03.** Siirretty tiedostosta [current-system.md](../../current-system.md)
> hydrauliikkamateriaalin tarkistuksessa. Kohdat koskevat kokoonpanoja, jotka on korvattu: P2 =
> Parker F1-61 + BPV (korvattu PVH57:llä 2026-10-27), 32 mm:n P2-imulinja (korvattu 50 mm:llä
> 2026-10-23) ja vanhat apupiirin venttiilit VPR3, OD15, CETOP-pohjalaatta, VMP ja BAV-713
> (korvattu PVG 32:lla 2026-10-27). Teksti on sellaisenaan, eikä sitä päivitetä.

## Tilarivin päivityshistoria (2026-10-23 – 2026-11-03)

> (ks. §0). Päivitetty 2026-11-03: PVG 32 saapui; rungon koodit ja kilven paineasetus (PVP 28? bar, todennäköisesti 280 bar) luettu, ks. [Vastaanotto](../aux-circuit-ls-clean-sheet.md#vastaanotto-2026-11-03-rungon-merkinnät). 2026-11-02: venttiilipöytä Danfoss PVG 32 ostettu (200 € + rahti 39,90 €). 2026-11-01: P2-pumppu Vickers PVH57 ostettu ja noudettu (150 €). 2026-10-28: P2:n nykyisen 32 mm:n imun täysiaukkoinen palloventtiili jää P1:lle; 50 mm:n palloventtiili P2:lle todennäköisesti jo olemassa **⚠ tarkista veneellä**; 50 mm:n ulosotto: muhvi → 90°:n kulma → palloventtiili → letkukara; [hankintalista](../../procurement.md) koottu. 2026-10-27: ankkurivinssissä kahden ketjun ketjuveto ja käsikäyttöinen nauhajarru ketjupyörän akselilla, vapaa pudotus, räikkälukitus ja käsikampi, sähkömoottori korvataan hydraulimoottorilla; U11:n vuotolinja uusiksi suoraan säiliöön, ankkurivinssi ei kytketty (voimansiirto uusiksi); **P2 on Vickers PVH57** (päätös, kaupat sovittu), kytkin HRC 150; venttiileiksi PVG 32 (ykkösvaihtoehto); F1-61-selvitys arkistoitu. 2026-10-26: P2:n valinta (F1-61) on alustava, omistaja kallistuu säätötilavuuspumppuun; säiliön öljypinta vähintään 1 m pumppujen yläpuolella; paluusuodattimen malli OMTF112C10NA2; 2026-10-24: P2 = Parker F1-61 tai vastaava ISO 7653 -vinoakselipumppu ohitusventtiilillä (Torin kauppa peruuntui); 2026-10-23: P2 = Parker F1-61 + BPV-F1, Spidex-kytkin, 50 mm imulinja (alustava päätös); P1:n imulinja 25 mm × 3,2 m ja muutosehdotus ([p1-steering-pump.md](../p1-steering-pump.md)). Kohdat, joissa on merkintä **⚠ tarkista**, pitää tarkistaa veneellä.

## §0 kohta 9: alkuperäiset oletukset (BAV-713 ja VPR3)

   *Oletukset: noin 6 barin häviö venttiilin kummallakin reitillä (P→A ja B→T), mitatut
   letkupituudet ja noin 1,5 bar paluusuodattimessa. 4–10 barin venttiilihäviöillä lämmin tulos on
   85–89 %. **⚠ Hanki BAV-713:n painehäviökäyrä** tarkentamaan tätä. **Virtauksensäätöventtiilin (F1-61-reitillä VPR3) omaa painehäviötä ei ole mukana** (**⚠ ei tiedossa**); vertailukohtana Sun FXDC vie noin 33 l/min:llä noin 8 bar [datalehti Sun FXDC, kuvaajasta luettu 2026-10-26], mikä pienentäisi työntövoimaa arviolta noin 3 prosenttiyksikköä.* 

## §0 kohdat 10–11: P2:n 32 mm:n imulinja ja F1-61 (korvattu)

10. **P2:n imulinja: omistajat vahvistivat 32 mm:n sisähalkaisijan (≈ 1-1/4"), mikä riittää.**
    Säiliön ulosotto on samaa kokoa, joten linjassa ei ole 1":n kuristusta. Arvioitu paine pumpun
    imuaukolla 51 cm³:n pumpulla, kun säiliön öljypinta on noin 1 m pumpun yläpuolella (+0,085 bar)
    ja liitinhäviöt ovat noin K = 2,5 (säiliön ulosotto, palloventtiili, kulmat):

    | Öljyn lämpötila | 700 rpm (tyhjäkäynti) | 1000 rpm |
    |---|---|---|
    | 5 °C | **−0,15 bar** | −0,26 bar |
    | 15 °C | −0,03 bar | −0,09 bar |
    | 20 °C | 0,00 bar | −0,04 bar |
    | 40 °C | +0,05 bar | +0,03 bar |

    Hammaspyöräpumput vaativat yleensä, että imupaine on vähintään noin −0,2…−0,3 bar (ylipaine).
    **Tarkista valitun pumpun datalehdestä.** 32 mm:n linja pysyy tämän sisällä tyhjäkäynnillä noin
    5 °C:een asti. (1":n linjalla vastaava arvo olisi ollut noin −0,5 bar, joten 32 mm oli oikea
    valinta.) Kylmänä kannattaa silti kytkeä pumppu tyhjäkäynnillä.
    Lähtö satamasta on kriittisin tilanne: keulapotkuria tarvitaan heti käynnistyksen jälkeen, kun
    öljy on konehuoneen lämpöistä. HV-luokan öljy antaa lisää marginaalia.

    2500 rpm:llä virtaus olisi niin suuri, että kytkimen pitää silti irrota automaattisesti noin
    1000–1200 rpm:n yläpuolella.

    **Päivitys 2026-10-27:** P2 on PVH57; sen mobiiliversio sallii 2400 rpm imupaineella 0 bar, ja
    50 mm:n imulinja säilyy, ks. [p2-variable-pump](../p2-variable-pump.md#sopivuus-vegaan-laskelma).
    Alla olevat F1-päivitykset ovat taustaa.

    **Päivitys 2026-10-23:** Parkerin F1-luettelon mukaan imupaineen pitää olla vähintään 1,0 bar
    absoluuttista (noin 0 bar ylipainetta), ja F1-61:lle suositellaan 50 mm:n imuliitintä. Nykyinen
    32 mm:n linja ei täytä tätä kylmällä öljyllä edes tyhjäkäynnillä (noin −0,2 bar 5 °C:ssa VG 46:lla).
    **Päätös 2026-10-23: 50 mm:n imulinja** (korvaa 2026-10-22:n 32 mm:n päätöksen). HV 32 -öljy on
    edelleen suositus.

    **Päivitys 2026-10-22:** Parker F1-061:llä (59,5 cm³) imuvirtaus on suurempi. **Suositus: 38 mm:n
    imulinja mahdollisimman lyhyenä (~2 m) ja HV 32 -öljy**, jolloin imupaine pysyy noin 0 barissa
    vielä 1000 rpm:llä ja 5 °C:ssa. Vertailu ja kierroslukuanalyysi:
    [p2-pump-options.md](p2-pump-options.md#imupuoli-letkun-koko-ja-pituus-sekä-öljylaatu).
11. ~~BPV syöttöasennossa korkeilla kierroksilla~~: ei koske PVH57:ää (päätös 2026-10-27). PVH57:n
    imupaine täydellä iskulla 2400 rpm:llä ks. [p2-variable-pump](../p2-variable-pump.md#sopivuus-vegaan-laskelma).


## Vanhentuneet avoimet kysymykset

- [x] BAV-713: fluiconnecto BAV-IC3-713, 60 l/min, 350 bar
- [ ] BAV-713:n painehäviö ~34 l/min:llä (P→A, B→T): ei luettelossa; kysy toimittajalta tai mittaa
- [x] BAV-713:n kelojen jännite: 24 VDC [omistaja 2026-10-23]
- [x] Keulapotkurin iskuventtiilit: ~~lisätään A/B-iskuventtiililohko~~ → **ei lisätä** (päätös 2026-10-23, korvaa saman päivän päätöksen)
- [x] Venttiilien tehtävät: Rexrothin 2/2-patruunaventtiili kytkee paineen CETOP-pohjalaatalle, BAV-713 ohjaa suuntaa [omistaja 2026-10-22]
- [x] CETOP-pohjalaatta: Flowfit NG6, 4-paikkainen, rinnankytketty, P/T 1/2", A/B 3/8"
- [x] 2/2-venttiili on omassa erillisessä rungossaan, ei pohjalaatan kavitetissa [omistaja 2026-10-23]
- [x] Pohjalaatan materiaali: teräs
- [ ] Pohjalaatan painearvo Flowfitilta: vahvista, että kestää 250 bar (teräs, todennäköisesti 250–350 bar)
- [x] ~~VMP:n nykyinen asetus~~: säädetään käyttöönotossa 250 bariin [omistaja 2026-10-23]
- [x] Paineenrajoitusventtiili: Marchesini VMP 3/4", enintään 90 l/min, 350 bar, jousi 80–300 bar (todennäköisesti)
- [x] ~~BPV:n ohitustilan lämpö ajossa~~: BPV:tä ei tule (päätös 2026-10-27)
- [x] ~~P2: Parker F1-61 (59,5 cm³) + BPV-F1 käsiohituksella (päätös 2026-10-23)~~ → **P2 on Vickers PVH57** (päätös 2026-10-27)
- [x] **Tarvitaanko iskuventtiililohko lainkaan?** Ei (päätös 2026-10-23, BAV-713-kokoonpanolle). BAV-713:n keskiasento on kelluva (A, B ja T yhdistetty), ja VMP rajoittaa P-linjan 250 bariin, joten painepiikit ovat jo rajattuja.
- [ ] **Käyttöönoton säädöt (vanha kokoonpano):** VMP 250 bariin painemittarilla (2G1) keulapotkuri jumitettuna tai BAV-713 ääriasennossa
