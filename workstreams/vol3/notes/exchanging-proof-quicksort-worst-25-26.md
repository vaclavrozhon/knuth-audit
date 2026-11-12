# Quicksort: celé úlohy 25–26 a obecná nejhorší cena

2026-11-07. Originál dolní 121, zadání 136 a odpovědi 632. Sazba
121/632 zobrazena; algoritmus a jeho cena převzaty z P1034–1054.
N>M≥1, různé klíče; jde o počet operací ve strojovém rozsahu, kde
je Program Q definován (samostatná nejasnost C0031 se tím nemění).
Žádný výpočet ani enumerace.

## P1076 — celý seřazený vstup, úloha 25

Při vstupu 1,2,...,N je pivot každé aktivní části její minimum.
Q3 se zastaví po jednom posunu, Q4 dojde na l, pivotová výměna je
samovýměna a zbude pouze pravá část o jeden kratší. Žádná skutečná
Q6 ani push nenastane. Po délkách N,N−1,...,M+1 zbude seřazená
část délky M a celé pole už je seřazené. Proto přesně

    A=N−M, B=0, S=0, D=0, E=0,
    C=sum_(k=M+1..N)(k+1)=binom(N+2,2)−binom(M+2,2).

To jsou všechny veličiny odpovědi 25. Dosazení do (16) dává
24(N−M)+4C+7N. Pro pevné M je to 2N²+O_M(N), tedy kvadratický
kontrast proti průměrnému N ln N z hlavního textu. Při M=N−1 se
provádí jediná partition a tento konkrétní seřazený vstup stojí jen
lineárně; tvrzení o kvadratickém chování zde drží práh pevný.

## P1077 — oba úplné svědky úlohy 26, současná dosažitelnost statistik

První svědek je

    1,2,...,N−M, N,N−1,...,N−M+1.

Prvních N−M pivotů jsou postupná minima. Všechny jejich výměny jsou
samovýměny, a proto po stejných délkách partition jako v P1076 zůstane
právě posledních M prvků v opačném pořadí. Závěrečná insertion u této
části vyvolá posun u každého kromě prvního prvku, a odstraní všechny
binom(M,2) inverze. Předchozí klíče jsou menší, takže přes hranici se
nic nepřesune. Dostáváme A,B,C,S jako v úloze 25 a navíc
D=M−1,E=binom(M,2).

Druhý svědek je

    N, M−1,M−2,...,1, M,M+1,...,N−1.

Pivot je nejprve maximum N; Q3 dojde na horní zarážku a Q4 se zastaví
ihned na r. Výměna prvního a posledního prvku přivede na začátek N−1.
Indukčně se odstraňují maxima N,N−1,...,M+1, zatímco sestupný úsek
M−1,...,1 zůstává na svých pozicích. Poslední výměna vloží na začátek
M, takže konečná část je M,M−1,...,1. Q6/push opět nejsou potřeba a
všechny statistiky jsou stejné jako u prvního svědka.

Zhoršení proti 25 je přesně 3(M−1)+4M(M−1)=(M−1)(4M+3).
Pro M=1 je nula, takže zde nelze žádat ostře pomalejší vstup; správné
maximální statistiky v odpovědi přesto platí. Pro M≥2 jsou oba svědci
skutečně pomalejší. Ještě zbývá dokázat, že žádný jiný vstup není horší.

## P1078 — přesná rekurzivní horní mez včetně celých nákladů

Odečtěme z (16) společný člen 7N a rozložme zbývající cenu po stromě.
List délky k≤M má jen insertion příspěvek 3D+8E. Ten je nejvýše

    L(0)=0,   L(k)=3(k−1)+4k(k−1)=4k²−k−3 pro k≥1,

protože se může posouvat nejvýše k−1 vkládaných prvků a každý pár je
nejvýše jedna inverze. Sestupný list obou mezí dosahuje současně.
Vnitřní uzel délky n s dětmi a,b, a+b=n−1, přispívá přesně
24+4(n+1)+11t+9[oba děti >M]. Z P1057/1046 plyne 0≤t≤min(a,b).
Pro horní mez lze proto použít 11min(a,b), aniž bychom předpokládali
současnou dosažitelnost všech dílčích maxim.

Definujme pro n≥M

    W(n)=sum_(k=M+1..n)(4k+28)+L(M)
        =2n²+30n+2M²−31M−3,

a pro n<M položme W(n)=L(n). Na n=M se oba předpisy shodují.
P1077 dosahuje W(N), takže stačí indukcí doložit, že pro každé
a,b≥0, a+b=n−1 a n>M,

    W(n) ≥ 4n+28+11min(a,b)+9[a>M,b>M]+W(a)+W(b).   (*)

Symetricky volme a≤b. Následující tři části pokrývají všechny možnosti.

## P1079 — jeden nebo oba dlouzí potomci v (*)

Pro a=0 musí být b=n−1≥M, a (*) je rovnost z definice W.
Je-li 1≤a≤M≤b, po odečtení pravé strany od levé zbude přesně

    a(4n+16−6a)+3.

Z n=a+b+1≥2a+1 je to nejméně a(2a+20)+3>0. Tento případ zahrnuje
i b=M; nemusíme u něj předpokládat skutečnou partition dítěte.

Jsou-li oba potomci dlouzí, a,b≥M+1≥2, zbude přesně

    a(4b−11)−2M²+31M−6.

Protože b≥a, je a(4b−11)≥4a²−11a. Poslední kvadratická funkce
je pro celá a≥2 rostoucí (její přírůstek je 8a−7>0). Celý rozdíl
je proto alespoň

    (M+1)(4M−7)−2M²+31M−6 = 2M²+28M−13 ≥17.

Tím je zahrnut i příspěvek 9 za push; nejde jen o maximalizaci počtu
porovnání za současného ignorování jiných instrukcí.

## P1080 — oba krátcí potomci a malé krajní hodnoty

Zbývá 1≤a≤b≤M, n=a+b+1>M. Položme delta=M−b. Z n>M plyne
0≤delta≤a. Rozdíl v (*) je přesně

    4b(a+delta)+2delta²−2a²+20a−31delta+3
      ≥ 2(a+delta)²+20a−31delta+3.

Nahradili jsme pouze b jeho dolní mezí a. S u=a−delta∈[0,a] se
poslední výraz rovná

    (a−1)(8a−3)+(31−8a)u+2u².

Pro a≤3 jsou všechny členy nezáporné. Pro a≥4 je 31−8a<0 a u≤a,
takže součet prvních dvou členů je alespoň
(a−1)(8a−3)+(31−8a)a=20a+3>0. Nerovnost tedy platí bez výjimky.
V nejmenší hraniční konfiguraci a=b=1,M=2 může nastat rovnost:
jediná Q6 u prostředního pivotu může nahradit nejhorší dvouprvkový
insertion list. Proto není správné tvrdit, že extrémní řetězec je
jediný nejhorší vstup; odpověď takovou jedinečnost ani nepožaduje.

## P1081 — závěr obecného maxima a jeho přesný rozsah

Listové báze a všechny případy (*) dokazují indukcí globální horní
mez W(N). Oba explicitní svědci P1077 jí dosáhnou. Přesná nejhorší
cena Programu Q pro různé klíče v jeho definovaném rozsahu je tedy

    7N+W(N)
      =24(N−M)+4[binom(N+2,2)−binom(M+2,2)]
         +3(M−1)+8binom(M,2)+7N.

Tím je prokázáno celé „you can't do worse“ v odpovědi 26, nikoli
pouze nalezen pomalý příklad. Cena zahrnuje Q9 i při M=1; varianta
s vynechaným Q9 se porovnává po odečtení stejného konstantního
příspěvku 7(N−1)+1 na všech vstupech, takže svědci zůstávají nejhorší.
Náklad abstraktního algoritmu s jinými instrukčními vahami ani možnost
shodných klíčů zde netvrdíme. Tyto předpoklady odpovídají analýze (16).

Pět vrstev `sources/exchanging-errata-review.json` nemá matematickou
změnu 25–26; sousední změna odkazu v 23 a bibliografie v 22 byly již
zohledněny. Nový nález nevznikl. Následuje úloha 27, kde svědek a
počet 546u ještě samy o sobě neprokazují globální minimum.
