# Souměrnosti dam: Dancing Links 22–24

Zadání na str. 126 a odpovědi 419–421 byly zobrazeny v původním PDF.
Tři malé diagramy úlohy 22 byly navíc vykresleny ve zvětšení. Pro nálezy
byly porovnány také autorovy stránky 124–125 z Fascicle 5C, datované
11. září 2019. Fyzický výtisk zatím ověřen není.

Nové nálezy: F106 (vypsané možnosti v 23(a)), F107 (nesprávné redukční
filtry v 24), F108 (poslední počet v 22(c)). E024 je již známá oprava
podílu v 23(a). Aktuální TeX a historické dlouhé seznamy errat 4B/4F5
byly znovu staženy 1. listopadu; všechny čtyři SHA256 souhlasí s archivem.
Vyhledání relevantních stran a výrazů zaznamenává
[errata-check.json](results/queen_symmetry/errata-check.json).

## Nezávislý úplný výčet

[queen_symmetry.cpp](queen_symmetry.cpp) pokládá jednu dámu po druhé podle
řádků a používá bitové masky obsazených sloupců a diagonál. Nepoužívá
exact cover ani párové kódování. V každém úplném řešení určí počet
obsazených hlavních diagonál, přítomnost centrální dámy, invarianci vůči
90°/180° a příslušné nerovnosti na obvodu. Sedm úplných množin n=4..10
souhlasí s nezávislými permutacemi; shoduje se každá klasifikace.

Potom doběhly úplné n=11..17. Největší výčet navštívil 8 017 021 932 uzlů
a našel 95 815 104 řešení. Čas, příkaz, PID, hashe binárky/zdroje/výsledků
a konečný stav jsou uloženy v `results/queen_symmetry/`. Tento výpočet je
dokončený; není zaměňován s dosud běžícími Langfordovými výpočty.

## Proč v případech 22 vzniká právě jeden zástupce z osmi

Žádné řešení n-dam pro n>1 nemůže být invariantní vůči zrcadlení.
Svislé/vodorovné zrcadlení by nutilo všechny dámy do prostředního sloupce/
řádku. Při diagonálním zrcadlení by odlišné protějšky (r,c),(c,r) ležely
na společné diagonále; samé pevné body by zase ležely na hlavní diagonále.
Obdobně pro druhou diagonálu. Stabilizátory tedy obsahují jen rotace.

V 22(a), liché n a obě hlavní diagonály prázdné, by 180° invariance
vyžadovala centrální dámu, což je vyloučeno. V (b) a (c) by každá
necentrální dáma na hlavní diagonále měla na téže diagonále i svůj
180° protějšek. Tyto případy proto nemají rotační stabilizátor a všechny
orbity mají osm prvků.

Pro (a) vezměme dámu v prostředním řádku a dámu v prostředním sloupci.
Jejich nenulové vzdálenosti od středu jsou různé, jinak by se napadaly.
Rotace a zrcadlení dovolují právě jedno uspořádání 1≤i<j<h, kde
h=floor(n/2)+1. V (b) lze jedinou diagonální dámu umístit na hlavní
diagonálu nad střed. Zbývající zrcadlení prohodí dámu v posledním řádku
a posledním sloupci. Jejich vzdálenosti od pravého dolního rohu se
nemohou rovnat, protože by se napadaly; právě jedna orientace má
dolní dámu blíže. V (c) působí stejné argumenty na dvě odlišné diagonální
dámy: jednoznačně dosáhneme 1≤i<j<h.

Vynechaná pole v odpovědi zajišťují rozsahy indexů pro tři párová
kódování. Po přejmenování na indexy z 0..m−1 je jejich podmínka právě
α-index≤β-index; v (a,c) znamená i<j, v (b) znamená, že sloupec dámy
v dolním řádku je větší než řádek dámy v pravém sloupci. Proměnění
diagonálních položek na primární zajišťuje požadovaný počet diagonálních
dam. Ostatní položky stále vyjadřují přesně nenapadání dam.

[check_queen_pair_symmetry.py](check_queen_pair_symmetry.py) sestavil
doslovné možnosti z odpovědi a spustil veřejný neupravený DLX1.
Všech **31 úplných počtů** souhlasí s nezávislým řádkovým výčtem;
**15 malých úplných množin modelů** souhlasí i jednotlivě.

Největší náklady jsou 3 328 344 219 memů pro (a),n17;
5 972 034 766 pro (b),n16; 5 521 722 581 pro (c),n16. První je pod
uváděnými 3,4G, další dvě se zaokrouhlují na 6,0G a 5,5G. Netvrdíme
bitovou totožnost původního neveřejného měření.

Tři diagramy na str. 126 mají řádkové posloupnosti
536928147, 146392857 a 184279635. Všechny jsou platná řešení n=9,
mají právě uvedený druh obsazení diagonál a splňují popsanou orientaci.

## F108: poslední počet v odpovědi 22(c)

Pro n=16 jsou na obou hlavních diagonálách různé dámy v přesně
9 767 344 řešeních. Orbity jsou volné, takže počet zástupců je
**9 767 344 / 8 = 1 220 918**, nikoli vytištěných **1 220 908**.
Stejných 1 220 918 dává nezávislý DLX1 s doslovným knižním kódováním.
Ostatních 30 vytištěných počtů v odpovědi 22 souhlasí.

Krátká dodatečná kontrola využívá rozklad všech řešení n=16 podle
počtu obsazených hlavních diagonál:

    (14 772 512 − 454 376 − 8 × 568 849) / 8 = 1 220 918.

Původní údaj by v tomto rozkladu ztratil 80 řešení. Oprava se týká
jediné číslice v seznamu. PDF420 i PS124 mají původní údaj; odpovídající
oprava v ověřených erratech nenalezena.

## Obvodové nerovnosti a F106 v odpovědi 23(a)

Používáme přesnou definici knihy: a je sloupec dámy v řádku 1, b je
řádek dámy ve sloupci n, c=n+1−(sloupec dámy v řádku n) a obdobně d
pro levý sloupec. Rotace cyklí (a,b,c,d), zrcadlení obrací pořadí
a doplňuje souřadnice na n+1. Volbou nejmenší ze souřadnic a jejich
doplňků lze dosáhnout a≤b,c,d<ā. Rovnosti s ā jsou vyloučeny
nenapadáním příslušných obvodových dam. Opakované minimum může
ponechat více zástupců jedné orbity; proto se zde neslibuje přesný faktor8.

Nezávislý výčet potvrzuje pro n16: 454 376 původních řešení,
64 374 po slabých nerovnostech, 59 648 po pěti dodatečných vzorech
rovností a 57 188 skutečných D4 tříd. Poslední číslo nezávisle dává
Burnsideův vzorec (454376+3000+2×64)/8. Pro centrální n17 souhlasí
4 067 152 původních a 577 732 slabě omezených řešení. Podíly se
zaokrouhlují na 7,06 a 7,04.

Vypsaný sedmimožnostní příklad má dvě chyby:

* Nadpis skupiny uvádí **a=1**, ale první možnost je r1 c2 a3 b−1,
  tedy **a=2** podle vlastní definice. Hodnota a=1 by znamenala
  zakázaný roh na hlavní diagonále.
* Zrcadlovým protějškem dolního sloupce2 je sloupec15, nikoli14.
  Možnost `r16 c14 a30 b2 y1 y2 y4` má ve skupině vzdálenosti2 znít
  **`r16 c15 a31 b1 y1 y2 y4`**. Při ponechání sloupce14 by se muselo
  vynechat y1, protože jde o vzdálenost3 s položkami B1={y2,y4}.

Chybná přidaná y1 není jen estetický rozdíl: překryje se s A1={y1}
horního sloupce3, přestože rovnost obvodových vzdáleností3 je dovolená.
Úplný platný svědek bez hlavních diagonál má řádkové sloupce

    3 5 8 10 13 2 6 1 16 11 15 4 7 9 12 14.

Jeho (a,b,c,d)=(3,9,3,9) splňuje všechny slabé nerovnosti, ale vytištěná
možnost pro poslední dámu by jej přes y1 odmítla. Svědek byl nalezen DLX1
a každá jeho dáma, diagonála i nerovnost je samostatně validována v
[check_queen_symmetry_example.py](check_queen_symmetry_example.py).
Obě chyby jsou i v autorově PS; v erratech nalezena pouze následující
jiná oprava.

## E024: již publikovaný podíl 3,58

Oficiální erratum z 16. 11. 2024 mění v odpovědi 23(a) podíl3,68 na3,58.
Z uvedených nákladů 4,3/1,2 = 43/12 = 3,58333… plyne právě oprava.
Je vedena jako známá, odděleně od F106.

Původní vstupy a výkonové údaje pro slabou a pětipřípadovou obvodovou
redukci zatím nejsou plně rekonstruovány. Text navíc ve druhém odstavci
znovu používá a při popisu indexovaných možností. Celá úloha23 proto
zůstává částečná; potvrzený lokální nález nepředstírá uzavření jejího rozsahu.

## Rotační možnosti a úplná tabulka odpovědi 24

Při invarianci vůči dané rotaci je množina dam sjednocením celých
orbit polí. Stačí tedy každou vnitřně slučitelnou orbitu nahradit jednou
možností obsahující sjednocení jejích řádkových, sloupcových a diagonálních
položek. Nekompatibilní orbitu poznáme podle opakované položky. Exact cover
pak přesně vybírá disjunktní nenapadající orbity a pokryje všechny řádky.
Pro liché n musí 180° souměrné řešení obsahovat střed; u 90° řešení je
to nutné také. Při n≡2,3 mod4 nemůže 90° řešení existovat.

Doslovné n4/n5 seznamy ze str. 420 byly jednotlivě přepsány a porovnány
s generovanými orbitami; souhlasí všech 14 možností ze čtyř seznamů.
Pro n4..9 souhlasí 12 úplných množin rotačních řešení s nezávislými
permutacemi. Pro n4..17 byly ve veřejném DLX1 spočítány oba typy rotací
a každý model 180° i redukovaný model90° byl samostatně geometricky ověřen.
Jejich počty se shodují s klasifikací nezávislého výčtu všech dam.

Protože zrcadlení nemají pevná řešení, jsou velikosti D4 orbit8,4,2,
podle toho, zda je rotační stabilizátor triviální, poloviční nebo úplný.
Označíme-li úplné počty invariantních řešení H a R, máme
Qa=(Q−H)/8, Qs=(H−R)/4 a Qd=R/2. Všech **42 hodnot tabulky** pro
n4..17 souhlasí. Pro n16 je H=3000,R=64; pro n17 H=8152,R=128.

## F107: vytištěné redukční filtry mohou odstranit všechna řešení

Poslední věta str. 420 navrhuje odstranit možnosti obsahující {r1,c_k}
pro k≥ceil(n/2), aby se počet řešení180° zmenšil na polovinu. Již pro
n4 jsou původní řešení 2413 a3142; obě začínají ve sloupci k≥2.
Pravidlo je tudíž odstraní **obě**, místo aby ponechalo jedno.

Tento protipříklad funguje i při vstřícném geometrickém výkladu
„obsahuje dámu v políčku (1,k)“. Doslovné čtení sjednocené možnosti
je ještě širší: položky r1 a c_k mohou pocházet z různých dam jedné
sloučené orbity. Geometrii páru proto nelze nahradit touto neoznačenou
dvojicí položek.

Navazující filtr90° na str. 421 odstraňuje možnosti obsahující {r_j,c_k}
pro j<ceil(n/2), k≥ceil(n/2). Každá necentrální kompatibilní čtvrtotáčková
orbita má bod v pravé horní části a její sjednocené položky zároveň
obsahují horní řádek i pravý sloupec. Filtr tak odstraní všechny takové
orbity. Konkrétně pro n4 z původních dvou možností nezůstane ani jedna,
přestože slíbený faktor2 má ponechat jedno řešení. Protipříklad zůstává
platný pod doslovným i geometrickým výkladem. Obojí ověřuje
[check_queen_rotations.py](check_queen_rotations.py).

Použitelná oprava pro180°: vyřadit orbitu, **jejíž skutečná dáma v prvním
řádku leží ve sloupci k>n/2**. Zachová se metadata geometrického páru.
Svislé zrcadlení páruje řešení a nemá pevný první sloupec; právě jedno
z každé dvojice proto přežije. U lichého n středový sloupec v prvním
řádku stejně není možný, protože středová dáma je vynucena.

Použitelná oprava pro90°: **ponechat jedinou možnost z každé dvojice
identických množin položek**. Čtvrtotáčková orbita a její zrcadlový
protějšek mají stejné řádky, sloupce i obě sady diagonál. Jsou dvě,
protože osová nebo diagonální poloha by dala vnitřně napadající orbity.
Řádková sada určuje právě tyto dvě chirality. Každé úplné řešení obsahuje
floor(n/4) takových orbit; chirality lze měnit nezávisle, neboť přesně
stejné položky zajišťují slučitelnost s ostatními orbitami. Odstranění
duplicit proto dává požadovaný faktor 2^floor(n/4). Centrální singleton
se neduplikuje.

Opravené varianty souhlasí se všemi počty n4..17. Pro n32 redukovaný
výčet dává **1589** geometricky ověřených modelů, takže počet tříd je
1589×2^7=203392, přesně jak uvádí kniha. Při organ-pipe pořadí trvá
n16 poloviční redukce 5 034 201 memů (přibližně5M), n16 čtvrtotáčková
40 989 memů (pod uváděnými70K) a n32 čtvrtotáčková19 625 456 memů
(přibližně20M). Číselné výsledky knihy jsou tedy správné a dosažitelné;
vadné je zveřejněné znění odstraňovacích pravidel. Stejné znění je v PS,
v relevantních aktuálních ani historických erratech oprava nenalezena.

## Stav průchodu

Úloha22 je uzavřena s opravou F108, úloha24 s opravou F107. Úloha23
zůstává částečná s lokálním F106 a známým E024. Celé strany420–421
se tím neoznačují za hotové, protože obsahují také částečnou23 a další
dosud neuzavřené odpovědi. Nálezy nejsou potvrzením prvenství ani odměny.
