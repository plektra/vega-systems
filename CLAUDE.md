# Ohjeet Vegan järjestelmärepossa työskentelyyn

Tämä repo dokumentoi ja suunnittelee Vegan järjestelmät. Vega on vuonna 1912 rakennettu
teräshinaaja (16,15 m), jota kaksi omistajaa kunnostaa. Kyse on dokumentaatiosta ja suunnittelusta,
ei ohjelmistosta: Markdownia, YAML-dataa ja myöhemmin pieniä laskentaskriptejä.

## Kenen kanssa työskentelet

- **Osallistujat eivät välttämättä osaa gitiä tai kehitystyökaluja.** Moni istunto tulee Claude
  Coden verkko- tai mobiiliversiosta. Hoida kaikki git-työ heidän puolestaan ja kerro tekemisistäsi
  yhdellä selkeällä lauseella ilman ammattisanastoa ("Tallensin muutoksesi ja tein
  muutosehdotuksen: <linkki>").
- **Vastaa sillä kielellä, jolla käyttäjä kirjoittaa** (yleensä suomi).
- **Omistajat päättävät.** Suosittele selkeästi, mutta kirjaa heidän päätöksensä sellaisinaan,
  myös hyväksytyt kompromissit (esim. "noin 90 %:n työntövoima hyväksytty kustannussyistä").
- **Kustannuksilla on väliä.** Suosi ratkaisuja, joissa käytetään olemassa olevia osia, ja kerro,
  kun halvempi vaihtoehto riittää.

## Kieli

- **Dokumenttien sisältö kirjoitetaan suomeksi:** tekstit, taulukot, päätösloki, pull requestien
  kuvaukset. Käytä vakiintunutta suomalaista hydrauliikka- ja venesanastoa (paineenrajoitusventtiili,
  virtauksensäätöventtiili, orbitroli, voimanulosotto/PTO, styyrpuuri, paapuuri).
- **Englanniksi pidetään:** tiedosto- ja kansionimet, YAML-avaimet (`pressure_bar`), commit-viestit,
  haaroiden nimet sekä tuotenimet ja osanumerot. Ne ovat tunnisteita, ja niiden pitää pysyä vakaina.
- **Lainaukset** datalehdistä voi jättää alkuperäiskielelle, kunhan merkitys selitetään suomeksi.
- **Desimaalierotin on pilkku** tekstissä ja taulukoissa (16,6 cm³), mutta YAML-arvoissa piste
  (16.6).

## Repon rakenne

```
vessel/       yhteiset tiedot (alus, kone, vaihteisto, sähköjärjestelmän perustiedot) — yksi totuuden lähde
hydraulics/   current-system.md, requirements.md, loads.yaml, design/, img/
electrics/    current-system.md, … (sama rakenne kuin hydraulics)
decisions.md  kaikkien järjestelmien päätösloki, uusin ensin
```

- **Uusi järjestelmä** (esim. `fuel/`, `water/`, `ventilation/`, `heating/`) saa oman kansionsa
  samalla rakenteella kuin `hydraulics/`: README.md, current-system.md, sitten vaatimukset ja
  selvitykset tarpeen mukaan. Lisää se juuren README:n taulukkoon.
- **Usean järjestelmän tarvitsema tieto** kuuluu tiedostoon `vessel/README.md`. Järjestelmien
  dokumentit linkittävät siihen eivätkä kopioi sitä.
- **Vaihtoehtoselvitykset ja vertailut** kuuluvat kansioon `<järjestelmä>/design/<aihe>.md`.

## Dokumentointisäännöt

1. **Merkitse jokaisen tiedon lähde** Lähde-sarakkeeseen tai tekstiin: `[omistaja VVVV-KK-PP]`
   (omistajan kertoma), `[blogi VVVV-KK-PP]` (plektra.github.io), `[datalehti <tuote>]` ja URL, tai
   `[laskelma]` omalle laskelmalle.
2. **Älä koskaan keksi lukuja.** Merkitse tuntematon arvo `**⚠ ei tiedossa**` ja epävarma
   `**⚠ tarkista**`. Jos arvioit, sano että kyse on arviosta, ja kirjaa oletukset (öljyluokka,
   hyötysuhteet, pituudet).
3. **Kun uutta tietoa tulee,** päivitä kaikki kohdat, joihin se vaikuttaa: järjestelmän dokumentti,
   `vessel/` jos tieto on yhteistä, `loads.yaml`, vaatimukset, selvitykset ja avointen kysymysten
   listat (rastita `[x]`, kun vastattu). Päivitä dokumentin tila ja päivämäärä.
4. **Tarkista aiemmat johtopäätökset uutta tietoa vasten.** Jos uusi tieto kumoaa aiemman
   laskelman tai suosituksen, korjaa se ja kerro siitä selvästi. Älä jätä vanhentuneita lukuja.
5. **Kirjaa päätökset** tiedostoon `decisions.md` (päivä, järjestelmä, päätös, perustelu, linkki) ja
   päivitä ne asianomaisiin dokumentteihin.
6. **Yksiköt:** SI, lisäksi bar, l/min, cm³ (kierrostilavuus), Nm, kW, °C, mm. Muunna vain, kun
   datalehdessä on muita yksiköitä.
7. **Tuotelinkit:** linkitä datalehdet URL:lla, älä tallenna valmistajien PDF:iä repoon. Omistajien
   omat kuvat ja piirustukset kuuluvat kansioon `<järjestelmä>/img/`.
8. **Skannatut PDF:t:** moni datalehti on skannattu. Jos tekstin poiminta ei onnistu, renderöi sivut
   kuviksi ja lue ne, ja kerro mitkä arvot luettiin kuvista.
9. **Repo on julkinen** (sisältö CC BY 4.0, koodi MIT). Älä tallenna henkilötietoja
   (puhelinnumerot, osoitteet, sähköpostit), salasanoja, verkkoavaimia, hälytyskoodeja tai muuta,
   mitä ei haluta julkiseksi. Jos käyttäjä antaa tällaista tietoa, kerro, ettei sitä kirjata
   repoon. Valmistajien PDF:iä ja muiden tekijänoikeuden alaisia kuvia ei tallenneta.
10. **Turvallisuuskriittiset toiminnot** (ohjaus, ankkurointi, kuorman pito, kaikki mikä voi
   puristaa ihmisen) vaativat vikatilanteiden kuvauksen. Muistuta omistajia, että pätevän henkilön
   pitää tarkistaa ne ennen rakentamista.

## Käytössä olevat laskentaoletukset

Nämä ovat voimassa, ellei dokumentissa toisin sanota. Muuta niitä tähän, jos omistajat päättävät
toisin.

- Hydrauliöljy ISO VG 46 (luokka vahvistamatta); tiheys 870 kg/m³.
- Hammaspyöräpumpun volumetrinen hyötysuhde 92 %, mekaaninen 90 %.
- Koneen tyhjäkäynti 700 rpm omistajan mukaan (2026-10-22, ei vielä mitattu), ks. `vessel/README.md`.

## Git-työnkulku (tee käyttäjän puolesta)

- **Larin muutokset menevät suoraan `main`-haaraan** ilman pull requestia: committaa ja pushaa
  `main`iin (tai yhdistä istunnon haara fast-forwardina `main`iin ja poista haara).
- **Muiden muutokset menevät pull requestina.** Älä committaa niitä suoraan `main`iin; työskentele
  haarassa (Claude Coden verkkoversio antaa jokaiselle istunnolle oman haaran).
- **Kuka käyttäjä on:** jos `git config user.name` on Lari, tai käyttäjä kertoo olevansa Lari, toimi
  Larin säännöllä. Jos asia on epäselvä, kysy kerran ennen tallennusta.
- **Aloita uusimmasta `main`-haarasta.** Jos haara on jäljessä, päivitä se ennen muokkauksia.
- **Pidä commitit ja pull requestit pieninä,** yksi aihe kerrallaan. Commit-viestit englanniksi.
  Pull requestin kuvaus suomeksi, alkaen selkokielisestä yhteenvedosta, jonka omistaja voi hyväksyä
  puhelimella.
- **Älä koskaan tee force-pushia.** Älä poista tai ylikirjoita toisen sisältöä kysymättä.
- **Jos tulee yhdistämiskonflikti, säilytä molempien tiedot.** Kysy käyttäjältä vain, jos versiot
  ovat ristiriidassa keskenään.
- Kun käyttäjä sanoo "tallenna", "valmis", "save" tai "done", käytä `/save`-taitoa.

## Repon taidot (skills)

| Taito | Käytä, kun käyttäjä… |
|---|---|
| `/save` | haluaa tallentaa tai lopettaa: commit, push ja pull request |
| `/add-info` | kertoo uusia tietoja, mittauksia, kuvia tai datalehtiarvoja |
| `/log-decision` | kertoo, että jotain on päätetty |
| `/open-questions` | kysyy, mikä on vielä auki tai puuttuu, tai mitä tehdä seuraavaksi |
