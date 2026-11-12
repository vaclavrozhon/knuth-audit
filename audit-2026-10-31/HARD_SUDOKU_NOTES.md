# Hard sudoku, 7.2.2.2–515

## F064 — chybějící omezení podmínky (vi)

Zadání na p.367 zakazuje všechny čtyři prázdné buňky každého obdélníku
s hodnotami k,l / l,k. Odpověď p.651–652 odpovídá pouze obdélníkům, které
leží ve dvou boxech (řádky jsou ve stejném pásu nebo sloupce ve stejném pásu).
Doslovná podmínka zahrnuje také obdélníky ve čtyřech boxech.

Vlastní přepis celé konstrukce přesně reprodukuje 2 471 proměnných,
58 212 klauzulí a 351 432 výskytů literálů. Blok (vi) má 34 992 klauzulí.
Po ztotožnění symetrických Z je nutné odstranit opakované literály; to vysvětluje
celkový počet výskytů. Žádná chyba v těchto třech počtech není hlášena.

Model v `results/hard_sudoku/literal-vi-counterexample.json` splňuje každou
klauzuli a přímá kontrola mřížky ověřuje (i)–(v). V řádcích 2,5 a sloupcích 2,5
má však čtyři prázdná pole s hodnotami 4,7 / 7,4. Jsou ve čtyřech boxech.
Také obsahuje druhý takový obdélník. Puzzle má čtyři doplnění, nezávisle
spočítaná přímým MRV prohledáváním a autorovým neměněným DLX2. Jednoznačnost
není podmínkou zadání 515.

Nejpřirozenější oprava je doplnit do (vi) omezení na dva boxy. Pak je popis
kódování i zamýšlený zákaz jednoduchého sudoku trade správný. Alternativou je
přidat klauzule i pro obdélníky ve čtyřech boxech a změnit uvedené počty.
Znění bylo vizuálně ověřeno v hlavním PDF a autorově fasc6a z 23. září 2015
(p.183 a 287). V all4b a all4f6 nebyla nalezena odpovídající oprava.
Fyzický výtisk není ověřen.

## Příklady a další rozsah

Dva nezávislé výčty potvrzují počty doplnění (a)–(d): **1, 1, 1237, 12**.
Každá mřížka splňuje symetrii, požadavky na prázdná místa a požadované minimum
2 nebo 3 možností v (iv),(v). Příklad (b) má 58 viditelných hodnot, zbývají
pouze číslice 2,4,7. (b),(d) mají nejvýše jedno prázdné pole v řádku či sloupci
každého boxu. U (c) stačí existence doplnění splňujícího (vi); 30 z 1237
vyhovuje doslovné podmínce, takže nejde o další chybu.

Pokus s pevně zvoleným čtyřboxovým obdélníkem a zesíleným (iii) byl UNSAT;
tento jediný neúspěšný pokus není použit jako důkaz obecného tvrzení.

## 517 — one-in-three SAT

Nová redukce z hlavního PDF je správná. Je-li první literál pravdivý, a=c=0,
b a d převezmou pravdivost ostatních literálů. Je-li nepravdivý, a+c=1 a lze
vybrat právě některý z pravdivých zbývajících literálů; při třech nepravdivých
nelze. Pro všechny tři literály pravdivé/nepravdivé byl projit celý prostor
čtyř pomocných bitů. Rozštěpení dlouhé rovnice má obecný důkaz se součty:
první součet je 1−t a druhý t. Ověřeno také 81 924 konečných rozštěpení.
Pomocný gadget pro krátké rovnice má přesně (a,b,c,d)=(0,0,1,1),(0,1,0,0),
tedy a=0 a b+c=1. Obě zkrácené redukce jsou tudíž správné.
Data: `results/one_in_three.json`. Starší PS má jinou redukci části (a),
proto jeho znění není zaměňováno za novou verzi.
