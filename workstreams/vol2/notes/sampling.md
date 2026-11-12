# V2-X0002: §3.4.2, algoritmy S a R

Kontrola dokončena 1. listopadu 2026 bez nového nálezu v uvedeném rozsahu.
Zdroj: algoritmy na tištěných str. 142–144, odpovědi 5, 6, 7, 9 a 11
na str. 591. Zobrazeny [S](../images/vol2-p142.png),
[R](../images/vol2-p144.png) a [odpovědi](../images/vol2-p591.png).
Relevantní vrstvy errat a sousední známé opravy jsou v [mapě](source-map.md).

## Předpoklady a výsledek

`N` je počet vstupních záznamů a `n` velikost vzorku; `1<=n<=N`.
Záznamy rozlišujeme podle pozic `1..N`, i kdyby jejich obsahy byly stejné.
Rovnoměrný vzorek znamená, že každá n-prvková podmnožina má pravděpodobnost
`1/C(N,n)`, kde `C(N,n)` je binomický koeficient. Náhodné volby jsou
nezávislé a mají ideální rovnoměrná rozdělení: u S spojité na `[0,1)`,
u R diskrétní na příslušné konečné množině. Závislosti konkrétního
pseudonáhodného generátoru ani zaokrouhlování zde nekontrolujeme.

Algoritmy S/R, jejich rovnoměrnost, ukončení, okamžik dokončení S,
velikost fyzického rezervoáru R a příklad §3.4.2-9 prošly. Případ `n=0`
je výslovně mimo vstupní podmínky; jeho selhání by nebylo chybou knihy.

## Algoritmus S

Po prohlédnutí `t` záznamů a výběru `m` z nich se další přijme s
pravděpodobností `(n-m)/(N-t)`. Dokud algoritmus neskončil, platí
`0<n-m<=N-t`. Při rovnosti je další přijetí jisté; nelze tedy přejít
za konec vstupu. Počet přijatých se zastaví přesně na `n`.

Pro konkrétní n-prvkovou podmnožinu můžeme po skončení doplnit imaginární
přeskočení zbývajících záznamů s pravděpodobností 1. Součin pravděpodobností
přijetí obsahuje v čitateli `n!`, součin přeskočení `(N-n)!` a společný
jmenovatel je `N!`. Každý vzorek má tedy pravděpodobnost `1/C(N,n)`.
To je tvrzení odpovědi 7, nejen rovnost pravděpodobností jednotlivých pozic.

Nechť `T` je počet přečtených záznamů při dokončení. Je to největší pozice
ve vybraném vzorku, takže

```text
Pr(T=k) = C(k-1,n-1)/C(N,n),  n<=k<=N.
```

Identity `k*C(k-1,n-1)=n*C(k,n)` a
`k*(k+1)*C(k-1,n-1)=n*(n+1)*C(k+1,n+1)` spolu se součtovou identitou
`sum_{k=r}^L C(k,r)=C(L+1,r+1)` dávají

```text
E[T] = n*(N+1)/(n+1),
E[T*(T+1)] = n*(N+1)*(N+2)/(n+2),
Var(T) = n*(N+1)*(N-n)/((n+1)^2*(n+2)).
```

Zde `E` značí střední hodnotu a `Var(T)=E[T^2]-E[T]^2` rozptyl.
Vzorce odpovídají odpovědím 5 a 6, včetně krajního případu `n=N`.

## Algoritmus R

Rezervoár je fyzický soubor všech někdy přijatých záznamů; tabulka `I`
má `n` odkazů na právě platný vzorek. Po příchodu záznamu číslo `t+1`
se rovnoměrně zvolí celé `M` od 1 do `t+1`. Při `M<=n` se nový záznam
přidá do rezervoáru a nahradí odkaz `I[M]`, jinak se přeskočí.

Indukcí předpokládejme rovnoměrný vzorek z prvních `t` pozic. Pro cílovou
n-prvkovou množinu `S` neobsahující `t+1` je pravděpodobnost výsledku
`(t+1-n)/((t+1)*C(t,n))`. Pokud `S` nový prvek obsahuje, předchozí vzorek
musel být `(S bez {t+1}) sjednoceno {x}`; takových možností `x` je
`t-n+1`. Každá přispěje `1/((t+1)*C(t,n))`, neboť právě jeden index
musí být nahrazen. V obou případech vychází `1/C(t+1,n)`.

Každý nový odkaz míří na poslední, dosud nepoužitou pozici v rezervoáru,
takže odkazy zůstávají různé. Fyzický soubor zachovává pořadí vstupu.
Jejich seřazení v R6 proto vydá právě aktuální vzorek v pořadí vstupu.

Označme `L` konečný počet záznamů v rezervoáru a `B_t` indikátor přijetí
záznamu číslo `t>n` (1 při přijetí, jinak 0). Pak
`L=n+sum B_t`. Indikátory jsou nezávislé, protože přijetí závisí pouze
na čerstvém `M`; `Pr(B_t=1)=n/t`. Pro pomocnou proměnnou `z` je
pravděpodobnostní vytvořující funkce `G(z)=E[z^L]` rovna

```text
G(z) = z^n * product_{t=n+1}^N ((t-n)/t + (n/t)*z).
```

Definujme harmonické součty `H_k=sum_{j=1}^k 1/j` a
`H2_k=sum_{j=1}^k 1/j^2`. Nezávislost dává

```text
E[L]   = n*(1+H_N-H_n),
Var(L) = n*(H_N-H_n) - n^2*(H2_N-H2_n).
```

To souhlasí s odpovědí 11. Pro `N=n` prázdný součin dává `L=n`
s jistotou. Příliš krátký vstup R1 explicitně odmítá.

## Konečné přesné kontroly

```sh
python3 workstreams/vol2/verify_sampling.py
```

[Skript](../verify_sampling.py) používá přesné racionální pravděpodobnosti
(`Fraction`), nikoli náhodnou simulaci. [Výsledek](../results/sampling.json):

- S: všechny `1<=n<=N<=12`, tedy 78 dvojic parametrů, 8 178 konečných
  podmnožin. Ověřeny pravděpodobnosti i oba momenty `T`.
- R: všechny `1<=n<=N<=8`, tedy 36 dvojic, 2 654 konečných stavů souboru
  a tabulky odkazů, 502 konečných podmnožin. Nezávisle porovnána distribuce
  velikosti souboru s koeficienty součinového vzorce `G(z)`.
- Příklad §3.4.2-9: rezervoár `1,2,3,5,9,13,16`, vzorek `2,5,16`;
  přesně odpovídá odpovědi v knize.

Vše prošlo. Odpověď 8, další metody přeskakování a algoritmus P nejsou
součástí uzavřeného bloku; jejich přečtení při navigaci není kontrolou.
