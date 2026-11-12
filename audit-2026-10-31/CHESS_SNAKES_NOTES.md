# Šachoví hadi, úloha172

Kontrola 1. 11. 2026. **Novou chybu jsme v ověřeném rozsahu nenašli.**
Byly zapracovány známé opravy z roku2023, zejména 72 místo36
střelcových cyklů a46 139 040 místo47 691 936 tříd věžových cest
s krajním bodem typu(0,1), ale bez rohového krajního bodu.

## Úplné výsledky pro8×8

Délka cesty je počet hran, tedy o1 menší než počet obsazených polí.
Délka cyklu je počet polí. Třídy jsou modulo osm symetrií celé desky.

| Figura | Max. délka cesty | Tříd nejdelších cest | Max. délka cyklu | Tříd nejdelších cyklů |
|---|---:|---:|---:|---:|
| král | 31 | 16 | 31 | 6 |
| jezdec | 33 | 1 | 32 | 4 |
| střelec | 12 | 32 | 12 | 72 |
| věž | 14 | 203 222 880 | 16 | 12 706 992 |
| dáma | 12 | 2 | 13 | 5 |

Celkový počet tříd věžových cest kniha neuvádí; je zde doplňujícím
výsledkem. Všechny ostatní hodnoty souhlasí s knihou po opravách.

Při pevném počátečním rohu mají nejdelší cesty krále, jezdce,
střelce a dámy po řadě34,26,64,268 poloh a16,13,32,134 tříd.
Pouhé dělení králova počtu dvěma nestačí: jedna třída má oba
konce v rozích a započítala by se podruhé. Obě zmíněné zvláštní
dámské cesty délky11 jsou jedinečné: jedna obsahuje i protější roh,
druhá začíná krokem(0,0)→(1,1).

Nejdelší cesty krále, jezdce, střelce a dámy jsou asymetrické. U jezdcových cyklů mají
tři třídy orbitu4 a jedna orbitu8, tedy20 poloh. Ostatní cykly mají
orbity8: král48, střelec576 a dáma40 poloh.

## Přímý výčet a nezávislá kontrola

`chess_snakes.cpp` rozšiřuje indukovanou cestu pouze o souseda
posledního vrcholu, který není sousedem žádného dřívějšího vrcholu.
U cyklů ponechá možnost závěrečné hrany k prvnímu vrcholu; takový
krok cyklus uzavře a nelze jej dále rozšiřovat. Počet ještě dostupných
polí je bezpečná horní mez, použitá k ořezu větví pod hledanou délkou.

Pro cesty začíná výčet v20 buňkách pokrývajících všechny orbity buněk
(některé dvakrát). Pro cykly jsou další buňky větší než počáteční a
druhý vrchol menší než poslední. Žádná třída nechybí: v každé orbitě
cyklu lze zvolit obraz s nejmenším možným nejnižším vrcholem; tento
vrchol musí být zástupcem své orbity buněk. Zbylé duplicity se odstraní
přesným výpočtem všech osmi obrazů celé množiny.

Celý algoritmus prošel nezávislou kontrolou **všech podmnožin** desek
2×2,3×3,4×4 pro všech pět figur a oba druhy hadů. Všech30 množin
tříd souhlasí. Každý velký svědek byl samostatně ověřen podle stupňů
indukovaného grafu a jeho souvislosti. Běhy8×8 jsou úplné, bez timeoutů;
prohledaly i možnost delších objektů. Největší měl70 421 872 uzlů.
Výstupy, úplné svědky a počty jsou v `results/chess_snakes/`.

## Věž: obecné kombinatorické důkazy

Věžový graf je hranový graf K_(n,n): pole(r,c) odpovídá hraně mezi
řádkem r a sloupcem c. Indukované cesty a cykly délky alespoň4 odpovídají prostým
cestám a cyklům v K_(n,n). Maximální cesty tedy mají2n−1 polí
a cykly2n. Zde používáme n=8; kontrolní úplné permutační výčty
v `rook_snakes.cpp` pokrývají také všechna n=2..6.

Maximální cestu určí dvě permutace p,q jednoznačně, když začneme
v jejím jediném řádkovém krajním vrcholu K_(n,n). Proto je poloh n!².
Žádná není invariantní při čtvrtotáčce, půlotáčce ani vodorovném či
svislém zrcadlení: symetrie prosté cesty je nejvýše obrácení a jeho
působení na bipartici a pevných vrcholech nesouhlasí s těmito mapami.
Každé diagonální zrcadlení fixuje n! poloh, protože druhou permutaci
určí první. Burnside proto dává (n!²+2n!)/8, pro n=8 celkem203 222 880.

U cyklů zafixujeme p0=0 a q0<q1. Tím dostaneme n!²/(2n) poloh,
pro n=8 přesně101 606 400. Diagonálně pevné cykly odpovídají
q_j=p_(k−j mod8); je jich20 160. Půlotáčkově pevné splňují
p_(j+4)=7−p_j a q_(j+4)=7−q_j, celkem9 216. Průnik má192 prvků.
Všechny tyto malé množiny byly explicitně vytvořeny a geometricky
ověřeny v `verify_rook_symmetry.py`.

Vodorovná/svislá reflexe fixuje osm vrcholů jedné části K_(8,8),
což neidentická symetrie cyklu nemůže. Čtvrtotáčka by musela být
rotací abstraktního16-cyklu o4 nebo12 kroků; ta ale zachovává
bipartici, zatímco otočení desky o90° ji vyměňuje. Jejich počty jsou
tedy nula. Burnside dává (101606400+9216+2·20160)/8=12 706 992.

Pro cesty s rohovým koncem vynutíme první krok dolů. Je jich
F=(n−1)!². Pokud i druhý konec leží v rohu, může to být jen opačný
roh. Z A=(n−2)!² takových poloh má B=(n−2)! příslušnou diagonální
symetrii; odečteme tedy (A−B)/2. Pro n=8 vyjde25 142 760.

Pro začátek(0,1) a druhý konec mimo rohy máme2N poloh, kde
N=F−2A, podle dvou orientací první hrany. Další konec typu(0,1)
může být v pěti buňkách: obrazy při transpozici, antitranspozici,
půlotáčce a obou čtvrtotáčkách. Každá má2A poloh. Dvě diagonální
možnosti mají po2B pevných poloh; ostatní žádné. Odstraněním
dvojího ukotvení odečteme5A−2B a dostaneme2F−9A+2B, pro n=8
právě46 139 040 podle opravy2023. Vzorce souhlasí i s úplnými
výčty n=4,6.

## Rozsah

Obecné MCC kódování stupňů je správné, když se z výstupu odstraní
nesouvislé komponenty. Známé odstranění trojúhelníkových možností
je bezpečné při hledání uvedených delších cyklů a cest. Obrázky knihy
nebyly přepsány. Obecné Beluhovovy věty pro libovolně velké desky
a jejich asymptotiky zde znovu nedokazujeme; ověřeny jsou konkrétní
počty8×8 a uvedené kombinatorické vzorce pro věže.
