# V2-C0171: Nerovnoměrnost při vynechání nulových souřadnic

Stav: **confirmed** vůči dostupným zdrojům.

Odpověď4.5.4-45, první odstavec671: výběr u,v z1,…,n−1 nezaručuje přesnou rovnoměrnost s. Pro n7,a3,b1 mají jednotky1,…,6 četnosti4,4,8,4,8,8; všechny předtesty procházejí. Opravený výběr všech zbytků vyžaduje odpovídající úpravu větvení.

Obecný důkaz a rozsah jsou v [auditu úlohy45](norm-equations.md).
Sazba417/670/671 byla přečtena vizuálně. Všechny čtyři řady errat
a aktuální TeX byly prohledány3.11.2026. Známá oprava6.2.1998
na670 řeší jiný překlep (y_2 versus y²); zde uvedenou chybu neopravuje.

Doklady: `images/vol2-p417.png`, `images/vol2-p670.png`,
`images/vol2-p671.png`, `images/all2-prepre-rsa-p42.png`.
Výpočty a jejich limity: `verify_norm_equations.py`,
`results/norm-equations.json`. Pro C0172 stačí přímé dosazení2²−1²=3.

Pozdější fyzický dotisk a priorita nálezu nejsou ověřeny.
[Návrh hlášení](../reports/C0171-norm-sampling-uniformity-draft.txt) zůstává neodeslaný.
