# §4.5.3-39/40: zlomky v intervalu a Sternův–Brocotův strom

Matematická část úlohy 40 je dokázána níže. Úloha 39 má
správný výsledek 287, známou textovou opravu z roku 2000
a nový nález C0138 v obecném postupu; viz samostatnou poznámku.
Historický odstavec odpovědi 40 má známé opravy z let 2000
(Brocotův svazek a rok) a 2017 (Eisensteinova dřívější práce).
Rozsah historických pramenů uvádí část 5.

## 1. Sousední meze a vložený zlomek

Zlomek p/q znamená poměr celého čitatele p a kladného celého
jmenovatele q; budeme používat zkrácený tvar gcd(p,q)=1.
Pomocná pravá mez 1/0 značí kladné nekonečno.

Uzel stromu má levou mez a/b a pravou mez c/d, které jsou
nejbližšími příslušnými předky. Začínáme mezemi 0/1 a 1/0.
Jeho značkou je mediant, tedy zlomek vytvořený sečtením
čitatelů a jmenovatelů:

```
M=(a+c)/(b+d).
```

Levé dítě používá meze (a/b,M), pravé (M,c/d). Indukcí platí

```
bc-ad=1.                                             (S1)
```

Je to pravda na začátku a oba nové determinanty se rovnají
starému. Společný dělitel a+c a b+d by dělil i
(a+c)d-c(b+d)=ad-bc=-1. Každý mediant je proto zkrácený.
Navíc a/b<M<c/d. Všechny značky v levém podstromu uzlu
jsou menší než jeho značka, v pravém větší. Symetrický průchod
stromem, tedy levý podstrom, uzel, pravý podstrom, se tak
shoduje s rostoucím pořadím racionálních hodnot.

## 2. Každý kladný zlomek se vyskytne právě jednou

**Myšlenka.** Při hledání daného p/q zapisujeme jeho čitatel
a jmenovatel jako kladnou celočíselnou kombinaci aktuálních
mezí. Cesta stromem pak odčítá menší koeficient od většího,
a proto musí skončit.

Nechť a/b<p/q<c/d a gcd(p,q)=1. Položme

```
alpha=cq-dp,        beta=bp-aq.
```

Obě čísla jsou kladná celá a z (S1) dostáváme

```
p=alpha*a+beta*c,   q=alpha*b+beta*d.                 (S2)
```

Matice mezí je celočíselná s determinantem -1, takže
navíc gcd(alpha,beta)=gcd(p,q)=1. Porovnání s mediantem dává

```
p(b+d)-q(a+c)=beta-alpha.
```

Je-li p/q<M, přejdeme vlevo a nové koeficienty jsou
(alpha-beta,beta). Je-li p/q>M, přejdeme vpravo a nové
koeficienty jsou (alpha,beta-alpha). Dokud se nerovnají,
zůstávají kladné a jejich součet ostře klesá. Nakonec jsou
oba rovny 1 a p/q=M. Na začátku jsou (alpha,beta)=(q,p),
takže argument platí pro každý kladný zkrácený zlomek.

Jednoznačnost plyne ze striktního uspořádání podstromů:
nejbližší společný předek dvou různých uzlů odděluje jejich
hodnoty, případně jeden z uzlů je předkem druhého.

## 3. Cesta a řetězový zlomek

Písmena L,R značí krok vlevo či vpravo. Zápis L^h znamená
h opakování tohoto kroku, s prázdným slovem pro h=0.
Pro kanonický rozvoj

```
p/q=[c_0;c_1,...,c_t],
```

kde c_0>=0 a poslední člen c_t>=2 pro t>=1, je cesta

```
R^(c_0) L^(c_1) R^(c_2) ...,
```

s exponentem posledního neprázdného bloku sníženým o 1.
Pro kladné celé číslo h je tedy cesta R^(h-1).
To plyne přímo ze součinitelů (alpha,beta) v (S2):
počet po sobě jdoucích odečtení určuje příslušný Eukleidův
podíl, ale při posledním kroku skončíme už na rovnosti 1=1,
nikoli dalším odčítáním do nuly.

Pro p/q<1 lze totéž psát pomocí rozvoje s poslední jedničkou
[0;a_1,...,a_r,1]. Cesta je přesně L^(a_1) R^(a_2) ...,
protože poslední jednička se zmenší na nulový blok. To je
formule v odpovědi. Čísla nad 1 dostaneme převrácením
zlomku a záměnou L,R; uzel 1/1 je kořen s prázdnou cestou.
Tím jsou výslovně zahrnuty i tyto okrajové případy.

## 4. Nejmenší jmenovatel v intervalu

Pro 0<u<v<1 postupujeme od kořene:

- Je-li mediant menší než u, pokračujeme vpravo.
- Je-li větší než v, pokračujeme vlevo.
- Je-li v [u,v], vrátíme jej.

Celý interval zůstává mezi aktuálními mezemi. Postup skončí,
protože interval obsahuje racionální číslo p/q a jeho konečná
vyhledávací cesta z části 2 prochází týmiž uzly až do prvního
zásahu intervalu.

Každý racionální bod p/q v aktuálním intervalu má vyjádření
(S2) s alpha,beta>=1. Proto

```
q=alpha*b+beta*d >= b+d.                              (S3)
```

První zasažený mediant má právě jmenovatel b+d, a je tedy
optimální. Protože v<1, před prvním zásahem jsme alespoň
jednou šli vlevo; aktuální b,d jsou oba kladné. Rovnost
v (S3) pak vynucuje alpha=beta=1. Výsledek je jediný
zlomek s minimálním jmenovatelem v intervalu.

Stejný stromový postup funguje s otevřenými konci, jestliže
podle toho upravíme porovnání; pro interval s kladnou délkou
zůstává konečnost i důkaz minima platný. U baseballového
příkladu 96/287 leží ostře uvnitř, a proto na konvenci
zaokrouhlování přesné půlky nezáleží.

Opravená verze řetězového postupu v C0138 dává tentýž
výsledek; jeho prefixový kraj odpovídá uzlu stromu, který
leží přímo na zahrnutém konci intervalu.

## 5. Historický kontext: doložený rozsah a otevřené prameny

Vizuálně přečteny původní strany 378,654,655 a příslušné
opravy podle inventáře. Oprava z 2017 připisuje dřívější
popis Eisensteinovu dopisu Sternovi ze 14. ledna 1850;
oprava z 2000 mění Brocotovu citaci na svazek 3 (1861).

Sternův originál *Ueber eine zahlentheoretische Funktion*,
Crelle 55 (1858), 193–220, byl získán z digitalizace GDZ;
vizuálně přečteny strany 193, 194 a 220. Na straně 193 sám
Stern výslovně připisuje objev Eisensteinovi a zmiňuje jeho
dopis ze 14. ledna v kontextu roku 1850. To přímo podporuje
známou opravu priority z roku 2017, i když samotný dopis na
straně 819 sebraných spisů zatím přečten nebyl. Strana 194
definuje opakované vkládání součtů mezi sousední členy.
Na poslední straně stojí autorské datum červenec 1855;
odlišuje se od roku vydání 1858 a není chybou knižní citace.
Netvrdíme, že byl prověřen celý Sternův článek.

Gallica pro původní Brocotův svazek vrátila HTTP 403;
přístupová překážka nebyla obcházena. Úplné doložení
poznámek o Schwenterovi, Wallisovi, Huygensovi, Lagrangeovi,
dobových hodinářských publikacích a Lehmerovi není nahrazeno matematickým důkazem
stromu. Tento rozsah zůstává ve frontě kontextu oddílu.

## 6. Přesná nezávislá validace

Program verify_euclid_stern_brocot.py porovnal opravené
řetězové pravidlo a stromový postup s přímým procházením
jmenovatelů. Všech 15931 intervalů mezi 179 racionálními
kraji se jmenovateli nejvýše 24 prošlo. Původní předpis
selhal na 131 intervalech, přesně v prefixových případech.
Dalších 961 členů obecné rodiny C0138 prošlo, stejně jako
nezávislá kontrola baseballového minima a jeho čitatele.

Pro všech 10043 kladných nesoudělných dvojic p,q<=128 byla
cesta přímým porovnáváním mediantů totožná s cestou z
Eukleidových podílů. Všech 181714 přechodů ověřilo kladné
celočíselné souřadnice, unimodularitu a klesající součet.
Konečný strom s 2047 uzly má zkrácené a ostře uspořádané
značky; první tři úrovně souhlasí se zadáním.

Běh 82194, PID 1223915, limit 120 sekund, exit 0, čas
1.47 sekundy. Výpočty doplňují obecné důkazy v částech 1–4
a C0138; historická tvrzení jimi nejsou testována.
