# Arkisto: PVH57:n FXDC + LS-purku -reitti ja vertailu F1-61:een

> **🗄 Arkistoitu 2026-11-03.** Siirretty tiedostosta [p2-variable-pump.md](../p2-variable-pump.md),
> kun apupiirin venttiileiksi valittiin Danfoss PVG 32 (päätös 2026-10-27), venttiili ostettiin
> (2026-11-02) ja sen karat todettiin käsin toimiviksi (2026-11-03). Tässä ovat alkuperäiset
> osiot sellaisinaan: F1-61:n ja PVH57:n vertailu, VPR3:n sopimattomuus, kaksitiekompensoitu
> virtauksensäätö (Sun FXDC) ja LS-purku 2/2-magneettiventtiilillä, ankkurivinssin 3/2-kytkentä,
> sekä tämän reitin osat, asennus, säädöt, vikatilat ja kustannukset.
>
> **Tila:** varavaihtoehto vain, jos PVG 32 osoittautuu koestuksessa korjauskelvottomaksi.
> Tekstin luvut ja suositukset ovat arkistointipäivän tilanteen mukaisia, eikä niitä päivitetä.
> Sisäiset linkit (#…) viittaavat osin alkuperäiseen tiedostoon.

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
- **Kannake ja akselikytkin tarvitaan kummassakin reitissä.** Kumpaakaan ei ole vielä rakennettu
  eikä hankittu [omistaja 2026-10-25], joten ne eivät ole PVH57:n lisäkustannus. Kannake
  suunnitellaan SAE C -laipalle (ISO 7653:n sijaan) ja 36 kg:n pumpulle; kytkimeksi valittiin
  HRC 150 kartioholkeilla (päätös 2026-10-27), ks. [Tarvittavat osat](#tarvittavat-osat-pumpun-lisäksi-minimi).
- **Vain PVH57-reitissä tarvittavat osat:** kaksitie-virtauksensäätöventtiili (esim. Sun FXDC),
  2/2-magneettiventtiili ja kuristin LS-linjaan, kotelovuotoletku säiliöön ja SAE-laippaliittimet.
  BPV-ohitusventtiiliä (noin 430 € + ALV) ei tarvita.
- **Ennallaan:** CETOP-pohjalaatta, BAV-713, VMP, letkut, säiliö, suodatin ja jäähdytin.

**Hinta ja tila:** pumppu ostettu 150 € (ilmoitushinta 190 €) ja noudettu [omistaja 2026-11-01]. Lisäksi tarvitaan FXDC, magneettiventtiili ja liittimet, mutta
BPV jää pois (ks. [kustannusvertailu](#kustannusvertailu-arvio)). **Päätös 2026-10-27:** P2 on PVH57,
ja kauppa toteutui 2026-11-01. F1-61-vaihtoehto on arkistoitu.

## Kumpi on monimutkaisempi: F1-61 vai PVH57

> Lisätty 2026-10-25. Vertailu on arvio, ei päätös.

Venttiilien ja ohjauksen määrä on reiteissä suunnilleen sama. Ero on pumpun vaatimuksissa ja
siinä, kuinka paljon järjestelmää pitää ymmärtää.

| | F1-61 + ohitusventtiili | PVH57 |
|---|---|---|
| Pumppu | yksinkertainen, kevyt (8,5 kg) | säädin, kotelovuotoletku, raskas (noin 36 kg **⚠ tarkista**) |
| Magneettiventtiilit | ohitusventtiili (BPV) ja OD15 | 2/2, ja vinssiä varten ehkä 3/2 |
| Virtauksen rajoitus | VPR3 (olemassa) | uusi FXDC |
| Ohjauslogiikka | BPV:n tilaa saa vaihtaa vain alle 20 barissa, joten tarvitaan paineanturi ja ohjain ([pressure-monitoring](../pressure-monitoring.md)) | 2/2 suljetaan, kun jotain käytetään |
| Käyttöönotto | paineenrajoitin säädetään | paineenrajoitin ja säädin säädetään, kotelo täytetään öljyllä |

**Missä PVH57 on oikeasti vaativampi:**

- **Öljyn puhtaus:** mäntäpumppu vaatii puhtaampaa öljyä: 17/15/13 140–210 barissa ja **16/14/12 yli
  210 barin** [luettelo s. 31]. Vegan 250 barin asetuksella pätee 16/14/12 (korjattu 2026-10-26;
  aiemmin tässä mainittiin vain 17/15/13). Valmiustilassa (noin 20 bar) vaatimus on lievempi.
  Nykyinen paluusuodatin on OMTF112C10NA2, 10 µm [omistaja 2026-10-26]. Tilauskoodin `C10` tarkoittaa
  jälleenmyyjien vastinelementtien perusteella **selluloosaa, 10 µm nominaalinen** (**⚠ tarkista**
  OMT:n luettelosta). Nominaalinen selluloosaelementti ei luotettavasti pidä öljyä luokassa
  16/14/12; siihen käytetään yleensä lasikuituelementtiä, jonka erotusaste on ilmoitettu
  (beta-arvo) [arvio, yleistieto]. Saman sarjan lasikuituversio `F10` (10 µm absoluuttinen) on
  jälleenmyyjän mukaan mitoitettu vain 55 l/min:lle [jälleenmyyjä Phoenix Hydraulics, OMTF112F10NA2].
  **Johtopäätös:** PVH57-reitillä suodatin tai ainakin elementti pitää vaihtaa lasikuituun, ja
  virtauskesto tarkistetaan (apupiiri noin 33–38 l/min ja P1:n paluu 14–37 l/min samassa
  suodattimessa). Kustannus on pieni (suodatin noin 30 £ jälleenmyyjällä), mutta se lisätään
  PVH57-reitin osaluetteloon.
  **Ehdokas: OMTF171F10NA1** [omistaja 2026-10-26], ks. [Paluusuodattimen vaihto](../p2-variable-pump.md#paluusuodattimen-vaihto-omtf171f10na1).
- **Kunto:** pumppu on arviolta 1980-luvun lopulta tai 1990-luvulta (ks.
  [Ikä](../p2-variable-pump.md#ikä-ja-siihen-liittyvät-riskit)) ja uudelleen maalattu. Myyjän mukaan se on säilytetty
  lämpimässä öljyt sisällä, ruosteetta, ja akseli pyörii äänettömästi [myyjä 2026-10-25], joten
  kuntoriski on pienempi kuin aluksi arvioitiin. Tiivistesarjat ja korjaukset ovat silti
  kalliimpia, ja harvempi korjaamo tuntee sen.
- **Ymmärrettävyys:** vian sattuessa F1-61:n toiminta on helpompi päätellä. LS-ohjauslinja on uusi
  käsite.
- **Asennus:** pumppu on noin neljä kertaa painavampi, ja siinä on yksi letku enemmän.

**Mitä PVH57:llä saavutetaan:** lähinnä pienempi lämpö, kun keulapotkuria käytetään korkeilla
kierroksilla (arviolta 2–3 kW eikä noin 38 kW [laskelma]). Keulapotkuria käytetään lyhyitä hetkiä ja
yleensä satamassa matalilla kierroksilla, jolloin hyötysuhteella on vähemmän väliä (ks.
[p2-pump-options: Käyttöjakso](p2-pump-options.md#käyttöjakso-miksi-hyötysuhteella-on-vähemmän-väliä-kuin-luulisi)).
Ankkurivinssin kanssa PVH57 ei ole automaattisesti parempi (ks.
[Ankkurivinssi](#ankkurivinssi-ja-muut-kuormat-samassa-kytkennässä)).

**Suositus:** F1-61 ohitusventtiilillä, kuten on alustavasti päätetty. Se on yksinkertaisempi ja käyttää
olemassa olevaa VPR3:a, eikä sen suurin heikkous juuri näy Vegan käytössä. PVH57:ään kannattaa
palata vain, jos ankkurivinssiä käytetään pitkiä jaksoja tai keulapotkuria joudutaan käyttämään
usein korkeilla kierroksilla, tai jos tavoitteeksi tulee jokin
[vain säätötilavuuspumpulla järkevistä ominaisuuksista](#mitä-pvh57-mahdollistaisi-mitä-kiinteällä-pumpulla-ei-ole-järkevää).

## Mitä PVH57 mahdollistaisi, mitä kiinteällä pumpulla ei ole järkevää

> Lisätty 2026-10-25. Arvio ilman laskelmia; ideat vaativat tarkistuksen ennen kuin niitä käytetään
> päätöksen perusteena.

### Proportionaaliohjaus onnistuu kummallakin

- **Kiinteä pumppu (F1-61):** proportionaaliventtiili, jonka tuloosassa on kolmitiekompensaattori.
  Se laskee ylimäärän säiliöön hieman kuorman painetta korkeammassa paineessa. Toimii hyvin, mutta
  korkeilla kierroksilla ylimäärä kuristuu lämmöksi kuten nyt.
- **PVH57:** pumppu tuottaa vain sen, mitä venttiili päästää läpi, joten lämpöä syntyy vähän millä
  tahansa kierroksilla.
- Kummassakin tapauksessa keulapotkurin portaaton ohjaus vaatii proportionaaliventtiilin ja ohjaimen,
  koska BAV-713 on on/off-venttiili (ks. [p2-pump-options, vaihtoehto E](p2-pump-options.md)).

### Mitä vain PVH57 tekee järkevästi

1. **Keulapotkurin portaaton teho halvemmalla.** LS-linjaan lisätään pieni sähköisesti säädettävä
   paineenrajoitusventtiili, jolla pumpun painetta säädetään noin 20 barin ja 250 barin välillä.
   Moottorin vääntö ja potkurin työntö seuraavat painetta, ja BAV-713 hoitaa edelleen suunnan.
   LS-linjan venttiili on pieni, koska sen läpi kulkee vain vähän öljyä. Kiinteällä pumpulla sama
   vaatisi täyden virtauksen venttiilin, ja ylimäärä menisi lämmöksi. **⚠ Idea, ei laskettu:**
   tarkista, sopiiko SH240 tällaiseen ohjaukseen ja miten säätö käyttäytyy (vakaus, vasteaika).
2. **Useita kuormia yhtä aikaa ilman hukkaa.** Vinssi, painepesuri tai nosturi saavat yhteensä enintään
   pumpun tuoton, ja pumppu tuottaa vain kulutetun määrän. Kiinteällä pumpulla käyttämätön osa
   kuristuu aina lämmöksi.
3. **Jatkuvat kuormat koneen käydessä,** esim. hydraulisesti käytetty generaattori tai pumppu:
   vakiovirtaus kierroksista riippumatta ilman ylimäärän kuristamista. Tällaisia kuormia ei ole nyt
   suunnitelmissa; hydrauligeneraattoria ei suositella (ks.
   [ac-power-source.md](../../../electrics/design/ac-power-source.md), 2026-10-28).
4. **Paineen pito ilman virtausta,** esim. sylinterin pitäminen paineessa: pumppu lepää
   nollatuotolla, kun kiinteän pumpun koko tuotto menisi paineenrajoittimen yli.

### Mitä PVH57 ei muuta

- **Suurin työntövoima ei kasva:** pumpun säätöalueen yläraja on 250 bar.
- **Tyhjäkäynnin tuotto on sama,** noin 38 l/min 700 rpm:llä [laskelma].
- **Venttiilejä ei jää pois:** suunta- ja virtausventtiilit tarvitaan edelleen.

**Johtopäätös:** PVH57 on järkevä, jos järjestelmää aiotaan laajentaa (portaaton keulapotkuri,
useita samanaikaisia tai jatkuvia kuormia). Miten apupiiri rakennettaisiin alusta alkaen LS-lohkoventtiilillä:
[aux-circuit-ls-clean-sheet](../aux-circuit-ls-clean-sheet.md); ilman venttiilipöytää on/off-venttiileillä:
[aux-circuit-ls-onoff](aux-circuit-ls-onoff.md). Nykyisillä tavoitteilla (on/off-keulapotkuri ja
ankkurivinssi) F1-61 riittää. Portaaton keulapotkuri on tärkein syy harkita PVH57:ää uudelleen.

## Miten LS-linjaa käytetään

CV-säädin pitää pumpun lähtöpaineen noin 20 bar LS-portin painetta korkeampana, ja paineenrajoitin
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
PTO ─ HRC150 ─ PVH57 ─ 2-tie kompensoitu virtauksensäätö ~34 l/min ─ CETOP P (VMP) ─ BAV-713 ─ keulapotkuri
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
- **Työntövoima** on arviolta noin 82–85 %. **Korjattu 2026-10-26:** aiemmin arvioitiin FXDC:n
  painehäviöksi muutama bar ja työntövoimaksi 85–88 %. Datalehden kuvaajan mukaan noin 33 l/min
  kulkee FXDC:n läpi noin 8 barin paine-erolla, joten moottori saa noin 242 bar miinus BAV-713:n ja
  letkujen häviö [datalehti Sun FXDC, kuvaajasta luettu; työntövoima arvio noin 4 % / 10 bar].
- **Lämpö keulapotkurin käytössä 1800 rpm:llä** on arviolta 2–3 kW (35 l/min × (250 − kuorman paine),
  kun kuorma on noin 200 bar). F1-61:llä se on noin 38 kW, ks.
  [p2-pump-options](p2-pump-options.md#käyttäytyminen-eri-kierroksilla-parker-f1-061) [laskelma].
- **Ohjausjärjestys:** 2/2 kiinni → BAV-713 suunta. Pois: BAV-713 keskelle → 2/2 auki. **2/2:n
  pitää olla auki aina, kun BAV-713 on keskellä.** Muuten pumppu seisoo 250 barissa nollatuotolla,
  mikä kuluttaa luettelon kuvaajan mukaan noin 10 kW.

### Ankkurivinssi ja muut kuormat samassa kytkennässä

> Lisätty 2026-10-25. Vinssin moottorin tiedot puuttuvat (kierrostilavuus, käyttöpaine,
> käyttöaika), joten luvut ovat esimerkkejä eri käyttöpaineilla [laskelma].

**Kytkentä onnistuu.** Vinssin suuntaventtiili tulee CETOP-pohjalaatan vapaaseen paikkaan
BAV-713:n rinnalle, kuten F1-61-suunnitelmassakin. Ohjaus toimii samoin: 2/2 suljetaan aina, kun
jokin suuntaventtiili (BAV-713 tai vinssin venttiili) ohjataan, ja avataan, kun kaikki ovat
keskellä. Vinssi saa enintään noin 34 l/min ja 250 bar.

**Ongelma on lämpö, jos vinssi toimii matalalla paineella.** Suosituskytkennässä pumppu pitää aina
250 baria, ja FXDC kuristaa paineen alas kuorman paineeseen. Lämpö on noin
34 l/min × (250 bar − kuorman paine) / 600:

| Vinssin käyttöpaine | Lämpö suosituskytkennällä | Vertailu: F1-61 700 rpm:llä | F1-61 1800 rpm:llä |
|---|---|---|---|
| 50 bar | noin 11 kW | enintään noin 1 kW | noin 6 kW |
| 100 bar | noin 8,5 kW | enintään noin 1 kW | noin 11 kW |
| 150 bar | noin 5,7 kW | enintään noin 1 kW | noin 17 kW |
| 200 bar | noin 2,8 kW | enintään noin 1 kW | noin 22 kW |

F1-61:n luvuissa ylimäärä (700 rpm:llä noin 3 l/min, 1800 rpm:llä noin 67 l/min) valuu VPR3:n
B-portista kuorman paineessa; VPR3:n oma painehäviö on jätetty pois [laskelma]. Keulapotkurin
lyhyillä käytöillä 2–3 kW ei haittaa, mutta minuuttien vinssauksessa 5–11 kW lämmittää öljyä
selvästi (ks. [oil-cooling](../oil-cooling.md)).

**Korjaus: LS-signaalin valinta kolmitiemagneettiventtiilillä.** LS-linjaan lisätään 3/2-venttiili,
joka valitsee, mistä pumppu saa ohjauspaineensa:

```
LS-portti ─┬─ 2/2 (NO) ─ säiliö                       lepo: pumppu 20 barissa
           └─ 3/2 ─┬─ (jännitteetön) pohjalaatan P-linja, FXDC:n jälkeen   vinssi: kuormantunto
                   └─ (jännitteellinen) kuristin Ø0,8 ─ pumpun lähtö       keulapotkuri: 250 bar
```

| Tila | 2/2 | 3/2 | Pumppu | Lämpö |
|---|---|---|---|---|
| Lepo | auki | – | noin 20 bar, lähes nollatuotto | vähän |
| Vinssi | kiinni | jännitteetön | kuorman paine + noin 20 bar | noin 34 l/min × 20 bar ≈ 1,1 kW kuorman paineesta riippumatta |
| Keulapotkuri (myös yhtä aikaa vinssin kanssa) | kiinni | jännitteellinen | 250 bar | noin 2–3 kW keulapotkurilla |

- Vinssitilassa FXDC:n yli jää vain noin 20 bar. **Datalehden kuvaajan mukaan se riittää:**
  30–40 l/min:n asetus saavuttaa asetusvirtauksen noin 15–20 barin paine-erolla ja noin 95 % jo
  noin 12–14 barissa; pienemmät asetukset noin 10 barissa [datalehti Sun FXDC, kuvaajasta luettu].
  Jos pohjalaatan ja suuntaventtiilin häviö vie marginaalista useita bareja, suurella asetuksella
  vinssin virtaus jää muutaman prosentin alle asetuksen.
- Lisäosa: suoraan toimiva 3/2-magneettiventtiili 24 V ja yksi 1/4":n letku pohjalaatan
  mittariliitännästä. **⚠ hinta ei tiedossa.**
- **Yhtäaikainen käyttö** (ankkurointi, S2 [requirements](../../requirements.md)): vinssi ja keulapotkuri
  jakavat saman 34 l/min, ja matalamman paineen kuorma saa suurimman osan. Sama rajoitus on
  F1-61-suunnitelmassa.
- **Jos vinssi tarvitsee alle 34 l/min** (hitaampi nopeus), sen CETOP-paikkaan lisätään välilaatta-
  kuristin. Vinssitilassa pumppu pitää silloin edelleen vain noin 20 bar kuorman yläpuolella, joten
  lämpö pysyy pienenä.
- **Turvallisuus:** sähkökatkossa 2/2 aukeaa ja vinssi pysähtyy. **Ankkurin pito ei saa riippua
  pumpusta:** vinssissä pitää olla jarru tai jarruventtiili ([requirements §7](../../requirements.md)).
  Pätevän henkilön pitää tarkistaa vinssin kytkentä ja kuorman pito ennen rakentamista.

**Suositus:** 3/2 kannattaa lisätä vasta, kun vinssin käyttöpaine ja käyttöaika tiedetään. Jos
vinssin käyttöpaine on lähellä 200 baria tai vinssaus kestää vain lyhyitä jaksoja, suosituskytkentä
riittää sellaisenaan.

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
| **Sun Hydraulics FXDC** (korvaa FXDA:n) | 2-porttinen, kiinteä kuristin, painekompensoitu; 45 l/min, sarja 2, pesä T-5A, **350 bar**; asetus valitaan valmiista vaihtoehdoista, `L`/`K` antaa ±25 %:n hienosäädön; tehdasasetus ±10 % (`L`, `K`) tai ±15 % (`X`) [Sunin tuotesivu](https://www.sunhydraulics.com/model/FXDC) | **Suositus.** Linjarunko T-5A-pesälle 3/4":n BSPP-porteilla on Sun **DAW**; valitaan **valurautainen DAW/S**, koska alumiinirunko kestää vain 210 bar [Sunin DAW-datalehti (paro.nl)](https://paro.nl/library//storage/datasheets/Sun/Line%20Mount%20Bodies/Sun_DAW.pdf/datasheet.html). Hinnat Hydrotechilla (USA) 2026-10-25: FXDC-LAN 83,10 $, FXDC-KAN 89,10 $, DAW (alumiini) 53,40 $; DAW/S:n hintaa ei löytynyt **⚠ ei tiedossa**. Toimittaja Suomessa Salhydro. Asetusalue keulapotkurille **T (31,45–42,55 l/min)** tai V; noin 33 l/min kulkee noin 8 barin paine-erolla [datalehti Sun FXDC, [cutsheet](https://www.sunhydraulics.com/cutsheet/FXDC/XAN?format=A4&unit=US&full=1&base=1), kuvaajasta luettu 2026-10-26]. |
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
| 1 | **HRC 150 -joustokytkin** (päätös 2026-10-27): kaksi napaa Taper Lock -holkeille (F tai H asennuksen mukaan) ja elastinen välikappale | korvaa F1-suunnitelman Spidex 48/60:n; ks. alla |
| 2 | Taper Lock 2012 -kartioholkit: **48 mm** (PTO) ja **1 1/4"** (pumppu, 31,75 mm), kiilaurat | vakio-osia, ei koneistusta; **⚠ tarkista** koodit ja 48 mm:n holkin kiilauran syvyys |
| 3 | Kannake SAE C -nelireikälaipalle | F1-reitin ISO 7653 -kannakkeen sijaan (ei vielä tehty); sama tapa: 10 mm:n teräslevy, laserleikkaus ja hitsaus. Pumppu noin 36 kg; laippa Ø127 mm:n keskitys ja 114,5 mm:n reikäneliö, ks. [tekniset tiedot](../p2-variable-pump.md#tekniset-tiedot) |
| 4 | Imuliitin: 2" SAE code 61 -laippa (UNC-pultit), O-rengas ja letkuliitin 50 mm:n letkuun | 2" = 50,8 mm, joten supistusta ei tarvita |
| 5 | Painelähdön 1" SAE code 61 -laippa (3/8-16 UNC) ja supistus 3/4":n painelinjaan | |
| 6 | Kotelovuotolinja (vähintään noin 1/2") ylimmästä vuotoportista säiliöön öljypinnan alle | korvaa BPV:n vuotolinjan |
| 7 | 2/2-magneettiventtiili, auki jännitteettömänä, suoraan toimiva, 24 V | LS-purku; ainoa uusi magneettiventtiili |
| 8 | Kuristin noin Ø0,8 mm, T-haara ja 1/4":n letkut LS-linjaan | |
| 9 | Kaksitiekompensoitu virtauksensäätöventtiili noin 34 l/min: Sun FXDC (`L`/`K`, säädettävä ±25 %) valurautaisessa linjarungossa **DAW/S** (T-5A, 3/4" BSPP) | VPR3:n tilalle; alumiininen DAW ei kelpaa (210 bar) |
| 10 | (valinnainen) 3/2-magneettiventtiili, suoraan toimiva, 24 V, ja 1/4":n letku pohjalaatan mittariliitäntään | vain jos ankkurivinssiä käytetään pitkään matalalla paineella, ks. [Ankkurivinssi](#ankkurivinssi-ja-muut-kuormat-samassa-kytkennässä) |

**Rivit 1–2: HRC 150 kartioholkeilla** (selvitys ja päätös 2026-10-27; korvaa PVH57-reitissä Spidexin). PVH57:n
akseli on lieriömäinen kiila-akseli, joten Spidexin etu (valmis 8×32×36-napa F1-61:lle) ei enää
päde. HRC 150:n H- tai F-napaan käy **Taper Lock 2012 -kartioholkki** (reikä 14–50 mm), jota saa
vakiona sekä **48 mm:n** (PTO) että **1 1/4":n** (pumppu) kiilaurallisena: ei koneistusta
[jälleenmyyjät, **⚠ tarkista** holkkikoodit; 48 mm:n holkissa kiilaura voi olla matala].
Momentti noin 600 Nm (nimellinen, **⚠ vahvista**), tarve kertoimilla noin 430 Nm ✅ [laskelma].
Hinnat: napa noin 19 € + ALV ([atlantis-pt](https://atlantis-pt.abstore.pl/couplings-semi-coupling-hub-hrc-150,c225,p263,en.html)),
elastinen osa noin 10 £ + ALV ([Cromwell](https://cromwell.co.uk/shop/bearings-and-transmissions/couplings/hrc150i-coupling-insert/p/DUN6956364E)),
holkit **⚠ hinta ei tiedossa** (arviolta 10–25 € kpl). Yhteensä arviolta **noin 80–120 € + ALV**
eli selvästi halvempi kuin Spidex (noin 215 € + ALV ja pumppunapa, jonka saatavuus 1,25":n
reiällä on epävarma). HRC 150 on halkaisijaltaan isompi (150 mm vs. 105 mm), mikä otetaan
huomioon kannakkeessa.

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

## Asennusjärjestys

> Lisätty 2026-10-25 [arvio]. Koostettu tämän dokumentin osalistasta ja kytkennästä. Pätevän
> henkilön pitää tarkistaa kannake, LS-kytkentä ja ohjauslogiikka ennen rakentamista.

1. **Pumpun tarkistus ennen asennusta.** Akselitiivisteen ympärillä ei saa olla öljyä, ja
   akselin pitää pyöriä käsin tasaisesti. Ulkoiset O-renkaat vaihdetaan liitäntöjä tehtäessä.
   Hydrauliikkakorjaamon koeajo kannattaa (ks. [Tiivistesarja](../p2-variable-pump.md#tiivistesarja)).
2. **Kannake ja kytkin.** Kannake 10 mm:n teräslevystä laserleikkaamalla ja hitsaamalla SAE C
   -reikäkuviolle ja noin 36 kg:n pumpulle **⚠ tarkista paino**. HRC 150 (päätös 2026-10-27): navat
   ja Taper Lock 2012 -holkit 48 mm (PTO) ja 1 1/4" (pumppu) sekä elastinen välikappale. Linjaus kytkimen sallimiin rajoihin
   ([current-system §0](../../current-system.md)) ja suojakotelo pyörivälle kytkimelle. Laipan mitat
   ks. [tekniset tiedot](../p2-variable-pump.md#tekniset-tiedot); tarkista mitat pumpusta ennen leikkausta. Keskitysreikä
   **Ø127**, ei Ø125 (Eatonin oma kannake: Ø127,05–127,15). Mallina voi käyttää
   [FB-C4-10:n mittoja](../p2-variable-pump.md#eatonin-jalkakannake-fb-c4-10). Kohdistus ks.
   [Pumpun kohdistus](../p2-variable-pump.md#pumpun-kohdistus).
3. **Imulinja.** 50 mm:n letku 2":n SAE code 61 -laipalla pumpun imuaukkoon (2" = 50,8 mm, ei
   supistusta); palloventtiili säilyy linjassa. Säiliön päässä: hitsattava muhvi →
   90°:n kulma → palloventtiili → letkukara [omistaja 2026-10-28], ks. [hankintalista](../../procurement.md).
4. **Kotelovuoto.** Ylimmästä vuotoportista oma letku (vähintään noin 1/2") säiliöön öljypinnan
   alle. **Ei yhteiseen paluulinjaan.**
5. **Painelinja.** Pumpulta FXDC:lle (linjarungossa) ja siitä CETOP-pohjalaatan P-porttiin.
   VPR3 ja OD15 irrotetaan.
6. **LS-linja.** Pumpun lähdöstä Ø0,8 mm:n kuristin LS-porttiin; LS-portista T-haara ja
   2/2-magneettiventtiili (auki jännitteettömänä) säiliöön. Letkut 1/4".
7. **Sähköt ja ohjaus** (ESP32 PDM):
   - päälle: 2/2 kiinni ensin, sitten BAV-713 suuntaan
   - pois: BAV-713 keskelle, sitten 2/2 auki
   - **2/2 on auki aina, kun kaikki suuntaventtiilit ovat keskellä.** Muuten pumppu seisoo
     250 barissa nollatuotolla (noin 10 kW lämpöä).
8. **Öljy.** Järjestelmä huuhdellaan ja täytetään HVLP 32:lla ([päätös 2026-10-23](../../../decisions.md)).
   **Pumpun kotelo täytetään öljyllä ennen ensimmäistä käynnistystä.** Imulinjan palloventtiili
   auki ennen käynnistystä.
9. **Käyttöönotto ja säädöt** mittarilla 2G1, ks. [seuraava luku](#säätö-käyttöönotossa-ilman-virtausmittaria).
   Pumpun paineenrajoittimen tehdasasetus on 120 bar, joten se nostetaan 250 bariin ennen
   keulapotkurin täyttä käyttöä.

## Säätö käyttöönotossa ilman virtausmittaria

> Lisätty 2026-10-25 [arvio]. Pätevän henkilön pitää hyväksyä säätöjärjestys ja -arvot.

Kaikki säädöt voi tehdä painemittarilla **2G1** (CETOP-pohjalaatan P-linja, FXDC:n jälkeen,
[pressure-monitoring](../pressure-monitoring.md)). Nollavirtauksella FXDC:n yli ei ole painehäviötä,
joten 2G1 näyttää silloin pumpun lähtöpaineen.

| Säätö | Miten | Mittari |
|---|---|---|
| **Valmiustila (LS-paine-ero, noin 20 bar)** | 2/2 auki, BAV-713 keskellä: 2G1 näyttää valmiustilan paineen. Tehdasasetus, säädetään vain, jos lukema poikkeaa selvästi. | 2G1 |
| **Paineenrajoitin 120 → 250 bar** | 2/2 kiinni, BAV-713 keskellä: pumppu nousee asetuspaineeseen nollatuotolla. Säädetään pumpun säätöruuvista. Pidä jakso lyhyenä, koska tilassa syntyy noin 10 kW lämpöä. | 2G1 |
| **VMP varaventtiiliksi noin 270 bariin** | VMP:n pitää avautua vasta pumpun asetuksen yläpuolella, joten sitä ei voi säätää 250 barin pumpulla suoraan. Esim. pumpun asetus nostetaan hetkeksi noin 280 bariin, VMP säädetään 270 bariin ja pumppu palautetaan 250 bariin. **Pätevä henkilö tekee tämän.** | 2G1 |
| **Keulapotkurin virtaus (FXDC)** | Keulapotkuria ajetaan, ja 2G1:n lukema muunnetaan virtaukseksi Sleipnerin taulukolla (alla). Jos lukema jää selvästi alle 250 barin, FXDC rajoittaa virtausta liikaa ja asetusta nostetaan (`L`/`K`-malli) tai valitaan suurempi kiinteä asetus. | 2G1 |

**Painemittari toimii virtausmittarina,** koska keulapotkurin moottorin paine ja virtaus kulkevat
yhdessä: potkurin momentti kasvaa kierrosnopeuden neliössä. Sleipnerin taulukko U11:lle
[datalehti Side-Power SH Series v1.0.0 2017]:

| Paine moottorilla | Virtaus | Työntövoima |
|---|---|---|
| 158 bar | 26,2 l/min | 60 % |
| 211 bar | 30,2 l/min | 80 % |
| 264 bar | 33,8 l/min | 100 % |

- 250 barissa moottori ottaa arviolta noin 33 l/min (interpoloitu) [laskelma]. **Valitaan
  FXDC:n asetusalue T (31,45–42,55 l/min) tai V (38,25–51,75 l/min), ei S:ää.** S-alueen
  (25,5–34,5 l/min) huippu on kuvaajan mukaan noin 32 l/min, jolloin FXDC rajoittaisi virtausta ja
  moottorin paine jäisi noin 237 bariin. T- tai V-asetuksella FXDC ei rajoita virtausta, vaan toimii
  ylikierrossuojana, ja tarkka asetus ei vaikuta työntövoimaan. Noin 8 barin painehäviö jää silti,
  koska noin 33 l/min tarvitsee sen jo ennen kompensointia [datalehti Sun FXDC, kuvaajasta luettu].
  Siksi tarkkaa virtausmittausta ei tarvita.
- **Ylikierrossuojaa keulapotkuri ei tarvitse,** koska potkuri on niin syvällä, ettei se saa ilmaa
  lapoihin [omistaja 2026-10-26]. Pelkälle keulapotkurille FXDC:n voisi siis jättää pois (noin
  85–88 %). Tässä kytkennässä FXDC on kuitenkin pohjalaatan yhteisessä P-linjassa ja rajaa myös
  ankkurivinssin virtauksen, joten se pysyy, jos vinssi liitetään. Vaihtoehto, jossa virtaus
  rajataan vain vinssin asemalla: [aux-circuit-ls-onoff](aux-circuit-ls-onoff.md).
- 2G1 näyttää paineen pohjalaatalla, ja moottorilla paine on BAV-713:n ja letkujen häviön verran
  pienempi **⚠ häviö ei tiedossa, arviolta muutama bar**.
- **Ankkurivinssin** nopeus tarkistetaan sekuntikellolla ketjun nopeudesta, kun vinssi on kytketty.
- **Varmistus tarvittaessa:** virtauksen voi mitata ämpärillä ja sekuntikellolla vapaasta
  paluuletkusta (34 l/min täyttää 20 l:n astian noin 35 sekunnissa). Letku pitää kiinnittää
  tukevasti ja tehdä matalalla paineella; tätä ei yleensä tarvita.

## Vikatilat

- **Kela tai sähkö pettää:** LS on yhteydessä säiliöön, pumppu on valmiustilassa ja keulapotkuri
  ei toimi. Tilanne on turvallinen.
- **2/2 juuttuu kiinni BAV-713:n ollessa keskellä:** pumppu seisoo 250 barissa nollatuotolla,
  ja öljyyn menee arviolta noin 10 kW 1800 rpm:llä. Öljyn lämpötila- ja paineanturi havaitsevat
  tämän.
- **Paineenrajoitin jumittuu täydelle tuotolle:** VMP rajoittaa paineen, ja tilanne on sama kuin
  vakiotilavuuspumpulla (lämpöä).
- **Ankkurivinssi ja sähkökatko:** 2/2 aukeaa, pumppu menee valmiustilaan ja vinssi pysähtyy.
  Ankkurin pidon hoitaa vinssin jarru tai jarruventtiili, ei pumppu.
- **3/2 (jos asennettu) jää jännitteettömäksi keulapotkuria käytettäessä:** pumppu toimii
  kuormantuntona, ja keulapotkuri saa noin 230 bar (työntövoima noin 80 %). Ei vaarallinen.
- **Kotelovuotolinja tukkeutuu:** akselitiiviste voi vaurioitua. Linja viedään omana letkunaan
  säiliöön, ei yhteiseen paluulinjaan.

## Kustannusvertailu (arvio)

| | F1-61-reitti | PVH57-reitti |
|---|---|---|
| Pumppu | käytetty 100–300 € | 150 € (ostettu tori.fi:stä 2026-11-01; ilmoitushinta 190 €) |
| Tyhjäkierto | BPV-F1 noin 430 € + ALV | 2/2-magneettiventtiili ja kuristin, arviolta 100–200 € |
| Virtauksen rajoitus | VPR3 (olemassa) | Sun FXDC noin 83–89 $ (Hydrotech, USA, 2026-10-25, toimitus vasta 2027) ja linjarunko DAW/S **⚠ hinta ei tiedossa**; Suomen hinta Salhydrolta **⚠ ei tiedossa** |
| Akselikytkin | Spidex 48/60, noin 215 € + ALV | HRC 150 + Taper Lock 2012 -holkit, arviolta 80–120 € + ALV (päätös 2026-10-27) |
| Kannake (ei vielä tehty) | 10 mm:n teräslevy, laserleikkaus ja hitsaus, ISO 7653 | sama tapa, SAE C -reikäkuvio; painavampi pumppu voi vaatia lisätuennan |
| Tiivisteet (ikä) | – | ulkoiset O-renkaat, akselitiiviste vain jos vuotaa (halpa, hinta ei tiedossa); koko sarjaa 02-102244 (noin 853 $) ei tarvita, jos kunto on myyjän kertoma, ks. [Tiivistesarja](../p2-variable-pump.md#tiivistesarja) |
| Muuta | – | SAE-laippaliittimet, vuotoletku |
| Paluusuodatin | nykyinen OMTF112C10NA2 käy | ehdokas OMTF171F10NA1, noin 85 £ (ALV:n kanssa) jälleenmyyjällä; kannen reiän avarrus ja 1 1/4":n liitin, ks. [Paluusuodattimen vaihto](../p2-variable-pump.md#paluusuodattimen-vaihto-omtf171f10na1); tai linjasuodatin paluulinjaan nykyisen rinnalle, arviolta 100–250 € **⚠ ei tiedossa**, ks. [linjasuodatin](../p2-variable-pump.md#vaihtoehto-linjasuodatin-paluulinjaan-nykyinen-suodatin-jää) |

## Arkistoidut avoimet kysymykset

- [x] ~~Sun FXDC:n asetusvaihtoehto~~ T (31,45–42,55 l/min) tai V; `L` = ruuvisäätö, `K` = käsinuppi, kumpikin ±25 % [datalehti Sun FXDC 2026-10-26]
- [ ] Salhydro: FXDC:n hinta euroina ja toimitusaika; valurautaisen DAW/S-rungon hinta ja saatavuus (runkomalli selvitetty: DAW/S, T-5A, 3/4" BSPP; USA-hinnat ks. [vaihtoehdot](#kaksitiekompensoidun-virtauksensäätöventtiilin-vaihtoehdot))
- [x] Voiko VPR3:n B-portin tulpata: **ei**, B kytketään aina säiliöön tai toiselle toimilaitteelle [omistaja 2026-10-25], [datalehti VPR3]
- [ ] Ankkurivinssin moottori on Danfoss OMP 160 (151-0031) [omistaja 2026-10-27]; kierrostilavuus (noin 155,7 cm³ ⚠), käyttöpaine ja tyypillinen käyttöaika: ratkaisevat, tarvitaanko LS-linjaan 3/2-venttiili
- [x] ~~Sun: FXDC:n pienin paine-ero, jolla asetusvirtaus pysyy~~ noin 15–20 bar 30–40 l/min:n asetuksella, noin 10 bar ≤ 23 l/min:llä; kuvaajasta luettu [datalehti Sun FXDC 2026-10-26]
- [ ] Omistajat: onko keulapotkurin portaaton ohjaus tavoite (ratkaisee venttiilikokoonpanon: FXDC + LS-purku, LS + on/off vai PVG 32)
- [x] Omistajat: PVH57 vai F1-61 → **PVH57**, kaupat sovittu (päätös 2026-10-27); ostettu ja noudettu 150 € [omistaja 2026-11-01]
