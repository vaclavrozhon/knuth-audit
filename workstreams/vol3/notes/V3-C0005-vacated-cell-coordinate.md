# V3-C0005 — souřadnice uvolněné buňky

Potvrzená drobná chyba v §5.1.4, s.56 / file67, první odstavec. Po
Algorithm S je právě uvolněná buňka P_(r−1),s, nikoli vytištěná P_rs.
Sazba S1–S5 na55 a návaznosti na56 zobrazena.

Stačí jednoprvková tabulka P11=1. S1 nastaví r=s=1; S2 pokračuje.
S3 porovná dvě nekonečna (zvláštní relace dovoluje jejich rovnost),
S5 zapíše P11=∞ a zvýší r na2. S2 nyní skončí s P21=∞.
Uvolněna je (1,1), kdežto pokyn vložit smazanou1 do P_rs vloží1 do
(2,1), mimo původní tvar. Obecně poslední S5 vždy posune r o1 za
uvolněnou buňku. Obrázek v knize správně zachovává původní tvar.
Oprava se týká následného uložení, samotné mazání Algorithm S funguje.

Relevantní all3-prepre/all3-pre/all3/err3 a historické err3-1e s.54–65
neobsahují odpovídající opravu. Výřezy v sources/tableaux-errata-review.json;
sazba images/tableaux-file-066.png a067.png. Fyzický výtisk a prvenství
neověřeny. Ruční průchod stačí, žádná enumerace.
