# Souvislý průchod §2.5 — 5. listopadu 2026

X0981. Přímo přečteny všechny původní strany435–456 a odpovědi607–618,
včetně všech44zadání, diagramů a vytištěných instrukcí. Přečteny všech šest
PROOFS původního paketu, SOURCES, ERRATA, kořenové revize kompakce,
buddy systému, alokačních konvencí, historického TeXu, Wolmana/Russella,
původních kompaktorů, nejhorších mezí, C0091 a posledních mezí životnosti.
Přesný vlastní first-fit důkaz byl znovu přečten celý. Nejde o nové čtení
každé stránky externích článků nebo všech vývojových pokusů v následných
paketech. Přijaté úspěšné výpočty se neopakovaly.

Nový nález nevznikl. C0062–C0069 a C0091 jsou zachovány s přesným rozsahem;
C0074 zůstává candidate, C0073 dismissed. Úlohy33 a38 jsou uzavřeny podle
nového bibliografického pravidla. Úlohy18,27,32,39,40 zůstávají partial.
Hlavní text zůstává partial pro původní měření a přesné níže uvedené meze.

## A–C: model, seznamy a hraniční značky

435–436: definice poolu, fragmentace a rozdílu mezi dostupnou pamětí a
nedosažitelnými dosud neuvolněnými uzly jsou konzistentní. Mapa má fond
2^17=131072; poslední dostupný interval začíná77519 a má53553slov, tedy
končí přesně na hranici fondu. Intervaly0..100 a632..673 odpovídají prvním
dvěma záznamům. Počty53rezervovaných a21volných bloků nebyly z původní
historické stopy nově rekonstruovány. Oprava obr.42 na27198 je veřejná.
Vznik paměťového významu slova heap kolem1975 nemá v této revizi nezávislý
dobový doklad; rychlé hledání našlo převážně přepis knihy. Není to důkaz
chyby ani důvod vydávat přesnou dataci za ověřenou.

A: Q je předchůdce P a všechny dříve prohlédnuté bloky mají SIZE<N.
Při přesném fitu se vyjme celý blok, jinak zůstane volný dolní prefix K
a přidělí se horní suffix. Příklad1300,1200 s požadavky1000,1100,250
správně rozlišuje first-fit od best-fit. A' ponechá při K<c skutečnou
SIZE původního bloku; uvolnění musí znát právě tuto velikost. Hodnoty c
8 či10 jsou výslovné empirické návrhy, nikoli dokázaná univerzální optima.

B: seřazený seznam najde sousedy Q,P vraceného P0. Předpoklad, že žádná
vracená buňka není volná, vylučuje překryv. Nejprve se případně připojí
horní soused, potom dolní; výsledkem jsou opět maximální volné intervaly.
SIZE hlavy0 a umístění hlavy mimo pool jsou podstatné okrajové podmínky.
Obrázky(2)–(6) správně rozlišují pouhé znovuzpřístupnění, slučování a
kompakci, která navíc musí přeložit odkazy.

Hraniční značky: záporná TAG značí volný blok, SIZE na jeho konci dovolí
nalézt levý začátek v konstantním čase. Kruhový seznam má dvě hlavičková
slova a délku bloku alespoň2. Pole SIZE a odkaz v druhém slově se při
délce2 nepřekrývají. Rovnice(8) dává obě inverze sousedních odkazů.
C odstraní dostupné sousedy, sloučí délky a v C5 zapíše obě patní značky
i přesné čtyři vazby seznamu. Všechny čtyři kombinace sousedů jsou pokryty.

Buddy: zarovnání délky2^k dává druhého sourozence XOR2^k; příklad442
souhlasí bit po bitu. R vybírá nejmenší neprázdný řád j≥k, proto jsou
všechny nižší seznamy při rozdělování prázdné a lze je přímo inicializovat
jediným blokem. S sloučí právě volného stejně velkého sourozence a
odstraní jej obousměrnými odkazy. Pořadí volných bloků nemění správnost.
TAG musí přežít uživatelské zápisy; KVAL je potřebné pouze u volných
bloků, při uvolnění zná k volající. Pozdější doplnění tyto kontrakty
vyjasňují, sama nedokazují chybu původního algoritmu.

## D–G: statistika a přesné hranice empirických tvrzení

Pro A,B,C rezervovaných bloků se dvěma, jedním, žádným volným sousedem
platí N=A+B+C a2M=2A+B+e, e∈{0,1,2}. Při rovnoměrném vracení a pevném
N je drift(C−A)/N; při rezervaci p−1. Původní1−p na444 je známá chyba.
Rovnováha dává2E[M]=pN+E[e]. Přibližně konstantní N je v textu výslovné;
při kolísání nelze bez dalšího zaměnit E[(C−A)/N] za podíl průměrů.
Společné nezávislé exponenciální životnosti dávají rovnoměrného příštího
odchozího. Uniformní životnosti tuto vlastnost nemají.

P1–P4 vrací před vložením, T≥1; uzel žije právě T kroků. Součet příspěvků
věkových kohort dává E[ST], při nezávislosti E[S]E[T]. S1 má střed1050,
S2 střed3.5 a jeho pravděpodobnosti sečtené do1. Současná velikost je i
v téměř-LIFO pokusu nezávislá na volbě životnosti. C=fM+rN je přesné
rozložení objemu; f≥r a z toho odvozené dvě třetiny jsou zde heuristika
typického zatížení, nikoli záruka pro každou historii.

Historická čísla447–450 (např.25/49 v čase4600,515/240/176 při větších
životnostech,95%,2.8,0.04,1.3,0.9) nejsou znovu reprodukována. Původní
proud náhodných čísel není uveden. Vlastních432pokusů úlohy3 se za jejich
replikaci nevydává. Tvar obr.42/43 a slovní vysvětlení odpovědi18 jsou
konzistentní s výběrem horního konce; přesná vazba obou historických map
na stejnou vstupní stopu zůstává neověřená. Úloha18 proto stále partial.
Původní obr.44 má veřejnou náhradu; originál a náhrada byly porovnány.

Tabulka449 používá hrubé časy: A* má32+7A+7F+I, kde F je počet průchodů
hlavou a I značí dělení. R původně19+25R; po úplné FIFO opravě21+25R.
S má27+25S+3B+2A, kde poslední A,B jsou jeho vlastní počty větví;
průměr27+26S není přesná formule pro každou operaci. C má čtyři základní
časy29/18/34/31 a případně3u navíc za opravu ROVER. Odhady kompakce na
uvolněný uzel souhlasí v uváděné hrubé přesnosti; závisí na náhodném
rozložení mrtvých běhů a nezahrnují novou opravu NULL.

Distributed fit: při N=2^14 je64slotů každé velikosti1..256, jejich objem
2105344;1792přepadových slotů po256 zabere458752, tj.17.89% celku. První
vhodný a nejmenší vhodný slot mají ve velikostně seřazené tabulce stejnou
velikost. Výběr celého slotu se nesmí zaměnit za dělení otvorů algoritmu A.
Pro N nezávislých rovnoměrných počátečních adres a bez odchodů dává
kruhová symetrie lineárního prohledávání střední počet překročení hrany
(Q(N)−1)/2. Součin v Q lze ohraničit exponenciálou a následnou integrální
mezí, takže přepadů je méně než sqrt(pi*N/8). Úplná odvozená formule Q
z Vol3 se zde znovu nedokazuje; je přesně zaznamenána jako závislost.
Zaokrouhlení počátečních adres dolů na1,65,129,… je pro statické vkládání
příznivé. Komentář o přesouvání při mazání není samostatný důkaz pro
libovolnou dynamickou stopu. Tyto přesné důkazní meze ponechávají451partial.

Přijatý Coffman–Leighton1986 skutečně předpokládá Poissonovy příchody a
nezávislé exponenciální pobyty; jeho silnější vysokopravděpodobnostní
mez podporuje asymptotický řád knihy. N je střední obsazenost, nikoli
tvrdá mez, a tvrzení není zárukou pro nekonečný časový horizont. Převzetí
konference nezaručuje každý redakční detail časopisecké sazby1989.

LRU na452 řadí podle posledního přístupu. Kruhová bitová druhá šance
opravdu skončí po nejvýše jednom mazacím oběhu a dalším kandidátu,
pokud souběžné přístupy předpoklad nemění; nejde o přesnou ekvivalenci
pořadí LRU. Tvrzení o naprosté většině brzkých dalších selhání po první
kompakci nemá určený vzorek a zůstává neověřeným empirickým údajem.

## Úlohy1–31: okraje, skutečné instrukce a modely

1: pool0..M−1 dovolí přesné zaplnění; C0066 opravuje≥ na> v607.
2: konvexní idealizovaná cena kL/(k−b)+k/2 má minimum b+sqrt(2bL).
Při b=1,L=10 dávají k5 a6 shodnou cenu15. Přesná atomová identita a
neuskutečnitelnost stejné hypotézy pro všechna neomezená k jsou zachovány
v dřívější revizi; Wolman sám užívá aproximaci poloviny prázdné buňky.
Nový protipříklad splňující celé zadání z toho nevzniká.
3 je vlastní, výslovně určená simulační studie.4 ukládá velikost bez
znaménka: rA=N−SIZE(P), jeho absolutní hodnota je zbytek K. Znaménko
nemění test nuly, unsigned STA ani pozdější LD1; nejde o chybu programu.
5 správně zachovává malé zbytky kvůli pozdějšímu slučování.6 vyžaduje
známou opravu ROVER při NULL; dva průchody koncem zaručí neúspěšné
ukončení.7 má správný opačný příklad2000,1000 a požadavky800,1300.
8 hledá nejmenší dostatečnou SIZE s jejím předchůdcem;9 připouští
vyvážený strom podle(size,address), s logaritmickými operacemi.

10 po známé opravě tvoří sjednocení intervalů: oba max jsou potřebné,
aby vracení podintervalu nezkrátilo již volnou oblast.11 při nezávisle
rovnoměrném ROVER mezi n+1hlavami a rovnoměrné mezeře má střed
(2n+3)(n+2)/(6(n+1)); tabulka pro n2 dává14/9. Pouhá rovnoměrnost
vracené adresy z ROVER rovnoměrný neudělá; v knize jde o předchozí
heuristický předpoklad.12–17 souhlasí s invarianty hraničních značek
a všemi vytištěnými větvemi MIX.19 slučuje pouze doprava při rezervaci;
každé sloučení zkrátí seznam a opraví případný ROVER. Citovaný dobový
TeX2.0/1986 je již doložen v X0785, s přesným rozlišením zdroje a sazby.

20 vysvětluje konstantní odstranění buddyho.21: při n=2^k*alpha,
1≤alpha≤2, má poměr profil4(alpha−2/3)/alpha², minimum4/3 a maximum3/2.
Obyčejná limita neexistuje; logaritmický průměr s mírou
dalpha/(alpha*ln2) je1/ln2.22 vyžaduje chráněný TAG také ve vnitřních
začátcích11slovního složení8+2+1;23 oba XOR příklady souhlasí.
24 vysvětluje stale TAG při vlastním root-buddy;25 dává les menších
kořenů;26 vyžaduje P+2^k≤M, tedy C0067.27 má oddělené C0068/C0069
a stále interpretačně otevřený C0074, viz níže.28 vyžaduje známou
záměnu dvou LOAD polí,29 externí TAG nebo dohledání ve volných seznamech.

30 má přesný konečný Markovův model s výslovně zvolenými příchody a
vracením. Dosažitelná třída je ireducibilní přes prázdný stav a díky
jeho smyčce aperiodická. Stacionární drift počtu živých bloků a listů
rozkladového stromu dává shodné střední počty dělení a slučování.
31 má úplný Fibonacciho stromový alokátor; slučují se skuteční sourozenci,
nikoli libovolní sousedé. Délka2 se dělí na1+1, nula není potřeba.
Russellovy metriky fragmentace a vlastní formát metadat se nezaměňují.

## Kompakce a nejhorší meze32–44

32: Crainovy rozdíly x_(k+1)−x_k jsou nejvýše čtvrtinové podlahy
předchozího rozdílu. Jejich součet je nejvýše16664, tedy pod16667.
Konečný stav zbývajících dob má jedinou aperiodickou rekurentní třídu;
regenerace dává alpha=E[Y]/E[tau]. Poslední přijatý X0917 certifikuje
11.03203≤alpha<12.99721822. Starší odhad12.10 je empirický a původní
„asi14, pravděpodobně nepřesné“ není tvrzení přesné hodnoty. Úplná přesná
hodnota nadále chybí; nové počítání52milionů událostí nebylo spuštěno.

33: pomocný LINK současně označuje živé uzly a tvoří zásobník; každá
dosažitelná hlavička se vloží právě jednou. G5–G7 přiřadí nové adresy
v původním pořadí a sentinel nedovolí sloučit mrtvý konec. G8 překládá
pouze skutečné nenulové odkazy živých uzlů. G9 ale musí uchovat SIZE před
překrývajícím přesunem: C0062.34 má SIZE správně v I5, ale překládá NULL
na výslovně nenulový LINK(0): C0063; přesný čas má24c: C0064.
35 správně rozlišuje přemístitelné rostoucí seznamy od nepřesouvaných
bloků pevné délky po dobu života.36–38: strategie trojic nesází dvojice
přes jejich hranice; při selhání by sedělo alespoň n−1osob. Paritní
útok s lichými mezerami dokazuje opačnou mez floor((3n−1)/2), včetně
zaokrouhlení. Vlastní first-fit invariant q+1+o(q)≤H a konstrukce podle
n modulo3 dokazují přesně floor((5n−2)/3) pro dolní konec otvoru.
Samotná autorova atribuce této přesnější formule Robsonovi se přeskočí.

39: tři oblasti s rozpočty n1,n2,2m−2 dávají subaditivní pomocnou funkci;
rozklad n=bc+a dokazuje existenci limity. Všechny čtyři číselné meze
N(3),N(4) jsou matematicky doloženy v X0676. Historický výrok o tehdejší
neznalosti všech přesných N(m),m>2 nebyl nezávisle ověřen. Aktuální
offline/známé-doby modely nejsou tímto online modelem; úloha39 partial.

40: C0091 vyvrací konkrétní dolně zarovnanou strategii pro maximum32:
obecný faktor4709347/783360>6, úplná dříve ověřená stopa5554555operací.
Robsonův algoritmus vyžaduje celý volný slot horní mocniny dvojky a
stejné zarovnání; optimální N(32)≤6 zůstává pravdivé. Dělitelné řetězce,
přesná mocninná formule a dolní mez23/18 pro{3,4} jsou doloženy dříve.
Koeficient1.1825 před ln m stále není dokázán ani vyvrácen. Přečtený
Robson1974 dokládá slabší1.2165…, nikoli1.1825. Nedostupný Krogdahl
je samostatná bibliografická výjimka. Harmonický výrok je výslovná
domněnka; audit z něj nedělá tvrzení ani povinnost nově vyřešit výzkum.

41: invariant rozštěpeného objemu dokazuje koeficienty
1,3/2,17/8,183/64,3769/1024,149607/32768. Následné přijaté důkazy
uzavřely ostré konstrukce do r5, libovolný konec fondu a přesnou
levostrannou mez i při lichém n/2^r; starší partial odstavce původního
paketu jsou proto historické. Sedm snímků na617 dává41n/16>2.5n při
vynucené přednosti nižších řádů, bez extrapolace testů.
42: přechody best-fit vzoru zachovávají všechny požadované délky a živý
rozpočet. Silnější konec(n−4m+11)(m−2) je již uzavřen X0651/X0675,
včetně původních242–243; chybějící244 se za přečtenou nevydává.
43: dolní-konec first-fit má indukční prefixy a teleskopující váhy
D_j/(m+j−1). Harmonický přepis na617 musí končit2m−1, nikoli2m+1:
C0065. Při rovnostech jsou D_j kladné a uvedená C_j souhlasí.
44: použije se zaokrouhlený zobecněný kvantil, také při plochém F;
konečná maximální velikost je předpoklad hlavního oddílu.

## Přesné lokace nálezů a známých oprav

| ID | Původní chybová stránka | Rozsah |
|---|---:|---|
| C0062 | 613 | G9 přečte přepsanou hlavičku; uložit velikost před přesunem. |
| C0063 | 615 | Řádky50–52 přeloží i NULL; doplnit J6Z před51. |
| C0064 | 615 | Součet vytištěných frekvencí má24c místo25c. |
| C0065 | 617 | Levý harmonický součet má špatný koncový index2m+1. |
| C0066 | 607 | Přesné zaplnění zásobníkového fondu je omylem odmítnuto. |
| C0067 | 611 | Buddy končící přesně na M je omylem vyloučen. |
| C0068 | žádná | Chyba veřejné opravy2006;611–612 jsou pouze kontext. |
| C0069 | 612 | Jen komentář ř.20: LINKB(P), nikoli LINKB(L). |
| C0074 | 611–612 | Candidate: stačí kladný TAG sentinelu, nebo se předpokládá i self-link? |
| C0091 | 616 | Vytištěná strategie nezaručuje tvrzený faktor. |

C0068: opravený MIX ponechá I4 na prvním bloku a vyjímá jej jako poslední.
V dosažitelném seznamu h→0→2→h se ztratí volný blok2. Přidané načtení
AVAILB[j] před R2 opraví výběr; sentinelová kontrola zůstane zachována.
C0074: kladné nulové slovo po LD4N vytvoří−0 a J4NN pokračuje. Standardní
self-link je nenulový a problém odstraní, ale jeho implicitní požadavek
na dodatečnou hlavu zůstává interpretační otázkou. Nepovyšujeme candidate.
C0073 zůstává dismissed: úloha43 dovoluje zvolit obrannou strategii;
vytištěná horní mez netvrdí správnost každé konvence odběru konce otvoru.

Čerstvý výpis všech čtyř vrstev obsahuje35záznamů: po odebrání duplicity
Krogdahl a cizího607/§2.4 zbývá33různých zásahů. Přímo byly znovu
porovnány erratové obrazy PP28,29,46,47. Známé obsahové vady původního
tisku mapujeme na436(obrázek),444(drift),448(obrázek),456(limitní indexy),
607(ROVER),608(sjednocení),611(odkaz na nesprávný vnitřní krok),
612(LOAD pole v S),613(AVAIL versus AVAILF) a616(Krogdahlův rozsah).
Změna FIFO na443, chránění TAG, znalost k, typografie, nové označení
algoritmů, reindexace správně definované posloupnosti32 a doplněný Crain
nejsou dalšími novými chybami původní stránky. „About four thirds“ je
přibližný výrok; známé zpřesnění se neeviduje jako přesná nepravdivá rovnost.

## Bibliografické výjimky a stav stránek

Přeskočeny přesné nedostupné sazby či atribuce uvedené v SOURCES a
pozdějších revizích: Shore/Davies/Reeves/Pflug445, Purdom–Stigler448,
Ross/Randell/Purdom–Stigler–Cheam/Margolin–Parmelee–Schatzoff/Campbell/
Shore/Nielsen450; JCSS1989 proti přečtené konferenci1986; LNCS1995 proti
přečtenému revidovanému Wilsonovi; osobní Weilandův příklad608;
zbývající přesné texty kompaktorů a Morrisovy dodatky613–614;
first-fit atribuce616 a přesná Krogdahlova sazba. Vlastní matematické
důkazy nejsou náhradou tvrzení, že jsme tyto prameny přečetli.

Stránky435–436,445–452,454–456,610–612,616 zůstávají částečné tam,
kde je nedoložená empirická/historická věta, přesná důkazní závislost,
otevřená úloha nebo candidate. Známá chyba může mít v pruhu červenou
barvu i při částečném pokrytí. Ostatní stránky tohoto bloku mají celý
matematický/faktický obsah účtován; přijatá chyba samozřejmě neznamená
bezchybnost. Strana607 navazuje na již dokončenou část§2.4.
Výslovné lokace zabraňují obarvení správného zadání455 kvůli chybě G9
na613 nebo původního programu kvůli vadnému erratu2006.

Další kurzor: historický oddíl§2.6, tištěná457 / soubor472.
