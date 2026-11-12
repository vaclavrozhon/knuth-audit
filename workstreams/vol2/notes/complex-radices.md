# §4.1: komplexní základy, úlohy 16–18 a 28

## Rozsah a prameny

Uzavřeny jsou čtyři úlohy s vlastními obecnými důkazy, text o základu
`−1+i` na straně 206 a matematické tvrzení o dimenzi hranice na straně 606.
Gaussovské celé číslo znamená `x+iy`, kde `x,y` jsou celá a `i²=−1`.
Jeho normou zde rozumíme eukleidovskou délku `sqrt(x²+y²)`.
Zápis čísla má konečně mnoho pozic vlevo od řádové čárky; vpravo smí
pokračovat do nekonečna. Úvodní nuly nerozlišujeme.

Originály 205–206, 210, 212 a 606–607 byly přečteny vizuálně; souborová
strana DjVu je tištěná strana +12. Všechny čtyři řady errat byly prohledány
v [uloženém výňatku](../sources/positional-errata-excerpts.txt).
Oprava z 9. 6. 2003 mění v odpovědi 18 podmínku „fixed“ na „sufficiently
small“; tento známý opravný zásah je nutný. Změna množinových závorek
na téže straně nemění následující důkaz uzavřenosti.
Nová chyba v tomto bloku nebyla potvrzena.

Výpočet [verify_complex_radices.py](../verify_complex_radices.py) používá
přesné dvojice celých čísel a racionální intervaly. Čtyři dokončené bloky
jsou v [JSON](../results/complex-radices.json) a [logu](../results/complex-radices.log).
Při prvním běhu prošly tři bloky a poslední selhal na mém nesprávném
odhadu desetinného intervalu kořene. Odhad nahradila racionální bisekce;
obnoven byl pouze poslední blok, s návratovým kódem 0. Úspěšný prefix
se neopakoval. První shell zakončený `cat` se nevydává za úspěch verifieru.

## 1. Celočíselné zápisy v základu β = −1+i

Zbytek `d` při dělení `z=x+iy` základem β je nuceně
`d=(x+y) mod 2`, tedy 0 nebo 1. Podíl `q(z)=(z−d)/β` má souřadnice

```
q(x,y) = ((−(x−d)+y)/2, (−(x−d)−y)/2).
```

Obě jsou celé. Opakování tohoto dělení dává číslice zprava doleva.
Dokud `|z|>1+sqrt(2)`, platí

```
|q(z)| <= (|z|+1)/sqrt(2) < |z|.
```

Proto trajektorie vstoupí do konečného disku `x²+y²<=5`; pokles je
skutečně konečný, protože kvadrát normy je nezáporné celé číslo.
Disk má přesně 21 bodů. Je invariantní, neboť
`(sqrt(5)+1)/sqrt(2)<sqrt(6)` a žádný výsledný celočíselný kvadrát normy
nemůže překročit 5. V JSON je pro každý bod vypsána celá trajektorie do 0.
Tento úplný konečný certifikát spolu s poklesem dokazuje ukončení pro
**všechna** Gaussovská celá čísla. Nejde o extrapolaci z testovaného okna.

Existence zápisu plyne z ukončení. Jednoznačnost plyne z nuceného zbytku,
po němž je nucen i podíl. Nezávislá rekonstrukce všech 4225 bodů
`−32<=x,y<=32` pak kontroluje implementaci.

## 2. Úloha 16: čtyři tištěné operace

Písmena `P,M,Q,N` označují postupné přičtení `+1,−1,+i,−i` k hodnotě
řetězce. Pro řetězec α a bit `x` jsou tištěná pravidla

```
(α0)^P = α1             (αx1)^P = α^Q x0
(αx0)^M = α^N x1        (α1)^M  = α0
(α0)^Q = α^P 1         (α1)^Q  = α^N 0
(α0)^N = α^Q 1         (α1)^N  = α^M 0.
```

Každá rovnost je rovností hodnot v základu β. Například druhé pravidlo
přidá `iβ²−1=1`, protože `β²=−2i`; páté přidá `β+1=i`.
Stejné dosazení ověří zbývající pravidla.

Aby tvrzení o ukončení mělo přesnou bázi indukce, pro prázdný řetězec
(hodnotu 0) použijeme výsledky

```
P: 1       M: 11101       Q: 11       N: 111.
```

Jejich hodnoty jsou přímo `1,−1,i,−i`; odpovídají tištěnému doplňování
nul zleva. Každé další rekurzivní volání má kratší prefix, takže algoritmy
končí. Test pro všechny řetězce délky 0 až 12 a čtyři operace obsahuje
32764 případů; porovnává výsledek s nezávislým dělením z §1.

Varování před naivním přepisem `2 -> 1100` odpovídá tomu, že přepis nemusí
snižovat délku ani velikost mezistavu. Verifier ověřuje hodnoty
`1100=2` a `11101=−1`; nesimuluje neurčené pořadí takových přepisů.
Správnost a ukončení vytištěných čtyř operací jsou dokázány výše.

## 3. Úloha 18: uzavřenost a skutečné okolí nuly

Nechť `S` je množina všech součtů `sum(k>=1) a_k β^(−k)`, kde každý
`a_k` je 0 nebo 1. Po prvních `m` cifrách má ocas normu nejvýše
`(sqrt(2)+1)|β|^(−m)`, nezávisle na zbývajících cifrách.
Z každé posloupnosti bodů S lze diagonálním výběrem vybrat podposloupnost,
na níž se nejprve ustálí první cifra, potom druhá atd. Rovnoměrná mez
ocasu dává konvergenci k bodu S. S je tedy kompaktní, zejména uzavřená.
To zpřesňuje argument knihy s nekonečnou větví stromu.

Osmá mocnina β je 16. Nechť `D8` označuje 256 hodnot osmiciferných
celých zápisů. Mocniny β pro exponenty 0 až 7 jsou

```
(1,0), (−1,1), (0,−2), (2,2), (−4,0), (4,−4), (0,8), (−8,−8).
```

Součet kladných a záporných souřadnic zvlášť dává přesné souřadnicové
meze D8: `−13<=x<=7`, `−14<=y<=11`. Seskupení po osmi cifrách znamená
`S={sum(j>=1) v_j 16^(−j): v_j in D8}`. Geometrická řada proto dává

```
S subset [−13/15,7/15] × [−14/15,11/15].             (1)
```

Každý nenulový celočíselný posun `S+(m,n)` je od nuly vzdálen alespoň
`1/15` v maximové normě `max(|x|,|y|)`: pokud je některá souřadnice
posunu kladná nebo záporná, její nejbližší možná hodnota se podle (1)
nemůže přiblížit více. Jde o jednotnou mez pro všechny posuny.

Pro libovolné `|x|,|y|<1/15` vezměme

```
z_k = (floor(16^k x) + i floor(16^k y))/16^k.
```

Čitatel má podle §1 konečný zápis. Dělení `16^k=β^(8k)` pouze posune
čárku, a tedy `z_k` patří do některého `S+(m,n)`. Pro dost velké k je
`max(|Re z_k|,|Im z_k|)<1/15`. Jediným možným posunem je potom `(0,0)`.
Uzavřenost S a limita `z_k -> x+iy` dokazují

```
(−1/15,1/15) × (−1/15,1/15) subset S.               (2)
```

Libovolný komplexní bod lze násobit dost velkou zápornou mocninou β,
aby spadl do tohoto okolí; zpětný posun čárky dá požadovaný zápis.
Tak je doložen i krok, který odpověď uvádí jen slovy „It can be shown“.
Bez známé opravy „sufficiently small“ by závěr chybně tvrdil `S=C`.

## 4. Obrázek a dimenze hranice

Z definice platí `βS=S union (S+1)` a
`16S=union(v in D8) (S+v)`. Druhá rovnost dává 256 zmenšených kopií,
první dvě kopie po otočení o 135 stupňů a přepočtu měřítka.
[Vlastní obrázek](../results/twindragon-truncations.png) obsahuje všech
65536 šestnácticiferných zlomků, barevně rozdělených podle první cifry.
Byl vizuálně porovnán s původním tvarem. Konečný obrázek sám nedokazuje
plnost oblasti, rozměr hranice ani (2).

Hausdorffova dimenze je exponent popisující velikost množiny při pokrývání
stále menšími množinami; zde se ověřuje tvrzení o hranici S, nikoli ploše S.
Pro přesnou definici a použitou větu odkazujeme na §3, Theorem 2 článku
[P. Duvall, J. Keesling, A. Vince, *The Hausdorff Dimension of the Boundary
of a Self-Similar Tile*, JLMS (2) 61 (2000), 748–760](https://people.clas.ufl.edu/avince/files/HausdorffDim.pdf).
Článek byl čten textově v hlavní části 748–759; původní strany 754–755
(věty a důkazy) a 757–758 (twindragon) také vizuálně.

Předpoklady jsou zde ověřeny takto. Násobení β má matici
`A=[[-1,−1],[1,−1]]`, zvětšuje všechny délky faktorem `c=sqrt(2)`
a má determinant 2. Číslice `(0,0),(1,0)` jsou úplní reprezentanti tříd
`Z²/AZ²`, což plyne z parity součtu souřadnic. Každý bod S lze aproximovat
prefixem jeho zápisu následovaným nulami. Protože 0 je vnitřní bod S,
každý takový prefix je vnitřním bodem příslušné zmenšené kopie S;
S je tedy uzávěr svého vnitřku. Má kladnou konečnou plochu. Z
`βS=S union (S+1)` a násobení plochy dvěma plyne, že obě kopie mají
průnik plochy nula; jejich vnitřky jsou disjunktní. To jsou podmínky
„self-similar digit tile“ z §1 článku.

Kontaktní matice počítá možné přenosy mezi konečnou množinou sousedních
mřížových bodů. Přesně: začneme množinou `N={0,±1,±i}` a uzavíráme ji
na operace `z -> q(z+d)` pro `d=0,1`, s podílem q z §1. Algoritmus 1
článku dává `N={0,±1,±i,±(1+i)}`. Po odebrání nuly je prvek `C_xy`
počet číslic d splňujících `q(x+d)=y`. V pořadí
`−1−i,−1,−i,i,1,1+i` vlastní přesný výpočet dává

```
C = [0 0 0 2 0 0]
    [0 0 0 0 0 1]
    [0 1 0 1 0 0]
    [0 0 1 0 1 0]
    [1 0 0 0 0 0]
    [0 0 2 0 0 0].
```

Její charakteristický polynom je
`(t−1)(t²+2t+2)(t³−t²−2)`. Největší modul vlastního čísla je kladný
kořen λ posledního faktoru. Ten leží mezi 3/2 a 2; ostatní dva jeho
kořeny jsou komplexně sdružené s modulem `sqrt(2/λ)<sqrt(2)`, kořeny
kvadratického faktoru mají modul `sqrt(2)`. Racionální bisekce v JSON
certifikuje interval šířky `2^(−81)` pro λ.

Jelikož `λ<2=det A`, Theorem 3 článku ověřuje dodatečnou podmínku věty 2
(o mřížovém dláždění a ploše 1). Věta 2 pak dává

```
dim_H(boundary S) = log(λ)/log(sqrt(2)) = 2 log_2(λ)
                 = 1.52362708620249210627…,
λ = 1.69562076955986205741… .
```

To souhlasí s knihou. Článek v příkladu §5.1 používá základ `1+i`,
nikoli `−1+i`; jeho další faktory charakteristického polynomu se proto
liší. Výpočet zde byl proveden přímo pro základ knihy.
Důkaz věty 2 porovnává počty malých pokrývacích čtverců s růstem mocnin C;
rovnost boxové a Hausdorffovy dimenze přebírá z Falconerovy věty 3.5.
Tato externí závislost není vydávána za nový samostatný důkaz všech
fraktálních vět. Historické připsání názvu Mandelbrotovi a další obecné
komplexní soustavy v odstavci na straně 607 patří do zbývajícího
kontextového bloku. Penneyho ACM PDF při pokusu vrátil HTTP 403;
[metadata](../sources/penney-1965.json) neznamenají, že byl přečten.

## 5. Úloha 17: proč základ γ = 1+i nestačí

Označme `S+` množinu zlomků s číslicemi 0/1 v základu γ.
Protože `γ^8=16`, analogický osmibitový výpočet dává

```
S+ subset [−2/3,2/3] × [−4/3,1/3].                 (3)
```

Jediná Gaussovská celá čísla, která zde mohou ležet, jsou 0 a −i.
Obě skutečně leží v S+: první má nulové cifry, druhé samé jedničky,
protože `sum(k>=1) γ^(−k)=1/(γ−1)=−i`.

Kdyby −1 mělo zápis s konečnou celočíselnou částí p a zlomkovou částí f,
pak p je Gaussovské celé číslo, a tedy i `f=−1−p`. Z (3) vychází
`p=−1` nebo `p=−1+i`. Nucené dělení základem γ ale dává

```
−1 -> −1+i -> i -> i -> … .
```

Žádná z obou možností tedy nemá konečný celočíselný zápis.
To vylučuje −1 i tehdy, dovolíme-li nekonečný zlomek, jak úloha připouští.
Tištěné příklady `−i=0.111…` a `i=100.111…` jsou správné: `γ²=2i`.

## 6. Úloha 28: revolving binary

Reprezentace je součet `sum(j=0..t) i^j γ^(e_j)`, kde exponenty e_j
jsou přísně rostoucí nezáporná celá čísla. Pro `z=x+iy` je první větev
určena paritou x+y. Je-li součet sudý, exponent 0 chybí a dělíme γ.
Je-li lichý, exponent 0 je přítomen, první člen je 1 a zbývající součet
má tvar `iγ w`; tedy přejdeme na `w=(z−1)/(iγ)=(z−1)/β`.

V obou případech platí kontrakční mez z §1. Stejný disk 21 bodů je
invariantní; v JSON jsou úplné trajektorie do nuly i pro tyto dvě větve.
Při návratu přičteme všem exponentům podúlohy 1 a v lichém případě
připojíme počáteční exponent 0. To dokazuje existenci pro všechna z.
Parita nutí každé rozhodnutí, takže reprezentace je jednoznačná.
Pro nulové z je jedinou reprezentací prázdný součet: případná neprázdná
konečná reprezentace by po odstranění nejmenší mocniny měla lichý
součet souřadnic. Dalších 4225 rekonstrukcí kontroluje kód vůči přímému
součtu komplexních mocnin.
