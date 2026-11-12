# §1.3.1′–54 a 55: úplná klasifikace přímých účinků

6. listopadu 2026. Zadání file36/p28, odpovědi file106/p98; původní
strana odpovědí je zobrazena v `images/file-106-p098.png`.
Následující klasifikace má vlastní důkaz všech pozitivních i negativních
rodin. Staré neadresné „IEEE/system dependency“ se tím nahrazuje přesnou
hranicí výkladu dvou vytištěných seznamů. Žádný nový confirmed nález.

## Společný rozsah

Počítá se přímý účinek **platné instrukce** v přípustném stavu
0≤L≤G≤255, G≥32, s povolenými relevantními paměťovými přístupy.
Činnost později spuštěného OS/handleru a instrukce vložené pomocí RESUME
se účtuje jejím vlastním opcodem. Jinak by mohl každý opcode nepřímo
změnit libovolný registr a klasifikace otázek 53–55 by neměla zamýšlený
význam. Neodvozuje se správnost uživatelského handleru ani cache hardware.

Každý kladný řádek znamená existenci přípustného stavu měnícího daný
registr; záporný znamená jeho zachování ve všech takových stavech.
Pro rA lze u svědků nastavit původní eventy i enables na nulu, takže
vyvolání doloženého eventu skutečně změní hodnotu registru.

## 54: přesně 38 opcodů může přímo změnit rA

Rounding mode i enables mění pouze přímý zápis/obnova rA; arithmetic
eventy se ORují při příslušném výjimečném výsledku. Úplný kladný seznam
v numerickém pořadí, **bez výpustek**, je:

    01 FCMP
    04 FADD     05 FIX      06 FSUB      07 FIXU
    08 FLOT     0a FLOTU    0c SFLOT     0e SFLOTU
    10 FMUL     11 FCMPE    13 FEQLE     14 FDIV
    15 FSQRT    16 FREM     17 FINT
    18 MUL      19 MULI     1c DIV       1d DIVI
    20 ADD      21 ADDI     24 SUB       25 SUBI
    34 NEG      38 SL       39 SLI
    a0 STB      a1 STBI     a4 STW       a5 STWI
    a8 STT      a9 STTI     b0 STSF      b1 STSFI
    f6 PUT      f7 PUTI     fb UNSAVE

Existenci pro každý člen dokládají následující disjunktní skupiny:

* FCMP s NaN vyvolá I. FCMPE a FEQLE s konečným epsilon −1 vyvolají I;
  zde není třeba rozhodnout nejasnou −0 či +∞ doménu.
* FADD(+∞,−∞), FSUB(+∞,+∞), FMUL(0,+∞), FREM(1,0) a FSQRT(−1)
  vyvolají I. FDIV(1,0) vyvolá Z. FIX/FIXU infinity a FINT signaling
  NaN vyvolají I. Tyto konkrétní svědky neovlivňuje žádná z otevřených
  širších IEEE povinností ani chybějící X v původním FINT.
* FLOT/FLOTU čísla 2^53+1 a SFLOT/SFLOTU čísla 2^24+1 při nearest
  vyvolají X. Obě přesné poloviny i representability jsou pokryty
  celým důkazem `fp-conversions-recovery.md` §4.
* MUL/MULI s max_signed64 a 2 vyvolají V. DIV/DIVI s nulovým dělitelem
  vyvolají D. ADD/ADDI s max_signed64 a 1, SUB/SUBI s min_signed64 a 1,
  NEG s Y=0 a Z=min_signed64, SL/SLI s Y=1 a posunem 63 vyvolají V.
  U NEG je Y immediate byte, zatímco Z je registr; je tedy přípustné
  přesně uvedené znaménkové minimum.
* STB/STBI s hodnotou 128, STW/STWI s 32768 a STT/STTI s 2^31 do
  povolené paměti vyvolají V. STSF/STSFI signaling NaN vyvolají I.
  Adresová immediate varianta nemění doménu ukládané hodnoty.
* PUT/PUTI s rA a hodnotou 1 změní původní nulu. UNSAVE může obnovit
  platný uložený obraz s jiným rA, podle již přijatého SAVE/UNSAVE
  kontraktu; nevyžaduje se nový důkaz starého algoritmu.

Pro zbývající opcodes je vyloučení úplné po těchto rodinách:

* FUN/FEQL/FUNE nikdy nevytvářejí arithmetic event, ani pro sNaN.
  To je výslovné MMIX pravidlo, již dokázané vlastním dispatcherem.
* **09 FLOTI, 0b FLOTUI, 0d SFLOTI, 0f SFLOTUI:** operand Z je byte
  0..255, tedy nezáporný integer s nejvýše osmi významnými bity.
  Je přesně representovatelný v obou cílových formátech, pro každý
  platný Y i režim rA. Není NaN, nemůže přetéct/podtéct a není inexact.
  Proto všechny čtyři rA zachovávají. Neplatný rounding field je
  neplatná instrukce, nikoli další aritmetický převod této domény.
* NEGI má oba operandy byty, rozdíl leží −255..255 a V je nemožné.
  Ostatní unsigned integer varianty výjimky z definice nesignalizují;
  porovnání CMP/CMPU a pravé posuny nemohou integer přetéct.
* Conditional, branch, bitové, Boolean-matrix, byte-difference,
  konstantové a adresové instrukce mají jen uvedené datové/PC účinky,
  bez událostí rA. Ani jejich výpočet adresy nepoužívá signed ADD s V.
* Loads včetně LDSF nemají arithmetic event; sNaN se při LDSF jen
  přesně přenese. Unsigned stores, úplné octa stores, STHT, STCO,
  CSWAP a cache/translation instrukce nemají příznak rA.
* Zbývající call/return/system instrukce neukládají rA a negenerují
  žádnou z osmi arithmetic výjimek. SAVE rA čte do obrazu; GET jej jen
  čte; TRIP/TRAP přenášejí řízení a příslušné kontextové registry.
  Přímé výjimky jejich pozdějších handlerů jsou mimo vymezenou klasifikaci.

Takto jsou pokryty všechna pole i mezní hodnoty každé rodiny; nejde
o odhad z tabulkového jména. Propojení s primárním zdrojem je
`mmix-sim-20250620.w:1910–2240,2273–2346,2586–2592` a příslušné
vlastní FP důkazy. Normativní architektura platí i tam, kde jednoduchý
simulátor výslovně neemuluje OS.

**Zbývající výklad odpovědi 54:** tisk obsahuje „FSUB, …, FCMPE“.
Jestliže jde o souvislý interval opcode #06..#11, obsahuje navíc čtyři
immediate konverze výše. Jestliže výpustka implicitně vybírá pouze
register formy, matematický seznam může být míněn správně. Proto zde
není potvrzený nález založený pouze na nevyjmenovaných členech výpustky.
Úloha již nemá otevřenou implementační klasifikaci; partial zůstává
pouze přesné čtení vytištěného seznamu. Všech osm veřejných vrstev
prošlo cíleným vyhledáním FLOTI/SFLOTI/answer54/p98; žádná nalezená
oprava tento výklad neupřesňuje.

## 55: obecný cíl, explicitní změna rámce a privilegovaná hranice

Při obyčejném zápisu do cíle X je rL změněno právě při L≤X<G:
nová hodnota je X+1. Staré marginal registry se přečtou jako nula a
nově dostupné registry se inicializují; to platí také pro conditional
set s nesplněnou podmínkou. Vlastní pravidlo alokace je již dokázáno
v register-stack bloku a primární dispatch jej provádí před výsledným
zápisem. Pro každou níže uvedenou normální rodinu zvolme L=0,G=32,X=0,
platné ostatní operandy a povolené adresy. Výsledek může být i nula,
ale rL se změní na 1. Úplné rozsahy obyčejných destination opcodů jsou:

    01..3f  FCMP až SRUI                 63 opcodů
    60..97  CSN až LDUNCI                56 opcodů
    9e..9f  GO, GOI                       2 opcodes
    c0..ef  OR až ANDNL                  48 opcodů
    f4..f5  GETA, GETAB                    2 opcodes
    fe      GET                           1 opcode

Čtyři PUSH varianty (#be,#bf,#f2,#f3) mají rámcový účinek: například
L=1,X=0 dá po push L=0. PUT/PUTI (#f6,#f7) mohou zkrátit L přímým
PUT rL,0 ze stavu L=1. PUT rG sám L nemění, protože platné nové G
musí být alespoň L; předchozí poznámka o rG byla zbytečně široká.
SAVE (#fa) z L=1 nastaví 0. UNSAVE (#fb) může obnovit legitimní obraz
s jiným počtem lokálních registrů. POP (#f8) může například ze stavu
L=0 po předchozím push s uloženou dírou k=1 obnovit L=1. Tyto případy
jsou konstrukce přípustných rámců, nikoli náhodné hodnoty v paměti.

Dohromady jde o **181 opcodů v uživatelském režimu**. Každý zbytek
tabulky nemá obecný destination ani jednu z právě vyjmenovaných změn
rámce: jsou to branches, stores/cache hints, JMP, RESUME, SYNC, SWYM,
TRAP/TRIP a dvě OS instrukce vyčleněné níže. Čtení lokálního nebo
marginal zdroje samo rL nezvětšuje. Tím je negativní část úplná.

**Privilegované LDVTS/LDVTSI (#98,#99)** mají podle výslovné primární
definice MMIX-doc:2988–3002 výstup do obecného X (hodnota 0..3).
Při povoleném OS provedení s L=0,G=32,X=0 tedy rovněž nastaví L=1,
například když zvolený key není v translation cache a výstupem je 0.
Normativní definice nijak neomezuje X na global register. Toto je
aplikace stejného obecného allocation pravidla, nikoli předpoklad
o realizaci cache v hypotetickém hardware. Při zahrnutí privilegovaného
režimu je tedy počet **183**.

Vytištěný seznam 55 se přesně rovná 181 uživatelským opcodům: rozsah
CSN..LDUNCI končí před LDVTS/LDVTSI. Text hlavního výkladu tyto dvě
instrukce odkládá jako OS-only; samotná otázka však říká všechny MMIX
opcodes. Zůstává přesná otázka rozsahu tohoto kvantifikátoru. Netvrdím
chybu na základě nerozhodnutého uživatelského versus privilegovaného
oboru. Výsledky pro **oba** obory jsou nyní úplně prokázány.

`results/opcode-effects-054-055.json` uvádí všech 256 jmen/čísel,
kladnou či zápornou klasifikaci a odkazy na tyto důkazové skupiny.
Jména jsou převzata z již jednou úplně reconciled tabulek; jejich
opakované sestavení není numerická simulace ani nový brute force.
Žádné náklady instrukcí se tím nemění.
