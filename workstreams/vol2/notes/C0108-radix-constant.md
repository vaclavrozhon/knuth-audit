# V2-C0108: příliš silná nutná podmínka konstanty převodu

**confirmed**, 2. listopadu 2026. TAOCP2, třetí vydání, první dotisk
1997, §4.4-5, odpověď na straně 636. [Původní sazba](../images/vol2-p636.png)
byla vizuálně přečtena spolu s programem (4) na straně 321.

Nechť `D=10^n<w`, kde w je kapacita slova, a `0<=u<D` vstup.
Nahrazení `LDX =D=` instrukcí `LDX =c=` dává po dělení
`q=floor((wu+c)/D)`. Následující smyčka vydá `floor(Dq/w)`.
Odpověď tvrdí, že program funguje právě pro `D-1<=c<w`.
Pro nezápornou celočíselnou konstantu ve slově je správná podmínka

```text
D-gcd(w,D) <= c < w.
```

**Důkaz.** Položme g=`gcd(w,D)` a `wu=Da+r`. Zbytek r je buď
0, nebo alespoň g. Jestliže c>=D-g, pak q>=ceil(wu/D), a tedy
Dq>=wu. Zároveň Dq<=wu+c<wu+w. Výstup je proto u.
Naopak při `0<=c<D-g` a g<D existuje `0<u<D` se zbytkem r=g,
protože w/g je invertibilní modulo D/g. Pro tento vstup q=a
a výstup je `floor(u-g/w)=u-1`. Při g=D je dolní mez 0 a
nutnost je prázdná.

Konkrétně `w=64^5=1073741824`, n=1, D=10 a c=8. Všech deset
vstupů 0,...,9 se převede správně, ačkoli c<9. Pro binární w
a dovolené n lze často psát dolní mez `10^n-2^n`.
Knižní podmínka je postačující; chybná je její nutnost.

Přesný test ověřil 1904 konstant u malých kapacit, včetně selhání
pod ostrou mezí. Instrukční simulace kontrolovala i skutečné binární
kapacity MIX. Viz `results/radix-basic.json` a `notes/radix-basic.md`.

V `all2-prepre`, `all2-pre`, `all2`, `err2` nebyla nalezena oprava
odpovědi 5 ani této konstanty; kontrolovány byly také sousední
změny 323, 328, 635–638 a názvy instrukcí. Poslední fyzický dotisk,
priorita a odměna neověřeny. Návrh hlášení není odeslán.
