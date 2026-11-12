# §5.2: počítací třídění, programy a úlohy1–9

Znovu zobrazeny původní73–79/files84–90 a odpovědi615–616/
files626–627. Jde o nové jednotlivé argumenty k dřívějšímu
rychlému čtení. Pět vrstev přebírá
`sources/insertion-errata-review.json`; známé změny76/77
jsou jazykové či opravují číslo tabulky, ne nový nález.
Přesný důkaz C0009 se přebírá bez opakování programu.

MIX náklady níže mají obvyklou jednotku u: načtení,
uložení, ADD a CMP stojí2u; nastavení/zvýšení registru
a skok1u. Oblasti paměti jsou disjunktní, adresy i indexy
reprezentovatelné a celé záznamy zde mají jeden word,
pokud se výslovně nemluví o obecné délce. Hotové MIX
smyčky vyžadují N≥1; prázdný vstup se zachytí před nimi.
Abstraktní algoritmy mají přirozené prázdné smyčky.

## P0644: pět čísel a principy uvedených rodin

Úvodní výzvu řeší například výběr: na i=1,…,4 najdeme
minimum v R_i,…,R_5 a prohodíme je s R_i. Invariant:
prefix obsahuje i nejmenších hodnot ve správném pořadí;
indukce dokazuje výsledek. Je třeba4+3+2+1=10 porovnání
a nejvýše4 výměny. Stejný důkaz platí pro libovolné N.

Vkládání zachovává setříděný prefix vložením dalšího klíče
mezi jeho posledního menšího/rovného a prvního většího
souseda. Výběr zachovává prefix nejmenších klíčů.
Výměna libovolného špatně uspořádaného páru x>y na
pozicích i<j zmenší počet přísných inverzí: zmizí
koncový pár a u mezilehlého z zmizí dvě inverze pro
y<z<x, jedna pro z=x nebo z=y, jinak žádná. Počet
tedy klesne nejméně o1; žádná dostupná špatná dvojice
znamená setřídění. Počítání pořadí je dokázáno v P0647.
Úvodní klasifikace není tvrzení o úplnosti všech možných
algoritmů; E–G jsou autorovy možnosti/žert, ne další věty.

## P0645: adresy, seznamy, satelity a oba obrázky75

Pro libovolnou permutaci p dává tabulka adres p(1),…,p(N)
přístup k záznamům v témž pořadí jako jejich fyzické
přemístění. Seznam s HEAD=p(1), LINK(p(i))=p(i+1)
a LINK(p(N))=0 vrací tutéž posloupnost. Nesmí obsahovat
cyklus nebo chybějící/duplicitní záznam; z tabulky právě
popsanou konstrukcí žádný takový problém nevznikne.
Obráceně N různých uzlů úplného seznamu určuje p.

V Fig6 jsou původní klíče89,37,41; cílová tabulka
ukazuje na R_2,R_3,R_1, tedy37<41<89. Ve Fig7 vede
HEAD na R_2, pak R_3, pak R_1 a0. Všechny šipky
a konec seznamu souhlasí. Satelitní data zůstávají
spojena s původním klíčem.

Při délce záznamu ℓ slov stojí přesun celého záznamu
Θ(ℓ), přesun jeho adresy Θ(1). Proto může být tabulka
adres výhodná; nejde o tvrzení nezávislé na modelu
přístupu do paměti. Přidání kopie krátkého klíče k adrese
zachová pořadí a odstraní nepřímé čtení při porovnání.
To dokládá smysl keysortingu, nikoli univerzální časový
poměr na libovolném hardwaru.

## P0646 — partial: přesun s jedním záznamem a „asi dvakrát“

Přímé kopírování do oddělené oblasti velikosti N záznamů
je správné: pro každé i uložíme původní R_(p(i)) do S_i.
Každý záznam se přečte/zapíše jednou a vstup se nezničí.
Čas je Θ(Nℓ), paměť záznamů2Nℓ plus reprezentace p.

Odkaz na metody s jedním pomocným záznamem je nyní
uzavřen přesnými invarianty P0660–61 a P0669–75
v `internal-proof-10-11-cycles.md` a
`internal-proof-12-list-rearrangement.md`; samotný tento
odstavec tyto algoritmy nedokazoval. Tvrzení „usually about
twice as fast“ nemá specifikovanou délku záznamu,
cenu nepřímého přístupu ani distribuci permutací.
Z pouhého počtu záznamů se faktor2 neodvodí. Tento
konkrétní modelový/empirický údaj zatím zůstává
neověřený; není označen za chybu ani skryt v bibliografii.

## P0647: Algorithm C, skutečný invariant a úloha2

Rozšiřme klíč K_i o původní index: L_i=(K_i,i) v
lexikografickém pořadí. Všechny L_i jsou různé. Pro
zpracovanou množinu neuspořádaných dvojic E platí

    COUNT[i]=#{j:{i,j}∈E a L_j<L_i}.

Zpočátku E=∅. C4 pro dvojici j<i přidá právě většímu
L jednu jednotku: při K_i<K_j zvítězí j, jinak i,
včetně rovnosti klíčů. Invariant se tedy zachovává.
Po všech dvojicích COUNT[i] je přesný počet menších
L, a COUNT[i]+1 je jeho jednoznačná hodnost1,…,N.
To dokazuje sortedness, žádné kolize a stabilitu:
pro stejné klíče s j<i je L_j<L_i a R_j předchází R_i.

Pro původně různé klíče jde prostě o počet přísně
menších klíčů; příklad27 menších dává pozici28.
Při opakování se slovní výraz „menší klíče“ zpřesňuje
právě pomocí L, jak vysvětluje odpověď2.

Pokud p označuje seznam původních indexů ve výstupním
pořadí, pak p(COUNT[i]+1)=i: tabulka COUNT+1 dává
inverzní permutaci, nikoli přímo p.

## P0648: počet dvojic, libovolné pořadí a úloha1

Z N² uspořádaných porovnání vyřadíme N diagonálních
a z každé zbývající dvojice opačných směrů ponecháme
j<i. Zbude A=N(N−1)/2, méně než polovina N² pro N>0.
Smyčky C2/C3 každou takovou dvojici navštíví právě
jednou. Pořadí sčítání v invariantu P0647 je libovolné,
takže obě navržené vzestupné smyčky fungují, i současně.

Paralelní provedení znamená sečtení dílčích příspěvků
nebo atomické inkrementy; nesynchronizované přepsání
stejného COUNT by nebylo realizací tohoto algoritmu.
Při čtení záznamů můžeme každý nově příchozí porovnat
se všemi dřívějšími a zpracovat tytéž dvojice.
Abstraktní N=0/1 má nula dvojic a správný výsledek.

## P0649: celý Program C, obr8 a přesný čas

01–04 nulují COUNT[N],…,COUNT[1]. 05–06 vstoupí
do20, kde j=i−1;21 skončí právě pro i=1. Jinak07
načte K_i do A a08 aktuální COUNT[i] do X.
09–10 porovnají s K_j. Je-li K_i<K_j,11–13 zvýší
COUNT[j] a14 přeskočí přírůstek X; jinak15 zvýší X.
16–17 postupně zpracují j=i−1,…,1. 18 vrátí X
do COUNT[i],19 zmenší i a20–21 zahájí další smyčku.
Žádný záznam se nepřepíše. I pro N=1 se po nulování
správně přeskočí všechna porovnání.

Fig8 odpovídá přesně i=N,…,2 a j=i−1,…,1;
výstupy i=1 a j=0 jsou správné, nikoli další iterace.
Počet drahých větví11–14 je

    B=#{(j,i):j<i a K_j>K_i}.

Všechny vytištěné četnosti nyní vyplývají ze smyček.
Pro kontrolu součtu seskupme čas:

| instrukce | čas/u |
|---|---:|
|01,05,06|3|
|02–04|4N|
|07,08,18,19|7(N−1)|
|20–21|2N|
|09,10,16,17|5A|
|11–14|6B|
|15|A−B|

Celkem T_C/u=13N+6A+5B−4. Pro N=1 je to9,
ve shodě s přesně provedenými instrukcemi.

## P0650: všechny zobrazené řádky počítací tabulky77

Známá oprava mění nadpis Table2 na Table1. Po dokončení
řádku i je COUNT[i] již konečná hodnost; předchozí
pozice dostanou jednotku právě tehdy, mají-li větší klíč.
Pro šest vytištěných mezikroků jsou množiny těchto
zvyšovaných dřívějších pozic a konečný nový COUNT[i]:

| i, K_i | dřívější zvýšené pozice | COUNT[i] |
|---|---|---:|
|16,703|5,7,15|12|
|15,765|5,7|13|
|14,677|5,7|11|
|13,612|5,7,9|9|
|12,509|3,5,7,9|7|
|11,154|1,3,5,6,7,8,9,10|2|

Od nulového řádku dávají tyto přírůstky přesně všechny
vytištěné mezihodnoty, včetně již ustavených posledních
sloupců. Seřazené klíče jsou

    61,87,154,170,275,426,503,509,512,612,653,677,703,765,897,908.

Jejich nulové hodnosti v původním pořadí jsou

    6,1,8,0,15,3,14,4,10,5,2,7,9,11,13,12,

přesně poslední řádek tabulky. Není zde nový programový
test ani opakování starých Shellsort běhů.

## P0651: statistiky, extrémy, průměr a příklad1129u

Pro různé rovnoměrně permutované klíče přebíráme
P0079/P0088–89, `notes/inversions-proof-main.md`:

    0≤B≤A,  E B=A/2,
    var B=N(N−1)(2N+5)/72,
    σ_B=sqrt(N(N−1)(N+2.5))/6.

Oba krajní vstupy existují (vzestupný a sestupný).
Dosazení do P0649 dává3N²+10N−4 a
5.5N²+7.5N−4; průměr je4.25N²+8.75N−4,
přesně jejich aritmetický průměr. Čitatel pod odmocninou
a dělení6 v sazbě jsou konzistentní; nepřesouvá se6
chybně pod odmocninu. Při opakovaných klíčích se
pravděpodobnostní vzorce bez dalšího nepoužívají.

Počty větších předchůdců šestnácti klíčů příkladu jsou

    0,1,0,3,0,3,1,4,2,5,8,4,3,2,2,3,

jejich součet je41. Tedy A=120 a
13·16+6·120+5·41−4=1129. To dokládá i údaj78.

## P0652: kvadratická cena a dopředná možnost N log N

Samotná množina A párů nutí tento algoritmus vykonat
Θ(N²) porovnání, a přesný čas má totéž tempo.
Čtyřnásobek po zdvojnásobení N se vztahuje k hlavnímu
kvadratickému členu; nižší členy nedávají přesnou
rovnost T(2N)=4T(N).

Dopředné tvrzení o jiných metodách má samostatný svědek:
rozdělme vstup na dvě téměř stejné poloviny, rekurzivně
je setřiďme a slijme postupným výběrem menšího prvního
zbývajícího prvku. Invariant slití dává setříděný výstup;
na každé úrovni se zpracuje nejvýše N prvků, úrovní
je nejvýše⌈lg N⌉. Celkový čas je O(N log N) v modelu
konstantních porovnání/přesunů záznamu. Žádná domněnka
o zrychlení právě párového počítání z toho neplyne.

## P0653: úloha3, změna ostrého testu

Test K_i≤K_j přidělí při rovnosti přírůstek j, ne i.
Invariant P0647 pak používá různé klíče(K_i,−i).
Výsledek je stále setříděný, ale každá skupina stejných
klíčů má opačné původní pořadí. Dvojice shodných klíčů
stačí pro ztrátu stability. Pokud E je počet takových
dvojic, drahá větev Programu C se provede B+E krát,
takže čas vzroste právě o5E u. Pro různé klíče je stejný;
slovní „slower“ se týká nenulových rovností.

## P0654: úloha4, dokončení a cena

Program odpovědi nastaví i=N; načte j=COUNT[i] a R_i,
uloží do OUTPUT+1+j, zmenší i a opakuje do1.
Podle P0647 jsou cíle1+j právě všechny pozice1,…,N
a každý záznam jde na svou stabilní hodnost. Oddělený
výstup chrání dosud nepřečtené záznamy. Pět instrukcí
opakované části stojí2+2+2+1+1=8u, počáteční ENT1
stojí1u. Přesný čas je(8N+1)u.

## P0655: úloha5, invariant upraveného registru i úspora

Po08a je X=starý COUNT[i]+i−1. Za každou přísnou
inverzi se nyní X zmenší v14 a COUNT[j] se stejně
zvýší; za ostatní dvojice se X nemění. Na konci tedy
X vzrostl právě o počet j<i s K_j≤K_i. To je přesně
původní C, včetně stejných klíčů a stability.

08a stojí navíc N−1 instrukcí. Vynechaná15 šetří A−B;
náhrada JMP za DECX má stejnou cenu. Celková úspora je

    Δ=A+1−N−B.

Zlepšení není univerzální: sestupný vstup má Δ=1−N.
Je přesně kladné tehdy, když počet neinverzí>N−1.
Pro rovnoměrné různé klíče je EΔ=(N−1)(N−4)/4;
pro N≥5 je kladné. Navíc rozdíl mezi střední hodnotou
A/2 a prahem N−1 je Θ(N²), zatímco var B=Θ(N³).
Čebyšev dává P(Δ≤0)=O(1/N). To vysvětluje kvalifikaci
„almost always“ v obvyklém asymptotickém náhodném modelu,
bez nesprávného tvrzení o všech malých N.

## P0656: Algorithm D, všechny invarianty a hranice

Pišme F_k=#{j:K_j=k} a L_k=∑_(t<k)F_t.
D1 nuluje tabulku. Po zpracování libovolného prefixu
záznamů v D2/D3 platí COUNT[k]=počet již viděných k.
Po dokončení je to F_k. D4 indukcí přes rostoucí k
vytvoří COUNT[k]=L_k+F_k; nepřečtené vyšší položky
stále obsahují F. Zejména COUNT[v]=N.

Během výstupu platí

    COUNT[k]=L_k+počet dosud nevydaných záznamů klíče k.

Je-li takový záznam právě zpracován, tento počet je≥1;
cíl COUNT[k] je v disjunktním intervalu(L_k,L_k+F_k]
a ještě není obsazen. D6 tam uloží celý záznam a ubere1.
Indukce dokazuje unikátní použití každého cíle, zachování
satelitů a konečné setřídění. Chybějící hodnoty F_k=0
nedostanou žádný výstup. Pro u=v je akumulace prázdná
a metoda stále správně naplní všech N pozic. Pro N=0
jsou v abstraktní verzi obě záznamové smyčky prázdné.

Pro M=v−u≥0 se provede M+1 nulování, N inkrementů,
M akumulací a N výstupů: Θ(N+M+1) operací. Pomocná
tabulka má M+1 čísel a výstup N záznamů. Pro pevný
rozsah1,…,100 je čas lineární v N. Třídění podle
vedoucích číslic vytvoří správně uspořádané skupiny
stejných prefixů; úplné lexikografické pořadí se získá
dotříděním uvnitř každé skupiny. Není zde odvozena
univerzální cena takového dotřídění.

Fig9 má stejné dvě záznamové smyčky a akumulaci.
Jeho první smyčka je nakreslena sestupně (výstup j=0),
zatímco text D2 dovoluje vzestupnou. Součet frekvencí
je komutativní, takže jde o správnou variantu, stejně
jako v MIX odpovědi9; druhá smyčka je skutečně sestupná.

## P0657: úlohy7–8, stabilita a obrácení smyčky

Pro stejný klíč a původní indexy a<b se R_b vydává
dříve než R_a a obsadí větší z dosud volných cílů
dané skupiny. Ve výstupu tedy R_a stále předchází R_b:
D je stabilní. Při vzestupném j je obsazování cílů
stále sestupné, takže všechny skupiny zůstávají správně
umístěné, ale uvnitř se jejich původní pořadí obrátí.
To dokazuje současně správnost třídění a nestabilitu
upravené varianty, ne pouze příklad pro dvě položky.

## P0658: úloha6, všechny mezistavy tištěné simulace

Pro16 vytištěných záznamů jsou frekvence klíčů0,…,9

    F=(2,2,1,0,1,3,3,2,1,1),
    kumulativně (2,4,5,5,6,9,12,14,15,16).

Po nulovém D1 jsou proto oba následující řádky odpovědi
přesné. Výstupní kroky, vždy se snížením příslušného
COUNT o1, mají následující cíle:

| j | záznam | cíl |
|---|---|---:|
|16|7N|14|
|15|7O|13|
|14|6I|12|
|13|6T|11|
|12|5L|9|
|11|1G|4|
|10|4A|6|
|9|6A|10|
|8|2R|5|
|7|8S|15|
|6|1N|3|
|5|9.|16|
|4|0O|2|
|3|5U|8|
|2|0C|1|
|1|5T|7|

Těsně před j=8 jsou COUNT=(2,3,5,5,5,8,9,12,15,16)
a obsazeny právě pozice4,6,9,10,11,12,13,14, jak
ukazuje odpověď. Konečný výstup je

    0C 0O 1N 1G 2R 4A 5T 5U 5L 6A 6T 6I 7O 7N 8S 9.

Všechny stejné klíče zachovávají pořadí; satelity
dávají CONGRATULATIONS. Kontrola byla ruční.

## P0659: úloha9, celý MIX program a převzatá chyba M=0

Pro N≥1 a M≥1 lze každou fázi přímo spárovat s P0656.
ENN3 M nastaví−M; v D1 tedy COUNT+v+rI3 postupně
navštíví COUNT+u,…,COUNT+v. Inkrement a J3NP provedou
M+1 iterací. D2/D3 jde j=N,…,1, načítá klíč v poli0:2
a inkrementuje jeho četnost; směr této fáze nevadí.

Před D4 nastaví ENN3 M−1 offset1−M, tedy první adresu
u+1. A obsahuje COUNT[u]. Každé ADD/STA přidá další
četnost k součtu a uloží součet, takže poslední je v.
Pro M≥1 je iterací přesně M. D5/D6 jde j=N,…,1,
načte klíč, jeho COUNT do I1, celý záznam do A a
uloží jej do OUTPUT+I1; potom sníží a vrátí COUNT.
Satelitní byty3:5 se přenesou beze změny, znaménko
klíče se načítá s polem0:2.

Časy fází jsou

    D1: 1+4(M+1),
    D2/D3: 1+9N,
    D4: 3+6M,
    D5/D6: 1+13N,

tedy přesně(10M+22N+10)u v uvedeném platném rozsahu.
U M=0 není smyčka D4 prázdná: její první přístup
směřuje na COUNT[v+1]. Konkrétní validní protipříklad,
originál i pět vrstev už obsahuje
`notes/V3-C0009-counting-single-key.md`; přebírá
se hotový důkaz tohoto nálezu, žádný nový běh.
Opravený program M=0 fázi D4 přeskočí; abstraktní D
z P0656 je správný i bez této opravy implementace.

## Přesné výjimky a další kurzor

Historická prvenství Friend1956, Seward1954, Feurzeig1960,
datum autorova výběru čísel a Kiplingova citace nebyly
nově externě ověřeny. Nejsou matematickými závislostmi.
Neurčitý časový poměr na74 je samostatné partial P0646,
nikoli bibliografická výjimka. Tento blok sám úlohy10–13
neuzavírá pouhým odkazem v úvodu; pozdější doplnění10–12
mají vlastní uvedené důkazy. Úloha13 je následně úplně doložena
v `notes/internal-proof-13-distribution-shuffle.md`.
