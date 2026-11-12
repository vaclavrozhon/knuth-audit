# Obrázek 104(c): všechny viditelné úseky a patnáct vrcholů T

Originál p11/file26 a zvětšený výřez
`images/file-026-clasp-cropbox.png` byly zobrazeny. Souřadnice SVG
jsou vůči CropBox, nikoli MediaBox; při vykreslení výřezu je nutný
přepínač `pdftoppm -cropbox`. Tím se vysvětluje nepoužitelný první
výřez `file-026-clasp.png`, který zachytil záhlaví a není důkazem.

## CP-1 — přesné vstupy a identifikace původní kresby

Přebírá se již uzavřený prostorový model Clasp z
`results/polyhedra-fixed.json`: 20 racionálních vrcholů,30 fyzických
hran,14 stěn rozdělených na22 konvexních dílců,18 hraničních cyklů.
Jeho vložení, orientace a všechny párové průniky se znovu nepočítají.
Úplná původní transparentní kresba102(c) má uloženou bijekci těchto
vrcholů a všech30 hran v `results/figure102-vectors.json`.

Všechny konce černých cest a bílé vyplňovací polygony104(c) byly
jednotlivě identifikovány přes tuto bijekci. Obsahují19 z20 vrcholů;
vrchol16 se nevyskytuje, protože je zcela skryt. Čtyři nekoplanární
vnější rohy0,1,2,3 určují afinní mapu do roviny. S touto jedinou mapou
souhlasí všechny výskyty všech19 promítnutých vrcholů; největší
čtverec odchylky je

59578750729 / 3136000000000000 < 0.000019 bodu².

Jde o identifikaci geometrie po zaokrouhlení tiskových souřadnic,
nikoli o prohlášení přibližné rovnosti dvou metrik za přesnou.
Lineární část mapy má hodnost dva; její jádro určuje směr q.
Mapa se liší od ortografické projekce podél q pouze invertibilní
změnou souřadnic obrazové roviny. Ta nemění viditelnost podél q,
křížení, pořadí bodů ani typy junctions. Znaménko q je určeno
viditelnou vnější stěnou012. Opačný směr by změnil viditelnost
22 z30 hran, takže není alternativním vysvětlením téže kresby.

## CP-2 — nezávislá prostorová viditelnost

Každá fyzická hrana se parametrizuje p(t)=(1−t)a+tb,0≤t≤1.
Rozdělíme ji všemi průsečíky její projekce s projekcemi ostatních
fyzických hran. Deteminant dvou rovinných směrů dává přesně oba
parametry průsečíku; rovnoběžné nebo kolineární dvojice se zpracují
zvlášť. Jsou to konečné racionální výpočty na pevných30 hranách.

Na otevřeném dílčím intervalu stačí jeden vnitřní bod: viditelnost se
nemůže změnit mimo obraz hranice stěny nebo prostorový průnik,
jak bylo dokázáno v HC-3. Pro bod p a každý konvexní dílec v rovině
n·x=d spočítáme t=(d−n·p)/(n·q). Všechny jmenovatele jsou nenulové.
Je-li t>0 a bod p+tq splňuje všechny uzavřené hranové poloroviny
dílce, zakrývá jej povrch. Body s t=0 jsou incidentní povrch a
nezastíní samy sebe. Obsahuje-li průsečík hranici mezi pomocnými
dílci, uzavřené testy ji započtou a nezanechají mezeru. Protože dílce
pokrývají celé ověřené stěny, test je úplný, včetně vnitřků tunelů.

Sousední viditelné intervaly se sjednotí. Všechny výsledné intervaly
každé z30 hran jsou uloženy, nikoli jen součet viditelných vrcholů.
Program nic nehledá a neopakuje prostorovou certifikaci modelu.

## CP-3 — samostatná kontrola každé původní černé cesty

Ze SVG se převezme skutečné pořadí černých cest a bílých výplní.
Každý původní tah se rozdělí průsečíky s hranicemi všech pozdějších
bílých výplní. Na každém otevřeném intervalu se rozhodne, zda leží
uvnitř některé pozdější výplně; použije se přesný winding-number
test, který odpovídá uvedenému `fill-rule=nonzero`. Funguje i pro
stěnu s otvorem a pro pomocný zpětný spojovací tah. Tahy Z se uzavřou,
samostatné M jen zahajují nový tah. Nezamění se mezera vytvořená
bílou značkou konkávnosti za skutečně skrytou část hrany.

Každý zbylý černý interval leží na právě jedné skutečné fyzické hraně.
Jeho parametry se převedou na její parametrizaci z CP-2. Sjednocení
všech takto získaných intervalů se u **každé** fyzické hrany přesně
rovná nezávislému prostorovému výsledku CP-2. Dva pomocné nehranové
spoje ve vykreslovacích polygonech jsou celé vymazány pozdějšími
výplněmi, takže v konečné kresbě netvoří falešnou hranu.

Tím je ověřena jak úplnost kresby, tak absence nesprávně viditelných
částí. Samotný počet, bodová ukázka nebo přebrané vykreslovací pořadí
by tuto shodu nenahradily. Výsledek je v `results/clasp-projection.json`
a krátký výpočet v `check_clasp_projection.py` (nice15, pod sekundu).

## CP-4 — všechny junctions a deklarovaný počet15

Vložíme všechny konce elementárních viditelných úseků a jejich incidenci.
Umělé řezy, které mají pouze dvě kolineární větve, odstraníme sloučením
sousedních úseků téže fyzické hrany. Dva nekolineární paprsky jsou V;
u tří přítomnost protilehlé dvojice určí T. Jinak znamená kladná
lineární závislost tří paprsků Y a její absence W: koeficienty závislosti
jsou jejich tři cyklické determinanty. Tento test je přesný.

Výsledek má27 junctions a37 čar:

* 7 V;
* 5 W;
* 15 T;
* žádné Y.

Viditelné skutečné vrcholy jsou0,1,2,3,4,5,6,10,11,13,17,19.
Právě zbývajících15 junctions neleží v obraze žádného fyzického
vrcholu a má typ T. To přímo dokazuje číselnou větu p11 o obrázku(c).
Stupně dávají kontrolní rovnost2·7+3·5+3·15=74=2·37.
Nejde o závěr o jiných obrázcích ani o celém p11.

## CP-5 — jednotlivé značky, omezený nesoulad

`check_clasp_labels.py` přebírá hotové intervaly z CP-2, znovu je
nepočítá. Čelnost incidentní stěny určuje n·q>0 s již uzavřenou
vnější orientací. Dvě čelní stěny dávají +/− podle uzavřeného
znaménka hrany. Při jedné čelní stěně se šipka určí z pravé strany:
ve směru orientovaného okraje stěny míří n×u do jejího vnitřku;
kladný rovinný determinant v souřadnicích PDF s y dolů znamená
vnitřek napravo. Opačná orientace okraje obrátí vnitřní vektor.

Každá původní červená značka se přiřadí konkrétní hraně podle polohy
a směru. Dvoubodová kolmice je +; trojbodová šipka má hrot prostředním
bodem. Její části se ořežou všemi pozdějšími bílými výplněmi, aby
se za chybu nevydávalo označení celé zakryté hrany. Sedm značek je
celých skryto. Z29 přeživších značek28 souhlasí a jediná šipka,
path239 na hraně17–18, nesouhlasí: vychází +. Dvě velmi krátké
viditelné fyzické hrany6–9 a14–15 nemají přeživší značku; nejsou
proto v součtu28 vydávány za zkontrolovaná označení.

Nesoulad path239 má navíc argument přímo z původních incidentních
stěn a jejich stran projekce, nezávislý na veřejných 3D souřadnicích:
`notes/F7-C0006.md`. Zůstává candidate/low do nezávislé revize.
Správných15 T ani obecnou tabulku označení tím nevyvracíme.
