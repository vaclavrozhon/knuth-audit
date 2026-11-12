# §1.2.2–25: Briggsova skutečná metoda

V1-X0735, 2. listopadu 2026. Celá původní úloha 25 je nyní
checked: matematika je již v X0030 a poslední pramenná mezera
je doložena původním vydáním *Arithmetica logarithmica* (1624).
Celé X0033, včetně jiných historických tvrzení, zůstává partial.

Root ověřil 13 souborů, 5 005 032 bajtů, zmrazeného paketu
`parallel/logarithm-history/briggs/MANIFEST.json`, SHA-256
`3f724e802d7dcbb71185e6bac3c5806f4647c1aabab94a63a896a26fe126a2bc`,
a všech 17 vstupů: 14 společných podkladů, původní celý PDF
a dva Bruceovy navigační překlady. Původní sazbu dokládá osmistránkový
výřez s přesnou mapou obráceného pořadí celého PDF.

Root přečetl HANDOFF i celou READING. Přímo obrazově četl titul,
vlastní errata a tištěné 32, 33, 35–36. Agentovo širší přímé
čtení 31–36 je přijato v deklarovaném rozsahu. Titul sám
potvrzuje Henryho Briggse a rok 1624; chybné katalogové autorství
Neppera není použito jako rozhodující doklad.

Briggs na 35–36 udržuje dělitel D a zbytek r=N−D pro dané číslo N.
Z tabulky na 32 vybírá faktory 1+q, kde q=d·10^(−k) a d je
jedna desetinná cifra. Přijatý krok zvětšuje D o qD, zmenšuje
r o qD a přičítá log(1+q) k dosavadnímu logaritmu D.
Zde log znamená desetinný logaritmus. Zachované vztahy jsou
D+r=N a L=log D, kde L je nasčítaný výsledek.

Přímo přečtený příklad dává přesně
3041·1.0002=3041.6082 a
3041.6082·1.00008=3041.851528656. Každé násobení qD
potřebuje desetinný posun a násobení jedinou cifrou, tedy
nejvýše devět součtů. S. 33 navíc dokládá opačný směr,
odečítání tabulkových logaritmů a násobení jejich faktorů.

To odpovídá knižní opatrné formulaci „goes back in essence“:
jednoduché faktory blízko jedné a součet jejich logaritmů.
Knuthův L používá 1−2^(−k), jiné řízení a pevnou řádovou
čárku; tento přesný binární program se Briggsovi nepřipisuje.
Původní tabulkové zaokrouhlení ani všechny Briggsovy příklady
nejsou tímto nezávisle certifikovány.

Briggsova errata k 32–33 byla přímo porovnána. Čtyři vrstvy
TAOCP errat nemění tuto atribuci; známé opravy matematické
části byly již přijaty. Úspěšné testy se neopakovaly. Nový
nález není. Souvislost s exponenciálním výpočtem sama nedokazuje
Feynmanovu atribuci v úloze 28.
