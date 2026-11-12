# V2-C0170: Chybějící faktor v mřížové mezi

Stav: **confirmed** vůči dostupným zdrojům.

Odpověď4.5.4-45, Fact3 na670: mez pro minimum (zu+mv)²+|a|u² potřebuje faktor|m| před sqrt(4|a|/3). Pro a2,s17,z6,m2 je minimum2, zatímco tištěná mez sqrt(8/3)<2. Závěrečná mez t²≤4|a|/3 po opravě platí.

Obecný důkaz a rozsah jsou v [auditu úlohy45](norm-equations.md).
Sazba417/670/671 byla přečtena vizuálně. Všechny čtyři řady errat
a aktuální TeX byly prohledány3.11.2026. Známá oprava6.2.1998
na670 řeší jiný překlep (y_2 versus y²); zde uvedenou chybu neopravuje.

Doklady: `images/vol2-p417.png`, `images/vol2-p670.png`,
`images/vol2-p671.png`, `images/all2-prepre-rsa-p42.png`.
Výpočty a jejich limity: `verify_norm_equations.py`,
`results/norm-equations.json`. Pro C0172 stačí přímé dosazení2²−1²=3.

Pozdější fyzický dotisk a priorita nálezu nejsou ověřeny.
[Návrh hlášení](../reports/C0170-norm-lattice-factor-draft.txt) zůstává neodeslaný.
