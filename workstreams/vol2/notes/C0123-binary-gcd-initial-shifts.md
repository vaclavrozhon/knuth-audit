# V2-C0123 — v přesném průměru D chybí počáteční posuny

Stav: **confirmed**. §4.5.2-22, první věta odpovědi na str.643,
navazující na identitu na642. Originály obou stran i definice D
na340 byly zobrazeny. Věta přenáší přesnou váhovou identitu pro
počet odečtení C na počet posunů D bez dalšího členu.

Pro N=2 jsou vstupy nezávisle rovnoměrné z{1,2,3}. Počty vykonání
B3 jsou následující; řádky označují první a sloupce druhý vstup:

```text
       1  2  3
   1   0  1  1
   2   1  0  2
   3   1  2  0
```

Součet je8, tedy průměr8/9. Liché třídy mají D_00=D_11=0 a
D_10=D_01=1. Dosazení do tištěné váhové identity dává jen4/9.

Chybějí posuny zpočátku sudého argumentu. Pro lichá u,v a nezáporná
a,b platí bodově `D(2^a*u,2^b*v)=D(u,v)+|a-b|`. B1 odstraní
společnou mocninu, zbývající |a-b| posuny však proběhnou v B3 a
definice na340 je zahrnuje do D. V příkladu přispívají po jednom
dvojice(1,2),(2,1),(2,3),(3,2).

Obecně je při M=2^N-1 nutné do průměru přičíst

```text
E[|a-b|] = 4/3 + (8/3-2N)/M - 2N/M².
```

Do nenormalizované pravé strany identity na642 proto patří
`(4M²+(8-6N)M-6N)/3`. Důkaz z konečných počtů násobků mocnin2 je
v `gcd-bins.md`. Oprava je O(1) a vedoucí asymptotický koeficient
v zadání22 nemění. Kontrola pro N=1..8 porovnává opravené vážení
s dříve nezávisle ověřeným celkovým sčítáním.

Čtyři vrstvy errat `all2-prepre`, `all2-pre`, `all2`, `err2`
prohledány2026-11-02 podle stran, úlohy a posunů; oprava nenalezena.
Aktuální fyzický dotisk a prvenství neověřeny; návrh neodeslán.
