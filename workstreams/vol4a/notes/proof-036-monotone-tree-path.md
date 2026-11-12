# §7.1.1–22 až 25: monotónní rozklad, stromy a cestové grafy

6. listopadu 2026, X0066. Původní sazba zadání p81/file98 a odpovědí
p537/file554; definice shellingu p84/file101. Perrinova definice
ověřena přímo na p623/file640, vlastní PDF/render. Nejde o kontrolu
ostatního obsahu p623. Žádný program ani enumerace.

Přebíráme přesné obecné důkazy P0607–P0611 z proof-035: monotónnost
po souřadnicích, kladnost prvoimplikantů a Corollary Q. Následují
argumenty všech částí a matematických dodatků odpovědí 22–25.

## P0618: úloha 22, nutné i postačující podmínky

Pro f(u,t)=g(u)⊕(h(u)∧t) jsou kofaktory f(u,0)=g(u) a
f(u,1)=g(u)⊕h(u). Monotónnost f je ekvivalentní monotónnosti obou
kofaktorů a bodové nerovnosti g≤g⊕h. Nutnost plyne omezením na
vrstvy a zvýšením t. Pro postačitelnost nejprve měníme souřadnice u
uvnitř vrstvy a potom t z 0 na 1.

Bodově g≤g⊕h právě když nenastane g=h=1, tedy g∧h=0.
To jsou přesně vytištěné podmínky. Samotná h nemusí být monotónní:
u monotónní f(x,t)=x∨t dostáváme g=x, h=¬x. Pro n=1 jsou kofaktory
konstantní a tentýž argument zahrnuje všechny přípustné konstanty.

## P0619: úloha 23, všechny prime klauzule

Zadaná funkce je

    f = x ∧ ((v∧w) ∨ (v∧z) ∨ (y∧z)).

Kladná klauzule je implikovaná touto DNF právě když její množina
proměnných protíná všechny tři množiny {v,w,x}, {v,x,z}, {x,y,z}
(P0602). Minimální takové množiny jsou {x} a minimální transversal
rodiny {v,w}, {v,z}, {y,z}. Obsahuje-li transversal v, musí mít ještě
y nebo z; bez v musí obsahovat w i z. Dostáváme přesně

    {x}, {v,y}, {v,z}, {w,z}.

Žádná menší podmnožina těchto čtyř množin neprotíná všechny termy.
Zároveň uvedené rozlišení vyčerpává všechny minimální možnosti.
Proto úplná konjunktivní prime forma je přesně

    x ∧ (v∨y) ∧ (v∨z) ∧ (w∨z).

## P0620: obecný postup v dodatku odpovědi 23

Dualita f*(u)=¬f(¬u) zachovává monotónnost a mění kladnou DNF
na kladnou CNF. Přesný důkaz Corollary Q se tedy přenese na klauzule:
kladná CNF je prime forma právě když její množiny literálů tvoří
antichain. To dokládá nejen neodstranitelnost, ale úplnost seznamu.

U konečného výrazu s ∧ a ∨ lze CNF získat rekurzivně. Konjunkce
spojí seznamy klauzulí; disjunkce dvou CNF vezme všechny dvojice
klauzulí a jejich sjednocení, podle distributivity. Konečný syntaktický
strom i všechny kartézské součiny jsou konečné, takže konstrukce skončí.
Odstraníme duplikáty a každou klauzuli obsahující jinou. Zbylý antichain
je podle předchozího přesně prime CNF. Konstanty se nejprve zjednoduší;
0 je prázdná klauzule a 1 prázdná konjunkce. Postup zde nemá tvrzenou
polynomiální složitost; rozvinutí může být velké.

## P0621: úloha 24, úplnost rekurence prvoimplikantů

Všechny listy jsou různé proměnné. Označme O_k počet prvoimplikantů
stromu výšky k s ∨ v kořeni a A_k počet pro ∧; pro k=0 jde v obou
případech o jednu proměnnou. Dva podstromy mají disjunktní proměnné.

Při ∨ v kořeni jsou primes přesně primes levého a pravého podstromu.
Jejich sjednocená rodina zůstává kladný antichain: mezi neprázdnými
termy z disjunktních podpor nemůže být inkluze. Při ∧ jsou primes
všechny součiny jednoho levého a jednoho pravého prime. Jejich různost
a antichain plynou projekcí do obou disjunktních podpor. Corollary Q
tak v obou případech dává úplnost, nikoli jen vhodnou DNF.

Proto

    O_0=A_0=1,   O_k=2 A_(k−1),   A_k=O_(k−1)^2.

Jsou-li o_k,a_k délky jednotlivých prime termů, současně

    o_0=a_0=1,   o_k=a_(k−1),     a_k=2 o_(k−1).

Indukce také dokazuje, že všechny termy v jednom stromu mají stejnou
délku. Při k=0 kořenová značka nemá roli, ale základ vzorců je správný.

## P0622: uzavřené vzorce a celý příklad k=6

Dosazením do předchozích rekurencí a rozlišením parity k dostáváme

    O_k = 2^(2^ceil(k/2)−1),       o_k = 2^floor(k/2),
    A_k = 4^(2^floor(k/2)−1),      a_k = 2^ceil(k/2).

Například pro sudé k=2r má A_k exponent při základu 2 roven
2(2^r−1); O_(k−1)^2 jej dává okamžitě. Pro liché k=2r+1 je
O_k=2 A_(2r), tedy exponent 1+2(2^r−1)=2^(r+1)−1.
Zbylé parity plynou obdobně a délkové rekurence dávají uvedené mocniny.

Pro k=6 a ∧ v kořeni lze každý prime zapsat jednotně jako

    ∧_(a,b,c∈{0,1}) x_(a t_a b t_ab c t_abc)_2.

Na třech úrovních ∧ se berou obě větve a na třech úrovních ∨
jedna větev. Volby t_a, t_ab, t_abc jsou tedy nezávislé a je jich
2+4+8=14. Osm listů v součinu je různých; každá volba dává jiný
term a všechny termy mají tento tvar. Rozpis pro osm trojic (a,b,c)
je právě osm indexů v původní odpovědi. Počet je 2^14=4^7 a délka 8.
Jde o bijekci, nikoli o odhad či vyčíslený census.

## P0623: úloha 25, minimal vertex covers a rekurence

Pro n≥2 je f_n=∧_(i=1)^(n−1)(x_i∨x_(i+1)). Kladný term s množinou
proměnných C je implikant právě když C protíná každou hranu cesty P_n.
Je prime právě když je C inkluzně minimální vertex cover. Žádné záporné
prime termy nejsou možné podle monotónnosti. V minimálním cover má
každý vybraný vrchol alespoň jednoho nevybraného souseda; jinak by šel
odstranit. Tato podmínka je současně postačující pro minimalitu cover.

Pro n>4 rozlišíme poslední dvojici:

- Je-li n−1 vybrán, n vybrán není, protože by byl nadbytečný.
  Zbytek C∩{1,…,n−2} je právě minimální cover P_(n−2). Hrana
  (n−2,n−1) nemůže nikomu ze zbytku sloužit jako svědek minimality,
  takže platí obě implikace. Nový n−1 má soukromou hranu k n.
- Není-li n−1 vybrán, musejí být vybrány n−2 i n. Zbytek na
  {1,…,n−3} je právě minimální cover P_(n−3). Připojený n−2
  nesvědčí minimalitě n−3, zatímco n−2 a n mají nevybraného
  souseda n−1. Opět jde o bijekci oběma směry.

To přesně dává vytištěné tvary p_(n−2)∧x_(n−1) a
p_(n−3)∧x_(n−2)∧x_n a rekurenci a_n=a_(n−2)+a_(n−3).
Základy mají úplné seznamy:

    n=2: {1}, {2};
    n=3: {2}, {1,3};
    n=4: {1,3}, {2,3}, {2,4}.

Proto a_2=a_3=2, a_4=3. Pro prázdný součin n=1 je funkce 1
s jedním prázdným prime termem; vytištěná rekurence tento okraj
nepotřebuje a není na něj neoprávněně rozšiřována.

## P0624: celý dodatek o lexikografickém shellingu

Použijeme vzestupné lexikografické pořadí charakteristických bitových
vektorů, 0<1, s vrcholem 1 jako první souřadnicí. Podle definice
úlohy 35 je shadow S_B sjednocení všech singletonů C\B pro dřívější
cover C s |C\B|=1. Je třeba pro každý dřívější A dokázat A∩S_B≠∅.

Nechť i je první rozdílná souřadnice A a B. Pak A_i=0, B_i=1.
Je-li i>1, musí A_(i−1)=B_(i−1)=1, aby A pokrýval levou hranu.
Minimalita B tedy nutí i<n a B_(i+1)=0; jinak by i neměl nevybraného
souseda. Pro i=1 platí stejný závěr z koncové hrany. Současně
A_(i+1)=1, protože A_i=0. Položme j=i+1.

Množina D=(B\{i})∪{j} stále pokrývá cestu: jediná levá dotčená
hrana je kryta i−1 a obě pravé dotčené hrany pokrývá j. Zvolme
libovolný inkluzně minimální cover C⊆D. Vrchol j v něm musí zůstat,
protože i v D není a hrana (i,j) vyžaduje j. Žádný původní vrchol
v<i nelze odstranit: jeho nevybraný soused svědčící minimalitě v B
zůstal nevybrán, případně se i nově stal nevybraným. Změna j z 0 na 1
může odebrat svědka jen vrcholu i+2, nikoli levému prefixu.

Proto C má stejný prefix jako B do i−1, pak C_i=0, takže C je
dřívější než B. Navíc C\B={j}. Tedy j∈S_B a také j∈A,
což dokazuje požadovanou shelling podmínku pro každé A<B.
Jednoprvkové rodiny ji splňují vakuózně. Není zde zaměněno
vzestupné pořadí s klesajícím pořadím z jiné úlohy 36.

## P0625: Perrinův vzorec se všemi počátečními hodnotami

Původní p623 definuje P_3=3, P_4=2, P_5=5 a
P_n=P_(n−2)+P_(n−3). Tedy P_6=5, P_7=7. Zpětné pokračování
stejné rekurence dává P_2=2 (a dále P_1=0, P_0=3).
Položme b_n=(7P_n+10P_(n+1)+P_(n+2))/23. Lineární kombinace
posunutých řešení splňuje stejnou rekurenci jako a_n. Přímé základy:

    b_2=(14+30+2)/23=2,
    b_3=(21+20+5)/23=2,
    b_4=(14+50+5)/23=3.

Proto b_n=a_n pro všechna n≥2 indukcí, přesně jak uvádí odpověď.
Nejde jen o souhlas několika čísel: rekurence už byla obecně dokázána.
Známé rozšíření odpovědi 7.1.4–15 v erratech přidává mocninný vzorec
a bibliografii, ale nemění zde použitou definici. Jeho další tvrzení
nejsou tímto lokálním použitím prohlášena za auditovaná.

## Errata, rozsah a pokračování

Prohlédnuty relevantní záznamy all4a-pre, all4a, err4a, all4f0 a
all4f1. Pro 22–25 žádná relevantní oprava; známé zpřesnění pořadí
v příkladu úlohy 35 a rozšíření Perrinova odkazu jsou zohledněny.
Historické citace Knuth–Moore, Gurvich–Khachiyan, Lucas/Perrin a
jejich bibliografické priority nebyly nezávisle ověřeny.

P0618–P0625 jsou checked v uvedeném rozsahu. Strany 81 a 537
ještě obsahují úlohy/odpovědi 26–27 bez argumentu, proto nejsou
celostránkově uzavřeny. P84 byla použita jen definice shellingu,
p623 jen Perrinova definice. Nový nález ani kandidát nevznikl.
Hlavní text pokračuje p56/file73; další sekvenční úloha je 26.

Doplnění seznamu zdrojů: prohlédnuty také krátké historické vrstvy
errata/text/err4f0.txt a err4f1.txt; nepřidávají relevantní změnu
tohoto matematického bloku.
