# V2-C0172: Nesprávná větev příkladu modulo8

Stav: **confirmed** vůči dostupným zdrojům.

Odpověď4.5.4-45, Fact1 na670 uvádí neřešitelnost x²±y²=3 modulo8. Minus má řešení x2,y1. Stačí ± nahradit plus; čtverce0,1,4 žádný součet3 nedají. Potřeba lichého n tím zůstává doložená.

Obecný důkaz a rozsah jsou v [auditu úlohy45](norm-equations.md).
Sazba417/670/671 byla přečtena vizuálně. Všechny čtyři řady errat
a aktuální TeX byly prohledány3.11.2026. Známá oprava6.2.1998
na670 řeší jiný překlep (y_2 versus y²); zde uvedenou chybu neopravuje.

Doklady: `images/vol2-p417.png`, `images/vol2-p670.png`,
`images/vol2-p671.png`, `images/all2-prepre-rsa-p42.png`.
Výpočty a jejich limity: `verify_norm_equations.py`,
`results/norm-equations.json`. Pro C0172 stačí přímé dosazení2²−1²=3.

Pozdější fyzický dotisk a priorita nálezu nejsou ověřeny.
[Návrh hlášení](../reports/C0172-norm-mod-eight-draft.txt) zůstává neodeslaný.
