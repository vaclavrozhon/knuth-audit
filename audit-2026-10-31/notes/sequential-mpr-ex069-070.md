# D171–D172 — celé MPR69–70

7. listopadu 2026. Přímo zobrazeno zadání p18–19/file38–39,
odpovědi p381/file401, autorův PS p18–19/file24–25 a p37–38/file43–44.
Odkazované metody ze svazku1, §1.2.5, byly zobrazeny na původní
p46/file61. Převzata je pouze definice těchto metod, nikoli kontrola
celé stránky nebo sekce jiného svazku. Všech šest vrstev errat
a tři TeX zdroje jsou zaznamenány v hashovaném manifestu.
Žádný výčet, numerický běh ani opakování starých testů.

## 69: obě konstrukce a pravděpodobnostní model

Permutaci π délky n≥1 přiřadíme uzel (r,b) s r+b=n+1,
tedy úroveň n−1 obrázku P. Základní permutace (1) odpovídá
kořenu (1,1). Přechod n−1→n ze zadání budeme zapisovat
jako n→n+1; jde pouze o pojmenování aktuální délky.

**Metoda1.** Nechť r je pozice prvku1, tedy π_r=1, a b=n+1−r.
Vložíme nové maximum n+1 do jednoho z n+1 míst, každého
se stejnou pravděpodobností. Pozici nového prvku označme k.
Právě pro k≤r se původní prvek1 posune doprava a nový uzel
je (r+1,b). Těchto možností je r. Ostatních b možností
ponechá pozici1 a dává (r,b+1). Proto

    P((r+1,b) | celá dosavadní historie)=r/(r+b),
    P((r,b+1) | celá dosavadní historie)=b/(r+b).

To jsou přesné předpoklady urnového modelu. Také po zapomenutí
permutací a podmínění pouze historií uzlů zůstávají stejné
pravděpodobnosti: všechny slučované permutace mají v daném
uzlu tytéž počty míst. Nejde pouze o shodu marginál.

Každá výsledná permutace má jediného předchůdce: odstraníme
největší prvek. Jeho pozice určí jediné k. Indukce od (1)
dokazuje úplnost i absenci duplicit. Každá historie délky n
má pravděpodobnost 1/(2·3·…·n)=1/n!. V každé pozici prvku1
je právě (n−1)! permutací, takže n uzlů úrovně n−1 má
pravděpodobnost1/n. Pro pevné n jde o n−1 konečných vložení.

**Metoda2.** Nyní r=π₁, b=n+1−r. Zvolíme k rovnoměrně
z1,…,n+1, všechny staré hodnoty≥k zvýšíme o1 a připojíme k
na konec. Přejmenované staré hodnoty jsou právě
{1,…,n+1} bez k, takže výsledek je permutace. První hodnota
se zvýší právě při k≤r. Znovu máme r možností pro (r+1,b)
a b pro (r,b+1), se stejnými pravděpodobnostmi vzhledem
k celé historii i po zapomenutí permutací.

Jednoznačná inverze odstraní poslední k a každou zbývající
hodnotu>k sníží o1. Indukce opět dává všechny permutace
právě jednou a pravděpodobnost1/n!. Pro každou první hodnotu
je (n−1)! permutací. Obě krajní volby k=1,n+1 jsou zahrnuty;
každá konstrukce pro pevné n používá konečný počet operací.

Příklad π=3124 má pozici prvku1 rovnou2 a první hodnotu3.
Při celkem5míčcích dává Metoda1 uzel (2,3), Metoda2 (3,2),
přesně jako tisk.

**Inverzní dovětek.** Tvrzení o inverzích má přirozený význam
při stejných volbách k v obou metodách. Nechť σ=π⁻¹.
Vložíme-li v Metodě1 maximum n+1 na pozici k, je inverze
nové permutace

    σ′_j=σ_j+[σ_j≥k] pro1≤j≤n,    σ′_{n+1}=k.

První formule vyjadřuje posun starých prvků, druhá pozici
nového maxima. Jsou to přesně operace Metody2 na σ se stejným k.
Protože (1) je vlastní inverzí, indukce dokazuje celý dovětek.
Nevykládáme jej jako tvrzení o dvou nezávisle vylosovaných
permutacích; explicitní párování i oba zákony jsou doloženy.

## 70: všechny barvy, stavy a počty

Nechť c≥1 je počet barev, každá s jedním počátečním míčkem.
Kořenu přiřadíme permutaci1,…,c−1 délky c−1 (pro c=1 prázdnou).
Metodou1 vkládáme maxima c,c+1,… . Prvky1,…,c−1 nazvěme
kotvami; jejich vzájemné pořadí se nemění. Obráceně každou
permutaci délky n≥c−1 se vzestupným pořadím kotev vrátíme
jednoznačně do kořene postupným odstraněním maxim n,…,c.
To dokazuje přesný prostor výsledků a jedinečnost historií.

Počet výsledků je

    binom(n,c−1)·(n−c+1)!=n!/(c−1)!.

Volíme pozice kotev a potom uspořádání ostatních prvků.
Každá historie má pravděpodobnost 1/(c(c+1)···n)=(c−1)!/n!,
tedy všechny výsledky jsou stejně pravděpodobné. V kořeni
má prázdný součin hodnotu1. Pro pevné n proběhne právě
n−c+1 konečných vložení.

Označme pozici kotvy j jako P_j, doplňme P₀=0,P_c=n+1
a položme A_j=P_j−P_{j−1} pro1≤j≤c. Všechny A_j jsou
kladné a jejich součet je n+1. Pro vložení do pozice k
existuje právě jedno j s P_{j−1}<k≤P_j. Předchozí kotvy
zůstanou, následující se posunou o1, proto se zvětší
pouze A_j a právě o1. Interval obsahuje A_j pozic, takže

    P(A′=A+e_j | celá historie)=A_j/(n+1).

Všechny pozice1,…,n+1 jsou rozděleny do těchto disjunktních
intervalů, včetně posledního za poslední kotvou. Jde tedy
přesně o urnový model; zapomenutí permutační historie
neovlivní pravděpodobnosti.

**Martingale.** Souřadnice podílu Z_n=A/(n+1) leží v[0,1],
jsou integrabilní a známé z historie. Pro každé j platí

    E(A′_j/(n+2) | historie)
      =(A_j+A_j/(n+1))/(n+2)=A_j/(n+1).

Tuplový zápis v knize vyjadřuje tuto souřadnicovou vlastnost;
každá pevná reálná lineární kombinace souřadnic je obyčejný
skalární martingale. Lze začít již v n=c−1; tisk uvádí
platný ocas n=c,c+1,…, nikoli neplatný kořenový index.

**Uniformita kompozic.** Každá kladná kompozice
A₁+…+A_c=n+1 určí právě pozice kotev P_j=A₁+…+A_j.
Na zbývajících pozicích je (n−c+1)! uspořádání ostatních prvků,
nezávisle na kompozici. Její pravděpodobnost je tedy

    (n−c+1)! / (n!/(c−1)!)=1/binom(n,c−1).

Počet kompozic binom(n,c−1) je počet voleb c−1 řezů mezi
n+1 jednotkami. Bijekce zároveň dokazuje úplnost stavů.
Pro c=3 má3142 kotvy na P₁=2,P₂=4 a P₃=5, takže A=(2,2,1).

Pro c=1 nejsou kotvy, A₁=n+1, podíl je stále1 a existuje
jediná kompozice, binom(n,0)=1. Pro c=2 dostáváme Metodu1
z69. Kořen n=c−1 má jedinou kompozici (1,…,1). Případ c=0
není urnový model s možností losování a není součástí tvrzení.

**Počáteční r,b.** Pro kladná celá r,b použijeme c=r+b barev
a první r barev sjednotíme do červené. Položme R=Σ_{j≤r}A_j
a B=Σ_{j>r}A_j. V kořeni je R=r,B=b. Součet pravděpodobností
disjunktních prvních r barev je R/(R+B), ostatních B/(R+B).
Sjednocený proces je proto přesně požadovaný dvoubarevný model.
Podíl R/(R+B) je součtem prvních r souřadnic martingalu.
Případné degenerované r=0 nebo b=0 při r+b>0 dávají
konstantní podíl0 nebo1 a fungují přímo.

## Bibliografie, errata a přesný rozsah

[Vybrané práce Davida Blackwella](https://celebratio.org/Blackwell_DH/article/252/)
uvádějí metadata Blackwell–Kendall, J. Applied Probability1(2),
prosinec1964, pp284–296. Reprodukovaný původní abstrakt popisuje
libovolný počet barev s jedním počátečním míčkem každé barvy
a přidání stejné barvy. Tematické přiřazení citace je ověřeno
v tomto rozsahu; celý článek a jeho Martinova hranice se
nepřebírají. Metadata ani abstrakt nedokazují historické
prvenství: slovo „first“ zůstává výslovně bibliograficky
neověřené. Žádný matematický krok na článku nezávisí.
Přímý vydavatelský odkaz nebyl dostupný; dlouhá rešerše se nekoná.

V šesti lokálních vrstvách errat a třech TeX zdrojích byly
posouzeny shody stran, čísel úloh i obsahových hesel. Odpovědi69/70
v jiných sekcích, známá změna63 a sousední změna72 nejsou opravou
tohoto bloku. Použitelná oprava69–70 nebyla nalezena. Žádný nový
nález ani kandidát nevznikl.

Celé69 a70, všechny příklady, inverzní dovětek, uniformita
i seskupení barev jsou uzavřeny. Tím je dokončen zbývající
matematický obsah file38. File39 a401 zůstávají partial
pro další úlohy; starší výjimky se nepřekrývají.

