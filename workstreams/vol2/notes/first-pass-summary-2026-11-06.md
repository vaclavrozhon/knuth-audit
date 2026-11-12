# §3.6 — první průchod závěrem kapitoly 3

6. listopadu 2026, V2-X0132. Přečtena původní sazba 184–193 a odpovědi
599–604. Převzaty archivní důkazy a kontroly `summary-generators.md`,
`discarded-bits.md`, `truncated-lcg.md`, `summary-applications.md`.
Žádné opakování kompilací, milionových generování ani historických simulací.
Nový nález žádný; matematika a instrukce byly posouzeny při čtení.

Rozlišeny původní programy, náhrady 2002 a samostatné autorské zdroje.
C0071 je **low**, chyba pomocné vzdálenosti místo kruhové vzdálenosti;
oddělení proudů platí. C0072 je **low**, chybějící posun 1990 ve výkladu
po zahřívání, nikoli vada generátoru. C0073 je **medium**, neúplný
opravný předpis opravdu opomíjí deklaraci pole x; samostatný rng-double.c
tím netrpí. Tento nález je chyba v erratu, nikoli už opravená chyba knihy.

C0074 je **low**, chybějící n v indexu obecné expanze. C0075 je **low**,
chybějící pravděpodobnost výpisu v aritmetickém výrazu; uvedený číselný
výsledek odpovídá doplněnému faktoru. Přesný model adaptivního pokusu
se s aproximací neztotožňuje. C0076/C0077 zůstávají **medium**:
rekonstrukce parametrů není z daných pozorování vždy jednoznačná;
jde o rozpor v požadované záruce, ne o bezpečnost doporučované šifry.
C0078 **low**, rok citátu Lovelace 1843 místo 1844.

Historické benchmarky, tvrzení o rozšíření RANDU, empirické srovnání
generátorů a přesnost televizních scénářů nepodléhají novému ověření.
Převzaty jejich výslovné zdrojové limity. U úlohy 14 se neopakuje
experiment s neuvedeným seedem; jeho archivní matematické vysvětlení
a chyby vzorce jsou oddělené od historického počtu výstupů.
Úlohy 3–6 jsou programovací/diskusní zadání; nekontrolujeme znovu
už doložené vzorové programy ani neprovádíme zásahy do cizích knihoven.

První průchod pokrývá celé 184–193 a 599–603. Na 604 zbývá následující
odpověď §4.1–1, proto stránka zůstává partial. Další kurzor 194/file206
(přechod ke kapitole 4). Dřívější otevřené mezery kapitoly 3 zůstávají
v RUN_STATE; projití kapitoly neznamená jejich automatické uzavření.
