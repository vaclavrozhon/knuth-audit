# D162–D163 — celé MPR 60–61

7. listopadu 2026. Původní zadání p17–18/file37–38 a odpovědi
p379/file399 byly přímo zobrazeny, stejně jako autorův PS
p17–18/file23–24 a p35–36/file41–42. Všech šest vrstev errat
a tři TeX zdroje byly prohledány a shody posouzeny podle sekce,
obsahu i historického stránkování. Žádná relevantní oprava.

P059 obsahuje správné omezené důkazy a historické testy FKG.
Původní rozsah i výsledky jsou zachovány v evidenci. Položka
byla skutečně znovu otevřena, protože čtyři jednověté důvody
61(e) nepokrývaly všechny normalizace a mezikroky obnoveného
standardu. Po doplnění D163 se znovu uzavírá; oba přechody
i původní poznámka jsou v quality_recovery_history.
Žádný historický běh se neopakuje.
Nová kontrola níže zahrnuje každou podčást, tištěný mezikrok
a všechny čtyři rodiny z odpovědi 61(e). D115 se přebírá
pro definiční vztah kovariance indikátorů a korelace událostí;
celá 61 se tím dříve nepovažovala za hotovou.

## 60(a): přesná konečná redukce a všechny čtyři funkce

F a G jsou konečné rodiny, jednotlivé množiny však v zadání
nemusí být konečné. Jsou-li F nebo G prázdné, jsou prázdné
také F∨G a F∧G a požadovaná nerovnost je 0≤0.

V ostatních případech vyjmenujme H=F∪G a položme V=⋃H.
Každému prvku V přiřaďme vektor jeho příslušnosti do všech
množin H. Rozdělme V podle těchto vektorů na neprázdné
atomy; jejich konečnou indexovou množinu označme E.
Je jich nejvýše 2^{|H|}. Vně V nejsou žádné prvky potřebné
pro rodiny ani jejich sjednocení a průniky.

Každá množina z H a každé její konečné sjednocení či průnik
je sjednocením celých atomů. Zobrazení φ, které jí přiřadí
množinu indexů jejích atomů, je na tomto oboru prosté a

    φ(S∪T)=φ(S)∪φ(T),    φ(S∩T)=φ(S)∩φ(T).

To plyne po jednotlivých atomech: členství je na každém
konstantní a operace OR/AND jsou přesně sjednocení/průnik.
Nevolíme ani nemusíme vyjmenovat všechny původní prvky.
Redukce tedy platí i pro nespočetné původní množiny.
Rodiny F, G, F∨G a F∧G se přenesou bijektivně, bez
započítávání různých reprezentací téhož sjednocení navíc.

Po přenosu váhových funkcí definujme na P(E)

    ᾱ(A)=α(φ⁻¹(A)) pro A∈φ(F), jinak 0;
    β̄(A)=β(φ⁻¹(A)) pro A∈φ(G), jinak 0;
    γ̄(A)=γ(φ⁻¹(A)) pro A∈φ(F∨G), jinak 0;
    δ̄(A)=δ(φ⁻¹(A)) pro A∈φ(F∧G), jinak 0.

Je-li ᾱ(A)β̄(B)>0, jsou A∈φ(F), B∈φ(G), takže jejich
sjednocení/průnik patří do odpovídajících rodin a původní
hypotéza dává

    ᾱ(A)β̄(B)≤γ̄(A∪B)δ̄(A∩B).                         (1)

Je-li levá strana nulová, platí (1) z nezápornosti přímo.
Věta o čtyřech funkcích z D161/59(b) nyní dává

    (∑ᾱ)(∑β̄)≤(∑γ̄)(∑δ̄),

což je právě α(F)β(G)≤γ(F∨G)δ(F∧G). Všechny součty jsou
konečné; funkce mimo původní rodiny nemusely být předem
definovány. Binární kód s=∑_{j∈A}2^j je konečné celé číslo
a jeho bitové OR/AND přesně odpovídá operacím v (1).
Tím jsou oprávněny oba zkrácené kroky „we can consider“
a „can be encoded“ v tištěné odpovědi. Nejde o nové erratum.

### 60(b)

Volba všech relevantních vah rovna 1 splňuje hypotézu
rovností. Čtyři konečné součty jsou přesně velikosti rodin,
takže |F||G|≤|F∨G||F∧G|. Prázdné rodiny jsou již pokryty.

## 61: konečná pravděpodobnostní oblast

Z věty „S occurs with probability μ(S)“ vyplývá μ≥0 a ∑μ=1.
Předpoklad U=⋃_{μ(S)>0}S konečné zaručuje, že podpora leží
v konečné P(U). Všechny uvažované reálné funkce i jejich
součiny mají proto konečná očekávání. Pro U=∅ jde o jediný
atom ∅ a každá kovariance je 0. Součty níže mohou být
omezeny na P(U); hodnoty mimo podporu nepřispívají.

Hypotéza je

    μ(S)μ(T)≤μ(S∪T)μ(S∩T).                              (**)

### 61(a): nezáporná verze a přesný posun

Pro nezáporné neklesající f,g položme

    α=fμ,    β=gμ,    γ=fgμ,    δ=μ.

Pro S,T⊆U máme po dvou explicitních krocích

    α(S)β(T)=f(S)g(T)μ(S)μ(T)
       ≤f(S)g(T)μ(S∪T)μ(S∩T)
       ≤f(S∪T)g(S∪T)μ(S∪T)μ(S∩T)
       =γ(S∪T)δ(S∩T).

První nerovnost je (**), druhá používá S,T⊆S∪T a
nezápornost všech faktorů. Nulové váhy nevyžadují
dělení. D161/59(b) dává (Ef)(Eg)≤E(fg)·E1=E(fg).

Pro obecné reálné neklesající funkce použijme přesně
tištěný posun f̂(S)=f(S)−f(∅), ĝ(S)=g(S)−g(∅).
Protože ∅⊆S, jsou f̂,ĝ nezáporné a neklesající, i když
μ(∅)=0. Přímé roznásobení s E1=1 dává

    E(f̂ĝ)−(Ef̂)(Eĝ)=E(fg)−(Ef)(Eg).

Tím je obecný závěr dokázán. Je přesně ekvivalentní
covar(f,g)≥0 podle definice kovariance. Pojem „positively
correlated“ zde znamená slabou nezápornost; nezávislé
funkce mohou mít rovnost, jak výslovně připomíná kniha.

### 61(b): všechna znaménka

Linearita konečných součtů dává pro každá reálná θ,φ,
včetně nuly, covar(θf,φg)=θφ covar(f,g).
Pro dvě nerostoucí funkce jsou −f,−g neklesající, takže
(a) dává jejich nezápornou kovarianci, rovnou covar(f,g).
Pro f neklesající a g nerostoucí jsou f,−g neklesající,
tedy −covar(f,g)≥0. Dostáváme přesně obě tištěné nerovnosti.

### 61(c): všechny jmenovatele a teleskopické kroky

Je-li μ(S)μ(T)=0, je (**) triviální. Jinak jsou S,T
podporované. Podle (i) jsou podporované také R=S∩T
a V=S∪T. Podle (ii) existují podporované řetězce

    S_i=R∪{s₁,…,s_i},  0≤i≤k,    S_k=S;
    T_j=R∪{t₁,…,t_j},  0≤j≤l,    T_l=T.

Seznamy s a t jsou disjunktní, protože vypočítávají
S\T a T\S. Podle (i) jsou všechny U_{ij}=S_i∪T_j
podporované, takže μ(U_{ij})>0. Pro i<k,j<l jsou
s_{i+1},t_{j+1} různé a neleží v U_{ij}. Podmínka (iii)
se proto vztahuje na přesnou dvojici U_{i+1,j},U_{i,j+1}
a dává

    μ(U_{i+1,j})μ(U_{i,j+1})
      ≤μ(U_{i+1,j+1})μ(U_{i,j}).

Dělení kladným μ(U_{i,j})μ(U_{i,j+1}) je oprávněné:

    μ(U_{i+1,j})/μ(U_{i,j})
      ≤μ(U_{i+1,j+1})/μ(U_{i,j+1}).                     (2)

Vynásobením (2) pro i=0,…,k−1 se každý vnitřní faktor
zkrátí a dostáváme

    μ(U_{k,j})/μ(U_{0,j})
      ≤μ(U_{k,j+1})/μ(U_{0,j+1}).

Postupné použití pro j=0,…,l−1 dává
μ(S)/μ(R)≤μ(V)/μ(T). Vynásobení kladným μ(R)μ(T)
dokazuje (**). Je-li k=0 nebo l=0, jsou S,T srovnatelné
a (**) je rovnost; prázdné součiny jsou rovny 1.
Jde o konečný obdélník nejvýše kl místních aplikací.
Každá podpora a kladnost jmenovatele je doložena.

### 61(d): nezávislost, normalizace a hraniční parametry

Každý souřadnicový faktor je p_j, je-li j∈S, jinak
1−p_j. Tento zápis nepoužívá nevymezené 0^0; ekvivalentní
tištěné mocniny mají konvenci prázdného součinu 1.
Součet všech konfigurací je

    ∑_S μ(S)=∏_{j=1}^m(p_j+(1−p_j))=1.

Pro každou pevnou specifikaci části bitů se součet
přes ostatní bity rozpadne na faktory 1. Marginály
a jejich součiny tedy přesně dokazují nezávislost
s parametry p_j; jde o model z již uzavřené MPR25.

Pro každý j platí
[j∈S]+[j∈T]=[j∈S∪T]+[j∈S∩T],
a stejná identita platí pro indikátory nepříslušnosti.
Obě strany (**) jsou totožné součiny týchž faktorů.
Neprovádí se žádné dělení, takže důkaz zahrnuje
p_j=0, p_j=1 i m=0.

Terminologický dovětek je doložen skutečným použitím
názvu „Poisson Trials“ v [primární přednášce Johna Cannyho](https://people.eecs.berkeley.edu/~jfc/cs174lecs/lec9/lec9.html),
CS174, Spring 1999, Lecture 9, právě pro nezávislé
binární proměnné s různými p_j. Ověřujeme výskyt
terminologie, nikoli kvantitativní frekvenci slova „often“.
Rozdíl proti Poissonovu zákonu z MPR39 je matematický:
zde jde o konečný binární vektor (jeho součet je ≤m),
kdežto Poissonův zákon s kladným parametrem má kladnou
hmotnost na každém nezáporném celém čísle. Jiný obsah
přednášky se nepřebírá jako matematická evidence.

### 61(e): normalizace společná všem čtyřem příkladům

Úvod odpovědi výslovně říká zvolit c tak, aby ∑μ=1.
Při μ=cw a konečných nezáporných vahách je tato volba
možná právě když Z=∑w>0, a pak jednoznačně c=1/Z.
To je podmínka oboru příkladů, nikoli tvrzení, že
každé libovolné zadání vah musí být normalizovatelné.
Ve (**) se společný kladný faktor c² zkrátí.

#### (i) Neklesající součinové váhy podle velikosti

Nechť 0<r₁≤…≤r_m, R₀=1 a R_j=∏_{h=1}^j r_h.
Pak w(S)=R_{|S|} a Z=∑_{j=0}^m binom(m,j)R_j>0.
Pro a=|S∩T|, b=|S\T|, d=|T\S| potřebujeme

    R_{a+b}R_{a+d}≤R_aR_{a+b+d}.

Každý faktor r_{a+h}≤r_{a+b+h} pro 1≤h≤d;
vynásobení těchto nerovností a kladným R_aR_{a+b}
dává přesně požadovaný vztah. Všechny indexy jsou
nejvýše m. Pro b=0 či d=0 jde o rovnost; m=0 je
jediná prázdná množina s vahou 1.

#### (ii) Váhy na řetězci a Chebyshevova nerovnost

Pro C_j={1,…,j}, 1≤j≤m, vezměme nezáporná p_j
s kladným součtem a w(C_j)=p_j, ostatní váhy 0.
Normalizace je c=1/∑p_j. Každé dvě podporované
množiny jsou srovnatelné, takže jejich průnik a
sjednocení jsou právě ony dvě původní množiny.
(**) je rovnost. Pokud levý součin je nulový,
nerovnost opět plyne z nezápornosti.

Pro stejná kladná p_j je zákon rovnoměrný na m
množinách řetězce. Neklesající f,g dávají neklesající
posloupnosti u_j=f(C_j), v_j=g(C_j). Identita

    m∑_j u_jv_j−(∑_j u_j)(∑_j v_j)
      =∑_{j<k}(u_j−u_k)(v_j−v_k)≥0                    (3)

plyne rozepsáním součtů: každý diagonální u_jv_j
má vpravo koeficient m−1 a každý smíšený člen −1.
Nezápornost je součin dvou souhlasných rozdílů.
Po dělení m² je (3) přesně FKG pro tento zákon.
Pro m=1 je kovariance 0. Pro m=0 nebo všechny
p_j=0 nelze tento konkrétní řetězcový zákon
normalizovat; takové parametry úvodní podmínku
„choose c“ nesplňují.

Odkaz §1.2.3–31 byl přímo ověřen v původní sazbě
svazku 1, p36/file51 a odpovědi p472/file487. Jde
právě o Chebyshevovu monotónní nerovnost (3).
Netvrdí se audit celých příslušných stránek svazku 1.

#### (iii) Lokální zákony na překrývajících se univerzech

Nechť w(S)=∏_{a=1}^k μ_a(S∩U_a), kde každý lokální
zákon splňuje (**). Pro každé S,T použijme místní
nerovnost na S∩U_a,T∩U_a a všechny nerovnosti vynásobme.
Všechny faktory jsou nezáporné a

    (S∩U_a)∪(T∩U_a)=(S∪T)∩U_a,
    (S∩U_a)∩(T∩U_a)=(S∩T)∩U_a.

Výsledek je w(S)w(T)≤w(S∪T)w(S∩T), bez požadavku
disjunktnosti U_a a bez dělení nulami.
Po normalizaci platí (**).

Kladnost Z není pro neslučitelné lokální zákony
automatická. Například U₁=U₂={x}, první zákon
soustředěný na ∅ a druhý na {x} dají w≡0.
Takové zadání však nesplňuje již uvedený pokyn
zvolit c s ∑μ=1, a není protipříkladem uvedené
normalizované konstrukce. Platných překrývajících
se příkladů je dost: pokud každé μ_a(∅)>0,
pak w(∅)>0 a Z>0. Pro k=0 je prázdný součin 1
a vzniká rovnoměrný zákon na P(U).

#### (iv) Exponenciála záporné submodulární funkce

Pro reálnou submodulární funkci f na P(U) je

    f(S∪T)+f(S∩T)≤f(S)+f(T).

Vynásobení −1 a rostoucí exponenciála dává
e^{-f(S)}e^{-f(T)}≤e^{-f(S∪T)}e^{-f(S∩T)}.
Váhy jsou konečné a kladné, takže Z>0 a normalizace
existuje. To dokazuje přesně tvrzení v odpovědi.

Pokud je f definována pouze na neprázdném oboru D
podporovaných podmnožin, vyžaduje tištěná podmínka
„whenever f(S) and f(T) are defined“ také definované
levé hodnoty f(S∪T),f(S∩T). D je tedy uzavřeno na
obě operace. Položíme w=e^{-f} na D a w=0 mimo D.
Pro dvojici v D platí předchozí důkaz, pro ostatní
je levý součin 0. Z je konečné kladné, takže celý
argument zůstává platný. Libovolné odstranění
bodů podpory tuto tištěnou definici nesplňuje.

Odkaz na budoucí §7.6 není v lokální knihovně
dostupný a je výslovnou bibliografickou výjimkou.
Potřebná submodulární nerovnost je v odpovědi celá
uvedena a její použití je výše dokázáno; matematický
argument na nedostupném zdroji nezávisí.

## Primární bibliografie a přesný rozsah

[Fortuin–Kasteleyn–Ginibre, původní článek](https://math.bme.hu/~balint/oktatas/perkolacio/percolation_papers/fortuin_kasteleyn_ginibre.pdf)
byl uložen a přímo byly zobrazeny jeho strany 89 a 91.
Potvrzují Commun. Math. Phys. 22 (1971), 89–103,
jména autorů a konečnou formulaci Proposition 1,
včetně výslovného přechodu od kladné míry k její
podpoře při nulových vahách. Celý původní článek
se nevydává za samostatně auditovaný; důkaz
potřebné booleovské verze je kompletně uveden výše.

Celé MPR60(a,b), MPR61(a–e), všechny dodatky a
tištěné mezikroky jsou reviewed. Jedinou novou
bibliografickou výjimkou je forward reference §7.6.
Žádný nový nález, kandidát ani numerický běh.
File37 je nyní celý reviewed; file38 je partial
pro další úlohy a file399 zůstává partial pouze
pro začátek odpovědi62. Starší výzkumné mezery,
výpočetní výjimky a censy zůstávají beze změny.

