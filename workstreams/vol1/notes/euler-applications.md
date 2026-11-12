# §1.2.11.2: harmonická čísla, Stirlingův vzorec a úlohy 5–6

Audit 1. listopadu 2026. Vycházíme z obecně dokázané formule
(E6) v [euler-summation.md](euler-summation.md). B_j znamenají
současná Bernoulliho čísla, s B_1=1/2; P_j jsou nezměněné
Bernoulliho polynomy. R_m(a,b) je tamní integrální zbytek,
nikoli chybový člen už po přechodu k nekonečnému intervalu.

## Harmonická čísla, (14)–(16)

Označme H_n=sum_{k=1}^n 1/k. Pro f(x)=1/x máme
f^(k−1)(x)=(−1)^(k−1)(k−1)!/x^k, takže pro m>=1

```text
H_n = ln n+1+sum_{k=1}^m B_k(−1)^(k−1)(n^(−k)−1)/k + R_m(1,n),
R_m(1,n) = −integral_1^n P_m({x})x^(−m−1)dx.             (A1)
```

Polynom P_m je omezený na [0,1], proto poslední integrál
konverguje absolutně i pro n→infinity. Tím dostáváme existenci
gamma=lim(H_n−ln n) a přesně současné (14)–(15).
Odečtením limitní rovnosti vyjde

```text
H_n = ln n+gamma+sum_{k=1}^m (−1)^(k−1)B_k/(k n^k)
                  + integral_n^infinity P_m({x})x^(−m−1)dx. (A2)
```

Integrál je O(n^(−m)); sloučením s posledním členem a použitím
řádu m+1 dostáváme (16) s chybou O(n^(−m−1)). To zahrnuje
všechna celá m>=1. V první konvenci nahradíme H_n výrazem
H_(n−1) a B_1 číslem b_1=−1/2; ostatní členy se nemění.

Ostrá chyba po sudém indexu plyne z (E10)–(E11), aplikovaných
na interval [n,N] a pak N→infinity. Znaménko ani ostrost se
neztratí: příslušné nenulové integrály kladného periodického
jádra proti derivaci pevného znaménka zůstávají nenulové
už na prvním celém intervalu [n,n+1]. Speciálně

```text
H_n = ln n+gamma+1/(2n)−1/(12n²)+1/(120n⁴)−epsilon,
0<epsilon<1/(252n⁶), n>=1.                              (A3)
```

Tento výsledek souhlasí s nezávislým integrálním důkazem
v [harmonic-analytic.md](harmonic-analytic.md), (A3)–(A6).
Fourierova formule (E7) dává
`B_(2j)=(−1)^(j+1)2(2j)! zeta(2j)/(2pi)^(2j)` a zeta(2j)→1.
Tím jsou ověřeny růst Bernoulliho čísel i divergence nekonečného
rozvoje (16) pro každé pevné kladné n: členy nejdou k nule.

## Logaritmus faktoriálu, (17)–(19)

Pro f(x)=ln x je pro k>=2 derivace řádu k−1 rovna
(−1)^k(k−2)!/x^(k−1). Eulerova formule dává opravenou (17):

```text
ln(n!) = n ln n−n+1+(ln n)/2
       + sum_{k=2}^m B_k(−1)^k (n^(1−k)−1)/(k(k−1)) + R_m(1,n),
R_m(1,n) = (1/m) integral_1^n P_m({x})x^(−m)dx.          (A4)
```

Pro m>=2 integrál absolutně konverguje na [1,infinity).
Tedy existuje konstanta
`sigma=lim(ln(n!)−(n+1/2)ln n+n)`, a odečtením limity
získáme přesně

```text
ln(n!) = (n+1/2)ln n−n+sigma
       + sum_{k=2}^m B_k(−1)^k/(k(k−1)n^(k−1))
       − (1/m) integral_n^infinity P_m({x})x^(−m)dx.      (A5)
```

Zbytek posledního integrálu je O(n^(1−m)). Použitím řádu m+1
a sloučením jeho posledního členu dostaneme (18) s chybou
O(n^(−m)); zvlášť pro m=5 je logaritmická korekce
`1/(12n)−1/(360n³)+O(n^(−5))`. Exponenciála tohoto výrazu je

```text
1+1/(12n)+1/(288n²)−139/(51840n³)−571/(2488320n⁴)+O(n^(−5)). (A6)
```

Koeficienty vznikají z konečného Taylorova rozvoje exponenciály;
zbytek je zachován díky exp(O(n^(−5)))=1+O(n^(−5)). Výraz (A6)
je přesně násobná závorka v (19).

## Úloha 5: určení konstanty Wallisovým součinem

Položme kappa=exp(sigma)>0. Z již získaného odhadu
`n!=kappa sqrt(n)(n/e)^n(1+O(1/n))` vyplývá

```text
kappa = sqrt(2) lim_{n→infinity} 4^n(n!)²/(sqrt(n)(2n)!). (A7)
```

Jeho druhá mocnina je limitou
`(2/n) product_{j=1}^n j²/(j−1/2)²`.
Tento součin se rovná `(2/n)(2n+1)W_n`, kde
`W_n=product_{j=1}^n (2j)²/((2j−1)(2j+1))` je Wallisův
součin. Již dokázáno W_n→pi/2 v
[gamma-functions.md](gamma-functions.md), části „Stirlingův odhad“.
Proto kappa²=2pi a kladnost dává kappa=sqrt(2pi), tedy
sigma=(ln(2pi))/2. Není potřeba znovu numericky odhadovat limitu.

## Úloha 6: kladný reálný argument gama funkce

Fixujme c>0 a aplikujme (E6) na f(x)=ln(c+x), a=0,b=N,
s m>=2. Definice Eulerovy konečné aproximace je

```text
Gamma_N(c) = N^c N! / product_{j=0}^N(c+j),
Gamma_N(c) → Gamma(c).                                  (A8)
```

Ta byla dokázána v [gamma-functions.md](gamma-functions.md).
Po odečtení Eulerova součtu od c ln N+ln(N!) a přechodu
N→infinity dostáváme

```text
ln Gamma(c) = (c−1/2)ln c−c+sigma
 + sum_{k=2}^m B_k/(k(k−1)c^(k−1))
 − (1/m) integral_0^infinity P_m({x})(x+c)^(−m)dx.        (A9)
```

V součtu lze psát také (−1)^k B_k, protože liché B_k pro k>1
jsou nulové. Limitní hlavní člen využívá
`(N+c+1/2)ln(1+c/N)→c`; členy se zápornými mocninami
N jdou k nule. Absolutní konvergence integrálu opravňuje limitu.
To ověřuje i podrobnou odpověď s Gamma_N po změně z roku 2021.

Pro m=2 je absolutní hodnota integrálu v (A9) nejvýše
`|B_2|/(2c)=1/(12c)`. Korekce B_2/(2c) je stejného řádu.
Proto po použití Gamma(c+1)=c Gamma(c) a exponenciály

```text
Gamma(c+1)=sqrt(2pi c)(c/e)^c (1+O(1/c)),  c→+infinity.  (A10)
```

Tento odhad je pro všechny dost velké reálné c s jednou
konstantou; nejde jen o limitu po posloupnosti se stejnou
zlomkovou částí. To je přesný současný obor zadání po opravě
ze září 2024. Na pevném [a,infinity), a>0, lze konstantu
rozšířit i na počáteční kompaktní interval spojitostí.
