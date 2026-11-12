# Úlohy 7.1.1–56/57: kvantifikace a lineární 2CNF

Checkpoint X0089, P0832–P0841. Zadání p87/file104 a odpověď
p545/file562 přečteny v původní sazbě proof-file104/562.png.
P0807–P0811 o grafu, SCC a jejich lineární konstrukci se přesně
přebírají. Žádný matematický program ani enumerace herních stavů.
Terminologická hranice slov „universal variable“ v(ii) je výslovná
samostatná P0840; vlastní algoritmus má níže jednoznačný literálový rozsah.

## Sémantika všech kvantifikátorů — P0832

Pro booleovskou x platí ∃x F=F(0)∨F(1), ∀x F=F(0)∧F(1).
Opakované existenční OR přes všechny souřadnice je1 právě tehdy,
když má F alespoň jeden splňující vstup. To je přesně SAT.
Smíšený prefix se vyhodnocuje v daném pořadí; existenční volba
může záviset na předchozích univerzálních hodnotách, nikoli na
pozdějších. Není dovoleno zaměňovat ∃ a∀ při jejich přesouvání.

## Celá formule56 a šest hran obrázku — P0833

Originál zadává

    F=(x∨y)(¬x∨z)(y∨¬z).

Při y=0 první klauzule vynutí x=1, druhá z=1 a třetí z=0,
spor. Při y=1 zůstává právě ¬x∨z. Proto

    F=y(¬x∨z).

Tři původní klauzule dávají přesně hrany

    ¬x→y, ¬y→x;
    x→z, ¬z→¬x;
    ¬y→¬z, z→y.

Jsou to dva řetězce ¬y→x→z→y a ¬y→¬z→¬x→y,
přesně jako v obrázku. Vrstvy ¬y; {x,¬z}; {z,¬x}; y
jsou topologické, takže každý ze šesti vrcholů je samostatná SCC.
To je celý graf, nikoli pouze absence jednoho nalezeného cyklu.

## Všech osm prefixů56 — P0834

Pořadí proměnných je x,y,z. Pokud je y univerzální, soupeř
vybere y=0 a F=0 pro všechny hodnoty x,z. Všechny čtyři
prefixy s prostředním∀ jsou tedy nepravdivé. Zbylé čtyři:

| prefix | hodnota | svědek / protistrategie |
|---|---|---|
|∃∃∃|1|x=0,y=1,z=0|
|∃∃∀|1|x=0,y=1 funguje pro obě z|
|∀∃∃|1|y=1,z=1 funguje pro obě x|
|∀∃∀|0|univerzální x=1,z=0 porazí každou volbu y|

Svědci respektují pořadí prefixu; nejsou dodatečně vybranými
hodnotami závislými na budoucím univerzálním tahu. Tabulka spolu
s předchozí čtveřicí přesně reprodukuje tři pravdivé a pět
nepravdivých možností odpovědi.

## Krychle kvantifikátorů a její částečné uspořádání — P0835

Pro každý booleovský podvýraz platí F(0)∧F(1)≤F(0)∨F(1).
Nahrazení jediného∃ za∀ tedy může hodnotu jen snížit. Všechny
vnější kvantifikátory jsou OR/AND, monotónní v argumentech,
takže toto pořadí zachovají. Osm prefixů jsou vrcholy3-krychle,
hrana mění jeden kvantifikátor. Pravdivostní množina je dolní
množina v pořadí, kde∀ je silnější požadavek než∃. Tvrzení
„more likely to be false“ je zde přesná monotónnost, nikoli
samostatný pravděpodobnostní experiment.

## Přesné podmínky57 a jejich nutnost — P0836

Každou proměnnou prefix kvantifikuje právě jednou. Literal l
nazveme univerzální, jestliže je jeho podkladová proměnná
kvantifikována∀; **patří sem obě polarity** x_i i¬x_i.
Dva různé literály zde mohou být i x_i a¬x_i stejné proměnné.
Cesty v následujících podmínkách mají tento přesný rozsah:

1. Žádná SCC neobsahuje literál a jeho komplement.
2. Neexistuje cesta mezi dvěma **různými univerzálními literály**.
   Cesta od literálu k sobě není zakázaná; cesta k jeho komplementu je.
3. Obsahuje-li SCC univerzální literál u a existenční literál v,
   pak kvantifikátor proměnné v leží v prefixu až za kvantifikátorem u.

První podmínka je nutná podle Theorem K: jinak je F nepravdivá
pro každé úplné přiřazení. Druhá je nutná, protože univerzální
hráč může nastavit počáteční literál na1 a koncový na0. Pro
různé proměnné to jsou dvě nezávislé volby; pro komplementární
literály to provede jediná volba. Žádné existenční hodnoty
nemohou splnit vynucenou implikaci mezi těmito konci.

Třetí je nutná, protože v SCC musí být v=u. Je-li existenční
v zvoleno dříve, může pozdější univerzální hráč nastavit u=¬v.
Jde o legální protistrategii závislou pouze na dříve viděném tahu.
Znaménka literálů pouze převádějí zvolené hodnoty proměnných.

## Konstruktivní dostatečnost všech podmínek — P0837

Označme U komponenty obsahující univerzální literál. Podle(1)/(2)
každá taková komponenta obsahuje právě jeden univerzální literál
 a komplementace ji páruje s komponentou komplementárního literálu.
Její existenční literály nastavíme rovny tomuto univerzálnímu literálu.
Podle(3) jde o závislost pouze na předchozí univerzální proměnné.
V komplementární komponentě je předpis konzistentně opačný.

Ostatní komponenty rozdělíme přesně podle dosažitelnosti:

* P: existuje z ní cesta do nějaké komponenty U;
* S: je dosažitelná z nějaké komponenty U;
* R: ani jedna z uvedených vlastností.

P a S jsou disjunktní. Jejich průnik by dával cestu U→C→U'.
Je-li U'=U, C by byla ve stejné SCC; jinak vznikne zakázaná
cesta mezi různými univerzálními literály. Obojí je spor.
Komplementace obrací cesty, a proto páruje P právě se S a R
s R. Nastavíme všechny literály v P na0 a v S na1.
To je konzistentní, neboť párové komponenty mají opačné hodnoty.

Zbývající indukovaný graf R je uzavřený na komplementaci a splňuje(1).
Theorem K, přesně P0808/P0811, mu dá konstantní booleovské hodnoty.
Zbývá ověřit všechny hranice, ne pouze vnitřek jednotlivých tříd:

* Do P nemůže vést hrana z R, S ani U: její počátek by sám
  dosáhl U, nebo by vytvořil zakázanou U→U' cestu.
* Ze S nemůže vést hrana do R, P ani U: její konec by byl
  dosažitelný z U, nebo by opět vznikl zakázaný vztah U→U'.
* Mezi U a R nejsou hrany, protože by R spadla do P nebo S.
* Mezi různými komponentami U nejsou hrany podle(2).

Zbylé mezitřídní hrany tedy mají tvar P=0→libovolná hodnota,
nebo libovolná hodnota→S=1, a jsou automaticky splněny.
Uvnitř každé U je jedna společná hodnota; uvnitř R splňuje
hrany Theorem K. Všechny implikace a tedy i všechny klauzule platí.

Existenční strategie tak používají jen konstanty nebo kopii/negaci
jediné předchozí univerzální proměnné. To dokazuje pravdivost
celého prefixu pro všechny univerzální tahy. Nezaměňujeme
existenci jednoho modelu s existencí správné kvantifikované strategie.

## Skutečně lineární testy a konstrukce — P0838

Graf má2n vrcholů a2m obloukových záznamů. P0810/P0811 dávají
SCC a jejich pořadí, ve kterém každý sink předchází svým předchůdcům.
Do polí zapíšeme ID komponenty, pořadí každé proměnné v prefixu
 a typ kvantifikátoru. Celkově O(n+m) čas a paměť.

Jedním průchodem přes členy komponent ověříme(1), spočítáme
univerzální literály v každé SCC a při dvou či více odmítneme.
U komponenty s jediným univerzálním literálem u porovnáme
pozici každého existenčního člena s pozicí u; tím ověříme(3).
Je nutné nejdřív zjistit u a pak porovnávat, dva průchody přes
členy jsou stále celkově O(n).

Pro podmínku(2) mezi různými SCC nepotřebujeme transitive closure.
Zpracujme SCC v pořadí výstupu a definujme příznak Rch(C), že
z C lze dosáhnout nějaké univerzální komponenty, včetně C samotné.
Pro všechny původní hrany C→D mezi různými komponentami už
hodnota Rch(D) existuje. Položme B(C)=OR jejich Rch(D).
Pokud je C univerzální a B(C)=1, odmítneme. Jinak

    Rch(C)=[C je univerzální] OR B(C).

Na každé hraně provedeme konstantní práci. Indukce v DAG dokazuje
přesnou dosažitelnost; odmítnutí proto nastává právě při zakázané
cestě mezi univerzálními komponentami. Smyčky uvnitř SCC ignorujeme;
paralelní hrany nevadí a není třeba je draze odstraňovat.

U neuniverzální C příznak Rch(C) přímo rozpozná třídu P.
Třídu S rozpozná Rch(¬C), protože komplement obrací cesty.
Zbytek je R. R může použít již získané pořadí SCC z celého grafu:
po omezení je stále obráceně topologické a porovnání C s¬C
podle P0811 dává požadované konstanty. Kopírovací předpisy
pro U vzniknou jedním průchodem přes členy.

Celé rozhodnutí a kompaktní předpis strategie tedy mají O(n+m)
čas i paměť, žádné kvadratické testování všech dvojic cest.
Příznak lze dopočítat i při emitování Tarjanovy SCC: její sousednosti
sice znovu projdeme, ale každý původní oblouk tak čteme jen
konstantněkrát a všechny jiné cílové SCC už jsou známé.

## Okrajové případy a význam prefixu — P0839

Bez univerzálních proměnných je U=P=S prázdné a algoritmus je
přesně Theorem K. Bez existenčních proměnných dovolí pouze
klauzule, jejichž hrany neimplikují jiný univerzální literál;
netautologická unit či binární klauzule je správně odmítnuta.
Například ∀x(x∨x) má hranu ¬x→x a porušuje(2), zatímco
∀x(x∨¬x) má pouze smyčky a je pravdivá.

Nepoužité proměnné mají izolované literalové komponenty a
nevytvářejí konflikt; existenční z nich mohou být konstantní.
Při n=m=0 je prázdná konjunkce pravdivá. Prázdná klauzule
není Kromova syntaxe; pokud ji vstup zvlášť dovolí, vrátíme
false ihned. Délka prefixu n je součást vstupu, takže lineární
mez neignoruje čtení nepoužitých, ale explicitně kvantifikovaných proměnných.

## Přesná terminologická mez původního(ii) — P0840, partial

Odpověď používá ve znění(ii) „universal variable x“ a „another
universal variable y or its complement“, zatímco její další důkaz
výslovně pracuje s „one universal literal“. Pro správný algoritmus
musí platit přesný literálový rozsah P0836, včetně obou polarit
 a cesty do komplementu téže proměnné. Pouhé označení pozitivních
vrcholů∀ není ekvivalentní test.

Konkrétně ∀x∀y(x∨y) je nepravdivá při x=y=0; graf má jen
¬x→y a¬y→x, všechny SCC jsou singletony. Test vycházející
pouze z pozitivních vrcholů x,y by žádnou zakázanou cestu nenašel.
Také předchozí úloha56 s jediným univerzálním y má cestu¬y→y,
nikoli cestu začínající pozitivním y. Nejde tedy o důkazovou
výjimku, kterou by bylo možné vynechat z implementace.

Intendovaný algoritmus a jeho dostatečnost jsou zde úplně dokázány.
Bez dalšího terminologického kontextu však nedeklarujeme doslovnou
formulaci(ii) za bezvýhradně ověřenou ani za nový confirmed/candidate
nález: „variable“ může být v této větě zkratka pro univerzální
literál. P0840 zaznamenává právě tuto zbývající interpretační mez,
ne nevyřešenou složitost kvantifikované2CNF.

## Externí hranice prvního řádu a bibliografie — P0841

Poslední dodatek57 srovnává booleovskou úlohu s prvním řádem.
Primární Cambridge záznam a autorský úvod potvrzují M. R. Krom,
Journal of Symbolic Logic35(1970),210–216, DOI10.2307/2270511:
rozhodování splnitelnosti obecných prenexových prvořádových formulí
s binárními disjunkcemi je nerozhodnutelné už pro uvedenou třídu
prefixu∀x∃y1…∃yk∀z bez rovnosti. Toto bereme jako přesný
externí vstup, nikoli jako nově zrekonstruovanou redukci tag systémů.

Zdroj: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/decision-problem-for-formulas-in-prenex-conjunctive-normal-form-with-binary-disjunctions/74F719604D13CB4C91F21C03E08242DA

Rozdíl v doméně je zásadní: tam se kvantifikuje přes objekty
libovolné struktury a atomy jsou predikáty parametrů; zde je každá
proměnná jediný booleovský bit. Neodvozujeme nerozhodnutelnost
pro konečnou předem danou booleovskou doménu. Obecné tvrzení
knihy tak má přesně odpovídající primární externí podklad.

Primární vydavatelská stránka Aspvall–Plass–Tarjan1979 vrátila403;
přesná kontrola celého článku se přeskočila. Vlastní úplný důkaz
booleovského algoritmu je výše a o tento nedostupný text se neopírá.
Errata all4a-pre/all4a/err4a/all4f0/err4f0 byla prohledána podle
57/56, p87/545, quantification/Aspvall/Krom/universal. Jediná
změna p545 je číslo odkazu u55; F0 odpověď57 na p191 je jiná sekce.
Žádná relevantní změna právě analyzovaného kritéria nebyla nalezena.

Celá56 je uzavřena, matematika algoritmu57 v přesné literálové
formulaci také. P0840 ponechává pouze uvedený výklad slov partial.
P87/p545 nejsou celé argument: pokračuje58 a další úlohy.
Dále58, main p65/file82, čtení218/file235 beze změny.
