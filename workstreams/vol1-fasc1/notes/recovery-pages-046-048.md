# Úplný rozsah file 46–48 / p38–40 — výrazy, assembler a volání I/O

Celé tři stránky byly přečteny znovu, po odstavcích a po každé položce
pravidel. V0098–V0101 se zde doplňují o přesné meze a skutečné větve
parseru. Definice jazyka se porovnávají s primární definicí MMIXAL;
netvrdí se úplná korektnost všech nesouvisejících částí assembleru.
Na file47 zůstává jedna konkrétní programová povinnost popsaná níže.

## File 46 / p38

**Dokončení pravidla 3.** Předdefinované symboly hardwaru a I/O jsou
explicitní tabulky v MMIXAL; primární text 225–244 dovoluje změnit jejich
význam a následně je používá jako obyčejné symboly. „Should not appear“
je doporučení jediného definičního výskytu. Nesmí být zaměněno za silnější
diagnostický výrok z p35, který již vyvrací C0017. Dvojice typů pure
(64 bitů bez znaménka) a register (konečný symbolický ekvivalent 0..255)
se shoduje s deklarací typů a kontrolou rozsahu. Register value není
obsah procesorového registru.

**Pravidlo 4, všechny alternativy.** Symbol a konstanta dodají svou
hodnotu; @ je čistá aktuální adresa; závorky vyhodnotí celý vnitřní výraz;
unární operátor pracuje nad bezprostředně následujícím primary, takže
se může řetězit. + je identita, − je 0−x modulo 2^64, ~ je doplněk
všech 64 bitů a $ změní typ čísla. Primární MMIXAL:246–273 uvádí
přesně tyto čtyři operace a navíc systémový serial operator &, jenž
není v tomto záměrně zkráceném přehledu. U defined register symbolů
se dodržuje 0..255; větší dočasné register expressions nejsou novým
procesorovým registrem.

**Pravidlo 5, všechny operace a meze.** Primární definice 274–301
uvádí unsigned významy *, /, //, %, <<, >>, &, +, −, | a ^ ve
stejných dvou skupinách. Součin, součet, rozdíl a levý posun jsou
modulo 2^64; pravý posun je floor(x/2^y). / a % vyžadují y>0.
Pro fractional division x<y plyne y>0 a 0≤floor(2^64 x/y)<2^64;
výsledek tedy přesně patří do pure oboru. Při x≥y je buď dělení nulou,
nebo výsledek nejméně 2^64, takže uvedený zákaz má přesnou mez.
Posuny y≥64 dávají nulu v obou směrech, což plyne z těchto definic;
samostatná parserová větev tuto mez skutečně používá.

Term je levě asociativní řetěz primaries se strong operacemi, expression
levě asociativní řetěz termů s weak operacemi. Tím vznikají právě
(a/b)/c a (a−b)+c. Pole precedence a scan_close v MMIXAL:2298–2504
odpovídají definici: před vložením nové operace se provede každá stará
operace s alespoň stejnou prioritou. Menší priorita se uloží a čeká.
Levá závorka vytvoří hranici, jejíž odstranění nastane jen na odpovídající
pravé závorce. Invariant je: value stack nese již zpracované souvislé
podvýrazy, operator stack dosud odložené vazby nad nimi. Unární operace
spotřebuje jednu hodnotu, binární dvě a nahradí je jednou; uzavření
termu proto nenechá nevyhodnocenou stejně silnou vazbu. To dokazuje
právě pořadí operací, nikoli obecnou korektnost všech aritmetických
helperů či všech chybových vstupů assembleru.

Konkrétní příklad má dvě terms (#ab<<32) a (k&~(k−1)), uvnitř druhé
jsou dvě primaries. Pro k=#cdef00 je nejnižší nenulový bit 2^8:
poslední byte je 00 a byte ef je lichý. Odečtení 1 nastaví spodních
osm bitů na 1, vymaže bit8 a vyšší bity nezmění. Bitové AND s doplňkem
tedy ponechá právě #100. #ab·2^32+#100=#ab00000100. Důkaz V0098 má
stejný obor a zde se přebírá celý, nikoli jen numerický výsledek.

Register výjimky jsou přesně register+pure, pure+register,
register−pure a register−register; poslední dá pure. Proto $1+2=$3
a $3−$1=2. Znaménko ani aritmetika obsahů registrů se neuplatňuje.
Ve zdroji plus/minus odmítají jiné směsi a strong operace vyžadují
pure. Future symbol zůstává undefined až do definice; binary + odmítne
undefined, takže 2F+1 je nepřípustné bez ohledu na budoucí číselný výsledek.
Identity unary + či závorky nejsou kombinací s jinou hodnotou a primární
definice je připouští. Případ 2F+1 tím není oslaben.

**Pravidlo 6 a začátek 7.** LABEL/OP/EXPR a comma list se shodují
s primární syntaxí. LABEL zahrnuje i speciální lokální nH již definované
na p35. Blank EXPR se změní na jedinou nulu ve větvi kopírování operandů;
nejde o seznam bez položek. OP je instrukce nebo zde uvedená pseudo-op;
aliasy jsou jména stejných strojových operací. File46 končí pouhým
uvedením následujícího tříkrokového pravidla a nic dalšího se nepřeskakuje.

**Stav file46:** všechny odstavce, podbody i numerický příklad mají argument.

## File 47 / p39

**Pravidlo 7(a–c).** Pro t=2,4,8 je zarovnání
((p+t−1) mod 2^64)&(−t). Pokud nenastane přechod přes 2^64, je to
t·ceil(p/t); na horním okraji je výsledkem 0. Staré tvrzení V0100
„vždy ≥p“ se tím výslovně omezuje na obyčejný číselný interval.
V obou případech se přidá nejmenší d∈{0,…,t−1}, která dává t|p+d,
a výsledek je platná 64bitová adresa. MMIXAL:2684–2692 dělá právě
tuto operaci před definicí LABEL i před vyhodnocením operandového @.
OCTA/TETRA/WYDE mají t=8/4/2, instrukce t=4. BYTE, IS, GREG a LOC
žádné další zarovnání nevyžadují. Běžný label dostane již zarovnanou
adresu, IS a GREG níže uvedený ekvivalent. assemble pro tetrabyte
zvýší cur_loc o 4 modulo 2^64; výsledek je opět zarovnaný.

ADD má tři pole: X,Y jsou register 0..255, Z je register nebo pure
0..255. V pure větvi se základní #20 zvětší o 1, tedy #21. Čtyři
byty mají nepřekrývající se bitové pozice OP<<24, X<<16, Y<<8, Z.
SETH má X register a YZ pure v 0..65535, tedy přesně dva byty.
Skutečné Do X/Y/Z a Do two-operand branches provádějí tato rozlišení
a kontroly rozsahu. Jde o stejné bitové obory jako v dříve uzavřené
instrukční definici, nikoli pokus odvodit je jen ze dvou příkladů.

BNZ s počtem tetrabytů k v −65536..65535 kóduje k≥0 přímo do YZ;
pro k<0 použije backward opcode a YZ=k+65536. V obou případech
instrukční sémantika vrátí právě @+4k modulo 2^64 a 0≤YZ≤65535.
Naopak každý povolený byte-pár a volba směru dají právě tento rozsah.
Target musí být stejně jako @ násobkem 4. Tím je matematická věta
o rozsahu úplně dokázána.

**Konkrétní dosud neuzavřená implementační hranice, R0006.** Pro
@=#7ffffffffffffffc a target=#8000000000000000 je běžný rozdíl adres
4, tedy k=1. Známý operand MMIXAL:2984–3005 i JMP:3080–3101
však nejprve obě adresy aritmeticky posunou doprava o 2 a potom
odečtou. Dostanou −2^61−(2^61−1)=−2^62+1, což odmítnou jako příliš
vzdálený target. Future fixup:2790–2814 odečte nejprve a pak posune
4 na 1, tedy stejný cíl přijme. Primární smlouva :410–420 výslovně
stanoví rozdíl adres dělený 4 a stejnou podmínku pro future hodnotu.
Nejde o původně zvažovaný wrap #ffff…fffc→0: ten aritmetický posun
naopak zpracuje správně jako −1→0. Zde zůstává samostatné ověření
originálu/oprav a případné malé reprodukce programové chyby; správná
knižní matematická definice se červeně neoznačuje. Strana47 zůstává
do uzavření této přesné povinnosti partial.

Dvouoperandová memory forma vyžaduje zachovanou base hodnotu b
v registru Y a pure z∈0..255 s A=b+z modulo 2^64. Immediate instrukce
pak vypočte právě A. Primární postup hledá mezi nenulovými GREG
nejmenší unsigned rozdíl A−b; pokud je některý v 0..255, vybraný
nejmenší je také v tomto rozsahu. To je úplný argument existence
volby v popsaném oboru. Alternativní volba -x pro expanzi je mimo
tento standardní jednoinstrukční kontrakt, nikoli opomenutá větev.

**Pravidlo 8(a–d).** IS dává symbolu hodnotu i pure/register typ
jediného výrazu a nerezervuje paměť. GREG pracuje s jednou pure
hodnotou x. Nula vždy vyžádá nový registr; nenulové x nejprve hledá
identickou již přidělenou hodnotu, jinak sníží greg o 1. Při greg=32
další alokaci odmítne. Indukcí jsou dosud použité globální registry
souvislý interval greg..254, takže nový greg−1 je největší dostupný
registr. Opakovaná nenulová konstanta sdílí stejnou base. Upozornění
neměnit tento registr je podmínkou budoucí adresní substituce b+z;
není tvrzením, že hardware nedovolí registr změnit.

LOC přiřadí @ hodnotu x. Label T vznikne před touto změnou, takže
`T LOC @+1000` označí původní p a nový ukazatel je p+1000 modulo
2^64. Vynechá se přesně 1000 adres, ale instrukce do nich sama
nezapisuje; nepředpokládá se vymazání již překrývajících se dat.
BYTE/WYDE/TETRA/OCTA mají n=1/2/4/8 a každý operand musí být pure
v [0,2^(8n)−1]. Příslušné n bytů stačí a jejich big-endian rozklad je
jednoznačný. Pole k zkontroluje přesně horní bity mimo tento rozsah;
OCTA dovoluje všechna pure octa i budoucí odkaz podle pravidla9.

**Pravidlo 9, celý argument jednoho průchodu.** Za předpokladu konečného
syntakticky platného vstupu, dostupných tabulek/bufferů a později
definovaných future symbolů lze každý nedefinovaný operand nahradit
nulovým polem a připojit k symbolu záznam (adresa,podtyp). Povolené
podtypy jsou OCTA, 16bitový YZ relativní a 24bitový XYZ relativní.
Žádný dosud neznámý výraz není nutné znovu parsovat: obor dovoluje
jen jediný future symbol, ne aritmetiku s jeho budoucí hodnotou.

Invariant seznamu pp->link v MMIXAL:1522–1548, 2771–2814,
2871–2881, 2971–2981 a 3067–3077 je přesně množina dosud nevyřešených
výskytů daného symbolu. Nový výskyt přidá jeden uzel a nulové pole.
Definice odebere každý uzel právě jednou a vydá fixup objektu, pak
nastaví stav defined. Budoucí lokální nF mají vlastní seznam; nH
vyřeší starý seznam před přechodem na nový lokální význam. To zachovává
pravidlo nejbližšího následujícího nH, včetně opakovaných lokálních čísel.
U nedefinovaného symbolu na konci místo nepravdivé hodnoty nastane chyba.

OCTA fixup vloží budoucí pure octa do původně nulového pole. Relativní
fixup vypočte d=(target−source)/4, zkontroluje stejný dovolený rozsah
a zakóduje jej do nulového displacement; backward příznak je XOR
jedničky do opcode. Instrukční pole jsou disjunktní a každý výskyt
má právě jeden uzel, takže se cizí pole nepřepíší. Při legálních
overlapech loader XOR kombinuje každý příspěvek právě jednou, jak
bylo dokázáno v recovery-pages-041-045.md. Každý výskyt stojí jednu
alokaci a jednu pozdější fixup operaci; F výskytů tedy O(F) této
práce a nejvýše F živých uzlů. Symbol lookup a načítání znaků mají
vlastní cenu, kterou tvrzení neudává. Jeden průchod **zdrojovým
textem** neznamená absenci loaderu nad vzniklým objektem.

Tím je motivace „quickly in one pass“ konstruktivně doložena, bez
neoprávněného tvrzení konstantní ceny celého assembleru nebo programu
s nedostatkem hostitelské paměti. Nově nalezená známá-target hranice
je odlišná od tohoto důkazu existence a invariantů future fixupů.

## File 48 / p40

**Figure15, všechny viditelné řádky.** Úvodní % je komentář; L IS500
a t IS$255 zachovávají dříve odvozené ekvivalenty. `n GREG ;;`
má prázdný operand, proto 0, a druhý semicolon zahájí comment řádek.
`q GREG /* Quotient */` a `r GREG // Remainder` jsou konkrétními
případy scanneru :2351–2375: první opening token / není začátkem
výrazu, takže celý operand se změní na 0. Není potřeba předpokládat
úplný C/C++ komentářový parser. `jj GREG 0 Index…` už má explicitní
operand a zbytek za mezerou se zahodí. Výpustka představuje vynechané
řádky, nikoli nový příkaz. PBN, LDA/TRAP a závěrečné CMP/PBNZ/TRAP
mají stejné argumenty a účinek jako odpovídající řádky plného P,
jejichž invarianty jsou v recovery-pages-041-045.md.

**Celý popis formátu.** Scanner :2618–2682 začne LABEL přesně na
počátku řádku nebo těsně po semicolonu; počáteční mezera znamená
blank LABEL. OP začne prvním dalším nonblank a skončí mezerou.
Operandová část skončí mezerou či semicolonem, kromě znaků uvnitř
char/string konstant. První neplatný znak labelu vyřadí comment;
při počátečních mezerách dojde prázdný OP na stejný bypass. Po operandové
části se další instrukce zpracuje jen při semicolonu. Má-li mít nová
instrukce label, nesmí před ním být mezera, protože právě ta znamená
prázdný LABEL. To dokazuje všechny uvedené varianty včetně posledního
trailing semicolonu. Hodgepodge a čitelnost jsou stylistická doporučení,
nikoli další matematický či výkonový výrok.

**Odkaz na MMIXware.** Skutečný zdroj obsahuje úplnou primární definici
i parser/assembler, včetně zmíněných dalších systémových prostředků
PREFIX, LOCAL a BSPEC/ESPEC. Existence tohoto dokumentu byla přímo
ověřena; není z ní vyvozená bezchybnost každé implementační větve.

**Začátek primitive I/O a obě calling sequences.** SET $255,arg předá
parametr přes globální registr a byte fields TRAP nesou function a
handle. Označení „usually“ dovoluje alternativní načtení pointeru:
GETA $255,String v H dává dříve prokázanou adresu textu. Fputs=7,
StdOut=1 a přímý string pointer se shodují s MMIX-SIM dispatcherem
a popisem funkce. Program P používá stejný kontrakt. Nad těmito
primitivami lze vytvořit složené služby postupným voláním, avšak text
nepředkládá konkrétní vyšší službu vyžadující další algoritmický důkaz.
Chyby jednotlivých služeb jsou mapovány na file49–51; stručný příklad
úspěšného výstupu tu netvrdí úplný error handling ani identitu adresy
arg s adresou souboru.

**Stav file48:** všechny položky Figure15, každý odstavec a obě
calling sequences mají vlastní argument. Bez nového běhu. File46/48
jsou úplné; file47 má pouze přesně uvedenou R0006 implementační mezeru.


### Uzavření R0006

Výše uvedená pracovní programová povinnost je nyní uzavřena v MMIX-S0007-relative-address-boundary.md: úplný důkaz, obě původní větve, původní sazba,11vrstev a39malých sestavení. File47 má po tomto doplnění úplné argumentové pokrytí; správná knižní definice nemá error.
