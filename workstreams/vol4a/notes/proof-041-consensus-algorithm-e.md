# §7.1.1–31: přesná existence konsensu a algoritmus E

6. listopadu 2026, X0070. Zadání začíná p82/file99, pokračuje
p83/file100; odpověď p539/file556. Původní sazba přečtena.
Žádný program. Konsensus znamená největší podkrychli d⊆c∪c',
která není obsažena ani v c ani v c'; nestačí libovolný průnik.

## P0663: nutnost jediné protilehlé souřadnice

Nechť d je podkrychle obsažená v c∪c', ale v žádném z nich samostatně.
Definujme D jako množinu souřadnic i, kde c_i je pevný bit a d_i se
od něj liší (buď protilehlým bitem, nebo hvězdičkou). Analogicky D'
pro c'. Obě množiny jsou neprázdné, jinak by d bylo obsaženo v c
nebo c'.

Kdyby existovaly různé i∈D,j∈D', nezávislost souřadnic podkrychle d
dovolí zvolit v ní bod s x_i≠c_i a x_j≠c'_j. Tento bod není v c∪c',
spor. Proto D=D'={j} pro jediné j. Bity c_j,c'_j musejí být opačné:
kdyby byly stejné, bod d porušující tuto společnou hodnotu by byl
mimo oba. Současně d_j=*; jediný pevný bit by vyhovoval jednomu
z obou a neporušoval jeho podmínku.

Pro i≠j má d omezení kompatibilní současně s c_i i c'_i, takže
na žádné další souřadnici nemohou stát protilehlé pevné bity.
To dokazuje nutnost přesně jedné protilehlé souřadnice, včetně
jedinečnosti jejího indexu. Je to obecný důkaz, nikoli kontrola
jednoho obrázku či dvojice.

## P0664: postačitelnost, největší krychle a příklad

Mají-li c,c' právě jednu protilehlou pevnou souřadnici j, dejme
tam d_j=* a na všech ostatních souřadnicích průnik omezení:
shodný bit zůstává, bit proti hvězdičce dává tento bit, dvě hvězdičky
dávají hvězdičku. Podle j-tého bitu leží každý bod d v c nebo v c'.
Obě hodnoty j se v d vyskytují, takže d není obsaženo v žádném
jednotlivě. Každá jiná straddling krychle má podle P0663 stejné j
a na ostatních pozicích musí respektovat obě původní omezení;
je tedy podmnožinou d. Máme právě jeden největší konsensus.

Tím jsou dokázána všechna uvedená pravidla x⊔x=x⊔*=*⊔x=x,
x⊔¬x=* a *⊔*=*, i přesná podmínka jediného použití protilehlé
dvojice. Pro 000* a *111 jsou protilehlé dvě prostřední pevné
souřadnice. Konsensus proto neexistuje a každá podkrychle jejich
sjednocení leží v jednom původním členu, jak uvádí text.

## P0665: všechny rozměrové meze části (b)

Je-li r počet souřadnic, kde obě původní krychle mají hvězdičku,
výsledný konsensus má přesně r+1 hvězdiček: společných r a jednu
protilehlou pevnou pozici. Proto pro rozměry k,k',k'' platí

    k''=r+1,  tedy 1≤k''≤min(k,k')+1.

Zvlášť důležitý použitý okraj: pokud c má rozměr j a jeho konsensus
má rozměr j+1, všech j hvězdiček c je společných s druhou krychlí.
Na jiných pozicích konsensus nic nového neomezuje proti c, pouze
uvolní jediný pevný bit. Proto skutečně obsahuje c. Tento vztah
není automatický pro konsensus menšího rozměru.

## P0666: úplný invariant E2

V je pevné sjednocení původního vstupu. Při vstupu do E2 platí:

1. Všechny krychle aktuální C leží ve V a C je antichain.
2. C neobsahuje krychle dimenze menší než j.
3. Každá j-krychle obsažená ve V je obsažena v některém členu C.

Pro j=0 to platí po E1: každému bodu původního sjednocení zůstane
pokrývající vstupní krychle i po odstranění obsažených členů.
Žádná neprázdná krychle nemá zápornou dimenzi.

Pro indukční krok vezměme libovolnou (j+1)-krychli h⊆V a rozdělme
ji na dva j-buddies h_0,h_1. Z invariantu existují c_0,c_1∈C
s h_i⊆c_i. Je-li h⊆c_0 nebo h⊆c_1, má tento člen dimenzi alespoň
j+1, takže přežije odstranění j-krychlí v E4, nebo jej nahradí
ještě větší člen při absorpci.

Jinak h straddluje c_0∪c_1. Podle P0663/P0664 existuje konsensus
c_0⊔c_1 obsahující h, tedy dimenze alespoň j+1. E3 jej proto
zařadí do C'. E4 jej ponechá nebo absorbuje větší krychlí, která
h také obsahuje. Každá (j+1)-krychle má tedy po E4 pokrytí.
Konsensus leží v unii svých rodičů, a tudíž ve V; absorpce
nepřidává body a ponechává antichain. Odstranění všech j-krychlí
zaručí druhou podmínku pro nové j+1. To dokazuje všechny tři
části invariantu v každé iteraci, nikoli jen coverage vybraných bodů.

## P0667: přesné kritérium výstupu E3

Je-li j-krychle c∈C maximální ve V, nemůže její konsensus s jiným
členem C mít dimenzi j+1: podle P0665 by byl větší krychlí ve V
obsahující c. Proto ji E3 vypíše.

Naopak, pokud c není maximální, lze ve V uvolnit jednu její pevnou
souřadnici. Dostaneme (j+1)-krychli h=c∪b, kde b je j-buddy c.
Z invariantu E2 je b obsažen v nějakém d∈C. Protože C je antichain
a c∈C, máme c⊄d; také h⊄c a h⊄d. H tedy straddluje c∪d.
Jejich konsensus existuje a obsahuje h; P0665 současně omezuje
jeho dimenzi na nejvýše j+1. Je proto právě h a E3 jej najde
v C'. Není odstraněn filtrem dimenzí≤j a zabrání vypsání c.

E3 tedy vypisuje právě maximální j-krychle mezi členy C. Každá
maximální j-krychle V v C skutečně je: invariant ji obsahuje v
nějakém členu C a maximalita nutí rovnost. Tím je doložena nejen
správnost vypsaných krychlí, ale úplnost výstupu daného rozměru.

## P0668: ukončení, žádné duplicity a okraje E

Po E4 se j zvětší o1 a všechny krychle předchozího rozměru jsou
odstraněny. Jedna krychle se tedy nemůže vypsat ve dvou iteracích,
a množinová reprezentace C vylučuje duplicity uvnitř jedné iterace.
Nejpozději při j=n je v C možná jen celá n-krychle. Pokud existuje,
vypíše se, nové větší konsensy neexistují a C se vyprázdní.
E2 pak skončí; provedeno je nejvýše n+1 iterací E3.

Je-li C prázdná už při dřívějším E2, invariant vylučuje všechny
j-krychle ve V, a tím i každou větší krychli. Všechny maximální
nižší dimenze byly předtím vypsány. Prázdný vstup skončí hned,
jediná krychle bez možného konsensu se vypíše při své dimenzi.
Nulární neprázdný případ má jediný bod a stejný argument j=0.
V průběhu není třeba explicitně vytvářet množinu všech bodů V.

## P0669: konkrétní konečná realizace jednotlivých operací

Pro dvojice masek (a,b),(a',b') z30 označme

    D=(b XOR b') & NOT(a OR a').

To jsou přesně protilehlé pevné souřadnice. Konsensus existuje právě
když D≠0 a D&(D−1)=0. Jeho masky pak jsou

    A=(a&a') OR D,     B=(b OR b') & NOT D,

ve významu n-bitových komplementů. P0664 dokazuje obě formule
souřadnici po souřadnici. Podmínka obsažení c(a,b)⊆c(a',b') je

    a & NOT a'=0,     (b XOR b') & NOT a'=0.

První vyloučí volný bit menší krychle tam, kde větší požaduje
pevný; druhá ověří všechny pevné hodnoty větší krychle. Formule
jsou obousměrné. Je tak k dispozici přímá realizace konsensu
i absorpce, nikoli neproveditelný existenční krok.

Při bitových polích lze každou dvojici zpracovat v O(n), případně
konstantně v n-bitovém slovním modelu kromě spočtení dimenze.
Dimenzi lze získat obyčejným O(n) průchodem nebo udržovaným údajem.
Vytvoření všech dvojic C×C i absorpce v konečném sjednocení proto
končí. Algoritmus zde netvrdí polynomiální celkovou velikost
mezivýsledků nebo výstupu. Odkaz na další bitové techniky v7.1.3–142
se tím neprohlašuje za kompletně auditovanou samostatnou úlohu.

## Errata, vazba na C0002 a rozsah

Všechny matematické části (a)–(c), příklad i argumenty odpovědi31
jsou doloženy. Relevantní all4a-pre/all4a/err4a/all4f0/err4f0
neobsahují změnu algoritmu31; známá oprava z21.12.2013 upravuje
historickou atribuci Archie Blake. Bibliografické citace Blake,
Samson–Mills, Quine, Robinson, Ewing–Roth–Wagner zůstávají výslovně
neověřené, nejsou použity jako matematické předpoklady.

C0002 se týká jiného použití generalized consensus na p120.
P0663–P0664 potvrzují přesnou doménu obyčejného konsensu: dvě
kompatibilní různé krychle bez protilehlého bitu jej nemají.
Tím se automaticky nerozhoduje, zda známá oprava odpovědi32 na540
má být redakčně přenesena i na120; stav C0002 se zde nemění.
Další úloha32 vyžaduje samostatný obecný argument více krychlí.
