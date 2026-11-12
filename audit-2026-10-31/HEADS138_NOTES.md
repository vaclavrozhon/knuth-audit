# DLX 138 — Heads and tails

Stav 2. listopadu 2026: matematická část je prověřená včetně všech obrázků
a úplných množin řešení. Úloha jako celek zůstává `partial`, protože původ
hlavolamu není nezávisle doložený. **C033** je drobný kandidát na doplnění
vysvětlení symetrií, žádný nový potvrzený numerický nález. **E068** je již
opravené historické erratum.

Zadání: tištěná strana 140 / PDF 160. Odpověď: strana 452 / PDF 472.
Oba originály byly zobrazeny. Autorův draft z 11. září 2019 má stejný
výklad symetrií na straně 156; obsahuje ještě staré `96/6 = 12`.

## Model a původní obrázky

Hrany zapisujeme proti směru hodinových ručiček od severu: N, W, S, E.
Velké písmeno je hlava, malé ocas. Barvy obrázku: A zelená, B modrá,
C bílá, D červená. Typ dlaždice je cyklický zápis začínající dvěma
hlavami, například `ABcd`. Permutace čtyř barev dávají 24 typů,
každý se čtyřmi natočeními; odraz není povolené umístění jedné dlaždice.

`extract_heads138.py` čte původní vektorové trojúhelníky a čtvercové
ořezové oblasti. Krátká strana určí základnu, protilehlý vrchol rozliší
hlavu směřující do středu od ocasu směřujícího ven. Kontrola zahrnuje
**488 hran**: 24 samostatných dlaždic a čtyři sestavy s 24/25/24/25 dílky.
Každá sestava obsahuje správný inventář, všechny kontakty souhlasí.
Oba obdélníky mají správné kontakty i přes protilehlé hranice.

Vnější hrany dané strany čtverce mají barvu odpovídající hrany jokeru;
nemusí mít všechny tutéž polaritu. Původní obrázek tento rozdíl ukazuje.
První verze našeho validátoru měla zbytečně silnou podmínku; ještě před
hledáním byla opravena podle originálu.

## Úplné výčty a normalizace

XCC má primární položku pro každou buňku i běžnou dlaždici. Sekundární
položka reprezentuje společnou hranu. Převrácení velikosti písmen na
stranách S/E mění párování hlava–ocas na rovnost barev XCC, i přes švy
toru. Modely tak bijektivně odpovídají sestavám.

Nezávislý C++ program generuje permutace a rotace přímo, vyplňuje buňky
po řádcích, kontroluje geometrické sousedy a bitovou maskou zakazuje
opakování dlaždic. Obě metody skončily úspěšně a mají **celé stejné
množiny 85 360 obdélníků a šesti čtverců s jokerem**. Všechny modely
jsou uložené a geometricky validované, nejde o vzorky.

| Rohový typ ABcd | Možností XCC | Řešení |
|---|---:|---:|
| Všechna čtyři natočení | 4 + 23²·4 = 2120 | 85 360 |
| Severní hrana je hlava | 2 + 23²·4 = 2118 | 42 680 |

První normalizace odstraňuje 4! přejmenování barev. Druhá odstraňuje
navíc **globální záměnu všech hlav s ocasy**, následovanou přejmenováním.
Tato operace zachovává inventář a pravidla. Působí volně, protože mění
polaritu severní hrany, kterou přejmenování čtyř barev nemění.
Bez normalizace barev je 85 360·24 = 2 048 640 označených sestav.

Samostatný původní DLX2 běh s 2118 možnostmi vrátil právě podmnožinu
42 680 modelů se severní hlavou. Spotřeboval 12 910 086 531 hrubých
vyhledávacích memů, což se zaokrouhlí na knižních 13 G. Po odečtení
`unmems` jde o 10 651 761 779. Reprodukujeme přibližnou velikost;
přesné pořadí a účtování autorova historického běhu doloženo není.

## Symetrie a C033

Posuny 4×6 a dva nezávislé odrazy dávají grupu 96 prostorových operací.
Všech 96 permutací bylo porovnáno s nezávislou souřadnicovou transformací;
zkontrolována je uzavřenost všech 9216 složení. Každá orbita je ověřena
proti úplné množině řešení; orbity jsou disjunktní a množinu pokrývají.

| Automorfismů | Pouze čtyři barvy a prostor | Navíc globálně hlavy ↔ ocasy |
|---:|---:|---:|
| 1 | 511 | 79 |
| 2 | 666 | 531 |
| 3 | 15 | 5 |
| 4 | 150 | 351 |
| 6 | 13 | 6 |
| 8 | 0 | 68 |
| 12 | 6 | 12 |
| 24 | 0 | 4 |
| Celkem tříd | **1361** | **1056** |

Poslední sloupec přesně reprodukuje knihu. Pracuje na 42 680
reprezentantech po odstranění polarity. Před tímto odstraněním má
rozšířená grupa řád 192.

Obrázek zadání má šest automorfismů; oba uvedené generátory souhlasí
i s barevnými permutacemi A→C→D→A a A↔D. Obrázek odpovědi má bez
záměny hlav/ocasů **12**, s ní **24** automorfismů. Jeho odraz shora
dolů vyžaduje právě globální záměnu polarity a žádné přejmenování barev.
Také uvedený posun o sloupec a dva řádky a levopravý odraz vyžadují
záměnu polarity. Všechny potřebné permutace jsou v `group-checked.json`.

Text (a) uvádí posuny, odrazy a přejmenování barev, ale globální záměnu
hlav a ocasů nezmiňuje. S ní jsou všechna čísla správná. **C033 zůstává
kandidátem na vyjasnění konvence**, ne potvrzenou chybou v počtech.
Autor mohl „barvami“ mínit rozšířené štítky Algorithm C. Odpověď 139(a)
globální záměnu hlav s ocasy uvádí výslovně.

## Joker a nespočetně mnoho pokrytí roviny

Při pevném jokeru ABCD jde o 49 primárních a 60 sekundárních položek.
Osm vnitřních běžných buněk má 96 možností, dvanáct okrajových 24,
čtyři rohové 8 a střed jednu: 8·96 + 12·24 + 4·8 + 1 = **1089**.

Šest řešení tvoří tři transpoziční dvojice. Každé je zachováno otočením
o 90 stupňů a odpovídajícím přejmenováním barev jokeru. Mají dva vzory
hlav/ocasů, v každém tři sestavy; transpozice vzory prohazuje. „Tři
řešení“ v (c) přirozeně znamenají zástupce se stejnou polaritou.

Odraz shora dolů, výměna hlav za ocasy a B↔D dává přesně vytištěný
duální obrázek. V každém vzoru mají tři hlavové bloky tutéž úplnou
hranici a tři ocasové bloky také. Každá z devíti dvojic se spojí ve
všech čtyřech směrech: celkem jsou prověřena **72 spojení**.

Na šachovnici 5×5 bloků zafixujeme ocasové bloky a nezávisle volíme
mezi dvěma různými hlavovými bloky na nekonečně mnoha místech. To je
injekce {0,1}^N do platných pokrytí roviny; nespočetnost je dokázána.

## Errata a dosud otevřené zdroje

Čtyři oficiální originály porovnány 2. listopadu 2026 v 15:22 UTC,
beze změny. Prohledány dlouhé i krátké seznamy 4B/F5 a oba zdroje TeX,
se zohledněním posunu stran 140/452 → 138/260. **E068:** oprava
z 23. července 2020 mění `96/6=12` na `96/6=16`. Lokální 4B má
správných 16. Odpovídající oprava konvence C033 nalezena nebyla.

Původní manuál či katalog k „Super Heads & Tails“ z roku 1990 nebyl
získán. Nedoložené zůstávají rok, autorství Howarda Swifta pro tuto
sadu, omezená výroba a historický výrok o MacMahonovi. Vyhledávání
našlo autorův draft a jiné Swiftovy hlavolamy. Katalog sbírky Slocum
v Indianě vrátil jen ověřovací stránku i přes HTTP 200; nešlo o obsah
katalogu. Přístupová kontrola nebyla obcházena.

Přijaté výsledky: [accepted.json](results/heads138/accepted.json).
Další sekvenční úloha **139** používá stejnou sadu. Hotové výčty 138
neopakovat; jejich programy a důkazní soubory zachovat beze změny.
