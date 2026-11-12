# Celá úloha 110: regularita, Chowovo pořadí a nejednoznačné minimum

7. listopadu 2026, X0122, P1156–P1164. Zadání p93/file110 a odpověď
p554/file571 zobrazeny. Použita známá oprava části (d) z 20. července
2011: předpokládá čistou většinu bez vstupních konstant. Níže jsou
protipříklady i v této užší doméně; nevydáváme chybnou testovanou
domněnku za chybu knihy. Žádný matematický program ani LP běh.

## (a) Regularita implikuje monotónnost

Je-li x≤y po bitech, jsou stejně uspořádány všechny prefixové součty,
tedy x≤y i v majorizaci. Regularita proto dává f(x)≤f(y), přesně
definici monotónnosti. Na prázdné doméně souřadnic je závěr triviální.

## (b) Samotné seřazení vah nestačí; nezáporná poslední váha stačí

Například n=1, w_1=−1, t=0 splňuje veškeré požadované seřazení,
ale f(x)=[−x≥0]=¬x není regulární: 0<1, avšak f(0)>f(1).

Je-li navíc w_n≥0, přesná charakterizace pokrytí z proof-094 dává
kladný obecný důkaz. Zvýšení posledního bitu přidá w_n≥0; záměna
01→10 na pozicích j,j+1 přidá w_j−w_(j+1)≥0. Každý vzestup
v majorizaci je složen z těchto pokrytí, takže vážený součet ani
jeho prahový indikátor neklesá. Nulové váhy i libovolný práh jsou
povoleny; konstantní funkce nijak nepřekážejí.

## (c) Seřazení Chowových složek i pro záporné váhy

Nechť s_j=Σ_x x_j f(x). Seskupme vstupy podle všech ostatních
souřadnic. Případy 00 a 11 se v rozdílu s_j−s_(j+1) ruší, takže

    s_j−s_(j+1)=Σ_rest (f(rest,1,0)−f(rest,0,1)).

Rozdíl příslušných vážených součtů je w_j−w_(j+1)≥0. Každý
sčítanec je tudíž nezáporný a s_j≥s_(j+1). Tento párový důkaz
nepotřebuje w_n≥0 ani regularitu, pouze příslušné pořadí dvou vah.
Tím je ověřen i výslovný dodatek odpovědi o záporné poslední váze.

## (d) První protipříklad v opravené doméně

Čistá většina s vahami (1,2,2) má délku 5 a práh 3. Když x_2=x_3,
určují oba tyto bity výsledek; když jsou opačné, váha je 2+x_1
a rozhoduje x_1. Jde tedy přesně o ⟨x_1 x_2 x_3⟩. Každá proměnná
je jedničkou na třech pravdivých vstupech, tedy Σ=(3,3,3).
Složky jsou seřazené, ale 1<2 odporuje požadovanému pořadí vah.
Tento příklad nepotřebuje konstanty ani záporné literály.

## Dodatek: symetrie vytištěného devítiproměnného příkladu

Vytištěný vektor je

    v=(17,9,8,6,7,5,3,2,2),       Σv=59,       t=30.

Změna pořadí x_4,x_5 může ovlivnit výsledek pouze tehdy, když součet
R ostatních vah je 23: porovnáváme R+6 a R+7 s 30. Ostatní váhy
jsou (17,9,8,5,3,2,2), se součtem 46. Pokud vybraná podmnožina
obsahuje 17, musel by zbytek mít součet 6. Pokud 17 neobsahuje,
komplement v množině (9,8,5,3,2,2), se součtem 29, by měl součet 6.

Součet 6 však mezi (9,8,5,3,2,2) není: 9 a 8 jsou příliš velké;
po 5 chybí 1; po 3 chybí 3 ze dvou dvojek; samotné dvojky dají
jen 0,2,4. Tedy R=23 nenastává. Funkce je skutečně symetrická
v x_4,x_5 na všech vstupech, bez tabulky 512 možností.

## Přesný duální certifikát minima 59

Osm podpor v následující tabulce má ve vytištěné reprezentaci váhu
přesně 30. Jsou pravdivé a prime, protože všechny odebrané váhy
jsou kladné. Tabulka uvádí ručně odvozené kladné násobky nutných
normalizovaných nerovností 2Σ_B w_j−Σ_all w_j≥1.

| Řádek | Podpora B | Její vytištěná váha | λ |
|---|---|---|---:|
| A | 145 | 17+6+7=30 | 1 |
| B | 1289 | 17+9+2+2=30 | 12 |
| C | 136 | 17+8+5=30 | 3 |
| D | 1378 | 17+8+3+2=30 | 7 |
| E | 1379 | 17+8+3+2=30 | 7 |
| F | 345689 | 8+6+7+5+2+2=30 | 11 |
| G | 24567 | 9+6+7+5+3=30 | 16 |
| H | 2345 | 9+8+6+7=30 | 2 |

Součet λ je 59 a všechny sloupcové incidence jsou 30:

    1: A+B+C+D+E =1+12+3+7+7=30,
    2: B+G+H     =12+16+2=30,
    3: C+D+E+F+H =3+7+7+11+2=30,
    4: A+F+G+H   =1+11+16+2=30,
    5: A+F+G+H   =1+11+16+2=30,
    6: C+F+G     =3+11+16=30,
    7: D+E+G     =7+7+16=30,
    8: B+D+F     =12+7+11=30,
    9: B+E+F     =12+7+11=30.

Každý váhový koeficient je po sečtení 2·30−59=1. Proto Σw_j≥59
pro každé přípustné reálné normalizované řešení. Vytištěný vektor
má lichý součet 59 a reprezentuje definovanou funkci, takže všechny
jeho pravdivé vstupy mají podepsanou mezeru alespoň 1; dolní meze
dosahuje. To je globální optimum, nikoli pouze lokální reprezentace.

Všechny proměnné jsou podstatné, protože každá patří některé z uvedených
prime podpor. Přesný argument proof-092 §5 proto navíc vylučuje kratší
plochou většinu i při povolení konstant a opačných literálů. Nevyžaduje
nový výpočet: monotónnost dává kladné net weights a self-dualita nutné
podepsané mezery, na které se použije právě tento duál.

## Dvě optima a seřazené s při neseřazených w

Symetrie dokázaná výše znamená, že stejnou funkci reprezentuje také

    v'=(17,9,8,7,6,5,3,2,2).

Má tutéž délku 59 a je tedy druhým skutečným optimem. Protože v' je
seřazené, část (c) dokazuje seřazení všech složek Σ této funkce.
Ve v jsou přesto w_4=6<w_5=7. Tím je úplně doložen i silnější
protipříklad s minimálním součtem a skutečná nejednoznačnost LP.

Konvexní kombinace obou přípustných vektorů také zůstávají optimální;
jsou to společné lineární nerovnosti a lineární cíl. Netvrdíme zde
bez dalšího úplnou klasifikaci extrémních bodů ani že jiné optimum
neexistuje: pro knižní dodatek postačují dvě odlišná prokázaná minima.

## Závěrečný ostrý výrok

Jestliže s_j>s_(j+1), nutně w_j>w_(j+1). Kdyby w_j≤w_(j+1),
tentýž párový argument (c) s obráceným pořadím indexů by dal
s_j≤s_(j+1), spor. Tento závěr platí pro obecný prahový popis,
nejen pro čisté většiny a nejen pro optimální váhy. Rovnosti s
naopak pořadí vah nevynucují, jak konkrétně ukazují oba příklady.

## Errata a pramen

Prohlédnuty relevantní položky all4a-pre, all4a, err4a, all4f0 a
err4f0. Známá oprava zadání (d) z 20.7.2011 je zohledněna; žádná
karta ani nový nález. Všechny čtyři části a matematické dodatky checked.

Nově dostupný primární článek Muroga–Tsuboi–Baugh, IEEE C-19 (1970),
p818–825, má tento konkrétní pár vah ve druhém řádku Table IV na p822;
originál byl zobrazen. Nezávislý důkaz minima a symetrie je výše,
takže nejde o převzetí závěru pouze ze zdrojové tabulky. Původní článek:
[scan](https://people.eecs.berkeley.edu/~alanmi/publications/other/01671639_002.pdf),
lokálně sources/muroga-tsuboi-baugh1970.pdf.
