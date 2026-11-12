# §4.5.3-51: racionální rekonstrukce

Zadání na 379 a odpověď na 656–657 byly vizuálně přečteny.
Algoritmus i jednoznačnost pro zadanou čtvercovou mez jsou správné.
Jde o `known_erratum`: oprava z 1999-05-31 na 657, řádek 15,
opravuje sazbu exponentu na `(-1)^(j-1)`. Nejde o nový nález.
Stop test v originále skutečně obsahuje `<=`, nikoli `<` z OCR.
Čtyři řady errat a aktuální TeX byly prohledány 2026-11-03.

## 1. Zadání a myšlenka

Jsou dána celá čísla m>a>1. Hledáme nesoudělná celá x,y taková, že

```
a*x = y (mod m),   0<x<=theta,   |y|<=theta,
theta=sqrt(m/2).                                           (R1)
```

Kongruence znamená, že a*x-y je celočíselným násobkem m.
Racionální rekonstrukce tak získává malý zlomek y/x z jeho
zbytku a modulo m. Například pro a=28481, m=199999 dostaneme
x=316, y=41: `28481*316-199999*45=41`.

Rozšířený Eukleidův algoritmus současně s klesajícími zbytky
udržuje jejich celočíselné vyjádření pomocí m a a. Zastavíme
při prvním dostatečně malém zbytku. Proč stačí tento jediný
kandidát: vlastnost nejlepší aproximace omezuje jeho jmenovatel
shora každým možným řešením (§3); dvě tak malé dvojice v téže
kongruenci pak musí být rovnoběžné (§4). Nesoudělnost určí měřítko.

## 2. Přesný algoritmus

Pro obecnější kladné reálné meze X,Y předpokládejme `2*X*Y<=m`.
Pokud X<1, není řešení. Jinak postupně vytváříme řádky (r,s,t)
s invariantem `s*m+t*a=r`, z počátečních řádků
`(m,1,0),(a,0,1)`. Nový řádek je předpředchozí minus q krát
předchozí, kde q je podíl při celočíselném dělení zbytků.
Zastavíme při prvním `r<=Y`. Symbol sign(t) je +1 pro kladné t
a -1 pro záporné t. Položíme

```
Q=|t|,   R=sign(t)*r,   Z=-sign(t)*s.
a*Q-m*Z=R.                                                (R2)
```

Vrátíme (Q,R), pokud `Q<=X` a `gcd(Q,R)=1`; jinak oznámíme,
že řešení není. Symbol gcd označuje kladného největšího
společného dělitele. Zbytky klesají až k nule, takže algoritmus
skončí; t v uvažovaných řádcích nikdy není nula.

Determinant dvojic koeficientů sousedních řádků je +1 nebo -1:
platí to na počátku a každý krok změní pouze znaménko.
Proto `gcd(s,t)=gcd(Q,Z)=1`. Pokud se zastaví až při r=0,
pak `Q=m/gcd(m,a)>1` a test `gcd(Q,0)=1` správně neprojde.

Pro (R1) lze bez zaokrouhlovací chyby použít
`X=Y=floor(sqrt(m/2))`, protože x,y jsou celá čísla.

## 3. Kandidát má nejmenší možný jmenovatel

Tvrdíme, že pro každé řešení (x,y) s `|y|<=Y` je `Q<=x`.
Pro Q=1 je to zřejmé. Jinak označme Q0 jmenovatel předchozího
konvergentu čísla a/m a r0 příslušný kladný zbytek. Konvergent
je useknutý pravidelný řetězový zlomek; vztah jeho jmenovatele
k Eukleidovým koeficientům je dokázán v úloze 48.
Z prvního zastavení máme `r0>Y`.

Dále `r0<=m/2`. Je-li a<=m/2, je to pravda pro všechny
relevantní zbytky. Je-li a>m/2, první podíl je 1, první dva
jmenovatele jsou 1 a další zbytek je m-a<m/2. Řádek s Q>1
tedy už má předchozí zbytek nejvýše m-a.

Označení `||v||` znamená vzdálenost reálného v od nejbližšího
celého čísla. Právě dokázaná mez dává `||Q0*a/m||=r0/m`.
Vlastnost nejlepší aproximace z §4.5.3-42, dokázaná v
[euclid-approximation.md](euclid-approximation.md), říká pro 0<x<Q:

```
||x*a/m|| >= ||Q0*a/m|| = r0/m > Y/m.
```

Kongruence případného řešení ale dává `||x*a/m||<=|y|/m<=Y/m`.
To je spor. Důkaz platí i pro poslední konvergent racionálního
a/m, kdy aktuální zbytek je nula.

## 4. Správnost a jednoznačnost pro čtvercovou mez

Nechť (x,y) splňuje (R1). Z §3 máme Q<=x<=theta. Obě dvojice
splňují kongruenci (R2), takže číslo `D=Q*y-x*R` je násobkem m.
Současně

```
|D| <= Q*|y|+x*|R| <= 2*theta^2 = m.                      (R3)
```

Rovnost |D|=m by vynutila `Q=x=|y|=|R|=theta` a opačná
znaménka y,R. Nesoudělnost x,y by pak dala theta=1, m=2,
což odporuje m>a>1. Proto D=0.

Protože (x,y) je nesoudělná dvojice a Q>0, z D=0 plyne
`(Q,R)=k*(x,y)` pro kladné celé k. Položme `z=(a*x-y)/m`;
jde o celé číslo a (R2) dává Z=k*z. Z `gcd(Q,Z)=1` dostaneme
k=1. Kandidát je tedy přesně požadované řešení. Pokud
neprojde některým závěrečným testem, žádné řešení neexistuje.

Stejný determinantový argument aplikovaný na dvě řešení
(R1) dokazuje jejich jednoznačnost. Nepotřebujeme předpokládat
prvočíselnost m ani nesoudělnost a,m.

## 5. Obdélníková mez a přesná výjimka z jednoznačnosti

Závěrečná poznámka knihy říká, že podobná metoda funguje při
`0<x<=X, |y|<=Y, 2*X*Y<=m`. Pro nalezení jednoho řešení je
to správně. Jednoznačnost sem nelze bez další podmínky přenést.

V důkazu (R3) nahradíme theta příslušnými X,Y. Případ |D|=m
vynucuje celočíselné `Q=x=X`, `|R|=|y|=Y`, `m=2*X*Y`
a opačná znaménka. Kongruence `a*X=±Y (mod 2*X*Y)` pak
vynutí X|Y. Z `gcd(x,y)=1` plyne X=1. Protože 1<a<m,
zůstává přesně výjimečná rodina

```
X=1,  m=2*Y,  a=Y>=2;
řešení (1,Y) a (1,-Y).                                   (R4)
```

Algoritmus v (R4) skončí okamžitě a vrátí (1,Y). V ostatních
případech argument D=0 z §4 platí beze změny. Pro porovnání
dvou libovolných řešení vede stejná rovnost k (R4); to je tedy
úplná klasifikace nejednoznačnosti. Při `2*X*Y<m` je řešení
vždy jediné. Kniha v závěrečné poznámce jednoznačnost znovu
netvrdí, proto tento okrajový jev není nový nález.

## 6. Nezávislé konečné kontroly a proces

[Verifier](../verify_euclid_reconstruction.py) porovnává zastavený
Eukleidův algoritmus s úplným procházením jmenovatelů a jejich
dvou možných zbytků r,r-m. V testovaném oboru Y<=m/2 toto
procházení nevynechá žádné přípustné y.

- 522753 čtvercových vstupů: všechna 3<=m<=1024, 2<=a<m;
  222654 řešení, z nich 204 na přesné hranici odmocniny.
- 215381 obdélníkových vstupů s m<=96, X,Y<=8, 2XY<=m;
  všech sedm nejednoznačných vstupů patří do (R4).
- Dalších 255 členů rodiny (R4), knižní příklad (316,41)
  a hranový vstup a=3,m=18 s řešením (1,3).

PID 1237182, relace 56538, limit 180 s. Všechny tři checkpointy
a závěrečné `passed` jsou zapsány; hlavní části trvaly 9.75 s
a 1.51 s. Následné vyzvednutí relace vrátilo stav 143 pro
obalový proces. Záznam proto netvrdí exit 0: úplné výsledky
assertů jsou doložené logem a JSON, obecný důkaz stojí samostatně.
Úspěšné kontroly nebyly opakovány.

## 7. Prameny a rozsah historické kontroly

[Kornerup–Gregory, BIT 23 (1983), 9–20](https://link.springer.com/article/10.1007/BF01937322)
má správné autory, ročník a strany. Získán byl také jejich
[preprint DAIMI PB-149 z 1982](https://tidsskrift.dk/daimipb/article/view/7423).
Vizuálně přečtené strany 1,8,13 potvrzují rekonstrukci rozšířeným
Eukleidovým algoritmem a mez `N<=sqrt((p-1)/2)`. Přiložené
errata, strany 2–3, upravují pomocná tvrzení. Nejde o úplný
audit tohoto článku; důkaz výše nezávisí na jeho nečtených částech.

[Wangův článek](https://link.springer.com/chapter/10.1007/3-540-12868-9_106)
má podle vydavatele správné údaje LNCS 162 (1983), 225–235;
abstrakt výslovně popisuje racionální rekonstrukci při faktorizaci.
Plný placený text nebyl získán. Bibliografická kontrola a vlastní
důkaz nejsou tvrzením, že byly prověřeny všechny důkazy pramenů.
