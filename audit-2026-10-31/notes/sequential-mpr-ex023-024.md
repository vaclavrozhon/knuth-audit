# D125–D126 — celé MPR23 a24(a–c)

6. listopadu 2026. Přímo zobrazeny zadání p14/file34 a celé odpovědi
p373–374/file393–394, také Pre-Fascicle5A p14/file20 a p30–31/file36–37.
Všechny následující argumenty jsou obecné; nový numerický běh není třeba.
Známé změny E122–E123 jsou ve svazku4B už zapracovány.

## D125: definice kumulativní binomické pravděpodobnosti

Nechť X₁,…,X_n jsou nezávislé bity s EX_j=p∈[0,1], q=1−p.
Pro daný k má každý konkrétní vzor s k jedničkami pravděpodobnost
p^k q^{n−k}; vzorů je binom(n,k) a jsou disjunktní. Proto

    B_{m,n}(p)=P(X₁+⋯+X_n≤m)
             =∑_{k=0}^m binom(n,k)p^k q^{n−k},       0≤m≤n.

Mocnina s exponentem0 je konstantní monom1, i když p či q je0.
Tak se správně vyhodnocují degenerované rozdělení, bez neurčitého
numerického výrazu0^0. Pro n=0,m=0 jde o prázdný součet proměnných
rovný0 a pravděpodobnost1. Část24 používá m/n, a tedy n≥1.

## D125: každá událost z nápovědy a druhý součet

Označme T počet nul a J₁<⋯<J_T jejich pozice. Nejprve předpokládejme
m<n a položme r=n−m≥1. Událost X₁+⋯+X_n≤m je právě T≥r.
Na této události existuje jediná r-tá nula, takže ji disjunktně
rozložíme podle J_r=s pro s=r,…,n.

Událost {T≥r,J_r=s} je přesně

    X_s=0 a X₁+⋯+X_{s−1}=s−r.

Prvních s−1 pozic obsahuje r−1 nul a s−r jedniček. Jejich
volba dává binom(s−1,s−r) možností. Pozice s přidá další nulu;
suffix s+1,…,n je volný a jeho celková pravděpodobnost je1.
Z nezávislosti tedy vychází přesně odpovědní pravděpodobnost

    P(T≥r,J_r=s)=binom(s−1,s−r)p^{s−r}q^r.

Dosazením k=s−r, tedy 0≤k≤n−r=m, získáme požadovaný druhý zápis

    B_{m,n}(p)=∑_{k=0}^m binom(n−m−1+k,k)p^k q^{n−m}.

Nápověda je tím provedena v obou směrech a její rozklad je úplný.
Při p=0 je nenulový pouze člen k=0 a dává1; při p=1,m<n je q^r=0
a celý součet0. Pro m=0 je jediný člen q^n, tedy událost samých nul.

Při m=n musí být J₀ vynecháno: nápověda pro r≥1 se na tento
okraj nevztahuje. Pravděpodobnost je přímo1. Vytištěný konečný
součet ji přesto dává správně: binom(−1,0)=1 podle prázdného
součinu a binom(k−1,k)=0 pro každé k≥1. Zbude jediný člen1,
včetně p=0 či1 a také n=m=0. Standardní rozšíření binomického
koeficientu v k=0 tedy přesně vyřeší záporný horní index.

## D126(a): každý derivační mezikrok a okraje integrálu

Nechť n≥1 a0≤m<n. B_{m,n}(x) je polynom. Derivace každého
monomu dává

    B′_{m,n}(x)
      =∑_{k=1}^m binom(n,k)k x^{k−1}(1−x)^{n−k}
       −∑_{k=0}^m binom(n,k)(n−k)x^k(1−x)^{n−1−k}.

První suma začíná1, takže v x=0 nevznikne formální0·x^{−1}.
Druhá suma má nezáporné exponenty, neboť m<n. Použijeme
k binom(n,k)=n binom(n−1,k−1) a
(n−k)binom(n,k)=n binom(n−1,k). Po posunu prvního indexu

    B′_{m,n}(x)
      =n[∑_{k=0}^{m−1}binom(n−1,k)x^k(1−x)^{n−1−k}
          −∑_{k=0}^{m}binom(n−1,k)x^k(1−x)^{n−1−k}]
      =−n binom(n−1,m)x^m(1−x)^{n−1−m}.

Pro m=0 je první suma prázdná; rušení členů stále platí.
Konstanta n binom(n−1,m)=(n−m)binom(n,m) je kladná.
Protože B_{m,n}(1)=0 pro m<n, integrace od p do1 dává

    B_{m,n}(p)=(n−m)binom(n,m)∫_p^1 x^m(1−x)^{n−1−m} dx.

To platí na celém intervalu p∈[0,1], včetně konců. Při p=0
dostáváme normalizaci celého integrálu na1/((n−m)binom(n,m)).
Při m=0 jde přímo o(1−p)^n; při m=n−1 o1−p^n.
Samotné m=n je z integrálního tvrzení výslovně vyloučeno.

## D125: navíc přímá konečná algebraická kontrola druhého součtu

Pro r=n−m≥1 položme a_k=binom(r+k−1,k) a
H(p)=q^r∑_{k=0}^m a_kp^k. Po derivování a vyjmutí q^{r−1}
je koeficient při p^j pro j<m roven

    (j+1)a_{j+1}−(j+r)a_j=0.

Rovnost plyne z poměru sousedních binomických koeficientů.
Zbývající koeficient při p^m je −(m+r)a_m,
takže H′(p)=−n binom(n−1,m)p^m q^{r−1}=B′_{m,n}(p).
Oba polynomy mají v0 hodnotu1, proto jsou totožné. Jde o druhý
úplný důkaz vzorce23, nezávislý na pravděpodobnostním rozkladu.
Pro m=n platí zvláštní vyhodnocení uvedené výše.

Konkrétní odkaz CMath, úloha8.17, není v lokální knihovně
k dispozici a jeho číslování je explicitní bibliografickou výjimkou.
Samotná algebraická identita zde nezůstala bez důkazu.

## D126(b): celý integrální argument pro0≤m<n/2

Položme a=m, b=n−1−m. Z celočíselnosti n,m a m<n/2 plyne
0≤a≤b. Prah m/n je t=a/(a+b+1). Označme
f(x)=x^a(1−x)^b. Podle(a) stačí dokázat

    ∫₀^t f(x)dx < ∫_t^1 f(x)dx.

Je-li a=0, pak t=0, levá strana je0 a pravá je1/(b+1)>0.
Tento případ musí být oddělen před dělením a či užitím logaritmu.

Nechť a>0 a c=a/(a+b). Pak 0<t<c≤1/2. Dokážeme nejprve
∫₀^c f≤∫_c^1 f. Pro 0≤ε≤a porovnáme dva body
x=(a−ε)/(a+b) a x′=(a+ε)/(a+b). Druhý leží v[c,2c]⊆[c,1].
Po násobení kladným faktorem(a+b)^{a+b} je požadovaná bodová
nerovnost f(x)≤f(x′) právě

    (a−ε)^a(b+ε)^b ≤ (a+ε)^a(b−ε)^b.

Pro0<ε<a a u≥a platí vytištěný logaritmický rozvoj

    ((u−ε)/(u+ε))^u
       =exp[u(ln(1−ε/u)−ln(1+ε/u))]
       =exp[−2ε(1+ε²/(3u²)+ε⁴/(5u⁴)+⋯)].

Taylorovy řady konvergují absolutně, neboť ε/u<1. Každý člen
za počáteční1 je nezáporný a při růstu u neroste. Celá závorka
proto neroste a po násobení −2ε argument exponenciály neklesá.
Funkce je tedy neklesající v u. Dosadíme u=a a u=b,
a dostaneme uvedenou bodovou nerovnost. Pro ε=0 je rovnost;
pro ε=a ji dostaneme spojitou limitou, včetně a=b.
Tím jsou ošetřeny i konce, kde zapsaná logaritmická řada přímo
konvergovat nemusí.

Reflexe x′=2c−x má jednotkový absolutní Jacobian, takže

    ∫₀^c f(x)dx ≤ ∫_c^{2c}f(x)dx ≤ ∫_c^1 f(x)dx.

Jelikož0<t<c a f je kladná uvnitř(0,1), máme

    ∫₀^t f < ∫₀^c f ≤ ∫_c^1 f < ∫_t^1 f.

Po normalizaci celým integrálem z(a) je tedy B_{m,n}(m/n)>1/2.
Případ a=b není ztracen: střední nerovnost je rovnost ze symetrie,
ale obě krajní nerovnosti z t<c zůstávají ostré. To pokrývá
také n=2m+1. Pro a=0 platí závěr již z oddělené větve.

## D126(c): všechny poměry, přesný kladný rozdíl a konečné párování

Případ m=n má p=1, součet proměnných je jistě n a B=1.
Oddělíme jej před použitím poměrů obsahujících n−m ve jmenovateli.
Pro n/2≤m<n položme l=n−m. Pak1≤l≤m a všechny členy

    t_k=binom(n,k)m^k l^{n−k},       0≤k≤n,

jsou kladné. Vytištěné pravděpodobnosti jsou
B_{m,n}(m/n)=n^{−n}∑_{k≤m}t_k a jeho doplněk
n^{−n}∑_{k>m}t_k, neboť m+l=n.

Každý člen pravého ocasu má k=m+d, 1≤d≤l. Spárujeme jej
s levým členem k=m+1−d. Tyto levé indexy jsou různé a leží
v[2m+1−n,m]⊆[1,m], tedy skutečně uvnitř levého součtu.
Pro poměr r_d=t_{m+d}/t_{m+1−d} vychází

    r₁=t_{m+1}/t_m=m/(m+1)<1.

Pro1≤d<l lze všechny poměry dělit, neboť jsou kladné, a běžný
poměr sousedních binomických členů dává přesně

    r_{d+1}/r_d
      = (l+d)(l−d)m² / ((m+1+d)(m+1−d)l²).

Jmenovatel je kladný. Jeho rozdíl s čitatelem je

    ((m+1)²−d²)l²−(l²−d²)m²
      =(2m+1)l²+(m²−l²)d²
      =(2m+1)(n−m)²+(2m−n)nd² >0.

První člen je kladný a druhý nezáporný, protože m≥n/2.
Tím je zkontrolována každá část tištěné identity i ostré znaménko.
Indukcí jsou všechny r_d<1. Při l=1 není žádný indukční krok
potřeba; stačí r₁. Při m=n/2 je druhý člen rozdílu0, první
zůstává kladný.

Každý člen pravého ocasu je tedy ostře menší než jeho levý partner.
Zbylé levé členy jsou nezáporné, například t₀ je kladný a není
spárován. Součtem dostáváme

    1−B_{m,n}(m/n)<B_{m,n}(m/n),

a tedy znovu B_{m,n}(m/n)>1/2. Všechny indexy jsou uvnitř
přípustných rozsahů; podíly0/0 z m=n se nepoužily.

## D126: skutečný závěr o mediánu

Části(b),(c) dávají P(S≤m)>1/2 pro každé celé0≤m≤n,
když S má binomické rozdělení s p=m/n. Pro druhou polovinu
definice mediánu použijeme S′=n−S. Jeho bity jsou1−X_j,
zůstávají nezávislé a mají střední hodnotu(n−m)/n. Stejný
již dokázaný výsledek pro celé n−m dává

    P(S≥m)=P(S′≤n−m)>1/2.

Proto m splňuje obě podmínky mediánu. Platí i oba degenerované
konce m=0 a m=n. Ostré nerovnosti dokonce vylučují jiný reálný
medián: pod m nebo nad m by příslušná jednostranná pravděpodobnost
byla menší než1/2. Poslední knižní věta tedy skutečně plyne,
nikoli jen z jednoho ze dvou potřebných ocasů.

## E122–E123 a přesný bibliografický rozsah

Ve známých erratech Fascicle5 jsou z18. října2020 oddělené
derivační sumy se začátkem k=1, podmínka a>0 a nahrazení
„increases“ slovem „nondecreasing“. Z27. října2020 je rating
HM28. Vše je v našem4B zapracováno; označujeme jako E122.
Z24. července2022 je přidaný Jansonův odkaz, rovněž zapracovaný,
evidovaný jako E123. Přímo zobrazeny all4f5 p10 a zdrojový
TeX, řádky740–754, rating též řádky262–264. Žádné UI karty
ani barevné lokace pro tyto již zveřejněné změny.

Šest textových vrstev errat a tři TeX zdroje jsou zachyceny
v `results/sequential/mpr-023-024-binomial-errata.json`.
Jiné odpovědi23/24 ve4B p420, Fascicle5 p208 a Fascicle6 p189
patří jiným oddílům, nikoli tomuto argumentu.

Historické atribuce Pearson1924, Neumann1966 a Lord2010 nebyly
v původních článcích rychle dostupné a jsou explicitní bibliografické
výjimky. Jejich matematické argumenty vytištěné v odpovědi byly
všechny provedeny výše; nevzniká neověřená věta převzatá jen z citace.
Přesné číslování CMath8.17 je rovněž vynecháno.

Jansonův článek je ověřen v
[metadatech vydavatele](https://www.sciencedirect.com/science/article/pii/S0167715220303230):
Svante Janson, Statistics & Probability Letters171(2021),109020,
DOI10.1016/j.spl.2020.109020. Jeho
[autorský preprint](https://arxiv.org/abs/2009.13781) má v abstraktu
stejnou binomickou pravděpodobnost a uvádí další výsledek o jejím
minimu. Zde byla ověřena pouze bibliografická souvislost, ne celý
další článek. Tištěný údaj10stran publikované verze nebyl samostatně
porovnán s PDF; počet12stran preprintu je jiná verze a není důvodem
pro nález. Metadata a omezení jsou v
`sources/mpr023-024-bibliography.json`.

Celé MPR23 a24 jsou reviewed, s uvedenými bibliografickými výjimkami.
Na file393 tím zůstává pouze Eulerova výzkumná poznámka u19;
na file394 je nově doložena jen zdejší část odpovědi24, nikoli25–28.
File34 má zbývající25–26. Staré výpočty a rozpracování se neopakovaly.
