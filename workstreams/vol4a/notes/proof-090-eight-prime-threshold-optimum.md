# Úloha104(a): všech21 prime podpor a minimum47

7. listopadu 2026. §7.1.1–104(a), p92/file109 a p553/file570;
checkpoint X0118, P1121–P1126, uzavření P1111–P1113.
Původní sazba zadání i výsledných vah byla zobrazena v X0117
a její přesný rozsah se přebírá. Žádný program, LP ani256vstupový
census se nespouštěl. Následuje úplná malá strukturální klasifikace
a celočíselný duální certifikát.

## 1. Doména, práh a všechny vítězné trojice

Původní váhy jsou

    a=(2,3,5,7,11,13,17,19),    Σa=77,    práh39.

Podpora B je minimální pravdivá právě tehdy, když její součet
dosáhne39 a každý její vlastní podvýběr prohraje. Žádná dvojice
nevyhraje, protože největší dvojice má19+17=36.

Trojice s indexem8 potřebuje ze zbývajících vah nejméně20.
S indexem7 to dává další index2,3,4,5 nebo6. Bez7 musí použít
index6 a další4 nebo5. Bez obou7/6 je největší pár11+7<20.
Trojice bez8 musí mít7 a dvojici o váze nejméně22; jedinou
takovou dvojicí je5,6 s vahami11+13. Úplný seznam je tedy

    278,378,478,578,678,468,568,567.

Všechny tyto trojice jsou minimální, protože žádná dvojice
nevyhraje. Máme přesně osm.

## 2. Všechny minimální čtveřice

Stačí hledat čtveřice, které neobsahují žádnou právě uvedenou
trojici. Rozdělíme je podle nejvyšších indexů:

| Větev | Zbývající podmínka | Nové minimální podpory |
|---|---|---|
|8 a7|Každé dva další indexy obsahují některý z2..6|žádná|
|8 a6, bez7|Nesmí4/5; pár z1,2,3 má váhu≥7|1368,2368|
|8, bez6/7|Trojice z1..5 má váhu≥20|1458,2458,3458|
|7 a6, bez8|Nesmí5; pár z1..4 má váhu≥9|1467,2467,3467|
|7, bez6/8|Trojice z1..5 má váhu≥22|3457|
|bez7/8|Největší čtyři zbývající váhy mají součet36|žádná|

Párové meze používají jen dvojice(2,3,5,7): alespoň9 dávají14,24,34,
alespoň11 jen34; s vahou11 dostaneme přesně uvedené trojice.
Každý vypsaný řádek neobsahuje vítěznou trojici, takže je
skutečně minimální. Celkem je přesně devět čtveřic.

## 3. Všechny minimální pětice a vyloučení větších podpor

Pětice nesmí obsahovat vítěznou trojici ani čtveřici.
S8 a7 už je vždy přítomna vítězná trojice. S8 a6, bez7,
nesmí být4/5; jediná zbývající pětice12368 obsahuje1368.
S8 a bez6/7 vybíráme čtyři z1..5. Přítomnost4 a5 spolu
s dalšími dvěma indexy dá některou z1458/2458/3458;
bez5 je součet příliš malý. Zůstává přesně12358.

Bez8, s7 a6, nesmí být5 a přítomnost4 by dala některou
z1467/2467/3467. Zůstává12367. Bez8/6, s7, potřebujeme
čtyři z1..5: bez4 nebo bez5 je součet nižší než39;
s4 a5 nesmí být3 kvůli3457. Zůstává12457.
Bez7/8 jde o pět z prvních šesti vah, jejichž součet je41.
Dosáhne39 pouze odstranění nejmenší váhy2, tedy23456.

Tyto čtyři podpory mají původní součty40,40,40,39; odebrání
jejich nejmenší váhy už dá méně než39, takže jsou minimální.
Žádná podpora alespoň šesti indexů nemůže být minimální:
pět největších vah libovolné šestice je po složkách nejméně
(3,5,7,11,13), jejichž součet je39. Obsahuje tedy vlastní
pravdivou podpodporu. Máme úplný počet8+9+4=21.

## 4. Ekvivalence všech vytištěných menších vah

Menší vektor v=(1,2,3,5,6,8,10,12) má součet47 a práh24.
Váhy všech21 minimálních pravdivých podpor jsou:

| Podpora | v-suma | Podpora | v-suma | Podpora | v-suma |
|---|---:|---|---:|---|---:|
|278|24|378|25|478|27|
|578|28|678|30|468|25|
|568|26|567|24|1368|24|
|2368|25|1458|24|2458|25|
|3458|26|1467|24|2467|25|
|3467|26|3457|24|12358|24|
|12367|24|12457|24|23456|24|

Každý původní pravdivý vstup obsahuje některou z těchto podpor;
nezáporné v proto dají hodnotu1 i nové funkci. Obě funkce jsou
liché čisté většiny, a tedy self-duální. Inkluze pravdivých
vstupů na komplementu x dává opačnou implikaci. Obě funkce
jsou přesně stejné na všech vstupech. Tím je prokázána celá
váhová identita, nikoli jen shoda na vybraných svědcích.

## 5. Explicitní duální certifikát minima47

Použijme jen deset podpor, které mají novou váhu přesně24:

|Řádek|Podpora|Multiplikátor λ|
|---|---|---:|
|A|278|9|
|B|567|2|
|C|1368|7|
|D|1458|5|
|E|1467|5|
|F|3457|4|
|G|12358|3|
|H|12367|2|
|I|12457|2|
|J|23456|8|

Součet λ je47. Každá z osmi proměnných má váženou incidenci24:

    1: C+D+E+G+H+I =7+5+5+3+2+2=24,
    2: A+G+H+I+J   =9+3+2+2+8=24,
    3: C+F+G+H+J   =7+4+3+2+8=24,
    4: D+E+F+I+J   =5+5+4+2+8=24,
    5: B+D+F+G+I+J =2+5+4+3+2+8=24,
    6: B+C+E+H+J   =2+7+5+2+8=24,
    7: A+B+E+F+H+I =9+2+5+4+2+2=24,
    8: A+C+D+G     =9+7+5+3=24.

Každé platné nezáporné celočíselné většinové váhy w musí na
pravdivé podpoře B splňovat2Σ_Bw_j−Σ_allw_j≥1. Vynásobením
těchto deseti nutných nerovností uvedenými λ a jejich sečtením
je koeficient každé proměnné2·24−47=1. Dostáváme přímo

    Σ_j w_j≥47.

Vektor v této meze dosahuje. Jde tedy o globální minimum,
dokonce již o minimum normalizovaného reálného LP. Certifikát
nepotřebuje algoritmus numerické optimalizace ani jeho výstup.

Každá proměnná je podstatná, protože je v některé minimální
podpoře. Přesný dřívější argument z proof-086 o zrušení opačných
literálů, monotónnosti a self-duálním centrování proto ukazuje,
že ani přidání konstant či negovaných literálů nemůže dát
kratší plochou většinu. Jejich nezáporné proměnné váhy stále
splňují stejné nutné nerovnosti, a samy tedy mají součet≥47.

Přebírá se přesná erratová rešerše104/p553 z X0117, včetně
odlišení stejně číslované úlohy ve fasciklu. Žádný nový rozpor.
P1111–P1113 jsou nyní checked. Všechny hlavní části104(a–c)
jsou uzavřeny; globální census dodatky a druhý samostatný
necelý příklad mají nadále vlastní explicitní partial položky.
