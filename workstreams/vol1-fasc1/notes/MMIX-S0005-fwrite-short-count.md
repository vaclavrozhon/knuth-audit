# MMIX-S0005 — Fwrite počítá i nezapsanou část chybného bloku

**Confirmed, medium, doprovodný program.** V MMIX-IO z distribucí
2013-10-17 a 2025-06-20 může Fwrite vrátit úspěch 0, přestože se
nezapsal ani jediný požadovaný byte. Obecně při krátkém hostitelském
zápisu podhodnocuje počet chybějících bytů o nezapsanou část právě
zpracovávaného bloku. Knižní definice n−size je správná.

## 1. Přesná smlouva a přípustný pozorovatelný stav

Originál fasciklu p42/file50 byl znovu zobrazen v
`images/file-050-p042.png`. Fwrite vrací počet úspěšně zapsaných bytů
minus požadovanou velikost. MMIX-SIM:348–357 má stejnou definici a
výslovný C ekvivalent `fwrite(buffer,1,size,file)-size`, doplněný flush.
MMIX-IO:8–12 sám deklaruje, že implementuje tyto primitivy MMIX-SIM.
Nejde tedy jen o požadavek libovolného jiného OS.

C11 committee draft N1570, §7.21.8.2 odstavec 3, specifikuje počet
úspěšně zapsaných elementů; při elementu o velikosti 1 jsou to byty.
Krátký návrat je dovoleným chybovým výsledkem. Primární PDF, metadata,
výňatek a zobrazená původní sazba p336 jsou uloženy v
`sources/c11-n1570*` a `images/c11-n1570-fwrite-return.png`.
Tento dokument pouze přesně určuje již explicitně použitou C operaci;
nenahrazuje kontrakt MMIX odlišnou normou.

Konkrétní MMIX stav: rG=32, rL=0, $255=#200, dvě zarovnané octa
na #200 a #208 obsahují #1000 a 1; byte na #1000 obsahuje #41.
Instrukce `TRAP 0,Fwrite,StdErr` má kód #00000602. Handle 2 je po
mmix_io_init platný TextWrite stream stderr. Hostitelský zápis jednoho
bytu selže a vrátí 0. To je přípustný vnější stav, nikoli porušení
předpokladu otevřeného handle nebo platného bufferu.

MMIX-SIM:2384–2435 vezme $255 jako b, načte mb=M8[b] a ma=M8[b+8],
zavolá mmix_fwrite(2,mb,ma), uloží návrat do rBB a beze změny do $255.
Žádná následná interpretace hostitelského ferror tento návrat neopraví.
Nejde o tvrzení, že každý skutečný NNIX musí používat tuto implementaci;
je to přímo dokumentované rozhraní dodaného simulátoru.

V těle mmix_fwrite se načte n=1, size se předem sníží na 0, host
fwrite vrátí 0 a chybová větev vrátí −size=0. Smlouva požaduje
0−1=−1, tedy #ffffffffffffffff. Tento rozdíl je přímo viditelný v $255.

## 2. Celý postižený obor a invariant

Použijme původní požadavek S, počáteční adresu A, platný write handle
a dostupnou paměť všech čtených bytů. Pro obvyklý záporný signed64
výsledek předpokládáme 0≤S<2^63. Octa sčítání a odčítání se provádí
modulo 2^64; žádné signed C přetečení se z těchto operací nevyvozuje.
Hostitelská volání skončí a vracejí hodnoty dané C smlouvou. Pro důkaz
počtu skutečně úspěšných bytů před chybou navíc předchozí flush proběhly
úspěšně. Samostatná chyba při flush není tímto nálezem uzavírána.

Na vstupu každé iterace platí:

* R=size, 0≤R≤S, a B=S−R bytů bylo předchozími bloky úspěšně zapsáno;
* buffer=A+B modulo 2^64;
* každý předchozí blok vrátil plný počet a pokračování tedy nepřešlo
  přes dřívější krátký fwrite.

Všechny tyto vztahy platí na začátku s B=0,R=S. Počet načtených bytů
je n=min(256,R). MMIX-SIM mmgetchars:2458–2517 se stop=−1 nemá
terminátorovou větev: jedno-bytový krok zvětší m o 1 a adresu o 1,
čtyřbytový krok o 4 a vrátí se právě při m=size. Čtyřbytový krok je
dovolen jen při zarovnané adrese a alespoň čtyřech zbývajících bytech.
Proto 0≤n≤256, přesně přečtený prefix odpovídá bufferu a všechny
indexy lokálního buf[256] jsou v rozsahu. Tato vazba je potřebná,
protože argument nepředpokládá nezaručený short read z MMIX paměti.

Nechť k je návrat hostitelského fwrite tohoto bloku, 0≤k≤n.
Při k<n je celkem zapsáno B+k; požadovaný návrat je

    (B+k)−S = k−R.

Původní rutina již odečetla n a vrací

    −(R−n) = n−R.

Odchylka je přesně n−k, celé číslo v 1..256. Jestliže jde o poslední
blok, R=n, původní rutina vždy vrátí 0, bez ohledu na velikost
neúspěšné části. U dřívějšího bloku vrací záporné číslo, ale velikost
chybějícího přenosu je příliš malá. To pokrývá krátký první, prostřední
i poslední blok, včetně k=0. Pro platný krátký přenos je k−R<0 a
|k−R|≤S<2^63, takže znaménková interpretace je jednoznačná.

Při k=n se smí pokračovat: nové R'=R−n a B'=B+n zachovají invariant,
adresa se posune o n právě tehdy, když je další blok. Je-li R'=0,
celý přenos je dokončen a správný návrat je 0. Pro S=0 se provede
jeden nulový fwrite, který podle C smlouvy vrací 0, a rutina skončí
s výsledkem 0; velikost 0 nezpůsobí nekonečnou smyčku.

## 3. Úplný rozsah auditní opravy a zachované větve

Samostatný change file `sources/audit-fwrite-short-count.ch` zachytí
`written=fwrite(...)` před zmenšením size. Při written!=n vrátí
`ominus(incr(zero_octa,written),size)`, tedy právě k−R. Až při plném
zápisu sníží size o n a pokračuje původní větví. Originální zdroje
se nemění.

Převod size_t na int je přesný, protože 0≤written≤n≤256. Také −n
leží v −256..0. Všechny změněné C celočíselné operace jsou bezpečné
na deklarovaném hostu s nejméně 32bitovým int a přesně 32bitovým
unsigned tetra. Octa výsledek k−R používá původní modulární pomocné
funkce; smí být záporný, aniž by se záporné číslo ukládalo do signed64.

Chybějící write mode vrací jako dříve −S bez přístupu ke streamu;
pro S=0 je to 0, což zde není nový návrh kontraktu neplatného handle.
U readwrite režimu zůstává původní zrušení read příznaku. Zpracování
nulové délky, každý plný blok, volání fflush, posun adresy a návrat
úspěchu zůstávají stejné. Krátký blok končí ihned v obou verzích;
oprava nemění počet přenosů ani se nepokouší opakovat neúspěšný zápis.

Při S>0 každá pokračující iterace sníží R nejméně o 1 a normálně
o 256; při S=0 je jeden průchod. Počet volání fwrite je při plném
úspěchu max(1,ceil(S/256)), při chybě odpovídající prefix tohoto počtu.
Paměťový buffer má konstantních 256 bytů. Oprava přidává pouze konstantní
práci na blok a žádnou smyčku. Architektonických 5υ pro TRAP nezahrnuje
výkon OS; počet C operací se s tímto modelem nezaměňuje.

**Přesná zbývající povinnost:** tento patch neřeší ignorovaný návrat
fflush, jestliže fwrite samo vrátí plnou délku. Pro takové chování
zůstává samostatný otevřený kontrakt přijatých versus vyprázdněných
bytů v `io-recovery-open-obligations.md`. Netvrdí se úplná správnost
MMIX-IO, libovolného C streamu ani libovolné implementace NNIX.

## 4. Originály, veřejné opravy a uložená reprodukce

Celé MMIX-IO z obou archivů jsou byte-identické, SHA-256
`d6732108356986956f4e4a5a883d210a1e4e69216e1f8d614c456fd3126496e5`.
Zdroje a jejich metadata jsou uloženy odděleně. Původní veřejná sazba
[MMIX-IO §18](https://mmix.cs.hm.edu/doc/mmix-io.pdf#page=7) byla zobrazena
v `images/mmix-io-upstream-file007.png`. V ní jsou handle a n deklarovány
unsigned int a záporný posun má explicitní cast; **tuto odlišnost nezamlčuji**.
Chybná posloupnost odečtení size a návratu z neúspěšného fwrite je však
stejná a stejný invariant pro n≤256 ji dokazuje. PDF nebylo vydáváno za
byte-identické zdrojům. Fyzický výtisk MMIXware nebyl zkontrolován.

Deset vrstev oprav a jejich hashe jsou v `results/errata-S0005.json`.
Všechny nalezené kontexty byly přečteny: oprava fasciklu p42 mění
„error“ na „serious error“ u Fread, nikoli u Fwrite; MMIXware p42 řeší
TRAP kontext a store protection. Aktuální veřejné opravy ani hledání
Fwrite/mmix_fwrite/short write neukázaly odpovídající opravu. To není
tvrzení světového prvenství.

`verify_fwrite_short_count.py` přeloží pouze jednou společný původní
modul a zvlášť auditní opravu. Každý dostane šest přesných krátkých
návratů fwrite, čtyři kontroly (jednobytový/plný víceblokový úspěch,
nulová délka, chybný mode) a jeden skutečný Linux zápis na stderr
přesměrovaný do /dev/full. Délky jsou nejvýše 600 bytů.

Stub modeluje jen návrat a úspěšný počet, které mmix_fwrite pozoruje.
Skrytý C stream error flag lze doplnit v souladu s krátkým návratem;
rutina ho nečte. V JSON je proto u mock případu flag null, nikoli
tvrzení, že chyba nenastala. Skutečný libc případ má pozorované
fwrite=0 a ferror=1. Přesný uint64 model helperů je modulární,
nevkládá vlastní logiku Fwrite do orákula. Expected je vždy součet
skutečně přijatých bytů minus S.

První pokus dokončil 11 původních volání, ale následný ctangle opravy
selhal: krátké @x kontexty našly jiné dřívější rutiny. Tehdejší skript
ukládal až na konci, takže tyto výsledky nebyly trvale zachovány a
nejsou použity jako evidence. Záznam je v `results/fwrite-short-count-attempts.json`
a samostatném build-diagnostic. Kontext opravy byl ukotven unikátní
hlavičkou funkce a ukládání přesunuto po každém buildu a volání.

Následný krátký `nice -n 15` běh uložil **22 volání a 4 úspěšné build
kroky**. Původní modul má sedm rozporů a čtyři správné kontroly; auditní
oprava souhlasí ve všech jedenácti případech. Skutečný stderr witness
vrací v originálu 0 a v opravě −1. `results/fwrite-short-count.json`
obsahuje všechny hodnoty i blokové stopy, build soubor všechna přeložení.
Celkem bylo v novém verifieru 33 volání včetně prvního neuloženého
pokusu; žádný starší audit ani dlouhá enumerace nebyly opakovány.
Reprodukce doplňuje obecný důkaz výše, nenahrazuje jej.
