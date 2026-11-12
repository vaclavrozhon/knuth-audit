# V2-C0193: §4.6.1–13, strana 674: v transformačním vzorci mají být u_(j+1),g_(j+1).

Stav: **confirmed**.

Pravá strana má u_j,g_j, ač levá transformuje u_(j+1),g_(j+1). Vezměme w=x, ell=1, u_1=x^3+3x+1,u_2=x^2+1. Potom u_3=2x+1 a po násobení vstupů w máme U_3=2x^2+x,G_3=2. Tištěný předpis dává x^3+x a 1. Obecná oprava a indukce jsou v oddílu 5 hlavní poznámky.

Původní sazba viz `images/vol2-p674.png`; matematický důkaz a přesné reprodukce v `notes/subresultants.md`, `verify_subresultants.py` a `results/subresultants.json`.

Prohledány all2-prepre, all2-pre, all2, err2, aktuální TeX a relevantní témata/staré stránky err2-2e; protokol `sources/subresultants-errata-search.txt`. Odpovídající oprava nenalezena. Nejnovější fyzický dotisk a prvenství neověřeny; nic neodesláno.
