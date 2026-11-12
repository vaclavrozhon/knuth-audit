# Obrázek104(d): celý pohled,45 značek a jediný T

Zdroj p11/file26 byl zobrazen. Přesný histoscape s maticí
[[4,3],[1,2]] má již uzavřenou úplnou geometrii v H27 a uložených
`results/histoscape-local.json`, položka `fig101d`. Jeho20 vrcholů,
30 hran a12 stěn se přebírá bez opakování staré kontroly150 lokálních
typů. Nynější nový rozsah je pohled a každá značka Fig.104(d).

## HP-1 — identifikace a všechny úseky

Horní čtverec z=4 v původní bílé cestě319 identifikuje postupně
(0,0,4),(0,1,4),(1,1,4),(1,0,4). První bod cesty282 je(1,0,1).
Čtyři z těchto nekoplanárních referencí určují dvě afinní promítací
souřadnice. Každý konec každé původní černé cesty i každý vrchol
bílé výplně je pak jednoznačně přiřazen některému z20 vrcholů;
největší čtverec odchylky je68667481/2250000000000 <0.000031 bodu²,
zatímco druhý nejbližší kandidát je vždy vzdálen více než1 bod.

Vnější normály všech12 stěn jsou přímo uvedeny jejich rovinou
a znaménkem souřadnicové osy. Orientace každého hraničního cyklu
je srovnána s touto normálou. Jednoduché stěny jsou rozděleny na
trojúhelníky odstraněním platných uší: vrchol je konvexní, úhlopříčka
nekříží hranici a ucho neobsahuje jiný vrchol. Po odstranění zůstává
jednoduchý polygon se stejnou orientací a postup končí trojúhelníkem.
Tím se zachová přesně celá stěna, včetně konkávních osmiúhelníků;
nejde o její nahrazení konvexním obalem.

Směr ke kameře je jádro promítací mapy se všemi třemi souřadnicemi
kladnými; znaménko určí viditelná horní stěna. Konečný přesný algoritmus
CP-2–CP-3 z `clasp-projection-fig104c.md` má nyní tyto ověřené vstupy:
platné uzavřené těleso, úplný rozklad jeho stěn, nenulové projekce
hran a žádný nulový jmenovatel testu paprsku s rovinou. U všech30 hran
byly samostatně porovnány všechny viditelné intervaly s každým původním
černým tahem po překrytí pozdějšími bílými výplněmi. Obě úplné množiny
se přesně rovnají. Odpovídající kontrolní program je
`check_histoscape_projection.py`, evidence `results/histoscape-projection.json`.

## HP-2 — vrcholy a jedna projekční křižovatka

Ze všech elementárních viditelných úseků se vytvoří graf. Odstraní se
pouze uměle vložené body se dvěma kolineárními větvemi téže fyzické
hrany. Přesná determinantová klasifikace z CP-4 dává:

5 V, 8 W, 5 Y, 1 T, celkem19 junctions a26 čar.

Z20 skutečných vrcholů jsou skryty právě(0,0,0) a(1,1,1); všech18
ostatních má odpovídající junction. Jediný zbývající junction leží
uvnitř fyzické hrany, má dvě kolineární větve a příčný konec jiné
hrany: T. Je pod středem kresby, přesně podle věty p11.
Kontrolní součet stupňů je2·5+3·8+3·5+3=52=2·26.

## HP-3 — všech45 označení

Z dvojice vnějších normál se pro každou fyzickou hranu určí
konvexita pomocí znaménka m·(n×u), kde u probíhá hranou po orientované
hranici první stěny; kladné znamená konkávní, záporné konvexní,
jak již bylo dokázáno v G-2. U každé dvojice je ověřeno, že její
orientace společné hrany je opačná a součin nenulový. Čelnost určuje
n·q>0. Při jediné čelní stěně určí n×u stranu šipky; při dvou
čelních stěnách se použije +/−. To je stejný již zdůvodněný test CP-5.

Každá jednotlivá původní značka má jednoznačně přiřazenou hranu.
Červená kolmice znamená +, bílý podélný výmaz černé čáry znamená −,
a trojbodový červený chevron určí přesný směr šipky. Přiřazení kontroluje
jak polohu, tak kolmost či rovnoběžnost; nezávisí na OCR. Všech45
značek souhlasí s prostorovým výsledkem. Žádná není zcela zakrytá
a každá viditelná fyzická hrana má alespoň jednu přeživší značku.
Výsledek je v `results/histoscape-labels.json`; program
`check_clasp_labels.py histoscape` znovu nepočítá hotovou viditelnost.

Oba malé nové výpočty proběhly s nice15 pod sekundu. Toto uzavírá
konkrétní Fig.104(d), nikoli automaticky obrázek převráceného pohledu103(d)
nebo následující přepis sítě(20); ty vyžadují své vlastní porovnání.

## HP-4 — samostatně ověřený opačný pohled103(d)

Původní cesty136–145 v `sources/file-025.svg` byly porovnány s tělesem
po půlobratu kolem osy z. Jeho matice změní znaménka prvních dvou
sloupců promítací mapy; posun obrázku se stanoví zvlášť. Všechny
vrcholy kresby jsou tak jednoznačně identifikovány, s odchylkou
<0.02 bodu od modelu půlobratu. Samostatná afinní mapa z referencí
(0,0,0),(0,0,4),(0,2,0),(2,0,0) pak dává největší čtverec zbytku
110660839913/3136000000000000 <0.000036 bodu² u všech výskytů.
Směr pohledu má nyní znaménka(−,−,+), jak vyžaduje půlobrat.

Pro tento nový směr byly nově zkontrolovány všechny viditelné intervaly
každé z30 hran a všechny původní černé tahy po zakrytí. Přesně se
rovnají; výsledek má14 junctions=6 V+5 W+1 Y+2 T a18 čar.
Viditelné skutečné vrcholy jsou indexy0,1,2,3,4,5,6,7,11,13,14,15
uloženého modelu. Nově se například objeví(0,0,0) a celá hrana
odtud k(0,0,4), které předchozí pohled skrýval. Nově vidíme vnější
stěny x=0,y=0; mnohé části původního pohledu jsou naopak zakryty.
To dokládá i konkrétní význam věty o nově odhalených částech v popisku.

Viz `check_histoscape_reverse.py` a `results/histoscape-reverse.json`.
Jde o nový směr pohledu, nikoli opakování dříve úspěšné kontroly.
