# §1.2.9: kombinatorické aplikace a koeficientové závorky

Audit 1. listopadu 2026. Originály úloh s. 94–96 a odpovědí
496–499 byly zobrazeny. `[z^n]F` znamená koeficient u z^n.
Všechny řady jsou nejprve formální nad racionálními nebo
komplexními čísly, aby každou manipulaci zdůvodnila konečnost
příspěvků do daného stupně. Analytické obory uvádíme zvlášť.

## Úloha 8: rozklady čísla

Rozklad n je multiset kladných celých čísel se součtem n.
Počet rozkladů je p(n), s p(0)=1 pro prázdný multiset.
Zvolený počet k_j částí velikosti j přispívá z^(j k_j).
Nezávislou volbou všech k_j>=0 tedy dostáváme

```text
sum_{n>=0}p(n)z^n=product_{j>=1}(1-z^j)^(-1).           (K1)
```

Pro koeficient stupně n stačí j<=n; jde o formálně
jednoznačný součin. Pro |z|<=r<1 je
`sum_j sum_{k>=1}|z|^(jk)/k <=sum_j r^j/(1-r^j)
<=r/(1-r)^2`. Logaritmus součinu tedy konverguje
absolutně a stejnoměrně, což dovoluje i analytickou interpretaci.
Historické tvrzení a odkaz na Pólyovu kapitolu 6 zatím zbývají.

## Úloha 15: polynomy s Fibonacciho rekurencí

Definujme pro celé n>=0

```text
G_n(z)=sum_{k=0}^n binom(n-k,k)z^k
      =sum_{k=0}^n binom(2k-n-1,k)(-z)^k.              (K2)
```

Druhá rovnost plyne z odrazu horního indexu
`binom(n-k,k)=(-1)^k binom(2k-n-1,k)`; platí i tam,
kde první koeficient je nula. Pascalova rekurence dává
G_n=G_(n-1)+zG_(n-2)+[n=0], s G_n=0 pro n<0.
Proto `sum_{n>=0}G_n(z)w^n=1/(1-w-zw^2)`.
Pro alpha,beta=(1 +/- sqrt(1+4z))/2 dostáváme

```text
G_n(z)=sum_{j=0}^n alpha^(n-j)beta^j
      =(alpha^(n+1)-beta^(n+1))/(alpha-beta), z!=-1/4;
G_n(-1/4)=(n+1)/2^n.                                  (K3)
```

První polynomiální tvar dokazuje i hodnotu při dvojitém
kořeni, bez neodůvodněného dělení nulou. V pomocném Markdownu
je místo (K2) jiný vzorec; autoritativní je originál s. 95.

## Úlohy 16 a 22: omezené násobnosti a binární součin

V úloze 16 pro celá n,r>=0 vybereme u každého z n typů
0,1,...,r kusů. Počet možností o celkové velikosti k je
koeficient

```text
G_nr(z)=(1+z+...+z^r)^n=((1-z^(r+1))/(1-z))^n.          (K4)
```

První výraz je platný i v z=1, kde má hodnotu (r+1)^n.
Pro n=0 je prázdný výběr jediný. Při r=1 jsou koeficienty
binom(n,k); bez omezení násobností dostaneme (1-z)^(-n)
a binom(n+k-1,k) pro n>=1. Formální limita r->infinity
platí po každém pevném koeficientu.

V úloze 22 začneme konečnou polynomiální identitou

```text
product_{j=0}^{J-1}(1+z^(2^j))=(1-z^(2^J))/(1-z).       (K5)
```

Po umocnění na parametr r (pomocí formálního logaritmu
s konstantou 0) a přechodu po koeficientech J->infinity
dostáváme `product_{j>=0}(1+z^(2^j))^r=(1-z)^(-r)`.
Každý koeficient je konečným součtem příspěvků jednotlivých
binomických rozvojů. Odpověď je proto binom(r+n-1,n).
Platí pro libovolné komplexní r a n>=0 v tomto formálním
významu, a tedy i pro celé r z běžné kombinatorické interpretace.

## Úlohy 24 a 25: slučování extrakcí

Pro n>=0 a mocninnou řadu G má zG nulový konstantní člen.
Binomická věta pak dává

```text
sum_k binom(m,k)[z^(n-k)]G(z)^k
   =[z^n]sum_{k>=0}binom(m,k)(zG(z))^k
   =[z^n](1+zG(z))^m.                                 (K6)
```

Ve stupni n přispěje pouze 0<=k<=n, i když m není celé.
Pro G=1/(1-z) se pravá strana rovná binom(m+n-1,n)
a levá dává Vandermondův součet
`sum_k binom(m,k)binom(n-1,n-k)`. Při n=0 se hodnota
1 čte přímo z konstantního koeficientu; binom(-1,0)=1
je s tím slučitelné. Pro G=(exp z-1)/z je pravá strana
koeficient exp(mz), tedy m^n/n!. Levá strana je
`sum_k m_under_k S(n,k)/n!`, kde
`m_under_k=m(m-1)...(m-k+1)` a S jsou Stirlingova čísla
druhého druhu. Násobení n! uvedené v opravě z 28. března
2026 je nezbytné pro následný odkaz na §1.2.6-(45).

Úloha 25 má ve skutečné sazbě součet

```text
sum_k binom(n,k)binom(2n-2k,n-k)(-2)^k.                (K7)
```

Píšeme druhé binomické číslo jako koeficient
`[z^(n-k)](1+z)^(2n-2k)`, potom přesuneme z^k dovnitř
jediné extrakce. Konečný binomický součet dává

```text
[z^n](1+z)^(2n)(1-2z/(1+z)^2)^n
  =[z^n](1+z^2)^n=binom(n,n/2)[n even].                (K8)
```

Pro n liché je výsledek 0 a symbol binom(n,n/2) se nemusí
definovat; jde o výběrový zápis obou případů. Nahradíme-li
-2 číslem -4, dostaneme `[z^n](1-z)^(2n)=(-1)^n binom(2n,n)`.
Vše platí pro n>=0, včetně n=0. Bibliografický odkaz na
Egorycheva zůstává oddělen od tohoto úplného důkazu.

## Úloha 26: rozšířené závorky a jejich obor

Pro polynom F(z)=sum_j f_j z^j definujme

```text
[F(z)]G(z)=sum_j f_j g_j=[z^0]F(z^(-1))G(z),           (K9)
```

kde g_j=[z^j]G. Suma je konečná; příklad ze zadání je
g_2-2g_5. Tato operace je lineární v obou argumentech,
není to komplexní skalární součin s konjugací.
Obecně stačí, aby indexy F byly shora omezené a indexy G
zdola omezené. Pak se překrývají v konečné množině a
F(z^(-1))G(z) je formální Laurentova řada, tj. má jen
konečně mnoho nenulových záporných mocnin. Tím je (K9)
definováno bez jakéhokoli analytického limitního přechodu.

Při platných oborech plyne přímo z konstantního členu
pravidlo přesouvání faktorů
`[F]GH=[F(z)G(z^(-1))]H` i škálování `[F]G(az)=[F(az)]G(z)`
pro a!=0. U polynomů navíc `[F]G=[G]F`; u nekonečných
řad je vždy třeba znovu zkontrolovat konečnost nebo
absolutní konvergenci párování. Identita
`[F]zG'=[zF']G` plyne z koeficientu j f_j g_j.

Jako kontrola hranic definice vezměme F=G=sum_{j>=0}z^j.
Formální párování by dávalo sumu samých jedniček, tedy není
definováno. Stejně nesmíme po změně z na z^(-1) přepsat
racionální funkci a poté potichu změnit její oblast rozvoje:
`1/(1-z^(-1))` má při rozvoji v záporných mocninách
konstantní člen 1, ale rovná racionální funkce `-z/(1-z)`
má při rozvoji v kladných mocninách konstantní člen 0.
Obě řady mají různé významy a různé analytické oblasti.

Citovaný článek je
[Knuth, Bracket notation for the coefficient-of operator](https://arxiv.org/abs/math/9402216),
nikoli jeho dřívější *Two Notes on Notation*. Relevantní
originální strany 1, 4, 5 byly zobrazeny; text stran 1–6
byl přečten. Potvrzují definici, obor formálních Laurentových
řad a nutnost zachovat oblast rozvoje. Vlastní příklady
a důkazy (K9) výše splňují otevřeně formulované zadání
„explore“; nejde o audit všech výsledků navazujícího článku.
