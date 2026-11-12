# Prostorové obrázky a úlohy35–37

Rozsah: p9–10/file24–25, zadání35–37 p116/file131, odpovědi p166/file181.
Originály byly zobrazeny. Podpůrný primární pramen je autorova poznámka
[Signed skeletons](https://www-cs-faculty.stanford.edu/~knuth/papers/signed-skeletons.pdf)
(24.4.2020, revize5.8.2026) a její odkaz na vlastní
[geometrická data](https://www-cs-faculty.stanford.edu/~knuth/js/DEK.js).
Stažené soubory a SHA256 jsou v příslušných `sources/*manifest.json`.
Nejde o převzetí správnosti programu: níže jsou nezávislé geometrické argumenty.

## G-1 — co skutečně obsahují vektory obrázku102

`sources/file-025.svg` vznikl přímo pomocí `pdftocairo -svg`. Černé tahy
obrázku102 jsou uzavřené lomené čáry, nikoli odhady hran z rastru.
`check_figure102_vectors.py` vypíše každý jejich vrchol a každou hranici.
Opakované souřadnice sdíleného konce se kvůli zaokrouhlení převodníku
liší nejvýše asi0.0056 bodu. Použitý slučovací poloměr je0.01 bodu;
nejmenší vzdálenost různých sloučených vrcholů je více než desetkrát
větší než největší slučovací odchylka. Všechny vzdálenosti se porovnávají
jako přesné racionální čtverce. Žádný průsečík nakreslených čar se
automaticky nepřidává jako vrchol.

Úplné seznamy v `results/figure102-vectors.json` dávají:

|Obrázek|Vrcholy|Hrany|Uzavřené polygonální hranice|
|---|---:|---:|---:|
|a|68|102|38|
|b|14|21|7|
|c|20|30|18|
|d|20|30|12|

Každá hrana je ve dvou polygonálních hranicích a každý vrchol má stupeň3.
To je úplná kontrola těchto konečných seznamů, nikoli samo o sobě důkaz
neprotínání ploch v prostoru. Pro b a d se geometrie přebírá z již
uzavřených důkazů26 a27, bez jejich opakovaného běhu.

Pro a,c je uložena také explicitní bijekce mezi vrcholy veřejného3D modelu
a původní kresbou. Čtyři známé korespondence určují afinní promítací
matici; nejbližší body identifikují ostatní vrcholy a přesná rovnost
všech množin hran následně ověří bijekci. U claspu souhlasí všech20
promítnutých souřadnic v toleranci kresby. U sfingy souhlasí64; zbývající
čtyři vrcholy47,51,62,66 se jednoznačně doplní podle již přiřazených
sousedů, ale jejich veřejné souřadnice se od obrázku liší. Neprohlašujeme
proto geometrický model sfingy za přesnou kopii knihy ani afinní fit
za důkaz přesné ortogonality kamery.

## G-2 — přesná geometrická certifikace pevných modelů

`check_polyhedra_fixed.py` kontroluje Clasp a C8A–D. Veřejná data jsou
zaokrouhlená pro vykreslování. Z nich jsou výslovně rekonstruovány
racionální realizace, s maximálním jmenovatelem22,40,14,10,22;
odchylka od každé zveřejněné souřadnice je menší než10^−5. Následující
argument pracuje výhradně s těmito přesnými racionálními souřadnicemi.
Samotná blízkost desetinných hodnot nedokazuje planárnost ani správnost.

Každý vykreslovací polygon má tři nebo čtyři vrcholy. U tří konkávních
čtyřúhelníků je vložena diagonála od jediného reflexního vrcholu k
protilehlému; oba vzniklé trojúhelníky mají stejnou orientaci. Každý
výsledný dílec je přesně rovinný a striktně konvexní. Pro trojúhelník
nebo čtyřúhelník to plyne z nenulové orientované plochy a stejného
znaménka všech lokálních otočení. Nejde o tento neplatný test pro
obecné hvězdicové mnohoúhelníky.

Každá hrana rozkladu má právě dva incidentní dílce s opačným průchodem.
Právě pomocné hrany chybějící v explicitním seznamu hran tělesa spojují
koplanární dílce. Spojité komponenty těchto dílců tvoří celé stěny;
jejich zbývající orientované hrany dávají všechny vnější i vnitřní cykly.
U každého takového vrcholu je jediný předchůdce a následník, takže
průchod končí právě v počátečním vrcholu a vypíše každý cyklus jednou.

Podstatná další kontrola prochází **každou dvojici dílců**. V různých
rovnoběžných rovinách je průnik prázdný. V jedné rovině se konvexní
polygony přesně ořežou postupně všemi uzavřenými polorovinami druhého
polygonu: na každé hraně se zachovají vnitřní konce a při změně znaménka
se přidá jediný racionálně interpolovaný průsečík. Indukcí podle počtu
polorovin vzniká přesný průnik. V nerovnoběžných rovinách leží průnik
na jejich společné přímce. Lineární rovnice druhé roviny má na každé
hraně nanejvýš jeden průsečík nebo je nulová na celé hraně; konvexita
pak dává celý interval mezi nejmenším a největším získaným parametrem.
Průnik dvou těchto intervalů je tedy úplný prostorový průnik.

Ve všech případech vyšel přesně společný vrchol, společná hrana rozkladu,
nebo prázdná množina podle incidence. Žádné vnitřky dílců se nepřekrývají
a nenastává nechtěný dotyk. Uzavřená orientovaná síť má kruhový link
každého vrcholu, neboť tam právě tři fyzické hrany oddělují tři rovinné
stěny; pomocné diagonály pouze dělí tyto sektory. Ohraničuje tedy
obyčejné polyhedrální těleso. Znaménko objemu jednotlivých uzavřených
komponent určuje vnější orientaci; zkontrolována je každá komponenta,
nikoli jen součet, který by mohl maskovat obrácenou orientaci jedné z nich.

Pro orientovanou hranu u na hranici stěny s vnější normálou n je n×u
směr do této stěny. Skalární součin druhé vnější normály m s n×u je
záporný na konvexní hraně a kladný na konkávní: lokální kolmý řez ukáže,
zda vnitřek první stěny míří dovnitř, nebo ven z druhé poloroviny.
Ve výpočtu se správně započítává znaménko celkové orientace cyklů.
Žádný testovaný součin není nulový.

## G-3 — clasp včetně provlečení

Prvních deset vrcholů tvoří jednu součást, druhá vzniká půlobratem
(x,y,z)↦(−x,y,−z); všechny souřadnice i hrany této shody jsou ověřeny.
V první součásti jsou0,1,2,3 vrcholy vnějšího tetraedru. Stěny012 a023
mají trojúhelníkové otvory456 a798. Zbývající dvě vnější trojúhelníkové
stěny jsou013 a123, vnitřní tunel má čtyřúhelníky4785,5896,4697.
Každý otvor je vnitřní, což plyne i z přesného rozkladu jeho okolí
na tři neprotínající se koplanární dílce. Stěn je proto7, jejich
hraničních polygonů9, vrcholů10 a hran15; tři vnitřní podélné hrany
47,58,69 jsou konkávní. Dvě součásti dávají20/30/14 a18 hraničních
polygonů. Právě rozlišení stěn od hraničních polygonů vysvětluje18
cyklů v původním drátovém obrázku. Všechny cykly souhlasí jednotlivě.

Párová kontrola dílců navíc dokazuje, že povrchy obou součástí jsou
disjunktní. Žádná není uvnitř druhé: například vrcholy opačných krajů
ležící mimo její vnější tetraedr to vylučují. Obě odpovídající omezená
tělesa jsou tedy disjunktní. Provlečení má samostatný přesný důkaz.
Uzavřený hranový trojúhelník10–11–12 protíná rovinu trojúhelníku012
ve dvou bodech. Bod(21/22,9/22,21/22) je vně trojúhelníku012, kdežto
(−9/22,9/22,−9/22) je striktně uvnitř. Žádný průsečík neleží na jeho
hranici a oba jsou příčné. Druhá smyčka tedy protíná napínací disk
první smyčky právě jednou: jejich linking number má absolutní hodnotu1.
Při rozpojení disjunktních součástí by musel být0, což by vyžadovalo
průchod jedné smyčky druhou. Jde tedy skutečně o dva provlečené objekty.

## G-4 — sfinga: uzavřené počty kresby, otevřená realizace

Přesný seznam vektorů knihy má68 vrcholů,102 hran a38 polygonálních
hranic. Hranový graf má komponenty o38 a30 vrcholech, tedy tělo a hlavu.
Není správné zamítnout čísla pouhým V−E+F: dvě povrchové komponenty
mohou dát4 a stěny s dírami navíc mění příspěvek F.

Veřejný model pokládá obdélníkové dno hlavy38–53–64–49 do z=−.07,
na vnitřek horní stěny těla31–33–37–36–32–30. Jeho doslovné sjednocení
by mělo horní stěnu s otvorem a nemělo by vnitřní dno hlavy. Ale veřejný
model ve čtyřech jiných souřadnicích neodpovídá původní kresbě a kresba
nemůže vyloučit velmi malou mezeru mezi částmi. Tento dotyk proto
**není důkaz chyby knihy**. Zůstává partial přesná prostorová realizace,
počet skutečných stěn a původní záměr dotyku/oddělení částí. Nová karta
se nevytváří. Ověřeny jsou samostatně všechny počty hranic kresby.

## G-5 — obě creases v odpovědi35

Kostra je kubická přímo z požadavku tří hran v každém vrcholu; hrana
spojuje dva různé vrcholy a nemá další vrchol ve vnitřku.

V tetraedru ABCD zvolme P uvnitř AB a Q uvnitř AC. Přehneme část APQ
kolem PQ tím, že posuneme A na přímce AD a rovinu APQ necháme procházet
pevnou PQ. Plochy ABD a ACD zůstávají ve svých rovinách. Pro dostatečně
malý nenulový posun jsou stále jednoduché a nepřibudou průniky;
nenulové úhly a kladné vzdálenosti neincidentních kompaktních částí
mají rezervu, a u P,Q vznikají skutečné trihedrální vrcholy.
Výsledné stěny jsou trojúhelníky A′PQ,BCD a čtyřúhelníky PBCQ,
A′PBD,A′DCQ: šest vrcholů, devět hran, pět stěn. Pohyb dovnitř vytvoří
jedinou konkávní hranu PQ; pohyb ven ji vytvoří konvexní a žádnou
jinou konkávní hranu nepřidá. Tím je doložen první tištěný mezikrok.

Nyní přehneme právě čtyřúhelník PBCQ: R leží uvnitř PQ, S uvnitř BC.
Otočíme polovinu RPBS kolem RS. P se posune na průsečnici zbývajících
dvou incidentních rovin A′P, B na jejich průsečnici BD. Všechny sousední
stěny tak zůstanou rovinné. Oba dosavadní trojúhelníky získají R nebo S
a stanou se čtyřúhelníky; přehnutá stěna se rozdělí na dva čtyřúhelníky.
Celkem vzniká8 vrcholů,12 hran, šest čtyřúhelníků a kostra krychle.
Malá změna zachová všechny staré ostré úhly. Hrana PQ se však rozdělí
na **dvě** hrany, takže byla-li konkávní, přispívá nyní dvěma.
Volba konvexního/konkávního RS proto dává0,1,2,3 konkávní hrany,
nikoli omylem0,1,1,2. To je podstatný pomocný krok odpovědi.

Jako úplné pevné realizace slouží certifikované C8A–D. V každé je hrana
mezi čísly0..7 právě tehdy, když jejich XOR je1,2 nebo4; to je explicitní
izomorfismus s3-krychlí. Všechny mají osm vrcholů, dvanáct hran a šest
jednoduchých čtyřúhelníkových stěn. Konkávní množiny jsou postupně
∅, {57}, {37,67}, {37,57,67}. Čtyři podepsané grafy přímo v zadání36
mají zleva3,1,2,0 takových hran a odpovídají těmto čtyřem signaturám:
dvě či tři přerušované hrany mají společný vrchol, u jedné je poloha
irelevantní díky symetrii krychle. Žádný obecný census realizací se tím
netvrdí.

## G-6 — podepsaný Szilassiho graf a každý tah obrázku36

Geometrie všech sedmi stěn byla uzavřena v důkazu26. Použijeme přesné
souřadnice a konzistentní orientace z jeho uloženého certifikátu, ne
nový geometrický běh. Z výše odvozeného skalárního testu vycházejí
právě konkávní hrany

023–310, 054–460, 134–421, 134–643, 356–643.

`check_szilassi_signature.py` zkontroloval všech21 hran. Dále načetl
všechny plné i přerušované úsečky původního diagramu36 z file181.svg.
Explicitní bijekce uložená v `results/szilassi-signature.json` zachovává
všech21 adjacencí i jejich znaménka. Malé hledání této jediné bijekce
navštívilo22 uzlů; nešlo o hledání realizace nebo velký výčet.

## G-7 — Heawood, odkaz7–(57) a všech336 automorfismů

Označme P_i cyklické trojice023,134,245,356,460,501,612 a L_j trojice
054,165,206,310,421,532,643, oboje v pořadí0..6. Přímý úplný seznam
hran je P_i–L_j právě při j−i∈{2,3,5} modulo7. Body P_i lze označit
vektory F₂³ v pořadí001,010,100,101,111,011,110. Pro každé L_j je
jediný nenulový normálový vektor kolmý na jeho tři body; všech sedm
normálových vektorů je různých. Dostáváme přesně incidenci p·ℓ=0.
To je původní graf a matice7–(57), skutečně zobrazené na4Ap33/file50
v `images/vol4a-p033.png`, nikoli pouze podobný název grafu.

Graf je souvislý: libovolné dva různé body mají jedinou společnou
přímku a každá přímka obsahuje body. Bipartice je proto určena až na
záměnu. Automorfismus zachovávající obě třídy musí zobrazit tři
nekolineární body na tři nekolineární body, tedy uspořádanou bázi.
Ty mají7·6·4=168 možností. Všechny ostatní body jsou jednoznačně
určeny jako třetí body přímek přes již určené dvojice, což je součet
vektorů; proto není žádná další volnost. Naopak každá invertibilní
lineární transformace A dává automorfismus p↦Ap, ℓ↦A^(−T)ℓ.
Je tedy přesně168 automorfismů zachovávajících bipartici. Záměna bodu
a normálového vektoru je dualita, protože skalární součin je symetrický.
Jejím složením vznikne právě dalších168 a celkem336. Tento důkaz
nepoužívá enumeraci automorfismů ani nedoložený známý počet.

## G-8 — půlobrat, hlavní p10 a přesné zbylé meze

Záměna rovin0↦0,1↔6,2↔5,3↔4 v souřadnicích26 je přesně
(x,y,z)↦(−x,−y,z). Každý ze14 vrcholů a každý cyklus stěny se
převede na příslušný jiný vrchol/cyklus; to je uloženo zvlášť v
certifikátu signatury. Celé Szilassiho těleso má tedy skutečný půlobrat,
vodorovná stěna0 je pevná jako množina a ostatních šest stěn se páruje.
Proto má po tomto otočení stejný obraz z každé pevné kamery. Důkaz
samotné symetrie není tvrzením, že byly ověřeny všechny viditelné
úseky, zakrytí a polohy kamer všech obrázků101–104; ty ještě pokračují.

Na p10 je lokální klasifikace hran správná. V kolmém řezu vnitřním
bodem hrany jsou dvě stěny dva paprsky a těleso zabírá jeden ze dvou
úhlových sektorů. Malý sektor je uvnitř u konvexní hrany, vně u
konkávní. Je-li konkávní hrana viditelná z vnější kamery, kamera musí
být v jejím malém vnějším sektoru a místně vidí oba incidentní paprsky,
tedy obě stěny. Nemůže být half edge. Je-li při obecné poloze kamery
vidět právě jedna incidentní stěna, je hrana tudíž konvexní. Vzdálené
zakrytí neodstraní tento místní argument na vnitřním viditelném úseku:
jiné kompaktní části mají kladnou rezervu; konce zakrytých úseků jsou
zvláštní projektované křižovatky, probírané dále.

Šipka má viditelnou stěnu vpravo definicí. Na vnější hranici promítnuté
oblasti je právě na této straně objekt a na druhé pozadí, takže všechny
takové hrany jsou half edges. Průchod s vnitřkem vpravo je po směru
hodin; u vnitřní díry by orientace byla opačná. Tvrzení se týká vnější
hranice, nikoli všech cyklů v obrázku. Jednotlivé značky104 se ještě
kontrolují zvlášť, nejsou tímto obecným argumentem automaticky uzavřeny.

Úloha37 zůstává otevřenou výzkumnou otázkou. Aktuální primární poznámka
opakuje otázku rozhodnutelnosti; neposkytuje takový algoritmus. Její
revize i erratum23.10.2026 zvyšují počet známých signatur příslušného
osmivrcholového grafu13→14 a krychle4→6. Nejde o naše chyby. Čtyři
realizace krychle jsou prokázány výše; navazující vlastní certifikát
v `known-signed-witnesses-exercise-037.md` již doplnil i zbývající dvě
a všech14 dalších pevných realizací, včetně úplného rozlišení signatur. Totéž platí pro tvrzení „jediná známá“ signatura Heawoodova
grafu: shoda s aktuálním primárním pramenem není důkaz úplnosti poznání.
Heawoodova historická priorita a publikace1890 jsou výslovně přeskočeny.

Všechny výpočty zde byly krátké a nice15. První geometrický pokus
odhalil nutnost rozdělit tři konkávní vykreslovací čtyřúhelníky;
teprve opravený přesný rozklad dal úplný certifikát. Neúspěšný afinní
fit sfingy byl uložen jako rozdíl zdrojů, ne jako neexistence geometrie.
