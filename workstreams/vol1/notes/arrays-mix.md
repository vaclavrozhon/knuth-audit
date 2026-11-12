# §2.2.6-15: skutečný MIX a rozsah aritmetiky

Původní zadání na s.306 výslovně předpokládá, že sčítání a odčítání
vrátí nulu při ztrátě většiny platných číslic a že plovoucí operace
mění pouze rA. Program na s.557–559 byl přečten v obrazech a přepsán
do `array_pivot_mix.py`. Návěští, instrukce, pole a větvení jsou
doslovné; zápis konstanty `=1.0=` je nahrazen pojmenovaným slovem
FONE se stejnou hodnotou. BROW, BCOL, vstupní matice, volné uzly,
koncový návrat a OVERFLOW jsou testovací okolí, nikoli změny algoritmu.

## Registrace abstraktních proměnných

rI1 postupně obsahuje adresu pivotu a sloupec J; rI2 je P0, rI3 je
Q0, rI4 je řádkový předchůdce P, rI5 je P1 nebo nově přidělený X.
rI6 hledá sloupcového předchůdce. ROW a UP sídlí v prvním slově uzlu,
COL a LEFT ve druhém, VAL ve třetím. ROW/COL zabírají pole0:3,
odkazy4:5. PTR[J] používá bajty1:3 sloupcové hlavičky, její záporné
znaménko a UP proto zůstávají zachovány. Slovní konstanty I0,J0,I
jsou disjunktní s programem a daty.

S1 uloží souřadnice a převrácenou hodnotu před přepsáním pivotu.
S2 získá LEFT, přečte COL a podle jeho znaménka rozliší datový uzel
od hlavičky. Tělo2H při každém nenulovém pivotním sloupci uloží
PTR a násobí VAL. Následující průchod S3 čte UP, přeskočí pivotní
řádek a při záporném ROW vrací řízení přes instrukci9H, jejíž
adresové pole bylo nastaveno STJ při vstupu.

V S4 se P0 posouvá po neměnném pivotním řádku, J0 se vynechá.
ENTA se SLA2 umístí J do stejné pozice, kterou má pole COL načtené
do rA; proto CMPA porovnává právě indexy, nikoli odkazy. Pro záporný
J se dokončí pivotní koeficient daného řádku. S5 posouvá dvojici
P,P1 až do shody nebo místa pro vložení.

S6 obdobně porovnává v rA posunuté I s ROW. rI6 je předchůdce,
rI5 nejprve následující uzel a pak nově odebraný AVAIL. Jeho starý
volný odkaz se přečte před přepsáním. Instrukce59–70 vyplní obě
souřadnice, oba odkazy, nulovou hodnotu a nakonec oba příchozí odkazy.
Nulové AVAIL vede na OVERFLOW před zápisem do neexistujícího uzlu.

S7 počítá (−c)*(b/a)+d, přesně v pořadí předepsaném algoritmem.
JAZ reaguje na nulový obsah rA podle předpokladu zadání. Při
nenulovém výsledku aktualizuje VAL, PTR[J] a P. S8 hledá rI6 tak,
aby UP(rI6)=P1, odpojí P1 v obou seznamech a vrátí jej do AVAIL.
Přitom zachová vodorovného předchůdce P; S4A tedy čte nový LEFT(P),
nikoli uvolněný uzel. Obecný invariant a konečnost jsou dokázány
v `arrays-sparse.md`, na nějž tento převod registrů navazuje.

## Co ověřuje běžící stroj

Základní instrukce provádí existující MIX interpret, nikoli pomocné
Python implementace kroků S. Rozšíření pro čtyři plovoucí operace
používá skutečná slova se znaménkem, exponentem e a čtyřbajtovou
mantisou m: hodnota je ±m*b^(e−floor(b/2)−4). Formát a normalizace
byly porovnány s originálem svazku2, s.215; kontrakt registrů a
operací se s.223–224. Pozor, v tomto DjVu svazku2 je převod +12,
nikoli +11 jako u svazku3.

Tento přídavný stroj přijímá pouze přesně reprezentovatelné výsledky
a při zaokrouhlení nebo rozsahové chybě výslovně skončí chybou.
Nepoužívá Python float a není úplným modelem zaokrouhlování kapitoly4.
Proto konečné testy dokládají instrukční a spojovou správnost na
přesně reprezentovatelných případech; obecný převod platí pod
aritmetickým kontraktem zadání. Numerická stabilita, volba tolerance,
podtečení a přetečení nejsou tímto vydávány za vyřešené.

Poznámka na s.559 pro skutečné konvence kapitoly4 nejprve vypočte
c*(b/a), porovná jej FCMP s d a při přibližné shodě smaže uzel;
jinak odečte uložený součin od d. Algebraicky i pořadím operandů
odpovídá S7. FCMP podle svazku2 s.224 zachovává rA a používá
EPSILON v buňce0. Implementace celé plovoucí jednotky z kapitoly4
není součástí tohoto auditu svazku1.

## Výsledky

`results/array-sparse.json` zaznamenává 1216 MIX pivotů, 113350
instrukčních kroků a7139 plovoucích operací, všech37 přípustných
velikostí bajtu64–100. Větev vložení navštívena492krát, mazání173krát.
Každý výstup byl porovnán s nezávislým hustým racionálním pivotem;
ověřeny oba seznamy, jejich pořadí, shodné množiny uzlů, oddělení
volného fondu a nezměněný rX. Zahrnuty prázdné řádky/sloupce,
pivoty na okrajích, doslovný příklad, uzel končící na adrese3999,
dostatek volné paměti i samostatný výstup OVERFLOW.
