# Prahové úlohy97–100: všechny předpoklady a dodatky

7. listopadu 2026. §7.1.1 p92/file109 a odpovědi p552/file569,
P1066–P1073, X0114. Obě původní stránky zobrazeny; v úloze98
jsou v příkladu nad x_4 a x_6 opravdu komplementační čárky.
Žádný matematický program. Převzaty pouze přesné důkazy paddingu
z proof-083 a mediánových zákonů (53)/(54) z proof-063.

## 1. Všech šest případů úlohy97

Při W=2 máme a=max(0,2t−3), b=max(0,3−2t). Dosazení dává:

| t | a | b | Medián | Funkce |
|---:|---:|---:|---|---|
|−1|0|5|⟨11111x_1x_2⟩|1|
|0|0|3|⟨111x_1x_2⟩|1|
|1|0|1|⟨1x_1x_2⟩|x_1∨x_2|
|2|1|0|⟨0x_1x_2⟩|x_1∧x_2|
|3|3|0|⟨000x_1x_2⟩|0|
|4|5|0|⟨00000x_1x_2⟩|0|

Počet jedniček proti prahu lichého mediánu dává uvedené funkce
přímo. Tabulka souhlasí se všemi šesti výrazy odpovědi, včetně
prahových hodnot mimo rozsah počtu jedniček.

## 2. Úloha98: zdůvodnění počátečního „můžeme předpokládat“

Self-duální bitová funkce nemůže být konstantní; pro n=0 žádná
taková funkce neexistuje. Použijeme celočíselnou reprezentaci
z proof-083. Převod záporných vah na kladné pomocí literálů
komutuje s globální komplementací všech bitů. Po změně polarit
tedy máme stále self-duální funkci g(z)=[Σa_j z_j≥t], a_j≥0.
Nulové váhy lze vypustit a nakonec vrátit s výsledným v_j=0.
Zůstane alespoň jedna kladná váha. Označme W=Σa_j>0.

Žádná dosažitelná suma Σa_j z_j se nerovná W/2. Jinak mají z
a ¬z shodnou sumu, a tedy shodný výsledek, proti self-dualitě.
U každé komplementární dvojice je proto právě vyšší suma pravdivá:
oba výsledky jsou opačné a prahový test je monotónní v samotné
sumě. Funkce se tedy rovná [Σa_j z_j>W/2].

Zde ještě W nemusí být liché. Chceme-li přesně předpoklad odpovědi,
vyberme jednu kladnou váhu a zdvojnásobme všechny váhy, k vybrané
navíc přičtěme1. Nový součet je2W+1, tedy lichý. Pro libovolný
vstup se původní nenulová celočíselná odchylka
Q=2Σa_j z_j−W změní na2Q+(2z_j−1). Její znaménko se zachová,
protože |Q|≥1. Nové kladné celočíselné váhy tak dávají stejnou
funkci jako čistou lichou většinu. Tím je počáteční předpoklad
odpovědi doložen i pro původně záporné/nulové váhy a sudý součet.
Nezavádíme žádnou další proměnnou.

## 3. Celý převod na ostrý nulový práh

Nyní použijme kladné váhy a_j s lichým W. Všechny podepsané součty
Σσ_j a_j, σ_j∈{−1,1}, jsou liché a nenulové. Konečná symetrická
množina těchto součtů obsahuje W>0; má tedy nejmenší kladný
prvek δ≥1. Vyberme znaménka s výsledkem δ a rozdělme indexy
na P (plus) a M (minus). Potom

    δ=Σ_P a_j−Σ_M a_j,   A=Σ_M a_j=(W−δ)/2.

Pro každý bitový z je Q=2Σa_j z_j−W jedním z těchto součtů,
takže Q≤−δ nebo Q≥δ. Proto přesně platí

    g(z)=1 ⇔ Q>0 ⇔ Q>−δ ⇔ Σa_j z_j>A
          ⇔ Σ_P a_j z_j−Σ_M a_j(1−z_j)>0.

Rovnost Q=−δ patří do nulového výsledku; proto se v posledním
výrazu musí ponechat ostré >0, jak má zadání. Položme v_j=a_j,
y_j=z_j pro P a v_j=−a_j, y_j=1−z_j pro M. Po složení s původní
změnou polarit je každý y_j opravdu x_j nebo ¬x_j. Vypuštěné
proměnné mají v_j=0. Prázdná M je dovolena, např. při jediné
relevantní proměnné. Existence δ není tvrzení o efektivním
vyhledání nejmenšího podepsaného součtu; nic takového se nespouštělo.

V konkrétním příkladu W=41 a

    2+3+5−7+11−13=1.

Všechny podepsané součty jsou liché, takže tento svědek dokazuje
δ=1 bez prohledávání ostatních možností. M={4,6}, A=20. Přesně
proto je původní práh≥21 ekvivalentní vytištěnému

    2x_1+3x_2+5x_3−7¬x_4+11x_5−13¬x_6>0.

## 4. Úloha99 a všechny formule dodatku

Nechť s,t≥1, X=Σ_{i=1}^{2s−1}x_i a Y=Σ_{j=1}^{2t−2}y_j.
Levá strana zadání je [[X≥s]+Y≥t]. Pravá strana má délku
(2s−1)+s(2t−2)=2st−1, tedy je [X+sY≥st]. Protože Y,t jsou
celé a 0≤X≤2s−1, platí

    [X+sY≥st]=[floor(X/s)+Y≥t]=[[X≥s]+Y≥t].

To dokazuje celý obecný vztah i pro s=1 nebo t=1. Nevyžaduje
nezávislost vstupů, proto dovoluje opakované literály i konstanty.
Při s=t=2 dává přesně ⟨⟨xyz⟩uv⟩=⟨xyzu²v²⟩. Obě další
rovnosti s ⟨x⟨yuv⟩⟨zuv⟩⟩ a ⟨⟨xuv⟩⟨yuv⟩⟨zuv⟩⟩ jsou
přesně (53)/(54), už obecně dokázané z mediánových axiomů
v `notes/proof-063-median-axioms-distributivity.md`, §„Krátká
i dlouhá distributivita“, P0871. Tento důkaz se neopakoval.

## 5. Úloha100: správnost odkazovaného důkazu i přímé parametry

Každý threshold lze podle proof-083 psát jako lichou většinu
literálů a konstant. Dále f∧z=⟨fz0⟩ a f∨z=⟨fz1⟩, tedy (45).
Úloha99 složí tuto vnější a vnitřní většinu v jedinou lichou
většinu. Její opakované literály a konstanty lze sečíst do
celočíselných vah a prahu, jak bylo již doloženo v proof-083.
Odpověď „true“ tedy platí v obou částech v přesně obecném rozsahu.

Navíc je možné dát parametry přímo bez rozbalování většinového
výrazu. Nechť f(x)=[S≥t], S=Σw_j x_j, a označme

    m=Σ min(0,w_j),   M=Σ max(0,w_j),
    B=max(0,M−t+1),   C=max(0,t−m).

Vždy m≤S≤M. Potom platí

    f(x)∧z = [S+Bz ≥ t+B],
    f(x)∨z = [S+Cz ≥ t].

V první rovnosti se při z=1 B zruší. Při z=0 je pravá strana
nepravdivá: buď B>0 a práh je M+1, nebo B=0 a už t≥M+1.
Ve druhé rovnosti z=0 vrátí f; při z=1 je pravá strana vždy
pravdivá, protože C>0 dává m+C=t a C=0 dává m≥t.
Tím jsou pokryty záporné a nulové váhy, oba konstantní výsledky,
nepodstatné vstupy i n=0. Nová proměnná je přesně z=x_{n+1}.
Parametry se získají jedním průchodem původními n vahami,
O(n) aritmetickými operacemi; při vstupních b-bitových parametrech
mají součty O(b+log(n+1)) bitů. Kniha zde žádnou optimalitu
nových vah netvrdí.

## 6. Bibliografický rozsah a errata

Primární IEEE záznam článku [Truth functions realizable by single
threshold organs](https://ieeexplore.ieee.org/document/5397278/)
je dostupný pouze jako vyhledávací výpis s názvem a konferencí;
přímé otevření vyžaduje JavaScript. Přesné místo Elgot p238
a historické připsání Mezeiovi z roku1961 výslovně přeskočeny.
Ani jeden údaj není matematický předpoklad důkazů výše.

Relevantní vrstvy `all4a-pre`, `all4a`, `err4a`, `all4f0`,
`err4f0` prohledány podle stran, answer97–100 a threshold/majority.
Opravy stejných čísel úloh v jiných sekcích se sem nevztahují.
Žádný nový nález. Všechny čtyři úlohy včetně matematických dodatků
jsou uzavřené; p92 a p552 mají další dosud neuzavřené úlohy.
