# Úloha1.3.2′–20: samostatné očekávané ceny pro různé prvky

Zadání file54, oba programy file110–112, obě vytištěné formule
file112. Důkaz nepřebírá instrukční multiplikátory z Hofriho–Jacqueta.
Používá úplné invarianty v recovery-pages-054-110-112.md a ceny
p22/endpaper. Platné konečné stavy a význam matematického m×n
zobecnění jsou výslovně uvedeny v C0018; není tvrzena nekonečná
kapacita fyzického MMIX. Níže jsou m,n≥2, při odhadech případně
m,n≥6, což neomezuje společnou limitu.

## Přesný profil Solution1, ještě bez předpokladu různých prvků

R = počet zpracovaných řádků; A = počet STB při jejich RowMin;
B = počet přísných zlepšení minima po prvním prvku řádku;
C = počet vyzkoušených kandidátních sloupců; D = počet jejich LDB;
S∈{0,1} = úspěšný návrat. Při shodě se zapisuje nová poloha
a přísné zlepšení B se nezvyšuje. První uložené minimum každého
řádku patří do A. Všechny tyto čítače mají konečný přesný obor.

Jedno RowMin bez počátečního SET ij: 5υ inicializace, 5υ závěr,
6υ za každý z n−1 dalších prvků, dalších7υ za přísné zlepšení
a dalších9υ za rovnost. Rovností je A_i−1−B_i. Tedy row cena je
`6n−5+9A_i−2B_i`, paměťově n+A_i. Zbylé cesty jsou:

| Část | υ |
|---|---:|
| Úvodní SET ij | 1 |
| Všechny RowMin | (6n−5)R+9A−2B |
| LDB/ADD na vstupu ColMax | 2C |
| Sloupcové LDB,CMP,PBN,SUB,PBP | 7D−4C+6S |
| No: SUB k a BP k | 4C−2R−2S |
| PBP ij po vyčerpání seznamu | R+2−3S |
| Úspěšné ADD/LDA/POP nebo neúspěšné POP | 3+2S |

Pro sloupcový řádek: neúspěšný sloupec má poslední cestu LDB,CMP,
taken PBN za3υ, předchozí za7υ. Úspěšný sloupec má všech m
průchodů, poslední PBP je chybně předpovězen a přidá2υ. V No
je BP not-taken právě R−Skrát, taken C−Rkrát. Poslední PBP ij
je not-taken právě při S=0. Tím jsou vyčerpány všechny větve.

Přesná cena pro libovolné shody je

`T_I=(nR+A+C+D) μ`
`   +[(6n−6)R+9A−2B+2C+7D+3S+6] υ`.                 (I)

Pro all-zero je R=1,A=n,B=0,C=1,D=m,S=1, tedy
(2n+m+1)μ+(15n+7m+5)υ; při9×8 přesně26μ+188υ.
Ručně lze zkontrolovat i nesedlovou2×2 matici se scan-řádky
(1,4),(3,2): A=3,B=1,C=2,D=3,R=2,S=0; vyjde12μ+68υ.
Tato kontrola nebyla spuštěna a nenahrazuje obecný profil.

Při různých prvcích je C=R a B=A−R. Formule(I) se zjednoduší na

`(nR+A+R+D) μ +[(6n−2)R+7A+7D+3S+6] υ`.           (I-distinct)

## První očekávání a chybějící2υ ve vytištěném výrazu

Vytvořme matematické čítače A*,D* pro všechny m řádky i v případě,
že původní rutina skončila dříve. Každý row minimum scan se provede
celý a sloupec se čte do prvního většího prvku, nejvýše m čtení.
To je definice náhodných veličin, nikoli nově spouštěný program.
Na matici bez sedla je R=m,S=0,A=A*,D=D* přesně.

Každý k-tý prvek v pořadí row-scanu je nové minimum s pravděpodobností
1/k, protože každý z k relativních ranků je stejně pravděpodobný.
Linearita očekávání tedy dává E[A*]=mH_n; nezávislost rekordů není
předpokládána.

Pro D* smíme místo rovnoměrné permutace vzít iid U(0,1) hodnoty:
všechna relativní pořadí mají stejnou pravděpodobnost a všechny
rozhodující větve závisí pouze na pořadí. Minimum jednoho řádku
má hustotu n(1−x)^(n−1). Po k nezávislých porovnáních z jiných
řádků je pravděpodobnost přežití

`q_k = n∫₀¹ x^k(1−x)^(n−1)dx = 1/binom(n+k,k)`.

Faktoriální integrál plyne opakovanou integrací per partes.
Je-li vlastní řádek kandidáta i-tý ve sloupcovém scanu, před j-tým
čtením je j−1 jiných porovnání při i≥j, jinak j−2; vlastní prvek
nikdy nemůže scan ukončit. Součtem přes všechna i,j dostáváme

`E[D*]=(m+1) Σ(k=0..m−1)q_k − m q_(m−1)`.

Z geometrické řady pod nezáporným integrálem plyne
Σ(k≥0)q_k=n/(n−1). Ocas od k=m je
`n∫x^m(1−x)^(n−2)dx = P/(n−1)`, kde
`P=m!n!/(m+n−1)!`; zároveň m q_(m−1)=P. Proto přesně

`E[D*]=(m+1)n/(n−1) − (m+n)P/(n−1)`.             (D)

Nikde se nepředpokládá nezávislost různých sloupcových scanů
nebo událostí, že dva řádky dávají sedlo; stačí linearita součtu.

Cena původní rutiny se od dosazení m,A*,D*,S=0 do(I-distinct)
liší jen při existenci sedla. Obě absolutní ceny jsou O((m+n)²),
protože A*≤mn a D*≤m². Pravděpodobnost tohoto jevu je P, jak je
nezávisle dokázáno v19/C0018. Rozdíl očekávání je proto
O((m+n)²P)=O((m+n)³/binom(m+n,m)). S pevnými μ,υ dostáváme

`E[T_I]=(mn+mH_n+2m+1+(m+1)/(n−1)) μ`
`       +(6mn+7mH_n+5m+13+7(m+1)/(n−1)) υ`
`       +O((m+n)³/binom(m+n,m))`.                  (I-corrected)

V knize stojí **11 místo13**. Počáteční SET a konečné POP jsou
zahrnuty stejně jako v obou správných all-zero příkladech. Poslední
PBP ij je not-taken a stojí3υ, nikoli1υ. Je to přesně rozdíl2υ
mezi řádným profilem a profilem, který tento konečný miss nezapočítá.

Podél m=n=N se opravný zbytek blíží nule, protože
binom(2N,N)≥4^N/(2N+1). Rozdíl skutečného očekávání a první
vytištěné hlavní části proto směřuje k2υ, zatímco vytištěný
O((2N)²/binom(2N,N)) směřuje k0. Tím je nezávisle vyvrácena také
první časová formule. **Pouhá změna11→13 zde není vydávána za
ověření původního ostřejšího zbytku**; dokázaný zbytek je(I-corrected).

## Solution2: přesná očekávání z podmíněných sloupců

Použijme přesný profil C0018:

`T_II=[(m+1)n+K+H] μ`
`    +[5mn+4n+11+9K−2R+5H+4S] υ`.                 (II)

R jsou navštívené řádky, K maticová čtení Phase2, H čtení s hodnotou
rovnou z=min_j C_j, S indikátor sedla. Pro odlišné hodnoty H≤1.
Definujme K*,H* stejnými row-scany ve všech m řádcích, i po případném
úspěchu. Platí |K*−K|≤mnS, |H*−H|≤S a |R−m|≤mS.

Při iid U(0,1) má z hustotu nm x^(m−1)(1−x^m)^(n−1). Sloupec L,
v němž C_L=z, je rovnoměrný mezi n možnostmi; jeho maximální řádek
I je rovnoměrný mezi m možnostmi. Podmíněně na z=x a L jsou ostatní
sloupce nezávislé, každý s maximem>x. V libovolném pevném řádku je
pravděpodobnost, že prvek takového sloupce je≥x, právě

`a(x)=(1−x)/(1−x^m)`:

jev „prvek≥x“ již zaručuje „maximum≥x“, takže jde přímo o podíl
pravděpodobností těchto dvou jevů. Ve sloupci L scan pokračuje jen
pokud jeho řádek je I, tedy s pravděpodobností1/m.

Pro j již přečtených sloupců prefix buď neobsahuje L (pravděpodobnost
1−j/n), nebo jej obsahuje (j/n). Přesná podmíněná pravděpodobnost
přežití prefixu je tedy

`q_j(x)=(1−j/n)a(x)^j + j/(mn) a(x)^(j−1)`, j≥1; q_0=1.

Proto `E[K*]=m Σ(j=0..n−1)E[q_j(z)]`.
Jediná hodnota z bude navštívena, pokud ve svém řádku přežije
všechny sloupce před L. Odtud též přesně

`E[H*]=(1/n)Σ(j=0..n−1)E[a(z)^j]`.

## Uniformní meze se stejným předpokladem jako v knize

Nechť m,n→∞ a log(n)/m→0. Položme Y=z^m, V=−logY; Y má
hustotu n(1−y)^(n−1) na(0,1). Ze vzorce

`∫₀¹ y^(s−1)(1−y)^kdy=k!/[s(s+1)…(s+k)]`

(integrace per partes) a jeho prvních dvou derivací v s=1 plyne
integrál prvního momentu −logy a druhého momentu log²y s hodnotami
H_(k+1)/(k+1) a [H_(k+1)²+H_(k+1)^(2)]/(k+1).
Derivace lze zaměnit s integrálem: v okolí s=1 dominují integrabilní
y^(−1/2)(1+|logy|²). H_t^(2)=Σ(k=1..t)1/k²≤2.

Nerovnost `0≤V−m(1−e^(−V/m))≤V²/(2m)` dává přímo

`0≤H_n−mE[q_1(z)]≤[H_(n−1)²+H_(n−1)^(2)]/(2m)`.

Tedy mE q_1=H_n+O(log²n/m), bez další podmínky na m/n.
Také

`E[a(z)²] ≤ n/[m²(n−2)] · [H_(n−2)²+H_(n−2)^(2)]`

pro n≥3, protože1−z≤V/m. Na z≥1/2 je a≤2/3, takže geometrické
součty členů j≥2 dávají

`m Σ(j≥2)E[q_j(z);z≥1/2] ≤ 3mE[a²]+18E[a]/n`.

Na doplňku P(z<1/2)=1−(1−2^(−m))^n≤n2^(−m) a celý počet
čtení je≤mn. Příspěvek je proto≤mn²2^(−m)=o(1/n): z podmínky
logn=o(m) plyne mn³2^(−m)→0. Dostáváme

`E[K*]=m+H_n+O(1/n)+O(log²n/m)`.

Analogicky E[H*]≤3/n+P(z<1/2)=O(1/n).

Zbývá odstranit umělý all-row průchod. Pro m,n≥6 označme N=m+n.
Binom(N,m)≥binom(N,6)≥(N/6)^6, protože min(m,n)≥6 a binomické
koeficienty rostou k prostředku. Proto mnP=O(N^(−3))=O(n^(−3)).
Chyby způsobené předčasným návratem se tedy vejdou do O(1/n).
S=P, E[R]=m+O(mP) a

`E[K]=m+H_n+O(1/n)+O(log²n/m)`, `E[H]=O(1/n)`.

Po dosazení do(II) máme samostatně dokázanou opravu druhé formule:

`E[T_II]=[(m+1)n+m+H_n] μ`
`        +(5mn+7m+4n+9H_n+11) υ`
`        +O(1/n)+O(log²n/m)`.                       (II-corrected)

Zbytek je v témže společném limitním režimu jako v knize. Když μ/υ
je pevné kladné, oba hlavní μ členy mají vedoucí mn, ale první
υ koeficient má6mn, druhý5mn. Rozdíl vedoucích nákladů je mnυ;
ostatní členy jsou o(mn), takže z těchto dvou konkrétních programů
je asymptoticky rychlejší Solution2. To není tvrzení globální
optimality ani srovnání s neimplementovanou třetí variantou.

## Rozsah uzavření

Obě původní distinct formule jsou doloženě chybné a obě mají výše
vlastní opravený výraz v přesně deklarovaném rozsahu. Původní
ostřejší zbytek první formule není potvrzen. Binární model se řeší
zvlášť; konkrétní třetí metoda a její náklady dosud nejsou uzavřeny.
Žádný nový běh se k tomuto důkazu nespouštěl. Historický článek
slouží jen jako bibliografický kontext, nikoli jako nepřečtené lemma.


Konečné doplnění20: exercises-1.3.2-020-third-recovery.md nyní dává úplný obecný MMIX kandidátní program, všechny větve a náklady, exact binary očekávání a rigorózní distinct9×8 srovnání. Třetí metoda je tím konkrétně realizována; v obou modelech má menší oba očekávané koeficienty než Solution2, a ta než Solution1. Úloha20 je argument_recorded; dřívější third-variant partial je vyřešeno. Globální optimum ani historické trial běhy se netvrdí.
