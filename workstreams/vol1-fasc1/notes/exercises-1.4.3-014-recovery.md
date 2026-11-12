# MMIX — úplná obnova argumentu §1.4.3′–14, RESUME

Rozsah: celé zadání p.92/file100, celá odpověď p.122–123/file130–131,
vynechané166–173 a řízení Fetch/AllDone. Již přijatý C0015 se
přebírá bez opakování svědka. Nový nezávislý zákaz ropcode2 má
samostatný C0023. Tento rozbor doplňuje obecnou konkrétní opravu,
nikoli tvrzení, že celý neupravený sim.mms je správný.

## 1. Přípustné stavy a invariant vložení

Přebírají se plné ring, tabulkové a operandové invarianty z
`recovery-pages-087-097.md`: 32≤G≤255, 0≤L≤G, ρ≥256,
platná konečná simulovaná paměť a autorův uživatelský model bez
privilegovaného RESUME1. Adresy se počítají modulo2^64;
při nedovoleném přístupu má tento jednoduchý interpret skončit Error.
Vstup do Resume má `inst=#f9000000`, ordinary resuming0.
Jiná XYZ je chyba. Obyčejný vložený RESUME se předem zakazuje,
takže Resume nevstupuje s kladným resuming z ropcode0.

Je-li rX záporné, načtené inst_ptr=rW přetrvá, resuming zůstane0
a Update provede normální vnější cenu5υ. Žádné ropcode testy
nejsou relevantní. Je-li rX nezáporné, jeho první byte r∈[0,127].
`t=r−2` je bezpečné signed číslo−2…125. Větve přijmou pouze0,1,2:
r0 přeskočí normal/X testy, r1 projde normal maskou, r≥2
vstoupí na1H a BP odmítne všechna r>2. Pro r1/r2 přesné
8X porovnání s8L a8G přijme právě X<L nebo X≥G.

Pro r1 má maska#70cf právě bity0,1,2,3,6,7,c,d,e. Posun1<<k,
0≤k≤15, nemůže přetéct. ANDNL odstraní právě povolené bity;
ostatní vedou Error. To je všech144 povolených opcode hodnot.
Ropcode0 nesmí mít OPf9. Ropcode2 nesmí tento test podstoupit:
samostatný důkaz a oprava jsou C0023.

NEG+CSNN vytvoří resuming1,−1,−2 pro r0,r1,r2. Zápis−r je
bezpečný. Update ještě účtuje vnější RESUME; AllDone jeho opf9
ponechá resuming. Následující Fetch nepřečte instrukční paměť:
vezme spodní32bit rX, nastaví loc=rW−4 a zachová inst_ptr=rW.
Všechny běžné pracovní x,y,z,exc se nulují. Po vložené instrukci
se resuming odstraní, protože její skutečný opcode není RESUME.
Ropcode2 proto musí současně s náhradou f nastavit opORI.
Relative preprocessing případného zahazovaného OP u r2 mění
jen dočasné yz a nemá vedlejší architektonický účinek.

## 2. Přesný význam operandů, včetně třetích vstupů

Zadání výslovně nahrazuje normální y,z plnými octabyty rY,rZ.
Nejsou to čísla registrů, bezprostřední8bit hodnoty ani dosud
neposunuté wyde. Kniha pro ropcode1 neupřesňuje implicitní třetí
operand všech operací. Zde přijímáme **konkrétní autorův model**:
MMIX-SIM1364,1738–1750,2640–2649 i MMIX-PIPE1985,2024–2036,
5806–5818 nulují třetí operand a obcházejí celou běžnou instalaci.
Neprohlašujeme tento výběr za jedinou fyzikálně možnou realizaci
stručné věty „assuming this makes sense“.

V opraveném interpretu tedy x0 z Unpack zůstane nulové do vlastní
operace. Tím CS při neplatné podmínce dává0, MUX používá masku0,
DIVU má horní polovinu0 a epsilon porovnání epsilon0. Nečtou se
ani starý virtuální X, ani virtuální rD/rM/rE. Host PUT rM,x,
PUT rE,x a DivU PUT rD,x instalují právě0. MULU naopak nadále
zapíše vlastní novou horní polovinu do virtuálního rH; DIV/DIVU
zapíší správný rR. Zvolený model souhlasí s oběma primárními
implementacemi, nikoli jen s několika testy.

`InstallDest` je nové jméno stávajícího testu X_is_dest_bit.
Má-li instrukce cíl, předem prokázaná nemarginal podmínka
vylučuje smyčku rozšiřující L. Global a local pointery jsou
stávajícími invarianty platné; aliasing X/Y/Z nevadí, protože
oba uložené vstupy už jsou načtené. Bez cílového flagu se žádný
X pointer neinstaluje. To je podstatné například pro TRAP.

## 3. Rozklad všech144 povolených opcode hodnot

Rodiny jsou disjunktní a úplné:12 FP instrukcí s režimemY,
4 NEG/NEGU,16 wyde a112 ostatních. Tabulka všech256 Info
záznamů má samostatnou úplnou kontrolu
`results/interpreter-info-table-reconciliation.json`; zde se
nepřebírá pouze vybraný reprezentant rodiny.

### A. Dvanáct FP instrukcí s režimemY

Jde o05,07,08–0f,15,17. Hostitelský Info tvar má nulový Y byte
určený k dosazení immediate režimu. Prvních64bit rY se porovná
unsigned s5. Hodnoty0…4 jsou přípustné, každá ostatní včetně
všech záporných signed reprezentací vede Error ještě před
hostitelskou operací. Tím se žádný vysoký bit potichu neztratí.
Při průchodu je `y<<40` přesně hodnota hostitelského Y byte;
OR nemůže zasáhnout OP,X,Z ani spodní metadata. Nula znamená
uložený režim aa,1…4 příslušné explicitní režimy.

Všechna Z zůstávají plnými64bit rZ, i u FLOTI/SFLOTUI.
Info používá odpovídající registrovou hostitelskou variantu;
bezprostřední přípona virtuálního opcode tedy neopravňuje
zkrátit uložený operand na byte. Signedness a short/long
volba jsou v původním opcode Info zachované. Samotná
aritmetika se deleguje normativnímu MMIX hostiteli; konkrétní
chyby dodávané C aritmetiky S0001–S0004 zůstávají samostatné.

### B. Čtyři NEG/NEGU

Pro34/35 se host NEG s8bit immediateY nahradí registrovým
SUB; pro36/37 registrovým SUBU. `op&2 | #24` dává přesně24/26.
Nahradí se pouze horní opcode byte f a hostitelský Y byte
se nastaví na číslo pracovního registru y. X,Z a všechna
metadata zůstanou. Pro libovolné64bit u,v je výsledek u−v
modulo2^64. Signed SUB vyvolá V právě při rozdílu mimo
[−2^63,2^63−1], stejně jako normativní NEG se dvěma uloženými
operandy; unsigned varianta V nevyvolá. Nejsou potřeba meze
u≤255. Uložené y,z zůstanou dostupné pro případný trip.

### C. Všech16 wyde instrukcí

E0–E3 mají host SET x,z: výsledek je celé rZ, bez dalšího
posunu. E4–E7, E8–EB, EC–EF mají původně ADDU/OR/ANDN x,x,z;
jejich Y byte se změní z pracovního x na pracovní y. Dostaneme
po řadě rY+rZ mod2^64, rY OR rZ a rY AND NOT rZ. Zbytek f
se zachová. Rozlišení čtyř poloh wyde už bylo provedeno v
nahrazeném normálním operandu; zvláštní rZ se neposouvá podruhé.

### D. Zbylých112 opcode hodnot

Jejich Info nepoužívá immediateY a již jmenuje pracovní y,z.
Přeskočení přímo do InstallDest ponechá plná rY/rZ. Patří sem
všechna ostatní celočíselná/binárníFP/bitová porovnání a operace,
32 podmíněných přiřazení a TRAP. Přípona immediateZ nehraje
roli, protože Info již počítá s pracovním z. Posuny dostávají
celé z; hostitelská definice pokrývá i z≥64. BinárníFP drží
syrové64bit NaN, nekonečna i znaménkové nuly.

TRAP nemá X destination flag; uložené y,z se použijí pro
rYY/rZZ. Výběr jeho služby i handle je nadále dán původním
instrukčním slovem a argument je ve virtuálním$255, stejně
jako ve standardním Trap helperu. Nelegální služby mohou
skončit Error. Náhrada operandů neslibuje opravu existujících
jiných I/O helperů; jejich samostatné důkazy a mezery zůstávají.

## 4. Ropcode2, všechny Q a pokračování

Původní OP,Y,Z nemají na set vliv. f dostane ORI x,z,0,
dest flag a cenu1υ; op se nastaví naORI pro AllDone. Tři
čtení instalují rY,rZ,rX a MOR#20 vybere přesně Q∈[0,255].
Nemarginal X se zapíše a společný Done zpracuje Q.

Toto není nekontrolovaná delegace256 kombinací. Označme enable
byte E, starý event byte A a Q aktuální events. Podle explicitní
MMIX-SIM2581–2586 výjimky se U vymaže, pokud U∈Q, X∉Q a
U∉E — **výslovně i pro RESUME_SET**. Nejde tedy o nový nález
z izolované věty „any subset“. Pro zbylé Q′ se při Q′&E=0
nastaví A OR Q′. Jinak se vybere nejvyšší bit q v Q′&E,
provede jeho handler a zaznamená A OR(Q′\{q}). Původní další
event bity nejsou kandidáty na nový trip. Zbytek aa včetně
režimu se nemění. Důkaz prioritní smyčky je převzat ze starého
§13; v dalších poznámkách se řeší pouze přesná store metadata,
která tento ORI set bez Mem_bit nemá.

Virtuální trip po set zachytí původní inst, rW a uložené y,z
podle knižního modelu; hodnoty mimo běžný tvar X=YopZ jsou
v primárním dokumentu obecně implementačně určené. MMIX-PIPE
rovněž zachovává rY/rZ, kdežto C MMIX-SIM pro svůj interní ORI
má y=rZ,z0. Netvrdíme jejich rovnost v každém záznamu tripu.
Při návratu z Done AllDone vidí opORI, jednou zruší resuming
a další Fetch přijme rW nebo adresu zvoleného trip handleru.

## 5. Konečnost, ceny a úplné větve

Nový setup neobsahuje smyčku. Vstupy jsou64bit slova,
opačné masky mění jen požadované byty f. Tři nové GREG mají
nenulové konstanty a neposouvají explicitní pracovní registr
čísla; assemblerový listing dokládá legální globální přidělení.
Nevkládají žádná data do instruction streamu ani nemění
existující lokální číselná návěští.

Cena od prvního LDOU na166 až po závěrečný JMP do InstallDest
nebo XDest, mimo společné destination/execution/Done:

| Cesta | Nominální hostitelská cena |
|---|---|
| r1,112 obyčejných |2μ+14υ |
| r1,NEG/NEGU |2μ+22υ |
| r1,platný FP režim |2μ+21υ |
| r1,neplatný FP režim až k Error |2μ+20υ |
| r1,SET wyde |2μ+12υ |
| r1,INC/OR/ANDN wyde |2μ+14υ |
| r2 |3μ+8υ |

První dva loady a vzatý BOD stojí2μ+5υ. Nonwyde test přidá5υ,
ordinary AND/vzatýBZ4υ. NEG přidá4+5+3υ; FP6+5υ. Wyde test
stojí3υ, SET rozhodnutí4υ; modifying větev3+3υ. U r2 je BOD
nevzatý a navíc SETf,SETop,LDOexc,MOR,JMP. Tyto součty uvádějí
skutečné větve, nikoli měřený hostitelský čas. Virtuální cena
vložené operace zůstává původní Info; r2 je1υ plus vnější5υ.

R0 se vrací do úplně prověřené ordinary instalace. Její helpery
mají své samostatné známé vady a přesné domény; E14 nedokazuje
znovu SAVE/UNSAVE, I/O nebo celý MMIX. R1 odmítá všechny
nepovolené nibbly a marginalX, r2 marginalX, RESUME samotné
odmítá XYZ≠0 a r≥3. Přímé rX<0 se nepokouší o žádný set.

## 6. Jediných27 nových malých případů

`verify_resume_recovery.py` vytvořil nezávislé validní binární
obrazy podle již prokázaného formátu úlohy20: G240,L1,
local0=99, marker1,16globals,12specials a packed header.
Uložené rD7,rE0.5,rM samé1 odlišují implicitní nulový vstup
od náhodného přečtení special registru. Žádný SAVE program ani
starý inverse test se nespouští. Řádky se uloží do text/data
chunků, výsledkem jsou čtyři octabyty X,rA,rR,rH.

17 nových r1 případů pokrývá všechny zvláštní cesty: ADDU579;
NEG997 a signedoverflow; NEGUI−1; SFLOTI zaokrouhlení dolů
na2^24+2; SFLOTUI tie k2^24; FSQRT4→2; tři modifyingwyde
operace a SET bez druhého posunu; oba CS výsledky; nulové
implicitní MUX/DIVU/epsilon a nový rH po MULU. Další4 případy
jsou ordinary r0, negativní rX, r2Q=#40 a r2sOPf9. Šest
odmítnutí je r3, r1load, oba marginalX, r0RESUME a savedround5.
Každý výsledek je uložen samostatně a odvozen výše nebo
přímým malým celočíselným výpočtem. Všechny27 poprvé uspěly,
build+běhy2.273246s, nice15. Žádný úspěšný běh neopakovat.

Unchanged SimHalt vrací při normálním konci hoststatus255;
verifier tuto transportní vlastnost nesmí zaměnit za guest
výsledek. Oracle je přesných32 výstupních bytů; při Error je
status234 a prázdný výstup. Všechny příkazy, stderry, SHA
obrazu/source/object a listing jsou uložené. Neprovádí se
nový test povoleného Q handleru; jeho všechny větve mají výše
algebraický důkaz, nepřisuzujeme jej samotným27 příkladům.

## Výsledek a použití vzorů

E14 může mít argument_recorded: celá definovaná řídicí/operandová
povinnost má vlastní argument a konkrétní opravu obou vad.
Nejde o uzavření každého helperu volaného vloženou instrukcí
ani celého interpretu. U implicitních třetích vstupů je přesně
deklarován přijatý autorův implementační model. Stará širší
poznámka, že tím zůstává V0071 otevřené, byla již nahrazena
rozborem024–033: jeho vytištěný normativní výklad je ověřený.

Vzory1/4B jsou použity konkrétně: úplný vstupní obor a všech144
opcode hodnot místo vzorku; explicitní nula třetího operandu
a všechna metadata/náklady místo pouhé změny BOD; každá
větev Q včetně neobvyklé U výjimky; obecný důkaz oddělený
od27 nových případů. S1–S8, C15 a C23 zůstávají oddělené
podle skutečného původu chyby.
