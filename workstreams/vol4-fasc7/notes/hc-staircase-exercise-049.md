# Úloha49 včetně všech vypsaných řetězců

Zadání p118/file133, odpověď p168–169/file183–184. Originální
stránky byly zobrazeny; přepis není založen pouze na OCR.
Původní tahy obrázku jsou path18–76 v `sources/file-133.svg`.
Některé krajní obrysy jsou v PDF opakovány čtyřikrát; po
ztotožnění stejných geometrických hran se nesmějí počítat
čtyřikrát jako různé proměnné.

## E49-0 — úplná kresba a skutečné odpojení vnitřku

`check_hc_staircase49.py` přiřadí každý původní bod jedné
souřadnici obdélníkové mřížky. Obě kladná osová měřítka
zachovávají incidenci a znaménka determinantů; každý bod
originálu má odchylku menší než0.01 bodu. Všechny průsečíky,
místní typy a pořadí paprsků jsou ověřeny jednotlivě.
Je zde95 junctions a138 čar:9V,44W,42Y, žádnéT. Obvod má32
různých junctions. Po odstranění těchto obvodových junctions
a incidentních čar skutečně zbudou čtyři oddělené komponenty
velikostí18,18,18,9. Úplné seznamy komponent jsou uloženy.
Subjektivní vnímání přeskakujícího obrazu se nedokazuje jako
univerzální psychologické tvrzení.

## E49-a1 — všechny čtyři vodorovné úrovně

Každá úroveň má deset po sobě jdoucích čar `j_0…j_10` a devět
mezilehlých junctions, střídavě W,Y,W,Y,…,W v přesném pořadí
uvedeném v odpovědi. Čtyři celé řetězce jsou přímo přiřazeny
jednotlivým původním tahům; není zkontrolována jen jedna řada.
Štítek každé čáry teď orientujeme zleva doprava podél řetězce.

U `W(j_(i−1),j'_i,j_(i+1))` dává Tabulka1 pro dvě řetězcové
čáry právě páry `++`, `−−`, `<<`; prostřední větev je postupně
`−,+,+`. U sousedního Y je třeba vyloučit dvě možnosti
s řetězcovou šipkou>, protože jeho oba sousedé W takovou
hodnotu nepovolují. Zbývají opět právě stejné páry `++`,`−−`,`<<`.
Tranzitivitou shody sousedních štítků musí být celá úroveň
jedním ze slov `++++++++++`, `----------`, `<<<<<<<<<<`.
Toto je nutná a lokálně dostačující podmínka, nikoli jen
pozorování výsledného labelingu.

Při hodnotě+ jsou postranní větve W záporné a Y kladné.
Při hodnotě− nebo< jsou naopak větve W kladné a Y záporné.
To vysvětluje i tištěný další krok o vynucení okolních štítků.

## E49-a2 — standardní obvod dává jediné celé řešení

Spodní řada je vnějším obvodem: při cestě zleva doprava má
objekt vlevo, proto standardní šipky míří opačně, tedy<.
Všechny tři vyšší řady dostávají hodnotu−; toto tvrzení bylo
zkontrolováno pro každý jejich konkrétní začátek, konec a
každou z deseti čar, nikoli předpokládáno podle perspektivy.

Úplný certifikát stanoví všechny32 obvodové šipky, potom
uvádí133 odstranění nepodporovaných hodnot u konkrétních
lokálních relací. Každé odstranění obsahuje všechny zbývající
podpůrné řádky. Proto neztrácí žádné řešení; konečnost domén
zaručuje ukončení. Na konci má každá ze138 proměnných právě
jednu hodnotu a všech95 úplných relací je znovu přímo splněno.
To zároveň dokazuje existenci i jednoznačnost a doloží všechny
zbývající štítky v okolí úrovní. Výsledek je
`standard_labeling` a `standard_propagation` v JSON.

## E49-b1 — obě svislé boční posloupnosti a dolní rohy

Vpravo směrem vzhůru a vlevo směrem dolů se v původní kresbě
nachází řetězec devíti junctions
`V,W,Y,W,Y,W,Y,W,V`, tedy osmi čar. Vnitřních sedm junctions
má přesně stejné pořadí jako v předchozí argumentaci, proto
opět nutí uniformní řetězec+,− nebo<. Oba řetězce a všechna
jejich pořadí jsou explicitně ověřeny v
`side_chain_certificates`; nejde o předpoklad zrcadlové symetrie.

Označme boční konstantu S a konstantu spodní desetihraňové
řady B. Tabulka V v dolním rohu, se správnými orientacemi,
dovoluje z devíti párů S,B∈{+,−,<} právě

`(−,<), (<,−), (<,<)`.

To platí u obou dolních rohů samostatně. Tím je vyloučena+
jak na bočních řetězcích, tak na spodní řadě. Pokud je alespoň
jeden boční řetězec−, musí být spodní řada<. Pokud jsou oba
boční řetězce<, spodní řada může být− nebo<. To je přesně
původní zdvojení poslední skupiny11, které by samotný počet29
horních řetězců nevysvětloval.

## E49-b2 — každé ze29 vypsaných horních slov

Horní nativní path18 má body `t_0,…,t_8`; všech sedm vnitřních
junctions jsou V s tištěnými střídajícími se pořadími.
Při orientaci štítků z t_(i−1) do t_i do t_(i+1) jsou páry

- pro liché i: `+<, −>, <+, <<, >−, >>`;
- pro sudé i: `+>, −<, <−, <<, >+, >>`.

První a poslední čára patří zároveň bočnímu řetězci, ale
v opačném směru. Jejich domény jsou tedy právě{−,>}.
Začneme oběma jednopísmennými prefixy a postupně přidáváme
pouze přechody z příslušné úplné dvojkové relace. Indukcí
po délce to generuje všechna a jen přípustná slova, každé
právě jednou. Počty prefixů jsou2,3,5,8,13,21,34,55; omezení
posledního symbolu ponechá29 slov délky8.

**Každé jednotlivé slovo** v sazbě bylo přepsáno do
`PRINTED_TOP` a porovnáno s touto odvozenou množinou. Seznam
nemá duplicitu ani vynechané slovo a všechny délky jsou8.
Podle prvního a posledního symbolu dostáváme

|První|Poslední|Počet|
|---|---|---:|
|−|−|4|
|−|>|7|
|>|−|7|
|>|>|11|

Předchozí dolní-rohový argument dává celkový počet obvodů
`4+7+7+11+11=40`. Všechna znaménka orientací jsou doložena
skutečným překryvem horních krajních hran s bočními řetězci.

## E49-c — úplný obvodový rozklad, nikoli jen součin čísel

Na celý původní obvod je aplikován již prokázaný čtyřstavový
maticový argument FB-1/FB-2. Jsou uloženy všechny místní
matice, všechny prefixové součiny i podmínka cyklické podpory
každé dvojice. Stopa je40, nezávisle na tištěném rozkladu29 slov.
Každý globálně přípustný obvodový pár předepisuje stejný
štítek své vnitřní větve: všech23 různých vnitřních čar
dotýkajících se obvodu má ve všech40 případech tentýž
explicitně uložený vektor hodnot.

Libovolné obvodové řešení lze tedy spojit s libovolným
vnitřním řešením pro tento pevný vektor a obráceně. Standardní
obvod je přípustný a jeho vnitřek je jediný podle E49-a2.
Proto existuje přesně40 celých labelingů a každý má stejný
vnitřek. Tím je prokázán i tištěný důvod části(c), ne pouze
číslo40. Jediný nový geometrický/početní běh trval asi0.75s
s nice15; následné dvě boční kontroly použily uložený výsledek.

## Výslovné meze a návaznost

Winstonova kniha1984 a přesnost citátu nebyly nezávisle
bibliograficky ověřeny. Poslední komentář o „any border“
zde není vydáván za obecnou větu, že každý obvod každé HC
sítě musí být volný. Samotný hlavní text výslovně připouští
výjimky a následující úlohy je analyzují. Přesný zamýšlený
rozsah této neformální obecné formulace zůstává partial,
bez nálezové karty; všechny tři matematické části49 a jejich
konkrétní tištěné mezikroky jsou uzavřeny.
