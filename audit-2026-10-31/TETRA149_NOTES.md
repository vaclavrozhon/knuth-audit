# DLX 149 — vrcholově obarvené čtyřstěny

3. listopadu 2026. Zadání str. 143 (PDF 163), řešení str. 458 (PDF 478).
Autorův draft má str. 79/162 (PDF 85/168). Matematika a všechny obrázky
ověřeny, nová chyba nenalezena. Celá úloha zůstává **partial** kvůli
nedohledané původní historické zmínce McComb/Scherphuis z roku 2015.

## Obecný důkaz modelu

Podle původního `sources/polygons143/gb_basic.w` určuje volání
`simplex(3,3,3,3,3,0,0)` čtyři nezáporné souřadnice se součtem 3.
Jejich horní meze 3 nic navíc neomezují, poslední nula znamená neorientovaný
graf. Sousední vrcholy se liší o +1 a −1 ve dvou souřadnicích.

Vrcholů je C(6,3) = 20. Jednotkových buněk je C(5,3) = 10, každá má
souřadnice se součtem 2 a čtyři vrcholy vzniklé přičtením jednotkových
vektorů. Každá hrana má jednoznačnou společnou buňku: souřadnicové minimum
jejích konců. Proto má graf 10 · 6 = 60 hran. Dvě různé buňky mají společný
nanejvýš jeden vrchol.

Každý čtyřstěn používá čtyři různé barvy. Pro každou z pěti vynechaných
barev existují 4!/12 = 2 rotační typy, protože vlastní rotace čtyřstěnu
tvoří sudé permutace A4. Celkem tedy deset fyzických dílků. Zrcadlení
prohodí oba typy se stejnou vynechanou barvou.

XCC model má deset primárních položek pro pozice, deset pro fyzické typy
a dvacet barevných sekundárních položek pro vrcholy. Každá možnost
jednoznačně umístí jeden typ do jedné pozice, jednou ze dvanácti rotací:
10 · 10 · 12 = 1200 možností. Pokrytí primárních položek použije každý
dílek i pozici právě jednou; shoda barev sekundárních položek je přesně
požadovaná shoda ve společných vrcholech. Opačný převod je jednoznačný.

V úvodním seznamu jmen je také `adec`. Je to platné jméno jiného typu;
seznam s výpustkou nemusí být lexikografický ani vypisovat zrcadlové
dvojice vedle sebe. Samotné pořadí není doložená chyba.

## Obrázky a úplnost

Přímo z původního PDF i draftu bylo přečteno všech dvacet čtyřciferných
souřadnic a dvacet barev, celkem 100 znaků na zdroj. Souřadnice odpovídají
afinní projekci čtyřstěnu. V obou zdrojích mají oba nakreslené grafy přesně
správných 60 hran; opakované tahy kvůli stínování jsou sloučeny. Zobrazená
sestava používá všech deset fyzických typů právě jednou.

Nezávislý C++ program přiřazuje barvy vrcholům. Typ poznává podle chybějící
barvy a parity inverzí; nepoužívá XCC řádky, DLX ani Python tabulku rotací.
Na prvním jednotkovém čtyřstěnu fixuje barvy `abcd`. Každé řešení má právě
jedno takové přejmenování; čtyři různé barvy určují i pátou, takže globální
grupa S5 působí volně. Úplný výčet dal **24** normalizovaných obarvení,
tedy **24 · 120 = 2880** pojmenovaných řešení. Běh trval 0,021 s.

Nezměněný původní DLX2 zpracoval všech 1200 možností a nalezl také
**2880** řešení za 1,982 s. Celé množiny se shodují; každý model byl přímo
geometricky ověřen. Obě metody běžely s `nice 15` a limitem 60 s.

Prostorové permutace čtyř souřadnic a přejmenování pěti barev dávají
24 · 120 = 2880 transformací problému. I prostorové zrcadlení je přípustné:
zamění chirality všech dílků, přičemž úplná sada obsahuje obě. Transformace
vytištěného svědka dávají 2880 **různých** platných modelů a přesně celou
ověřenou množinu. Existuje tedy jedna orbita a stabilizátor řešení má
velikost 1. Výraz „2880 automorphisms present“ označuje transformace
problému, ne 2880 symetrií jediného obarveného řešení.

Naše nativní měření má **474 615 675 čistých mems**. Je slučitelné
s knižním 500 Mμ při jedné platné číslici; přesnou historickou posloupnost
přístupů tím nereprodukujeme. Nejde o nález a další ladění pořadí nespouštíme.

## Prameny a hranice

Šest aktuálních i historických vrstev errat bylo prohledáno podle stránek,
úlohy, autorů, čtyřstěnů a čísel. Žádná příslušná oprava nalezena nebyla.
Zachované výsledky obsahují pouze nesouvisející shody na theorem 266
a hexadecimal. Obě původní strany byly také vizuálně zkontrolovány.

Vyhledávání přesného znění i jmen zatím vrátilo jen kopie Knuthova draftu.
[Scherphuisův index](https://www.jaapsch.net/puzzles/) je datovaný 2014;
původní zadání či řešení z roku 2015 v něm doloženo není. Knuthův
[seznam programů](https://www-cs-faculty.stanford.edu/~knuth/programs.html)
neobsahoval odpovídající program ani McCombovo jméno. To není důkaz,
že původní záznam neexistuje. Výslovně otevřené zůstává datování zadání
a autorství prvního řešení; matematické výčty neopakovat.

Reprodukce: `tetra149.py`, `count_tetra149.cpp`, `extract_tetra149.py`,
`check_tetra149.py`, `check_tetra149_sources.py`. Hotové důkazy jsou v
`results/tetra149/figures-checked.json`, `topology-checked.json` a
`bounded/checked.json`. Ukládají celé množiny, terminály, vstupy, hashe
a příkazy. Varování překladače o odsazení výstupního cyklu nemění jeho
význam; zdroj přijatého běhu ponechán beze změny. Žádný drahý výčet nezůstal
spuštěný. Další úloha: 150, řetězový hlavolam.
