# V2-C0205: záporný exponent v generující funkci počtu faktorů

Stav: **confirmed**. §4.6.2–5, strana 680, řádek 3: `z^(-m)` má být `z^m`.
Originál byl zobrazen v `images/vol2-p680.png`.

Počty `a[m,w]` jsou polynomy ve w dané Möbiovým vzorcem odpovědi 4.
Pro w=1 jsou a[1,1]=1 a a[m,1]=0 pro m>1. Tištěný výraz pak dává
`1/(1-p/z)` místo správné generující funkce všech monických polynomů
`1/(1-pz)`. Zejména první výraz nemá správný konstantní člen.

Prohození p,w v koeficientu a[m,w] je **správné**: jde o Wittovu symetrii,
jejíž důkaz je v [berlekamp.md](berlekamp.md), §3. Zjištění se týká
výhradně znaménka exponentu, nikoli této symetrie.

Známá oprava z 30. června 2002 doplňuje na stejném řádku závorku;
originální errata strana 42 byla zobrazena a exponent neopravuje.
Šest vrstev errat bylo prohledáno 4. listopadu 2026, viz
`sources/polynomial-factorization-errata.txt`. Odpovídající oprava
nenalezena. Fyzický dotisk a prvenství nejsou ověřeny; nic neodesláno.
