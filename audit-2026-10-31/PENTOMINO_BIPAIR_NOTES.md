# Bipáry pentomin: úloha 217

Kontrola 1. listopadu 2026, hlavní díl 4B, strany 151 a 473–474.

Úplný katalog má opravdu **34** tříd bez děr. Každé z dvanácti pentomin se
vyskytuje. Osmnáct oblastí má osovou souměrnost podle vodorovné či svislé osy,
čtrnáct podle diagonály a dvě nemají žádnou netriviální symetrii. Žádný nový
nález. Podmínku bez děr zadání opomíjí, ale odpověď to výslovně přiznává;
nepovažujeme to za nový objev.

## Dva nezávislé postupy

[check_pentomino_bipairs.py](check_pentomino_bipairs.py) nejprve generuje všechny
překrývající se polohy téhož dílku. Každé relativní posunutí lze získat
ztotožněním jedné buňky obou kopií. Rozdíl má 1 až 4 kladné a stejně mnoho
záporných buněk. Kanonizace používá posunutí, D4 a změnu znaménka; všechny
možné zrušené průniky zůstávají uchovány i při symetriích rozdílu. Shodné
rozdíly různých pentomin se spojí pouze tehdy, když se průniky nekříží.

[verify_pentomino_bipairs.py](verify_pentomino_bipairs.py) místo rozdílů přímo
generuje dvojice disjunktních dílků, které se dotýkají hranou. Seskupí je
podle desetibuněčné oblasti a vyhledá různé rozklady týmiž dvěma pentominy.
Prošlo 28 140 poloh a 27 968 oblastí normalizovaných posunutím. Dostali jsme
přesně stejných 34 přípustných a 7 vyřazených bipárů s dírou.

Výsledky: [první katalog](results/pentomino_bipairs/catalog.json),
[nezávislá kontrola](results/pentomino_bipairs/independent.json),
[obrázek všech rozkladů](results/pentomino_bipairs/catalog.png).

## Čísla a příklady

Počty normalizovaných rozdílů pro O,P,Q,R,S,T,U,V,W,X,Y,Z jsou
10,64,81,73,78,25,23,24,22,3,78,24. Počty s jedinou kladnou buňkou jsou
1,7,3,3,2,0,1,0,1,0,4,0. Vše souhlasí s knihou.

Rozdíl sdílí právě 1,2,3,4 pentomina v počtech 410,27,11,2. Oba uvedené
čtyřnásobné rozdíly a jejich jména souhlasí. Rozdíl 00−23 pro Q,W opravdu
nedovoluje žádné doplnění. U 00+01−12−22 vyhovuje bez díry jen PY;
UY má díru a PU se nedá spojit. [Přesná data příkladů](results/pentomino_bipairs/examples.json).

Názvy odpovídají Knuthově abecedě: O=obvyklé I, Q=L, R=F, S=N.
Případy s pěti změněnými buňkami by měly disjunktní kopie téhož pentomina;
pro bipár různých typů by pak druhý dílek musel být kongruentní s prvním.
Proto je omezení k≤4 úplné. Obrázky knihy nebyly jednotlivě přepsány;
ověřen je úplný nezávislý katalog, počty, symetrie a uvedené algebraické příklady.
