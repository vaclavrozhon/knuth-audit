# V2-C0206: minimální polynom v úloze 14 může mít stupeň 1

Stav: **confirmed**. §4.6.2–14, strana 681, tvrzení `2<=k<=r`.
Zadání na straně 456 požaduje jen v^p=v modulo u, deg(v)<deg(u);
nekonstantnost v nepožaduje. Obě původní stránky byly zobrazeny.

Nad F_2 vezměme u=x(x+1), v=1. Vstup u má dva různé ireducibilní
faktory, takže r=2. Jediná konstanta s s gcd(u,v−s) nejednotkovým
je s=1; hledaný polynom je w(T)=T+1, tedy k=1. V matici algoritmu N
jsou již první dva řádky stejné a první závislost vznikne v řádku 1.

Obecně k je počet různých hodnot v na faktorech u, proto
`1<=k<=min(p,r)`. Hodnota k=1 nastává právě pro konstantní v.
Oprava: buď spodní mez 1, nebo výslovný předpoklad nekonstantnosti v.
Samotný algoritmus pracuje správně i pro konstanty; nález se týká
pouze deklarované spodní meze. Důkaz a 614 kontrol minimálních polynomů
jsou v [berlekamp.md](berlekamp.md), §5, a `results/berlekamp.json`.

Šest vrstev errat prohledáno 4. listopadu 2026; odpovídající oprava
nenalezena. Protokol: `sources/polynomial-factorization-errata.txt`.
Nejnovější fyzický dotisk a prvenství neověřeny. Nic neodesláno.
