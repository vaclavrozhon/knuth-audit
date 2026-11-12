# Nesprávně předpovězený výstup programu v odpovědi §2.2.3-24

Stav: **confirmed v elektronických podkladech**, bez přidělení globálního ID,
bez ověření fyzického dotisku a bez tvrzení o prvenství.

## Tvrzení a odlišení chyby

Poznámka na s. 549 za programem odpovědi 24 říká, že po přidání
relací 9<1 a 6<9 k datům (18) program vytiskne cyklus `9,6,8,5,9`.
Původní obrazy s. 264, 266–268 a 548–549 byly zobrazeny a přesný
program přepsán do `programs.py` (`TOPO`, `with_cycles`, `CYCLE_END`).
Program ve skutečnosti vytiskne `1,9,6,4,7,3,1`.

Oba řetězce popisují platný cyklus ve zpětném směru. **Algoritmus ani
MIX program se tím nevyvrací.** Chybná je pouze předpověď konkrétního
výstupu. Vytištěný kratší cyklus odpovídá jiné povolené volbě pořadí
předchůdců, kterou však uvedený MIX program neprovádí.

## Ruční důkaz

Data (18) mají přesné pořadí

```
(9,2),(3,7),(7,5),(5,8),(8,6),(4,6),(1,3),(7,4),(9,5),(2,8).
```

Připojme (9,1),(6,9). Každý z devíti vrcholů má nyní aspoň jednu
vstupující hranu. První fáze třídění proto nevypíše žádný vrchol,
pouze koncovou nulu, a přejde při N=9 do diagnostiky cyklu.
Všechny seznamy TOP jsou nedotčené.

T3 každou novou hranu přidává na **začátek** seznamu zdrojového
vrcholu. Seznamy následníků jsou tedy:

| k | následníci v pořadí TOP/NEXT |
|---|---|
|1|3|
|2|8|
|3|7|
|4|6|
|5|8|
|6|9|
|7|4,5|
|8|6|
|9|1,5,2|

Řádky 80 a 88–89 nastaví rI6=n a po každém zdrojovém vrcholu
jej sníží o 1. T9 tedy zpracuje **k=9,8,...,1**. Řádek 85
při každé hraně k→j přiřadí QLINK[j]=k. Pozdější zdroj přepíše
staršího; ve výsledku QLINK[j] obsahuje nejmenšího předchůdce j.
Pořadí hran uvnitř jednoho seznamu to nemění: všechna přiřazení
z téhož zdroje používají stejné k. Rovněž vložení nových dvou
hran na jiné místo vstupní pásky nemůže tuto tabulku změnit.

| j |1|2|3|4|5|6|7|8|9|
|---|---|---|---|---|---|---|---|---|---|
| QLINK[j] |9|9|1|7|7|4|3|2|6|

Po sestupné smyčce je rI6=0. Řádky 90–92 začnou od k=1,
jehož QLINK je nenulový. T12 tedy projde

```
1 -> 9 -> 6 -> 4 -> 7 -> 3 -> 1.
```

Každý navštívený vrchol označí v TOP svou vlastní nenulovou
hodnotou. První opakovaný vrchol je 1. T13 vypisuje počínaje
ním; po prvním vypsání každému vrcholu smaže značku, takže
po návratu do 1 vytiskne znovu 1 a skončí. Výstup je proto
přesně `1,9,6,4,7,3,1`.

Pokud bychom místo toho provedli T9 se **vzestupným** k,
QLINK by obsahoval největší předchůdce. Cesta od 1 pak je
`1,9,6,8,5,9`, jejím prvním opakovaným vrcholem 9; vypsaný
cyklus by byl `9,6,8,5,9`. To vysvětluje záměnu s přirozeným
vzestupným provedením abstraktní odpovědi 23.

## Doplňková exekuce a errata

`check_programs.py` vykonává doslovnou transkripci v MIX modelu,
včetně asynchronní vstupní/výstupní pásky a tiskárny. Výstup
srovnává s právě odvozeným řetězcem a nezávisle kontroluje,
že sousední vypsané vrcholy tvoří zpětné vstupní hrany. Používá
radix64 i100 a zpoždění zařízení0 i97. Vlastní lokální rozvinutí
END je ekvivalent předepsané sémantiky MIXAL, nikoli změna
algoritmu nebo pořadí dat.

Ve všech čtyřech vrstvách errat (`all1-prepre`, `all1-pre`, `all1`,
`err1`) byly hledány strany548–549, answer24, výstupní čísla,
loop, T9/T12/T13. Jediná oprava na s.549 je alpha→alphameric
z 28. 9. 2002; týká se komentáře k CHAR, nikoli poznámky.
Originál této opravy je `images/all1-prepre-file41.png`.
Aktuálnost vrstev koordinátor ověřil 1. 11. 2026.

## English ASCII draft

In the note following the program for exercise 2.2.3-24 (page 549),
the printed output should be "1, 9, 6, 4, 7, 3, 1", instead of
"9, 6, 8, 5, 9". Lines 80 and 88--89 scan the source vertices
in decreasing order, so QLINK[6] finally equals 4 and QLINK[5]
finally equals 7. The search then starts at vertex 1 and follows
1,9,6,4,7,3,1. The shorter cycle in the note would result from
scanning source vertices in increasing order. Both are valid cycles;
only the prediction of this program's particular output is incorrect.
