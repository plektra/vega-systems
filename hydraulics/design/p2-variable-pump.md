# P2 säätötilavuuspumppuna: Vickers PVH57 ja LS-ohjaus

> **Tila:** **PÄÄTETTY 2026-10-27: P2 on Vickers PVH57** (kaupat sovittu [omistaja 2026-10-27]); Parker F1-61
> -vaihtoehto on arkistoitu ([archive/p2-pump-options](archive/p2-pump-options.md)). **Venttiilikokoonpanon
> ykkösvaihtoehto on [PVG 32](aux-circuit-ls-clean-sheet.md)** (päätös 2026-10-27). Tämän dokumentin FXDC + LS-purku
> ja [LS + on/off](aux-circuit-ls-onoff.md) ovat varavaihtoehtoja; pumpun tiedot, kytkin, kannake, suodatus ja
> asennus pätevät kaikissa. Selvitys 2026-10-25, korjattu 2026-10-25 (asennusjärjestys; VPR3:n B-porttia ei saa tulpata; myyjän vastaukset kunnosta),
> 2026-10-26 (FXDC:n painehäviö ja asetus; paluusuodatin; puhtausvaatimus 250 barissa 16/14/12) ja 2026-10-27
> (akselikytkin HRC 150; pumppu päätetty) sekä 2026-10-28 (asennusmitat ja porttikoot Eatonin luettelosta: imu 2", ei 2 1/2"; huoltotiedote M-2206-S luettu kokonaan). Vertailut F1-61:een on jätetty perusteluiksi.
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
  [laskelma, ks. [p2-pump-options](archive/p2-pump-options.md#käyttäytyminen-eri-kierroksilla-parker-f1-061)].

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

**Hinta ja tila:** pumppu 190 €. Lisäksi tarvitaan FXDC, magneettiventtiili ja liittimet, mutta
BPV jää pois (ks. [kustannusvertailu](#kustannusvertailu-arvio)). **Päätös 2026-10-27:** P2 on PVH57,
ja kaupat on sovittu. F1-61-vaihtoehto on arkistoitu.

## Kumpi on monimutkaisempi: F1-61 vai PVH57

> Lisätty 2026-10-25. Vertailu on arvio, ei päätös.

Venttiilien ja ohjauksen määrä on reiteissä suunnilleen sama. Ero on pumpun vaatimuksissa ja
siinä, kuinka paljon järjestelmää pitää ymmärtää.

| | F1-61 + ohitusventtiili | PVH57 |
|---|---|---|
| Pumppu | yksinkertainen, kevyt (8,5 kg) | säädin, kotelovuotoletku, raskas (noin 36 kg **⚠ tarkista**) |
| Magneettiventtiilit | ohitusventtiili (BPV) ja OD15 | 2/2, ja vinssiä varten ehkä 3/2 |
| Virtauksen rajoitus | VPR3 (olemassa) | uusi FXDC |
| Ohjauslogiikka | BPV:n tilaa saa vaihtaa vain alle 20 barissa, joten tarvitaan paineanturi ja ohjain ([pressure-monitoring](pressure-monitoring.md)) | 2/2 suljetaan, kun jotain käytetään |
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
  **Ehdokas: OMTF171F10NA1** [omistaja 2026-10-26], ks. [Paluusuodattimen vaihto](#paluusuodattimen-vaihto-omtf171f10na1).
- **Kunto:** pumppu on arviolta 1980-luvun lopulta tai 1990-luvulta (ks.
  [Ikä](#ikä-ja-siihen-liittyvät-riskit)) ja uudelleen maalattu. Myyjän mukaan se on säilytetty
  lämpimässä öljyt sisällä, ruosteetta, ja akseli pyörii äänettömästi [myyjä 2026-10-25], joten
  kuntoriski on pienempi kuin aluksi arvioitiin. Tiivistesarjat ja korjaukset ovat silti
  kalliimpia, ja harvempi korjaamo tuntee sen.
- **Ymmärrettävyys:** vian sattuessa F1-61:n toiminta on helpompi päätellä. LS-ohjauslinja on uusi
  käsite.
- **Asennus:** pumppu on noin neljä kertaa painavampi, ja siinä on yksi letku enemmän.

**Mitä PVH57:llä saavutetaan:** lähinnä pienempi lämpö, kun keulapotkuria käytetään korkeilla
kierroksilla (arviolta 2–3 kW eikä noin 38 kW [laskelma]). Keulapotkuria käytetään lyhyitä hetkiä ja
yleensä satamassa matalilla kierroksilla, jolloin hyötysuhteella on vähemmän väliä (ks.
[p2-pump-options: Käyttöjakso](archive/p2-pump-options.md#käyttöjakso-miksi-hyötysuhteella-on-vähemmän-väliä-kuin-luulisi)).
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
  koska BAV-713 on on/off-venttiili (ks. [p2-pump-options, vaihtoehto E](archive/p2-pump-options.md)).

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
   [ac-power-source.md](../../electrics/design/ac-power-source.md), 2026-10-28).
4. **Paineen pito ilman virtausta,** esim. sylinterin pitäminen paineessa: pumppu lepää
   nollatuotolla, kun kiinteän pumpun koko tuotto menisi paineenrajoittimen yli.

### Mitä PVH57 ei muuta

- **Suurin työntövoima ei kasva:** pumpun säätöalueen yläraja on 250 bar.
- **Tyhjäkäynnin tuotto on sama,** noin 38 l/min 700 rpm:llä [laskelma].
- **Venttiilejä ei jää pois:** suunta- ja virtausventtiilit tarvitaan edelleen.

**Johtopäätös:** PVH57 on järkevä, jos järjestelmää aiotaan laajentaa (portaaton keulapotkuri,
useita samanaikaisia tai jatkuvia kuormia). Miten apupiiri rakennettaisiin alusta alkaen LS-lohkoventtiilillä:
[aux-circuit-ls-clean-sheet](aux-circuit-ls-clean-sheet.md); ilman venttiilipöytää on/off-venttiileillä:
[aux-circuit-ls-onoff](aux-circuit-ls-onoff.md). Nykyisillä tavoitteilla (on/off-keulapotkuri ja
ankkurivinssi) F1-61 riittää. Portaaton keulapotkuri on tärkein syy harkita PVH57:ää uudelleen.

## Ehdokas: Vickers PVH57C-LAF-1S-10-C12V-31 (tori.fi)

Ilmoitus: <https://www.tori.fi/recommerce/forsale/item/45217879>, **190 € tai tarjous** (tarkistettu
2026-10-25). Ilmoituksen teksti: *"Käyttämätön Vickers säätötilavuuspumppu. 57 cm3,
pyörimisuunta vastapäivään. Pumpun perään voidaan kytkeä toinen pumppu."*

- **Tyyppikilpi** (ilmoituksen kuvasta): Model Code `PVH57C LAF 1S 10 C12V 31`, Part No.
  **02-159964**, Made in U.S.A.
- **Kunto kuvien perusteella:** maalattu uudelleen tai kauttaaltaan (maalia kilven reunoilla ja
  pulttien kannoissa), ruostepilkkuja säädinlohkossa ja rungossa. Portit tulpattu. Akselissa ja
  tiivistepinnoissa ei näy vaurioita. "Käyttämätön" voi tarkoittaa varastossa ollutta tai
  kunnostettua.
- **Myyjän vastaukset** [myyjä 2026-10-25, omistajan välittämä]: akseli pyörii ilman ääniä;
  pumppu on säilytetty koko ajan lämpimässä tallissa; sisällä on öljyt, eikä ruostetta ole.
  Muuta myyjältä ei kysytä [omistaja 2026-10-25]: alkuperä, varastointiaika ja kunnostus jäävät
  tuntemattomiksi, ja säätimen asetus mitataan käyttöönotossa.

### Ikä ja siihen liittyvät riskit

**Valmistusvuosi ei ole tiedossa** **⚠ ei tiedossa**. Kilven tiedoista sitä ei voi lukea, ja
päivämääräkoodia ei ole tunnistettu. Arvio perustuu rakennenumeroon:

- Koodin **10** on rakennenumero. Huolto-ohje M-2210-S (rev. 2/93) kattaa sen.
- Vickersin huolto-ohjeessa, jonka revisio on 11/1997, kuvataan jo PVH57/63:n **rakenne 11**
  ([manualmachine.com](https://manualmachine.com/eaton/pvh63/350146-user-manual/), hakutuloksen
  tiivistelmä, ei luettu kokonaan).
- Kilvessä lukee pelkkä *Vickers* eikä Eaton. Tämä ei rajaa ikää, koska Eaton (osti Vickersin 1999)
  ja nyt Danfoss käyttävät Vickers-nimeä yhä.

Pumppu on siis **todennäköisesti 1980-luvun lopulta tai 1990-luvulta**, noin 25–40 vuotta vanha
[arvio]. Tarkemmin sen voi tarvittaessa kysyä Danfossilta sarjanumeron perusteella.

**Riskit, jotka liittyvät ikään eivätkä käyttöön:**

| Riski | Miksi | Mitä tehdään |
|---|---|---|
| Tiivisteiden vanheneminen | Akselitiiviste ja O-renkaat (nitriili) kovettuvat ja halkeilevat vuosikymmenten varastoinnissa, vaikka pumppua ei olisi käytetty | **Vaihda akselitiiviste ja O-renkaat ennen asennusta**, ks. [Tiivistesarja](#tiivistesarja) |
| Sisäinen korroosio | Jos pumppu on varastoitu ilman öljyä, sylinteriporaukset, männät ja säätimen karat voivat ruostua. Ruostepilkut säädinlohkossa ulkopuolella viittaavat kosteuteen | Katso porttien sisään, pyöritä akselia käsin; säätimen karan pitää liikkua vapaasti |
| Laakerit | Pitkä seisonta ilman pyörimistä voi jättää laakereihin kosteus- tai seisontajälkiä | Akselin pitää pyöriä käsin tasaisesti ilman kohtia, joissa se tarttuu tai rahisee |
| Säädin | Kara voi jumittua lakkaan tai ruosteeseen, jolloin pumppu ei palaa valmiustilaan | Tarkista käyttöönotossa paine ja valmiustila mittarilla 2G1 |
| Varaosat | Vanha rakenne voi poiketa nykyisestä | **PVH-sarjaa myydään yhä** (Danfoss/Vickers), ja PVH57:n tiiviste-, laakeri- ja mäntäsarjoja on saatavilla jälleenmyyjiltä ([hydraulic-supply.com](https://www.hydraulic-supply.com/877423.html)) **⚠ varmista sopivuus rakenteelle 10** |

### Tiivistesarja

Lähteet: hakutulosten tiivistelmät 2026-10-25; sivuja ei saatu avattua tästä ympäristöstä, joten
**⚠ tarkista koodi ja hinta toimittajalta** pumpun osanumerolla 02-159964 ja tyyppikoodilla.

| Koodi | Mitä | Lähde |
|---|---|---|
| **02-102244** (vanha koodi **02-102260**, myös C1AC14) | PVH57/63:n tiivistesarja. Vickersin huoltotiedote M-2206-S (PVH57/63, **rakenne 11**, rev. 11/1997) viittaa siihen: *"Available in double shaft seal kit 02-102244"*; erillinen akselitiiviste 513439 mainitaan kaksoistiivisteversiolle. Hinta noin **853 $** (Motion, tarjouspyyntö) | [M-2206-S (paro.nl)](https://paro.nl/library//storage/datasheets/Eaton/PVH57_M-2206-S22175617.pdf/datasheet.html), [Motion](https://www.motion.com/products/sku/01283726), [hydraulic-supply.com](https://www.hydraulic-supply.com/02-102244.html) |
| 02-346217 | Danfossin sivulla PVM-sarjan alla ("PVM series code B"); jälleenmyyjä mainitsee PVQ63:n. **Ei luultavasti tämän pumpun sarja.** | [Danfoss PowerSource](https://powersource.danfoss.com/products/pumps/industrial-pumps/medium-duty-open-circuit-piston-pumps/pvm-series-code-b-pumps/p/02-346217) |

- **Epävarmuus:** Vegan pumppu on **rakenne 10** ja yksinkertaisella akselitiivisteellä (`S`).
  Löydetty tieto koskee rakennetta 11, ja sarjasta puhutaan kaksoistiivisteen yhteydessä. Kysy
  Danfossin jälleenmyyjältä, sopiiko 02-102244 rakenteelle 10.
- **Hinta on noin nelinkertainen pumpun hintaan nähden.** Halvempi vaihtoehto: jos pumppu pyörii
  käsin tasaisesti ja sisältä on puhdas, vaihdetaan vain akselitiiviste ja ulkoiset O-renkaat
  (portit, laipat, säädin), jotka saa mitoilla tavallisina osina. Mitat tiivisteistä tai
  osaluettelosta **⚠ ei tiedossa**. Tämän arvioi hydrauliikkakorjaamo.
- **Mitä voi vaihtaa avaamatta pumppua** [arvio yleisen mäntäpumppurakenteen perusteella,
  **⚠ tarkista huolto-ohjeesta M-2210-S**]:
  - *Ilman purkua:* porttien ja laippojen O-renkaat, tulppien O-renkaat ja säätimen O-renkaat
    (säädin irrotetaan omilla ruuveillaan, mäntäryhmä ei aukea). Akselitiiviste vaihdetaan
    monissa mäntäpumpuissa ulkopuolelta kiilan ja lukkorenkaan irrotuksen jälkeen; PVH:n osalta
    tämä on tarkistamatta.
  - *Vaatii purun:* rungon ja venttiililohkon välinen tiiviste ja muut sisäiset tiivisteet.
  - **Avattua liitosta ei koota vanhoilla tiivisteillä.** Ne ovat painuneet muotoonsa ja vuotavat
    helposti uudelleen asennettuina. Jos pumppu avataan, liitoksen kaikki tiivisteet vaihdetaan.
    Avaamattomat sisäiset tiivisteet jätetään rauhaan: ne ovat suojassa, ja liikuttamaton tiiviste
    pitää yleensä paremmin kuin liikutettu.

**Arvio (päivitetty 2026-10-25 myyjän vastausten jälkeen):** ikä ei sinänsä estä käyttöä, koska
sarjaa valmistetaan yhä ja osia saa. Myyjän mukaan pumppu on säilytetty lämpimässä, sisällä on
öljyt eikä ruostetta, ja akseli pyörii äänettömästi. Silloin sisäisen korroosion ja laakerivaurion
riski on pieni, eikä pumppua ole syytä avata. **Koko tiivistesarjaa (02-102244) ei tarvita.**
Tiivisteiden ikä on yhä riski: akselitiiviste ja ulkoiset O-renkaat voivat olla kovettuneet, vaikka
pumppu on ollut öljyssä. Tarkista ostaessa, ettei akselitiivisteen ympärillä ole öljyä ja että
tiivisteen huuli ei ole halkeillut, ja vaihda ulkoiset O-renkaat liitäntöjä tehdessä. Akselitiiviste
vaihdetaan, jos se vuotaa koeajossa. Hydrauliikkakorjaamon kannattaa koeajaa pumppu ennen
asennusta.

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
s. 7, 8 ja 31 luettu kuvina; asennusmitat s. 20–22 luettu kuvina 2026-10-28). Pumppu on **mobiiliversio**: teollisuusversiossa on aina lisäkoodi
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
| Asennus | **akseli vaakaan** (*"Mounting attitude should be horizontal"*); pystyasennus vain erikoisversiona (lisäkoodi `057`, ylimääräinen vuotoportti), jota tässä pumpussa ei ole. Suora veto joustavalla kytkimellä; linjaus asennuspiirustuksen toleransseihin. **Kiertoasento akselin ympäri:** luettelo ei määrää sitä. **Korjaus 2026-10-28:** pääportit ovat venttiililohkon **päällä ja pohjassa**, eivät kyljissä. Luettelon piirustuksessa (oletettavasti R-pumppu) säädin on ylhäällä, 1":n lähtö päällä (näkymä A-A) ja 2":n imu pohjassa (alin näkymä on pohjakuva). Omistajan pumpussa (L) säädinpuolella ylhäällä on laippaportti, jota omistaja pitää imuna [omistaja 2026-10-28, kuva]: L-pumpun venttiililohko on eri osa kuin R-pumpun (M-2206-S s. 2), joten portit voivat olla toisin päin **⚠ tarkista reikäväleistä** (imu 77,8 × 42,9 mm, lähtö 52,4 × 26,2 mm). Vuotolinja aina **ylemmästä** vuotoportista, jotta kotelo pysyy täynnä | s. 21, 30, 31; M-2206-S |
| Paino | noin 36 kg (jälleenmyyjät) **⚠ tarkista** | jälleenmyyjät |
| Imuaukko | **2" SAE J518 code 61** -nelireikälaippa (reikäväli 77,77 × 42,88 mm, kierre `F`-mallissa 1/2-13 UNC; `M`-mallissa M12). **Korjaus:** jälleenmyyjien 2 1/2" oli väärin. Imu on venttiililohkon päällä tai pohjassa (ks. Asennus) **⚠ tarkista pumpusta** | s. 21–22 (*kuvana*) |
| Painelähtö | **1" SAE J518 code 61** -laippa (reikäväli 52,37 × 26,19 mm, kierre 3/8-16 UNC / M10×1,5) | s. 21–22 |
| LS-portti | SAE O-rengasportti 9/16-18 UNF (3/8":n putkelle); painemittariportti M10 (tulpattu) | s. 21 |
| Asennuslaippa | SAE C nelireikä: keskitysolake Ø127,00/126,95 mm, reiät Ø14,15–14,53 mm, reikäneliö 2 × 57,25 = **114,5 mm**; pumpun pituus laipasta takapäähän noin 293 mm (mitta C) | s. 21–22 |
| Akseli (koodi 1) | SAE C suora kiila (J744-32-1): **Ø31,75 mm**, kiila 7,93 mm, kiila-akselin pituus laipasta 56,0 mm | s. 20 |
| Säätöruuvit | painesäädin noin 28 bar/kierros; LS-paine-ero noin 14 bar/kierros (tehdasasetus 20 bar) | s. 21; M-2206-S s. 8 |
| Kotelovuoto | pakollinen vuotolinja säiliöön. Vuotoportti 3/4-16 UNF SAE O-rengas (1/2":n putkelle); luettelon piirustuksessa **kaksi**: alhaalla ja ylhäällä ("optional drain port"). Onko ylempi portti tässä pumpussa avattu, **⚠ tarkista pumpusta** | s. 21; M-2210-S |
| Käyttöönotto | kotelo täytetään öljyllä jonkin portin kautta ennen käynnistystä; ilmaus avaamalla lähtöliitintä; 5–10 min kuormittamatta, öljy ei saa olla maitoista | M-2206-S s. 7 |

### Sopivuus Vegaan [laskelma]

Oletukset: volumetrinen hyötysuhde 95 %, mekaaninen 90 %, tyhjäkäynti 700 rpm.

| Tarkistus | Tulos |
|---|---|
| Tuotto 700 rpm:llä | noin 38 l/min, enemmän kuin keulapotkurin 33,8 l/min ✅ |
| Momentti 250 barissa | noin 254 Nm; PTO noin 420 Nm ✅; HRC 150 (noin 600 Nm **⚠ vahvista**) riittää (tarve kertoimilla noin 430 Nm) ✅ |
| Pyörimissuunta | L ✅ |
| Kierrosluku | koneen 2400 rpm on tasan mobiiliversion rajalla, kun imupaine on vähintään 0 bar. Säiliö on noin 1 m pumpun yläpuolella ja imulinja 50 mm. Täydellä iskulla 2400 rpm:llä (noin 138 l/min) imupaine olisi kylmällä öljyllä arviolta 0…−0,03 bar. **Vegan käytössä täyttä iskua ei tule korkeilla kierroksilla**: ajossa pumppu on valmiustilassa ja keulapotkuria käytettäessä virtaus on rajattu noin 35 l/minuun. Luettelo ei kerro, saako pienemmällä iskulla pyöriä nopeammin **⚠ kysy Danfossilta**. |
| Laippa ja akseli | SAE C ja kiila-akseli: **ei ISO 7653 eikä 8×32×36**. Kannake suunnitellaan PVH57:lle; kytkimeksi HRC 150 kartioholkeilla (päätös 2026-10-27) [omistaja 2026-10-25, 2026-10-27] |
| Paino | noin 36 kg (F1-61 8,5 kg): kannake mitoitetaan tälle painolle ja tärinälle; reaktiomomentti noin 254 Nm on lähes sama kuin F1-61:llä (noin 250 Nm) [laskelma] |

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
  [p2-pump-options](archive/p2-pump-options.md#käyttäytyminen-eri-kierroksilla-parker-f1-061) [laskelma].
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
selvästi (ks. [oil-cooling](oil-cooling.md)).

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
- **Yhtäaikainen käyttö** (ankkurointi, S2 [requirements](../requirements.md)): vinssi ja keulapotkuri
  jakavat saman 34 l/min, ja matalamman paineen kuorma saa suurimman osan. Sama rajoitus on
  F1-61-suunnitelmassa.
- **Jos vinssi tarvitsee alle 34 l/min** (hitaampi nopeus), sen CETOP-paikkaan lisätään välilaatta-
  kuristin. Vinssitilassa pumppu pitää silloin edelleen vain noin 20 bar kuorman yläpuolella, joten
  lämpö pysyy pienenä.
- **Turvallisuus:** sähkökatkossa 2/2 aukeaa ja vinssi pysähtyy. **Ankkurin pito ei saa riippua
  pumpusta:** vinssissä pitää olla jarru tai jarruventtiili ([requirements §7](../requirements.md)).
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
| 3 | Kannake SAE C -nelireikälaipalle | F1-reitin ISO 7653 -kannakkeen sijaan (ei vielä tehty); sama tapa: 10 mm:n teräslevy, laserleikkaus ja hitsaus. Pumppu noin 36 kg; laippa Ø127 mm:n keskitys ja 114,5 mm:n reikäneliö, ks. [tekniset tiedot](#tekniset-tiedot) |
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
   Hydrauliikkakorjaamon koeajo kannattaa (ks. [Tiivistesarja](#tiivistesarja)).
2. **Kannake ja kytkin.** Kannake 10 mm:n teräslevystä laserleikkaamalla ja hitsaamalla SAE C
   -reikäkuviolle ja noin 36 kg:n pumpulle **⚠ tarkista paino**. HRC 150 (päätös 2026-10-27): navat
   ja Taper Lock 2012 -holkit 48 mm (PTO) ja 1 1/4" (pumppu) sekä elastinen välikappale. Linjaus kytkimen sallimiin rajoihin
   ([current-system §0](../current-system.md)) ja suojakotelo pyörivälle kytkimelle. Laipan mitat
   ks. [tekniset tiedot](#tekniset-tiedot); tarkista mitat pumpusta ennen leikkausta.
3. **Imulinja.** 50 mm:n letku 2":n SAE code 61 -laipalla pumpun imuaukkoon (2" = 50,8 mm, ei
   supistusta); palloventtiili säilyy linjassa. Säiliön päässä: hitsattava muhvi →
   90°:n kulma → palloventtiili → letkukara [omistaja 2026-10-28], ks. [hankintalista](../procurement.md).
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
8. **Öljy.** Järjestelmä huuhdellaan ja täytetään HVLP 32:lla ([päätös 2026-10-23](../../decisions.md)).
   **Pumpun kotelo täytetään öljyllä ennen ensimmäistä käynnistystä.** Imulinjan palloventtiili
   auki ennen käynnistystä.
9. **Käyttöönotto ja säädöt** mittarilla 2G1, ks. [seuraava luku](#säätö-käyttöönotossa-ilman-virtausmittaria).
   Pumpun paineenrajoittimen tehdasasetus on 120 bar, joten se nostetaan 250 bariin ennen
   keulapotkurin täyttä käyttöä.

## Säätö käyttöönotossa ilman virtausmittaria

> Lisätty 2026-10-25 [arvio]. Pätevän henkilön pitää hyväksyä säätöjärjestys ja -arvot.

Kaikki säädöt voi tehdä painemittarilla **2G1** (CETOP-pohjalaatan P-linja, FXDC:n jälkeen,
[pressure-monitoring](pressure-monitoring.md)). Nollavirtauksella FXDC:n yli ei ole painehäviötä,
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
| Pumppu | käytetty 100–300 € | 190 € (tori.fi) |
| Tyhjäkierto | BPV-F1 noin 430 € + ALV | 2/2-magneettiventtiili ja kuristin, arviolta 100–200 € |
| Virtauksen rajoitus | VPR3 (olemassa) | Sun FXDC noin 83–89 $ (Hydrotech, USA, 2026-10-25, toimitus vasta 2027) ja linjarunko DAW/S **⚠ hinta ei tiedossa**; Suomen hinta Salhydrolta **⚠ ei tiedossa** |
| Akselikytkin | Spidex 48/60, noin 215 € + ALV | HRC 150 + Taper Lock 2012 -holkit, arviolta 80–120 € + ALV (päätös 2026-10-27) |
| Kannake (ei vielä tehty) | 10 mm:n teräslevy, laserleikkaus ja hitsaus, ISO 7653 | sama tapa, SAE C -reikäkuvio; painavampi pumppu voi vaatia lisätuennan |
| Tiivisteet (ikä) | – | ulkoiset O-renkaat, akselitiiviste vain jos vuotaa (halpa, hinta ei tiedossa); koko sarjaa 02-102244 (noin 853 $) ei tarvita, jos kunto on myyjän kertoma, ks. [Tiivistesarja](#tiivistesarja) |
| Muuta | – | SAE-laippaliittimet, vuotoletku |
| Paluusuodatin | nykyinen OMTF112C10NA2 käy | ehdokas OMTF171F10NA1, noin 85 £ (ALV:n kanssa) jälleenmyyjällä; kannen reiän avarrus ja 1 1/4":n liitin, ks. [Paluusuodattimen vaihto](#paluusuodattimen-vaihto-omtf171f10na1); tai linjasuodatin paluulinjaan nykyisen rinnalle, arviolta 100–250 € **⚠ ei tiedossa**, ks. [linjasuodatin](#vaihtoehto-linjasuodatin-paluulinjaan-nykyinen-suodatin-jää) |

## Paluusuodattimen vaihto: OMTF171F10NA1

Omistajan ehdotus [omistaja 2026-10-26]: nykyisen OMTF112C10NA2:n tilalle saman sarjan
suurempi OMTF171F10NA1 lasikuituelementillä. Tiedot ovat jälleenmyyjien sivuilta (hakutuloksista;
sivuja tai OMT:n luetteloa ei saatu auki 2026-10-26), ks. [datasheets](../../datasheets/README.md).

| | Nykyinen OMTF112C10NA2 | OMTF112F10NA2 (vertailu) | **Ehdokas OMTF171F10NA1** |
|---|---|---|---|
| Elementti | selluloosa 10 µm, nominaalinen **⚠ tarkista** | lasikuitu 10 µm absoluuttinen | **lasikuitu** (epäorgaaninen kuitu) 10 µm absoluuttinen; vaihtoelementti CR171F10R |
| Virtaus, Phoenix | 100 l/min | 55 l/min | **157 l/min** |
| Virtaus, Oudshoorn | 150 l/min | 71–80 l/min (sivulla kaksi arvoa) | **200 l/min** |
| Liitäntä | 1" BSP | 1" BSP | **1 1/4" BSP** |
| Kannen reikä | Ø 86 mm | Ø 86 mm | **Ø 129 mm** |
| Upotussyvyys säiliöön | 150 mm | 150 mm | **244 mm** |
| Ohitusventtiili | 1,7 bar (Phoenix) / 3 bar (Oudshoorn) | sama | 1,7 bar (Phoenix) / 3 bar (Oudshoorn) **⚠ tarkista** |
| Pulttijako, pulttien määrä ja koko | **⚠ ei tiedossa** | sama | **⚠ ei tiedossa** |
| Korkeus kannen yläpuolella | **⚠ ei tiedossa** | sama | **⚠ ei tiedossa** |
| Hinta | noin 29 £ (Phoenix) | – | **84,70 £ ALV:n kanssa** (Phoenix 2026-10-26); elementin hinta **⚠ ei tiedossa** |

Jälleenmyyjien virtausarvot eroavat toisistaan, mutta ero on johdonmukainen (Phoenixin arvot noin
65–75 % Oudshoornin arvoista); erot johtuvat todennäköisesti eri painehäviö- tai
viskositeettioletuksista [arvio]. Vertailussa käytetään Phoenixin pienempiä arvoja.

**Virtaus riittää reilusti.** Suodattimen läpi kulkee apupiirin noin 33–38 l/min ja P1:n paluu
14–37 l/min, yhteensä enintään noin 75 l/min 1800 rpm:llä [laskelma, luvut tästä dokumentista ja
[p2-pump-options](archive/p2-pump-options.md)]. OMTF171F10NA1:llä marginaali on noin kaksinkertainen
(157 l/min), mikä on hyödyllistä kylmäkäynnistyksessä, kun öljy on paksua ja ohitusventtiili
avautuu helpommin [arvio]. Saman runkokoon lasikuituversio OMTF112F10NA2 (55 l/min) olisi liian
pieni, joten **runkokoon suurentaminen on perusteltu**.

**Paluulinja:** yhteinen paluulinja on 3/4" (myös EC100:n öljyliitännät ovat 3/4" BSP,
[oil-cooling](oil-cooling.md)), joten linjaa ei tarvitse suurentaa koko matkalta: riittää
supistus 3/4" → 1 1/4" BSP suodattimen liittimellä [arvio]. 75 l/min:n virtauksella 3/4":n
letkussa (sisähalkaisija noin 19 mm) nopeus on noin 4,4 m/s [laskelma], yli paluulinjan tavallisen
suositusarvon (noin 2–3 m/s) [yleistieto]; lyhyellä (< 0,5 m) linjalla painehäviö on silti pieni (ks.
[current-system §3](../current-system.md)). Jos paluulinja kootaan uudelleen jäähdyttimen kanssa,
1":n letku jäähdyttimeltä suodattimelle on halpa parannus [arvio].

**Säiliön kansi ja syvyys (mitattava veneellä):**

- **Reikä:** Ø 86 → Ø 129 mm eli säde kasvaa 21,5 mm. Avarrus onnistuu esim. reikäsahalla tai
  plasmaleikkurilla; vanhat pulttireiät eivät todennäköisesti osu uuteen laippaan, joten uudet
  reiät porataan ja kierteytetään tai tehdään läpipultein. Pulttijakoa ei löytynyt; sen saa OMT:n
  luettelosta, jälleenmyyjien STEP-tiedostoista tai suoraan suodattimen rungosta mittaamalla.
  Vanhat reiät jäävät mahdollisesti laipan tiivisteen alle tai tulpataan.
- **Tila kannella:** uuden laipan ulkohalkaisija **⚠ ei tiedossa** (selvästi yli 129 mm). Tarkista,
  ettei se osu virtauksensäätöventtiileihin, täyttö- ja huohotinkorkkiin tai kannakkeisiin, ja että
  painemittari saadaan samalla luettavampaan suuntaan ([current-system §4](../current-system.md)).
- **Upotussyvyys 244 mm** (nykyinen 150 mm): suodattimen alapään pitää olla öljypinnan alla myös
  pienimmällä öljymäärällä (muuten paluuöljy vaahtoaa ja sekoittaa ilmaa), mutta se ei saa osua
  pohjaan tai väliseinään, eikä paluuvirta saa suuntautua suoraan imu-ulosottoihin (P2:n 50 mm,
  P1:n 32 mm). **Säiliön syvyys kannesta pohjaan 365 mm** [omistaja 2026-10-27]. Suodattimen alapää jää
  siis noin 120 mm pohjan yläpuolelle, eli pohjaan se ei osu. Öljypinnan pitää pienimmälläkin
  öljymäärällä olla selvästi yli 120 mm pohjasta. Jos 100 litraa vastaa koko 365 mm:n syvyyttä
  (suora säiliö), 1 cm öljyä on noin 2,7 l, ja 80 litran täytöllä pinta on noin 290 mm pohjasta
  [laskelma, arvio]. Upotukselle jää silloin noin 170 mm, ja pienemmälläkin öljymäärällä (esim.
  60 l, noin 220 mm) noin 100 mm. **Syvyyden puolesta OMTF171 sopii** [arvio]. Tarkista vielä
  öljypinnan todellinen korkeus ja se, ettei suodattimen alapää suuntaa paluuvirtaa imu-ulosottoihin
  tai osu väliseinään.
- **Kannen paksuus ja jäykkyys** suuremman reiän ympärillä **⚠ tarkista** (säiliön tyyppi A/B/C
  ei ole tiedossa).

**Muut vaikutukset:** ohitusventtiilin asetus (1,7 tai 3 bar) lisää paluulinjan vastapainetta
enintään saman verran; orbitrolin T-linjan 25 barin raja ei ole vaarassa. U11:n vuotolinja
tehdään uusiksi suoraan säiliöön [omistaja 2026-10-27], joten vastapaine ei vaikuta sen koteloon.

**Suositus:** OMTF171F10NA1 sopii, jos säiliön mitat sallivat. Halvempaa saman rungon
vaihtoehtoa ei ole: OMTF112:n lasikuituelementti on liian pieni Vegan virralle. Jos kannessa ei ole
tilaa, ks. [linjasuodatin](#vaihtoehto-linjasuodatin-paluulinjaan-nykyinen-suodatin-jää).

### Vaihtoehto: linjasuodatin paluulinjaan, nykyinen suodatin jää

Omistajan huomio [omistaja 2026-10-26]: kannessa ei välttämättä ole tilaa isommalle suodattimelle,
ja uusi kansi pitäisi luultavasti teettää laserleikattuna. Vaihtoehtona nykyinen OMTF112C10NA2 jää
paikalleen, ja yhteiseen paluulinjaan lisätään linjamallinen lasikuitusuodatin. Malli ja hinta
**⚠ valitsematta**; luvut ovat arvioita.

**Paikka:** yhteiseen paluulinjaan jäähdyttimen (EC100) jälkeen ja ennen kannen suodatinta:

```
apupiirin paluu ─┐
                 ├─ EC100 (+ ohitus 3–4 bar) ─ UUSI linjasuodatin 10 µm lasikuitu ─ OMTF112C10NA2 ─ säiliö
orbitrolin T ────┘
U11:n ja PVH57:n vuotolinjat ─────────────────────────────────────────────────────────────── suoraan säiliöön
```

- **P1:n paluu kulkee aina uuden suodattimen läpi,** kun kone käy (14–37 l/min,
  [p1-steering-pump](p1-steering-pump.md)). Se puhdistaa säiliön öljyä jatkuvasti, vaikka PVH57
  olisi valmiustilassa lähes ilman virtausta [arvio].
- **Nykyinen suodatin jää toiseksi vaiheeksi** halvalla selluloosaelementillä. Siitä on hyötyä
  myös, jos linjasuodattimen ohitusventtiili aukeaa kylmällä öljyllä.
- **Vuotolinjat (U11 ja PVH57:n kotelo) suoraan säiliöön,** ei suodattimien läpi: kotelot eivät
  kestä paluulinjan vastapainetta.

**Mitoitus [arvio]:** 10 µm absoluuttinen lasikuitu, beta-arvo ilmoitettu (vähintään 200);
virtauskesto noin 100 l/min tai enemmän (yhteinen virta enintään noin 75 l/min, ks. yllä);
liitäntä 3/4"–1" BSP; sisäänrakennettu ohitusventtiili ja tukkeumaosoitin; tila elementin vaihtoon
kupin alla (tyypillisesti 10–15 cm) ja kiinnityskannake.

**Vastapaine:** kylmällä öljyllä jäähdyttimen ohitus (3–4 bar), linjasuodatin ja kannen suodatin
(ohitus 1,7 tai 3 bar) voivat nostaa paluupaineen noin 5–8 bariin [arvio]. Orbitrolin T-linjan
25 barin raja ei ole vaarassa; keulapotkurin paine-ero pienenee lämpimällä öljyllä vain noin
1 bar [arvio].

| | Uusi kanteen asennettava (OMTF171F10NA1) | Linjasuodatin, nykyinen jää |
|---|---|---|
| Säiliön kansi | reikä Ø 86 → Ø 129 mm, uudet pulttireiät; kansi ehkä uusittava (laserleikkaus) | ei muutoksia |
| Upotussyvyys | 244 mm; säiliön syvyys 365 mm riittää [arvio] | ennallaan (150 mm) |
| Virtauskesto | 157 l/min (Phoenix) | valitaan noin 100 l/min tai enemmän |
| Suodatusvaiheita | yksi | kaksi (lasikuitu + nykyinen) |
| Paluulinjan vastapaine | pienempi | hieman suurempi (yksi suodatin lisää) |
| Tila | kannella | paluulinjan varrella, kannake ja tila elementin vaihtoon |
| Hinta | 84,70 £ + mahdollinen uusi kansi **⚠ ei tiedossa** | suodatin **⚠ ei tiedossa** (arviolta 100–250 €) + liittimet |
| Huolto | yksi elementti | kaksi elementtiä |

**Suositus [arvio]:** jos kanteen mahtuu Ø 129 mm:n reikä ja 244 mm:n upotus ilman uutta kantta,
OMTF171F10NA1 on yksinkertaisempi (yksi suodatin, pienempi vastapaine). Jos kansi pitäisi
uusia, linjasuodatin on todennäköisesti halvempi ja nopeampi. Kumpikin valinta ratkeaa veneellä
tehtävillä mittauksilla (ks. avoimet kysymykset).

### Riittääkö nykyinen paperisuodatin?

Vaatimus riippuu pumpusta [luettelot, ks. [p2-pump-options](archive/p2-pump-options.md) ja
[Tekniset tiedot](#tekniset-tiedot)]:

| Pumppu | Puhtausvaatimus (ISO 4406) | Nykyinen OMTF112C10NA2 (selluloosa 10 µm nominaalinen) |
|---|---|---|
| **F1-61 (päätetty)** | 20/18/13 [Parker MSG30-8200 s. 80] | **todennäköisesti riittää** [arvio], ks. ehdot alla |
| PVH57 (selvitys), 250 bar | 16/14/12 [Eaton s. 31] | **ei riitä** [arvio]: vaatimus on noin 2–3 luokkaa tiukempi (jokainen luokka kaksinkertaistaa hiukkasmäärän) |

**F1-61:n kanssa** nykyinen suodatin kannattaa pitää [arvio], kunhan

- järjestelmä huuhdellaan ja uusi HVLP 32 lisätään suodattimen kautta (uusi öljy ei tynnyristä
  ole tavallisesti edes luokassa 20/18/13 [yleistieto]),
- huohotinkorkki vaihdetaan suodattavaan (esim. 3 µm), koska suurin osa liasta tulee säiliöön
  ilman mukana [yleistieto],
- elementti vaihdetaan käyttöönoton jälkeen (kokoamisessa syntynyt lika) ja sitten painemittarin
  mukaan,
- öljystä otetaan näyte hiukkaslaskentaan (ISO 4406) muutaman kymmenen käyttötunnin jälkeen;
  hinta **⚠ ei tiedossa**. Näyte kertoo varmasti, riittääkö suodatin.

Vegan käyttö keventää vaatimusta: P2 on suurimman osan ajasta ohitusasennossa matalalla paineella,
ja suurpaineinen käyttö (keulapotkuri, vinssi) on lyhytaikaista. Se ei kuitenkaan muuta
valmistajan vaatimusta [arvio].

**Auttaako tiheämpi elementin vaihto (esim. 100 h välein)?** Ei puhtausluokkaan [arvio,
yleistieto]. Paperielementti ei ole ongelma siksi, että se kuluisi, vaan siksi, että se päästää läpi
suuren osan 10 µm:n ja sitä pienemmistä hiukkasista jo uutena: nominaalisen selluloosaelementin
erotusaste (beta-arvo) 10 µm:llä on tyypillisesti vain noin 2 (noin puolet hiukkasista jää
kiinni yhdellä läpikululla), lasikuituelementin 200 tai enemmän (yli 99,5 %) [yleistieto].
PVH57:n vaatimus koskee nimenomaan pieniä, 4 ja 6 µm:n hiukkasia (luvut 16 ja 14), joita
paperielementti juuri päästää läpi. Öljyn puhtaus asettuu tasolle, jonka määräävät elementin
erotusaste ja säiliöön tulevan lian määrä, ei vaihtoväli. Uusi paperielementti suodattaa jopa
hieman huonommin kuin osittain likaantunut [yleistieto].

Vaihtoväli ratkaisee vain sen, ettei elementti tukkeudu: tukkeutunut elementti avaa
ohitusventtiilin, ja silloin öljy kulkee kokonaan suodattamatta. Lisäksi vesi ja kuuma öljy
heikentävät selluloosaa. **Suositus:** vaihto ensimmäisten käyttötuntien jälkeen, sitten
painemittarin (tai tukkeumaosoittimen) mukaan ja vähintään kerran vuodessa [arvio]. Vegan kone
käy alle 1000 h vuodessa ([vessel](../../vessel/README.md), [omistaja 2026-10-23]), joten 100 tunnin
väli tarkoittaisi enimmillään noin 10 elementtiä vuodessa ilman puhtaushyötyä [laskelma].

**PVH57:n kanssa** halvin välivaihe olisi lasikuituelementti nykyiseen runkoon, jos se sopii
(`F10`-elementti CR112F10R samaan runkoon **⚠ tarkista**). Elementin virta 55 l/min (Phoenix)
tai 71–80 l/min (Oudshoorn) jää kuitenkin tiukaksi: tyhjäkäynnillä suodattimen läpi kulkee noin
35 + 16,5 ≈ 52 l/min ja kylmällä öljyllä painehäviö kasvaa [laskelma]. Siksi PVH57-reitillä
suositus on OMTF171F10NA1 tai [linjasuodatin](#vaihtoehto-linjasuodatin-paluulinjaan-nykyinen-suodatin-jää)
nykyisen rinnalle.

## Avoimet kysymykset

- [x] Myyjältä: pyöriikö akseli tasaisesti (pyörii ilman ääniä), säilytys (lämmin talli), onko sisällä öljyä ja ruostetta (öljyt sisällä, ei ruostetta) [myyjä 2026-10-25]
- [x] ~~Myyjältä: alkuperä, varastointiaika, kunnostettu vai ei, onko säädin koskematon~~ ei kysytä enempää [omistaja 2026-10-25]; tarkistetaan paikan päällä ja koeajossa (säätimen asetus mitataan käyttöönotossa)
- [ ] Valmistusvuosi (sarjanumero kilvestä; myyjältä ei kysytä, Danfossilta voi kysyä tarvittaessa)
- [ ] Tiivistesarja: sopiiko 02-102244 (vanha 02-102260) rakenteelle 10 ja yksinkertaiselle akselitiivisteelle, hinta Suomesta; vaihtoehtona pelkän akselitiivisteen ja O-renkaiden mitat
- [ ] Danfoss (Vickers): saako PVH57-mobiilia pyörittää yli 2400 rpm pienemmällä iskulla; valmiustilan häviöteho; kotelon suurin paine
- [x] PVH57:n asennusmitat: laippa, imu 2", lähtö 1", vuoto 3/4-16 UNF, LS 9/16-18 UNF [Eatonin luettelo V-PUPI-TM008-E1 s. 20–22, 2026-10-28]. M-2206-S on osaluettelo eikä sisällä mittoja.
- [ ] Pumpusta: kumpi pääportti on imu (2" = reikäväli 77,8 × 42,9 mm, 1" = 52,4 × 26,2 mm), onko ylempi vuotoportti avattu, paino
- [x] ~~Sun FXDC:n asetusvaihtoehto~~ T (31,45–42,55 l/min) tai V; `L` = ruuvisäätö, `K` = käsinuppi, kumpikin ±25 % [datalehti Sun FXDC 2026-10-26]
- [ ] Salhydro: FXDC:n hinta euroina ja toimitusaika; valurautaisen DAW/S-rungon hinta ja saatavuus (runkomalli selvitetty: DAW/S, T-5A, 3/4" BSPP; USA-hinnat ks. [vaihtoehdot](#kaksitiekompensoidun-virtauksensäätöventtiilin-vaihtoehdot))
- [x] Akselikytkin PVH57:lle: HRC 150 + Taper Lock 2012 -holkit (päätös 2026-10-27)
- [ ] HRC 150: valmistajan luettelosta nimellismomentti, sallitut linjausvirheet ja pituus kannakkeen suunnitteluun; F- vai H-navat asennustilan mukaan
- [ ] Taper Lock 2012 -holkit 48 mm ja 1 1/4": koodit, hinta ja kiilauran syvyys 48 mm:n holkissa (PTO-akselin kiila)
- [x] Paluusuodattimen suodatusaste vs. 16/14/12 (aiemmin 17/15/13): nykyinen OMTF112C10NA2 on 10 µm, arviolta selluloosa nominaalinen, **ei riitä** sellaisenaan [omistaja 2026-10-26]
- [x] ~~Lasikuituelementti: virtauskesto, kun P1:n paluu kulkee samasta suodattimesta~~ OMTF112F10 (55 l/min) liian pieni; ehdokas OMTF171F10NA1 (157 l/min), ks. [Paluusuodattimen vaihto](#paluusuodattimen-vaihto-omtf171f10na1)
- [ ] Sopiiko lasikuituelementti CR112F10R nykyiseen OMTF112C10NA2:n runkoon
- [ ] Öljynäytteen hiukkaslaskenta (ISO 4406) käyttöönoton jälkeen: mistä ja hinta
- [ ] OMTF171F10NA1: beta-arvo, ohitusventtiilin asetus (1,7 vai 3 bar), pulttijako ja laipan ulkohalkaisija (OMT:n luettelo tai STEP-tiedosto), elementin CR171F10R hinta
- [ ] Linjasuodatin (jos kansi ei salli OMTF171:tä): malli, beta-arvo, virtauskesto noin 100 l/min, hinta; paikka ja kannake paluulinjassa
- [ ] Omistajat: uusi kanteen asennettava suodatin vai linjasuodatin (ratkeaa kannen mittauksilla)
- [x] Säiliön syvyys kannesta pohjaan: 365 mm [omistaja 2026-10-27]
- [ ] Veneellä: öljypinnan etäisyys kannesta pienimmällä öljymäärällä, imu-ulosottojen ja mahdollisen väliseinän paikka suodattimen kohdalla, tila kannella Ø 129 mm:n reiälle ja laipalle, nykyisten pulttireikien jako
- [x] Voiko VPR3:n B-portin tulpata: **ei**, B kytketään aina säiliöön tai toiselle toimilaitteelle [omistaja 2026-10-25], [datalehti VPR3]
- [ ] Ankkurivinssin moottori on Danfoss OMP 160 (151-0031) [omistaja 2026-10-27]; kierrostilavuus (noin 155,7 cm³ ⚠), käyttöpaine ja tyypillinen käyttöaika: ratkaisevat, tarvitaanko LS-linjaan 3/2-venttiili
- [x] ~~Sun: FXDC:n pienin paine-ero, jolla asetusvirtaus pysyy~~ noin 15–20 bar 30–40 l/min:n asetuksella, noin 10 bar ≤ 23 l/min:llä; kuvaajasta luettu [datalehti Sun FXDC 2026-10-26]
- [ ] Omistajat: onko keulapotkurin portaaton ohjaus tavoite (ratkaisee venttiilikokoonpanon: FXDC + LS-purku, LS + on/off vai PVG 32)
- [x] Omistajat: PVH57 vai F1-61 → **PVH57**, kaupat sovittu (päätös 2026-10-27)
- [x] Omistajat: apupiirin venttiilikokoonpano PVH57:lle → **PVG 32** ykkösvaihtoehto (päätös 2026-10-27)
