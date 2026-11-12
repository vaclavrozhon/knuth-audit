# §5.2.1: celé44 a závěr43

2026-11-07. P0927–0933. Originály105/file116 a628/file639
zobrazeny. Pět vrstev přebírá `sources/insertion-errata-review.json`;
na628 je jen bibliografická oprava dalšího§5.2.2-2. Žádný nový
nález, žádný matematický běh. Rozlišují se dva různé uspořádávací
vztahy; pravdivost výsledku není dovozena z důkazu pouze pro silnější
předpoklad. Praktické srovnání varianty43 je zvlášť partial.

## P0927–0928: částečné h-průchody na konci43

Dosud prokázané sentinelové zrychlení43 se nepřepočítává. Nová
poznámka na628 navrhuje **jen pro h>1** při každém j porovnat
K_(j−h),K_j a při nesprávném pořadí je vyměnit, bez dalšího
propagování menšího prvku doleva. Takový průchod má přesně N−h
porovnání, je-li1<h<N, a nejvýše tolik výměn. Zachová všechny
záznamy a skončí po konečné rostoucí smyčce j. Není to úplné
h-třídění: pro h=2 a vstup3,4,2,5,1 dostaneme po j=3,4,5
2,4,1,5,3; liché pozice2,1,3 zůstaly neseřazené.

Poslední h=1 ale podle přesné formulace zůstává původním úplným
insertion sortem. P0685–0692 proto dokazují výsledné setřídění
libovolného mezivýsledku. Z pouhého jednoho částečného průchodu
h=1 by správnost neplynula; to však tato poznámka nenavrhuje.
Tím je doložena správnost popsané varianty a lokální nižší režie,
nikoli stejná h-ordered invarianta či starší nákladové věty Shellsortu.

Výrok „seems to require more increments“ neudává porovnávanou
posloupnost, počet, distribuci, přesnost ani celkový nákladový cíl.
**P0928 partial** pro toto praktické srovnání, stejně jako již
evidované jiné empirické návrhy; není označeno za falešnou větu.
Více přírůstků není nutné k samotné správnosti s úplným závěrečným
h=1. Původní Dobosiewicz1980 nebyl z dostupného publisher endpointu
získán (403), takže jeho plné experimenty a vlastní přesný kód se
nevydávají za nezávisle ověřené.

## P0929: definice44, prefixové prahy a částečné uspořádání

Označme s_(j,1)<…<s_(j,j) vzestupně setříděný prefix délky j.
Knižní definice pomocí i-tého největšího je totéž jako
s_(j,k)≤s'_(j,k) pro všechna j,k. To přesně vyjadřuje
komponentové srovnání po j krocích straight insertion; příslušný
invariant se přebírá z P0685–0692.

Užitečný ekvivalentní zápis je

    C_π(j,t)=#{i≤j:a_i≤t}, 0≤j,t≤n,
    π≼π' právě tehdy, když C_π(j,t)≥C_π'(j,t) pro všechna j,t. (A)

Je-li k prvků druhého prefixu≤t, jeho k-tý prvek≤t a z komponentové
nerovnosti totéž platí pro první prefix. To dává dopředný směr.
Pokud naopak s_(j,k)>s'_(j,k), volba t=s'_(j,k) dává
C_π(j,t)≤k−1<k≤C_π'(j,t), spor. Oba směry jsou doloženy.

Reflexivita a tranzitivita jsou komponentové. Při π≼π'≼π jsou
všechny prefixové množiny shodné; rozdíl prefixů délek j a j−1
určuje jediný a_j, takže π=π'. Je to skutečně částečné uspořádání,
včetně prázdné a jednoprvkové permutace. Rovné hodnoty mezi
různými permutacemi nepůsobí problém; uvnitř každé jsou hodnoty různé.

## P0930:44(a), slabé uspořádání implikuje prefixové

Konvence „π above π'“ v5.1.1-12 znamená E(π)⊆E(π'), kde E je
množina inversí jako dvojic **hodnot**. P0157 již obecně dokázal,
že pak existuje cesta z π do π' přes sousední vzestupné dvojice
x<y, které se obracejí na y,x a pokaždé přidají jedinou inversi.
Tento důkaz se přebírá; nejde o předpoklad nové silné relace.

Jediný takový krok na pozicích r,r+1 mění pouze prefix délky r:
v něm se nahradí x větším y. Pro x≤t<y jeho C(r,t) klesne o1,
všechny jiné prahové počty zůstanou. Podle(A) tedy původní
permutace≼nová. Tranzitivita přes celou cestu dokazuje požadované
π≼π'. Tím je také určena orientace názvů „above/below“ v krátké
odpovědi, bez spoléhání na prohozená jména proměnných v její první větě.

## P0931:44(b), úplný argument pro skutečný předpoklad

π^R znamená obrácení pořadí pozic. Celá permutace obsahuje právě t
hodnot≤t, takže pro všechny0≤j,t≤n přesně

    C_(π^R)(j,t)=t−C_π(n−j,t).

Z π≼π' a(A) proto plyne C_(π^R)(j,t)≤C_(π'^R)(j,t), což je
π^R≽π'^R, jak otázka požaduje. Jde o obecný důkaz, nikoli o
případ, kdy jsou navíc porovnatelné v slabém uspořádání. Zahrnuje
j=0,n a prohozené role dává i obrácenou implikaci.

Tištěná vysvětlující věta(b) výslovně mluví pouze o „above/below“.
Ta je také pravdivá: obrácení pozic nahradí E jeho doplňkem ve všech
dvojicích hodnot, a tedy obrátí inkluzi. **Sama tato slabá implikace
není důkazem celé otázky(b)**, protože obrácení(a) neplatí, viz(c).
Proto je výše doplněn potřebný prefixový argument. Výsledek „Yes“
i uvedená slabá implikace jsou správné; stručnost návodu se zde
nepřeklasifikovává na potvrzenou chybu matematického tvrzení.

## P0932:44(c), všechny části tištěného protipříkladu

Pro213 a312 jsou prefixy délek1,2 vzestupně(2),(1,2) a
(3),(1,3). Komponentové nerovnosti platí, prefix délky3 je stejný.
Tedy213≼312. Inverzní množiny jsou

    E(213)={(2,1)}, E(312)={(3,1),(3,2)}.

Ani jedna není podmnožinou druhé. Nejsou tedy ani above, ani below,
přesně jak říká odpověď. Tím se současně dokazuje, že slabé
uspořádání je logicky silnější podmínka, i když má název „weak“.

## P0933: mřížka — převzatá slabá a konkrétní neslabá

Slabá relace má obě mřížkové operace podle úplného důkazu P0126
v `inversions-proof-01-13.md`: tranzitivní uzávěr sjednocení inversí
a jeho doplňková duální konstrukce. Tento obecný důkaz se neopakuje.

Pro prefixové uspořádání již v S₃ mají132 a213 dvě společné horní
meze231 a312. Zkontrolují se jen prefixy délek1,2:

    132: (1);(1,3)        213: (2);(1,2)
    231: (2);(2,3)        312: (3);(1,3).

Všechny čtyři požadované relace dolní≼horní z tabulky platí.
231 a312 jsou neporovnatelné: první má větší minimum prefixu2,
druhá větší první prvek. Ještě je nutné vyloučit jinou nejmenší
horní mez σ pod oběma: její první prvek musí být≥2 a≤2, tedy2.
Její prefix2 musí mít minimum≤1 a maximum≥3, a tedy obsahovat
1 i3; to je neslučitelné s již přítomnou2. Žádná taková σ neexistuje.
Spojení132∨213 proto neexistuje a relace není mřížka.

Připojením4,…,n se tentýž argument vloží do všech S_n,n≥3:
rovnost třetího prefixu s horními mezemi vynutí množinu{1,2,3},
takže pozdější hodnoty překážku neodstraní. Pro n≤2 jsou obě
relace stejné řetězce; obecné knižní srovnání rodin uspořádání
neznamená popření těchto malých degenerovaných případů.

## Bibliografie

Katalog původního časopisu potvrzuje Ehresmannův titul, ročník35(1934)
a strany396–443: <https://www.jstor.org/stable/i307177>,
DOI10.2307/1968440. Obsah§20 a prvenství nezávisle neověřeny.
Primární Springerův popis Björner–Brenti, *Combinatorics of Coxeter
Groups* (2005), výslovně rozlišuje kapitoly Bruhat order a Weak order:
<https://link.springer.com/book/10.1007/3-540-27596-7>.
Samotný katalog není použit jako důkaz rankového kritéria; všechna
potřebná tvrzení o zde definovaných relacích jsou dokázána výše.
Dobosiewiczův úplný článek po403 výslovně přeskočen, nikoli
nahrazen sekundárními tvrzeními o jeho experimentech.
