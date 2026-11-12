# Generátory, komplementy a hranové grafy: str. 24–26, §7–73 až 88

6. listopadu 2026. Cílené argumenty bez nového programu a bez censu.
Původní zadání file058–059, odpovědi proof-file541/542; obrázky a vzorce
textu převzaty z předchozího celostránkového čtení file041–043.
Rozsah níže přesně odděluje matematické důsledky od datových tvrzení.

## Generátory na str. 24–25

plane_miles: 129 vrcholů a 381 hran splňují 3·129−6=381, jak má
triangulace s vrcholem INF. Počet 128 měst, jejich souřadnice, konkrétní
Delaunay hrany a absence degenerací nebyly nově ověřeny; jde o partial.
Obecné geometrické vlastnosti Delaunay triangulace nejsou zde dokazovány.
F0 oprava „smallest circle“ na „there is a circle“ je již v dotisku 4A.

plane_lisa: pixelové počty 3027/5967 neověřeny; známá oprava posledního
parametru 2295000→22950000 aplikována. Kontrakce souvislých pixelových
oblastí rovinného rookwise grafu zachová rovinnost; odstranění smyček
a násobností ji nezmění. Proto popsaný graf oblastí je rovinný.
bi_lisa: rozdělení na 360 řádků a 250 sloupců dokazuje bipartitnost
a počet 610 vrcholů. Údaj 40923 hran a konkrétní pixel nejsou ověřeny.

raman(31,23,3,1): (23³−23)/2=6072 a 6072·32/2=97152.
raman(5,37,4,1): 37³−37=50616 a 50616·6/2=151848.
Jsou to ověřené aritmetické důsledky udaných parametrů, nikoli důkaz
regularity generátoru. Girth/diameter 4/4 a 10/10, bipartitnost druhého
grafu, maticový model a příklad hrany zůstávají partial.

random_graph: popsané odmítání smyček/duplicit udržuje jednoduchý graf
a po 5000 přidáních má právě 5000 hran. Konkrétní seed, izolovaný vrchol
908, komponenta 999 a vzájemná podmnožinovost obou běhů nejsou reprodukovány.

subsets: pětice z 11 bodů mají binom(11,5)=462 možností.
Disjunktní pětice k dané pětici vybíráme ze šesti zbývajících prvků:
stupeň binom(6,5)=6 a hran 462·6/2=1386.
Průnik velikosti 4 znamená odebrat jeden z 5 a přidat jeden ze 6:
stupeň 30 a hran 6930. Pro dvojice z pěti bodů jde o KG(5,2), jehož
Petersenův model je již dokázán v proof-007. Shoda konkrétního SGB
hexadecimálního parametru s popisem nebyla znovu trasována ve zdroji.

parts: vrcholový počet je koeficient x³⁰ v ∏_(i=1)^10 (1−x^i)^−1
konjugací partition. Hodnoty 3590 a 31377 se nově nepočítaly.
Ukázkový oblouk dělí 13 na 7+6; součet 30 a orientaci k delší partition zachová.

simplex: stars-and-bars dává binom(13,3)=286.
Orientovaný jednotkový přenos z i do j, i≠j, je možný pro
binom(12,3)=220 kompozic s x_i≥1. Je 12 uspořádaných párů souřadnic,
takže neorientovaných hran je 12·220/2=1320.
Příklad 3.1.4.2→3.0.4.3 je přenos ze druhé do čtvrté souřadnice.
Známá oprava zápisu souřadnic je aplikována.

Knight na m×n má pro m,n≥2 celkem
2((m−1)(n−2)+(m−2)(n−1)) hran: počítej kladný posun řádku 1 nebo 2
a oba směry sloupce. Pro 8×8 je to 168; ukázkový 6×9 má 134.
Bishop 8×8 má v každém ze dvou směrů diagonál délky
1,2,...,7,8,7,...,2,1. Počet hran je
2(2Σ_(j=1)^7 binom(j,2)+binom(8,2))=2(2·56+28)=280.
Pravidla δ₁²+δ₂²=5 dávají právě knight; pro p=−2 jsou směry
(±1,±1) a libovolný kladný násobek, právě bishop.
Vykreslené konkrétní hrany obou obrázků ve Fig. 5 nebyly jednotlivě očíslovány;
jejich úplná obrazová identifikace je partial.

## Komplement a hranový graf na str. 26

Komplement přepne každou mimodiagonální dvojici a ponechá nuly na diagonále;
proto je involucí a A+bar(A)=J−I. Komplement K_n je prázdný graf.
Hranový graf L(K_n) má binom(n,2) vrcholů; hrana uv má n−2 sousedních
hran u–x a n−2 hran v–y, disjunktně, tedy stupeň 2n−4.
Barvení hran je z definice barvení vrcholů L(G).
Zohledněno známé slovní zpřesnění „two edges of G“ z 23. 4. 2011.

Sjednocení rook a bishop hran je přesně queen pohyb. Disjunktní
sjednocení spojuje pouze vrcholy uvnitř jednotlivých částí;
komplement disjunktního sjednocení úplných grafů je tedy úplný
multipartitní graf, což dokazuje (38)–(39). Každý graf je disjunktním
sjednocením komponent, protože mezi nimi není hrana. Join k součtu
přidá všechny mezitřídní dvojice; directed join jen z první části do druhé.
Konkrétní volání gunion nebylo provedeno; jeho grafový význam je správný.

## Úlohy 73–77

73: Jednoduchý bezsmyčkový graf na 10 vrcholech s 45=binom(10,2)
hranami musí být K10. Analogicky jednoduchý digraf s povolenými
smyčkami a 100=10² oblouky musí být J10. Tento argument přebírá
zadané pravidlo random_graph, neověřuje konkrétní běh PRNG.
74: badness s out-degree 22 a ostatní s out-degree≤20 jsou datový
census roget; partial, bez spuštění generátoru.

75: Parametry v odpovědi jsou ověřeny proti pravidlům zadání.
Pro jednu souřadnici a |p|=1 jsou základní posuny ±1; záporné p
povolí všechny kladné násobky. p=2 v jedné dimenzi nemá celočíselný
základní posun a dává prázdný graf. Proto:
(a) (n,0,0,0,−1,0,0) dává všechny dvojice;
(b) (n,0,0,0,1,0,0) jen sousední místa;
(c) (n,0,0,0,1,1,0) přidá cyklické zabalení;
(d)–(f) stejné tři s o=1 ponechají kladnou orientaci;
(g)–(i) (m,n,0,0,1,w,0), w=0,2,3, dávají grid/cylinder/torus;
(j) (m,n,0,0,−1,0,0) povolí libovolnou vzdálenost v řádku/sloupci;
(k) (m,n,0,0,1,3,1) je directed torus;
(l) (n,0,0,0,2,0,0) je prázdný graf;
(m) (2,−n,0,0,1,0,0) opakuje n souřadnic délky 2 a mění právě jednu.
Rozměry jsou kladné jako v zadání. C1/C2 se chápou jako multigrafy,
jak kniha výslovně stanoví na str. 13. Ukázka opakování 2,3,5 do délky 7
má 2·3·5·2·3·5·2=1800 vrcholů.

76: Při p=1 a wrap na jednorozměrné desce délky 1 vznikne smyčka;
pro délku 2 obě cyklické sousednosti dávají paralelní hrany.
Pro p<0 generátor podle popsané konvence skončí před návratem y=x,
takže smyčky nepřidá. Implementační stop-podmínka nebyla nově trasována.

77: Vyber x,y s d_G(x,y)≥3. V komplementu je xy hrana.
Žádný další v není v G sousedem současně x i y, takže v je
v komplementu soused alespoň jednoho z nich. Libovolné u,v spojíme
přes x–y cestou délky nejvýše 3. Funguje i pro nekonečný průměr G.

## Úloha 78: celé tvrzení i malé případy

(a) Počet hran je n(n−1)/4, tedy n≡0 nebo 1 mod 4.
Pro n<8 jsou možné pouze n=0,1,4,5. U n=4 mají stupně 1,1,2,2
(stupně 0 a 3 by se musely vyskytovat současně, což nelze);
jediný samodoplňkový typ je P4. U n=5 jsou možné stupně pouze 1,2,3,
s týmž počtem 1 a 3. Graf je souvislý: bez izolací by rozklad 2+3
měl nejvýše 4 hrany místo 5. Je tedy unicyklický.
Pět stupňů 2 dává C5. Sekvence 3,2,2,2,1 dává buď C4 s přívěskem,
nebo trojúhelník s cestou délky 2; tyto dva jsou vzájemnými komplementy,
nikoli samodoplňkové. Sekvence 3,3,2,1,1 dává jedině bull
(trojúhelník a po listu u dvou jeho vrcholů), který je samodoplňkový.
Celkem jsou K0,K1,P4,C5,bull, jak uvádí odpověď.

(b) Lichá mocnina φ přepíná hranu/nehranu, proto nemůže fixovat
neuspořádanou dvojici. Cyklus liché délky >1 by příslušnou lichou
mocninou fixoval alespoň dva vrcholy; cyklus délky 2 mod 4 by
lichou mocninou prohodil protilehlé dva vrcholy. Obojí je spor.
Zbývají cykly délky dělitelné 4 a nejvýše jeden fixní bod.
Pro n≡0 mod4 nemůže být ani ten jeden fixní bod.

(c) Na neuspořádaných dvojicích má indukovaná permutace jen sudé cykly:
mezi dvěma cykly vrcholů je délka lcm jejich délek; uvnitř cyklu
délky 4r je délka 4r, nebo 2r u protilehlé dvojice.
Nezávislé střídání černé/bílé v každém takovém cyklu dá požadovaný
graf. Pro t párových orbit je přesně 2^t voleb.

(d) Pro n≡1 mod4 je právě jeden fixní vrchol a ostatní cykly mají
délku dělitelnou 4. Páry k fixnímu bodu mají jednu orbitu na každý
ze zbývajících r cyklů, tedy 2^r rozšíření každého odpovídajícího
grafu bez fixního bodu. F0 oprava „all multiples of 4“→„all even“
u párových orbit je již zahrnuta v původní sazbě 4A.

## Úlohy 79–80: obě parametrické konstrukce

79, řešení 1: V kladných vrcholech 1,...,4k je každá třída modulo 4
velikosti k. Vrchol residue r se pojí se třídami −r a 1−r.
Pro sudé r se započte i sám, takže má 2k−1 kladných sousedů a
navíc hranu do 0; lichý r má rovnou 2k kladných sousedů. Vrchol 0
má 2k sudých sousedů. Graf je 2k-regulární.
φ=(1 2 ... 4k), φ(0)=0, zvětší součet residuí o 2 modulo 4,
tedy přepne podmínku {0,1} na {2,3}; současně přepne paritu souseda 0.
Je to samodoplňkový graf i pro k=0.

79, řešení 2: Každý blok má cestu b–a–c–d a hrany 0–b,0–d;
všichni čtyři mají lokální stupeň 2. Mezi bloky i<j je předepsaný
8-cyklus, každý vrchol tedy získá 2 sousedy za každý další blok.
Stupně jsou znovu 2k včetně 0.
Tabulka hran mezi bloky v pořadí a,b,c,d má řádky
1100,1001,0011,0110. Současný cyklický posun řádku i sloupce ji
přepne na doplněk. Totéž platí pro vnitřní cestu a pro hrany k 0.
Permutace (a b c d) v každém bloku je proto správná.

80: V E1 se každý dřívější blok pojí ke všem b,d pozdějšího bloku,
v E2 ke všem a,c. Permutace φ obě tyto poloviny přepne na doplněk
a také přepne vnitřní cesty; totéž udělá s přidanými hranami do 0.
V E0∪E1 jsou vrcholy různých bloků ve vzdálenosti ≤2:
k nenapojenému pozdějšímu a/c vede cesta přes jeho b/d souseda.
V jednom bloku mají všechny dvojice vzdálenost ≤2 kromě konců b,d;
u posledního bloku je spojí libovolný dřívější vrchol, jinde společný
soused v pozdějším bloku. Pro k≥2 je proto průměr 2.
V E0∪E2 má poslední b a d každý jen jediného souseda a,c;
nemají společného souseda a jejich vzdálenost je 3 po b–a–c–d.
Ostatní páry mají vzdálenost ≤3 stejným argumentem jako výše.
Po přidání 0 je jeho vzdálenost do každého vrcholu ≤2; b_k,d_k
nadále nemají společného souseda v případu E2. Tím jsou obě části hotové.
Známé upřesnění úvodní věty na „two or more vertices“ je aplikováno.

## Úlohy 81–88

81: Samodoplňkový digraf řádu 3 má tři z šesti možných oblouků.
Buď má mezi každou dvojicí právě jeden oblouk (dva turnaje: tranzitivní
a cyklický), nebo má jednu obousměrnou dvojici a jediný další oblouk
(do dvojice nebo z dvojice). To jsou přesně čtyři uvedené typy;
všechny jsou izomorfní doplňku (u posledních prohoď osamocený vrchol
s koncem obousměrné dvojice, který se dotýká třetího oblouku).
Počty typů podle počtu oblouků 0,...,6 jsou 1,1,4,4,4,1,1, celkem 16:
pro dva oblouky jsou out-star, in-star, cesta a obousměrná dvojice.
Počty self-converse typů jsou 1,1,2,2,2,1,1, celkem 10; komplement
zachová tuto vlastnost. Žádný programový census.

82(a): Po vložení G do G′ ber jeho hrany jako podmnožinu vrcholů L(G′).
Jejich vzájemné incidence se nezmění, takže L(G) je indukovaný podgraf.
(b): Hrana uv má d(u)+d(v)−2 sousedů, u d-regulárního grafu 2d−2.
(c): U K_m,n je stupeň každého hranového vrcholu m+n−2.
(d): K_1,1,2 má stupně 3,3,2,2 a 5 hran; jeho line graph má stupně
4,3,3,3,3, tedy 8 hran a není regulární.
(e): Hranu a_i b_j mapuj na souřadnice (i,j); incidence je právě
shoda jedné souřadnice, tedy K_m □ K_n.
(f): Jediné neadjacentní dvojice hran K4 jsou tři páry protilehlých hran,
tedy L(K4)=K_2,2,2. (g): Po sobě jdoucí hrany P_(n+1) tvoří P_n.
(h): Každá netriviální komponenta dává jednu komponentu L(G);
izolované vrcholy žádnou. Rovnost počtů tedy vyžaduje absenci izolací.

83: Komplement L(K5) má jako vrcholy dvojice z pěti bodů a hrany
mezi disjunktními dvojicemi. Je to KG(5,2), již doložený Petersenův
model z proof-007. Přesný pruh komplementace byl ověřen v zadání.

84: Rook graph L(K3,3) má souřadnice (u,v) nad F3.
Zobrazení (u,v)→(u+v,u−v) je invertibilní, protože determinant −2≠0.
Rozdíl s právě jednou nulovou souřadnicí změní na dvě nenulové;
jsou-li obě nenulové, nad F3 jsou stejné nebo opačné a právě jedna
transformovaná souřadnice je nula. Tedy jde o izomorfismus na komplement.

85: Je-li G≅L(G), musí e=n a také počet hran L(G)=n.
Z Σd_i=2n a Σd_i(d_i−1)=2n plyne Σ(d_i−2)²=0.
Všechny stupně jsou 2, takže podle 58 jde právě o disjunktní sjednocení
cyklů délky alespoň 3 (včetně prázdného sjednocení).
Obráceně každá taková komponenta je izomorfní svému line graphu.

86: Použij trojúhelník ABC s jedním listem a,b,c u A,B,C.
Komplement má kliku a,b,c a vrcholy A,B,C připojené vždy k druhým
dvěma listům. Izomorfismus do L(G) je
a→BC, b→CA, c→AB, A→Aa, B→Bb, C→Cc.
Všech devět hran komplementu souhlasí s incidencemi v L(G).

87(a): V modelu KG(5,2) dej barvu 1 dvojicím obsahujícím 1,
barvu 2 zbývajícím dvojicím obsahujícím 2, barvu 3 dvojicím z {3,4,5}.
V každé třídě se dvojice protínají, tedy žádná není hranou Petersena.
(b): Tři barvy na hranách vnějšího C5 musejí mít četnosti 2,2,1;
po odebrání ojedinělé barvy zbylé čtyři hrany alternují. Až na symetrii
jsou barvy vnějších hran A,B,A,B,C, a proto spokes B,C,C,C,A.
Vnitřní hrany z vrcholu 0 do 2 i 3 pak musejí mít barvu A,
spor s řádným barvením. Tištěný argument je tím doplněn.
Brooksova obecná věta v závorce je externí vstup, zde není potřebná;
její historický článek a ostatní atribuce v tomto bloku nebyly ověřeny.

88: Označ r počet vrcholů obvodu. Jediný cyklus bez středu je C_r.
Každý cyklus se středem určí dva odlišné obvodové konce a jeden
ze dvou obvodových úseků, tedy 2·binom(r,2)=r(r−1) cyklů.
Celkem 1+r(r−1). V původním značení r=n−1 odpovídá prvnímu dotisku;
v opraveném značení W_n s n spokes je r=n.
Indukované jsou obvod a právě r trojúhelníků u středu:
delší obvodový úsek má chord ze středu do svého vnitřního vrcholu.
Známá změna zadání i odpovědi z 23. 12. 2015 je aplikována.

## Návaznost

Str. 24–26 a úlohy 73–88 mají výše samostatný argument nebo přesnou mezeru.
Relevantní errata all4a-pre/all4a/err4a/all4f0/err4f0 byla zohledněna.
Při navazující odpovědi 90 vznikl F0002: samostatně doložený obecný
podgraf K4→P4 vyvrací chybějící slovo „induced“. Nevztahuje se na tuto
klasifikaci komplementů ani na správné zadání. Pokračování: p27 a §7–89.

X0056 doplňuje dříve otevřené zdrojové detaily: P0246 v proof-025 má
obecný důkaz stop-podmínky před vložením hrany a ukončení pro p<0.
P0233 v proof-026 má přesnou normalizaci, úplný generovací invariant
a bitové masky pro všechna tři vytištěná subsets volání. Primární
zdroj uložen beze změn; nic se nekompilovalo ani nespouštělo. Ostatní
SGB datové/obrazové a Delaunay položky zůstávají oddělené.

## Doplnění X0057 — plane_miles

Původní neověřené části výše jsou nyní přesně rozděleny v
[proof-027](proof-027-delaunay-geometry-and-examples.md). P0505 dokazuje
obě geometrické implikace za explicitní obecné polohy; P0506 literal
128 měst, transformaci a 129 vrcholů; P0507 všechny tři příklady hran
striktními certifikáty. P0221 zůstává partial pro globální degenerace
původních souřadnic, celý inkrementální program a geografickou historii.
Samotný aritmetický počet P0220 se nerozšiřuje na změřený výstup.
