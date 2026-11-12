# §1.3.2: jazyk, hlavní příklady a úlohy 1–9

> Oprava auditu 5. listopadu 2026: C0022 je zamítnuto. Originál na s.512
> správně obsahuje ≥64; starší čtení níže přehlédlo spodní čárku.
> Platný závěr a obrazový detail jsou v [souvislé recenzi](sequential-mixal-basics-2026-11-05.md).

Kontrola prvního dotisku třetího vydání, 1.11.2026. Originály s.144–163
 a odpovědi511–512 byly zobrazeny. Pro další úlohy je zatím potvrzeno
zadání, nikoli řešení. Značení: b je počet hodnot bajtu, 64<=b<=100;
B=b^5 je o jednu větší než největší velikost slova; u je časová jednotka.
Slovo má samostatné znaménko i při nulové velikosti. Specifikace instrukcí
je v [mix-semantics.md](mix-semantics.md).

## Pravidla jazyka

Symbol je řetězec1–10 písmen/číslic s alespoň jedním písmenem. Lokální
symbol dH označuje místo; dB/dF označuje nejbližší předchozí/následující
výskyt dH, **nikdy vlastní řádek**. Čítač umístění, zde pc, označuje adresu
příštího sestaveného slova. Hvězdička ve výrazu má hodnotu tohoto čítače.
Příklady1:3=11, -1+5*20/6=13 a ***=pc*pc odpovídají pravidlu, že všech
šest binárních operací má stejnou prioritu a vyhodnocuje se zleva.

Operace +,-,* pracují se znaménkem a velikostí MIX slova, s případným
odříznutím velikosti modulo B. Dělení / usekne velikost k nule; // nejprve
násobí čitatele B. Výsledek dělení musí být reprezentovatelný a dělitel
nenulový, stejně jako u odpovídajícího DIV. Dvojtečka je operace8A+B,
s mezikrokem definovaným instrukcemi knihy. Proto 1//3=floor(B/3), zatímco
1(4:4) jako W-hodnota představuje b.

W-hodnota je postupná konstrukce slova: začíná +0 a jednotlivé složky
přepisují své pole (L:R), 0<=L<=R<=5, poslední přepis má přednost.
Tak 1,-1000(0:2) má záporné znaménko, velikost1000 v prvních dvou bajtech
 a poslední bajt1. Opačné pořadí -1000(0:2),1 dává celé slovo+1.

LOC běžné instrukce, CON nebo ALF dostane dosavadní pc a pc se zvýší o1.
EQU určuje hodnotu symbolu, nevytváří běhové přiřazení. ORIG nastavuje pc,
ale jeho LOC dostává ještě starou hodnotu: TABLE ORIG *+100 rezervuje
100 míst a TABLE ukazuje na první z nich. ALF uchovává přesně5 znaků,
včetně úvodní mezery, takže ` HUND` má kódy0,8,24,15,4.

Instrukce sestaví pole znaménko/adresa,index,F,C postupnými částečnými
zápisy. Budoucí reference je povolena samotná v A-části; nesmí vstoupit
do aritmetiky ani W-hodnoty. Asembler proto může při jednom průchodu
ukládat seznam nevyřešených adres a později opravit právě tato pole.
Nedefinovaný symbol dostane na konci vlastní nulové slovo. Literály
jsou taktéž vložené konstanty; pořadí je libovolné, známá oprava2010
výslovně připouští con2 před con1. Symbol na END leží až za vloženými
slovy. Tato konstrukce dokazuje tvrzení o jednoduchém průchodu se
zpětnými opravami; nejde o tvrzení, že budoucí adresu známe předem.

Příklad lokálních symbolů na s.151: prostřední2H má hodnotu pc, první2H
hodnotu10, poslední2H hodnotu pc−3. Výsledná MOVE je proto MOVE pc−3(10).
Při nahrazení labelu4H v řádku15 Programu P za2H se změní i další
reference2F/2B: řádek14 míří do15 místo25 a řádek24 do15 místo12.
Odpověď7 je správná.

`mixal.py` je reprodukční sestavovač strukturovaných trojic, nikoli parser
štítků/terminálu. Podporuje operace, lokální symboly, dopředné adresy,
W-hodnoty a literály použité zde. Literály obsahující hvězdičku výslovně
odmítá; není vydáván za úplnou implementaci všech hraničních případů
jazyka. Pravidla číselných výrazů a význam příkladů mají výše vlastní
odvození, nezávislé na úspěchu implementace.

## Maximum a výběrové třídění

Předpoklady Programu M: n>=1, vstup X[1],...,X[n] i kód leží v platné,
vzájemně nekolidující paměti; I1=n a J je návratová adresa. Krok STJ
přepíše adresu závěrečného JMP, a proto tam nevznikne nekonečná smyčka
(úloha2). ENT3 nastaví k=n; první průchod načte X[n] a j=n.

Při vstupu do porovnání s X[k] je m maximum hodnot X[k+1],...,X[n]
 a j je **největší index** výskytu tohoto maxima. Když m>=X[k], obě
hodnoty zůstanou; jinak se nastaví m=X[k],j=k. DEC3 a J3P sníží k
 až na0. Invariant dokazuje správnost včetně shodných maxim a záporných
čísel. Knižní číselná slova na s.145 souhlasí s adresami a kódy.

Nechť A značí počet striktních nových maxim při průchodu zprava po prvním
prvku. Profil je přesně1,1,1,n−1,n−1,A+1,A+1,n,n,1. S cenami instrukcí
je součet 2+1+1+3(n−1)+3(A+1)+2n+1 = 5+5n+3A jednotek u.
Pro n=1 je čas10u. ENT1 100; JMP MAXIMUM; STA MAX používá návrat
na STA MAX přes J tak, jak text uvádí.

Úloha1: ENTX1000;STX X uloží+1000, protože ENTX je běhové přiřazení
registru a STX zapisuje paměť. Úloha3: po načtení100 slov z pásky0
čeká JBUS na jejich dokončení. Pro k=100,...,1 vymění maximum prefixu
X[1..k] s X[k]. Indukcí je suffix už uspořádán a všechny jeho hodnoty
jsou alespoň tak velké jako zbývající prefix. Výsledkem je neklesající
permutace vstupu, zapsaná na pásku1; duplicity ničemu nevadí.
Odkaz na Algorithm5.2.3S je uveden níže v soupisu pramenů.

## Prvočísla a zastavení zkoušení dělitelů

Prvočíslo je kladné celé číslo větší1 s právě dvěma kladnými děliteli.
Pro složené n>1 existuje prvočíselný dělitel <=sqrt(n): ze součinu dvou
netriviálních faktorů je alespoň jeden nejvýše sqrt(n), a lze vzít jeho
prvočíselného dělitele. Použita oprava15.5.1999, která v úloze6 mění
triviální dolní mez1<=d na1<d.

Před testem P7 jsou vyloučeni všichni prvočíselní dělitelé <=p=PRIME[K].
Podmínka Q=floor(N/p)<=p spolu s R=N mod p>0 dává

```
N = pQ+R < p²+p < (p+1)².
```

Každý zbývající prvočíselný dělitel je většíp, tedy alespoňp+1>sqrt(N).
Složenost je tak nemožná. Kniha používá ještě ostřejší >p+1, což zde
platí, neboť p>=3 je liché a p+1 je sudé. Podmínka Q<=p, nikoli Q<p,
je zásadní a v originále je správně; OCR rovnost ztrácí.

Dostupnost dostatečně velkého dělitele v dosud nalezené tabulce plyne
ze standardní Bertrandovy věty: mezi p a2p je pro p>1 prvočíslo. Pro
sousední prvočísla tudíž p_next<2p<p²+p. Když N=p_next, nejpozději test
p poskytne Q<=p; tabulka se nepřečte za poslední uložený prvek. To
ověřuje **použití** této klasické věty v odpovědi6, nikoli nové samostatné
dokazování Bertrandovy věty. Pro konkrétních500 prvočísel je dostupnost
 a celý výsledek navíc ověřen nezávislým přesným sítem do3999.

Invariant hlavní smyčky: I1=J−500, I2=N je další lichý kandidát; před P6
index I3=K ukazuje na právě zkoušené prvočíslo. ENTA0;ENTX0,2 vytváří
kladný dělenec AX=N. DIV vrátí Q,R, nulové R vyloučí kandidáta. CMPA
před zvýšením K uchová porovnání s původním p. JG je přesně Q>p.
Úspěšný kandidát se uloží do PRIME+500+I1=PRIME+J. Skutečný nejvyšší
kandidát3571 se vejde i do dvoubajtového indexu při b=64.

Výstupní invariant: na začátku vnějšího průchodu je I5=M−51;
INC5 501 nastaví M+450. Vnitřní smyčka načítá deset položek zprava
na indexech M+450,...,M, zmenšuje I5 o50 a I4 o1. CHAR vytvoří
10desetinných znaků; STX(1:4) ukládá poslední4 znaky do začátku slova,
za nimi zůstane mezera. Po deseti krocích I4 ukazuje na začátek bufferu,
I5=M−50. OUT tiskne správnou řádku a LD4(24+I4) přepne na druhý buffer
plus10. Při M=50 je I5=0 a program končí po50 řádcích.

Titul používá24 slov od1995, tedy zasahuje do BUF0. První datová řádka
se však staví v BUF1. Každý OUT čeká na **předchozí operaci téže tiskárny**;
při dalším přepnutí je starý buffer už volný. To dokazuje bezpečnost
bez JBUS pro každou konečnou prodlevu, nejen pro testované0 a50000u.
Přebytečné slovo na offset24 slouží jako ukazatel a leží za24 tisknutými
slovy. Čtení a zápis jeho hodnoty nekoliduje s výstupem.

Všech30 instrukcí a konstanty odpovědi4 byly porovnány se sestavením
původního programu pro všech37 radixů. Odpovídají původnímu PRIME=−1.
Oprava2022 na PRIME=99 vyžaduje další související změny; viz C0021.
V obou variantách je profil DIV9538 a čas řádků10–24 přesně182144u,
bez počátečního IOC a bez tisku. Nezávislé síto potvrzuje všech500 hodnot,
zejména poslední3571 a všech60 hodnot vypsaných na s.147.

## Úloha8, odvozena bez spuštění

Pro k=1,...,74 se uloží k prázdných slov a jedno slovoAAAAA. Po k blocích
je zaplněno S(k)=k(k+3)/2 slov. S(74)=2849, tedy méně než rezervovaných
3000 a méně než kapacita indexu i při b=64. Následný tisk používá první
2400 slov po24, tedy přesně100 řádek a12000 znaků. Výstupní paměť se už
nemění; OUT proto sám zajišťuje potřebné čekání.

S(67)=2345 a S(68)=2414. Poslední viditelné AAAAA leží ve slově2344,
na pozicích11720–11724 číslovaných od0. Řádka98 končí pozicí11759,
tedy poAAAAA zbývá35 mezer. Řádky99–100 jsou prázdné. Souhlasí úplně
s odpovědí. Testovací program tuto úlohu nespouští.

## Úloha9: tabulková kontrola instrukce

Testujeme syntaktickou platnost podle tabulky1.3.1-1 a výslovné výjimky
adresy v zadání, nikoli bezpečnost skutečného provedení s libovolnými
indexovými registry. I musí být0..6 a C musí být0..63. Tabulka má jednu
položku pro každý C; její bajt4 obsahuje největší F a bajty1–2 adresu
dalšího testu. Výrazy (5:5) v sestavení tabulky mají hodnotu45, nikoli
význam vytažení jednoho bajtu. Paměť tabulky se neprovádí jako instrukce.

Povolené F: NOP/MOVE libovolný bajt; NUM/CHAR/HLT0..2; posuny0..5;
I/O0..20; skupina JMP0..9; skoky registrů0..5; adresové operace0..3;
částečné čtení/zápis podle0<=L<=R<=5. ADD/SUB/MUL/DIV/CMPA navíc F=6
pro plovoucí variantu. Oprava2002 správně mění její skok na MEMORY,
aby i plovoucí instrukce prověřily adresu.

Trik pro pole: napišme F=9q+r, 0<=r<9. DIV9, STX a samomodifikované
INCA vytvoří q+r. Platí

```
F = 8L+R, 0<=L<=R<=5  <=>  q+r<=5,
```

protože vpřed q=L,r=R−L (tento rozdíl je<=5); zpět L=q,R=q+r.
Předchozí kontrola maxima45 je kompatibilní, a DECA5;JAP odmítá přesně
neplatné pole. Poslední MEMORY přijme libovolnou adresu pro I!=0;
pro I=0 odmítne záporné číslo a hodnotu>3999. Záporná nula je platná0.
Operace bez paměťové adresy přeskočí tento poslední test podle zadání.
Známé zkrácení2008 zachovává rozhodnutí a šetří konstanty/cykly.

Samotná rozhodovací logika je správná. Doprovodný komentář `C field >64?`
postrádá rovnost; viz drobná oprava C0022. Není to chyba programu.

## Výpočetní doklady

`check_mixal_basics.py` prošel52324 kontrolami, z toho49684 případů
validátoru instrukcí. Všechny bajtové velikosti64..100 byly použity pro
sestavení, příklady jazyka, maximum a časy M. Úplný Program P běžel
pro64/100, starý/opravený základ a dvě prodlevy tiskárny. Model hlídá
čtení nedokončeného vstupu a zápis do dosud používaného výstupu.
Přesný rozsah a omezení jsou v `results/mixal-basics.json`.

První spuštění zachytilo dvě naše chybně opsané hodnoty2383/2389 v tabulce;
skutečný sken je správný. Po opravě přepisu prošel kompletní běh jednou.
Nedošlo k úpravě původního celočíselného modelu ani opakování jeho4323
již úspěšných kontrol. Nové I/O je samostatné rozšíření. Konečné testy
nenahrazují výše uvedené invarianty a nejsou certifikací překladače.
