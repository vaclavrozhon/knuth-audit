# §1.3.2′–34 — všechny řídicí stavy a přesné zbývající podmínky

Zadání file58/p50, celý program file119–121/p111–113. Všechny původní
stránky jsou v images; nové120/121 byly zobrazeny při rozboru. Známou
opravu z15.3.2024 `MUL delay,rho,18`→`MUL delta,rho,18` uplatňujeme
před jakýmkoli závěrem. Zacyklení Delay je samostatný potvrzený
`MMIX-C0020-delay-reset-loop.md`; tato poznámka netvrdí jeho opravu.

## 1. Všechny bajty a paměťové předpoklady

Čtyři pole mají disjunktní bity: D vozidla7…6, B vozidla5…4,
D chodci3…2, B chodci1…0. Proto součet i OR předepsaných kódů
souhlasí a nemá přenos mezi poli. Všechny čtyři řetězce každé báze
mají jeden nenulový příkazový bajt a výslovný nulový terminátor:

| báze, offset | bajt | D vozidla/chodci | B vozidla/chodci |
|---|---|---|---|
| Boulevard,0 | #67 | zelená/WALK | červená/DON'T WALK |
| Boulevard,2 | #6f | zelená/DON'T WALK | červená/DON'T WALK |
| Boulevard,4 | #63 | zelená/vypnuto | červená/DON'T WALK |
| Boulevard,6 | #ef | oranžová/DON'T WALK | červená/DON'T WALK |
| Avenue,0 | #9d | červená/DON'T WALK | zelená/WALK |
| Avenue,2 | #9f | červená/DON'T WALK | zelená/DON'T WALK |
| Avenue,4 | #9c | červená/DON'T WALK | zelená/vypnuto |
| Avenue,6 | #bf | červená/DON'T WALK | oranžová/DON'T WALK |

Žádný Fputs tedy neskončí před samotným příkazovým bajtem a žádný
nevypíše dva příkazy. Adresy offsetů0/2/4/6 jsou správné; bází green
je vždy začátek právě jednoho z těchto dvou polí. V každém předepsaném
stavu má kolmé rameno červenou a oba chodci při oranžové/červené
DON'T WALK. Vypnutí při blikání patří pouze odpovídajícímu chodci.

Oba názvy zařízení jsou nulově zakončené. Fopen dostane adresy dvojic
jméno,BinaryWrite nebo jméno,BinaryRead, handly3/4. Read_Sensor obsahuje
právě Sensor_Buf a délku1. OCTA deklarace jsou zarovnané podle MMIXAL;
datový Sensor_Buf=Data_Segment se nepřekrývá s kódem/názvy od#100.
GREG@ pro kód umožní assembleru adresovat Delay/Flash přes jeho bázi;
GREG pro Sensor_Buf obdobně adresuje LDB. Zápis Fread mění jen jediný
bajt bufferu. Ostatní programová data jsou neměnné příkazové řetězce.

Zadání určuje abstraktní připojení dvou zařízení, ne běžné konečné
soubory. Důkaz použitelnosti I/O proto předpokládá úspěšná otevření,
úspěšný přenos jednoho bajtu na každý read a synchronně dokončené
příkazy Fputs; stav zařízení vydrží do dalšího příkazu. Fread vrací
latched nonzero právě pro události od předchozího read. Kód netestuje
chyby systému a při selhání čtení by mohl číst starý bajt; na takový
stav se původní normativní model zařízení nevztahuje. Nezakládá se
nový nález jen z hypotetického neúspěšného otevření `/dev/lights`.

## 2. Celý Flash a volací registry

Každý call `GO flash_go,Flash` uloží skutečný návrat. Flash jej drží
v samostatném GREG; své volání Delay ukládá do jiného delay_go.
Delay mění pouze t,delta,ref_time,delay_go, takže zachová n,green
i flash_go. Pracovní GREG0 jsou odlišné; jde o nereentrantní rutiny
se standardním zachováním registrů při obsluze přerušení.

Na začátku Flash je n8 a green určuje správné rameno. Jedno kolo
vypíše offset2, počká floor(ρ/2), vypíše offset4, počká floor(ρ/2)
a sníží n. Před j-tým kolem n=9−j; PBP se vrací právě pro j<8.
Všech osm dvojic tedy nastane jednou, v pořadí DON'T WALK/off.
Potom offset2 zapne trvale DON'T WALK, prodleva je4ρ a offset6
přepne příslušná vozidla na oranžovou. GO flash_go,flash_go,0
použije starou cílovou adresu před uložením nového nepoužitého linku.

Součet požadovaných prodlev je16floor(ρ/2)+4ρ=12ρ−8[ρ liché].
To je celý důvod osmivteřinového blikání a následných čtyř sekund,
včetně přesné osmítaktové odchylky při lichémρ. Není zde tvrzení,
že každý libovolný fyzický interrupt má nulovou latenci.

Bez samotných těl17 volání Delay má Flash přesně207υ:
SET n1; osm kol po22υ a poslední chybná predikce navíc2;
závěrečné nastavení/4ρ/call19υ; oranžová a návrat9υ.
V této programové části nejsou datové load/store instrukce. Fputs
vnějšího zařízení má nominální cenu TRAP5υ; jeho hostitelské čtení
řetězce není do programových mem zahrnuto, stejně jako v tabulce knihy.

## 3. Hlavní řídicí stav, prodlevy a sensor

Main otevře oba handly a JMP2F začne zelenou D. Po opraveném
MUL delta,rho,18 následuje prodleva18ρ a Wait. Pokud sensor dává0,
Wait nevyšle žádný nový příkaz a D zůstane zelená libovolně dlouho.
Jeden prázdný průchod GETA/TRAP/LDB/BZ stojíμ+10υ; při nenulovém
bajtu je průchod k GETA green kratší o2υ. LDB může dát zápornou
hodnotu u bajtu≥128, ale BZ ji správně považuje za nonzero.

Nenulový sensor začne Flash pro D, potom osm sekund D oranžové.
Následuje Avenue0, osm sekund B zelené/WALK, Flash pro B a pět
sekund B oranžové. Potom se vrací Boulevard0 a celé schéma se opakuje.
Bez dodatečného čekání a bez režie jsou po sobě hranice0,18,30,38,46,
58,63 sekund. D zelená trvá nejméně30 sekund plus Wait, B zelená20;
oranžové intervaly jsou8 a5. Skutečné režie a lichéρ jsou oddělené.

Při D zelené, jejím blikání a oranžové se požadavky na B nevyhazují
před jeho následující zelenou. B je během celé této doby červená.
Na B zelené už mohou obsloužené požadavky zůstat v latchi, proto je
po jeho Flash ještě jeden Fread bez testu. Další Wait po D startu
opět řeší pouze do té doby nevymazané požadavky.

**Přesná otevřená hrana:** poslední Fputs uvnitř Flash už aktivoval
B oranžovou; až po GO návratu a GETA provede Main ignorovaný Fread.
Aktivace sensoru v tomto krátkém skutečném oranžovém intervalu se tedy
spotřebuje. Pokud žádná další aktivace nenastane, následný Wait může
vracet0 navždy a další požadovaný B cyklus nepřijde. Doslovné zadání
žádá pro amber/red události nový cyklus. Knižní dovětek o „few hundredυ“
může zamýšlet toleranci klasifikace vstupů u přechodu; její přesný
význam není určen. Malá šířka okna sama neomezuje výsledné zpoždění.
Proto tuto interpretaci nepovyšujeme na checked ani na nový confirmed;
je konkrétní součást zbývajícího partial34, oddělená od C0020.

## 4. Co modulární Delay skutečně dokazuje a co nikoli

Pro vytištěnéρ250000000 jsou všechny18ρ/8ρ/5ρ/4ρ i floor(ρ/2)
kladné signed64 a delta<2^63. Totéž platí pro obecné kladné celéρ
s18ρ<2^63; žádná širší maximální hodinová frekvence se zde neslibuje.
Na začátku Delay je t původní rI a ref_time=(t−delta) mod2^64.
Je-li t≥2^63, BN přeskočí druhý test: protože delta<2^63≤t,
starý interval má dostatek času. Je-li0≤t<2^63 a t<delta, signed
ref_time je záporný a2B nastaví delta←delta−t. Ve zbývajícím případě
je ref_time nezáporný a jde se přímo do normálního polling loopu.

**Podmíněný důkaz normálního loopu:** jestliže mezi původním GET
a zachycením deadline nedojde ke skrytému resetu, pak po e taktech
GET/SUBU vyhodnotí(delta−e) mod2^64. Dokud0<delta−e<2^63,
PBP pokračuje; při prvním malém překročení deadline je signed výsledek
nekladný a odejde. V případě přechodu přes samotné2^64 bez resetu
má SUBU právě tento správný význam; CMPU by porovnával nesouvisející
nezabalené adresy. Správnost této lokální aritmetiky není správnost
přes libovolné obnovení časovače handlerem, jak prokazuje C0020.

V resetové větvi1B uchovává ref_time předchozí přečtené rI, GET
vezme nové a CMPU zůstává kladné, dokud nové je menší. Při zachyceném
zvýšení, nebo rovnosti způsobené resetem, PBP odejde a znovu začne
Delay se zbývající delta. Rovnost bez resetu není možná při skutečně
klesajícím timeru a několika taktech mezi reads. Při každém takovém
spolehlivě zachyceném přechodu odečtené t započte čas do staré nuly.
Dobu handleru a kus nového intervalu program přesně neodečítá;
vzniká dodatečné zpoždění. Aby každý reset byl zachycen, je třeba
kvantitativní podmínka na velikost obnoveného rI a mezery mezi reads,
ne jen slovo „not-too-small“. Při více resetech se režie sčítá.

Nezávisle na této neurčitosti již **C0020** prokazuje opravdové
zacyklení normální větve i při rychlých, dobře oddělených resetech.
Starý argument0≤delta<2^63 je výslovně odvolán v původní027–035
poznámce. Není potřeba spoléhat pouze na nemožnost vyčíslit slovo soon.

## 5. Přesné nominální meze tam, kde žádný reset není

Uvažujme explicitně jednotaktové GET/SUBU a správně predikované PBP
podle knižního modelu, bez přerušení a s dostatečným zbývajícím timerem.
První polling GET přijde p=4 takty po vstupním GET u nízkého t a p=5
u vysokého t, kvůli vzatému obyčejnému BN. Další reads jsou po3υ.
Při velkém delta≥p první úspěšný read nastane po

    e=p+3ceil((delta−p)/3), tedy delta≤e≤delta+2.

Od tohoto read do návratu stojí GET1,SUBU1,nevzaté PBP3,GO3, celkem8υ.
Proto přesná délka je e+8, tedy delta+8…delta+10. Pro delta<p se
vrací po p+8. Tento rozpis obsahuje i poslední chybnou predikci.
Je to podmíněný instruktážní model, nikoli nová univerzální OS záruka.

Za těchto podmínek má celý Flash proρ/2≥5 cenu

    12ρ−8[ρ liché]+343…377 υ,

protože má207υ vlastní režie a17 prodlev s dalšími8…10υ. Tím lze
pochopit řád několika setυ u lokálního světelného přechodu. Žádná
pevná horní mez několika setυ pro všechny povolené OS/I/O průběhy
z toho neplyne; po C0020 nemůže taková původní obecná věta platit.

## 6. Přesné pokrytí stránek a zbytek práce

Celáfile119: přibližné S10 má030–031-recovery; každý kalendářní výrok
32/33 má032–033-recovery, včetně dvou převzatých historických nálezů
a explicitních pramenných výjimek. Všechny věty úvodu34, jeho GREG/
adresa/clock předpoklady i každý první Delay blok mají§1/4/5 zde
a potvrzený C0020. File119 je kompletně zmapovaná, ale partial pro
E32 superlativ, E34 a přesné faktické výjimky.

Celáfile120: normální Delay loop/return mají C0020 a§4/5; všechny
názvy, handly, arg bloky,16bajtů příkazových polí a deklarace mají§1;
každá Flash instrukce, jeho osmičlenný cyklus a náklady mají§2/5;
Main/Wait až po první přípravu osmivteřinové prodlevy mají§3. File120
je kompletně zmapovaná, ale partial pro správnou celou realizaci34.
File121 je zde posouzena pouze po konec odpovědi34; následující1.4.1
odpovědi nejsou tímto blokem uzavřené. File58 má ještě křížovku35.

E34 zůstává partial s těmito konkrétními závazky: opravit a dokázat
Delay pro přípustné timer resety, vymezit/ověřit maximální OS/I/O
režii požadované časové tolerance, a vyřešit význam ztraceného
sensorového požadavku u amber hranice. Matematika bajtů, všechny
řídicí větve a podmíněné náklady už nejsou neurčená mezera. Nový
výpočet ani rerun k tomuto bloku nebyl potřebný.

Vzorové zásady byly použity na přípustné stavy a každou větev, celou
cenu finálních predikcí a rozlišení lokálně správné modulární operace
od chybného globálního ukončení. Malé zpoždění jednoho čtení se
automaticky nepovažuje za malý dopad vynechané události.
