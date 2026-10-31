# Invertterilaturi ja BMS: yhteensopivuus

> **Tila:** Selvitys, aloitettu 2026-10-31. **Päätetty 2026-10-31: Victron MultiPlus-II 24/5000/120-50,
> Cerbo GX ja JK-BMS (kaksi, yksi kummallekin 8S-akulle)** [omistaja 2026-10-31, [decisions.md](../../decisions.md)]. Hinnat on haettu verkkokaupoista ja
> keskustelupalstoilta 2026-10-31. Dollarihinnat on muunnettu kertoimella noin 0,9 €/USD (**⚠ arvio**).
> Ennen tilausta arvot tarkistetaan valmistajilta. Päivitetty 2026-10-31: P3 käynnistysakuilla.

Tavoite: valita invertterilaturi ja käyttöakuston BMS niin, että ne toimivat yhdessä toisen laturin
säätimen kanssa. Lähtökohdat:

- Käyttöakusto kootaan **kahtena erillisenä 8S-akkuna** (EVE MB31 tai MB56), ja kummallakin on oma
  BMS ([house-battery.md](house-battery.md)). Optio kolmannesta akusta pidetään auki (päätös 2026-10-31).
- Toinen laturi: Prestolite 175 A ja **Mastervolt Alpha Pro III** -säädin, tai Mastervoltin oma
  laturi ([ac-power-source.md 2.5](ac-power-source.md#25-toisen-laturin-hintataso-haettu-2026-10-28)).
- Varalataus kannettavalla **Timco SS2200i** -aggregaatilla (1,8 kW eli noin 7,8 A, päätös 2026-10-31).
  Invertterilaturin tulovirran raja pitää saada **alle noin 7,5 A:n Power Assist / PowerAssist
  päällä**, jotta sauna aggregaatin kanssa onnistuu ([ac-power-source.md D](ac-power-source.md#d-kannettava-bensiiniaggregaatti-varalataukseen-selvitetty-2026-10-31)).
- Veneen valvonta on **Signal K** ([current-system.md 4](../current-system.md#4-valvonta-verkot-ja-tehonjako)).

**Turvallisuus:** BMS katkaisee akun vikatilanteessa. Ohjauksen varapumppu P3 ja tärkeät kuormat
eivät saa jäädä yhden BMS:n varaan ([dc-distribution.md 3](dc-distribution.md#3-tärkeät-kuormat-ja-vikatilanteet)).
Kokonaisuus tarkastutetaan pätevällä sähköasentajalla.

## 1. Mitä BMS:n pitää pystyä tekemään

| Toiminto | Miksi |
|---|---|
| **Ennakkovaroitus latauslähteille ennen katkaisua** | Jos BMS katkaisee akun laturin ladatessa, laturin jännite piikkaa (load dump) ja voi rikkoa elektroniikkaa. Laturi ja invertterilaturi pysäytetään ensin (Alpha Pro III: Reg on -johdin tai MasterBus "Stop charge"; invertterilaturi: väylä). Sterling APD24 on lisäsuoja |
| Latauksen esto alle 0 °C:ssa | LiFePO4 ei saa latautua pakkasella |
| Riittävä virta | Invertteri noin 160 A ja muut 24 V:n kuormat hetkellisesti 50–90 A: yhteensä noin 200–250 A. P3 (noin 100 A) on käynnistysakuilla (päätös 2026-10-31) |
| Valvonta | Kennojännitteet, varaustila ja hälytykset Signal K:hon |

**Kahden akun erityispiirre:** jos toinen akku katkaisee, koko kuorma siirtyy toiselle. Yksi MB31-akku
(314 Ah) kestää kennojen puolesta jatkuvasti noin 157 A (0,5 C, [house-battery.md](house-battery.md#2-itse-kootut-kennot)),
ja invertteri ottaa täydellä teholla noin 160 A. **Kun vain toinen akku on käytössä, invertterin
purkuvirta rajataan** (esim. DVCC) [laskelma]. P3:n siirto käynnistysakuille (päätös 2026-10-31,
[dc-distribution.md 3.3](dc-distribution.md#33-p3-käynnistysakuilta-päätetty-2026-10-31)) poisti
aiemman ongelman, jossa invertteri ja P3 yhdessä (noin 260 A) olisivat ylittäneet 200 A:n BMS:n.

## 2. BMS-vaihtoehdot

| | **JK BMS (esim. B2A8S20P)** | **REC (Q-BMS tai ABMS)** |
|---|---|---|
| Tyyppi | MOSFET: virta kulkee BMS:n läpi | Ohjaa erillistä kontaktoria; BMS ei kanna virtaa |
| Virta | 200 A jatkuva | Kontaktorin mukaan (esim. 300–500 A) |
| Victron-liitäntä | CAN-väylä Cerbo GX:n BMS-CAN-porttiin, protokolla "Victron CAN" (DVCC); CAN-H ja CAN-L voivat olla eri järjestyksessä kuin Victronin kaapelissa ([Victron-yhteisö](https://community.victronenergy.com/t/jk-bms-einbinden/30144), [Akkudoktor](https://akkudoktor.net/t/victron-multiplus-5000-gx-oder-cerbo-gx-an-jk-inverter-bms-v19/34579?page=2)) | CAN-väylä GX-laitteeseen: latausvirran ja -jännitteen rajat, purkuvirran raja ja varaustila (DVCC) ([Victron-yhteisö](https://communityarchive.victronenergy.com/questions/26455/rec-active-bms-for-victron-gx-how-many-contactors.html)) |
| Releet laturin säätimelle | Kuivakosketin **⚠ tarkista** valitusta mallista | Ohjelmoitavat releet (lataus, purku, hälytys); niillä katkaistaan Alpha Pro III:n Reg on ennen kontaktoria |
| Hinta / akku | noin 190–210 € ([Fruugo](https://www.fruugo.co.nz/smart-jk-b2a8s20p-with-bt-can-rs485-8s-24v-200a-lifepo4-li-ion-lto-battery-3s-8s-2a-active-balance-jk-b/p-331614392-731314084)) | 16S-mallin hinta noin 540 € ([Current Connected](https://www.currentconnected.com/item/rec-bms/)); 8S:n hinta **⚠ ei tiedossa**. Lisäksi kontaktori ja esivarauspiiri, hinnat **⚠ ei tiedossa** |
| Kahdelle akulle | **noin 400 €** | **noin 1 100 € ja kaksi kontaktoria** (**⚠ arvio**) |
| Plussat | Halpa, aktiivinen balansointi, Bluetooth; 200 A riittää, kun P3 on käynnistysakuilla | Veneisiin yleinen; kontaktori ei laukea lyhyistä virtapiikeistä; releet latauslähteille |
| Miinukset | 200 A:n raja (invertterin huippu yli 300 A jaetaan kahden akun kesken); valmistajan tuki ja dokumentaatio heikko | Kallis; käyttäjät raportoivat kytkentäongelmia esivarauksen kanssa ([Victron-yhteisö](https://communityarchive.victronenergy.com/questions/83792/rec-active-bms-relay-for-contactor.html)) |

Molemmat toimivat Mastervoltin kanssa vain releiden kautta (kohta 3). Victronin oma Lynx Smart BMS
ja VE.Bus BMS toimivat vain Victronin omien akkujen kanssa, joten ne eivät sovi itse koottuun akustoon.

## 3. Invertterilaturi ja BMS yhdessä

| | **A. Mastervolt Mass Combi Ultra 24/3500-100** | **B. Victron MultiPlus-II 24/5000/120-50 ja Cerbo GX** | **C. Victron MultiPlus-II 24/3000/70-32 GX** |
|---|---|---|---|
| Hinta | noin 3 126 € | noin 1 700–2 400 € ja Cerbo GX noin 300 € (290–340 USD; [Signature Solar](https://signaturesolar.com/victron-energy-cerbo-s-gx), [Shop Solar Kits](https://shopsolarkits.com/products/victron-cerbo-gx)) | noin 1 518 € (GX sisäänrakennettu) |
| Teho | 3500 W @ 40 °C | 4000 W (5000 VA) | 2400 W (3000 VA) |
| BMS:n ohjaus | Ei suoraa liitäntää muihin kuin Mastervoltin akkuihin. BMS:n releet → **MasterBus Digital Input** (77030900, noin 185 € ilman ALV:tä, [Blue Bottle Marine](https://www.bluebottlemarine.com/products/mastervolt-masterbus-digital-input.html)) → "Stop charge" -tapahtuma. Hyväksyykö Mass Combi Ultra tapahtuman **⚠ tarkista** Mastervoltilta | BMS:n CAN → Cerbo GX → DVCC ohjaa latausvirtaa ja -jännitettä ja pysäyttää latauksen | Kuten B, jos sisäänrakennetussa GX:ssä on BMS-CAN-portti (**⚠ tarkista**) |
| Alpha Pro III -säädin | Sama MasterBus-tapahtuma, kaikki samassa väylässä | BMS:n rele katkaisee Reg on -johtimen, tai säädin vaihdetaan Wakespeed WS500:aan (650–820 USD), joka liittyy CAN-väylään | kuten B |
| Pieni aggregaatti (tulovirta alle noin 7,5 A Power Assistin kanssa) | Säädettävä MasterLink MICC -paneelilla, yläraja DIP-kytkimillä ([MICC-ohje](https://www.chmarine.com/content/Mastervolt/MV70403105_Installation%20Manual.pdf)); pienin arvo **⚠ ei tiedossa** | PowerAssist päällä pienin tulovirta riippuu mallista. Käyttäjien mukaan 5 kVA:n MultiPlussa noin 3,9 A ([Victron-yhteisö](https://communityarchive.victronenergy.com/questions/81434/input-current-limit-multiplus-ii.html)), joten **todennäköisesti onnistuu** (**⚠ tarkista** Victronin taulukosta "Minimum input current limits") | Pienemmissä malleissa raja voi olla korkeampi: 48/3000-mallissa raportoitu 9,5 A ([Victron-yhteisö](https://community.victronenergy.com/t/48v-multiplus-ii-input-current-limit-from-ac-arbitrary-minimum-threshold/18675)). Jos 24/3000:n raja on yli 7,5 A, **sauna aggregaatin kanssa ei onnistu** |
| Signal K | MasterBus ei liity Signal K:hon suoraan (**⚠ tarkista**) | Venus OS (Cerbo GX) näkyy Signal K:ssa | kuten B |
| Kiukaan ja uunin samanaikaisuus | Kuormanhallinta tarvitaan | Kuormanhallinta tarvitaan | Kuormanhallinta tarvitaan; 2400 W ei riitä kiukaalle ja jääkaapille ilman marginaalia |

### 3.1 Mihin Cerbo GX tarvitaan (lisätty 2026-10-31)

MultiPlus-II:ssa ei ole CAN-liitäntää, joten se ei ymmärrä BMS:n viestejä suoraan. Cerbo GX on
väylien välinen ohjain:

1. **BMS → invertterilaturi (DVCC):** GX lukee BMS:n CAN-viestit (latausjännite, latausvirran ja
   purkuvirran rajat, latauksen esto) ja ohjaa niillä MultiPlus-II:ta VE.Busin kautta. Tämä hoitaa
   ennakkovaroituksen ennen BMS:n katkaisua ja purkuvirran rajauksen, kun vain toinen akku on
   käytössä (kohta 1). JK-BMS:n luotettava liitäntä on juuri CAN.
2. **Asetukset käytössä:** tulovirran raja (laituri 14 A, aggregaatti noin 7 A) vaihdetaan
   kosketusnäytöltä tai puhelimesta.
3. **Valvonta:** akusto, invertterilaturi ja lataus Signal K:hon (Venus OS) ja etänä VRM-portaaliin.

**Vaihtoehdot ilman Cerbo GX:ää** (**⚠ tarkista** ennen valintaa):

- **BMS:n releet MultiPlus-II:n aux-tuloihin** ("two-signal BMS" -asetus VEConfigure-ohjelmalla):
  latauksen ja purun esto toimii ilman GX:ää, mutta vain päälle/pois, ei virran rajoitusta.
  Edellyttää BMS:ää, jossa on kuivakoskettimet (JK **⚠ tarkista**). Tulovirran raja asetetaan
  esim. Digital Multi Control -paneelilla.
- **Venus OS Raspberry Pi:llä** ja MK3-USB-liitäntä MultiPlussaan sekä CAN-liitäntä Pi:hin
  BMS:ää varten. Halvempi, mutta Victron ei tue sitä virallisesti, ja Pi 5:n tuki **⚠ tarkista**.
- **Cerbo-S GX** on halvempi, mutta siinä ei ole BMS-CAN-porttia ([Signature Solar](https://signaturesolar.com/victron-energy-cerbo-s-gx)),
  joten se ei sovi JK:n CAN-liitäntään.

**Arvio:** Cerbo GX (noin 300 €) kannattaa, koska JK-BMS:n hallittu ohjaus ja purkuvirran rajaus
toimivat sen kautta luotettavimmin, ja se tuo Victronin tiedot Signal K:hon.

## 4. Kokonaishinnat [laskelma, ⚠ arviot]

Invertterilaturi, väylälaitteet ja kahden 8S-akun BMS. Kontaktorit, esivarauspiirit, kaapelit ja
akusto puuttuvat.

| Yhdistelmä | Hinta |
|---|---|
| A + REC (Mastervolt-kokonaisuus) | noin 3 126 + 230 + 1 100 ≈ **4 450 €** ja kontaktorit |
| B + REC | noin 1 700–2 400 + 300 + 1 100 ≈ **3 100–3 800 €** ja kontaktorit |
| **B + JK** | noin 1 700–2 400 + 300 + 400 ≈ **2 400–3 100 €** |
| C + JK | noin 1 518 + 400 ≈ **1 900 €**, jos 24/3000 hyväksyy pienen aggregaatin |

## 5. Suositus (päätetty 2026-10-31: vaihtoehto B ja JK)

1. **Invertterilaturiksi Victron MultiPlus-II 24/5000/120-50 ja Cerbo GX (B).** Se on noin
   1 000–1 400 € halvempi kuin Mass Combi Ultra, tehoa on enemmän, BMS liittyy suoraan CAN-väylään,
   pieni aggregaatti todennäköisesti toimii PowerAssistin kanssa, ja tiedot näkyvät Signal K:ssa.
   Mastervolt on perusteltu vain, jos koko järjestelmä halutaan MasterBusiin (Alpha-laturi ja
   -säädin), jolloin BMS:n kytkentä on varmistettava Mastervoltilta.
2. **BMS:ksi JK riittää nyt, kun P3 on käynnistysakuilla (päivitetty 2026-10-31); REC on varmempi,
   jos budjetti sallii.** JK on noin 700 € halvempi. RECin releet pysäyttävät laturin valmiiksi ennen
   katkaisua. JK:n kanssa:
   - laturin säädin pysäytetään ennen katkaisua: Reg on -johdin JK:n kuivakoskettimelta (jos
     mallissa on sellainen) tai Wakespeed WS500 CAN-väylässä, ja Sterling APD24 lisäsuojana.
3. **Toinen laturi:** Prestolite ja Alpha Pro III (halvin) Reg on -ohjauksella, tai Wakespeed WS500,
   jos halutaan, että DVCC ohjaa myös laturia.
4. **Kummallakin BMS:llä** kuormaa rajoitetaan, kun vain toinen akku on käytössä (kohta 1).
5. **Ennen tilausta varmistettavat:** MultiPlus-II 24/5000:n pienin tulovirta PowerAssistin kanssa;
   valitun BMS:n releet tai kuivakoskettimet; 24/3000 GX:n BMS-CAN-portti, jos halvin vaihtoehto
   kiinnostaa.

## 6. Avoimet kysymykset

- [x] Invertterilaturi: Victron MultiPlus-II 24/5000/120-50 ja Cerbo GX [omistaja 2026-10-31]
- [x] BMS: JK, kaksi kappaletta [omistaja 2026-10-31]
- [ ] **Ennen tilausta:** Victronin "Minimum input current limits": MultiPlus-II 24/5000:n pienin tulovirta PowerAssistin kanssa (tavoite alle noin 7,5 A Timco SS2200i:lle)
- [ ] JK-malli: B2A8S20P vai muu 8S-malli; onko kuivakosketin latauksen estolle (Alpha Pro III:n Reg on); CAN-kaapelin johdinjärjestys Cerbo GX:n BMS-CAN-porttiin
- [ ] Kahden JK-BMS:n yhteiskäyttö Cerbo GX:n kanssa: näkyvätkö molemmat, ja ohjaako DVCC pienimmän rajan mukaan (**⚠ tarkista**)
- [ ] Invertterin purkuvirran raja, kun vain toinen akku on käytössä (DVCC-asetus)
- [ ] Sterling APD24 laturin varasuojaksi
- [ ] Säädin: Alpha Pro III Reg on -ohjauksella vai Wakespeed WS500 CAN-väylässä? (MasterBusin "Stop charge" ei ole käytössä ilman Mastervoltin invertterilaturia)
