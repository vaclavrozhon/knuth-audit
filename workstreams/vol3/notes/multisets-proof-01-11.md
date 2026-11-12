# Multisety: jednotlivé argumenty úloh1–11

Zadání31, odpovědi597–599. Dopředně hotová2 a příklady hlavního textu
se přebírají; důkazy se neopakovaly. Úloha9 má dvě konkrétní funkce
v scripts/multiset_factorizations.py. Jediný běh s nice15 ověřil
tištěný15písmenný příklad a prázdný vstup; žádná enumerace.
Výstup results/multiset-factorization-example.json. V3-C0017 je
drobný candidate u izolovaných vrcholů v konstrukci odpovědi11.

## 1–4

1: Vezmeme M_1=M_2={a}, α=β=a. Součin je aa, zatímco sjednocení
dvou stejných množin je{a}. Četnosti v součinu se sčítají, takže
správná operace je multisoučet, nikoli sjednocení. To je přímo
konvence sjednocení citovaná v odpovědi.

2: Výsledek bcaddadadb a všechny jeho fronty jsou již doloženy
v multisets-proof-main.md; převzato bez nového výpočtu.

3: α=a,β=aa komutují a sdílejí a; tím je obrácení9 vyvráceno
dokonce i pro různé faktory. Odpovědní příklad α=β je také platný.
Neformální „not too many“ neobsahuje samostatnou kvantitativní mez.

4: Zachováme konkrétní dvouřádkové pole12 a pouze obrátíme prioritu
koncových minim v kanonické konstrukci. Fronty zůstávají
Q_a=db,Q_b=cbcac,Q_c=dad,Q_d=dbbbd. Postupné návraty do nejmenšího
zbývajícího písmene v pořadí d<c<b<a dávají
(d),(bcd),(bbcad),(babcd),(d), přesně vytištěnou odpověď.
Nezaměňuje se to s jiným polem vzniklým novým přiřazením nezměněné
dolní řádky k přeuspořádané horní řádce. Jednorázový programový
příklad potvrzuje i zpětné složení těchto pěti faktorů.

## 5: stejné sousední prvky

Hrana x→x uvnitř netriviálního cyklu se objeví jako xx i po
vypuštění závorek. Rozdíl mohou způsobit jen jednočlenné cykly(x).
Při jejich vypuštění se ztratí uzavírací smyčka, ale získá spoj xx
od předchozího cyklu s týmž minimem x, pokud takový předchází.
V každém bloku cyklů s minimem x se proto ztratí nejvýše jedna
započtená smyčka: právě když první cyklus tohoto bloku je(x).
Počet xx je tedy počet sloupců x/x minus0 nebo1.
Je-li x nejmenším permutovaným prvkem, první cyklus je(x) právě
tehdy, když výsledné slovo začíná x; podle B(a) právě tehdy začíná
x i původní slovo. To dokazuje i poslední větu odpovědi5.

## 6–7: počty podle sousedností a počátečního písmene

6: Věta B převádí k dvojic ba na k dolních a pod horním b.
Bilance vynutí k dolních b pod horním a. Výběry k míst z m
a k z n jsou nezávislé, tedy choose(m,k)choose(n,k).

7: Pro A≥1 fixujeme první dolní znak pod prvním horním a.
Další umisťování je stejné jako v již dokázaném20.
Pro začátek a zbývá A−k−m−1 dolních a v A−1 místech;
ostatní čtyři faktory se nemění. Pro začátek b/c zbývá
A−k−m dolních a v A−1 místech a poté B+k−1 volných míst
pod horními a,b. Do nich vložíme B−l−1 dolních b při začátku b,
nebo B−l při začátku c. Faktory choose(B,m),choose(C,k),
choose(C−k,l) se nemění. To jsou přesně všechny tři odpovědní vzorce.

Při A=0 nutně k=m=0. Pro B>0 redukce na dvě písmena dává
počty začátků b/c rovné choose(B−1,l)choose(C,l) a
choose(B−1,l−1)choose(C,l); stejně se redukují uvedené výrazy
s obvyklým choose(−1,0)=1. Při A=B=0,C>0 je jediným slovem c^C.
Výroky o prvním písmenu se používají pro neprázdná slova;
prázdné slovo žádný první znak nemá.

## 8: všechna rozdělení na dva faktory

Prvočíselný rozklad příkladu12 je
(d),(bcd),(b),(adbc),(ab),(bcd),(d).
Kontrola front a jednorázový běh dávají přesně původní pole12.
Každé dvě sousední cykly sdílejí písmeno; nelze tedy provést ani
první dovolenou záměnu disjunktních sousedů. Věta C zaručuje, že
neexistuje jiný prvočíselný rozklad. Každé α⊤β lze rozložit na
prvočinitele a musí odpovídat jednomu ze8 řezů tohoto jediného slova
sedmi faktorů, včetně prázdného α a prázdného β. To dokazuje úplnost.

## 9: dva programy a invarianty

canonical používá fronty a první návrat do minimálního písmene.
Invarianty i nemožnost uváznutí jsou již dokázány v hlavním textu.
Každá hrana se odebere právě jednou a cykly končí předepsaným minimem.

primes sleduje funkční graf první položky každé neprázdné fronty,
aniž zatím něco odebírá. Cílový vrchol má neprázdnou frontu, protože
celé zbývající pole má vyrovnané stupně. Cesta proto najde opakovaný
vrchol; její cyklický suffix má různé vrcholy a používá právě první
hranu každé své fronty. Je tedy prvočíselným levým faktorem. Odebrání
hran zachová bilanci; indukce podle počtu hran ukončí rozklad.
Rotace jednoduchého cyklu k nejmenšímu písmenu jeho fronty nemění.

Oba programy pracují s libovolným konečným slovem na uspořádané
abecedě; prázdný vstup vrací prázdný seznam. Při n znacích a m
různých písmenech postačí O(nm+n log n) času a O(n+m) prostoru
pro tuto jednoduchou implementaci. Jediný cílený běh potvrdil
tištěnou kanonickou, obráceně prioritní i prvočíselnou faktorizaci
a jejich zpětné složení. Nejde o plošné experimentální ověření.

## 10: kdy lokální pořadí jednoznačně normalizuje faktory

Komutující faktory seřadíme orientovaným přepisem τσ→στ proσ≺τ.
Celkový počet inverzí v konečném slově klesá, tedy normální tvar
existuje. Dva přepisy na disjunktních místech komutují. Jediný
překryv má tvar τσρ sρ≺σ≺τ aτ∼σ∼ρ. Oba výsledky lze sloučit
právě kdyžρ∼τ; potom se všechny tři prvky uspořádají. Pokud tato
podmínka platí pro každou trojici, indukce na délce přepisování
dává jediný normální tvar celé komutační třídy.

Nutnost téže podmínky: přiρ∼σ∼τ,ρ≺σ≺τ,ρ nesouvisejícím sτ
jsou slova στρ aτρσ ekvivalentní přesunutímσ přes oba sousedy,
ale obě již splňují lokální pořadí a jsou různá. To dokazuje přesně
nutnou a postačující podmínku odpovědi10, bez problémového výběru k;
známé erratum tam požaduje nejmenší k.

Všechna prvočísla takto uspořádat nelze: cykly(ab),(de),(bc),(ea),(cd)
mají komutační graf pětiúhelníku bez úhlopříček. Podmínka zakazuje
monotónní cestu délky2, takže každý vrchol musí být lokálním maximem
nebo minimem. Ty by se musely na lichém cyklu střídat, spor. Je-li
(ab)≺(de), dostáváme přesně vytištěný řetěz střídajících nerovností.
Pro šest cyklů29 tvoří netriviální komutace dvě disjunktní hrany,
takže podmínka platí a dříve dokázaný speciální normální tvar je platný.

## 11: lineární rozšíření a přesný otevřený okraj

Poset bereme jako tranzitivní uzávěr vztahů i<j s protínajícími se
nosiči σ_i,σ_j. Každé lineární rozšíření lze získat přesouváním
jeho prvního prvku před předchozí nezávislé prvky, pak indukcí.
Všechna taková přesunutí komutují, takže zachovají interkalaci.
Obráceně věta C dovoluje jen výměny disjunktních sousedů, které
nemění pořadí porovnatelných indexů. Výskyty identických cyklů se
označí v jejich původním pořadí; nemohou se prohodit. Každé výsledné
neoznačené slovo faktorů proto má jedinou posloupnost označených
výskytů. To dokazuje bijekci a přesný počet, včetně známé opravy
podmínky pro opakované identické cykly v odpovědi11.

Existenční tvrzení pro libovolný poset lze dokázat úplně: očíslujme
vrcholy v jednom lineárním rozšíření, každému porovnatelnému páru
(i,j) dejme samostatné písmeno a vložme je do cyklů i a j.
Každému vrcholu přidáme navíc jeho soukromé písmeno z_i.
Cykly jsou neprázdné a dva různé sdílejí písmeno právě tehdy,
jsou-li příslušné vrcholy porovnatelné; dostáváme přesně požadovaný
poset. Příklad s páry(1,2),(1,4),(3,4) v odpovědi dává uvedené
tři vztahy již bez doplňkových písmen, protože nemá izolované vrcholy.

Původní konkrétní konstrukce však soukromá písmena neuvádí.
Pro dvouprvkový antichain dává dva prázdné seznamy. Zda má
kontext zvláštní konvenci pro tento okraj, zůstává V3-C0017
candidate/low. Samotná bijekce pro neprázdné cykly i obecné
existenční tvrzení jsou výše dokázány; nejde o jejich vyvrácení.
