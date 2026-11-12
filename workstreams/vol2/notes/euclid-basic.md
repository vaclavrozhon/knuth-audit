# §4.5.3: continuanty a první úlohy

Rozsah: základní identity textu 357–359 a úlohy 1–10, 32, 48,
nová 52. Původní zadání, odpovědi a příslušná errata byly
zobrazeny; inventář je v `euclid-inventory.md`. Historické atribuce
v odpovědi 32 zůstávají součástí budoucího kontextového bloku.
Numerická tabulka známých konstant a zbytek hlavního textu se
tímto zápisem ještě neuzavírají.

## Značení a obecné identity

Pro konečný seznam x=(x_1,...,x_n) označuje C(x) řetězový zlomek
1/(x_1+1/(x_2+...+1/x_n)); C(prázdný seznam)=0.
Continuant K(x) je polynom daný K(prázdný seznam)=1 a
K(x_1,...,x_n)=x_n K(x_1,...,x_(n-1))+K(x_1,...,x_(n-2)).
Pro sjednocení krajních maticových vzorců klademe K_(-1)=0.
V úloze 9 jsou identity racionálních funkcí: nulový vnitřní
jmenovatel lze překlenout pomocí dvojice čitatel/jmenovatel;
pokud je nulový jmenovatel výsledné funkce, konečnou hodnotu
netvrdíme. Tato interpretace je nutná už kvůli výslovným nulám
v zadání 9(b,c).

Položme M(x)=[[x,1],[1,0]]. Násobení zprava a indukce dávají

```text
M(x_1)...M(x_n) =
 [[K(x_1,...,x_n), K(x_1,...,x_(n-1))],
  [K(x_2,...,x_n), K(x_2,...,x_(n-1))]].                 (A)
```

Pro n=1 je pravý dolní prvek K_(-1)=0. To řeší úlohu 2.
Protože každá M má determinant -1, determinant součinu je
(-1)^n. Tím dostáváme identitu (8), po posunu indexu a využití
rekurze; jde o úlohu 4. Součin M současně dává poměr čitatele
a jmenovatele v (5). Z determinantové identity plyne

```text
C(x_1,...,x_n)-C(x_1,...,x_(n-1))=(-1)^(n-1)/(q_(n-1) q_n),
q_n=K(x_1,...,x_n), q_0=1.                              (B)
```

Teleskopický součet (B) je přesně (9). Pro celočíselné podíly
jsou čitatel a jmenovatel nesoudělné, protože každý jejich společný
dělitel by podle determinantu dělil 1.

Determinant tridiagonální matice v úloze 3 má po rozvoji posledním
řádkem rekurzi D_n=x_n D_(n-1)+D_(n-2), D_0=1,D_1=x_1.
Znaménko plus vzniká ze součinu horního prvku 1 a dolního -1
s opačným znaménkem kofaktoru. Výsledek je K_n.

## Úlohy 7 a 32: pokrytí řady a symetrie

Rozdělme n pozic na jednotlivé body a sousední dvojice. Jednotlivé
pozici i přiřadíme váhu x_i, dvojici váhu 1; váhu rozdělení tvoří
součin. Součet vah splňuje tutéž rekurzi jako K_n. To je přesná
interpretace teček a čárek v 32(a) i Eulerova pravidla mazání párů
v textu. Počet rozdělení je F_(n+1), kde F_0=0,F_1=1 a
F_(j+2)=F_(j+1)+F_j jsou Fibonacciho čísla. Obrácení řady
zachovává váhy, takže dostáváme symetrii (6).

Pro n>=3 členy stupně n-2 vznikají právě odstraněním jediné
sousední dvojice. Permutace proměnných zachovávající polynom
proto musí zachovat sousedství cesty 1,2,...,n. Obraz krajního
vrcholu určuje postupně celou cestu: možné jsou jen identita
a obrácení. Pro n=1 a n=2 tvrzení ověříme přímo. Tím je úloha 7
dokázána bez rozlišování případných shod počtů jednotlivých členů.

Členů obsahujících x_k je F_k F_(n+1-k): po určení bodu k se
levá i pravá část pokrývají nezávisle. To potvrzuje známou opravu
z roku 2000; původní F_k F_(n-k) je chybné.

Rozdělením pokrytí podle toho, zda dvojice protíná hranici m/m+1,
dostaneme identitu 32(b). Také rozšířený vzorec odpovědi je správný.
Pro jeho důkaz napišme součin (A) jako ABC, kde A obsahuje prvních
m matic, B dalších k a C zbývajících n-k, s 0<=k<n. Označme
A_11=a,A_12=b, B=[[p,q],[r,s]], C_11=u,C_21=w. Rozdíl levé
strany rozšířeného vzorce a prvního členu pravé strany je

```text
[(ap+br)u+(aq+bs)w]p - (ap+br)(pu+qw)
    = b(ps-qr)w = (-1)^k b w.
```

Převod b a w zpět na continuanty dává přesně tištěný poslední člen.

## Úlohy 5 a 6: konvergence a jednoznačnost

Jsou-li všechna x_j kladná, q_(j+1)>q_(j-1). Členy střídavé
řady (B) tedy klesají v absolutní hodnotě. Řada konverguje právě
když q_n q_(n+1) roste do nekonečna: nutnost plyne z rozdílů
sousedních částečných součtů, postačitelnost ze střídavé řady.

Při x_j>epsilon>0 položme r=1+epsilon/2. Platí
epsilon*r+1-r²=epsilon²/4>0. Z rekurze a vhodné c>0 pro první
dva členy vyjde indukcí q_n>=c r^n. Konečná limita proto existuje.
Pouhá kladnost nestačí: při x_n=2^-n indukce dává
q_n<=2-2^-n. Podle (B) jsou pak rozdíly sousedních konvergentů
větší než 1/4, takže limita neexistuje. Jde o přesný protipříklad,
nikoli jen nezkonvergovanou numerickou iteraci.

Při kladných celočíselných podílech B_j je každý nekonečný ocas
v (0,1): jeho první člen dává kladnou dolní mez a další kladný
ocas zajišťuje ostrou horní mez i při prvním podílu 1. Pokud X
je hodnota celého zlomku a Y hodnota následujícího ocasu, máme
1/X=B_1+Y s 0<Y<1, tedy floor(1/X)=B_1. Opakováním získáme
všechny podíly. X nemůže být racionální, protože jeho Eukleidův
postup by skončil, zatímco všechny tyto ocasy jsou kladné.
Pro konečný seznam s posledním B_m>1 stejný argument končí
nulovým ocasem a dokazuje jedinečnost kanonického zápisu.

Pomocná nerovnost v odpovědi 6 je však formulována příliš obecně:
C(1)=1 nesplňuje uvedené C(x_1,...,x_n)<1 pro všechny kladné
celé podíly. Podmínka posledního podílu >1 nebo vyloučení
jednočlenného seznamu (1) ji opravuje. Hlavní zadání 6 zůstává
správné. Drobný nález je oddělen v `C0130-continued-fraction-endpoint.md`.

Pro vlastní pravidelný rozvoj čísla X má jeho ocas X_n vztah
X=C(A_1,...,A_n+X_n). Matice (A) dává přímo přesnou chybu
1/(q_n K(A_1,...,A_n,1/X_n)) pro X_n>0 a odhad (12), neboť
1/X_n>=A_(n+1). Z q_n>=F_(n+1) plyne konvergence k X.
Racionální rozvoje jsou přesně kroky Eukleidova algoritmu,
jak ukazují (14)–(17); ukončení a podmínka posledního podílu >=2
vyplývají z kladných klesajících celočíselných zbytků.

## Úlohy 8–10: převrácení a nulové podíly

Z X_j=1/X_(j-1)-A_j plyne
-1/X_j=1/(A_j-1/X_(j-1)). Opakování této rovnosti dává
obrácený seznam v úloze 8. Pro konečnou číselnou hodnotu je
třeba X_j!=0; při nulovém ocasu jde o pól téže racionální identity.
Pro n=0 dostáváme C(-X)=-1/X.

9(a) je vložení ocasu do posledního jmenovatele; 9(b) dvojí
převrácení; 9(c) plyne z přesné matice
M(x)M(0)M(y)=M(x+y). Pro 9(d) stačí
1-1/(x+t)=1/(1+1/(x-1+t)). Tyto identity jsou platné jako
racionální funkce i tehdy, když je některý vnitřní podíl nula.

Úloha 10 používá A_0=floor(X), A_1,... kladné celé podíly.
Následující tabulka uvádí celou konečnou část před nezměněným
ocasem A_5,A_6,...; první položka každého řádku je celá část.

| Podmínka | Konečný seznam pro 1/X před A_5,... |
|---|---|
| A_0>0 | 0,A_0,A_1,A_2,A_3,A_4 |
| A_0=0 | A_1,A_2,A_3,A_4 |
| A_0=-1,A_1=1 | -(A_2+2),1,A_3-1,A_4 |
| A_0=-1,A_1>1 | -2,1,A_1-2,A_2,A_3,A_4 |
| A_0<-1 | -1,1,-A_0-2,1,A_1-1,A_2,A_3,A_4 |

První dva řádky jsou přímé převrácení. Záporné případy dostaneme
dvěma použitími 9(d) a oddělením celé části; ekvivalentně stačí
v (A) prohodit řádky výsledné matice. Tím vznikne přesná
racionální identita v dosud neznámém ocasu, ne jen shoda pro
vybrané hodnoty. Každou nulu uvnitř seznamu odstraníme pravidlem
9(c); když A_0=-2,A_1=1, proběhnou dvě taková odstranění.
Zbývající podíly jsou kladné. Nenulový nekonečný ocas v (0,1)
pak podle úlohy 6 zaručuje, že jde o pravidelný rozvoj.
Počet podílů po celé části je vždy lichý i po odečtení dvojic;
tento fakt bude použit v úloze 11.

## Úloha 48: koeficienty rozšířeného algoritmu

Nechť u,v>0, d=gcd(u,v), a_1,...,a_n jsou podíly Eukleidova
postupu a T_j=(x_j,y_j,z_j), kde x_j u+y_j v=z_j.
Z počátečních T_0=(1,0,u), T_1=(0,1,v) a rekurze
T_(j+1)=T_(j-1)-a_j T_j dostáváme

```text
x_j=(-1)^j K(a_2,...,a_(j-1)),
y_j=(-1)^(j-1) K(a_1,...,a_(j-1)),
z_j=d K(a_(j+1),...,a_n).                              (C)
```

První složka při j=1 znamená K_(-1)=0. Pro j=n+1 je poslední
složka rovněž 0. Všechny tři vzorce mají správné počátky a tutéž
rekurzi: pro z_j ji ověříme odzadu od posledního kladného zbytku d.
Parita stupňů členů K_n je n, proto
K_n(-a_1,...,-a_n)=(-1)^n K_n(a_1,...,a_n), což ověřuje také
první variantu vyjádření v odpovědi.

## Úloha 52: Ostrowského zápis

Jsou dána kladná celá a_1,a_2,... a q_0=1,q_1=a_1,
q_(j+1)=a_(j+1)q_j+q_(j-1). Hledáme cifry c_j s
0<=c_j<=a_(j+1), přičemž maximální cifra je dovolená jen
pro j>0 a vynucuje c_(j-1)=0. Zvlášť 0<=c_0<a_1.

Dokážeme silnější tvrzení: povolené cifry c_0,...,c_m reprezentují
právě jednou všechna celá čísla v [0,q_(m+1)). Pro m=0 je to
zřejmé. Při c_m<a_(m+1) dává indukce sousední bloky
[c_m q_m,(c_m+1)q_m). Při c_m=a_(m+1) musí být c_(m-1)=0;
zbylé cifry dávají poslední blok
[a_(m+1)q_m,a_(m+1)q_m+q_(m-1)). Pro m=1 se tento poslední
blok skládá jen z jedné hodnoty, v souladu s q_0=1.
Bloky se nepřekrývají a jejich sjednocení je požadovaný interval.
Protože q_m roste do nekonečna, každé nezáporné celé číslo má
konečný jednoznačný zápis, s obvyklým ignorováním vedoucích nul.

Důkaz také dává algoritmus: postupně od největší váhy bereme
c_m=floor(n/q_m) a pokračujeme se zbytkem. Při maximální cifře
je zbytek menší než q_(m-1), takže předchozí cifra je automaticky 0.
Případ a_1=1 má q_0=q_1=1, ale c_0=0; nezpůsobuje nejednoznačnost.

## Úloha 1: program MIX a jeho čas

Přepis je v `sources/euclid-unit.mix`. Na začátku smyčky jsou
dividend a v rA, dělitel b>0 v rX. Po STX/SUB/CMPA je testován
rozdíl a-b proti b. SRAX přesune jeho velikost do rX a zachová
výsledek porovnání. Je-li a>=b a a-b<b, jde o podíl 1 a přímý
zbytek a-b. Jinak DIV vypočte (a-b) mod b = a mod b.

Vstupní pořadí může dát a<b pouze při prvním průchodu. Pak
program přeskočí DIV a použije |a-b|; také to zachovává gcd
a nový pár má správné pořadí. Pro a=0,b>0 vznikne (b,b) a další
průchod skončí. Při b=0 smyčka vůbec nezačne. Tím jsou pokryty
i nulové vstupy a obě pořadí; od druhého průchodu kladné zbytky
striktně klesají. Odčítání slov nepřetéká a DIV se provádí pouze
s nezáporným čitatelem, jehož horní slovo je 0.

Označme T' počet průchodů smyčkou a Q počet přeskočených DIV.
Přesné časování MIX je **24T'-12Q+6**. Pro seřazený první pár
je T' počet běžných Eukleidových dělení a Q počet podílů 1.
V obecném počátečním pořadí nelze tyto počty bez upozornění
ztotožnit. Například počáteční podíl 0 je nahrazen odečtením.

Dosazení limitní četnosti podílu 1, p=log2(4/3), do vedoucího
koeficientu dává 24-12p=19.01955..., tedy uvedených přibližných
19.02. Je to o trochu více než 19 u původního programu A.
Platnost Gaussova limitního modelu se kontroluje zvlášť v textu
362–368; tento počet není tvrzení o stejné četnosti v každém
konečném vstupu ani o rigorózním průměrném konstantním členu +6.

## Nezávislé kontroly

`verify_euclid_basic.py` porovnává rekurentní polynom s přímým
součinem matic, přesnou eliminací tridiagonálního determinantu
a enumerací všech nepřekrývajících se dvojic. Permutační symetrie
jsou kontrolovány na celých množinách monomů. Další bloky používají
přesné zlomky, koeficientové identity Möbiových transformací,
přímé rozšířené dělení, úplné malé číselné intervaly a nezávislý
interpret přepsaného MIX programu. Výsledné počty a stav každého
checkpointu jsou v `results/euclid-basic.json`.
