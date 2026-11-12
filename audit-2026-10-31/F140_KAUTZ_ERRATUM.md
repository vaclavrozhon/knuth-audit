# F140: chybné koncové číslo stránky v erratech 4B

**Potvrzený drobný bibliografický nález v publikovaných erratech.**
Nejde o novou matematickou chybu knihy. Kontrola 3. 11. 2026.

Naše PDF uvádí na str.465 u W. H. Kautze rozsah **177–180**.
[Knuthova errata](https://www-cs-faculty.stanford.edu/~knuth/err4b.textxt)
jej položkou z 13. 3. 2026 mění na **179–189**. Oprava začátku je
správná, ale koncové číslo má zůstat **180**.

Vydavatelem IEEE vložený záznam DOI
[10.1109/TEC.1958.5222529 v Crossref](https://api.crossref.org/works/10.1109/TEC.1958.5222529)
identifikuje článek *Unit-Distance Error-Checking Codes*, EC-7, číslo2,
1958, strany **179–180**. Surová odpověď API je uložena jako
[kautz-crossref.json](sources/snakes172/kautz-crossref.json), s časem,
URL a SHA256 v [metadatech stažení](sources/snakes172/kautz-retrieval.json).

Chybných179–189 jsem přečetl také přímo v obou renderovaných verzích:

- [krátká errata, str.12](images/snakes172-err4b-Kautz-pdf12.png),
- [souhrnná errata, str.14](images/snakes172-all4b-Kautz-pdf14.png).

Živě stažené TeX i PS err4b z 3.11.2026 jsou po bajtech shodné
s našimi archivními soubory. Nejde tedy jen o chybu OCR ani o
zastaralý opis. Šest vrstev errat neobsahuje následnou opravu konce180;
podrobnosti má [errata-check.json](results/snakes172/errata-check.json).

Opravená položka má být **177–180 → 179–180**.
Úplný původní dvoustránkový článek se nepodařilo získat; závěr o
paginaci stojí na primárních metadatech vydavatele, nikoli na
předstírání přečteného skenu. Obsah článku a prvenství termínu se
tímto nálezem neověřují. Prvenství našeho upozornění není doloženo.
Žádná zpráva autorovi nebyla vytvořena ani odeslána.
