# MMIX — úplný rozsah rejstříku a prázdného listu 135–143

Rozsah je celých osm stran rejstříku, file135–142 / p127–134,
a prázdný list143. Všechny řádky obou sloupců byly přečteny.
`results/index-entry-inventory.json` uchovává každý obsahový záznam
v pořadí původního PDF; `sources/index-raw-135-142.txt` je přímá
extrakce v pořadí sloupců. Porovnání zřetězeného obsahu každé strany
ověřuje, že inventura žádný neprázdný obsahový znak neztratila
(ignorují se jen mezery, záhlaví, foliace a vlastnické zápatí).

Inventura má 793 záznamů včetně úvodního odstavce a nadpisu Notational
conventions, nikoli 793 nezávislých matematických vět. Rozsahy odkazů
jsou rozepsány na 1628 jednotlivých lokátorů. Všechna čísla patří
do skutečného rozsahu knihy. To **není důkaz relevance všech odkazů**.
Tečka nad monus v sazbě vytvořila falešný konec extrahované položky;
obě části byly sloučeny po zobrazení originálu
`images/index-file139-p131.png`. Původní znaky jsou zachované.
Poškozené OCR cizích písem není označeno jako chyba knihy.

## V0181: celý technický slovníček

Každá následující položka má stejný význam a obor jako uvedený důkaz;
nejde o rozšíření těchto důkazů na další implementace.

* File135: symboly μ a υ definují deklarovaný nákladový model
  (V0076 a `notes/recovery-pages-024-033.md`), νx počet jedniček
  (V0049 / úplný SADD), φ zlatý řez (úlohy24 a Fibonacciho rozbor).
  Bit je prvek {0,1}; byte order „big-endian“ určuje sestupné váhy
  v již doloženém pozičním rozvoji V0010–V0014. Associative law pouze
  **definuje** rovnost obou závorkování; netvrdí, že každá operace
  v MMIX je asociativní. Přesný model MOR/MXOR je V0050–V0053.
  #100 a #f0 jsou standardní a alternativní počáteční místo podle
  `notes/recovery-pages-037-040.md` a
  `notes/recovery-pages-098-101-124-134.md`; neříkají, že libovolný
  nulový obsah #f0 je příznakem absence programu.
* File136: byte má osm bitů. Commutative law pouze definuje
  a◦b=b◦a; nečiní žádnou novou univerzální komutativní domněnku.
  Byte difference a příbuzné názvy odkazují na již uzavřené operace,
  nikoli na nové optimality.
* File137: machine-language instruction je definice kódu určujícího
  akci počítače. Nemá nový požadavek na fyzickou realizaci hypotetického
  hardwaru. IEEE má zde správné plné jméno; nezávislým primárním
  dokladem je copyright/titulní strana již uloženého standardu
  `sources/ieee754-1985.txt`, řádek30. Nedostupná aktuální webová
  stránka IEEE se za ověření nepovažuje.
* File138: little-endian určuje vzestupné váhy; není tvrzením, že
  MMIX tento formát používá. Matrix znamená dvourozměrné pole,
  což je přesně obor b/m/t převodů. Memory označuje úložiště dat,
  mems počet paměťových přístupů, MMIXAL zde znamená MMIX Assembly
  Language. Tyto definice odpovídají základnímu modelu, nákladovým
  součtům i úplnému syntaktickému rozboru
  `notes/recovery-pages-041-045.md`.
* File139: každý řádek Notational conventions byl jednotlivě
  spárován: ν počet jedniček; b byte vector; f floating interpretation;
  int integerization; m a mT bitová matice a transpozice; M[x],Mt[x]
  paměť se správným zarovnáním; s/u signed/unsigned interpretace;
  t tetra vector; v a v̄ množina bitových pozic a doplněk; w wyde vector;
  monus max(x−y,0); pravý/levý posun; &,|,⊕ průnik/sjednocení/symetrický
  rozdíl; rem IEEE remainder s nearest-even quotient; XYZ a YZ
  složení bajtů. Jsou to přesně V0012–V0014,V0041–V0055,
  `notes/fp-remainder-recovery.md` a úplný formát instrukcí.
  Rozlišují se domény slov a jejich matematických interpretací.
  Nybble4, nyp2, octabyte64 a zkrácené octa souhlasí s 8bitovým byte;
  opcode je operation code; profile je vektor počtů skutečných
  provedení, který se používá v dokázaných součtech nákladů.
* File140: registers jsou kvalitativní součást modelu s nejpřímějším
  přístupem k datům. Slovníček neudává kvantitativní benchmark pro
  všechna skutečná zařízení. Všech32 uvedených r-register názvů
  souhlasí s úplnou primární tabulkou a již uzavřeným V0072;
  samotný název rN „serial number“ zde neopakuje silnější neuzavřenou
  jedinečnost všech instancí R0004. Self-reference132 skutečně míří
  na tuto vlastní položku; odkaz126 je příslušná rekurzivní úloha.
* File141: tetra/tetrabyte32, U_Handler adresa underflow trip.
  Druhá definice je skutečný label a přechod na p89, doložený ve
  `notes/recovery-pages-087-097.md`, nikoli dodatečný předpoklad
  o jakémkoli hostitelském exception handleru.
* File142: wyde16; W_Handler adresa float-to-fix overflow trip,
  odpovídající předdefinovanému symbolu na p37. W a U se nezaměňují.

Všechny parentetické výklady opcodů a assemblerových direktiv byly
přečteny a porovnány s již uzavřenými rodinami a úplnými tabulkami:
2/4/8/16ADDU, ADD/SUB/NEG/MUL/DIV a U varianty; všechny load/store
šířky a jejich U varianty; všechny B/PB a CS/ZS podmínky;
bitové/maticové/difference operace; čtyři polohy wyde pro SET/INC/OR/ANDN;
všechna FP jména; JMP/GO/PUSH/POP/GET/PUT/SAVE/UNSAVE/RESUME;
cache/translation/synchronization názvy; TRIP/TRAP/SWYM;
IS/LOC/GREG/LOCAL/BSPEC/ESPEC/LDA. Převzatý rozsah je **význam jména**,
ne tvrzení, že všechny implementace jsou správné. Doložené programové
chyby zůstávají v samostatném software-ledger. Jména D/I/O/U/V/W/X/Z_BIT
a StdIn/StdOut/StdErr odpovídají již ověřené symbolové tabulce.
KKB/MMB a přípony mmb/mmo/mms jsou definovány v celé odpovědi2/20;
již uzavřené významy se nepřevádějí na ověření historických benchmarků.
Každý takový záznam má v inventuře explicitní druh a odkaz na tento
převzatý rozsah; ostatní položky zůstávají lokátory či bibliografií.

Omezená externí kontrola rozšíření názvů byla provedena v primárních
zdrojích: [ANSI](https://ansi.org/about/introduction),
[Unicode, tabulka zkratek](https://www.unicode.org/reports/tr17/tr17-4.html),
[ISO](https://www.iso.org/about),
[Berkeley, CSD-82-106](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1982/5449.html).
Dokládají jen American National Standards Institute, ASCII,
International Organization for Standardization a Reduced Instruction
Set Computer. Unicode odkaz je výslovně informativní návrh z roku2004,
ne aktuální normativní encoding specifikace. ISO je krátké jméno,
nikoli tvrzený akronym; kniha takové silnější tvrzení nečiní.
Metadata a přesný rozsah jsou `results/index-glossary-primary.json`.

## V0182: přesné bibliografické výjimky

Plná osobní jména, jejich historická ztotožnění a transliterace nebyly
externě ověřeny. Patří sem i znakové podoby v hebrejštině, arabštině,
čínštině, řečtině a indických písmech. Neprohlašuji za prokázanou
relevanci každého ze1628 lokátorů, úplnost hesel ani úplnost křížových
odkazů. Úvodní redakční pravidlo, že answer page je samostatně uvedena
jen pro téma chybějící v zadání, nebylo globálně zkontrolováno porovnáním
každého hesla se všemi odpověďmi. Jde o konkrétní bibliografické
výjimky povolené zadáním, nikoli o nezodpovězený matematický teorém.

V0181 zůstává reused s tímto rozšířeným přesným rozsahem; V0182 zůstává
partial. Všech osm stran má nyní úplnou mapu obsahu a doložený technický
slovníček, ale **nemá complete_argument_coverage** kvůli výslovným
výjimkám. To je odlišné od dosavadního stavu pending_scope_check.
File143 je prázdný netechnický list; nezvyšuje počet matematicky
ověřených stran. Již plně ověřené tabulky144–145 se nepřepočítávaly.

Celá mapa145 stran je hotová. Samotné V0054/V0055, ostatní konkrétní
prose/exercise mezery, R0001/R0004/R0007–R0010 a dvě candidates
zůstávají otevřené. Konec inventury není konec auditu.
