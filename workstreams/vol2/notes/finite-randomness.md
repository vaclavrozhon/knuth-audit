# §3.5 E: konečná náhodnost, tabulky a úloha 38

Stav 1. listopadu 2026. Původní strany 168–170 a zadání 38 na straně 183
přečteny vizuálně. Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2`
a aktuální TeX errat podle stran, Q1/Q2, jmen i témat. K tomuto bloku
nenalezena věcná oprava; změna z 25. října 2010 pouze odděluje definice.
Žádný nový potvrzený nález. Úloha 38 je výzkumná: níže je audit její
formulace, obecné meze a malé přesné případy, nikoli úplné asymptotické řešení.

## 1. Q1 a tabulka na straně 168

Slovo délky N nad číslicemi 0,...,b−1 je podle Q1 náhodné, když pro každé
k s b^k<=N a každé k-slovo w platí |C(w)/N−b^(−k)|<=1/sqrt(N).
C(w) počítá pouze výskyty celé obsažené ve slově, nikoli cyklická okna;
normalizační jmenovatel přesto zůstává N. V konečné definici správné
četnosti k-slov nemusí implikovat správné četnosti kratších slov.
Například 00010001000 má devět nul, takže neprojde pro k=1; počty
00,01,10,11 jsou 6,2,2,0 a pro k=2 projdou.

Přesný výčet všech 2048 binárních slov délky 11 dává právě 178 slov
nevyhovujících Q1. Jejich množina přesně souhlasí s 21 explicitně uvedenými
slovy, střídavým slovem, slovy s alespoň devíti nulami a všemi doplňky.
Při testování se odmocnina eliminuje přesnou celočíselnou nerovností
(C(w)b^k−N)^2<=N b^(2k); nezávisí to na zaokrouhlení.

Existenci pro každé N lze dokázat přímo pomocí úplného cyklu:
cyklus řádu r nad b číslicemi má periodu P=b^r a každé r-slovo obsahuje
právě jednou jako cyklické okno. Jeho existence byla dokázána v
`complete-sequences.md`. Pro N<b nejsou žádné testy. Jinak zvolme r
nejmenší s P>=sqrt(N); tedy sqrt(N)<=P<b sqrt(N) a P<=N. Opakujme
libovolný takový cyklus a vezměme prvních N číslic.

Pro k<=r se v každé periodě každé k-slovo objeví P/b^k krát. Rozdělme
N−k+1 počátečních pozic oken na celé periody a jeden zbytek. Odchylka
počtu ve zbytku od jeho očekávaného počtu nepřesáhne P/b^k. Proto

```
|C(w)−N/b^k| <= (P+k−1)/b^k <= P/b < sqrt(N).
```

Druhá nerovnost je pro k=1 rovnost; pro k>=2 plyne z
k−1<=P(b^(k−1)−1). Pro k>r může dané k-slovo začínat nejvýše v jedné
fázi periody, protože jeho první r číslic již fázi určuje. Pak
C(w)<=ceil(N/P). Z testovaného b^k<=N zároveň plyne N/b^k>=1, takže
kladná odchylka nepřesáhne ceil(N/P)−1<=N/P<=sqrt(N). Záporná odchylka
nepřesáhne N/b^k<=N/(bP)<=sqrt(N)/b. Tím je Q1 dokázána obecně.

Kontrolní program sestavil 23 různých cyklů, každý ověřil výčtem všech
svých r-oken, a pak otestoval 4608 slov pro b=2,...,10 a N=1,...,512.
To je kontrola konstrukce, nikoli náhrada předchozího důkazu.

## 2. Q2 a Kolmogorovova mez (37)

Algoritmus smí adaptivně číst dosud nepřečtené pozice slova a před
přečtením rozhodnout, zda bit vybere. Q2 požaduje, aby každý takto
vybraný výstup délky m>=n měl podíl jedniček vzdálený od 1/2 nejvýše
epsilon. Algoritmus smí skončit podle již viděných hodnot.
Pro N=8, n=4, epsilon=1/8 a čtyři pravidla z knihy (všechny pozice,
sudé pozice při indexování od nuly, po nule, po jedničce) přesný výčet
256 slov dává 46 přijatých slov. Každá položka vytištěné tabulky i její
doplněk souhlasí.

Zde je vlastní důkaz meze (37), včetně adaptivního ukončování. Uvažujme
rovnoměrné náhodné vstupní slovo, kladné n a 0<epsilon<1/2. Vybrané
bity převedeme na hodnoty Y=−1,+1 a S_m označí jejich součet. Před
každým čtením nového bitu je jeho podmíněné rozdělení stále rovnoměrné,
ať algoritmus zvolil kteroukoli dosud neviděnou pozici.

Položme eta=2 epsilon, theta=atanh(eta) a

```
M = exp(theta S_m)/(cosh(theta))^m,
I(eta) = ((1+eta)ln(1+eta)+(1−eta)ln(1−eta))/2.
```

M má při každém kroku čtení nezměněnou podmíněnou střední hodnotu:
při přeskočení bitu zůstává stejné, při výběru se násobí faktorem
se střední hodnotou jedna. Takový proces se nazývá martingal.
Pokud kdykoli m>=n a S_m>=eta m, potom M>=exp(n I(eta)).
Zastavme proces při prvním takovém překročení, jinak po N čteních.
Jeho střední hodnota je stále jedna, takže pravděpodobnost překročení
je nejvýše exp(−n I(eta)). Stejně ošetříme zápornou odchylku.
Protože I(0)=I'(0)=0 a I''(eta)=1/(1−eta²)>=1, máme
I(eta)>=eta²/2 a pro každý algoritmus

```
Pr(odmítnutí Q2) <= 2 exp(−2 n epsilon²).
```

Součet těchto pravděpodobností pro nejvýše
(1/2) exp(2 n epsilon²(1−epsilon)) algoritmů nepřesáhne
exp(−2 n epsilon³)<1. Existuje tedy alespoň jedno slovo, které přijmou
všechny algoritmy. To dokazuje tištěnou mez. Pro epsilon=0 dovoluje
mez pouze prázdnou rodinu; pro epsilon>=1/2 přijmou všechna slova.

## 3. Úloha 38: přesná konečná formulace a meze

Označme B(N,n,epsilon) počet binárních slov délky N, jejichž nějaký
prefix délky m>=n má podíl jedniček mimo povolený interval. Největší
pravděpodobnost, s jakou může jediný algoritmus odmítnout rovnoměrné
N-bitové slovo, je přesně p=B/2^N. Horní mez plyne z nezávislých
vybíraných čerstvých bitů: vybráno je nejvýše N bitů a neúspěch je
možný jen při prvním průchodu jejich součtu přes hranici. Doplnění
nevybraného konce novými nezávislými bity dává celý férový náhodný
pochod. Rovnosti dosáhne algoritmus čtoucí všechny pozice po řadě
a končící při prvním odmítajícím prefixu.

Tedy každá rodina odmítající všechna slova potřebuje alespoň ceil(2^N/B)
algoritmů, pokud B>0. Počet B lze spočítat celočíselnou rekurzí pro
počty dosud nepřekročených prefixů podle délky a počtu jedniček.
Kontrola s přímým výčtem slov souhlasí ve 165 případech N<=10.
Samotný počet odmítaných slov ovšem neurčuje nejlepší pokrytí.

Lze také přesně rozhodnout, zda nějaké konečné pokrytí vůbec existuje.
Pro 1<=n<=N a 0<=epsilon<1/2 položme M=ceil(N/2). Pokrytí existuje
právě tehdy, když

```
epsilon < min(1/2, M/n−1/2).
```

Každé slovo má alespoň M stejných bitů. Při platnosti nerovnosti lze
zvolit n pozic s min(n,M) stejnými bity, které Q2 poruší. Rodina všech
pevných výběrů n pozic tedy stačí a dává horní mez binom(N,n).
Naopak u nejvyváženějšího slova nepřesáhne žádná podposloupnost délky
m>=n odchylku min(1/2,M/n−1/2), takže při neplatnosti ostré nerovnosti
je takové slovo neodmítnutelné. Pro n>N nebo epsilon>=1/2 pokrytí také
neexistuje. Tento okrajový režim není chybou výzkumné otázky.

Pro přesné malé případy program vyčísluje všechny adaptivní rozhodovací
stromy, sloučené podle množiny odmítaných vstupů. Stav (q,m,h) znamená
q nepřečtených pozic a dosud m vybraných bitů, z nichž h jsou jedničky.
Jestliže stav již porušuje Q2, okamžité zastavení odmítá všechny zbývající
vstupy. Jinak zvolíme jednu z q pozic, předem výběr či přeskočení,
a pro obě hodnoty bitu nezávisle zvolíme přípustné pokračování.
To je úplná rekurze všech povolených algoritmů. Množiny obsažené v jiné
množině lze pro účel minimálního pokrytí vypustit. Nad maximálními
množinami pak přesně hledáme nejmenší pokrytí všech 2^N vstupů.
Každý uchovaný rozhodovací strom je nezávisle spuštěn na všech vstupech;
celkem 6916 těchto kontrol. Maximální velikost odmítané množiny navíc
souhlasí s nezávislým výpočtem B.

Ve 20 případech N<=4, 1<=n<=N, epsilon v {0,1/4} vycházejí zejména
minima 3 pro (N,n,epsilon)=(3,2,1/4) a (4,2,1/4). Dolní objemová mez
zde dává jen 2. Horní meze 3 dosáhnou tři pravidla vybírající jednotlivé
dvojice ze tří pevných pozic: některá dvojice má stejné bity. Pro
(4,3,1/4) pokrytí neexistuje. Úplné výsledky jsou v JSON; nevyvozujeme
z nich obecnou asymptotiku ani dnešní otevřenost původního problému.

## 4. Délka nejkratšího programu

Délka programu zde znamená počet bitů vstupu pevného univerzálního
výpočetního stroje, jenž vytiskne celé konečné slovo a skončí.
Maximalizace této délky se týká zvlášť každé délky slova N;
nejde o tvrzení, že všechny prefixy jedné nekonečné posloupnosti
současně maximalizují obyčejnou programovou složitost.

Následující jednoduchý argument ověřuje kvalitativní tvrzení knihy.
Pro binární slova délky N existuje slovo s programovou složitostí
alespoň N: programů délky menší než N je jen 2^N−1. Je-li nějaká
vypočitatelně vyčíslitelná vadná množina těchto slov velikosti nejvýše
2^(N−d), lze její prvky popsat pořadím v jejím výčtu, N, d a programem
výčtu. Délka je nejvýše N−d+O(log N+log(d+1))+c, kde c závisí pouze
na testu. Velká rozpoznatelná vada proto vylučuje maximalitu složitosti.

Konkrétně fixujme délku k, k-slovo a kladnou odchylku delta od jeho
správné četnosti 2^(−k). Okna rozdělíme podle počátku modulo k;
v každé třídě jsou disjunktní, tedy jejich indikátory nezávislé.
Exponenciální odhad pro součet nezávislých omezených veličin dává,
po sjednocení k tříd a zanedbání k−1 koncových pozic, nejvýše
2^N exp(−c_(k,delta) N) vadných slov pro dostatečně velké N,
kde c_(k,delta)>0. Úspora v popisu je lineární v N a převáží
logaritmickou režii. Maximalizující slova proto pro každé pevné k
mají při N->nekonečno správné limitní četnosti všech k-slov.
Nejde o tvrzení, že splní každou libovolně předem určenou konečnou
hladinu významnosti každého myslitelného testu.

Primární Martin-Löfův článek (1966), strany 602–608, byl přečten.
Rozlišuje obyčejnou a podmíněnou složitost při známé délce slova;
svůj univerzální konečný test váže na druhou z nich s konstantní
chybou. Univerzálnost dovoluje posun hladiny závislý na konkrétním
testu. To vysvětluje kvalifikaci knihy o vhodném významu všech
vypočitatelných testů. Úvod i přesná věta odpovídají tomuto rozsahu.
Chaitinova citovaná práce z roku 1969 byla bibliograficky dohledána,
ale její plný text se v tomto bloku nečetl. Totéž platí pro další
citované Levinovy práce; bibliografie Zvonkin–Levin 1970 souhlasí
s primárním záznamem MathNet, jeho PDF vrátilo 403.
Neprohlašujeme nezávislou historickou prioritu ani nové ověření všech
teorémů těchto článků.

## Reprodukovatelnost

`verify_finite_randomness.py --resume` uchovává dokončené bloky.
`results/finite-randomness.json` obsahuje obě tabulky, kontrolu konstrukce,
přesné pravděpodobnosti zastavení i minimální pokrytí; log zaznamenává
čtyři úspěšné bloky. První běh (session 20707) skončil s kódem 0;
nově přidaný blok pokrytí byl spuštěn samostatně a také skončil 0.
Úspěšné předchozí bloky se neopakovaly. Původní články, adresy, otisky
a přesný rozsah čtení eviduje `sources/finite-randomness-sources.json`.
