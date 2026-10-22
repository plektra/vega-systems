---
name: save
description: Tallentaa istunnon muutokset GitHubiin pull requestina. Käytä, kun käyttäjä sanoo "tallenna", "valmis", "save" tai "done", tai pyytää lähettämään tai jakamaan muutoksensa.
---

# Tallenna muutokset pull requestina

Käyttäjä ei välttämättä osaa gitiä. Tee kaikki vaiheet itse ja kerro lopputulos yhdellä tai
kahdella selkeällä lauseella käyttäjän kielellä.

1. **Tarkista mitä muuttui** (`git status`, `git diff`). Jos mitään ei muuttunut, kerro se ja lopeta.
2. **Tarkista muutosten johdonmukaisuus:** lähteet merkitty, `⚠ tarkista` epävarmoissa arvoissa,
   avointen kysymysten listat ja `decisions.md` päivitetty, tiedostojen väliset linkit toimivat.
   Korjaa pienet puutteet; kerro isommista.
3. **Varmista, ettet ole `main`-haarassa.** Jos olet, luo aiheen mukainen haara, esim.
   `hydraulics/steering-cylinder-data`.
4. **Tuo uusin `main`** (`git fetch origin main`, sitten merge tai rebase). Jos tulee konflikteja,
   säilytä molempien tiedot; kysy käyttäjältä vain, jos versiot ovat ristiriidassa.
5. **Committaa** lyhyellä englanninkielisellä viestillä, joka kuvaa aiheen, esim. "Add steering
   cylinder dimensions". Lisää loppuun ohjeidesi mukaiset attribuutiorivit, jos sellaisia on.
6. **Pushaa haara** (ei koskaan force-pushia) **ja avaa pull request** `main`-haaraan:
   - Otsikko: sama lyhyt yhteenveto.
   - Kuvaus suomeksi: ensin **selkokielinen yhteenveto** siitä, mitä muuttui ja miksi, muutama
     ranskalainen viiva, jonka omistaja voi hyväksyä puhelimella. Sitten muuttuneet luvut
     (vanha → uusi) ja mahdolliset uudet avoimet kysymykset.
   - Jos et pysty avaamaan pull requestia itse, pyydä käyttäjää painamaan **Create PR** -painiketta
     Claude Coden käyttöliittymässä.
7. **Kerro käyttäjälle:** "Tallennettu. Muutoksesi odottavat hyväksyntää täällä: <linkki>. Avaa se
   ja paina *Merge pull request*, niin muutokset tulevat osaksi päädokumentteja."
