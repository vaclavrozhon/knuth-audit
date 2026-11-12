# Předmluva a úvodní listy: fakta, odkazy a explicitní výjimky

6. listopadu 2026; file 1–6. Výchozí bibliografická identita a stránkování
se přebírají z již doloženého `notes/edition-and-pagination.md` a
`inventory/books.json`, nikoli jen ze starého záznamu „přečteno“.

## P-P01. Obálka, titul, tiráž, file 1–3

Inventář identifikuje ISBN 978-0-13-532824-8 a první digitální release
březen 2025; primární tiráž `sources/file-003.txt` a uložený obraz
`inventory/images/vol4-fasc7-constraint-satisfaction-digital1-2025-copyright.png`
jsou přímou oporou. Obálka a titul shodně označují fascikl 7 a téma
Constraint Satisfaction. Netvrdí se nejnovější digitální release ani
ověřený fyzický dotisk. Údaje autorství/vydavatele jsou bibliografická
metadata z tiráže; žádné nové matematické tvrzení zde není.

## P-P02. Umístění obsahu v TAOCP, file 4 / p. iii

Křížové odkazy byly porovnány s lokálními primárními texty svazků:
`text/vol4a.txt`, obsah kolem řádků 483–505, má §7.1 Zeros and Ones,
§7.2 Generating All Possibilities, §7.2.1 Generating Basic Combinatorial
Patterns; poslední podsekce 7.2.1.7 je na p. 486. `text/vol4b.txt`,
obsah kolem řádků 540–700, navazuje §7.2.2, obsahuje Dancing links
a Satisfiability. Vlastní file 16 nese záhlaví §7.2.2.3. Jde přesně
o návaznost popsanou v předmluvě, nikoli o důkaz metod těchto sekcí.
„Nakonec čtyři svazky“ a podíl budoucího 4C jsou plány autora, ne
matematické nebo již uskutečněné publikační údaje.

## P-P03. Rozsah úloh a konkrétní navigace, file 5 / p. iv

Záhlaví zadání na p. 113–157 mají souvislou posloupnost 1,…,486;
kontrola jen těchto nadpisů je uložena v `results/preface-exercise-count.json`.
To dokládá zaokrouhlené „přibližně 500“. Nedokládá to žádnou odpověď.
Zadání mají 45 stran, odpovědi p. 158–261 mají 104, celkem 149.
149 > 281/2 pro číslované tělo; dokonce 149 > 296/2, pokud se přičtou
všechny úvodní listy až po poslední stranu knihy a vynechají jen dvě
reklamy file 297–298. Tvrzení „více než polovina“ tedy souhlasí.

Na file 57 / p. 42 jsou skutečně odkazy na úlohy 221, 226, 224, 225,
228 v tomto pořadí. Strana se týká převodů barvení do SAT, jak říká
předmluva. Tato krátká kontrola navigace neověřuje matematiku p. 42
ani odpovědi těchto úloh; ty zůstávají ve vlastní frontě.

## P-P04. Programy a přehled témat, file 5–6 / p. iv–v

Aktuálně dostupná autorova [stránka programů](https://www-cs-faculty.stanford.edu/~knuth/programs.html)
obsahuje všech pět názvů SSXCC0, SSXCC, SSXCC-BINARY, SSMCC a XCCDC.
Primární HTML je `sources/programs-2026-11-06.html`, řádky 482–500;
URL, datum, velikost a hash v `sources/preface-primary-manifest.json`.
Tím je doloženo tvrzení o dostupném seznamu, nikoli správnost těchto
programů, všechny jejich verze nebo autorův autobiografický počet
sepsaných programů. Prototypy algoritmů se budou ověřovat v příslušných
matematických blocích, bude-li to potřebné.

Výčty témat (scene analysis, graceful graphs, embedding, look-ahead,
sparse sets, knight's tours, fillomino) jsou deklarace obsahu. Odpovídají
vlastnímu obsahu file 13–14 a heslům v indexu; jejich tvrzení o metodách
se kontrolují u příslušných kapitol, ne odvozením z úvodního slibu.
Srovnávací „často lepší“ odkazuje na benchmarky a není univerzální
dominance jedné metody. Tyto konkrétní nákladné benchmarky zde nebyly
reprodukovány; zůstávají oddělenou výpočetní výjimkou.

## P-P05. Číslování obrázků a notace, file 6 / p. v

`text/vol4b.txt` obsahuje na řádku 26874 popisek Fig. 99; v pořadí
popisků je to poslední číslovaný obrázek. Vlastní Fig. 100 na file 22 /
p. 7 je první zdejší číslovaný obrázek. To potvrzuje návaznost uvedenou
v předmluvě, nikoli věcný obsah obrázků.

Odkazy na §7.1.3 a §7.1.1 ve 4A odpovídají umístění ruler/population
count a median: v `text/vol4a.txt` je ruler v (44), sideways sum/
population count v blízkém výkladu, median odkazován na 7.1.1–(43).
Zdejší #123=(123)16 je definice šestnáctkového zápisu (hodnota 291),
ne další věta. „Notational conventions“ je skutečné heslo ve vlastním
indexu na p. 275, file 290; příslušná příloha B v obsahu 4A i 4B
existuje. Tyto navigační kontroly se nevydávají za nový audit 4A/4B.
Placeholder 00 a redakční plán budoucí přílohy jsou autorovy konvence.

## P-P06. Přesně vynechaná bibliografie a osobní výroky

Neověřeny v primárních historických pramenech: citát Marka Twaina
z Roughing It (1872), citát Roberta E. Tarjana v SIAM Review (1978),
osobní poděkování a okolnosti vzniku, historická odměnová nabídka a
autorovy autobiografické počty programů. Jsou výslovnou bibliografickou
výjimkou. Text odměn je pouze záznam nabídky v roce vydání; nic nebylo
odesláno a není slibována odměna. Dva benchmarkové archivy zde nebyly
staženy ani jejich dostupnost ověřena; jde o vynechané zdrojové odkazy.

Kontrola file 1–6 se týká výše jednotlivě vymezených faktů a definic,
ostatní neověřené historické/bibliografické údaje jsou zde vyjmenovány.
Žádný nový nález. Nově vypsané nadpisy úloh a hranice odpovědí nejsou
argumentové ověření ani čtenářské uzavření těch vzdálených stran.
