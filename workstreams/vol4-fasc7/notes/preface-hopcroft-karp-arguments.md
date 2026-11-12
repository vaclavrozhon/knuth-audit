# Předmluva ix–xi: jednotlivé argumenty pro Algorithm H

6. listopadu 2026. První digitální vydání, březen 2025, file 10–12.
Zobrazeny celé originály; přepis OCR zvlášť ztrácí `≠`, čárky q′/g′
a znaménka. Níže se respektují známé opravy pole MARK (včetně indexu 0)
a STACK→BOY, s indexy 1,…,min(M,N), ze 4. září 2026. Nejsou to nálezy.
F7-C0001 je přebrán přesným odkazem na `notes/F7-C0001.md`, bez opakování.

Rychle dostupný autorův primární [prefascicle 14a](https://www-cs-faculty.stanford.edu/~knuth/fasc14a.pdf)
z 18. září 2026 je uložen v `sources/fasc14a-2026-11-06.pdf` a `.txt`;
provenance je v `sources/preface-primary-manifest.json`. Jeho odpověď 7
výslovně popisuje inicializaci IQUEUE, kterou reprezentace v předmluvě
již požaduje. Důkazy níže jsou vlastní a pokrývají i pomocné kroky
vynechané v krátké předmluvě. Cizí úlohy 7.5.1 se tím neprohlašují
za samostatně zkontrolovanou součást celého dalšího svazku.

## H-P01. Párování, augmentace a nutnost augmentující cesty

Vstup je konečný bipartitní graf s částmi G a B o velikostech M,N.
Pole GMATE a BMATE reprezentují párování: nenulová hodnota jednoho
určuje souhlasnou nenulovou hodnotu druhého, hrana je ve vstupu a každý
vrchol má nejvýše jednoho partnera. Alternující cesta mezi dvěma volnými
vrcholy, jejíž první a poslední hrana nejsou v párování, má lichou délku.
Záměnou členství jejích hran se všechny vnitřní vrcholy stále párují
právě jednou, oba konce nově jednou a velikost se zvětší přesně o 1.

Pro párování P a Q má každý vrchol v symetrické diferenci stupeň ≤2.
Její netriviální komponenty jsou alternující cesty a sudé cykly.
Cyklus a cesta se stejným počtem hran z obou párování přispívají 0
k |Q|−|P|; cesta s jednou hranou Q navíc přispívá +1 a je augmentující
pro P, opačná cesta přispívá −1. Pokud |Q|=s je maximum a |P|=s′,
existuje tedy nejméně s−s′ navzájem vrcholově disjunktních augmentujících
cest. To současně dokazuje: žádná augmentující cesta ⇒ P je největší.
Není třeba vnější věta bez důkazu.

## H-P02. Reprezentace, H1 a předpoklady inicializace

Při postupném zpracování dívek stačí každé přiřadit libovolného dosud
volného souseda, pokud existuje. Dívka, která zůstane volná, měla již
v tu chvíli všechny sousedy obsazené; žádný chlapec se v této inicializaci
neuvolní. Na konci proto není hrana mezi dvěma volnými vrcholy:
párování je maximální. Každý dívčí seznam se projde nejvýše jednou,
tedy O(M+N+E) včetně nulování polí.

Pro každou neobsazenou dívku g se uloží `QUEUE[f]=g, IQUEUE[g]=f`
a zvýší f. To je přesně definovaná reprezentace p. ix, ne nové omezení
na vstup. H1 je vysokoúrovňová inicializace této reprezentace; není
platný protipříklad zvolit nesouhlasnou IQUEUE a tvrdit, že byly splněny
definice polí. Autorův primární rozpis v odpovědi 7 obsahuje oba zápisy.

MARK má po známé opravě index 0 a počáteční nuly. Nikdy se do MARK[0]
nezapisuje nenulová hodnota; H13 ho může bezpečně číst pro volnou dívku.
Každá hrana má jeden uzel e a v seznamu své dívky se objeví právě jednou.
Pole GLINK, GTIP, BTIP, GNEXT se nemění. BLINK/BNEXT se mohou měnit,
protože pro každou novou vrstvu skládají jiný seznam hran z chlapce.
Souběžné hrany by jen opakovaly tutéž možnost a důkaz také neporušují.

## H-P03. H2–H10: přesné vrstvy, fronta a předčasné zastavení

Pro pevné současné párování orientujme nepárovací hrany z dívek do
chlapců a párovací hrany opačně. Zdrojem je množina všech volných dívek.
Vzdálenosti v tomto pomocném grafu jsou `d(g)=2l` pro G_l a
`d(b)=2l−1` pro B_l. Volné dívky jsou G_0. U párovaného chlapce
v B_l je jeho partner novou dívkou G_l: předchozí objev téže dívky
by vyžadoval dřívější objev tohoto jediného partnera.

H2 nastaví frontu na všechny f zdrojů. Na počátku H3 tvoří
`QUEUE[i:q]` právě G_l; q′ zmrazí konec této vrstvy. H4 prohlédne
každou dívku do q′ jednou, H5–H7 každý její incidentní hranový uzel
jednou. Nový chlapec dostane v H8 první a tudíž nejmenší možnou vrstvu
l+1 a vstup do MARKED. Jeho případná partnerka se v H9 přidá za q′.
Každý chlapec i každá taková dívka se tedy vloží nejvýše jednou.
Velikosti QUEUE≤M, MARKED≤N stačí.

Je-li chlapec již označen, nemůže mít při zpracování G_l vrstvu vyšší
než l+1. Podmínka `MARK[b]>l` v H6 tak znamená právě vrstvu l+1;
uloží všechny další hrany z této vrstvy chlapců do G_l. Podmínka
`MARK[b]≤l` zahodí hranu, která nepokračuje po nejkratších vrstvách.
Párovací hrana dívky v G_l vede do B_l a je správně zahozená.
Seznam BLINK tedy reprezentuje zpětně orientované nepárovací hrany
z B_(l+1) do G_l. Jediný výstup z dívky je její partner v B_l,
případně ⊥. Všechny cesty v takto obráceném DAG klesají po vrstvách.

První volný chlapec stanoví `L=l+1`, délku SAP `2L−1`, a H9 vrátí
q na q′. Před jeho objevením již mohly být do fronty vloženy partnerky
několika obsazených chlapců téže poslední vrstvy. Tyto partnerky leží
až v G_L, takže žádná cesta délky 2L−1 je nepoužije; jejich zahození
je bezpečné. Už označení obsazení chlapci v B_L mohou v DAG zůstat,
ale neposkytují volný konec. Po stanovení L další nové obsazené chlapce
H8 vynechá, kdežto každý další volný chlapec se vloží a zvýší r.
Proto přesně posledních r prvků MARKED jsou volní chlapci B_L,
i když před nimi jsou ještě obsazení chlapci téže vrstvy.

Zpracování zbytku G_(L−1) pokračuje, aby se zachytily všechny SAP,
ale q=q′ zabrání vstupu do další vrstvy. Bez nalezeného volného chlapce
pokračuje H10 právě tehdy, když q>q′, tedy když vznikla další G vrstva.
Jinak už není dosažitelný žádný nový vrchol a L=0 dokazuje neexistenci
augmentující cesty. Prázdná počáteční fronta (f=0) správně dojde
rovnou k tomuto ukončení. Algoritmus netestuje neexistující vrstvu L=0
v zásobníku, protože H10 již skončil.

## H-P04. H11–H15: trvalé odstraňování DAG a neztrácení cest

H11 postupně vybírá právě r volných konečných chlapců. Z chlapce b
ve vrstvě l vybere H13 oblouk do dívky g v G_(l−1); pokud není volná,
její jediný partner je v B_(l−1), takže H14 přejde o jednu vrstvu dolů.
BOY[l] si pamatuje chlapce pro návrat. Při slepé uličce H15 přeskočí
na vyšší l; chybí-li vyšší vrstva, tento konečný chlapec už nemá SAP.
Při dosažení volné dívky nutně l=1, neboť všechny volné dívky byly
prvotní G_0. Cesta má právě L chlapců a L dívek, takže
`1≤L≤min(M,N)`; to je správný rozsah známé opravy zásobníku.

H13 odstraní hranový uzel ze seznamu před sestupem. To je bezpečné
v obou možných výsledcích: neúspěšný průchod pod jeho dívkou vyčerpal
všechny cesty odtud, a úspěšný průchod její vrchol odstraní. Graf se
v této fázi jen zmenšuje, proto se slepá ulička nikdy znovu neoživí.
Když je dívka již z předchozí augmentace odstraněna, její nový partner
má MARK<0; právě test v H13 ji přeskočí. U dosud nedotčené dívky je
partner beze změny a má nezápornou značku. Po dokončení H17 jsou
všechny dívky i chlapci použitých cest takto označeni nepřímo/přímo.
Neexistuje dodatečně odstraněná dívka s dosud nezáporným partnerem.

Všechny vybrané SAP jsou tedy vrcholově disjunktní. V okamžiku vstupu
do H11 s r=0 není v zbývajícím DAG žádná cesta mezi volnými konci.
Není třeba maximum počtu disjunktních cest; stačí tato maximalita.
H11 vymaže značky všech t navštívených chlapců, včetně −1 i případných
mrtvých vrcholů B_L. Ostatní značky byly nulové po celou fázi. H2
proto může začít s přesně stejným invariantem nulových značek.

## H-P05. H16–H17: fronta volných dívek a vlastní augmentace

Nechť se volná dívka g nachází na indexu k<f_old. H16 sníží
f na f_old−1 a poslední dosud platný prvek i přesune na k, se současnou
opravou `IQUEUE[i]=k`. Pokud k=f, jde o neškodné přepsání odstraňovaného
prvku sebou samým mimo nový platný prefix. Jinak všechna zbývající
volná g mají stále správný inverzní index. Žádná nová dívka se při
augmentaci neuvolní, takže tento prefix nadále obsahuje všechny a jen
volné dívky. Obsah IQUEUE u obsazených dívek není požadován.

V H17 nechť aktuální g je již připravená nová partnerka chlapce b_l.
Uložením g′=BMATE[b_l] před přepsáním se zachová stará partnerka.
Potom dva zápisy BMATE/GMATE přidají právě novou hranu a označení
MARK[b_l]=−1 vyřadí použitý vrchol pro zbytek fáze. Je-li g′≠0,
další iterace s g=g′, b=b_(l+1) opraví právě uvolněné staré spojení.
Na posledním chlapci je g′=0 a cyklus skončí. Takto se převrátí všech
2L−1 hran, zachová se párovací invariant a velikost stoupne o jednu.
Nikdy se nečte BOY[L+1], protože poslední chlapec je volný.

## H-P06. Proč následující úspěšná fáze má větší L

Tento krok není nahrazen pouhou citací Hopcrofta–Karpa. Použijme úplné
původní BFS vzdálenosti d před danou fází, i za poslední vrstvou, kterou
skutečná implementace pro účely rychlosti neprohlédla. Pro každý původní
reziduální oblouk x→y s dosažitelným x platí `d(y)≤d(x)+1`.
Každý oblouk SAP má rovnost. Po převrácení libovolného počtu disjunktních
SAP se změní směr právě těchto oblouků; nově orientovaný oblouk má
`d(y)=d(x)−1`, a zvlášť stále splňuje nerovnost ≤d(x)+1.

Každý zbývající volný dívčí začátek měl d=0 a každý zbývající volný
chlapecký konec měl d≥2L−1, nebo byl nedosažitelný. Nedosažitelný se
novými obrácenými hranami nestane dosažitelným: všechny jejich konce
měly konečné d a každá stará hrana z konečného d také vedla do konečného d.
Každá nová augmentující cesta má tudíž délku nejméně 2L−1. Při rovnosti
musí každý její oblouk zvětšit d přesně o 1; nesmí použít žádnou
obrácenou hranu z některé vybrané SAP.

Navíc nemůže použít ani žádný vrchol vybrané SAP: oba její původně
volné konce jsou nyní obsazené a každý její vrchol musí v nové
augmentující cestě použít svou novou párovací hranu. Ta je právě jednou
z obrácených hran a hodnotu d snižuje. Nová cesta délky 2L−1 je tedy
právě cestou v původním DAG mimo již odstraněné vrcholy. Takové cesty
H11–H15 vyčerpají. Po fázi proto zbývající nejkratší augmentující cesta
má délku aspoň 2L+1 a další úspěšná fáze má L alespoň o 1 větší.

## H-P07. Certifikát q=t+f, nezávislá množina a optimálnost

V poslední neúspěšné BFS fázi (L=0) označme A všechny q dívek fronty,
B′ všech t označených chlapců. Všechny seznamy dívek A byly prohlédnuty,
takže jejich sousedé jsou přesně B′. Každý z B′ je obsazený, jinak by
L nebylo 0, a jeho partnerka je v A. Párování dává bijekci B′ na
nevolné dívky A. A navíc obsahuje všech f volných dívek. Proto q=t+f.
Stejný vztah plyne i indukcí H8–H9: nový chlapec zde pokaždé přidá
právě jednu novou partnerku za původních f dívek.

Žádné párování nemůže obsadit více než t dívek A, protože mají jen
t možných různých partnerů. Nechá tedy alespoň q−t=f dívek volných.
Současné párování má M−f hran, a tím je prokázaná maximálnost.
Je-li f=0, obsahuje už M hran a triviální horní mez M stačí; sporné
slovo „perfect“ patří pouze do dříve uzavřeného F7-C0001.

Množina `I=A ∪ (B\B′)` je nezávislá: uvnitř částí nejsou hrany a
každý soused A je v B′. Její doplněk K je proto vrcholové pokrytí
velikosti `(M−q)+t=M−f`, tedy velikosti nalezeného párování. Každé
vrcholové pokrytí má aspoň tolik vrcholů jako libovolné párování,
protože jeho disjunktní hrany potřebují různé pokrývající vrcholy.
K je minimální a I maximální. Naopak nezávislá množina větší než I
by dala menší pokrytí a odporovala tomuto párování. Pro f=0 závěrečný
DAG nic neobsahuje; I je celá chlapecká část, její doplněk všechny
dívky a argument stále platí, včetně M=0 či N=0.

## H-P08. Theorem H a všechny jeho tištěné mezikroky

V okamžiku, kdy vstupujeme do H11 s r=0, jsou podle H-P06 všechny
zbývající augmentující cesty dlouhé nejméně 2L+1. Pro pevné maximální
párování Q velikosti s dá symetrická diference z H-P01 nejméně s−s′
disjunktních augmentujících cest, kde s′ je aktuální velikost.
Na každé je aspoň L+1 hran z Q (a aspoň L hran ze současného párování).
Tyto hrany Q jsou navzájem různé, tedy `s≥(L+1)(s−s′)`.
Úpravou dostáváme přesně `s′≥Ls/(L+1)`; členy jsou nezáporné
a L+1>0. To dokládá oba krátké tištěné mezikroky zvlášť. Pokud s=s′,
rodina potřebných cest je prázdná a nerovnost zůstává platná.

## H-P09. Cena každé fáze, ukončení a Corollary K

V BFS fázi je každý z nanejvýš M zařazených seznamů dívky zpracován
jednou a každá hrana nejvýše jednou. Každý chlapec se do MARKED přidá
jednou. DFS natrvalo odstraní každou navštívenou hranu z BLINK;
každý sestup i návrat lze účtovat k této hraně, každý nový start
k jednomu koncovému chlapci. H17 sečte délky disjunktních cest a je
celkem O(M+N). Reset MARK je O(N). Fáze tedy stojí O(M+N+E),
inicializace H1 také; pomocná paměť O(M+N+E) včetně polí hran.
Každá úspěšná fáze zvýší velikost párování aspoň o 1, takže jich je
nejvýše s. Poslední fáze je neúspěšná a skončí. Ukončení je tím
dokázáno i bez následující ostřejší meze.

Pro s≥1 má L v úspěšných fázích ostře rostoucí celočíselné hodnoty.
Fází s `L≤sqrt(s)` je nejvýše floor(sqrt(s)). Před první fází s
`L>sqrt(s)`, pokud taková fáze existuje, mají všechny augmentující cesty
alespoň L hran maximálního párování Q. Argument symetrickou diferencí
z H-P08 proto přímo dává deficit `s−s′≤s/L<sqrt(s)`. Každá další
úspěšná fáze deficit sníží aspoň o 1. Dohromady je počet fází O(sqrt(s)),
včetně jedné závěrečné neúspěšné fáze pro s≥1. To dává uvedenou mez.

Tím je přesně doložen také tištěný mezikrok s′≥s−sqrt(s) před první
fází s L>sqrt(s). Předchozí hodnota L může přeskočit mez o víc než 1;
výše se nepředpokládá, že každá změna L je právě o 1. Pro L=0
v závěrečné neúspěšné fázi se
věta „L se zvětšuje“ vztahuje pouze k dalším existujícím SAP, nikoli
k pomocnému vynulování registru v H2.

Při s=0 má graf E=0 a algoritmus správně skončí po inicializaci a jedné
prázdné BFS. Trvá to O(M+N), nikoli doslovně O((M+N+E)sqrt(s))=O(0).
Obecný vzorec bez předpokladu s≥1 je například
`O((M+N+E)(1+sqrt(s)))` (pro zcela prázdný vstup též konstantní overhead).
Tento okrajový rozsah tištěné asymptotické věty je evidován odděleně
jako nízká interpretační pochybnost; nemění správnost párování ani
dokázanou mez pro s≥1.

## H-P10. Rozsah a známé opravy

Ověřena matematika vysvětlení a všech H1–H17, certifikátu, Theorem H
i důkazu Corollary K pro s≥1. Známá oprava MARK zahrnuje sentinel 0
čtený H13. Známá oprava BOY dovoluje mezní L=min(M,N), kterou původní
0≤l<M neobsáhlo při L=M. Přidání GLINK mezi neměnná pole je správné,
protože s ním H neprovádí žádný zápis. Úplná errata v lokálním TeXu
a obou PDF vrstvách jsou zohledněna; současný primární prefascicle
nemění matematickou strukturu H. Nový nález F7-C0001 se zde neopakuje.
Případ s=0 zůstává oddělený od uzavřeného nenulového oboru.
