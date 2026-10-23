# Hydrauliikan kaavio (suunniteltu kokoonpano)

> **Tila:** päivitetty 2026-10-23 (P2 = F1-61 + BPV, Spidex-kytkin, 50 mm imu). Lohkokaavio suunnitellusta järjestelmästä, ei ISO 1219 -piirrosmerkein.
> Yhtenäinen viiva = olemassa tai päätetty, katkoviiva = suunnitteilla tai vaihtoehto.
> Lähteet ja tarkemmat arvot: [current-system.md](current-system.md),
> [design/p2-pump-options.md](design/p2-pump-options.md), [design/oil-cooling.md](design/oil-cooling.md).
> Vanha kaavio (2018): [img/hydraulics-v3-2018.png](img/hydraulics-v3-2018.png).

## 1. Voimansiirto ja ohjauspiiri

```mermaid
flowchart LR
  ENG["CAT 3126B<br/>700–2400 rpm"]
  BELT["2 kiilahihnaa 1:1,24<br/>+ tukilaakeri"]
  TANK[("Säiliö<br/>Flowfit 100 l")]
  P1["P1 Salami 2PE16D<br/>16,6 cm³<br/>max 3000 rpm"]
  RPF3["RPF3<br/>etusija 20 l/min"]
  ORB["Orbitroli<br/>HKUS 160/4<br/>sis. paineenrajoitus"]
  CYL["Ohjaussylinteri<br/>+ hätäohitus A–B"]
  P3["P3 sähköpumppu<br/>24 V, 2,5 kW (vara)"]
  RET(["Paluu"])

  ENG -->|kampiakseli| BELT --> P1
  TANK -->|"imu 1#quot;"| P1
  P1 --> RPF3 -->|P| ORB
  ORB <-->|A / B| CYL
  TANK -.->|"imu 3/4#quot;"| P3
  P3 -.->|vastaventtiili| RPF3
  RPF3 -->|ylimäärä| RET
  ORB -->|"T, max 25 bar"| RET

  classDef planned stroke-dasharray: 5 5
  class P3 planned
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
- Varapumpun P3 kytkentä (asennettu?) **⚠ tarkista**
- Iskuventtiilit, öljynjäähdytin ja merivesihaara ovat suunnitteilla
