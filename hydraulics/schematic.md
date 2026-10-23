# Hydrauliikan kaavio (suunniteltu kokoonpano)

> **Tila:** päivitetty 2026-10-23 (P2 = F1-61 + BPV, Spidex-kytkin, 50 mm imu). Lohkokaavio suunnitellusta järjestelmästä, ei ISO 1219 -piirrosmerkein.
> Yhtenäinen viiva = olemassa tai päätetty, katkoviiva = suunnitteilla tai vaihtoehto.
> Lähteet ja tarkemmat arvot: [current-system.md](current-system.md),
> [design/p2-pump-options.md](design/p2-pump-options.md), [design/oil-cooling.md](design/oil-cooling.md).
> Vanha kaavio (2018): [img/hydraulics-v3-2018.png](img/hydraulics-v3-2018.png).
>
> **ISO 1219 -kaaviot** (2026-10-23, luonnos): arkki 1 ohjauspiiri valmis (v0.2), ks. alla. Arkit 2 (apupiiri)
> ja 3 (paluu ja jäähdytys) tulossa. Alla olevat Mermaid-lohkokaaviot säilyvät yleiskuvana.

## ISO 1219 -kaaviot (luonnos)

Piirretty ISO 1219-1:n piirrosmerkein ja ISO 1219-2:n periaattein: venttiilit lepoasennossa,
komponenttitunnus muotoa *piiri + tyyppi + numero* (P pumppu, M moottori, V venttiili, A toimilaite,
Z muu), osaluettelo alla. **Tila: luonnos, ei rakentamiseen.** Ohjaus on turvallisuuskriittinen:
pätevän henkilön pitää tarkistaa kaavio ennen rakentamista.

### Arkki 1: Piiri 1, ohjaus

![Ohjauspiiri ISO 1219 -merkein](img/schematic-1-steering.svg)

| Tunnus | Osa | Tiedot | Lähde |
|---|---|---|---|
| 1M1 | Pääkone CAT 3126B, 2 kiilahihnaa | välitys 1:1,24; kone 700–2400 rpm | [blogi 2017-07-04], [omistaja 2026-10-22] |
| 1P1 | Ohjauspumppu Salami 2PE16D-P28P1 | 16,6 cm³/r, max 3000 rpm, imupaine ≥ 0,7 bar abs, imuaukko 3/4" | [datalehti Salami 2PE], [omistaja 2026-10-23] |
| 1V5 | Imulinjan palloventtiili | täysiaukkoinen, auki ajossa; imu 25 mm × 3,2 m (ehdotus 32 mm) | [p1-steering-pump.md](design/p1-steering-pump.md) |
| 1V7 | P1:n vastaventtiili | ennen T-haaraa, jossa P1 ja P3 yhdistyvät | [omistaja 2026-10-23] |
| 1V1 | Kolmitievirtauksensäätöventtiili Marchesini RPF3 | vakiovirtaus CF 20 l/min orbitrolille pumpun kierroksista riippumatta, ylimäärä EF paluuseen; koko todennäköisesti 1/2" (linjat 1/2") **⚠ tarkista** | [datalehti RPF3] |
| 1V2 | Orbitroli M+S HKUS 160/4 | 158,4 cm³/r, avoin keskiasento, ei kuormantakaisinkytkentää; sis. paineenrajoitus 80–170 bar (asetus **⚠**), iskuventtiilit 140–220 bar; T max 25 bar | [datalehti HKUS] |
| 1V3 | Hätäohitus A↔B | käsiventtiili sylinterin vieressä, lepoasennossa kiinni | [blogi 2017-07-04] |
| 1A1 | Ohjaussylinteri ZS60350100, kaksitoiminen | männän Ø 60 mm, varren Ø 35 mm, isku 100 mm | [omistaja 2026-10-23], [blogi 2017-07-04] |
| 1P2, 1M2 | Varapumppu P3, sähkömoottori 24 V 2,5 kW | kytketty T-haaraan oman vastaventtiilin kautta [omistaja 2026-10-23]; kierrostilavuus **⚠ ei tiedossa** | [blogi 2017-04-01] |
| 1V4 | P3:n vastaventtiili | ennen T-haaraa → RPF3 | [omistaja 2026-10-23] |
| – | Piirin 1 painelinjat | **1/2"** (P1/P3 → RPF3 → orbitroli → sylinteri) | [omistaja 2026-10-23] |
| 1V6 | P3:n imun palloventtiili | imu 3/4" | [blogi 2017-04-10] |
| 1Z1 | Säiliö Flowfit 100 l | 80 l öljyä | [blogi 2017-07-04] |

**Kaaviota piirtäessä esiin tulleet kysymykset:**

- ~~P1:n painelinjan vastaventtiili~~: on olemassa (1V7) ennen T-haaraa [omistaja 2026-10-23].
- Orbitrolin iskuventtiilejä ja imuventtiilejä ei ole piirretty erikseen (orbitrolin sisällä).
- Painelinjat 1/2" [omistaja 2026-10-23]; paluulinjojen koot puuttuvat.

## 1. Voimansiirto ja ohjauspiiri

```mermaid
flowchart LR
  ENG["CAT 3126B<br/>700–2400 rpm"]
  BELT["2 kiilahihnaa 1:1,24<br/>+ tukilaakeri"]
  TANK[("Säiliö<br/>Flowfit 100 l")]
  P1["P1 Salami 2PE16D<br/>16,6 cm³<br/>max 3000 rpm"]
  RPF3["RPF3<br/>virtauksensäätö 20 l/min"]
  ORB["Orbitroli<br/>HKUS 160/4<br/>sis. paineenrajoitus"]
  CYL["Ohjaussylinteri<br/>+ hätäohitus A–B"]
  P3["P3 sähköpumppu<br/>24 V, 2,5 kW (vara)"]
  RET(["Paluu"])

  ENG -->|kampiakseli| BELT --> P1
  TANK -->|"imu 25 mm, 3,2 m<br/>(ehdotus 32 mm)"| P1
  P1 -->|"vastaventtiili, 1/2#quot;"| RPF3 -->|P| ORB
  ORB <-->|A / B| CYL
  TANK -->|"imu 3/4#quot;"| P3
  P3 -->|vastaventtiili| RPF3
  RPF3 -->|ylimäärä| RET
  ORB -->|"T, max 25 bar"| RET

```

## 2. Apupiiri: PTO-pumppu ja keulapotkuri

```mermaid
flowchart LR
  GB["Advance 300<br/>PTO 1:1, Ø48<br/>≤ 420 Nm"]
  CPL["Spidex 48/60<br/>98 Sh A"]
  TANK[("Säiliö")]
  P2["P2 Parker F1-61<br/>59,5 cm³"]
  BPV["BPV-F1 24 V<br/>käsiohitus<br/>jännitteetön = ohitus"]
  VPR3["VPR3 3/4#quot;<br/>35 l/min"]
  VMP["VMP 3/4#quot;<br/>paineenrajoitus<br/>250 bar"]
  UNL["2/2-patruunaventtiili<br/>jännitteettömänä auki"]
  BAV["BAV-713 4/3<br/>suunta"]
  SHOCK["Iskuventtiilit A/B<br/>~275 bar"]
  THR["Keulapotkuri<br/>SH240-U11<br/>240 kg"]
  RET(["Paluu"])

  GB --> CPL --> P2
  TANK -->|"imu 50 mm"| P2
  P2 <--> BPV
  BPV -->|"vuotolinja 1/4#quot;,<br/>öljypinnan alle"| TANK
  BPV -->|"3/4#quot;, 3–4 m"| VPR3
  VPR3 -->|P| UNL
  VPR3 -.-> VMP
  UNL -->|"kiinni = paine<br/>pohjalaatalle"| BAV
  BAV -.-> SHOCK
  SHOCK -.->|"A / B 1/2#quot;, 2 × 8,5 m"| THR
  BAV -->|"A / B 1/2#quot;, 2 × 8,5 m"| THR
  VPR3 -->|"B, ylimäärä"| RET
  UNL -->|"auki → T"| RET
  BAV -->|T| RET
  VMP -->|T| RET
  THR -->|"vuotolinja 1/4#quot;"| TANK

  subgraph MAN ["CETOP 3 -pohjalaatta, 4 paikkaa"]
    UNL
    BAV
    SHOCK
  end

  classDef planned stroke-dasharray: 5 5
  class SHOCK planned
```

Pohjalaatan paikat 2–4 ovat vapaana (esim. ankkurivinssi).

## 3. Paluu ja öljynjäähdytys

```mermaid
flowchart LR
  RET(["Paluut:<br/>orbitroli, RPF3,<br/>VPR3, 2/2, BAV-713, VMP"])
  COOL["Öljynjäähdytin<br/>Bowman EC100"]
  BYP["Ohitus 3–4 bar"]
  FILT["Paluusuodatin"]
  TANK[("Säiliö")]
  RWP["Merivesipumppu<br/>~70 l/min @ 650 rpm"]
  LIM["Virtauksenrajoitin<br/>30–40 l/min"]
  GBC["Merivaihteen<br/>jäähdytin"]
  EHX["Koneen<br/>lämmönvaihdin"]

  RET -->|nykyinen| FILT
  RET -.-> COOL -.-> FILT
  RET -.-> BYP -.-> FILT
  FILT --> TANK

  RWP --> GBC --> EHX
  RWP -.-> LIM -.->|merivesi| COOL
  COOL -.->|"palaa ennen koneen<br/>lämmönvaihdinta"| EHX

  classDef planned stroke-dasharray: 5 5
  class COOL,BYP,LIM planned
```

## Toimintatilat (apupiiri)

| Tila | BPV-F1 | 2/2-patruunaventtiili | BAV-713 | Mitä tapahtuu |
|---|---|---|---|---|
| Ajo | jännitteetön (ohitus) | jännitteetön, auki | keskellä | P2 pyörii mutta kiertää tyhjänä pumpun päädyssä; pieni jäähdytysvirtaus vuotolinjan kautta säiliöön (lämpö **⚠ ei tiedossa**) |
| Keulapotkuri valmiina (tyhjäkäynti) | jännitteellinen (vaihdettu 2/2:n ollessa auki, < 20 bar) | jännitteetön, auki | keskellä | P2:n öljy kiertää matalalla paineella säiliöön (~0,7 kW) |
| Keulapotkuri käytössä | jännitteellinen | jännitteellinen, kiinni | a tai b | Paine nousee pohjalaatalla; VPR3 rajaa virtauksen 35 l/min:iin; potkuri saa ~88 % työntövoimasta (~210 kg) |
| Kierroslukitus (> ~1000 rpm) | pakotetaan jännitteettömäksi (2/2 ensin auki) | pakotetaan jännitteettömäksi | estetty | Pumppu ohitukseen; hälytys, jos syöttö päällä yli ~1200 rpm |
| Sähkökatko | ohitus | auki | keskellä | Keulapotkuri ei toimi; käsiohitus vain kone sammutettuna |

## Avoimia kohtia kaaviossa

- VMP:n fyysinen paikka P-linjassa (VPR3:n P-portin ja pohjalaatan välissä?) **⚠ tarkista**
- Onko 2/2-patruunaventtiili pohjalaatan paineenrajoitusventtiilin kavitetissa **⚠ tarkista**
- ~~Varapumpun P3 kytkentä~~: P1 ja P3 yhdistyvät T-haarassa kumpikin oman vastaventtiilin kautta RPF3:lle [omistaja 2026-10-23]
- Iskuventtiilit, öljynjäähdytin ja merivesihaara ovat suunnitteilla
