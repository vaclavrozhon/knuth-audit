# Úloha37: všech14 a6 známých signatur jako pevné svědky

Tento dodatek uzavírá dvě konečná existenční tvrzení z opravené odpovědi37
na p166/file181. **Neřeší** otevřenou rozhodovací otázku ani úplnost
všech možných realizací. Primární poznámka a modely jsou uloženy se SHA256
v `sources/signed-skeletons-manifest.json` a `polyhedra-primary-manifest.json`.

## K37-1 — konečná geometrie všech šestnácti nových svědků

Předchozí čtyři krychle C8A–D se přebírají bez dalšího geometrického běhu.
`check_known_signed_witnesses.py` přidává pouze14 konkrétních C4 modelů
a C8E,F. Každý úspěšný model hned uloží a při pokračování ho nepřepočítává.
Výsledkem je `results/known-signed-witnesses.json`. Všechny mají přesně
8 vrcholů,12 fyzických hran, šest stěn, každou s jedinou jednoduchou
polygonální hranicí. Všechny dvojice plošných dílců jsou ověřeny přesnými
racionálními průniky podle již dokázaného G-2 v poznámce35–37.

Nové pětiúhelníkové i konkávní stěny potřebují doplnit rozklad G-2.
Nejprve se ověří rovinnost a disjunktnost všech neincidentních stran
polygonu přesnými orientacemi; tím je doložena jednoduchost. Zvolený
ušní trojúhelník má správnou konvexní orientaci, neobsahuje žádný jiný
vrchol ani na hranici a jeho diagonála neprotíná žádnou neincidentní
stranu. Leží tedy uvnitř jednoduchého polygonu a jeho odstranění dá
menší jednoduchý polygon. U každého konkrétního polygonu je uložena
konečná posloupnost takových kroků až do trojúhelníku, plus rovnost
součtu orientovaných ploch. Není potřeba spoléhat na to, že obecné
hledání ucha vždy uspěje: certifikován je každý skutečně zvolený krok.
Párová kontrola všech výsledných trojúhelníků znovu vyloučí překryvy
a nechtěné dotyky. Počet vrcholů se každým krokem zmenší o1, takže
tento konkrétní rozklad má konečný počet kroků.

Zdroj C4B41 má jeden vykreslovací čtyřúhelník s opačným průchodem;
geometrie polygonu tím není změněna. Orientace trojúhelníků se proto
nejprve sjednotí přes sdílené hrany: sousední průchody po stejné hraně
musí být opačné. Na všech hranách se kontrolují konzistentní znaménka,
a poté se podle objemu určí vnější orientace. Obrácené dílce4,5 jsou
výslovně zaznamenány. Nejde o změnu staženého souboru ani o knižní nález.

Přesné zlomky v novějších modelech se pouze parsují jako data. Stažený
JavaScript se nevyhodnocuje. Starší zaokrouhlené modely mají výslovně
uloženou racionální rekonstrukci a skutečnou odchylku; všechny vlastnosti
se dokazují až pro tyto přesné souřadnice.

## K37-2 — neplanární veřejný C8E a samostatný platný svědek

Veřejný C8E **nelze beze změny převzít** jako důkaz. Jeho uvedený
vrchol7 je(−957/1820,252/2197,−1/169). Skalární trojsoučiny
pro stěny[1,5,7,3] a[5,4,6,7] jsou postupně

−243/123032 a −1458/1830101.

Oba jsou nenulové, takže tyto čtyřúhelníky nejsou rovinné. Jde o
přesný rozpor uvnitř veřejného doprovodného modelu, nikoli o důkaz
nepravdivosti počtu šesti realizací v knize. Stažený zdroj se nemění.
Příslušné původní souřadnice, determinanty a hash jsou samostatně
uloženy v `results/companion-C8E-nonplanarity.json`; nevzniká z toho
automaticky karta chyby knihy.

Pro vlastní důkaz existence použijeme všech sedm ostatních vrcholů
beze změny a **výslovně nově definujeme** vrchol7 jako průsečík rovin
určených trojicemi(1,5,3),(2,3,6),(5,4,6). Přesná nesingulární
lineární soustava má řešení

(−2066409123/3934112140, 3052179/28100801, −371726/28100801).

Nový vrchol tedy není převzatá tištěná nebo zveřejněná hodnota.
Všechny roviny, pravé strany, původní i nové souřadnice jsou v
certifikátu. Následuje celá kontrola všech stěn, hran a prostorových
průniků, nikoli pouze kontrola tří rovnic. Ta pro tuto samostatnou
racionální realizaci uspěla a dala požadovanou pátou signaturu.
C8F je kontrolován přímo z přesných zveřejněných zlomků, bez úprav.

## K37-3 — všech14 signatur jsou různé

Označení kanonického grafu je explicitně určeno hranami v certifikátu
C4A1. Má právě dva trojúhelníky012 a567. Jediná hrana přímo mezi
těmito trojúhelníky je05. Zbývající vrcholy3,4 jsou spojeny hranou34;
jejich další sousedé jsou1,6 a2,7. To je přesně malý graf v původní
odpovědi37:0=levý dolní,1=levý horní,2=levý vnitřní,3=střední horní,
4=střední dolní,5=pravý dolní,6=pravý horní,7=pravý vnitřní vrchol.
Všech12 čar originálu odpovídá tomuto seznamu jednotlivě.

Automorfismus musí zachovat nebo zaměnit oba trojúhelníky a jejich
jediný spoj05. Po této volbě má ještě dvě možnosti pro obrazy1,2;
všechny ostatní vrcholy jsou potom vynuceny sousedností. Jsou tedy
nejvýše čtyři automorfismy. Všechny čtyři skutečně existují a jsou
generovány permutacemi

(1 2)(3 4)(6 7),  (0 5)(1 6)(2 7).

Každý ze14 zdrojových grafů má uložený konkrétní izomorfismus na tento
graf; žádný nalezený izomorfismus není důkazem různosti signatur sám.
Po aplikaci **všech čtyř** automorfismů se vezme lexikograficky nejmenší
množina konkávních hran. Úplné výsledky jsou:

|Model|Kanonická množina konkávních hran|
|---|---|
|C4A1|∅|
|C4A2|12|
|C4B11|34|
|C4B12|12,34|
|C4B13|01,34|
|C4B21|01,12,13|
|C4B22|12,13|
|C4B23|01,13|
|C4B32|12,67|
|C4B41|01|
|C4B42|01,67|
|C4B51|01,57|
|C4B52|01,56|
|C4C1|01,05,57|

Všechny výsledky jsou různé. Jelikož byly vyčerpány právě všechny
automorfismy základního grafu, jde o14 neizomorfních podepsaných
grafů, každý s úplnou vlastní realizací. Tím je doložena dolní mez14,
nikoli horní mez nebo úplnost autorova katalogu.

## K37-4 — všech šest krychlových signatur je různých

Krychlové vrcholy jsou bity0..7 a hrany mají XOR1,2,4. Každý
automorfismus může nejprve zvolit obraz0 osmi způsoby. Jeho tři
sousedy lze potom permutovat šesti způsoby. Zbylé vrcholy jsou určeny:
vrchol ve vzdálenosti2 je jediný další společný soused příslušné
dvojice sousedů0 a vrchol ve vzdálenosti3 je jediný takový vrchol.
Existuje tedy nejvýše48 automorfismů a všechny jsou realizovány
permutací bitů následovanou XOR s pevnou trojicí bitů. Toto dává
úplný seznam, nikoli pouze podgrupu vybraných symetrií obrázku.

Minimum přes těchto48 automorfismů dává postupně

|Model|Kanonická množina konkávních hran|
|---|---|
|C8A|∅|
|C8B|01|
|C8C|01,02|
|C8D|01,02,04|
|C8E, vlastní přesná realizace K37-2|01,26|
|C8F|01,02,15|

Tyto množiny jsou různé, takže máme šest neizomorfních realizovatelných
signatur. Znovu jde pouze o dolní mez6. Úplné transformace i minima
jsou v `results/known-signed-signatures.json`. Nekontrolovala se
žádná velká množina kandidátních těles: šlo o16 dodaných pevných
modelů a čtyři, respektive48 transformací konečných seznamů hran.
