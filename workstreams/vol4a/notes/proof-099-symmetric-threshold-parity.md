# Symetrické funkce p77–78 a celé úlohy 113–115

7. listopadu 2026, X0125. Původní p77/file94, p78/file95,
p94/file111 a odpovědi p556/file573 zobrazeny. P1200–P1212.
Žádný matematický program, enumerace funkcí ani nový nález.
Theorem T na horní části p77 je přesně převzata z proof-084.

## Definice symetrie, všechny příklady a (90)

Dva bitové vektory mají stejnou váhu právě tehdy, když je převádí
permutace souřadnic: bijektivně spárujeme jejich pozice jedniček
a zvlášť pozice nul. Proto permutační invariance přesně znamená
závislost pouze na s=x1+…+xn. Opačný směr plyne ze zachování s
permutací. To platí i pro n=0 s jediným vstupem.

S_T má tedy hodnotu [s∈T]. Pro pět vstupů S_{1,3,5} je XOR,
protože parita součtu je 1 právě pro lichá s. Medián pěti vstupů
má práh 3, tedy S_{3,4,5}. Připojení dvou nul dává medián sedmi
s prahem 4, tedy S_{4,5}. S_3 na šesti vstupech vyžaduje přesně
tři jedničky a tři nuly, jak je uvedeno.

Pro každé 0≤k≤n je s=k ekvivalentní s≥k a s<k+1. To dokazuje
(90), včetně k=0 a k=n, pokud S_≥k=[s≥k]; S_≥0 je konstanta 1
a S_≥(n+1) konstanta 0. Prázdný seznam přípustných vah tedy dává
konstantu 0. Všechny S_≥k jsou prahové s vahami 1 a prahem k.

## Celý příklad (91), včetně všech třinácti součtů

Pro s∈{0,…,12} položme a=[s≥4], b=[s≥7], c=[s≥10]. Nerovnost
s≥2+4a+2b+5c je pravdivá právě na vrstvách 2,3,6,8,9: v blocích
0–3, 4–6, 7–9 a 10–12 má příslušné pravé strany 2,6,8,13.

První vnitřní medián má pět nul a dvanáct negovaných vstupů,
délku 17 a práh 9. Jeho součet je 12−s, tedy výstup 1−a.
Druhý má jednu jedničku a dvanáct negovaných vstupů, délku 13
a práh 7, tedy výstup 1−b. Třetí má sedm jedniček a dvanáct
negovaných vstupů, délku 19 a práh 10, tedy výstup 1−c.

Vnější medián obsahuje dvě nuly, dvanáct původních vstupů a 4,2,5
kopií těchto tří výsledků. Délka je přesně 25 a práh 13. Počet
jedniček je s+11−4a−2b−5c, postupně

    11,12,13,14,11,12,13,12,13,14,10,11,12.

To je všech třináct vytištěných hodnot a stejná podmínka jako první
nerovnost. Konstrukce má čtyři prahové operace a hloubku dvě,
protože tři vnitřní operace jsou nezávislé.

Také obecné tvrzení o dvou úrovních má explicitní konstrukci.
Je-li f_s∈{0,1} hodnota libovolné symetrické funkce na vrstvě s,
pak pro každý s∈{0,…,n} teleskopicky

    f_s=f_0+Σ_(k=1)^n (f_k−f_(k−1))[s≥k].

Vnitřní brány [s≥k] mají práh k. Vnější brána s celočíselnými
vahami f_k−f_(k−1) a prahem 1−f_0 vrací právě f_s. Nulové
koeficienty lze vynechat; jde nejvýše o n+1 prahových operací
v hloubce dvě, včetně konstant a n=0. Je to postačující obecná
konstrukce; neobsahuje tvrzení o optimálním počtu bran.

## Úloha 113: všechny tři prahy a jejich mediánový zápis

Nechť s=x1+…+x12. Pro g1=[s≥6] a g2=[s−6g1≥2] jsou pravdivé
vrstvy g2 přesně 2,3,4,5,8,9,10,11,12: v prvním pásmu s<6
odečítáme 0, ve druhém 6. Poslední skóre −2s+13g1+7g2 má
v pásmech s=0–1,2–5,6–7,8–12 postupně tvary

    −2s; 7−2s; 13−2s; 20−2s.

Je alespoň 1 právě na s=2,3,6,8,9. To dokazuje celý vytištěný
tříprahový postup, ne pouze závěrečné označení g3.

Medián pro g1 má jednu jedničku a dvanáct x_i, tedy délku 13
a práh 7; je ekvivalentní s≥6. Medián pro g2 má tři jedničky,
dvanáct x_i a šest kopií ¬g1, tedy délku 21, práh 11 a skóre
9+s−6g1. Třetí medián má pět nul, dvě kopie každého ¬x_i,
třináct kopií g1 a sedm kopií g2: délka 49, práh 25 a skóre
24−2s+13g1+7g2. Všechny negace, násobnosti i prahy tedy přesně
odpovídají třem nerovnostem v zadání.

Jsou to tři prahové operace v hloubce tři. Pro tento konkrétní
příklad se počet oproti čtyřem branám (91) skutečně zmenšil;
není tím prokázána globální optimalita všech možných obvodů.

## Úloha 113: všechny čtyři prahy druhé funkce

V odpovědi je g1=[s≥6], g2=[s≥3],
g3=[s−5g1−2g2≥2] a g4=[2s−15g1−9g3≥1]. První dvě brány
lze vyhodnotit paralelně. Skóre g3 je s pro s≤2, s−2 pro
3≤s≤5 a s−7 pro s≥6. Pravdivé vrstvy jsou tedy přesně
2,4,5,9,10,11,12, jak se uvádí.

Pro s=0,…,12 jsou skóre poslední brány postupně

    0,2,−5,6,−1,1,−3,−1,1,−6,−4,−2,0.

Práh 1 přijímá právě 1,3,5,8, takže g4=S_{1,3,5,8}. Ověřeny
všechny vrstvy včetně rovnosti 0 na obou koncích; záměna za ≥0
by nefungovala. Konstrukce má čtyři operace a hloubku tři.

## Úloha 114: konkrétní funkce i obecné vložení

Argumenty x,x,x,x,y,y,z mají součet 4x+2y+z. Hodnota 3 nastává
jen při (x,y,z)=(0,1,1), hodnota 6 jen při (1,1,0). Výsledek
je tedy přesně (¬x AND y AND z) OR (x AND y AND ¬z).

Pro libovolnou booleovskou funkci n vstupů vytvořme 2^n−1
argumentů: 2^(n−i) kopií x_i pro každé i=1,…,n. Jejich součet
je binární číslo k=Σ_i 2^(n−i)x_i, které jednoznačně identifikuje
původní vstup. Vyberme T jako množinu čísel těch vstupů, na nichž
f=1. Pak S_T na uvedených opakovaných argumentech je právě f.
To dokazuje obecný dodatek, včetně konstant. Pro n=0 je seznam
argumentů prázdný a volby T=∅ nebo T={0} dávají obě konstanty.

## Úloha 115 a (92): redukce a lichý případ

Předpoklad je výslovně m>0. Indexy x1,…,x_(2m) bereme cyklicky,
x0 zůstává samostatný. Každý vnitřní s_j je medián 2m+1 literálů
a vnější medián má rovněž 2m+1 vstupů. Při komplementování všech
původních bitů se každý jeho literál komplementuje; self-dualita
lichého mediánu proto komplementuje postupně každý s_j i celý
výsledek. XOR lichého počtu 2m+1 bitů je také self-duální. Stačí
tedy dokázat rovnost pro x0=0; druhá polovina vstupů následuje
komplementací, aniž by se předpokládala dosud nedokázaná symetrie.

Označme A_j součet cyklického bloku x_j,…,x_(j+m−1), B_j součet
protilehlého bloku délky m. Je-li x0=0, má s_j součet A_j+m−B_j
a práh m+1. Tedy s_j=[A_j>B_j]. Vnější vstup ¬x0 je 1,
takže celý výsledek je [Σ_(j=1)^(2m) s_j≥m].

Pro T=x1+…+x_(2m) liché je A_j+B_j=T, proto A_j≠B_j. Protilehlý
index j+m je obrátí, tedy s_j+s_(j+m)=1. Celkem máme přesně m
jedniček mezi s_j a vnější výsledek je 1, stejně jako parita T.

## Sudý případ: proč rovná dvojice skutečně existuje

Při T sudém položme D_j=A_j−B_j. Každé D_j je sudé celé číslo,
D_(j+m)=−D_j a přechodem na další cyklický blok se mění o

    D_(j+1)−D_j=2(x_(j+m)−x_j) ∈ {−2,0,2}.

Je-li D_1=0, máme požadovanou rovnost. Jinak po m krocích dojdeme
od nenulového sudého D_1 k opačnému −D_1. Posloupnost sudých
čísel se skoky nejvýše 2 musí cestou dosáhnout nuly. Jeden takový
index lze zvolit mezi 1 a m. Příslušná dvojice s_j,s_(j+m) má
hodnoty 0,0; každá jiná dvojice má součet nejvýše 1. Proto
Σs_j≤m−1 a vnější výsledek je 0, stejně jako parita T.

Tím je doplněn vytištěný, jen naznačený krok o existenci nulového
rozdílu a dokázána (92) pro všechna m>0 i všechny vstupy. Důkaz
zahrnuje T=0, T=2m i m=1. Vyloučené m=0 se nepřidává: tehdy by
vnější singleton byl ¬x0, což vysvětluje význam daného předpokladu.

## (93), (94), symetrie a náklady

Pro m=1 jsou vnitřní mediány přesně
<x0,x1,¬x2>, <x0,x2,¬x1>; připojení ¬x0 dává (93).
Pro m=2 jsou čtyři vnitřní mediány

    <x0,x1,x2,¬x3,¬x4>, <x0,x2,x3,¬x4,¬x1>,
    <x0,x3,x4,¬x1,¬x2>, <x0,x4,x1,¬x2,¬x3>.

To je přesně pořadí a všechny negace v (94). Plná symetrie pravých
stran nyní plyne z dokázané rovnosti s paritou všech 2m+1 vstupů;
nebyla použita jako předpoklad důkazu. Obecný zápis má 2m+1
prahových operací v hloubce dvě, každou s 2m+1 vstupy. Tento počet
se týká modelu prahových bran s uvedenou aritou a neslibuje minimum.

## Errata, bibliografie a pokrytí

Prohledány all4a-pre, all4a, err4a, all4f0, err4f0 podle stran,
čísel úloh, vzorců a jmen; pro tento blok žádná relevantní změna.
Známá oprava parity na p556 se týká předchozí 112 a již je v proof-097.

Minnickův primární DOI byl nedostupný už při proof-087; tuto
bibliografickou výjimku přebíráme bez opakování pokusu. Primární
Fischler–Tannenbaum DOI 10.1109/TC.1968.229102 nebylo možné otevřít.
Kautzův přesný odkaz na p378 se nepodařilo rychle ověřit primárním
zdrojem. U těchto tří citací i Sasakiho/Huffmanovy atribuce se proto
historické údaje výslovně neuzavírají. Všechny zde použité matematické
výsledky mají vlastní úplné důkazy, takže na dostupnosti citací nezávisí.

Celá p77/file94 má nyní úplný obsahový rozpis: horní Theorem T je
proof-084, všechny definice, příklady, (90), (91), obecné dvouúrovňové
tvrzení a (92) jsou výše. Bibliografické hodnocení Murogovy monografie
a historické atribuce zůstávají samostatnými skipy. Stránka může
přejít na review_depth argument.

P78/file95 má zde doložené pouze pokračování parity, (93),(94).
Následující canalizing a kvantitativní část jsou dalším kurzem.
P94/file111 i p556/file573 stále obsahují nedokončenou 116 a zůstávají
partial. Další úloha je celá 116 včetně obecných asymptotických mezí.
