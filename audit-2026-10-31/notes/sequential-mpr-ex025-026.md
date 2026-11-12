# D127–D128 — celé MPR25(a,b) a26

6. listopadu 2026. Přímo zobrazeny celé zadání p14/file34 a odpovědi
p374/file394, také Pre-Fascicle5A p14/file20 a p31/file37.
Následující důkazy pokrývají každou tištěnou identitu, index,
nulovou pravděpodobnost i indukční mezikrok. Bez numerického běhu.

## D127: definice zobecněného binomického koeficientu

Označme P_n(k)=P(X₁+⋯+X_n=k), kde X_j jsou nezávislé bity,
p_j=EX_j∈[0,1], q_j=1−p_j. Přirozený rozsah počtu jedniček
je celé0≤k≤n; mimo něj položíme P_n(k)=0. Pro prázdnou rodinu
P₀(0)=1. Část(b) s podílem k/n předpokládá n≥1.

Každá množina I pozic s jedničkou má pravděpodobnost
∏_{i∈I}p_i ∏_{j∉I}q_j. Sečtením přes |I|=k získáme právě
koeficient z^k v ∏_{j=1}^n(q_j+p_jz). Tím je doloženo
generující vyjádření v zadání, včetně případů p_j=0 či1.
Rozdělením podle posledního bitu, nebo vynásobením posledního
lineárního faktoru, dostaneme

    P_n(k)=p_nP_{n−1}(k−1)+q_nP_{n−1}(k).

Nejde o dělení podmíněnou pravděpodobností; rovnost platí i při
deterministickém posledním bitu. Normalizace všech koeficientů
plyne z hodnoty produktu v z=1, která je∏(q_j+p_j)=1.

## D127(a): přesné násobnosti všech rozkladů

Nejprve0≤k<n. Sumujme přes všechny disjunktní rozklady
{1,…,n}=I⊔J⊔{t}, kde |I|=k a |J|=n−k−1. Označme
p_I=∏_{i∈I}p_i a q_J=∏_{j∈J}q_j, s prázdným součinem1.
Platí vytištěná identita

    P_n(k)−P_n(k+1)
      =∑_{I,J,t}p_Iq_J(q_t/(n−k)−p_t/(k+1)).

Pro první část zvolme množinu k jedniček I. Každá z jejích
n−k zbývajících pozic může být označena jako t a ostatní tvoří J.
Všech n−k takových členů má součin p_Iq_{Ī}; dělení n−k
vrací přesně jeden příspěvek do P_n(k).

Pro druhou část zvolme množinu k+1 jedniček K. Každá z jejích
k+1 pozic může být t, zbývající tvoří I a J=K̄. Součin je
vždy p_Kq_{K̄}; dělení k+1 vrací právě jeden příspěvek
do P_n(k+1). To dokazuje úplnost součtu a oba tištěné dělitele.

Všechny p_Iq_J jsou nezáporné a pro každý t

    q_t/(n−k)−p_t/(k+1)
       =((k+1)−(n+1)p_t)/((n−k)(k+1)).

Jmenovatel je kladný, takže tento výraz je nezáporný právě když
p_t≤(k+1)/(n+1). Za předpokladu zadání je celý součet
nezáporný, čili P_n(k)≥P_n(k+1).

Okraj k=n nepatří do rozkladového vzorce s dělitelem n−k.
Samotné tvrzení je zde přímo P_n(n)≥P_n(n+1)=0 a podmínka
p_j≤1 je automatická. Kraj k=0 je ve vzorci zahrnut:
I=∅ a oba dělitele n a1 jsou platné. Při n=0 je jen
k=0 a stejná přímá pravděpodobnostní nerovnost1≥0.
Žádný krok nevyžaduje kladnost všech p_j nebo q_j.

Při společné hodnotě p_j=(k+1)/(n+1),0≤k<n, je každý výraz
v závorce0, takže nastává rovnost. To také ověřuje přesné
umístění k+1 i n+1 v mezní podmínce.

## D127(b): celý argument postupného zvyšování souřadnic

Nechť0≤k≤n,n≥1 a0≤p_j≤p≤k/n. Pro k=0 musí být p=0
a všechny p_j=0; obě strany požadované nerovnosti jsou1.
Tento případ oddělíme před odkazem na index k−1.

Pro1≤k≤n fixujme všechny parametry kromě posledního a pišme

    P_n(k)=P_{n−1}(k)+p_n(P_{n−1}(k−1)−P_{n−1}(k)).

Jde o afinní funkci p_n. Část(a) použitá na n−1 bitů
s indexem k−1 dává nezápornou směrnici, protože její podmínka
je přesně p_j≤k/n. Pro k=n jde o již vyřešený koncový
případ(a): P_{n−1}(n−1)−P_{n−1}(n)≥0. Také n=1,k=1
se redukuje na prázdnou rodinu a směrnici1.

Proto zvýšení p_n na p nezmenší P_n(k). Symetrie součtu
umožňuje totéž pro každou souřadnici. Po každém kroku všechny
ostatní parametry stále splňují p_j≤p≤k/n, takže podmínka
použité části(a) zůstává zachována. Po přesně n konečných
nahrazeních mají všechny bity společný parametr p. Výsledek je

    P_n(k)≤binom(n,k)p^k(1−p)^{n−k}.

„Maximized when p_n=p“ neznamená jediné maximum; nulová směrnice
dovoluje rovnost pro celý interval. Nepoužívá se neodůvodněná
nezávislost parametrové optimalizace, ale zachovaný předpoklad
v každém z n kroků.

Pro k=n lze výsledek ověřit i přímo jako ∏p_j≤p^n. Hodnota
p=1 je podmínkou p≤k/n dovolena jen při k=n a výsledek dává
pravděpodobnost≤1. Při p=0 jsou všechny bity0; pro k>0 jsou
obě strany0, pro k=0 obě1. Mocniny s exponentem0 jsou konstantní
monomy1, takže koncové případy nevyvolávají neurčené dělení.

## D128: normalizace a ekvivalence přesné zadané nerovnosti

Pro0≤k≤n definujme r_{n,k}=P_n(k)/binom(n,k); binomický
jmenovatel je kladný. Mimo tento rozsah definujme r_{n,k}=0
přímo, nikoli jako0/0. Pro0<k<n platí

    binom(n,k−1)binom(n,k+1)/binom(n,k)²
      =k(n−k)/((k+1)(n−k+1)).

Proto po vynásobení kladnými binomickými koeficienty je přesně
ekvivalentní dvojice nerovností

    r_{n,k}²≥r_{n,k−1}r_{n,k+1},

    P_n(k)²≥P_n(k−1)P_n(k+1)(1+1/k)(1+1/(n−k)).

Nedělíme pravděpodobnostmi, takže ekvivalence platí také při
některých nulových koeficientech. Oba dodatečné faktory v zadání
jsou tím odvozeny a mají správné indexy.

## D128: chybějící podrobnost „by induction“ — souvislá podpora

Každý z těchto součtů má souvislou celočíselnou podporu. Je-li
s parametrů rovno1, u parametrů leží ostře mezi0 a1 a ostatní
jsou0, je součet jistých jedniček s plus u nedegenerovaných bitů.
Každý počet0,…,u má kladnou pravděpodobnost: vybereme příslušnou
množinu jedniček a součin jejích kladných p_j a kladných q_j
je kladný. Mimo s,…,s+u je pravděpodobnost0. Normalizace
kladnými binomickými koeficienty tuto podporu nemění.

Tato vlastnost bude potřeba pro prostřední člen B. Samotná
abstraktní sousední logaritmická konkávnost bez podmínky podpory
by nulové případy automaticky nevyřešila; zde však podporu
známe přímo z původního modelu, včetně parametrů0 a1.

## D128: celá normalizovaná rekurence a indukční základ

Z rekurence P_n a poměrů

    binom(n−1,k−1)/binom(n,k)=k/n,
    binom(n−1,k)/binom(n,k)=(n−k)/n

plyne pro0≤k≤n

    n r_{n,k}=k p_n r_{n−1,k−1}+(n−k)q_n r_{n−1,k}.

Na koncích se použije nulové rozšíření r; nedělíme tam nulovým
binomickým koeficientem. Pro n=0 a1 nejsou žádné vnitřní indexy
0<k<n. Na krajích a mimo podporu nerovnost r_j²≥r_{j−1}r_{j+1}
platí z nulového rozšíření, takže indukční základ je úplný.

Předpokládejme tvrzení pro n−1. Fixujme1≤k≤n−1 a označme

    a=r_{n−1,k−2}, b=r_{n−1,k−1},
    c=r_{n−1,k},   d=r_{n−1,k+1},
    p=p_n, q=q_n, L=n−k.

Všechny a,b,c,d,p,q jsou nezáporné a k,L≥1.
Indukce a krajní nulové rozšíření dávají

    A=b²−ac≥0,       C=c²−bd≥0.

Také B=bc−ad≥0: je-li bc>0, vynásobení ac≤b² a bd≤c²
a následné dělení kladným bc dává ad≤bc. Je-li bc=0,
pak ad=0, protože kladné a,d by díky souvislé podpoře vynutily
kladné b,c. V obou větvích tedy B≥0. Tím je třetí tištěná
nezápornost plně doložena, nikoli jen odvozena slovy „by induction“.

## D128: přímé ověření každého koeficientu indukční identity

Rekurence dává

    n r_{n,k}=kpb+Lqc,
    n r_{n,k−1}=(k−1)pa+(L+1)qb,
    n r_{n,k+1}=(k+1)pc+(L−1)qd.

Jejich čtverec a součin mají v rozdílu následující koeficienty:

| Faktor | Koeficient v n²(r_{n,k}²−r_{n,k−1}r_{n,k+1}) |
|---|---|
| p² | k²b²−(k²−1)ac |
| q² | L²c²−(L²−1)bd |
| pq | ((k−1)(L−1)−2)bc−(k−1)(L−1)ad |

Pro smíšený koeficient jsme použili přesně
2kL−(k+1)(L+1)=(k−1)(L−1)−2.
Po vyjmutí čtverce(pb−qc)² dostáváme tedy právě knižní identitu

    n²(r_{n,k}²−r_{n,k−1}r_{n,k+1})
      =(pb−qc)²+(k²−1)p²A
         +(k−1)(n−1−k)pqB+((n−k)²−1)q²C.

Všechny její čtyři členy jsou nezáporné: první je čtverec,
A,B,C byly dokázány a k,L≥1 zaručují nezáporné číselné
koeficienty. Proto požadovaná nerovnost platí i pro n.

Kraje k=1 či k=n−1 mohou nulovat některé koeficienty, ale
nevytvářejí záporný člen ani neurčitý výraz. Všechny nuly v a,b,c,d
jsou již zahrnuty předchozími větvemi. Indukce je konečná,
začíná skutečným základem a uzavírá každý vnitřní k.

Pro společný parametr p_j=p∈(0,1) je r_{n,k}=p^k(1−p)^{n−k},
takže nastává rovnost pro každé vnitřní k. Také deterministické
koncové rozdělení při všech p_j=0 nebo1 je zahrnuto nulovým
rozšířením; nic se nedělí mizícím koeficientem.

## Errata, bibliografie a přesný stránkový rozsah

Šest vrstev errat a tři TeX zdroje byly cíleně prohledány podle
stran, čísel25/26 a obsahových hesel. Nenalezena relevantní změna
ani neopravený rozpor. Sousední rating a citace24 jsou již E122/E123.
Číslovky25 a26 v datech jiných vložených odpovědí nejsou čísly
těchto úloh. Evidence:
`results/sequential/mpr-025-026-coefficients-errata.json`.

Historická tvrzení o Newtonově tisku1707, přesných stranách242–245
a Sylvesterově publikaci1865 nebyla ověřena v původních exemplářích;
v lokálních již uzavřených poznámkách nebyl nalezen dostatečný
pramen. Jsou explicitní bibliografickou výjimkou. Matematická
Newtonova nerovnost i každý krok zde vytištěného důkazu jsou
samostatně uzavřeny výše.

MPR25(a,b) a26 jsou celé reviewed. Tím je na původní p14/file34
posouzeno úplně každé zadání14–26: všechny požadované části19
jsou hotové, její otevřená Eulerova poznámka leží až v odpovědi
na file393 a tam zůstává partial. P14 lze uzavřít reviewed,
s dříve vyjmenovanou bibliografickou výjimkou Bayesovy atribuce.
Na file394 jsou nyní úplné zdejší odpovědi24–26;27–28 zůstávají
neuzavřené. Žádný nový nález, žádný běh či restart censu.
