# Úloha1.3.2′–17: úplný maskový test a přesná hranice platnosti

Zadání46/file54, odpověď101–102/file109–110. Celá masková metoda
je níže dokázána pro všech256 opcodes a všechna pole XYZ. Úloha
nadále zůstává **partial pro silnější stavový výklad platnosti**;
vytištěná odpověď sama přiznává dvě výjimky. Žádná z nich zde
není hlášena jako nový neznámý nález.

## Přesný obor a invariant vstupu

Vstupní callee$0=A je64bitový pattern. Pro A<0 se BN vrátí
hned a ponechá nenulové A, tedy správné odmítnutí adresy bez
pokusu o čtení. Pro A≥0 předpokládáme dostupné M4[A], platnou
tabulku256 tetrabytes na4 zarovnané bázi B a platný subroutine
stack. Zdroj se neprovádí; pouze se čte jako data. Tabulka a
kód se nemění, global table jeB, lokály0..2 jsou dostupné a
nemění význam global base. Přístupová chyba v samotném čtení
je mimo specifikaci subroutine testu; není vydávána za vrácený
negativní výsledek.

LDTU dá u=OP·2^24+X·2^16+Y·2^8+Z,0≤u<2^32, v tetra=$1.
SR$0,tetra,22 dává4OP+floor(X/64). Poslední člen je0..3;
následné LDT zaokrouhlí efektivní adresu dolů na násobek4,
a protožeB je aligned, čte přesně masku B+4OP. Ani největší
OP255 nepřekročí1024bytovou tabulku; poslední čtení je offset1020.
Vysoké32 bity masky vzniknou sign extension LDT.

Invariant dále: tetra je původní unsigned instrukce, maxXYZ je
sign-extended maska jejího opcode, $0 je bytewise saturated
difference BDIF(u,mask). Vysoké čtyři byty u jsou0; vůči
maskovému0 či255 tedy dávají0. Ve spodních bytech je rozdíl0
právě tehdy, když příslušný byte u nepřekračuje jeho maskové
maximum. Žádný carry nemůže přetéct do sousedního byte.

## Všech256 buněk a primární smlouva každé třídy

| Třída | Opcode čísla | Přesná statická omezení |
|---|---|---|
| b=ffff04ff | 05,07,08–0f,15,17 | Y≤4; X,Z libovolné |
| c=001f00ff | f6,f7 | Y=0, X≤31; zvláštní PUT test níže |
| d=ff000000 | f9 | X=Y=Z=0 pro unprivileged RESUME |
| e=ffff0000 | fa | Y=Z=0; global podmínka X zde chybí |
| f=ff0000ff | fb | X=Y=0, Z libovolné |
| g=ff000003 | fc | X=Y=0, Z≤3 |
| h=ffff001f | fe | Y=0, Z≤31, X libovolné |
| 0 | 98,99 | LDVTS/LDVTSI jsou vždy privileged |
| a=ffffffff | ostatních235 | žádné další pevné omezení operandových bytů |

Primární MMIX-doc:1582–1615 jmenuje přesně FIX/FIXU, všech osm
FLOT/SFLOT signed/unsigned/immediate variant aFSQRT/FINT jako
unary FP příkazy s Y≤4. Žádná binární FP operace takové pole
nemá: jejíY je registr, nikoli rounding code. Tím je každá
z12 buněk b i vyloučení ostatních FP buněk odůvodněno.

Doc:2678–2716 určuje GETY0/Z<32 a PUTY0/X<32, readonly
9..11 a privileged8,12..18. Po jejich vyloučení zůstává
X0..7 nebo19..31. Doc:2346–2390 povoluje uživatelský RESUME0,
vyžaduje X=Y0, RESUME1 patří negativnímu OS aZ>1 je reserved.
Doc:2718–2743 určuje SAVEYZ0, UNSAVEXY0 a navíc skutečnou
global podmínku SAVE. Doc:1932–1977 rozlišuje SYNCXYZ0..3
unprivileged,4..7 privileged a>7 illegal; to je právě X=Y0,
Z≤3. Doc:2984–3000 výslovně omezuje oba LDVTS na OS.

Zbývající a buňky tvoří:00–04,06,10–14,16,18–97,9a–f5,
f8,fd,ff. Celé dříve zkontrolované definice těchto skupin mají
libovolné register/byte operands: integer arithmetic, conditional
branches a sets, loads/stores a cache hints, bit/byte operations,
constant building, jumps a běžný linkage. POP má definované
chování i pro X větší než počet lokálů; nejde o zakázaný byte.
SWYM ignoruje XYZ aTRAP/TRIP předávají XYZ handleru. Omezení
zjednodušeného simulátoru na jeho deset I/O trapů se nepřevádí
na omezení architektonického TRAP. Effective-address privilege,
data values a případná arithmetic exception nejsou další pevné
horní masky bytů těchto opcodes.

`results/instruction17-table-reconciliation.json` porovnává každou
ze256 skutečně vytištěných buněk s tímto samostatně odůvodněným
rozdělením:21 zvláštních,235 generických, všechny souhlasí.
Jediný nový malý nice15 krok načetl16 printed řádků a zkontroloval
256 jmen; žádná MMIX instrukce se nespustila a žádný4^16 či2^32
operandový prostor se neenumeroval. Obecný XYZ důkaz je bytewise
argument výše, nikoli tato kontrola pouhých256 hodnot.

## Všechny řídicí větve a PUT dovětek

Masky a,b,d,e,f,g,h jsou záporné po LDT; nula proLDVTS je
nekladná. PBNP maxXYZ,9F proto ukončí všechny tyto případy.
Pro nezápornou instrukční adresu je u každé neprivileged
maskové třídy návrat0 právě když všechna její uvedená omezení
XYZ platí. Opcode byte má maximumff a sám nemůže výsledek
zkazit. U LDVTS má maska0 a opcode98/99 je nenulový, takže
BDIF zaručeně vrátí nenulu pro všech2^24 trojic XYZ.

Jediná kladná maska jePUTc, takže PBNP pokračuje právě proPUT/PUTI.
BDIF má v opcode byte samotnéf6/f7, ale ANDNML$0,#ff00
vynuluje právě tento byte v dolním32bitovém slově; ostatní
XYZ rozdíly zachová. BNZ odmítne právě X>31 neboY≠0.
Z je v masceff, tedy se neomezuje. Pokud BNZ neodejde, máme
0≤X≤31,Y=0 a $0=0.

MOR tetra,tetra,#4 izoluje X do dolního byte: jediná jednička
v low řádku matice vybere byte číslo2 původního tetra, ostatní
výstupní řádky jsou0. CMP$0,tetra,18 dává kladný výsledek právě
pro X19..31; CSP potom nahradí tetra nulou právě v těchto
případech. Pro X0..18 zachová X. ODIF$0,tetra,7 je unsigned
octa saturated subtraction: vrátí0 pro původní X0..7 i19..31,
a X−7∈1..11 pro X8..18. Proto všechny čtyři části PUT oboru
včetně X7/8/18/19/31/32 mají přesný a úplný výsledek.

POP1 vrátí jediný výsledek pomocí dříve uzavřeného call interface;
žádné vnitřní volání nemění rJ. Každá cesta skončí po konečně
mnoha vypsaných instrukcích; zde nejsou smyčky. Žádná hodnota
masky, pole či výsledku nepřeteče aritmetický důkazový obor.

## Deklarované náklady tohoto kódu

Negativní vstup: takenBN3υ aPOP3υ, celkem6υ bez paměti.
Každý nezáporný vstup má přesně dvě loads, tedy2μ. Obvyklá
non-PUT cesta má BN,LDTU,SR,LDT,BDIF po1υ, správně předpovězený
PBNP1υ aPOP3υ, celkem2μ+9υ. PUT má PBNP not-taken, tedy3υ;
je-li X/Y maska vadná, ANDNML1, takenBNZ3 aPOP3 dávají
2μ+15υ. Jinak BNZ stojí1 a následují MOR,CMP,CSP,ODIF po1,
POP3:2μ+17υ. To pokrývá i pozdější odmítnutí X8..18.
Tabulka má1024 bytů, práce O(1), bez run-time zápisů do paměti.

To je konkrétní důkaz efektivity poskytnutého řešení. Zadání
„try as efficient as possible“ a doporučení tabulkového dispatch
neposkytují pevně zadaný univerzální model všech alternativ;
globální instrukční minimum se zde netvrdí ani nenahrazuje
příkladem. Pro doporučený octabyte dispatch v zadání analogicky
SR instruction,21 dává8OP+floor(X/32); LDO vyrovná adresu na8
a vybere přesně OP-tou octa, je-li báze8-aligned.

## Přesně co tím není uzavřeno

Na začátku file110 odpověď výslovně říká, že se neodmítá jump
do negativní adresy ani SAVE$0,0, přestože$0 nemůže být global.
To odpovídá skutečnému kódu: e nemá spodní mez naX. Ani pro
X≥32 nerozhodne, zda X≥aktuálnírG. Pevné masky tedy neimplikují
úplnou stavovou legalitu vykonání instrukce.

Stejně přesně jsou odděleny hodnotové PUT podmínky. Například
PUTI rG,0, wordf7130000, má Y0,X19,Z0 a tabulka jej přijme:
po c/ANDNML/BNZ je nula, X19 se přesCSP změní na0 aODIF dá0.
Přitom MMIX-SIM:2220–2225 výslovně odmítá z<32 při PUT rG,
v souladu s primárním G≥32. PUT rA zase může mít zakázané
vysoké bity hodnoty aRESUME0 může mít nepřípustný stav rX/ropcode.
To jsou konkrétní důvody, proč „statický byte obal“ nelze bez
dalších podmínek přejmenovat na úplný test legality.

Není zde novýconfirmed nález z těchto případů: odpověď již své
omezení explicitně deklaruje a původní význam otázky může být
právě kontrola tohoto syntaktického obalu. Chybí definitivní
rozlišení, zda „all restrictions“ v zadání požaduje i hodnotové
a stavové předpoklady, a případná úplná rutina pro takto širokou
smlouvu. **E0132-017 proto zůstávápartial**, nyní však s úplným
důkazem celého skutečně vytištěného kódu a všech256 buněk.
Neřeší se znovu SAVE/UNSAVE/RESUME implementace; jejich přijaté
primární podmínky se pouze přesně používají k vymezení této úlohy.
