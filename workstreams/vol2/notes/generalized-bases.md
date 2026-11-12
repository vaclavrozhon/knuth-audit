# §4.1: obecné váhy a binární báze (úlohy 26 a 30)

Kontrola 2. listopadu 2026. Původní sazba: strany 211–212 a 608–610,
DjVu strany 223–224 a 620–622. Přečteno v předchozím průchodu celé §4.1.
Úloha 26 je správná; níže je doplněn naznačený důkaz nutnosti, včetně
případu divergentní kapacity. Úloha 30 je správná po známé opravě
absolutní hodnoty z 3. července 2025. Nový nález v tomto bloku není.

## 1. Úloha 26: kapacita nižších pozic

Váha `beta_k` je kladná hodnota jedné jednotky na pozici `k`; indexy
probíhají všechna celá čísla. Váhy přísně rostou, klesají k nule směrem
k zápornému nekonečnu a rostou neomezeně směrem ke kladnému nekonečnu.
Na pozici `k` jsou povoleny celé cifry `0,...,c_k`, kde `c_k >= 1`.
Přípustný zápis má nejvyšší nenulovou cifru a nekonečně mnoho cifer
menších než jejich maximum. Poslední podmínka vylučuje zobecněné ocasy
samých devítek. Definujme kapacitu

```
T_n = sum_{k <= n} c_k beta_k,      0 < T_n <= infinity.
```

Tvrdíme: každé kladné reálné číslo má právě jeden přípustný zápis právě
tehdy, když `beta_(n+1) = T_n` pro všechna `n`.

**Postačitelnost.** Při rovnosti jsou všechny kapacity konečné a odečtením
sousedních rovností dostaneme `beta_(n+1) = (c_n+1) beta_n`.
Pro `x > 0` zvolme `n` s `beta_n <= x < beta_(n+1)`. Postupně dolů
volíme `a_k = floor(r / beta_k)` a odečítáme `a_k beta_k` od zbytku `r`.
Před krokem `k` platí `0 <= r < beta_(k+1)`; proto `a_k <= c_k`
a po kroku `0 <= r < beta_k`. Zbytky konvergují k nule, takže součet
je `x`. Žádný výsledný ocas nemůže být samé maximum: měl by hodnotu
`T_m = beta_(m+1)`, zatímco zbytek před jeho konstrukcí je přísně menší.

U dvou různých zápisů vezměme nejvyšší pozici `r`, na které se liší.
Rozdíl tamních příspěvků má absolutní hodnotu alespoň `beta_r`.
Nižší cifry ho mohou kompenzovat nejvýše o
`T_(r-1) = beta_r`. Rovnost by vyžadovala v jednom zápisu samá maxima
na všech nižších pozicích a v druhém samé nuly. První možnost je zakázána.

**Nutnost: mezera.** Je-li `beta_(n+1) > T_n`, žádné číslo v otevřeném
intervalu `(T_n, beta_(n+1))` nelze zapsat. Zápis s nejvyšší pozicí nejvýše
`n` dává nejvýše `T_n`; při vyšší pozici dává alespoň `beta_(n+1)`.

**Nutnost: překryv.** Zbývá případ `beta_(n+1) <= T_n` pro každé `n`.
Potřebujeme následující tvrzení, které nevyžaduje konečnost `T_n`:
každé `0 <= x < T_n` má přípustný ocas používající jen pozice `k <= n`
(pro nulu připouštíme pomocný nulový ocas).

Použijeme omezenou hladovou volbu

```
a_k = min(c_k, floor(r / beta_k));
r   = r - a_k beta_k.
```

Před krokem `k` platí `r < T_k`. Zvolí-li se maximum, potom
`r_new < T_k - c_k beta_k = T_(k-1)`; tato rovnost se čte v rozšířených
nezáporných reálných číslech a odečítá jen konečné číslo. Nezvolí-li se
maximum, pak `r_new < beta_k <= T_(k-1)`. Invariant tedy zůstává platný.
Cifry nemohou od jisté pozice dolů být samá maxima: při konečné kapacitě
by jejich součet převýšil tehdejší zbytek, při nekonečné kapacitě by
konečné částečné součty nakonec převýšily konečný zbytek. Nekonečně často
se tedy zvolí menší cifra; po těchto krocích je zbytek menší než `beta_k`.
Monotónnost nezáporných zbytků a `beta_k -> 0` dokazuje jejich limitu nula.

Pokud nyní `beta_(n+1) < T_n`, zvolme konečné
`x` v `(beta_(n+1), T_n)`. Má zápis jen na pozicích nejvýše `n`.
Současně můžeme napsat cifru `1` na pozici `n+1` a zapsat
`x-beta_(n+1)` na nižších pozicích podle právě dokázaného tvrzení.
Oba zápisy jsou přípustné a různé. Tím je nutnost dokončena.

Závěrečná charakterizace smíšených celočíselných základů v zadání
plyne z `beta_(n+1) = (c_n+1) beta_n`; opačný směr dává teleskopický
součet a limita vah k nule. Žádný numerický test nemá nahradit tento
obecný důkaz.

## 2. Úloha 30(a–b): právě jeden lichý prvek

Binární báze je posloupnost celých čísel `b_j`, v níž každé celé číslo
má právě jeden zápis jako součet konečné podmnožiny jejích indexů.
Prázdná podmnožina reprezentuje nulu; proto žádné `b_j` není nula.

Označme `A_j` množinu čísel, jejichž zápis index `j` nepoužívá.
Jednoznačnost dává rozklad `Z = A_j` disjunktně sjednoceno s `A_j+b_j`.
Členství v `A_j` se tedy při posunu o `b_j` změní na opačné a při posunu
o `2b_j` se zachová. Pro různé `j,k` má průnik `C = A_j intersect A_k`
periodu `L = 2 abs(b_j b_k)`, společný násobek obou period.
Čtyři množiny

```
C, C+b_j, C+b_k, C+b_j+b_k
```

tvoří disjunktní rozklad celých čísel: odpovídají čtyřem možnostem výběru
indexů `j,k`. V cyklické grupě zbytků modulo kladné `L` mají stejný počet
prvků, takže `4` dělí `L`. Obě `b_j,b_k` nemohou být lichá.
Alespoň jedno liché být musí, aby bylo možné reprezentovat jedničku.

Každé sudé číslo má zápis bez jediného lichého prvku. Jeho odstraněním
a vydělením všech ostatních prvků dvěma tedy opět vznikne binární báze.
Iterací dostaneme právě jeden původní prvek s každým exponentem dvojky:
po přeuspořádání `b_k = 2^k d_k`, kde `d_k` je liché. Žádný původní
prvek nezůstane stranou, neboť nenulové celé číslo je dělitelné jen
konečně mnoha mocninami dvojky.

Pro libovolnou posloupnost lichých `d_k` jsou konečné zápisy již
jednoznačné: u dvou různých podmnožin jejich nejnižší rozdílný index
určuje nenulový rozdíl modulo následující mocninu dvojky. Samotná
existence zápisů z lichosti neplyne; tu kontrolují další části.

## 3. Úloha 30(c): znaménka +1 a −1

Při konečně mnoha kladných prvcích by všechny konečné součty měly
společnou horní mez; obdobně pro záporné prvky dolní mez. Obě znaménka
se proto musí vyskytovat nekonečně často.

Naopak pro takovou posloupnost cifru na pozici `k` vynucuje parita
aktuálního zbytku `r`: `epsilon = r mod 2`, poté
`r := (r-epsilon d_k)/2`. Při `abs(r) >= 2` se absolutní hodnota přísně
zmenší. Zbytek `r = +/-1` může stagnovat jen při `d_k = -r`;
nejbližší výskyt `d_k = r` ho změní na nulu. Algoritmus proto končí.
Jeho kroky i obecná jednoznačnost odpovídají tištěné odpovědi.

## 4. Úloha 30(d): konečné certifikáty obou period

Pro periodická lichá `d_k` slučme celou periodu kroků do mapy `F`
zbytku `r`. Pro periodu `(7,-13)` dostáváme

```
F(4q+r) = q+t_r,   r = 0,1,2,3,   t = (0,5,7,-1).
-7/4 <= F(n)-n/4 <= 13/2.
```

Pro `n >= 9` platí `-2 <= F(n) < n`, pro `n <= -3` platí
`n < F(n) <= 8`. Po konečně mnoha krocích tedy přijdeme do `[-2,8]`.
Tento interval je invariantní a všechny jeho body dosáhnou nuly:

```
3 -> -1 -> -2 -> 6 -> 8 -> 2 -> 7 -> 0;
4 -> 1 -> 5 -> 6;   0 -> 0.
```

Původní rozklad jedničky souhlasí přesně:

```
7*2^0 - 13*2^1 + 7*2^2 - 13*2^3 - 13*2^5 - 13*2^9 + 7*2^10 = 1.
```

Pro dodatečný příklad s periodou `(5,-3,3)` platí

```
F(8q+r) = q+t_r,   t = (0,-2,1,-1,-1,0,0,1);
-17/8 <= F(n)-n/8 <= 3/4.
```

Mimo `[-2,2]` se absolutní hodnota přísně zmenšuje. Uvnitř stačí
`2 -> 1 -> -2 -> -1 -> 0` a pevný bod nula. Obě periody tedy
skutečně vytvářejí binární bázi všech celých čísel.

[Samostatný ověřovač](../verify_binary_bases.py) odvozuje mapy přímo
z jednotlivých dělení, přesnými zlomky ověřuje meze a všechny malé
trajektorie, rekonstruuje každé celé číslo v `[-10000,10000]` a nezávisle
sčítá všech `2^14` podmnožin prvních 14 vah každé báze. Testuje jejich
různost i navrácení původní podmnožiny. Celkem 40002 rekonstrukcí,
32768 podmnožin a 2412 kontrol posunutých skupinových kroků prošlo.
Běh 98962 skončil s exit 0; [výsledky](../results/binary-bases.json)
a [log](../results/binary-bases.log) zachovány, úspěšné testy neopakovány.

## 5. Errata a prameny

Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2` i aktuální uložený
TeX podle stran 211–212, 608–610 a pojmů. Přehled je v
[positional-errata-excerpts.txt](../sources/positional-errata-excerpts.txt).
Oprava 3. července 2025 na straně 609 nahrazuje ve dvou výskytech
`2b_j b_k` výrazem `2 abs(b_j b_k)`; výše je důkaz již opravený.
Jiná relevantní oprava úloh 26 a 30 nebyla nalezena.

Mendelsohnův článek z roku 1952 (str. 45–55) nebyl získán v původní sazbě.
Bibliografické odkazy se rozcházejí v čísle svazku 46/47; bez originálu
z toho neděláme nález. Matematický závěr 26 byl dokázán nezávisle.
De Bruijnův související zdroj z roku 1950 se nepodařilo stáhnout
(HTTP 403, [metadata](../sources/debruijn-1950-bases.json)).
Závěry 30 jsou doloženy vlastními úplnými důkazy, nikoli předstíranou
četbou nedostupného článku.
