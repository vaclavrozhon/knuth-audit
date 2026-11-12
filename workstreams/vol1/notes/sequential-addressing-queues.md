# §2.2.2-3–8: adresace, ukázka a kruhové fronty

## Rozšířená adresa a obecný důkaz algoritmu A

Rozšířená adresa je trojice(a,i,j): vezme se číselná adresa a, aplikuje
modifikace i a poté j. Modifikace0 nic nemění, modifikace1..6 přičítá
příslušný indexový registr a modifikace7 načítá adresní trojici z buňky
na dosavadní adrese a rekurzivně ji vyhodnotí. Výsledky jednotlivých
adresních modifikací musejí zůstat v rozsahu dvoubajtového indexu.

Doslovný vyhodnocovač udržuje dosud neprovedené modifikace jako seznam:
7 nahradí adresu obsahem načteného slova a jeho dva modifikátory připojí
před čekající seznam. Tím je definice přímo provedena; obecně může seznam
růst. Příklad odpovědi5(a) byl takto celý rekonstruován, včetně výsledku1007.

Omezí-li se7:7 na hlavní instrukci a v nepřímo načtených slovech se zakáže,
čekající seznam má tvar skupiny obyčejných přírůstků následované nejvýše
jednou7. Obyčejné přírůstky mohou být sečteny do H a poslední7 určena
bitem N. A2 před nepřímým čtením provede preindex, postindex přidá do H;
A3 pokračuje nepřímým čtením. Na konci řetězu přičte H a vynuluje jej.
A4 buď vykoná poslední čekající7, nebo vrátí výsledek. Tento invariant
dokazuje algoritmus pro všechny končící platné výpočty pod původním
omezením. Obyčejný nekončící cyklus je výslovně dovolen a demonstruje
jej úloha4(a); omezení zásobníku záruku ukončení neslibuje.

Mírnější pravidlo5(c) dovolí více čekajících7, uchovaných počitadlem N,
ale nesmí se ztratit dosud čekající postindexy při resetuH vA2. Dostatečné
syntaktické omezení z odpovědi vylučuje7:7 vnořené pod7:j s1≤j≤6.
Ještě slabší sémantická podmínka je H=0 při každém takovém resetu.
Například LDA Y,7:7 s Y obsahujícím NOP X,7:7 pak provede tři
požadované dereference. Vícenásobné7 jsou representovány jediným čítačem.
Pokud předpoklad porušíme, dodaný přesný příklad vrátí103 místo104;
nejde o chybu odpovědi, která tuto výjimku výslovně uvádí.

## Úlohy3 a4 a jejich časy

3(a): LD1 I; LDA BASE,7:1 provede načtení indexu a potom dereferenci
základny plus index. Obě instrukce trvají2u, jedna nepřímá modifikace
přidá1u, celkem5u. Původní dva různé způsoby na246 trvají4u a8u.
3(b): LDA BASE,2:7 načte základnu J-té tabulky; má-li tato buňka
modifikátor0:1, rovnou přičte I. Alternativní pomocné X2 obsahuje
NOP BASE,2:7 a hlavní LDA X2,7:1 dělá jeden nepřímý krok navíc.
Známé erratum18.6.1998 opravuje chybné2 naX2 v této odpovědi.
3(c): ENT4 s nepřímou adresou nastaví index na adresní pole buňky X,
stejně jako LD4 X(0:2). Pro numerickou nulu ENT4 použije znaménko
původní instrukční adresy X, tedy kladné; samotné načtení by zápornou
nulu paměťového slova zachovalo.

4(a) NOP *,7 nikdy neukončí nepřímé vyhodnocení. 4(b) LDA X,7:7(0:2)
dá dvě dereference s nulovými dalšími indexy. 4(c) třetí obecná
neznámá dereference pod původním omezením nelze: první načtené ukazatelové
slovo má0:0 a ukončí vlastní řetěz, a instrukce má jen dvě pole schopná
vyvolat nepřímý krok. Pevné pomocné konstanty nemohou dopředu obsahovat
obecnou neznámou adresu druhého následníka.
4(d) čtyři pomocné trojice na540 přidají postupně I2,I3,I4,I5,I6 a
hlavní instrukce přidá I1. Provedou se čtyři nepřímá čtení, tedy2+4=6u.
4(e) pomocná0,6:6 dává2*I6, hlavní modifikátor:6 dalšíI6 a INC6 ještě
přičte původníI6. Výsledek je4*I6 za předpokladu definovaných mezivýsledků.

`check_sequential_addressing.py` porovnává doslovné přepisování čekajícího
seznamu s algoritmemA v2960 nezávisle vygenerovaných platných výpočtech,
pro všech37 radixů, včetně záporných indexů a dvou hlavních7. Každá
vygenerovaná trojice je navíc sestavena se známou výslednou adresou.
Test potvrzuje i počet nepřímých čtení. Znaménková výjimka3(c) je
odvozena z definice MIX, nikoli předstírána celočíselným modelem bez
záporné nuly. Výsledky: `results/sequential-addressing.json`.

## Úloha6 a obrázek4

Přímé provedení(12) dává BASE=(0,3,5,6,20), TOP=(2,4,6,8) a hvězdičky
přesně u operací1,2,4,6,8,9. Proto I1 aI2 ještě zaplní poslední volnou
pozici, I3 okamžitě přeteče a pětI4 se vejde. D2D2 podteče při druhém
odebrání; kdyby se po neúspěšném odebrání pokračovalo s nezměněným
stavem, poslední ze tří následnýchI2 přeteče. Přesně to odpověď říká.

## Úloha8: úplná konstrukce pro kruhové fronty

Fronta j má svůj interval(b_j,b_(j+1)], délku C_j a počet prvků q_j<C_j.
F_j je pozice bezprostředně před čelem a R_j poslední položka, obojí
cyklicky v tomto intervalu. Počet q_j lze uchovávat, nebo vypočíst
jako(R_j−F_j) mod C_j. Vložení a odebrání užívají stejné cyklické
nástupce jako na245; podtečení je q_j=0, potřeba větší oblasti nastává
při vložení do q_j=C_j−1. Nová hodnota Y se před úspěšným přebalením
nikam do oblasti nezapisuje.

Zde je explicitní provedení, které zpřesňuje obrázkovou odpověď. Před
každým přebalením G/R znormalizujeme každou kruhovou frontu samostatně:
cyklicky otočíme celý její interval tak, aby původní nástupce F_j byl
na b_j+1. Rotaci lze provést třemi obráceními úseků, s jednou pomocnou
buňkou. Je to bijekce pozic dané oblasti, proto nezasáhne sousední
seznam; živé prvky se v pořadí dostanou na b_j+1,...,b_j+q_j.
Za ně připočteme jednu rezervovanou prázdnou buňku a nastavíme
virtuální TOP[j]=b_j+q_j+1. Právě tento příspěvek navíc vyžaduje
knižní odpověď kvůli rozlišení plné a prázdné fronty.

R lze nyní použít doslova: pohybuje souvislým blokem živých prvků a
jedné rezervované buňky. G počítá SUM a D z virtuálních TOP, včetně
této buňky. Po R nastavíme F_j na novou pravou hranici intervalu a
R_j=b_j+q_j pro neprázdnou frontu, jinak R_j=F_j. Tím se fronta
vrátí do platné kruhové reprezentace. Zásobníky se znormalizovat
nemusejí a jejich virtuálníTOP je skutečnýTOP; smíšený případ je stejný.

Pro rozpracované vložení zvýší G virtuální velikost cílové fronty o1,
stejně jako zásobníku. Při R se kopíruje původní blok včetně původní
rezervované buňky, nikoli neexistující nový konec. Po R se nový prvek
zapíše do původní rezervované buňky, tj. na novýTOP−1; novýTOP nyní
vyznačuje další rezervu. To je přesná úprava zápisového místa v(9).

Každá fronta musí dostat od počátku alespoň jednu rezervovanou buňku.
Je-li součet počtů front a živých prvků větší než M, nelze reprezentaci
alokovat a G správně hlásí nedostatek místa. C=1 je platná prázdná fronta
s nulovou užitnou kapacitou; její první vložení tedy vždy požaduje
zvětšení. Postup nepotřebuje pomocný seznam všech živých prvků.
Jeho dodatečná normalizace stojí O(M) na přebalení; není tvrzeno,
že pro tuto snadno ověřitelnou variantu automaticky platí zásobníkový
amortizovaný odhad úlohy18. Odpověď8 takovou časovou mez nepožaduje.
