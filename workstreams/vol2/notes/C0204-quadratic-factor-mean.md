# V2-C0204: chybný průměr počtu ireducibilních kvadratických faktorů

Stav: **confirmed**. §4.6.2–1, strana 678, poslední řádek hranaté poznámky.
Původní sazba: `images/vol2-p678.png`.

Pro p=n=2 jediná ireducibilní kvadratika x²+x+1 tvoří jeden ze čtyř
monických polynomů. Průměrný počet kvadratických faktorů je 1/4.
Tištěný vzorec `1/2-(1/2)p^(-2 floor(n/2))` dává 3/8.

Počet ireducibilních kvadratik je A=p(p−1)/2 a pravděpodobnost
dělitelnosti j-tou mocninou jedné z nich je p^(-2j), pokud 2j<=n.
Správný průměr s násobností je tedy
`A sum_{j=1..floor(n/2)} p^(-2j) = p/(2(p+1)) (1-p^(-2 floor(n/2)))`.
Tato chyba je nezávislá na C0203. Důkaz a výčet:
[berlekamp.md](berlekamp.md), §2, a `results/berlekamp.json`.

Prohledáno všech šest vrstev errat; záznam
`sources/polynomial-factorization-errata.txt`, 4. listopadu 2026.
Odpovídající oprava nenalezena. Fyzický dotisk a prvenství neověřeny;
návrh v reports je neodeslaný.
