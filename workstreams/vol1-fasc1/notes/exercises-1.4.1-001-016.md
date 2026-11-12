# §1.4.1′ — úlohy 1–16

Zadání p. 65–66 / file 73–74, odpovědi p. 113–115 / file 121–123.
Logický model PUSH/POP je doložen v `independent-arguments-052-065.md`.
Fyzické spilling, SAVE/UNSAVE a úplné IEEE chování se tím nenahrazují.

**1.** Pro r,n>0 jsou navštívené indexy `n,n−r,…,a`, kde
`a=1+(n−1) mod r`; právě po a je další index a−r≤0. Nahrazení SUB kk,8
za SUB kk,rr s rr=8r tedy prochází přesně požadovanou množinu. Původní
maximum invariant a rozhodnutí PBP zůstávají stejné. Vstup GoMax nejdřív
nastaví r=1, obecný vstup používá n v $1 a r v $2. GO návrat přes $0
zachová globální výsledky. Jako u původního programu předpokládáme validní
pole a nepřetečení byteových indexů 8n,8r.

**2.** PUSHJ $R převede n v $(R+1) na $0 a r v $(R+2) na $1.
rr=$4 se vypočte dřív, než je m=$1 přepsáno prvkem pole. kk=$2, xk=$3
jsou samostatná pracovní místa. Max100 nastaví n=100 a propadne přes Max,
který nastaví r=1. POP 2 vrací m do $R a j do $(R+1), přesně jako
původní Max. Předpoklady mezí jsou stejné jako u 1.

**3.** List nepotřebuje chránit návrat v $0 před vlastním voláním jiné
rutiny. Je-li 20 míst skalárních a jsou-li k dispozici přidělené pracovní
registry, lze je držet přímo v registrech a odstranit frame prolog/epilog;
zůstane GO $0,$0,0. To je konkrétní zjednodušení odpovědi. Pro lokální
pole přístupné adresou nebo požadavek zachovat jinak obsazené registry
zůstává potřebný odpovídající prostor či ukládání, jak vysvětluje p. 61.
Nejde o tvrzení, že leaf s libovolným rozhraním nepotřebuje žádnou paměť.

**4.** PUSHJ cíl je @±4YZ, tedy dopředně až 2^18−4 bajtů a zpětně
nejvýše 2^18 bajtů. PUSHGO používá součet operandů jako absolutní adresu;
PUSH část i rJ mají stejnou sémantiku. „Within ±2^18“ v odpovědi je
mez rozsahu, nikoli tvrzení o dosažitelnosti každé nezarovnané adresy.

**5.** Počet čísel v [L,G) je G−L. Zbytek je L lokálních a 256−G
globálních; součet je přesně 256.

**6.** Oba zdrojové výskyty marginal $5 se přečtou jako 0 před zápisem.
Unsigned dělení `(rD*2^64+0)/0` použije předepsaný případ divisor≤rD:
quotient rD, remainder původní dolní slovo 0. Zápis přidělí lokály až
po $5, nové mezilehlé pozice jsou 0, L=6. DIVU zde nespouští signed
integer divide-check; nejde o ordinary aritmetické dělení nulou.

**7.** Marginal dest se nejdřív stane nulovým lokálem. INCML přičte
`#abcd*2^16`, tedy $5=#abcd0000, ostatní nové lokály jsou 0 a L=6.
Přenos žádné další bity nezapne, protože původní hodnota byla nula.

**8.** SET $15,0 zvýší L z 10 na 16. Globální PUSHJ $255 pak uloží
odkaz na původní konec lokálů p=L; následné POP 1 umístí hlavní výsledek
právě do $p. Dva stavy se tak odliší výsledkem v $10 versus $16.
Nejde tedy o redundantní instrukci při libovolném pokračování.
Dopad na objem SAVE je zatím jen závislost na počtu živých položek,
nikoli přesný časový profil SAVE.

**9.** Trip uloží staré $255 do rB a staré rJ do $255. PUSHJ $255,Handler
chrání všechny původní lokály a vytvoří L=0; protože G≥32, je volných
nejméně $0…$31. Pomocník musí respektovat použité globals/speciální
registry, zejména zachovat $255 a trip context. POP 0 obnoví původní
lokály; PUT rJ,$255 obnoví původní rJ, GET $255,rB původní $255 a
RESUME pokračuje přes uložené rW/rX. Známé erratum z 2007 přidávající
PUT rJ je již v odpovědi. Samotný PUSHJ samozřejmě nezachovává libovolné
speciální registry, které by Handler svévolně změnil; uvedená konstrukce
prokazuje dostupnost bezpečného lokálního pracovního prostoru.

**Recovery correction,7 November2026:** The earlier whole-exercise closure is withdrawn. C0021 contradicts the startup GREG count and C0022 contradicts the SAVE extension even with matched zero initial states. The following induction covers only its restricted no-SAVE premise; the separate initial-value/permutation interpretation remains partial.

**10.** Platnost vyžaduje kvalifikace výslovně uvedené v odpovědi.
Bez PUSH/POP, změn rL/rG a pozorování těchto čítačů lze každému číslu
registru přiřadit jeho hodnotu: marginal i dosud nulový local reprezentují
0 a zápis se v obou případech stane běžným zápisem. Indukce přes instrukce
dokazuje ekvivalenci přejmenování $2…$254. $0/$1 nesou vstup a $255
slouží jako trap/trip argument. Doslovné zadání bez dalších omezení není
bezpodmínečně true: PUT rL,0 zahodí lokály, ale nezmění globals. Odpověď
právě tuto mezeru v závěrečném přesném tvrzení výslovně vylučuje, proto
nejde o nový rozpor. U SAVE/RESUME jsou uvedeny další podmínky destination
registrů; neuzavíráme tím jejich plnou implementaci.

**11 — partial.** Při běžném počátečním zásobníku začíná O na
#6000000000000000. POP bez předchozího PUSH čte odkaz na O−8,
tedy #5ffffffffffffff8. To dokazuje adresu v odpovědi. Page fault/abort
navíc předpokládá, že poslední pool stránka není mapovaná a OS takto
obslouží fault. Text explicitně předpokládá „nothing has been stored
there“; nepovažujeme to za univerzální architekturní záruku pro program,
který si tam úmyslně něco namapoval. Varianta POP těsně po SAVE a celý
OS kontrakt zůstávají otevřené.

**12.** (a) Indukce: první prefix je :, relativní argument PREFIX se
k němu připojí a absolutní už dvojtečkou začíná. (b) PREFIX Foo nastaví
:Foo, bez koncové dvojtečky, tedy false. (c) Dvojtečky jsou znakové části
jména a nezkracují se jako opakovaná lomítka; : a :: jsou různá absolutní
jména. To plyne přímo z pravidla lexikálního prefixování.

**13.** Předpoklad n≥0 je známé doplnění errat z 2023; n musí být
reprezentovatelné v použitém signed porovnání. Fib při n≤1 vrací n.
Jinak $1 uchová rJ. První call s R=2 chrání n a návrat, předává n−1
v $3 a vrací F(n−1) do $2. Druhý s R=3 chrání i tento výsledek,
předává n−2 v $4 a vrací F(n−2) do $3. ADDU do $0 sečte modulo 2^64;
PUT obnoví rJ. Silná indukce dává F_n modulo 2^64.

Fib1 začne pro n>1 dvojicí (1,0) a opakuje n−1 krát transformaci
`(a,b)→(a+b,a)`; po k krocích má (F(k+1),F(k)). SUBU používá právě
novou první souřadnici minus starou druhou, takže přesně obnoví starou
první i modulo 2^64. Fib2 využije kladný výsledek CMP jako $1=1 a
nastaví $0=0. Dvě ADDU mění `(F(2k),F(2k+1))` na
`(F(2k+2),F(2k+3))`. Smyčka proběhne floor(n/2) krát. Pro sudé n
je konečný čítač −1 a vrací se $0; pro liché n je 0 a CSZ vybere $1.
Obě základní hodnoty n=0,1 vrací vstup. Žádná rutina nepotřebuje global.

**14.** Počet listů rekurzního stromu je F(n+1), vnitřních uzlů
F(n+1)−1, všech POP tedy 2F(n+1)−1 a ADDU F(n+1)−1. List stojí
CMP+správně predikované PBN+POP =5υ. Vnitřní uzel mimo své dvě děti
stojí 14υ, včetně špatně predikované PBN a dvou PUSHJ. Volající SET
plus PUSHJ přidá 2υ: celkem `19F(n+1)−12`.

Fib1 pro n>1: příprava 5υ, n−1 čtyřinstrukčních iterací, poslední
chybná predikce +2υ, POP 3υ, caller 2υ; součet `4n+8`.
Fib2: příprava 4υ, floor(n/2) čtyřinstrukčních iterací, konec +2υ,
CSZ 1υ, POP 3υ a caller 2υ; součet `4 floor(n/2)+12`.
Základní hodnoty nejsou zahrnuty ve vzorcích pro n>1, jak uvádí kniha.
K důkazu >10^22υ pro F100 stačí již známé F92>7.54*10^18 a
F93>1.22*10^19 z úlohy §1.3.2′–27: `F101=34F93+21F92`, takže
`19F101−12>1.0889*10^22`. Žádný exponenciální běh se neprováděl.

**15.** Global n je zároveň výsledkové fn. Každý vnitřní rámec uloží
fp, návrat, původní n a po prvním volání i F(n−1). Po druhém volání
z paměti přičte F(n−1) k F(n−2); epilog obnoví link, sp a fp. List
ponechá n=F_n. Na vnitřní uzel připadá 8 memory operací a 27υ,
na list 5υ; caller SET/GO má 4υ. Celkem proto
`8(F(n+1)−1)μ+(32F(n+1)−23)υ`, přesně jako odpověď.
Poměr pro velké n jde k `(8μ/υ+32)/19`; při μ≥υ je alespoň 40/19>2.

Varianta bez fp nechá sp ukazovat na bázi současného tříslovného rámce.
Vstup vnitřního uzlu nejdřív zvýší sp o 24, používá offsety 0 (návrat),
8 (n),16 (první výsledek), výstup jej sníží o 24. Oproti plnému rámci
zmizí STO fp, SET fp a LDO fp; SET sp,fp nahradí SUB sp,sp,24.
Zůstává 6 memory operací a 24υ na vnitřní uzel, tedy hlavní koeficient
`(6μ/υ+29)/19`. Všechna load/store posunutí jsou nezáporná a přímo
kódovatelná; není potřebný neexistující záporný immediate offset.

**16.** Za každý call do C vloží B i C landing pad
`PUT rJ,$1; POP 0,0`; $1 obsahuje vlastní původní návrat a musí být
chráněn volbou R≥2. Normální návrat C pomocí POP 0,2 přeskočí obě
instrukce landing padu. Nonlocal návrat POP 0,0 naopak vstoupí do padu,
který obnoví předchozí rJ a zruší další rámec; stejný postup se opakuje
přes všechny aktivní C a B až k volání B z A. Každý rámec se odstraní
právě jednou, takže návrat do A má správný register-stack kontext.
Pro jiné návratové hodnoty/adresy je potřeba rozšířit protokol; text
výslovně pro tento příklad předpokládá, že B/C nic nevracejí.

Stav: 15 úloh má argument, 11 zůstává partial pro OS/SAVE chování.
Překlep „been been“ v zadání 9 je již evidovaný C0005; nový nález žádný.
