# §1.4.3′–5: dosažitelné maximum 11 skutečných stack položek

7. listopadu2026. Zadání file99/p91, odpověď file125/p117.
Potvrzené C0013 již opravilo konkrétní součet10→11. Zde
se doplňuje přesně stará mezera: horní mez pro všechny
volací cesty a validní vstup, který ji při vstupu do Error
skutečně dosáhne. Žádný nový nález ani test nebyl spuštěn.

Původní doklad C0013 a jeho originály/errata se přebírají.
Znovu sestavené úplné důkazy PUSH/POP a validního UNSAVE
se **neopakují**; použijí se `exercises-1.4.3-001-014.md`,
úlohy10/12, a `independent-arguments-073-082.md`, V0149–V0153.
Právě ty pokrývají G254,L0 a libovolnou platnou bázi image.

## 1. Co se počítá

Otázka se týká **skutečného** MMIX register stacku interpretu
při větvení jeho MemFind na Error. Simulované uživatelské
PUSH jsou pouze hodnoty v jeho virtuálním poli a backing
paměti; do tohoto počtu se nepřičítají. Počítají se dosud
pushed skutečné položky a současné skutečné lokály, právě
jako v tištěném součtu. Stav je okamžik před prvním vstupem
do Error, nikoli libovolná nově napsaná diagnostika po něm.

Základní caller interpretu nemá žádný starší nevyřízený
skutečný rámec. Jeho vstupní0/1 jsou počet/ukazatel argumentů;
po běžných helper calls jsou chráněné opět v kořenovém rámci.
Případná libovolná jiná vnější rutina volající interpret
by přidala svůj vlastní prefix, což není rozhraní tohoto
samostatného programu ani vytištěné odpovědi.

## 2. Úplná horní mez

Přečten celý relevantní call graph tištěného programu i
odpovídajícího primárního `sources/sim-20131017.mms`.
Soubor2025 je byteově totožný, jak dokládá
`sources/sim-source-metadata.json`; to samo neznamená,
že všechny jeho starší chyby jsou opravené. Zde se používají
pouze skutečné instrukce volání. Nejhlubší cesty do MemFind
jsou tyto:

| Cesta před MemFind | Pushed skutečné položky |
|---|---:|
|root→MemFind|3|
|root→StackLoad/StackStore→MemFind|nejvýše3+3|
|root→GetArgs→MemFind|1+3|
|root→StackRoom→StackStore→MemFind|nejvýše3+3+3|

GetReg nevolá MemFind. I/O pomocníci kromě GetArgs volají
MemFind přímo z kořene; GO vazby SimInst/DoInst nepřidávají
PUSH rámec. OutTetra žádné MemFind nevolá. Globální PUSH,
POP,SAVE,UNSAVE větve volají StackRoom/Store/Load přesPUSHJ0,
takže jejich první člen je1, menší než3 z XDest. Žádná
z těchto pomocných rutin rekurzivně nevolá sama sebe.

Každé PUSHJ res má res=$2<G, proto uloží přesně3 položky,
i když byl předtím $2 marginal. Jediné argumentové místo
je$3, které se stane callee0. MemFind před svou Error
větví provede pouze ANDN key=$1,addr=$0,mask; CMPU t;
PBZ t; BN addr. Má tedy přesně2 current locals0/1, žádné
pozdější newlink3/p4 se při tomto vstupu nevytvoří.
Proto nejvýše9 pushed+2 current=**11**. Tištěné2 místo3
u StackRoom je již samostatné C0013, nikoli nová chyba.

## 3. Přípustný počáteční kontext těsně pod zápornými adresami

Označme B=2^63,ρ=256. Simulovaný proces začne s G254,
L0 a prázdným register stackem s O=S=B−128. Oba jeho
globální registry254/255 jsou platné;255 obsahuje běžnou
textovou vstupní adresu Main,254 může být0. Aritmetické
trips jsou vypnuté. Kód leží v platném textu od#100.

Tento stav má přesný validní bootstrap image:

* na B−128 marker0;
* na B−120 uloženýglobal254, na B−112 uloženýglobal255;
* na B−104…B−16 dvanáct specials v předepsaném pořadí;
* na B−8 packed word(254<<56)|A, zde A0.

Jde o16 octa a všechny jejich **adresy** jsou nezáporné
a octabyte-zarovnané, v horní části uživatelského stack
segmentu. Header má jako hodnota horní bit1, což není
neplatná adresa. Přijatý validní UNSAVE argument tento
image obnoví právě na O=S=B−128,L0. Neexistuje zde
malformed header ani předchozí unmatched POP.

Binární vstup řešení úlohy20 tento obraz umí obsahovat:
nenulový kód, global255=Main a packed header lze zapsat
do jeho λ,x…,0 skupin; nulové položky ponechá počáteční
nulová paměť. Poslední načtený octabyte je headerB−8.
Loaderova dočasná loc=B po jeho načtení se závěrečným
SUBU loc,loc,8 vrátí naB−8. Main se čte na loc−104=B−112.
Zde se tedy používá přesně deklarovaný platný vstupní
formát, nikoli libovolný poškozený dumped soubor. Formát
nepřikazuje jedinou pevnou bázi každého uživatelského stacku;
primární MMIX kontrakt výslovně dovoluje vlastní platné
context stacks a jejich inicializaci pomocí UNSAVE.

Zpočátku stačí chunk pro kód, pro tento malý image a
pozdější stackové položky; žádná interní fyzická alokace
se nepřibližuje Pool_Segment. Vzdálené **virtuální** adresy
se promítnou do několika malých uzlů MemFind.

## 4. Konkrétní konečný uživatelský program

Počáteční headerG254 zajišťuje, že254/255 jsou globals.
Použijeme přesně následující tělo:

```text
Main    SET    $254,271
Loop    PUSHJ  $255,AfterPush
AfterPush SUB  $254,$254,1
        PBP    $254,Loop
        SET    $0,0
        TRAP   0,Halt,0
```

SET271 je přímo kódovatelný; čítač klesá271…0 bez
signed overflow. Každý PUSHJ má globální X255 a vstupníL0,
takže vloží právě marker0, zvýší O o8 a zanechá L0.
SUB/PBP používají pouze global254 a L nemění. Neprobíhá
žádné POP. Cíl AfterPush je následující běžná instrukce;
rJ se může přepisovat, ale program jej nepotřebuje.

Pro n vykonaných PUSH platí z přijatého ring invariantu

    O = B−128 + 8n,
    S = B−128 + 8 max(0,n−255),
    L = 0,
    cached = min(n,255) položek.

Indukce: dokud je nová velikost≤255, žádný spill. Při
dalším markeru vznikne přechodová velikost256, StackRoom
odloží právě nejstarší pushed položku a zvýší S o8,
pak se marker rovněž považuje za pushed a L je opět0.
Nejde o opětovné dokazování algoritmu ringu, ale o dosazení
konkrétního jedno-položkového vstupu do jeho již přijaté
transformace. Všechny mezilehlé počty se vejdou do64 bitů;
O může přejít přesB, avšak je uchováno přes unsigned
ADDU/SUBU a není do té chvíle použito jako fyzický host pointer.

Prvních16 spillů čte/zapisuje virtuální adresy
B−128,B−120,…,B−8. Všechny jsou stále nezáporné, proto
MemFind uspěje; následující zvýšení S po posledním z nich
jej nastaví právě naB. Po n271 je tedy

    S=B, O=B+2040, L=0, cached=255.

Následující SET $0,0 má marginal destinaci. XDest vloží
nulovou current položku, nastaví L1 a přes **PUSHJ res**
z řádku218 zavolá StackRoom. Test(ss−oo−ll)&2047 je0,
takže nastane StackStore. Zde γ0,α255; ukládaná položka
je skutečně pushed, nikoli nepřípustný current-local spill.
StackStore zavolá MemFind s A=S=B, jehož signbit je1.

Žádný záporný key ještě v seznamu není: předchozí všechny
adresy byly nezáporné, a MemFind vždy testuje negativitu
před vložením nového key. Cached fast hit tedy není možný.
PBZ se neprovede a BN addr,Error je vzat. Přesně v tomto
okamžiku je skutečná cesta

    XDest PUSHJ2 → StackRoom PUSHJ2 → StackStore PUSHJ2
    → MemFind s L2,

tedy **3+3+3+2=11** skutečných stack položek. Simulovaných
271 markerů se do této sumy nemíchá. Jde o předepsané
odmítnutí uživatelského stacku dosahujícího chráněných
záporných adres; jeho běh do první takové chyby je přípustný.

## 5. Zbytek vytištěné odpovědi

Error v primárním programu nastaví t=−22 a provede Halt,
proto nevrácené rámce neovlivní další uživatelskou instrukci.
Kdyby explicitní politika dovolila pokračovat, jejich
ignorování potřebuje nový kořenový kontext; není tvrzeno,
že původní rJ a všechny lokály jsou beze změny.
Výstupy podle1.4.1′–16 mohou zrušit každý aktivní rámec
jednou; jejich plný důkaz je již v novém subroutine rozboru.
Opakované POP do původní **skutečné** rO=Stack_Segment
funguje, když původní markery zůstávají platné a žádný
POP se neprovede pod tento cíl. Pro jedno pokračování
smí caller obnovit rJ před každým POP na vhodný unwind
pad; samotná kontrola rO neřeší adresu skoku automaticky.

Horní mez i dosažitelnost11 jsou tím uzavřeny. E005 již
není partial pro globální maximum. C0013 nezvyšuje počet
nálezů. Vzor Algorithm R je použit na skutečný call graph
a konečnou dosažitelnou posloupnost, binomický rozbor na
všechny adresní/mezikrokové meze a kografové rozbory na
oddělení chybného součtu od správného programu diagnostiky.
