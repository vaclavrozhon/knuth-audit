# Hornerova schémata, posuny a konečné diference

Blok **V2-X0076** kontroluje matematický obsah stran 485–489 a úloh
§4.6.4–1 až 7 s odpověďmi 698–699. Algoritmy počítají správné hodnoty.
Nový nález **C0234** se týká druhu dvou ušetřených operací v odpovědi 6;
je doložen v §6 níže. Historické priority, Dornův model paměti a úplný
pramen Hasslerovy inicializace nejsou tímto blokem uzavřeny.

Používáme polynom `u(X) = sum_{j=0}^n u_j X^j`, kde `u_n != 0`.
Velké `X` je formální proměnná, malé `x` nebo `a` je dosazovaná hodnota.
`M`, `D` a `A` znamenají jedno skalární násobení, dělení a sčítání či
odčítání. Počty jsou pro obecné koeficienty; předem známé nuly a jednotky
mohou dovolit další úspory. Kopírování se nepočítá. Koeficienty jsou
v tomto bloku reálné nebo komplexní. Rozšíření na obecné algebraické
struktury vyžaduje příslušnou komutativitu a existenci uváděných podílů.

## 1. Hornerovo pravidlo a úlohy 1, 3, 5

Označme `q_j(x) = sum_{k=j}^n u_k x^(k-j)`. Z rovnosti
`q_j = u_j + x q_{j+1}` a počáteční hodnoty `q_n = u_n` přímo plyne
Hornerovo pravidlo. Pro `n >= 1` potřebuje `n M + n A`; každé vynechané
přičtení nulového koeficientu ušetří jedno A. U naivního společného
výpočtu mocnin stojí `x^2,...,x^n` celkem `n-1 M`, násobení koeficientů
dalších `n M` a součet `n A`. Výsledek `2n-1 M + n A` sedí.
Konstantní polynom se pouze vrátí; tyto počty předpokládají `n>=1`.

Pro úlohu 1 pišme `u(X)=X w(X^2)`, kde `w` má stupeň `n`. Stačí jeden
čtverec, Hornerův výpočet `w`, a násobení výsledku `x`: `n+2 M + n A`.
Pro lineární lichý polynom není třeba počítat nepoužité `x^2`.

V úloze 3 je koeficient `X^i` polynom stupně `n-i` v druhé proměnné.
Jeho Hornerův výpočet stojí `n-i` násobení i sčítání. Vnější průchod
přidá `n` obou operací, celkem `sum_{i=0}^n (n-i)+n=n(n+3)/2`.
Počet koeficientů je součet `1+2+...+(n+1)=(n+1)(n+2)/2`.
Pro homogenní polynom, v němž má každý člen součet exponentů `n`, platí
`u(x,y)=y^n w(x/y)`. Doplněk odpovědi 3 je správný při `y != 0`;
volba `0 < |x| <= |y|` drží podíl v jednotkovém intervalu. Nulové
argumenty se vyřídí přímo, při opačné velikosti se role proměnných vymění.

Rozklad `u(X)=E(X^2)+X O(X^2)` dává schéma (4). Stupně `E,O` jsou
`floor(n/2)` a `ceil(n/2)-1`. Pro `n >= 1` je celková cena
`1+floor(n/2)+ceil(n/2)=n+1 M` a
`floor(n/2)+ceil(n/2)-1+1=n A`. Uchováme-li oba sčítance, další
odčítání dává `u(-x)`. Přibližné zkrácení paralelního času předpokládá
nezávislé aritmetické jednotky bez dalších úzkých míst.

Obecně lze seskupit exponenty podle zbytku modulo `k` a vyhodnotit
`k` polynomů v `x^k`. Estrinova tabulka pro stupeň 7 je rozklad

```text
[(u7*x+u6)*x^2 + (u5*x+u4)]*x^4
  + [(u3*x+u2)*x^2 + (u1*x+u0)].
```

Používá `9 M + 7 A`, včetně dvou čtverců. Závislosti ve třech řádcích
jsou správné; celý řádek ale nestojí jedinou skalární operaci.

## 2. Komplexní argument a úloha 4

Píšeme `z=x+i y`, kde `i^2=-1`, a `r=2x`, `s=x^2+y^2`. Platí
`z^2=rz-s`. Zbytek po dělení dosud zpracované části polynomu výrazem
`X^2-rX+s` má tvar `a_j X+b_j`. Připojení dalšího koeficientu změní
tento zbytek na

```text
X(a_j X+b_j)+u = (r a_j+b_j)X+(u-s a_j).
```

To dokazuje (3) i závěrečné `u(z)=z a_n+b_n`, také pro komplexní
koeficienty. V kroku pro `b_j` se použije původní `a`. Hornerův postup
je obdobně zbytek po dělení `X-x`.

Přímé komplexní násobení používá `4 M + 2 A`. Alternativně pro
`(a+i b)(x+i y)` vypočteme

```text
p=x(a+b), q=(x+y)b, r=(y-x)a;
real=p-q, imaginary=p+r.
```

Cena je `3 M + 5 A`. Při opakovaném stejném `z` se hodnoty
`x+y,y-x` připraví jednou a další součin stojí `3 M + 3 A`.
Z toho vycházejí všechny vytištěné počty:

| Koeficienty a metoda | M | A |
|---|---:|---:|
| reálné, Horner se čtyřmi M | `4n-2` | `3n-2` |
| reálné, Horner se třemi M | `3n-1` | `6n-5` |
| reálné, (3) | `2n+2` | `2n+1` |
| komplexní, Horner se čtyřmi M | `4n` | `4n` |
| komplexní, Horner se třemi M | `3n` | `7n` |
| komplexní, (3), poslední součin se čtyřmi M | `4n+2` | `4n+2` |
| komplexní, (3), poslední součin se třemi M | `4n+1` | `4n+5` |

Pro reálné koeficienty a `n >= 2` se opakováním násobitele ušetří
`2n-4 A`, jak uvádí strana 487. Pro komplexní koeficienty lze obdobně
ušetřit `2n-2 A`; odpověď 4 uvádí neoptimalizované obecné operace.
Nepřítomnost této další optimalizace není chybným počtem.
Ve skutečné sazbě je zlepšení pro **`n >= 3`**, nikoli OCR `n > 3`.
Pro `|z|=1` je `s=1`; vynechá se výpočet `s` i násobení tímto číslem.
Zůstává `n+1 M` a `2n A`. Rozdělení `u(exp(i theta))` na kosinovou
a sinovou řadu plyne z Eulerova vzorce po jednotlivých členech.

## 3. Posun argumentu: H, G a úloha 2

Binomická věta dává koeficient `X^j` v `u(X+a)`:

```text
v_j = sum_{k=j}^n binom(k,j) u_k a^(k-j).                 (P1)
```

V charakteristice nula je to také `u^(j)(a)/j!`. Rovnice (P1) sama
žádné dělení faktoriálem nevyžaduje. Příklad z knihy je správně
`3(X-2)^2+2(X-2)-1=3X^2-10X+7`.

Pro důkaz H zapišme `u(X)=q(X)(X-a)+u(a)`. První sestupný průchod
vypočte zbytek `u(a)` a koeficienty `q`. Další průchod dělá totéž
s `q`, takže po `n` průchodech máme všechny koeficienty posunu.
Počet aktualizací je `n+(n-1)+...+1=n(n+1)/2`, každá obsahuje M a A.

Shodu s G doložíme i na úrovni jednotlivých aritmetických výrazů.
Definujme `T[-1,j]=u_j`, `T[r,n]=u_n` a pro `0 <= r <= j < n`

```text
T[r,j] = T[r-1,j] + a*T[r,j+1].                          (P2)
```

H počítá `r` vzestupně a `j` sestupně. Vnější krok G s indexem `k`
počítá pro vzestupná `j >= k` právě položky `T[j-k,j]`. Oba vstupy
už existují: staré `v_j` je `T[j-k-1,j]` a ještě neaktualizované
`v_{j+1}` je `T[j-k,j+1]`. Oba postupy skončí s `T[j,j]`. Počítají
tedy stejné aritmetické výrazy v jiném pořadí; při stejném zaokrouhlení
každé operace budou stejné i jejich numerické hodnoty.

## 4. Škálování S a jeho stabilita

Pro `a != 0` vytvoří S polynom `w(X)=u(aX)`. Posun o 1 dává
`w(X+1)=u(aX+a)` a závěrečné dělení koeficientu `X^j` hodnotou `a^j`
dává (P1). Pro `a=0` je výsledek původní pole koeficientů a škálování
se nepoužije. Toto explicitní dělení a triviální nulový posun nepovažujeme
za nový nález o dělení nulou.

Příprava mocnin vyžaduje `n-1 M`, škálování koeficientů `n M`.
Posun o 1 má pouze `n(n+1)/2 A`. Výstup `v_n=u_n` lze převzít přímo,
takže stačí `n-1 D`. Toto vysvětlení doplňuje známé erratum
z 7. června 1999; vytištěný počet už byl správný.

„Stejná numerická stabilita“ neznamená totožné zaokrouhlené výsledky.
Lze přímo ověřit obvyklou chybu stejného řádu. Předpokládejme relativní
chybu každé základní operace nejvýše `epsilon`, bez přetečení a podtečení.
Položka `u_k a^k` má po sekvenční přípravě mocnin nejvýše `k`
zaokrouhlovacích faktorů. Každá cesta příspěvku sčítací tabulkou má
nejvýše `n` sčítání: pro `k<n` jde o `k-j` vodorovných a `j+1` svislých
kroků v (P2), pro `k=n` se narazí na konstantní okraj. Závěrečné dělení
přidá jeden faktor a převrácenou chybu připravené mocniny `a^j`,
s nejvýše `j-1` faktory.

Proto každému výslednému příspěvku v (P1) odpovídá relativní porucha
`O(n epsilon)` pro `n epsilon` malé. Pro `j>=1` horní faktor nepřekročí
`(1+epsilon)^(k+n+1)/(1-epsilon)^(j-1)`; obdobná dolní mez plyne
z obrácených znamének. Pro `j=0` výstupní dělení odpadá. Absolutní
chyba je nejvýše konstanta řádu `n epsilon` krát
`sum_{k=j}^n binom(k,j)|u_k||a|^(k-j)`. Stejný řád má H, kde cesta
obsahuje nejvýše `n` sčítání a `n` násobení. To je tvrzení o každém
výstupu, nikoli důkaz jediné společné poruchy vstupních koeficientů
realizující všechny výstupy současně.

Shaw–Traub 1974 ještě analýzu zaokrouhlení neobsahuje. Zpráva autorů
z roku 1975 na straně 2 odkazuje na Woźniakowského 1974. Jeho primární
abstrakt potvrzuje stabilitu rodiny. Celý článek se získat nepodařilo;
výše je náš vlastní jednodušší důkaz pro S, nikoli reprodukce všech
jeho výsledků.

## 5. První derivace: D1–D4

Položme `t=ceil(sqrt(n/2))`, pro `0 <= j < n`
`f(j)=t-1-((n-1-j) mod 2t)` a `f(n)=t`. Číslo `g(j)` je `2t`,
pokud `n-1-j` je kladný násobek `2t`, jinak 0. Platí

```text
g(j) + f(j+1) - f(j) = 1.                               (P3)
```

Po D2 je `v_j=x^f(j) u_j`. Průchod D3 a (P3) dávají
`v_j=x^f(j) q_j(x)`, kde `q_j` bylo definováno v §1. Průchod D4 dává

```text
v_1 / x^f(1) = sum_{j=1}^n x^(j-1) q_j(x)
               = sum_{k=1}^n k u_k x^(k-1) = u'(x).
```

Hodnota `v_0` se v D4 nemění a stále dává `u(x)`. Při `x=0`
se vracejí `u_0,u_1`; pro konstantní polynom `u_0,0`. Algoritmus
s vytištěnými indexy je určen pro `n>=1`.

D1 stojí `t M`. V D2 je `Z=floor((n+t)/(2t))` nulových exponentů,
tedy `n+1-Z` operací M/D. V D3 je `B0=floor((n-1)/(2t))` násobení,
ve D4 `B1=max(0,floor((n-2)/(2t)))`. Závěrečné škály vyžadují po
jedné operaci, právě když je příslušné `f` nenulové. Celkem tedy

```text
t+n+1-Z+B0+B1+[f(0)!=0]+[f(1)!=0]
    = n+t+n/(2t)+O(1) = n+sqrt(2n)+O(1)                 (P4)
```

operací M/D a přesně `2n-1 A`. Hranaté závorky označují 1 při platnosti
podmínky a 0 jinak. Kniha netvrdí přesný celočíselný vzorec bez `O(1)`.
Obě starší opravy D3 z 4. července 1997 už tento dotisk obsahuje.

## 6. Úloha 6 a nový nález C0234

Definujme `m=floor(n/2)` a `h=ceil(n/2)`. J2 vytvoří
`w(X)=a^(-m)u(aX)`. Po J3 je `w(X+1)=a^(-m)u(aX+a)`;
násobení koeficientu `X^j` hodnotou `a^(m-j)` obnoví (P1).
Stačí připravit `a^2,...,a^h`. Pro `n>=1` mají J1–J4 dohromady

```text
(h-1)+h+m = n+h-1 M,    m+h = n D,
n(n+1)/2 A.                                               (P5)
```

Tento vytištěný počet je správný. Následující věta však slibuje úsporu
dalšího jednoho M a jednoho D zvláštním zacházením s `v_n,v_0`.
Správná přímá úprava pro `n>=2` šetří **dvě D**:

1. Závěrečné `v_n/a^h` vynecháme a vrátíme uložené `u_n`.
2. `v_0` se účastní pouze poslední operace prvního průchodu J3.
   Máme-li v tom okamžiku `w=v_1`, nahradíme
   `a^m(u_0/a^m+w)` výrazem `u_0+a^m w`.

Druhá úprava ruší počáteční dělení; jedno násobení i jedno sčítání
zůstávají. Správný počet je `n+h-1 M`, `n-2 D` a stejný počet A.
Pro `n=1` stačí `1 M + 1 A` a ušetří se jen jediné D.

Nejde pouze o neúspěch této konkrétní interpretace: vytištěný slib
**nelze splnit obecně už pro `n=2`**. Po jeho aplikaci by zbylo
`1 M + 1 D`. Samotný konstantní koeficient posunutého polynomu je
`u_0+u_1 a+u_2 a^2`, polynom celkového stupně 3 ve čtyřech nezávislých
vstupech. Aritmetický program s nejvýše jedním M, jedním D a libovolně
mnoha A takový polynom vypočítat nemůže:

- Jestliže je M před D, všechny vstupy do jediného dělení jsou
  polynomy celkového stupně nejvýše 2. Při generickém společném
  škálování vstupů parametrem `T` má jejich podíl růst nejvýše `T^2`.
  Následná sčítání tuto mez nezvětší.
- Jestliže je D před M, jde o podíl afinních forem. Pod generickým
  škálováním roste nejvýše jako `T`. To platí pro oba operandy jediného
  M; po něm je růst nejvýše `T^2` a další A jej nezvětší.

Generické škálování znamená volbu pevného směru, ve kterém se nezruší
vedoucí homogenní část žádného nenulového jmenovatele. Takový směr
existuje, protože nenulových polynomů, jimž se vyhýbáme, je konečně
mnoho. Požadovaný výstup má v tomto směru nenulový člen řádu `T^3`,
což je spor. Důkaz používá standardní model bez předběžně zdarma
adaptovaných koeficientů.

Naopak `2 M + 0 D` skutečně stačí:

```text
b = u_2*a;
w = u_1+b;
v_0 = u_0 + a*w;
v_1 = w+b;
v_2 = u_2.
```

Proto je C0234 **confirmed** v rozsahu chyby počtu M versus D.
Celkový slib úspory dvou operací M/D pro `n>=2` zůstává pravdivý.
Šest vrstev errat neobsahuje odpovídající opravu; doplnění u S na
straně 489 je jiné místo. Sazba odpovědi 6 byla přečtena vizuálně.
Pozdější fyzický dotisk a prvenství neověřeny, hlášení neodesláno.

## 7. Tabulace a úloha 7

Definujeme dopřednou diferenci `Delta f(k)=f(k+1)-f(k)`. Každá
diference sníží stupeň nekonstantního polynomu o 1. Nechť
`f(k)=u(x0+k h)` a `beta_j=Delta^j f(0)`. Pro `h=0` je `f` konstantní.
Newtonův binomický rozvoj je

```text
f(k)=sum_{j=0}^n binom(k,j) beta_j.                       (P6)
```

Zobecněný binomický koeficient znamená
`binom(k,j)=k(k-1)...(k-j+1)/j!`, s hodnotou 1 pro `j=0`.
(P6) plyne indukcí podle stupně: diference pravé strany posune
`beta_j` o index díky Pascalově identitě, zatímco hodnota v nule
souhlasí. Je to polynomová identita, tedy platí i pro záporná celá `k`.

V odpovědi se uloží `y_j=f(j)`. Po `r` sestupných průchodech platí
pro `j>=r` invariant `y_j=Delta^r f(j-r)`; hodnoty s menším indexem
jsou hotové `Delta^j f(0)`. Sestupné pořadí zaručuje, že `y_{j-1}`
ještě nebylo v aktuálním průchodu změněno. Výstup je tedy `beta`.
Staré erratum z 26. února 1996 napravovalo opačné pořadí;
třetí vydání je už správné.

Ve schématu (5) se naopak aktualizuje **vzestupně**. Nechť `N` posune
vektor o index doleva a poslední souřadnici nahradí nulou. Krok je
násobení maticí `I+N`. Protože `N^(n+1)=0`, binomická věta dává
`(I+N)^k=sum binom(k,j)N^j` a tištěnou formuli pro všechny souřadnice.
Každý krok stojí `n A`. Stupeň je nejvýše `n`, a právě `n`, je-li
`beta_n != 0`; nulové koncové diference odpovídají menšímu stupni.

Chyba `delta` v aktuální souřadnici `j` po dalších `k` krocích přispěje
do hodnoty přesně `delta*binom(k,j)`. V souřadnici 0 vznikne polynomová
chyba stupně nejvýše `j`, což vysvětluje upozornění knihy. Při pevném
řádu a bez přetečení je sčítání přesné; počáteční chyby diferencí se
přesto zvětšují podle tohoto vzorce.

Doplněk na straně 699 volí kladný celočíselný rozestup `d` a kontrolní
uzly `0,d,...,nd`. Matice `binom(i*d,j)` je nesingulární: determinant
je `d^(n(n+1)/2)` z vedoucích koeficientů binomických polynomů a
Vandermondova determinantu. Při chybách `epsilon_i` v uzlech je chyba
mezi nimi přesně `sum epsilon_i L_i(k)`, kde
`L_i(k)=product_{r!=i}(k-r*d)/(i*d-r*d)`. Malé uzlové chyby dávají mez
`max|epsilon_i| * sum|L_i(k)|` v intervalu tabulace. Vhodné kvantované
`beta` mohou být výhodnější než samostatné zaokrouhlení každé diference;
nejde o univerzální dominanci pro každý vstup. Kniha zde nespecifikuje
normu optimalizace ani algoritmus pro její řešení. Nadbytečná závorka
u `x_nd` je známá oprava z 28. června 1999, nikoli nový nález.

## 8. Zdroje a rozsah ověření

Strany TAOCP 485–489, 515 a příslušné odpovědi 698–699 byly přečteny
v OCR i obrazu; stránka 485 zde jen od nadpisu 4.6.4. Manifest
`sources/polyeval-basic.json` obsahuje otisky dokumentů a šesti vrstev errat.

[Shaw–Traub 1974](https://iiif.library.cmu.edu/file/Traub_box00028_fld00002_bdl0001_doc0001/Traub_box00028_fld00002_bdl0001_doc0001.pdf)
byl čten v rozsahu algoritmů a počtů stran 161–165 a poznámek o stabilitě
na 167, také vizuálně. Strana 166 s důkazem optimality není součástí
auditu. Jejich příklad pro první derivaci volí jiný parametr než
Knuthovo D; naše ověření D se opírá o vlastní identitu (P3).

[Zpráva Shaw–Traub 1975](https://iiif.library.cmu.edu/file/Traub_box00028_fld00010_bdl0001_doc0001/Traub_box00028_fld00010_bdl0001_doc0001.pdf)
byla použita jen pro úvod a poznámku o zaokrouhlení na tištěné straně 2,
souborové 5, která byla také vizuálně přečtena. Následnou optimalizaci
parametrů zde netvrdíme prověřenou.

[Woźniakowski 1974](https://epubs.siam.org/doi/abs/10.1137/0711064)
je pouze primární abstrakt a metadata; lokální požadavek na celý text
skončil HTTP 403. De Jong–van Leeuwen 1975 je bibliograficky ověřen přes
Crossref, DOI `10.1145/1008343.1008345`; pokus o PDF ACM skončil 403,
hledání ve veřejném CWI článek nedalo. Jeho celý text se netvrdí přečten.
Hassler 1996 zatím nebyl nalezen. Tyto mezery nemění nezávislé důkazy
výše ani C0234; historické a bibliografické pokrytí oddílu zůstává partial.

Tři nové bloky prošly jednou, session 74056:

| Blok | Obsah | Proces / limit | Čas vlastní kontroly |
|---|---|---|---:|
| basic | 192 reálných, 384 komplexních, 39 dvourozměrných případů | PID 1592222 / 120 s | 0.728463 s |
| shifts | 164 posunů, 135 bázových vstupů, 384 kontrol D; 41 shod grafů výrazů H/G | PID 1592225 / 120 s | 1.815905 s |
| differences | 33 inicializací, 1749 hodnot, 792 poruch, 27 matic | PID 1592232 / 120 s | 0.611780 s |

Orákula používají přímé součty monomů a binomický rozvoj. Operace
M/D/A se sčítají při skutečném provádění. Vše je racionální nebo
gaussovsky racionální aritmetika, bez tolerance. Celkem 3.156147044 s
vlastních kontrol, 3.461335657 s včetně tří obalů; všechny exit 0.
Úspěšné bloky neopakovat bez nové změny nebo konkrétní pochybnosti.
Cíl celého svazku pokračuje.
