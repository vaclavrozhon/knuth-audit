# §7.1.1–5: converse nonimplication, dosažitelnost a minima

6. listopadu 2026, X0060. Zadání p80/file97, odpověď p535/file552;
originály images/file097.png a images/proof-file552.png. Zdroj odpovědi
sources/proof-file552.pdf. V zadání se úloha 4 přenáší na základní
operaci C(a,b)=¬a∧b, tj. řádek 0100 Table 1. Nejde o implikaci.
Cena je opět počet uzlů stromu formule; zkratky se při výskytu opakují,
nikoli sdílejí. Žádný matematický program či enumerace formulí.

## P0557–P0558: bez konstant přesně šest funkcí, všechny minimální

**P0557:** C(A,B) implikuje B. Indukcí podle stromu proto každý
term bez konstant implikuje svůj pravý krajní list, tedy x nebo y.
Jeho jedničky jsou podmnožinou {10,11}, nebo podmnožinou {01,11}.
Sjednocení všech těchto možností dává právě tabulky
0000,0001,0010,0011,0100,0101. Zbývajících deset nelze vyjádřit.

**P0558:** všech šest možností skutečně vzniká, přesně podle odpovědi:

| tabulka | formule | cena |
|---|---|---:|
| 0000 | C(x,x) | 1 |
| 0001 | C(C(x,y),y) | 2 |
| 0010 | C(y,x) | 1 |
| 0011 | x | 0 |
| 0100 | C(x,y) | 1 |
| 0101 | y | 0 |

Pro AND je C(C(x,y),y)=¬(¬x∧y)∧y=(x∨¬y)∧y=xy.
Ostatní významy jsou definice. Jedinou nulovou cenou mají x,y.
Jednou operací nad x,y vznikají jen 0,0010,0100, proto AND
vyžaduje alespoň 2; všechny zbývající ceny jsou také minimální.

## P0559: každá vytištěná formule s konstantami

Polož U=C(y,x)=x∧¬y, V=C(x,y)=¬x∧y,
A=C(x,1)=¬x, B=C(y,1)=¬y a R=C(y,A)=¬x∧¬y.
Cena U,V,A,B je 1 a R má cenu 2. Odpověď přesně přepisuje:

| tabulka | formule | cena | výskyty proměnných |
|---|---|---:|---:|
| 0000 | 0 | 0 | 0 |
| 0001 | C(B,x) | 2 | 2 |
| 0010 | U | 1 | 2 |
| 0011 | x | 0 | 1 |
| 0100 | V | 1 | 2 |
| 0101 | y | 0 | 1 |
| 0110 | C(C(U,C(V,1)),1) | 5 | 4 |
| 0111 | C(R,1) | 3 | 2 |
| 1000 | R | 2 | 2 |
| 1001 | C(U,C(V,1)) | 4 | 4 |
| 1010 | B | 1 | 1 |
| 1011 | C(V,1) | 2 | 2 |
| 1100 | A | 1 | 1 |
| 1101 | C(U,1) | 2 | 2 |
| 1110 | C(C(B,x),1) | 3 | 2 |
| 1111 | 1 | 0 | 0 |

C(U,C(V,1))=¬U∧¬V=¬(U∨V) je ekvivalence, protože U,V
jsou dva nesouhlasné vstupy. Jeho doplnění dává XOR.
C(B,x)=xy, R=¬(x∨y), ostatní řádky jsou uvedené negace
nebo původní zkratky. Tím jsou vyřešeny všechny jednotlivé formule
a úplnost se všemi šestnácti funkcemi, nikoli jen abstraktní báze.

## P0560: úplné dolní meze s konstantami

Cena 0 připouští pouze 0,1,x,y. C nad dvěma takovými listy dává
jen tyto čtyři funkce a navíc ¬x,¬y,U,V. Proto AND, NOR a obě
implikace potřebují alespoň 2; jejich horní formule mají cenu 2.
Negace,U,V potřebují ≥1 a projekce/konstanty ≥0.

U minimální formule C(a,b)=f je f podmnožinou b. Je-li b=f,
samotný podstrom b je kratší formula pro f, což je spor minimality.

Pro OR=0111 jsou možné nadmnožiny pouze OR a 1; proto b=1
a a=NOR. Cena OR je nejméně 2+0+1=3.
Pro NAND=1110 analogicky musí být b=1, a=AND; cena je nejméně 3.

Zbývají ekvivalence E=1001 a XOR X=0110.
Vezmi nejkratší formuli mezi E a X. Žádný její potomek nemůže
počítat E ani X: byl by kratším prvkem téhož páru.

Je-li kořen E, nadmnožiny pro b jsou E,1011,1101,1.
E je vyloučena; b=1 by vyžadovalo a=X, také vyloučeno.
Při b=1011 musí a být 0010 nebo X; po vyloučení X zůstává U.
Při b=1101 musí a být 0100 nebo X; zbývá V.
Cena je v obou případech alespoň 1+2+1=4.

Je-li kořen X, nadmnožiny pro b jsou X,OR,NAND,1.
X je vyloučena; b=1 by vyžadovalo a=E, také vyloučeno.
Při b=OR musí a být AND nebo E, při b=NAND musí být a=NOR
nebo E. V obou případech po vyloučení E má a cenu ≥2 a b≥3,
takže tento minimální kořen stojí alespoň 6.

Nejmenší cena v páru je tedy alespoň 4. Nyní již obecná minimální
formula pro X může mít b=1 a a=E, ale to stojí ≥4+1=5.
Jiné větve mají b=OR/NAND a a=AND/NOR nebo E, tedy stojí ≥6.
Proto X potřebuje nejméně 5 a E nejméně 4. Vytištěné formule
těchto mezí dosahují. Jde o nekruhový minimální argument, nikoli
předpoklad hodnoty E použitý k důkazu téže hodnoty.

Tím jsou doloženy dolní meze všech šestnácti řádků.

## P0561: sekundární počet proměnných a návaznost algoritmu

Každá podstatná proměnná se musí vyskytnout. Pokud se ve stromu C
vyskytuje právě jednou, jediná cesta ke kořeni mění polaritu při
průchodu levým vstupem C a zachovává ji při pravém. Celková
monotónní orientace je tedy pevná nezávisle na ostatních vstupech.
E a X mají opačné orientace podle druhého vstupu, takže potřebují
po dvou výskytech obou proměnných. Všechny uvedené formule mají
nejmenší možný počet výskytů (0,1,2 nebo4) i bez podmínky minimální
délky. Žádná další preferovaná formula v odpovědi tedy nezůstala
bez kontroly.

Korektnost cenového generování z odpovědi 4 se přenáší beze změny:
C je pevná binární funkce a nahrazení podstromu stejnou levnější
funkcí zachová výsledek. P0554 dokazuje příslušný invariant a úplnost.
Zde bylo vše odvozeno bez spuštění takového generátoru.

Bernsteinův historický odkaz je explicitně neověřenou bibliografií.
Žádný rozpor, kandidát nebo celostránkové uzavření p80/p535:
na obou stranách zůstávají další samostatné úlohy.
Další úloha 6 včetně obecného algebraického dodatku a počtu prvků.
