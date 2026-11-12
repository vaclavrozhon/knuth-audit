# §2.3.4.3: obecné důkazy a přesný rozsah kontroly

Pracujeme s orientovaným stromem zakořeněným v jednom vrcholu; každá hrana
směřuje od dítěte k rodiči a každý vrchol má konečnou cestu ke kořeni.
„Větev“ níže znamená nekonečnou posloupnost po sobě jdoucích dětí,
nikoli konečnou cestu orientovanou opačně. Kniha používá obrat
„infinite path to the root“ a ihned jej přesně definuje.

Původní obrazy `images/p382.png` až `p386.png` a `p586.png` až
`p588.png` byly prohlédnuty. OCR je pouze navigace. Osm původních
úloh zůstává osmi; pozdější doplnění se týkají odpovědí 4 a 5.

## Věta K a její kontrapozice

Kořen má nekonečně mnoho potomků, protože jimi je celý nekonečný
strom. Má-li vybraný vrchol nekonečně mnoho potomků a konečně mnoho
dětí, některé dítě musí mít nekonečně mnoho potomků: konečné sjednocení
konečných množin spolu s vrcholem by bylo konečné. Takové dítě lze
vybrat a postup opakovat. Každý krok zvýší hloubku o jednu, takže
vrcholy jsou různé a dostáváme požadovanou větev. Není potřeba jednotná
horní mez stupňů. Jde o obvyklou klasickou matematiku; kniha netvrdí
efektivní algoritmus pro rozhodnutí, které dítě má nekonečné pokračování.

U algoritmu jsou vrcholy skutečná volání s konečným počtem potomků,
včetně příslušné konečné lokální práce. Nekonečně mnoho volání by
podle K dalo nekonečnou větev. Pokud každá větev skončí, počet volání
je konečný a skončí i celý výpočet. Nekonečná lokální smyčka by sama
porušovala předpoklad o skončení příslušné větve.

Každá úroveň stromu je konečná indukcí z konečného větvení. Příklad
stromu s kořenem a nekonečně mnoha konečnými rameny délek 1,2,3,...
ukazuje nezbytnost konečného stupně. Souvislost s důkazem
Bolzanovy–Weierstrassovy věty je skutečná: půlení omezeného intervalu
vždy ponechá podinterval s nekonečně mnoha body; vnořené intervaly
mají společný hromadný bod. Historickou podobu u Königa ověřuje
originál z roku 1927, s. 121–125.

Watsonova známá chybná závěrečná úvaha je skutečně v primárním článku,
s. 143. Pro jeho příklad je pravděpodobnost vyhynutí po n generacích
iterací `x_(n+1)=f(x_n)`, `x_0=0`, kde `f(x)=(3+x)^5/4^5`.
Funkce je na [0,1] rostoucí a
`f(3/4)=(15/16)^5=759375/1048576 < 3/4`.
Proto všechny iterace zůstávají nejvýše 3/4; nemohou konvergovat k 1,
jak článek tvrdí. Tento výpočet ověřuje Knuthovu poznámku o původním
omylu; není to nová chyba v TAOCP. Přesný rok vydání příslušné části
časopisu zůstává bibliografickou mezí popsanou v SOURCES.md.

## Posloupnosti a úloha 1

V původním obrazu s. 383 je délka `n >= 0` a v podmínce (i)
`0 <= k <= n`, nikoli OCR `> 0`. Pro neprázdné S proto obsahuje S
prázdnou posloupnost. Ta je kořenem, rodičem neprázdné posloupnosti
je její prefix o jeden člen kratší. Jednoznačnost rodiče, souvislost
a nepřítomnost cyklů plynou z klesající délky. Podmínka (ii) dává
konečný počet dětí, (iii) vylučuje větev, a K proto dává konečnost S.
Je-li S prázdná, závěr je triviální; slovní identifikaci se stromem
čteme v neprázdném případě. Nejde o novou věcnou chybu.

## Dlaždice v hlavním textu

Dlaždice má čtyři barevné strany. Pořadí složek ve všech našich
souborech je `(N,S,W,E)` = sever, jih, západ, východ. Sousední strany
musí mít přesně stejnou barvu, rotace a zrcadlení nejsou dovoleny.
Nekonečnou rovinu modelujeme mřížkou `Z x Z`.

Šest typů z (2) má vodorovné přechody
`3 -> 1 -> 2 -> 3` nebo `13 -> 11 -> 12 -> 13`.
Každý typ jednoznačně určuje souseda vpravo i vlevo. Svislé barvy
pak vynutí střídání horního a dolního řádku obdélníka (3), se stejnou
vodorovnou fází. Dostáváme právě vyobrazený vzor 3 x 2 až na posun.
Přímý validator ověřuje i oba švy toru, tedy replikaci do celé roviny.

U tří typů (4) musí každý řádek cyklit `0,1,2`, kde typy bereme
zleva v obrázku. Jejich severní slova v jednom období jsou `1,1,2`,
jižní `2,1,2`. Žádné cyklické posunutí prvního slova se nerovná
druhému (mají i různé počty dvojek). Dva celé sousední řádky tedy
nelze spojit. Konkrétně neexistuje ani obdélník šířky 3 a výšky 2;
menší 2 x 2 obdélník ještě existuje. Kontrola neztotožňuje tato dvě
různá tvrzení.

Je-li konečnou sadou vydlážděn kvadrant, existují čtverce libovolné
velikosti. Uvažujme čtverce souřadnic `[-n,n-1]^2`, s rodičem
daným odstraněním vnějšího rámu. Kořen je jediný prázdný čtverec.
Každý rám má konečně mnoho buněk a každá buňka konečně mnoho typů,
takže strom je konečně větvící. Má uzel v každé hloubce. Větev z K
určuje souhlasná dláždění všech čtverců; jejich sjednocení pokrývá
rovinu a každá sousední dvojice se ověří již v konečném čtverci.

## Úloha 2: povolené rotace

Pro libovolný dostupný typ `t=(a,b,c,d)` je otočení o 180 stupňů
`t'=(b,a,d,c)`. Šachovnicový vzor `t,t'; t',t` souhlasí na všech
vnitřních stranách i na obou švech opakovaného 2 x 2 obdélníka.
Předpoklad dostupnosti alespoň jedné dlaždice je obvyklý implicitní
kontext úlohy („take one tetrad type“ v odpovědi). Prázdná sada
pochopitelně netvoří dláždění; nevedeme to jako nový nález.

## Úloha 3: nekonečná sada

Typ `t_j=(1,1,j,j+1)` existuje pro každý kladný celý j. Pravou
polorovinu lze dláždit tak, že v každém řádku vybereme libovolné
počáteční kladné j a doprava je zvyšujeme o jedna. Řádky jsou nezávislé,
protože svislé barvy jsou 1. Již dvě možnosti začátku každého řádku
dávají nespočetně mnoho dláždění. Celá rovina není možná: vlevo od
typu j musí být postupně j-1,j-2,..., a typ s indexem 0 neexistuje.
Konečnost sady je tedy pro argument v hlavním textu podstatná.

## Úloha 4: podmíněný rozhodovací algoritmus

Pro n=1,2,... úplně vypíšeme všechna dláždění n x n. Není-li žádné,
odpovíme ne. Je-li některé platné i při ztotožnění protějších stran,
odpovíme ano. Každá fáze je konečná. Jestliže rovinu nelze dláždit,
nějaký konečný čtverec nelze dláždit podle kontrapozice K. Jestliže
existuje toroidální obdélník šířky w a výšky h, lze jej opakováním
rozšířit na toroidální čtverec strany násobku w i h. Za předpokladu
zadání algoritmus proto skončí v obou případech. Bez nepravdivého
předpokladu může běžet navždy; není to obecný rozhodovač problému.

`tiles.py:decide_under_periodicity_assumption` implementuje tento
algoritmus skutečně, v Pythonu. Úloha nevyžaduje MIX. Konečný generátor
`rectangles` vybírá typy v řádkovém pořadí, kontroluje již známého
severního a západního souseda a volitelně švy. Každé platné pole má
jedinou takovou posloupnost voleb; žádná neplatná větev nemůže přidáním
pozdějších typů opravit starou chybu. To dokazuje úplnost výpisu.
Pro šest typů vrátí ano při n=6; pro tři typy ne při n=3.

### Doplněk z roku 2005: kvaziperiodické dláždění

„Kvazitoroidální“ zde znamená, že každý v dláždění přítomný n x n
vzor se objeví v každém čtverci strany f(n), pro nějakou konečnou f(n).
Množina X všech dláždění konečnou sadou je kompaktní: z libovolné
posloupnosti lze postupně vybrat podposloupnosti shodující se na
čtvercích 1,2,... a vzít diagonální limit. Je uzavřená a invariantní
vůči celočíselným posunům.

Vypišme všechny konečné vzory P_1,P_2,... . Z neprázdné X postupně
odstraňme všechny posuny vzoru P_i, kdykoli tím zůstane neprázdná
uzavřená invariantní podmnožina. Vnořené kompaktní neprázdné množiny
mají neprázdný průnik Y. Ten neobsahuje žádnou vlastní neprázdnou
uzavřenou invariantní podmnožinu: taková podmnožina by vynechala
nějaký konečný vzor přítomný v Y, ale tento vzor by byl odstraněn již
v příslušné fázi konstrukce.

Pokud by vzor P přítomný v Y chyběl v libovolně velkých čtvercích
některého prvku Y, posuňme tyto čtverce do středu a vezměme limit.
Vznikne prvek Y bez P kdekoli, takže neprázdná uzavřená invariantní
podmnožina vyhýbající se P je vlastní, spor. Pro každý P tedy existuje
konečná mez. Maximum mezí přes konečně mnoho n x n vzorů je f(n).
To je obecný důkaz tvrzení doplňku; nedává efektivní výpočet f.
Durandův publikovaný abstrakt potvrzuje přesně tuto větu. Plný originál
článku zatím nezískán; bibliografický status je uveden zvlášť.

## Úloha 5: všech 92 typů

Písmena A,B,C,D v kódu znamenají řecké alfa,beta,gama,delta pouze
na první pozici názvu; velká písmena dále v názvu jsou původní značky
ze zadání. Prázdný kód B z prvního tisku byl v roce 2017 přejmenován
na epsilon; v kódu jej vynecháváme. Skládání kódů je po složkách
a pořadí znaků v každé složce se třídí. Přesný přepis dává 4,21,22,45
různých typů podle tříd, celkem 92, bez duplicit barevných čtveřic.

### Pravidelná mřížka

Číselná vrstva vynutí uspořádání

```text
A B A B ...
C D C D ...
A B A B ...
```

jednoznačně až na posun. Dlaždice třídy A mají druhy a,b,c,d.
Na této řidší mřížce vynucují vodorovné značky přechody
`a <-> b` a `c <-> d`: mezi a a b musí být K, mezi b a a vodorovné
P, mezi c a d S a mezi d a c T. Svisle a musí přejít do c přes J
a c do a přes Q. Svislá volba v sousedním sloupci je pak určena
vodorovnou vazbou. Proto i druhy A tvoří pravidelnou mřížku
`a b / c d` až na posun.

### Konečné lokální lemma

Rozdělme rovinu na překrývající se čtverce 3 x 3 s vrcholy třídy A;
sousední čtverce sdílejí celý krajní sloupec nebo řádek. Podle
druhu levého horního A je řada rohových druhů plně určena:

| levý horní | pravý horní | levý dolní | pravý dolní | počet všech lokálních výplní |
|---|---|---|---|---|
| a | b | c | d | 4 |
| b | a | d | c | 28 |
| c | d | a | b | 27 |
| d | c | b | a | 45 |

Z celkem 104 výplní je 12 nemožných v celé rovině. U rohu b jsou
to středy `DNb,DNc,DNd,DL,DLU,DLD,DLQ`: nemají žádného souseda
vlevo. U rohu c jsou to `DLU,DPU,DRU,DSU,DTU`: nemají žádného
souseda nahoře. Toto je lokální konečný rozbor, nikoli empirický
předpoklad o velkých polích. Úplný seznam výplní je `results/blocks3.json`;
počet sousedů každé vyloučené výplně je v `results/tiles-check.json`.

Zbývá přesně 92 bloků. Z každého uděláme jednu hrubou dlaždici:
rohové druhy a,b,c,d dají hrubé třídy A,B,C,D; ze středu ponecháme
všechny písmenné kódy, pouze u hrubé A odstraníme N. Výsledek je
právě původní seznam 92 barevných čtveřic, každá právě jednou.
Pořadí složených kódů není významové: např. PU a UP znamenají totéž.
Zápis `results/substitution-blocks.json` udává pro každý hrubý typ
jeho jediný 3 x 3 blok.

Dva bloky mají stejný společný kraj právě tehdy, když hrubé dlaždice
mají stejnou příslušnou barvu. Tuto poslední konečnou identitu lze
ověřit přímým dosazením všech kódů; `check_tiles.py` provádí všech
`2 * 92^2 = 16928` porovnání vodorovných a svislých dvojic.
Spolu s úplným generátorem a explicitní tabulkou to je reprodukovatelný
důkaz konečného lokálního lemmatu. Nepředpokládáme, že konečně mnoho
náhodných velkých dláždění dokazuje nekonečnou větu.

### Existence pro libovolnou velikost

Každý platný konečný obdélník lze nahradit bloky z tabulky, přičemž
sousedé sdílejí kraj. Lokální lemma zaručuje shodu celého překryvu;
čtyřnásobný průnik je roh, na němž shoda plyne již z dvojic.
Ze čtverce strany m vzniká čtverec strany 2m+1. Začneme jedinou
dlaždicí a opakováním dostaneme strany `1,3,7,15,...`. Konečnost
sady a věta K nyní dávají dláždění celé roviny. Žádný krok nepředpokládá,
že vybraný původní čtverec má pokračování do roviny.

### Vyloučení period

Naopak každé dláždění roviny má uvedenou mřížku a lze je zmenšit
pomocí lokálního lemmatu na jiné dláždění stejnými 92 typy. Jakýkoli
vektor celočíselné periody `(u,v)` musí podle číselné vrstvy mít obě
složky sudé. Po zmenšení je `(u/2,v/2)` periodou hrubého dláždění.
Postup opakujeme libovolně mnohokrát; obě celá čísla jsou proto
dělitelná každou mocninou dvou a musejí být nulová. Neexistuje tedy
ani jediná nenulová translační perioda, tím spíše toroidální řešení.

### Doplněk z roku 2019: šest typů lze vynechat

Uzávěr typu Aa pod uvedenou substitucí obsahuje přesně 86 typů;
chybí `BUS, DLD, DLU, DRD, DRU, DSU`. Jinými slovy, tabulka pro
kterýkoli z těchto 86 typů používá pouze těchto 86. Stejný obecný
argument růstu čtverců a K proto dává dláždění i bez šesti vypsaných
typů. Neperiodičnost podmnožiny plyne z neperiodičnosti celé sady.
To přímo dokazuje formulaci „can actually be omitted“; netvrdíme
z této kontroly, že se těch šest typů nemůže vyskytovat v žádném
jiném dláždění původní sady.

### Obrázek a doplněk z roku 2023

Původní 7 x 7 tabulka obsahuje známý překlep `gamma ST`, opravený
22. 7. 2005 na `gamma SJ`. V roce 2017 se celá tabulka přepsala;
nové pořadí znaků a vypuštění prázdného B jsou významově stejné.
Přímé porovnání všech 84 vnitřních společných stran opraveného
obrázku prošlo. Substituce dává vedle obecného důkazu i ověřené
čtverce 31 x 31 ze všech 92 počátečních typů a jeden 255 x 255.

Doplnění o jedenácti typech a čtyřech barvách přesně odpovídá
hlavnímu výsledku Jeandela–Raa. Získali jsme celý článek v publikované
sazbě a přečetli příslušné pasáže: znění, definici periodicity a popis výpočetní části.
Nereplikovali jsme jejich úplnou klasifikaci všech sad nejvýše deseti
typů; jde o kontrolu citovaného primárního výsledku, nikoli nový
nezávislý důkaz tohoto vnějšího výsledku. Zvlášť evidujeme podezření
na chybný koncový údaj citace 1:39 namísto 1:37.

## Úloha 6: konečná van der Waerdenova věta

Překrývající se pokrytí k množinami převedeme na obarvení: každému
číslu přiřadíme nejmenší index množiny, která jej obsahuje. Jednobarevná
aritmetická posloupnost pak leží v odpovídající původní množině.
Stačí tedy rozklady na očíslované barevné třídy, z nichž některé
mohou být prázdné.

Pro pevná kladná k,m sestrojíme strom všech k-obarvení počátků
`{1,...,n}`, která nemají jednobarevnou aritmetickou posloupnost délky m.
Rodič vynechá poslední číslo, kořen je prázdné obarvení a počet dětí
je nejvýše k. Nekonečná větev by dala obarvení všech kladných čísel
bez takové posloupnosti, v rozporu s předpokládanou nekonečnou větou.
K tedy říká, že strom je konečný; zvolíme N větší než jeho největší
hloubka. To dokazuje tvrzení pro všechna k,m včetně k=1 a m=1.

Příklad `W(2,3)=9` ověřujeme úplným výpisem všech 2^n obarvení
pro n<=9. Pro n=8 je šest přípustných obarvení, např. 00110011;
pro n=9 žádné. Test pro každou diferenci d>0 a počátek a kontroluje
všechny tři členy a,a+d,a+2d v rozsahu.

Primární článek z roku 1927 byl přečten celý (s. 212–216); už jeho
úvod uvádí konečnou podobu věty. Vlastní van der Waerdenovo vzpomínání
z roku 1954 na s. 49–50 potvrzuje diskusi s Artinem a Schreierem
v roce 1926, Schreierovu otázku po konečné mezi a diagonální argument.
Na s. 53 autor sám odkazuje na rok 1927. Tím je atribuce úlohy
podložena primárním svědectvím; přesné stránky anglického přetisku
z roku 1971 jsme přímo neprohlédli.

## Úloha 7: nekonečná aritmetická posloupnost

Tvrzení neplatí. Obarvěme kladná čísla podle parity `floor(log2 n)`.
Každá barva má po sobě jdoucí bloky rostoucí bez omezení. Pro libovolnou
nekonečnou aritmetickou posloupnost s diferencí d>0 leží v každém
dostatečně pozdním bloku délky alespoň d nějaký její člen. Posloupnost
proto potká obě barvy. To je explicitní počitatelný protipříklad.

Silnější poznámka odpovědi o dvou množinách bez nekonečné počitatelné
podmnožiny je rovněž správná v obvyklém smyslu nekonečné posloupnosti
různých prvků. Vypišme všechny nekonečné počitatelně vyčíslitelné
množiny (samotný tento výpis nemusí být efektivní). Z každé vybereme
dva dosud nepoužité prvky a dáme je do různých barev; ostatní prvky
obarvíme libovolně. Každá nekonečná vyčíslitelná množina protne obě
barvy. Kniha nepožaduje efektivní konstrukci této silnější dvojice.
Triviální nekonečné opakování jednoho čísla není zamýšlenou
„infinite sequence“ v tomto tvrzení; nejde o nález.

## Úloha 8: Kruskalův argument

Vložení T do U je injekce uzlů zachovávající jejich relativní pořadí
v preorderu i postorderu podle §2.3.2-22. Je reflexivní a tranzitivní.
Pro nesingulární strom T znamená l(T) jeho první kořenový podstrom
a r(T) strom vzniklý odstraněním tohoto podstromu. Oba mají méně
uzlů než T a oba se vkládají do T. Již prokázané lepení říká:
`l(T) <= l(U)` a `r(T) <= r(U)` implikuje `T <= U`.

Špatná posloupnost je nekonečná posloupnost stromů bez dvojice
i<j s `T_i <= T_j`. Předpokládejme její existenci. Volme postupně
T_1,T_2,... tak, aby každý člen měl nejméně uzlů mezi všemi možnostmi,
které ještě připouštějí nekonečné špatné pokračování dosavadního
prefixu. Minimum existuje v přirozených číslech; lze stanovit i
pevné pořadí konečně mnoha stejně velkých tvarů. Každý konečný
prefix zůstává špatný, takže špatná je i výsledná posloupnost.
Žádný člen není jediný kořen, který se vkládá do každého pozdějšího.

Posloupnost `l(T_i)` nemá špatnou podposloupnost s indexy
n_1<n_2<... . Jinak by `T_1,...,T_(n_1-1), l(T_n1), l(T_n2),...`
byla špatná: dvojice uvnitř prefixu a uvnitř konce jsou vyloučeny;
vložení staršího T_j do některého l(T_ni) by tranzitivitou dalo
zakázané vložení do T_ni. První změněný člen má méně uzlů, spor
s jeho minimálností.

Z toho odvodíme nekonečný řetězec `l(T_n1) <= l(T_n2) <= ...`.
Jen konečně mnoho indexů j nemá žádný větší k s `l(T_j)<=l(T_k)`:
nekonečně mnoho takových indexů by samo tvořilo špatnou
podposloupnost. Za posledním výjimečným indexem tedy začneme a
rekurzivně vybíráme většího následníka. Tranzitivita zajistí všechny
porovnatelnosti v řetězci.

Pro j<k nyní nemůže platit `r(T_nj)<=r(T_nk)`, protože lepení
by dalo `T_nj<=T_nk`. Stejně jako výše je proto
`T_1,...,T_(n_1-1),r(T_n1),r(T_n2),...` špatná, ale její první
změněný člen je menší. Druhý spor dokončuje důkaz. Věta K zde
není použita jako přímá implikace a odpověď to výslovně upozorňuje.

Doplňková věta o n-ticích nezáporných čísel má také přímý důkaz:
z nekonečné posloupnosti přirozených čísel lze vybrat neklesající
podposloupnost (buď se nějaká hodnota opakuje nekonečně, nebo
hodnoty neomezeně rostou). Opakujme tento výběr po n souřadnicích.
Vznikne dvojice i<j porovnatelná po všech složkách. Platí tedy i
silnější sekvenční tvrzení než pouhá nepřítomnost nekonečného
antichainu, tedy množiny po dvojicích neporovnatelných prvků.
