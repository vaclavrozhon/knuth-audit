# MMIX-S0007 — známý relativní cíl přes bit63 se chybně odmítne

**Confirmed, low, doprovodný assembler.** MMIXAL 2013 a 2025 odmítají
platné známé relativní adresy přes hranici #8000000000000000. Tentýž
cíl ve formě future reference přijmou a správně sestaví. Knižní
definice relativní adresy je správná; programový nález nezvyšuje
knižní počet a nemění její barvu na chybnou.

## 1. Jednoznačný kontrakt a přípustný svědek

Fascikl p39/file47 stanoví target=@+4k, −65536≤k<65536 pro BNZ.
Primární MMIXAL:410–420, původní sazba §14 p6, výslovně požaduje
**odečíst current location od cíle a výsledek dělit čtyřmi**. Future
reference má po definici splnit stejné omezení jako známá hodnota.
GETA a PUSHJ používají stejný obor; JMP má −2^24≤k<2^24.
Známé erratum z 13. října 2001 opravuje právě pořadí odčítání v této
normativní větě; v obou zkoumaných verzích je již správný text.

Nejkratší relevantní vstup je:

    Target IS #8000000000000000
     LOC #7ffffffffffffffc
    Main BNZ $1,Target

LABEL Target má před použitím definovaný pure ekvivalent. LOC i target
jsou násobky4, registr1 je platný a rozdíl číselných adres je **4**,
bez přetečení unsigned adres. Správné k=1 dává strojové slovo
#4a010001. Oba originály však ohlásí příliš vzdálený backward target
a skončí s chybou.

Přesuneme-li stejnou `Target IS #8000000000000000` až za Main,
vznikne dovolený future reference. Primární fixup nejprve odečte adresy,
dostane4, posune na1 a vytvoří přesně #4a010001. Odkaz tedy není
neplatný kvůli rozložení programu nebo range pravidlu.

Pro odstranění jakékoli domněnky o zákazech vykonání cílové instrukce
je uložen také stejný případ `GETA $1,Target`, jehož výsledek má být
pouze číslo adresy v registru: správné slovo #f4010001 originál také
odmítne. Důkaz je o sestavení dané instrukce, nezávisí na povolení
pozdějšího fetch přes uživatelskou/kernel hranici. Žádný hardware či
libovolný OS se tu nedokazuje ani nespouští.

## 2. Přesná příčina a celý postižený obor

`shift_right(y,2,0)` v MMIX-ARITH:129–138 je aritmetický posun,
nikoli unsigned. Pro source=#7ffffffffffffffc vrátí 2^61−1, pro
dest=#8000000000000000 vrátí −2^61. Známá YZ větev :2984–3005
i XYZ větev :3080–3101 posunou obě adresy zvlášť a potom odečtou:

    acc = −2^61 − (2^61−1) = −2^62+1.

Tato hodnota je mimo oba malé relativní rozsahy. Přičtení 2^16 nebo
2^24 v backward větvi horní nenulové bity neodstraní, takže nastane
range error. Celé obě relevantní zdrojové větve jsou v archivech
2013/2025 byte-identické; ostatní programy či celé archivy za stejné
neprohlašuji.

Označme H=2^63 a šířku pole w∈{16,24}. Pro source=H−4a,
target=H+4b, a≥1,b≥0,a+b<2^w, je správné k=a+b, zatímco původní
acc=k−2^62. V opačném směru source=H+4a,target=H−4b,
a≥0,b≥1,a+b≤2^w, je správné k=−(a+b), původní acc=k+2^62.
V obou rodinách jsou adresy platné a zarovnané, všechny meze pole
jsou explicitní a originál odmítne každý případ. Rovnosti na obou
povolených mezích se posuzují zvlášť: +2^w je zakázáno, −2^w dovoleno.

Typové bity op_init_table posílají větve, probable branches, GETA
a PUSHJ do stejné YZ cesty, JMP do XYZ cesty. Tím je přenos problému
na tyto skupiny odůvodněn sdílenou skutečnou větví, nikoli analogií
z jediného BNZ testu. U PUSHJ je první pole pure/register povoleno
příslušnou samostatnou kontrolou; změna ho neovlivňuje.

Původní pracovní podezření na wrap #fffffffffffffffc→0 bylo po
přečtení helperu výslovně zamítnuto: signed posuny tam dávají −1 a0,
tedy správné k=1. Tento správný případ je i v uložených kontrolách.
Není započítán jako další chyba.

## 3. Úplný důkaz auditní opravy a všech rozsahových větví

`sources/audit-relative-address-boundary.ch` v obou známých cestách
nahradí samostatné posuny jediným výrazem

    acc=shift_right(ominus(target,cur_loc),2,0);

Je to stejné pořadí jako již používané future fixupy. Nezmění se
test dělitelnosti4, rozlišení 16/24bitového pole, výběr backward
opcode, rozsahové kontroly ani sestavení ostatních polí. Pomocné
lokální proměnné source,dest zůstávají nevyužité; nemají žádný účinek.

Nechť A,T jsou libovolné zarovnané 64bitové adresy. Ominus vytvoří
D=(T−A) mod2^64 přesně pomocí unsigned tetra aritmetiky. Nechť d je
jeho signed interpretace v [−2^63,2^63−1]. Protože A,T jsou násobky4,
d je násobkem4. Arithmetický posun dělením4 proto nevypustí nenulový
zbytek a dá přesně k=d/4 v [−2^61,2^61−1]. Helper užívá pouze
unsigned tetra posuny o2 a30, doplnění sign bitu a spojení disjunktních
bitových částí; nedochází k signed C overflow ani k posunu o šířku slova.

Pro k≥0 má acc sign bit0. Kontrola acc.h==0 a acc.l≤2^w−1 přijme
právě 0≤k<2^w. Pole je k a forward instrukce tedy získá A+4k=T
modulo2^64. Pro k<0 se acc zvýší o2^w a opcode o1. Kontrola přijme
právě 0≤k+2^w<2^w, tedy −2^w≤k<0. Pole je k+2^w a backward
instrukce vrátí A+4((k+2^w)−2^w)=T. Pro k<−2^w zůstává výsledek
po přičtení záporný s nenulovým horním tetra a je odmítnut. Pro
k≥2^w se odmítne horní hodnota nebo její horní tetra. Tím jsou všechny
kladné/záporné a hraniční větve úplné.

Protože 2^w≪2^61, žádný druhý reprezentant téhož modular displacement
nemůže také ležet v dovoleném intervalu. Oprava tedy nepřijme cizí
vzdálenou adresu aliasem. Každý dříve přijatý k je zachován: rozdíl
signed souřadnic, který originál po dělení4 přijal, má absolutní hodnotu
nejvýše2^(w+2), tedy bez signed64 přetečení. Odečtení před posunem
musí dát tentýž k. Všechny změny accepted/rejected se týkají právě
platného modular rozdílu, který originál rozbil oddělením posunů.

Nezarovnaný target nadále narazí na původní diagnostiku před změněnou
částí. Undefined operands nadále jdou do původního fixup seznamu;
register operand nadále projde či selže svou typovou cestou. Patch
nemění parser, symboly, pořadí definic ani obsluhu chybového IS. Obor
důkazu je platný aligned pure relativní operand a existující kapacity
assembleru, nikoli libovolný poškozený zdroj nebo nedostatek hostitelské
paměti. Oprava má konstantní práci, žádné smyčky a nezvyšuje délku
strojové instrukce; žádné architektonické náklady se nemění.

## 4. Originalita zdrojů, známá errata a omezená reprodukce

Originální sazba [MMIXAL §14](https://mmix.cs.hm.edu/doc/mmixal.pdf#page=6)
i obě celé větve §§126/131 na p50/52 byly zobrazeny v
`images/mmixal-upstream-file006.png`, `050.png` a `052.png`.
Knižní file47 byl zobrazen v `images/recovery-language-047.png`.
PDF, metadata, oba skutečné zdroje a přímý zdroj shift_right jsou
výslovnou evidencí. Fyzický MMIXware výtisk nebyl kontrolován.

`results/errata-S0007.json` má deset dosavadních vrstev a jeden
samostatně získaný upstream report IS. Celý assemblerový blok
MMIXware oprav :785–890 byl přečten. Známá oprava IS z roku2013
řeší undefined operand použitý před kontrolou a zavádí test statusu;
v našem zdroji je Target při IS čistý literal a status test správně
projde. Nejde o znovu hlášenou známou chybu. GREG oprava p39,
indexová hesla relative addresses, bitové obrázky znaků a floating
shifty jsou nesouvisející. Odpovídající signed-boundary oprava se
v prohlédnutých vrstvách nenašla; netvrdí se světové prvenství.

Jeden nový `nice -n 15` běh `verify_relative_address_boundary.py`
provedl 13 třířádkových sestavení v každém z originálů2013/2025 a
v samostatné auditní opravě: **39 sestavení, 9 úspěšných build kroků**.
Žádný MMIX program se neprováděl. Každý originál má sedm chybných
odmítnutí; auditní oprava souhlasí ve všech13 případech, včetně
odmítnutí dvou skutečně vzdálených targetů. Kontroly zahrnují forward
i backward, oba w, maximální povolené mezní hodnoty, future fixups,
správný wrap přes0, běžnou backward mez i GETA/PUSHJ/probable branch.

Expected acceptance se vypočte z přesného celočíselného rozdílu adres;
expected instruction z disjunktních bitových polí. U přijatých objektů
malý decoder zpracuje pouze doložené MMO lokace, data, quoting, metadata
a fixr/fixrx, které tento vstup používá. Pro každý loader krok udržuje
aktuální lokaci a XOR součet příspěvků v dané tetra; fixr/fixrx zapisují
jediné původně nulové pole na λ−4δ. Tato invariantní interpretace je
právě primární definice MMO, nikoli volání testované assemblerové funkce.
U dvou future kontrol jsou uloženy i konkrétní δ=1 a δ=−1.

`results/relative-address-boundary.json` obsahuje všechny vstupy,
výsledky, diagnostiky, listing, celé malé MMO objekty v hex a decoded
slova; build log je samostatný. Není třeba cokoli znovu spouštět.
Příklady potvrzují konkrétní implementaci; obecné family a úplný
proof domain opravy jsou odvozeny výše.

Tím je **R0006 uzavřena** jako samostatný programový nález. Všechny
ostatní argumenty celé stránky47 jsou v recovery-pages-046-048.md,
takže tato stránka již nemá zbývající matematickou/implementační mezeru.
