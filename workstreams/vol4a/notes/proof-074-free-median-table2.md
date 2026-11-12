# Celá Table 2 a zbytek stran 70–71

Checkpoint X0103, P0967–P0972. Původní tabulka, všechna
jména/štítky i diagram na p71/file88 prohlédnuty ve
`images/proof-file088.png`; navazující text p70/file87
rovněž. P0897 už strukturálně klasifikuje všech 12
monotónních self-duálních funkcí čtyř proměnných a jejich
prime formy. Tento argument se nepřepočítává: zde se
doplňuje graf, tabulka, přesný průběh H a každý další
závěr textu. Žádný program nebyl spuštěn.

## Volná algebra a všechny funkce závislé na čtyřech proměnných — P0967

Množina všech monotónních self-duálních funkcí w,x,y,z
je uzavřena na bodový medián a obsahuje čtyři projekce.
Theorem P (P0826–P0830) ukazuje, že každý její prvek je
mediánovým termem projekcí. Dva termy určují tutéž
booleovskou funkci právě když jsou identitou všech
mediánových algeber, podle obecného principu 0–1 P0936.
Libovolné přiřazení čtyř generátorů do libovolné algebry
proto dává dobře definované vyhodnocení termů, které je
homomorfismem; je jediné, protože projekce generují.
Tím je doložen přesný význam „free median algebra“
v názvu tabulky, ne jen počet jejích prvků.

P0897 dává čtyři projekce, čtyři majority tří různých
proměnných a čtyři hvězdové funkce. Poslední mají tvar

    S_a=a(b∨c∨d)∨bcd=M(a,a,b,c,d),

kde a,b,c,d jsou čtyři různé proměnné. Rovnost plyne
po a=0 jako bcd a po a=1 jako b∨c∨d. Každá závisí
na všech čtyřech: význam a ukáže bcd=100, význam třeba
b ukáže a=0,c=d=1. Projekce závisí na jedné a ternární
majority na třech. To dokazuje celý poslední odstavec
p70 o všech funkcích skutečně využívajících čtyři vstupy.

## Všechna čísla v truth tables a sloupci štítků — P0968

Pořadí vstupů je lexikografické wxyz=0000,...,1111.
Nejprve omezme w=0, takže následujících osm bitů je
pořadí xyz=000,...,111. Označení A,...,H níže jsou
pouze místní zkratky pro dlouhá tištěná jména.

| značka | funkce | cofactor w=0 | prvních osm bitů | sedmibitový štítek |
|---|---|---|---|---|
| w | w | 0 | 00000000 | 0000000 |
| A | M(w,w,x,y,z) | xyz | 00000001 | 0000001 |
| B | M(w,y,z) | yz | 00010001 | 0010001 |
| C | M(w,x,y,z,z) | z(x∨y) | 00010101 | 0010101 |
| D | M(x,y,z) | xy∨xz∨yz | 00010111 | 0010111 |
| z | z | z | 01010101 | 1010101 |
| E | M(w,x,y,y,z) | y(x∨z) | 00010011 | 0010011 |
| y | y | y | 00110011 | 0110011 |
| F | M(w,x,z) | xz | 00000101 | 0000101 |
| G | M(w,x,x,y,z) | x(y∨z) | 00000111 | 0000111 |
| x | x | x | 00001111 | 0001111 |
| H | M(w,x,y) | xy | 00000011 | 0000011 |

Každý osmibitový řádek je přímým vyhodnocením uvedeného
cofactoru: např. yz je pravda pouze pro 011,111;
y(x∨z) pro 011,110,111; xz pro 101,111. Takto jsou
v tabulce uvedeny všechny pravdivé vstupy, včetně tří
jednoduchých periodických projekcí. První bit je vždy
0, protože monotónní self-duální funkce má f(0)=0;
f(0)=1 by monotónností dalo konstantu 1, která není
self-duální.

Druhých osm bitů je doplněk prvních osmi v opačném
pořadí: booleovský doplněk vstupu s pořadovým číslem
k má číslo 15−k a selfdualita dává f(15−k)=1−f(k).
Z tabulky proto vycházejí přesně vytištěné plné řetězce

    t(w)=0000000011111111,
    t(x)=0000111100001111,
    t(y)=0011001100110011,
    t(z)=0101010101010101,
    t(A)=0000000101111111.

Bodový pětičlenný medián t(w),t(w),t(x),t(y),t(z)
je právě poslední řetězec, podle obou cofactorů S_w
v P0967. Ze všech dvanácti prvních polovin po odstranění
úvodní nuly vzniká přesně sloupec l(s_j), bez permutace
v tomto konkrétním číslování.

## Všechny hrany a úplnost diagramu — P0969

V osmi bodech A,...,H je poslední bit stále 1, pozice
1,2,4 jsou 0 a pozice 3,5,6 tvoří celou krychli:

    A=000, B=100, C=110, D=111,
    E=101, F=010, G=011, H=001.

Zbylé w,z,y,x jsou po řadě listy připojené k A,C,E,G
vlastními unikátními bity 7,1,2,4. Celý graf je tedy
Q_3 se čtyřmi připojenými listy. Dvanáct krychlových hran
je rozděleno v následující tabulce tříd; čtyři listové
hrany ji doplňují. Přesně těchto 16 spojnic je v sazbě,
včetně zadních E–D, H–G a G–x; křížení čar není nový
vrchol.

Hammingova vzdálenost mezi dvěma core body je krychlová
vzdálenost. Mezi listem a core je navíc právě jeden
unikátní bit/krok; mezi dvěma různými listy právě dva.
Proto tento konkrétní graf realizuje všechny vzdálenosti
svých sedmibitových štítků. Žádné další dva štítky
vzdálené 1 jsme nevynechali.

Pro mediánovou algebru jsou její grafové hrany právě
tyto: dvojice vzdálená 1 nemá mezi svými štítky jiný
bod, zatímco mezi každou dvojicí vzdálenou >1 vede
uvedená cesta s vnitřním vrcholem. Bodový interval
obsahuje každý takový vnitřní vrchol. Tedy právě první
dvojice mají dvoubodový algebraický interval, jak
požaduje definice (61). Diagram je úplný, nikoli jen
některý podgraf odpovídajícího mediánového grafu.

## Sedm přesných tříd a jednoznačnost sloupců — P0970

| bitová pozice zleva | všechny hrany třídy |
|---|---|
| 1 | C–z |
| 2 | E–y |
| 3 | A–B, F–C, H–E, G–D |
| 4 | G–x |
| 5 | A–F, B–C, H–G, E–D |
| 6 | A–H, B–E, F–G, C–D |
| 7 | w–A |

Každý bit se na některé hraně mění a ostatní bity se
na té hraně nemění; dvě sloupcové funkce proto nemohou
být stejné nebo navzájem komplementární. Hodnota všech
sedmi je u w nulová. Vyhodnocení funkce při konkrétním
booleovském vstupu je homomorfismus mediánů. Argument
P0944 tedy každou tuto souřadnici ztotožní s projekcí
na hranu, na níž se mění. Tabulka tudíž obsahuje právě
všech sedm různých redukovaných hranových souřadnic.

P0950/P0957 nyní zaručují, že H dostane stejné štítky
až na permutaci sloupců při libovolném přípustném
pořadí sousedů. Výrok p71 o počtu jedniček i Hammingově
vzdálenosti byl už obecně doložen P0945 a zde se
přebírá pro tento konkrétní graf.

## Přesný master list a realizovatelné pořadí průchodu — P0971

Na počátku lze zachovat např. tato pořadí late sousedů:
A:(B,F,H), B:(C,E), C:(D,z), E:(D,y), F:(C,G),
G:(D,x), H:(E,G); w má jediný A a ostatní jsou listy
nebo D bez late souseda. Všechny early sousedy H1
zařadí před ně. Takové uspořádání splňuje H1; již
odstraněné položky se při pozdější volbě přirozeně vynechají.

Následující tabulka uvádí pro každou skutečnou fázi
její komponentu před řezem a pravou část pro rekurzi.
Levá část je její doplněk, takže žádné vrcholy nezmizí
bez uvedené rekurze nebo pozdějšího zpracování.

| j | r_j→s_j | bit řezu | živá komponenta C | pravá část R |
|---|---|---|---|---|
| 1 | w→A | 7 | všech 12 | A,B,C,D,E,F,G,H,x,y,z |
| 2 | A→B | 3 | A,B,C,D,E,F,G,H,x,y,z | B,C,D,E,y,z |
| 3 | B→C | 5 | B,C,D,E,y,z | C,D,z |
| 4 | C→D | 6 | C,D,z | D |
| 5 | C→z | 1 | C,z | z |
| 6 | B→E | 6 | B,E,y | E,y |
| 7 | E→y | 2 | E,y | y |
| 8 | A→F | 5 | A,F,G,H,x | F,G,x |
| 9 | F→G | 6 | F,G,x | G,x |
| 10 | G→x | 4 | G,x | x |
| 11 | A→H | 6 | A,H | H |

P0953–P0956 dokládají, že každý z těchto řezů skutečně
odstraní přesně příslušné hrany, než se začne další
rekurze. Pořadí uvnitř pomocné BFS nemění výslednou
komponentu ani master list. Tabulka proto není jen
spanning tree, který by mohl být s H neslučitelný:
je to celý platný sled jeho rekurzivních fází.

Doplňme přímou kontrolu každého výstupního kroku H3:
řádky po řadě mění bity 7,3,5,6,1,6,2,5,6,4,6
v dříve hotovém rodičovském štítku. V P0968 jde vždy
o změnu 0→1 a vznikne přesně uvedené l(s_j). Jména
r_j i s_j v sazbě po dosazení A,...,H přesně souhlasí.

## Sousedé a počet prime implicants — P0972

Každá hrana mění právě jeden ze sedmi uložených bitů;
ve druhé polovině plné truth table se tím obrátí právě
bit odpovídající komplementárnímu vstupu. Přesně dva
komplementární vstupy tak změní hodnotu, jak text říká.
Naopak každé sousedství je v úplném seznamu P0970.

Stupně všech 12 vrcholů a počty jejich prime implicants
jsou po třídách:

| vrcholy | grafový stupeň | prime implicants |
|---|---|---|
| w,x,y,z | 1 | jediný generátor |
| B,F,H,D | 3 | tři dvoučlenné dvojice příslušné trojice |
| A,G,E,C | 4 | ab,ac,ad,bcd pro opakovanou proměnnou a |

Prime formy v posledním sloupci i jejich úplnost byly
obecně dokázány P0897. Stupně vyplývají ze všech hran
P0970: krychlové vrcholy mají tři core sousedy a právě
hvězdovým vrcholům přibyl jeden list. Tím je doložena
poslední věta p71 pro každý z jejích vrcholů; žádná
pětivstupová tabulka úlohy84 se zde neprohlašuje za
spočítanou. Odkaz na70 je v této doméně n=4 oprávněný
(P0914), unary výjimka F0008 se sem nepřenáší.

## Úplné stránkové mapy a errata

P70: celý I1–I10, deklarovaná sémantika polí a rekurze
P0951–P0957; dvojité seznamy a všechny náklady P0964–P0966;
mez návštěv P0958; hranová mez P0959–P0963; všech 12
funkcí a pětičlenné formy posledního odstavce P0897/P0967;
konkrétní Table2 průběh P0971.

P71: caption/univerzální význam P0967; všechna jména,
řádky, rodiče, štítky a diagram P0968–P0971; libovolné
pořadí a vzdálenosti P0945/P0970; všechny plné truth
tables, jejich redukce a majority výpočet P0968;
dvoubitové změny a všechny stupně/prime počty P0972.

Obě stránky tedy nyní mají úplný argumentový rozsah.
Pět relevantních vrstev errat pro Table2/p70–71 prověřeno;
známé I4 už zohledněno v proof-072. Žádný další relevantní
záznam a žádný nový nález. P71 nemá další bibliografický
odkaz; historické meze algoritmické atribuce p69 zůstávají
výslovné v proof-072, nikoli matematickou mezerou tabulky.
