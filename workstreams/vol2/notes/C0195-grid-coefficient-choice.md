# V2-C0195: §4.6.1–16, strana 675: součet stupňů vyžaduje vhodný výběr koeficientů.

Stav: **candidate**.

Libovolný nenulový koeficient je přípustný pro součinovou mřížkovou mez. Nezaručuje však sum d_j<=d: pro f=x+y a koeficient x^0 rovný y máme d_1=d_2=1, d=1. Volba vedoucího koeficientu v každém kroku dokazuje správný závěr. Existenční čtení textu je správné, proto pouze interpretační kandidát; Schwartzův–Zippelův odhad není vyvrácen.

Původní sazba viz `images/vol2-p675.png`; matematický důkaz a přesné reprodukce v `notes/subresultants.md`, `verify_subresultants.py` a `results/subresultants.json`.

Prohledány all2-prepre, all2-pre, all2, err2, aktuální TeX a relevantní témata/staré stránky err2-2e; protokol `sources/subresultants-errata-search.txt`. Odpovídající oprava nenalezena. Nejnovější fyzický dotisk a prvenství neověřeny; nic neodesláno.
