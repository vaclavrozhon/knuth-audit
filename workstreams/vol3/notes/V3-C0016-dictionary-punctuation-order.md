# V3-C0016 — dvouklíčové pravidlo nedává pořadí s interpunkcí

Confirmed, low. Odpověď §5-4, s. 585 / file 596, nejprve navrhuje
lexikografický klíč (α′,α), kde α′ sjednocuje velikost písmen. Potom
uvádí rozšířený příklad a < A < Å < a- < a. < … a říká, že v této
obecnější situaci α′ také odstraní akcenty, spojovníky a tečky.
Ponechaný sekundární lexikografický klíč α tento příklad nesplní.

Stačí tři řetězce a, A, a-. Jejich α′ je vždy a. Aby seřazení dvojic
splnilo první část a < A, musí sekundární abeceda mít znak a před A.
Pak ale řetězec a- lexikograficky předchází A, protože se rozhodne
již na prvním znaku. Dostaneme a < a- < A, nikoli vytištěné a < A < a-.
Umístění znaku spojovníku v abecedě na rozpor nemá vliv.

Základní řešení pro samotná velká/malá písmena je správné. Rozšířený
příklad vyžaduje další pravidlo pro sekundární klíč, nebo změnu příkladu;
pouhá uvedená úprava α′ nestačí. Nejde o tvrzení o skutečných pravidlech
nějakého konkrétního slovníku, ale o rozpor navrženého algoritmu s jeho
vlastním požadovaným výstupem.

Původní sazba file 596 prohlédnuta. Relevantní moderní vrstvy jsou v
sources/opening-errata-review.json; doplněná kontrola prvního vydání
v sources/dictionary-order-errata-review.json. all3-prepre, all3-pre,
all3, err3 a err3-1e neobsahují odpovídající opravu. Dodatek s. 585
z 14. 9. 2019 se týká kódu odpovědi 8. Historické odpovědi začínají
na 571; příslušné okolí 571–576 neobsahuje opravu dictionary order.
Prvenství/fyzický výtisk neověřeny.
