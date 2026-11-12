# §1.2.6-63: dvojitý binomický součet

Audit 1. listopadu 2026; zobrazeny s. 74 a 491. Odpověď
odkazuje na dvě úlohy *Concrete Mathematics*. Následuje
přímý důkaz, který na těchto odkazech nezávisí.

Značíme `C(r,j)=r(r−1)...(r−j+1)/j!` pro celé j>=0
a 0 pro j<0. Pro mocninnou řadu F(t) značí [t^a]F
koeficient t^a; u Laurentovy řady smí být a záporné.
Předpoklady jsou celá l,m,n, n>=0, a libovolná r,s.

Označme zadaný součet H(l,m). Jeho nenulové členy mají
0<=k<=n a 0<=j<=m; pro m<0 je tedy součet 0.
Pro m>=0 vytvoříme formální generující funkci
`F_l(y)=sum_{m>=0} H(l,m)y^m`. Slovo „formální“ znamená,
že pracujeme po koeficientech, bez tvrzení o konvergenci.
V každém koeficientu y^m se vyskytuje jen konečně mnoho j,k.

Sečtení posledního binomického koeficientu přes m dává
`sum_m C(s+n−j−k,m−j)y^m=y^j(1+y)^(s+n−j−k)`.
Použijeme také `C(j+k,k+l)=[t^(k+l)](1+t)^(j+k)`.
Proto po konečném sečtení přes k a koeficientovém sečtení
přes j dostáváme

```text
F_l(y)
 = (1+y)^(s+n) [t^l]
      (1−y(1+t)/(1+y))^r
      sum_{k=0}^n C(n,k)(−(1+t)/(t(1+y)))^k
 = (1+y)^(s+n−r) [t^l]
      (1−yt)^r ((yt−1)/(t(1+y)))^n
 = (−1)^n (1+y)^(s−r) [t^(n+l)](1−yt)^(n+r).
```

Koeficient poslední řady je 0 pro n+l<0. Jinak je
`(−y)^(n+l)C(n+r,n+l)`. Koeficient y^m proto je

```text
H(l,m) = (−1)^l C(n+r,n+l) C(s−r,m−n−l),
```

což je přesně tvrzená pravá strana. Pro m<0 je také nulová:
buď n+l<0 a vynuluje se první koeficient, nebo n+l>=0
a vynuluje se druhý. Důkaz tedy zahrnuje celý otištěný
celočíselný obor l,m, nikoli jen nezáporné hodnoty.
