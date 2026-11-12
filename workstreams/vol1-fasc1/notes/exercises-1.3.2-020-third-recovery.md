# Úloha1.3.2′–20: konkrétní třetí MMIX metoda a úplné srovnání

Poslední otevřená matematická podčást úlohy20 je zde uzavřena.
Kniha třetí kód neudává; cenu proto musíme spojit s konkrétním
provedením, nikoli s neurčitou větou „méně řádků“. Celý původní
`workstreams/vol1/notes/mixal-saddle.md`, včetně §8, byl nově
přečten. Přebírá se odtud pouze úplně dokázaný princip obecného
kandidátního filtru se stejnými předpoklady; MIX instrukce ani
MIX časové koeficienty se nepřenášejí. Níže jsou vlastní MMIX
kód, invarianty a náklady.

## Konkrétní program a obor

`sources/saddle20-candidates.mms` má kompletní tělo podprogramu
Saddle3. Pro skutečné zadání m=9,n=8, signed byty v A+8i+j,
A=Data_Segment. Matice je čitelná a během rutiny se nemění;
žádný pomocný zápis do ní ani do prefixu A+1..8 není třeba.
GREG báze a pracovní registry jsou definovány, ans=$0,t=$255.
Volající musí mít platný návratový rámec pro POP1 a smí připustit
změnu pojmenovaných pracovních registrů. Žádné další volání není.

Phase1 je plné sloupcové hledání z Solution2, s těmito dvěma
změnami: vynechá se STB sloupcového maxima a přidá se
`CSN best,t,j` hned za CSN z,t,x. T stále obsahuje výsledek
srovnání nového maxima s předchozím z. Invariant: x je maximum
zpracovaného úseku sloupce, z nejmenší dosud dokončené maximum,
best index jednoho sloupce s tímto maximem. První maximum je
≤127<1000, takže best se vždy definuje; při rovnosti zůstane
dřívější index, tj. pravější sloupec v pořadí scanů. Po všech
sloupcích C_best=z=min C. Zbylé průchody a meze jsou přesně
uzavřené v Solution2. Matice není poškozena vynecháním STB.

Phase2 pro řádek i udržuje ii=8(i−1). ADD ans,ii,best dává
offset kandidátní buňky vůči a10=A+8. LDB/CMP/PBNZ zahodí řádek,
pokud jeho hodnota v best není z. Hodnota nikdy nemůže být>z,
protože z=C_best; selhání filtru tedy znamená a_i,best<z.

Pokud filtr projde, ans už obsahuje index skutečné hodnoty z.
ADD ij,ii,8 a SET j,8 zahájí celý row scan. LDB/CMP/PBN odmítne
řádek při prvním prvku<z; jinak SUB j/SUB ij/PBP projdou všech8
prvků. Při úspěchu je každý prvek≥z a a_i,best=z, proto jde
o řádkové minimum a zároveň sloupcové maximum. LDA/POP vrátí
správnou adresu. Ans se během tohoto row-scanu nemění.

Na NextRow snížíme ii o8; PBNN zpracuje i ii=0. Teprve−8
vede k SET ans,0/POP. Každý skutečný sedlový řádek musí filtrem
projít: jeho minimum je z a v best má současně hodnotu≥z a≤z.
Žádné sedlo se tedy neztratí, včetně libovolných shod. Neúspěšné
ans z jiného řádku se nikdy nevrací. Rutinou je realizována
nadmnožina průniku kandidátních řádků z knižní nápovědy; zbývající
podmínky všech dalších minimaxových sloupců vyřídí úplný row test.
Nejde o tvrzení totožnosti s nějakým v knize nevypsaným kódem.

Indexy jsou v bezpečném rozsahu−7..72, všechny čtené adresy
A+9..80. CMP nepotřebuje rozdíl s možným overflow. Počet řádků
R≤m, počet kandidátů C≤R a row čtení K≤nC; konečnost a návrat
jsou úplné. Stejné relativní pořadí a srovnání dávají matematické
m×n zobecnění popsané v C0018, s m,n≥2.

## Úplný profil všech větví

Phase1 má mn LDB, žádný store. Vynechaný STB a přidaný CSN best
mají každý1υ; proto je cena přesně

`mn μ +(5mn+4n+4) υ`.

Označme R počet navštívených řádků, C počet těch, které projdou
filtrem, K počet maticových LDB uvnitř jejich úplného row testu,
S∈{0,1} úspěch. Filter LDB není součástí K.

| Phase2 část | υ |
|---|---:|
| Úvodní SET ii | 1 |
| ADD ans,LDB,CMP pro každý řádek | 3R |
| PBNZ: C not-taken, R−C taken | R+2C |
| ADD ij a SET j pro kandidáta | 2C |
| Row LDB,CMP | 2K |
| PBN: C−S taken, ostatní not-taken | 3K−2C+2S |
| SUB j a SUB ij | 2K−2C+2S |
| PBP j: poslední not-taken jen při úspěchu | K−C+3S |
| NextRow: SUB ii a PBNN | 2R+2−4S |
| LDA/POP nebo SET/POP | 4 |

Součet je6R−C+8K+3S+7; mems jsou R+K. Tedy přesně

`T_III=(mn+R+K) μ`
`     +(5mn+4n+11+6R−C+8K+3S) υ`.                   (III)

Stejná cena platí při shodách i bez nich. U all-zero9×8 je
R=C=S=1,K=8 a dostáváme81μ+475υ. Nejmenšího z původních
all-zero časů,26μ+188υ, tato varianta nedosahuje; očekávané
srovnání se nesmí zaměnit za dominanci na každém vstupu.

## Různé prvky: přesný třetí průměr

P=(m+n)/binom(m+n,m). Jediný minimaxový sloupec má právě jeden
maximální řádek, tedy C=1 vždy. Tento řádek se jistě navštíví.
Jestliže neexistuje sedlo, filtrem se projde všech m řádků.
Při sedle je jeho řádek rovnoměrný mezi m možnostmi, proto

`E[R]=m−(m−1)P/2`, `E[S]=P`.

Při podmínění z=x použijme a(x)=(1−x)/(1−x^m) z již úplného
distinct důkazu. V kandidátním řádku se minmaxový sloupec nikdy
neodmítne. Pravděpodobnost přežití prvních j sloupců je tedy

`r_j(x)=(1−j/n)a(x)^j+(j/n)a(x)^(j−1)`, j≥1; r_0=1.

Odůvodnění: poloha vybraného sloupce je rovnoměrná, ostatní
sloupce jsou po podmínění nezávislé; na rozdíl od obecného řádku
zde přežití vybraného sloupce nemá další faktor1/m. Proto

`J=E[K]=Σ(j=0..n−1)E[r_j(z)]`.

Pro přesné vyčíslení definujme

`I(k,N)=m∫₀¹(1−x)^k x^(m−1)(1−x^m)^(N−1)dx`.

Rozvinutím obou konečných binomů, bez limitní aproximace,

`I(k,N)=m Σ(a=0..k)Σ(b=0..N−1)`
`       (−1)^(a+b)binom(k,a)binom(N−1,b)/[m(b+1)+a]`.

Pro j<n pak E[r_j]=(n−j)I(j,n−j)+jI(j−1,n−j+1), kde
druhý člen při j=0 vynecháme. Celý třetí distinct průměr je
exact dosazení C=1,R=m−(m−1)P/2,K=J,S=P do(III).

Pro společnou limitu logn/m→0 odhady a² a výjimečné oblasti
z<1/2 z distinct poznámky dávají J=1+O(logn/m)+O(1/n).
Tedy třetí cena má hlavní členy

`(mn+m+1)μ+(5mn+6m+4n+18)υ`.

U Solution2 jsou odpovídající dodatečné členy v μ větší o
n+H_n−1 a v υ o m+9H_n−7. Jeho chybový člen O(log²n/m)
je o(m) a také o(n); pro pevné μ/υ jsou tedy nižšího řádu
než tyto kladné rozdíly. Třetí varianta je asymptoticky lepší
než Solution2, a ta lepší než Solution1. Žádné optimum vůči
všem možným MMIX programům se netvrdí.

## Rigorózní pevné9×8 srovnání, bez asymptotického odhadu

Pro dvě původní rutiny je možné získat těsné přesné intervaly.
Nechť M je počet řádků vynechaných po nalezení sedla; E[M]=
(m−1)P/2. V prvním programu každá vynechaná řádka obsahuje
1..n rekordních zápisů a1..m sloupcových čtení. Označme jejich
součty A_skip,D_skip. All-row cena T* z distinct poznámky se od
skutečné ceny liší přesně o

`[(n+1)M+A_skip+D_skip]μ`
`+[(6n−2)M+7A_skip+7D_skip−3S]υ`.

Meze M≤A_skip≤nM a M≤D_skip≤mM dávají exact racionální intervaly
po dosazení již odvozených E[A*]=mH_n a E[D*]. Nespoléhají na
žádnou podmíněnou nezávislost těchto veličin.

Pro Solution2 označme K* all-row počet. Je M≤K*−K≤nM. Hodnota z
je v celé matici jediná a při sedle leží v úspěšném řádku, takže
H*=H přesně, i při předčasném návratu. Máme

`E[K*]=mΣ(j=0..n−1)[(n−j)I(j,n−j)+(j/m)I(j−1,n−j+1)]`,
`E[H*]=Σ(j=0..n−1)I(j,n−j)`.

Tyto konečné racionální integrály a přesné E[R],E[S] dosadíme
do jeho úplného profilu, s oběma mezemi K. Výsledné intervaly
nejsou statistické intervaly spolehlivosti.

| Distinct9×8 | Mems | Oops |
|---|---:|---:|
| Solution1 | [116.814860,116.856819] | [670.753671,671.047378] |
| Solution2 | [92.378902,92.398484] | [495.715645,495.891869] |
| Konkrétní III | 82.577965547… | 468.631416685… |

Meze v tabulce jsou zaokrouhleny ven; exact čitatele a jmenovatele
jsou v výsledném JSON. Oba náklady jsou odděleny kladnými mezerami,
proto pro každé μ,υ>0 platí E[T_III]<E[T_II]<E[T_I].

## Binární model: exact třetí očekávání

Použijme již úplně dokázaná a,b,c,Q(r,k) z binary poznámky.
Na𝒵 (nulový sloupec) z=0, první řádek je kandidát a celý projde:
R=C=S=1,K=n. Na𝒩 jsou všechna C_j=1, proto best zůstane právě
první zpracovaný sloupec, tedy pravý krajní. To je i první
prvek každého úplného row-scanu. Row r je kandidátem právě když
je dosažen a první jeho bit je1, což má váhu Q(r,1).

Kandidátní row scan znovu čte první bit a pak pokračuje při
přežití prefixů délky1..n−1. Tedy přesně

`E[C]=a+Σ(r=1..m)Q(r,1)`,
`E[K]=na+Σ(r=1..m)[Q(r,1)+Σ(k=1..n−1)Q(r,k)]`.

R a S mají stejná očekávání jako u dvou původních programů.
Dosazení do(III) dává pro9×8

`E[T_III]=221753301564073224388927/2361183241434822606848 · μ`
`        +2628573652287829589991265/4722366482869645213696 · υ`,

tj. přibližně93,916176294μ+556,622121943υ. Obojí je přísně méně
než již exact106,322256350μ+587,464791692υ pro Solution2;
ta byla zase lepší než Solution1. Pořadí tedy platí i v binárním
modelu pro každé kladné μ,υ, se stejným započtením POP u všech.

## Malá reprodukce a konečný rozsah úlohy

Jeden nový běh

`nice -n 15 python3 workstreams/vol1-fasc1/verify_saddle20_candidates.py`

trval0,0056s. Pouze nová metoda byla nezávisle kontrolována na16
binárních2×2 a64 binárních3×2 maticích. Dřívější ověřovače dvou
programů se neopakovaly; binární reference se pouze přečetly z
uloženého JSON. Nové integrály a intervaly jsou přesné racionální
součty, žádný náhodný benchmark, MMIX/assembler ani2^72 enumerace.
Výstup: `results/saddle20-candidates-expectations.json`.

Celé zadání20 má nyní samostatné důkazy pro oba random modely,
oba původní programy i konkrétní obecnou třetí realizaci a jejich
srovnání. **E0132-020 může být argument_recorded.** Chybné knižní
formule zůstávají C0018; zvolené vlastní optimalizace nejsou nové
nálezy a nedokazují globální minimum. Historické trial vzorky a
nedostupný AMM bibliografický důkaz z úlohy18 zůstávají oddělené
výjimky; jejich stav se tím nemění.
