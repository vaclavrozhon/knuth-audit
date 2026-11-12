# §4.2.3: programy a úlohy1–8

Kontrola2.11.2026, původní sazba246–253 a617–619 vizuálně přečtena.
Devět původních úloh; nové úlohy v erratech nenalezeny. **Úloha9 a cílený
historický kontext se řeší zvlášť.** Časová tabulka252 bude propojena
s předpoklady rozdělení vstupů v §4.2.4; není to tvrzení o každém běhu.

## Zdroje a konvence

`all2-prepre`: str.246,16.7.2006 denormal→subnormal;2.11.2004 odlišení
nekonečen od NaN; str.247,24.9.1999 a10.8.1998 dvě jazykové opravy.
`all2-pre`: str.618,24.11.2012 řádek22→23 v odpovědi5 a záporné znaménko
v příkladu odpovědi7; str.619 better then→than v odpovědi8.
`all2` a `err2` další relevantní změny neobsahují. Prohledány i názvy
programů a témat. Historické stránky15 a14 příslušných errat zobrazeny.

Báze `b` je počet hodnot bytu, v MIX kontrolách64 a100. Označme `Q=b^2/2`
(exces exponentu), `W=b^5` (počet velikostí slova bez znaménka) a
`F` celé číslo tvořené osmi zlomkovými byty. Normalizované nenulové číslo je

```
s F b^(e-Q-8),  s in {-1,+1},  b^7 <= F < b^8,  0 <= e < b^2.
```

Nula má `e=F=0`. První slovo nese znaménko a exponent; znaménko druhého slova
nemá význam. `truncate_p` níže znamená normalizovat a odříznout vše za p-tou
číslicí směrem k nule. Nejde o zaokrouhlení k nejbližšímu číslu.

## Nezávislé modely a rozsah výpočtu

- [Přepis MIX](../sources/double-precision.mix) zachovává čísla řádků;
  lokální návěští mají jednoznačná jména. Programy nepřepsány z OCR.
- [Interpret](../mix_float_machine.py) zachovává znaménka nul, oddělená
  znaménka rA/rX, adresová pole, přetečení a samomodifikaci.
  Doplněn MOVE, pojmenovaná pole a volitelný pozorovatel; původní operace
  ze4.2.1 zůstávají stejné. Zdrojové varianty generuje ověřovač.
- [Celočíselný model](../double_precision_model.py) používá níže odvozené
  vzorce, nesimuluje jednotlivé instrukce.
- [Kontrola](../verify_double_precision.py),
  [výstup](../results/double-precision.json):4529 dvojic pro každou bázi,
  původní i přesnější sčítání/odčítání/násobení, obě verze dělení,
  nulové vstupy, znaménka nízkého slova, exponentové kraje. Celkem
  72464 porovnání hlavních operací a9058 kontrol odstranění zbylého rX.
  Úspěšně prošly i uvedené meze relativní chyby. Konečné vzorky samy o sobě
  nejsou obecný důkaz.
- [Další kontrola](../verify_double_precision_edges.py),
  [výstup](../results/double-precision-edges.json): převody, nezávislý
  součet cen instrukcí u časových protipříkladů a192 navazujících volání
  bez odstranění samomodifikovaného stavu.

Programy záměrně nejsou správně zaokrouhlenou aritmetikou; jejich odchylky
v povolených mezích nejsou nové chyby. **C0091** opravuje časové výroky
odpovědí4/5, nikoli výpočty nebo meze přesnosti.

## Sčítání: invariant, znaménko, meze7/8

Po případné výměně předpokládejme `|u|>=|v|`, změňme společné znaménko tak,
aby `u>0`, a pišme jeho zlomkovou část `U/b^8`; druhá je `sigma V/b^8`,
kde `sigma` je1 nebo-1. Nechť `d=e_u-e_v>=0`. Původní program před závěrečným
odříznutím reprezentuje

```
(U + sigma floor(V/b^d)) / b^8.
```

Vylepšení z úlohy5 reprezentuje

```
(b U + sigma floor(V b/b^d)) / b^9.
```

Před oběma výrazy stojí společný faktor `b^(e_u-Q)`. Řádky18–30 zarovnají
zlomky. Vložená1 na začátku nižší části zaručí znaménko většího operandu;
pak řádky36–40 současně přenesou přenos nebo půjčku. U nulového rA musí
zůstat znaménko správné pro nenulový rX. Prohození řádků39/40 je skutečně
chybné: pro opačná znaménka a zlomky lišící se o poslední byte může obrátit
znaménko výsledku. Konkrétní reprodukce je ve výstupu obou bází.

**Původní sčítání, úloha7.** Pro stejné znaménko je ztráta při zarovnání
menší než jednotka posledního vstupního bytu. Případný přenos vyžaduje
odříznout jeden byte, s další ztrátou nejvýše `b-1` těchto jednotek. Relativní
chyba je menší než `b^-7`.

Pro opačná znaménka, `d=0`, je rozdíl přesný. Při `d>=1` položme
`q=U-V/b^d>0`. Program vrátí přesně `ceil(q)` v jednotkách zarovnání:
je to celé číslo menší než `b^8`, takže levá normalizace nic neodřízne.
Pro `d=1` je `q>=1/b`; pro `d>=2` je
`q>b^7-b^(8-d)>=b^7(1-1/b)`. Z toho relativní chyba nepřekročí `b-1`.
Rovnosti dosáhneme pro `U=b^7,V=b^8-1,d=1`: `q=1/b`, výsledek1.
To je opravený příklad odpovědi7. Výsledek0 nastane právě při přesném
vyrušení stejných opačných operandů (nepočítáme hlášený exponentový rozsah).

**Přesnější sčítání, úloha8.** Pro `d<=1` se při zarovnání neztratí nic;
normalizace s odříznutím osmi číslic má relativní chybu menší než `b^-7`.
Při `d>=2` a stejných znaménkách je celá ztráta menší než b jednotek
zarovnání bez přenosu a menší než `b^2` s přenosem; příslušné součty jsou
nejméně `b^8`, resp. `b^9`, takže opět dostáváme `b^-7`.

Při `d>=2` a opačných znaménkách je přesná velikost v jednotkách devátého
bytu `q=bU-V/b^(d-1)>b^8(1-1/b)`. Program nejprve vytvoří `n=ceil(q)`.
Je-li `n<b^8`, výsledek je n a chyba menší než1. Jinak vrátí
`b floor(n/b)`; je-li výsledek větší než q, chyba je nejvýše1, jinak
nejvýše `b-1`. Poměr `(b-1)/(b^8(1-1/b))=b^-7` dává požadovanou mez.

## Násobení: invariant, úlohy2/3/4 a meze7/8

Označme `U_m=floor(U/b^3)`, `U_l=(U mod b^3)b^2` a obdobně `V_m,V_l`.
Pak zlomky operandů jsou `U_m/W+U_l/W^2`, resp. `V_m/W+V_l/W^2`.
Jsou-li oba nenulové, `b^4<=U_m,V_m<W` a `0<=U_l,V_l<W`.

Původní program připraví devítimístné celé číslo

```
K9 = floor(U_m V_m/b)
   + floor(U_m V_l/b^6) + floor(V_m U_l/b^6).
```

Vylepšení připraví desetimístné

```
K10 = U_m V_m + floor(U_m V_l/W) + floor(V_m U_l/W).
```

Normalizují se zlomky `K9/b^9` nebo `K10/b^10` s exponentem `e_u+e_v-Q`.
Oba vzorce vynechávají nejnižší součin `U_l V_l/W^4`. Odpovídají obrázku4.

**Úloha2.** Ve starém programu po řádku31 zbyde část původního rX až za
prvními devíti byty. Součin vysokých částí zaručí hodnotu nejméně `b^-2`,
pokud jsou oba vstupy nenulové; normalizace se tedy posune vlevo nejvýše
jednou. Výstupních osm bytů zbylý byte nemůže použít. Při nulovém vstupu
jsou tyto zbytky také nulové. Vložení ENTX0 nezmění odpověď.

**Úloha3.** Řádek09 sčítá dvě dvoubytová čísla. Na22 jde o dvě čtyřbytová,
na30 o tři čtyřbytová; pro MIX bázi nejméně64 se vždy vejdou do pěti bytů.
Na32 výsledek nepřekračuje přesný součin zlomků, který je menší než1.
Indexový registr2 nese jen `-Q`; součet exponentů je v pětibytovém EXPO.
Všechny deklarované absence přetečení tedy platí.

**Úloha4.** Nové sčítání vysokých částí křížových součinů může přetéct;
registr1 zaznamená přenos. Druhý přenos může vzniknout při přičtení nízké
části hlavního součinu. `ENTX 0,1; SRC 5` převede oba přenosy do správných
pozic. Součet má hodnotu K10. Přibylo skutečně pět řádků; údaj o celkovém
čase má výjimky popsané v [C0091](C0091-double-precision-timing.md).

**Původní mez.** Označme přesný součin zlomků x. Platí
`0<=x-K9/b^9<3b^-9`. Pokud není třeba levý posun, odřízne se ještě zbytek
nejvýše `(b-1)b^-9`, takže relativní chyba je menší než `(b+2)b^-8`.
Při levém posunu už se další číslice neztrácí a `x>=b^-2`, takže stačí
`3b^-7`. Obě situace pokrývá uvedená mez `delta2=3b^-7`.

**Přesnější mez.** Ztráta před normalizací je menší než `3b^-10`.
Bez levého posunu se odřízne nejvýše `(b^2-1)b^-10`; jelikož `x>=1/b`,
relativní chyba je menší než `(b^2+2)b^-9<=(b+2)b^-8`.
S levým posunem je další ztráta nejvýše `(b-1)b^-10` a `x>=b^-2`,
tedy relativní chyba menší než `(b+2)b^-8`. Případ, kdy přesný x leží
nad1/b, ale aproximace pod1/b, do druhé nerovnosti také patří.

## Dělení: přesný význam programu a mez7

Předpokládejme kladné zlomky `f_u,f_v`; výsledek obdrží součin původních
znamének. Nechť `v_m=V_m/W`, `v_l=V_l/W`, `epsilon=b^-5` a

```
a = f_u/(b v_m), beta = v_l/(b v_m), t = b^-4 beta.
```

Přesný zlomek podílu v použitém měřítku je `x=a/(1+t)`.
Řádky15/18 vypočtou `floor(a b^10)`, vysoká část je `floor(a b^5)`;
řádek22 vytvoří `floor(beta b^5)`. Řádky24–26 připraví korekci a27–35
ji odečtou. Přesná celočíselná hodnota před normalizací je

```
K = floor(a b^10)
  - floor(floor(a b^5) floor(beta b^5)/b^4).
```

Je normalizována s exponentem `e_u-e_v+Q+1`, což ruší úvodní faktor1/b.
Geometrická řada(2) je platná, protože `0<=epsilon v_l/v_m<b^-4<1`.

Pro kontrolu převodu znaménka při půjčce pišme první celočíselný člen jako
`A W+C` a korekci jako `H W+L`, kde `0<=C,L<W`. Řádky27–29 vytvoří
`L-C-W`. Přetečení nastane právě při `L<=C`; bez něj se zvýší H o1.
Po otočení slov jsou nízké byty `(C-L) mod W` a horní část
`A-H-[L>C]`. To je přesně odčítání K. Znaménko vysokého slova je až nakonec
obnoveno z uloženého původního výsledku. Nulový dělitel je zachycen na23;
nenormalizované vstupy nejsou součástí deklarované domény programu.

Pro nenulový čitatel normalizace potřebuje nejvýše jeden levý posun.
Zde je kontrola tohoto hraničního tvrzení i pro nejmenší zlomek. Položme
`A=V_m`, takže `b^4<=A<W`. Při zvýšení U o1 vzroste
`floor(a b^10)=floor(U b^6/A)` nejméně o b. Hodnota
`floor(a b^5)=floor(U b/A)` vzroste nejvýše o1, a odečítaná korekce tedy
nejvýše o b, neboť `floor(beta b^5)<W`. K je proto neklesající funkcí U.
Stačí U=`b^7`. Položme `d=W-A`. První člen K pak je
`b^8+floor(b^8 d/A)`, zatímco korekce je nejvýše
`floor(b^8(W-b^2)/A^2)`. Pro `1<=d<=W-b^4` platí
`d(W-d)>=W-b^2`: konkávní kvadratická funkce nabývá minima na jednom konci,
kde jsou hodnoty `W-1` a `b^4(W-b^4)`. Korekce je tedy nejvýše
`floor(b^8 d/A)` a `K>=b^8`. Současně `a<1`, takže `K<b^10`.
Zlomek `K/b^10` skutečně leží mezi `b^-2` a1.

Následuje samostatný důkaz uvedené meze, včetně rezervy v odhadu. Položme
`z=K/b^10`. Chyby odříznutí `d0,d1,d2,d3` definujeme rovnostmi

```
floor(a b^10)/b^10 = a-d0,
floor(beta b^5)/b^5 = beta-d1,
floor(a b^5)/b^5 = a-d2,
floor(floor(a b^5) floor(beta b^5)/b^4)/b^6
    = (a-d2)(beta-d1)-d3.
```

Jsou nezáporné a menší než `b^-10,b^-5,b^-5,b^-6`.
Proto `z=a-d0-b^-4((a-d2)(beta-d1)-d3)`.
Relativní chyba `(z-x)/x` se rozpadá na kladnou část P a zápornou část N:

```
P = (1+t)b^-4 (d1+d2 beta/a+d3/a),
N = (1+t)(d0/a+b^-4 d1 d2/a)+t^2.
```

Z `b^-1<=v_m<1`, `f_u>=b^-1`, `v_l<1` dostaneme
`a>=1/(b^2 v_m)`, `beta<=1/(b v_m)` a `beta/a<b`.
Tedy `P<(1+b^-4)(2+1/b)b^-8<3b^-8`.
Pro `c=(1+b^-4)^2` máme

```
N < b^-8 (c v_m + 1/(b^2 v_m^2)) <= b^-8 (1+c/b).
```

Poslední funkce je konvexní na `[1/b,1]`, takže maximum leží na konci;
platí `c<=1+1/b`, a větší je levý konec. Tím je také `z>0`.
Závěrečné odříznutí osmi číslic ztrácí nejvýše `b^-7 z`, takže jeho
relativní vliv vůči x je nejvýše `b^-7(1+P)`.
Celková záporná chyba je proto menší než

```
b^-7 + (1+c/b+3b^-7)b^-8 < (b+2)b^-8   (b>=2).
```

Kladná chyba je nejvýše `P<3b^-8<=(b+2)b^-8`. Tím je dokázána mez
`delta3=(b+2)b^-8`, bez nutnosti pokládat zanedbané vyšší členy za nulu.
Nulový čitatel se vyřizuje přesně; exponentové přetečení/podtečení se hlásí.

## Úlohy1,5,6

**1.** Pro `epsilon=1/1000` dává první dělení
`floor((.180/.314)10^6)/10^6=.573248`. Korekce do tří míst je
`floor((.573*.159/.314)10^3)/10^3=.290`. Rozdíl je `.572958`.
Přímé dělení180000/314159 odříznuté na šest desetinných míst dává totéž.
Tvrzení odpovědi1 je správné.

**5.** Se změnou23 místo původně chybně uvedeného22 vznikne výše popsaný
devítibytový součet. Přibývá šest řádků. Při přetečení je nutné nejprve
snížit exponent a teprve podmíněně vrátit1: kdyby se jen změnil EXPO na0,
`INC2 1` by mohl překročit dvoubytový rozsah indexového registru.
Časový údaj vyžaduje výjimky C0091.

**6.** Převod do dvojité přesnosti opraví exponent o `Q-b/2`, vymaže rX,
posune původní čtyři byty na začátek zlomku a přesně normalizuje; nevznikne
ztráta číslic ani rozsahu. Převod zpět odčte stejný rozdíl excesů a použije
již prověřenou normalizaci4.2.1 včetně jejího pravidla půlení.
Přetečení či podtečení se posuzuje až po normalizaci a zaokrouhlení,
což správně zachytí i přenos při zaokrouhlení na hranici exponentu.
Cílené testy zahrnují tyto hrany, nulová znaménka a ignorovaný znak rX.
