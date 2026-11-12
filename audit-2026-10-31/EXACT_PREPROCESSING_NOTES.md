# Předzpracování přesného pokrytí: Algorithm P, 218–224

Kontrola 1. listopadu 2026. Použit původní
[DLX-PRE](https://www-cs-faculty.stanford.edu/~knuth/programs/dlx-pre.w),
archivovaný se SHA-256 v `sources/knuth-programs/`. Překlad:

```
ctangle dlx-pre.w - /tmp/knuth-program-build/dlx-pre.c
gcc -O2 -Wno-implicit-int -Wno-implicit-function-declaration /tmp/knuth-program-build/dlx-pre.c -o /tmp/knuth-dlx-pre
```

Hlavička `gb_flip.h` je v pracovním adresáři překladu; program nevolá její
funkce. Originální zdroj nebyl změněn.

## Zapracovaná známá errata E011

Ve vzorcích (103) a (105) je argument p, nikoli i (2. ledna 2025).
P3 má testovat i>N (11. března 2026). P5 má přeskočit také obarvený
první uzel (2. ledna 2023). Tyto chyby se nepočítají mezi nové nálezy.

## Ověření algoritmu a odpovědí 220–223

[check_exact_preprocessing.py](check_exact_preprocessing.py) implementuje
adresy, ULINK, DLINK, TOP, COLOR, spacery i zkracování řádků podle knihy.
Při testu blokování dokončí celý průchod a pak jej obrátí; nepoužívá
optimalizovaný skok uprostřed smyčky. Zásobník rušených řádků je obyčejný
seznam adres místo dočasného přepsání TOP. Při každé stabilní fázi kontroluje
všechny obousměrné seznamy, hlavičky a jejich délky.

Na 1 500 náhodných úlohách s 1–4 primárními a 0–3 sekundárními položkami,
1–10 možnostmi, barvami a opakováním možností souhlasí **přesné množiny
původních čísel řádků** před a po zpracování, u obou implementací. Oracle
prochází všechny podmnožiny řádků, bez DLX. Všech 1 212 splnitelných vstupů
má navíc shodný redukovaný výstup. Rozdíly ve 178 nesplnitelných případech
jsou jen v názvu jediné ponechané prázdné primární položky. Zbývajících
110 nesplnitelných případů má i tuto reprezentaci shodnou.

Polovina vstupů začíná primární položkou v každé možnosti; všechny jejich
výstupy jsou bez dalšího blokování a nucených položek. U libovolného pořadí
zůstalo v 72 případech dohromady 122 blokovaných možností. Důvod je známé
omezení z komentáře autorova zdroje k opravě P5 z roku 2023: obarvený první
uzel se přeskočí. Například `s:1 a`, `a`, `b s:2` na primárních a,b obsahuje
neužitečný první řádek. Přesunutí a na začátek jej odstraní. Toto evidujeme
jako známé omezení, nikoli nový nález. Data: [random.json](results/exact_preprocessing/random.json).

Obecná správnost redukcí: možnost blokující jinou primární položku nemůže
být součástí řešení. Jestliže každá možnost pro primární p obsahuje i bez
barvy, pak lze odstranit i a všechny jeho možnosti bez p; každé řešení
stále vybírá právě jednu původní možnost pro p. Tato bijekce zachovává i
opakované možnosti jako různé řádky. Zkrácením nemůže zmizet poslední
primární položka z ponechaného řádku, protože v něm zůstává p.

218: dvě různé barvy nelze prostě zapomenout, protože by mohly přestat
omezovat jiné možnosti. 219: volba možnosti s i bez p,q nutí obě možnosti
pro p a q použít j bez barvy, což je spor; důkaz je správný. Samotné smazání
i,j nemusí zachovat počet řešení. Obecné argumenty 218–219 byly zkontrolovány,
historické rychlosti a velké příklady 225 nikoli.

## F074: konstrukce 224 nemá požadovaný počet průchodů

Znění potvrzeno v PDF, strana 475, a autorově PS, strana 179.
Pro **n=6** má uvedená konstrukce 15 položek a 18 možností. Oba programy
provedou jen **čtyři pracovní průchody**, poslední bez změny. V doslovném
Algorithm P to znamená **pět návštěv P2**, včetně posledního testu C=0;
ani jedna konvence nedává šest.

[Přesný vstup se jmény z knihy](results/exact_preprocessing/chain6.xcc),
[úplný autorův výpis](results/exact_preprocessing/chain6.log),
[nezávislé stopy pro n=2,…,30](results/exact_preprocessing/chains224.json).
V tomto rozsahu je počet pracovních průchodů min(n,4); obecnou konstantní
mez pro všechna n jsme samostatně nedokazovali. Již n=6 je úplný protipříklad.

Mechanismus selhání: od konce řetězce se v prvním průchodu odstraňují
blokující možnosti. Například `i2 p4 x5` blokuje p5; následně se odstraní
`i3 p3 x4` a `i4 p2 x3`. Kniha tuto opačnou propagaci nezohledňuje.
V dalších dvou průchodech se zbytek rozpadne, čtvrtý potvrdí stabilitu.

### Náhradní rodina s lineárním počtem možností

Jednodušší barevná rodina: primární P_(z−1),…,P_0 v tomto pořadí a
sekundární E_0,…,E_(z−2). Pro každé k jsou dvě možnosti P_k s barvou c=1,2
na sousedních E_(k−1),E_k, pokud existují. Pro k=0 ponecháme jen c=1.
V každém průchodu od konce řetězce se odstraní právě další možnost c=2;
proto máme z pracovních průchodů včetně závěrečného bez změny.

Rodina funguje také **bez barev**: každý E_k nahradíme dvěma sekundárními
položkami E_(k,0),E_(k,1). Možnost hodnoty c v P_k používá odchozí E_(k,c)
a příchozí E_(k−1,1−c). Sekundární položky řadíme po dvojicích od konce
řetězce. P_0 má jen hodnotu 0. Rozdílné sousední hodnoty se střetnou,
stejné nikoli. Primární fáze posune známou hodnotu 0 o jeden vrchol a
sekundární fáze o další; opačné pořadí položek další propagaci v témže
průchodu zastaví. Pro z=2n−2 dostaneme n pracovních průchodů, 4n−5 možností,
2n−2 primárních a 4n−6 sekundárních položek. Pokud požadujeme doslova
n návštěv P2 včetně konečné, použijeme z=2n−4 pro n≥3.

Obě varianty souhlasí s původním DLX-PRE pro n=2,…,30:
[barevná](results/exact_preprocessing/replacement224.json),
[neobarvená](results/exact_preprocessing/replacement224-uncolored.json).

## C013: potvrzené vynechání inicializace značek v hlavičkách

P1 odkazuje na C1; strana 89 výslovně dovoluje neinicializované COLOR v
hlavičkách. Odpověď 220 ale jejich hodnoty porovnává s adresou prvního uzlu.
Vstup `a b | s`, řádky `a s:1`, `a`, `b s:2`, má první uzel na adrese 5.
Pokud COLOR(b)=5 již při vstupu, test přehlédne blokování b prvním řádkem;
algoritmus skončí bez jeho odstranění. S COLOR(b)=0 jej odstraní.
[Přesná reprodukce](results/exact_preprocessing/header-initialization.json).

Oprava by byla inicializovat COLOR všech primárních hlaviček na nulu v P1.
Původní C program má nulovanou paměť z calloc, takže tuto potíž nemá.
Při závěrečné revizi bylo potvrzeno, že P1 skutečně přebírá jen C1 a žádnou
inicializaci značek nedoplňuje. P1 byl znovu přečten v obrazu PDF i autorova PS;
strana89 výslovně připouští neinicializované hodnoty. Nález je nyní potvrzený,
původní identifikátor C013 zůstává kvůli návaznosti evidence. Nejde o ztrátu
řešení, ale o nesplněný požadavek úplného odstranění blokování. Ukazatelový
příklad již používá všechny známé opravy z let2023–2026.

## Zpřesnění po doslovné kontrole 3. listopadu 2026

Nová [F145](F145_PREPROCESS_DELETE_LOOP.md) ukazuje chybu koncové podmínky mazací smyčky221. Starý model výše používal předem sestavený seznam uzlů a tuto podmínku netestoval. Jeho přijaté výsledky nejsou důkazem doslovné smyčky. Nové přesné rozsahy, oprava a malé kontroly jsou v [úplném průchodu218–224](PREPROCESS218_224_SOURCE_NOTES.md). Známé opravyE011 byly zapracované do modelu, nikoli do našehoPDF. Staré programy a výsledky se nemění.
