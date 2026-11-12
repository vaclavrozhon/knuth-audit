# §4.3.1-34: čtyři operace s propojenou alokací

Zadání283 a odpověď627 přečteny v originálu. Úloha žádá implementaci
bez pevného omezení délky celých čísel, s propojenou správou paměti.
Odpověď uvádí příklady v Maederových článcích, nikoli vlastní program.
Dodáváme [spustitelný model](../sources/linked_integer.py), obecný důkaz
jeho vazby na A/S/M/D a [nezávislé kontroly](../verify_classical_linked.py).
Bez nového nálezu. Čtyři vrstvy errat prohledány podle283/627,34 a Maeder;
pro tuto úlohu nenalezena oprava.

## Formát a alokace

Základ b>=2 je počet hodnot jedné nezáporné číslice. Číslo reprezentuje
znaménko s z{-1,0,1} a obousměrně propojený seznam číslic d0,...,d_(n-1),
který má hodnotu s sum d_j b^j. Nenulové číslo má d_(n-1)!=0; nula má
prázdný seznam a s=0. Hlavička obsahuje délku a oba konce seznamu.
Jeden uzel obsahuje číslici a dva odkazy. Neexistuje požadavek, aby
uzly jednoho čísla ležely vedle sebe.

Pool obsahuje pevně vyhrazenou dostupnou paměť, zvolenou při inicializaci.
Všechny volné uzly tvoří další propojený seznam. Alokace odebere jeho
první uzel, uvolnění uzel vloží na začátek: obě operace mají konstantní
počet kroků a nevyhledávají souvislý úsek. Jednorázová inicializace
stojí O(kapacita). Délka čísla nemá samostatnou programovou mez;
omezuje ji jen paměť potřebná také pro vstupy a pracovní výsledky.
Adresy i délky se vejdou do adresového slova dostupné paměti.

Pokud volné uzly dojdou, model vrátí MemoryError. Správa dočasných
hlaviček uvolní i dosud nedokončené výsledky, vstupy zůstanou platné.
Jde o explicitní chování při vyčerpání skutečného poolu, nikoli další
omezení čísel. Úspěšný výstup vlastní volající a uvolňuje jej close().
Celá operace může číst tentýž objekt dvakrát; výstup dostává vlastní uzly.

Python je zde vykonavatelem modelu slov a odkazů. Aritmetické rutiny
neskládají víceslovné číslo do Python integer. Operandy v lokálních
násobeních a děleních mají nejvýše dvě číslice; vestavěná velká čísla
se používají pouze v označených převodnících testovacího orákula.
Nevydáváme tento model za optimalizovanou strojovou knihovnu.

## Operace a jejich důkazy

`add_abs` postupuje od nejnižších číslic a udržuje přenos0/1; po k
krocích jsou nižší k číslice správné a přenos představuje jejich
příspěvek do místa k. `sub_abs` má obdobný invariant výpůjčky a požaduje
|u|>=|v|. Poslední výpůjčka je0. Horní nuly se uvolní. Znaménková
operace nejprve rozhodne, zda přičítat velikosti, nebo odečítat menší
od větší. Vyžaduje O(max(m,n)) kroků a uzlů výstupu.

`multiply` je přesná smyčka M. Vnější iterace posune počátek výstupního
řádku o jeden odkaz, vnitřní iterace postupuje po obou seznamech.
Po dokončení j řádků je uložen přesný součin u s prvními j číslicemi v.
Lokální t=u_i v_j+w_(i+j)+carry splňuje0<=t<b²; podlaha t/b a zbytek
modulo b jsou další přenos a cifra. Dosud nedotčené místo i+j+1 po
poslední vnitřní iteraci je nulové, takže do něj patří závěrečný přenos.
Cena O(mn), výstup nejvýše m+n uzlů.

`divide_abs` pro jednociferného dělitele používá krátké dělení.
Pro delšího dělitele jde o algoritmus D s d=floor(b/(v_top+1)),
normalizovanými kopiemi a nejvýše jedním přičtením zpět. Jeho obecný
aritmetický důkaz je už uložen v [division.md](division.md). Zde navíc
ověřujeme realizaci odkazů: ukazatel high je u_(j+n), low je u_j,
předchozí odkazy high dávají dvě číslice pro odhad. Smyčka odečtení
jde přesně n odkazy od low k high. Po odečtení/korekci je high nulový;
oba krajní ukazatele se přesunou o jeden odkaz směrem dolů. Ukazatel
podílu se pohybuje stejně. Není potřeba opakovaně prohledávat seznam
kvůli indexování ani budovat pole ukazatelů na všechny číslice.

Koncový zbytek se vydělí normalizačním d; krátké dělení má nulový
zbytek. Platí u=qv+r,0<=r<|v| pro magnitudy. `divmod_trunc` vrací
podíl zaokrouhlený k nule a zbytek se znaménkem děleného, takže pro
podepsané vstupy zůstává u=qv+r a |r|<|v|. Nulový dělitel je ošetřen
před alokací. Cena pro M-místné u,N-místné v je
O(M+N+(M-N+1)N), je-li M>=N; paměť O(M+N). Délka jednoho číselného
objektu tedy nepřidává faktor způsobený procházením odkazů.

## Kontroly a bibliografický rozsah

[Výsledky](../results/classical-linked.json),[log](../results/classical-linked.log):
9604 úplných dvojic u,v v[-24,24] v základech2,3,10,256;720 větších dvojic
v šesti základech až2^32 a s délkami až100 slov. Každá dvojice prošla
součtem, rozdílem, součinem a dělením s přesným Python orákulem; dále120
případů se stejným vstupním objektem. V malém bloku proběhlo140 přičtení
zpět D6, ve větším404, takže opravná větev byla skutečně vykonána.
Strukturu seznamů ověřuje samostatný průchod, který porovnává množinu
živých a volných uzlů a kontroluje oba směry odkazů.

Samostatný paměťový scénář naplnil všech80 uzlů po opětovném použití62
rozptýlených volných uzlů. Všechny čtyři operace byly přerušeny nedostatkem
paměti a obnovily platný volný seznam, bez změny vstupů či úniku uzlů.
Běh78941 exit0, všechny3 checkpointy dokončeny; neopakovat bez nové změny.

Maederovy bibliografické údaje a popis obsahu souhlasí s primárními
záznamy vydavatele:
https://library.wolfram.com/infocenter/Articles/1665/
(6(2),1996,32–40, základní aritmetika a datové typy),
https://library.wolfram.com/infocenter/Articles/2531/
(6(3),1996,37–43, efektivní násobení a dělení).
Záznam prvního článku výslovně uvádí procedurální prototyp s poli.
Původní PDF odkazy nyní vracejí404; jejich obsah netvrdíme přečtený
ani naše propojené rutiny za doslovnou Maederovu implementaci.
Metadata pokusů jsou v sources/maeder-fetch-2026-11-02.json.
