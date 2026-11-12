# Fibonacciho prahy: celé101 a105

7. listopadu 2026. §7.1.1–101/105, zadání p92/file109,
odpovědi p552–553/file569–570. P1074–P1083, X0115. Původní
sazba všech stránek a detail podtržení i obou trojúhelníků
zobrazen. Žádný program, LP běh ani census. Proof-044 se přebírá
jen pro již dokázanou shellingovou větu; proof-067 jen pro přesné
obecné Y zobrazení z dvojic prime termů.

## 1. Normalizace vah a obě omezení funkce

Aby se nepletly indexy, Fibonacciho čísla označuji q_0=0,
q_1=q_2=1, q_{k+1}=q_k+q_{k-1}; funkci ze zadání označuji Φ_n.
Pro n≥3 má váhy

    (q_1,q_2,…,q_{n−1},q_{n−2}).

Identita Σ_{i=1}^r q_i=q_{r+2}−1 plyne indukcí z rekurence.
Celková váha je proto q_{n+1}−1+q_{n−2}=2q_n−1, lichá;
práh většiny je q_n. Funkce je monotónní a self-duální podle
proof-084. Pro n=7 jsou přesně váhy(1,1,2,3,5,8,5), délka25,
práh13, jak uvádí zadání.

Při x_n=x_{n−1}=0 je celý možný zbytek nejvýše
Σ_{i=1}^{n−2}q_i=q_n−1, tedy výsledek0. Při obou bitech1
už jejich váhy q_{n−1}+q_{n−2}=q_n stačí, tedy výsledek1.
Při x_n=1−x_{n−1} se suma po odečtení q_{n−2} změní na

    Σ_{i=1}^{n−2}q_i x_i + q_{n−3}x_{n−1},

s prahem q_n−q_{n−2}=q_{n−1}. Pro n≥4 je to přesně Φ_{n−1}.
Případ n=3 se bere jako samostatný základ, obyčejný medián tří bitů.

## 2. Úplnost a minimalita rekurze prime termů

Základ Φ_3 má právě podpory12,13,23. Předpokládejme nyní n≥4
a znalost všech minimálních pravdivých podpor Φ_{n−1}.
Žádná pravdivá podpora Φ_n nemůže vynechat oba poslední indexy.
Obsahuje-li oba, je minimální právě tehdy, je-li rovna{n−1,n}.
Tato dvojice je minimální, neboť jednotlivé váhy jsou menší než q_n.

Každá stará minimální podpora A se zvedne takto:

* obsahuje-li n−1, ponecháme A;
* neobsahuje-li n−1, přidáme n.

V první větvi jde o omezení x_n=0, x_{n−1}=1. Vítěznost
a nemožnost odstranit kterýkoli nižší index plyne z přesné
shody s Φ_{n−1}; odstranění n−1 dá oba poslední bity0.
Ve druhé větvi jde o x_n=1, x_{n−1}=0 a stejný argument;
odstranění n opět dá oba poslední bity0. Zvednuté podpory
jsou tedy všechny skutečně minimální a navzájem odlišné.

Doplním krok úplnosti, který samotné rozdělení vstupů ještě
nezaručuje. Má-li nová minimální podpora n, ale ne n−1, obsahuje
podle omezení nějakou starou minimální A bez n−1, a minimalita
nutí přesně A∪{n}. Má-li n−1, ale ne n, obsahuje nějakou starou
minimální A. Kdyby A neobsahovala n−1, její původní váha by byla
alespoň q_{n−1}. Obsahovala by alespoň dva indexy: největší
dostupná jednotlivá váha q_{n−2} je menší než q_{n−1}.
Můžeme tedy vybrat j∈A s j≤n−3 a q_j≤q_{n−3}. Pak

    Σ_{i∈A\{j}}q_i ≥ q_{n−1}−q_{n−3}=q_{n−2}.

Podpora (A\{j})∪{n−1} by už vyhrála v Φ_n a byla by vlastní
podmnožinou původní nové podpory, spor. Proto A obsahuje n−1
a nová podpora je přesně A. Rekurze je úplná, nejen dostačující.

Máme n−1 zvednutých podpor a jednu novou dvojici: přesně n
prime implikantů pro každé n≥3. Monotónnost zaručuje, že žádný
prime implicant nepotřebuje negovaný literál.

## 3. Uzavřený tvar všech podpor a n=7

Položme

    T_k={k} ∪ {k+1,k+3,k+5,…≤n}       (1≤k≤n−1),
    T_0={1,3,5,…≤n}.

Tyto množiny splňují právě výše dokázanou rekurzi: nová T_{n−1}
je poslední dvojice; starý T_k dostane n právě tehdy, když neobsahuje
n−1. Základ n=3 souhlasí, tedy seznam je úplný pro všechna n.
V pořadí T_{n−1},…,T_0 dává pro n=7 přesně

    67, 56, 457, 346, 2357, 1246, 1357,

což jsou všechna vytištěná zadání části(a), po komutativním
přeskládání literálů. Nejde pouze o namátkovou kontrolu těchto sedmi.

## 4. Celý shelling a všechna podtržení části(b)

Pro uvedené sestupné pořadí definujme

    S_k={k+2,k+4,k+6,…≤n}       (1≤k≤n−1),
    S_0={2,4,6,…≤n}.

Dokážeme, že S_k jsou přesně stíny z úlohy35. Pro dřívější
T_l, l>k≥1, při stejné paritě l,k je T_l\T_k={l}.
Při opačné paritě je rozdíl {l+1,l+3,…≤n}. V obou případech
je neprázdný a leží v S_k. Každý prvek j∈S_k, j<n, sám vzniká
jako jednoprvkový rozdíl z T_j. Je-li j=n, dostaneme singleton
{n} z T_{n−1}. Žádný jiný singleton není možný, takže stín je
přesně S_k. Pro T_0 stejný argument rozliší sudé l (rozdíl{l})
a liché l (sudý suffix od l+1); výsledný stín je přesně S_0.

Každý dřívější T_l tedy protíná příslušný S_k. To je přesná
shellingová podmínka P0693, již dokázaná v proof-044. Hledaná
ortogonální DNF je tudíž disjunkce právě n krychlí

    (AND_{i∈T_k} x_i) AND (AND_{j∈S_k} ¬x_j),
    k=n−1,n−2,…,0.

Pro n=7 jsou podtržené nulové pozice postupně

    ∅, {7}, {6}, {5,7}, {4,6}, {3,5,7}, {2,4,6}.

Detail původní sazby přesně odpovídá všem těmto bitům. Nejde
jen o jednu negaci na řádek; oba delší stíny jsou pro disjunktnost
nutné. Hotová obecná věta P0692/P0693 dává úplné pokrytí i
disjunktnost, bez znovuřešení všech vstupů.

## 5. Obě Y konstrukce a všechny jejich buňky

Očíslujme prime termy p_i=T_{n−1−i}, 0≤i≤n−1. Přesně přebíráme
P0910 z `notes/proof-067-y-representation-flip.md`: v trojúhelníku
řádu n−2 lze na buňku(r,j), 0≤j≤r≤n−2, dát libovolnou
proměnnou z p_j∩p_{r+1}; výsledné Y je daná monotónní self-duální
funkce. Průniky jsou neprázdné (je to již doložený obecný důsledek
self-duality). Zde je počet prime termů n≥3, takže nenastává
starý jednočlenný okraj P0912.

První obecnou konstrukci získáme volbou největšího indexu
v každém průniku, druhou volbou nejmenšího. Pro n=7 jsou všechny
průniky po řádcích:

    {6}
    {7}, {5}
    {6}, {6}, {4}
    {7}, {5}, {5,7}, {3}
    {6}, {6}, {4}, {4,6}, {2}
    {7}, {5}, {5,7}, {3}, {3,5,7}, {1}.

Maximum/minimum těchto 21 množin dává přesně obě vytištěné
matice, včetně všech odlišných vnitřních voleb. Generalizace
je tím explicitní pro každé n: má n(n−1)/2 buněk a nepotřebuje
konstanty. Netvrdí se nejmenší možný Y trojúhelník.

## 6. Úloha105: nutné nerovnosti a obecný duální certifikát

Nechť libovolná jiná reprezentace čistou lichou většinou má
nezáporné celočíselné násobnosti w_1,…,w_n a lichý součet W.
Na každé pravdivé podpoře p_i musí platit

    Σ_{j∈p_i}w_j − Σ_{j∉p_i}w_j ≥ 1.                 (*)

Jde přímo o podmínku většiny, nikoli o neprokázaný výsledek LP.
Pro n=7, p_i v pořadí §3, dává (*) přesně všech sedm nerovností
v odpovědi105, včetně znamének u každé váhy.

Přiřaďme těmto n řádkům kladné multiplikátory

    λ_i=q_{i+1}       pro 0≤i≤n−2,
    λ_{n−1}=q_{n−2}.

Jejich součet Λ je2q_n−1. Pro index proměnné j označme
H_j=Σ_{i:j∈p_i}λ_i. Z explicitního tvaru T_k máme

    H_j=q_{n−j}
        + Σ_{k=j−1,j−3,…≥1} q_{n−k}
        + [j je liché] q_{n−2},                     (**)

kde q_0=0 ošetřuje j=n. První dvě hodnoty jsou
H_1=q_{n−1}+q_{n−2}=q_n a H_2=q_{n−2}+q_{n−1}=q_n.
Pro 1≤j≤n−2 rozdíl H_{j+2}−H_j podle (**) je

    q_{n−j−2}+q_{n−j−1}−q_{n−j}=0.

Tedy všechna H_j=q_n. Koeficient w_j po vynásobení a sečtení
nerovností(*) je proto2H_j−Λ=1. Dostáváme obecně

    Σ_j w_j ≥ Σ_i λ_i = 2q_n−1.

Původní reprezentace má přesně tuto délku, takže je nejkratší.
Platí i n=3, kdy jsou všechna λ rovna1. Pro n=7 dostaneme
přesně multiplikátory1,1,2,3,5,8,5 a mez25 z odpovědi.
Certifikát funguje dokonce pro reálné nezáporné váhy splňující
normalizované nerovnosti(*); stačí však pro požadovanou
celočíselnou většinovou reprezentaci. O jiném obvodovém modelu
ani o minimálním počtu hradel nic netvrdí.

Ani případné povolení konstant a negovaných vstupních literálů
by délku nezkrátilo. Dvojici x_j,¬x_j lze z liché většiny odstranit
stejně jako0,1. Po všech takových zrušeních je každý vstup pouze
jedné polarity. Každá proměnná Φ_n je podstatná, protože se
vyskytuje v některé minimální pravdivé podpoře; monotónnost tedy
vynutí kladnou polaritu. Pro zbylé nezáporné váhy a konstantní
práh self-dualita podle proof-085, §2, vylučuje dosažitelnou
rovnost poloviny součtu a všechny pravdivé podpory splňují(*).
Proto už počet proměnných literálů je alespoň2q_n−1; konstanty
a dříve zrušené páry mohly původní délku jen zvětšit.

## 7. Bibliografie, errata a rozsah

Primární [IEEE záznam Muroga1965](https://ieeexplore.ieee.org/document/4038392/)
potvrzuje název *Lower Bounds of the Number of Threshold Functions
and a Maximum Weight*, EC-14(2), duben1965, strany136–148,
DOI10.1109/PGEC.1965.263958. Abstrakt se výslovně týká rekurzivní
rodiny a dolních mezí maximálních minimálních vah. Priorita
objevu a celý historický článek se znovu neauditují; matematický
optimální výsledek105 má úplný vlastní certifikát výše.

Vrstvy `all4a-pre`, `all4a`, `err4a`, `all4f0`, `err4f0`
prohledány podle Fibonacci, p92/552/553 a úloh101/105. Žádná
relevantní oprava ani nový nález. Všechny části101 i105 a
matematické dodatky odpovědi101 jsou uzavřeny. P76 stále čeká
na vlastní optimalizační postup103, p92/552/553 obsahují další
dosud neuzavřené úlohy; žádná celá stránka se tím nepovyšuje.
