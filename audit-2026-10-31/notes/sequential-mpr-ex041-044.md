# D143–D146 — celé MPR41–44

7. listopadu 2026. Původní file36/p16 byl zobrazen celý;
obsahuje úlohy41–57. Jejich soupis není důkazem kontroly.
Zde se uzavírají pouze41–44, s odpověďmi na p377/file397.
Autorův PS má zadání na p16/file22 a odpovědi na
p33–34/file39–40; všechny tyto stránky byly zobrazeny.

## D143, 41(a): všechny reálné exponenty a domény

Pro a≥1 je h(t)=tᵃ na [0,∞) neklesající a konvexní.
Pro a=1 je lineární; pro a>1 má na kladné poloose
h″(t)=a(a−1)tᵃ⁻²≥0 a spojité rozšíření v0. Konvexitu
včetně0 lze získat limitou z kladných argumentů.
Proto pro 0≤θ≤1

    |θx+(1−θ)y|ᵃ
      ≤(θ|x|+(1−θ)|y|)ᵃ
      ≤θ|x|ᵃ+(1−θ)|y|ᵃ.

První krok je trojúhelníková nerovnost a monotónnost h,
druhý jeho konvexita. Pro a=0 se tištěná rodina chápe
jako konstantní funkce1, včetně její hodnoty v0; je
konvexní i konkávní.

Pro 0<a<1 funkce není konvexní: pro x=0,y=1,θ=1/2
je (1/2)ᵃ>1/2. Není ani konkávní na celé ose: pro
x=−1,y=1 má v jejich středu hodnotu0<1. Na kladné
poloose je však h″<0, tedy je konkávní, jak dodává odpověď.

Pro a<0 není |x|ᵃ v0 konečnou reálnou funkcí. Ani žádné
doplnění tohoto bodu však nemůže napravit konvexitu:
pro x=1,y=−1,θ=3/4 je střední argument1/2 a
(1/2)ᵃ>1=θ|1|ᵃ+(1−θ)|−1|ᵃ. Tento rozpor vůbec
nepoužívá hodnotu v0. Konkávnost vylučuje už kladná
poloosa, kde h″=a(a−1)tᵃ⁻²>0; například mezi1 a3
je h(2)<(h(1)+h(3))/2. Na této poloose je h konvexní.
To dokládá celý tištěný rozbor bez předstírání konečné
hodnoty v zakázaném bodě.

## 41(b): celá řada, integrální zbytek a obě znaménka

Označme Rₙ(x)=∑ₖ≥ₙxᵏ/k!, n≥0. Řady i jejich derivace
konvergují absolutně a stejnoměrně na každém omezeném
intervalu, například porovnáním s exponenciální řadou
v |x|. Proto je lze derivovat po členech. Máme

    R₀=eˣ, R₁=eˣ−1,
    Rₙ=eˣ−∑ₖ₌₀ⁿ⁻¹xᵏ/k!,
    Rₙ″=Rₙ₋₂ pro n≥2.

Pro n=0 a1 je druhá derivace eˣ>0, takže obě funkce
jsou konvexní. Pro n≥1 platí pro všechna reálná x

    Rₙ(x)=1/(n−1)! ∫₀ˣ tⁿ⁻¹e^(x−t) dt.       (A)

Odkaz1.2.11.3–(5) byl přímo ověřen v původním svazku1
na p117/file132: dosazení f=eˣ a řádu n−1 dává právě(A).
Navíc je zde vlastní důkaz celé použité identity. Pro n=1
je integrál eˣ−1. Pro n≥2 integrace per partes dává
Iₙ=Iₙ₋₁−xⁿ⁻¹/(n−1)!, což indukcí dává vypsaný
exponenciální zbytek. Integrace po orientovaném intervalu
je platná i pro záporné x; žádný kladný obor se tiše
nepřenáší na celou osu.

Je-li x>0, pravá strana(A) je kladná. Je-li x<0,
znaménko integrandu je (−1)ⁿ⁻¹ a obrácení mezí přidá
další minus: znaménko Rₙ(x) je (−1)ⁿ. Pro x=0 je
Rₙ(0)=0, n≥1.

Je-li n≥2 sudé, Rₙ″=Rₙ₋₂≥0 na celé ose; pro n=2
jde o R₀=eˣ, ostatní sudé případy pokrývá(A).
Proto je Rₙ konvexní. Pro liché n≥3 má Rₙ″ znaménko x,
a tedy je záporná na záporné a kladná na kladné poloose.
Taková funkce není na celé ose ani konvexní, ani konkávní.
Tištěné Rₙ″(x)/x>0 platí přesně pro x≠0; v0 není
podíl potřeba. Tím je ověřena každá větev odpovědi,
včetně zvláštního lichého n=1.

## 41(c): dvojná exponenciála a celý obecný dovětek

Zadaná funkce je exp(exp(|x|)). Je konvexní, protože
absolutní hodnota je konvexní a exponenciála je
konvexní a neklesající; dvakrát použijeme přesně stejný
dvoukrokový argument jako výše s h.

Obecně nechť F(z)=∑ⱼ≥₀aⱼzʲ, kde aⱼ≥0 a řada konverguje
pro každé z. Každá funkce |x|ʲ je pro celočíselné j≥1
konvexní podle(a); j=0 je konstanta. Každý konečný
součet ∑ⱼ≤Naⱼ|x|ʲ je tedy konvexní. Přejdeme-li ve
dvoubodové nerovnosti k N→∞, jsou všechny tři hodnoty
konečné a dostaneme konvexitu F(|x|). Nepotřebujeme
derivovat řadu v bodě0 ani předpokládat hladkost |x|.

Konkrétní dvojitá exponenciála do tohoto dovětku také
patří. Již dokázaný Bellův generující vzorec D140 dává

    exp(exp(z))=e∑ⱼ≥₀varpiⱼ zʲ/j!,

s nezápornými koeficienty a celou pravou funkcí.
Tento dřívější důkaz se přebírá, žádná čísla se nepočítají.

## 41(d): přesný význam nekonečné hodnoty

Tištěný indikátorový zápis znamená po částech definovanou
funkci F(x)=f(x) pro x∈I, jinak F(x)=+∞. Nepožaduje
vyhodnocení nedefinovaného f mimo I ani aritmetiku
neurčitého součinu0·∞. Pro θ=0 nebo1 se konvexní
nerovnost čte prostě jako rovnost příslušné koncové hodnoty.

Pro 0<θ<1: jsou-li x,y∈I, jejich konvexní kombinace
leží v intervalu I a platí nerovnost pro f. Je-li alespoň
jeden z x,y mimo I, pravá strana je+∞ a nerovnost je
automatická. Je tedy konvexní v rozšířeném smyslu,
přesně jak výslovně uvádí odpověď. Otevřené konce
intervalu a jednoprvkový interval jsou stejnými případy.
Při konvenci dovolující prázdný interval je F≡+∞ rovněž
konvexní; žádná hodnota−∞ se zde nevyskytuje.

## D144, 42: přesné převzetí úplného D095

Celý matematický důkaz už existuje v
`notes/sequential-mpr-004-005.md`, oddíl „(20), úplný důkaz
Jensenovy nerovnosti“. Přebíráme jej beze změny, protože
obsahuje všechny předpoklady i mezikroky této úlohy:

- konečnou indukci přes q=1−pₙ, včetně pₙ=1, nulových vah
  a příslušnosti normalizovaného průměru do intervalu;
- spočetnou limitu přes Sₙ=∑ⱼ≤ₙpⱼ, μₙ=∑pⱼxⱼ/Sₙ
  a νₙ=∑pⱼf(xⱼ)/Sₙ; normalizace se nesmí vynechat;
- absolutní konvergenci obou očekávání, Sₙ→1,
  μₙ→EX a νₙ→Ef(X);
- důkaz EX∈I, spojitost konvexního f uvnitř I pomocí
  omezených sečen a zvláštní případ krajního EX,
  kdy je X konstantní skoro jistě. Krajní skok f tím
  není neprávem vyloučen.

To přesně doplňuje všechny předpoklady tištěného
„taking limits“. Za „convex combination“ se v konečném
případě označuje vážený součet s nezápornými vahami
součtu1; EX je odpovídající spočetný vážený průměr.

Odkaz6.2.2–36 byl ověřen nejen v nápovědě p458, ale
také v původní odpovědi svazku3 p711–712/file722–723.
Ta obsahuje konečnou indukci pro konkávní f slučováním
posledních dvou vah; při nulovém součtu vah se tyto
členy vynechají. Dosazení −f dává použitou konvexní
variantu. Vlastní důkaz D095 nepředpokládá derivovatelnost.
Zbývající entropická část úlohy svazku3 se nepřebírá.

Historická věta, že Jensen začal podmínkou p=q=1/2,
zůstává explicitně bibliograficky neověřená. Není použita
jako neprokázaný matematický předpoklad úlohy42.

## Pomocný argument: integrabilní afinní dolní mez

Budeme potřebovat doplnit existenci E f(E(X|Y)), nejen
formálně přepsat symboly. Je-li μ uvnitř intervalu I,
konvexita dává

    supₓ<μ (f(μ)−f(x))/(μ−x)
      ≤ infₓ>μ (f(x)−f(μ))/(x−μ).

Obě meze jsou konečné: na každé straně existuje pevný
bod v I s konečnou sečnou a libovolná levá sečna je
nejvýše libovolná pravá. Vybereme číslo c mezi nimi.
Po přeuspořádání obou druhů sečen máme na celém I

    f(x)≥f(μ)+c(x−μ)=:L(x).                  (B)

Je-li U integrabilní s hodnotami v I, je L(U)
integrabilní a záporná část f(U) je nejvýše |L(U)|.
To opravňuje níže použité konečné i rozšířené očekávání.
Je-li μ krajním bodem a μ=EX, argument D095 dává
X=μ skoro jistě a potřebné tvrzení se řeší přímo.

## D145, 43: každý přechod zesíleného Jensena

Předpokládejme E|X|<∞ a E|f(X)|<∞ podle zdejší definice
očekávání. Položme U=E(X|Y), V=E(f(X)|Y). Z podmíněných
absolutních součtů plyne E|U|≤E|X| a E|V|≤E|f(X)|.
Na každém kladném vlákně Y=y mají X a f(X) konečné
podmíněné absolutní momenty; D095 proto dává

    f(U)≤V.

Podmíněný průměr U patří do I stejným intervalovým
argumentem jako v D095. V nulovém vlákně jsou podle
konvence U=EX a V=Ef(X); tam stejnou nerovnost zajišťuje
už globální Jensen. Při krajním EX je X, a tedy U,
konstantní skoro jistě. Jinak(B) při μ=EX a integrabilitě
U dává integrabilní dolní mez f(U), zatímco f(U)≤V
omezuje jeho kladnou část integrabilním V⁺. Proto
E|f(U)|<∞: prostřední očekávání skutečně existuje.

Nyní je každý krok zadaného zesílení oprávněný:

    f(EX)=f(EU)≤E f(U)≤E V=E f(X).

První a poslední rovnost jsou(12); první nerovnost je
Jensen pro U a druhá je očekávání právě dokázaného
podmíněného Jensena. Všechny operandy mají správný obor.

Přesná sazba tištěného předposledního členu je
E(E f(X)|Y), nikoli E(f(X)|Y). Vnitřní E f(X) je už
konstanta; její podmíněné očekávání je táž konstanta.
Tedy E(E f(X)|Y)=E f(X), jak tisk uvádí. Náš E V
je rovněž E f(X) podle(12), takže lze jím právě tento
konstantní člen nahradit a celý řetěz v tisku je platný.
Nezaměňujeme náhodné V s touto konstantou bodově.
Žádný nový nález kvůli tomuto zápisu nevzniká.
Původní detail je uložen jako `ref-397-answer43.png`.

## D146, 44: konvexita g, její minimum a celý kladný paprsek

Nechť EX=0 a f je konečná konvexní funkce na R.
Definujme g(y)=E f(yX). Bod0 je vnitřní a(B) dává
f(yX)≥f(0)+cyX, takže toto očekávání není −∞;
v případném rozšířeném smyslu může být+∞.

Pro každé pevné x a 0≤θ≤1 máme

    f(x(θy₁+(1−θ)y₂))
      ≤θf(xy₁)+(1−θ)f(xy₂).

Tvrzení platí i pro záporné x, protože oba argumenty
jsou doslova v konvexní kombinaci; neprovádí se změna
směru nerovnosti. Očekávání dává konvexitu g. Jsou-li
obě krajní očekávání konečná, integrabilní afinní dolní
mez a tato horní mez opravňují také očekávání uprostřed.
Je-li pravá strana+∞, konvexní nerovnost je triviální.
Tím je ověřena i tištěná věta o průměru konvexních funkcí.

Jensen dává g(y)≥f(yEX)=f(0)=g(0); při g(y)=+∞ je
to rovněž pravda. Pro 0≤a≤b: je-li b=0, jsou oba body0.
Je-li g(b)=+∞, požadovaný horní odhad je automatický.
Jinak b>0 a pro θ=a/b∈[0,1] dostáváme

    g(a)≤(1−θ)g(0)+θg(b)≤g(b),
    g(0)≤g(a).

To doplňuje celý poslední tištěný krok, včetně a=0,
a=b a případů rovnosti. Výsledkem je zadané
E f(aX)≤E f(bX); nejde o nepravdivé tvrzení pro dvě
libovolné proměnné seřazené jen podle rozptylu.

## Zdroje a přesný rozsah

PDF+PS, všech6lokálních vrstev errat a3TeX: žádná použitelná
oprava tohoto MPR bloku. Početní ani starší verifikační
běh nebyl spuštěn. Všechny41(a–d),42,43,44 jsou reviewed;
file36 zůstává partial pro45–57 a file397 pro45–50.

Primární [autorský PDF Boyd–Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
ověřuje vydání2004 a přesně odkazované cvičení3.10(b),
tištěná p115/file129: monotónnost E f(x₀+t v) pro t≥0
a Ev=0. Lokální tvrzení44 je jeho případ x₀=0; důkaz
je celý uveden výše. Zpřístupněný PDF je sedmý opravený
dotisk2009, nikoli domnělý sken prvního dotisku.

Bibliografické výjimky: Jensenův historický počáteční
předpoklad p=q=1/2 a přesné Lemma3.2.1 v S. M. Ross,
Probability Models for Computer Science(2002), nebyly
z původních pramenů ověřeny. Rychlé hledání Rossova
pramene poskytlo jen katalogy, které se za důkaz obsahu
lemmatu nepřebírají. Všechny matematické kroky jsou
doložené samostatně nebo převzatým úplným D095.
