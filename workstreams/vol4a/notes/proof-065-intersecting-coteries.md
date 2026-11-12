# Úlohy 7.1.1–65/66: protínající se rodiny a coteries

Checkpoint X0094, P0887–P0897. Zadání p87–88/file104–105,
odpovědi p546/file563 a odkázané funkce tabulky 2 na p71/file88
přečteny v původní sazbě. Nové rendery `proof-file105.png`
a `proof-file088.png`. Žádná enumerace, SAT ani matematický program.
Věty o maximálních rodinách a nedominovaných coteries níže mají
výslovnou doménu n≥1; společný nulární limit je veden pod P0863.

## Přesná korespondence rodin a funkcí — P0887

Pro U=[n] přiřazení X↦χ_X dává bijekci mezi podmnožinami U
a bitovými vektory délky n: inverzí je množina jedničkových pozic.
Rodina F pak odpovídá právě své indikátorové funkci
f(χ_X)=[X∈F]; inverzí je množina vstupů, na nichž f=1.
Tato bijekce platí i pro prázdnou rodinu a n=0. Inkluze množin
odpovídá souřadnicovému pořadí vektorů, komplement souřadnicové
negaci. Tím je přesně doložen převod jazyka na začátku 65.

## Maximalita implikuje monotónnost a selfdualitu — P0888

Rodina je protínající se, jestliže X∩Y≠∅ pro **všechny**
X,Y∈F, včetně X=Y. Nemůže tedy obsahovat prázdnou množinu.
Pro n≥1 nemůže být maximální protínající se rodina prázdná:
šlo by přidat například {1}.

Ověřme jednotlivě tři vlastnosti z odpovědi:

1. Je-li X∈F, pak U\X∉F, protože jejich průnik je prázdný.
2. Je-li X∈F a X⊆Y, pak Y protíná každý Z∈F, neboť
   obsahuje neprázdné X∩Z. Přidání Y tedy zachová protínání;
   maximalita nutí Y∈F. To je přesně monotónnost indikátoru.
3. Je-li X∉F, přidání X poruší protínání. Existuje Y∈F
   disjunktní s X; pro X=∅ lze vzít libovolné Y, neboť F
   není prázdná. Máme Y⊆U\X a podle bodu 2 také U\X∈F.

Body 1 a 3 říkají, že právě jedna z každé komplementární dvojice
patří do F. Proto f(¬x)=1−f(x). Důkaz nepletl maximalitu
v inkluzi s největší možnou velikostí rodiny.

## Opačný směr a všechny tři booleovské přepisy — P0889

Nechť f je monotónní a selfduální. Pokud by X,Y∈F byly
disjunktní, máme X⊆U\Y. Monotónnost dává f(U\Y)=1,
v rozporu se selfdualitou a f(Y)=1. Rodina je protínající se.
Pro každé X∉F je U\X∈F, takže přidání X vytváří disjunktní
dvojici; rodina je maximální.

Tento argument současně ověřuje dodatek odpovědi: vlastnosti
1 a 2 samy zaručují protínání, vlastnost 3 pak maximalitu.
Přepisy jsou přesně f(x)=1⇒f(¬x)=0, x≤y⇒f(x)≤f(y),
a f(x)=0⇒f(¬x)=1. Je nutné zachovat komplement na vstupu
a nelze jej zaměnit s komplementem jedné libovolné proměnné.

## Antichain a pozitivní prime implikanty — P0890

Libovolné inkluzní antichain C odpovídá monotónní funkce

    f_C(X)=1 ⇔ existuje Q∈C s Q⊆X.

Každé Q∈C je minimální pravdivou množinou: proper podmnožina
nemůže obsahovat jiné Q'∈C, jinak by C nebyla antichain.
Naopak každá minimální pravdivá X obsahuje některé Q∈C;
minimalita vynutí X=Q. Přesně tato minimální pravdivá množina
je indexovou množinou pozitivního prime implikantu, jak bylo
doloženo obecně pro monotónní funkce v proof-035.

Korespondence je tedy jednoznačná v obou směrech. Zahrnuje
C=∅ s f_C=0 i antichain {∅} s f_C=1. Druhá z nich však
není coterie: její jediné quorum neprotíná samo sebe.

## Protínání kvór jako nerovnost funkce — P0891

Protínání všech kvór je ekvivalentní

    f_C(X) ≤ 1−f_C(U\X) pro každé X⊆U.               (I)

Kdyby obě hodnoty f byly 1, existovala by kvóra Q⊆X
a Q'⊆U\X, tedy disjunktní. Obráceně z disjunktních kvór
Q,Q' zvolme X=Q; pak f_C(X)=f_C(U\X)=1. Platí to i
pro stejná kvóra; prázdné quorum je tím správně vyloučeno.
Prázdná coterie sama obě univerzální podmínky splňuje.

## Směr dominance a jeho striktnost — P0892

Pro coteries C,C' je vytištěná podmínka dominance přesně

    C dominuje C' ⇔ f_{C'}≤f_C a f_{C'}≠f_C.

Pokud každý Q'∈C' obsahuje nějaké Q∈C, každá množina X
obsahující Q' obsahuje i Q. To dává bodovou nerovnost.
Obráceně ji vyhodnoťme na X=Q': z f_C(Q')=1 dostaneme
požadované Q⊆Q'. Striktnost odpovídá C≠C', protože
P0890 dává jednoznačnost antichain reprezentace. Není možné
zaměnit směr této nerovnosti ani nahradit C≠C' pouhou
změnou zápisu stejné DNF.

## Oba příklady v zadání — P0893

Pro C₀={{1,2},{2,3}} mají obě kvóra průnik {2} a stejnou
velikost, takže tvoří coterie. Rodina D={{1,2},{1,3},{2,3}}
má každé dvě kvóra protínající se a rovněž žádnou proper
inkluzi. Obsahuje obě kvóra C₀, a proto C₀ dominuje;
striktnost dosvědčuje X={1,3}, pro něž f_D=1 a f_C₀=0.

Také E={{2}} je coterie a její jediné quorum je podmnožinou
obou kvór C₀. Dominuje C₀ a striktnost dosvědčuje X={2}.
Oba příklady platí na každém U obsahujícím 1,2,3; ostatní
proměnné mohou být nepodstatné.

## Selfdualita vylučuje dominující coterie — P0894

Nechť f_C je selfduální a jiná coterie D by ji dominovala.
Podle P0892 existuje X s f_C(X)=0, f_D(X)=1 a všude
f_C≤f_D. Selfdualita dává f_C(U\X)=1, takže také
f_D(U\X)=1. To porušuje (I) pro D. C je tedy nedominovaná.
Tento směr nevyžaduje hledat všechna ostatní možná kvóra.

## Není-li funkce selfduální, explicitně ji dominujeme — P0895

Pro coterie platí (I). Pokud f_C není selfduální, musí tedy
existovat Y s f_C(Y)=f_C(U\Y)=0. Je-li Y=∅ nebo Y=U,
pak f_C(U)=0, a tudíž C=∅. Ta je podle definice dominována
každou jinou coterie; na n≥1 například {{1}}. To přesně
ověřuje zvláštní prázdnou větev odpovědi.

V ostatních případech je Y neprázdná. Žádné staré quorum
Q nemůže být disjunktní s Y, jinak Q⊆U\Y a f_C(U\Y)=1.
Rodina C∪{Y} je proto protínající se, včetně průniku Y se sebou.
Vezměme její inkluzně minimální členy D. Jsou stále protínající
se a tvoří antichain, tedy coterie. Jejich vzestupný uzávěr je

    f_D(X)=f_C(X) OR [Y⊆X],

protože odstranění ne-minimálních členů vzestupný uzávěr nemění.
Právě tuto funkci navrhuje odpověď. Je monotónní, splňuje (I),
je ≥f_C a na Y je přísně větší. Proto D dominuje C.
To dokazuje i tvrzení, že nová funkce odpovídá skutečné coterie,
nikoli jen booleovské formuli s neověřeným průnikem.

S P0894 máme oba směry požadované charakterizace: nedominované
coteries jsou přesně prime antichain monotónních selfduálních
funkcí na neprázdném základním univerzu.

## Přesný matematický význam praktické preference — P0896

Je-li A množina dostupných uzlů a k operaci stačí získat
všechna povolení některého kvóra Q, operace je možná právě
když f_C(A)=1. Dominance C nad C' znamená, že každá dostupnost
umožňující operaci v C' ji umožní i v C; pro některou A navíc
operace v C možná je a v C' není. To je přesný význam preference
založené na dostupnosti, bez tvrzení o všech nákladech a všech
dalších vlastnostech libovolného distribuovaného protokolu.

Primární článek Garcia-Molina–Barbará, p841–843, potvrzuje tento
kontext, definice a použití k vzájemnému vyloučení a replikaci.
Samotný průnik množin nenahrazuje protokol, který brání uzlu
současně udělit konfliktní povolení; žádný takový implementační
algoritmus zde kniha ani tento důkaz nekonstruují.

## Všech dvanáct funkcí odkázané tabulky 2 — P0897

Na U={w,x,y,z} klasifikujeme všechny monotónní selfduální
funkce bez procházení jejich 2¹⁶ možných pravdivostních tabulek.
Je-li některý singleton pravdivý, funkce je příslušnou projekcí
podle P0859. To jsou přesně čtyři případy.

Jinak jsou všechny singletony nepravdivé a všechny jejich
komplementární trojice pravdivé. Zbývá vybrat hodnoty šesti
dvojic. Jsou rozděleny do tří komplementárních párů

    wx / yz,   wy / xz,   wz / xy.

Selfdualita vybírá právě jednu pravdivou dvojici z každého páru.
Každá z 2³ voleb je monotónní: nižší singletony jsou 0 a
vyšší trojice 1. Vybrané tři dvojice se po dvou protínají,
protože jediné disjunktní dvojice jsou komplementární páry.
Tři různé po dvou se protínající hrany jsou buď hvězda,
nebo trojúhelník: pro první dvě ab,ac má třetí bez a nutně
tvar bc, jinak má tvar ad. Jsou čtyři hvězdy a čtyři trojúhelníky.

Trojúhelník dává medián tří jeho vrcholů. Hvězda se středem w
má navíc minimální pravdivou trojici xyz a funkci

    wx OR wy OR wz OR xyz = M₅(w,w,x,y,z).

Při w=0 musí být x=y=z=1; při w=1 stačí jeden z x,y,z.
Tím jsou ověřeny všechny prime implikanty i opakovaný vstup
v mediánovém zápisu. Stejně platí ostatní tři středy.

Přesný seznam prime kvór odpovídající všem funkcím tabulky je:

| funkce v tabulce 2 | její kvóra |
|---|---|
| w, x, y, z | po jednom {w}, {x}, {y}, {z} |
| M(x,y,z) | xy, xz, yz |
| M(w,y,z) | wy, wz, yz |
| M(w,x,z) | wx, wz, xz |
| M(w,x,y) | wx, wy, xy |
| M₅(w,w,x,y,z) | wx, wy, wz, xyz |
| M₅(w,x,x,y,z) | wx, xy, xz, wyz |
| M₅(w,x,y,y,z) | wy, xy, yz, wxz |
| M₅(w,x,y,z,z) | wz, xz, yz, wxy |

V původní tabulce jsou právě tyto čtyři projekce, čtyři trojkové
mediány a čtyři zdvojené mediány, každý jednou mezi počátečním
w a sloupcem s_j. Počet 4+8=12 a úplnost seznamu tím mají
strukturální důkaz. To uzavírá přesně odkaz z úlohy 66.
**Hrany grafu, pořadí r_j/s_j a sedmibitové štítky se zde
nepovažují za ověřené**; patří k pozdějšímu auditu Algorithm H.

## Nulární rozsah a bibliografie

Společný doménový limit P0863 se rozšiřuje i na 65/66:
pro n=0 je jediná přípustná protínající se rodina i coterie
prázdná, přitom maximální/nedominovaná, ale žádná selfduální
nulární funkce neexistuje. Na všech n≥1 jsou důkazy výše úplné.
Implicitní n≥1 se zde neprohlašuje za vyřešenou terminologickou
konvenci; nevzniká nová karta ani další podobná položka.

Dne 2026-11-07 prohledány `all4a-pre`, `all4a`, `err4a`,
`all4f0`, `all4f1` podle stran 88/546, čísel 65/66 a témat
coterie/intersecting/Ibaraki/Kameda. Relevantní oprava nenalezena.
F0 p193/answer66 patří obvodům; all4a-pre p778/answer66
je jiná úloha o třech optimálních rozkladech.

[Lamportova autorská stránka](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/)
potvrzuje CACM21(7),1978,558–565.
[Ibarakiho autorský seznam, položka 128](https://web1.kcg.edu/~t_ibaraki/epubl.html)
potvrzuje Ibaraki–Kameda, IEEE TPDS4(7),1993,779–794.
[Primární článek Garcia-Molina–Barbará](https://www.cs.purdue.edu/homes/bb/cs542-11Spr/How%20to%20assign%20Votes-JACM-garcia-molina.pdf)
má uvedenou bibliografii JACM32(4),1985,841–860 a na p842
přisuzuje princip protínajících se skupin Lamportovi 1978.
Je uložen v `sources/garcia-molina-barbara-1985.pdf`; rozsah
čtení a meze jsou v `sources/coteries-primary-inputs.json`.

Celý Ibarakiho/Kamedův článek, přesná historická priorita,
samostatné použití v name servers a pozdější počty/algoritmy
v článku z roku 1985 se neprověřovaly. Vlastní matematické
důkazy výše na těchto vynechaných tvrzeních nezávisí.
