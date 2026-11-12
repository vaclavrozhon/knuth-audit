# §4.5.4: Lucasův test z N+1 a věta L

Úloha 15 a matematický důkaz Lucasova–Lehmerova testu na
409–411 jsou uzavřeny. Věta i hlavní odpověď jsou správné.
V doprovodném předtestu na 660 je hraniční chyba
[C0160](C0160-lucas-gcd-boundary.md), která se netýká
platnosti kritéria. Historie, velký seznam prvočísel na 409
a otázka 16 tvoří samostatný navazující blok.

Vizuálně byly přečteny 409–411, 413, 660 a dříve 661.
Zde P,Q označují nesoudělná celá čísla a `D=P²-4Q`
jejich diskriminant, tedy výraz rozlišující kořeny
kvadratického polynomu `x²-Px+Q`. Lucasovy posloupnosti
jsou definovány rekurencemi

```
U_0=0, U_1=1, U_(n+1)=P*U_n-Q*U_(n-1),
V_0=2, V_1=P, V_(n+1)=P*V_n-Q*V_(n-1).                       (1)
```

## 1. Identity a nejmenší index dělitelnosti

Matice `M=((P,-Q),(1,0))` se nazývá doprovodná matice
rekurence: její násobení posouvá dvojici sousedních členů.
Z `M²=P*M-Q*I` indukcí dostaneme pro n>=1

```
M^n = U_n*M-Q*U_(n-1)*I,
(M^n)_(2,1)=U_n,       trace(M^n)=V_n.                        (2)
```

Stopa matice je součet jejích diagonálních prvků. Vzorec (2)
poskytuje výpočet U_n i V_n opakovaným čtvercováním v
O(log n) modulárních operacích, jak uvádí zadání.
Další identity jsou

```
V_n=U_(n+1)-Q*U_(n-1),
U_(m+n)=U_m*U_(n+1)-Q*U_(m-1)*U_n,
U_(2n)=U_n*V_n,       V_(2n)=V_n²-2Q^n.                       (3)
```

Druhá platí pro m>=1,n>=0. První tři vyplývají z (2),
poslední také ze stopy a determinantu `det(M^n)=Q^n`.

Pokud `gcd(Q,N)=1`, je M invertibilní modulo N.
Podle (2) je U_n dělitelný N právě tehdy, když M^n je
skalární matice, tedy násobek identity. Nějaká kladná
mocnina M je identita, protože invertibilních matic modulo N
je konečně mnoho. Nejmenší kladný index z se členem U_z=0
modulo N tedy existuje. Nazývá se **rank of apparition**,
zde nejmenší index dělitelnosti. Skalár M^z je invertibilní,
takže dělení indexu n se zbytkem podle z dává

```
U_n=0 (mod N)  právě když  z|n.                              (4)
```

Tento důkaz nepředpokládá, že N je prvočíslo. Pro speciální
P=4,Q=1 současně `gcd(U_n,U_(n+1))=1`, neboť společný
dělitel se rekurencí přenese zpět až na U_1=1. To ověřuje
i knižní důkaz (37) posunem posloupnosti.

Pro úplnost se zavedením formálních kořenů
`alpha=(P+sqrt(D))/2`, `beta=(P-sqrt(D))/2` dostáváme
`V_n=alpha^n+beta^n` a, při D!=0,
`U_n=(alpha^n-beta^n)/sqrt(D)`. Binomický rozvoj dává

```
2^(n-1)*U_n = sum_k binom(n,2k+1)*P^(n-2k-1)*D^k,
2^(n-1)*V_n = sum_k binom(n,2k)*P^(n-2k)*D^k.                 (5)
```

Sčítá se pouze přes nezáporné exponenty P. Tyto polynomiální
identity platí i pro D=0; není tam nutné dělit odmocninou.
Pro P=4,Q=1 dávají přesně (30), (31), (34) na 410.

## 2. Prvočíselná a mocninná mez pro index

Nechť p je liché prvočíslo nedělící 2QD a χ je Legendreův
symbol D modulo p: χ=1 pro nenulový čtverec a χ=−1 jinak.
Počítejme s výrazy `a+b*t`, kde `t²=D`, nad zbytky modulo p.
Jde o kvadratickou algebru: každý výsledek má jednoznačné
dva koeficienty a,b. Nemusí být tělesem, když D je čtverec;
to není pro následující výpočet překážkou. Prvky t, alpha,
beta jsou invertibilní, protože D a alpha*beta=Q jsou jednotky.

Binomická věta v charakteristice p a Eulerovo kritérium
dávají `t^p=χ*t`. Proto se alpha a beta při p-té mocnině
buď zachovají, nebo prohodí. Pro jednotku `gamma=alpha/beta`
tedy platí `gamma^p=gamma^χ`, a tak

```
gamma^(p-χ)=1,      U_(p-χ)=0 (mod p).                       (6)
```

Stejné výrazy lze definovat modulo p^a. Z (6) máme
`gamma^(p-χ)=1+p*w`. Jestliže je prvek tvaru `1+p^j*w`,
jeho p-tá mocnina je 1 modulo p^(j+1), opět podle
binomické věty. Indukcí tedy

```
U_(p^(a-1)*(p-χ))=0 (mod p^a).                              (7)
```

Není tu použit předpoklad, že nejmenší index při každém
zvednutí opravdu vzroste p-krát; tvrzení je dělitelnost.

Tištěné (35) je také přímý důsledek (5): pro liché p
`U_p=D^((p-1)/2)` a `V_p=P` modulo p. Pro P=4,Q=1
odpovídá D=12 a druhá mocnina 2 se v Legendreově symbolu
odstraní, takže vznikne `3^((p-1)/2)`.
V (36) na 410 zbývají p=2,3: `U_2=4`, `U_3=15`,
tedy v obou případech lze vzít epsilon(p)=0.

Zvedací tvrzení (33) platí i pro tato dvě prvočísla.
Položíme-li U_n=b*p^e a U_(n+1)=a, (2) pro P=4,Q=1
má tvar `M^n=a*I+U_n*(M-4I)`. Jelikož `p^(2e)` je
násobkem p^(e+1), binomický rozvoj dává

```
U_(kn)=k*a^(k-1)*U_n,
U_(kn+1)=a^k                         (mod p^(e+1)).           (8)
```

Pro k=p plyne (33). Všechny jeho vypsané mezikroky na 410
jsou tedy platné i pro e=1 a p=2.

## 3. Důkaz kritéria v úloze 15

Předpoklady zadání jsou `gcd(N,2D)=1`, `U_(N+1)=0 mod N`
a `U_((N+1)/r)!=0 mod N` pro každého prvočinitele r čísla N+1.
Případ N=1 neprojde: pro r=2 dostáváme U_1 mod1=0.
Dále je N>1 a liché.

Nejprve musí být `gcd(Q,N)=1`. Kdyby prvočíslo p dělilo
Q i N, nesoudělnost P,Q by dala `U_n=P^(n-1)!=0 mod p`
pro každé n>0. To je v rozporu s nulou U_(N+1).
Podle (4) je nejmenší index z dělitelem N+1. Kdyby byl
vlastním dělitelem, dělil by také (N+1)/r pro některé
prvočíslo r, ve sporu s předpoklady. Proto z=N+1.

Rozložme `N=product_(i=1)^d p_i^a_i`, s různými p_i.
Nechť `epsilon_i=−(D/p_i)` je opačný Legendreův symbol;
jde vždy o ±1. Vztah (7), čínská věta o zbytcích a (4)
ukazují, že N+1 dělí nejmenší společnou násobnost

```
T=lcm_i p_i^(a_i-1)*(p_i+epsilon_i).
```

Všechny členy této nejmenší společné násobnosti jsou sudé.
Jejich násobnost je proto nejvýše součin dělený 2^(d−1).
Jelikož p_i>=3,

```
N+1 <= T <= 2^(1-d)*product_i p_i^(a_i-1)*(p_i+1)
           <= 2*(2/3)^d*N.                                  (9)
```

Pro d>=2 je pravá strana nejvýše 8N/9, spor. Máme tedy
N=p^a. Zde `T=p^(a-1)*(p+epsilon)` leží pod 2(N+1),
a pokud epsilon=−1, dokonce pod N+1. Dělitelnost N+1|T
vynucuje epsilon=1 a T=N+1. Odtud p^(a−1)=1, tedy a=1.
N je prvočíslo. Zcela postačí tištěné podmínky „není nula
modulo N“; silnější podmínky nesoudělnosti se nepřidávají.

Odpověď pro Fibonacciho posloupnost P=1,Q=−1 je správná:
celá vypsaná posloupnost modulo 23 má první kladnou nulu
na indexu 24. Modulo 13 je první nula na 7, modulo 17
na 9, takže tyto dvě prvočíselnosti stejným kritériem
s touto pevnou dvojicí P,Q doložit nelze.

## 4. Věta L: kratší nezávislý důkaz

Nechť q>=3 je liché prvočíslo a N=2^q−1. Pro P=4,Q=1
položme alpha=2+sqrt3 a beta=2−sqrt3=alpha^−1.
Z (3) je `L_j=V_(2^j) mod N`, což je (38).

Předpokládejme nejprve L_(q−2)=0 a vezměme libovolný
prvočinitel p čísla N. Je p>=5, neboť N je liché
a N=1 modulo 3. Nad kvadratickou algebrou modulo p
má alpha inverzi beta a řád dělící `p−(3/p)`:
Frobeniova mocnina alpha^p je buď alpha, nebo beta.
Z `alpha^(2^(q-2))+alpha^(-2^(q-2))=0` plyne
`alpha^(2^(q-1))=−1`, tedy alpha má řád přesně 2^q.
Proto `2^q<=p+1`, čili p>=N. Jelikož p|N, musí N=p
být prvočíslo.

Naopak nechť N je prvočíslo. Je N=7 modulo 12, takže
`(3/N)=−1`. Číslo `c=2^((q+1)/2) mod N` splňuje c²=2.
V kvadratické algebře modulo N definujme
`delta=(1+sqrt3)/c`. Potom `delta²=alpha` a

```
delta^(N+1) = ((1-sqrt3)/c)*((1+sqrt3)/c) = -1.
```

Tedy `alpha^((N+1)/2)=−1` a `V_((N+1)/2)=−2`.
Protože `(N+1)/2=2^(q−1)`, identita zdvojení v (3)
dává `V_(2^(q-2))²=0 mod N`. N je prvočíslo, takže
V_(2^(q−2))=0, jak bylo potřeba.

## 5. Kontrola delšího knižního důkazu L

Kniha v prvním směru používá nejmenší index
`m=2^(q−1)`. To plyne z (3), (4) a
`gcd(U_n,V_n)<=2`, protože `2U_(n+1)=4U_n+V_n`
a sousední U jsou nesoudělná. Násobnost T z (7) pak
splňuje tištěný řetězec

```
m <= T <= 2*(3/5)^d*N < 4*(3/5)^d*m < 3m.
```

Pro d>=3 by navíc prostřední mez byla pod m. Proto
d<=2 a T je m nebo 2m, mocnina dvojky. Z p_i>=5
plyne a_i=1. Zbývající složený případ d=2 má dva
prvočinitele tvaru 2^k±1. Protože N=3 modulo 4,
jedno znaménko je plus a druhé minus, jak uvádí text.

Krok označený za zřejmý je opravdu platný. Z
`(2^k+1)(2^h−1)=2^q−1` bychom dostali
`2^q=2^(k+h)+2^h−2^k`. Pokud k<h, vyjmeme 2^k
a zbude lichý činitel větší než 1; při k>h obdobně
vyjmeme 2^h. Musí tedy být k=h, a pak q=2k je sudé,
spor. Ve zpětném směru se tištěný binomický rozvoj
na 411 přesně shoduje s (5) po odmocnění alpha;
okrajové binomické koeficienty i použití kvadratické
reciprocity dávají −2, bez změny znaménka či indexu.

## 6. Předtest v poznámce na 660

Pro P=1 doporučuje poznámka zvolit Q tak, aby N bylo
nesoudělné s QD. V závorce tvrdí, že jinak je N složené,
ledaže `|QD|>N`. **Rovnost byla vynechána.** Pro N=5,
Q=−1 je D=5 a gcd(N,QD)=5, ale |QD|=N. Číslo 5
je přesto prvočíslo. Stejně selže N=3,Q=1,D=−3.
Povolená degenerace Q=0 dává dokonce |QD|=0.

Přesná oprava je požadovat `1<gcd(N,QD)<N`, než se
oznámí složenost. Pokud se ponechá původní formulace
s absolutní hodnotou, výjimka musí zahrnout `QD=0`
i `|QD|>=N`. Jde o C0160; hypotézy a důkaz úlohy 15
se nemění.

## 7. Výpočetní a bibliografický rozsah

`verify_primality_lucas.py` porovnává lineární rekurenci
s mocninami doprovodné matice, přesnými binomickými
rozvoji a kvadratickou algebrou. Zvlášť kontroluje
zvedání u 2 a 3, a přijímající instance proti přímému
testu dělitelů. Celá vypsaná Fibonacciho posloupnost
je součástí výsledků. Lucasova–Lehmerova rekurence se
porovnává s přímým testem dělitelů pro všechny exponenty
3 až 31 a dvěma odlišnými modulárními modely pro všech
22 lichých uvedených prvočíselných exponentů nejvýše
11213. Prošlo 5408 přesných U/V indexů, 45968 součtových
identit, 600 zvedacích případů a 16972 instancí kritéria
s 58152 nezávislými maticovými kontrolami. Exponent 2 dává prvočíslo 3 přímo. Vyšší
historické ani současné rekordy se v tomto běhu
znovu necertifikují.

Bibliografie [Lehmer 1930](https://www.jstor.org/stable/1968235)
je potvrzena metadaty původního vydavatele; doplnění
série (2) v erratu z 8. října 2010 je správné.
PDF požadavek vrátil HTML, nikoli článek: str. 443
ani plný článek se proto nevykazují jako přečtené.
Lucasův původní text na 316 byl dostupný jako veřejný
[OCR přepis](https://fr.scribd.com/document/842433229/Lucas-ThoriedesFonctions-1878); vzor rekurence 4,14,194 a příklad
pro exponent13 odpovídají odkazu. Nejde o vizuální
přečtení originálu. Reprodukci fragmentu na Commons se
nepodařilo stáhnout (HTTP403). Rozsah navazující kontroly
Mersennova seznamu se eviduje samostatně v metadatech. Vlastní důkazy v §1–5 tyto zdroje
nepoužívají jako neověřené matematické kroky.

Všechny čtyři vrstvy errat i aktuální TeX byly
prohledány podle stran, Lucasova jména, QD a tématu.
Oprava poznámky na 660 nebyla nalezena. Novější
fyzický dotisk ani prvenství nálezu nebyly ověřeny;
návrh hlášení zůstává neodeslaný.
