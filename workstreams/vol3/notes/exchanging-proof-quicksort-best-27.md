# Quicksort 27: globální minimum, všechny prahy a svědek 546u

2026-11-07. Zadání 136/file147 a odpověď 632/file643 zobrazeny.
M≥1, k≥0 celá, N=3(M+1)2^k−1. Důkaz pokrývá celé obecné tvrzení
odpovědi i konkrétní případ N=23,M=3. Nejde jen o kontrolu svědka.
Početní model (16) přebírám z P1054; řešíme různé klíče a parametry,
pro které je program definován. Žádný výpočet, enumerace ani hledání.

## P1082 — přesný vážený stromový model a dosažitelnost nulových B/D/E

Nechť q=M+1. Každé konečné části délky m≤M přiřaďme váhu w=m+1,
tedy celé 1≤w≤q. Prázdná část má váhu 1 a také je listem. Pro uzel
délky n je n+1=(a+1)+(b+1), takže váhy se sčítají a celková váha je
W=N+1. Plný binární partition strom má A vnitřních uzlů a A+1 listů.
Počet S je počet vnitřních uzlů, jejichž obě děti jsou samy vnitřní.
Každý vnitřní uzel přidává do C právě svou váhu. Dvojím sečtením cest
od kořene tedy

    C=sum_(leaves i) w_i d_i,

kde d_i je hloubka listu. Cena bez společného 7N je alespoň
24A+4C+9S, protože B,D,E jsou nezáporné.

Pro každý platný strom lze této dolní ceně dosáhnout. Přidělme listům
rostoucí bloky ranků a uvnitř listů rostoucí pořadí. Od listů nahoru
zvolme pro uzel pivot odpovídající velikosti levé části a vstup
(pivot,L2,...,La,L1,R), kde L,R jsou již zkonstruované vstupy dětí.
Pro a=0 použijeme (pivot,R). Všechny menší klíče jsou souvisle před
většími, takže žádná Q6 není třeba; pivotová výměna vytvoří přesně
L,pivot,R (konstrukce P1045). Indukcí B=0 a listy jsou seřazené,
takže D=E=0. Stromový minimizační problém je proto přesně ekvivalentní
minimu skutečného programu, nikoli jen jeho relaxací.

## P1083 — redukce libovolného stromu na L listů stejné váhy q

Zde je W=Lq pro L=3*2^k. Každý strom má nejméně L listů, protože
jednotlivé váhy jsou ≤q. Zafixujme tvar stromu a hloubky všech listů.
Z podmínky 0≤w_i≤q, sum w_i=Lq plyne

    sum w_i d_i ≥ q * sum L nejmenších hloubek.

Důkaz: přesouvání váhy z hlubšího listu do neplného mělčího cenu
nezvyšuje; po naplnění L nejmělčích listů má každý váhu q a ostatní
váhu 0. Integrální W/q zajišťuje, že není zbytkový částečný list.
Toto mezikrokové povolení nuly slouží jen k dolní mezi.

Nulové listy potom odstraníme a potlačíme každý uzel s jediným
zbývajícím dítětem. Získáme plný binární strom T' s L listy váhy q.
Hloubky kladných listů se nezvýší, vnitřních uzlů je A'=L−1≤A.
Také S'≤S: každý uzel T' se dvěma vnitřními dětmi odpovídá původnímu
rozvětvení, v jehož obou větvích jsou aspoň dva vybrané listy; obě
původní děti tudíž také byly vnitřní. Mapování těchto uzlů je injektivní.
Potlačení cesty tedy nevytváří nový nepočítaný push.

Proto 24A+4C+9S je nejméně 24(L−1)+4qP(T')+9S(T'), kde P je
součet nevážených hloubek listů. Strom T' je i platným partition
stromem: každý list má délku M, každý vnitřní uzel nejméně dva takové
listy a tedy délku ≥2q−1>M. Tím lze pro hledání minima opravdu
omezit pozornost na L shodných listů, ačkoli původní algoritmus mohl
vytvářet prázdné i kratší části.

## P1084 — čistá dolní mez hloubek pro L=3*2^k

Pro plný binární strom platí Kraftova rovnost sum 2^(−d_i)=1:
každé rozdělení nahradí váhu uzlu dvěma polovinami. Položme D=k+1.
Pro každou celočíselnou hloubku d≥0 platí

    d ≥ D+2−2^(D+1−d),

s rovností právě pro d=D,D+1. Pro d≥D+2 je pravá strana <D+2≤d.
Pro d=D−j, j≥0, se nerovnost redukuje na 2^(j+1)≥j+2, což plyne
indukcí. Součtem a Kraftovou rovností dostaneme

    P(T')≥L(D+2)−2^(D+1)=L(k+5/3)=P0.

Konstrukce níže má L/3 listů v hloubce k+1 a 2L/3 v hloubce k+2,
takže čisté minimum P0 dosahuje. To ještě samo nestačí: jiné stromy
by mohly snížit počet push za cenu větších hloubek.

## P1085 — druhá dolní mez, která zahrnuje režii zásobníku

Označme Z počet vnitřních uzlů se dvěma listovými dětmi („cherries“).
Počet vnitřních hran je zároveň A'−1 a U+2S, kde U počítá uzly s
jedním vnitřním dítětem. Z A'=Z+U+S plyne Z=S+1. Pro pevné L je
tedy třeba minimalizovat P+lambda Z, kde lambda=9/(4q)≤9/8;
konstantu −9 a 24(L−1) lze přičíst na konci.

Nejdříve dokážeme pro každý plný binární strom s n≥3 listy mez

    P+(9/8)Z ≥ h(n),
    h(x)=x(log2(x/3)+49/24).

Pro jeden list je cena 0, pro dva listy 2+9/8=25/8, pro tři listy
5+9/8=49/8=h(3). Dále je 25/8>h(2), protože rozdíl je
−23/24+2log2(3/2)>1/24 (jelikož (3/2)^2>2).

Indukce: kořen se dvěma neprázdnými podstromy o a,b listech má
n=a+b a přidává n do P. Je-li a,b≥2 a n≥4, sám není cherry.
Striktní konvexita h a identita 2h(n/2)=h(n)−n dávají

    n+cost(a)+cost(b) ≥ n+h(a)+h(b) ≥ h(n).

Je-li a=1,b=n−1, pak n≥4 a stačí h(n)−h(n−1)≤n.
Máme h'(x)=log2(x/3)+49/24+1/ln2. Platí ln2>2/3 (například
z přísné konvexity 1/x a integrálu na [1,2]) a log2(4/3)<5/12,
protože 2^19=524288<3^12=531441. Proto h'(4)<95/24<4.
Funkce x−h'(x) má pro x≥4 derivaci 1−1/(x ln2)>0, takže
h'(n)<n a integrál derivace na [n−1,n] je nejvýše h'(n)<n.
To dokončuje i silně nevyvážený případ a celou indukci.

Pro L=3*2^k je h(L)=P0+(9/8)(L/3). Konstrukce níže má právě
Z0=L/3 a rovnost. Tím je dokázána dolní mez včetně dostatečně velké
penalizace cherry; argument neignoruje alternativní tvary stromu.

## P1086 — všechny M≥1 a obecná optimální konstrukce

Pro 0≤lambda≤9/8 je P+lambda Z konvexní kombinace hodnot P a
P+(9/8)Z. Obě předchozí dolní meze má stejná konstrukce, takže

    P+lambda Z ≥ P0+lambda Z0.

To zahrnuje lambda=9/(4q) pro všechna M≥1. Po P1083 a Z=S+1
dostáváme globální minimum 24(L−1)+4qP0+9(Z0−1), bez 7N.

Dosahující strom nejprve k-krát půlí váhu W. Má 2^k koncových
podstromů váhy 3q, tedy délek 3M+2. Každý z nich se rozdělí na váhy
q a 2q, a druhá část na q,q. To je přesně tištěná „trisection“.
Každý takový trojlist má hloubky 1,2,2 a jedinou cherry; nad nimi
jsou k dokonale vyvážené úrovně. Všechny listy mají délku M a
P1082 zajišťuje realizaci s B=D=E=0.

Je L=3*2^k, takže A=L−1. Push vzniká jen na horních k úrovních,
celkem S=2^k−1. Každá horní úroveň přidá do C celou váhu W a
každý trojlist přidá 3q+2q=5q, tedy

    A=3*2^k−1, C=(k+5/3)(N+1), S=2^k−1, B=D=E=0.

To jsou všechny obecné vzorce odpovědi 27 i důkaz jejich globální
časové optimality. Případ k=0 obsahuje jen trojlist, takže S=0;
žádný skrytý záporný počet úrovní nebo neexistující push nevzniká.

## P1087 — celý konkrétní svědek pro N=23,M=3

Tištěný vstup je

    12,2,3,1,8,6,7,5,9,10,11,4,
    16,14,15,13,20,18,19,17,21,22,23.

Každá fáze má již všechny menší klíče před většími, takže Q6 nenastane.
Úplný seznam aktivních intervalů, pivotů a závěrečných pivotových výměn:

| Interval | Pivot | Poslední výměna | C fáze | Zásobník po fázi |
|---|---:|---|---:|---|
| [1,23] | 12 | (1,12) | 24 | [13,23] |
| [1,11] | 4 | (1,4) | 12 | [13,23] |
| [5,11] | 8 | (5,8) | 8 | po pop prázdný |
| [13,23] | 16 | (13,16) | 12 | prázdný |
| [17,23] | 20 | (17,20) | 8 | prázdný |

Po první výměně je levý vstup 4,2,3,1,8,6,7,5,9,10,11.
Po druhé má první blok 1,2,3 a zbytek začíná 8,6,7,5; třetí výměna
z něho vytvoří 5,6,7,8,9,10,11. Stejný průchod pravé části mění
16,14,15,13 na 13,14,15,16 a 20,18,19,17 na 17,18,19,20.
Všechny šestice konečných tříprvkových listů jsou tím rostoucí,
ostatní prvky jsou pivots 4,8,12,16,20. Q9 nic neposune.

## P1088 — přesná cena a uzavření zadání

Z úplného průchodu A=5,C=64,S=1 a B=D=E=0. Proto

    24*5+4*64+7*23+9=120+256+161+9=546u.

P1083–P1086 pro q=4,L=6 dokazují, že žádná jiná permutace 1..23
nemůže mít menší cenu, ani kdyby měla jiné velikosti listů nebo méně
push. Pro úplnost: kandidátní strom současně dosahuje všech dolních
mezí, takže nejde o nekonzistentní součet minim různých vstupů.

Pět dodaných vrstev je v `sources/exchanging-errata-review.json`;
není v nich matematická změna odpovědi 27. Bibliografické autorství
Sedgewick se zde samostatně neověřuje, ale vlastní argument pokrývá
celé tvrzení. Nový nález nevznikl. Následuje náhodný pivot(27) na
121 a varianty od 122, nikoli opakování právě uzavřených extrémů.
