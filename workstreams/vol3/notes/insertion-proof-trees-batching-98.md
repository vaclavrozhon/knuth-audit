# §5.2.1: stromy a dávkové vkládání98

2026-11-07. P0895–0899. Originál98/file109 zobrazen. Žádný běh ani
nový nález. Dosavadní soupis pěti vrstev `insertion-errata-review.json`
obsahuje na98 pouze jazykovou změnu odkazu na5.2.4 z2000.

## P0895–0896: co přesně dovoluje shrnutí předchozích metod

Pro dvousměrné vkládání přebírám P0704–0711: součet průměrných
vzdáleností dává vedoucí N²/8 přesunů. Prattových O(N log²N)
porovnání/přesunů je již obecně doloženo P0812–0824. Pro list insertion
P0885–0888 dávají E B=N(N−1)/4 a počet porovnání B+N−1−A,
tedy N²/4+O(N). Žádný původní záznam se nepřemístí. Inicializace
zapíše dva linky a každé z N−1 vložení další dva, celkem2N.

Samostatné tvrzení „about N^(7/6), for N in a practical range“ nemá
na98 určený rozsah, přesnost aproximace ani experimentální podklady.
P0852 již přesně vymezil související empirické mezery. **P0896 partial**
pro tento konkrétní praktický fit; nejde o vyvrácení asymptotické věty
ani nový nález. Částečný empirický údaj brání uzavření celé98.

## P0897: celý Wheelerův obrázek a invariant

Každý uzel obsahuje vzestupnou posloupnost; jeho podstrom v mezeře
(a,b) obsahuje pouze klíče striktně mezi a,b. Nové minimum/maximum
daného uzlu přidáme na příslušný konec, pokud neporuší interval od
rodiče. Klíč uvnitř uzlu jde do jediné příslušné mezery; neexistující
podstrom založí jako singleton, jinak postupuje rekurzivně. Není třeba
posunout žádný dřívější záznam. Klesá konečná zbývající hloubka
existujícího stromu; v prázdné mezeře vložení skončí. Indukce zachová
všechny intervaly a inorder průchod vrací právě všechny klíče seřazeně.
Jde o popsanou abstraktní strukturu, ne odhad alokátoru proměnných uzlů.

Všech16 příchodů Table8:

1. 503 založí kořen.
2. 087 se přidá vlevo a512 vpravo.
3. 061 se přidá vlevo a908 vpravo: kořen je061,087,503,512,908.
4. 170 založí dítě v(087,503);897 dítě v(512,908).
5. 275 rozšíří první dítě vpravo,653 druhé dítě vlevo.
6. 426 rozšíří první dítě vpravo,154 vlevo.
7. 509 založí dítě v(503,512).
8. 612 rozšíří dítě v(512,908) vlevo.
9. 677 založí dítě v(653,897),765 je rozšíří vpravo.
10. 703 založí jeho dítě v(677,765).

Tedy vedle kořene jsou154,170,275,426; singleton509;612,653,897;
pod posledním677,765 a pod nimi703. To jsou všechny hodnoty, uzly,
mezery a spojení Fig13. Šipky ukazují na původní zakládací hodnotu
uzlu, ne nutně jeho pozdější levý konec; například na170 a897.
Příklad má různé klíče. Obecnou stabilní variantu lze definovat na
lexikografických párech(klíč,původní index).

## P0898: strom skutečně umožňuje N log N bez přesunu záznamů

U obyčejného binárního vyhledávacího stromu je nový záznam listem
v první prázdné větvi odpovídající porovnáním. Intervalový invariant
právě dokazuje správnost; změní se jeden rodičovský link a inicializují
se dva nulové linky. Žádný záznam se nepřemístí. Inorder výstup je
lineární, bez dalších porovnání klíčů. Pro rovnoměrné pořadí různých
klíčů je hodnost j předkem k právě tehdy, když je j první vloženou
hodnotou z uzavřeného intervalu hodností mezi j,k. Pravděpodobnost
je1/(|j−k|+1): první taková hodnota oddělí či zachová jejich cestu.
Součet očekávaných hloubek, tedy všech porovnání při vkládání, je

    2 Σ_(d=1)^(N−1) (N−d)/(d+1)
      =2(N+1)H_N−4N =Θ(N log N).

N=1 dává0. Seřazený vstup pro obyčejný strom dává N(N−1)/2;
průměrný argument se proto nevydává za jeho nejhorší případ.

Existenci varianty s garantovanými O(N log N) porovnáními lze navíc
doložit bez dovozu dosud nezkontrolované kapitoly6.2.2. Udržujme váhy
podstromů a podmínku, že každé dítě má nejvýše3/4 váhy rodiče.
Po vložení přestavíme porušené podstromy: inorder sebereme jejich
adresy a rekurzivně vybereme prostřední adresu za kořen. Přepisují se
jen linky, záznamy zůstávají na místech; nové klíčové porovnání netřeba.
Každý přestavěný uzel má dítě nejvýše poloviny své váhy. Před dalším
vložením je hloubka≤log_(4/3)N+O(1), tedy samotné hledání potřebuje
O(log N) porovnání i v nejhorším případě.

Ani cenu přestaveb nemusíme skrývat. Podstrom založený/přestavěný
s velikostí n₀ má každé dítě≤n₀/2. Po t dalších vloženích má velikost
n=n₀+t a dítě≤n₀/2+t. Porušení3n/4 vyžaduje t>n₀, tedy t>n/2.
Lineární přestavbu tak zaplatí konstantní kredit za každé z těchto
t vložení do podstromu. Jedno vložení ukládá kredity jen na své
O(log N) cestě. Přestavba předka resetuje dotčené kredity a vytvoří
znovu vyvážené podstromy; případné zahazování kreditů neškodí horní
mezi. Celkem O(N log N) práce a linkových změn, nulový počet přesunů
záznamů. Pomocná tabulka adres spotřebuje nejvýše O(N) místa.
To dokládá existenční shrnutí98; celý následující6.2.2 se tím neuzavírá.

## P0899: dávka dvou klíčů, hranice i odkaz do svazku2

Nechť prvních N−2 záznamů je seřazeno, N≥2. Dvě nová čísla seřadíme
jedním porovnáním x≤y. Od pravého konce slučujeme starý seznam
s(x,y) do jeho dvou volných koncových míst. Každý starý záznam>x
se zkopíruje právě jednou: o1 či2 místa. Po umístění obou nových
záznamů zůstává prefix≤x beze změny. Nikdy se nepřepíše nepřečtený
záznam, protože cíl leží o počet dosud neumístěných nových záznamů
napravo od starého zdroje. Index starého nebo nového zdroje při každém
kroku klesá; nula se otestuje před čtením. Pro rovné klíče umísťujeme
zezadu nejprve novější, což zachová stabilní pořadí.

Je-li Q počet starých záznamů>x, provedeme Q přesunů starých,
dva zápisy nových a Q+O(1) porovnání (nejvýše dvě porovnání končí
vložením nového klíče). Pro náhodné různé klíče je každý starý klíč
větší než minimum dvojice nových s pravděpodobností2/3, podle své
rovnoměrné relativní hodnosti ve trojici. Linearita dává

    E Q=2(N−2)/3,

tedy přesně žádané2N/3+O(1) pro porovnání i přesuny. Dvě samostatná
vložení mají průměr (N−2)/2+(N−1)/2=N−3/2 přesunů starých;
jejich další režie je O(1). N=1000 je obyčejné dosazení, nikoli
nový distribuční předpoklad. Pro N=2 není starý prvek a důkaz platí.

Odkaz3.4.2-5 je otázka na poslední vybranou pozici při rovnoměrném
vzorku. Originál svazku2 má zde skutečný offset+12:146/file158
a odpověď591/file603, oba obrazy v `images/vol2-sampling-cross-reference-*`.
Pro vzorek velikosti n je Pr(T=k)=binom(k−1,n−1)/binom(N,n),
a k binom(k−1,n−1)=n binom(k,n). Součet hockey-stick tudíž dává
E T=n(N+1)/(n+1), jak uvádí odpověď. Pro n=2 a čtení z opačné
strany je počet projitých pozic včetně obou nových2(N+1)/3;
odečtením dvou dostaneme opět E Q=2(N−2)/3. Odkaz je věcně správný.

Obecná rada dávkovat není univerzální optimální věta. Její uvedený
příklad je právě dokázán; opakované slučování dvou seřazených dávek
je definice přechodu k merging, jehož celý algoritmus přijde v5.2.4.

## Bibliografická výjimka

Rychlé dohledání primárních Douglas1959 a Berners-Lee1960 skončilo
nedostupnými DOI10.1093/comjnl/2.1.1 a10.1093/comjnl/3.3.174.
Sekundární katalogy nejsou důkazem tvrzení o prvenství či letech1957/1958.
Tyto historické údaje a podrobnosti původní Wheelerovy implementace
neověřeny; matematický obrázek a uvedené konstrukce jsou nezávislé.
