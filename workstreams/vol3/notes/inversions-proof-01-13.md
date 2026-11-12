# Inverze: úlohy1–13

S.17–19, odpovědi591–593. Hotové úlohy3 a10 se přebírají z
inversions-proof-main.md. Obecný důkaz úlohy5 byl uzavřen pod V3-P0031;
níže jsou pouze nové podrobnosti a vytištěný příklad. Žádné nové testy,
enumerace ani nález. Zdrojové erratum pro význam Josephusova příkladu
a pro index proměnné v odpovědi13 je již ve sources/inversions-errata-review.json.

1. Pro271845936 počty větších předchůdců podle hodnoty jsou
2,0,5,2,2,3,0,0,0, jak uvádí odpověď. Rekonstrukce z50121200 má
postupné stavy8;78;786;7586;75486;735486;2735486;27354186.
Každé vložení má předepsaný počet větších předchůdců.

2. Použito známé vyjasnění23.5.1998: a_i je pořadí úmrtí muže i,
nikoli číslo muže zemřelého jako i-tý. b_j je tak index místa j-tého
vyřazení v dosud žijících mužích seřazených podle původního čísla,
počítaný od0. První je(m−1) mod n. Po odstranění místa b_j začíná
počítání na jeho nástupci, jehož nový index je b_j modulo n−j;
další vyřazený má proto b_(j+1)=(b_j+m−1) mod(n−j).
Pro n=8,m=4 vyjdou b=36310010. Skutečná čísla postupně vyřazených
mužů jsou4,8,5,2,1,3,7,6; jejich pořadí úmrtí je54613872, v souladu
s textem i známým erratem. Řešení se nehodnotí pod nesprávnou opačnou
interpretací slova „order“.

4. Invariant C2: propojený seznam s hlavou x₀ obsahuje právě hodnoty
n,…,k+1 ve správném relativním pořadí. b_k≤n−k zaručuje, že se
průchod b_k odkazy nezastaví předčasně. Dvojice přiřazení x_k←x_j,
x_j←k vloží k právě za b_k větších hodnot. Seznam zůstane bez cyklů
a končí0. C4 vydá po jednom každý prvek. Sdílení x_k s b_k je bezpečné:
hodnota b_k je před zápisem již spotřebována a ostatní měněné odkazy
patří dříve vloženým hodnotám>k. Počet kroků je Θ(n+Σb_k), takže
očekávaný čas je Θ(n²) podle již doloženého EΣb_k=n(n−1)/4.

5. Asociativitu, korektnost a O(n log n) čas slučovací operace ∘
přebíráme z V3-P0031. Ručně ověřené mezistavy vytištěného příkladu:

- První průchod: [2,1][1,2]; [4,4][1,3]; [0,5][2,6]; [1,8][0,7]; [0,9].
- Druhý: [2,1][1,2][1,4][1,3]; [0,5][1,8][0,6][0,7]; [0,9].
- Třetí: [0,5][1,1][0,8][0,2][0,6][0,4][0,7][0,3]; [0,9].
- Čtvrtý: všechny mezery0, hodnoty591826473.

Každá řádka vznikla přímo dvěma větvemi operace, nikoli výčtem permutací.
Kombinace s O(n) Josephusovou rekurencí je O(n log n) místo obecného
O(mn) simulování, bez tvrzení zrychlení pro každé malé m.
Uvedená alternativa v RAM je také konkrétní: vyvážený strom počtů
volných míst vyhledá(b_i+1)-ní volné místo a vynuluje jej v O(log n).
Opakování pro i=1,…,n je bijektivní rekonstrukce a stojí O(n log n).

6. Pro každé k má x_s během průchodu počet předchozích prvků s
horním prefixem s=floor(a_j/2^(k+1)) a k-tým bitem1. Při bitu0
se tedy přičtou právě větší předchůdci, jejichž první odlišný bit je k.
Každá inverze má jediný nejvyšší odlišný bit, a započte se přesně jednou.
Počet bitových průchodů je floor(lg n)+1; inicializace má celkem
O(n) až O(n+log n) položek, průchody O(n log n). Sazba má správně
0≤s≤n/2^(k+1), takže se inicializuje i krajní prefix při přesné
dělitelnosti; nejde o domnělou chybu z OCR.

7. c_j počítá menší následníky, tedy0≤c_j≤j−1. Z c se rekonstruuje
vkládáním j do již postaveného pořadí1,…,j−1 tak, aby za ním bylo
právě c_j prvků. U daného devítiprvkového příkladu je c=000142157.
B_j má nejvýše j−1 levých prvků a C_j nejvýše n−j pravých prvků.
Pro rekonstrukci z B_k je pořadí nového prvku mezi dosavadním prefixem
r=k−B_k; zvýšení starých pořadí≥r a připojení r zachová přesně
relativní pořadí prefixu. Po posledním kroku je to původní permutace.
Pro C se symetricky postupuje zprava doleva s novým pořadím C_j+1.
Všechny přípustné tabulky tak dávají právě jednu permutaci.

## Úloha8: všechny uvedené identity

Polož p_j=a′_j. Z počtu menších předchůdců je
p_j−1=(j−1)−c_j+b_j, tedy p_j=j+b_j−c_j.
Po dosazení hodnoty a_j dostaneme a_j=j+C_j−B_j, obě identity(f).
Inverze(a_i,a_j) původní permutace odpovídá inverzi(j,i) inverzní
permutace. Převodem počítaných hodnot/pozic z toho dostaneme
b′=C, c′=B, B′=c, C′=b, včetně všech indexů.

(a) c_j=j−1 znamená, že j předchází všem menším i. Všichni větší
předchůdci j spolu s j pak předcházejí i, takže b_i>b_j. Pokud naopak
nějaké i<j předchází j, vyber největší takové i. Větší předchůdci i
jsou všichni>j a také předcházejí j, takže b_i≤b_j: podmínka selže.

(b) b_j=n−j znamená, že všichni větší i předcházejí j. Každému takovému
i následují j i všichni menší následníci j, tedy c_i>c_j. Pokud nějaké
i>j následuje j, vyber nejmenší takové i; jeho menší následníci jsou
všichni<j a patří i mezi následníky j, takže c_i≤c_j.

(c) j−c_j je1 plus počet menších prvků před j. Jestliže j předchází
všem větším i, tyto menší předchůdce i samotné j vidí i před sebou,
takže i−c_i>j−c_j, ekvivalentně c_i−i<c_j−j. Pokud nějaký větší
prvek předchází j, vyber nejmenší takový i; jeho menší předchůdci
jsou pouze<j, tedy i−c_i≤j−c_j. To dokazuje ekvivalenci s b_j=0.

(d) n−j−b_j je počet větších následníků j. Jestliže každý menší i
předchází j, jeho větší následníci zahrnují j i všechny větší
následníky j, tedy b_i+i<b_j+j. Pokud menší prvek následuje j,
vyber největší takový i; každý jeho větší následník je>j a také
následuje j, takže b_i+i≥b_j+j. To dokazuje ekvivalenci s c_j=0.

(e) Je-li p_i<p_(i+1), větší předchůdci i jsou podmnožinou větších
předchůdců i+1, a menší následníci i+1 jsou podmnožinou menších
následníků i. Proto b_i≤b_(i+1), c_i≥c_(i+1). V opačném pořadí
je navíc samotný i+1 započten v b_i a samotný i v c_(i+1), takže
platí opačné přísné nerovnosti. Všechny tři podmínky v(e) jsou tedy
ekvivalentní. Žádná z těchto identit nebyla odvozena pouze testováním.

9. Jelikož b′=C a b-tabulka určuje permutaci jednoznačně, b=C
je ekvivalentní b=b′, a tedy a=a′. Oba směry jsou tím dokázány.

## Úlohy11–13: množiny inverzí

11a. V E platí současně x>y>z a p_x<p_y<p_z, v jeho doplňku
p_x>p_y>p_z. V obou případech se příslušný vztah přenese na x,z.
11b. Z E a jeho doplňku vznikne turnaj určující zamýšlené pořadí
každé dvojice. Nejkratší orientovaný cyklus by měl délku3: každý
delší cyklus lze zkrátit orientovanou tětivou, nebo tím najít trojúhelník.
Pro tři hodnoty x>y>z však cyklus poruší tranzitivitu buď E, nebo
jeho doplňku. Turnaj je tedy acyklický a jeho topologické pořadí má
přesně předepsané inverze. Díky orientaci každé dvojice je jediné.

12. Nechť E je tranzitivní uzávěr E₁∪E₂. Předpokládejme a>b>c,
(a,b),(b,c) mimo E, ale(a,c)∈E. Existuje klesající řetězec od a
do c s hranami z E₁∪E₂. Nemůže obsahovat b. Některá jeho hrana
(u,v) proto překročí b, u>b>v. Patří některému E_i. Tranzitivita
doplňku E_i vynutí(u,b)∈E_i nebo(b,v)∈E_i. V prvním případě
prefix řetězce dává(a,b)∈E, v druhém suffix dává(b,c)∈E: spor.
Doplněk E je tedy tranzitivní a úloha11 zaručí příslušnou permutaci.
Uzávěr sjednocení je nejmenší přípustný nadmnožinový invariant;
duální operace je T\closure((T\E₁)∪(T\E₂)). Existují tedy obě
mřížkové operace. V knižní konvenci „above“=menší množina inverzí dává uzávěr
sjednocení nejvyšší společný dolní prvek a duální operace nejnižší
společný horní prvek, jak vyžaduje tvrzení o mřížce.

13. Pro1≤m≤n ponech všechny položky kromě b_(n−m+1) pevné.
Tato položka má právě možnosti0,…,m−1, takže každý zbytek celkového
součtu modulo m nastane právě jednou. Zbylých tabulek je n!/m.
To zároveň dokazuje rovnost počtu sudých/lichých permutací pro n≥2.
Použit správný index z errata2.6.2007; chybný starší index b_m není
nový nález.

Další aktivní úloha16 na20/file31; úlohy14 a15 již uzavřeny.
Výzkumná/rozšířená část20 bude případně oddělena jako partial.
