# Úlohy 7.2.2.1–75–76: semisymetrické kvazigrupy

Kontrola 1. listopadu 2026 UTC / 2. listopadu v Praze. Lokální 4B,
první vydání, druhý dotisk. Zadání na tištěné132 (PDF152), odpovědi432
(PDF452); autorův Pre-Fascicle5C z11.9.2019 má68/136 (PDF74/142).
Obě dvojice originálních stránek byly zobrazeny. Vydaný Fascicle5 používá
strany130/240; tyto posuny jsou zahrnuty při hledání errat.

**Dva nové nálezy:** F121 je drobný chybný operátor v75(b). F122 je
podstatná chyba redukce76(c): pro každé n≥2 vytvoří nesplnitelný problém,
i když hledaná tabulka existuje. Oba jsou v PDF i autorově PS a nemají
nalezenou odpovídající opravu v kontrolovaných erratech. Fyzický výtisk
nebyl ověřen. Potvrzení neznamená doložené prvenství.

Matematické části všech75(a–e),76(a–c) jsou po uvedených opravách
prověřeny obecnými důkazy a úplnými malými výčty. Celé úlohy prozatím
zůstávají `partial`: původní úplný Bennett1978 a Stein1957 nebyly získány.
Bibliografii není správné vydávat za plné přečtení článků.

## Reprodukovatelnost a úplné výčty

Spuštění: `python3 audit-2026-10-31/check_gropes.py`.
[Výsledek](results/gropes75/check.json), vstupy a protokoly původního
nezměněného DLX1 jsou v `results/gropes75/`. Každá úplná množina tabulek
má komprimovaný JSON se SHA256; všechny nalezené tabulky jsou znovu
ověřeny přímo dosazením obou identit a latinskostí všech řádků i sloupců.

Tři metody: přímé sestavování latinských řádků do n=5, nezávislé přesné
pokrytí neměnnými bitovými maskami a původní DLX1 do n=6. U prvního
postupu se projdou všechny permutace každého řádku; prefix se odstraní
jen při opakování ve sloupci nebo při porušení již úplně určené identity.
Nepoužívá možnosti redukce75(d). Porovnávají se celé množiny tabulek,
nikoli jen jejich počty. Mezi dvěma XC metodami se porovnávají také celé
množiny vybraných možností.

| n | všechny | idempotentní | komutativní | neutrální prvek0 | tištěné76(c) |
|---|---:|---:|---:|---:|---:|
|1|1|1|1|1|1|
|2|2|0|2|1|0|
|3|3|1|3|0|0|
|4|18|2|16|1|0|
|5|120|0|30|2|0|
|6|2880|0|480|0|0|

Prázdné univerzum přesného pokrytí má právě jedno řešení, prázdnou
množinu možností. To je zvlášť ošetřeno: DLX1 vyžaduje neprázdnou
hlavičku, proto se jeho nezpůsobilý vstup nevydává za výsledek počítání.
První vlastní běh měl chybu dekodéru triviálního n=1 u doslovné varianty;
po doplnění vynuceného neutrálního prvku celý běh prošel. Nešlo o chybu knihy.

## 75(a): druhá identita a latinskost

Označme danou identitu `x∘(y∘x)=y`. Její použití nejprve na
`(y,x)` a potom na `(x∘y,y)` dává přesně tištěný důkaz:

`(x∘y)∘x = (x∘y)∘(y∘(x∘y)) = y`.

Levé a pravé translace pro pevné x jsou tedy vzájemně inverzní:
`L_x R_x = R_x L_x = id`. Jsou bijektivní i pro nekonečnou množinu,
takže jde skutečně o kvazigrupu; nebyla použita konečnost ani asociativita.
Z `x∘y=z` dostáváme `y∘z=x` a `z∘x=y`. Každá trojice se tedy uzavírá
cyklicky. Prázdná množina splňuje samotnou zadanou identitu vakuózně;
netriviální konstrukce níže používají n≥1.

## 75(b), F121: plus má být XOR

Všech pět tabulek bylo přepsáno z originálu po všech80 položkách a
ověřeno. První je `x XOR y`, druhá `(-x-y) mod4`. Prohození značek1/2
v druhé dává třetí. Poslední dvě přecházejí jedna v druhou při každé
ze šesti transpozic prvků. Úplné S4 orbity první, třetí a poslední mají
velikosti4,12,2 a jsou disjunktní; pokrývají všech18 tabulek řádu4.

Ve čtvrté tabulce `f=(0,2,3,1)`, v páté `f=(0,3,1,2)`. Obě mají
`x∘y = x XOR f(x XOR y)`. Při `t=x XOR y` platí přesně

`x∘(y∘x) = x XOR f(t XOR f(t))`.

Proto je nutnou a postačující podmínkou **`f(t XOR f(t))=t`**.
Odpověď432 píše obyčejné **`f(t + f(t))=t`**. Pro první z obou funkcí
už t=2 požaduje nedefinované f(5). Ani skrytý výklad sčítání modulo4
chybu nezachrání: pro t=3 je f((3+1)mod4)=f(0)=0≠3. U druhé funkce
dává t=1 při tomto výkladu rovněž0≠1. Všechna čtyři správná dosazení
XOR pro obě funkce jsou v JSON.

Jde o chybný symbol v pomocném zdůvodnění, nikoli o neplatnost tabulek
nebo klasifikace. Zadání samo správně důsledně používá symbol⊕.

## 75(c): obecné konstrukce

Na zbytkových třídách modulo n funguje `x∘y=-x-y`, neboť
`-x-(-y-x)=y`. Pro obecnou grupu a prvek a s a²=1 definuje kniha
`x∘y=a x⁻¹ a y⁻¹ a`. Inverze `y∘x` je `a x a y a`, takže

`x∘(y∘x) = a x⁻¹ a (a x a y a) a = y`.

Zrušení sousedních a² a x⁻¹x je legitimní bez komutativity. V komutativní
grupě funguje pro libovolné a také `x∘y=x⁻¹y⁻¹a`; po dosazení se
všechny faktory kromě y zruší. Nezávislé konečné doplňky kontrolují
všechny involuce v S1 až S4 a všechny dvojice prvků, dále všechny
parametry a v cyklických grupách řádu1–40. Tyto testy nenahrazují obecný důkaz.

## 75(d,e): přesná bijekce a počet idempotentů

Z tabulky rozdělme uspořádané dvojice `(x,y)` do cyklů transformace
`(x,y) ↦ (y,x∘y)`. Díky75(a) má transformace třetí mocninu identitu.
Pevný bod znamená `x=y=x∘x` a dává jedinou položku `xx` typu(i).
Jinak má cyklus délku3. Pokud se v jeho trojici opakuje menší prvek,
dostáváme typ(ii) `xx xy yx`, x<y. Pokud se opakuje větší prvek,
dostáváme typ(iii) s y=z. Tři různé prvky reprezentujeme jednoznačně
nejmenším x a jednou ze dvou orientací zbytku. Tím je zahrnuta každá
možná cyklická trojice právě jednou.

Obráceně přesné pokrytí určí v každé dvojici právě jednu hodnotu součinu;
cyklické doplnění řádků je konzistentní a přímo splňuje obě identity.
Neexistují jiné volby, takže jde o bijekci, nikoli pouze injekci.
Počet možností je

`n + C(n,2) + Σ_(r=0)^(n−1) r² = n + (n³−n)/3`.

Je-li k prvků idempotentních, vybrané možnosti mají k singletonů
a zbytek je velikosti3. Proto `n²-k` dělí3, jak říká75(e).
Úplné výčty mají spektra `k:počet`:

```
n1: 1:1           n2: 1:2
n3: 0:2, 3:1      n4: 1:16, 4:2
n5: 1:80, 4:40    n6: 0:480, 3:2400
```

V tomto rozsahu přesně potvrzují uváděnou výjimku n=k=6 i všechna
povolená k. Netvrdíme tím nezávislý důkaz Bennettovy věty pro všechna n.

## 76(a,b): idempotence, komutativita a trojice

Idempotence vynutí všechny singletony. Po jejich předvýběru odstraníme
diagonální položky a každou možnost s opakovaným prvkem. Zbudou
`n(n−1)` uspořádaných dvojic a `2 C(n,3)` orientovaných trojic. Každé
řešení tedy obsahuje `n(n−1)/3` cyklů, které pokrývají každou dvojici
různých prvků právě jednou: přesně Mendelsohnův systém.

Komutativita dovoluje sloučit dvojice `(x,y),(y,x)` do jedné položky
s x≤y. Cyklus s trojicí všech stejných je singleton; opakovaný menší
prvek dává `xx xy`, opakovaný větší `xy yy`; tři různé prvky dávají
`xy xz yz`. Jejich tabulkové hodnoty se doplní všemi permutacemi trojice.
Z přesného pokrytí dostaneme jedinou komutativní kvazigrupu a obráceně.
Celkem je `C(n+1,2)` položek. Kniha typ(i) neruší, takže se zachovává.

Komutativita spolu s cyklickými záměnami dává úplnou symetrii vůči S3
(transpozice a třícyklus generují S3). Při idempotenci se trojice různých
prvků stanou neuspořádanými bloky pokrývajícími každou neuspořádanou
dvojici jednou: Steinerovy trojice. Tato korespondence je obecně dokázána,
bez závislosti na dostupnosti Steinova původního článku.

## 76(c), F122: je nutné vynechat také x=y

Neutrální prvek0 vynutí `x∘0=0∘x=x` a z identity s y=0 také
**`x∘x=0`**. V původním75(d) jsou tedy předem vybrány singleton00
a všechny trojice `0x xx x0`. Jejich odstranění z univerza vynechává
řádek0, sloupec0 **i celou diagonálu**.

Odpověď432 však přikazuje vynechat pouze x=0 nebo y=0. Ponechá n−1
položek `11,...,(n−1)(n−1)`, ale žádná z uvedených možností typu(iii)
se třemi různými kladnými prvky je neobsahuje. Pro každé n≥2 je tak
tištěné XC nesplnitelné. Nejmenší protipříklad je n=2:

```
   0 1
0  0 1
1  1 0
```

Tabulka XOR je platná grope s neutrálním prvkem0. Tištěná redukce má
jedinou položku11 a žádnou možnost; opravená má prázdné univerzum
a jediné prázdné řešení, které se doplní právě na uvedenou tabulku.

Oprava: **vynechat položky s x=0, y=0 nebo x=y**. Pak zůstává
`(n−1)(n−2)` položek a `2 C(n−1,3)` možností, jak už správně píše kniha.
Výsledek pro x,y>0 a x≠y není0 (jinak by x=y), ani x nebo y
(odporovalo by to vynucenému nulovému diagonálnímu součinu).
Na kladných prvcích tedy pouze nahradíme `x∘x=0` hodnotou x: dostaneme
idempotentní grope řádu n−1. Obráceně přidání0 a uvedených vynucených
součinů vždy funguje; toto je úplná bijekce tvrzená poslední větou odpovědi.

## Primární citace a známá doplnění

Datované adresy, výsledky HTTP a hashe jsou v `sources/gropes75/fetch-*.json`.
Stažené soubory zůstaly beze změn. [Kontrola zdrojů](results/gropes75/source-check.json)
odděluje skutečně získané originály od pouhých bibliografických metadat.

- **Schröder1876**, *Ueber v. Staudt's Rechnung mit Würfen und verwandte
  Processe*, Math. Annalen10,289–317: získán celý původní svazek ze skenu
  Google/InternetArchive. Strany289,305–306 zobrazeny. Rovnice(40–41)
  definují levou a pravou inverzní operaci; `(C0)` na306 je
  `a:b=ab=b/a`, ekvivalentní semisymetrii. `(C1),(C2)` společně znamenají
  úplnou symetrii. Číslo strany a matematický obsah citace sedí. Autor
  odkazuje na vlastní publikaci1874; absolutní historické prvenství
  neprohlašujeme za ověřené. Knuthovo „seems“ tuto nejistotu již připouští.
- **Mendelsohn1971**, *A Natural Generalization of Steiner Triple Systems*,
  v Atkin/Birch, *Computers in Number Theory*,323–338: úplný původní sborník
  získán z archivu Atlas Laboratory. Theorem1 na325 je přesně použitá
  bijekce. Theorem5 na331 a pokračování332–333 dávají existenční spektrum.
  Původní text výslovně vynechává také v=1; v knižní definici lze tento
  triviální případ doplnit jedinou jednoprvkovou tabulkou a prázdnou
  rodinou trojic. Nejde o chybu4B. Nevýskyt n=6 potvrzují oba naše úplné
  výčty. Strany323,325,331 byly zobrazeny, zbytek uvedeného důkazu přečten.
- **Bennett1978**, *Extended cyclic triple systems*, Discrete Math.24,
  139–146, DOI10.1016/0012-365X(78)90192-9: metadata Crossref/Elsevier
  a veřejný vydavatelský abstrakt potvrzují tematickou a bibliografickou
  shodu. Přesné znění obecné existenční věty a původní důkaz zatím nejsou
  z plného článku ověřeny. Vydavatelský PDF endpoint vrací403, API pro
  PDF406; XML obsahuje jen metadata. To není důvod prohlašovat tvrzení
  knihy za chybné ani za plně zrevidované.
- **Stein1957**, *On the foundations of quasigroups*, Trans. AMS85,
  228–256, §8: Crossref potvrzuje bibliografii a DOI
  10.1090/S0002-9947-1957-0094404-6. Původní PDF AMS vrací403.
  Indexovaný přepis §8 sloužil pouze jako navigace; originál této sekce
  ještě nebyl vizuálně zkontrolován. Odkaz OpenAlex na PMC528312 není
  používán jako náhrada: jeho totožnost s citovaným29stránkovým článkem
  nebyla doložena.
- **E038**, oficiální doplnění13.2.2024: topologické gropes u Cannona,
  Bull. AMS84(1978),832–866. Úplný původní článek z univerzitního archivu
  Edinburgh získán. Supplement13,860–861 skutečně definuje nekonečný
  topologický2-komplex a uvádí původ názvu u D. R. McMillana. Jde o jiný
  objekt než kvazigrupu. Doplnění v našem druhém dotisku ještě není.
- **E039**, oficiální upřesnění19.9.2021: v zadání76 se „an identity
  element“ mění na „the identity element0“. Náš4B je již obsahuje;
  starší autorůvPS ještě ne. Neopravuje izolovanou diagonálu v odpovědi.

Pro příběh o Knuthově výuce na Caltechu1968 je zdrojem jeho vlastní
svědectví v knize. Nejde o nezávisle ověřenou archivní událost.

## Errata a přesný rozsah

`check_gropes_errata.py` prohledal všech šest relevantních úplných
textových vrstev a zaznamenal33 kontextů. Čtyři aktuální originály
`all4b.ps.gz`, `all4f5.ps.gz`, `err4b.textxt`, `err4f5.textxt` byly
staženy z autorova webu a jejich SHA256 se shodují s archivem.
[Protokol](results/gropes75/errata-check.json) uvádí čas i hashe.
Nesouvisející čísla stran/úloh byla odlišena podle sekce. F121/F122
nejsou E038/E039. Historický PS má oba nové nálezy ve stejném znění.

Další dostupné matematické kontroly tohoto bloku jsou hotové. Zbývají
dva přesně pojmenované původní články; hotové výčty není třeba opakovat.
Po získání článků lze uzavřít příslušné bibliografické mezery. Celá strana132
zahrnuje také74 a77–83, strana432 také73–74; dokončení75–76 by samo
o sobě neznamenalo úplné dokončení těchto stran.
