# Runs: jednotlivé argumenty hlavního textu35–44

Režim: vlastní argument ke každému níže uvedenému tvrzení. Sazba je
v `images/multisets-file-046.png` a `images/runs-file-047.png`
až `runs-file-055.png`; známé opravy
v `sources/runs-errata-review.json`. Není to nový nález. Označení
`A(n,k)` znamená Eulerovo číslo, `S(n,k)` Stirlingovo číslo druhého druhu.

## Počty a generující funkce,35–39

1. Sestup odděluje právě dvě sousední maximální rostoucí části: neprázdné
   slovo má počet běhů roven počtu sestupů plus1. V příkladu357168942
   jsou hranice po7,9,4, tedy čtyři běhy. Záměna hodnot `a→n+1−a`
   převádí sestupy na vzestupy a dokazuje všechny uvedené symetrie.
2. Vložením maxima do permutace délky n−1 vznikne n různých permutací;
   smazání maxima je inverze. Při k sestupech je k+1 míst na konci běhu,
   kde se počet nezmění, a n−1−k ostatních. Proto
   `A(n,k)=(k+1)A(n−1,k)+(n−k)A(n−1,k−1)`.
   Ze šesti vložení do31245 mají361245 a312456 jeden sestup, ostatní dva.
3. `A(0,0)=1`, ostatní nultý řádek0; pro n>0 je nosič0≤k<n,
   součet n!, oba kraje1 a `A(n,k)=A(n,n−1−k)`.
   Tabulka1 byla ručně dosazena do rekurence; řádky jsou
   `[1];[1];[1,1];[1,4,1];[1,11,11,1];[1,26,66,26,1];
   [1,57,302,302,57,1];[1,120,1191,2416,1191,120,1];
   [1,247,4293,15619,15619,4293,247,1];
   [1,502,14608,88234,156190,88234,14608,502,1]`.
   Například1191=3·302+5·57,2416=4·302+4·302,
   15619=4·2416+5·1191,88234=4·15619+6·4293.
4. Stabilní třídění slova nad1..m určí jedinou permutaci indexů.
   Při r bězích indexů musí být hodnoty přísně rostoucí na r−1 sestupech,
   jinde mohou být stejné. Přičtení počtu předchozích nepřísných hran
   mění podmínky na výběr n různých čísel z1..m+n−r. Zpětné odečtení
   je inverze. Po součtu a symetrii dostáváme
   `m^n=Σ_k A(n,k) choose(m+k,n)`.
   Pro indexy357168942 jsou přírůstky0,1,2,2,3,4,5,5,5,
   tedy tištěných `choose(m+5,9)` možností.
5. Rovnost polynomů platná pro všechna kladná celá m platí pro reálné x.
   Pro n=3 dává koeficienty1,4,1. Dosazení x=1,2 dává kraje a
   `A(n,1)=2^n−n−1`; soustava x=1,..,n je trojúhelníková s diagonálou1,
   proto čísla určuje jednoznačně.
6. Ekvivalentní GF je
   `(1−z)^(n+1) Σ_{t≥1} t^n z^t = Σ_k A(n,k) z^(k+1)`.
   Rozvinutí levé strany a výběr koeficientu dokazuje Eulerův vzorec13:
   `A(n,k)=Σ_{j=0}^k (−1)^j choose(n+1,j)(k+1−j)^n`.
7. Pro n≥1 má `g_n(z)=Σ_k A(n,k−1)z^k/n!` pravděpodobnostní
   koeficienty. Symetrie dává `g_n(z)=z^(n+1)g_n(1/z)` a střední
   hodnotu(n+1)/2. Formální `g_0(z)=z` se používá pouze v superGF;
   pravděpodobnostní a druhé symetrické identity zde mají n≥1.
8. Rozklad `t^n=Σ_j S(n,j)(t)_j` a
   `Σ_{t≥0}(t)_j z^t=j!z^j/(1−z)^(j+1)` dávají
   `g_n=Σ_j S(n,j)j!z^j(1−z)^(n−j)/n!`.
   Symetrií vznikne druhý tvar18,
   `g_n=z Σ_j S(n,j)j!(z−1)^(n−j)/n!`.
   Koeficient u(z−1)^(n−k) je
   `k!S(n,k)+(k+1)!S(n,k+1)=k!S(n+1,k+1)`, což dokazuje oba tvary16
   a derivace15: `g_n^(m)(1)=S(n+1,n+1−m)/choose(n,m)` pro0≤m≤n.
9. Pro n≥2 jsou indikátory sousedních sestupů Bernoulli(1/2);
   nesousední jsou nezávislé, sousední mají společnou pravděpodobnost1/6.
   Tedy rozptyl `(n−1)/4+2(n−2)(1/6−1/4)=(n+1)/12`.
   S derivacemi to souhlasí, neboť
   `S(n+1,n−1)=choose(n+1,3)+3choose(n+1,4)` a
   `g_n''(1)=(n+1)(3n−2)/12`.
10. Označené neprázdné bloky dávají
    `Σ_n S(n,k)t^n/n!=(e^t−1)^k/k!`. Dosazení do18 a součet geometrické
    řady dokazuje20:
    `g(z,x)=Σ_n g_n(z)x^n/z=(1−z)/(e^((z−1)x)−z)`.
    V bodě z=1 jde o odstranitelnou singularitu s hodnotou1/(1−x).

## Délky běhů,39–41

11. Při společném počítání všech běhů všech permutací je průměrná délka
    `n n!/(n!(n+1)/2)=2n/(n+1)→2`. Také n/R_n→2 v pravděpodobnosti,
    protože výše dokázaný rozptyl dává R_n/n→1/2.
12. První m hodnot tvoří rostoucí posloupnost právě v jednom z m!
    relativních pořadí. Proto ocas první délky je q_m=1/m!, hmotnosti
    jsou q_m−q_(m+1) pro m<n a1/n! pro m=n, a střední hodnota je
    `Σ_{m=1}^n1/m!=e−1−δ_n`. Zbytek
    `δ_n=1/(n+1)!·(1+1/(n+2)+...)≤(e−1)/(n+1)!`;
    součiny j dalších jmenovatelů jsou alespoň(j+1)!.
    Nekonečný model realizují nezávislé spojité rovnoměrné hodnoty,
    jejichž všechna konečná relativní pořadí jsou rovnoměrná.
13. Pro celkovou délku S_k prvních k běhů platí
    `Pr(S_k≥m)=Σ_{j=0}^{k−1}A(m,j)/m!`.
    Permutaci s nejvýše k běhy lze určit přiřazením každé hodnoty jednomu
    z k rostoucích seznamů; proto počet je nejvýše k^m. Ocas je tedy
    sčitatelný. Součet ocasů a odečtení E S_(k−1) dávají24,
    `L_k=Σ_{m≥1}A(m,k−1)/m!`.
14. Sčítání nezáporných koeficientů, případně formální výběr koeficientu,
    dává25: `L(z)=Σ_{k≥0}L_kz^k=z(g(z,1)−1)
    =z(1−z)/(e^(z−1)−z)−z`, L_0=0.
15. Eulerův vzorec, Pascalův rozklad choose(m+1,r) a exponenciální
    součet pro choose(m,r) dávají
    `L_k=k Σ_{j=1}^k (−1)^(k−j) j^(k−j−1)e^j/(k−j)!−[k=1]`.
    Jde o monický polynom v e. Pro k=1,2,3 dává e−1,e²−2e,
    e³−3e²+3e/2. Tištěné mezní součty se používají s opravou z18.5.2000;
    nejde o nový nález.
16. Tabulku2 včetně všech18 znamének za poslední číslicí uzavřel jeden
    cílený běh `nice -n15` bez enumerace. Skript
    `scripts/runs_numeric_reference.py` používá racionální interval
    `Σ_{j=0}^{90}1/j! < e < Σ_{j=0}^{90}1/j!+92/(91·91!)`
    a intervalové dosazení polynomu. Výsledek
    `results/runs-numeric-reference.json` obsahuje vnější meze a stav passed.
    Ověřuje i L_1<L_2<L_3 a skutečné oscilace kolem2.
17. Vysvětlení prvních tří začátků lze zpřesnit v rovnoměrném modelu.
    Podmíněná hustota následujícího začátku y při začátku x je
    `K(x,y)=e^(1−x)−[y≥x]e^(y−x)`: sečteme všechny možné rostoucí
    prostřední úseky před prvním poklesem. Její integrál je1.
    Hustoty prvních tří začátků jsou
    `f_1(y)=1`, `f_2(y)=e−e^y`,
    `f_3(y)=e²−e+(y−e)e^y` pro0≤y≤1.
    F_2−F_1=(e−1)y−e^y+1≥0 konvexitou exponenciály.
    Pro F_3−F_2 má derivace hodnotu e²−3e+1>0 v0, hodnotu0 v1,
    a její derivace je `(y−e+2)e^y`: nejprve záporná, pak kladná.
    Proto má první derivace jedinou změnu z+ na− uvnitř intervalu;
    F_3−F_2 je nezáporná, neboť na obou koncích je0.
    Začátky se tedy pro první tři běhy zmenšují i ve stochastickém smyslu.
    Podmíněná střední délka e^(1−x) s x klesá. Žádnou monotonicitu všech
    pozdějších L_k tento argument netvrdí.

## Komplexní kořeny a asymptotiky,41–43

18. Pišme D(z)=e^(z−1)−z. Reálný kořen je pouze1, dvojnásobný;
    vyplývá to z přísné konvexity e^(x−1)−x. Pro y>0 rozklad na
    reálnou a imaginární část dává27, `r=y/sin y`, `x=1+log r=y cot y`.
    Nutně x≥1 a y leží v pásu(2πk,(2k+1/2)π).
19. Rovnice pro y je `F(y)=y cot y−1−log(y/sin y)=0` a
    `y sin²y·F'(y)=−(y−sin y cos y)²−sin⁴y<0`.
    V pásu k=0 limit F(0)=0 vylučuje další kořen; v každém pásu k≥1
    začíná F v+∞ a končí záporně, tedy má právě jeden kořen.
    Ostatní kořeny jsou konjugované. Z x=1+log r plyne x=O(log y),
    r∼y∼2πk a `y_k=2πk+arg z_k`; argument jde kπ/2, tudíž
    `y_(k+1)−y_k→2π`. Poloměry jsou přísně rostoucí, neboť
    `y²=r²−(1+log r)²` má pro r>1 kladnou derivaci.
20. Tentýž jediný cílený běh použil uvedenou monotonicitu a intervalové
    vyhodnocení znamének F na koncích čtyř úzkých intervalů. Výsledek
    doložil všechna tištěná čísla z_1,r_1..r_4,θ_1..θ_4 včetně znamének.
    Obr.3 odpovídá rovnicím27, polohám i konjugaci kořenů; váha osy y=0
    je samostatná známá tisková oprava z1.1.2006.
21. V jednoduchém kořeni z_k je D'=z_k−1, tedy reziduum
    (1−z)/D je−1 a reziduum L je−z_k. Rozvoj u=z−1 dává D=u²/2+O(u³),
    takže reziduum v1 je−2. Po odečtení konečného počtu pólů ve tvaru
    známé opravy je
    `R_m=L+2z/(z−1)+Σ_{j=1}^m[z/(z−z_j)+z/(z−conj(z_j))]`
    analytické pro |z|<r_(m+1). Cauchyho odhad dává koeficienty
    o(M^(−n)) pro každé M<r_(m+1). Pro ostřejší tištěný zbytek
    O(r_(m+1)^(−n)) odečteme ještě pár m+1 a zvolíme
    r_(m+1)<M<r_(m+2). Tím je dokázána29 i L_n→2.
22. Nekonečný rozvoj také plyne přímo ze standardní Hadamardovy
    faktorizace celé funkce řádu nejvýše1. D nemá kořen v0 a
    `D(z)=D(0)e^(az)∏_ρ[(1−z/ρ)e^(z/ρ)]`, kde kořen1 počítáme dvakrát
    a a=D'(0)/D(0)=1−e. Logaritmická derivace je přípustná lokálně
    stejnoměrně mimo kořeny, protože Σ|ρ|^(−2)<∞. Přitom přesně
    `L(z)=−zD'(z)/D(z)`. Pár sdružených reciprokých kořenů je
    `2Re(z_k)/|z_k|²=O(log k/k²)`, takže i součet těchto párů konverguje.
    Odtud R_m→c z lokálně stejnoměrně mimo póly; c je konstanta, jak
    stanoví známá oprava. Pro n>1 výběr koeficientu dává přesnou
    konvergentní řadu `L_n=2+2Σ_{k≥1}r_k^(−n)cos(nθ_k)`.
    Hodnotu c ani nově přidanou úlohu28 zde nepotřebujeme.
23. Rozvoj25 u z=1 dává `L=−2/u−7/3+O(u)`.
    Proto `H=L−2z/(1−z)` je analytická pro |z|<r_1 a H(1)=−1/3.
    Zvolíme 8<R<r_1; koeficienty H jsou O(R^(−k)). Součet jejich
    ocasu dokazuje `E S_k=2k−1/3+O(8^(−k))` bez nekonečného rozvoje22.

## Multisety,42–44

24. Foatova bijekce je převzata z uzavřeného důkazu hlavního textu§5.1.2.
    Spojuje k sestupů slova s k sloupci top>bottom v biwordu. Pro p
    výskytů každé hodnoty1..m se transformace32→33 skládá z komplementu
    každé dolní hodnoty x'=m+1−x a přemístění horních bloků:
    blok1 zůstává1, blok y≥2 jde na m+2−y. Je involucí a zachová multiset.
    Blok1 v obou obrazech nemá sloupec top>bottom. V ostatních blocích
    `x<y ⇔ x'≥m+2−y`, takže z celkem(m−1)p sloupců se přesně
    (m−1)p−k stane sestupnými. Přes Foatu vzniká deklarovaná symetrie
    počtů běhů k+1 a mp−p−k+1.
25. Párování involucí dává průměr `1+p(m−1)/2`. Pro m13,p4 je25.
26. Pro libovolné kladné n=Σn_j jsou dvě určené sousední pozice obě
    rovné j s pravděpodobností `n_j(n_j−1)/(n(n−1))` (n≥2).
    Přeházení dvojice páruje případy< a>, tedy pravděpodobnost sestupu je
    `(n²−Σn_j²)/(2n(n−1))`. Přičtení jednoho koncového běhu a součet
    n−1 indikátorů dává34, `E R=1+n/2−Σn_j²/(2n)`.
    Pro n=1 je stejný konečný vzorec přímo1; prázdný multiset není
    v pasáži o rozdání karet použit. Po vynásobení N jde o tištěný
    celkový počet, stejná četnost splývajících karet se krátí.

Historické atribuce, obsah citovaných článků a hlášené chyby historických
19/42místných implementací nebyly reprodukovány. Matematické hodnoty
tabulky jsou na těchto zprávách nezávisle doloženy. Dosavadní hotové
důkazy§5.1.2 ani předchozí úspěšné výpočty se neopakovaly.
