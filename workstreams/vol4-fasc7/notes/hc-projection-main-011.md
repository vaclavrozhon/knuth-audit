# Hlavní text p10–12: obecná projekce a HC obrázek

Rozsah: definice HC na p10–11/file25–26, obecná projekce, čtyři typy
vrcholů a počty jejich označení na p11, první věty p12/file27.
Originály byly zobrazeny. Konkrétní pohledy Fig. 101/103/104 mají vlastní
evidenci; níže uvedený obecný důkaz neuzavírá jejich jednotlivé skryté
úseky ani počty T. Odkaz na „formal definition“ v odpovědi 40 má
samostatný otevřený C0005 a není předpokladem tohoto důkazu.

## HC-1 — význam definice a úplnost čtyř typů

Různé junctions jsou různé body. Spojující přímé úsečky představují
hrany grafu a jejich průniky jsou jen společné konce; takto zadané
nakreslení je rovinné vnoření, tedy graf je planární. Vrchol stupně tři
je viditelný jako rozvětvení. Vrchol stupně dva je díky zákazu kolinearity
viditelný jako zlom. Uvnitř ostatních úseček není zlom ani rozvětvení.
To odůvodňuje obě věty za podmínkami (ii),(iii), včetně toho, proč by
bez (iii) nešlo stupeň dva vyčíst pouze z čar.

U stupně dva je menší úhel dvou paprsků mezi 0 a π: typ V. U stupně tři
jsou tři kladné cyklické úhly se součtem 2π. Je-li jeden π, ostatní dva
mají součet π a dostáváme T. Je-li jeden větší než π, ostatní dva mají
součet menší než π a dostáváme W. Zbývající možnost jsou všechny tři
menší než π, tedy Y. Dva úhly ≥π nemohou nastat. Toto je přesně (19)
a vylučuje chybějící pátý typ. Paprsky nemohou splývat: pak by dvě
úsečky sdílely celý interval, v rozporu s definicí HC.

## HC-2 — existuje hustá množina opravdu obecných pohledů

Pracujeme s konečným vloženým 3VP: různé vnitřky stěn se neprotínají,
hrany jsou skutečné hranice nekoplanárních stěn a každým vrcholem
procházejí právě tři. Směr pohledu označme q. Stačí vyloučit:

1. q rovnoběžný s některou hranou nebo s rovinou některé stěny;
2. projekci vrcholu na neincidentní hranu, případně na jiný vrchol;
3. kolineární projekce dvou prostorově nekolineárních nositelek hran;
4. společný průsečík projekcí tří hran, který není obrazem jejich
   skutečného společného vrcholu.

Nejde o tvrzení, že právě tato formulace je minimální. Zahrnuje také
zbytečné výjimky skryté uvnitř tělesa. Pro důkaz obecného tvrzení stačí
její postačitelnost a hustota přípustných směrů.

První výjimky jsou konečně mnohé velké kružnice nebo jednotlivé body
na sféře směrů. Projekce v na bod hrany a+tu znamená, že q je násobkem
v−a−tu; směry leží v rovině span(v−a,u), případně na přímce, je-li
v na nositelce. U nesplývajících prostorově kolineárních segmentů
je projekce injektivní, není-li q jejich směr, takže nemohou kolidovat.
Dvě různé nositelky mohou mít shodný promítnutý obraz jen tehdy,
jsou-li koplanární a q leží v jejich společné rovině. Tím jsou
odůvodněny nulové plošné míry i pro druhou a třetí podmínku.

Pro trojí křížení je nutný ještě samostatný argument — právě ten
v odpovědi 40 chybí. Jsou-li dvě nositelky koplanární, jejich rovina
se pro obecný q promítá injektivně. Rovnoběžné pak nemohou křížit;
protínající se mají jediný společný bod p. Náleží-li p oběma úsečkám,
je to jejich skutečný společný vrchol a projekce třetí neincidentní
hrany přes něj je již vyloučena bodem 2. Není-li na obou úsečkách,
nejde ani o dvojí křížení těchto segmentů.

Zbývá dvojice mimoběžných nositelek L1,L2. Spojnice bodů
p(s)∈L1 a r(t)∈L2 má směr d(s,t)=r(t)−p(s). Vektory směrů
u1,u2 jsou nezávislé a d·(u1×u2) je pevná nenulová konstanta.
Proto normalizované směry d parametrizují otevřenou část sféry
jednoznačně dvojicí (s,t); zpětně se směr protne s touto afinní
rovinou a dvě souřadnice určí s,t.

Kdyby třetí odlišná nositelka L3 protínala spojnice pro otevřenou
množinu (s,t), obsahovala by tato množina součin dvou intervalů.
Pro pevné p(s), které neleží na L3, by L3 musela ležet v rovině
P_s určené p(s) a L2: jinak má s P_s nanejvýš jeden bod a jím může
procházet nanejvýš jedna z různých spojnic p(s)r(t). Pro dvě různá s
jsou roviny P_s různé, protože L1 a L2 jsou mimoběžné, a jejich
průnik je L2. Dostali bychom L3=L2, spor. Případ L3=L1 nebo L2
se skutečnými různými segmenty byl již vyloučen injektivitou projekce
na jedné přímce. Trojí křížení tedy nemůže nastávat na otevřené
množině směrů.

Navíc jde o algebraickou výjimku, nikoli o libovolnou množinu s prázdným
vnitřkem. Pro Li={a_i+t u_i} je projekční rovina nad jeho obrazem
dána n_i·x=n_i·a_i, n_i=q×u_i. Společná promítnutá průsečnice
vyžaduje slučitelnost těchto tří rovnic a q·x=0, tedy nulový determinant
jejich rozšířené matice řádu čtyři. Na otevřené oblasti s nezávislými
prvními dvěma normálami je to přesně podmínka souběžnosti. Předchozí
argument dokazuje, že tento polynom není identicky nulový. Jeho nuly
na sféře mají míru nula: v racionálních lokálních souřadnicích sféry
jde o nenulový polynom dvou proměnných; mimo nuly jeho koeficientů
má při pevné první proměnné konečně mnoho nul druhé. Indukce a Fubini
dávají nulovou plochu. Totéž dokazuje prázdný vnitřek nulové množiny.

Konečné sjednocení všech výjimek má tedy nulovou plochu a jeho doplněk
je hustý. Každý pohled lze libovolně málo pootočit do takového obecného
pohledu. Výrok o pravděpodobnosti nula se vztahuje na náhodné pootočení
s hustotou vzhledem k plošné míře, jak je v této geometrické formulaci
zamýšleno, nikoli na libovolné diskrétní rozdělení kamer.

## HC-3 — proč po odstranění skrytých bodů dostaneme HC

Na otevřeném úseku jedné promítnuté hrany mezi průsečíky s ostatními
promítnutými hranami se viditelnost nemění. Jednotlivé rovinné stěny
mají nad obrazem afinní hloubku. Příslušnost k obrazu stěny se může
změnit jen na obrazu její hranice; pořadí dvou různých hloubek se
nemůže změnit jejich rovností, neboť by v prostoru došlo k nepovolenému
průniku stěn či hrany s neincidentní stěnou. Incidentní stěny jsou
lokálně již rozlišeny. Všechny řezy jsou tedy konečné a na každém
zbývajícím úseku viditelnost konstantní.

U viditelného skutečného vrcholu je jeho blízké okolí izolováno
od neincidentních stěn (T39-0). Projekce vrcholu neleží na jiné hraně;
každá neincidentní stěna, jejíž obraz toto okolí pokrývá, je buď
striktně za vrcholem, nebo by zakryla i vrchol sám. Proto skutečně
viditelný vrchol má přesně místní vzor J41-c: V,W nebo Y. Viditelné
jsou dvě či tři větve, nikdy jedna, a žádné dvě nejsou kolineární.
Zde se používá již dokázaný přenos od cubies k obecnému vrcholu,
nikoli domněnka, že všechny úhly 3VP jsou pravé.

U průsečíku dvou projektovaných vnitřků hran jsou jejich prostorové
body v různých hloubkách. Není-li bližší hrana viditelná, nemůže
vzniknout viditelná křižovatka. Je-li viditelná s oběma incidentními
stěnami, ty pokrývají obě strany v jejím obrazovém okolí; vzdálenější
hrana je tam zakryta z obou stran. Je-li viditelná jen jedna incidentní
stěna, máme half edge a její povrch pokrývá právě jednu stranu.
Vzdálenější hrana pak buď zůstane zakryta i jiným povrchem, anebo
končí v průsečíku na odkryté straně. V druhém případě je to T:
dvě kolineární větve stejné bližší hrany a jedna příčná vzdálenější.
Trojí současné křížení je vyloučeno HC-2. Žádný stupeň čtyři ani
osamocený konec tudíž nevzniká.

Všechna křížení jsou tak zahrnuta jako konce vzniklých úseček.
Junctions jsou různé, mají stupeň dva či tři a stupeň dva není
kolineární. Výsledek splňuje všechny tři podmínky HC. Každý viditelný
skutečný vrchol je junction; další jsou právě T popsané výše.
U T leží stonek vlevo od šipky bližší half edge, neboť ta má
viditelný povrch vpravo. To dokazuje obecné věty p11 odděleně
od konkrétního počtu 15 artefaktů v obrázku (c).

Kvalitativní definice p11 říká, že malé pootočení nezmění počet čar
ani jejich vzájemné vztahy. Je-li tento typ kresby stabilní, lze
podle HC-2 vybrat dostatečně blízký obecný pohled a použít HC-3.
Stabilní kresba má tentýž počet a incidenci čar i stejné typy vrcholů,
a je proto také HC. Její správnost se tím neodvozuje z nepostačujících
dvou kvantitativních podmínek opravené odpovědi 40.

## HC-4 — označení, oba konce čáry a přesné počty

Úplný argument `cubie-junctions-exercise-041.md`, oddíly J41-c1–d,
dokazuje přesně 4 možnosti T,6 možností V,3 možnosti W a5 možností Y
včetně jejich dosažitelnosti a shody s tabulkou 1. Bez geometrických
omezení má každá větev čtyři nezávislé možnosti, takže u stupně tři
je to 4³=64, u stupně dva 4²=16. Všechny čtyři srovnávací počty p11
jsou tedy správné.

Každá čára HC je úsečka mezi dvěma různými junctions a účastní se
obou jejich lokálních podmínek. Uvnitř této čáry jde o stále stejnou
prostorovou hranu se stejnými incidentními stěnami; nedochází tam
ke změně konvexity ani počtu viditelných incidentních stěn. Má tedy
jediné označení. Je-li half edge, při popisu směrem od jednoho konce
znamená I/O opačné znaménko než od druhého, ale geometrická šipka
zůstává tatáž. To přesně vysvětluje první „second punch line“ p12
a potřebu orientace proměnných v pozdějším CSP; není to rovnost
dvou nezávislých místních I/O symbolů bez obrácení směru.
