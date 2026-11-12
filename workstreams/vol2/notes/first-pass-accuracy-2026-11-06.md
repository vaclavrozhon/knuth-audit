# §4.2.2 — první průchod analýzou přesnosti

6. listopadu 2026, V2-X0135. Přečteny celé původní strany229–245
a odpovědi §4.2.2 na613–617. Všech31 zadání spárováno s odpověďmi
a archivními důkazy. Převzaty `accuracy-basic/exact/drift/diamond`,
`accuracy-compensation/product-mod/iterations/fcmp`, `unnormalized`,
`intervals` a `accuracy-context`. Žádný nový nález ani výpočet.

Posouzeny algebraické zákony, porovnávací relace, věty A–D, kompenzované
sčítání a násobení, stabilita iterací, intervalová a nenormalizovaná
aritmetika. Již uzavřené dlouhé důkazy, censy a experimenty se neopakují.
Podmínka bez přetečení/podtečení je součástí platnosti těchto vět.

Závažnosti podle dopadu: C0083 **low** (nula v implikaci36), C0084
**low** (jednociferná ternární výjimka v odpovědi15 i její opravě),
C0085 **low** (pouze liché zaokrouhlení při b2,p1, nikoli doporučená
binární varianta), C0086 **low** (4n+2 kvadratických členů místo4n;
hlavní mez platí), C0087 **low** (nadbytečná nula v jednom příkladu
errata2020). C0089 **medium**: chybná horní mez intervalového součtu
nepokrývá všechny kombinace dovolených konců; znalost přesných SI
konstant je jiné zadání. C0090 **low**, starší primární příklady
vyvracejí domnělé prvenství Scarborough1930; neurčují absolutní prvenství.
Chyby nově zavedené v opravném textu nejsou již napravené známé chyby.

C0088 zůstává **candidate**: zachování počtu úvodních nul před
zaokrouhlením a po něm jsou odlišné interpretace. Obě v uvedeném
příkladu dávají hodnotu100; potvrzená chyba hodnoty tím doložena není.

Historické limity zůstávají: datum1750 u Johnsonova epigrafu nemá
archivním pramenem potvrzenou dataci; Tanneryho připsaná motivace
kompenzací nebyla v přečtené pasáži nalezena. To samo nevyvrací zdroj.
Nepřečtené články a prvenství z `accuracy-context.md` nejsou nově
ověřeny. Příklady kalkulaček a výkonnostní procenta se nereprodukují.

Celostránkový první průchod229–245 a613–616; 239 partial kvůli C0088,
241 partial také kvůli konkrétní neuzavřené Tanneryho atribuci.
617 partial: následující §4.2.3 ještě čeká na spárování. Kurzor246/file258.
