# Úloha 7.1.1–52: všechny čtyři hry pro n=7

Checkpoint X0084, P0782–P0787. Zadání p86/file103, odpověď
p544/file561, znovu porovnány s původními rendery proof-file103.png
 a proof-file561.png. Zápis abcdefg, první hráč P, druhý Q.
P0776 se přebírá: druhý tah 2→4 je pro obě identity remízový.
Pro případnou výhru Q zbývá pouze levý začátek 2,1,3.
Žádný program ani enumerace stavů.

## Společný bezpečný prefix pro začínajícího hráče 0 — P0782

P nastaví b=c=1. Před každým dalším tahem Q z3 budeme držet

    S(a,d): Q na tahu z3, slovo a11d***,

kde d je zatím * nebo bit. Hodnotu a původně zvolil Q.
Pokud Q3→5 přiřadí e, přejdeme do koncovky popsané pro konkrétní
funkci níže. Pokud Q3→2 přepne b na0, P použije

    P2→1: přepne a;
    Q1→3: nuceně přepne c na0;
    P3→2: přepne b zpět na1.

Q z2 má přesně dvě možnosti:

* Q2→1 přepne a zpět a P1→3 přepne c zpět na1.
  Vrací se přesně stejný S(a,d), včetně hráče na tahu: remíza.
* Q2→4 přiřadí nebo přepne d; P4→3 přepne c zpět na1.
  Vrací se tvar S s přepnutým a a novým d, b=c=1 stále.

Dokud Q neodejde do5, zůstávají e,f,g nepřiřazené. Existuje jen
šest stavů S(a,d), takže pokračování bez odchodu musí zopakovat
úplný stav. I případné dřívější opakování znamená bezpečnou remízu.
Nejde o předpoklad, že b=c=1 zůstává po každém jednotlivém tahu;
invariant platí přesně ve vyznačených rozhodovacích stavech Q.

Koncovka tedy vždy začíná po Q3→5 ve slově a11dE**,
kde E je bit zvolený Q a P je na tahu z5. Hodnotu d je nutné
rozlišit: přiřazený bit dovoluje dřívější konec hry.

## Hra(b): druhý hráč vyhraje pro obě identity — P0783

Q vybere levou větev a potom3→5. P z5 může do4 nebo7.
Q jde v obou případech do6; P musí6→5 a přepne e.
Q z5 přiřadí dosud volnou z dvojice4,7. Tím přiřadí poslední *:

    2,1,3,5,4,6,5,7
    nebo 2,1,3,5,7,6,5,4.

Všechny mezi tím uvedené P-tahy jsou nucené kromě obou výslovně
pokrytých možností z5. P0765 dovoluje Q nastavit požadovanou
paritu posledním bitem. K opakování stavu před koncem nedojde:
při druhé návštěvě5 jsou oproti první přiřazeny dva další bity.

## Hra(a): přesně „1 loses if first“ — P0784

### Začíná P=1

Q=0 použije levou větev s a=1 a při3→5 nastaví e=1.
Pokud P5→4, Q4→6 nastaví f=0, P6→5 přepne e na0
 a Q5→7 nastaví g=0. Vnější dvojice a=1,g=0 dává f_a=0.
Pokud P5→7 nastaví g, Q7→6 nastaví f=0, P6→5 přepne e
na0 a Q5→4 přiřadí poslední d libovolně. Nyní a=1≥g;
při rovnosti b≥f=0; při další rovnosti c≥e=0. Slovo tedy
není menší než své obrácení. Q vynutí0 i v případě úplné rovnosti.

### Začíná P=0

P používá prefix P0782. Po odchodu Q do5 nastaví P5→7
hodnotu g=a. Q musí7→6 a nastaví f=F.

Je-li d již bit, hra právě skončila. Vnější dvojice je shodná,
b=1≥F, a při další rovnosti c=1≥E. Výsledek je0.

Je-li d=*, P musí6→5 a přepne e na1−E. Vznikne stav

    T: Q na tahu z5, slovo a11*(1−E)Fa.

Pokud Q5→4 přiřadí poslední d, stejný lexikografický argument
dá0. Pokud Q5→7 přepne g na1−a, následují nucené P7→6
(přepne f) a Q6→5 (přepne e zpět na E). P je nyní na tahu z5.

* Je-li a=1, pak g=0. P5→4 přiřadí poslední d a vyhraje0.
* Je-li a=0, P5→7 přepne g zpět na0; Q7→6 přepne f zpět
  na F; P6→5 přepne e zpět na1−E. Vrací se přesně T,
  se stejným hráčem na tahu, tedy remíza.

To jsou všechny možnosti Q. P zaručí neprohru vlevo; pravou
větví Q může zaručit remízu podle P0776. Výsledek při začátku0
je proto přesně draw, nikoli tvrzení, že P vyhraje každý průběh.

## Hra(c): přesně „1 loses if first“ — P0785

### Začíná P=1

Q=0 vybere levou větev, při3→5 nastaví e=0. Po kterékoli
P-volbě4/7 nastaví Q v6 hodnotu f=1. P musí6→5, takže e=1.
Q přiřadí zbývající d nebo g. Dvojice ef=11 zaručí0 nezávisle
na všech ostatních bitech. Opačná volba e=1 by tuto argumentaci
nedávala; záleží na povinném přepnutí e.

### Začíná P=0

Použije prefix P0782. Po Q3→5 jde P5→7 a přiřadí g libovolně;
Q7→6 přiřadí f. Je-li d již bit, hra končí s bc=11 a výsledkem0.

Je-li d=*, P6→5 přepne e. Pokud Q5→4 přiřadí d, opět
končí s bc=11. Pokud Q5→7 přepne g, P7→6 přepne f,
Q6→5 přepne e a P5→4 přiřadí poslední d. Dvojice bc=11
se po celou koncovku nemění. Všechny její terminály dávají0.
Prefix může remizovat; pravá větev také. P=0 tedy zaručí
neprohru a Q pravou větví přesnou remízu.

## Hra(d): přesně „1 loses if first“ — P0786

### Začíná P=1

Q=0 použije levou větev s a=1 a při3→5 nastaví e=1.
Pokud P5→4, Q4→6 přiřadí f libovolně, P6→5 přepne e
na0 a Q5→7 nastaví g=0. Výsledné číslo je sudé a alespoň64.

Pokud P5→7 přiřadí g, Q7→6 nastaví f=b. P6→5 přepne e
na0 a Q5→4 nastaví d=0. Pro g=0 jde opět o sudé číslo
alespoň64. Pro g=1 má hodnotu

    65+34b+16c ∈ {65,81,99,115}.

To jsou postupně 5·13, 9², 9·11, 5·23. Všechny P-volby
jsou pokryty a Q vynutí0 bez jakékoli pravděpodobnostní úvahy.

### Začíná P=0

Použije prefix P0782. Po Q3→5 s e=E jde P5→7 s g=0;
Q7→6 přiřadí f=F. Pokud d je již bit, hra končí sudým
číslem alespoň48 a P vyhrává.

Pro d=* P6→5 přepne e na1−E. Vznikne

    T: Q na tahu z5, slovo a11*(1−E)F0.

Q5→4 by skončilo sudým číslem alespoň48, tedy0. Zbývá
Q5→7 (g=1), P7→6 (f=1−F), Q6→5 (e=E). P je na tahu z5.
Při P5→4 má terminál hodnotu

    49+64a+4E+2(1−F)+8d.

Následující tabulka uvádí konkrétní složený terminál a volbu d;
jediná označená výjimka se místo dokončení vrátí do T.

| a | E | F | d | složená hodnota |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 51=3·17 |
| 0 | 0 | 1 | 0 | 49=7² |
| 0 | 1 | 0 | 0 | 55=5·11 |
| 0 | 1 | 1 | — | návrat do T |
| 1 | 0 | 0 | 0 | 115=5·23 |
| 1 | 0 | 1 | 1 | 121=11² |
| 1 | 1 | 0 | 0 | 119=7·17 |
| 1 | 1 | 1 | 0 | 117=9·13 |

Ve výjimce je slovo 011*101, P na tahu z5. Zvolí5→7,
tedy g=0; nucené Q7→6 vrátí f na1 a P6→5 vrátí e na0.
Tím se zopakuje přesně T=011*010, Q na tahu z5: remíza.
Tento cyklus ponechává d nepřiřazené, takže hra neskončí dříve.
P tedy vždy vyhraje nebo remizuje. Q pravou větví zaručí remízu;
celý vytištěný výsledek pro začátek0 je dokázán.

## Palindromy a srovnávací komentář — P0787

Dosud prokázané řádky dávají pro n=7 stejné výsledky(c) a(d)
pro oba začínající hráče; příslušný srovnávací komentář je uzavřen.

V(a) má libovolné palindromické slovo hodnotu0 podle definice.
Přesný význam dopadu této asymetrie lze dokázat bez nového řešení
her: změňme pouze přidělení palindromů, tedy použijme

    h(x)=[x≤reverse(x)]=1−f_a(complement(x)).

Bitový komplement každého přiřazeného bitu, ponechání * a ukazatele,
a současná záměna identit0/1 dává izomorfismus celých her. První
přiřazení se komplementuje a povinné přepnutí s komplementem
komutuje; opakování úplných stavů i okamžik konce se zachovají.
Pro h se tedy prokázaný výsledek obrátí: začínající1 remizuje,
začínající0 prohraje proti1. H a f_a se liší právě na palindromech.
To dokládá, že jejich jednostranné přiřazení ovlivní výsledek už
při n=7; nejde jen o statistický komentář.

Celé řádky n=2,…,7 jsou nyní prokázány, včetně obou počátečních
identit a příslušných dodatků. P0768 ponechává přesně osm buněk
n=8,9 a jejich srovnávací komentář. Žádná nová celostránková
argumentová propagace: na p86/544 jsou i další otevřené části.
Další n=8; hlavní text60/file77 a čtení218/file235 odděleně.
