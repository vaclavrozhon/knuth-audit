# §1.2.6: Stirlingova čísla a změna báze polynomů

Audit 1. listopadu 2026, třetí vydání, první dotisk. Původní
stránky 65–69,72–74,487,489–491 byly zobrazeny. Níže jsou důkazy
matematických tvrzení (44)–(58), tabulky 2 a úloh 32,35,39,55,61,64.
Analytické formule (59)–(60) řeší zvláštní poznámka.

## Definice, rekurence a tabulka

Padající mocnina `x_[n]=x(x−1)...(x−n+1)` a rostoucí mocnina
`x^[n]=x(x+1)...(x+n−1)` jsou pro celé n>=0 polynomy;
obě mají při n=0 hodnotu 1. Stirlingova čísla prvního druhu
`c(n,k)` a druhého druhu `S(n,k)` definujeme změnou báze

```text
x_[n] = sum_k (−1)^(n−k)c(n,k)x^k,
x^n   = sum_k S(n,k)x_[k].                                  (S1)
```

Pro n>=0 je rozsah součtu 0<=k<=n; mimo něj mají obě čísla
hodnotu 0. První rodina je neznaménková, jako hranaté závorky
v knize. Druhá odpovídá složeným závorkám. Polynomy x_[k]
mají různé stupně a vedoucí koeficient 1, proto je definice
jednoznačná. Z násobení první rovnosti činitelem x−n a druhé
rovnosti x, s použitím `x x_[k]=x_[k+1]+k x_[k]`, dostaneme

```text
c(n+1,k) = n c(n,k)+c(n,k−1),
S(n+1,k) = k S(n,k)+S(n,k−1),                              (S2)
c(0,k) = S(0,k) = [k=0].
```

Úloha 32 vznikne nahrazením x číslem −x v první rovnici (S1)
a vytažením (−1)^n: `x^[n]=sum_k c(n,k)x^k`. Úloha 35
žádá právě obě rekurence (S2); odvození výše zahrnuje i krajní
indexy po zavedení nulových koeficientů mimo 0<=k<=n.

Zápis [P] má hodnotu 1, když výrok P platí, jinak 0. To dokazuje
(46). Rekurence současně ukazují kombinatorický význam: novou
značku permutace vložíme za jednu z n původních značek v jejích
cyklech, nebo založíme nový jednoprvkový cyklus. Nový prvek
rozkladu množiny vložíme do jednoho z k bloků, nebo vytvoříme
nový samostatný blok. Proto c(n,k) počítá permutace s k cykly
a S(n,k) rozklady do k neprázdných bloků. Prázdná množina má
jeden rozklad do nuly bloků. Úloha 64 i oprava její počáteční
podmínky v odpovědi z 4. října 2021 jsou tím ověřeny.

Postupné použití (S2) dává přesně oba trojúhelníky tabulky 2
pro n=0,...,8; doslovné hodnoty jsou také vstupem samostatné
aritmetické kontroly. Například řádky n=8 jsou

```text
c: 0, 5040, 13068, 13132, 6769, 1960, 322, 28, 1;
S: 0,    1,   127,   966, 1701, 1050, 266, 28, 1.
```

Dosazení n=5 do (S1) dává oba otištěné rozvoje:

```text
x_[5] = x^5−10x^4+35x^3−50x²+24x,
x^5 = x_[5]+10x_[4]+25x_[3]+15x_[2]+x_[1]
    = 120C(x,5)+240C(x,4)+150C(x,3)+30C(x,2)+C(x,1).
```

Zde C(x,k)=x_[k]/k! je binomický koeficient pro celé k>=0.

## Inverze a jednoduché hodnoty (47)–(53)

Složením obou změn báze (S1) v obou pořadích získáme (47).
Znaménka se mohou přesunout mezi faktory: dvě příslušná
uspořádání se liší činitelem (−1)^(n−m), který na nenulové
pravé straně, kde n=m, činí 1. Tím je současně dokázána
odpověď 55 o inverzích každého konečného hlavního podbloku
obou trojúhelníkových matic. Totéž platí pro nekonečné matice,
protože každý koeficient jejich součinu je konečný součet.

(48)–(50) vyplývají z (S2) nebo z uvedeného počítání. Pro
S(n,n−1)=c(n,n−1)=C(n,2) spojíme jedinou dvojici prvků.
Jednocyklových permutací n+1 značek je n!, a rozklad do
dvou neprázdných nepojmenovaných bloků lze vytvořit
`(2^(n+1)−2)/2=2^n−1` způsoby. Tak jsou zahrnuty i n=0
a rohové hodnoty c(0,0)=S(0,0)=1.

První (51) dostaneme porovnáním koeficientů x^m v
`(x+1)^[n]=x^[n+1]/x`. Nejde o problém při x=0: pravý
podíl je polynom po zkrácení faktoru x. Druhá (51) vzniká
opačným posunem x→x−1 v téže polynomiální identitě.

V rozkladu n+1 prvků do m+1 bloků vybereme k prvků, které
neleží v bloku obsahujícím poslední prvek. Zbylých k prvků
rozdělíme do m bloků. Tím vzniká první (52):
`sum_k C(n,k)S(k,m)=S(n+1,m+1)`. Binomická inverze, již
dokázaná pomocí konečných diferencí, dává druhou (52).

Počet surjektivních zobrazení n-prvkové množiny do m-prvkové
množiny je m!S(n,m). Princip inkluze a exkluze podle chybějících
hodnot dává `sum_k C(m,k)(−1)^(m−k)k^n`, tedy (53).
Konvence 0^0=1 je zde správná: existuje jediné zobrazení
prázdné množiny do prázdné množiny.

V úloze 39 položení x=1 do rostoucího rozvoje dává součet
c(n,k)=n!. Dosazení x=−1 dává střídavý součet
`[n=0]−[n=1]`. Součet S(n,k) počítá všechny rozklady
množiny; ty jsou v bijekci s relacemi ekvivalence, jejichž
třídy jsou právě bloky rozkladu.

## Diagonální polynomy a dualita (57)–(58)

Pro celé d>=0 označme `P_d(n)=c(n,n−d)` a
`Q_d(n)=S(n,n−d)` zatím pro n>=0. Rekurence (S2) dávají

```text
P_d(x+1)−P_d(x) = x P_(d−1)(x),
Q_d(x+1)−Q_d(x) = (x+1−d)Q_(d−1)(x).                      (S3)
```

Začínáme P_0=Q_0=1; pro d>0 vyžadujeme P_d(0)=Q_d(0)=0.
Každý polynom má polynomiální antidiferenci, jednoznačnou
až na konstantu: například `Delta C(x,j+1)=C(x,j)`.
Indukce podle d proto konstruuje jednoznačné polynomy
P_d,Q_d stupně 2d s vedoucím koeficientem `1/(2^d d!)`.
Souhlas s celočíselnými hodnotami zajišťuje (S3) a počátek.
Tím je tvrzení o polynomiálním pokračování skutečně dokázáno.

Polynom R_d(x)=P_d(d−x) splňuje druhou rekurenci (S3):

```text
R_d(x+1)−R_d(x)
 = −(d−x−1)P_(d−1)(d−x−1)
 = (x+1−d)Q_(d−1)(x).
```

Pro d>0 navíc R_d(0)=P_d(d)=c(d,0)=0. Jednoznačnost dává
`Q_d(x)=P_d(d−x)`, čili (58), kdykoli rozdíl horního
a dolního indexu je nezáporné celé číslo. Tato formulace
nevymýšlí hodnoty mimo obor právě definovaného pokračování.

V (57) ověříme dosazením do (S3) a hodnotou v n=0:

```text
P_2(n) = C(n,4)+2C(n+1,4),
P_3(n) = C(n,6)+8C(n+1,6)+6C(n+2,6).
```

Dualita a negace horního indexu binomického koeficientu pak
dají Q_2,Q_3 se správně obrácenými koeficienty 1,2 a 1,8,6,
přesně jako v knize.

## Identita (54) pomocí interpolace

Fixujme celé d>=0. Polynom `f(x)=Q_d(d+x)` má stupeň 2d
a v uzlech x=−d,...,−1 je nulový, protože odpovídá
S(d+x,x) se záporným dolním indexem. Lagrangeova interpolace
na všech 2d+1 uzlech −d,...,d je jednoznačné vyjádření
polynomu jeho hodnotami v uzlech. Váha hodnoty f(k), k>=0,
při vyhodnocení v x=−n je

```text
product_{−d<=j<=d, j!=k} (−n−j)/(k−j)
 = C(d−n,d+k) C(d+n,d−k)
 = C(d−n,d+k) C(d+n,n+k),       n>=0.                      (S4)
```

První rovnost napravo se ověří rozdělením součinu u k
a vytažením znamének; platí i když některý činitel je nula.
Druhá používá celočíselnou symetrii. Protože
f(−n)=Q_d(d−n)=P_d(n), (S4) dává první (54), s d=m.
Záměna P a Q dává druhou (54). Případ d=0 má jediný uzel
a všechny vzorce zůstávají správné. Nenulové členy mají
0<=k<=d; záporné k se vynechají podle nulové konvence.

## Složené a prefixové identity (55)–(56), úloha 61

Dosadíme `S(n+1,k+1)=sum_j C(n,j)S(j,k)` z (52)
do levé strany (55). Konečné součty prohodíme a vnitřní
součet `S(j,k)c(k,m)(−1)^(k−m)` je podle (47) [j=m].
Zbývá C(n,m), jak má být.

První (S2), vydělená n!, dává

```text
c(n+1,m+1)/n! − c(n,m+1)/(n−1)! = c(n,m)/n!,   n>=1.
```

Teleskopování spolu s případem n=0 vede k první (56).
Druhou (56) dává rozvinutí druhé (S2) jako nehomogenní
rekurence s násobícím činitelem m+1. Oba součty musejí mít
rozsah **0<=k<=n**, jak opravují errata z 16. května 2026.
Záporné faktoriály se nesmějí vyhodnocovat před vynecháním
nulových členů. Opravené konečné součty tento problém odstraňují.

Pro úlohu 61 označme požadovaný součet a(n,m). První (S2)
a inverze (47) dávají
`a(n,m)=n a(n−1,m)+[n=m]`, přičemž a(0,m)=[m=0].
Indukce proto dává přesně `[n>=m] n!/m!` pro n,m>=0.

## Rozsah dokladu

Tyto důkazy ověřují matematický obsah. Historická priorita
Stirlinga, Karamatovo značení a jednotlivé asymptotické práce
z popisku tabulky vyžadují čtení pramenů; nelze je odvodit
z kontrolních hodnot. Oprava svazku JLMS v popisku tabulky
z 5. dubna 2026 je zvlášť evidována jako známé erratum.
