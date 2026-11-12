# Celý rozsah file52–53 a odpovědí107–109

Tento blok mapuje každé zadání4–16, konec úlohy15, celý úvod druhé
sady, všechny odpovědi1–16 a začátek odpovědi17 včetně celé její
tabulky. Nově zobrazeny originály52/53/107/108/109. Odpověď17
pokračuje na110; její dosavadní přesná omezení zůstávají partial,
nikoli předstírané dokončení celé validační úlohy.

## File52/p44 a odpovědi4–10 na107/p99

**4.** Hex číslo má18 cifer; ekvivalenty se redukují modulo2^64,
takže horní11 je násobek2^64 a výsledkem je2233445566778899.
Převzatý argument úlohy4 pokrývá přesně vytištěné číslo i odpovědní
pravidlo redukce, nejen počet cifer.

**5.** Rozvinutí stringu je tokenový seznam3+'p','i','l','l','s'+6.
První konstanta112+3=115 je's', poslední115+6=121 je'y'; střední
tři znaky se nemění. BYTE tedy vytvoří přesně „silly“. Žádná
aritmetika nad řetězcovým objektem se neprovádí. Odpovědní stylistické
nedoporučení triku není tvrzení o jeho neplatnosti.

**6.** Pro current location100hex je `TETRA @,@` v jedné operandové
sadě00000100,00000100. Dvě instrukce `TETRA @; TETRA @` mají
00000100,00000104, protože druhý EXPR vzniká po zvýšení location.
V obou případech začínáme zarovnaně a končíme na108, takže se
liší právě druhý obsah paměti, nikoli vedlejší neplatný stav.
Jeden takový přípustný protipříklad plně vyvrací otázku „always“.

**7.** GETA kóduje tetrabyte target, nikoli byte rozdíl. Při
zarovnané lokaci A mají A i A+1 po odstranění nízkých dvou bitů
tentýž cílA a displacement0. Výsledkem je stejná adresaA.
Primární assembler u nezarovnaného targetu dává označené warning,
potom skutečně sestaví posunutý target; primární architektura
nezná samostatné dva nízké offset bity. Není to důkaz pro
libovolné náhradní assemblerové politiky warnings.

**8.** Piš p=16q+r,0≤r<16. Výraz(p+15)&−16 má hodnotu p při
r=0 a16(q+1) jinak; přidaný byte počet je0 nebo16−r∈1..15.
Výsledek se jako každá adresa bere modulo2^64. Na horním okraji
se může stát0; běžná nerovnost nový p≥starý p vyžaduje, že
následující aligned adresa nepřekročí prostor. Obě alternativy
odpovědi `-@/16*-16` a `-(-@>>4<<4)` mají stejnou modular
hodnotu: pro p>0 nejprve−p=M−p, jeho unsigned dělení16 je
2^60−q pro r=0, jinak2^60−q−1; následné−16 nebo opačný posun
vrátí uvedené zarovnání. p=0 se spočte zvlášť jako0. Jde o
assemblerový výraz, bez tvrzení runtime či globální optimality.

**9.** Celé parametrické řešení L=600, kapacity, obě tiskové meze
i dodatečné přesné údaje1230/6542 jsou nyní úplně v
`exercises-1.3.2-009-014-recovery.md`, části9. Původní uzavřené
invarianty se přebírají jen v prokázaném konečném oboru; exact
census má nový malý certifikát bez opakování starého intervalu.

**10.** Převzatý ruční argument v exercises-1.3.2-001-016.md byl
znovu porovnán s celou původní sazbou107. Pokrývá všech46
nenulových tetrabytes100..158 a15c..1b4:15 prvních instrukcí,
8 tetrabytes stringů/padding a23 dalších nenulových instrukcí.
Halt na1b8 je nula a správně není ve výčtu nonzero data. Jediné
nenulové počáteční datum v data segmentu je M2[D]=0002; ostatní
loaderem nulovaná paměť není opomenuté nonzero datum.

Každý OP/X/Y/Z je v převzatém argumentu rozepsán; relativní
offsety13,−5,−10,−7,−5,−12,−19 mají konkrétní source/target
adresy. Například BZ na110 k15c má19 tetrabytes=13hex,
PBNZ na1b4 k168 má−19. Stringy mají25 znaků title,LF,NUL,
tři spaces,NUL a jediný padding byte: dohromady32 bytů na13c..15b.
Tím je current location před2H přesně15c. První SET n,3 jeSETL,
SETjj,j0 jeORI0, jak říká závěrečná poznámka odpovědi.

Předdefinované GREGy v pořadí dávají n254,q253,r252,jj251,kk250,
pk249,ptop248,j0247,TitleBase246,Pattern245 a rG245=f5. Čtyři
vypsané nenulové inicializace jsou přesně D+1000,−998,13c a
2030303030000000; ostatní uvedenéGREGy začínají0. Tím jsou
kontrolovány i všechny závěrečné registry, ne jen strojové instrukce.
Žádný assembler nebyl při úloze požadující ruční sestavení použit.

## File52/p44 a odpovědi11–14 na108–109

**11(a),(b) a celá odpověď.** Samostatný argument nejmenšího
dělitele, test n<p²+p<(p+1)², přesná ostrá mez pro další prime,
dostupnost všech tabulkových čtení i celý převzatý obecný Bertrand
jsou v exercises-1.3.2-009-014-recovery.md, části11. Všechny jeho
předpoklady jsou stejné; pouhý konečný certifikát500 primes by
obecnou odpovědní větu nenahrazoval.

**12: všechny tři navržené alternativy.** Přesun Title,NewLn,
Blanks těsně za osmibytový BUF v data segmentu dá offsety8,33,35
odptop. Všechny jsou≤255, takže tři dvouoperandové LDA se opět
přeloží na jedinou ADDU immediate za1υ. Řetězce se nepřekrývají
s BUF a mají původní NUL. Smazání nadbytečnéhoGREG je pouze
změna loaderových metadat; žádný další runtime krok nevzniká.

Druhá alternativa ponechá řetězce v textu a mění přímo třiLDA
naSETL. Jejich původní adresy13c,155,157 se vejdou do16 bitů,
takže SETL předá přesný pointer a stojí stejně1υ. Třetí alternativa
GETA stojí také1υ, ale vyžaduje zarovnat každý string: Title
obsahuje nyní svůj LF,NUL, pakLOC(@+3)&−4, samostatný NewLn
LF,NUL, další stejnýLOC aBlanks. Při původním Title13c vyjdou
NewLn158 aBlanks15c, první následující instrukce164. Každý GETA
tak má správné nízké dva bity a vzdálenost bezpečně pod2^16
tetrabytes; ostatní symbolické větve se přepočtou. Alignment
nevytváří prováděné instrukce a Fputs dostává stejné ukončené
řetězce. Žádná alternativa neslibuje optimálnost proti všem programům.

**13: všechny jednotky a příkazy.** Řádky35–37 se změní BYTE→WYDE,
všechny čtyři Fputs na39/43/55/59 naFputws. Pattern je
0020066006600660, tedy space a tři vyšší nuly; units pointer je
BUF+8. Každé decimal remainder0..9 se zvýší o0660, uloží STWU
a pointer klesne o2. Každé prime2..3571 má1..4 digits, takže se
vždy zapíše units wyde na+8 a nejvýše další tři na+6,+4,+2.
Space na+0 zůstane; konečný NUL wyde na+10 zůstane z počáteční
nulové paměti. Žádná jiná instrukce do+10 nezapisuje. Platný buffer
zde zabírá12 bytů, přestože původní inicializační OCTA zapíše jen8;
zbylé byty jsou dostupná nulová data NNIX, nikoli cizí živý objekt.

Invariant každého decimal kroku je původní celočíselný quotient
a již zapsaný přesný suffix cifer; mění se pouze kód jednotky a
měřítko paměti. Počet vydů výstupu je stále space+čtyři digits,
terminátor se netiskne. Newline je000a. Všechny ukázané numerické
řádky byly čteny po skupinách z původního obrazu52: všech40 čísel
je správně převedeno do Arabic-Indic cifer a skupiny jsou ve
vizuálním pořadí obrácené proti logickému pořadí tabulky. Přímá
transkripce a shoda s dříve uzavřeným prime certifikátem jsou
v results/arabic-prime-display-reconciliation.json. Neproběhl
nový prime výpočet pro tento obrázek.

**13: numerické kódy, pořadí a formátovací předpoklady.** Primární
Unicode15 UnicodeData:1595–1604 přiřazuje každému0660..0669 právě
decimal value0..9 a bidi typAN. [UAX9, revize45](https://www.unicode.org/reports/tr9/tr9-45.html)
byla získána vcelku a přečteny konkrétní pravidla W3,N1,N2,I1,I2,L1,L2.
Arabic letters AL se převedou naR. Mezera mezi dvěma AN skupinami
se podleN1 chová jakoR. Při základní úrovni0 dostanou vnitřní
mezery úroveň1 a čísla2; při úrovni1 čísla rovněž dostanou2.
L2 obrátí každou úroveň2 a pak celý příslušný úsek úrovně1.
Proto se obrátí pořadí číselných skupin, ale uvnitř každé skupiny
proběhnou dvě obrácení a most-significant digit zůstane vlevo.
Krajní mezery/newline mají zvláštní L1/N2 pravidla, která nemění
žádnou ze40 hodnot ani jejich pořadí.

Je to přesná aplikace algoritmu na zdejší číslice/mezery bez
explicitních direction overrides, ne obecné tvrzení o všech Unicode
řetězcích. Výstup musí být podle zadání zformátován Unicode-aware
systémem a správně interpretován jako vyde data MMIX. Přímý
výpis do libovolného byte terminálu není takový předpoklad.
Odpověď správně odlišuje logické pořadí kódů v paměti od vizuálních
ligatur; rozvinutí stringu na jednotlivé character constants podle
pravidla2 nemění uloženou posloupnost.

Skutečný referenční MMIXAL:117–127 výslovně zatím nepřijímá
Unicode source characters přímo. Číselné `WYDE #0623,#0648,...`
a `INCL r,#0660` poskytují totéž data/code bez tohoto parserového
předpokladu; obecný jazykový příklad s Unicode literalem se
nevydává za empiricky podporovaný současný byte parser.
Přesná jazyková správnost arabského překladu titulku a historické
slovo „authentic“ nebyly nezávisle ověřeny. Jsou výslovná
lingvistická/historická výjimka, nikoli otevřená numerická nebo
bidi povinnost. Proto52 a108 nejsou plně zelené stránky.

**14.** Celý nový důkaz v exercises-1.3.2-009-014-recovery.md
pokrývá funkci první FP varianty, všechna9597 rozhodnutí, přesný
μ/υ rozdíl426192υ−59μ, konkrétní short-float variantu s38169υ
a posunutou odmocninu s9357 testy. Jsou tam explicitní FP režimy,
event předpoklady, roundoff meze, všechny indexy, změny instrukcí
a oba časové prahy. Obě „unless“ věty jsou posouzeny ve správném
směru implikace; žádné nové erratum z nich nevzniklo. Úloha14
již nemá starou neověřenou benchmarkovou část.

## File52–53/p44–45 a odpověď15 na109

**15, bez jakéhokoli provedení programu.** GREGy a,b,c jsou
konstantní global registry s2a,20,D; lokály1..3 jsou disjunktní.
Main NEG$1,1,75 nastaví−74, nikoli−75, a$2=0 je další volný
offset. Při začátku outer iterace k∈1..74 platí$1=k−75 a buffer
obsahuje přesně předchozí bloky spaces^j následované'*', j<k;
$2 je jejich součet délek. ADD$3,$1,75 nastaví k.

Vnitřní smyčka má zbývající counter$3∈1..k; STB napíše jeden
space na další byte, ADD zvýší$2 a SUB sníží counter. PBP jde
zpět právě dokud je counter>0. Po přesně k průchodech STB a
INCL přidají jednu hvězdičku. Obě větve, k=1 i k=74, mají totéž
invariantní chování; všechny indexy jsou malé nezáporné a
aritmetika nemůže přetéct. Zvýšení$1 a PBN pokračuje právě pro
k<74. Nakonec je$1=0 a řetězec kompletní.

Všechny zapsané byty jsou nenulové; první nezapsaný byte D+2849
je stále0 z počáteční paměti a slouží jako terminátor. Součet
délky je∑(k+1),k1..74=74·75/2+74=2849=binom(76,2)−1.
Fputs při úspěchu vypíše přesně tento řetězec, žádný newline
program nepřidává. Vizuální „OP art“ závisí na šířce a fontu
zobrazení; není to nezávislé tvrzení o konkrétní geometrii všech
terminálů. Halt potom končí. Program nebyl spuštěn ani sestaven.

## Zbytek file53/p45

**16.** Zadání je návrh a realizace PL/MMIX, s požadavkem rich
machine-oriented struktury a literate programming. Nic takového
v tomto auditu nevzniklo: E0132-016 zůstává open_research_project.
Úvodní motivace assembleru versus vyššího jazyka je návrhový
kontext, ne ověřená empirická statistika rozsahu programů. Původní
Wirth JACM15(1968),37–74 ani Literate Programming1992 nebyly
v tomto bloku získány; přesná bibliografie je výslovně přeskočena.

**Celý seznam technik druhé sady.** Každý vypsaný odkaz byl
porovnán se zadáním54–59. 17 má opcode switching table;18/28/35
matrix/square/diagram;24/25/35 copy/frequencies/text output;
21/27/30/32 mají Farey/Fibonacci/scaled harmonic/calendar arithmetic;
27 vyžaduje FP a32 umožňuje FP pro malé racionální výrazy s floor;
23/24/32 žádají subroutiny a33/34/35 jsou vhodné k rozdělení do
opakovaných rutin;29 je kruhové odstraňování z listu;34 řízení
v čase;35 typografický diagram;23/26 výslovně pipeline optimalizaci.
Je to pedagogické přiřazení možných technik, ne tvrzení, že každý
problém nutně potřebuje danou datovou strukturu nebo FP instrukci.
Žádný odkaz se nezaměnil za jinou úlohu.

**Fragment versus complete program.** Následující dva odstavce
normativně definují, co autor požaduje formulacemi write an MMIX
program/subroutine a write a complete MMIX program. První potřebuje
LABEL/OP/EXPR a remarks, případně externě dodaná data bez I/O;
nevyžaduje Main ani numeric/Times sloupce. Druhý vyžaduje executable
MMIXAL včetně Main a doporučuje test assemblerem/simulátorem.
To je přímá definice zadání, nikoli důkaz, že dříve převzatý MIX
program automaticky splňuje MMIX implementační úlohu. Stávající
partial položky s chybějícím úplným MMIX kódem zůstávají otevřené.

## Celý file107/p99 a108/p100

Odpovědi1–3 mají samostatný úplný důkaz v recovery-pages-049-051.md,
včetně modular počitadla a skutečného call interface třídění.
Srovnání s Algorithm5.2.3S je bibliografický odkaz na selection sort;
mechanismus stejné volby maxima a výměny je zde dokázán samostatně,
originální znění jiné kapitoly se nepřebírá jako nečtený důkaz.
Všechny vlastní matematické a implementační věty107 (odpovědi1–10)
jsou nyní argument-complete. Pouhé srovnávací čtenářské doporučení
není tvrzení o historickém prvenství ani chybějící premisa.

108 obsahuje celé odpovědi11–13 a první část14; všechny technické
věty mají výše přesné důkazy. Jedinou zachovanou výjimkou je
neověřený lingvistický titul/„authentic“ u13. Nezamlčuje se pod
statusem úplného argumentového pokrytí stránky.

## Celý file109/p101 a přesná zbývající odpověď17

Horní časové věty14 i celá odpověď15 jsou uzavřeny výše.
Zbývá17: tabulka má16 řádků po16 tetra a pojmenované maximové
masky a..h; kód začíná BN adresy, LDTU instrukce, SR22/LDT
tabulky, BDIF aPBNP, dále PUT větev sANDNML,BNZ,MOR,CMP,CSP.
Jeho dosavadní aritmetický invariant je přesně v
exercises-1.3.2-017-020.md, část17; cílená kontrola všech256
opcode/operandových oborů proti primární architektuře ještě není
tímto odstavcem prohlášena za úplnou. Pokračování na110 samo
uvádí omezení SAVE a skokových cílů, která musí být odlišena od
širšího zadání „all restrictions“. Globální optimalita rovněž
neplyne ze vzoru tabulky. E0132-017 zůstávápartial a109 není zelená.

Výsledná mapa:52/108 úplný technický rozsah s přesnou jazykovou
výjimkou;53partial kvůli otevřenému projektu16;107argument-complete;
109partial kvůli17. Žádný z těchto statusů neznamená, že je
hotová celá kniha nebo všechny odpovědní stránky.
