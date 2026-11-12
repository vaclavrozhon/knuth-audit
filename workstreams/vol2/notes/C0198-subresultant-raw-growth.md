# V2-C0198: §4.6.1, strana 432 po (25): rozsah meze (26) pro normalizované hodnoty.

Stav: **candidate**.

Pro u=x^4+x^3+x^2+1,v=x^3-x^2-x+1 jsou normalizované zbytky 4x^2+x-1,-7x+11,32, ale C2 skutečně počítá poslední syrový zbytek 512. Při N=1,m=4,n=3 má (26) čtverec 32000<512^2. Normované hodnoty a determinantový důkaz jsou správné; sporné je pouze zahrnutí syrových mezivýsledků do formulace, proto kandidát.

Původní sazba viz `images/vol2-p432.png`; matematický důkaz a přesné reprodukce v `notes/subresultants.md`, `verify_subresultants.py` a `results/subresultants.json`.

Prohledány all2-prepre, all2-pre, all2, err2, aktuální TeX a relevantní témata/staré stránky err2-2e; protokol `sources/subresultants-errata-search.txt`. Odpovídající oprava nenalezena. Nejnovější fyzický dotisk a prvenství neověřeny; nic neodesláno.
