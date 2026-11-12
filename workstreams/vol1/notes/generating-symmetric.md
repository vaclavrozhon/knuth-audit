# §1.2.9: symetrické funkce a úlohy 7–11, 18

Audit 1. listopadu 2026; originály s. 92–95 a 496–497
zobrazeny. Proměnné x_1,...,x_n komutují. Úplná homogenní
symetrická funkce h_m je součet součinů m proměnných,
v němž se indexy smějí opakovat a zapisují se neklesajícím
způsobem. Elementární symetrická funkce e_m je stejný
součet s navzájem různými indexy. Definujeme h_0=e_0=1.
Mocninný součet je `S_j=sum_{i=1}^n x_i^j` pro j>=1.

## Součiny, rozklady indexu a Newtonovy identity

Z konečného součinu geometrických řad máme formálně

```text
H(z)=sum_{m>=0}h_m z^m=product_i(1-x_i z)^(-1),
log H(z)=sum_{j>=1}S_j z^j/j.                          (S1)
```

Formální logaritmus `log(1+u)=sum_{j>=1}(-1)^(j-1)u^j/j`
je dovolen, protože u má nulový konstantní člen. Jeho inverzí
je formální exponenciála. Exponenciací druhé rovnosti a volbou
k_j členů stupně j dostaneme

```text
h_m=sum_{k_1+2k_2+...+m k_m=m}
           product_{j=1}^m S_j^k_j/(j^k_j k_j!).       (S2)
```

Součet je konečný: k_j<=m/j a j<=m. Odpovídá rozkladům m
na kladné části; k_j udává počet částí velikosti j. Tím je
doložen každý krok (33)–(38) a úloha 7. U knižního příkladu
m=12, k_1=1,k_2=3,k_5=1 je jmenovatel `1! 2^3 3! 5=240`.
Pro m=2,3 dostáváme uvedené výrazy; pro úlohu 9:

```text
h_4=(S_1^4+6 S_1^2 S_2+3 S_2^2+8 S_1 S_3+6 S_4)/24.  (S3)
```

Derivace (S1) dává `H'/H=sum_{j>=1}S_j z^(j-1)`.
Porovnání z^(m-1) dává
`m h_m=sum_{j=1}^m S_j h_(m-j)` pro m>=1. To je (39)
po opravě 2023, která odstranila kolizi indexu m s n,
počtem původních proměnných. Dodatek h_0=1 pochází z roku 2024.

Úloha 10: ze součinu `E(z)=product_i(1+x_i z)=sum e_m z^m`
máme `log E(z)=sum_{j>=1}(-1)^(j-1)S_j z^j/j`.
Ve (S2) se tedy každý S_j nahradí (-1)^(j-1)S_j; výsledný
znaménkový faktor je (-1)^(m-K), kde K=sum_j k_j.
První čtyři výrazy jsou

```text
e_1=S_1,
e_2=(S_1^2-S_2)/2,
e_3=(S_1^3-3S_1S_2+2S_3)/6,
e_4=(S_1^4-6S_1^2S_2+3S_2^2+8S_1S_3-6S_4)/24.        (S4)
```

Derivace dává `m e_m=sum_{j=1}^m(-1)^(j-1) S_j e_(m-j)`.
Změna názvu a_m na e_m je známá oprava z roku 2002;
definice e_0=1 byla výslovně doplněna roku 2024.

Úloha 11: pro m>=1 je `S_m=m[z^m]log H(z)`. V logaritmické
řadě monom `h_1^k_1...h_m^k_m` vzniká pouze z mocniny K,
jeho multinomický koeficient je K!/product k_j!. Hledaný
koeficient proto je

```text
(-1)^(K-1) m (K-1)! / product_{j=1}^m k_j!.            (S5)
```

K>=1, takže faktoriál je definován. Při vyjádření S_m pomocí
e_j přibude (-1)^(m-1), protože mocninné součty v log E
mají tento faktor. To odpovídá odpovědi s. 497. Historické
věty o Newtonovi a Girardovi jsou samostatné neuzavřené položky;
matematická platnost (S1)–(S5) na nich nezávisí.

## Specializace na celé indexy

Úloha 18 dosazuje x_i=i pro 1<=i<=n. Ze stoupajícího
faktoriálu `x(x+1)...(x+n)=sum_j c(n+1,j)x^j`, kde c
jsou nezáporná Stirlingova čísla prvního druhu, dostaneme

```text
e_r(1,...,n)=c(n+1,n+1-r).                             (S6)
```

Z `sum_{k>=0}S(k,n)z^k=z^n/product_{i=1}^n(1-iz)`,
kde S jsou Stirlingova čísla druhého druhu, vyjde

```text
h_r(1,...,n)=S(n+r,n).                                (S7)
```

Pro r>n je elementární funkce 0 a (S6) to respektuje;
včetně r=n+1 je c(n+1,0)=0. Pro r=0 jsou obě hodnoty 1.
Počítání přímých součinů bude porovnáno s (S2), (S4),
(S5), (S6), (S7) v samostatném přesném validátoru tohoto bloku.
