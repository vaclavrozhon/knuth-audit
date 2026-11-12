# §3.5 A/B: distribuce posloupností a první úlohy

Stav 1. listopadu 2026. Uzavřen matematický blok str.149–158, úlohy
1–18,22–25,28 a odpovídající odpovědi592–596. Výzkumná úloha17 je uzavřena
jen jako kontrola formulace a doloženého publikovaného stavu; nebyla vyřešena.
Na str.159 zatím přečten úvod C; ostatní text a ostatní úlohy tímto neuzavíráme.
Inventář44 původních úloh potvrzen v sazbě179–183; žádná další úloha nebyla
nalezena ve čtyřech vrstvách errat. Nové chyby V2-C0059 a V2-C0060 níže.

Doklady: obrázky149–159,179–183,592–597; mapa tištěná strana +12.
Originál je třetí vydání, první tisk ze září1997. Kontrolovány
`all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální `sources/err2.textxt`.
Fyzický poslední dotisk ani prvenství nových nálezů neověřeny. Nic neodesláno.

## 1. Definice a rozsah tvrzení

Přirozená hustota tvrzení S(n) je limita počtu jeho platných výskytů pro
0<=n<N, děleného N. Kniha ji značí Pr(S(n)); nejde zde o náhodný výběr n
z neexistujícího rovnoměrného rozdělení na všech celých číslech.
Dolní a horní hustota znamenají liminf a limsup téhož podílu.
Konečná aditivita platí; spočetná obecně neplatí, jak ukazuje úloha6 níže.

Posloupnost U_n v [0,1) je k-distribuovaná, když každá podmínka
u_i<=U_(n+i)<v_i pro i=0,...,k−1 má hustotu prod_i(v_i−u_i),
kde 0<=u_i<=v_i<=1. Je tedy rovnoměrně rozdělená současně v každém
okně délky k. Pro k=1 užíváme též „ekvidistribuovaná“.
Posloupnost je nekonečně distribuovaná, splňuje-li to pro všechna konečná k.
Pro b-ární posloupnost X_n, tj. symboly0,...,b−1, se požaduje četnost
b^(−k) každého slova délky k. (m,k)-distribuce navíc požaduje stejnou
vlastnost při omezení začátků oken na libovolnou třídu n modulo m.

Projekce souřadnic a konečné sjednocení tříd dokazují všechny elementární
implikace mezi definicemi. Konečná změna počátečních členů nezmění žádnou
hustotu. Každé pevné slovo s kladnou předepsanou hustotou se musí objevit
nekonečněkrát: dlouhé běhy stejných symbolů nejsou v rozporu s distribucí.
Příklad střídání dolní a horní poloviny na str.151 je ekvidistribuovaný,
ale zakazuje sousední členy v téže polovině; tedy není2-distribuovaný.

## 2. Věta A a V2-C0059: záporné délky v důkazu

Věta A převádí k-distribuci číslic floor(b_j U_n) pro neomezené základy
b_j na k-distribuci reálných U_n. Výrok je správný. Důkaz na str.153
však bez omezení používá produkty délek i pro prázdné vnitřní intervaly
a pro vnější intervaly přesahující1. Výslovně tvrdí platnost pro všechna b_j.

Nejkratší protipříklad k tištěné rovnosti: k=2, b=2, u_1=u_2=0,
v_1=v_2=1/4. Potom u'_i=v'_i=0. Každý vnitřní interval je [1/2,0),
tedy prázdný. Pravděpodobnost souběhu je0, ale tištěný součin je
(−1/2)^2=1/4. To nezávisí na volbě posloupnosti. Pro vnější rovnost
stačí k=1,u=0,v=1,b=2: událost U_n v [0,3/2) má pravděpodobnost1,
nikoli tištěných3/2.

Přímá oprava používá mřížkové intervaly s krajními body v [0,1]:

```
I_i = [ceil(b*u_i)/b, floor(b*v_i)/b), případně prázdný;
O_i = [floor(b*u_i)/b, ceil(b*v_i)/b).

vol(I) = prod_i max(0, floor(b*v_i)/b - ceil(b*u_i)/b),
vol(O) = prod_i (ceil(b*v_i)/b - floor(b*u_i)/b).
```

Součin I_i je uvnitř cílového boxu, ten je uvnitř součinu O_i.
Jejich hustoty jsou uvedené nezáporné objemy, protože oba jsou konečným
sjednocením mřížkových buněk. Každá délka se od v_i−u_i liší nejvýše2/b;
produkty tedy konvergují ke správnému objemu. Tím je věta dokázána i pro
nulové délky a krajní body0,1. Jde o lokální chybu důkazu, ne o neplatnou větu.

Na str.153 opravují errata2019 pouze „integer sequences“ na „2^j-ary
sequences“. Žádná ze čtyř vrstev ani aktuální TeX neopravuje uvedené součiny.
ASCII návrh: `reports/C0059-distribution-grid-bounds-draft.txt`.

## 3. Věta B a důsledky P/S

Věta B říká, že průměr omezené Riemannovsky integrovatelné funkce f
na po sobě jdoucích k-ticích konverguje k jejímu integrálu přes jednotkovou
krychli. Pro schodovité funkce na konečném rozkladu do boxů jde o konečnou
linearitu hustot. Obecné f sevřeme mezi dolní a horní schodovitou funkcí,
jejichž integrály se liší o méně než libovolně malé epsilon. To je přímo
Darbouxova charakterizace Riemannova integrálu. Důkaz v knize souhlasí.

Indikátor oblasti s hranicí nulového objemu je přípustný. Zvláště k!
oblastí různých pořadí k souřadnic má stejný objem1/k!; rovnosti souřadnic
leží na konečně mnoha hyperrovinách nulového objemu. To dokazuje důsledek P.
Pro důsledek S, při pevném kladném posunu h, jsou průměry U_n a U_(n+h)
rovny1/2, průměr U_n^2 je1/3 a průměr U_n U_(n+h) je1/4. Čitatel
centrované sériové korelace konverguje k0 a jmenovatel k1/12.
Není dovoleno vyvozovat nezávislost ze samotné nulové korelace; úlohy26/27
budou kontrolovány samostatně.

## 4. Věta C: rozdělení v aritmetických podposloupnostech

Věta C tvrdí, že nekonečně distribuovaná posloupnost je (m,k)-distribuovaná
pro všechna kladná m,k. Stačí dokázat (m,m) pro všechna m: (mk,mk)
lze projektovat na prvních k souřadnic a sloučit třídy modulo mk do tříd
modulo m. Věta A převede číslicový důkaz zpět na reálná čísla.

Následuje samostatný důkaz, který zároveň reprodukuje mez(25).
Fixujme b-ární slovo w délky m a položme p=b^(−m). I_n je indikátor,
že w začíná v n. Pro libovolné kladné L položme q=Lm a
Z_n=(I_n+I_(n+m)+...+I_(n+(L−1)m))/L. Nekonečná distribuce určuje
všechny společné četnosti těchto konečných, nepřekrývajících se oken:

```
lim avg_n Z_n = p,
lim avg_n (Z_n-p)^2 = p(1-p)/L.
```

Pro j=0,...,m−1 označme p_j(N) průměr I_n na n<N,n=j mod m.
Průměr Z_n na stejné třídě se liší o O(q/N); pevné posunutí pouze
vymění členy u krajů. Jensenova nerovnost pro čtverec dává
limsup sum_j(p_j(N)−p)^2 <= m*p*(1−p)/L. Pro libovolně velké L
musí každý p_j(N) konvergovat k p. Tím je věta C dokázána.

V notaci knihy je y_j počet výskytů ve třídě dělený N, tedy
p_j/m+O(1/N). Předchozí výpočet dává přesně

```
limsup sum_j y_j^2 <= p^2/m + p(1-p)/(m*L)
                     = (q-m)/(q*m*b^(2m)) + 1/(q*b^m).
```

To je(25). Čtení původních stran156–158 a kontrola vážených součtů(20)–(25)
souhlasí. Podmínka m|q je použita v aritmetickém součtu(22), jak správně
uvádí odpověď10. Lemma E je důsledek
sum_j(y_j−a)^2=sum_j y_j^2−2a sum_j y_j+ma^2: za jeho předpokladů
má nezáporná levá strana horní limitu0, takže každé y_j konverguje k a.

Primární Niven–Zuckerman, *On the Definition of Normal Numbers*,
Pacific J. Math.1 (1951),103–109:
[PDF vydavatele](https://msp.org/pjm/1951/1-1/pjm-v1-n1-p10-p.pdf).
Přečten text103–109, zejména převod mezi překrývajícími a blokovými
četnostmi a kvadratický odhad; špatné OCR vzorců není podkladem numerické
transkripce. Vlastní výpočet výše a původní sazba Knutha nesou přesný důkaz.
PDF, text a SHA-256 uloženy v `sources/niven-zuckerman-1951-normal.*`.

## 5. Úlohy1–12: hustoty a elementární důsledky

1. Periodická b-ární posloupnost může být ekvidistribuovaná, např.
opakování0,...,b−1. Periodická reálná posloupnost má konečně mnoho hodnot,
proto mine nějaký interval kladné délky a ekvidistribuovaná být nemůže.
2. Perioda0011 má obě číslice po dvou a každou binární dvojici jednou;
není3-distribuovaná, protože například111 chybí.
3. Použije se již obecně i přesným soupisem ověřená ternární de Bruijnova
perioda délky27 z §3.2.2-17; viz `results/complete-sequences.json`.
Není třeba opakovat dříve úspěšný soupis.
4. Identita indikátorů průniku a sjednocení je přesná pro každé n.
Existence libovolných tří ze čtyř limit tedy zajistí existenci čtvrté a vztah.
5. Pro U_n=(2^floor(log2(n+1))/3) mod1 se střídají konstantní bloky
hodnot1/3 a2/3 délek1,2,4,8,... . Počet nu(N) hodnot pod1/2 splňuje
nu(2^(2k−1)−1)=nu(2^(2k)−1)=(2^(2k)−1)/3. Podíly mají dílčí limity2/3
a1/3, takže přirozená hustota neexistuje. Závorkový odkaz na logaritmickou
pravděpodobnost1/2 bude mít kontext v §4.2.4; nejde o přirozenou hustotu.
6. Konečná aditivita a monotonicita dolní hustoty dávají dolní hustotu
spočetného sjednocení alespoň součet hustot. Ostrý protipříklad k rovnosti:
S_j(n) znamená n=j−1; každý má hustotu0, sjednocení hustotu1.
Známé erratum2005 mění chybný odkaz v odpovědi593 z úlohy5 na4.
7. Označme p_ij jednotlivé hustoty a p_i=sum_j p_ij. Podle6 má řádek i
dolní hustotu alespoň p_i; jeho doplněk má dolní hustotu alespoň
sum_(h!=i),j p_hj=1−p_i. Horní hustota řádku je proto nejvýše p_i.
Existence a hodnota všech řádkových hustot tím plyne bez neplatné výměny limit.
8. Sloučení m/d tříd pro d|m zachová rovnoměrné četnosti.
9.–10. Viz důkaz a lemma v oddílu4.
11. Okenní k-tice U_2n,U_(2n+2),... vznikne projekcí (2,2k−1)-distribuce.
12. Objem oblasti u<=max(x_1,...,x_k)<v je v^k−u^k; věta B nebo
rozdíl dvou boxů dává tvrzení.

## 6. Úlohy13–16: mezery, běhy a kupony

13. Pro interval A délky p>0 má vzor „člen v A, k−1 členů mimo A,
člen v A“ hustotu p^2(1−p)^(k−1). Konce mezer mají hustotu p.
Při přechodu z indexu původní posloupnosti na pořadí nalezených konců
proto dostaneme p(1−p)^(k−1). Umělá počáteční hodnota f(0)=0 ovlivní
nejvýše jednu mezeru a v limitě nezáleží na tom, zda U_0 leží v A.

14. Pro běh délky k je potřeba sestup, k členů ve vzestupném pořadí,
a další sestup. V k+2 nezávislých spojitých souřadnicích má tato oblast objem
k/(k+1)!−(k+1)/(k+2)!. Například lze začít pravděpodobností1/k!
prostředního vzestupu, odečíst dvakrát1/(k+1)! a přičíst1/(k+2)!;
to je tentýž výraz. Hustota sestupů je1/2, tedy rozdělení délek běhů
je dvakrát uvedená hodnota. Množina rovností má hustotu0 a krajní
neúplný běh neovlivní limitu. Konečná kontrola všech46 230 permutací
pro k=1,...,6 souhlasí s nezávislým počítáním pořadí.

15.–16. Stav sbírky je vlastní podmnožina S z b druhů, které už byly
získány od posledního ukončení. Při doplnění posledního chybějícího druhu
se stav resetuje na prázdnou množinu. Není předem dovoleno předpokládat,
že volba začátků podle celé minulosti zachovává nezávislost; právě to
zajišťuje následující synchronizační argument.

Stanleyho slovo W=(b−1,b−2,...,0,0,1,...,b−1), délky2b, vždy
zanechá prázdný stav. V první sestupné polovině musí nějaká sbírka skončit.
Nechť j je číslice posledního takového resetu v první polovině. Následují
menší číslice a pak vzestupná polovina. Nová sbírka nemůže skončit dříve
než na závěrečném b−1 a tam určitě skončí. To platí pro každý vstupní stav.

Pravděpodobnost, že v posledních M pozicích nebylo žádné W, je nejvýše
(1−b^(−2b))^floor(M/(2b)): stačí kontrolovat pevná nepřekrývající se
okna, jejichž společné četnosti udává nekonečná distribuce. Tato mez jde
k0. Mimo množinu této malé hustoty je stav před aktuální pozicí určen
jen konečnou minulostí délky M. Proto existují jeho četnosti a každé
pevné budoucí slovo je na tomto stavu nezávislé: pro konečnou minulost
jde o četnosti delšího slova, zbytek je omezen předchozí mezí.

Označme pi_s četnost stavu s právě s druhy, 0<=s<b. Přechody z velikosti s
zůstávají na s s pravděpodobností s/b, přecházejí na s+1 s pravděpodobností
(b−s)/b; z b−1 přechází doplnění na0. Ve stacionárním toku musí být
pi_s*(b−s)/b stejná hodnota lambda pro všechna s. Normalizace dává

```
H_b = 1 + 1/2 + ... + 1/b,
pi_s = lambda*b/(b-s),
lambda = 1/(b*H_b).
```

Lambda je kladná hustota konců a začátků sbírek. Po daném začátku
počet slov, která poprvé dokončí všech b druhů přesně v kroku k, je
b!*S(k−1,b−1). Zde S(r,j) značí Stirlingovo číslo druhého druhu:
počet rozkladů r označených pozic do j neprázdných skupin. Poslední druh
lze vybrat b způsoby; předchozích b−1 druhů musí vytvořit surjekci z k−1
pozic, což dává (b−1)!*S(k−1,b−1). Vydělením b^k dostaneme standardní
kuponový zákon pro k>=b. Podíl hustoty začátků s danou délkou a lambda
převádí tuto hodnotu na četnost mezi samotnými sbírkami.

Pro b=2 jde o2^(1−k), průměrná délka3 a lambda=1/3, jak požaduje15.
Tištěná alternativa s pravděpodobnostmi p_st a q_t používá poslední pár
stejných bitů před střídajícím se ocasem; nekonečně střídající ocas má
nulovou hustotu. Její součty dávají2/3 pro nezačátek sbírky a
(1/3)*2^(−s−1) pro začátek délky s+2. Souhlasí s obecným důkazem výše.

Přesné doplňkové kontroly: všech501 vlastních stavů pro b=2,...,8;
stacionární rozdělení na všech podmnožinách
pi(S)=1/[H_b*(b−|S|)*binom(b,|S|)];97 632 kuponových slov v18
úplných souborech pro b=2,...,4,k=b,...,8. Nejde o náhradu obecného důkazu.

## 7. Úlohy22–25: Fourierovo kritérium a diference

Označme e(t)=exp(2*pi*i*t). Weylovo kritérium22 říká: k-distribuce je
ekvivalentní nulovým limitám průměrů e(c_1 U_n+...+c_k U_(n+k−1))
pro každý nenulový celočíselný vektor c. Nutnost je věta B a integrál
komplexní exponenciály. Pro opačný směr platí správná limita nejprve pro
konečné trigonometrické polynomy, tedy konečné lineární kombinace těchto
exponenciál. Fejérova konvoluce, kladné aproximační jádro s hmotou
soustředěnou u0, aproximuje každou spojitou periodickou funkci stejnoměrně.
Indikátor boxu lze sevřít mezi spojité periodické funkce s libovolně malým
rozdílem integrálů, protože jeho hranice má nulový objem. Sevření pak dá
četnost boxu. Nejde o nepravdivou stejnoměrnou aproximaci nespojitého
indikátoru. Tištěná formulace o hladkých aproximacích dovoluje právě toto
integrální sevření; v tomto smyslu je důkaz správný.

23(a) následuje použitím22 na všechna celočíselná lineární spojení.
Pro23(b) pozor na složené b: gcd(c_1,...,c_k)=1 neznamená, že některý
koeficient je invertibilní modulo b. Bézoutova identita ale zaručí, že
zobrazení (Z/bZ)^k -> Z/bZ, x -> c*x, je surjektivní; každé vlákno
má b^(k−1) prvků. Tím plyne nutnost. Obráceně vezměme libovolný nenulový
vektor a s reprezentanty0,...,b−1. Napišme a=g*c, kde g je gcd jeho
nenulových souřadnic a c má gcd1. Protože1<=g<=b−1, rovnoměrnost c*X
modulo b vynuluje průměr e(g*(c*X)/b). Tedy všechny netriviální Fourierovy
koeficienty v konečné grupě jsou0; konečná Fourierova inverze dává
rovnoměrnost všech k-tic. To dokazuje i složené základy bez dalšího předpokladu.

24(a). Fixujme nenulové celé c, z_n=e(c U_n) a A_N=N^(−1)sum_(n<N)z_n.
Průměr K posunutých verzí A_N se od A_N liší o O(K/N). Cauchyho nerovnost
na jejich blokové součty dává pro pevné K

```
limsup |A_N|^2 <= 1/K
  + (2/K^2) sum_(0<=j<k<K) Re lim avg_n z_(n+k)*conj(z_(n+j)).
```

Každá křížová limita je0 díky ekvidistribuci rozdílu kladného posunu k−j.
Potom K->infinity a22 dokazují tvrzení. Pro24(b) diference polynomu
stupně d s iracionálním vedoucím koeficientem má stupeň d−1 a vedoucí
koeficient d*h*alpha_d, stále iracionální. Indukce končí geometrickým
součtem v případě d=1. Rozšíření v odpovědi596 na libovolný iracionální
nekonstantní koeficient: vybereme nejvyšší takový stupeň a rozdělíme n
modulo společný jmenovatel všech vyšších racionálních koeficientů.
Na každé třídě jsou vyšší racionální členy konstantní modulo1 a zbývající
polynom má iracionální vedoucí koeficient. Konečné sloučení tříd dokončí důkaz.

25. Bílá posloupnost znamená nulové sériové korelace při každém kladném
posunu. Za ekvidistribuce jmenovatel korelace konverguje k1/12, kdežto
průměr (U_n−1/2)(U_(n+h)−1/2) se od čitatele liší o o(1).
Nulová limita uvedených součinů je tedy nutná a postačující. Vyžaduje se
h>=1; h=0 by mělo limitu1/12.

## 8. Věta F a výzkumná úloha17

Věta F tvrdí, že (theta^n mod1) je nekonečně distribuovaná pro téměř
všechna theta>1; „téměř všechna“ znamená mimo množinu Lebesgueovy míry0.
Uvádíme úplný samostatný důkaz, nikoli extrapolaci konečného experimentu.

Podle22 stačí pro každý nenulový celočíselný polynom P dokázat
N^(−1)sum_(n<N)e(theta^n P(theta))->0 pro téměř všechna theta>1.
Mimo konečně mnoho kořenů P pokryjeme oblast spočetně mnoha kompaktními
intervaly [a,b], a>1, na nichž má P stálé nenulové znaménko. Případným
nahrazením P za−P máme P>=delta>0. Položme B_1=max|P'| a B_2=max|P''|
na tomto intervalu. Pro m>n>=0, d=m−n, r=theta^(−d) a
g(theta)=(theta^m−theta^n)P(theta) máme

```
g' = theta^(m-1)*[(m-n*r)*P + theta*(1-r)*P'],
g'' = theta^(m-2)*[(m*(m-1)-n*(n-1)*r)*P
              + 2*theta*(m-n*r)*P' + theta^2*(1-r)*P''].
```

Platí m−n*r>=m*(1−1/a), dále
m*(m−1)−n*(n−1)*r >= (m−1)*(m−n*r), a1−r<=(m−n*r)/m.
Proto pro všechna dostatečně velká m, stejnoměrně v n<m, je

```
g' >= (delta/2)*m*(1-1/a)*a^(m-1),
g'' >= 0.
```

Druhá nerovnost plyne z dolního odhadu hranaté závorky druhé derivace
pomocí (m−n*r)*[delta*(m−1)−2*b*B_1−b^2*B_2/m]. První derivace
je tedy kladná, monotónní a exponenciálně velká. Integrace po částech
s e(g)/(2*pi*i*g') dá

```
|integral_a^b e(g(theta)) dtheta| <= C/(m*a^(m-1)),
```

kde C nezávisí na m,n. Hraniční členy a celková variace1/g' jsou společně
nejvýše2/min(g'), před dělením2*pi. Součet těchto odhadů přes n<m
a všechna m je konečný; konečný počet malých m se absorbuje do konstanty.
Po rozvinutí čtverce proto

```
integral_a^b |N^(-1)sum_(n<N)e(theta^n P(theta))|^2 dtheta
    = (b-a)/N + O(N^(-2)).
```

Pro N=j^2 je řada integrálů konečná. Nezápornost a Tonelliho věta
pak dávají konečnou řadu čtverců průměrů pro téměř každé theta,
a tedy jejich konvergenci k0. Mezi j^2 a(j+1)^2 se průměr jednotkově
omezených členů mění nejvýše o O(1/j); limita tudíž platí pro všechna N.
Spočetné sjednocení výjimek přes polynomy P a intervaly má míru0.
To dokazuje F.

Je-li theta algebraické, nějaký nenulový celočíselný P splňuje P(theta)=0;
odpovídající Weylův průměr je stále1, nikoli0. Nekonečná distribuce proto
není možná. Pro r=p/q racionální stačí P(t)=qt−p stupně1: posloupnost
(r^n mod1) není2-distribuovaná. Jde o první, vyřešené tvrzení úlohy17.
U r=0 je případný člen0^0 pouze počáteční konvence a výsledek nemění.

Otázka ekvidistribuce jednotlivých racionálních mocnin, zejména(3/2)^n,
zde vyřešena nebyla. Omezená rešerše1.11.2026 nenašla řešení.
Dubickasův primární článek2023 uvádí již pro hustotu takových posloupností
zásadní otevřené obtíže, viz úvod na první straně
[Density of Some Special Sequences Modulo1](https://epublications.vu.lt/object/elaba:164926835/164926835.pdf).
Novější článek2025, úvod str.1–2,
[Numbers Whose Powers Are Arbitrarily Close to Integers](https://epublications.vu.lt/object/elaba:247717971/247717971.pdf),
rozlišuje metrické výsledky pro téměř všechny parametry a dosud nevyřešený
Mahlerův problém Z-čísel. Ten je příbuzný, ale není totožný s otázkou
rovnoměrnosti(3/2)^n. Tyto prameny nedávají řešení17; evidence je časově
omezená rešerše, ne důkaz neexistence novější publikace. Souhrnná metadata
jsou v `sources/distribution-research-status.json`.

Franklinův primární PDF se nepodařilo získat: AMS403, alternativní host
nedostupný. Přesné pokusy jsou v `sources/franklin-1963-deterministic.json`.
Jeho článek proto není označen jako přečtený; matematický závěr F nese
vlastní důkaz výše. Historické prvenství nebylo nezávisle prokázáno.

## 9. Úloha18: malá změna členů

Pro n>=1 platí0<=U_n−floor(n U_n)/n<1/n; V_0 zvolíme libovolně v[0,1).
V každém pevném okně délky k jde maximální změna souřadnic k0.
Pro libovolné epsilon>0 lze počínaje nějakým n událost příslušnosti
upraveného okna k boxu sevřít mezi původní okna v boxech zmenšených
a zvětšených o epsilon, s oříznutím na[0,1]. Jejich objemy jdou při
epsilon->0 ke stejnému objemu. Konečná počáteční výjimka hustoty nemění.
To je obecný důkaz i explicitní vyjasnění nevýznamné konvence pro n=0.

## 10. V2-C0060: opačné bity v odpovědi28

Perioda(11) na str.155 je X=0001000111011101, počínaje X_0.
Každá binární trojice se cyklicky vyskytne dvakrát; posloupnost je
3-distribuovaná. Sudé pozice však mají bity0,0,0,0,1,0,1,0, tedy podíl
jedniček1/4 a nul3/4. Zadání28 na str.182 požaduje
Pr(V_(2n)>=1/2)=3/4.

Odpověď596 bere nekonečně distribuované U a V_n=(X_n+U_n)/2.
Pro libovolné0<=U_n<1 je ale V_n>=1/2 právě tehdy, když X_n=1.
Tištěná konstrukce proto dává1/4, nikoli3/4. Nejde o konečný experiment
ani o přibližnou odchylku.

Oprava je V_n=(1−X_n+U_n)/2. Doplněné bity mají na sudých místech
podíl jedniček3/4 a zachovávají četnosti všech trojic. Pro každou třídu
n modulo16 je trojice U_n,U_(n+1),U_(n+2) rovnoměrná podle věty C.
Každá z osmi dyadických polokrychlí odpovídá právě dvěma třídám
z16; v každé je podmíněné rozdělení rovnoměrné. Směs tedy dává objem
každého boxu, tj.3-distribuci opravené V.

Errata155 opravují pouze úvodní indexy párů(2024) a iniciály(2002);
periodu(11) nemění. Errata182 se týkají26 a31. Na596 je pouze kosmetická
změna1999. V žádné ze čtyř vrstev ani v aktuálním TeXu oprava28 nenalezena.
ASCII návrh: `reports/C0060-alternating-bias-draft.txt`.

## 11. Reprodukovatelnost a meze pokrytí

`verify_distribution_foundations.py` má pět checkpointovaných bloků,
uložených v `results/distribution-foundations.json` a logu. Všech pět
prošlo, běh skončil exit0. Obsah:2418 přesných mřížkových intervalů,
periodické příklady a oba nové protipříklady,65 536 členů oscilujícího
příkladu5,46 230 permutací běhů a kuponové kontroly popsané v oddílu6.
Úspěšné starší kontroly nebyly znovu spuštěny.

Známé opravy v tomto bloku: změny závorek definic na150, odkaz151
z5 na4(2017), zpřesnění153 na2^j-ární(2019), indexy párů155(2024),
odkaz v odpovědi6 na593(2005). Jsou zapracovány; nejsou nové nálezy.
Další relevantní errata celého §3.5 jsou zmapována, ale budou vyhodnocena
v dalších blocích. Existenční algoritmus citovaný na159, následující
kritika R1/R2 a ostatní definice náhodnosti zde ještě nejsou uzavřeny.
