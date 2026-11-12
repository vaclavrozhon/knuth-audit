# F0004 — pět barev nestačí pro torus se třemi řádky

**Confirmed, medium.** §7–126, odpověď str. 530 / file547,
věta „Otherwise we obtain a 5-coloring“. Zadání str. 44 / file061.
Původní sazba: images/file061.png a images/proof-file547.png.
Kontrola 6. listopadu 2026; první vydání/dotisk 2011, file=printed+17.

## Doména a protipříklad

Zadání výslovně žádá optimum pro C_m strong C_n **when m,n≥3**.
Definice silného součinu na str. 27–28 nezavádí omezení m,n>3;
C₃ je obyčejný trojúhelník K₃. Přesná pravidla součinu jsou už doložena
v notes/proof-012-graph-products.md, bez nutnosti dalšího ověření.
Odpověď sama odděluje (3,3), (3,4) a (3,5), a pak přechází na pět barev.
Přípustný vstup **m=3,n=6** tedy patří do této poslední větve.

Šest vrcholů {(i,j):i∈{0,1,2},j∈{0,1}} tvoří kliku K₆:
v první souřadnici jsou každé dvě různé hodnoty sousední v C₃,
ve druhé jsou 0 a 1 sousední v C₆. Definice silného součinu proto
spojuje každou dvojici těchto šesti různých vrcholů. Nutně χ≥6.

Šest barev stačí: dej c(i,j)=i+3(j mod 2), i=0,1,2 a j=0,...,5.
Každý sloupec má tři různé barvy a sousední sloupce mají disjunktní
palety, včetně uzávěru 5–0. Tedy **χ(C₃ strong C₆)=6**, nikoli 5.
Jde o přímý důkaz, žádný vyhledávací program ani census.

Selže i zdůvodnění tištěnou periodickou posloupností: tři kroky ±1
mají součet ±1 nebo ±3, nikdy 0 modulo5. Posloupnost délky3 s danými
sousedními rozdíly tudíž neexistuje.

## Rozsah opravy

Symetrií lze předpokládat 3≤m≤n. Pro m,n≥4 funguje tištěná konstrukce:
sudou délku získáme střídáním kroků +1,−1; lichou délku nejméně5
jedním oběhem C₅ a vloženými dvoukrokovými návraty. Na silné hraně
je změna a+2b některá z ±1,±2,±3, a tedy nenulová modulo5.

Chybějící rodina m=3 má χ=6 pro sudé n≥4 a χ=7 pro liché n≥7;
(3,3) má 9 a (3,5) má 8, jak už uvádí kniha. Důkazy a explicitní
konstrukce celé opravy jsou v notes/proof-016-colorings-cliques.md.
Nález neoznačuje za chybné zadání ani správné části odpovědi.

## Vyloučení známých errat a primární citace

Prohledány všechny relevantní vrstvy errata/text/all4a-pre.txt,
all4a.txt, err4a.txt, all4f0.txt a err4f0.txt. Hledána str.44/530,
fasciklové odpovědi149–150, číslo126, kingwise, torus, period lengths,
5-coloring a Vesztergombi. Jediné příslušné erratum odpovědi126
je bibliografické **1978→1979 z23.5.2011**, all4a-pre řádky798–799.
Matematické omezení rozměru3 ani oprava poslední větve zde nejsou.
Ostatní záznamy pro stejné stránky patří úlohám114/119/122/131/133.

Primární [stránka časopisu](https://cyber.bibl.u-szeged.hu/index.php/actcybern/article/view/3179)
potvrzuje autora, rok1979, svazek4(2),207–212. Dostupný
[článek](https://cyber.bibl.u-szeged.hu/index.php/actcybern/article/view/3179/3164)
ve větě2 výslovně omezuje oba liché cykly na délky větší než3;
na str.210 také pojednává K₃ strong lichý cyklus s číslem7.
Protipříklad na této citaci nezávisí. Nečiníme nárok na prvenství nálezu
ani na kontrolu fyzického výtisku.

Jediná error location pro UI: **file547 / printed530**.
