# Přechod k samostatnému ověřování tvrzení a úloh

6. 11. 2026 uživatel zvolil důkladnější rozsah. Níže uvedené čtení
zůstává platným prvním průchodem, ale nezaručuje samostatný argument
pro každé tvrzení. UI first-pass coverage se zpětně nepovyšuje.

| Přečtený blok | Text | Úlohy | Odpovědi | Neuzavřený důkladný rozsah |
|---|---|---|---|---|
| Předmluvy a úvod | souborové 1–11 | — | — | Historické/statistické a bibliografické výroky přeskočeny; vydání/offset již doloženy. File8 useknut. |
| Kapitola 5, úvod | 1–10 | §5-1 až25 | 584–591 | Individuální důkazy všech tvrzení/úloh nejsou kompletní; první nový důkladný kurzor 1/file12. |
| Inversions | 11–22 | §5.1.1-1 až29 | 591–597 | Přebrat uvedené bijekce/momenty, doplnit jednotlivé důkazy, algoritmy a vzorce. |
| Multisety | 22–35 | §5.1.2-1 až24 | 597–602 | Samostatná evidence všech tvrzení dosud chybí; C0003 již doložen. |
| Runs | 35–47 | §5.1.3-1 až27 | 602–607 | Samostatná evidence všech tvrzení dosud chybí; C0004 již doložen. |
| Tableaux | 48–72 | §5.1.4-1 až44 | 607–615 | Samostatná evidence všech tvrzení dosud chybí; C0005/6/8 doloženy, C0007 otevřen. |
| Internal sorting | 73–80 | §5.2-1 až13 | 615–619 | Instrukční a obecné důkazy doplnit; C0009 již doložen. |
| Insertion sort | 80–105 | §5.2.1-1 až44 | 619–628 | Individuální důkazy a analýzy doplnit; existující dvě malé stopy a C0010 neopakovat. |
| Exchanging sort | 106–138 | §5.2.2-1 až56 | 628–639 | Individuální důkazy/analýzy doplnit; C0011–15 doloženy. Výzkumná úloha9 a externí důkaz42 zůstávají otevřené. |
| Začátek selection | konec138 | — | 639: odpovědi1–4 přečteny | Zadání dosud nespárována; nejde o důkladně ověřený blok. |

Všechny arabské stránky mají file=printed+11. Hranice sekcí na sdílených
stránkách se překrývají. Zbytek knihy za čtenářským kurzorem 139/file150
dosud nemá souvislé čtení; konec791 byl pouze stránkovací doklad.

Přebírané konkrétní uzavřené důkazy: notes/V3-C0002 až C0006, C0008
až C0015; C0001 a C0007 jen v dosavadním kandidátském rozsahu.
Přebírané výpočty: results/intro-targeted-checks.json (identita §5-18,
konstrukce klik a modul), results/insertion-targeted-checks.json
(dva vytištěné Shellsort příklady). Žádný z nich se znovu nespouští.
Starší stručné argumenty v blokových poznámkách se rozvedou či odkážou
jen v potřebném rozsahu; tabulka neříká, že vůbec žádný argument neexistuje.

Postup: úvodní matematické definice/tvrzení, potom §5-1 až25 včetně
všech částí odpovědí; následně §5.1.1 atd. Každá položka má samostatný
záznam a důkaz/odkaz v proof-audit.json. Náročné nebo otevřené části
zůstávají partial; bibliografické výjimky jsou od matematických mezer
oddělené. Plošné brute force ani opakování uzavřených kontrol se nedělá.
