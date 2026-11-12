# V2-C0250 — chybějící plus v identitě pro sudé pozice

6. listopadu 2026. **Confirmed / low**, §3.5, odpověď 29,
tištěná **596**, souborová **608**. Původní sazba nově zobrazena
v `images/vol2-p596.png`, včetně plného rozlišení. V rovnici bezprostředně
za „Therefore we find that“ chybí plus mezi první závorkou a druhým
součtem. Přilehlé výrazy tak tvoří součin namísto požadovaného součtu.

Při označení

```
A_n = (1/n) Σ_x s(x) ν_x(n),
B_n = (1/n) Σ_x (r(x)−s(x)) ν_x^E(n)
```

je v tisku `2k ν_0^E(n)/n = A_n B_n + O(1/n)`.
Správně má být `2k ν_0^E(n)/n = A_n + B_n + O(1/n)`.
Zde r(x), resp. s(x), počítá nuly na lichých, resp. sudých místech
slova délky 2k; horní E značí sudý index začátku.

## Přesný příklad pod všemi předpoklady úlohy

Položme k=1 a vezměme binární posloupnost s periodou **0011**, počínaje
X_0=0. Je 2-distribuovaná: její čtyři cyklické dvojice jsou právě
00, 01, 11, 10. Při n=4M a knižním počítání 1≤p≤n platí

```
ν_0^E(n)=M,           A_n=1/2,           B_n=0.
```

Na sudých místech začínají jen dvojice 00 a 11, u obou je r−s=0;
proto B_n mizí přesně, bez limitního přechodu. Ze 4M dvojic má právě
2M druhý bit nula, takže A_n=1/2. Tištěná rovnost by tudíž pro
všechna M vyžadovala `1/2=0+O(1/(4M))`, což je nemožné.

## Správný mezikrok a hlavní výsledek

Sečteme počty výskytů nul na všech 2k pozicích okna. Až na O(k²)
krajních příspěvků tím dostaneme

```
2k ν_0^E(n)
 = Σ_x (r(x)ν_x^E(n)+s(x)ν_x^O(n)) + O(k²)
 = Σ_x s(x)ν_x(n) + Σ_x(r(x)−s(x))ν_x^E(n) + O(k²).
```

Při pevném k vede dělení n k opravené rovnici. Následující odstavce
odpovědi už správně maximalizují **součet** obou členů. Obecný důkaz
v `white-parity.md`, §4, má rovněž správné plus; mez úlohy 29,
doplňkové binomické identity i optimální konstrukce úlohy 30 jsou
správné. Nový nález se týká pouze vytištěného pomocného vzorce.

## Vrstvy errat a rozsah potvrzení

6. listopadu 2026 prohledány `errata/text/all2-prepre.txt`,
`all2-pre.txt`, `all2.txt`, `err2.txt` a aktuální TeX
`errata/originals/err2.textxt` podle stran 182/596/597, čísla odpovědi
29, parity a okolních témat. Příslušné stránkové rozsahy byly přečteny.
Jediná oprava 596 v `all2-prepre` z 29. června 1999 mění `. We` na
`We`; odpovídá tečce před „We find“ v odpovědi 30, nikoli chybějícímu
plus v odpovědi 29. Oprava odpovědi 29 na 617 patří jiné sekci.
Žádná dostupná vrstva toto plus nedoplňuje.

Zadání 182 bylo nově zobrazeno. Vydání 3, první tisk 1997, file=printed+12.
Pozdější fyzický dotisk a prvenství neověřeny. Žádný program ani dlouhý
výčet se nespouštěl; příklad je přesný rozbor jedné čtyřciferné periody.
