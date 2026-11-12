# DLX 117–120: barvení a periodická dláždění

Checkpoint 2. listopadu 2026 navazuje na [115–117](GRAPHS115_120_NOTES.md).
Úlohy **118, 119 a 120 jsou úplně prověřeny**, včetně opraveného závěru 120(b).
Úloha 117 zůstává částečná. Odkazy na úlohy zde znamenají §7.2.2.1;
zdrojem je lokální druhý dotisk 4B z listopadu 2022. Fyzický výtisk nemáme
ověřený. Žádné nové emailové návrhy nevznikají.

## F132: druhé dláždění v odpovědi 120(b)

**Tvrzení o jediném dláždění je za vytištěných podmínek nesprávné.**
Stačí druhý, čtvrtý a šestý dílek rodiny (b) na straně 138. Jejich barvy
v pořadí sever, východ, jih, západ jsou:

| Pořadí dílku v obrázku | Sever | Východ | Jih | Západ |
|---|---|---|---|---|
| 2 | bílá | červená | červená | bílá |
| 4 | červená | modrá | modrá | červená |
| 6 | modrá | bílá | bílá | modrá |

Vpravo i dole po dílku 2 následuje 4, po 4 následuje 6 a po 6 následuje 2.
Opakujeme proto tento blok v obou směrech:

    2 4 6
    4 6 2
    6 2 4

[Obrázek pro ruční kontrolu](images/tetrads120-counterexample.png) ukazuje
všechny hrany. Pro libovolná celá r,c dává vzorec
`tile(r,c) = [2,4,6][(r+c) mod 3]` platné dláždění celé roviny, bez otočení
či převracení dílků. Základní periodická buňka má plochu 3; obdélník 3×3
obsahuje tři její kopie. Použité tři typy jsou různé, takže index periodické
mřížky je přesně 3.

Knižní obrázek s buňkou plochy 13 je také platný, ale není posunutím tohoto
vzoru: obsahuje dalších sedm typů. Zadání nevyžaduje výskyt každého z deseti
typů. Kdyby takovou podmínku doplnilo, jediná třináctibuněčná třída by zůstala.
Bez ní chybí v odpovědi celá další třída řešení.

Všechny barvy i orientace tří dílků byly ověřeny v původních PDF vektorech
a nezávisle v autorově PostScriptu z roku 2019. Odpovídající oprava
jednoznačnosti není v aktuálních ani historických erratech. Nejde o tvrzení
o prvenství nálezu nebo o jeho přijetí autorem.

## Úplná klasifikace 120

Z původních vektorů bylo přečteno všech **80 barevných trojúhelníků** dvaceti
typů, **2 688 trojúhelníků** obou ilustračních pásů a **250 znaků** tabulky
vynucených okolí. Všech 672 zobrazených dílků má správné sousedy.

Dvě odlišné metody vyčíslily všechny výplně čtverce 5×5: původní Knuthův
Algoritmus C a přímé skládání vodorovných řádků podle jejich horních a dolních
barev. Shodují se celé množiny: **125 výplní pro (a), 1 636 pro (b)**.
Řádková metoda prochází všechny vodorovně přípustné řádky a všechny jejich
navazující pětice. Konstrukce XCC má jednu primární položku na buňku a
barevné sekundární položky na hrany; její modely jsou v bijekci s výplněmi.

Počty podle středového typu v (a) jsou přesně knižních
`16,8,19,8,8,8,10,8,16,24`. Průniky souhlasí se všemi 250 znaky tabulky.
Pro (b) vycházejí `8,402,12,392,108,411,84,27,66,126`.

**Proč konečné výpočty dokazují výsledek pro rovinu:** každý výskyt typu
v nekonečném dláždění má některé z vyčíslených okolí 5×5. Průnik těchto
okolí tedy dává nutná místní pravidla. U (a) zvolíme kotvu typu 5,
číslováno od nuly; u (b) typ 0. Uložený řetězec pravidel vynutí z kotvy
další stejné kotvy v obou směrech dvou nezávislých posunů a všechny
zástupce tříd modulo příslušná periodická mřížka:

| Rodina | Generátory posunů (řádek, sloupec) | Index mřížky |
|---|---|---:|
| a | (0,3), (4,−1) | 12 |
| b, obsahuje typ 0 | (0,13), (1,−9) | 13 |

Tentýž konečný důkaz lze přeložit do každé další vynucené kotvy. Indukcí
podél generátorů pokryje všechny kotvy a jejich okolí celou Z². To je
obecný důkaz jednoznačnosti při pevné kotvě. Certifikát uvádí rodiče a
pravidlo každého kroku. Samostatné přehrání certifikátu i kontrola všech
hran základní buňky potvrzují správnost a existenci nekonečného vzoru.
Jediná kotva v základní buňce dokazuje také minimálnost indexu.

Každé možné okolí 5×5 rodiny (a) obsahuje její kotvu, takže (a) má právě
jednu třídu až na posunutí. V rodině (b) typy 0,2,4,6,7,8,9 vynutí typ 0
přímo nebo přes další vynucený typ. Zbývají jen 1,3,5. Mezi nimi je pravý
i dolní soused určen cyklem 1→3→5→1, tedy právě výše uvedený protipříklad.
**Rodina (b) má proto přesně dvě třídy až na posunutí, s plochami 13 a 3.**

[Úplné konečné množiny](results/graphs117_120/tetrads120-finite-checked.json),
[certifikáty pro rovinu](results/graphs117_120/tetrads120-plane-checked.json)
a [extrakce vektorů](results/graphs117_120/tetrads120-vectors.json).

## F131 a E060: citace a již opravený obrázek

**F131:** v zadání 120 na straně 138 je v citaci číslo ročníku **231**;
správně je **213**. Stejné přehození číslic má autorův draft na straně 74.
[Vydavatelský přehled listopadu 1965](https://www.scientificamerican.com/issue/sa/1965/11-01/)
a metadata původního článku Hao Wanga, DOI
[10.1038/scientificamerican1165-98](https://doi.org/10.1038/scientificamerican1165-98),
nezávisle potvrzují ročník 213, číslo 5. Jde o drobnou bibliografickou chybu.

Původní článek byl archivován z veřejné kopie v Institute for Advanced Study.
Prohlédnuty byly skutečné strany 103 a 106; první obsahuje deset typů
rodiny (a), druhá jejich periodické uspořádání. U všech 72 zobrazených dílků
na straně 106 byly přečteny barvy, ověřeny typy a shody hran. Kontrola
neznamená audit ostatního obsahu článku.

**E060:** historická oprava z **15. října 2021**, Fascicle 5, strana 253,
řádek −3, nahrazuje obrázek u **120(a)**. Naše 4B už obsahuje opravenou
verzi: všech 336 dílků odpovídá erratu. Starý draft se liší ve 156 buňkách
tohoto pásu. Rodina (b), jejích deset vstupních typů ani její obrázek se tím
nemění; tato oprava tedy neodstraňuje F132.

[Doklady k historii](results/graphs117_120/wang1965-history-checked.json),
[šest úplných vrstev errat](results/graphs117_120/errata-check.json).
Čtyři aktuální originály byly při kontrole staženy a jejich hash se nezměnil.

## 118: všechny čtyři rozklady a oba geometrické typy

Žádná barva nemůže zabrat více než dvě buňky v jednom řádku, a tedy více
než 16 buněk celé šachovnice. Čtyři barvy dohromady pokryjí 64 buněk:
každá proto musí mít právě 16, přesně dvě v každém řádku.

Úplný výčet všech dvojic v každém z osmi řádků, s vylučováním třetího
kolineárního bodu, dává **380 množin**. Každá byla samostatně ověřena
determinantem pro všech 560 trojic. Každá přípustná šestnáctice se ve
výčtu nutně objeví a žádná se nevynechá kvůli zvolené symetrii.

Původní Algoritmus X i nezávislé skládání disjunktních bitových množin
dávají celé stejné **čtyři neoznačené rozklady**. Kanonizace osmi symetrií
čtverce je rozdělí na **dvě třídy**. Všech 64 znaků vytištěného příkladu
bylo přečteno z původních vektorů. Druhý typ opravdu vznikne transpozicí
poloh B a D při zachování A a C; nejde o pouhé přejmenování B↔D.

Obecná redukce hypergrafového barvení také platí: pro každou hyperhranu H
a barvu je položka s dovolenou násobností 0 až |H|−1. Výběr jedné možnosti
na vrchol určuje jeho barvu a zakazuje právě jednobarevné hyperhrany.
V této úloze stačí za hyperhrany vzít všechny kolineární trojice.
[Úplný doklad](results/graphs117_120/hypergraph118-checked.json).

## 119: bílý dílek musí ležet při okraji

Mezi 24 různými trojúhelníky je 11 s žádnou bílou hranou, 9 s jednou,
3 se dvěma a 1 se třemi. Dohromady mají 18 bílých stran. Bílé obvodové
hrany hexagonu spotřebují 12; každá vnitřní bílá hrana spotřebuje dvě.
Vnitřní bílé hrany jsou proto vždy právě **(18−12)/2 = 3**.

Kdyby celý bílý dílek ležel uvnitř, jeho tři hrany by vyčerpaly všechny
vnitřní bílé hrany. Ostatní dílky mají nejvýše jednu obvodovou hranu
a nejvýše jednu hranu sousedící s tímto dílkem. V žádné vnitřní poloze
nejsou tři sousední místa s oběma možnostmi současně. Všechny tři dílky
se dvěma bílými stranami tedy nelze umístit.

Argument je doložen pro všech 12 vnitřních poloh. Doplňkově bylo vyzkoušeno
všech 4 060 trojic vnitřních hran: správné rozložení bílých stran má
72 kostřiček a jejich bílý dílek leží právě v jedné z 12 okrajových poloh.
Ty tvoří jedinou orbitu dvanácti symetrií hexagonu, obsahující také polohu
v obrázku 59(b) na straně 91. Netvrdíme, že každá bílá kostřička jde doplnit
všemi barevnými dílky; pro důkaz normalizace stačí nutná podmínka.
[Geometrický certifikát](results/graphs117_120/macmahon119-checked.json).

## 117 a dlouhé výpočty zůstávají otevřené

Obecné převody (a),(b) jsou v bijekci s barveními: primární položka vynutí
jednu barvu každého vrcholu a sekundární položka pro dvojici klika–barva
zakáže dva vrcholy téže barvy v téže klice. Hrany jsou speciálním případem
dvouprvkových klik. U Q8 bylo přímou geometrií ověřeno všech **728 hran**
a všech **42 klik**, včetně rovnosti obou popisů sousednosti.

Horní řádek obsahuje osm navzájem sousedních vrcholů. Při devíti dostupných
barvách jej lze jednoznačně přeznačit na 0,…,7 a zbylou barvu na 8. Každé
barevné rozdělení tak má 9! označených variant, i když devátou barvu
nepoužije. Tento faktor je přesný.

Nově běží tři oddělené výpočty: původní Algoritmus X s hranami, s klikami,
a nezávislý DSATUR. Každý má vlastní vstup, PID, limit 48 hodin a přímý
soubor pro výstup. Žádný není při tomto checkpointu přijat jako dokončený.
Zdrojové soubory jsou po dobu běhu neměnné. U nativních běhů se ukládá
každý desetitisící model; konečný počet bude nezávisle porovnán.
Úprava z 122, odpovídající běhy Algoritmu C a přesné historické náklady
i Monte Carlo poznámka k M6 zbývají. Dřívější úplné počty Mc se neopakují.

Ze starší fronty slovních schodů bylo nově přijato sedm dokončených optim:
diagonální případy 9 a 10 a dvousměrné případy 2 až 6. Souhlasí s knihou.
Celkem je hotovo 13 ze 17; dvousměrné 7 až 10 zůstávají otevřené.
[Nové terminály](results/graphs117_120/stairs-new-checked.json).

## Doplnění 2. listopadu 2026, 07:14 UTC: dokončený nezávislý Q8

DSATUR dokončil všech 2 906 400 379 uzlů a našel přesně **262 164**
barevných rozdělení do devíti tříd. Do osmi nebo méně tříd nenašel žádné.
Terminál má návratový kód nula; vstup všech 728 hran, binární soubor,
neměnný zdroj a oba výstupy byly ověřeny proti zaznamenaným hashům.
Stejný zdroj byl dříve porovnán s úplným oracle na 300 malých případech;
tyto úspěšné výpočty nebyly opakovány.

Výběr vrcholu DSATUR závisí na počtu zakázaných barev, zbývajícím stupni
a indexu vrcholu, takže je invariantní vůči přejmenování barev. Větev může
použít každou již zavedenou přípustnou barvu a právě jednu novou; tím
reprezentuje každé neoznačené rozdělení právě jednou. Undo obnovuje
předchozí masku každého dosud neobarveného souseda. Vyřazení při devíti
zakázaných barvách je přesné. Počet uzlů i konečný počet se vejdou do
64bitových čítačů; pro 64 vrcholů kód výslovně obchází posun o64 bitů.

Jde o úplný nezávislý počet, nikoli archiv všech výsledných obarvení
nebo reprodukci paměťových nákladů algoritmu C. Čtyři další výpočty
Algoritmy X/C stále běží. Úloha117 jako celek zůstává partial kvůli
M6, Monte Carlo údaji a přesným historickým nákladům.
[Přijímací kontrola](results/graphs117_120/queen117-independent-checked.json)
neprovádí nové hledání.

## Doplnění 2. listopadu 2026, 20:25 UTC: třetí úplný počet Q8

Původní běh Algorithm C s klikami skončil v19:48:42 UTC, kód0.
Stejně jako již přijatý X s klikami a nezávislý DSATUR dává **262164**
rozkladů. Oba klikové nativní běhy navštívily **16809942790 uzlů**.
Nový C běh má **6.951597006912 T čistých memů**. Všech26 uložených
vzorků prošlo přímým geometrickým testem útoků a kontrolou různosti.
Vstup i všechny otisky terminálu byly ověřeny bez opakovaného hledání.

Tím se aktualizuje starší stav výše: zbývají pouze dva hranové běhy
X/C. Celé množiny Q8 modelů se neukládaly, proto jejich shodu netvrdíme.
M6, Monte Carlo a přesné historické náklady zůstávají otevřené.
[Přijatý C terminál](results/symmetry121_123/graphs/q8-queen-cliques-accepted.json).
