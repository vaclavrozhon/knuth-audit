# Souvislý průchod §2.2.3 — 5. listopadu 2026

Přímo přečteny celé originály255–273 a545–551. Úvod a diagram254
byly přečteny s předchozí sekcí. Na273 a551 začíná další sekce;
její obsah zatím nedostává uzavřené stránkové pokrytí. Revidovány
všechny obecné důkazy v `parallel/linked-allocation/notes/`,
původní erratum s náhradní odpovědí13, věta1.3 v autorově kopii
Brightwell–Tetali a tabulka počtů v Brouwer–Christensen2017.
Starších4494 kontrol,448 MIX běhů,160 alokačních případů ani
úplná herní analýza nebyly opakovány.

## Spojové operace a hranice

Rozklad paměti na živé disjunktní seznamy a fond AVAIL zachovávají
alokace i vrácení jednoho uzlu. Nový uzel délky c z POOLMAX smí
končit přesně na SEQMIN; překrytí začíná až při POOLMAX>SEQMIN.
Tvrzení o nejmenším poolu označuje odložené zprovoznění paměti,
nikoli kompakci po každém uvolnění. Časové srovnání spojových
a sekvenčních operací je v daném modelu, s adresou předchůdce
známou při konstantním vložení či vyjmutí.

Zásobníkové vložení permutuje tři odkazy AVAIL,LINK(P),T;
vyjmutí provede opačný cyklus po záchraně obsahu. MIX kód stojí
17u, tedy osm paměťových operací a jeden skok. Návrat OVERFLOW
na rJ−2 znovu načte novou AVAIL. INSERT/DELETE zachovávají
předepsané registry a rozlišují oba návraty DELETE; známá oprava
INFO(rI1)→INFO(rI3) je v komentáři, ne v instrukci.

Prázdná fronta má F=Λ,R=LOC(F), přičemž F je skutečně uložené
v poli LINK. Po posledním vyjmutí se R musí obnovit. Vkládání
vpředu mění R jen u původně prázdné fronty; odebírání zezadu
hledá předchůdce od fiktivního uzlu LOC(F), takže zvládne
i singleton. Při vynechání koncového LINK(R)=Λ se nejprve
testuje staré F=R a teprve jinak čte jeho následník. Poznámka
o garbage collection se vztahuje k dané konvenci odkazů.

Obrácení odděluje obrácený prefix a dosud nedotčený suffix;
jejich sjednocení jsou přesně původní uzly. Tři střídající se
indexové registry poskytují požadovaných5n+O(1) časových jednotek;
vytištěná jednodušší varianta má7n+6. Vrácení celého seznamu
potřebuje při známém konci konstantní počet změn odkazů, jinak
lineární hledání konce. Případ prázdného seznamu je oddělen.

Obě varianty úlohy30 jsou správné: původní nepoužívá zastaralé R
při F=Λ; náhrada2021 vlastní prázdný koncový uzel R a rozpoznává
prázdnost pomocí F=R. Obsah tohoto prázdného uzlu není položkou.
Náhrada úlohy je doplněk, nikoli důkaz chyby původního řešení.

## Částečná uspořádání a topologické třídění

Přísná a reflexivní definice jsou ekvivalentní; asymetrie přísné
relace plyne z transitivity a irreflexivity. Antisymetrie reflexivní
relace neplyne z ostatních vlastností. Úloha9 rozlišuje biologickou
genealogii, kontextově podmíněná volání a tranzitivní závislost.
Záporné násobky i parita dávají uvedené protipříklady. Závorkové
x mod y v9(c) se při y=0 nevyužívá jako definice dělení nulou;
slovní násobnost je rozhodující. Píseň v odpovědi9 je kulturní
odkaz, nikoli další předpoklad matematického argumentu.

Jedinečnost lineárního rozšíření plyne ze srovnatelnosti sousedů.
Přidání orientace nesrovnatelné dvojice a Zornovo lemma dávají
obě rozšíření i pro nekonečnou množinu. Iredundantní generátor
musí být právě množina pokrytí; na konečné množině generuje vše,
na Z∪{∞} nikoli. To potvrzuje rozdíl mezi „právě jeden“ a
„nejvýše jeden“ v odpovědi15. Permutace řádků i sloupců relace
podle topologického pořadí správně dává horní trojúhelníkovost.

Obrázky6–8 a všech deset vstupních hran souhlasí. T udržuje
počet ještě neodstraněných vstupních hran; COUNT se přepíše na
QLINK až při nule. Duplicitní hrany jsou započteny i odečteny
se stejnou násobností. Zachování F do konce T6 je nezbytné:
předčasné T7 selže už pro jedinou hranu1→2. Zbylý neprázdný
graf bez nulového stupně obsahuje cyklus. Čas a paměť jsou
O(n+m). Užití zásobníku místo fronty správnost nemění.

Obě topologická pořadí193274586 a912374586 splňují vztahy;
liší se směrem počátečního průchodu T4. Všech52 pořadí na546
tvoří disjunktní skupiny2+4·8+6·3 a odpovídají rekurzi přes
aktuální minima. Program T správně hlídá páskové hranice,
sentinel−1 za bufferem, čekání na přenos a koncovou nulu.
Frekvence a součet32m+24n+7b+2c+16 používají vydání I/O za1u,
vynechávají čekací smyčky a konečný HLT. Platí pro úspěšný
vstup s n≥1; odpověď22 výslovně požaduje kontrolu0<n, takže
nulový počet objektů zde není nový protiklad časové tabulky.
Plné vstupní slovo se má validovat před dvoubajtovým načtením.

Diagnostika cyklu vytvoří funkci předchůdce na zbylých vrcholech,
prvním opakováním najde cyklus a smaže značky přesně při jeho
vypisování. Všechny vytištěné sousední dvojice jsou vstupní
hrany v opačném směru. **C0040 zůstává confirmed:** konkrétní
poznámka na549 předpovídá jiný cyklus. Sestupné k=9,…,1
nechá nejmenšího předchůdce, tabulku(9,9,1,7,7,4,3,2,6),
a výstup1,9,6,4,7,3,1. Tištěné9,6,8,5,9 dává vzestupný
průchod. Oba cykly jsou platné; algoritmus touto vadou netrpí.

## Booleova mřížka a přesný rozsah asymptotiky

Dolní mez L_n=product binom(n,k)! vzniká řazením po vrstvách.
Náhodný maximální řetěz dává pro antichain součet vah
1/binom(n,k) nejvýše1. Výběr dostupného minima podle těchto
vah dává každému rozšíření pravděpodobnost alespoň1/U_n,
kde U_n=product binom(n,k)^binom(n,k). Tím je stará horní
mez dokázána obecně, bez nutnosti plného Sha–Kleitman1987.

V entropickém důkazu silnější meze byly zkontrolovány kladné
stupně sousedních vrstev, identita počtu hran, podmíněná
Shearerova nerovnost, Jensenův krok a všechny mocniny v Q_j.
Limitní přechod po násobcích s zachovává přesné počty celých
hodnot; multinomická pravděpodobnost omezená1 ospravedlňuje
poslední faktorovou nerovnost. Pro B_n vyjde
r=(2^(n+1)−2)/(n+1) a B_n=(2en2^n/r)^r L_n, n≥1.
Případ n=0 má počet1 přímo.

Stirling a binomické momenty dávají
ln L_n/2^n=n ln2−(ln n)/2−(ln(2pi))/2+ln2−3/2+O(1/n).
Mez B_n přidává O(log n/n). Je tedy ověřena ostrá
**logaritmická** asymptotika, nikoli ekvivalence a_n/L_n→1.
Historický poměr U_n/L_n má logaritmus
2^n−n²/4+O(n log n); původní tisk i neúplná oprava2001
jsou odlišeny od náhrady2018, která tento výrok vypustila.

**C0036 zůstává confirmed pouze v erratu2018.** Nově přímo
porovnaný obraz all1-pre16 má exp(B_n), zatímco věta1.3
Brightwell–Tetali pouze B_n. exp(B_n) je nadále horní mez,
ale nezlepšuje U_n pro žádné n≥1. Ruční nerovnosti při n=16
dávají B16<U16<exp(B16). Naší původní straně547 tuto
exponenciálu nepřipisujeme. Její vlastní staré asymptotické
chyby jsou již známé X0256.

Počty0–5 mají přijatý vlastní dynamický výpočet přes ideály.
Hodnoty6–7 včetně zaokrouhlení6.305×10^137 jsou porovnány
s původní tabulkou autorů. Velké výpočty těchto dvou hodnot
výslovně znovu nereprodukujeme; nejde o naše nezávislé počty.

## Zbývající algoritmy

25: vnější třídění po vrstvách, zdvojování ukazatelů pro řetěz
a obecné max-plus zdvojování cest mají obecné konstruktivní
důkazy. Poslední varianta potřebuje O(n³+m) pracovních záznamů;
malý počet průchodů se nezaměňuje za malý objem přenosů. Nápověda
do svazku3 je ověřena v jejím rozsahu. Výzkumné „as efficient
as possible“ nemá přesně fixovanou optimalizační metriku;
netvrdíme globální optimalitu.

26–27: značení hlaviček0→2 a−1→1 odliší už navštívené
podprogramy, zastaví se i při cyklech a vybere přesnou
dosažitelnou množinu. Druhá fáze respektuje pořadí pásky.
ENT2 FIRST je správné, protože první dereference je až v B4.
Příklad dává základy2400,2430,2450,2510,2530 a konec2730.
Známá oprava skoku při N=0 je nutná pro inicializaci rI1.

28: čítače následníků a fronta předchůdců mají O(v+e)
analýzu; klesající rank dokazuje konečné vítězství, nejen
lokální příznak W. Zbylé neoznačené stavy mají bezpečné
pokračování. U vojenské hry je prostor1320 rozestavení,
2640 stavů s hráčem na tahu. Přijatý certifikát všech10752
tahů podporuje uvedený cyklus i jedinou odpověď A do L.
Rank23 standardního startu znamená nejvýše12 tahů A.
Při výhře B opakováním nestačí náhodně volit libovolné L:
pomůže klesající rank nebo výslovné zahrnutí historie.

## Bibliografie, známé opravy a uzavření

Nový krátký webový pokus má samostatný protokol. Kahn1962
i Sha–Kleitman1987 znovu vrátily403. Přeskakujeme jejich
plné znění a Winning Ways3, kap.21. Úlohy13 a28 se mohou
změnit partial→checked: matematika má samostatné důkazy,
u hry navíc původní Lucasův pramen. Bez těla Kahna se
nepotvrzuje technický dovětek o nepoužití queue links.
Bez Sierpiński1928 s.158 se neuzavírá historické prvenství
Szpilrajna; jeho samotná věta i údaje o kolezích mají primární
doklad. Hlavní text na268 proto zůstává partial.

Výslovně odděleny též nedoložená Dijkstrova klavírní anekdota
na sdílené545 a kulturní odkaz na píseň v546. Nejde o
matematické předpoklady; u545 zůstává historická mezera.
Píseň jako bibliografický dovětek přeskakujeme.

Nový výpis čtyř vrstev zachovává i formální změny. Diagram256
postrádá číslo(3), na které odkazuje úloha7; tato známá oprava
je obsahově lokalizovatelná. Náhrada věty na260 naopak zachovává
stejné správné F=Λ,R=LOC(F), nejde o nalezenou chybu invariantu.
Oprava jednotky na258, COUNT[k] na266, bibliografický název
a křížový odkaz na268, komentář545 a N=0 na550 jsou přesné.
Nová verze30 nepobarvuje původní273/551 jako vadné algoritmy.

Výsledek: všech30 úloh matematicky uzavřeno s uvedenými
pramennými a výpočetními výjimkami. Nový neznámý nález:0.
Hlavní text partial kvůli vyjmenovaným tvrzením na268.
Následuje §2.2.4 na273.
