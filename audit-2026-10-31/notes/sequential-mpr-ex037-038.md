# D139–D140 — celé MPR37–38

7. listopadu 2026. Původní zadání p15/file35 a odpovědi
p376/file396 jsou přímo zobrazeny, stejně jako autorův
Pre-Fascicle5A p15/file21 a p33/file39. Pro odkaz38 byla
zobrazena původní 4A p416, rovnice(4), a p418, odstavec
definující Bellova čísla. Ostatní obsah těchto stran 4A
se tím nepřebírá jako zkontrolovaný.

## D139, 37: všechny podmíněné počty

Nechť n≥1 a 1≤k≤n. Každý skutečně možný prefix
(x₁,…,xₖ₋₁) tvoří různé prvky množiny {1,…,n}.
Má (n−k+1)! pokračování. Pro každou dosud nepoužitou
hodnotu v má rozšířený prefix s xₖ=v přesně (n−k)!
pokračování; původní permutace mají stejnou kladnou váhu.
Podmíněná pravděpodobnost každé takové hodnoty je proto
1/(n+1−k). Použité hodnoty mají pravděpodobnost0.

Položíme-li C=n(n+1)/2 a Sⱼ=∑ᵢ₌₁ʲXᵢ, dostaneme

    E(Xₖ | X₁,…,Xₖ₋₁)=(C−Sₖ₋₁)/(n+1−k).

To dokládá jak tištěný součet zbývajících hodnot, tak
jeho zkrácení pomocí 1+⋯+n=C. Pro k=1 je prefix prázdný,
S₀=0 a výsledek (n+1)/2. Pro k=n zbývá jediná hodnota,
jmenovatel je1 a podmínění ji určuje. Každý prefix, který
nastane na tomto konečném prostoru, má kladnou hmotnost;
žádný použítý podíl nedělí nulou. Pro n=0 není žádné Xₖ
ani úloha o jeho podmínění; tištěný martingal je určen
pro kladné n, nikoli pomocí neexistujícího Z₋₁.

## 37: všechny koeficienty a martingal

Tištěný součet lze bez vynechaných členů zapsat

    Zⱼ=∑ᵢ₌₁ʲ⁺¹(n+j−2i+2)Xᵢ−(j+1)C,  0≤j<n.

První koeficient je n+j, druhý n+j−2 a poslední n−j,
což souhlasí s originálem. Pro j≥n je Zⱼ=Zₙ₋₁.
Definujme Fⱼ=σ(X₁,…,X_min(j+1,n)). To je rostoucí
historie a Zⱼ je vůči ní měřitelný. Všechny Zⱼ jsou
integrabilní: před ustálením jde o konečný součet
omezených proměnných, po něm o tutéž konečnou proměnnou.

Pro 0≤j≤n−2 se při přechodu j→j+1 každý z již přítomných
koeficientů zvětší o1, přibude (n−j−1)Xⱼ₊₂ a odečte C:

    Zⱼ₊₁−Zⱼ=Sⱼ₊₁+(n−j−1)Xⱼ₊₂−C.

Předchozí vzorec s k=j+2 dává

    E(Xⱼ₊₂ | Fⱼ)=(C−Sⱼ₊₁)/(n−j−1).

Jmenovatel je v celém tomto rozsahu kladný. Po dosazení
má přírůstek podmíněné očekávání0, a tudíž
E(Zⱼ₊₁|Fⱼ)=Zⱼ. Pro j=n−2 je přírůstek dokonce bodově0,
protože poslední hodnota permutace už je známá. Pro j≥n−1
je přírůstek0 z definice. Při n=1 je Z₀=X₁−1=0 a celá
posloupnost je konstantní; není třeba použít žádný
neexistující přechod z uvedeného rozsahu.

Také E Z₀=n·(n+1)/2−C=0. S vlastní historií
Gⱼ=σ(Z₀,…,Zⱼ)⊆Fⱼ jde rovněž o martingal: věžová
identita dává E(Zⱼ₊₁|Gⱼ)=E(Zⱼ|Gⱼ)=Zⱼ.
Tím je ověřen přesný tištěný dovětek. Netvrdíme
adaptovanost k o jednu proměnnou kratší historii
σ(X₁,…,Xⱼ), kterou kniha pro tento dovětek neurčuje.

## D140, 38: význam řetězců, t a Bellových čísel

Rovnice 7.2.1.5–(4) ve 4A výslovně říká, že řetězec
a₁…aₙ má a₁=0 a 0≤aⱼ₊₁≤1+max(a₁,…,aⱼ).
Stejné hodnoty označují stejný blok rozkladu {1,…,n};
nový blok dostane nejmenší dosud nepoužité číslo. Proto
mezi použitými čísly nejsou mezery. Naopak seřazením
bloků podle prvního výskytu získáme právě jeden takový
řetězec pro každý rozklad. To je bijekce, nikoli pouze
shoda počtů. Bellovo číslo varpiₙ je počet těchto rozkladů;
varpi₀=1 odpovídá prázdnému rozkladu.

Pro m,r≥0 je tₘ,ᵣ počet řetězců délky m+r s prefixem
01…(m−1). Prvních m prvků pak patří do různých bloků,
a naopak tato podmínka v kanonickém řetězci nutí právě
uvedený prefix. Tím je ověřen tištěný ekvivalentní popis.

Z r dalších prvků vyberme k, které nebudou patřit do
žádného z m starých bloků. Volba má binom(r,k) možností,
jejich rozklad do nových bloků varpiₖ možností, a každý
z ostatních r−k prvků lze nezávisle přiřadit k jednomu
z m označených starých bloků. Každý konečný rozklad
má jednoznačně právě tento rozklad na tři volby. Proto

    tₘ,ᵣ=∑ₖ₌₀ʳ binom(r,k) varpiₖ m^(r−k).

Pro m=0 se bere 0⁰=1, počet jediné funkce z prázdné
množiny do prázdné množiny; všechny jiné mocniny0 jsou0.
Tedy t₀,ᵣ=varpiᵣ. Pro r=0 vyjde tₘ,₀=1 pro každé m,
včetně m=0. Všechny tyto počty jsou kladné.

## 38: celý exponenciální generující vzorec

Koeficient r!·[zʳ](eᶻ−1)^ℓ/ℓ! počítá rozklady r označených
prvků do ℓ neprázdných bloků: součin nejprve počítá
uspořádané bloky a dělení ℓ! odstraňuje jejich pořadí.
Pro každý stupeň r přispívá jen konečně mnoho ℓ≤r,
takže jde o platnou identitu formálních mocninných řad:

    ∑ᵣ≥₀ varpiᵣ zʳ/r! = ∑ℓ≥₀ (eᶻ−1)^ℓ/ℓ!
                         = exp(eᶻ−1).

Násobením s exp(mz)=∑ₛ≥₀mˢzˢ/s! dostaneme přesně
předchozí binomickou konvoluci, a tedy

    ∑ᵣ≥₀tₘ,ᵣ zʳ/r! = exp(eᶻ−1+mz).

Každý koeficient i faktor r! je tak doložen. Není nutné
předpokládat analytickou konvergenci pro výpočet počtů;
pravá strana je navíc celá funkce.

## 38: každý prefix, podmíněný podíl a očekávání

Pro 2≤k≤n fixujme možný prefix X₁,…,Xₖ₋₁ a položme
M=1+max(X₁,…,Xₖ₋₁). Jde přesně o počet dosavadních bloků.
Počet pokračování závisí pouze na M a počtu zbývajících
pozic, nikoli na velikostech starých bloků: zachováme
jednoho označeného zástupce každého starého bloku a
zapomeneme ostatní prefixové prvky. Každé rozšíření
těchto zástupců jednoznačně obnoví rozšíření původního
prefixu. Prefix má proto t_M,n+1−k pokračování.

Nová hodnota může být pouze j∈{0,…,M}. Je-li j<M,
připojí se do určeného starého bloku a zbude
t_M,n−k pokračování. Je-li j=M, vytvoří nový blok a
zbude t_M+1,n−k pokračování. Původní řetězce jsou
stejně pravděpodobné, takže pro r=n−k platí

    P(Xₖ=j | X₁,…,Xₖ₋₁)=t_M,r/t_M,r+1,      0≤j<M,
    P(Xₖ=M | X₁,…,Xₖ₋₁)=t_M+1,r/t_M,r+1.

To jsou podmíněné pravděpodobnosti; autor v tomto
odstavci po fixaci prefixu zkracuje jejich zápis jako
Pr(Xₖ=j). Není důvod číst je jako nepodmíněné marginály.
Rozdělení podle nové hodnoty je disjunktní a úplné,
a dává také rekurenci

    t_M,r+1 = M t_M,r+t_M+1,r.

Podíly tedy mají kladný jmenovatel a sečtou se na1.
Součet starých označení je ∑ⱼ₌₀ᴹ⁻¹j=M(M−1)/2=binom(M,2).
Vynásobením všech podílů jejich hodnotami získáme

    E(Xₖ | X₁,…,Xₖ₋₁)
      =(binom(M,2)t_M,n−k+M t_M+1,n−k)/t_M,n+1−k.

Pro k=n je r=0, všech M+1 možností má váhu1/(M+1)
a výsledek je M/2. Pro k=1 je X₁=0 deterministicky,
takže odpověď je0. Není nutné přiřazovat hodnotu max
prázdné množiny. Chceme-li jednotný počítací vzorec,
určíme M=0 jako počet bloků prázdného prefixu; pak
t₀,n=t₁,n−1=varpiₙ, nový symbol0 má pravděpodobnost1
a čitatel očekávání je0. Rovnost počtů plyne i přímo
z toho, že každý neprázdný RGS začíná0. N=1 je tím
pokryto; n=0 nemá žádné podmíněné Xₖ.

## F163: jediný chybný index v závěru38

V posledním očekávání odpovědi je v originálu PDF i PS
vytištěno E(Xₖ|X₀,…,Xₖ₋₁). X₀ však není v zadání,
v právě použité definici M ani v definici RGS ve 4A.
Začátek seznamu má být X₁. Nejde o změnu výše odvozené
pravé strany; jde o zjevný lokální přebytečný index.

Přesný význam chyby při pokusu doplnit libovolné X₀:
pro n=2 jsou řetězce00 a01, každý s váhou1/2. Pro k=2
je M=1, t₁,₀=t₂,₀=1, t₁,₁=2, takže pravá strana je1/2.
Pokud by X₀=X₂, pak E(X₂|X₀,X₁)=X₂, nikoli1/2,
na obou kladných atomech. Samotné zadané očekávání
E(X₂|X₁)=1/2 je správné. Kniha neurčuje dodatečné
konstantní X₀, které by bylo neškodné.

Jde o F163 low, bez vlivu na hlavní výsledek. Všech6
lokálních vrstev errat a3TeX neobsahuje použitelnou
opravu; přesné hashe a kontexty jsou v přiloženém JSON.
Matematický důkaz obou úloh je úplný; file396 má celý
obsah31–38 posouzený, s touto lokální opravou. File35
zůstává partial pro39–40. Žádná bibliografická výjimka
v novém bloku, žádný numerický běh ani restart.
