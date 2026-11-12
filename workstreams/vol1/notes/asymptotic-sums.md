# §1.2.11.3: diskrétní součty, úlohy 14–18 a rozvoje P,S

V celé poznámce n→∞ přes kladná celá čísla a α je pevná reálná konstanta.
Původní zadání úlohy 14 nemá na s. 506 samostatnou odpověď: její části
(a)–(e) samy tvoří návod. Níže kontrolujeme všechny kroky i zbytky.

## Úloha 14(a)–(c): soustředění součtu u maxima

Označme `U_α(n)=∑_{k=0}^n k^(n+α)exp(−k)`; pro velké n je n+α>0,
takže člen k=0 je 0. Záměna k↦n−k dává

```text
U_α(n)=n^(n+α)exp(−n) sum_{k=0}^n exp(−k²/(2n)) f(k,n),
f(k,n)=(1−k/n)^α exp(−k³/(3n²)−k⁴/(4n³)−…).            (S1)
```

V bodě k=n je součin interpretován spojitým prodloužením původního
výrazu `(1−k/n)^(n+α) exp(k+k²/(2n))`, tedy jako 0. Pro α<0
se nevyhodnocují zvlášť nekonečný faktor a nulová exponenciála.

Pro důkaz (b) položme s=k/n, t=k³/n². Potom
`f(k,n)=F(s,t)=(1−s)^α exp(−t ψ(s))`, kde
`ψ(s)=∑_{j≥0}s^j/(j+3)` je analytická pro |s|<1.
Člen s^(j−i)t^i Taylorova polynomu F má tvar
`k^(2i+j)n^(−i−j)` a 0≤i≤j. Truncace celkového stupně j≤m dává
přesně koeficienty c_ij v knize. Pro 0<ε<1/6 a k≤n^(1/2+ε) jsou
s=O(n^(−1/2+ε)), t=O(n^(−1/2+3ε)), takže analytický zbytek je
`O(n^((m+1)(−1/2+3ε)))`, rovnoměrně v tomto rozsahu k.

Pro větší ε je požadovaný odhad slabší a platí triviálně v původním
rozsahu 0≤k≤n: každý z konečně mnoha monomů je omezen
O(n^(j(−1/2+3ε))), zatímco f je rovnoměrně omezená. Poslední fakt je
pro α≥0 zřejmý. Je-li α=−A<0, píšeme s=k/n a L=−ln(1−s):
`ln f=A L−n(L−s−s²/2)`.
Pro s≤1/2 je to ≤2As−ns³/3, což je shora omezené nezávisle na n.
Pro s≥1/2 platí L−s−s²/2≥L/72: když L≤3, použijeme s³/3≥1/24;
když L≥3, použijeme s+s²/2≤3/2. Pro n≥72A je pak ln f≤0.
Vyjádření mimo původní rozsah k≤n se nepoužívá.

Při sečtení chyby z (b) lze využít
`∑_{k≥0} exp(−k²/(2n))=O(sqrt n)` (porovnání s integrálem), a získat
`O(n^(−m/2+3(m+1)ε))`. Pro dané δ>0 volíme ε<δ/[3(m+1)].
Ocas původního součtu za n^(1/2+ε) je díky omezenosti f nejvýše
Cn exp(−n^(2ε)/2), tedy menší než každá záporná mocnina n.
Totéž platí pro ocasy všech konečně mnoha gaussovských monomů po
prodloužení jejich součtů do ∞. To dokazuje (c) s přesným zbytkem
O(n^(−m/2+δ)), bez předpokladu platnosti lokální řady pro všechna k.

## Úloha 14(d)–(e): Eulerův vzorec a koeficienty

Gaussovský moment je integrál monomu proti exp(−t²/2):
`∫_0^∞ t^d exp(−t²/2)dt=2^((d−1)/2)Γ((d+1)/2)`, d>−1.
Položme h=n^(−1/2) a z=k/sqrt n. Lokální integrand (S1) má tvar

`exp(−z²/2) exp(∑_{j≥1} h^j E_j(z))`,
`E_j(z)=−αz^j/j−z^(j+2)/(j+2)`.

Definujme polynomy A_j(z) koeficienty druhé exponenciály. Jsou určeny
rekurencí `A_0=1`, `A_j=(1/j)∑_{r=1}^j r E_r A_(j−r)`.
Eulerův součtový vzorec se sítí h pro každý polynom krát Gaussovu funkci
pak dává

```text
sum_{k≥0} exp(−(kh)²/2) A_j(kh)
 = h^(−1) integral_0^infty exp(−z²/2)A_j(z)dz + A_j(0)/2
   −sum_{r≥1} B_(2r)/(2r)! · h^(2r−1)
       · [d^(2r−1)/dz^(2r−1)(exp(−z²/2)A_j(z))]_(z=0).
```

Každá konečná truncace má zbytek požadovaného řádu, protože integrály
absolutních hodnot všech derivací polynomu krát Gaussovu funkci jsou konečné.
Zde jsou B_(2r) Bernoulliho čísla z předchozí ověřené sekce.
Použití (c) s libovolně velkým m dovoluje určit libovolný konečný počet
členů. První tři jsou přesně

`U_α(n)/(n^(n+α)exp(−n)) = sqrt(πn/2)−1/6−α`
` +(1/12+α/2+α²/2)sqrt(π/(2n))+O(n^(−1))`.              (S2)

V úloze (d) stojí obecně pevné t≥0, nejen celé t. Pro necelé t nelze
bez doplnění použít vysoké derivace x^t v nule. Eulerův postup se opraví
odečtením dostatečně mnoha členů
`∑_{j<M}(−1)^j x^(t+2j)/(j!(2n)^j)` v okolí 0 s hladkým ořezem;
zbytek pak má potřebný počet nulových derivací v 0. Na jednotlivé
odečtené mocniny se Eulerův vzorec použije od 1, kde jsou hladké.
Jejich konstantní členy jsou ζ(−t−2j), definované Eulerovým pokračováním:
pro q≥0 a 2r>q+1 je ζ(−q) limitou

`∑_{k=1}^N k^q−N^(q+1)/(q+1)−N^q/2`
`−∑_{l=1}^r B_(2l) q_under(2l−1) N^(q−2l+1)/(2l)!`.

Zápis q_under(j) znamená q(q−1)…(q−j+1). Eulerův zbytek této
limity je O(N^(q−2r+1)); dovoluje v předchozím odečítání zvolit r
libovolně velké. Po zrušení závislosti na ořezu dostaneme obecně

```text
sum_{k≥0} k^t exp(−k²/(2n))
 ~ (2n)^((t+1)/2)Γ((t+1)/2)/2 + [t=0]
   + sum_{j≥0} (−1)^j ζ(−t−2j)/(j!(2n)^j).
```

Hranatá závorka [t=0] je 1 při t=0 a 0 jinak; používáme 0^0=1.
Při každé konečné truncaci lze zbytek odhadnout další mocninou 1/n
výše uvedeným odečtením s větším M,r. Pro celočíselná t=2i+j skutečně
použitá v (c) není toto doplnění nutné: platí přímo hladký Eulerův vzorec.
Úloha tedy není vyvrácena nehladkostí necelých mocnin v nule.

## Rovnice (24): P(n)

Funkce P(n) je `∑_{k=0}^n k^(n−k)k!/n!` pro n≥1.
Stirlingův rozvoj k! je rovnoměrný v pásu k=n+O(n^(1/2+ε));
mimo něj jsou součty exponenciálně menší, jak plyne z maxima funkce
k^n exp(−k) a jejích ocasů. Lze tedy po vynásobení zachovat libovolný
počet jeho členů. Označme levou stranu (S2) V_α(n). Potom

`P(n)=exp(−1/(12n)+O(n^(−3)))`
` · [V_(1/2)(n)+V_(−1/2)(n)/(12n)+V_(−3/2)(n)/(288n²)+O(n^(−5/2))]`.

Pro zobrazené členy se V_α vypočítá výše uvedenou rekurencí do h³
(k tomu jsou potřeba A_0,…,A_4). Vlastní zbytek O(n^(−2)) lze
ospravedlnit použitím (c) s m=5 a libovolným 0<δ<1/2, potom zahrnout
další vypočtený člen do zbytku. Vyjde přesně

`P(n)=sqrt(πn/2)−2/3+(11/24)sqrt(π/(2n))+4/(135n)`
`     −(71/1152)sqrt(π/(2n³))+O(n^(−2))`.                (S3)

Také jednodušší Eulerův postup v hlavním textu (20)–(23) dává první
dva členy: z (G2) pro x=n+1/2,y=−1/2, Stirlingova poměru a koncového
členu (22) získáme sqrt(πn/2)−2/3+O(n^(−1/2)). Hlavní text správně
netvrdí, že jeho hrubý zbytek sám dokazuje všechny členy (S3).
Číslo (11/24)sqrt(π/2) leží mezi 0.5744 a 0.5745 (ověřitelné
umocněním s již ověřeným intervalem π); numerická poznámka na s. 120
odpovídá tomuto koeficientu, nikoli Eulerově konstantě.

## Úloha 17: čtvrtý součet S(n)

Definice je
`S(n)=∑_{k≥0}(n+k−1)!/[(n−1)!(n+k)^k]`.
Konverguje, protože Stirlingova formule omezuje členy konstantou krát
polynomem v k násobeným exp(−k). Přímé rozdělení součtu v indexu n dává

`S(n+1)+P(n)=T(n)=∑_{k≥0} k^(n−k)k!/n!`.               (S4)

Pro celý součet T lze použít tentýž diskrétní výpočet kolem k=n.
V lokální proměnné z=(n−k)/sqrt n nyní integrujeme přes celou reálnou
osu. Vzdálené ocasy jsou zanedbatelné: pro k/n v pevném intervalu
kolem 1 je exponent n(ln(k/n)−k/n+1) omezen zápornou konstantou
krát (k−n)²/n; mimo tento interval klesá exponenciálně. Polynom A_j
má paritu j, takže integrály lichých A_j jsou nulové, sudé jsou
dvojnásobkem půlkových momentů. Eulerovy koncové příspěvky v k=n
se při spojení obou polovin zruší, protože tento člen počítáme jen jednou.

Tedy pro T použijeme ve výpočtu (S3) místo V_α pouze dvojnásobek
integrálních příspěvků A_0,A_2,A_4,… . Z (S4) dostaneme S(n+1);
posun n↦n−1 pak dává odpověď

`S(n)=sqrt(πn/2)+2/3−(1/24)sqrt(π/(2n))−4/(135n)`
`     +(49/1152)sqrt(π/(2n³))+O(n^(−2))`.

Zbytek se odůvodní stejným lokálním rozvojem s větším m jako u P.
Známá oprava 27.3.1998 mění pouze zápis indexu sumy na k≥0.

## Úlohy 15,16,18: přesné identity

Úloha 15: binomický rozvoj integrandu a
`∫_0^∞ z^k exp(−z)dz=k!` dávají
`∫_0^∞ (1+z/n)^n exp(−z)dz=∑_{k=0}^n n_under(k)/n^k=1+Q(n)`.

Úloha 16: po rozepsání Q(k)=∑_{j=1}^k k_under(j)/k^j zaměníme dva
konečné součty. Pro pevné j je vnitřní součet

`(−1)^j n_under(j) ∑_{l=0}^{n−j}(−1)^l binom(n−j,l)(l+j)^(n−j−1)`.

Je-li j<n, jde o (n−j)-tou konečnou diferenci polynomu nižšího stupně,
tedy o nulu. Pro j=n zbývá `(−1)^n n!/n=(−1)^n(n−1)!`, jak se žádá.
Člen k=0 v původním zkráceném zápisu je chápán jako prázdný součet,
tedy 0; funkce Q je jinak definována pro k≥1. Výpočet netvrdí hodnotu
výrazu 0^(−1) odděleně od tohoto prázdného součtu.

Pro úlohu 18 zaveďme polynom
`H_n(x,y)=∑_{k=0}^n binom(n,k)(x+k)^k(y+n−k)^(n−k)`.
Rozklad `(x+k)^k=x(x+k)^(k−1)+k(x+k)^(k−1)` a již ověřená Abelova
identita dávají pro n>0
`H_n(x,y)=(x+y+n)^n+n H_(n−1)(x+1,y)`, H_0=1.
Při této rekurzi se x+y+n nemění; proto

`H_n(x,y)=∑_{k=0}^n binom(n,k)k!(x+y+n)^(n−k)`.

V místech zdánlivých záporných mocnin při odvození Abelovou identitou
se používá polynomiální prodloužení, takže výsledná identita platí pro
všechna reálná i komplexní x,y. Pro x=y=0 je odpověď n^n(1+Q(n));
pro x=1,y=0 je odpověď (n+1)^n Q(n+1). Zde n≥1; případ n=0 se
vyhodnotí přímo jako 1. Připsání Cauchymu je samostatná kontrola zdroje.
