# §4.3.3-15: online násobení a rozsah známých mezí

Kontrola 2.11.2026. Zadání na318, odpověď na634 a erratum7.8.2020
byly vizuálně přečteny. Úloha má obtížnostM49 a ptá se na výzkumný
problém. Uzavření auditu znamená kontrolu uvedených výsledků,
modelů a citací; neznamená vyřešení optimální online složitosti.

## Definice a původní horní mez

Online zde znamená, že k-tý bit součinu od nejnižší pozice musí
být vydán před přečtením (k+1)-ních bitů obou operandů. Cena se
počítá do vydání požadovaného počtu bitů, včetně všech pomocných
výpočtů. Není to omezení na jeden výpočetní krok mezi dvěma bity.

Fischer–Stockmeyer, *Fast On-Line Integer Multiplication*,
MIT-LCS-TM-045, květen1974, tištěná str.3 (PDF7), Theorem1,
uvádí převod offline algoritmu s cenou F(n) na online algoritmus
s cenou O(F(n) log n), za podmínek

```
n <= F(n) <= F(2n)/2 <= c F(n)
```

a monotónnosti F. Pásky jsou v článku výslovně jednorozměrné.
Vydavatelský abstrakt článku JCSS9(3),317–331 potvrzuje tutéž
větu i dosazení F(n)=O(n log n log log n). Tím je knižní horní
mez O(n log^2 n log log n) doložena primárním zdrojem.

Princip převodu je rozvrhnout součiny již dostupných bloků
v geometrických velikostech. Na každé velikosti b vzniká O(n/b)
blokových součinů; rozvrh zajišťuje jejich dokončení před prvním
výstupním bitem, který je potřebuje. Je-li F(b)/b neklesající,
každá z O(log n) velikostí stojí O(F(n)), včetně skládání. Toto
je vysvětlení časové meze citované konstrukce, ne nová samostatná
implementace jejího páskového rozvrhu. Vizuálně byly přečteny
abstrakt a úvod včetně přesného Theorem1, nikoli celý jeho důkaz.

Pro ukazatelový stroj se stejná bloková konstrukce kombinuje
s lineárním offline násobením z úlohy12 a dává O(n log n).
Dolní mez Omega(n) plyne už z počtu vydaných bitů. Z páskového
výsledku níže nelze odvodit silnější dolní mez pro tento model.
Pole souběžně pracujících automatů z částiE navíc vydává jeden
bit za takt, ale používá rostoucí počet současně činných modulů;
není to sekvenční výpočet s konstantním počtem pásek.

## Dolní mez a C0106

Paterson–Fischer–Meyer, *An Improved Overlap Argument for On-Line
Multiplication*, MIT-LCS-TM-040, leden1974, rozlišuje dva závěry:
pro širší třídy strojů Omega(n log n/log log n), pro vícepáskové
Turingovy stroje s jednorozměrnými páskami Omega(n log n).
Jde dokonce o střední čas, takže závěr platí i pro nejhorší vstup.
Přesné rozlišení modelů je na tištěné str.7 (PDF9), Theorem2
na str.21 (PDF23). Abstrakt, tyto stránky a navazující rozšíření
na str.22–23 byly přečteny v originálu.

Stejný rozdíl výslovně uvádí také Fischer–Stockmeyer na str.3
(PDF7). Harvey–van der Hoeven2021, str.2, uvádí Omega(n log n)
a odkazuje na stejný článek. Knižní slabší mez je tedy platná,
ale pro běžný páskový model není správné označit ji za nejlepší
známou. To je potvrzené citační/modelové pochybení C0106;
netvrdíme, že slabší nerovnost je sama o sobě nepravdivá.

## Doplnění2014/2020 a C0107

V erratu7.8.2020 je vizuálně přečteno

```
R_*(n) = n ln n exp(sqrt(ln4 * ln ln n)) sqrt(ln ln n).
```

Poslední odmocnina je násobek mimo exponenciálu, nikoli jmenovatel.
Změna báze vnějšího logaritmu nemění řád, ale uvnitř exponenciály
je potřeba zachovat přirozený logaritmus a jeho konstantu.

Revidovaná autorská verze van der Hoevenova článku *Faster relaxed
multiplication* z29.4.2014 tuto funkci definuje na str.2. Sekce3–4
odvozuje O(R_*(n)) v **algebraickém modelu**: každá operace
v základním okruhu s vhodnými kořeny jednotky stojí jeden krok.
To nelze bez dalšího dosadit jako počet bitových kroků na pásce.

Sekce8 pracuje s p-adickými čísly, tj. cifernými proudy v bázi p,
a výslovně započítává bitovou cenu. Theorem17 na str.7 říká

```
R_p(n) = O(R_**(n) log(p) L log L),
R_**(n) = R_*(n) log log n,
L = log(log n + log p).
```

Pro pevné p=2 z toho přímo plyne
O(R_*(n) (log log n)^2 log log log n), nikoli doslovně O(R_*(n)).
Převod v důkazu na str.8 používá bloky a další celočíselné násobení;
čteny jsou tyto stránky i definice a věta2 na str.3. Úplný důkaz
všech pomocných vět o obecných okruzích zde nebyl auditován.

To zatím vedeme jako **C0107candidate**: chybí doložený přechod
k přesné bitové mezi z errata. Slabší horní mez z článku nedokazuje,
že ostřejší mez je nemožná. Může existovat specializace, kterou
krátká citace neuvádí. Bez ní je bezpečnou shrnující formulací

```
O(n log n exp((sqrt(ln4)+o(1)) sqrt(ln ln n))).
```

Tuto podobu uvádí také spoluautor van der Hoeven v článku2021,
str.2. Polynomické faktory v log log n se do o(1) absorbují,
protože log log log n / sqrt(log log n) jde k nule.

## Zdroje, errata a omezení

Primární PDF a kontrolované stránky jsou v manifestu
`../sources/fast-context-sources.json`. Úplný přehled nejlepších
výsledků do2.11.2026 nebyl prokázán; uvedené horní meze jsou
ověřené historické výsledky, nikoli tvrzení o dnešním optimu.
Vyhledávání navíc vrátilo tvrzení o novém offline preprintu2026,
ke kterému se nepodařilo otevřít primární stránku. Nepoužíváme
jeho závěr ani tvrzení ze sekundárních blogů.

Všechny čtyři vrstvy errat byly prohledány podle634, čísel úloh,
jmen autorů, online a logaritmických faktorů. Oprava7.8.2020
mění horní mez; dolní mez nepřepisuje. Žádné další relevantní
erratum nebylo nalezeno. Kontrola dostupných zdrojů nepotvrzuje
poslední fyzický dotisk, prvenství nálezů ani nárok na odměnu.
