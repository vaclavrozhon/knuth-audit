# DLX 129: symetrie MacMahonových trojúhelníků

Rozsah: zadání na stranách 138–139 a celá odpověď na stranách 448–449
lokálního 4B, první vydání, druhý dotisk. Doplnění ze 2. listopadu 2026
navazuje na [původní výčty a F065](MACMAHON_NOTES.md); úspěšná hledání
neopakuje. Původní stránky 139, 448 a 449 byly znovu vizuálně prohlédnuty.

Matematické závěry jsou rozšířeny o obecné důkazy redukcí, kontrolu všech
pěti obrázků a výslovný součet překrývajících se tříd. Celá úloha zatím
zůstává `partial`: chybí originál citované příručky z roku 1991. Samotný
starší záznam `checked` o počtech nebyl dokladem úplného průchodu úlohou.

## Proč jsou možné právě uvedené symetrie

Geometrie je konstruována z koncových bodů hran, nezávisle na názvech
sekundárních položek v XCC. Rotace o 60° kolem vrcholu (2,2) působí po
posunu počátku jako `(x,y) → (−y,x+y)`. Spolu s reflexí `(x,y) → (y,x)`
dává všech dvanáct symetrií hexagonu. Každá je ověřena jako permutace
24 trojúhelníků a 42 hran.

Slabá symetrie zachovává hranice barevných ploch, tedy všechny tři testy
rovnosti dvojic barev v každém trojúhelníku. Silná symetrie navíc indukuje
jediné globální přejmenování čtyř barev. Protože na společných hranách
barvy souhlasí, není třeba doplňovat další hranice mezi sousedními dílky.

Čtyři jednobarevné dílky musejí při každé slabé symetrii tvořit invariantní
množinu. Rotace o 60° a 300° mají jen šestiprvkové orbity buněk; rotace
o 120° a 240° jen tříprvkové. Ani jedna proto nemůže zachovat čtyři
jednobarevné buňky. Zbývá pouze půlobrat. Jeho permutace barev při silné
symetrii nemá pevný bod a má řád dva, tedy jednu ze tří podob
`(ab)(cd), (ac)(bd), (ad)(bc)`. Přejmenováním lze zvolit poslední z nich.

Silná reflexe neexistuje. Všech deset involucí barev bylo zkontrolováno
takto: geometricky pevná hrana potřebuje pevnou barvu; každý typ dílku,
který zrcadlení s přejmenováním zachová, musí obsadit pevnou buňku, protože
každý typ je použit právě jednou. Hornodolní reflexe má čtyři pevné hrany
a žádnou pevnou buňku, levopravá dvě pevné hrany a čtyři pevné buňky.
Permutace bez pevných barev odporují hranám. Identita ponechává 16 typů
dílků, transpozice osm, v obou případech více než dostupných pevných buněk.
Osm typů pro `b ↔ c` je přesně knižních
`aaa, aad, abc, acb, bcd, bdc, dda, ddd`, modulo cyklické otočení dílku.

Dvě různé osy téhož typu by složením daly zakázanou rotaci o 120° nebo
240°. Osa každého typu je tedy jedinečná. Dvě osy různých typů mohou
koexistovat pouze jako kolmá dvojice, jejímž složením je půlobrat.

## Kanonické typy a násobnosti

Po volbě půlobratové permutace `(ad)(bc)` zbývá osm přejmenování barev,
která s ní komutují, a dvanáct prostorových symetrií. Grupa má 96 prvků.
Silné řešení má stabilizátor velikosti přesně dva: identitu a půlobrat
spojený s přejmenováním. Proto je jeho orbita velikosti 48 a
`68 024 064 / 48 = 1 417 168`.

Úplnost šesti knižních kanonických typů byla nově ověřena bez opakování
velkého výčtu. Prošli jsme všech **408** přípustných barevně označených
poloh jednobarevných dílků při půlobratu. U každé byly vyhodnoceny všechny
prostorové a barevné transformace, včetně všech možných barev hran
používaných k dodatečnému výběru. Vždy vyhovují přesně dvě transformace.
To dává jeden kanonický obraz silného řešení a dva obrazy slabého
nesilného. Kontrola je silnější, než vyžaduje úloha: tvrzení platí i pro
barvy vybírajících hran, které nelze rozšířit na platné skládání.

Analogický důkaz pro hornodolní reflexi prošel všech **168** přípustných
barevných poloh, čtyři prostorové transformace zachovávající osu a osm
barevných transformací. Opět vždy vyhovují dvě. Výjimku v násobnosti
zobrazení tvoří právě řešení, která jsou navíc silně půlobratová:
jejich stabilizátor má velikost dva, ostatní stabilizátor je triviální.

Levopravá reflexe dovoluje přesně **67** invariantních nesousedících
čtveřic jednobarevných buněk: 35 bez pevné buňky a 32 se dvěma pevnými
buňkami. Čtyři pevné buňky by vynutily sousedství odlišných jednobarevných
dílků. Žádná z 32 čtveřic druhé větve není invariantní při půlobratu.
Celá tato větev proto nemá žádné silné řešení; po normalizaci barev
má každá prostorová orbita přesně čtyři prvky.

Doklad: [symmetries129.py](symmetries129.py) a
[úplné konečné certifikáty](results/symmetries129/geometric-proofs.json).

## Všech pět původních obrázků

Z vektorů originálního PDF bylo přečteno všech **360 barevných výsečí**.
Každý obrázek obsahuje všech 24 různých typů právě jednou a shodu na
každé společné hraně. Kontrolovány byly všechny prostorové symetrie,
nikoli jen ta, kterou obrázek slibuje.

| Obrázek | Úplný výsledek kontroly |
|---|---|
| Str. 139 vlevo | Silný půlobrat s `a ↔ d, b ↔ c`; žádná další netriviální slabá symetrie. |
| Str. 139 vpravo | Slabá levopravá reflexe; žádná netriviální silná symetrie. |
| Str. 449 vlevo | Silný půlobrat a obě slabé reflexe; kanonické typy [1] a (5). |
| Str. 449 uprostřed | Silný půlobrat a obě slabé reflexe; typy [4] a (3). |
| Str. 449 vpravo | Silný půlobrat a obě slabé reflexe; typy [6] a (1). |

První obrázek skutečně dláždí rovinu bez otáčení. Překladová podmřížka
má bázi `(4,−2), (2,2)` a index 12. Hexagon zastupuje právě 24 různých
trojúhelníkových kosetů a 36 hranových kosetů. Šest dvojic ztotožněných
okrajových hran má shodné barvy. To je obecný důkaz dlažby celé roviny,
ne pouze kontrola několika přiložených hexagonů.

Doklad: [extraktor a validátor](extract_symmetry129_figures.py),
[všechna původní data](results/symmetries129/original-figures-checked.json).
Další obrázky na stejných stranách, patřící úlohám 130 a dále, tím nejsou
automaticky prověřeny.

## Počty a opravený celkový výsledek

Staré dokončené nativní výčty, jejich koncové protokoly a nezávislé
bitsetové počty byly znovu propojeny aritmetikou, bez nového hledání.

| Třída | Počet podstatně různých vzorů |
|---|---:|
| Silný půlobrat | 1 417 168 |
| Slabý, ale ne silný půlobrat | 609 203 |
| Slabá hornodolní reflexe, bez silné symetrie | 41 608 |
| Slabá levopravá reflexe, bez silné symetrie | **294 457** |
| Obě slabé osy, bez silné symetrie | 194 |

Současný výskyt libovolných dvou z půlobratu a obou reflexí implikuje
třetí. Každý párový průnik tří nesilných tříd je tedy totožný s jejich
trojitým průnikem o velikosti 194. Inkluze a exkluze dává dohromady

`1 417 168 + 609 203 + 41 608 + 294 457 − 2·194 = 2 362 048`.

To je odvozená odpověď na celkovou otázku v zadání; v knize tento
závěrečný součet není vytištěn. **Není to nový nález nad rámec F065.**

Všechny vytištěné rotační a hornodolní dílčí počty souhlasí, včetně
40 208 silných periodických a 261 silných se slabými osami. Ve větvi
se dvěma pevnými jednobarevnými dílky byly identifikovány také tři
geometrické skupiny, které dávají přesně knižních **46 975, 35 375,
25 261**, dohromady 107 611. Jejich 430 444 označených skládání se dělí
čtyřmi. Původní chyba F065 zůstává v druhé větvi: 186 846 místo 174 007,
tedy celkem 294 457 místo 281 618.

Šest konkrétních slabých voleb z textu má správné značky barevných
hranic. Náš starý generátor používá jiná čísla masek: prohazuje bity
0 a 1. Jde o bijektivní přejmenování značek, které nemění podmínku
rovnosti; všechny 64 trojice barev to potvrzují. Není to chyba knihy.
Doslovná párová volba `02 abc ... 31' bdc ...` rovněž souhlasí.

Doklad: [kontrola aritmetiky a voleb](check_symmetry129_counts.py),
[počty s odkazy na původní důkazy a hashi](results/symmetries129/counts-reconciled.json).

## Nové nezávislé výpočty

Starý úplný výčet 68 024 064 řešení používal zkrácené kódování se
36 primárními položkami a 21 barevnými hranovými položkami. Nový běh
doslovného párového kódování má 48 primárních položek, 42 hran a stejných
768 voleb. Dokončil **68 024 064 řešení** a všech 680 vypsaných vzorků
prošlo geometrickou kontrolou. Čistý náklad **453 526 853 015 memů**
se zaokrouhluje na knižních **0,5 Tμ**. Hrubý náklad je 532 164 598 063;
obě konvence jsou v protokolu rozlišené. Tím je dřívější benchmarková
mezera této úlohy uzavřena.
[Terminál a přijetí](results/symmetries129/literal-strong-rotation-checked.json).

32 případů se dvěma pevnými jednobarevnými dílky dosud mělo pouze
bitsetový výčet. Nová fronta původního DLX2 dokončila druhý nezávislý
výpočet zvlášť pro každý vstup. Všech 32 počtů souhlasí, v součtu
**430 444**. Všech **4 288 vypsaných vzorků** je geometricky validovaných;
nejsou vydávány za úplný archiv všech modelů. Starý bitsetový výčet
se neopakoval. [Přijetí všech případů](results/symmetries129/fixed-queue.json).

Při revizi podkladů se ukázalo, že šest hornodolních počtů, jejich
18 silných podvariant a tři počty průniku obou os měly také pouze
bitsetové terminály. Proto byla pro těchto 27 dosud nezávisle
neověřených vstupů spuštěna další nativní fronta. Malé silné případy
a průnik exportují každý model; u větších hornodolních případů se
geometricky kontroluje každý stý. [Spuštění](results/symmetries129/reflections-launch.json).
Všech **27 případů dokončilo** nativní výpočet se stejnými počty jako
bitsetový řešič. Geometricky prošlo všech **2 391 vypsaných modelů**:
261 ze silných případů, 832 vzorků obecných hornodolních případů a
všech **1 298 modelů průniku obou os**. Explicitní kanonizace poslední
množiny dala 261 orbit velikosti dva a 194 orbit velikosti čtyři.
Přijetí všech terminálů a tento úplný podíl jsou v
[záznamu fronty](results/symmetries129/reflections-queue.json).

Závěrečný [checkpoint](results/symmetries129/checkpoint-checked.json)
propojuje 60 nových nativních terminálů této úlohy a jeden nově dokončený
případ úlohy 127 s jejich zdroji, vstupy, výstupy a validacemi. Kontroluje
také zachování předchozích důkazů a uživatelových poznámek. Úspěšná
hledání se při přijetí neopakují.

## Errata a historický pramen

Prohledáno šest relevantních vrstev: úplná i krátká errata 4B a
publikovaného Fascicle 5 a oba autorovy TeXové zdroje. Čtyři aktuální
autorovy soubory byly ověřeny proti webu 2. listopadu v 08:06 UTC;
nová kontrola zachovává jejich shodné hashe a hledá i formulace a čísla,
nejen lokální stránku. Oprava F065 v těchto vrstvách nalezena nebyla.

**E065** zaznamenává známou opravu z 21. října 2021: ve Fascicle 5,
str. 256, řádku −5 se `13:a` mění na `−13:a`. Jde o hranovou podmínku
typu [6]. V našem 4B na str. 448 je už správné `−13:a`.
[Kontrola errat a kontexty](results/symmetries129/errata-check.json).

Autor připisuje objev kombinované silné a slabé symetrie Kate Jones
a odkazuje na příručku Multimatch III z roku 1991. Původní příručka
nebyla získána; přesný obsah, datum vydání této příručky a prvenství
proto zatím nejsou nezávisle doloženy.

Primární [produktová stránka vydavatele](https://www.gamepuzzles.com/edgemtch.htm)
potvrzuje sadu 24 různých čtyřbarevných trojúhelníků a přisuzuje nové
vzory barevných ploch vlastnímu výzkumu Kadonu.
[Retrospektiva roku 1989](https://www.gamepuzzles.com/1989notes.htm)
rozlišuje Philpottovy výsledky a následný výzkum vydavatele. Rok uvedení
produktu 1989 neodporuje vydání příručky v roce 1991.
[Profil Philpotta](https://www.gamepuzzles.com/wade.htm) potvrzuje původ
části výzkumu a odkazuje na archiv v Calgary. Žádný z těchto dokladů
nenahrazuje chybějící příručku ani nedokazuje konkrétní prvenství.

Přesný dotaz na Internet Archive nenašel žádný záznam. Zmínka na
BoardGameGeek slouží jen jako vodítko, nikoli jako primární potvrzení.
Kopie Knuthova textu opakují tentýž odkaz a nejsou nezávislou oporou.
[Archivované zdroje a záznam hledání](sources/symmetries129/history-search.json).
Nikomu nebyla poslána žádná zpráva.
