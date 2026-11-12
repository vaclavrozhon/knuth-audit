# §4.5.2: Harris33, graf35 a extrémní vstupy36

Zadání341/355 a odpovědi645 byly vizuálně zkontrolovány v původním
skenu. Všechny čtyři řady errat prohledány podle stran, úloh i obsahu.
Bez nového nálezu. Úloha33 je výzkumná: níže uzavíráme kontrolu
algoritmu, nejhoršího případu a nalezených výsledků; neoznačujeme
nedoloženou průměrnou asymptotiku za vyřešenou.

## 33: algoritmus a přesné meze

H(u,v) označuje počet dělení Harrisova algoritmu na lichých číslech
u>=v>0, včetně posledního přesného dělení. Píšeme d=gcd(u,v).
Nejprve vypočteme u=pv+r0, 0<=r0<v. Je-li r0 sudé, ponecháme je;
jinak použijeme r=r0-v a q=p+1. V prvním případě q=p a r=r0.
Tak vždy platí u=qv+r, r je sudé, |r|<v a q je liché. Právě jeden
ze dvou sousedních zbytků je sudý, takže volba je jednoznačná.
Při r=0 končíme; jinak zapíšeme |r|=2^e w, kde e>=1 a w je liché,
a nahradíme dvojici (u,v) dvojicí (v,w).

Všechna společná dělení jsou zachována: gcd(u,v)=gcd(v,r)=gcd(v,w),
protože v je liché. Navíc 2w<=|r|<v, takže se menší operand
zmenšuje více než na polovinu. Algoritmus končí správným d a po
prvním kroku je poměr větší než2, tudíž další lichý podíl q>=3.
To potvrzuje přesné tvrzení na341, včetně rovnosti u=v na začátku.

Zesílíme odhad na ostré meze. Při H(u,v)=k platí

```text
v >= (2^k-1)d,                  u >= (2^(k+1)-3)d.       (1)
```

Pro k=1 je to u,v>=d. Při k>=2 má následující dvojice (v,w)
k-1 dělení. Lichá čísla v/d a w/d splňují v>=2w+d. Proto
indukčně v>=(2^k-1)d. Současně u>=v+2w: při q=1 je
u=v+2^e w, při q>=3 je u>=3v-|r|>2v>v+2w. Indukce pro w
dá i druhou nerovnost(1).

Obě meze se současně rovnají pro

```text
(u,v) = (2^(k+1)-3, 2^k-1),  k>=1.                     (2)
```

Pro k>=2 první krok s q=1 přejde na (2^k-1,2^(k-1)-1).
Následují q=3 a záporné zbytky -2(2^(j-2)-1), až do dvojice
(3,1); případ k=1 je (1,1). Tím jsou doloženy i nejmenší součet
3*2^k-4 a ostré meze H<=floor(lg(v/d+1)),
H<=floor(lg(u/d+3))-1. Symbol lg je logaritmus o základu2.

Toto je vlastní rozvedení argumentu z původního
[Harrisova článku,102–103](https://www.fq.math.ca/Scanned/8-1/harris1.pdf),
který byl přečten celý v sazbě. Jeho příklad (28567,3829) dává gcd7
ve4 děleních; běžný Eukleides potřebuje6 a nejbližší celočíselné
podíly5. Článek sám neobsahuje analýzu průměru.

Pro nejvýše Nbitové vstupy má obyčejná implementace O(N²)
bitových operací. Máme O(N) dělení. Při aktuálních délkách a>=b
stojí školní dělení O(N(a-b+1)); další délka prvního operandu
je právě b. Součet rozdílů a-b teleskopuje na nejvýše N.
Součet odstraněných exponentů e je nejvýše lg(v/d), protože
nový menší operand je menší než v/2^e. I jednotlivé bitové
posuny, porovnání a opravy znaménka tedy vyžadují O(N²).
To není tvrzení o nejlepší dostupné implementaci ani průměrné ceně.

## Harris versus dvě Eukleidovy varianty

[Rieger1976,196](https://www.fq.math.ca/Scanned/14-3/rieger-a.pdf)
a [pokračování200](https://www.fq.math.ca/Scanned/14-3/rieger-b.pdf)
byly přečteny v sazbě. E(a,b) níže značí počet běžných dělení,
N(a,b) počet dělení s podílem zaokrouhleným k nejbližšímu celému
číslu. Obě počítání zahrnují poslední přesné dělení. Jeho první
konstrukci lze přímo ověřit: c_j=6*2^j-5 splňuje

```text
c_j=3c_(j-1)-2c_(j-2),    c_j=2c_(j-1)+5.
```

První rovnost dává H(c_k,c_(k-1))=k. Druhá dává E<=5:
po prvním dělení zbývá nejvýše dělení číslem5 a jeho zbytkem.
Při k=1 jde přímo o (7,1). Tedy poměr počtů dělení není
shora omezen konstantou ve prospěch Harrise.

Opačný rozdíl dokládá Riegerova druhá konstrukce: pro libovolné
s existují liché vstupy s H=2 a N>s (také E>s). V ověřovacím
skriptu je přepsána s přesnými celými čísly pro sudá k=2..100.
Její algebraické invarianty a důvod dlouhých běhů jsou následující.
Definujme Pellova čísla P0=0,P1=1,P_(j+1)=2Pj+P_(j-1),
K=4k+3. Zvolíme liché r_(k+1) v (0,2P_(k+1)), které splňuje

```text
P_(k+1)r_k + P_k r_(k+1) = 2^K.
```

Existence a jednoznačnost této volby plyne z gcd(Pk,P_(k+1))=1,
lichosti P_(k+1) a dvou reprezentantů opačné parity. Je r_k
sudé a r_k>2r_(k+1): stačí
2^K>2P_(k+1)(Pk+2P_(k+1)), což plyne z Pj<3^(j-1) pro j>=2
a 2^(4k+3)>5*9^k. Rekurze r_j=2r_(j+1)+r_(j+2) dává
r_j>2r_(j+1), r_j liché právě pro liché j a invariant
P_(j+1)r_j+P_jr_(j+1)=2^K. Zvláště 2r1+r2=2^K.

Položíme y=2*2^K+r1, x=3y+2^K. Harrisův první zbytek je
2^K, jeho lichá část1, takže H=2. Běžné i nejbližší podíly
začínají3,2,2,... a zbytky jsou 2^K,r1,r2,...: všechny dotčené
poměry zbytků jsou menší než1/2. Obě varianty proto vykonají
více než k kroků. To také vysvětluje, proč nelze průměrný výkon
rozhodnout jen porovnáním dvou nejhorších případů.

Riegerův výrok o neznámém průměru je výrokem z roku1976.
Rešerše2026-11-02, zaznamenaná v `sources/harris-research.json`,
nenašla rigorózní průměrnou asymptotiku pro právě tuto variantu.
Novější nalezené implementační/experimentální práce takový důkaz
nedokládají. Jde o omezený výsledek rešerše, nikoli důkaz, že
žádná publikace neexistuje. Knuthova výzkumná otázka33 není
nepravdivým matematickým tvrzením; audit jejího rozsahu je uzavřen.

## 35: nejdelší cesta v grafu délek

Vrchol (m,n) zaznamenává podlahy lg obou lichých operandů před
odečtením. Hrana vyjadřuje existenci nějakého vhodného páru,
ne zachování stejného páru podél libovolně složené cesty.
Z již ověřené tabulky20 dostáváme pro m>=n přesně tyto podpory:

- m=n: Stop a (n,r),(r,n) pro 0<=r<=n-2; při n=0,1 jen Stop.
- m>n=0: (r,0) pro 0<=r<m.
- (m,n)=(2,1): pouze (0,1).
- ostatní m>n>0: všechny (r,n) pro 0<=r<m.

Případy m<n vzniknou prohozením souřadnic. Každá hrana kromě
Stop snižuje jejich součet, takže je graf bez orientovaných cyklů.
Nechť L(m,n) je délka nejdelší cesty do Stop. Indukce dává

```text
L(m,n)=m+floor(n/2)+1-[m=n=1],  m>=n,                    (3)
```

kde hranatá závorka je1 při pravdivé podmínce, jinak0.
Pro (0,0),(1,1) je L=1; pro (2,1) je L=1+L(1,0)=3.
Při m>=n+2 má maximum následníků hodnotu L(m-1,n), ostatní
jsou nejvýše tak velké, a přičtení1 dává(3). Totéž platí
pro n=0. Při m=n+1,n>=2 dosahuje maxima následník(n,n).
Při m=n>=2 dosahuje maxima (n,n-2), s hodnotou
n+floor((n-2)/2)+1=n+floor(n/2); další hrana dá(3).

Například graf má cestu (2,2),(2,0),(1,0),(0,0),Stop délky4,
zatímco skutečný algoritmus z dvou lichých3bitových čísel
udělá nejvýše3 odečtení. Hrany existují, ale jejich jednotliví
svědci nemusejí navazovat. Přesně tento rozdíl popisuje odpověď35.

## 36: vstupy dosahující skutečného maxima

Definujme a_j=(2^j-(-1)^j)/3. Platí a0=0,a1=a2=1,
a_j=a_(j-1)+2a_(j-2) a a_j+a_(j+1)=2^j. Pro j>=1 jsou
a_j lichá. Počet odečtení B včetně posledního nulového
označíme S(u,v); odstranění mocniny2 v kterémkoli operandu
jej nemění.

Nejprve S(a_j,a_(j+1))=j pro j>=1. Případ j=1 je (1,1).
Pro j>=2 rozdíl sousedních členů je2a_(j-1); po jednom
posunu vznikne předchozí sousední dvojice, takže platí indukce.

Při m>n>=1 knižní dvojice
u=2^(m+1)-a_(n+2), v=a_(n+2) má předepsané délky.
Prvních m-n odečtení s jediným posunem nahradí postupně
první člen výrazem2^m-a_(n+2),...,2^(n+1)-a_(n+2)=a_(n+1).
Zbývá sousední dvojice s n+1 odečteními, celkem m+1.

Při m=n>=1 znění po opravě2005 dává
u=a_(n+2), v=u+(-1)^n=2a_(n+1). Po počátečním posunu
jde opět o sousední dvojici a S=n+1. Oba vstupy mají délku
n+1 bitů. Původní konstrukce max/min těchto dvou čísel
je tatáž neuspořádaná dvojice: a_(n+3)=a_(n+2)+2a_(n+1).
Změna2005 je tedy zjednodušení, ne nový chybný příklad.
Dodatek2020 o Brocardovi je bibliografický. Následná kontrola
původních stran 145–147 potvrdila posloupnost i rekurzi;
přesný rozsah je v `gcd-context.md`.

Druhá dvojice u=2^(n+1)-2,v=2^(n+1)-1 se po počátečním
posunu a prvním odečtení změní na (2^n-1,1). Zbytek tvoří
posloupnost2^n-1,2^(n-1)-1,...,1. Má B=1,C=n+1,D=2n,E=n
ve značení programuB. Obecný důkaz tohoto nejhoršího času je
už v `gcd-basic.md`; zde byla kontrolována shoda s odpovědí36.

## Nezávislé konečné kontroly

`verify_gcd_extremal.py` a `results/gcd-extremal.json`:
131328 lichých uspořádaných vstupů do1023, minima pro k1..9;
400 dalších Harrisových extrémů do k200 a50 protichůdných
Riegerových konstrukcí. Dále4753 vrcholů délkového grafu do96,
561 porovnání podpor s již ověřenou tabulkou,8256 konstrukcí36,
128 porovnání původního/opraveného příkladu,128 časových extrémů
a24 větších dvojic do2049bitů. Všechny tři checkpointy prošly,
relace23874 skončila exit0. Tyto testy doplňují uvedené obecné
důkazy; nenahrazují je ani necertifikují průměrnou asymptotiku.
