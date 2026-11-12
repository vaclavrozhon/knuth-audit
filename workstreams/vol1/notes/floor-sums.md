# §1.2.4: součty celých částí

Kontrola 1. listopadu 2026. Položky V1-X0002 a V1-X0005.
Výsledek: zadání cvičení 37–38 a oba hlavní vzorce v odpovědi 37 jsou správné.
Poznámka o symetrii za vzorcem pro horní celé části obsahuje známé erratum.

## Zdroj a rozsah

Třetí vydání, první dotisk z května 1997. Zadání je na tištěné s. 43
([strana souboru 58](../images/vol1-file058-p43.png)); odpovědi na s. 478
([strana souboru 493](../images/vol1-file493-p478.png)). Oba obrazy byly prohlédnuty.
`floor(t)` je největší celé číslo nejvýše t, `ceil(t)` nejmenší celé číslo
nejméně t. Zlomek `frac(t) = t - floor(t)` leží v intervalu [0,1).

## Cvičení 37: důkaz i pro záporné m a x

Nechť m je celé, n kladné celé, x reálné a d = gcd(m,n) kladný největší
společný dělitel. Položme t = n/d, u = m/d a x = dq+r, kde q = floor(x/d)
a 0 <= r < d. Platí gcd(u,t)=1, včetně případu m=0, kdy t=1.

V každém bloku t po sobě jdoucích indexů k procházejí zbytky uk+q modulo t
právě hodnoty 0,...,t-1. Proto zlomkové části (mk+x)/n tvoří d kopií seznamu

```text
r/n, r/n + 1/t, ..., r/n + (t-1)/t.
```

Žádný člen nepřesáhne ani nedosáhne 1, protože r/n < 1/t. Jejich součet je
`(n-d)/2 + r`. Součet samotných (mk+x)/n pro 0 <= k < n je
`m(n-1)/2 + x`. Odečtením dostaneme přesně

```text
sum_{0 <= k < n} floor((mk+x)/n)
  = ((m-1)(n-1) + d-1)/2 + d floor(x/d).                 (1)
```

Použitím `ceil(v) = -floor(-v)` v (1), se záměnou (m,x) za (-m,-x), vyjde

```text
sum_{0 <= k < n} ceil((mk+x)/n)
  = ((m+1)(n-1) - d+1)/2 + d ceil(x/d).                  (2)
```

To ověřuje i odpověď v knize; žádný předpoklad m>0 není pro (1)–(2) nutný.

## V1-X0005: známá chybná mez v poznámce o symetrii

Ve skenu se doporučuje rozsah `0 <= k <= n`. Pro kladná m,n však není
takový součet symetrický: při m=1, n=2, x=2 je 5, po záměně m,n je 6.
Správný rozsah je `0 < k <= n`. Přechod od (2) k tomuto rozsahu přidává m,
takže výsledek je

```text
(mn+m+n-d)/2 + d ceil(x/d),                             (3)
```

což už je symetrické v kladných m,n. Jde přesně o opravu z 8. listopadu 2005
v `all1-prepre`, s. 31 ([obraz errata](../images/errata-all1-prepre-file031.png)).
`all1`, položka s. 478 z 12. května 2026, ještě zpřesňuje slovní označení
této symetrie. Nejde o nový nález.

## Cvičení 38: důkaz počítáním překročených prahů

Nechť y>0, N=ceil(y), q=floor(x) a r=x-q, tedy 0<=r<1. Sčítané indexy
jsou k=0,...,N-1. Protože 0<=k/y<1, každá celá část x+k/y je q nebo q+1.
Hodnotu q+1 dostane právě tehdy, když k>=y(1-r). Počet takových k je
`N-ceil(y(1-r))`, včetně případů r=0 a celočíselného prahu. Celý součet je

```text
N(q+1) - ceil(y(1-r)).                                 (4)
```

Pravá strana Knuthova vzorce se přepíše jako

```text
floor(xy + floor(x+1)(ceil(y)-y))
  = floor(N(q+1) - y(1-r))
  = N(q+1) - ceil(y(1-r)),
```

tedy (4). Pro celočíselné y=n dostaneme Hermitovu identitu
`sum_{0<=k<n} floor(x+k/n) = floor(nx)`. Důkaz platí pro všechna reálná x,
bez aproximace a bez předpokladu x>=0.

## Výpočetní kontrola a errata

[Program](../check_first_blocks.py), funkce `floor_sums`, používá pouze
celá čísla a přesné racionální zlomky. [Výstup](../results/first-blocks.json):

- (1) i (2): 126 600 trojic, m=-12,...,12, n=1,...,24 a 211 různých x;
  x jsou všechny různé zlomky a/b s -20<=a<=20 a 1<=b<=8.
- Cvičení 38: 42 622 dvojic na racionální síti a 10 818 dalších kontrol
  přesně v prahu a ve vzdálenosti 1/1000003 po jeho obou stranách.
- Opravená symetrie (3): 30 384 trojic pro 1<=m,n<=12 a stejná x.

Vše prošlo. Tyto konečné kontroly doplňují uvedené obecné důkazy.
Prohledány `all1-prepre`, `all1-pre`, `all1`, `err1` a aktuální TeX `err1.textxt`
podle s. 43–44, 478–479 a výrazů pro cvičení, celé části a Buscheho identitu.
Jiná oprava těchto dvou zadání nebo vzorců (1)–(2) nebyla při této kontrole
nalezena. Aktuálnost a přesné hashe viz [zdrojový záznam](sources-and-scope.md).

## V1-X0008: zavádějící přepis sousedního cvičení

V `md/vol1/06-1.2.4-integer-functions.md` chybí u `csc` ve cvičení 40
exponent 2. [Sken s. 44](../images/vol1-file059-p44.png) má správně
`csc^2(pi x)`. Podezření na chybu v knize je tím zamítnuto. Celé cvičení 40
ani jeho klasifikace funkcí tím nejsou označeny za prověřené.
