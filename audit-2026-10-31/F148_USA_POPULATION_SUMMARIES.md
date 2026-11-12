# F148 — tři zaokrouhlené populační údaje na straně 116

Potvrzeno v našich dvou zdrojích 3. listopadu 2026. Nízká závažnost:
chybná číselná shrnutí, nikoli důkaz nesprávnosti optimalizační metody.
4B, hlavní text 7.2.2.1, strana 116 (PDF 136); autorský draft 5C,
strana 52 (PDF 58).

| Místo | Kniha, miliony | Přesný součet použitých vstupů | Zaokrouhlení na desetinu milionu |
|---|---:|---:|---:|
| Šest států Nové Anglie, první odstavec | 14,3 | 14 445 438 | 14,4 |
| New York a Nová Anglie dohromady | 33,7 | 33 823 525 | 33,8 |
| Nejmenší skupina bez NY v levém (116) | 37,3 | 37 177 055 | 37,2 |

Nová Anglie je CT, MA, ME, NH, RI, VT. Nejmenší skupina v obrázku je
**AZ, ID, KS, MN, MT, ND, NE, NV, OK, OR, WA, WY**. Celý její součet
je uložen po jednotlivých státech ve
[svědku](results/usa239_246/f148-f149-witness.json).
Všech sedm skupin bez NY má přesný rozsah **37 177 055 až 38 056 315**.
Větu lze napsat „roughly 37.2 to 38.1 million“, případně uvést přesná čísla.

Jde o hodnoty z autorova
[contiguous-usa.gb](https://www-cs-faculty.stanford.edu/~knuth/contiguous-usa.gb),
jehož celkový součet přesně odpovídá knižním 306 084 180. U všech států
potřebných pro tento důkaz se hodnoty zároveň přesně shodují s oficiálním
sloupcem **Estimates Base, April 1, 2010** v tabulce
[Census Bureau, vintage 2015](https://www2.census.gov/programs-surveys/popest/tables/2010-2015/national/totals/PEPANNRES.pdf).
Samostatná otevřená otázka kalifornské hodnoty proto tento důkaz neovlivňuje.

[Zvětšený text a obrázek](images/usa239-246-main116-text-and-graph.png),
[celá knižní strana](images/usa239-246-original-136.png),
[celý autorský draft](images/usa239-246-draft-58.png).
Členství států bylo přečteno z vektorových hran obou verzí a vizuálně
zkontrolováno. Úloha 246 navíc výslovně popisuje zvláštní propojení AZ,
ND a OK bez NM, CO a UT; odpovídá získané dvanáctičlenné skupině.

[verify_f148_f149.py](verify_f148_f149.py) pouze sčítá archivované hodnoty
a kontroluje krátké geometrické svědky. Nepouští optimalizaci.
Rozpor v údaji 34 111 a obecná atribuce dat mají vlastní otevřené záznamy;
nejsou započteny jako potvrzená chyba.

Šest vrstev historických i současných errat 4B/Fascicle 5 neobsahuje
odpovídající opravu; [záznam hledání](results/usa239_246/errata-search.json).
Fyzický výtisk, celá nejnovější digitální verze a prvenství nejsou ověřené.
