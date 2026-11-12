# Hitori: počty, symetrie a mez počtu černých polí

Rozsah: 4B, 7.2.2.1–439 až 445, str. 183 a 545–547. Hlavní přesné
výpočty pro 442, konstrukce 444 i bezsemenné úlohy 445 jsou hotové. Posuzujeme definici z knihy: bílé vrcholy tvoří neprázdné
minimální souvislé vrcholové pokrytí.

## F060: nepravdivá mez v úloze 443

Na desce 3×3 obarvěme černě všechny čtyři rohy. Bílé vrcholy tvoří kříž.
Jsou souvislé; černé vrcholy jsou nezávislé. Jediný bílý vrchol, který
nesousedí s černým, je střed, a ten je artikulací. Jde tedy o hitori cover,
ale 4 > (9+2)/3. Dokonce jde o jednoznačné řešení platného puzzle

```
AAA
BCD
EEE
```

V každé krajní trojici stejných písmen musí zůstat prostřední pole bílé,
a tedy oba rohy černé. Prostřední řádek jsou semena. Přímý výčet všech
512 obarvení potvrzuje jednoznačnost.

Pro každé liché n lze obdobně na desce 3×n obarvit černě sudé sloupce
horního a dolního řádku (číslování od nuly). Získáme n+1 černých polí,
což překračuje n+2/3. Bílé vrcholy tvoří strom: prostřední řádek s listy
v lichých sloupcích. Každý bílý vrchol bez černého souseda je artikulací.
Kontrolováno pro 51 lichých n až 101; platnost pro všechna n plyne z popisu.
Případ 3×1 je současně jednorozměrný protipříklad AAA.

Chybný krok důkazu na str. 547 je

```
b + 2c <= m+n+2 - [m even] - [n even] - [mn odd].
```

Pro čtyři černé rohy 3×3 je vlevo 8 a vpravo 7. Poslední odečítaný člen
je nutno odstranit. Správná mez plyne sečtením čtyř odhadů počtu černých
vrcholů na stranách: každá strana délky k má nejvýše ceil(k/2) černých
vrcholů. Rohy se počítají dvakrát. Pak porovnání počtu bílých hran
s počtem bílých vrcholů minus jedna dává obecně pro m,n>1

```
3s <= mn + 3 - [m even] - [n even].
```

Tedy jednoduchá univerzální oprava je (mn+3)/3. Jednorozměrné případy
mají nejvýše 0, 1, 2 černá pole při délce 1, 2, alespoň 3 a splňují
stejnou opravenou mez. Neprohlašujeme ji za ostrou pro všechny rozměry.
Nezávislý dynamický program pro váženou nezávislou množinu na obvodu
ověřil opravený mezikrok na 4 950 dvojicích rozměrů do 100×100.

Doklad znění: vykreslené PDF str. 183 a 547 a autorův původní PostScript
`fasc5c` str. 119 a 251. Historický vydaný Fascicle 5 má odpověď na str. 355.
V `all4b` ani `all4f5` příslušná oprava není. Tabulka na str. 546 sama
obsahuje správná maxima 4, 6, 8, 10 pro 3×3, 3×5, 3×7, 3×9, a tudíž
s chybnou mezí nesouhlasí. F060 je jeden nález zahrnující zadání a důkaz.

## F061: první interval tabulky 442

Na str. 546 má být v levém horním rohu tabulky černých polí `[0..0]`
místo `[1..1]`. Jediným hitori cover desky 1×1 je jediné bílé pole.
Také odpověď 441 výslovně považuje jednopísmenný puzzle za platný.
Obě verze sazby mají chybu: PDF str. 546 a PS str. 250 (historický
vydaný Fascicle 5 str. 354). V obou archivech errat nenalezena.

## Přesné počty a nezávislé kontroly

`hitori_zdd.cpp` staví rodinu všech souvislých vrcholových pokrytí pomocí
frontier stavu: komponenty bílých polí, černí sousedé a příznak uzavřené
komponenty. Poté operace NONSUB vybere inkluzně maximální množiny černých
polí, tedy minimální pokrytí. Implementace používá kanonický ZDD.

- Operátory UNION a NONSUB ověřeny na všech 65 536 dvojicích rodin
  podmnožin tříprvkové množiny; MAXIMAL na všech 256 rodinách.
- Pro 14 malých desek až do 4×5 nezávislý přímý výčet všech podmnožin
  kontroluje sousednost, souvislost flood fillem a odstranění každého
  bílého vrcholu. Shodují se počty i oba extrémy počtu černých polí.
- Všech 45 desek 1≤m≤n≤9 souhlasí s tabulkou počtů. Pro 9×9 vychází
  **32 411 910 059** hitori covers. Intervaly souhlasí kromě F061.
- Symetrické vzory počítá jiný algoritmus: výčet orbit příslušné grupy,
  nezávislost a přímý test minimality. Souhlasí všech 45 počtů pro
  vodorovnou i svislou symetrii a všech 27 čtvercových počtů pro D4,
  rotace o 90 stupňů a obě diagonály, včetně odečtení osminásobné symetrie.

Počty uzlů ZDD závisejí na pořadí proměnných a konkrétní reprezentaci;
naše menší hodnoty nepovažujeme za rozpor s uvedeným během Knuthova
programu. Mems a historické časy nebyly reprodukovány.

Výsledky: `results/hitori_counts.json`, `hitori_symmetry.json`,
`hitori_validation.json`, `hitori_operator_validation.json`,
`hitori_bounds.json`. Výpočet všech tabulek trval přibližně minutu.

## Co zbývá

Dodatek 443 je nyní posouzen níže: spodní asymptotická mez má obecný
důkaz. U popsané konstrukce modulo 5 je potvrzen rozpor F066. Obecnou
existenci jiného pokrytí s nejvýše mn/5+2 poli tím nevyvracíme.

## Doplnění: úlohy 441, 444 a 445 uzavřeny

### Jednořádkové puzzle a dvouřádkové pokrytí

Pro 1×n může být černé jen první a/nebo poslední pole: bílé buňky musí
tvořit interval a dvě černé nemohou sousedit. Přímý výčet 25 384 puzzle
v 28 kombinacích n≤7, velikost abecedy≤4 potvrzuje formuli odpovědi 441.
Pro n>1 je počet `(n−2)^2 d^(falling n−2)`; při n=1 je to d.

U 2×n označme sloupec bez černé buňky 0 a ostatní sloupce T nebo B.
Dva neprázdné sloupce nesmějí sousedit: stejné písmeno poruší nezávislost,
různé rozpojí bílé. Minimalita vyžaduje nejvýše jeden krajní nulový
sloupec a mezi dvěma neprázdnými sloupci právě jeden nebo dva nulové.
Delší mezera dovolí odstranit bílý vrchol cyklu. Při uvedených kratších
mezerách je naopak každý nechráněný bílý vrchol artikulací. Proto

```
X(z) = 2z(1+z)^2 / (1−2z^2−2z^3).
```

Rekurence X_n=2X_(n−2)+2X_(n−3) platí od n=4; první hodnoty jsou
2,4,6. Charakterizace byla navíc porovnána se všemi ternárními slovy
až do délky 10 přímým grafovým testem. `results/hitori_strips.json`.

### Obecná konstrukce 444

Položme n=3k, k≥2. Cyklický základní řádek je
`0,0,1,0,2,3,0,4,5,...,0,2k−2,2k−1`; řádek r je posunut o r doleva.
Pro t=1,...,2k−1 změňme nulu na 2k v buňce H_t=(r_t,c_t), kde

```
r_t = t+1            pro t≤k,
r_t = 2t−k+1         pro t>k,
c_t = 3t−r_t.
```

Řádky i sloupce těchto buněk jsou navzájem různé. Všechny nenulové
buňky jsou tedy semena. Pro k=3 vznikne přesně obrázek knihy.
Řešení: černé jsou buňky s r+c dělitelným třemi kromě H_t.

**Souvislost.** Ostatní buňky se dělí na diagonální pásy
r+c∈{3t+1,3t+2}. Každý pás je neprázdná souvislá klikatá cesta
(poslední je jediná buňka). H_t spojuje právě dva sousední pásy.
Bílé jsou proto souvislé. V každém řádku i sloupci zůstane právě jedna
nula, takže podmínka neopakování symbolů platí.

**Jednoznačnost při bílých semenech.** Roh (0,0) musí být černý: kdyby
byl bílý, sousední nuly (0,1),(1,0) by musely být černé a roh by byl
odpojený. Tyto dvě sousední nuly jsou tedy bílé. Označme zvláštní nulu
každého řádku Z_r, kde r+c≡1 (mod n). Bílá Z_r vynutí černé všechny
ostatní nuly téhož řádku a sloupce. Podél diagonály r+c=n to následně
vynucuje bílé Z_(r+1), nebo opačným směrem Z_r. Na této diagonále
chybí jediná nula, H_k=(k+1,2k−1), takže řetěz má jedinou mezeru.
Z prvního směru se šíří bílá Z_1; z druhého bílá Z_(n−1), vynucená
Z_0 přes (n−1,1). Oba konce jsou zachované pro k≥2. Všechny Z_r jsou
bílé a ostatní nuly černé. Tím je celé řešení určeno.

**Semena nelze dodatečně začernit.** Každé H_t je artikulace, protože
je jediným spojením dvou sousedních pásů. Každá jiná bílá buňka má
černého souseda, až na V=(n−1,n−3). Ta je také artikulací: buňka
(n−1,n−4) má V za jediného bílého souseda. Tento list existuje pro
n≥6; žádná jiná H_t mu neodstraňuje černé sousedy. Řešení je tedy
minimálním souvislým pokrytím. Jakékoli řešení s černým semenem lze
odčerněním semen rozšířit na řešení s bílými semeny, takže by bylo
vlastní podmnožinou právě dokázaného minimálního pokrytí: spor.

Pro k=1 stačí samostatný puzzle `000 / 021 / 111`, jehož jediné řešení
má černé čtyři rohy. Doslovné použití konstrukce určené pro k>1 při
k=1 minimalitu nesplňuje; to je naše záměrná okrajová kontrola, nikoli
chyba knihy.

Nezávisle ověřeny případy k=2,3,4,5,6,10,20, tedy až 60×60. SAT
kódování podmínek řádků, sloupců a sousednosti po vyloučení určeného
řešení potřebovalo vždy jediný nevyhovující model a dva platné řezy
souvislosti. Výsledné UNSAT certifikáty DRAT nezávisle ověřil drat-trim.
Případ k=1 zkontroloval výčet všech 512 obarvení.

Odpověď na otázku o méně než 2n/3 symbolech zůstává **ne** i po F060.
Opravená univerzální mez dává v některém řádku nejvýše
floor(n/3+1/n)≤floor(n/3) černých buněk pro n≥3. Případy n=1,2 jsou
přímé: 1×1 potřebuje symbol a jednobarevný 2×2 nemá platné řešení.

### Bezsemenné puzzle 445

Každá bílá buňka bez semene musí mít shodný černý symbol ve svém řádku
nebo sloupci. Přiřaďme jí R nebo C. V každém řádku může být nejvýše
b_r značek R a v každém sloupci nejvýše b_c značek C, kde b počítá
černé buňky. Proto mn−s≤2s, tedy s≥mn/3. Nutnost platí i tehdy,
pokud různé černé buňky nesou stejný symbol.

Z původního ZDD všech souvislých pokrytí (bez operace MAXIMAL) byly
vyexportovány **všechny** černé množiny nad tímto prahem. Počty pro
n=1,...,9 jsou 0,0,9,0,1,104,1,0,1952. Export byl zkontrolován proti
polynomu podle velikosti množiny a každé obarvení znovu přímým
flood fillem. RC problém řeší nezávislý maximální tok; shoduje se
s počítacím DP na 60 malých pokrytích. Počet přípustných obarvení
je 0 pro n≠6 a **56** pro n=6. Tím je konečné tvrzení pro n≤9 ověřeno
úplně, včetně nemožnosti 9×9, bez spoléhání na chybnou mez 443.

Pět obrázků z úlohy 445 bylo přečteno z vykresleného PDF. Nezávislé
DP po řádcích dává:

| Vzor | Černá pole | RC řešení | Puzzle na RC řešení | Celkem |
|---|---:|---:|---:|---:|
| (i) | 8 | 0 | 0 | 0 |
| (ii) | 12 | 4 | 20736 | 82944 |
| (iii) | 12 | 8 | 20736 | 165888 |
| (iv) | 12 | 0 | 0 | 0 |
| (v) | 12 | 1 | 62208 | 62208 |

Faktor na RC řešení je součin faktoriálů počtů černých buněk v řádcích
a sloupcích. Každý skrytý symbol lze nezávisle přiřadit příslušným
bílým R/C místům. Vzniklá L-trojice vynucuje alespoň jednu černou
buňku; jedinou možností s jednou je její roh. Alternativa vyžaduje
alespoň 13 černých buněk, zatímco i opravená horní mez pro 6×6
povoluje jen 12. Proto jsou všechna započítaná puzzle platná.

Počty používají konvenci knihy: pevný odlišný skrytý symbol u každé
černé pozice, bez libovolného přejmenování abecedy. Symboly z oddělených
řádků i sloupců lze ztotožnit bez změny jakékoli podmínky puzzle;
tyto různé zápisy nepřipočítáváme jako novou strukturu.

Známá oprava dvou obrázků na str. 547 z 12. října 2025 (P→E) není
nový nález. Neovlivňuje zde ověřované počty.

Výše uvedené výsledky nezávisejí na dodatku 443. Jeho následná kontrola
je zaznamenána v dalších oddílech.


## Dodatek 443: obecný důkaz dolní asymptotické meze

Nechť W je graf bílých buněk a s počet černých. V každém bloku W
(včetně mostů jako dvouvrcholových bloků) je maximální stupeň nejvýše 3.
Vrchol stupně 4 uvnitř bloku by totiž měl všechny své mřížkové sousedy
bílé, neměl by žádnou hranu do jiného bloku a nebyl by artikulací W.
Jeho začernění by zachovalo souvislé vrcholové pokrytí, což odporuje
minimalitě.

Každý dvousouvislý mřížkový blok má alespoň čtyři vrcholy stupně 2:
stačí extrémy čtyř lineárních forem ±r±c. Dva sousední takové extrémy
nemohou splývat, protože by společný vrchol měl stupeň nejvýše 1.
Pro každý blok tedy 2e_i ≤ 3v_i−4; pro most je tato nerovnost rovností.
Při b blocích platí Σv_i=|W|+b−1, a proto

```
2|E(W)| ≤ 3|W|−b−3 ≤ 3|W|−4.
```

Pro m,n>1 je |W|≥2. Se stejným značením a,b,c jako v knize (zde b
znovu označuje černé nerohové buňky na hranici) dostáváme

```
5s ≥ mn − 2m − 2n + 4 + 2b + 4c ≥ mn − 2(m+n) + 4.
```

Tím je mn/5−O(m+n) dokázáno s explicitní konstantou 2/5 u obvodu.
Jednorozměrné desky mají pravou stranu nekladnou, kromě triviálního
případu 1×1, který se vyřídí zvlášť. Nejde o převzatý Beluhovův důkaz;
je to naše nezávislé ověření tvrzené asymptotické meze.

## F066: konstrukce modulo 5 nedává slíbenou konstantu +2

Poslední věta dodatku na str. 547 navrhuje začernit všechny buňky
s i+2j dělitelným pěti a případně přidat další; výsledku přisuzuje
nejvýše mn/5+2 černých buněk. Tato konkrétní konstrukce nefunguje.

Na desce 7×7, se souřadnicemi 0 až 6, mají základní vzory
i+2j≡t (mod 5), t=0,...,4, postupně 10,10,10,10,9 černých buněk.
Každé doplnění na hitori cover, které tyto buňky zachová, má nejméně
**13** černých buněk. Tvrzená mez je přitom 49/5+2=11,8.

Při t=0 je jen pět buněk, které vůbec smějí být dodatečně černé:
(0,3), (1,6), (2,0), (6,4), (6,6). Všechny ostatní bílé buňky už mají
černého souseda. Dva z těchto pěti kandidátů jsou povinní: (0,3) a
(2,0). Dokud zůstanou bílí, nemají černého souseda a jejich sousedé
jsou spojeni cestami z vynuceně bílých buněk i po jejich odstranění.
Konkrétní spojovací cesty jsou:

```
Pro (0,3): (0,2)-(0,1)-(1,1)-(2,1)-(2,2)-(2,3)-(1,3),
           (0,4)-(1,4)-(1,3).
Pro (2,0): (1,0)-(1,1)-(2,1),
           (3,0)-(4,0)-(4,1)-(4,2)-(3,2)-(2,2)-(2,1).
```

Už těchto deset základních a dvě povinné buňky překračují 11,8.
Otočení desky převádí t=0 na t=1,2,3. Při t=4 jsou čtyři rohové
dvojice {(0,0),(1,0)}, {(0,5),(0,6)}, {(6,0),(6,1)}, {(5,6),(6,6)}.
Z každé musí být alespoň jedna další buňka černá: jinak lze bílý roh
odstranit, protože jeho sousedy spojuje třetí vrchol příslušného
jednotkového čtverce. To dává 9+4=13. Žádný posun počátku souřadnic
ani otočení tedy nepomůže.

Úplný výčet doplnění používá jen 32,32,32,32,256 podmnožin. Dvě
nezávislé implementace (množiny a bitové masky, přímý flood fill) se
shodují na minimu 13. Širší bitový výčet pokrývá 180 kombinací rozměrů
a posunů do 9×9, celkem 7 802 podmnožin. Znění bylo vizuálně potvrzeno
v PDF str. 547 i autorově PS str. 251; v all4b ani all4f5 oprava není.

**Důležitá hranice nálezu:** jiné hitori cover 7×7 s 11 černými buňkami
existuje. Našel ho nezávislý SAT model a ověřil přímý grafový test;
odpovídá i původnímu úplnému ZDD výčtu a správně přečtené tabulce.
Při průběžném čtení byla hodnota 12 omylem vzata ze sousedního řádku;
tento omyl byl odvolán a není součástí F066. Netvrdíme, že obecná
existence pokrytí s mn/5+2 je nepravdivá. Opravu vyžaduje popsaná
konstrukce, která dovoluje jen přidávání černých buněk.

Bezpečná slabší formulace pro ni je mn/5+O(m+n), když m,n>1. Základní
vzor je nezávislý a jeho bílé pole souvislé: kolem každé odstraněné
buňky lze mřížkovou cestu obejít po bílých sousedech, protože dvě
základní černé buňky mají vzdálenost alespoň 3. Každá vnitřní bílá
buňka už má přesně jednoho černého souseda. Doplňování na maximální
černou množinu se proto týká pouze O(m+n) buněk na obvodu.

SAT kódování pomocí svědků rozpojení po odstranění bílého vrcholu
bylo porovnáno s přímou definicí na 1 208 malých obarveních. Výsledek
7×7 je SAT, nikoli UNSAT certifikát; správný svědek je uložen v
`results/hitori_min_sat/7x7-atmost11-connected-g4.json`.
