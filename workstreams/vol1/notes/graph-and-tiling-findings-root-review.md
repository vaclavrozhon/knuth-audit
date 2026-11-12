# Kořenová revize C0051 a C0052

2026-11-01. Root přečetl oba samostatné podklady, přímo zobrazil
originály377/581 a první/poslední stranu Jeandel–Rao i původní all1-15.

## C0051: čas výpisu cyklů, confirmed

Původní zadání výslovně chce vypsat fundamentální cykly a C6 vypisuje
jednotlivé orientované hrany se znaménkem. Nejde o předpoklad odvozený
jen z obvyklého významu slova výstup. C1/C2 mění zakořenění, nikoli
množinu přijatých hran. Při vstupní cestě a následných obloucích
(1,k) pro k=3,...,n je tak součet délek přesně n(n+1)/2−3.
To vyvrací O(m log n) obecnou nekonečnou rodinou, bez časového experimentu.

Root také nezávisle zkontroloval silnější DFS argument. Před návštěvou
univerzálního vrcholu1 není v grafu bez1 žádné větvení mimo cestu,
takže dosavadní předci tvoří interval. Zbývají nejvýše dvě komponenty
a každou první rekurze z1 vyčerpá. Proto má1 nejvýše dva syny a rodiče.
Je-li sám kořenem, má jediného syna. Po jeho odstranění jsou nejvýše
tři stromové komponenty, všechny cesty. Nejmenší součet vzdáleností
cesty velikosti s od jejího připojení je alespoň s²/4.
Nerovnost mezi součtem čtverců a čtvercem součtu dává (n−1)²/12.
Odečtení nejvýše tří stromových paprsků a přičtení nestromových hran
dává uvedenou dolní mez délky cyklů. Volba DFS pořadí proto nepomůže.

Opravená mez O(n+m+L) je dosažitelná: vytvoříme DFS strom a hloubky,
u každé nestromové hrany vystoupáme z hlubšího konce po stromu,
dokud se oba konce nesetkají. Každý krok této fáze vydá nebo dočasně
uloží právě jednu hranu budoucího cyklu. Pomocný zásobník dovolí
vypsat obě části ve správném pořadí a se znaménky; práce je úměrná
délce cyklu. Součet s inicializací je uvedená mez.
Hvězdová kostra vějíře má krátké cykly, ale není DFS kostrou;
report tuto podstatnou mez obecnosti výslovně zachovává.

Přesné primární Tarjanovo čtení a čtyři vrstvy errat dokumentuje
podagent ve zmrazeném podkladu. Rootův protipříklad nevyužívá
neověřenou větu z Tarjanova článku.

## C0052: rozsah stran, confirmed

Originál all1-15 přímo uvádí rozsah1:1–1:39. Publikovaná sazba prvního
a posledního listu článku uvádí37pp a poslední stranu37. Nejde tedy
jen o počet souborových PDF stran, odlišný preprint či bibliografický
vyhledávací výsledek. Správná citace je1:1–1:37.
Původní matematický výsledek nebyl tímto zjištěním zpochybněn.
Nový nález patří pozdějšímu doplňku z31.1.2023, nikoli originálu1997.

Oba globální reporty jsou anglicky a ASCII. Není doloženo prvenství
ani konkrétní fyzický pozdější výtisk; žádné externí odeslání neproběhlo.

