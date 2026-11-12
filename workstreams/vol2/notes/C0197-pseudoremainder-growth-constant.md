# V2-C0197: §4.6.1, strana 433: doslovná koeficientová mez N^3 vynechává součty.

Stav: **confirmed**.

Pro u=x^3+x^2+x+1,v=x^2-x-1 je N=1, ale u=(x+2)v+(4x+3). Všechny následné poklesy stupňů jsou 1. Platná normální rekurence je H_i<=4H_(i-2)H_(i-1)^2; řešení H_i=(2N)^alpha_i/2 zachovává kvalitativní exponenciální růst. Nález se týká explicitního N^3, nikoli kvalitativního závěru nebo přibližnosti (27).

Původní sazba viz `images/vol2-p433.png`; matematický důkaz a přesné reprodukce v `notes/subresultants.md`, `verify_subresultants.py` a `results/subresultants.json`.

Prohledány all2-prepre, all2-pre, all2, err2, aktuální TeX a relevantní témata/staré stránky err2-2e; protokol `sources/subresultants-errata-search.txt`. Odpovídající oprava nenalezena. Nejnovější fyzický dotisk a prvenství neověřeny; nic neodesláno.
