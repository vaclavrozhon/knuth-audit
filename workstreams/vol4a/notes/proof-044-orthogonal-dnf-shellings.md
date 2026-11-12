# Úloha 7.1.1–35: ortogonální DNF, stíny a přesné počty shellingů

Checkpoint X0073, P0690–P0700. Originál zadání p84/file101 a odpovědi
p541/file558; images/proof-file101.png, images/proof-file558.png
a detail images/proof-answer35e-detail.png. Všechny bitové kódy
jsou čteny z původní sazby. Poslední kód druhé rodiny v 35(e) je
**011010**, nikoli 011011. Žádná enumerace ani matematický program.

Souřadnice číslujeme zleva 1,…,n. Kód B zároveň označuje množinu
jedničkových souřadnic. Jeho kladná krychle C(B) má na B jedničky
a jinde hvězdičky. Doplněk kódu se bere v pevných n bitech.

## Ortogonalita a úvodní příklad — P0690

Plná DNF je ortogonální, protože její různé členy jsou různé body.
Pro nezávislé Bernoulliho souřadnice má krychle s pevnými jedničkami
B a nulami S pravděpodobnost

    ∏_{i∈B}p_i · ∏_{i∈S}(1−p_i).

U disjunktních krychlí se tyto výrazy přímo sčítají. Přesná
spojitost s polynomem úlohy 13 je již dokázána v proof-033,
P0586; nejde o nové přebírání či ověřování starého výpočtu.
To vysvětluje uvedenou užitečnost ortogonální DNF.

Pro f=x₁x₂∨x₂x₃∨x₃x₄ rozdělíme pravdivé body takto:
pokud x₁x₂=1, patří prvnímu členu; jinak při x₂x₃=1 je x₁=0;
pokud neplatí ani první dva, ale x₃x₄=1, je x₂=0.
Vznikají přesně krychle

    11**, 011*, *011.

Jsou disjunktní: první dvě se liší x₁, třetí od obou hodnotou x₂.
Mají 4+2+2=8 bodů, takže i vytištěný počet je přesný. Jejich
(A,B) kódy jsou (0011,1100), (0001,0110), (1000,0011),
přesně jak stojí v zadání.

## Význam β, monus a bezpečné odčítání — P0691

Stín S_k je sjednocení jednoprvkových množin B_j∖B_k pro j<k.
Označme x=B_j & complement(B_k). Vytištěná operace za XOR je
**monus**, x dot-minus y=max(0,x−y), nikoli obyčejné odečtení:

    β_jk=(x XOR (x−1)) dot-minus (x−1).

Pro x>0 pišme x=(2a+1)2^r, a≥0. Přepnutí bitů při odečtení 1
dává x XOR (x−1)=2^(r+1)−1. Obyčejný rozdíl by tedy byl
(1−2a)2^r; monus vrátí x při a=0 a nulu při a≥1.
Je to přesně požadovaný test, zda x má jediný jedničkový bit.

Pro x=0 vrací vzorec také nulu: v n-bitové aritmetice je x−1
samá jednička, XOR je stejný kód a jejich monus je nula.
Při celočíselném dvoudoplňkovém výkladu jsou oba argumenty −1,
opět s výsledkem nula. Vlastní množinová definice je nezávislá
na tomto implementačním okraji.

Každý bit S_k je mimo B_k. Proto A'_k=complement(B_k)−S_k
je obyčejné odečtení podmasky bez půjček, ekvivalentní
complement(B_k) & complement(S_k).
Nová krychle D_k tedy má přesně B_k=1 a S_k=0; zbývající bity
jsou volné. Nikdy nevznikne rozporný term ani prázdná krychle.

## 35(a): obecné zachování pokrytí — P0692

Každá D_k leží v C(B_k), takže jedno zahrnutí sjednocení je zřejmé.
Pro opačné vezměme bod x pokrytý původními krychlemi a zvolme
nejmenší k, pro který B_k⊆support(x).

Kdyby měl x jedničku v některém i∈S_k, existovalo by j<k
s B_j∖B_k={i}. Pak B_j⊆B_k∪{i}⊆support(x), spor s volbou k.
Všechny bity S_k jsou tedy v x nulové a x∈D_k.

Tento důkaz platí pro každý prefix seznamu, pro libovolné pořadí
i pro redundantní či duplicitní kladné termy. Je to současně úplný
invariant indukce, kterou odpověď formuluje po permutaci souřadnic.
Prázdná rodina reprezentuje 0; při jediném prázdném B reprezentuje
1 a S=∅. Vzorec nevyžaduje antichain.

## 35(b): obě implikace shellingové podmínky — P0693

Jestliže B_j∩S_k≠∅ pro každé j<k, mají D_j a D_k v některé
souřadnici pevnou 1 a pevnou 0, a jsou tedy disjunktní.

Obráceně nechť B_j∩S_k=∅ pro nějaké j<k. Bod x=complement(S_k)
patří D_k, protože S_k je disjunktní s B_k, a zároveň patří C(B_j).
Prefixová verze P0692 jej pokrývá některou D_i, i<k.
Proto D_k protíná dřívější novou krychli; nemusí to být přímo D_j.
To ověřuje přesně logický krok v odpovědi a dokazuje ekvivalenci.

## Všechna počáteční pořadí a stíny — P0694

Pro pořadí (1100,0110,0011) jsou jednoprvkové rozdíly postupně
{1}, pak {2}; první rozdíl do třetího členu má velikost 2 a
nepřispívá. Proto

    (S₁,S₂,S₃)=(0000,1000,0100).

Každý dřívější B protíná příslušný nenulový stín, takže jde o
shelling. Výsledné krychle jsou právě P0690.

Při pořadí (1100,0011,0110) je S₂=0000, neboť první rozdíl
má dva bity; shelling selže už pro první dvojici.
Do S₃ přispívá první člen bitem 1 a druhý bitem 4,
takže S₃=1001, jak uvádí zadání.
Známé erratum z 21.4.2019 přidává k prvnímu příkladu „in that order“.
Závislost na pořadí je v tomto důkazu výslovná; nejde o nový nález.

## 35(c): nutnost primes a jeden přidaný kód — P0695

To, že každý kladný prvoimplikant musí být mezi kladnými B,
přebíráme v přesném rozsahu z proof-035, P0609–P0611:
jeho charakteristický bod potřebuje některý B⊆prime a primalita
pak vynutí rovnost. Nevztahujeme to na libovolnou zápornou DNF.

Pro dva kódy 1100 a 0011 je v obou možných pořadích první
rozdíl dvoubitový. S₂ je prázdný, takže žádný shelling neexistuje.
Přidání 1011 nemění funkci, protože tento term implikuje 0011.
Pořadí

    (1100,1011,0011),   stíny (0000,0100,1000)

splňuje všechny tři párové podmínky. Výsledné krychle jsou
11**, 1011, 0*11 a dávají přesně vytištěnou ortogonální DNF

    x₁x₂ ∨ x₁¬x₂x₃x₄ ∨ ¬x₁x₃x₄.

Samostatný nemožnostní argument pro dva původní členy a tento
svědek dokazují, že právě jeden přidaný kladný kód stačí a je nutný.

## 35(d): vytištěný svědek — P0696

Označme

    A=12, B=23, C=34, D=45, E=124.

Jde o kódy 11000,01100,00110,00011,11010. Číslice zde znamenají
množiny souřadnic, nikoli desetinné kódy.
Vytištěné pořadí (B,C,D,E,A) má stíny

| člen | stín jako množina | stín jako kód | nová krychle |
|---|---|---|---|
| B | ∅ | 00000 | *11** |
| C | {2} | 01000 | *011* |
| D | {3} | 00100 | **011 |
| E | {3,5} | 00101 | 11010 |
| A | {3,4} | 00110 | 1100* |

Každý stín protíná všechny dřívější členy: pro E jsou to
B∩{3,5}, C∩{3,5}, D∩{3,5}; pro A mají B/C bit 3,
D/E bit 4. Předchozí dva kroky jsou bezprostřední singletony.
Všechny podtržené bity v odpovědi souhlasí.

## Proč je pořadí právě osm — P0697

Následující tabulka obsahuje všechny možné generátory stínu cíle;
přispěje jen generátor ležící v pořadí před cílem.

| cíl | generátor → přidaný bit |
|---|---|
| A | B→3, E→4 |
| B | A→1, C→4 |
| C | B→2, D→5 |
| D | C→3 |
| E | B→3, C→3, D→5 |

Z shellingové podmínky pro D plyne D<A a D<E: jeho jediný možný
stín {3} je disjunktní s A i E. Z A⊂E plyne E<A, protože
kdyby A předcházel E, nemohl by protínat jeho stín.
Máme tedy D<E<A.

Zbývající podmínky tabulky jsou ekvivalentní těmto dvěma:

1. C není poslední mezi B,C,D. D před B vyžaduje C před B;
   B před D vyžaduje C před D.
2. Je-li E před C, musí být B před C. Podmínka pro A před C
   je pak automatická, protože E<A. Podmínka pro E před B
   je automatická z D<E a bodu 1.

Všechny ostatní dřívější členy protne jejich vlastní jednoprvkový
příspěvek nebo už vynucený E; tabulka tím dává i postačitelnost.
Čtyři přípustná relativní pořadí B,C,D a počty rozšíření jsou:

| relativní pořadí | nutná další omezení | počet |
|---|---|---|
| B,C,D | D<E<A | 1 |
| C,B,D | D<E<A | 1 |
| C,D,B | vložit B mezi/okolo řetězce E<A po D | 3 |
| D,C,B | navíc C<E; pak vložit B do E<A | 3 |

V posledním řádku E<C odporuje bodu 2. Žádný případ nechybí,
protože obě zbývající relativní pořadí mají C poslední.
Celkem 1+1+3+3=8, bez procházení 5! permutací.

## 35(e): symetrická přidaná rodina a všechny podtržené bity — P0698

Původní členy jsou A=12, B=23, C=34, D=45, E=56.
První vytištěné řešení přidává F=125 a H=256. Oba jsou implikanty:
F obsahuje A, H obsahuje E. Množina sedmi kódů je symetrická
při obrácení souřadnic i↔7−i, které zaměňuje F a H.
Netvrdíme navíc symetrii samotného zvoleného pořadí.

Pro vytištěné pořadí (C,B,D,F,A,H,E) vycházejí:

| člen | S jako množina | S jako kód | nová krychle |
|---|---|---|---|
| C | ∅ | 000000 | **11** |
| B | {4} | 000100 | *110** |
| D | {3} | 001000 | **011* |
| F | {3,4} | 001100 | 11001* |
| A | {3,5} | 001010 | 110*0* |
| H | {1,3,4} | 101100 | 010011 |
| E | {2,4} | 010100 | *0*011 |

Tyto stíny se získají ze všech singletonů B_j∖B_k, ne výběrem
několika vhodných. Pro poslední čtyři řádky průniky se všemi
dřívějšími členy postupně dosvědčují bity:

    F: 3 nebo 4, 3, 4;
    A: 3, 3, 5, 5;
    H: 3 nebo 4, 3, 4, 1, 1;
    E: 4, 2, 4, 2, 2, 2.

Proto je seznam shelling a díky P0692 pokrývá přesně původní funkci.
Ověřeny jsou oba přidané kódy, všechny stíny i podtržení v odpovědi.

## Druhá rodina: obecná redukce podmínek — P0699

Pro údaj 42 jsou původní A,…,E stejné, ale přidané členy jsou

    F=125 (110010), G=235 (011010).

Opět jsou redundantní implikanty, protože obsahují A, respektive B.
Úplná tabulka možných singletonových příspěvků:

| cíl | generátor → přidaný bit |
|---|---|
| A | B→3, F→5 |
| B | A→1, C→4, G→5 |
| C | B→2, D→5 |
| D | C→3, E→6 |
| E | D→4 |
| F | B→3, G→3, D→4, E→6 |
| G | A→1, F→1, C→4, D→4, E→6 |

Z podmínek shellingu nejprve dostáváme:
F<A a G<B kvůli obsaženým členům;
D<F, D<A, protože možný stín D⊆{3,6} neprotíná F ani A;
E<F,E<G,E<A,E<B, protože stín E⊆{4} neprotíná tyto čtyři členy.

Podmínky pro trojici C,D,E dále říkají, že D není poslední:
E<C vyžaduje D<C a C<E vyžaduje D<E.
Kdyby G<D, podmínka v D by vyžadovala C<D. Současně E<G<D,
takže by D bylo poslední mezi C,D,E, spor. Proto i D<G.

Všechny získané pevné nerovnosti lze shrnout do posetu

    D,E před F i G;   F<A;   G<B.

Zbývají právě dva zákazy:

    D není poslední mezi C,D,E;
    B není poslední mezi A,B,C.

Druhý je kombinací C<A⇒B<A a A<C⇒B<C.
Postačitelnost lze ověřit přímo v úplné tabulce:
v A bit 5 od F pokryje D/E/F/G, případ C vyřeší druhý zákaz;
v B bit 5 od G pokryje D/E/F/G, A/C přispějí samy;
v C dřívější A potřebuje B a dřívější E potřebuje D, což
jsou oba zákazy, zatímco dřívější F/G již mají před sebou D.
V D nemohou být dříve A/F/B/G, ostatní přispějí samy.
V E nemohou být dříve A/B/F/G, dřívější C vyřeší první zákaz.
V F je případ C pokryt povinně dřívějším D a ostatní přispívají
samy; v G jsou všechny možné dřívější členy vlastními generátory.
To vyčerpává každou podmínku, nikoli jen nutné podmínky.

Nyní C dočasně smažme. Zbývající pořadí začíná D,E nebo E,D;
potom jde o jedno ze šesti proložení dvou řetězců F,A a G,B.
Ve třech je A před B a pak B končí celé pořadí; ve třech je
B před A a pak končí A.

Vraťme C do jedné ze sedmi mezer tohoto šestiprvkového pořadí:

- Při začátku D,E první zákaz nic neomezuje.
  Je-li A<B, druhý zákaz nutí C až za B: jediná mezera.
  Je-li B<A, druhý zákaz nic neomezuje: sedm mezer.
  Dostáváme 3·1+3·7=24 pořadí.
- Při začátku E,D první zákaz nutí C až za D: zbývá pět mezer.
  Pro A<B je stále jedinou možností až za poslední B;
  pro B<A lze použít všech pět.
  Dostáváme 3·1+3·5=18 pořadí.

Mazání a vkládání C jsou navzájem inverzní, takže není
dvojí započtení. Celkem je přesně 24+18=42 shellingů.
Neproběhl census 7! pořadí; důkaz je vyčerpávající redukcí
na dva řetězce a povolená místa jediného dalšího členu.

## Náklady, errata a mapa celé p84 — P0700

Pro zadaných p kódů lze stíny vypočítat všemi j<k pomocí
prokázané maskové operace; test shellingu pak používá stejné
množství párových průniků. Při n-bitových polích jde o O(p²n)
bitové práce a O(pn) uložených maskových bitů; při kódu v jediném
slově o O(p²) těchto slovních operací. Nejde o tvrzení o počtu
nutných přidaných termů v obecném problému.

Relevantní all4a-pre, all4a, err4a, all4f0 a err4f0 i obě vrstvy
F1 byly prohledány podle stránek, stínů, shellingu a úlohy 35.
Jediná zdejší změna je známé upřesnění pořadí z roku 2019.
F1 úloha 35 na p55 je jiný bitový problém a nezaměňuje se za tuto.
Historická priorita Ball–Provan 1988 a jejich další aplikace jsou
bibliografická výjimka; obecné věty zde mají vlastní důkazy.

Úplný matematický obsah p84/file101 nyní pokrývají:

- všechny čtyři části 34 a nápověda: proof-043, P0679–P0689;
- definice ortogonality, plná DNF, pravděpodobnostní použití,
  konkrétní osmibodový příklad a všechny jeho kódy: P0690;
- stíny, maskový vzorec a počáteční dvě pořadí: P0691/P0694;
- 35(a)/(b), oba obecné směry: P0692/P0693;
- 35(c), prvoimplikanty a nutný/dostačující jeden nový kód: P0695;
- 35(d), svědek i přesný počet v odpovědi: P0696/P0697;
- 35(e), oba přidané kódy, symetrie, podtržení a přesný počet42:
  P0698/P0699.

P541/file558 zůstává partial, protože obsahuje další odpovědi
36 a začátek 37. Žádný nový nález či kandidát. Následuje úloha 36;
již hotový shelling minimálních cestových covers P0624 se neopakuje.
