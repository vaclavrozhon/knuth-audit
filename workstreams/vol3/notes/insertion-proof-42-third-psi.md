# §5.2.1-42(b): třetí průchod, přesná ψ a asymptotika

2026-11-07. P0871–0883; tím se doplňuje i P0785/odpověď25.
Originál105/file116,627/file638 a623/file634 zobrazen. Primární článek
Janson–Knuth, *Shellsort with three increments*, arXiv:cs/9608105v1(1996),
později RSA10(1997),125–142, je v sources/. Níže jsou vlastní úplné
argumenty pro všechny použité kroky sekcí1–7, nikoli pouze převzatá věta1.
Klasická Berryova–Esseenova věta je pojmenovaná vnější závislost pouze
v závěrečném normálním přiblížení. Žádné matematické běhy ani enumerace.
P0870/C0024 o pomocné mezi části(a) tím není uzavřen.

## Přesný rozklad inversí — P0871

Zde používáme indexy0,…,N−1. Nechť X_l je původní klíč, r=l mod h.
Po h-třídění skončí na pozici r+hY_rl, kde Y_kl je počet klíčů menších
než X_l v původní třídě k modulo h. Proto po následném g-třídění zůstane
v g-třídě

    J_rl=(r+hY_rl) mod g.

Obecně J_kl=(k+hY_kl) mod g pro0≤k<h. Nechť S_jl je počet klíčů
menších než X_l, které po prvním průchodu leží ve třídě j modulo g.
Tyto počty se druhým průchodem nemění.

Pro j<j' se obě výstupní g-třídy fyzicky střídají, počínaje j; první
má stejně nebo o1 více prvků. Pokud X_l patří do j, má index S_jl v této
rostoucí třídě, před jeho pozicí je S_jl prvků druhé třídy, avšak podle
hodnoty jich před něj patří S_j'l. Obsahuje tedy přesně |S_jl−S_j'l|
inversí s druhou třídou. Součet přes prvky třídy j započítá všechny
inverse tohoto páru právě jednou. Součet přes j<j' započítá všechny
zbývající inverse; uvnitř jedné g-třídy žádné nejsou.

## Deterministická modulární identita — P0872

Díky gcd(h,g)=1 existuje jediné d∈{1,…,g−1} s j'≡j+hd(mod g).
Označme j_s=(j+hs) mod g, H={j₁,…,j_d}, a Q_l=#{k:J_kl∈H}.
Platí přesně

    S_jl−S_j'l=Q_l−floor(hd/g).                            (1)

Důkaz začíná před nejmenším klíčem, kdy Y_k=0 a J_k=k mod g.
Počet k∈{0,…,h−1} s k mod g=v je w(v)=ceil((h−v)/g).
Pro v=j_s je to

    w(j_s)=floor((j+hs)/g)−floor((j+h(s−1))/g).

Součet od s=1 do d teleskopuje na floor((j+hd)/g). Jelikož j<j'<g
a j+hd=j'+qg, máme q=floor(hd/g); tím je(1) na začátku dokázána.
Tento podlahový argument platí i pro h<g a nepotřebuje enumeraci.

Při přechodu přes další klíč X_l vzroste pouze Y_r o1, tedy J_r se
posune o h v cyklu modulo g. Indikátor členství v H se změní o+1
právě pro původní J_r=j, o−1 právě pro J_r=j', jinak o0. Přesně totéž
se stane s S_j−S_j', protože právě zpracovaný klíč náleží g-třídě J_r.
Indukce podle rostoucích hodnot klíčů dokazuje(1) pro všechna l.

V příspěvku podmíněném J_rl=j lze z Q vynechat k=r, protože j∉H.
Označíme-li tento součet bez r rovněž Q, příspěvek páru je

    [J_rl=j] |Q−floor(hd/g)|.                              (2)

## Pravděpodobnostní model a nezávislost — P0873

Vezměme nezávislé X_0,…,X_(N−1) rovnoměrné na(0,1). Hodnosti mají
rovnoměrné rozdělení na N! permutacích a shody mají pravděpodobnost0;
tento model tedy přesně zachovává očekávaný počet přesunů.
Podmíněně na X_l=t jsou pro různá k proměnné Y_kl nezávislé, neboť
používají disjunktní množiny ostatních původních klíčů. Přesně

    Y_kl ~ Bin(n_k−[k=r],t),  n_k=#{i:0≤i<N,i≡k(mod h)}.

Tedy také J_kl jsou nezávislé a Q v(2) je nezávislé na J_rl. Příspěvek
páru j<j' a prvku l je proto

    W_jj'l(t)=Pr(J_rl=j) E|Q−floor(hd/g)|.                 (3)

Skutečný očekávaný počet je Σ_l Σ_(j<j') ∫₀¹ W_jj'l(t)dt.
Závislosti mezi různými l či různými t se nikde neignorují: použita
je jen linearita tohoto konečného součtu integrálů.

## Fourierův odhad reziduí — P0874

Pro Y~Bin(m,t), ω=exp(2πi/g), dává kořenový filtr

    Pr(Y≡a mod g)=(1/g)Σ_(k=0)^(g−1) ω^(−ka)(1−t+tω^k)^m.

Jeho nultý člen je1/g. Dále
|1−t+tω^k|²=1−4t(1−t)sin²(πk/g). Pro1≤k≤g/2 použijeme
sin(πk/g)≥2k/g a1−u≤e^(−u), pro druhou polovinu symetrii k↔g−k.
Tím dostaneme

    |Pr(Y≡a)−1/g| ≤(2/g)Σ_(k≥1) exp(−8m t(1−t)k²/g²).

Při N≥4h je každý m=n_k−[k=r]≥N/h−2≥N/(2h). Proto pro všechna
J_kl (násobení h permutuje rezidua)

    |Pr(J_kl=a)−1/g|≤φ(t)/g,
    φ(t)=2Σ_(k≥1) exp(−4N t(1−t)k²/(g²h)).               (4)

Koncové t=0,1 lze vynechat jako nulovou množinu. φ je na(0,1) kladné
a integrabilní; později doložený odhad integrálu ospravedlňuje použití
bodové majoranty. Není třeba předpokládat přesnou uniformitu reziduí.

## Ideální uniformní hodnota ψ — P0875

Pokud by J_k byly nezávislé a přesně uniformní na g reziduích, pak
Pr(J_r=j)=1/g a Q~Bin(h−1,d/g). Položme

    F_d=E|Bin(h−1,d/g)−floor(hd/g)|.

Pár j<j' by přispěl F_d/g. Pro pevné d označme a_d počet j s
j<(j+hd) mod g. Obrácení orientace páru d↔g−d dává a_d+a_(g−d)=g.
Navíc gcd(h,g)=1 a0<d<g zaručují hd/g necelé, takže
floor(h(g−d)/g)=h−1−floor(hd/g). Symetrie binomického rozdělení
R↔h−1−R proto dává F_(g−d)=F_d. Tedy

    Σ_d (a_d/g)F_d=(1/2)Σ_(d=1)^(g−1)F_d=ψ(h,g).         (5)

Rozepsání binomické pravděpodobnosti dává přesně dvojitý součet v105,
včetně1/2, h−1, podlahy a absolutní hodnoty. Hodnota je stejná pro
každý l,t, takže ideální celkový příspěvek je Nψ(h,g).

## Explicitní vazba na skutečné rozdělení — P0876

Pro dva pravděpodobnostní vektory p,u, kde u_i=1/g, položme
D_i=min(p_i,u_i), a_i=(p_i−u_i)_+, b_i=(u_i−p_i)_+,
R=Σa_i=Σb_i=(1/2)Σ|p_i−u_i|. Je-li R>0, společné rozdělení je

    Pr(J=i,J*=j)=[i=j]D_i+a_i b_j/R.

Protože a_i b_i=0, má správné oba marginály a Pr(J≠J*)=R.
Pro R=0 bereme J*=J. Tato výslovná konstrukce nepotřebuje větu o toku.
Pro každé k ji provedeme nezávisle; nezávislost J_k se tak zachová i
pro J*_k. Podle(4) je každá pravděpodobnost neshody≤φ(t)/2.

Q,Q* počítají členství h−1 proměnných v H, takže
E|Q−Q*|≤(h−1)φ/2. Funkce |z−floor(hd/g)| je1-Lipschitz a na
0≤z≤h−1 je≤h. Z(3) proto

    |W(t)−W*(t)|
      ≤|Pr(J_r=j)−1/g| h +(1/g)E|Q−Q*|
      ≤3h φ(t)/(2g).                                     (6)

Důkaz je bodový pro dané l,t. Nevyžaduje společnou vazbu pro všechna
t ani domnělou nezávislost po bezpodmínečném integrování.

## Integrace a absolutní chyba — P0877–P0878

Pro0<t≤1/2 je t(1−t)≥t/2. Symetrie a Tonelliho věta pro nezáporné
členy dávají

    ∫₀¹φ(t)dt
      ≤4Σ_(k≥1)∫₀^∞exp(−2Nt k²/(g²h))dt
      =2g²h/N Σ_(k≥1)1/k²
      =π²g²h/(3N).

Sčítáním(6) přes N prvků a g(g−1)/2 párů je pro N≥4h celková chyba
nejvýše (π²/4)g²(g−1)h², tedy O(g³h²) s absolutní konstantou.

Pro N<4h není třeba uniformitu reziduí vůbec dokazovat:
skutečný počet inversí≤N²/2≤8h² a
Nψ≤N(g−1)(h−1)/2≤2gh². Oba jsou O(g³h²), opět uniformně.
Pro g=1 je suma prázdná a konečný průchod nepřesune nic; pro h=1
už první průchod seřadil vše a ψ=0. Konečně N=0 dává přesně0.
Tím je **celé42(b)** dokázáno ve skutečné doméně, bez podmínky h>g
či dělitelnosti N:

    E B_1=Nψ(h,g)+O(g³h²),  gcd(h,g)=1.

Je to počet inversí a tedy skutečných přesunů na posledním vkládání;
plný čas obsahuje ještě lineární režii, která není součástí B.

## Obě dodatečné konstanty odpovědi25 — P0879 a P0785

Pro h=3,g=2 je pouze d=1, floor(hd/g)=1 a R~Bin(2,1/2).
E|R−1|=1/4+1/4=1/2, tudíž ψ(3,2)=1/4.
Pro h=2,g=3 jsou dva členy: Bernoulli(1/3) s podlahou0 a
Bernoulli(2/3) s podlahou1, každý s očekávanou odchylkou1/3.
Tedy ψ(2,3)=1/3. Proto po3-třídění a2-třídění zbývá N/4+O(1)
inversí; po opačném pořadí N/3+O(1). Chyba je O(1), protože zde h,g
jsou pevné. Tím se uzavírá přesně starý P0785; rovnoměrný výběr ze
všech společně2/3-uspořádaných permutací má jinou, již dokázanou míru.

## Binomická absolutní odchylka — P0880–P0881

Nechť Z~Bin(m,p),0<p<1, μ=mp, σ²=mp(1−p), q=ceil(μ).
Pro pravděpodobnost P_m(k) platí

    (k−mp)P_m(k)=mp(1−p)(P_(m−1)(k−1)−P_(m−1)(k)).

Součet od k=q do m teleskopuje a centrovaná kladná/záporná část mají
stejnou střední hodnotu. Proto

    E|Z−μ|=2q(1−p) P_m(q).                                (7)

Pro σ²≥4 jsou μ,m−μ≥σ² a q=μ+θ,0≤θ<1. Stirling s jeho obvyklou
uniformní chybou O(1/k) dává

    log P_m(q)=−(1/2)log(2πσ²)+O(σ^(−2)).

Konkrétně exponenciální část je −mD(q/m||p)=O(σ^(−2)), protože
|q/m−p|≤1/m a na tomto intervalu jsou p,1−p srovnatelné s q/m,1−q/m;
prefaktor q(m−q)/m je σ²(1+O(σ^(−2))) a tři Stirlingovy chyby mají
tentýž řád. Také q(1−p)=σ²(1+O(σ^(−2))). Dosazení do(7) tedy dává

    E|Z−μ|=sqrt(2/π)σ+O(1/σ).                             (8)

Pro σ²<4 je stejný odhad ve smyslu absolutní chyby O(1/σ) triviální
z E|Z−μ|≤σ; tato větev nepoužívá Stirling při malém argumentu.

Pro každé a∈[floor μ,ceil μ] potřebujeme totéž s |Z−a|.
Klasická Berryova–Esseenova věta pro součet nezávislých centrovaných
proměnných s konečným třetím absolutním momentem dává chybu distribuční
funkce≤C ΣE|V_i|³/σ³. Pro Bernoulli je
E|V_i|³=p(1−p)((1−p)²+p²)≤p(1−p), takže chyba≤C/σ.
Zvláště Pr(Z≤μ)=1/2+O(1/σ). Mezi floor μ a ceil μ je funkce
E|Z−a| lineární se směrnicí2Pr(Z≤floor μ)−1; pokud μ je celé,
interval obsahuje pouze μ. Tedy |E|Z−a|−E|Z−μ||=O(1/σ).
Dostáváme uniformně

    E|Z−a|=sqrt(2mp(1−p)/π)+O((mp(1−p))^(−1/2)).          (9)

Berry–Esseen je zde výslovně převzatá klasická věta, nikoli nově
auditovaný důkaz obecné CLT. Všechny její předpoklady a přesný Bernoulli
moment jsou ověřeny; stejné použití má primární Janson–Knuth na10.

## Součet chyb a kvadratura — P0882–P0883

V ψ je m=h−1,p=d/g,a=floor(hp)=floor(mp+p). Proto
floor(mp)≤a≤ceil(mp), takže(9) platí pro každý člen. Pro h≥2

    ψ(h,g)=sqrt((h−1)/(2π)) Σ_(d=1)^(g−1)sqrt((d/g)(1−d/g))
           +O(g/sqrt(h−1)).                              (10)

Pro chybu jsme použili
Σ_(d=1)^(g−1)1/sqrt(d(g−d))≤4: na první polovině g−d≥g/2,
součet d^(−1/2)≤2sqrt(g/2), druhá polovina je symetrická. Není třeba
předpokládat d/g oddělené od0 a1.

Položme f(x)=sqrt((x/g)(1−x/g)). Na[1,g−1] je konkávní,
f''(x)=−1/(4g² f(x)³). Chyba složeného lichoběžníkového pravidla je
omezena konstantou krát ∫₁^(g−1)|f''(x)|dx=f'(1)−f'(g−1)=O(g^(−1/2)).
Tento odhad plyne na každém jednotkovém intervalu z integrálního zbytku
s jádrem velikosti nejvýše1/8 a sečtením. Také f(1),f(g−1) a oba
vynechané krajní integrály jsou O(g^(−1/2)); například
∫₀¹ f(x)dx≤∫₀¹sqrt(x/g)dx=2/(3sqrt(g)). Proto

    Σ_(d=1)^(g−1)f(d)=∫₀^g f(x)dx+O(g^(−1/2))
                    =πg/8+O(g^(−1/2)).                   (11)

Poslední integrál je g∫₀¹sqrt(t(1−t))dt=πg/8 (substituce
2t−1=cos θ). g=2 splňuje stejný odhad přímo; asymptotika g→∞ tedy
nezatajuje singularitu krajní derivace v0 ani v g.

Dosadíme(11) do(10) a nahradíme sqrt(h−1) za sqrt(h), což přidá
O(g h^(−1/2)). Dostáváme přesně odpověď627:

    ψ(h,g)=sqrt(πh/128) g
           +O(g^(−1/2)h^(1/2))+O(g h^(−1/2)).

Obě O-konstanty jsou absolutní; růst h,g nemusí mít předem zadaný
poměr. Pro h=1 či g=1 může poslední chybový člen pohltit hlavní člen,
ale tvrzená relativní asymptotika se samozřejmě používá pro obě velké
hodnoty. Tím jsou všechny zadané vzorce42 a dovětek s ψ odvozeny.
