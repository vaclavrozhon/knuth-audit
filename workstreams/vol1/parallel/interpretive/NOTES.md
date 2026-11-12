# §1.4.3: interpretace, simulátor M a trasování

Rozsah tvoří hlavní text od nadpisu na s.200 do konce s.214, cvičení
1.4.3.1–1 až9 včetně dodatku z1.1.2025, cvičení 1.4.3.2–1 až7 a odpovědi
na s.530–531. S.200 nad nadpisem a s.215 již patří jiným blokům. Prohlédnuty
byly původní obrazy s.200–214,530–531, nikoli jen OCR. Přepis instrukcí
je v [programs.py](programs.py). Výsledky mají oddělené technické a
bibliografické meze; konečný stav je v [UNIT_STATUS.json](UNIT_STATUS.json).

## Značení a invariant simulátoru

`b` je základ MIX bytu, libovolné celé číslo64 až100; `B=b^5` je počet
možných velikostí celého slova. Slovo uchovává zvlášť znaménko a pět
bytů, takže `+0` a `-0` jsou různé reprezentace stejné číselné hodnoty.
Pole `F=8L+R` vybírá znaménko při `L=0` a byty od `max(1,L)` do `R`;
platí `0<=L<=R<=5`. Instrukce má kód `C`, indexový selektor `I` a
efektivní adresu `M`, tedy podepsanou adresní část plus indexový registr
vybraný `I`, je-li `I` nenulové. Simulovaný program používá paměť0 až3499.

Na vstupu do řádku010 je `rI6` adresa příští simulované instrukce.
Příslušná dvojice `AREG,...,XREG` a `SIGNA,...,SIGNX` obsahuje velikost
a znaménko každého simulovaného registru. Znaménka jsou celá čísla±1,
nikoli jen znaménkový bit těchto buněk. `JREG` je kladná návratová adresa,
`COMPI` je−1,0,+1 podle porovnání a `OVTOG` je0 nebo1. `CLOCK` již zahrnuje
čas předchozí instrukce: řádky007–009 jej započítávají na začátku cyklu.
Při zastavení těsně před CYCLE je proto nutno přičíst ještě adresní pole
samomodifikované instrukce TIME. MOVE přičítá navíc2 za každé kopírované
slovo přímo do CLOCK. Tento invariant platí indukcí po instrukcích,
dokud nenastane výslovně zachycená chyba nebo nepodporovaná operace.

Různé registry vnitřního MIX jsou pracovní prostředky; jejich indikátor
porovnání není simulovaný COMPI. Řádky035–036 před přechodem na operátor
vypnou skutečné přetečení, které mohlo vzniknout pomocným výpočtem.
Vlastní chyba sledovaného programu se pak zachytí přes OVCHECK. Při
platném reprezentovatelném CLOCK nepřeteče časový čítač; nekonečně dlouhý
program nelze měřit konečným slovem a není zde tvrzen neomezený čítač.

## Obecná správnost jednotlivých částí M

**Řízení a pole.** Řádky010–015 uloží celou instrukci a sestaví její
podepsanou adresu. Znaménko zůstává v rA z řádku010, ačkoli LDX na013
bere pouze byty1:2. Při indexování řádky020–023 přičtou index se správným
znaménkem. CMPA ZERO(1:3) testuje nulovost tří horních bytů, tedy mez
`|M|<b^2`. Indexový selektor musí být0 až6. Tabulka OPTABLE je ukotvena
na poslední položce, takže `rI4=C-63` adresuje přesně položku C; nejde
o chybný záporný index. V bytu3 tabulky jsou značky pro operace nad
dvoubytovými registry. MEMORY kontroluje `0<=M<3500` a rozdělí slovo
na velikost v rA a znaménko±1 v rX. FCHECK dělí F osmi, kontroluje
`R<=5` a `L<=R`; nezápornost plyne z nezáporného bytu F.

GETV nejprve získá celé paměťové slovo. Pro `L>0` nastaví kladné znaménko
a vynuluje prvních `L-1` bytů dvojicí posunů; posun o `5-R` poté
zarovná vybrané pole vpravo. Pro `L=0` zachová znaménko i při `R=0`.
GETAV používá stejnou extrakci pro již načtený simulovaný registr.

**Aritmetika.** ADD/SUB přejdou na společnou rutinu INC se správným
znaménkem operandu. Označme starou velikost registru `a` a velikost
operandu `v`. Pro stejná znaménka se sečtou velikosti; přetečení se
zachová přes OVCHECK. Pro opačná znaménka se spočte `v-a`: při kladném
výsledku se převezme znaménko operandu, jinak se zachová znaménko
registru. To zahrnuje nulový výsledek, jehož znaménko má zůstat původní.
STA(1:5) ukládá absolutní velikost. SUB pouze obrací znaménko operandu.
MUL nastaví obě výsledná znaménka na jejich součin a násobí velikosti.
DIV nastaví znaménko podílu na součin znamének a znaménko zbytku na
staré znaménko rA; zřetězí velikosti A a X. Případ, kdy podíl nevejde
nebo je dělitel nula, má podle MIX neurčené A/X: nebyla mu přisouzena
nová definovaná hodnota ani tvrzena chyba knihy.

**Načítání a adresní operace.** LOAD/LOADN ukládají velikost a původní,
resp. opačné znaménko. SIZECHK kontroluje dvoubytovou mez právě u
indexových registrů. ADDROP vybírá INC, DEC, ENT a ENN pomocí `F-3`.
Při `M=0` získá znaménko z původní instrukce, jak vyžaduje pravidlo
pro ENTA−0 a ENTA−5,1 při `rI1=5`. Znaménko při součtu adres, jehož
číselný výsledek je0, se proto omylem nepoužije pro ENT/ENN.

**Ukládání.** STORE ponechá pravých `5-R` bytů ve spodní části rX,
připojí příslušný počet nízkých bytů registru a doplní původních
`L-1` horních bytů z paměti. Pokud `L=0`, použije znaménko registru;
jinak původní znaménko paměti. Konstrukce funguje i pro pole0:0,
pro STJ s dvoubytovou velikostí a pro STZ s kladnou nulou.

**Skoky a porovnání.** JUMP má přesně deset variant F=0 až9. JOV/JNOV
testují původní OVTOG a vždy jej vypnou. Větev JMP uloží příští PC do
JREG, JSJ to neudělá; MEMORY kontroluje cíl pouze při provedeném skoku.
REGJUMP převede znaménko/velikost registru na−1,0,+1 a použije posledních
šest položek stejné tabulky. Záporná nula proto splňuje nulový test,
nikoli záporný. COMPARE extrahuje stejné pole paměti a registru, připojí
znaménka a zapíše přesně−1,0,+1; `-0` a `+0` jsou porovnáním stejné.

Tím jsou pokryty všechny uvedené kódy0–4,8–33,39–63. Kniha výslovně
vynechává floating point,5–7, I/O a chybová hlášení; absence není nový
nález. V přepisu jsou chybové vstupy samostatné HLT zarážky, nikoli
pokus o doplnění politiky pokračování po chybě.

## Cvičení 1.4.3.1

1. FCHECK je voláno na150 a207, pokaždé bezprostředně před MEMORY.
   Může se stát dalším vstupem do MEMORY; oba návratové body se sloučí
   a `rI2=-R` lze připravit jednou. Nutno zachovat rozdíl, že samotné
   MEMORY používá také JSJ a MOVE bez kontroly F. Odpověď je správná.
2. SHIFT volí poslední dva byty jedné ze šesti instrukcí SLA/SRA/SLAX/
   SRAX/SLC/SRC a přenese je na místo vykonávaného posunu. Opakováním
   posunu o1 přesně M-krát dostaneme posun oM, včetně saturace nulami
   nebo rotace modulo10. `M=0` se vrací bez změny. Signální buňky
   se nemění, a proto se neposouvají znaménka. Negativní M a F>5 se
   zachytí. Ověřeny i maximální hodnoty M=b²−1 ve všech37 radicích.
3. MOVE po každé iteraci zvyšuje zdroj i cílové I1 o1. Přímá sekvenční
   kopie, nikoli snímek bloku, správně reprodukuje i překrývající se
   oblasti. Při záporném cíli se chybuje; `-0` je legální a před prvním
   inkrementem se jeho znaménko změní na plus. Při F=0 nedojde ani
   k přístupu do paměti, ani ke změně znaménka I1. Čas je1+2F.
4. IN0(16) a JBUS*(16) před řádkem004 čekají na celé načtení16 slov;
   zbytek BEGIN nastaví počáteční PC a čerstvě sestavený JREG je0.
   Ověřena skutečná MIX vstupní sekvence při prodlevách0 a17 ve všech
   radicích. Použitý oddělený vstup je ekvivalentní vložení dvou řádků
   bez nutnosti přemístit celý doslovný přepis. Nejde o tvrzení, že
   opakované zavolání BEGIN bez obnovení dat resetuje všechny registry.
5. Řízení007–036 stojí34u bez indexování a dalších15u s indexováním.
   GETV stojí52u a dalších5u při L≠0. Přidání LOAD obsluhy dává97u
   pro LDA/LDX,99u pro LDi; příplatek za indexování/pole se sčítá.
   ENTA/ENTX stojí55u, ENTi57u; M=0 přidává2u. Výrok přibližně50:1
   je konzistentní s97/2 a55/1. Číslo8422/178≈47.3146 je aritmeticky
   správné, ale konkrétní historický testovací program v knize chybí,
   a proto jeho běh nebyl nezávisle rekonstruován.
6. Kniha nemá tištěnou odpověď. Konstruktivní řešení udržuje pro každou
   jednotku čas dokončení `ready[u]`; IN/OUT/IOC nejprve počkají na
   předchozí akci téže jednotky, provedou přenos a nastaví nový čas.
   JBUS/JRED testují `clock<ready[u]`, resp. opak, a při skoku zapisují
   JREG. Čtení karty a posun stránky trvají10000u, řádek7500u.
   Pro JBUS* lze přeskočit přímo na čas dokončení. Jestli se alespoň
   jednou skákalo, musí zůstat JREG=p+1; poslední neprovedený skok
   přidá1u. Zrychlení nesmí přeskočit události jiné jednotky.
   [check_extensions.py](check_extensions.py) je spustitelné algoritmické
   řešení a nezávislá reference. Následně byly doplněny skutečné MIX
   obsluhy v io_program.py; jejich testy jsou v check_io.py.
7. Každá rozpracovaná akce má navíc čas přenosu a uloženou adresu
   bufferu. CYCLE provede všechny již splatné přenosy právě jednou a
   jejich čas nahradí nekonečnem. Indukční invariant: nedokončená akce
   má buď čekající přenos, nebo už přenesla, ale jednotka je stále busy.
   Při nuceném čekání i HLT je třeba provést i takto odložené události.
   To dokazuje popsanou odpověď; testuje se IN v5000u, OUT v3750u,
   souběh obou zařízení a dokončení při HLT. Odložení odhaluje běžné
   předčasné použití bufferu, není to úplný detektor všech chybných
   přístupů v celém intervalu busy. Úplná politika kontroly vlastnictví
   bufferu není tvrzena ani potřebná pro zadané řešení.
8. Odpověď je správná. Pád z3499 vede na rI6=3500 a fetch BEGIN;
   simulovaný STZ TIME potom narazí na MEMERROR. Indukce dává
   `0<=rI6<=3500`, dokud diagnostika zastavuje. Provedené skoky kontroluje
   řádek254; jediné překročení při sekvenci vede na uvedenou chybu.
9. Nové zadání z1.1.2025, bez připojené odpovědi. Vlastní SPEC řešení
   rozliší F=0,1,2, větší F odmítne. NUM/CHAR působí na skutečná rA/rX
   načtená z velikostí a výsledek uloží přes STOREAX/OVCHECK; znaménka
   zůstávají ve svých buňkách. HLT v našem doplňku připíše1u do CLOCK,
   vynuluje odložený TIME, zastaví a při pokračování přejde na CYCLE.
   Pro NUM/CHAR se používá známě opravená tabulková doba10u.

## Trasování: invariant a skutečná omezení

Na CYCLE obsahuje rA adresu další sledované instrukce, PREG se na ni
nastaví, AREG uchovává sledované rA a adresní pole JREG sledované rJ.
Ostatní registry i porovnání/přetečení mají skutečné sledované hodnoty.
Instrukce mimo skoky a STJ se kopírují na INST a vykonají samy; žádná
taková MIX instrukce nepočítá adresu vzhledem k vlastnímu PC.
STJ se nahradí STA se stejnou adresou, indexem a polem, s rA rovnou
simulovanému J. Všechny skoky34,38–47 jsou přesměrovány na JUMP bez
indexování. Jejich podmínka se tedy vyhodnotí původním hardwarem,
zatímco původní adresa/index byly zachovány v INST1. Při provedeném
skoku se uloží původní PC+1 do JREG, kromě JSJ; pak se původní cíl
spočte přes ENTA. Neprovedený skok pokračuje na následující adresu.

Pomocná aritmetika používá pouze kódy, pole a adresy velikosti nanejvýš
řádu b², nemůže tedy přetéct celé slovo. Nepoužívá porovnávací instrukce,
takže COMPI ani overflow sama nemění. Výjimkou jsou samozřejmě skutečné
sledované operace. J se při základním LEAVE neobnoví, což text výslovně
uvádí. I/O načasování není při zpomalení shodné s nativním během;
to odpovídá uvedenému omezení(c).

Doslovné omezení6(a) je slabší než invariant nutný pro průhlednost:
sledovaný program nesmí používat pro významná data ani **čtení** buněk,
které tracer mění. Jediná instrukce LDA AREG při původním AREG=0 a rA=1
dá přímo0, pod tracerem1. Reprodukce je samostatně v
[trace-private-read.txt](trace-private-read.txt). Je to redakční kandidát
s podstatnou nejistotou: autor mohl považovat privátní oblast za implicitně
vyhrazenou. Není prezentován jako nový algoritmický nález ani odeslán ven.

## Cvičení 1.4.3.2

1. Nechť `j` je obnovované J, `1<=j<=4000`. Odpověď na chvíli uloží
   do paměti j−1 instrukci, jejíž zakódovaný cíl je místo za konstantou1H.
   První JMP se dostane na j−1; tam vykonané JMP nastaví J právě na j.
   Původní paměťové slovo je mezitím v rA a STA je vrátí zpět.
   Obnoví se I1, X i A a JSJ opustí tracer, aniž znovu přepíše J.
   Předpoklad j≠0 je potřebný pro existenci adresy j−1. Platí obvyklá
   rezervace privátní oblasti traceru; program ji nesmí používat jako data.
2. Buffer má100 slov a PTR postupuje od−100 do−10 po10. Každý záznam
   zabírá právě deset slov a desátý vyvolá OUT, pak se PTR vrátí na−100.
   JBUS před zápisem dalšího záznamu chrání buffer. Znaménka registrů
   se ukládají plnými ST instrukcemi, včetně záporné nuly.
   `B4=b^4` a `BIG=B−8`. ENTA8; JNOV buď nechá8 a vypnutý overflow,
   nebo ADD BIG přeteče na0 a znovu jej zapne. JL/JE přidají0,1,2
   podle původního porovnání. Výsledný byt tedy obsahuje přesně
   požadované0/1/2 plus8, právě když overflow nebylo zapnuto.
   Známá oprava z3.9.2008 přesouvá LD1 I1REG před řádky14–35.
   Původní umístění až po31 rozbije indexované STJ: větev19–23
   obchází obnovu I1. Reprodukce a následný úspěch opravy jsou uložené.
   Doplnění vypsání neúplného posledního bufferu a přetočení pásky je
   výslovně ponecháno zvláštní závěrečné rutině; nebylo zaměněno za chybu.
3. Pro MIX je páska rychlejší zařízení a ukládá slova přímo. Převod
   deseti registrů do tisknutelného formátu by prodloužil i zvětšil
   tracer; odložený tisk umožňuje výběr záznamů. Správné pro popsaný
   stroj, nejde o univerzální tvrzení o současném hardware.
4. Při self-trace nejprve projdou ENTER,...,CYCLE. Samotné trasování
   CYCLE ale přepíše jeho PREG adresou ENTER; INCP z něj přečte ENTER
   a pokračuje na ENTER+1. Přesně potvrzená posloupnost při ORIG3500
   je3500,3501,3502,3503,3504,3505,3501,3502,3503,... . Odpověď tedy
   správně popisuje první porušení invariantu a porušení omezení(a).
5. Dvě neoddělené kopie problém neřeší: jakmile vnější tracer vykonává
   vnitřní a vnitřní se pokusí trasovat zápis do privátní buňky vnějšího,
   zničí jeho aktivní kontext. Přesný chybný cyklus závisí na inicializaci
   adres/J/X; zadání žádnou jedinou takovou konfiguraci nefixuje a
   kniha nedává odpověď. Obecný závěr je neplatnost věrného vzájemného
   trasování, ne univerzální konkrétní perioda. Zde není odvozen úplný
   běh všech možných inicializací. Doplněná konkrétní konfigurace v
   check_mutual.py má kopie na1000 a2000 a tři vstupní instrukce, které
   při vstupu B nastaví jeho J na ENTER_A. První křížový zápis je
   STX do TEST_A na1006 v kroku486; později se opakuje celý stav po82
   instrukcích (kroky2539 a2621). Zahrnuty jsou všechny měněné buňky,
   registry, J a flagy. Proto je perioda certifikovaná rovností stavů,
   nikoli pouze pozorováním počitadla. Ověřeno ve všech37 radicích.
6. Nápověda odpovědi je správná jako princip oddělení stavů. Každá úroveň
   musí mít vlastní hodnoty pracovních buněk, které vnější program změnil.
   Logické čtení vrátí hodnotu ze soukromé tabulky dané úrovně, jinak
   z neměnné základní paměti; zápis mění pouze tuto tabulku. Přepnutí
   úrovně navíc ukládá registry, PC, J, indikátor porovnání a přetečení.
   Indukcí po jednotlivých logických instrukcích má pak každá úroveň
   stejný stav jako oddělený počítač a nedochází ke clobberu zex4/5.
   Počtem současně rozpracovaných úrovní roste potřebná paměť, takže
   skutečný MIX musí ohlásit vyčerpání. Úplná vlastní MIX implementace
   je nyní v selftrace_program.py a důkaz v SELFTRACE.md. Používá
   nezměněné jádro emulátoru; dva plné běhy do vyčerpání128slovné
   přidělené oblasti mají po4 465 344 MIX krocích a reálný vnořený
   výpis. Navíc byl ověřen výpis třetí úrovně z dosažitelného mezistavu
   a maximální2000slovná alokační hranice ve všech37radicích.
7. Odpověď skenuje od aktuálního PC po nejbližší potenciální skok,
   opatří jeho místo i následující místo návratem k monitoru, obnoví
   registry a pustí celý přímý úsek. Při návratu obnoví přepsaná slova
   a zaznamená skutečně provedený skok. Pro posloupnost dvojic
   `(x_i,y_i)` jsou mezi skoky vykonány intervaly `[y_i,x_(i+1)]`;
   začátek a konec běhu je nutno znát jako metadata. Četnosti se získají
   sečtením pokrytí těchto intervalů plus prvního/posledního úseku.
   Výslovně uvedená výjimka samomodifikace je skutečná: nové skoky mohou
   přeskočit monitor a změna již opatřeného skoku může smazat návrat.
   STJ lze zvlášť zachytit nebo virtualizovat jeho zápis. Odpověď
   neprohlašuje obecnou správnost pro libovolnou samomodifikaci.

## Errata, prameny a reprodukovatelnost

Prohledány všechny čtyři vrstvy; lokální výpisy jsou
`results/errata-{all1-prepre,all1-pre,all1,err1}.json`. Originální PDF
ověřeno na stranách17,39 all1-prepre a8 all1. Známé opravy jsou
SPEC(1)→SPEC(10), komentář rI1 na208, JXL→JXNP na213, přesun LD1
I1REG v odpovědi na531 a drobné typografické opravy202,204,211.
Žádná z nich se nepočítá jako nový nález. Doplněk212/ex9 byl zahrnut.

`check_simulator.py`, `check_trace.py`, `check_extensions.py` a
`check_go_spec.py` jsou deterministické příkazy spouštěné pomocí python3.
Importují auditní mix_machine/mixal/mix_io beze změn. Přepisy byly
porovnány s obrazy, nikoli generovány OCR. Testy jsou doplněk výše
uvedených invariantů, ne jejich náhrada. Neproběhla kontrola současných
externích MIX implementací ani formální důkaz core emulátoru.

Bibliografické podrobnosti jsou odděleny v
[sources/coverage.json](sources/coverage.json). Randell–Russell1964
s.34–36 dokládají interpretovaný objektový jazyk Whetstone a Control
Routine; s.34–35 byly ověřeny i obrazem. Primární tex.web obsahuje
část31 v modulu583 a lig_kern jazyk v přesně citovaném modulu545,
včetně výslovného Fuchs1979. Současná dokumentace dvips potvrzuje
Rokického autorství a převod DVI→PostScript. PostScript1990 byl získán
jako druhé vydání z veřejného zrcadla (elektronické revize1992–1994); nejprve stažené třetí
vydání1999 je správně přejmenováno a není vydáváno za citovaný pramen.
Knuth1963 a Evans1964 mají ověřené bibliografické údaje, ale jejich
celé původní články se zatím nepodařilo získat (vydavatelé403). Osobní
anekdoty na203 jsou označené autorské svědectví, ne nezávisle ověřené
výkonnostní měření. Obecné tvrzení o historii prvních interpretů nebylo
samostatně dokumentárně prokázáno.

## Doplnění: skutečné MIX obsluhy I/O

`io_program.py` doplňuje všechny obsluhy požadované vex6/7. S původním
M, SHIFT, MOVE i SPEC zůstává poslední adresa3965 a celý simulovaný
prostor0–3499 je nedotčený. Pole READY a DUE mají po dvou položkách;
COMMAND uchovává přenosovou instrukci s již vyhodnocenou adresou a
vynulovaným indexem. Záporné DUE znamená, že přenos není naplánován.
UNIT ověřuje jednotku16/18 a konkrétní obsluha přípustný směr přenosu;
pro IOC je zde definován jen tiskový posun stránky sM=0. BUFCHK
vyžaduje úplný buffer uvnitř simulované paměti, včetně krajních adres
3484 pro16slovnou kartu a3476 pro24slovný řádek.

WAIT posune CLOCK na READY, je-li nutné čekat na minulou akci, a zavolá
TICK. Po každém započtení odloženého času do CLOCK a před fetch se TICK
volá také zCYCLE. Přenos se provede právě tehdy, když DUE není záporné
a DUE<=CLOCK; DUE se nejprve nastaví na−1. Vykoná se skutečný IN/OUT/IOC
a fyzické JBUS počká na dokončení hostitelského přenosu, aniž tento
pomocný čas přičítá k simulovanému CLOCK. Logická jednotka zůstává busy
až do READY. Přeskočení čekací smyčky JBUS* nastaví JREG na p+1,
posune CLOCK naREADY a ponechá1u za poslední neprovedený JBUS na TIME.
HLT počká na obě jednotky, takže žádný odložený přenos nezůstane ztracen.

TICK může vyřídit obě jednotky v pevném pořadí: u platného programu
mají souběžné operace nekolizní buffery, jinak už jde o vMIX neurčené
časné použití bufferu. Pro takový chybný program se neslibuje jediný
univerzální hardwarový výsledek. Kopírované COMMAND používá plnou
effektivní adresu, takže indexované I/O nesčítá index podruhé. Pracovní
I1 je přes TICK uložen a obnoven, ostatní důležité dekódovací registry
TICK nemění. COMPI/OVTOG jsou oddělené, takže pomocná porovnání
nezničí simulované příznaky.

1184 testů pokrývá oba režimy přenosu, všech37radixů a fyzické prodlevy
0/17. Nezávislý oracle provádí běžné instrukce přímo a I/O podle
časového modelu. Porovnávají se všechna simulovaná slova, registry,
PC/J, oba příznaky, CLOCK a skutečné vytištěné bloky/posuny stránky.
Dále12 testů míří přesně před/na/za polovinu doby přenosu a8 testů
na neplatnou jednotku/směr/adresu. Žádná úprava shared mix_io.py.
