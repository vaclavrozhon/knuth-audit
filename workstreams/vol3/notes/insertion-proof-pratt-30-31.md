# Prattovy přírůstky a úplný algoritmický blok30–31

7. listopadu 2026. Originály91/file102,104/file115 a
623–624/file634–635 zobrazeny. Převzaty konkrétní důkazy K,
matchingové25 a instrukční součet C0022/P0811. Žádný program,
enumerace permutací ani opakovaný starý výpočet se nespouští.
Pět vrstev errat: `sources/pratt-eight-item-errata-review.json`
a širší `sources/insertion-errata-review.json`. Známé znaménko
ENN2 a úpravy četnosti/prosy jsou zahrnuté, nikoli nové nálezy.

## P0812: celá množina přírůstků a počet průchodů

Pro N≥2 vezmeme všechna h=2^p3^q<N, p,q≥0. Jednoznačnost
prvočíselného rozkladu zaručuje různé přírůstky pro různé páry.
Polož L=ln N, α=ln2, β=ln3. Příslušné mřížové body leží
v trojúhelníku αp+βq<L v prvním kvadrantu.

Sjednocení jednotkových čtverců zakotvených v těchto bodech
obsahuje celý trojúhelník: podlahy souřadnic každého jeho bodu
jsou také přípustné. Naopak celé sjednocení leží v trojúhelníku
αx+βy<L+α+β. Plochy dávají

    L²/(2αβ)≤T≤(L+α+β)²/(2αβ),
    T=½(log_2 N)(log_3 N)+O(log N).

Přísná hranice h<N nemění plochu ani odhad. Tím je doložen
celý koeficient a zbytek v odpovědi30, nikoli jen řád log²N.

## P0813: nejvýše N/2 přesunů za průchod

V sestupném pořadí před h již proběhly2h a3h, pokud jsou<N;
jinak je jejich uspořádání prázdnou podmínkou. K zachovalo oba
výsledky. Každá h-třída je tedy po přeznačení pozic2- a3-ordered.
P0780–0781 dokazují, že má pouze disjunktní sousední inverse.
Jejich počet je nejvýše⌊L_i/2⌋. Součet přes všechny třídy
je nejvýše N/2, a insertion sort provede právě tento počet
přesunů. Argument platí i pro jednobodové třídy a prázdné
předchozí uspořádání, bez skrytého předpokladu2h,3h<N.

## P0814: všechny nerovnosti a oprávnění přeskočit porovnání

Pokud K_(j−h)>K_j, platí u existujících indexů z předchozích
2h- a3h-uspořádání

    K_(j−3h),K_(j−2h)≤K_j<K_(j−h)≤K_(j+h),K_(j+2h).

V h-třídě jde právě o jednu hranu matchingových inversí.
Záměna ji odstraní a žádnou jinou inversi nezmění: dvojice
s libovolným třetím prvkem jsou uspořádané v obou pořadích
sousedního páru. Zbývající inverse jsou nadále disjunktní páry.
To je invariant i **během** průchodu, nejen po celém h-sortu.

Po záměně lze přeskočit srovnání s bezprostředním pravým
sousedem v této třídě a zvýšit j o2h. Na hranici třídy se
žádný neexistující klíč nečte. Zároveň odpadá hledání dalších
vkládacích posunů doleva. Tím jsou zdůvodněny všechny změny30,
včetně předpokladu používaného následným programem31.

## P0815: skutečný řád času v hlavním textu91

Z B_s≤N/2 a T=Θ(log²N) vychází B=O(Nlog²N).
ProgramD má přesně doložený čas9B+10NT−10S−3A+13T+1,
takže je O(Nlog²N). Naopak počet přírůstků<N/2 má stejný
vedoucí člen jako T. Každý takový průchod provede alespoň
N−h≥N/2 vkládacích iterací i na seřazeném vstupu.
To dává Ω(Nlog²N) a tedy celý řád Θ(Nlog²N).

Nezaměňujeme ho s tvrzením o praktickém crossoveru nebo se
zaručenou skutečnou rychlostí proti jiné implementaci; tyto
empirické formulace na91 jsou odděleny v P0823.

## P0816: každý adresový a řídicí krok MIX programu31

Předpoklady: N≥2,1≤H_1<…<H_T<N, všechny Prattovy přírůstky,
jednoslovné záznamy/klíče a platný rozsah MIX adres/indexů.
Řádek01 nastaví rI3=T;02 načte aktuální h do rI4. Na03
ENN2 -INPUT-N,4 vytvoří rI2=INPUT+N−h. Uložení polí0:2
na04–06 nastaví v řádcích12,14,10 adresy předchozího záznamu
INPUT+N−h; zachová index1 i opcode a porovnávací pole.
Následné ENT2 0,4 přepne rI2 na číslo třídy h.

Vnější smyčka zpracovává třídy q=h,h−1,…,1. Na19 je
rI1=q−N. Kladné q vede20 na16, kde se před prvním čtením
přičte h: první testovaný j je q+h, tedy druhý prvek třídy.
Pokud j>N,17 přeskočí celý jednobodový případ bez čtení.

Jinak09 načte K_j a10 porovná s K_(j−h). JGE na11 přeskočí
záměnu právě při správném pořadí. Řádky12–14 jinak načtou
levou hodnotu a zapíší vyměněný pár.15 přidá první h,16 druhé;
bez záměny proběhne jen16. J1NP na17 pokračuje právě při j≤N.
P0814 dokazuje, že přeskočená sousední hrana se nemusela testovat.

Po konci třídy18 sníží q.19–20 buď začnou další třídu,
nebo při q=0 přejdou na21 bez načtení prvku.21–22 sníží
číslo přírůstku a pokračují, dokud nezpracují H_1=1.
Všechny třídy jsou konečné, každý průchod je správný a poslední
jednotkový průchod celé pole seřadí. Samostatný nulový/jednoprvkový
vstup by potřeboval vstupní guard; do vymezeného MIX modelu nepatří.

## P0817: význam A, všechny četnosti a čas

V tomto programu A počítá inversní **poslední hrany** h-tříd.
Každá jiná záměna přeskočí jedno existující porovnání, poslední
záměna již žádné existující porovnání nevynechá. Proto je při
M=NT−S počet porovnání C=M−B+A. Řádky09–11 mají četnost C;
12–15 četnost B;16–17 četnost C+S=NT−B+A, protože na každou
z S tříd připadá ještě počáteční increment/test.
18 má S,19–20 mají S+T včetně konečného q=0; všechny ostatní
četnosti jsou1 nebo T přesně podle tabulky.

Úplný již uložený součet všech22 instrukcí v P0811/C0022 dává

    7NT+7A−2S+1+15T.

Tím je nezávislost vzorce na B skutečně dokázána; není to
tvrzení, že B je konstantní. Nález C0022 mění jen tištěný
číselný příklad276.24u, ne tento správný vzorec.

## P0818: přesný význam stejného statistického chování A

V 2/3-ordered třídě může být novým prefixovým minimem kromě
prvního prvku jen druhý, a to právě při inversi první hrany.
Obdobně pravolevé maximum kromě posledního prvku může být
jen předposlední při inversi poslední hrany. Definuj involuci
vstupních permutací

    (Rπ)_i=N+1−π_(N+1−i).

Obrátí pozice i pořadí hodnot. Permutuje h-třídy, v každé
obrátí a komplementuje její posloupnost; proto komutuje s každým
úplným h-sortem, včetně nestejně dlouhých tříd. První inversní
hrana se mění v poslední a počet inversí B se zachovává.
Přes všechny stejné průchody tedy A_end(π)=A_start(Rπ),
a současně B(π)=B(Rπ).

Na rovnoměrných odlišných vstupech tak mají obě A dokonce
stejné společné rozdělení s B. To je rigorózní význam věty
pod programem. Na témže jednotlivém vstupu se A rovnat nemusí;
žádná nezávislost tříd/průchodů se netvrdí.

## P0819: celý osmiprvkový maximální příklad jako svědek

Pro vstup7,3,8,4,5,1,6,2 a sestupné přírůstky jsou všechny
výstupy a lokální počty:

|h|výstup průchodu|B_h|A_h|
|---:|---|---:|---:|
|6|6,2,8,4,5,1,7,3|2|2|
|4|5,1,7,3,6,2,8,4|4|4|
|3|3,1,2,5,4,7,8,6|3|2|
|2|2,1,3,5,4,6,8,7|2|1|
|1|1,2,3,4,5,6,7,8|3|1|

Každá změna je záměna matchingového páru v příslušné třídě;
A_H započítává jen poslední hrany. Výsledkem je A=10,B=14.
Tabulka je ruční kontrola konkrétního svědka, nikoli sama důkaz
maximality obou veličin.

## P0820: obecný důkaz maxima A=10 pro N=8

První dva průchody mají A_6≤2,A_4≤4. Pro zbývající tři
piš A_3≤3,A_2≤2,A_1≤1. Pokud A_2=2, před2-sortem jsou
b_5>b_7 a b_6>b_8. Pole je3-ordered, tedy b_5≤b_8.
Po záměně obou posledních hran jsou na pozicích7,8 hodnoty
b_5,b_6 a platí b_5≤b_8<b_6. Proto A_1=0.
Vždy tedy A_2+A_1≤2.

Je-li A_3≤2, stačí to k A_3+A_2+A_1≤4. Zbývá A_3=3.
Před3-sortem označ hodnoty c_1,…,c_8. Všechny tři poslední
hrany jsou inversní a pole je4- i6-ordered. Dostáváme řetězec

    c_5>c_8>c_4>c_7>c_3>c_6>c_2.

Po3-sortu je pole
c_1,c_2,c_6,c_7,c_8,c_3,c_4,c_5. Při2-sortu je poslední
lichá hrana inversní(c_8>c_4), poslední sudá nikoli(c_3<c_5),
tedy A_2=1. Jeho koncové hodnoty jsou c_8,c_5 ve správném
pořadí, takže A_1=0. I zde je součet posledních tří A nejvýše4.
Celkem A≤2+4+4=10 a P0819 této meze dosahuje.

## P0821 — partial: průměry a maximum B pro N=8

Tištěné A_ave≈3.892 a B_ave≈6.762 dosud nemají vlastní
obecné koeficientové odvození. Tvrzení o maximu B=14 má
konkrétního svědka P0819, ale chybí horní mez pro všechny
vstupy. Čísla se neuzavírají pouhým přepisem z knihy ani
odvozením již dokázaného maxima A. Enumerace8! vstupů nebyla
spuštěna. Nález C0022 na těchto nezávislých otázkách nezávisí:
uvedený průměr času odporuje už univerzálnímu minimu324u.

## P0822: celý počet40 a numerická konzistence velkého příkladu

Pro N=1000 mají jednotlivé mocniny3 následující úplné rozsahy:

|q|p|počet|součet přírůstků|
|---:|---|---:|---:|
|0|0…9|10|1023|
|1|0…8|9|1533|
|2|0…6|7|1143|
|3|0…5|6|1701|
|4|0…3|4|1215|
|5|0…2|3|1701|
|6|0|1|729|

Rozsahy dokazují sousední mocniny2 na obou stranách hranice1000;
pro q=7 už3^q>1000. Počet je40 a součet S=9045. Největší
hodnoty972,864,768,729 a konec8,6,4,3,2,1 skutečně odpovídají
této množině. Je-li přijato pouze pro kontrolu aritmetiky empirické
A≈875, správný programový vzorec dává268636u. Je to stejný
hrubý řád jako tištěné „about268000u“; vzhledem k neurčené
přesnosti empirického údaje z toho nevytváříme další chybu.
Samotné hodnoty A,B tím nebyly statisticky ověřeny.

## P0823 — partial: empirická srovnání a praktický crossover

A≈875,B≈4250 a srovnání s přírůstky úlohy28 jsou uváděná
měření, jejichž vzorek není v tomto bloku reprodukován.
Také výroky91 o „astronomically large“ crossoveru a nejlepším
praktickém geometrickém poměru nemají vymezený strojový model
a univerzální práh. Asymptotický důkaz P0815 tyto výroky
nepotvrzuje; zůstávají výslovně partial/empirické, bez nálezu.

## P0824: všechny kroky generátoru P1–P5 a jeho platné pořadí

P1 nastaví m=2^(⌈lg N⌉−1), největší mocninu2 přísně menší
než N; je správně o jednu menší při N samotné mocnině2.
P5 projde m=2^r až po1 a pak skončí. Při pevném r dává
P2–P4 postupně

    h=2^(r−j)3^j,  j=0,…,r,

dokud h<N. Přechod h←h+h/2 je při sudém h přesně násobení3/2
a sníží exponent2 o1. Při lichém h je j=r a řádek končí.

Každé přípustné2^p3^q má r=p+q a2^r≤2^p3^q<N, takže
jeho řádek je zahrnut. Předchozí hodnoty v tomtéž řádku jsou
menší, takže předčasné překročení N jej nemůže vynechat.
Jednoznačnost exponentů vylučuje opakování. Generátor tedy
projde přesně celou požadovanou množinu bez pomocné tabulky.

Pořadí je podle klesajícího p+q a v řádku podle rostoucího q.
Obě potřebné hodnoty2h,3h mají stupeň p+q+1, takže pokud<N,
byly v celém dřívějším řádku již zpracované. P0813–0814 proto
platí i zde; poslední řádek obsahuje1 a výsledek je seřazený.
Nejde o tvrzení stejného konečného A/B jako v sestupném pořadí;
náklady generování také nejsou zahrnuty do tabulkového programu31.

Celé30 a algoritmické části31 jsou doloženy. P0821/P0823
zachovávají přesné zbývající mezery; celou624 ani tento blok
nelze označit bezvýhradně checked. Další souvislý kurzor je
konstrukce Incerpi/Sedgewick na konci91 a na92.
