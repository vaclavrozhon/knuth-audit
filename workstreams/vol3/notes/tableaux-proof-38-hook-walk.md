# Tableaux38: celý pravděpodobnostní důkaz hook walk

Zadání70/file81, odpověď613/file624; oba originály již zobrazené.
Stávající C0008 (nesprávný základ k=l=1 místo k=l=0) se přebírá
v jeho dříve doloženém rozsahu, bez nového výpočtu/protipříkladu.
Následuje samostatný obecný důkaz všech částí úlohy i odpovědi.
Známá oprava „column sets“2006 je pouze jazyková, není nálezem.

## P0576: graf, ukončení a přesný počet cest se zadanými množinami

Neprázdný Youngův tvar T má N buněk, délky řádků λ_i a sloupců
λ′_j. Z(i,j) vedou hrany do všech buněk vpravo ve stejném řádku
a dole ve stejném sloupci. Jejich počet je
d_ij=λ_i−j+λ′_j−i=H_ij−1. Každá hrana striktně zvyšuje i+j,
tedy nevzniká cyklus; každá procházka skončí v rohu s d=0.

Fixujme roh(a,b), I={i_0<…<i_k=a} a J={j_0<…<j_l=b}.
Celý obdélník1,…,a ×1,…,b patří do T. Cesta s přesně těmito
množinami musí začínat v(i_0,j_0) a každým krokem přejít buď
k následujícímu prvku I, nebo k následujícímu prvku J. Přeskočený
prvek by už kvůli monotónnosti nikdy nemohl navštívit.
Naopak každé promíchání k svislých a l vodorovných kroků na této
zmenšené mřížce dává platnou cestu v původním grafu; jeho hrany
smějí přeskočit původní řádky/sloupce mimo I,J. Počet je proto
přesně binom(k+l,k), včetně hodnoty1 při k=l=0.

## P0577: rozklad stupně, který skutečně způsobuje zkrácení

Protože(a,b) je roh, platí λ_a=b a λ′_b=a. Pro i≤a,j≤b tedy

    d_ij=d_ib+d_aj.                                      (1)

Pravá strana je (λ_i−b+a−i)+(b−j+λ′_j−a), což se rovná
levé. Položme u_r=d_(i_r,b), v_s=d_(a,j_s). Pro r<k je u_r>0,
pro s<l je v_s>0, zatímco u_k=v_l=0. Žádný níže použitý
neprázdný součin neobsahuje nulový terminální stupeň.

## P0578: část(a), všechny indukční větve a správný základ

Označme P(I,J) úplnou pravděpodobnost události včetně uniformního
výběru startu z N buněk. Tvrdíme

    P(I,J)=1/(N·∏_(r<k)u_r·∏_(s<l)v_s).                (2)

Pro k=l=0 není žádná hrana: jde pouze o výběr rohu jako startu,
s pravděpodobností1/N. To je správný základ; C0008 eviduje jiný
vytištěný základ, nikoli nepravdivost samotného vzorce(2).

Je-li k>0,l=0, první hrana musí odstranit i_0 z I. Proto
P(I,J)=P(I\{i_0},J)/d_(i_0,b), což zkrátí přesně u_0.
Analogicky pro k=0,l>0 se zkrátí v_0. Pro k,l>0 má první hrana
dvě možnosti a

    P(I,J)=[P(I\{i_0},J)+P(I,J\{j_0})]/d_(i_0,j_0).

Tato rovnice zahrnuje uniformní start správně: každý ze dvou
podproblémů má faktor1/N, zatímco přidání první konkrétní hrany
přidá právě1/d_(i_0,j_0). Po dosazení indukce je čitatel
(u_0+v_0)/(N∏_(r<k)u_r∏_(s<l)v_s). Rovnost(1) jej zkrátí
na(2). Tím jsou pokryty všechny k,l≥0 bez dělení nulou nebo
odkazu na nedefinovanou prázdnou množinu řádků/sloupců.

## P0579: část(b), součet disjunktních událostí a podíl f

Každá cesta končící v(a,b) má jednoznačné I,J. Jejich ostatní
prvky jsou libovolné podmnožiny {1,…,a−1} a {1,…,b−1};
P0576 zaručuje existenci všech těchto cest. Součtem(2) tedy
pravděpodobnost koncového rohu je

    p_(a,b)=N^−1 ∏_(i<a)(1+1/d_ib) ∏_(j<b)(1+1/d_aj).  (3)

Definujme f(T)=N!/∏_(c∈T)H_c, prozatím jen kladné racionální
číslo, a f(∅)=1. Odstranění rohu zmenší délku háčku právě
buňkám nad ním v jeho sloupci a vlevo od něj v jeho řádku o1;
ostatní háčky se nemění, samotný odstraněný má délku1.
V podílu f(T\{(a,b)})/f(T) se proto zkrátí faktoriály na1/N
a dotčené háčky přispějí H/(H−1)=(d+1)/d. Výsledek je přesně(3).
Nikde nebyl předpokládán háčkový vzorec pro počet tableaux.

## P0580: první část(c), nezávislá rekurence pro počet tableaux

Každá procházka skončí v právě jednom rohu, proto součet(3)
přes všechny rohy je1. Z P0579 tedy

    Σ_(c roh T) f(T\{c})=f(T).

Skutečný počet standardních tableaux má tutéž rekurenci: největší
štítek N musí být v rohu; po jeho odstranění zbývá libovolné
standardní tableau menšího tvaru a obráceně je možné N připsat.
Oba počty mají základ1 pro prázdný tvar, takže se indukcí rovnají.
Jde o celý požadovaný pravděpodobnostní důkaz Theorem H.

## P0581: druhá část(c), uniformita, hranice a počet náhodných voleb

Po procházce umístíme aktuální největší štítek do jejího koncového
rohu a opakujeme s čerstvými uniformními volbami na menším tvaru.
Pro pevné výsledné tableau je posloupnost odstraňovaných rohů
jednoznačná: T_N=T,T_(N−1),…,T_0=∅. Součin podmíněných
pravděpodobností této posloupnosti teleskopuje:

    ∏_(r=1)^N f(T_(r−1))/f(T_r)=1/f(T).

Každé tableau tedy dostává stejnou pravděpodobnost. Jednobuňkový
tvar provede jen jeden jistý výběr startu, žádnou hranu; prázdný
tvar se vyplní prázdně bez náhodné volby. Procházka na r buňkách
navštíví nejvýše r různých buněk, tedy provede nejvýše r−1
výběrů hran a jeden výběr startu. Celkem je nejvýše N(N+1)/2
takových voleb. To je prostá obecná horní mez počtu voleb, nikoli
neprokázané tvrzení o konstantní implementační ceně uniformního
výběru nebo o optimální očekávané době.

Úplný původní článek Greene–Nijenhuis–Wilf1979 nebyl bibliograficky
přezkoumán. Všechny použité matematické kroky jsou zde vlastní;
nový nález ani numerický běh nevznikl.
