# §1.3.1-22: dvě MUL, posun či DIV a NUM v šesti slovech

Tato konstrukční cesta ke kratšímu programu je vyloučena obecným
argumentem, bez testování vybraných konstant. **Nejde o globální
šestislovnou dolní mez.** Tvrzení se týká přesně posloupnosti

```
LDA/LDAN  vstup
MUL       první operand
T
MUL       druhý operand
NUM
HLT
```

kde T je jeden z šesti posunů nebo jedno DIV. Obě MUL i případné
DIV jsou **celočíselné** operace; plovoucí FMUL/FDIV jsou jinou
rodinou a tato věta je nezahrnuje. Operandy celočíselné aritmetiky
mohou používat libovolná platná pole a číst libovolná slova
vlastního kódu. Tím jsou zahrnuty konstanty skryté v instrukcích,
nikoli jen oddělená datová slova. Je započteno všech šest míst
uvedených instrukcí, takže další připravená konstanta již není
šestislovným řešením. Čtení původního vstupu je také dovoleno.
Není však dovolena změna tohoto vymezeného sledu na jiný program.

## Redukce na radix100 a číslicový převod

Přenositelné řešení musí fungovat i pro radix b=100. Položme
B=100^5=10^10. Na tomto radixu NUM z desetibajtové velikosti P
vytvoří číslo phi(P): každému bajtu z jeho zápisu v základu100
vezme zbytek modulo10 a těchto deset číslic přečte v základu10.
Tedy je-li

```
P = d9*100^9 + ... + d1*100 + d0,   0<=dj<100,
phi(P) = (d9 mod10)*10^9 + ... + (d1 mod10)*10 + (d0 mod10).
```

Vždy je phi(P)<10^10=B, takže na radixu100 NUM nepřeteče.
Pro všechny kladné vstupy n musí úspěšný program dát
phi(Pn)=n^13; nutné znaménko plus můžeme pro dolní mez ignorovat.
Počáteční indexy zvolíme nulové. Žádná instrukce uvedeného sledu
je nemění, takže adresy operandů i vzdálenost posunu jsou pro
všechny vstupy stejné. Pokud některá adresa není platná, program
už nesplňuje zadání.

Paměťový operand může pocházet z kódu nebo ze vstupu. Kdyby
pocházel z další nepředepsané buňky, lze ji zvolit nulovou:
první či poslední násobení by vynulovalo výsledek, případné DIV
by bylo nedefinované. Připravení nenulového obsahu této další
buňky by místo toho zvětšilo prostor nad šest slov.

## Poslední násobitel musí být celé slovo s opcode3

Označme K2 velikost druhého násobitele a An velikost A těsně
před posledním MUL. Vždy An<B. Pro vstup5 je nutno dosáhnout

```
5^13=1220703125 > 10^9.
```

Kdyby K2<100^4, bylo by P5=A5*K2<100^9. Nejvyšší bajt P5
by byl nulový a phi(P5)<10^9, což nestačí. Druhý operand tedy
nemůže být pole s méně než pěti datovými bajty. Nemůže být ani
původní vstup, jehož velikost je nejvýše5. Musí jít o všech
pět bajtů některého ze šesti instrukčních slov. Pole může,
ale nemusí zahrnovat znaménko; velikost je tatáž.

Poslední bajty těchto šesti slov jsou jejich opcodes:

```
8 nebo16; 3; (6 pro posun nebo4 pro DIV); 3; 5; 5.
```

Protože phi(P1)=1, je P1=A1*K2 rovno1 modulo10. K2 tedy musí
být nesoudělné s10. Z uvedených opcodes je to pouze3. Nutně
se čte celé slovo některého MUL a

```
K2 mod10=3,       A1 mod10=7.
```

Tento krok neomezuje ostatní bajty instrukce MUL. Adresy,
indexy, pole i znaménka obou násobení mohou být libovolné,
pokud program jako celek zůstane platný.

## První násobitel je pevná konstanta z kódu

Kdyby první MUL četlo vstup, byla by jeho velikost buď n,
nebo0 podle zvoleného pole. Nulový případ ihned selže. Pro n=1
by pak společná velikost AX byla1. Jediný posun z ní v A vytvoří
buď0, nebo jedinou nenulovou číslici1 v některé pozici. Poslední
desetinná číslice A je tedy0 nebo1, nikoli požadovaných7.
Jedno DIV s pevným kladným dělitelem dá pro n=1 také jen0
nebo1. DIV vstupem není přípustné pro nulový vstup.

První MUL tedy čte pevný operand z kódu. Jeho velikost označme
K, kde0<=K<B. Případ K=0 selže. Po prvním násobení má AX
přesnou velikost n*K. Pro n=1 je horních pět bajtů A nulových.

## Mezilehlý příkaz dává podíl s malým zbytkem

Je-li T=DIV, musí jeho operand být pevný kladný dělitel d.
Nulový dělitel je neplatný a čtení vstupu selže na n=0.
Pro úspěšný program nepřeteče DIV; proto

```
An = floor(n*K/d).
```

Je-li T posun, samostatné SLA/SRA ponechají pro n=1 A nulové,
takže selžou. U sdruženého posunu musí poslední bajt A1 přijít
z některého z pěti dolních bajtů původního AX, jinak je opět
nulový. Pětiprvkové okno končící v této dolní polovině nepřechází
přes kruhový konec desetibajtového slova. Případné doplnění
pravého konce nulou také nevyhoví požadovanému A1 mod10=7.
Pro některé r=0,...,4 je tedy pro všechny vstupy

```
An = floor(n*K/100^r) modB.
```

Platí to i pro kruhový posun s libovolným počtem otočení;
rozhoduje jen zbytek jeho vzdálenosti modulo10. SRAX nedodá
nenulový poslední bajt A1 a je tím rovněž vyloučeno.

V obou případech existuje pevné celé d>=1 a rozklad

```
K=q*d+t,   0<=t<d,
A1=q,
A2 = 2*q+e moduloB,   e=floor(2*t/d) patří do{0,1}.
```

U DIV se zbytek moduloB vůbec neuplatní, protože jinak by
instrukce přetekla. U posunu vyjadřuje přesně výběr pěti bajtů.

## Spor mezi posledními dvěma desetinnými číslicemi

Protože P1=q*K2 je rovno1 modulo10, musí být

```
phi(P2) mod10 = (2*q+e)*K2 mod10 = 2+3*e mod10.
```

Požadovaná poslední číslice 2^13 je2, takže e=0. Dostáváme
P2 shodné s2*P1 moduloB. Zvláště se shodují jejich poslední
dva bajty v základu100.

Z phi(P1)=1 plyne, že poslední dva bajty P1 mají tvar

```
d0=10*a+1,   d1=10*c,   0<=a,c<=9.
```

Při zdvojení je poslední desetinná číslice dolního bajtu2.
Přenos do následujícího bajtu je
`floor(2*d0/100)`, tedy0 nebo1. Poslední desetinná číslice
následujícího bajtu je právě tento přenos, protože2*d1 je
dělitelné10. Proto nutně

```
phi(P2) mod100 je2 nebo12.
```

Jenže2^13=8192 končí číslicemi92. To je spor.

## Význam pro otevřené minimum

Vyloučena je celá uvedená šestislovná rodina, včetně všech
konstant získaných čtením vlastních instrukcí a včetně částečných
aritmetických operandů. Není potřeba konečný rozsah konstant,
numerický výčet programů ani limit počtu kroků. Závěr se ale
nevztahuje na jiné pořadí instrukcí, jiné aritmetické příkazy,
cykly ani samomodifikaci; globální prostorové minimum22 je
nadále partial.

Přímo přečtený originál138 dává převod modulo10 v NUM. MUL
a DIV jsou podle131, včetně známé opravy28.9.1997, která
v podílu/zbytku výslovně opravuje A na celé AX. Posuny jsou
podle již přímo přečtené135. Čtyři vrstvy errat byly prověřeny
v dosavadním stabilním zdrojovém rozsahu. K tomuto čistě
algebraickému důkazu nebyl spouštěn žádný nový test.
