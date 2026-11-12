# §2.4: všechny čtyři vrstvy errat

Použity lokální aktuální kopie `errata/text/{all1-prepre,all1-pre,all1,err1}.txt`;
kořen ověřil verze dne 1.11.2026. Prohledány stránky 424–434 a 605–607
i témata Data Table, COBOL, PL/I, CORRESPONDING, SCOPE, Dahm, Lawson,
Algorithm A/B/C, stack a exhausted. OCR sloužilo k navigaci.

Přímo zobrazené příslušné originály: `all1-prepre` strany 28,46;
`all1-pre` strana 18; `all1` strany 10,15; `err1` strany 9,14.
Obrazy jsou v `../images/`. Strana `all1-pre-page20.png` byla také otevřena,
ale není dokladem níže uvedených oprav; správný doklad starších nových
pojmenování je strana 18.

| Kniha | Datum | Obsah a posouzení |
|---|---|---|
| 426 ř.8 | 26.10.1998 | Čárka v MONTH, DAY, and YEAR; redakční. |
| 426 ř.9 | 26.12.2002 | DAY, MONTH, YEAR → MONTH, DAY, and YEAR. Párování jde podle jmen, ne podle fyzického pořadí polí; oprava je správná. |
| 428 ř.−9 | 20.9.1997 | memory location → memory allocation; návaznost na úmluvu o AVAIL. |
| 430 ř.6 | 8.5.2000 | P=PREV(P) → přiřazení P←PREV(P). B5 má opustit kandidáta. |
| 430 ř.−9 | 15.10.2007 | Rozsah j<n−1 a doplnění rodičovství posledního kvalifikátoru vzhledem k oběma kořenům. Oprava odstraňuje odkaz na neexistující A_n. |
| 431 ř.16 | 31.1.2008 | qualifications → complete qualifications; přesně invariant C3, žádné přeskočené úrovně. |
| 432 ř.−11 | 20.9.1997 | Opraveny uvozovky a spojka mezi dvěma testy NAME. |
| 433 poslední řádek | 22.1.1999 | A_(i+1) → A_(j+1) v úloze 6; oprava indexu. |
| 433 ř.14 | 7.7.2023 | Lawsonova citace doplněna o 74–75. Primární autorův text a metadata souhlasí; rozsah viz sources.md. |
| 430 za (8) | 20.5.2024 | Výslovné „or both“ u elementárních položek. C2 již správně používá inkluzivní logické OR. |
| 606 odp.12 | 6.1.2011 | Algoritmus varianty přejmenován na B'. |
| 606 odp.14 až 607 | 6.1.2011 | Varianta C přejmenována na C'. |
| 607 ř.1–9 | 24.6.2016 | V některých dotiscích vypadly čárky u názvů kroků C'; oprava označení. |
| 605 odp.6 | 18.11.2023 | Odkazy B3,B6,B2 → B3',B6',B2'. |
| 606 odp.12 | 7.7.2023 | Odkazy B2–B5 → B2''–B5'', odlišení od PL/I varianty B' v odpovědi 6. |

Při čtení se změny aplikují v časovém pořadí: dvě varianty B mají nakonec
označení B' (PL/I) a B'' (SCOPE). Navazující známá oprava Appendix C na 629
ze 17.4.2011 rozlišuje B' 605 a B'' 606; jde o indexové pojmenování, nikoli
o dodatečnou změnu kroků konstrukce tabulky.

Žádná z vrstev nemění EOF odpovědi 13 ani sentinel `(0,NULL)` algoritmu A.
Nový nález C0061 tedy není některou ze známých oprav názvů B'/B''/C'.
Jeho úplné doložení, včetně nejpříznivějšího výkladu EOF, je ve zmrazeném
`scope-builder-eof.md`. V témže rozsahu nebylo nalezeno další nové erratum.

Opravy 607 odpovědi 6 patří §2.5, nikoli §2.4-6; při vyhledávání byly
rozlišeny. Stejně tak horní část 605 patří ještě §2.3.5-12 a není součástí
tohoto bloku. Fyzický výtisk knihy nebyl ověřován.
