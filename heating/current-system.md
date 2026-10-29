# Vega — lämmityksen nykytila ja tarpeet

> **Tila:** Runko, aloitettu 2026-10-29. Lämmitysjärjestelmä on suunnitteilla; laitteita ei ole
> valittu. Täydennä tietojen karttuessa.

## 1. Lämmönlähde ja jakelu

| Kohde | Arvo | Lähde |
|---|---|---|
| Lämmitystapa | Vesikiertoinen lämmitys, kiertovesipumppu 24 V (suunniteltu) | [omistaja 2026-10-29], [electrics/current-system.md](../electrics/current-system.md#31-suunnitellut-24-vn-kuluttajat-konehuoneessa) |
| Lämmönlähde | Öljykäyttöinen lämmityslaite, poltin 230 V alle 1 A (harkinnassa) | [omistaja 2026-10-28], [electrics/loads.yaml](../electrics/loads.yaml) |
| Vedenlämmitin | 3 kW:n sähkövastus (harkinnassa); koneen jäähdytysvesikierukka **⚠ ei tiedossa** | [omistaja 2026-10-28] |

## 2. Lämmittimet tiloittain

Jokaiseen tilaan tarvitaan lämmitin, joko konvektiotyyppinen (lämpöpatteri, ei sähköä) tai
puhallinmoottorillinen (puhallinkonvektori) [omistaja 2026-10-29]. Lämmittimet ovat
oletettavasti vesikiertoisen lämmityksen lämmönluovuttimia, eivät sähkölämmittimiä (**⚠ tarkista**).

| Tila | Lämmitin | Huomiot |
|---|---|---|
| Keulahytti | konvektori tai puhallinkonvektori | |
| Keskihytti | konvektori tai puhallinkonvektori | |
| Takahytti | konvektori tai puhallinkonvektori | |
| Komentosilta (brygga) | konvektori tai puhallinkonvektori | |
| Konehuone | luultavasti; konvektori tai puhallinkonvektori | [omistaja 2026-10-29] |
| Komentosilta: tuulilasin huurunpoisto | puhallin | Tarvitaan [omistaja 2026-10-29]; tuulilasissa myös Atlas-kirkasnäkölasi |

### Konvektori vai puhallinkonvektori [arvio]

| | Konvektori (patteri) | Puhallinkonvektori |
|---|---|---|
| Sähkö | ei | 24 V:n puhallin, arviolta noin 10–30 W/kpl (**⚠ arvio**) |
| Lämmitysteho samassa koossa | pienempi | suurempi; tila lämpenee nopeammin |
| Tilantarve | isompi pinta-ala seinällä | pienempi, mahtuu esim. penkin alle |
| Ääni | äänetön | puhaltimen ääni |
| Hinta | yleensä halvempi | yleensä kalliimpi |

**Vaikutus akustoon** [laskelma, **⚠ arvio**]: viisi puhallinkonvektoria noin 20 W:lla 8 h
vuorokaudessa vie noin 0,8 kWh/vrk lämmityskaudella, eli akustoa noin 40 Ah enemmän
(litium, 80 % käytettävissä, 25,6 V). Konvektorit eivät kuluta sähköä, mutta kiertovesipumppu
käy molemmissa. Yhdistelmä on mahdollinen: puhallinkonvektori sinne, missä tilaa on vähän tai
lämpöä tarvitaan nopeasti (esim. komentosilta), patterit muualle.

**Huurunpoisto** on puhallin, joka ohjaa lämmintä ilmaa tuulilasiin; tavallisesti se on
lämmityskierron lämmönvaihdin ja 24 V:n puhallin, teho **⚠ ei tiedossa**.

## 3. Avoimet kysymykset

- [ ] Ovatko lämmittimet vesikiertoisen lämmityksen konvektoreita, vai harkitaanko sähkölämmittimiä? (Sähkölämmittimiä ei kannata käyttää akustolta: 1 kW vie noin 1,1 kWh tunnissa)
- [ ] Konvektori vai puhallinkonvektori kuhunkin tilaan
- [ ] Lämmöntarve tiloittain (tilavuus, eristys); lämmönlähteen teho
- [ ] Huurunpoistopuhaltimen malli ja teho
- [ ] Lämmönlähde: öljypoltin, dieselkattila tai koneen jäähdytysvesi ajossa
