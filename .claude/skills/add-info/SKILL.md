---
name: add-info
description: Kirjaa uudet tiedot, mittaukset, kuvat, hinnat tai datalehtiarvot Vegan järjestelmistä oikeisiin dokumentteihin. Käytä, kun käyttäjä kertoo jotain, minkä on mitannut, lukenut, ostanut, muuttanut veneellä tai löytänyt datalehdestä tai linkistä.
---

# Lisää uutta tietoa

1. **Selvitä mitä tieto koskee** (järjestelmä, komponentti) ja **mistä se on peräisin**:
   - omistaja mittasi tai näki → `[omistaja VVVV-KK-PP]` tämän päivän päivämäärällä;
   - datalehti tai verkkosivu → `[datalehti <nimi>]` ja URL;
   - arvio → sano se.

   Jos lähde tai yksikkö on epäselvä, kysy yksi lyhyt kysymys.
2. **Etsi kaikki paikat, joihin tieto kuuluu.** Hae repoa komponentin nimellä ja siihen liittyvillä
   sanoilla. Yleensä:
   - `<järjestelmä>/current-system.md`: taulukot, tilannekatsaus, avointen kysymysten lista;
   - `vessel/README.md`, jos muutkin järjestelmät käyttävät tietoa (kone, vaihteisto, jännitteet,
     mitat);
   - `<järjestelmä>/loads.yaml` kuormien luvuille (pidä validina YAML:na, avaimet englanniksi);
   - `<järjestelmä>/requirements.md` ja `<järjestelmä>/design/*.md`, jos arvo vaikuttaa laskelmaan
     tai vertailuun.
3. **Päivitä ne** suomeksi. Korvaa `⚠ ei tiedossa` tai `⚠ tarkista` arvolla ja lähteellä. Rastita
   vastatut kysymykset `[x]`. Päivitä tilan päivämäärä.
4. **Tarkista seuraukset.** Jos uusi arvo muuttaa aiempaa laskelmaa, johtopäätöstä tai suositusta,
   laske uudelleen (kerro oletukset), päivitä teksti ja kerro käyttäjälle selvästi mikä muuttui.
   Esimerkki: "Tyhjäkäynti on 700 rpm eikä 800, joten 43 cm³:n pumppu antaa nyt noin 67 %
   työntövoimasta 88 %:n sijaan."
5. **Datalehtilinkin kohdalla** lue se, myös skannatut PDF:t (renderöi sivut kuviksi, jos tekstin
   poiminta ei onnistu). Kirjaa tärkeimmät arvot URL:n kanssa ja tarkista ne nykyistä suunnitelmaa
   vasten.
6. **Kerro käyttäjälle** hänen kielellään mitä kirjasit, minne, ja mitä siitä seuraa. Jos hän on
   valmis, ehdota `/save`.
