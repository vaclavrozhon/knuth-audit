# §4.5.3-33/34: Heilbronnovy reprezentace a rovnoměrný odhad

Audit 2026-11-03. Obě úlohy jsou uzavřeny obecným důkazem
včetně konečných krajních případů a rovnoměrnosti pomocných
odhadů. Původní strany377/653 byly vizuálně přečteny. Známé
opravy z roku2004 odstraňují meze sumy v34(c) a doplňují
Möbiovu funkci i druhou sumu v odpovědi34. Všechny čtyři
vrstvy errat prohledány; nový nález v tomto bloku nevznikl.

Značení T_n, phi, mu a Lambda je definováno v oddílu3
poznámky euclid-discrete.md: T_n je průměr počtu dělení,
phi je Eulerova funkce, mu Möbiova a Lambda von Mangoldtova.
V dalším textu K_r označuje continuant, tj. jmenovatel
řetězového zlomku [0;a_1,...,a_r] v základním tvaru, s K_0=1.

## 1. Přesná parametrizace v úloze33

Nechť h(n) počítá čtveřice kladných celých čísel splňující

```
n = x x' + y y',   x>y,   x'>y',   gcd(x,y)=1.           (H1)
```

Povolíme-li také x'=y'=d, máme n=d(x+y). Položme m=dx.
Pak n/2<m<n a d=gcd(m,n-m). Obráceně každé takové m
určuje právě jednu novou čtveřici. Je jich floor((n-1)/2),
což dokazuje33(a).

Fixujme y>=1 a zástupce t v1,...,y s gcd(t,y)=1. Pro dané
x'>0 splňující x't=n modulo y musí x ležet v třídě t a

```
n/x'-y <= x < n/x'.                                   (H2)
```

Tento interval délky y, s právě jedním uzavřeným krajem,
obsahuje právě jedno číslo této třídy. Podmínka x>y je
ekvivalentní x'<n/(y+t). Potom y'=(n-xx')/y je celé
a splňuje0<y'<=x'. To dokazuje obě implikace33(b).

Označme t' jediného zástupce t' v1,...,y splňujícího
tt'=n modulo y. Povolená x' jsou t',t'+y,t'+2y,... pod
ostrou horní mezí n/(y+t). Jejich počet je

```
ceil((n/(y+t)-t')/y).                                 (H3)
```

Výraz uvnitř je větší než-1, takže není potřeba další maximum
s nulou. Sečtení(H3) a odečtení floor((n-1)/2) je33(c).
Nenulový člen vyžaduje n>=2y+1; suma je tedy fakticky konečná.
Zásadní je horní celá část, protože mez pro x' je ostrá.

## 2. Rozdělení řetězového zlomku a počet kroků

Každý nesoudělný pár x>y>0 má jediný zápis

```
x=K_m(a_1,...,a_m), y=K_(m-1)(a_1,...,a_(m-1)),
a_1>=2, a_2,...,a_m>=1.                              (H4)
```

Je to obrácení kanonického rozvoje y/x. Podobně pro
d=gcd(x',y') jednoznačně platí

```
x'=d K_k(a_(m+1),...,a_(m+k)),
y'=d K_(k-1)(a_(m+2),...,a_(m+k)), a_(m+k)>=2.          (H5)
```

Continuantová identita z úlohy32 dává n/d=K_(m+k).
Obráceně každý kanonický seznam délky r>=2, s oběma
krajními podíly alespoň2 a s K_r dělícím n, má r-1 míst
řezu a každý řez určuje jinou čtveřici(H1). Jednoznačnost
(H4),(H5) zaručuje také jednoznačnost obráceného převodu.
To dokazuje33(d), včetně m=1 nebo k=1, kdy se použije K_0=1.

Pro zlomek m/n s0<m<=n/2 označme jeho počet podílů r(m/n).
Z předchozí korespondence a úlohy26 plyne

```
h(n) = sum_(m=1..floor(n/2)) (r(m/n)-1),
sum_(m=1..floor(n/2))T(m,n) = 2 floor(n/2)+h(n).         (H6)
```

Počáteční nulový podíl při m<n znamená T(m,n)=r(m/n)+1.
Pro m<n/2 přidá přechod na1-m/n jeden podíl, takže
T(n-m,n)=T(m,n)+1. Prostřední zlomek1/2, pokud existuje,
má T(n/2,n)=2; navíc T(0,n)=1. Oddělení lichého a sudého n
v(H6) proto dává přesně

```
n T_n = floor((5n-3)/2)+2h(n).                         (H7)
```

Platí i pro n=1. Tím je33(e) dokázána bez asymptotického
odhadu nebo předpokladu nesoudělnosti původního m,n.

## 3. Symetrie a rovnoměrný odhad h_d

Nechť g(n) počítá(H1) bez požadavku gcd(x,y)=1. Dále h_d(n)
počítá původní primitivní čtveřice s xd<x', s vahou1/2
pro čtveřice splňující xd=x'. Vydělení x,y jejich společným
dělitelem a Möbiova inverze dávají

```
g(n)=sum_(d|n)h(n/d),
h(n)=sum_(d|n)mu(d)g(n/d).                             (H8)
```

V g(n) lze zaměnit primované a neprimované dvojice. Případy
x<x' tedy mají stejný počet jako x>x'; rovnosti se započtou
poloviční vahou. Po vydělení x,y jejich největším společným
dělitelem d dostáváme druhou identitu34(a):

```
g(n)=2 sum_(d|n)h_d(n/d).                              (H9)
```

Nyní n,d>=1 a Y=sqrt(n/d). Z xd<=x' a(H1) plyne y<Y.
Pro každé y<Y a t v1,...,y s gcd(t,y)=1 spočtěme nejprve
všechny čtveřice s x'>=y' pomocí33(b). Podle(H3) se jejich
počet liší od n/[y(y+t)] nejvýše o1.

Nežádoucí čtveřice s xd>=x' mají x'<sqrt(nd), neboť
n>xx'>=(x')^2/d. V příslušné třídě modulo y jich je nejvýše
sqrt(nd)/y+1. Celkem přes všechna y,t je jich nejvýše
n+n/d<=2n. Součet chyb zaokrouhlení je nejvýše n/d<=n.
Nakonec odstraníme x'=y'; všech takových čtveřic je nejvýše
n/2 podle33(a). Rovnosti xd=x' s poloviční vahou jsou
při tomto odhadu již pokryté počtem nežádoucích čtveřic.

Získáváme tedy explicitní, na d nezávislou verzi34(b):

```
|h_d(n)-n sum_(0<t<=y<sqrt(n/d), gcd(t,y)=1)1/[y(y+t)]|
 <= 4n.                                              (H10)
```

Pro Y<=1 jsou obě počítané části nulové. Rovnoměrnost(H10)
je důležitá, protože později se sčítá přes mnoho parametrů d.

## 4. Harmonické součty v34(c)/(d)

Definujme sigma_-1(y)=sum_(d|y)1/d a H_r=sum_(j=1..r)1/j,
s H_0=0. Nechť

```
s(y)=sum_(1<=t<=y, gcd(t,y)=1)y/(y+t).
```

Rozdělení všech t=1,...,y podle gcd(t,y) dává

```
sum_(d|y)s(d)=y(H_(2y)-H_y)=:k(y),
s(y)=sum_(d|y)mu(y/d)k(d).                             (H11)
```

Druhá rovnost obsahuje Möbiovu funkci, doplněnou známým
erratem. Použijeme lichoběžníkové pravidlo na f(x)=1/(1+x)
v intervalu [0,1] s y stejnými dílky. Jeho chyba je nejvýše
max|f''|/(12y^2); max|f''|<=2. Po vynásobení y dostáváme

```
k(y)=y ln2-1/4+e_y,   |e_y|<=1/(6y).                  (H12)
```

Vložením do(H11), s identitami úlohy28, plyne

```
s(y)=phi(y)ln2-(1/4)[y=1]+sum_(d|y)mu(y/d)e_d
    =phi(y)ln2+O(sigma_-1(y)).                          (H13)
```

Dokonce velikost poslední chyby je nejvýše5 sigma_-1(y)/12.
Součet přes všechna y této chyby dělené y^2 konverguje, neboť

```
sum_(y>=1)sigma_-1(y)/y^2=zeta(2)zeta(3)<infinity.      (H14)
```

Z definice phi(y)=y sum_(d|y)mu(d)/d dále přesně vychází

```
sum_(y=1..M)phi(y)/y^2
 =sum_(d=1..M)mu(d)H_floor(M/d)/d^2.                   (H15)
```

To dokazuje34(d); opravená dvojitá suma v odpovědi653
odpovídá přeskupení y=cd. Pro u>=1 platí
H_floor(u)=ln u+gamma+O(1/u) s absolutní konstantou.
Protože sum mu(d)/d^2=1/zeta(2)=6/pi^2,
sum (ln d)/d^2<infinity a ocas sum1/d^2 je O(1/M), plyne

```
sum_(y<=M)phi(y)/y^2=(6/pi^2)ln M+O(1).                (H16)
```

Všechny konstanty jsou absolutní. Stejný odhad platí pro
ostrou mez y<Y, Y>1; případné odstranění posledního členu
je omezené. Z(H10),(H13),(H14),(H16) tedy dostaneme

```
h_d(n)=alpha n log^+(n/d)+O(n),
alpha=3 ln2/pi^2,   log^+(z)=max(ln z,0),               (H17)
```

rovnoměrně pro všechna celá n,d>=1. Když d<=n, je to
tištěný výraz alpha n ln(n/d)+O(n). Když d>n, žádná
čtveřice nemůže splnit xd<=x', a hlavní člen musí být0.
Tuto část rozsahu nelze při následném sčítání prostě ignorovat.

## 5. Dokončení34(e) a odstranění kladné části

Spojením(H8),(H9) máme přesně

```
h(n)=2 sum_(cd|n)mu(d)h_c(n/(cd)).                      (H18)
```

Součet absolutních chyb po dosazení(H17) je

```
O(n sum_(cd|n)1/(cd))=O(n sigma_-1(n)^2).               (H19)
```

Poslední nerovnost se ověří po prvočinitelích: koeficient
p^(-j) pro0<=j<=e v sum_(c d|p^e)1/(cd) je j+1;
čtverec (sum_(i=0..e)p^-i)^2 má stejné koeficienty
v tomto rozsahu a další nezáporné členy.

Zbývá zdůvodnit, proč lze v hlavním součtu nahradit
log^+(n/(c^2d)) obyčejným logaritmem. Pišme e=n/(cd).
Rozdíl se vyskytuje jen pro c>e a jeho absolutní hodnota
po odstranění faktoru n je nejvýše

```
sum_(cde=n, c>e) ln(c/e)/(cd)
 <=sum_(cde=n, c>e)1/(ed)
 <=sum_(ed|n)1/(ed) <= sigma_-1(n)^2.                   (H20)
```

Použili jsme pouze ln r<=r pro r>1. Tím je doplněna
rovnoměrná kontrola rozsahu d, kterou stručná odpověď
nerozepisuje. Dodatečná chyba se vejde do(H19).

Nyní jsou logaritmy oddělitelné a přesné identity jsou

```
sum_(cd|n)mu(d)/(cd)=1,
sum_(cd|n)mu(d)ln(cd)/(cd)=0,
sum_(cd|n)mu(d)ln c/(cd)=sum_(k|n)Lambda(k)/k.            (H21)
```

První dvě plynou po seskupení podle k=cd ze sum_(d|k)mu(d).
Pro třetí použijeme sum_(d|k)mu(d)ln(k/d)=Lambda(k).
Z(H17)–(H21) dostáváme

```
h(n)=2 alpha n (ln n-sum_(d|n)Lambda(d)/d)
     +O(n sigma_-1(n)^2).
```

Nakonec(H7) dává přesně tvrzení34(e):

```
T_n=(12 ln2/pi^2)(ln n-sum_(d|n)Lambda(d)/d)
    +O(sigma_-1(n)^2).                                (H22)
```

Aditivní omezený člen z floor((5n-3)/2)/n je absorbován
do chyby, protože sigma_-1(n)>=1. Žádný krok této derivace
nepředpokládá, že původní čitatel je nesoudělný se jmenovatelem.

## 6. Pomocná mez sigma_-1(n)=O(log log n)

Pro úplnost dokládáme také poslední poznámku odpovědi653.
Součin po prvočíslech dává

```
sigma_-1(n)<=product_(p|n)(1-1/p)^-1.                  (H23)
```

Nejprve ukážeme product_(p<=Y)(1-1/p)^-1=O(ln Y) pro Y>=2.
Označme theta(Y)=sum_(p<=Y)ln p. Prvočísla mezi m a2m
dělí binom(2m,m)<=4^m. Sečtením po dyadických intervalech
proto theta(Y)=O(Y). Částečné sčítání pak dává

```
sum_(p<=Y)ln p/(p-1)=O(ln Y).                          (H24)
```

Položíme s=1+1/ln Y. Rozvinutím logaritmů Eulerových faktorů
a nerovností1-exp(-u)<=u dostaneme

```
ln product_(p<=Y)(1-1/p)^-1
-ln product_(p<=Y)(1-p^-s)^-1
 <=(s-1)sum_(p<=Y)ln p/(p-1)=O(1).
```

Druhý součin je nejvýše zeta(s)<=1+1/(s-1)=1+ln Y,
což dokazuje požadovanou mez. Nyní zvolme Y=max(2,ln n).
Počet prvočinitelů n větších než Y je nejvýše ln n/ln Y.
Jejich příspěvek k logaritmu(H23) je nejvýše
2 ln n/(Y ln Y)=O(1). Součin pro malá prvočísla je O(ln Y).
Tedy sigma_-1(n)=O(log log n) pro n>=3; finitně mnoho
menších hodnot neovlivňuje asymptotiku. Důkaz používá jen
binomickou nerovnost a absolutně konvergentní Eulerův součin.

## 7. Nezávislé konečné kontroly a prameny

Program verify_euclid_heilbronn.py má tři obnovitelné bloky.
První přímo vyjmenuje čtveřice celočíselnými smyčkami a
porovná je s jiným modelem: řezy všech řetězových zlomků.
Zachovává celé množiny čtveřic, nejen shodu jejich počtů.
Další blok ověří všechny parametry d=1,...,n+1 pro n<=128,
včetně rovností s poloviční vahou. Třetí blok kontroluje
harmonické a dělitelové identity přesnými zlomky; koeficienty
logaritmů porovnává symbolicky po jednotlivých prvočíslech.

Session97799/PID1206690, limit300s, všechny tři bloky exit0:

- 13054 čtveřic s povolenou rovností, z toho9022 ostrých řezů
  a4032 hraničních reprezentací; všechny části33 prošly.
- 8384 dvojic n,d a1627 výskytů rovnosti xd=x'; všechny
  identity34(a) a explicitní mez4n prošly. Největší pozorovaný
  poměr chyby k n byl11/15 při n=12,d=1; jde pouze o konečný
  údaj, nikoli návrh optimální globální konstanty.
- 512 harmonických/Möbiových a1024 závěrečných dělitelových
  vstupů prošlo, včetně chybové majoranty sigma_-1(n)^2.

Reprodukce s python-flint0.9.0 dostupným kvůli sdílenému
pomocnému modulu:

```
python3 workstreams/vol2/verify_euclid_heilbronn.py --resume
```

Příkaz bez --resume znovu vytvoří i uloženou množinu
reprezentací. Výstupy jsou euclid-heilbronn.json a
euclid-heilbronn-representations.json v results/.

[Heilbronnův vydavatelský záznam](https://link.springer.com/chapter/10.1007/978-1-4615-4819-5_7)
potvrzuje titul, rok1969 a strany87–96; úplná kapitola nebyla
dostupná. Matematický audit výše má proto vlastní úplný důkaz,
ne tvrzení o přečtení nedostupného originálu. Související
veřejný sken zprávy Yao–Knuth STAN-CS-75-510 byl získán
pro následující úlohu35. Stav pramenů a jejich konkrétní
omezení jsou v sources/euclid-heilbronn.json.

Na aktuální autorově stránce Selected Papers on Analysis
of Algorithms je oprava jiného vzorce na straně29, měnící
sigma_-1(n)^2 na(log log n)^4. Bez původní strany29 ji
nelze přenést na zdejší tvrzení o T_n. Výše jsme(H22)
odvodili přímo se všemi chybami; nepoužíváme ji jako
neověřenou citaci a netvrdíme shodu obou míst.
