# §1.2.6: základní binomické identity

Rozpracovaný audit 1. listopadu 2026, třetí vydání, první dotisk.
Tato poznámka pokrývá s. 53–64 a související elementární úlohy.
Stirlingova čísla, obecné dolní indexy, q-analogie a zbývající úlohy
se zde neprohlašují za prověřené. Zobrazeny původní stránky
53–64,69–71,483–486 a relevantní stránky všech vrstev errat.

## Definice a počítání

Značíme `C(r,k)=r(r−1)...(r−k+1)/k!` pro celé k>=0, s prázdným
součinem C(r,0)=1. Pro celé k<0 definujeme C(r,k)=0. Horní index
r může být reálný či komplexní. Pro pevné k>=0 je C(r,k) polynom
stupně k s vedoucím koeficientem 1/k!; pro k<0 nulový polynom.

Pro celá n>=0 a 0<=k<=n rozděluje zapomenutí pořadí injekční
k-tice na třídy velikosti k!. Proto C(n,k) počítá k-prvkové
podmnožiny n-prvkové množiny. Pro k>n takové podmnožiny nejsou;
součin v definici obsahuje nulu. To zahrnuje prázdnou podmnožinu
i prázdnou množinu. Seznam deseti trojic z pěti prvků na s. 53
obsahuje každou právě jednou; OCR zaměňuje bcd,bce za bed,bee.

Obr. 8 zobrazuje čtyři trojúhelníkové vrstvy velikostí 1,3,6,10,
celkem 20=C(6,3) bodů. Obecně lze bod označit čtveřicí nezáporných
celých souřadnic se součtem n−1. Vložení tří oddělovačů mezi
n−1 stejných značek dává C(n+2,3) možností. To ověřuje
geometrický obsah obrázku; tvrzení o antických pramenech je jiné.

## Základní pravidla (5)–(11), (17)–(20)

(5) Faktoriálový podíl platí přímo krácením pro celá n>=k>=0.
Rozšíření z errat 4. října 2021 na reálné r>=k plyne k-násobnou
rekurencí Gamma. V tomto oboru žádný použitý faktoriál nemá pól.

(6) Doplněk podmnožiny dává C(n,k)=C(n,n−k) pro celé n>=0.
Je-li k mimo [0,n], obě strany jsou nula. Pro obecné reálné n
nelze tento krok používat bez jiné definice dolního indexu.

(7),(8) Z konečných součinů máme polynomiální rovnosti

```text
k C(r,k) = r C(r−1,k−1),
(r−k) C(r,k) = r C(r−1,k).
```

První zahrnuje k=0: obě strany jsou nula. Pro k<0 jsou rovněž
obě nula. Dělení k či r−k je dovoleno právě při jejich nenulovosti.
Knižní důkaz druhé rovnosti pro kladná celá r se správně rozšíří
polynomiální identitou: nenulový polynom má jen konečně mnoho
kořenů. V několika proměnných lze tento argument použít postupně.

(9) Pascalovo pravidlo `C(r,k)=C(r−1,k)+C(r−1,k−1)` plyne
sečtením obou rovností a krácením r pro r≠0, potom polynomiálním
pokračováním pro r=0. Lze je ověřit také přímo; k<=0 je zahrnuto.

(10) Indukce podle n>=0 s Pascalovým pravidlem dává
`sum_{k=0}^n C(r+k,k)=C(r+n+1,n)`. Rozšíření z errat 2021
na záporná celá n je správné: i při orientované konvenci konečného
součtu jsou všechny přidané členy s k<0 nula, stejně jako pravá
strana. (11) Teleskopování rovnosti
`C(k,m)=C(k+1,m+1)−C(k,m+1)` dává
`sum_{k=0}^n C(k,m)=C(n+1,m+1)` pro celá m,n>=0.
Počáteční člen C(0,m+1) je nula; n<m také dává nulu.

(17) Vytažení k záporných znamének a obrácení pořadí činitelů dává
`C(r,k)=(−1)^k C(k−r−1,k)` pro k>=0. Pro záporné celé k
jsou obě strany nula. (18) Dosazením do (10) vzniká
`sum_{k<=n} (−1)^k C(r,k)=(−1)^n C(r−1,n)` pro všechna
celá n; n<0 dává prázdný nenulový rozsah. Kombinace (6),(17)
dává (19), `C(n,m)=(−1)^(n−m) C(−m−1,n−m)` pro n>=0
a libovolné celé m. Pro m<0 i m>n jsou obě strany opět nula.

(20) Identita
`C(r,m)C(m,k)=C(r,k)C(r−k,m−k)` plyne rozdělením padajícího
součinu pro 0<=k<=m, popřípadě dvojím výběrem podmnožiny.
Jestliže m<0, pak pro k>=0 je m−k<0 a pro k<0 C(r,k)=0.
Jestliže m>=0 a k mimo [0,m], alespoň jeden faktor na každé
straně je nula. Tím je doložen celý otištěný obor, nejen kladné indexy.

## Binomická věta a konvergence (13)–(15)

Pro celé n>=0 roznásobení n činitelů x+y vybere k pozic pro x;
to dává koeficient C(n,k). Alternativně indukce použije (9).
Konvence 0^0=1 je v polynomiálním vzorci konzistentní i pro n=0.
Součet přes všechna celá k znamená vynechat členy s nulovým
binomickým koeficientem před vyhodnocením případné záporné mocniny
nuly. Toto pravidlo „strongly zero“ bylo výslovně přidáno v 2022.
Nejde o běžnou aritmetickou rovnost 0 krát nedefinovaný výraz.

Pro obecné r má řada `F(x)=sum_{k>=0} C(r,k)x^k` poloměr
konvergence alespoň 1: poměr sousedních absolutních hodnot jde
k |x|, pokud řada nekončí. Uvnitř jednotkového kruhu lze derivovat
po členech. Z (k+1)C(r,k+1)=(r−k)C(r,k) dostáváme
`(1+x)F'(x)=r F(x)`, F(0)=1. Jediné řešení je
`F(x)=exp(r Log(1+x))`, kde Log je analytická větev s Log(1)=0.
Na reálném intervalu (−1,1) jde o obvyklou reálnou mocninu.
Obecný tvar (13) vznikne násobením y^r při |x/y|<1, všude,
kde jsou mocniny definovány s navzájem slučitelnou větví;
pro reálná x,y a reálné necelé r postačuje y>0.

## Konečné diference a polynomy (12), (33)–(38)

Dopředná diference je `Delta f(x)=f(x+1)−f(x)`. Indukce dává
`Delta^r f(0)=sum_{k=0}^r (−1)^(r−k) C(r,k)f(k)`.
Pascalovo pravidlo znamená `Delta C(x,j)=C(x,j−1)`;
odtud (33) s Kroneckerovou deltou, která je 1 pro stejné indexy
a 0 jinak. Platí i pro záporný dolní index n, kdy jsou obě nula.

Polynomy C(x,0),...,C(x,m) tvoří bázi polynomů stupně nejvýše m,
protože jejich stupně jsou různé a vedoucí koeficienty nenulové.
Každá diference sníží stupeň o 1 a násobí vedoucí koeficient
původním stupněm. Proto pro f(x)=sum_{j=0}^r b_j x^j je
`Delta^r f(0)=r! b_r`, což je (34), včetně r=0.
Pro f(k)=C(s−tk,r) je vedoucí koeficient (−t)^r/r!, takže
vynásobení (34) znaménkem (−1)^r dává přesně (35).

V (12) je `k²=2C(k,2)+C(k,1)`. Součet přes k=0,...,n podle
(11) dává n(n+1)(2n+1)/6. Analogicky pro úlohu 14 máme

```text
k^4 = 24C(k,4)+36C(k,3)+14C(k,2)+C(k,1),
sum_{k=0}^n k^4 = 24C(n+1,5)+36C(n+1,4)+14C(n+1,3)+C(n+1,2)
                = n(n+1)(2n+1)(3n²+3n−1)/30.
```

V (37), pro prefix n>=0, je C(−2,k)=(−1)^k(k+1).
Párování sousedních členů dává (−1)^n ceil((n+1)/2).
Obecně pro pevné záporné celé m je C(m,k) znaménko (−1)^k
krát polynom v k. Součet má tvar (−1)^n Q(n)+c s polynomem Q:
operátor Q(n)→Q(n)+Q(n−1) je na každém konečném prostoru
polynomů invertibilní, neboť v mocninné bázi je trojúhelníkový
s diagonálou 2. To dokládá i slovní zobecnění na s. 64.

(38) plyne přímo z
`(k−m/2) C(m,k) = (m/2)[C(m−1,k−1)−C(m−1,k)]`.
Teleskopování dává `−m C(m−1,n)/2`, včetně m=0.
Tvrzení o nemožnosti určitých uzavřených součtů v následujícím
odstavci vyžaduje zvlášť vymezit třídu výrazů. Pramen A=B
a přesný důkaz neexistence hypergeometrické antidiference
jsou prověřeny v `hypergeometric-summation.md`.

## Součiny a konvoluce (21)–(25)

Symbol `[x^n]F(x)` označuje koeficient x^n v mocninné řadě F.
Součin dvou takových řad má koeficient
`sum_{k=0}^n [x^k]F [x^(n−k)]G`; tento konečný součet
se nazývá konvoluce. Pro záporné n je koeficient 0.
Z (1+x)^r(1+x)^s=(1+x)^(r+s) dostáváme (21),
`sum_k C(r,k)C(s,n−k)=C(r+s,n)` pro všechna celá n.
Pro n>=0 jsou obě strany polynomy v r,s, takže postačí i
kombinatorický důkaz pro nezáporná celá r,s a polynomiální pokračování.

(22) Změníme v prvním faktoru C(r,m+k) na C(r,r−m−k)
a dosadíme j=n+k. Dostáváme (21) s cílovým stupněm r−m+n.
Podmínka celé r>=0 ospravedlňuje symetrii i konečnou podporu;
m,n jsou libovolná celá, s libovolné reálné či komplexní.

(23) Pascalovo pravidlo dává `Delta C(s+k,n)=C(s+k,n−1)`
při diferencování v k. R-násobná diference proto dává
`sum_k (−1)^(R−k)C(R,k)C(s+k,n)=C(s,n−R)` pro R>=0
a celé n. To je požadovaný induktivní důkaz úlohy 19.

(24) Je-li r<t nebo r−t<m, jsou všechny členy i pravá strana 0.
Jinak položme N=r−t−m>=0 a j=k−t. Nenulový rozsah je 0<=j<=N.
Použití (19) ve tvaru
`C(r−k,m)=(−1)^(N−j) C(−m−1,N−j)` spolu s (21) dává

```text
sum_j C(r−t−j,m) C(s,j)(−1)^j
 = (−1)^N C(s−m−1,N)
 = C(r−t−s,N).
```

Poslední krok je (17). Otištěné podmínky t,r,m>=0 jsou dostačující.

(25) Pro celá 0<=s<=n a r,m>=0 položme j=s+k. Doplnění
součtu na j=0,...,r+s nezmění hodnotu, protože j<s<=n má
C(j,n)=0. Počítáme tak
`sum_j C(r+s−j,m)C(j,n)=C(r+s+1,m+n+1)`.
Kombinatorický důkaz: z podmnožiny velikosti m+n+1 množiny
{0,...,r+s} určíme její (n+1)-ní nejmenší prvek j; n prvků
zvolíme pod j a m nad j. Tím je každá podmnožina započtena jednou.
Stejnou identitu lze získat i převodem (24) pomocí (19), jak žádá
úloha 20. Položíme t=n−s>=0; pak
`C(s+k,n)=(−1)^(k−t)C(−n−1,k−t)`.
Vzorec (24) s parametry r,t,m a s' =−n−1 dává
`C(r+s+1,r+s−n−m)`. Symetrie (6) změní dolní index
na m+n+1. Použité horní indexy s+k a r+s+1 jsou nezáporné.

Pro obecné s je správný doplněk odpovědi 21 z roku 2003

```text
sum_{k=0}^r C(r−k,m)C(s+k,n)
 = C(r+s+1,m+n+1)
   −sum_{j=0}^m C(r+1,j)C(s,m+n+1−j).                 (B1)
```

Důkaz: Pascalovou indukcí podle r dostaneme polynomiální rovnost

```text
x^(m+1) sum_{k=0}^r C(r−k,m)(1+x)^k
 = (1+x)^(r+1)−sum_{j=0}^m C(r+1,j)x^j.
```

Vynásobíme (1+x)^s a porovnáme koeficient stupně m+n+1.
Pro 0<=s<=n celý opravný součet mizí. Obecně levá strana
(25) má v s stupeň nejvýše n, pravá stupeň m+n+1; shoda
v n+1 bodech nestačí. Původní výjimka „m=0“ v odpovědi 21
je také nesprávná a byla nahrazena v 2003. Například m=n=r=0,
s=1 dává levou stranu 1, pravou 2; (B1) opraví rozdíl přesně.

## Úlohy 1–9,16,29,36–37

1–4. C(n,n−1)=n pro n>=1; při formálním rozšíření n=0 jsou
obě strany 0. C(0,0)=1. Bridgeová ruka má C(52,13)=635013559600
možností, s rozkladem `2^4 5^2 7^2 17 23 41 43 47`.
5. Dosazení x=10,y=1,n=4 do (13) dává 14641 bez přenosů.
6. Řádky pro r=−1,−2,−3 jsou
`(−1)^k`, `(−1)^k(k+1)`, `(−1)^k(k+1)(k+2)/2` pro k>=0;
vlevo od k=0 jsou nuly. Celá řada splňuje (9).
7. Poměr sousedních kladných členů je (n−k)/(k+1), proto maxima
leží v floor(n/2) a ceil(n/2); při sudém n jde o stejný index.
8–9. Symetrie znamená obrácení nenulové části řádku.
C(n,n)=1 pro n>=0, ale 0 pro n<0 kvůli zápornému dolnímu indexu.

16. Obě strany zadané identity jsou po použití (17),(6) rovny
`(−1)^(n+k−1) C(n+k−2,k−1)` pro kladná celá n,k.
29. Pro uzly 0,...,n je
`product_{0<=j<=n,j!=k}(k−j)=k!(−1)^(n−k)(n−k)!`.
Vzorec 1.2.3-33 pro nejvyšší koeficient interpolačního polynomu
se tedy po vynásobení n! změní přesně na (34).
36–37. Dosazení x=1 a x=−1 do (15) dává 2^n a [n=0]
pro celá n>=0. Součet sudých indexů je polovinou jejich součtu,
tedy 2^(n−1) pro n>0 a 1 pro n=0. Liché indexy analogicky
dávají 2^(n−1) pro n>0 a 0 pro n=0.

## Rozsah a návaznost

Rotheho a Abelovy identity a příklady 1–5 jsou v
[rothe-abel.md](rothe-abel.md). Kongruence úloh 10–12 budou
evidovány odděleně. Historické údaje o Pascalovi, indických
a čínských pramenech, Ettingshausenovi, Newtonovi a Gaussovi
zatím nejsou uzavřeny. Četnost nalezených známých errat není
počtem nových chyb.
