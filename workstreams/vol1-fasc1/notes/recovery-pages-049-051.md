# Úplný rozsah file49–51 / p41–43: I/O a úlohy1–3

Přečteny všechny tři stránky a zobrazeny původní sazby
`images/file-049-p041.png`, `file-050-p042.png`, `file-051-p043.png`.
Tento zápis nahrazuje domněnku, že staré V0102–V0107 pokrývají bez
výhrad celý text. Jejich platné argumenty se přebírají s původními
předpoklady; dvě nově přesně vymezené mezery jsou níže R0007/R0008.
Nejde o opakování přijatých stack/SAVE/UNSAVE důkazů ani o nový běh.

## File49/p41 — návrat, Fopen, Fclose a všechny příklady

**Návrat do $255.** Primární dispatcher MMIX-SIM:2385–2406 ukládá
návrat každé z deseti služeb do rBB a poté přímo do g[255]. Je to
definované simulátorové rozhraní popisované v knize, nikoli tvrzení
o všech představitelných OS. Do služeb s třemi argumenty vstupují
mb=M8[$255], ma=M8[$255+8]; ostatní varianty předávají přímý $255,
nebo jej nepotřebují. Pole Z dává handle0..255. Příslušné arg_count
pro Fopen/Fread/Fgets/Fgetws/Fwrite jsou3, pro Fputs/Fputws/Fseek2,
pro Fclose/Ftell1. Každý knižní tvar volání tak má vlastní vazbu
na skutečný dispatcher.

**R0007 — přesný obor „negative iff error“ zůstává partial.** Pro
platné přenosové S v [0,2^63−1], počet0≤n≤S a signed návrat platí
−S≤n−S≤0; neúplnost n<S je právě negativita. Serious Fread error
−1−S leží v [−2^63,−1] a mimo všechny běžné n−S. Pro služby
s0/−1 je znaménkový test okamžitý; úspěšný počet nebo pozice se musí
vejít do nezáporného signed64. Fgets/Fgetws potřebují S≥1; případ
S=0 není popsanou konečnou délkou S−1 znaků.

Stránka však sama neříká, zda se tímto pravidlem myslí pouze takto
reprezentovatelné počty a pozice a validní velikosti. Pokud bychom
bez další premisy dovolili unsigned S=2^63, serious error by se
po redukci modulo2^64 změnil na kladné2^63−1. To není potvrzený
knižní protipříklad: chybí doložení, že takový parametr je v zamýšleném
oboru. Je to přesná chybějící předpokladová věta, kterou starý omezený
argument neuzavírá. Není potřeba žádný obrovský buffer ani běh.
Zbývá vymezit obor parametrů/počtů z primární specifikace, nebo
ponechat tuto výslovnou kvalifikaci; stránka49 proto není zelená.

**H a P nekontrolují chyby.** Již úplně zkontrolované instrukční
seznamy H a P po TRAP nezjišťují znaménko návratu a řídí další práci
jen svými vlastními počítadly. H po Fputs končí; P nastaví další
argument či pokračuje tiskovým čítačem. To dokládá konkrétní
vytištěnou větu. Rada o důležitosti obsluhy chyb je metodické
doporučení, nikoli univerzální matematický či empirický benchmark.

**Fopen: celý normativní popis.** Deset služeb používá byte handle,
tedy256 různých indexů. Name je adresa NUL ukončeného řetězce.
Pět režimů a jejich operace souhlasí s MMIX-SIM:253–300; tabulky
MMIX-IO mají r,w,rb,wb,w+b a příznaky1,2,5,6,15. Právě tři režimy
obsahující Write otevírají pomocí w, což při úspěchu vytvoří/prázdní
soubor. Režimy r/rb nezapisují a nezkracují. 0 značí úspěšně přidělený
handle, −1 neúspěch. Tím je kontrolována definice rozhraní, ne
neomezená garance hostitelského fopen při nedostatku prostředků.

**Volání (3)/(4) a foo.** OCTA zarovná Arg na8; dva sloty leží
na Arg a Arg+8. První má adresu nejbližší následující1H, druhý
BinaryWrite=3. Byte řetězec je66,6f,6f,00. LDA vytvoří adresu Arg,
nikoli adresu foo přímo; dvě načtení dispatcheru získají správnou
dvojici(name,mode) a Z=5 je platný handle. Future1F je dovolený
v OCTA, jeho fixup se provede při1H. Příklad je podmíněn úspěšným
hostitelským otevřením; netvrdí, že jméno foo lze otevřít na každém OS.

**Tři počáteční handles.** MMIXAL má StdIn=0,StdOut=1,StdErr=2;
mmix_io_init nastavuje přesně fp stdin/stdout/stderr a mode1/2/2.
To odpovídá TextRead/TextWrite/TextWrite. Interaktivní adaptace stdin
je v primární dokumentaci popsána zvlášť; tato věta ji nepovažuje
za stejnou jako libovolný binary soubor.

**Fclose a (5).** Normativní definice v MMIX-SIM:302–308 vyžaduje
deaktivaci asociace,0 při úspěchu,−1 pro již zavřený/unclosable.
Přímý TRAP nepotřebuje argument v $255: arg_count=1 a dispatcher
předá pouze Z. Programová větev mode0 vrátí−1; u handle>2 hostitelský
fclose!=0 vrátí−1, jinak mode=0 a0. U0..2 je ochrana hostitelského
stdio explicitní implementační záměr a MMIX asociace mode se přesto
deaktivuje. Další hostitelská životnost FILE* při neúspěšném fclose
není tímto tvrzením prohlášena za univerzálně bezpečnou.

**Poznámka text/binary.** Kniha normativně přebírá konvence hosta.
MMIX-SIM:274–281 to říká výslovně a uvádí možnost rozdílné reprezentace
textových newline. Netvrdí se stejná fyzická reprezentace všech OS.
Jde o podmínku rozhraní, ne další požadavek dokazovat každý OS.

## File50/p42 — každá služba a každá větev jejího kontraktu

**Fread (6)/(7).** Povolené read režimy jsou přesně TextRead,
BinaryRead,BinaryReadWrite. Dvojice(buffer,S) se načte z obou
octa slotů jako u Fopen. Při běžném výsledku n je n−S odvozen výše;
serious error má odlišnou hodnotu−1−S. Nulu dává n=S, krátký EOF
dává n<S. Známá knižní oprava serious error je již v originálu
zapracovaná a není nový nález. Platný konkrétní neinteraktivní
programový obor 0<S≤INT_MAX má přímý důkaz: calloc buď selže a
o zůstane−1, nebo fread dá0≤n≤S; ferror větev uvolní buffer a
neuloží jej, success uloží právě n bytů a vrátí n−S. Všechny převody
int jsou v tomto oboru přesné. Velikosti nad INT_MAX a interaktivní
stdin jsou jiné konkrétní implementační povinnosti v pracovní I/O
poznámce; norma Fread netvrdí, že každý velký požadavek uspěje.

**Fgets.** V normativní úspěšné větvi s S≥1 vznikne n≤S−1 bytů,
poslední může být LF0a, a za nimi jeden NUL. Celkem n+1≤S, tedy
buffer má předepsanou kapacitu. Vložený NUL není normativní stopping
condition; primární MMIX-SIM:331–334 to navíc výslovně říká. Chyba
smí ponechat obsah bufferu nedefinovaný a vrací−1. Volání se liší
od Fread jen Y=4 místo3; argumenty a handle jsou stejné.

**R0008 — EOF u neprázdného posledního řádku.** Dosavadní V0104
nevyřešilo rozpor dvou primárních popisů: próza požaduje−1 při EOF
před S−1 či newline, ale uvedené C fgets/strlen vrací počet také pro
neprázdný poslední řádek bez newline. Např. jediný byte A a S=3
se podle literal prózy nedočte, kdežto standardní C fgets uspěje
s jedním znakem. Oba předpoklady platí i bez vložených NUL, takže
výslovná výjimka u C analogie tento rozdíl neodstraňuje.

Kniha má tutéž prózu; netvrdím automaticky, že je chyba právě v knize
nebo právě v implementaci. Zbývá určit zamýšlené completion pravidlo
z autoritativního upřesnění, případně ponechat tuto interpretaci
otevřenou. V0104 se proto znovu otevírá jako partial. Dřívější
správné důkazy kapacity, znaků a volání zůstávají platné.

**Fgetws.** Nahrazení byte jednotky wyde dává nejvýše S−1 vydů,
NUL wyde na konci a nejvýše2S bytů paměti; newline je000a. Pro
počty s2S reprezentovatelným jako platná délka se obě meze získají
pouhým násobením2. Návrat počítá vydy, nikoli byty. MMIX-SIM:336–346
obsahuje totožnou definici, tedy i EOF nejednoznačnost R0008.
Prázdný EOF není nejednoznačný: próza i C verze požadují−1; celý
programový protipříklad a úzká oprava jsou samostatně S0006.
Normativní vyde rozhraní se nesmí tiše zaměnit za libovolný hostitelský
wchar_t/endianness; přijatý S0006 na těchto volbách nezávisí.

**Fwrite.** Povolené write režimy jsou TextWrite,BinaryWrite,
BinaryReadWrite. Dvouslotové volání mění Y na6. Přesná smlouva
n−S a její range je důkazem shodná s běžným Fread, s n počtem
úspěšně napsaných bytů. Skutečný short-block rozpor a úplný
invariant/oprava jsou S0005; správný knižní kontrakt se kvůli tomu
neoznačuje za chybný. Případ, kdy host fwrite přijme n bytů a
následný fflush selže, má vlastní neuzavřenou interpretační povinnost
v io-recovery-open-obligations.md. S0005 jej nepovažuje za opravený.

**Fputs (8).** Nechť první NUL leží na string+k a předchozích k
bytů je nenulových. Definice zapisuje právě tento prefix, nikoli
terminátor, vrací k, nebo−1 při chybě. SET přenese přímý pointer
do $255; arg_count=2 předá b přímo, takže se nečte Arg. Úspěšná
programová smyčka má invariant: po j plných blocích je vypsán
prefix256j, string ukazuje za něj a o=256j; mmgetchars(stop0)
vrací nejbližší NUL nebo256. Každý fwrite short vrací−1, plný blok
prodlužuje prefix a poslední n<256 vrátí k. Platí s konečným
terminátorem, platnou pamětí, reprezentovatelným k a úspěšnými
flush operacemi. Počet bloků je floor(k/256)+1, včetně prázdného
posledního bloku, leží-li NUL přesně na hranici.

**Fputws.** Stejný důkaz se užije na vyrovnané vyde jednotky:
mmgetchars(stop1) zastaví před první0000, plný256bytový blok má
128 vydů, n je sudé a o se zvýší o n/2. Konečný nulový wyde
není vypsán a počet je v jednotkách wyde. Předpoklady alignmentu,
velikosti a úspěšných flush jsou výslovné; obecná hostitelská
konverze wide textu není dokázána tímto bitovým argumentem.

**Fseek, začátek.** Je to binary služba. Pro offset o≥0 je cíl o;
pro o<0 a délku L je cíl L−(−o−1)=L+o+1. Tím o=0 dává začátek,
o=−1 konec, o=−2 byte před koncem a o=−L−1 opět začátek. Poslední
vzorec vyžaduje reprezentovatelný offset a povolenou pozici. Rozhraní
smí odmítnout nepodporované umístění; netvrdí bezpodmínečný úspěch.

## File51/p43 — zbytek API, všechna čísla a úlohy1–3

**Fseek dokončení a (9).** 0/−1 hlásí úspěch/neúspěch. SET předá
přímý signed offset; Y=9, arg_count=2, žádné dvouslotové Arg.
Povinný Fseek při změně směru BinaryReadWrite je normativní
podmínka MMIX-SIM:392–394, nikoli odvozená vlastnost všech OS.
Implementace používá mode bit8 pro readwrite a zakáže opačný směr
do dalšího Fseek; přesné zotavení po neúspěšném hostitelském seek
není do obecného kontraktu přidáváno jako nový skrytý slib.

**Ftell a (10).** Binary režimy, byte pozice a−1 odpovídají primárnímu
MMIX-SIM:396–407. Arg_count=1 potvrzuje, že vstupní $255 není třeba.
Úspěšná long hodnota ztrácí v MMIX-IO horní tetra; plný přípustný
LP64 obor, všechny větve a oprava jsou samostatně S0008. Kniha
definuje správné API; kontext strany51 není programový error mapping.

**MMIXware a tabulka (11).** Existence popisu všech deseti funkcí
i reference implementation je doložena celým načteným MMIX-SIM
Rudimentary I/O a celým MMIX-IO. Tato bibliografická existence
neimplikuje jejich bezchybnost. Všech16 číselných přiřazení bylo
jednotlivě porovnáno s MMIXAL:2059–2090: Fopen1,Fclose2,Fread3,
Fgets4,Fgetws5,Fwrite6,Fputs7,Fputws8,Fseek9,Ftell10; TextRead0,
TextWrite1,BinaryRead2,BinaryWrite3,BinaryReadWrite4; Halt0.
Nejde o vzorek tabulky. MMIX-SIM enum a arg_count mají stejné pořadí.

**Úloha1(a).** Na řádku29 je4B nejbližší předešlé4H, řádek24.
**1(b).** Po změně24 na2H a29 na r,2B jde řádek29 stále na24,
ale23 nyní bere2F jako24 místo38 a31 bere2B jako24 místo21.
Při prvním n=5 má dělení5/3 kvocient1,zbytek2 a test1≤3 přejde
na24 místo uložení5 na21. Výsledná tabulka už nevzniká správným
algoritmem; nejde jen o jiný zápis téže hrany. Odpověď99 správně
jmenuje obě další poškozené reference. Všechny tyto labely a větve
jsou v původní sazbě P, nikoli v odhadnutém přepisu.

**Úloha2.** Před první9H je nejbližší9B definováno jako0. Jestliže
dosud bylo m řádků, následující IS vyhodnotí předchozí9B a vytvoří
nové ekvivalentní číslo m+1 modulo2^64. Indukce dává po m řádcích
m modulo2^64, tedy obyčejný počet, dokud se vejde do octa. Žádné
jiné9H do indukce nezasahuje podle zadání. Počet se týká řádků
zdrojového souboru, nikoli počtu runtime návštěv; IS nevytváří
instrukci. Modulární kvalifikace plyne z dříve stanovené aritmetiky
MMIXAL a není vynechaná možnost neomezeného integer čítače.

**Úloha3 — přesný vstup a rozhraní.** Úspěšný Fread načte100 signed
octa X[1..100] do D+8 až D+800, kde D=Data_Segment. Precedence
dává X0+1<<3=X0+(1<<3)=D+8 a N<<3=800. X0 není součástí načítaného
pole. x0 je globální254, t=255, takže lokály0..3 a Maximum se
nepřekrývají s base registry. Předpokládá se běžný dostupný stack
a buffer disjunktní od kódu a argumentů; to je původní obor důkazu M.

Přesný již uzavřený V0124 se přebírá beze změny: PUSHJ $1 zachová
caller$0, caller$2=n se stane callee$0, POP2 vrátí callee$1=m do
caller$1 a callee$0=j do caller$2. M pro každé1≤n≤100 vrací
m=max X[1..n] a platné1≤j≤n, beze změny pole. Důkaz M a počtu
jeho kroků je recovery-pages-037-040.md; úplná stack realizace se
zde neopakuje. Tím už neplatí stará hláška „callinterface partial“.

**3 — invariant a všechny větve swapu.** Na vstupu outer loop je
caller$0=8n,1≤n≤100; suffix X[n+1..100] je neklesající a každý
jeho prvek je alespoň každý prvek prefixu. Zároveň pole je permutací
vstupu. SR kladného8n o3 dá n přesně. LDO$3 uchová původní X[n],
SL j o3 vytvoří8j. První STO dá m do X[n], druhé původní X[n]
do X[j]. Pro j<n jde o transpozici; pro j=n jsou obě adresy totožné
a m=původní X[n], takže obě uložení zanechají stejnou správnou hodnotu.
Po výměně je nový X[n] maximum prefixu a nepřevyšuje starý suffix.
Obě části invarianty i permutace tedy platí pro n−1.

SUB sníží8n o8. PBNZ pokračuje právě pro n>1, takže se provede
přesně100 outer iterací a skončí s n=0; base případ má prázdný
suffix. Všechny indexy leží8..800, jsou zarovnané a žádný posun
ani SUB nepřeteče. Na konci je celé pole neklesající a zachovává
multimnožinu všech100 vstupů, i při rovnostech nebo krajních signed64
hodnotách: M porovnává signed CMP, ne nebezpečný aritmetický rozdíl.

**3 — adresy a výstup.** M zabírá100..128, Main začíná12c,
PUSHJ na13c má target100, tedy−15 tetra; PBNZ na154 míří138,
tedy−7. Dvojice Arg9H je po zarovnání na168. Oba GETA na12c/158
mají displacement15 a4, platné16bitové hodnoty. Arg je mimo kód
i data. Druhé volání se stejným Arg zapisuje právě800 uspořádaných
bytů, je-li Fwrite úspěšný, poté Halt0 končí. Při selhání nebo
krátkém I/O program nemá kontrolu; tvrzení o třídění100 dodaných
octa je proto výslovně podmíněno úplným vstupem/výstupem. Žádná
stabilita ani globální rychlostní optimalita se netvrdí. Není zde
vytištěn nový časový benchmark, který by bylo nutné spouštět.

Odkaz odpovědi na Algorithm5.2.3S je srovnávací bibliografie, nikoli
předpoklad tohoto samostatného invariantního důkazu. Samotný originál
této jiné kapitoly se v tomto bloku neověřoval; patří k úplné mapě
odpovědní strany107, která ještě není zelená.

## Přesná dispozice

File49 má celý rozsah zmapovaný, ale R0007partial. File50 má celý
rozsah zmapovaný, ale R0007 a R0008partial; V0104 je otevřeno znovu.
File51 má všechny vlastní věty,16 číselných položek a úlohy1–3
samostatně pokryté a je argument-complete. Programové S0005/S0006/
S0008 jsou od správných knižních definic a jejich barvy oddělené.
Další konkrétní I/O implementační otázky jsou přesně vypsány
v io-recovery-open-obligations.md a tento zápis je nevydává za
uzavřený důkaz každé řádky externího MMIX-IO.
