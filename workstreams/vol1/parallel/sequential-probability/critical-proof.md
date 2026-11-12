# §2.2.2-13: kritický případ p=1/2

Dokazujeme limitu střední největší velikosti zásobníku a analytickou
totožnost dvou řad pro její konstantu. První část používá přesné
rozvinutí diskrétní procházky a odhad chyby harmonické funkce v jednom
kroku. Druhá část počítá stejnou harmonickou funkci dvěma způsoby.
Není třeba zaměňovat numerickou shodu za důkaz ani předpokládat
konvergenci zastavených procesů bez jejího zdůvodnění.

## 1. Přesné rozvinutí diskrétní procházky

`X,Y` jsou velikosti dvou zásobníků; každé vložení či odebrání z každého
z nich má pravděpodobnost `1/4`. Odebrání z nuly je nulový krok.
Zastavujeme při `X+Y=m`. Nechť `(U,V)` je obyčejná čtvercová náhodná
procházka z `(0,0)`: každý z kroků `(1,0),(-1,0),(0,1),(0,-1)` má
pravděpodobnost `1/4`. Potom

```
X=|U+1/2|-1/2,   Y=|V+1/2|-1/2                           (1)
```

má přesně požadovaný přechodový zákon. Mimo nulu je jeden ze dvou
směrů vložením a druhý odebráním. V nule odpovídají předobrazy
`U=0,-1` dvěma polohám, mezi nimiž je nulový krok; zbývající krok
vede do velikosti jedna. Totéž platí pro druhou souřadnici.

Položme `N=m+1` a otočme a přeskálujme procházku:

```
A=(U+V+1)/N,   B=(U-V)/N,   h=1/N.                       (2)
```

Start je `(h,0)`. Každý krok mění `A` a `B` o nezávislá znaménka
`+h,-h`, tedy čtyři diagonální směry mají stejnou pravděpodobnost.
Identita `max(|s+t|,|s-t|)=|s|+|t|` ukazuje, že zastavení `X+Y=m`
je přesně první zásah hranice čtverce

```
Q=[-1,1]^2.
```

Než se dosáhne hranice, procházka zůstává uvnitř; velikost kroku
neumožňuje hranici přeskočit. Označme čas zastavení `tau` a `C`
tu výstupní souřadnici, která nemá absolutní hodnotu jedna.
Roh čtverce není na dosažitelné síti: celočíselné souřadnice
`NA,NB` mají vždy součet lichý, kdežto v rohu by byl sudý.
Z (1)–(2) tedy přesně plyne

```
max(X,Y)/m = 1/2 + N/(2m) |C|.                          (3)
```

## 2. Harmonická funkce na čtverci

Harmonická funkce je zde dvakrát diferencovatelná funkce, jejíž
Laplacián `Delta w=w_aa+w_bb` je nulový. Její hodnoty lze použít
jako potenciál pro symetrickou náhodnou procházku. Definujme
`a_k=(k+1/2)pi`, `k=0,1,...`, a

```
w(a,b) = sum_(k>=0) (2/a_k^2) *
 [cos(a_k b) cosh(a_k a)/cosh(a_k)
  + cos(a_k a) cosh(a_k b)/cosh(a_k)].                    (4)
```

Každý sčítanec je harmonický. Na celém `Q` je jeho absolutní hodnota
nejvýše `4/a_k^2`, takže řada konverguje stejnoměrně a součet je
spojitý. Na kompaktních podmnožinách vnitřku všechny derivace
konvergují díky exponenciálnímu útlumu, a `w` je tam harmonická.

Kosinové Fourierovy koeficienty funkce `1-|t|` na `[-1,1]` jsou

```
integral_(-1)^1 (1-|t|) cos(a_k t) dt = 2/a_k^2;
integral_(-1)^1 cos(a_k t)^2 dt = 1.
```

Jde o obvyklou Fourierovu řadu sudého stanu s nulovými koncovými
hodnotami; integrace po částech dává uvedené koeficienty a jejich
absolutní sumovatelnost dává i stejnoměrnou konvergenci. Proto
`w(±1,b)=1-|b|` a `w(a,±1)=1-|a|`. V rohu je hodnota nula.
Princip maxima zajišťuje jednoznačnost tohoto spojitého řešení
Dirichletovy úlohy. V počátku je

```
w(0,0)=4 sum_(k>=0) 1/(a_k^2 cosh(a_k)).                 (5)
```

## 3. Diskrétní limitní přechod s kontrolou chyby

Nejprve potřebujeme konečnou střední dobu zastavení. První souřadnice
`NA` je jednoduchá symetrická procházka z `1` mezi `-N,N`. Její doba
prvního zásahu těchto konců má střední hodnotu `N^2-1` (řešení
diferenční rovnice je `N^2-i^2`). Čtvercová procházka končí nejpozději
v tomto čase, tedy

```
E tau <= N^2-1.                                         (6)
```

Funkce `w` nemusí mít omezené vysoké derivace až k hranici. Pro pevné
`0<r<1` proto použijme `w_r(z)=w(rz)`. Tato funkce je harmonická
a hladká v okolí celého uzavřeného `Q`. Průměr jejích hodnot po
jednom kroku procházky je

```
P_h w_r(a,b) = (1/4) sum_(s,t in {-1,1}) w_r(a+sh,b+th).
```

Taylorův rozvoj do třetího řádu s omezeným čtvrtým zbytkem dává

```
P_h w_r-w_r = (h^2/2) Delta w_r + O_r(h^4) = O_r(h^4).    (7)
```

Smíšený kvadratický člen i všechny liché členy se při průměrování
vyruší. (7) platí stejnoměrně pro všechny přechodné síťové body;
segmenty ke čtyřem následníkům leží v `Q`.

Teleskopování podmíněných středních změn do `tau wedge n`, potom
omezená konvergence vlevo a odhad (6) vpravo, dávají

```
|E w_r(A_tau,B_tau)-w_r(h,0)| <= O_r(h^4 E tau)=O_r(h^2). (8)
```

Označme `omega_r=sup_(z in Q)|w(rz)-w(z)|`. Spojitost `w` na
kompaktním `Q` zaručuje `omega_r->0` pro `r->1`. Z (8) a `h->0`
plyne

```
limsup_(m->infinity) |E w(A_tau,B_tau)-w(0,0)| <= omega_r.
```

Nejprve jsme nechali růst `m` při pevném `r`; nyní necháme `r->1`.
Dostáváme `E w(A_tau,B_tau)->w(0,0)`. Na hranici `w=1-|C|`, takže
(3)–(5) dokazují

```
E max(X,Y)/m -> alpha_square
             = 1-2 sum_(k>=0) 1/(a_k^2 cosh(a_k)).         (9)
```

Tento argument dokazuje přímo potřebnou limitu střední hodnoty.
Nevyžaduje citaci invariance principu ani neověřenou spojitost
operace „zastav při prvním výstupu“.

## 4. Analytické převedení na trojúhelník

Na trojúhelníku

```
D={(x,y): x>=0, y>=0, x+y<=1}
```

definujme

```
u(x,y)=1-(1/2)w(x+y,x-y).                                (10)
```

Otočení a změna měřítka zachovávají harmonicitu. Symetrie (4)
ukazují, že `u` je sudá při odrazu přes každou souřadnicovou osu;
na obou osách tedy má nulovou normálovou derivaci (Neumannovu
podmínku). Na přeponě má podle hraničních hodnot `w`

```
u(x,1-x) = (1+|2x-1|)/2 = max(x,1-x).                    (11)
```

V počátku `u(0,0)=alpha_square`. Tuto hodnotu nyní spočítáme pomocí
Greenovy funkce: harmonického potenciálu s logaritmickou singularitou
v počátku, nulovými normálovými derivacemi na osách a nulovou
hodnotou na přeponě. Greenova identita pak vyjadřuje `u(0,0)` jako
integrál jejích hraničních hodnot s tokem tohoto potenciálu.

## 5. Greenova funkce a její hraniční tok

Nejprve na čtverci `S=[0,1]^2` položme

```
G(x,y)=1/2-y + sum_(n>=1)
 2 cos(n*pi*x) [cosh(n*pi*(1-y))-(-1)^n cosh(n*pi*y)]
 / [n*pi*sinh(n*pi)].                                    (12)
```

Na kompaktních podmnožinách `0<y<1` konvergují všechny derivace
řady. Každý člen je harmonický a na svislých stranách má nulovou
normálovou derivaci. Rozložením hyperbolických funkcí na exponenciály
lze oddělit dvě jediné singularity:

```
G(x,y) = -(2/pi) log|1-exp(-pi*y+i*pi*x)|
         +(2/pi) log|1-exp(-pi*(1-y)+i*pi*(1-x))|
         + R(x,y),                                      (13)
```

kde `R` je hladká v okolí uzavřeného čtverce (obsahuje také
`1/2-y`). Zbylé řady a všechny jejich derivace konvergují
exponenciálně; nejmenší zbývající exponenciální vzdálenost
od obou singularit je kladná i v malém okolí `S`. Tedy

```
G=-(2/pi)log(sqrt(x^2+y^2))+O(1)        u (0,0),
G= +(2/pi)log(sqrt((1-x)^2+(1-y)^2))+O(1) u (1,1).        (14)
```

Na otevřené dolní straně lze spočítat normálovou derivaci jako
limitní Abelův součet: je `-1-2 sum_(n>=1) cos(n*pi*x)=0`.
Rovnost plyne přímo ze součtu geometrické řady s faktorem `t^n`
a limitou `t->1`; pro `0<x<1` je výsledný kosinový součet `-1/2`.
Na horní straně je stejně `-1-2 sum (-1)^n cos(n*pi*x)=0`.
Rozklad (13) zaručuje, že tyto limity jsou skutečné klasické
derivace mimo rohy, nikoli jen formální Fourierův zápis.

Funkce (12) má střední hodnotu nula na `S`: kosiny mají nulové
integrály přes `x` a `1/2-y` má nulový integrál přes `y`.
Tyto integrace jsou legitimní i u logaritmických rohů, například
protože integrál absolutní hodnoty n-tého členu je `O(n^-2)`.

Neumannova úloha s těmito dvěma logaritmickými singularitami je
až na konstantu jednoznačná. Rozdíl dvou řešení má odstranitelné
singularity (po sudém odrazu přes strany), nulovou normálovou
derivaci a je konstantní: Greenova identita pro jeho energii dává
integrál čtverce gradientu roven nule. Nulový průměr konstantu
určuje. Odraz `R_*(x,y)=(1-y,1-x)` prohodí oba singulární rohy;
funkce `-G(R_*(x,y))` má stejné singularity, stejné Neumannovy
podmínky a stejný nulový průměr. Proto

```
G(1-y,1-x)=-G(x,y).                                      (15)
```

Na úsečce `x+y=1` je tudíž `G=0`. Omezení (12) na `D` je hledaná
Greenova funkce s jediným zdrojem v počátku. Součinitel `2/pi`
v (14) odpovídá jednotkovému toku přes čtvrtkružnici kolem
počátku: její úhel je `pi/2`.

Pro `0<t<1` označme

```
f(t)=sum_(n>=1) cos(n*pi*t)sinh(n*pi*t)/sinh(n*pi).        (16)
```

Tato řada konverguje lokálně stejnoměrně uvnitř `(0,1)`. Na
přeponě, parametrizované jako `(t,1-t)`, je hustota vnějšího
toku vzhledem k `dt`

```
J(t)=-(G_x+G_y)(t,1-t).
```

Derivace podél přepony `G_x-G_y` je nulová. Derivováním (12)
podle `y` proto dostáváme přesně

```
G_y(t,1-t)=-1-2[f(t)+f(1-t)],
J(t)=2+4[f(t)+f(1-t)].                                   (17)
```

Greenova identita pro `u,G` na trojúhelníku s vynechanou malou
čtvrtkružnicí kolem počátku dává po limitě

```
u(0,0)=integral_0^1 u(t,1-t) J(t) dt.                    (18)
```

Na osách se oba normálové příspěvky ruší; na přeponě je `G=0`;
tok přes malou kružnici konverguje k `u(0,0)` díky (14).
Stejný výpočet s `u=1` ukazuje `integral_0^1 J(t)dt=1`.
U konců přepony je `G` hladká, její gradient je nulový kvůli
Neumannovým podmínkám na dvou přilehlých stranách `S`, a tudíž
`J(t)=O(t)` u nuly a `O(1-t)` u jedničky. Vzorce jsou proto
obyčejné konvergentní integrály. Pro naše spojitá hraniční data
lze Greenovu identitu případně nejprve použít na jejich hladké
aproximace; princip maxima a konečný tok dovolují přejít k limitě.

## 6. Integrace a analytická totožnost řad

Ze symetrie `J(t)=J(1-t)`, normalizace a (11)–(18) plyne

```
alpha_square=1-2 integral_0^(1/2) t J(t) dt
            =1/2-8 integral_0^(1/2) t[f(t)+f(1-t)] dt.    (19)
```

Záměna součtu a posledního integrálu je absolutně oprávněná.
Pro `a=n*pi` a `0<=t<=1/2` totiž

```
|cos(at)sinh(at)/sinh(a)| <= C exp(-a/2),
|cos(a(1-t))sinh(a(1-t))/sinh(a)| <= C exp(-a*t).
```

Po vynásobení `t` je integrál druhé meze nejvýše `C/a^2`.
Součet těchto integrálů je konečný.

Pro výpočet jednotlivého členu položme

```
K(t)=[sin(at)sinh(at)+cos(at)cosh(at)]/(2a),
M(t)=sin(at)cosh(at)/(2a^2).
```

Pak `K'(t)=cos(at)sinh(at)` a `M'(t)=K(t)`. Integrací po částech
a substitucí `s=1-t` v druhém sčítanci dostáváme

```
integral_0^(1/2) t [cos(at)sinh(at)
                    +cos(a(1-t))sinh(a(1-t))] dt
 = M(1)+M(0)-2M(1/2)
 = -sin(a/2)cosh(a/2)/a^2,                               (20)
```

protože `sin(a)=0`. Dosazení (20) do (19) dává **přesně tištěnou
řadu**, nikoli pouze asymptoticky nebo numericky ekvivalentní výraz:

```
alpha_square
 = 1/2 + 8 sum_(n>=1) sin(n*pi/2)cosh(n*pi/2)
                     / [n^2*pi^2*sinh(n*pi)]
 = 1/2 + (4/pi^2) sum_(n>=1) sin(n*pi/2)
                            / [n^2*sinh(n*pi/2)].        (21)
```

Poslední rovnost používá `sinh(2z)=2 sinh(z)cosh(z)`.
Spojením (9) a (21) jsme současně analyticky dokázali identitu

```
sum_(k>=0) (-1)^k / [(2k+1)^2 sinh((2k+1)*pi/2)]
 + 2 sum_(k>=0) 1 / [(2k+1)^2 cosh((2k+1)*pi/2)]
 = pi^2/8.                                               (22)
```

Důkaz (22) je založen na dvou výpočtech téže jednoznačně určené
harmonické funkce; žádný krok nepoužívá numerickou hodnotu řad.
Obě řady v (22) konvergují exponenciálně.

## 7. Závěr pro audit

Pro `p=1/2` platí

```
E max(X,Y) = alpha*m + o(m),
alpha = 0.675314483313567611597758668255117756950853449779...
```

Číselná hodnota byla již vypočtena v kořenové kontrole; úlohou
tohoto doplňku je obecný důkaz limity a rovnosti řad. Originál
s. 543 (soubor 558) obsahuje první řádek (21) a aproximaci
`0.6753144833`, obojí souhlasí. Není zde nový kandidát na chybu.
Flajoletův zdroj používá jinou parametrizaci a jeho vytištěné
číslo `0.67526` není číslem převzatým do knihy.
