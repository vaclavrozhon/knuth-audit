# Bubble: všechny konečné momenty, úlohy4/7/8 a přesný asymptotický rozsah

2026-11-07. P0946–0956. Originály109,134,628 zobrazeny;
relevantních pět vrstev přebírá `sources/exchanging-errata-review.json`.
Žádný nový nález ani matematický běh. Plný již doložený rozvoj
P(n) ze svazku1 se přebírá se stejnou normalizací; neověřená
historická atribuce není náhradou důkazu. **P0955 zůstává partial**
pro ostřejší Cave v(12), jehož samostatný analytický blok128–130
dosud není zpracován. Konečný součet i vedoucí čas níže jsou dokázány.

## P0946: přesná střední hodnota A, rovnice(7)

P0945 dává F_k=Pr(A≤k)=k^(n−k)k!/n!, 1≤k≤n, a F_0=0
pro n≥1. Z identity pro kladnou celočíselnou A≤n plyne

    E A=Σ_(k=0)^(n−1)(1−F_k)=n+1−Σ_(k=0)^n F_k=n+1−P(n).

Definice P je přesně stejná jako v§1.2.11.3. Nikde se nepočítá
s nezávislostí průchodů. Pro n=1 je P(1)=1 a A=1.
Převzatý úplný důkaz je v
`workstreams/vol1/notes/asymptotic-sums.md`, oddíl Rovnice(24),
a jeho cílené doplnění v
`workstreams/vol1/notes/quality-recovery-section-1.2.11.3-2026-11-06.md`,
oddíly(20)–(26). Pro c=√(π/2) skutečně dává

    P(n)=c√n−2/3+(11c/24)n^(−1/2)+4/(135n)+O(n^(−3/2)). (A)

Tam jsou doloženy i silnější zbytek, nulový k=0 člen,
Eulerovy krajní členy a uniformní Stirlingovo okno. Zde pouze
aplikujeme tento uzavřený výsledek. Ihned
E A=n−c√n+5/3+O(n^(−1/2)), tedy celé průměrové tvrzení(10).

Friend1956 p150 ani Demuth64–68 nebyly obsahově ověřeny.
`workstreams/vol1/notes/demuth-gould-root-status.md` již doložil
Demuthův titul, instituci a říjen1956 z originální ukázky,
ale právě64–68 v ní nejsou. Tento omezený bibliografický výsledek
se přebírá přesně, bez nové předstírané četby těchto stran.

## P0947–0948: celá úloha7, druhý moment, rozptyl a odmocnina

Protože A²=Σ_(k=0)^(A−1)(2k+1), platí

    E A²=n²−Σ_(k=0)^(n−1)(2k+1)F_k.

Položme S=Σ_(k=0)^n kF_k. Z definice P(n+1), vyčleněním
jejího koncového členu k=n+1, vyjde přesně

    P(n+1)=1+S/(n+1).

Tedy Σ_(k<n)F_k=P(n)−1 a Σ_(k<n)kF_k=S−n, takže
E A²=(n+1)²−2S−P(n). Odečtením[n+1−P(n)]² získáme

    Var A=2(n+1)(1+P(n)−P(n+1))−P(n)−P(n)².          (B)

To je celý výraz pod odmocninou v odpovědi7. Nezápornost plyne
z odvození jako rozptylu, nikoli z numerického odhadu rozdílu
velkých členů. Pro n=1: P(1)=1,P(2)=3/2 a(B)=0.

Pro asymptotiku je nutné ovládat **rozdíl** P(n+1)−P(n);
samotné P(n)=c√n+O(1) by pro tento účel nestačilo. Převzaté(A)
dává po explicitním oddělení c√n, konstanty a n^(−1/2) členu

    P(n+1)−P(n)=c/(2√n)+O(1/n).

Zbytky O(1/n) na obou sousedních argumentech skutečně dávají
O(1/n); nepředpokládáme jejich neoprávněnou diferencovatelnost.
Po dosazení do(B) dostaneme
Var A=(2−c²)n+O(√n). Koeficient2−π/2 je kladný, protožeπ<4.
Rozdíl odmocnin lze racionalizovat, a proto

    sd A=√((2−π/2)n)+O(1).

Jsou pokryty jak přesný vzorec, tak požadovaný asymptotický
řád chyby; nejde pouze o výpočet dominantní konstanty.

## P0949: celá událost t=1 v úloze4

Při t=1 následuje prázdná smyčka s BOUND=1, takže lze skončit
už v B4. Pro n≥2 nastane tato situace právě tehdy, když

    b_1>max(b_2,…,b_n).

Důkaz použije přesnou hranici P0943. Po r-tém neprázdném
průchodu je BOUND=max{b_i+i:b_i≥r}−r. Rovnost1 vyžaduje
pro každý aktivní i nerovnost b_i+i≤r+1. Protože b_i≥r
a i≥1, jediná možnost je i=1,b_1=r a všechny ostatní b_i<r.
Obráceně při ostrém maximu b_1=m≥1 je po m-tém průchodu
hranice právě1. Je to jediný možný výskyt, protože BOUND
po každém neprázdném průchodu klesá. Pro n=1 je pravděpodobnost0;
prázdná maxima se zde bez konvence nepoužívají.

Pro b_1=k, 1≤k≤n−1, mají ostatní souřadnice omezení b_i<k.
Počet možností je

    ∏_(i=2)^n min(k,n−i+1)=k^(n−k−1)k!.

Součet přes k a dělení n! dává přesně vytištěnou pravděpodobnost

    Q_n=Σ_(k=1)^(n−1) F_k/k.                         (C)

Pro n=1 je součet prázdný a správně0. Žádná nezávislost po
průchodech se nevyužívá, pouze původní rovnoměrná inversion table.

## P0950: asymptotika úlohy4 s kontrolou ocasu

Potřebujeme Q_n=P(n)/n+O(1/n), nikoli pouze heuristické k≈n.
Při k=n−m, 0≤m≤n−1, je

    F_(n−m)=∏_(i=0)^(m−1) (n−m)/(n−i)
           ≤exp(−m(m+1)/(2n)).                       (D)

Použili jsme1−x≤e^(−x) a(m−i)/(n−i)≥(m−i)/n.
Pro k>n/2 je1/k−1/n≤2m/n². Součet
Σ_(m≥1)m e^(−m²/(2n)) je O(n): na intervalu[m−1,m]
je(x+1)e^(−x²/(2n))≥m e^(−m²/(2n)), a jeho integrál
na[0,∞) je n+√(πn/2). Blízká část součtu rozdílů je tedy
O(1/n). Pro k≤n/2 dává(D) F_k≤e^(−n/8); součet n takových
členů s1/k≤1 je rovněž O(1/n). Nakonec je v P(n)/n
navíc člen F_n/n=1/n. Všechny tři odhady dávají požadované
Q_n=P(n)/n+O(1/n). Dosazením(A) plyne

    Q_n=√(π/(2n))+O(1/n),

tedy celý závěr odpovědi4. Slovo negligible označuje tuto
limitní pravděpodobnost, nikoli malou chybu pro každé malé n.

## P0951: všechna rovnice(8)/úlohy8, i nulové průchody

Pro 1≤j≤n definujme c_j=0, pokud už algoritmus skončil.
Jinak P0943 dává c_j=max{b_i+i:b_i≥j−1}−j. Vždy
0≤c_j≤n−j, protože každá předchozí neprázdná smyčka
snížila BOUND alespoň o1. Událost c_j≤k pro k≥0 je
ekvivalentní současným podmínkám

    b_i<j−1 nebo b_i+i−j≤k, pro všechna i.            (E)

Při již ukončeném běhu jsou všechny b_i<j−1 a podmínka
je správně automatická. Jinak je to přímo podmínka na maximum.

Pro j≥2 a0≤k≤n−j jsou počty voleb b_i∈{0,…,n−i}:

| Index i | Počet | Důvod |
|---|---:|---|
|1≤i≤k+1|j+k−i+1|druhý interval v(E) obsahuje první a nepřekračuje n−i|
|k+2≤i≤n−j+2|j−1|první interval0,…,j−2 obsahuje druhý a je přípustný|
|i>n−j+2|n−i+1|celá původní souřadnice už leží v prvním intervalu|

Součin je

    [(j+k)!/(j−1)!] (j−1)^(n−j−k+1) (j−2)!
      =(j+k)!(j−1)^(n−j−k)=f_j(k).

Prázdný poslední interval pro j=2 má součin0!=1.
Hraniční k=n−j dává f_j(k)=n!, jak musí úplná CDF.
Při j=1 se neprovádí neplatná manipulace s(−1)!: první
průchod má vždy c_1=n−1. Přímo(E) s i=n vynutí k≥n−1,
takže f_1(k)=0 pro k<n−1 a f_1(n−1)=n!. Vytištěné(8)
to vyjadřuje s obvyklým0^0=1. Tak je pokryt i n=1,j=1,k=0.

## P0952: obě konečné sumy pro Cave a správné krajní členy

Pro d=n−j a f_j(−1)=0 je pravděpodobnost c_j=k rovna
(f_j(k)−f_j(k−1))/n!. Sčítáním po částech dostaneme

    E c_j=d−Σ_(k=0)^(d−1)f_j(k)/n!
         =d+1−Σ_(k=0)^d f_j(k)/n!,

neboť f_j(d)=n!. Platí to i pro d=0. Sečtení přes1≤j≤n
dá první tvar(9), s konstantou Σ(n−j+1)=binom(n+1,2).
Substituce r=j−1,s=j+k je bijekce mezi
{1≤j≤n,0≤k≤n−j} a{0≤r<s≤n}; dosazení do f dává

    E C=binom(n+1,2)−W_n,
    W_n=(1/n!) Σ_(0≤r<s≤n) s! r^(n−s).               (F)

Zvlášť je potřeba člen r=0,s=n: má hodnotu n!·0^0=n!,
nikoli0. Pro n=1 je to jediný člen a(F) správně vrací C=0.
Přidání hypotetických nulových průchodů po ukončení nezměnilo C.

## P0953–0954: všechny extrémy a vedoucí průměrný MIX čas

Pro A platí1≤A≤n; identita má1, reverzní permutace b_1=n−1
dává n. Pro B se přebírá úplný P0088/P0089: minimum0,
průměr n(n−1)/4 a maximum n(n−1)/2. První průchod B vždy
provede n−1 porovnání, takže C≥n−1. Každý další aktivní
BOUND klesne alespoň o1, a proto C≤(n−1)+(n−2)+…+1.
Identita dolní mez realizuje; při reverzní permutaci je
po r průchodech BOUND=n−r, takže horní mez je dosažena.
Extrémy A,B,C jsou tedy **současně** dosažitelné; součet mezí
pro cenu nepoužívá neexistující společný vstup.

Dosazením do8A+7B+8C+1 vyjdou přesně min8n+1 a
max(15/2)n²+n/2+1. Pro n=1 oba dávají9, shodně s programem.

Vedoucí průměrný čas lze dokázat bez ještě otevřené jemné
asymptotiky W. Pro s≥1 a k=n−s≥0 dává monotonie x^k

    Σ_(r=0)^(s−1)r^k ≤ ∫_0^s x^k dx=s^(k+1)/(k+1),

s konvencí x^0=1 i v levém krajním členu. Tedy s-tý příspěvek
W_n je≤F_s·s/(n−s+1)≤n/(n−s+1). Koncový s=n sám dává n,
takže n≤W_n≤nH_n. Proto

    E C=n²/2+O(n log n),
    E T=8E A+7E B+8E C+1=(23/4)n²+O(n log n).

Je tím plně doloženo5.75n² i uvedený řád chyby v čase na109,
aniž by se předstíral důkaz koeficientu lineárního členu Cave.

## P0955 partial: přesně oddělený dosud nedoložený člen

Ve(12) zbývá jednotlivě doložit

    E C=1/2[n²−n ln n−(γ+ln2−1)n]+O(√n).

Konečné(F), oba extrémy a vedoucí čas už jsou checked výše.
Ostřejší výsledek kniha odvozuje až přes W na128–130 a úlohu44;
jeho zmínka109 ani existence dané odpovědi není samostatným
důkazem. Položka je do úplného rozvoje včetně zbytků **partial**,
bez nové chyby či domněnky o neplatnosti výsledku.

## P0956: přesný rozsah srovnání se straight insertion

P0687–0691 již doložily pro vytištěný Program S jeho12 instrukcí,
průměr(9/4)n²+(31/4)n−3H_n−6 a oba extrémy; tento důkaz
se přebírá. Bubble program má16 instrukcí, samomodifikaci
a dodatečný vnější průchod. V modelu **průměru rovnoměrné
permutace pro velká n** je poměr časů

    (23/4)/(9/4)=23/9>2.

Právě v tomto kontextu předchozí průměrové analýzy je doloženo
slovní srovnání109. Není to univerzální poměr pro každý vstup:
na identitě jsou časy8n+1 a10n−9 a na konkrétním obrázku
960u proti514u. Tyto případy nevydáváme za protipříklad k právě
uvedenému asymptotickému průměru. Moderní hardware se sem
automaticky nepřenáší; jeho poznámka v erratech2021 patří
do navazujících refinements110.
