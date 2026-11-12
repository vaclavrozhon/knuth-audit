# §1.3.1: programy v úlohách 16–25

Značení: b je radix MIX bajtu (64 až 100), B=b^5 kapacita velikosti
slova plus jedna, u jednotka času. Znaménko je samostatný bit;
podrobnosti jsou v [mix-semantics.md](mix-semantics.md). Níže jsou
invarianty platné pro všechny povolené vstupy, nikoli jen výsledky
testovacích běhů. Časy nezahrnují koncové HLT.

## Nulování, úlohy 16–17

Úloha16(a): STZ 0 vytvoří první nulové slovo, ENT1 1 nastaví cíl.
MOVE 0(49) vytváří kopie do adres 1,...,49 postupně: před každým
zápisem je už zdrojová adresa nulová. Poté je rI1=50. MOVE 0(50)
přenese nuly do 50,...,99 a nastaví rI1=100. Celkem 4 slova kódu,
čas 2+1+(1+98)+(1+100)=203u. F<=63 na všech strojích.

Úloha16(b): 100 instrukcí STZ dává čas 200u. Bez připraveného
vnějšího vstupu musí být každá ze sta libovolně obsazených paměťových
buněk zapsána. STORE stojí 2u na buňku, MOVE stojí 2u na buňku
a další 1u; jiné celočíselné instrukce do paměti nepíší. Tedy 200u
je dolní mez v tomto přirozeném modelu bez předem připraveného I/O.
Nejde o dolní mez při volně dostupné pásce s hotovým výsledkem.

Úloha17(a): před průchodem smyčkou STZ 0,2; DEC2 1; J2NN 3000
je rI2=k, kde k klesá od N k 0. Zápis vynuluje k a zmenšení dává
k−1. Po kroku k=0 se neskáče. Zapsány přesně 0,...,N; čas
4(N+1)u, tři instrukce. Kapacitní problém nenastane ani pro N=0.

Úloha17(b), krátká rychlá varianta: nulu v adrese0 rozmnožuje MOVE
v dávkách po 63, zatímco rI1 ukazuje první ještě nezapsanou buňku.
Pro N>=1 položme q=floor((N−1)/63), r=N−63q; tedy 1<=r<=63.
Pro N=0 položme q=r=0. Proběhne q úplných dávek, pak poslední
dávka r. DEC2 63 a J2P zajišťují, že přesně při r<=63 smyčka
skončí; INC2 63 vrátí r a ST2 do pole (4:4) nastaví počet poslední
MOVE. Nikde se nevyužívá přenos mimo bajt, protože r<=63.
Výsledný čas je (2N+3q+10)u. Modifikace vlastního F je zamýšlená.

Dlouhá varianta má 993 instrukcí STZ j,2 pro j=1,...,993.
Před celým blokem je rI2=N−993k>=0 a blok zapisuje interval
[rI2+1,rI2+993]. Po q=floor(N/993) celých blocích je zbytek
r=N−993q. Další DEC2 udělá r−993<0; ENN1 a indexovaný JMP
skočí na STZ s j=993−r. Provedený koncový úsek zapisuje přesně
0,...,r. J2N pak přeskočí do 3999. Celkem čas (2N+3q+8)u.
Pro všechna N je tedy rychlejší než devítiinstrukční varianta.

**Dolní meze:** správnost a uvedené časy jsou dokázány. X0685
uzavírá tři slova u17(a) pro přenositelný program se započtením
všech použitých kódových a pomocných buněk; kvalifikace jsou v
`mix-optimality-root-review.md`. Dosud není uzavřeno minimum16(a), ani
globální minimum času17(b) při všech možných samomodifikacích.
Není korektní odvozovat tato minima z toho, že nenalezneme lepší
krátký program. Úlohy16–17 proto zůstávají `partial` pro optimalitu.

## Úlohy 18–21

U „number one“ po prvních třech instrukcích platí X=−1 a
mem[1]=(−,1,0,0,0,0). SLAX 1 přesune −1 na velikost b v X,
INCX 1 vytvoří −(b−1). ENNA 1 nastaví A=−1. SRC 1 pak vytvoří
A=−(b−1)b^4, X=−b^4. ADD 1 přičte −b^4, tedy −B:
výsledkem je **−0 a zapnuté přetečení**. DEC1 −1 zvýší rI1 z1 na2;
STZ 1 dá +0, CMPA porovná −0 s +0 a nastaví EQUAL. MOVE −1,1(1)
zkopíruje mem[1] do mem[2] a zvýší rI1 na3. NUM přečte číslice
0000010000, tedy 10000, se záporným znaménkem A. CHAR vytvoří
A=(−,30,30,30,30,30), X=(−,31,30,30,30,30). Přetečení zůstane on.
Ostatní registry I2–I6 a J se nezmění. HLT zastaví počítač; čítač
instrukcí ukazuje za HLT. Součet cen prvních15 instrukcí je 42u.
Výjimka umístění programu do0 v odpovědi je nutná: první STZ pak
vymaže dosud neprovedené ENNX. Umístění do1 nebo2 tuto vadu nemá.

Úloha20: první MOVE uloží HLT do0 a rI1=1. Před k-tým blokovým
MOVE je nulová adresa HLT a všechny již zaplněné buňky obsahují
totéž slovo. Každý průchod vyplní dalších43 buněk. 93*43=3999;
poslední průchod doplní všechny zbývající buňky včetně své instrukce
v3993 a skoku v3994. Instrukce3993 už byla načtena, takže doběhne;
následující fetch3994 je nyní HLT. Všech4000 buněk tedy skutečně
obsahuje HLT; rI1=4000 se stále vejde do dvou bajtů.

Úloha21(a): běžný skok z P ukládá J=P+1, takže program nemůže
vytvořit J=0, neboť P>=0. GO je explicitní vnější výjimka. Ani
skok z3999 nepomůže: 4000 se do dvoubajtového J vejde.
(b) V buňce N−1 se dočasně nahradí původní slovo (uchované v A)
instrukcí JMP3005. JMP z3003 přejde do N−1, tamější skok nastaví
J=N, a STA v3005 obnoví původní paměť. N−1<2999, takže nekoliduje
s vlastními šesti instrukcemi. Všechny paměťové buňky jsou obnoveny.

## Třináctá mocnina, úloha22

Nechť x=|X|. Předpoklad x^13<B zaručuje x^2<b, x^4<b^2,
x^5<b^2 a x^8<b^4. Pattův program zachovává znaménko X v A.
Po načtení a prvním násobení je A=0, X=x^2. Uložení do pole(1:1)
v3500 a SRC1 vytvoří A=x^2 b^4. Další MUL dává A=x^4 b^3,
X=0; toto A se uloží v3501. ADD původního X vytvoří velikost
x^4 b^3+x, která je <B. Násobení x^4 b^3 potom dává
A=x^8 b a X=x^5 b^3. Po uložení X a dalším násobení je společná
velikost AX=x^13 b^4. SLAX1 tedy přenese do A přesně x^13 a
vyprázdní X. Uvedené nerovnosti vylučují nechtěné smíchání polí.
Čas je54u a využito14 slov včetně dvou nulových konstant.

Sedmiinstrukční smyčka začíná A=X, počitadlo12. Po j průchodech
MUL a SLAX5 je A=X^(j+1); všechna mezilehlá čísla se vejdou,
protože |X| je celé. Po12 průchodech je A=X^13. Čas171u.
Minimalita **sedmi slov** mezi všemi MIX programy zatím dokázána není.

Jelikož 6^13=13060694016>100^5, je |X|<=5. Tabulka proto stačí
pro11 vstupů. Navíc 65^5<5^13<66^5, takže krajní položky ±5^13
se nesmějí vkládat do slova při b<=65; toto řeší errata17.11.2007.
LD1 vstupu a LDA tabulky dají výsledek za4u, plus závěrečné HLT.
Úplná dolní mez je nyní X0684 v `mix-optimality-root-review.md`.
Opravuje neúplnost dřívějšího argumentu, který bez zdůvodnění
předpokládal běžné čtení dat: vstup by mohl být také vykonán
jako instrukce. Nový důkaz tuto možnost i předchozí samomodifikaci
výslovně vylučuje. Jde o číselné zadání; +0 a−0 jsou totéž celé
číslo. Zachování zvláštního znaménkového bitu nuly se zde nepožaduje.

Poznámka o pěti násobeních odkazuje na **addition chains** v §4.6.3:
to je model, v němž se předchozí mocniny násobí jako celá čísla,
nikoli jako zde zabalené polynomy v b. Délka řetězce pro13 je5:
1,2,3,6,12,13 funguje. Čtyři kroky nestačí: poslední13 vyžaduje
mezi předchozími hodnotami alespoň7, maximem po3 krocích je8;
dvojice8+5 ani7+6 se do tří předchozích kroků nedostanou.
Hodnota7 po3 krocích sama nevznikne (po1,2 je další3 nebo4;
z1,2,3 je maximum6, z1,2,4 lze vytvořit5,6,8, nikoli7).

## Obrácení bajtů a přeskupení, úlohy23–24

Dixonova smyčka má rI1 postupně4,3,2,1,0. LDA vždy obnoví celý
vstup; SRA vybere na pravý kraj postupně a,b,c,d,e. SRAX1 vloží
tento pravý bajt na levý kraj X a původní X posune doprava.
Po pěti průchodech jsou všechny původní číslice X vytlačeny a X
obsahuje e,d,c,b,a. SLAX5 přesune tyto číslice do A; znaménko A
je + díky LDA. Osm slov, čas43u bez HLT.

Wahidův dodatek2018 uvádí A>=0, ale tato podmínka není dostatečná:
**C0083** dokládá chybu pro A=−0 a vstupní slovo+0. Všech pět
posunů i nulových součtů ponechá znaménko minus, ačkoli zadání
požaduje plus. Dřívější přijetí této podmínky v auditu bylo příliš
široké; původní testy začínaly kladným A a tento okraj nepokrývaly.

Po zpřesnění na **A má znaménko plus** je invariant správný:
rI1=45,36,27,18,9 postupně modifikuje F na(5:5),...,(1:1).
Velikost A se mění na (bA mod B)+další_bajt. Po pěti krocích
původní číslice A zmizí a zbude obrácené slovo. ADD nepřeteče:
po SLA je velikost nejvýše B−b a přičítá se nejvýše b−1.
Znaménko zůstane plus i při nulovém součtu. Sedm slov a41u.
Přidání ENTA0 na začátek odstraní předpoklad za cenu dalšího slova.
Globální prostorová dolní mez v obou třídách zůstává otevřená.

Úloha24(a): desetibajtové AX=(0,a,b,c,d,e,f,g,h,i). Dělení kladným
b^4 dá kvocient (a,b,c,d,e) a zbytek (0,f,g,h,i). Horní A<b^4,
takže DIV nepřeteče. Potřebuje instrukci a konstantu, tedy2slova,
a12u. Úloha24(b) udělá stejnou permutaci pomocí SRC4,SRA1,SLC5
za6u a3slova; lze ji sledovat přímo na deseti symbolech.
Checker nezávisle vyčerpal všech66 možností jednoho posunu
(6typů a M=0,...,10) a všechny jejich dvojice: dvě posunové
instrukce nestačí. Pro kruhové posuny stačí zbytky mod10, pro
ostatní jsou M>=5/10 stejné, takže toto vyčerpání je úplné pro
**třídu posunů**. Neprohlašujeme ho za globální dolní mez všech
možných smíšených programů. Úloha24 zatím `partial` pro tuto mez.
Pozdější kořenová revize X0670 v `mix-crossrefs-and-space.md`
dokazuje globální prostorové minimum dvou slov pro část (a).
X0680 navíc uzavírá globální nejhorší čas6u pro část(b);
celá úloha24 je nyní checked, starší omezení na třídu posunů
již není aktuální mezí celého auditu.

## Rozšíření, úloha25

Jde o návrhovou, nikoli jedinou početní odpověď. Každé rozšíření
lze udělat konzervativně: existující platné instrukce zachovají
akci, nové možnosti obsadí dosud nedefinované I/F/adresy.
Jako nové I lze zavést J, dvojici indexů nebo nepřímou adresu.
Pětibajtové indexy dovolí větší paměť, aniž by změnily hodnoty
legacy programu: indukcí zůstávají jeho původně dvoubajtové
registry v původním rozsahu. Podobně lze přidat nepoužité záporné
adresy pro hodiny a přerušení, nové booleovské/bitové operace,
execute a porovnání s okamžitou adresou.

Kompatibilita předpokládá, že přerušení nejsou sama nově aktivována
ve starém programu a původní příkazy nemění význam. Rychlejší I/O
smí změnit počet průchodů čekací smyčkou: původní specifikace tento
počet už nechává neurčený. Nenahrazujeme „correctly written“ silnější
garancí stejného fyzického času nebo stejné stopy všech čekání.
Konkrétní odkazy na cvičení v dalších svazcích byly později přímo
zkontrolovány v X0669; úplný seznam a obrazy cílových stran jsou
v `mix-crossrefs-and-space.md`. Návrhový argument je nezávislý.
