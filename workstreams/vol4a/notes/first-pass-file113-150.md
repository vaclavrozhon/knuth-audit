# První průchod: file 113–150 / tištěné 96–133

6. listopadu 2026. Souvisle přečten celý rozsah v OCR a původní sazbě:
závěrečná zadání §7.1.1–132/133 na str.96, text §7.1.2, všechna jeho zadání
1–88 a úvod §7.1.3 na str.133. Přečtení zadání není vyřešení úloh; odpovědi
čekají až na průchod answer section. Nový nízkoprioritní **V4A-C0002** pouze
pro zbylý výskyt na str.120; žádné nové confirmed. Neběžel žádný matematický
program, census, optimalizace ani herní solver.

## Konkrétní kontroly

- Str. 96–100: mux v (2) v obou tvarech, C/L/D, řetězce v obrázku9,
  normalizace a Algorithm L přečteny. V (6) dosazením x1=1 dostáváme x2,
  při x1=0 první dvě čtveřice 1100/1001, tedy správný původní truth table.
  Řetězec (7) spojuje „nejsou všechny bity stejné“ se sudou paritou, což
  pro čtyři vstupy dává přesně dvě jedničky. Minimálnost C/L/D ani celou
  knihovnu obvodů v obrázcích9/10 jsme znovu neprokazovali.
- Str. 101–106: footprint, minimum memory, zpětné substituce, special chains
  a tabulky1/2. V (15) maska00110011 vybírá dvojice a2,a3,a6,a7, které si
  mají vyměnit místa; v (16) maska01010000 kopíruje a0 do a1 a a2 do a3.
  Rozdělení na top-down/bottom-up/special přečteno; censy a tvrzení o
  optimech převzaty bez přepočtu. Historické obvody a jejich cost models
  přečteny, historické priority a úplnost katalogů přeskočeny.
- Str. 107–111: full adder v (23), ripple carry a jeho cena 2+5(n−1),
  sideways recurrence (28), decoder (30), mux a Theorem S včetně důkazu.
  Sčítání tří bitů má carry (x1∧x2)∨(x3∧(x1⊕x2)); použití společného XOR
  dává pět kroků. U (28) liché n=2k+1 potřebuje k plných sčítaček, sudé
  n=2k nahrazuje poslední půlsčítačkou, tedy 5k−3. Číselné příklady souhlasí.
  Matice prvočísel a rozklad (36)/(37) přečteny; odvozené indexy dávají
  2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61. Lupanovův postup a
  součet ceny (38) přečteny, asymptotické doplnění odkazované do úloh nebylo
  znovu odvozeno. Vylepšení horní meze z2023 je známý doplněk.
- Str. 112–117: seven-segment truth tables, footprints, partial functions,
  tic-tac-toe definice a vady první strategie. Konstrukční řetězce přečteny,
  neimplementovány. Pozdější kratší řetězce (43)/(45) jsou známé doplňky.
  Chybné OR v (56) a součet396 místo394 jsou známá errata, ne nálezy.
  Celá herní strategie nebyla spuštěna ani znovu ověřena ve všech pozicích.
- Str. 117–121: Ashenhurstova podmínka dvou různých sloupců, bad pairs,
  Hornovy implikace, částečné funkce a více výstupů. Počet good pair patterns
  je 4+binom(4,2)(2^4−2)=88. Empirické seznamy implikací a jejich průměrné
  časy se nepřepočítávaly. Na str.120 je V4A-C0002: kompatibilní 0* a *0
  nemají generalized consensus dle32(a), ale mají průnik00. Známé erratum
  odpovědi540 mění tvrzení o existenci, nikoli definici; věta na120 zůstává
  odlišným nevyřešeným výskytem. Bipartitní charakterizace platí. Viz samostatný
  doklad; str.540/file557 prohlédnuta pouze v první části odpovědi32(a).
- Str. 121–125: local synthesis, gate elimination, explicitness, Stockmeyer–
  Meyerův jazyk a monotone lower bounds. Důkaz externí meze (71) se nepřebírá
  jako znovu ověřený; numerický důsledek sedí při r=431:
  460+0.302r+5.08 ln(r)<621 a 2^(r−5)=2^426>10^128. Současný stav lower
  bounds ani historické prvenství nebyly ověřovány.
- Str. 125–133: všechna zadání1–88 přečtena včetně algoritmu S, transduceru,
  tabulek/diagramů a exponentů v dolních mezích. Krátká kontrola formulace
  a návaznosti, žádná tvrzení o vyřešení těchto úloh. S-box hledání, minima,
  hry, asymptotické důkazy a enumerace median chains se nespouštěly.

## Errata, omezení a kurzor

Prohledány relevantní `all4a-pre`, `all4a`, `err4a`, `all4f0`, `err4f0`.
Změny str.96/98/100/103/108–110/112–115/117–118/120 a úloh na125–133 jsou
zohledněny. Zvláště: S1 na109, AND v(56), 394 gates, nové řetězce43/45,
Uhligova úloha76 O(n²) a skalární maska, indexace78 a dolní mez86(f).
Známé erratum odpovědi540 z19.6.2011 je výslovně odděleno od C0002.
Žádná karta ani lokace pro známou chybu540.

Bibliografie, citace, autorství/historické priority, externí lower bounds a
současný stav otevřených problémů přeskočeny. Reviewed označuje celou
přečtenou stránku, nikoli ověřené optimum či vyřešenou úlohu. File137/p120
zůstává partial kvůli kandidátu; file557/p540 je pouze cílené partial čtení.

Doklady: `sources/file113-150-ocr.txt`, `sources/file113-150.pdf`, původní
`images/file113.png` až `images/file150.png`; samostatný file557 a detailní
file100/file137. Původní offset +17 zachován. Další kurzor je **file151 /
tištěná134**, pokračování §7.1.3 Bitwise Tricks and Techniques.
