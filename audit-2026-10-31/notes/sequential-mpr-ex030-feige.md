# D132 — doplněný důkaz optimálnosti a Feigeho dovětku MPR30

Tento dodatek řeší matematické otázky ponechané v knize jako výzkumné
a současně doplňuje nutnost tvaru každého minimalizátoru v30(b).
Výchozím podnětem je §2 práce A. Milojević a B. Sudakov,
[Perfect matchings in hypergraphs and Feige’s inequality,
arXiv:2610.10380v1,7.10.2026](https://arxiv.org/html/2610.10380v1).
Nejde o náš nález chyby v knize z2022. Níže je úplný přezkoušený
argument v rozsahu potřebném pro30, s výslovným důkazem všech
okrajů, směsí, rovnosti a malé hodnoty b. Není přebírána
neověřená Dirichletova či konvexně geometrická věta z červencových prací.
Zbytek článku o hypergrafech se neprohlašuje za zkontrolovaný.

## 1. Konečný dvoubodový model a kladné podmínění

Nejprve nechť nezávislé X₁,…,X_n mají střední hodnotu1 a každá
je buď konstantní1, nebo má dvě konečné hodnoty0≤u_i<1<v_i
s oběma pravděpodobnostmi kladnými. Fixujeme δ>0 a λ=n+δ.
S je jejich součet. Při postupné náhradě některých X_i jejich
nižší hodnotou u_i zůstanou ostatní proměnné nezávislé a nezměněné.
Označme libovolný aktuální součet T, včetně již pevných členů.

Součet všech nižších hodnot a konstant je≤n<λ. Událost, kdy
všechny dosud náhodné proměnné nabudou nižší hodnoty, má kladnou
pravděpodobnost. Proto E_T={T<λ} má vždy kladnou pravděpodobnost;
žádné podmínění v důkazu není na nulové události.
Položme

    p_T=Pr(E_T),  a_T=E(T|E_T),
    r_T=λ−a_T>0,  b_T=ET−a_T≥0.

Poslední nezápornost: na doplňku E_T je T≥λ>a_T, a celkový
průměr je váženým průměrem obou podmíněných průměrů. Je-li
doplněk nulový, b_T=0. Všechny proměnné jsou v tomto konečném
modelu omezené, takže očekávání i kovariance existují.

Nahradíme-li jeden dosud nekonstantní X_i hodnotou u_i, označme
nový součet T_i. Platí T_i≤T a E_T⊆E_{T_i}. Událost E_{T_i}
závisí pouze na ostatních souřadnicích, a je proto nezávislá na X_i.

## 2. Přesný úbytek b a pravděpodobnostní faktor

Rozklad E_{T_i} na E_T a jeho doplněk uvnitř E_{T_i} dává

    E(T|E_{T_i})
      ≥ (p_T/p_{T_i})a_T+(1−p_T/p_{T_i})λ,
    E(T|E_{T_i})−a_T ≥ (1−p_T/p_{T_i})r_T.

Na nově přidaných výsledcích je T≥λ; nerovnost zůstává platná
i při T=λ. Nezávislost z předchozího odstavce zároveň dává

    E(T|E_{T_i})=a_{T_i}+E(X_i−u_i)=a_{T_i}+1−u_i,
    Δ_i:=b_T−b_{T_i}
        =(ET−ET_i)+(a_{T_i}−a_T)
        =1−u_i+a_{T_i}−a_T
        =E(T|E_{T_i})−a_T.

Tedy

    0≤(1−p_T/p_{T_i})r_T≤Δ_i,
    p_T≥p_{T_i}(1−Δ_i/r_T).                         (A)

Není zde obrácené znaménko při přesunu členu. Je-li navíc
r_{T_i}≥r_T, pak a_{T_i}≤a_T a

    0≤Δ_i=1−u_i−(r_{T_i}−r_T)≤1−u_i≤1.           (B)

V dalším kroku vždy vybereme souřadnici s r_{T_i}≥r_T.

## 3. Taková souřadnice vždy existuje

Pro dosud nekonstantní X_i napišme X_i=u_i+(v_i−u_i)I_i,
kde I_i je indikátor horní hodnoty. Všechny následující
kovariance jsou v rozdělení podmíněném E_T. Přímé rozepsání
kovariance s1−I_i dává

    Cov(T,X_i|E_T)
      =(v_i−u_i)Pr(X_i=u_i|E_T)
         (a_T−E(T|X_i=u_i,E_T)).

Při X_i=u_i je T=T_i. Nezávislost ostatních souřadnic na X_i
znamená, že poslední podmíněný průměr je a_{T_i}. Proto

    Cov(T,X_i|E_T)
      =(v_i−u_i)Pr(X_i=u_i|E_T)(r_{T_i}−r_T).    (C)

Váha před závorkou je striktně kladná: událost všech nižších
hodnot leží v E_T a má kladnou hmotnost i s X_i=u_i.
Sečtení(C) přes dosud náhodné členy dává

    0≤Var(T|E_T)=∑_i Cov(T,X_i|E_T).

Pevné členy mají nulovou kovarianci. Kdyby všechny rozdíly
r_{T_i}−r_T byly záporné, byla by pravá strana záporná.
Aspoň jeden rozdíl je tedy nezáporný. Platí to i při nulovém
podmíněném rozptylu; není zapotřebí žádné dělení rozptylem.

## 4. Konečnost, invariant a součin

V každém kroku je jeden nekonstantní člen nahrazen konstantou.
Po nejvýše n krocích je výsledný součet deterministický a≤n<λ.
Případné chybějící kroky doplníme identickými kroky sΔ=0.
Označme vzniklé součty T₀=S,T₁,…,T_n. Výběr z§3 zachovává
r_{T_j}≥r_S. Máme p_{T_n}=1, b_{T_n}=0 a podle(B)

    Δ_j=b_{T_{j−1}}−b_{T_j}∈[0,1],
    ∑_{j=1}^n Δ_j=b_S=:b∈[0,n],
    r_S=n+δ−a_S=δ+b.

Je-li b=0, pak p_S=1: jinak kladná hmotnost na S≥λ>a_S
činí celkový průměr striktně větší než a_S. Tento případ je
hotov zvlášť, bez výrazů0^0 nebo dělení b.

Při b>0 je každé Δ_j≤b, takže Δ_j/(δ+b)<1.
Všechny faktory v(A) jsou kladné a lze je násobit.
Z r_{T_{j−1}}≥δ+b, (A) a konečné teleskopie dostáváme

    Pr(S<λ)≥∏_j(1−Δ_j/r_{T_{j−1}})
            ≥∏_j(1−Δ_j/(δ+b)).                  (D)

Tím jsou doloženy i předpoklady následujících logaritmů.

## 5. Ostrá mez pro δ=1

Pro0≤x≤1 a b>0 leží konkávní funkce
log(1−x/(1+b)) nad spojnicí svých hodnot v0 a1. Tedy

    log(1−x/(1+b))≥x log(b/(1+b)).

Dosazením x=Δ_j a součtem v(D)

    Pr(S<n+1)≥(b/(b+1))^b.

Funkce f(b)=(b/(b+1))^b je na b>0 striktně klesající,
neboť

    (log f)′=−log(1+1/b)+1/(b+1)<0.

Poslední nerovnost plyne z log(1+x)=∫₀ˣdt/(1+t)>x/(1+x)
pro x>0. Jelikož b≤n, máme

    Pr(S<n+1)≥(n/(n+1))^n.                       (E)

Tento důkaz nepoužívá žádnou domněnku ani census.

## 6. Rovnost pro celá čísla a každý minimalizátor

Uvažujme dvoubodové celočíselné členy {0,m_i}, 1≤m_i≤n+1,
s Pr(X_i=m_i)=1/m_i. Hodnota m_i=1 znamená konstantu1.
Je-li v(E) rovnost, nemůže být b=0 a striktní monotónnost f
vynutí b=n. Tedy a_S=0. Protože S≥0, musí S=0 skoro jistě
na E_S={S<n+1}={S≤n}, která má kladnou pravděpodobnost.

Žádný člen nemůže být konstantní1, neboť pak S≥1 všude.
Všechny m_i≥2 a všechny pravděpodobnosti nuly jsou kladné.
Kdyby některé m_i≤n, událost „právě tento člen má hodnotu
m_i a všechny ostatní jsou0“ by měla hmotnost

    (1/m_i)∏_{j≠i}(1−1/m_j)>0

a na ní by0<S≤n. To odporuje a_S=0. Nutně tedy všechna
m_i=n+1. Naopak tato volba má Pr(S≤n)=(n/(n+1))^n.
Jde o jediné minimum v konečné třídě z30(b), nikoli jen o
jeden nalezený extremální bod.

V hlavní poznámce k30(b) je úplně dokázáno, že každý globální
minimalizátor má podporu v{0,…,n+1}. Pro takovou marginálu
x_{i,m}=Pr(X_i=m) položme y_{i,m}=m x_{i,m}, 1≤m≤n+1.
Platí ∑_m y_{i,m}=1 a přesně

    Law(X_i)=∑_{m=1}^{n+1} y_{i,m} Law(V_m),
    Pr(V_m=m)=1/m, Pr(V_m=0)=1−1/m.

Na kladném bodě m dává pravá strana y_{i,m}/m=x_{i,m};
v0 dává ∑(m−1)x_{i,m}=x_{i,0}, takže rovnost platí ve
všech bodech. Produkt nezávislých marginál je směs produktů
Law(V_{m₁})⊗⋯⊗Law(V_{m_n}) s vahami∏_i y_{i,m_i}.
Pr(S≤n) je proto vážený průměr jejich hodnot, z nichž každá
je nejméně(E), s rovností jen pro vektor(n+1,…,n+1).

Rovnost původního průměru tedy nutí celou hmotnost směsi na
tento jediný vektor. To vynutí y_{i,n+1}=1 pro každé i.
Každý globální minimalizátor je tudíž právě původní volba30(a).
Tím je pro všechna n vyřešen i tištěný výzkumný dovětek
a silnější „in any set“ v30(b), bez záměny existence a nutnosti.

## 7. Všechny δ>0, zejména tištěné δ₀=1/(e−1)

Pro0<b≤1 lze v(D) použít
∏(1−z_j)≥1−∑z_j pro nezáporná z_j≤1.
Důkaz je indukce: při přidání faktoru vznikne nezáporný
dodatečný člen z_j∑_{k<j}z_k, nebo ekvivalentně sjednocovací
mez pro nezávislé indikátory. Dostáváme

    Pr(S<n+δ)≥δ/(δ+b)≥δ/(δ+1).                 (F)

Tato větev je nutná; při δ+b≤1 se nesmí logaritmovat
1−1/(δ+b). Pro b≥1 je δ+b>1, a chordový argument jako
v§5 platí s tímto novým jmenovatelem:

    Pr(S<n+δ)≥exp(g_δ(b)),
    g_δ(b)=b log(1−1/(b+δ)).

Na b≥1, se z=b+δ>1, vychází přesně

    g′=log(1−1/z)+b/(z(z−1)),
    g″=((2δ−1)z−δ)/(z²(z−1)²),
    lim_{b→∞}g′=0.

Pro δ≤1/2 je g″<0; g′ proto klesá k0 a je kladná.
Pro δ>1/2 mění čitatel g″ znaménko nejvýše jednou,
ze záporného na kladné. V oblasti g″>0 roste g′ k0
a je záporná; v případné předchozí oblasti g′ klesá.
Proto g′ může uvnitř[1,∞) měnit znaménko jen z+ na−.
Funkce g tedy nemá vnitřní minimum na[1,n] a

    exp(g_δ(b))≥min{δ/(1+δ), (1−1/(n+δ))^n}.   (G)

Tím je přesně doplněn znaménkový krok z konce článku;
případ n=1 má interval[1,1] a stejný závěr přímo.
Spolu s(F) a b=0 to dává tuto mez pro všechny dvoubodové členy.

Nyní δ₀=1/(e−1) leží v(1/2,1), neboť2<e<3, a
δ₀/(1+δ₀)=1/e. Dále

    −b/(b+δ₀−1)≤g_{δ₀}(b)≤−b/(b+δ₀),

což plyne integrací1/(1−t) na[0,1/(b+δ₀)]. Obě krajní
hodnoty mají limitu−1. Minimum na každém[1,N] je v konci,
g_{δ₀}(1)=−1 a g_{δ₀}(N)→−1. Pro fixované b a N→∞
proto g_{δ₀}(b)≥−1. Z(F),(G) plyne

    Pr(S<n+1/(e−1))≥1/e.                        (H)

Nejde o záměnu s jednodušším prahem n+1. Mez(H) je dosažena,
když n−1 členů jsou konstanty1 a poslední je0 s pravděpodobností
1/e a1+δ₀ s pravděpodobností1/(1+δ₀). Jeho průměr je1
a horní hodnota dosahuje přesně vyloučeného prahu.

## 8. Obecná reálná rozdělení: přesná směs, žádná skrytá aproximace

Zbývá doložit přechod od konečných dvoubodových proměnných
k libovolným nezáporným integrabilním X s EX=1. Nechť μ je
jeho zákon, μ_L omezení na[0,1), μ_H omezení na(1,∞),
a c=μ({1}). Z EX=1 plyne

    d=∫(1−x)μ_L(dx)=∫(y−1)μ_H(dy)<∞.

Je-li d=0, pak X=1 skoro jistě. Pro d>0 definujme na
dvojicích x<1<y kladnou míru

    W(dx,dy)=(y−x)μ_L(dx)μ_H(dy)/d.

Její celková hmotnost je

    (μ_L([0,1))d+μ_H((1,∞))d)/d=1−c.

Ke každému páru přiřadíme dvoubodový zákon Q_{x,y} s hmotami
(y−1)/(y−x) v x a(1−x)/(y−x) v y. Jsou kladné, součet1,
průměr je přesně1. Směs∫Q_{x,y}dW má v dolní části zákon
μ_L, neboť integrace(y−1)/d přes μ_H dává1; v horní části
má zákon μ_H stejným výpočtem s(1−x)/d. Přidáním cδ₁
dostaneme přesně μ. Všechny integrandy jsou nezáporné,
takže Tonelli opravňuje výměnu integrací i pro neomezené podpory.

Nezávislá volba těchto směsných parametrů pro každou souřadnici
dává produkt původních zákonů. Každý výsledný konečný
dvoubodový produkt splňuje(H), proto ji splňuje i jejich směs.
Tento argument současně přenáší(E),(F),(G); není potřeba
předpokládat existenci minima v nekonečně rozměrném prostoru.

Má-li původní X_i pouze EX_i=μ_i≤1, položme
Y_i=X_i+1−μ_i. Zůstanou nezáporné a nezávislé, EY_i=1, a

    {∑Y_i<n+δ₀}={∑X_i<∑μ_i+δ₀}⊆{∑X_i<n+δ₀}.

Použití(H) na Y_i proto dává přesně poslední tvrzení na p375.
Všechny přenosy zachovávají ostré znaménko prahu. Tím je
Feigeho dovětek v požadovaném rozsahu úplně doložen.

Žádná enumerace, numerický verifier ani restart nebyly spuštěny.
