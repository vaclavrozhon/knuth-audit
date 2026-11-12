# §1.2.6-(40), úloha 58 a q-identity v odpovědi 62

Audit 1. listopadu 2026. Zobrazeny původní s. 65,73,489–491
a opravy `all1-prepre` s. 33, `all1` s. 12. Poslední odstavec
s. 489 navíc zobrazen v měřítku 300. Nález **V1-C0006**
se týká konvergence nekonečného rozvoje, nikoli konečné věty.

## Definice a obory

Pro celé k>=0 definujeme q-binomický koeficient

```text
G(r,k) = product_{i=0}^{k−1}(1−q^(r−i))
                       / product_{j=1}^k(1−q^j),          (Q1)
G(r,0)=1,    G(r,k)=0 pro celé k<0.
```

Pro libovolné reálné r zprvu bereme q>0, q!=1, aby všechny
mocniny byly jednoznačné a jmenovatele nenulové. Algebraické
identity lze chápat také jako identity racionálních funkcí
v q a R=q^r. U nezáporných celých horních indexů se
podíly krátí na polynomy v q, takže se potom dají vyhodnotit
i v kořenech jedničky. V analytické části používáme
0<|q|<1 a pevnou větev q^r=exp(r Log q).

V (40) je k nezáporné celé; tento rozsah explicitně doplňují
errata z 4. října 2021. Při q→1 podíl
`(1−q^a)/(1−q)` konverguje k a, takže (Q1) přechází
v obvyklý C(r,k). Nestačí hovořit o libovolném q v bodech,
kde původní podíl není definován.

## Rekurence, konečná věta, symetrie

Převedení na společný jmenovatel v (Q1) dává obě rekurence

```text
G(r,k) = G(r−1,k)+q^(r−k)G(r−1,k−1)
       = q^k G(r−1,k)+G(r−1,k−1).                         (Q2)
```

Pro celé n>=0 indukce po vynásobení posledním činitelem
1+q^(n−1)x dokazuje

```text
product_{j=0}^{n−1}(1+q^j x)
 = sum_{k=0}^n G(n,k) q^(k(k−1)/2)x^k.                   (Q3)
```

Posun exponentu u nového členu je
`n−1+(k−1)(k−2)/2−k(k−1)/2=n−k`, tedy přesně (Q2).
Pro 0<=k<=n je G(n,k) polynom s nezápornými celými
koeficienty a stupněm k(n−k): v (Q2) první člen má stupeň
k(n−k)−k a druhý stupeň k(n−k), s vedoucím koeficientem 1.
Krajní k=0,n dávají konstantu 1. Mimo [0,n] jde o nulový
polynom, kterému se tento stupeň nepřisuzuje.

Označme `[n]!_q=product_{j=1}^n(1+q+...+q^(j−1))`,
s [0]!_q=1. Pak G(n,k)=[n]!_q/([k]!_q[n−k]!_q),
odkud plyne symetrie k↔n−k. Nahrazení q číslem 1/q
v (Q1) a vytažení mocnin q dává
`G(n,k;q)=q^(k(n−k))G(n,k;1/q)`.

## Dvě konvoluce a negace horního indexu

Rozdělíme součin v (Q3) na prvních r a dalších s činitelů,
kde r,s>=0 jsou celá, a porovnáme koeficient x^n.
Příslušná mocnina q se zkrátí na (r−k)(n−k). Opačné
pořadí obou bloků dává druhou podobu:

```text
sum_k G(r,k)G(s,n−k)q^((r−k)(n−k))
 = sum_k G(r,k)G(s,n−k)q^((s−n+k)k) = G(r+s,n).           (Q4)
```

Při n>=0 mají oba součty podporu 0<=k<=n. Pro pevné
q>0,q!=1 jsou všechny výrazy polynomy v R=q^r,S=q^s.
Shoda pro všechna nezáporná celá r,s znamená shodu na
kartézském součinu dvou nekonečných množin různých hodnot;
postupná polynomiální jednoznačnost rozšiřuje (Q4) na
libovolná R,S, tedy i obecné r,s. Pro n<0 jsou obě strany 0.

Vytažení činitelů `1−q^a=−q^a(1−q^−a)` z (Q1)
a obrácení pořadí dává

```text
G(r,k) = (−1)^k q^(kr−k(k−1)/2) G(k−r−1,k).              (Q5)
```

To je přesně negace horního indexu v odpovědi 58.

## Nekonečný rozvoj: správný obor a V1-C0006

Pro 0<|q|<1 a pevné q^r definujme

```text
F_r(x)=product_{j>=0}(1+q^j x)/(1+q^(r+j)x).               (Q6)
```

Součiny v čitateli i jmenovateli konvergují lokálně
stejnoměrně v x, protože součty absolutních hodnot q^j x
a q^(r+j)x jsou na kompaktních množinách omezené.
Na kruhu |q^r x|<1 nemá jmenovatel žádnou nulu.
Zrušení prvních faktorů dává funkcionální rovnici

```text
(1+q^r x)F_r(x)=(1+x)F_r(qx),    F_r(0)=1.                (Q7)
```

Pro Taylorovy koeficienty c_k z (Q7) plyne
`c_k=(q^(k−1)−q^r)c_(k−1)/(1−q^k)`.
S počátkem c_0=1 tedy

```text
F_r(x)=sum_{k>=0} G(r,k)q^(k(k−1)/2)x^k,
                          |q^r x|<1.                    (Q8)
```

Pro neukončenou řadu jde poměr sousedních členů k −q^r x.
Pro reálné 0<q<1, r nepatřící mezi nezáporná celá čísla,
je poloměr konvergence přesně q^(−r). Pokud r>=0, podmínka
|x|<1 z knihy stačí. Pro záporné r ale může selhat.

**Přesný protipříklad:** q=1/2, r=n=−1, x=3/4.
Podle (Q1) nebo (Q5) je
`G(−1,k)=(−1)^k q^(−k(k+1)/2)`.
K-tý člen v (Q8) proto je (−x/q)^k=(−3/2)^k;
nejde k nule, a řada diverguje. Současně konečný součin
v (Q6) pro j=0,...,N teleskopuje na
`(1+q^N x)/(1+q^−1 x)→2/5`.
Všechny faktory jsou kladné, konečné a nenulové. Není zde
problém větve mocniny ani neurčitý výraz.

Zvětšený sken s. 489 uvádí jen |q|<1 a |x|<1 pro
libovolné reálné n. Relevantní změny odpovědi 58 z 2003
a 2023 opravují úvod a bibliografii, nikoli tuto podmínku.
Prohledány `all1-prepre`, `all1-pre`, `all1`, `err1`
a původní `err1.textxt`, ověřené stažením 1. listopadu 2026;
manifest obsahuje jejich hashe. Proto jde o **confirmed**
v našich zdrojích, bez tvrzení o prvenství nebo ověření
fyzického exempláře. Návrh opravy je v `reports/V1-C0006.txt`.

Nezávislá kontrola standardní formulací: v
[DLMF 17.2.37](https://dlmf.nist.gov/17.2.E37) položme
a=q^(−r), z=−q^r x. Podmínka |z|<1 je právě |q^r x|<1.
Tento odkaz není potřeba pro uvedený elementární protipříklad
ani pro vlastní důkaz (Q7)–(Q8).

Následující Cauchyho forma na s. 490 je správná:

```text
product_{j>=0}(1−q^(j+r+1)x)/(1−q^j x)
 = sum_{k>=0} G(k+r,k)x^k,             |x|<1.              (Q9)
```

Dosadíme do (Q8) r' =−r−1 a x' =−q^(r+1)x a použijeme
(Q5). Opravená podmínka |q^r' x'|<1 se změní přesně na
|x|<1, nezávisle na r. Přímý důkaz lze stejně získat
z funkcionální rovnice součinu v (Q9).

## q-Pfaffova a q-Dixonova identita z odpovědi 62

Nechť m,n>=0 jsou celá, a=m−r+s, b=n+r−s, M=m+n.
V součtu q-Pfaffovy identity rozvineme poslední faktor
pomocí druhé konvoluce (Q4):

```text
G(r+k,M)=sum_j G(k,j)G(r,M−j)q^((r−M+j)j).
```

Součinová identita
`G(a,k)G(k,j)=G(a,j)G(a−j,k−j)` plyne přímo z (Q1).
Vnitřní součet podle k nyní podle první (Q4) dává
G(M−j,n−j). Po zkrácení součinu s G(r,M−j) zbývá

```text
G(r,m) sum_j G(a,j)G(r−m,n−j)q^((r−m−n+j)j)
 = G(r,m)G(s,n).
```

To dokazuje přesně první identitu s. 491, s exponentem
`(m−r+s−k)(n−k)`, jehož chybějící závorku opravují
errata z 28. ledna 1998. Rozšíření na záporná celá m,n
funguje stejnými nulovými případy jako v `rothe-abel.md`.

Pro q-Dixonovu identitu předpokládejme celá l,m,n>=0.
V právě dokázané identitě nahraďme její parametry
`(m,n,r,s,k)` postupně `(m+k,l−k,m+n,n+l,j)`.
Její levá strana pak rozvine součin
G(m+n,m+k)G(n+l,n+k) původního součtu.
Dodatečný exponent je `(l+k−j)(l−k−j)=(l−j)²−k²`.
Po vynásobení původní váhou q^((3k²−k)/2) a po
zkrácení q-faktoriálů tedy dostaneme, s h=l−j,

```text
sum_j [m+n+j]!_q /
       ([2h]!_q [j]!_q [m−l+j]!_q [n+j−l]!_q)
       * sum_k (−1)^k G(2h,h+k)q^(h²+k(k−1)/2).           (Q10)
```

Jen 0<=j<=l a nezáporné argumenty všech faktoriálů
přispívají; ostatní členy mají původní nulový koeficient
a žádný záporný q-faktoriál se nevyhodnocuje.
Po substituci u=h+k je vnitřní součet v (Q10)

```text
(−1)^h q^((3h²+h)/2)
    * product_{i=0}^{2h−1}(1−q^(i−h)),                    (Q11)
```

podle (Q3). Pro h>=1 obsahuje součin faktor 1−q^0=0;
pro h=0 je roven 1. Přežije jen j=l a dostáváme
`[l+m+n]!_q/([l]!_q[m]!_q[n]!_q)`, jak tvrdí odpověď.
Limitou q→1 současně plyne obyčejná Dixonova identita
zadaná v úloze 62. Přímý knižní důkaz je stejný výpočet
s faktoriály a vnitřním součtem (1−1)^(2h).

Historické atribuce Gaussovi, Schweinsovi, Cauchymu,
Jacobimu, Heinemu, Dixonovi, Rogersovi, MacMahonovi
a Dougallovi nejsou samy o sobě důsledkem těchto důkazů.
