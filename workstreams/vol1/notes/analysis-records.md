# §1.2.10: maximum a rozdělení rekordů

Podklad: zobrazené s. 96–107 a odpovědi 500–502 třetího vydání,
prvního dotisku. Důkazy zde kontrolují hlavní algoritmus, vzorce (1)–(9),
(14), (16), poznámku o momentech a úlohy 1, 3, 7–10, 18–20.
Známé změny se vyhodnocují ve všech historických vrstvách errat.

## Algoritmus a přesná distribuce

Nechť X[1],…,X[n] je neprázdný vstup. Algoritmus M prochází pole zprava
doleva; m je dosavadní maximum, j jeho index, k další index ke zpracování.
Na vstupu do M2 platí invariant
`m=max_{k<i≤n} X[i]`, přičemž j je nejpravější index dosahující tohoto maxima.
Inicializace m=X[n], j=n, k=n−1 jej splňuje. Je-li X[k]≤m, nic se nemění;
jinak M4 nastaví m=X[k], j=k. Po snížení k je invariant obnoven.
Klesající nezáporné k dokazuje ukončení; pro k=0 invariant dává výsledek.
Shodné hodnoty jsou důvodem neostré nerovnosti v M3 a nejpravějšího j.
Podmínka n>0 byla výslovně doplněna v roce 2024.

Označme A počet průchodů M4. Kroky M1,…,M5 se provedou v počtech
`1, n, n−1, A, n−1`. Vývojový diagram na s. 97 souhlasí s těmito počty
i s větvením M3. Pomocná paměť je konstantní počet slov; tvrzení zde
nevykládáme jako konstantní počet bitů pro libovolně velká n.

Rekord zprava je prvek přísně větší než všechny prvky napravo od něj;
poslední prvek je rekord automaticky. Proto A+1 je počet těchto rekordů.
U rovnoměrné permutace n různých hodnot označme P_{n,k} počet vstupů s A=k
a p_{n,k}=P_{n,k}/n! jejich pravděpodobnost. Vložíme nejmenší prvek do
permutace délky n−1. V poslední pozici přidá jeden rekord, v ostatních
n−1 pozicích nic nemění. Tedy

`P_{n,k}=P_{n−1,k−1}+(n−1)P_{n−1,k}` pro n≥2,

s P_{1,0}=1 a nulou mimo povolené indexy. Chyba indexu v tištěné rekurenci
byla opravena 12. září 1997; rekurenci nekontrolujeme v chybném původním tvaru.
Pro n=3 dává šest pořadí počty A = 0,1,0,1,1,2 a průměr 5/6.

Pravděpodobnostní vytvořující funkce, tj. polynom s koeficienty p_{n,k}, je

`G_n(z)=∏_{j=2}^n (z+j−1)/j = (z+1)…(z+n−1)/n!`.

Racionálně zapsaný výraz pomocí zobecněného binomického koeficientu
na s. 99 znamená právě tento polynom i v odstranitelných singularitách.
Počet c(n,r) permutací s r cykly splňuje stejnou rekurenci jako P_{n,r−1}
(vložíme nový prvek do existujícího cyklu nebo vytvoříme nový cyklus).
Proto `p_{n,k}=c(n,k+1)/n!`. Z G_n(0)=1/n plyne odpověď 1:
poslední prvek musí být největší.

Každý faktor G_n je PGF Bernoulliho veličiny s pravděpodobností 1/j;
A má tedy rozdělení součtu nezávislých takových veličin, j=2,…,n.
Definujme harmonické součty `H_n^(r)=∑_{j=1}^n j^(−r)`, H_n=H_n^(1).
Střední hodnota a rozptyl jsou
`μ_n=H_n−1`, `σ_n²=H_n−H_n^(2)`.
Pro n=12 je μ_n=58301/27720; rozptyl se zaokrouhlí na 1.54.
Obrázek 10 odpovídá koeficientům G_12; přesná data a kontrola zaokrouhlení
jsou v `results/analysis-records.json`. Pro n=1000 dostaneme rozsah
0,…,999, průměr 6.49 a směrodatnou odchylku 2.42 (úloha 3).

## Vyšší momenty poznámky na s. 100

Položme R_n=A+1, S(r,k) počet rozkladů r-prvkové množiny do k neprázdných
bloků a L(z)=ln(1/(1−z)). Identita pro cykly dává
`∑_{n≥0} E(u^{R_n}) z^n=(1−z)^(−u)` s R_0=0.
Derivace k-krát podle u v bodě 1 poskytne
`∑_{n≥0} E(R_n(R_n−1)…(R_n−k+1)) z^n=L(z)^k/(1−z)`.
Rozvinutím mocniny x^r do klesajících faktoriálů dostaneme přesně
`E(R_n^r)=[z^n](1−z)^(−1) ∑_{k=0}^r S(r,k)L(z)^k`.
Jde o identitu formálních řad, takže není potřeba analyticky zaměňovat limity.

Pro každé pevné celé r≥1 je navíc `E(R_n^r)~(ln n)^r`.
V nezávislém Bernoulliho modelu zahrneme i B_1=1 a ∑E B_j=H_n.
Rozvoj H_n^k do uspořádaných k-tic se od k-tého faktoriálového momentu
liší jen členy s opakovanými indexy. Jejich součet je pro k≥2 nejvýše
`C(k,2) (∑j^(−2)) H_n^(k−2)`, protože vybereme jednu rovnou dvojici;
všechny členy jsou nezáporné. Faktoriálový moment je tedy
H_n^k+O(H_n^(k−2)); k=0,1 řešíme přímo. Převod na obyčejný moment
dává vedoucí člen H_n^r, ostatní jsou O(H_n^(r−1)). Pro r=0 je tvrzení 1=1.
Tím je matematický obsah poznámky ověřen bez opření o historickou citaci.

## Úlohy 7–10: opakované hodnoty

Při podmínce přesně m různých hodnot nejprve fixujme rozklad pozic
do m neprázdných tříd stejných hodnot. Hodnoty lze třídám přiřadit m!
rovnoměrnými způsoby. Z každé třídy může být rekordem pouze její
nejpravější prvek; jejich relativní pořadí hodnot je rovnoměrná permutace m.
Podmíněné rozdělení A je tedy p_{m,k} nezávisle na zvoleném rozkladu.
Pevné násobnosti jednotlivých uspořádaných hodnot tuto symetrii nemají;
právě na to upozorňuje odpověď 7 svými příklady pro n=5 a n=3.

Nyní vybíráme n hodnot nezávisle rovnoměrně z M uspořádaných možností.
Pravděpodobnost, že všechny jsou různé, je
`M(M−1)…(M−n+1)/M^n` (n≤M), jinak nula.
Přebytečný faktor (M−n)! v prvním dotisku odpovědi 8 byl odstraněn 1999.
Pravděpodobnost právě m různých hodnot je
`q_{n,m}=M(M−1)…(M−m+1) S(n,m)/M^n`:
zvolíme rozklad pozic a injektivní přiřazení hodnot blokům. Stejný výsledek
dává rekurence `q_{n,m}=[(M−m+1)q_{n−1,m−1}+m q_{n−1,m}]/M`.
Kombinace s úlohou 7 dává odpověď 10:

`Pr(A=k)=M^(−n) ∑_{m=1}^{min(M,n)} C(M,m) S(n,m)c(m,k+1)`.

Pro očekávaný počet rekordů sečteme pravděpodobnosti rekordů jednotlivých
pozic. Má-li daná pozice včetně sebe j prvků do konce, její pravděpodobnost
rekordu je `(1/M)∑_{v=1}^M ((v−1)/M)^(j−1)`. Součet geometrických řad dává

`E(A)+1=H_M−∑_{m=1}^M (1−m/M)^n/m`.

Pro Bernoulliho čísla B_k v nynější knižní konvenci B_1=+1/2 je ekvivalentně

`E(A)+1=H_n+∑_{k=1}^n (C(n,k)−1)B_k/(k M^k)−(n−1)/M`.

Poslední člen přidávají errata 2023 po změně konvence B_1. Ověření identity:
pro n=1 dávají oba výrazy 1. Rozdíl pravých stran pro n a n−1 je
`(1/n)∑_{k=0}^{n−1} C(n,k)B_k/M^k−1/M`.
Vzorec pro součet (n−1)-ních mocnin z předchozího oddílu jej ztotožní s
`M^(−n)∑_{v=0}^{M−1}v^(n−1)`, což je právě nový příspěvek rekordu.
Indukce n≥2 dokazuje opravenou konečnou identitu pro všechna M≥1.

## Úloha 18: pevné násobnosti

Nechť k_r≥0 je počet hodnot rovných r a `K_r=∑_{i=r}^n k_i`; K_1=n>0.
Vkládáme postupně hodnoty od největších k nejmenším. Mezi již umístěné
K_{r+1} větší hodnoty se k_r stejných hodnot vloží rovnoměrně jedním
z C(K_r,k_r) způsobů. Tyto volby v různých krocích lze provést nezávisle;
jejich součin je n!/∏k_r!, takže výsledná slova s danými násobnostmi
jsou přesně rovnoměrná. Počet rekordů vzroste právě když poslední pozici
obsadí nová hodnota r, s pravděpodobností k_r/K_r.

Proto opravená PGF počtu A je

`z^(−1) ∏_{r=n,…,1; K_r>0} (k_r z+K_{r+1})/K_r`.

Faktor pro největší přítomnou hodnotu je z a ruší z^(−1), takže jde
o polynom i v z=0. Pro K_r=0 se faktor vynechá, což odpovídá knižní
konvenci 0/0=1. Původní vzorec předpokládal k_n>0; oprava z 15. října
2007 doplňuje chybějící krajní faktor i dělení z. Například všechna X[i]=1
dávají G=1, jak mají. Přesná enumerace zahrnuje i nulové krajní násobnosti.

## Úlohy 19–20: rekordy při inverzi a odečítání

Je-li a permutace a b její inverze, a_k=l znamená b_l=k.
Podmínka a_j<l pro všechna j<k je ekvivalentní tomu, že všechny hodnoty
větší než l jsou až za k, tedy b_j>k pro všechna j>l. To je právě
rekordní minimum zprava v pozici l inverzní permutace. Indexy i směr
nerovností v odpovědi 19 souhlasí.

V úloze 20 nechť b_1≤…≤b_n. Pokud a_k není přísné rekordní maximum
zleva, existuje j<k s a_j≥a_k, a tedy a_j−b_j≥a_k−b_k.
Opakujeme přechod k menšímu indexu, dokud nedojdeme k rekordu.
Maximum všech a_i−b_i je proto dosaženo mezi rekordy zleva. Obrácením
pořadí a znamének dostaneme analogii pro maximum b_i−a_i mezi rekordními
minimy zprava. Maximum těchto dvou maxim je max_i |a_i−b_i|.
Důkaz pracuje i s rovnostmi a opakovanými a_i; původní sken má ≥,
zatímco OCR tento znak místy ztrácí.

U náhodné permutace očekáváme H_n rekordů každého druhu. Počet pozic,
na nichž je třeba odečítat, je nejvýše jejich součet, tedy v průměru
nejvýše 2H_n~2 ln n; případný překryv počty jen zmenší.
To je smysl asymptotické poznámky, nikoli rovnost pro každé n nebo vstup.
