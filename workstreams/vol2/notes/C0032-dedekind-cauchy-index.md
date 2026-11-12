# V2-C0032: chybný index v Cauchyově odhadu

**Confirmed**, 1.11.2026. §3.3.3-12, druhý řádek odpovědi
na tištěné str.573 (strana585 souboru DjVu). Původní sazba
[strany573](../images/vol2-p573.png) byla vizuálně přečtena.

Označme `psi(x)=x−floor(x)−1/2` pro necelé x a `psi(x)=0`
pro celé x. Kniha definuje Dedekindův součet

```text
sigma(h,k,c)=12 sum_(j=0)^(k−1) psi(j/k) psi((hj+c)/k).
```

Odpověď tvrdí `sigma(h,k,c)^2 <= sigma(h,k,0)^2`.
První h na pravé straně musí být **1**. Pro h=2,k=5,c=1
jsou vektory desetinásobků hodnot psi

```text
psi(j/5):       (0, −3, −1, 1, 3)/10,
psi((2j+1)/5):  (−3, 1, 0, −1, 3)/10,
psi(2j/5):     (0, −1, 3, −3, 1)/10.
```

Jejich skalární součiny dávají `sigma(2,5,1)=3/5`,
`sigma(2,5,0)=0`. Vytištěná nerovnost tedy požaduje `9/25<=0`.

Je-li h nesoudělné s k a c celé, druhý vektor je permutací
prvního. Cauchyova nerovnost proto dává

```text
sigma(h,k,c)^2 <= (12 sum_j psi(j/k)^2)^2
                = sigma(1,k,0)^2,
sigma(1,k,0) = (k−1)(k−2)/k.
```

Zadání úlohy12, hlavní algoritmus i jeho použití k odhadu
korelace jsou správné. Přímý přesný výpočet a obecný důkaz
jsou v [kontrole sekce](dedekind.md), výsledek malého příkladu
v [JSON](../results/dedekind.json).

Všechny čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
a aktuální `sources/err2.textxt` byly prohledány1.11.2026 podle
strany573, Dedekind, Cauchy, sigma a okolních odpovědí.
Jediná nalezená oprava pro stranu573 je změna `math.` na
`Math.` v odpovědi9 z28.9.2002; týká se jiného místa.
Oprava uvedené nerovnosti nebyla nalezena.

Fyzický nejnovější dotisk ani prvenství nálezu neověřeny.
Anglický ASCII draft je připraven, nic nebylo odesláno.
