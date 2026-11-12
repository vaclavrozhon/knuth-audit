# Úloha 7.1.1–52: malé hry, obecná sémantika a pravděpodobnosti

Checkpoint X0081, P0758–P0768. Originál p86/file103 a odpověď
p544/file561, images/proof-file103.png a proof-file561.png.
Všech dvanáct výsledků pro n=2,3,4 je níže dokázáno ručně.
Dvacet výsledků pro n=5,…,9 se tím neprohlašuje za ověřené.
Žádný program, generování stavů nebo census.

## Přesný konečný herní model — P0758

Stav obsahuje n znaků z {*,0,1}, ukazatel m a hráče na tahu.
Z 0 je pro n≥2 první tah pouze do pozice2. Později je každé
navštívené m už přiřazené. Každý z nejvýše dvou dovolených
cílů m+2, m−1 dává buď dvě volby při prvním přiřazení,
nebo právě jedno povinné přepnutí. Proto má stav nejvýše
čtyři tahy, jak zadání tvrdí. Po přiřazení poslední * hra
končí ihned, před případným dalším přepnutím.

Dvě návštěvy stejného slova a stejného m během jedné partie
automaticky mají i stejného hráče na tahu. Mezi nimi nemohlo
dojít k prvnímu přiřazení (množina * už jen klesá). Každý
mezilehlý tah proto přepnul právě jeden bit; návrat stejného
slova vyžaduje sudý počet těchto přepnutí. Reprezentace se
samostatným příznakem hráče tedy nemění pravidlo opakování52.

Hrubá mez počtu stavů je 2n3^n plus dva počáteční stavy
s m=0. Zkonstruované terminály mají vítěze f(x), ostatní
stavy jsou neoznačené. P0753–P0756 pak dávají přesně klasifikaci
výhra/prohra/remíza od každého čerstvého počátečního stavu.
To je správnost metody, nikoli tvrzení, že byla tabulka spočítána.

## n=2: všechny čtyři hry — P0759

Jediná cesta ukazatele je 0→2→1, takže první hráč nastaví
b=x2 a druhý a=x1; druhý tah ihned končí.

* (a) f(ab)=[ab<ba]=¬a∧b. Je-li první hráč0, nastaví b=0;
  je-li druhý hráč0, nastaví a=1. Hráč0 vždy vyhraje.
* (b) Druhý hráč nastaví a tak, aby a XOR b bylo jeho číslo.
  Druhý hráč tedy vyhraje.
* (c) f(ab)=¬(a∧b). Hráč1 na prvním tahu volí b=0,
  na druhém a=0; vyhraje vždy.
* (d) Z hodnot0,1,2,3 jsou prvočísla2,3, tedy f(ab)=a.
  Druhý hráč přímo zvolí výsledek a vyhraje.

Žádná z těchto cest nemůže skončit opakováním.

## n=3: všechny čtyři hry — P0760

Ukazatel musí projít 0→2→1→3. První hráč nastaví b=x2,
druhý a=x1 a první dokončí c=x3.

* (a) f(abc)=[a<c]. Je-li hráč0 první, dokončí c=0;
  je-li druhý, nastaví a=1. Hráč0 vždy vyhraje.
* (b) První hráč posledním c nastaví požadovanou paritu.
* (c) f=¬b∨(¬a∧¬c). První hráč1 volí b=0.
  První hráč0 volí b=1 a pak c=1. První hráč vždy vyhraje.
* (d) Prvočísla pod8 jsou2,3,5,7. Pro a=0 je f=b,
  pro a=1 je f=c. První hráč j volí b=j a pak c=j,
  takže vyhraje nezávisle na a.

Malý seznam prvočísel je přímo doložen: 0,1 nejsou prvočísla,
4 a6 jsou sudé složené a pro2,3,5,7 stačí test možných
dělitelů do odmocniny. Nebyl spuštěn testovací program.

## n=4: úplný rozklad možných tahů — P0761

Označme slovo abcd, první hodnotu pozice2 jako β.
První čtyři tahy mají nutně tvar

    0→2→(1 nebo4)→3→2.

Druhý hráč tedy zvolí krajní pozici a její bit z,
první hráč pak zvolí c; čtvrtý tah druhého hráče musí
přepnout b, takže v centrálním stavu m=2 je b=1−β.
První hráč je znovu na tahu. Právě jedna krajní pozice
je dosud *, všechny ostatní jsou přiřazené.

První hráč nyní buď navštíví nepřiřazený kraj, zvolí jeho
bit a ihned ukončí hru; nebo navštíví již přiřazený kraj.
Druhá možnost nutně vykoná okruh kraj→3→2: přepne všechny
tři známé bity a prohodí hráče na tahu. Po druhém takovém
okruhu by se opakoval stejný centrální stav, což je remíza.
Tím jsou vyčerpány všechny možnosti, ne jen zvolené svědecké cesty.

Pro centrální stav tedy platí: může-li aktivní hráč ukončením
získat svou hodnotu, vyhraje hned. Nemůže-li, musí pro neprohru
zvolit okruh; pokud pak soupeř může vyhrát ukončením, je stav
prohraný. Pokud ani soupeř nemůže vyhrát ukončením, oba se
mohou vyhnout prohře okruhem a dosáhnou remízy.

## n=4, hra(a) a tvrzení o prvním tahu — P0762

Máme

    f(abcd)=[a<d] ∨ ([a=d] ∧ t),    t=¬b∧c.

Je-li neznámé d a známé a=0, lze dostat1 vždy a0 právě při t=0.
Při známém a=1 lze dostat0 vždy a1 právě při t=1.
Symetricky, je-li neznámé a: při d=0 lze dostat0 vždy a1
právě při t=1; při d=1 lze dostat1 vždy a0 právě při t=0.
Tyto čtyři případy plynou přímým dosazením obou hodnot
jediného nepřiřazeného bitu.

První hráč0 zvolí c=0, takže t=0 a vždy může skončit s f=0.
První hráč1 zvolí β=1 a c=1, takže po přepnutí b máme
b=0,t=1 a vždy může skončit s f=1. Proto první hráč vyhraje.

Zbývá neobvyklý dodatek o první volbě hráče1. Pokud zvolí
β=0, máme v centrálním stavu b=1,t=0. Druhý hráč0 může
zvolit kraj a=1 nebo kraj d=0. V obou případech je f=0
při každém přímém dokončení; hráč1 musí pro neprohru zvolit okruh.

Po okruhu se známý kraj změní na a=0 nebo d=1, b na0
a c na1−c, tedy nový t=1−c. Zvolil-li hráč1 c=1, soupeř0
teď může dokončit s f=0 a vyhraje. Zvolil-li c=0, nový t=1
a soupeř0 naopak nemůže dokončit jinak než s f=1; může
zvolit druhý okruh a remizovat. Hráč1 tedy zajistí alespoň
remízu volbou c=0, ale soupeřovou krajní volbou nemůže
vynutit výhru. To dokazuje přesně „*0** draws“ a nutnost
výherního prvního tahu *1**, nikoli jen jeho postačitelnost.

## n=4, hry(b),(c),(d) — P0763

V centrálním stavu může první hráč skončit už pátým tahem.

* (b) Zvolí poslední bit k požadované paritě. Vyhraje první.
* (c) První hráč1 volí β=1, c=0. Po přepnutí je b=0;
  nepřiřazený kraj doplní0, takže bez ohledu na druhý kraj
  nevznikne11. První hráč0 volí β=0,c=1, takže při ukončení
  má b=c=1 a jistě f=0. Vyhraje první.
* (d) První hráč1 volí β=1,c=1, tedy při dokončení b=0.
  Je-li neznámé d, zvolí d=1 a dostane3 nebo11; je-li
  neznámé a, zvolí a=0 a dostane2 nebo3. Vše jsou prvočísla.
  První hráč0 volí β=0, takže b=1. Je-li známé a, zvolí
  c=0,d=0 a dostane4 nebo12. Je-li známé d=0, zvolí c=0,a=0
  a dostane4; při známém d=1 zvolí c=1,a=1 a dostane15.
  Vše jsou složená čísla. Vyhraje první.

Ve všech případech první hráč vynutí výhru bez okruhu.
Obecná úplnost P0761 také vylučuje jiné nepostihnuté odbočky.

## Palindromy a význam „nevýhody“ v(a) — P0764

Palindrom je určen prvními ceil(n/2) bity, takže jich je
2^ceil(n/2). Každý nepalindromický řetězec tvoří s obráceným
řetězcem dvojici, v níž právě jeden má f=1. Proto rovnoměrná
pravděpodobnost hodnoty1 je

    (2^n−2^ceil(n/2))/2^(n+1) < 1/2.

To je přesný statický smysl vlivu palindromů; samotná nerovnost
pravděpodobností neimplikuje strategickou výhodu.
Zvláštní komentář o dopadu na n=7 patří k dosud nedoloženému
většímu hernímu případu P0768, nikoli k tomuto počtu.

## Hra(b) jako závod o poslední * — P0765

Při posledním prvním přiřazení je poslední bit ve funkci XOR
s koeficientem1. Aktivní hráč j může nastavit tento bit na
j XOR (parita všech ostatních), takže vyhraje bez ohledu
na dřívější přepínání. Jiná možnost ukončení s výhrou není;
opakování dává remízu. To přesně ospravedlňuje komentář
o závodu o poslední *, ale samo neurčuje všech osm řádků tabulky.

## Fibonacciho pravděpodobnost hry(c) — P0766

Počet A_n řetězců bez dvou sousedních jedniček splňuje
A_0=1,A_1=2 a A_n=A_(n−1)+A_(n−2): řetězec končí0,
nebo končí01 (pro n≥2). Tyto dvě možnosti jsou disjunktní
a odstraněním příslušné koncovky dávají bijekce. Proto
A_n=F_(n+2), při F_0=0,F_1=1.

Pro φ=(1+sqrt5)/2 platí φ²=φ+1. Indukce z prvních dvou
hodnot dává φ^n≤A_n≤(2/φ)φ^n. Dělení 2^n dokazuje
přesně F_(n+2)/2^n=Θ((φ/2)^n). Žádná stochastická
nezávislost mezi sousedními dvojicemi se nepředpokládá.

## Prvočíselná pravděpodobnost hry(d) — P0767

Samostatná F0007-prime-bit-probability.md dokazuje

    π(2^n−1)/2^n = Θ(1/n), nikoli vytištěné Θ(1/log n).

Horní mez má vlastní elementární binomický důkaz; dolní
Chebyshevova mez je přesně převzata z V2 discrete-log.md §4
bez přepočítání starých výsledků. Originál a všech pět
relevantních vrstev errat zkontrolovány. F0007 confirmed/low,
jen komentář p544/file561, nikoli herní tabulka.

## Přesně otevřená část tabulky a dodatků — P0768 partial

Následujících dvacet buněk pro n=5,…,9 má stále pouze knižní
odpověď; nebyla ověřena strategií, rankovým certifikátem ani během:

| n | (a) | (b) | (c) | (d) |
|---|---|---|---|---|
| 5 | second | draw | draw | 1 loses if first |
| 6 | second | second | 1 loses if first | 1 loses if first |
| 7 | 1 loses if first | second | 1 loses if first | 1 loses if first |
| 8 | draw | draw | draw | 1 loses if first |
| 9 | draw | draw | draw | 1 loses if first |

„1 loses if first“ znamená podle výslovné knižní definice:
začíná-li0, remíza; začíná-li1, vyhraje0. Každá buňka tak
zahrnuje dvě počáteční identity hráče, nikoli jedinou partii.

S těmito buňkami zůstává otevřen i komentář o vlivu palindromů
pro n=7 a strategické srovnání(c) proti(d) pro n=5,…,9.
Pro n=2,3,4 je srovnání už doloženo: při n=2 si1 vede v(c)
přísně lépe, při n=3,4 jsou oba výsledky stejné.
Pravděpodobnostní asymptotiky nemohou větší tabulku nahradit.

Další krok je malý přesný herní argument pro nejstarší
neuzavřený případ n=5; nepřeskakovat tabulku jako vyřešenou
a nespouštět kvůli ní brute-force census. Strany86/544
zůstávají částečné. Main-text p60/file77 a čtení p218/file235
se nezaměňují s tímto lokálním herním kurzorem.

Dodatek X0082: celý řádek n=5 i srovnání(c)/(d) je nyní
uzavřen v proof-053-boolean-games-five.md, P0769–P0775.
P0768 proto aktuálně ponechává šestnáct buněk n=6,…,9;
seznam dvaceti výše zachycuje původní stav při X0081.

X0083: P0776–P0781 v proof-054-boolean-games-six.md uzavírají celý
řádek n6 a jeho srovnávací komentář. P0768 nyní označuje jen
dvanáct buněk n7–9, nikoli původní tabulku dvaceti mezer.

X0084: P0782–P0787 v proof-055-boolean-games-seven.md uzavírají celý
řádek n7, palindromický efekt a jeho srovnání(c)/(d). P0768 nyní
označuje jen osm buněk n8/9 a jejich srovnání.

X0085: proof-056 uzavírá n8(a)/(b) a začátek0 v n8(c)/(d).
P0768/P0794 ponechávají začátek1 v těchto dvou buňkách, celé n9
a závislé srovnání. Jde o šest částečných buněk, nikoli uzavřenou52.
