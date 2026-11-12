# §4.6.3: struktura sčítacích řetězců

Stav 2026-11-04: věty A–D, matematický text 466–471 po (25) a úlohy
11–14,16 uzavřeny. Věta C a úloha 14 mají [samostatný úplný rozbor](powers-two-small.md).
Úloha 15, věta E a další text zůstávají otevřeny. Historické odkazy se
neprohlašují za uzavřené bez uvedeného původního zdroje.

Nové testy jsou hotové a nesmějí se opakovat: `results/powers-structure.json`,
čtyři bloky, všechny exit 0. Předchozí minima 1–233 a 975 byla načtena
z uloženého výsledku; nebyla znovu počítána.

## 1. Značení, elementární vztahy a věta A

lambda(n)=floor(log2 n), nu(n) je počet jedniček. Malý krok nezvýší lambda;
každý jiný krok ji zvýší o 1. Hvězdový krok přičítá k poslední hodnotě
některou dřívější; zdvojení je zvláštní případ. l(n) je nejkratší délka
obecného řetězce, l*(n) nejkratší délka hvězdového řetězce. Pro řetězec
končící n, délky r a s malými kroky platí r=lambda(n)+s.

Řetězec lze seřadit a vypustit duplicity i nepotřebné členy větší než cíl,
protože každý kladný sčítanec je menší než součet. Složením řetězce pro m
s řetězcem pro n škálovaným faktorem m dostáváme l(mn)<=l(m)+l(n).
Po zdvojení musí být další krok hvězdový: součet dvou starších členů
by nepřekročil poslední hodnotu. Po velkém kroku musí být následující
krok malý nebo hvězdový: součet dvou ještě starších členů nedosáhne
následující mocniny dvou. Rekurence lambda/nu i binární horní mez v textu
z toho a z dvojkového zápisu přímo plynou.

Označme d počet zdvojení, f počet ostatních kroků a F_j Fibonacciho čísla,
F_0=0,F_1=1,F_(j+2)=F_(j+1)+F_j. Věta A říká n<=2^(d-1)*F_(f+3).
Indukce rozliší poslední zdvojení (pravou stranu násobíme dvěma), dva
poslední nezdvojovací kroky (sečteme meze s F_(f+2),F_(f+1)) a závěrečný
nezdvojovací krok po zdvojení. V posledním případě je n<=3a_(r-2) a stačí
3F_(f+2)<=2F_(f+3), protože rozdíl je F_(f+1)-F_f>=0.
Prázdný řetězec i první krok jsou přímé základní případy.
Mez je ostrá: po d zdvojeních na 2^d pokračujeme součty dvou posledních
členů; dostáváme 2^(d-1)*F_3,...,2^(d-1)*F_(f+3).

Je-li phi=(1+sqrt(5))/2, indukce dává F_(f+3)<=2*phi^f. Z n>=2^lambda(n)
a d+f=lambda(n)+s plyne f<=s*log(2)/log(2/phi). Malý krok není zdvojení,
tedy s<=f. Konstanta je menší než 3.271. Nezávislý přesný celočíselný
certifikát používá phi<809017/500000 a identitu
phi^3271=F_3271*phi+F_3270; ověřuje 2^2271>phi^3271. Tím nevycházíme
jen ze zaokrouhleného logaritmu. Růst a_i<=2^i dává l(n)>=ceil(log2 n)
a přesné hodnoty pro jedno- a dvojbitová čísla.

## 2. Obecný důkaz šesti typů (B)

Před prvním malým krokem jsou jen mocniny dvou. První malý krok má tvar
U=2^A+2^B, A>B>=0. Po C zdvojeních je poslední číslo 2^C U.
Pokud C=0, zachování počtu malých kroků dovoluje jako
nezdvojení jen 2^(A+1) nebo V=2^(A+1)+2^B. První volba dává typ 6,
druhá typ 2. Po V může následovat další nezdvojení jen bez vloženého
zdvojení a při B=A-1; výsledkem je 2^(A+2), tedy typ 3.

Pokud C>0, po zdvojení musí následovat hvězdový krok. Maximum jiného
sčítance je polovina posledního čísla. Přechod přes další mocninu dvou
je tak možný jen pro B=A-1. Sčítanec 2^(C-1)U dává 9*2^(A+C-2), typ 5;
navíc při C=1 lze přičíst původní 2^A a získat 2^(A+2), typ 4.
Po typu 5 není další nezdvojení možné: bez předchozího zdvojení je součet
s největším starším číslem jen 15*2^(A+C-2), pod další mocninou 16*2^(A+C-2).
Po zdvojení je poměr k vedoucí mocnině pouze 9/8, takže ani přičtení
poloviny nestačí. Po dosažení čisté mocniny dvou jsou další kroky
bez nového malého kroku nutně zdvojení. Ukončení v libovolné fázi dává
právě šest knižních typů. Každý konec má nu<=2, a tedy pro tři jedničky
je l(2^A+2^B+2^C)=A+2.

Program generuje typy a nezávisle všechny řetězce s nejvýše jedním malým
krokem. Počty typů 1 až 6 do délky 14 jsou 455,364,66,66,286,364.
Nejde o náhradu obecného důkazu, ale kontrolu klasifikace a přepisu.

## 3. Úlohy 11–12: optimální prefixy a nemožnost nekonečného stromu

Nově úplně vypsané cesty, jejichž každý prefix je optimální, jsou:

- 43: 1,2,3,5,10,20,(23 nebo 40),43;
  nebo 1,2,4,8,9,17,(26 nebo 34),43.
- 77: 1,2,4,8,9,17,34,(43 nebo 68),77;
  nebo 1,2,4,5,9,18,36,(41 nebo 72),77.
- 149: 1,2,4,5,9,18,36,72,(77 nebo 144),149;
  nebo 1,2,4,8,16,17,33,66,(83 nebo 132),149.

Každé dvě z těchto hodnot mají kompatibilní dvojici cest, ale žádná
ze 64 trojic není slučitelná v jediném stromu s jedním výskytem každého
čísla. Program kontroluje shodu rodiče všech společných vrcholů.
Úplnost výčtu plyne z generování všech součtů dřívějších členů a z přesných
uložených minim. U prefixově optimální cesty musí být každý krok hvězdový:
při nepoužití předchozího členu jej lze vypustit a prefix zkrátit.

Slučitelnost 43 a 77 vynucuje u 77 prefix 1,2,4,8,9,17,34.
První dvojice cest k149 má rodiče9 rovného5, místo vynuceného8;
druhá má rodiče17 rovného16, místo vynuceného9. To je také přímé
ruční vysvětlení nekompatibility všech trojic.

Úloha 11 tedy souhlasí. Pro úlohu 12 je trojice 43,77,149 samostatný
konečný důkaz nemožnosti nekonečného optimálního stromu. Nápad pochází
z úvodu autorské stránky Achima Flammenkampa, ale výčet a kontrola všech
kompatibilit jsou naše. Výrok neříká, že 149 je nejmenší možná překážka.

Tři nové bloky: prefix 7030 stavů, 64 nekompatibilních trojic;
one_small 1601 řetězců s jedním malým krokem do délky 14;
cases 648 hvězdových konstrukcí všech čtyř případů C s nejvyšším bitem <=16.
Časy 0.025421830, 0.127652871 a 0.089744833 s. Žádné selhání ani opakování.

## 4. Konstrukce úlohy 13 a úloha 16

V této části A>B>C>D>=0 jsou pozice čtyř jedniček cíle.
Všechny následující řetězce jsou hvězdové a mají A+2 kroků. Dolní mez
A+2 již plyne z klasifikace jediného malého kroku, nezávisle na celé větě C.

1. A-B=C-D. Položme u=B-D, v=C-D. Nejprve 2^u+1 (u+1 kroků),
   v zdvojení a přičtení uloženého 2^u+1, potom D zdvojení.
2. A-B=C-D+1. Položme t=C-D, u=B-D. Nejprve 2^t, přičtení 1,
   přičtení 2^t; máme 2^(t+1)+1. Po u zdvojeních přičteme uložené
   2^t+1 a provedeme D zdvojení.
3. A-B=3, C-D=1. Položme v=B-D. Řetězec 1,2,3, poté v zdvojení,
   přičtení 1 a násobení dosažené hodnoty třemi dvěma hvězdovými kroky;
   nakonec D zdvojení. Výsledkem je 2^D*3*(3*2^v+1).
4. A-B=5, B-C=C-D=1. Použijeme 1,2,3,6,9,18,27,54,108,135,
   potom D zdvojení.

Úloha 16: binární délka b(n)=lambda(n)+nu(n)-1 má podíl k lambda(n)
roven 1 na n=2^k a roven 2 na n=2^(k+1)-1, pro k>=1. Limita neexistuje.

## 5. Věta D a horní asymptotika (25)

Nechť k>=1 je celé, m=2^k a n>=m má t+1 číslic v základu m.
Hornerova konstrukce se všemi předpočítanými mocninami 1,...,m-1 stojí
nejvýše m-2+(k+1)t kroků. Po odstranění opakovaných počátečních hodnot
je hvězdová: první nová hodnota a splňuje m-1<a<=2(m-1), takže ji lze
připojit jako (m-1)+(a-(m-1)); rozdíl už je předpočítaný. Dále jsou všechny
kroky přímo hvězdové. Pro n<m místo toho stačí sériový řetězec délky n-1.
Proto pro všechna n>=1 platí knižní ostrá horní mez

    lambda(n) <= l(n) <= l*(n) < (1+1/k)*log2(n)+2^k.

Zvolíme-li k=floor(log2(lambda(n))/2), pak k roste do nekonečna,
2^k<=sqrt(lambda(n)) a podíl horní meze k lambda(n) konverguje k 1.
To dokazuje obě limity ve větě D.

Pro přesnější mez označme M=lambda(n), L=lambda(M), J=lambda(L).
Pro velké n zvolme k=L-2J. Pak 2^k<=4M/L^2 a
1/k=1/L+O(log(L)/L^2). Protože log2(n)=M+O(1), dostáváme
l*(n)<=M+M/L+O(M*log(L)/L^2), což je (25), včetně celočíselných podlah.
Tato horní mez neprokazuje skoro-všude dolní mez; ta patří až k větě E.
Vynechání sudých číslic v předpočítání na 466 odpovídá přinesení liché
části číslice o příslušný počet zdvojení dříve; známé erratum 2008 výslovně
přidává dělení 2^e, nejde o nový nález.

## 6. Rozsah kontrol, errata a zdroje

Čtvrtý blok enumeruje všechny rostoucí řetězce do délky 13 s nejvýše
dvěma malými kroky: 14 s nulou, 1266 s jedním a 108029 se dvěma.
Potvrzuje A, korolár, základní vztahy kroků a C. Sedm uložených příkladů
39*2^d zachycuje doplňkovou větev rozebranou v poznámce o C.
Čtyři bloky dohromady 1.162433024 s; žádné selhání a žádné opakování
již dokončeného bloku. Obecné důkazy jsou výše a v doprovodné poznámce.

Errata jsou v již uloženém šestivrstvém logu `sources/powers-basic-errata.txt`.
Relevantní změny: přidání199 mezi de Jonquieresovy chybné údaje (2005),
přesunuté liché části číslic (2008), pojmenování Corollary A (2011),
exponent m-1 místo m+1 na470 (1998), oprava formulace11 na „all a_i“
(2015), upřesnění m v úloze14 (2008). Jde o známá errata.
Oprava negace osmi vzorů v odpovědi15 (1998) se týká dalšího bloku.

Primární čtení a limity:

- [Flammenkamp, autorská stránka](https://wwwhomes.uni-bielefeld.de/achim/addition_chain.html):
  úvod, definice a část tabulky; inspirace pro trojici43/77/149, kterou jsme
  následně nezávisle ověřili. Nejde o audit celé rozsáhlé tabulky.
- [Flammenkamp, publikace](https://wwwhomes.uni-bielefeld.de/achim/publications.html):
  metadata diplomové práce1991. Odkázaný adds.dvi nástroj neumí číst,
  takže původní klasifikace tří malých kroků ještě není přečtena.
- [Thurber1973](https://msp.org/pjm/1973/49-1/pjm-v49-n1-p25-p.pdf):
  text229–231 a začátek232, definice, lemmata1–4, vyjádřeníC a začátek
  důkazu pro nu>=9. Bez celého důkazu a bez vizuálního čtení vzdáleného PDF.
- [Clift, Small Step Enumeration](https://additionchains.com/SmallStepEnumeration.html):
  celá úvodní stránka, čtyři oblasti pro dva malé kroky odpovídají C;
  odkázané výstupy pro tři a více kroků zatím nebyly čteny.
- Brauerův AMS PDF odmítl přístup403; zkusená adresa Project Euclid byla
  nedostupná. Původní článek tím není ověřen; matematický důkaz D je vlastní.

Kniha466–471 a693 byla čtena vizuálně, úlohy481–482 již v předchozím bloku.
Ostatní nyní vyrenderované strany472–477,694 zatím jen textově; samotný
vznik obrázku není záznam jeho přečtení. Žádný nový nález v tomto bloku.
Úloha15 a zbytek sekce zůstávají otevřené.
