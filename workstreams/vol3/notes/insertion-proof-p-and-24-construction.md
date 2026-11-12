# Věta P a doložená část konstrukce24

7. listopadu 2026. Originál91/file102 a104/file115,
odpověď622–623/file633–634 zobrazen. Pětivrstvá evidence
`sources/insertion-errata-review.json` převzata. Historickou atribuci
Papernov/Stasevich ani Prattovu širší generalizaci zde nedohledáváme.
Žádný program se nespouští. Horní věta P je úplně doložena;
ostrý dolní odhad24 zůstává níže přesně označený partial.

## P0798: všechny předpoklady a oba součty horní meze P

Nechť N≥2, t=⌊lg N⌋ a h_s=2^(s+1)−1 pro0≤s<t.
Přírůstky jsou kladné, přísně rostoucí, největší je<N,
a h_0=1, takže jde o platný dokončující programD.

Při libovolném h-sortu je součet inversí jeho tříd nejvýše
součet binomických čísel jejich délek. Každá má délku≤N/h+1
a h<N, takže B_s≤2N²/h_s. Pro s≥t/2 je h_s≥2^s a

    ∑_(t/2≤s<t) B_s=O(N²2^(−t/2))=O(N^(3/2)),

protože N<2^(t+1). Pro s<t/2 a t≥4 jsou oba předchozí
průchody h_(s+1),h_(s+2) skutečně přítomné. Jsou nesoudělné:
h_(s+2)=2h_(s+1)+1. K a již doložená23 proto dávají

    B_s=O(N h_(s+2)h_(s+1)/h_s)=O(N2^s),

neboť h_(s+1)=2h_s+1≤3h_s a h_(s+2)=4h_s+3≤7h_s.
Součet pro s<t/2 je O(N2^(t/2))=O(N^(3/2)).

Pro t≤3 jde pouze o2≤N≤15. Hrubý konečný odhad O(N²t)
lze zahrnout zvětšením absolutní konstanty. Neaplikujeme23
na neexistující druhý předchozí průchod v těchto malých případech.
Rozdělení podle celočíselných s funguje pro sudé i liché t;
geometrické řady mění jen absolutní faktor.

## P0799: skutečný čas programu, nikoli pouze přesuny

Převzatý úplný instrukční součet P0714 je

    time_D=9B+10NT−10S−3A+13T+1.

Zde T=t=O(log N), S,A≥0. Horní mez času je proto
9B+10Nt+13t+1=O(N^(3/2)), protože N log N=O(N^(3/2)).
Žádný krok nepoužil rovnoměrný vstup: všechny B_s byly omezeny
pro každou permutaci. Jde tedy skutečně o nejhorší případ,
a tím zároveň i o horní mez libovolného průměru.

## P0800: kvadratický nejhorší případ dělitelné posloupnosti

Pro přísně dělitelné přírůstky sousední hodnoty rostou alespoň
dvojnásobně. Součet horních mezí N²/h_s+O(N) přes průchody
je O(N²), stejně jako režie O(N log N).

Je-li jen jeden průchod, sestupná permutace má binom(N,2)
přesunů. Jinak je h_1≥2. Podle již doložené zpětné konstrukce
P0759 lze v posledním průchodu realizovat maximum
fhat(N,h_1). S q=⌊N/h_1⌋≥N/(2h_1) máme

    fhat(N,h_1)≥binom(h_1,2)binom(q+1,2)
               ≥h_1²q²/8≥N²/32.

To je uniformní dolní mez, nikoli asymptotika pouze pro pevné h_1.
Každý přesun stojí kladný čas, takže nejhorší čas je Θ(N²).
Nadbytečné opakování téhož přírůstku lze vynechat; kontrast na91
se vztahuje na obvyklou přísnou posloupnost, ne na uměle přidané
libovolné množství nečinných průchodů.

## P0801: přípustnost a terminace celé recidivious konstrukce

V úloze24 piš Q=2^h, A=Q−1, h≥2, a G pro nezáporný
semigroup generovaný A,2Q−1,4Q−1,… . Pozici i vyplníme v
prvním kroku j≥2, pro který Aj−i je **kladný** prvek G.
Při stejném j se vyplňují pozice zleva doprava; přidělují se
dosud nepoužité hodnoty1,2,… . Označ tento první krok τ_i.

Existence τ_i plyne z úplně doloženého conductoru Q A:
pro velké j je Aj−i≥QA. Konstrukce tedy každou pozici právě
jednou vyplní a při konečném N skončí s permutací1,…,N.

Je-li d=2^k−1, k≥h, a i+d≤N, z
Aτ_(i+d)−(i+d)∈G\{0} po přičtení generátoru d plyne
Aτ_(i+d)−i∈G\{0}. Proto τ_i≤τ_(i+d). Při ostré nerovnosti
dostane i menší hodnotu dříve; při rovnosti ji dostane dříve
kvůli levopravému pravidlu. Vždy a_i<a_(i+d).
Permutace je tedy uspořádaná pro **všechny** přírůstky2^k−1,
k≥h. Tyto předchozí průchodyD ji vůbec nezmění. První průchod,
který může něco měnit, má přírůstek a=2^(h−1)−1>0.

## P0802: celý příklad h=2, N=20

Pro A=3 jsou nejmenší kladné reprezentovatelné hodnoty v jeho
třech zbytcích W⁺={3,7,14}; první je3, nikoli0. U i=3q+r
proto τ_i=q+1 pro r=0, q+5 pro r=1 a q+3 pro r=2.
Všechna vyplnění příkladu jsou:

|j|pozice vyplněné zleva|přidělené hodnoty|
|---:|---|---|
|2|3|1|
|3|2,6|2,3|
|4|5,9|4,5|
|5|1,8,12|6,7,8|
|6|4,11,15|9,10,11|
|7|7,14,18|12,13,14|
|8|10,17|15,16|
|9|13,20|17,18|
|10|16|19|
|11|19|20|

Čtení podle pozic dává přesně
6,2,1,9,4,3,12,7,5,15,10,8,17,13,11,19,16,14,20,18
z odpovědi. Nulový rozdíl Aj−i je správně vyloučen podle zadání
konstrukce; jeho zahrnutí by změnilo pořadí.

## P0803: přesně A nových pozic v každém vnitřním kroku

Nechť W⁺ je množina nejmenších kladných členů G v jednotlivých
zbytcích modulo A. Má přesně A členů; pro nulový zbytek je to A,
pro ostatní obvyklé minimální zástupce. V kroku j se vyplňují
právě existující pozice

    i=Aj−w,  w∈W⁺.

Doklad: Aj−i=w je kladně reprezentovatelné, ale w−A již není
kladně reprezentovatelné. To přesně vylučuje krok j−1 i všechny
dřívější, protože G je uzavřené na přičtení A.

Z conductoru a poslední mezery v P0792 máme
max W⁺=QA−1+A=(Q+1)A−1; minimum je A.
Pro Q<j≤N/A proto všechny pozice Aj−w leží v1,…,N:
nejmenší je nejméně1 a největší A(j−1)<N. Jsou různé,
takže se skutečně vyplní přesně A pozic, jak tvrdí odpověď.

## P0804 — partial: přesný zbývající lokální odhad

Seřaď W⁺ sestupně jako w_0>w_1>…>w_(A−1). Vnitřní krok j
přiděluje pozice i_k=Aj−w_k v tomto pořadí. Počet inversí,
v nichž a_(i_k) je levý větší člen a pravá pozice leží ve stejné
třídě modulo a=Q/2−1, je přesně

    c(w_k)=#{ℓ≥1: w_k−A−ℓa ∈ G\{0}}.             (*)

Pravá pozice p=i_k+ℓa dostala menší hodnotu právě tehdy,
když byla vyplněna nejpozději v kroku j−1, tedy když
A(j−1)−p=w_k−A−ℓa je kladně reprezentovatelné. Při stejném
kroku by pravější pozice měla větší hodnotu a inversí by nebyla.
Kladnost v(*) také zaručí p<A j≤N, takže se nepřidávají
neexistující pozice. To dokazuje obousměrně vzorec(*).

Dosud zbývá pro všechna h≥2 dokázat knižní lokální odhad

    c(w_k)≥Q/2−2k.

Zejména nestačí místo něj spočítat všechny inverse daného prvku
bez podmínky stejné třídy modulo a. Převzetí již dokázaného
conductoru či samotné tabulky pro h=2 obecný odhad také nedává.
Tato mez se proto neoznačuje checked.

Pokud bude dokázána, zbývající algebra je již přesná:
pro N=2QA je Q vnitřních kroků j=Q+1,…,2Q. Součet kladných
mezí pro k=0,…,Q/4−1 je
(Q/4)(Q/4+1)>Q²/16. Celkem tedy B>Q³/16=2^(3h−4).
Protože N<2Q² a2√2<4, vyjde též B>N^(3/2)/64.
To je požadovaná neklesnutelnost exponentu3/2. Prozatím jde
o **podmíněný** závěr závislý na nedokončené lokální mezi, ne
o uzavřenou dolní větu. Širší historické generalizace na623
nejsou náhradou tohoto chybějícího argumentu.

Další kurzor je přesně(*) a jeho lokální mez v24; žádná další
stránka91/104/622/623 se na základě této části neuzavírá.
