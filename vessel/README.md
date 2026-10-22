# Vega — alustiedot

Usean järjestelmän tarvitsemat yhteiset tiedot. Järjestelmäkohtaiset tiedot ovat kunkin
järjestelmän kansiossa ([hydraulics](../hydraulics/), [electrics](../electrics/)).

Lähteet: `[perustiedot]` ja `[blogi VVVV-KK-PP]` viittaavat Plektra-blogiin
(<https://plektra.github.io>, repo `plektra/plektra.github.io`); `[omistaja VVVV-KK-PP]` on
omistajien suoraan antama tieto.

## Alus

| Parametri | Arvo | Lähde |
|---|---|---|
| Nimi | Vega | |
| Tyyppi | Teräsrunkoinen hinaaja, muutettu vapaa-ajan käyttöön | [perustiedot] |
| Rakentaja / vuosi | Borgå Mekaniska Verkstad, 1912 | [perustiedot] |
| Pituus | 16,15 m | [perustiedot] |
| Leveys | 4,16 m | [perustiedot] |
| Syväys | 1,97 m | [perustiedot] |
| Uppouma | **⚠ ei tiedossa** | |
| Kotisatama | Laivalahti, Helsinki (ollut myös Saimaalla) | [perustiedot], [blogi 2017-07-04] |
| Ohjauspaikka | Yksi ruori, komentosillan keskellä | [blogi 2017-04-19] |
| Peräsin | Yksi peräsin; mitat **⚠ ei tiedossa** | |
| Keulapotkuri | Side-Power SH240-U11 (hydraulinen), 250 mm:n tunneli, asennettu 2017 | [blogi 2018-11-12] |

## Voimansiirto

| Kohde | Arvo | Lähde |
|---|---|---|
| Pääkone | Caterpillar 3126B, asennettu 2012. Teho **säädetty 350 hv:hen** omistajan muistin mukaan (blogissa 420 hv, joka on luultavasti mallin nimellisteho) **⚠ tarkista** koneen tyyppikilvestä tai Caterpillar-huollosta | [perustiedot], [omistaja 2026-10-22] |
| Kierrosalue | Tyhjäkäynti (ks. alla) – ~2500 rpm, matka ~1800 rpm | [blogi 2018-11-12] |
| Vauhtipyörä / kytkinkoppa | SAE 11-1/2 -vauhtipyörä, luultavasti SAE #3 -koppa, sovitelaippa SAE 14:ään | [blogi 2021-02-08] |
| Vaihteisto (alkuperäinen) | Masson RSD200 (1976), poistettu | [blogi 2019-01-24] |
| Vaihteisto | Advance 300, ~5,4:1, **asennettu ja linjattu** (2026) | [blogi 2021-02-08], [omistaja 2026-10-21] |
| Vaihteiston PTO | 1:1, ensiöakselilta (pyörii vapaalla), ei omaa kytkintä, 0,044 kW/rpm (≈ 420 Nm), Ø48 mm:n kiila-akseli | [omistaja 2026-10-21] |
| Akselin laakeri | Uusi laakeripukki potkuriakselille | [omistaja 2026-10-21] |
| Koneen tilanne | Asennetaan takaisin ja linjataan vaihteistoon (lokakuu 2026) | [omistaja 2026-10-21] |
| Koneen kiinnitys | Sekä vaihteisto että kone jäykästi runkoon | [blogi 2021-02-08] |
| Potkuri | Oikeakätinen | [blogi 2019-01-24] |

### Tyhjäkäyntikierrokset

**Tyhjäkäynti on noin 700 rpm** [omistaja 2026-10-22] (**⚠ tarkista** mittaamalla, kun kone käy).
Vuoden 2018 blogissa mainittu noin 800 rpm oli siis yläkanttiin. 700 rpm sopii myös verkosta
löytyneisiin tietoihin (haettu 2026-10-22):

- Scribdissä olevassa 3126B:n esitteessä on **700 rpm**, mutta on epäselvää, mihin teholuokkaan se
  liittyy. ([lähde](https://www.scribd.com/document/832207648/3126B))
- Kahden 3126B:n omistaja kertoo tyhjäkäynnin olevan **noin 680 rpm**, ja "low-RPM"-kytkimellä noin
  540 rpm. ([lähde](https://forums.ybw.com/threads/low-rpm-toggle-switch.584153))
- Muissa Caterpillarin merimoottoreissa tyhjäkäynti on **ohjelmoitavissa 550–750 rpm:iin**
  moottorinohjaimesta Cat ET -huoltotyökalulla.
  ([lähde](https://www.cat.com/en_US/products/new/power-systems/marine-power-systems/commercial-propulsion-engines/18408926.html))

PTO-pumpun mitoitus riippuu tyhjäkäynnistä suoraan: 700 rpm:llä tarvitaan noin 51 cm³:n pumppu, ks.
[hydraulics/design/p2-pump-options.md](../hydraulics/design/p2-pump-options.md#herkkyys-tyhjäkäyntikierroksille).
Vahvista lukema mittaamalla, kun kone käy, esim. Signal K:n moottoritiedoista. Caterpillar-huolto
voi todennäköisesti nostaa ohjelmoitua tyhjäkäyntiä tarvittaessa.

## Sähköjärjestelmän perustiedot

Tarkemmin: [electrics/current-system.md](../electrics/current-system.md).

| Kohde | Arvo | Lähde |
|---|---|---|
| DC-jännite | 24 V (päätelty 24 V:n hydrauliikan varapumpusta) **⚠ tarkista** | [blogi 2018-11-12] |
| Koneen laturi | 65 A | [blogi 2017-07-04] |
