# §7.1.1–14 až 17: optimální self-dual funkce, bitové polynomy a NAND

6. listopadu 2026, X0064. Původní zadání p80–81/file97–98 a odpovědi
p536/file553. Negace ve třetí odpovědi14 je **¬x₃**, nikoli x₃ z OCR.
Žádný matematický program, enumerace funkcí nebo opakování starého
binomického důkazu.

## P0587–P0588: obecné optimum self-dual funkce

**P0587:** self-dualita znamená f(¬a)=1−f(a). Osm stavů tří
jednotek se dělí na čtyři disjunktní komplementární dvojice.
V každé dvojici může být pravdivý právě jeden stav. Aby se
maximalizovala pravděpodobnost f=1, je nutné i postačující
v každé dvojici zvolit pravděpodobnější stav. Volby jsou nezávislé
a součet jejich příspěvků je celá dostupnost. Při shodě jsou
obě volby optimální; při všech ostrých nerovnostech je optimum
jedinečné. Tento argument platí i při p_j=0 nebo1.

**P0588:** konkrétní zadání má 0<p_j<1, takže lze použít
r_j=p_j/(1−p_j). Pravděpodobnost stavu a je
∏(1−p_j) · ∏_(j:a_j=1)r_j. Porovnání čtyř dvojic proto dává:

| stav zvolený za pravdivý oproti komplementu | přesná podmínka |
|---|---|
| 111 oproti 000 | r₁r₂r₃>1 |
| 110 oproti 001 | r₁r₂>r₃ |
| 101 oproti 010 | r₁r₃>r₂ |
| 100 oproti 011 | r₁>r₂r₃ |

To jsou všechny čtyři ekvivalence v odpovědi. Není zde předpoklad
monotónnosti f; při některých pravděpodobnostech je optimem negace.

## P0589–P0591: všechny tři konkrétní příklady úlohy14

**P0589, (a):** p=(9/10,4/5,7/10) dává r=(9,4,7/3).
Podmínky jsou 84>1, 36>7/3, 21>4 a nakonec
9<28/3. Pravdivé stavy jsou 111,110,101,011, přesně ternární
většina. Její dostupnost je
p₁p₂+p₁p₃+p₂p₃−2p₁p₂p₃=451/500.
Poslední těsná nerovnost není nahrazena odhadem.

**P0590, (b):** p=(4/5,3/5,2/5) dává r=(4,3/2,2/3).
Platí 4>1, 6>2/3, 8/3>3/2 a 4>1. Zvolené stavy
111,110,101,100 jsou právě x₁=1. Jedinečné optimum je
x₁ a dostupnost 4/5.

**P0591, (c):** p=(4/5,3/5,1/10) dává r=(4,3/2,1/9).
Máme 2/3<1, 6>1/9, 4/9<3/2 a 4>1/6.
Zvolené stavy jsou 000,110,010,100, přesně x₃=0.
Odpověď ¬x₃ je správná; dostupnost je 9/10.

Všechny nerovnosti jsou ostré, tedy uvedené funkce jsou nejen
nějakými optimy, ale v těchto třech případech jedinými self-dual
optimy na všech osmi stavech.

## P0592: přesně převzatý binomický vstup pro úlohu15

Přebírá se již uzavřený argument
[svazek1, binomial-congruences.md](../../vol1/notes/binomial-congruences.md),
úvod a rovnice (L1)–(L2), potvrzený v úplném mapování
[quality-recovery §1.2.6, úloha10](../../vol1/notes/quality-recovery-section-1.2.6-2026-11-06.md).
Jeho přesný použitý rozsah je:

1. Pro pevné k≥0 je binom(t,k) celé pro každý celý t, i záporný.
2. Pro nezáporná t,k a p=2 je binom(t,k) liché právě tehdy,
   když každý jedničkový bit k je také jedničkovým bitem t.

Druhý bod plyne přímo z součinu jednociferných faktorů (L2);
první je v převzatém úvodu doložen podmnožinami a vztahem pro
záporný horní index. Obecný Lucasův důkaz, historická pramenná
kontrola ani žádný census se znovu neprovádějí.

V pořadí t=(xₙ…x₁)₂ tak pro k=Σ_(j∈S)2^{j−1} dostáváme

    binom(t,k) mod 2 = ∏_(j∈S)x_j.

Kontrolované předpoklady jsou přesně splněny: t je nezáporný
zakódovaný vstup a k pevný nezáporný index monomu.

## P0593: obecný polynom z úlohy15 a integrálnost i mimo bitový rozsah

P0532 dává f(x)=Σ_S a_S∏_(j∈S)x_j modulo2, a_S∈{0,1}.
Polož

    F(t)=Σ_S a_S binom(t, Σ_(j∈S)2^{j−1}).

Každý sčítanec je polynom v t s racionálními koeficienty a je
celočíselný na **všech** celých t podle P0592. Součet je proto
celočíselný i pro záporná t; na zakódovaných 0≤t≤2ⁿ−1 má
zbytek modulo2 právě f. Stupeň nepřekročí 2ⁿ−1.
Nezaměňuje se celočíselně hodnotový polynom s polynomem, jehož
každý koeficient musí být celé číslo; zadání vyžaduje první věc.
Pro n=0 lze vzít konstantu f().

## P0594: oba vytištěné příklady a přesná interpolace bez modulo2

11=(1011)₂, tedy binom(t,11) mod2=x₄∧x₂∧x₁,
jak stojí v odpovědi. Jde o p=2 specializaci již převzaté věty.

Pro **čtyřbitový** rozsah 0≤t≤15 je
D(t)=binom(t,11)binom(15−t,4) přesně indikátorem t=11.
Je-li t<11, první koeficient je0. Je-li t>11, druhý má nezáporný
horní index menší než4, tedy je0. Při t=11 jsou oba koeficienty1.
Tím je vytištěný přesný příklad x₄∧¬x₃∧x₂∧x₁ doložen.
Netvrdí se periodicita tohoto pevného polynomu mimo čtyřbitový rozsah.

Obecně pro N=2ⁿ−1 a 0≤k≤N jsou
D_k(t)=binom(t,k)binom(N−t,N−k) přesně indikátory t=k
na celém celočíselném intervalu0,…,N. Tentýž dvoustranný argument
to dokazuje pro všechny k, i k=0,N. Proto
Σ_k f(bits(k))D_k(t) reprezentuje f na těchto vstupech dokonce
bez modulo2 a stále je celočíselně hodnotovým polynomem pro
všechny celé t. Tím je vysvětlen i celý matematický dodatek odpovědi,
nikoli jen zvláštní číslo11.

## P0595: úloha16, XOR i obyčejný součet úplných mintermů

Dva různé úplné mintermy vyžadují opačné hodnoty alespoň jedné
proměnné, takže nemohou být současně pravdivé. Na každém vstupu
je proto počet pravdivých členů úplné DNF buď0, nebo1.
OR, XOR i obyčejný součet členů mají stejnou hodnotu. Prázdná
DNF je0 a nulární jednička je jediný prázdný minterm1; oba
okraje také souhlasí.

Obecná DNF toto nezaručuje: x∨y má při x=y=1 hodnotu1,
zatímco XOR dává0 a součet2. Dodatek odpovědi tedy správně
odlišuje úplnou mintermovou formu od libovolné DNF. Netvrdí se,
že jiné speciální disjunktní DNF nemohou mít stejnou vlastnost.

## P0596: úloha17 a přesná arita NAND

Pro s≥0 definuj s-ární NAND
N_s(u₁,…,u_s)=¬(∧_k u_k). Pro s=1 tedy N₁(u)=¬u,
nikoli u; pro s=0 vychází N₀=0.
Jestliže T_j=∧_k u_jk, pak

    N_m(N_s1(u₁₁,…), …, N_sm(u_m1,…))
       = ¬(∧_j ¬T_j)
       = ∨_j T_j.

Dvouúrovňová NAND realizace DNF je tudíž správná. Platí také při
prázdných blocích: prázdný člen DNF je1, jeho vnitřní NAND0
vynutí vnější výstup1; bez členů je vnější N₀=0.

Binární NAND ale není asociativní; to už přesně dokazuje
P0562, svědek001. Například N₂(N₂(0,0),1)=0, ale
N₃(0,0,1)=1. Quickův řetězový symbol proto funguje jen při
výslovném s-árním významu, ne jako opakované libovolně závorkované
binární použití. To zahrnuje i varování odpovědi o jednom vstupu.
Historickou totožnost uvedeného studenta samostatně neověřuji.

## Meze a pokračování

Všechny části a dodatky úloh14–17 mají argumenty. Byly převzaty
hotové důkazy P0532/P0562 a přesný binomický argument svazku1;
žádné opakované výpočty. Nový nález ani kandidát nevznikl.

P80/file97 má nyní argumenty úloh3–14, ale jeho globální označení
ponechává explicitní limit P0580 u rozsahu koeficientové meze.
P81 i p536 zůstávají partial kvůli dalším úlohám. Další jsou
18–21 a s nimi přirozeně propojený hlavní text p54–55 o
prvoimplikantech, krychlích a monotónních funkcích.
