# CI sítě, celý důkaz F a retrakty

Checkpoint X0107, P1000–P1014. Originály p73–74/file90–91,
zadání 89/93/94 na p91/file108 a celé příslušné odpovědi
na p551/file568 prohlédnuty. Zvlášť jsou uloženy detaily
69–71. Žádný matematický program ani census nebyl spuštěn.

Přebíráme P0997 (hranový homomorfismus každé CI sítě),
P0998 (úplné relace a nejvýše jeden chybějící vzor na pár
sloupců), P0999 (acykličnost a zákaz cesty k doplňku),
P0943–P0945 (konvexní řezy a isometrie) a celou Table 2
v proof-074. Obecné důkazy zde mají neprázdné X. Společná
konvence P0886 o prázdném objektu při t=0 zůstává oddělená;
pro t=0 a X={()} jsou všechny konstrukce identitou.

## Síť 69 a všechna její mezidata — P1000

Vstup označme (a,b,c,d), linie shora 1 až 4. Sedm po
sobě jdoucích stupňů původního obrázku je:

1. Invertovat 2 a porovnat 3,4.
2. Invertovat 3.
3. Porovnat 1,2 a současně 3,4.
4. Invertovat všechny čtyři linie.
5. Porovnat 1,3 a současně 2,4.
6. Invertovat 1,2.
7. Porovnat 1,4.

Komparátor vždy dává min na horní linii. Položme
p=a∧¬b, q=a∨¬b a e=c XOR d. Po prvním stupni je stav
(a,¬b,c∧d,c∨d). Po třetím je (p,q,e,1), protože
¬(c∧d)∧(c∨d)=e a ¬(c∧d)∨(c∨d)=1. Další stavy jsou

    (¬p, ¬q, ¬e, 0),
    (¬(p∨e), 0, ¬(p∧e), ¬q),
    (p∨e, 1, ¬(p∧e), ¬q).

Výstup je tedy přesně

    (¬a∧b∧e, 1, ¬(a∧¬b∧e), (a XOR b)∨e).

Pro vytištěný vstup 0010 jsou stavy po jednotlivých
stupních 0101, 0111, 0111, 1000, 0010, 1110, 0111.
Všechny bity vytištěné mezi moduly souhlasí. Obrázek
má šest komparátorů a osm invertorů, celkem 14 modulů.

## Všech šestnáct hodnot 70 — P1001

Předchozí obecný vzorec dává následující úplné rozdělení.
Sloupce jsou čtyři hodnoty cd v pořadí 00,01,10,11.

| ab | cd=00 | cd=01 | cd=10 | cd=11 |
|---|---|---|---|---|
| 00 | 0110 | 0111 | 0111 | 0110 |
| 01 | 0111 | 1111 | 1111 | 0111 |
| 10 | 0111 | 0101 | 0101 | 0111 |
| 11 | 0110 | 0111 | 0111 | 0110 |

Jde o každou vytištěnou buňku, nikoli o výběr testů.

## Všechny relace 71 — P1002

Použijme vrcholy A=⟨wwxyz⟩, B=⟨wyz⟩, C=⟨wxyzz⟩,
D=⟨xyz⟩, E=⟨wxyyz⟩, F=⟨wxz⟩, G=⟨wxxyz⟩,
H=⟨wxy⟩ a w,x,y,z jako v proof-074. Z úplných štítků
Table 2 jsou jedničkové podpory sloupců přesně

    S1={z}, S2={y}, S3={B,C,D,E,y,z}, S4={x},
    S5={C,D,F,G,x,z}, S6={D,E,G,H,x,y}, S7=V\{w}.

Ve všech dvojicích se vyskytuje 00, protože w má samé
nuly. Disjunktní podpory zakazují 11, inkluze Si⊆Sj
zakazuje 10. Tím dostaneme přesně levých 18 implikací:

    1 → ¬2,3,¬4,5,¬6,7
    2 → 3,¬4,¬5,6,7
    3 → ¬4,7
    4 → 5,6,7
    5 → 7
    6 → 7.

Kontrapozice dávají přesně pravou polovinu 71:

    2,¬3,4,¬5,6,¬7 → ¬1
    ¬3,4,5,¬6,¬7 → ¬2
    4,¬7 → ¬3
    ¬5,¬6,¬7 → ¬4
    ¬7 → ¬5
    ¬7 → ¬6.

Z 21 párů sloupců chybějí jen (3,5),(3,6),(5,6),
protože všechny čtyři vzory skutečně existují. Jejich
průniky jsou {C,D,z}, {D,E,y}, {D,G,x}; obě jednostranné
diference jsou postupně {B,E,y}/{F,G,x},
{B,C,z}/{G,H,x}, {C,F,z}/{E,H,y}. Vzor 00 dává w.
Ostatních 18 párů je vyčerpáno uvedenými relacemi;
P0998 vylučuje další chybějící vzor téhož páru.

## Vysvětlující konvexní odstavec — P1003

Hrana A–B mění právě bit 3. Její strana blíže B je
proto přesně S3 a je konvexní podle P0943. V S3 není x,
tedy jeho bit 4 je všude nulový. Hrana G–x mění právě
bit 4; každý vrchol S3 je proto blíže G než x. To
ověřuje oba výběry vrcholů i všechny vzdálenostní
a konvexní kroky odstavce pod 71.

## Antisymetrické topologické pořadí a celé 72 — P1004

Graf všech relací je DAG uzavřený na kontrapozici.
Vyberme zdroj u. Jeho doplněk ¬u je sink: hrana
¬u→v by kontrapozicí dala ¬v→u, spor se zdrojem.
Odstraňme oba vrcholy a opakujme. Zbylý graf má
stejné vlastnosti. Když u dáme na první a ¬u na
poslední místo, indukce dává pořadí u1,...,uN,
N=2t, s uj=¬u(N+1−j). Všechny hrany jdou vpřed.
P0999 navíc vylučuje hranu mezi dvěma doplňky.

Vytištěné 72 má pozice

    1, ¬7, 4, 2, ¬3, ¬5, ¬6, 6, 5, 3, ¬2, ¬4, 7, ¬1.

Pozice každého komplementárního páru mají součet 15.
Levé relace 71 mají pozice začátku/cílů:

    1 : 11,10,12,9,7,13
    4 : 10,12,6,8,13
    10: 12,13
    3 : 9,8,13
    9 : 13
    8 : 13.

Každý cíl je větší než začátek. Obrácení indexů
ověřuje současně všech 18 kontrapozic. Tím jsou
ověřeny všechny hrany, ne pouze sousedé v pořadí.

## Čtyři moduly 73 — P1005

Pro fyzické linie i<j převádějí invertory před a po
komparátoru příslušné literály na min a max. Přesné
výstupy na dvojici vstupních bitů (a,b) jsou:

| relace | výstup |
|---|---|
| i→j | (a∧b,a∨b) |
| i→¬j | (a∧¬b,¬a∧b) |
| ¬i→j | (a∨¬b,¬a∨b) |
| ¬i→¬j | (a∨b,a∧b) |

To odpovídá všem čtyřem původním diagramům: žádné
invertory; dva na dolní; dva na horní; dva na obou
liniích. Každý shluk vynucuje danou relaci a každý
již splňující vstup ponechá. Pokud zvolené topologické
pořadí uvádí fyzickou linii j před i, přejdeme na
kontrapozici. Operace na skutečných bitech se nezmění.
Jeden shluk obsahuje nejvýše pět modulů.

## Přesná úplnost smyčky, ukončení — P1006

Hrana pozic (k,k+d) má kontrapozici
(N+1−k−d,N+1−k), se stejnou vzdáleností d. Z dvojice
zvolíme začátek ne větší než začátek protějšku:

    k ≤ N+1−k−d  ⇔  k ≤ t−floor(d/2).

Rovnost obou začátků je možná pouze pro dvojici
komplementárních literálů téže proměnné, mezi nimiž
relace není. Také vzdálenost N−1 dává jen takový pár.
Smyčka d=N−2,...,1 a k=1,...,t−floor(d/2) proto
zpracuje každou platnou relaci právě jednou modulo
kontrapozici a nic nevynechá. Je konečná. Pro t=0
nebo t=1 nemá žádnou platnou dvojici; neprázdné
redukované X je v těchto případech celý příslušný cube.

## Zachování předchozích relací; celá úloha 89 — P1007

Důležitý předpoklad: zpracováváme všechny platné
implikace mezi různými souřadnicemi. Jsou tedy
tranzitivně uzavřené tam, kde jsou konce různé;
cesta ke komplementu je P0999 vyloučena.

Nejdříve uvažujme hodnoty z1,...,zN na všech literálech
formálně jako nezávislé bity. Komparátor pro hranu
k→l, k<l, zmenší zk na min(zk,zl) a zvětší zl na
max(zk,zl). Před krokem jsou splněny všechny dřívější
relace, zejména všechny s rozdílem větším než l−k.

Starou relaci s oběma konci mimo {k,l} krok nemění.
Relace začínající v k se může jen uvolnit; totéž
relace končící v l. U staré i→k by vadilo zmenšení
zk, ale tranzitivita dává i→l s větším rozdílem,
která už je splněna. Proto zi≤zk i zi≤zl, tedy
zi≤min(zk,zl). U staré l→j obdobně máme k→j
s větším rozdílem a zk,zl≤zj, takže nový zl≤zj.
Toto jsou všechny možnosti sdílení konce; stejná
relace je právě vynucena a obrácená v DAG není.
Argument pokrývá i staré relace se stejným rozdílem.

Skutečný shluk na bitech odpovídá dvěma těmto
komparátorům: na (k,l) a na komplementární dvojici
(N+1−l,N+1−k). Dvojice jsou disjunktní, protože
jde o dvě různé proměnné. Po prvním komparátoru
platí všechny staré relace; druhý je zachová stejným
argumentem a nově vynucené k→l vůbec nezmění.
Spolu zachovají antisymetrii hodnot z(N+1−j)=1−zj.
Dočasná nezávislost formálních bitů nevadí: důkaz
zachování používal jen nerovnosti, nikoli antisymetrii.
Tím jsou negované případy skutečně odvozeny.

V označení odpovědi 89 se tak dokládají všechny její
případy: i=i' zmenšuje levou stranu; j=j' zvětšuje
pravou; i=j' potřebuje dřívější delší i'→j a dává
xi'≤min(xi,xj); j=i' potřebuje i→j' a dává
max(xi,xj)≤xj'. Rozpojené konce jsou beze změny.
Žádný případ vytištěné odpovědi není vynechán.

## Dokončení věty F — P1008

Indukce přes konečnou smyčku nyní zaručuje, že na
jejím konci jsou splněny všechny relace. Jejich
množina modelů je přesně X podle Theorem S/P0998,
takže f(a)∈X pro libovolný vstup a∈{0,1}^t.
Je-li a∈X, splňuje každou relaci od začátku a
každý shluk jej ponechá podle P1005. Tedy f(a)=a.
CI homomorfismus P0997 je proto retrakce; také
f(f(a))=f(a). Jde o celou větu, včetně obou jejích
závěrů a všech předpokladů, pro neprázdné X.

## Deklarovaný model a odvozené náklady — P1009

Počet zkoušených dvojic ve smyčce je pro t≥1
Σ[d=1..2t−2](t−floor(d/2))=t²−1. Na jeden pár
souřadnic připadá nejvýše jeden chybějící vzor,
tedy nejvýše binom(t,2) shluků a 5 binom(t,2)
jednotlivých modulů. Při t=0 jsou oba počty nulové.

Je-li X zadáno explicitním seznamem bitových vektorů,
všechny zakázané vzory lze získat v O(|X|t²)
bitových krocích a O(t²) pomocné paměti. Zdrojový
toposort se záznamem vstupních stupňů a odstraňováním
každé hrany jednou stojí O(t+r), r≤t(t−1).
Potom tabulka relací dává O(1) na test a celá
zbývající konstrukce O(t²), s výstupem O(t²).
To jsou zde odvozené náklady v uvedeném modelu;
kniha na p74 samostatnou implementační cenu neslibuje.
Hloubku paralelního provedení úlohy 88 tato mez
neřeší a tato úloha zůstává pro další blok.

## Celý konkrétní diagram 74 — P1010

Dosazení 71/72 do smyčky dává přesně následující
shluky v pořadí zleva doprava. Zápis relace je vždy
upraven na fyzicky horní první linii; (d,k) je
skutečný vybraný pár v topologickém pořadí.

| pořadí | (d,k) | fyzická relace |
|---|---|---|
| 1 | (12,1) | 1→7 |
| 2 | (11,1) | 1→¬4 |
| 3 | (10,1) | 1→¬2 |
| 4 | (10,2) | 4→7 |
| 5 | (9,1) | 1→3 |
| 6 | (9,2) | 2→7 |
| 7 | (8,1) | 1→5 |
| 8 | (8,3) | 2→¬4 |
| 9 | (6,1) | 1→¬6 |
| 10 | (6,3) | 4→5 |
| 11 | (6,4) | 2→3 |
| 12 | (5,2) | 6→7 |
| 13 | (5,3) | 4→6 |
| 14 | (4,2) | 5→7 |
| 15 | (4,4) | 2→6 |
| 16 | (3,2) | 3→7 |
| 17 | (2,3) | 3→¬4 |
| 18 | (2,4) | 2→¬5 |

Pro d=7 ani d=1 žádná platná relace není. Původní
diagram má každé z těchto 18 svislých spojení a
právě dva invertory u šesti negovaných cílů
(řádky 2,3,8,9,17,18), tedy 30 modulů celkem.
Také vytištěná první čtveřice relací souhlasí:
čtvrtý vybraný pár je ¬7→¬4, tj. 4→7.

V komentáři je ukázkový vynechaný pár ¬7,3 na
pozicích 2,10. Relace ¬7→3, ekvivalentní ¬3→7,
je skutečně nepravdivá na vrcholu w se samými nulami.
Žádný příslušný modul tedy chybět nemá.

## Celý Corollary F — P1011

Neprázdná redukovaná X má v každé souřadnici nulu
i jedničku. Uzavřenost na AND/OR tedy dává AND všech
jejích prvků =0^t a OR všech prvků =1^t, oba v X.
Ve dvojici sloupců nemůže chybět 00 ani 11. Zbývají
jen pozitivní implikace i→j nebo j→i a jejich
negativní kontrapozice. DAG pozitivních implikací
topologicky uspořádejme a tak přejmenujme souřadnice.
Každá pozitivní implikace pak jde z menší fyzické
linie na větší a vynutí ji obyčejný komparátor.
I kdyby smyčka vybrala její negativní kontrapozici,
stejná operace na fyzických bitech je tento komparátor.
Žádný invertor není třeba. Pro t=0 je síť prázdná.

## Retrakty a celá úloha 93 — P1012

Nechť f:G→X⊆G je hranový homomorfismus a f|X=id.
Každá cesta uvnitř X je cestou v G, tedy dX≥dG.
Naopak obraz nejkratší G-cesty mezi x,y∈X je
sled v X stejné délky s konci x,y. Odstraněním
případných opakování vznikne cesta ne delší, tedy
dX≤dG. Obě meze dávají rovnost. Tím je doložen
také nevyřčený přechod „path“ v tištěné odpovědi,
jejíž obraz může formálně nejprve být jen sled.

Pro nesouvislé dvojice je vzdálenost na obou stranách
nekonečná; konečná cesta v G by předchozím zobrazením
dala konečnou v X. Retrakt souvislého grafu je tudíž
souvislý. I kdyby X nebyl předem zadán jako indukovaný
podgraf, každá hrana G mezi jeho vrcholy je zachována
fixováním konců, a proto patří do X. Celý odstavec
o vzdálenostech na p74 je tedy ověřen.

## Retrakt krychle je mediánový: celá hlavní část 94 — P1013

Nechť f retractuje krychli na X, x,y,z∈X a
w=m(x,y,z) je bitový medián v celé krychli.
Homomorfismus nezvětšuje vzdálenosti, a proto

    d(x,f(w))+d(f(w),y)
      ≤ d(x,w)+d(w,y) = d(x,y).

Trojúhelníková nerovnost dává opačnou nerovnost,
tedy rovnost. Stejně pro dvojice x,z a y,z.
P1012 dovoluje všechny vzdálenosti číst i v X.
Vrchol f(w) proto leží ve všech třech intervalech.
V krychli je jejich jediným společným bodem w:
v každé souřadnici dvě shodné vstupní hodnoty
vynutí tuto hodnotu na intervalu příslušné dvojice.
Tedy f(w)=w∈X. Jde o celý vytištěný argument
včetně důkazu jeho vzdálenostní a jedinečnostní části.

## Redukce konstant, první odstavec 94 a charakterizace — P1014

Odstranění konstantních souřadnic je izomorfismus
indukovaného grafu i mediánové algebry. Každá zbylá
souřadnice nabývá obou hodnot. Souvislost X dává
cestu mezi vrcholy s různými hodnotami; na cestě
musí být hrana měnící tuto souřadnici. Hrana krychle
mění právě jeden bit, takže jde přesně o redukčního
svědka požadovaného na p72. Tím je dokázána úplná
redukce, nejen různorodost sloupců.

Speciálně dvě nekonstantní souřadnice nemohou být
vždy stejné ani vždy komplementární: jejich svědecká
hrana by změnila jen jednu a vztah porušila. Také
tištěné zdůvodnění pomocí typů 00 a 11 je platné:
žádná krychlová hrana nemůže přejít mezi typy bez
mezilehlého 01/10, takže by nebyla souvislost.

P1013 a tento redukční argument dokazují celou 94;
P1008 dokazuje opačný směr. Neprázdné konečné mediánové
grafy jsou tedy právě retrakty konečných krychlí,
jak tvrdí závěr p74. Důkaz zde nepřebírá nedoloženou
externí charakterizaci.

## Errata, bibliografické meze a stránkový rozsah

Prověřeny všechny relevantní vrstvy `all4a-pre`, `all4a`,
`err4a`, `all4f0`, `err4f0` v `errata/text/`.
Známé opravy p73 (x=x1...xt), p74 (šipka místo ≤)
a dvakrát „relations“ místo „inequalities“ jsou
zohledněny. Jde o test existence relace v systému,
nikoli o test aktuálních vstupních hodnot. Další
známý dodatek k 88 na p551 patří až do dalšího bloku.
Žádná z těchto oprav není nález.

Primární autorův seznam potvrzuje Federovu monografii
*Stable Networks and Product Graphs*, Memoirs AMS 116,
No. 555 (1995), 223 stran. Přesné Lemma 3.37 a celý
text monografie nebyly ověřeny. Wiedemannova citovaná
Waterloo disertace 1986 nebyla rychle dohledána a její
obsah/historická role jsou bibliografická výjimka.

Primární Springer potvrzuje Hell, *Absolute retracts
in graphs*, LNM 406 (1974), 291–301. Tvrzení „first
pointed out“ není nezávisle ověřeno. Primární Wiley
potvrzuje Bandelt, *Retracts of hypercubes*, JGT 8(4)
(1984), 501–510, DOI 10.1002/jgt.3190080407; abstrakt
uvádí přesně charakterizaci retrakty/median graphs.
Celé historické články ani priorita nebyly nově
přezkoušeny. Přesné zdroje a rozsahy jsou v
`sources/ci-retractions-bibliography.json`.

P73–74 nyní mají individuální argument ke každému
matematickému tvrzení, konkrétní síti i tabulce pro
neprázdný rozsah. P0886 ponechává společnou konvenční
otázku prázdných mediánových štítků; tyto stránky
proto zatím nepovyšujeme na bezvýhradné celé argument.
Úlohy 89,93,94 jsou úplné. Úlohy 84–88 a 90–92/95
ani zbytek p551 tím uzavřeny nejsou.
