# První průchod: souborové 41–81 / tištěné 24–64

6. listopadu 2026. Celý souvislý rozsah přečten v režimu rychlého prvního
průchodu. Součástí jsou všechna **zadání §7–1 až 145**, nikoli všechna jejich
řešení. Původní sazba zobrazených vzorců, algoritmů a obrázků byla přečtena.
Žádný nový program, census ani ověřovač se nespouštěl. Použity jen krátké
algebraické argumenty při čtení. **Confirmed 0; candidate 1** (hraniční n=1
v úloze 7–20, viz samostatný záznam V4A-C0001).

## Konkrétní matematický obsah

- **24–25:** příklady SGB. Přímé vztahy počtů u podmnožin a simplexů sedí:
  C(11,5)=462, stupně 6/30, hrany 1386/6930; C(13,3)=286 a 6·C(12,3)=1320.
  Počty obrázkových/pseudonáhodných grafů, rozklady a girth/diameter nebyly
  generovány. Známou opravu parametrů `plane_lisa` zohledňuji.
- **26–28:** komplement, line graph, disjunktní sjednocení, join a všech pět
  grafových součinů. Blokové matice (40)–(46), souvislost s úplnými
  multipartitními grafy a podmínky na a,b v k-násobných součinech jsou
  při čtení konzistentní. Torové obrázky a vzorec k-krychle prohlédnuty.
- **29–31:** konjugované posloupnosti a tabulky 55544322→43333 odpovídají
  odebíraným hranám. Algoritmus H přečten z originálu. Lemma M využívá
  přenos jednotky z většího stupně do menšího; protože di≥dj+2, lze vybrat
  souseda v odlišného od j, aby přesun hrany nevytvořil smyčku. Corollary H
  redukuje problém na menší graf pomocí majorizace. Neprováděna systematická
  enumerace stupňových posloupností.
- **31–35:** sítě, hypergrafy, incidence, dualita, pokrytí/nezávislost,
  chromatičnost, kliky a exact cover. Sedm množin (56) odpovídá skalárnímu
  součinu mod2; 28 trojúhelníků ve Fano rovině plyne z C(7,3)−7=28.
  Matici a incidence v (57) prohlédnuty. Dualita cover↔independent set je
  přímá komplementací podmnožiny vrcholů. Mapové optima 38/11 a 30/19
  nepřepočítána. Známá vynechaná podmínka V∩E=∅ a změny RISC/SGB vzaty v úvahu.
- **36–46:** přečtena všechna zadání 145 úloh, včetně obrázků a předpokladů.
  Krátké sanity argumenty: 13 vrcholů stupně5 odporuje sudému součtu stupňů
  (42); turnaj má cestu vložením dalšího vrcholu (59), vrchol maximálního
  výstupního stupně má do ostatních vzdálenost≤2 (60); Mooreovy meze (63)
  odpovídají stromovým okolím; odstranitelnost sloupce (143) plyne z nejvýše
  m−1 rozdělení tříd shodných řádků; konfliktový graf v144 zachytí slučitelnost
  řádků; vyrušování nestejných párů v145 zachovává přísnou většinu.
  Těžké konstrukce, programovací úlohy, počty a otevřené problémy zůstávají
  pouze přečtenými zadáními, ne nově vyřešenými úlohami. Známé opravy 5,80,88,
  107,114,137,140,142 zohledněny. Kandidát7–20 je samostatně označen.
- **47–54:** všech 16 binárních operací, základní identity, De Morgan,
  multilineární forma a DNF/CNF. V původní sazbě zkontrolovány pruhy
  negací, které OCR často ztrácí. Osm bodů (28) přesně odpovídá tabulce (22);
  její maximální podkrychle jsou 000*,0*00,*100,*111,11**. Horní/dolní
  rozklad podle poslední proměnné dává správně (16)–(21).
- **55–60:** Theorem Q, SAT/3SAT, Hornovy funkce, Theorem H, gramatika a
  Algorithm C. Monotónní funkce má kladné prime implicants; nastavení
  proměnných jednoho implicantu na1 a ostatních na0 ukazuje jeho nutnost.
  Sedm 3CNF-klauzulí po třech různých proměnných vyloučí nejvýše 7/8 vstupů.
  Osmiklauzulový příklad (32) přečten včetně známého přeuspořádání.
  Hornova uzavřenost na průnik dává nejmenší model. Gramatika má 275
  výroků a24·11 + 3·11² + 13 = 640 klauzulí. Algorithm C z prvního dotisku je
  standardní dopředné odvozování: každý výrok je na zásobník vložen jednou,
  každý záznam hypotézy jednou sníží COUNT, tedy O(N+n). Pozdější známá
  změna datové struktury není nález; její implementace se nově neauditovala.
- **60–64:** komediantský 2SAT příklad, kontrapoziční graf a Theorem K,
  mediány a úplný důkaz Theorem P. Cyklus (42) obsahuje u i jeho negaci;
  po vynechání v hodnoty tuwxyz=110000 dávají bezkolizní rozpis šesti
  komiků. Důkaz K správně páruje zdrojovou silnou komponentu s komplementární
  koncovou komponentou. V důkazu P se kladné prime implicants vzájemně
  protínají; posloupnost mediánových výrazů postupně zahrne všechny a
  self-dualita promění dominanci v rovnost. Opakovaný rozpis deseti
  trojliterálových implicantů má podle T_j = 2T_{j-1} + 2 celkem 2046 operací.
  Na s.64 v(49) je původní první znak **v**, nikoli y podle OCR.

## Cílené odpovědi a zrušené podezření

Při čtení úlohy 7–6(c) jsem zaznamenal, že třetí znaménková symetrie pro n=2
mění znaménko. **Nejde o nález:** odpověď 7–6(c) na s.515 výslovně uvádí,
že rovnost platí jen pro n mod4=0 nebo3. Tentýž originál umožnil krátce
uzavřít dolní mez šířky v 7–7: při šířce≤6 je součet rozpracovaných párů
nejvýše 11n−30, zatímco Langfordovo párování dává n(n+3)/2. Pro n=16 by bylo
152≤146, spor. Tím se doplňuje dřívější kontrola konkrétní šířky7 v(2).
Souborová 532 má pouze `partial` pokrytí pro odpovědi 6–7, ostatní obsah
odpovědí nebyl systematicky zpracován.

Při čtení 7–20 vznikl V4A-C0001: n=1. Originály zadání i odpovědi zobrazeny;
žádná odpovídající oprava v pěti relevantních vrstvách errat nenalezena.
Souborová 54 je v pokrytí `partial` kvůli otevřené hraniční konvenci, a 535
je `partial` pro cílenou kontrolu odpovědi 20. Navigační prohlédnutí dalších
odpovědí se nevydává za plošnou kontrolu jejich stránek.

## Známé opravy a přeskočení

Relevantní vrstvy `all4a-pre`, `all4a`, `err4a`, `all4f0`, `err4f0` zůstávají
stejné; prohledány při kandidátu i podle obsahu a odpovědi, ne jen podle
strany. V tomto bloku se zohledňují s.24,25,26,29,31,32,33,34,35,36,42,43,
44,45,46,48,49,52,54,56,59,60,62 a příslušné historické varianty F0.
Žádná známá oprava není vlastní karta nebo červená stránka.

Bibliografie a historické atribuce jsou výslovně přeskočeny po stránkách
v `ui-page-coverage.json`; žádné nové externí prameny se nestahovaly.
Nezávisle nejsou reprodukovány datové sady SGB, velké grafové enumerace,
počty nejkratších formulí a řešení, implementace/benchmarky ani historické
rekonstrukce. Převážná většina odpovědí k 145 úlohám ještě čeká na svůj průchod.

Další kurzor: **file82 / tištěná65**, median algebras and median graphs.
