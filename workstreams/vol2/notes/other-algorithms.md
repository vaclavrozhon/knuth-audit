# §3.2.2: algoritmy A, M, B a první důkazy o periodách

Kontrola 1. listopadu 2026. Uzavřeny implementace A/M/B, konkrétní
příklad (13) a úlohy 1–7, 13–16, 24, 25 a 27. Navazující tabulka primitivních
polynomů, obecné zvedání period a zbytek sekce jsou nyní uzavřeny
v dalších poznámkách; soupis viz [dokončení textu](other-methods-context.md).
Nález v poznámce k úloze 15 je [C0007](C0007-shuffle-gap-period.md);
přidanou úlohu 38 řeší [C0008](C0008-universal-max-digits.md).

Používáme `mod m` pro nezáporný zbytek, `floor` pro celou část a
periodu pro nejmenší kladnou eventualní periodu. Eventualní znamená,
že opakování může začít až po konečném úvodním úseku. Lcm je nejmenší
společný násobek, gcd největší společný dělitel.

## A a dávková varianta (úloha 25)

[Str. 28](../images/vol2-p028.png) předepisuje
X_n=X_(n-24)+X_(n-55) modulo 2^e. Tabulka Y[1..55] začíná hodnotami
X_54,...,X_0; j=24,k=55 proto ukazují na X_31,X_0. Oba ukazatele
klesají v cyklu délky 55, jejich rozdíl modulo 55 zůstává 31.
Nemohou být oba nulové; invariant A1 i větvení A2 jsou správné.
Upozornění na poslední fakt již přidalo erratum z 4. 10. 2007.
MIX uloží nízké bity součtu; přetečení se zde smí ignorovat, protože
požadujeme právě redukci modulo velikost slova.

[Odpověď 25, str. 556](../images/vol2-p556.png) provede k=55,...,32
jako `Y[k]+=Y[k-31]`, potom k=31,...,1 jako `Y[k]+=Y[k+24]`.
Druhá část správně čte již aktualizovaná data. Čtení Y[55],...,Y[1]
pak dává stejné výstupy jako 55 jednotlivých vyvolání A.

Časování MIX: A stojí 10 jednotek plus dva resety za 55 kroků.
Volání JMP, STJ a návrat JMP přidají 4, celkem 14+2/55.
U dávkové varianty stojí vnější DEC/J6Z/LDA 4 na výstup, tělo dávky
55*8+6; celkem 12+6/55. Oba vytištěné časy souhlasí.

Program porovnal přímou rekurenci, model devíti instrukcí a dávkové
průchody na 348 počátečních vektorech pro šest šířek slova: všech
55 jednotkových vektorů, nuly, maxima a pevně seedované vektory.
Celkem 191 400 jednotlivých výstupů. Obecný invariant je důkaz;
testy navíc hlídají indexy a přenosy.

## M, B a úlohy 3–5

M ([str. 33](../images/vol2-p033.png)) má první k hodnot X v tabulce,
další X zapisuje na pozici `floor(kY/m)` a vrací její původní obsah.
B ([str. 34](../images/vol2-p034.png)) používá místo druhého vstupu
předchozí výstup Y; na začátku je Y=(k+1). hodnota vstupu.

Přesná simulace potvrdila tabulky i všechny číslice odpovědi 3
na [str. 551](../images/vol2-p551.png) a [552](../images/vol2-p552.png):

- M: úvod `0 4 5 6 2 0 3`, potom cyklus `2 7 4 1 6 3 0 5` délky 8.
  Je to aritmetická posloupnost s přírůstkem 5 modulo 8, tedy potence 1.
- B: 46 výstupů před periodou délky 40. Celý uložený stav má úvod
  délky 47, protože obsahuje i minulý výstup. Kniha správně udává
  periodu pozorovatelného výstupu, nikoli tohoto rozšířeného stavu.

Program (14) je správný s k rovným velikosti bajtu a m velikosti slova;
druhou podmínku doplňuje erratum 18. 6. 2024. Nejvyšší bajt Y je pak
`floor(kY/m)`. Výpočet `a(X+1)` modulo velikost slova je správný i při
přetečení INCA. LDA V,j; STA Y; STX V,j vrátí starý prvek a vloží nový.
Jsou to čtyři instrukce navíc vůči samotnému LCG; slovo „additional“
je v erratu 16. 9. 2014. Model ověřen v 8 000 krocích.

Úloha 4: spodní bajt LCG modulo velikost slova má krátkou vlastní
periodu; vyšší bajt proto obvykle dává vhodnější index. Nejde o obecnou
větu pro každý myslitelný generátor.

Úloha 5: při sdílení **téže aktuální hodnoty X a Y v M1** každý přepis
V[j] vloží prvek do intervalu j/k<=V[j]/m<(j+1)/k. Po prvním přepisu
buňky se tedy její vyšší cifry nemíchají. Odpověď používá právě tuto
implementační interpretaci úspory generátoru. Doslovné zarovnání dvou
abstraktních posloupností X_n=Y_n před inicializací by ještě vyžadovalo
ošetřit posun k hodnot spotřebovaných při naplnění tabulky. Obě indexové
konvence zde nezaměňujeme. Pevné posuny či vybírání jiných cifer zůstávají
deterministickým filtrem jedné periodické posloupnosti; po prohřátí
tabulky neprodlouží její periodu.

## Velký příklad (13): důkaz periody výstupu M

Položme m=2^35, k=64. Oba generátory mají násobitel 1 modulo 4 a lichý
přírůstek, tedy periodu m a různé prvky periody. Z Y se vynechá jediná
nula, nová perioda je L=m-1. Zbývají dvě podmínky úlohy 15.

První: návratové mezery q_n ke stejné buňce jsou menší než m/2.
Úplný [soupis C++](../census_shuffle_y.cpp) prošel 34 359 738 368 stavů,
zkontroloval frekvence 64 buněk i uzavření cyklu: 201,49 s, exit 0.
Největší zaznamenaná mezera je 1 616.
[Výsledek](../results/shuffle-y-census.json).

**Nezávislý důkaz dostatečné meze:** rozdělíme čas na 4 096 bloků délky
2^23. [Python](../verify_shuffle_y.py) vypočte začátek každého bloku
samostatně mocněním afinní transformace s přesnými celými čísly.
V prvních nejvýše 758 krocích každého bloku najde všechny buňky.
Každá mezera v celé cyklické posloupnosti má proto délku nejvýše
2^23+758=8 389 366 < m/2. Vynechání nuly mezery nezvětší.
Tento argument nepoužívá správnost úplného soupisu ani jeho maximum.
Validátor ověřil i všech 64 svědků zaznamenaných maximálních mezer;
jejich přesné globální horní meze pocházejí ze soupisu, nezávislá
globální mez je výše uvedená slabší. [Validace](../results/shuffle-y-validation.json).

Druhá: nejmenší perioda q je L. Buňka 0 se v periodě L vyskytne
2^29-1 krát, každá jiná 2^29 krát. Je-li p perioda q, pak p dělí L.
Vazby n na n-q_n spojují právě všechny výskyty téže buňky. Posun o p
zachovává tyto vazby, a tedy permutuje buňky při zachování frekvencí.
Musí fixovat jedinou méně častou buňku 0. Indikátor jejích návštěv je
p-periodický, a L/p dělí 2^29-1. Ale
gcd(2^35-1,2^29-1)=2^gcd(35,29)-1=1, tedy p=L.

Věta z úlohy 15 dává přesně lcm(m,L)=2^70-2^35,
tj. 1 180 591 620 683 051 565 056. Známá errata opravují odkaz (12)
na (13), 29. 12. 1997, a stránky Greenwoodova článku na 222–227,
8. 12. 2009. Důkaz je vlastní; celý Greenwoodův článek znovu neověřen.

## Binární zpětná vazba, úlohy 6, 7 a 16

Součet bitů modulo 2 je XOR. Slovo délky k představuje polynom stupně
menšího než k podle svých bitů; posun vlevo je násobení x.
Maska A=(a_1...a_k)_2 určuje f(x)=x^k+a_1 x^(k-1)+...+a_k.
Program (10) násobí slovo x a případný nejvyšší bit odstraní přičtením f:
je to násobení x modulo f. Je-li f **primitivní**, všechny nenulové
zbytky tvoří jeden cyklus délky 2^k-1. Obecné kritérium a velké konkrétní
masky budou ověřeny zvlášť; zde je tvrzení podmíněné primitivitou.

Úloha 16 plyne z f(T)=0 pro lineární přechod T, tedy
T^k=a_1 T^(k-1)+...+a_k I, kde I je identita. Aplikace na libovolný
počáteční stav a odečtení libovolného bitu dává požadovanou rekurenci,
také pro nejvyšší bit. V elementárním důkazu oprava 1. 6. 2001 mění
druhý člen rozvoje na a_2 X_((n-2),1), poslední X_((n-2),3) zůstává.
Viz [str. 555](../images/vol2-p555.png) a
[původní errata](../images/all2-prepre-p31-direct.png).

Úloha 6: při X<2^(k-1) je další celé slovo přesně 2X; uniformní
zastoupení jednotlivých slov neznamená nezávislost sousedních slov.

Úloha 7: upravený program mění právě dva přechody: 100...0 jde do 0
a 0 do A. Vloží jeden nulový bit do jediného běhu k-1 nul.
Nenulová okna k sousedních bitů zůstanou právě jednou a přibude jediné
nulové okno, celkem 2^k. Mantelův rok 1897 je již opraven na 1895
v erratech z 23. 12. 2024.

Ověřeno 757 304 bitových rekurencí pro všechny liché masky a počáteční
stavy k<=8, 43 690 stavů upraveného programu a 104 úplných cyklů obou
variant pro masky s maximální periodou. Všech 16 řádků obrázku 1
na str. 31 souhlasí.

## Další elementární úlohy

**1, zlomky.** Normalizace U_n=X_n/m dává přesně
U_(n+1)=(aU_n+c/m) mod 1. Plovoucí součin však může zničit nízké cifry:
při 53bitové mantise, m=2^53, a=2^52+1, c=1 a U_0=1/2 se k přesnému
produktu 2^51+1/2 nepřičte representovatelně 2^-53. Výsledkem je 1/2
místo 1/2+2^-53. Varování odpovědi je věcné; nevylučuje speciální
přesně proveditelné varianty.

**2, Fibonacci.** Pro u,v v [0,m) je (u+v) mod m buď alespoň obě
hodnoty bez přetečení, nebo nejvýše obě s přetečením. Nikdy neleží
přísně mezi nimi. To dokazuje i obdobné tvrzení o lagu (24,55).

**13–14, součet.** Jsou-li periody X,Y rovny l_1,l_2 a Z=X+Y modulo m
má periodu L, pak L dělí lcm(l_1,l_2). Zároveň l_2 dělí lcm(L,l_1),
protože při tomto posunu se nemění Z ani X, a symetricky l_1 dělí
lcm(L,l_2). Má-li prvočíslo p v l_1 a l_2 různé exponenty, musí L
obsahovat větší z nich. Při stejných exponentech může nastat vyrušení.
To jsou meze úlohy 14; nesoudělné periody dávají jejich součin.
Ověřeno 111 365 dvojic malých periodických slov modulo 2,3,4.

**24, reciproké lagy.** Pro Z_n=Y_(-n) vyřešíme původní rekurenci
pro poslední člen: Z_n=Z_(n-k+l)+Z_(n-k) modulo 2. Zpětný běh zachovává
periodu, protože poslední koeficient je 1 a přechod je vratný.

## Úloha 27: synchronizace B

J_n=floor(kX_n/m) je číslo intervalu vstupní hodnoty. Slovo odpovědi
na [str. 557](../images/vol2-p557.png) je

```
0^(k+2) 1 0^(k+1) 2 0^k ... (k-1) 0^3.
```

Má délku l=(k^2+7k-2)/2 a převede intervaly všech buněk i Y na nulu.
Nulový vstup změní navštívenou buňku na nulovou. Nejvýše po k nových
buňkách se cesta vrátí do již nulové a zamíří do buňky 0; dva kroky
navíc vynutí nulový obsah i ukazatel 0. Je-li toto hotovo pro buňky
0,...,i-1, vložení i do buňky 0 a dalších k+2-i nul vynutí také buňku i.
To dokazuje indukci knihy. Záměna i/j je již opravena 25. 1. 2003.

Po tomto slově se intervalová trajektorie vždy synchronizuje. Každá
později používaná buňka se posléze přepíše; skutečný výstup pak má
periodu dělící vstupní periodu lambda. Nemůže být kratší: má-li výstup
periodu p, mají ji i vybrané indexy; doba do příští návštěvy téhož
indexu je pak p-periodická. Vstup v čase n je výstup při této příští
návštěvě, takže i vstup má periodu p. Nejmenší perioda je tedy lambda.

Dovětek „unless ... isn't very random“ není univerzální věta.
Přesný výklad: v nezávislých rovnoměrných indexech je pravděpodobnost
absence daného slova v r disjunktních oknech (1-k^-l)^r. Při
lambda>=l*k^l lze vzít aspoň k^l oken, takže absence má pravděpodobnost
menší než exp(-1). Tato argumentace nenahrazuje záruku pro konkrétní
generátor. Vyčerpávající kontrola lemmatu: 16 739 intervalových stavů
k<=5 a 1 364 stavů s více skutečnými hodnotami v každém intervalu.

## Reprodukce

[verify_other_algorithms.py](../verify_other_algorithms.py) a
[výsledek](../results/other-algorithms.json) obsahují konečné kontroly.
Nejprve validátor chybně požadoval shodu délky úvodu celého stavu a
výstupu B; po rozlišení obou veličin všechny testy prošly.
Velký příklad má vlastní soupis a nezávislou validaci odkazované výše.

Vrstvy all2-prepre, all2-pre, all2, err2 a err2.textxt porovnány pro
všechny uvedené stránky a úlohy. Původní sazba str. 27–31,33–34,
36–40,551–552,554–557 byla vizuálně přečtena.
