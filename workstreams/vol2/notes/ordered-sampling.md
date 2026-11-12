# §3.4.2-16: seřazený náhodný výběr

Kontrola 1. listopadu 2026. Zadání na 148 a odpověď na 592 přečteny
v původní sazbě; jmenovatel tištěné meze je skutečně 2, tedy 5n/2 sond.
Správnost algoritmu a lineární řešení zadání jsou dokázány níže.
**Konkrétní obecná mez 5n/2 pro tištěné lineární sondování zůstává
partial.** Malé přesné modely ji podporují, ale nejsou důkazem.

## Model a rovnoměrnost

Z N celých čísel 1,...,N chceme rovnoměrnou n-prvkovou podmnožinu,
vypsanou vzestupně. Počet paměťových buněk i očekávaný čas mají být O(n).
Předpokládáme jednotkovou cenu celočíselných operací a jednoho přesného
rovnoměrného výběru z 1,...,N, stejně jako zadání. Pro n>N/2 vybereme
m=N−n vynechaných čísel a při průchodu 1,...,N vypíšeme doplněk;
N<2n, takže tento průchod je O(n). Případy n=0,N jsou přímé.
Dále 1<=n<=N/2 a M=2n je délka hashovací tabulky.

Nezávislé rovnoměrné pokusy odmítají již přítomná čísla. Z libovolné
aktuální k-prvkové množiny S je příští nové číslo rovnoměrné na jejím
doplňku, proto po n úspěších dostaneme rovnoměrnou podmnožinu. Střední
počet pokusů je

```text
R = sum_{k=0}^{n−1} N/(N−k) < 2n.
```

Dokonce R<2 log(2) n: při pevných n,k výraz klesá s N, a pro N=2n
jej shora odhadne integrál rostoucí funkce 1/(1−x/2) na [0,1].

## Tištěné uspořádané lineární sondování

Domovská adresa klíče x je h(x)=floor(M(x−1)/N). Z její buňky postupujeme
po jedné **klesajícími** indexy modulo M, jak stanoví svazek 3,
§6.4, algoritmus L na 526. Nula znamená prázdnou buňku.

Při pokusu vložit x: rovnost s uloženým klíčem znamená duplikát;
prázdnou buňku obsadíme; při setkání s menším klíčem oba prohodíme
a neseme dál ten menší. Jinak pokračujeme s původním klíčem.
To je algoritmus v primárním Knuthově programu, CACM 29 (1986), 367.

Invariant: před klíčem x na jeho sondovací cestě jsou pouze větší
klíče. Každá obsazená buňka se při výměně zvětšuje, takže invariant
zůstává platný pro staré klíče; přenášený menší klíč pokračuje tam,
kde skončil jeho dosud platný prefix. K duplikátu se proto dostaneme
před první výměnou a tabulka se při odmítnutí nezmění. Prázdná buňka
existuje a postup skončí.

Výsledek nezávisí na pořadí vkládání: odpovídá obyčejnému lineárnímu
vkládání klíčů **od největšího k nejmenšímu**. Největší klíč musí být
ve své domovské buňce; každý další je v první buňce své sondovací
cesty, kterou nezabírají větší klíče. To induktivně určuje celou tabulku.
Věta o jednoznačnosti je také v Amble–Knuth a odpovědi §6.4-66 na 741.
Věta „as if ... increasing order“ ve svazku 2 sama neurčuje vložení
obyčejným, nebo uspořádaným algoritmem. Není zde vedena jako chyba:
uspořádané vkládání má stejné uspořádání pro každé pořadí vstupu.

Pro výstup nestačí cyklicky otočit seznam nenulových buněk. Přesný
program používá tyto dva **filtrované** průchody:

```text
if T[0] == 0:
    output nonzero T[1], ..., T[M−1]
else:
    output T[i] with 0 < T[i] < T[0], for i=1,...,M−1
    output T[i] with T[i] >= T[0], for i=0,...,M−1
```

Důvod lze vidět při kanonickém vkládání od největšího klíče. Domovské
adresy klesají a neobtočené klíče jsou v tabulce zleva doprava vzestupně.
Když vkládání poprvé překročí nulu, nejmenší neobtočený klíč je právě
T[0]. Všechny další, menší klíče se musejí obtočit také: jejich domovské
adresy leží v již obsazeném prefixu končícím nulou. Obtočené klíče jsou
opět vzestupné podle indexu. Filtr obě části oddělí i tehdy, když se
jejich pozice prolínají. Například N=12, n=3, S={1,2,12} dává
T=[2,0,0,0,1,12]; první průchod vypíše 1 a druhý 2,12.

## Samostatný úplný důkaz lineární složitosti zadání

Pro samotné zadání lze použít tutéž monotónní adresu h, ale v každé
z M přihrádek udržovat **seřazený spojový seznam**: každý uložený klíč
má odkaz na následující klíč téže přihrádky. Seznam projdeme do nalezení
klíče nebo místa vložení. Každá přihrádka obsahuje nejvýše ceil(N/M)
možných vstupních čísel. Pro pevnou množinu S velikosti k je tedy střední
počet porovnávaných starých klíčů při jednom rovnoměrném pokusu nejvýše

```text
sum_b |S in bucket b| * |universe in bucket b| / N
 <= k*ceil(N/M)/N <= k/n.
```

Poslední nerovnost plyne z N/M>=1 a ceil(u)<=2u. Přičteme jeden přístup
k hlavičce seznamu. Pravděpodobnost úspěchu je p=(N−k)/N; odmítnutí
nemění S. Rekurence pro očekávanou cenu do dalšího úspěchu proto dává
nejvýše (1+k/n)/(1−k/N), aniž bychom předpokládali nezávislost ceny a
úspěchu téhož pokusu. Po sečtení a odhadu rostoucím integrálem:

```text
expected bucket accesses plus key comparisons
 <= sum_{k=0}^{n−1} (1+k/n)/(1−k/(2n))
 < n * integral_0^1 (1+x)/(1−x/2) dx
 = (6 log(2)−2)n < 2.159n < 5n/2.
```

Paměť M hlaviček a n uzlů je O(n); výstup prochází přihrádky a jejich
seřazené seznamy v čase O(n). Tím je požadavek zadání úplně splněn.
Tato konstanta se vztahuje k **jinému algoritmu a uvedenému počítání
operací**; nedokazuje konstantu tištěné odpovědi pro lineární sondy.

## Co přesně zbývá u tištěné konstanty

Pro tabulku množiny S definujme posunutí klíče x jako počet sondovacích
kroků od h(x) do jeho umístění, tedy (h(x)−position(x)) mod M. Označme
D(S) součet těchto posunutí a d_k jeho očekávání pro rovnoměrnou
k-prvkovou množinu. Nové vložení stojí 1+D(S∪{x})−D(S) sond;
duplikát stojí 1+displacement(x). Každý krok neseného klíče zvětší
celkový součet posunutí o jednu; návrat za jeho domovskou adresu
nenastane, protože v tabulce je prázdná buňka. Sčítáním očekávaných cen
včetně všech odmítnutých opakování dostaneme přesnou identitu

```text
expected total probes = R + d_n + sum_{k=0}^{n−1} d_k/(N−k).
```

Například obecná mez d_k<=k/2 by stačila: pravá strana by byla
nejvýše 3R/2 < 3 log(2)n < 5n/2. Běžná analýza lineárního sondování
při nezávislých rovnoměrných domovských adresách skutečně dává

```text
d_k = (k/2) * sum_{j=1}^{k−1} (k−1)(k−2)...(k−j)/M^j
    <= k(k−1)/(2(M−k+1)) < k/2.
```

Jenže zde jsou klíče vybírány bez opakování a monotónní h má přihrádky
o floor(N/M) nebo ceil(N/M) prvcích. Původní Amble–Knuth výslovně
předpokládá nezávislé rovnoměrné hashovací adresy v analyzované části
na straně 8. Přenos uvedené meze na tento konečný model zatím není
dokázán. Nejde o protipříklad ani o potvrzenou chybu knihy.

## Konečné kontroly a zdroje

[Program](../verify_ordered_sampling.py) ověřil 6150 úplných pořadí
vložení, 22834 prefixů a 22834 duplikátních dotazů pro N<=9. Doslovné
prohazování porovnává s nezávislým vkládáním od největšího klíče a
filtrovaný výstup s přímým seřazením množiny.

Další blok průměruje přes všechny k-prvkové množiny a všech N dotazů,
včetně ceny libovolně mnoha opakovaných duplikátů. Pro N<=20,
n<=min(N/2,7) jde o 304584 množin a 5491226 dotazů. Všechny výsledky
jsou přesné zlomky; největší poměr celkové ceny k n je
12844889/9529520 < 1.348, při N=17,n=7. Běh 37022 skončil 0.

Primární [Knuthův program v Bentleyho sloupku](https://cs61.seas.harvard.edu/site/pdf/p384-bentley.pdf)
byl přečten v oddílech 1–14, strana 367 také vizuálně. Primární
[Amble–Knuth, Stanford CS-TR-73-367](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/OCR/CS-TR-73-367-ocr.pdf)
byl přečten v OCR na tištěných stranách 2–9; originální matematická
formulace je nadále dostupná v uloženém scanu. Ve svazku 3 byly
strany 526,556,741 přečteny v textu i vizuálně. Žádný soubor jiného
pracovního proudu nebyl změněn.

Všechny čtyři vrstvy errat byly pro toto zadání i odpověď prohledány;
relevantní změna tištěné konstanty nebyla nalezena. Finitní model,
primární analýza a samostatný algoritmus zůstávají zřetelně odděleny.
