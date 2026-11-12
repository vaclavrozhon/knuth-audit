# Batcher11: globální maximum, konstrukce a asymptotický poměr

7. listopadu2026. Zadání134/file145, odpovědi629–630/file640–641
a celá geometrie113/file124 zobrazeny. P0986–0992 již dokazují
skládání cest; P1003–1011 počty porovnání. Zde tyto výsledky
přebíráme a doplňujeme váhu každé hrany a vlastní maximalizaci.
Žádná enumerace permutací, cest ani numerický matematický běh.
Všech pět vrstev pro tento blok je v
`sources/exchanging-errata-review.json`; žádná změna zdejších
maximalizačních vzorců není uvedena. Sedgewickův bibliografický
odkaz zatím není externě prověřen; jeho uvedené tvrzení je
níže odvozeno samostatně.

## P1012: přesná váha hrany a počet všech výměn při slučování

Nechť f(k) je počet změn sousedních bitů v nezáporném k,
s nekonečným prefixem nul. Tedy f(0)=0 a
f(k)=popcount(k xor⌊k/2⌋). Pro kladnou mocninu2 m a m≤k<2m
platí

    f(k)=1+f(2m−k−1).                                  (1)

Vrchní1 přidá jednu změnu proti vedoucí0; nižší bity se
odrazem doplní, takže všechny jejich vzájemné změny zůstanou
a přechod k vrchnímu bitu je právě nový vedoucí přechod
doplněného čísla. To dokazuje(1), včetně obou krajů.

Cesta dvou uspořádaných podposloupností má výšku h=i−j.
Každá jednotková hrana překračuje právě interval[h,h+1].
První složení odráží intervaly h<0; další složení o přímce m
odráží intervaly h≥m. Jejich nové dolní konce jsou −h−1,
respektive2m−h−1. Počet odrazů jednoho původního intervalu
nezávisí na orientaci hrany ani na ostatní cestě. Z(1) a
postupně půlených m proto vychází

    R(h)=f(h)                    pro h≥0,
    R(h)=1+f(−h−1)               pro h<0.              (2)

Kapacita2^t stačí: po absolutní hodnotě má každý interval
dolní konec≤2^(t−1)−1, tedy všechny jeho možné vrchní bity
postupné osy2^(t−2),…,1 pokryjí. Pro N=2 nejsou další
osy a stejné vzorce platí přímo.

Při každém složení je počet výměn polovinou počtu odražených
hran: páry z P0991–0992 mají jednu svislou a jednu vodorovnou
hranu. Alternativně počet průchodů každou odráženou hladinou
nahoru i dolů souhlasí. Cesta totiž začíná ve výšce0 a končí
ve výšce0 pro sudé N, ve výšce1 pro liché N. Jediná možná
nevyvážená hladina je h=0, ale ta se nikdy neodráží.

Označ U_h počet původních svislých hran přes interval[h,h+1]
a D_h vodorovných. Máme U_h=D_h kromě případného U_0=D_0+1,
a R(0)=0. Sečtením odrazů po všech průchodech tedy dostaneme

    exchanges=½Σ_h(U_h+D_h)R(h)=Σ_h U_h R(h).           (3)

To je přesně váha odpovědi16: svislá hrana z(i,j) do(i+1,j)
má f(i−j) při i≥j a1+f(j−i−1) při i<j. Je prokázána
pro každý konkrétní vstup, i lichou délku. Netvrdíme chybně,
že původní svislá hrana představuje samostatnou výměnu při
každém svém odrazu; takové přiřazení by selhalo při změně
orientace. Rovnost(3) používá vyváženost celé cesty.

## P1013: proč lze maximum hledat nad diagonálou, také při lichém N

Pro uzavřený kladný výlet od h=0 zpět do0 nahradíme h jeho
zápornou hodnotou. Počty obou orientací každé hladiny výletu
souhlasí. Váha f(h) na hladině h≥0 se změní na1+f(h)
na hladině−h−1. Každý takový výlet tím přísně získá.
Pro sudé N tedy některá optimální cesta leží celá v h≤0.

Pro liché N vezměme poslední krok0→1. Před ním lze právě
uvedeným způsobem odstranit všechny kladné výlety. Za ním
je uzavřený výlet z1 do1, který již neklesá pod1. Nahradíme
jej odrazem h↦1−h, umístíme před závěrečný krok0→1 a tento
krok přesuneme na úplný konec. Váha původní hladiny h≥1
se změní z f(h) na1+f(h−1), což není méně.

Poslední nerovnost je doložena přímo: Grayovy vektory
G(h)=h xor⌊h/2⌋ a G(h−1) se liší právě v jednom bitu.
Piš h xor(h−1)=2^(v_2(h)+1)−1; xor s jeho posunem
zruší všechny bity kromě2^v_2(h). Proto
|f(h)−f(h−1)|=1 a f(h)≤1+f(h−1).

Maximum pro délku2n+1 je tedy stejné jako pro2n: optimální
nezáporná hloubková cesta s n kroky každého druhu a na konci
jediný dodatečný svislý krok nulové váhy. Pro2n se tento
dodatečný krok vynechá. Zde n=⌊N/2⌋≥1.

## P1014: úplná horní mez přes hloubky a dosažitelná cesta

V h≤0 piš hloubku d=−h. Každý návrat z d do d−1 má
váhu v(d)=1+f(d−1), d≥1. Cesta s n návraty, která dosáhne
největší hloubky M, musí každý z návratů d=1,…,M provést
alespoň jednou. Ostatních n−M návratů má váhu nejvýše
K=max_(d≤M)v(d). Proto její celková váha je nejvýše

    Σ_(d=1)^M v(d)+(n−M)K.                            (4)

Nechť M_K je první hloubka s váhou K. Přesunutí všech
povinných návštěv hlubších než M_K na tuto nejlepší hladinu
(4) nezmenší, protože každá odstraněná váha je≤K. Tím
dostáváme horní mez

    K n−P_K,   P_K=Σ_(d=1)^M_K(K−v(d)).               (5)

Je dosažitelná cestou, která nejprve jde M_K kroků vodorovně,
potom n−M_K krát svisle a vodorovně, a nakonec M_K krát
svisle. Všechny nadbytečné návraty mají právě váhu K.
Maximalizace všech cest se tak přesně redukuje na rekordní
hladiny M_K≤n, nikoli na heuristickou volbu jedné cesty.

## P1015: všechny rekordní hladiny a uzavřený vzorec penalizace

První číslo s k−1 bitovými změnami má střídavé bity1010…
délky k−1: kratší zápis nemůže mít tolik změn a u této délky
musí být každý přechod změnou. Pro k=1 jde o0. Součet
střídavých mocnin2 dává

    M_k=ceil(2^k/3),
    M_(k+1)=2M_k       pro liché k,
    M_(k+1)=2M_k−1     pro sudé k.

Současně je M_k liché právě při lichém k. Nechť
F(M)=Σ_(h=0)^(M−1)f(h). Z přidání nejnižšího bitu plyne

    f(2h)=f(h)+[h liché],
    f(2h+1)=f(h)+[h sudé],
    F(2M)=2F(M)+M.

Máme P_k=(k−1)M_k−F(M_k). Pro liché k tedy
P_(k+1)=2P_k+M_k. Pro sudé k navíc
f(2M_k−1)=f(M_k−1)=k−1, takže
P_(k+1)=2P_k+M_k−1. Společně

    P_1=0,
    P_(k+1)=2P_k+(2^k−(−1)^k)/3,
    P_k=((3k−2)2^(k−1)+(−1)^k)/9.                    (6)

Poslední uzavřený výraz splňuje uvedený základ i rekurenci
přímým odečtením2P_k; je tedy prokázán pro všechna k≥1.
To dokazuje přesný celý koeficient1/9 i střídavý člen v odpovědi.

## P1016: přesná obecná konstrukce a spojitelnost obou podproblémů

Z P1014–1015 je největší počet výměn posledního slučování

    G(n)=max_(k≥1,M_k≤n)(k n−P_k).                    (7)

Podmínka M_k≤n vyjadřuje, že uvedená množina sudých klíčů
má skutečně n prvků. Lze maximalizovat i číselný výraz přes
všechna k, ale při krajních remízách volíme přípustné k.
Opravdu P_k−P_(k−1)≥M_k−1: na starých M_(k−1) hladinách
se penalizace zvýší o1 a na každé nové kromě poslední je
alespoň1. Proto pro n<M_k nový nepřípustný k nezvýší
hodnotu maxima. Například při n=1 či2 může nepřípustná
hodnota jen remizovat; kontext velikosti množiny ji vylučuje.

Kroky vodorovně v dosažitelné cestě P1014 jsou právě hodnoty

    {1,2,…,M,M+2,M+4,…,2n−M}, M=M_k.

Ty tedy tvoří sudou podposloupnost, přesně jako v odpovědi629.
Ostatní klíče tvoří lichou; při lichém N je poslední dodatečná
hodnota2n+1 lichá. Před slučováním jsou obě množiny seřazené.
Jejich původní pořadí však můžeme nezávisle zvolit tak, aby
každé maximalizovalo předchozí rekurzivní třídění. Porovnání
závisejí jen na relativním pořadí, takže přeznačení na tyto
konkrétní množiny počet výměn nemění.

Pro maximum celého algoritmu V(N) proto platí přesně

    V(0)=V(1)=0,
    V(N)=V(⌈N/2⌉)+V(⌊N/2⌋)+G(⌊N/2⌋), N≥2.          (8)

Horní mez vzniká omezením každé ze tří částí; právě popsaná
konstrukce dosahuje všech tří současně. Tím je zaručeno,
že lokální maximalizace nepoškozuje dřívější podproblémy.

## P1017: maximum61 a celý konkrétní svědek odpovědi11

Pro n=1,2,4,8 jsou přípustné hodnoty k n−P_k postupně

    n=1: 1;
    n=2: 2,3;
    n=4: 4,7,9;
    n=8: 8,15,21,23.

Další k mají M_k>n a horní mez nemohou zlepšit. Proto
G(1)=1,G(2)=3,G(4)=9,G(8)=23. Z(8) je
V(2)=1,V(4)=5,V(8)=19,V(16)=61. Jde o horní mez pro
**všechny** vstupy, nikoli pouze spočítaný počet jednoho běhu.

Uvedená permutace je

    16,10,13,5,14,6,9,2,15,8,11,3,12,4,7,1.

Její sudé hodnoty jsou{1,2,3,4,5,6,8,10}, tedy optimální
M=6 pro n=8. Relativní pořadí obou polovičních posloupností
je totožně w_8=(8,5,6,2,7,3,4,1). U w_8 jsou sudé hodnoty
{1,2,3,5}, optimální M=3 pro n=4, a obě poloviční relativní
permutace jsou w_4=(4,2,3,1). Ta má sudou množinu{1,2},
optimální M=2 pro n=2, a oba páry v pořadí(2,1).
Každé rekurzivní slučování tak dosahuje příslušného G,
což dokazuje všech61 výměn bez rozepisování nebo simulace61 kroků.

## P1018: přesné asymptotické maximum jednoho slučování

Pro k≥2 dává(6) například

    k2^k/12 ≤ P_k ≤ k2^k/5.

Polož L=lg n a q=L−lg L. Pro velké n je k=⌊q⌋ přípustné,
k2^k≤n a P_k=O(n). Tedy G(n)≥nq−O(n).
Naopak pro k≤q je k n−P_k≤nq. Pro k>q, d=k−q>0,
máme q≥L/2 pro L≥4 a tedy

    (k n−P_k)/n ≤ q+d−2^d/24 ≤ q+O(1).

Funkce d−2^d/24 má konečné absolutní maximum. Tyto dvě
meze dokazují s konstantami nezávislými na n

    G(n)=n lg n−n lg lg n+O(n).                        (9)

Konečně mnoho malých n se absorbuje do konstanty. Není
potřeba předpokládat n mocninou2 ani přesnou reálnou polohu
diskrétního maximalizátoru.

## P1019: celý poměr maxima k porovnáním, pro všechna N

P1005 a P1008 dávají μ(s)=y(s−1)=(s/2)lg s+O(s).
Z(9), včetně zaokrouhlení a všech s≥4, plyne

    G(⌊s/2⌋)=(s/2)(lg s−lg lg s)+O(s).                (10)

V rekurzivním stromu podle parity mají na úrovni ell všechny
velikosti hodnotu⌊N/2^ell⌋ nebo⌈N/2^ell⌉ a jejich součet
je N. Pro ell≤⌊lg N⌋−2 jsou alespoň4. Jejich lg se liší
od L−ell, L=lg N, o jednotně omezené množství, a stejně
se liší lg lg s od lg(L−ell). Proto součet μ na této
úrovni je(N/2)(L−ell)+O(N); součet G je
(N/2)(L−ell−lg(L−ell))+O(N). Poslední nejvýše dvě úrovně
mají dohromady O(N) příspěvek.

Konečné aritmetické sumy a integrální meze pro rostoucí log
dávají

    Σ_ell(L−ell)=L²/2+O(L),
    Σ_ell lg(L−ell)=L lg L+O(L).

Sečtením O(L) úrovní tedy

    c(N)=N L²/4+O(NL),
    V(N)=N L²/4−(N/2)L lg L+O(NL),
    V(N)/c(N)=1−2 lg lg N/lg N+O(1/log N).

To je přesně asymptotický výrok odpovědi11, se stejnou
konstantou2 a platností pro všechny délky. Zaokrouhlení
polovin ani blízkost mocnin2 se neztratily v neuniformní chybě.

## Rozsah

Celá11 včetně obecné odpovědi a asymptotiky je uzavřena.
P1012 navíc dokazuje přesné hranové váhy používané odpovědí16;
její průměrné součty, analytická konstanta a periodická odchylka
se tím ještě neuzavírají. Nový nález nevznikl.
