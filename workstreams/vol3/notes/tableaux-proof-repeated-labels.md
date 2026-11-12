# Opakované štítky: doplnění matematické zmínky na58

P0445–0447 dokládají samotnou existenci zobecněné korespondence,
odděleně od neověřených historických citací na58. Není třeba vnější
věta ani nový výpočtový běh: použijeme již dokázanou bijekci pro různé
štítky a následující obecné porovnání dvou vkládacích cest.

## P0445: dva sousední vstupy a sloupce jejich nových rohů

Vložme do libovolného tableau postupně dva různé chybějící prvky
x,y. Tvrdíme: nový roh druhého vložení je striktně vpravo od nového
rohu prvního právě tehdy, když x<y. Při x>y je slabě vlevo a ve
striktně nižším řádku.

Nechť první cesta v řádku i nahradí pozici r_i hodnotou x_i a vytlačí
x_(i+1); r_i se slabě zmenšují podle P0390. Pro x<y začne druhá
cesta napravo od r_1, protože na r_1 už stojí x<y. Dokud obě cesty
pokračují, platí indukcí y_i>x_i a druhá pozice je>r_i. Pokud
vytlačí konečný klíč, ležel v původním řádku napravo od starého
x_(i+1), takže y_(i+1)>x_(i+1). Pokud první cesta skončila v řádku s,
na r_s připojila nový poslední prvek. Druhá cesta v tomto řádku
nemůže pokračovat: napravo od r_s již najde∞ a skončí. Skončí tedy
v řádku t≤s a její sloupec je>r_t≥r_s. To dokazuje první směr.

Pro x>y je v každém společném řádku druhá pozice≤r_i, protože
v r_i už stojí x_i>y_i. Při přísně levější pozici vytlačí hodnotu
<x_i; při stejné vytlačí právě x_i. Její další přenášená hodnota
je tedy≤x_i<x_(i+1), dokud první cesta pokračuje. V žádném z těchto
řádků nemůže druhá cesta skončit, protože její vybraná buňka je
konečná. To platí i v řádku s nového rohu první cesty: je tam již
konečné x_s. Druhá pokračuje níže a její další sloupce se nezvětšují,
proto konečný sloupec≤r_s. Oba případy pokrývají všechny dva různé
klíče a dokazují také potřebnou opačnou implikaci o pravém rohu.

## P0446: konstrukce pro oba opakované seznamy

Vezměme konečný multiset dvojic(q,p) z dvou úplně uspořádaných
abeced. Seřaďme jej lexikograficky podle q a při shodě podle p.
Vzniklé sloupce očíslujme i=1,…,n. Každému q přidejme pořadové číslo
jeho výskytu v tomto seznamu, každému p obdobně pořadí jeho výskytu.
Ve výsledných značkách q*,p* se nejprve porovnává původní hodnota
a potom pořadové číslo. Všechny q* i všechny p* jsou různé a q*
vstupují vzestupně; lze tedy přímo použít dokázaný Theorem A.

Výsledek(P*,Q*) je dvojice obyčejných tableaux. Po zapomenutí
pořadových čísel jsou řádky obou alespoň neklesající. Dokážeme,
že sloupce zůstávají striktní, tedy dostaneme semistandardní tableaux.

Stejné původní q tvoří souvislý vstupní blok. Jeho p* rostou,
protože původní p jsou v něm neklesající a pořadová čísla shodných
p rostou. Podle P0445 proto nové rohy během tohoto bloku leží ve
striktně rostoucích sloupcích. To jsou neměnné pozice daného bloku
q* v Q*, takže po smazání značek nemohou být dvě stejná q ve sloupci.

Pro P* použijeme symetrii Theorem B: v inverzním biwordu, seřazeném
podle p*, se opakované původní p čtou podle původních vstupních i.
Odpovídající q* jsou proto striktně vzestupné. Jeho recording tableau
je P*, a stejný argument P0445 tedy dává různé sloupce všem kopiím
téhož p. Oba zapomenuté výsledky mají slabé řádky, striktní sloupce,
stejný tvar a správné multimnožiny hodnot.

## P0447: inverze a skutečná bijekce

Naopak vezměme libovolnou dvojici takových semistandardních tableaux
P,Q stejného tvaru. Kopie každé stejné hodnoty označme v pořadí
zleva doprava podle sloupce. Mají různé sloupce, takže označení je
jednoznačné. Pořadové číslo rozliší shody v řádcích a nemůže porušit
sloupcovou nerovnost mezi původně různými hodnotami. Dostaneme
obyčejná tableaux P*,Q*, na něž se vztahuje úplná inverze Theorem A.

Ve výsledném různě označeném biwordu jsou q* seřazené. V souvislém
bloku jedné původní hodnoty q jsou jejich buňky v Q* označeny po
rostoucích sloupcích. Jsou to časově po sobě vytvořené rohy, takže
opačná implikace P0445 nutí rostoucí vložené p*. Po zapomenutí
značek jsou tedy p uvnitř stejného q neklesající: získaný biword
je přesně lexikograficky seřazený multiset dvojic.

Ještě je třeba ověřit, že značky p* jsou pořadí výskytu, nejen
nějaké náhodné rozlišení. Aplikujme znovu symetrii na inverzní
biword. Značky stejných původních p v recording tableau P* jsou
po rostoucích sloupcích, proto příslušné vložené q* rostou. To
znamená, že kopie každého p se ve vstupním seznamu vyskytují právě
v pořadí svých značek. Značky q* tuto vlastnost mají už ze seřazení.
Standardizace rekonstruovaného multisetu tak vrátí přesně původní
označený biword. Oba směry jsou vzájemně inverzní.

Při různých q dostaneme specializaci s opakovanými p a obyčejným
recording tableau; při opakovaných q i p obecnou dvojici
semistandardních tableaux. Ekvivalentně se multiset dvojic popíše
konečnou maticí jejich nezáporných celočíselných četností. Prázdný
vstup dává prázdný pár. Tím je matematická zmínka na58 doložena,
aniž by se tvrdilo ověření podoby nebo prvenství citovaných prací.
