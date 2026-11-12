# MPR19(d): úplný důkaz transcendentnosti paritního čísla

6. listopadu 2026. Tento důkaz uzavírá matematické tvrzení v odpovědi
na p373, bez převzetí nepročteného důkazu nebo opravy z roku 1930.
Neřeší otevřenou Eulerovu poznámku v části (e). Neobsahuje numerický běh.

Položme

    F(z) = ∏_{j≥0}(1−z^{2^j}),       |z|<1,
    β = F(1/2).

Dokážeme, že β je transcendentní. V hlavní poznámce je přesně odvozeno
ER=1/2−β/4, takže tím je dokázána i transcendentnost ER.

## 1. Existence, koeficienty a funkční rovnice

Na každém uzavřeném kruhu |z|≤r<1 konverguje součet ∑r^{2^j}.
Pro konečný ocas součinu platí

    |∏(1+w_j)−1| ≤ ∏(1+|w_j|)−1 ≤ exp(∑|w_j|)−1.

Proto součiny konvergují lokálně stejnoměrně; jejich limita je analytická.
Konečný součin pro j<k má koeficient při z^n, 0≤n<2^k,
rovný (−1)^{ν(n)}, kde ν(n) je počet jedniček v binárním zápisu n.
Důvod je jednoznačné vyjádření n jako součtu různých mocnin dvou.
Lokální stejnoměrná konvergence proto dává

    F(z)=∑_{n≥0}(−1)^{ν(n)}z^n,
    F(0)=1,
    F(z)=(1−z)F(z²).

Řada také přímo konverguje absolutně pro |z|<1, neboť její koeficienty
mají velikost 1. Pro reálné 0<t<1 je F(t)>0: vyberme J tak velké,
že ∑_{j≥J}t^{2^j}<1/2. Indukce na počtu faktorů dává
∏_{j≥J}(1−t^{2^j})≥1−∑_{j≥J}t^{2^j}>1/2. Předchozí konečný
součin je kladný. Zvláště β≠0.

## 2. Funkce F není algebraická nad C(z)

Předpokládejme opak. Po odstranění jmenovatelů existuje nenulový
Q(z,u)∈C[z,u] s Q(z,F(z))=0. Vydělíme nejvyšší společnou mocninu u
všech členů Q. Protože F není identicky nulová, dostaneme opět vztah,
ale nyní je Q(z,0) nenulový polynom.

Nechť ζ je libovolný kořen jednotky řádu dělícího 2^s. Iterováním
funkční rovnice, pro 0<r<1,

    F(rζ)=∏_{j<s}(1−r^{2^j}ζ^{2^j}) · F(r^{2^s}).

První faktor má velikost nejvýše 2^s. Druhý leží v intervalu
0<F(r^{2^s})≤1−r^{2^s}, protože všechny jeho ostatní faktory leží
v (0,1). Tedy F(rζ)→0 při r↑1. Ze spojitosti polynomu Q plyne
Q(ζ,0)=0. Takových různých ζ je nekonečně mnoho; nenulový polynom
Q(z,0) jich nemůže mít nekonečně mnoho. Spor.

Tento krok nevyžaduje analytické pokračování F přes jednotkovou
kružnici. Bere pouze radiální limity, jejichž existenci jsme dokázali.

## 3. Pomocný polynom s vysokým řádem nuly

Pro spor předpokládejme, že β je algebraická stupně d≥1. Nechť
H(u)∈Z[u] je její primitivní ireducibilní polynom, s vedoucím
koeficientem a≠0 a různými kořeny β₁=β,β₂,…,β_d. Různost kořenů
plyne z charakteristiky nula: společný dělitel H a H′ by jinak
porušoval ireducibilitu a nižší stupeň H′.

Zvolme N=2d a M=(N+1)²−1=N²+2N. Polynom

    Q(z,u)=∑_{0≤i,j≤N} c_ij z^i u^j

má (N+1)² neznámých koeficientů. Požadavek, aby prvních M koeficientů
řady Q(z,F(z)) bylo nulových, je homogenní soustava M lineárních
rovnic nad Q; koeficienty F jsou celá čísla. Má tedy nenulové racionální
řešení. Po násobení společným jmenovatelem lze vzít c_ij∈Z,
ne všechny nulové.

Podle kroku 2 není G(z)=Q(z,F(z)) identicky nulová. Má tedy v nule
konečný řád nuly nejméně M. Z její konvergentní Taylorovy řady existují
C>0 a δ>0 tak, že pro 0<z<δ

    0<|G(z)|≤C z^M.

Nenulovost zde není formální domněnka: po vyjmutí první nenulové
mocniny z má zbývající analytická funkce nenulovou hodnotu v nule,
a proto je nenulová v dostatečně malém okolí.

## 4. Přenesení malého argumentu zpět k β

Pro k≥0 označme

    q_k=2^{2^k},
    A_k=2^{2^k−1}=q_k/2,
    D_k=∏_{j<k}(2^{2^j}−1),       D₀=1.

Iterace funkční rovnice dává přesně

    F(1/q_k)=β A_k/D_k,

protože ∏_{j<k}2^{2^j}=2^{2^k−1}=A_k. Platí 1≤D_k≤A_k≤q_k.
Definujme

    R_k(u)=q_k^N D_k^N Q(1/q_k, u A_k/D_k).

Jde o polynom v Z[u] stupně nejvýše N: každý jeho člen je

    c_ij q_k^{N−i} D_k^{N−j} A_k^j u^j,

a všechny exponenty jsou nezáporné. Pro dost velké k je

    0<|R_k(β)|≤C q_k^{2N−M}.

Pro každý další pevný kořen β_σ existuje konstanta C_σ nezávislá na k,
pro niž |R_k(β_σ)|≤C_σ q_k^{2N}. To plyne z předchozího konečného
rozvoje: každý koeficientní člen má velikost nejvýše
|c_ij|q_k^{2N−i} a počet členů je pevný.

## 5. Celočíselný resultant dává spor

Použitá elementární vlastnost resultantu je následující. Pro
H,R∈Z[u], deg H=d, deg R=m a vedoucí koeficient H rovný a je

    Res(H,R)=a^m ∏_{σ=1}^d R(β_σ).

Je to celé číslo, protože je determinantem Sylvesterovy matice
s celočíselnými položkami. Uvedený součinový vzorec vzniká rozkladem
H=a∏(u−β_σ) a linearitou determinantu, případně postupným použitím
Res(u−β_σ,R)=R(β_σ). Je nenulový právě tehdy, když H a R nemají
společný kořen: nulový determinant je ekvivalentní netriviální
polynomiální relaci U H+V R=0 s deg U<m, deg V<d, tedy společnému
děliteli; totéž plyne přímo ze součinového vzorce.

Protože R_k(β)≠0 a H je ireducibilní nad Q, nemají H a R_k společný
dělitel. Resultant je nenulové celé číslo, tedy má absolutní hodnotu
nejméně 1. Na druhé straně předchozí odhady, s m=deg R_k≤N, dávají

    1 ≤ |Res(H,R_k)| ≤ C′ q_k^{2Nd−M}.

Konstanta C′ nezávisí na k; faktor |a|^m je omezen číslem
max(1,|a|)^N. Jelikož N=2d, máme M=4d²+4d>2Nd=4d².
Pravá strana jde k nule. To je spor.

β je tedy transcendentní. Kdyby ER=1/2−β/4 bylo algebraické,
bylo by β=2−4ER rovněž algebraické, takže ER je transcendentní také.

## Rozsah a historické prameny

V původním Mahlerově článku byly zobrazeny titulní metadata, p342,
p343 a p366. Na p343 je právě produkt F a jeho funkční rovnice.
Celý historický důkaz nebyl převzat. Oprava Math. Ann. 103 (1930),
532 je ověřena pouze v metadatech vydavatelské reedice, nikoli v
originálním znění; zůstává bibliografickou výjimkou. Tento soubor
obsahuje vlastní úplný speciální důkaz pro argument 1/2.

Prameny: [originální sken z Mahlerova archivu](https://carmamaths.org/resources/mahler/docs/004.pdf),
[metadata vydavatelské reedice](https://ems.press/books/dms/252/4968).
Lokální metadata a přesný rozsah jsou v
`sources/mpr019-primary-source-manifest.json`. Nejde o tvrzení, že
všechny obecné věty původního článku byly přezkoušeny.
