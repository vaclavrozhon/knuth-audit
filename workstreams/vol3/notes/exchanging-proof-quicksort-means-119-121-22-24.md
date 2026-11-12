# Quicksort: nezávislost, všechny GF a průměry 22–24

2026-11-07. Zobrazen originál 119–121, zadání 135, odpovědi 631–632.
Tento blok dokládá (18)–(25), celé požadované GF a průměry úloh 22–24.
Nákladová optimalizace (26), variance a limitní zákon mají další blok.
Žádný výpočtový běh. Počty první fáze (17) jsou převzaté z P1046,
jejich důkaz se neopakuje. Všude M≥1 celé, různé klíče a uniformní
permutace; nula prvků má nulové náklady a prázdnou GF rovnu 1.

## P1056 — ranky, podmíněná rovnoměrnost a skutečná nezávislost

Každé rostoucí přeznačení klíčů zachová všechna rozhodnutí Q, takže
smíme vstup chápat jako permutaci 1..N. Podmiňme pivot K1=s a úplný
binární vzor pozic menších/větších zbývajících klíčů. V něm je a=s−1
menších a b=N−s větších. Pro tento vzor existuje právě a!b! vstupů;
uspořádání menších i větších na jejich pozicích jsou navzájem nezávislé
rovnoměrné permutace.

Skeny porovnávají jen s pivotem, takže jejich posuny a všechny výměny
závisejí jen na tomto vzoru. Pro menší klíče provedou určitou pevnou
permutaci jejich a pozic, pro větší určitou pevnou permutaci b pozic.
Výměna pivotu je také daná vzorem. Proto jsou výsledné levé a pravé
seznamy podmíněně *nezávislé* uniformní permutace, nikoli jen jednotlivě
uniformní. Jejich produktové rozdělení nezávisí na vzoru, a tedy se
nezmění ani po odpodmínění vzoru nebo podmínění pouze jeho statistikou t.
To ospravedlňuje všechny produkty GF níže i následující indukci.

## P1057 — přesný společný zákon pivotu s a přesunů t

Pivot s má pravděpodobnost 1/N. Mezi prvními s pozicemi je pivot a
a=s−1 ostatních míst, z nichž má být t obsazeno většími klíči. Volíme
tedy t míst z a. Ve zbývajících b místech musí být právě t menších,
což lze zvolit binom(b,t) způsoby. Celkem je binom(N−1,a) vzorů.
Proto

    b_(s,t,N) = binom(a,t) binom(b,t) / (N binom(N−1,a))
              = a! b! binom(a,t) binom(b,t) / N!.

To jsou oba tvary tištěné odpovědi 22. Platný rozsah je
0≤t≤min(a,b), ostatní členy jsou nula podle binomické konvence;
součet do s je proto neškodný. Součet přes t je 1/N, protože každý
binární vzor má právě jeden t. Podmíněně na s je t hypergeometrický:
každá z a sledovaných pozic obsahuje větší klíč s pravděpodobností
b/(N−1), takže E(t|s)=ab/(N−1). Tento argument nevyžaduje nezávislost
pozic. N>M≥1 zajišťuje N−1>0.

## P1058 — všechny A/B/C/S generující funkce v úloze 22

Pro každou statistiku X píšeme X_n(z)=E(z^X). Pro n≤M jsou
A_n=B_n=C_n=S_n=1. Pro n>M jsou, s a=s−1,b=n−s,

    A_n(z) = (z/n) sum_s A_a(z) A_b(z),
    B_n(z) = sum_s,t b_(s,t,n) z^t B_a(z) B_b(z),
    C_n(z) = (z^(n+1)/n) sum_s C_a(z) C_b(z),
    S_n(z) = (1/n) sum_s z^[M+1<s<n−M] S_a(z) S_b(z).

Každá fáze přidá 1 do A, t do B, n+1 do C. Do S přidá právě jednu
tehdy, když obě části mají více než M prvků, tedy právě pro uvedený
indikátor. P1056 dává nezávislost obou následných statistik i podmíněně
na t, proto GF příspěvků skutečně násobíme. Součet přes s,t je úplná
disjunkce všech případů, takže koeficienty jsou nezáporné a při z=1
se normalizují na 1. Vybrané pořadí zásobníku neovlivní tyto součty.

## P1059 — D/E, mezery mezi listy a celé počáteční produkty

Po partition se insertion nikdy nepřesune přes pivot: všechny předchozí
části mají menší klíče. Vložený první prvek každého konečného bloku
proto nevyvolá přesun, stejně jako první prvek samostatně tříděného
seznamu. D i E se sčítají přes obě děti bez dodatečného kořenového
příspěvku. Tudíž pro n>M

    D_n(z) = (1/n) sum_s D_(s−1)(z) D_(n−s)(z),
    E_n(z) = (1/n) sum_s E_(s−1)(z) E_(n−s)(z).

Pro n≤M proběhne obyčejná insertion. Nechť r_k je rank k-tého původního
prvku mezi prvními k. Vektor r_1..r_n s 1≤r_k≤k určuje jedinou
permutaci (rekonstrukcí od n dolů); všech n! možností je rovnoměrných.
Proto jsou r_k nezávislé uniformní hodnoty. Při vložení k-tého prvku
je prefix již seřazen a jeho maximum je na k−1. Přesun nastane právě
při r_k<k, a počet posunů je k−r_k. Tedy

    D_n(z) = product_(k=1..n) (1+(k−1)z)/k,
    E_n(z) = product_(k=1..n) (1+z+...+z^(k−1))/k.

D není počet sestupů původní permutace; jde o počet původních prvků,
které nejsou novými prefixovými maximy. Tím je také vysvětlen důležitý
rozdíl proti Eulerovskému polynomu. Z produktů nebo přímo z r_k plyne
E D_n=n−H_n a E E_n=n(n−1)/4, včetně n=0,1. Toto jsou všechny báze
i rekurence požadované v úloze 22.

## P1060 — všechny kroky (19)–(23), obecný faktor a báze

Nechť m≥1, x_0..x_(m−1) jsou dány a pro n≥m platí
x_n=f_n+(2/n)sum_(k<n)x_k. Hodnota x_m musí splnit tuto první rovnici.
Odečtení n-té rovnice násobené n od (n+1)-ní násobené n+1 dává

    (n+1)x_(n+1)=(n+2)x_n+g_n,
    g_n=(n+1)f_(n+1)−nf_n.

Z rozdílové rovnice a správné báze x_m lze indukcí získat zpět (19);
bez báze by šlo jen o nutnou podmínku. Dělením (n+1)(n+2) dostáváme
celé (23). Pro f_n=1/n je g_n=0, takže x_n/(n+1) je konstantní.
Pro f_n=n+1 je g_n=2(n+1), tudíž

    x_n/(n+1)=x_m/(m+1)+2(H_(n+1)−H_(m+1)).

Součet při n=m je prázdný. Ani příklad 1/n se nepoužívá v n=0.

Pro obecné a_n x_(n+1)=b_n x_n+g_n nastavme
w_n=(a_0...a_(n−1))/(b_0...b_(n−1)). Pak
w_(n+1)=w_n a_n/b_n a násobení w_n/b_n dává
y_(n+1)=y_n+c_n pro y_n=w_nx_n,c_n=w_ng_n/b_n. To je každá část (22),
včetně prázdných součinů v n=0. Samotná napsaná podílová metoda
předpokládá nenulové b_i; pro zpětné vyjádření x_i též nenulové a_i.
Nulový koeficient se řeší přímo původní rovnicí a metoda se po něm
znovu inicializuje; zde mají všechny koeficienty kladné hodnoty.
Pro a_n=n+1,b_n=n+2 je w_n/b_n=n!/(n+2)!, přesně tištěný faktor.

## P1061 — rovnice (18), přesné C_N a rozsah aproximace (24)

První fáze má C=n+1 a každá ze dvou nezávislých částí svou průměrnou
cenu. Uniformní s proto dává (18); symetrie a,b dává faktor 2.
Pro n≤M je C_n=0. Nastavíme m=M+1: C_m=m+1, tedy x_m/(m+1)=1.
P1060 dokazuje přesně

    C_N=(N+1)(2H_(N+1)−2H_(M+2)+1),   N>M.

Pro N=M+1 dává N+1, jak musí. Z integrálního srovnání harmonického
součtu platí H_u−H_v=ln(u/v)+O(1/v) pro u≥v≥1, a proto

    C_N=2(N+1)ln((N+1)/(M+2))+(N+1)+O((N+1)/(M+2)).

Vytištěné „≈“ tedy udává vedoucí člen v režimu N/(M+2)→∞, zejména
pro pevné M a N→∞. Není to uniformní relativní aproximace až k
N=M+1 (tam je logaritmický člen nula). Přesná rovnost nad ní zůstává
platná všude v předepsané doméně; nepovažuji heuristické ≈ za další
rovnost se skrytou chybou.

## P1062 — celé A_N a B_N v úloze 23 / (25)

Z (17) a P1057

    A_n=1+(2/n)sum_(k<n)A_k,
    B_n=(n−2)/6+(2/n)sum_(k<n)B_k,   n>M.

Druhý toll plyne přímo ze součtu
sum_(a=0..n−1)a(n−1−a)=(n−1)n(n−2)/6 a dělení n(n−1).
Obě báze jsou n≤M nulové. Pro m=M+1 máme A_m=1 a B_m=(M−1)/6.
U A má (23) přírůstek 1/((n+1)(n+2)), jehož teleskopický součet dává

    A_N=2(N+1)/(M+2)−1.

U B je g_n=(2n−1)/6 a

    g_n/((n+1)(n+2))
      =1/(3(n+2))−(1/2)(1/(n+1)−1/(n+2)).

Sečtením od m do N−1 a dosazením B_m dostáváme

    B_N=(N+1)/6 (2H_(N+1)−2H_(M+2)+1−6/(M+2))+1/2.

To je celý druhý řádek (25), nejen jeho vedoucí koeficient. Platí i
pro M=1 a nejmenší n=2, kdy B_2=0.

## P1063 — celé D_N a E_N v úloze 23 / (25)

Pro n>M mají obě rekurence nulový toll. Báze D_k=k−H_k a
E_k=k(k−1)/4 pro k≤M jsou z P1059. Pro m=M+1 dostaneme

    D_m = (2/(M+1))sum_(k=1..M)(k−H_k)
        = M+2−2H_(M+1),
    E_m = (2/(M+1))sum_(k=1..M) k(k−1)/4
        = M(M−1)/6.

Použité konečné identity mají přímé důkazy:
sum H_k=sum_(j=1..M)(M+1−j)/j=(M+1)H_M−M a
sum k(k−1)=2 sum binom(k,2)=2binom(M+1,3).
Při nulovém tollu je x_N/(N+1) konstantní, takže

    D_N=(N+1)(1−2H_(M+1)/(M+2)),
    E_N=(N+1)M(M−1)/(6(M+2)).

Pro M=1 jsou oba výrazy nula, v souladu se zbytečností insertion.
Není zde nezapočtené přesouvání přes pivot ani mezi sousedními listy.

## P1064 — celé S_N v úloze 23 / (25), včetně prvního nenulového N

Kořen přidá push při M+2≤s≤n−M−1. Je-li n≥2M+2, počet takových
ranků je max(0,n−2M−2); při menším n není žádný. Pro n≤2M+2 proto
S_n=0 i rekurzivně. Pro n≥m=2M+2 má rekurence toll
f_n=1−m/n, který je v bázi m nula. Jeho g_n=1, a proto

    S_N=(N+1)/(m+1)−1=(N+1)/(2M+3)−1,   N>2M+1.

Na N=2M+2 je opravdu nula, na 2M+3 je 1/(2M+3), protože jediný
pivot s=M+2 připouští oba dlouhé potomky. To kontroluje oba ostré
prahy v zadání i odpovědi. Známá oprava poslední věty odpovědi 23
mění odkaz (20) na (19); obě použité rekurence jsou výše odvozeny.

## P1065 — úloha 24: konkrétní bezpečné vynechání a přesné C_N

Nestačí slepě zastavit oba skeny při i≥j a pak vždy zaměnit pivot:
je třeba využít již zjištěný vztah klíče, na kterém se ukazatele potkají.
Přesná realizace bez opakovaného porovnání pro různé klíče je tato.
Nezařazené pozice tvoří interval [u,v], zpočátku [l+1,r]. Zleva
prohlížíme R[u]. Je-li <pivot, zvýšíme u. Je-li >pivot, tento vztah
si zachová řídicí větev a zprava prohlížíme jen v>u. Větší R[v]
vyřadíme snížením v; při menším R[v] zaměníme známý špatný pár,
zvýšíme u, snížíme v a vrátíme se vlevo. Pokud v dospěje na u,
již víme, že R[u]>pivot, tedy jej zařadíme napravo bez porovnání a
snížíme v na u−1. Po vyčerpání je v poslední menší pozice (nebo l).
Pivotová výměna l,v dokončí rozdělení.

Každý nepivotový záznam je prohlédnut právě jednou. Výsledek partition
je stejný jako v Q: vynechána jsou pouze závěrečná porovnání již známé
strany a pivotu/zarážky. V první fázi je tedy přesně n−1 porovnání.
Uniformita P1056 se zachová. Rekurence v odpovědi 24 plyne s toll n−1
a nulovou bází. Alternativně na *každém* vstupu je nový počet starý
C−2A, protože partition strom je stejný a šetříme dvě porovnání na fázi.
Z P1061/P1062 proto

    C_guard,N=(N+1)(2H_(N+1)−2H_(M+2)+1−4/(M+2))+2,
    Delta_N=4(N+1)/(M+2)−2.

To je přesně tištěná odpověď, včetně +2. Při N=M+1 dává M=n−1.

## P1066 — smysl cenového komentáře v odpovědi 24

Přesná úspora je Delta_N výše. Zápis „about 4N/M“ navíc nahrazuje
M+2 hodnotou M; jeho relativní odchylka při velkém N je 2/(M+2),
tedy nejde o další uniformní asymptotickou rovnost pro všechna M.

V popisovaném modelu, kde každé zachované porovnání klíčů doprovází
nový test indexů, je počet dodatečných register tests G≥C_guard,N.
Při jednotkových cenách c_K,c_R může dojít k úspoře jen když

    c_K/c_R > G/Delta_N ≥ C_guard,N/Delta_N.

Pro pevné M a N→∞ je pravý podíl
(M+2)ln N/2+O_M(1), a tedy nakonec větší než M ln N/2. Tím je
slabší nutná asymptotická podmínka uvedená v odpovědi správná v jejím
pevně-prahovém modelu. Netvrdí, že dosažení této slabší hranice stačí,
ani nedokazuje cenu každé možné optimalizované implementace. Pro M
rostoucí s N by bylo nutné zachovat ln(N/(M+2)) a přesné poměry.
Komentář o jiných učebnicích není ověřen jako bibliografický průzkum.

## P1067 — dosud neuzavřený momentový/limitní dovětek (partial)

Rovnice (24) má na 120 dopředné tvrzení o směrodatné odchylce při M=1:
sqrt((21−2pi²)/3)N. Odpověď 22 na 631–632 navíc zmiňuje nenormální
limitní zákon pro rekurenci s n−1. Samotné právě prokázané GF ani
průměry tyto dva výsledky nedokazují. Zůstávají explicitně partial
do následujícího momentového/limitního bloku; nesmí tím být celá 120
ani celá odpověďní 631 povýšena. Výrok „not yet fully analyzed“ je
dobový popis, nikoli ověřený stav současné literatury.

## Zdroje a návaznost

`sources/exchanging-errata-review.json` zahrnuje všech pět vrstev.
Zohledněno 119/2007 (prvních s klíčů), 632/2000 (odkaz 19),
632/2016 (Régnier) a historické opravy GF na prvním vydání 608.
Citace Computing Surveys6(1974),287–289 a dobová srovnání jiných
partition algoritmů nejsou znovu bibliograficky kontrolovány.
Žádný nový nález. Průměry jsou matematické počty abstraktního Q;
strojová mez P1055 se nesmí zaměnit za omezení těchto kombinatorických
rekurencí. P1033 dál zahrnuje neurčené obecné praktické účinky shodných
klíčů v próze 119; zdejší pravděpodobnostní závěry různé klíče předpokládají.


Aktualizace: P1067 je nyní uzavřena v `exchanging-proof-quicksort-limit-cost-120-121.md`, P1068–1072. Předchozí označení partial zachycuje stav tohoto mezikroku; aktuální stav je v proof-audit.json.
