# §1.2.11.2-7–9: hyperfaktoriál a binomické koeficienty

Audit 1. listopadu 2026, originály s.116 a 504 zobrazeny.
Používáme současná Bernoulliho čísla B_j, B_1=1/2, a polynomy
P_j definované v [euler-summation.md](euler-summation.md).
Symbol O(g(n)) omezuje absolutní velikost zbytku konstantou krát g(n)
pro n→infinity; všechny parametry mimo n jsou pevné.

## Úloha 7: součin a jeho konstanta

Hyperfaktoriál K_n je součin `product_{k=1}^n k^k`; jeho logaritmus
je L_n=sum_{k=1}^n k ln k. Aplikujeme Eulerův vzorec na f(x)=x ln x.
Jeho primitivní funkce je x² ln x/2−x²/4; f'=ln x+1 a pro j>=2
je `f^(j)(x)=(−1)^j(j−2)!/x^(j−1)`.
Pro řád m=2t>=4 je zbytek na [1,infinity) absolutně konvergentní.
Všechny konstantní členy z dolní meze a tohoto integrálu
sloučíme do jediné reálné konstanty ln A. Odtud

```text
L_n = (n²/2+n/2+1/12)ln n−n²/4+ln A
      −sum_{j=2}^t B_(2j)/((2j−2)(2j−1)(2j)n^(2j−2)) + E_t(n).
                                                               (P1)
```

Z (E10)–(E11) na intervalu [n,N] a přechodu N→infinity plyne,
že E_t má znaménko prvního vynechaného členu a

```text
|E_t(n)| < |B_(2t+2)|/((2t)(2t+1)(2t+2)n^(2t)), n>=1.  (P2)
```

Derivace sudých řádů f jsou kladné, takže podmínka znamének je
splněna. Zbytek v (P1) je záporný ocas integrálu R_(2t)(1,n);
proto má právě znaménko −B_(2t+2), jak vyžaduje pokračování řady.
Exponenciála (P1) dokazuje celý knižní výsledek, včetně
O(n^(−2t)) v exponentu a vedoucího členu
`K_n ~ A n^(n²/2+n/2+1/12) exp(−n²/4)`.

Konstanta se identifikuje pomocí funkce zeta. Pro Re(s)>1 je
`zeta(s)=sum_{k>=1} k^(−s)`; v následujícím zápisu jde o její
jednoznačné meromorfní pokračování. Eulerův vzorec pro x^(−s)
dává v okolí s=−1, například se zbytkem řádu 4,

```text
zeta(s)=sum_{k=1}^N k^(−s)+N^(1−s)/(s−1)−N^(−s)/2
       +sum_{j=1}^t B_(2j) s^[2j−1] N^(1−s−2j)/(2j)! + T_t(s,N).
                                                               (P3)
```

Zde s^[r]=s(s+1)...(s+r−1) je rostoucí mocnina. Integrální
zbytek T_t je lokálně stejnoměrně konvergentní pro Re(s)>1−2t;
derivování přidává nejvýše faktor log x do integrabilního ocasu.
Proto lze (P3) v s=−1 derivovat. První dva krajní členy a j=1
pak dávají

```text
zeta'(−1)=lim_{N→infinity}
 [−L_N+(N²/2+N/2+1/12)ln N−N²/4+1/12].                (P4)
```

Vyšší členy i derivace zbytku jdou k nule. Srovnání s (P1)
ukazuje `ln A=1/12−zeta'(−1)`; současně (P3) při s=−1 dává
zeta(−1)=−1/12.

Pro druhé knižní vyjádření použijeme standardní funkcionální rovnici
[DLMF 25.4.2](https://dlmf.nist.gov/25.4#E2):
`zeta(s)=2^s pi^(s−1) sin(pi s/2) Gamma(1−s) zeta(1−s)`.
Logaritmická derivace, psaná jako podíl derivace a funkce,
v s=−1 dává

```text
zeta'(−1)/zeta(−1) = ln(2pi)−1+gamma−zeta'(2)/zeta(2),
A = (2pi exp(gamma−zeta'(2)/zeta(2)))^(1/12).             (P5)
```

Zde gamma je Eulerova konstanta a psi(2)=1−gamma byla odvozena
z Gamma součinu v [gamma-functions.md](gamma-functions.md).
Nevybíráme reálný logaritmus záporné hodnoty zeta(−1).
Funkcionální rovnice je zde výslovně přijatá standardní analytická
věta; její zdroj byl přečten, není nahrazována numerickou shodou.
Numerická kontrola A se opírá přímo o (P1)–(P2), bez knihovního
vyhodnocování zeta nebo její derivace.

## Úloha 8: argument an²+bn a poměr binomických koeficientů

Pro pevné a>0 a reálné b je x=an²+bn nakonec kladné.
Výraz x! pro necelé x znamená Gamma(x+1), jak dovoluje úloha 6.
Použijeme ln(x!)=(x+1/2)ln x−x+sigma+O(1/x),
kde sigma=(ln(2pi))/2. Dosazením
`ln x=2ln n+ln a+ln(1+b/(an))` a Taylorovým rozvojem do
řádu n^(−3) dostáváme

```text
ln((an²+bn)!) = 2an²ln n+a(ln a−1)n²+2bn ln n+bn ln a
 +ln n+b²/(2a)+(ln a)/2+sigma
 +(3a−b²)b/(6a²n)+O(n^(−2)).                            (P6)
```

Člen (ln a)/2 je známá oprava z 1. ledna 2006. Protože
x=Theta(n²), stačí první Stirlingův odhad s chybou O(1/x).
Potištěná odpověď pracuje s tímto kvadratickým režimem a>0.
Pokud a=0,b>0, použije se přímo Stirlingův rozvoj bn;
pokud a=b=0, je log(0!)=0. Záporný vedoucí argument nepatří
kladnému oboru reálného logaritmu faktoriálu v této úloze.

Pro druhou část nechť c>0 a
`Q_n=binom(cn²,n)/(c^n binom(n²,n))`. Členy jsou kladné
pro všechna dost velká n. Kombinace (P6) pro (a,b) rovné
(c,0),(c,−1),(1,0),(1,−1) vede k

```text
ln Q_n = (c−1)/(2c)−(c−1)(2c−1)/(6c²n)+O(n^(−2)),
Q_n = exp((c−1)/(2c))
      (1−(c−1)(2c−1)/(6c²n))(1+O(n^(−2))).              (P7)
```

Nezávisle lze začít přesným součinem z poslední věty odpovědi:
`Q_n=product_{j=1}^{n−1}(1+alpha j/(n²−j))`, alpha=1−1/c.
Jeho logaritmus lze rozvinout jednotně v j, protože každá
porucha je O(1/n). Platí
`sum j/(n²−j)=1/2−1/(6n)+O(n^(−2))` a
`sum (j/(n²−j))²=1/(3n)+O(n^(−2))`;
součet třetích mocnin je O(n^(−2)). Tedy
ln Q_n=alpha/2−(alpha+alpha²)/(6n)+O(n^(−2)), přesně (P7).
Závorky ve jmenovateli jsou podstatné, jak opravují errata 2012.

## Úloha 9: střední binomický koeficient

Stirlingův logaritmický rozvoj dává
`ln binom(2n,n)=2n ln2−ln(pi n)/2−1/(8n)+O(n^(−3))`.
Exponenciála tedy dává

```text
binom(2n,n)=4^n/sqrt(pi n) (1−1/(8n)+1/(128n²)+O(n^(−3))). (P8)
```

Druhá metoda používá přesnou identitu
`binom(2n,n)=4^n binom(n−1/2,n)=4^n n^[1/2]/(n sqrt(pi))`
a rozvoj (F3) v
[asymptotic-factorial-powers.md](asymptotic-factorial-powers.md).
Označíme-li zde Stirlingovy diagonální polynomy D_k(r)=c(r,r−k),
jejich první hodnoty jsou D_0(1/2)=1,D_1(1/2)=−1/8,
D_2(1/2)=1/128, přesně (P8). Písmeno D odlišuje tuto rodinu
od Bernoulliho polynomů P_k použitých v Eulerově zbytku.
Další otištěné koeficienty jsou
`5/1024, −21/32768, −399/262144, 869/4194304`.

Všechny jmenovatele jsou mocniny 2 z obecného důvodu:
Stirlingův polynom c(r,r−k) má celočíselné hodnoty pro
r=0,1,2,..., a tudíž celočíselné koeficienty v Newtonově bázi
binom(r,j), získané konečnými diferencemi. Pro j>=1 je
`binom(1/2,j)=(−1)^(j−1)Catalan_(j−1)/2^(2j−1)`.
Číslo Catalan_h=binom(2h,h)/(h+1) je celé (například rozdíl
binom(2h,h)−binom(2h,h−1)). Vyhodnocení konečného Newtonova
součtu v 1/2 je tedy dyadické, tj. má po zkrácení pouze mocninu
2 ve jmenovateli. To dokazuje obecné tvrzení i bez přečtení
citovaného časopiseckého řešení Knuth–Vardi 1990; dostupnost
této konkrétní publikace je evidována zvlášť.
