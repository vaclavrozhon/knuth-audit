# D154–D155 — celé MPR52–53

7. listopadu 2026. Původní zadání p16/file36 a odpovědi
p378/file398 přímo zobrazeny; autorův PS má zadání p16/file22
a odpovědi p34–35/file40–41. Všech šest vrstev errat a tři
zdrojové TeX soubory byly prohledány podle stran, úloh
i obsahu. Sousední E124 patří jen úloze51. Pro52–53 nebyla
nalezena relevantní oprava. Úplný důkaz nerovnosti(24)
a všech nulových větví se přebírá z D152, nikoli jen její zápis.

## 52: úplný součet přes průniky

Nechť n je nezáporné celé číslo, 0≤k≤n a Y₁,…,Yₙ jsou
nezávislé bity s pravděpodobností p∈[0,1]. Označme R=∑ᵢYᵢ.
Pro každou k-prvkovou podmnožinu A⊆{1,…,n} zaveďme

    W_A=∏ᵢ∈A Yᵢ,       Z=∑_|A|=k W_A=binom(R,k).

Součin je1 právě tehdy, když jsou všechny souřadnice z A
rovny1. Proto druhá rovnost počítá všechny k-prvkové
podmnožiny R úspěšných souřadnic. Z>0 právě tehdy, když
R≥k; pro k=0 je prázdný součin1 a Z=1. Tedy P(Z>0)
je přesně požadovaná spolehlivost F(p,…,p).

Každý W_A má střední hodnotu p^k. Je-li p>0, podmínění
W_A=1 pevně určí Yᵢ=1 pro i∈A a ostatní nezávislé
souřadnice ponechá s pravděpodobností p. Pro jinou
k-prvkovou množinu B proto platí

    E(W_B | W_A=1)=p^{|B\A|}.

Položme j=|B\A|. Protože |A|=|B|, také |A\B|=j.
Množinu B určuje právě výběr j vynechaných prvků z A
a j přidaných prvků z jejího doplňku. Jde o bijekci,
tedy pro každé j je přesně binom(k,j)binom(n−k,j)
takových B; pro j>n−k je počet0. Součtem všech příspěvků
dostáváme stejný podmíněný průměr pro každé A:

    T=E(Z | W_A=1)
      =∑_{j=0}^k binom(k,j)binom(n−k,j)p^j.

Počet indikátorů je binom(n,k). Nerovnost(24), plně
odvozená v D152, tedy dává přesně tištěný výsledek

    F(p,…,p) ≥ binom(n,k)p^k
                 / ∑_{j=0}^k binom(k,j)binom(n−k,j)p^j.       (A)

Jmenovatel má člen j=0 rovný1 a ostatní nezáporné,
takže T≥1 na celém p∈[0,1]. Nemůže zde vzniknout0/0.

### Všechny přirozené kraje

- Je-li p=0 a k>0, je skutečná pravděpodobnost0 a(A)
  dává0/1=0. Podmínění W_A=1 je pak nemožné; netvrdíme,
  že jeho knižní nulový reprezentant je T. Výsledná
  polynomická mez platí přímo, protože všechny čitatele0.
- Je-li k=0, existuje jediná prázdná množina, Z=1,
  T=1 a(A) dává1. Platí i pro n=0 a p=0; p^0 zde
  znamená hodnotu prázdného součinu1.
- Je-li p=1, je Z=binom(n,k) jistě. Výše dokázaná
  bijekce počítá ve jmenovateli každé B právě jednou,
  takže T=binom(n,k) a(A) dává1.
- Je-li k=n, jen j=0 má nenulový koeficient. Dostáváme
  přesnou pravděpodobnost p^n, včetně již vyřešeného n=0.
- Je-li k=1, vzorec je np/(1+(n−1)p), rovněž s kladným
  jmenovatelem a krajními hodnotami0 a1.

Pro celočíselný práh k>n je funkce konstantně0 a pro k<0
konstantně1; tyto triviální případy se řeší přímo.
Tištěný kombinatorický podíl má přirozenou doménu0≤k≤n,
nikoli nevymezené binomické koeficienty se záporním horním parametrem.

## 53: všech šest podmíněných součtů

Nechť Y₁,…,Y₆ jsou nezávislé bity s parametry pᵢ∈[0,1].
Indexy dále bereme modulo6. Položme

    Aᵢ={Yᵢ=1, Yᵢ₊₁=1, Yᵢ₊₂=0},
    Wᵢ=[Aᵢ],        aᵢ=P(Aᵢ)=pᵢpᵢ₊₁(1−pᵢ₊₂),
    Z=∑ᵢ₌₁⁶Wᵢ.

Z>0 je právě disjunkce šesti termů v zadání, takže jeho
pravděpodobnost je požadovaná spolehlivost F(p₁,…,p₆).
Podmíníme-li na Aᵢ s aᵢ>0, všech šest možností pro j
má následující přesné příspěvky:

| j−i modulo6 | E(Wⱼ | Aᵢ) | důvod |
|---|---|---|
| 0 | 1 | podmiňujeme na samotném Aᵢ |
| 1 | 0 | Aᵢ₊₁ žádá Yᵢ₊₂=1 místo0 |
| 2 | 0 | Aᵢ₊₂ žádá Yᵢ₊₂=1 místo0 |
| 3 | aᵢ₊₃ | používá právě zbývající tři nezávislé souřadnice |
| 4 | 0 | Aᵢ₊₄ žádá Yᵢ₊₆=Yᵢ=0 místo1 |
| 5 | 0 | Aᵢ₊₅ žádá Yᵢ₊₇=Yᵢ₊₁=0 místo1 |

Proto E(Z|Aᵢ)=1+aᵢ₊₃ a(24) dává

    F(p₁,…,p₆) ≥ ∑ᵢ₌₁⁶ aᵢ/(1+aᵢ₊₃).                    (B)

Všech šest členů, včetně těch skrytých tištěnou výpustkou:

    p₁p₂(1−p₃) / (1+p₄p₅(1−p₆)),
    p₂p₃(1−p₄) / (1+p₅p₆(1−p₁)),
    p₃p₄(1−p₅) / (1+p₆p₁(1−p₂)),
    p₄p₅(1−p₆) / (1+p₁p₂(1−p₃)),
    p₅p₆(1−p₁) / (1+p₂p₃(1−p₄)),
    p₆p₁(1−p₂) / (1+p₃p₄(1−p₅)).

První i poslední člen přesně souhlasí s původní sazbou.
Každý jmenovatel je≥1. Nulové aᵢ znamená nulový člen,
který se v odvození(24) vynechává; není potřeba nepravdivě
přiřazovat nemožnému podmínění hodnotu1+aᵢ₊₃. Jestliže
všechna aᵢ=0, konečné sjednocení má pravděpodobnost0
a(B) je rovnost. Tím jsou zahrnuty všechny smíšené
nulové i jisté parametry, nejen vnitřek jednotkové krychle.

### Přímá kontrola celého výsledku

Z tabulky plyne, že jedinými slučitelnými dvojicemi
jsou (1,4),(2,5),(3,6). Žádné tři různé události
nemohou nastat současně: každá má jen jednoho slučitelného
partnera. Protilehlé události závisejí na disjunktních
trojicích souřadnic, a jsou tudíž nezávislé. Přesná
pravděpodobnost je tedy

    F=∑ᵢ₌₁⁶ aᵢ−a₁a₄−a₂a₅−a₃a₆.

Pro libovolné a,b∈[0,1] je algebraicky

    (a+b−ab)−a/(1+b)−b/(1+a)
       =ab(1−ab)/((1+a)(1+b)) ≥0.

Sečtením pro tři protilehlé dvojice se znovu odvodí(B),
včetně všech hraničních parametrů. Není to numerický
výčet. Například deterministická konfigurace110110 má
a₁=a₄=1 a ostatní aᵢ=0, takže(B) je přesně1; při všech
pᵢ=0 nebo všech pᵢ=1 jsou všechny termy0 a výsledek0.

## Oba obecné dodatky odpovědi53

Odvození D152 vyžaduje binární indikátory, jejich součet
a odpovídající sjednocení. Nepoužívá monotónnost f ani
prvoimplikantnost termů a nepožaduje nezávislost Wᵢ.
Termy mohou obsahovat negované proměnné, mohou být
redundantní a nemusí být prvoimplikanty. Jestliže jejich
disjunkce vyjadřuje f, sjednocení je přesně{f=1}; i pro
pouhou podrodinu implikantů je sjednocení podmnožinou
{f=1}, takže dolní odhad stále platí.

Jsou-li termy vzájemně disjunktní jako události (stačí
až na nulovou pravděpodobnost), je na každém kladně
pravděpodobném Aᵢ jistě Z=1. Každý podmíněný jmenovatel
je tedy1 a(24) dává ∑ᵢP(Aᵢ)=P(⋃ᵢAᵢ), přesnou rovnost.
Nulové události se vynechají. Tištěný výrok je dostačující
podmínka přesnosti, nikoli tvrzení její nutnosti.

## Rozsah

Celé52 i53 včetně všech dodatků jsou reviewed. Žádný
nový nález, kandidát, bibliografická výjimka nebo numerický
běh. Předchozí důkazy a výpočty se neopakují. File36
zůstává partial pro54–57 a file398 pro54–59.

