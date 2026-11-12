# D181–D182 — celé MPR80–81

7. listopadu 2026. Původní zadání p19/file39 a odpovědi
p382/file402 přímo zobrazeny, stejně PS p19/file25 a p38–39/file44–45.
Šest vrstev errat a tři TeX zdroje posouzeny v manifestu80–82;
to zatím samo neuzavírá82. Žádný nový výpočet ani restart.
Obecná konvence absolutně existujících očekávání z p2,p6,p7
se používá i pro níže uvedené součiny. Není tvrzena
integrabilita libovolné neomezené funkce automaticky.

## 80(a): každý předvídatelný faktor

Férovost znamená E(Y_n|Y₀,…,Y_{n−1})=0 pro n≥1.
Neukládá E Y₀=0. Pro každou funkci g známou z této historie,
pro niž gY_n je integrabilní, platí podle vytknutí a věže

    E(g(Y₀,…,Y_{n−1})Y_n)
      =E(g(Y₀,…,Y_{n−1}) E(Y_n|Y₀,…,Y_{n−1}))=0.

To je celý obecný dovětek odpovědi(a), s výslovným
děděným předpokladem existence očekávání. Pro n=5 a g=Y₃²
dává přesně E(Y₃²Y₅)=0. Faktor používá jen minulost,
nikoli nový Y₅; tento rozdíl je v další části rozhodující.

## 80(b): celý konečný model s nekonečným pokračováním

Vezměme nezávislé férové ε,η∈{−1,1}. Položme
Y₃=ε, Y₅=[ε=1]η a všechny ostatní Y_j=0, včetně Y₀
a celého pokračování j≥6. V čase3 je ε nezávislé
na nulové minulosti s průměrem0. V čase5 je [ε=1]
známé z historie a nový nezávislý bit η má průměr0.
Ve všech ostatních časech je nový člen0. Tím je celá
nekonečná posloupnost férová; všechny členy i součiny
jsou omezené.

Přitom Y₅²=[ε=1], a tudíž

    E(Y₃Y₅²)=E(ε[ε=1])=1/2≠0.

Jde o úplnou konkrétní instanci tištěného příkladu,
nikoli pouze izolovanou specifikaci dvou proměnných.

Také dovětek o permutaci je doložen: prohoďme pozice3 a5.
Po pozorování nového třetího členu, tedy starého Y₅,
je starý Y₃ jistě1, je-li Y₅≠0, a jistě−1, je-li Y₅=0.
Proto jeho podmíněný průměr v nové pozici5 není0
v žádné z těchto větví. Permutovaná posloupnost tedy
není férová.

Jsou-li naopak Y₃,Y₅ nezávislé s E Y₃=0 a existujícími
potřebnými momenty, pak E(Y₃Y₅²)=E Y₃·E Y₅²=0.
To je přesný kladný dodatek z odpovědi, nikoli předpoklad
původního příkladu.

## 80(c): všechny indexy a celý dovětek

Pro různé indexy n₁<…<n_m a n_m≥1 položme
g=Y_{n₁}···Y_{n_{m−1}}. Je známé z historie do n_m−1;
při m=1 je g prázdný součin1. Argument(a) dává

    E(Y_{n₁}···Y_{n_m})=0.

Jediný neprázdný případ s n_m=0 je m=1,n₁=0.
Férovost jeho střední hodnotu neurčuje. Například
Y₀=1 a Y_j=0 pro j≥1 je férové, ale E Y₀=1.
Pro m=0 je součin1 a očekávání1, rovněž nikoli0.
Tím jsou přesně pokryty obě výjimky tištěné odpovědi.
Když m≥2, je n_m≥1 i při n₁=0, takže předchozí
důkaz platí a žádná další výjimka není.

U „totálně nekorelovaných“ posloupností bereme různé
indexy jako v právě řešeném tvrzení. Každá férová
posloupnost má E Y_j=0 pro j≥1, opět věží.
Pro m≥2 je tedy poslední centrovaný faktor Y_{n_m}
a součin předchozích centrovaných faktorů je známý
z historie. Jeho očekávání krát poslední faktor je0.
Pravá strana součinu jednotlivých centrovaných očekávání
je také0. Pro m=1 je rovnost0=0 přímo z centrování;
pro m=0 je1=1. To dokazuje celý kladný dovětek, aniž
by se neoprávněně předpokládalo E Y₀=0.

Obrácená implikace selže i se všemi nulovými průměry.
Nechť Y₀ nabývá−1,0,1 rovnoměrně a
Y₁=Y₀²−2/3; všechny Y_j pro j≥2 jsou0.
Pak E Y₀=E Y₁=0 a

    E(Y₀Y₁)=E(Y₀³)−(2/3)E Y₀=0.

Každý součin aspoň tří různých členů obsahuje některý
nulový člen; ostatní párové součiny jsou také0.
Spolu s jednotlivými nulovými průměry to dokazuje
všechny požadované centrované součinové rovnosti.
Přesto E(Y₁|Y₀)=Y₀²−2/3 nabývá1/3 nebo−2/3,
nikoli0. Posloupnost není férová. Všechny atomy
a nekonečné pokračování jsou specifikovány.

## 81: koeficienty, záporné indexy a rekonstrukce historie

Předpoklad je
E(X_{n+1}|X₀,…,X_n)=X_n+X_{n−1} pro n≥0,
s X_{−1}=0. Členy jsou integrabilní v obecné konvenci knihy.
Hledáme univerzální deterministické koeficienty tak,
aby Z_n=a_nX_n+b_nX_{n−1}. Podmínění celou historií X dává

    E(Z_{n+1}|X₀,…,X_n)
      =(a_{n+1}+b_{n+1})X_n+a_{n+1}X_{n−1}.

Postačí proto koeficientové identity

    a_{n+1}=b_n,    b_{n+1}=a_n−b_n.                (1)

Jsou to přesně rovnosti z odpovědi. Jde o univerzální
volbu koeficientů; netvrdíme, že pro nějaký degenerovaný
pevný proces X nemohou existovat další náhodou vyhovující
koeficienty. Zadání takovou další jednoznačnost nepožaduje.

Použijme Fibonacciho čísla F₀=0,F₁=1,
F_{j+1}=F_j+F_{j−1} pro všechna celá j.
Zpětná rekurence dává F_{−1}=1,F_{−2}=−1,F_{−3}=2.
Indukce z F_{−m}=F_{−m+2}−F_{−m+1} dokazuje
F_{−m}=(−1)^{m+1}F_m pro m≥1.
Zvláště F_m>0 pro m≥1 plyne dopřednou indukcí.
Proto navržené

    a_n=F_{−n−1},    b_n=F_{−n−2}                 (2)

splňují(1): a_{n+1}=b_n a
b_{n+1}=F_{−n−3}=F_{−n−1}−F_{−n−2}.
Také b_n=a_{n+1} a b_{n−1}=a_n, takže tiskové
b_{n+1}=b_{n−1}−b_n platí pro n≥1.

V n=0 má(2) a₀=1,b₀=−1; protože X_{−1}=0,
je Z₀=X₀. V n=1 má a₁=−1,b₁=2, tedy přesně
Z₁=2X₀−X₁. První martingalový krok je rovněž správný:

    E(Z₁|X₀)=2X₀−E(X₁|X₀)=2X₀−X₀=X₀.

Pro n≥1 dává dosazení(1) do podmíněného výpočtu
hodnotu Z_n. Každý Z_n je integrabilní lineární
kombinace dvou integrabilních proměnných, s konečnými
koeficienty, a je známý z celé historie X.

Zbývá ověřit úvodní předpoklad tištěného řešení.
Z₀ určuje X₀. Pro každé n≥1 je
a_n=(−1)^n F_{n+1}≠0. Z již známého X_{n−1}
a nového Z_n získáme

    X_n=(Z_n−b_nX_{n−1})/a_n.

Konečná indukce rekonstruuje celou historii X₀,…,X_n
z historie Z. Opačná závislost je dána definicí Z,
takže obě historie určují stejnou informaci. Všechny
podmíněné rovnosti v odpovědi proto skutečně platí
i pro vlastní historii Z; předpoklad nebyl ponechán
bez důkazu. Žádné dělení nulou ani chybějící počáteční
Fibonacciho hodnoty se nevyskytují.

## Bibliografie a rozsah

[Instituce vydávající Annals of Probability](https://imstat.org/2014/12/16/obituary-james-b-macqueen-1929-2014/)
v textu Thomase Fergusona potvrzuje MacQueenův článek
A Linear Extension of the Martingale Convergence Theorem,
svazek1(1973), pp263–271, a popisuje příslušné lineární
podmíněné rekurence. Metadata a tematická souvislost
jsou ověřeny. Přímý odkaz Project Euclid vyžádal
dodatečnou kontrolu přístupu; přesný obsah původního
článku se výslovně bibliograficky vynechává.
Žádná jeho věta není potřebná pro výše uvedený důkaz.

Všechny erratové shody v manifestu patří sousedním
úlohám nebo jiným oddílům; použitelná oprava80–81
nenalezena. Celé80(a–c), oba dovětky a celá81 se všemi
indexy a rekonstrukcí jsou uzavřeny.82 zůstává další
samostatnou úlohou. Bez nálezu, kandidáta nebo běhu.

