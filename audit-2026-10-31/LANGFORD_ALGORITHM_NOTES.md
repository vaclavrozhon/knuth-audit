# Algorithm L a úlohy 7.2.2–17–22

Kontrola 1. listopadu 2026. Přečteny původní stránky 35, 56, 399 a 400;
odpovědi 20–22 také v autorově Pre-Fascicle 5B, str. 38 (11. září 2019).
Doslovná stavová implementace je v [check_langford_algorithm.py](check_langford_algorithm.py).
Nezávislý model umisťuje celé dvojice v pořadí od největšího označení k nejmenšímu;
nepoužívá spojové seznamy ani vyplňování prvního prázdného místa.

## Ověřené části

**L.** Seznam od p₀ obsahuje právě dosud nepoužitá kladná označení, vzestupně.
Při volbě k se nastaví oba jeho výskyty a uloží předchůdce j. Při návratu
z hlubších úrovní jsou všechny jejich zásahy vráceny; p_k proto opět ukazuje
na původního následníka a p_j←k skutečně obnoví seznam. Záporný výskyt
je pevně vynucený a není samostatným rozhodnutím. Algoritmus tak projde
všechny přípustné prefixy právě jednou, v lexikografickém pořadí.
Když nejmenší dostupné k přesahuje pravý okraj, přesahují jej i všechna větší.

**17.** Znaménko rozlišuje rozhodnutí od jeho vynuceného druhého výskytu.
Navržená změna testu v L2 na x_l≠0 tam funguje; rozbije se však L5.
Například n3, rozhodnutí x₁=1,x₂=2, vedou přes vynucenou pozici3 na l4.
Zbývající3 se nevejde, takže L5 couvne na3. Bez záporné značky by považoval
druhý výskyt1 za samostatné rozhodnutí a použil dosud neinicializované y₃.

**18.** Přesná simulace dává x₄…x₈=(-2,-1,0,-4,0), p₀…p₄=(3,3,3,0,0),
y₁…y₈=(1,3,0,2,0,nepoužito,nepoužito,nepoužito). Souhlasí i poznámka
o historických hodnotách y₄,y₅. Celý strom (9), včetně 27 uzlů a všech
kladných rozhodnutí na hranách, odpovídá vyobrazení.

**19.** Obě navržené domény obsahují každý možný výskyt: kladné k musí
splňovat l+k+1≤2n, záporné -k musí mít první výskyt na l-k-1≥1.
Podmínka permutace ve formulaci (7) dále vylučuje označení mimo ±1,…,±n.
Alternativní domény tedy samy nemusejí být v tomto rozsahu těsné.

**20.** Poslední možný začátek k je 2n-k-1. Je-li tato pozice již vynuceně
záporná a k dosud nebylo umístěno, větev nemá řešení. Je-li volná, zbývá
právě k. Větší dosud neumístěné označení by muselo být odhaleno při předchozí
pozici; proto je vynucené k poslední v seznamu a po jeho vyčerpání nelze
zkoušet nepřípustnou alternativu. Toto vysvětluje i správnost přeskakování
záporných pozic: test se provádí na každé z nich.

**21.** Duální pozice prvního výskytu k je 2n+1-(k+1)-j=2n-k-j.
Pro liché n zvolíme k=n, pro sudé k=n-1. Součet obou prvních pozic je
pak lichý, takže právě jedna leží v předepsané první polovině. Dodatečný
návrat L5 po vyčerpání této vynucené volby zabraňuje zkoušení většího označení.
Základní L, verze20 i verze21 souhlasí s nezávislým modelem pro všechna
n=1,…,10; pro symetrickou verzi se porovnávají celé dvojice, nikoli jen počty.

**22, správné části.** Zde d(k)=floor(3k/2). Přímá kontrola potvrzuje všechny
uvedené malé svědky. Pro n=2m je součet vzdáleností 3m²+m, pro n=2m+1
je 3m²+4m+1. Musí mít stejnou paritu jako součet všech pozic, tedy jako n.
To vylučuje n≡3 modulo4. Hodnoty n=1,2 jsou samoduální.

Pro n≥4 je vytištěné n′ zvoleno tak, aby d(n′) bylo sudé. Mez h z odpovědi
je přesně n-d(n′)/2; první pozice n′ v duálních řešeních mají součet 2h+1.
Matematické pravidlo pro výběr jedné poloviny řešení je tedy správné.
Správný je také index q=floor((4n+2-2l)/3) pro termín vynuceného umístění.
Vzdálenosti některá celá čísla vynechávají; v takové pozici už musí být q
umístěno z předchozího kroku. Samotná verze20 s těmito vzdálenostmi funguje.

Celá vytištěná tabulka pro n=1,…,16 byla přepočtena nezávislým bitovým
modelem [loose_langford_counts.cpp](loose_langford_counts.cpp). Dostává
1,1,0,2,4,20,0,156,516,2008,0,52536,297800,1767792,0,75678864.
Nuly n≡3 modulo4 v tomto běhu vyplývají z právě uvedeného důkazu; nejsou
vydávány za samostatný obrovský výčet. Model vybírá první volné pole,
kontroluje nejzazší přípustný začátek největšího zbývajícího označení a
podmínku pro symetrii testuje přímo při umístění n′.

## F082: neúplné přenesení úprav21 na loose párování

Strana400, odpověď22, druhý odstavec. Doslovné substituce do odpovědí20–21
mají dva různé projevy chybějícího ošetření vynucené volby.

**n=6: dvě současné povinnosti.** Máme n′=4,h=3. Při l=3 a již zvolených
x₁=2,x₂=5 jsou dosud nepoužitá 4 i 6. První vložený test v L3 vybere4
kvůli symetrii; druhý je přepíše na6, které musí začínat právě zde.
Takovou větev je však třeba odmítnout, protože obě různé hodnoty nemohou
začínat v jedné pozici. Chybná větev vydá například

    (2,5,6,-2,4,3,1,-1,-5,-3,-4,-6).

Vydá i jeho dualitu, která má4 na pozici2. Celkem navštíví13 řešení místo10;
tři duální dvojice jsou navštíveny oběma způsoby. Úplných řešení je20,
jak kniha správně uvádí.

**n=10: opakování nepřípustné vynucené volby.** Máme n′=8,h=4. Dosažitelný
prefix začíná (1,-1,9), tedy x₁₆=-9, a seznam zbývajících označení je
(2,3,4,5,6,7,8,10). Při l=4 vybere symetrický test8, ale jeho druhé pole16
je obsazené. L4 pokračuje na10. Při novém L3 se cyklus hledající8 projde
přes 10,0,2,3,4,5,6,7,8, opět narazí na obsazené pole16 a vrátí se na10.
Žádné pole ani úroveň se nemění: jde o skutečný nekonečný cyklus, nikoli
jen pomalé hledání. Oddělený malý důkaz cyklu je uložen ve výsledcích.

Stačí dvě opravy:

1. Pokud současné podmínky vynucují různá označení, okamžitě jít do L5.
2. Pokud selže pokus o symetricky vynucené n′, jít také rovnou do L5.
   Původní dodatek k L5 ošetřuje až návrat z úspěšného umístění, nikoli
   odmítnutí obsazeným druhým polem. Lze proto přidat tentýž test
   `l=h and k=n′` i na začátek L4.

S oběma opravami přesný výčet pro n=4,…,10 dává každou duální dvojici právě
jednou, včetně10 reprezentantů pro n6 a1004 pro n10. Oprava zachovává
správnou povinnost n′ umístit nejpozději na h, a proto odřezává pouze větve,
které tuto povinnost již nemohou splnit.

Znění potvrzeno v [PDF](images/vol4b-p400.png) i
[autorově PS](images/fasc5b-p38.png). Dne1.11.2026 prohledány celé
err4b.textxt, err4f5.textxt a jejich historické vrstvy all4b/all4f5;
relevantní oprava nenalezena. Známá změna ve Fascicle5 na str208 se týká
úlohy24 (x₃→x_l), nikoli tohoto algoritmu. Fyzický výtisk zatím neověřen.

Výsledky: [doslovná L a nezávislé modely](results/langford_algorithm/verified.json),
[opakující se cyklus](results/langford_algorithm/nontermination-cycle.json),
[úplná tabulka](results/langford_algorithm/counts.json),
[metadata běhu](results/langford_algorithm/counts-run.json),
[návrh hlášení](knuth-report-f082-draft.txt).

Velké běhy n17 na stranách35–36 zůstávají otevřené; nyní je prověřuje
samostatný dlouhý runner popsaný níže. Údaj9.93 gigamems byl doplněn
následnou kontrolou. Model paměťových přístupů se nesmí zaměnit za sekundy.
Samotný počet uzlů n15 byl navíc přepočten doslovnou implementací
[langford_literal.cpp](langford_literal.cpp): **396535288**, což správně
zaokrouhluje na vytištěných397 milionů. Výsledný profil je v
[literal15.json](results/langford_algorithm/literal15.json). V tomto případě
nemají obě nové opravy vliv na strom, protože vynucené n′=15 je největší
označení a jeho termín se nekryje s termínem pravého okraje.

## Doplnění memů úlohy22

[langford_mems.cpp](langford_mems.cpp) přidává explicitní čítání přístupů
do polí x,p,y,a. Vlastní implementace vychází z vytištěných kroků a
opravF082; není vydávána za dochovaný původní Knuthův měřicí program.
Pro n1–10 byly ověřeny celé množiny výstupů a profily všech tří běžných
variant L,L20,L21; pro n4–10 také opravená loose varianta. Celkem37 případů
souhlasí s dřívější doslovnou simulací a nezávislým modelem, který umisťuje
celé dvojice od největšího označení. Kontrolují se i duální třídy, ne jen počty.

Dokončený loose běh n15 má znovu přesně396535288 uzlů a nulový počet
řešení. Každá položka profilu souhlasí s dřívější implementací. Při
uchování x_l z posledního testu smyčky L5 do registru potřebuje9537980169
memů. Při doslovném účtování dalšího načtení v `k←x_l` přibude jeden mem
na každou úspěšnou hranu, tedy396535287. Výsledkem je **9934515456 memů**,
což souhlasí s knižními9.93Gμ.

U n15 je n′=15 největší označení a h=4<8 je před prvním termínem pravého
okraje. Oprava kolidujících povinností proto nikdy nezabere. Druhá oprava
F082 může pouze ušetřit jedno nadbytečné čtení p15=0 po neúspěšné vynucené
volbě. Každý takový případ odpovídá jednomu prefixu prvních tří polí;
těch je nejvýše15³=3375. Přímé účtování původního neopraveného postupu
proto leží v intervalu

    [9934515456, 9934518831],

který se celý zaokrouhluje na9.93Gμ. To uzavírá poslední výkonový údaj
úlohy22 bez předstírání přesné shody s neveřejným původním čítačem.
Ověření výsledku a meze znovu nic neprohledává:
[check_langford_mem_claims.py](check_langford_mem_claims.py),
[claims-checked.json](results/langford_mems/claims-checked.json).

Příkazy, kontrolní součty a všech37 malých případů obsahuje
[validation.json](results/langford_mems/validation.json); úplný n15 výsledek
je v [loose15.json](results/langford_mems/loose15.json).

## Dlouhé kontroly hlavního textu, n17

[run_langford_mems.py](run_langford_mems.py) byl spuštěn1.11.2026
v15:55:50UTC a postupně prověřuje L21, L20 a základní L. Nejdříve zpracuje
nejmenší z těchto tří stromů. Paritní důkaz nemožnosti se nepoužívá jako
zkratka, protože by neověřil uváděné počty uzlů a memy. Každý případ má
limit172800 sekund, vlastní PID, příkaz, log průběhu a výsledný JSON.

Runner kontroluje hash zdroje i již ověřené binárky, používá procesový
zámek a hotové případy při navázání nepřepočítává. Nedokončené případy
vyžadují prohlédnutí; timeout není nulový počet řešení ani potvrzená mez.

První varianta **L21** skončila1.11.2026 v18:27:21UTC s návratovým kódem0,
po9090.343sekundách. Úplný profil má **160392399085uzlů**, žádné řešení
a3943329114242přístupů při knižním načtení L5 bez cache. Všechny tři
vytištěné hodnoty na36 se správně zaokrouhlují: **160 miliard**, **3.94Tμ**
a **24.6μ/uzel**. Všechny mezivýsledky jsou v `n17-L21.json`, metadata
a hash v `n17-L21-run.json`; `check_langford_mem_claims.py` ověřil jejich
shodu s neměnným zdrojem a dřívější malou validací. Verze s jedním
načtením L5 do cache má3782936715158memů a není zaměňována za knižní
účtování. Rozdíl je přesně počet uzlů minus1.

Varianta **L20** skončila1.11.2026 v23:23:09UTC, návratový kód0,
po17712.628sekundách. Úplný profil má **330438173533uzlů** a žádné
řešení. Knižní načítání L5 bez cache dává **8073717908199memů**;
kontrola `check_langford_mem_claims.py` potvrdila všechna tři zaokrouhlení
na str36: **330 miliard**, **8.1Tμ**, **24.4μ/uzel**. Cache varianta
má7743279734667memů a nezaměňuje se za tištěný model.

Původní runner pokračuje základní variantou L, dítě845134. Tento
poslední případ zůstává neuzavřený; první dva úspěchy neověřují jeho
počet uzlů ani výkonové hodnoty. Proces byl skutečně potvrzen živý,
nic se nespouštělo znovu.
Stav je v [large-wrapper.json](results/langford_mems/large-wrapper.json).
Dokud případ neskončí, odpovídající tvrzení ze str35–36 zůstává otevřené.
