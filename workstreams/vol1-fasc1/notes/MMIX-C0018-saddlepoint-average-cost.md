# MMIX-C0018 — oba průměrné časy sedlových programů mají chybný profil

**Stav:** confirmed v doloženém digitálním vydání, nezávislá kořenová
revize přijata v X0072 dne12.11.2026. **Závažnost:** low. **Rozsah:** knižní časová analýza
v odpovědi 1.3.2′–20, p.104/file112. Správnost hledání sedlového prvku
se tím nemění. Není to nález v doprovodném programu.

První vytištěný výraz navíc podhodnocuje konstantu o2υ; jeho vlastní
obecný důkaz a opravený očekávaný profil jsou v
`exercises-1.3.2-020-distinct-recovery.md`. Níže je celý samostatný
rozpor druhého výrazu, který nezávisí na tomto dodatečném výsledku.

Vytištěný druhý výraz je

`(m+1)n μ + (5mn+6m+4n+7H_n+8) υ + O(1/n)+O(log²(n)/m)`.

Uvedený koeficient μ je přesně počet load/store instrukcí samotné
Phase1. Na každé matici bez sedlového prvku musí Phase2 navíc číst
alespoň m prvků. Ani další koeficienty se nemohou proti této ztrátě
vyrušit: níže je přímý důkaz, že pro m=n=N a libovolné pevné μ,υ>0
je skutečná očekávaná cena vyšší o Ω(N), zatímco oba vytištěné
zbytky směřují k nule.

## Smlouva a platné stavy

Čas se počítá přesně podle p.22/file30: mem je každé load/store,
υ podle tabulky, správná předpověď větve 1υ, chybná 3υ, POP 3υ.
Nezapočítáváme volajícího, počáteční assemblerová data, fetches,
cache ani OS. μ a υ jsou nezávislé jednotky téhož knižního modelu.

Pro skutečný vytištěný program jsou m=9,n=8, A=Data_Segment,
data jsou signed byty na A+8i+j, 1≤i≤9,1≤j≤8. Oblast A+1..8
je zapisovatelná pomocná hlavička a s maticí A+9..80 je disjunktní.
Globální báze a pracovní registry jsou platně inicializované,
$255 je scratch, ans=$0, návratový zásobník splňuje standardní
POP kontrakt. Všechny indexy jsou malé a adresy jsou nezáporné;
SUB/CMP pracují s rozdíly −255..255, bez overflow.

Asymptotický výrok knihy sám zobecňuje tento algoritmus na m×n
matice s libovolným relativním pořadím mn různých prvků. V témže
abstraktním modelu níže nahradíme rozměrové konstanty symboly m,n
a počítáme stejné instrukční cesty pro m,n≥2. Netvrdíme, že se
nekonečná rodina různých hodnot vejde do pevného signed-byte oboru
nebo do konečné 64bitové paměti. Dodatečná příprava velkých konstant
či širších hodnot by chybějící kladnou práci neodečetla. Rozpor je
uvnitř zamýšleného matematického modelu vytištěné asymptotiky.

## Úplný profil Phase1

Invariant v jednom sloupci: x je maximum již přečteného spodního
úseku; každý průchod přidá právě další prvek a CSN zachová maximum.
Po posledním průchodu ij=j−n, takže STB zapisuje na A+j, nikoli
do matice. Z je minimum dosud dokončených sloupcových maxim.
Po všech n sloupcích je z=min_j C_j. Pro signed byty je počáteční
z=1000 přísně větší než každý možný C_j.

Každý sloupec načte m hodnot a zapíše jednu hlavičku: přesně
`(m+1)n` mems, bez závislosti na datech.

| Část | Počet υ |
|---|---:|
| Dva úvodní SET | 2 |
| ADD a první LDB v každém sloupci | 2n |
| LDB,CMP,CSN,SUB pro dalších m−1 prvků | 4n(m−1) |
| Vnitřní PBP: m−2 taken, poslední not-taken | n(m+1) |
| STB,CMP,CSN,SUB j po sloupci | 4n |
| Vnější PBP: n−1 taken, poslední not-taken | n+2 |

Součet je přesně `5mn+4n+4` υ. Pro 9×8 dostáváme 80μ+396υ,
což souhlasí i s nezávisle ručně rozebraným all-zero případem.

## Úplný profil Phase2, včetně úspěchu, neúspěchu a rovnosti

Označme R počet navštívených řádků, K počet načtených maticových
prvků v této fázi, H počet navštívených prvků rovných z a S indikátor
úspěšného návratu, S∈{0,1}. H se počítá pro každou rovnost, i když
její sloupcové maximum není z. Pro různé vstupní hodnoty H≤1;
níže uvedený profil platí i při shodách.

Při vstupu do řádku jsou ii=n(i−1), ij=ii+n a j=n. Smyčka čte
řádek zprava doleva. Prvek <z řádek odmítne. Při prvku >z se
přeskočí hlavička. Při rovnosti se čte C_j; CSZ uloží kandidáta
jen při C_j=z. Pokud celý řádek projde, máme R_i≥z; protože
R_i≤min C_j=z, je tento řádek sedlový. Sloupec s C_j=z existuje
a v tomto řádku musí mít hodnotu z, takže ans byl určitě přepsán.
Staré ans z dřívějšího neúspěšného řádku nemůže uniknout do návratu.
Při neúspěchu všech m řádků poslední SET ans,0 výsledek vynuluje.

| Instrukce/cesta | Počet υ |
|---|---:|
| SET ii | 1 |
| ADD ij a SET j na začátku řádku | 2R |
| Maticové LDB a SUB t,z,x | 2K |
| PBP t,No: R−S taken, ostatní not-taken | 3K−2R+2S |
| PBN t,2F: H not-taken, ostatní taken | K−R+S+2H |
| Hlavičkové LDB,CMP,CSZ | 3H |
| SUB j a SUB ij | 2(K−R+S) |
| PBP j: právě S závěrečných not-taken | K−R+3S |
| No: SUB ii a PBNN, poslední not-taken jen při S=0 | 2(R−S)+2(1−S) |
| LDA/POP při úspěchu nebo SET/POP při neúspěchu | 4 |

Součet je přesně `9K−2R+5H+4S+7` υ. Jediné paměťové operace
jsou K maticových a H hlavičkových LDB, tedy K+H mems.
R≤m a K≤mn zaručují ukončení; indexy snižujeme a žádná větev
nevrací již zpracovanou část. Hlavičky se během této fáze nemění.

**Přesná opravená parametrická cena celého programu** je proto

`[(m+1)n+K+H] μ`
`+ [5mn+4n+11+9K−2R+5H+4S] υ`.

Pro nulovou 9×8 matici jsou R=1,K=H=8,S=1; vyjde přesně
96μ+517υ, tedy zde kniha uvádí správné číslo. Při absenci sedla
jsou R=m,S=0,K≥m,H≥0, a Phase2 proto stojí alespoň

`m μ + (7m+7) υ`.

To nevyžaduje nezávislost řádkových událostí ani odhad délky scanů.

## Přesný probabilistický rozpor

Pro m×n různé prvky s rovnoměrným relativním pořadím je
P(sedlo)=m!n!/(m+n−1)!=(m+n)/binom(m+n,n). Důkaz: sedla mají
stejnou hodnotu podle minimax nerovnosti, a proto je při různých
prvcích nejvýše jedno. Pro danou buňku vyžadujeme, aby m−1 prvků
jejího sloupce bylo menších a n−1 ostatních v jejím řádku větších.
Z (m+n−1)! relativních pořadí vyhovuje (m−1)!(n−1)!, potom násobíme
mn disjunktními možnostmi. Jde o přesný argument, nikoli simulaci.

Phase1 je deterministická pro každou matici a Phase2 má nezápornou
cenu i při sedle. Pro P=P(sedlo) tedy

`E[T] ≥ (m+1)n μ + (5mn+4n+4) υ`
`        + (1−P)[m μ+(7m+7) υ]`.

Po odečtení vytištěné hlavní části zbývá nejméně

`m(1−P) μ + [m+3−7H_n−(7m+7)P] υ`.

Vezměme m=n=N→∞. Je to dovolená cesta s log(n)/m→0.
Centrální binomický koeficient je největší z 2N+1 koeficientů,
jejichž součet je 4^N; proto

`P=2N/binom(2N,N) ≤ 2N(2N+1)/4^N`.

Tedy P→0 a NP→0. Z integrálního srovnání H_N≤1+log N plyne,
že rozdíl dělený N má dolní limit alespoň μ+υ>0. Vytištěné
O(1/N)+O(log²N/N) jsou oproti tomu o(1). Rovnost s uvedeným
zbytkem je proto nemožná i pro pevné μ=υ=1; není třeba spoléhat
jen na nezávislé interpretování obou koeficientů.

Následný úplný vlastní důkaz v `exercises-1.3.2-020-distinct-recovery.md`
odvodil E[K]=m+H_n+O(1/n)+O(log²n/m), E[H]=O(1/n) a přesné
meze předčasného návratu. Opravená druhá hlavní část je
`[(m+1)n+m+H_n]μ+(5mn+7m+4n+9H_n+11)υ` se stejným
deklarovaným zbytkem a předpokladem logn/m→0. První výraz
má13 místo11 a samostatně dokázaný zbytek
O((m+n)³/binom(m+n,m)); původní ostřejší zbytek se nepotvrzuje.

Také oba binární průměry jsou nyní přesně odvozeny v samostatné
`exercises-1.3.2-020-binary-recovery.md`, bez2^72 enumerace.
Následně `exercises-1.3.2-020-third-recovery.md` uzavřela i
konkrétní třetí variantu v obou modelech, včetně úplného MMIX
zdroje a vlastního nákladového srovnání. Celá úloha20 je nyní
argument_recorded. Dva chybné výrazy zůstávají jediným souvisejícím
knižním nálezem C0018, nikoli dalšími programovými kartami.

## Originál, zdroje a všechny vrstvy errat

Zobrazeny sazby file110–112, zejména celý druhý výraz na file112;
rozpor není OCR. PDF digital release3, květen2023, SHA256
`16f86d86839647a0c99be829a537a7516577704393ad8f95492ab42119905666`.
Fyzický dotisk prohlédnut nebyl. Definice mem/υ je na file30;
všechny použité náklady potvrzuje původní endpaper file145 a
MMIX-doc:3230–3273. Nepoužil se další běh, assembler ani benchmark.

`results/errata-C0018.json` obsahuje hash a konkrétní kontexty
13 vrstev: fasciklový zdroj, krátká a dlouhá errata; MMIXware errata,
aktuální distribuce, upstream bugs, rounding notes a warnings;
svazek1 source/current long, oba historické long soubory a druhé
vydání. Všechny nalezené kontexty byly přečteny.

Známá oprava p104 z26.5.2012 mění PBP ii,3B na PBNN ii,3B;
**již je v naší sazbě a v tomto důkazu použita**. Není novým nálezem
a chybějící Phase2 mems neopravuje. Starší svazek1 p514 opravuje
MIX indexování a koncové instrukce; p515 přidává roku1997 MIX
asymptotiku. Jsou to jiné instrukční ceny, bez MMIX μ koeficientu.
Žádná z těchto vrstev neopravuje nynější druhý MMIX výraz.
Doplňkové dotazy na primárních webech nenalezly odpovídající opravu;
netvrdíme světové prvenství ani nepřítomnost soukromé korespondence.

[Autorský report Hofriho–Jacqueta v Rice](https://repository.rice.edu/server/api/core/bitstreams/0f8d143e-0a09-40fd-900e-c8ffa1c865d4/content)
byl získán a celý text přečten; jeho úvod výslovně nepočítá
instrukční multiplikátory konkrétního programu. Získaná verze
navíc při některých rozvojích předpokládá srovnatelné tempo růstu
m,n; totožnost se stránkami publikované verze není zatím doložena.
Žádný její rozvoj proto zde nenahrazuje samostatný výše uvedený
důkaz. Je uložen jako bibliografický podklad, nikoli autorita pro
chybné koeficienty v knize.
