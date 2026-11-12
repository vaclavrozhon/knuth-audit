# Historické a bibliografické odkazy v §4.6.1

Kontrola 4. listopadu 2026. Rozsah: odkazy u Gaussova lemmatu na straně
422, dějiny polynomiálního gcd na 424, determinantové metody na 434–435
a související odkazy odpovědí 12, 15 a 16 na 674–675. Zkratka gcd označuje
největšího společného dělitele; nad tělesem je určen až na nenulový skalár.
Tento blok nepřidává nový nález. Matematické jádro sekce má samostatné
důkazy v [základním bloku](polynomial-division-basic.md),
[subresultantech](subresultants.md) a [Sturmově větě](sturm-cf.md).

Rozlišujeme původní publikaci, pozdější přetisk, preprint a bibliografická
metadata. Ověření historického odkazu zde znamená nalezení příslušného
výsledku v uvedeném prameni; není důkazem, že nikde na světě neexistoval
starší předchůdce. Přesné lokální soubory, URL a hashe jsou v
`sources/polynomial-history.json`. Nezdařená stažení jsou zaznamenána
odděleně a nejsou důkazem obsahu článku.

## 1. Gauss 1801, §42

Originál *Disquisitiones arithmeticae* byl získán z digitální knihovny
Humboldtovy univerzity. Vizuálně přečten titul z roku 1801 a tištěné
strany 36–38, kde začíná a končí §42 (PDF 5, 56–58).

Gauss pracuje s monickými polynomy s racionálními koeficienty. Pokud
některý z jejich koeficientů není celé číslo, jejich součin nemůže mít
všechny koeficienty celé. Nejde doslova o moderní formulaci pomocí
primitivních částí nad libovolným oborem s jednoznačným rozkladem;
jde o příslušný celočíselný předchůdce. Knuthův odkaz je věcně správný.

Mechanismus důkazu lze vyjádřit takto. Pro prvočíslo p označíme v_p(a)
exponent p v nenulovém racionálním čísle a. Minimum těchto exponentů
přes koeficienty součinu je součtem minim pro oba činitele: po vydělení
příslušnými mocninami p stačí redukovat modulo p; součin dvou nenulových
polynomů nad tělesem se p prvky je nenulový. U monického polynomu je
minimum nejvýše nula. Záporné minimum jednoho činitele tedy dává záporné
minimum součinu. Toto také vysvětluje vztah k modernímu Gaussovu lemmatu.
Celých 703 stran souboru kontrolováno nebylo.

## 2. Nuñez 1567 a Stevin 1585/1634

Nuñezův *Libro de algebra en arithmetica y geometria* má na původním
titulu jméno **Pedro**, místo **En Anvers** a rok **1567**. Přečteny
PDF 3 a 283–285, tj. titul a folia 127r–128r. Na foliu 127v je hledán
společný dělitel výrazů, které v dnešní notaci jsou

```text
A = x^3 + x^2 = x^2(x+1),
B = x^2 + 7x + 6 = (x+1)(x+6).
```

Autor navrhuje tabulku součinů lineárních výrazů a zvláštní pravidla,
nikoli obecný eukleidovský algoritmus. Záhlaví tohoto listu skutečně
říká „PARTE SEGVNDA“; Stevinův popis začátku třetí části proto nepoužíváme
jako přesnou moderní lokalizaci. Tato nepřesnost převzatého starého odkazu
není tvrzením Knuthova textu, který část Nuñezovy knihy neuvádí.

Původní Stevinovo *L'Arithmetique* z Leidenu 1585 je dostupné v ETH
e-rara. Vizuálně přečten titul a strany 240–242 (IIIF canvasy 5,
267–269). Problém LIII na 240–241 výslovně požaduje největší společnou
míru dvou algebraických výrazů, zmiňuje Petra Nonia a popisuje opakované
dělení stejně jako u celých čísel. Jeho konkrétní výpočet je

```text
A - x B = -6x^2 - 6x = C,
B - (-1/6) C = 6x + 6 = D,
C = (-x) D.
```

První krok ještě nedává zbytek menšího stupně než B, ale zachovává
společné dělitele; další krok stupeň sníží. Výsledek D je správný:
A/D = x^2/6 a B/D = x/6+1 jsou nesoudělné. Problém LIV na 242 používá
výsledek ke krácení zlomku. Historické tvrzení o Stevinově použití metody
je tedy doloženo přímo v edici 1585, nikoli jen pozdějším odkazem.

Samostatně přečten i titul Girardova vydání *Les Oeuvres Mathematiques
de Simon Stevin* 1634 a citovaná strana 56 (canvasy 7 a 68; navíc
prohlédnuta 57). Obsahuje tentýž problém a výpočet. Číslo strany 56
v Knuthově citaci je správné. Canvasy 285, 295 a 305 vydání 1585
byly jen navigační vzorky; canvas 4 vydání 1634 je prázdný list,
nikoli titulní strana.

**Známá errata:** all2-prepre, tištěná strana 24, oprava z 28. října
2000 mění Pablo na Pedro. all2-pre, strana 11, doplnění z 30. ledna
2022 označuje Nuñeze jako portugalského a Stevina jako vlámského
matematika. Originální tituly dokládají Nuñezovo spojení s portugalským
králem a Coimbrou a Stevinovo „de Bruges“; nejde o nové chyby auditu.

## 3. Bareiss, Habicht, Loos a determinantové identity

Bareissova časopisecká práce je *Sylvester's Identity and Multistep
Integer-Preserving Gaussian Elimination*, Math. Comp. 22 (1968),
565–578. Stažení z AMS vrací 403. Místo předstírání přečtení tohoto
PDF používáme původní autorův preprint ANL-7213 z května **1966**,
uložený v OSTI. Vizuálně přečten titul a strany 4–8 (PDF 1, 6–10).
Na stranách 6–7 jsou přesně dělená rekurze (10) a její interpretace
pomocí minorů (13); strana 8 rozvíjí více kroků najednou. Rok preprintu
není opravou roku časopisecké citace.

Základní matematickou souvislost lze dokázat přímo. Nechť A je matice
nad oborem integrity, tedy komutativním okruhem bez dělitelů nuly.
Minor je determinant podmatice. Pro I=(1,...,k-1) položme

```text
d = det A[I,I],
B_uv = det A[I,u ; I,v]       (u,v >= k).
```

Zápis A[I,u ; I,v] znamená ponechat řádky I následované u a sloupce I
následované v, v uvedeném pořadí. Pak pro i,j>k platí

```text
B_kk B_ij - B_ik B_kj = d det A[I,k,i ; I,k,j].        (H)
```

Důkaz: pro obecnou matici s nezávislými neurčitými prvky přejdeme do
tělesa racionálních funkcí a eliminujeme blok A[I,I]. Zbylý blok 2×2
má determinant rovný příslušnému velkému minoru dělenému d, zatímco
jeho jednotlivé prvky jsou B_uv/d. Po vynásobení d² vznikne (H).
Jde o polynomiální identitu s celočíselnými koeficienty, a proto platí
po libovolné specializaci i tehdy, když d=0. **Výpočet podílu** v
Bareissově algoritmu ovšem vyžaduje d nenulové; identita sama neopravňuje
dělit nulou. Pro nenulové d je dělení přesné a výsledkem je opět minor.

Subresultanty jsou polynomy složené z minorů koeficientové matice dvou
polynomů a jejich posunů. Opakované použití téhož vztahu při eliminaci
vedoucích koeficientů vysvětluje přesné normalizační faktory. Úplné
vlastní odvození těchto faktorů, včetně větších poklesů stupně, je
v [subresultants.md, §§2–3](subresultants.md).
Tím je doložen matematický smysl Knuthovy opatrné formulace, že obecná
determinantová eliminace zahrnuje C jako speciální případ. Netvrdíme,
že libovolné pivotování v matici provádí doslova stejné instrukce jako C.

Nezávislý primární článek Lionela Ducose, *Algorithme de Bareiss,
algorithme des sous-résultants*, RAIRO 30(4) (1996), 319–347, výslovně
rozvíjí společný formalismus obou metod. Přečteny 319–320, 322–323,
335–336 (PDF 2,3,5,6,18,19), včetně algoritmu v §5.1. Tento rozsah
potvrzuje souvislost a bibliografii; vlastní důkaz neopíráme o tvrzení,
že byly zkontrolovány všechny Ducosovy mezilehlé věty.

Habichtův článek *Eine Verallgemeinerung des Sturmschen
Wurzelzählverfahrens*, Comm. Math. Helv. 21 (1948), 99–116, získán
z e-periodica. Vizuálně čteny 99–103 a 116 (PDF 2–6,19). Úvod
skutečně řeší zbytkové posloupnosti pomocí determinantů s polynomiální
závislostí na koeficientech a jejich specializaci; závěr vztahuje metodu
ke Sturmovu počtu reálných kořenů. Datum doručení 14. května 1947 na
116 není rozpor s publikací 1948. Všechny důkazy na 104–115 se zde
znovu neauditují.

Loosova kapitola *Generalized Polynomial Remainder Sequences*,
Computing Supplementum 4 (1982), 115–137, je potvrzena metadaty
Springeru i původní první stranou 115 v dostupném náhledu. Abstrakt
výslovně spojuje Habichtův přístup, subresultanty a algoritmy
Brown–Collins. Další strany celé kapitoly získány nebyly. Druhá Loosova
kapitola, *Computing in Algebraic Extensions*, 173–187, má již ověřený
bibliografický záznam v předchozím bloku. Aritmetické použití resultantů
má vlastní důkaz v subresultants.md; nejde o audit celých obou kapitol.

## 4. Chiò, Dodgson a Knuthova citace na 435

Knuthovo *Overlapping Pfaffians* bylo získáno jako arXiv preprint
math/9503234 z března 1995. Přečteny strany 1,4–8,10; relevantní
§3 o determinantech je na 5–8. Rekurze kondenzace (3.9)–(3.10)
pracuje se sousedními minory a správně upozorňuje na možné nulové
jmenovatele. Jejím algebraickým podkladem je rovněž (H), po příslušném
uspořádání řádků a sloupců. Příbuznost s přesným dělením v C je správná.

Oficiální časopisecký záznam přiřazuje článek k Electronic Journal of
Combinatorics **3(2), #R5 (1996)**, přestože zároveň uvádí datum
online publikace 14. května 1995. Rok 1995 na arXivu tedy **není**
protipříkladem Knuthově citaci roku 1996. Oprava z 3. března 2021
doplňuje v citaci strany 1–13; jde o známou změnu.

Oprava z 9. března 2013 mění historickou větu na připsání metody
Felici Chiòovi v roce 1853 a pozdější znovuobjevení Dodgsonem. Tuto
opravu jsme přímo přečetli v all2-pre, strana 11. Chiòova původní
32stránková brožura zde nebyla získána. Nezaměňujeme proto kontrolu
existence této autorovy opravy za nezávislé potvrzení celé priority
či doslovné totožnosti různých variant kondenzace. Žádný nový nález
z této neúplnosti nevzniká.

## 5. Gram–Schmidt, odpověď 15

Z GDZ získány původní články J. P. Grama, Crelle 94 (1883), 41–73,
a Erharda Schmidta, Math. Ann. 63 (1907), 433–476. U Grama
přečteny titulní 41 a závěrečné 71–73; nejde o ověření všech jeho
konvergenčních úvah. U Schmidta přečteny 433 a 441–443.

Na citované **442, §3** Schmidt výslovně konstruuje ortonormální
funkce postupným odečtením projekcí a dělením normou. Následuje důkaz
nenulovosti jmenovatelů při lineární nezávislosti a na 443 důkaz
ortogonality. Poznámka pod čarou na 442 přímo připisuje v zásadě
stejné vzorce Gramově práci v Crelle 94. Knuthova přesná lokalizace
i souvislost s ortogonalizací tedy souhlasí. Datum 18. října 1881
na konci Gramova rukopisu není rok vydání časopiseckého svazku.
Vlastní konečněrozměrný důkaz Hadamardovy nerovnosti byl dokončen
v subresultants.md; nevyžaduje teorii integrálních rovnic.

## 6. DeMillo–Lipton a Zippel, odpověď 16

Časopiseckou citaci DeMillo–Lipton, Information Processing Letters
7(4) (1978), 193–195, potvrzuje primární záznam vydavatele. Získán
rovněž veřejný předchozí technický report **GIT-ICS-77/07, květen
1977**, z archivu DTIC. Přečten titul, dokumentační list, abstrakt
a vlastní text. Report není vydáván za časopiseckou sazbu z roku 1978.
Indukce skutečně vybírá nenulový koeficient v poslední proměnné a
dává součinovou mez na podíl nenulových hodnot; jde o odpovídající
předchůdce Knuthovy odpovědi. Jeho následná hrubá asymptotická práce
s e^(-1) není součástí Knuthova důkazu a nebyla do něj přejata.

Zippelův původní článek z EUROSAM 1979, LNCS 72, 216–226, získán
z univerzitní sbírky SFU. Přečteny 216,221–222,226 (PDF 1,6,7,11).
Úvod skutečně popisuje použití náhodných specializací při řídkém
polynomiálním gcd. Věta 1 na 221 dává pro nenulový polynom v v
proměnných, s jednotlivými stupni nejvýše D, na mřížce o B>D
možnostech v každé souřadnici nejvýše B^v-(B-D)^v nul. Je uveden
i příklad dosahující meze. Pravděpodobnostní aplikace pokračuje na 222.
Matematické zobecnění na různé množiny a stupně v Knuthově úloze
má vlastní důkaz v subresultants.md, takže se zde neopíráme o
nepřečtené části Zippelova algoritmu nebo o jeho měření času.

## 7. Navazující matematický blok

Tvrzení na 674 o O(n log² n) aritmetických operacích pro resultanty
a Sturmovy posloupnosti bylo následně uzavřeno vlastním důkazem
v [fast-sturm.md](fast-sturm.md), včetně kompaktní reprezentace. Bibliografie Schwartz
1980 je doložena, ale skutečný úplný PDF článek se zatím nepodařilo
získat. Indexované odkazy Wisconsin a CiteSeer vracejí 404; ACM
403. Byl prověřen i správný starý identifikátor CiteSeer
10.1.1.391.1254. Nejde o důkaz chybnosti tvrzení.

Veřejný neautoritativní přepis naznačuje, že autor počítá posloupnost
vedoucích koeficientů a informace pro počet kořenů, nikoli explicitní
husté koeficientové seznamy všech zbytků. Je to navigační vodítko,
nikoli přečtený originál. Rozlišení reprezentací je nezbytné: běžná
posloupnost může mít kvadraticky mnoho koeficientových pozic. Samotný
argument velikostí explicitního výstupu proto ještě nevyvrací správně
formulovaný kompaktní algoritmus.

Všech šest vrstev errat bylo prohledáno podle stránek i témat;
konkrétní shody jsou v `sources/polynomial-history-errata.txt`.
Tento blok nevyžadoval nový numerický test a žádný úspěšný starší
výpočet se neopakoval. Tento historický blok původně ponechal rychlý
algoritmus otevřený; navazující matematický blok již sekci uzavřel. Fyzický nejnovější dotisk
není ověřen a žádné hlášení nebylo odesláno.
