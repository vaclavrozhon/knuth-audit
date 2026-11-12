# §4.3.3E: synchronní automaty a úloha 11

Kontrola 2.11.2026. Vizuálně přečteny strany313–317 a odpověď11
na633–634. Zde dokazujeme správnost rovnic (57)/(58), tabulky2
a počet potřebných modulů. Historické odkazy a tvrzení o paralelních
obvodech na315–316 patří do navazujícího kontextu.

## Stav a rozdělení dílčích součinů

Modul M_j má stav `(c,x0,y0,x1,y1,x,y,z2,z1,z0)`; c má čtyři
hodnoty a dalších devět složek jsou bity. Jde tedy o2^11 stavů.
Všechny moduly současně počítají nový stav ze starých stavů sousedů.
Tři z-bity budeme společně označovat `S_j(t)=4z2+2z1+z0` v čase t.
Člen se součiny x,y v (58) označme P_j(t). Potom (58) říká

```
S_j(t+1) = z0_(j+1)(t)+z1_j(t)+z2_(j−1)(t)+P_j(t).
```

Pro levý okraj se místo z2_0(t) dosazuje vstupní bit q_t. Pravá
strana je nejvýše1+1+1+4=7, takže se opravdu vejde do tří bitů.
Čtyřstavový čítač je
`c_j(t)=min(3,max(0,t−3(j−1)))`, jak plyne indukcí z (57).

Položme a=3(j−1), A=2(j−1). Modul j začíná v čase a číst proud
bitů u_A,v_A; další vstup přichází v každém taktu. Zpoždění vstupu
o j−1 taktů plyne z kopírování x,y přes levé sousedy. Proměnné x0,y0
uchovají první pár, x1,y1 druhý a x,y poslední předchozí pár.
Pro lokální čas s=t−a je tedy P_j(t) rovno

```
s=0: u_A v_A,
s=1: u_A v_(A+1)+u_(A+1) v_A,
s=2: u_A v_(A+2)+u_(A+1) v_(A+1)+u_(A+2) v_A,
s>=3: u_A v_(A+s)+u_(A+1) v_(A+s−1)
      +u_(A+s−1) v_(A+1)+u_(A+s) v_A.
```

Před aktivací je P_j=0. Tato rozdělení tvoří disjunktní pásy všech
dvojic indexů: do modulu j patří právě součiny u_i v_l s
`floor(min(i,l)/2)=j−1`. Každý dílčí součin se tedy objeví jednou.
Jeho váha je `2^(i+l)=2^(4(j−1)+s)=2^(t+j−1)`.

## Zachování hodnoty a okamžité výstupní bity

Nechť B_(t−1) je hodnota bitů, které již byly vydány v časech
1,...,t−1. Pro t>=1 platí invariant

```
B_(t−1)+sum_(j>=1) 2^(t+j−2) S_j(t)
 = sum_(tau=0..t−1) [2^tau q_tau
                    +sum_(j>=1) 2^(tau+j−1) P_j(tau)].  (1)
```

V každém konečném čase je nenulových členů jen konečně mnoho.
Rovnice (1) plyne přímo ze stavového přechodu: bit z0 jde o modul
doleva, z1 zůstává a z2 jde o modul doprava. Jejich váhy se přitom
přesně zachovají; z0 prvního modulu se stává dalším výstupním bitem.
Na levém okraji přibude q_t s váhou2^t.

Každý dosud nepřidaný P_j(tau), tau>=t, má váhu dělitelnou2^t.
Ve stavovém součtu na levé straně je modulo2^t jediný možný člen
`2^(t−1) z0_1(t)`. Proto po jeho vydání máme přesně nejnižších t
bitů UV+q. To dokazuje správnost a načasování pro každý vstup,
nikoli jen konečné simulace. Pro n-bitové U,V,q je UV+q<2^(2n),
takže celých2n bitů je hotovo po2n taktech.

Při každém taktu pracují všechny moduly současně. Sekvenční
simulace tohoto pole proto sama o sobě není lineárním algoritmem
pro Turingův stroj; čas a počet současně činných součástek jsou
odlišné parametry.

## Počet modulů

Ve všech dosažitelných stavech nemůže mít M_j z2=1 dříve než v
čase3j−1, kdy jeho čítač poprvé dosáhne2. Před aktivací přicházejí
v x,y samé nuly a při prvním vstupu může vzniknout součet nejvýše2.
Indukcí v čase pak všechny tři z-bity M_j jsou nulové před časem
`3(j−1)`; první možná nenulová hodnota přichází právě od z2 vlevo.
To odůvodňuje první časový odhad tištěné odpovědi.

Kdyby z0_j(t)=1, má v (1) váhu2^(t+j−2). Všechny příspěvky jsou
nezáporné a jejich celková hodnota je nejvýše UV+q<2^(2n), takže
nutně `t+j−1<=2n`. Spolu s t>=3(j−1) dostaneme

```
4(j−1)<=2n, tedy j<=floor(n/2)+1.
```

Vzdálenější moduly mají z0 vždy0 a lze je odstranit, protože levý
soused jinou jejich složku nečte. Tím je horní mez dokázána.

Pro ostrost je potřeba rozlišit čisté UV a obecné UV+q. U lichého n
je poslední modul potřebný již pro dílčí součin u_(n−1)v_(n−1).
Pro sudé n>=4 můžeme vzít U=V=2^n−1,q=0. Pro proud samých
jedniček a q=0 dává dosazení do (58) následující profily S_j
od lokálního času t−a_j=0 (a_j=3(j−1)):

| Modul | lokální čas0 | 1 | 2 | 3 | každý čas>=4 |
|---|---:|---:|---:|---:|---:|
| j=1 | 0 | 1 | 2 | 4 | 4 |
| j=2 | 0 | 2 | 4 | 4 | 6 |
| j>=3 | 1 | 2 | 4 | 4 | 6 |

Před počátečním časem jsou S_j nulové. Tabulka je ověřitelná přímo
v přechodu (58): soused vlevo je o tři takty napřed a soused vpravo
o tři pozadu; po uvedených počátečních stavech se hodnoty ustálí.
Pro j=n/2+1>=3 je tedy z0_j(3(j−1))=1. Tento stav závisí jen na
vstupních bitech s indexem nejvýše `3(j−1)−j=2j−3=n−1`, protože
informace z levého okraje potřebuje nejméně j taktů. Stejný stav
proto nastane i pro konečné n-bitové operandy. Jeho vynechání
odebere kladný příspěvek k výstupu. Mez je ostrá.

Výjimka pro **čistý součin** je n=2: jeden modul vždy stačí.
Bez přídavného q nemá první modul nikdy z2=1 a modul2 zůstává
nulový. S nenulovým q už dva moduly potřeba jsou, například pro
U=V=q=3. Vymezení zadání vůči této možnosti je zaznamenáno jako
[C0105](C0105-automata-addend-scope.md), zatím pouze candidate.
Pro obecnou operaci UV+q je tištěná mez ostrá pro každé n>=1.

## Kontroly a tabulka

`verify_fast_automata.py` doslovně implementuje (57)/(58) se dvěma
oddělenými poli starých a nových stavů. Ověřuje (1), všechny výstupní
bity a výsledek proti nezávislému celočíselnému UV+q. Tabulka2 pro
U=V=23,q=11 má výsledek540 a výstup0,0,1,1,1,0,0,0,0,1,0,... .
Všech36 vytištěných stavů souhlasí s původní sazbou.

První ruční přepis čtyř buněk v časech8–10 byl chybný. Kontrola ho
odhalila, originál byl znovu přečten a přepis opraven; první neúspěšný
log je zachován. Nejde o chybu knihy a nebyl opakován žádný úspěšný
checkpoint.

Všechny čtyři vrstvy errat byly prohledány podle stran313–315/633–634,
automata/iterative array i odpovědi11. Úprava této konstrukce nebo
rozsahu úlohy11 nalezena nebyla; sousední známé opravy patří jiným
úlohám. Důkazy a konkrétní limity auditu jsou výše.

Běh6289,exit0,všechny tři checkpointy:36 stavů tabulky,4680
vyčerpávajících trojic U,V,q do4bitů,5120 dalších čistých součinů
a176 větších případů do127bitů.128 porovnání zkráceného pole
pro n1..64 potvrdilo potřebu posledního modulu s jedinou výjimkou
q0,n2; obecný důkaz výše pokrývá všechny n.
