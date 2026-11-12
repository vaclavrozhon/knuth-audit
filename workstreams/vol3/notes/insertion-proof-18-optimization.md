# Úloha18: celé minimum odhadu a jeho platná aplikace

7. listopadu 2026. Originál103/file114 a621/file632 zobrazen;
navazující úvod90/file101 kontrolován ve stejném rozsahu níže.
Pětivrstvá `sources/insertion-errata-review.json` neobsahuje opravu18.
Přebíráme konkrétní H/corollary a uniformní odhad P0755–0766,
nikoli pouhou první čtenářskou kontrolu. Numerické příklady mají
jediný krátký přímý výpočet s nice15 v
`results/insertion-ex18-optima.json`; žádná optimalizační enumerace.

## P0767: odkud pocházejí všechny členy odhadu

Uvažuj pevný počet t≥1 a kladné přírůstky
h_0=1<h_1<…<h_(t−1). Pro skutečný algoritmus požadujeme
celočíselnost a dělitelnost; spojitou úlohu následně odlišíme.
První průchod má přesný průměr

    N²/(4h_(t−1))−N/4+r(h_(t−1)−r)/(4h_(t−1)),

takže jeho chyba proti prvnímu členu odhadu je O(N).
Pro následující průchod h_(s−1) má každá jeho třída délku
m=N/h_(s−1)+O(1) a je k-ordered, k=h_s/h_(s−1).
P0763 dává, pokud k→∞ a N/h_s→∞,

    f(m,k)~(√π/8)m^(3/2)√k.

Sečtení přes všech h_(s−1) tříd dává přesně vedoucí člen
(√π/8)N^(3/2)√h_s/h_(s−1). Délky zaokrouhlené o1
nemění relativní odhad, protože m→∞. Pro pevné t proto získáme
zadanou funkci

    E(h)=N²/(4h_(t−1))
         +(√π/8)N^(3/2)∑_(1≤s<t)√h_s/h_(s−1).

Pouhé „velké N“ nestačí uniformně pro libovolné přírůstky;
potřebné poměry se při aplikaci minima ověří v P0772.

## P0768: skutečná doména spojitého minima

Polož C=√π N^(3/2)/8 a H=4N/π. Pro výpočet definuj h_t=H,
takže E=C∑_(1≤s≤t)√h_s/h_(s−1). Tento pomocný h_t **není**
virtuální přírůstek N h_(t−1) použitý v přesném důsledku H.
Má zde jediný účel: absorbovat první člen E, protože C√H=N²/4.

Úloha požaduje reálné hodnoty; příslušná doména je h_s>0 pro
1≤s<t, h_0=1. Nuly mají nulové jmenovatele a záporné hodnoty
nejsou doménou reálných odmocnin. Na této doméně nevnucujeme
celočíselnost, dělitelnost ani rostoucí pořadí. To je přesně
minimum **odhadu**, nikoli automaticky skutečný program.

Polož y_s=ln h_s, y_0=0, y_t=ln H. Minimalizujeme

    S(y)=∑_(s=1)^t z_s,  z_s=exp(y_s/2−y_(s−1)).

Pro libovolný nenulový směr v=(v_1,…,v_(t−1)), v_0=v_t=0,
je druhá směrová derivace

    ∑z_s(v_s/2−v_(s−1))²>0.

Rovnost by totiž nutila postupně v_1=2v_0=0, v_2=2v_1=0,…
a tedy v=0. Funkce je přísně konvexní. Každý její stacionární
bod je proto jediné globální minimum na celé kladné doméně;
nepřehlížíme jiné místní minimum ani neprovedený okrajový test.
Pro t=1 nejsou volné proměnné a E=N²/4 přímo.

## P0769: všechny derivační kroky a uzavřený tvar

Derivace podle y_s, 1≤s<t, je z_s/2−z_(s+1). Ve stacionárním
bodě tedy z_s=2z_(s+1), neboli

    h_s³=4 h_(s−1)² h_(s+1).

Přejděme na x_s=lg h_s, X=lg H a D=2^t−1. Rekurence je

    x_(s+1)−3x_s+2x_(s−1)=−2.

Její obecné řešení je A2^s+B+2s: homogenní kořeny jsou1,2
a přímé dosazení2s dává pravou stranu−2. Z x_0=0 a x_t=X
vyjde B=−A, A=(X−2t)/D, tedy

    x_s=2s+(2^s−1)(X−2t)/D.                         (*)

Všechny h_s=2^x_s jsou kladné a mají požadované krajní hodnoty,
takže existuje právě nalezené globální minimum. Pro s=1 dává(*)

    (2^t−1)lg h_1=2^(t+1)−2(t+1)+lg h_t,

přesně mezivýsledek v odpovědi621.

## P0770: hodnota minima i limita t→∞

Máme z_1=√h_1=2·2^(A/2) a z_s=z_1/2^(s−1). Geometrický
součet je S_min=4(1−2^(−t))2^(A/2). Vynásobením C a rozepsáním
H=4N/π dostáváme

    E_min=(1−2^(−t))
          π^((2^(t−1)−1)/(2^t−1))
          N^(1+2^(t−1)/(2^t−1))
          /2^(1+(t−1)/(2^t−1)).

Každý exponent a faktor zde pochází z
2^(A/2)=H^(1/(2D))2^(−t/D). Pro t=1 formule vracíN²/4;
pro t=2 souhlasí s dříve doloženým dvouprůchodovým minimem.
Při pevném N a t→∞ je přesný poměr k N√(πN)/2 roven

    (1−2^(−t)) exp{(ln(4N/π)−2t ln2)/(2(2^t−1))}.

Konverguje k1 s chybou O((t+|ln N|)/2^t). To dokazuje i slova
„rapidly approaches“. Jde o limitu matematické funkce E; pro
takto rostoucí t nejsou její odvození jako asymptotiky algoritmu
ani přípustnost vypočtených přírůstků automaticky zachovány.

## P0771: všech osmnáct číselných údajů a jejich význam

Jediné dosazení(*) pro N=1000 reprodukuje po zaokrouhlení na
dvě desetinná místa všechny zveřejněné hodnoty:

|t|h_(t−1),…,h_1; h_0=1|
|---|---|
|3|57.64,6.13|
|4|135.30,22.05,4.45|
|5|284.46,67.23,16.34,4.03|
|10|9164.74,12294.05,7119.55,2708.95,835.50,232.00,61.13,15.69,3.97|

Soubor výsledků ukládá i nezaokrouhlené hodnoty a srovnání každé
položky. U t=10 je h_8>h_9 a několik přírůstků>N. Přesto jsou
to správné hodnoty **neomezeného kladného minima zadaného odhadu**.
Kniha u „optimum“ používá uvozovky; nevydáváme tuto řadu za platný
desetiprůchodový Shellsort ani numerický protipříklad k derivaci.
Dodatečné omezení přírůstků by znamenalo jinou optimalizační úlohu.

## P0772: platný dělitelnostní algoritmus a exponent na90

Pro pevné t a N→∞ dává(*)

    h_s*=c_s N^a_s,  a_s=(2^s−1)/(2^t−1),  c_s>0.

Pro s≥1 rostou poměry h_s*/h_(s−1)* jako
N^(2^(s−1)/(2^t−1)) a všechny jdou k∞. Největší skutečný
přírůstek má exponent a_(t−1)<1/2, takže N/h_s*→∞.
Všechny podmínky odvození P0767 jsou splněny a přírůstky jsou
nakonec přísně rostoucí a menší než N.

Pro dělitelnost zaokrouhli každý poměr h_s*/h_(s−1)* na nejbližší
kladné celé k_s a definuj h_0=1, h_s=k_1···k_s. Každý poměr
roste k∞, takže jeho relativní zaokrouhlovací chyba jde k0;
pro pevné t tedy h_s/h_s*→1 pro všechny s. Výsledné celé
přírůstky jsou dělitelné, splňují stejný asymptotický režim a
ve všech členech E zachovávají vedoucí ekvivalent.

MIX cena mimo9B je nejvýše řádu Nt pro pevné t. Dostáváme
skutečně realizovatelný průměrný čas

    O(N^(3/2+1/(2(2^t−1)))),

jak říká začátek90. Exponent s pevným t přísně klesá od2
k3/2; pro t=2 je5/3 a tedy také zaokrouhlené O(N^1.6667).
Tvrzení zde není přesná konečná optimalita neomezených reálných
hodnot pro všechny N a t ani optimum mezi nedělitelnými sekvencemi.

## P0773: bariéra3/2 pro dělitelné přírůstky

Při aspoň dvou různých skutečných přírůstcích je h_1≥2 a před
posledním průchodem máme podle P0757 rovnoměrnou h_1-ordered
permutaci. Poslední průchod má proto průměr přesně f(N,h_1).
Dolní mez P0766 platí uniformně pro2≤h_1≤N a dává

    f(N,h_1)≥c N^(3/2)√h_1≥c√2 N^(3/2).

Neodvozujeme ji z neuniformního vynechání faktoru(h_1−1)/h_1.
Jediný průchod má naopak průměr N(N−1)/4. Opakování téhož
přírůstku nepomůže: nadbytečný průchod již uspořádaných tříd
lze vynechat, poslední různý předchůdce je stále nejméně2.
Žádná dělitelnostní posloupnost tedy nemůže překročit průměrnou
bariéru Ω(N^(3/2)) směrem dolů. Není to dolní mez pro obecný
Shellsort s nedělitelnými přírůstky, o němž text dále hovoří.

Celá18 i odpověď621 jsou uzavřeny. P0772–0773 pokrývají celý
úvodní odstavec90; následují TheoremK/L a úlohy20–26. Změny
známých errat zůstávají mimo nálezy; žádný nový nález nevznikl.
