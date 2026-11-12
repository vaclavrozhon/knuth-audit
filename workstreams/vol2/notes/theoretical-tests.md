# §3.3.3-18–28: částečné součty, běhy a spojité modely

Audit1.11.2026 navazuje na [Dedekindovy součty](dedekind.md),
kde jsou definovány psi, sigma a Eukleidovy podíly.
Skeny zadání90–93 a odpovědí574–577 byly přečteny vizuálně.
Všech pět bloků [programu](../verify_theoretical_tests.py)
je dokončeno; [výsledky](../results/theoretical-tests.json)
rozlišují platné vzorce a nalezené výjimky.

**Zbývá obecný důkaz ostré meze discrepancy v komentáři19
a historické atribuce.** Žádný protipříklad této meze
nebyl nalezen; konečná kontrola není její obecný důkaz.
Nové doložené chyby jsou [C0033](C0033-fibonacci-run-table.md),
[C0034](C0034-descending-period-two.md),
[C0035](C0035-continuous-unit-multiplier.md).

## 1. Částečný součet (18)

Pro kladná celá h,k,z a libovolné reálné c definujme
`S(h,k,c,z)=sum_(0<=j<z) psi((hj+c)/k)`.
Váha `floor(j/k)−floor((j−z)/k)` pro `0<=j<k`
počítá, kolikrát se tento zbytek vyskytne v intervalu
0,...,z−1. Identita tedy platí i pro z>=k, nejen pro
z<=k v zadání. Rozvinutí podlah pomocí psi a delta dává

```text
S(h,k,c,z)=zd/k psi(c/d)
 +(sigma(h,k,hz+c)−sigma(h,k,c))/12
 +psi(c/k)/2−psi((hz+c)/k)/2,   d=gcd(h,k).
```

První člen plyne z replikačního zákona, oba krajní
členy jsou přesně příspěvky delta. Přímý součet,
vážený součet po zbytcích a vzorec se shodují v6525
případech, včetně záporného a neceločíselného c,
nesoudělnosti i soudělnosti h,k a několika celých period.

## 2. Počítání v obdélníku (19)

Nechť s(x)=(ax+c) mod m je permutace stavů a
`0<=alpha<beta<=m`, `0<=alpha'<beta'<=m` jsou celá.
Indikátor prvního intervalu lze přesně zapsat

```text
I(x)=(beta−alpha)/m
 +psi((x−beta)/m)−psi((x−alpha)/m)
 +([x=alpha mod m]−[x=beta mod m])/2.
```

Stejný vzorec platí pro s(x) a druhý interval.
Součet každé pilovité funkce je0. Násobení a změny
indexu proto dají přesně čtyři sigma členy odpovědi19
a zbytek epsilon z delta členů. Každý ze dvou
smíšených součinů je podporován nejvýše na dvou
bodech a má absolutní součet nejvýše1; součin
dvou delta rozdílů má absolutní součet nejvýše1/2.
Proto `|epsilon|<=2.5/m`, jak je vytištěno.

Přímé počty a tato formule souhlasí pro27124 obdélníků;
největší pozorované m|epsilon| bylo1. Přesné maximum
odchylky od plochy bylo navíc nalezeno pro všech95
plnoperiodových násobitelů s m<=50. Stačí c1: svislé
posunutí bodů zachovává maximum, protože interval
přecházející přes okraj lze nahradit doplňkem, který
pouze změní znaménko odchylky. Pro každé rozmezí x
je maximum přes y rozdílem maxima a minima přesného
prefixového součtu; nejde o vzorkování obdélníků.

Ve všech těchto modelech platí tvrzená ostrá mez
`sum_j a_j/(4m)`. Přímé dosazení věty K do čtyř sigma
členů však samo odstranění epsilon nevysvětluje.
Obecné odvození této přesné konstanty a komentáře
o opačném odhadu **zůstává otevřenou položkou auditu**.
Bez odstranění epsilon už máme rigorózní mez stejného
řádu `sum_j a_j/(4m)+O(1/m)`.

Pro a řádu sqrt(m) je součet podílů O(sqrt(m)):
první podíl je nejvýše m/a a součet zbývajících
podílů nejvýše a, jak plyne indukcí z Eukleidova
algoritmu. Kvalitativní komentář o O(1/sqrt(m)) je
proto platný i s prokázanou slabší mezí.

## 3. Dva po sobě jdoucí poklesy (20)

Pro plnou periodu m>1 označme
`u=x/m,v=s(x)/m,w=s(s(x))/m`, `b=a−1` a
`f=psi((bx+c)/m),g=psi(a(bx+c)/m)`.
Neexistují pevné body, a tedy indikátory poklesů jsou
`u−v+f+1/2` a `v−w+g+1/2`. Jejich součin má
devět kvadratických členů:

```text
uv−uw+ug−v²+vw−vg+fv−fw+fg.
```

Po nahrazení u,v,w pomocí psi a delta odpovídají
právě S1−S2+S3−S4+S5−S6+S7−S8+S9 v knize.
Změna indexu x na s(x), případně na s(s(x)), dává
u S7/S8 inverzi a modulo m a uvedená znaménka.
Lineární členy u−w se sečtou na0; f i g mají
součet `d psi(c/d)`, kde d=gcd(b,m), protože
a=1 modulo d. To vysvětluje člen d/m psi(c/d).

U S9 se hodnoty bx+c mod m rovnají c0+d j, každá
d-krát, kde c0=c mod d. Plná perioda zaručuje
0<c0<d. Posunutí prvního pilovitého faktoru má
jediný poloviční delta příspěvek u j0; replikační
zákon pak dává přesně vytištěný redukovaný S9.

Krajní příspěvky nulových stavů vedou k poslední
závorce na str.574. Při m2 se ovšem první a třetí
nulový stav shodují; je nutno odečíst další1/(4m).
To je C0034. Přímá kontrola2133 modelů s m<=60
potvrdila všech devět součtů i výjimku; jediný
nesouhlas původního celkového vzorce je m2,a1,c1.

## 4. Spojitá korelace a poklesy (21–23)

Nyní x znamená rovnoměrný bod intervalu[0,1),
`s(x)={ax+theta}`, kde `{z}=z−floor(z)` a
`0<=theta<1`. Násobitel a je kladné celé číslo;
pro22–24 je nutné a>1 (C0035).

Na každém dílčím intervalu mezi body `(j−theta)/a`
je s(x) lineární. Přímá integrace x s(x) dává

```text
integral_0^1 x s(x) dx
 =1/(3a)−theta/(2a)+(a−1)/(4a)+theta²/(2a),
C=(1−6theta+6theta²)/a.
```

Pomocný integrál s_n na str.575 i oprava krajního
intervalu mají správné členy; výsledný vzorec platí
i pro a1.174 přesných integrálů jej ověřilo.

Pro a>1 se oblasti s(x)<x skládají z intervalů
`[(j−theta)/a,(j−theta)/(a−1))`, j1,...,a−1,
a posledního intervalu `[(a−theta)/a,1)`.
Jejich celková délka je1/2 (22). Pro a1 je délka
theta, čímž vzniká výjimka v zadání i odpovědi.

Při dvou poklesech rozdělíme první interval podle
celého čísla odčítaného při druhém kroku. Součty
délek jsou přesně oba součty a poslední max v23.
Označíme-li n=floor(a theta), výsledná pravděpodobnost je

```text
1/6+1/(6a)−theta/(2a)
 +(n(n+1−2theta)/(2(a−1))
   +max(0,{a theta}+theta−1))/a².
```

Obecný rozklad a174 nezávislých přesných průniků
lineárních intervalů potvrzují vzorec i body zlomu.
Asymptotika je stejnoměrná v theta: dosazení
n=a theta−{a theta} dává zbytek O(1/a²).

Přesné minimum lze navíc určit bez asymptotiky.
Mezi zlomy je pravděpodobnost lineární; minima jsou
v bodech theta=j/(a+1), maxima v j/a. Znaménka
směrnic před a po aktivaci členu max jsou záporné
a kladné. Hodnota minima minus1/6 je

```text
(a−2)/(24a(a+1)),  a sudé,
(a−3)/(24a²),      a liché.
```

Proto komentář o nemožnosti dosáhnout1/6 platí pro
a>=4. Výjimky jsou a2 s theta1/3,2/3 a a3 s theta1/2.
Vytištěný asymptotický výrok pro velké a tím není
vyvrácen. Přesné intervaly těchto výjimek jsou v JSON.

## 5. Delší běhy a spojitý obdélník (24/25)

Pro theta0 a a>1 vede t−1 poklesů ke slabě uspořádaným
cifrám `0<j1<=...<=j_(t−1)<a`. Délka příslušného
intervalu je `j1/(a^(t−1)(a−1))`. Součet j1 počítá
volbu další cifry `1<=j0<=j1` a dává
`binom(a+t−2,t)`. Tím dostáváme přesnou pravděpodobnost
`binom(a+t−2,t)/(a^(t−1)(a−1))`, ekvivalentní součinu
v zadání. Pro t1 se ověří přímo hodnota1.

Součet těchto ocasových pravděpodobností podle
binomické řady je
`(a/(a−1))^a−a/(a−1)`; rozvoj logaritmu potvrzuje
`e−1+(e/2−1)/a+O(1/a²)`. Transformace x na1−x
mimo nulovou množinu mění klesání na růst a zachovává
mapu theta0, takže i tvrzení o vzestupných bězích platí.
59 přímých intervalových modelů ověřilo délky až7.

V25 se průnik obdélníku s grafem s skládá z průniků
`[alpha,beta)` a `[(j+alpha'−theta)/a,(j+beta'−theta)/a)`.
Úplné prostřední intervaly a dva případné krajní kusy
dávají vytištěný vzorec s ceil v definicích k0,k1.
Každý krajní kus je nejvýše `(beta'−alpha')/a`,
čímž plyne uvedená mez chyby.12348 přesných průniků
včetně dotyků hranic potvrdilo vzorec a ostrou mez.

## 6. Fibonacciho generátor a potence2 (26–28)

Pro26 označme první dvě hodnoty x,y a třetí z={x+y}.
Pod přímkou x+y=1 je z větší než obě; nad ní menší
než obě. Přímka x=y každou polovinu rozdělí na dvě
čtvrtiny. Dostáváme správné čtyři pravděpodobnosti1/4
a dva nemožné prostřední případy; Fig.A-1 souhlasí.

Pro27 je přesný trojúhelníkový důkaz v C0033.
Správný obecný vzorec i Fig.A-2 se shodují, tabulka
ovšem zaměňuje ocas a přesnou délku. Pro nezávislá
rovnoměrná čísla je podmíněný ocas
`Pr(L>=k)=2k/(k+1)!`: v uspořádání k+1 hodnot má
U0 k možných pozic nad U1. Rozdíl sousedních ocasů
potvrzuje celý vytištěný náhodný řádek.
Nezávislá polygonová rekurence ověřila15 délek.

Pro28 můžeme parametr alpha redukovat modulo1.
Pišme z={alpha+2y−x}, `0<=alpha<=1`, a D=y−x.
Oblast x<y<z má při D>0 dvě části s délkami
`1−alpha−2D` pro `0<D<(1−alpha)/2` a
`2−alpha−2D` pro `1−alpha<D<(2−alpha)/2`.
Integrací vychází `(1−alpha)²/4+alpha²/4`.

Zobrazení (x,y) na(z,y) zachovává plochu a obrací
první a třetí pořadí, protože `x={alpha+2y−z}`.
Proto mají123 a321 stejné pravděpodobnosti;132/312
a213/231 jsou dvě další dvojice. Události x<y
a x>y mají každá pravděpodobnost1/2, takže všechny
čtyři zbylé případy mají `(1/2−Pr(123))/2`.
To dokazuje všechny vytištěné kvadratické výrazy.
Rovnost šesti pravděpodobností1/6 nastává právě pro
`alpha=1/2±sqrt(3)/6` modulo1.47 přesných racionálních
hodnot alpha a všech šest polygonů potvrdilo vzorce.
Fig.A-3 má správné přímky, průsečíky a štítky oblastí.

## 7. Zbývající rozsah

Známé opravy22/23 z2005/1999 jsou zahrnuty.
Čtyři vrstvy errat pro nové nálezy prohledány; podrobnosti
v samostatných poznámkách. [Historický záznam](../sources/theoretical-tests-history.json)
rozlišuje přečtený Coveyouův reprint přes webový extrakt
od nedostupných plných textů Greenberger/Dieter/Franklin.
Obecná matematika výše na těchto nepřečtených zdrojích
nezávisí. Odpověď19 a konec hlavního textu zůstávají
otevřené kvůli přesné mezi discrepancy a jejímu převodu
z věty K; sekci zatím neoznačovat za celou hotovou.


## 8. Otevřená mez19: zpřesnění1.11.2026

Nový [reproduktor](../verify_discrepancy_frontier.py) a
[výsledky](../results/discrepancy-frontier.json) rozšiřují
konečnou kontrolu na všech7805 nesoudělných dvojic
`1<=a<m<=160`, nejen plnoperiodové násobitele.
Žádný protipříklad horní meze nevznikl. Počet obdélníků
se zmenší následující přesnou symetrií: posun x o alpha
přidá a alpha do druhé souřadnice; cyklický interval
přes okraj lze nahradit doplňkem a obrátit znaménko
odchylky. Stačí tedy první interval[0,w) a všechny
rozdíly prefixů ve druhé souřadnici. Stejná symetrie
odstraňuje c. Každý prefix je celočíselný čitatel
`m N−w y`, takže maximum není zatíženo zaokrouhlením.

Následující redukce odstraňuje epsilon **přesně**, ale
obecná mez nového součtu dosud není dokázána. Položme
`r_j=(j+1/2)/m−1/2` a definujme středový součet

```text
tau(a,m,c)=12 sum_(j=0)^(m−1) r_j r_((aj+c) mod m).
```

Pro inverzi a' modulo m přímé rozvinutí dává

```text
tau(a,m,c)=sigma(a,m,c)+6 psi(a'c/m)−6 psi(c/m)
          +3[c=0 mod m]−3/m.                         (T)
```

Poloha hranic mezi body j a j+1 dovoluje zapsat
intervalové indikátory bez delta členů. Vzorec se
čtyřmi sigma v oddílu2 proto platí **bez epsilon**,
pokud každé sigma nahradíme tau. Přímé racionální
součty a obdélníky tuto identitu nezávisle ověřily;
přesné počty jsou v bloku midpoint_identity.

Pro funkci F_a na celých0,...,m definovanou

```text
F_a(n)=sum_(j=0)^(n−1) ((aj mod m)−(m−1)/2)/m,
R(a,m)=max_n F_a(n)−min_n F_a(n)
```

platí `max_c tau−min_c tau=12R(a',m)`.
Důkaz: zvýšení c o1 mění druhý faktor každého sčítance
o1/m, kromě jediného přechodu přes okraj. Součet
prvních faktorů je0; rozdíl tau je tedy−12r_j
pro j=−a'(c+1) modulo m. Cyklus těchto přírůstků
je po obrácení a cyklickém posunutí právě cyklus
přírůstků12F_a'. To zachovává rozsah částečných součtů.

Označme D maximální absolutní obdélníkovou odchylku
pravděpodobnosti od plochy, s celočíselnými hranicemi
v souřadnicích před dělením m. Pak přesně

```text
R(a',m) <= mD <= 2R(a',m).                           (U)
```

Horní mez je součet dvou rozdílů tau. Pro dolní
zvolíme první rozdíl jako maximum minus minimum.
Druhý rozdíl, posunutý o a w, má při průměrování
w=0,...,m−1 nulový průměr. Některý tedy nezmenší
první rozdíl. Cyklické intervaly se pomocí doplňků
převedou na obyčejný obdélník; absolutní odchylka
se nezmění.

K dokončení horní meze by stačilo dokázat
`R(a,m)<=sum_j a_j/8`, kde a_j jsou Eukleidovy
podíly m/a. Inverze a mění pořadí řetězového zlomku
s případnou úpravou koncového1 a jeho součet zachovává.
Všech76115 nesoudělných dvojic m<=500 tuto novou mez
splňuje,2629 dokonce s rovností. To je stále jen
konečná kontrola. Lákavá rekurence
`R(a,m)<=floor(m/a)/8+R(m mod a,a)` je **nepravdivá**:
a3,m4 dává1/2>11/24. Nesmí být použita jako důkaz.

Z(T) je rovněž jasné, že rozpětí tau a sigma se liší
nejvýše o absolutní konstantu. Těsnost věty K proto
přenáší na D správný asymptotický řád, ale přesný
výrok o polovině horní meze zde není uzavřen.

Niederreiter1978, str.1021–1022, byl dostupný jen přes
indexované úryvky: popisuje Dieterův postup a odhad
s nejbližšími celočíselnými podíly a dodatečnými členy.
Přímý soubor vrací bezpečnostní stránku, AMS403.
Tento zdroj tedy zatím nedokládá přesnou konstantu
knihy. Kontrola pokračuje §3.3.4, zatímco19 zůstává
**partial**; nový nález zde není potvrzen.

## 9. Přesné maximum discrepancy a další redukce

Další průchod1.11.2026 zesiluje(U) na **přesnou identitu**

```text
mD = (max_c tau(a,m,c)−min_c tau(a,m,c))/6
   = 2R(a',m) = 2R(a,m).                            (V)
```

Zde D nadále znamená diskrétní obdélníky s celočíselnými
hranicemi před dělením m, nikoli supremum přes libovolné
reálné hranice. To odpovídá zadání19.

Důkaz chybějící rovnosti využívá symetrii
`tau(a,m,c)=tau(a,m,a−1−c)`, kde argumenty bereme modulo m.
V definici tau zaměníme j za m−1−j; oba centrované faktory
změní znaménko. Nechť H je argument maxima a L argument
minima. Pro obdélník s prvním intervalem[0,w) zvolíme

```text
w = a'(a−1−H−L) mod m,
bot = −H mod m, height = H−L mod m.
```

Druhý interval je cyklický interval začínající v bot
a dlouhý height. Čtyři rohy vzorce s tau pak mají argumenty
`H,L,a−1−H,a−1−L`; kladné členy jsou obě maxima a záporné
obě minima. Dostaneme přesně dvojnásobek rozpětí tau.
Přechází-li interval přes okraj, nahradíme jej doplňkem
a změníme znaménko odchylky. Horní mez(U) je tak dosažena.
Záměna dvou souřadnic dává
`tau(a,m,c)=tau(a',m,−a'c)`; rozpětí se nezmění a poslední
rovnost(V) následuje z předchozího vztahu k R.

Nový blok reproduktoru ověřuje symetrii, sestrojený
maximalizující obdélník a(V) pro všechny nesoudělné dvojice
s m<=100; pro m<=60 jej porovnává s nezávislým úplným
hledáním obdélníků. Starší úspěšné bloky zachovává --resume.

Pro další pokus o obecný důkaz definujme
`T(a,m,n)=sum_(j=1)^n ((aj mod m)/m−1/2)` pro0<=n<m.
Je-li `b=floor(an/m)` a `r=an mod m`, přesně platí

```text
T(a,m,n)+T(m mod a,a,b)=r(a+r−m)/(2am).             (W)
```

Při a1 je druhý součet prázdný a definuje se jako0.
Pro n<m a j1,...,n nejsou aj/m celá; počítání bodů
pod přímkou proto dává
`sum floor(aj/m)=nb−sum_(k=1)^b floor(mk/a)`.
Po dosazení součtů aritmetických posloupností a
`n=(bm+r)/a` zůstane(W). Dále
`F_a(n)=T(a,m,n)−r/m+n/(2m)`.
To je přesný Eukleidův algoritmus pro jednotlivé hodnoty,
zatím však ne důkaz požadovaného rozpětí.

Omezení dříve odmítnuté jednoduché indukce na a<m/2
ji nezachrání: a3,m10 dává `R=3/4`, zatímco
`floor(m/a)/8+R(m mod a,a)=3/8+1/3=17/24`.
Samotná knižní mez má v tomto příkladu rovnost.

Dolní komentář lze díky(V) doložit kvantitativně.
Přečtená rovnice(4.28) Knuthova článku1977 dává
`osc(sigma)>=3(A−E)/2−8`, kde A je součet podílů
a E je součet1/q přes liché podíly q. Používá se
reprezentace se sudým počtem podílů, případně rozdělení
posledního q na q−1,1; A se tím nezmění.
Rozdíl tau−sigma z(T) leží mezi−6 a6, a proto

```text
mD >= (A−E)/4−10/3.                               (X)
```

Zvláště `A−2E>=80/3` zaručuje alespoň polovinu vytištěné
horní meze, tedy `D>=A/(8m)`. To dává přesný dostatečný
význam neurčitému komentáři o velkých podílech. Například
při pevném počtu podílů rostoucích do nekonečna je
`E=o(A)` a dolní mez se blíží dokonce A/(4m).
Není nutné vydávat asymptotické „best possible“ za přesnou
rovnost pro každé konečné m.

Vizuálně doplněny str.318–325 článku; další tamní
reciprocity neodstraňují zbývající úkol. **Ostrá horní
mez R<=A/8 stále není obecně dokázána**. Rešerše Pinnerova
článku1997 doložila bibliografii a abstrakt, ale odkazy
na autorský PostScript vracejí404; jeho nepřečtené důkazy
zde nepoužíváme. Následující blok auditu může pokračovat
§3.4.1, zatímco tento přesně vymezený bod zůstává otevřený.

## 10. Další průchod 2. listopadu: dva kroky indukci nezachrání

Označme q1=floor(m/a), r1=m mod a, q2=floor(a/r1)
a r2=a mod r1, přičemž zde r1>0. Ani dvoukroková domněnka
`R(a,m)<=(q1+q2)/8+R(r2,r1)` neplatí. Nejmenší nalezený
protipříklad při neomezeném a je a7,m10: 3/4>17/24.
Omezení a<m/2 nepomůže: a7,m24 má q1=3,q2=2,r1=3,r2=1
a dává 1>5/8+1/3=23/24. Nová konečná kontrola testovala
222 dvojic do osmého protipříkladu; nejde o opakování
staršího sčítání mezí.

[Borda2023](https://arxiv.org/pdf/2303.07796), uložený v
`sources/borda-2023-birkhoff.pdf`, dává v Lemma9 přesný
vzorec pro částečné součty pomocí Ostrowského číslic.
Přečten úvod1–4 a tato formule na12 v textové extrakci;
pozdější důkazy limitních zákonů nebyly předmětem kontroly.
Vzorec sám zde zatím není obecným důkazem ostré konstanty.
Nově užitečná forma cíle: při S_N=T(a,m,N) a
`C_N=S_N+N/(2m)` pro0<=N<m platí `R=osc(C_N)`, neboť
`F_a(N+1)=C_N−(m−1)/(2m)`. K tomu není třeba externí věta.

Zápis uchovává neúspěšné pomocné domněnky, aby se další
průchod neopakoval. §3.3.3-19 a konkrétní konstanta
§3.4.2-16 zůstávají partial; pokračujeme §4.2.
