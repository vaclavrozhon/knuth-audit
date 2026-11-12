# 103(f), obecný dovětek: konzistentní minulost a rozsah zrychlení

Tento vlastní důkaz doplňuje celý dovětek odpovědi103 na p385.
Hlavní konkrétní algoritmus a všechny jeho náklady jsou v
`sequential-mpr-ex103-104.md`. Následující výsledek se týká
konečného uspořádaného prostoru S s nejmenším a největším prvkem
⊥,⊤ a IID náhodných neklesajících aktualizací f_1,f_2,…;
nepředpokládá, že libovolný monotónní řetězec musí koaleskovat.

Pro Φ_T=f_1∘…∘f_T monotónnost dává
Φ_T(⊥)≤Φ_T(x)≤Φ_T(⊤) pro každý x. Shoda krajních hodnot je
proto ekvivalentní konstantnosti celé funkce. Je-li Φ_N konstantní,
pak pro T≥N je Φ_T=Φ_N∘f_(N+1)∘…∘f_T stejná konstanta.
Předpokládáme N<∞ skoro jistě; tento předpoklad níže výslovně
dokazujeme v konkrétních rodinách.

Nechť P je jednorázová přechodová matice. Existenci stacionárního
zákona π lze v konečném prostoru doložit bez jiné věty: průměry
ν_m=(ν+νP+…+νP^(m−1))/m mají konvergentní podposloupnost
v kompaktním simplexu a ν_mP−ν_m=(νP^m−ν)/m→0. Její limita
π tedy splňuje πP=π. Zvolme I s rozdělením π nezávislé na všech
f_t. Pro každý pevný T má Φ_T(I) opět rozdělení π, protože
jde o T nezávislých přechodů s maticí P v obráceném pořadí.
Na události N≤T je tato hodnota rovna výsledné konstantě Z.
Pro každou množinu A je proto
|P(Z∈A)−π(A)|≤P(N>T)→0. Výstup má přesně zákon π; argument
funguje pro každý stacionární zákon, a proto z koalescence plyne
i jeho jednoznačnost. To je potřebný obecný důkaz správnosti.

Pro analogii původních tří stavů na{0,…,d−1},d≥2, s férovými
oříznutými kroky±1 je P symetrická a řádkově stochastická,
takže rovnoměrný zákon je stacionární. Každý blok d−1 nulových
bitů složí konstantní funkci0. Takový blok má kladnou
pravděpodobnost2^(−(d−1)); nezávislé disjunktní bloky dávají
P(N>k(d−1))≤(1−2^(−(d−1)))^k. Tím je doloženo skoro jisté
ukončení i konečná střední doba, bez simulace nebo rychlé směšovací
hypotézy. Jednoprvkový prostor lze vrátit ihned.

Další konkrétní rodinu dávají ideály libovolného konečného posetu
V,|V|=m≥1, uspořádané inkluzí. Zvolíme rovnoměrně v∈V a férový
bit. Pro bit1 vložíme v, pokud jsou všechny jeho přísné předchůdce
už v ideálu; pro bit0 odstraníme v, pokud v ideálu není jeho
přísný následník. Jinak stav ponecháme. Všechny stavy zůstávají
ideály. Je-li I⊆J, vložení v do I je povoleno i v J; odstranění
v z J je povoleno i v I. Proto obě aktualizace zachovávají inkluzi.
Každý netriviální přechod I↔I∪{v} má v obou směrech pravděpodobnost
1/(2m), takže P je symetrická a rovnoměrný zákon je stacionární.

Fixujme obrácené topologické pořadí všech m prvků. Blok, který
postupně volí tyto prvky a vždy bit0, odstraní každý počáteční
ideál: při pokusu o odstranění v jsou všichni jeho následníci
již odstraněni. Tento blok má pravděpodobnost(2m)^−m>0.
Disjunktní IID bloky tedy opět zaručují konečné N skoro jistě
i v průměru. Výstup je rovnoměrný ideál. Zobrazení I↦max(I)
je bijekce na antichainy: zpětně bereme dolní uzávěr; každému
prvku neprázdného konečného ideálu dominuje jeho maximální prvek.
Takto vzniká i přesně rovnoměrný antichain. Tyto celé rodiny
podporují tvrzení o generování různých kombinatorických objektů.

Srovnání cen v knize je s doslovným postupem(b), který při každém
kroku aktualizuje tabulku všech d=|S| hodnot. To stojí dN
tabulkových přiřazení a O(d) stavů paměti. Postup(f) při stejných
náhodných mapách používá pouze dva krajní stavy, po dyadických
opakováních méně než8N jednotlivých vyhodnocení aktualizace
(viz hlavní poznámka). Pro aktualizaci dostupnou v konstantní
jednotkové ceně je poměr prací menší než8/d. Při velkém d je
tedy tvrzené zrychlení vůči plné tabulce doloženo. Nejde o
nezávislou mez rychlosti směšování, univerzální benchmark všech
reprezentací stavů ani záruku, že každá monotónní mapa koaleskuje.
Paměť pro konzistentní bity/aktualizace zůstává zvláštní náklad;
v cache realizaci je O(N), generátor může místo toho reprodukovat
jednotlivé dyadické bloky ze zachovaných stavů.

Bibliografie je ověřena v rozsahu zdejší citace. Primární
[článek Proppa a Wilsona, autorská verze16.7.1996](https://www.stat.berkeley.edu/~aldous/206-RWG/RWGpapers/propp_wilson.pdf)
má na p7–8 monotónní krajní stavy, zdvojnásobování a zachování
náhodných aktualizací ukládáním či resetem na hranicích bloků.
Původní PDF p1,7,8 bylo přímo zobrazeno. Abstrakt uvádí další
aplikace ve statistické mechanice a konečných distributivních
svazech. [Vydavatelský záznam](https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291098-2418%28199608/09%299%3A1/2%3C223%3A%3AAID-RSA14%3E3.0.CO%3B2-O)
potvrzuje oba autory, Random Structures & Algorithms9(1996),223–252.
Netvrdí se audit dalších vět či fyzikálních modelů celého článku;
zdejší obecný algoritmus a konkrétní aplikace mají úplné vlastní
argumenty výše. Bibliografická výjimka pro tuto citaci není potřeba.
