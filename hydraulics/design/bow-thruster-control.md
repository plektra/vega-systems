# Keulapotkurin portaaton ohjaus: PVEH:n ohjauselektroniikka

> **Tila:** selvitys ja suositus 2026-11-02, ei päätetty. Turvallisuuskriittinen: pätevän henkilön
> pitää tarkistaa sallintaketju, kytkentä ja vikatilat ennen käyttöönottoa.

Liittyy: [PVG 32 -selvitys: sähkö ja ohjaus](aux-circuit-ls-clean-sheet.md#ehdokas-danfoss-pvg-32-5-lohkoa-torifi),
[käsivipu (PVM)](pvg32-lever.md), [vaatimukset §10.2](../requirements.md#102-ohjaus),
[sähköjärjestelmä: ESP32-PDM](../../electrics/current-system.md#4-valvonta-verkot-ja-tehonjako).

## 1. Lähtötilanne

- Keulapotkuri (Side-Power SH240-U11) ohjataan **PVG 32:n lohkosta 1, jossa on PVEH 157B4024
  (24 V, sarja 0)** [päätös 2026-10-27], [kuvasta, ks. PVG 32 -selvitys](aux-circuit-ls-clean-sheet.md#ehdokas-danfoss-pvg-32-5-lohkoa-torifi).
  Venttiili on ostettu, ja PVE-liittimet tulevat sen mukana [omistaja 2026-11-02].
- P2 on PVH57 ilman PTO-kytkintä; ajossa pumppu on valmiustilassa noin 20 barissa
  [päätös 2026-10-23], [päätös 2026-10-27].
- Vegan DC-jännite on 24 V ([vessel/README.md](../../vessel/README.md)).

## 2. Mitä PVEH tarvitsee

PVEH:ssa on oma säätöelektroniikka ja karan asentoanturi (suljettu säätö). **Se ei tarvitse
erillistä venttiilivahvistinta tai PWM-virtaohjainta**, toisin kuin paljaat proportionaalikelat.
Se tarvitsee vain syötön ja ohjausjännitteen, jota kara seuraa.

| Asia | Arvo | Lähde |
|---|---|---|
| Syöttö U | 22–30 V (Vegan 24 V käy) | [datalehti PVG 32 520L0344 s. 15–18](../../datasheets/README.md) |
| Ohjaussignaali | **suhteessa syöttöön:** keskiasento 0,5 × U, täysi isku 0,25 × U (suunta 1) tai 0,75 × U (suunta 2) | sama |
| Vikavalvonta | kara pysähtyy ja vikasignaali aktivoituu, jos signaali on alueen 15–85 % × U ulkopuolella (myös johdon katketessa) | sama |
| Liitin | Hirschmann DIN, 4-napainen: syöttö, signaali, maa, vikasignaali | sama |
| Signaalitulon impedanssi | **⚠ ei tiedossa** (vaikuttaa potentiometrin arvoon) | tarkista 520L0344:stä |
| Virrankulutus | **⚠ ei tiedossa** | sama |
| Vikanastan tyyppi ja kuormitettavuus | **⚠ ei tiedossa** | sama |
| Kelpaako PWM suoraan signaaliksi | **⚠ ei tiedossa** | sama |
| Reaktioajat (keski → täysi, täysi → keski) | **⚠ ei tiedossa** | sama |
| Sarjan 0 PVEH:n nastajärjestys | **⚠ tarkista** liittimestä tai Danfossin ohjeesta | |

### Tärkein sudenkuoppa: signaalin on seurattava syöttöjännitettä

24 V:n järjestelmän jännite vaihtelee, latauksessa noin 28,8 V. Jos ohjain antaa kiinteät 12 V
"keskiasennoksi", venttiili näkee 0,417 × U eli kara on noin (0,5 − 0,417) / 0,25 ≈ **kolmanneksen
iskusta auki, ja potkuri pyörii itsestään** [laskelma]. Siksi ESP32:n kiinteä 0–3,3 V:n DAC ja
vahvistin eivät sellaisenaan kelpaa, vaan signaali tehdään PVEH:n omasta syötöstä.

## 3. Vaihtoehdot

| | A. Potentiometrijoystick suoraan | B. ESP32-PDM antaa signaalin | C. CAN-ohjattu PVE |
|---|---|---|---|
| Periaate | joystickin potentiometri samasta 24 V:n syötöstä kuin PVEH; liukuja suoraan signaalinastaan | ESP32:n PWM ohjaa pientä puolisiltaa, jonka käyttöjännite on PVE:n syöttö; RC-suodin tasoittaa lähdön → pulssisuhde × U | PVE vaihdetaan CAN-väyläiseen malliin |
| Seuraa syöttöä | itsestään | itsestään (pulssisuhde 25–75 %) | – |
| Toimii ilman ohjelmistoa | ✅ | ❌ | ❌ |
| Rampit, kuollut alue, useampi ohjauspaikka, kaukosäädin, autopilotti | ❌ (vain joystickin mekaniikka) | ✅ | ✅ |
| Kustannus | joystick ja muutama vastus | oma piirilevylohko ja ohjelmisto | uusi PVE; pelkkä PVEH uutena noin 670 € + ALV ([PVG 32 -selvitys](aux-circuit-ls-clean-sheet.md)), CAN-malli **⚠ hinta ei tiedossa** |
| Arvio | **suositus perusohjaukseksi** | lisätään myöhemmin tarvittaessa | ei tarvita |

Vaihtoehdossa B ESP voisi myös mitata syöttöjännitteen ja korjata kiinteää lähtöä sen mukaan, mutta
se on huonompi tapa: ohjelmistovirhe tai mittausvirhe avaa karan.

### Potentiometrin kytkentä (vaihtoehto A)

```
+24 V (PVE:n sallittu syöttö) ── R_s ──┬── potentiometri R_p ──┬── R_s ── 0 V
                                        └──── liukuja ──► PVEH signaali
```

- **R_s = R_p / 2 kummassakin päässä** rajaa liukujan alueen 0,25–0,75 × U [laskelma]. Esimerkki:
  5 kΩ:n potentiometri ja 2 × 2,4 kΩ → noin 0,245–0,755 × U.
- Ilman sarjavastuksia ääriasento menisi yli 85 %:n ja venttiili menisi vikatilaan.
- Jos potentiometrin pään johto katkeaa, signaali menee 0:aan tai U:hun, ja vikavalvonta pysäyttää
  karan.
- Potentiometrin arvon pitää olla selvästi pienempi kuin PVEH:n signaalitulon impedanssi
  (**⚠ ei tiedossa**), muuten keskiasento siirtyy.
- Joystickin pitää olla **jousipalautteinen**, jotta irti päästetty ohjain palaa keskelle.

## 4. Suositus [arvio]: suora joystick ja ESP32-PDM valvojana

```
Hätäseis ── hydrauliikan pääkytkin ── sallintarele (ESP32-PDM voi pudottaa) ──► PVEH:n 24 V:n syöttö
                                                                                │
                                         joystick (potentiometri + R_s) ◄───────┘
                                                │
                                                └── liukuja ──► PVEH signaali
PVEH vikasignaali ──► ESP32-PDM tulo ──► Signal K (hälytys)
joystickin liukuja (jakajan kautta) ──► ESP32 ADC ──► Signal K (käyttötieto)
```

- **Joystick ohjaa PVEH:ta suoraan johdotettuna.** Keulapotkuri toimii, vaikka ohjelmisto tai
  PDM olisi rikki.
- **Sallintaketjussa ovat hätäseis ja hydrauliikan pääkytkin.** PTO-kytkintä ei ole, eikä
  kierroslukitusta tarvita: PVH57 tuottaa vain tarvittavan virtauksen (keulapotkurilla noin
  35 l/min), ja koneen 2400 rpm on pumpun rajoissa, ks.
  [p2-variable-pump](p2-variable-pump.md#sopivuus-vegaan-laskelma).
- **ESP32-PDM voi lisäksi pudottaa sallinnan** hälytyksistä (esim. öljyn lämpötila tai imupaine,
  [vaatimukset §10.1](../requirements.md#101-anturit)). Se on lisäsuoja, ei ainoa suoja.
- ESP32 lukee vikanastan ja joystickin asennon ja vie ne Signal K:hon. Joystickin jännite pitää
  jakaa ESP:n ADC-alueelle; suhteellisuuden vuoksi myös syöttöjännite mitataan.
- **Käsivipu (PVM)** on varaohjaus veneen sisällä, jos sähköohjaus pettää, ks.
  [pvg32-lever.md](pvg32-lever.md).
- **Kaksi ohjauspaikkaa tai kaukosäädin myöhemmin:** kahta potentiometria ei voi kytkeä rinnan.
  Tarvitaan valintarele (vain yksi paikka kerrallaan) tai vaihtoehto B. Ohjauspaikkojen määrä on
  vielä auki ([vaatimukset §10.2](../requirements.md#102-ohjaus)).

## 5. Vikatilat

| Vika | Seuraus | Suoja |
|---|---|---|
| Sähkökatko tai hätäseis | Jouset palauttavat karan keskelle; potkuri pysähtyy ja pyörii vapaasti avoimen keskiasennon kautta | Sallintaketju katkaisee PVEH:n syötön |
| Joystickin tai signaalijohdon katkos | Signaali alueen 15–85 % ulkopuolella → kara pysähtyy, vikasignaali | PVEH:n vikavalvonta; hälytys Signal K:hon |
| Joystick jumittuu taipuneena | Potkuri jää pyörimään | Hätäseis; käyttäjä näkee potkurin toiminnan. Harkitse joystickia, jossa on keskiasentokytkin sallintaketjussa **⚠ ei päätetty** |
| Signaali ei seuraa syöttöä (väärä kytkentä, kiinteä lähde) | Kara aukeaa osittain ilman ohjausta | Kytkentä aina PVEH:n omasta syötöstä; käyttöönotossa tarkistetaan keskiasento kahdella syöttöjännitteellä |
| PVEH:n sisäinen vika, kara jumissa | Potkuri pyörii tai ei pyöri | Vikasignaali, hätäseis, venttiilin paineenrajoitin rajaa paineen |
| ESP32-PDM vikaantuu | Valvonta ja hälytykset puuttuvat; perusohjaus toimii | Sallintareleen kytkentä niin, ettei PDM:n vika estä hätäseisiä **⚠ suunnittele** |

## 6. Käyttöönotto

1. Mittaa sarjan 0 PVEH:n nastajärjestys ja tarkista arvot 520L0344:stä (§2:n avoimet rivit).
2. Kokeile PVEH 24 V:lla ja potentiometrilla ilman painetta: kara liikkuu, keskiasento pitää ja
   vikasignaali toimii (myös [PVG 32 -selvityksen koestus](aux-circuit-ls-clean-sheet.md#puhdistus-ja-koestus)).
3. Tarkista, että keskiasento pysyy 24 V:lla ja noin 28 V:lla.
4. Paineen kanssa: ensin pieni ohjaus, sitten täysi, kuten PVG 32 -selvityksen käyttöönotossa.

## 7. Avoimet kysymykset

- [ ] PVEH 520L0344: signaalitulon impedanssi, virrankulutus, vikanastan tyyppi, PWM-signaalin
      kelpoisuus, reaktioajat
- [ ] Sarjan 0 PVEH:n (157B4024) nastajärjestys
- [ ] Joystickin valinta: tyyppi, potentiometrin arvo, kotelointi (IP-luokka) ja keskiasentokytkin
- [ ] Ohjauspaikkojen määrä ja sijainnit ([vaatimukset §10.2](../requirements.md#102-ohjaus))
- [ ] Sallintareleen ja hätäseisin kytkentä sekä ESP32-PDM:n rooli siinä (pätevä henkilö tarkistaa)
- [ ] Omistajat: perusohjaus suoralla joystickilla (suositus) vai heti ESP32-signaalilla
