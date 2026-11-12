# Tableaux36–37: koeficienty, nový důkaz háčkového vzorce a nekonečný součin

Zadání69–70/file80–81 a odpověď613/file624, originály zobrazené.
Přebírá se úplná obousměrná bijekce P0562–0569 z
notes/tableaux-proof-35-hillman-grassl.md. Tvar má N buněk; n
z knižní odpovědi odpovídá našemu N, proměnná m je součet hodnot.
Toto rozlišení je potřebné, protože asymptotika drží tvar i N pevné.

## P0570: úloha36(a), přesný koeficientový součin

Nechť H_c je kladná délka háčku buňky c. Každé q_c≥0 v bijekci
přispívá hmotností H_c q_c, takže jeho formální řada je
Σ_(q≥0)z^(H_c q)=(1−z^H_c)^−1. Hodnoty q_c jsou zcela nezávislé:
pravý směr inverze P0568 dokazuje, že každá nezáporná celočíselná
volba opravdu vzniká. Proto počet reverse plane partitions součtu m
je přesně [z^m]∏_c(1−z^H_c)^−1.
Pro prázdný tvar je součin1 a jediný objekt má součet0.

## P0571: pomocný asymptotický vzorec, včetně nezbytného faktoru1−z

Pro pevná kladná celá a_1,…,a_k označme

    F_k(m)=[z^m]1/((1−z)∏_(j=1)^k(1−z^a_j)).

Vytištěný samostatný faktor1−z je podstatný: bez něj by při
společném děliteli mohly nastat periodické výpadky hlavního členu.
Pro k=0 je F_0(m)=1 přesně. Pro k=1 je
F_1(m)=floor(m/a_1)+1=m/a_1+O(1). Pro k≥2 použijme

    F_k(m)=Σ_(r=0)^floor(m/a_k) F_(k−1)(m−a_k r).

Indukčně je F_(k−1)(s)=s^(k−1)/((k−1)!a_1…a_(k−1))
+O((s+1)^(k−2)), uniformně pro celá s≥0. Součet zbytků je
O((m+1)^(k−1)). Pro hlavní člen monotónnost t^(k−1) porovná
obdélníkové součty na mřížce kroku a_k s integrálem:

    Σ_(r=0)^floor(m/a_k)(m−a_k r)^(k−1)
       =m^k/(a_k k)+O((m+1)^(k−1)).

Příspěvek posledního zbytku intervalu délky<a_k i rozdíl horního
a dolního součtu mají tuto mez. Dělením příslušnými konstantami
dostáváme F_k(m)=m^k/(k!a_1…a_k)+O(m^(k−1)). Protože
binom(m,k)=m^k/k!+O(m^(k−1)), je to přesně

    F_k(m)=binom(m,k)/(a_1…a_k)+O(m^(k−1)).              (1)

Konstanty mohou záviset na pevných a_j a k. Odhad netvrdí
uniformitu při rostoucím tvaru nebo rostoucích délkách háčků.

## P0572: asymptotika obou druhů partičních dat a přísné sevření

Počet P_N(m) partičních seznamů m do nejvýše N částí má řadu
∏_(j=1)^N(1−z^j)^−1, již dokázanou v §5.1.1. Pro N≥2 tedy(1)
se samostatným faktorem j=1 dává

    P_N(m)=binom(m,N−1)/N!+O(m^(N−2)).                  (2)

Počet D_N(m) rozkladů na přesně N různých kladných částí
p_1>…>p_N>0 je P_N(m−N(N+1)/2): odečtení schodiště
(N,N−1,…,1) dává slabě klesající nezáporný seznam a převod je
obousměrný. Pevný posun argumentu změní hlavní polynom(2)
nejvýše oO(m^(N−2)), proto i D_N má stejný hlavní člen a zbytek.

Označme T_λ skutečný počet standardních tableaux tvaru λ, dosud
bez použití jeho háčkového vzorce. Každý výběr N různých kladných
hodnot součtu m lze do tvaru vložit přesně T_λ způsoby podle
jejich hodností. Dává to dolní mez T_λ D_N(m) pro počet R_λ(m)
reverse plane partitions.

Pro horní mez seřaďme hodnoty libovolného reverse plane partition
a při shodě rozhodněme pevným pořadím buněk po řádcích shora
dolů, v každém řádku zleva doprava. Toto pořadí rozšiřuje relace
buňky≤vpravo/dole, takže
hodnosti tvoří standardní tableau. Pár (seřazený seznam hodnot,
toto tableau) původní pole jednoznačně obnoví. Dostáváme injekci
do T_λ P_N(m) možností. Tedy

    T_λ D_N(m)≤R_λ(m)≤T_λ P_N(m),

a obě meze z(2) dávají

    R_λ(m)=T_λ binom(m,N−1)/N!+O(m^(N−2)).              (3)

Tím je doložen i přechod přes pole s opakovanými a nulovými
hodnotami; není jen prohlášen za zanedbatelný. Pro N=1 jsou
P_1(m)=D_1(m)=R_λ(m)=1 pro m≥1 a T_λ=1, takže zvláštní
jednobuňkový případ je přesný.

## P0573: úloha36(b), nekruhové odvození Theorem H

Každý neprázdný tvar má roh s délkou háčku1. V součinu P0570
jej vyberme jako samostatný faktor1−z a ostatních N−1 háčků
dosadíme do(1). Pro N≥2 dostáváme

    R_λ(m)=binom(m,N−1)/∏_c H_c+O(m^(N−2)).             (4)

Porovnání hlavních koeficientů(3) a(4), například po dělení
m^(N−1) a limitě, dává T_λ=N!/∏H_c. To je přesně Theorem H.
Pro N=1 platí přímo; prázdný tvar má T_∅=1 a prázdný součin1.
Předchozí důkaz Theorem H se zde nepoužil: T_λ byl jen počet
lineárních označení a bijekce35 stojí na vlastních algoritmech.

## P0574: úloha37, obdélníky a obousměrné otočení

Otočení r×c obdélníku o180 stupňů mění slabý pokles doprava/dolů
na slabý růst doprava/dolů. Je involutivní, zachovává nezápornost
i součet položek. Plane partitions v daném obdélníku jsou proto
v bijekci s reverse plane partitions téhož součtu.

Háček buňky(i,j) obdélníku má délku r+c−i−j+1. Po přeznačení
i′=r+1−i, j′=c+1−j je to i′+j′−1. Z36(a) proto dostáváme
přesně ∏_(i=1)^r∏_(j=1)^c(1−z^(i+j−1))^−1.

## P0575: neomezený tvar, nulové doplnění a formální limita

V „unbounded shape“ se stejné pole po doplnění nulami vpravo
a dole počítá jako týž objekt. Takto je určena i knižní limita
obdélníků. Ekvivalentní přesná definice je nekonečné nezáporné
celočíselné pole se slabým poklesem a konečným součtem; jeho
kladná podpora je Youngův tvar. Kdyby se naopak každé libovolné
nulové zvětšení konečného tvaru počítalo zvlášť, žádný konečný
počet by nevyšel. Použitá konvence je zde výslovná, ne skrytá.

Je-li při celkovém součtu m>0 kladná buňka(i,j), jsou kladné
všechny i·j buňky vlevo nahoře od ní. Proto i≤m a j≤m.
Každý objekt dané hmotnosti se tedy vejde do m×m; koeficient
stabilizuje, jakmile r,c≥m. Pro m=0 je jediný objekt nulové pole.

Na součinové straně koeficienty do stupně m ovlivňují jen faktory
s i+j−1≤m. Pro pevné k existuje právě k dvojic kladných celých
(i,j) s i+j−1=k. Koeficientová limita proto dává

    ∏_(k≥1)(1−z^k)^−k
      =1/((1−z)(1−z²)²(1−z³)³…).

Jde o formální mocninnou řadu, a pro každý koeficient byl limitní
přechod doložen stabilizací konečné množiny faktorů i objektů.

Úplné historické publikace Stanley1971, MacMahon1912 a Carlitz1967
nebyly nezávisle přezkoumány; u MacMahona je převzata známá oprava
svazku na A211 z2002. Matematické důsledky v odpovědích jsou celé
doloženy. Žádný nový nález ani numerický běh nevznikl.
