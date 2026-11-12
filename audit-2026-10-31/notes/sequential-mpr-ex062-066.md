# D164–D168 — celé MPR 62–66

7. listopadu 2026. Zadání p18/file38 a odpovědi p379–380/file399–400
byly přímo zobrazeny; autorův PS p18/file24 a p36–37/file42–43
rovněž. Zkontrolováno všech šest vrstev errat a tři TeX zdroje.
E125 eviduje pouze již zapracované úpravy63 z 16.8.2020.

Převzat je úplný FKG argument D163, vztah korelace z D115,
dřívější platný aplikační odstavec62 z D096 a věžová identita
D098 (notes/sequential-mpr-006-008.md, oddíl o dvou historiích).
D100/91 je další již uzavřená aplikace této identity; samotné
64–65 dosud uzavřené nebyly. Níže jsou posouzeny v plném rozsahu.
Žádný starý výpočet se neopakuje a žádný nový se nespouští.

## 62: obě monotónnosti a celý podmíněný dovětek

Množina možných hran je konečná, má m=binom(n,2) prvků.
Bitový vektor hran je bijektivně podmnožina této množiny;
booleovská funkce je tedy množinová funkce s hodnotami 0 nebo 1.

Součinový Bernoulliho zákon z61(d) splňuje hypotézu FKG,
včetně p_j=0 nebo1. D163/61(a,b) proto přímo dává
covar(f,g)≥0 pro dvě neklesající funkce a covar(f,g)≤0
pro neklesající f a nerostoucí g. Totéž platí pro jakýkoli
jiný zákon splňující61; nezávislost zde je postačující
způsob zajištění hypotézy, nikoli další nutný předpoklad.

Pro E⊆E′ je každá cesta v grafu s hranami E také cestou
v grafu s hranami E′. Pokud tedy první graf je souvislý,
je souvislý i druhý: f(E)≤f(E′). Naopak správné obarvení
grafu E′ nejvýše čtyřmi barvami zůstává správné po
odebrání hran, takže g(E)≥g(E′). FKG dává přesně
požadovanou zápornou (tj. nekladnou) korelaci.

Označme A={f=1}, B={g=1}. Indikátory mají
Ef=P(A), Eg=P(B), E(fg)=P(A∩B), a tudíž

    covar(f,g)=P(A∩B)−P(A)P(B).                         (1)

Pro P(B)>0 je dělení (1) kladným P(B) ekvivalentní
P(A|B)≤P(A). Pro P(B)=0 je kovariance0 a dřívější
knižní konvence P(A|B)=P(A) dává rovnost i na druhé
straně. Pro P(B)=1 je oběma stranami rovněž rovnost.
Tím je úplný poslední odstavec odpovědi doložen.

Nejde o nutně striktní korelaci. Pro n≤4 je každý
jednoduchý graf 4-obarvitelný, g=1, takže kovariance0.
Pokud je jen jeden možný graf, obě funkce jsou
konstantní a totéž platí nezávisle na zvolené konvenci
souvislosti prázdného grafu. Žádný algoritmus pro
testování souvislosti či obarvitelnosti se zde nepožaduje.

## 63: nutnost i postačitelnost všech devíti hodnot

Položme r_a=p_{a0}+p_{a1}+p_{a2}. Pro r_a>0 má
podmíněné očekávání na celé události Z₀=a hodnotu

    E(Z₁|Z₀=a)=(p_{a1}+2p_{a2})/r_a.                  (2)

Hodnota b jednotlivého atomu (Z₀=a,Z₁=b) se v (2)
neobjevuje, protože podmiňujeme jen na Z₀.

Pro a=0 rovnost (2)=0 dává p₀₁+2p₀₂=0, tedy
p₀₁=p₀₂=0 z nezápornosti. Pro a=1 dostáváme
p₁₁+2p₁₂=p₁₀+p₁₁+p₁₂, tedy p₁₀=p₁₂.
Pro a=2 platí p₂₁+2p₂₂=2p₂₀+2p₂₁+2p₂₂,
tedy 2p₂₀+p₂₁=0 a p₂₀=p₂₁=0.

Pokud r_a=0, jsou všechny tři členy příslušného
řádku nulové, takže odvozené podmínky platí také;
nikdy se nedělí nulovým r_a. Očekávací rovnost je
rovností náhodných proměnných skoro jistě. Hodnota
zvoleného reprezentanta na nemožném Z₀=a výsledek
nemění, stejně jako v již uzavřeném D098.

Obráceně mají právě všechny přípustné matice tvar

    [ A  0  0 ]
    [ B  C  B ],    A,B,C,D≥0,    A+2B+C+D=1.
    [ 0  0  D ]

Každý nenulový řádek této matice dává v (2) svůj
řádkový index a nulové řádky nemají pravděpodobnost.
To dokazuje postačitelnost i úplnost. Jsou zahrnuty
všechny degenerované zákony a žádné jiné omezení
na devět pravděpodobností není třeba.

### E125 — známé změny

Originální all4f5.pdf, file3 a file10, přímo uvádí
16.8.2020: doplnění slova „nine“ v zadání a celé
náhradní znění odpovědi63. Shodují se s aktuální
4B p18/p380. TeX má odpovídající bloky
\improvepage 4f5.18 a \improvepage 4f5.191.
Saved PS, datovaný11.9.2019, už obsahuje stejný
matematický podíl a stejné podmínky; tato shoda
se nepřepisuje jako neexistující numerický rozpor.
Jde o známou úpravu, žádný nález, kartu ani barvu mapy.

## 64(a): všechny dvojice a nekonečné pokračování

Na třech atomech a,b,c s pravděpodobností1/3 dejme

    a: (Z₀,Z₁,Z₂)=(0,0,−2),
    b: (Z₀,Z₁,Z₂)=(1,0, 2),
    c: (Z₀,Z₁,Z₂)=(1,2, 2).

Pro všechna n≥2 definujme Z_n=Z₂, čímž je opravdu
určena posloupnost splňující otázku „for all n≥0“.

Všechna vlákna prvních dvou dvojic jsou následující:

- Z₀=0: pouze a, E(Z₁|Z₀=0)=0.
- Z₀=1: b,c se stejnými podmíněnými vahami1/2,
  E(Z₁|Z₀=1)=(0+2)/2=1.
- Z₁=0: a,b s vahami1/2, E(Z₂|Z₁=0)=(−2+2)/2=0.
- Z₁=2: pouze c, E(Z₂|Z₁=2)=2.

Pro n≥2 je Z_{n+1}=Z_n, takže požadovaná dvojicová
rovnost platí přímo. Všechny proměnné jsou omezené,
a tedy integrabilní. Plná historie (Z₀,Z₁)=(0,0)
však určuje atom a, a tudíž

    E(Z₂|Z₀=0,Z₁=0)=−2≠0=Z₁(a).

Selhání má pravděpodobnost1/3, není otázkou nulové
verze podmínění. Tento jediný neplatný krok stačí
k vyvrácení martingalové vlastnosti.

## 64(b): tištěné marginální součty i obecná věž

Pro martingale a pevnou historii z₀,…,z_n s kladnou
pravděpodobností vynásobíme podmíněnou rovnost
její pravděpodobností:

    ∑_{z_{n+1}}(z_{n+1}−z_n)
        P(Z₀=z₀,…,Z_{n+1}=z_{n+1})=0.                 (3)

Pro historii s nulovou pravděpodobností jsou
všechny společné pravděpodobnosti0 a (3) platí přímo.
Při pevném z_n sečteme (3) přes z₀,…,z_{n−1}.
Přeskupení je oprávněno, neboť součet absolutních
hodnot přes všechny atomy je nejvýše
E|Z_{n+1}|+E|Z_n|<∞. Vnitřní marginální součet
je právě P(Z_n=z_n,Z_{n+1}=z_{n+1}), takže dostáváme
druhý tištěný řádek. Dělení kladným P(Z_n=z_n)
dává E(Z_{n+1}|Z_n=z_n)=z_n; nulová vlákna jsou
opět nepodstatná pro skoro jistou rovnost.

Stejný argument vyjadřuje věžová identita D098:

    E(Z_{n+1}|Z_n)
      =E(E(Z_{n+1}|Z₀,…,Z_n)|Z_n)
      =E(Z_n|Z_n)=Z_n.

Část(b) je tedy ano, část(a) ne, přesně jako v knize.
Přechod od plné historie k poslednímu stavu je
oprávněný; obrácený směr vyvrací výše uvedený svědek.

## 65: libovolná pevná rostoucí podposloupnost

Označme H_j=(Z₀,…,Z_j). Pro k<n dává D098

    E(Z_{n+1}|H_k)
      =E(E(Z_{n+1}|H_n)|H_k)
      =E(Z_n|H_k).                                    (4)

Základ k=n je přímo E(Z_{n+1}|H_n)=Z_n.
Konečným opakováním (4), vždy se snížením horního
indexu o1, tedy pro r≥k dostaneme E(Z_r|H_k)=Z_k.
Jsou tím zdůvodněny všechny vynechané mezikroky
první tištěné implikace.

Indexy m(0)<m(1)<… jsou pevná nezáporná celá čísla.
Položme Y_j=Z_{m(j)} a K_n=(Y₀,…,Y_n). Každé Y_j
je integrabilní a K_n je funkcí H_{m(n)}.
Výše dokázaný vztah a druhé podmínění proto dávají

    E(Y_{n+1}|K_n)
      =E(E(Z_{m(n+1)}|H_{m(n)})|K_n)
      =E(Z_{m(n)}|K_n)=Y_n.

Poslední rovnost platí, protože Y_n je součástí K_n.
To dokazuje adaptovanost i martingalovou podmínku
vzhledem k vlastní historii podposloupnosti.
Není třeba m(0)=0, pravidelné rozestupy ani omezené
rozdíly m(n+1)−m(n); každá použitá mezera je konečná.
Nevztahujeme tvrzení na libovolné náhodné indexy,
které zadání vůbec nevolí.

## 66: úplnost, existence a každý koeficient

Z₀=0 nutně. Rovnost E(Z₁|Z₀)=0 a Z₁∈{−1,1}
jednoznačně dává P(Z₁=1)=P(Z₁=−1)=1/2.
Pro n≥1 pišme Z_n=nσ_n, σ_n∈{−1,1}, a

    p(σ₁,…,σ_n)=P(Z₁=σ₁,…,Z_n=nσ_n).

Pro historii h=(σ₁,…,σ_n) položme p_+=p(h,1),
p_−=p(h,−1). Marginalizace a martingalová rovnost
dávají přesně dva lineární vztahy

    p_++p_−=p(h),
    (n+1)(p_+−p_−)=nσ_n p(h).                          (5)

Vyřešením této soustavy dostaneme

    p(h,τ)=p(h)(n+1+nσ_nτ)/(2n+2),    τ∈{−1,1}.        (6)

Oba koeficienty v (6) jsou kladné: pro stejná
znaménka (2n+1)/(2n+2), pro opačná 1/(2n+2).
Jejich součet je1. Základní p(±1)=1/2 je kladný,
takže indukcí je kladná každá konečná historie.
Tištěné dělení p(h) je tedy oprávněné, nikoli
předpoklad nevyloučené nulové historie. Vztah (6)
je totožný s tištěným

    p(h,τ)/p(h)=(1+2n[σ_nτ>0])/(2n+2).

Každý konečný společný zákon je vynucen (5) a
jednoznačným základem. Násobením přechodů vychází

    P(Z₁=z₁,…,Z_n=z_n)
      = ∏_{k=1}^{n−1}(1+2k[z_kz_{k+1}>0])/(2^n n!),

kde z_k∈{−k,k}. Jmenovatel je přesně
2·∏_{k=1}^{n−1}(2k+2)=2^n n!, včetně n=1.
Pro n=0 má prázdná historie pravděpodobnost1.

### Existence, ne pouze vynucená formule

Začněme intervalem [0,1) s rovnoměrnou pravděpodobností.
Rozdělme jej na dvě poloviny podle σ₁. Každý interval
historie h dále rozdělme na dva zleva uzavřené a zprava
otevřené podintervaly v poměru p(h,1):p(h,−1) z (6).
Oba podíly jsou kladné a mají součet1. Pro každý
pevný konečný stupeň vzniká disjunktní úplný rozklad
[0,1), zjemňující předchozí stupeň.

Každý bod určuje právě jednu konzistentní nekonečnou
posloupnost znamének. Událost konečné historie je
příslušný interval a má délku p(h), takže odvozené
konečné zákony skutečně společně existují.
Proměnné Z_n=nσ_n jsou měřitelné a |Z_n|=n,
tedy integrabilní; (5) na každém kladném vláknu
dokazuje martingalovou vlastnost. Neopíráme se
pouze o formálně konzistentní seznam čísel.

„Only one solution“ zde označuje jediný společný
zákon všech Z_n; různá pojmenování atomů nebo
realizace na jiném pravděpodobnostním prostoru
nejsou dalšími zákony.

### Osm vytištěných případů pro n=3

Znaménka v lexikografickém pořadí a jejich čitatele:

| σ₁σ₂σ₃ | první faktor | druhý faktor | součin |
|---|---:|---:|---:|
| +++ | 3 | 5 | 15 |
| ++− | 3 | 1 | 3 |
| +−+ | 1 | 1 | 1 |
| +−− | 1 | 5 | 5 |
| −++ | 1 | 5 | 5 |
| −+− | 1 | 1 | 1 |
| −−+ | 3 | 1 | 3 |
| −−− | 3 | 5 | 15 |

Společný jmenovatel je 2³·3!=48 a součet čitatelů48.
Tabulka přesně odpovídá pořadí
123,12(−3),1(−2)3,…,(−1)(−2)(−3) v původní sazbě.
Není k tomu potřeba numerický běh.

## Rozsah checkpointu

Celé MPR62–66 a všechny jejich tištěné dodatky jsou reviewed.
Bez nového nálezu, kandidáta, bibliografické výjimky i běhu.
E125 je pouze známá zapracovaná úprava. File399 je nyní
celý reviewed s dřívější výjimkou forward§7.6.
File38 zůstává partial pro67–69 a file400 pro67–68.
Dřívější izolované důkazy ani censy nebyly nahrazeny.

