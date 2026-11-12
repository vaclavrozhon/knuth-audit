# Recovery §1.4.4: celý kruh bufferů a všechny části 9–14

X1019 pokrývá hlavní text 218 od „Multiple buffers“ až po
první odstavec 224, všechny kroky A/R/B, vazbu a celé úlohy
9–14 včetně tabulek 227/533. Úvody k poolingu, sdílenému
kanálu a čtyřbarevnému kruhu na 224–225 se dokončí spolu
s 16–17; tento blok nepředstírá hotovou celou sekci.

Původní obrazy 218–227 a 533 jsou přímo přečtené, stejně
jako plné notes/circle.md, notes/comparison.md, programs.py,
check_circle.py a check_comparison.py. Každý uložený čas
a každá větev comparison.json byly přečteny; staré testy
se nespouštěly. Převzaté otisky i čtyři vrstvy errat jsou
v results/quality-recovery-input-output-circle-errata-2026-11-07.json.

C0033 zůstává dříve potvrzený nález v odpovědi 12; nic nového
se nepřidává. Opravuje se však naše starší příliš široká
věta o Fig.25: obě šipky jsou B6→B2, ale původní RELEASE
má chybně označený krok B1 místo R1. Tato přesná změna je
už obsažena ve známé náhradě obrázku z 8.8.1997.

## 1. Všechny významy, hranice a barvy

N≥1 je konečný počet platných oddělených bufferů. Pro každý
buffer je předchozí buňka platná a obsahuje adresu následujícího
v jediném N-prvkovém cyklu. Data mají přesně délku zařízení;
linky neleží v přenášených slovech. Ve skutečném MIX se cyklus,
linky, program a soukromá data vejdou do paměti, tedy i počty
a všechny ukazatele do kladných dvoubytových indexů.

G znamená připravený buffer: na vstupu hotová data, na výstupu
volná oblast. Y vlastní výpočet, který ji získal ASSIGN a ještě
neudělal RELEASE. R je oblast předaná řídicí rutině; zahrnuje
čekající I/O, právě probíhající I/O i fyzicky dokončené I/O,
jehož dokončení ještě CONTROL nezapočítal. Poslední rozlišení
je nutné, protože hardware končí mezi procesorovými instrukcemi.

Při původním střídání ASSIGN/RELEASE je y∈{0,1}. Od NEXTR
jdou po kruhu nejprve n červených, potom případná jediná žlutá
a poté N−n−y zelených. NEXTG je začátek zeleného úseku;
CURRENT je žlutá. U prázdného úseku má ukazatel význam jeho
hranice. Po dokončení příslušných atomických algoritmických
kroků platí 0≤n+y≤N. Kód nemusí příznak barvy fyzicky ukládat:
barva je určena hranicemi, n a přítomností platného CURRENT.

ASSIGN se v původním rozhraní volá jen při y=0. Proto n<N
znamená právě alespoň jeden G, a nikoli obecně pouze
„nejvýše N−1 červených při libovolném počtu žlutých“.
Změna NEXTG na Y a jeho posun prodlouží žlutý úsek o jedno.
RELEASE připojí jediný Y ke konci červeného úseku a zvýší n.
CONTROL vybírá první R, po dokončení jej změní na G, posune
NEXTR a sníží n. Všechny tři přechody invariant zachovávají.

Z toho plyne zákaz předběhnutí ukazatelů na 221: n=N
zablokuje další ASSIGN, protože všechny oblasti patří I/O;
n=0 zablokuje nové I/O, protože žádný blok dosud nebyl
RELEASE. Zařízení nikdy nedostane Y nebo nedokončený G,
výpočet nikdy nedostane R. U vstupu to brání čtení během
přenosu, u výstupu změně právě zapisovaných dat.

Příklad 219 s pěti rychlými požadavky a následným dlouhým
výpočtem vysvětluje další buffery: po zpracování/uchování
pěti bloků lze během dlouhé nezávislé práce anticipovat
další dávku. Čísla pět/šest jsou praktická volba podle
délky držení CURRENT, ne bezpodmínečné globální optimum.
Výpočet může data před RELEASE zkopírovat jinam; nemůže
je současně uvolnit pro vstup a nadále na jejich stabilitu
spoléhat v téže oblasti. Čím dříve je již nepotřebná oblast
RELEASE, tím dříve ji může využít I/O. O tomtéž rozhoduje
rozlišení práce před a po RELEASE v přesných rekurencích níže.

Příklad (5) na 220 používá samostatné výstupní rozhraní
ASSIGNP, které podle komentáře vrátí buffer v I5. ENT1 0,5
zkopíruje adresu do I1 a MOVE 800(24) přenese přesně
0800…0823 do 24 slov tiskového bufferu; index I1 skončí
o 24 výše. RELEASEP smí blok předat až poté. I5 zde není
omylem zaměněno za pozdější CURRENT=I4: jde o dvě výslovně
popsaná rozhraní. Požadavek, aby příkladové adresy nekolidovaly
s vyhrazenými buffery, je obvyklý paměťový kontrakt.

Fig.23 a všechny části Fig.24 byly už přesně odvozeny v X1018,
úloze 8; zde se přebírají včetně poloh všech ukazatelů. Na
vstupu stejné přechody místo vytištění mění načítaný R na G
s hotovou kartou. Fig.27 je podrobně doložena v §4 níže.

## 2. Každý algoritmický krok a každá MIX instrukce

A1 čeká jen při n=N. Je-li čekání potřeba, všechny oblasti
jsou R, takže při pravidelných přechodech do CONTROL existuje
práce pro zařízení; konečný přenos uvolní G. A2 nastaví
CURRENT a A3 postoupí NEXTG. R1 zvýší n právě po skončení
práce s CURRENT. B1 předá práci výpočtu a pokračuje až při
ready. B2 vrátí řízení při n=0, jinak B3 zahájí I/O prvního
R. B4 opět předá řízení a pokračuje až po dokončení. B5/B6
posunou NEXTR, sníží n a vrátí se **přímo k B2**.

Jde o korutiny, nikoli současné nezávislé přepisování registrů.
Výpočet předává řízení pouze přes JRED; CONTROL vrací přes
JMP COMPUTE. A2/A3 a B5/B6 neobsahují takové předání a jsou
tedy vůči druhé korutině atomické. Dokončení zařízení samo
registry/hranice nemění. Tím je vyloučeno pozorování půlky
aktualizace. Přerušovaná varianta v 18 vyžaduje samostatný důkaz.

V Programu A první STJ uloží návrat do 9F. JRED umožní
doběhlé obsluze aktualizovat n; CMP6 =N= a JE opakují A1.
Při n<N LD4 NEXTG vrátí CURRENT, LDX −1,4 načte jeho
link a STX NEXTG jej uloží. Poslední JMP se vrátí na
původní volání. Počet osmi instrukcí je přesný. Běžné
volání může přes JRED provést konečný kus CONTROL, takže
osm slov kódu není automaticky osm časových jednotek.
A mění I4, X, CI, J; případná obsluha také I5/I6.

Program R je vkládaný kód, ne nedoplněný podprogram:
INC6 1 připojí buffer a JRED případně hned obslouží ready.
Hodnota před zvýšením je nejvýše N−1, takže n nepřeteče
dvoubytový index. Mezi INC6 a JRED žádné druhé logické
RELEASE nevzniká. Jsou to přesně dvě instrukce.

Program B má přesně sedm instrukcí: první JMP COMPUTE
je B1; J6Z *−1 jde zpět na tento JMP, pokud n=0. IN
0,5(U) spustí právě NEXTR, druhé JMP je B4. K němu
se řídicí vazba vrátí až při ready; LD5 −1,5 postoupí
linkem, DEC6 1 odečte stále započtený červený blok a JMP
1B znovu testuje n. Pro výstup stačí nahradit IN za OUT.
Původní B používá jen JMP, J6Z, IN/OUT, LD5 a DEC6:
mění I5, I6 a J, ale zachovává A, X, I1…I4, CI i overflow.
Při invariantních hodnotách nedojde k indexovému přetečení.

CONTROL STJ COMPUTEX zachytí návrat z výpočtu. CONTROLX JMP
CONT1 má napoprvé vstup B1; později obsahuje pokračování
uložené COMPUTE STJ CONTROLX před každým návratem. COMPUTEX
JMP COMP1 začíná výpočet a pak obsahuje poslední volající
JRED+1. Obě samomodifikovaná adresní pole leží v soukromém
kódu a mají platné dvoubytové adresy. Z tohoto invariantního
uložení plyne správné střídání B1 a B4, nikoli pouze tvrzení,
že jde o „obvyklou vazbu“.

Počáteční NEXTR=NEXTG může ukazovat na kterýkoli z bufferů.
Vstup má n=N, všechny R čekají na první načtení; výstup n=0,
všechny G čekají na vytvoření dat. CURRENT před první ASSIGN
nemá platnou hodnotu a výpočet jej nepoužije. Právě tato
inicializace, nikoli odlišný barevný algoritmus, rozlišuje
anticipující vstup od výstupu čekajícího na data.

Požadavek vkládat JRED zhruba jednou za 50 instrukcí je
heuristika režie a latence, ne dokázaná optimální perioda.
Správnost a živost potřebují, aby ready obsluha nakonec
dostala řízení. Nezávislá práce mezi ASSIGN/RELEASE musí
skončit, hardware musí dokončovat přenosy a výpočet nesmí
žádat vstup za koncovým blokem. Za těchto podmínek A1 skončí,
každý blok projde cyklem a nekonečné korektní proudy jsou
produktivní. Konečný celý program vyžaduje ještě ukončení
vstupu nebo odvodnění výstupu z úloh 12–13.

## 3. Počet bufferů: přesný obsah tvrzení na 224

Pracujme v ideálním modelu bez instrukční režie a bez speciální
penalizace zařízení. U bloku k označme a_k práci od ASSIGN
do RELEASE a b_k práci od RELEASE do dalšího ASSIGN; obě
jsou nezáporné. C_k=a_k+b_k je nominální procesorová práce
mezi ASSIGN, nikoli čekání A1. T>0 je stálá doba přenosu.

Pro výstup mají nejčasnější časy následující rekurenci:

    A_1=0,
    A_k=max(A_(k−1)+C_(k−1), E_(k−N)),
    R_k=A_k+a_k,
    S_k=max(R_k,E_(k−1)),   E_k=S_k+T.

Neexistující E_i pro i≤0 bereme jako 0. Důvod každého maxima
je přesně dostupnost CPU, znovupoužití stejného bufferu po
N krocích, dostupnost dat a jednoho sériového zařízení. Každá
mez je nutná; algoritmus příslušnou operaci ihned po splnění
všech mezí zahájí, takže rekurence je také postačující.
Odsud indukcí plyne monotónnost ve větším N: termín E_(k−N)
se přesune k dřívějšímu dokončení, zbylé max a součty jsou
monotónní. Přidání bufferů nemůže tento ideální rozvrh zpomalit.

Na vstupu je analogicky S_k=max(E_(k−1),R_(k−N)), E_k=S_k+T,
A_k=max(A_(k−1)+C_(k−1),E_k), R_k=A_k+a_k; počáteční
R_i=0 pro i≤0. Opět jsou to všechny nutné závislosti a
greedy realizace je splní s rovností. RELEASE mají FIFO
pořadí, tedy neklesající časy. Stejná indukce proto dokazuje
monotónnost N i na vstupu. Není to tvrzení, že více paměti
nemůže změnit reálnou implementační režii nebo chování cache.

Pokud všechna C_k>T, dvě oblasti stačí, aby po rozběhu
CPU nečekal. Na vstupu je oblast k uvolněna nejpozději při
A_(k−1), tj. R_(k−2)≤A_(k−1), a přenos k−1 již skončil
před A_(k−1). Přenos k se tedy vejde do dalšího intervalu
C_(k−1)>T. Na výstupu při rozvinutí maxima platí
E_k=max_(i≤k)(R_i+(k−i+1)T). Protože R_i≤A_(i+1) a
každý z k−i+1 následujících CPU intervalů je delší než T,
platí E_k≤A_(k+2) pro nominální nečekající CPU rozvrh.
Právě to vyžaduje opětovné použití dvou bufferů.

Pokud všechna C_k<T, dvě oblasti stačí pro přenosovou
propustnost. Na vstupu po rozběhu k-tý ASSIGN dostane blok
při jeho dokončení a R_k přijde před dokončením k+1, takže
oblast je včas uvolněna pro k+2. Na výstupu před prvním
čekáním ASSIGN běží CPU svou nejvyšší možnou rychlostí;
jakékoli mezery I/O jsou vynuceny dosud nevytvořenými daty
a více bufferů je neodstraní. Při prvním čekání A_k=E_(k−2).
Blok k−1 přitom začne a R_k přijde před jeho dokončením,
protože a_k≤C_k<T. Další nominální ASSIGN přijde rovněž
před E_(k−1), tedy zase čeká právě na uvolnění. Indukcí
je odtud výstup nepřetržitý. Doslovné „at all times“ tím
nepřenášíme na nenaplněný rozběh nebo konečný doběh.

Tvrzení o zmenšení N o jednu při velmi krátkém držení
ASSIGN→RELEASE se týká malé žluté části: pro a_k=0 se
RELEASE stane v okamžiku ASSIGN a jedna z těchto oblastí
může okamžitě sloužit I/O. Pro malé kladné a_k se doba
potenciálního čekání odpovídajícím způsobem zkrátí; „little
effect“ není číselná univerzální mez pro libovolný konečný
program. Průměrná délka shluků plus jedna je také výslovně
„may be right“, ne tvrzená optimalita. Pokud se všechen
vstup uskuteční před jediným výpočtem a všechen výstup až
po něm, právě tyto datové závislosti znemožňují hlavní
překryv CPU/I/O, takže pouhé další buffery tento přínos
neobnoví. Růst rychlosti nemůže být neomezený: CPU práce
a sériová práce zařízení zůstávají dolními mezemi.

## 4. Úlohy 9–11: všechny řádky, ne jen konečné součty

Dosadíme a/b čtyřikrát 1000/1000, čtyřikrát 7000/5000,
potom 1000/1000 a 2000/1000. T=7500. Tabulky níže udávají
pro každý blok všechny čtyři časy A,R,S,E v jednotkách u.
Použitý buffer je 1+((k−1) mod N). Jsou to přímé dosazení
do výše dokázané rekurence; uložený model výsledky doplňuje.

| k | N=1: A,R,S,E | N=2: A,R,S,E |
|---|---|---|
|1|0,1000,1000,8500|0,1000,1000,8500|
|2|8500,9500,9500,17000|2000,3000,8500,16000|
|3|17000,18000,18000,25500|8500,9500,16000,23500|
|4|25500,26500,26500,34000|16000,17000,23500,31000|
|5|34000,41000,41000,48500|23500,30500,31000,38500|
|6|48500,55500,55500,63000|35500,42500,42500,50000|
|7|63000,70000,70000,77500|47500,54500,54500,62000|
|8|77500,84500,84500,92000|59500,66500,66500,74000|
|9|92000,93000,93000,100500|71500,72500,74000,81500|
|10|100500,102500,102500,110000|74000,76000,81500,89000|

| k | N=3: A,R,S,E | N=4: A,R,S,E |
|---|---|---|
|1|0,1000,1000,8500|0,1000,1000,8500|
|2|2000,3000,8500,16000|2000,3000,8500,16000|
|3|4000,5000,16000,23500|4000,5000,16000,23500|
|4|8500,9500,23500,31000|6000,7000,23500,31000|
|5|16000,23000,31000,38500|8500,15500,31000,38500|
|6|28000,35000,38500,46000|20500,27500,38500,46000|
|7|40000,47000,47000,54500|32500,39500,46000,53500|
|8|52000,59000,59000,66500|44500,51500,53500,61000|
|9|64000,65000,66500,74000|56500,57500,61000,68500|
|10|66000,68000,74000,81500|58500,60500,68500,76000|

Každá čekací žádost vzniká v A_(k−1)+C_(k−1), pokud je
menší než příslušné A_k. Dokončení CPU je R_10+1000.
Výstup se zastaví v E_k právě tehdy, když S_(k+1)>E_k,
a definitivně v E_10. Tím tabulky určují také všechny
nevypsané řádky „ASSIGN wait“, „Output stops“ a „Computation
stops“, ne pouze časy nových startů. Současné události
mají stejný čas; logické pořadí v textovém řádku nemění stav.

Pro N=1 čeká CPU v intervalech 2000–8500,10500–17000,
19000–25500,27500–34000,46000–48500,60500–63000,
75000–77500,89500–92000,94000–100500 a po skončení
103500–110000. Celkem 49000; zařízení je nečinné 35000.
Pro N=2 jsou čekání 4000–8500,10500–16000,18000–23500,
73500–74000 a 77000–89000, celkem 28000; zařízení 14000.
Pro N=3 jsou 6000–8500,10500–16000 a 69000–81500,
celkem 20500; zařízení 0–1000,46000–47000,54500–59000,
celkem 6500. To jsou přesně všechny intervaly a součty 227.
Pro N=4 jsou 8000–8500 a 61500–76000, celkem 15000;
zařízení čeká pouze 0–1000, tedy 1000.

Výpočetní práce je 4·2000+4·12000+2000+3000=61000,
přenosy 10·7500=75000. Celkové časy 110000,89000,81500,
76000 souhlasí s odpovědí i se všemi jejími úvodními
sloupci na 533. Každý barevný úsek Fig.27 je nyní dán
intervaly: Y=[A_k,R_k), plný R=[R_k,S_k), šrafovaný
aktivní R=[S_k,E_k), potom G do dalšího použití. Porovnání
všech deseti bloků s obrazem226 dává přesně tři řádky
bufferů, obě mezery zařízení a obě čekání CPU v diagramu.

První výstup nemůže začít před 1000, takže každé řešení
potřebuje nejméně 1000+75000=76000. N=4 tuto mez dosahuje;
monotónnost a dolní mez dokazují tvrzení pro každé N≥4,
nikoli pouze zkoušené hodnoty 5 a 6. Toto je globální
optimum přesného modelu úloh 9–11, na rozdíl od nedoložené
instrukční optimality samostatné úlohy 15.

## 5. Úloha 12: celé ukončení, C0033 a úplná místní oprava

Poslední znak karty je byte5 jejího šestnáctého slova,
tedy 15,5(5:5). Program se sem dostane až po B4, když
JBUS/JRED oznamují ready; nečte probíhající vstup. LDA
3F načte hodnotu ALF se čtyřmi mezerami a tečkou, tedy
kladné číslo40. CMPA je porovná s právě posledním znakem.
STA 2F/LDA 2F správně zachovají A včetně −0. LD5 −1,5
a DEC6 započtou dokončený blok před volbou další činnosti.
Nerovnost pokračuje B2, rovnost přejde na trvalou dvojici
JMP COMPUTE; JMP *−1. Ta při každém dalším volání CONTROL
jen vrací řízení a již nikdy nezahájí IN. Alternativní
JMP COMPUTEX také vrací na uložené místo bez dalšího vstupu.

Právě načtený poslední blok se stane G a výpočet ho může
ještě dostat. U N většího než počet načtených bloků mohou
zůstat další R bez reálných dat; nesmějí být znovu ASSIGN.
To není ztracená koncová karta: výpočet ukončí žádosti na
označené kartě. Obsluha zastaví vstup okamžitě po její
detekci, bez čtení traileru nebo karty za koncem.

Přidané CMPA však mění CI, přestože původní CONTROL CI
zachovává a JRED se vkládá i mezi porovnání a podmíněný
skok výpočtu. Právě to je C0033. Dva buffery a dvě karty
stačí: první prázdná, druhá s tečkou ve sloupci80. Po
ASSIGN první karty je druhý přenos zahájen. Následuje

    JBUS *(16)
    ENTA 0
    CMPA =1=
    JRED CONTROL(16)
    JL SUCCESS

JBUS dokončí druhý přenos a CMPA nastaví less. Původní
CONTROL zpracuje dokončení, nechá CI=less a JL skočí.
Tištěná odpověď zjistí koncovou tečku, vrátí A=0, ale
CI=equal; JL neskočí. n po dvou dokončeních je přesně0.
Není použit neurčený počáteční indikátor, aktivní buffer,
třetí karta ani konflikt paměti. Pro greater obdobně selže
JG; equal se v tomto konkrétním koncovém případu náhodou
zachová. U nekoncové karty je CI výsledek porovnání40 se
znakem, nikoli starý stav výpočtu.

Úplná varianta preserve_ci nejprve STA ASAVE. ENTA −1;
JL SAVECI zachytí less, jinak ENTA 1; JG SAVECI zachytí
greater, jinak ENTA 0 zachytí equal. Tyto příkazy samy CI
nemění; CISAVE je tedy přesně −1/0/+1. Až pak se zkouší
tečka, posune NEXTR a sníží n. JE ENDINPUT nejprve vybere
koncovou větev podle nového testu. Na **obou** větvích
LDA CISAVE; CMPA =0=; LDA ASAVE obnoví CI i celé A.
Nekoncová pak skočí na B2, koncová do návratové dvojice.
Toto pořadí je nutné: obnova CI před JE by zničila test EOF.
Pomocné ENTA/CMPA/LOAD/STORE nepřetékají a overflow ponechají;
I1…I4/X zůstanou zachované, I5/I6/J mají původní řídicí účinek.

Všech 54 starých běhů a162 kontrol bylo přečteno: báze64/100,
tři latence0/17/10000, všechny tři počáteční CI a všechny
tři varianty. Původní a opravená vždy zvolí správnou větev,
tištěná selže ve 12 případech less/greater. Tím se doplňuje
obecný důkaz; znovu se žádný běh nespouští. Všechny čtyři
vrstvy errat byly porovnány také tematicky, včetně TeX
aktuální vrstvy. Oprava 533/14 není opravou 533/12. Stav
C0033 a jeho původní přesná chybná lokace533 se nemění.

## 6. Úlohy 13–14 a známé opravy obrázku a mezí

**13.** Po posledním RELEASE žádné další R nepřibývají.
Smyčka JRED CONTROL(U); J6NZ *−1 pravidelně zpracuje
dokončení, případně zahájí další čekající výstup. Každé
dokončení sníží konečné nezáporné n o1, takže skončí.
Při n=0 už není ani právě aktivní, ani hotový nezapočtený
přenos, protože oba stavy zůstávaly R. Tato CPU bariéra
tedy zaručuje úplné fyzické dokončení, ne pouhé zahájení
posledního OUT. Při počátečním n=0 se po konečné řídicí
vazbě rovnou vrátí; nulový výstup nezpůsobí falešný přenos.

**14.** Po povolení více žlutých je y přesně dosavadní
počet ASSIGN minus RELEASE. Potřebujeme y≥0 a n+y≤N,
tedy y≤N−n. Před dalším ASSIGN musí být nerovnost ostrá.
Původní test n=N tuto silnější podmínku sám nevynucuje;
je to dodatečný kontrakt volajícího nebo doplněný test
n+y=N. U RELEASE se musí vracet nejstarší žlutý, protože
kód připojuje oblast ke konci červeného úseku bez předání
její adresy. Při jiném pořadí už n neurčuje správnou oblast.
Je také třeba uchovat dřívější CURRENT: další ASSIGN jeho
registr přepíše. Za těchto podmínek stejné změny hranic
indukcí zachovají posloupnost R,Y…Y,G a mají smysluplné
použití, například současnou práci se dvěma po sobě jdoucími
bloky bez jejich kopírování. Spotřebují však další oblast.

Pro N=1 a n=0 dá první ASSIGN jedinou oblast, ale druhý
test n<N nepozná, že už je Y, a dá znovu tutéž. Po prvním
RELEASE může I/O pracovat s oblastí, kterou výpočet stále
používá jako druhý CURRENT. Zároveň to přesně porušuje
y≤N−n. Je-li n=1, ASSIGN napřed čeká; proto byla podmínka
n=0 ve známé opravě 28.3.2026 správně připojena. Původní
horní mez y≤N je slabší než nutná y≤N−n právě pro n>0.
Obě změny jsou výslovně v all1 i err1, nikoli nový nález.

Fig.25 na původní223 i jeho náhrada v all1-prepre17 mají
dlouhou šipku z B6 do B2; správnost této hrany se znovu
ověřila v plném rozlišení. Krátká horní šipka z B2 ano
vede do B1. Skutečný rozdíl je **pravý samostatný RELEASE
krok**: původní štítek je „B1. Increase n“, náhrada „R1.
Increase n“. Algoritmus R na222 má rovněž R1. Proto je
zde konkrétní známá chyba označení na223, a dřívější závěr
„samotná existence náhrady není chyba naší šipky“ nelze
rozšířit na „celý obrázek neobsahuje žádnou známou vadu“.
Algoritmické chování se touto opravou štítku nemění.

Odkaz Fig.27 na221 je v naší první edici správný; oprava
z8.5.2019 výslovně platí jen pro dotisky32–40. Žádná změna
čísel tabulek 227/533, kódu původního B ani odpovědi12
nebyla v relevantních vrstvách nalezena. Nový confirmed0,
nová matematická mezera0; global-optimum mezera15 zX1018
zůstává. Přesná nová mapa v žádném případě nezavírá dosud
nezrevidované 16–19 ani zbývající hlavní text224–225.

## 7. Přesný rozsah přijatých kontrol

Událostní output_schedule implementuje přímo změny barev
a nejčasnější dokončení, nikoli přepsanou tabulku odpovědí.
Všechna původní data227, všechny tři částečné sloupce533,
celé rozvrhy N=1…6 a idle součty se kontrolují odděleně.
Čtyři sta třicet dva skutečných MIX běhů navíc ověřují
N=1/2/3/5, 1/2/7 bloků, báze64/100, latence0/19/211,
tři rozdělení práce před/po RELEASE a oba směry I/O.
Každé ASSIGN kontroluje konkrétní pointer a hotová vstupní
data; každé RELEASE kontroluje obsah výstupní oblasti.
Konec kontroluje počet přidělení, celé data, absence další
karty po markeru i n=0 a prázdné zařízení po výstupu.
Celkem4252 kontrol. Ideální časový diagram a skutečné MIX
časy se v žádném kroku nezaměňují; čekání na JBUS zkracuje
jen již prokázaná ekvivalentní optimalizace simulátoru.
