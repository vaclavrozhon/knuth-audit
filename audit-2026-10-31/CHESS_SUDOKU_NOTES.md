# Jezdcové a střelcové sudoku, úlohy173–174

Ověřeno 1. 11. 2026. Všech jedenáct prověřených zadání má přesně
jedno řešení. Každé spočítal nezávislý SAT model a původní DLX3
podle převodu173(a); úplné množiny27 obsazených buněk souhlasí.

| Zadání | Figura | Nápověd | Výsledek |
|---|---|---:|---|
| 173, příklad(ii) | jezdec | 8 | přesně obrázek(i) |
| 173, příklad(iv) | střelec | 9 | přesně obrázek(iii) |
| 173(b), první | jezdec | 5 nul | jediné řešení |
| 173(b), druhé | jezdec | 4 šestky | jediné řešení |
| 173(b), třetí | střelec | 3 nuly | jediné řešení |
| 173(b), čtvrté | střelec | 3 dvanáctky | jediné řešení |
| 173(d), původní Fig.A–3 | jezdec | 3, hodnoty6,8,6 | jediné řešení |
| 174, první dvojice | obě figury | 9, hodnoty0..8 | obě jediné řešení |
| 174, druhá dvojice | obě figury | 10 čtyřek | obě jediné řešení |

Číslice byly získány z textové vrstvy PDF podle přesných souřadnic
buněk, po vizuální kontrole str.146 a466. Není použito OCR.
Oba úplné příklady(i,iii) byly samostatně zkontrolovány: každý má
27 figur, tři v každém řádku, sloupci i boxu a všech27 vytištěných
čísel odpovídá počtu sousedů. Podle stejné geometrie jsou ověřeny
všechny nalezené modely. Střelcové sousedství znamená společnou
diagonálu bez ohledu na jiné figury na ní; tomu odpovídají i vysoké
číselné nápovědy v zadání.

Převod173(a) je bijektivní: předem dané figury se odečtou od všech
kvót. Nulová kvóta vyloučí všechny zbývající možnosti svého řádku,
sloupce, boxu či sousedství nápovědy. Každá jiná volná buňka tvoří
jednu možnost a současně spotřebuje všechny příslušné kladné kvóty.
Záporná kvóta znamená spor. Výběr možností tedy odpovídá právě
doplnění šachovnice.

SAT model naproti tomu zachovává všech81 buněk a přímo ukládá
součty3 v řádcích, sloupcích a boxech a sousedské součty nápověd.
Po prvním řešení zakáže celou polohu a prokáže nesplnitelnost
druhého modelu. DLX3 rovněž ukončí úplný výčet s jediným řešením.

Doklady jsou v `results/chess_sudoku/verified.json`; zahrnují všechny
nápovědy a řešení. `check_chess_sudoku.py` ukládá vstupy a logy
MCC i souřadnicovou extrakci obou stránek.

Známá náhrada Fig.A–3 z12.10.2023 uvádí lepší další hlavolamy a
informaci o minimalitě některých z nich. Zde netestujeme celou
galerii ani její minimality a nesplňujeme otevřenou tvůrčí část173(c).
Původní tří-nápovědový příklad pro173(d) zůstává platným svědkem.
Část174 je ověřena celá v rozsahu čtyř vytištěných zadání.
