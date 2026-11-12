# Úloha 112: Chaseovo pořadí, obě malé části a Fourierův převod

7. listopadu 2026, X0124. Originál p94/file111, p555–556/file572–573
a odkazovaná rekurence (35) p365–366/file382–383 zobrazeny. Tato
poznámka dokládá úvod, celé (a),(b) a přípravu (c); obecnou dolní mez
dokončuje proof-098. Žádný matematický program ani census.

Rozlišujeme m proměnných původní funkce f a n=2^m vstupů funkce F,
kterými jsou všechny bity pravdivostní tabulky f. Koeficienty M(f)
jsou celočíselné podle již dokázané úlohy 12, proof-033. Prahové váhy
v (c) jsou celá čísla v definici na p75; libovolné reálné škálování
by samozřejmě žádnou absolutní dolní mez velikosti nemělo.

## Přesně potřebná část Chaseovy rekurence

Z originálu (35) přebíráme definici seznamů

    A_st = 1 B_(s,t−1), 0 reverse(A_(s−1,t)),
    B_st = 1 A_(s,t−1), 0 A_(s−1,t).

Pro záporný index jde o prázdný seznam; A_00=B_00 obsahuje jediné
prázdné slovo. Odtud A_s0=B_s0=(0^s), A_0t=B_0t=(1^t).
Indukcí podle s+t je každý seznam úplným seznamem slov s s nulami
a t jedničkami bez opakování: dva bloky rozlišuje první bit a jejich
suffixy dávají přesně dvě menší příslušné třídy. Rekurence tedy končí.

Pro s,t>0 mají oba seznamy první slovo 1^t 0^s; poslední slova jsou

    last A_st = 0 1^t 0^(s−1),
    last B_st = 0^min(s,2) 1^t 0^(s−min(s,2)).

To plyne přímo z posledního bloku a indukce; s=1 používá singleton
A_0t. Uvnitř bloků se sousední slova mění jen 01↔10 či 001↔100
indukčně, také při obrácení seznamu. Na hranici bloků A je pro s≥2
přechod

    100 1^(t−1) 0^(s−2) → 001 1^(t−1) 0^(s−2),

a pro s=1 přechod 10 1^(t−1)→01 1^(t−1). Hranice B je
10 1^(t−1) 0^(s−1)→01 1^(t−1) 0^(s−1). Platí i při t=1
díky uvedeným singletonovým základům. Tím je celá potřebná sousednost
dokázána bez předpokládání obecné klasifikační věty N nebo algoritmu C.

Po zapracování errata z 22.1.2012 spojujeme
A_(m,0), A_(m−1,1), …, A_(0,m). Poslední slovo vrstvy k<m je
0 1^k 0^(m−k−1), první slovo další vrstvy je 1^(k+1) 0^(m−k−1).
Na spojích se tedy mění jediná 0→1. Dostáváme všech 2^m slov,
seřazených podle počtu jedniček, se všemi přesně uvedenými přechody.

Pro m=4 rekurence dává jednotlivé vrstvy

    0000;
    1000,0010,0001,0100;
    1100,1010,1001,0011,0101,0110;
    1110,1101,1011,0111;
    1111.

To je všech šestnáct vytištěných slov ve správném pořadí. Převod
exponentů na monomy vysvětluje i první uvedené členy 1,x1,x3,x4,x2.
Při m=0 máme jediný prázdný exponent, bez sousedního přechodu.
Tato lokální kontrola neuzavírá zbytek p365–366 ani implementaci C.

## Vytištěný čtyřproměnný příklad

První disjunkt je ((x1 XOR ¬x2) AND x3). Ekvivalence x1, x2 má
celočíselný polynom 1−x1−x2+2x1x2. Druhý disjunkt má polynom
x1(1−x3)x4. Disjunkty jsou disjunktní kvůli x3/¬x3, takže OR
je zde součet. Výsledek je přesně

    x3 − x1x3 + x1x4 − x2x3 + 2x1x2x3 − x1x3x4.

Uvedené exponenty mají v seznamu indexy 2,6,7,10,11,13. Poslední
nenulový člen je tedy −x1x3x4 a F(f)=0. Pro nulový polynom
rovněž F=0, protože žádný jeho koeficient není kladný.

## (a) Všech šestnáct funkcí

Z úplných polynomů Table 1 v proof-028 a jejich celočíselné formy
v proof-033 dostáváme následující poslední členy v pořadí 1,x,y,xy.
Čtyřbitový vstup má pořadí 00,01,10,11.

| f | Poslední člen | F |
|---|---|---|
| 0000 | 0 | 0 |
| 0001 | xy | 1 |
| 0010 | −xy | 0 |
| 0011 | x | 1 |
| 0100 | −xy | 0 |
| 0101 | y | 1 |
| 0110 | −2xy | 0 |
| 0111 | −xy | 0 |
| 1000 | xy | 1 |
| 1001 | 2xy | 1 |
| 1010 | −y | 0 |
| 1011 | xy | 1 |
| 1100 | −x | 0 |
| 1101 | xy | 1 |
| 1110 | −xy | 0 |
| 1111 | 1 | 1 |

Všech osm kladných případů i posloupnost šestnácti členů souhlasí
s odpovědí. Použity již uzavřené polynomy, nikoli nová enumerace.

## (b) Obecný smíšený radix a skutečné oddělení znamének

Pro podporu T velikosti k je koeficient

    c_T = Σ_(U⊆T) (−1)^(|T|−|U|) f(1_U).

Pro k≥1 je v součtu 2^(k−1) kladných i záporných členů, a proto
−2^(k−1)≤c_T≤2^(k−1). Pro T=∅ je c_∅=f(0)∈{0,1}.
To odpovídá vytištěným zaokrouhleným mezím i pro k=0.

Nechť α_0,…,α_(n−1) je právě doložené pořadí. Položme

    R_j=2^|α_j|+1,   M_0=1,   M_j=∏_(i<j) R_i,
    D(f)=Σ_j M_j c_(α_j).

Každé c_T je celočíselná lineární kombinace vstupních bitů, tedy také
D. Je-li j≥1 poslední nenulový koeficient, platí díky M_1=2

    Σ_(1≤i<j) M_i 2^(|α_i|−1)=(M_j−2)/2.

Celý nižší součet proto leží mezi 1−M_j/2 a M_j/2, zatímco
|M_j c_(α_j)|≥M_j. Jeho znaménko nelze zvrátit. Pokud jsou všechny
nekonstantní koeficienty nulové, je D=c_∅∈{0,1}. Ve všech případech

    F(f)=[D(f)>0]=[D(f)≥1].

Máme tedy celočíselnou prahovou reprezentaci a nezůstává neprokázané
„přenášení“ záporných číslic. Totéž zahrnuje m=0, kdy D=f(0).

Pro m=2 jsou M=(1,2,6,18). Po dosazení koeficientů

    D=18c_11+6c_01+2c_10+c_00
     =18f_11−12f_01−16f_10+11f_00.

Vytištěný medián má 57 vstupů: 18 kopií f_11, 12 kopií ¬f_01,
16 kopií ¬f_10 a 11 kopií f_00. Součet je D+28, práh 29,
takže přesně D≥1. Také kratší medián

    <f_11,f_11,¬f_01,¬f_10,f_00>

je správný: má podmínku 2f_11−f_01−f_10+f_00≥1. Při f_11=0
přijme právě 1000, při f_11=1 všechny případy kromě 0111. To je
přesně osm pravdivých řádků předchozí tabulky.

## Fourierova transformace se všemi normalizačními faktory

Ztotožněme bitový index a s jeho podporou. Pro S⊆[m] definujme
χ_S(a)=∏_(i∈S)(2a_i−1)=(−1)^|S\a|. Potom

    F_S = Σ_a χ_S(a)(f_a−1/2)
        = Σ_a χ_S(a)f_a − (n/2)[S=∅],
    w_S = Σ_a χ_S(a)v_a.

Z faktorizace po souřadnicích plyne Σ_a χ_S(a)χ_T(a)=n[S=T].
Proto přesně

    v_a = (1/n) Σ_S χ_S(a)w_S,
    Σ_S w_S F_S = n Σ_a v_a(f_a−1/2).

Originál na p556 faktor 1/n obsahuje. Žádný problém normalizace
se nepotvrdil. Oba uvedené příklady w_01 a F_11 jsou okamžitým
dosazením znamének do těchto vzorců.

Rozvinutí M(f) a součet po bitových souřadnicích dávají obecně

    F_S = Σ_(T⊇S) 2^(m−|T|) c_T − (n/2)[S=∅].

Je-li nějaká souřadnice S mimo T, příslušný součet je nula;
jinak každá souřadnice T přispěje faktor 1 místo 2. To dokazuje
vzorec. Trojúhelníkový systém podle velikosti podpory ukazuje oběma
směry, že při vymizení všech stupňů >k>0 platí
F_S=2^(m−k)c_S na stupni k. V rámci stupně tedy zůstává každý
koeficient i pořadí znamének stejné. Nejvýznamnější nenulové F_S má
stejné znaménko jako nejvýznamnější koeficient M(f). Pro konstantní
f=0,1 je jediné nenulové F_∅ rovno −n/2,+n/2, což dává stejnou
klasifikaci. Transformovaný vektor není nulový, neboť f−1/2 není.

## Proč smíme centrovat každou reprezentaci a proč w_S≥1

Při nahrazení celé tabulky f za 1−f se všechny nekonstantní
koeficienty M změní na opačné; dvě konstantní funkce se prohodí.
F je tedy self-duální jako funkce n vstupů. Je-li F(y)=[v·y≥t]
a V=Σv_a, každá komplementární dvojice má opačné výstupy. U pravdivého
y máme současně v·y≥t a v·y>V−t, tedy v·y>V/2; u nepravdivého
je tomu opačně. Proto bez změny celočíselných vah

    F(f)=[Σ_a v_a(f_a−1/2)>0]=[Σ_S w_S F_S>0].

Pro libovolné S, k=|S|, zvolme f=(1+χ_S)/2. V bitovém zápisu je
to XOR proměnných S, navíc XOR [k je sudé]. Jediné nenulové F je
F_S=n/2>0. Pro k≥1 je vedoucí člen 2^(k−1)∏_(i∈S)x_i; pro
k=0 máme f=1 a člen 1. To je přesně opravené ceil(2^(k−1)).
F tohoto testu je 1, takže w_S>0. Jelikož v_a jsou celá čísla,
jsou také w_S celá a w_S≥1. Zahrnutí S=∅ je podstatné.

Pokud přidáme nepoužívanou proměnnou, přímým součtem přes její bit
dostaneme F_(S,0)=2F_S a F_(S,1)=0, včetně konstantní korekce.
Tím je ověřen také tento dodatek odpovědi. Obecný růst jednotlivých
w, všechny vytištěné testy a převod na všechny původní váhy následují
v proof-098.

## Zdroje a rozsah

Pět vrstev all4a-pre, all4a, err4a, all4f0, err4f0 bylo prohledáno
podle úlohy, stran i Fourier/threshold tématu. Zapracováno n→m v
Chaseových indexech (22.1.2012), výslovné n=2^m a opravený paritní
test s k≥0 (14.12.2013). Pro použitou rekurenci byly navíc prohlédnuty
all4f3 a err4f3; žádná změna jejího matematického obsahu nenalezena.
Známé opravy nejsou nálezy. Historickou prioritu Chaseovy konstrukce
tato lokální kontrola nezjišťuje.
