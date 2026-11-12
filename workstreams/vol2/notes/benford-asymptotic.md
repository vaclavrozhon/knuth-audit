# §4.2.4-20: přesná první chyba opakovaného průměrování

Vlastní řešení, 2.11.2026. Zadání str.264 je vizuálně přečteno; v odpovědích
619–623 ani ve čtyřech erratech není řešení20. Níže je obecná asymptotická
formule pro každé pevné m a r. Nezaměňuje m→∞ z Theorem F s limitem
velikosti argumentu x→∞.

## Definice a výsledek

Předpokládejme `1<r<10`; krajní r=1,10 jsou popsány na konci.
P0(k) je indikátor, že significand celého k je menší než r.
Pro m>=1 definujme

```
Pm(x) = (1/x) sum_{1<=k<=x} P(m-1)(k),       x>=1.
```

Na celých argumentech je to přesně(9); reálné rozšíření odpovídá výpočtu(8).
Funkce Sm(s) je limit z Lemma Q, pro `1<=s<=10`, a je periodická
po změně proměnné na logaritmus. Označme

```
L = ln10,                 alpha = log_10 r,
c = (r-1)/9,              mu = alpha-c > 0,
delta_j = ceil(r*10^j)-r*10^j,       j=0,1,...,
D_j = sum_{0<=h<j} delta_h,
T = ln x,                 u_+ = max(u,0).
```

Kladnost mu plyne z přísné konkávnosti logaritmu: jeho graf je mezi1
a10 nad příslušnou tětivou. Vždy `0<=delta_j<1`. Tyto rozdíly popisují,
o kolik se délka intervalu vedoucích číslic liší od počtu celých bodů.

Pro pevné m>=2 položme

```
G_m(T) = 1/(m-1)! * ( mu*T^(m-1)
       + sum_{j>=0} delta_j * (
           (1-alpha)*(T-jL)_+^(m-1)
         + alpha*(T-(j+1)L)_+^(m-1) ) ).                    (1)
```

Součet je pro každé T konečný. Pro `x=10^n s`, `1<=s<=10`, platí
stejnoměrně v s

```
Pm(x)-Sm(s) = ( G_m(ln x) + O((ln x)^(m-2)) ) / x.        (2)
```

Konstanta v O může záviset na pevných m,r. Protože
`G_m(T)>=mu*T^(m-1)/(m-1)!`, je(2) skutečná asymptotická ekvivalence:
podíl levé strany a `G_m(ln x)/x` jde stejnoměrně k1. Poskytuje i
obecný odhad `O((ln x)^m/x)`, tedy `O(n^m/10^n)` na dekádových
podposloupnostech, ale rozlišuje případy s menší hlavní chybou.

## Přesný výchozí počet pro m=1

Pišme celé `k=10^j t`, kde `1<=t<10`, a
`d_m(x)=x(Pm(x)-Sm(significand(x)))`. Výpočet počtu v úplných
dekádách a v posledním intervalu dává přesně

```
d_1(k) = D_j-c+delta_j + (1-delta_j)*P0(k).                (3)
```

Například pro r=2 je `d_1(k)=8/9`, pokud P0(k)=1, a `-1/9` jinak.
Při reálném x=10^j t jsou odpovídající přesné větve

```
d_1(x) = D_j-c+1-{x},       pokud 1<=t<r,
       = D_j-c+delta_j,      pokud r<=t<10.                (4)
```

Složené závorky značí zlomkovou část. Pro t=10 použijeme j+1,t=1.
To je plné řešení případu m=1; nemusí mít hladký hlavní člen, protože
obsahuje skutečné celočíselné skoky. Rovnice(3) zároveň pokrývá všechny
celočíselné argumenty a žádný hraniční bod nezapočítává dvakrát.

## Omezená chyba kvadratury pro spojité Sm

Nechť `h_q(x)=Sq(significand(x))`, x>0, q>=1. Tato funkce je omezená
mezi0 a1, spojitá a po dekádách má tvar polynomu v ln x děleného x
plus konstantu. Na každé hladké části

```
|h_q'(x)| <= C_q/x,     |h_q''(x)| <= C_q/x^2.
```

Případné skoky první derivace jsou jen v geometrických řadách bodů
10^j a r10^j; jejich velikosti jsou `O(10^-j)`. První derivace tedy
má konečnou celkovou variaci na[1,∞). Zde celková variace znamená
součet absolutních změn, včetně skoků, nikoli změnu znaménkovou.

Na každém jednotkovém intervalu lze chybu lichoběžníkové kvadratury
odhadnout konstantou krát variace první derivace na tom intervalu.
Po sečtení je celková chyba omezená. Rozdíl lichoběžníkového součtu
od součtu koncových hodnot je rovněž omezený, protože h_q je omezená.
Neúplný poslední interval a integrál od0 do1 přispějí nejvýše konstantou.
Proto

```
E_m(x) = sum_{k<=x} h_(m-1)(k) - integral_0^x h_(m-1)(t)dt
       = O(1),                                         m>=2. (5)
```

Tento krok je podstatný: hrubý odhad pouze přes `|h'|` by dal O(ln x)
a ztratil by první člen pro konečné desetinné rozvoje.

Z integrální rekurence Lemma Q plyne
`integral_0^x h_(m-1)(t)dt=x h_m(x)`. Odečtení od diskrétního
průměru proto dává přesnou rekurenci

```
d_m(x) = sum_{k<=x} d_(m-1)(k)/k + E_m(x),       m>=2.    (6)
```

## Základ m=2

Na úplné dekádě `10^j<=k<10^(j+1)` platí

```
sum 1/k = L+O(10^-j),
sum P0(k)/k = alpha*L+O(10^-j).
```

Druhá rovnost je integrální srovnání přesného prefixového intervalu;
její odhad je platný i při celé hranici r10^j. Podle(3) tedy

```
sum d_1(k)/k = a_j*L+O((j+1)10^-j),
a_j = D_j+(1-alpha)delta_j+mu.                           (7)
```

Chyby úplných dekád jsou absolutně sčitatelné. V neúplné dekádě
s horním significandem s dostaneme místo a_j ln s ještě člen

```
(1-delta_j)*(ln(min(r,s))-alpha*ln s),
```

který je stejnoměrně omezený. Z(5)–(7) tak plyne

```
d_2(x) = integral_0^(ln x) a_floor(u/L) du + O(1).        (8)
```

Funkce pod integrálem se dá napsat jako

```
a_floor(u/L) = mu + sum_{j>=0} delta_j * (
                 (1-alpha)*[u>=jL] + alpha*[u>=(j+1)L]).
```

Integrace dává přesně G_2 z(1), čímž je základ dokázán.

## Indukce pro m>=3

Z definice(1) máme `G_m(0)=0` a `G_m'(T)=G_(m-1)(T)` pro m>=3.
Navíc G_m i jeho po částech definované derivace rostou nejvýše
polynomiálně v T, protože delta_j jsou omezené a je jich O(T).
Integrální srovnání tedy dává

```
sum_{k<=x} G_(m-1)(ln k)/k
    = integral_1^x G_(m-1)(ln t) dt/t + O(1)
    = G_m(ln x)+O(1).                                   (9)
```

Odůvodnění omezené chyby v první rovnosti: variace funkce
`G_(m-1)(ln t)/t` je konečná na[1,∞), neboť její derivace je omezena
polynomem v ln t děleným t^2. Pro G_2 jsou pouze skoky derivace,
samotná funkce zůstává spojitá.

Indukční zbytek `O((ln k)^(m-3))` po dělení k a sečtení přispěje
`O((ln x)^(m-2))`. Rovnice(5),(6),(9) dokončují důkaz(2).
Všechny odhady byly pro libovolné x→∞, proto jsou stejnoměrné v s.

## Dva důležité zvláštní případy

**Konečný desetinný rozvoj.** Pokud r10^J je celé, pak delta_j=0
pro j>=J. Položme `mu_r=mu+sum_{j<J}delta_j`. Z(1) plyne

```
Pm(x)-Sm(s) = mu_r*(ln x)^(m-1)/((m-1)! x)
              + O((ln x)^(m-2)/x),             m>=2.    (10)
```

Pro celočíselné r je `mu_r=log_10 r-(r-1)/9`; například pro r=2
je to `log_10 2-1/9`. Hodnota je kladná, takže chyba je nakonec kladná.

**Existující kladný průměr rozdílů.** Jestliže
`(delta_0+...+delta_(n-1))/n -> d>0`, součtová per partes, případně
Riemannovy součty s Cesàrovou konvergencí, dávají

```
G_m(T) ~ d*T^m/(L*m!),
Pm(10^n s)-Sm(s) ~ d*L^(m-1)*n^m/(m!*10^n*s).            (11)
```

Pro r=4/3 je každý delta_j=2/3, takže tento případ je explicitní.
Pro r s rovnoměrně rozdělenými posuny desetinných číslic je d=1/2;
žádný takový předpoklad však není potřebný pro obecnou formuli(1)–(2).
Pro libovolné iracionální r nelze bez důkazu nahradit delta_j průměrem1/2.

**Kraje.** Pro r=1 je Pm=Sm=0. Pro r=10 jsou celočíselná Pm rovna1;
na reálných x při zde zvoleném rozšíření Pm(x)=floor(x)/x a Sm=1.
Tedy chyba je přesně `-{x}/x` pro m>=1. Na celých x je nulová.
Odhad(2) s G_m=0 je stále platný, ale asymptotická ekvivalence s
nulovým hlavním členem se samozřejmě netvrdí.

## Konkrétní mez pro m=2 a numerické ověření

Pro m=2 lze vzít například `|d_2(x)-G_2(ln x)|<20`, x>=1.
Z explicitního S1: na dekádě [B,10B] je součet hladkých variací h1′
nejvýše `(1+10/36)/B`, skok v rB nejvýše1/B a skok v10B nejvýše1/(10B).
Po sečtení dekád je celková variace menší než3. Lichoběžníková chyba
je nejvýše osmina této variace; konce, integrál(0,1) a poslední neúplný
interval dávají dohromady méně než4 pro E2.

Chyba harmonického součtu úplné dekády vůči L je nejvýše1/B;
prefixového součtu vůči ln r nejvýše2/B. V(7) tak zbude nanejvýš
`(j+4)10^-j`. Jejich součet je menší než4.57. V poslední neúplné
dekádě oba harmonické odhady mají chybu nejvýše2/B, tedy příspěvek
nejvýše `(2j+6)10^-j<=6`; oscilující člen v(8) má absolutní hodnotu
nejvýše L<2.31. Součet těchto hrubých mezí je menší než20.

[Ověřovač](../verify_benford_asymptotic.py),
[výstup](../results/benford-asymptotic.json): pět r (2,6/5,4/3,
314159/100000,999/100), každé s přímými poli až do10^6 a šesti
průměrováními. Celkem260 přesných racionálních porovnání(3) a počtů,
75 porovnání(1) s nezávislou integrací po dekádách a650 naměřených
asymptotických zbytků. Všech pět checkpointů prošlo, včetně meze20
pro m=2. Výstup uvádí konzervativní mez zaokrouhlení části s binárními
součty/průměry; funkce Sm a G jsou počítány s65 desetinnými místy.
Toto není úplná intervalová certifikace transcendentních výpočtů.

Při r=2,m=2,N=10^6 je d_2 přibližně2.73218 a G_2 přibližně2.62383.
Při m=6 může poměr d_m/G_m v takto malém N být ještě2.29; netvrdíme,
že vedoucí člen je už pro všechna m malou relativní chybou. Obecná
asymptotická ekvivalence je dokázána výše, nikoli vyvozena z těchto dat.
