# §1.2.11.3-11: parametrické součty Q_x a R_x

Pro celé n≥1 a reálné x používáme definice Q_x,R_x z
`asymptotic-findings.md`, oddíl V1-C0018. Zde ověřujeme všechny větve
rozvojů a přesný význam jejich zbytků. Výsledek pro záporné x vyžaduje
opravu popsanou v uvedeném nálezu.

## Přesné integrály a větve

Binomická věta a beta integrál dávají

```text
Q_x(n) = integral_0^infty exp(−t)(1+xt/n)^(n−1) dt,
R_x(n) = n integral_0^1 exp(nxt)(1−t)^(n−1) dt
       = integral_0^n exp(xt)(1−t/n)^(n−1) dt.            (P1)
```

První integrand je polynom krát exponenciála, druhá řada pro exp
konverguje na konečném intervalu absolutně pro všechna pevná x, takže
obě výměny součtu a integrálu jsou přípustné.
Rozdělení exponenciální řady dává pro x≠0

`x Q_x(n)+R_(1/x)(n)=n!(x/n)^n exp(n/x)`.                 (P2)

Vazby na gama funkci na s. 505 souhlasí s (P1):
`R_x=n!(exp(x)/(nx))^n γ(n,nx)/(n−1)!`
`=1+(exp(x)/(nx))^n γ(n+1,nx)` pro x≠0.
Pro záporné x je n celé, takže integrály přes zápornou úsečku mají
celočíselné mocniny a nevzniká volba komplexní větve. Pro x=0 jsou
Q_0=R_0=1 a singularity těchto výrazů odstranitelné limitou.

Pro pevné x<1 dává druhý integrál (P1) úplný rozvoj R_x v 1/n.
Pro 0≤x<1 dává první integrál totéž pro Q_x: dominuje levý krajní bod,
protože `exp(−t)(1+xt/n)^(n−1)≤exp(−(1−x)t)`.
Pro x<0 je nutné první integrál rozdělit v −n/x; přesný ocas
`T_x=n!x^(n−1)exp(n/x)/n^n` nelze obecně zanedbat. Zbytek je
`Q_x−T_x=−R_(1/x)/x`, takže jeho rozvoj plyne z již ověřené větve R.
Pro x>1 dá (P2) rozvoj Q_x s týmž T_x a rozvoj R_x s exponenciálním
členem `U_x=n!exp(nx)/(n^n x^n)`, protože obě reciproké hodnoty jsou v (0,1).

## Koeficienty a význam dvojitých součtů

Označme `R_x(n) ~ ∑_{m≥0} a_m(x)n^(−m)` v algebraické větvi x<1.
Přesná řada pro R splňuje diferenciální rovnici
`x ∂R_x/∂x = n[1−(1−x)R_x]`.
Stejnou rekurenci koeficientů lze získat integrací lokálně rozvinutého
integrandu; rovnice sama bez analýzy zbytku by existenci rozvoje nedokazovala.
Dává

`a_0=1/(1−x)`, `a_m=−x a'_(m−1)/(1−x)`.

Definujme Eulerova čísla druhého řádu A(m,j) zde přesně rekurencí
`A(1,0)=1`, hodnotou 0 mimo 0≤j≤m−1, a

`A(m,j)=(j+1)A(m−1,j)+(2m−j−1)A(m−1,j−1)`, m≥2.

Pak pro m≥1

```text
r_m(x)=sum_{j=0}^{m−1} A(m,j)x^(j+1),
q_m(x)=sum_{j=0}^{m−1} A(m,j)x^(2m−1−j)=x^(2m)r_m(1/x),
a_m(x)=(−1)^m r_m(x)/(1−x)^(2m+1).                     (P3)
```

Dosazení do rekurence a_m přesně dává definici A. První řádky jsou
1; 1,2; 1,8,6; 1,22,58,24. Reciproká identita (P2) transformuje (P3)
na vytištěné koeficienty q_m v každé uvedené větvi. Například
r_2=x+2x² a q_2=2x²+x³. To ověřuje i pořadí indexů v obou polynomech.

Dvojité Stirlingovy součty na s. 506 jsou použitelné pro výpočet
**formálních koeficientů** v 1/n: pro každý pevný m konverguje suma
v x pro |x|<1, jak kniha výslovně říká. Nejsou tvrzením o absolutní
konvergenci součtu přes oba indexy pro každé pevné n. Pro Q je původní
součet v k konečný, ale po změně pořadí se ztrácí rušení nulových
klesajících mocnin; pro R je rozvoj jednotlivých recipročních faktorů
v 1/n závislý na k. Oprava 10.8.2008 doplňuje k,m≥0, ale sama
asymptotické zdůvodnění nedává. To poskytují integrály (P1).

## Zbytky v rozvojích

Pro pevné x<1 a R rozdělme integrační proměnnou v t=n^δ, kde
0<δ<1/2. Taylorova řada logaritmu je na první části stejnoměrná.
Po zachování dostatečného počtu členů lze zbytek omezit
`C n^(−m−1)(1+t)^L exp(−c t)` s pevnými C,L,c>0; vzniká to z
Taylorova zbytku logaritmu a exponenciály a z nerovnosti
`exp(xt)(1−t/n)^(n−1)≤exp(−(1−x)t/2)` pro velké n.
Na druhé části tento exponenciální odhad pohlcuje všechny mocniny n.
Integrace prvního majorantu dává O(n^(−m−1)). Stejný argument s
ln(1+xt/n) a c=1−x ověřuje Q na 0≤x<1. Je-li pro daný m potřeba více
Taylorových členů kvůli zvolené δ, nejprve je ponecháme a jejich
integrované příspěvky řádu n^(−m−1) či menší absorbujeme do zbytku.

**Rovnoměrnost pro záporné x.** Obě neexponenciální části lze převést
na násobek společného integrálu

```text
K(n,z)=integral_0^(n/z) exp((z−1)v)(1−zv/n)^(n−1) dv,
0≤z≤1; při z=0 je integrál integral_0^infty exp(−v)dv.
```

Pro R_x s x<0 je z=1/(1−x) a násobek 1/(1−x)≤1.
Pro Q_x−T_x je z=x/(x−1) a násobek opět 1/(1−x)≤1.
Pro n≥2 a 0≤v<n/z je integrand ≤exp(−v/2), neboť
`(z−1)v+(n−1)ln(1−zv/n)≤−v+zv/n≤−v/2`.
Taylorovy koeficienty i majoranty na v≤n^δ jsou polynomy v z na
kompaktním intervalu [0,1]; všechny jejich konstanty lze tedy volit
nezávisle na z. Předchozí rozdělení integrálu dokazuje zbytek
O(n^(−m−1)) s konstantou nezávislou na x<0 pro **R_x a Q_x−T_x**.
Právě tato druhá výhrada v knize chybí; samotné Q_x není takto omezeno.

V bodě x=−1 z (P2) přesně plyne
`R_(−1)(n)−Q_(−1)(n)=(−1)^n n!/(exp(n)n^n)`.
Stirlingova formule dává vedoucí člen `(−1)^n sqrt(2πn)exp(−2n)`.
Závěrečná poznámka odpovědi je tedy správná po známém doplnění závorek
ve jmenovateli z 10.8.2008. Bod x=1 je z rozvojů záměrně vyňat a je
řešen odděleně hlavním textem; jeho odmocninový řád se s žádnou větví
s pevným x≠1 nezaměňuje.
