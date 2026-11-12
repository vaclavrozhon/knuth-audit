# §4.5.3-16: analytické rozvoje tanh a exponenciály

Zadání 375–376 a odpověď 649–651 byly vizuálně přečteny.
C(a_1,...,a_k)=1/(a_1+1/(...+1/a_k)) je řetězový zlomek;
jeho čitatel a jmenovatel vyjadřují continuanty K z
`euclid-basic.md`. Níže se rozlišují identity konečných
polynomů, konvergence nekonečných rozvojů a numerické kontroly.
Historické atribuce Euler/Cotes/Davis patří do kontextového bloku.

## Od diferenciální rovnice k lokálním rozvojům

Začněme f_0(z)=tanh(z) a definujme
f_(n+1)(z)=1/f_n(z)-(2n+1)/z. Indukcí platí

```text
f_n'(z)=1-f_n(z)^2-2n f_n(z)/z,
f_n(z)=z/(2n+1)-z^3/((2n+1)^2(2n+3))+O(z^5).         (1)
```

Funkce f_n je přitom lichá a analytická v okolí nuly.
Pro n=0 jde o běžnou derivaci tanh. Je-li (1) známo pro n,
jednoduchá nula f_n v počátku dává
1/f_n=(2n+1)/z+z/(2n+3)+O(z^3); odečtení pólového členu
tedy vytvoří analytickou lichou f_(n+1). Diferencování definice
a dosazení (1) dává stejnou rovnici s n+1. Její lineární
a kubický koeficient určují další tvar (1).

Přesné koeficienty zapišme jako
f_n(z)=sum(k>=0)(-1)^k c_(n,k) z^(2k+1). Rovnice (1) dává

```text
c_(n,0)=1/(2n+1),
c_(n,k)=sum(i=0..k-1)c_(n,i)c_(n,k-1-i)/(2n+2k+1).    (2)
```

Všechny c jsou kladné. Indukce v k ukazuje, že mají přesně
tištěný tvar součtu zlomků s kladnými celočíselnými čitateli
a jmenovateli (2n+1)^(k+1) krát k faktorů 2n+b, kde b jsou
kladná celá čísla nezávislá na n. Odtud i monotónnost v n.
Pro k=3 vycházejí oba tištěné sčítance koeficientu -a_(n,7).

Silnější jednoduchý odhad z (2) je

```text
c_(n,k) <= c_(0,k)/(2n+1)^(k+1),
|f_n(z)| <= tan(|z|/sqrt(2n+1))/sqrt(2n+1).            (3)
```

Při indukci stačí použít 2n+2k+1>=2k+1. Proto mocninná řada
konverguje alespoň pro |z|<pi*sqrt(2n+1)/2, právě jak tvrdí
odpověď. V menším kruhu |z|<pi/2 také |f_n(z)|<=tan|z|.
Tento argument skutečně dokazuje rostoucí kruhy analyticity;
nejde jen o formální manipulaci s koeficienty.

## Polynomové identity a přesný zbytek

Pro n>=0 definujme

```text
A_n(z)=n! sum(k=0..n) binom(2n-k,n) z^k/k!
      =sum(k=0..n) (n+k)! z^(n-k)/(k!(n-k)!).           (4)
```

Máme A_0=1, A_1=z+2. Porovnáním koeficientů pro n>=1 dostaneme

```text
A_(n+1)(z)=(4n+2)A_n(z)+z^2 A_(n-1)(z).              (5)
```

Koeficientový výpočet v odpovědi odpovídá rozkladu
(n+k)(n+k+1)=(4n+2)k+(n+1-k)(n-k), včetně krajních členů.
Stejná rekurze continuantů a počáteční hodnoty dávají

```text
K_n(1/z,3/z,...,(2n-1)/z)
    =(A_n(2z)+A_n(-2z))/(2^(n+1) z^n),
K_(n-1)(3/z,...,(2n-1)/z)
    =(A_n(2z)-A_n(-2z))/(2^(n+1) z^n).                (6)
```

Pro konečný konvergent T_n(z)=C(1/z,3/z,...,(2n-1)/z)
tedy platí podíl liché a sudé části A_n z (6).

Zobecněný binomický koeficient zde znamená
binom(t,n)=t(t-1)...(t-n+1)/n!, i pro záporné celé t.
Koeficienty exponenciálního součinu určuje identita

```text
sum(k=0..n)(-1)^k binom(m,k)binom(2n-k,n)
    =binom(2n-m,n),
[z^m](exp(z) A_n(-z))=n! binom(2n-m,n)/m!.            (7)
```

První rovnost pro m=0,...,n plyne binomickým rozvojem;
obě strany jsou polynomy v m stupně nejvýše n, a proto
platí pro každé m. Pro n<m<=2n je pravá strana nula.
Pro m=2n+1+k použijeme binom(-k-1,n)=(-1)^n binom(n+k,n).
Tím dostáváme přesný zbytek

```text
R_n(z)=exp(z)A_n(-z)-A_n(z)
      =(-1)^n z^(2n+1)
        *sum(k>=0)(n+k)! z^k/((2n+k+1)! k!).           (8)
tanh(z)-T_n(z)=2R_n(2z)/
        ((A_n(2z)+A_n(-2z))*(exp(2z)+1)).              (9)
```

Rovnice (9) plyne pouhým společným jmenovatelem; koeficient 2
i argument 2z jsou správné.

Pro |2z|<=1 máme |R_n(2z)|<=e*n!/(2n+1)!, protože
(n+k)!/(2n+k+1)! klesá s k. Dále

```text
|A_n(2z)+A_n(-2z)|/2 >= (2/3)*(2n)!/n!.               (10)
```

Poměr binom(2n-2j,n)/binom(2n,n) je nejvýše 4^(-j);
trojúhelníková nerovnost pro sudé koeficienty a součet
geometrické řady dávají (10). Faktor exp(2z)+1 je zde
oddělen od nuly: jeho reálná část je alespoň 1+exp(-1)cos(1).
Tištěná rychlá konvergence v malém kruhu je tedy rigorózní.

## Konvergence v celé komplexní rovině

Pro přehledný globální důkaz normalizujme
B_n(z)=A_n(z)/A_n(0). Koeficient z^j/j! v B_n je

```text
r_(n,j)=product(i=0..j-1)(n-i)/(2n-i), 0<=j<=n;
0<=r_(n,j)<=2^(-j),  r_(n,j)->2^(-j) pro pevné j.     (11)
```

Odhad exponenciální řadou umožňuje limitu vzít uniformně na
každé kompaktní množině: B_n(z)->exp(z/2). Z (6) vyplývá

```text
T_n(z) -> (exp(z)-exp(-z))/(exp(z)+exp(-z))=tanh(z).    (12)
```

Konvergence je lokálně uniformní mimo nuly cosh(z). V těchto
izolovaných bodech, tedy pólech tanh, jmenovatel jde k nule
a čitatel k nenulové hodnotě, takže hodnoty směřují k nekonečnu
v rozšířené komplexní rovině. Tvrzení o celé rovině je tak
platné v obvyklém meromorfním smyslu: funkce jsou analytické
mimo izolované póly. V z=0 se konečné racionální funkce
vykládají po odstranění zdánlivého singularitního zápisu 1/z.

## Známé opravy z roku 2006

Hypergeometrický zápis používá rostoucí součin
(a)_k=a(a+1)...(a+k-1) a
2F0(a,b;;t)=sum(k>=0)(a)_k(b)_k t^k/k!.
Při b=-n je řada konečná. Z (4) vyjde

```text
A_n(z)=z^n 2F0(n+1,-n;;-1/z),                         (13)
```

bez nadbytečného n! z prvního dotisku. Druhá známá oprava
doplňuje m! ve jmenovateli levé sumy odpovídající (7).
Obě opravy z 12. ledna 2006 jsou potřebné a dostačující.
Například n=2,z=1 dává A_2=19, kdežto chybný faktor n!
by dal 38. Pro n=1 má exp(z)(2-z) koeficient z^3 rovný
-1/6; vynechané m! by z něj udělalo -1. Nové vysvětlení
symbolu 2F0 z roku 2024 je konzistentní. Bibliografická
oprava Davisova svazku z roku 2026 je v kontextové frontě.

## Pravidelné rozvoje exponenciály

Nechť M(a)=[[a,1],[1,0]], P je součin těchto matic a
S=[[1,1],[1,-1]]. Z již dokázaného tanh rozvoje plyne
coth(z)=[1/z;3/z,5/z,...]. Zobrazení u->(u-1)/(u+1)
je matice M(0)S a dává exp(-2z). Dvě obecné identity jsou

```text
S M(2r) = P(1,r-1,1) S,
S P(2u+1,b,2v+1) = P(1,u,2b,v,1) S.                  (14)
```

Lze je ověřit přímo čtyřmi maticovými koeficienty. První,
s r=(2m+1)n a z=1/(2n), dává pro celé n>=1 opakované
trojice (1,(2m+1)n-1,1), m=0,1,..., v rozvoji exp(-1/n).
To je přesně zadání 376. Pro n=1 obsahuje první trojice
nulu; sloučení sousedů ji odstraní a převrácení dává obvyklý
rozvoj e ze vzorce (13) hlavního textu.

Je-li n kladné liché, položme h=floor(n/2). Druhá identita
(14), s u=3mn+h, b=(6m+3)n a v=(3m+2)n+h, sdružuje
vstupní trojice ((6m+1)n,(6m+3)n,(6m+5)n). Pro z=1/n
z ní dostáváme opakované pětice

```text
(1,3mn+h,(12m+6)n,(3m+2)n+h,1), m=0,1,...,            (15)
```

v rozvoji exp(-2/n). Souhlasí i obě tištěné podlahy v 651.
Při n=1 se opět odstraní první nula; začátek je C(7,2,1,...).
Pro dostatečně pozdní vstupní ocas y>1 je S(y)=(y+1)/(y-1)>1.
Zmenšování kladných válcových intervalů proto ospravedlňuje
přechod maticových identit k nekonečnému rozvoji.

## Reprodukovatelné kontroly

`verify_euclid_analytic.py` ověřil 160 polynomových identit,
3680 exponenciálních koeficientů, 550 Riccatiho koeficientů
a 504 identit převrácení. Dalších 48 komplexních případů
ověřilo přesný zbytek (včetně bodu blízko pólu), 12 malé
kruhové meze a 51 případů nezávislé poměry hypergeometrických
funkcí a diferenciální rovnici; numerika používá 160 míst.
Tyto numerické kontroly nenahrazují důkazy (1)–(15).

Celkem 1800 prefixů exponenciálních rozvojů je certifikováno
přesnými racionálními Taylorovými mezemi. Pro kladné x
se zbytek za N-tým členem exp(x) sevře geometricky poměrem
x/(N+2); převrácení mezí dá exp(-x). Kontrola zahrnuje obě
rodiny, n=1 a sloučení nul. Čtyři checkpointy celého bloku
16–18 prošly, relace 65693, PID 1174387, limit 300 sekund,
exit 0. Stav 16 je `known_erratum`; žádný nový nález.
