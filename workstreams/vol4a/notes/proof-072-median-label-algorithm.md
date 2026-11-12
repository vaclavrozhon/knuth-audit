# Algorithm H a Subroutine I: invariant, správnost a počet návštěv

Checkpoint X0101, P0951–P0958. Originál H na p69/file86,
I na p70/file87, zadání 77–78 na p90/file107 a odpovědi
p548–549/file565–566. Použity obě známé opravy z 10.–11. 7.
2011: I4 hledá `MARK(u) != s or RANK(u) != 1`; opravený
odstavec 77(d) je v `images/proof-y-errata22.png`.

Přebíráme přesně P0943–P0950: izometrii redukovaných štítků,
konvexitu obou poloprostorů, jediného mate, konvexní hranice
B_0/B_1 a úplnost čtyřcyklové ekvivalence. Není zde nový běh
algoritmu ani enumerace. Mezi teoretickým rankem a pracovním
polem RANK níže výslovně rozlišujeme.

## Kořen komponenty a neměnná orientace — P0951

Na počátku každé fáze I1 je živá komponenta C konvexním
indukovaným podgrafem původního grafu. Její kořen r je
branou původního zdroje a do C:

    d(a,x)=d(a,r)+d(r,x) pro každé x∈C.

Počáteční C=G,r=a to splňuje. Pro volbu hrany r–s normalizujme
teoretické štítky na r=0 a označme její souřadnici h, takže
s=e_h. Po odstranění všech hran tohoto řezu zbudou přesně
konvexní části L={h=0}, R={h=1}. r zůstává branou do L.
Pro každé x∈R obsahuje l(x) bit h, a proto

    d(r,x)=1+d(s,x).

Tedy s je branou r, a následně i a, do R. Rekurze na R
ani pokračování na L invariant neporuší. Konvexní neprázdná
část mediánového grafu je mediánová: její geodetiky mají
stejné vzdálenosti a medián trojice leží v jejích intervalech.

Z bránové rovnosti vyplývá, že na každé dosud živé hraně
je pořadí vzdáleností od a stejné jako od aktuálního r.
Předzpracované early/late označení H1 se tedy **nemusí měnit**.
Zejména z r vedou pouze late hrany a mate každého v∈B_1
je jeho early soused. Uvnitř R platí d(r,x)=1+d(s,x),
takže early/late souhlasí i s vrstvením od s.

Následující lokální důkaz I3–I9 předpokládá tento invariant
a dokazuje právě potřebné úplné odstranění řezu; indukce
přes fáze se tím uzavírá, nejde o předpoklad správnosti H.

## Geometrie sousedů a explicitní square případ — P0952

Po celou fázi jsou ranky definovány vůči C **před** jejími
mazáními. Všechny vnitřní hrany L a R zůstávají v I3–I9
přítomny, takže hraniční průchod B_1 se mazáním nemění.

Je-li v∈B_1, každý jeho early soused v R leží v I(s,v),
a tedy v B_1. Jediný early soused mimo B_1 je mate(v)∈B_0.
Late soused u leží v R a má rank 1 nebo 2, protože jeho
vzdálenost do L je nejvýše 2 a není nula.

Pišme d(s,v)=D a l(v) s podporou {h}∪S, |S|=D. Late
soused u má podporu {h}∪S∪{i}, i∉S∪{h}. Libovolný jiný
early soused w≠v vznikne odstraněním souřadnice j≠i.
Jsou právě tyto možnosti:

1. j=h. Pak w∈L je mate(u), rank(w)=0, rank(u)=1 a
   x=m(s,v,w)=v.
2. j∈S. Pak w∈R a x=m(s,v,w) má podporu {h}∪(S\{j}).
   Je v I(s,v)⊆B_1, má vzdálenost D−1 od s a je sousedem w.
   Proto rank(w) je 1 nebo 2.

Druhá možnost navíc dává přesnou ekvivalenci

    rank(u)=1 ⇔ rank(w)=1.

Je-li rank(w)=1, cesta v–u–w je nejkratší (v,w se liší
ve dvou bitech), takže u∈B_1 díky konvexitě. Je-li u∈B_1,
pak w∈I(s,u)⊆B_1. Při druhém ranku jsou tedy oba ranky 2.
To současně dokládá všechny věty opraveného odstavce 77(d):
x je v B_1, při x≠v byl zpracován v předchozí vrstvě,
a zbývající rozhodnutí vyplývá z konvexity. Silnější
kořenový invariant zde vylučuje případ x=v,w∈R.

Má-li u jen jednoho early souseda v, nemůže mít rank 1:
jeho mate by byl další, od v různý early soused. Proto
je návrat z I8 bez zařazení u do fronty správný.

## Celá 77(d): značky, I8 a BFS — P0953

Vrcholy použité jako značka s jsou po celou rekurzi různé;
formální indukce master listu je níže. Proto porovnání
MARK=s odlišuje právě současnou fázi od všech starších
hodnot polí. Jediné současné značky vznikají na s a na
late sousedech již zpracovaných vrcholů B_1. Všechny takové
vrcholy patří R; žádný vrchol L nedostane současnou značku.

Indukce podle BFS vrstev od s:

- s má správně RANK=1 a jako první vstoupí do fronty.
- Při zpracování v ve vrstvě D jsou všechny vrcholy B_1
  ve vrstvách <D již zpracovány. Jejich late sousedé už
  mají správnou současnou značku a RANK 1 nebo 2.
- Pro late souseda u, který už má současný RANK=1, I8
  správně skončí; u bylo zařazeno právě jednou.
- Jinak I8 předběžně zapíše RANK=2. Není-li druhý early
  soused, je to správné podle P0952. Pokud w∈L, nemá
  současný MARK=s,RANK=2, a test správně přeřadí u do 1.
- Je-li w∈R, bod x z P0952 byl zpracován ve vrstvě D−1.
  Tehdy už I8 správně určil rank(w). Test tedy přeřadí u
  do 1 právě když rank(w)=1, ekvivalentně rank(u)=1.
  Pro rank(w)=2 nechá správně rank(u)=2.

Tento krok nepředpokládá žádné ještě neověřené zařazení
ve vrstvě D: informace o w pochází ze zpracování vrstvy
D−1. Pro D=0 druhá možnost P0952 nenastává.

Při opakovaném setkání se správným RANK=2 se stejný
argument znovu shodne; nedojde k nesprávnému povýšení.
Každý nově nalezený rank 1 je připojen právě jednou na
konec LINK fronty a má vzdálenost D+1. Proto I9 udržuje
BFS pořadí. Každý vrchol B_1 má cestu od s uvnitř B_1,
a tedy bude nalezen. Každý rank 2 sousedí s B_1 a takový
soused musí být early: opačná orientace by dala rank 2
bod uvnitř I(s,v)⊆B_1. Proto budou označeny všechny
vrcholy ranku 2. Vyšší ranky I8 nikdy nenavštíví.

Při výběru w jsou potřebné early hrany u stále přítomny:
u s RANK=1 by se vyřadilo už prvním testem; dosud
nezpracované u vlastní hranu k mate neztratilo. Rank 2
žádnou hranu řezu nemá. Použití prvního či druhého
stále přítomného early souseda je tudíž oprávněné.

## I4/I5 a přesné odstranění řezu — P0954

Při vyjmutí v∈B_1 z fronty jsou všichni jeho early
sousedé v B_1 již zpracováni; mají MARK=s,RANK=1 a
vyplněný MATE. Jediný zbývající early soused je skutečný
mate(v). Opravený test I4 jej vybere jednoznačně.
I5 sloučí jeho hranu s r–s a smaže právě tuto hranu.
Hrany řezu tvoří matching, takže jde při různých v
vždy o jinou hranu a ta před daným krokem stále existuje.

P0953 navštíví právě všechny v∈B_1, tedy I5 odstraní
všechny a pouze hrany daného řezu. Sloučení v I5 je
platné podle P0950. Hrany uvnitř obou polovin zůstávají.

## I7 zachytí všechny zaniklé čtyřcyklové relace — P0955

Pro early souseda u∈B_1 jsou oba mates známy. Izomorfismus
hranic P0949 zaručuje hranu mate(u)–mate(v) v L. I7 tedy
slučuje právě protější hrany skutečného čtyřcyklu a nikdy
nepřidá neplatnou ekvivalenci. Každá hrana B_1 se takto
zpracuje při svém pozdějším konci.

Každý čtyřcyklus, který zasahuje L i R, má dvě protější
hrany řezu h a jednu hranu v každé hranici. Relaci jeho
dvou hran řezu zaznamená I5; druhou relaci zaznamená I7.
To jsou všechny čtyřcykly, které po řezu zmizí. Čtyřcykly
uvnitř L nebo R zůstanou příslušnému rekurzivnímu zpracování.
Prvky struktury ekvivalencí zůstávají existovat i po
odstranění odpovídajících hran z adjacency listů.

## Celá 77(e): rekurze, ukončení a master list — P0956

Silná indukce podle počtu vrcholů živé komponenty C:
kořen r už byl zapsán (nebo je původní a); všechny ostatní
vrcholy C dosud na master listu nejsou. Pro jediný vrchol
I1 ihned skončí. Jinak zvolené s je nové; I2 jej právě
jednou zapíše s rodičem r. To zaručuje i čerstvost jeho
MARK značky použitou v lokálním důkazu.

I3–I9 rozdělí C na dvě menší neprázdné konvexní části
P0954. I10 dokončí R s kořenem s: indukčně zapíše všechny
R\{s} právě jednou a smaže její vnitřní hrany. Žádná její
hrana se již nevrátí. Pokračování I1 pracuje pouze s L,
se stejným kořenem r; indukce platí i pro tento menší zbytek.
Každá fáze zmenší živou komponentu a každé rekurzivní
volání má menší počet vrcholů, takže celý algoritmus končí.

Tak vznikne přesně n−1 záznamů, každý vrchol kromě a
právě jednou jako s_j; jeho rodič r_j už má dřívější
záznam nebo je a. Master list je proto orientovaný
spanning tree. Mimo právě zpracovávané C se nic nemění.
Po dokončení se smažou všechny původní hrany právě jednou.

P0955 a indukce zachytí všechny čtyřcyklové relace,
P0954/P0955 přitom přidávají jen správné. Jejich tranzitivní
uzávěr tedy dává přesně celé třídy P0950. To uzavírá
správnost klasifikace hran i celé 77(e).

## H1 a H3: výstupní štítky a všechny krajní případy — P0957

BFS z a dává vzdálenosti; izometrie P0945 vylučuje hranu
mezi stejnými vrstvami. H1 proto každou hranu správně
rozdělí na early/late a žádnou možnost neopomene.
Inicializace na singleton třídy je přesný nejjemnější
počáteční stav pro pozdější platná sloučení.

V H3 je r_j vždy již označeno. Hrana r_j–s_j je podle
P0951 orientována od a a mění právě svou třídní souřadnici
z 0 na 1. Zkopírováním l(r_j) a právě touto změnou tedy
vznikne přesné teoretické l(s_j). Indukce v pořadí master
listu dokazuje všechny štítky. Zvolené číslování tříd
určuje jen permutaci sloupců.

Pro n=1 je j=0, t=0 a jediný štítek je prázdný řetězec;
I1 ihned skončí a H3 nemá krok. Vstup n=0 nemá zdroj a,
takže není vstupem formulovaného algoritmu. Počáteční
null je zvláštní hodnota odlišná od všech vrcholů.

## Celá 78: k návštěv znamená nejméně 2^k vrcholů — P0958

Při každé návštěvě v v I4 se odstraní jiná early hrana
v–u_j. Každý soused se liší právě v jednom bitu; dvě
různé hrany u v nemohou mít stejnou souřadnici díky
injektivitě štítků. Každý z těchto k bitů je v l(v)
roven 1, protože u_j je early vzhledem k a=0.

Po přeuspořádání souřadnic tedy

    l(v)=α1^k,
    l(u_j)=α1^(j−1)01^(k−j), 1≤j≤k.

Pro libovolné dva existující štítky αβ,αβ' platí

    m(αβ,αβ',l(a))=α(β AND β').

V části α většina dvou stejných bitů ponechá α, ačkoli
l(a)=0. V posledních k pozicích je to bitový AND.
Postupným průnikem příslušných u_j získáme αβ pro
každou množinu nulových pozic β; prázdný průnik je v.
Všechny tyto mediány jsou skutečné vrcholy grafu,
nikoli pouze formální vektory. Je jich 2^k různých,
tedy n≥2^k a k≤floor(lg n). Pro k=0 je tvrzení n≥1.

## Stránky, zdroje a zbývající náklady

Celá p69 má nyní argumentovou mapu: Corollary C/příklad
P0942, čtyřcykly a jedinečnost P0943–P0950, všechny H1–H3
P0951–P0957. P548 je úplná: zbytek 75(d–f) P0919–P0922,
celá76 P0876 a všechny části77 P0947–P0956.

Primární vydavatelské archivy potvrzují Jha–Slutzki,
Ars Combinatoria34 (1992),75–92 a článek Hagauer–Imrich–
Klavžar v TCS215 (1999),123–136; záznamy viz
`sources/median-label-algorithm-bibliography.json`.
Původní historické algoritmy nebyly znovu celé přezkoušeny;
konkrétní vazba tištěného H na jednotlivá historická
zlepšení je bibliografická výjimka. Zde je dokázán H
v knize, nikoli rozpoznávací algoritmy těch článků.

Všech pět vrstev errat pro H/I/77–78 prohledáno;
známé opravy jsou výslovně použity, nový nález nevznikl.
P70 zatím není celá uzavřená: počet hran79, detailní
realizace ceny I7/slučování a tabulka průběhu následují.
78 dokazuje jen omezení počtu návštěv; samo o sobě
nenahrazuje důkaz celkové časové složitosti.
