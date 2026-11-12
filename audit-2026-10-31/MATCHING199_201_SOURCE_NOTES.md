# Úplný průchod 199–201: zdroje, důkazy a hranice

3. listopadu 2026. Kniha §7.2.2.1, zadání str.149, odpovědi str.470–471;
autorský Fascicle 5c, zadání str.85, odpovědi str.174–175. Obě verze
zobrazeny, rovnice porovnány. Předchozí přesné výčty zůstávají přijaté
a nespouštějí se znovu. Nový program pouze dekóduje 63 políček matice
z každé ze dvou verzí; žádný solver ani dlouhý výpočet.

Výsledek: 200 a 201 mají úplný obecný důkaz a dokončený zdrojový průchod.
C003 se potvrzuje při zachování ID. F002 se nemění. U 199 je profil
dokázán, ale celý záznam průchodu zůstává partial kvůli interpretaci
centrální asymptotiky C002; neposouváme ji mezi jednoznačné chyby.

## 199: nesplnitelnost, profil a dvě parity

Pracujeme s přirozenou doménou 1≤m≤n. Prvních m položek A se může
párovat pouze s m−1 položkami C, takže řešení neexistuje. Po záměně
A a C a obrácení obou pořadí přejde zakázaný obdélník na tentýž typ
pro m'=n+1−m. Proto lze předpokládat m≤ceil(n/2).

Po l<m vybraných možnostech z prvních m položek A má každá zbývající
taková položka (n−l)(m−1−l) možností. Položka C mimo prvních m−1 má
(n−l)(n−m) možností; ostatní typy nemají méně než kritické A.
MRV tedy vybírá kritické A. V centrálním lichém případě může v kořeni
nastat remíza A/C: přirozené pořadí A před C vybírá A; opačná volba
vede symetrií ke stejnému profilu. Po prvním kroku tato remíza mizí.

Pro l=0,…,m−1 je přesný počet uzlů

    N_l = n!/(n−l)! · (m−1)!/(m−1−l)!.

Poslední úroveň má L=n!(m−1)!/(n−m+1)! uzlů. Pro j≥0 je poměr
N_(m−1−j)/L nejvýše 1/[j!(n−m+2)^j]. Proto

    1 ≤ N/L ≤ exp(1/(n−m+2)),

kde N je celkový počet uzlů. To dává obecný odhad, nikoli extrapolaci
z dřívějších 55 vstupů n≤10.

- n=2q, m=q: L=(2q)!/[q(q+1)] ∼4(n−2)!.
- n=2q+1, m=q+1: L=(2q+1)!/(q+1) ∼2(n−1)!.

Slova m≈n/2 sama nerozlišují tyto dvě centrální posloupnosti. Knižní
Theta((n−2)!) odpovídá první, nikoli druhé. Protože aproximativní
formulace může implicitně mínit sudou posloupnost, **C002 zůstává
kandidátem**. Dřívější M199 označuje správně ověřený přesný profil,
nikoli bezvýhradné přijetí této asymptotické věty.

## 200(a): přesná determinantová identita

Rozvoj det Q(X) vybere pro každé A právě jednu položku B, tedy
permutaci p, a jeden index C mimo X. Pro pevnou n-tici indexů C je
součet znamének (−1)^|X| přes podmnožiny nevyužitých C nulový, pokud
některá položka C chybí. Jinak je jedna. Proto zůstanou právě volby,
které používají každé A,B,C jednou. Jsou to dokonalá 3D párování.

Různá párování používají různé množiny možností, tedy různé monomiály.
Koeficient každého je sign(p)=±1, bez možného vzájemného vyrušení.
Nepřítomné možnosti se nastaví na nulu. Nenulovost proto přetrvá i
po redukci modulo libovolné prvočíslo; nejde jen o formální nenulovost
nad celými čísly. S je multiafinní a má celkový stupeň n.

Zadání má sedm možností t,u,v,w,x,y,z. Všech sedm vytištěných 3×3
matic v každé verzi je nově dekódováno přímo ze zdrojových glyfů a
porovnáno s definicí Q(X); osmou maticí Q(C) je nula. Sady X nad
maticemi a úplný popisek jsou zkontrolovány vizuálně. Rozvoj
det Q(empty)=u(v+w)x−t(v+w)(y+z) odpovídá dvěma možným nenulovým
permutacím řádků/sloupců. Přijatý výsledek S=uvx−twy se neopakuje.

## 200(b): pravděpodobnost, C003 a složitost

Nenulový multiafinní polynom v M proměnných nad F_p je nenulový
alespoň v (p−1)^M bodech F_p^M. Indukce: napiš S=x_M A+B. Je-li
A nenulové, podle indukce je A nenulové alespoň v (p−1)^(M−1)
bodech; v každém takovém vlákně zbývá alespoň p−1 nenulových hodnot
S. Je-li A=0, použij B a všech p hodnot x_M. Konstantní báze je jasná.
Odtud pro pevný vstup s existujícím párováním

    Pr(s=0) ≤ 1−(1−1/p)^M ≤ M/p < 1/2,     p>2M.

Knižní první ostrá mez je dosažitelná: n=M=2, dvě diagonální možnosti,
S=xy, p=5 dávají 9/25=1−(4/5)^2. Tím je **C003 confirmed** bez ohledu
na další interpretační výhradu k obrácenému podmínění v textu. Pro
M=1 je navíc rovností i prostřední mez; pro M≥2 je prostřední ostrá.
Podrobnosti a krátký ruční důkaz má [C003](C003_PROBABILITY_BOUND_CONFIRMED.md).

Algoritmus se tím nemění. Nenulové vyhodnocení je bezchybný svědek
existence, zatímco r nulových vyhodnocení má na řešitelném vstupu
pravděpodobnost <2^(−r). Neřešitelný vstup je vždy správně odmítnut.

### Časová mez O(2^n n^4)

Pro n≥1 je M≤n^3. M<n dovoluje okamžité odmítnutí; jinak Bertrandova
věta dává prvočíslo 2M<p<4M. Má O(log n) bitů. Jeden pokus sestaví
nejvýše 2^n matic v O(2^n(M+n²)) operacích a vypočte jejich
determinanty eliminací s pivotováním v O(2^n n³) polních operacích.
Výběr r=n dává O(2^n n^4) v modelu jednotkové ceny malých slov
a chybu <2^(−n), tedy q.s.

Také bitovou složitost lze vměstnat do zadané meze: školní aritmetika
a eukleidovský algoritmus dávají konzervativní O(log³ n) bitových
operací na polní operaci včetně inverze. Zvolme místo r=n
r=ceil(log2(n+1)^2). Chyba 2^(−r) klesá rychleji než každá záporná
mocnina n. Cena je

    O(2^n n³ log^5 n) = O(2^n n^4).

Najít prvočíslo jednou i hrubým zkoušením dělitelů stojí jen polynom
v n, který tato exponenciální mez absorbuje. Rovnoměrný výběr z F_p
lze dělat odmítáním bitových slov délky ceil(log2 p), s úspěchem
větším než 1/2. Pokud požadujeme pevnou mez počtu bitových kroků,
omezíme každý výběr na n pokusů a při neúspěchu vrátíme „ne“.
Všech M r výběrů pak přidává nejvýše M r 2^(−n) k jednostranné chybě,
stále q.s., a pouze polynomiální čas. Případy omezeného n lze ošetřit
přímo. Dřívější poznámka „bitovou složitost neověřuji“ je tím uzavřená.

Nulový řádek či sloupec Q(X) zůstane nulový v Q(X') pro X'⊇X:
odstraňují se další možnosti. Praktické prořezání tedy platí.
Na nesplnitelných případech 199 je rozdíl mezi exponenciálním horním
odhadem a faktoriálním prohledáváním skutečný; nejde o nové měření času.

### Primární článek a odkaz do svazku 2

Björklund, *Exact Covers via Determinants*, STACS 27 (2010), 95–106:
[vydavatelská stránka](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2010.2447)
a uložené PDF. Zobrazeny PDF1,5,6,7 (tištěné95,99,100,101).
Lemma2.3 uvádí neostrou Schwartzovu–Zippelovu mez; Lemma2.4 a
Corollary2.5 používají eliminaci neúplných pokrytí součtem přes
podmnožiny, s náhodností při pevném vstupu. Definice3.1, Lemma3.2
a §3.1 poskytují determinantový mechanismus párování. Článek pracuje
v charakteristice2, knižní varianta s lichým prvočíslem používá znaménka.
Theorem1.1 má pro k=3 čas O*(2^(N/3)), kde N=3n je počet všech položek;
není to rozpor s knižním 2^n. Bibliografické údaje souhlasí. Celý článek
ani všechny jeho obecnější výsledky neprohlašujeme za zrevidované.

Odkaz 4.6.1–16 byl přímo zobrazen v našem prvním dotisku svazku2,
tištěné436,674,675, DjVu strany448,686,687. Uvádí neostrou mez
počtu kořenů v kartézském součinu, indukční důkaz a dosažitelnost
součinem lineárních faktorů. Je to přesný podklad pro opravu C003.
Nevzniká tím nové tvrzení o úplném auditu svazku2.

## 201(a,b): kruhové přesazování a zachovaná F002

Permutace dovoluje každému zůstat, posunout se vlevo nebo vpravo.
Její cyklus délky≥3 musí projít celou kružnici, protože vlastní
podmnožina hran kružnice žádný takový cyklus neobsahuje. Zbývající
cykly jsou pevné body a sousední transpozice. Pro n=3 jde také o dvě
orientace celého trojúhelníku. Jsou tedy dvě úplná cyklická posunutí
a párování hran kružnice C_n, kterých je

    F_(n+1)+F_(n−1)=L_n.

Například rozdělení podle použití hrany (n,1) dává dva path matching
počty. Celkový počet L_n+2 je správný. Pro sudé n existují dvě dokonalá
párování kružnice, která také nemají pevný bod. Proto pro sudé n≥4
jsou čtyři přesazení bez pevného bodu a L_n−2 s pevným bodem, nikoli
dvě a L_n. **F002 beze změny**, nový důkaz neduplikuje nález.

## 201(c): obecný počet aktualizací, nikoli jen n≤24

Pořadí položek je X1,Y1,…,Xn,Yn. MRV remízy vždy řeší toto pořadí,
jak odpověď výslovně požaduje. U jednoduchého bipartitního grafu je
lokální cena rozvětvení na vrcholu v

    1+d(v)+sum_{w soused v} d(w).

Pokrytí v stojí jednu hlavičku a d(v) uzlů; při větvi vw už položka
w ztratila řádek vw, takže její pokrytí stojí právě původní d(w).
Obnovení nepočítáme znovu jako další update, v souladu s definicí
úlohy a dříve přijatým měřením Algorithm X.

Označme P_m cenu cestového bipartitního grafu s hranami XiYj pro
|i−j|≤1, i,j=1,…,m, s týmž pořadím. P0=0, P1=3, P2=13.
Pro m≥3 je první X1 stupně2 a sousedé Y1,Y2 mají stupně2,3:
kořen stojí8. Větev X1Y1 nechá P_(m−1). Větev X1Y2 vynutí
Y1X2 za4 aktualizace a nechá P_(m−2). Proto

    P_m=P_(m−1)+P_(m−2)+12,
    P_m=5F_(m+3)−12 pro m≥1.

P0 je samostatná báze, vzorec pro něj netvrdíme.

Dále A_t označuje cenu posunutého řetězce s řádky1,…,t a sloupci
2,…,t+1, opět |i−j|≤1. X1 má jediného souseda Y2. Pro t≥3 má Y2
stupeň3, takže první vynucení stojí5 a nechá A_(t−1). Pro t=2
stojí4 a pro t=1 stojí3. Tedy A1=3 a A_t=5t−3 pro t≥2.
Transponovaný řetězec má stejnou cenu; jen první vynucená položka
je Y místo X. Tím je zohledněna i druhá orientace v kružnici.

Pro kruhový případ n≥4 má první X1 tři sousedy stupně3, tedy cenu13.
Větev X1Y1 nechá P_(n−1). V každé zbývající větvi X1Y2 nebo X1Yn
vybere MRV jako další Y1, stupně2, se sousedy stupňů2,3: cena8.
Jedna z jejích větví dokončí sousední transpozici a nechá P_(n−2),
druhá vynutí dlouhé kruhové posunutí a nechá A_(n−2) nebo transpozici.
Celkově

    U_n=13+P_(n−1)+2(8+P_(n−2)+A_(n−2))
       =P_(n−1)+2P_(n−2)+10n+3
       =5(F_(n+2)+2F_(n+1))+10n−33
       =5L_(n+2)+10n−33.

Pro n=3 je celý graf K3,3. Kořen stojí13 a každá ze tří větví
K2,2 stojí13, takže U3=52, shodně s touto formulí. Důkaz pokrývá
všechna n≥3 a doplňuje staré měření n=3,…,24 bez jeho opakování.

## Errata, výpočetní rozsah a navázání

Prohledáno všech šest relevantních vrstev: all4b, err4b, all4f5, err4f5
a oba originální TeX soubory. Zohledněna čísla otázek, knižní i fasciklové
strany a obsahové výrazy. Sousední známá oprava198(a) je již E092,
nikoli oprava199–201. F002, C002 ani C003 nemají nalezenou opravu.
Hashy, vzory a kontext jsou v results/matching199_201/errata-check.json
a errata-context.txt. Čerstvost archivu navazuje na
results/gould189_192/live-fascicle5-errata-check.json a retrieval soubory
snakes172; další stejné stahování nebylo nutné.

Přijaté výsledky unsat_3d_matching, determinant_matching, circular_matching
a algorithm_x_validation se pouze čtou. Jejich původní popis omezeného
rozsahu se nepřepisuje; obecná rozšíření jsou v tomto datovaném souboru.
Žádná nová dlouhá reprodukce ani solver. Vlastní výpočty nice15.
Další souvislý blok: operace na stromech 202–206 a změna heuristik207.
Svazek jako celek není dokončený.
