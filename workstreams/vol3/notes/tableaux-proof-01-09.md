# Tableaux, zbývající argumenty k úlohám 1–9

Zadání64–66/file75–77, odpovědi607–608/file618–619. Původní sazba
pro oba ruční příklady a celý konec odpovědí byla zobrazena v
images/tableaux-file-075.png, -076.png a images/runs-file-618.png.
Nejde o nové běhy algoritmů; následují krátké ruční stavy a obecné důkazy.
Známá errata se přebírají z sources/tableaux-errata-review.json;
novější vrstvy neobsahují změnu zde kontrolovaných úloh1–9.

Úloha2 je již v P0403, úlohy4(a,b) v P0421–P0426, úloha5 v P0427
a úloha7 v P0453. Jejich obecné důkazy se nepřepočítávají. Zejména
pro úlohu4(b) je už výslovně zachycen reflexivní případ nulového
počtu záměn; nevrací se nyní tiše k silnější doslovné interpretaci.

## P0477: úloha1, dopředný příklad

Vkládáme p=(6,4,9,5,7,1,2,8,3), s q=1,…,9. Lomítka oddělují řádky.
Algoritmus I a pravidlo Q jsou obecně doloženy v P0387–P0397;
zde každé vytlačení i nový roh kontrolují tyto konkrétní stavy:

| q | Nové P | Nové Q |
|---|---|---|
|1|6|1|
|2|4 / 6|1 / 2|
|3|4 9 / 6|1 3 / 2|
|4|4 5 / 6 9|1 3 / 2 4|
|5|4 5 7 / 6 9|1 3 5 / 2 4|
|6|1 5 7 / 4 9 / 6|1 3 5 / 2 4 / 6|
|7|1 2 7 / 4 5 / 6 9|1 3 5 / 2 4 / 6 7|
|8|1 2 7 8 / 4 5 / 6 9|1 3 5 8 / 2 4 / 6 7|
|9|1 2 3 8 / 4 5 7 / 6 9|1 3 5 8 / 2 4 9 / 6 7|

Například při q=6 jdou dolů4,6,∞; při q=7 jdou dolů5,9,∞;
při q=9 pouze7,∞. Finální dvě tableaux přesně souhlasí s odpovědí607.

## P0478: úloha1, inverzní příklad a celé přiřazení klíčů

Počáteční P=(1 4 7)/(2 8)/(5 9), Q=(1 3 7)/(4 5)/(8 9).
Odstraňujeme největší zbývající q a ve stejném rohu spouštíme D.
Jeho obousměrná inverznost je v P0395–P0398; konkrétní reverzní kroky:

| Odstraněné q | Roh | Vrácené p | Zbylé P |
|---|---|---|---|
|9|(3,2)|7|1 4 8 / 2 9 / 5|
|8|(3,1)|1|2 4 8 / 5 9|
|7|(1,3)|8|2 4 / 5 9|
|5|(2,2)|4|2 9 / 5|
|4|(2,1)|2|5 9|
|3|(1,2)|9|5|
|1|(1,1)|5|prázdné|

První dva přenášené řetězce jsou9→8→7 a5→2→1; všechny další
mají nejvýše jeden mezilehlý řádek. V každém řádku se bere poslední
prvek menší než přenášená hodnota, nikoli pevný sloupec z Q.
Ve vzestupném q pořadí proto vyjde přesně

    q: 1 3 4 5 7 8 9
    p: 5 9 2 4 8 1 7.

Tím jsou obě části úlohy1 uzavřeny včetně skutečných nesouvislých
množin štítků; nelze je zaměnit za standardní permutaci délky9.

## P0479: úloha3, invariant jedné generované linky a ukončení

V lince k ignorujme prázdná místa a∞. Zbývá posloupnost různých
celých klíčů v pořadí původních časových značek. V jednom průchodu
od (a) se vybírají její postupná prefixová minima: první zbývající
prvek, pak první menší, pak první ještě menší atd. Přestože (b)
výslovně hledá zleva v celé lince, nikdy se v tomto průchodu nevrátí
do levějšího sloupce. Každý dříve přeskočený prvek byl větší než
tehdejší p, a tedy i než právě snížené p.

Po odstranění tohoto průchodu se najdou prefixová minima zbylé
posloupnosti. Podle P0401 odstranění prvních minim odstraňuje právě
první buňku průběžného insertion řádku; opakování proto vybírá přesně
třídu2, třídu3 atd. Ve třídě (q_1,p_1),…,(q_h,p_h), q rostou
a p klesají. Krok(c) zapíše do první pozice∞ a do dalších pozic
p_1,…,p_(h−1). To jsou přesně klíče vytlačené při změnách jediné
buňky dané třídy, včetně prvního vytlačeného∞.

Každé(c) vyplní dosud prázdné místo pod jedním konečným vstupem.
Je-li ještě nevyplněný vstup, restart s p=∞ jej nakonec najde.
Žádný restart nemůže běžet bez následného zápisu nebo ukončení.
Jedna linka tedy končí po přesně M zápisech pro M konečných vstupů.
Vytlačených konečných prvků je M−s, kde s≥1 je počet tříd, je-li
M>0. Počet konečných prvků při přechodu dolů přísně klesá, takže
celá konstrukce skončí. Pro M=0 skončí bez zápisu; prázdný vstup
také dává prázdná tableaux. Kniha zde žádnou zvláštní časovou mez
pro doslovné hledání v(b) netvrdí.

## P0480: úloha3, čtení obou tableaux a sloupců

Konečný výstup z první linky je právě bumped array z P0400. Indukce
podle k tedy ztotožní každou další linku s prvky přicházejícími do
k-tého insertion řádku při stejných původních q. Každý sloupec je
celý řetězec vytlačených hodnot jedné původní operace I až do∞;
další políčka v tomto sloupci zůstávají prázdná.

Prvky, které se objevily v lince k, ale nebyly vytlačeny do k+1,
jsou přesně finální obsah k-tého řádku P. Do řádku se řadí vzestupně;
samotné jejich pořadí ve vstupních sloupcích nemusí být vzestupné.
Výstup∞ v lince k+1 znamená, že dané vložení skončilo novou buňkou
v řádku k. Zapsané původní q jsou proto přesně k-tý řádek Q,
v rostoucím pořadí. Tím jsou odvozeny všechny instrukce čtení za
algoritmem i tvrzení odpovědi607, nikoli jen shoda příkladu.

## P0481: všechna políčka tabulky úlohy3

Na lince1=(7,2,9,5,3) jsou první dvě třídy7→2 a9→5→3; výstupní
linka2 je tedy(∞,7,∞,9,5). Konečná část linky2 má třídy7→5 a9,
což dává na lince3 hodnoty∞ ve sloupcích q=3,6 a7 ve sloupci q=8.
Poslední linka4 má pouze∞ pod q=8. To jsou všechna vytištěná
políčka, včetně prázdných. Čtení dává P=2 3 / 5 9 / 7 a
Q=1 5 / 3 6 / 8, shodně s již doloženým příkladem P0400.

## P0482: úloha6, parita každé třídy involuce

Předpokládáme involuci na konečné lineárně uspořádané množině
štítků; nemusí to být interval celých čísel. Její množina dvojic
je invariantní při záměně souřadnic. Třída je určena maximální
délkou rostoucího řetězce (P0403), a je proto také invariantní.
V každé třídě lze označit první souřadnice a_1<…<a_h. Druhé jsou
stejná množina, ale klesají, tedy celá třída je přesně

    (a_1,a_h), (a_2,a_(h−1)), …, (a_h,a_1).

Obsahuje jeden pevný bod právě tehdy, když h je liché, a jinak
žádný. Má-li involuce k pevných bodů a celkem s tříd, právě k tříd
má lichou velikost. To zdůvodňuje první větu odpovědi i její
zobrazený obecný tvar; není třeba předpokládat jej z obrázku.

## P0483: úloha6, skutečná involuce ve vytlačeném zápisu

Z předchozí třídy se podle P0401–P0404 vytlačí právě dvojice

    (a_(j+1),a_(h+1−j)), 1≤j<h.

Jde znovu o symetrickou obrácenou posloupnost, nyní na množině
{a_2,…,a_h}. Pro h sudé má jeden pevný bod, pro h liché nemá žádný.
Různé původní třídy používají disjunktní množiny štítků, takže celý
vytlačený zápis je involuce na sjednocení těchto zmenšených množin
a má přesně s−k pevných bodů. Její nové třídy nemusí být původní
třídy; důkaz je na tom nezávislý. Má n−s<n prvků pro n>0, což
opravňuje indukci i pro nesouvislou množinu štítků.

## P0484: úloha6, dokončení indukce a nulové dolní sloupce

Pro n=0 je tvrzení triviální. Pro n>0 je první řádek délky s.
Dolní tableau je insertion tableau vytlačené involuce (P0400),
takže z indukce má s−k sloupců liché délky. Počítejme jeho sloupce
na všech s pozicích prvního řádku: chybějící dolní sloupce mají
délku0, tedy sudou. Vrácením první buňky se na všech s pozicích
parita obrátí. Celé tableau má proto s−(s−k)=k lichých sloupců.
Tím jsou pokryty i jednoprvková involuce a identita (samé sloupce
délky1), nikoli jen tvar s neprázdným druhým řádkem.

## P0485–P0486: úloha8, mez a její ostrost

Podle P0453 jsou počty řádků a sloupců insertion tableau přesně
délky nejdelší klesající a rostoucí podposloupnosti. Pokud jsou
obě nejvýše n, vejde se tvar do n×n a má nejvýše n² buněk.
Více než n² prvků proto vynutí jednu délku>n.

Ostrost pro n≥1 dokládá konkrétní permutace tvořená n bloky délky n:

    n,n−1,…,1 | 2n,2n−1,…,n+1 | … | n²,…,n²−n+1.

Rostoucí podposloupnost může vzít nejvýše jeden prvek z každého
bloku; klesající nemůže přejít do dalšího bloku, kde jsou všechny
hodnoty větší. Obě meze jsou tedy n a obě jsou dosažitelné.
Pro n=0 je ostrým případem prázdná permutace; jakákoli neprázdná
má monotónní podposloupnost délky1. Argument v odpovědi přes existenci
čtvercového tableau je rovněž úplný díky obousměrné RSK bijekci,
nikoli pouhé existenci nějakého obrázku.

## P0487: úloha9, čtverec a obě vytištěné formule

Máme přesně n² prvků. Obě délkové meze≤n tedy určují přesný tvar
n×n: jiný podtvar obdélníku by měl méně buněk. Theorem A přiřazuje
permutaci nezávisle volitelnému páru(P,Q) tohoto tvaru, takže počet
je f_(n^n)²; nesmí se zaměnit s počtem samotných tableaux či involucí.

Z již doloženého rozměrového vzorce P0437–P0438 je

    f_(n^n)=(n²)! Δ(2n−1,2n−2,…,n) / ∏_(j=0)^(n−1)(n+j)!.

Háček buňky(i,j) má délku2n−i−j+1. Pro délky h=1,…,n je
počet buněk h, pro h=n+1,…,2n−1 je počet2n−h. Součin háčků je
proto přesně

    (2n−1)(2n−2)² … n^n (n−1)^(n−1) … 1.

Theorem H (P0443) tak převádí první tištěný zlomek na druhý;
umocnění na druhou dává odpověď607. Pro n=1 je počet1; prázdné
součiny při n=0 opět dávají jedinou prázdnou permutaci.

## P0488: pokračování odpovědi608, obecný obdélník

Pro přesně mn prvků a meze LIS≤m, LDS≤n musí být tvar právě
obdélník s n řádky a m sloupci. Stejný bijektivní argument a
rozměrový vzorec dávají

    počet = ((mn)! ∏_(j=0)^(n−1) j!/(m+j)!)².

Vandermonde totiž pro délky m+n−1,…,m je ∏_(j=0)^(n−1)j!.
Vzorec je symetrický v m,n díky součinu háčků nebo transpozici;
nemá skrytý předpoklad m≥n. Prázdný obdélník dává počet1.
To ověřuje také obecné tvrzení v první větě strany608.

Historické atribuce Schützenberger, Schensted a Erdős–Szekeres
a bibliografický údaj1935 nebyly znovu ověřovány; matematická
tvrzení mají výše vlastní argumenty. Celá strana66 ani608 tímto
blokem uzavřena není: následují další úlohy a části odpovědí.
