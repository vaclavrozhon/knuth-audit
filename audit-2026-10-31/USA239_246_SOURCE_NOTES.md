# USA a optimalizační převody 239–246

Kontrola 3. listopadu 2026, oba naše zdroje: 4B hlavní strany 114–116,
otázky 153, odpovědi 478–479; draft 5C strany 50–52, 89, 182–183.
Starší [USA_PARTITION_NOTES.md](USA_PARTITION_NOTES.md) a
[COST_REDUCTION_NOTES.md](COST_REDUCTION_NOTES.md) zůstávají platnou evidencí
svého tehdejšího omezeného rozsahu. Žádný jejich hotový cenzus nebo DLX běh
se neopakoval.

Nové potvrzené záznamy jsou [F148](F148_USA_POPULATION_SUMMARIES.md),
tři nepřesná populační shrnutí na straně 116, a
[F149](F149_USA_INTERNAL_DASHED_EDGES.md), čtyři chybně čárkované hrany.
Oba jsou drobné chyby prezentace. Starý protipříklad F078 k úloze 243
se zachovává, nepočítá se podruhé.

## Celý rozsah obrázků

Z původních vektorů se získalo **11 grafů na každou verzi**, celkem
530 vrcholů a 1159 hran na verzi. Všechny popisky, skupiny i styly hran
souhlasí mezi knihou a draftem. Všechna sousedství navíc přesně odpovídají
autorovu archivovanému `contiguous-usa.gb`: 105 hran u 48 států, s DC 107.
Plochy populačních kroužků odpovídají vahám s relativní odchylkou pod 0,05 %,
což pokrývá zaokrouhlení souřadnic kresby.

| Obrázek | Skupiny | Exterior cena | Interior cena |
|---|---:|---:|---:|
| (115), vlevo | 8 po 6 | 72 | 102 |
| (115), vpravo | 6 po 8 | 54 | 180 |
| (116), vlevo | 8 | 108 | 210 |
| (116), vpravo | 6 | 96 | 250 |
| 245(a) | 7 po 7, včetně DC | 58 | 138 |
| 245(b) | 7, včetně DC | 106 | 230 |
| 246, exterior vlevo / vpravo | 8 / 6 | 90 / 74 | 192 / 274 |
| 246, interior vlevo / vpravo | 8 / 6 | 98 / 80 | 176 / 230 |

Tabulka počítá skutečné hranice skupin v původním grafu, včetně opravy
čtyř stylů F149. U (115) výměna VA/WV a uvedený cyklus MI/NE/LA/VA dávají
druhá platná optima se stejnou cenou; jejich úplnost již dokládá přijatý
starší DP. Obrázek 245(a) přesně souhlasí se starším jediným optimem.

## Krátké nové počty možností

Nový generátor používá rozhodování zahrnout/vyloučit vrchol na hranici
souvislé množiny. Nejmenší vrchol je kořen, dříve odmítnuté vrcholy zůstávají
zakázané. Každá neprázdná souvislá množina tak má právě jednu větev;
kladné populační váhy dovolují zastavit větev při horní mezi.
Třicet úplných malých případů souhlasí s nezávislým výčtem všech podmnožin.
Všechny vypsané výsledky jsou různé; z každého velkého případu bylo
nezávisle ověřeno 250 deterministicky vybraných možností. Nejde o tvrzení,
že Python podruhé validoval každý vrchol všech velkých seznamů.

| Interval populace | Všechny souvislé možnosti | Po testu 242 | Čas hledání |
|---|---:|---:|---:|
| 48 států, [34 009 354, 43 726 312) | 1 926 811 | 355 754 | 1,58 s |
| 48 států, [37 000 000, 39 000 000) | 291 282 | 31 685 | 0,23 s |
| 48 států, [50 500 000, 51 500 000) | 1 587 884 | 36 190 | 0,57 s |
| 49 včetně DC, [43 000 000, 45 000 000] | 1 176 310 | 59 551 | 0,43 s |

První a poslední řádek přesně potvrzují knižní rozdíly
1 926 811−1 571 057 a 1 176 310−1 116 759. Každý nový běh měl limit 20 s
a nice 15. Všechny skončily úplně. Použité programy a výstupy jsou v
[population-runs.json](results/usa239_246/population-runs.json).

**C040, otevřený počet 34 111:** pro doslovný interval a test 242 vychází
31 685, bez redukce 291 282. Pouhé omezení již redukovaného širokého seznamu
dává 61 526. Samostatná nová kontrola dovolila v odříznuté komponentě také
jednu ze dvou později zavedených NY výjimek a dala 33 716 za 0,17 s.
Žádný z těchto přesně popsaných postupů nedává 34 111. Z veřejného seznamu
autorových programů nebyl získán původní populační generátor ani jeho
konkrétní vstup. Proto zatím kandidát, nikoli potvrzené erratum.
Všechny vytištěné běžné možnosti levých rozkladů se nacházejí v novém
seznamu s NY výjimkami; konkrétní svědci zůstávají platní.

## Populační argumenty a původ dat

P=306 084 180 přesně odpovídá autorovu GraphBase souboru. Meze pro přesně
osm skupin jsou správně floor(P/9)+1=34 009 354 a ceil(P/7)=43 726 312.
NY odděluje všech šest států Nové Anglie od zbytku grafu. Žádná skupina
z [37,39) milionů nemůže pokrýt NY: musí vzít celou Novou Anglii, dohromady
33 823 525, a další krok přes NJ nebo PA ji zvětší nad 39 milionů.
Tento krátký důkaz nepotřebuje úplný solver.

Po přidání obou NY možností má každý úplný rozklad stále osm částí:
jedna výjimka a šest běžných možností je příliš málo, výjimka a osm je
příliš mnoho. Podobně jsou pevné počty šest částí pro [50,5;51,5) a sedm
částí s DC pro [43;45]. Proto převod na součet čtverců funguje; celková
populace je konstantní a chyba sekundárních položek F078 zde nevzniká.
Populační rozsahy pravého (116) a 245(b) jsou správné. V levém (116)
jsou drobné numerické chyby F148.

**C039, otevřená atribuce:** oficiální původní sčítání 2010 dává pro
48 států 306 073 283. Sloupec Estimates Base ve vintage 2015 dává
306 085 788. SGB odpovídá u všech 49 použitých položek tomuto druhému
sloupci, s jedinou výjimkou CA: 37 252 895 místo 37 254 503, rozdíl −1608.
To vysvětluje celý rozdíl mezi SGB a tímto revidovaným základem.
Původ kalifornského údaje ještě není určen. Autor výslovně popisuje
GraphBase data jako zmrazené ilustrativní vstupy, které nejsou definitivním
zdrojem reálných faktů. Data se proto nepřepisují a jejich nesoulad se
sčítáním automaticky není chybou algoritmu. Kandidát se týká slova
„officially“ a označení zdroje v knižním textu.

Primární zdroje: [SGB](https://www-cs-faculty.stanford.edu/~knuth/sgb.html),
[původní Census 2010](https://www2.census.gov/programs-surveys/decennial/tables/2010/2010-apportionment/apport2010-table4.pdf),
[Census vintage 2015](https://www2.census.gov/programs-surveys/popest/tables/2010-2015/national/totals/PEPANNRES.pdf).
HTTP metadata a neměnné kopie jsou v `sources/usa239_246/`.

## Převody a otázky 239–244

239: primární položky jsou k a dvojice označené jk; písmeno j není další
samostatná položka. Pro množinu mimo zvolené pokrytí se použije její
svazková možnost s cenou wj. Prvky pokrytí mají párové možnosti; ostatní
kopie jsou slack položky. Hlavní cena je konstantní součet všech wj minus
cena pokrytí. Formální infinitesimály vybírají kanonické nejmenší j pro
každý prvek. Prázdné kladně oceněné množiny lze předem odstranit.
Obecný převod a příklad jsou správné. **Původní obsah Gondran–Minoux,
Graphs and Algorithms (1984), cvičení 10.35, nebyl získán**, proto úplná
zdrojová kontrola 239 zůstává částečná.

240–241: přijaty dřívější úplné šestice MT/TX i výstup DLX-PRE. Řetězec
(114) po předzpracování zůstává; LA AR TN VA MD PA je odstraněn. Cena řetězce
je exterior 19, interior 20, zbylé komponenty mají 11 a 31 vrcholů.

242: d lze vyjádřit součtem q celých čísel z [L,U), právě když
qL≤d≤q(U−1). Nejmenší možné q je ceil(d/(U−1)); podmínka odpovědi je tedy
nutná i postačující pro aritmetický rozklad velikosti. Nezaručuje sama
existenci grafového rozkladu. Dřívějších 36 000 kontrol přijato bez opakování.

243: F078 zůstává platný pro sekundární položky. Pro primární váhy nebo
konstantní celkovou váhu platí obecná algebra uvedená v odpovědi.

244: u stejných velikostí t oba cíle maximalizují počet vnitřních hran k:
interior n(t−1)−2k, exterior 2(m−k). Pro digraf je obdobně n(t−1)−k,
případně faktor 2 u obousměrně počítané vnější hranice. Zde jsou míněny
různé vrcholy, což potvrzuje příklad řetězce s interior cenou 20.
Rozklady 246 při různých velikostech konkrétně potvrzují odlišnost obou cílů.

## Errata a výslovně vynechané výpočty

E106 shrnuje již zveřejněné opravy odpovědi 239 z 26. a 28. listopadu 2019:
epsilon i→j, titul Algorithms v množném čísle a „additional cost 0+epsilon4“.
E107 je oprava belongs of→belongs to z 26. února 2022. Kniha je obsahuje,
draft má stará znění. Šest vrstev errat neuvádí odpovídající opravu nových
F148/F149 ani oba otevřené populační nesoulady.

Podle uživatelova pokynu **nebyla znovu hledána globální minima a násobnosti
populačních rozkladů (116), 245(b), 246**. Platnost, populace a ceny jejich
svědků jsou ověřeny; globální optimalita tím nezískala nezávislý důkaz.
Stejně se nereplikují historické náklady 807G, 3,2G, 327G, 1046M, <2G,
3,3G, 1,1G, 8G, 101M, 7,7G, 612M, 11M, 1700M a 100M memů.
Staré úplné nepopulační optimum zůstává přijaté. Otevřené C039/C040 a
chybějící původní citace 239 nejsou vyřešeny tímto povoleným vynecháním.

Všechny nové výpočty běžely s nice 15. Kontrola vlastních dlouhých úloh
znovu našla 9 kořenových úloh a 23 procesů, všechny již nice 15.
Žádná další dlouhá fronta nebyla spuštěna.

Další průchod: zbývající implementace C$ od dolní části strany 116,
úlohy 247–250. Hotové zdejší výpočty ani staré C$ testy se neopakují.
