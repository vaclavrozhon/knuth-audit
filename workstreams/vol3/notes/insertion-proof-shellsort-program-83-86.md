# Shellsort: celý algoritmus, MIX, tabulky a úlohy8–10/43

Původní83–86/file94–97, úlohy102/105 a odpovědi619–620/627
zobrazeny. Všech pět vrstev je v
`sources/insertion-errata-review.json`. Dříve úspěšně
zkontrolované stavy a B,C tabulek se přebírají z
`results/insertion-targeted-checks.json`, bez nového běhu.
Známé přeznačení lokálních značek odpovědi10 z2001
a doplnění43 z2001 jsou zohledněny. C0010 se pouze
přebírá ve svém již doloženém rozsahu.

## P0712: AlgorithmD, invariant každé třídy a všechny meze

Inkrementy jsou kladná celá čísla, t≥1 a h₀=1.
Pro pevné h tvoří pozice r,r+h,…, r=1,…,h,
disjunktní podposloupnosti. Při zpracování j jsou
všechny dříve navštívené pozice jeho třídy seřazené.
Kroky D3–D6 jsou přesně invariant s dírou P0685
po přejmenování indexu na pořadí uvnitř této třídy.
Přesouvají se pouze klíče>K, ostatní třídy se nezmění.
Interleaving různých tříd podle j tedy žádnou indukci
nenarušuje. Na konci průchodu je každá třída seřazena,
ekvivalentně K_i≤K_(i+h) pro1≤i≤N−h.

Zvlášť důležitý okraj: poslední i nemusí být0, ale
může být libovolné1−h,…,0. Tehdy i+h je nejmenší
kladná pozice r dané třídy a právě tam se R vloží.
Žádný nekladný index se v D4 nečte. Vnitřní index
klesá o kladné h a vnější j roste, takže vše skončí.
Poslední průchod h₀=1 zaručuje úplné setřídění.
Klesání inkrementů není potřebné pro **správnost**;
opakované nebo libovolně řazené kladné kroky jsou
také platné. Pro t=1 je abstraktní algoritmus právě S.

Při h≥N je abstraktní D2 prázdný, stejně jako u
N=0/1 s h₀=1. MIX program však výslovně předpokládá
všechny h<N, tedy N≥2; nemá se bez úpravy použít
na prázdný průchod. Paměť dat je původní pole plus
jeden pomocný záznam, tabulka t inkrementů a indexy.

## P0713: všechny tři samomodifikace a všechny instrukce

ENT3 T−1 a následné DEC3/J3NN projdou právě s=T−1,…,0.
LD4 načte h_s. ENT1 INPUT,4 nastaví INPUT+h a dvě
ST1 s polem0:2 mění **jen** znaménko/adresu instrukcí
STX a STA; jejich index2 a opcode zůstanou zachovány.
ENN1 −N,4 dává−(−N+h)=N−h a další ST1 přepíše
adresovou část ENT2. ENT1 1−N,4 pak nastaví j−N
pro první j=h+1.

LDA INPUT+N,1 načte R_j. Upravená ENT2 N−h,1 dává
i=j−h. CMPA/JGE je D4; LDX/STX přenesou celé R_i
na INPUT+i+h; DEC2 0,4 sníží i právě o h.
J2P opakuje jen s kladným i, jinak upravené STA
uloží R na platné i+h. INC1/J1NP projdou až j=N
včetně. Po přechodu na další h se všechny tři
adresy přepíší znovu z původních konstant, takže
se chyby ani posuny předchozího průchodu nekumulují.
Vše předpokládá platné disjunktní oblasti kódu/tabulky/dat
a reprezentovatelné adresy/indexy, jako jiné MIX programy.

## P0714: každý počet a celý nákladový vzorec

Polož M=∑(N−h_s)=NT−S. To je přesný počet vkládání.
B je součet inverzí **v aktuálních podposloupnostech
na začátku jednotlivých průchodů**, nikoli nutně
počet inverzí původního celého pole. A počítá dosažení
nekladného i: nová striktní minima v každé zpracovávané
třídě, bez jejího prvního prvku. Stejný argument jako
P0687 dává počet porovnání B+M−A.

Inicializace stojí1. Sedm instrukcí setupu každého h
stojí2+1+2+2+1+2+1=11, závěr průchodu2; tedy13T.
Setup/závěr každého vložení stojí7M, CMPA/JGE
3(B+M−A), čtyři instrukce přesunu6B. Celkem

    T_D=1+13T+7M+3(B+M−A)+6B
       =9B+10NT−10S−3A+13T+1.

Tím jsou ověřeny všechny vytištěné četnosti a významy
pěti faktorů v úvodu86. Pro jeden průchod h=1 je
algoritmus S, ale obecnější program stojí o13u více
než ProgramS: ekvivalence algoritmů není ekvivalence
jejich konstantní režie.

## P0715: obě celé tabulky a nově doložené počty A

Všechny čtyři výstupní řádky obou tabulek a jejich
B,C přebíráme z uvedeného uloženého výsledku.
Oblouky obrázků spojují vždy i s i+h; je jich N−h,
tedy pro Table3 postupně8,12,14,15 a pro Table4
9,11,13,15. Každá takto propojená třída je ve
výstupním řádku seřazena. Úvodní popis83 přesně
odpovídá osmi párům pro h=8, čtyřem čtveřicím pro4
a dvěma osmicím pro2;512/154 se vymění a908/897 jdou doprava.

Nově je třeba doložit počty konců na prvním místě třídy:

- Table3: h=8, j=11,13,15 jsou minima svých dvouprvkových
  tříd ⇒A=3. Při h=4 jediné posunuté512 přeskočí765,
  ale zastaví se nad154 ⇒A=0. Při h=2 mají154 na j=3
  a61 na j=4 nové minimum; posunuté512 a897 je nemají
  ⇒A=2. Poslední h=1 má jen nové minimum61 ⇒A=1.
- Table4: h=7 všechny čtyři posuny na j=8,10,12,14
  dosáhnou prvního místa ⇒A=4. Při h=5 se170 a pak154
  stanou minimy první třídy ⇒A=2. Při h=3 jsou novými
  minimy61 na j=4 a170 na j=6, ostatní přesuny skončí
  nad dřívějším minimem ⇒A=2. Před posledním h=1
  je61 už prvním prvkem ⇒A=0.

Součty jsou A=6,B=3+1+4+21=29 pro Table3 a
A=8,B=4+3+8+10=25 pro Table4. Neopakoval se žádný
starý test; doplněn je právě chybějící argument pro A.

## P0716: úloha8, skutečná nestabilita

Vezmi tři označené záznamy(2,1A,1B) a h=2,1.
První průchod vymění2 s1B, takže vznikne(1B,1A,2).
Druhý průchod má shodné1 již v tomto pořadí a jeho
stabilní vnitřní vkládání je nepřekříží. Výstup tedy
obrací1A/1B. Stejný mechanismus vysvětluje vytištěný
delší vstup2,1,…,1: první h>1 přenese první1 ze své
třídy před mezilehlé stejné klíče. Stabilita jednotlivé
třídy nezaručuje stabilitu celého Shellsortu. Pro
zvláštní jediný krok h=1 je samozřejmě S stabilní.

## P0717: úloha9, oba časy a konkrétní dvouprůchodová alternativa

Table3 má T=4,S=15,M=49, takže
9·29+10·49−3·6+13·4+1=786u.
Table4 má T=4,S=16,M=48, takže
9·25+10·48−3·8+13·4+1=734u.
Převzatý čas ProgramS je514u. Oba konkrétní Shellsorty
jsou tedy navzdory menším B pomalejší kvůli režii.

Tvrzení o vhodnějších dvou průchodech lze pro tato
data podložit i bez průměrového modelu. Zvol4,1.
Při h=4 mají čtyři původní třídy počty inverzí3,0,3,0
a jediné nové minimum154, tedy B=6,A=1. Výsledek
je shodný s již uloženým řádkem4-sort v Table3:
první8-sort působí pouze uvnitř stejných4-tříd,
jejich konečné setřídění se tím nemůže změnit.

Pro finální1-sort tohoto řádku jsou počty větších
předchůdců0,1,1,3,0,2,1,3,0,4,0,4,0,2,1,3,
se součtem25; nová minima jsou87 a61, tedy A=2.
Celkem B=31,A=3,T=2,S=5,M=27 a čas
279+270−9+26+1=567u. To je méně než obě čtyřprůchodové
varianty, ale stále více než514u. Netvrdí se, že2
průchody porazí S na každém jednotlivém16prvkovém vstupu.

## P0718: dosud otevřený průměrový crossover z úlohy9

Navazující „about N=13“ se týká průměrného chování,
nikoli právě vypočteného příkladu. Jeho samostatné
ověření vyžaduje přesnou funkci f(N,h), cenu A pro
oba průchody a volbu h. To se zde nepředjímá z příkladů.
Položka zůstává partial do následujícího analytického
bloku TheoremH; není to tvrzení chyby ani důvod k enumeraci.

## P0719: úloha10, aktuální lokální značky a celý tok řízení

Použije se oprava z8.3.2001: první nová CMPA má0H,
její přeskočení vede na původní7H (INC1), ENT2 má3H,
LDX4H, STX5H a STA6H. Nově vložená setupová ST1
proto míří na0F, zatímco stará ST1 stále na3F.
Tím se správně oddělují dvě různé adresy:

    ENT2 dostane N−h;
    první CMPA dostane INPUT+N−h.

Dosáhne se toho po staré ST1 instrukcemi
INC1 INPUT; ST1 0F(0:2), ještě před obnovením j−N.
Staré dvě ST1 s INPUT+h zůstávají správně navázány
na STX/STA. Známé původní chybné lokální značky nejsou
novým nálezem.

První CMPA načte K_(j−h) přímo z relativního j−N.
Při K≥K_(j−h) je zpracovaná třída už správně rozšířená:
lze přeskočit ENT2 i zápis R_j na sebe. Jinak první
posun určitě nastane. LDX/STX/DEC2 jsou jako dříve;
J2NP jde při nekladném i na STA, jinak se porovná
další klíč a JL pokračuje jen při K<K_i. Celý
invariant P0712 se zachová v obou větvích, včetně rovnosti.

## P0720: úloha10, všechny četnosti a převzetí C0010

Označ C počet prvních porovnání s K_j≥K_(j−h).
Nový první CMPA/JGE má četnost M, ENT2 a STA mají
M−C. Přesunové instrukce mají B; po přesunu se
další CMPA/JL provede B−A krát. Celkový počet
porovnání i cenově stejných skoků zůstává M+B−A,
a všechny datové přesuny se také zachovají.

Odpadne C instrukcí ENT2 za1u a C instrukcí STA za2u;
přibudou INC1/ST1 za3u na každý průchod. Čistá úspora
je přesně3(C−T). Počet řádek roste o4: dvě setupové
a dvě v přeuspořádaném těle. Z dříve doložených
C=33 a29 pro tabulky tedy vychází87 a75u.
Chybné vytištěné88 je již uzavřený C0010 v
`notes/V3-C0010-shellsort-time-saving.md`; tento
blok jej znovu nehledá, nezapočítává ani nepřepočítává testem.

## P0721: proč je obdobná úprava S jen logaritmická v průměru

Pro jediný běžný průchod se prvotní porovnání obejde
bez přesunu právě tehdy, je-li nový klíč maximem
dosavadního prefixu (při různých klíčích). Pravděpodobnost
je1/j, tedy E C=H_N−1. Analogické přeuspořádání
programu S ušetří konstantní cenu ENT2/STA v těchto
C případech, nejvýše s konstantním setupem, a proto
O(log N) očekávaných jednotek. U známého setříděného
vstupu je naopak C=N−1. To dokládá současné znění2013
bez neplatného univerzálního zákazu této optimalizace.

## P0722: úloha43, úplné odstranění testu hranice z hledací smyčky

Nejlevější pozice aktuální třídy je
l=1+((j−1) mod h). Pro j=h+1 je l=1; aktualizace
l←l+1−h[l=h] přesně cykluje1,…,h, jak tvrdí odpověď.
Z invarianty třídy je K_l minimum všech předchůdců j
v této třídě. Po D3 se nejprve zvlášť porovná K s K_l.

Je-li K<K_l, jsou **všechny** tyto klíče větší.
Lze proto bez dalších porovnání klíčů posunout
R_l,R_(l+h),…,R_(j−h) o jedno místo v jejich třídě
doprava (kopírujeme od konce) a zapsat R do l.
Přesný počet kopií je(j−l)/h. Hranice této předem
známé kopírovací smyčky není neznámá hledací podmínka.

Jinak K≥K_l a původní porovnávací smyčka musí
zastavit nejpozději na i=l; po žádném provedeném
přesunu proto nemůže být nutné číst nekladné i.
V této větvi je tedy bezpečné odstranit test i>0
z D5 a vracet se přímo na D4. Rovnost s minimem
je zahrnuta právě v této větvi. Nevytváří se falešný
společný sentinel R₀ pro všechny zbytkové třídy.

## P0723: výslovně oddělená empirická doporučení

Poměry C/(NT−S) přibližně0.4 a0.3 pro určité poměry
inkrementů jsou v knize označeny jako empirické.
Není zadána úplná sekvence, konečný N ani přesný
limitní režim, z nichž by šlo odvodit univerzální číslo.
Zde se nereprodukuje rozsáhlé měření ani se čísla
nevydávají za větu. Stejně zůstává vymezeným empirickým
dodatkem varování2001 u43, že při dobrých inkrementech
malý počet vnitřních průchodů nevyváží další režii.
Přesná správnost obou úprav a vzorec3(C−T) jsou
nezávisle uzavřené; tato srovnávací doporučení jsou partial.

## P0724: explicitní otevřená optimalizační otázka

Odstavec85 výslovně neudává nejlepší obecnou sekvenci
inkrementů pro velká N. Tento blok řeší správnost
a přesné ceny zadané sekvence, nikoli globální optimum
mezi všemi sekvencemi. Otevřená otázka se nepovyšuje
na vyřešenou a netvrdí se bez současné rešerše její
vědecký stav k2026. Žádný nový nález z tohoto odstavce
neplyne. Historické autorství Shell1959 a Thimbleby1989
zůstávají bibliografickými výjimkami.

Další argumentový kurzor:86/file97, rovnoměrná2-ordering
a celá lattice analýza s úlohami11–15. P0718 se vrátí
po dokázání TheoremH; P0723/P0724 jsou přesně vymezené
empirické/výzkumné meze, ne chyby algoritmu.
