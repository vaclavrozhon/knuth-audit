# §1.2.9-23: Carlitzovy konečné a nekonečné cyklické součty

Audit 1. listopadu 2026. Zadání s. 96 a úplná odpověď
s. 498–499 zobrazeny. Níže je vlastní obecný důkaz všech
matematických tvrzení odpovědi, včetně dodatku s nekonečnou
řadou. Polynom znamená konečný součet monomů v komutujících
proměnných; všechny konečné identity tedy platí i při nulových
nebo záporných hodnotách proměnných. Binomické číslo binom(a,b)
pro celé a>=0 je nula, pokud b není mezi 0 a a.

## 23(a): otevřený řetězec

Pro m>=1 a celá n>=r>=0 označme

```text
T_m(n,r)=sum_{k_1,...,k_m>=0}
  binom(r,n-k_1) product_{i=1}^{m-1}binom(k_i,n-k_(i+1))
  product_{i=1}^m z_i^k_i.                             (C1)
```

Všechny nenulové členy mají k_i<=n, neboť k_i>n by
vynulovalo předchozí binomické číslo. Definujme f_m,g_m
rekurencemi pro m>=1

```text
f_m=z_m f_(m-1)+z_(m-1) f_(m-2),
g_m=z_m g_(m-1)+z_(m-1) g_(m-2),
f_(-1)=0, f_0=g_(-1)=g_0=z_0=1.                       (C2)
```

Hledaná identita je `T_m(n,r)=f_m^(n-r)g_m^r`.
Pro m=1 plyne z binomické věty: f_1=z_1,g_1=1+z_1.
Při připojení posledního indexu se použije přesný součet

```text
sum_{k=0}^n binom(j,n-k)z^k=z^(n-j)(1+z)^j,
                                                   0<=j<=n. (C3)
```

Proto T_(m+1) vznikne z T_m násobením z_(m+1)^n a
nahrazením z_m výrazem z_m(1+1/z_(m+1)). Stejnou substituci
splňují f,g s předfaktorem z_(m+1); z jejich linearity
v poslední proměnné a (C2) to plyne indukcí. Po rozdělení
předfaktoru na mocniny n-r a r dostáváme tvrzení. Mezivýpočet
s inverzemi se dělá pro nenulové proměnné; výsledná identita
polynomů tím platí všude.

Polynom g_m má také jednoduchý význam: z produktu z_1...z_m
vyškrtneme libovolnou množinu indexů, která neobsahuje dva
sousední indexy, a sečteme zbývající monomy. Rozlišení,
zda poslední index vyškrtneme, dává (C2). Pro f_m navíc
nesmíme vyškrtnout index 1. Počet monomů v g_m je F_(m+2),
kde F_0=0,F_1=1,F_(j+1)=F_j+F_(j-1): podmnožiny cesty
splňují stejnou rekurenci a mají počty 1,2 pro délky 0,1.

Poměr g_m/f_m je řetězový zlomek v odpovědi. Z podmnožin
máme f_m=z_1 g_(m-1)(z_2,...,z_m) a pro m>=2
`g_m=f_m+z_2 g_(m-2)(z_3,...,z_m)`. Tedy poměr R_m=g_m/f_m
splňuje `R_m=1+z_1^(-1)/R_(m-1)(z_2,...,z_m)`,
s R_1=1+z_1^(-1). Iterace přesně dává uvedený zlomek.
Jde o identitu racionálních funkcí tam, kde jsou všechny
jmenovatele nenulové; polynomy f_m,g_m platí bez omezení.

## 23(b): uzavření řetězce a jeho generující funkce

Nechť Z=z_1...z_m a

```text
S_n=sum_{k_1,...,k_m>=0}
       product_{i=1}^m binom(k_i,n-k_(i+1)) z_i^k_i,
                      k_(m+1)=k_1.                    (C4)
h_m=z_m g_(m-1)+z_(m-1) f_(m-2).                       (C5)
```

Hodnota h_m je součet monomů po vyškrtnutí cyklicky
nesousedních indexů: je-li index m zachován, dostaneme první
člen (C5); jinak musejí zůstat 1 i m-1, což dává druhý.
Pro m=1 se jediný index považuje za sousední sám se sebou,
a proto h_1=z_1. Pro m=2 je h_2=z_1z_2+z_1+z_2.

Z (C1) uzavřeme řetězec extrakcí pomocného koeficientu:
`S_n=[w^n]sum_{r=0}^n z_m^r w^(n-r) f_m(z_1,...,z_(m-1),w)^(n-r)
g_m(z_1,...,z_(m-1),w)^r`. Rozvinutí obou posledních
lineárních faktorů a výběr stupně n dává

```text
S_n=sum_{0<=s<=r<=n} binom(r,s)binom(n-r,s)
                a^(r-s)b^s c^s d^(n-r-s),              (C6)
a=z_m g_(m-1), b=z_(m-1)g_(m-2),
c=z_m f_(m-1), d=z_(m-1)f_(m-2).
```

Položme i=r-s,j=n-r-s. Součet přes i,j>=0 využije
`sum_i binom(i+s,s)(at)^i=(1-at)^(-s-1)` a pak geometrickou
řadu přes s. Výsledkem je

```text
sum_{n>=0}S_n t^n = 1/((1-at)(1-dt)-bc t^2)
                  =1/(1-h_m t+(-1)^m Z t^2).           (C7)
```

Pro poslední rovnost je třeba a+d=h_m a ad-bc=(-1)^m Z.
První je definice (C5). Druhá plyne z determinantu níže;
také přímo rozdíl `g_j f_(j-1)-f_j g_(j-1)` podle (C2)
mění znaménko a násobí se z_(j-1).

Pro kořeny rho,sigma rovnice `lambda^2-h_m lambda+(-1)^m Z=0`
je (C7) rovno `1/((1-rho t)(1-sigma t))`. Tedy

```text
S_n=sum_{j=0}^n rho^(n-j)sigma^j
   =(rho^(n+1)-sigma^(n+1))/(rho-sigma)  if rho!=sigma;
S_n=(n+1)rho^n                             if rho=sigma. (C8)
```

Druhá řádka je odstranění zdánlivé singularity, nikoli
nový nález: první řádka je polynom a tuto hodnotu určuje.
Počáteční hodnoty jsou S_0=1,S_1=h_m a rekurence
`S_n=h_m S_(n-1)-(-1)^m Z S_(n-2)` pro n>=2.

## 23(c): stejné proměnné a charakteristický polynom

Zaveďme matici `M(z)=[[z,1],[z,0]]` a produkt
`P_m=M(z_m)...M(z_1)`. Násobení a (C2) dávají

```text
P_m=[[f_m,                g_m-f_m],
     [z_m f_(m-1),        z_m(g_(m-1)-f_(m-1))]].       (C9)
```

Stopa (součet diagonálních prvků) je h_m a determinant
je (-1)^m Z. Také determinant [[a,b],[c,d]] v (C6) má
stejnou hodnotu podle (C2). Při všech z_i=z je P_m=M(z)^m;
jeho vlastní čísla jsou rho_1^m,sigma_1^m, kde
`rho_1,sigma_1=(z +/- sqrt(z^2+4z))/2`. Dosazení do (C8)
je hledaný vzorec; případ shodných mocnin se opět vyhodnotí
polynomiální první řádkou, i když rho_1!=sigma_1.

Dodatek o n x n matici `A_ij=binom(i,n-1-j)`, 0<=i,j<n,
má následující nezávislý důkaz. Na homogenních polynomech
stupně d=n-1 ve dvou proměnných působí lineární zobrazení
`Tf(X,Y)=f(Y,X+Y)`. V bázi `X^(d-i)Y^i` je jeho matice
transponovaná A, protože rozvoj `Y^(d-i)(X+Y)^i` dává
koeficient binom(i,d-j) u X^(d-j)Y^j. Základní substituce
(X,Y)->(Y,X+Y) má různá vlastní čísla
phi=(1+sqrt(5))/2 a psi=(1-sqrt(5))/2. Součiny vlastních
lineárních forem tudíž dávají vlastní čísla T
`phi^(d-j)psi^j`, 0<=j<=d, a tvoří bázi. Proto

```text
det(xI-A)=product_{j=0}^{n-1}(x-phi^(n-1-j)psi^j).     (C10)
```

Identita (B3) v `fibonomial.md` převádí tento produkt na
knižní fibonomické koeficienty se znaménkem
`(-1)^ceil((n-k)/2)` u x^k. Tím je dodatek pro všechna
n>=1 dokázán; n=0 má prázdný determinant 1.

## Nekonečná cyklická řada: vlastní důkaz

Zbývající tvrzení v odpovědi se týká formální řady

```text
B(z_1,...,z_m)=sum_{k_1,...,k_m>=0}
                 product_i binom(k_i+k_(i+1),k_i)z_i^k_i,
                 k_(m+1)=k_1.                         (C11)
```

Nechť I běží přes cyklicky nesousední podmnožiny jako
v (C5), včetně prázdné, a položme

```text
D=sum_I (-1)^|I| product_{i in I} z_i
 =(-1)^m Z h_m(-1/z_1,...,-1/z_m).                    (C12)
```

Pravá strana se po roznásobení stane polynomem; při z_i=0
ji tak i vyhodnocujeme. Dokážeme

```text
B=(D^2-4Z)^(-1/2),                                    (C13)
```

s odmocninou mající konstantní člen +1. To je přesně
vzorec s. 499, protože čtverec odstraní znaménko (-1)^m.

Pro m proměnných u_i definujme
`Phi_i(u)=(1+u_i)(1+u_(i-1))`, indexy cyklicky, a jediné
formální řešení `u_i=z_i Phi_i(u)` s u_i(0)=0. Existuje
rekurzí podle celkového stupně: stupeň d na pravé straně
používá jen stupně <d. V okolí nuly je řešení také analytické,
protože lineární část implicitní rovnice je jednotková matice.
Označme

```text
J=det(delta_ij-z_i (partial Phi_i/partial u_j)),         (C14)
```

vyhodnoceno v tomto řešení. J je determinant příslušné
derivační matice, tedy Jacobián až na diagonální faktory.
Vícenásobný Cauchyho vzorec a substituce z_i=u_i/Phi_i(u)
dávají pro každý nezáporný vektor k

```text
[z_1^k_1...z_m^k_m](1/J)
  =[u_1^k_1...u_m^k_m] product_i Phi_i(u)^k_i
  =product_i binom(k_i+k_(i+1),k_i).                  (C15)
```

Podrobnost substituce: determinant dz/du je
`J/product_i Phi_i`. V integrandu `J^(-1) product z_i^(-k_i-1) dz`
se J vykrátí a zůstanou faktory
`product u_i^(-k_i-1) Phi_i^k_i du`. Substituce je lokálně
invertibilní, zachovává jednotlivé souřadnicové hyperroviny
a má lineární část identitu. Malý integrační torus se tedy
deformuje bez překročení pólů; Cauchyho koeficient se zachová.
Toto zároveň poskytuje formální koeficientový důkaz (C15),
protože každý dotčený koeficient závisí na konečném počtu členů.
Mocnina (1+u_i) na pravé straně má exponent k_i+k_(i+1),
což dokazuje poslední rovnost. Z (C15) máme B=1/J.

Zbývá vyčíslit J. Položme `t_i=u_i/(1+u_i)` a `q_i=1-t_i`.
Z implicitních rovnic plyne `t_i=z_i/q_(i-1)` a
`q_i=1-z_i/q_(i-1)`. Matice v (C14) má diagonálu q_i
a jedinou další nenulovou cyklickou diagonálu
`-t_i q_(i-1)/q_i`. Proto pro m>=2

```text
J=product q_i-product t_i=P-Z/P,    P=product q_i.      (C16)
```

Determinant má pouze dvě nenulové permutační volby: identitu
a celý cyklus. Pro m=1 se oba derivační příspěvky sečtou
na téže diagonále a J=1-2t_1=q_1-t_1, takže (C16) platí také.

Matice `N_i=[[1,-z_i],[1,0]]` splňuje
`N_i(q_(i-1),1)^T=q_(i-1)(q_i,1)^T`. Produkt N_m...N_1
má tedy vlastní číslo P, determinant Z a stopu D.
Poslední tvrzení lze vidět přímo v rozvoji stopy: nenulové
uzavřené přechody mezi dvěma stavy používají člen -z_i jen
na cyklicky nesousedních indexech, čímž vznikne (C12).
Platí to i pro m=1,2, kde stopy jsou 1 a 1-z_1-z_2.
Z charakteristické rovnice dostáváme `P+Z/P=D`.
Čtverec (C16) je tedy D^2-4Z. J má konstantní člen 1,
což určuje správnou větev odmocniny a dokončuje (C13).

## Zdroje a meze kontroly

Knižní svazek časopisu 27 byl již roku 2021 opraven na 17.
Bibliografický záznam je potvrzen katalogem vydavatele přes
Dialnet; přímé stažení článku *Multiple sums and generating
functions*, Collectanea Math. 17 (1965), 281–296 z RACO
vrátilo HTTP 403. Obsah tohoto článku zatím nebyl přečten;
vlastní důkazy výše tento nedostatek nezakrývají. Historická
část úlohy proto ještě není úplně uzavřena.

Samostatný primární článek
[Carlitz, The characteristic polynomial of a certain matrix of binomial coefficients](https://www.fq.math.ca/Scanned/3-2/carlitz.pdf),
Fibonacci Quarterly 3 (1965), 81–89, byl získán. Zobrazeny
byly s. 81–83 a 88–89: tvrzení, metoda přes stopy, převod
pomocí q-binomické věty a závěrečné poznámky. Potvrzuje
(C10) i fibonomický rozvoj; na s. 81 Carlitz připisuje
původní sdělení tohoto výsledku Hoggattovi. Tím netvrdíme,
že byl přečten jiný, výše citovaný článek z Collectanea.

`check_carlitz.py` prošel jednou: 9657 kontrol a porovnaných
koeficientů. Obsahuje všechny koeficienty konečných sum
pro m<=5,n<=4, nekonečnou řadu do celkového stupně 6 pro
m<=7 a skutečné charakteristické polynomy matic velikosti
1–16. Obecné důkazy zůstávají hlavním podkladem.
