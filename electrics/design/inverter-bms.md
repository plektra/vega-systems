# Invertterilaturi ja BMS: yhteensopivuus

> **Tila:** Selvitys, aloitettu 2026-10-31. Ei päätöstä. Hinnat on haettu verkkokaupoista ja
> keskustelupalstoilta 2026-10-31. Dollarihinnat on muunnettu kertoimella noin 0,9 €/USD (**⚠ arvio**).
> Ennen tilausta arvot tarkistetaan valmistajilta.

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
| Riittävä virta | Invertteri noin 160 A, P3 noin 100 A, muut 24 V:n kuormat hetkellisesti 50–90 A: yhteensä noin 300–350 A ([house-battery.md](house-battery.md)) |
| Valvonta | Kennojännitteet, varaustila ja hälytykset Signal K:hon |

**Kahden akun erityispiirre:** jos toinen akku katkaisee, koko kuorma siirtyy toiselle. Jos kumpikin
BMS kestää vain 200 A, noin 260 A:n kuorma (invertteri ja P3) laukaisee myös jäljelle jääneen
akun. Lisäksi yksi MB31-akku (314 Ah) kestää kennojen puolesta jatkuvasti vain noin 157 A (0,5 C,
[house-battery.md](house-battery.md#2-itse-kootut-kennot)). **Kun vain toinen akku on käytössä,
kuormaa on siis rajoitettava BMS:stä riippumatta**, esim. invertterin purkuvirran rajalla (DVCC)
ja niin, ettei invertteriä ja P3:a käytetä täysillä yhtä aikaa [laskelma]. Vaihtoehtoisesti P3
syötetään käynnistysakuilta, jolloin ongelma pienenee selvästi ([dc-distribution.md 3.3](dc-distribution.md#33-vaihtoehto-p3-käynnistysakuilta-selvitetty-2026-10-31)).

## 2. BMS-vaihtoehdot

| | **JK BMS (esim. B2A8S20P)** | **REC (Q-BMS tai ABMS)** |
|---|---|---|
| Tyyppi | MOSFET: virta kulkee BMS:n läpi | Ohjaa erillistä kontaktoria; BMS ei kanna virtaa |
| Virta | 200 A jatkuva | Kontaktorin mukaan (esim. 300–500 A) |
| Victron-liitäntä | CAN-väylä Cerbo GX:n BMS-CAN-porttiin, protokolla "Victron CAN" (DVCC); CAN-H ja CAN-L voivat olla eri järjestyksessä kuin Victronin kaapelissa ([Victron-yhteisö](https://community.victronenergy.com/t/jk-bms-einbinden/30144), [Akkudoktor](https://akkudoktor.net/t/victron-multiplus-5000-gx-oder-cerbo-gx-an-jk-inverter-bms-v19/34579?page=2)) | CAN-väylä GX-laitteeseen: latausvirran ja -jännitteen rajat, purkuvirran raja ja varaustila (DVCC) ([Victron-yhteisö](https://communityarchive.victronenergy.com/questions/26455/rec-active-bms-for-victron-gx-how-many-contactors.html)) |
| Releet laturin säätimelle | Kuivakosketin **⚠ tarkista** valitusta mallista | Ohjelmoitavat releet (lataus, purku, hälytys); niillä katkaistaan Alpha Pro III:n Reg on ennen kontaktoria |
| Hinta / akku | noin 190–210 € ([Fruugo](https://www.fruugo.co.nz/smart-jk-b2a8s20p-with-bt-can-rs485-8s-24v-200a-lifepo4-li-ion-lto-battery-3s-8s-2a-active-balance-jk-b/p-331614392-731314084)) | 16S-mallin hinta noin 540 € ([Current Connected](https://www.currentconnected.com/item/rec-bms/)); 8S:n hinta **⚠ ei tiedossa**. Lisäksi kontaktori ja esivarauspiiri, hinnat **⚠ ei tiedossa** |
| Kahdelle akulle | **noin 400 €** | **noin 1 100 € ja kaksi kontaktoria** (**⚠ arvio**) |
| Plussat | Halpa, aktiivinen balansointi, Bluetooth | Veneisiin yleinen; kontaktori ei laukea lyhyistä virtapiikeistä (P3:n käynnistys); releet latauslähteille |
| Miinukset | 200 A:n raja ja käynnistysvirtapiikit (P3) voivat laukaista BMS:n; valmistajan tuki ja dokumentaatio heikko | Kallis; käyttäjät raportoivat kytkentäongelmia esivarauksen kanssa ([Victron-yhteisö](https://communityarchive.victronenergy.com/questions/83792/rec-active-bms-relay-for-contactor.html)) |

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

## 4. Kokonaishinnat [laskelma, ⚠ arviot]

Invertterilaturi, väylälaitteet ja kahden 8S-akun BMS. Kontaktorit, esivarauspiirit, kaapelit ja
akusto puuttuvat.

| Yhdistelmä | Hinta |
|---|---|
| A + REC (Mastervolt-kokonaisuus) | noin 3 126 + 230 + 1 100 ≈ **4 450 €** ja kontaktorit |
| B + REC | noin 1 700–2 400 + 300 + 1 100 ≈ **3 100–3 800 €** ja kontaktorit |
| **B + JK** | noin 1 700–2 400 + 300 + 400 ≈ **2 400–3 100 €** |
| C + JK | noin 1 518 + 400 ≈ **1 900 €**, jos 24/3000 hyväksyy pienen aggregaatin |

## 5. Suositus (ei päätös)

1. **Invertterilaturiksi Victron MultiPlus-II 24/5000/120-50 ja Cerbo GX (B).** Se on noin
   1 000–1 400 € halvempi kuin Mass Combi Ultra, tehoa on enemmän, BMS liittyy suoraan CAN-väylään,
   pieni aggregaatti todennäköisesti toimii PowerAssistin kanssa, ja tiedot näkyvät Signal K:ssa.
   Mastervolt on perusteltu vain, jos koko järjestelmä halutaan MasterBusiin (Alpha-laturi ja
   -säädin), jolloin BMS:n kytkentä on varmistettava Mastervoltilta.
2. **BMS:ksi REC ja kontaktorit, jos budjetti sallii; JK, jos ei.** RECin kontaktori ei laukea P3:n
   käynnistyspiikistä, ja sen releet pysäyttävät laturin ennen katkaisua. JK on noin 700 € halvempi,
   mutta silloin:
   - P3:n käynnistysvirta pitää tarkistaa JK:n piikkivirtarajaa vasten (P3:n tyyppikilpi **⚠ ei
     tiedossa**), ja
   - laturin säädin pysäytetään ennen katkaisua: Reg on -johdin JK:n kuivakoskettimelta (jos
     mallissa on sellainen) tai Wakespeed WS500 CAN-väylässä, ja Sterling APD24 lisäsuojana.
3. **Toinen laturi:** Prestolite ja Alpha Pro III (halvin) Reg on -ohjauksella, tai Wakespeed WS500,
   jos halutaan, että DVCC ohjaa myös laturia.
4. **Kummallakin BMS:llä** kuormaa rajoitetaan, kun vain toinen akku on käytössä (kohta 1).
5. **Ennen tilausta varmistettavat:** MultiPlus-II 24/5000:n pienin tulovirta PowerAssistin kanssa;
   valitun BMS:n releet tai kuivakoskettimet; 24/3000 GX:n BMS-CAN-portti, jos halvin vaihtoehto
   kiinnostaa.

## 6. Avoimet kysymykset

- [ ] Invertterilaturin valinta: Mastervolt Mass Combi Ultra vai Victron MultiPlus-II (24/5000 tai 24/3000 GX)?
- [ ] BMS:n valinta: REC ja kontaktorit vai JK?
- [ ] Victronin "Minimum input current limits": MultiPlus-II 24/5000:n ja 24/3000:n pienin tulovirta PowerAssistin kanssa
- [ ] Mastervolt: hyväksyykö Mass Combi Ultra MasterBus Digital Inputin "Stop charge" -tapahtuman, ja mikä on pienin tulovirran raja?
- [ ] REC 8S -BMS:n hinta ja sopiva kontaktori (virta, kelajännite 24 V, hinta)
- [ ] JK B2A8S20P: onko kuivakosketin latauksen estolle; CAN-kaapelin johdinjärjestys
- [ ] Onko MultiPlus-II 24/3000 GX:ssä BMS-CAN-portti?
- [ ] Säädin: Alpha Pro III Reg on -ohjauksella vai Wakespeed WS500 CAN-väylässä?
