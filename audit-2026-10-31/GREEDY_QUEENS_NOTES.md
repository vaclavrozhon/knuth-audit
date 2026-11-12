# Nekonečné dámy — úlohy 7.2.2.1–37–38

Kontrola 1. listopadu 2026. Zadání str. 127, odpovědi str. 423;
autorův PostScript `fasc5c`, str. 127. Obě původní stránky byly vizuálně
zkontrolovány. Historická errata finálního Fascicle 5 používají str. 231.

## F111: prohozené indexy v odpovědi 37(a)

Pro uvedenou rekurenci platí **a[q_i,i]=1**, nikoli vytištěné **a[i,q_i]=1**.
Už i=2 stačí: zadání má q₂=3, ale rekurence dává a[2,3]=5,
zatímco a[3,2]=1. Její levý horní roh je

```
1 3 2 6
2 4 5 1
3 1 6 2
4 2 3 5
```

Nejde o volbu názvů řádků a sloupců: konkrétní indexy odporují vytištěné
číselné posloupnosti a vlastní rekurenci. Úprava pouze přehodí dva indexy;
permutace q i zbytek důkazu zůstávají beze změny.

## Úplný důkaz vlastností pomocné matice

Rekurence je dobře založená. Buňky lze počítat podle rostoucího i+j,
při shodě podle rostoucího j. Člen a[i+k,j−k] má stejný součet,
ale menší j; ostatní kladně indexované členy mají menší součet.
Nekonečné množiny v zápisu mají jen konečně mnoho nenulových členů.
Nula v každém mexu zajišťuje kladné hodnoty.

Každá pevná hodnota se v libovolném řádku, sloupci a úhlopříčce objeví
nejvýše jednou: pozdější výskyt vidí předchozí v příslušné množině mexu.

**Sloupce.** Předpokládejme, že ve sloupci j chybí nejmenší hodnota v.
Menší hodnoty už od určitého místa všechny leží nad aktuální buňkou.
V j−1 sloupcích vlevo je nejvýše j−1 výskytů v, které zakážou jen konečně
mnoho míst sloupce j. Dostatečně nízko je proto v povolená a všechny menší
hodnoty jsou zakázané. Mex musí dát v, spor.

**Řádky.** Obdobně nechť v je nejmenší chybějící hodnota v řádku i.
Menší hodnoty už od určitého sloupce leží vlevo. V řádcích nad i se v
vyskytne nejvýše i−1krát; jejich vliv na tento řádek skončí po konečně
mnoha sloupcích. Kdyby v dál pořád chyběla, muselo by pro každé dostatečně
velké j existovat v v buňce (i+d,c), d,c>0, d+c=j.

Pro t po sobě jdoucích j=J,…,J+t−1 by šlo o t bodů s navzájem různými
kladnými d i c. Součet jejich souřadnic je nejméně t(t+1), ale součet
předepsaných j je tJ+t(t−1)/2. Odtud t≤2J−3, což pro libovolně velká t
není možné. Každý řádek tedy rovněž obsahuje všechny kladné hodnoty.

**Spojení s q.** V pevném sloupci j vzniká první jednička v nejnižší buňce,
která není napadena starší jedničkou. To je přesně definice greedy queens.
Indukcí je proto a[q_j,j]=1. Protože každý řádek obsahuje právě jednu
jedničku, každé kladné číslo se v q objeví právě jednou.

Dva nezávislé výpočty matice — doslovná rekurence a množiny použitých barev
na čtyřech směrech — souhlasí ve všech 12 720 buňkách s i+j≤160.
Sedmdesát pět pozic q v tomto trojúhelníku splňuje opravený indexový vztah.
Přímá definice greedy queens, Pythonový Algorithm G, nativní implementace
a nezměněný Knuthův `infty-queens.w` souhlasí ve všech prvních 10 000 členech.
Celý vytištěný 28členný prefix je správný.

## Algorithm G: proč lze přeskočit velký interval

Před dalším krokem jsou vektory a,b,c indikátory použitých řádků,
součtů a rozdílů. Platí invarianty vytištěné v G2: s je nejmenší volný řádek,
rozdíly −r+1,…,t jsou obsazené a hraniční rozdíly −r a t+1 jsou volné.
Každá z těchto tří množin má přesně n prvků. V počátečním stavu jsou prázdné.

Po zvýšení n testuje G3 všechny možné řádky s≤k≤n−r. Řádky menší než s
už jsou obsazené; řádky n−r<k≤n+t blokuje invariant c. Pokud G3 nenajde
řešení, je k=n+t+1 volné: má nový rozdíl t+1 a leží nad každou předchozí
dámou, jejíž řádek je nejvýše (n−1)+t. Totéž platí pro jeho součet s n.
G4 jej tedy smí vybrat a prodloužit souvislý úsek kladných rozdílů.

G5 zaplní volný k≤n−r. Hodnota s se musí změnit právě při k=s;
levý okraj souvislého úseku c se musí změnit právě při k=n−r.
Příslušné smyčky najdou první nulu. Přidávají se tři dosud nepoužité bity,
takže invarianta pokračuje. Tím je dokázána shoda s greedy definicí pro
libovolný počet kroků, bez předpokladu zlatého řezu.

Pro měření používáme pořadí testů b,c,a z autorova programu. Rovnostní
podmínka v knize pořadí krátkého vyhodnocování neurčuje; jiné pořadí může
mít jiný počet přístupů, aniž by šlo o chybu algoritmu.

## Miliardový výpočet dokončen

Vlastní C++ překlad s bity balenými po 64 potřebuje pole odvozená z bezpečných
mezí t≤n, q_n≤2n a 2n+t≤3n, nikoli z nedokázané asymptotiky.
Dokončil **1 000 000 004 kroků**, návratový kód 0. Osm posledních hodnot je

```
618033989, 1618033985, 618033988, 1618033988,
1618033990, 1618033992, 1618033994, 618033991
```

Všech osm souhlasí s knihou. Bylo **5 725 793 906** přístupů k bitům,
průměr **5,7257938830968245**, maximum **19**. Vytištěné zaokrouhlení 5,726
je správné. Úplný histogram, příkaz, hash zdroje/binárky a hash celé
posloupnosti jsou v `results/greedy_queens/`. Desetitisícový kontrolní běh
má stejný histogram jako původní autorův program.

Tyto empirické výsledky nepředstavují důkaz meze 19 pro všechna n.
Kniha je také výslovně uvádí jako empirické.

## Výzkumný stav 37(b) a poslední domněnky v 38

[Ho, Greedy queens and the golden ratio, arXiv:2609.31336v2](https://arxiv.org/abs/2609.31336v2)
z 5. října 2026 tvrdí důkaz jak 37(b), tak užších intervalů z odpovědi 38.
Jde o **preprint** s počítačovým důkazem. Ověřili jsme formulace vět 1–2
a převod indexování q_k=1+q^Ho_{k−1}; externí důkaz zde nezávisle necertifikujeme.
Zdroj s kontrolním součtem je archivován. Novější výsledek není chyba knihy.

Historická citace [Dekking–Shallit–Sloane, EJC 27(1), P1.52 (2020)](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v27i1p52)
odpovídá článku vydanému 6. března 2020. Jeho případ celé roviny a případ
jediného kvadrantu se nesmějí zaměňovat. Záznamy
[A065188](https://oeis.org/A065188) a [A269526](https://oeis.org/A269526)
potvrzují orientaci matice a odkazují i na nový preprint.

## Errata a rozsah

Historická změna z 3. března 2021 doplňuje bibliografii odpovědi 37;
změna z 7. února 2021 přesouvá kontrolu k>n−r na začátek G3.
Obě už jsou zapracovány v našem 4B, zatímco starý PS má předchozí znění.
E026 eviduje tyto známé změny, nikoli nový nález.
F111 není opraveno ani v aktuálních, ani v historických prohledaných erratech.
Fyzický výtisk neověřen. Úlohy 37–38 jsou prošlé v tomto rozsahu;
neprohlašujeme vlastní vyřešení původně otevřené úlohy.
