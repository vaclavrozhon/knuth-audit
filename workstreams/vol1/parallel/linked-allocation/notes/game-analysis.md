# §2.2.3-28: retrográdní analýza a vojenská hra

Stav matematické části: checked. Knižní zadání s.272–273 a odpověď
s.550 byly prohlédnuty v originále. Lucasovy citované s.105–116 a titul
svazku III byly přečteny v původním skenu; druhý odkaz, Winning Ways,
má ověřeno nakladatelské vydání a obsah, ne celé znění kapitoly 21.
Žádný nový nález.

## Obecný algoritmus a jeho důkaz

Stav zahrnuje postavení i hráče na tahu. Orientovaná hrana `x -> y`
znamená jeden legální tah a prohazuje hráče. `W` označuje stav, z nějž
hráč na tahu vynutí konečné vítězství; `L` stav, v němž proti správné
hře soupeře musí prohrát. Zbývající stavy umožňují neprohrát, ale
nevynucují konečné vítězství. Nekonečnou partii zde považujeme za remízu.
Konkrétní pravidlo o opakování je rozebráno zvlášť níže.

Počáteční koncové výsledky jsou pevné a již se nepřeznačují. Běžné
pravidlo „není legální tah, tedy prohra“ dává všem vrcholům s nulovým
výstupním stupněm značku L. Jiná hra může mít pevně dané koncové W či
remízy; koncovou remízu je nutné uchovat jako pevný výsledek nebo
reprezentovat remízovým cyklem. Vágne popsané kroky zadání chápeme jako
značkování dosud neoznačených neterminálních stavů, nikoli jako přepsání
již stanoveného výsledku. To je běžné doplnění algoritmu žádané úlohou.

Pro každý stav uložíme seznam předchůdců a čítač `c(x)` původně rovný
počtu následníků. Do fronty vložíme všechny počáteční W/L. Při vyjmutí
`y` z fronty projdeme dosud neoznačené předchůdce `x`:

* je-li `y` typu L, označíme `x` jako W a vložíme do fronty;
* je-li `y` typu W, snížíme `c(x)` o 1. Při nule označíme `x` jako L
  a vložíme do fronty.

Čítač neoznačeného stavu je počet jeho hran do stavů, jejichž značka W
ještě nebyla zpracována. Hranové násobnosti je třeba počítat shodně
v čítači i seznamu. Každý vrchol se zařadí nejvýše jednou a každá hrana
se zpracuje nejvýše jednou, tedy čas i prostor jsou `O(v+e)` pro `v`
stavů a `e` tahů.

Kromě značky přidělme celočíselný **rank**, tj. klesající horní mez počtu
tahů do výsledku. Terminály mají rank 0. Nové W dostane rank `1+rank(y)`
pro jednoho již známého následníka L; nové L dostane
`1+max rank(y)` přes všechny následníky, kteří už jsou W. Indukcí podle
okamžiku označení dokážeme správnost i vítěznou strategii: ve W zvolit
svědčící L s menším rankem, v L všechny odpovědi vedou do W s menším
rankem. Při správné hře vítěze tedy nelze pokračovat nekonečně.

Na konci neoznačený `x` nemá následníka L, jinak by byl W, a má aspoň
jednoho neoznačeného následníka, jinak by byl L. Volbou takového tahu
zůstane hráč v neoznačené oblasti; pokud soupeř opustí tuto oblast,
může přejít pouze do W pro následujícího hráče. Oba hráči tak mají
strategii neprohrát. To dokazuje úplnost značkování, nikoli jen jeho
bezespornost. Totéž platí s pevnými remízovými terminály, které se
považují za dovolený bezpečný cíl.

## Přesná varianta vojenské hry

Vrcholům desky říkáme `A,1,...,9,B`; symboly A/B pro krajní vrcholy
je nutné odlišit od jmen hráčů A/B. Deska má 11 vrcholů a 22
neorientovaných hran. Hráč A má tři nerozlišené figurky, hráč B jednu.
V zápisu `258-7:A` jsou figurky A na 2,5,8, figurka B na 7 a A je na
tahu. Jednotlivé řady desky mají výšky 0 (`A`), 1 (`1,2,3`),
2 (`4,5,6`), 3 (`7,8,9`), 4 (`B`). Hráč A přesouvá jednu figurku po
hraně na volné pole s neklesající výškou; hráč B smí po hraně libovolně.
Zachycení B znamená, že B nemá legální tah. Varianta použitá zde dovoluje
jen pohyb A dopředu a do stran.

Lucas s.110–111 uvádí v původním prospektu jednu možnost počátečního
zpětného tahu pro dosud nepohnutou figurku. Na s.116, poznámka III,
výslovně doporučuje tuto komplikaci vypustit: A vyhrává i bez ní.
Použitá varianta tedy přímo odpovídá citovanému zdroji. Počáteční
postavení je `A13-2:B`, B povinně táhne 2→5; analyzovaný běžný start je
`A13-5:A`. Krajní vrchol B není počáteční poloha samostatné figurky.

Počet rozestavení je `binom(11,3)*8=1320`, s hráčem na tahu 2640.
Kód `check_combinatorics.py` explicitně vypisuje všech 22 hran, generuje
všechny tahy a má dvě nezávislé implementace řešení: frontu předchůdců
a synchronní iteraci definujících pravidel. Obě se shodly na všech
2640 stavech a 10752 orientovaných tazích. Třetí kontrola certifikátu
ověřuje u každého stavu příslušné lokální rankové nerovnosti a u každé
remízy existenci remízového následníka i absenci následníka L.

```
W: 347 stavů; L: 155 stavů; neoznačeno: 2138 stavů.
Největší rank: 28.
A13-5:A je W s rankem 23.
```

Tyto počty platí pro úplný prostor rozestavení a výše uvedené konvence;
nejsou tvrzením, že všechny stavy nastanou při rozumné hře. Ze standardního
startu je při libovolných legálních tazích dosažitelných 2632 stavů.
Koncové B-stavy v dosažitelné části jsou právě knižní
`157-4:B`, `789-B:B`, `359-6:B`. Formální čtvrtá past `123-A:B` není ze
startu dosažitelná, což vysvětluje její nepřítomnost v odpovědi.
Existují také tři dosažitelné A-stavy bez tahu: `78B-9:A`, `79B-8:A`,
`89B-7:A`; obecné pravidlo nulového počtu následníků je správně označí L.

Rank 23 startu znamená vítězství nejvýše za 12 tahů A (a 11 odpovědí B).
To souhlasí s Lucasovým závěrem na s.116. Ověřujeme výsledek vlastní
úplnou analýzou; netvrdíme samostatnou formální verifikaci každé větve
Lucasovy kreslené tabulky na s.115.

## Knižní příklad opakování a jeho oprava

Ověřená posloupnost je

```
258-7:A  W, rank 11
158-7:B  L, rank 14
158-B:A  W, rank 13
258-B:B  L, rank 12
258-7:A  W, rank 11.
```

Všechny čtyři tahy jsou legální. Ve stavu `158-B:A` je tah 1→2,
vedoucí do `258-B:B`, **jediným** tahem do stavu L. Takže A může volbou
prvního tahu do L opravdu dopustit, aby B vynutil opakování; nestačí
vybírat libovolný vítězný stav bez ohledu na historii. Knižní příklad
i toto silnější tvrzení o vynucené odpovědi jsou správné.

Při konvenci „opakování celého stavu znamená výhru B“ se remízy
nehistorického modelu počítají jako výhry B. A v oblasti W však má
jednoduchou bezpečnou strategii: vždy vybrat L s menším rankem. Rank
klesá také při každé B-odpovědi a žádný celý stav se neopakuje.
Tím se obejde opakované řešení hry. Slovo „must“ v knižní radě je
v kontextu náhodného výběru mezi všemi vítěznými tahy; není nutnou
podmínkou každého možného správného programu.

Chceme-li zachovat volbu mezi mnoha tahy, lze postupovat podle knihy
s explicitními konvencemi: při posuzování dalšího tahu je každý stav,
který již alespoň jednou nastal, zakázaným návratem. Jeho opětovný
příchod je terminální výhrou B, tedy L při tahu A a W při tahu B.
Z těchto terminálů se již netahá. Aktuální stav se pro potřeby volby
tahu reprezentuje zvláštní kořenovou kopií s původními následníky;
návrat do jeho historické kopie je také zakázán. Je důležité nezapomenout
právě aktuální stav: jinak by se knižní cyklus stále mohl povolit.
Pro úplnou přesnost konkrétního pravidla opakování lze vždy připojit
historii ke stavu; konečný stavový prostor pak sice naroste, ale obecný
důkaz algoritmu platí beze změny.

Výsledky jsou v `results/combinatorics.json`, úplný lokálně ověřitelný
certifikát v `results/military-certificate.json`.
