# Celá úloha 109: majorizační svaz, oba obrázky a dodatky

7. listopadu 2026, X0121, P1144–P1155. Originály p92–93/file109–110
a p554/file571 zobrazeny; zvlášť zvětšeny Fig. 8 a orientovaný trojúhelník.
Každá část (a)–(h) má níže obecný argument. Žádný matematický program.

Pišme A_k=Σ_(i≤k) a_i, A_0=0; α≥β v tomto souboru znamená
majorizaci A_k≥B_k pro všechna k, nikoli lexikografickou či bitovou
nerovnost. Prefixový vektor jednoznačně určuje slovo rozdíly A_k−A_(k−1).
Reflexivita a tranzitivita jsou po složkách; antisymetrie plyne právě
z jednoznačnosti těchto rozdílů. Pro n=0 je svaz jednoprvkový.

## (a) Komplement obrací pořadí

Prefix komplementu je k−A_k. Proto A_k≥B_k právě když
k−B_k≥k−A_k, současně pro všechna k. Tedy α≥β iff ¬β≥¬α.
Platí to i pro k=0 a prázdné slovo, bez podmínky na celkové počty jedniček.

## (b), (c) Skutečná existence meet a join a jejich výpočet

Položme C_k=min(A_k,B_k), D_k=max(A_k,B_k). Oba vektory začínají
nulou, jsou neklesající a jejich přírůstky jsou nejvýše 1. Pro C:
vyberme ten prefixový vektor, který dosahuje minima v k−1; jeho
další složka je nejvýše C_(k−1)+1, takže tím spíše C_k. Pro D
stačí A_k,B_k≤D_(k−1)+1. Nezápornost přírůstků obou vektorů plyne
z neklesání A a B. Proto C i D skutečně jsou prefixy binárních slov.

Pro libovolné γ je Γ_k≤A_k a Γ_k≤B_k ekvivalentní Γ_k≤C_k;
to je celá univerzální vlastnost největší dolní meze α∧β. Obdobně
Γ_k≥A_k a Γ_k≥B_k iff Γ_k≥D_k dokazuje nejmenší horní mez α∨β.
Nejde jen o souřadnicový návrh, který by nemusel zůstat v doméně.

Algoritmus udržuje A_k, B_k a předchozí minimum či maximum a vypisuje
jejich rozdíly. Čte každý bit jednou: O(n) operací se slovy délky
O(log(n+1)) bitů a O(1) pomocných slov mimo výstup. Opačná cesta
α∨β=¬(¬α∧¬β) plyne z (a) a rovněž souhlasí s odpovědí.

## (d) Obě distributivity a smíšené radixy

Na lineárně uspořádaných číslech min distribuuje přes max a naopak.
Například pro b≤c je min(a,max(b,c))=min(a,c), zatímco
max(min(a,b),min(a,c))=min(a,c); případ c≤b je symetrický.
Duální argument dokazuje druhou identitu. Použitím v každé prefixové
souřadnici a jednoznačností rozdílů dostáváme obě rovnosti (d).

Dodatek dovoluje na pozici j číslice 0≤a_j<m_j s pevnými kladnými
celočíselnými radixy m_j. Položme r_j=m_j−1. V §(b,c) nahradíme
horní mez přírůstku 1 hodnotou r_j: při min zvolíme vektor, který
dosáhl předchozího minima, a při max použijeme meze obou vektorů.
V obou případech je nový přírůstek mezi 0 a r_j. Uzavření, univerzální
vlastnosti a distributivity tedy platí beze změny. Radix 1 dává pevnou
nulu a nepůsobí problém. Radix 0 by nebyl radixem neprázdné domény
a není součástí tohoto tvrzení. Nikde se nepředpokládá společný radix.

## (e) Úplná charakterizace pokrytí

Poklesy jsou právě dva typy:

* poslední bit 1 změnit na 0;
* sousední 10 změnit na 01.

Každý sníží právě jednu prefixovou souřadnici o 1 a ostatní ponechá.
Mezilehlý celočíselný prefixový vektor tudíž neexistuje: jde o pokrytí.

Pro úplnost nechť α>β. Zvolme první p s A_p>B_p. Pak a_p=1,b_p=0.
Sledujme souvislý běh jedniček v α od p do q. Rozdíl A_k−B_k je
na tomto běhu neklesající, tedy v q kladný. Je-li q=n, smažeme
poslední jedničku; jinak je a_(q+1)=0 a zaměníme 10 na 01. Nový
vektor γ sníží jen prefix q o 1, proto α>γ≥β. Je-li α pokrytím β,
musí γ=β. Žádný třetí typ pokrytí tedy chybět nemůže.

## (f) Délka každé nasycené cesty

Definujme

    r(α)=Σ_(k=1)^n A_k=Σ_(i=1)^n (n−i+1)a_i.

Každé pokrytí z (e) sníží r právě o 1. Na nulovém slově je r=0,
takže libovolná cesta požadovaná zadáním má přesně r(α) hran.
Existenci takové cesty dává konstrukce (e) s β=0: kladná celočíselná
hodnost klesá, až zbude nula. Rovněž každá maximální sestupná cesta
musí skončit tam, protože jinak by další pokrytí existovalo.

## Fig. 8: všech 32 vrcholů a všech 48 hran

Všechny popisky i následující sestupní sousedé byli jednotlivě porovnáni
s originálním zvětšeným diagramem. Jsou přesně výsledkem obecné (e).
Tabulka obsahuje každé pětibitové slovo jednou a každou hranu právě
jednou u horního konce; křížení úseček není dalším vrcholem.

| Horní slovo | Všechna přímo pokrytá slova |
|---|---|
| 00000 | žádné |
| 00001 | 00000 |
| 00010 | 00001 |
| 00011 | 00010 |
| 00100 | 00010 |
| 00101 | 00011, 00100 |
| 00110 | 00101 |
| 00111 | 00110 |
| 01000 | 00100 |
| 01001 | 00101, 01000 |
| 01010 | 00110, 01001 |
| 01011 | 00111, 01010 |
| 01100 | 01010 |
| 01101 | 01011, 01100 |
| 01110 | 01101 |
| 01111 | 01110 |
| 10000 | 01000 |
| 10001 | 01001, 10000 |
| 10010 | 01010, 10001 |
| 10011 | 01011, 10010 |
| 10100 | 01100, 10010 |
| 10101 | 01101, 10011, 10100 |
| 10110 | 01110, 10101 |
| 10111 | 01111, 10110 |
| 11000 | 10100 |
| 11001 | 10101, 11000 |
| 11010 | 10110, 11001 |
| 11011 | 10111, 11010 |
| 11100 | 11010 |
| 11101 | 11011, 11100 |
| 11110 | 11101 |
| 11111 | 11110 |

Celkem je 16 mazání posledního bitu a 4·8 záměn sousedního 10,
tedy 48 hran. Všechny úrovně v obrázku souhlasí s hodností
5a_1+4a_2+3a_3+2a_4+a_5, od 0 do 15.

## (g) Obě rekurence včetně slova bez jedničky

Nad slovem 1α musí každé dominující slovo začínat 1; po odstranění
prvního bitu z obou stran zbývá přesně majorizace β≥α. To je bijekce
a dokazuje m(1α)=m(α).

Nad 0α rozdělíme dominující slova podle prvního bitu. Slova 0β
dávají m(α) možností. Pro 1β požadujeme ve zbývajících prefixech
B_k≥A_k−1. Před první jedničkou α je A_k=0 a požadavek je automatický;
od této jedničky dá její smazání přesně A'_k=A_k−1. Podmínka je tedy
ekvivalentní β≥α', což dává druhý sčítanec m(α'). Pokud α nemá
jedničku, je α'=α a oba případy dovolují všechna β. Pro prázdné
slovo m(ε)=1, takže rovněž m(1)=1 a m(0)=2. Jde o přesnou disjunktní
rekurenci; netvrdí se tím žádná neodvozená polynomialita jejího výpočtu.

## (h) Přesný počet pomocí reflexe, nikoli jen odkaz na balotáž

Požadavek α≤¬α je A_k≤k−A_k, tedy v každém prefixu je nejvýše
tolik jedniček jako nul. Nulu čtěme jako krok +1, jedničku jako −1.
Pro pevný počet j jedniček, 0≤j≤⌊n/2⌋, existuje C(n,j) cest celkem.

Špatnou cestu zrcadlíme do prvního dosažení −1 včetně. Tento prefix
má o jednu jedničku více než nul, takže po záměně 0↔1 vznikne cesta
s j−1 jedničkami. Opačně každá taková cesta končí ve výšce
n−2j+2≥2, a tedy má první dosažení +1; zrcadlení právě tohoto
prefixu obnoví špatnou cestu. Jde o bijekci, proto je dobrých cest
C(n,j)−C(n,j−1), s C(n,−1)=0. Sečtení přes j teleskopuje na

    C(n,⌊n/2⌋).

Pro n=0 dává prázdná cesta hodnotu 1. Tím je doložena celá odpověď
bez potřeby přebírat dosud nekontrolované křížové odkazy na jiné úlohy.

## Trojúhelníkový poset a jeho ideály: explicitní obecná bijekce

V původním trojúhelníku šipky vedou doprava: po jedné diagonále nahoru,
po druhé dolů. Nesmí se ignorovat a číst obrázek jako obvyklý kořenový
poset s pěti minimálními prvky. Přesně jde o

    P_n={(i,j):1≤i≤j≤n},

s komponentním pořadím. Ve vizuálním řádku t=0,…,n−1 a na pozici
k=0,…,t zleva má vrchol souřadnice (k+1,n−t+k). Šipka doprava
nahoru zvětší j, šipka doprava dolů zvětší i. Pro n=5 to je všech
15 vytištěných bodů a 20 šipek. Následující důkaz je obecný.

Nechť jedničky α stojí na p_1<…<p_s. Položme

    λ_i=n−p_i+1,       λ_1>…>λ_s>0,
    I_α={(i,j):1≤i≤s, i≤j≤i+λ_i−1}.

Protože λ_i jsou různé části nejvýše n, je λ_i≤n−i+1, tedy všechny
buňky patří P_n. Koncové sloupce b_i=i+λ_i−1 jsou neklesající směrem
nahoru (b_i≥b_(i+1)). Každý bod pod zvoleným bodem v komponentním
pořadí tak zůstává v množině; I_α je ideál.

Opačně libovolný ideál má neprázdné řádky 1,…,s a v každém počáteční
úsek i≤j≤b_i. Vlastnost ideálu vynutí b_i≥b_(i+1); jejich délky
λ_i=b_i−i+1 jsou proto ostře klesající kladná čísla nejvýše n.
Určí jediné slovo s jedničkami na n−λ_i+1. To je inverzní mapa.

Navíc α≥β právě když má α alespoň tolik jedniček a každá její i-tá
jednička stojí nejvýše na pozici i-té jedničky β. Směr ⇒ použije
prefix končící touto jedničkou β; směr ⇐ pro libovolný prefix spočítá
jedničky β a použije příslušné pozice v α. To je ekvivalentní
λ_i(α)≥λ_i(β), s nulovým doplněním, a tedy I_α⊇I_β.

Jde o bijektivní uspořádání zachovávající inkluzi, nikoli jen shodu
počtů: Fig. 8 je přesně svaz ideálů zobrazeného P_5. Počet buněk
I_α je Σλ_i=r(α), takže souhlasí i hodnosti a pokrytí.

## Errata, primární odkaz a přesné bibliografické meze

Zkontrolovány all4a-pre, all4a, err4a, all4f0 a err4f0 podle čísel,
stránek a obsahu. Historické F0 erratum z 2. května 2008 nahrazuje
odpověď 109(d) na p173 právě smíšenými radixy a trojúhelníkem. Obojí
už je v prvním tisku 4A na p554 a výše má vlastní důkaz. Je to známá
historická změna bez karty a bez přírůstku našich nálezů.

Stanleyho [autorský seznam](https://math.mit.edu/~rstan/pubs/) a
[primární článek](https://math.mit.edu/~rstan/pubs/pubfiles/42.pdf)
potvrzují časopis/rok a relevantní obsah na p177–179: M(n), uspořádání
podmnožin a distributivní svaz. Článek má celý rozsah p168–184;
citace p177–179 je relevantní výběr, nikoli chybný údaj o rozsahu.
Originál p177 byl zobrazen. Jeho hlubší výsledky o Weylových grupách
a Spernerově vlastnosti zde nejsou externími vstupy ani znovu auditovány.

Winderův DOI 10.1109/PGEC.1965.264136 nebyl dostupný a původní
Lindströmův článek se nepodařilo rychle dohledat. Atribuce prvenství,
zejména věta, že Winder neprokázal svazovou vlastnost, proto zůstávají
výslovně bibliograficky neověřené. Veškerá zde požadovaná matematika
je dokázána nezávisle. Celá 109, Fig. 8 i matematické dodatky jsou checked.
