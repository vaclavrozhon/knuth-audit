# Souvislý průchod: úvod druhého svazku

6. listopadu 2026; V2-X0081 až V2-X0083. Přímo přečteny všechny
dostupné úvodní obrazy souboru 1–12 a úvodní odpovědi na tištěné 538.
Obrazy `images/vol2-fileNNN-frontmatter.png` jsou nové reprodukce našeho
DjVu. Nejde o ověření fyzického výtisku.

## Vydání a mapa

Titul a tiráž potvrzují třetí vydání, první tisk ze září 1997,
ISBN 0-201-89684-2. Kontrolní číslice ISBN svazků 1 a 2 vycházejí.
Copyright 1998 vedle tisku 1997 není sám o sobě rozpor. Oficiální
[Knuthův seznam](https://www-cs-faculty.stanford.edu/~knuth/taocp.html)
potvrzuje rok 1997 a rozsah xiv+762.

| Soubor | Tištěná strana / obsah |
|---|---|
| 1–3 | autorská strana, titul, tiráž; ii–iv odvozeno z návaznosti |
| 4–6 | v–vii, předmluvy |
| 7–9 | ix–xi, instrukce a čtyři cvičení |
| 10–11 | xii–xiii, obsah |
| 12 | xiv, kresba číslic 1–9; není prázdná |
| 13 a dál | arabská strana = soubor − 12 |

Římské i a viii v kopii nemají samostatný obraz. Jejich obsah
neprohlašuji za zkontrolovaný. Souhrnná jednotka frontmatter proto
zůstává částečná, i když všech 12 dostupných obrazů má stránkový záznam.
Opraveno dřívější nepřesné označení souboru 12 za prázdnou stránku:
OCR jej vynechává, protože jde o ilustraci.

Všech pět oficiálních souborů errat bylo nově staženo a bajtově
porovnáno s kopií z 1. listopadu: beze změn. Hashe, URL a časy jsou
v `sources/sequential-2026-11-06/errata-manifest.json`.
Pro tento blok zkontrolovány všechny položky úvodu a strany 538
ve čtyřech řadách all2-prepre, all2-pre, all2 a err2; aktuální TeX
zůstává dostupný jako pátý podklad. Extrakce je uložena zvlášť.

## Předmluva, instrukce a obsah

Rozdělení témat mezi kapitoly 3 a 4 odpovídá obsahu. Poznámky o
výuce, estetice algoritmů a předpokládané délce řešení jsou doporučení
a autorská zkušenost. Plán čtvrtého vydání „snad za 16 let“ je
výslovně odhad z roku 1997, nikoli současný slib či matematické tvrzení.
Tabulka obtížností, M/HM a doporučující šipka jsou vnitřně konzistentní.
Zbytek hodnocení modulo 5 vyjadřuje pracnost, nikoli přesný časový zákon.
Research rating 50 nevydává tvrzení úlohy za dokázanou větu.

Odkazy obsahu byly porovnány s nadpisy příslušných stran přímo přes
`djvutxt --page`, nikoli podle pořadí bloků společného OCR. Celé
extrahované kotvy jsou v `results/sequential-frontmatter-toc-anchors.json`.
Údaj 41 u §3.3.1 je chybný: oddíl začíná na 42. Obě původní strany
41–42 byly navíc vizuálně porovnány; V2-X0082 je známá oprava z
22. prosince 1997. Kontrola jejich nadpisu ještě neznamená audit celých
stran 41–42. Chybějící spojovník v názvu §4.3 je rovněž zveřejněná
drobná oprava, nikoli samostatný nový nález.

Přesun §4.5.4 z 379 na 380 v pozdějších erratech nelze slepě promítnout
do prvního tisku: jeho oddíl skutečně začíná na 379. Doplnění přílohy C
v roce 2011 mění poslední řádek obsahu i katalogový rozsah 762→764;
původních 762 nebylo v tomto exempláři chybné. Pozdější změny formulací,
hodnocení 45→40 a vysvětlení výzkumných obtížností byly rozlišeny od chyb.

## Čtyři úvodní úlohy

1. M20 znamená průměrnou matematicky zaměřenou úlohu. Odpověď 538
   souhlasí s definicí a nepožaduje vyšší matematiku.
2. Přínos cvičení je vysvětlen v úvodním odstavci. Nová krátká odpověď
   z 24. listopadu 2023 přidává možnost kontroly porozumění. Chybějící
   původní odpověď není chyba: kniha slibuje řešení většiny úloh.
3. Původní zadání výslovně dovoluje `0 ≤ w ≤ x ≤ y < z < 10^6`.
   Přesná celočíselná aritmetika ověřila Fryeovu čtveřici
   `(95800,217519,414560,422481)` i její dvojnásobek
   `(191600,435038,829120,844962)`. Třetí násobek již překračuje mez.
   Původní odpověď obsahuje pouze první: druhou doplňuje all2-pre
   24. ledna 2014. Jde o V2-X0083, známou neúplnou odpověď, nikoli
   nový objev. Na str. xi téhož dne přibývá M v hodnocení.
   Případ w=0 nepřináší řešení: pro x>0 jde o Fermatův případ exponentu
   4; pro x=0 odporuje y=z ostré podmínce y<z.
4. Vydání jasně označuje tvrzení pro n>4 jako výzkumnou úlohu M50;
   odpověď paroduje Fermatovu poznámku o okraji. Nový důkaz zde není.
   [Croot–Yip, JLMS 2026, Conjecture 2.8](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.70499)
   stále formuluje obecnou Landerovu–Parkinovu–Selfridgeovu domněnku.
   Po dosazení počtu členů 3 a 1 její závěr vyžaduje n≤4; každý člen
   vlevo je v kladném řešení menší než pravá báze, takže se nic nekrátí.
   To ověřuje vztah zadání k citovanému otevřenému problému, nikoli jeho
   pravdivost. Rychlá aktuální rešerše neodhalila řešení tohoto zadání.

Elkiesův původní článek Math. Comp. 51 (1988), 825–835 byl získán
z veřejné kopie; AMS vrátilo 403. Vizuálně přečteny 825 a postscript
834–835, navíc text úvodu 826. Ověřeno autorství, bibliografie,
rok přijetí 1987, tvrzení o nekonečné rodině a zpráva o jediném
primitivním řešení pod milionem po odstranění společného dělitele.
Kompletnost Fryeova výčtu je převzata s tímto přesným rozsahem;
nezávislý úplný výčet znovu neběžel podle povolení vynechat drahý
brute force. Ani celý důkaz s eliptickými křivkami nebyl nově přezkoušen.
Přímé dosazení ověřuje i Elkiesovu úvodní čtveřici. Počítačový čas
110 hodin v knize a přibližně 100 v článku nepovažuji za prokázaný rozpor.

## Výslovné pramenné výjimky

Nedohledávám nyní přesné původní vydání Hamletova verše, Campbellův
citát, Coltonovo datum, Bellmanovu pověst ani Recordeův citát. U vydání,
ochranných známek a poděkování nejde o nový právní či biografický audit.
Historii prvního nasazení TeXu a METAFONTu zde beru jako autorovo
svědectví, nikoli nezávisle reprodukovanou událost. Elkies píše 1769,
TAOCP 1772 u Eulerovy domněnky; bez přezkoumání Eulerova originálu
a rozlišení formulace/publikace tento bibliografický rozdíl nechávám
výslovně neuzavřený, bez nového chybového nálezu.

Strana 538 má zatím jen částečný stránkový záznam: odpovědi úvodu
jsou hotové, ale její zbytek patří do souvislé kontroly §3.1.
Nový matematický nález v tomto bloku nevznikl.
