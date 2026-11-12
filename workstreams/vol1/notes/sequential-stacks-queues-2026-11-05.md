# Souvislý průchod §2.2 a §2.2.1 — 5. listopadu 2026

Přečteny celé originály 238–243 a odpovědi536–540 (na540 pouze
odpověď14). Revidovány úplné důkazy v `stack-permutations.md`,
`queue-and-asymptotics.md`, `deques.md`, `deque-basis.md`,
`parallel/linear-lists/notes/deque-sufficiency.md`, úplný důkaz
opraveného rozpoznávače v `parallel/deque-followup/notes/`, jeho
pramenné meze a uložené výsledky. Žádný úspěšný běh nebyl opakován.
Nový výpis všech čtyř errat je ve `sources/sequential-2026-11-05/`.

## Hlavní text a jednoduché úlohy

Definice konečného seznamu správně zahrnuje n=0. FIFO/LIFO a obě
omezení deque souhlasí s železničními šipkami i Fig.3. Horní
uzavřená větev omezuje vstupy, dolní výstupy. top(A) a odběr jsou
definovány jen pro neprázdnou strukturu. Terminologie pamětí
vysvětluje odlišné funkce, netvrdí vzájemně disjunktní technické
kategorie. Srovnání cen operací je kvalitativní, nikoli neprokázaná
exaktní dolní mez.

1: výstupně omezená deque je zásobník při vkládání na výstupním
konci a fronta při vkládání na opačném. 2: SSSXXSSXSXXX dává325641;
154623 blokuje trojice5,2,3. Základní příklad SSXSSXXX dává2431.
6: obyčejná fronta zachová jediný výstup1,…,n. Včetně n=0.

## Zásobníkové permutace a ballotové počty

3: legálnost je nezáporná výška každého prefixu. První rozdíl S/X
dvou legálních historií mění pořadí nově vloženého prvku a starého
vrcholu, a tedy výstup. 4: odraz prefixu do první výšky−1 dává
C_n=binom(2n,n)−binom(2n,n−1)=binom(2n,n)/(n+1).
Obecný ballotový vzorec pro l,m≥0 a kladné h je
f(l,m,h)=binom(l+m,min(m,l−h)); pro l≥m+h dosáhne h každá cesta,
jinak odraz při prvním dosažení h dává l−h kroků prvního druhu.
Nulové dolní indexy mimo přípustný rozsah se berou jako nulové
koeficienty. Symetrie platí v uvedené nezáporné oblasti argumentů.

Opravená rekurence g(L+1,h)=[h>0]g(L,h−1)+g(L,h+1) a počáteční
g(0,h)=[h=0] určují všechny koeficienty. Malý kořen r(z) má
kladný řád, takže dosazení do formální řady je oprávněné a dává
G=r/(z(1−rx)). Odtud mocnina f(z²)^(h+1), ne f(z²)^h: známá
chyba X0009 selže už na x⁰z². Sudé i liché explicitní koeficienty
na537 souhlasí s rozdílem dvou binomických koeficientů. Triangulace
vyžadují konvexitu; nekonvexní čtyřúhelník má jedinou triangulaci.
To je známé X0020, nikoli nová vada.

5: vzor312 je nemožný, protože prostřední požadovaný malý prvek
zůstane pod větším pozdějším výstupem. Selže-li hladové vytváření
permutace, zakrývající větší prvek byl vložen kvůli ještě většímu
dřívějšímu výstupu, což přesně vyrobí312. Obě implikace jsou obecné.
Konečných46234permutací a902koeficientů je přijatý doplňkový test,
nikoli náhrada těchto důkazů.

## Omezené deque a asymptotika

7–8: výlučné čtyřprvkové příklady4132,4213 a společně nedosažitelná
4231 souhlasí. Pro neomezenou deque jsou při n=5 právě čtyři
výjimky51324,51342,52314,52341. 9: časové obrácení historie a
přeznačení dávají involuci p↦R p⁻¹ R, R(i)=n+1−i, mezi oběma
omezenými typy.

10: kanonizace mění S na Q při prázdné deque a XQ na QX; zachová
výstup a lexikograficky sníží počet S a počet dvojic X před Q.
Pro první rozdíl Q/X musí větev s X nakonec vložit další prvek
pomocí S při stále neprázdné frontě; proto se změní jeho pořadí
vůči starému obsahu. Ostatní první rozdíly se rozhodnou okamžitě.
Existence i jednoznačnost kanonické historie jsou tedy dokázány.

11: jednoznačný rozklad při prvních sestupech výšky dává gramatiku
F=1/(1−zB), B=1+zB²/(1−zB), odtud
F=(3−z−sqrt(1−6z+z²))/2 s F(0)=1. Stejný výsledek dává dvojitá
řada prefixů G,H po oddělení koncového X a stavu prázdné deque.
První koeficienty1,1,2,6,22,90 a lineární rekurence
nb_n=3(2n−3)b_(n−1)−(n−3)b_(n−2) pro n≥2 souhlasí.

12: Stirlingův vzorec dává a_n=4^n/(sqrt(pi)n^(3/2))(1+O(1/n)).
Pro b_n rozklad diskriminantu s λ=3+2sqrt(2), ρ=1/λ a α=ρ² dává
konstantu (sqrt(2)−1)/(2^(3/4)sqrt(pi)). Obecná konvoluce
koeficientů sqrt(1−w)sqrt(1−αw) pro pevné |α|<1 má hlavní člen
−sqrt(1−α)/(2sqrt(pi)n^(3/2)); horní polovina součtu exponenciálně
klesá a dolní dovoluje rovnoměrný konečný rozvoj. Úplná asymptotická
řada vyplývá z konečného Taylorova polynomu analytického faktoru,
bez neplatné záměny dvou nekonečných řad. Známé X0017 správně
opravuje znaménko 1/Gamma(−k−1/2): pro k=1,n=2 má být+3/8.
Posuny zobecněných Stirlingových čísel v opravených c_j souhlasí
s dříve prověřenou §1.2.11.1. Hlavní tištěná asymptotika je správná.

## Obecná deque a dva zásobníky

13: znovu revidován obecný důkaz obou směrů Prattovy báze. Vytváření
z identity dává údolní deque; redukce odkládá zbytečné vstupy.
Nejdelší úspěšný prefix a největší možný soused blokovaného prvku
určují pevné jádro bAa. Kdyby bylo jádro někdy samo, zrcadlení
dalších operací prodlouží prefix nebo zlepší souseda, spor.
Zpětný střídavý řetěz c_i striktně klesá, má průchody d_i mezi
sousedními hodnotami a musí skončit pod max(a,b). Obě parity
vytvoří přesně rodiny4k+1 a4k+3 a čtyři varianty výměn z knihy.
Nutnost zákazu plyne z vynucených střídavých vkladů; vymazání
ostatních operací zachovává dosažitelnost podvzoru.

Opravený lineární rozpoznávač používá opačnou konvenci, třídění
daného vstupu do identity; pro knižní výstup se tedy použije
inverzní permutace. Jeho bloky reprezentují přesnou množinu horských
front bez pasti. Kanonizace spodního monotónního bloku zachová
tuto množinu; normalizace odstraňuje právě pasti. U jednoprvkového
centra mohou dvě orientace označovat tutéž frontu, a proto se
správnost dokazuje množinami, ne počtem orientací. Každý pokračující
krok spojí bloky nebo vypíše prvek; v rámci n vstupů je nejvýše n
odstranění/spojení bloků. Spojové seznamy s posledním uzlem dávají
konstantní spojení, tedy celkově O(n) času i paměti ve slovním modelu.

Publikovaný protipříklad254163 a oprava z2012 jsou externí známá
věc, nikoli náš nový nález TAOCP. Odpovídající knižní permutace je
416325. Dentonův opomenutý kardinalitní mezikrok pro vstup231
nevyvrací opravený algoritmus; přijatý množinový důkaz jej nepotřebuje.
Rosenstiehl–Tarjanův přesný originál389–390 se nadále nevydává za
přečtený. Také novější enumerativní články nejsou tímto kompletně
auditovány a současný stav výzkumu nepřepisuje historické zadání.

14: abstraktní fronta je R od vrcholu ke dnu a S ode dna k vrcholu.
Při prázdném R se celý S obrátí do R; každý prvek se nejvýše dvakrát
vloží a dvakrát vyjme. Mez4i po i vkladech je amortizovaná, nikoli
konstantní nejhorší čas jediného odběru. Volitelný přímý vklad do R
vyžaduje oba zásobníky prázdné. Erratum2021 vyjasňuje instrukce;
netvrdíme protipříklad proti každému přirozenému výkladu původního
stručného textu.

## Pramenné výjimky a uzavření

Primární články Aebly/Mirimanoff/André, de Moivre1711 a jeho vlastní
zpráva1756 o roku1708, Segner/Euler a Prattova gramatika již mají
přesné přijaté čtecí doklady. Historická inference, že de Moivre
obecný vzorec uměl dokázat, se odlišuje od dochovaného úplného důkazu.
Hood–Melville1980 přímo podporuje metodu dvou seznamů a amortizaci;
osobní připsání řešení Melvilleovi není tvrzením výlučného prvenství.
Soukromé předání Knuthovi nezávisle doloženo není.

Výslovně se bibliograficky přeskakují plné Barton–Mallows1965,
Ramanan1984, původní strany Rosenstiehl–Tarjan1984 a případný
soukromý záznam předání Melville1980. Tyto výjimky neskrývají
nedokázanou místní matematiku: všechny původní úlohy1–14 jsou
uzavřené včetně oprav, obou charakterizací a algoritmické složitosti.
Úlohy4,5,13,14 se proto mění partial→checked s výslovným zdrojovým
omezením podle pokynu uživatele z5.11.2026.

Hlavní §2.2.1 nadále zůstává partial kvůli konkrétním historickým
údajům na240: původ železniční analogie, některá synonyma a jejich
dobové rozšíření. KDF9, Huskey a Daly dokládají jen uvedené části.
Samostatná §2.2 obsahuje na238 pouze nadpis, její průchod je uzavřen.

Přesné červené lokace známých matematických oprav: X0009/X0010 na537,
X0011 na538, X0017 na539, X0020 na536. X0018 je na540 související
vyjasnění, nikoli zde nový důkaz vady. X0963 doplňuje dříve pouze
poznámkou zaznamenané názvoslovné a historické opravy; červeně242
(cards/cars) a536 (atribuce odrazu). Formát Fig.3(a), římské číslice
a doplnění slova bottom samy nejsou obsahovým selháním.

Strany238–239 a241–243 mají celé pokrytí;240 částečné. Odpovědi
536–539 celé, na536 společně s předchozím koncem §2.1. Strana540
zůstává částečná kvůli následujícím odpovědím §2.2.2. Nová neznámá
vada:0. Další hlavní text je §2.2.2 na244.
