# Kromovy klauzule, komici a úlohy 7.1.1–53/54

Checkpoint X0086, P0795–P0812. Původní strany p60–62/file77–79
v sources/proof-krom-pages060-062.pdf, obrazy proof-krom-1/2/3.png.
Zadání53/54 p86/file103 a odpovědi p544/file561 v dřívějších
proof-file103/561.png. Bez matematického programu, řešiče nebo censu.
Hornova část p60 je přesně převzata z proof-049, nikoli znovu auditována.

## Přesný model rozpisu — P0795

A,B,C,D,E znamenají Aladdin, Bellagio, Caesars, Desert, Excalibur.
Každý komik musí vystoupit právě jednou v každém ze svých dvou hotelů,
ve dvou různých dovolených dnech. Má tedy právě dvě možnosti. Kladný
literál přiřadí první hotel prvnímu dni a druhý druhému; záporný pořadí
obrátí. Kompletní mapa z(37) je:

| komik / bit | hodnota1 | hodnota0 |
|---|---|---|
| Tomlin t | A1,C2 | C1,A2 |
| Unwin u | B1,E2 | E1,B2 |
| Vegas v | D2,E3 | E2,D3 |
| Williams w | A1,D3 | D1,A3 |
| Xie x | C1,E3 | E1,C3 |
| Yankovic y | B2,D3 | D2,B3 |
| Zany z | B1,C2 | C1,B2 |

Každá bitová volba už sama splňuje individuální smlouvy a zákaz
souběžných vystoupení téhož člověka. Jediná zbývající podmínka je,
aby žádná dvojice různých komiků nepoužila stejný hotel a den.
Proto je přesně zachycena zákazem každé dvojice odpovídajících literálů.
Nejde o ověřování skutečných historických smluv; je to zadaná modelová data.

## Všech 16 konfliktů, klauzule a 32 implikací — P0796

Pro zakázanou dvojici p,q platí ¬(p∧q)=¬p∨¬q, ekvivalentně
p⇒¬q a q⇒¬p. Následující tabulka je ve stejném pořadí jako(39)–(41):

| č. | hotel/den | zakázaná dvojice | implikace(40) | kontrapozice(41) |
|---|---|---|---|---|
|1|A1|t,w|t→¬w|w→¬t|
|2|B1|u,z|u→¬z|z→¬u|
|3|B2|¬u,y|¬u→¬y|y→u|
|4|B2|¬u,¬z|¬u→z|¬z→u|
|5|B2|y,¬z|y→z|¬z→¬y|
|6|C1|¬t,x|¬t→¬x|x→t|
|7|C1|¬t,¬z|¬t→z|¬z→t|
|8|C1|x,¬z|x→z|¬z→¬x|
|9|C2|t,z|t→¬z|z→¬t|
|10|D2|v,¬y|v→y|¬y→¬v|
|11|D3|¬v,w|¬v→¬w|w→v|
|12|D3|¬v,y|¬v→¬y|y→v|
|13|D3|w,y|w→¬y|y→¬w|
|14|E1|¬u,¬x|¬u→x|¬x→u|
|15|E2|u,¬v|u→v|¬v→¬u|
|16|E3|v,x|v→¬x|x→¬v|

Úplnost není odhad z počtu: A1 má2 možné účastníky, B1 má2,
B2 má3, C1 má3, C2 má2, D2 má2, D3 má3, E1/E2/E3 mají každý2.
Každá další hotelová buňka A2,A3,B3,C3,D1 má jediného účastníka.
Součet příslušných binomických počtů dvojic je
1+1+3+3+1+1+3+1+1+1=16. Tím není vynechán žádný konflikt.
Obě znaménka každé vytištěné klauzule a obě orientace implikace
souhlasí s tabulkou; každý řádek dává právě dva uvedené oblouky.

## Celý cyklus a nezbytnost změny jedné ze šesti smluv — P0797

Vytištěný cyklus(42) je

    u→¬z→¬y→¬v→¬u→z→¬t→¬x→u.

Jednotlivé hrany jsou postupně řádky 2,5,10,15,4,9,6,14
předchozí tabulky; popisky jsou B1,B2,D2,E2,B2,C2,C1,E1.
Cyklus obsahuje obě polarity u. Jestliže je jedna pravdivá,
implikace po cestě vynutí pravdivost druhé; při opačné hodnotě
začneme druhou polaritou. Žádné přiřazení jej tedy nesplňuje.

Používá pouze t,u,v,x,y,z. Když se žádná z jejich smluv nezmění,
všechny tyto zakázané dvojice zůstávají bez ohledu na Williamsovu
smlouvu. Změna alespoň jedné z vyjmenované šestice je proto nutná.
To není tvrzení, že každá libovolná změna jedné smlouvy postačí.

## Obrázek6: všech 22 hran a právě šest komponent — P0798

Vypuštění v odstraní přesně řádky10,11,12,15,16. Zůstane11 klauzulí
a22 různých uvedených oblouků. Při porovnání s původním obrázkem jsou
jejich konce i směry právě zbylé řádky tabulky. Lomené linky jsou
jednotlivé oblouky; geometrická křížení bez vrcholu nejsou incidencemi.

Dvě netriviální silné komponenty jsou

    C+={t,u,¬x,¬z},  C−={¬t,¬u,x,z}.

V C+ jsou cykly u→¬z→¬x→u a t→¬z→t; jejich společný vrchol
¬z dokládá vzájemnou dosažitelnost všech čtyř členů. V C− jsou
z→¬u→x→z a ¬t→z→¬t. Zbylé komponenty jsou singletony
{w},{y},{¬w},{¬y}. Kontrahovaný graf má přesně tyto sousednosti:

    w → C−, ¬y;
    y → C−, C+, ¬w;
    C− → C+, ¬y;
    C+ → ¬w, ¬y;
    ¬w a ¬y nemají následníky.

Pořadí (w,y), C−, C+, (¬w,¬y) je topologické. Žádné dvě
uvedené skupiny se tedy nemohou spojit do větší silné komponenty.
To dokazuje úplnost šesti tečkovaných obrysů, nejen jejich vnitřní cykly.
Žádná skupina neobsahuje literál spolu s komplementem.

## Tištěný rozpis bez Vegase — P0799

Při tuwxyz=110000 jsou pravdivé C+ a ¬w,¬y, ostatní komponenty
nepravdivé. Seznam sousedností nemá oblouk1→0; každá z11 klauzulí
je tedy splněna. Přímo ze smluv dostaneme:

| den | A | B | C | D | E |
|---|---|---|---|---|---|
|1|t|u|z|w|x|
|2|—|z|t|y|u|
|3|w|y|x|—|—|

Každý z šesti komiků se vyskytuje právě ve dvou správných dnech
 a hotelech. První řádek je přesně výčet na začátku p62.

## Úloha53(a): obě uvedené změny Tomlin — P0800

Nejprve ponecháme původní smlouvy ostatních šesti. Jejich platný rozpis:

| den | A | B | C | D | E |
|---|---|---|---|---|---|
|1|—|z|x|w|u|
|2|—|u|z|y|v|
|3|w|y|—|v|x|

Odpovídá u=0,v=0,w=0,x=1,y=0,z=1; přímo podle P0795 má každý
správné dva hotely a dny. Při změně dne1→3 přidáme t do A2,C3.
Při změně dne2→3 přidáme t do A1,C3. Všechny tyto buňky jsou
prázdné a obě dvojice používají A,C v nových dovolených dnech.

## Úloha53(b): uvedená změna Unwin — P0801

Ostatní komici mohou mít t=1,v=0,w=0,x=0,y=0,z=0:

| den | A | B | C | D | E |
|---|---|---|---|---|---|
|1|t|—|z|w|x|
|2|—|z|t|y|v|
|3|w|y|x|v|—|

Změna Unwinova dne2→3 dovolí vložit u do B1,E3. Obě buňky
jsou volné a ostatní smlouvy se nezmění. Odpověď uvádí příklad,
ne úplný seznam všech možných renegociací; žádný takový census netvrdíme.

## Úloha53(c): obě uvedené změny Vegas — P0802

Použijeme přesně rozpis P0799. Při změně Desert→Aladdin vložíme
v do A2,E3. Při změně Excalibur→Aladdin vložíme v do A2,D3.
Všechny tři dotčené buňky jsou prázdné; dny2,3 zůstávají správně.
To je přesný vztah k obrázku6, nikoli pouze samotné vypuštění Vegase.

## Úloha53(d): obě uvedené změny Xie — P0803

Ostatní komici mohou mít t=0,u=0,v=0,w=0,y=0,z=1:

| den | A | B | C | D | E |
|---|---|---|---|---|---|
|1|—|z|t|w|u|
|2|t|u|z|y|v|
|3|w|y|—|v|—|

Při změně Caesars→Aladdin vložíme x do A1,E3; při změně
Excalibur→Aladdin do A1,C3. Obě verze mají dny1,3, správné
nové hotely a žádný konflikt. Pět ostatních párů a Williamsův
pár ověřuje přímo tabulka P0795.

## Úloha53(e): obě uvedené změny Yankovic — P0804

Ostatní komici mohou mít t=1,u=1,v=1,w=0,x=0,z=0:

| den | A | B | C | D | E |
|---|---|---|---|---|---|
|1|t|u|z|w|x|
|2|—|z|t|v|u|
|3|w|—|x|—|v|

Při změně Bellagio→Aladdin vložíme y do A2,D3; při změně
Desert→Aladdin do A2,B3. Všechny buňky jsou volné a dny2,3
se zachovají. Ostatních šest původních smluv je opět přímo splněno.

## Úloha53(f): uvedená změna Zany — P0805

Ostatní komici mohou mít t=1,u=1,v=1,w=0,x=0,y=1:

| den | A | B | C | D | E |
|---|---|---|---|---|---|
|1|t|u|—|w|x|
|2|—|y|t|v|u|
|3|w|—|x|y|v|

Změna Zanyho dne2→3 dovolí vložit z do C1,B3. Zůstávají
hotely B,C a ostatní původní smlouvy. To dokládá konkrétní
příklad v odpovědi, bez tvrzení o úplném seznamu změn.

## Dodatek o Williamsovi — P0806

P0797 již dokázala, že žádná změna pouze w nemůže odstranit
nesplnitelnost zbývajících šesti smluv. Slova o jeho neúčasti
na konfliktu mají právě tento význam. Williams přitom může
v(38) kolidovat s jinými komiky; netvrdíme, že se nevyskytuje
v žádné podmínce nebo že libovolný jeho rozpis je vždy slučitelný.

## Obecný implikační graf a doména — P0807

Pro n proměnných vytvoříme2n literálových vrcholů. Každá
klauzule u∨v dává ¬u→v a ¬v→u. Je splněna právě tehdy,
když žádný z těchto oblouků nejde z pravdy do nepravdy.
Každá orientovaná cesta proto vynucuje implikaci svých konců;
ve stejné silné komponentě musí mít všechny literály stejnou hodnotu.

Kromovy klauzule z p57 obsahují právě dva, ne nutně různé literály
(P0722). Unit u lze psát u∨u: dvě stejné hrany představují tentýž
požadavek. Tautologie u∨¬u dává smyčky. Počet2m je počet
vložených obloukových záznamů; po sloučení duplicit může být
různých oblouků méně. Žádný argument unikátnost hran nepotřebuje.
Prázdná konjunkce je pravdivá a graf bez hran to správně zachytí.
Prázdná klauzule do této dvouliterálové syntaxe nepatří; pokud ji
obecné vstupní rozhraní připouští, odmítne se ihned jako UNSAT.

Komplementace obrací každou hranu a tedy i každou cestu:
(u→v) právě tehdy, když (¬v→¬u). Proto komplementy členů
silné komponenty S tvoří přesně jednu celou komponentu ¬S:
vzájemná dosažitelnost dává inkluzi a komplementace zpět vyloučí,
že by se do výsledné komponenty dostal nějaký další vrchol.

## Theorem K: obě implikace a úplný invariant konstrukce — P0808

Obsahuje-li jedna komponenta x i ¬x, vzájemná dosažitelnost
nutí stejnou hodnotu komplementů, což je nemožné.

Naopak předpokládejme, že se to nestává. Kondenzace konečného
digrafu je DAG: cyklus různých komponent by je spojil do jediné.
Každý neprázdný konečný DAG má zdroj, protože sledování předchůdců
jinak opakuje vrchol a vytváří cyklus. Zvolme zdrojovou komponentu S.
Její komplement ¬S je díky obracení hran koncová komponenta a ¬S≠S.
Přiřaďme S hodnotu0 a ¬S hodnotu1 a oba celky odstraňme.

Žádná hrana této dvojice se zbytkem nemůže porušit implikaci:
do zdroje S žádná nevstupuje; ze S=0 jsou všechny implikace splněny;
ze sinku ¬S žádná nevychází; do ¬S=1 jsou všechny splněny.
Uvnitř komponent jsou hodnoty stejné; mezi nimi může být pouze
směr S→¬S, protože opačný odporuje zdrojové/koncové vlastnosti.

Zbylý indukovaný graf je uzavřený na komplementaci. Odstranění
celých komponent neporuší vzájemnou dosažitelnost ve zbývajících:
cesta mezi dvěma členy jedné SCC nemůže projít jinou SCC, jinak
by se sloučily. Zbývající SCC tedy stále tvoří disjunktní dvojice
S,¬S a žádná neobsahuje oba komplementy. Invariant se opakuje,
v každém kroku ubude alespoň dvojice komponent, takže konstrukce
skončí a dá konzistentní hodnotu všem proměnným. Všechny hrany
jsou splněny a P0807 pak dokazuje všechny klauzule. Platí i n=m=0.

Tento existenční důkaz sám netvrdí lineární cenu opakovaného
vyhledávání zdrojů. Konkrétní lineární řešení je uvedeno níže.

## Úloha54: jediný vybraný komplement stačí — P0809

Nechť neprázdná SCC S obsahuje x,¬x a libovolné u∈S. Existují
cesty x→u a u→x. Jejich kontrapozice dávají ¬u→¬x a ¬x→¬u.
Protože ¬x∈S, je také ¬u∈S. Pro u=u1 je tedy jeho komplement
v témže S; není u1, protože literal a jeho negace jsou různé vrcholy.
Obrácená implikace je okamžitá: pokud S obsahuje u1 a ¬u1,
obsahuje požadovaný pár. Pro singleton je obojí nepravdivé.

Původní odpověď používá navíc cesty x↔¬x, což je rovněž platné.
Známá náhrada z9.12.2015 má kratší argument právě ve výše uvedeném
tvaru; původní i opravená verze jsou správné. Žádný nový nález.

## Explicitní externí vstup: Tarjanovy SCC — P0810

Použitý primární článek je R. Tarjan, SIAM Journal on Computing1
(1972),146–160, DOI10.1137/0201010. Již existuje read-only v
workstreams/vol1/parallel/oriented-trees/sources/tarjan-1972.pdf
(URL https://www.cs.cmu.edu/~cdm/resources/Tarjan1972-sccs.pdf).
Pro tento blok přečten §4 a původní p157–159, vlastní obrazy
images/tarjan-scc-12/13/14.png. Theorem13 uvádí čas a paměť
O(V+E); Theorem14 správnost na libovolném orientovaném grafu.
Používá seznamy následníků, DFS čísla/lowlink, zásobník dosud
nepřiřazených vrcholů a booleovské on-stack pole.

Přijímáme právě tento standardní externí výsledek o SCC. Nespoléháme
na dřívější V1 důkaz o explicitní délce cyklové báze, který má jiný rozsah,
a netvrdíme novou úplnou rekonstrukci Tarjanovy indukce. Pro naši aplikaci
je graf konečný, reprezentovaný sousednostmi a má2n vrcholů a2m
záznamů hran. Smyčky a duplicity nic nemění: jsou jen dalšími
konstantně zpracovanými sousednostmi.

Z primárního programu je zároveň patrná cena: každý vrchol se čísluje,
vkládá na zásobník a odebírá nejvýše jednou, každá sousednost je
prohlédnuta jednou, on-stack test má konstantní cenu. Tento aplikační
součet nevyžaduje spouštění programu ani nový benchmark.

## Pořadí komponent, přiřazení a celkové náklady — P0811

Tarjanův program odebírá sinky nejdříve. Pro hranu mezi různými
komponentami C→D je D odebrána dříve než C: při zpracování hrany
je D buď již dokončena, nebo ji DFS navštíví před návratem z C.
V druhém případě nemůže zůstat svázána s aktivní C, protože
zpáteční cesta by znamenala C=D; podle správnosti SCC výstupu je
tedy samostatně odebrána před C. Tato vlastnost platí i mezi různými
kořeny DFS: z již dokončené oblasti by nebyla neprozkoumaná dosažitelná D.

Očíslujme SCC vzestupně podle výstupu r(C). Pro různé komponenty
C→D máme r(C)>r(D); pro libovolnou hranu u→v tedy
r(Cu)≥r(Cv). Je-li formule SAT, nastavme

    u=1 právě tehdy, když r(Cu)<r(C¬u).

To přesně odpovídá knize: první nalezené komponentě z každé
komplementární dvojice dát1 a její druhé komponentě0. Neznamená
to při pozdějším zpracování znovu přepsat již přiřazenou proměnnou.

Kdyby hrana u→v měla u=1,v=0, pak její kontrapozice dává

    r(Cu) ≥ r(Cv) > r(C¬v) ≥ r(C¬u) > r(Cu),

spor. Přiřazení tedy splňuje všechny implikace i klauzule.

Sestavení grafu stojí O(n+m), SCC podle P0810 také O(n+m).
Uložení ID komponenty každému literálu a test ID(x)=ID(¬x) pro
každou proměnnou stojí O(n). Alternativní test P0809 dovolí po
odebrání celé komponenty vyzkoušet komplement jejího prvního literálu;
nejprve musí být označeni všichni její členové. Přiřazení podle r stojí
O(n). Celkem čas i uložený graf a pracovní paměť O(n+m), s O(n)
pomocnou pamětí nad vstupními seznamy. Nulové počty a izolované
proměnné jsou pokryty; neúčtujeme výstup n bitů za konstantní čas.
Tím je zbývající Kromova část P0729 uzavřena.

## Poslední odstavec p62: medián a obě formy(43) — P0812

Pro tři booleovské hodnoty je prostřední uspořádaná hodnota1 právě
při alespoň dvou jedničkách. Výraz xy∨yz∨zx říká právě to.
Výraz (x∨y)(y∨z)(z∨x) je1 právě tehdy, když neexistuje dvojice
nul; pro tři bity to opět znamená alespoň dvě jedničky. Tím jsou
obě vytištěné formy i název medián ověřeny pro všechny počty
jedniček0,1,2,3. Následující vlastnosti na p63 se zde nepřebírají.

## Errata, bibliografie a přesné celostránkové pokrytí

7.11.2026 prověřeny all4a-pre, all4a, err4a, all4f0, err4f0 podle
p60–62,p86,p544 a témat Krom/Tarjan/53/54, nejen samotných čísel.
Známé změny C z2016/2022/2023 a p60 jméno Scutellà jsou převzaty
z proof-049 a errat. Změna odkazu p62 z7.4.1 na7.4.1.2 je známá.
F0 má úpravu zakončení(42), bibliografie Hornových algoritmů a roku
SGB; z aktuální původní sazby byl ověřen celý cyklus s negacemi.
Náhrada odpovědi54 z2015 je přečtena i v původním erratu p22.
Žádná z těchto známých úprav není vlastní karta nebo červená stránka.

Primární Wiley záznam potvrzuje Krom1967, svazek13, strany15–20
(https://onlinelibrary.wiley.com/doi/10.1002/malq.19670130104).
Přesné číslování Corollary2.2 nebylo z úplného článku ověřeno:
prohlížeč poskytl bibliografii, nikoli plný text. Jde o bibliografickou
výjimku; Theorem K má zde úplný vlastní důkaz. Tarjan je výslovný
primární externí vstup výše. Strany512–519 SGB a historické autorství
všech dílčích formulací se nově nezávisle nereprodukovaly.

Úplná obsahová mapa dovoluje nově review_depth: argument pro:

* **p60/file77:** pokračování C, srovnání s topologickým tříděním a
  Horn SAT přesně P0737–P0745/proof-049; Kromův lineární příslib
  P0807–P0811; všechna modelová data(37) a jejich bitový význam P0795.
  Bibliografické výjimky zůstávají zvlášť.
* **p61/file78:** všechny(38)–(42) P0796/P0797, celý obrázek6,
  počet odstraněných klauzulí/hran i všechny komponenty P0798,
  bezkonfliktní význam přiřazení P0799/P0808.
* **p62/file79:** konkrétní rozpis P0799, všechny obecné grafové
  definice/důsledky P0807, oba směry Theorem K P0808, celý aplikační
  SCC algoritmus s výslovným externím vstupem P0810/P0811,
  související test54 P0809 a obě mediánové formy P0812.

P86/file103 a p544/file561 zůstávají partial: herní mezery52 a
pokračování55 nejsou vyřešeny těmito důkazy. Dále main p63/file80,
úloha55; dřívější přesné mezery včetně P0768/P0794 zůstávají otevřené.
