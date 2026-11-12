# §5.2.1: celé ProgramM,34–36

2026-11-07. P0900–0909. Originály99/file110,100/file111,
104/file115,625/file636 a626/file637 zobrazeny. Známé LD3→LD4
na100(2008) zohledněno; není nový nález. Pět vrstev přebírá
`sources/insertion-errata-review.json`. Matematika bez programu.
Dosud neuzavřená distribuce a asymptotika101–102/37–40 následují.

## P0900: předpoklady a celý více-seznamový invariant

Rozdělme uspořádanou doménu klíčů na M≥1 po sobě jdoucích intervalů.
M hlaviček a jeden LINK na každý z N záznamů stačí: seznamy si
nekonkurují o samostatné pevné kapacity, každý uzel už má místo
v původním vstupu. Po každém vložení jsou zpracované záznamy rozděleny
podle intervalu právě jednou, v každém seznamu vzestupně. Inicializace
dává prázdné seznamy; vložení do právě jednoho z nich přebírá celý
invariant L v P0885–0886, s explicitním testem prázdné hlavičky.
Ostatní seznamy se nemění. Složení neprázdných seznamů v pořadí
intervalů proto dává globálně seřazený seznam.

V ProgramM se postupuje odzadu a vloží před první rovný klíč;
stabilita proto platí i při opakování hodnot. V úvodní ilustraci se
postupuje dopředu; pro16 různých klíčů je výsledné pořadí stejné.
Klíče není nutné fyzicky přesouvat. Prostor je N linků+M hlaviček
a O(1) registrů; při M=Θ(N) jde o lineární pomocnou paměť. Analogii
s knihovnou a „probably best use“ nelze číst jako univerzální optimum
mezi všemi reprezentacemi. Distribution counting je příslušný příklad
adresování podle klíče, s již doloženým blokem P0651–0659/C0009.

**Pravděpodobnostní model:** binomické počty a následující momenty
potřebují nezávislé výběry intervalů s pravděpodobnostmi1/M, nikoli
pouze stejné marginály. Relativní pořadí různých klíčů uvnitř každého
intervalu je rovnoměrné (např. nezávislé stejně rozdělené spojité
klíče). Model je také výslovný v úloze38. Správnost programu tento
pravděpodobnostní předpoklad nepotřebuje. Samotné rovnoměrné
marginály by nestačily: všechny klíče mohou sdílet jednu náhodnou
buňku. Tento rozdíl je omezení použitého modelu, nikoli hlášená chyba.

## P0901: všech16 buněk vytištěné tabulky99

Po prvních4 klíčích mají intervaly seznamy(061,087),(),(503,512),().
Další908,170,897,275 přidají170 do1,275 do2 a897,908 do4.
Další653,426,154,509 přidají154 do1,426 do2 a509,653 do3.
Poslední612,677,765,703 přidají612,677,703 do3 a765 do4.
Tím jsou doloženy všechny čtyři vytištěné sloupce, včetně prázdných
seznamů. Konečné intervaly mají velikosti4,2,7,3 a dohromady všech16
původních klíčů, ve správném vzestupném pořadí.

## P0902: každá aritmetická a adresová část ProgramM

Pišme b=BYTESIZE. KEY=(1:3), LINK=(4:5),0≤K_j<b³. Všechny
adresy, rozdíly adres a N,M musí být reprezentovatelné, oblasti
programu, vstupu a hlaviček disjunktní, N,M≥1. To jsou stejné
paměťové předpoklady jako u L; cyklus není vydáván za bezpečný pro
počáteční N=0 nebo M=0. Abstraktní prázdný případ se zachytí předem.

03 nastaví I2=M;04–06 nulují celé HEAD+M,…,HEAD+1, každý právě
jednou.07 nastaví I1=N.08 načte K_j zarovnané vpravo do A.
Literál=M(1:3)= má hodnotu M b². Součin na09 je M K_j b²;
horních pět bytů rA je tedy d=floor(M K_j/b³),0≤d≤M−1.
10 vloží d do adresové části následující ENT4,11 tak nastaví I4=d.
I4 se nerozšíří za reprezentovatelný rozsah, protože d<M.
12 nastaví I3=HEAD+1−INPUT+d, takže INPUT+I3 ukazuje přesně
na hlavičku intervalu d+1.13 znovu načte celý původní záznam;
porovnání15 používá pouze KEY, takže LINK ani výsledek násobení
neovlivňují porovnání. Pro celočíselné klíče je adresování přesné i na
hranicích floor(MK/b³); nikdy nevznikne hlavička M+1.

## P0903: každý přechod vkládací smyčky

14 skočí nejprve na18, které načte p=LINK(q), q=I3, do I2.
19 porovnává klíč pouze při p>0. Je-li hlava prázdná, jde rovnou
na20.15/16 zastaví při K_j≤K_p; jinak17 nastaví q=p a18/19
postoupí na další uzel. To je přesně konečný sken L, nyní platný
i pro prázdný seznam.20/21 změní q→p na q→j→p, aniž zasáhnou
KEY.22/23 zmenší j a opakují právě pro j>0. Každé vložení zachová
rozdělení do intervalů i stabilitu. Při N=1 se provede jedno vložení
do prázdného seznamu a bezpečně skončí, bez klíčového porovnání.

## P0904: všechny četnosti a přesná cena

Pro j nechť b_j počítá pozdější menší klíče **v témže intervalu**.
Každý se právě jednou přeskočí, tedy Σ b_j=B. Konečné porovnání
chybí právě tehdy, je-li j přísným maximem svého intervalového
suffixu, včetně jeho posledního prvku. Jejich celkový počet je A.
Proto15/16 proběhnou B+N−A,17 B,18/19 B+N a20–23 N krát.
Všechny08–14 rovněž N krát. To platí při rovnostech s přísnými
inverzemi/maximy; uniformní permutační momenty pak už vyžadují
různé klíče. Při M=1 je A celý počet pravostranných maxim, o1 více
než A v původním ProgramL.

MIX ceny jednotlivých bloků:

    03,07             2
    04–06             4M
    08–14             19N = (2+10+2+1+1+2+1)N
    15–16             3(B+N−A)
    17                B
    18–19             3(B+N)
    20–21             4N
    22–23             2N.

Součet je **7B+31N−3A+4M+2**, přesně text100. Singleton má A=1,B=0
a cenu28+4M+2, stejně jako explicitní průchod. Z již uzavřených
permutací plyne pro jediný seznam E A=H_N,E B=binom(N,2)/2;
nejde o nově předpokládanou nezávislost A a B.

## P0905: varianta M=b a známé erratum

Při M=b je d=floor(K/b²), tedy první byte klíče. Opravené
`LD4 INPUT,1(1:1)` tak nahrazuje přesně08–11. Vytištěné LD3 by
bylo hned přepsáno na12 a I4 by zůstalo staré; právě tuto chybu
již opravuje all3-prepre,30.4.2008. Vlastní nový nález nevzniká.

Jedno MOVE pro vyčištění hlaviček lze realizovat po nulovém seedu:
`STZ HEAD+1; ENT1 HEAD+2; MOVE HEAD+1(b−1)`. MOVE kopíruje
postupně a zdroj s cílem se překrývají; nula se tak rozšíří přes
všech b hlaviček. Jeho pole b−1 je reprezentovatelné jedním bytem.
Není třeba nepovolené MOVE s počtem b.07 následně znovu nastaví I1.

## P0906: celá34, včetně obou krajních počtů

Nechť I_j je indikátor, že klíč j patří do pevného intervalu.
Za uvedeného nezávislého modelu jsou I_j Bernoulli(1/M).
Pro každou n-prvkovou podmnožinu přesně těchto klíčů je pravděpodobnost
(1/M)^n(1−1/M)^(N−n), události jsou disjunktní a je jich binom(N,n).
To dokazuje(14) i odpověď34. Nula a N jsou zahrnuty; M=1 dává
degenerovaný počet n=N (mocnina0⁰ v součtovém zápisu znamená1).
Prázdný vstup v matematickém modelu má n=0; tím se neprohlašuje
nehlídaný MIX program za implementaci N=0.

## P0907: celá35 a každá instrukce spojování

24 inicializuje I1=0, adresu umělé globální hlavy v INPUT.
25 nastaví I2=1−M; při zpracování intervalu t platí I2=t−M,
takže26 načte HEAD+t do I3.27 prázdný interval přeskočí na32,
aniž změní předchozí konec. Jinak28 připojí novou hlavu za konec I1.
29 nastaví konec na právě čtený uzel,30 čte jeho LINK a31 pokračuje
pouze pro kladný následník. Na konci je I1 poslední uzel tohoto
seznamu, s nulovým LINK.32/33 zvyšují t a skončí po t=M.

Invariant před26: globální hlava ukazuje na spojení dosavadních
neprázdných seznamů a I1 je jeho konec, případně0 před prvním.
Prázdný interval jej zachová. Neprázdný se připojí jedním přepsáním
nulového koncového LINK; sken se nesplete s již připojeným prefixem,
protože jde jen novým původním seznamem. Všechny seznamy jsou konečné
a disjunktní. Poslední konec už má0, takže další zápis netřeba.
Při N≥1 existuje alespoň jeden neprázdný seznam a INPUT(LINK) se
opravdu inicializuje prvním28. Pro N=0 by se musela zvlášť nulovat
globální hlava; takový rozšířený vstup zde není předpokládán.

Výsledek je vzestupný a stabilní a obsahuje každý index právě jednou.
Stabilní pořadí indexů je jednoznačné, proto každý LINK přesně
odpovídá ProgramL, jak úloha požaduje, nikoli jen stejným klíčům.

## P0908: všechny náklady35 a poznámka s END

Označme E počet prázdných seznamů a U=M−E.24/25 mají cenu2,
26/27 cenu3M,28 cenu2U,29–31 cenu4N,32/33 cenu2M. Tedy

    T_join=4N+7M−2E+2.

Četnosti26/27/32/33 jsou M,28 M−E,29/30/31 N. V sazbě625 je
známá typografická změna centrování M, nikoli změna této hodnoty.

Poznámka626 vloží `ST1 END,4` mezi19 a20, ale štítek5H zůstává
na20. Proto tento nový příkaz proběhne **jen při p=0**, nikoli
při skoku JLE na20. Přesně tehdy se změní konec seznamu a END[d]
dostane j. Proběhne A krát, přidá2A. Prázdné END není třeba číst.
Ve spojování lze pak29–31 nahradit jediným
`LD1 END+M-1,2`, které načte konec právě připojeného intervalu.
Cena je9M−4E+2, namísto4N+7M−2E+2. I s2A navíc ušetříme
4N−2U−2A≥0, protože U≤N a A≤N. Rovnost je možná například
při samých singletons. To plně zdůvodňuje poznámku o úspoře,
bez dovozu dosud nezkontrolovaného5.2.5H.

## P0909: celá36 a návaznost na převzatý C0025

Při b=100 mají klíče503000,…,703000 tři byty a M=4 rozděluje
přesně podle hranic250000,500000,750000. Původní pořadí v buňkách:

    087,061,170,154                  B=2,A=2
    275,426                         B=0,A=1
    503,512,653,509,612,677,703      B=3,A=1
    908,897,765                     B=3,A=3.

První dvě inverse jsou087>061 a170>154. Ve třetím seznamu jsou
512>509,653>509,653>612; poslední seznam je obrácená trojice.
Pravostranná maxima jsou po řádcích(170,154),(426),(703),
(908,897,765). Tedy B=8,A=7,N=16 a ProgramM má
56+496−21+16+2=549u. E=0 dává spojování64+28+2=94u,
celkem643u při stejné jediné výstupní hlavě jako L.

P0888/P0894 již obecně i konkrétně doložily původní L=496u
a zlepšené L=433u; nepřepočítávají se. Vytištěné358u je převzatý
C0025, jediný nález tohoto příkladu. Násobení stojí10N=160u,
takže poznámka o jeho významné režii má konkrétní podklad.

## Výslovné meze pokrytí

Isaac/Singleton1956, Tarter/Kronmal1966 a prvenství na99 se nyní
bibliograficky neověřují. To neuzavírá žádnou matematickou mezeru.
Pravděpodobnostní model a program jsou doloženy; součty(15)–(19),
čísla pro M≈N a celé37–40 zůstávají pro následující blok.
