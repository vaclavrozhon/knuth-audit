# §4.5.3-35: vážené reprezentace a odečítací algoritmus

Audit 2026-11-03. Zadání na straně378 a odpověď na653–654
byly přečteny v původním skenu. Hlavní identita i asymptotika
jsou správné; níže je úplný důkaz s rovnoměrnými odhady.
Dodatečná experimentální formule na654 má chybnou slovní
normalizaci, evidovanou samostatně jako V2-C0134. Neprohlašujeme
její případnou normalizovanou verzi za dokázanou.

**Myšlenka.** Každému místu řezu řetězového zlomku přiřadíme
čtveřici z úlohy33. Její váha je příslušný podíl; dodatečný
řez před koncovou jedničkou zachytí poslední podíl minus1.
Po seskupení čtveřic podle dvou souřadnic vzniknou dva
harmonické součty. Jejich logaritmy dají hlavní člen
n(log n)^2. Pomocné prvočíselné součiny se nakonec přesně
vyruší. V oddílu3 je rovnoměrná harmonická mez; oddíly4–5
hlídají součet všech chyb i malé pomocné horní meze.

## 1. Přesná váha a počet odečítání

Pro 0<m<n označme A(m,n) součet podílů kanonického rozvoje
m/n=[0;a_1,...,a_t], kde poslední podíl a_t>=2.
Continuant K je jmenovatel takového zlomku; K prázdného
seznamu je1. Definujme množinu a vážený součet

```
H_n = {(x,x',y,y'): n=xx'+yy', x>y>0, x'>=y'>0,
                        gcd(x,y)=1},
W(n)=sum_(H_n) floor(x/y).                            (S1)
```

Pro m<n/2 má kanonický seznam první i poslední podíl>=2.
Řez za a_j, j<t, dává reprezentaci z euclid-heilbronn.md,
oddíl2. Protože x/y=[a_j;a_(j-1),...,a_1], její váha je a_j.
Nahradíme-li poslední a_t dvojicí a_t-1,1 a provedeme řez
před1, dostaneme x'=y'=gcd(m,n) a váhu a_t-1. Platí to
i pro seznam délky1: pro m<n/2 je pak a_1>=3, takže x>y.
Tento nový řez dává právě všechny hraniční reprezentace.
Jednoznačnost obou kanonických rozvojů v úloze33 dokazuje
bijektivitu. Tedy

```
W(n)=sum_(0<m<n/2) (A(m,n)-1).                        (S2)
```

Označme b(m,n) počet operací „odečti menší číslo od většího“
do okamžiku rovnosti. Každé nefinální dělení s podílem a_i
odpovídá a_i odečtením; poslední odpovídá a_t-1 odečtením.
Proto b(m,n)=A(m,n)-1. Po prvním odečtení začínají dvojice
(m,n) i (n-m,n) stejnou neuspořádanou dvojicí {m,n-m}.
Odtud b(m,n)=b(n-m,n). Prostřední dvojice (n/2,n) má
b=1, pokud n je sudé, zatímco b(n,n)=0. Dostáváme

```
sum_(1<=m<n) A(m,n)=2(W(n)+floor(n/2)),               (S3)
S(n):=(1/n)sum_(1<=m<=n)b(m,n)
     =(2W(n)+1-(n mod 2))/n.                         (S4)
```

Vzorce platí také pro n=1. S(n) je průměrný počet odečtení
do rovnosti, nikoli součet přes všechny zlomky ani počet
odečtení do nulového zbytku. Toto rozlišení je důležité
pro dodatečnou poznámku v odpovědi.

## 2. Seskupení reprezentací

Z řezu kanonických seznamů plyne |H_n|=O(n log n): každý
má O(log n) podílů, neboť každé dva eukleidovské kroky
zmenší kladný zbytek alespoň na polovinu. Pro x'y>=n/2
platí 1<x/y=n/(x'y)-y'/x'<2, takže floor(x/y)=1.
Tyto členy přispějí O(n log n). Ve zbývajících členech
nahradíme floor(x/y) výrazem n/(x'y); jednotlivá chyba
má velikost menší než2.

Pro kladné celé v definujme

```
P(v)=phi(v)/v=product_(p|v)(1-1/p),
P(a\b)=product_(p|a,p does not divide b)(1-1/p).
```

Součiny jsou přes prvočísla p; phi je Eulerova funkce,
počet zbytkových tříd nesoudělných s v. Prázdný součin je1.
Fixujme y,x' s x'y<n/2 a položme d=gcd(y,n). Nutná podmínka
existence je gcd(y,x')=d, protože gcd(x,y)=1. Pišme

```
n=dm, y=dj, x'=dk, gcd(j,m)=gcd(j,k)=1.
```

Rovnice m=xk+jy' má pro 1<=y'<=dk právě d řešení:
y' probíhá jednu třídu modulo k. Podmínka n>2d^2jk
zaručuje x>dj=y u všech těchto řešení. Navíc gcd(x,j)=1.
Při postupném zvyšování y' o k klesá x o j. Každé
prvočíslo p|d, které nedělí j, tedy vyloučí právě podíl
1/p kandidátů. Čínská věta o zbytcích dává přesně
d P(d\j) platných řešení; prvočísla dělící j už x nedělí.

Pro X=n/(2d^2)=m/(2d) proto platí

```
W(n)=sum_(d|n) m sum_(j<X,gcd(j,m)=1) P(d\j)/j
                       sum_(k<X/j,gcd(k,j)=1) 1/k
      +O(n log n).                                  (S5)
```

Všechny indexy j,k jsou kladné. Pro X<=1 je příslušná
suma prázdná. Jde o rovnost konečných racionálních součtů
po náhradě vah, nikoli o pravděpodobnostní aproximaci.

## 3. Rovnoměrná harmonická mez

Definujme H(x)=sum_(1<=k<x)1/k pro x>=1 a H(x)=0 pro
x<1. Integrální srovnání dává 0<=H(x)-ln x<=1 pro x>=1.
Dále H_j(x) omezuje stejný součet na gcd(k,j)=1, opět
s hodnotou0 pro x<=1. Označme A_j množinu kladných čísel,
jejichž všechny prvočinitele dělí j; patří sem1.
Jednoznačný rozklad k=ab, a v A_j, gcd(b,j)=1 dává

```
H(x)=sum_(a in A_j) H_j(x/a)/a,
sum_(a in A_j) 1/a =1/P(j),
sum_(a in A_j) (ln a)/a
   =(1/P(j)) sum_(p|j) (ln p)/(p-1).                 (S6)
```

Poslední dvě identity plynou z konečného součinu
geometrických řad a jejich derivací. Protože všechny
členy první identity jsou nezáporné a H_j(x/a)<=H_j(x),
máme H_j(x)>=P(j)H(x)>=P(j)ln x. Také

```
0<=H_j(x)-H_j(x/a)<=H(x)-H(x/a)<=ln a+1.              (S7)
```

Je-li x/a<1, poslední mez plyne přímo z H(x)<=ln x+1;
jinak z integrálního srovnání harmonického součtu na
intervalu [x/a,x). Sečtení(S7) pomocí(S6) vede k

```
0<=H_j(x)-P(j)ln x<=2+sum_(p|j)(ln p)/(p-1)           (S8)
```

pro všechna j>=1,x>=1, se stejnou konstantou2.
Tento důkaz nepoužívá rozvoj ln(x/d) pro d>=x.

Pišme B(j)=1+sum_(p|j)(ln p)/(p-1) a L(n)=log log(3n).
Pak B(j)=O(log log(3j)). Pro úplnost rozdělme prvočísla
v Y=max(2,ln j): malá přispějí O(ln Y) podle elementární
Chebyshevovy meze dokázané v euclid-heilbronn.md, oddíl6;
velká přispějí nejvýše (2/Y)sum_(p|j)ln p<=2 ln j/Y.
Ve stejné poznámce je dokázána mez

```
sigma_-1(n):=sum_(d|n)1/d=O(L(n)).
```

Dále rozdělením podle prvočísel a součtem konečné
geometrické řady platí

```
sum_(d|n)(ln d)/d
 <=sigma_-1(n) sum_(p|n)(ln p)/(p-1)=O(L(n)^2).        (S9)
```

Zde střední exponent k v řadě sum_(k=0..e)p^-k nepřesáhne
střední exponent nekonečné řady, tedy1/(p-1). Tím je(S9)
odůvodněna i pro prvočíselné mocniny s velkým exponentem.

## 4. Druhý harmonický součet

Použití(S8) v(S5) vytvoří celkovou chybu nejvýše

```
O(L(n) sum_(d|n)(n/d) sum_(j<X)1/j)
   =O(n log n L(n)^2).                               (S10)
```

Identita P(d\j)P(j)=P(d)P(j\d) ponechá hlavní součet
sum_(d|n)m P(d) A_(d,m)(X), kde

```
A_(d,m)(X)=sum_(j<X,gcd(j,m)=1) P(j\d)/j ln(X/j).
```

Möbiova funkce mu(r) je0, obsahuje-li r druhou mocninu
prvočísla, jinak (-1) umocněno na počet prvočinitelů r.
Eulerův součin dává P(j\d)=sum_(r|j,gcd(r,d)=1)mu(r)/r.
Po substituci j=rs a použití dm=n dostaneme

```
A_(d,m)(X)=sum_(r<X,gcd(r,n)=1) mu(r)/r^2 J_m(X/r),
J_m(Y)=sum_(s<Y,gcd(s,m)=1) ln(Y/s)/s
      =integral_(1..Y) H_m(t) dt/t
      =P(m)/2 (ln Y)^2+O(B(m)ln Y),  Y>=1.           (S11)
```

Konstanta posledního O je absolutní podle(S8).
Absolutní konvergence sum 1/r^2 a sum (ln r)/r^2 dovolí
v hlavním členu nahradit (ln(X/r))^2 výrazem (ln X)^2
s chybou O(ln X): pro 1<=r<X je rozdíl nejvýše
2 ln X ln r. Prodloužení sumy r<X na všechna r přidá
O((ln X)^2/X)=O(ln X). Definujeme-li log^+ X=max(0,ln X),
platí proto pro všechna X>0

```
A_(d,m)(X)=P(m)/2 C_n (log^+ X)^2
                         +O(B(m)log^+ X),
C_n=sum_(r>=1,gcd(r,n)=1) mu(r)/r^2
   =(1/zeta(2)) product_(p|n)(1-p^-2)^-1.             (S12)
```

Zeta(2)=sum_(r>=1)r^-2=pi^2/6. Pro X<=1 jsou obě
strany(S12) nulové včetně majoranty chyby. Po vynásobení
mP(d) a sečtení přes d|n je chyba opět O(n log n L(n)^2).

## 5. Vyrušení prvočíselných faktorů

Pro n>=2 a d|n platí

```
0<=log^+(n/(2d^2))<=ln n,
ln n-log^+(n/(2d^2))<=2 ln d+ln 2.
```

Rozdíl čtverců je tedy nejvýše2 ln n(2 ln d+ln2).
Protože C_n<=1 a mP(d)P(m)<=n/d, přispěje nahrazení
všech log^+ výrazů číslem ln n díky(S9) pouze
O(n log n L(n)^2). Zbývá přesná identita

```
sum_(d|n)(n/d)P(d)P(n/d)
       =n product_(p|n)(1-p^-2).                     (S13)
```

Obě strany jsou multiplikativní, tj. rozkládají se na
součin při nesoudělných argumentech. Stačí n=p^e, e>=1.
Oddělení obou krajních členů d=1,p^e a sečtení zbývající
geometrické řady dává přesně p^e(1-p^-2). Platí také
n=1, kdy je na obou stranách1. Vynásobení(S13) číslem
C_n/2 vyruší všechny prvočíselné faktory. Konečný výsledek:

```
W(n)=3/pi^2 n(ln n)^2+O(n log n (log log n)^2),
S(n)=6/pi^2 (ln n)^2+O(log n (log log n)^2).           (S14)
```

Použití log log(3n) v důkazu jen zahrnuje malé vstupy do
kladné majoranty; asymptotika při n->infinity je totožná
s tištěnou. Důkaz(S14) nepoužívá empirickou formuli654.

## 6. Prameny a rozsah kontroly

Zpráva Yao–Knuth STAN-CS-75-510 ze září1975 byla získána
z veřejného archivního skenu; všech11 číslovaných stran
textu bylo přečteno vizuálně (strany5–15 souboru PDF).
Její finální sazba v PNAS72 (1975),4720–4722 nebyla získána.
Metadata, hash a omezení přístupu jsou v
sources/euclid-heilbronn.json. Výše je vlastní podrobnější
důkaz rovnoměrnosti, nikoli přepis zkrácené argumentace
zprávy. Zejména se vyhýbá nahrazení H(x/d) výrazem ln(x/d)
v rozsahu d>=x.

Na straně10 zprávy se opakuje nesprávné připsání skoro
jisté asymptotiky součtu podílů Khinchinovi. Jde o stejnou
matematickou chybu jako V2-C0132, nikoli další nález.
Důkaz(S14) tento závěrečný odstavec nepoužívá.

Všechny čtyři řady all2-prepre, all2-pre, all2 a err2 byly
prohledány. Jediná oprava odpovědi35 je velké „Its“
v názvu časopisu (2003-07-12). Opravy sousedních úloh34,
39 a40 nijak nemění zdejší normalizaci. Původní článek
Pitteway–Castle1988 nebyl získán; aktuální stav jeho
normalizované domněnky tímto auditem není rozhodnut.

Reprodukce konečných kontrol je v verify_euclid_subtractive.py;
výsledky a přesný rozsah jsou v results/euclid-subtractive.json.
Program používá uložené množiny z již dokončeného ověření33,
nově kontroluje váhy, hranice, seskupení(S5) a identitu(S13).
Obecný důkaz je v oddílech1–5; konečný výčet jej nenahrazuje.

Běh72239/PID1209772, limit180s, dokončen exit0. Nové kontroly:
13054 vah a řezů,10423 neprázdných dvojic y,x',5225
vyloučených dvojic,8256 přímých odečítacích vstupů;4096
závěrečných a8192 lokálních přesných identit;1064
intervalových harmonických kontrol při80 desetinných
místech. Starý výčet čtveřic se znovu nespouštěl.
