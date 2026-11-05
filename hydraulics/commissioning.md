# Hydrauliikan täyttö ja ilmaus (käyttöönotto)

> **Tila:** ohje 2026-11-05, ei vielä tehty veneellä. Koottu repon tiedoista, PVH57:n
> huoltotiedotteesta M-2206-S (s. 7) ja yleisestä hydrauliikkakäytännöstä. Kohdat, joissa lukee
> [yleistieto], eivät ole valmistajan ohjeita. **Ohjaus on turvallisuuskriittinen: pätevän henkilön
> pitää tarkistaa järjestelmä ja tämä järjestys ennen ensimmäistä ajoa.**
>
> Liittyy: [p2-variable-pump: asennus ja säädöt](design/p2-variable-pump.md#säätö-käyttöönotossa-ilman-virtausmittaria),
> [hydraulic-oil](design/hydraulic-oil.md) (öljy ja huuhtelu), [schematic](schematic.md) (osatunnukset).

## 1. Valmistelu

- [ ] **Puhtaus.** PVH57 vaatii puhtausluokan 16/14/12 [Eaton PVH s. 31]. Pidä letkujen ja porttien
  tulpat paikallaan kytkentään asti, ja huuhtele uudet letkut ennen kytkentää [yleistieto].
- [ ] **Täyttö suodattimen läpi.** Öljyä ei kaadeta suoraan säiliöön, vaan se pumpataan
  siirtopumpulla suodattimen läpi tai paluusuodattimen kautta [yleistieto].
- [ ] **Öljy.** Koeajot ajetaan vanhalla, kirkkaalla öljyllä (Teboil Hydraulic Lift 32) uuden
  suodatinelementin läpi (päätös 2026-10-27). Sen jälkeen vaihdetaan HVLP 32:een, ks. kohta 8.
- [ ] **Lisäöljyä varalle noin 20 l.** Linjat ja sylinteri sitovat täytössä noin 15 l, ja säiliön
  pinta laskee saman verran:

  | Linja | Mitat | Tilavuus [laskelma] |
  |---|---|---|
  | P2:n imu | 50 mm × 3 m | noin 5,9 l |
  | P1:n imu | 32 mm × 3,2 m | noin 2,6 l |
  | Paluulinja | 1" (25,4 mm) × 5 m | noin 2,5 l |
  | Keulapotkurin A + B | 1/2" (12,7 mm) × 2 × 8,5 m | noin 2,2 l |
  | P2:n painelinja | 3/4" (19 mm) × 4 m | noin 1,1 l |
  | Ohjaussylinteri | 283 + 187 cm³ | noin 0,5 l |
  | **Yhteensä** (ilman pumppuja, venttiilejä, orbitrolia ja pieniä letkuja) | | **noin 15 l** |

  *Oletus: letkujen sisähalkaisija on nimelliskoko. Pituudet: [current-system §0](current-system.md),
  [schematic](schematic.md).*

## 2. Säiliö ja imulinjat

Säiliön öljypinta on vähintään 1 m pumppujen imuaukkojen yläpuolella [omistaja 2026-10-26], joten
imulinjat täyttyvät painovoimalla.

1. [ ] Täytä säiliö (Flowfit 100 l) maksimiin.
2. [ ] Avaa imulinjojen palloventtiilit (P1 ja P2).
3. [ ] Löysää imuliitintä pumpun päässä, kunnes öljyä tulee ilman kuplia, ja kiristä liitin.
4. [ ] Tarkista, ettei imuletkuissa ole ilmaa kerääviä yläkohtia: letkun pitää laskea koko matkan
   säiliöltä pumpulle.
5. [ ] Täytä säiliö uudelleen maksimiin.

## 3. P2 (Vickers PVH57): kotelo täyteen ennen käynnistystä

**Kuivana käynnistetty kotelo vaurioittaa laakereita ja pyörivää ryhmää.**

1. [ ] Täytä pumpun kotelo öljyllä **ylemmästä vuotoportista** [M-2206-S s. 7]. Käännä akselia käsin,
   jotta ilma pääsee ulos [yleistieto].
2. [ ] Kytke kotelovuotoletku ylemmästä portista säiliöön öljypinnan alle (ei yhteiseen paluulinjaan).
3. [ ] Tarkista, että imulinjan palloventtiili on auki.
4. [ ] Käynnistä tyhjäkäynnillä, kaikki PVG 32:n karat keskellä. Pumppu on silloin valmiustilassa
   noin 20 barissa.
5. [ ] Ilmaa painelinja löysäämällä pumpun lähtöliitintä varovasti, kunnes öljyä tulee ilman
   kuplia [M-2206-S s. 7].
6. [ ] Aja **5–10 min kuormittamatta**. Öljy ei saa muuttua maitomaiseksi [M-2206-S s. 7].
7. [ ] LS-linja (1/4"): löysää liitintä pumpun LS-portissa hetkeksi valmiustilassa, kunnes öljyä
   tulee ilman kuplia [yleistieto].

## 4. P1 (ohjauspumppu)

1. [ ] Kaada pumppuun öljyä painelähdön kautta ennen painelinjan kytkentää, jos pääset siihen
   käsiksi [yleistieto].
2. [ ] Käynnistä tyhjäkäynnillä. RPF3:n ylimäärävirta ja orbitrolin avoin keskiasento kierrättävät
   ilman säiliöön. Aja muutama minuutti koskematta ruoriin.

## 5. Ohjaussylinteri

Sylinterissä ei ole ilmausruuveja ja liitännät ovat sivuilla, joten ilma jää helposti sylinteriin
[blogi 2017-07-04]. Menetelmä on [yleistieto].

1. [ ] **Jos mahdollista, käännä sylinteri niin, että liitännät osoittavat ylöspäin:** irrota varren
   pään tappi ja kierrä sylinteriä varren ympäri ilmauksen ajaksi.
2. [ ] Käännä ruoria hitaasti laidasta laitaan 10–20 kertaa. Pidä ääriasennoissa lyhyt tauko, mutta
   älä paina pitkään paineenrajoitusta vasten.
3. [ ] Kiinnitä sylinteri takaisin.
4. [ ] Merkit jäljellä olevasta ilmasta: pehmeä tai nykivä ohjaus, ratin välys kasvaa, säiliössä
   vaahtoa. Jatka tarvittaessa ja anna öljyn välillä seistä.

## 6. Keulapotkuri (lohko 1, 8,5 m:n linjat)

1. [ ] Täytä ja kytke U11:n vuotolinja (1/4") suoraan säiliöön.
2. [ ] Ohjaa lohkoa 1 hetkittäin ja pienellä virtauksella vuorotellen kumpaankin suuntaan.
3. [ ] Jos moottorin liitännät ovat linjojen ylimpänä kohtana, löysää niitä vähän kerrallaan
   valmiustilan paineessa [yleistieto].
4. [ ] Pidä ihmiset poissa potkuritunnelin läheltä.

## 7. Lopuksi

1. [ ] Anna järjestelmän seistä muutama tunti, jotta ilma nousee öljystä, ja täytä säiliö
   pintaan [yleistieto].
2. [ ] Tarkista säiliöstä vaahto ja sameus sekä paluusuodattimen mittari.
3. [ ] Tarkista kaikki liitokset vuotojen varalta.
4. [ ] Tee säädöt vasta ilmatulla järjestelmällä: PVH57:n paineenrajoitin 120 → 250 bar ja muut,
   ks. [p2-variable-pump](design/p2-variable-pump.md#säätö-käyttöönotossa-ilman-virtausmittaria);
   orbitrolin paineenrajoitus, ks. [current-system](current-system.md).
5. [ ] Koeta ohjaus laiturissa ääriasennosta toiseen ja hätäohitusventtiili hätäpinnan kanssa
   ennen ajoa.

## 8. Huuhteluöljyn vaihto koeajojen jälkeen

Päätös 2026-10-27, ks. [hydraulic-oil](design/hydraulic-oil.md#suositus).

1. [ ] Tyhjennä öljy säiliöstä, letkuista, sylinteristä ja orbitrolista.
2. [ ] Vaihda paluusuodattimen elementti.
3. [ ] Täytä HVLP 32:lla suodattimen läpi ja ilmaa uudelleen kohtien 2–7 mukaan (PVH57:n kotelo
   täyteen ennen käynnistystä).
4. [ ] Kirjaa öljyn ja suodattimen vaihto tiedostoon `maintenance/consumables.yaml`.

## ⚠ Turvallisuus

- **Löysää liittimiä vain paineettomana tai valmiustilan matalalla paineella, älä koskaan
  paineenrajoituksen paineessa.** Ohut öljysuihku voi tunkeutua ihon läpi, ja se vaatii aina
  päivystyskäynnin. Käytä suojalaseja ja käsineitä.
- Pidä ihmiset poissa peräsimen, vivuston ja pyörivän PTO-kytkimen läheltä. Kytkimen suojakotelon
  pitää olla paikallaan.
- **Vikatilat ilmauksen aikana:**
  - Ilmaa ohjauspiirissä: peräsin reagoi viiveellä tai jää ääriasentoon. Ennen ajoa kokeillaan
    laiturissa, ja hätäpinna on saatavilla.
  - Pumppu imee ilmaa (kova ääni tai vaahtoava öljy): pysäytä kone heti ja tarkista imulinja,
    palloventtiili ja öljypinta.
  - Kotelovuotolinja tukossa tai kotelo kuiva: akselitiiviste tai laakerit vaurioituvat. Tarkista
    ennen jokaista käynnistystä, että linja on auki.
