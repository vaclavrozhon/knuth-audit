# Úloha 84: všech 81 funkcí, všechny hrany a přesné meze dodatku

Checkpoint X0108, P1015–P1026. Zadání p91/file108,
odpověď p550/file567 a detail celé tabulky prohlédnuty.
Jde o strukturální důkaz, nikoli o census. Přiložený
program přímo vypisuje prokázané třídy; nebyl spuštěn.
Počty pro šest proměnných a přesná externí asymptotika
zůstávají oddělené od dokončené pětivstupové úlohy.

## Přesné parametrizování funkcí — P1015

Vstup ztotožníme s množinou jeho jedničkových proměnných
v pětiprvkové množině V. Monotónní selfdualní f má
f(∅)=0 a f(V)=1. Jestliže f({z})=1, monotónnost dává
f(S)=1 pro z∈S a selfdualita f(S)=0 pro z∉S. Jde
přesně o projekci z, tedy jednu z pěti možností.

Ve všech ostatních případech jsou singletony nepravdivé,
čtyřprvkové množiny pravdivé a funkci určují její
pravdivé dvojice E. Trojice S je pravdivá právě když
V\S∉E. Dvě disjunktní dvojice A,B nemohou být v E:
A⊆V\B, ale f(A)=1 a f(V\B)=0 by porušilo monotónnost.
E je tedy navzájem se protínající rodina hran K5.

Obráceně každá taková E určuje uvedeným předpisem
selfdualní funkci. Jediný netriviální přechod v
monotónnosti je z pravdivé dvojice A do trojice S⊃A.
Nepravdivost S by znamenala V\S∈E, disjunktní s A.
To je zakázáno. Všechny ostatní přechody mezi sousedními
velikostmi jsou okamžité. Parametrizace je oboustranná
a jednoznačná.

## Všech sedm typů a počet 81 — P1016

Neprázdná rodina navzájem se protínajících hran je
buď hvězda, nebo celý trojúhelník či jeho podrodina.
Přesně: obsahuje-li různé hrany ab,ac, každá další
hrana buď obsahuje a, nebo musí být bc. Pokud bc
opravdu patří do rodiny, žádná ad s d mimo {b,c}
už neprotíná bc; rodina je tedy uvnitř trojúhelníku.
Jinak mají všechny hrany společný vrchol a.

Tato klasifikace dává přesně následující typy v
pořadí tištěné tabulky:

| typ | popis | počet |
|---|---|---|
| 1 | projekce | 5 |
| 2 | čtyřhranová hvězda | 5 |
| 3 | tříhranová hvězda | 5·4=20 |
| 4 | dvouhranová hvězda | 5·binom(4,2)=30 |
| 5 | jediná hrana | binom(5,2)=10 |
| 6 | prázdná rodina | 1 |
| 7 | trojúhelník | binom(5,3)=10 |

U hvězd s aspoň dvěma hranami je střed jednoznačný;
u jediné hrany proto střed vůbec nevolíme. Žádný
typ ani žádná funkce se nepočítá dvakrát. Součet je
5+5+20+30+10+1+10=81. Klasifikace je vyčerpávající,
ne pouze ověření sedmi nalezených příkladů.

## Všechny tištěné reprezentanty jako mediány lichého počtu — P1017

Medián lichého počtu výskytů proměnných je práh na
součtu jejich četností. Uvedeme váhy v pořadí v,w,x,y,z;
hodnota je jedna právě při dosažení vytištěného prahu.

| typ | tištěný reprezentant | váhy | práh | E |
|---|---|---|---|---|
| 1 | ⟨z⟩ | (0,0,0,0,1) | 1 | projekce |
| 2 | ⟨vwxyzzz⟩ | (1,1,1,1,3) | 4 | zv,zw,zx,zy |
| 3 | ⟨wxyzz⟩ | (0,1,1,1,2) | 3 | zw,zx,zy |
| 4 | ⟨vwxxyyzzz⟩ | (1,1,2,2,3) | 5 | zx,zy |
| 5 | ⟨vwxyyzz⟩ | (1,1,1,2,2) | 4 | yz |
| 6 | ⟨vwxyz⟩ | (1,1,1,1,1) | 3 | ∅ |
| 7 | ⟨xyz⟩ | (0,0,1,1,1) | 2 | xy,xz,yz |

V každém neprojekčním řádku je každá jednotlivá váha
menší než práh a právě uvedené dvojice jej dosahují.
Například u typu 4 mají váhu aspoň 5 pouze zx a zy;
xy má jen 4 a každá jiná dvojice nejvýše 4. Součet
vah je lichý, takže funkce je selfdualní. P1015 pak
určuje všechny její ostatní hodnoty. Permutace
proměnných dává celou danou třídu. Tím je dokázáno
i tvrzení, že každá z 81 funkcí má jednoduchou
reprezentaci jako medián lichého počtu výskytů.

## Proč hrany znamenají právě jednu změnu — P1018

Všechny funkce jsou uzavřeny na bodový medián: ten
zachová monotónnost i selfdualitu. Štítek tvoří pět
hodnot na singletonech a deset na dvojicích. Ostatní
hodnoty jsou buď konstantní, nebo jejich doplňky,
takže jde o injektivní mediánový homomorfismus.

Každá z patnácti souřadnic je potřebná. Pro dvojici
ab dávají E=∅ a E={ab} svědky lišící se právě v
této hodnotě. Pro singleton z dávají svědky projekce
z a čtyřhranová hvězda se středem z: jejich dvojicové
hodnoty jsou stejné a singletonové se liší jen v z.
Jde proto o redukovanou mediánovou množinu podle
P0994/P0995. Její grafové hrany jsou přesně změny
jediné z těchto souřadnic, nikoli jen některé takové
změny.

Mezi neprojekčními vrcholy tedy hrana přidá nebo
odebere právě jednu hranu E a musí zachovat vzájemné
protínání. Projekce z má jediného souseda, svou
čtyřhranovou hvězdu: ponechání pravdivého singletonu
z už nutí celou projekci a při jeho jediném flipu
jsou ostatní hodnoty zcela určeny.

## Všichni sousedé, všechny stupně a každý příklad v tabulce — P1019

U následujících popisů jsou všechny uvedené možnosti
opravdu různé; klasifikace P1016 vylučuje jakéhokoli
dalšího souseda.

| typ | všechny změny | počty sousedů podle typu | stupeň |
|---|---|---|---|
| 1 | flip singletonu | 1 typu 2 | 1 |
| 2 | přidat pravdivý singleton středu; odebrat jednu ze 4 hran | 1 typu 1, 4 typu 3 | 5 |
| 3 | přidat chybějící hranu hvězdy; odebrat jednu ze 3 | 1 typu 2, 3 typu 4 | 4 |
| 4 | přidat jednu ze 2 dalších hran středu; doplnit trojúhelník; odebrat jednu ze 2 | 2 typu 3, 1 typu 7, 2 typu 5 | 5 |
| 5 | přidat jednu ze 6 hran protínajících danou hranu; odebrat ji | 6 typu 4, 1 typu 6 | 7 |
| 6 | přidat libovolnou z 10 hran | 10 typu 5 | 10 |
| 7 | odebrat jednu ze 3 hran | 3 typu 4 | 3 |

Reprezentativní sousedé v původní tabulce jsou přesně
tyto povolené změny: typ 2 ztrácí zv do ⟨wxyzz⟩;
typ 3 ztrácí zw do ⟨vwxxyyzzz⟩. Typ 4 přidá xy
do ⟨xyz⟩, přidá zw do ⟨wxyzz⟩, nebo odebere zx
do ⟨vwxyyzz⟩. Typ 5 může přidat zx do typu 4 nebo
odebrat yz do ⟨vwxyz⟩. Poslední dva řádky jsou
přesně opačné změny. Symetrie proměnných dává všechny
ostatní sousedy daného typu.

Celý graf má odvozeně 185 hran: mezi typy 1–2,2–3,
3–4,4–5,4–7,5–6 je postupně 5,20,60,60,30,10 hran.
Stejný součet dává polovina součtu stupňů. Žádná
počtová shoda nenahrazuje předchozí důkaz úplnosti.

## Požadovaný program a jeho argument — P1020

`scripts/median5_structural.py` generuje přímo sedm
prokázaných rodin. Smyčky jsou konečné a jejich
indexy jsou právě jednoznačné parametry P1016.
Nevybírá z 2^(2^5) pravdivostních tabulek a netestuje
podmnožiny možných hran. Funkce `value` implementuje
jednotlivé velikosti množin z P1015 a zvlášť projekce.
Každý vrchol dostane úplnou pravdivostní tabulku
v pořadí bitových masek 0,...,31 a patnáctibitový
štítek z P1018.

Slovník štítek→index je injektivní. Pro každý vrchol
a každý z patnácti bitů program hledá štítek s jediným
flipem; P1018 dokazuje přesnou ekvivalenci s hranou.
Podmínka index<jiný_index vydá každou neorientovanou
hranu právě jednou. P1016/P1019 tak dokazují úplnost
a správnost obou výstupních seznamů.

Počet vyhodnocení `value` je přesně 81·(32+15),
počet slovníkových hledání 81·15. Jedno vyhodnocení
použije konstantně mnoho operací na pěti bitech a
rodině nejvýše čtyř dvojic. Paměť odpovídá seznamům
81 vrcholů a 185 hran plus slovníku. Jde o přímý
výpis, nikoli o experimentální potvrzení počtů.
Program nebyl spuštěn; pouze syntaxe a přesná vazba
jeho větví na důkaz byly zkontrolovány.

## Tištěný šestivstupový protipříklad jednoduchému mediánu — P1021

Nechť

    h = m(m(a,b,d), m(a,c,e), m(b,c,f)).

Je monotónní a selfdualní jako kompozice mediánů.
Je pravdivý na čtyřech koalicích

    abc, ade, bdf, cef.

Na abc jsou pravdivé všechny tři vnitřní mediány;
na každé z dalších koalic právě příslušné dva.
Na čtyřech doplňcích def,bcf,ace,abd je proto
nepravdivý. Každá proměnná se v první čtveřici
vyskytuje právě dvakrát a ve druhé také dvakrát.

Kdyby šlo o prahovou funkci s jakýmikoli reálnými
váhami a prahem T, součet vah čtyř pravdivých vstupů
by byl aspoň 4T, zatímco součet čtyř nepravdivých
by byl menší než 4T. Součty jsou však přesně stejné.
Spor. Tím je zvláště vyloučen medián lichého počtu
opakovaných vstupů, který je prahový s nezápornými
celočíselnými váhami. Příklad není jen nenalezená
reprezentace; má obecný certifikát neexistence.

## Přesná vzdálenost v obecné volné algebře — P1022

Pro n≥2 vezměme všechny monotónní selfdualní funkce.
Jako souřadnice stačí jeden vstup z každé dvojice
S,V\S kromě konstantního páru ∅,V; je jich
2^(n−1)−1. Abychom mohli použít isometrii, doložíme
jejich skutečnou redukovanost pro každé n.

Pro neprázdné vlastní S velikosti k zvolme j∉S.
Dejme váhu 1 členům S, váhu k−1 proměnné j a váhu
0 ostatním. Celková váha je 2k−1 a práh k, takže
jde o monotónní selfdualní funkci, na níž S je
minimální pravdivý vstup. P0913/P0914 dovoluje
flipnout právě S a jeho doplněk, se zachováním
monotónnosti i selfduality; n≥2 je zde výslovný.
Obě funkce jsou svědky přesně jedné evaluační
souřadnice. Není předpokládána neprokázaná
neredundance celé pravdivostní tabulky.

Souřadnicový medián zachovává třídu funkcí, takže
P0995 a P0945 dávají isometrický graf na těchto
redukovaných štítcích. Vzdálenost f,g je přesně
polovina počtu úplných vstupů, na nichž se liší;
druhý člen každého komplementárního páru přispívá
stejný rozdíl. Pro n=1 je jediný vrchol a žádná
dvojice různých projekcí.

## Projekce opravdu dosahují průměru grafu — P1023

Dokážeme potřebnou korelační nerovnost přímo.
Pro monotónní booleovské f,g na rovnoměrném
n-bitovém vstupu platí E(fg)≥E(f)E(g). Pro n=0
je rovnost. Podmiňme první bit hodnotou b a označme
a_b=E(f|b), c_b=E(g|b). Indukce dává
E(fg)≥(a_0c_0+a_1c_1)/2. Rozdíl této pravé strany
a E(f)E(g) je (a_1−a_0)(c_1−c_0)/4≥0.
To je celý indukční důkaz pro každý n.

Selfdualita dává E(f)=E(g)=1/2, tedy
Pr(f≠g)=1−2E(fg)≤1/2. P1022 pak dává
d(f,g)≤2^(n−2). Dvě různé projekce se liší
na přesně polovině vstupů, a jejich vzdálenost
je tudíž právě 2^(n−2). Jsou vždy nejvzdálenější,
jak tvrdí poslední věta odpovědi 84.

Primární Kleitmanův článek má na p154 stejnou
korelaci ve formě nerovnosti pro rostoucí a klesající
rodinu; její dosazení U={f=1}, L={g=0} je též
přímo použitelné. Zde máme vlastní úplný argument,
nikoli pouze odkaz na jméno nebo nepříbuznou
Kleitmanovu větu o průměru podmnožin krychle.

## Přesná vazba na maximal intersecting families — P1024

Pravdivé vstupy monotónní selfdualní funkce tvoří
protínající rodinu: disjunktní pravdivé A,B by
daly A⊆V\B a spor s monotónností. Obsahuje
právě jednu množinu z každé komplementární dvojice,
takže je maximální protínající rodinou.

Naopak maximální protínající rodina je nahoru
uzavřená, protože nadmnožinu jejího členu lze
vždy přidat. Není-li A v rodině, maximalita dává
její člen B disjunktní s A, tedy B⊆V\A; uzavřenost
nahoru dává V\A v rodině. Oba doplňky současně
patřit nemohou. Indikátor je proto monotónní
a selfdualní. Jde o přesnou bijekci pro n≥1,
takže počty v citované teorii opravdu znamenají M_n
z odpovědi 84.

## Přesné otevřené dodatky — P1025/P1026

P1025: Primární článek Erdős–Hindman, *Enumeration
of intersecting families*, Discrete Math. 48 (1984),
61–65, má v §3, Corollary 3.5, příslušný asymptotický
výsledek pro počet maximálních protínajících rodin.
Primární webový PDF text a metadata byly dostupné,
ale OCR koeficientu je porušené, lokální stažení
vracelo 403 a náhled nástroje neposkytl čitelnou
sazbu. Přesná rovnost s vytištěným ekvivalentem
binom(n−1,floor(n/2)) proto zůstává partial.
Bijection P1024 je plně dokázána, ale není sama
důkazem hluboké asymptotiky. Celou externí teorii
zde nezávisle nerekonstruujeme.

P1026: Tři šestivstupové census údaje 2646 funkcí,
30 typů a 21 typů s jednoduchou lichou mediánovou
reprezentací zůstávají neověřené. Přesný zdroj
Meyerowitz je identifikován dřívější primární
bibliografií; úplný článek nebyl dostupný. Nebyl
spuštěn nový census ani rozhodování váženosti všech
tříd. Jediný zde vytištěný šestivstupový svědek je
naopak úplně vyřešen v P1021.

Von Neumann–Morgenstern 1944, §52.5, historická
enumerace/terminologie simple games a priorita
nebyly nezávisle ověřeny: bibliografická výjimka.
Pět relevantních vrstev errat (`all4a-pre`, `all4a`,
`err4a`, `all4f0`, `err4f0`) pro tuto úlohu a
odpověď prověřeno; žádná příslušná oprava nenalezena.
Žádný nový nález. Samotná úloha 84 i celá její
pětivstupová tabulka jsou dokončeny; dodatky mají
výše uvedené dva přesné matematické limity. P550
zůstává partial i kvůli dalším dosud neuzavřeným
odpovědím 85–88.
