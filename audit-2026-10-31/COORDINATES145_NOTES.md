# DLX 145 — sudé a liché souřadnice kvádru

3. listopadu 2026; zadání 4B str. 142, odpověď str. 455.
**Celá úloha ověřena bez nové chyby.** Známá jazyková oprava E072
z 24. července 2020 je v našem 4B již zapracovaná.

V jednom rozměru souřadnice `2i` označuje bod `i`, zatímco `2i+1`
označuje interval `[i,i+1]`. Kartézský součin tří takových objektů
je právě vrchol, hrana, stěna nebo buňka podle počtu intervalů, tedy
podle **0, 1, 2 nebo 3 lichých souřadnic**. Koncové body dávají jednoznačnou
inverzi. Každá přípustná celočíselná trojice má význam, nic není vynecháno
a různé trojice označují různé objekty. Platí to i pro nulový rozměr kvádru.

Pro rozsahy `0≤x≤2l`, `0≤y≤2m`, `0≤z≤2n` proto počty udává koeficient
u příslušné mocniny t v součinu

`((l+1)+lt)((m+1)+mt)((n+1)+nt)`.

Jeho čtyři koeficienty jsou přesně všechny čtyři vzorce v zadání.
Součet je `(2l+1)(2m+1)(2n+1)`, takže není potřeba žádný další typ položky.

Středy v tomto zdvojeném souřadnicovém systému vysvětlují všechny
uvedené průměry: střed dvou sousedních vrcholů je hrana, střed protějších
rovnoběžných hran jedné jednotkové stěny je stěna, střed protějších
stěn jedné buňky je buňka. Naopak sousední kolineární hrany se setkají
ve vrcholu, sousední rovnoběžné stěny stejného typu v hraně a sousední
buňky ve stěně; průměr jejich označení dává právě společný objekt.
Slovo „parallel“ v první části se čte v kontextu hran jedné jednotkové
stěny, ne libovolných vzdálených hran kvádru.

Vytištěné příklady `(2i,2j+1,2k)`, `(2i+1,2j,2k+1)` a
`(2i+1,2j+1,2k+1)` mají přesně uvedené koncové vrcholy. Stejná
konstrukce ve dvou rozměrech rozlišuje H/V hrany jejich lichou souřadnicí,
takže poznámka odkazující na odpověď 109 je správně.

Doprovodná krátká kontrola pokryla všech **125 kvádrů** s rozměry
0 až 4: **15 625 objektů** a **30 000 identit průměrů**, včetně
degenerovaných případů. Porovnala přímé množiny koncových vrcholů,
inverzi, jedinečnost, dimenzi a všechny čtyři počty. Obecný důkaz
výše není omezen na tento konečný test.

E072: autorův draft 2019 na str. 159 ještě píše „3 three odd coordinates“;
veřejné erratum Fascicle 5, str. 263, mění „3 three odd“ na „3 odd“.
Datum v TeXu `(20.07.24)` znamená **24. 7. 2020**, což potvrzuje tištěný
seznam errat. Naše 4B str. 455 již má správnou podobu. Jde o známou
opravu, nikoli nový nález. Obě původní stránky byly prohlédnuty.

Doklady: [kontrola a počty](results/coordinates145/checked.json),
[program](check_coordinates145.py),
[šest vrstev errat](results/hexagons144/errata-check.json),
[strana 455](images/vol4b-p455-polygons143.png),
[draft str. 159](images/fasc5c-p159-polygons143.png).
