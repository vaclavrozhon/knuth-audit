# Gramatika 7.1.1–(34)/(35), sémantický core a úloha46

Checkpoint X0077, P0730–P0736. Originál p58–59/file75–76,
zadání46 na p85/file102 a odpověď p543/file560.
Doklady images/proof-file075.png, images/file076.png,
images/proof-file102.png, images/proof-file560.png.
Žádné generování řetězců ani matematický program.

## Zadaný řetězec používá všechny produkce — P0730

Zkratky E,T,F,V,L,C,D označují sedm vytištěných neterminálů.
Gramatika má 20 jednotlivých alternativ: 3+4+3+3+3+2+2.
Každý neterminál je produktivní a dosažitelný z E; žádná
produkce není prázdná.

Řetězec a/(-b0-10)+cc*cc má tento konkrétní rozklad:

- E→E+T; levá E→T, pravá T→T*F.
- Levá T→T/F, její levá T→F→V→L→a; pravá F→(E).
- V závorkách E→E−T; levá E→T→−F→−V,
  V→VD→LD→b0.
- Pravá vnitřní T→F→C→CD→DD→10.
- Oba pravé výskyty cc mají V→VL→LL→cc,
  s potřebnými T→F a F→V.

Jsou tak použity všechny tři E-alternativy, všechny čtyři
T-alternativy, všechny tři F i V alternativy, L→a,b,c,
C→D i C→CD a D→0,1. Tvrzení platí i v silném významu
„každá alternativa“, nikoli pouze každá ze sedmi řádkových pravidel.

## Všechny typy pravidel a oba vytištěné počty — P0731

Abeceda Σ={+,-,*,/,(,),a,b,c,0,1} má 11 různých terminálů.
Proměnné Xx, xX a xy mají odlišné typy (neterminály nejsou
terminály), takže je jich přesně

    7·11+11·7+11·11=77+77+121=275.

V (35) je následujících 24 jednoparametrických implikací;
řádky jsou rozděleny podle jejich účelu, žádná nebyla vynechána:

    xT⇒xE, Tx⇒Ex, xF⇒xT, Fx⇒Tx;
    xV⇒xF, Vx⇒Fx, xC⇒xF, Cx⇒Fx;
    xL⇒xV, Lx⇒Vx, Dx⇒Vx, xD⇒xC, Dx⇒Cx;
    Ex⇒x+, xT⇒+x, Ex⇒x-, xT⇒-x;
    xF⇒-x, Tx⇒x*, xF⇒*x, Tx⇒x/, xF⇒/x;
    xE⇒(x, Ex⇒x).

Tři dvouparametrické implikace jsou

    Vx∧yL⇒xy, Vx∧yD⇒xy, Cx∧yD⇒xy.

Třináct faktů je

    -T, (F, F);
    aL, La, bL, Lb, cL, Lc;
    0D, D0, 1D, D1.

Každý unary parametr má 11 hodnot, každý dvojitý 121; uvedené
instance jsou navzájem odlišné. Proto počet klauzulí je
24·11+3·121+13=264+363+13=640, včetně přesně třinácti
klauzulí s prázdným předpokladem. Každá má jednu pozitivní hlavu,
tedy je definite Hornova.

Přepis na začátku p59 je prostě A⇒B jako ¬A∨B a
A∧B⇒C jako ¬A∨¬B∨C. První dvě instance xT⇒xE pro
x=+ a x=- dávají přesně vytištěný začátek; instance
Vx∧yL⇒xy pro x=+,y=0 dává ¬(V+)∨¬(0L)∨(+0).
Závěrečné (D1) je jeden z faktů. Záměna symbolů s jejich
pravdivostními hodnotami se nepoužívá.

## Přesné FIRST a LAST všech neterminálů — P0732

Označme A={a,b,c,0,1}, L₀={a,b,c}, D₀={0,1}.
Úplné množiny možných prvních a posledních znaků jsou:

| X | FIRST(X) | LAST(X) |
|---|---|---|
| L | L₀ | L₀ |
| D | D₀ | D₀ |
| V | L₀ | A |
| C | D₀ | D₀ |
| F | A∪{(} | A∪{)} |
| T | A∪{(,-} | A∪{)} |
| E | A∪{(,-} | A∪{)} |

Pro V je první znak dán základním L a připojování L/D mění
jen poslední znak. Pro C se stejně připojují pouze číslice.
F přidává k V/C závorkové výrazy, T navíc počáteční minus;
operace E a zbývající T ponechávají první symbol prvního
dítěte a poslední posledního dítěte. Žádné další znaky proto
nemohou vzniknout, indukcí podle derivačního stromu.
Každý uvedený znak má svědka: samostatné písmeno/číslice,
proměnná a0, závorkový (a), nebo −a a jejich jednoduché kontexty.

Součet velikostí všech FIRST je30 a všech LAST také30.
Tyto počty jsou pomocné důsledky tabulky, nikoli vytištěné
výsledky převzaté bez argumentu.

## Správnost a úplnost Hornovy reprezentace — P0733

Každá unary implikace je přenos prvního/posledního znaku přes
konkrétní produkci nebo sousedství terminálu se znakem jeho
neterminálního souseda. Dvouparametrické implikace popisují
hranici V|L, V|D a C|D v příslušné konkatenaci.
Oba potřebné svědky lze nezávisle zvolit, protože gramatika je
bezkontextová. Produktivita ostatních dětí a dosažitelnost
z E dovolují každý lokální pár vložit do úplného výrazu.
Fakta jsou přímo terminální alternativy, minus nebo závorky.
Všechny odvozené propozice tedy mají skutečné gramatické svědky.

Pro úplnost first/last stačí indukce na derivačním stromu:
protože není prázdné dítě, první/poslední znak pochází z krajního
dítěte. Všechny netriviální přenosy jsou v seznamu P0731.
V rekurzích E→E±T, T→T*F/T/F, V→VL/VD a C→CD by
zbývající first/last přenos byl buď tautologický, nebo už plyne
ze základní alternativy E→T, T→F, V→L, C→D.

Pro libovolné dva sousední terminály vezměme nejnižší uzel
derivačního stromu, jehož výstup obsahuje oba. Jsou přes hranici
dvou sousedních neprázdných dětí nebo terminálů pravé strany.
Všechny takové hranice jsou:
E|±, ±|T, T|*, *|F, T|/, /|F, −|F, (|E, E|), V|L, V|D a C|D.
Každá má právě pravidlo v P0731. Dvojice uvnitř dítěte pokryje
indukce. Tím je reprezentace úplná, nikoli jen korektní aproximace.

## Úloha46: všech88 dvojic a žádné další — P0734

Z P0732/P0733 vychází tento úplný popis po řádcích:

| první znak x | možné následující znaky y | počet dvojic |
|---|---|---|
| x∈A | A∪{+,-,*,/,)} | 5·10=50 |
| x∈{(,+,-} | A∪{(,-} | 3·7=21 |
| x∈{*,/} | A∪{(} | 2·6=12 |
| x=) | {+,-,*,/,)} | 5 |

Řádky jsou disjunktní a dávají50+21+12+5=88.
Jde přesně o seskupení odpovědi: pět řádků pro (,*,/,+,-
má nejprve šest možností a navíc minus v řádcích (, + a -.

Úplnost lze také přímo přečíst z hranic produkcí:
A×A vzniká ve V→VL/VD (číslicový levý znak dovolí např. a0);
(A∪{)}) předchází každý binární operátor i uzavírací závorku;
+,− a ( předcházejí FIRST(T)=FIRST(E), kdežto *,/ předcházejí
FIRST(F). Připojování číslic v C už žádnou novou dvojici nepřidá.
To vyčerpává všechny hranice z P0733 a současně poskytuje
svědka každé skupiny. Nebylo nutné generovat řetězce ani
procházet tabulku121 samostatnými testy.

Fakt −T implikuje −E a pravidlo xE⇒(x pak dává (-.
Dvojice ++ není v příslušném řádku, stejně jako *-;
nemohou tedy nastat, přesně podle dvou příkladů na p59.
Dvojice -- naopak může nastat v a--a: druhé minus je unary T→−F.

## Proč jsou právě sémantické pravdy core — P0735

U libovolného konečného definite Hornova systému začněme fakty
a opakovaně přidávejme hlavy s již přítomnými předpoklady.
Všechny přidané proměnné patří do každého modelu, indukcí
podle přidávání. Jakmile nelze nic přidat, dosažená množina
je sama modelem: splněné předpoklady už mají splněnou hlavu.
Je tedy nejmenším modelem, čili core podle P0726.

P0733 dokazuje, že v systému(35) je tato odvoditelnost ekvivalentní
skutečné gramatické pravdě. Core tedy obsahuje přesně všechny
pravdivé first/last/pair propozice, celkem30+30+88=148.
To prokazuje význam úvodního vysvětlení na p59.
Naivní přidávání určitě skončí po nejvýše275 nových proměnných;
**není to ještě důkaz lineárního času konkrétní implementace C**.

## Otevřená implementační mez a mapa p58 — P0736

Příslib O(N+n) práce na p59 pro rozvinuté klauzule stále čeká
na konkrétní data a kroky algoritmu C, včetně opravy z28.7.2016.
Patří k samostatné povinnosti P0729 o lineárních algoritmech;
P0736 zde přesně odlišuje abstraktní konečnou saturaci od její
lineární implementace. Nejde o nový nález.

Celý matematický obsah p58 je nyní doložen:

- definite Horn a core/faktorizace: P0725/P0726 v proof-047;
- gramatika a řetězec používající všechny alternativy: P0730;
- význam všech propozic a počet275: P0731–P0733;
- každé pravidlo(35), třináct faktů a počet640: P0731;
- proč právě tato pravidla řeší sousední znaky: P0732–P0735,
  včetně celé odpovědi46.

Poznámka o hrách jen odkazuje na pozdější konkrétní úlohy51/52;
jejich konstrukce se zde za ověřené nevydávají. V tomto
gramatickém bloku není samostatný externí matematický vstup.
Relevantní all4a-pre, all4a, err4a, all4f0, err4f0 byly prohledány;
žádná oprava gramatiky, počtů ani46 nebyla nalezena. Známá
úplná změna algoritmu C se bude kontrolovat v dalším bloku.

Strana59 zůstává partial: úvodní sémantika je hotová, náklady
a algoritmus teprve následují. Další kurzor p59/file76, C a47/48.
Žádný matematický program, nový nález ani kandidát.

Dodatek X0078: P0736 je nyní uzavřena důkazem obou implementací
v proof-049-horn-core-algorithm.md, P0737–P0742. Původní označení
mezery výše zaznamenává stav při X0077.
