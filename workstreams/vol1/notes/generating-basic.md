# §1.2.9: základní operace s generujícími funkcemi

Audit 1. listopadu 2026. Zobrazeny originály s. 87–96 a 496–499
(strany souboru vždy o 15 vyšší). Zde jsou obecné matematické
důkazy hlavního textu a úloh 1–6, 12, 14, 17, 20. Historické
atribuce a některé odkazy mají samostatný, dosud částečný záznam.

## Formální a analytický význam

Koeficientový zápis `[z^n]G(z)=a_n` vybírá n-tý člen řady
`G(z)=sum_{n>=0}a_n z^n`. Formální mocninná řada nad Q nebo C
je tato posloupnost koeficientů; součet a součin se definují
konečně po každém koeficientu. Analytická mocninná řada navíc
označuje součet číselné řady v bodech, kde konverguje.

Konverguje-li G(z_0) pro z_0!=0, jsou členy a_n z_0^n omezené
nějakým M. Pro |z|<|z_0| tedy `|a_n z^n|<=M(|z|/|z_0|)^n`;
geometrická majoranta dokazuje absolutní konvergenci a stejnoměrnou
konvergenci na každém menším uzavřeném kruhu. Pro n>=1 je
`|a_n|^(1/n)<=max(1,M)/|z_0|`. Obráceně, je-li posloupnost
n-tých odmocnin omezená B, řada konverguje absolutně pro |z|B<1.
Případ B=0 znamená a_n=0 pro n>=1. To dokazuje oba body s. 87;
a_0 se do n-té odmocniny při n=0 vůbec nezahrnuje.

Poloměr konvergence R je supremum poloměrů těchto otevřených
kruhů. Všechny analytické operace níže se provádějí uvnitř R
(u součinu uvnitř obou poloměrů). Formální verze takovou podmínku
nepotřebují. Nekonečný součin je formálně dovolen, přispívá-li
do každého stupně jen konečně mnoho netriviálních faktorů,
např. faktory `1+O(z^j)` pro j rostoucí do nekonečna. Knižní
dodatek „whenever this is meaningful“ u (9) tuto podmínku nezahazuje.

## Operace (2)–(18)

Linearita (2) je po koeficientech. Pro celé m>=0 posun (3)
plyne z `[z^n]z^mG=a_(n-m)` při konvenci a_j=0 pro j<0.
Odstranění prvních m členů a vydělení z^m dává (4).

V součinu `G(z)H(z)` je koeficient z^n roven konečnému součtu
`sum_{k=0}^n a_k b_(n-k)`: to je (6). Zvláštní případy jsou
geometrická řada (5), kumulativní součty (7) a více faktorů
(8)–(9). Konstantní člen chybně vysázený jako a_0+b_0 na s. 88
má známou opravu na a_0 b_0 z 27. února 1998.

Pro exponenciální generující funkce, které ukládají a_n jako
koeficient z^n/n!, je po vynásobení koeficientu z^n číslem n!

```text
n! sum_{k=0}^n (a_k/k!)(b_(n-k)/(n-k)!)
  =sum_{k=0}^n binom(n,k)a_k b_(n-k).                   (G1)
```

Tím jsou (10)–(11) i úloha 2 dokázány. Dosazení cz násobí a_n
číslem c^n. U (12) parita rozhoduje, zda 1+(-1)^n nebo
1-(-1)^n vynuluje koeficient.

Pro celé m>=1, 0<=r<m a `omega=exp(2 pi i/m)` máme

```text
(1/m) sum_{j=0}^{m-1} omega^(j(n-r)) = [n mod m=r].     (G2)
```

Je-li omega^(n-r)!=1, konečná geometrická řada je nula;
jinak je součet m. Dosazení do G dává filtr (13) a úlohu 14.
V analytickém případě mají všechny omega^j z stejnou velikost,
tedy leží společně uvnitř R. Známý dodatek n>=0 z roku 2007
opravuje chybějící dolní mez vlevo; záporné koeficienty nevznikají.

Formální derivace násobí a_(k+1) číslem k+1 a integrace dělí
a_(k-1) číslem k, takže (14)–(15) platí přímo; integrační
konstanta je 0. Dolní mez v (15) je k>=1 podle opravy 1998.
Operátor `z d/dz` násobí n-tý koeficient číslem n, a proto
jeho polynomy realizují násobení libovolným polynomem v n.
Analytická legitimita plyne z geometrické majoranty na menším
kruhu i po vynásobení členů pevnou mocninou n.

Derivace a integrace geometrické řady dávají (16) a
`L(z)=log(1/(1-z))=sum_{n>=1}z^n/n`, tedy (17).
Definujeme `H_n=sum_{j=1}^n 1/j`, H_0=0. Součin s 1/(1-z)
dává `G_H(z)=L(z)/(1-z)`, rovnici (18).

U lineární rekurence `a_n=sum_{j=1}^m c_j a_(n-j)` pro n>=m
má `(1-sum c_j z^j)G(z)` nulové koeficienty od stupně m,
takže je polynomem. Tvrzení o racionální funkci na s. 88 je
tím dokázáno včetně počátečních podmínek.

## Tabulka (19)–(30)

Značíme `binom(r,k)=r(r-1)...(r-k+1)/k!` pro k>=0,
`S(k,n)` počet rozkladů k-prvkové množiny na n neprázdných
bloků a `c(k,n)` počet permutací k prvků s n cykly.
Obě Stirlingovy posloupnosti mají počáteční hodnotu (0,0)=1
a hodnotu 0 mimo 0<=n<=k. Z předchozího bloku máme jejich
rekurence a polynomiální identity; viz `stirling-identities.md`.

Binomická věta (19) plyne z řešení `(1+z)F'=rF`, F(0)=1:
koeficienty splňují `(k+1)a_(k+1)=(r-k)a_k`. Volba r=-n-1
a z->-z dává (20). V (21) se položí y=x-1, a pak
`y=z(1+y)^(-t)`. Lagrangeova koeficientová formule dává pro k>=1

```text
[z^k]x^r = (r/k)[u^(k-1)](1+u)^(r-1-kt)
         = (r/k)binom(r-1-kt,k-1).                    (G3)
```

To je polynomiální význam knižního výrazu
`r binom(r-kt,k)/(r-kt)` i při odstranitelném nulovém jmenovateli.
Konstantní člen je 1. Důkaz použité Lagrangeovy formule a této
identity je již v `binomial-exercises.md`, úloha 1.2.6-25.
Při t=0 dostáváme (19), jak žádá úloha 4.

Exponenciální řada (22) je určena F'=F, F(0)=1. Položme
`E_n(z)=(exp z-1)^n`. Platí `E_n'=n(E_(n-1)+E_n)` a E_0=1.
Pro koeficienty ve tvaru z^k/k! to dává přesně rekurenci
Stirlingových čísel druhého druhu, tedy

```text
(exp z-1)^n = n! sum_{k>=0} S(k,n) z^k/k!.              (G4)
```

Jiný indukční krok: součin E_(n-1)(exp z-1) má koeficient
`(n-1)!/k! sum_{0<=j<k} binom(k,j) S(j,n-1)`.
Součet je n S(k,n), neboť vyznačíme jeden z n bloků rozkladu.
První dotisk v odpovědi 5 opomíjí faktor 1/k!; jde o opravu 2006.

Logaritmus (24) je integrál 1/(1+z). Parametrická derivace
`(1-z)^(-m-1)=sum_{k>=0}binom(m+k,k)z^k` podle m dává (25):
derivace polynomu v m je při celém m>=0
`binom(m+k,k)(H_(m+k)-H_m)`. Přesněji nejprve derivujeme
identitu s komplexním parametrem v okolí m; koeficientová
rovnost je polynomiální. Pro k=0 je derivace 0.

Pro (26) vezmeme `L(z)^n/n!`. Derivace je
`L(z)^(n-1)/((n-1)!(1-z))`. Alternativně koeficienty v
`exp(w L(z))=(1-z)^(-w)` určuje stoupající faktoriál
`w(w+1)...(w+k-1)=sum_n c(k,n)w^n`; tím přímo dostáváme

```text
L(z)^n = n! sum_{k>=0}c(k,n)z^k/k!.                    (G5)
```

Současně je tím dokázána úloha 17: koeficient z^k w^n
je c(k,n)/k!. Všechny indexy jsou nezáporné; oprava 2023
doplňuje k>=0 v odpovědi.

Rovnice (27) je právě stoupající faktoriál. Z rekurence
`S(k,n)=nS(k-1,n)+S(k-1,n-1)` plyne pro pevné n>=0

```text
sum_{k>=0} S(k,n)z^k = z^n/product_{j=1}^n(1-jz),       (G6)
```

což je (28), s prázdným součinem 1 pro n=0.

V (29) první dotisk užívá Bernoulliho čísla s B_1=-1/2.
Oprava z 21. března 2021 přešla na konvenci B_1=+1/2:
`z/(1-exp(-z))=sum B_k z^k/k!`. Obě řady se liší pouze
členem z, neboť `z/(1-exp(-z))=z+z/(exp z-1)`.
Srovnání s tabulkou a §1.2.11.2 musí respektovat tuto změnu.
Zde je zkontrolována identita a první členy, nikoli celý
dosud nenavštívený výklad §1.2.11.2 a tabulka v příloze.

V (30) položíme y=log x, takže `y=z exp(ty)`. Tatáž
Lagrangeova formule dává pro k>=1

```text
[z^k]x^r = (r/k)[u^(k-1)]exp((r+kt)u)
         = r(r+kt)^(k-1)/k!.                           (G7)
```

Konstantní člen je 1; zápis k=0 v součtu je této hodnotě
podřízen a nevyžaduje dělit nulou při r=0. Rovnice pro y
určuje jediné formální řešení y(0)=0; analyticky existuje
v okolí nuly podle nenulové derivace implicitní rovnice.
Odkazy na §2.3.4.4-29 a §4.7-22 jsou evidovány odděleně.

## Extrakce koeficientu a drobné úlohy

Cauchyho vzorec (32) pro 0<rho<R je
`a_n=(1/(2 pi i)) integral_|z|=rho G(z)/z^(n+1) dz`,
s kladnou orientací kružnice. Stejnoměrná absolutní konvergence
na kružnici dovoluje integrovat po členech. Parametrizace
z=rho exp(it), -pi<=t<=pi, vynuluje všechny mocniny kromě
z^(-1), jejíž integrál je 2 pi i. To dokazuje tvrzení
bez odkazu na asymptotické aproximace.

Úloha 1 je součet dvou geometrických řad
`1/(1-2z)+1/(1-3z)`, koeficienty 2^n+3^n.
Úloha 3: z rovnice
`G_H'=L/(1-z)^2+1/(1-z)^2` porovnáním z^(n-1) dostáváme
`nH_n=sum_{k=0}^{n-1}H_k+n`, tedy známý součet harmonických čísel.
Úloha 6: konvoluce `sum_{k=1}^{n-1}1/(k(n-k))` je koeficient
L^2. Protože `(L^2)'=2G_H`, vyjde `2H_(n-1)/n` pro n>=1;
pro n=0 je prázdný součet 0, bez dělení nulou.

Úloha 12: dvourozměrná řada je `sum a_mn w^m z^n`.
Pro a_mn=binom(n,m) je po vnitřním konečném součtu
`sum_n z^n(1+w)^n=1/(1-z-wz)`. Formálně jsou všechny
koeficienty jednoznačné, analyticky lze např. vyžadovat
|z|(1+|w|)<1 pro absolutní konvergenci dvojité řady.

Úloha 20: z rozkladu mocnin
`n^m=sum_k S(m,k)n(n-1)...(n-k+1)` a z (20) dostáváme
`sum_n n^m z^n=sum_k k!S(m,k) z^k/(1-z)^(k+1)`.
Proto c_mk=k!S(m,k), včetně m=0 s konvencí 0^0=1.
