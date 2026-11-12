# Předání: §2.3.4 a §2.3.4.1 Free Trees

Stav 1. 11. 2026: matematický audit je dokončen, zdrojový audit zůstává
částečný pouze v přesně vymezených bodech úlohy 8. Celý tento adresář je po
předání zmrazen. Sdílený ledger, scope, kořenové stavové soubory ani nástroje
nebyly měněny; commit nebyl vytvořen.

## Rozsah a výsledek

Původní obrazy hlavního textu s. 362 od nadpisu §2.3.4 až do s. 371 a všech
13 odpovědí na s. 578–580 byly přečteny. Obecné důkazy pokrývají Theorem A,
fundamentální cykly a rozměr prostoru toků, obě části Theorem K, všechny
tokové identity příkladů, redukci vrcholových toků, minimální kostry a
generování permutací hranovými transpozicemi. Přesné důkazy a stavy všech
úloh jsou v [general-proofs.md](notes/general-proofs.md).

Jediný nový nález je první implementace v odpovědi §2.3.4.1-12 na s. 580:
již vybraný vrchol může být znovu aktivován aktualizací a(j). Obecná rodina
protipříkladů a nejmenší konkrétní příklad se čtyřmi vrcholy jsou v
[prim-answer12.md](notes/prim-answer12.md). Kořen nález nezávisle revidoval
a přidělil mu **V1-C0041, confirmed**. Podklad se od této revize neměnil.
Druhá implementace se seznamem nevybraných vrcholů je správná; algoritmus
úlohy 11 i Primův originál jsou správné. Potvrzení neznamená prvenství ani
fyzickou kontrolu tištěného výtisku.

## Errata a primární literatura

Všechny čtyři vrstvy errat byly prohledány podle stran a předmětu; příslušné
obrazy PDF byly prohlédnuty. Přehled [errata.md](notes/errata.md) má 20 řádků
známých oprav, některé s více zásahy do terminologie. Žádná vrstva neopravuje
nový problém odpovědi 12. Aktuálnost stažených errat 1. 11. 2026 ověřil kořen.

[sources.md](notes/sources.md) zaznamenává přesný rozsah každého čtení.
Jarníkův a Primův článek, Dijkstrův článek a relevantní části Ball–Larus,
Kirchhoff a Stanford GraphBase podporují příslušné odkazy knihy. Celé dlouhé
citované publikace se automaticky neprohlašují za auditované.

Úloha 8 má dokončené vlastní důkazy včetně surjektivity redukce, rozměrového
počtu měření a izomorfismu odchozí/příchozí konstrukce. Zdrojové mezery jsou:

* Nahapetian (1973), s. 37–41: dostupný byl pouze vydavatelský abstrakt
  a metadata; původních pět stran se získat nepodařilo.
* Knuth–Stevenson (1973), s. 313–322: přečteno vlastní tělo autorského
  přetisku 2000 v dostupném textovém náhledu; chybí původní článek a obrazy
  sazby přetisku. Nečitelná programová příloha se neprohlašuje za ověřenou.

Konkrétní neúspěšné přístupy i úspěšně stažené zdroje mají záznam v
`sources/downloads.json`. Nejde o mezeru v obecném matematickém důkazu.

## Výpočetní doklady

[check_figures.py](check_figures.py) a [figures.json](results/figures.json)
nezávisle porovnávají koncové vrcholy hran a prohledané kostry s přepsanými
cykly a rovnicemi: všech 20 rovnic (6), všech 15 toků boxy, všech pět cyklů
a rovnic úlohy 7 a každou řezovou volbu obrázku 33. Délka uvedené kostry je
přesně `7+2*sqrt(2)+2*sqrt(5)`; globální minimum dokazuje výměnný argument.

[check_prim_answer.py](check_prim_answer.py) a
[prim-answer12.json](results/prim-answer12.json) doplňují obecný protipříklad:
760 úplných grafů na nejvýše čtyřech vrcholech s cenami 1, 2, 3; opravená
varianta souhlasí s nezávislým Kruskalovým výpočtem ve všech případech.
Knižní první varianta selže v 445 ze 729 čtyřvrcholových případů. Úspěšné
kontroly nebyly bez důvodu opakovány.

Strojový seznam jednotek je [UNIT_STATUS.json](UNIT_STATUS.json). Úloha 8
je celkově `partial` kvůli zdrojům, úloha 12 `confirmed`, ostatní přidělené
jednotky `checked`. Vnitřní odkazy mimo rozsah jsou výslovně vymezeny
v poznámkách; zvláště implementace 2.3.3E patří kořeni. Následující přidělený
blok je §2.3.4.2 Oriented Trees v samostatném adresáři.
