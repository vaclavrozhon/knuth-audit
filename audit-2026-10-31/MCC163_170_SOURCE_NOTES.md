# DLX163–170: úplné znění, důkazy a krátká kontrola výpisu

Kontrola 3. listopadu 2026. Zadání na str. 145, odpovědi na str. 462–463;
autorský draft na str. 81 a 166–167. Odpověď 170 končí před číslem 171
na téže straně. Přímo přečteny také pravidla (69)–(72) a Algorithm M
na str. 96–98, odpovědi 12–13 na str. 418 a odkaz MPR125(c) na str. 25/391.
Tyto dílčí odkazy samy neznamenají kontrolu celých okolních stran.

Staré úplné kontroly grafů do čtyř vrcholů, prefixových konstrukcí i F071
se neopakovaly. Jejich soubory jsou svázané kontrolními součty v
[záznamu zdrojů](sources/mcc163_170/source-observations.json).

## 163: prázdný seznam

Je-li seznam položky i prázdný, jeho DLINK i ULINK ukazují na záhlaví i.
Aby M3 přesto pokračoval, musí být zbývající dolní mez nulová. M4 uloží
`x_l = FT[l] = i`. V M5 se nevolá tweak, protože `x_l = i`.
Při návratu proto (71) potřebuje rozpoznat, že FT ukazuje na záhlaví,
nikoli na datový uzel. Nastaví `p = a = i`, a tudíž `x = z = i`.
Cyklus proběhne nulakrát, k zůstane nula a délka seznamu se nezmění.
Větev pro `a <= N` je právě potřebná: TOP záhlaví obsahuje délku seznamu,
ne identifikátor položky.

Pro interval [0,1] navíc pracuje varianta untweak', která obnoví pokrytí;
pro [0,2] se pouze obnoví aktivita položky. Oba malé příklady jsou v novém
diagnostickém archivu. Znění odpovědi je správné.

## 164: null a původní pořadí větví

Datové uzly možností leží nad N; záhlaví v rozsahu 1..N značí null.
Proto se null nesmí předat původnímu hledání následujícího záporného
spaceru z odpovědi 13. Stačí jej vynechat jako možnost, případně vypsat
`null NAME(x)`. Ostatní uzly se převedou na původní čísla možností beze změny.

Podrobný dodatek používá dva různé mechanismy:

- `FT[j] = 0` znamená obyčejnou větev algoritmu C. Její položka je pokrytá
  a její seznam umožňuje původní výpis z odpovědi 12.
- Jinak FT uchovává první odstraňovaný uzel. Jeho řetěz DLINK vede přes
  již vyzkoušené možnosti k právě zvolenému x. Dříve odebrané uzly se
  do dalšího hledání neúčastní a jejich spojení před x se už nemění.
  Při null na konci vede řetěz až k záhlaví; u od začátku prázdného seznamu
  začíná rovnou na něm. Podmínky `x = FT[j]` a `x = TOP(FT[j])` pokrývají
  právě tyto dvě možnosti null.

Pořadí k tedy vznikne počítáním od FT, nikoli od současného DLINK záhlaví,
které už přeskočilo odstraněný prefix. Sentinel i=0 nemůže být platným
uzlem takové větve; při platném x se dojde k x. Jmenovatel musí být uložené
`SCORE[j] = theta_i` z M3, protože aktuální LEN už nepopisuje původní počet
větví. Jde o výpis skutečné cesty řešení, nikoli obecnou rutinu pro libovolnou
neplatnou adresu.

Nový [krátký program](check_mcc164_printing.py) přeložil nezměněný autorův
DLX3 a zkontroloval deset diagnostických úloh s nejvýše pěti možnostmi:
prázdné seznamy, pevné i intervalové násobnosti, null po neprázdném prefixu,
interakci primárních položek, konflikty a barvy. Pořadí větví počítá
nezávisle z časové posloupnosti návštěv; dodatečný tisk celé cesty porovnává
s touto dřívější posloupností. Každou množinu řešení navíc porovnává
s přímou definicí MCC na všech podmnožinách vstupních možností.

Všech **102 větví, 41 null větví a 162 zpětně vypsaných kroků 55 řešení**
souhlasí. Přímý oracle prošel dohromady jen **134 podmnožin**; nejdelší
nativní běh trval 0,0076 s při nice 15. Výsledky jsou v
[printing/accepted.json](results/mcc163_170/printing/accepted.json).
Toto je kontrola odpovídající autorovy implementace a obecný důkaz
doslovného pravidla knihy, nikoli nový úplný audit Algorithm M.

## 165: velikost stromu a logaritmická konkávnost

Při volbě p možností z p+d je na úrovni j vybrána rostoucí j-tice,
jejíž poslední člen smí být nejvýše d+j, aby ji bylo možné doplnit.
Proto počet uzlů na této úrovni je `a_j = binom(j+d,d)`.
Po dokončení první položky začíná u každého listu stejný strom druhé.
Oba vytištěné profily tedy přímo vyplývají z nezávislosti položek:

```
2 ze 4 nejdříve: 1, 3, 6, 18, 36, 60, 90, 126; součet 340.
5 ze 7 nejdříve: 1, 3, 6, 10, 15, 21, 63, 126; součet 245.
```

Pro d>0 poměr `a_(j+1)/a_j = (j+d+1)/(j+1)` přísně klesá.
Tím je přímo dokázaná silná logaritmická konkávnost všech kladných a_j.
Pro první skupinu nerovností stačí vynásobit r poměrů posunutých o p:
`a_(p+r)/a_p < a_r/a_0`, pro 1<=r<=q-p.
Pro druhou skupinu porovnáme p-r stejně dlouhých součinů:
`a_q/a_(q-p+r) < a_p/a_r`, pro 1<=r<p.
Jde přesně o všechny vytištěné nerovnosti; první p+1 úrovní a poslední
úroveň jsou stejné, prostřední úrovně jsou menší při pořadí q,p.
Kladné p odpovídá aktivním přesným násobnostem Algorithm M; nulovou
násobnost lze předem vyřešit triviálně.

Odkaz MPR125(c) skutečně uvádí porovnání poměrů. Jeho jiné podčásti zde
znovu neuzavíráme. **E083** je známá gramatická oprava z 2. 1. 2025:
`Would it better` má být `Would it be better`. V obou našich verzích chybí.

## 166: počet větví a rozhodování remíz

Před M4 označme délku L, horní zbývající mez B a SLACK S. Zbývající
povinný počet je r=max(B-S,0). Je-li r>0, první možnost může ležet nejvýše
na pozici L-r+1: za ní musí zbýt dalších r-1 možností. Je-li r=0,
máme všech L možností a navíc null. Při nedostatku možností je počet nula.
Všechny případy sjednocuje přesně formule

`theta = max(L+1-max(B-S,0),0)`.

Při S=0 a stejném theta mají obě položky stejné d=theta-1. Je-li theta>1,
platí důkaz z 165 a delší seznam má pro nezávislé položky menší strom.
Při theta=1 jsou obě varianty pouze řetězy a jsou stejně dlouhé; preferovat
delší seznam je nadále přípustné pravidlo remízy. Při theta=0 se backtrackuje.
Jde o motivaci heuristiky, nikoli záruku nejlepší volby pro každou dvojici
navzájem závislých položek.

Vytištěný průchod vybírá lexikografické minimum `(theta,SLACK,-LEN)`
a při úplné shodě zachová první položku. První konečná lambda je menší
než počáteční nekonečno, takže se i nastaví dřív, než je potřeba jeho SLACK.
**E084** je známá chybějící koncová hranatá závorka z 26. 11. 2024;
v PDF i draftu dosud chybí. Autorův CWEB před rozhodováním remíz ořezává
SLACK hodnotou BOUND; není proto doslovnou implementací každé remízy
vytištěného pseudokódu. V kořeni protipříkladu F071 se toto ořezání neuplatní.

## 167: potvrzené F071 a kratší ověření

Oba první příklady odpovědi jsou správné: [0,1] proti [0,2] u prázdného
seznamu mění místo deaktivace a přesná jednička proti [1,2] u jediné
možnosti mění tweakování a přidává úroveň s null. Pokrývají je také
nové krátké diagnostické běhy.

Při stejné posloupnosti vybraných možností zůstává rozdíl BOUND roven
delta a rozdíl SLACK také delta; jejich rozdíl BOUND-SLACK je invariantní.
To ale samo nezaručuje stejnou další položku, protože pravidlo 166 používá
i samotný SLACK. Závěrečná indukce a úplná ekvivalence proto neplatí.

F071 zůstává beze změny: možnosti `A X`, `A Y`, `B U`, `B V`, `B W`;
A má [1,4] nebo [1,5], B má [2,6]. Oba stupně větvení jsou 2. Při horní
mezi A=4 vyhraje její menší SLACK 3; při A=5 jsou oba SLACKy 4 a vyhraje
delší seznam B. Přitom obě horní meze A jsou alespoň M_A+2. Tento rozdíl
první volby sám stačí k vyvrácení úplné ekvivalence.

[verify_f071.py](verify_f071.py) tento argument ověří pouze aritmetikou
a počet 12 doloží součinem dvou binomických součtů. Nepouští prohledávání.
Staré nativní výsledky 37/35 uzlů a nezávislé profily zůstávají přijaté;
historické mems se nyní znovu neměřily. V šesti vrstvách errat odpovídající
oprava F071 nenalezena; prvenství tím netvrdíme.

## 168–170: obecné bijekce

**168.** U dvou kopií je druhá možnost s `+:1` slučitelná pouze s první
kopií `! alpha`, nikoli s prázdnou volbou `! +:0`. Z výběru 0, 1 nebo 2
kopií proto vždy vznikne právě jedno rozšíření. U tří kopií první dvojice
vynutí totéž pro první dvě; `++:0/1` současně vynutí, že třetí kopie
vyžaduje druhou. Pro každou násobnost 0..3 je právě jeden prefix.
Původní položky alpha a všechny ostatní možnosti si ponechávají původní
omezení; pomocné primární položky mají přesnou násobnost jedna.

**169.** Každá z n možností znamená vybrat právě svůj vrchol. Dva vybrané
sousední vrcholy jsou neslučitelné, protože pro tentýž sekundární prvek
požadují nebarvený výskyt a barvu 0. Vybrané nesousední vrcholy mohou
na společných sousedech sdílet 0 bez konfliktu. Primární # vynutí přesně
t vrcholů. Tím je dána bijekce, počet 1+n položek a n možností souhlasí.

**170.** Nová primární !v vybere jednu z d+1 možností pro v. První znamená
v zvolit: jeho hodnota je 1, sousedé 0 a přibude jedno #. Ostatní možnosti
dávají v hodnotu 0 a určují jeho prvního zvoleného souseda. Předchozí
sousedé mají 0, vybraný první má 1. Nezávislost tak plyne z první možnosti
a každému nezvolenému vrcholu je zaručen zvolený soused, tedy maximalita.
Obráceně má každá maximální nezávislá množina právě takové jednoznačné
rozšíření podle prvního zvoleného souseda v uvedeném pořadí. Izolovaný
vrchol má jedinou možnost, a musí tedy být zvolen.

Případ t=0 je triviální: pro 169 je jediným výsledkem prázdná množina,
pro 170 existuje jen u prázdného grafu. Protože doslovný vstup Algorithm M
na str. 97 vyžaduje nenulovou horní mez, lze tuto hranici vyřešit předem;
staré konečné testy používaly nucenou pomocnou možnost a posun násobnosti.
Tato implementační hranice nemění obecné kombinatorické konstrukce.

Starých **150 případů graf/varianta** a **7 případů počtu kopií** souhlasí
a nebyly opakovány. Nové obecné důkazy uzavírají rozsah mimo konečný test.

## Stav

Všech osm úloh 163–170 je **reviewed**, včetně dřívějšího F071 a známých
E083/E084. Celá odpovědní strana 462 je nyní zrevidovaná. Strany 145 a 463
zůstávají částečné kvůli dalším úlohám. Žádný nový velký výpočet, žádné
nové tvrzení o prvenství a žádný emailový návrh. Další blok je 171–174,
nejprve se přečtou jeho již přijaté výsledky a známé náhradní odpovědi.
