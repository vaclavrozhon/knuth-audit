# První průchod — file 41–80 / tištěné p.33–72

Celý blok souvisle přečten. Pokrývá dokončení Programu P, úplné shrnutí MMIXAL a I/O, zbývající zadání §1.3.2′, §1.3.3′, celou §1.4.1′ včetně zadání úloh a §1.4.2′ po úlohu4. Odpovědi jsou až od p.94 a nebyly tímto blokem auditovány.

Krátce sledovány indexy a ukončení Programu P, jeho buffer a místní symboly; nebyly znovu reprodukovány statistiky p.37 (9538 dělení; 10036μ+641543υ a 2804μ+124559υ). Pravidla symbolů, GREG, zarovnání a I/O přečtena včetně zohledněných historických errat. U příkladů s Fareyovými zlomky, magickým čtvercem, Josephem, zaokrouhlením a Velikonocemi proběhlo čtení zadání a základní kontrola návaznosti, nikoli řešení všech úloh či běh programů. Obrázky14–19 prohlédnuty v sazbě tam, kde je extrakce neúplná; čísla arabské tabulky přečtena vizuálně, jazyková správnost titulku není nezávisle ověřena.

U podprogramů zkontrolovány algebraické vzorce úspory kódu a běžné případy posunu registrů PUSH/POP v popsaných příkladech; nikoli úplný soupis všech kombinací rG/rL. U korutin sledován formát výstupního bufferu a přechody In/Out. To odhalilo **MMIX-C0004**, ztrátu dat za dovoleným nulovým bytem; krátký důkaz používá přímo knižní kontrakt Fgets a nezávisí na simulátoru. Přibyl také nízký překlep **MMIX-C0005**. C0003 rY/NEG zůstává candidate.

Zveřejněná doplnění p.48 (omezení vzorce zaokrouhlení) a p.66 (n≥0 u Fibonacciho úlohy) jsou zohledněna v errata-033-072.json; nejsou naše nálezy.

Bibliografie ponechána s explicitními výjimkami: Conway1958; Wirth PL/360/JACM1968; Literate Programming1992; Ibn al-Haytham a Ball/Coxeter1939; Ahrens1918; Lilius/Clavius a CACM1962 p.556; Dijkstra1972/Wirth1971; Turing1945. Přesné anglické položky jsou v coverage podle stránek. Žádný brute force ani nové testovací běhy.

Celkem souvisle přečteno file1–80; dřívější cílené výřezy file91,96,130 zůstávají partial. Další kurzor **file81 / p.73**, dokončení korutin a začátek interpretativních rutin.
