# V2-C0128: přesný logaritmus zaměněný za jeho horní zaokrouhlení

Stav: **confirmed**, drobná chyba značení v doplňujícím příkladu.
§4.5.2-40, odpověď na str.646. Hlavní algoritmus a časová mez jsou správné.

Odpověď nejprve definuje `m=lg max(|u|,|v|)`. V následující poznámce
pro `u=1,v=3*2^k-1,k>=2` uvádí `m=k+2`. Ve skutečnosti

```text
m = k+lg(3-2^-k),    k+1 < m < k+2,    ceil(m)=k+2.
```

Nejmenší uvedený případ je k=2, tedy u=1,v=11: m=lg11, nikoli4.
Tištěné počty posunů s=2k a návštěv K2 t=k+4 jsou správné;
pro tento příklad jsou4 a6. Obecný důkaz i přesná stopa jsou
v `gcd-variants.md` a `results/gcd-variants.json`.

Minimální oprava: v poznámce nahradit `m=k+2` výrazem
`ceil(m)=k+2`, případně uvést přesnou hodnotu logaritmu.
Není potřeba měnit definici m ani hlavní důkaz.

Sazba byla zkontrolována na `images/vol2-p646.png` a výřezu
`images/gcd-kung-logarithm.png`. Všechny čtyři vrstvy errat
`all2-prepre`, `all2-pre`, `all2`, `err2` byly prohledány2026-11-02
podle strany, čísla odpovědi, autorů i obsahu; tato oprava nenalezena.
Nový fyzický dotisk ani prvenství neověřeny; hlášení neodesláno.
