# Tableaux45: celý dodatek2020 a obousměrná konstrukce

Jde o přidanou úlohu, nikoli o text prvního dotisku. Zadání je
v all3-pre.pdf, file4, odpověď ve file11; oba originály zobrazeny.
Logická vazba je72/file83 a odpověď615/file626. Oprava2022
pouze doplňuje bibliografické stránky211–234. Pět vrstev,
primární bibliografie a obrázky jsou v
`sources/tableaux-permutation-tableaux-sources.json`.

Podmínka(ii) zakazuje nulu, která má nějakou1 nad sebou
ve stejném sloupci a nějakou1 nalevo ve stejném řádku.
Neznamená zákaz všech nul jihovýchodně od jediné diagonální1.
Tuto konvenci potvrzuje i zobrazený příklad.

## P0631: přesný model cest a vypuštění vnějších dlaždic

Pišme λ_i=n_i, w=λ_1, n=m+w a c_j počet řádků délky≥j.
Z pořadí kroků hranice přímo plyne

    r_j=j+m−c_j,       u_i=λ_i+m+1−i.

Hodnoty r_j rostou se sloupcem, u_i klesají s řádkem.
Dohromady rozdělují1,…,n podle pravých a horních kroků.

Orientujme všechny cesty na východ a na jih. Nulová dlaždice
spojuje sever s jihem a západ s východem; jedničková sever
s východem a západ s jihem. Křížení nuly není větvení cest.
Každý vstup má jediného následníka, každý výstup jediného
předchůdce a součet souřadnic roste. Proto existuje přesně
n různých vláken mezi n vstupy a n výstupy, tedy permutace.

V doplňku Youngova tvaru jsou jen1. Pro severní vstup do
buňky(i,j) označme hodnotu m−i+j+1, pro západní m−i+j.
Oba přechody jedničkové dlaždice tuto hodnotu zachovají:
N(i,j)→W(i,j+1) a W(i,j)→N(i+1,j). Na dolním okraji
je hodnota j, na pravém n+1−i, přesně vytištěné výstupy.
Po opuštění tvaru se cesta do něj nemůže vrátit, protože
doplněk je uzavřený směrem na jih a na východ.

Stačí proto cesty sledovat uvnitř T. Vodorovný výstup
z řádku i má konečnou hodnotu u_i, svislý výstup
ze sloupce j hodnotu r_j. To platí i pro výstup přímo
na dolní/pravé hraně obdélníku a pro nulovou délku řádku.

## P0632: všech devět cest tištěného příkladu

Ze sazby, nikoli z chybného řádkování OCR, je

    T = 0 0 1 0 1
        1 0 1 0 1
        0 0 0 0
        0 1 1 1.

Tvar je(5,5,4,4). Horní štítky jsou1,2,3,4,7;
levé shora9,8,6,5. V následující tabulce jsou vypsány
jedničky, ve kterých se cesta otočí; mezilehlé nuly
ji vedou přímo. N/W označuje směr vstupu do buňky.

| vstup | otáčky v T | výstup na hranici T | p_k |
|---|---|---|---|
|1|N(2,1), W(2,3), N(4,3), W(4,4)|dolů ze sloupce4|4|
|2|N(4,2), W(4,3)|dolů ze sloupce3|3|
|3|N(1,3), W(1,5), N(2,5)|vpravo z řádku2|8|
|4|N(4,4)|vpravo z řádku4|5|
|5|W(4,2)|dolů ze sloupce2|2|
|6|žádná|vpravo z řádku3|6|
|7|N(1,5)|vpravo z řádku1|9|
|8|W(2,1)|dolů ze sloupce1|1|
|9|W(1,3), N(2,3), W(2,5)|dolů ze sloupce5|7|

Výsledek je438526917. Každý sloupec má1. Jediné nuly
s1 nad sebou jsou v řádku3 a(4,1); všechny jsou bez1
nalevo. Ostatní nuly nemají1 nad sebou. T je tedy přípustné.

## P0633: nelze odstranit žádnou1 v řádcích2–4

Jde o šest buněk. (2,1),(4,2),(4,4) jsou jedinými1
svých sloupců, takže změna na0 poruší(i). U(2,3)
by zůstaly1 v(1,3) a(2,1), u(2,5) v(1,5) a(2,1),
u(4,3) v(2,3) a(4,2). Každá z těchto tří změn
proto poruší(ii). V řádku3 žádná1 není.

## P0634: část(a), pevné body a oba směry nerovností

Cesta z horního vstupu r_j nejprve klesá sloupcem j.
Podle(i) potká1 ještě uvnitř T a poprvé se otočí doprava.
Pokud později vyjde dolů, musí to být ve sloupci k>j:
další otočka z východu na jih nastává až v dalším sloupci.
Výstup r_k je tedy>r_j. Pokud vyjde vpravo v řádku h,
musí λ_h≥j, tedy h≤c_j, a

    u_h=λ_h+m+1−h ≥ j+m+1−c_j=r_j+1.

Horní vstupy jsou proto přesně kandidáti na excedance
a všechny skutečně jsou excedance.

Cesta z levého vstupu u_i je přímá, pokud je celý řádek0;
pak vyjde na hranici právě se štítkem u_i. Má-li řádek1,
první taková1 cestu otočí dolů. Vodorovný výstup pak leží
v řádku h>i, takže u_h<u_i. Svislý výstup leží ve sloupci
k≤λ_i, protože všechny navštívené nižší řádky jsou nejvýš
tak dlouhé jako řádek i. Hranice má krok r_k před u_i,
tedy opět r_k<u_i. Dostáváme přesnou charakterizaci:

    p_(r_j)>r_j;
    p_(u_i)=u_i právě pro nulový řádek i;
    jinak p_(u_i)<u_i.

Tento důkaz nepotřebuje(ii); tu skutečně využijeme až
pro vynucený tvar posledního sloupce při inverzi.

## P0635: co přesně dělá „poslední“ nula v odpovědi(a)

Zvolíme poslední nulu v řádkovém pořadí, takže napravo
ve stejném řádku a ve všech nižších řádcích obdélníku
jsou1. Změna této nuly na1 nevyvolá nový zakázaný vzor:
žádná nula napravo ani pod ní už není. Dvě dotčené cesty
původně končí na sousedních hodnotách

    v=m−i+j,    v+1.

Změna prohodí jejich konce; severní vstup do buňky
získá+1, západní−1. Neznamená to, že se mění jen
jediná položka permutace.

Není-li nad nulou1, severní cesta začala na r_j.
Ve sloupci musí být1 níže, takže c_j≥i+1 a r_j≤v−1;
zvětšuje se tedy hodnota excedance. Je-li nad nulou1,
podmínka(ii) vynucuje nulový prefix nalevo; západní cesta
pak začala na u_i≥v+1 a zmenšuje se hodnota nonexcedance.
To jsou právě dvě alternativy stručné odpovědi. Úplné
zachování typu obou dotčených cest dodává přímý důkaz
P0634, nikoli nevyřčený předpoklad o druhé cestě.
Pro základ se samými1 má horní cesta výstup m+j>r_j
a levá m+1−i≤u_i, ve shodě s týmž důkazem.

## P0636: část(b), žádná excedance

Pokud p_k≤k pro všechna k, rovnost součtů ∑p_k=∑k
vynucuje p_k=k pro každé k. Podle(a) nemá tvar žádný
sloupec: w=0, m=n, λ_1=…=λ_m=0. Obráceně každý
z těchto n prázdných řádků má přímou cestu ze štítku
n+1−i do stejného výstupu. Jde přesně o identitu.
Pro n=0 použijeme přirozený prázdný objekt, aniž bychom
vyhodnocovali neexistující λ_1; n=1 má jediný prázdný řádek.

## P0637: část(c), odstranění pevného bodu

Pevný bod k musí podle P0634 být vstup u_i nulového
řádku. Vymažeme tento řádek. Všechny svislé cesty jen
ztratí přímý segment; vodorovná cesta k→k zmizí.
Křížení nulových dlaždic nic nepřepojuje. Na hranici
tvaru zmizí jediný horní krok se štítkem k, takže zbylé
vstupy i výstupy se přeznačí x↦x−[x>k]. Hodnota k
se nikde jinde nevyskytuje, proto je to na zbylých
hodnotách přesně odpověď p′=p−[p≥k].

Žádná sloupcová1 se neodstraní. U zbývající nuly se
neobjeví nová1 nad ní ani nalevo, takže přípustnost zůstane.
To zahrnuje nulové řádky mezi stejně dlouhými řádky
i řádky nulové délky. Šířka nemůže tímto krokem klesnout:
nenulový sloupec měl1 v jiném než smazaném řádku.

## P0638: část(d), vynucený sloupec a přesný počet nul

Nyní nejsou pevné body, tedy každý řádek obsahuje1.
Největší excedance je k=r_w. Poslední sloupec má výšku
c=c_w, kde λ_1=…=λ_c=w a další řádky jsou kratší.
Jakmile se v něm objeví první1, nemůže níže být0:
ta by měla1 nad sebou a protože je poslední v nenulovém
řádku, měla by též1 nalevo, v rozporu s(ii).
Sloupec je tedy0^a1^(c−a), kde0≤a<c.

Cesta k jde dolů přes a nul a otočí se doprava
v řádku a+1, přímo na hranici. Proto

    p_k=u_(a+1)=n−a,    a=n−p_k.

To zároveň ověřuje krajní varianty a=0 a a=c−1.

## P0639: část(d), permutace po odstranění sloupce

Odstraňme sloupec w, tedy zmenšeme každé λ_i=w o1.
Ostatní sloupce stále mají1; zakázaná nula nemůže nově
vzniknout. Vstup k zmizí a ostatní vstupy se změní
x↦x−[x>k], protože z hraničního slova mizí krok k.

Zbývá zkontrolovat výstupy, ne je jen předpokládat.
Označme v=p_k=n−a. Cesta přicházející zleva do posledního
sloupce v řádku i≤c měla dříve výstup

    n+1−i,  jestliže i≤a;
    n−i,    jestliže a<i≤c.

První případ prochází nulou doprava. Ve druhém jde
jedničkou dolů a následující jedničkou doprava;
pro i=c vyjde dolů se štítkem r_w=n−c=k.
Nová hraniční hodnota téhož levého konce je vždy n−i.
V prvním případě původní hodnota>v a klesne o1;
ve druhém je<v a nezmění se. Ostatní výstupy jsou<k<v
a také se nezmění. Mizí právě výstup v.

Nová permutace je proto přesně vymazání pozice k
a přeznačení všech ostatních hodnot p↦p−[p≥p_k],
jak žádá zadání. Důkaz výstupního přeznačení ve skutečnosti
platí pro libovolný sloupec0^a1^(c−a); nepředpokládá
další vnitřní vlastnosti zbylých řádků.

## P0640: část(e), tvar a redukce libovolné permutace

Množina excedancí E určuje hraniční slovo: na pozicích E
jsou pravé kroky, jinde horní. Poslední krok je horní,
protože p_n≤n. Slovo tedy jednoznačně určuje tvar s
w=|E| sloupci a m=n−w řádky, včetně prázdných řádků.

Při odstranění pevného bodu k se ostatní excedance zachovají
po stejném přeznačení indexů. Jediný zdánlivě nebezpečný
přechod by vyžadoval p_i=k pro i≠k, což je nemožné.
Takto z hraničního slova mizí příslušný horní krok.

Nejsou-li pevné body, existuje excedance, protože jinak
je permutace identita. Vezměme největší k∈E a v=p_k>k.
Při vymazání této pozice a hodnoty zůstane typ každého
i<k zachován: zmenšení hodnoty nad v>k nemůže překročit i.
Pro i>k máme p_i<i, tedy p_i≤i−1, nový index je i−1
a nová hodnota se může jen zmenšit. Nevznikne tedy
žádná nová excedance. Nová množina E je přesně E\{k},
což je hraniční slovo bez posledního pravého kroku.
Obě algebraické redukce se shodují s úpravami tvaru(c),(d).

## P0641: část(e), zpětné vložení a oba směry inverze

Snižujme n předchozími kroky, až zbude prázdná permutace.
Záznam kroků čtěme pozpátku. Při vracení pevného bodu
vložíme příslušný nulový řádek. Nemůže porušit(ii),
protože v něm není1 nalevo od žádné nuly, a jiné buňky
nezískají novou1 nad sebou. Sloupce nemizí ani se
nezbaví1. P0637 dokazuje přesnou obnovu permutace.

Při vracení největší excedance k přidáme poslední sloupec
výšky c=n−k: za posledním pravým krokem je právě c
horních kroků. Vyplníme jej0^(n−v)1^(v−k).
Z k<v≤n plyne0≤n−v<c, takže má aspoň1.
Každá jeho nula je nad všemi novými1; jiné sloupce
nemají nové1 nad sebou ani nalevo. Opět je tedy
přípustný. P0639 dokazuje přesně požadovanou obnovu
všech vstupních a výstupních štítků.

Tím existuje T pro každou permutaci, bez odvolání na
součet počtů tableaux. Je dokonce jediné: u každého
existujícího T určují(c),(d) přesně odstraněný řádek
nebo všechna políčka odstraněného sloupce; indukce
na n pak vynucuje celou rekonstrukci. Volba mezi více
pevnými body nemění konečný výsledek. Každý krok
zmenší n o1; prázdné řádky, šířka1 i konečná šířka0
jsou zahrnuty. Neprovádí se enumerace tableaux.

## P0642: část(f), přesná cyklová bijekce z nápovědy

Originál svazku1,179/file194,§1.3.3–(20), byl zobrazen:
v každém cyklu je minimum první, cykly jsou seřazeny
podle klesajících minim a singletony zůstávají.
Vymažme závorky a označme vzniklé slovo q_1…q_n.
Inverze vloží začátek cyklu před každé minimum zleva.
Uvnitř bloku je jeho první hodnota nejmenší, takže
další minimum zleva nevznikne; první hodnoty bloků
jsou klesající. Tím je skutečně dána bijekce všech n! slov.

Uvnitř cyklu máme p_(q_i)=q_(i+1). Každý vzestup
q_i<q_(i+1) je tedy excedance. Přes hranici cyklů
vzestup být nemůže: nové minimum je menší než každý
prvek předchozího cyklu. Závěrečná hrana každého
cyklu vede zpět do jeho minima, takže není excedance;
singleton je pevný bod. Obráceně každá excedance
musí být vnitřní hranou cyklu, tedy vzestupem q.
Jde o přesnou obousměrnou rovnost statistik.

## P0643: část(f), Eulerova konvence a mezní hodnoty

Počet slov s r vzestupy je Eulerovo číslo ⟨n;r⟩.
Pokud se definuje pomocí sestupů, komplement hodnot
q_i↦n+1−q_i vzestupy a sestupy prohodí, takže počet
zůstává stejný. Pro samostatnou kontrolu indexace vložme
největší hodnotu n do slova délky n−1. Slovo s r vzestupy
má r+1 míst, kde počet zůstane r: mezi dvěma hodnotami
každého vzestupu a před prvním prvkem. Slovo s r−1
vzestupy má n−r míst, kde počet vzroste na r: mezi dvěma
hodnotami sestupu nebo za posledním
prvkem. Tedy

    ⟨n;r⟩=(r+1)⟨n−1;r⟩+(n−r)⟨n−1;r−1⟩.

Základ je ⟨0;0⟩=1 a hodnoty mimo0≤r<n jsou pro n>0
nulové. Pro r=0 dostaneme jedinou identitu p podle(b),
pro r=n−1 jedinou permutaci(2,3,…,n,1). To kontroluje,
že nejde o posunutý počet slabých excedancí.

Všechny části(a)–(f), pomocné kroky odpovědi i celý
příklad jsou tím doloženy. Vnější články slouží jen
k ověření bibliografické poznámky; žádný hluboký
externí výsledek tento důkaz nepotřebuje. Celé články
a další výsledky v nich nebyly znovu auditovány.
Nevznikl nový nález a nebyl spuštěn matematický program.
