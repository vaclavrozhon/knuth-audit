# D188 — úplný důkaz dosažení suprema v MPR88

7. listopadu 2026. Tato poznámka doplňuje přesné
první zásahy a atomový výpočet v
sequential-mpr-ex087-088.md. Dokazuje právě
dovětek pro původní urnu(1,1), ne všechny
zobecněné modely citovaného článku.

## Explicitní prostor se správným urnovým zákonem

Na standardním produktu vezměme U rovnoměrné
na(0,1) a nezávislé rovnoměrné V₁,V₂,…
na(0,1). Položme X_i=[V_i≤U].
Pro každé pevné u mají X_i nezávislý
Bernoulliho zákon s parametrem u. Směšování
přes u je integrál na produktu; nejde
o podíl pravděpodobností nulové události U=u.

Pravděpodobnost libovolného konečného slova
s a jedničkami a b nulami je

    ∫₀¹ u^a(1−u)^b du=a!b!/(a+b+1)!.

Pro b=0 je integrál1/(a+1). Pro b>0
integrace per partes dává
I(a,b)=b I(a+1,b−1)/(a+1); oba krajní
členy jsou0. Indukce v b tedy dokazuje
uvedený zlomek včetně všech krajů a,b≥0.

To je přesně již doložená pravděpodobnost
každého urnového slova D173. Válce konečných
slov tvoří generující π-systém na{0,1}^N,
a pravděpodobnostní míry, které se na něm
shodují, jsou stejné (uzavření přes monotonní
třídu). Proto má tento produktový model
celý původní urnový zákon, včetně všech
měřitelných událostí definovaných spočetně
mnoha prefixy. Red ratio je

    Z_n=(1+X₁+⋯+X_n)/(n+2), Z₀=1/2.

## Konvergence pro každý pevný parametr

Fixujme0<u<1 a označme
W_n=X₁+⋯+X_n−nu, W₀=0.
Přírůstky X_i−u jsou nezávislé, mají
průměr0 a deterministické meze−u a1−u.
Platná deterministická verze Hoeffdingovy
nerovnosti, úplně dokázaná v D100
(notes/sequential-mpr-009-010.md), má
součet čtverců šířek právě n. Pro ε>0 tedy

    P_u(|W_n|≥nε)≤2 exp(−2nε²).

Dolní ocas používá tytéž podmínky pro
−(X_i−u). Nepoužívá se chybná verze
s náhodnou šířkou F160. Pro každé N je
pravděpodobnost některého porušení s n≥N
nejvýšeΣ_{n≥N}2exp(−2nε²), což je ocas
konvergentní geometrické řady. Tento ocas
jde k0, a proto téměř jistě nastane jen
konečně mnoho porušení. Přes spočetně
mnoho ε=1,1/2,1/3,… dostaneme

    W_n/n→0 skoro jistě.

Tudíž Z_n−u=(W_n+1−2u)/(n+2)→0.
Tento krok má vlastní argument; nepřebírá
neověřenou silnou zákonitost velkých čísel.

## Neomezené kladné výkyvy bez LIL

Pro libovolná a,b>0 nechť τ je první čas,
kdy W_n≥a nebo W_n≤−b. Jde o zastavovací
čas vůči dosavadním X. Zvolme celé L tak,
že L(1−u)>a+b. Z každého vnitřního stavu
L po sobě jdoucích jedniček způsobí
výstup přes horní hranici. Nezávislost
disjunktních bloků a pravděpodobnost u^L
tak dávají

    P_u(τ>kL)≤(1−u^L)^k.

Zvláště τ<∞ skoro jistě. Nerovnost platí
i podmíněně na libovolný dosavadní vnitřní
stav, takže argument nevyžaduje nezávislost
poloh procesu.

Každý přírůstek leží v[−u,1−u]⊂[−1,1].
Proto je W_{τ∧n} vždy v[−b−1,a+1].
Pro každý konečný n má zastavený martingale
očekávání0 podle již dokázaného omezeného
zastavení D099; integrabilita je dána
uvedenou deterministickou mezí. Dominovaná
konvergence při n→∞ dává E_u W_τ=0.
Není zde použita neomezená zastavovací
věta bez ověření podmínek.

Označme q=P_u(W_τ≥a). Na horním výstupu
W_τ≤a+1 a na dolním W_τ≤−b. Tedy

    0=E_u W_τ≤q(a+1)+(1−q)(−b),

odkud q≥b/(a+b+1). Pravděpodobnost, že
W někdy dosáhne a, je nejméně q pro
každé b. Necháme-li b→∞ přes celá čísla,
dostáváme tuto pravděpodobnost rovnou1.
Průnikem přes a=1,2,3,… plyne

    sup_n W_n=+∞ skoro jistě.

Každý konečný prefix má konečné maximum,
takže také limsup_n W_n=+∞. Celý použitý
výkyvový fakt má elementární důkaz.
Nepřebíráme zákon iterovaného logaritmu,
kterým odpovídající krok zdůvodňuje
citovaný článek.

## Konečné dosažení a všechny důsledky

Pro pevné u probíhají oba předchozí závěry
současně na množině pravděpodobnosti1.
Existuje tedy j s W_j>2u−1, a tudíž Z_j>u.
Pišme δ=Z_j−u>0. Konvergence Z_n→u dává
konečné N tak, že pro všechna n≥N je
Z_n<u+δ/2<Z_j. Supremum celé posloupnosti
je proto maximum konečného prefixu
Z₀,…,Z_{N−1}; je dosaženo.

Tvrzení platí pro každý0<u<1. Fubiniho
věta přes uniformní U tedy dává jeho
pravděpodobnost1 i ve směsi a tím v původní
urně. Události konvergence, neomezenosti
a dosažení jsou vyjádřitelné spočetnými
průniky/sjednoceními prefixových nerovností,
takže použitá integrace je oprávněná.
Parametry u=0,1 mají ve směsi míru0;
zejména u=1 by mělo supremum1 nedosažené,
což nepůsobí žádnou výjimku kladné míry.

Každý Z_n je racionální podíl celých
kladných počtů. Proto P(S∈Q)=1.
Nechť T je nejmenší index, kde Z_T=S;
na nulové výjimečné množině lze zvolit
T=∞. Je to měřitelná veličina, protože

    {T≤m}={Z_n≤max_{0≤j≤m}Z_j pro všechna n>m}.

Události napravo jsou spočetné průniky.
T<∞ skoro jistě, a tedy P(T≤m)→1,
což dokazuje tištěné asymptotické tvrzení
o dosažení maxima během n kroků.
T není potřeba prohlásit za zastavovací
čas a žádná zastavovací věta se na něj
nepoužívá.

Mimo nulovou množinu má pro každé α
událost S≥α nějakého konečného svědka
Z_n≥α. Při α=(t−1)/t s celým t≥2
dává kladný skok velikosti1 u
R−(t−1)B návštěvu přesné hranice.
Proto jsou návštěvní pravděpodobnosti
v hlavní poznámce skutečně P(S≥α).
Odečtení P(S>α) dává všechny tištěné
atomové vzorce. Tento argument uzavírá
dřívější pouze dolní mez pro atom2/3.

Původní autorské strany3–4 článku
Schulte-Geers–Stadje potvrzují příslušný
výrok i jeho přesný rozsah; zde je celý
potřebný argument, včetně výkyvového
kroku, odvozen. Žádný nový běh.

