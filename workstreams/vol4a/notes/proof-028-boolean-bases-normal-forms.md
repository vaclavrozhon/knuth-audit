# §7.1.1: operace, identity a normální formy, p47–53

6. listopadu 2026, X0058. Originály images/file064.png až file070.png
přečteny znovu; OCR je pouze navigace. Každá níže identifikovaná položka
má argument. Úlohy a dodatky jejich odpovědí se vedou samostatně.

Doména v celém bloku je B={0,1}; n je nezáporné celé číslo. Značíme
¬x=1−x, x∧y=xy, x∨y=max(x,y) a x⊕y=(x+y) mod 2. Symbol ≡ zde
znamená binární booleovskou ekvivalenci, nikoli rovnost výrazů.

## P0508–P0513: počet a celá Table 1

**P0508, p47:** vstupy 00,01,10,11 jsou čtyři různé uspořádané dvojice.
Volba každého výstupu je nezávislá, tedy existuje přesně 2⁴=16 funkcí.
Vektor výstupů určuje funkci jednoznačně a každý čtyřbitový vektor
takové funkci přísluší. První bit patří 00, poslední 11.

**P0509, p48:** pro disjunktní booleovské hodnoty xy=0 je x+y také
bit a rovná se x∨y. Bez disjunktnosti platí
x+(1−x)y=x+y−xy=x∨y: pro x=0 dostáváme y, pro x=1 hodnotu 1.
Idempotence Jevonsova plusu je max(x,x)=x; neplatí pro obyčejné
celočíselné sčítání při x=1. Historické používání symbolů tímto
matematickým ověřením není nezávisle potvrzeno.

**P0510, (1), p48:** při z=0 jsou obě strany (x∨y)∧z a
(x∧z)∨(y∧z) nula; při z=1 jsou obě x∨y.

**P0511, (2), p48:** při z=0 jsou obě strany (x∧y)∨z a
(x∨z)∧(y∨z) rovny x∧y; při z=1 jsou obě 1.

**P0512, Table 1, p49:** tabulka při pořadí 00,01,10,11 ověřuje
všech šestnáct řádků. Vpravo je obyčejná celočíselná aritmetika;
všechny hodnoty uvedených výrazů na B² jsou 0 nebo 1.

| výstupy | logická funkce | aritmetický výraz |
|---|---|---|
| 0000 | false | 0 |
| 0001 | x∧y | xy |
| 0010 | x∧¬y | x(1−y) |
| 0011 | levá projekce | x |
| 0100 | ¬x∧y | (1−x)y |
| 0101 | pravá projekce | y |
| 0110 | xor | x+y−2xy |
| 0111 | or | x+y−xy |
| 1000 | nor | (1−x)(1−y) |
| 1001 | equivalence | 1−x−y+2xy |
| 1010 | ¬y | 1−y |
| 1011 | y⇒x | 1−y+xy |
| 1100 | ¬x | 1−x |
| 1101 | x⇒y | 1−x+xy |
| 1110 | nand | 1−xy |
| 1111 | true | 1 |

Nerovnosti v tabulce odpovídají [x>y], [x<y], [x≥y], [x≤y].
První dva mají saturující rozdíl max(x−y,0), resp. max(y−x,0).
Při obvyklé zde použité konvenci 0⁰=1 dávají xʸ a yˣ právě řádky
1011 a 1101: exponent 0 vrací 1 a exponent 1 základ. Nejde o
obyčejný záporný rozdíl, který OCR někdy naznačuje. Implikace je
zejména pravdivá při x=y=0, jak říká text. Symbolické vzorky za
tabulkou jsou přímo jejími řádky.

**P0513, p49:** dvě funkce jsou konstantní; nekonstantní funkce
závislé pouze na jednom vstupu jsou x,¬x,y,¬y. Jedinou jedničku
mají čtyři součiny x∧y, x∧¬y, ¬x∧y, ¬x∧¬y; jejich komplementy
mají tři jedničky a jsou příslušnými disjunkcemi literálů. Zbývají
xor a equivalence. Tím jsou doložena všechna tvrzení o tomto rozdělení.

## P0514–P0525: základní identity a úplnost NAND/NOR

**P0514, p50:** položme N(a,b)=¬(a∧b). Pak ¬a=N(a,a),
a∧b=N(N(a,b),N(a,b)) a a∨b=N(N(a,a),N(b,b)).
Konstantu 1 dá N(x,N(x,x)), nulu její NAND se sebou. Všech šestnáct
funkcí je tedy vyjádřitelných, například OR svých mintermů.
Pro R(a,b)=¬(a∨b) obdobně ¬a=R(a,a), a∨b=R(R(a,b),R(a,b)),
a∧b=R(R(a,a),R(b,b)); R(x,R(x,x))=0 a jeho NOR se sebou je 1.
To dokazuje úplnost obou operací bez vstupních konstant.
**Neříká to, že tyto formule jsou nejkratší**; to požaduje úloha 4.

**P0515, (3)–(4), p50:** nad F₂ jsou ¬x=1+x, xor x+y a ekvivalence
1+x+y. Negace právě jednoho vstupu zamění xor a ekvivalenci, což
dává všechny rovnosti (3). Také
0≡x≡y=(1+0+x)≡y=1+(1+x)+y=x+y, tedy (4).
Ekvivalence je asociativní, protože obě uzávorkování tří vstupů
dají x+y+z; xor také. Plusy v tomto argumentu jsou modulo 2.

**P0516, (5), p50:** dvě stejné vstupní hodnoty dávají xor 0, různé
dávají 1, tedy xor=(x+y) mod 2. And je součin. Redukce celočíselných
součtů/součinů modulo 2 zachovává asociativitu, komutativitu a
distributivitu; neutrály jsou 0 a 1, každý prvek je svým opačným
a jediný nenulový prvek 1 je svým inverzním. Tím je ověřeno pole
dvou prvků, nejen tabulka sčítání.

**P0517, p50:** ∧ a ∨ jsou minimum a maximum na lineárně uspořádané
dvouprvkové množině. Obě uzávorkování tří prvků vyberou tentýž
nejmenší/největší prvek a pořadí nehraje roli. Xor má obě vlastnosti
z předchozí redukce součtu modulo 2.

**P0518, (6), p50:** z(x+y)=zx+zy v F₂. Také přímo: z=0 dává
na obou stranách nulu, z=1 dává na obou stranách x⊕y.

**P0519, (7), p50:** min(x,y)≤x≤max(x,y), tedy
max(min(x,y),x)=min(max(x,y),x)=x.

**P0520, (8)–(10), p50:** x+x=0 v F₂ dává (8). Asociativita a
komutativita dávají (x⊕y)⊕x=y a (x⊕y)⊕y=x, tedy (9).
Neutrálnost nuly je x+0=x. Obě hodnoty x=0,1 dávají ¬x=x⊕1,
tedy (10). Obnova druhého vstupu z xor a prvního je právě (9).

**P0521, (11), p51:** ¬(x∧y)=1 právě tehdy, není-li x=y=1,
tj. je-li alespoň jedna z ¬x,¬y jednička. To je ¬x∨¬y.

**P0522, (12), p51:** ¬(x∨y)=1 právě tehdy, když x=y=0,
tj. právě když ¬x∧¬y=1. U obou zákonů ekvivalence jedniček
ověřuje celé funkce, protože jejich hodnoty jsou bity.

**P0523, (13), p51:** první rovnost x∧y=¬(¬x∨¬y) je (12)
s komplementovanými vstupy. Z celočíselného x∨y=x+y−xy po redukci
modulo 2 plyne x⊕y⊕(x∨y)=xy, tedy druhá rovnost.

**P0524, (14), p51:** první rovnost je obdobně (11); přesunutí xy
v předchozí rovnosti nad F₂ dává x∨y=x⊕y⊕(x∧y).

**P0525, (15), p51:** (x∨y)∧¬(x∧y) znamená alespoň jednu a ne obě
jedničky, tedy xor. Disjunktní případy x=1,y=0 a x=0,y=1 dávají
přesně (x∧¬y)∨(¬x∧y). Pruhy negací byly čteny z originálu.

**P0526, p51: partial.** Text tvrdí dolní mez 4(n−1) kroků výpočtu
parity pomocí ∧,∨,¬ a odkazuje na §7.1.2–77. Identity výše dávají
pouze horní konstrukci: binární xor realizuje (x∨y)∧¬(x∧y) ve čtyřech
krocích, dohromady 4(n−1). Horní konstrukce nedokazuje minimum.
Přesný model kroků, sdílení mezivýsledků a dolní důkaz se prověří
s odkazovanou úlohou/odpovědí. n=1 má triviální nulu kroků; n=0
není tento výrok o xor zadaných proměnných zamýšlen. Žádný nález.

## P0527–P0532: úplná multilineární reprezentace

**P0527, p51:** Bⁿ má 2ⁿ vektorů, při n=0 jediný prázdný vektor.
Lexikografická posloupnost vypíše každý právě jednou; poslední
souřadnice se mění nejrychleji. Funkce je tedy určena 2ⁿ bity,
včetně osmi pro n=3. Důsledkem je 2^(2ⁿ) funkcí, při n=0 dvě.

**P0528, (16)–(17), p51:** označ f₀(u)=f(u,0), f₁(u)=f(u,1).
Při posledním vstupu 0 je g⊕h·0=g, tedy g musí být f₀.
Při vstupu 1 musí být g⊕h=f₁, tedy h=f₀⊕f₁. Tyto nutné volby
také postačují. Rozklad je správný i jednoznačný pro každé n>0;
při n=1 jsou g,h nulární, nikoli chybějící.

**P0529, p51–52:** každé rozvinutí sníží aritu obou podúloh o jednu.
Po právě n úrovních skončí úplný binární strom s 2ⁿ listy, každý
nulární konstanta. Vnitřní uzly stále obsahují proměnné x₁,…,xₙ.
To poslední doplňuje známé erratum p52 z 11. 2. 2012. Počet listů
není časově optimální algoritmus ani počet různých hodnot konstant.

**P0530, (18), p52:** xy při y=0 je 0, při y=1 je x; x⊕0=x.
Po distributivním rozepsání do různých čtvercově volných monomů
a vyrušení stejných členů se nulové koeficienty odstraní. Nenulový
výsledek nepotřebuje explicitní konstantu 0; nulový lze reprezentovat
právě jí. Každý neprázdný monom mizí na nulovém vektoru, proto
samostatný člen 1 zůstane právě tehdy, když f(0,…,0)=1.
Jde o tuto zjednodušenou reprezentaci, nikoli zákaz redundantních formulí.

**P0531, příklad (19), p52:** první vnější větev je
(1⊕0·x)⊕(0⊕1·x)y=1⊕xy; druhá je
(0⊕1·x)⊕(1⊕1·x)y=x⊕y⊕xy. Výsledek tedy je
1⊕xy⊕xz⊕yz⊕xyz, přesně vytištěný polynom modulo 2.
Nikde nevzniká druhá mocnina proměnné. Jeho pravdivostní tabulka
je 11101001; nejde o jiný, čtyřproměnný příklad (22).

**P0532, p52:** indukcí podle n mají f₀ a f₀⊕f₁ jediný součet
různých monomů v prvních n−1 proměnných. Rozklad každého
multilineárního polynomu P(u,xₙ)=G(u)+xₙH(u) je jednoznačný:
G=P(u,0), H=P(u,0)+P(u,1). Pro n=0 je koeficient hodnotou funkce.
To dokazuje existenci i jednoznačnost pro všechna n, nikoli jen
počet výrazů. Monomy jsou v bijekci s podmnožinami {1,…,n}, tedy
jich je 2ⁿ; prázdná podmnožina dává člen 1.

## P0533–P0539: Booleův rozklad, DNF a CNF

**P0533, (20)–(21), p52:** (f₀(u)∧¬xₙ)∨(f₁(u)∧xₙ)
se při xₙ=0 rovná f₀(u), při xₙ=1 f₁(u). Obě větve nemohou být
současně 1. Rozklad je přesný i pro konstantní funkce.

**P0534, p52:** opakování rozkladu přiřadí každému a∈Bⁿ právě
minterm m_a, jehož j-tý literál je x_j při a_j=1 a ¬x_j při a_j=0,
s koeficientem f(a). Indukční krok rozděluje vektory podle posledního
bitu na disjunktní skupiny; nic nevynechá ani nepřidá. Term m_a
je pravdivý právě na a. OR těch s koeficientem 1 je proto přesně f.
Vytištěný příklad x₁∧¬x₂∧¬x₃∧x₄∧x₅ určuje jediný vektor 10011.

**P0535, (22)–(23), p52:** jedničky 1100100100001111 jsou
0000,0001,0100,0111,1100,1101,1110,1111. Pruhy osmi vytištěných
termů (23) dávají v uvedeném pořadí právě tyto vektory. Žádné dva
nejsou zároveň pravdivé; výsledek má přesně uvedených osm jedniček.

**P0536, p53:** v normalizované úplné DNF bez opakování musí být
m_a přítomen právě tehdy, když f(a)=1, protože jiný minterm na a
nepřispěje. To dokazuje jedinečnost až na pořadí; syntaktické
duplicity se odstraní idempotencí. Prázdné OR je 0 a prázdné AND
je 1, aby zůstaly neutrály spojování bloků. Pro n=0 je jediným
mintermem prázdné AND=1: nulová funkce jej vynechá, jednička jej
použije. Nulární okraj je pokryt.

**P0537, (24), p53:** minclause c_a má j-tý literál x_j při a_j=0
a ¬x_j při a_j=1. Je 0 právě na a, takže AND všech c_a s f(a)=0
je přesně f. Každý nulový bod si vynucuje právě svoji klauzuli.
U (22) jsou tyto body 0010,0011,0101,0110,1000,1001,1010,1011;
osmi klauzulím (24) odpovídají v tomto pořadí všechny pruhy negací.
Konstanta 1 má prázdné AND, nula všechny minclauses; při n=0
má nulová funkce jedinou klauzuli, prázdné OR=0.

**P0538, (25)–(26), p53:** každý člen má vlastní počet literálů
s_j; rozvinuté závorky odpovídají j=1,…,m a k=1,…,s_j.
U_jk je x_i nebo ¬x_i. DNF je OR takových AND, CNF duálně.
Nevyžaduje se úplnost všech proměnných, disjunktnost členů ani
odlišnost literálů. Prázdné případy upravuje P0536; rozporný člen
lze zahodit a tautologickou klauzuli vynechat. Podmíněné tvrzení,
že PLA s OR součinových členů realizuje DNF, je tato definice;
četnost hardwarového použití, rychlost a cena se zde neověřují.

**P0539, konec p53:** pro f=T∨U hodnota T=1 nutí f=1, tedy každý
term DNF je implikant. V příkladu
f=(x∧¬y∧z)∨(y∧z)∨(¬x∧y∧¬z) první term určuje (1,0,1),
kde je f opravdu 1. Rozšíření příkladu a prvoimplikanty pokračují
na p54; jsou samostatným dalším blokem.

## Rozsah, známé opravy a pokračování

Relevantní pasáže všech pěti vrstev errata/text/all4a-pre.txt,
all4a.txt, err4a.txt, all4f0.txt a err4f0.txt prověřeny. Zohledněno
zpřesnění disjunktních množin p48, tři historické symboly a
„and not; but not“ Table 1, přidání proměnných p52 a historické
názvy projekcí/exclusive normal form již přítomné v první 4A.
Posunutí sazby tabulky a Looking-Glass jsou známé drobnosti;
nevytvářejí nálezy ani karty.

Citace, autorství a historické priority Boole, Jevons, Peirce,
Sheffer, De Morgan, Ockham, Burley, Zhegalkin, Bernays a úvodní
motta se zde nezávisle nerevalidují. Technologické poznámky o
tehdejších počítačích/PLA nejsou číselnou nákladovou větou.
P0526 je otevřený matematický odhad, nikoli bibliografická výjimka.
Žádný matematický program, nový nález ani hromadné celostránkové
uzavření. Dále jednotlivé úlohy od 1 a hlavní text p54; čtecí náskok p218.

## Doplnění X0059: implementační vstup a úplná stránková mapa

**P0555, p49:** primární [MIT 6.884, přednáška 3 z roku 2005](https://ocw.mit.edu/courses/6-884-complex-digital-systems-spring-2005/5db68ba6abd100ecc232604ccfeb9f46_l03_cmos_gates.pdf),
snímky 15–18, dokládá použitý ideální spínačový model i NAND/NOR
zapojení. Lokální zdroj sources/mit-6884-2005-cmos-gates.pdf má metadata;
obě schémata byla zobrazena. Dva sériové n-spínače vedou k zemi
právě při x=y=1, paralelní p-spínače k napájení právě jinak: NAND.
Paralelní n a sériové p realizují NOR. V každém stabilním binárním
případu vede právě jedna větev, výstup není plovoucí ani zkratovaný.
To podporuje konkrétní tvrzení o jednoduché tranzistorové realizaci;
neověřuje rychlost, cenu ani kompletní fyziku zařízení.

**P0556, p47:** konečnou abecedu m symbolů lze injektivně očíslovat
0,…,m−1 a každý index zapsat pevnými ⌈log₂ m⌉ bity (pro m=1 stačí
prázdné slovo). Konkatenace pevných bloků zachová rozlišitelnost zpráv;
případnou délku lze připojit samostatně. Konečná relace má bitovou
incidenční tabulku a konečný algoritmický zápis je opět řetězec nad
konečnou abecedou. Tak je doložena schopnost bitů kódovat informace,
relace i popisy algoritmů. Text nestanoví univerzální mez zrychlení
všech binárních strojů vůči všem desetinným. Historické údaje o
obvyklé architektuře a relativní četnosti použití instrukcí jsou
výslovnou bibliografickou výjimkou, ne novou nákladovou větou.

Po dokončení všech částí úloh 1–4 v proof-029 je úplný rozpis následující.
Četnost položek sama není důvodem k uzavření; tabulka pokrývá i odstavce
mimo číslované rovnosti a konkrétní příklady.

| p / file | celý matematický obsah a přesný argument | celostránkový stav |
|---|---|---|
| 47 / 64 | Kódovací schopnost bitů P0556; šestnáct funkcí a pořadí pravdivostních tabulek P0508. Zbytek je motivační/historický komentář bez kvantifikované nákladové meze. | argument; historické výjimky zvlášť |
| 48 / 65 | Disjunktní sčítání, obecný OR výraz a idempotence P0509; obě distributivity P0510/P0511; logický smysl citátu úlohou 1/P0540. | argument; historické atribuce zvlášť |
| 49 / 66 | Všech šestnáct řádků, vzorce/notace, implikace na 00 a následné ukázky P0512; všechny skupiny operací P0513; tranzistorový význam P0555. | argument; historické názvy a priority zvlášť |
| 50 / 67 | NAND/NOR úplnost P0514 a konkrétní/optimální NAND výrazy P0549–P0554; ekvivalence/XOR P0515; pole P0516; asociativita/komutativita a všechny (6)–(10) P0517–P0520. Praktická užitečnost je motivace, nikoli měřená četnost. | argument; historické atribuce zvlášť |
| 51 / 68 | P0521–P0529 pokrývají každou identitu, počet vstupů i rozklad; **P0526 dolní mez parity zůstává otevřená**. | partial |
| 52 / 69 | Strom/konstanty/známá oprava P0529/P0530, konkrétní celý výpočet P0531, existence/jednoznačnost P0532, druhý rozklad P0533, mintermy P0534 a všechny členy příkladu P0535. | argument; historické atribuce zvlášť |
| 53 / 70 | P0536–P0539 pokrývají zdejší vzorce; rozpracovaný implikantový příklad pokračuje na p54 a související jednotlivé úlohy ještě nejsou uzavřené. | partial |
| 534 / 551 | §7–145 a dodatek nad n/k: převzaté P0491–P0493/proof-018; §7.1.1–1 až 4 včetně všech dodatků, minim a algoritmu: P0540–P0554/proof-029. | argument; bibliografie zvlášť |

Bibliografické výjimky u p47–50/p52: motta a historické údaje,
Boole/Jevons/Peirce/Philo/Galen/Bochenski/Sheffer, původ symbolů,
historická běžnost architektur a kvalitativní komentáře o praktické
užitečnosti. U p534: Carroll/Sartena/Sheffer a staré citace algoritmu
majority/Misra–Gries/pozdější Alonso–Reingold; vlastní matematický
obsah těchto odpovědí má uvedené argumenty. P51 a p53 se nepovyšují.
