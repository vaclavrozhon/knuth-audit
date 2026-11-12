# V2-C0156 — chybný mezikrok v matici svědků

**Confirmed.** §4.5.4–24, odpověď str. 663: přechod

```
q((n-1)/4+1)+min(b_n+1,r) <= qn/3+min(n/4,r)
```

není platný. Pro `n=9,N=12,q=1,r=3` je `b_n=2`
(silným testem projdou nenulové zbytky 1 a 8), takže by
nerovnost zněla `6<=21/4`. Celý tištěný řetězec mezí je
`5<=6<=21/4=21/4<=11/2<=6`; první chybný krok je zjevný.

Skutečný řádek má pouze tři nuly: sloupce 8, 9, 10.
Výsledná věta o nejvýše `floor(lg N)` základech zůstává správná.
Stačí zachovat odečtení sloupce 1 a počítat zbytkový interval
bez nuly modulo n:

```
Z <= q(b_n+1)+min(b_n,r)-1
  <= qn/3+min(n/4,r)-1
  <= N/2-1.
```

První řádek odpovědi navíc zahrnuje `n=1` podmínkou `1<=n<=N`,
zatímco zadání na414 požaduje `1<n<=N`; rozsah řádků má tuto
podmínku převzít. Všechny skutečné složené liché řádky mají `n>=9`,
jak opravený argument potřebuje. Obě opravy téhož maticového
argumentu jsou evidovány pod jedním ID.

Vizuální doklad [663 ve větším rozlišení](../images/vol2-p663-detail.png),
[zadání414](../images/vol2-p414.png). Všechny čtyři vrstvy errat
i aktuální `err2.textxt` prohledány, odpovídající oprava nenalezena.
[Obecný důkaz](primality-deterministic.md), §1–2, a
[přesný výpočet](../results/primality-deterministic.json) dokládají
protipříklad i nápravu. Novější fyzický dotisk a priorita neověřeny.
Draft neodeslán.
