# V2-C0169: Znaménko v násobení norem

Stav: **confirmed** vůči dostupným zdrojům.

Zadání4.5.4-45 na417 a Fact2 odpovědi na670 mají x=x1*x2−a*y1*y2. Se současným y=x1*y2+x2*y1 musí být v x plus. Pro a=2 a obě dvojice(1,1) je součin norem1, tištěný výsledek má normu−7. Dva výskyty téže chyby.

Obecný důkaz a rozsah jsou v [auditu úlohy45](norm-equations.md).
Sazba417/670/671 byla přečtena vizuálně. Všechny čtyři řady errat
a aktuální TeX byly prohledány3.11.2026. Známá oprava6.2.1998
na670 řeší jiný překlep (y_2 versus y²); zde uvedenou chybu neopravuje.

Doklady: `images/vol2-p417.png`, `images/vol2-p670.png`,
`images/vol2-p671.png`, `images/all2-prepre-rsa-p42.png`.
Výpočty a jejich limity: `verify_norm_equations.py`,
`results/norm-equations.json`. Pro C0172 stačí přímé dosazení2²−1²=3.

Pozdější fyzický dotisk a priorita nálezu nejsou ověřeny.
[Návrh hlášení](../reports/C0169-norm-composition-sign-draft.txt) zůstává neodeslaný.
