# Souvislý průchod §2.3.4.3 — 5. listopadu 2026

X0975. Přímo přečteny originály 382–386 a 586–588 v hranicích oddílu,
všech osm zadání a odpovědí, definice všech 92 dlaždic a obrázky.
Přezkoušeny `parallel/infinity-lemma/PROOFS.md`, `tiles.py`, `check_tiles.py`,
pramenný inventář, errata a pozdější kořenová doplnění Dershowitze a
anglického van der Waerdena. Přijaté velké kontroly se neopakovaly.
Nový krátký výpočet se týká pouze rozsahu opravy diagonály z roku 2017.

## Nekonečný strom a dláždění

K: kořen má nekonečně mnoho potomků; konečný počet dětí vynutí dítě
s nekonečně mnoha potomky. Opakovaná volba dává větev. Každá úroveň
je konečná a každý vrchol má konečnou cestu do kořene. Není potřeba
jednotná mez stupňů ani algoritmicky rozhodovat nekonečnost podstromu.
Bez lokální konečnosti nestačí kořen s rameny délek 1, 2, 3, … .
Analogie s dělením omezeného intervalu v Bolzanově–Weierstrassově větě
souhlasí. Algoritmický důsledek předpokládá konečnou práci mezi větveními.

Ve formulaci pomocí prefixů jsou v originálu opravdu n≥0 a 0≤k≤n.
Neprázdná prefixově uzavřená množina obsahuje prázdnou posloupnost;
oblouk odstraní poslední prvek. Prázdná S je sama konečná a není
protipříkladem k tvrzení. Watsonův chybný závěr je vyvrácen již přijatou
nerovností f(3/4)=(15/16)^5<3/4 pro f(x)=(3+x)^5/4^5. Iterace z nuly
zůstávají pod 3/4, takže nemohou konvergovat k jedné. Originál článku
byl čten; datum jeho konkrétního sešitu zůstává bibliografickou výjimkou.

Šest dlaždic na 383 má v řádku vynucené cykly 3→1→2→3 nebo
13→11→12→13. Svislé značky vynutí střídání dvou řádků; zobrazený
obdélník 3×2 souhlasí i přes oba periodické švy. Tři dlaždice na 384
naopak vynutí vodorovný cyklus s horním řádkem barev 1,1,2 a dolním
2,1,2; žádný cyklický posun tyto řádky nesjednotí. Už 3×2 není možné.

Z dláždění kvadrantu získáme čtverce všech sudých velikostí. Jejich
vnořené rámy na souřadnicích [−n,n−1]² tvoří lokálně konečný strom
s prázdným kořenem a nekonečnou výškou. K dává kompatibilní sjednocení
na celé Z². Žádný posun o nekonečno se nepoužívá.

Úloha 2: t=(a,b,c,d) a otočená t'=(b,a,d,c) dávají šachovnici
t,t'/t',t, všechny švy souhlasí. Úloha 3: typy (1,1,j,j+1), j>0,
vyplní pravou polorovinu; nezávislé počáteční j každého řádku dávají
nespočetně mnoho řešení. Směrem doleva musí j klesat k nepovolené nule.

Úloha 4: pro n=1,2,… úplně projdeme konečně mnoho výplní čtverce.
Není-li žádná, odmítneme; je-li toroidální, přijmeme. Periodický
obdélník w×h lze opakovat do čtverce se stranou násobkem w i h.
Obě větve tedy skončí **pod uvedeným předpokladem periodicity**.
Pro obecné sady se ukončení netvrdí. Doplněk Durand 2005 má vlastní
důkaz: v kompaktním prostoru dláždění postupně zakazujeme všechny
posuny konečného vzoru, pokud zůstane neprázdný uzavřený invariantní
podprostor. Průnik je minimální. Vzor s libovolně velkými prázdnými
okolími by po posunu a limitě dal jeho vlastní neprázdný invariantní
podprostor, spor. Maximum mezí pro konečně mnoho n×n vzorů dává f(n).
Efektivní výpočet f ani četbu nedostupného celého Duranda netvrdíme.

## Všech 92 typů a přesný rozsah známých oprav

Kódy z 385 souhlasí s přepisem: třídy mají 4, 21, 22 a 45 různých
typů. Prázdný kód B je neutrální; jeho přejmenování na ε roku 2017
žádný typ nemění. Numerické značky vynutí mřížku αβ/γδ; na α pozicích
značky vynutí a,b/c,d. Přijatý úplný lokální rozbor má 104 bloků 3×3
s α rohy; 12 nemá levého nebo horního souseda. Zbývajících 92 bloků
je v bijekci s původními typy. Všech 16 928 směrových párových kontrol
ověřuje právě ekvivalenci shody sdílené řady/sloupce a makrobarvy.
Jde o konečné lemma obecného důkazu, nikoli náhradu důkazu velkou mřížkou.

Inflace s překryvem jedné řady a sloupce má velikost m→2m+1.
Dává libovolně velké čtverce, a proto podle K celou rovinu. V každém
dláždění je perioda (u,v) sudá díky numerickým třídám; deflace periodu
půlí. Nenulový celočíselný vektor nemůže být dělitelný všemi mocninami
dvou. Uzavřená substituční rodina z αa má 86 typů; chybí BUS, DLD,
DLU, DRD, DRU, DSU v kódu programu. To dokazuje možnost šesti typů
nepoužít, nikoli jejich nemožnost ve všech dlážděních původní sady.

Na 587 je v originálu skutečně γST místo γSJ. Je to neplatný typ
a známá oprava z 22.7.2005. Nová přesná kontrola navíc rozlišuje
význam změny z 12.8.2017: samotný střed δNa neurčuje celý blok 7×7.
Dvě inflace semen Aa a DNa dávají dva validní bloky se stejným středem,
ale diagonálami (Aa,DNa,Ad,DNa,Aa,DNd,Ad) a
(Aa,DNd,Ad,DNa,Aa,DNa,Ad). První je opravený knižní obrázek.
Druhá konstrukce se opakovanou inflací DNa rozšiřuje kolem svého
středu: prostřední dlaždice substituce DNa je znovu DNa. Má tedy
kompatibilní rozšíření do celé roviny. Nová podmínka celé diagonály
odstraňuje příliš široké původní určení na rozhraní 586–587.
Výsledek je v `results/sequential-infinity-diagonal.json`; běh nice 15
ověřil jen tyto dva malé bloky, nikoli znovu dřívější velké testy.

C0052 zůstává confirmed-low: doplněk z 31.1.2023 má u Jeandel–Rao
1:1–1:39, publikovaný článek má 37 stran a končí označením 37.
Jde výhradně o chybu doplňku errata. Na původní 587 tato citace není.
Věta o 11 typech a čtyřech barvách byla ověřena v publikovaném článku;
výpočetní klasifikaci menších sad znovu nespouštíme dle uživatelovy
výslovné výjimky pro drahé reprodukce.

## Konečná barvení a Kruskalova věta

6: z překrývajícího se pokrytí zvolíme nejnižší index barvy.
Konečná barvení bez monochromatické progrese délky m tvoří prefixový
strom s nejvýše k dětmi. Nekonečná větev by odporovala předpokládané
nekonečné van der Waerdenově větě, takže strom musí být konečný.
Tištěný výčet a+δ,…,a+mδ má přesně m členů. N=9 pro k=2,m=3
souhlasí s přijatou úplnou kontrolou: šest vyhovujících barvení délky
8, žádné délky 9. Krajní případy k=1 či m=1 argument neporušují.

7: parita floor(log2 n) dává střídavé intervaly neomezených délek.
Každá nekonečná aritmetická posloupnost s kladným krokem zasáhne obě
barvy. Silnější výrok z odpovědi: z každé nekonečné vyčíslitelné množiny
postupně vybereme dva dosud nepoužité prvky a dáme jim opačné barvy.
Výběr nemusí být efektivní; žádná barva pak neobsahuje nekonečnou
vyčíslitelnou podmnožinu. „Nekonečná posloupnost“ zde znamená nekonečně
mnoho různých prvků, nikoli opakování jedné konstanty.

8: v minimální špatné posloupnosti jsou l(T) i r(T) menší vlastní
části T; vložení je tranzitivní a dvě příslušná vložení lze spojit
podle §2.3.2–22. Špatná podposloupnost levých částí by po nahrazení
prvního příslušného T menší částí odporovala minimální volbě.
Indexů bez pozdějšího většího levého prvku proto může být jen konečně
mnoho; nad jejich maximem postupně volíme nekonečný rostoucí řetězec.
Pravé části na těchto indexech musí tvořit špatnou posloupnost,
jinak se vloží celé T. Opět nahradíme první T menší pravou částí
a dostaneme spor. V konečně mnoha souřadnicích n-tic opakovaný
výběr neklesající podposloupnosti dává také uvedený Dicksonův důsledek.

## Prameny, výjimky a stránková mapa

Zachovávám přesné rozsahy přímé četby v původním `SOURCES.md`:
König 1927/1932, Watsonův chybný krok, Wangův argument kvadrantu,
Robinsonovy relevantní strany, původní van der Waerden a Kruskal.
Pozdější `notes/dershowitz-original-root-review.md` uzavírá **celý**
Dershowitz 212–215; aplikace k ukončování je skutečně doložena.
`notes/waerden-english-reprint-root-review.md` uzavírá citovaný obsah
autorizovaným anglickým přetiskem 2009 s přesnou proveniencí k 1971.
Staré stavy „článek nezískán“ se u těchto dvou zdrojů již nepřebírají.

Výslovně přeskočeno: datum Watsonova jednotlivého sešitu; úplná kolace
Grünbaum–Shephard 1987 kap. 10–11; Bergerův původní 72stránkový důkaz
a přesný vztah jeho konstrukce ke Knuthově; celý Durand 1999;
Penroseův původní článek a Gardner 1989 kap. 1–2, tedy přesná historická
návaznost dvou polygonů a sady 16 typů. Matematická existence a
optimalita menších sad je doložena publikovaným Jeandel–Rao, není
označována za naši opakovanou klasifikaci. Historické formulace v
odstavci nahrazeném roku 2023 nejsou prohlášeny za přímo ověřené.

Krátké nové hledání našlo institucionální kopii Ammann–Grünbaum–Shephard,
*Aperiodic Tiles*, DCG 8 (1992), 1–25. PDF bylo skutečně staženo,
metadata a hash jsou v `sources/sequential-2026-11-05/`; přímo zobrazeny
jen tištěné 1 a 25 (PDF 2 a 26). Ty potvrzují identitu, rozsah a odkaz
na Penrose 1974, samy ale neuzavírají přesný historický řetězec výše.
Ostatní strany nového článku ani nepřístupné kapitoly se nevydávají
za přečtené. Nepokračujeme v již neúspěšných přístupových trasách Duranda.

Čtyři celé vrstvy errat z aktuálního listopadového snímku byly nově
prohledány podle stran i témat; 10 stránkových bloků a 13 tematických
zásahů je v `infinity-lemma-errata-extract.json`. Sedm různých datovaných
položek zůstává sedmi, duplicity all1/err1 nejsou nové opravy.

Hlavní text a všech osm úloh jsou v dohodnutém rozsahu checked,
s uvedenými bibliografickými a reprodukčními výjimkami. Není nový nález.
Celé strany 382–385 a 586–587 jsou nyní prošlé; na 382/586 je zahrnut
předchozí orientovaný blok. Na 386 a 588 zbývá následující enumerace.
X0353 mapuje známé vady přesně na 586–587. C0052 má jen related lokaci
587 a kind=errata, takže samo původní stránku neobarvuje červeně.
