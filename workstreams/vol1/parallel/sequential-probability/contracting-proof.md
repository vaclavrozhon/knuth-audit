# §2.2.2-13: pevné p > 1/2 a rostoucí kapacita

Tento vlastní důkaz doplňuje otevřený krok v
`../../notes/sequential-probability.md`. Je platný pro každé **pevné**
`1/2 < p < 1`. Při `p=1` se paměť nikdy nezaplní. Nejprve dokážeme,
že body uvnitř absorpční hrany mají asymptoticky stejnou pravděpodobnost;
pak odhadneme celkovou hmotnost u obou konců. Nevyžadujeme stejný
bodový odhad přímo v koncových bodech.

## 1. Model a přesné tvrzení

Nezastavený Markovův řetězec `Z_t=(X_t,Y_t)` žije na nezáporné
celočíselné kvadrantě. V každém kroku se vybere jedna souřadnice,
každá s pravděpodobností `1/2`; s pravděpodobností `1-p` se zvětší
o jednu a s pravděpodobností `p` se zmenší o jednu, je-li kladná.
Odebrání z nuly ponechá souřadnici nulovou. Volby v různých krocích
jsou nezávislé. Počáteční stav je `(0,0)`.

Položme `rho=(1-p)/p`, takže `0<rho<1`, a `delta=2p-1>0`.
Pro kapacitu `m` označme

```
B_m = {(j,m-j): 0 <= j <= m},
T_m = inf{t >= 0: Z_t in B_m},
H_m(j) = P_(0,0)(Z_(T_m)=(j,m-j)).
```

Pro každé pevné `epsilon` v `(0,1/2)` dokážeme

```
sup_(epsilon*m <= j <= (1-epsilon)*m) |m H_m(j)-1| -> 0.   (1)
```

Dále `X_(T_m)/m` konverguje v rozdělení k rovnoměrnému rozdělení
na `[0,1]`; dokonce jeho distribuční funkce konvergují stejnoměrně.
Odtud plyne

```
E max(X_(T_m),Y_(T_m))/m -> integral_0^1 max(u,1-u) du = 3/4. (2)
```

Toto je přesný asymptotický význam tvrzení knihy na s. 543. Nejde
o společnou limitu, ve které by `p` současně záviselo na `m`.

## 2. Doba návratu do počátku

Pro `z != (0,0)` nechť `T_0` je první zásah počátku. Dokážeme

```
E_(x,y) T_0 <= x^2+y^2+C_p,                              (3)
```

kde konečná konstanta `C_p` závisí jen na pevném `p`.

Použijeme funkci `V(x,y)=x^2+y^2`. Pro kladnou souřadnici `x`
je její příspěvek do podmíněné střední změny `V` roven

```
((1-p)(2x+1)+p(-2x+1))/2 = -delta*x+1/2.
```

Pro nulovou souřadnici je příspěvek `(1-p)/2 <= 1/2`. Proto

```
E[V(Z_(t+1))-V(Z_t) | Z_t=(x,y)] <= 1-delta*(x+y).
```

Zvolme celé `R` tak, aby `delta*(R+1)>=2`, a konečnou množinu
`C={(x,y):x+y<=R}`. Vně `C` je drift nejvýše `-1`. Zastavení
supermartingalu `V(Z_t)+t` při vstupu do `C`, nejprve v čase
omezeném číslem `n` a pak monotónní limitou `n->infinity`, dává
střední dobu vstupu do `C` nejvýše `V(x,y)`.

Ze stavu v `C` následujících `R` pokusů odebrat z prvního zásobníku
a dalších `R` pokusů odebrat z druhého vede do počátku. Pravděpodobnost
této konkrétní posloupnosti je `eta=(p/2)^(2R)>0`. Pokud se během
bloku délky `2R` do počátku nedostaneme, má součet souřadnic nejvýše
`3R`; střední doba dalšího vstupu do `C` je proto nejvýše `9R^2`.
Silná Markovova vlastnost dovoluje pokusy opakovat. Podmíněná
pravděpodobnost neúspěchu v každém pokusu je nejvýše `1-eta`;
očekávaný celkový čas od prvního vstupu do `C` do počátku je tedy
nejvýše `(2R+9R^2)/eta`. To dokazuje (3). Tím je zároveň doloženo
téměř jisté dosažení počátku, nikoli pouze formální driftový výpočet.

## 3. Od hlubší vrstvy je návrat k zaplnění nepravděpodobný

Řetězec je vratný vzhledem k pravděpodobnostem

```
pi(x,y)=(1-rho)^2 rho^(x+y).
```

Vratnost zde znamená `pi(v)P(v,w)=pi(w)P(w,v)` pro každou dvojici
stavů; stačí zkontrolovat sousední body, kde `rho*p=1-p`.
Nulové kroky tuto rovnost nemění.

Greenova funkce řetězce zastaveného v počátku je očekávaný počet
návštěv před zastavením:

```
G^0(v,z) = E_v sum_(0 <= t < T_0) [Z_t=z],   v,z != (0,0).
```

Obrácením každé konečné dráhy, která neprochází počátkem, plyne

```
pi(v) G^0(v,z) = pi(z) G^0(z,v).
```

Součty jsou konečné podle (3). Je-li `v` ve vrstvě `s=x+y<m`,
pak ze (3) a `G^0(z,v)<=E_z T_0` vyplývá

```
P_v(T_m<T_0)
 <= sum_(z in B_m) G^0(v,z)
 <= rho^(m-s) sum_(z in B_m) E_z T_0
 <= (m+1)(m^2+C_p) rho^(m-s).                             (4)
```

První nerovnost pouze říká, že při zásahu `B_m` se před `T_0`
navštíví alespoň jeden její bod. Nezaměňuje první zásah s celým
tokem opakovaných návštěv. Pro `v=(0,0)` má obdobný požadovaný
odhad pravděpodobnosti zásahu před okamžitým `T_0=0` triviálně
levou stranu nula.

Zvolíme-li celočíselné

```
L=L_m=ceil(c log(m)),   c > 4/(-log(rho)),
```

pak pravá strana (4) pro `s=m-L` jde k nule, stejnoměrně v bodu
této vrstvy. Přebytek konstanty `4` není optimalizován; stačilo
by libovolné číslo větší než `3`.

## 4. Pravděpodobnost návratu z vrstvy m-1

Definujme `h_m(v)=P_v(T_0<T_m)` pro `0<x+y<m` a `h_m(0,0)=1`.
Tvrdíme, že pro každé pevné `epsilon>0`

```
h_m(x,y) -> 1-rho
```

stejnoměrně ve stavech `x+y=m-1`, `min(x,y)>=epsilon*m`. Dokud
nezasáhneme některou osu, má součet souřadnic nezávislé kroky
`+1` s pravděpodobností `1-p` a `-1` s pravděpodobností `p`.
Jeho hloubka `D=m-X-Y` má tedy drift `delta>0`. Spřáhněme ji
s neodraženou procházkou, která začíná v `D=1`, a zastavme tuto
procházku v čase `sigma` prvního zásahu `0` nebo `L`.

Zastavený součet `D_(sigma wedge n)-delta*(sigma wedge n)` má
střední hodnotu `1`. Jelikož `0<=D_(sigma wedge n)<=L`, dostáváme
`E sigma <= (L-1)/delta`. Dosažení některé osy před `sigma`
vyžaduje alespoň `epsilon*m` kroků. Markovova nerovnost tudíž dává

```
P(coupling fails before sigma) <= E sigma/(epsilon*m)
                               = O_p(L/(epsilon*m)).     (5)
```

Pravděpodobnost, že procházka hloubky z `1` dosáhne `L` před `0`,
je přesně

```
P_1(T_L<T_0) = (1-rho)/(1-rho^L).                         (6)
```

Rovnice plyne například dosazením harmonické funkce `rho^d`
do zastavení na `0,L`; drift hloubky je směrem k `L`.
Při zásahu `0` jsme zaplnili paměť. Při zásahu `L` dosáhne
odražený řetězec počátku před novým zaplněním s pravděpodobností
alespoň `1-(m+1)(m^2+C_p)rho^L`, podle (4). Z (5)–(6) tedy

```
|h_m(x,y)-(1-rho)/(1-rho^L)|
 <= O_p(L/(epsilon*m)) + (m+1)(m^2+C_p)rho^L.              (7)
```

Oba členy vpravo jdou k nule. Dostáváme požadovanou rovnoměrnou
limitu `1-rho`. Je zásadní, že se počítají pravděpodobnosti
**prvního** zásahu, nikoli jen stacionární hmotnosti vrstvy.

## 5. Přesný vzorec pro zásahový zákon

Nyní zastavme řetězec při `T_m` a označme jeho Greenovu funkci
`G_m(v,w)`. Pro konečné přechodné stavy `x+y<m` je její hodnota
konečná: blok `m` vložení do prvního zásobníku vede k zastavení
s pravděpodobností alespoň `((1-p)/2)^m`, nezávisle na dosavadní
dráze. Vratnost a silná Markovova vlastnost při prvním zásahu
počátku dávají

```
G_m(0,v) = pi(v)/pi(0) * G_m(v,0)
         = rho^(x+y) h_m(v) G_m(0,0).                     (8)
```

Pro bod `b_j=(j,m-j)` jsou jeho předchůdci uvnitř oblasti
`(j-1,m-j)` pokud `j>=1` a `(j,m-j-1)` pokud `j<=m-1`.
Nechť `W_m(j)` je součet hodnot `h_m` přes tyto existující
předchůdce. Každý přechod z předchůdce do `b_j` má pravděpodobnost
`(1-p)/2`; ze (8) je proto

```
H_m(j) = ((1-p)/2) rho^(m-1) G_m(0,0) W_m(j).
```

Zastavení nastává právě jednou a téměř jistě. Sečtení přes `j`
tedy dává přesnou normalizovanou identitu

```
H_m(j) = W_m(j) / sum_(i=0)^m W_m(i).                     (9)
```

Vždy platí `0<=W_m(j)<=2` a pro koncové body dokonce `<=1`.
Pro `epsilon*m<=j<=(1-epsilon)*m` mají oba předchůdci obě
souřadnice alespoň `epsilon*m-1`, takže (7) implikuje

```
W_m(j) -> 2(1-rho)
```

stejnoměrně v tomto rozmezí. Vynechání nejvýše `2epsilon*m+O(1)`
koncových členů v normalizačním součtu má po dělení `m` velikost
nejvýše `4epsilon+o(1)`. Nejprve `m->infinity` a pak
`epsilon->0` proto dává

```
(1/m) sum_(i=0)^m W_m(i) -> 2(1-rho).                    (10)
```

Spojením (9)–(10) vzniká lokálně stejnoměrná limita (1).
Současně `H_m(j)<=C/m` pro všechna `j` a všechna dost velká `m`,
s konstantou závislou na pevném `p`. Koncové úseky celkové délky
`2epsilon` tedy nesou hmotnost `O(epsilon)`.

Pro každou spojitou funkci `f` na `[0,1]` lze její zásahovou
střední hodnotu rozdělit na koncové úseky a vnitřní interval.
Koncový příspěvek je `O(epsilon ||f||_infinity)`; na vnitřním
intervalu (1) mění součet na běžný Riemannův součet. To dokazuje
slabou konvergenci k rovnoměrnému rozdělení a výběrem
`f(u)=max(u,1-u)` i (2). Stejnoměrná konvergence distribučních
funkcí plyne rovněž přímo: vnitřní chyba je součtem nejvýše `m`
členů `o(1/m)` a koncová chyba je `O(epsilon)`.

## 6. Rozsah a vztah ke zdroji

Důkaz neodkazuje na nevypsaný asymptotický výpočet Flajoletovy
věty 3. Používá jen přesnou vratnost, zastavené martingaly,
jednorozměrný gambler's ruin a Riemannovy součty. Parametr
Flajoletova článku má odlišný význam: jeho pravděpodobnost
jednoho konkrétního vložení je `(1-p_knihy)/2` a konkrétního
odebrání `p_knihy/2`. Jeho „contracting case“ tedy odpovídá
právě zde zkoumanému `p_knihy>1/2`.

Originál knihy, s. 543 (soubor 558), byl prohlédnut. Věta knihy
je tím pro `1/2<p<1` dokázána. Není zde nový kandidát na chybu.
