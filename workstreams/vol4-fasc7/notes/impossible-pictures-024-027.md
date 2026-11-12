# Každý nemožný dílčí obrázek24–27

Rozsah: p14/file29, původní SVG a celá zobrazená sazba.
Všech osm malých vzorů24–25 je kontrolováno samostatně.
Čáry vycházející ven z malého vzoru mají volný konec: není jim
uměle předepsána další V relace. Pokud by celý obrázek měl
labeling, jeho restrikce by splnila všechny zde přítomné
úplné junctions. Rozpor těchto lokálních podmínek proto
vylučuje každý obsahující obrázek bez ohledu na pokračování.

Používáme lokální symboly O,I pro šipku ven z junctionu a do
něj. Přesné Tabulkové relace jsou

`T: O+I,O−I,OOI,OII; V: I+,IO,+O,O−,OI,−I;`
`W: O+I,−+−,+−+; Y: IO−,O−I,−IO,−−−,+++`.

Tedy T stanoví oba bary, prostřední větev W nikdy není šipka,
levá větev W nikdy není I a pravá větev W nikdy není O.
V nemá OO aniII; Y nemá dvě příchozí ani dvě odchozí šipky.

## I24 — čtyři vzory se dvěma T

Názvy vNN níže jsou podle rostoucích souřadnic v příslušném
malém vzoru, nikoli globální označení celé stránky. Přesné
body a všechny úplné relace jsou v
`results/impossible-subpictures24-25.json`.

1. **TT:** T v02 a v04 předepisují na společném baru současně
   v02→v04 a v04→v02. Rozpor je přímo na jediné čáře.
2. **VTT:** oba T v02,v03 předepisují šipky z centrálního
   V v01 směrem k sobě. Jeho řádek by byl OO, který není
   v Tabulce1. Všechny další větve mohou být libovolné.
3. **YTT:** T v03,v04 obdobně předepisují dvě šipky od
   centrálního Y v02. Žádný jeho přípustný řádek nemá dvě O.
4. **WTVT:** T v02 nutí levou větev W v00 na O, tedy W má
   jediný řádek O+I. Hrana z v00 do V v03 je proto +.
   V v03 je V(v00,v06); jeho + na levé větvi nutí O na
   pravé, tedy v03→v06. T v06 ale předepisuje v06→v03.

## I25 — všechny čtyři vzory s jediným T

1. **WT:** společná čára je prostřední větev W v00, kde musí
   být znaménko. Současně je bar T v02, který z ní dělá šipku.
2. **První WWT:** T v05 nutí pravou větev W v04 na I.
   Tím jeho řádek musí být O+I, a tedy čára k W v01 je
   šipka. Je to ale prostřední větev v01, kde šipka není možná.
3. **Druhé WWT:** T v05 nutí levou větev W v03 na O.
   Řádek O+I pak předepíše v02→v03. Tato čára je pravá
   větev W v02, kde tedy vznikne zakázané O.
4. **WYT:** T v05 nutí třetí větev Y v03 na I. Jediným
   odpovídajícím řádkem Y je O−I, takže větev k W v00 je
   šipka. Ve v00 je však prostřední a musí být znaménkem.

`check_impossible_subpictures.py` porovnává všechny původní
path18–46 s jejich přesnými mřížkovými body, včetně vložených
T uprostřed souvislých tahů. Největší odchylka je menší než
0.01 bodu. Po rozštěpení všech průsečíků se ověří každé
pořadí větví a každý typ. Stejné rozpory mají úplné podpůrné
propagační řádky v JSON; není spuštěno žádné větvení.

## I26 — celý Reutersvärdův obrázek

Všechny path47–65 jsou samostatně přepsány. Pravé čtyři konce
mají jednu přesnou mřížku, levé tři konce druhou; devět dlouhých
spojů zůstává skutečnými přímými úsečkami mezi nimi. Každý
původní koncový bod souhlasí v toleranci0.01 bodu. Rozštěpení
T a kontrola všech incidencí dávají28 junctions a37 čar:
10V,11W,4Y,3T. Původní souřadnice a normalizační mapy jsou
uloženy v `results/hc-drawings26-27.json`.

Krátký úplný rozpor lze vybrat z celého uloženého průchodu:

- T v18=T(v20,v23,v17) předepisuje v17→v18.
- W v17=W(v18,v14,v12) proto má řádek O+I a hranu k v14
  označenou +.
- Y v14=Y(v04,v17,v15) s jedním + musí mít řádek +++.
  Je tedy také v04–v14 označena +.
- V v04=V(v14,v03) pak nutí v04→v03.
- W v03=W(v04,v15,v05) by tím mělo levou větev I, což
  žádný řádek W nedovoluje.

To je rozpor skutečných dlouhých spojů od pravé strany k levé,
nikoli jen subjektivní dojem optického klamu. Celý uložený
propagační certifikát navíc uvádí každý podpůrný řádek všech
mezikroků. Historická atribuce a národnost umělce nebyly zvlášť
bibliograficky ověřovány; matematický výrok o této kresbě ano.

## I27-1 — obě kresby lze konzistentně označit

`check_hc_drawings26_27.py` přepíše všechny tahy66–72 a73–77.
Normalizace je afinní s kladnými osovými měřítky a zachovává
incidenci i úhlové typy; zaokrouhlení všech původních bodů je
menší než0.01 bodu. Vlevo je17 junctions/23 čar
(5V,5W,3Y,4T), vpravo14/18 (6V,4W,2Y,2T).
Každá lokální relace a obvod jsou uloženy samostatně.

Po stanovení standardního obvodu jsou vpravo všechny domény
jednoprvkové. Vlevo zbývá pouze `v07_v08 ∈ {+,<}`; obě hodnoty
skutečně splňují všechny úplné relace. Žádné jiné možnosti
nejsou, protože každé odstranění má nepřítomnost podporujícího
řádku jako úplný argument. Dva, respektive jeden úplný svědek
jsou vypsány v `standard_labelings`. Tím je přímo doložena
lokální označitelnost a zároveň úplnost standardních případů,
kterou níže potřebujeme pro prostorovou nemožnost.

## I27-2 — proč rovinná oblast určuje jednu prostorovou rovinu

Otevřená souvislá oblast mezi viditelnými čarami nemůže přejít
z jedné viditelné stěny do jiné bez viditelné hrany nebo obrysu.
Její viditelné body proto patří jedné rovinné stěně. Skryté
stěny mohou ležet za ní, ale nemění její nosnou rovinu.
Protože její projekce obsahuje otevřenou2D oblast, rovina se
dá psát `z=f(x,y)` s afinní funkcí f; obecná poloha vylučuje
projekci stěny do jediné čáry. Menší z je zde blíže k pozorovateli,
v souladu s konvencí hlavního textu.

Dvě různé roviny mají nejvýše jednu společnou přímku: odečtení
jejich rovnic dává nenulovou lineární rovnici v jejich společné
rovině, tedy přímku, případně prázdný průnik. Pokud dva grafy
afinních funkcí souhlasí na dvou různých rovnoběžných přímkách
projekce, jejich rozdíl je nulový všude. Nešlo by o skutečnou
konvexní nebo konkávní hranu dvou různých stěnových rovin.

Každý skutečný konečný3VP v obecné poloze má standardní vnější
obrys podle již uzavřeného argumentu B-2. Proto pro vyloučení
realizace těchto kreseb stačí vyloučit právě všechny standardní
labelingy z I27-1. Neomezujeme svévolně množinu fyzických případů.

## I27-3 — pravý obrázek a přesný tištěný pomocný krok

V normalizovaných souřadnicích je A vnitřní oblast0 a B oblast2.
Jejich dvě společné čáry jsou

`v00–v09 : (0,1)–(29,1)` a
`v04–v13 : (4,4)–(33,4)`.

Obě mají v jediném standardním labelingu vynucené +. Proto
jsou skutečnými společnými hranami rovin A,B, nikoli pouhými
obrysy zakrývajícími zadní stěnu. Roviny by se musely shodovat
na dvou různých rovnoběžných přímkách y=1 a y=4. Podle I27-2
by byly totožné, což je v rozporu s +. Zde je tak doslova
uzavřen i autorův argument dvou odlišných průsečnic.

## I27-4 — levý obrázek: úplný argument pomocí pořadí hloubek

Zde je A oblast0 a B oblast4. Ve **všech obou** standardních
labelinzích je společná dolní hrana

`v04–v13 : (4,4)–(37,4)` označena +,

zatímco společný horní úsek

`v08–v10 : (25,3)–(29,3)` je šipka směrem doprava.

Spodní + znamená skutečnou společnou konvexní hranu. Rozdíl
afinních výšek `d=z_A−z_B` tedy má tvar `c(y−4)`, c≠0.
Lokálně je těleso u konvexní hrany průnikem vnitřních
poloprostorů `z≥z_A` a `z≥z_B`, protože obě stěny jsou viditelné
a vnitřek leží ve směru většího z. Viditelná plocha tak má
výšku max(z_A,z_B). Na straně A, těsně pod y=4, musí být
z_A>z_B; odtud c>0. Proto při y=3 máme d=−c<0: rovina A
leží před rovinou B.

Horní šipka směřuje doprava, takže její přední viditelná
stěna leží pod čárou, kde je právě B. A je druhá viditelná
oblast, zakrytá za tímto obrysem; musí tedy být z_A>z_B,
čili d>0. Rovnost by z obrysu dělala společnou hranu obou
viditelných stěn nebo výjimečný dotyk, což odporuje značce
půlhrany a obecné poloze. Dostáváme přímý rozpor d<0 a d>0.
Nezávislá volba na v07–v08 se žádného z těchto kroků netýká.

JSON zapisuje i obecný orientační výpočet: pro obvod A
v opačném směru než hodinové ručičky má determinant h na
středu horní šipky hodnotu33. Konvexní hrana dává znaménko
d=−sign(h), ale šipka vyžaduje +. Tento malý výpočet je
podpůrný; předchozí afinní argument dokazuje rozpor pro všechny
možné výšky, nikoli pouze jednu zvolenou3D konfiguraci.

## I27-5 — přesně vymezená neuzavřená věta

U levého obrázku se tištěné vysvětlení „A a B se protínají
ve dvou různých přímkách“ nepřebírá pouze ze dvou společných
hranic rovinných oblastí. Horní společný úsek je totiž vynucená
půlhrana, kde se dvě viditelné stěnové roviny obecně fyzicky
neprotínají. Vlastní úplný důkaz nemožnosti z I27-4 sám o sobě
tento jiný pomocný krok neověřuje. Jeho zamýšlené prostorové
odvození proto zůstává partial, bez nové karty. Pravá kresba
ani hlavní tvrzení o nemožnosti levé kresby tím otevřené nejsou.

Příslušné aktuální errata p14 neobsahují opravu24–27.
Výpočty byly malé, nice15; původní obecná Tabulka1 ani žádný
starý3D certifikát se znovu nepočítaly. Odkaz na úlohu57 bude
uzavřen až jejím vlastním důkazem, stejně jako pokračování
posledního odstavce p14 na p15.
