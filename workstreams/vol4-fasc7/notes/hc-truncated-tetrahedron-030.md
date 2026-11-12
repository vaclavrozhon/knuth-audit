# Obrázek30: prostorový svědek, souběžnost a libovolně malá porucha

Původní p15/file30 byla celá zobrazena. Tento blok posuzuje
oba horní obrázky30 i oba jejich spodní doplňky se všemi
třemi červenými nositelkami. Zdrojový ověřovač
`check_truncated_tetrahedron30.py` a úplný certifikát
`results/truncated-tetrahedron30.json` byly vytvořeny jediným
krátkým během nice15. Obrázek31 a argument o nemožnosti
každé realizace jeho sítě nejsou tímto blokem uzavřeny.

## R30-1 — všech šest bodů a všechny čtyři ilustrace

Levá přesná rekonstrukce v obrazových souřadnicích je

    a=(0,0), b=(60,0), c=(20,−16),
    d=(16,−4), e=(42,−3), f=(112/5,−10).

Nativní cesty38–42 dávají vnější trojúhelník a,b,c,a,
vnitřní d,e,f,d a čáry ad,be,cf. Každý výskyt bodu je
do0.01pt od uvedené přesné geometrie po kladném měřítku
a posunu. Pro pravou rekonstrukci se přímo použily přesné
zdrojové souřadnice všech šesti bodů cest43–44; cesty45–47
se shodují s příslušnými spojnicemi v téže toleranci.
Žádná domnělá jednoduchá hodnota jejich změněných souřadnic
nebyla odhadována z OCR nebo z tvaru obrázku.

V obou případech je šest junctions a devět čar, s přesně
těmito stejnými uspořádanými relacemi:

    a=W(c,d,b), b=W(a,e,c), c=W(b,f,a),
    d=Y(a,f,e), e=Y(d,f,b), f=Y(d,c,e).

Každé pořadí i každé nechtěné křížení bylo zkontrolováno.
Standardní šipky po vnějším obvodu ve třech W okamžitě
nutí ad=be=cf=+. Tři Y pak nutí všechny tři vnitřní
trojúhelníkové hrany také+. Jediné výsledné standardní
přiřazení přímo splňuje každou ze šesti relací v obou
obrázcích. Pravý je tedy určitě lokálně konzistentní.

## R30-2 — skutečný levý zkrácený čtyřstěn

Začněme čtyřstěnem s vrcholy

    a=(0,0,0), b=(60,0,0), c=(20,−16,0),
    o=(24,−6,−1).

Body d,e,f leží na ao,bo,co v parametrech2/3,1/2,3/5:

    d=(16,−4,−2/3), e=(42,−3,−1/2),
    f=(112/5,−10,−3/5).

Rovina těchto tří bodů oddělí o od a,b,c. Odříznutím
o tak vznikne konvexní těleso s šesti vrcholy, devíti
hranami a pěti stěnami

    acb; abed; bcfe; cadf; def.

Každá hrana náleží přesně dvěma opačně orientovaným
stěnám a každý vrchol má stupeň3. Všechny stěny jsou
jednoduché rovinné polygony. Jejich normály mají nulový
skalární součin právě s body příslušné stěny a přísně
záporný se všemi ostatními vrcholy po odečtení bodu stěny.
Jde tedy o skutečné podpůrné stěny jednoho konvexního
3VP. V certifikátu je každá z těchto hodnot uložena.

Ortografická projekce vynechá z, pozorovatel je ve směru
(0,0,−1). Vnější zadní trojúhelník acb je odvrácený,
další čtyři stěny jsou přivrácené; jejich normálové
součiny s pohledem jsou všechny nenulové. Každá z devíti
hran je vidět v celém intervalu, jak ověřuje přesný test
proti všem trojúhelníkům všech stěn. Žádné další vrcholy
či čáry nejsou přítomny. To dává právě celý levý obrázek.

Konvexita, ostré směry stěn a nepřítomnost neincidentních
viditelných průsečíků dokazují stabilitu viditelného grafu
při malé rotaci. V každém vnějším vrcholu zůstávají dvě
přivrácené boční stěny a jedna odvrácená základna, ve
vnitřním vrcholu tři přivrácené stěny. Tím je splněna
skutečná definice obecné polohy z p11 a levý30 je silně
realizovatelný, bez spoléhání na nedostatečné podmínky40.

## R30-3 — levé tři nositelky a každý červený tah

Oblasti A,B,C odpovídají stěnám cadf,bcfe,abed. Jejich
párové průsečnice jsou nositelky cf,be,ad. V obrazu jsou

    ad: y=−x/4,  be: y=(x−60)/6,
    cf: y+16=(5/2)(x−20).

Všechny tři procházejí přesně(24,−6), projekcí odříznutého
vrcholu o. Tento bod není vrcholem výsledného tělesa:
zachovaly se jen nositelky původních hran, což přesně
vysvětluje tištěný „invisible common point“.

Spodní levé cesty48–49 byly celé porovnány s toutéž šesticí
bodů po kladném měřítku a posunu. U každého červeného tahu
50,51,52 bylo nezávisle ověřeno, že začíná v a,b,c,
leží na příslušné nositelce a jako úsečka obsahuje společný
bod(24,−6). Největší kolmá odchylka každého konce je<0.01pt.
Vpravo jsou stejně úplně porovnány cesty53–54 a každá ze
tří červených nositelek55–57 s odpovídajícími horními
pravými čarami. Červená kresba tedy není použita jako
nezávislý geometrický předpoklad; její shoda je sama doložena.

## R30-4 — přesný pravý determinant a potřebná věta o rovinách

Pro obrazové body (x,y) použijme homogenní souřadnice(x,y,1).
Přímka uv je vektor u×v. Tři takové nositelky mají společný
projektivní bod právě tehdy, když determinant jejich tří
vektorů je0; zde jsou první dvě neparalelní, takže případný
společný bod musí být konečný. Pro pravý originál vychází
přesný racionální determinant kladný, přibližně6271.3005322
po normalizaci šířky vnějšího trojúhelníku na60.

Navíc byly všechny obě souřadnice všech šesti původních
bodů obaleny intervalem±0.01pt. Přímé intervalové provedení
tří vektorových součinů a determinantu dává interval
[6056.84228…,6485.78660…], celý nad0. Spor tedy nezávisí
na volbě racionální rekonstrukce ani na poslední desetinné
zaokrouhlovací číslici původních vektorů.

Prostorový důvod je třeba formulovat přesně. Všechny ad,be,cf
jsou nucené+, tedy skutečné průsečnice příslušných odlišných
rovin A,B,C. Pokud by normály těchto tří rovin měly hodnost2,
všechny jejich párové průsečnice by měly tentýž směr
(společné jednorozměrné jádro normálů). Jejich nekonečně
dlouhé nositelky by proto byly paralelní a také promítnuté
nositelky by byly paralelní nebo se zhroutily do bodu.
Viditelná dvojice ad,be je však neparalelní a nenulová.
Normály tedy mají hodnost3; soustava tří rovinných rovnic
má jediné řešení a všechny tři párové nositelky jím
procházejí. Jeho projekce musí ležet na všech třech
obrazových nositelkách, což pravý nenulový determinant
vylučuje. Pravý30 není silně realizovatelný.

**Oddělená nejasnost tištěného zdůvodnění:** věta „because
no two of them are parallel“, pokud „them“ znamená pouze
trojici rovin, sama o sobě nestačí. Roviny x=0,y=0,x+y=1
jsou po dvojicích neparalelní a nemají společný bod;
jejich tři průsečnice jsou paralelní s osou z. V kontextu30
ale skutečně platí výše použitá silnější vlastnost
neparalelních **průsečnic**, doložená původním obrázkem.
Závěr je proto dokázán a jde zatím o partial výkladu
pomocné věty, bez nové karty nálezu. Správný závěr se
nevydává za obecnou platnost její slabší doslovné premisy.

## R30-5 — přesně libovolně malá porucha

Ponechme všech šest levých bodů kromě d, které změníme na
d_ε=(16,−4+ε). Nositelky be a cf se stále protínají
v(24,−6). Determinant dvou vektorů ad_ε a ao je však

    16·(−6)−(−4+ε)·24 = −24ε.

Pro každé ε≠0 tedy ad_ε tímto bodem neprochází. Naopak
v ε=0 jsou všechny úhlové determinanty v šesti junctions
ostré a všechny neincidentní úsečky disjunktní s kladnou
vzdáleností. Konečnost těchto podmínek zaručuje δ>0 takové,
že pro |ε|<δ má obrázek právě tutéž uspořádanou HC síť
i vnější obvod. Pro0<|ε|<δ je tedy lokálně konzistentní
a slabě realizovatelný původním levým svědkem, ale podle
R30-4 není silně realizovatelný. To dokazuje tvrzení
o libovolně malé změně souřadnice, nikoli jen dva od sebe
vzdálené konkrétní obrázky. Silná realizace opravdu není
otevřenou vlastností v prostoru všech obrazových souřadnic.

Historické připsání Huffmanovi zůstává výslovně neověřené;
všechny zdejší prostorové, rovinné a perturbační výroky
mají vlastní úplné argumenty.
