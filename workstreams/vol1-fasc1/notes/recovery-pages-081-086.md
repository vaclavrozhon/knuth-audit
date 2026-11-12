# Obnova úplného rozsahu: file 81–86 / p. 73–78

Každý odstavec úvodu, oba druhy interpretačních příkladů, celý datový
layout a všechny řádky 001–054 jsou přiřazeny k argumentu. Odpovědi
korutin 5–7 na začátku 81 jsou již uzavřené v
`exercises-1.4.2-006-007-recovery.md` a `recovery-pages-075-080.md`;
jejich programy ani běhy se neopakují. Žádný nový běh simulátoru,
žádný nový nález. Starý V0144 se nyní uzavírá přesným převzetím
profilu Programu P a kontrolou skutečné koncové cesty.

## 1. File 81: vymezení, přenositelnost a diagnostika

Definice „machine-like“ je výslovně neostrá. Určuje účel programu,
který dekóduje instrukci a provede její operaci, nikoli rozhodnutelnou
nutnou a postačující vlastnost všech programů. Písmena a)/b) rozlišují
kompaktní popis činnosti a rozhraní mezi průchody; konkrétní konstrukce
na 82 dokládají jejich možnost. Není tvrzena globální optimalita
každé takové reprezentace.

Přenositelnost má přesný předpoklad: oba hostitelské interprety
realizují stejný virtuální stav, aritmetiku, paměť a vnější rozhraní.
Mají-li při prvním kroku odpovídající stavy a stejný vstup, provedení
stejné virtuální instrukce dá opět odpovídající stavy a výstup. Indukce
po každém konečném prefixu dává nezměněný virtuální program a jeho
chování; přizpůsobuje se interpret včetně vazeb na zařízení. Nejde
o tvrzení, že libovolná závislost na hostu automaticky zmizí.

Společný bod před dekódováním zpřístupňuje další kód i celý virtuální
stav. Kontrola předpokladu, výpis či zastavení v tomto bodě je
konstruktivní podklad pro diagnostické možnosti. Samostatné úplné
provedení trasovače žádá až úloha 22 a tímto odstavcem se neuzavírá.

Historická priorita prvních interpretů, četnost jejich používání,
jejich růst a hodnocení schopností „today's expert programmers“
zůstávají výslovnými faktografickými výjimkami V0141. Odkazy na
kapitoly 8/10 jsou plán série v tomto vydání, nikoli kontrola
nepřítomného vydaného pokračování. Přebírá se přesně tento rozsah
§1 z `workstreams/vol1/notes/quality-recovery-section-1.4.3.1-2026-11-07.md`,
ne důkazy tamního MIX simulátoru nebo jeho počty.

## 2. File 82 a začátek 83: všechna schémata a prameny

Deset kategorií každého ze dvou uspořádaných operandů dává přesně
100 případů. Indexování tabulky touto dvojicí vybere správnou obsluhu.
Bytový opcode dovoluje 256 různých kódů; do MMIX octabytu se vejde
osm takových bytů. Výrok „ideally fits in a single word“ je podmíněný
návrh pro dostatečně krátké programy, nikoli věta, že libovolných
100 úloh lze vyřešit osmi instrukcemi na úlohu. Typ operandu určí
teprve příslušné potřebné činnosti, ne univerzální minimální délku.

Převedení posloupnosti volání na kódy a argumenty je správné, pokud
dekodér vybere stejnou obsluhu a její parametry. Při větvení se navíc
přenese stav řízení a cíle. Indukce po virtuálních instrukcích pak
prokáže stejnou posloupnost stavů; opačný překlad rozvine každý kód
na totéž volání. Úspora místa je podmíněna kratším kódem/argumenty
oproti přímému volání. Víceprůchodové schéma obdobně předá následujícímu
průchodu příkazy s definovanou sémantikou. Není tím dokázáno slovo
„most efficiently“ pro každý jazyk ani empirická četnost takové výhody.

Přesné zdrojové výsledky, včetně SHA256, jsou v
`results/interpreter-introduction-sources.json`. Z již uloženého
peerova pramenného bloku se přebírá pouze skutečně stejný obsah:

* Randell–Russell, *ALGOL 60 Implementation* (1964), p. 34–36,
  file 49–51: objektový jazyk Whetstone interpretuje Control Routine.
  Peer při obnově X1016 znovu četl obrazy 34–35 i text 36. Je to
  přesný důkaz tohoto odkazu, nikoli kontrola celého překladače.
* Knuth, CACM 6(9), 555–563 (1963), a Evans, Annual Review in
  Automatic Programming 4, 87–124 (1964): primární metadata ověřena,
  plné články vracely 403. Jejich konkrétní obsahové příklady zůstávají
  bibliograficky přeskočené; nepřebírá se obsah z titulku.
* Autorský `tex.web`, celý modul 545, obsahuje čtyřbytové
  `lig_kern` instrukce, test následujícího znaku, řízení přes skip,
  ligature/kern operace, nepřímý start i stop. To přímo dokládá
  malý interpret. Část 31 / modul 583 definuje DVI jako proud kódů
  s parametry a výslovně připisuje formát Fuchsovi v roce 1979.
  Potřebné části byly přečteny včetně konce modulu 545. Je to
  následnický primární zdroj; přesná sazba *TeX: The Program* 1986
  nebyla získána. Samotná historická atribuce se opírá o autora,
  nikoli o nezávisle rekonstruovaný archiv vývoje z roku 1979.
* Oficiální `dvips.texi`, titul, autorství a část *Invoking Dvips*,
  uvádí Tomase Rokického a převod DVI na PostScript. Pro tento
  přesný obsah je primární následnický zdroj dostačující; historický
  binární soubor ani výrobní workflow tohoto exempláře se netestují.
* **Přesně citované třetí vydání Adobe z roku 1999**, nikoli druhé
  z roku 1990: zobrazen titul, copyright/first printing February
  1999 a §3.1 na p. 24 / file 38. Interpret skenuje proud znaků
  nebo vykonává pole objektů, rozlišuje jejich typ/atributy/hodnotu
  a jména vyhledává ve slovníku; operátory realizují činnosti.
  Zdroj je původní Adobe PDF už uložené vedle peerova druhého vydání.
  Vlastní zobrazené obrazy jsou `images/postscript1999-file-001.png`,
  `-002.png` a `-038.png`.

Kompozice TeX→DVI→dvips→PostScript→tisk zachovává výsledek za
předpokladu správnosti jednotlivých překladů a interpretačního
rozhraní. Tato kapitola je neimplementuje a nežádá nový důkaz
celého TeXu nebo tiskárny. Skutečná cesta konkrétních knižních desek
zůstává autorovým svědectvím. Výroky o historické hodnotě mikrokódu
a specializovaných obvodů jsou kvalifikované faktografické výjimky.

## 3. Zbytek file 83: režie, emulace a účel příkladu

Je-li cena dekódování a výběru d a obsluhy t, podíl režie je
d/(d+t). Pro t výrazně větší než d je malý, což přesně dokládá
možnost uvedenou kvalifikovaným „often“. Není to obecná mez pro
simulaci každé jednoduché MMIX instrukce. Diagnostika a nezávislost
mají výše určené předpoklady.

Simulator/emulator označuje zde interpret jazyka jiného stroje.
Pozdější rozlišení od simulace diskrétních systémů je vymezení
účelu modelu. Historická tvrzení o nákladech přeprogramování,
autorovo pětinásobné zrychlení a skutečný příběh A→B→C nejsou
nezávisle ověřené benchmarky. Řetězové interpretování je proveditelné
kompozicí přechodových relací, ale samotná písmena A,B,C nedokazují
konkrétní zpomalení. Text tato hodnocení uvádí jako autorův názor.

Tři pedagogické důvody a)–c) nejsou nové výkonnostní věty. Delegování
aritmetiky na hostitelské MMIX znamená převzetí jeho architektonického
kontraktu. Neznamená důkaz bezchybnosti každé doprovodné C implementace;
programové S0001–S0008 zůstávají oddělené. Přijaté obecné důkazy
register stacku, PUSH/POP a SAVE/UNSAVE se později převezmou přesně,
ne znovu odvozují z těchto motivačních vět.

## 4. File 84: přesný model a úplné rozhodnutí času Programu P

Simulují se sekvenční user instrukce s uvedenými rudimentárními
I/O trapy. Pipeline, cache, překlad virtuálních adres, privilegované
operace a ostatní dynamické trapy jsou výslovně mimo model. Není
nutné dokazovat jejich realizaci v hypotetickém hardwaru. Odkaz na
existující širší metasimulátor dokládá původní `mmix-pipe.w` v uloženém
balíku 2025: jeho úvod definuje `MMIX_run`, pipeline a dynamické
plánování. Uložen `sources/mmix-pipe-20250620-introduction.txt`, přesně
prvních 125 řádků; není deklarován audit jeho vlastní správnosti.

Vstupní binární obraz popisuje počáteční paměť uživatelského kontextu.
Zamýšlený pozorovatelný stav tedy tvoří virtuální registry, paměť,
PC, exception/trip kontext a I/O; skutečné registry programu simulátoru
jsou oddělené. Global obsahuje 256 octabytů. Prvních 32 může sloužit
special registers, protože dostupné globální obecné registry mají
index alespoň G≥32. Sedm special registers uložených samostatně
se před GET/SAVE synchronizuje podle pozdějšího explicitního kódu;
tato úvodní věta neříká, že oba jejich obrazy musí být shodné po
každé pomocné hostitelské instrukci.

Hodiny jsou jedna lineární kombinace 2^32·μ+υ modulo 2^64, nikoli
dvě neomezená oddělená počitadla. Nízká část se u dlouhého běhu může
přenést do vysoké. V konkrétním příkladu se to nestane.

Přesný profil Programu P je již uzavřen v
`MMIX-C0016-program-p-mems.md` a `results/program-p-profile.json`:
první fáze 10037μ+641543υ, druhá 2803μ+124559υ včetně závěrečného
TRAP Halt. Celkem tedy 12840μ+766102υ. **Závěrečný Halt obchází
Update:** `Trap` vybere `SimHalt`, instrukce je nulová a `BZ inst,Exit`
jde přímo na hostitelský `TRAP 0,Halt,0`. Už se nepřičte jeho
tabulkových 5υ. Zbylé TRAP Fputs končí přes TrapDone→Update a jejich
cena se započítá právě jednou. Program P nepoužívá lokální stack,
SAVE ani aritmetické trips; jeho globální registry a meze jsou již
dokázané v `recovery-pages-041-045.md`.

Také počáteční pomocný UNSAVE se nezapočte: při bootstrapu je
uu=0 a resuming=1. Konec Unsave po obnově kontextu proto přejde
přes `PBNZ uu` a `BZ resuming` na `AllDone`, nikoli `Update`.
`AllDone` zruší příznak resuming, protože vložený opcode není
RESUME. Počáteční cc zůstane nula. Tyto větve jsou v byteově
shodných `sim-20131017.mms` a `sim-20250620.mms`, konec Unsave
a SimHalt/Update. Žádný skrytý příspěvek inicializace nezbývá.

Výsledkem je přesně 12840μ+766097υ, tedy high #3228 a low #bb091,
jak uvádí stránka. V0144 již není partial pro historický benchmark:
numerický výrok je rozhodnut z dříve uzavřených konečných certifikátů
a skutečných řídicích větví. Autorův fyzický běh se netvrdí ani
znovu nereprodukuje.

Ring o ρ položkách stojí 8ρ bytů; větší ring může omezit počet
spill/load při vhodném programu, ale text správně říká „might“.
ρ≥256 a mocnina dvou jsou podmínky pozdějšího modulo invariantu.
Každý navržený konečný layout navíc musí zapadnout do hostitelské
adresní oblasti a ponechat potřebnou paměť; „higher power“ se
nevykládá jako existence nekonečné fyzické paměti.

## 5. File 85: každý byte layoutu a doména MemFind

Řádky 001–012 dávají pro D=2^61 Global=[D,D+2047], dále
Local=[D+2048,D+2048+8ρ−1], dva octabyty IOArgs a potom Chunk0.
Při ρ=256 je Chunk0=D+4112; všechna pole jsou disjunktní a
octabyte-aligned. Nenulové GREG g,l a báze IOArgs mají různé adresy.
`LOC #100` přesune pouze sestavovací adresu, nikoli obsah či živé
registry. $255 je volatilitní scratch podle deklarovaného kontraktu.

Nelze injektivně uložit všech 2^64 nezávislých bytů do 2^61 bytů.
Simulátor ukládá jen navštívené chunky; user-only rozsah navíc
odmítá záporné virtuální adresy. Pro C=2^12 je A=key+offset,
key=A&~(C−1), offset=A&(C−1). Horních 52 bitů vybírá chunk,
dolních 12 pozici. Totéž platí pro každou mocninu dvou C≥8,
za předpokladu přípustné velikosti hostitelského layoutu.

Node má KEY v bytech 0..7, LINK v 8..15, DATA v 16..C+15 a
nulový padding v C+16..C+23, tedy C+24=4120 bytů. Node i DATA
jsou zarovnané na osm. Je-li R=head+16+offset, pak
floor(R/8)·8=head+16+floor(offset/8)·8. To je přesný hostitelský
obraz M8[A]; poslední přípustný začátek octabytu je offset C−8.
Žádný zarovnaný octabyte přes hranici DATA nepřeteče. Pro kratší
aligned load/store platí stejný argument s 1,2 nebo 4. Padding
není součást virtuální paměti sousedního chunku.

Počáteční node je nulový a head=Chunk0, curkey=0, alloc=Chunk0+4120.
Nulovost nepoužité paměti je doložena skutečným `new_mem` přes
calloc v `mmix-sim-20250620.w` 744–751, viz již uzavřený
`exercises-1.3.2-030-031-recovery.md` §4. Simulátor své nové bloky
neinicializuje opakovaně, proto důkaz vyžaduje dosud nepoužitou
nepřekrývající se oblast bez přetečení alloc. Před dosažením Pool
to jeho layout splňuje. Úloha 4 již dokládá přesnou kapacitu
559670633304293 plných uzlů a zbývajících 2680 bytů z uloženého
`results/node-capacity4.json`; podíl ani žádný průchod se neopakuje.
Praktický komentář o lidském životě není univerzální časovou větou.

Move-to-front udržuje pořadí podle posledního použití indukcí:
head hit nic nemění, jiný hit odstraní právě tento node a vloží
jej před dosavadní pořadí, nový key analogicky přidá dosud neexistující
node. Historická frekvence locality se z toho neodvozuje; pro cyklické
použití mnoha chunků může být seznam opakovaně dlouhý. Kniha svou
motivaci výslovně podmiňuje podobností budoucnosti s minulostí.

## 6. File 86: každá větev MemFind a řádek 013–054

PREFIX vytvoří vlastní namespace `Mem:`; `:t` odkazuje na vnější
scratch a `:MemFind` exportuje vnější vstup. Závěrečné PREFIX :
vrací původní namespace. Local aliasy $0..$4 a konstanty KEY/LINK/
DATA nepřekrývají živé hodnoty v rozporu s použitím: addr v $0
se přepíše až po získání offsetu; p a newlink vzniknou pouze při
search větvi. GREG nuly jsou samostatné proměnné, nodesize/mask
jsou různé nenulové konstanty.

Při vstupu je seznam konečný, acyklický, s různými keys; head není
nula, curkey=KEY(head), a všechny keys jsou nezáporné. 029–031
vypočtou správný key a head hit. Při neshodě 032 odmítne A<0
ještě před změnou seznamu. Proto indukčně nikdy nevznikne záporný
cached key a rychlá větev tuto kontrolu nemůže obejít.

Po 033 je newlink původní head. V 034–036 je p předchůdce právě
zkoumaného head. Každá neúspěšná 041–043 přesune hledání přes jeden
další node; počet zbývajících nodes přísně klesá. Při shodě se
skončí u právě jednoho existujícího key. Při nulovém LINK nastaví
037–040 head na čerstvé alloc, zapíše jeho key a posune alloc
o nodesize. Ostatní pole čerstvého node jsou nulová z výše doložené
inicializace. Důkaz nepožaduje, aby MemFind procházel virtuální
adresy vzestupně; libovolné pořadí dává stejný key lookup.

Označme nalezený/nový node M, jeho předchůdce P a původní následník
N=LINK(M). Řádky 044–047 provedou M.LINK=old_head a P.LINK=N,
head=M, curkey=KEY(M). Ostatní odkazy zůstávají, takže žádný node
nezmizí, nezdvojí se ani nevytvoří cyklus. Pro nový M je N=0 a
P je původní poslední node, proto tytéž instrukce fungují i bez
předchozího dočasného připojení nového M do seznamu.

048–050 vrátí head+16+(A−key), správný R z předchozí části.
`res=$2`, `arg=$3` a `PUSHJ res,MemFind` chrání staré $0,$1
volajícího, předají A jako callee $0 a `POP 1,0` přenese právě
výsledný R do res. Živá data volajícího nesmí bez uložení používat
volatilní $255; tuto podmínku následující helpers splňují oddělením
skutečného a simulovaného rJ. Záporný Error končí místo návratu,
což je součást výslovné user-only domény.

Deklarovaná cena se přebírá přesně z celého větveného důkazu C0009:

`9υ+(2μ+8υ)C+(3μ+6υ)U+(2μ+11υ)A`,

kde C počítá skutečná porovnání v 042, U=[key≠curkey] a
A=[alokace]. Head hit má C=U=A=0; jiný hit U=1,A=0,C≥1;
alokace U=A=1,C≥0. Platí 0≤A≤U≤1. Tento vzorec zahrnuje
POP a všechny větvové penalizace, nikoli volající SET/PUSHJ.
Chyba záměny U/A na answer page 125 zůstává samostatný C0009;
záměna jmen neopravuje nedoložené historické průměry. V tomto
bloku se starý rozpis ani běh nezopakoval.

Závěrečný odstavec definuje logický stack se všemi τ položkami,
včetně současných L lokálních. Jejich pozice τ−L až τ−1 jsou
právě posledních L prvků. V jiné konvenci, která počítá pouze
pushed část, je její délka τ−L; nejde o jiné přeznačení registrů.
Podrobný ring začíná až na následující stránce.

## Výsledek rozsahu a použití vzorů

File 81–83 jsou celé zmapované s přesnými historickými/pramennými
výjimkami; jejich technické transformační argumenty jsou doložené.
File 84–86 mají úplné argumentové pokrytí vlastního obsahu.
V0144 je nyní argument_recorded, V0141/V0143 zůstávají partial
jen v konkrétním výše uvedeném faktografickém rozsahu. Odpovědi
124–134 se tím celé neuzavírají; kapacitní rekurzivní C0010 a
další specifické úlohy zůstávají samostatně evidované.

Ze vzoru binomické nerovnosti je přenesen přesný obor a oddělení
správného výsledku od chybných mezikroků: časový součet vyžaduje
rozlišení Halt a bootstrapu. Ze vzoru Algorithm R je převzato
počítání skutečných cest, nikoli jmen rutina či neprovedené práce.
Ze vzoru kografů oddělení obecného invariantu a všech povolených
stavů od empirické locality nebo příběhu o jediném programu.
