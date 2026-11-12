# §1.2.7-20: integrální transformace a V1-C0010

Audit 1. listopadu 2026. Zadání s. 79 (strana souboru 94)
a odpověď s. 492 (strana souboru 507) byly zobrazeny.
`H_n=sum_{j=1}^n 1/j`, H_0=0, je n-té harmonické číslo.
Zadání předpokládá konvergenci `f(x)=sum_{n>=0} a_n x^n`
v bodě x=x_0 a žádá dokázat

```text
sum_{n>=0} a_n x_0^n H_n
 = integral_0^1 (f(x_0)−f(x_0 y))/(1−y) dy.              (T1)
```

Samotný předpoklad nestačí. Následující příklad dokonce
splňuje **absolutní konvergenci** původní řady v x_0=1
a má pravý integrand spojitě prodloužitelný do y=1.

## Přesný protipříklad

Pro celá k>=1 položme `N_k=2^(2^k)` a definujme koeficienty

```text
a_(N_k)=2^(−k),  a_(N_k+1)=−2^(−k),
a_n=0 na ostatních indexech.                            (T2)
```

Dvojice indexů se nepřekrývají. Součet absolutních hodnot
koeficientů je `2 sum_{k>=1}2^(−k)=2`, takže řada
konverguje absolutně a stejnoměrně na |x|<=1. Seskupení
dvojic je tedy v původní řadě legitimní a dává

```text
f(x)=(1−x)g(x),    g(x)=sum_{k>=1} 2^(−k) x^(N_k),
f(1)=0,           g(1)=1.                              (T3)
```

Funkce g je spojitá na [0,1], opět stejnoměrnou konvergencí.
Pravý integrand v (T1) je pro y<1 přesně −g(y), a tedy
má v y=1 spojitou hodnotu −1. Jeho vlastní integrál je

```text
−sum_{k>=1} 2^(−k)/(N_k+1),                            (T4)
```

konečné záporné číslo. Integrace po členech v (T4) je
oprávněná stejnoměrnou konvergencí g, případně nezáporností
jejích členů a konečným součtem integrálů.

Naproti tomu levá řada v (T1) nemůže konvergovat.
Již ověřená knižní mez (2) dává

```text
a_(N_k) H_(N_k)
 = 2^(−k) H_(2^(2^k))
 >= 2^(−k)(1+2^(k−1)) > 1/2.                           (T5)
```

Členy tedy nejdou k nule. Párové součty by daly (T4),
ale to je seskupení divergentní řady; není její obyčejnou
konvergencí podle n. Rovnice neuvádí takovou sumační metodu.
Protipříklad také není problémem divergentního pravého
integrálu nebo podmíněné konvergence původní mocninné řady.

## Dostačující oprava a důkaz

Stačí předpokládat

```text
sum_{n>=0} |a_n x_0^n| H_n < infinity.                  (T6)
```

Platí totiž konečná identita
`H_n=integral_0^1 (1−y^n)/(1−y)dy`, včetně n=0.
Absolutní integrály jednotlivých členů součtu jsou
právě `|a_n x_0^n|H_n`. Podmínka (T6) dovoluje podle
absolutní integrability prohodit integrál a řadu a dává
(T1). Zvláště (T6) platí, když x_0 leží **uvnitř** kruhu
konvergence mocninné řady: pro |x_0|<rho<R jsou
|a_n|rho^n omezené a geometrický faktor (|x_0|/rho)^n
převáží H_n<=1+log n. Pro x_0=0 jsou obě strany 0.

Všech pět vrstev errat `all1-prepre`, `all1-pre`, `all1`,
`err1` a `err1.textxt`, ověřených 1. listopadu 2026,
bylo prohledáno podle stránky, úlohy i konvergenčního znění.
Změna z 3. března 2026 pouze zkracuje bibliografii odpovědi
20 odstraněním Gouldova odkazu; nezpřísňuje předpoklad.
Nález je proto **V1-C0010 confirmed** v našich zdrojích.
Prvenství, autorovo přijetí a fyzický dotisk nejsou doloženy.
Citovaný článek AMM 69 (1962), 239 dosud nebyl získán;
o jeho hypotézách tento nález nic netvrdí.
