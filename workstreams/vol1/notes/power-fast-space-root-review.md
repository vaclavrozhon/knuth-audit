# §1.3.1–22: prostor mezi nejrychlejšími programy

Kořenová revize 2. listopadu 2026, V1-X0702. Přijatý výsledek je
**13 dodatečných slov v nejhorším radixu mezi přenositelnými programy
s nejhorším časem 4u před HLT**. Jednotka u je knižní jednotka času;
HLT přidává 1u. Vstupní buňka 2000 se do dodatečného prostoru nepočítá,
všechny použité instrukce, konstanty a pomocná místa ano. Radix b je
počet hodnot jednoho bajtu, 64 <= b <= 100. Počáteční nepředepsané
registry, příznaky a paměť mohou mít libovolný obsah.

Nejde o globální prostorové minimum při libovolně dlouhém výpočtu.
Knižní sedmislovný program proto nadále nemá uzavřený důkaz svého
prostorového minima. Původní tabulka na s. 509 skutečně používá
14 míst; její počet ani čas nejsou novou konstrukcí vyvráceny.
Nevzniká nový nález chyby.

## Konstrukce a přijatá kontrola

Tři instrukce jsou `LD1 2000; LDA 2000,1; HLT 0`. Na adresách
2000+k jsou připraveny hodnoty k^13 pro všechny přípustné nenulové
vstupy k. Nulovou položkou je původní vstup, který se nepřepisuje.
Pro b = 64, 65 je |k| <= 4, jinak |k| <= 5. Tím vzniká 11,
respektive 13 dodatečných slov. Výpočet zachová i znaménko nuly.

Root přečetl celý důkaz, celý nový checker a výsledná metadata.
Uložených 440 kontrol zahrnuje všech 37 radixů, každý přípustný
vstup včetně obou nul a nepřednastavené ostatní registry/příznaky.
Všechny mají čas 5u včetně HLT, přesný znaménkový výsledek a nemění
paměť. Úspěšný checker nebyl spuštěn znovu. Obecná správnost plyne
přímo z adresování, nikoli jen z těchto konečných kontrol.

## Revize dolní meze a výslovné doplnění výběru pole

Zmrazená poznámka `parallel/mix-optimality/notes/power-fast-space.md`
provede úplnou redukci rozpočtu 4u při b = 100. Vstup +3 vyžaduje
výsledek 1594323, který nevytvoří jedno čtení a dvě jednotkové
adresové operace. Zvlášť jsou vyřízeny vstup jako instrukce,
samomodifikace, MOVE, floating operace a nepředepsaná zařízení.
Zbývají dvě operace za 2u. Afinní aritmetika ani jediný posun
nepostačují. Jediná správná dvojice pro libovolné počáteční registry
je načtení vstupu do indexu a načtení výsledku z jím indexované
tabulky. Jde o dvě čtení bez skoku a zápisu, tedy o stejný průběh
pro všechny vstupy. Root tento rozbor přijal.

Pro závěrečné vyloučení překryvu kódu s tabulkou doplňujeme výslovně
krok o poli druhého LOAD. Výběr pole označený (L:R) určuje přenesené
pozice slova; pozice 0 je znaménko a pozice 1 až 5 jsou bajty.
Při b = 100 je 5^13 = 1220703125 > 100^4. Druhý LOAD tedy musí
přenášet všech pět bajtů velikosti. Stejný opcode musí vrátit oba
výsledné znaky pro vstupy +5 a −5, takže musí přenášet také znaménko.
Jeho pole je nutně (0:5). První indexový LOAD musí rozlišit poslední
bajt a znaménko vstupu, a proto má rovněž pole (0:5).

Tabulkové slovo je tudíž skutečně příslušná mocnina nebo její zápor,
ne pouze slovo s vhodným podřetězcem. Jeho operační bajt je jeden
z 0, 1, 92, 23, 64, 25. Žádný se nerovná kódu použitého indexového
LOAD, LOAD do A ani HLT. Jedenáct různých tabulkových adres se
proto nekryje se třemi vykonanými instrukcemi. Nejvýše jedna
tabulková adresa je daným vstupem; nejméně deset dalších musí být
připraveno. Dolní mez je 3 + 10 = 13. Radix 100 postačuje pro
minimum maxima přes všechny radixy; není tím prokázáno samostatné
minimum 13 pro každý radix 66 až 99.

X0684 již dokázal časové minimum 4u pro číselný výsledek. Nová
konstrukce dosahuje téže meze se zachováním znaménka nuly; stará
dolní mez platí i pro tento silnější požadavek.

## Prameny a evidence

Root přímo zobrazil původní s. 143, 509, 138 a 139. Sémantika
znaménka, volitelnost I/O a floating operace byly již přímo čteny
v předchozích přijatých blocích. Čtyři vrstvy errat, včetně
opravy krajních tabulkových hodnot z 17. listopadu 2007, jsou
zachyceny v přijatém výtahu. Nová konstrukce nevyžaduje uložení
nepřípustných mocnin na menším radixu.

Před revizí souhlasily délky a SHA-256 všech tří nových souborů
a osmi zdrojů ze zmrazeného `power-fast-space-manifest.json`.
Kořenový manifest `results/power-fast-space-root-manifest.json`
zachycuje toto převzetí a výše uvedené doplnění bez změny původního
agentova důkazu. Celá úloha 22 i souhrnná X0153 zůstávají partial.
