# §4.2.4: rozsah empirické a historické kontroly

Kontrola 2.11.2026. Celý text253–264 a odpovědi619–623 byly vizuálně
přečteny. Matematické jádro, všech20 úloh a doplňující důkazy jsou
v `benford-math.md`, `benford-axioms.md`, `benford-asymptotic.md`
a `benford-addition-experiment.md`. Následující poznámky rozlišují
potvrzenou citaci, prověřený obsah a nedostupný podklad.

## Empirická tvrzení

- Newcomb1881, tištěné39–40 (soubor2–3), obě strany vizuálně přečteny.
  Primární článek skutečně spojuje opotřebení logaritmických tabulek
  s nestejnými četnostmi vedoucích číslic, uvádí logaritmický zákon
  a otázku antilogaritmů. [PDF](../sources/newcomb-1881.pdf),
  [metadata](../sources/newcomb-1881.json).
  Absolutní historické prvenství nad rámec tohoto dokladu netvrdíme.
- Benford1938, tištěné551–553 (soubor2–4), vizuálně přečteny.
  TabulkaI uvádí20 skupin a20229 pozorování; součet20 zobrazených
  četností je přesně20229, uložen v `results/benford-context.json`.
  Rok1938 je rok publikace, datum přednesení1937 není rozpor.
  [PDF](../sources/benford-1938.pdf), [metadata](../sources/benford-1938.json).
  Původní jednotlivá pozorování nebyla rekonstruována; údaj30.6% v článku
  je průměr skupinových procent a nemá se bez dalšího vydávat za váženou
  četnost všech20229 čísel. Kniha tuto záměnu netvrdí.
- Třikrát30 jedniček mezi prvními100 hodnotami n!,2^n,F_n bylo již
  ověřeno přesnými celými čísly v `results/benford-math.json`.
- Sweeney1965, IBM Systems Journal4,31–42: primární PDF se nepodařilo
  stáhnout z původního archivu ani veřejných zrcadel; podrobnosti403,
  connection refused, timeout a chybný hostname/TLS jsou v metadatech
  `sources/sweeney-1965*.json`. Nebyla obcházena kontrola TLS.
  Bibliografický záznam a veřejně indexovaný abstrakt potvrzují téma,
  radices a analýzu milionu operací; tvrzení „over250000“ s tím samo
  není v rozporu. Nelze z toho potvrdit každé číslo tabulek1–2 ani
  jejich šest původních programů. Vlastní experiment úlohy2 poskytuje
  nová, zcela popsaná data; odlišnost není vyvrácením historického měření.
- Dostupná elektronická tabulka2.3 Abramowitz–Stegun na str.7 je
  **pozdější verze s konstantami upravenými1969**, jak uvádí přímo její
  záhlaví. [Obraz](../sources/abramowitz-stegun-table2-3.jpg) byl přečten.
  [Tiráž elektronického zdroje](https://iopb.res.in/~somen/abramowitz_and_stegun/intro.htm)
  uvádí10.dotisk1972. Proto z této stránky neověřujeme ani nevyvracíme
  Knuthův počet8 z28 pro vydání1964; změna podkladu by nebyla přípustná.

## Matematické odkazy a datace

- Janvresse–de la Rue2004, autorská verze, str.7–9 vizuálně přečteny:
  obsahují Flehingerovu rekurzi, pravděpodobnostní interpretaci a
  geometrickou konvergenci při opakovaném průměrování. Je to nezávislá
  kontrola směru Q/F, nikoli řešení naší asymptotiky při n→∞ v úloze20.
  [PDF](../sources/janvresse-de-la-rue-2004.pdf).
- Duncan1967, Fibonacci Quarterly5,137–140, celé čtyři strany vizuálně
  přečteny. Dokazuje rovnoměrnost logaritmů Fibonacciho čísel modulo1
  pomocí Binetova vzorce a iracionální rotace. Jeho indexování začíná
  1,2 místo1,1; konečný posun indexu zákon nemění. Knižní citace souhlasí.
  [PDF](../sources/duncan-1967.pdf).
- Diaconis1977, Annals of Probability5,72–81: vizuálně přečteny72,74–76
  (soubor2,4–6). Věta3 je o n!, věta4 o jednotlivých řádcích binomických
  koeficientů, přesně v uvedeném smyslu. Nejde pouze o průměr přes celý
  Pascalův trojúhelník. [PDF](../sources/diaconis-1977-leading-digits.pdf).
  Na str.76 jsou v pomocné fázi a její druhé derivaci znaménkové
  nesrovnalosti; nepřenášíme je do auditu Knutha jako nový nález.
  Platnost citovaných závěrů kontroluje samostatné odvození níže.
- Berger–Bunimovich–Hill, TAMS357,197–219: původní PDF str.197–198
  vizuálně přečteno. Hlavička výslovně uvádí elektronické publikování
 16.4.2004 a copyright2004, zatímco svazek je běžně citován rokem2005.
  Rok2004 v Knuthově doplňku proto neoznačujeme za chybu.
  [PDF](../sources/berger-bunimovich-hill-2004.pdf),
  [autorský seznam](https://www.math.ualberta.ca/~aberger/Publications.html).
  Ověřen tematický rozsah a kvalifikace „almost all“, nikoli všechny
  věty celého23stránkového článku.
- Jech, autorský text o konečně aditivních mírách: str.2,5–6 vizuálně
  přečteny. Jeho míra je výslovně na všech podmnožinách; tento zdroj
  tedy sám nedokazuje Knuthovu verzi18 s částečným oborem.
  [PDF](../sources/jech-leading-digits.pdf). Vlastní důkaz slabé verze
  je úplný v `benford-axioms.md`.
- Conway–Michael J. T. Guy: přetisk článku „Pi in Fours“ v Eureka62,
  str.28–29 (soubor30–31), vizuálně přečten. Přetisk uvádí původní
  číslo25(1962). Iteruje faktoriál od4 a zkoumá opakované odmocniny;
  souvislost se zdejší otevřenou otázkou je tematická, nikoli totožná
  formulace. Původní číslo25 nebylo získáno. Viz přesné vymezeníC0092.
- Barlow–Bareiss1985: [institucionální záznam autora](https://pure.psu.edu/en/publications/on-roundoff-error-distributions-in-floating-point-and-logarithmic/)
  potvrzuje Computing34(4),325–347, DOI10.1007/BF02251833 a pravděpodobnostní
  analýzu zaokrouhlování. Úplný primární článek nebyl přečten.
- Schatte1990: [obsah čísla vydavatele](https://onlinelibrary.wiley.com/doi/10.1002/mana.v148%3A1/issuetoc)
  potvrzuje název „On Benford’s Law for Continued Fractions“, Math.Nachr.148,
 137–144. Plný důkaz pro Hurwitzovy řetězové zlomky zde nebyl reprodukován;
  tvrzení je v knize citovaným externím výsledkem, nikoli nově ověřenou větou auditu.
- U Franel1917, Flehinger1966, Hamming1970, Raimi1969/1976, Schatte1973/1988,
  Tsuji1952, Cesàro1888 a Diaconisovy disertace1974 nebyly všechny primární
  dokumenty získány. Jejich bibliografické uvádění není tvrzením, že jsme
  je celé přečetli. Obsah úloh a hlavní vlastní důkazy knihy byly prověřeny
  nezávisle; nejširší historické priority a zobecnění těchto článků nejsou
  součástí potvrzených nálezů. Pokus o Raimiho1976 PDF skončilHTTP406.

## Samostatná kontrola n! a binomických řádků

Pišme `e(t)=exp(2πit)`. Weylovo kritérium redukuje rovnoměrnost modulo1
na `N^-1 sum e(h x_n)→0` pro každé nenulové celé h.
Použijeme standardní odhad druhé derivace: pokud na intervalu délky L
platí `lambda<=|f''|<=C lambda`, potom

```
|sum_{integer j in interval} e(f(j))|
    = O_C(L sqrt(lambda)+1/sqrt(lambda)).
```
Eulerova gama funkce je `Gamma(t)=integral_0^infinity u^(t−1)exp(−u) du`
pro t>0. Definujme `g(x)=ln Gamma(x+1)` pro x>0. Jeho druhá derivace je
`g''(x)=sum_{k>=0}(x+1+k)^-2`. Porovnáním klesající řady s integrály
na sousedních intervalech dostaneme `1/(x+1)<=g''(x)<=1/x`.

Pro n! je přesná fáze `f(x)=h g(x)/ln10`. Na `[epsilon N,N]`, kde
0<epsilon<1 je pevné, je její druhá derivace v absolutní hodnotě
mezi dvěma kladnými násobky1/N. Příspěvek tohoto úseku je tedy
`O_(epsilon,h)(sqrt(N))`; prvních nejvýše epsilon N+1 členů má
absolutní součet nejvýše epsilon N+1. Vydělení N, limita N→∞ a potom
epsilon→0 dávají Weylovo kritérium.

Pro n-tý binomický řádek je přesná fáze až na konstantu
`f_n(x)=−h(g(x)+g(n−x))/ln10`. Na `[epsilon n,(1−epsilon)n]`
platí opět `|f_n''|` mezi dvěma kladnými násobky1/n, protože oba
členy g'' se **sčítají**. Prostředek má součet `O_(epsilon,h)(sqrt(n))`,
oba konce dohromady nejvýše2epsilon n+2. Stejná dvojí limita potvrzuje
rovnoměrnost logaritmů každého řádku, a tedy knižní vzorec na str.622.
Toto odvození používá přesné fáze; neodhazuje Stirlingův logaritmický
člen ani neodvozuje závěr z číselného experimentu.

## Co přesně mohou znamenat „mírná omezení“ pro součiny a součty

Následující vlastní argumenty jsou dostatečné případy, nikoli tvrzení,
že reprodukují nejsilnější verze citovaných článků.
Pro celočíselný základ b>=2 a nezávislé stejně rozdělené kladné veličiny X_i položme
`phi_k=E exp(2πik log_b X_1)`. Pokud `|phi_k|<1` pro každé nenulové
celé k (stačí například nenulová absolutně spojitá složka rozdělení
logaritmu), má logaritmus součinu modulo1 Fourierovy koeficienty
`phi_k^n→0`. Aproximace spojitých funkcí trigonometrickými polynomy
pak dává slabou konvergenci k rovnoměrnému rozdělení. Jde o rozdělení
n-tého součinu, nikoli automaticky tvrzení o každé jednotlivé trajektorii.

Pro součty kladných X_i s konečným kladným průměrem mu silný zákon
velkých čísel dává téměř jistě `log_b(sum_{i<=n}X_i)=log_b(n mu)+o(1)`.
Vezměme indikátor libovolného pevného intervalu logaritmických zlomkových
částí. Případné neshody způsobené o(1) leží pro dost velké n v libovolně
malých okolích dvou krajů. Q/F, s posunutým intervalem a obecným základem,
dávají po opakovaném průměrování těmto okolím nejvýše jejich délku.
Nejprve počet průměrování→∞, potom šířka okolí→0, proto opakované
průměrování součtů dává logaritmický zákon téměř jistě. Obyčejná hustota
nemusí existovat, jak ukazuje už konstantní X_i=1.

Heuristiky na str.255 ani rozsáhlé empirické zkušenosti nemají být čteny
jako univerzální zákon všech vstupů. Kniha tuto výhradu výslovně obsahuje;
naše vlastní experimenty ji konkretizují. Nové potvrzené body sekce jsou
C0092, C0093 aC0094, nikoli samotná omezenost těchto heuristik.
