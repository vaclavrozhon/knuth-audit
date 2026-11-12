# Známá errata §2.2.5

Prohledány všechny čtyři vrstvy, stránkové rozsahy 280–298 a 553–556
i termíny `2.2.5`, `Doubly`, `4820`, `4840`. Soubor
`results/errata-search.txt` uchovává prvotní vyhledání; úplný inventář
níže vznikl i hledáním celých rozsahů. Živé hashe jsou v SOURCES.

| Vrstva | Místo | Datum | Změna a dopad |
|---|---|---|---|
| all1-prepre | 281, ř. 9–10 | 2004-05-03 | sazba NODE(X), X; bez změny algoritmu |
| all1-prepre | 285, E3 | 1997-08-20 | door → doors |
| all1-prepre | 285, E5 | 1997-08-20 | door → doors |
| all1-prepre | 287, D2 | 1997-08-20 | door → doors |
| all1-prepre | 290, komentáře 047/049 | 1997-08-20 | door → doors |
| all1-prepre | 292, komentář 098 | 2003-01-25 | Compute IN,OUT → Set INFLOOR,OUTFLOOR |
| all1-prepre | 292, 103/105 | 1998-07-08 | POOLMAX → POOLMAX(0:2); použito v programu |
| all1-prepre | 293, ř. −14 | 2001-12-24 | Coroutine E, velké počáteční písmeno |
| all1-prepre | 294, komentář 201 | 1997-08-20 | door → doors |
| all1-prepre | 295, komentář 237 | 1997-08-20 | door → doors |
| all1-prepre | 296, ř. 7 | 1998-07-08 | POOLMAX CON → NOP; viz syntaktický důvod v NOTES |
| all1-prepre | 296, ř. 20 | 1999-02-14 | by performed → be performed |
| all1-prepre | 296, ř. 22 | 2005-10-08 | quasi-parallel → quasiparallel |
| all1-prepre | 296, ř. −4 | 1998-08-31 | smyčka E4: 216–218 → 217–219 |
| all1-prepre | 298, konec úlohy 11 | 1999-02-14 | on the same step → in the same step |
| all1-prepre | 555, odp. 9, 04 | 1997-08-20 | door → doors |
| all1-prepre | 555, odp. 9, 14 | 2001-07-04 | doplnění tečky komentáře |
| all1-prepre | 555, konec odp. 9 | 1998-08-03 | ukončovací značka za subroutine |
| all1-pre | 286, čas 4820, D3 | 2017-12-03 | 0 → X; ověřeno oběma simulacemi |
| all1/err1 | 286, druhý čas 0180, D2 | 2023-07-07 | X → 0; ověřeno oběma simulacemi |
| all1/err1 | 297, zadání 8 | 2024-05-02 | 277–292 → 277–291, 292 už je v textu |
| all1/err1 | 554, odp. 6 | 2024-05-02 | jednoznačná logická podmínka způsobilého směru v U2/U4 |

Při počátečním čtení byl poslední čas E1 v tabulce mylně přečten jako
4820. Nové prohlédnutí originálu jednoznačně ukázalo **4840**, shodně
s algoritmem i oběma programy. Podezření bylo vyřazeno před vytvořením
nálezového reportu. Nejde o nevyřešený kandidát.
