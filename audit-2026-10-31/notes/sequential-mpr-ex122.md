# MPR 122: oba zákony, každý rozvoj a úplná chyba O(1/n)

D220, 7. listopadu 2026. Původní p24/file44 a p390/file410
i autorův PS p24/47,file30/53 zobrazeny. Žádný nález nebo
kandidát. Starý společný P121 obsahoval přesné odvození
hlavního členu a 40 konečných součtů; přečteny poznámky,
celý příslušný kód a uložené řádky, bez opakování běhu.
Zde jsou navíc doloženy všechny tištěné lokální mezikroky,
uniformní chyby, chvosty a posunutý mřížkový součet.

## (a) Normalizace, momenty a oba logaritmy

Pro t≥0 máme x(t)=(1/2)(1/2)^t a y(t)=(1/4)(3/4)^t.
Geometrická řada dává oba součty 1. Derivací uvnitř
|a|<1, odůvodněnou stejnoměrnou konvergencí na každém
menším uzavřeném kruhu, je Σ_(t≥0)t a^t=a/(1−a)^2.
Proto EX=1, EY=3; všechny potřebné první momenty jsou
absolutně konečné. Podpory jsou stejné a

    ρ(t)=y(t)/x(t)=(3/2)^t/2,
    D(y||x)=3lg(3/2)−1=lg(27/16),
    D(x||y)=1−lg(3/2)=lg(4/3).

To vyhodnocuje každý člen a celou tištěnou nekonečnou
sumu. scripts/verify_mpr122_log_rounding.py používá
přesnou12člennou atanh řadu s geometrickou majorantou
ocasu, odůvodněnou v D219. Importuje pouze funkci
log_bounds; testy121 se nespouštějí. Racionální intervaly
dávají přibližně [.7548875021634671,.7548875021636988]
a [.41503749927884326,.41503749927897043]. Oba leží
striktně uvnitř intervalů pro tištěná zaokrouhlení
.755 a .415. Jeden nice15 běh:0.0008620379958301783s,
žádný starý běh/restart. Každá řada má pevně12 kroků.

## (b) Doména, podpory a převzatý Stirlingův důkaz

n je kladné celé, p je pevné s 0<p<1, q=1−p.
Všechny O-konstanty dále smějí záviset na p; netvrdí
se uniformita při p→0 nebo1. Binomický zákon y má
podporu0,…,n, Poissonův x s parametrem np má kladnou
hmotnost na každém nezáporném celém t. Normalizace
plynou z binomické věty a exponenciální řady.

D(y||x) je konečný součet. Naopak x(n+1)>0=y(n+1),
takže D(x||y)=+∞ přesně podle opravené součtové
definice D/F008. Pokud by se mimo asymptotické zadání
připustilo n=0, oba zákony jsou bodové v0 a obě
divergence jsou0; věta o n+1 se týká kladného n.

Používáme pouze již doloženou Stirlingovu formuli

    ln(m!)=(m+1/2)ln m−m+(1/2)ln(2π)+r_m,
    0<r_m<1/(12m), m≥1.

Přečtený přesný argument je v
workstreams/vol1/notes/gamma-functions.md, (S1)–(S2),
a jeho převzetí v quality-recovery-section-1.2.5-2026-11-06.md.
Rozdíly b_m−b_(m+1) mají kladnou atanh řadu menší než
1/[12m(m+1)], což dává součtovou mez zbytku. Wallisovy
integrály určují konstantu ln√(2π) nezávisle na právě
dokazované asymptotice. Doložená zbytková mez je pro
tento rozbor dostatečná; žádný cizí certifikát neběží.

## Přesný lokální logaritmus binomické pravděpodobnosti

Položme t=np+u√n a s=t/n=p+h, h=u/√n. t je stále
celé. Pro |h|≤min(p,q)/2 leží s i1−s v pevném
kladném intervalu, takže všechny níže používané
derivace jsou omezené konstantou závisející pouze na p.

Z přesných faktoriálů a Stirlingovy formule dostáváme

    ln y(t)=−n Φ(s)−(1/2)ln(2πn s(1−s))+O_p(1/n),
    Φ(s)=s ln(s/p)+(1−s)ln((1−s)/q).

Opravdu n−t=n(1−s) a lineární faktoriálové členy
se zruší; zbytky jsou r_n−r_t−r_(n−t)=O_p(1/n).
Φ(p)=Φ'(p)=0, Φ''(p)=1/(pq),
Φ'''(p)=1/q²−1/p². Taylorova formule s omezenou
čtvrtou derivací dává

    −nΦ(s)=−u²/(2pq)
            +(u³/(6p²)−u³/(6q²))/√n+O_p(u⁴/n).

Logaritmus prefaktoru se rozvine jako

    −(1/2)ln(s(1−s))
      =−(1/2)ln(pq)+(u/(2q)−u/(2p))/√n+O_p(u²/n).

Proto přesně tištěný exponent má koeficient

    A(u)=u/(2q)−u/(2p)+u³/(6p²)−u³/(6q²),

a celkově

    y(t)=exp(−u²/(2pq))/√(2πpqn)
          ·exp[A(u)/√n+R_y],
    |R_y|≤C_p(1+u²+u⁴)/n.

Pro pevné u je R_y=O_p,u(1/n), jak stojí v tisku.
Pro rostoucí centrální interval užíváme právě uvedenou
polynomiální uniformní majorantu, nikoli nedoložené
tvrzení, že konstanta nezávisí na u.

## Přesný lokální logaritmus poměru

Poissonův zákon dává obdobně

    ln x(t)=−n Ψ(s)−(1/2)ln(2πns)+O_p(1/n),
    Ψ(s)=p−s+s ln(s/p).

Ψ(p)=Ψ'(p)=0, Ψ''(p)=1/p, Ψ'''(p)=−1/p².
Proto

    ln x(t)=−u²/(2p)−(1/2)ln(2πnp)
             +[−u/(2p)+u³/(6p²)]/√n+R_x,
    |R_x|≤C_p(1+u²+u⁴)/n.

Odečteme každý člen. Kvadratický koeficient je
−1/(2pq)+1/(2p)=−1/(2q), konstanta −(1/2)ln q,
a koeficient n^(−1/2) je

    B(u)=A(u)−[−u/(2p)+u³/(6p²)]
         =u/(2q)−u³/(6q²).

Tedy tištěná druhá rovnost je přesně

    lnρ(t)=L(u)+B(u)/√n+R_ρ,
    L(u)=−u²/(2q)−(1/2)ln q,
    |R_ρ|≤C_p(1+u²+u⁴)/n.

Všechny znaménkové a normalizační členy jsou tím
ověřeny, včetně chybějícího u³/p² po správném zrušení.

## Uniformní centrální součin

Zvolme konkrétně ε=1/12 a |u|≤n^ε. Pro velké n
je předchozí podmínka na h splněna. A/√n i R_y
jdou uniformně k0. Taylorova mez
|e^v−1−v|≤(v²/2)e^|v| dává

    y(t)=G(u)/√n ·[1+A(u)/√n+O_p((1+|u|⁶)/n)],
    G(u)=exp(−u²/(2pq))/√(2πpq).

Vynásobením předchozím logaritmem vzniká

    y(t)lnρ(t)=G(u)/√n
       ·[L(u)+(B(u)+A(u)L(u))/√n
                  +O_p((1+|u|^10)/n)].

Majoranta stupně10 bezpečně pokrývá A²L, AB a
všechny součiny zbytků: na centrálním intervalu
u²≤n a malé exponentové chyby jsou omezené.
L je sudý polynom a A,B liché, tedy B+AL je lichý.
Tento člen se nezahazuje pouze podle přibližné symetrie
binomického rozdělení; jeho příspěvek vyřeší mřížka níže.

## Skutečné chvosty a přesný význam trading tails

D189 v notes/sequential-mpr-ex089.md byl znovu přečten
v potřebném rozsahu. Pro n nezávislých Bernoulliho
proměnných s koeficienty1 dává
Pr(K−np≥a)≤exp(−2a²/n). Použitím na n−K
dostaneme i dolní ocas. Proto

    Pr(|K−np|>n^(1/2+ε))≤2exp(−2n^(2ε)).

Z přesného faktoriálového zkrácení

    lnρ(t)=ln(n!)−ln((n−t)!)−t ln n
            +(n−t)ln q+np

plyne |lnρ(t)|≤C_p n ln(n+1) na celém0≤t≤n,
včetně obou krajů. Skutečný vnější příspěvek k D
má tudíž absolutní hodnotu nejvýše
C_p n ln(n+1) exp(−2n^(2ε)), menší než kterákoli
pevná záporná mocnina n.

Stejně mizí integrály i mřížkové součty každého
polynomu krát exp(−u²/(2pq)) pro |u|>n^ε:
polynom pohltí polovina Gaussova exponentu; na buňce
vzdálené nejvýše1/2 od bodu u je exponenciála
omezena jinou pevnou Gaussovou funkcí v argumentu
buňky. Porovnání se zbylým integrálem dává
O_p(exp(−c_p n^(2ε))) po případném zvětšení konstanty.

Původní odkaz7.2.1.5–(20), Vol4A p421/file438,
byl zobrazen. Obsahuje právě vysvětlení nahrazení
obou zanedbatelných chvostů a Gaussovy momenty.
Z něj se nepřebírá audit okolního komplexního
integrálu ani dalších stránek; potřebná výměna
chvostů je zde doložena vlastními konkrétními mezemi.

## Mřížka: np nemusí být celé

Přípustná u tvoří posunutou mřížku
u_j=(j−np)/√n s krokem δ=1/√n. Po výměně chvostů
ji lze rozšířit na všechna j∈Z. Pro hladké f
s integrovatelnou druhou derivací platí rovnoměrně
ve všech posunech mřížky

    |δΣ_j f(u_j)−∫_R f(u)du|≤(δ²/8)∫_R |f''(u)|du.

Důkaz: intervaly [u_j−δ/2,u_j+δ/2] rozdělují R.
Taylorův lineární člen má na každém takovém intervalu
integrál0. Integrální zbytek po prohození pořadí
má u každého bodu jádro nejvýše δ²/8; sečteme
integrály |f''| přes disjunktní buňky.
Pro polynomy krát G konvergují všechny použité sumy,
integrály i derivace, takže přechod z konečných
buněk na celou osu je oprávněný.

Aplikace na GL dává chybu O_p(δ²)=O_p(1/n).
Aplikace na G(B+AL), jehož integrál je0 z lichosti,
dává mřížkový průměr O_p(δ²); po dalším1/√n je
jeho příspěvek O_p(n^(−3/2)). Na nezáporné
G(1+u^10) dává totéž konečný uniformní mřížkový
průměr, takže sečtená centrální chyba je O_p(1/n).
Tím není skryta chybná představa přesně symetrické
mřížky nebo nedoložený přechod z Riemannova součtu.

## Gaussův integrál a poslední rovnost

Z předchozích kroků plyne

    D(y||x)=(1/ln2)∫_R G(u)
                 [−u²/(2q)−(1/2)ln q]du+O_p(1/n).

To je přesně tištěný prefaktor1/√(2πpqn),
integrand a diferenciál du√n. Normalizace
∫G=1 plyne z Gaussova integrálu (jeho čtverec
se vyhodnotí v polárních souřadnicích); pro a>0
∫e^(−au²)du=√(π/a). Integrací po částech
∫u²e^(−au²)du=(1/(2a))∫e^(−au²)du,
protože u e^(−au²)→0 na obou koncích.
S a=1/(2pq) tedy ∫u²G=pq. Dostáváme

    D(y||x)=[−p−ln q]/(2ln2)+O_p(1/n)
            =[ln(1/(1−p))−p]/(2ln2)+O_p(1/n).

To dokazuje požadovaný absolutní zbytek, všechny
tištěné mezikroky i správný převod z ln na lg.
Hlavní člen je nezáporný, protože −ln(1−p)>p
pro0<p<1, což plyne integrací1/(1−p)>1.

## Přesné převzetí staré nezávislé kontroly a rozsah

INFORMATION_NOTES.md vychází z téhož přesného
faktoriálového zkrácení s L=n−K a dává nezávislý
momentový výpočet. K požadované přesnosti jej lze
uzavřít stručně: pro m=nq, h(s)=(s+1/2)ln s−s
a c=(1/2)ln(2π) je ln(L!)=h(L)+c+O(1/n)
na |L−m|≤m/2. Taylor do třetího řádu má čtvrtý
zbytek O(|L−m|⁴/n³). Přesné binomické momenty
jsou μ2=npq, μ3=npq(p−q) a μ4=O_p(n²);
plynou rozvinutím součtu nezávislých centrovaných
Bernoulliho proměnných (nepárové singletony mají
střední hodnotu0). Proto

    E ln(L!)=h(m)+c+(1/2)h''(m)npq+O_p(1/n)
             =h(m)+c+p/2+O_p(1/n).

Třetí člen má velikost O(1/n) a čtvrtý zbytek také;
vynechaný ocas je exponenciální podle D189 a
|ln(L!)|≤n ln(n+1). Z h(n)−h(nq) se pak přesně
zruší lineární a nlogn členy v původním vzorci
a zbude −(1/2)ln q−p/2+O_p(1/n).
Jde o další uzavřený argument pro hlavní výsledek.

Přečtený starý soubor results/information_asymptotics.json
má40 řádků při60ciferné přesnosti a porovnává navíc
další koeficient p²/[12q ln2]. Tyto uložené kontroly
se zachovávají, neběží znovu a nenahrazují důkaz.
Nové uzavření nepotřebuje silnější O(n^−2) tvrzení
o dalším členu; jeho původní poznámka zůstává beze změny.

Šest vrstev errat a tři TeX zdroje neposkytly opravu122.
Žádná bibliografická výjimka; potřebné vnitřní závislosti
jsou přesně doloženy a původní4A odkaz zobrazen.
Konečný součet divergence by šel spočítat O(n)
aritmetickými/logaritmickými operacemi, s postupně
aktualizovanými váhami; zde se žádný takový nový
součet neprovádí a netvrdí se bitová cena.

Celá122 je checked. P121 je nyní checked pro celý
společný rozsah121–122 s výslovnými doménami D219/D220.
File44 je reviewed; file410 zůstává partial pro123–124.

