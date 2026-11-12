# §4.5.3: Dixon, Porter a Collins na stranách 372–373

Kontrola 3. listopadu 2026. Rovnice (63) má vlastní důkaz
níže, v přesném modelu průměrování podle délek vstupů a gcd.
Porterův asymptotický výsledek (60) je porovnán s novějším
primárním článkem; jeho původní důkaz se zde nenahrazuje
číselným experimentem. Dva nové drobné nálezy jsou
[C0145](C0145-dixon-epsilon-range.md), rozsah epsilon, a
[C0146](C0146-variance-of-mean.md), rozptyl již zprůměrované
veličiny. Historický dodatek o Lochsovi následně uzavřen v [euclid-lochs.md](euclid-lochs.md).

## 1. Pevný jmenovatel a konvence počítání kroků

T(u,v) je počet všech dělení v knize, včetně případného
počátečního nulového podílu. Pro 0<m<n označme s(m/n)
délku kanonického řetězového rozvoje [0;a_1,...,a_s],
s posledním podílem a_s>=2. Platí přesně

```
s(m/n)=T(n,m)=T(m,n)-1.
```

Pro n>1 proto tau_n z (48) je o 1 větší než průměr s(m/n)
přes čitatele nesoudělné s n. Bykovskii–Frolenkov2017,
strany 644–646, vzorce (1)–(3), používají právě s a uvádějí
Porterův výsledek s konstantou C_P-1 a chybou
O_epsilon(n^(-1/6+epsilon)). Jejich C_P po dosazení
zeta(2)=pi^2/6 je přesně C z knižního (61). Zde zeta(s)
značí součet sum_(j>=1)j^-s pro s>1; O_epsilon dovoluje
konstantu závislou na pevném epsilon. Posun +1 tedy
v (60) souhlasí; není to chyba konstanty.

Článek současně vyslovuje silnější vlastní Theorem 2
pro tento průměr. Zde byl čten úvod a přesná tvrzení,
nikoli celý čtyřicetistránkový důkaz. Webový nástroj zpřístupnil
text PDF; místní stažení selhalo HTTP403 a obrázky se nepodařilo
získat. Otevření Porterova vydavatelského PDF vedlo jen
na bibliografickou stránku. **(60) je proto externě doložená
věta se zkontrolovanou normalizací, ne vlastní nový důkaz.**

Kniha správně předchozí odhady označuje za heuristické a
až v (60) přechází k větě. Numerické C a D z (61)/(62)
už byly certifikovány v `euclid-discrete.md`; testy se neopakovaly.
Tamní přesné konvoluce navíc dokazují, že z (60) plyne (62).
Nortonův vydavatelský záznam potvrzuje rok1990, svazek10,
strany53–58 a výsledek pro nezávisle rovnoměrné vstupy
ve čtverci. Celý Nortonův článek zde nebyl přečten.

## 2. Elementární hustota dvojic s mnoha děleními

Pro následující důkaz označme D(a,b)=T(a,b) pro a>=b>=1.
Nechť l=D(a,b), d=gcd(a,b), a_1=a, a_2=b a

```
a_i=q_i a_(i+1)+a_(i+2),
a_(l+1)=d, a_(l+2)=0, q_i>=1.
```

Posloupnost q_1,...,q_l,d jednoznačně určuje dvojici (a,b)
a splňuje a>=d product q_i. Počet L_l(X) dvojic 1<=b<=a<=X
s l děleními je proto pro každé reálné s>1 nejvýše

```
L_l(X) <= X^s zeta(s)^(l+1),
zeta(s)=sum_(j>=1) j^-s.
```

To plyne sečtením (X/(d product q_i))^s přes všechny kladné
celočíselné seznamy; platné seznamy jsou jen podmnožina.
Dvojice s D(a,b)<(ln a)/2 patří mezi seznamy l<(ln X)/2.
Geometrický součet tedy dává pro pevné s

```
# {bad pairs} = O(X^(s+(ln zeta(s))/2)).               (A1)
```

Vezměme s=3/2. Součet prvních pěti členů a integrál zbytku
od5 ukazují zeta(3/2)<2.657<8/3<e. Všechny tyto meze jsou
elementární: členy s odmocninami lze shora omezit
1,.354,.193,.125,.090 a integrál 2/sqrt(5)<.895;
e>1+1+1/2+1/6+1/24=65/24>8/3.
Exponent v (A1) je tedy 2-delta s nějakým delta>0.
Špatných dvojic je o(X^2). To je úplný potřebný slabý
Dixonův odhad; nepotřebujeme silnou koncentraci z roku1970.

Původní Dixon1971, strany374–376, byl přečten ze skenu.
Jeho ostřejší číselný odhad 5X^1.99 není pro náš důkaz nutný.
Jeho rekapitulace silného výsledku má tutéž vadu rozsahu
epsilon jako kniha, viz C0145.

## 3. Cena konkrétního běhu klasického algoritmu

Zafixujme celočíselný základ beta>=2. Délka kladného celého
čísla x je L(x)=1+floor(log_beta x). Položme
m=L(a), n=L(b), k=L(d). Znak Theta znamená dvě kladné
konstantní meze, nezávislé na a,b,m,n,k; smějí záviset
na pevném základu a klasické implementaci. O značí horní
a Omega dolní takovou mez.

Školní dělení má cenu Theta(L(q_i)L(a_(i+1))). Přesuny
a testy mají nejvýše stejný řád, jak plyne i z již
zkontrolované §4.3.1. Celý běh má tedy cenu úměrnou

```
W(a,b)=sum_(i=1..l) L(q_i)L(a_(i+1)).                 (A2)
```

Pro neterminální kroky q_i+1<a_i/a_(i+2), zatímco
q_l=a_l/d. Teleskopické násobení dává

```
product_(i=1..l)(q_i+1) <= 2ab/d^2.
```

Součet L(q_i) je nejvýše konstantní násobek
sum ln(q_i+1), tudíž O(1+ln(a/d)). Proto

```
W(a,b)=O(n(m-k+1)).                                  (A3)
```

Rovnost a=b s jediným podílem1 je zahrnuta. Dolní meze
užitečné později jsou

```
W(a,b) >= c_1 n(m-n+1),
W(a,b) >= c_2 (l^2+kl),                              (A4)
```

pro pevné c_1,c_2>0. První plyne z prvního dělení:
délka floor(a/b) je srovnatelná s m-n+1, včetně m=n.
Pro druhou stačí L(q_i)>=1 a zpětné Fibonacciho meze
a_(l+1-r)>=d F_(r+2), r=0,...,l-1, kde F_0=0,F_1=1
a F_(j+2)=F_(j+1)+F_j. Součet délek těchto kladných zbytků
je Omega(kl+l^2), včetně malých l,k po úpravě jediné konstanty.

## 4. Průměr při pevných délkách

Collinsův přesný pravděpodobnostní prostor je rovnoměrné
rozdělení na konečné neprázdné množině

```
S_(m,n,k)={(a,b): a>=b>=1, L(a)=m, L(b)=n,
                       L(gcd(a,b))=k},
m>=n>=k>=1.                                         (A5)
```

Neprázdnost: pro n=k vezmi a=beta^(m-1),b=beta^(k-1);
pro n>k vezmi a=beta^(m-1)+beta^(k-1),b=beta^(n-1).
Obě konstrukce mají gcd=beta^(k-1).

Ukážeme, že kladný podíl této množiny má l=Omega(n-k),
rovnoměrně pro n-k dost velké. Položme h=n-k,
v=beta^h a u=ceil(beta^(h+1/2)). Interval [v,u) obsahuje
w=u-v=Theta(beta^h) celých čísel. Počet Q nesoudělných
uspořádaných dvojic v tomto intervalu splňuje

```
Q=w^2/zeta(2)+O(w log u+u).                          (A6)
```

Důkaz: počet násobků j v intervalu je w/j+O(1).
Möbiova inverze, tedy součet mu(j) krát čtverec tohoto počtu,
dává chybu O(w sum_(j<=u)1/j+u); ocas sum j^-2 je O(1/u).
Funkce mu(j) je Möbiova funkce z úlohy28 a
sum mu(j)/j^2=1/zeta(2). Protože u=Theta(w), hlavní člen
dominuje. Po omezení na a_0>b_0 a odečtení o(u^2)
výjimek z (A1) zbývá Omega(beta^(2h)) dvojic s

```
gcd(a_0,b_0)=1, D(a_0,b_0)>=(ln a_0)/2.
```

Pro každé celé d s beta^(k-1)<=d<beta^(k-1/2) dostaneme
A=d a_0, B=d b_0 s L(A)=L(B)=n a gcd(A,B)=d.
Takových d je alespoň (sqrt(beta)-1)beta^(k-1).
Zobrazení je prosté: d lze zpětně získat jako gcd.
Celkem jde o Omega(beta^(2n-k)) dvojic (A,B).

Pro m>n každou dvojici převedeme na (qA+B,A), přičemž q
volíme tak, aby první číslo mělo délku m. Počet takových q
je alespoň (beta-1)beta^(m-n-1), protože A<beta^n a
interval pro první číslo má délku beta^m-beta^(m-1).
Tato dolní mez je celé číslo. První dělení obnoví B,
takže i toto zobrazení je prosté a počet kroků se zvýší o1.
Pro m=n zachováme původní dvojici. V obou případech máme
Omega(beta^(m+n-k)) prvků (A5) s l=Omega(n-k).

Naopak |S_(m,n,k)|<=beta^(m+n-k+2): stačí počítat všechna
d<beta^k, a/d<beta^(m-k+1), b/d<beta^(n-k+1).
Dobré dvojice tedy tvoří podíl omezený zdola kladnou
konstantou závislou jen na beta. Z (A4) jejich cena
je Omega(n(n-k)). Průměr má navíc první dolní mez (A4)
pro každý vstup. Dohromady

```
E_S W = Omega(n(n-k)+n(m-n+1))=Omega(n(m-k+1)).        (A7)
```

Je-li n-k omezené konstantou potřebnou výše, samotné
první dělení dává stejný výsledek po změně konstanty.
S (A3) je dokázána Collinsova věta pro všechny m>=n>=k>=1.

## 5. Překlad na (63) a hranice tvrzení

V třídě (A5) je m-k+1 srovnatelné s 1+ln(a/d) a n
s 1+ln b. Celková průměrná cena je tedy řádu

```
(1+ln(a/d))(1+ln b).
```

Pro b>=2 lze druhý faktor nahradit ln b. To dává právě
(63), symetricky s a=max(u,v), b=min(u,v). Pro b=1
musí zůstat přidaná1; doslovné ln1 by cenu anulovalo.
Tuto okrajovou výluku zde vymezujeme, ale nezakládáme
samostatný nález v asymptotickém tvrzení o víceciferných vstupech.

Nejde o dolní mez každého běhu: pro a=2^r+1,b=2^r,r>=1
jsou jen dva podíly 1,2^r a binární W=2r+2. Pravá strana
(63) je Theta(r^2). Kniha však výslovně říká průměrná cena,
takže tento příklad není jejím protipříkladem.

Celý Collins1974 byl přečten textově, strany6–10 vizuálně.
V původním článku jsou drobné tiskové vady (např. převrácená
hodnota 6/pi^2 ve (32)/(33) a „at most“ v jednom kroku
Theorem7); výše uvedený důkaz potřebné meze odvozuje správně.
Tyto vady cizího článku se nezapočítávají jako nálezy v TAOCP.

Všechny čtyři vrstvy errat na372–373 a aktuální TeX byly
prohledány. Zdrojové soubory, otisky, nedostupné části a přesný
rozsah čtení jsou v [euclid-average.json](../sources/euclid-average.json).
Nevznikl nový numerický běh; všechny zdejší dolní/horní meze
jsou obecné, starší úspěšné certifikáty se neopakovaly.

