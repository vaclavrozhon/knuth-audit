# Souvislý průchod §1.2.10 — 5. listopadu 2026

Přímo přečten původní výklad 96–107 a odpovědi 500–502, soubor
111–122 a 515–517. Na 107 a 502 již začíná následující oddíl;
jeho obsah tento blok ještě neuzavírá. Přijaty celé důkazy
`analysis-records.md`, `analysis-probability.md`, `analysis-tails.md`,
`analysis-findings.md` a přehled všech vrstev errat. Přečteny také
přijaté pramenné recenze de Moivra, Gnedenka–Kolmogorova, publikovaného
Chernoffa, Thieleho–Halda a zbývajících historických citací.
Jejich přesné rozsahy původní četby se nerozšiřují.

Uložených 168264 kombinatorických/numerických a 150 symbolických
kontrol bylo přečteno, nikoli znovu spuštěno. Žádný brute force
se nespouštěl a žádný nový nález nevznikl.

## Matematika a fakta

Algoritmus M pro n>0 udržuje maximum zpracovaného suffixu a jeho
nejpravější index. Počet kroků je 1,n,n−1,A,n−1; obrázek 9 odpovídá
větvení. Rekurence počtu permutací a součin generující funkce dávají
střed H_n−1 a rozptyl H_n−H_n^(2). Tabulka šesti permutací, obrázky
10 a 11, čísla pro n=12 a n=1000 i dvanáctimístné normální
pravděpodobnosti souhlasí s uloženými přesnými intervaly.

Případy opakovaných hodnot je třeba rozlišit: při podmínění na počet
různých hodnot jsou jejich přiřazení k blokům záměnná; pevné četnosti
jednotlivých uspořádaných hodnot mají jiný součin. Správný součin
v úloze 18 zahrnuje i nejvyšší přítomnou hodnotu a dělení z. Prázdné
faktory s nulovým součtem četností se vynechají. Obsazovací rekurence,
Stirlingovy koeficienty, střed počtu rekordů, vztah k inverzní permutaci
a výběr krajních rekordů pro rozdíly a_k−b_k jsou obecně dokázány.

Pravděpodobnostní generující funkce konvergují absolutně na uzavřeném
jednotkovém kruhu. Momentové vzorce u 1 se používají s příslušnými
konečnými momenty; pro konečnou formální identitu kumulantů není třeba
automaticky tvrdit existenci celé momentové funkce v okolí nuly.
Součin vyjadřuje součet nezávislých veličin, složení náhodný počet
nezávislých sčítanců. Odvození momentů směsi i složení, všech kumulantů
rovnoměrného rozdělení a momentově-kumulantové rozkladové formule
souhlasí. Normální limity pro rekordy, binomické a Poissonovo rozdělení
mají správné centrování a škálování; nulový rozptyl se nestandardizuje.

Chebyshevův ostrý ocas a oba odhady pomocí generující funkce jsou
ověřeny včetně krajních případů. Obecná verze vyžaduje nezápornost f
na celém nosiči, nikoli jen v ocasu. Binomické odhady plynou z relativní
entropie D_p; pro všechna p platí D_p(ε)>=2ε². Silnější symetrický
řadový odhad vyžaduje p>=1/2 a ε<=1−p. Chernoffova formule funguje
i pro rozdílná p_k; uvedené konstanty 0.825 a práh 4.32 odpovídají
uloženým intervalům. U negativně binomického rozdělení je horní
kvadratický odhad omezen na ε<=p. Nové 4pq v jmenovateli z roku 2024
je platné zesílení staršího 6pq na tomto oboru.

## Nálezy a mapa původních stran

C0013 je podstatná původní chyba v odpovědi 13 na 501: pro n=2
je standardizovaná absolutní odchylka vždy 1. Při x=1/2 tedy žádné
a>0 nemůže dát 1<exp(−a/2). Nutný je násobný faktor C; citovaná
definice Flajoleta–Sorii ho obsahuje. Vlastní důkaz připouští
a=1/2, C=2exp(1/4) jednotně pro n>=2. Tato karta zůstává high.

C0014 je menší původní nepřesnost odpovědi 17(a) na téže straně:
pro f=(1+z)/2 je konstantní koeficient g(f) nekonečný součet
sum q_j 2^(−j), obecně nikoli polynom v konečně mnoha koeficientech.
Nezáporné konvergentní součty dokazují požadovaný závěr. UI priorita
se mění z medium na low; pravdivost tvrzení o složené PGF ani správné
momentové vzorce se tím nemění.

C0015 patří výhradně do dodatku z 25.4.2023 k odpovědi 21. V původním
textu 1997 tato řada není. Chybí n v exponentu a ani po jeho vložení
není odhad platný pro všechna p: n=8,p=1/4,ε=1/2 dává
277/65536>1/256. Při ε>1/2 navíc řada diverguje. Aktuální all1 strana
13, přímo vykreslená z dnešního PostScriptu a přečtená v X0943,
potvrzuje přesně toto chybné znění. Karta má kind=errata; původní
502 je pouze souvisejícím místem vložení. Ostatní skutečné vady
původní 502 mají samostatný známý záznam X0118.

X0118 přesně umisťuje původní opravy na 96,98,100,103–106,500–502:
chybějící n>0 u M; index rekurence; interpunkce citace; datum Thieleho
a index kumulantu; globální nezápornost f; město vydání; de Moivre,
zavádějící „distinct“ a chybný součin úlohy 18; závorky a argument H′,
přebytečný faktoriál, term/factor; další závorky a člen Poissonova
rozvoje; lineární člen binomického logaritmu, rozsah Chernoffova
článku, záporné exponenty, chybějící <1/2 a obor ε<=p.

Ekvivalentní přeuspořádání z+1, počáteční hodnota G_0 místo G_1,
změna Bernoulliho konvence a doplnění již kontextových parametrů
se automaticky neoznačují za původní matematickou chybu. Oprava
odpovědi 10 z roku 2023 napravuje dopad nové konvence B_1=+1/2;
původní vzorec byl se starou konvencí správný. Rozšíření odhadu
Chernoffa na všechna δ>=0 je nový výsledek, nikoli stará vada.

## Přesné zbývající výjimky

Všech 23 úloh bylo již uzavřeno a tento stav se nemění. Roesova
citovaná 342, Hald2000 137–153 a kolace Kolmogorova1933/Bernsteina1924
s prvními tisky se podle zadání bibliograficky přeskakují. Jejich
matematický obsah má vlastní přijaté důkazy nebo identifikované přetisky.
Původní de Moivrova obecná aproximace, věta Gnedenka–Kolmogorova,
publikovaný Chernoff, Thiele1889 a Bienaymé1853 byly přijaty v přesných
rozsazích již uložených recenzí.

Tvrzení o historickém prvenství Foster–Stuarta na 100 a obecného
Kolmogorovova principu na 104 zůstávají výslovně neověřená; hlavní
oddíl proto zůstává partial. Otevřené prvenství není matematická
chyba ani ověřená historie. Strany 100 a 104 mají částečné pokrytí,
107 a 502 také čekají na následující oddíl. Ostatní zde uvedené
strany jsou obsahově zkontrolovány. Žádné nové stahování nedostupných
článků ani úspěšné výpočty se neopakovaly.
