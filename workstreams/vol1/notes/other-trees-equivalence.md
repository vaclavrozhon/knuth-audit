# §2.3.3: ekvivalence, Algorithm E a úlohy 7–11

Přečteny originály pp. 353–355, 360–361 a 576. Ekvivalence je reflexivní,
symetrická a tranzitivní relace; dané dvojice určují nejmenší takovou
relaci, která je obsahuje. Její třídy jsou komponenty neorientovaného
grafu vstupních dvojic. Toto grafové vyjádření slouží i jako nezávislé
srovnání v konečných kontrolách.

## E a úlohy 7–10

Pole PARENT tvoří orientovaný les: nula označuje kořen, kladná hodnota
rodiče. Po každé dvojici jsou jeho komponenty přesně dosavadní třídy
ekvivalence. Na začátku to platí pro singletony. E3 konečně vystoupá
k oběma kořenům; pokud jsou stejné, nic se nemění, jinak E4 připojí
první kořen ke druhému. Spojí tím právě dvě různé komponenty a nemůže
vzniknout cyklus. Indukce dokazuje algoritmus i následný dotaz z úlohy
8: dvě položky jsou ekvivalentní právě při shodě kořenů.

Původní formulace E3 opakuje krok; novější dvě výslovné while smyčky
z 7. července 2023 jeho význam vyjasňují. Obě podoby při tomto čtení
skončí v kořenech. Nejde o nový nález.

V příkladu dvojice 1~5,6~8,7~2,9~8,3~7,4~2,9~3 dávají po dokončení
PARENT=(5,0,2,2,0,8,2,2,8). Před zpracováním poslední dvojice jsou
třídy {1,5}, {2,3,4,7}, {6,8,9}; to řeší 7 a 9. Diagram má kořeny
5 a 2, s hranami právě určenými tímto polem.

Původní E má kvadratický nejhorší případ: dvojice (1,2),(1,3),...,(1,n)
postupně prodlužují řetězec a hledání kořene 1 pro i-té připojení
projde i−2 hran. Součet je (n−1)(n−2)/2.

Pro úlohu 10 uložíme u kořene zápornou velikost komponenty a vždy
připojíme menší komponentu k větší, při rovnosti libovolně. Kořenová
velikost se aktualizuje součtem. Pokaždé, když se hloubka pevného uzlu
zvětší, jeho komponenta alespoň zdvojnásobí velikost. Proto má hloubku
nejvýše floor(log_2 n) a jedna dvojice stojí O(log n). Záporné kořeny
se v E3 rozpoznají testem PARENT>0, takže není třeba další pole.

Komprese cest z druhé části odpovědi přepojí navštívené uzly kromě
konečného kořene přímo k němu. Na původní cestě ke kořeni žádný cyklus
nevytvoří a všechny uzly zůstávají v téže komponentě. Při současné
úpravě podle velikosti zůstávají kořenové velikosti správné. Výrazně
lepší amortizované meze zde nejsou tvrzeny bez důkazu; knižní odkaz
byl opraven z §7.4.1 na §7.4.1.1, který není v dodaných hotových svazcích.

## Úloha 11: překryvy polí

Každý uzel P označuje jedno pole NAME(P). Je-li rodičem Q a hranový
posun DELTA(P)=d, význam je NAME(P)[t]=NAME(Q)[t+d] pro všechna t.
LBD,UBD v kořeni vymezují nejmenší souvislý interval, který obsahuje
všechny deklarované buňky komponenty v souřadnicích kořenového pole.
Údaje o mezích u nekořenů již nejsou závazné.

Pro vstup (P,j,Q,k) vystoupáme po obou rodičovských cestách, přičítáme
hranové DELTA k příslušnému indexu a dostaneme rovnici mezi kořeny.
Jsou-li kořeny stejné, právě j=k znamená konzistenci. Jinak připojíme
Q pod P a nastavíme DELTA(Q)=j−k. Dolní mez P se stane minimem
dosavadní meze P a LBD(Q)+j−k; horní mez analogickým maximem.

Důkaz je indukcí podle počtu rovnic. Součet hranových posunů je přesný
převod souřadnic, protože každá hrana vyjadřuje překlad o konstantu.
Ve stejné komponentě už existuje jediný rozdíl počátků; nerovnost j,k
proto znamená a také postačuje k rozporu. Různé komponenty nemají
dosavadní vzájemné omezení, takže nový posun je lze spojit konzistentně.
Spojení kořenů opět nevytvoří cyklus. Posunuté minimum a maximum jsou
přesné krajní obsazené adresy; každý souvislý blok pokrývající všechny
adresy musí obsahovat celý interval mezi nimi, včetně případných děr.
To dokazuje i minimalitu přiděleného bloku.

Příklad má X[0:10],Y[3:10],A[1:1],Z[−2:0]. Z X7=Y3 plyne Y→X
s posunem 4 a meze X 0..14; ze Z0=A0 plyne A→Z s posunem 0.
Y1=A8 pak připojí Z→X s posunem −3 a meze jsou −5..14, tj. 20 míst.
A1 leží na X−2; následující X−1 je neobsazená, ale nutná mezera.
Indexy v ekvivalenci mohou být mimo deklarovaný rozsah, jak vyžaduje
zadání; určují posun, nepřidávají tím deklarované buňky.

## Kontroly

check_other_trees.py porovnává E a variantu podle velikosti s nezávislými
množinovými štítky po každém z 63 360 náhodných slučovacích kroků.
Kontroluje také zdvojnásobovací mez pro hloubky. Dalších 16 320 kroků
s posuny srovnává s nezávislou propagací celočíselných potenciálů
v grafu rovnic, včetně odmítaných rozporů, relativních posunů a přesných
mezí všech komponent. Knižní příklad je ověřen zvlášť.
Obecné důkazy výše nevyužívají konečný rozsah testů. Historické
atribuce Galler/Fischer, McIlroy a Tritter jsou odděleny v pramenných
poznámkách; matematická správnost sama atribuci neověřuje.

