# Úloha 41(a–d), všech 32 středových vrcholů a tabulka 1

Zadání p117/file132, odpověď p167/file182 a tabulka 1 na p12/file27
byly zobrazeny v originální sazbě. Následující argument přebírá právě
úplnou místní klasifikaci T38-d a T39-a z
`trihedral-exercises-038-039.md`, nikoli nedostatečné podmínky odpovědi 40.
Používá skutečně obecný pohled: žádná incidentní stěna se nepromítá
na přímku a nepříslušný vzdálenější povrch neprochází přes obraz vrcholu.
Otázka postačitelnosti opravené odpovědi 40 zůstává samostatný C0005.

Aktuální přímé TeX erratum i krátká a kumulativní vrstva byly prohledány
podle p11–12,117,167, tabulky, oktantů a junctions. Obsahují opravy 39(b),
40 a 47(e), žádnou změnu úlohy 41 ani tabulky 1. Známé opravy 38–40
jsou již rozlišeny v předchozích rozborech a nejsou našimi nálezy.

## J41-a — všech 64 těles, bez vynechané sudé možnosti

U středového trojstěnného vrcholu vychází právě jedna hrana ve směru
každé ze tří souřadnicových os; kdyby dvě ležely na stejné ose, tři
incidentní roviny by nebyly nezávislé (T38-a). Je tedy osm voleb znamének
těchto tří paprsků. Při jedné pevné volbě dává T39-a právě osm obsazení:

{0}, {1,2,3}, {1,4,5}, {2,4,6} a jejich doplňky v {0,…,7}.

Záměna znamének os odpovídá operaci XOR s jedním číslem 0,…,7.
Žádné dvě z výsledných 8·8 možností nesplývají: z hran jejich hranice
znovu zjistíme znaménka tří vycházejících paprsků a pak konkrétní řádek
T39-a. Počty obsazených oktantů jsou pouze 1,3,5,7; žádný sudý počet
nemůže vytvořit požadovaný místní vrchol. Právě tím se odůvodňuje
tištěná věta o nemožnosti sudého počtu, nikoli pouhou zkouškou příkladů.

Ještě je třeba ověřit celé těleso: místní podmínka sama nestačí.
Jeden cubie je krychle. Tři tvoří L v jedné vrstvě, tedy kolmý hranol
nad jednoduchým L šestiúhelníkem; každý jeho vrchol má tři hrany.
Pět je plná vrstva 2×2 plus jediný cubie druhé vrstvy a sedm je krychle
2×2×2 s odstraněným rohovým cubie. Poslední dvě tělesa jsou platné
histoscapes s maticí výšek 2×2, v níž je právě jedna výška vyšší,
respektive nižší než ostatní tři. Jejich místní případy jsou již
dokázány v H27 (`histoscapes-and-exercise-027.md`); vnější rohy jsou
obyčejné rohy pravoúhlého hranolu. Nevzniká dotyk hranou ani vrcholem
dvou oddělených částí. Všechny uvedené místní možnosti se tedy skutečně
realizují globálními 3VP.

Samostatné počítání souhlasí: jeden cubie lze umístit osmi způsoby;
pro L zvolíme jednu ze šesti krajních vrstev a jeden ze čtyř vynechaných
čtverců, tedy 24. Každé L má právě jednu takovou vrstvu. Doplnění dává
24 případů s pěti a 8 se sedmi cubies. Celkem 8+24+24+8=64.
Místní tabulka T39-a také přímo dává 0,1,2,3 konkávních hran pro
1,3,5,7 cubies. Doplnění obrátí konvexitu všech tří hran a záměny
znamének ji zachovají. Tím je doložena i závorka v odpovědi (a).

## J41-b — přesně 32 viditelných středů

Přesuňme střed do počátku a očíslujme souřadnice tak, aby vektor směrem
ke kameře měl všechny složky záporné. Jeho paprsek od středu až po opuštění
boxu leží v oktantu 7. Žádný jiný cubie jej nemůže zakrýt; cubie 7 jej
naopak zakrývá, je-li obsazen. Obecná poloha vylučuje nulovou složku,
takže paprsek neleží na hranici dvou cubies. Přesně jeden člen každé
dvojice doplňkových obsazení má oktant 7 prázdný. Je tedy 64/2=32
viditelných středů, s počty 7,15,9,1 podle 1,3,5,7 obsazených cubies.

## J41-c1 — výpočet každé hrany a jejího označení

Bit osy je b∈{4,2,1}. U paprsku kladného či záporného směru osy jsou
čtyři přilehlé oktanty s pevným bitem 0 či b. Paprsek je skutečná hrana
právě tehdy, když je z nich obsazen jeden nebo tři; první možnost je
konvexní, druhá konkávní. Dva sousední obsazené oktanty znamenají
hladkou stěnu, žádná či všechna čtyři obsazení nejsou hranice. Dva
protilehlé obsazené oktanty se v dokázaných 64 případech nevyskytují.
Pro každý z nich vyjdou právě tři skutečné paprsky, jeden na každé ose.

Záporný paprsek je viditelný, protože jeho výhled leží v prázdném
oktantu 7. Od kladného paprsku výhled nejprve prochází oktantem 7 XOR b
a pak oktantem 7. Je tedy viditelný právě tehdy, když je prázdný i
oktant 7 XOR b. Toto je celý paprsek pohledu, nikoli jen test infinitesimální
viditelnosti bez kontroly vzdálenějšího zakrytí.

U viditelné hrany zjistíme incidentní čelní stěny takto. Pro druhou osu j
a pevné znaménko zbývající osy k existuje čelní stěna právě tehdy, když
je přilehlý oktant na kladné straně j obsazen a na záporné straně prázdný.
Její vnější normála je −e_j, tedy směřuje ke kameře. Jsou-li dvě,
hrana má již odvozené označení + nebo −. Je-li jedna, je to half edge.
Její šipka vede tak, aby viditelná stěna ležela vpravo: pro venkovní
paprsek E a vektor V do viditelné stěny platí v souřadnicích obrazovky
s osou y nahoru označení O (out), je-li det(E,V)<0, a I (in), je-li >0.
V je příslušný kladný nebo záporný průmět e_k. Determinant není nulový.

To jsou nezávislé geometrické podmínky, z nichž malý kontrolní program
`check_cubie_junctions.py` odvodí každý řádek. Negeneruje ani nehledá
velkou rodinu těles: zpracovává přesně dokázaných 64 místních obsazení.

## J41-c2 — původní kresby, všechny značky a tabulka 1

Z nativních vektorů `sources/file-182.svg` bylo identifikováno všech
32 černých středových kotoučků a všech 78 vycházejících silných hran.
Každá hrana má bezprostředně následující vlastní značku: červenou kolmou
čárku pro +, bílý výmaz části tahu pro −, nebo červenou šipku se třemi
body. Směr šipky určuje její hrot, nikoli odhad podle OCR. Celkem jde
o 21 plusů,21 minusů,18 šipek O a18 šipek I. Každý trojúdaj
(osa, znaménko paprsku, označení) byl jednotlivě porovnán s J41-c1;
všech 78 souhlasí. Výsledek a indexy cest jsou v
`results/cubie-junctions.json`.

Také všech 103 šedě vyplněných šestiúhelníků bylo jednotlivě přiřazeno
k průmětu konkrétního cubie. Jejich vrcholy odpovídají mřížce
{−1,0,1}³ a cyklické pořadí souhlasí s konvexním obalem osmi rohů.
Ve všech 32 kresbách jde přesně o uvedené obsazení, s jedinou výjimkou
nezakresleného cubie 0 u ¬7. Ten je zcela zakryt: každý jeho paprsek
ke kameře při opuštění cubie 0 vstoupí do obsazeného cubie 4,2 nebo1.
Tedy i tato výjimka je správná. Viz `check_cubie_silhouettes.py`
a `results/cubie-silhouettes.json`. Toto přiřazení neprohlašuje
samostatně za ověřené všechny tenké pomocné čáry průhledného vnějšího
boxu a ostatní úseky kresby mimo střed; ty netvoří tvrzený středový
vrchol ani tabulku označení. Tato užší dosud neuzavřená kontrola
zůstává v inventáři výslovně partial.

Při čtení vektorů se připouští pouze zaokrouhlení tiskových souřadnic.
Největší čtverec odchylky přiřazení bodu je 0.000014689586 bodu²,
zatímco nejmenší čtverec vzdálenosti různých mřížkových obrazů je
28.56233 bodu². Hrany různých os jsou odděleny velkým úhlem; tolerovaný
čtverec sinu odchylky směru je <10⁻⁶. Pro kolmost značky nebo její
souběžnost s hranou je mez 10⁻⁵. Tyto rezervy rozlišují jednoznačně
původní kresbu, nemění přesná geometrická kritéria J41-c1.

U V píšeme větve v pořadí l,r po směru hodinových ručiček přes menší
úhel. U W je pořadí l,m,r po směru hodinových ručiček v jeho úhlu <π.
U Y používáme cyklické pořadí po směru hodinových ručiček, začínáme
větví s nejmenším bitem osy. Vyjde přesně:

|Typ|Možné řetězce označení|Počet každého v kresbách|
|---|---|---|
|V|I+, IO, +O, O−, OI, −I|3|
|W|O+I, −+−, +−+|3|
|Y|IO−, O−I, −IO, −−−, +++|1|

Je tedy 18 V,9 W,5 Y a 2·18+3·9+3·5=78 viditelných větví.
Všech šest, tři a pět vzorů jednotlivě souhlasí s originální tabulkou 1,
včetně šipek a polohy jediné konkávní větve u prvních tří Y.
Kompletní přiřazení každé tištěné konfigurace je doplněno na konci.

Cyklická permutace x→y→z→x zachovává oktant kamery 7 a orientaci.
Permutuje tři osové bity a cyklicky větve; nemění typ ani označení.
V seznamu tvoří případy V a W trojice stejného vzoru a tři smíšené Y
cyklické varianty. Případy +++ a −−− jsou pevné. To dokládá také
tištěnou poznámku o ekvivalentním junction pattern po této rotaci.

## J41-c3 — proč krychličky pokrývají libovolný 3VP

Nechť U má jako sloupce tři nezávislé incidentní hranové vektory
libovolného vrcholu a q je směr ke kameře. Souřadnice λ=U⁻¹q nemají
nulu: nulová složka by znamenala, že se jedna incidentní stěna promítá
na přímku. Obrácením některých os převedeme λ do záporného oktantu;
všechny takové volby byly v J41-a zahrnuty. Kladným přeškálováním os
pak docílíme λ=(−1,−1,−1). Obsazení otevřených oktantů, konvexita
materiálového sektoru a viditelnost stěn se při těchto změnách nemění.

Průmět má v této bázi hodnost dva a jádro span(1,1,1). Dva lineární
průměty se stejným jádrem se liší invertibilní mapou obrazové roviny:
definujeme ji na obrazu jednoho průmětu pomocí druhého; shoda jader
zaručí jednoznačnost a hodnost dvě invertibilitu. Pozitivním
přeškálováním os lze stejné jádro zajistit i pravoúhlému cubie modelu.

Invertibilní rovinná mapa zachovává kolinearitu, existenci společné
otevřené poloroviny pro tři paprsky a cyklické pořadí až na obrácení.
Proto zachovává typy V,W,Y. Při kladném determinantu zachovává i
pravou stranu šipky. Při záporném obrátí pořadí větví a všechny šipky.
Odvozený seznam je pod touto operací uzavřen: u V se I+ a +O zamění,
O− a −I zamění, IO a OI zůstanou; každý W zůstane; u Y se permutují
tři cyklické varianty IO− a konstantní +++/−−− zůstanou.

Tím jsou všechny libovolné trojstěnné vrcholy převedeny na některý
z dokázaných případů, nikoli pouze na rodinu kolmých hran. A každý
uvedený vzor má realizaci některým skutečným cubie tělesem. Drobné
obecné pootočení odstraní nepodstatná náhodná promítací souběžnost,
aniž změní ostré místní nerovnosti. Seznam je tedy nutný i dosažitelný.

## J41-d — čtyři a pouze čtyři typy T

Umělý vrchol vzniká tam, kde vzdálenější hrana přechází pod obrysovou
hranou bližšího povrchu. Dvě kolineární větve T jsou části stejné
bližší half edge a mají shodně orientovanou šipku. Viditelný konec
vzdálenější hrany leží mimo bližší těleso, tedy vlevo od šipky;
bližší těleso je vpravo. V konvenci tabulky (příčka vodorovná, stonek
dolů) proto obě šipky příčky míří doleva, přesně jak uvádí odpověď.

Stonek může mít každé ze čtyř označení +,−,I,O. Pro dosažitelnost
vezmeme vnitřní bod viditelné hrany z již realizovaných cubie vzorů
s požadovaným označením a umístíme před něj oddělené malé těleso,
jehož obrysová hrana jej příčně překříží a zakryje jen jednu polovinu.
Lze použít vhodně pootočenou krychli: obrys má libovolný zvolený
obrazový směr a průběžným posunutím překryje požadovanou stranu.
Hloubku zvolíme striktně před původním tělesem, tedy bez prostorového
dotyku. V okolí vybraných vnitřních bodů je kladná vzdálenost k ostatním
hranám a vrcholům; dostatečně malá konstrukce je nezasáhne. Obě
orientace šipky stonku dostaneme volbou viditelné poloviny. Případné
ostatní náhodné souběžnosti odstraní obecné malé posunutí/pootočení.
Nesouvislé 3VP jsou dovoleny. Žádné další omezení na stonek tudíž
nevzniká a počet je přesně čtyři, nikoli 4³.

Tento argument předpokládá skutečně obecnou projekci, která vylučuje
současné trojí křížení nezávislých hran; nepoužívá chybnou implikaci
z pouhých dvou podmínek odpovědi 40.

## J41-table — všech 32 tištěných středových konfigurací

Znak ¬ znamená doplněk v {0,…,7}; I/O jsou šipky k/od středu.

|Tištěné obsazení|Typ|Pořadí označení|
|---|---|---|
|0|Y|+++|
|1|W|O+I|
|2|W|O+I|
|3|V|OI|
|4|W|O+I|
|5|V|OI|
|6|V|OI|
|¬7|Y|−−−|
|023|V|I+|
|102|W|+−+|
|231|V|IO|
|310|V|+O|
|¬467|V|−I|
|546|Y|O−I|
|¬675|W|−+−|
|¬754|V|O−|
|046|V|I+|
|¬157|V|−I|
|204|W|+−+|
|315|Y|−IO|
|462|V|IO|
|¬573|W|−+−|
|620|V|+O|
|¬731|V|O−|
|015|V|I+|
|154|V|IO|
|¬237|V|−I|
|¬376|W|−+−|
|401|W|+−+|
|540|V|+O|
|623|Y|IO−|
|¬762|V|O−|
