# Přesná hranová mez 79 a úplná cena algoritmu H

Checkpoint X0102, P0959–P0966. Originály zadání p90/file107,
odpovědi p549/file566 a nákladového odstavce p70/file87 byly
přečteny. P0951–P0958 o správnosti H/I a nejvýše lg n
návštěvách vrcholu se přebírají bez opakování. Zde není
spuštěn program ani census.

Pišme ν(k) pro počet jedniček binárního zápisu nezáporného
celého k a f(n)=Σ_(0≤k<n)ν(k), s f(0)=0. Počet vrcholů
je n; m níže značí počet hran. Pro logaritmickou mez
předpokládáme n≥1, pro asymptotické náklady n≥2.

## Celá 79(a): dosažitelnost f(n) — P0959

Vezměme přesně štítky 0,...,n−1 stejné délky ceil(lg n).
Každý menší soused čísla k vznikne zrušením právě jednoho
jeho 1-bitu. Všech ν(k) takových čísel je nezáporných
menších než k, tedy jsou přítomna. Žádné jiné menší
číslo se neliší v právě jednom bitu. Počítáme každou
hranu u jejího většího konce, takže počet hran je f(n).
Pro n=1 stačí jediný prázdný štítek a počet je nula;
pro n=0 je přirozené prázdné pokračování rovněž nula.

## Celá 79(b): každá bitová pozice — P0960

Pro pozici j položme n=q·2^(j+1)+r, 0≤r<2^(j+1).
Počet jedniček v této pozici mezi 0,...,n−1 je přesně

    q·2^j+max(0,r−2^j).

Druhý člen nepřevyšuje r/2: pro r≤2^j je nulový,
pro r>2^j je nerovnost r−2^j≤r/2 ekvivalentní r≤2^(j+1).
Celý celočíselný počet je proto nejvýše floor(n/2).
Použitých pozic je ceil(lg n), takže

    f(n)≤floor(n/2)·ceil(lg n)≤n·ceil(lg n)/2.

To je tištěná mez i její silnější celočíselná verze.
Pro n=1 je počet pozic nula, takže žádná výjimka nevzniká.

## Všechny čtyři případy recidivy odpovědi 79(c) — P0961

Z ν(2k)=ν(k), ν(2k+1)=ν(k)+1 dostáváme pro k≥0

    f(2k)=2f(k)+k,
    f(2k+1)=f(k)+f(k+1)+k.

Definujme pro všechna p,q≥0

    g(p,q)=f(p+q)−p−f(p)−f(q).

Přímé dosazení uvedených dvou vzorců dává všechny čtyři
řádky; zápis g(a,b) je zde vždy tentýž nesymetrický g:

| vstup | pravá strana |
|---|---|
| g(2p,2q) | 2g(p,q) |
| g(2p,2q+1) | g(p,q)+g(p,q+1) |
| g(2p+1,2q) | g(p+1,q)+g(p,q) |
| g(2p+1,2q+1) | 1+g(p+1,q)+g(p,q+1) |

Například poslední řádek má na obou stranách rozvinutý
výraz 2f(p+q+1)−f(p)−f(p+1)−f(q)−f(q+1)−2p.
Ve smíšeném třetím řádku je společný výraz
f(p+q)+f(p+q+1)−f(p)−f(p+1)−2f(q)−2p−1.
První a druhý řádek vycházejí stejně přímo. Je to přesně
vytištěná jednotná recidiva

    g(2p+a,2q+b)=ab+g(p+a,q)+g(p,q+b), 0≤a,b≤1.

## Důsledná indukce a maximální recidiva f — P0962

Přímo z dvojic vzorců pro f plyne

    g(p,p)=0, g(p,p+1)=0, g(0,q)=0.

Pro ostatní uspořádané argumenty M≤N máme N≥M+2.
Napišme M=2p+a,N=2q+b. Pak q≥p+1, a tedy
p+a≤q a p≤q+b. Oba páry na pravé straně recidivy
jsou uspořádané a mají menší součet než M+N.
Silná indukce na součtu dává g(M,N)≥0, protože ab≥0.
Základní blízké páry jsme oddělili: nesmíme u M=N
neopatrně předpokládat nezápornost g(p+1,p).

Pro libovolné k,n−k tedy

    min(k,n−k)+f(k)+f(n−k)≤f(n).

Volba k=floor(n/2) dosahuje rovnosti podle g(p,p)=0
nebo g(p,p+1)=0. To dokazuje celou vytištěnou rovnici
s maximem přes 0≤k≤n, ne pouze její jednu nerovnost.
Pro n=0,1 rovnost platí přímo.

## Celá 79(c): horní mez pro každý indukovaný podgraf — P0963

Indukce podle n. Pro n≤1 nejsou hrany. Pro n>1 zvolme
bitovou pozici, v níž se některé dva štítky liší. Rozdělí
vrcholy na neprázdné části velikostí k,n−k, obě menší
než n. Přes tuto pozici může vést nejvýše min(k,n−k)
hran: každému štítku odpovídá nejvýše jediný štítek
s tímto bitem obráceným. Je to matching.

V každé části po smazání fixované pozice zůstává
indukovaný podgraf menší hyperkrychle, takže indukce
dává nejvýše f(k), respektive f(n−k) vnitřních hran.
P0962 nyní dává nejvýše f(n) hran celkem. V kombinaci
s 79(a) je mez přesná pro každý n. Výběrem skutečně
proměnné pozice jsme vyloučili kruhovou indukci s k=0.

Mediánové grafy jsou indukované podgrafy podle P0945,
proto mají m≤f(n)≤n·ceil(lg n)/2, tedy m=O(n log n).

## Počet operací H/I před řešením datových struktur — P0964

H1: BFS, přeskládání všech adjacency listů, inicializace
polí vrcholů i prvků hran stojí O(n+m). Každý adjacency
záznam si ponechá identifikátor původní hrany i odkaz
na opačný záznam. Oba seznamy jsou dvojitě zřetězené,
takže odstranění známé hrany I5 trvá O(1).

Všechny vrcholy navštíví I4 nejvýše floor(lg n)-krát
(P0958). Při každé návštěvě v hledání I4 a průchod I6
prohlédnou nanejvýš konstantní násobek původního deg(v).
I8 čte nejvýše první dva early sousedy; každá jednotlivá
operace I6–I9 má kromě požadovaného union/lookup O(1)
cenu. Celkem tedy nejvýše

    O(Σ_v deg(v)·lg n)=O(m log n)

prohlédnutých záznamů. Odstranění je přesně m; požadavků
I7 je K=O(m log n). Master list má n−1 položek, zásobník
rekurze nejvýše n a počet I1/I2/I10 je O(n). K těmto
údajům je nutné připočíst konkrétní realizaci hledání
mate hrany v I7 a slučování, nikoli je prohlásit zdarma.

## Konkrétní deterministická realizace I7 lookup — P0965

Stačí standardní RAM s O(log n)-bitovými adresami a
konstantními operacemi nad indexy velikosti polynomu v n.
Uvedeme realizaci bez hashování i bez inicializace n²
matice. Neprohlašujeme, že ji kniha už výslovně popsala.

I5 a I7 pouze ukládají požadavky na sjednocení; žádný
krok průchodu I1–I10 nečte výslednou ekvivalenční třídu.
Vlastní uniony proto lze provést po skončení H2 a před
H3, aniž se změní pořadí návštěv, mazání nebo výsledek.
I5 zná oba identifikátory hran. V I7 známe identifikátor
živé hrany u–v a pro druhou hranu uložíme dvojici
(min(mate(u),mate(v)),max(mate(u),mate(v))) čísel vrcholů.
P0955 zaručuje, že tato hrana v původním grafu existuje.

Očíslujme vrcholy 0,...,n−1. Dvojice všech původních
hran a všech K požadavků se seřadí lexikograficky dvěma
stabilními counting-sort průchody. Každý průchod nuluje
pole n čítačů a projde O(m+K) záznamů, tedy stojí
O(n+m+K). V každé skupině stejných dvojic je právě jeden
původní identifikátor hrany a libovolný počet požadavků;
lineárním průchodem jim identifikátor doplníme.

Celá fáze stojí O(n+m+K) času a paměti. Žádné pátrání
v adjacency listu levého mate vrcholu nepřidává další
faktor stupně ani logaritmu. Máme teď přesně tytéž union
požadavky, které požaduje abstraktní H/I.

Pro srovnání autorův `sources/embed.w`, řádky 74–82 a
401–408, řeší právě tento přístup přímou maticí ukazatelů.
Byly čteny pouze relevantní datové struktury a union;
celý doprovodný program nebyl přezkoušen ani spuštěn.
Jeho pevné limity nmax/cmax se nepoužívají jako argument
pro asymptotický algoritmus v knize.

## Cena unionů, celková mez a výjimka H3 — P0966

Každý původní hranový prvek má přímý ukazatel na svého
reprezentanta. Třída má zřetězený seznam prvků a velikost.
Požadavek s dvěma stejnými reprezentanty stojí O(1).
Při skutečném sloučení přepíšeme ukazatele jen prvkům
menší třídy a oba seznamy spojíme za O(1).

Kdykoli se ukazatel daného prvku mění, velikost jeho
třídy se alespoň zdvojnásobí. Žádný prvek se tedy
nepřepíše více než floor(lg m)-krát; všechny úspěšné
uniony dohromady stojí O(m log(m+1)). O(1) cena každého
požadavku přidá O(m+K). To je také princip konkrétního
unionu v `embed.w`, řádky 136–143 a 200–214; zde má
samostatný amortizovaný důkaz.

Pro jednoduchý graf log(m+1)=O(log n). S P0964/P0965
získáváme celkem

    O(n+m log n)=O(n(log n)^2)

před materializací všech bitových štítků. Důkaz zahrnuje
vyhledání hran, všechny uniony, mazání, frontu i předzpracování;
nevyžaduje průměrný čas hashování. Odložené požadavky
používají O(n+m log n) pomocných slov. Kniha zde žádnou
menší prostorovou mez netvrdí. Méně efektivní libovolná
implementace vysokých operací nemusí téže ceny dosáhnout.

Počet tříd t≤n−1, protože každému neprázdnému řezu
odpovídá aspoň jedna hrana spanning tree a každá hrana
stromu patří právě jedné třídě. Očíslování tříd stojí
O(m). Při přímém bitovém výstupu H3 kopíruje n−1 řetězců
délky t a změní v každém jeden bit: O(nt) bitových
operací, případně O(n·ceil(t/w)) slov pro w-bitová slova,
s triviálním samostatným případem t=0. Úplný explicitní
výstup má nt bitů. To je přesně důvod tištěné výjimky
pro nastavování štítků; výstupní náklad jsme neskryli
do O(n(log n)^2).

## Errata, bibliografické limity a stránkový rozsah

Všech pět vrstev `all4a-pre`, `all4a`, `err4a`, `all4f0`,
`all4f1` prověřeno pro 79/H/náklady. F0 p90, 13. 12. 2009
opravuje „subgraph“ na „induced subgraph“; náš dotisk
4A už má správné znění. Nový nález nevznikl.

Historický odkaz Annals of the New York Academy of
Sciences175 (1970),170–186 nebyl v rychle dostupném
primárním zdroji ověřen. Knuthův vlastní bibliografický
seznam v `mariages-stables.pdf` potvrzuje titul
*Mathematical analysis of algorithms*, IFIP Congress1971,
vydání1972,19–27; konkrétní obsah p24 znovu ověřen nebyl.
Tyto bibliografické výjimky nejsou použity jako důkaz79.
Autorův primární EMBED má ověřený původ na stránce programů;
metadata a přesný rozsah čtení jsou ve zdrojovém záznamu.

P70 má nyní doloženu celou správnost i náklady H/I.
Před povýšením celé stránky zbývá propojit její poslední
odstavec s konkrétní Table2 na p71. P90/p549 zůstávají
partial zejména pro 80,82,83. Vlastní všechny části79
jsou úplné; žádné převzetí maximální hranové meze bez
obecného důkazu nezůstalo.
