# Theorem S, redukované mediánové množiny a začátek sítí

Checkpoint X0106, P0991–P0999. Originály p72–73/file89–90
prohlédnuty. Jde o celý Theorem S, celý odstavec o redukci,
princip 0–1 pro sorting networks, sémantiku CI modulů
a obecné předpoklady relací v důkazu F. Konkrétní síť69,
všech16 hodnot70 a konkrétní seznam71 jsou následující blok.

Přebíráme původní definice Krom clauses (nejvýše dva literály),
mediánové axiomy, Theorem G pro neprázdnou konečnou algebru
P0877–P0885 a přesnou isometrii/hranové projekce P0927/P0945.
Žádný program ani enumerace nebyly spuštěny.

## S: nutnost, obě vytištěné větve a všechny typy literálů — P0991

Nechť tři splňující přiřazení dávají ve dvojici literálů
hodnoty (x_1,x_2),(y_1,y_2),(z_1,z_2), každé s OR=1.
Přeznačme celá tři přiřazení tak, aby x_1≤y_1≤z_1.
Medián prvních souřadnic je y_1. Je-li y_1=1, klauzule
je ihned splněna. Je-li y_1=0, pak x_1=y_1=0, takže
x_2=y_2=1 a medián druhých souřadnic je1. To dokazuje
každý krok tištěné nutnosti.

Pro negovaný literál platí NOT M(x,y,z)=M(NOT x,NOT y,NOT z),
takže tentýž důkaz pokrývá libovolné znaménko každého
literálu. Jednotková klauzule fixuje hodnotu ve všech
třech vektorech a medián ji zachová. Prázdná klauzule
nemá modely, tedy podmínku splňuje vakuózně. Konjunkce
zachovává vlastnost, protože její modely jsou průnikem
modelových množin jednotlivých klauzulí.

## S: všechny svědecké vektory prime clause — P0992

Vezměme netautologickou minimální implikovanou klauzuli
u_1∨...∨u_k se vzájemně různými proměnnými. Minimalita
znamená, že po odstranění u_j již nejde o implikovanou
klauzuli. Proto existuje x^(j) s f(x^(j))=1, na němž
všechny u_i pro i≠j mají hodnotu0. Původní klauzule
je implikovaná, takže u_j má hodnotu1.

Je-li k≥3, vezměme medián x^(1),x^(2),x^(3). Pro
každé i∈{1,2,3} jsou dvě ze tří hodnot u_i nulové;
pro i>3 jsou nulové všechny. Komutace s negací ukazuje,
že každý u_i je na mediánu nulový. Uzavřenost modelů
ale dává f=1, což odporuje klauzuli. Tedy k≤2.
Vytištěný výběr právě tří svědků funguje pro každé
k≥3, nejen pro k=3.

## S: existence potřebné CNF, konstanty a přesná ekvivalence — P0993

Pro každé nesplňující přiřazení a existuje plná klauzule,
která je nepravdivá právě v a: v každé proměnné použije
literál s opačnou hodnotou než a. Tato klauzule je
implikována f a je netautologická. Postupně z ní smažme
každý literál, jehož odstranění implikovanost zachová.
Konečný proces skončí minimální klauzulí, stále nepravdivou
v a. P0992 má pro ni délku nejvýše2.

Konjunkce takto získaných klauzulí je pravdivá na všech
modelech f a vylučuje každé jeho nesplňující přiřazení,
takže je rovna f. Tím je z „každá prime clause je krátká“
doložen i nezbytný přechod k úplné 2CNF reprezentaci.
Není třeba zahrnovat tautologické klauzule.

Pro f=1 je konjunkce prázdná. Pro f=0 se minimální
klauzule vyprázdní; jde o standardní konstantní0 CNF.
Při alespoň jedné proměnné lze totéž napsat x∧NOT x.
Při nulovém počtu proměnných jsou právě dvě možné
modelové množiny ∅ a {()}, obě mediánově uzavřené,
a odpovídají konstantám0,1 se standardními prázdnými
spojkami. Toto je celý význam (68) a následné ekvivalence
median sets se všemi 2SAT modelovými množinami.

## Přesný význam redundantní souřadnice — P0994

Projekce, která vynechá souřadnici k, je vždy mediánový
homomorfismus. Je injektivní právě když v X neexistují
dva různé vektory lišící se pouze v k. V takovém případě
souřadnice nepřidává rozlišení prvků a lze ji odstranit
bez změny abstraktní mediánové algebry.

Naopak existence vytištěné dvojice x^(k),y^(k), se
x_k=0,y_k=1 a všemi ostatními souřadnicemi stejnými,
znamená, že odstranění k slije dva různé prvky. Definice
reduced je tedy přesně irredundance v tomto smyslu,
nepouze požadavek různých sloupců. Redukované hranové
štítky grafu tyto dvojice mají: stačí konce kterékoli
hrany dané souřadnicové třídy, podle P0944.

## Z redukované množiny ke skutečnému mediánovému grafu — P0995

Nechť neprázdné X⊆{0,1}^t je mediánově uzavřené a
redukované. Bodový medián dělá z X konečnou algebru;
Theorem G jí přiřadí souvislý mediánový graf s hranou
u–v právě při dvoubodovém algebraickém intervalu I(u,v).

Každá dvojice lišící se jediným bitem má dvoubodový
interval, a tedy je hranou. Zbývá opačný směr, který
nelze odvodit jen z uzavřenosti množiny. Kdyby algebraická
hrana u–v měnila více než jeden bit, zvolme jednu měněnou
souřadnici k a její redukční svědky p,q lišící se pouze
v k. Projekce

    m(p,u,v), m(q,u,v)

leží v dvoubodovém I(u,v). Liší se právě v k: v k
medián ponechá p_k versus q_k, protože u_k≠v_k;
v každé jiné pozici mají shodné vstupy p_i=q_i.
Jsou tedy různé a musejí to být u,v. To však vylučuje,
aby se u,v lišily v další pozici. Spor.

Všechny algebraické hrany jsou tudíž přesně all-but-one
rovnosti v definici grafu na p72. Theorem G nyní skutečně
dokazuje jeho souvislost a mediánovou vlastnost; žádná
nedoložená existence jedné-bitových cest není předpokladem.

## Původní vektory jako hranové štítky a nulární mez — P0996

Každá evaluační souřadnice je homomorfismus a mění se
na své svědecké hraně. P0944 ji tedy ztotožňuje s
orientovanou projekcí na tuto hranu. Různé souřadnice
nejsou stejné ani komplementární: svědecká hrana jedné
mění jen ji. Každá grafová hrana mění některou z nich,
takže jiné hranové třídy nechybějí. Původní vektory X
jsou přesně redukované mediánové štítky při této volbě
orientací souřadnic.

Normalizujeme-li navíc libovolný kořen na nulový řetězec,
komplementují se právě jeho jedničkové pozice. P72
nepředepisuje tuto dodatečnou normalizaci; původní X
nemusí obsahovat nulový vektor. Jeho tvrzení o původních
vektorech proto nevyžaduje takový předpoklad.

Pro t=0,X={()} jde o jediný vrchol a prázdný štítek.
Pro t>0 redukční svědci zaručují neprázdnost X.
Zbývá pouze společná dosavadní konvenční mez P0886:
X=∅,t=0 splňuje podmínku svědků vakuózně, ale pojem
prázdného mediánového grafu/jeho souvislosti zůstává
neuzavřený. Nepřidáváme novou kartu a tento případ
nepovyšujeme na důkaz celé stránky.

## Komparátory, celý princip 0–1 a CI homomorfismus — P0997

Komparátor zachová dvojici vstupních hodnot a vydá
min nahoru, max dolů. Každá neklesající prahová mapa
θ z uspořádaných hodnot do{0,1} komutuje s min i max,
a indukcí tedy s celou sítí komparátorů.

Jestliže síť na nějakém vstupu vydá inverzi A>B,
vyberme práh mezi nimi; výstupní bity mají inverzi10.
Správnost na všech binárních vstupech proto implikuje
správnost na všech uspořádaných hodnotách, i s rovnostmi.
Naopak libovolný binární vstup lze získat prahováním
permutace1,...,n, když všem nulovým pozicím přiřadíme
nižší různé ranky než jedničkovým. Správnost na všech
n! permutacích a komutace s prahem pak dává správnost
na všech2^n binárních vstupech. Pro n=0,1 je tvrzení
přímo triviální. To je přesně odkazovaná Theorem5.3.4Z.
V evidenci vol3 nebyl nalezen hotový cílený důkaz, který
by se místo tohoto krátkého argumentu převzal.

Pro booleovské hodnoty min=AND,max=OR; invertor mění
bit na jeho doplněk. Dvouvstupový komparátor má úplnou
mapu00→00,01→01,10→01,11→11. Všechny čtyři hrany
2-krychle (00–01,00–10,01–11,10–11) zobrazí na hranu,
nikoli na jediný vrchol. Změna na nezúčastněné linii
se pouze přenese. Invertor je krychlový automorfismus.
Kompozice modulů tedy posílá každou hranu t-krychle
na hranu, přesně podle tvrzení p73 o homomorfismu.
Nejde o tvrzení o injektivitě; dva nesousední vstupy
01 a10 se na komparátoru mohou slít.

## Obecné dvojice sloupců na začátku důkazu F — P0998

Svědecká hrana souřadnice i dává v páru i,j vzory
(0,c),(1,c); svědecká hrana j dává (d,0),(d,1).
Tyto dvě různě orientované hrany čtverce mají nejvýše
jeden společný konec, takže dohromady jsou přítomny
aspoň tři ze čtyř vzorů. Může chybět nejvýše jeden.
Všechny čtyři tištěné překlady jsou:

| chybějící vzor (i,j) | klauzule | obě stejné implikace |
|---|---|---|
| 00 | i∨j | NOT j→i, NOT i→j |
| 01 | i∨NOT j | j→i, NOT i→NOT j |
| 10 | NOT i∨j | i→j, NOT j→NOT i |
| 11 | NOT i∨NOT j | i→NOT j, j→NOT i |

Protože každý sloupec nabývá obou hodnot a X je
neprázdné, nemá jeho indikátor žádnou jednotkovou ani
prázdnou implikovanou klauzuli. Theorem S dává úplnou
reprezentaci právě těmito zakázanými dvojicemi; mohou
být uvedeny všechny platné implikace, ne pouze prime
podmnožina, aniž se množina modelů změní.

## Acykličnost a nepřítomnost cesty ke komplementu — P0999

Všechny uvedené implikace platí na každém vektoru X.
Pokud by tvořily orientovaný cyklus přes dvě různé
literálové proměnné, byly by v celé X hodnoty těchto
literálů stejné. Svědecká hrana jedné z dotčených
souřadnic však mění právě její literál a druhý ponechá,
což je spor. Pokud cyklus obsahuje proměnnou i její
doplněk, vyžaduje jejich rovnost v neprázdném X, opět
spor. Smyčky se nevytvářejí, protože se zpracovávají
jen různé sloupce. Graf relací je tedy acyklický.

Cesta od literálu u k jeho komplementu by v každém
modelu vynutila u=0. Redukční svědci této souřadnice
však dávají i u=1. Taková cesta proto neexistuje.
To jsou obecné předpoklady budoucího antisymetrického
topologického pořadí; konkrétní pořadí72 a celá
konstrukce F dosud nejsou tímto argumentem uzavřeny.

## Bibliografie, errata a přesný rozsah

Primární ACM záznam potvrzuje Schaefer, *The complexity
of satisfiability problems*, STOC1978,216–226, DOI
10.1145/800133.804350. Přesné číslování Lemma3.1B a
historická priorita nebyly v plném článku nově ověřeny;
Theorem S má zde úplný nezávislý důkaz. Metadata jsou
v `sources/schaefer1978-metadata.json`.

Pět relevantních vrstev errat pro p72–73/Theorem S/
reduced sets prověřeno. Známá úprava formulace F p73
zůstává pro další blok, nikoli nový nález. Celý obsah
p72 má nyní argument pro neprázdnou redukovanou množinu;
jediná konvenční mez X=∅,t=0 je přesně společná P0886.
P72 proto zůstává partial. P73 má nyní obecný CI
homomorfismus, vzory/implikace a acykličnost; síť69,
tabulka70, vztahy71 a vlastní věta F následují.
