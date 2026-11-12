# Optimalizační převody, 239 a 243–250

## F078: úloha 243 musí omezit váhy na primární položky

Zadání na straně 153 připouští váhu každé položky XCC problému. Odpověď
na straně 478 ale používá rovnost Σx_k=W, která u sekundárních položek
neplatí: mohou zůstat nepokryté nebo se vyskytnout opakovaně ve stejné barvě.

Krátký protipříklad má primární položky a,b, sekundární s a všechny váhy 1.
Možnosti jsou `{a}`, `{a,s}`, `{b}`. Každé řešení používá d=2 možnosti.

| Řešení | Váhy možností | Σx² | Σ(x−2)² |
|---|---|---:|---:|
| `{a}`, `{b}` | 1,1 | 2 | 2 |
| `{a,s}`, `{b}` | 2,1 | 5 | 1 |

Minimum prvního kritéria tedy neminimalizuje druhé. Není potřeba žádná
záporná váha ani barevná kolize. Zadání i odpověď jsou shodné v autorově
Pre-Fascicle 5C na stranách 89 a 182; všechny čtyři stránky byly vizuálně
ověřeny. Odpovídající oprava v all4b ani all4f5 nebyla nalezena.

Oprava: vážit jen primární položky a nechat sekundární přispívat nulou.
Pak je Σx_k=W konstantní a obecný důkaz knihy funguje pro libovolné reálné r.
Ještě obecněji stačí, aby celková započítaná váha byla stejná v každém řešení.
Hlavní aplikace na rozdělení států má pouze primární položky, proto ji tato
chyba nezasahuje.

## Ostatní převody

**239.** Pro každé původní pokrytí C zvolíme možnost `j k1 ... j kt`
právě pro j mimo C. Pro každý prvek k vybereme jednu množinu j∈C, která jej
obsahuje, a pokryjeme k párovou možností `k jk`; ostatní `jk` jsou samostatné
nulové možnosti. Dostaneme přesně původní pokrytí s nějakým přiřazením
prvků množinám. Hlavní cena je součet vah mimo C, tedy konstantní celková
váha minus cena C. Infinitesimální ε^j vybere pro každý prvek nejmenší
možné j a poskytne jedinečného reprezentanta pro dané C. Zmíněná poznámka
ke k nejlepším řešením je potřebná. Prázdné původní množiny s kladnou cenou
lze předem odstranit; nejsou součástí optimálního pokrytí.

**244.** U neorientovaného grafu je počet vnitřních uspořádaných nehran
n(t−1)−2k a součet vnějších stupňů 2(m−k). Oba cíle tedy maximalizují k.
U digrafu a orientovaných nehran jsou analogicky n(t−1)−k a m−k;
při započítávání obou směrů vnější hranice má druhý výraz faktor 2.
Tvrzení o společném optimu platí i zde.

**247.** Odečtení minima cen možností jedné primární položky zachová
nezápornost a sníží cenu každého řešení o tutéž hodnotu. Jakmile má položka
nulovou možnost, další odečty ji nezkazí: každá další položka této nulové
možnosti má sama minimum nula. Proto po jedné průchodové sérii má každá
primární položka alespoň jednu nulovou možnost. Lineární dualita uvedená
v odpovědi má správný směr nerovností; duální proměnné nemusí být nezáporné.

**249–250.** Nejlepší spodní mez ze známých t cen vznikne doplněním
neznámých dk−t cen nulami a součtem každé k-té ceny v seřazeném seznamu.
Doslovný algoritmus 249 je kontrolován po každém přijatém prvku proti tomuto
přímému třídění. Pro hint z je mez platná: každá budoucí možnost pokrývá z
položek a její cena je alespoň maximum jejich jednotlivých minimálních cen.
Nejmenší součet takových maxim se dostane seskupením seřazených hodnot
po z, což dává právě uvedený součet. Oddělené třídy Z pokrývají každou
budoucí možnost právě jednou. Součty se vzájemně nesčítají; každý jednotlivě
poskytuje bezpečnou mez.

## Výpočetní kontrola a omezení rozsahu

[check_cost_reductions.py](check_cost_reductions.py) porovnává původní DLX5
s úplným výčtem podmnožin malých XCC vstupů, včetně nulových cen, barev,
shodných řádků a různých K. Nejde o formální verifikaci celého ukazatelového
algoritmu. Historické počty memů zde neporovnáváme.

Dokončeno: 1000 náhodných vstupů DLX5, všechny požadované nejnižší ceny
souhlasí včetně násobností; 157 497 prefixových kontrol algoritmu 249.
Výsledek: [verified.json](results/cost_reductions/verified.json).
