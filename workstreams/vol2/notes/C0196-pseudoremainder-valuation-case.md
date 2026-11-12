# V2-C0196: §4.6.1–14, strana 674: v důkazu chybí případ j>=k.

Stav: **confirmed**.

Z prvního koeficientu plyne p^min(j,k)|a_1, nikoli vždy p^j|a_1. Primitivní u=2x^5+10x^4+11x^3+x^2,v=2x^3+8x^2+4x+1 mají q=8x^2+8x-4,r=8x+4 a 8u=vq+r. Pro p=2,j=3,k=1 je a_1=4, nedělitelné 8. Samotná požadovaná dělitelnost r platí; oddíl 6 doplňuje obecný důkaz obou případů.

Původní sazba viz `images/vol2-p674.png`; matematický důkaz a přesné reprodukce v `notes/subresultants.md`, `verify_subresultants.py` a `results/subresultants.json`.

Prohledány all2-prepre, all2-pre, all2, err2, aktuální TeX a relevantní témata/staré stránky err2-2e; protokol `sources/subresultants-errata-search.txt`. Odpovídající oprava nenalezena. Nejnovější fyzický dotisk a prvenství neověřeny; nic neodesláno.
