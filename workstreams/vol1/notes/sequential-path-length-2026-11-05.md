# Souvislý průchod §2.3.4.5 — 5. listopadu 2026

X0977. Přečten výklad 399–404, všech 17 zadání na 404–406 a odpovědi
594–596 v hranicích oddílu. Přezkoušeny tři důkazní poznámky v
parallel/tree-path-length/notes, celý huffman.py a pozdější pramenné
doplňky. Úspěšné konečné testy nebyly spuštěny znovu.

## Délky cest a Huffmanův důkaz

Pro rozšířený t-ární strom platí tn=n+s−1. Rozštěpení vnějšího uzlu
hloubky d zvýší I o d a E o (t−1)d+t, proto E=(t−1)I+tn, včetně
prázdného původního stromu n=0. Počet dvojic předek/potomek dává
I≤n(n−1)/2; rovnosti dosahuje řetěz. Minimum vyplní nejmělčí místa.
Pro t≥2 je hloubka uzlu k rovna floor(log_t((t−1)k)); sečtení
vrstev dává přesně (7), včetně hranic mocnin a n=0.
Rodič v očíslování úplného t-árního stromu je ceil((k−1)/t).
Oba očíslované obrázky na 401 a příklady cen 34,53,40 na 402 souhlasí.

Při pevném počtu listů je konečně mnoho tvarů. Dvě nejmenší reálné
váhy lze v optimu vyměnit do nejhlubší sourozenecké dvojice bez
zvýšení ceny: změna je součin rozdílu vah a opačného rozdílu hloubek.
Kontrakce odečítá konstantu w1+w2. Důkaz nepotřebuje nezápornost.
Příklad prvočísel na 403 má slučovací součty
5,10,17,24,34,42,53,65,78,95,143,238; součet ceny je 804.
Všechna spojení a uspořádání listů obrázků na 403 a 595 souhlasí.

Vedlejší minima výšky a součtu hloubek vyplývají z výměnného lemmatu
pro bloky stejné váhy, velikosti N a výšky h. Původní listy mají
N=1,h=0; FIFO vnitřních bloků při rovnosti vah zachovává obě pořadí.
Dva různé vytvořené kladné bloky stejné váhy W mají všechny čtyři
děti váhy W/2. Nulové bloky se řadí FIFO; v záporné fázi existuje
nejvýše jediný agregát, který se ihned znovu odebírá.
Pro kladné váhy jsou také vážené profily hloubek takto seřazených
bloků stochasticky uspořádané. Konvexní přírůstky f pak ospravedlňují
stejnou výměnu a minimum sum(w_i f(l_i)) mezi primárními optimy.
Podrobný obecný důkaz v generalizations.md byl přezkoušen; nedostupnost
Markowského originálu není nahrazena pouhým numerickým testem.

## Úlohy 1–12

1: při n=12 se vybírá pět z osmi pozic poslední vnitřní hladiny,
celkem binom(8,5)=56 včetně vyobrazeného stromu.
2: čtvercové váhy mají součty 5,14,30,55,85,119,166,219,385,
cena 1078; diagram na 594 souhlasí.

3: Kraftova rovnost se týká nezáporných celých hloubek. Rozštěpení
listu součet zachová; obráceně je počet listů maximální hloubky sudý,
takže kontrakce dvou listů dává indukci. Formulaci „numbers“ čteme
v kontextu délek hran, nikoli jako libovolná reálná čísla.
4: výměna přísně různých vah v optimu vynucuje opačné pořadí hloubek;
rovné váhy lze přerovnat. Kraftova konstrukce pro seřazené hloubky
dává požadované abecední pořadí listů, včetně jediného listu.

5: B(w,z)=1+z B(w,wz)^2. Derivace v w=1 dává
H=2zC(H+zC'), tedy h_n=4^n−(3n+1)C_n a průměr
4^n/C_n−3n−1 = sqrt(pi)n^(3/2)−3n+O(sqrt(n)).
Jde o rovnoměrné Catalanovy tvary, ne náhodně vkládané vyhledávací
stromy. Nultý koeficient i vytištěné malé koeficienty souhlasí.

6–9: počítání hran a předků dává oba vztahy I/E, vrstvový součet
minimum a součet vnitřních vah jako váženou délku cest.
10: při nezáporných vahách se neplné větvení soustředí do jediného
nejhlubšího uzlu; minimální doplnění nul zajistí m≡1 mod(t−1).
Ternární příklad má cenu 5+30+91+194+385=705.
Pro předepsané stupně se nejhlubší uzel výměnou stupňů udělá uzlem
nejmenšího stupně; přesunuté nezáporné listy cenu nezvýší. Pak
kontrahujeme nejmenší váhy. Nezápornost je zde skutečně potřeba.
11: binární zápis k přidává bit pro 2k nebo 2k+1.
12: součet velikostí podstromů je n+I, průměr 1+I/n; náhodně
vybíraný uzel implicitně vyžaduje n>0.

## Algoritmus H, lesy a zobecnění

13: na vstupu H2 je x už odebraný nejmenší kořen; H2 vybírá druhý
z čel dvou front a H3 vytvoří rodiče s menším indexem než děti.
Pro A[y]<0 je nový součet menší než oba vstupy a všechny zbývající
listy, existuje jen jediný vnitřní agregát a platí přesně invariant
H5. Od nezáporné druhé vybrané váhy slučovací součty neklesají.
První H2 neporovnává váhy; další H2 a H5 jsou nejvýše po m−2,
tedy nejvýše 2m−4 porovnání pro m≥2. Čas je lineární.
Pracovní sentinel A[2m] bereme výslovně jako pomocné místo algoritmu,
nikoli další výstupní uzel.

C0060 zůstává confirmed: pro m=1,w1=1 i s povoleným sentinelem
H1 dává x=1,i=2,j=0,k=1, H2 zvolí y=2 a H3 sníží k na 0.
Zápisy L[0],R[0],A[0] jsou mimo rozsah a H4 již nezastaví.
Po zkopírování jediné váhy je nutný návrat před H2.
V UI měním critical na medium: konkrétní chybějící základ, obecný
algoritmus m≥2 je správný. Uživatelské osobní hodnocení se nemění.
Přijatých 6427 úplných malých testů se neopakovalo.

14: nejhlubší sourozenecká dvojice v celém lese dovoluje stejnou
výměnu a kontrakci, která zachová počet komponent. Huffmanův prefix
je proto minimální les i pro reálné záporné váhy.
15a: stejné lemma pro max(w_i+l_i) slučuje 1+max(w1,w2).
15b: pro x>1 nejmenší dvě váhy, pro 0<x<1 největší dvě; v obou
případech nová váha x(w1+w2). Při x=1 jsou všechny ceny stejné;
rozvoj u 1 dává obyčejnou váženou délku. Pro x=1/2 vznikne řetěz
s vytištěnou cenou; m=1 se vyřídí prázdným prefixem a cenou w1.
16: seřazené optimální hloubky pro w' a sčítání po částech dávají
prefixové porovnání. V obou rozdílech hloubek musí být index k,
nikoli tištěný volný j. Funguje i pro reálné váhy.

17a: každý topologický prefix uzlů je les, takže stačí 14.
Pro záporné váhy při přechodu k 17b nestačí beze slova přerovnat
konstrukční posloupnost. Přezkoušené lemma o k označených uzlech
minimalizuje sum(w_i d_i) a dává rekurenci
M_k(w)=min(M_k(w*), w1+w2+M_(k−1)(w*)).
Jediný Huffmanův strom realizuje minima pro všechna k. Tím dostáváme
slabou majorizaci skutečně seřazených vnitřních vah.
Sum min(a_i,t)=min_k(P_k+(N−k)t) a obrácená duální rovnost dokazují
ekvivalenci se všemi neklesajícími konkávními součty; C² není nutné.

Pro n jednotkových listů je optimální kořenový rozklad
k=2^ceil(lg(n/3)), tj. jediná mocnina dvou v [n/3,2n/3).
Při poměru 1:2 se volí menší. Cena dokonalých větví se předpočítá
v O(log n), druhá větev je nejvýše 2n/3, takže celý výpočet má
O(log n) aritmetických kroků. Pro neklesající konvexní f mají
hodnoty vyvážené rekurence neklesající první diference, a proto
optimální rozklad je floor(n/2),ceil(n/2). Předpoklad f(2)≥0
není nutný. Přijaté testy zobecnění ani velký příklad se neopakovaly.

## Prameny, výjimky a nové posouzení errat

Pozdější pramenné kontroly skutečně doložily relevantní pasáže
Hwang 1979, Hu–Tucker 1971, Hu–Kleitman–Tamaki 1979,
Glassey–Karp 1976 a HLP 1929. X0555 uzavřel celé citované původní
rozsahy Riordan 1960 a Rényi–Szekeres 1967 jako prameny k podobným
problémům, nikoli jako nový audit všech jejich analytických vět.
Schwartzova zpráva z 1.6.1963 přímo dokládá obě vedlejší minima,
pravidlo rovností a kanonický kód. Zachováváme přesné čtecí meze
van Leeuwena a ostatních zdrojů z notes/source-followup-root-review.md.

Dle aktuálního zadání se výslovně přeskakuje kolace dvou časopiseckých
verzí Schwartz/Schwartz–Kallick 1964, celý Markowsky 1981,
celý Golumbic 1976, přesná Parkerova atribuce varianty 0<x<1 a
časopisecká sazba Knuth 1982 oproti přečtenému preprintu 1981.
Parkerův článek 1980 i oprava 1998 byly přečteny, ale konkrétní
atribuci v TAOCP nedokládají; nepovažujeme ji tím za vyvrácenou.
Matematické varianty mají vlastní důkazy. Ukazatele na svazek 3
zůstávají v budoucím auditu svazku 3, zdejší matematika na ně nečeká.
Tyto výjimky uzavírají hlavní text a úlohy 4/15 podle nového zadání,
nikoli historické záznamy partial zpětným přepsáním.

Čerstvý výtah čtyř vrstev je path-length-errata-extract.json.
Sedm známých položek X0523 zůstává evidováno, ale staré hodnocení
obrázku na 403 bylo nepřesné: náš originál již má správný kruhový
rodič a čtvercové listy. V náhradě je vidět doplněná tečka.
Žádná matematická vada obrázku není doložena. Na 404 jde o
explicitnější omezení porovnávané rodiny; „such a tree“ v původním
kontextu již obsahuje sourozence. Vlastní směry kontrakčního důkazu
jsou správné a samostatný protipříklad k původnímu kontextu nemáme.
Proto 403/404 kvůli těmto položkám nebarvíme červeně.
Ani rozepsání odkazu 5.2.3-21 není matematická chyba.

Skutečné chybné údaje X0523 mapujeme na 402 (1951 místo 1952),
406 (1939 místo 1929) a 596 (indexy). Tam je také doplnění
slučovací funkce pro 0<x<1. C0060 se mapuje pouze na odpověď 596,
správné zadání 405 není chybová lokace.
Celé 399–405 a 594–596 jsou obsahově uzavřeny; 406 čeká na zbývající
historický oddíl. Fyzický pozdější dotisk ani prvenství nálezů
nejsou tímto potvrzeny.
