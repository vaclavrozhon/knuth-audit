# Úloha1.3.2′–20: přesná očekávání obou programů pro binární matice

Vstup: všech2^(mn) binárních m×n matic je stejně pravděpodobných,
tj. jednotlivé bity jsou nezávislé a rovnoměrné. Pro konkrétní
vytištěný kód m=9,n=8. Všechny stavy, signed bezpečnost, shody,
ukončení a návraty byly úplně dokázány v recovery-pages-054-110-112.md.
Přesné bodové náklady jsou z C0018 a distinct-recovery poznámky;
níže se jejich předpoklad různosti nepoužije: oba obecné profily
výslovně platí i pro shody. Žádný výsledek není odhad z náhodného
vzorku a prostor2^72 matic se neprochází.

## Společný stop stav a označení

Přečíslujme řádky v pořadí scanů jako r=1..m, tj. ve skutečné
matici od původního řádku9 k1. Sloupce se při row-scanu procházejí
zprava doleva; Solution1 pak kandidátní seznam obrátí a zkouší
sloupce zleva doprava. Rozdělení náhodných bitů je invariantní
vůči oběma těmto pevným přečíslováním.

Nechť 𝒵 znamená existenci nulového sloupce a 𝒩 jeho nepřítomnost.
Položme

`q=2^−m`, `b=1−q`, `c=1−2^−n`,
`a=P(𝒵)=1−b^n`, `p₁=1−c^m`,
`w₀=1/2−q`, `w₁=1/2`, `G=Σ(r=0..m−1)c^r`.

Na 𝒵 oba programy najdou sedlo0 už v prvním řádku: každá buňka
nulového sloupce je jeho minimum. Na 𝒩 je min_j C_j=1; řádek
se sedlem musí být celý jedničkový a oba programy skončí u prvního
takového řádku, nebo navštíví všech m řádků. Jedničkový řádek sám
zaručuje 𝒩. Proto R a S (počet navštívených řádků a indikátor
úspěchu) mají u obou programů stejnou distribuci.

Pro r-tý řádek na 𝒩 musí všechny předchozí řádky nebýt celé1.
Inkluze–exkluze dává

`P(𝒩 a dosažen řádek r)=b^n+c^(r−1)−1`.

První člen je P(𝒩). Každá neprázdná vybraná množina předchozích
jedničkových řádků zaručuje 𝒩 a má pravděpodobnost2^(−n|L|);
jejich znaménkový součet je c^(r−1)−1. Nemícháme nezávislost
řádkových a sloupcových událostí. Tedy přesně

`E[R]=a+Σ(r=1..m)[b^n+c^(r−1)−1]`,
`E[S]=a+p₁=2−b^n−c^m`.                              (R,S)

Druhý vzorec souhlasí s nezávislým důkazem úlohy19.

## Solution2: všechna maticová a hlavičková čtení

K je počet načtených maticových prvků Phase2, H počet navštívených
hodnot rovných z. Na 𝒵 je R=1,S=1,K=n,z=0 a H je počet nul
v prvním řádku. Pro daný sloupec platí

`P(první bit0 a 𝒵)=1/2−w₀b^(n−1)`:

odečteme případ, kdy daný sloupec je nenulový s prvním bitem0
(pravděpodobnost w₀) a všechny ostatní sloupce jsou nenulové.
Proto E[H;𝒵]=n/2−nw₀b^(n−1), E[K;𝒵]=na.

Na 𝒩 je z=1 a řádkový scan čte až do první0 nebo do konce.
Pravděpodobnost, že řádek r byl dosažen a jeho prvních k scan-bitů
je1, při současném 𝒩, je

`Q(r,k)=2^−k[b^(n−k)+c^(r−1)−1]`, 0≤k≤n.          (Q)

Bez podmínky předchozích řádků má prvních k sloupců díky zadané1
už nenulové maximum; zbývajících n−k sloupců musí být nenulových.
To dává2^−k b^(n−k). Inkluze–exkluze přes předchozí jedničkové
řádky přidá2^−k(c^(r−1)−1), protože jejich bity jsou nezávislé
na k bitech současného řádku. To dokazuje celý vzorec(Q).

K čte další prvek po každém prefixu délky0..n−1. H se zvýší,
jen když další přečtený bit je1, tj. prefix má délku1..n. Proto

`E[K]=na+Σ(r=1..m)Σ(k=0..n−1)Q(r,k)`,
`E[H]=n/2−nw₀b^(n−1)+Σ(r=1..m)Σ(k=1..n)Q(r,k)`.   (K,H)

Přesný profil se všemi větvemi je

`T_II=[(m+1)n+K+H] μ`
`    +[5mn+4n+11+9K−2R+5H+4S] υ`.

Linearita spolu s(R,S),(K,H) tedy uzavírá celé očekávání programu.
Korelaci čítačů nepotřebujeme a nejsou zanedbány předčasné návraty.

## Solution1: uložení řádkových minim

A je celkový počet STB v RowMin, B počet přísných snížení minima
po prvním prvku řádku. Pro jeden binární řádek platí:

* A_row = počet všech nul + délka počátečního úseku jedniček ve
  směru scanu. Dokud se neobjeví0, zapisuje se každá1; potom se
  zapisují právě0. Platí i pro samé0 a samé1.
* B_row =1 právě když první scan-bit je1 a některý další bit je0;
  jinak0. Přísný pokles1→0 může nastat nejvýše jednou.

Pro rovnoměrný řádek jsou tedy

`g_A=n/2+Σ(k=1..n)2^−k`, `g_B=1/2−2^−n`.

Při současné události𝒩 mají jednotlivé sloupce nezávislé
nenormalizované váhy w₀ pro0 a w₁ pro1; součet vah je b.
Odtud pro tentýž řádek dostáváme vážená očekávání

`g_A,𝒩=nw₀b^(n−1)+Σ(k=1..n)w₁^k b^(n−k)`,
`g_B,𝒩=w₁b^(n−1)−w₁^n`.

Pro libovolnou funkci g jednoho řádku a r≥2 je její příspěvek
po započtení dosažitelnosti

`E[g(row r);dosažen]=g_𝒩+(c^(r−1)−1)g`.

Důkaz je stejná inkluze–exkluze; při alespoň jednom předchozím
jedničkovém řádku je𝒩 automatické a g současného řádku je na
zadaných předchozích bitech nezávislé. První řádek je vždy dosažen
a dává g. Součtem proto

`E[A]=(m−1)g_A,𝒩+[G−(m−1)]g_A`,
`E[B]=(m−1)g_B,𝒩+[G−(m−1)]g_B`.                    (A,B)

Tyto vzorce zahrnují i přepsané starší kandidátní seznamy;
nezaměňují konečnou velikost seznamu s počtem jeho zápisů.

## Solution1: počet kandidátních sloupců C

Na𝒩 každý neúspěšný navštívený řádek vyzkouší všechny své0,
protože žádný sloupec není celý0. Úspěšný jedničkový řádek má
0 nul a vyzkouší právě jeden sloupec. S row funkcí počet nul,
jejíž očekávání je n/2 a vážené očekávání nw₀b^(n−1), dostáváme

`E[C;𝒩]=mnw₀b^(n−1)+(G−m)n/2+p₁`.                 (C𝒩)

Na𝒵 se prochází pouze první řádek. Sloupce seznamu jsou v rostoucím
pořadí indexu. První celý nulový sloupec je úspěšný; před ním se
vyzkoušejí právě nenulové sloupce, které mají první scan-řádek0.
Definujme konečný součet

`L=Σ(j=1..n)b^(j−1)(1−b^(n−j))`.

Člen udává pravděpodobnost, že před daným sloupcem žádný nulový
není, ale za ním alespoň jeden je. Připočítáme úspěšný sloupec:

`E[C;𝒵]=a+w₀L`, a tedy `E[C]=E[C;𝒩]+E[C;𝒵]`.     (C𝒵)

## Solution1: všechna sloupcová čtení D

V nenulovém sloupci označme F první řádek scanu, který obsahuje1.
P(F=f)=2^−f,1≤f≤m. Kandidát0 z jiného řádku se odmítne přesně
po F čteních; kandidát1 nebo nulový sloupec vyžaduje všech m čtení.

Na𝒵 mají neúspěšné kandidátní sloupce první bit0, tedy F≥2.
Události před/za sloupcem jsou na jeho bitech nezávislé. Proto

`E[D;𝒵]=ma + L Σ(f=2..m) f2^−f`.                   (D𝒵)

Na𝒩 přispěje úspěšný jedničkový řádek cenou m, celkem mp₁.
Pro ostatní kandidáty zafixujme sloupec j a jeho F=f.

Je-li zkoušený řádek r<f, jeho bit i všechny předchozí bity
sloupce j jsou0. Žádný předchozí řádek nemůže být celý1, takže
row r je dosažen, pokud zbývajících n−1 sloupců je nenulových.
Tento faktor je b^(n−1); takových r je f−1.

Je-li r=f, bit je1 a tento řádek nedává nulového kandidáta.
Je-li r>f, bit v row r musí být0, s pravděpodobností1/2.
Předchozí možné jedničkové řádky jsou f..r−1; řádky před f
mají v tomto sloupci0. Inkluze–exkluze přes jedničkové řádky
dává pro zbývající podmínku přesně

`b^(n−1)+(1−2^(−(n−1)))c^(r−f−1)−1`.

Prázdná vybraná množina požaduje nenulovost ostatních sloupců,
tedy b^(n−1). Pro neprázdnou množinu je tato nenulovost automatická.
Řádek f má ve sloupci j již danou1, takže jeho další constraint
má pravděpodobnost2^(−(n−1)); řádky f+1..r−1 potřebují všech n
jedniček a mají faktor2^−n. Jejich znaménkový součin je
(1−2^(−(n−1)))c^(r−f−1), z něhož odečteme prázdnou množinu.
To vyčerpává všechna r<f, r=f, r>f i meze f=1,m.

Po násobení cenou f, pravděpodobností2^−f a počtem n sloupců:

`E[D;𝒩]=mp₁ + n Σ(f=1..m) f2^−f ·`
` { (f−1)b^(n−1)`
`   +(1/2)Σ(r=f+1..m)[b^(n−1)+(1−2^(−(n−1)))c^(r−f−1)−1] }`. (D𝒩)

Nakonec E[D]=E[D;𝒵]+E[D;𝒩]. Neprovádí se chybná záměna
E[F·početkandidátů] za součin jejich očekávání: jejich závislost
je právě důvodem podmínění na F a uvedeného rozdělení r případů.

## Dosazení do přesných instrukčních cen

Pro Solution1 platí úplný profil

`T_I=(nR+A+C+D) μ`
`   +[(6n−6)R+9A−2B+2C+7D+3S+6] υ`.

Všechny očekávané čítače na pravé straně jsou nyní dány konečnými
racionálními součty. Jediný krátký běh

`nice -n 15 python3 workstreams/vol1-fasc1/verify_saddle20_expectations.py`

je přesně vyčíslil pro9×8. Současně nezávisle porovnal všechny
čítače s přímým provedením abstraktních algoritmů na všech16
binárních2×2 a64 binárních2×3 maticích. To je pouze omezená
kontrola80 malých případů; obecný důkaz je výše. Nespouštěl se
MMIX, assembler, starý benchmark ani9×8 enumerace. Celý nový
výpočet trval přibližně0,005s, výsledek je
`results/saddle20-binary-expectations.json`.

| Program | Přesné očekávané mems | Přesné očekávané υ |
|---|---:|---:|
| Solution1 | 1064444590222388256940947 / 4722366482869645213696 | 403103103707592028253789 / 295147905179352825856 |
| Solution2 | 251046329884157605558779 / 2361183241434822606848 | 1387112021075431772792029 / 2361183241434822606848 |

Přibližně jde o225,404910μ+1365,766440υ versus
106,322256μ+587,464792υ. Přesný rozdíl má kladné oba čitatele:

`562351930454073045823389 / 4722366482869645213696 · μ`
`+1837712808585304453238283 / 2361183241434822606848 · υ`.

Proto je pro rovnoměrnou binární9×8 matici **Solution2 rychlejší
v očekávání pro každé μ,υ>0**. Toto je exact očekávání pod daným
rozdělením, nikoli tvrzení, že je rychlejší na každé matici:
u all-zero je první řešení pro některé poměry μ/υ lepší, jak
ukazují již samostatně dokázané pevné profily.

Tím jsou pro dva vytištěné programy uzavřeny oba požadované
náhodné modely (distinct v samostatné poznámce). Třetí naznačená
metoda stále potřebuje konkrétní realizaci a vlastní srovnatelné
náklady; úloha20 proto nadále není označena jako úplně uzavřená.
Nevzniká z toho další numerický knižní nález: binary čísla kniha
neuvádí a její trial průměry používají jiné, pětiúrovňové rozdělení.


Konečné doplnění20: exercises-1.3.2-020-third-recovery.md nyní dává úplný obecný MMIX kandidátní program, všechny větve a náklady, exact binary očekávání a rigorózní distinct9×8 srovnání. Třetí metoda je tím konkrétně realizována; v obou modelech má menší oba očekávané koeficienty než Solution2, a ta než Solution1. Úloha20 je argument_recorded; dřívější third-variant partial je vyřešeno. Globální optimum ani historické trial běhy se netvrdí.
