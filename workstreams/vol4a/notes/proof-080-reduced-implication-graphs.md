# Úlohy 85–86: redukované modely a uzavřenost

Checkpoint X0109, P1027–P1031. Zadání p91/file108,
celé odpovědi a digraf p550/file567 prohlédnuty.
Přebíráme Theorem S, P0807/P0808 a antisymetrický
toposort P1004. Žádný matematický program neběžel.

## Přesná doména a smyčky — P1027 / F0009

Literálový digraf má s u→v i ¬v→¬u. Model přiřadí
doplňkům opačné hodnoty a žádná hrana nejde z 1 do 0.
Smyčky z tautologií neukládají podmínku. Odpověď 85
správně vyžaduje singletonové silné komponenty,
ale nesprávně z toho vyvozuje acykličnost původního
digrafu. Přesný protipříklad (x∨y)∧(x∨¬x), doména,
originály a errata jsou v F0009-implication-self-loops.md.

Správná charakterizace: po odstranění smyček je
digraf acyklický a neexistuje cesta od žádného
literálu k jeho doplňku. První podmínka je právě
ekvivalentní singletonovým silným komponentám.

## Nutnost — P1028

Redukovanost poskytuje pro každou proměnnou dva
modely, které se liší právě v ní. Dva různé literály
v jedné silné komponentě mají ve všech modelech
stejnou hodnotu. Jsou-li z různých proměnných,
svědek jedné tuto rovnost poruší; jsou-li doplňky,
rovnost je nemožná v každém modelu. Komponenty
jsou proto singletony. Po odstranění smyček máme DAG.

Cesta u→¬u vynucuje ve všech modelech u=0, tedy
konstantní souřadnici bez redukčního svědka. To
prokazuje i druhou nutnou podmínku v celém rozsahu.

## Postačitelnost: oba svědci každého bitu — P1029

Odstraňme smyčky. Pro pevný literál x nechť A jsou
všichni striktní předchůdci x nebo ¬x a B všichni
striktní následníci x nebo ¬x; samotné x,¬x do
nich nepatří. A a B jsou disjunktní: společný bod
by dal cestu od x či ¬x do x či ¬x, tedy cyklus
nebo cestu k doplňku. Obojí je zakázáno.

Kontrapozice dává ¬A=B. A je dolní ideál, B horní
ideál. Zbývající vrcholy R mimo A,B,{x,¬x} jsou
uzavřeny na komplementaci a jejich indukovaný graf
splňuje stejné dvě podmínky. Dejme 0 na A a 1 na B.
V R použijme P1004: první polovině antisymetrického
toposortu dejme 0 a druhé 1. Tím splníme všechny
vnitřní hrany R a opačné hodnoty doplňků.

Nemůže existovat hrana z B do R či A, ani z R do A,
protože by porušovala uzavřenost ideálů. Z A
vycházející a do B vcházející hrany jsou bezpečné.
Každá hrana vstupující do x nebo ¬x přichází z A;
každá vystupující končí v B. Mezi x a ¬x hrana
není. Můžeme proto bez jakékoli jiné změny položit
(x,¬x)=(0,1), nebo (1,0). Obě přiřazení splňují
celý graf a liší se právě v jedné proměnné.

Konstrukce funguje pro každý bit. Pro t=0 má
prázdný graf jediný prázdný model a redukovanost
platí vakuózně. Pro t=1 dává oba jednobitové modely.
Není zde dodatečná nevyjádřená prázdná nepravdivá
klauzule: jde přesně o modely grafových implikací.
Theorem S a P0995 dávají redukovaný mediánový graf.
Tím jsou všechny „appropriate values“ z odpovědi
konkrétně zkonstruovány.

## Celý konkrétní digraf a jeho šest štítků — P1030

Čtyři nezávislé relace obrázku jsou

    w→y, x→y, w→¬z, x→z.

Další čtyři šipky jsou přesně kontrapozice
¬y→¬w, ¬y→¬x, z→¬w, ¬z→¬x. Souhlasí všech
osm hran včetně vodorovných cest a diagonál.

V pořadí w,x,y,z má w=1 za následek y=1,z=0
a pak x=0: jediný model 1010. Pro w=x=0 jsou
y,z libovolné: 0000,0001,0010,0011. Pro w=0,x=1
je y=z=1: 0111. To je právě celý tištěný seznam,
bez dalšího modelu. Redukční svědci jsou

    w: 0010–1010; x: 0011–0111;
    y: 0000–0010; z: 0000–0001.

Graf je čtyřcyklus 0000–0001–0011–0010–0000,
s listem 0111 u 0011 a listem 1010 u 0010.
Jiné jednobitové dvojice v seznamu nejsou.
Mediánovou uzavřenost dává Theorem S. Tím je
doložen celý dodatek odpovědi 85.

## Celá úloha 86 a obecnější věta odpovědi — P1031

Pětivstupová funkce „aspoň tři jedničky“ je monotónní.
Komplementace mění počet jedniček k na 5−k a právě
jedna z nerovností k≥3, 5−k≥3 platí. Je tedy také
selfdualní. Theorem P, úplně doložená v proof-059,
ji vyjadřuje termem z ternárních mediánů.

Mediánová množina X je uzavřená na každý takový
term, indukcí podle jeho konstrukce. Medián pěti
prvků X tedy patří do X. Totéž funguje pro každou
monotónní selfdualní funkci kladné arity, jak
zobecňuje odpověď. Vstupy se smějí opakovat;
prázdné X nemá zadanou pětici a není výjimkou.
Není třeba žádná enumerace.

## Přesný rozsah

85 a 86 včetně dodatků jsou dokončeny s lokální
opravou F0009/low. Pět relevantních vrstev 4A/F0
a kvůli cyklům i čtyři vrstvy V1 prověřeny.
P550 zůstává partial kvůli P1025/P1026 a 87;
p91 také obsahuje další neuzavřené úlohy. Další
blok je 87–88 včetně známého dodatku o lineární
paralelní hloubce, potom text p75.
