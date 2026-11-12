# Úlohy 7.1.1–36 až 38: obecný shelling a ostrá ortogonální DNF

Checkpoint X0074, P0701–P0710. Zadání p85/file102, odpovědi
p541–542/file558–559. Původní obrazy file102.png, proof-file558.png,
proof-file559.png a nový detail proof-answer37-detail.png.
Žádný matematický program. Obecná věta o stínech z proof-044
a již hotová úloha 39 z proof-037 se přebírají bez opakování.

## 36: bitová operace a reprezentace funkce — P0701

Pro x>0 operace x'=x & (x−1) vymaže právě pravou krajní jedničku:
odečtení 1 ji změní na 0, všechny nižší nuly na 1 a vyšší bity
ponechá; průnik vymaže nově vytvořené nižší jedničky.
Pro x=0 je x'=0 při celočíselném i slovním výkladu.

Monotónní f, která není identicky 1, má f(0)=0. Pro každý pravdivý
bod y opakovaně mažme pravou jedničku, dokud vznikne 0. Na řetězci
je nějaký krok x→x' s f(x)=1 a f(x')=0. Takový x patří zadané
množině B a x⊆y. Jeho kladná krychle pokrývá y. Obráceně každá
kladná krychle s minimem x∈B leží v f díky monotónnosti.
Seznam B tedy opravdu reprezentuje f, což je potřeba k tvrzení
o ortogonální DNF, nejen k samotné definici shellingu.

Pro f=0 je B prázdné; pro n=0 je to jediný povolený případ.
Vyloučení f=1 zajišťuje uvedenou reprezentaci: u f=1 by B bylo
prázdné a nereprezentovalo by f, i když prázdný seznam formálně
shellingovou podmínku splňuje. Nenazýváme konstrukci polynomiální
ve stručném popisu f: přímá tvorba B z tabulky prohlíží 2^n bodů.

## 36: celý důkaz klesajícího lexikografického pořadí — P0702

Vezměme libovolné dva členy B_j před B_k. V první rozdílné
souřadnici mají tvary

    B_j=α1β,   B_k=α0γ.

Začněme x₀=α1γ a opakujme x_{i+1}=x_i', dokud nedostaneme
x_l=α00…0. Smažeme tedy nejprve jedničky v γ, nakonec novou
jedničku v první rozdílné souřadnici. Před tímto posledním krokem
zůstává prefix α1.

Protože x₀⊇B_k, monotónnost dává f(x₀)=1. Naproti tomu
x_l⊆B_j': odstranění pravé jedničky B_j zachová celý prefix α;
je-li β nulové, B_j'=x_l, jinak je B_j' ještě větší.
Tedy f(x_l)=0, jelikož definice B_j dává f(B_j')=0.

Někde na tomto řetězci je f(x_i)=1 a f(x_{i+1})=0.
Bod x_i je členem B, leží před B_k lexikograficky, protože má
prefix α1, a x_i∖B_k obsahuje právě první rozdílnou souřadnici.
Ostatní jedničky x_i jsou podmnožinou jedniček γ a společného α.

Tento dřívější člen proto přidá do S_k právě daný bit, který
zároveň patří B_j. Dostáváme B_j∩S_k≠∅ pro každé j<k.
To je celé obecné tvrzení; není nahrazeno testem několika funkcí.
P0701 a P0692/P0693 nyní dávají reprezentující ortogonální DNF.

## 36: úplnost vytištěného čtyřčlenného seznamu — P0703

Pro f=x₁x₂∨x₃x₄ může přechod do nepravdy po smazání pravé
jedničky nastat dvěma způsoby:

- Platí x₃x₄=1. Pravou jedničkou je x₄ a po jejím smazání
  musí být x₁x₂ nepravda. Dostáváme 0011,0111,1011.
- Pravdivý je pouze první pár. Každá další jednička v x₃/x₄
  by se smazala bez zrušení prvního páru, takže musí být obě nuly.
  Dostáváme 1100.

Proto B v klesajícím pořadí je přesně
(1100,1011,0111,0011), nikoli jen podmnožina zadaného B.
Stíny jsou (0000,0100,1000,1100), výsledné krychle
11**,1011,0111,0011. Jsou disjunktní a mají 4+1+1+1=7 bodů,
tj. všech 16−3² pravdivých bodů. Konstrukce 36 nemusí být
minimální: dřívější 35(c) dává pro stejnou funkci tři krychle.

## 37: obecná shellovatelná konstrukce s 2^n−1 členy — P0704

Pišme f_n=∨_{k=1}^n x_{2k−1}x_{2k}. Pro každý k=n,n−1,…,1
zařaďme všechny kódy

    B_(k,T)={2k−1,2k} ∪ {2j : j∈T},
    T⊆{k+1,…,n},

uvnitř bloku v klesajícím lexikografickém pořadí T.
Každý kód je implikantem f_n a členy s T=∅ obsahují všechny
původní páry, takže disjunkce představuje přesně f_n.
Kódy jsou různé podle prvního obsazeného páru k a podle T.
Je jich Σ_{k=1}^n2^(n−k)=2^n−1.

Jejich stíny lze odvodit úplně:

    S_(k,T)={2j−1 : j∈T} ∪ {2j : j>k, j∉T}.

Z dřívějšího bloku j>k je v rozdílu vždy lichý bit 2j−1.
Singleton vznikne právě když j∈T a ostatní přidané sudé bity
předchozího člena už jsou v T; člen s žádnými přídavky tak vždy
dosvědčuje potřebný lichý bit. Jiné singletony tyto bloky nevytvoří.
Ve vlastním bloku může singleton vzniknout pouze sudým bitem
2j pro j∉T. Dřívější člen T∪{j} jej vždy vytvoří.

Nová krychle tedy má:
páry před k volné, pár k roven 11 a každý pozdější pár j ve tvaru

    01, je-li j∈T;   *0, je-li j∉T.

Každý pravdivý vstup má jediný poslední pravdivý pár k.
Každý pozdější nepravdivý pár patří právě jednomu z disjunktních
tvarů 01 a *0. Tím jsou dokázány disjunktnost a úplnost všech krychlí,
a podle P0693 je zadané pořadí shelling. Nezaměňuje se s jiným,
globálně klesajícím pořadím úlohy 36.

Pro n=1 vznikne jediný člen 11; pro n=0 je prázdná disjunkce
i prázdná rodina, v souladu s počtem 0. Explicitní zapsání kódů
má O(n2^n) bitů a lze je takto přímo vypsat; žádná implicitní
polynomiální komprese výstupu se netvrdí.

## 37: všech sedm vytištěných shellingových členů — P0705

Dosazení n=3 do předchozí konstrukce dává přesně:

| B | S | výsledná krychle |
|---|---|---|
| 000011 | 000000 | ****11 |
| 001101 | 000010 | **1101 |
| 001100 | 000001 | **11*0 |
| 110101 | 001010 | 110101 |
| 110100 | 001001 | 1101*0 |
| 110001 | 000110 | 11*001 |
| 110000 | 000101 | 11*0*0 |

Souhlasí celý seznam i podtržené bity původní odpovědi.
Počty bodů 16+4+8+1+2+2+4=37 souhlasí s
2^6−3^3=37; hlavní důkaz disjunktnosti je však obecný P0704,
nikoli pouze tento součet.

## 37: cyklický příklad a nemožnost vzniku shellingem — P0706

Původní sazba má krychle

    110***, 1110**, **110*, **1110, 0***11, 10**11, 111111.

Na úrovni tří párů označme pravdivý pár stavem T a nepravdivý F.
První dvě krychle představují T,F,*; druhé dvě *,T,F;
třetí dvě F,*,T, přičemž F je disjunktně rozděleno na 0* a 10.
Poslední krychle je T,T,T.

Cyklické slovo délky 3 obsahující T i F má právě jeden přechod
T→F: při jednom T je zřejmý, při dvou T je jediná navazující
dvojice T před jediným F. Každý pravdivý vstup, který nemá
všechny páry pravdivé, proto patří právě jedné z prvních šesti
krychlí; všechny pravdivé páry pokrývá jen poslední. Jde o
disjunktní rozklad a cyklické otočení párů jej permutuje.
Velikosti 8+4+8+4+8+4+1 opět dávají 37.

Proč tento konkrétní rozklad není výstupem konstrukce 35 pro
žádné pořadí jeho sedmi bitových kódů: první stín musí být prázdný,
tedy první krychle nesmí mít žádnou pevnou nulu. Taková je zde
pouze 111111. Každý jiný kód má jen dvě nebo tři jedničky,
takže jeho rozdíl od prvního kódu má tři nebo čtyři bity.
Stín druhého člena je proto prázdný a shellingová podmínka už
pro tuto dvojici selže. Navíc by druhá krychle neměla požadovanou
pevnou nulu. To dokazuje i dodatek „not based on shelling“.

## 37: všech devět lokálních váhových součtů — P0707

Definujme v(a,b)=a+b−3ab. Hodnoty na bodech 00,01,10,11
jsou 0,1,1,−1. Pro devět možných neprázdných podkrychlí dvojice
souřadnic jsou součty následující:

| krychle | 00 | 01 | 10 | 11 | 0* | *0 | 1* | *1 | ** |
|---|---|---|---|---|---|---|---|---|---|
| součet v | 0 | 1 | 1 | −1 | 1 | 1 | 0 | 0 | 1 |

Váha odpovědi je w_x=−∏_{j=1}^n v(x_{2j−1},x_{2j}),
s jediným minusem před celým součinem.
Libovolná 2n-rozměrná podkrychle je kartézský součin svých
projekcí na tyto dvojice. Distributivita konečných součtů dává

    Σ_{x∈Q}w_x=−∏_j Σ_{(a,b)∈Q_j}v(a,b) ∈ {0,1,−1}.

Tím je věta pro všechny podkrychle prokázána z uvedené tabulky;
nejde pouze o ověření n=1 bez zdůvodnění přenosu.

## 37: přesná váha pravdivé množiny a globální optimum — P0708

Nenulovou váhu mají právě body bez páru 00. Má-li bod k párů 11,
zbývající n−k páry mohou být 01 nebo 10, tedy existuje
binom(n,k)2^(n−k) takových bodů. Jejich váha je
−(−1)^k=(−1)^(k−1). Bod je pravdivý právě při k≥1. Proto

    Σ_{x:f_n(x)=1}w_x
      =Σ_{k≥1}binom(n,k)2^(n−k)(−1)^(k−1)
      =2^n−(2−1)^n=2^n−1.

V každé ortogonální DNF jsou disjunktní krychle Q právě rozkladem
pravdivé množiny. Protože každý jejich váhový součet je ≤1,

    počet členů ≥ Σ_Q Σ_{x∈Q}w_x
                =Σ_{x:f_n(x)=1}w_x =2^n−1.

Záporné váhy nejsou překážkou: používá se pouze horní mez 1 pro
součet na každé jednotlivé krychli a disjunktnost rozkladu.
Důkaz platí pro všechny ortogonální DNF včetně záporných literálů,
nejen pro shellingové či prvoimplikantové konstrukce.
P0704 dosahuje stejné meze, takže optimum je přesně 2^n−1.
Při n=0 je prázdná pravdivá množina a obě meze jsou 0.

## 38: satisfiabilita DNF a její doména — P0709

V knize jsou implicanty konzistentní neprázdné krychle, jak již
vymezilo P0597 a proof-035. DNF z těchto termů je splnitelná
právě tehdy, když má alespoň jeden term: přiřadíme jeho literálům
požadované hodnoty a ostatním libovolné.

Je-li vstup syrový syntaktický OR konjunkcí, nejprve vynecháme
termy obsahující x_i i ¬x_i a odstraníme opakované literály.
Splnitelnost je ekvivalentní existenci alespoň jednoho zbývajícího
termu. Jde o polynomiální kontrolu; při indexovaných proměnných
a značkách výskytů o lineární průchod seznamy literálů.
Prázdná DNF je nesplnitelná, term bez literálů je konstantní 1.
Tím se nevydává rozporný syntaktický term za skutečný implicant.

## 38: přesný význam obtížnosti tautologie — P0710

DNF není tautologie právě tehdy, když existuje přiřazení s hodnotou 0.
Takové přiřazení lze ověřit v čase lineárním v popisu formule;
komplement problému tautologie DNF je tedy v NP.

Pro libovolnou 3CNF F lze De Morganovými pravidly v lineární
velikosti vytvořit DNF ¬F: každá klauzule přejde na jediný term.
Pak ¬F je tautologie právě když F není splnitelná. NP-úplnost
3SAT se přebírá v přesném rozsahu z P0614/P0631/P0632; redukce ani
Cookův důkaz se neopakují. Komplementace tudíž dává coNP-úplnost
tautologie DNF. To dokládá vytištěné slovo „hard“, aniž by se
tvrdila dokázaná nerovnost P≠NP nebo chybně NP-úplnost samotné
tautologie. Negace DNF je CNF, nikoli obecně stejně malá DNF
po jiném libovolném převodu.

## Errata, bibliografie a úplná mapa p541

Relevantní all4a-pre, all4a, err4a, all4f0, err4f0 byly prohledány
podle stran, čísel odpovědí, vah a shellingu. Pro36–38 nebyla
nalezena související matematická oprava; F0 odpověď36 na p185
a37 na p186 patří jiným sekcím a nezaměňují se za tento blok.
Známé opravy sousední39 už byly aplikovány v proof-037.

P541/file558 je nyní celá argumentově pokryta:

- 34(c)/(d), všechny logaritmy a obě větve: proof-043;
- 35(a)–(e), všechny masky a počty8/42: proof-044;
- 36, obecná existence svědka a jeho lexikografická poloha: P0701–P0703;
- první část37, obecná sedmičlenná konstrukce pro n=3, cyklická
  alternativa, všechny váhy a dolní mez: P0704–P0708,
  včetně nutného pokračování počítání na p542.

Bibliografické výjimky: Boros–Crama–Ekin–Hammer–Ibaraki–Kogan 2000,
Ball–Nemhauser 1979 a jejich priority nebyly ověřeny v primárních
článcích; nic z toho není nepřiznaným vstupem našich důkazů.
Starší výjimky z34/35 zůstávají.

Úloha39 je již celá uzavřena v proof-037, P0630–P0632, včetně
obou známých oprav; nyní se pouze přebírá při dosažení jejího
sekvenčního místa. P85 a p542 nadále obsahují další otevřené úlohy.
Žádný nový nález ani kandidát. Další úloha40; textový frontier p57
a čtenářský cursor p218 zůstávají oddělené.
