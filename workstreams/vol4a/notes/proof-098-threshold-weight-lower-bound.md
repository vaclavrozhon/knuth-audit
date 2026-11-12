# Úloha 112(c): obecná dolní mez každé váhy a uzavření P1056

7. listopadu 2026, X0124. Navazuje přesně na proof-097; originály
p94/file111 a p555–556/file572–573 zobrazeny. Žádný matematický
program ani externí neprokázaná matematická věta. Níže je celý krok
od vhodných testů k růstu vah rozepsán, nikoli převzat jako intuice
„váhy začnou rychle růst“.

Používáme znaménkové souřadnice z_i=2x_i−1 a χ_S(z)=∏_(i∈S)z_i.
Booleovská tabulka f odpovídá h=2f−1∈{−1,1}. Proof-097 dokázal,
že F(f) je znaménko posledního nenulového Fourierova koeficientu
h v Chaseově pořadí. Kladný výstup vynucuje striktně kladné skalární
součty s libovolnými reprezentujícími vahami. Všechny transformované
váhy w_S jsou kladná celá čísla.

## Dva obecné testy pro sousední podpory

Nechť α,β jsou sousední podpory v pořadí, β pozdější, |β|=k.
Chaseův důkaz dává právě dva typy, bez ohledu na vzdálenost měněných
bitů: přidání prvku nebo záměnu jednoho prvku.

**Přidání:** α=A, β=A∪{a}, |A|=k−1. Vyberme libovolný v na β
s v_a=1. Definujme h_v na těchto k souřadnicích jako −χ_α kromě
jediného bodu v, kde je +χ_α; ostatní souřadnice ignorujeme.
Normalizovaný Fourierův koeficient β je 2^(1−k)>0. Koeficient α
je −1+2^(1−k); všechny další koeficienty mají podporu v β a stupeň
<k. Vedoucí koeficient je tedy kladný a F((1+h_v)/2)=1 pro každé v.

Zprůměrujme tyto platné testy přes všechna v s v_a=1. Pro pevné z
je pravděpodobnost změněného bodu 2^(1−k), pokud z_a=1, jinak 0.
Proto bodově

    E_v h_v(z) = −χ_α(z)+2^(2−k)χ_α(z)[z_a=1]
               = −(1−2^(1−k))χ_α(z)+2^(1−k)χ_β(z).

Průměr konečně mnoha striktně kladných reprezentujících součtů je
striktně kladný. Ortogonalita proto přímo vynucuje

    w_β > (2^(k−1)−1) w_α.                         (A)

**Záměna:** α=A∪{a}, β=A∪{b}, |A|=k−1. Vyberme v na A∪{a,b}
s v_a=v_b a v' vzniklé současným obrácením a,b. Funkce h_v je
−χ_α kromě těchto dvou bodů, kde je +χ_α. Fourierova změna může
být nenulová pouze na podporách obsažených v A∪{a,b}, které obsahují
právě jeden z a,b: příspěvky obou bodů se jinak vyruší. Jediné dvě
takové podpory stupně k jsou α,β. Jejich koeficienty jsou opět
−1+2^(1−k), respektive 2^(1−k), protože v_a v_b=1. Ostatní mají
stupeň <k. Opět je každé F((1+h_v)/2)=1.

Pro pevné z s z_a=z_b jsou při rovnoměrném výběru v dvě možnosti,
v=z nebo v'=z, z celkem 2^k. Při z_a≠z_b žádná. Tedy

    E_v h_v(z) = −χ_α(z)+2^(2−k)χ_α(z)[z_a=z_b]
               = −(1−2^(1−k))χ_α(z)+2^(1−k)χ_β(z),

protože χ_α z_a z_b=χ_β. Stejné zprůměrování dává (A).
Argument zahrnuje i k=1, kde faktor v (A) je 0 a závěr je prostě
kladnost w_β. Nejde o provedení enumerace testů: jejich průměr byl
vyčíslen obecně po jednom pevném vstupu. Žádný předpoklad o velikosti
ostatních vah ani skrytá indukční hypotéza zde není.

## Všechny vytištěné jednotlivé testy na p556

Při přidání dává nezprůměrovaný test přesně

    w_β > (2^(k−1)−1)w_α
          − Σ_(S⊊β, S≠α) χ_α(v)χ_S(v)w_S.         (B)

Při záměně stejný vzorec používá místo všech proper subsets jen
S⊆A∪{a,b}, které obsahují právě jeden z a,b, kromě α,β. Z ostatních
souřadnic vzniká všude stejný faktor, který se vykrátí.

První vytištěná funkce je skutečně

    x2 XOR … XOR xm XOR (x1 ¬x2 … ¬xm),

včetně všech negací. Zde α={2,…,m}, β=[m], v=(+1,−1,…,−1).
Po případném obrácení celého znaménka h je to test (B); self-dualita
zaručuje stejnou výslednou nerovnost. Pro každý S=β\{j}, j≥2,
je χ_α(v)χ_S(v)=−1. Dostáváme přesně kladný součet všech těchto
vah stupně m−1, násobek (2^(m−1)−1)w_α a zbývající členy
stupně ≤m−2. Při m=2 jsou poslední z nich +w_∅ a výsledkem je

    w_11 > w_01+w_10+w_00.

Druhá funkce obsahuje negace také:

    x1 XOR … XOR x_(m−1)
      XOR (¬x1 … ¬x_(m−2) (x_(m−1) XOR ¬xm)).

Zde A={1,…,m−2}, a=m−1, b=m. Oprava parity právě obrátí dva
body se z_A=(−1,…,−1) a z_a=z_b. Jde tedy o druhý obecný test.
Každá podpora stupně m−2 obsahující právě jeden z a,b má v (B)
kladný příspěvek: její součin charakterů s α je −1. To jsou přesně
obě skupiny vytištěného součtu, každá s m−2 členy; ostatní mají
stupeň ≤m−3. Pro m=3 žádné další nenulové členy nezbývají a máme

    w_101 > w_110+w_010+w_001.

Tím jsou zkontrolovány také dva explicitní příklady a oba popisy
„smaller terms“, nejen obecný závěr. Zprůměrování výše pak dává
všem sousedním podporám přesně vytištěnou růstovou nerovnost (A).

## Od poslední transformované váhy ke všem původním vahám

Pro libovolnou dvojici {a,b} lze první dvoubitový test použít s
ostatními proměnnými ignorovanými; dostáváme

    w_{a,b}>w_a+w_b+w_∅.                            (C)

Pro m≥2 z toho plyne, že každá váha stupně ≤1 je menší než největší
váha stupně 2. Podle (A) váhy celé vrstvy 2 striktně rostou, takže
její poslední váha B je zároveň největší. Váhy stupně ≥3 při každém
dalším kroku rostou faktorem alespoň 3.

Položme q=1+m+C(m,2) a h=n−q, tedy počet podpor stupně ≥3. Pro
m≥4 je h≥5. Je-li W=w_[m] poslední váha a W' bezprostřední
předchůdce, součet všech dřívějších vah stupně ≥3 je menší než
(3/2)W' geometrickou řadou. Každá z q nižších vah je nejvýše B,
a po h−1 růstových krocích B<W'/3^(h−1). Navíc

    q/3^(h−1)<1/2 pro všechna m≥4.

V základu je 11/81<1/2. Při zvýšení m se q zvětší o m+1 a je
menší než 3q, zatímco h se zvýší o 2^m−m−1≥1; indukce nerovnost
zachová. Tedy součet všech vah kromě W splňuje

    Σ_(S≠[m]) w_S < 2W'
                   < 2W/(2^(m−1)−1) ≤ 5W/n       (m≥4).

Fourierova inverze nyní pro KAŽDÝ původní index a dává

    |v_a| = W/n + O(W/n²),
    |v_a| ≥ (W/n)(1−5/n).

Horní i dolní odhad plyne z trojúhelníkové nerovnosti po oddělení
jediného členu χ_[m](a)W; velikost jeho znaménka je 1. Tím je
doloženo tvrzení o všech vahách, nikoli pouze existence jedné velké.
Konstanta je uniformní v reprezentaci, protože všechny předchozí
nerovnosti byly uniformní.

Od B≥1 aplikujeme (A) pro každou podporu stupně 3 až m. Dostáváme

    W > P_m := ∏_(k=3)^m (2^(k−1)−1)^C(m,k).

Každá z C(m,k) podpor má svůj přechod, také první ve vrstvě;
není vynechán žádný faktor na spojích. Pro všechna m≥4 tedy máme
explicitní dolní mez

    |v_a| > (P_m/n)(1−5/n).

To přímo implikuje vytištěnou mez (P_m/n)(1−O(n^−1)). Malé m
se do asymptotického tvrzení „when m is large“ nevnucují.

## Přesný asymptotický exponent

Zapíšeme logaritmus produktu se základem 2 jako

    log2 P_m = Σ_(k≥3) C(m,k)(k−1)
                + Σ_(k≥3) C(m,k)log2(1−2^(1−k)).

Binomické identity dávají první součet mn/2−n+1−C(m,2). Pro
u≤1/4 platí |ln(1−u)+u|≤u²/(2(1−u))≤(2/3)u²; plyne to
sečtením mocninné řady od druhého členu. Součet těchto zbytků je
O(Σ_k C(m,k)4^(1−k))=O((5/4)^m). Lineární člen je přesně

    Σ_(k≥3) C(m,k)2^(1−k)
       =2(3/2)^m−2−m−C(m,2)/2.

Všechny zbývající polynomy v m, také dělení n (log2 n=m), jsou
O((5/4)^m). Faktor 1−5/n má logaritmus O(1/n). Výsledný exponent
je proto přesně

    mn/2 − n − 2(3/2)^m/ln 2 + O((5/4)^m).

Jde o asymptotickou podobu doložené dolní meze, nikoli o tvrzení,
že každá reprezentace má právě takové váhy nebo že jsou optimální.

## P1056: přesný smysl srovnání s úlohou 96

Horní mez pro n vstupů, již úplně doložená v proof-083, je
U_n=(n+1)^((n+1)/2)/2^n. Její logaritmus je

    log2 U_n = (n/2)log2 n − n + O(log n).

Právě dokázaná rodina pro n=2^m vyžaduje u všech celočíselných vah

    log2 |v_a| ≥ (n/2)log2 n − n − O(n^log2(3/2)).

Mají tedy stejný hlavní exponent, dokonce i lineární člen −n;
ztráta je sublineární. Netvrdíme poměr vah jdoucí k 1. Nekonečná
posloupnost n=2^m stačí pro „sometimes“ v poslední větě odpovědi 96.
Tím je P1056 skutečně uzavřena, nikoli odvozena z horní meze samotné.

Také poznámka u (b), že obecně nelze konstrukci výrazně zkrátit,
má tento přesný asymptotický smysl. Pro smíšený radix z proof-097
je každá výsledná váha v absolutní hodnotě nejvýše Σ_j M_j<2M_(n−1)
(radixy od j=1 jsou alespoň 3). Logaritmus této meze je nejvýše
mn/2+O((3/2)^m), protože log2(1+2^−k)≤2^−k/ln 2 a binomický
součet je (3/2)^m. Horní konstrukce a nutná dolní mez mají stejný
vedoucí člen mn/2; netvrdí se optimálnost konkrétního radixu.

## Bibliografie, errata a přesná mapa celých stránek

Relevantní vrstvy a tři zapracované opravy jsou uvedeny v proof-097.
Žádný nový rozpor ani kandidát. Primární autorův archiv a SIAM
záznam potvrzují Håstadův článek v SIAM J. Discrete Math. 7 (1994),
484–492, DOI 10.1137/S0895480192235878. Uložený PDF z autorova webu
je třináctistránková autorská verze, nikoli devítistránková sazba
časopisu. Její testovací konstrukce byly porovnány; argument výše
její dlouhou indukci nepotřebuje a všechny meze dokazuje výslovně.

[Primární vydavatelský záznam Alon–Vũ](https://www.sciencedirect.com/science/article/pii/S0097316597927801)
potvrzuje JCTA 79 (1997), p133–160, DOI 10.1006/jcta.1997.2780,
a rozšíření Håstadovy konstrukce. Širší výsledky tohoto článku ani
historickou prioritu zde znovu neauditujeme; žádný z nich není vstupem
našeho důkazu. Metadata jsou v sources/threshold-lower-bibliography.json.

Celá p555/file572: pokračování 111(b), všech sedm seznamů a 111(c)
jsou úplně v proof-096; 112(a),(b), všechny konkrétní mediány a
celý začátek 112(c) v proof-097. Bibliografické meze zůstávají oddělené.
Stránka proto nyní může mít review_depth argument.

Celá p552/file569: horní dodatek 96 je proof-083 a právě uzavřená
P1056; 97–100 jsou celé proof-085; všechna tři zadání/obě Y kresby
101 jsou proof-086; celé 102 a 103 včetně neintegrálních optim jsou
proof-087. Staré důkazy se nepřepočítávají. Také tato stránka má
nyní úplné argumentové pokrytí, se zachovanými bibliografickými skipy.

P94/file111 zůstává partial kvůli 113–116; p556/file573 kvůli
odpovědím 113–116. Odkazované p365–366 se nepovyšují: doložena je
jen přesně potřebná rekurence a její vlastnosti. Hlavní kurzor textu
zůstává na symetrických funkcích p77/file94, čtecí kurzor p218/file235.
