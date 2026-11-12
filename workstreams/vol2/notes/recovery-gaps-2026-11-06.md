# Obnova §3.5, úlohy 20–21 — V2-X0152

6. listopadu 2026, po restartu. Celé `gap-structure.md` bylo znovu
přečteno a jeho obecné argumenty porovnány s každou částí zadání
181/file193 a odpovědí 594–595/file606–607. Všechny tři původní
stránky byly znovu zobrazeny. Staré programy ani výčty se neopakovaly.
Vydání a stránkování ověřeno proti inventáři: edice 3, tisk 1, 1997-09,
běžný posun file = printed + 12.

## 20(a–d): co přebíráme a co opravujeme

**20(a).** `gap-structure.md`, §2(a), dokazuje přesné konečné profily
van der Corputovy posloupnosti. Při n=2^r jsou všechny mezery 1/n;
pro 2^r<n<2^(r+1) je maximum 2^(−r) a minimum 2^(−r−1).
V každém dyadickém bloku n·maximum roste k 2 a n·minimum začíná
arbitrárně blízko 1/2. Proto limsup a liminf jsou přesně 2 a 1/2,
nikoli jen jednostranné odhady. Tím je odůvodněna i závorka odpovědi
o půlení největší mezery.

**20(b).** Argument §2(b) je úplný: k−1 nových bodů nemůže rozdělit
všech k původně největších mezer; opakované body situaci nezhorší.
Vlastní starší důkaz správně používá `p_n≥1/S_n`. Srovnání s tiskem
odhalilo nový **C0249**: násobení harmonického asymptotického rozvoje
neomezeným p_n mění velikost chyby. Přesný protipříklad z různých bodů,
oprava a všechny erratové vrstvy jsou v
`C0249-gap-harmonic-remainder.md`. Závěrečný výrok o nekonečně mnoha m
i dolní mez 1/ln 2 jsou správné po uvedené opravě.

**20(c).** Převzat §2(c) včetně všech omezení na indexy a harmonické
váhy. Nový bod vytvoří nejvýše dvě konečné mezery. Čas vzniku mezery
je stav `1+max(m,m′)`, proto se používá opravený index
`a=max(m+1−n,m′+1−n,1)`. Krajní bod 1 se chápe jako kruhový obraz
U_0=0; vznik krajní mezery určuje její druhý konec. U opakovaných
bodů se nuly počítají pevným pořadím indexů. Pro každé a≥2 jsou
nejvýše dva výskyty; z 2n vah a jejich monotonicity pak vyplývá
`1≥2ρ_n(H_(2n)−H_n)`. Pro n=1 je to jen správný odhad ρ_1≤1.
Protože minimum se dosahuje v [n+1,2n], výsledné indexy jdou do
nekonečna a liminf je nejvýše 1/ln 4. Starý **C0065** přesně zachycuje
chybějící +1 v tištěném pomocném indexu; není novým nálezem.

**20(d).** Převzat §2(d), nikoli pouze konečné testy. Rozklad lichých
čísel podle mocnin 2 identifikuje kruhové mezery; přidání W_n dělí
štěpením štítek n na 2n a 2n+1. Tím vznikají přesně délky
`lg((j+1)/j)`, n≤j≤2n−1. Všechny W_n jsou různé, protože poměr dvou
různých kladných lichých čísel není mocninou 2. Logaritmické integrály
dávají pro x>0 `x/(1+x)<ln(1+x)<x`, a tedy obě ostré meze i pro n=1.
Příslušné limity dokazují současnou optimalitu obou konstant.
Původní citace de Bruijn–Erdős 1949 nebyla nově získána; matematika
je zde dokázána přímo a bibliografický obsah se nepovažuje za ověřený.

## 21(a–c): obecná majorizace, ne výčet

**21(a).** Převzat §3. Pro každý dyadický pás se spočítají lichá čísla
v `[2^h,2^(h+1/2))`; chyba zaokrouhlení je O(1) na pás, a tedy O(m)
do 2^m. Mezi `ceil(2^(m−1/2))` a `2^m` nepřibude bod pod 1/2,
takže oba uvedené prefixy mají přesně stejný počet. Po vydělení jejich
délkami vzniknou odlišné limity `2−sqrt(2)` a `sqrt(2)−1`. Stropy,
směr horní/dolní hustoty a celý zobrazený součet odpovědi souhlasí.

**21(b).** Převzaty §4–5. Odraz všech bodů kromě nuly zachovává
seřazené délky mezer, takže starý **C0064** nadále vyvrací jednoznačnost
bodové posloupnosti. Silnější kladná informace je také dokázána:
jednoznačný je každý seřazený profil L_n. Nejde jen o protipříklad.

Při revizi úplného srovnávacího lemmatu byly zvlášť ověřeny tyto kroky:

- Obě operace odstraňující nerozdělený kořen mění dvojici délek na
  vyrovnanější dvojici se stejným součtem. Nejhlubší větev má dvě
  listové děti, takže žádné pozdější dělení jejich změnu nenaruší.
  Počet nerozdělených kořenů klesne, a proces tedy skončí.
- Po cyklickém posunu za minimum prefixových součtů jsou všechny
  rozdíly součtů nezáporné. Při nahrazení rozdělené složky dvěma dětmi
  se větší dítě dává první; lichý mezikrok je alespoň průměr sousedních
  sudých. Následné sestupné seřazení součty jen zvětší.
- Při zpětném slučování je součet dvou nejmenších mezer přesně
  `lg(m/(m−1))`. Skutečně sloučená dvojice nemůže mít menší součet
  a předchozí největší mezera nemůže mít větší délku. Obě nerovnosti
  proto musí být rovnost. Odstranění posledních dvou souřadnic a
  přidání společného součtu zachová majorizaci. Indukce dojde k n.

To je úplný konečný důkaz správné jednoznačnosti profilů. Odpověď
21(b,c) v knize je jen citace; převzatá autorská zpráva Ramshaw 1977
má v §5 starší poznámky uvedeny přesné strany důkazu a vizuální kontrolu.
Časopiseckou verzi 1978 ani starý verifier jsme znovu neotevírali.

**21(c).** Převzat §6. Síť perfektních polygonů má maximální krok 2/m;
jejich stejnoměrná konvergence k `E(t)=lg(1+t)` dovolí sevřít libovolný
pevný pozitivní profil `(1−ε)L_j+ε(1/j,…,1/j)` v jeho konečně mnoha
rozích. Mezi rohy stačí konkávnost. Pro j=1 je porovnání přímo
`A(t)≥t`, takže argument nepotřebuje neexistující vnitřní roh.
Rovnoměrné rozštěpení převádí porovnání do společné dimenze;
spojitost se používá až poté při ε→0 v jediné pevné dimenzi j.
Pro každé j tak limsup libovolné strategie dominuje f_j(L_j).
Supremum přes j dává jak minimax, tak konečnou nerovnost pro W.
Je dovolen i výsledek +∞; žádné zaměnění limit není potřeba.

Zobrazené příklady funkcionálů byly rovněž porovnány s předpoklady.
Pro n·maximum a −n·minimum plyne monotonicita z prvního a předposledního
prefixu. Pro poměr maxima/minima platí na **kladných** délkách oba
směry. Pro `nΣ l_i²` plyne monotonicita z částečného sčítání:
je-li D_k=Σ_{i≤k}(l_i−l′_i)≥0, potom rozdíl součtů čtverců je
`Σ_{k<n}D_k[(l_k+l′_k)−(l_(k+1)+l′_(k+1))]≥0`.
Všechny čtyři funkcionály mají požadovanou invarianci po rovnoměrném
rozštěpení. Tři jsou spojité i pro nulové délky. Poměrový příklad na
hranici l_n=0 není konečný ani spojitý: pro (1−ε,ε) jde do nekonečna.
To je výslovná výhrada k jeho oboru, nikoli mezera důkazu pro skutečně
spojité funkce z předpokladu 21(c). Z kontextu pozitivních mezer lze
číst zamýšlený obor; netvrdíme platnost poměrového příkladu na uzavřené
simplexové hranici ani zde z nejasnosti oboru nevytváříme nový nález.

## Rozsah checkpointu

Dvě další úlohy jsou jednotlivě posouzeny ve všech sedmi částech,
včetně vedlejších příkladů a tištěných mezikroků. C0064/C0065 jsou
převzaty, nový C0249 je lokální chybný zbytek; počty nálezů nejsou
metrikou kvality. Strany 181, 594 a 595 se jako celky neuzavírají,
protože obsahují další úlohy. Bibliografická výjimka 1949 zůstává.
Další obnova: 26–30, pak hlavní text E od 168/file180. Dopředný
418/file430 nadále držen; žádný proces neběží.
