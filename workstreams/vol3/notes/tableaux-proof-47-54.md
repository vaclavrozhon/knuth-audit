# Tableaux47–54: jednotlivé argumenty, včetně úlohy2

Navázání na dříve uložený draft, nyní dokončený a spárovaný se sazbou
47–54/file58–65 a úlohou2 na65, odpovědí607. Dřívější ruční příklady
se přebírají; nové odvození doplňuje zejména rozhraní I/D, oba směry
inverznosti a úplnou indukci symetrie. Žádný výpočtový běh.

Errata: sources/tableaux-errata-review.json obsahuje všechny pět vrstev
včetně kontextu prvního vydání. Zde zohledněna oprava50 z21.4.2019:
v konstantní pracovní paměti je třeba uchovávat také i. Opravy52
„poof/proof“, doplnění54 o nezávislosti sloupců dvouřádkového zápisu
a název Corollary B nejsou nálezy. Historické atribuce Young/Rothe,
Youngova práce1928 a uvedené Saganovo vydání nebyly znovu ověřovány;
jde o výslovnou bibliografickou výjimku, nikoli matematický argument.

## Definice a deset malých případů — P0384–386

Tablo(1) má řádky(1,2,5,9,10,15), (3,6,7,13), (4,8,12,14), (11).
Délky jsou6,4,4,1 a všechny prvky1,…,15 se vyskytují jednou. Sloupce
jsou(1,3,4,11), (2,6,8), (5,7,12), (9,13,14), (10), (15), tedy spolu
s řádky striktně rostou. Tím je ověřena definice i uvedený tvar.

Permutace je involuce právě tehdy, když každý její cyklus má délku1
nebo2: druhá mocnina k-cyklu je identita právě pro k|2. Pro čtyři prvky
je tedy jedna identita, binom(4,2)=6 jednotlivých transpozic a3 párování
do dvou transpozic. To je přesně deset vytištěných permutací(2).

Všechny tvary se čtyřmi buňkami jsou(4),(31),(22),(211),(1111).
První a poslední mají jedno vyplnění. V(31) lze dolní buňku zvolit
libovolně z2,3,4, zbytek řádku je vynucen; transpozice dává tři vyplnění
tvaru(211). V(22) musí být1 vlevo nahoře,4 vpravo dole a2,3 mohou být
ve zbývajících dvou buňkách oběma způsoby. Celkem1+3+2+3+1=10.

Převzaté ruční vložení každé vytištěné involuce dává následující P=Q
(lomítko odděluje řádky), ve stejném pořadí jako(2) a(3):

| Permutace | Tableau P=Q |
|---|---|
|1234|1234|
|2134|134/2|
|3214|14/2/3|
|4231|13/2/4|
|1324|124/3|
|1432|12/3/4|
|1243|123/4|
|2143|13/24|
|3412|12/34|
|4321|1/2/3/4|

Obecná rovnost počtů není odvozena z této tabulky; plyne až z P0405.

## Sentinely a Algorithm I — P0387–391

Algoritmy používají různé kladné celočíselné prvky,0 nahoře/vlevo
a∞ v chybějících buňkách. Relaci z(6) zde označím ≺: a≺b právě pro
a<b nebo a=b=0 nebo a=b=∞. Není to neostré uspořádání běžných klíčů:
rovnost konečných kladných prvků povolena není. Podmínky(7) tak přesně
vyjadřují striktní růst uvnitř konečné Youngovy oblasti, její levé
zarovnání a neklesání∞ směrem doprava/dolů. Pro libovolné konečné
uspořádané množiny klíčů se lze do kladných celých čísel převést podle
pořadí; tento převod zachovává všechny porovnávané vztahy.

**I1/I2.** Nechť původní první řádek má délku w. Na začátku i=1,
j=w+1, nad buňkou je0<x_1 a v buňce∞>x_1. Obecný invariant při I2 je

    P_(i−1),j < x_i < P_i,j,    x_i není v aktuálním tableau.

Při posunu j←j−1 platí x_i<P_i,j z testu. Hodnota nad novou buňkou
je nejvýše hodnota nad starou buňkou, tudíž stále menší než x_i.
Při j=1 test x_i<P_i,0 nemůže uspět, protože x_i>0=P_i,0.
Po zastavení není možné x_i=P_i,j−1, neboť x_i chybí; tedy

    P_i,j−1 < x_i < y=P_i,j ≺ P_i,j+1,
    P_i−1,j < x_i < y=P_i,j ≺ P_i+1,j.

**I3/I4.** Náhrada y hodnotou x_i zachovává všechny čtyři sousední
nerovnosti. Jiná buňka se nemění a x_i nikde neduplikuje klíč.
Pokud y<∞, po i←i+1 je nad sledovanou buňkou právě x_i<y, pod ní
v původním řádku bylo něco většího než y; y je nyní jediný přenášený
chybějící klíč. To je invariant dalšího I2. Pokud y=∞, nová konečná
buňka má napravo a dole∞, protože oba sousedé před náhradou splňovali
∞≺soused. Je tedy vnějším rohem(8). Nad ní a vlevo jsou přípustné
menší hodnoty; tvar zůstává partition shape.

**Konec, cesty, cena.** V každém navštíveném řádku se nahradí právě
jedna hodnota. Přenášené hodnoty jsou striktně rostoucí x_1<…<x_s<∞;
j se pouze zmenšuje, proto r_1≥…≥r_s. Nejpozději v původně prázdném
řádku h+1 se narazí na∞ a skončí. Jen poslední náhrada mění tvar,
každá jiná přesouvá původní klíč; výsledná množina je původní plus x.
Prázdné tableau má w=h=0 a vloží x do(1,1).

Při přímém přístupu k buňkám/sentinelům je celkem nejvýše w posunů
vlevo a h+1 řádkových kroků, tedy O(w+h+1) času, včetně lineárního
nalezení počátečního j, pokud délka řádku není uložena. Pro vlastní
výpočet stačí aktuální i,j,x_i,x_(i+1), tedy O(1) slov, kromě tableau
a přidělení nové buňky. Celé posloupnosti(9),(10) nejsou potřeba.
Toto je přesný RAM předpoklad, nikoli bitový nebo libovolný paměťový model.

Příklad(4)→(5) přebíráme: vložení8 vytlačuje9,10,13,∞ ve sloupcích
4,3,2,2. Řádky výsledku jsou(1,3,5,8,12,16), (2,6,9,15),
(4,10,14), (11,13), (17). Na každém kroku je vytlačen první větší
prvek daného řádku; nová buňka je(4,2). Souhlasí oba tištěné seznamy
cesty i všechny hodnoty výsledného obrázku.

## Algorithm D a přesná inverznost — P0392–396

**D1/D2.** Vstup je neprázdné tableau a vnější roh(s,t) splňující(8).
Přenášené y=x_(s+1)=∞ chybí v sentinelovém smyslu; P_s,t<∞≺P_s+1,t.
Obecný invariant D2 je

    P_i,j < y=x_(i+1) ≺ P_i+1,j,    y není v aktuálním tableau.

Jestliže pravý soused je<y, lze j zvětšit: nová sledovaná buňka je<y
podle testu a nový dolní soused není menší než původní. Invariant
zůstává. Posun skončí, protože∞<y neplatí ani při y=∞. Sledovaná
buňka je proto konečná a kladná. Vybrané j je jediné místo, kde

    P_i,j=x_i < y ≺ P_i,j+1.

**D3/D4/D5.** Vlevo i nahoře je hodnota menší než x_i<y; napravo
a dole jsou hodnoty≻y. Náhrada x_i za y tedy opět zachová tableau
a x_i se stane jedinou přenášenou chybějící konečnou hodnotou. Pro
řádek i−1 je jeho sledovaná buňka<x_i<y, přičemž y nyní stojí dole;
to obnovuje D2 po posunu nahoru. Při i=1 se vrátí kladné konečné x_1.
Jen první náhrada za∞ odstraňuje roh, ostatní náhrady tvar nemění.
Algoritmus prochází přesně s řádků a j se pouze zvětšuje; celkový
počet posunů doprava je nejvýše w−t, čas O(s+w−t+1), pracovní prostor
O(1) slov ve stejném přístupovém modelu. Pro singleton vrátí jeho
prvek a prázdné tableau. Pro prázdné tableau chybí vstupní roh,
takže nejde o přípustný vstup D, nikoli o chybu ukončení.

Příklad opačné cesty: z rohu(4,2) se odstraní13; v řádku3 je největší
prvek<13 hodnota10, v řádku2 je největší<10 hodnota9, v řádku1 je
největší<9 hodnota8. Náhrady obnoví celé(4) a vrátí8.

**I pak D.** Po I je v řádku i, sloupci r_i hodnota x_i a pravý
soused je≻x_(i+1); všechny buňky vlevo jsou<x_i. D přenášející
x_(i+1) proto musí vybrat právě r_i jako poslední pozici s hodnotou
<x_(i+1). Začíná nejvýše v tomto sloupci, protože r_(i+1)≤r_i;
v posledním řádku začíná přímo v r_s. Indukce od s dolů k1 obnoví
každý původní x_(i+1), včetně posledního∞, a vrátí původně vložené x_1.
Jiný řádek během takového kroku ještě není dotčen, takže unikátní
volbu sloupce nemůže znehodnotit dřívější krok.

**D pak I.** Označme odebrané hodnoty/sloupce D jako x_i,r_i. Po D
stojí v r_i hodnota x_(i+1), vlevo jsou hodnoty<x_i. První prvek
větší než x_i je proto právě v r_i. I začne v řádku1 v prvním∞,
tedy napravo od něj nebo přímo v něm; v dalším řádku začíná v
r_(i−1)≥r_i. Skenování doleva proto najde r_i, vrátí x_i a přenese
x_(i+1). Indukce nahoru podle i skončí doplněním původního rohu(s,t)
a vytlačením∞. I vrátí právě(s,t), nikoli pouze stejné množství buněk.
Oba směry tak platí na celých určených doménách; nejde jen o kontrolu
jednoho příkladu nebo o jednostrannou levou inverzi.

## Theorem A a rozklad dolních řádků — P0397–400

Pro dva seznamy q_1<…<q_n a různé p_i vkládáme p_i pomocí I a do
nového rohu Q zapíšeme q_i. Indukce drží stejný tvar P,Q. Nový q_i
je větší než všechny staré prvky Q a nový roh má napravo/dole∞;
vlevo/nahoře jsou menší hodnoty. Q proto zůstává tableau. P obsahuje
přesně dosavadní p_i a Q dosavadní q_i.

Obráceně největší prvek aktuálního Q musí být vnějším rohem: konečný
soused napravo nebo dole by byl ještě větší. Odstraníme tento q_i
(nebo jej při další iteraci jen považujeme za odstraněný) a provedeme
D ve stejném rohu P. Ten existuje, protože tvary jsou shodné. D vrátí
jediný odstraněný p_i a opět shodné menší tvary. Vrácené p_i jsou
navzájem různé, protože každé skutečně zmizí z množiny P. Oba směry
I/D v předchozím oddílu indukcí dokládají vzájemnou inverzi obou
celých konstrukcí. Pro n=0 odpovídá prázdný zápis právě páru prázdných
tableaux. To dokazuje zobecněnou bijekci i specializaci Theorem A.

Příklad(12),(13), s q=(1,3,5,6,8), p=(7,2,9,5,3), má postupné stavy:

| Po vložení | P | Q |
|---|---|---|
|7|7|1|
|2|2/7|1/3|
|9|29/7|15/3|
|5|25/79|15/36|
|3|23/59/7|15/36/8|

Každý nový q je v právě přidané buňce. Při zpětném čtení rohů8,6,5,3,1
dává D postupně3,5,9,2,7 a obnovuje předchozí řádky tabulky; poslední
stav je prázdný. Tím je spárován i výslovný reverzní příklad na52.

Po vytlačení z prvního řádku se prvek již nemůže do prvního řádku
vrátit: I postupuje jen dolů. Pokračování v řádku2 volí první větší
prvek stejně jako nové nezávislé vložení do dolního tableau. Počáteční
sloupec je pouze horní mez pro toto místo; i když leží za prvním∞
kratšího řádku, I2 přes tyto∞ dojde ke stejné jediné pozici. Indukce
po vložených sloupcích proto říká: dolní P je insertion tableau
právě vytlačené posloupnosti a dolní Q zapisuje odpovídající původní
časové značky q. V příkladu je vytlačený zápis(q,p)=((3,6,8),(7,9,5))
a jeho dvojice je59/7,36/8, přesně dolní část(13). První řádek se
mění7→2→29→25→23; nové rohy v něm vznikají jen při q=1,5, což
dokládá všechny řádky(14).

## Třídy a symetrická charakterizace — P0401–403

Třída t je sloupec, do něhož se vloží p v prvním řádku. Třída1
znamená p menší než dosavadní první prvek, tedy nové prefixové minimum.
Ekvivalentně všech i−1 dřívějších prvků tvoří s p inverzi. Zde se
počítají inverze končící v p, nikoli libovolné jiné konvence.

Vynechání všech událostí třídy1 odstraní pouze první pozici řádku:
tyto události mění jen jeho první buňku. Při každé jiné události p
je p větší než aktuální první buňka a stejný test prvního většího
prvku se provede na nezměněném ocasu. Indukce po vstupních událostech
tedy identifikuje nový první řádek přesně s původním ocasem a všechny
zbývající třídy sníží o1. To není předpoklad o konečném pořadí, nýbrž
rovnost celého průběhu, včetně prázdného ocasu.

Ve třídě t se hodnota buňky P_1t mění jen při událostech této třídy
a každá nová hodnota je menší než předchozí. Jejich q rostou podle
vstupu. Pro seřazené členy(q_i1,p_i1),…,(q_ik,p_ik) proto platí(18),
finální P_1t=p_ik a Q_1t=q_i1. Každý kromě prvního vytlačí předchozí
hodnotu, takže do spodního zápisu jdou právě(q_i2,p_i1),…,(q_ik,p_i(k−1)).
Pro příklad jsou třídy1:(1,7),(3,2);2:(5,9),(6,5),(8,3).
Ve vytlačeném zápisu jsou1:(3,7),(8,5);2:(6,9). Všechny vzorce
(18)–(20) i obě konkrétní klasifikace tím souhlasí.

**Úloha2, včetně obou implikací odpovědi607.** Po každém prefixu
označme a_j nejmenší možný poslední prvek rostoucí podposloupnosti
délky j, a_0=−∞; pro neexistující délku a_j=∞. Tvrdíme, že konečné
a_j jsou právě první řádek P. Před vložením p nechť t je první index
s a_t>p. Podposloupnost končící hodnotou a_(t−1)<p se dá prodloužit
o p, takže délka t existuje (pro t=1 stačí singleton). Kdyby v p
končila délka t+1 nebo delší, její prefix délky t by skončil pod p,
tedy a_t<p, spor. Delší podposloupnosti proto nevzniknou. Pro j<t
nemůže p vylepšit minimum, protože a_j≤a_(t−1)<p. Pro j=t se minimum
stane p; pro j>t se nic nemění. To je přesně změna prvního řádku I.
Prázdný prefix spouští indukci, takže invariant platí obecně.

Vstupní q jsou vzestupné; podposloupnost tedy znamená současně
striktně rostoucí q a p. Třída t prvku(q,p) je přesně největší délka
takového řetězce končícího v něm, jak požaduje úloha2. Konstrukce
z a_(t−1) dokládá první implikaci v odpovědi; libovolný dřívější
řetězec s posledním prvkem<p dokládá opačnou. Charakterizace nepoužívá
pořadí fyzického zápisu sloupců a je symetrická v obou souřadnicích.

## Theorem B, involuce a minimum — P0404–406

Zaměňme souřadnice všech párů a seřaďme podle nové první souřadnice.
Řetězcová charakterizace třídu zachová. V každé třídě se původně
rostoucí q a klesající p nyní čtou v opačném pořadí. Proto z(19)
plyne první řádek nového P rovný starému Q a první řádek nového Q
rovný starému P. Konkrétně P'_1t=q_i1 a Q'_1t=p_ik, jak v(23).

Původní vytlačené dvojice jsou(q_i(j+1),p_ij), 1≤j<k.
Nové jsou(p_ij,q_i(j+1)), čtené podle rostoucího p_ij. To je přesně
transpozice stejné množiny dvojic; v různých třídách se jen sloučí
podle rostoucích časových značek. Vytlačené hodnoty jsou různé,
protože každý prvek může první řádek opustit jen jednou. Obě dolní
konstrukce tedy opravdu přijímají přípustné dvouřádkové zápisy,
navzájem inverzní; vzorec(24) je jejich pořadí uvnitř jedné třídy.

Úplná indukce podle počtu sloupců vstupního zápisu: pro n=0 je
tvrzení triviální. Pro n>0 je první řádek neprázdný; vytlačený zápis
má n−c<n sloupců, kde c je počet tříd. Předchozí odstavec a indukční
předpoklad zamění i celé dolní P,Q. Spolu s již zaměněnými prvními
řádky to dává Theorem B pro obecný zápis, tedy zejména pro π a π⁻¹.
Tato indukce nepředpokládá předem stejný počet řádků obou výsledků.

Theorem A je bijekce, proto π=π⁻¹ právě když jeho dvojice(P,Q) je
rovna(Q,P), tedy P=Q. Každé tableau T určuje jedinou permutaci pro
pár(T,T), která je tak involucí. To dokazuje Corollary B v obou
směrech, včetně prázdného případu, a obecný výrok ze48.

V neprázdném tableau je P_11 minimum: pro každou buňku(i,j) lze
postupovat v její Youngově oblasti nejprve po prvním řádku do j
a pak dolů do i; všechny kroky hodnotu striktně zvětšují. Jediná
buňka bez kroku je(1,1). Nápad řazení opakovaným vložením a mazáním
minima na konci54 bude uzavřen až s Algorithm S na55. Proto54 zatím
nemá celé stránkové argumentové uzavření; tento důkaz nepředbíhá S.
