# MMIX — celé strany98–101 a124–134

Tato mapa prochází celý obsah stránek, nikoli jen začátky
položek starého inventáře. Znovu se nespouštějí přijaté
SAVE/UNSAVE/PutL/RESUME svědky, dlouhé self-simulation ani
historické programové profily. Nový malý výpočet níže řeší
pouze6067 členů explicitní skalární rekurence.

## 98 / p90: každý řádek542–594 a inicializační odstavec

542–544: již uzavřenýV0176 dává přesné modulo přírůstky
cc,uu,ii; je to autorův jednoduchý nominální model, nikoli
implementace externího časovače libovolného OS. 545–548:
V0177 a celý nový rozbor úlohy14 dokazují všechny hodnoty
resuming a skutečný vykonanýopcode. Známéerratum komentáře
CMPU je evidované odděleně, nikoli jako vlastnínález.

549–559: handle3 je platný; head=Chunk0 aalloc=head+4120
zakládají úplný MemFind invariant. HostrN se kopíruje plus1
modulo2^64; tato lokální rovnice netvrdí globální unikátnost
serialů (samostatnéR0004). Za vytištěného předpokladu
dodaného filename je argv[1] na$1+8. IOArgs obsahuje
jeho pointer a již inicializovanýBinaryRead; Fopen záporný
výsledek vedeError, jinak se použije loader20. Jeho všechny
platné skupiny, nulové délky, EOF a překryvy mají argument
v `exercises-1.4.3-015-020-recovery.md`.

576–579: posledníloc je packedG/A word platnéhoSAVE obrazu.
Mezi ním a uloženým$255 je12specials a tento jeden word,
tedy13octabytů=104bytů. Odečteníloc−104 správně najdeMain.
580–584: nezávislýMemFind aLDTU z#f0 načte přesně startup
tetrabyte. CSNZ nahradíMain adresou#f0 právě pro nenulový
tetrabyte. Tentýž explicitní nonzero test má primární
MMIX-SIM3385–3389. NulovýHALT na#f0 tímto konvenčním
markerem alternativního startu není; nezaměňujeme to
s tvrzením, že loader uchovává samostatný bit přítomnosti
každé nulové instrukce.

585–588: #FB0000FF je UNSAVE$255 sX=Y0. G255 před prvním
Fetch zajistí, že pointer$255 jeglobal. resuming1 vloží
umělou instrukci, validní inverse obnoví registry a poté
AllDone odstraní resuming. inst_ptr je užMain nebo#f0.
Úloha12 má přesný bootstrap argument a samostatnou opravu
pozdějšího přetočeníuu; žádný nový inverse se neprohlašuje.
589–590: Error nastaví hostt=−22 a Halt ukončí interpret,
jak tato úmyslně jednoduchá diagnostika stanovuje.

591–594: úplný primárníMMIX-SIM1806–1811 inicializuje
rK=−1, rT.h=#80000005, rTT.h=#80000006 a rV.h=#369c2004;
ostatníhalves statickéhog jsou nula. To je přesná shoda
všech čtyř64bit konstant. **Odvození obecného OS není
chybějící povinností této věty**, která udává modelové
počáteční hodnoty. Tuto částV0180 uzavíráme tímto přímým
specifikačním porovnáním.

## 99 / p91: všechny odstavce a úlohy1–7

První dva odstavce jsou přesně předchozí bootstrap/nonzero
konvence a čtyři konstanty. Řeč o načtené instrukci na#f0
je třeba číst ve výslovné nonzero startup konvenci; zde
neověřujeme samostatnou loader-přítomnost nuly.

Bodya–d přesně říkají, co program vynechává. a: vlastní
text obsahuje označené cvičebnímezery; b: všechny popsané
error cesty končí jednotnýmError/Halt; c: jediné udržované
souhrnné statistiky jsoucc/uu, branchcc adjustment nezakládá
samostatný histogram; d: předložená rutina nemá interaktivní
diagnostickýdispatcher. To lze ověřit celým listingem.
Tvrzení o snadnosti či užitečnosti debuggeru je autorské
hodnocení bez určené číselné meze, ne nová optimalizačníúloha.

Samostatnýfakt „delší než kterýkoli jiný program in this book“
nemá dosud úplnou porovnávací inventuru ani jednoznačně
vymezenýFascicle/Volume1 rozsah. V0180 proto zůstávápartial
**jen pro tento přesný fakt**, nikoli pro hypotetickéOS
odvození. Pracovník
svazku1 výslovně potvrdil, že jeho celý obnovený rozbor
MIX interpretu takovou inventuru neobsahuje. Žádný nový
census se nepouští. Strana99 se nezelení.

1: všechny čtyřiInfo hodnoty a jejich skutečné operandy,
specialrM a wyde posun jsou v původním§1 plus úplné256tabulce.
2: všechny tři časové sloupce, flagovépodmínky, local/marginal
a dvěMemFind misses jsou ve starém§2; konkrétníC0009/C0012
se přebírají, netestují znovu. 3: celý přechodovýL256 a
okamžitýpush je v úplném ring argumentu. 4: kapacita,
zarovnání a nulové nové nodes mají přesný důkaz v081–086
a `results/node-capacity4.json`. 5: celýcallgraph i dosažení
maxima11 jsou v `exercises-1.4.3-005-recovery.md`, ne pouze
protiargument10. 6/7 mají celé níže spárované odpovědi.

## 100–101 / p92–93: každé zadání8–22

8–11: kompletníGET,PUT,POP a opravenýSAVE se přebírají
z `exercises-1.4.3-001-014.md`, včetně přípustných oborů,
markerů a všech větví. Poznámka kPOP po250pushed aG32
je přímý případmin(G,p+min(X,L+1)) a nepřidává nové
neověřené tvrzení. Úplný seznamSAVE jeG…255,0…6,23…27
a2^56G+A: přesně12samostatnýchspecials a packedword.

12–14 mají nové samostatné012/013/014recovery důkazy.
Malformedimages se nepřidávají; store-ruleR0009 se naopak
neskrývá za správnost knižníhohelperu. Celá definice r1/r2
včetněnormalmasky, nemarginalX a všechQ je pokrytá.

15–20: celý nový `exercises-1.4.3-015-020-recovery.md` dává
každou I/O větev/cenu, ringρ32, konkrétníGrowLocal i celý
binární formát. E16 má přesnou volnou scratchmez, E17
R0007count/buffer doménu; oba staré bezpodmínečné checked
se znovuotevírají. l0 v20 dává formálníposledníadresuλ−8,
a přípustnostspustitelnéhoobrazu je další samostatnýkontrakt.

21: kvalitativní finite-state část i aritmetika rekurence
níže jsou oddělené od skutečnérekurze aC0010. 22: oprava
čtyřbajtovéhotaktuC0006 a rekonstrukce trace jsou přesně
prokázané; úplný požadovaný tracer nadále chybí. Každá
vytištěná část zadání, omezeníself-modifyingtext a minimální
dalšírestrikce zůstáváviditelná, není z ní uzavřenýprojekt.
Strany100/101 zůstávajípartial.

## 124 / p116: celý konec korutin a odpovědi interpretu1–2

Dokončeníkorutiny1 je argument jednotoho/těchto dvou
continuationstavů; srovnáníužitečnosti při více propojeních
je označenéautorskéhodnocení. Korutiny2/3 mají úplnýztracený
prvníznak a každýTETRAoffset v001–007 i075–080. Korutina4
má oba rR wrappers, počátečníkontext a8υcenu. Korutina5
má obaPUSHJ/POP wrappers, celouobnovuL/rJ a6υcenu.
Korutina6má nejenbalanced-stackčást, ale i celýkonkrétní
private-context protokol v006–007recovery. Nikde se
nepřebírá starépartial soukromýchstacků jako hotovédůkazy.

Interpreter1 jsou všechny čtyři správnéoctabyty, včetně
PBPB3υzákladu aMUXIrM. Konecstrany uvádí dvěchybné
nákladovéformule: celýMemFindC0009 aGetRegC0012 jsou
převzaté v jejich přesném rozsahu, ne znovupotvrzované.

## 125 / p117: celá tabulka a odpovědi2–6

Všech30dílčíchbuněk a3součty tabulky má rozklad starého§2.
UADDU jsou dvějednotkové položky přehozené meziX/Z řádky;
součet to nemění a je to zapsaná drobnost bez novékarty.
π znamená2υpři vzaté větvi, nikoli0/1indikátor. Dvě
optimálnímiss korekce patříC0009; marginalsource patříC0012.
EmpiricképrůměryC/U/A zdlouhého self-simulation běhu jsou
výslovněvynechaná reprodukce, ne nezávisleověřenýcensus.

3: celýL256edge;4: přesnákapacita559670633304293node i
shodaobouzaokrouhlenýchčitatelů; praktickýlidskýčas je
nekvantifikovanýkomentář.5: nejdelšískutečná cesta má11,
dosažitelnývalidnívstup jeprokázaný; ukončenípoError a
obě možnostiunwind mají úplnépřevzatéargumenty.

6: všech7řádkůDiv/DivU používá jižnačtené y,z. SignedDIV
proběhne se zakázanýmiD/Vhosttrips, unsignednejprveinstaluje
horníhalf z x do realrD. GET/STO zapíší celý rR do g[rR]
ještě předXDone. Aliasingguestregistrů nepoškodí pracovní
vstupy. Obě helpercesty stojí1μ+64υ předXDone, včetně
samotné60υDIV/DIVU; znaménkové/nulovévýjimky má celý
aritmetickýdůkaz. Stranaobsahuje výslovné empirickévýjimky.

## 126–128 / p118–120: všechnyřádkyCSWAP/GET/PUT/POP/SAVE

7: rovnost staréhoM8 a rP je v t uchována ažpoZSZ. Equal
větev uloží původníX doM a vrátí1; unequal uložístaréM
do rP a vrátí0. Každávětev má3μ+8υpředXDone. Sériový
model nevyžaduje nový důkazmulti-CPUatomiky.

8: YZ<32 přesněvynucujeY0,Z0…31. Sedmaktuálníchworking
specialsii/oo/ss/uu/aa/ll/gg se předloadem synchronizuje;
SRll/gg3 je přesné maléceléčíslo. Ostatnígslotsjsou buď
udržované svými instrukcemi, nebo modelovékonstanty.
Validníhelper má8μ+14υ, invalidnítest4υdoError. Extra
věta „better“oproti32waybranch nebo průběžnémuzápisu
neuvádí kritérium/costmodel; neprohlašuje se za ověřenou
globálníoptimalitu. Je vedená jako výslovná hodnoticívýjimka.

9: všechnypermissionvětve, kódy0…31 ainvalidníXY jsou
prokázané v§9. PutL skutečná64bitchyba máC0014 aobecnou
krátkouopravu; PutA akceptuje právě z<2^18. PutG nejprve
vyloučí vysokébitovéhodnoty,z<32,z<L a potom nuluje přesně
novéglobalsoldG−1…newG. Při zvýšeníG nenuluje žádné
zachovanélocal hodnoty. Známýkomentář PutG se přebírá,
nepočítá jako nález. Preference9testů oproti32waytable
zůstává stejným nevymezeným engineeringhodnocením.

10: celýpůvodní§10 pokrýváX0/X>L/0<X≤L, načtenímarkeru,
každýStackLoad, oba return-valuecases, moduloindexaci,
clampL≤G a dva kroky posunuO. Full-ring přepis může zahodit
jenprávědiscardovanouhornípoložku; jediný možnýreturnvalue
byl uchovánpředem v y. P.120komentář „in most cases“ je
empirickápredikce bez zde nověprokázané četnosti.

11: úplná přijatáinverse dokazujeceloumarker/spill posloupnost,
všechny globals, oběnesouvisléčástispecials i závěrečný
packedword/cílovýpointer. C0007BNZ→BZ se přesně přebírá.
Úloha a stránka nepředstírají správnost neupravené větve.
Toto je mapování jižuzavřenéhodůkazu na každývytištěnýřádek,
nikoli novýběh nebo duplicitníodvozováníSAVE.

## 129–132 / p121–124: celéodpovědi12–17

129: každýUNSAVEřádek, oborvalidníhoimage, prvníbootstrap
a pozdějšíuu-wrap jsou v012recovery. CitovanýProverbs24:26
je literárnípramen; přesnáanglickáverze nebyla rychle
identifikovaná a je výslovněpřeskočena, nikoli matematicky
ověřena. Strana se proto neprohlašuje za plněfaktografickyuzavřenou.

130: celátriproutine je013recovery; širšístoreklauzuleR0009
zůstávápartial. CelýResumehelper doNEG má014recovery a
nové samostatnéC0023. 131: CSNN/JMP a všechny166–173
mají úplnýopravenýargument, nikoli jenC0015vzorek. Každý
Fputs/DoInst/SimInst/SimFinish/SimFclose řádek i počátek
Fopen mají015–020recovery. Výrok o „almost obscenely slow“
byte-at-a-timeI/O je kvalitativníhodnocení bez číselného
hardwarovéhomodelu, ne ověřenéglobálníčasovéoptimum.

132: celýcopy/cleanup aGetArgs mají důkaz včetně všech
arénovýchmezí; chybějícíobecnýscratchkontraktE16 je přesný
partial. CelýFreadloop včetně obou velikostníchvětví,
kladnéhopostupu a všechshort/errorvýsledků má tentýžrozbor.
Zůstává E17/R0007explicitnísigned-domain interpretace.

## 133–134 / p125–126: zbytek17, celé18–22 a rekurence

Konec17odečítá správnýdeficit; aliasesSimFwrite/SimFseek/
SimFtell zachovajíoriginálníTRAP a smlouvu služby. Explicitní
read-serious-error předpoklad je zakreslený v celémargumentu.
ExistenceexterníchSimFgets/SimFgetws/SimFputws je potvrzená
v primárnímsim.mms608/643/699; celýexterníprogram se tím
automatickyneuzavírá. Všechny18–20 mají přesnépřevzetí výše.

U21základníHello stojí μ+17υ přímo: LDOU μ+υ, GETAυ,
dvěFputsTRAP po5υ aHalt5υ. Jeho celývýstupníargument je
v037–040, beznovéhoběhu. Délky176/5768 a všechnyhlubší
μ/υprofily,časyFopen/Fclose a praktickéHello3 dokončení
nebyly zopakovány: jde o přesněvyjmenované historické
nákladnéreprodukce, ne o matematickyprokázanéčíselnébuňky.

Finite-state důkaz: pro uzavřenýdeterministickýmodel s
pevnýmvstupnímsouborem a standardnímúspěšnýmI/O se po
opakováníglobálníhostavu opakuje budoucíposloupnost.
Má-li nekonečněmnohoopen/closeevents, jejichmezery jsou
nakonec omezené periodou. To vylučuje jejich navždyrostoucí
exponenciálnírozestupy. Neprokazuje to, že prvním selháním
musí být právě node crossing ani určitouhloubku; neomezené
vnější nedeterministickéOSčasování se nepřidává do modelu.

Explicitní skalárníhornírekurence je přesně
`a0=0; a[k+1]=a[k]+5+ceil((3a[k]+2)/512)`.
Prok<30 je a[k]=6k; při k29 je čitatel524 a a30=181.
Protože přičítanáceilčást je mezi(3a+2)/512 a touto
hodnotouplus1, řešeníje sevřené dvěmaafinímirekurencemi
se stejnýmkoeficientem1+3/512>1 a rosteexponenciálně.

První cílenýnice15výpočet pouze6067malýchcelýchhodnot
trval0.00818s; obě algebraickétvary souhlasily vkaždémkroku.
`results/recurse21-scalar-bound.json` dokládá:

* a6065=2300134210731528098≤2^61,
  a6066=2313611559622533151>2^61; uvedené6066sedí.
* Pro skutečnou nodekapacitu559670633304293 přechází
  stejnáhorníposloupnost již mezi a4640=557373330226371
  a a4641=560639189583172.

Ani jedno číslo není skutečněodsimulovanáhloubka. Přenos
hornírekurence na reálnéalokace,chunk-versus-byte jednotky
a dolnímez100^6065 jsou stáleC0010partial. Překročení
horníhoodhadu samo nedáváprotipříklad dolnímezi. Faktor100
je vytištěnýpodmíněnýpředpoklad; neprokazuje se vzorkem
třínormálníchopcode. Žádný dlouhýself-simulation neproběhl.

U22je převzatýcelýargument rekonstrukce správných4bytových
sekvenčníchúseků. Odpověďobsahuje pouze strategii skenovat
do branch/GO/PUSH/POP/JMP/RESUME/TRIP, dočasněměnittext,
přesměrovat9tripvstupů a odsimulovat původnísloty. OS
write-textpermission je explicitní. Chybí konkrétníúplný
tracer se zachovánímstavu, původníchinstrukcí, vložených
RESUME a souběžnýchtripů. E22zůstávápartial pro celou
tutoimplementaci, nikoli chybněoznačenýopenresearchproject.

## Stav a konkrétní použití vzorů

Mapováno je všech15novýchstran, každýodstavec/řádek a
každézadánípodčást. Plnéargumentovépokrytí přibývá na98;
ostatní mají výše přesněuvedenou mezeru nebo výjimku.
V0180konstantyjsouuzavřené, zbývájenporovnávacífakt o
délceprogramu. E16/17se po novéúplnékontrole poctivěotevírají.

Vzory1/4B se používají na všechnyadmisibilnístavovéobory,
souvislouvolnoupaměť, každýnákladovýsloupec, přesnýrozsah
převzatéinverse a oddělenískalárníhornírekurence od
neprokázanéglobálnímeze skutečnésimulace. Žádná správná
jednotlivátabulka nebo nalezenýprotipříklad nezavírá okolní
stránku automaticky.
