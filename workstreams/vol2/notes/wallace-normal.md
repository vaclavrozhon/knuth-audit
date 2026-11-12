# §3.4.1-31: přímé generování normálních veličin

Rozsah: zadání na str.141, odpověď589–590, známá změna citace z8.7.1999.
Strany jsou vizuálně přečteny. [Program](../verify_wallace.py) a
[výsledky](../results/wallace.json) doplňují obecné důkazy níže.

**C0058 potvrzen:** tištěná volba úhlu v31(c) má vždy kladný sinus.
Při přirozeném výstupu prvních682 čísel každého zásobníku to způsobuje
silnou zápornou korelaci součtů bloků vzdálených o dva kroky. Důkaz v§4–5
zahrnuje náhodné afinní permutace, vynechání přibližně2/3 hodnot i uvedené
škálování. Týká se konkrétního návodu na str.590; obecná Wallaceova
konstrukce ani samotné zachování normálního rozdělení tím vyvráceny nejsou.

## 1. Část(a): lineární kombinace a ortogonální matice

Standardní normální veličina má střední hodnotu0, rozptyl1 a
charakteristickou funkci exp(−t²/2); charakteristická funkce je
E(exp(itX)). Pro nezávislé X_i a koeficienty a_i s sum a_i²=1 dostáváme
součin exp(−a_i²t²/2)=exp(−t²/2). Kombinace tedy má stejné rozdělení.
Kniha ekvivalentně používá rotaci roviny. Krajní případ sin(theta)=0
v jejím redukčním důkazu je přímý, bez dělení nulou.

**Ortogonální matice** Q splňuje QQ^T=I a zachovává délky vektorů.
Pro vektor nezávislých standardních normálních veličin má QX opět stejnou
společnou hustotu, protože ta závisí jen na součtu čtverců a |det Q|=1.
Pokud je Q náhodná a nezávislá na X, platí totéž po podmínění Q.
Neříká to, že nový a starý zásobník jsou navzájem nezávislé.

## 2. Část(b): exponenciální růst téměř jistě

Uvažujme X_n=A*X_(n−24)+B*X_(n−55), kde A,B>0, A+B>1.
Funkce A*r^(-24)+B*r^(-55) přísně klesá pro r>0, v1 je>1 a vnekonečnu0.
Má tedy jediný kladný kořen r>1, ve kterém je rovna1.
Charakteristický polynom je z^55−A*z^31−B. Pro jeho kořen z s |z|>=r
musí nastat rovnost v trojúhelníkovém odhadu; jinak by kladná klesající
funkce byla>=1 při |z|>r. Rovnost při |z|=r vynucuje zároveň
exp(24i arg z)=exp(55i arg z)=1. Protože gcd(24,55)=1, je z=r.
Kořen r je jednoduchý, jak plyne i z přísně záporné derivace původní
funkce. Všechny ostatní kořeny mají menší absolutní hodnotu.

Obecné řešení tudíž je C*r^n plus členy menšího exponenciálního řádu.
C je nenulová lineární forma počátečních55 hodnot: pro počátek r^j
je C=1. Při nezávislé normální inicializaci má C nenulový rozptyl,
a tedy C!=0 s pravděpodobností1. To zpřesňuje tištěné tvrzení o růstu;
výjimečné deterministické počátky, například samé nuly, se netvrdí.

Přesně ověřené racionální intervaly šířky10^(-30) dávají

```
A=B=1/sqrt(2): r=1.009061487262140957132040010729...
A=3/5,B=4/5:  r=1.008294653966518170100426261179...
```

Pro první případ se znaménka testují celočíselným polynomem
(r^31+1)²−2r^110, pro druhý3r^31+4−5r^55. Nejde jen o numericky
nalezené kořeny. Návrh proměnlivých úhlů v následujícím odstavci knihy
je výslovně pravděpodobnostní doporučení, nikoli prokázaná kvalita.

## 3. Co je v části(c) správně

Označme N=1024, d=2N=2048. Zásobník tvoří dvě N-složkové části X,Y.
Zobrazení j -> aj+b mod N je permutace právě když gcd(a,N)=1;
liché a tuto podmínku splňuje. Nezávislé permutace obou částí a následné
rotace dvojic proto dohromady tvoří ortogonální matici rozměru d.
Každá nová hodnota vyžaduje dvě násobení a jedno sčítání, kromě řízení,
indexování a sdíleného předvýpočtu.

Součet S=sum(X_j²+Y_j²) je invariant. Normální zásobník by při novém
nezávislém generování měl S s rozdělením chi-square o d stupních volnosti,
tj. rozdělení součtu čtverců d nezávislých standardních normálních hodnot.
Má střední hodnotu d a rozptyl2d. Kniha správně rozpoznává vynucenou
konstantnost S jako statistický nedostatek.

Pro pomocnou standardní normální veličinu W má aproximační čitatel
T=(W+sqrt(2d−1))²/2 přesně E(T)=d a Var(T)=2d−1/2. Pro d2048 je tedy
rozptyl4095.5 místo4096. Třetí kumulant je6d−2 místo8d; kumulant zde
znamená třetí centrální moment. Tištěný text správně říká aproximace,
ne přesná chi-square transformace. Závislosti mezi zásobníky se touto
úpravou obecně neodstraní.

V kódu bylo ověřeno682 všech afinních permutací pro moduly2,4,8,16,32
pomocí nezávislé inverze,18 724 jednotlivých obrazů. Průměry přes posuny
byly ověřeny až pro N1024. Identita zachování normy je také symbolická.

## 4. C0058: korelace před škálováním

V úloze23, na kterou odpověď odkazuje, jsou U,V nezávislé uniformní
veličiny na(0,1), podmíněné U²+V²<=1. Píšeme U=r*cos(phi),
V=r*sin(phi), kde phi je rovnoměrný na(0,pi/2). Tištěné poměry jsou

```
c = (U²−V²)/(U²+V²) = cos(theta),
s = 2UV/(U²+V²)     = sin(theta), theta=2phi.       (1)
```

Tedy s>=0. Po volitelném doporučeném odmítání |c|<1/2 nebo |s|<1/2
je theta rovnoměrný na[pi/6,pi/3] sjednoceno[2pi/3,5pi/6]. Pravděpodobnost
přijetí této úhlové podmínky je1/3. Symetrie a přímý integrál dávají

```
E(c)=0, beta=E(s)=3*(sqrt(3)−1)/pi=0.6990570277... . (2)
```

Bez úhlového odmítání je rovněž E(c)=0 a E(s)=2/pi>0.

Matice J má všechny N² prvky1/N. Je to operátor nahrazující souřadnice
jejich společným průměrem, a platí J²=J. Náhodný posun b dělá průměr
každé afinní permutační matice přesně J, nezávisle na lichém násobiteli.
Proto má celá náhodná aktualizační matice Q střední hodnotu

```
E(Q) = [ 0       beta*J ],
       [ −beta*J  0     ].                         (3)
```

Volby v různých obnovách jsou nezávislé. Pro dvě obnovy proto
E(Q_2 Q_1)=E(Q_2)E(Q_1)=−beta²*diag(J,J).

Nechť po každé obnově odevzdáváme X_0,...,X_(m−1), m=682, a zbytek
zásobníku ponecháme jen pro další výpočet. To je přirozená realizace
pokynu použít asi1/3 z2048 hodnot. Definujme normalizovaný součet
L_t=(X_0+...+X_(m−1))/sqrt(m) v t-tém zásobníku. Začínáme skutečně
nezávislými normálními hodnotami, jak požaduje zadání. Každý zásobník
má sám o sobě stejnou normální hustotu, takže E(L_t)=0 a Var(L_t)=1.
Z(3) a počáteční kovariance I však přesně vychází

```
Cov(L_t,L_(t+2)) = −(m/N)*beta²
                 = −0.3254690004819360133... .     (4)
```

Pro m/N blízké2/3 nezmizí tento jev ani při zvětšování zásobníku.
Pro nezávislé normální výstupy by kovariance disjunktních bloků byla0.
Tak silná korelace součtů přímo narušuje použití generátoru např. pro
náhodné procházky nebo odhady průměrů.

Další názorný invariant je (sum X_j)²+(sum Y_j)²: permutace zachovají
oba součty a společná rotace je otočí jako jedinou dvojici. Tento
invariant sám není nový výrok knihy; vysvětluje přetrvávající mód průměrů.

Doplňkový **přesný** experiment pro N2,4 používá c=±3/5,s=4/5,
všechny afinní permutace a všechny uspořádané dvojice obnov. Přímé
celočíselné násobení matic potvrzuje(4) s beta=4/5 pro všechna m<=N.
To nezávisle kontroluje maticové odvození, nikoli skutečný spojitý integrál(2).

## 5. Důkaz, že škálování v knize vadu nezachrání

Pro každý zásobník položme W=Y_(N−1), kappa=sqrt(2d−1),
a=|W+kappa|/sqrt(2S) a Z=aL. To je **kladná odmocnina** přesně tištěného
a², bez zanedbání vzácných záporných hodnot W+kappa. Součet L neobsahuje
W. Pro normální zásobník je S chi-square(d), E(S)=d, Var(S)=2d.
Směr G/sqrt(S) je rovnoměrný na jednotkové sféře a nezávislý na S.

Sférické momenty, případně symetrie a normální čtvrté momenty, dávají

```
E(L²/S)=1/d,
E(W² L²/S)=1/(d+2).
```

Zrcadlení ve směru L při pevném W,S ukazuje E(Z)=0. Rozvinutí a²
pak dává přesně

```
Var(Z) = (2d−1)/(2d) + 1/(2(d+2))
       = 1−1/(d(d+2)) < 1.                         (5)
```

Odhad je nezávislý na m, pokud L je jednotková lineární forma kolmá k W.
Pomocí ||W+kappa|−kappa|<=|W| a (u+v)²<=2(u²+v²) dostáváme

```
E((Z−L)²)
 <= 1/(d+2) + E((kappa−sqrt(2S))²)/d
 <= 1/(d+2) + (8d+1)/(d(2d−1))
  = 4197581/1719244800 < 1/400.                     (6)
```

Poslední krok používá
(kappa−sqrt(2S))²=(2d−1−2S)²/(kappa+sqrt(2S))²,
jmenovatel>=2d−1 a E((2d−1−2S)²)=8d+1.

Cauchyova nerovnost a(5),(6) nyní dávají

```
|E(Z_t Z_(t+2))−E(L_t L_(t+2))|
 <= sqrt(E((Z_t−L_t)²))*sqrt(E(Z_(t+2)²))
  + sqrt(E(L_t²))*sqrt(E((Z_(t+2)−L_(t+2))²))
 < 1/10.
```

Protože beta²*m/N>8/25, platí **i po tištěném škálování**

```
Cov(Z_t,Z_(t+2)) < −11/50 = −0.22.                  (7)
```

Všechny racionální nerovnosti v(6),(7) ověřuje program přesnými zlomky.
Pro odhad beta stačí sqrt3>1.732 a pi<22/7. Důkaz nevyžaduje simulaci,
zanedbání závislostí ani předpoklad S=2048.

## 6. Reprodukce, oprava a rozsah závěru

Nezávislý experiment používá32 768 nových normálních zásobníků, pro každý
dvě obnovy s tištěnými afinními permutacemi. Úhly vznikají skutečně
odmítáním bodů jednotkového čtverce podle(1), nikoli přímým výběrem
předpokládaného rozdělení theta. Výstupní součty jsou včetně a.
Použitý PCG64 slouží pouze k tomuto nezávislému experimentu.

| varianta | E(Z_0 Z_2), odhad | empirická standardní chyba |
|---|---:|---:|
| tištěná | −0.32746435 | 0.00644830 |
| nezávislé náhodné znaménko sinu | 0.00686835 | 0.00670023 |

Bez škálování je první odhad−0.32734426, ve shodě s přesným(4).
Nejde o důkaz celkové kvality druhé varianty ani o kalibrovaný test
všech závislostí. Invariant S v experimentu souhlasí do9e−16 relativně;
invariant součtů obou polovin do2.2e−14.

**Minimální oprava tohoto problému:** vynásobit s v(1) nezávislým
rovnoměrným znaménkem±1 při každé obnově. Pak E(c)=E(s)=0, tedy E(Q)=0,
a mechanismus(3),(4) zmizí. Ekvivalentní jednoduchá konstrukce vychází
z rovnoměrného bodu celého disku se souřadnicemi obou znamének.
Ortogonálnost, úhlové meze i náklady jednoho páru zůstanou zachovány.
Vlastnosti celého generátoru a dalších korelací stále vyžadují testy.

## 7. Zdroje a kontrola errat

Primární [Brent1997](https://maths-people.anu.edu.au/~brent/pd/rpb170tr.pdf)
byl přečten v§2–8, vizuálně str.7. Obsahuje stejný typ afinních permutací,
chi-square aproximaci a faktor vynechávání3. Jeho implementace mění
matice uvnitř průchodu a připouští také záporné úhly; nezaměňujeme ji
s konkrétním receptem z knihy. Dobová měření rychlosti nereprodukujeme.

Primární [Brent2008,§5.2](https://maths-people.anu.edu.au/~brent/pd/rpb213.pdf)
výslovně řeší E(y_i x_j)=E(q_ij) a doporučuje náhodná znaménka, aby byl
průměr prvků transformace blízký0. Vizuálně přečteny str.2–3; v textu
navíc§5.6–5.8 o zbytkových závislostech a omezení malých zásobníků.
Tato obecná diskuse není prvenstvím C0058 a sama nedokazuje naši přesnou
mez(7). Ta je doložena výše. [Brent1998](https://maths-people.anu.edu.au/~brent/pub/pub185.html)
potvrzuje opravenou bibliografickou citaci; celý jeho20stránkový článek
zde znovu neauditujeme.

Wallace1996, TOMS22,119–127, je potvrzen v primárním
[katalogu jeho domovské instituce](https://users.monash.edu.au/~dld/CSWallacePublications/CSWallace_1976-1996_pseudo-RNG_papers).
Přímý vydavatelský PDF vrátil403; plný původní článek neprohlašujeme za
přečtený. Vlastní matematické ověření31 tím není podmíněno.

Znovu prohledány all2-prepre, all2-pre, all2, err2 i aktuální err2.textxt
pro590,31,Wallace,sine,random sign a související formulace. Jediná změna
31 je8.7.1999: citace Brentova preprintu se nahrazuje LNCS1470(1998),1–20;
původní str.33 errat byla vizuálně ověřena. Znaménko ani tento korelační
problém tam opraveny nejsou. Fyzický nejnovější dotisk a prvenství nebyly
ověřeny. [Anglický návrh](../reports/C0058-wallace-sine-sign-draft.txt)
nebyl odeslán.
