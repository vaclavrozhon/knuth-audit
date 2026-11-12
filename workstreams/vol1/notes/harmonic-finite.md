# §1.2.7: konečné harmonické součty

Audit 1. listopadu 2026. Zobrazeny s. 75–79 a odpovědi
492–493, včetně aktuálních oprav odpovědí. Pro celé n>=0
definujeme `H_n=sum_{k=1}^n 1/k`, s H_0=0. Obecně
`H_n^(r)=sum_{k=1}^n k^(−r)`; pro komplexní r používáme
kladnou reálnou hodnotu log k. `C(n,k)` je binomický
koeficient, nulový při k<0 nebo k>n pro n>=0.
Všechny součty v této poznámce jsou konečné; analytické
odhady jsou v `harmonic-analytic.md`, dělitelnost
v `harmonic-valuations.md` a úloha 20 v `harmonic-transform.md`.

## Definice a růst, úlohy 1–4

Prázdný součet a první dvě hodnoty dávají
H_0=0,H_1=1,H_2=3/2. Blok 2^m+1,...,2^(m+1)
obsahuje 2^m členů, každý alespoň 2^(−m−1) a nejvýše
2^(−m). Indukce proto dává pro m>=0

```text
1+m/2 <= H_(2^m) <= 1+m.                               (H1)
```

Tím jsou doloženy (2), divergence H_n a úloha 2.
Pro r>1 rozdělíme řadu do bloků 2^j,...,2^(j+1)−1.
Každý blok je nejvýše 2^(j(1−r)). Geometrická řada dává

```text
H_n^(r) < 1/(1−2^(1−r))=2^(r−1)/(2^(r−1)−1).            (H2)
```

Neostrá mez pro konec bloku v odpovědi 3 tedy platí;
pro každé konečné n lze použít ostrou mez celé geometrické
řady. Přesnější integrální odhad ocasu je v analytické poznámce.

Posloupnost `H_n−log n`, n>=1, klesá: její úbytek je
`log(1+1/n)−1/(n+1)>0`, jak plyne integrací 1/t
na [n,n+1]. Je zdola kladná, protože H_n>log(n+1).
Její limitu značíme gamma, Eulerova konstanta. Každý
konečný člen je ostře nad limitou. V úloze 4 tedy
platí (b),(c), zatímco (a) selže již pro n=1.

## Stirlingova čísla a přibližná aditivita, úlohy 6–7

Neznaménková Stirlingova čísla c(n,k) jsou koeficienty
rostoucí mocniny `x(x+1)...(x+n−1)=sum_k c(n,k)x^k`
z předchozí sekce. Koeficient x² v
`x product_{j=1}^n (x+j)` je `n! sum_{j=1}^n 1/j`.
To dokazuje `H_n=c(n+1,2)/n!`, včetně n=0, kdy je
koeficient x² nulový. Ekvivalentně důkaz funguje rekurencí
c(n+1,2)=n c(n,2)+(n−1)!.

Pro kladná celá m,n nechť `T(m,n)=H_m+H_n−H_(mn)`.
Přímé odečtení dává

```text
T(m+1,n)−T(m,n)
 = 1/(m+1)−sum_{j=1}^n 1/(mn+j) <= 0.                  (H3)
```

Každý jmenovatel v součtu je nejvýše n(m+1). Při n>1
je alespoň jedna nerovnost ostrá. Symetrie dává totéž
v druhém argumentu. Maximum je 1, dosažené právě když
m=1 nebo n=1. Minimum neexistuje; infimum, tj. největší
dolní mez, je gamma. Skutečně při m,n→infinity platí
T(m,n)→gamma podle existence limity H_t−log t;
monotonie zaručuje T(m,n)>=gamma. Pro m,n>1 je díky
ostré monotonii T(m,n)>gamma; pro m=1 nebo n=1 je 1>gamma.
Odpověď správně rozlišuje nedosaženou dolní mez od minima.
Její odkaz na zobecnění z roku 1963 je samostatný pramenný bod.

## Sumace po částech a (8)–(9), úlohy 10–11

Pro posloupnosti a_k,b_k platí rozložením rozdílu součinu

```text
(a_(k+1)−a_k)b_k + a_(k+1)(b_(k+1)−b_k)
 = a_(k+1)b_(k+1)−a_k b_k.
```

Sečtení pro 1<=k<n teleskopuje na a_n b_n−a_1 b_1,
což je přesně úloha 10 pro celé n>=1. Toto je sumace
po částech: součet součinu a rozdílu se převede na
okrajové členy a rozdíl druhého činitele. n=1 dává 0=0.

Výměna konečných součtů dává

```text
sum_{k=1}^n H_k = sum_{j=1}^n (n+1−j)/j = (n+1)H_n−n.   (H4)
```

Pro celá m,n>=0 použijeme Pascalovo pravidlo
`C(k,m)=C(k+1,m+1)−C(k,m+1)` a rozdíl
H_(k+1)−H_k=1/(k+1). Dostaneme

```text
sum_{k=1}^n C(k,m)H_k
 = C(n+1,m+1)H_(n+1)−C(1,m+1)
   −(C(n+1,m+1)−C(0,m))/(m+1)
 = C(n+1,m+1)(H_(n+1)−1/(m+1)).                         (H5)
```

V posledním kroku C(1,m+1)=C(0,m)/(m+1)=[m=0].
To ověřuje i opomenutelné okrajové členy pro m=0; n=0
a m>n vycházejí také správně. Knižní analogický integrál
`integral_1^n x^m log x dx` plyne obyčejnou integrací po
částech pro n>0,m!=−1; v použitém oboru m>=0 není singularita.

Pro úlohu 11 rozepíšeme 1/(k(k−1))=1/(k−1)−1/k.
Posunem indexu a H_(j+1)=H_j+1/(j+1) dostáváme

```text
sum_{k=2}^n H_k/(k(k−1)) = 2−(H_n+1)/n,    n>=1.        (H6)
```

Pro n=1 je součet prázdný a pravá strana 0; n=0
odpověď výslovně vylučuje.

## Binomická transformace (10), věta A a úlohy 9,13

Nechť `S_n(x)=sum_{k=1}^n C(n,k)x^k H_k`. Pascalovo
pravidlo a k C(n+1,k)=(n+1)C(n,k−1) dávají

```text
S_(n+1)(x)=(1+x)S_n(x)+((1+x)^(n+1)−1)/(n+1), S_0=0.
```

Teleskopování po vydělení (1+x)^(n+1) dává pro x!=−1
rovnici (10). Její polynomiální podoba je

```text
S_n(x)=(1+x)^n H_n−sum_{j=1}^n (1+x)^(n−j)/j.            (H7)
```

Platí pro všechna komplexní x včetně x=−1. Pro n>=1
zde přežije jediný člen j=n, a proto S_n(−1)=−1/n.
Pro n=0 je S_0=0, jak opravuje odpověď 9 z roku 2022.

Pro reálné x>0 a n>=0 má logaritmická řada
`log(1+1/x)=sum_{j>=1}1/(j(1+x)^j)` kladné členy.
Ocas za n je kladný a ostře menší než
`1/((n+1)x(1+x)^n)`, protože 1/j<=1/(n+1)
a pro j>n+1 je nerovnost ostrá. Vynásobení (1+x)^n
v (H7) dokazuje větu A včetně mezí 0<epsilon<1/(x(n+1)).
Také n=0 je platné: epsilon=log(1+1/x)<1/x.

V úloze 13 jsou obě strany polynomy v x. Jejich
derivace jsou `sum_{j=0}^{n−1} x^j`; rovnost se ověří
v x=1, kde mají obě hodnotu H_n. Tím je pro všechna x
prokázána identita

```text
sum_{k=1}^n x^k/k = H_n+sum_{k=1}^n C(n,k)(x−1)^k/k.
```

Případ n=0 je prázdný a v x=0 dostáváme související
alternující binomický součet.

## Kvadratické a konvoluční součty, úlohy 14–16,21–22

Rozdělení čtverce 1<=j,k<=n na dvě trojúhelníkové
oblasti a diagonálu dává

```text
sum_{k=1}^n H_k/k = (H_n²+H_n^(2))/2,
sum_{k=1}^n H_k/(k+1) = (H_(n+1)²−H_(n+1)^(2))/2.        (H8)
```

Pro úlohu 15 použijeme rozdíl
`H_k²−H_(k−1)²=2H_k/k−1/k²` a sumaci po částech.
Spolu s (H4) vyjde

```text
sum_{k=1}^n H_k² = (n+1)H_n²−(2n+1)H_n+2n.              (H9)
```

Oddělení sudých jmenovatelů v H_(2n) dává pro n>=0
`sum_{k=1}^n 1/(2k−1)=H_(2n)−H_n/2`. Původní
odpověď H_(2n−1)−H_(n−1)/2 je stejná pro n>=1;
náhrada z 2016 zahrnuje i n=0 bez H_(−1).

Položme N=n+1. V úloze 21 změníme dvojici j<=k
na j,b s b=N−k, tedy j,b>=1 a j+b<=N. Potom

```text
sum_{k=1}^n H_k/(n+1−k)
 = sum_{s=2}^N sum_{j=1}^{s−1} 1/(j(s−j))
 = 2 sum_{s=2}^N H_(s−1)/s
 = H_N²−H_N^(2).                                        (H10)
```

Vnitřní rovnost používá 1/(j(s−j))=(1/j+1/(s−j))/s.
Poslední rovnost je druhá trojúhelníková identita (H8).

Pro úlohu 22 spočítáme, pro kolik k platí a<=k a
b<=n−k: je to n+1−a−b, pokud a+b<=n. Proto

```text
sum_{k=0}^n H_k H_(n−k)
 = sum_{a,b>=1, a+b<=n}(n+1−a−b)/(ab)
 = (n+1)(H_n²−H_n^(2))−2n(H_n−1).                       (H11)
```

Použili jsme (H10) s N=n a
`sum_{a=1}^{n−1}(n−a)/a=nH_n−n`. n=0 je ověřeno
přímo jako 0=0. Také n=1 má nulové obě strany.

## Přidaná úloha 25: dvě uspořádané sumace

Úloha byla přidána 11. února 2013; její původní odpověď
měla prohozené výrazy, opravené 1. března 2022. Definuje
`H_n^(u,v)=sum_{1<=j<=k<=n} 1/(j^u k^v)`.
Pro libovolné komplexní u,v a celé n>=0 přímo dostáváme

```text
H_n^(0,v)=H_n^(v−1),
H_n^(u,0)=sum_{k=1}^n H_k^(u)
          =(n+1)H_n^(u)−H_n^(u−1),
H_n^(u,v)+H_n^(v,u)=H_n^(u)H_n^(v)+H_n^(u+v).            (H12)
```

Poslední rovnost rozděluje čtverec indexů na dvě
trojúhelníkové oblasti, které diagonálu počítají dvakrát.
Dosazení u=1,v=0 dává přesně (H4). n=0 opět není výjimkou.
Eulerův odkaz z roku 1775 je oddělený pramenný úkol.
