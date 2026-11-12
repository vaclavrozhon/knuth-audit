# Tableaux44: všechny kroky průměrného počtu převratů

Zadání72/file83, odpověď615/file626, původní sazba zobrazená.
n≥1 je počet skutečných genů; níže se zvlášť vysvětluje,
proč ostrá nerovnost nepokrývá prázdný případ.
Definice grafu a dolní mez n+1−c se přebírají z P0606–07.

## P0622: počet formálních střídavých cyklů

Vyberme uspořádaný seznam k různých šedých hran z n+1 hran
a u každé vyberme jednu ze dvou orientací. Počet je
2^k(n+1)_(k), kde podtržený index je klesající faktoriál.
Spojme konec každé hrany se začátkem následující černou hranou,
včetně poslední s první. Dostaneme formální střídavý2k-cyklus.

Každý neorientovaný cyklus má přesně2k takových zápisů:
k voleb první šedé hrany a dva směry obcházení.
Všechny jsou různé, protože šedé hrany jsou různé a každá má
dva odlišné konce. Platí to i pro k=1, kdy dva směry zapisují
stejný dvoubarevný2-cyklus. Počet formálních cyklů je tedy

    2^k(n+1)_(k)/(2k).

Nejde ještě o počet cyklů realizovatelných fyzickou lineární
posloupností všech genů.

## P0623: všechny tři vytištěné nemožné příklady

Přidejme pro tento test ke stanoveným černým hranám pevné
vnitřní spojení kL—kR každého genu. Úplná fyzická posloupnost
musí tvořit jedinou cestu od0R do(n+1)L, ne uzavřený okruh.

- (1R,2L,2R,3L) vyžaduje černou hranu2L—2R uvnitř téhož
  genu; spolu s vnitřní hranou uzavírá samostatný okruh.
- (1R,2L,3L,2R,3R,4L) vyžaduje černé hrany2L—3L
  a2R—3R. S vnitřními hranami genů2,3 tvoří uzavřený okruh.
- (1R,2L,6R,7L,4L,3R,2R,3L,6L,5R) vyžaduje černé
  hrany2L—6R,3R—2R a3L—6L. Uzavřený fyzický okruh je
  2L—2R—3R—3L—6L—6R—2L.

Každý příklad proto opravdu patří do formálního počtu,
ale není součástí žádné přípustné lineární permutace.

## P0624: přesný počet doplnění každého realizovatelného cyklu

Pro1≤k≤n obsahuje zvolený cyklus k předepsaných černých
hran. Pokud je realizovatelný, spojení těchto hran s geny
nemá uzavřený okruh. Ani nesmí již spojovat obě pevné hranice:
cesta obsahující všech n genů by vyžadovala n+1 černých hran,
zatímco kratší cesta by znemožnila vložit zbývající geny.

Kontrahujme tedy tyto k vazeb. Z n genů a dvou pevných hranic
vznikne n+2−k cestových bloků. Dva různé bloky obsahují
pevné hranice; jejich umístění na začátku/konci i orientace
jsou určeny. Zbývá n−k volných bloků. Každý lze orientovat
dvěma způsoby a bloky lze libovolně uspořádat. Přesný počet je

    2^(n−k)(n−k)!.

Naopak každé takové uspořádání po rozvinutí bloků splňuje
všech k požadovaných černých hran, bez dalších podmínek.
Přidané hrany nemohou změnit zvolený střídavý cyklus:
všechny jeho vrcholy již mají obě příslušné hrany.
Počet doplnění je proto stejný pro každý realizovatelný cyklus,
nikoli jen horní odhad založený na nezávislosti hran.

## P0625: celý příklad k=5,n=9

Cyklus(0R,1L,9L,8R,7R,8L,1R,2L,5L,4R)
předepisuje černé hrany

    1L—9L, 8R—7R, 8L—1R, 2L—5L, 4R—0R.

Poslední nutí první gen−4. První tři spojují orientovaný
blok[−9,1,8,−7], čtvrtá blok[−2,5]. Volné geny jsou3,6.
Zbývající čtyři volné bloky tedy jsou

    A=[−9,1,8,−7], B=[−2,5], [3], [6].

Mají16·24=384 uspořádání za pevným−4, přesně
2^(9−5)(9−5)!. Záporná orientace A znamená[7,−8,−1,9],
záporná B znamená[−5,2]. To výslovně kontroluje všechna
znaménka knižních podřetězců i význam nahrazování symbolů1,2
v podepsané permutaci množiny{1,2,3,6}.

## P0626: očekávání jednotlivých počtů cyklů

Náhodný vstup je rovnoměrný na všech2^n n! podepsaných
permutacích. Pro každý realizovatelný2k-cyklus je jeho
pravděpodobnost podle P0624 rovna
2^(n−k)(n−k)!/(2^n n!). Sečtení indikátorů všech možných
cyklů dává E c_k; nezávislost indikátorů není potřeba.

Po nahrazení počtu realizovatelných cyklů větším formálním
počtem P0622 dostaneme pro1≤k≤n

    E c_k ≤ [2^k(n+1)_(k)/(2k)]
                      [2^(n−k)(n−k)!/(2^n n!)]
          = (n+1)/(2k(n+1−k))
          = (1/2)(1/k+1/(n+1−k)).

Zkrácení používá(n+1)_(k)=(n+1)!/(n+1−k)! a
(n−k)!/(n+1−k)!=1/(n+1−k); žádný záporný faktoriál
se tedy nepoužije.

## P0627: součet a přesný zdroj ostré nerovnosti

Sečtením pravé strany pro k=1,…,n dostaneme H_n,
protože oba harmonické součty jsou stejné.
Zbývající c_(n+1) je indikátor toho, že celý graf tvoří jediný
cyklus. Je tedy nejvýše1, a pro n≥1 má očekávání striktně
menší než1: kladná identita má n+1≥2 cyklů a kladnou
pravděpodobnost1/(2^n n!). Proto

    E c = Σ_(k=1)^n E c_k + E c_(n+1) < H_n+1.

Pro n=1 tento argument stále platí; identita má dva cykly,
záporný singleton jeden. Není třeba dokazovat striktnost
některého z předchozích jednotlivých odhadů.

Pro n=0 by graf měl jediný2-cyklus vždy a ostrý závěr by
neplatil:0 není>0−H_0. Závěr úlohy má tedy doménu
kladného počtu genů; prázdný případ se pod něj nepodsouvá.

## P0628: očekávaná vzdálenost

Pro každou jednotlivou permutaci platí d≥n+1−c (P0607).
Linearita očekávání spolu s P0627 dává

    E d ≥ n+1−E c > n−H_n.

Směr obou nerovností je správný; nepožaduje se rovnost
d=n+1−c, která obecně neplatí. Tím je hlavní úloha dokázána
bez výpočtu celé distribuce vzdáleností.

## P0629: závěrečný součin cyklů a skutečná konvence

Knuth násobí permutace zleva doprava: výslovně to stanoví
svazek1,§1.3.3,165/file180, odstavec k(4)–(5).
Tento dohledaný předpoklad je nutný pro součin
(1 2 3)(3 4 5)… v posledním odstavci odpovědi.

Při této konvenci lze přímo sledovat každou hodnotu.
Hodnota1 jde do2; další sudé hodnoty postupují na další
sudou; po největší sudé se jde přes největší lichou dolů
po lichých až do3 a zpět do1. Pro sudé n poslední
transpozice(n−1 n) vloží n před n−1. Součin je tedy cyklus

    (1,2,4,…,největší sudé≤n, největší liché≤n,…,5,3).

Je to inverze Gollanovy permutace

    γ_n=(1,3,5,…,největší liché≤n, největší sudé≤n,…,4,2).

Například n=4 dává jednopásmově2413, n=5 dává24153.
Při automatickém převzetí opačné konvence by vyšel jiný
objekt a nebyl by to platný protipříklad knižního tvrzení.

## P0630: přesná vnější věta pro nepodepsanou poznámku

Primární [Bafna–Pevzner1993](https://www.cs.sjsu.edu/faculty/khuri/HUT_2008/Bafna_1993.pdf),
definice γ_n na149 a Theorem3 na151, uvádí pro
**nepodepsané** převraty d(γ_n)=d(γ_n^−1)=n−1.
Tato přesná vnější věta je aplikovatelná podle P0629.
Její úplný grafový důkaz zde není znovu odvozen; prvotní
konferenční verze je dostupným primárním zdrojem tvrzení
později citovaného v SICOMP25(1996),272–289.

Že n−1 je horní mez v nepodepsaném problému, plyne také
přímo: pro i=1,…,n−1 obraťme úsek od pozice i po aktuální
výskyt hodnoty i. Tím ji ustavíme a předchozí pozice zůstanou
beze změny. Žádné dodatečné otočení znaménka není potřeba.
Inverze permutace má stejnou vzdálenost, protože obrácení
pořadí slova složeného ze samoinverzních převratů dává
slovo pro inverzní permutaci.

Není zde převzato silnější tvrzení o klasifikaci všech
nejhorších permutací ani zaměněna nepodepsaná vzdálenost
za podepsanou. Hlavní průměrná mez P0622–28 má vlastní
úplný důkaz a není na této historické poznámce závislá.
Žádná enumerace ani numerický běh nebyly spuštěny.

