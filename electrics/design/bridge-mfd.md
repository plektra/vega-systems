# Oma monitoiminäyttö komentosillalle

> **Tila:** Selvitys ja suositus, aloitettu 2026-11-08. **Ei päätetty.** Näyttö tulee
> komentosillan kattopaneeliin Simrad NSS evo3:n rinnalle [omistaja 2026-11-08], ks.
> [current-system 3.5](../current-system.md#35-komentosillan-kattopaneeli-lisätty-2026-11-08) ja
> [nmea2000-network 5.6a](nmea2000-network.md#56a-komentosillan-kattopaneeli-lisätty-2026-11-08).

## 1. Vaatimukset

Omistajan toiveet [omistaja 2026-11-08]:

- **Vaihdettavat näkymät (sivut):** jokainen kamera omalla sivullaan, hydrauliikan reaaliaikainen
  valvontakuva, tärkeimmät navigointimittarit ja muita näkymiä tarpeen mukaan.

Lisäksi ehdotan [arvio]:

- **Hälytykset näkyvät aina**, sivusta riippumatta (palkki ylälaidassa ja summeri), ja hälytyksen
  painallus vie oikealle sivulle.
- **Yövalaistus:** himmennys lähes pimeäksi ja punainen tai tumma teema, jotta näyttö ei sokaise
  ruorimiestä.
- **Käyttö märin käsin ja hanskoin:** sivujen vaihto fyysisillä painikkeilla tai kiertonupilla,
  kosketus lisänä.
- **Käynnistyy itsestään** suoraan näkymiin, kestää virran katkeamisen ilman korruptoitunutta
  muistikorttia, eikä vaadi näppäimistöä.
- **Ei turvallisuuskriittistä ohjausta pelkän näytön varassa.** PDM-lähtöjä voi ohjata näytöltä
  (vahvistuksella), mutta keulapotkuri, ohjaus ja hätäseis pysyvät johdotettuina.

## 2. Mitä on jo olemassa

| Osa | Tila | Lähde |
|---|---|---|
| Kioskinäyttö: Raspberry Pi, Openbox ja Chromium kioskitilassa; näyttää Signal K:n Node-RED-kojelaudan; komentosillan kamera `ffplay`-ikkunassa RTSP:llä; Touchegg-eleet | olemassa, Ansible-rooli `kiosk` | [vega-ansible](https://github.com/plektra/vega-ansible) (`roles/kiosk`), luettu 2026-11-08 |
| Frigate (kameratallennin, kohteiden tunnistus, Coral) NUC:lla (`santio`), kamera `bryga` | olemassa | sama (`roles/frigate`) |
| Signal K -palvelin, Grafana ja Signal K -datalähde Grafanaan | olemassa | [current-system 4](../current-system.md#4-valvonta-verkot-ja-tehonjako) |
| Kojelautakokeilut React / Next.js ja MUI (`dashboard-test`, `-test2`, `-test3`) | kokeiluja | paikalliset repot, luettu 2026-11-08 |

**Huom.:** `vega-ansible` on julkinen repo, ja kioskin `autostart.j2`-tiedostossa on kameran
RTSP-osoite tunnuksineen selväkielisenä. Salasana kannattaa vaihtaa ja siirtää Ansible Vaultiin
tai muuttujaan, kuten Frigaten asetuksissa on jo tehty (`{FRIGATE_RTSP_PASSWORD}`).

## 3. Vaihtoehdot

| | **A. Selainpohjainen: oma kuorisovellus ja valmiit web-sovellukset** (suositus [arvio]) | B. Pelkät valmiit sovellukset (KIP, Node-RED, Frigate) välilehtinä | C. Natiivisovellus (Qt/QML tms.) |
|---|---|---|---|
| Periaate | Kioskiselaimessa oma pieni web-sovellus: sivuvalikko, hälytyspalkki ja yötila. Sivuina omia näkymiä (hydrauliikka) ja upotettuja valmiita sovelluksia (mittarit, kartta, kamerat) | Chromium vaihtaa valmiiden sovellusten välillä | Kaikki itse koodattua |
| Työmäärä | kohtalainen; laajenee sivu kerrallaan | pienin | suurin |
| Hälytykset kaikilla sivuilla, yhtenäinen yötila, fyysiset painikkeet | ✅ | ❌ jokaisessa sovelluksessa omansa | ✅ |
| Hydrauliikan valvontakuva | oma SVG-sivu | Node-RED-kojelauta tai Grafana (kömpelö) | ✅ |
| Kamerat pienellä viiveellä | WebRTC (go2rtc, sisältyy Frigateen) | Frigaten käyttöliittymä | oma toteutus |
| Toimii puhelimella ja tabletilla samoin | ✅ | osittain | ❌ |
| Sopii olemassa olevaan | jatkaa kioskiroolia ja React-kokeiluja | jatkaa kioskiroolia | ei |

**Suositus [arvio]: A.** Kioski-Pi ja Chromium ovat jo olemassa. Oma kuorisovellus tuo
hälytyspalkin, yötilan ja sivujen vaihdon yhteen paikkaan, ja jokainen sivu voi olla joko oma tai
valmis sovellus. Sama sovellus toimii myös puhelimella, tabletilla ja kotona VPN:n kautta.

## 4. Ehdotettu toteutus

### 4.1 Arkkitehtuuri

```
Kattopaneeli                               Konehuone
┌──────────────────────────────┐           ┌──────────────────────────────────────┐
│ Näyttö (HDMI, 24 V)          │           │ Pi 5: Signal K (+ CAN HAT → N2K)     │
│ Panel-Pi: Chromium kiosk ────┼─Ethernet──┤   KIP, Freeboard-SK, Node-RED        │
│   kuorisovellus (sivut)      │           │   kuorisovellus (staattiset tiedostot)│
│ Painikkeet / nuppi (USB HID) │           │ NUC: Frigate + go2rtc (WebRTC)        │
│ (valinnainen CAN HAT → N2K)  │           │ PoE-kytkin → kamerat                  │
└──────────────────────────────┘           └──────────────────────────────────────┘
```

- **Panel-Pi** (Raspberry Pi 5 tai nykyinen kioski-Pi) paneelin takana, syöttö 24 V → 5 V
  DIN-muuntimella samaan tapaan kuin konehuoneen Pi:llä. Se on pelkkä näyttöpääte, joten
  ohjelmistot ja tiedot pysyvät konehuoneen palvelimilla.
- **Kuorisovellus** on staattinen web-sovellus (esim. React, kuten kokeiluissa), jota Signal K
  -palvelin jakaa web-sovelluksena (Signal K webapp). Se tilaa tiedot Signal K:n
  WebSocket-rajapinnasta.
- **Kamerat:** Frigaten mukana tuleva go2rtc jakaa kamerat selaimelle WebRTC:llä pienellä viiveellä
  (**⚠ tarkista** käytössä olevasta Frigate-versiosta). Kamerasivulla näytetään pääsuoratoisto ja
  ruudukkosivulla kevyemmät alivirrat, jotta Pi ja verkko eivät kuormitu.

### 4.2 Sivut (ensimmäinen ehdotus)

| Sivu | Sisältö | Toteutus |
|---|---|---|
| **Navigointi** | nopeus (SOG/STW), suunta (COG/HDG), syvyys, tuuli, peräsinkulma, kierrokset, sijainti, AIS-lähimmät | oma mittarisivu tai KIP-kojelauta upotettuna |
| **Kartta** (valinnainen) | kartta, oma reitti, AIS-kohteet | Freeboard-SK (Signal K:n karttasovellus) upotettuna. Pääkarttana on navigointitietokoneen noin 20":n OpenCPN-näyttö ja Simrad [omistaja 2026-11-08], joten tämä sivu on lähinnä varalla |
| **Kamera: komentosilta** | yksi kamera koko ruudulla | go2rtc WebRTC |
| **Kamera: konehuone** | sama | sama |
| **Kamera: masto** | sama | sama |
| **Kamerat: ruudukko** | kaikki kamerat pieninä | alivirrat |
| **Hydrauliikka** | valvontakuva [kaavion](../../hydraulics/schematic.md) mukaan: pumput P1/P2/P3, paineet 1B2/2B1/2B2, öljyn lämpötila 3B1, venttiilien ja PVEH:n tila, joystickin asento; värit normaali / varoitus / hälytys [vaatimusten §10.1](../../hydraulics/requirements.md#101-anturit) rajoilla | oma SVG-sivu, arvot Signal K -poluista |
| **Kone** | kierrokset, öljynpaine, jäähdytysneste, käyttötunnit | oma mittarisivu (anturinode N-03) |
| **Sähkö** | akustot (SOC, virta, jännite), lataus, invertteri, maasähkö, käynnistysakut, TK-kiskon syötöt | oma sivu; Victron-tiedot Cerbo GX:n kautta |
| **Kytkimet** | PDM-lähdöt (valot, pumput, puhaltimet) tiloineen ja virtoineen; ohjaus vahvistuksella | oma sivu, Signal K → N2K 127502 |
| **Säiliöt ja olosuhteet** | polttoaine, vesi, harmaa- ja septivesi, lämpötilat | oma sivu |
| **Hälytykset** | aktiiviset ja kuitatut hälytykset, kuittaus ja vaiennus | Signal K -hälytykset (notifications) |

Sivuja lisätään sitä mukaa, kun anturit valmistuvat. Kuorisovelluksen sivulista kannattaa pitää
asetustiedostona, jolloin uuden sivun lisäys ei vaadi koodimuutosta.

### 4.3 Käyttö

- **Hälytyspalkki** kaikkien sivujen yllä (Signal K:n notifications); uusi hälytys soittaa summeria
  ja vilkuttaa palkkia; painallus vie asianomaiselle sivulle. Summeri myös ilman näyttöä
  (esim. PDM-lähtö), jotta hälytys kuuluu, vaikka näyttö olisi pimeänä.
- **Sivujen vaihto:** 4–6 painiketta paneelissa tai kiertonuppi ja painike. Toteutus helpoimmin
  pienellä USB-näppäimistönä näkyvällä ohjaimella (esim. ESP32-S3 USB HID), jolloin painikkeet
  ovat selaimelle näppäimiä. Kosketus toimii lisänä (Touchegg-eleet ovat jo käytössä).
- **Yötila:** himmennys ja tumma / punainen teema yhdellä painikkeella, ja automaattisesti
  auringonlaskun mukaan (Signal K laskee ajan sijainnista). Näytön taustavalon himmennys
  laitteiston kautta (**⚠ tarkista** valitusta näytöstä, esim. DDC/CI tai PWM).
- **Oletussivu** käynnistyksessä ja paluu siihen, kun näyttöön ei ole koskettu hetkeen
  (valinnainen).

### 4.4 Näyttölaite

| Vaatimus | Perustelu |
|---|---|
| Kirkkaus noin 800–1000 cd/m² tai enemmän [arvio] | komentosillan ikkunoista tulee päivänvaloa; tavallinen 250–300 cd/m²:n näyttö jää haaleaksi |
| IPS tai vastaava laaja katselukulma | näyttö on katossa, ja sitä katsotaan alaviistosta |
| Himmennys lähes nollaan | yöajo |
| 24 V:n syöttö tai DC-DC-muunnin; paneeliasennus | sähköjärjestelmä |
| Koko noin 10–15" [arvio] | kattopaneelin tila ja katseluetäisyys; Simrad 7" tai 9" vieressä |
| Kosketus valinnainen | katossa ylös kurottaminen on hankalaa; painikkeet ensisijaisia |

Mallia ei ole valittu; hinnat **⚠ ei tiedossa**. Teollisuus- ja venenäytöt (sunlight readable,
HDMI) ovat selvästi tavallisia näyttöjä kalliimpia.

### 4.5 Luotettavuus

- **Vain luku -tiedostojärjestelmä** (overlay) tai SSD Pi 5:lle, jotta virran katkeaminen ei
  korruptoi muistikorttia.
- **Vahtikoira:** jos Chromium kaatuu tai sivu jumittuu, se käynnistetään uudelleen. Laitteiston
  watchdog Pi:ssä.
- **Asennus Ansiblella** nykyisen `kiosk`-roolin jatkona; vaihdettava Pi saadaan toimimaan yhdellä
  ajolla.
- **Riippuvuus konehuoneen Pi:stä:** jos Signal K -palvelin kaatuu, mittari- ja hydrauliikkasivut
  tyhjenevät; kamerat toimivat edelleen NUC:lta, ja Simrad näyttää navigointitiedot suoraan
  N2K:sta. Jos tämä ei riitä, panel-Pi:hin lisätään oma eristetty CAN HAT ja paikallinen Signal K,
  jolloin navigointi- ja konesivut toimivat ilman konehuoneen Pi:tä ([nmea2000-network 5.6a](nmea2000-network.md#56a-komentosillan-kattopaneeli-lisätty-2026-11-08)).
- **Lämpö:** Pi 5 ja kirkas näyttö lämpenevät umpinaisessa kattopaneelissa → tuuletus.

## 5. Vaiheistus

1. **Nykyinen kioski kuntoon:** Chromium uusimpaan Raspberry Pi OS:ään, kameran tunnukset pois
   julkisesta reposta, kamera WebRTC:llä `ffplay`n tilalle.
2. **Kuorisovellus:** sivuvalikko, hälytyspalkki, yötila, painikeohjain; ensimmäisiksi sivuiksi
   kamerat ja KIP-mittarit.
3. **Hydrauliikan valvontakuva,** kun anturit 3B1 ja 2B1 ovat Signal K:ssa.
4. **Sähkö, kone ja kytkimet,** kun Cerbo GX, anturinode ja PDM:t ovat käytössä.
5. **Näyttölaite ja paneeli** valitaan, kun kattopaneelin mitat ovat tiedossa.

## 6. Avoimet kysymykset

- [ ] Omistajat: selainpohjainen kuorisovellus (suositus A) vai pelkät valmiit sovellukset (B)?
- [ ] Panel-Pi: nykyinen kioski-Pi vai uusi Pi 5; oma CAN HAT ja paikallinen Signal K varalle?
- [ ] Näytön koko, kirkkaus ja malli; kosketus vai pelkät painikkeet
- [ ] Sivujen järjestys ja oletussivu; mitä muita sivuja tarvitaan
- [ ] Hälytyssummerin paikka ja ohjaus (näytön kautta vai PDM-lähtö)
- [ ] Frigaten versio ja go2rtc:n WebRTC-tuki; kameroiden alivirrat
- [ ] **Kameran salasana `vega-ansible`-repossa:** vaihto ja siirto Ansible Vaultiin
