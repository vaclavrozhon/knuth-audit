# V2-C0203: v pravděpodobnosti kvadratického faktoru chybí 1−

Stav: **confirmed**. §4.6.2–1, strana 678, hranatá poznámka o faktorech
stupně 2. Sazba byla zobrazena v `images/vol2-p678.png`.

Pro p=n=2 jsou monické kvadratiky x², x²+1, x²+x, x²+x+1.
Pouze poslední má ireducibilní kvadratický faktor. Pravděpodobnost je 1/4.
Tištěný součet `sum_k binom(p(p-1)/2,k)(-1)^k p^(-2k)` je 3/4.
Je to pravděpodobnost žádného kvadratického faktoru; před součet patří 1−.
Obecné odvození a kontrola ostatních mezí: [berlekamp.md](berlekamp.md), §2.

Šest vrstev errat včetně posunutých stran druhého vydání bylo prohledáno
4. listopadu 2026; protokol `sources/polynomial-factorization-errata.txt`.
Odpovídající oprava nenalezena. Přesný výčet a výsledky jsou v
`verify_berlekamp.py` a `results/berlekamp.json`.
Fyzický nejnovější dotisk a prvenství nejsou ověřeny. Nic neodesláno.
