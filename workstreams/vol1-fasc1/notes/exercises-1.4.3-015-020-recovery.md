# MMIX — úplný rozsah odpovědí1.4.3′–15 až20

## 15. Fputs a všechny společné vstupy

Přebírá se opravený MemFind invariant: každý node obsahuje
4096bytů DATA a8nulových padding bytů. Na vstupu je virtuální
pointer A=t, ukončený řetězec délkyN, všechny jeho adresy včetně
NUL jsou nepřivilegované a potřebné nodes se vejdou do deklarované
areny. Proto 0≤N≤2^63−A−1<2^63. Toto konkrétně zajišťuje,
že signed ADDxx akumulující počet nemůže přetéct.

Invariant každého průchodu: xx je počet již vypsaných bytů,
z=A+xx je první dosud nevypsaný virtuální znak. MemFind převádí
právě tuto adresu, bez změny DATA. Host Fputs může přečíst
nejvýše zbývající kus DATA plus první padding nulu. Při úspěchu
t je přesná délka tohoto kusu. Je-li t0, skončíme; jeho nula
musí být skutečný první byte aktuálního virtuálního kusu.
Je-li t>0, xx a z narostou o t. Adresa z uvnitř chunku
označuje skutečný NUL, takže skončíme; je-li na jeho hranici,
projde se další chunk a odliší pokračování od skutečného NUL.
Při libovolné chybě t<0 se vrací−1, jak požaduje Fputs,
bez tvrzení, že již vypsaný prefix lze vrátit zpět.

Každý úspěšný průchod kromě případného posledního spotřebuje
kladný počet znaků. KonečnéN tedy zaručuje konec. PřípadN0,
NUL přímo na hranici i řetězec začínající na posledním byte
chunku jsou zahrnuty. NUL ani padding se nikdy nevypisuje.

DoInst dostává originální32bit TRAP v inst a hostitelský
návratový link v$0; PUT rW,$0 a PUT rX,inst následované
RESUME0 vloží právě tuto instrukci a vrátí se na link.
Pracovní xx/yy/zz se nepoužijí místo jejích skutečných bytů.
SimInst nastaví t=&IOArgs a vrací volajícímu; SimFinish
nastaví totéž a přejde do SimFclose, které nahradí link
zaTrapDone. Samotné SimFclose/Fseek/Ftell zachovají vstupní
t i opcode/handle. Hostitelský service-contract se přebírá;
oddělené vady dodávaného I/O programu S0005–S0008 tím nemizí.

Cena zde i níže znamená nominální μ/υ bez času uvnitř OS;
jednotlivý vložený TRAP má5υ. Nechť M_i je již uzavřená
úplná cena i-tého MemFind včetně jeho POP, bez volajícího
PUSHJ. Jeden pozitivní průchod Fputs stojí M_i+26υ,
včetně buď dalšího skoku, nebo závěrečnéhoSET/JMP. Vstup
má2υ. Pro k pozitivních průchodů je tedy celkemΣM_i+(26k+2)υ;
jestliže posledník-tý průchod vrátí0, je toΣM_i+26kυ;
při chybě v poslednímk-tém průchoduΣM_i+(26k−3)υ.
SpolečnéTrapDone není zahrnuto. Rozklad18υ před kontrolou
výsledku obsahuje SETarg/PUSHJ/SETt/GO aDoInst s vloženýmTRAP;
po něm stojí pozitivní cesta8υ, nulová6υ a chybová3υ.

## 16. GetArgs a filename: platný invariant, skutečná prostorová mez

GetArgs čte dva octabyty argumentů přes nezávislé MemFind.
I při přechodu chunku je to správné. LDOU zarovnává na8;
proto oba argumenty z t a t+8 zůstávají správně sousední i
pro nevyrovnaný základ. z je virtuální první argument,
x jeho fyzický pointer, y původní virtuální$255, zz druhá
hodnota. IOArgs dostane(x,zz). Počet do konce chunku musí
být4096−(z&4095), nikoli4096−(x&4095): přebírá se C0008.
Fopen tento počet nevyužívá. Ochrana návratu v lokálním$0,
nestedPUSHJres a závěrečnéPUT rJ/POP jsou podle přijatého
stack invariantu korektní. Celá cena GetArgs je
4μ+20υ+M_1+M_2+M_3, včetně jeho POP, bez vstupníhoPUSHJ.

Označme a původní Mem:alloc, b=a+4120 a d délku filename
bezNUL. Dočasná kopie začíná na b, za jedním rezervním node.
Dokud má virtuální řetězec nenulové byty, leží v již
existujících nodes; první nový node má DATA nulová, a proto
právě tam kopírování skončí. Během celé kopie se tedy může
přidělit nejvýše jeden node, který končí na b. Úpravy LINK
existujících nodes jejich DATA ani fyzické adresy nemění.

Po j průchodech je z=A+j, x=b+j a prvních j bytů kopie
souhlasí s virtuálním řetězcem. LDBU/STBU kopírují iNUL,
proto j=d+1=m. Host Fopen dostane přesnou souvislou kopii.
Mode i handle se nezmění. Návrat t se během úklidu nemění,
takže se vrátí přesně úspěch či chyba hostitelského Fopen.

Úklid začíná v x=b+m a nulujícíSTCO vždy zaokrouhlí x
dolů na8. NáslednýCMP porovnává s původním b, SUB odečte8
a PBN opakuje. Po c=ceil(m/8)+1 krocích je poslední
nulovaný octabyte na b (m dělitelné8) nebo b−8 (jinak).
Všechny byty kopie jsou vymazané. Případný b−8 je padding
rezervního node, který podle MemFind musí být nula.
Vzdálenější předchozí DATA se nikdy nevymažou.

**Dříve nevypsaný předpoklad není automaticky dokázaný:**
kopie i úklid potřebují souvislou volnou hostitelskou oblast
až do b+8*(floor(m/8)+1), nikoli jen místo na jeden další node.
Dostatečná přesná podmínka v deklarované data areně je

`b+8*(floor((d+1)/8)+1) ≤ Pool_Segment`.

Při ní jsou všechny adresy, signedSUB a dočasné operace
bezpečné; po úklidu je obnovena nulovost budoucích nodes.
Ale samotná přípustnost dlouhého virtuálního filename ani
kapacitní výpočet úlohy4 tuto dodatečnou podmínku nezaručují.
Není zde kontrola délky či mezí scratch prostoru. Není proto
poctivé zachovat staré bezpodmínečné argument_recorded.
E16 je partial jen pro tuto přesnou prostorovou povinnost:
doplnit bounded scratch/streaming řešení nebo doložit
přípustnou délkovou mez a prostorový kontrakt z primárního
OS modelu. Neprohlašujeme nový confirmed nález a nic obrovského
nealokujeme. Běžná konečná kopírovací/úklidová logika je uzavřená.

Při uvedeném dostatečném předpokladu je úplná cena, mimo
TrapDone a OS, GetArgs+(1+2m+c)μ+(7m+4c+26)υ+ΣM_i,
kde M_i patří m byte-copy překladům. Kopie má m−1 vzatých
PBNZ a jeden nevzatý, úklid c−1 vzatýchPBN a jeden nevzatý;
oba poslední skoky přidávají po2υ. Výpočet zahrnuje i host
Fopen a úklid po neúspěšném otevření.

## 17. Všechny chunk větve a rozdíl Fread/Fwrite

Po opravě C0008 označme N velikost požadavku, C4096 a
c0=C−(A modC). Pro0≤N<2^63 a platnou nepřivilegovanou
adresní oblast platí invariant: y je celkový zbytek, z jeho
první virtuální adresa, IOArgs ukazuje na její fyzický překlad,
xx je kapacita aktuálního chunku. Jsou to kladná malá xx≤4096.

Pokud y≤xx, závěrečnéSimFinish žádá celý zbytek. Jinak
host dostane přesněxx bytů a y se nejprve sníží oxx.
Při úspěchu se z zvětší oxx, novýMemFind přeloží následující
chunk a IOArgs se obnoví na celý zbývající y. xx se nastavíC.
Každý tento průchod spotřebuje kladnéxx, takže skončí.
N0, přesněc0, přesněc0+C a poslední neplný blok jsou zahrnuté.

Při krátkém přenosu n<xx je host výsledek n−xx. Odečtení
zbývajícího y vrátí n−xx−y, tedy skutečný deficit celého
původního požadavku, nezávisle na již úspěšných kusech.
Závěrečný kus už žádá celý zbytek, takže jeho deficit se
předá přímo. Toto je správně pro všechny krátké Fread iFwrite.

Pouze Fread má navíc zvláštní serious-error hodnotu−1−size.
Je-li chyba v prvním vnitřním kusu,−1−xx−y=−1−N, správně.
Pozdější serious-error by potřebovala původníN; kniha její
výskyt po prvním úspěšném Fread **výslovně vylučuje**.
Také závěrečný serious-error po dřívějších kusech spadá pod
tento explicitní předpoklad. Fwrite žádný takový sentinel
nemá: jeho kontrakt vrací vždy n−size. Předpoklad o čtení
tedy není nedopatřením aplikovaný na zápis a nevzniká z něj
nový Fwrite nález. Samostatný S0005 je chyba hostitelského
programu, nikoli tohoto algebraického skládání deficitů.

Starý důkaz ale mlčky omezil N<2^63. Při horním bituN
vyhodnotí signedCMP malé kladnéxx jako≥y a rovnou předá
celý rozsah jediným fyzickým pointerem, což chunk překlad
obecně neprovádí. Přípustnost takových požadavků patří
do již otevřeného R0007; není zde automaticky rozhodnuta
faktem, že případ vyžaduje obrovské množství dat. Stejně
musí být přesně řečen platný buffer i proN0, protože
GetArgs jej překládá před samotným I/O. E17 proto znovu
partial pro konkrétní doménu počtu/bufferu, nikoli pro
již prokázané obyčejné chunk větve.

Pro úspěch je q=1 pokudN≤c0, jinak1+ceil((N−c0)/C).
M_i nyní označuje jen přechody po úspěšných vnitřních kusech.
Celková nominální cena je

`GetArgs + ΣM_i + 3(q−1)μ + (31q−13)υ`.

Úvod stojí2υ, každý nefinální úspěch3μ+31υ+M_i,
posledníSimFinish16υ. Chyba v nefinálnímj-tém kusu stojí

`GetArgs + Σ_{i<j}M_i + (3j−2)μ + (31j−1)υ`.

Poslední chybová větev má1μ+28υ včetně opravy deficitu.
Náklady končí předTrapDone; neodvozují rychlost OS ani
správnost chybných dodávaných C služeb.

## 18–20. Přesné převzetí celých již uzavřených argumentů

18: `exercises-1.4.3-015-022.md` dokazuje každou fázi ringu
pro mocninu dvouρ a architektonickéL≤ρ−1, včetně markeru,
PUSH/POP a validníhoUNSAVE. Novýbootstrap nemusí býtL2;
musí sám splnit tutéžpodmínku. Nejde o tvrzení pro libovolná
ρ bez bitové podmínky ani pro program, který ji později poruší.
Konkretizaceρ32 je proto správná.

19: stejná poznámka dává konkrétníGrowLocal se všemi třemi
argumenty:0 pro marginal destination, původníL proglobalPUSH
aSAVE. Zápis proběhne na staréβ předINCL, StackRoom se
nezmění; globalPUSH přeskočí svoje druhé uložení markeru.
Tím je doložen skutečný refactoring, nikoli jen shoda tří
výřezů. Netvrdí se rychlostní optimum. ZnáméXOR→AND2005
je převzatá publikovaná oprava.

20: celá starší indukce loaderu se přebírá včetněl0,
nonzero-only dat, terminátorů, skupin aEOF. Doplnění rozsahu:
každá další skupina smí překrýt dřívější data, potom poslední
zápis vyhraje podle pořadí. λ nemusí být zarovnané;
M8[λ+8k] se vždy zarovná stejně jako jeho hostSTOU přes
MemFind. loc sleduje formální nezarovnanou adresu, takže
závěrečnéλ+8(l−1) souhlasí i tehdy. Platný spustitelný
obraz ovšem končí skutečným nonzero packed-header word;
samotná syntaxe souboru nestačí na validníSAVE obraz.

Na EOF po poslední nulové skupinové značce zůstává loc
nezměněné; Fread do g[255] aniFclose tento pracovníglobál
nemění. JedinéSUBUloc8 tedy dává požadovaný výsledek.
EOF či serious error uvnitř platně rozečtené skupiny vede
Error. Rozlišování vadného polovičního headeru odEOF je
mimo výslovně zadaný souborový formát, ne otevřená úloha.
Pro všechny platné vstupy platí invariant vnitřní smyčky,
bez nového běhu starého loaderu.

## Výsledek obnovy

E15/18/19/20 mají celý argument převzatý či doplněný. E16
aE17 se oproti starému checked znovuotevírají pro přesné
resource/domain povinnosti, které předchozí krátký důkaz
opomněl. Bibliografická existence pomocnýchFgets/Fgetws/Fputws
v autorověsim.mms byla ověřena čtením příslušných labelů;
jejich celý další implementační audit tím netvrdíme.

Žádný nový build, simulace, dlouhý I/O vstup ani opakovaný
C0008/S0005 případ. Vzory1/4B jsou použity na všechny
větevní/vstupní meze, explicitní volnou paměť, samostatné
deficitové a sentinelové smlouvy a úplné nominální ceny.
