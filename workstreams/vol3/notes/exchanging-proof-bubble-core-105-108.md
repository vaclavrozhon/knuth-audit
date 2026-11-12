# §5.2.2: výměny, celý Algorithm B a jeho přesné statistiky

2026-11-07. P0934–0945. Originály105–108,134,628 a dopředný
Algorithm S na139 zobrazeny; offset+11. Pět vrstev v
`sources/exchanging-errata-review.json`: poznámka BOUND=1 z1976
už je v našem tisku; na628 pouze bibliografická oprava Cayleyho
citace. Nový nález ani matematický program nevznikl. Níže se
nepředpokládá, že seznam tvrzení nebo samotný obrázek dokazuje
obecný algoritmus. Úlohy4,7,8 a momentová/asymptotická část109
mají samostatný následující blok; zde se neprohlašují za uzavřené.

## P0934: úvod105–106 a celá úloha1

Pro permutaci nechť na pozicích i<j leží x>y. Při jejich výměně
zanikne inverse(x,y). Pro každý vnitřní z=a_k, i<k<j, se mění
součet dvou indikátorů [x>z]+[z>y] na [y>z]+[z>x]. Je-li y<z<x,
klesne o2; pro z<y nebo z>x zůstává1. Pro k<i nebo k>j se jen
permutují dva sčítance se stejným z, jejich součet zůstává.
Ostatní páry se nemění. Celkový pokles je tedy přesně2m+1,
kde m=#{k:i<k<j, y<a_k<x}; m může být0.

Každá skutečná výměna nesprávně uspořádané dvojice snižuje
nezáporný celočíselný potenciál. Jestliže procedura vybírá další
takovou dvojici, dokud existuje, skončí a výstup nemá inversi,
tedy je vzestupně setříděný. Tvrzení neříká, že libovolné
předčasné zastavení zaručuje setřídění. Pro různé klíče je to
celá odpověď1; obecný rovnostní případ už pokrývá P0644.

Přímé vkládání přesouvá novou položku doleva právě přes větší
sousedy. Posuny implementace jsou stejná výsledná permutace
jako tyto sousední výměny, s případným uchováním nové položky
v registru. Proto příslušnost k insertion i exchange není
disjunktní klasifikace. Názvy čtyř dalších rodin jsou rozcestník,
nikoli dosud dokázaná správnost Batcherova či Hoareova algoritmu.

## P0935–0936: všechna2(a),(b), cykly a dopředný S

V cyklovém zápisu chápejme permutaci jako šipky u→a_u. Výměna
hodnot na různých místech u,v prohodí právě jejich dvě odchozí
šipky. Leží-li u,v v jednom cyklu

    (u, A, v, B),

vzniknou dva cykly(u,B) a(v,A); prázdné A/B dávají regulérní
jednoprvkové cykly. Leží-li naopak v cyklech(u,A),(v,B), vznikne
jediný(u,B,v,A). Počet cyklů se tedy změní právě o±1. Identita
má n cyklů, takže z c cyklů je nutno nejméně n−c výměn.
Rozštěpování každého délkyℓ na singletony spotřebujeℓ−1 výměn,
celkem n−c; dolní mez je dosažitelná. Pro n=0/1 je výsledek0.

Konkrétní permutace úlohy je3,7,6,9,8,1,4,5,2, s cykly

    (1 3 6), (2 7 4 9), (5 8).

Má c=3, proto minimum9−3=6. Například výměny **pozic**
(1,6),(3,6),(2,9),(7,9),(4,9),(5,8) dávají identitu: první dvě
opraví cyklus1→3→6, další tři2→7→4→9, poslední5↔8.

Dopředné tvrzení o5.2.3S lze dokázat už z jeho skutečného znění
na139. Při kroku j jsou hodnoty>j na správných místech a maximum
zbývajícího prefixu je j. Je-li na pozici i≠j, šipka i→j zaručuje,
že i,j jsou ve stejném cyklu. Výměna i,j oddělí singleton j
a zvýší c o1. Je-li i=j, stav se nemění. Proto počet **netriviálních
výměn** je přesně n−c; vykonání S3 je n−1, protože zahrnuje
i samovýměny. Těch je(n−1)−(n−c)=c−1, v souladu s dopřednou
úlohou5.2.3-4. Tato výslovná konvence je potřebná; tvrzení628
se nevydává za rovnost počtu všech vykonaných instrukcí S3.
Celý další nákladový blok S tímto lokálním argumentem uzavřen není.
Cayleyho článek a historická priorita byly bibliograficky přeskočeny.

## P0937–0938: celý B1–B4, obrázek15, ukončení a stabilita3

Pro algoritmus a program předpokládejme N≥1. Na začátku průchodu
je suffix za BOUND již neklesající a každá jeho položka má klíč
alespoň tak velký jako každý klíč aktivního prefixu. Před
porovnáním na j je na j maximum původních prvních j klíčů
tohoto průchodu; v dřívějších pozicích jsou zbývající položky
tohoto prefixu, na pozicích>j dosud nedotčené položky. Porovnání
j,j+1 umístí maximum jejich sjednocení na j+1. To induktivně
dokazuje základní přenos maxima i to, že na konci je pravý
kraj aktivního úseku správný.

Je-li poslední výměna na j=t, na t+1 právě skončilo maximum
dosavadního prefixu. Každé další porovnání bylo bez výměny;
od t+1 po starý BOUND jsou tedy klíče neklesající a všechny
≥každému klíči pozic≤t. Připojení již hotového suffixu zachová
tuto vlastnost. Nová hranice t je tudíž platná. Při t=0 jsou
všechny zbývající sousední dvojice uspořádané a algoritmus končí
správným pořadím. Při t>0 platí t≤starý BOUND−1, takže hranice
ostře klesá. Po nejvýše N−1 průchodech s výměnou následuje
poslední bez výměny; může mít BOUND=1 a prázdnou smyčku.

Tento důkaz přesně odpovídá všem hranám obrázku15: B1→B2,
1≤j<BOUND vede do B3 a zpět do smyčky, j=BOUND do B4,
kladné t zpět do B2 a nulové t ven. Paměť navíc je konstantní,
records se jen vyměňují; multiset je invariantní.

Výměna nastává pouze pro ostré Kj>Kj+1. Dva stejně klíčované
záznamy se v posloupnosti sousedních transpozic mohou předběhnout
jen při přímé vzájemné výměně, která nikdy nenastane. Algoritmus
je tedy stabilní i při duplicitách. Jedna sousední výměna sníží
počet ostrých inversí právě o1, takže počet výměn je původní
počet těchto inversí i v tomto obecnějším případě.

## P0939: všech16 MIX instrukcí, modifikace a četnosti

Předpoklady stejné jako v předchozích MIX programech: jeden
záznam/klíč na adresu, porovnávaný obsah reprezentuje jeho pořadí,
INPUT+1,…,INPUT+N i indexy jsou adresovatelné. Po01 je rI1=N.
02 ukládá **jen adresní bajty1:2** instrukce14, nikoli její
znaménko. Původní záporné znaménko ENTX proto zůstává a jeho
efektivní adresa je j−BOUND. 03 nastaví j=1,04 t=0 a05 skočí
na test dříve, než by načetl jakoukoli dvojici. 14–15 pustí
do06 právě j<BOUND. Po dosažení j=BOUND se jde do16, nikoli
za aktivní úsek. To je také přesná ochrana BOUND=1.

06–08 načtou levý záznam a pro ≤ přeskočí výměnu do13.
Při > uloží09 pravý do rX,10 jej přesune vlevo,11 přesune
původní levý z rA vpravo a12 nastaví t=j. 13 zvyšuje j.
Přepsání rX při14 nevadí, protože jeho dočasně uložený record
už byl zapsán. 16 při t>0 jde do02, které znovu uloží hranici;
při t=0 končí. To přesně realizuje B, včetně samomodifikace.

Pro A průchodů, B výměn a C porovnání jsou četnosti:

| Řádky | Četnost | Cena jedné skupiny |
|---|---:|---:|
|01|1|1|
|02–05|A|2+1+1+1=5|
|06–08|C|2+2+1=5|
|09–12|B|2+2+2+1=7|
|13|C|1|
|14–15|A+C|2|
|16|A|1|

Každý průchod má jeden počáteční test14–15 a jeden po každém
porovnání. Součet je přesně **8A+7B+8C+1** jednotek u.
Pro N=1: A=1,B=C=0, cena9u, žádné čtení INPUT+2.
Nejde o tvrzení stejného minimového vzorce pro prázdný vstup N=0.

## P0940: celý obrázek14 a všechny jeho hranice

Počáteční řada je503,087,512,061,908,170,897,275,653,426,154,
509,612,677,765,703. Ruční přenos maxima podle invariantu dává
následující **úplné** řady po každém průchodu; ve zdroji jsou
kresleny zdola nahoru.

```text
1: 087 503 061 512 170 897 275 653 426 154 509 612 677 765 703 908
2: 087 061 503 170 512 275 653 426 154 509 612 677 765 703 897 908
3: 061 087 170 503 275 512 426 154 509 612 653 677 703 765 897 908
4: 061 087 170 275 503 426 154 509 512 612 653 677 703 765 897 908
5: 061 087 170 275 426 154 503 509 512 612 653 677 703 765 897 908
6: 061 087 170 275 154 426 503 509 512 612 653 677 703 765 897 908
7: 061 087 170 154 275 426 503 509 512 612 653 677 703 765 897 908
8: 061 087 154 170 275 426 503 509 512 612 653 677 703 765 897 908
9: 061 087 154 170 275 426 503 509 512 612 653 677 703 765 897 908
```

Výměny byly postupně na j={1,3,5,…,15}; {2,4,6,…,14};
{1,3,5,7,8,9,10,13}; {4,6,7,8}; {5,6}; {5}; {4}; {3}; ∅.
Tím jsou zkontrolovány všechny křivky, nikoli jen koncové řady.
Počty výměn13,11,8,4,2,1,1,1,0 dávají41. Hranice po průchodech
s výměnou jsou15,14,13,8,6,5,4,3; po čtvrtém přibylo přesně
pět definitivních pozic9,…,13. Počty porovnání15,14,13,12,7,5,4,3,2
odpovídají všem nakresleným porovnáním a dávají75. Devátý průchod
neprovede výměnu; všechny horizontální čáry tím mají doložený význam.

## P0941–0942: větaI, všechny řádky(1) a vztahy(2)–(4)

Zde jsou klíče různé a nahrazené hodnostmi1,…,n. Pro **hodnotu** i
je b_i počet větších hodnot vlevo od ní. Sledujme její původní
pozici p v jediném průchodu. Až do porovnání p−1 se jí průchod
nedotkl. Je-li b_i>0, přinesené prefixové maximum je>i, takže
i se vymění právě o jedno místo doleva. V tomto průchodu už
znovu porovnávána nebude; ztratila právě jednu větší hodnotu
vlevo. Je-li b_i=0, stane se prefixovým maximem, případně jde
doprava přes menší hodnoty, ale nikdy nepřejde přes větší.
Její počet větších předchůdců zůstává0. To dokazuje celý lokální
přechod b'_i=max(b_i−1,0).

Úsek za platnou BOUND je hotový a větší než prefix. Doprovedení
plného průchodu až do n by v něm už nic nevyměnilo. Proto
důkaz pro plný průchod platí i pro zkrácenou implementaci B.
Indukcí po r průchodech je b_i^(r)=max(b_i−r,0). Je-li m=max_i b_i,
právě prvních m průchodů má nějakou výměnu a následuje jeden
bez ní. Tedy A=m+1 včetně m=0; součet všech úbytků dává B=Σb_i.
Počet porovnání každého uskutečněného průchodu je BOUND−1,
takže C=Σ_(j=1)^A c_j. Už hotové obecné distribuční důkazy pro
inversion table se tím nepočítají znovu.

Pro příklad má hodnostní permutace tvar
7,2,9,1,16,4,15,5,11,6,3,8,10,12,14,13. Počty větších
předchůdců po jednotlivých hodnotách1,…,16 jsou

```text
3 1 8 3 4 5 0 4 0 3 2 2 3 2 1 0
2 0 7 2 3 4 0 3 0 2 1 1 2 1 0 0
1 0 6 1 2 3 0 2 0 1 0 0 1 0 0 0
0 0 5 0 1 2 0 1 0 0 0 0 0 0 0 0
```

První řádek je přímo spočten z uvedených pozic; další jsou
právě dokázaný přechod a souhlasí se všemi řádky(1).
Může se tedy převzít A=9,B=41,C=75 z plného obrázku a cena
8·9+7·41+8·75+1=960u. Je to konkrétní kontrola přesného programu,
nikoli odhad asymptotické složitosti.

## P0943: úplná úloha5 a rovnice(5), včetně r=0

Nejprve pomocný fakt pro libovolnou aktuální permutaci s alespoň
jednou inversí. Označme c_i její inversion table a p_i pozici
hodnoty i. Výměna nastane při prvním navštívení původní pravé
položky i právě když c_i>0, a to na indexu p_i−1. Poslední
výměna je proto t=p_*−1, kde p_*=max{p_i:c_i>0}.

Za p_* nemůže být menší hodnota než jakákoli hodnota i s c_i>0:
pak by sama měla většího předchůdce i a byla pozdější takovou
pozicí. Všech i hodnot≤i tedy leží v prefixu p_*, stejně jako
c_i větších předchůdců hodnoty i. Tyto množiny jsou disjunktní,
takže i+c_i≤p_*. Pro hodnotu v na p_* žádná menší hodnota
vpravo není, tudíž p_*=v+c_v. Proto přesně

    t=max{i+c_i:c_i>0}−1.

Před r-tým průchodem, 1≤r≤m, dosadíme
c_i=(b_i−r+1)[b_i≥r] a dostaneme

    BOUND po r průchodech=max{b_i+i:b_i≥r}−r.

Při r=0 je b_i≤n−i, tedy maximum b_i+i≤n, a i=n dává rovnost.
To je počáteční BOUND=n i pro již seřazený vstup m=0.
Použitím r=j−1 dostaneme celé(5)

    c_j=max{b_i+i:b_i≥j−1}−j, 1≤j≤A.

Maximum se bere vždy z neprázdné množiny v uvedeném rozsahu.
Pro j>A lze definovat c_j=0, ale nelze bez tohoto dovětku
vyhodnocovat maximum prázdné množiny. Tento okraj bude použit
v distribučním argumentu pro C.

## P0944: úloha6, oba argumenty odpovědi

Nechť p_i=a'_i a d_i je počet menších hodnot vpravo od i.
Pak vlevo je i−1−d_i menších a b_i větších, takže
p_i−i=b_i−d_i. Ihned max(p_i−i)≤max b_i=m. Zvolme b_v=m.
Kdyby menší k leželo vpravo od v, mělo by všech m větších
předchůdců v a navíc samotné v, takže b_k≥m+1. To je spor,
tedy d_v=0 a p_v−v=m. S větouI plyne přesné A=1+max(p_i−i).

I fyzický argument odpovědi lze dokončit bez domněnky o přesunech.
Položka s nějakým větším předchůdcem jde za průchod přesně o1
doleva. Položka bez většího předchůdce se může nést doprava,
ale na každé pozici q, které dosáhne jako prefixové maximum i,
platí q≤i: prvních q prvků jsou všechny≤i. Její pravé posunutí
se tedy nestane kladným. Každá položka s kladným p_i−i nutně
většího předchůdce má. Maximum pravého posunutí proto při každém
nesetříděném průchodu klesne přesně o1; původní maximalizátor
dává dolní rovnost a ostatní nemohou vytvořit větší hodnotu.
Maximum0 znamená p_i=i pro všechna i, neboť Σ(p_i−i)=0.
Po vyrovnání zbývá poslední bezvýměnný průchod, jak žádá(2).

## P0945: celé rozdělení A a všechny meze v(6)

Rovnoměrná náhodná permutace odpovídá rovnoměrné inversion table
s nezávislými souřadnicemi b_i∈{0,…,n−i}; bijekce i nezávislost
jsou již doložené v úvodu. Událost A≤k, 1≤k≤n, je současně
b_i≤k−1 pro všechna i. Počet takových tabulek je

    ∏_(i=1)^n min(k,n−i+1)=k^(n−k) k!.

Označme F_k tuto hodnotu/n!, F_0=0 pro n≥1. Rozdíl
F_k−F_(k−1) je pravděpodobnost přesně k průchodů a dává(6),
včetně k=1, kde druhý člen0^n·0!=0, a k=n, kde F_n=1.
Všechny pravděpodobnosti jsou nezáporné a teleskopují do1.
To uzavírá konec108; momenty a použití P(n) se dokládají zvlášť.
