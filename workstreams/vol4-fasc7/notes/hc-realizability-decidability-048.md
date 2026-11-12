# Úloha48: přesný rozhodovací převod, nikoli úplná klasifikace složitosti

Zadání p117/file132 se ptá na algoritmus rozhodující realizovatelnost
HC sítě podle definice47. Odpověď p168/file183 pak klade otázku
rozhodnutelnosti a složitosti. Nejde o realizaci prostorového 3VP,
ani o existenci line labelingu. Je třeba rozhodnout konečný
rovinný obrázek s předepsanými přímými čarami, úhlovými typy,
pořadím a se zákazem vnějšího T z úlohy47.

Níže je úplný vlastní převod do existenciální teorie reálných
čísel. Existence rozhodovacího algoritmu a horní mez PSPACE
využívají přesně určenou externí větu, nikoli náš nový důkaz
celé eliminace kvantifikátorů. Přesná složitost tohoto speciálního
problému, dolní meze a praktický algoritmus zůstávají partial.
Žádná nová karta chyby se z formulace výzkumné otázky nevytváří.

## D48-1 — lokální polynomiální podmínky

Nejprve ověříme konečnou syntaxi sítě: různé jmenované vrcholy,
různé jiné sousedy v každém seznamu a reciproční sousednost.
Po komponentách lze postupovat nezávisle podle E47(b); prázdná
síť je realizovatelná. Pro jednu neprázdnou komponentu zaveďme
2n neznámých souřadnic p_i=(x_i,y_i). Volíme orientaci roviny
jako v sazbě, s osou y dolů. Označme
`[u,v]=u_x v_y−u_y v_x` a `u·v=u_xv_x+u_yv_y`.

Všechny vrcholy musí být různé:
`(x_i−x_j)²+(y_i−y_j)²>0` pro každé i≠j.
Pro paprsky L=p_l−p_i,M=p_m−p_i,R=p_r−p_i předepíšeme:

- V(l,r): `[L,R]>0`;
- W(l,m,r): `[L,M]>0`, `[M,R]>0`, `[L,R]>0`;
- T(l,m,r): `[L,R]=0`, `L·R<0`, `[L,M]<0`, `[M,R]<0`;
- Y(a,b,c): všechny tři cyklické determinanty paprsků jsou>0.

Každá sada je ekvivalentní přesné úhlové definici. U W první
a poslední paprsek vymezují sektor<π a dvě další nerovnosti
kladou prostřední právě mezi ně. U T rovnost a záporný skalární
součin znamenají protilehlé kolineární paprsky, nikoli souběžné
větve na stejné straně. Poslední dvě nerovnosti volí stranu
stonku. U Y jsou všechny tři cyklické mezery striktně<π.
Nevyžaduje se předem racionálnost souřadnic.

## D48-2 — žádné nedovolené průniky, pouze existenciální kvantifikátory

Dvě disjunktní uzavřené úsečky lze striktně oddělit přímkou.
Potřebujeme i důkaz této ekvivalence, abychom neskrývali
univerzální podmínku nad všemi body úseček.

Jsou-li A,B kompaktní disjunktní úsečky, existují nejbližší body
a∈A,b∈B s b≠a. Položme v=b−a. Derivace kvadrátu vzdálenosti
v přípustném směru z a dává `v·(p−a)≤0` pro všechna p∈A;
obdobně `v·(q−b)≥0` pro všechna q∈B. Pro
`z=v·(a+b)/2` tedy `v·p<z<v·q`. Opačně přísné oddělení
okamžitě vylučuje společný bod. Stejný důkaz platí pro bod
a úsečku. Existence nejbližších bodů plyne z kompaktnosti
součinu dvou uzavřených omezených intervalů a spojitosti
kvadrátu vzdálenosti.

Pro každou dvojici neincidentních hran ab a cd proto přidáme
tři nové existenciální neznámé v_x,v_y,z a čtyři podmínky
`v·p_a<z`, `v·p_b<z`, `v·p_c>z`, `v·p_d>z`.
Lineárnost v bodové souřadnici zaručuje totéž pro celé úsečky.
Pro každý vrchol i neincidentní hraně ab obdobně přidáme
`v·p_i<z`, `v·p_a>z`, `v·p_b>z` s vlastními třemi neznámými.
Tím jsou explicitně vyloučeny také dotyky vrcholů s cizí hranou.
Incidentní hrany se díky různým lokálním paprskům protínají
pouze ve společném konci; protilehlé T bary se nepřekrývají.

Každý atom je polynomiální nerovnost stupně≤2 s celočíselnými
koeficienty. Žádný nový normálový vektor nemusí mít předem
omezenou délku; jeho nenulovost plyne už z opačných přísných
nerovností. Existenciální svědci různých separací jsou nezávislí.

## D48-3 — vnější stěna je také konečná polynomiální podmínka

Předepsané typy určují cyklické pořadí všech sousedů: W má
pořadí(l,m,r), Y(a,b,c), T(r,m,l); u stupně2 je cyklus určen
jednoznačně. Z nich se předem vypočtou stěnové průchody
permutací orientovaných hran z B-1. Tato operace používá jen
konečná vstupní data. V libovolném skutečném rovinném vložení
se stejnými pořadími jsou to právě jeho stěnové průchody.

Vyřaďme kandidátní průchod f, pokud obsahuje obě barové hrany
některého T. U každého zbývajícího spočtěme formální polynom

`A_f = Σ_k [p_(f_k),p_(f_(k+1))]`, s cyklickými indexy.

Přidáme disjunkci `∨_f (A_f>0)` přes tyto přípustné kandidáty;
prázdná disjunkce znamená nepravdu. V orientaci s y dolů má
vnější průchod kladnou dvojnásobnou plochu a každý vnitřní
zápornou. Opakované mosty se v tomto součtu přesně vyruší.
Neprázdná HC komponenta má minimální stupeň2, tedy obsahuje
cyklus a její vnější plocha je kladná. Výběr kladného A_f
proto přesně vybere skutečnou vnější stěnu a zaručí právě
požadovaný zákaz T. Nezaměňuje se zde vnější stěna se všemi
stěnami ani s libovolným abstraktním cyklem.

Souvislá síť s nesférickou rotací může být předem zamítnuta
Eulerovým testem; není to však nutné pro správnost formule,
protože žádné její neprotínající se rovinné souřadnice pak
neexistují. U nesouvislé sítě je obvod míněn pro každou
komponentu zvlášť, stejně jako v tištěné redukci E47(b).

## D48-4 — obě implikace, konečnost a velikost

Každá realizace poskytne souřadnice splňující D48-1, oddělovací
přímky z D48-2 a skutečný přípustný vnější průchod z D48-3.
Proto splňuje celou existenciální formuli.

Naopak řešení formule dává různé body, právě předepsané místní
typy a pořadí, žádné křížení, překryv nebo cizí vrchol na hraně.
Je tedy skutečným HC obrázkem dané sítě. Kladný přípustný
stěnový průchod je jeho vnější obvod, na němž nenastává
zakázané T. Je tedy realizací podle přesné definice47.
Jde o ekvivalenci, ne pouze o nutné souřadnicové podmínky.

Protože E≤3n/2, obsahuje konstrukce O(n²) pomocných neznámých,
O(n²) atomů a polynomiálně dlouhé zápisy indexů a koeficientů.
Všechny polynomy mají stupeň≤2; součet délek všech stěnových
průchodů je2E, takže disjunkce vnějších stěn není exponenciální.
Rovnost p=0 lze zapsat jako p≥0 a−p≥0. Dostáváme tedy v
polynomiálním čase existenciální formuli nad reálnými čísly,
s konečnou monotónní booleovskou kombinací atomů p≥0,p>0.

## D48-5 — přesně převzatá externí věta a neuzavřená část

Primární zdroj: John F. Canny, *Some Algebraic and Geometric
Computations in PSPACE*, UCB/CSD-88-439(1988), §3.1,p9 a
Theorem3.3,p12–13. [Univerzitní záznam](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1988/6041.html)
a [původní PDF](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1988/Archive/CSD-88-439.pdf).
Originální stránky9,10,12,13 byly přímo zobrazeny; jsou uloženy
v `images/Canny-scope-09.png`, `Canny-scope-10.png`,
`Canny-12.png`, `Canny-13.png`, spolu s úplným PDF ve sources.

Na p9 je přesně vymezen vstup ∃x P(x), kde P je konečná
booleovská kombinace znaménkových podmínek polynomů; Theorem3.3
poskytuje rozhodování v PSPACE. Předchozí vlastní konstrukce
splňuje právě tento vstupní formát a má polynomiální velikost.
Přebíráme tuto externí algoritmickou větu včetně ukončení,
nikoli vlastní implementaci ani nový důkaz její obecné platnosti.
Z toho plyne rozhodnutelnost a horní mez PSPACE pro úlohu48;
přesněji jsme doložili příslušnost do třídy ∃R.

Výrok, že tento speciální problém je např. ∃R-úplný, NP-úplný
nebo řešitelný v polynomiálním čase, zde prokázán není. Přesná
složitost požadovaná v odpovědi48 tedy zůstává partial. Ani
malý praktický program pro obecné vstupy nebyl spuštěn. Tento
výsledek se automaticky nepřenáší na otázku prostorových
signed skeletons v úloze37, která má jiné předpoklady a potřebuje
samostatný úplný převod.
