# MPR 119: oba důkazy rovnoměrného mediánu, včetně všech integrálů

D217, 7. listopadu 2026. Zadání p24/file44 a odpověď p389/file409
zobrazeny v původním PDF; autorův PS p24/46,file30/52 také.
Žádný nález, kandidát, výpočet ani restart. Jedna úzká bibliografická
výjimka se týká pouze autorství Terpaiova důkazu.

## Doména, události a přesný význam výsledku

Parametr x∈[0,1] je pevný. U,V,W jsou nezávislé, s rovnoměrnými
zákony na[0,x],[x,1],[0,1]. Na jednoprvkovém intervalu jde o
konstantní proměnnou. Nejprve0<x<1, takže společná hustota je
c=1/[x(1−x)] na příslušném kvádru. Protože U≤x≤V, existují
až na nulové rovnosti jen tři pořadí:

1. U<V<W: A=U,M=V,Z=W;
2. U<W<V: A=U,M=W,Z=V;
3. W<U<V: A=W,M=U,Z=V.

Vždy A≤x≤Z a A<Z skoro jistě. Výsledek doložíme i v silném
smyslu: podmíněně na A=a,Z=z je M rovnoměrné na[a,z], pro
téměř všechny(a,z). Veličina T=(M−A)/(Z−A) je pak uniformní
na[0,1] a nezávislá na(A,Z).

První tištěný výpočet ověřuje přímo marginální CDF T. Jeho
f(x,t),g(x,t),h(x,t) jsou příspěvky uvedených tří pořadí
s podmínkou T≤t. Jejich součet je tedy P(T≤t). Samotný
marginální výpočet by nedokládal nezávislost na(A,Z); úplnou
podmíněnou verzi dokazuje níže druhý argument, včetně přesných
vah směsi. Rozdíl těchto dvou rozsahů není skrytý.

## Každý reflexní krok

Celková pravděpodobnost třetího pořadí je
P(W≤U)=EU=x/2. Při transformaci
U'=1−V,V'=1−U,W'=1−W dostaneme stejnou konstrukci pro
x'=1−x, stále s nezávislostí. Třetí pořadí se změní na první
a T se změní na1−T. Proto

    x/2−h(x,t)=f(1−x,1−t).

To je přesně tištěná rovnost, s přeznačením dvou koncových
proměnných. Doplňující rovnost je
(1−x)/2−f(x,t)=h(1−x,1−t), neboť první pořadí má
pravděpodobnost P(W≥V)=1−EV=(1−x)/2.

Rovnost na prahu nemá kladnou pravděpodobnost: při pevných
u<v a0<t<1 událost T=t určuje v každém pořadí nejvýše
jednu hodnotu spojitého W. Pro t=0 nebo1 by musela nastat
shoda dvou ze tří hodnot, opět nulová. Reflexe tedy pro celou
CDF dává F_x(t)=1−F_{1−x}(1−t). Je-li t>x, pak1−t<1−x,
takže opravdu stačí spočítat oblast0≤t≤x. Tím je odůvodněno
tištěné zkrácení případu; nestačí ho pouze prohlásit za symetrii.

## Výpočet g: prostřední W

Pro pevné u,v je požadovaný interval W od u do u+t(v−u).
Leží v[u,v] pro0≤t≤1 a má délku t(v−u). Proto

    g(x,t)=∫_0^x du/x ∫_x^1 dv/(1−x) t(v−u)
          =t(EV−EU)=t((1+x)/2−x/2)=t/2.

Všechny integrandy jsou nezáporné, omezené a integrační oblasti
konečné; pořadí integrací je tedy oprávněné.

## Výpočet f: všechny meze i konečné vyhodnocení

Pro0<t≤x<1 a U=u,V=v musí platit
v≤(1−t)u+tW. Tedy W≥[v−(1−t)u]/t; tato dolní mez je
alespoň v, protože v≥u. Je nejvýše1 právě tehdy, když
v≤(1−t)u+t. Jelikož v≥x, přípustné u leží mezi
a=(x−t)/(1−t) a x; zde0≤a≤x. To dává právě tisk

    f(x,t)=∫_a^x du/x ∫_x^((1−t)u+t) dv/(1−x)
                                      [1−(v−(1−t)u)/t].

Položme b=(1−t)u+t−x. Vnitřní integrál je
b²/[2t(1−x)], neboť integrand v čitateli je
[(1−t)u+t−v]/t. Při u=a je b=0, při u=x je
b=t(1−x) a du=db/(1−t). Proto

    f = [t(1−x)]³/[6tx(1−x)(1−t)]
      = t²(1−x)²/[6(1−t)x].

Pro t=0 je událost bez rovností nemožná a f=0 přímo;
nepoužije se mezikrok dělící t. V oblasti0<t≤x<1
jsou všechny ostatní jmenovatele kladné.

## Výpočet h: rozdělení podle tv a oba integrály

Při pevných u,v má třetí pořadí W∈[0,u] a podmínka
u≤(1−t)W+tv požaduje W≥(u−tv)/(1−t). Délka intervalu
je tedy u, když u≤tv, a t(v−u)/(1−t), když u≥tv.
Protože t≤x a v≤1, je tv≤x pro každé integrační v.
Tištěné rozdělení v bodě tv je tak vždy uvnitř intervalu[0,x]:

    h=∫_x^1 dv/(1−x) [∫_0^(tv) u du/x
                     +∫_(tv)^x t(v−u)du/((1−t)x)].

Výraz v hranaté závorce se vyhodnotí na

    t/[x(1−t)] [vx−x²/2−tv²/2].

Opravdu první integrál přispívá t²v²/(2x); druhý je
t/[x(1−t)] [vx−x²/2−tv²+t²v²/2]. Po společném
jmenovateli se krychlové členy v t zruší a vznikne uvedený
výraz. Nyní EV=(1+x)/2 a EV²=(1+x+x²)/3 pro V uniformní
na[x,1], takže

    h=t/[x(1−t)] [x/2−t(1+x+x²)/6]
     =t/2−t²(1−x)²/[6x(1−t)]
     =t/2−f(x,t).

Poslední rovnost plyne také přímým sjednocením jmenovatelů:
čitatel obou zápisů je3tx−t²(1+x+x²). Tudíž
f+g+h=t na0≤t≤x a reflexe dává všechny t∈[0,1].
Vně[0,1] je CDF0 nebo1 z definice T. Všechny tištěné
integrály, přepnutí mezí a algebraické kroky jsou tím ověřeny.

## Druhý důkaz: úplná společná hustota a přesné váhy

Zafixujme0<a<x<z<1. Prostor(a,m,z) vzniká ve třech pořadích
jen permutací původních souřadnic, s absolutním Jacobianem1:

- (U,V,W)=(a,z,m) pro a<m<z;
- (U,V,W)=(a,m,z) pro x<m<z;
- (U,V,W)=(m,z,a) pro a<m<x.

Každá větev přispívá hustotou c. Pro a<m<x jsou přítomny
první a třetí větev, pro x<m<z první a druhá. Celková
hustota(A,M,Z) je proto konstantní2c na a<m<z, pro
0<a<x<z<1. Hraniční rovnosti mají nulovou míru.

Integrací přes m dostaneme hustotu(A,Z) rovnou2c(z−a).
Je správně normalizovaná, protože
∫_0^x da∫_x^1(z−a)dz=x(1−x)/2. Podíl společné
a marginální hustoty je tedy1/(z−a). To přesně dokazuje
požadovaný podmíněný rovnoměrný zákon; nepodmiňuje se
obyčejným podílem pravděpodobností nulových bodových událostí.

Integrály jednotlivých větví přes m jsou
c(z−a),c(z−x),c(x−a). Jejich podmíněné váhy jsou proto
přesně tištěné

    (z−a,z−x,x−a)/(2z−2a).

První složka je uniformní na[a,z], druhá na[x,z], třetí
na[a,x]. Po vynásobení příslušnými vahami přispívá první
hustotou1/[2(z−a)] na celém intervalu; druhá a třetí
se skládají do stejné hustoty na jeho dvou částech.
Součet je1/(z−a). Pouhé neupřesněné míchání uniformních
zákonů obecně uniformitu nezaručuje; zde správnost zajišťují
tyto skutečné váhy, které byly přímo vypočteny.

Pro0≤t≤1 podmíněná pravděpodobnost M≤a+t(z−a) je t.
Proto pro každou měřitelnou množinu B dvojic(A,Z) platí
P(T≤t,(A,Z)∈B)=tP((A,Z)∈B): T je opravdu uniformní
a nezávislé na koncích. V žádném kroku se netvrdí, že by
samotné M bez normalizace muselo být uniformní na[0,1].

## Oba krajní parametry x

Při x=0 je U=0, A=0 a V,W jsou nezávislé uniformní
na[0,1]. Jejich uspořádaná dvojice(M,Z) má hustotu2
na0<m<z<1, protože dva opačné původní pořadové obory
mají každý hustotu1. Marginální hustota Z je2z a
podmíněná hustota M při Z=z je1/z na[0,z]. To je celý
výsledek bez dělení x. Z>0 skoro jistě.

Při x=1 je V=1, Z=1 a(A,M) jsou uspořádané dva
nezávislé uniformní body U,W. Společná hustota2 na
0<a<m<1 má marginální hustotu A rovnou2(1−a),
takže podmíněný zákon M je uniformní na[a,1]. A<1
skoro jistě. Oba případy zahrnují T=0/1 jako nulové
události a netrpí neurčitým podílem Z−A=0.

## Prameny, výjimka a rozsah

Volkovův primární autorský článek je uložen z arXiv1112.0932.
V důkazu Theorem5, str.17 a první odstavec str.18, byl
přímo přečten a zobrazen přesně příslušný výpočet relativní
polohy tří bodů. Definice na str.14 dávají jeden uniformní
bod v[0,x], druhý v[x,1] a třetí v[0,1]; přejmenování
nezávislých uniformních parametrů jejich zákon nemění.
Metadata autora, RSA43(2013),115–130 a DOI10.1002/rsa.20454
potvrzuje primární univerzitní záznam Lund/Bristol.
Celý dynamický konvergenční výsledek Theorem5 není úlohou119
a neuzavírá se zde; potřebný statický výpočet má úplný důkaz výše.

Jediná bibliografická výjimka: nezávislý historický doklad
autorství kratšího důkazu Tamásem Terpaiem nebyl rychle
dostupný. Tištěné připsání je zachováno jako autorovo sdělení,
nikoli nezávisle potvrzená priorita. Samotný důkaz je plně
ověřen a tato výjimka není matematickou mezerou.

Šest vrstev errat a tři TeX zdroje byly prohledány podle
úlohy, současné i fasciklové stránky, mediánu a jmen.
Použitelná oprava119 nenalezena. Celá119 je checked;
file44 zůstává partial pro120–122 a file409 pro120.
