# Quicksort: celé invarianty a úlohy 17–21

2026-11-07. Originál 113–117, zadání 135, odpovědi 630–631;
file = printed + 11. Sazba 114–116 a 631 znovu zobrazena; navazuje na
již zobrazené 113/630. Žádný matematický běh. Program MIX od 117 a
pravděpodobnostní úlohy 22 dál patří do dalšího bloku.

## P1032 — co přesně rozdělení řeší

Klíče mají úplné uspořádání, shodné hodnoty jsou dovoleny. Jestliže se
pivot uloží na pozici s a každý klíč vlevo je ≤ pivotu a každý vpravo ≥,
pak libovolné samostatné seřazení obou částí seřadí celek. Pivot nemusí
mít jednoznačnou výslednou pozici mezi shodnými klíči; má jednu platnou.
Podúlohy jsou disjunktní, přesuny uvnitř jedné nemění nerovnosti druhé.
Každá skutečná partition odstraní jeden pivot z dalších podúloh. Tím
vzniká konečný strom s nejvýše N partition uzly. Zde nezávislost znamená
nezávislost operací; pravděpodobnostní nezávislost bude zvlášť prokázána.
Záznamy zůstávají ve vstupním poli, navíc jsou jen mezníky, pivot a zásobník.

## P1033 — přesný zbytek v praktických formulacích (partial)

M má pevnou posloupnost komparátorů; B mění konec dalšího průchodu a Q
rozhoduje o dalším indexu po jednotlivých porovnáních. To plyne přímo z
jejich kroků. Jedna konkrétní scan smyčka Q je závislý řetězec a není
hotovou vrstvou nezávislých komparátorů. Bez modelu ale nelze uzavřít
obecné „inappropriate for parallel computations“ (113): disjunktní
podúlohy samotné lze provádět souběžně. Stejně nevymezené zůstává „seems
to be best“, „extremely fast on most computers“ (114), vhodnost teprve
pro „fairly large N“ a globální úspora režie při jediném insertion pass
oproti lokálním voláním (115). Nejde o nový nález: porovnání modelů a
historické tvrzení nejsou přesnou obecnou větou. Konkrétní MIX náklady
se budou ověřovat samostatně. Formální fakta: pivot je během fáze jediný
pevný klíč v registru a každá scan iterace mění jen jeden index.

## P1034 — Q1/Q2, doména a zarážky

N je kladné celé číslo, M≥1 celé. Pro N≤M se rovnou třídí insertion;
prázdný vstup lze stejně triviálně obsloužit, ale údaj floor(lg N) pak
není definicí kapacity. Pro N>M je aktivní [1,N]. V každém aktivním nebo
odloženém [l,r] platí r−l+1>M a K[l−1]≤K[k]≤K[r+1] pro všechny jeho
prvky. Základ dává (13). Partition níže vytvoří obě nové zarážky z
pivotu a zachová staré vnější. Proto indukce platí i po vyzvednutí
odložené části: práce v ostatních disjunktních částech její hranice
nepřepisuje. Q2 nastaví i=l, j=r+1 a K=K[l], čímž přímo vznikne (14),
včetně l≤i<j. Rovnost s oběma umělými krajními hodnotami nevadí.

## P1035 — Q3/Q4 a všechny krajní indexy

Na vstupu Q3 jsou K[k]≤K pro l−1≤k≤i a K[k]≥K pro j≤k≤r+1.
Při každém zvětšení i je přeskočený klíč <K; staré K[j]≥K zastaví scan
nejpozději na starém j. Na výstupu je K[i]≥K, vlevo od i vše ≤K.
Q4 nejprve sníží j, takže j≤r. Přeskočí jen klíče >K. Klíč K[i−1]≤K
zastaví scan nejpozději na i−1. Na výstupu tedy

    r ≥ j ≥ i−1 ≥ l,   K[i] ≥ K ≥ K[j].

Kromě dvou scan konců dál platí (14). Pravý scan nečte K[l−1]: nejhorší
zarážkou je původní pivot K[l]=K. Levý scan smí číst K[r+1], ale tuto
pozici nikdy nevyměňuje. Při pivotu rovném krajní zarážce scan zastaví
právě rovnost; nepotřebujeme ostrou nerovnost v (13).

## P1036 — Q5/Q6, křížení a partition

Je-li j>i, výměna vloží ≤K na i a ≥K na j, tedy obnoví celé (14).
Další Q3/Q4 posunou oba indexy alespoň o jeden. Žádný Q6 se proto
nemůže opakovat donekonečna. Je-li j≤i, předchozí mez připouští jen
j=i−1 nebo j=i. V druhém případě musí být K[i]=K[j]=K. V obou případech
jsou všechny pozice l..j−1 ≤K a j+1..r ≥K. Výměna l,j umístí pivot
na j; přemístěný K[j]≤K je na l, ostatní nerovnosti zůstanou.
Pro j=l jde o dovolenou samovýměnu. Tím je přesně dokázán postcondition
Q7, nejen existence nějakého rozdělovacího algoritmu.

## P1037 — každá větev Q7 a obrázek 19

Označme a=j−l, b=r−j. Jsou nezáporné, a+b=n−1 pro n=r−l+1.
Pokud min(a,b)>M, obě části mají práci: při b≥a se odloží pravá a
pokračuje levou; při a>b opačně. Tyto větve pokrývají i shodu délek.
Jestliže b>M≥a, zůstane jen pravá; jestliže a>M≥b, jen levá. Zbylý
případ a,b≤M přejde na Q8. Přesné nové mezníky dávají délky a,b a
splňují P1034. Každá nová aktivní část je kratší než původní, všechny
mají velikost >M. Potenciál „počet prvků ještě přítomných v aktivních a
odložených částech“ se každou partition sníží nejméně o jeden; pop sám
jej nemění. Po finitně mnoha partition/pop nastane Q9. Všechny šipky
obr. 19 odpovídají těmto případům, Q5 označuje srovnání i:j, takže
větev ≥ znamená j≤i. Známé doplnění závorky v Q7 (1998) význam nemění.

## P1038 — Q8 a správnost libovolného pořadí, úloha 19

Každá vložená položka označuje právě jednu nespracovanou disjunktní část
s platnými zarážkami. Vyzvednutí ji odstraní z čekající množiny a udělá
aktivní. Žádná se neztratí ani nespracuje dvakrát. Tento důkaz používá
množinu částí, nikoli pořadí jejich výběru; platí i pro FIFO. Po skončení
je pole souborem konečných bloků délky ≤M a jednotlivých pivotů, přičemž
každý klíč před pozdějším blokem je ≤ každému klíči v něm. Případné
inverze tedy leží jen uvnitř jednoho konečného bloku.

## P1039 — celý Q9, M=1 a význam varování na 117

Na začátku iterace j je prefix 1..j−1 seřazen. Je-li K[j−1]≤K[j],
je již seřazen i prefix j. Jinak se uloží celý R[j], a zprava se posouvá
souvislý suffix prefixu s klíči >K. Díra putuje doleva; K[0]≤K zaručuje
zastavení před čtením záporného indexu. Vložením uloženého záznamu do
díry vznikne seřazený prefix j a zachová se multiset záznamů. Rovné
klíče se přes sebe nepřesouvají. Posunů je přesně počet inverzí
odstraněných touto insertion; pro Q1–Q8 bez chyby jsou uvnitř bloků ≤M,
proto jejich součet je ≤N(M−1)/2 a Q9 má O(NM) operací, O(N) pro pevné M.
Při M=1 nezůstane žádná inverze a Q9 lze vynechat. Když je v Q1–Q8
chybná partition, ale stále zachová pole a zarážku, Q9 jej stejně seřadí
jako obecný insertion sort, potenciálně kvadraticky. Proto správný
výsledný pořádek sám netestuje správnost či čas partition části.

## P1040 — přesná místa použití umělých klíčů, úloha 17

K[N+1] čte Q3 pouze při r=N, když pivot je ostře větší než všechny
zbývající prvky aktivní části; při shodách může scan skončit dříve.
Při různých klíčích je to právě případ největšího pivotu, jak zní
odpověď. Obecná podmínka „largest key“ je dostačující popis možného
případu, nikoli tvrzení, že při každém maximu se shodami se zarážka čte.
K[0] se při partition nečte (P1035). V Q9 se čte právě tehdy, když
vkládaný klíč je menší než všechny předchozí, a tedy se přesune na 1.
To jsou příslušná nová levostranná minima. Dolní zarážka s rovností
zastaví stejně dobře. Úloha 17 je tím celá zodpovězena.

## P1041 — každá fáze příkladu a všech 17 výměn

V úvodní fázi 114 jsou dvojice Q6 (3,11), (5,10), (7,8); při stopu
i=8,j=7 a pivotová výměna je (1,7). Řádky nadepsané „1st exchange“
atd. ukazují stav *před* příslušnou výměnou, vyznačená čísla jsou přesně
scan konce. Tím vznikne levá část 275,87,154,61,426,170 a pravá
897,653,908,512,509,612,677,765,703, přesně jako v obou obrázcích.

Následující tabulka dává celý nezávislý ruční průchod tabulkou 2.
Nevypsané pozice se nemění; každá prostřední dvojice je Q6, poslední Q5.

| Aktivní [l,r] | Pivot | Q6 | Q5 | Nová aktivní část; čekající |
|---|---:|---|---|---|
| [1,16] | 503 | (3,11),(5,10),(7,8) | (1,7) | [1,6]; [8,16] |
| [1,6] | 275 | (5,6) | (1,5) | [1,4]; [8,16] |
| [1,4] | 170 | žádná | (1,4) | [1,3]; [8,16] |
| [1,3] | 61 | žádná | (1,1) | [2,3]; [8,16] |
| [2,3] | 87 | žádná | (2,2) | [8,16]; prázdný |
| [8,16] | 897 | (10,16) | (8,15) | [8,14]; prázdný |
| [8,14] | 765 | žádná | (8,14) | [8,13]; prázdný |
| [8,13] | 677 | (10,13) | (8,12) | [8,11]; prázdný |
| [8,11] | 509 | žádná | (8,8) | [9,11]; prázdný |
| [9,11] | 653 | žádná | (9,11) | [9,10]; prázdný |
| [9,10] | 512 | žádná | (9,9) | konec |

Po fázích 2–5 jsou postupně aktivní seznamy
(170,87,154,61), (61,87,154), (87,154) a pravá původní část.
Po fázích 6–10 jsou (765,653,703,512,509,612,677),
(677,653,703,512,509,612), (509,653,612,512), (653,612,512), (512,612).
Tím jsou ověřeny všechny hodnoty, závorky i mezníky tabulky.
Je 11 pivotových výměn a 6 výměn Q6: celkem 17, včetně čtyř
samovýměn. Netriviálních výměn je 13; údaj 17 je počet operací
popsaného algoritmu, nikoli minimum z úlohy 2. Parametr odpovídá M=1.

## P1042 — všechny shodné klíče, první část úlohy 18

V části délky n=r−l+1 se každý scan zastaví po jednom posunu. Při k-tém
testu Q5 jsou i=l+k a j=r+1−k. Test ukončí při 2k≥n, tedy k=ceil(n/2).
Q6 proběhne k−1=floor((n−1)/2)krát. Každý test používá dvě porovnání,
takže C=2ceil(n/2)=n+(n mod 2), A=1. Výsledný
j=l+floor(n/2)=ceil((l+r)/2), přesně horní zaokrouhlení v originálu.
Podčásti mají délky floor(n/2), ceil(n/2)−1, tedy rozdíl nejvýše jedna.
Q9 nic neposune. Označení „essentially in the best case“ odkazuje na
vyvážené velikosti; přesná časová optimalita (která závisí i na B) se
tím netvrdí a úloha 27 bude ověřena zvlášť.

## P1043 — změna < na ≤, druhá část úlohy 18

Rovné klíče přestanou být zarážkami. Když také (13) dovolí rovnost,
scan může už v první fázi utéci za vnější konec. Ani ostré (13) nestačí:
pro N>M a všechny vstupní klíče c levý scan skončí na N+1, pravý na 0;
Q5 zamění R[1] a R[0]. Tím je porušena i permutace vstupních záznamů.
Tato správná hlavní výstraha odpovědi 18 je doložena.

Její pokračování o třetí partition je ale chybné: již druhá není
definována. Po první výměně a Q7 zůstává [l,r]=[1,N], ale nový pivot
je původní K[0]<c a nová K[0]=c. Druhý Q4 přejde přes všechny hodnoty c,
přes rovný pivot na 1 a znovu přes c na 0, takže chce číst K[−1].
Samostatný minimální doklad a všechny vrstvy errat jsou v
`V3-C0030-quicksort-equal-key-trace.md`. Toto je lokální low vada
vysvětlení vadné varianty; správný algoritmus Q se nijak nemění.

## P1044 — FIFO velikost, druhá část úlohy 19

Berme pevné M a dokonale vyvážený strom s h partition úrovněmi:
například N=(M+1)2^h−1, takže spodní nespracované části mají délku M.
Každý vnitřní uzel hloubky <h−1 vloží pravé dítě do FIFO a pokračuje
ihned levým. Jedno vyzvednutí tedy zpracuje celou levou větev. Nazvěme
ji řetězcem; jeho kořen je počáteční kořen nebo pravé dítě nějakého uzlu.

Kořen řetězce označíme počtem k pravých hran na cestě od kořene. Každý
řetězec k vytváří pouze řetězce k+1. FIFO tudíž zpracuje celou vrstvu k
dříve než vrstvu k+1. Kořen řetězce s k≥1 v hloubce d má poslední hranu
pravou a mezi d−1 předchozími k−1 pravých, tedy binom(d−1,k−1)
možností. Součet přes k≤d≤h−1 je binom(h−1,k), podle Pascalova
součtu (rozdíl po sobě jdoucích binom(d,k)). Po skončení vrstvy k−1
jsou všechny tyto kořeny k současně ve frontě. Pro centrální k je počet
Θ(2^h/sqrt(h)), přímo ze Stirlingových mezí pro prostřední binomický
koeficient. To je Ω(N/sqrt(log N)) pro každé pevné M.

Při obecném N s co nejrovnějšími rozklady má strom úplný prefix
h=floor(lg((N+1)/(M+1))) partition úrovní. U nerovných dětí zde „levá“ označuje okamžitě zpracovanou menší část,
nikoli nutně geometricky levou část pole. Hlouběji přidané řetězce
nemění řazení podle k a nemohou zmenšit uvedený počet z prefixu;
stejná dolní mez tedy platí pro všechna dost velká N, nejen mocniny.
Konstanta závisí na M. Pokud by M rostlo s N, správný explicitní rozsah
je řád N/((M+1)sqrt(log(N/(M+1)))) pro N/(M+1) velké, nikoli uniformní
Ω(N/sqrt(log N)); kniha parametr v asymptotickém tvrzení drží pevný.
To dokazuje neobvyklý faktor sqrt(log N) i důvod, proč nejde o běžnou
BFS frontu velikosti Θ(N): levé větve se zpracují okamžitě.

## P1045 — zásobník, úloha 20, převzetí C0011

Přebírám uzavřený `V3-C0011-quicksort-stack-bound.md`: minimum pro k
současných položek je n_k=2^k(M+2)−1, tedy správná kapacita
max(0,floor(lg((N+1)/(M+2)))). N+2 v odpovědi je již potvrzená low
chyba, bez nové kontroly či nového nálezu. Hrubá floor(lg N) z hlavního
textu platí: (N+1)/(M+2)≤N pro N≥1,M≥1.

Zde doplňuji pouze realizovatelnost rovnosti, užitečnou i pro FIFO.
Libovolné předepsané dva výstupní seznamy L=(L1,...,La) < pivot < R
lze získat z počátečního (pivot,L2,...,La,L1,R), pro a>0: žádná Q6
není nutná, skeny se kříží za posledním menším a Q5 vrátí L1 na začátek.
Pro a=0 je pivot minimum a zbytek je přímo R. Indukcí od listů tedy
lze realizovat každý předepsaný strom ranků a požadované pořadí dětí.
Pro N větší než n_k se zvětší odložené dítě kořene, menší n_(k−1)
zůstane nezměněno; minimum tedy dává maximum pro každé N, ne jen n_k.

## P1046 — každý člen první fáze, úloha 21

Různé klíče lze přeznačit ranky 1..N. Pivot s skončí na j=s, protože
vlevo musí být právě všech s−1 menších klíčů. V Q5 nemůže být i=j:
pak by obě scan nerovnosti dávaly K[i]=K a pivot s před Q5 pořád stojí
na l=1, zatímco i≥2. Proto i=s+1. Levý ukazatel šel z 1 na s+1:
C'=s porovnání. Pravý šel z N+1 na s: C−C'=N+1−s, tedy C=N+1.

Nechť t počítá větší klíče mezi prvními s původními pozicemi, dle
známého zpřesnění formulace na 119 z roku 2007. Na pozici 1 je pivot,
takže t jsou přesně špatně umístěné větší klíče v 2..s; v s+1..N je
stejný počet menších. Každá Q6 vymění jednu dvojici těchto chybných
stran, žádná nesahá na již správnou stranu a chybný klíč se nikdy
nevrátí. Proto B=t. A=1 z definice fáze. Pro s=1 dostaneme C'=1,
C−C'=N, B=0; pro s=N pravý scan jen jeden, levý N, opět B=0.

## P1047 — nestabilita Q v odpovědi 13

M=1,N=2 a dva označené záznamy se shodným klíčem (a,b). Q3/Q4 se
zastaví s i=j=2, Q5 vymění pozice 1,2, a výsledkem je (b,a). Q9 nic
nezmění. Q tedy není stabilní. U každého pevného M lze stejně použít
M+1 shodných záznamů a nezanedbatelnou první pivotovou výměnu. Část M
odpovědi 13 je již prokázána, část R zůstává na audit radix exchange.

## Errata a vymezení

Pět vrstev je inventarizováno v `sources/exchanging-errata-review.json`;
pro novou přesnou vadu navíc `sources/quicksort-equal-key-trace-errata-review.json`.
Zohledněny závorka Q7 (116,1998), upřesnění prvních s klíčů (119,2007)
a interpunkce v odpovědi 18 (631,2016). Starší náhrada odpovědi 19
na prvním vydání 608 (1986) obsahuje právě zde prokázanou FIFO mez;
starší oprava 20 pouze přidala max(0,...) a C0011 neopravila.
Autorství Sedgewick/Singleton a hodnotící popis Hoareova článku
Comp.J.5(1962),10–15 nejsou znovu bibliograficky ověřovány. Nevydávám
je za matematický doklad ani za nový nález.
