# §4.5.2: Lehmer L, inverze a celočíselné rovnice

Originály 343–347, zadání 16–19 na 354 a odpovědi na 642 byly zobrazeny.
Čtyři vrstvy errat prohledány 2026-11-02. Oprava z 29. září 2001 mění
v druhém vzorci odpovědi 17 počáteční 1 na u; oprava z 14. září 1999
na str. 345 mění „integer variables“ na „integer values“.

## Proč funguje algoritmus L

Nechť b>=2 je základ soustavy, p>=1 počet cifer slova a W=b^p.
Jednoslovná nezáporná čísla jsou 0..W-1. V jednom bloku algoritmu
označme původní dvojici U>=V>=W a h=floor(U/b^k), j=floor(V/b^k),
kde k je nejmenší celé nezáporné číslo, pro něž h<W. Matice
`M=[[A,B],[C,D]]` sleduje celočíselné lineární kombinace původní dvojice;
na začátku je jednotková. Každý přijatý Eukleidův krok ji násobí zleva
maticí `[[0,1],[1,-q]]`, kde q je právě určený podíl. Determinant M
je tedy vždy 1 nebo -1; toto také znamená, že transformace má
celočíselnou inverzi a zachovává gcd.

Na začátku jsou dvě krajní dvojice `(h,j+1)` a `(h+1,j)`. Jejich poměry
ostře svírají U/V, neboť oba odříznuté zlomkové zbytky leží v [0,1).
Nulový j znamená horní krajní poměr +infinity. Po r přijatých krocích
jsou transformované krajní dvojice přesně

```text
(u',v')   = (h_r+B, j_r+D),
(u'',v'') = (h_r+A, j_r+C),
(h_r,j_r) = M*(h,j).
```

Je-li podlaha obou konečných krajních poměrů q, má stejnou podlahu
i pravý poměr. Zobrazení x -> 1/(x-q), které představuje Eukleidův
krok na poměrech, zachovává sevření a obrací jeho orientaci. Při shodě
obou podlah jsou krajní zbytky nezáporné a skutečný zbytek je kladný:
pravý poměr leží ostře uvnitř krajů, nemůže se rovnat dolní celistvé
hranici q. To dokazuje indukcí správnost celé simulované posloupnosti.
Při neshodě nebo nulovém krajním jmenovateli se simulace zastaví.

Obě krajní dvojice nemohou mít současně nulovou druhou souřadnici.
Jejich původní determinant je `-(h+j+1)`, tedy nenulový, a násobení
maticí M tuto nenulovost zachovává. Jejich první i druhé souřadnice
zůstávají nezáporné. Na začátku jsou u''<=W, v'<=W, u'<W, v''<W,
což jsou přesně nerovnosti (31). Po prvním přijatém kroku jsou již
všechny čtyři menší než W. Jedinou možnou překážkou by bylo původní
v'=W; tehdy h=j=W-1 a oba první podíly se neshodují, takže se žádný
krok nepřijme. Další zbytky jsou vždy menší než předchozí jmenovatele.

Koeficienty každého řádku M mají opačná znaménka, případně je jeden
na začátku nula. Proto

```text
|A|,|B| <= |A-B| = |u''-u'| < W,
|C|,|D| <= |C-D| = |v''-v'| < W
```

po prvním přijatém kroku. Počáteční koeficienty splňují meze přímo.
Také q<W: lze jej počítat z u'/v', kde u'<W a v'>=1. V aktualizacích
A-qC a B-qD se sčítají absolutní hodnoty; jednotlivé součiny qC,qD
proto nepřetečou, jestliže je výsledný nový koeficient menší než W.
Konečně q*j_r<=h_r<W, neboť simulovaný krok platí i pro prostřední
poměr h_r/j_r. Tím jsou prověřeny i dočasné součiny L3, nikoli jen
uložené výsledky.

Jediná možná hodnota W v L2 tedy nastává při původním h=W-1,A=1
nebo j=W-1,D=1, jak text uvádí. Přetečení musí implementace výslovně
ošetřit; přesný model níže je neignoruje a zaznamenává jeho výskyty.
Čitatel W lze při dělení kladným d vyřídit přes podíl a zbytek W-1,
zvýšením podílu právě při zbytku d-1. Jmenovatel W při této počáteční
konfiguraci vede rovnou k neshodě podílů.

B je nula právě tehdy, když nebyl přijat žádný krok. Po prvním kroku
je B=1, dále jeho absolutní hodnota tvoří kladné kontinuanty, tj.
rekurzi nová hodnota = q krát poslední + předposlední. L4 buď vykoná
alespoň jeden správný Eukleidův krok maticově, nebo jeden krok přímo.
Kladný druhý argument přitom klesne. Po konečně mnoha krocích se
vejde do slova a L1 dokončí obyčejný Eukleidův algoritmus. Platí
i nulové vstupy: ty se vyřídí přímo v L1, včetně gcd(0,0)=0.

## Nepřesné vysvětlení L4: C0121

Tvrzení, že B=0 implikuje velmi velký podíl, neplatí. Pro desetinné
čtyřciferné slovo, U=10001,V=10000, dostaneme k=1 a h=j=1000.
První dva testované podíly jsou `floor(1001/1000)=1` a
`floor(1000/1001)=0`. L4 proto provede plné dělení, ale U div V=1.
Stejný jev nastane pro každé W=b^p s U=W+1,V=W; když h=1,
první horní odhad je 2 místo 1, stále se však neshoduje s nulou.
Jde o chybu důvodového komentáře, nikoli návratové hodnoty algoritmu.
Nenahrazujeme ji tvrzením o četnosti tohoto jevu bez určení modelu vstupů.

Tištěný příklad 27182818,10000000 dává pět podílů 2,1,2,1,1,
matici `[-4,11;7,-19]` a novou dvojici 1268728,279726, přesně jako
v knize. Všechny jednotlivé krajní dvojice tabulky na 346 vzniknou
obyčejným dělením; další krajní podíly jsou 19 a 3. Výrok o 99.856 %
malých podílů na 345 patří k limitnímu rozdělení podílů v §4.5.3,
nikoli k libovolnému rozdělení první vstupní dvojice; úplný rozbor
tohoto limitního modelu zůstává v navazujícím oddílu.

## Úloha 18: rozšířený L

Pro vstupy U,V uchováváme trojice (a,b,r) s invariantem aU+bV=r,
zpočátku (1,0,U) a (0,1,V). Maticový blok L4 se aplikuje na každou
ze tří souřadnic se stejnými koeficienty A,B,C,D. Přímý krok používá
tytéž celočíselné řádkové operace. L1 při malém druhém zbytku provede
rozšířený Eukleidův algoritmus, opět včetně prvních dvou souřadnic.
Invariant a správnost třetí souřadnice dokazují odpověď 18 obecně.
Vnitřní test L2 ani simulace L3 se nemění. Při současném přiřazení
je nutné použít původní hodnoty obou řádků, jak zajišťují tištěné
pomocné proměnné t,w.

## Úloha 16: dělení modulo m

Pro kladné u,v,m s gcd(v,m)=1 vrátí rozšířený gcd koeficient x s
xv+ym=1. Potom `w=(u*x) mod m` leží v 0..m-1 a vw=u modulo m.
Je také jediné: rozdíl dvou řešení je po násobení x nulový modulo m.
Případ m=1 má jediné reziduum w=0 a všechny kongruence platí. Druhé
koeficienty rozšířeného algoritmu skutečně není třeba počítat.

Čas O(n²) pro vstupy s nejvýše n bity lze dokázat přímo. Po případném
počátečním prohození mají dva aktuální argumenty bitové délky s_i>=t_i;
položme delta_i=s_i-t_i. Dělení a aktualizace koeficientů školní
aritmetikou stojí O(n*(delta_i+1)), neboť podíl má nejvýše delta_i+1
bitů a Bézoutovy koeficienty nejvýše O(n) bitů (důkaz mezí je v
`gcd-basic.md`). Součet delta_i teleskopuje na nejvýše n a počet
kroků je O(n): každé dva kroky zmenší větší argument alespoň dvakrát.
Celkový součet je proto O(n²), stejně jako závěrečné násobení a redukce.

## Úloha 17: zdvojení přesnosti inverze

Označme M=2^e. Z uv=1 modulo M plyne
`1-v*(2u-vu²)=(1-vu)²=0 modulo M²`. Tedy první tištěný vzorec je
správný. Je-li `uv=1+M*w modulo M²`, dostaneme ekvivalentně
`2u-vu² = u-M*u*w modulo M²`, a tedy

```text
u' = u + M*((-u*w) mod M).
```

To je vzorec po známé opravě 2001. Původní počáteční 1 selže například
pro e=2,u=v=3,w=2: vrátí 9 a 3*9=11 modulo16; opravená hodnota 11
splňuje 3*11=1 modulo16. Pro u mimo základní interval vzorec nemusí
vracet nejmenší reziduum, ale požadovaná kongruence platí. Důkaz dovoluje
i záporná celá u,v; při e>=1 musejí být obě lichá. Triviální e=0 lze
vyřídit modulo1. Zmínka o tabulkovém startu e=8 či16 je s postupem
zdvojování přesnosti slučitelná.

## Celočíselné soustavy a úloha 19

Jedna transformace (25) má t=x0+sum floor(c_i/c)*x_i. Jde o bijekci
celých souřadnic, neboť zpětně x0=t-sum floor(c_i/c)*x_i. Substituce
ve všech rovnicích zachovává přesně množinu řešení. Rovnice (26)
obsahuje zbytky v 0..c-1 i při záporných původních koeficientech.
Je-li některý zbytek nenulový, nejmenší nenulový koeficient celé
soustavy klesne. Jsou-li všechny nulové, musí c dělit pravou stranu;
potom lze rovnici vydělit c a eliminovat proměnnou s koeficientem1.
Počet rovnic klesne. Uspořádaná dvojice (počet rovnic, nejmenší
nenulový koeficient) tedy lexikograficky klesá, což dokazuje ukončení.

Nulové řádky je třeba běžným způsobem odstranit, pokud mají pravou
stranu0, nebo označit neslučitelnost při 0=d!=0. Text tuto triviální
normalizaci nerozepisuje; není zde vykázána jako nová chyba.
Při dokončení jsou zbylé proměnné volné a zpětné bijektivní substituce
dají všechna celočíselná řešení, nikoli jen racionální parametrizaci.

V příkladu na343–344 je vytištěná parametrizace (23) správná. Z každého
původního řešení ji lze obrátit pomocí
`t1=3w+x+y+2z`, `t3=15w+7x+5y+15z`. Dosazení do obou rovnic i
obnovení obou parametrů platí identicky. Pro úlohu19 dává substituce
t=x+2y+3z rovnice `3t+y+2z=1`, `5t-3y-20z=±3`.
Eliminací y vznikne `14t-14z=6` v (a), což je neslučitelné, a
`14t-14z=0` v (b). V (b) proto t=z a všechna řešení jsou
`x=8z-2`, `y=1-5z`, z libovolné celé. Obě tištěné odpovědi správné.

## Reprodukovatelné kontroly

`verify_gcd_extensions.py --resume`, relace95648, exit0; všechny tři
checkpointy prošly. Výsledky v `results/gcd-extensions.json` a `.log`.
První běh43348 byl přerušen před dokončením prvního checkpointu kvůli
zbytečně pomalému opakovanému výpočtu mocniny b^k. Test nyní používá
předchozí mocninu a nezávisle kontroluje přesnou minimalitu k. Přerušení
bylo ukončeno kódem130, nikoli vydáváno za úspěšný test.

- 132610 dvojic, osm konfigurací slov v základech2,3,10,64,100,
  úplné malé trojúhelníky do180 a800 náhodných dvojic do2048 bitů.
  Každý přijatý podíl se porovnává se skutečným dělením původních
  velkých zbytků; konečný gcd s knihovním gcd a koeficienty přímým
  dosazením do Bézoutovy identity. Kontrolováno510837 vnitřních testů,
  113728 simulovaných kroků, všechny krajní meze a dočasné součiny.
- 30035 modulárních dělení porovnáno také s nezávislou vestavěnou
  modulární inverzí;1633 Newtonových případů zahrnuje jiné reprezentanty,
  záporná čísla a přesnosti až1024 bitů. Známá chyba2001 reprodukována.
- 2428 soustav:3789 bijektivních transformací,119260 omezených vektorů,
  z nich2253 řešení. Každé nalezené řešení projde inverzním převodem na
  volné parametry a obnoví se přesně. Výstupní posun splňuje původní
  rovnice a každý sloupec parametrizace jejich homogenní část.
  Celkem896 soustav rozpoznáno jako neslučitelných. Konečný test
  nedokazuje obecnou úplnost sám; tu zajišťují bijekce výše.

Lehmerovu bibliografii potvrzuje
[vydavatelský záznam](https://doi.org/10.1080/00029890.1938.11990797):
AMM45 (1938),227–233. Úplný článek se nepodařilo přečíst; metadata
a omezený rozsah první stránky ve webovém výpisu jsou v
`sources/lehmer-1938-access.json`. Důkaz L zde stojí samostatně na
originálu knihy, nikoli na domnělém přečtení tohoto článku.
