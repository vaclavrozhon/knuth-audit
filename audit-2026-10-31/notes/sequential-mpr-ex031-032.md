# D133–D134 — celé MPR31 a32

6. listopadu2026. Zadání p15/file35 a odpovědi p376/file396
přímo zobrazeny, stejně jako Pre-Fascicle5A p15/file21 a
p32/file38. Níže jsou všechny polynomy, obecný důkaz, opačný
směr konstrukce i nulové/jisté konce. Nezávislost se nepředpokládá.

## 31: přesný význam polynomu

Označme N={1,…,n}, I_i=[A_i] a
π_J=Pr(⋂_{j∈J}A_j), včetně π_∅=1. Pro každý J⊆N
definujme atom

    E_J=(⋂_{j∈J}A_j)∩(⋂_{j∉J}¬A_j).

Všech2^n atomů je vzájemně disjunktních a jejich sjednocení
je celý prostor: každý výsledek určí právě množinu pravdivých
událostí. Některé atomy smějí mít nulovou hmotnost.
Indikátor E_J je přesně

    M_J(I)=∏_{j∈J}I_j ∏_{j∉J}(1−I_j).

Pro booleovskou funkci f:{0,1}^n→{0,1} tedy celočíselný
multilineární polynom

    F(x)=∑_{J⊆N} f(1_J)∏_{j∈J}x_j ∏_{j∉J}(1−x_j)

souhlasí s f na každém booleovském vektoru: právě jeden
minterm tam má hodnotu1. Každá proměnná vystupuje v každém
součinu nejvýše jednou. Po roznásobení jde o součet
F(x)=∑_{J⊆N}c_J∏_{j∈J}x_j s celočíselnými c_J.
Je to obyčejný reálný polynom, ne součet modulo2.

Jednoznačnost: nulový multilineární polynom v n proměnných
lze psát U(x₁,…,x_{n−1})+x_nV(x₁,…,x_{n−1}).
Nulovost na vrcholech s x_n=0 dává U=0 indukcí, a vrcholy
s x_n=1 potom V=0. Základ n=0 je nulová konstanta.
Tím je identifikován právě polynom užitý v zadání.

## 31: očekávání každého monomu

Součin∏_{j∈J}I_j je indikátor průniku, takže jeho očekávání
je π_J, také pro J=∅, kdy prázdný součin je1. Proto

    Pr(f(I)=1)=E f(I)=E F(I)=∑_{J⊆N}c_J π_J.

První rovnost je přesně tištěné odůvodnění; f(I) nabývá jen0,1.
Poslední přechod je linearita konečného součtu, nikoli
neoprávněná záměna očekávání součinu za součin očekávání.
Tím je dokázána instrukce nahradit každý monom číslem π_J.
Obecná neshoda π_J≠∏π_{j} nepředstavuje žádný problém.

## 31: každý člen vytištěného XOR příkladu

Pro bity a,b platí[a⊕b]=a+b−2ab: pro oba bity stejné
je hodnota0, pro různé1. Proto postupným dosazením

    x₁⊕(x₂⊕x₃)
      =x₁+(x₂+x₃−2x₂x₃)−2x₁(x₂+x₃−2x₂x₃)
      =x₁+x₂+x₃−2x₁x₂−2x₁x₃−2x₂x₃+4x₁x₂x₃.

Jsou tak ověřeny všechny tři kladné lineární, všechny tři
záporné kvadratické i kladný kubický koeficient. Dosazení
očekávání dává přesně

    π₁+π₂+π₃−2π₁₂−2π₁₃−2π₂₃+4π₁₂₃.

## 31: všechny čtyři členy mintermu v odpovědi

Při n=4,J={1,4} je

    M_J(x)=x₁(1−x₂)(1−x₃)x₄
           =x₁x₄−x₁x₂x₄−x₁x₃x₄+x₁x₂x₃x₄.

Odpovídající událost je A₁∩¬A₂∩¬A₃∩A₄. V tištěném
dvoukroku nejprve odečteme část s pravdivým A₃ od
A₁∩¬A₂∩A₄; uvnitř obou členů potom odečteme část A₂.
Tedy přesně

    Pr(A₁¬A₂¬A₃A₄)
      =Pr(A₁¬A₂A₄)−Pr(A₁¬A₂A₃A₄)
      =(π₁₄−π₁₂₄)−(π₁₃₄−π₁₂₃₄).

Obě odečítané události jsou podmnožinami příslušných větších
událostí. Výraz nevyžaduje žádnou nezávislost ani kladné
jednotlivé pravděpodobnosti. Sčítáním disjunktních mintermů
dostaneme každou booleovskou funkci, jak tvrdí odpověď.

## 32: explicitní nutná podmínka pro všech2^n atomů

Roznásobením indikátoru E_J z první části dostáváme

    μ_J:=Pr(E_J)=∑_{K⊆N\J}(−1)^{|K|}π_{J∪K}.   (1)

Proto je nutné, aby všechna μ_J≥0. Přesně tato čísla má
na mysli odpověď32 jako pravděpodobnosti mintermů.
Pro J=N je to π_N≥0; pro J=∅ je to celý inkluzivně-exkluzivní
součet, nikoli součin pravděpodobností doplňků.

## 32: součet je automaticky1

Sečtením(1) přes J a seskupením koeficientu daného π_L
dostáváme

    ∑_{J⊆N}μ_J
      =∑_{L⊆N}π_L ∑_{J⊆L}(−1)^{|L\J|}
      =π_∅=1.

Vnitřní součet je1 pro L=∅; pro neprázdné L lze členy
spárovat podle přítomnosti jednoho pevného prvku a vyruší se.
Tím je automatická normalizace prokázána i bez předpokladu,
že nějaké původní události už existují. Všechny součty jsou konečné.

## 32: úplná dostačitelnost, včetně návratu všech π

Předpokládejme zadaná čísla s π_∅=1 a μ_J z(1) nezáporná.
Na konečném prostoru Ω=2^N přiřaďme výsledku J hmotnost μ_J
a položme A_i={J⊆N:i∈J}. Předchozí normalizace zaručuje
pravděpodobnostní prostor. Pro libovolné I⊆N platí

    Pr(⋂_{i∈I}A_i)=∑_{J⊇I}μ_J
      =∑_{L⊇I}π_L ∑_{I⊆J⊆L}(−1)^{|L\J|}
      =π_I.

Tentokrát se vnitřní součet páruje po prvku L\I a přežije
jen L=I. Každá zadaná průniková pravděpodobnost je tedy
obnovena přesně. Nulové atomy lze ponechat jako výsledky
s nulovou hmotností. Žádná dodatečná skrytá podmínka nechybí.
Z konstrukce ostatně plyne i0≤π_I≤1 a monotónnost, pokud
by tyto požadavky nebyly už uvedeny v zadání.

## 32: proč samotná monotónnost nestačí

Pro I⊆J je⋂_{j∈J}A_j⊆⋂_{i∈I}A_i, tedy π_I≥π_J.
Při n=2 však data

    π_∅=1, π₁=π₂=3/4, π₁₂=0

splňují všechny tyto monotónnosti i rozsah[0,1], zatímco
μ_∅=1−π₁−π₂+π₁₂=−1/2. Žádné rozdělení neexistuje.
Obecně μ_∅≥0 pro n=2 dává právě další tištěnou podmínku

    π₁₂≥π₁+π₂−1.

Zbývající tři atomové podmínky jsou π₁₂≥0,
π₁−π₁₂≥0 a π₂−π₁₂≥0. Je tak patrné, která nutná
podmínka v monotónnosti chybí. Pro n=1 již rozsahπ₁∈[0,1]
stačí, neboť atomy jsou π₁ a1−π₁. Pro n=0 je jediný
atom Ω s hmotnostíπ_∅=1 a obě úlohy jsou konstantní případ.

## Odkaz, errata a rozsah

Skutečný odkaz4A7.1.1–12 byl přímo zobrazen na p80/file97.
Definuje právě celočíselnou multilineární reprezentaci bez
redukce modulo2; tento definiční rozsah odpovídá zdejšímu
polynomu. Neprohlašuje se za dokončenou celá úloha4A–12
s jejími částmi(a–e), celá stránka80 ani sousední úloha13.

Všech6errat+3TeX prohledáno podle obou čísel, současných
i historických stránek a klíčových pojmů. Záznam4Bp554/answer31
se týká jiné sekce, stejně jako F6p135/exercise31. Žádná oprava
tohoto MPR bloku nenalezena. Bibliografická výjimka zde není.
Přesné hashe a kontexty jsou v mpr-031-032-events-errata.json.

D133/MPR31 a D134/MPR32 jsou checked/reviewed. File35
zůstává partial pro33–40. Na file396 jsou nově posouzené31–32;
dříve doložená samotná věžová identita(*) z35 zůstává převzata
v původním rozsahu. Celé sousední odpovědi33–38 tím uzavřeny
nejsou. Žádný nález ani numerický běh.
