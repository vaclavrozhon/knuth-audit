# Obnova úplného rozsahu: file34–36 a answer pages102–106

6. listopadu 2026. Znovu jsou spárovány všechny podčásti úloh 25–58,
jejich odpovědi i začátek §1.3.2′. Staré argument_recorded se nepřebírá
automaticky: u úlohy48 se znovu otevírá nedoložená úplnost klasifikace.
Poznámka doplňuje mapu 145 stran, nikoli jen historický seznam partial.

## File34/p26: úlohy25–40

Každý následující odkaz znamená vlastní očíslovaný odstavec
`exercises-1.3.1-025-040.md`, přečtený proti odpovědím file103–105.

| Úloha/podtvrzení | Přesný argument a stav |
|---|---|
| 25 | XOR indikátor každé odlišné pozice, SADD součet 0..64; povolené aliasy vymezeny. |
| 26 | Čtyři dvojice vstupních bitů dávají právě ANDN, nezávisle ve všech64 pozicích. |
| 27 max i min | Bytewise d=max(0,y−z), z+d a y−d; meze0..255 vylučují carry/borrow mezi byty; explicitní scratch podmínky. |
| 28 | Dva monus rozdíly mají disjunktní nenulové případy, OR je absolutní rozdíl. |
| 29 | Dvojí komplement a monus dávají min(255,y+z); známá2023 oprava scratch není nový nález. |
| 30 | XOR s20, BDIF od1 a SADD: každý blank přispěje právě jednou. Předem načtené konstanty jsou výslovně povoleny zadáním. |
| 31 | MXOR redukuje každý byte do jediného parity bitu; SADD jej sčítá. |
| 32 | Pro1×1 je komutativita • nutná; pro obecné matice stačí, protože pořadí vnější redukce zůstává stejné. Protipříklad bez ní je vlastní. |
| 33 | Konkrétní byte permutace a jednooperační minimum s dostupnou maskou jsou prokázány. Neurčený setup masky zůstává přesná partial optimalita. |
| 34 oba směry a BadCase | Všech osm výběrů řádků, obě MUX větve, kontrola všech high bytů a konečná permutace jsou odvozeny. BadCase ověřuje8bitovou representability, nikoli obecnou7bitovou ASCII platnost. |
| 35 | Dvě MOR jsou násobení antidiagonální maticí zleva i zprava; každá pozice(i,j) přejde na(9−i,9−j). |
| 36 všechny tři věty odpovědi | Nerovnostní maska, varianta větší-než s BDIF i osmibitové kódování pozic mají vlastní bitové argumenty. |
| 37 hlavní konstrukce a všechny dodatky | Viz přesné převzetí níže; nejsou uzavřeny pouze jednou ukázkou T². |
| 38 všechny výstupy a obě změny programu | Smyčkový invariant suffixu, nejvýše8 iterací (pro0jedna), rozsah součtu, poslední nenulový byte, unsigned varianta a možnost SL overflow. |
| 39(a–f), prahy a signed výhrada | Všech šest dvojic časů, jejich očekávání podle p, práh2/3 a overflow v nepotřebné spekulativní větvi; při p=1 se(e) rovná, „win“ není doklad ostrého zlepšení. |
| 40 a pokračování na file105 | Rozdíl alignovaného M4[A] a skutečného PC, konkrétní101/105, GETA i zachování low dvou bitů relativním posunem. |

U37 se přesně přebírá **celý** důkaz kritéria z
`workstreams/vol2/notes/primitive-polynomials.md`, „Kritérium na str.30“:
zbytek x řádu2^k−1 vyčerpá nenulové prvky podílového okruhu, takže
každý nenulový prvek je jednotka a okruh je těleso. Předpoklady p=2,
monický stupeň k a počet2^k zbytků jsou stejné. Žádný starý census
nebyl spuštěn. Uložené **všechny** sedm certifikátů pro masky
7,d,19,29,61,c1,171 a všechny jejich prime-factor exponenty byly
přečteny v `results/field37-power-certificates.json`. To odpovídá
právě šesti menším maticím a hlavní8×8, ne obecné tabulce všech polí.

MaticeT má minimální polynom stupně8 z nezávislosti prvního řádku
I,T,…,T^7; její p(T)=0, zobrazené T² a komutace polynomů vT jsou
samostatné argumenty. Blokové16×16 násobení má čtyři výstupy po dvou
součinech a jednom XOR. V kvadratickém rozšíření existuje c s trace1:
trace je nenulový polynom stupně128<256 a trace(t)²=trace(t), takže
jeho obraz je celéF2. Obraz t²+t má128 prvků, je v jádru trace a proto
se mu rovná. u²+u+c je tedy ireducibilní. Roznásobení dává přesně
pět MXOR a tři XOR, jak tvrdí odpověď. Konstrukce menších polí používá
jednotku příslušného bloku, nikoli celé8×8 identity.

File34 je celé zmapováno, ale zůstává partial kvůli minimálnímu
programu33 při neurčeném počátečním oboru konstant. Připsání J.Dallos
u pozdější43 a další autorská poděkování nejsou matematickými důkazy.

## File35/p27: úlohy41–52, začátek

V `exercises-1.3.1-041-058.md` jsou proti originálu přečteny jednotlivě:
41(a,b,c) obě větve a destinační alokace; 41(d) konkrétní neshoda SR
versus nezáporný byte a úplná náhrada SRU; 42(a) signed minimum s V,
42(b) sign-bit transformace všech typů; 43 trailing i leading count,
zero dodatek a obě ceny; 44 všechny čtyři high-tetra operace včetně
alias podmínky a nulového dělitele; 45 přiřazení všech8eventů; 46 TRIP
na0; 47 oba opcodes i assemblerová volba I/B; 49 celá ruční stopa,
50 všechny četnosti/náklady, 51 všech18kódů ve správném sloupcovém
pořadí; 52 pokračuje na další stránce.

U49 se přebírá přesně vymezený abstraktní instrukční kontrakt a platné
adresy; program nesmí být přepsán svými třemi stores. Výsledkové
registry, obě paměťové změny, rH, rA a rB mají samostatnou stopu.
Vnitřní reprezentace register stacku není znovu dokazována touto úlohou.
U43 zůstává globální fastest/shortest mez neprokázaná; srovnání dvou
konkrétních konstrukcí není její důkaz.

**48 se znovu otevírá.** Starý text prokázal všechny **vyjmenované**
ekvivalentní dvojice a uvedl rozlišující NEG/NEGU příklad. Neprokázal
však, že žádné další dvojice všech256 opcodů neexistují za stejných
XYZ a se stejnou cenou. Tuto úplnost nelze doplnit větou „ostatní
instrukce jsou různé“. Je potřeba přesná operační ekvivalence včetně
cache-hint účinků a rozlišující argumenty zbývajících rodin. Kladné
dvojice a celé malé immediate konverze zůstávají prokázané; status
celé úlohy je nyní partial. Žádný nový nalezený chybný pár netvrdím.

## File36/p28: 52–58 a začátek ProgramuM

52 má přesné již přijaté C0011 pro chybějící no-op případy. Důkaz
neúplnosti odpovědi je uzavřen, ale požadovaná opravená klasifikace
všech256 opcodů zatím není. Nový průchod nezaměňuje tyto dva závazky.
53 má úplný přímý seznam rH (MULU/MULUI, PUT/PUTI, UNSAVE) a záporný
argument zbývajících účinků; stejná přímá konvence je výslovná u54–55.

`exercises-1.3.1-054-055-recovery.md` nově prokazuje celé klasifikace:
38opcodů pro rA,181pro rL v uživatelském režimu a183 při zahrnutí
privilegovaného LDVTS. U54 zbývá pouze výklad vytištěné výpustky
FSUB…FCMPE; u55 pouze rozsah uživatelský/privilegovaný. Větší neadresná
závislost na celém IEEE nebo hypotetickém OS již není důvodem partial.

56 má ověřeny všechny tři publikované konstrukce, všechny čtyři
části packing argumentu (low/high,25bit sign extension, konečný
součin), původní krajové certifikáty28/29, addition-chain dolní mez
pouze v jejím vlastním modelu a všechny uvedené ceny. Globální minima
prostoru/času se nepřebírají z těchto tří příkladů. Navíc je třeba
zpřesnit, zda předem načtené globální konstanty smějí být spotřebovány
jako scratch: pokud ano, preloaded12 může být přímo loop counter a
v šestipříkazové konstrukci odpadne SETL. Tato hranice je zaznamenána
níže, bez předčasného nového nálezu.

57 má doložené konkrétní důvody nevýhody self-modification; univerzální
„cannot be used by more than one process“ zůstává bez určeného
sdílení/synchronizace partial. 58 je otevřený NNIX projekt s rating50,
nikoli dokončená úloha. Citace Randolph/Wilson1953 nebyla v rychlém
hledání nalezena v originálu; výsledky pouze opakují tuto knihu.
Je výslovně přeskočená bibliografie, nikoli ověření citace.

V0078–V0079 začínají na stejné stránce. Převzatý argument
`independent-arguments-028-032.md` má konkrétní invariant suffixového
maxima, předpoklad1≤n<2^60, platné pole, stabilní global x0 a celé
dekódování11instrukcí. Na této stránce prvních šest assemblerových
řádků nevytváří instrukce, tři následující nastaví kk=8n,m=X[n] a
jump na DecrK. Jejich kódy39020003,8c01fe02,f0000006, adresy100/104/108
a jednorázové četnosti přesně souhlasí. Návratový kontrakt a pokračování
na dalších stranách mají vlastní dříve přijaté důkazy; nereprodukují se.

## Přesná hranice mutable-global u úlohy56

Pokud „all necessary constants have been preloaded into global registers“
dovoluje změnit pomocný global a nepožaduje jeho zachování, nechť global
c obsahuje12 a global a adresu vstupu x. Pak stačí těchto pět instrukcí:

    LDO  $1,a,0
    SET  $0,$1
1H  MUL  $0,$0,$1
    SUB  c,c,1
    PBP  c,1B

Po j iteracích,0≤j≤12, je $0=x^(j+1), c=12−j a $1=x. Konec je
přesně j=12, tedy požadované x^13. Pro dovolené |x|≤28 žádný součin
nepřekročí velikost povoleného x^13 (případy0,±1 jsou přímo bezpečné);
counter jde12..0 bez V. Prostor je20bytů; čas μ+148υ. Oproti otištěné
smyčce se skutečně odstraní jedno SETL, žádný další příkaz se nepřidá.
Při požadavku zachovat všechny preloaded globals tento program není
přípustným zlepšením. Zatím není rozhodnuto, zda tento požadavek plyne
z zamýšlené konvence zadání; proto je to konkrétní scope závislost
globálního minima, nikoli nově potvrzený nález či důkaz nejlepšího času.

## Celé odpovědní strany102–106

102/p94 obsahuje přesně odpovědi1–13. Všechny matematické části jsou
spárovány s úplným již uloženým blokem1–24 a jeho recovery mapou;
Purdy, historie byte/Buchholz a O'Beirne citace zůstávají bibliografické
výjimky. SI prefixy i známá2023oprava jsou zohledněny, nikoli nálezy.
Stránka je reconciled_with_exclusions.

103/p95 obsahuje14–31. 14–24 mají plné dřívější argumenty včetně všech
499 kritérií odpovědi19, zde nyní doplněných25–31. Granlund/Montgomery
a historické tvrzení o compiler-writers/1950s zůstávají explicitní
faktické/bibliografické výjimky. Matematický census se neopakoval.

104/p96 obsahuje32–40 a je partial pouze kvůli33. 105/p97 obsahuje
konec40 a41–52, partial kvůli43, nově znovu otevřenému48 a52. 106/p98
obsahuje53–57, partial kvůli přesným54/55 interpretacím,56 minimům a57
rozsahu sdílení. Všechny dodatky odpovědí jsou zahrnuty; shoda samotných
zadání s čísly odpovědí by tento stav neospravedlnila.

Žádný nový aritmetický běh, benchmark ani census. Stránkový kurzor
pokračuje file37/p29; odpovědní strany jsou mapovány mimo pořadí,
protože jejich celý obsah byl právě pokryt. Reading a argument coverage
zůstávají oddělené; žádná z těchto osmi stran se neoznačuje zeleně.
