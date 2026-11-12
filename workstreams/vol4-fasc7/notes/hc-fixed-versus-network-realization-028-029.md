# Obrázky28–29: explicitní prostorové modely a přesný význam realizace

Celá původní p15/file30 byla zobrazena v `images/file-030.png`.
Následující blok pokrývá oba obrázky28 a oba29 i jejich
klasifikaci; obrázky30–31 a jejich odlišné argumenty jsou
teprve další práce. Úplná data jsou
`results/hc-realizability28-29.json`, ověřovač
`check_hc_realizability28_29.py`. Jeden cílený běh nice15
trval asi0.2s; nešlo o hledání prostorové realizace.

## R28-1 — všechny nativní čáry a všechny uspořádané junctions

Černé nativní cesty18–22,23–27,28–32,33–37 byly porovnány
s přesnými racionálními souřadnicemi všech jejich konců.
Kladné měřítko a posun v každé obrazové ose mají u každého
výskytu chybu menší než0.01pt. Zachycují zamýšlené přesné
průsečíky a kolinearity ilustrací, nikoli dodatečné fyzikální
tvrzení o každé mikroskopické zaokrouhlovací odchylce PDF.
Každý originální tah a každý junction je zkontrolován.

Pro levý pár označíme vnější pětici a,b,c,d,e po obvodu
od levého dolního rohu; f,g,h,i jsou čtyři přední body
výřezu, j horní a k dolní vnitřní špička. Čáry jsou přesně
průchody

    a b c d e a; e f g h i c; f j i; j k g; k h.

Oba obrázky tak mají11junctions a15čar. Každá jednotlivá
uspořádaná definice je v obou případech stejná:

    a=V(e,b), b=V(a,c), c=W(b,i,d), d=V(c,e), e=W(d,f,a),
    f=Y(e,j,g), g=W(f,k,h), h=W(g,k,i), i=Y(j,c,h),
    j=W(i,k,f), k=Y(g,j,h).

Pro pravý pár jsou a,b,c,d,e,f vnější šestice od levého
dolního rohu, g levá vnitřní špička, h dolní, i střední,
j horní a k přední pravý roh. Čáry jsou

    a b c d e f a; g h i j g; f g; i k d; b k.

Oba pravé obrázky mají11junctions a14čar a přesně

    a=V(f,b), b=W(a,k,c), c=V(b,d), d=W(c,k,e), e=V(d,f),
    f=W(e,g,a), g=Y(f,j,h), h=V(g,i), i=W(j,k,h),
    j=V(i,g), k=Y(i,d,b).

U Y se porovnávají cyklické rotace, nikoli zrcadlení.
Ověření zahrnuje všechny dvojice čar a determinanty všech
pořadí; pouhá abstraktní izomorfie by nestačila.

## R29-L — levý skutečný prostorový svědek

Vezměme trojboký kolmý hranol se základnou
(0,0),(29,0),(29/2,29/2) a výškou9. Z jeho horní přední
části vyřízněme trojboký hranol s půdorysem
(8,0),(21,0),(29/2,13/2), od výšky9/2 do9. Výřez se
dotýká pouze přední a horní stěny; jeho další tři stěny
vytvoří dutinu. Půdorys leží uvnitř původního trojúhelníku
s výjimkou svého předního základního úseku.

Všechny vrcholy tohoto tělesa jsou přesně

    a=(0,0,0), b=(29,0,0), c=(29,0,9),
    d=(29/2,29/2,9), e=(0,0,9),
    f=(8,0,9), g=(8,0,9/2), h=(21,0,9/2), i=(21,0,9),
    j=(29/2,13/2,9), k=(29/2,13/2,9/2),
    l=(29/2,29/2,0).

Osm orientovaných stěn je

    efjicd; abcihgfe; aedl; bldc; alb; fgkj; ijkh; ghk.

První dvě jsou A a B. Každá stěna je rovinný jednoduchý
polygon; konkávní stěny byly rozděleny certifikovanými
ušima na trojúhelníky. Všechny dvojice těchto trojúhelníků
mají právě očekávané společné vrcholy či hrany a nic dalšího.
Každá z18hran náleží dvěma opačně orientovaným stěnám;
všech12vrcholů má stupeň3. Konstrukce je tedy skutečný
3VP, nikoli pouze systém rovin nebo nezaplněná kostra.

Zvolme obrazové souřadnice

    U=x,  V=9−z−(9/13)y,

a směr k pozorovateli q=(0,−1,9/13). Přesné promítnuté
souřadnice každého z jedenácti viditelných vrcholů jsou
ty, které odpovídají originálu29 vlevo. Jediné celé
neviditelné hrany jsou al,bl,dl. Všech dalších15hran je
vidět v celém otevřeném intervalu; žádná další čára nevzniká.

## R29-R — pravý skutečný prostorový svědek

Začněme kvádrem [0,5]×[0,2]×[0,27/10]. Z přední horní
hrany vyřízněme čtyřstěn s vrcholy

    g=(2,0,27/10), i=(3,0,27/10),
    h=(4,0,9/10), j=(8/3,4/3,27/10).

Čtyřstěn leží v kvádru a jeho dvě trojúhelníkové stěny
jsou v původní horní a přední rovině. Odstranění vytvoří
přesně další dvě stěny ghj a ijh. Zbývající vrcholy jsou

    a=(0,0,0), b=(5,0,0), c=(5,2,0), d=(5,2,27/10),
    e=(0,2,27/10), f=(0,0,27/10), k=(5,0,27/10), l=(0,2,0).

Osm orientovaných stěn je

    fgjikde; abkihgf; bcdk; ledc; afel; alcb; ghj; ijh.

Opět je přesně12vrcholů stupně3,18hran a8jednoduchých
rovinných stěn; úplná kontrola všech jejich trojúhelníků
vylučuje nežádoucí průniky. Obrazové souřadnice jsou

    U=x+y,  V=27/10−z−(27/20)y,

směr k pozorovateli q=(1,−1,27/20). Výsledkem je přesně
pravá racionální rekonstrukce29. Neviditelné jsou al,cl,el
a **také hj**. Poslední hrana čtyřstěnového výřezu je
zakryta přední/horní částí kvádru; nesmí se do obrazu přidat
jen proto, že spojuje dva viditelné vrcholy. Všech zbývajících
14hran je vidět v celém intervalu. Právě tato kontrola
zakrytí odlišuje skutečný důkaz od odhadu tvaru z obrázku.

## R29-V — přesná viditelnost, ortografičnost a obecná poloha

U obou těles se každá prostorová hrana rozdělí v parametrech
všech promítnutých průsečíků s hranami. V každém otevřeném
atomu testujeme paprsek směrem q proti každému konvexnímu
trojúhelníku každé stěny. Rovnice roviny dává přesný
racionální parametr zásahu; polorovinné determinanty
rozhodnou, zda zásah leží ve stěně a před hranou.
To je stejný již doložený postup z
`notes/clasp-projection-fig104c.md`, nyní s novými úplně
ověřenými stěnami a všemi hranami. Vzhledem k absenci
nežádoucích prostorových průniků se viditelnost uvnitř
atomu nemění; jeho hranice jsou právě vyjmenované promítnuté
hrany. Sjednocení atomů dává výše uvedené celé intervaly.

Žádná stěna není viděna hranou: každý normál má nenulový
skalární součin s q. Viditelné neincidentní čáry mají
kladnou vzdálenost a všechny místní úhlové nerovnosti jsou
ostré. Zakryté vrcholy a vnitřky zakrytých hran jsou
striktně za krycími stěnami; u viditelného konce zakryté
hrany rozhodují ostré místní strany stěn. U hj vpravo
se může krycí stěna změnit, ale bez rovnosti hloubek.

Tyto poslední podmínky mají i přímý konkrétní doklad.
Všechny skryté hrany kromě hj jsou konvexní vnější hrany
hranolu/kvádru a obě jejich incidentní stěny mají n·q<0;
paprsek směrem q tedy ihned vstupuje do vnitřku tělesa.
Všechny tři stěny u skrytého l mají také n·q<0. Přesné
skalární součiny jsou uloženy v certifikátu.

Pro hj položme p(t)=h+t(j−h),0<t<1. Je-li t<1/2,
paprsek narazí na přední stěnu po kladném parametru4t/3
v bodě (4,0,9/10+18t/5). Ten leží mimo výřez: přední
trojúhelník se x=4 dotýká pouze v h. Pro t>1/2 narazí
na horní stěnu po parametru4(1−t)/3 v bodě
((16−8t)/3,(8t−4)/3,27/10). Zde x+y=4, zatímco pravá
hrana vyříznutého horního trojúhelníku má x=3−y/4;
rozdíl1−3y/4 je kladný pro y<4/3. Zásah je tedy opět
striktně mimo výřez. Pro t=1/2 jde o společný přední horní
úsek v bodě(4,0,27/10), ale kladná hloubková mezera2/3
zůstává. Na koncích jsou příslušné ostré koeficienty t
a1−t kladné, takže ani tam nejde o nestabilní tečnost.

Případné promítnuté incidence zcela zakrytých čar tedy
nemění viditelný graf. Tyto konečné ostré podmínky přetrvají
při dostatečně malé změně pohledu, takže platí kvalitativní
obecná poloha definovaná na p11. Nespoléháme na nedostatečné
dvojí podmínky odpovědi40.

Použité U,V jsou lineární obrazové souřadnice. Aby šlo
doslova o ortografické promítnutí do(x,y) roviny, použijme
v prostoru invertibilní afinní změnu souřadnic
(x,y,z)↦(U,V,−q·(x,y,z)). Obě první složky mají jádro q,
třetí na q nezaniká, tedy transformace je invertibilní.
Zachovává roviny, průniky, hranice tělesa i stupeň3, a
závěrečný ortografický pohled zahodí třetí souřadnici.
Kladné měřítko a posun obrazových os lze zahrnout do U,V.
Tím svědci splňují skutečnou definici silné realizovatelnosti.

## R28-2 — přímý důkaz, že oba pevné obrázky28 realizaci nemají

Každé skutečné promítnutí 3VP má na vnějším obvodu standardní
hodinové šipky. Vlevo pak W v e,c okamžitě nutí ef=ci=+.
Vpravo W v f nutí fg=+; W v b,d nutí bk=dk=+ a Y v k
s těmito dvěma+ nutí i třetí větev ik=+. Každý požadovaný
krok je přímo řádkem Tabulky1 a uložená úplná propagace
poskytuje další kontrolu.

Levý obrázek má oblasti A=efjicd a B=eabcihgf, sdílející
právě oba nucené konvexní úseky ef a ci. V normalizovaných
souřadnicích jsou e=(0,0),f=(4,9/2),c=(29,0),i=(25,9/2).
Jejich nositelky jsou různé a neparalelní; determinant
směrových vektorů je36. Pravý má A=fgjikde a B=fabkihg,
sdílející fg a ik. Jsou na přímkách V=0 a V=27/20:
opět dvě různé nositelky, tentokrát paralelní.

Znaménko+ znamená skutečnou konvexní hranu mezi dvěma
viditelnými rovinnými stěnami, nikoli occlusion. Každá
z obou sdílených nositelek by tedy ležela zároveň v rovině
A i v rovině B. Dvě různé roviny mají průnik prázdný
nebo jedinou přímku: jejich dvě lineární rovnice mají
hodnost2. Proto by zde A=B; to zase odporuje nenulovému
konvexnímu ohybu+. Žádný z obou pevných obrázků28 tak
není silně realizovatelný. Tento argument výslovně
nepřipisuje occlusion čáře vlastnost společné průsečnice.

## R28-3 — místní konzistence, slabá realizace a logické důsledky

Oba přesné prostorové svědky29 lze označit fyzickými štítky,
které splňují všechny lokální relace. Totožné uspořádané
sítě28 mají stejné proměnné a stejné relace, a proto přijímají
tytéž labelings. Jsou tedy lokálně konzistentní. Svědek29
je zároveň přesně tím jiným obrázkem H′ z definice slabé
realizace pro odpovídající28. Oba29 jsou silně realizovatelné,
oba28 slabě, ale nikoli silně realizovatelné.

Obecně silná realizace implikuje slabou volbou H′=H.
Je-li naopak HC síť neoznačitelná, nemůže mít žádný silně
realizovatelný obraz: takový obraz by měl fyzické štítky
splňující stejné relace. Již uzavřený úplný spor pro26
v `notes/impossible-pictures-024-027.md` tak dokazuje
i zdejší tvrzení, že26 je nemožné ve smyslu „ne slabě
realizovatelné“. Není potřeba jeho starou propagaci opakovat.

Historické připsání rozlišení Huffmanovi1971 zůstává
výslovně bibliograficky neověřeno. Matematické výroky
tohoto konkrétního bloku mají uvedené vlastní důkazy.
