# Povolené záměny, úlohy4–5 a úplné věty C/D

Rozsah: §5.1.4–4,5 na65 a odpovědi607, Theorem C55/úloha13/608,
Theorem D57 a obecná involutivita na56. Závislosti ponechané v minulém
checkpointu partial jsou zde skutečně odvozeny. Neopakuje se žádný
program ani známý protipříklad. Označení d(P) znamená jediné odstranění
minima, E(P) celou duální tabulku, v knize P^S. Kandidát C0007 se týká
právě přetížení tohoto symbolu v odpovědi13; správná matematická věta
se tím nevyvrací.

## P0421: přesný význam přípustné záměny a příklad

Pro x<y<z jsou oba možné lokální vztahy právě

    K1: x z y ↔ z x y,
    K2: y x z ↔ y z x.

Jde o prohození sousedních krajních hodnot trojice, je-li prostřední
hodnota vedle nich. Tím je pokryta levá i pravá alternativa definice
úlohy4. Ve slově1,5,4,6,8,3,7 jsou možné přesně záměny1↔5
(svědek4),4↔6(svědek5),8↔3(svědek6 nebo7). Pro dvojice5/4,6/8,3/7
žádný dovolený soused mezi hodnotami neleží; jde o všech šest hranic.

## P0422: řádkové lemma pro K1 — všechny případy

Uvažujme libovolný původní vzestupný řádek R, který neobsahuje x,y,z.
„Výstup“ řádku je posloupnost konečných vytlačených prvků; vytlačené∞
se vynechá. Dokážeme, že dvě trojice z K1 vytvoří stejný nový řádek
a jejich výstupy jsou stejné nebo samy tvoří jeden vztah K1/K2.

Označme a první původní prvek>x a c první původní prvek>z, případně∞.

1. Je-li a<z, leží jeho pozice před c. Pořadí x,z tak vytlačí a,c,
   pořadí z,x vytlačí c,a. Obě náhrady jsou na různých pozicích
   a vytvoří stejný řádek před vložením y. Třetí výstup je stejný
   prvek v. Konkrétně v=min(z, první prvek>y po samotném vložení x).
   Platí a<v≤z<c: pro a<y je to zřejmé; pro a>y byl
   a odstraněn a další kandidát i z jsou>a. Proto výstupy
   (a,c,v) a(c,a,v) jsou K1. Pokud c=∞, po jeho vynechání jsou
   oba výstupy jednoduše(a,v).
2. Je-li a>z, včetně a=∞, je a=c. Označme d následující původní
   prvek nebo∞. Přímé tři kroky x,z,y vytlačí(a,d,z), zatímco
   z,x,y vytlačí(a,z,d). Pro konečná a,d je z<a<d, tedy jde o K2.
   Je-li jen d=∞, oba konečné výstupy jsou(a,z); je-li i a=∞,
   oba jsou(z). Tím jsou zahrnuty i krátký a prázdný řádek.

V obou případech jsou množiny výstupů stejné. Nový vzestupný řádek
má množinu R∪{x,y,z} minus tuto množinu výstupů, a proto je stejný.
Zde se nekonečno nikdy nevydává za skutečný vstupní klíč.

## P0423: řádkové lemma pro K2

První vložení y je společné a vytlačí b=min{r∈R:r>y}, případně∞.
V novém řádku označme a první prvek>x a c první prvek>z. Přítomnost
y zaručuje a≤y. Pro konečné b dále platí a<b<c: pokud bylo b>z,
bylo odstraněno a c je až jeho následník; pokud bylo b<z, c leží
až za ním. Je-li b=∞, také c=∞.

Následující vložení x,z zasahují různá místa, protože a≤y<z<c,
a tedy na úrovni řádku komutují. Celé výstupy jsou(b,a,c) a(b,c,a),
což je K2 při konečných b,c. Pokud c=∞, oba konečné výstupy jsou(b,a);
při b=c=∞ jsou oba(a). Výsledný řádek je opět stejný. Nezůstává
žádný případ podle délek mezer v řádku: zachytily jej první větší
prvky a výslovné varianty∞.

## P0424: úloha4(a), od jednoho řádku k celému tableau

Před zaměňovanou trojicí byl zpracován stejný prefix, tedy máme
stejné počáteční tableau T. P0422–423 dají stejný první řádek a pro
dolní řádky buď stejnou posloupnost, nebo další K1/K2 na třech různých
prvcích. Ty v dolním původním tableau chybějí, protože všechny klíče
celého vstupu jsou různé. Indukce podle počtu původních řádků tedy
prokáže stejný výsledek dole. V původně prázdném řádku jsou oba
výstupy již stejné, jak výslovně zahrnují řádková lemmata, takže
indukce má platný základ i při zvětšení výšky.

Zbytek vstupního slova se pak zpracuje ze stejného tableau stejně.
Povolená záměna kdekoli ve slově proto P nemění. To je obecný důkaz
pro libovolný prefix, nikoli jen shoda obou holých trojic.

## P0425–426: úloha4(b), konstruktivní kanonická reprezentace

Pro jeden vzestupný řádek R a nový x je při nevytlačení konečného
prvku Rx už správný nový řádek. Jinak napišme R=A b B, kde b je
první prvek>x; každý prvek vzestupného A je<x<b a každý prvek B je>b.
Platí konkrétní konečná posloupnost dovolených vztahů

    A b B x  ~  A b x B  ~  b A x B.

První krok posouvá x doleva přes B: v každé trojici u v x je
x<u<v a K2 ji mění na u x v; posledním svědkem je b. Druhý posouvá
b doleva přes A: nejprve a b x→b a x pro a<x<b, potom postupně
c b a→b c a pro c<a<b. Oba kroky mohou být prázdné, je-li příslušný
seznam prázdný. Výsledkem je bR', kde R' je právě řádek po vložení x.

Nechť W(T) jsou řádky T čtené zespodu nahoru, každý zleva doprava.
V W(T)x aplikujme předchozí faktorizaci nejprve na poslední, horní
řádek. Vytlačený b se nyní ocitne hned za předchozím řádkem, takže
na něj lze použít totéž lemma. Pokračováním přes všechny vytlačené
řádky dostaneme přesně W(I(T,x)); nevytlačený konečný prvek ukončí
řetězec, nebo vznikne nový spodní řádek. Indukce po vstupním slově
tedy konstruktivně dává w~W(P(w)). Dvě slova se stejným P mají
stejný kanonický zápis, a tudíž jsou spojena přípustnými záměnami.

Používám obvyklý reflexivní uzávěr, tedy dovoluji také nulový počet
záměn, je-li slovo již stejné. Pro dvě různé permutace je spojovací
posloupnost neprázdná, jak říká úloha. Doslovné požadování „one or
more“ i pro tutéž jednoprvkovou permutaci by bylo jen hraniční
formulací, nikoli vadou dokázané ekvivalence; nezakládám z toho kartu.

Příklad odpovědi607 není třeba enumerovat: do horního řádku
(1,3,5,9,12,16) se připojí8 a lemma vytlačí9; další řádky
(2,6,10,15), (4,13,14), (11) postupně vytlačí10,13 a nic.
Kanonický zápis tak přejde z

    17 | 11 | 4 13 14 | 2 6 10 15 | 1 3 5 9 12 16 | 8

na

    17 | 11 13 | 4 10 14 | 2 6 9 15 | 1 3 5 8 12 16,

přesně jak je vytištěno. Každá z uvedených faktorizací má výše
explicitně popsány dovolené lokální záměny.

## P0427: úloha5, reverze slova dává transpozici

Reverze K1 je K2 a reverze K2 je K1. Z w~W(T) proto plyne
w^R~W(T)^R. Zbývá skutečně dokázat, co vytvoří vložení W(T)^R;
samotné označení „canonical“ to nedokazuje.

Obecně lze tableau U vytvořit čtením jeho sloupců zleva doprava,
každého zdola nahoru. Před přidáním nového sloupce délky l jsou
všechny předchozí sloupce již hotové. Označme nové hodnoty shora
c_1<…<c_l. Vložíme je v pořadí c_l,…,c_1. Po k vloženích obsahuje
nový sloupec v prvních k řádcích c_(l−k+1),…,c_l; staré sloupce
jsou nedotčené. Při dalším vložení se změny šíří jen tímto sloupcem:
v řádku r je přenášený c_(l−k+r−1)≥c_r větší než všechny staré
prvky řádku, ale menší než současný nový prvek. Vytlačí jej do
dalšího řádku, kde platí stejný vztah. Po l vloženích je sloupec
správně c_1,…,c_l. Pro první sloupec jsou staré řádky prázdné;
pro další jejich potřebná délka existuje z Youngova tvaru.

Slovo W(T)^R je právě tento sloupcový zápis T^T: řádky T se čtou
shora dolů, každý zprava doleva. Proto P(W(T)^R)=T^T. Invariance
P0424 dává P(w^R)=T^T. Tím je doplněn i implicitní mezikrok odpovědi5.

## P0418 doplněn: Theorem C a oba případy odpovědi13

Relabelujme prvky pořadím na1,…,n. Pro n≤1 je tvrzení přímo z S.
Indukční předpoklad je Theorem C pro všechna kratší slova.

**Dvojka před jedničkou.** Dokud není vložena1, zůstává2 prvním
prvkem prvního řádku: žádný dosud vložený prvek ji nemůže vytlačit.
Vložení1 právě nahradí2 hodnotou1 a vytlačí2. Porovnejme slovo
s jedničkou a slovo bez ní. Od tohoto okamžiku se jejich první řádky
liší jen první buňkou1 versus2; všechny další vstupy jsou>2 a mění
stejným způsobem stejný zbytek řádku. Jejich vytlačené posloupnosti
se liší jen přítomností2, nejmenšího prvku původní vytlačené posloupnosti.

Dolní tableau původního výsledku má2 v rohu(2,1), jako minimum.
Proto d při prvním kroku přesune2 nahoru (každý pravý kandidát je>2)
a potom provede přesně d na dolním tableau. Podle indukce se dolní
část tím změní na insertion tableau vytlačeného slova bez2. To je
právě dolní část konstrukce pro celé vstupní slovo bez1. První řádky
už byly ztotožněny, takže tvrzení platí.

**Dvojka za jedničkou.** V obráceném vstupním slově je dvojka před
jedničkou. Právě dokázaný první případ proto lze aplikovat na toto
slovo téže délky: jeho důkaz používá pouze indukci pro kratší slova,
takže nevzniká kruh. P0427 identifikuje jeho tableau s P^T, a stejně
tak pro slovo po vynechání1. Jelikož d komutuje s transpozicí podle
P0416, transpozice výsledné rovnosti d(P^T)=P(w bez1)^T dává
d(P)=P(w bez1). Oba případy odpovědi13 jsou tím úplně odvozeny.

## P0428: vynechání největšího prvku z vloženého slova

Je-li M největší klíč ve zvoleném pořadí, pak vynechání M ze vstupu
jen odstraní buňku M z výsledného tableau. Důkaz indukcí po prefixu:
samotné vložení M pouze přidá M na konec prvního řádku. Při každém
dalším vložení x jsou cesty v tableaux s M a bez M stejné, dokud
případně zasáhnou jeho buňku. M i odpovídající∞ jsou větší než
všechny přenášené konečné klíče, takže žádné dřívější rozhodnutí se
nemění. Bez M cesta v této buňce končí; s M vytlačí M do dalšího
řádku, kde se pouze připojí na konec, protože je největší. Ostatní
buňky jsou v obou případech stejné. M vždy leží v rohu. Tím je
dokázán důležitý krok na57; tvrzení „M samo nic nevytlačí“ by bez
této kontroly dalších vložení samo nestačilo.

## P0429–431: každý krok Theorem D

Označme A změnu pořadí časových značek q na opačné a příslušné
obrácení pořadí sloupců vstupu; B změnu pořadí hodnot p na opačné.
Jsou to dvě nezávislé operace, každá provedená dvakrát je identita.
Nezaměňujme toto pomocné označení operací s dřívějšími názvy vět.

P0427 už dokládá, že A mění první tableau na P^T; druhé zatím
označme X. Symetrie dvojice při inverzi biwordu (Theorem B na53–54)
pak říká, že B dává dvojici(Y,Q^T), kde Y má tvar P^T. Tato aplikace
platí pro libovolná dvě úplná pořadí: předchozí důkaz používá pouze
porovnání a lze jej přeznačit podle pořadí. Žádný vzorec pro E se
v tomto kroku ještě nepředpokládá.

Nyní dokážeme Y=E(P)^T indukcí po n. Pro n=0 je to prázdný pár.
Nechť a je nejmenší hodnota p v původním pořadí, tedy největší
v opačném. Vynecháním a ze vstupu dostaneme v původním pořadí d(P)
podle právě dokázané věty C. V opačném pořadí dostaneme Y minus a
podle P0428. Indukční předpoklad tedy dává

    Y minus a = E(d(P))^T.

Definice celé dualizace E nejprve uloží a do rohu odstraněného při
d(P), potom vytvoří E(d(P)) ve zbytku tvaru. Proto přesně platí

    E(P)^T minus a = E(d(P))^T,

což je identita(29). Y a E(P)^T mají stejný celý tvar P^T a shodují
se po odebrání stejného prvku a, tudíž chybějící a musí ležet v téže
jediné buňce. To dokazuje část(b). Opětovná aplikace symetrie biwordu
dává část(a): dvojici(P^T,E(Q)^T).

Pro obě změny pořadí nejprve použijeme(a), pak(b). Dostaneme

    ( E(P^T)^T, (E(Q)^T)^T ) = (E(P),E(Q)),

protože E komutuje s transpozicí podle P0416. To je část(c), včetně
obou komponent. Odtud také plynou dvě závěrečná tvrzení57: reverzní
vložení dává P^T a reverzní vložení s opačnými porovnáními dává E(P).
Sentinely se současně vymění, aby zůstaly krajními prvky zvoleného
pořadí; původní kladné klíče se nemění.

## P0420 doplněn: plná involutivita a jednoznačnost

Proveďme operaci(c) dvakrát, pokaždé v aktuálně používaném pořadí.
Obě změny pořadí i reverze sloupců se vyruší, takže se vrátí původní
biword a jeho jediná dvojice(P,Q). Výsledek na straně tableaux je
(E_dual(E(P)),E_dual(E(Q))), tedy E_dual(E(P))=P. Každé tableau P
se v nějaké dvojici vyskytuje (například(P,P) v Theorem A), proto je
závěr obecný, nikoli jen pro zobrazený šestnáctiprvkový příklad.
E je tedy jednoznačně vratná duálním opakováním téhož algoritmu,
včetně prázdného tableau. Všechna tvrzení o C/D a involutivitě,
dříve P0418–0420 partial, jsou nyní doložena.

Převzata kontrola všech pěti vrstev errat pro tento úsek; nová chyba
ani výpočtový běh nevznikly. Historické atribuce Schensted/Schützenberger
jsou stále výslovnou bibliografickou výjimkou.
