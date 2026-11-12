# Úlohy 87–88: konkrétní sítě a úplné meze hloubky

Checkpoint X0110, P1032–P1039. Zadání p91/file108,
odpovědi p550–551/file567–568, detail obou sítí a
originál známého dodatku k 88 prohlédnuty.
Přebíráme přesné stromové štítky P0928 a celý důkaz
F v proof-078, zvláště invariant P1007. Žádný
matematický program ani enumerace nebyly spuštěny.

## Všechny relace stromu 63 — P1032

Ze štítků P0928 jsou jedničkové podpory sedmi sloupců

    S1={b,c,d,e,f,g,h}, S2={b}, S3={d,e,f,g,h},
    S4={e,f,g}, S5={f}, S6={g}, S7={h}.

Každé dvě jsou buď disjunktní, nebo je pro i<j
podpora Sj vlastní podmnožinou Si. V obou případech
se vyskytují právě tři z možných čtyř dvojic bitů:
00 dává a; neprázdné podpory a jejich příslušný
rozdíl dávají zbývající dva vzory. Proto vzniká
přesně jedna relace na každý z 21 párů sloupců.

Disjunktní dvojice jsou

    (2,3),(2,4),(2,5),(2,6),(2,7),
    (4,7),(5,6),(5,7),(6,7).

Vynucují i→¬j. Zbylých 12 párů je vnořených
(1,j) pro j=2,...,7, (3,j) pro j=4,...,7 a
(4,5),(4,6); vynucují j→i, tedy ¬i→¬j.
Tím jsou úplné všechny relace, ne pouze ty potřebné
pro některou menší reprezentaci stejného stromu.

## Pořadí a každé místo smyčky — P1033

Vytištěné pořadí je 7,6,5,4,3,2,1,¬1,¬2,...,¬7.
Pozice literálů jsou p(i)=8−i a p(¬i)=7+i;
komplementární pozice mají součet 15. Vnořená
relace j→i pro i<j jde vpřed. U disjunktních
podpor jdou obě relace z pozitivní do negativní
poloviny, tedy také vpřed. Pořadí je přípustné.

Pro vnořený pár i<j má vybraný oblouk smyčky
(d,k)=(j−i,8−j). Pro disjunktní pár se vybere
j→¬i s (d,k)=(i+j−1,8−j), ekvivalentní i→¬j.
Dosazení d v klesajícím, k v rostoucím pořadí dává
všech 21 následujících shluků.

| # | (d,k) | linie (i,j) | typ |
|---|---|---|---|
| 1 | (12,1) | (6,7) | D |
| 2 | (11,1) | (5,7) | D |
| 3 | (10,1) | (4,7) | D |
| 4 | (10,2) | (5,6) | D |
| 5 | (8,1) | (2,7) | D |
| 6 | (7,2) | (2,6) | D |
| 7 | (6,1) | (1,7) | N |
| 8 | (6,3) | (2,5) | D |
| 9 | (5,2) | (1,6) | N |
| 10 | (5,4) | (2,4) | D |
| 11 | (4,1) | (3,7) | N |
| 12 | (4,3) | (1,5) | N |
| 13 | (4,5) | (2,3) | D |
| 14 | (3,2) | (3,6) | N |
| 15 | (3,4) | (1,4) | N |
| 16 | (2,2) | (4,6) | N |
| 17 | (2,3) | (3,5) | N |
| 18 | (2,5) | (1,3) | N |
| 19 | (1,3) | (4,5) | N |
| 20 | (1,4) | (3,4) | N |
| 21 | (1,6) | (1,2) | N |

Pro d=9 se nepřidá nic. D znamená i→¬j, N znamená
¬i→¬j. To je přímá aplikace přesné smyčky F.

## Každý modul obrázku 87 a rušení invertorů — P1034

V detailu originálu souhlasí všech 21 svislých
spojení s tabulkou. U devíti D shluků jsou invertory
jen před a po spodním konci; u dvanácti N shluků
jsou před a po obou koncích. Každá trojice teček
je invertor, konec komparátoru, invertor. Obrázek
tedy obsahuje přesně 21 komparátorů a 9·2+12·4=66
invertorů, před zjednodušením celkem 87 modulů.

F zaručuje, že síť dává právě osm stromových štítků
a každý z nich ponechá. Není nutné znovu procházet
128 vstupů. Dva po sobě následující invertory na
téže linii bez mezilehlého modulu této linie lze
zrušit, protože ¬¬x=x. Moduly na jiných liniích
mezi nimi tuto identitu neovlivní. To je přesně
závěrečná poznámka odpovědi; netvrdí optimální
počet modulů zjednodušené sítě.

## Celá zhuštěná síť ze zadání 88 — P1035

Přebíráme pořadí 18 shluků sítě 74 z P1010. Každý
komparátor nebo invertor má jednotkové zpoždění.
Nejdřívější čas modulu je 1 plus maximum časů jeho
bezprostředních předchůdců na zúčastněných liniích.
To je dolní mez z datových závislostí a současně
dosažitelný rozvrh, indukcí v pořadí modulů.

Následující tabulka obsahuje každý modul. Značka
„—“ znamená, že shluk invertory nemá; jinak jsou
oba na spodní linii j.

| shluk # | linie | invertor před | komparátor | invertor po |
|---|---|---|---|---|
| 1 | 1,7 | — | 1 | — |
| 2 | 1,4 | 1 | 2 | 3 |
| 3 | 1,2 | 1 | 3 | 4 |
| 4 | 4,7 | — | 4 | — |
| 5 | 1,3 | — | 4 | — |
| 6 | 2,7 | — | 5 | — |
| 7 | 1,5 | — | 5 | — |
| 8 | 2,4 | 5 | 6 | 7 |
| 9 | 1,6 | 1 | 6 | 7 |
| 10 | 4,5 | — | 8 | — |
| 11 | 2,3 | — | 7 | — |
| 12 | 6,7 | — | 8 | — |
| 13 | 4,6 | — | 9 | — |
| 14 | 5,7 | — | 9 | — |
| 15 | 2,6 | — | 10 | — |
| 16 | 3,7 | — | 10 | — |
| 17 | 3,4 | 10 | 11 | 12 |
| 18 | 2,5 | 10 | 11 | 12 |

Každý z 18 komparátorů a 12 invertorů je přítomen
v původní zhuštěné kresbě v této časové úrovni;
nepatrné vodorovné odsazení současných svislých
spojů odlišuje křížení od spojení. Pořadí modulů
na každé linii se zachová. Konečné časy linií
jsou (6,11,11,12,12,10,10), takže hloubka je 12.

Také dolní mez 12 je konkrétní: závislost prochází
komparátory 1,2,3,5,7,9, následným invertorem 9,
komparátory 12,13, předchozím invertorem 17,
komparátorem 17 a jeho posledním invertorem.
Jde o 12 navazujících modulů. Celý obrázek i
tvrzení o nejdřívějším čase jsou tak doloženy.

## Proč konstrukce může mít kvadraticky mnoho modulů — P1036

Vezměme X={0^k1^(t−k):0≤k≤t}. Je uzavřené
na bitový medián, každá souřadnice má jednobitového
svědka a je to cesta na t+1 vrcholech. Pro každý
i<j chybí právě vzor 10, takže je relace i→j.
Konstrukce F zpracuje všech binom(t,2) párů a
přidá tolik komparátorů. To je Ω(t²) modulů.
Tvrzení je o této konstrukci, nikoli dolní mez
pro každou možnou síť reprezentující stejné X.

## Pevné d: všechny závislosti a tištěná mez — P1037

Uvažujme nejprve 2t formálních literálových pozic.
Všechny neorientované dvojice vzdálenosti d tvoří
disjunktní cesty podle zbytkových tříd modulo d.
Každá má nejvýše ceil(2t/d) vrcholů, tedy nejvýše
ceil(2t/d)−1 hran. Zrcadlení j↦2t+1−j posílá
každou takovou cestu na cestu a obrací její pořadí.

Fyzická linie je dvojice zrcadlových pozic. Pokud
zrcadlení prohodí dvě různé cesty, jejich ztotožnění
je jedna cesta. Pokud zachová cestu, ztotožní ji
podle obrácení pořadí; vznikne opět cesta, případně
s prostřední smyčkou. Tato smyčka by byla relace
mezi literálem a jeho doplňkem, která neexistuje
podle P0999. Po jejím odstranění máme cesty.
Skutečně přidané shluky jsou pouze podmnožinou
jejich hran a délku komponent nemohou zvýšit.

U pevného d se proto každý řetězec závislostí mezi
shluky pohybuje uvnitř komponenty s nejvýše
ceil(2t/d)−1 < 2 ceil(t/d) hranami. Jednotlivý
shluk má hloubku nejvýše 3: invertovat potřebné
linie souběžně, komparátor, souběžné zpětné inverze.
Celá fáze daného d má tudíž nejvýše 6 ceil(t/d)
jednotek hloubky, přesně mez tištěné odpovědi 88.

To platí i při zachování původního pořadí k:
na každé komponentě může být kritický řetězec
nejvýše tak dlouhý jako počet jejích shluků.
Nezávislé komponenty se mohou provádět souběžně.

## Celá původní asymptotika a případy t≤1 — P1038

Pro t≥2 sečtením přes d=1,...,2t−2 dostáváme

    hloubka ≤ 6 Σ ceil(t/d)
             ≤ 6t H_(2t−2)+6(2t−2) = O(t log t).

Stačí elementární H_m≤1+ln m. Jednotlivé fáze
provádíme postupně, což je platný rozvrh; dřívější
spouštění některých modulů může hloubku jen snížit.
Pro t=0 nebo t=1 nemá F žádnou relaci a síť má
nulovou hloubku. Asymptotický zápis pro rostoucí t
se tedy neopírá o logaritmus nuly či o neplatnou
zvláštní konstrukci.

## Celý známý dodatek: nejvýše 9 úrovní na d — P1039

Pro pevné d má každý fyzický vrchol stupeň nejvýše
2: vybereme-li jeho literálovou pozici j, může se
stýkat pouze s j−d a j+d. Hrany u jeho doplňku
jsou stejné dvojice modulo kontrapozici. Na jeden
pár proměnných připadá nejvýše jedna platná relace
podle P0998, takže nejsou další paralelní konflikty.

Obarvěme hrany tohoto grafu třemi barvami hladově.
Každá hrana má nejvýše dvě sousední hrany, a proto
je při jejím barvení aspoň jedna ze tří barev volná.
Každá barevná třída je matching a všechny její
shluky mohou proběhnout souběžně ve třech úrovních.
Tři barvy tedy dají nejvýše 9 úrovní pro dané d.

Změna pořadí shluků se stejným d je přípustná:
důkaz P1007 používá pro kritické tranzitivní
relace přísně větší rozdíl, a zachovává i už
provedené relace se stejným rozdílem. Může změnit
hodnotu f mimo X, ale stále zaručuje f(a)∈X
pro každý vstup a a f(a)=a pro a∈X.

Celková hloubka je nejvýše 9(2t−2)=O(t) pro
t≥2; menší případy jsou identita. Všechny fáze
lze vytvořit a obarvit v O(t²) práci a s O(t²)
výstupní pamětí, protože každá má O(t) incidencí
a jedna hrana zkoumá nejvýše dva sousedy. Výstupní
počet modulů zůstává O(t²); hloubka není počet
všech provedených operací.

## Errata a hranice checkpointu

Originál `all4a-pre.pdf`, p22, přidává 14. prosince
2013 k odpovědi 88 právě O(t) a ≤9 jednotek pro
stejné d, s atribucí Omidu Etesamimu. Celý jeho
matematický obsah je výše dokázán. Historickou
okolnost soukromého pozorování nepřezkoumáváme.
Jde o známý doplněk, nikoli nález.

Všech pět relevantních vrstev 4A/F0 errat bylo
prověřeno spolu s předchozím blokem. Celé 87 a 88,
všechny moduly obou obrázků, obě asymptotiky a
všechny dodatky jsou dokončeny. P550 zůstává
partial pouze kvůli P1025/P1026 v odpovědi 84;
p551 má dosud další neuzavřené odpovědi 90–92/95/96.
Žádný nový nález ani matematický běh. Další je
úloha 90; 89/93/94 se přebírají bez opakování.
