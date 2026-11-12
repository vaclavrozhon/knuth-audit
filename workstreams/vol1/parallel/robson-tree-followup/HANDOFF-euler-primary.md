# Předání: de Bruijn, Steffensen a Seki

2026-11-02. Nový samostatný paket; předchozí Robson/algorithms/constants
zůstávají zmrazené. Žádný commit ani zásah do společné evidence.

| Jednotka | Přesný výsledek |
|---|---|
| de Bruijn, *Asymptotic Methods in Analysis*, §3.7 | **Obsah i původní obraz checked.** Institucionální sken prvního vydání 1958; titul, obsah a s. 40–42 přímo přečteny. §3.7 je celý na s. 42. Normalizace dává `log(A)=1/12-zeta'(-1)`; druhý tvar už má samostatný kořenový důkaz. Pozdější vydání nekontrolována. |
| Steffensen, *Interpolation*, §14 | **Obsah i původní obraz checked.** Veřejný sken vydání Baltimore 1927, titul a rub, celý §14 na s. 129–138. Č. 149 přesně odpovídá knižnímu kritériu zbytku. Známá oprava roku 1937 → 1927 potvrzena. |
| Seki, původní *Katsuyō sanpō* 1712 | **Konkrétní historický obsah doložen.** Přečtena tabulka koeficientů na obr. 26, autorská hlavička, úvod posmrtného doslovu a tiráž 1712. Doložené `B_1=+1/2` souhlasí s dodatkem 2021. Není tvrzena úplná četba japonského spisu. |
| Seki, *Collected Works* 1974, s. 39–42 | **Source-partial.** Přesný NDL záznam nalezen, obsah omezen na registrovaný přístup; žádná strana moderního svazku nečtena. Původní tisk 1712 tuto přesnou bibliografickou mezeru nenahrazuje. |

Hlavní argumenty a přesné meze:
[notes/euler-primary-followup.md](notes/euler-primary-followup.md).
Strojový soupis pramenů: `results/source-inventory-euler-primary.json`.
Čtyři vrstvy errat: `results/errata-euler-gaps.json`.
Nové hledací stopy: `results/euler-primary-searches.json`.
Stažení: `sources/retrievals-euler-gaps.jsonl`.

Rozhodné originály:

* `sources/debruijn-rice-ch12.pdf`, titul PDF 1; `sources/debruijn-rice-ch3.pdf`,
  PDF 4–5 = tištěné s. 40–43. Obrazy `images/debruijn-title-01.png`,
  `images/debruijn-ch3-04.png`, `images/debruijn-ch3-05.png`.
* `sources/steffensen1927-original.pdf`, PDF 7–8 a 143–152;
  stejné číslování v `images/steffensen1927-*.png`.
* `sources/seki1712-026-full.jpg`, `sources/seki1712-007.jpg`,
  `sources/seki1712-110.jpg`, `sources/seki1712-111.jpg` a
  `sources/seki-kyoto-1712-manifest.json`.

Bez nového nálezu. Hotová obecná matematika ani testy se neopakovaly.
Concrete Mathematics řeší root v X0689. Nový paket uzavírá
`MANIFEST-euler-primary.sha256`; průběžný `progress.json` do něj nepatří.
