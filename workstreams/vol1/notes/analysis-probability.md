# §1.2.10: pravděpodobnostní funkce, momenty a normální limita

Kontrolovány zobrazené s. 100–106 a 500–501. Tato poznámka pokrývá
vzorce (10)–(23), úlohy 2, 4–6, 11–17 a číselné údaje o normálním rozdělení.
Doplňuje `analysis-records.md` a `analysis-findings.md`.

## Pravděpodobnostní vytvořující funkce a součin

Pro nezápornou celočíselnou náhodnou veličinu X definujeme
`G(z)=∑_{k≥0}Pr(X=k)z^k`. Tato PGF konverguje absolutně pro |z|≤1
a G(1)=1. Derivace uvnitř jednotkového kruhu a monotónní limita zleva
v z=1 dávají `G'(1)=EX`, `G''(1)=E(X(X−1))`. Při konečném druhém momentu
tedy `Var X=G''(1)+G'(1)−G'(1)²`, což dokazuje úlohu 2 i (10)–(13).
Pro nekonečné momenty nemá smysl odčítat dvě nekonečna; tento audit
nevykládá vzorce jako takovou operaci. Všechna konečná rozdělení v textu
mají potřebné momenty automaticky.

Součin GH dvou PGF má jako koeficienty konvoluci, tj. součty
`∑_{i+j=k}Pr(X=i)Pr(Y=j)`. Je to rozdělení X+Y pro nezávislé X,Y.
Při G(1)=H(1)=1 platí `(GH)'(1)=G'(1)+H'(1)` a
`(GH)''(1)=G''(1)+2G'(1)H'(1)+H''(1)`.
Dosazení do vzorce pro rozptyl ruší smíšený člen a dokazuje Theorem A.
Tato algebraická věta vyžaduje jen existenci uvedených derivací;
nezávislost patří až k interpretaci součinu jako součtu náhodných veličin.

## Binomické a rovnoměrné rozdělení

Při n nezávislých pokusech s úspěchem pravděpodobnosti p, q=1−p, je
`G_n(z)=(q+pz)^n`, `Pr(X=k)=C(n,k)p^k q^(n−k)` pro 0≤k≤n.
Jeho střední hodnota je np, rozptyl npq. Rekurence (17) vyplývá
z posledního pokusu; mimo rozsah klademe pravděpodobnosti rovné nule.
Počáteční podmínka G_0=1 byla doplněna 2024 a je slučitelná i s n=0.
Rozsah 0,…,n v (19) je dosažitelný při 0<p<1; v krajních případech
p=0 nebo p=1 je rozdělení deterministické. Pro Fig. 11 (n=12,p=3/5)
jsou μ=36/5, σ=6√2/5≈1.697. Výšky sloupců jsou v souladu s binomickými
koeficienty; kontroluje se jejich relativní velikost, nikoli přesné rozměry sazby.

Rovnoměrné rozdělení na 1,…,n má
`G(z)=(z+…+z^n)/n=(z^(n+1)−z)/(n(z−1))`.
V z=1 jde o odstranitelnou singularitu. Podílové pravidlo dává oba
zobrazené vzorce pro G',G'' na s. 102. Nezávislá kratší kontrola:
`[w^r]G(1+w)=C(n+1,r+1)/n` pro r≥1, zatímco konstantní člen je 1.
Pro r=1,2 dostaneme G'(1)=(n+1)/2 a G''(1)=(n²−1)/3.
Proto μ=(n+1)/2, σ²=(n²−1)/12 a σ~0.288675…n, v souladu s 0.289n.

## Kumulanty a úlohy 6, 11, 12

Kumulanty κ_r jsou koeficienty logaritmu momentové funkce:
`K(t)=ln E(exp(tX))=∑_{r≥1}κ_r t^r/r!` v okolí 0, kde funkce existuje.
Pro výpočet do konečného řádu r stačí r konečných momentů a lze pracovat
formálně s Taylorovým polynomem. Není nutné předpokládat konvergenci
celé momentové řady pro každé rozdělení. Charakteristická funkce
`E exp(itX)=G(exp(it))` naproti tomu existuje pro každé reálné t.
Přímé derivování dává κ_1=EX a κ_2=Var X. V původním vzorci (23)
byl u t² omylem index 1, již opravený 29. července 1997.

Z K_{X+Y}=K_X+K_Y při nezávislosti se sčítají všechny kumulanty.
Posunutí X→X+c přidává ct do K: κ_1 vzroste o c, ostatní se nemění.
Pro celočíselné nezáporné c je PGF nové veličiny z^c G(z) (úloha 11).
Terminologickou opravu „term“ na „factor“ obsahují errata 2024.

Pro Bernoulliho veličinu je třetí koeficient
`κ_3=p(1−p)(1−2p)`. Součty dávají pro binomické rozdělení
`κ_3=npq(q−p)` a pro počet aktualizací
`κ_3=H_n−3H_n^(2)+2H_n^(3)`.
Rovnoměrné rozdělení má
`K(t)=t+J(nt)−J(t)`, kde `J(t)=ln((exp(t)−1)/t)` s J(0)=0.
Derivace `J'(t)=1/(1−exp(−t))−1/t` a vytvořující funkce Bernoulliho
čísel v konvenci B_1=+1/2 dávají
`κ_r=(n^r−1)B_r/r` pro r≥2, zejména κ_3=0.
Podkladová errata 2002 opravují argument derivace a 2021 přizpůsobují
její zápis nové konvenci Bernoulliho čísel; vzorce pro r≥2 se nemění.

Pro obecné momenty `M_r=E(X^r)` platí formálně
`E exp(tX)=1+∑_{r≥1}M_r t^r/r!`.
Dosadíme U=∑_{r≥1}M_r t^r/r! do ln(1+U)=∑_{j≥1}(−1)^(j−1)U^j/j.
Pro vektor nezáporných celých k_1,…,k_n s ∑r k_r=n a K=∑k_r
je výsledný příspěvek do κ_n roven

`(−1)^(K−1)n!(K−1)! ∏_{r=1}^n M_r^(k_r)/(k_r!(r!)^(k_r))`.

Součet přes tyto vektory je přesně odpověď 12; jde také o Arbogastův
vzorec z již kontrolované úlohy §1.2.5-21. Pro centrální momenty
`m_r=E((X−EX)^r)` je m_1=0 a κ_n se pro n≥2 nemění. Vynecháme tedy
členy k_1>0. Získáme κ_2=m_2, κ_3=m_3, κ_4=m_4−3m_2²;
necentrovaný čtvrtý je M_4−4M_1M_3−3M_2²+12M_1²M_2−6M_1^4.

Pokud všechny vyšší kumulanty mizí a σ²=κ_2>0, po standardizaci jsou
momenty 0 v lichých řádech a (2r−1)!! v sudých. To skutečně určuje
normální rozdělení: monotónní sčítání řady pro cosh dává
`E cosh(tY)=exp(t²/2)`, a z exp(|tY|)≤2 cosh(tY) plyne existence
exponenciálního momentu. Nyní lze zaměnit řadu charakteristické funkce
s očekáváním a získat exp(−t²/2). Pro σ=0 jde o degenerovaný případ.
Oprava 2024 „except possibly“ dovoluje i nulovou střední hodnotu a rozptyl.

## Normální limity, úlohy 13–15

Normální limita zde znamená, že charakteristická funkce centrované
veličiny vydělené její směrodatnou odchylkou konverguje bodově k
exp(−t²/2). Kniha tuto definici stanoví přímo v úloze 13.

Pro počet aktualizací označme μ=H_n−1 a σ²=H_n−H_n^(2).
Pak σ→∞ a μ/σ²→1. Pro pevné reálné t položme z=exp(it/σ), δ=z−1.
Protože ∑_{j≥2}j^(−2)<∞, rozklad PGF dává stejnoměrně pro malé δ

`ln G_n(z)=∑_{j=2}^n ln(1+δ/j)=δ μ+O(|δ|²)`.

Používáme větev logaritmu spojitou v δ=0. Taylorova řada δ poskytne

`ln(exp(−it μ/σ)G_n(exp(it/σ)))
 = −t² μ/(2σ²)+O(μ/σ³)+O(1/σ²) → −t²/2`.

To je samostatný důkaz závěru. Knižní postup přes funkci Γ má správnou
stejnoměrnost: z Eulerova součinu v `gamma-functions.md`, §Eulerova limita,
a H_n−ln n−γ=O(1/n) dostaneme
`G_n(z)=n^(z−1)/Γ(z+1) · (1+O(1/n))` stejnoměrně pro |z−1|≤1/2.
Odhad chyby součinu plyne z `∑_{j>n}j^(−2)=O(1/n)` a omezeného δ.
Proto lze v knižním důkazu dosazovat n-závislé z blížící se 1.
Údaj o exponenciálních ocasech na konci odpovědi je oddělený nález C0013.

Pro binomické rozdělení při pevném 0<p<1 a q=1−p máme

`exp(−it np/√(npq))(q+p exp(it/√(npq)))^n
 = (q exp(−itp/√(npq))+p exp(itq/√(npq)))^n`.

Lineární člen v závorce se ruší, kvadratický je −t²/(2n), zbytek
O(n^(−3/2)). Logaritmus n-té mocniny je −t²/2+O(n^(−1/2)), což
dokazuje úlohu 14. Historická oprava 1997 napravuje chybné závorky
v exponentu. Krajní p=0,1 nemají kladný rozptyl a standardizace se jich
netýká; nejde o nenulovou normální limitu deterministických veličin.

Poissonovo rozdělení s parametrem λ≥0 má pravděpodobnosti
exp(−λ)λ^k/k!, PGF exp(λ(z−1)) a všechny kumulanty rovné λ.
Při λ=np s pevným p>0 je logaritmus standardizované charakteristické
funkce `np(exp(it/√(np))−1−it/√(np))=−t²/2+O(n^(−1/2))`.
To dokazuje všechny části úlohy 15; p=0 opět znamená degenerovaný případ.

Souvislost s konvergencí distribučních funkcí je standardní věta o spojitosti
charakteristických funkcí. Citovaný primární článek Flajolet–Soria 1993,
s. 164, ji používá ve stejném významu a odkazuje na Billingsleyho §26.
Historickou citaci konkrétního překladu Gnedenka–Kolmogorova tím ještě
nepovažujeme za ověřenou.

Procenta na s. 104 byla ověřena racionálními intervaly: integrujeme
Taylorův polynom exp(−t²/2) na [0,r], r=1,2,3, se znaménkem a odhadem
zbytku z Taylorovy věty, a násobíme 200/√(2π). Certifikovaný interval π
pochází z dřívější samostatné kontroly. Všechny tři hodnoty se po
zaokrouhlení na 12 desetinných míst shodují s knihou. Detaily intervalů
jsou v `results/analysis-records.json`.

## Směsi a složení, úlohy 16–17

Pro směs rozdělení g_i s pravděpodobnostmi w_i≥0, ∑w_i=1, je
`g=∑w_i g_i`. Pokud μ_i a v_i označují jejich střední hodnoty a rozptyly,
pak `μ=∑w_i μ_i` a
`v=∑w_i v_i+∑_{i<j}w_i w_j(μ_i−μ_j)²`.
Poslední identita plyne z rozdílu `∑w_i μ_i²−(∑w_i μ_i)²`.

Složení h=g∘f je PGF součtu Y_1+…+Y_N, kde N má PGF g, veličiny Y_i
mají PGF f a všechny potřebné volby jsou nezávislé. Podmíněním na N=j
dostaneme f(z)^j a po zprůměrování g(f(z)). Potom
`mean(h)=mean(g)mean(f)` a
`var(h)=var(g)mean(f)²+mean(g)var(f)`.
Stejné vzorce vzniknou dvakrát řetězovým pravidlem a dosazením f(1)=1.
Interpretace pomocí potomků v generacích je správná právě za uvedené
nezávislosti a stejného rozdělení počtu potomků.
Chybné slovo „polynomy“ v důkazu uzavřenosti PGF je samostatný drobný
nález C0014; správný důkaz konvergentními nezápornými součty je tam uveden.
