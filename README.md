# Rahoitustarjoushälytin GitHub Pages -versio

Tällä paketilla saat HTTPS-osoitteen, jota voi katsoa selaimella päivittäin.

## Käyttöönotto
1. Luo GitHubiin uusi repository, esimerkiksi `rahoitustarjoushalytin`.
2. Pura tämän ZIPin sisältö repositoryyn.
3. Commit + push GitHubiin.
4. GitHubissa: Settings > Pages > Deploy from branch > main > /root > Save.
5. Odota hetki. Saat osoitteen muotoa `https://käyttäjä.github.io/rahoitustarjoushalytin/`.
6. Mene Actions-välilehdelle ja aja workflow käsin: `Päivitä rahoitustarjoushälytin` > Run workflow.

## Mitä tämä tekee?
- GitHub Actions ajaa `scripts/update_results.py` joka aamu cronilla.
- Se luo/päivittää `results.json` tiedoston.
- GitHub Pages näyttää `index.html` kautta tuoreen listan.

## Huomio
Tässä on vielä demodata. Live-parserit lisätään `scripts/update_results.py` tiedostoon liike kerrallaan.
