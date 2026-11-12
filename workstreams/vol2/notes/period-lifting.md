# §3.2.2-8–12: kvadratické generátory a zvedání period

Kontrola 1. listopadu 2026. Zadání na str. 37–38, odpovědi 552–554
a všechny relevantní vrstvy errat přečteny. `v_p(n)` znamená exponent
prvočísla p v nenulovém n. Periodou rozumíme nejmenší eventualní periodu;
úvod před opakováním se nezapočítává. Výsledky níže mají obecné důkazy,
nikoli pouze konečné testy.

## 8: přesné kritérium pro kvadratický generátor

Pro F(x)=d x^2+a x+c modulo m je perioda m právě tehdy, když:

1. gcd(c,m)=1;
2. pro každé liché prvočíslo p dělící m jsou d a a-1 násobky p;
3. při 4|m je d sudé a d=a-1 modulo 4; při 2|m je d=a-1 modulo 2;
4. při 9|m je d různé od 3c modulo 9.

**Nutnost.** Plná perioda prochází nulou a její projekce modulo každý
dělitel m prochází všemi zbytky. Kdyby p dělilo c, trajektorie nuly
by zůstala v násobcích p. Pro liché p a d nenulové modulo p má kvadratický
polynom stejnou hodnotu v x a -a/d-x, takže není permutací. Pro d=0
a a!=1 modulo p by měl pevný bod. Zbývající omezení jsou úplná kontrola
dvou, čtyř a devíti zbytků. Program ji ověřuje nezávisle přímou trajektorií.

**Dostatečnost a první zvednutí.** Stačí modul p^e, protože při složeném
m se plné periody jeho prvočíselných mocnin skládají podle čínské věty.
Pro p=2 podmínky dávají F^2(x)=x+2 modulo 4. Pro p=3 dávají
F^3(x)=x-d+3c modulo 9, s nenulovým přírůstkem děleným 3.
Pro p>=5 pišme d=pr, a=1+ps a X_0=0. Položení X_n=cn+pY_n modulo p^2
dává

```
Y_(n+1)-Y_n = n^2 c^2 r + nc s (mod p),
Y_n = 2 binom(n,3)c^2r + binom(n,2)(c^2r+cs) (mod p).
```

Oba binomické koeficienty pro n=p jsou dělitelné p; proto
X_(n+p)=X_n+pc modulo p^2. Platnost pro každé n plyne také z komutace
F s posunem o pc modulo p^2, nebo ze stejného výpočtu pro libovolný seed.

**Další zvedání.** Předpokládejme
X_(n+p^f)=X_n+t p^f modulo p^(f+1), kde p nedělí t. Zaveďme Z_n modulo p
vztahem X_(n+p^f)=X_n+t p^f+Z_n p^(f+1) modulo p^(f+2).
Dosazení do F dává

```
Z_(n+1)-Z_n = t(s+2rnc) (mod p).
```

Součet pravé strany přes p po sobě jdoucích indexů je 0 modulo p,
takže Z_(n+p)=Z_n. Tedy také Z_(n+p^f)=Z_n. Po p opakováních posunu
p^f dostaneme X_(n+p^(f+1))=X_n+t p^(f+1) modulo p^(f+2).
V každém kroku se perioda vynásobí p. Tento argument zahrnuje p=2 i 3
po jejich správně ošetřeném prvním zvednutí.

Pozor na lokaci známého errata: oprava 18. 2. 2004 na str. 553 je
na řádku **-2**, v odpovědi 11(c), nikoli ve vzorci pro Z na horním
okraji stránky. Přímá sazba PS tuto polohu potvrzuje.

**Doplňující Coveyouova podmínka pro vyšší stupně.** Pokud F(0) je liché,
F'(j)=1, F''(j)=0 a F(j+1)=F(j)+1 modulo 4 pro j=0,1,2,3, pak Taylorův
rozvoj s celočíselnými koeficienty dává F(x+2)=F(x)+2 modulo 8.
Proto F^4(x)=x+4 modulo 8 a F je plný cyklus modulo 4.
Pro G=F^(2^e), e>=2, je G'(x)=1 modulo 4. Z G(x)=x+2^e t, t liché,
dostaneme G^2(x)=x+2^(e+1)t modulo 2^(e+2); vyšší členy Taylorova
rozvoje zmizí. Tím se plná perioda zvedá na všechny 2^e.
Toto ověřuje matematický obsah poznámky na str. 553; celá citovaná
Coveyouova kapitola není nově přezkoumána.

## 9: upravený middle-square generátor

Na str. 26 je X_0=2 modulo 4, X_(n+1)=X_n(X_n+1) modulo 2^e.
Substituce X_n=4Y_n+2 dává

```
Y_(n+1)=4Y_n^2+5Y_n+1 (mod 2^(e-2)).
```

Kritérium úlohy 8 dává plnou periodu 2^(e-2). Pro e=2 je to triviální
cyklus jediného stavu. Vztah ke středním cifrám na str. 27 také souhlasí:
pro Z_n=2^e X_n má číslo Z_n^2+2^e Z_n tvar 2^(2e)X_n(X_n+1).
Jeho prostředních 2e bitů je tedy 2^e(X_n(X_n+1) mod 2^e)=Z_(n+1).

## 10: Fibonacci modulo mocniny dvou

F_0=0,F_1=1 a F_(n+1)=F_n+F_(n-1). Pro e>1 jsou tištěné indukční
identity správné:

```
F_(3*2^(e-1)) = 0 (mod 2^(e+1)),
F_(3*2^(e-1)+1) = 1+2^e (mod 2^(e+1)).
```

Základ e=2 je (F_6,F_7)=(8,13). Krok plyne z
F_(2n)=F_n(2F_(n+1)-F_n) a F_(2n+1)=F_n^2+F_(n+1)^2.
Modulo 2 má dvojice periodu 3; uvedené identity dokládají přesně
e-1 zdvojení, tedy periodu 3*2^(e-1). Malý přechod modulo 4 lze
ověřit přímo (perioda 6).

Pro X_0=u,X_1=v platí X_n=uF_(n-1)+vF_n. Podmínky návratu dvojice
(u,v) tvoří dvě lineární rovnice pro F_n a F_(n+1)-1 s determinantem
v^2-uv-u^2. Ten je lichý, nejsou-li u,v oba sudé. Rovnice jsou tedy
ekvivalentní návratu Fibonacciho dvojice a perioda je stejná.

## 11: polynomický důkaz zvedání period

Pišme f(z)=1-a_1 z-...-a_k z^k. Kongruence modulo (f,p^e) znamená,
že rozdíl polynomů je f násobek plus polynom se všemi koeficienty
dělitelnými p^e. Není třeba, aby nejvyšší koeficient f byl jednotka;
důležitý je konstantní koeficient f(0)=1.

**(a)** Pokud z^L=1+p^e v modulo f, ale rovnost s 1 neplatí modulo
(f,p^(e+1)), pak v není 0 modulo (f,p). Pro p^e>2 binomický rozvoj dává
z^(pL)=1+p^(e+1)v modulo (f,p^(e+2)). Všechny ostatní členy jsou
dělitelné p^(e+2), včetně mezních případů p=3,e=1 a p=2,e=2.
Člen p^(e+1)v nemůže být nulový modulo (f,p^(e+2)): kdyby f b měl
všechny koeficienty dělitelné p^(e+1), byl by jimi dělitelný i b,
protože f modulo p je nenulový a polynomy nad tělesem nemají nulové
dělitele. Opakované dělení p by dalo v=0 modulo (f,p), spor.

**(b)** Nechť 1/f(z)=sum A_n z^n je formální mocninná řada, tedy
algebraické koeficienty bez předpokladu analytické konvergence.
Její koeficienty jsou eventualně L-periodické modulo p^e právě tehdy,
když (1-z^L)/f(z) je modulo p^e polynom. To je ekvivalentní
z^L=1 modulo (f,p^e), a nejmenší takové L je hledaná perioda.
Tento důkaz zahrnuje i rekurence s přechodným úvodem.

**(c)** Z binomického rozvoje bez nenulového závěru vždy plyne,
že perioda A modulo p^(e+1) dělí p-násobek periody modulo p^e;
projekce dává opačnou dělitelnost bez faktoru p. Při změně se tedy
perioda násobí právě p. Část (a) pro p^e>2 vynutí další násobení p
navždy. Nutnost výjimky potvrzuje tištěný příklad a_1=4,a_2=-1:
periody modulo 2,4,8 jsou 2,4,4.

Známé opravy: 18. 2. 2004 doplňuje d do indexu X_(n+p^(f+1)d)
v posledním argumentu dělitelnosti na str. 553; 28. 4. 2017 doplňuje
lambda do indexu A_(n+p lambda) v alternativním důkazu na str. 554.
Obě jsou správné. Doprovodný návod na str. 37 však nemusí skončit;
úzký nález [C0009](C0009-period-search-termination.md) se týká právě
tohoto návodu, nikoli části (c).

**(d–e)** Generující řada libovolných počátečních hodnot má tvar g/f,
kde koeficient g_n pro 0<=n<k je X_n-sum_(j=1..n) a_j X_(n-j).
Je-li gcd(f,g)=1 modulo p, existuje polynomická Bezoutova identita
bf+cg=1+pH. Vynásobením konečným součtem sum_(j=0..e-1)(-pH)^j
ji zvedneme modulo p^e. Z periodičnosti plyne f|g(1-z^L) modulo p^e;
vynásobení Bezoutovou identitou odstraní g. Perioda je proto přesně
perioda A. Bez podmínky nesoudělnosti ji pouze dělí, protože X je
konečná celočíselná kombinace posunů A.

## 12: afinní rekurence druhého řádu

Rekurence X_(n+1)=aX_n+bX_(n-1)+c má po odečtení sousedních rovnic
homogenní charakteristický polynom (t-1)(t^2-at-b).
Modulo 2 má odpovídající univerzální posloupnost A periodu nejvýše 4:
zbývající kvadratický faktor buď dává jen kořeny 0,1 (největší
násobnost kořene 1 je 3), nebo je t^2+t+1 a dává periodu 3.
Nulové kořeny ovlivní jen úvod. Část 11(b) a binomické zvedání dávají
pro A modulo 2^e periodu nejvýše 4*2^(e-1)=2^(e+1).
Každé konkrétní X má periodu dělící tu univerzální.

Toto je důležité rozlišení: u libovolných počátečních hodnot se po
zvýšení modulu může objevit dříve nulová složka. Není obecně pravda,
že jejich konkrétní perioda při každém zvednutí roste nejvýše dvakrát.
Horní mez zde dokazuje univerzální posloupnost, ne tato silnější domněnka.

Mez je dosažitelná volbou a=0,b=c=1, X_0=X_1=0:
výstup je 0,0,1,1,2,2,... modulo 2^e a má nejmenší periodu 2^(e+1).

## Přesné kontroly

[verify_period_lifting.py](../verify_period_lifting.py) úspěšně ověřil:

- 1 382 976 trojic koeficientů kvadratických map pro všechny m<=48;
  5 623 z nich má plnou periodu, přesně podle kritéria;
- 113 682 počátečních identit modulo p^2 a 32 767 Coveyouových stavů;
- 1 860 period univerzálních lineárních rekurencí, nezávislé polynomické
  certifikáty fH=1-z^L a 3 720 posloupností s různými čitateli g;
- 4 095 Fibonacciho počátečních dvojic a 99 identit rychlého zdvojování;
- všech 1 082 400 stavů 4 680 afinních map druhého řádu modulo 2,4,8,16.

[Výsledky](../results/period-lifting.json), [log](../results/period-lifting.log).
Všechny testy skončily exit 0. Vrstvy errat neobsahují jinou opravu
těchto úloh než obě výše uvedené indexové opravy.
