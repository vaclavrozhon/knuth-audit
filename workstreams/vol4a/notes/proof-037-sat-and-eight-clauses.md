# §7.1.1 p56 a úloha 39: pravděpodobnost, 3SAT a osm klauzulí

6. listopadu 2026, X0067. Originál p56/file73, zadání39 p85/file102,
odpověď39 p542/file559. Opravené (32) přímo z all4a-pre.pdf p7,
vlastní render images/proof-errata-pre-p7.png. Žádný program.

## P0626: úplná zkouška přiřazení a její rozsah

Pro n booleovských proměnných existuje přesně 2^n přiřazení;
vyhodnocení formule na každém z nich rozhodne splnitelnost.
Pro 30 proměnných je 2^30=1024^3=1 073 741 824, tedy vytištěné
„about a billion“. K počtu přiřazení se přičítá práce na jednotlivém
vyhodnocení; text netvrdí miliardu jako počet všech strojových operací.
Zakódovaná podmínka f(x)=1 má řešení právě v pravdivých vektorech
formule; to je přesný použitý význam modelování praktických problémů.
Neurčitá praktická formulace o mnoha problémech se 100 proměnnými
není údaj o konkrétním cenzu ani deklarovaná hranice složitosti.

## P0627: obě pravděpodobnostní věty s přesným experimentem

Položme m=2^n. Rovnoměrná volba z 2^m pravdivostních tabulek znamená
m nezávislých spravedlivých bitů. Jediná nesplnitelná tabulka je nulová,
takže

    Pr(SAT)=1−2^(−m).

Výraz „almost surely“ má zde asymptotický smysl: tato pravděpodobnost
jde k 1 s n, není doslova 1 pro pevné n.

Zkoušejme různá přiřazení v libovolném pevném pořadí a skončeme první
jedničkou nebo po m nulách. Počet provedených zkoušek T splňuje
Pr(T≥j)=2^(−j+1), 1≤j≤m. Proto

    E T = Σ_(j=1)^m 2^(−j+1) = 2(1−2^(−m)) < 2.

Pokud se slovem „find“ myslí pouze splnitelné instance, pak přesně

    E(T | SAT) = (Σ_(j=1)^m j·2^(−j))/(1−2^(−m))
               = 2−m/(2^m−1) < 2.

Obě přirozené konečné interpretace tedy dávají vytištěnou mez. Není
použito nekonečné čekání na úspěch u nulové funkce ani opakování již
vyzkoušeného bodu. Pro n=0 je m=1 a oba uvedené průměry jsou 1;
tehdy ovšem pravděpodobnost SAT je 1/2, jak udává přesný vzorec.
Tvrzení o obtížnosti praktických formulí se tím nezaměňuje s průměrem
přes rovnoměrně náhodné celé tabulky.

## P0628: opakované literály, tři různé proměnné a dolní mez osmi

3CNF zde znamená tři literály v každé klauzuli, s opakováním povoleným.
Jedna taková klauzule je splnitelná (stačí splnit jeden její literál),
prázdný seznam klauzulí je pravdivý. Dvě klauzule

    (x∨x∨x) ∧ (¬x∨¬x∨¬x)

jsou nesplnitelné, takže dvě je nejmenší možný počet bez dalšího omezení.

Jsou-li v každé klauzuli tři různé proměnné, uniformní přiřazení
zneplatní klauzuli právě s pravděpodobností 1/8: z osmi hodnot jejích
tří literálů je zakázána jen 000, ostatní proměnné jsou volné.
Pro m takových klauzulí dává union bound

    Pr(všechny pravdivé) ≥ 1−m/8.

Pro m≤7 je tedy funkce splnitelná a náhodné přiřazení uspěje
s pravděpodobností alespoň 1/8. Nezávislost různých klauzulí se
nepředpokládá. K nesplnitelnosti je nutných alespoň osm; příklad níže
ukazuje dosažitelnost. Slovo „interesting“ v textu není další
matematická optimalizační podmínka.

## P0629: všechny klauzule (32), všechna přiřazení a známé přeuspořádání

Očíslujme klauzule v původním prvním dotisku C_1,…,C_8. Jejich
nulové podkrychle jsou přesně následující; pořadí bitů je x_1x_2x_3x_4.

| Klauzule | Její nulová krychle | Obě přiřazení |
|---|---|---|
| C_1=x_2∨x_3∨¬x_4 | *001 | 0001,1001 |
| C_2=x_1∨x_3∨x_4 | 0*00 | 0000,0100 |
| C_3=¬x_1∨x_2∨x_4 | 10*0 | 1000,1010 |
| C_4=¬x_1∨¬x_2∨x_3 | 110* | 1100,1101 |
| C_5=¬x_2∨¬x_3∨x_4 | *110 | 0110,1110 |
| C_6=¬x_1∨¬x_3∨¬x_4 | 1*11 | 1011,1111 |
| C_7=x_1∨¬x_2∨¬x_4 | 01*1 | 0101,0111 |
| C_8=x_1∨x_2∨¬x_3 | 001* | 0010,0011 |

Každý řádek plyne nastavením jeho tří literálů na 0. Pravý sloupec
obsahuje každé ze šestnácti čtyřbitových čísel právě jednou, což je
úplný ručně zapsaný certifikát rozkladu krychle. Osm klauzulí tedy
vylučuje vše. Vynechání libovolné jediné klauzule ponechá přesně její
dva body; shodují se ve třech souřadnicích a liší se ve čtvrté. To
dokazuje oba dodatky o sedmi klauzulích, včetně přesného počtu řešení
a tří vynucených proměnných. Vynechání C_8 dává x_1x_2x_3=001.

Známá úprava z 17.6.2013 seřazuje tytéž klauzule jako

    C_8,C_1,C_2,C_3,C_4,C_5,C_6,C_7,

s pouhou permutací literálů uvnitř některých klauzulí. Proto je v
opravené větě „last seven“, kde v prvním dotisku bylo „first seven“.
V obou verzích se vynechává C_8 a platí stejný závěr 001.
Známá změna není nález; nezávisle je doložen jak výsledek, tak každá
část příkladu po jejím uplatnění.

## P0630: úloha 39, všechny čtyři klauzule pro libovolné hradlo

Pro binární operaci o, vstupy l,r a výstup y vytvoříme pro p,q∈{0,1}

    c_pq = y^((1−(p o q))N) ∨ l^(pN) ∨ r^(qN),

kde a^(0N)=a a a^(1N)=¬a. Je to přesný význam sazby s pruhem nad
p o q v odpovědi. Když (l,r)≠(p,q), některý ze dvou vstupních
literálů je 1. Když (l,r)=(p,q), zůstane pouze výstupní literál,
který nutí y=p o q. Konjunkce čtyř klauzulí je proto ekvivalentní
y=l o r, pro každou ze všech šestnácti operací v Table 1.

Pro o=∧ vzniká doslova

    (¬y∨l∨r) ∧ (¬y∨l∨¬r) ∧ (¬y∨¬l∨r) ∧ (y∨¬l∨¬r),

ve shodě s příkladem odpovědi. Pokud oba vstupy označují stejnou
proměnnou, některé klauzule jsou tautologické, ale předchozí důkaz
pro skutečné hodnoty l,r stále platí. Nevyžaduje různost tří
proměnných uvnitř klauzule. Konstantní binární operace jsou rovněž
přípustné a dávají stejným argumentem pevný y.

Známé přeznačení odpovědi z 9.12.2015 definuje x^p=[x=p] a píše
c_pq=y^((¬p) o (¬q))∨l^p∨r^q. Při skutečném vstupu (a,b) je jediná
omezující klauzule indexovaná p=¬a,q=¬b; její výstupní literál je
[y=a o b]. Jde tedy o reindexaci téže čtveřice klauzulí a celý důkaz
platí také po známé úpravě. Opravený AND příklad je stejná čtveřice
v opačném pořadí. Původní sazba errata je v
images/proof-errata-answer39-detail.png; tato notace není nový nález.

## P0631: invariant celé konstrukce, ekvivalence a náklady

Předpoklad je opravený N>0. Každému vnitřnímu uzlu stromu přiřadíme
čerstvou proměnnou y_i v preorder, takže kořen je y_1. Listový
potomek označuje svoji původní proměnnou x_j, vnitřní potomek svoji
novou y. Opakované listy se stejným x_j nejsou omylem považovány
za nezávislé proměnné.

Pro každé pevné x existuje právě jedno rozšíření na všechna y,
které splňuje všechny rovnosti hradel. Indukční invariant směrem
od listů říká, že y uzlu je přesně hodnota jeho podformule. Existence
plyne vyhodnocením stromu, jednoznačnost stejnou indukcí z P0630.
Přidání klauzule (y_1∨y_1∨y_1) vynutí pravdivý kořen. Tedy pro
každé x zvlášť

    f(x)=1  ⇔  existují y_1,…,y_N s F(x,y)=1.

Konstrukce má právě N nových proměnných a 4N+1 klauzulí, všechny
se třemi literály. Klauzule se pro tento přesný počet nesimplifikují
ani nededuplikují. Strom se obejde konečně; každý uzel vytvoří
konstantní počet klauzulí. Čas a velikost jsou O(N) v modelu práce
s odkazy na proměnné; při binárním zápisu jmen je výstup
O(N log(n+N)) bitů a konstrukce zůstává polynomiální v běžné délce
vstupu. N=0 je výslovně vyloučeno známým erratem, takže y_1 vždy
existuje. Samotná formule tvořená jedním listem by se řešila zvlášť,
nikoli neexistujícím kořenem této konstrukce.

## P0632: přesný význam srovnání obtížnosti 3SAT

P0631 je polynomiální redukce formulového SAT na zde definované
3SAT. Opačný směr pouze bere 3CNF jako obecnou formuli. S explicitním
externím vstupem P0614 o NP-úplnosti formulového SAT je tedy 3SAT
NP-těžké; je také v NP, protože přiřazení ověříme průchodem klauzulí.
To dokládá tvrzení na p56 „not really easier“, aniž by předpokládalo
neprokázané P≠NP. Žádný nový externí důkaz úplnosti není potřebný.

## Úplná mapa p56, meze a errata

- První odstavec: P0626, výstižný počet přiřazení a význam formule.
- Náhodné pravdivostní tabulky: P0627, přesná pravděpodobnost i oba
  konečné významy průměrného počtu zkoušek.
- Definice (31), opakované literály, redukce a obtížnost: P0628,
  P0630–P0632; zkontrolována celá související úloha39 i odpověď.
- Nejkratší nesplnitelný případ, distinct-variable doména a mez sedmi:
  P0628, bez neplatného předpokladu nezávislosti klauzulí.
- Osm klauzulí (32) a všechny závěry posledního odstavce: P0629,
  včetně známého přeuspořádání.

P56/file73 je tím matematicky celá doložena. Historické autorství
Rivestova šifrovacího příkladu a jeho odkaz na §6.5–13 nejsou
nezávisle ověřeny; zde použitý certifikát nevyžaduje vlastnosti šifry.
Peirceova citace na odpověďové p542 nebyla bibliograficky ověřena.
To jsou bibliografické výjimky, nikoli nevyřešené předpoklady důkazu.

Relevantní all4a-pre/all4a/err4a/all4f0/err4f0 zohledněny;
pro související odkazy byly prohlédnuty také all4f1/err4f1. Změna
2^n na „2^n-bit“ byla už zapracovaná v prvním dotisku 4A. Odkaz 7.9
je známě nahrazen 7.2.2.2, (32) přeuspořádáno, v39 doplněno N>0
a v její odpovědi změněna notace mocnin, jak je doloženo výše.
Žádná z těchto známých oprav není nálezem. P85/p542 nejsou celé
argumentově uzavřeny, protože ostatní úlohy/odpovědi zůstávají ve frontě.
Další text p57/file74; sekvenční úlohový kurzor26 se nepřeskakuje,
hotová39 se později převezme bez opakování.
