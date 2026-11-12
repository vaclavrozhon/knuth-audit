# §1.3.1′ — argumenty k úlohám41–58 a přesné mezery

Zadání p.27–28/file35–36, odpovědi p.97–98/file105–106. Úlohy43,48,52,54–57 zůstávají částečné v níže uvedeném rozsahu;58 je výslovně velký výzkumný/projektový úkol. Jejich pouhé přečtení se nepovažuje za řešení.

**41.** (a) Je-li Y odd, CSOD zapíše0 aZSEV také0; je-li even, CSOD zachováX aZSEV kopíruje staréX. Destinační pravidlo pro marginal je v obou případech stejné. (b) Unsigned porovnání s0 dává1 právě proY≠0, jinak0, totéž coZSNZ s1. (c) MOR immediate1 ponechá jen poslední byteY (maska v posledním řádku vybírá poslední řádek), tedy AND sff. (d) MXOR immediate80 ponechá první byteY jako nezáporný nejnižší byte, zatímco SR o56 znaménko rozšíří. Např. Y=8000000000000000 dává128 proti−128. SeSRU je shoda. Všechny čtyři odpovědi doloženy.

**42.** (a) NEG spočítá−x aCSNN jej nahradí původním x právě pro x≥0. Pro x<0 dostaneme−x. Jediná nereprezentovatelná absolutní hodnota je x=−2^63; NEG správně signalizuje signed overflow podle obecné konvence. Známá oprava8.12.2006 NEGU→NEG je v tomto vydání zahrnuta. (b) Floating sign bit je nezávislý na exponentu/fraction, takže jeho vynulování zachová velikost a dá nezáporné číslo (včetně+0 a+∞). U NaN pouze vynuluje sign bit a zachová payload; nepředstírá matematickou absolutní hodnotu reálného čísla. ANDN je přesná bitová implementace.

**43 — algoritmy ověřeny, globální optimalita partial.** Pro nenulové z s k trailing zeros má z−1 spodních k bitů1 a první následující1 změní na0; všechny vyšší bity zachová. (z−1)&~z má proto přesně k jedniček. SUBU aSADD dávají k bez větvení,2υ. Pro leading zeros položme j=floor(log2z). FLOTU v ROUND_OFF zachová exponentj, protože2^j je reprezentovatelné a zaokrouhlení dolů nepřeskočí pod tuto hodnotu ani nad2^(j+1). Exponentové pole je1023+j, poSRU o52 zbývá toto pole a1086−(1023+j)=63−j, správný počet leading zeros. Pro z=0 přídavnéCSZ nastaví64 (původníZ musí zůstat zachován). Tato cesta stojí4+1+1=6υ. DvaMOR obracející bity a dvě instrukce trailing count stojí4υ, tedy jsou o2υ rychlejší. **Není dokázán dolní limit pro všechny možné programy/opcodes a všechny režimy předem načtených konstant**, takže tvrzení „shortest/fastest“ zůstávápartial, ne nová chyba.

**44.** Reprezentuj signed32 a,b jako aQ,bQ v signed64, Q=2^32. ADD/SUB dají(a±b)Q a overflow nastane právě když a±b∉[−2^31,2^31). Pro multiplication SR bQ o32 dá přesněb aMUL(aQ,b)=(ab)Q se stejným správným overflow kritériem; podmínka X≠Y zachová aQ. DIV(aQ,bQ) pro b≠0 dá floor(a/b) a remainderQ(a−b·floor(a/b)); následnýSL o32 převádí quotient na high tetra a signalizuje overflow právě při32bitovém překročení (jediný hraniční případ a=−2^31,b=−1). Při b=0 dáDIV q0,r=aQ a divide check, následnýSL0 nic dalšího nezkazí. LDHT/STHT aSETMH odpovídají stejné škále. Všechny čtyři operace jsou tak ověřeny včetně hranic.

**45.** Jde o osobní mnemotechnickou pomůcku, ne dokazatelné faktické tvrzení. Použitelná vlastní volba je rozdělit DVW|IOUZX na tři události s celočíselným výsledkem a pět floating událostí, a spojit je s pořadím bitů80,40,20|10,08,04,02,01. D=integer divide check,V=integer overflow,W=float-to-fix overflow,I=invalid,O=overflow,U=underflow,Z=division by zero,X=inexact; přiřazení odpovídá p.18.

**46.** ffffffff máOP=ff=TRIP, všechny tři operandové bytyff. TRIP má pevný cíl00 bez ohledu na tato data, proto odpověď „trip to0“ souhlasí. Není to halt/TRAP0.

**47.** ŘádekD máMXOR=de a immediateDF; řádek5 máPBP=54 a backward55. PříponyI/B vyjadřují právě tyto rozdíly. Správná jména jsouMXORI aPBPB.

**48 — kladné páry ověřeny, úplnost znovu otevřena 6. listopadu.** STO/STOU se shodují, protože signed64 se vždy vejde do signed64 paměti a oba zapíší stejné64 bity; stejné platí pro immediate adresové varianty aLDOI/LDOUI. ProNEGI/NEGUI jsou Y iZ byty, rozdílY−Z leží−255..255, takže signed overflow není možný a modular vzory jsou stejné. ObecnéNEG/NEGU se mohou lišit overflow, proto nejsou ekvivalentní. FLOTI/FLOTUI/SFLOTI/SFLOTUI konvertují unsigned byteZ=0..255; signed/unsigned význam je stejný a všechny hodnoty jsou přesné i vbinary32, takže všechna čtyři konečná přiřazení souhlasí, se stejnými povolenými rounding field hodnotami. Tabulkové integer signed/unsigned rodiny mají odstupopcodu2 (ADD/SUB/MUL/DIV/CMP/NEG/SL/SR/load/store a fixed↔float konverze); toto tvrzení se nevykládá jako existence „unsigned FADD“.

**49 — přesná ruční stopa.** Předpoklad odpovědi, že zápisy nepřekryjí spuštěný program, je podstatný. PoNEG je$1=−1; STCO1 na adrese−1+1=0 uloží M8[0]=1; CMPU vrátí1; STB na adrese1+1=2 vloží byte01 a M8[0]=0000010000000001. LDOU na2 zarovná na0 a načte toto octa. INCH přičte2^48, 16ADDU násobí17, takže v=$1=17(257·2^40+1)=0011110000000011.

Potom v² =289·66049·2^80 +289·514·2^40+289. Protože289·66049=0x1234321 a289·514=0x24442, je high=0000012343210000 a low=0244420000000121. PUT rA,1 nastaví1; STW na adrese low+1=0244420000000122 uloží0121, ale low>32767, takže přidáV_BIT40 a rA=41. Enable bity jsou0, tedy se netripne.

Low má8 jedniček; SADD s immediate1 vypustí právě posledníbit, takže vrátí7. FLOT7 je přesné401c000000000000 aPUT je uloží do rB. XOR s1 nejprve udělá odd slovo; PBOD se vrátí naXOR, druhé XOR vrátí even původnífloat aPBOD skončí. NOR dábfe3ffffffffffff, arithmeticSR o1 dádff1ffffffffffff aSRU o1 dá6ff8ffffffffffff. rL se na začátku zvýší na2 právě pokud bylo0 nebo1. To jsou všechny hodnoty uvedené v odpovědi; žádná numerická simulace není pro stopu potřeba.

**50.** Počítáme čtyři paměťové operaceSTCO,STB,LDOU,STW =>4μ. JednoMULU=10υ,jednoFLOT=4υ. XOR aPBOD se provedou dvakrát, PBOD stojí1υ při taken a3υ při not-taken; ostatní uvedené operace1υ. Součet v pořadí stopy je7+10+1+1+1+4+1+2+4+1+1+1=34υ. Výsledek4μ+34υ souhlasí.

**51.** Samostatné zakódování v pořadí programu (OP,X,Y,Z neboYZ) dává:
`35010001 b5010101 33010101 a0010101 8e010101 e4010001 2e010101 1a010101 f7150001 a5010101 db010101 08010001 f6000001 c7010101 5701ffff c4010101 3d010101 3f010101`.
PolePUT používá rA=21=15hex a rB=0; INCH používáwyde0001; PBOD má backward opcode57 a offset−1=ffff. Zbývající běžná pole jsou01 podle zadání. Odpověď je vysázena po sloupcích po třech instrukcích; při správném pořadí se všechny18tetrabytes shodují.

**52 — confirmed C0011, celá klasifikace partial.** Uvedené pozitivní rodiny lze odvodit z identit x±0=x, shifts0, xOR0=x,xXOR0=x,xANDNOT0=x, monus(x,0)=x,x·1=x, OR/AND/MUX(x,x)=x; globální255 odstraní růst rL. CS sZ=X zachová hodnotu při obou větvích, branch/JMP sforward offset1 má běžného následníka. PRELD/PREGO/SWYM jsou architektonické hinty/no-op v konvenci této úlohy. Seznam však vynechává tři doložené případyZSNZ,CSZI,PUTI: plný důkaz a sazba/errata jsou v notes/MMIX-C0011.md. **Úplnost zbývajících negativních případů všech256 opcodů, zejména systémových/IEEE, ještě nebyla dokázána.** Nepředstírá se, že nalezené vynechané položky už tvoří jedinou možnou opravu.

**53.** Přímý zápis do rH způsobujeMULU/MULUI (high half), PUT/PUTI sX=rH aUNSAVE obnovením uložené hodnoty. GET pouze čte, ostatní zde definované instrukce tento speciální registr jako cíl nemají. To potvrzuje uvedený seznam přímých účinků. Následně vykonané instrukce handleru či vložená instrukce poRESUME se účtují vlastnímopcodem, nikoli libovolné předcházející větvi; bez této konvence by žádný podobný seznam nebyl lokální.

**54 — úplná matematická klasifikace, výklad výpustky partial.** Nový samostatný důkaz `exercises-1.3.1-054-055-recovery.md` pokrývá všech256opcodů a dává38 možných přímých změn rA. Každá kladná rodina má přípustného svědka, každá záporná úplný argument. Čtyři immediate float konverze jsou vždy přesné; širší IEEE závislosti a epsilon okraje nebrání této existenční klasifikaci. Zbývá jen výklad vytištěného „FSUB, …, FCMPE“: souvislý interval by tyto čtyři opcodes nesprávně zahrnul, implicitně vybrané register formy nikoli. Bez nového confirmed nálezu.

**55 — úplná klasifikace obou režimů, rozsah otázky partial.** Stejná nová poznámka dokazuje181opcodů s možnou změnou rL v uživatelském režimu a183 při povoleném privilegovaném LDVTS/LDVTSI. Všechny obyčejné cíle, přímé změny rámce a negativní rodiny jsou pokryty. PUT rG sám L nemění, protože platné G musí být alespoň L. Zbývá přesná interpretace otázky „all MMIX opcodes“ vůči OS-only instrukcím, nikoli neprovedený důkaz hypotetického hardware.

**56 — tři konstrukce ověřeny, minima partial.** Krátký nice15 výpočet dvou krajů je v results/ex56-endpoint-bounds.json:28^13=6502111422497947648≤2^63 a29^13=10260628712958602189>2^63, tedy|x|≤28. Dále28^8<2^39 a28^5<2^25. Šestiinstrukční smyčka začíná hodnotoux a12krát násobíx, takže vrátíx^13; žádný menší mezivýsledek absolutní hodnotou nepřesáhne dovoleno.12MUL,12SUB,11takenPBP a1not-takenPBP plus inicializace dávají120+12+14+3=149υ a1μ;6tetras=24bytů.

V rychlejší12instrukční variantě vznikne a=2^39x+x^4,b=2^25x^4. Unsigned interpretacea je a+B[x<0], takže součin s b má low=2^25x^8 a high=x^5+2^25x^4[x<0]; low se vejde, protože x^8<2^39. High má tedy správných spodních25bitůx^5. MUX s1ffffff vezme tyto bity a horní bity původníhox; jelikož|x^5|<2^25 a má stejné znaménko jako x, vznikne přesněx^5. SRU low o25 dáváx^8 a posledníMULx^13. Všechny prepacking signed výrazy se při|x|≤28 vejdou.4multiplications za40υ, sedm ostatních lokálníchoperací aLDO zaμ+υ dávajíμ+48υ,48bytů.

Pět násobení je nutných pouze v addition-chain modelu: po nejvýše třech násobeních jsou dosažitelnénejvyšší exponenty6 nebo8; exponent7 po třech nelze (řetězce začnou1,2,3 nebo1,2,4). S6 dalším součtem nepřesáhneme12; s8 jsou předchozí exponenty1,2,4,8 a žádné dvě hodnoty nedají13. Řetězec1,2,3,6,12,13 ukazuje dosažitelnost pěti. Packing program tento omezený model obchází.

Tabulka má57hodnot pro−28..28.8ADDU vytvoříTable+8x a následnéLDOs224 vybere položku x+28. Prostor3·4+57·8=468bytů, čas2μ+3υ; je lepší než packing právě kdyžμ<45υ a rovna přiμ=45υ. **Globální minima počtu instrukcí, prostoru či času přes všechny možné MMIX programy a hodnotyμ nejsou dokázána**, proto úloha zůstávápartial; nejde o potvrzení univerzální optimality jen porovnáním tří příkladů.

**57 — partial kvalitativní tvrzení.** Neměnný kód dovoluje sdílet read-only stránky a instrukční cache; po modifikaci může být nutná synchronizace/invalidace a odstranění již dekódovaných instrukcí z pipeline. Měnící se instrukce komplikují profilování stabilních adres/opcodů. To vysvětluje obvyklou nevýhodu. Striktní formulaci odpovědi „cannot be used by more than one process at once“ bez určení režimu sdílení/synchronizace zde **nepovažuji za dokázanou nemožnost**; vyžaduje kontext. Žádný nový nález z této formulace neoznačuji. Historické/empirické hardwarové náklady nejsou změřeny.

**58 — open research/project.** Zadání požaduje knihu a kompletníNNIXkernel, rating50. Nebyla vytvořena ani nezávisle ověřena realizace; úloha zůstává otevřená. Podle AGENTS se nemá řešit výzkumný projekt za každou cenu.

## Stav

Z58úloh oddílu má49 samostatný argument pro požadovaný rozsah;33,43,48,52,54,55,56,57 jsoupartial a58open research/project. Vedlejší neověřené census/bibliografie jsou nadále oddělené. Nový doložený nálezC0011 vznikl v52. Další průběžný kurzor je §1.3.2′ ProgramM, p.28/file36; staršípartial závislosti se neztrácejí a čekají v backlogu.


Dodatek k48: původní argument neprokazoval vyloučení všech ostatních
dvojic opcodů v témže rozsahu stavu, cache účinků a času. Tato úplnost
je nyní výslovně partial; kladné páry a jejich důkazy zůstávají.
Dodatek k56: `recovery-pages-034-036.md` uvádí přesný pětitetrabytový
program při spotřebovatelném preloaded global12; preservation
konvence a globální minimum zůstávají otevřené. Žádný nový běh.
