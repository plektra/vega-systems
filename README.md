# Vegan järjestelmät

**Vegan** järjestelmien suunnittelu ja dokumentaatio. Vega on vuonna 1912 rakennettu teräshinaaja,
jota kunnostetaan vapaa-ajan käyttöön. Kaikki järjestelmät ovat samassa repossa, jotta ne voivat
viitata toisiinsa.

| Kansio | Sisältö |
|---|---|
| [vessel/](vessel/) | Yhteiset tiedot: alus, kone, vaihteisto, sähköjärjestelmän perustiedot |
| [hydraulics/](hydraulics/) | Ohjaus, keulapotkuri, ankkurivinssi: nykytila, vaatimukset, selvitykset |
| [electrics/](electrics/) | Akut, lataus, tehonjako, linkit valvonta- ja ohjauselektroniikkaan |
| [decisions.md](decisions.md) | Kaikki tähän asti tehdyt päätökset perusteluineen |
| [CLAUDE.md](CLAUDE.md) | Clauden työskentelyohjeet (myös ihmisten luettavissa) |

## Näin osallistut ilman git-osaamista

Et tarvitse gitiä, komentoriviä etkä muitakaan kehitystyökaluja. Kaikki onnistuu keskustelemalla
Clauden kanssa selaimessa tai puhelimessa.

### Kerran tehtävät

1. Luo ilmainen tunnus osoitteessa [github.com](https://github.com) ja pyydä Laria kutsumaan sinut
   tähän repoon.
2. Avaa [claude.ai/code](https://claude.ai/code) tai Claude-mobiilisovelluksessa **Code**, ja yhdistä
   GitHub-tunnuksesi pyydettäessä.
3. Valitse tämä repo.

### Joka kerta

1. **Aloita uusi istunto** jokaiselle aiheelle, esim. "ohjaussylinterin mitat" tai "akusto".
2. **Kirjoita normaalisti**, suomeksi tai englanniksi. Esimerkiksi:
   - *"Mittasin ohjaussylinterin: männän halkaisija 63 mm, varsi 32 mm, isku 250 mm."*
   - *"Mitä hydrauliikassa on vielä auki?"* (tai `/open-questions`)
   - *"Päätettiin ostaa Borellin 30502-kytkin."* (tai `/log-decision`)
   - *"Vertaa näitä kahta pumppua: <linkki>"*
3. **Kun olet valmis, sano "tallenna"** (tai `/save`). Claude tallentaa muutoksesi ja tekee
   *pull requestin* eli muutosehdotuksen, joka odottaa hyväksyntää. Saat linkin.
4. **Hyväksy:** avaa linkki ja paina **Merge pull request**. Myös Lari voi tehdä sen. Ennen
   hyväksyntää muutos ei ole osa päädokumentteja.

### Vinkkejä

- **Yksi aihe per istunto** pitää muutokset pieninä, eikä kahden ihmisen yhtäaikainen työ mene
  ristiin.
- **Claude kirjaa jokaisen luvun lähteen.** Kerro, mittasitko itse, luitko datalehdestä vai
  arvaatko.
- **Kuvat ja PDF:t:** avaa GitHubin verkkosivulla järjestelmän kansio, valitse
  **Add file → Upload files** ja lataa tiedostot sen `img/`-kansioon. Kerro sitten Claudelle.
- **Mitään ei katoa.** Jokainen muutos jää historiaan ja on peruttavissa. Pyydä vain Claudea.

## Liittyvät repot

Veneen elektroniikka (Signal K, NMEA 2000 -nodet, ESP32-tehonjakokortit) on erillisissä repoissa
osoitteessa [github.com/plektra](https://github.com/plektra). Ks.
[electrics/current-system.md](electrics/current-system.md).
