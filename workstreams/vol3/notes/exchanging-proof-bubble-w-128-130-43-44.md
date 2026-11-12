# Bubble: celý W rozvoj128–130 a úlohy43–44

2026-11-07. P0969–0983; uzavírá také P0955. Originály128–130,
137/636 zobrazeny. Pět vrstev:
`sources/regularized-sum-upper-limit-errata-review.json` a původní
`sources/exchanging-errata-review.json`. Known2021 znaménko v(33),
pravý endpoint v(36) a odstranění−δ_{k0} v44 jsou zapracovány.
Nový C0028/low se týká jen chybějící konečné meze pomocné rovnosti,
ne výsledku(37). Žádný matematický běh; všechny koeficienty níže
vznikají z explicitních momentů a konečné racionální algebry.

## P0969: definice(31), pořadí příspěvků a přesná(32)

Konečný W_n=(1/n!)Σ_(0≤r<s≤n)s!r^(n−s) je přesně P0952;
konvence0^0=1 je součástí této rovnosti. Pro s<n položme p=n−s≥1.
Každé r^p v s-tém příspěvku je≤(s+1)r^(p−1), a nový člen r=s
v následujícím příspěvku je kladný. Proto s-té příspěvky skutečně
rostou se s; s=n je největší. Argument platí i pro r=0,p=1,
kdy levá hodnota0 není zaměněna s pravou0^0=1.

Substituce m=n+1,t=n−s+1,N=m−t má přesně rozsah1≤t<m,N≥1.
Proto

    W_(m−1)=m Σ_(1≤t<m) (N!/m!) S_t(N),
    S_t(N)=Σ_(0≤r<N)r^(t−1).                            (A)

To dokazuje(32), včetně všech krajních členů a faktoru m.

## P0970: celý mocninný součet(33), znaménka a delta členy

Použijme knižní Bernoulliho konvenci B_1=+1/2. Identita

    Σ_(r=0)^(N−1)e^(rz)=(e^(Nz)−1)/(e^z−1),
    z/(e^z−1)=Σ_(j≥0)(−1)^j B_j z^j/j!

dává porovnáním koeficientu z^(t−1) přesně

    S_t(N)=(1/t)Σ_(j=0)^t binom(t,j)(−1)^j B_j
                         (N^(t−j)−δ_(t,j)).           (B)

To je zároveň algebraický důkaz opraveného(33), bez nevyjádřené
konvence pro B_1. Pro pevná t a počet členů je jeho zbytek
odpovídající polynomový O-člen. Protože později t roste s m,
pro součet(A) potřebujeme navíc následující **jednotnou** mez.
Samotná existence O s konstantou závislou na t by nestačila.

První členy(B) jsou

    N^t/t − N^(t−1)/2 + δ_(t,1)/2
      +(t−1)N^(t−2)/12 − δ_(t,2)/12 + E_t(N).          (C)

Pro t=1,2,3,4 je E_t=0; přímo jde o součty konstant,
prvních mocnin, čtverců a krychlí. Zejména delty ruší
nepatřičný−1/2 při t=1 a+1/12 při t=2.

## P0971: jednotný zbytek mocninného součtu

Pro t≥5 aplikujme Eulerův součet na x^(t−1) do čtvrté derivace.
Člen s B_4 a absolutní mez integrálního zbytku mají dohromady
velikost nejvýše konstanty krát

    (t−1)(t−2)(t−3) N^(t−4).

Pro integrál se použije
∫_0^N |(d/dx)^4 x^(t−1)| dx
=(t−1)(t−2)(t−3)N^(t−4); konstanty periodických Bernoulliho
polynomů jsou pevné. Tedy jednotně pro N≥1

    |E_t(N)|≤C t³ N^(t−4), t≥5.                      (D)

V lokálním pásu N≥m/2 se po násobení mN!/m! tento zbytek
v celém W odhadne pomocí R_m(t)=N!N^t/m! jako

    O(m^(−3) Σ_t t³ e^(−t²/(2m)))=O(m^(−1)).          (E)

Gaussian momentový odhad i oprávněnost vynechání zbytku pásu
jsou doloženy hned níže. Jde o menší chybu než požadované m^(−1/2).

## P0972: celý ocas(34) a jeho skutečný exponenciální řád

Pro každé celé1≤t<m platí přesný součin

    R_m(t)=∏_(i=0)^(t−1) (m−t)/(m−i)
          ≤exp(−t(t+1)/(2m)).                         (F)

Použili jsme log(1−x)≤−x a(m−i)≤m. Navíc monotonie
x^(t−1) dává S_t(N)≤N^t/t, i při t=1. Tím je příspěvek
původního nezáporného součtu W omezen mR_m(t)/t.

Zvolme pevné ε=1/24 a T=m^(1/2+ε). Pro t>T je součet
příspěvků W i každé pevné polynomové váhy v(34) omezen
polynomem v m krát exp(−m^(2ε)/2). To je O(exp(−m^δ))
například pro δ=ε; nevynechává se polynom při zachování
stejného exponentu. Všechny tyto ocasy jsou menší než libovolná
pevná záporná mocnina m. Tak je doložena přesná zanedbatelnost
použitá v textu, nikoli pouhý bodový odhad jednotlivého sčítance.

Pro pevné a≥0 platí

    Σ_(t≥1) t^a e^(−t²/(2m))=O(m^((a+1)/2)).          (G)

Rozdělíme součet u maxima funkce x^a e^(−x²/(2m)); každá
monotónní část se omezuje integrálem a jedním maximálním členem.
Integrál po substituci x=√m y má uvedený řád, maximální člen
je O(m^(a/2)). Pro váhu t^(−1) je součet O(log m), rozdělením
u√m na harmonický počátek a integrálně omezený Gaussian ocas.
Tyto meze ospravedlňují(E) a všechna další sčítání zbytků.

## P0973: celý vytištěný Stirlingův krok

V pásu t≤T je N=m−t≥m/2 pro dost velká m. Uniformní
Stirlingův vzorec pro log faktoriálu s chybou O(N^(−3)) dává

    log R_m(t)=(m+1/2)log(1−t/m)+t
                  +1/(12(m−t))−1/(12m)+O(m^(−3)).

Oddělíme(1/2)log(1−t/m). Zbývající logaritmus rozvineme
do páté mocniny t/m, a 1/(m−t) do prvního nenulového rozdílu:

    R_m(t)=√(1−t/m) exp[ t/(12m²)
      −t²/(2m)−t³/(3m²)−t⁴/(4m³)−t⁵/(5m⁴)
      +O(t²/m³+t⁶/m⁵+m^(−3)) ].                     (H)

Protože t≤m^(1/2+ε), tento poslední zbytek je
O(m^(−2+6ε)), právě jak uvádí129. Koeficienty−1/3,−1/4,
−1/5 pocházejí z m log(1−t/m), nikoli z aproximace párového
součinu nezávislými členy. Uniformní platnost umožňuje pozdější
součet; konečný počet malých m nemá na asymptotické tvrzení vliv.

## P0974: Eulerův vzorec(36) a odhad jeho zbytku

Položme h=1/√(2m), g_k(x)=x^k e^(−x²), f_k(x)=g_k(hx),
nejprve pro pevné celé k≥0. S B_1=+1/2 je správná pravá
endpointová forma

    Σ_(0<t≤m)f(t)=∫_0^m f(x)dx
       +Σ_(j=1)^p B_j/j! [f^(j−1)(m)−f^(j−1)(0)] + R_p,
    R_p=(−1)^(p+1)/p! ∫_0^m B_p({x}) f^(p)(x)dx.      (I)

Toto je přesně known oprava2021; pro původní Σ_(0≤t<m)
by znaménko endpointového1/2 členu bylo opačné.

Je důležité skutečně doložit R_p=O(h^p) uvedené v textu.
Samotná absolutní mez po změně proměnné by dala jen
O(h^(p−1)), protože dx=dy/h. Použijeme navíc omezenou
periodickou primitivní funkci B_(p+1)({x})/(p+1): integrací
po částech je R_p součet endpointů f^(p) a integrálu proti
f^(p+1). Endpointy jsou O(h^p), zatímco

    ∫_0^m |f^(p+1)(x)|dx
       =h^p ∫_0^(mh)|g^(p+1)(y)|dy=O(h^p).

Gaussian krát polynom má všechny potřebné derivace omezené
a integrabilní. Tím je silnější závěr(36) opravdu prokázán;
chybějící Jacobian v naivním absolutním odhadu se nepřeskočil.
Pro pevná k,p lze výsledek zapsat i s konstantou násobící
∫|g_k^(p)|, jak činí text, ale rozhodující je tato dodatečná
periodická integrace. Nejde o nový nepravdivý výsledný odhad.

## P0975: všechny koeficienty Gaussian r_k, opravená odpověď44

Pro t≥m jsou sčítance r_k omezeny polynomem krát e^(−m/2);
odstranění této hranice tedy nemění žádný algebraický člen.
Integrál přes[0,∞) je

    ∫_0^∞ x^k e^(−x²/(2m))dx
      =(1/2)(2m)^((k+1)/2) Γ((k+1)/2).

Taylorova řada v nule je
x^k e^(−x²/(2m))=Σ_(j≥0)(−1)^j x^(k+2j)/(j!(2m)^j).
Dosazením všech nenulových endpointových derivací do(I)
dostaneme pro pevné celé k≥0 asymptotickou řadu

    r_k(m) ~ (1/2)(2m)^((k+1)/2) Γ((k+1)/2)
       −Σ_(j≥0) (−1)^j B_(k+2j+1)
                    /[(k+2j+1) j! (2m)^j].          (J)

Pro k=0 její první člen−B_1=−1/2 již zahrnuje endpoint.
Nesmí se přidat další−δ_{k0}, jak správně opravuje erratum2021.
Pro sudá k>0 jsou všechny zobrazené Bernoulliho korekce nulové;
pro lichá k je generují příslušné liché derivace. Zbytek po
libovolném pevném počtu členů se zajistí volbou vyššího p v(I),
protože násobení h^(−k) změní R_p na O(h^(p−k)). Symbol∼
znamená rozvoj po konečných truncacích, nikoli konvergenci
nekonečné Bernoulliho řady.

Zvlášť budeme používat

    r_0=√(2πm)/2−1/2+O(m^(−2)),
    r_1=m−1/12+O(m^(−1)),
    r_2=(m/2)√(2πm)+O(m^(−1)),
    r_3=2m²+O(1),  r_5=8m³+O(1).                  (K)

Všechny gamma momenty vznikají z Γ(1/2)=√π a Γ(z+1)=zΓ(z),
jejichž uzavřený důkaz se přebírá ze svazku1. Není potřeba
numerické aproximace Gaussian integrálů.

## P0976: odstranění singularity a celá úloha43

Původní g_(−1)=e^(−x²)/x je v nule singularní. Pouhá změna
spodní meze na1 nevytváří asymptotickou hierarchii absolutních
Eulerových zbytků: derivace normalizované funkce
e^(−x²/(2m))/x na[1,2] konvergují pro m→∞ k derivacím1/x,
jejichž L¹ normy jsou nenulové pro každý pevný řád.

Nahradíme ji g(x)=(e^(−x²)−1)/x, g(0)=0. V nule je
analytická, g(x)=Σ_(j≥1)(−1)^j x^(2j−1)/j!;
v nekonečnu g^(p)(x)=O(x^(−p−1)) pro p≥1. Proto má
všechny derivace potřebné pro(I) a pro jeho silnější odhad
integrabilní, ačkoli samotné g v nekonečnu integrabilní není.

P0924 už nezávisle dokázal přesně
∫_0^1(e^(−y)−1)/y dy+∫_1^∞e^(−y)/y dy=−γ;
jeho argument s H_N−ln N a dominovanou konvergencí se
neopakuje. Zkontrolovat lze i vlastní nabízené řešení43:
pro a>0 je součet obou integrálů s váhou y^(a−1)
Γ(a)−1/a=(Γ(a+1)−1)/a. Při0<a≤1 je první integrand
absolutně≤1 na(0,1) a druhý≤e^(−y) na(1,∞), takže
limitu lze přenést dovnitř. Ze stejnoměrně konvergentního
gamma součinu v `workstreams/vol1/notes/gamma-functions.md`
plyne Γ'(1)=−γ: jeho logaritmická derivace v1 je
−1−γ−Σ_(j≥1)(1/(j+1)−1/j)=−γ. To ověřuje i tento
konkrétní odkaz a mezikrok tištěné odpovědi43.

Pro f(x)=g(hx) a A=m/2 pak přesná substituce y=x²/(2m)
dává

    2h∫_0^m f(x)dx
       =∫_0^A(e^(−y)−1)/y dy
       =−γ−ln A−E_1(A).

Platí0<E_1(A)≤e^(−A)/A. Pro m≥2 je tedy zbytek skutečně
O(e^(−m/2)), jak píše130; jeho případný polynomový faktor
zde **klesá**, nikoli roste. Jsou ověřeny všechny rovnosti
a velikost zbytku tohoto integrálního kroku.

## P0977: všechna endpointová zrušení a řada r_(−1)

Aby byla konvence(I) zcela průhledná, nejprve připojme poslední
Gaussian člen a označme

    S_m=Σ_(t=1)^m e^(−t²/(2m))/t
       =H_m+hΣ_(t=1)^m f(t).                         (L)

Od původního r_(−1)(m) se liší jen e^(−m/2)/m. Eulerův
rozvoj H_m, získaný z téže formule pro1/x a definiceγ, je

    H_m ~ ln m+γ+1/(2m)−Σ_(j≥1)B_(2j)/(2j m^(2j)).

Horní endpointy h f(m) a h f^(2j−1)(m), po zanedbání
exponenciálně malých Gaussian členů, jsou−1/m a
(2j−1)!/m^(2j), protože h f(x)=(e^(−x²/(2m))−1)/x.
Proto člen h f(m)/2 zruší+1/(2m) v H_m a každý horní
Eulerův člen zruší právě odpovídající záporný Bernoulliho
člen harmonického rozvoje. To dokazuje tvrzené zrušení
v odpovědi44 po jednotlivých řádech, nikoli jen první z nich.

Dolní endpoint f(0)=0. Z Taylorovy řady g plyne

    h f^(2j−1)(0)
       =(−1)^j (2j−1)!/[j!(2m)^j].

Po jejich odečtení a přičtení integrálu z P0976 tedy

    r_(−1)(m) ~ (ln(2m)+γ)/2
       −Σ_(j≥1)(−1)^j B_(2j)/[2j j!(2m)^j].         (M)

Pro každý požadovaný konečný řád lze v(I) zvolit tak vysoké p,
že hR_p=O(h^(p+1)) je menší. Zbytek H_m lze nezávisle omezit
integrálem vyšší derivace1/x od m do∞. Upper Gaussian endpointy
mají jen polynomový násobek e^(−m/2). Tím je zdůvodněn celý
asymptotický, nikoli jen formální rozvoj. Pro výpočet konstanty
stačí zvlášť

    r_(−1)(m)=(ln(2m)+γ)/2+1/(24m)+O(m^(−2)).         (N)

## P0978: přesná rovnost636 musí mít konečnou mez

Předchozí správná(L), nebo ekvivalentně
r_(−1)(m)=H_(m−1)+hΣ_(0<t<m)f(t), má konečnou horní mez.
V odpovědi636 je místo ní Σ_(t>0)f(t). Protože h f(t)
je(e^(−t²/(2m))−1)/t, jeho nekonečný součet diverguje
záporně jako harmonická řada. Platný m=2 už dává přímý
rozpor s konečným r_(−1)(2)=e^(−1/4). Celý krátký důkaz,
opravná mez a pět vrstev jsou v
`notes/V3-C0028-regularized-sum-upper-limit.md`.
**C0028 confirmed/low**; asymptotiky(J),(M),(37) jsou naopak
doloženy se správnou konečnou identitou.

## P0979: vážené rozvinutí R_m a celková chyba O(m^(−1/2))

Pišme G=e^(−t²/(2m)), x=t/m, a=t³/(3m²), b=t⁴/(4m³).
Pro t≤T z(H), Taylorových vzorců s omezenými zbytky a
našeho pevného ε plyne

    R_m(t)=G(1−a+a²/2)(1−b)(1−x/2−x²/8)+G E_m(t),

kde absolutní E_m(t) je omezen konstantou krát

    t³/m³ + t⁹/m⁶ + t⁸/m⁶ + t/m²
      +t⁵/m⁴ + t²/m³ + t⁶/m⁵ + m^(−3).             (O)

První člen je zbytek odmocniny; druhý zbytek e^(−a);
třetí zbytek e^(−b); t/m² je vypuštěná Stirlingova korekce,
t⁵/m⁴ další logaritmický člen a poslední tři pocházejí
z uniformního zbytku(H). V pásu jsou a,b,x malé a ostatní
faktory omezené, takže součiny těchto odhadů neztrácejí
jednotnost. Lze použít i |e^(−a)−1+a−a²/2|≤a³/6 pro a≥0.

Po násobení největší relevantní vahou m/t a sečtení dávají
členy(O), podle(G), postupně řády

    m^(−1/2), m^(−1/2), m^(−1), m^(−1/2),
    m^(−1/2), m^(−1), m^(−1), O(m^(−2)log m).

Proto celkový zbytek je O(m^(−1/2)). Přechod z t≤T na všechny
kladné t v jednotlivých **Gaussian polynomech** je oprávněn
P0972; neprovádí se u regularizovaného harmonického součtu.
Vyšší součiny v rozepsaném polynomu, které níže nejsou ponechány,
se stejným způsobem omezí O(m^(−1/2)); nejnižší z nich mají
váhy r_4/m³ nebo r_6/m⁴. Tím je doložen absolutní zbytek,
nikoli jen bodové pořadí malých veličin v jednom sčítanci.

## P0980: celý příspěvek N^t/t včetně konstanty4/9

Z prvního členu(C) plyne W příspěvek mΣR_m(t)/t. Rozepsání
předchozího součinu a zachování všech členů, které mohou být
alespoň konstantní, dává

    m r_(−1) −r_0/2 −r_2/(3m) −r_1/(8m)
       −r_3/(12m²)+r_5/(18m³) +O(m^(−1/2)).          (P)

Koeficient−1/12 u r_3 je součet−1/4 z b a+1/6 z a·x/2.
Použitím(K),(N) jsou odmocninové členy
−√(2πm)/4−√(2πm)/6=−5√(2πm)/12. Konstanty jsou

    1/24+1/4−1/8−1/6+4/9=4/9.

Celý příspěvek tedy je

    (m/2)ln m +(ln2+γ)m/2 −5√(2πm)/12 +4/9
       +O(m^(−1/2)),

přesně jak tvrdí odpověď44. Zvlášť konstantu1/24 nelze
získat pouze z hlavního logaritmického členu r_(−1).

## P0981: celý příspěvek−N^(t−1)/2

Z(A),(C) je tento příspěvek−(m/2)ΣR_m(t)/(m−t).
Pro konstantní přesnost stačí

    m/(m−t)=1+t/m+O(t²/m²),
    R_m(t)=G(1−a)(1−x/2)+zbytek.

Vyřazené x²,b,a²,a·x mají po sečtení bez váhy m/t
nejvýše O(m^(−1/2)), opět z(G). Výsledek je tudíž

    −r_0/2 +r_3/(6m²)−r_1/(4m)+O(m^(−1/2))
       =−√(2πm)/4+1/3+O(m^(−1/2)).                 (Q)

Konstanta je+1/4+1/3−1/4=1/3. Známá historická oprava
tohoto konstantního členu je v našem tisku již zohledněna.

## P0982: oba delta členy, příspěvek B_2 a zbývající řády

Člen+δ_(t,1)/2 dává přesně
m(m−1)!/(2m!)=1/2. Člen−δ_(t,2)/12 dává
−1/[12(m−1)]=O(1/m), proto jej odpověď správně nemusí
samostatně uvádět v konstantě. Zbytek(D) je O(1/m) podle(E).

Člen(t−1)N^(t−2)/12 dává

    (m/12)Σ R_m(t)(t−1)/(m−t)²
       =(1/(12m))Σ tG +O(m^(−1/2))
       =1/12+O(m^(−1/2)).                           (R)

Zde nahrazení t−1 za t stojí O(r_0/m), nahrazení
(1−t/m)^(−2) za1 stojí O(r_2/m²) a nahrazení R_m zaG
stojí O(r_2/m²+r_4/m³); všechny jsou O(m^(−1/2)).
Tím jsou doloženy všechny vytištěné čtyři příspěvky odpovědi44,
i nevytištěné části, které musely skončit ve zbytku.

## P0983: součet(37) a úplné uzavření jemného Cave(12)

Sečtením(P),(Q),(R) a delta1 příspěvku dostaneme

    W_n=(m/2)ln m +(γ+ln2)m/2
          −(2/3)√(2πm)+49/36+O(m^(−1/2)), m=n+1.

Koeficient odmocniny je−5/12−1/4=−2/3; konstanta je
4/9+1/3+1/2+1/12=49/36. Protože m=n+1, oba uvedené
řády O(m^(−1/2)) a O(n^(−1/2)) jsou ekvivalentní.
Známá první-edice oprava31/36→49/36 se nepočítá jako nález.

Konečné E C=n(n+1)/2−W_n z P0952 a
(n+1)ln(n+1)=n ln n+ln n+1+O(1/n) pak dávají

    E C=1/2[n²−n ln n−(γ+ln2−1)n]+O(√n).

Všechny další členy, včetně√n a ln n, se skutečně vejdou
do tohoto absolutního zbytku. **P0955 je tím checked**:
lineární koeficient i deklarovaný řád chyby mají obecný důkaz.
Žádný závěr o úplných průměrech cocktail-shaker sortu nebo
dosud nezkontrolovaném radixovém pokračování z tohoto rozvoje
nevyplývá; příslušné samostatné mezery zůstávají otevřené.
