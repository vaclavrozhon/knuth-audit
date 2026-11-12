# MPR 116: celý polynomický důkaz dělitelného podgrafu

D214; 7. listopadu 2026. Zadání str. 24 / file 44, odpověď str. 389 /
file 409; původní PDF i Pre-Fascicle 5A str. 24 a 45 / file 30 a 51
přímo zobrazeny. Lokální znaménková chyba F176 nemění závěr. Žádný
výpočet, census nebo restart; žádná bibliografická výjimka.

## Každý předpoklad a polynom

G je konečný neorientovaný multigraf s n vrcholy a m hranami;
paralelní hrany jsou samostatné prvky indexové množiny E. Smyčka má
dvě incidence v jednom vrcholu, jak zadání výslovně říká. p je
prvočíslo, tedy p≥2, a m>(p−1)n. Pro n=0 předpoklad není splnitelný
(žádné dvojice konců a tudíž m=0); v přípustném případě je m≥1.

Nad tělesem F_p zaveďme m samostatných proměnných x_e. Položme
a_{v,e}=0,1,2 podle počtu incidencí e ve v a
g_v=Σ_e a_{v,e}x_e. Pro booleovské x je g_v(x) modulo p přesně
stupeň vrcholu v podgrafu vybraných hran; to zahrnuje i p=2,
kdy se příspěvek smyčky 2 zredukuje na nulu.

Použijeme přesně tištěný polynom

    f(x)=Π_v(1−g_v(x)^(p−1)) − Π_e(1−x_e).

První součin má stupeň nejvýše (p−1)n<m. Druhý má nejvyšší monom
(−1)^m Π_e x_e, a proto má f stupeň přesně m a jeho koeficient
u Π_e x_e je **(−1)^(m+1)**, nenulový v každé charakteristice p.
Tisk zde uvádí (−1)^m: to je F176. Předchozí věta o stupni prvního
součinu potřebuje jen horní mez ≤(p−1)n. Doslovná rovnost může
klesnout, je-li nějaký g_v nulový (izolovaný vrchol; také vrchol
pouze se smyčkami v charakteristice 2). V přesném důkazu ji proto
píšeme jako ≤; tento drobný kvalifikátor je zaznamenán v téže
lokální poznámce, bez další karty nebo dalšího kandidáta.

Převzatá 114/D212 se použije s počtem proměnných m, všemi d_e=1
a S_e={0,1}⊂F_p. I pro p=2 jsou oba body různé. Součet exponentů
je m, právě celkový stupeň, a koeficient je nenulový; všechny
předpoklady jsou tedy splněné. Vzniká booleovské x s f(x)≠0
(dokonce podíl takových x je alespoň 2^(−m)).

## Význam každé hodnoty f na booleovské krychli

Pro a∈F_p je a^(p−1)=0 při a=0 a 1 jinak. Nenulová část plyne
přímo z toho, že násobení a permutuje nenulové prvky tělesa:
a^(p−1)Π_{b≠0}b=Π_{b≠0}b a nenulový součin lze zkrátit.
První součin v f je tedy indikátor, že všechny g_v jsou nula.
Druhý součin je indikátor x=0. V bodě x=0 jsou oba rovny 1,
takže f(0)=0. V ostatních booleovských bodech druhý součin mizí
a f je 1 právě tehdy, když všechny stupně dělí p; jinak je 0.
Proto je každý nalezený nekořen nenulový výběr hran s požadovanou
dělitelností. „Nonempty“ znamená alespoň jednu hranu; nejde jen
o izolované vrcholy. Nulové stupně zbývajících vrcholů jsou povolené.

Nejde o konstruktivní algoritmus pro rozsáhlé grafy. Důkaz má
konečnou krychli a dokládá existenci bez její enumerace. Pro dané
x lze incidence i všechny g_v spočítat v O(m+n) operacích,
případně vyhodnotit původní mocniny v O(n log p) dalších operacích
tělesa opakovaným čtvercováním. Žádný takový běh zde nebyl potřeba.

## Dovětek o p-regularitě a přesná kontextová interpretace

Podmínka „fewer than 2p neighbors“ je zde stupňová podmínka
deg_G(v)<2p, s násobnostmi incidencí. Zadání hned za ní stanoví,
že smyčka přidává ke stupni 2. Původní svazek 4A str. 14 / file31
definuje stupeň počtem sousedů pro jednoduché grafy; str. 19 /
file36 rozšiřuje graf na multigraf a výslovně počítá opakované
hrany i obě incidence smyček. Tyto dva přesné úseky byly zobrazeny;
neuzavírá se celé jejich okolí. Alonův primární Theorem6.1 uvádí
ekvivalentně maximální stupeň ≤2p−1 pro bezsmyčkový případ.

Při tomto kontextovém čtení je každý kladný stupeň získaného H
kladným násobkem p menším než 2p, tedy přesně p. Odstraněním
izolovaných vrcholů dostáváme neprázdný p-regulární podgraf; jako
podgraf nemusí být indukovaný ani rozpínající. Smyčky a paralelní
hrany tento krok nemění, protože odstranění hran stupeň nezvětšuje.

Nezaměňujeme tento předpoklad za počet různých sousedních vrcholů.
Takový odlišný výklad by byl nepravdivý: jediný vrchol se třemi
smyčkami při p=3 má tři hrany>2, ale všechny stupně podgrafů jsou
sudé a žádný není3-regulární. V zamýšleném stupňovém čtení má
však tento vrchol stupeň6 a podmínku <6 nesplňuje. Vzhledem k
výslovné smyčkové konvenci a navazujícímu důkazu jde o vysvětlení
domény, nikoli o nový kandidát či druhý nález.

## Alternativní konvence smyčky z odpovědi

Pokud se smyčka počítá do stupně jen jednou, změníme její
a_{v,e} z2 na1. Ostatní důkaz zůstává doslova platný: g_v je stále
lineární, první součin má stupeň nejvýše(p−1)n, nejvyšší
koeficient f se nezmění a indikátorová interpretace teď zachytí
stupně podle nové konvence. To je celý dodatek odpovědi, včetně
p=2 a pouze smyčkových grafů. Není potřeba předpokládat, že
historický článek používá obě konvence.

## F176: přesný svědek a lokální oprava

Nechť p=3,n=2 a G má pět paralelních hran mezi dvěma vrcholy.
Pak m=5>4 a oba stupně5<6, takže jsou splněny i předpoklady
dovětkové verze. S=Σ_{i=1}^5x_i dává první součin (1−S^2)^2,
stupně4; ten nemůže přispět k x_1x_2x_3x_4x_5. Z odečteného
Π_i(1−x_i) dostáváme koeficient −(−1)^5=1. Tištěná hodnota
(−1)^5=−1=2 vF_3 je odlišná. Oprava je přidat+1 k exponentu.
Obě hodnoty jsou nenulové, proto existence podgrafu zůstává
správná; například libovolné tři z pěti hran tvoří3-regulární
podgraf. Závažnost low, jediná chybová lokace p389/file409.

Pro přesnost stupňového kvalifikátoru lze k tomuto grafu připojit
izolovaný vrchol a vzít sedm paralelních hran: n=3,m=7>6,
první součin má stupeň4, nikoli(p−1)n=6. Použitá nerovnost4<7
samozřejmě platí. Tento doplněk dokládá, proč v důkazu výše stojí
„nejvýše“; samostatný F identifikátor pro něj nevzniká.

## Primární zdroje a errata

Alonův autorův PDF Combinatorial Nullstellensatz, p10, Theorem6.1
a celý příslušný důkaz byly přímo přečteny a zobrazeny. Obsahuje
správný exponent |E|+1 i výslovné „at most“ u stupně prvního
součinu. Prvotní článek Alon–Friedland–Kalai, JCT B37(1984),79–91,
je uložen z autorova seznamu publikací. Původní p79 potvrzuje
metadata i bezsmyčkovou konvenci s povolenými paralelními hranami;
p83 obsahuje Theorem3.1 o dělitelných podgrafech. Potřebná
matematika včetně rozšíření na smyčky je celá dokázána výše;
silnější prvočíselně-mocninné výsledky článku nejsou tvrzením116
a nepřebírají se jako nově zkontrolované.

Šest vrstev errat i tři TeX zdroje zkontrolovány podle MPR116,
současné str.24/389, Pre-Fascicle str.45, publikovaného Fascicle5
str.200/201 a slovních klíčů. Žádná oprava znaménka nalezena.
Opravy116 na Fascicle5p135 jsou jiné zadání o Mycielského grafech;
oprava114 na p200 je už E134. PDF a starý PS mají shodné znaménko.
Fyzický výtisk ani nezávislé přijetí kořenem se netvrdí.

Celá116 je po uvedeném lokálním upřesnění checked. File44 a409
jsou stále partial kvůli následujícím úlohám, jejich přečtení
v tomto kroku neznamená důkazové uzavření.
