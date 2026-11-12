# Dodatky k rejstříku: přímá revize kořenovým agentem

2. listopadu 2026. Tento soubor doplňuje zmrazené podklady
`parallel/index-errata-content/`; nepřepisuje jejich původní závěry.

## V1-C0085: Lévyho odkaz 363

**Confirmed pro veřejné erratum svazku 1.** Na straně 19
`all1-pre.pdf` je nové heslo Lévy, Paul Pierre s cílem 363.
Původní rejstřík na 639 přitom správně odkazuje na 105,
kde je v úloze 1.2.10-13 výslovně uvedena Lévyho věta
o spojitosti charakteristických funkcí.

Root přímo přečetl oba řádky a obě cílové strany. Celá
strana 363 svazku 1 obsahuje obecnou terminologii grafů
a stromů a začátek Theorem A; nemá Lévyho cíl. Přímo
přečtený dodatek `all1-prepre`, PDF24, pouze upravuje
terminologii walk/path/cycle. Hledání ve všech čtyřech
vrstvách podle jména i strany neodhalilo vložení Lévyho
textu na 363 ani následnou opravu vadného odkazu.

Konkrétní srovnání: `all2-pre.pdf`, PDF19, obsahuje
totožné nové jméno s cílem 363. Root přímo přečetl
tento řádek a skutečnou tištěnou 363 svazku 2
(DjVu375). Tam je Lévyho zpřesnění Gaussova–Kuzminova
odhadu i bibliografická citace jeho práce z roku 1929.
Shoda podporuje záměnu svazku při úpravě indexu;
konkrétní mechanismus vzniku je pouze inference.

Nejmenší oprava ve svazku 1 je **363 → 105**. Nové
prostřední jméno se zachová. Chybu nepřipisujeme
původnímu rejstříku ani neviděnému pozdějšímu dotisku.

## V1-C0086: Čebyševovy odkazy 377,388

**Confirmed pro veřejná errata svazku 1.** Přímo přečtené
`all1.pdf`, PDF16, a `err1.pdf`, PDF14, mají u rozšířeného
Čebyševova jména cíle 377,388. Totéž má zdrojový TeX
`err1.textxt`; čísla tedy nejsou chybou OCR. Jde o jednu
chybu zopakovanou ve dvou seznamech.

Root přímo přečetl celé původní strany 377 a 388 svazku 1.
První je soupis úloh o orientovaných stromech, druhá
pokračování centroidové enumerace a začátek enumerace
uspořádaných stromů. Žádná neposkytuje věcný Čebyševův
cíl. Přímo zkontrolované změny k 377 (`all1-prepre`, PDF26)
opravují P table a oriented walks; změna k 388 (`all1`,
PDF10) doplňuje podmínku maxima větve. Čebyševův obsah
nepřidávají.

Správné cíle jsou doloženy přímo: původní heslo na 631
uvádí 98,104 a na obou stranách je pravděpodobnostní
nerovnost výslovně pojmenována. `all1-pre`, PDF19,
rozšiřuje podheslo inequalities na 98,104,472. Na PDF14
téže vrstvy je přímo přečtené nové zakončení odpovědi
1.2.3-31 na 472 s monotónní Čebyševovou nerovností.

V `all4b.pdf`, PDF24, je totožný nový jmenný řádek
s dvojicí 377,388. Root přímo porovnal i oba cíle ve
svazku 4B: odpověď MPR-48 na 377 zmiňuje Čebyševovu
nerovnost a práci z roku 1874; poznámka k MPR-113 na
388 jeho funkci psi(n)=ln lcm(1,...,n). Jejich obsah
potvrzuje původ čísel v jiném svazku; matematika těchto
odpovědí ani Čebyševovy originály se zde znovu neauditují.

Oprava: odstranit nesouvisející **377,388** a zachovat
správné cíle **98,104,472** i nové pravopisné varianty.
Bez úplné pozdější sazby netvrdíme, že nová hlavní položka
nutně smazala staré podheslo inequalities nebo že vadný
řádek skutečně vyšel tiskem.

## Rozsah potvrzení

Oba nálezy se týkají doloženého obsahu veřejných seznamů
oprav, nikoli jejich redakční historie, prvenství nálezu
nebo autorova přijetí. Místní ASCII návrhy zpráv nejsou
odeslány. Neproběhly nové numerické testy; rozhodující
je přímé porovnání sazby, cílových stran a čtyř vrstev
errat. Přesné soubory a jejich hashe jsou v přejímacím
manifestu.

## Převzetí celého inventáře dodatků, X0695

Agentův manifest `MANIFEST.json` má SHA-256
`1c9fa2e4223c25f2ac716ce6827e259de1e32d4667179de23fb4ecdf67d3a5e9`.
Root ověřil všech 54 obsahových souborů (3 488 486 bajtů)
a všech 60 přesných vnějších vstupů. Přijímá individuální
ruční rozpis 435 výskytů: 388 v dlouhých vrstvách a 47
obrazově porovnaných krátkých duplikátů. Čísla 609,187,190,163
v původních agregovaných ID jsou pořadí záznamů, nikoli počty
indexových hesel.

Agentův zmrazený stav je 426 checked, šest partial a tři
candidate; poslední tři výskyty odpovídají výše potvrzeným
dvěma chybám. Kořenový stav je tedy **426 checked, šest partial,
tři confirmed výskyty**, při **dvou samostatných nálezech**.
Bez krátkých duplikátů: 380 checked, šest partial, dva confirmed.
Šest mezer je přesně vyjmenováno v agentově REPORT.md:
pět odkazů na chybějící původní úvodní strany a Swiftův
novější cíl 630. Žádná se nepovažuje za chybu knihy.

Root navíc přímo přečetl novější vydavatelský obraz 9
s Turing machines a xi se jmény Fuller/Gordon. Tyto cíle
se přijímají pro dostupnou novější sazbu. Historické chybějící
strany prvního tisku tím nejsou nahrazeny. Chronologické řady
hesel ani jejich poslední uvedené znění nepředstavují úplný
současný index. Stav celého rejstříku X0596 zůstává partial.
