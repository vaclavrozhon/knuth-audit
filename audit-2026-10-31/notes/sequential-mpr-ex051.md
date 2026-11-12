# D153 — celá MPR51, se známou opravou E124

7. listopadu 2026. Zadání p16/file36 a odpověď p378/file398
byly přímo zobrazeny, také autorův PS p16/file22 a
p34/file40. Všech6vrstev errat a3TeX je zkontrolováno.
Známá oprava z6. dubna2026 je přímo vidět také v původním
all4b.pdf, file9; TeX err4b.textxt, řádky683–687.

## Obecný převod dolního odhadu na horní

Pro booleovskou funkci f definujme její duál
g(y₁,…,yₘ)=1−f(1−y₁,…,1−yₘ). Jsou-li Bᵢ nezávislé
bity s parametry pᵢ, jsou Yᵢ=1−Bᵢ nezávislé bity
s parametry qᵢ=1−pᵢ. Bodově g(Y)=1−f(B), takže
pro jejich spolehlivostní polynomy platí přesně

    G(q₁,…,qₘ)=1−F(p₁,…,pₘ).

Je-li g vyjádřeno jako disjunkce termů s indikátory Wⱼ,
pak pro Z=∑ⱼWⱼ máme {Z>0}={g(Y)=1}. Úplná MPR50
dává dolní odhad L(q)≤G(q), a tedy F(p)≤1−L(1−p).
Vzájemná nezávislost Wⱼ není potřebná. Pro konstantní
g=0 nebo1 se přesný výsledek určí přímo; pro konečnou
nekonstantní booleovskou funkci vždy existuje konečná
disjunktivní reprezentace, například její mintermy.
Je-li f monotónní, je také g monotónní, neboť převrácení
vstupů i výstupu obrátí uspořádání dvakrát.

## Celý booleovský rozklad konkrétního příkladu

V(25) je

    f(x)=x₁x₂x₃ ∨ x₂x₃x₄ ∨ x₄x₅.

Po De Morganovi a označení yᵢ=1−xᵢ máme

    ¬f=(y₁∨y₂∨y₃)(y₂∨y₃∨y₄)(y₄∨y₅).

Položme B=y₂∨y₃. První dva faktory splňují
(y₁∨B)(B∨y₄)=B∨y₁y₄. Roznásobení s posledním
faktorem pak dává

    B y₄ ∨ B y₅ ∨ y₁y₄ ∨ y₁y₄y₅
      = y₁y₄ ∨ y₂y₄ ∨ y₃y₄ ∨ y₂y₅ ∨ y₃y₅.

Poslední rovnost používá absorpci y₁y₄y₅ do y₁y₄
a přesné rozvedení B. Tím je doloženo všech pět
tištěných termů i úplnost disjunkce.

E124: původní PDF i PS mají mezi těmito termy znaménka+.
Ta zde musí být OR; například při všech yᵢ=1 dává
aritmetický součet5, zatímco ¬f=1. Změnu všech čtyř
plusů výslovně obsahuje zveřejněné erratum6.4.2026.
Jde pouze o známou opravu, nikoli náš nový nález,
kartu nebo důvod barvit mapu. Zbytek řešení se kontroluje
s touto opravou, nikoli automaticky přebírá z errata.

## Všech25 podmíněných příspěvků

Definujme A₁={1,4}, A₂={2,4}, A₃={3,4}, A₄={2,5},
A₅={3,5}, Wᵢ=∏ᵣ∈AᵢYᵣ a Z=∑ᵢ₌₁⁵Wᵢ.
Pro P(Wᵢ=1)>0 podmínění nutí právě Yᵣ=1 pro r∈Aᵢ;
ostatní nezávislé souřadnice si zachovají původní zákon.
Proto každý příspěvek v E(Z|Wᵢ=1) je přesně

    E(Wⱼ|Wᵢ=1)=∏ᵣ∈Aⱼ\Aᵢ qᵣ.

Prázdný součin je1. Všechny rozdíly množin a všechny
tištěné příspěvky zachycuje tato úplná tabulka:

| podmínění | W₁ | W₂ | W₃ | W₄ | W₅ |
|---|---|---|---|---|---|
| W₁=1 | 1 | q₂ | q₃ | q₂q₅ | q₃q₅ |
| W₂=1 | q₁ | 1 | q₃ | q₅ | q₃q₅ |
| W₃=1 | q₁ | q₂ | 1 | q₂q₅ | q₅ |
| W₄=1 | q₁q₄ | q₄ | q₃q₄ | 1 | q₃ |
| W₅=1 | q₁q₄ | q₂q₄ | q₄ | q₂ | 1 |

Součty řádků D₁,…,D₅ jsou tudíž právě

    D₁=1+q₂+q₃+q₂q₅+q₃q₅,
    D₂=q₁+1+q₃+q₅+q₃q₅,
    D₃=q₁+q₂+1+q₂q₅+q₅,
    D₄=q₁q₄+q₄+q₃q₄+1+q₃,
    D₅=q₁q₄+q₂q₄+q₄+q₂+1.

Čitatele E Wᵢ jsou q₁q₄,q₂q₄,q₃q₄,q₂q₅,q₃q₅.
MPR50 dává přesně každý zlomek vytištěného součtu:

    G(q)≥q₁q₄/D₁+q₂q₄/D₂+q₃q₄/D₃
                         +q₂q₅/D₄+q₃q₅/D₅.       (A)

Všechna Dᵢ≥1 pro qᵢ∈[0,1], takže zde nejsou nulové
jmenovatele. Je-li čitatel E Wᵢ nulový, původní
podmíněný průměr podle autorovy nulové konvence nemusí
být Dᵢ; netvrdíme takovou identitu na nemožné události.
Tento člen se ale v MPR50 vynechává a v(A) je přesně0.
Je-li EZ=0, jsou všechny čitatele0, G(q)=0 a(A) je
platná rovnost. Polynomické jmenovatele tak poskytují
správné všude definované pokračování výsledného odhadu.

Pro qᵢ=1 jsou Dᵢ=5 a každý čitatel1, takže(A) dává1=1.
Pro všechna qᵢ=0 dává0=0. Smíšené nulové/jisté parametry
jsou už zahrnuty předchozím rozlišením pozitivních termů.

## Obě tištěné desetinné meze přesně

Pro q₁=⋯=q₅=1/10 je každý čitatel1/100.
Řádky1,4,5 mají Dᵢ=61/50, řádky2,3 mají Dᵢ=131/100.
Tedy

    L=3/122+2/131=637/15982.

Porovnání s0.039 je přesná celočíselná nerovnost

    1000·637−39·15982=13702>0.

Z toho G(.1,…,.1)≥637/15982>0.039. Po doplnění
pᵢ=1−qᵢ=9/10 dostáváme druhý vytištěný výsledek

    F(.9,…,.9)≤15345/15982<0.961,

neboť 961·15982−1000·15345=13702>0.
Oba striktní desetinné výroky tedy následují z přesné
neostré momentové meze; nejde o zaokrouhlení v nesprávném
směru. Dříve dokázaná přesná hodnota F(.9,…,.9)=0.9558
z D096 zůstává beze změny a bez opakování kontroly.

## Rozsah

Celá51 je reviewed s aplikovaným E124. Žádný nový nález,
kandidát nebo bibliografická výjimka tohoto bloku.
Všech6vrstev errat+3TeX a originální sazba byly posouzeny;
známá oprava se neeviduje jako naše karta. Každý z25
symbolických příspěvků i obě číselné meze jsou dokázány
výše bez numerického běhu. File36 zůstává partial pro52–57;
file398 má úplné50(b–e) a51, ostatní52–59 zůstávají otevřené.
