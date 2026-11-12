# Samostatné argumenty p. 9–15 / file 17–23

Následuje po V0001–V0037. Definice instrukcí jsou odděleny od tvrzení, která z nich plynou. Při kontrole matic byla použita sazba images/file-019-p011.png, ostatní sazba již byla přečtena v prvním průchodu; native text je navigace. Nejde o důkaz plné shody nezávislé implementace s IEEE či MMIXware.

## P. 9

**V0038 — DIVU a LDA.** Podmínka rD<divisor a fallback jsou již obecně zdůvodněny V0036; pro divisor0 není možné0>rD, tedy vždy fallback. DIVU nemá integer-divide check podle definice, zatímco signed DIV ano. Shoda LDA a ADDU je V0026. Tyto dva argumenty se neopakují.

**V0039 — násobit a přičíst.** Pro k∈{2,4,8,16} je kADDU definováno zbytkem (k·u(Y)+u(Z)) modB, B=2^64. Výsledek tedy vždy patří0..B−1. 2ADDU X,Y,Y dává3u(Y) modB, stejné spodní bity jako násobení3; pokud signed přetečení není relevantní, hodnota je požadovaná. Časová výhoda je pouze v modelu tabulky1:1υ proti10υ, nikoli univerzální empirický zákon o hardwaru.

**V0040 — NEG/NEGU.** Y je byte, tedy0..255, a uvedené vzorce Y−s(Z) a (Y−u(Z)) modB jsou konzistentní se signed/unsigned přiřazením. Vynechání Y stanoví Y=0, takže vznikne negace. Jediný případ overflow pro čistou64bitovou signed negaci je s(Z)=−2^63; obecné Y může zvětšit rozsah overflow. Vazba immediate Y na trip operand zůstává otevřená v C0003; tento záznam ji neuzavírá.

**V0041 — SL=SLU v bitovém výsledku.** s(Y)−u(Y) je0 nebo−B. Po násobení2^z je rozdíl stále násobkemB, takže oba výsledky modB shodné. Signed overflow navíc sleduje interval z V0019; unsigned ho nesleduje. Platí i pro z≥64: spodních64 bitů jsou0, je-li z≥64, a signed nenulový výsledek může přetéct.

**V0042 — SR a SRU.** Pro0≤z<64 je unsigned floor dělení posun s nulami a signed floor dělení posun se sign extension (pro záporné y viz y=−B+u a floor(y/2^z)=floor(u/2^z)−2^(64−z)). Pro z≥64 je SRU0, SR je0 pro nezáporné a−1 pro záporné y. Proto se bitové výsledky shodují právě při y≥0 nebo z=0. Shifts a příslušné násobení/dělení mocninou2 mají uvedený matematický vztah; čas1υ proti10υ/60υ je tabulková konvence. SLU nezapisuje rH a SRU nečte rD, takže tato vedlejší chování nejsou zaměňována s MULU/DIVU.

**V0043 — CMP/CMPU.** Trichotomie uspořádaných celých čísel dává pro a<b dvojici indikátorů(0,1), při a=b(0,0), při a>b(1,0); rozdíly jsou−1,0,1. Obě varianty se liší jen interpretací operandů a výsledek se vejde do signed64.

## P. 10

**V0044 — podmínky a ZS.** Osm podmínek tvoří čtyři komplementární dvojice N/NN,Z/NZ,P/NP,OD/EV. Dvoukomplementová hodnota je záporná právě pro horní bit1 (V0012); modulo2 závisí jen na posledním bitu, protože všechny vyšší váhy jsou sudé a rozdíl signed/unsigned je sudéB. CS kopíruje jen při pravdě a jinak zachová X. Násobení vzoruZ indikátorem v ZS dáváZ nebo0, přesně popisované chování pro každou z osmi podmínek; zde není skrytá aritmetická konverze.

**V0045 — bitové tabulky (8).** Pro všechny čtyři dvojice(0,0),(0,1),(1,0),(1,1) je AND součin/minimum s výsledky0,0,0,1; OR maximum0,1,1,1; XOR součet modulo2 s výsledky0,1,1,0. ANDN/ORN pouze předem obrátí druhý bit. NAND/NOR/NXOR obrátí výstup; přiřazení do complement v(X) znamená totéž, protože komplement je involuce. Tím jsou všechny zde uvedené bitové ekvivalence jednotlivě určeny tabulkou čtyř případů.

## P. 11

**V0046 — MUX.** V jedné pozici je výsledek(y&m)|(z&~m). Pro m=1 je y|0=y; pro m=0 je0|z=z. Nezávislost64 pozic dokazuje popis celé operace.

**V0047 — SADD.** Bitový vzor y&~z má1 právě v pozicích y=1,z=0. Popcount ν je tedy přesně počet takových pozic, ležící v0..64, který má signed64 reprezentaci. Zde je ν definice počtu jedniček, nikoli návrh algoritmu počítání.

**V0048 — monus.** Pro dva unsigned n-bit díly y,z je max(0,y−z) v0..y⊆0..2^n−1. Proto BDIF/WDIF/TDIF/ODIF jednotlivé části vždy unese, aniž by si části musely předávat zápůjčku. Jednotky8 bytů/4 wydes/2 tetras jsou V0010. Tvrzení o praktických aplikacích samo o sobě neprokazuje žádný konkrétní algoritmus; úlohy27–30 budou zvlášť.

**V0049 — matice (10).** Řádky jsou binární rozklady bytů9e,37,79,b9,7f,4a,7c,16 z V0003. Čtení jejich sloupců shora dolů dává postupně90,2e,7a,fb,be,cb,cd,78, tj. řádky transponované matice. Každý z osmi výsledných řádků byl porovnán se sazbou (10); souhlasí. Nebyl spuštěn census ani plošný test matic.

**V0050 — zobecněný součin (11).** Pro řádek i a sloupec j mají všechna n dvojčlenná data Ai,k a Bk,j platné indexy. Associativita operace○ dovoluje vynechat závorky při jejich skládání; výsledek má m×s položek. Pro○=+ a•=× je vzorec přímo skalární součin řádku a sloupce, tedy běžné násobení matic. Zde se nepředpokládá nevyřčená komutativita obecných operací. Původní Iversonův text nebyl dohledán.

## P. 12

**V0051 — shoda tří maticových součinů.** Má-li každý řádekA nejvýše jednu1, pro pevné(i,j) může být nenulový nejvýše jeden člen AikBkj. Totéž plyne z nejvýše jedné1 v každém sloupciB. U seznamu nul s nejvýše jednou1 je OR=XOR=obyčejný součet; tvrzení tedy platí pro každou(i,j) a celou matici. Nevyžaduje současně obě podmínky.

**V0052 — transpozice MOR/MXOR.** (A^T⊙B^T)^T_ij je redukce členů A_kj B_ik. Bitové násobení je komutativní, proto jde o členy B_ik A_kj a přesně o(B⊙A)_ij. OR i XOR jsou asociativní a komutativní. To dokazuje obě ekvivalentní definice m(X)=m(Z)⊙m(Y). Podrobná úloha32 se bude řešit vlastním zadáním, tento obecný argument lze převzít.

**V0053 — výběr bytů, (14).** Řádek k matice m(Z) vybírá pro XOR/OR právě ty řádky m(Y), v jejichž pozicích má1. Pro byte posloupnost01,02,04,08,10,20,40,80 leží jediná1 postupně ve sloupcích8,7,…,1, takže X dostane Y v obráceném pořadí bytů. Pro Z=00000000000000ff jsou první sedm řádků nulové a poslední má osm1; pouze poslední byteX je tedy OR/XOR všech osmi bytůY. Oba konkrétní příklady tím mají vlastní odvození.

**V0054 — rozdělení binary64 a binary32.** 1+11+52=64 a1+8+23=32; mantisová pole mají rozsahy0..2^52−1 a0..2^23−1. U binary64 je nejmenší normální exponent1−1023=−1022; krok mantisy na této úrovni je2^(−1022−52)=2^−1074, tedy subnormal formula navazuje správně. Největší subnormal je(1−2^−52)2^−1022, o jeden krok pod nejmenším normal. Rozdělení E=0,0<E<2047,E=2047 a rozděleníF=0/F≠0 se nepřekrývá a pokrývá všechna pole. Analogicky pro binary32 je bias127 a23 fraction bitů. To ověřuje vnitřní číselnou konzistenci zdejšího popisu; úplná shoda všech výjimek s IEEE754/MMIXware zůstává zvláštní závislostí, nikoli uzavřeným testem.

## P. 13

**V0055 — FP porovnání a konverze, omezený rozsah.** Pro konečné uspořádané reálné hodnoty funguje FCMP jako V0043 a FEQL jako indikátor rovnosti; +0 a−0 jsou stejné reálné číslo, přesto různý sign bit. FSQRT/FINT/FIX/FIXU/FLOT/FLOTU/SFLOT/SFLOTU/LDSF/STSF jsou definice operací a zaokrouhlení. FIX s ROUND_UP dává ceil(z), přesně symbol v příkladu. SFLOT nejprve zaokrouhlí na binary32; konečný binary32 je přesně reprezentovatelný v binary64, protože má jen24 významných bitů a menší rozsah exponentu. Proto následná konverze druhou chybu nepřidá. Chování NaN, infinities, signed zero a epsilon relace FCMPE/FEQLE/FUNE nejsou jen těmito argumenty uzavřeny; jde o **partial závislost** na podrobném §4.2/MMIXware, uvedenou v backlogu.

**V0056 — IEEE remainder.** Pro nenulové konečné z a konečné y vyber n nejbližší k y/z, při půlce sudé. Pak |y/z−n|≤1/2, tedy r=y−nz splňuje|r|≤|z|/2. Při rem se zaokrouhluje quotient podle tohoto vlastního pravidla, ne podle případného ROUND_UP. Definice int je naopak obecné aktuální zaokrouhlení na celé číslo. Zvláštní nečíselné případy zůstávají součástí V0055 partial.

## P. 14

**V0057 — immediate varianty.** Nahrazení$Z nezáporným bytemZ dává jednotlivě ADD: s(Y)+Z; NEG s vynechanýmY:−Z; SRU:floor(u(Y)/2^Z); FLOT:float(Z). Všechny0..255 jsou přesně binary64 reprezentovatelné, takže v posledním příkladu není problém se zaokrouhlením. FADD používá jako operand floatingZ, proto do uvedeného pravidla immediate variant nespadá. Číselná dvojice20/21 je v tabulce1 a odpovídá pravidlu even opcode+1; samotné přidělení čísel je definice architektury.

**V0058 — wyde operace.** YZ tvoří unsigned16bit číslo0..65535. Násobky2^48,2^32,2^16,1 umístí jeho bity do čtyř disjunktních bloků po16, aniž by nejvyšší vyšel nad bit63. SET nastaví ostatní bloky na0; INC je modulární součet; OR zapne zadané bity a ANDN vypne zadané bity. U INC může přenos zasáhnout vyšší blok, což definice výslovně zachovává a nepopírá.

**V0059 — konstrukce libovolného octa ve4 instrukcích.** Každé x<B má jediné rozložení a3·2^48+a2·2^32+a1·2^16+a0,0≤ai<2^16. SETH a3 vytvoří první člen a tři INC přidají zbývající členy do dosud nulových disjunktních bloků; součet je x<B, žádný přenos mezi neprázdnými bloky nevzniká. Konkrétní ai=0123,4567,89ab,cdef proto dají0123456789abcdef. Pokud některé bloky jsou0, instrukce lze vynechat; čtyři stačí vždy.

**V0060 — SET register.** Pro každý bit y platí y|0=y, takže OR X,Y,0 skutečně kopíruje64bitový vzor; SET jako zkratka SETL pro konstantu je syntaktická definice.

## P. 15

**V0061 — forward JMP.** Instrukce má4 byty, proto běžný následník je@+4. OffsetXYZ=2 udává2 tetrabyty, tedy8 bytů. OP=f0 a pole000002 tvoříf0000002; z adresy1000 se přejde na1008. Přímá adresa1008 vyžaduje vypočítat(1008−@)/4, takže závisí na výchozím@.

**V0062 — backward JMP a dosah.** Pro offset−2 je24bitové pole2^24−2=fffffe a backwardOP=f1, tedyf1fffffe. Forward offsety jsou0..2^24−1, backward−2^24..−1, takže byte rozsah je−2^26..2^26−4 =−67108864..67108860. Textové „about67 million bytes“ je přesné přiblížení, při instrukčně zarovnaném cíli.

**V0063 — GO return.** A se vyčíslí ze zdrojových operandů starého stavu; pak se doX uloží původní@+4 a provede skokA. Je-li tato návratová adresa později v$X, GO X,X,0 vyčíslí A ze starého$X, tedy skočí na návratovou adresu a uloží doX nový následník. Přepis cílového registru nemůže zpětně změnit už získanou efektivní adresu. Toto je současně nutná operandová konvence použitá knihou.

**V0064 — branch dosah a predikce.** Osm testů je stejných jako V0044, jen mění@ místo registru. Dvoubajtový offset dává tetrabytové rozpětí−2^16..2^16−1, tedy adresy@−2^18..@+2^18−4. Probable varianta mění časovou preferenci, nikoli podmínku ani rozsah. V tabulkovém modelu s pravděpodobností skoku p je E[B]=1+2p a E[PB]=3−2p (vυ), takže PB je lepší právě pro p>1/2, rovné při1/2. Tím je i následující rada na p.16 matematicky odůvodněna v uvedeném modelu.

## Otevřené hranice

P.12–13 mají ověřené uvedené číselné/zaokrouhlovací argumenty, ale úplné IEEE výjimky a epsilon definice zůstávají partial závislostí. Žádný nový nález. Výrok o skutečné rychlosti na všech reálných procesorech se neprokazuje; p.21–23 jej samo omezuje na model a odhad. Další kurzor p.16/file24, s odděleným backlogem V0054–V0055.

### Dodatek obnovy kvality, 6. listopadu 2026

Nový úplný rozbor běžného porovnání, matematických epsilon relací pro
konečné nezáporné epsilon a invariant konkrétního porovnávacího kódu je
v `notes/fp-comparisons-recovery.md`. V0054–V0055 zůstávají partial pro
ostatní přesně vyjmenované operace a specifikační okraje. Samostatný
programový rozpor MMIX-S0001 není knižním nálezem a nepovyšuje celou
p. 12–13 na ověřenou stránku. Podčásti mapuje `fp-verification-items.json`.
