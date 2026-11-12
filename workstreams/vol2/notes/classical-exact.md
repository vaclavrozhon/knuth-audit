# §4.3.1-40: přesné dělení z obou stran

Stav2.11.2026: matematika dělení a korektní spojení obou částí dokázány;
**uniformní tištěný zbytek O(n) při pevném malém základu zůstává partial**.
Jasný lokální tiskový problém je zvlášť potvrzen jako C0099. Nesměšovat
jej s dosud nerozhodnutou silnější časovou interpretací.

Zadání284 a odpověď629 vizuálně přečteny, stejně jako změna bibliografie
z28.12.2000 na str.38 all2-prepre. Ostatní tři vrstvy a současný err2 TeX
prohledány podle strany, čísla úlohy i témat. Chybějící dělení b neopravují.

## Dolní část podílu

Nechť U=VQ, V>0 a U,V jsou nezáporná celá čísla, zapsaná v základu
b=2^w, w>=1. Číslice jsou0..b-1. Odstraníme ze V nejvyšší dělící
mocninu2, současně ze U, což zachovává Q a vede k lichému V. Uložení po
slovech umožňuje najít tuto mocninu průchodem přes koncová nulová slova
a jedním počítáním koncových nul v prvním nenulovém slově. Posun stojí
O(n) slovních operací. Tuto redukci netvrdíme pro libovolný nebinární
základ se stejně levnou implementací.

Nechť c je inverze V modulo b. První číslice Q je q_0=c*(U mod b) mod b.
Potom **U_1=(U-q_0 V)/b** a U_1=V*floor(Q/b). To je přesná rekurence
pro další číslice. Pokud hledáme jen k dolních míst, stačí průběžně
uchovávat zbytek U_j modulo b^(k-j) a stejný počet nejnižších míst V.
Po odečtení je nejnižší místo nula; jeho zahození je dělením b. Vyšší
vynechané násobky b^(k-j) nemohou ovlivnit žádnou zbývající číslici.

Pro k>=1 potřebujeme k součinů s inverzí a při j=0..k-2 dalších
k-j součinů číslic s číslicí q_j. Celkem

```
k + sum_(j=0)^(k-2) (k-j) = k(k+3)/2-1.
```

Poslední odečtení není potřebné. Pro k přibližně n/2 je hlavní člen
n^2/8. Čistě pravostranné získání n míst má hlavní člen n^2/2.
Inverze jednoslového V mod b se počítá jednou, např. postupem41.

## Zaručené spojení s horní aproximací

Pouhé zřetězení přibližných horních a přesných dolních číslic může selhat
kvůli přenosu. Níže doplňujeme algoritmus s přesnou mezí; není to doslovný
přepis algoritmu H z citovaného článku.

Předpokládejme b^(n-1)<=V<b^n a U<b^(2n). Krátkou binární normalizací
dostaneme A=dU, B=dV, kde b^n/2<=B<b^n, d je mocnina2 a d<=b/2.
Označme alpha=A/b^(2n), beta=B/b^n; tedy1/2<=beta<1 a Q=b^n alpha/beta.
Dolních k=floor(n/2) míst, Q_L=Q mod b^k, už známe přesně.

Vybereme celé g>=0 tak, aby pro L=n-k+g platilo

```
b^g > 4*(b+(b+1)L).                                      (1)
```

Pro horní výpočet začneme R_0=floor(alpha b^L). V krocích j=0..L-1
zavedeme D_j=floor(beta b^(L-j)), nastavíme q_j=floor(R_j/D_j)
a R_(j+1)=R_j-q_j D_j. D_j vznikají vždy odstraněním nejnižšího slova
předchozího D; počáteční D_0 je prefix B, případně doplněný nulami.
Nemusíme konstruovat dlouhé zlomky alpha a beta; jsou to jen posuny.

V prvním kroku q_0<b, protože alpha<d<=b/2 a D_0>=b^L/2.
V dalších krocích R_j<D_(j-1)<=bD_j+b-1, zatímco D_j>=b/2. Odtud
q_j<=b+1. Pokud q_j>=b, odečteme nejprve bD_j posunem a dopočítáme
jednu obyčejnou číslici. Výpočet jedné číslice používá dva či tři
nejvyšší údaje a korekci D3/D6 s normalizovaným D_j; nevolá obecné
víceslové dělení. Případ jednoslového D_j je strojové krátké dělení.
Redundantní číslice b a b+1 lze na konci převést běžným přenosem.

Položme y=sum q_j b^(-j), theta=alpha b^L-R_0 a
eta_j=beta b^(L-j)-D_j. Hodnoty theta a eta_j leží v[0,1). Z rovnic
algoritmu dostaneme přesnou identitu

```
(alpha-beta*y)b^L = R_L+theta-sum q_j eta_j.
```

Protože R_L<D_(L-1)<b a q_j<=b+1, plyne

```
|alpha/beta-y| < 2*(b+(b+1)L)/b^L,
|Q-b^n y| < b^k/2                                       (2)
```

z volby(1). Horní část podílu tedy získáme jako nejbližší celé číslo
k `(b^n y-Q_L)/b^k`; mez(2) vylučuje poloviční rovnost. Výsledné
Q=Q_H b^k+Q_L je vždy přesné. Ke spojení je potřeba jen sčítání,
zaokrouhlení a posuny, ne opětovné plné násobení VQ. V kontrolním
programu se VQ používá pouze v nezávislém orákulu.

## Přesný rozsah nákladů a zbývající otázka

Měříme hlavní počet **jednoslových součinů** stejně jako citovaná analýza,
nikoli naměřený čas Pythonu. Klasický D potřebuje n(n+1) součinů pro
2n-místný dělenec a n-místný dělitel. Horní postup má pro délky L až2
právě L(L+1)/2-1 součinů v odčítací smyčce, navíc O(L) součinů při
odhadu číslic. Dolní má výše uvedených k(k+3)/2-1. Pro pevné g tedy
součet je n^2/4+O(n), což vysvětluje přibližnou75% úsporu.

Pro běžný velký slovní základ stačí g2, pokud
`b^2>4*(b+(b+1)*(n-k+2))`. V tomto výslovně daném rozsahu jde o
**záruku pro všechny vstupy**, bez pravděpodobnostního předpokladu.
Například n512,b=2^32:66561 hlavních součinů oproti262656 v D, poměr
0.253415;377 dalších odhadových součinů je uloženo zvlášť. Srovnání
nezamlčuje tyto nižší členy ani nezaměňuje součiny za celkový čas.

Při pevném malém b může(1) vyžadovat g=O(log_b n). Tato konstrukce pak
prokazuje n^2/4+O(n log n), a tedy stejnou asymptotickou75% úsporu,
ale **nikoli uniformní tištěné O(n)**. Z této mezery nevyvozujeme, že
jiný algoritmus takovou mez nemůže splnit. Silnější interpretace zůstává
otevřená k dalšímu doložení. Úloha je proto zatím evidována jako partial,
přestože C0099 je už samostatně confirmed.

## Primární článek a bibliografie

Vizuálně přečteny str.1–7 zprávy Krandick–Jebelean, RISC94-50,
*Bidirectional Exact Integer Division* (1994), PDF2–8. Zdroj:
[veřejný archiv RISC](https://ftp.risc.uni-linz.ac.at/pub/techreports/1994/94-50.ps.gz).
Její H počítá zkrácený součin se známou horní mezí vynechání a výsledek
certifikuje porovnáním zbytku. Může ohlásit neúspěch; úvod i analýza
výslovně diskutují vysokou pravděpodobnost úspěchu při velkém slovním
základu a náhodných datech. Trojúhelníkový počet součinů odpovídá
knižnímu argumentu. Náš důkaz(1)–(2) navíc řeší nejistotu horního prefixu
při spojení s přesnou dolní částí, za uvedenou cenu rezervních míst.

Bibliografická změna2000 odkazuje na časopiseckou verzi1996,441–455,
[metadata vydavatele](https://www.sciencedirect.com/science/article/pii/S0747717196900243).
Její plný text se nepodařilo získat (403); předtisk1994 za něj
nevydáváme. Schönhage–Vetter1994,448–459 je potvrzen v
[seznamu autora](https://pages.iai.uni-bonn.de/schoenhage_arnold/publis.html),
ale plný text dosud přečten nebyl. Rozdíly mezi těmito verzemi mohou
být významné právě pro zbývající silnější časovou otázku.

## Kontroly

`verify_classical_exact.py`, tři úspěšné checkpointy, běh12635 exit0:

- 21523 úplných malých vstupů: b2,n2..7 a b4,n2..3, všechny n-místné
  V a všechny nezáporné přesné podíly s VQ<b^(2n).5733 korekcí D6.
- 800 dalších dvojic až64 slov a šest nákladových případů až512 slov,
  základy2..2^32.64 redundantních horních číslic a440 korekcí D6
  v náhodné větvi. Vstupy zahrnují sudé V, jejichž mocnina2 se odstraní.
- Samostatná reprodukce C0099 včetně přesných délek zadání.

Všechny výstupy porovnány s nezávislým celočíselným dělením; každý běh
navíc přesně ověřuje mez(2) racionální aritmetikou. Úspěšné bloky
bez nové pochybnosti neopakovat.
