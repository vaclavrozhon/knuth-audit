# §3.1-11 až 15: rovnoměrné náhodné zobrazení

Kontrola 1. listopadu 2026. Zadání na [str. 8](../images/vol2-p008.png),
odpovědi na [str. 541](../images/vol2-p541.png) a
[542](../images/vol2-p542.png). Níže jsou obecné důkazy odpovědí 11, 12,
14 a 15 a přesné části odpovědi 13. Citované hlubší asymptotiky odpovědi
13 jsou níže ověřeny proti primárním zdrojům; nejde o nové důkazy těchto vět.

## Jedna trajektorie

Nechť `m>=1` je počet stavů. Zobrazení `f` vybíráme rovnoměrně ze všech
`m^m` funkcí; počáteční stav `X_0` vybíráme nezávisle a rovnoměrně.
Trajektorie je posloupnost `X_(i+1)=f(X_i)`. Její ocas má délku `mu>=0`
a její konečný cyklus délku `lambda>=1`; celkem je v ní `t=mu+lambda`
různých stavů. Definujme

```text
p_0=1,   p_j=product_(k=1)^j (1-k/m),
Q(m)=sum_(j=0)^(m-1) p_j.
```

Dokud se neopakuje vstup funkce, každá další hodnota `f` je nová nezávislá
rovnoměrná volba. Pravděpodobnost prvních `j+1` různých stavů je `p_j`.
První kolize v čase `t` má každou z `t` možných cílových pozic stejně
pravděpodobnou. Pro každé přípustné `mu,lambda` tedy přesně platí

```text
Pr(mu,lambda) = p_(mu+lambda-1)/m.                 (1)
```

To přímo dává odpověď 11: `Pr(lambda=1)=Q(m)/m`. Podmíněně na `t`
je `lambda` rovnoměrná na `1,...,t`. Součet pravděpodobností přežití
navíc dává `E(t)=sum_j Pr(t>j)=Q(m)`, kde `E` označuje střední hodnotu.
Proto odpověď 12 splňuje

```text
E(lambda)=(Q(m)+1)/2,  E(mu)=(Q(m)-1)/2,  E(mu+lambda)=Q(m).    (2)
```

Tím je ověřena i symetrie středních hodnot `lambda` a `mu+1`.

## Asymptotika Q

Značení `O(h(m))` znamená chybu absolutní velikosti nejvýše konstantní
násobek `h(m)` pro dost velká `m`; `o(1)` znamená veličinu jdoucí k nule.
Položme `x=j/sqrt(m)`. Taylorův rozvoj logaritmu součinu dává

```text
log p_j = -x^2/2 - (x/2+x^3/6)/sqrt(m)
          + O((x^2+x^4)/m).
```

Rozvoj stačí použít pro `j<=sqrt(m)*log(m)`. Zbytek součtu lze zanedbat
s chybou menší než libovolná záporná mocnina `m`, protože
`p_j<=exp(-j*(j+1)/(2*m))`. Po exponentování je zbytek omezen
integrovatelným polynomem krát Gaussovou funkcí. Součet s krokem
`1/sqrt(m)` se převede na integrál s příspěvkem `1/2` v počátku.
Použitím

```text
integral_0^infinity exp(-x^2/2) dx = sqrt(pi/2),
integral_0^infinity x*exp(-x^2/2) dx = 1,
integral_0^infinity x^3*exp(-x^2/2) dx = 2
```

dostáváme konstantní člen `1/2-1/2-2/6=-1/3`, tedy

```text
Q(m)=sqrt(pi*m/2)-1/3+O(m^(-1/2)).                (3)
```

Vzorce a konstanty v odpovědích 11 a 12 z toho vyplývají: zejména
`E(lambda)=sqrt(pi*m/8)+1/3+O(m^(-1/2))` a pro `m=10^10` je
pravděpodobnost konečného pevného bodu přibližně jedna ku 80 000.
Nejde o tvrzení, že konkrétní algoritmus K je rovnoměrná náhodná funkce.

## Rozklad funkce na les a permutaci

Graf funkce má z každého vrcholu právě jednu šipku, do jeho obrazu.
Cyklické vrcholy jsou ty ležící na cyklech. Odstraněním jejich cyklických
šipek vznikne les stromů orientovaných ke kořenům; kořeny jsou právě
cyklické vrcholy. Jejich původní šipky tvoří permutaci množiny kořenů.

Označme `T_mn` počet lesů s libovolnou množinou `n` kořenů na `m`
označených vrcholech. Pro pevnou množinu kořenů je počet
`n*m^(m-n-1)`, pokud `n<m`; pro `n=m` je jeden prázdný les.
Lze to dokázat inkluzí a exkluzí nežádoucích orientovaných cyklů mimo
kořeny: její součet je determinant matice `m*I-J` řádu `m-n`, kde
`I` je jednotková matice a `J` matice samých jedniček. Diagonální člen
`m-1` volí jakéhokoli rodiče kromě sebe, záporné součiny mimo diagonálu
odečítají disjunktní cykly. Vlastní čísla jsou `n` jednou a `m` ve všech
zbývajících směrech, takže determinant má uvedenou hodnotu.
Volbou kořenové množiny tak získáme pro všechna `1<=n<=m`

```text
T_mn=binom(m-1,n-1)*m^(m-n).                      (4)
```

Každý takový les lze doplnit libovolnou z `n!` permutací kořenů.
To dokazuje `sum_n T_mn*n!=m^m`. Označíme-li počet cyklických vrcholů
náhodné funkce `C`, dostáváme

```text
Pr(C=n)=(n/m)*p_(n-1),
Pr(C>=n)=p_(n-1),   E(C)=Q(m),   E(1/C)=Q(m)/m.   (5)
```

Poslední tři identity plynou teleskopickým součtem
`p_(n-1)-p_n=(n/m)*p_(n-1)` a definicí `Q`.

## Počet cyklů: odpověď 14

Označme `c_r(m)` počet funkcí s právě `r` konečnými cykly a `[n;r]`
počet permutací `n` prvků s právě `r` cykly. Rozklad výše dává
`c_r(m)=sum_n T_mn*[n;r]`, což je vzorec v knize.
Pro `r=1` máme `[n;1]=(n-1)!`, a tedy
`c_1(m)=m^(m-1)*Q(m)`.

Také úvodní rekurence odpovědi je správná. Funkce s jediným cyklem,
jejíž obraz vynechává daných `k` vrcholů, vznikne z takové funkce na
`m-k` vrcholech a z libovolných `(m-k)^k` šipek vynechaných vrcholů.
Inkluze a exkluze proto dává

```text
(m-1)! = sum_(k=0)^(m-1) (-1)^k*binom(m,k)*(m-k)^k*c_1(m-k),
```

protože funkce bez vynechaného obrazu je permutace a musí mít jeden cyklus.

Počet konkrétních orientovaných cyklů délky `j` je `(m)_j/j`, kde
`(m)_j=m*(m-1)*...*(m-j+1)`. Každý je přítomen s pravděpodobností
`m^(-j)`. Střední počet cyklů `E_m` je proto

```text
E_m=sum_(j=1)^m (m)_j/(j*m^j)
   =integral_0^infinity ((1+x/m)^m-1)*exp(-x) dx/x.             (6)
```

Integrální zápis se ověří rozvinutím konečné binomické sumy a integrálem
`integral x^(j-1)*exp(-x) dx=(j-1)!`.

Podmíněně na `C=n` je permutace cyklických vrcholů rovnoměrná, takže
její střední počet cyklů je harmonické číslo `H_n=sum_(i=1)^n 1/i`.
Z (5) plyne, že `C/sqrt(m)` má v limitě hustotu `r*exp(-r^2/2)` pro
`r>0`. Přechod ke střednímu logaritmu je oprávněn i u nuly: z (5)
plyne `Pr(C<=u*sqrt(m))<=u^2/2+O(u/sqrt(m))`; horní ocas je Gaussovsky
omezen. Oba integrály ocasu logaritmu tak lze omezit stejnoměrně.
Protože `H_n=log(n)+gamma+O(1/n)`, kde `gamma` je Eulerova konstanta,
a `E(1/C)=O(m^(-1/2))`, vychází

```text
E_m = (log(m)+gamma+log(2))/2 + o(1).             (7)
```

Zde jsme použili substituci `u=r^2/2` a integrál
`integral_0^infinity log(u)*exp(-u) du=-gamma`.
To ověřuje i asymptotickou konstantu uvedenou v odpovědi.

## Nejdelší cyklus a žádný pevný bod

Pro odpověď 13 definujme `P_nk` jako počet permutací `n` prvků, jejichž
nejdelší cyklus má délku `k`. Přesný počet funkcí se stejným maximem
je `sum_n T_mn*P_nk`. Tato část je plně odvozena a nezávisle otestována.
Pokud použijeme citovanou asymptotiku permutací
`E(L_n)=c*n+c/2+O(1/n)`, kde `L_n` je nejdelší cyklus a `c≈0.62433`,
vzorce (5) dávají `E(L_C)=c*Q(m)+c/2+O(m^(-1/2))`.
Samotnou tuto asymptotiku permutací zde nepřebíráme jako vlastní důkaz;
její zdrojové ověření je v následujícím oddílu.
První tisk na str. 541 uvádí slabší zbytek `O(m^(1/2))`; není to
nepravdivá rovnost a nevedeme ji jako potvrzenou chybu.
Citované konstanty pro nejdelší ocas a největší `mu+lambda` souhlasí
s primárním článkem, jak dokládá následující oddíl.

Odpověď 15 je přesná pro všechna `m`: podmínky `f(x)!=x` jsou nezávislé,
takže pravděpodobnost žádného pevného bodu je `((m-1)/m)^m`. Ta jde
k `exp(-1)`; pravděpodobnost existence pevného bodu jde k `1-exp(-1)`.

## Primární zdroje k asymptotikám odpovědi 13

[Shepp a Lloyd (1966), str. 355](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Ordered-cycle-lengths-in-a-random-permutation.pdf)
uvádějí členy `c*n+c/2+o(1)`. Ostřejší zbytek použitý Knuthem potvrzuje
Gourdonův rozvoj zveřejněný také v článku, jehož je spoluautorem:
[Flajolet, Fusy, Gourdon, Panario a Pouyanne (2006), §5, str. 33](https://pouyanne.perso.math.cnrs.fr/hybridEjc.pdf).
Začíná `c*n+c/2-exp(gamma)/(24*n)+O(n^(-2))`, kde `gamma` je Eulerova
konstanta. Je tedy dostatečný pro knižní `O(1/n)` a přesný lesní rozklad
výše opravňuje jeho použití pro náhodná zobrazení.

[Flajolet a Odlyzko, Random Mapping Statistics (1990)](https://algo.inria.fr/flajolet/Publications/maps.ps.gz)
ve větách 5–7 analyzují stejný model rovnoměrné funkce. Vlastní značení
ocasu a cyklu mají oproti Knuthovi prohozené; zde používáme knižní význam.
Jejich konstanty pro nejdelší cyklus, nejdelší ocas a největší počet
různých stavů při volbě nejlepšího počátku jsou po řadě

```text
0.78248160099... * sqrt(m),
sqrt(2*pi)*log(2) * sqrt(m),
2.41490102372... * sqrt(m).
```

Protože `Q(m)~sqrt(pi*m/2)`, druhý koeficient je přesně `log(4)` krát
hlavní člen `Q`, třetí je `1.92681224269...` krát tento člen. Shodují se
s `Q(m)*log(4)` a `1.9268*Q(m)` v knize. Původní sazba vět zobrazena:
[věta 5](../images/flajolet-odlyzko-p13.png),
[věta 6](../images/flajolet-odlyzko-p14.png),
[věta 7](../images/flajolet-odlyzko-p16.png).

Konstanty byly navíc numericky přepočteny z integrálů v těchto větách;
[výsledek](../results/random-map-constants.json). Definujeme
`E1(v)=integral_v^infinity exp(-u) du/u` a

```text
I(v)=integral_0^v exp(-u)*(1-exp(-2*u/(exp(v-u)-1))) du/u.
c=integral_0^infinity (1-exp(-E1(v))) dv.
d=integral_0^infinity (1-exp(-E1(v)-I(v))) dv.
```

Zde `d=1.92681224269...`. Výpočet použil `scipy.integrate.quad`,
vnitřní substituci `u=v*t`, meze vnějšího integrálu 0 až 50 a požadované
absolutní/relativní tolerance `1e-9` (vnitřní `2e-11`). Je to numerická
kontrola zaokrouhlených konstant, nikoli intervalový důkaz chybové meze.
Rovnost dvou obvyklých integrálů pro `c`, totiž výše uvedeného a
`integral exp(-v-E1(v)) dv`, plyne integrací per partes.

Rozsah zdrojové kontroly: model, formulace vět, příslušné náčrty důkazů
a převod normalizací. Neprohlašujeme nové úplné prověření všech analytických
odhadů těchto článků. Autorova kopie Flajolet–Odlyzko obsahuje například
zjevně nekonzistentní znaménka ve vzorcích (53)–(54); kvadraturu jsme
odvozovali z formulací vět, nikoli z tohoto mezikroku. To není nález
v TAOCP a nezapočítává se do jeho ledgeru.

## Výpočetní kontrola a errata

[verify_intro.py](../verify_intro.py) prošel všech 50 069 funkcí pro
`1<=m<=6`, rozložil každou na cykly a ověřil všechny počáteční stavy.
Přesné četnosti dvojic `(mu,lambda)`, počtů cyklů, pevných bodů a
nejdelších cyklů souhlasí s odděleně vypočítanými racionálními vzorci.
Výsledek je v [intro.json](../results/intro.json). Tyto konečné kontroly
nenahrazují obecné argumenty výše.

V `all2-prepre`, `all2-pre`, `all2`, `err2` a `err2.textxt`, stav
1. 11. 2026, nebyla nalezena změna těchto vzorců pro unární náhodné
zobrazení. Nová odpověď 19 z roku 2005 se týká odlišného modelu závislého
na `k` předchozích hodnotách; není oprávněním nahradit všude `m` číslem
`m^k`, protože přechody mezi k-ticemi mají pevnou strukturu.
