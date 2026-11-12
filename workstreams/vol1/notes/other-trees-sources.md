# §2.3.3: inventář, errata a primární prameny

Zdroj je třetí vydání, první dotisk 1997, soubor
books/taocp-vol1-ed3-print1-1997.djvu. Strana knihy p odpovídá straně
souboru p+15. Hlavní text je 348–359, úlohy 359–362 (před §2.3.4),
odpovědi 575–577. Všech 18 příslušných původních stran bylo přímo
zobrazeno; obrazy jsou images/vol1-file363-p348.png až
vol1-file377-p362.png a vol1-file590-p575.png až vol1-file592-p577.png.

Inventář má přesně 19 původních úloh, žádnou přidanou. Původní ratingy:
20,22,24,18,16,24,15,15,20,28,24,21,M29,40,40,M24,25,28,M27.
OCR u úlohy 13 nesprávně čte M25; obraz 361 potvrzuje M29.
V roce 2014 byly přidány odpovědi 14–15, nikoli nová zadání.

## Errata

Všechny čtyři lokální vrstvy byly prohledány podle stran i témat.
Jejich živou shodu se zdrojem kořen ověřil již 1. listopadu 2026
v této relaci. Strojový výpis s SHA256 je results/other-trees-errata.json.
Parser byl opraven, aby rozpoznával také Page bez hranice slova za
OCR značkou x; původní hranice chybně spojovala některé záznamy.

Je zde 20 různých položek, z toho oprava Hussein se opakuje v err1:

| Místo | Známá oprava nebo doplnění |
|---|---|
| 348 | Odstranění zbytku věty o LLINK, 15. 7. 1997 |
| 349 (1) | Opravené závorky lesního příkladu, 8. 8. 1997 |
| 351 F4 | Posun P+c místo P+1, 29. 8. 1997 |
| 352 | Dvě číselné opravy 6→5 a 60→50, 26. 12. 2002 |
| 353 Fig. 26 | Opravený rodičovský diagram, 21. 8. 1997 |
| 354 | Pairs of equivalent elements, 29. 8. 1997 |
| 355 | Roots of two trees, 29. 8. 1997 |
| 360-8 | Equivalent elements, 29. 8. 1997 |
| 360-9 | Equivalences, 29. 8. 1997 |
| 360-11 | A set of relations, 29. 8. 1997 |
| 360-11 | Nadbytečná levá závorka deklarace X, 25. 7. 1997 |
| 575-2 | Posun P−c místo P−1, 29. 8. 1997 |
| 577-17 | Posun P−c místo P−1, 29. 8. 1997 |
| 577-18 | INFO1 místo INFO, 24. 12. 2001 |
| 355 | Odkaz §7.4.1.1, 11. 11. 2021 |
| 576-10 | Odkaz §7.4.1.1, 11. 11. 2021 |
| 576-14,15 | Článek Ward–Zedan, 9. 9. 2014 |
| 349 | Přesnější popis nevyplněného RLINK, 1. 12. 2022 |
| 355 E3 | Dvě výslovné while smyčky, 7. 7. 2023 |
| 576-14,15 | Jméno Hussein místo Hussain, 1. 11. 2022 |

Příslušné původní PDF obrazy byly prohlédnuty: all1-prepre 23,24,42,43;
all1-pre 12,17; all1 9,15; err1 13. Část je sdíleným již přečteným
dokladem stromových nálezů a část nově v images/other-trees-errata-*.
Oprava §2.3.2-20 na p. 348 patří předchozí sekci a do počtu 20 nevstupuje.

## Přesný stav citací

Stažená data a neúspěšné přístupy jsou v sources/other-trees/.
Soubory downloads-*.json rozlišují status HTTP, finální URL, hash
a skutečný PDF od HTML odpovědi. Soubor končící pdf-attempt.txt
není přečtený článek. HTTP 429 salton-crossref.json je prázdný;
platná následná metadata jsou salton-crossref2.json.

| Citace v knize | Získaný primární doklad | Co ještě chybí |
|---|---|---|
| Salton, CACM 5 (1962), 103–114, p. 351 | Vydavatelská metadata přes Crossref, DOI 10.1145/366792.366828 | Text článku a přesné místo užití level order; ACM PDF 403 |
| Burks–Warren–Wright, MTAC 8 (1954), 53–57, úloha 2 | Vydavatelská metadata, DOI 10.1090/S0025-5718-1954-0061484-4 | Plných pět stran; oba AMS PDF přístupy 403 |
| Galler–Fischer, CACM 7 (1964), 301–303 a 506, hlavní text a úloha 11 | Metadata obou položek: 10.1145/364099.364331 a 10.1145/355586.364830 | Obsah obou textů a přesné porovnání rozšířeného algoritmu; první PDF 403 |
| McIlroy a Alan Tritter, odpověď 10 | Atribuce v původní knize přečteny | Nezávislý primární doklad této atribuce; vlastní důkaz obou úprav je hotov |
| Ward–Zedan, FAC 26 (2014), 993–1031, nové odpovědi 14–15 | Vydavatelská stránka 10.1007/s00165-013-0287-2 potvrzuje bibliografii a jméno Hussein; webový náhled autorova PDF ukázal úvod a obsah | Relevantní celé §5, zejména derivační důkaz a násobení; přímý autorův host není dosažitelný, vydavatelský PDF endpoint vrací HTML, alternativy a RG nebyly úspěšné |
| Pallo, Computer Journal 29 (1986), 171–175, odpověď 19 | Metadata 10.1093/comjnl/29.2.171 potvrzují článek a stránky | Vlastní článek a porovnání reprezentace; OUP 403 |
| Tamari, pařížská disertace 1951, odpověď 19 | Knižní atribuce a navazující křížový odkaz přečteny | Samotná disertace nebo přesný dostupný primární přetisk relevantního místa |

Primární odkazy jsou DOI uvedená v tabulce, např.
https://doi.org/10.1007/s00165-013-0287-2.
Autorův PDF je https://www.gkc.org.uk/martin/papers/trans-prog-t.pdf.
Katalogy a abstrakty nejsou vydávány za důkaz obsahu.
Metadata prvního Gallerova článku navíc píší Fisher, zatímco druhá
vydavatelská položka Fischer; tuto nekonzistenci metadat nepřenášíme
jako údajnou chybu Knuthova textu.

## Křížové odkazy a celkový stav

Převod z §2.3.2, diferenciátor a jeho vyšší arita byly přímo porovnány
s dokončeným auditem sousední sekce. Odkaz na §2.4 a úlohu 2.4-12
byl následně uzavřen úplnou kontrolou obou reprezentací a původních
stran350,434,606: liší se zahrnutím konce preorder intervalu. Viz
notes/multilinked-root-review.md a parallel/multilinked/notes/general-proofs.md,
část10. §7.4.1.1 je budoucí nedodaný oddíl,
nikoli důkaz, který by byl nutný pro zdejší vlastní O(log n) argument.

Odkaz §6.2.3-32 byl přímo přečten v originálu Volume 3 pp. 481 a 718;
obrazy jsou images/other-trees-vol3-p481.png a -p718.png.
Zadání porovnává pravé rotace s pravými velikostmi podstromů, odpověď
výslovně odkazuje zpět na podmínky §2.3.3-19 a uvádí minimum jako průsek.
Cíl odkazu je tedy správný. Nejde o audit všech sekundárních citací
navazující odpovědi ve Volume 3 ani o nezávislý důkaz priority z roku 1951.

Technicky je dokončen hlavní text i všech 19 úloh. Nová chyba nebyla
v tomto oddílu nalezena. Celkově zůstávají partial úlohy 2,10,11,14,15,19
a citace hlavního textu, výhradně v právě vyjmenovaném rozsahu pramenů.
Vlastní obecné důkazy jsou v other-trees-sequential.md,
other-trees-equivalence.md a other-trees-polynomial-proofs.md.

