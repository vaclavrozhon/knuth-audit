# Úplná obnova §1.4.1′–1 až16

7. listopadu 2026. Zadání file73–74/p65–66, všechny odpovědi
file121–123/p113–115. Starý rozbor `exercises-1.4.1-001-016.md`
je převzat jen pro argumenty, které níže mají stejné předpoklady.
Každá dodatečná věta odpovědí je zahrnuta; zejména jsou doplněny
POP po SAVE, celý program bez fp, konečné nákladové meze a obě
rozšíření nelokálního návratu. C0021/C0022 mají samostatné důkazy.

Použité primární kontrakty jsou MMIX-DOC2013, oddíly marginal,
PUSH/POP, trip a SAVE; jejich úplné implementační důkazy z
`independent-arguments-073-082.md`, V0149–V0153, a úloh1.4.3′–10,
11 a12 se přebírají bez nového běhu. Oprava SAVE obrázku C0007
je v tomto převzetí již zohledněna. Tabulkové časy jsou nominální
μ/υ model, ne změřená latence libovolného hardwaru či OS.

## 1. Celé GoMaxR včetně vynechaného těla

Předpoklady jsou 1≤n,r<2^60, platné osmibajtové prvky pole,
platný návrat a navzájem odlišné globální j,m,kk,xk,rr,x0,t.
t je konvenční $255. Hodnoty X jsou libovolné signed64 včetně
obou extrémů. Tato strojová omezení zpřesňují matematické n,r>0;
nepředstíráme, že signed PBP dovoluje libovolné 64bitové značky.

Úplné tělo odpovídající výpustce v odpovědi je:

```text
GoMax   SET  $2,1
GoMaxR  SL   rr,$2,3
        SL   kk,$1,3
        LDO  m,x0,kk
        JMP  1F
3H      LDO  xk,x0,kk
        CMP  t,xk,m
        PBNP t,5F
        SET  m,xk
1H      SR   j,kk,3
5H      SUB  kk,kk,rr
        PBP  kk,3B
        GO   kk,$0,0
```

Navštěvované indexy jsou n,n−r,…,a, kde
a=1+(n−1) mod r. Je jich q=ceil(n/r). Před každým SUB je
kk=8k, m maximum navštívených prvků a j největší navštívený
index s touto hodnotou. Po SUB je buď kladný další index, nebo
poslední a−r∈[1−r,0]. PBNP při xk≤m ponechá m,j; při xk>m
se obojí nahradí. CMP tedy pokrývá všechna znaménka bez přetečení
odečítání a při shodě zachová větší index. PBP končí přesně po q
prvcích; r>n dává jediný prvek, r=1 původní úlohu. Výsledek j
je index v poli, nikoli pořadí mezi q návštěvami.

8n,8r jsou kladné signed64; poslední rozdíl ≥8(1−r)>−2^63.
Žádná mezilehlá SUB nepřeteče. Pole se nepisuje a $0 se před
návratem nemění. Závěrečné GO používá staré $0 jako adresu,
přepíše již nepotřebné kk a zachová oba výsledky j,m.

Při h striktních zlepšeních mezi q−1 porovnáními stojí tělo
GoMaxR **qμ+(5q+7+4h)υ**: přesně obecný Max z rozboru60–70
s n=q a jedním dodatečným SL rr. Caller SET r; SET n; GO
přidává5υ, tedy qμ+(5q+12+4h)υ. Jednoinstrukční SET předpokládá
registr nebo přímo kódovatelnou konstantu; příprava širší konstanty
se přičítá. Special entrance GoMax přidává SET r=1, zatímco
caller tento SET nepotřebuje; jeho celková režie je stejná.

## 2. PUSHJ verze a oba zvláštní vstupy

j=$0,m=$1,kk=$2,xk=$3,rr=$4. Caller uloží n do $(R+1),
r do $(R+2) a provede PUSHJ $R,MaxR; vyžaduje R+2<G.
Vstupní SL rr,$1,3 proběhne **před** přepsáním $1 prvkem X[n];
SL kk,$0,3 proběhne před přepsáním $0 výsledkem j. Tělo je
doslova předchozí s těmito aliasy a s POP2,0 místo GO.
G≥32 zaručuje lokální pracovní čísla0…4.

PUSH uloží callerovy pozice0…R−1 a markerR; n,r se stanou
callee0,1. POP2 vrátí hlavní m do callerR a pomocné j do
callerR+1. List nemění rJ, takže se vrátí za původní call.
Max100 nejprve nastaví0=100, propadne do Max nastavujícího1=1,
pak MaxR; Max samotné přijímá n v0. Oba zvláštní vstupy tedy
splní právě dokázaný invariant. Tělo MaxR má stejný čas jako
GoMaxR, protože POP i GO stojí3υ. Dva SET a PUSHJ přidají3υ,
tedy qμ+(5q+10+4h)υ pro obecné volání. Přidané vstupní SET
mají vždy svou jednuυ; nepřisuzujeme je opět volajícímu.

## 3–5. List, adresování a počet marginal

3. Ve schématu(15) zabírá20 lokálních skalárních proměnných
$1…$20, zatímco $0 drží návrat. G≥32 tato čísla dovoluje.
List nevolá další GO, takže návrat nemusí ukládat; končí
GO $0,$0,0. Rozhraní dovoluje tyto pracovní registry změnit.
Adresované lokální pole nelze obecně přeměnit na skalární
registry; tuto výjimku text již uvádí na p61. Odpověď je
zjednodušení registrovatelných lokálů, nikoli univerzální
odstranění veškeré paměti z libovolného listového programu.

4. PUSHJ má posun4YZ nebo4YZ−2^18: všechny násobky4 od
−2^18 do2^18−4. PUSHGO používá součet starých adresních operandů
nebo assemblerem rozloženou absolutní adresu. U obou je stejný
push a rJ=adresa instrukce+4. „Any desired place“ předpokládá
platnou adresu instrukce a její dostupné vyjádření; neslibuje
vykonávání libovolného nezarovnaného či nepřístupného bajtu.

5. Disjunktní intervaly[0,L),[L,G),[G,256) mají velikosti
L,G−L,256−G. Součet256 a marginal početG−L platí i pro L=G.

## 6–8. Marginal registry a pozorovatelná změna L

6. $5 marginal znamená L≤5<G. Oba zdroje DIVU $5,$5,$5
jsou stará nula. Předepsaná unsigned větev divisor≤rD nastane
pro **každé** rD, i nulu; vrací quotient rD a původní dolní
slovo0 do rR. Zápis vytvoří lokály až5: L=6, $5=rD a
nové mezilehlé pozice0. Není vyvolána signed divide-check D.
To není aplikace neexistujícího běžného podílu číslem0.

7. Čtená původní hodnota marginal destinace je0. INCML přidá
#abcd·2^16, tedy $5=#abcd0000 bez dalšího přenosu; opět L=6
a ostatní nově přidělené lokály jsou0.

8. SET $15,0 při L10 nastaví L16. Následný PUSHJ $255
uloží marker10 nebo16; POP1 umístí hlavní výsledek právě do
této díry. Existuje tedy pokračování rozlišující oba stavy,
i když všechny jednotlivé původní hodnoty registrů byly stejné.

Přijatý SAVE layout má pro L16 místo L10 o šest uložených
lokálních octa více, tj.48 bajtů; úplné obnovení musí jejich
hodnoty opět zpřístupnit. To vysvětluje vytištěné „generally
take longer“ jako více paměťové práce. Není z toho odvozováno
jiné nominální ohodnocení SAVE/UNSAVE: tabulka jim přisuzuje
konstantních20μ+υ a neurčuje přesnou latenci pro každý L.

## 9. Celý protokol trip handleru

MMIX-DOC2013:2160–2195 stanoví trip vstup: staré $255→rB,
staré rJ→$255; rX má záporný horní tetrabyte a rY/rZ příslušné
operandy. PUSHJ $255,Handler chrání všechny staré lokály,
vloží markerL a vytvoří L0. Nejméně32 pozic0…31 je marginal.
Handler v nich může pracovat, protože žádný jeho zápis nedosáhne
na uložené lokály volajícího. Musí zachovat $255, G a trip
context rB/rW/rX/rY/rZ; jiné použité globals/specials musí
rovněž uložit a obnovit. Vnořený trip vyžaduje samostatnou
ochranu tohoto kontextu; není automaticky slíben samotným PUSH.

Po běžném návratu POP0 obnoví přesně původní lokály. PUT rJ,$255
obnoví původní rJ, GET $255,rB původní $255 a RESUME se záporným
rX pokračuje po přerušené instrukci s jejím normálním výsledkem.
Pro úlohu stačí handler používající pouze tento lokální workspace
a netrippující operace; libovolné svévolné poškození globals
nebylo součástí slibu. Záměrná náhrada výsledku změnou rX/rZ
je jiný deklarovaný kontrakt. Známá oprava2007 doplňující
PUT rJ je aplikovaná a není nový nález. Popsaná čtveřice
instrukcí má16 bajtů, tedy se vejde do trip vstupního slotu.

## 10. Dvě chyby a samostatný neuzavřený význam permutace

První věta odpovědi o počtu GREG je vyvrácena
`MMIX-C0021-greg-coalescing-count.md`: shodné nenulové hodnoty
se sdílejí, nulové nikoli. Druhý odstavec o SAVE je vyvrácen
`MMIX-C0022-save-register-equivalence.md` i při stejném G254,
nulových počátečních hodnotách a globální destinaci SAVE.
Tyto důkazy a jejich původní sazba/errata se zde neopakují.

Platný omezený argument bez PUSH/POP/SAVE/UNSAVE/RESUME,
bez čtení L a bez změn L/G je následující. Pro odpovídající
počáteční hodnoty a pevné G asociujeme každému číslu jeho
hodnotu; marginal i nulový local představují0. Čtení zdroje
bere tuto hodnotu. Zápis local/global zapisuje danou hodnotu;
případně nově zpřístupněné ostatní lokály měly předtím hodnotu0
a dostanou0. Operace se stejně přejmenovanými explicitními
operandy tedy zachovávají asociaci. Indukce platí pro rutiny,
jejichž ostatní pozorování ani volané služby nepoužívají
odlišnou klasifikaci registrů či introspekci přejmenovaného kódu.
$0/$1 pro vstup a $255 pro I/O/trips zůstávají pevné.

**Zbývající partial má konkrétní obsah:** knižní „permute register
numbers arbitrarily in any … program“ neurčuje transformaci
počátečních nenulových GREG hodnot. Při GREG1 má $254 hodnotu1,
ale marginal $2 hodnotu0; pouhá změna čísla zdroje SET $255,$254
na $2 se stejnými deklaracemi změní výsledek. Při přejmenování
i celé počáteční reprezentace může být zamýšlena jiná ekvivalence.
Bez vyjasnění tohoto významu není celý první odstavec uzavřen.
Nezakládáme další confirmed nález jen z této interpretace;
ani netvrdíme úplnou opravenou klasifikaci SAVE/RESUME programů.

## 11. Přebytečný POP a konkrétní POP po SAVE

Úloha žádá odhad běžného chování, nikoli definici libovolného OS.
Při počátečním rO=#6000000000000000 první přebytečný POP
čte marker na rO−8=#5ffffffffffffff8. MMIX-DOC2013:1715–1722
výslovně ukládá OS uspořádat ochranu tak, aby přebytečný POP
vyvolal memory-protection interrupt. S obvyklou nečtenou
guard stránkou a OS politikou ukončení chybného procesu dostaneme
přesně vytištěný page fault/abort. Samotné „nic tam nebylo
uloženo“ **není** důkaz unmapped stránky. Jiný OS může fault
obsloužit jinak; tato vnější politika je přiznaný předpoklad
odpovědi, ne univerzální důsledek aritmetiky adres.

Po platném SAVE do adresy z je v M8[z] hlavička
H=(G<<56)|A; rO=rS=z+8 a L0. Následné POP0 načte H jako
údajný push marker a vezme p=H mod256=A&255. Přijaté POP
pravidlo dává nový rO=z−8p a L=min(p,G). Při p0 tak přejde
na rO=z,L0 bez skutečného zrušení volání. Při p1 přejde na
rO=z−8,L1 a jeho $0 se stane M8[z−8], tedy **uloženým rZ**.
Obě octa pocházejí z platného uloženého kontextu; tento jev
nepotřebuje vadnou adresu. Návrat přesto používá rJ+4YZ,
nikoli obnovení celého kontextu. Pro větší p může marker
vyžádat další starou paměť a případný fault; netvrdíme, že
všechny takové chybné operace mají úspěšný přístup.

Tím je konkrétně doloženo „much more bizarre“ a uzavřena
dosavadní matematická mezera E11. SAVE inverse nebyl znovu
počítán ani spuštěn. Podmíněné OS tvrzení je omezeno výše,
nikoli rozšířeno na skutečné chování každého hypotetického OS.

## 12. Všechny tři prefixové otázky

(a) První prefix je :. Relativní PREFIX se připojí za dosavadní
prefix, absolutní už dvojtečkou začíná. Indukcí tedy každý
prefix začíná :. (b) PREFIX Foo z počátečního : vytvoří :Foo,
bez koncové dvojtečky; tvrzení je false. Případné slepení
poslední části prefixu s názvem symbolu vysvětluje upozornění
na matoucí použití, nejde o zákaz assembleru. (c) : a :: jsou
různé znakové absolutní názvy; MMIXAL neprovádí normalizaci
opakovaných oddělovačů jako cestový systém. Přesné parserové
pravidlo již doložil celý rozbor70.

Vedlejší přirovnání k absolutnímu jménu UNIX pracovního adresáře
není důkaz o libovolné hodnotě proměnné PWD. Přímý oficiální
POSIX odkaz při nové rychlé kontrole vrátil403; přesná univerzální
formulace tohoto historického přirovnání zůstává výslovně
přeskočena. Tři MMIX otázky jsou tímto omezením nedotčeny.

## 13. Všechny Fibonacciho algoritmy a přípustné stavy

Známé erratum29.3.2023 přidává n≥0. Pro konkrétní signed CMP
zde platí0≤n<2^63, platný callerR s R+1<G a dostatečný
register-stack backing pro uskutečněná volání. F se vždy
počítá modulo B=2^64. Při velmi velkém n není slibována
dokončitelnost na konečné nepostačující paměti či v časovém limitu.

Fib: n0/1 vrátí původní n. Pro n≥2 se uloží rJ do1.
PUSHJ2 chrání n0 a návrat1, argumentn−1 v3 se stane0,
výsledek se vrátí do2. PUSHJ3 pak chrání i tento výsledek;
argumentn−2 v4 se stane0 a výsledek se vrátí do3. ADDU0,2,3
vrátí Fn−1+Fn−2 modB, PUT rJ,1 obnoví návrat, POP1 vrátí0.
Všechny SUB n−1/n−2 jsou nezáporné a signed bezpečné.
Silná indukce podle n dokazuje výsledek, návrat a uchování
chráněných míst; každé dítě má menší n, takže při dostatečných
zdrojích strom skončí. G≥32 dovoluje všechna čísla0…4,
žádný global není potřebný. Hloubka je nejvýše n, nikoli
počet všech uzlů; paměť se při každém návratu uvolňuje.

Fib1: pro n0/1 původní vstup. Pro n>1 počáteční(a,b)=(1,0),
counter=n−1. ADDU a,a,b a SUBU b,a,b dávají(a+b,a) i moduloB,
protože druhá instrukce používá nové a a staré b. Po k kolech
je dvojice(Fk+1,Fk), counter=n−1−k. Přesně n−1 iterací dá Fn;
counter nikdy neklesne pod0, konečná PBNZ neskočí.

Fib2: CMP n,1 pro n>1 nastaví1=1, SET0,0 vytvoří(F0,F1).
Dvě ADDU tvoří(F2k+2,F2k+3) z(F2k,F2k+1). Counter je
n−1−2k. Smyčka proběhne floor(n/2) krát; konec je−1 pro
sudé n a0 pro liché n. CSZ v lichém případě vybere1=Fn,
v sudém ponechá0=Fn. Counter je vždy signed bezpečný,
nejmenší hodnota−1. Pro n0/1 BNP přeskočí tělo a vrátí n.
Počet instrukcí na2H je včetně obou základů n−[n≠0] ve Fib1,
floor(n/2) ve Fib2. Všechny tři rutiny jsou bez globals.

## 14. Úplné náklady, včetně základů a tvrzení o rychlosti

Počet listů rekurzního stromu splňuje l0=l1=1,
ln=ln−1+ln−2, tedy l=Fn+1. Plný binární strom má l−1
vnitřních uzlů (indukce při spojení obou dětí). POP se tedy
provede2l−1 krát, ADDU l−1 krát. List stojí CMP1+správné
PBN1+POP3=5υ. Vnitřní uzel bez dětí stojí14υ včetně chybné
PBN3 a obou PUSHJ1. Caller SET+PUSHJ přidá2υ. Celkem
**(19Fn+1−12)υ**; tento vzorec platí i pro n0/1 a dává7υ.

Fib1 pro n>1 má přípravu5υ, n−1 iterací po4υ, dodatečné2υ
za konečnou chybnou predikci, POP3υ a caller2υ, tedy
**(4n+8)υ**. Fib2 má přípravu4υ, floor(n/2) iterací po4υ,
poslední chybnou predikci2υ, CSZ1υ, POP3υ, caller2υ, tedy
**(4 floor(n/2)+12)υ**. Pro n0/1 stojí obě iterativní varianty
9υ (CMP1+vzatý ordinary branch3+POP3+caller2). Fib2 tedy
není nikdy pomalejší než Fib1, jsou stejně rychlé pro n0,1,2
a Fib2 je rychlejší pro n≥3; vytištěná stručná charakteristika
„faster alternative“ se nepřenáší na striktní nerovnost n2.

Přijaté F92,F93 z úplného rozboru1.3.2′–27 dávají
F101=34F93+21F92, a proto19F101−12>1.0889·10^22.
To dokazuje vytištěnou mez pro F100 bez exponenciálního běhu.

## 15. Celý paměťový rámec a realizovaná varianta bez fp

V tištěném programu n=fn je global odlišný od fp,sp, báze
kódu i pracovních $0/$1. Caller $0 je GO návrat; sp ukazuje
na první volný octabyte S a platné navazující rámce mají
32 bajtů, bez adresního přetečení a mimo kód/data volajícího.
U vnitřního uzlu leží staré fp naS, návrat naS+8, n naS+16,
první výsledek naS+24. Nastaví se fp=S,sp=S+32.

Indukční kontrakt dítěte vrací Fn−1 či Fn−2 a obnovuje
rodičovské fp/sp. První výsledek se uloží na24, původní n
se obnoví z16 před SUB2. Po druhém dítěti se ADDU přičte
první výsledek; LDO8 obnoví návrat, SET sp,fp vrátí S,
LDO fp,sp,0 staré fp. List n0/1 nemění fp/sp, vrací původní n.
Všechny paměťové sloty jsou vyplněny před čtením, rámce jsou
disjunktní a $0 lze dočasně použít pro první výsledek až po
posledním child call, před opětovným načtením návratu.

Vnitřní uzel má8 paměťových operací a27υ mimo děti,
list5υ, caller SET+GO4υ. Pro l=Fn+1 je tedy přesně
**8(l−1)μ+(32l−23)υ**. Poměr k registrům konverguje
k(8μ/υ+32)/19. Pro μ=υ je konečný poměr(40l−31)/(19l−12),
větší než2 právě při2l>7, tedy pro n≥4. Pro n2/3 jde
o49/26 a89/45. Vytištěné „approximately“ a následující
srovnání jsou asymptotické; netvrdíme univerzální faktor>2
pro všechny malé vstupy. Věta o podobném chování jiných rutin
je zkušenostní zobecnění, nikoli důkaz pro každou rutinu.

Celý nový program je `sources/fib15-no-frame-pointer.mms`.
Při vstupu nechává sp=S ukazovat na bázi předchozího rámce.
Vnitřní uzel zvýší sp o24 a použije0(návrat),8(n),16(Fn−1).
Dítě zvýší sp opět o24 a indukcí jej obnoví, takže rodič vždy
čte své tři sloty. Návrat sníží sp o24. List sp nemění.
Nevyužitých prvních24 bajtů je součást alokované oblasti,
nikoli překryv rámců. Všechny offsety0/8/16 jsou přímo
kódovatelné a nezáporné. Stejná indukce dokazuje Fn modB,
platný GO návrat, obnovení sp a všechny čtené hodnoty.

Vnitřní uzel má6 paměťových operací a24υ, list5υ, caller4υ:
**6(l−1)μ+(29l−20)υ**, asymptotický poměr(6μ/υ+29)/19,
právě jako vytištěné poslední tvrzení. Nejde jen o odhad
odstraněných instrukcí: úplný zdroj i všechny cesty jsou doloženy.

První sestavovací pokus měl vlastní nepřípustný dopředný
dvouoperandový GO (tělo následovalo až po Main); assembler jej
odmítl a program se nespustil. Zdroj a log jsou zachovány
jako `fib15-no-frame-pointer-initial-forward-go.mms` a
`fib15-no-frame-pointer-initial-build-failure.json`. Po pouhém
přesunu těla před Main proběhl **první a jediný native běh**
n10. Vrátil55, měl1680 instrukcí,528μ a2568υ. l=F11=89
dává528μ+(29·89−20+7)υ;7υ je explicitní režie standalone
driveru SETH/SET výstup/Halt navíc k volací dvojici. Počet
instrukcí je88·16+89·3+5=1680. Celý první úspěšný build/run
trval1.4645s při nice15. Žádný starý Fibonacciho běh ani
tento úspěšný nový svědek se neopakoval. Tento jeden test
dokládá propojení zdroje/profilu; obecný důkaz stojí výše.

## 16. Každý návrat a obě vytištěná rozšíření

Původní protokol: B a každé C uloží své rJ do1. Každý
jejich vnitřní call má R≥2, takže1 je chráněna; za call
následují PUT rJ,1;POP0,0. Normální výstup C nejprve obnoví
své rJ a POP0,2 skočí o8 bajtů za místo následující po call,
tedy přes obě pad instrukce. Nelokální výstup POP0,0 přejde
do rodičovského padu; ten obnoví vlastní návrat z1 a zruší
právě další rámec. Indukcí přes konečný počet aktivních C
a B dojde do A přesně za jeho call B. Každý rámec je zrušen
jednou a rodičovské1 se obnoví dřív, než je použito. Pouhý
JMP tyto rámce neobnovuje a není náhradou tohoto postupu.

**Konstruktivní rozšíření s hodnotou a libovolnou adresou.**
Nechť B/C ukládají vlastní rJ do2. Vnitřní call má R≥3,
R+1<G. Callee vrací dva lokály:0 je hodnota či cílová adresa,
1 je flag0(normální)/1(unwind). POP2 je přenese do caller
R+1 aR v tomto pořadí. Za každý call C vložíme čtyři instrukce:

```text
SET $0,$(R+1)
SET $1,$R
PUT rJ,$2
POP 2,0
```

Normální C nastaví flag0, obnoví rJ z2 a provede POP2,4,
které všechny čtyři instrukce přeskočí. Nelokální C nastaví
flag1 a adresu0, obnoví rJ z2 a provede POP2,0. Pad kopíruje
oba výsledky z čísel≥3 do0/1 bez překryvu a chráněné2
obnoví rJ; další POP je předá stejným způsobem výše. A po
call B má vlastní rámec a podle flagu použije normální hodnotu
nebo GO na vrácenou platnou adresu. Flag umožňuje i adresu0,
která není rezervována jako sentinel. Každý krok uchovává
payload; rozšíření tedy není jen tvrzení „clearly possible“.
Další návratové hodnoty vyžadují odpovídající konečnou aritu
a dost lokálních pozic; netvrdíme neomezenou registrovou aritu.

**GO paměťový protokol.** A před call B uloží svůj sp,fp
a požadovaný target do vyhrazeného záznamu mimo všechny nové
rámce. Zachovaný global může držet jeho bázi. C načte target
do odděleného scratch registru, obnoví sp/fp ze záznamu a
provede GO scratch_link,target,0; obě adresní role jsou odlišné.
Všechny vyšší rámce jsou nyní mrtvé, A rámec se nezměnil.
Požaduje-li rozhraní obnovení dalších globals či návratových
hodnot, záznam je výslovně uloží/obnoví také. Žádné register-stack
PUSH rámce zde nejsou; reset sp/fp tedy stačí pro tento
deklarovaný memory-frame kontrakt. Nejde o automatické provedení
destruktorů či libovolných dalších vedlejších efektů vyššího jazyka.

## Úplnost a meze bloku

Všech16 zadání, všechny kódy a odstavce jejich odpovědí jsou
mapovány výše. E11 má nově konkrétní argument včetně SAVE;
E10 zůstává partial pro přesně uvedenou interpretaci, vedle
samostatných confirmed C0021/C0022. Všechny ostatní úlohy
mají argument v deklarovaném strojovém oboru. Obecné OS,
historické UNIX přirovnání a zkušenostní srovnání jiných rutin
se nevydávají za nové univerzální věty. Celé121 stále obsahuje
neuzavřené E1.3.2′–34 a celé123 začíná další coroutine úlohu;
tyto stránky nelze zazelenit jen dokončením tohoto oddílu.

Použití vzorů: binomický rozbor pro vstupní obory a malé n,
Algorithm R pro přesné rekurence a každou nákladovou větev,
kografový rozbor pro oddělení správné základní sémantiky od
nepravdivé rozšířené věty a od interpretačního partial.
