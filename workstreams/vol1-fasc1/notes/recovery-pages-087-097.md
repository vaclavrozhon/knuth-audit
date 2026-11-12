# Obnova úplného rozsahu: file 87–97 / p. 79–89

Pokrytí zahrnuje každý odstavec, obrázek (2), vztahy (3)/(4)/(5),
řádky 055–309, celou vytištěnou tabulku Info a řádky 500–516,
539–541. Záměrně vynechané obsluhy mají vlastní cvičební důkazy.
Přijaté PUSH/POP/SAVE/UNSAVE důkazy a C0015 se neopakují. Pro
ropcode 1 zůstává konkrétní úloha 14, nikoli neadresná pochybnost
o libovolném hardwaru. Každý níže převzatý výsledek má stejnou
architektonickou doménu jako právě kontrolovaný text.

## 1. File 87: celý ring a obrázek (2)

Přebírá se celý intervalový argument V0149/V0150 z
`independent-arguments-073-082.md`, spolu s explicitní transientní
výjimkou V0153 a odpovědí 3 v `exercises-1.4.3-001-014.md`.
Platné běžné stavy mají 32≤G≤255, 0≤L≤G, ρ mocninu dvou
alespoň 256 a byteově zarovnané rO/rS. V jednotkách octabytů
jsou v ringu reprezentovány po sobě jdoucí logické položky
[S,O+L), s [S,O) pushed a [O,O+L) current. Běžná délka je <ρ;
každá logická pozice j má slot j modρ a mapování na tomto
intervalu je prosté. Modulo jde realizovat maskou ρ−1.

Proto α=O modρ, β=(O+L) modρ a γ=S modρ vymezují právě tři
popsané oblouky. Když se rámec posune o k, staré $(k+i) a nové
$i mají totožný slot; návrat mění počátek opačně. Žádné hromadné
kopírování lokálů není potřebné. Při běžném store pushed položky
se její hodnota uloží před S←S+1. Při loadu se nejprve sníží S
a načte přesně připojená položka do dosud volného slotu. Fyzická
rychlost registrů je motivace tohoto modelu, ne změřená univerzální
poměrná rychlost každého stroje.

Originál `images/file-087-p079.png` byl zobrazen: oblouk L jde
od α k β a γ leží v ostatní části kruhu, v souladu s uvedeným
pořadím. Kruh neudává absolutní počty oběhů; ty nese O/S. Při
L=0 může být α=β a při prázdném cache α=β=γ. Stejné residue
samotné nerozlišují prázdný a plný ring; volající zná změnu
logického intervalu. Právě proto StackRoom následuje **přírůstek**
β, nikoli libovolné volání na prázdném ringu.

Vztah (3) užívá rO/8 a rS/8, protože skutečné registry jsou
byteové adresy. Simulační ll=8L a gg=8G dovolují další indexaci
bez nového násobení. Všech sedm zvlášť uložených special registers
je přesně ss,oo,ll,gg,aa,ii,uu; cc je vlastní modelový čas,
nikoli osmý přidaný architektonický special register. První čtyři
GREG 055–058 mají oddělené nulové inicializace.

## 2. File 88: GetReg a přesun hranice cache

059–062 doplňují zbylé tři hodnoty a clock. GREG nuly se
neslučují, takže se živé proměnné nepřekryjí. `8ρ−1` maskuje
byteový offset do vyhrazených 8ρ bytů Local.

GetReg je již úplně doložen V0151 a C0012. Jeho vstup 8k je
v [0,2040]. Pro k≥G vrátí Global[8k]. Jinak si CMP proti ll
uchová výsledek k<L před tím, než přičte oo a zamaskuje index.
Pro k<L vrátí správný ring slot, pro k≥L ho CSNN přepíše nulou.
I marginal načtení je uvnitř vyhrazeného pole; nedefinovaná stará
hodnota se nikde nepoužije. Zdrojové čtení nikdy nezvětší L.
Celá doména 256 registrů je tím rozdělena na tři disjunktní
případy. Volajícího SLU/PUSHJ předá 8k do callee $0 a POP 1
vrátí právě jednu hodnotu.

Cena je μ+6υ pro global a μ+12υ pro **každý nonglobal**, tedy
i marginal; přesný rozpis a původní chybný údaj v odpovědi má
C0012. V tomto bloku se jeho výpočet ani svědek neopakují.
Redundantní úvodní colon na 064 odpovídá PREFIX :, zatímco
exportovaný :MemFind pod PREFIX :Mem: colon potřeboval. Je to
přesně již dokázaný namespace kontrakt, nikoli jiná sémantika
podprogramu podle grafické podoby labelu.

StackStore 074–082 uloží l[S modρ] přes MemFind do M8[rS],
pak zvýší rS o osm; StackLoad 083–091 sníží rS před lookupem
a načte tentýž virtuální octabyte do odpovídajícího slotu.
V obou je skutečné rJ v $0 a přenášená hodnota v $1, chráněné
PUSHJ res=$2 před lokály MemFind. MemFind ani volatilní host
$255 tyto dvě hodnoty nepřepíší. Obnoví se skutečné rJ, nikoli
simulované g[rJ]. Každá rutina má cenu 2μ+11υ+M, kde M je
celá právě provedená cesta MemFind včetně jejího POP, a končí,
pokud tento lookup uspěje. Error při nepřípustné virtuální
adrese je výslovný konec, nikoli nevracející se platná větev.

Věta „called only when γ≠α/β“ je čtena s **výslovnou vlastní
výjimkou odpovědí 3 a 10**. Není rozšířena na invariant každého
vnitřního mezikroku: global PUSH/SAVE může přechodně zaplnit
ρ=256 current položkami a POP smí přepsat zahazovaný nejvyšší
slot. Oba případy mají přijaté úplné důkazy zachování hodnot.

## 3. File 89: StackRoom a obě cesty Fetch

Po jediném růstu β je délka cache nejvýše ρ. 092–095 testují
(rS−rO−ll)&(8ρ−1), tedy právě rovnost γ=β. Nenulový výsledek
má volné místo a končí. Nulový znamená po tomto růstu plný ring;
jedno StackStore uvolní právě jeden slot. Pro L≤255<ρ je tu
pushed položka. Pro přechodné L=ρ při global PUSH/SAVE je
uložená nejstarší current položka vzápětí pushed; její hodnota
zůstává v paměti pro pozdější POP/UNSAVE. Zbytek stavu se
nepřepisuje. Skutečné rJ se ukládá až ve větvi, která ho voláním
StackStore přepíše. Nominal no-store cena je 7υ, plná cesta
12υ plus celá StackStore; nejsou zahrnuty externí spill náklady
hostitele mimo deklarovanou tabulku instrukcí.

Fetch 105–115 má dva případy: resuming=0 uloží původní next
do loc, načte unsigned M4[loc] a next posune o čtyři. Nenulový
resuming načte pravou polovinu g[rX], nastaví loc=next−4 a next
nemění. Jsou to přesně dvě polohy vložené instrukce architektonického
RESUME. Horní polovina g[rX] se nenačte jako opcode. Finální
unsigned test loc<Data_Segment odmítne všechny adresy mimo text
včetně těch s high bitem 1. U normální cesty může před tím
MemFind připravit chunk odmítnuté adresy; program stejně skončí
Error a netvrdí zachování neplatného vstupu. Zarovnání hostitelského
LDTU je ekvivalentní virtuálnímu načtení podle uzavřeného chunk
argumentu. Všechny zde deklarované globální proměnné jsou oddělené.

## 4. File 90: každé pole, maska a ukazatel Info

unsigned inst má jedině čtyři nenulové byteové pozice OP,X,Y,Z.
Bitový/MOR důkaz z V0155 vybere maskami #8,#4,#2,#1 právě
tyto byty do pravého bytu výsledku. Zbylé byty jsou nula.
ANDN s −2^16 ponechá YZ. Násobení X/OP osmi nepřeteče:
maximální offset je 2040. LDOU proto vybere přesně jeden
osmibytový záznam Info[OP]. 256 záznamů od #1000 vyplní
#1000…#17ff a následující Done je #1800.

Osm flagů 1,2,4,8,16,32,64,128 je navzájem disjunktních.
Každý níže uvedený test maskuje pouze příslušný bit. Po načtení
záznamu se x,y,z,exc vždy nulují, takže chybějící operand ani
event nezdědí stav předchozí simulované instrukce. f je jen data
a hostitelské předinstrukční operandové registry jsou oddělené od
virtuálních $X,$Y,$Z.

Tvrzení o lichém f a Rel_addr_bit nyní není jen kontrola vzorku:
všech 256 příznaků má úplnou tabulkovou evidenci v části 9.
JMP/JMPB užívají #1 jako výslovnou zvláštní značku 24bitové
adresy, nikoli jako požadavek získat ještě třetí běžný operand.
Immediate wyde má naopak jeden šestnáctibitový YZ operand;
jednotlivé pole Z tu není samostatný immediate argument.

## 5. File 91: relative, X/special/Z/Y a vynechaná větev

154–164 mají úplný důkaz V0157. Pro relativní ne-JMP instrukce
je d=YZ nebo YZ−2^16 podle parity opcode; pro JMP/JMPB je to
XYZ nebo XYZ−2^24. Flag #1 rozlišuje obě šířky před testem
parity. Signed 4d leží v [−2^26,2^26−4], takže SL o dva
bity nepřeteče; ADDU s loc dává správný modulární cíl. Stálé
−2^16 a −2^24 se nepletou se znaménkovým rozšířením samotného
unsigned YZ. U nerelativních instrukcí yz zůstane původní YZ.

174–182 nejprve načtou starý X pro CS, stores či wyde-modify.
`(f>>5)&#f8` vybere special byte násobený osmi; 0 znamená
žádný implicitní zdroj. Použity jsou rD pro DIVU, rE pro tři
epsilon porovnání, rM pro MUX a rJ pro POP. Každý je načten
před změnou odpovídajícího výsledku. Žádná obsluha nepotřebuje
implicitní rB=0, které by se se sentinel hodnotou pletlo.

183–197 rozdělí register/immediate Z. Volání GetReg(8Z) načte
starou hodnotu; immediate flag nastaví z=Z∈[0,255]. Pro op
#e0…#ef se místo toho sestaví z=YZ·2^(48−16(op&3)). Pole má
nejvýše 16 bitů, takže všechny čtyři umístěné wydes jsou přesné
octabyty. y=x umožní původní hodnotu u modify rodin; SET ji
ignoruje. Všechny zdroje se instalují před XDest, a tedy i
aliasování X=Y, X=Z, Y=Z zachová předepsané staré hodnoty.

198–207 instalují immediate Y nebo register Y podle disjunktních
flagů. U immediate Y má každá hostitelská šablona v příslušném
bytu nulu, a přičtení Y<<40 proto tento byte vyplní bez přenosu
jinam. To zahrnuje číselný operand NEG/NEGU i explicitní rounding
pole FIX/FLOT/SFLOT/FSQRT/FINT. Kód se nesnaží číst $Y tam,
kde je operandem číslo Y. Illegal rounding mode může odmítnout
hostitelská instrukce; tvrzení o správné simulaci je pro platné
uživatelské instrukce, ne o jednotném recovery neplatných slov.

165 rozlišuje resuming<0. **Konkrétní zbývající mezera na této
straně jsou úlohou 14 doplňované řádky 166–173 pro ropcode 1**,
nikoli znovu dokazovaná běžná instalace. C0015 je již úplný
protipříklad k vytištěné odpovědi; úplný opravený převod všech
povolených rodin se dokončí zvlášť. Proto file 91 zatím není
označena úplnou jen díky správnosti ostatních řádků.

## 6. File 92: cíl, paměť a vložení hostitelské instrukce

XDest 208–223 přebírá V0161. X≥G dává Global+8X. Jinak se
pro marginal X opakuje uložení nuly do dosud volného slotu β,
L←L+1 a StackRoom, až je L=X+1. Horní mez X<G≤255 zajistí
nejvýše 255 přírůstků a žádné překročení G. Každý starší local
zůstane správný v ringu nebo jako pushed v paměti. Výsledný
xptr ukazuje na přesný slot X; zápis výsledku je odložen až
po práci se zdroji. Signed ADD v 221 případně nastaví **host** V,
ale jeho enable je při těchto pomocných cestách vypnutý a 239
host rA před vlastní operací znovu nastaví; nesmí se tento
pomocný event zaměnit za simulovaný overflow.

224–231 sčítají y+z modulo 2^64 a překládají přes MemFind,
jehož invariant zachovává zarovnání pro všechny šířky. Hostitelský
operand res+0 tedy přistupuje na stejné virtuální byty. Pro
op≥#a0 se navíc vyžaduje A≥Data_Segment, zákaz zápisu textu
podle runtime konvence. CSWAP je #94 a tímto guardem neprochází,
ale správnost jeho podporované domény vyžaduje již deklarovaný
program bez zápisu do textu; nejde o slib úplného sandboxu pro
každý neplatný guest. Cache hints nemají Mem_bit a nemusí
alokovat chunky pro oblasti, na něž pouze upozorňují.

232–242 vloží horní čtyři byty f do spodní poloviny host rX,
horní rX=0 tedy volí ropcode 0. Host rW=Done určí umístění
vložené instrukce Done−4. Nastavení rM/rE z x se děje před
host výsledkem a zachová správnou masku/epsilon. rA získá jen
virtual rounding bits #30000 a host U-enable, všechny staré
eventy i ostatní enables se vymažou. Přímá aritmetika proto
nezpůsobí neošetřený host D/V/W/I/O/Z/X trip; zachová jejich
event bits pro Done. Přesné zachycení U je dokázáno v části 10.

Je to aplikace architektonického RESUME 0 na řádně vytvořené
instrukční slovo. Vložený opcode nikdy není RESUME: i guest
RESUME má hostitelské JMP do své obsluhy. Obecná chybná guest
obsluha C0015 se proto do této hostitelské invokace nepřenáší.

## 7. File 93–94: výjimky z přímého vykonání a celé PUSH

MULU je pokryt V0164: host low x a high rH jsou oba části
téhož unsigned 128bitového součinu; GET/STOU uloží high před
XDone, který zapíše low. Signed/unsigned DIV doplňuje již
uzavřená úloha 6 se zachováním původního rD a všech výsledků
rR, včetně nulového dělitele a high≥divisor. Zde žádný starý
aritmetický algoritmus znovu nespouštíme.

Obyčejné větve mají v Info základ 1υ; taken cesta 254/255
přidá 4−2=2υ. Probable větve mají základ 3υ; taken vstoupí
až na 255 a odečte 2υ. Netaken větev do těchto řádků nevstoupí.
Jsou tak přesně čtyři ceny podle pravdivosti testu a předpovědi.
Všech osm predikátů i oba směry mají původní x a absolutní
yz. Taken změní next na yz. Přímý skok Update nevynechá
výsledek ani event, protože branch nemá dest a neprovádí
aritmetiku s výjimkou. GO nejprve uloží původní next do x,
potom změní next na y+z a XDone zapíše link; aliasy guest
registrů už byly ošetřeny oddělenými starými operandy.

261–277 se přesně přiřazují k přijatému logickému V0121–V0123
a ring V0153/V0167. Marginal X již předtím rozšířilo L.
Pro local X je marker=X a do pushed části přejde X+1 hodnot;
pro global X se nahradí X starým L, vytvoří marker a případně
spillem uvolní transientní plný ring. Na 269–271 se marker
uloží na původní pozici O+X, 272–273 uloží loc+4 do g[rJ],
274–276 nastaví L'=L−(X+1) a O'=O+8(X+1). Přesně tento
marker pozdější POP použije; global varianta má L'=0. PUSHGO
nejprve sestaví yz=y+z, PUSHJ má již relativní absolutní cíl.
Neopakujeme obecnou inverse ani její krajní případy G=255.

Výslovné odložení POP/SAVE/UNSAVE/RESUME do úloh neprohlašuje
jejich implementaci za hotovou na této stránce. Zachovány jsou
C0007/C0014/C0015 a konkrétní další cvičební povinnosti.

SYNC 278–281 kontroluje X=0 a YZ<4, právě povolené user
XYZ=0,1,2,3. Model nemá cache ani paralelní paměťové operace,
proto stačí zachovat stav a započítat cenu. Privilegované
rozšíření 4–7 sem nepatří. TRIP 282–283 nastaví index handleru
0 a použije obecný vstup; nevyžaduje aktivní arithmetic enable.

Trap 284–293 uloží už určený next do rWW, původní inst+2^63
do rXX a staré y,z do rYY/rZZ. Pak teprve pracovní y přepíše
dispatch indexem. Protože opcode TRAP=0,
inst>>6=1024X+4Y+floor(Z/64). Test <44 je ekvivalentní X=0
a Y≤10. V posledním bytu může být libovolný handle Z; jeho
horní dva bity nezmění čtyřbytově zarovnaný jump-table index.

## 8. File 95: celá tabulka skoků a relocace

GO 295 použije starý y jako offset a pak ho přepíše svým
linkem. Základ je adresa první JMP, takže po ignorování spodních
dvou bitů míří přesně na její Y-tou čtyřbytovou položku.
Všech jedenáct položek 296–306 má pořadí definovaných služeb
Halt,Fopen,Fclose,Fread,Fgets,Fgetws,Fwrite,Fputs,Fputws,Fseek,Ftell.
Původní raw TRAP inst zůstane k dispozici pomocným obsluhám,
protože přepis yy/zz/xx nebo y není přepis uložené instrukce.
Po normálním I/O návratu je t výsledek; 307–309 uloží stejnou
hodnotu do rBB i virtuálního $255 a právě jednou přejde Update.
Rutiny služeb mají samostatné úlohy 15–17; tabulka sama není
důkaz jejich celého I/O chování. Halt bez návratu byl rozhodnut
v X0061 a nepoužívá TrapDone.

Info má přesně 4+1+1+1+1=8 bytů. FIX příklad #26 znamená
destX, immediateY, sourceZ, bez implicitního special source,
cenu 0μ+4υ. Nulový Y byte host FIX je naplněn 202; není to
pevné ROUND_NEAR ignorující původní Y.

Pro každé vložené relativní host JMP/branch nastavíme
O=Done−4. Sestavovací cíl T+@−O má displacement T−O, protože
assembler odečte @. Vložení na O tudíž skočí na T. Všechny
zdejší helper adresy i Info jsou v krátkém vlastním textovém
úseku programu a displacement bezpečně leží v 16/24bitové
tetra-adresní doméně; nejsou tu absolutní virtuální guest adresy
ani hraniční obrovské relative výrazy ze samostatného S0007.

## 9. File 96: všech 256 záznamů a všech 95 vytištěných řádků

Originál `images/file-096-p088.png` zobrazen celý. Nejde již
jen o domněnku, že se dají výpustky doplnit. Nový konečný
`verify_interpreter_info_table.py` má nezávislé pravidlo podle
architektonické role každé z následujících disjunktních rodin.
Ověřuje host instrukci, special source, všechny flagy i cenu
pro 256 řádků primárního `sim-20250620.mms`, a všech 95
vytištěných řádků porovnává po každém poli. Úplný výsledek je
`results/interpreter-info-table-reconciliation.json`, bez rozdílu.

| Opcode rodina | Host a příznakový závazek |
|---|---|
| 00 | Trap helper; staré Y/Z, #0a, 5υ |
| 01–17 | Stejná FP operace; #2a pro binary, #26 pro unary/rounding; FLOT/SFLOT immediate #25; epsilon navíc rE |
| 18–33,38–3f | Signed běžná arithmetic/shift stejný host; MULU/DIV/DIVU příslušné helpers, poslední rD; #2a/#29 |
| 34–37 | NEG/NEGU mají immediateY a Z source/immediate, #26/#25 |
| 40–4f | Stejný predikát do BTaken, starý X a relativeYZ, #50, základ 1υ |
| 50–5f | Stejný probable predikát do PBTaken, #50, základ 3υ |
| 60–6f | CS zachovává starý X, #3a/#39; host identický predicate |
| 70–7f | ZS nepotřebuje starý X, #2a/#29 |
| 80–93,96–97 | Stejný typ loadu z res+0, Mem+dest+Y/Z, #aa/#a9 |
| 94–95 | CSWAP helper, současně source/dest X, #ba/#b9, 2μ+2υ |
| 98–99 | LDVTS je v tomto user modelu Error; #2a/#29 |
| 9a–9d,b8–bd | PRELD/PREGO/SYNCD/PREST/SYNCID bez cache, SWYM, Y/Z #0a/#09 |
| 9e–9f,be–bf | GO/PUSHGO helpers, dest+Y/Z #2a/#29, 3υ |
| a0–b3,b6–b7 | Stejný store typu do res+0, sourceX+Mem+Y/Z #9a/#99 |
| b4–b5 | STCO uloží samotný byte xx v octabytu, bez čtení $X, #8a/#89 |
| c0–df | Stejné bitové/difference/matrix operace, #2a/#29; MUX navíc rM |
| e0–e3 | SET x,z po sestavení wyde, pouze dest #20 |
| e4–ef | ADDU/OR/ANDN x,x,z, source+dest #30 |
| f0–f1 | SET next,yz, #41 pro 24bitové relative; 1υ |
| f2–f3 | PUSHJ helper, relative+dest #60; 1υ |
| f4–f5 | GETA přes SET x,yz, #60; 1υ |
| f6–f7 | PUT helper, jen Z source/immediate #02/#01 |
| f8 | POP helper, implicitní rJ, žádný obecný source/dest flag, 3υ |
| f9 | RESUME helper, žádné běžné operandy, 5υ |
| fa–fb | SAVE dest #20 / UNSAVE sourceZ #02; 20μ+1υ |
| fc–ff | SYNC #01, SWYM #00, GET dest #20, TRIP Y/Z #0a; 1,1,1,5υ |

Párová immediate varianta nahrazuje bit sourceZ=2 bitem
immediateZ=1; ostatní příznaky zůstávají. Forward/backward
branch pár má naopak tutéž host instrukci, neboť směr je už
zahrnut do yz. Proto nejsou tyto dvě parity zaměněny.

Ceny se porovnaly s již přijatým úplným certifikátem
`results/opcode-table-reconciliation.json`; žádná tabulka
základních nákladů se znovu nepočítala. Probable větev má
odlišnou **reprezentaci** téže ceny: Info 3υ minus 2υ při
taken, základní certifikát 1υ plus 2υ při not-taken. První
vlastní kontrolní pokus tento rozdíl zapomněl, druhý omylem
zahrnul heading do regexu. Oba vlastní omyly jsou uloženy v
`results/interpreter-info-initial-comparison.json`; nejsou
nálezy. První úplná úspěšná kontrola měla 256/95 shod, nice15,
bez assembleru, spuštění MMIX nebo opakování úspěšného běhu.

V0173 se tím uzavírá v **rozsahu tabulky**: operandové bity,
rounding pole a implicitní rE se přenesou na stejnou FP
architektonickou operaci. Raw NaN, signed zero i libovolný
binary64 vzor se kopírují bez numerické konverze a bez ztráty
payloadu. Jde o ekvivalenci kroků téhož architektonického
stroje pro všechny hodnoty; nepotřebuje znovu dokazovat C
implementaci froot/fremstep/fpack. Samostatné výsledky, opravy
S0001–S0004 a zbývající široké IEEE tvrzení V0054/V0055 jsou
nadále vedeny zvlášť. Správnost Info neznamená správnost
vytištěného Resume/Save helperu; existující konkrétní nálezy
se tím neskrývají ani nepřipisují správné tabulce.

## 10. File 97: každý event, přesný underflow a update maska

500–502 uloží x jen při dest flagu. Ostatní příkazy nesmějí
použít starý xptr. Speciální obsluha přecházející rovnou XDone
má dest zajištěný svým vlastním kontraktem. 503–505 sjednotí
host sticky events s exc, do něhož mohl mezitím vstoupit
underflow handler nebo ropcode 2. Staré host eventy byly před
každou vloženou instrukcí vymazány, staré virtuální sticky
eventy jsou naproti tomu v aa a neovlivňují tento nový výběr.

Ověřený primární MMIX-doc 1221–1238 a 1979–2020 stanoví,
že exact subnormal vyvolá U právě při enabled U; inexact
underflow má U i X. Na výsledku standardní operace se při
trippingu nic samo dodatečně nemění: každá operace jej ukládá,
a doc 2193–2208 výslovně vysvětluje, jak **handler** může
později nahradit defaultní výsledek. Není zde převzat širší
IEEE trapping interface s upraveným exponentem; to je přesně
samostatná dosud otevřená otázka V0054.

Host U-enable je vždy 1, a proto host detekuje i exact U.
V tom případě je výsledek už vytvořen; U handler na #60
provede pouze `ORL exc,U_BIT; JMP Done`. Nezmění x ani
virtuální paměť. Host trip vedle PC zapisuje host rB/rW/rX/
rY/rZ a host $255; žádný z nich není virtual g[] ani pracovní
global x,y,z,f,exc. Host $255 je zde právě scratch t a Done
jej znovu stanoví. Host rJ se tripem nemění. Přepsaný host
resumption kontext už tato iterace nepoužije a před příští
vloženou instrukcí se rX/rW znovu nastaví. V handleru ani
Done není jiná FP operace, která by rekurzivně trippingovala.

Všechny možnosti U/X a virtual U-enable jsou nyní vyčerpány:

| Nové události host operace | Virtual U-enable | Výsledek 506–512 |
|---|---:|---|
| bez U | 0 nebo 1 | žádný U se nepřidá ani neodebere |
| U bez X | 0 | U se odstraní |
| U bez X | 1 | U zůstane pro virtuální trip |
| U a X | 0 nebo 1 | obě události zůstanou |

Ostatní event bity AND U|X netestuje a ANDNL U je neodstraní.
Host U-trip sám svůj U event nezaloguje, ale explicitní ORL
ho zachová v exc. Případný X současně zůstane v host rA,
protože host X-enable je vypnutý; GET a OR ho připojí. Vznikne
tedy přesně tentýž virtuální event/trip vstup jako podle MMIX
pravidla. Stejné booleovské pravidlo působí na ropcode2 Q,
jak stanoví jeho primární postprocessing kontrakt; nová
aritmetická operace při tomto ORI nevzniká.

513–516 při exc=0 přejdou rovnou Update. Jinak AND s aa>>8
vybere právě enable průnik. Je-li prázdný, 539 připojí všechny
nové eventy do aa. Je-li neprázdný, chybějící úloha 13 vybere
nejvyšší bit a odstraní pouze tuto obslouženou událost; ostatní
se také připojí na 539. Rounding/enables v aa se tím nemění,
protože exc používá jen pravých osm bitů. Konkrétní operandový
kontext tripů je v samostatném cvičebním rozboru, ne zameten
do tohoto obecného event důkazu.

Odstavec o duplicitním Done je správný: oba labely mají stejný
typ a hodnotu #1800, což assembler dovoluje; právě C0017
samostatně rozlišil tuto podmínku od příliš silného obecného
zákazu duplicitních labelů. Číslo 500 je číslování výkladu,
nikoli počet strojových instrukcí nebo nová adresa.

540–541 MOR s #0000000800000004 umístí byte mems z f do
byteové pozice 4 a byte oops do pozice 0. Výsledkem je
přesně 2^32·mems+oops; žádné instruction bits ani flagy se
nepřipojí. Pokračující ADDU a counter logika jsou na file98.

## 11. Výsledek a konkrétní použití vzorů

V0173 a V0175 jsou argument_recorded pro přesně vytištěné
tabulkové a řídicí závazky. V0054/V0055 tím nezískávají
automatický důkaz širších vnějších tvrzení. File87–90 a92–96
mají úplné pokrytí vlastního obsahu; file91 drží konkrétní
ropcode1 povinnost. File97 má úplný vlastní event/U důkaz,
ale celkový trip kontext doplňované úlohy13 zůstává při této
aktualizaci samostatně otevřený; stránka se zatím nezelení.

Binomický vzor se použil na přesný povolený interval a
transientní hranice, Algorithm R na skutečné větve a odlišné
reprezentace nákladů, kografový vzor na úplné rodiny místo
vzorku a na oddělení správného invariantního jádra od
nezávislých silnějších tvrzení. Žádný původní successful test,
SAVE inverse ani potvrzený ropcode protipříklad se neopakoval.
