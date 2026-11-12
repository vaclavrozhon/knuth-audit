# Szilassi104(b), původní101(b–d) a opakovaný103(b)

Původní stránky p9–11/file24–26 byly zobrazeny. Nové kontroly níže
přebírají uzavřenou prostorovou geometrii, nikoli její důkaz opakují.
Metoda úplného porovnání viditelných intervalů je CP-1–CP-5 v
`clasp-projection-fig104c.md`; zde jsou doloženy konkrétní nové
vstupy a výsledky pro každý uvedený obrázek.

## SP-1 — celý pohled104(b)

Všechny14 souřadnice,7 jednoduchých rovinných šestiúhelníků a21 hran
pocházejí přímo z dokázané úlohy26 (`results/szilassi-exact.json`).
Konzistentní orientace tam má záporný objem, proto se všechny cykly
obrátí, aby normály mířily ven. Každý šestiúhelník se trianguluje
platnými ušima s kontrolou jednoduchosti, rovinnosti, diagonál
a vnitřků uší; výsledné28 trojúhelníků pokrývají právě sedm stěn.
Znaménka konvexity21 hran se přebírají ze samostatně uzavřené úlohy36.

Původní vodorovný cyklus102(b), SVG path62, identifikuje vrcholy
023,206,460,054,501,310 postupně s indexy7,6,13,12,4,3 úplného
vektorového seznamu. Z každého již přiřazeného vrcholu, který má
právě jednoho nepřiřazeného souseda na obou stranách, následuje
vynucené další přiřazení. Takto se bez hledání doplní všech14.
Následně se nezávisle porovnají úplné množiny všech21 hran a všech7
neorientovaných cyklických hranic stěn. Obě přesně souhlasí.

Přes tuto bijekci je identifikován každý konec černé cesty a každý
vrchol bílé výplně104(b). Čtyři nekoplanární reference023,206,054,532
určují promítací mapu; největší čtverec odchylky původního výskytu
vrcholu je2472517050433/30625000000000000 <0.000081 bodu².
Znaménko směru pohledu určí viditelná vodorovná stěna0.

Všech21 hran je rozděleno všemi projektovanými průsečíky. Přesné
testy paprsku s každým z28 dílců určují úplnou viditelnost, a každá
výsledná množina intervalů se rovná všem přeživším černým tahům
původního SVG po pozdějších bílých výplních. Nejde pouze o kontrolu
souřadnic či několika vybraných vrcholů.

Obrázek má15 junctions=5 V+5 W+2 Y+3 T a20 čar. Skryté jsou
skutečné vrcholy356 a643, ostatních12 je vidět. Kontrolní součet
stupňů2·5+3·5+3·2+3·3=40=2·20 souhlasí. Výsledek je v
`results/szilassi-projection.json`; vlastní výpočet
`check_szilassi_projection.py` trval s nice15 pod sekundu.

## SP-2 — všechny zobrazené značky

Čelnost určuje vnější normála proti směru pohledu; znaménka hran
jsou již uzavřena. Při jediné čelní stěně určí směr šipky projekce
vnitřního vektoru n×u; u dvou čelních stěn je značka + či −.
Každá původní kolmice, podélný bílý výmaz a trojbodová šipka je
geometricky přiřazena jedné hraně. Pozdější bílé výplně zcela skryjí
značky201,202; ty se nezapočítají jako viditelné. Všech26 zbývajících
značek souhlasí. Krátký viditelný konec hrany460–643 nemá přeživší
značku a není v součtu26 vydáván za ověřenou vyznačenou hranu.
Evidence `results/szilassi-labels.json` vznikla příkazem
`check_clasp_labels.py szilassi`, který hotovou viditelnost přebírá.

## SP-3 — přesná věta o půlobratu

Čelní a skutečně aspoň zčásti viditelné jsou původní stěny0,1,2,4.
Uzavřený souřadnicový půlobrat R(x,y,z)=(−x,−y,z) z úlohy36
převádí celý Szilassiho polyedr na sebe a permutuje stěny
0→0,1↔6,2↔5,3↔4. Po fyzickém otočení tudíž obraz obsahuje
tentýž geometrický povrch, ale vidíme původní stěny0,6,5,3.
Stěna0 má půlobratovou symetrii a je znovu vidět; zbývající tři
nebyly v předchozím pohledu čelní. Tím je dokázána každá část
závorky v popisku103, nejen tvrzení o abstraktní symetrii grafu.

## SP-4 — každý původní tah101(b–d) a103(b)

Bez nové prostorové simulace se porovnají další skutečné kresby:

|Obrázek|Původní SVG a cesty (včetně první, bez poslední)|Přebíraný úplný prostorový pohled|
|---|---|---|
|101(b)|file024,84–92|Szilassi104(b)|
|101(c)|file024,92–110|Clasp104(c), pouze geometrie|
|101(d)|file024,110–126|Histoscape104(d)|
|103(b)|file025,123–131|Szilassi104(b), se symetrií SP-3|

Každý konec každého původního černého tahu a každý vrchol bílé
výplně se jednoznačně přiřadí vrcholu již uzavřeného pohledu.
Tři nekolineární reference určují invertibilní mapu obrazové roviny
s kladným determinantem. Všechny další výskyty souhlasí v tiskové
přesnosti: čtverec odchylky je <0.0004 bodu², tj. vzdálenost<0.02 bodu.
Tato mez zahrnuje zaokrouhlení obou nezávislých tiskových kopií
i již zdokumentovanou odchylku výchozího přesného modelu.
Druhý nejbližší kandidát při přiřazení má čtverec vzdálenosti>0.1,
takže bijekce není citlivá na tuto rezervu.

Samotná shoda koncových bodů nestačí. U každé kresby se proto znovu
zpracuje její vlastní pořadí všech bílých výplní a černých cest,
vymažou se právě překryté intervaly a zkontroluje se každý zbývající
úsek. Výsledky se u každé fyzické hrany přesně rovnají dříve
uzavřeným intervalům. Všechny čtyři původní kresby tedy mají správný
obrys a skryté části; zároveň jsou HC obrázky s již doloženými
typy a stupni junctions. Jde o úplné porovnání, ne vzorek tahů.
Evidence je `results/repeated-views.json`, program
`check_repeated_views.py`; staré prostorové výpočty nebyly spuštěny.

Zde není uzavřena sfinga101–104(a), jejíž veřejná geometrie se na
čtyřech vrcholech liší, ani zpětný clasp103(c). U něj prostá
identifikace půlobratu kolem souřadnicové osy veřejného modelu
neodpovídá kresbě: veřejná soustava má jiné osy symetrie než
zvolená svislá osa scény. To není důkaz chyby knihy. Tyto pohledy
zůstávají přesně vymezenými partial a neblokují samostatný přepis(20).
