# Pollardova metoda p−1 a Williamsova metoda p+1

Rozsah: §4.5.4, úlohy 19–20 na str. 413, odpovědi na 661
a Pollardův odstavec na 402. Sken třetího vydání, prvního dotisku
z roku 1997. Strany 392, 393, 413 a 661 byly znovu zobrazeny;
402 byla vizuálně přečtena v předchozím bloku. Matematika obou
úloh je níže uzavřena. C0161 se týká pevné báze v odpovědi 19
a slibovaného příkladu, nikoli samotné myšlenky metody p−1.

## 1. Dělitelnost a vlastní dělitel jsou různé podmínky

Pro celá čísla x,N značí gcd(x,N) jejich největší společný dělitel.
**Vlastní dělitel** zde znamená d s 1<d<N. Zjištění p|gcd(x,N)
ještě nezaručuje vlastní dělitel: gcd může být celé N.

Je-li D kladné celé číslo, číslo M=2^D−1 je dělitelné každým
lichým prvočíslem p s p−1|D. To je přímo Fermatova věta.
Obecněji stačí, aby D byl násobkem **řádu** báze 2 modulo p,
tedy nejmenšího kladného d s 2^d=1 modulo p. První věta
odpovědi 19 je správná.

Položme B1=1000, B2=100000 a E=lcm(1,...,1000), kde lcm značí
nejmenší společný násobek. E je součin nejvyšších mocnin všech
168 prvočísel nejvýše 1000; označme tyto mocniny q_1,...,q_168.
Každá je nejvýše 1000. Proto postupné umocňování v knize skutečně dává
A=2^E modulo N. E má 1438 bitů. V konstrukci není potřeba
používat zaokrouhlený reálný logaritmus: mocniny se mohou
násobit celými čísly, dokud nepřesáhnou B1.

Přesná podmínka druhé fáze je

    p−1 | E*q,
    q=1 nebo q prvočíslo s 1000<q<100000.                 (1)

To pokrývá zamýšlený případ úlohy: malé prvočíselné mocniny
a nanejvýš jeden další prvočíselný faktor v uvedeném intervalu.
Není to tvrzení o libovolně vysoké mocnině tohoto dalšího faktoru.
Pro bázi a nesoudělnou s N platí p|gcd(a^(E*q)−1,N).
Případ q=1 je vhodné zkontrolovat již na konci první fáze.

## 2. C0161: báze 2 nerozloží vlastní knižní příklad

V rovnici (15) na 392 je N=2^214+1. Úloha 19 uvádí jeho
druhý největší prvočinitel

    p = 23528569104401
      = 1 + 2^4 * 5^2 * 67 * 107 * 199 * 41231.

Rozklad i prvočíselnost všech šesti prvočinitelů N již byly
nezávisle certifikovány v results/primality-certificates.json;
zde se tyto certifikáty nepřepočítávají.

Avšak 428=4*107 dělí E a 2^428=1 modulo N. Odpovědí předepsaná
báze a1=2 tedy dává A=1 modulo N. Každý její b_q je potom N
a každý součin v dávce je 0 modulo N. Slibovaný faktor tímto
postupem nevznikne.

Nejde o problém odstraněný předběžným dělením. Pro zbytek z 393

    n6 = 192343993140277293096491917
       = 8174912477117 * 23528569104401

platí stejný argument. Dokonce modulo obou prvočinitelů n6 má
2 přesně řád 428: řád dělí 428, nedělí 214, a nemůže být 4,
protože oba prvočinitelé jsou větší než 2^4−1. Proto pro každé
kladné d dostaneme gcd(2^d−1,n6) buď 1, nebo n6. Nepomůže ani
kontrola mezikroků, jiná hranice hladkosti nebo půlení exponentu
při zachování báze 2.

Konkrétní místní oprava příkladu je báze 3. Pro stejné E platí

    3^E mod n6 = 73685933081392488107523778,
    gcd(3^E−1,n6) = 1,
    gcd(3^(E*41231)−1,n6) = 23528569104401.

Obecný algoritmus potřebuje připustit změnu báze. Následující
oddíl vysvětluje rigorózní doplnění tvrzení o vysoké pravděpodobnosti.

## 3. Dávky a hranice druhé fáze

Pro A nesoudělné s N a q=30r−k je

    gcd(A^q−1,N) = gcd(A^(30r)−A^k,N),

protože násobení výrazem A^k nemění gcd. Předsunutá kontrola
gcd(a,N) buď najde faktor, nebo zajistí tuto nesoudělnost.
Pro liché N a pevnou bázi 2 je splněna automaticky.

Kniha tiskne **33<=r<=3334**, oba konce včetně. OCR zaměnilo
oba znaky za ostré nerovnosti; není to chyba sazby. Pro
k v {1,7,11,13,17,19,23,29} těchto 3302 dávek pokrývá všech
9424 prvočísel mezi 1000 a 100000. Poslední prvočíslo je
99991=30*3334−29. Některé další exponenty jsou složené nebo
těsně vně intervalu, což správnosti nevadí.

Také postup od 1009 se střídavými přírůstky 4,2 pokrývá všechna
potřebná prvočísla; sám nefiltruje složená čísla. Kdyby gcd celé
dávky vyšlo N, lze zkusit jednotlivé členy nebo dávku rozdělit.
To může odhalit vlastní faktor, ale u A=1 jsou i všechny
jednotlivé výsledky N, takže je nutné změnit bázi.

## 4. Důkaz vysoké pravděpodobnosti pro doplněnou metodu p−1

Předpokládejme, že liché složené N má alespoň dva různé
prvočíselné dělitele a jeden prvočinitel p splňuje (1).
Samotné prvočíselné mocniny lze předem zachytit přesným testem
celých kořenů. Netvrdíme, že metoda musí rozkládat prvočíslo.

Zvolme a rovnoměrně mezi jednotkami modulo N; **jednotka** je
zbytek nesoudělný s N, tedy invertovatelný při násobení.
Lze losovat všechny zbytky a zkoušet gcd: vlastní gcd již
ukončuje rozklad, gcd=N znamená nové losování.

Pro správné q z (1) napišme E*q=2^s*K, K liché. Vedle
konečného gcd zkusme všechna

    gcd(a^(K*2^j)−1,N), j=0,...,s.                     (2)

Modulo p má a řád dělící E*q. Fixujme zbytek a modulo p
a vezměme jiný prvočinitel r čísla N. Podle čínské věty
o zbytcích je a modulo r stále rovnoměrná nezávislá jednotka.
Pokud její řád nedělí E*q, poslední gcd v (2) obsahuje p,
ale nikoli r, a je vlastní.

Jinak záleží na exponentu dvojky v obou řádech. Jsou-li tyto
exponenty různé, jeden člen (2) opět oddělí p a r. Ve skupině
nenulových zbytků modulo liché prvočíslo r, která je cyklická
(tvořená mocninami jednoho prvku) a má sudý počet prvků,
má každá jednotlivá třída podle exponentu dvojky
v řádu nejvýše polovinu prvků. Konkrétně je-li 2^v nejvyšší
mocnina dvojky dělící r−1, tyto podíly jsou
1/2^v, 1/2^v, 2/2^v, ..., 2^(v−1)/2^v.
Dodatečná podmínka na lichou část řádu počet jen zmenšuje.

Pravděpodobnost selhání všech (2) je tedy nejvýše 1/2 pro
každou nezávislou bázi. Po t bázích je nejvýše 2^(−t).
Důkaz platí i při opakovaných prvočinitelích N: oddělení
již modulo p a r zaručuje vlastní gcd modulo celého N.

Zkoušení (2) nevyžaduje nové dlouhé mocnění pro každý j.
Je-li E=2^s*K, spočteme a^K, pro každé liché q je umocníme
na q a pak s-krát čtvercujeme. Potřebujeme
O(log E + součet_q(log q+s)) modulárních násobení a obdobný
počet gcd; log v tomto odhadu má základ 2. Jde o účinné doplnění;
explicitní mez 1/2 ani toto
doplnění nepřipisujeme stručné knižní odpovědi.

## 5. Lucasova varianta pro p+1

Použijme polynomy V_n(P) určené vztahy

    V_0(P)=2, V_1(P)=P,
    V_(n+1)(P)=P*V_n(P)−V_(n−1)(P).

Pro jednotku alpha s alpha+alpha^(-1)=P je
V_n(P)=alpha^n+alpha^(−n), jak plyne indukcí. Proto platí
polynomiální identity

    V_ab(P) = V_a(V_b(P)),
    V_2n(P) = V_n(P)^2−2,
    V_(2n+1)(P) = V_n(P)*V_(n+1)(P)−P.                  (3)

Platí i modulo složeného N, bez dodatečného dělení.
Binární postup s dvojicí V_n,V_(n+1) vypočte V_m za O(log m)
modulárních násobení.

**Diskriminant** polynomu X²−PX+1 je d=P²−4. Je-li d
kvadratický nezbytek modulo lichého prvočísla p (nenulový
zbytek, který není čtvercem), kořeny tohoto polynomu
alpha a alpha^(-1) leží v tělese s p² prvky a Frobeniův
automorfismus x→x^p je zaměňuje. Tedy alpha^(p+1)=1
a V_(p+1)(P)=2 modulo p. Je-li d nenulový čtverec, oba kořeny
leží již modulo p a analogicky V_(p−1)(P)=2.

Pro pevné P tak první fáze opakovaně skládá V_(q_j) podle
(3), čímž dává A=V_E(P); druhá fáze zkouší gcd(V_q(A)−2,N).
Za podmínky p+1|E*q a nezbytkového diskriminantu bude p
dělitelem výsledku. Stejně jako u p−1 to samo neznamená
vlastní faktor.

První část úlohy 20 žádá jedno číslo dělitelné všemi
vhodnými p. Pro sudé D>=4 lze zvolit konečný nenulový součin

    M = product_(P=3)^(D+1) (V_D(P)−2).                 (4)

Každé liché p s p+1|D je nejvýše D−1, takže parametry
P=3,...,D+1 pokrývají všechny zbytky modulo p. Některý
z nich má nezbytkový diskriminant, a příslušný člen součinu
je dělitelný p. Každý člen je kladný, neboť P>=3 a V_D(P)>2.
Pro liché D nebo D<4 nejsou žádná vhodná lichá p a stačí M=1.
Součin (4) je konstruktivní existence, nikoli návrh účinného
zápisu exponenciálně velkého celého čísla.

Počet nezbytkových diskriminantů je přesně (p−1)/2; nenulových
čtvercových je (p−3)/2 a nulové jsou dva. Důkaz: počet řešení
y²=P²−4 je p−1, protože (P−y)(P+y)=4 se parametrizuje
libovolným nenulovým P−y. Současně se tento počet rovná
p + součet_P chi(P²−4), kde chi je Legendreův symbol,
tedy znaménko 0,+1,−1 podle nulovosti a čtvercovosti.

## 6. Rigorózní náhodná varianta p+1

Následující vlastní doplnění dává explicitní mez pro získání
**vlastního** faktoru, ne pouze pro příznivý diskriminant.
Nepřipisujeme je jako doslovný algoritmus Williamsovu článku.
Opět předpokládejme dvě různá lichá prvočísla p,r dělící N,
přičemž p+1|E*q pro některé z testovaných q.

Zvolme rovnoměrnou jednotku Delta modulo N. Pak zvolme
rovnoměrně a,b modulo N, podmíněně tím, že
h=a²−Delta*b² je jednotka. Každý vlastní gcd nalezený při
těchto předtestech už dává faktor. Pro důkaz rozdělení lze
takový úspěch ignorovat a losovat znovu, což úspěšnost jen sníží.

Počítejme v kvadratické algebře t²=Delta. Její prvek x+y*t
má **normu** x²−Delta*y²; normou 1 tedy nazýváme prvky, které
při násobení se sdruženým x−y*t dají 1. Položme

    z = a+b*t,
    gamma = z / conjugate(z) = (a+b*t)^2 / h,
    P = gamma + gamma^(-1) = 2*(a²+Delta*b²)/h modulo N. (5)

Všechny inverze v (5) existují díky předtestu h. Gamma má
normu 1. Modulo každého prvočísla l dělícího N je algebra
buď těleso s l² prvky (Delta nezbytek), nebo součin dvou
kopií tělesa modulo l (Delta čtverec). V obou případech je
skupina prvků normy 1 cyklická, řádu l+1, respektive l−1.
Pro čtvercový případ se tato skupina skládá z dvojic (u,u^−1).

Zobrazení z→z/conjugate(z) dosáhne každého prvku této skupiny.
Každé vlákno, tedy množina z vedoucích ke stejné gamma,
má l−1 prvků: v tělesovém případě jde o mocnění
na 1−l, ve štěpeném případě o poměr dvou nenulových souřadnic.
Rovnoměrný podmíněný výběr z tedy dává rovnoměrnou gamma
ve skupině normy 1. Rozdělení pro různá prvočísla jsou
nezávislá; při mocninách prvočísel má každý přípustný zbytek
stejný počet zdvihů. Parametr P²−4 zde nemusíme vylučovat:
gamma=±1 jsou platné prvky tohoto rozdělení.

S pravděpodobností přesně 1/2 je Delta nezbytek modulo
cílového p. Tehdy řád gamma modulo p dělí p+1, tedy E*q.
Pro E*q=2^s*K a j=0,...,s zkoušejme

    gcd(V_(K*2^j)(P)−2,N).                             (6)

Modulo každého l platí V_e(P)=2 právě tehdy, když gamma^e=1.
Skutečně gamma^e+gamma^(−e)−2=(gamma^e−1)²/gamma^e;
uvažovaná algebra modulo l nemá nenulový prvek se čtvercem 0.
To platí i ve štěpeném případě po obou souřadnicích.

Nyní se použije stejný argument s exponenty dvojky v řádech
jako v oddílu 4. Podmíněně příznivou Delta má (6) pravděpodobnost
alespoň 1/2 oddělit p a r. Jeden nezávislý pokus (5) proto
uspěje s pravděpodobností alespoň 1/4, a t pokusů selže
s pravděpodobností nejvýše (3/4)^t. Zachycené vlastní gcd
v předtestech tuto mez mohou pouze zlepšit.

Při generování jednotek lze předtesty chápat jako opakované
losování až do splnění podmínky. Při fixované Delta dává
podmínka na normu přesně popsané rovnoměrné rozdělení; nesmíme
současně znovu losovat Delta při každém odmítnutém z, což by
ji mohlo vychýlit. Modulární práce pro (6) má stejný řád
jako u (2), protože kompozice a zdvojování v (3) nahrazují
mocnění a čtvercování.

Ani očekávaná cena tohoto losování není skrytě exponenciální.
Má-li N k různých lichých prvočinitelů l_1<...<l_k, pak
l_i>=i+2, takže podíl jednotek je alespoň 2/(k+2).
Pro pevnou Delta je podíl přípustných z lokálně buď
(1−1/l_i)^2, nebo 1−1/l_i², tedy celkově alespoň
4/(k+2)^2. Očekávaný počet pokusů je nejvýše kvadratický
v k<=log_3 N. Počet bitových operací je proto polynomiální
v délce N a v uvedených hranicích B1,B2.

## 7. Přesné kontroly a jejich rozsah

verify_factoring_pminusplus.py, limit 180 s, session 10253,
exit 0; čtyři checkpointy celkem 3.706 s. Proces skončil před
zaznamenáním PID. Úspěšné checkpointy se neopakovaly.

- 672 mezistavů knižní první fáze nezávislým binárním
  mocněním, obě báze pro N i n6, celá perioda 428 pro n6;
  9424 prvočísel druhé fáze a 64192 dávkových identit.
- 37375 hodnot Lucasovy posloupnosti současně přímou rekurzí,
  binárním postupem a stopou mocniny matice [[P,−1],[1,0]];
  46575 kompozic, 1058 diskriminantů, 106 případů součinu (4).
- 450 případů p−1 se všemi 94280 jednotkami; nejmenší skutečná
  úspěšnost doplněné metody je přesně 1/2.
- 389344 přípustných dvojic a,b pro p+1, úplná rovnoměrná
  vlákna (5), 85060 kontrol stopy a 15 přesných racionálních
  pravděpodobností. Podmíněná mez 1/2 i celková 1/4 splněny.

Konečné kontroly nejsou náhradou obecných důkazů v oddílech
1–6. Prvočíselné certifikáty velkého příkladu se přebírají
z již uzavřeného předchozího bloku, nikoli z pravděpodobnostního
testu nového skriptu.

## 8. Errata a historické zdroje

Prohledány celé all2-prepre, all2-pre, all2, err2
i aktuální err2.textxt, podle stran i charakteristických čísel,
báze, jmen a vzorců. Oprava odpovědi 19 ani příkladu nalezena
nebyla. Sousední opravy odpovědí 17 a 22 se netýkají tohoto
nálezu. Novější fyzický tisk a prvenství nejsou ověřeny.

Pollardův článek *Theorems on factorization and primality
testing*, Proc. Cambridge Phil. Soc. 76 (1974), 521–528,
DOI 10.1017/S0305004100049252: bibliografie ověřena; plný
článek nebyl získán. Jeho nepřístupnost nenahrazujeme tvrzením,
že byl přečten.

Williamsův primární článek *A p+1 Method of Factoring*,
Math. Comp. 39 (159), 225–234 (1982), DOI
10.1090/S0025-5718-1982-0658227-7, byl čten v dostupném
[OCR přepisu originálu](https://paperzz.com/doc/9339784/io-phiitf-j---i.---american-mathematical-society)
v oddílech 1–5, str. 225–230: definice, obě fáze a
pravděpodobnostní kontext. Článek dokládá dřívější nepublikovanou
znalost obou Lehmerů, ale sám tento čtený úsek nezjišťuje
konkrétní desetiletí 1920–1929 uvedené v knize.

Oficiální PDF bylo nepřístupné (403); další archivní pokus
selhal síťově. Vizuální kontrola celého Williamsova originálu
ani přepočet jeho empirických tabulek 231–234 se netvrdí.
Tato bibliografická omezení jsou oddělena od vlastního důkazu
úloh 19–20. Nic nebylo odesláno.
