# §1.2.2: čísla, mocniny a elementární logaritmy

V1-X0030, kontrola 1. listopadu 2026. Zobrazeny původní s. 21–27
a odpovědi 469–471. První dotisk má cvičení 1–29, errata z 28. června
2003 přidávají úlohu 30. Algoritmy a jejich chyby se probírají v
`logarithm-algorithms.md`. Číslování rovnic níže je z prvního dotisku;
errata 2024 vkládají nové (5) a následující čísla zvyšují o jedna.

## 1. Desetinná reprezentace, kořeny a mocniny

Desetinný zápis je n+sum_(j>=1) d_j 10^(−j), kde n je celé číslo,
0<=d_j<=9 a cifry nekončí samými devítkami. Prefix délky k je dolní
mez; horní mez se liší o 10^(−k). Řada konverguje geometrickým odhadem
ocasu. Obráceně intervaly z (2) určují nejvýše jedno číslo, neboť
jejich délky jdou k nule. Každé reálné číslo lze takto zapisovat
postupným výběrem největší cifry, jejíž prefix je ještě nejvýše x.

Výběr zakazuje nekonečný koncový blok devítek: takový zápis se rovná
zápisu s přenosem jedničky a nulovým ocasem. První rozdílná cifra
určuje pořadí; pozdější cifry mohou její příspěvek nejvýše vyrovnat,
a rovnost by právě vyžadovala vyloučený ocas devítek. Pro záporná x
je n dolní celá část, například −0,2=−1+0,8; nejde o zápis znaménka
před kladnou absolutní hodnotou. Toto je podstatné pro úlohy 5–6.

Pro kladné celé m je zobrazení t->t^m na nezáporných reálných číslech
striktně rostoucí a spojité. První vlastnost plyne z rozkladu
v^m−u^m=(v−u)(v^(m−1)+...+u^(m−1)); spojitost z téhož vzorce
na omezeném intervalu. Úloha 8 vybírá největší n a pak cifry d_k tak,
aby m-tá mocnina dolního prefixu nepřekročila zadané u>0. Mocniny
obou krajů svírají u a jejich rozdíl jde k nule. Limita je tedy
kladný m-tý kořen, jednoznačný díky striktnímu růstu. Pokud by
kořenový zápis končil devítkami, následující větší prefix by už také
měl mocninu nejvýše u, což odporuje maximálnímu výběru cifry.
Doplněk odpovědi z roku 2013 výslovně obsahuje tento poslední argument.

Pro b>0 dávají definice celočíselných mocnin (4) grupové pravidlo
b^(x+y)=b^x b^y: pro nezáporné exponenty seskupíme konečné součiny,
pro záporné použijeme převrácenou hodnotu a zkrácení. Z něj indukcí
v exponentu y plyne (b^x)^y=b^(xy), včetně záporných y.
Pro r=p/q, q>0, je b^r kladný q-tý kořen b^p. Nezávislost na
zápisu zlomku i obě mocninná pravidla se ověří umocněním na společný
kladný jmenovatel a jednoznačností kladného kořene. To nepoužívá
pravidlo pro racionální exponenty před jeho důkazem; upřesnění
odpovědi 9 z roku 2021 je správné.

Pro b>1 mají intervaly v (7) délku nejvýše
b^(n+1)(b−1)10^(−k), která jde k nule. Použitá nerovnost z úlohy 13
je (1+t)^(1/m)−1<=t/m pro t>0,m>=1, s rovností pro m=1:
indukce dává (1+t/m)^m>=1+t. V (7) je m=10^k>1 a horní
prefix je menší než n+1, takže vytištěná ostrá mez je v pořádku.
Zákaz koncových devítek zaručuje, že limitní hodnota neleží na
vyloučeném pravém kraji žádného z intervalů. Klesání jejich délky
samo o sobě by tuto poslední skutečnost pro polootevřené intervaly
ještě nedokázalo.

Pro 0<b<1 se použije b^x=(1/b)^(−x); pro b=1 hodnota 1.
Spojitost tohoto rozšíření a hustota racionálních čísel přenesou
mocninná pravidla na reálné exponenty. Pro b>1 je funkce rostoucí,
má limity 0 a infinity na koncích reálné osy a nabývá všech kladných
hodnot; pro b<1 je klesající. Proto pro b>0,b!=1 existuje právě
jeden log_b y pro každé y>0. Logaritmická pravidla (11),(12),(14)
plynou aplikací této inverzní funkce na pravidla mocnin. Převod
základu (14) navíc vyžaduje c>0,c!=1; tyto obory se přebírají
z významu použitého logaritmu.

Komplexní číslo z=x+iy má conjugate(z)=x−iy a
z conjugate(z)=x^2+y^2=|z|^2 přímým roznásobením, neboť i^2=−1.
Definice intervalů na s. 21 jsou konzistentní včetně nekonečných
otevřených konců. Errata 2024 doplňují mocniny nuly a záporného
základu pro celočíselné exponenty: 0^0=1 jako zdejší konvence,
0^n=0 pro n>0 a (−b)^n=(−1)^n b^n. Nezavádějí záporné mocniny nuly.

## 2. Přirozený logaritmus, iracionalita a číselné hodnoty

Funkce L(x)=integral_1^x dt/t pro x>0 je spojitá, striktně rostoucí
a změna měřítka t=xu dává L(xy)=L(x)+L(y). Nabývá všech reálných
hodnot: L(2^n)=nL(2) pro libovolné celé n. Jediné číslo e s L(e)=1
proto určuje L(x)=log_e x. Obrázek 6 správně znázorňuje plochu pro
x>=1; pro x<1 se používá orientovaný integrál se zápornou hodnotou.
Změna měřítka je současně geometrickým důkazem úlohy 23 pro x,y>1;
rozdělení orientovaných intervalů dává obecný případ x,y>0.

Z t/(1+t)<=ln(1+t)<=t pro t>−1 plyne
N ln(1+r/N)->r pro každé pevné reálné r. Proto
(1+r/N)^N->e^r. To ověřuje výklad složeného úročení jako čistě
matematický příklad; r musí být roční sazba, jak upřesnila errata 2002.

Iracionalita phi plyne z iracionality sqrt(5): rovnost p^2=5q^2
pro nesoudělná p,q by vynutila dělitelnost obou pěti. Pro úplnost
lze ověřit i v textu převzatou iracionalitu pi následujícím
integrálním argumentem. Kdyby pi=a/b s kladnými celými a,b, zvolme
f(x)=b^n x^n(a−bx)^n/n!. Každá derivace f v 0 je celé číslo,
protože nenulové koeficienty mají stupně alespoň n; také derivace
v pi jsou celé díky f(pi−x)=f(x). Pro polynom
F=f−f''+f''''−... platí F+F''=f. Tedy
integral_0^pi f(x)sin(x) dx=F(pi)+F(0) je kladné celé číslo.
Současně je nejvýše pi·(a^2/4)^n/n!, což pro dost velké n leží
mezi 0 a 1. Spor dokazuje tvrzení. Argument používá obvyklé
vlastnosti sinu a integrálu, nikoli desetinný odhad pi.

`check_elementary_constants.py` certifikuje vytištěné prefixy pi,
phi a e racionálními intervaly, nikoli desetinným zaokrouhlováním.
Používá pi=16 atan(1/5)−4 atan(1/239), střídavou řadu pro atan,
řadu sum 1/k! pro e a celočíselnou druhou odmocninu pro sqrt(5).
Identita pro pi plyne ze vzorce pro tangens součtu: tangens
4 atan(1/5) je 120/119 a po odečtení atan(1/239) vyjde 1;
úhel leží v intervalu (0,pi/2). Ocas řady e za 100! je menší než
1/(100·100!), ostatní ocasy mají přímé geometrické či střídavé meze.
Ověřené intervaly jsou dost úzké pro 40 desetinných míst, ale příloha A
dosud nebyla s nimi porovnána. Výsledky: `results/elementary-constants.json`.

## 3. Jednotlivé úlohy 1–24

1. Nejmenší kladné racionální číslo neexistuje, protože r/2<r.
2. Zápis s nekonečným ocasem devítek není dovolený kanonický rozvoj;
   dané číslo má zápis 1,24 s nulovým ocasem.
3. (−3)^(−3)=−1/27. V prvním dotisku ještě definice neobsahovala
   záporný základ; odpověď na tuto mezeru výslovně upozorňuje.
   Doplněné definice z roku 2024 ji odstraňují.
4. (1/8)^(−2/3)=4, protože kladný třetí kořen 1/8 je 1/2.
5. Nahradíme 10 číslem 2, cifry jsou 0,1 a vyloučíme koncové samé
   jedničky. Interval po k cifrách má délku 2^(−k).
6. Porovnání celých částí a první odlišné cifry je dokázáno v oddílu 1.
   Nejde o slib konečného algoritmu rozhodujícího rovnost dvou
   libovolně zadaných nekonečných proudů cifer.
7.–9. Obecné důkazy mocnin a konstrukce kořene jsou v oddílu 1.
10. Kdyby log_10 2=p/q pro kladná celá p,q, pak 2^q=10^p.
    Pravá strana je dělitelná pěti, levá nikoli.
11. Žádný konečný prefix x souhlasící s log_10 2 neurčí první cifry
    10^x: díky iracionalitě leží log_10 2 uvnitř každého svého
    desetinného prefixového intervalu a jsou v něm čísla z obou stran.
    Jejich mocniny leží pod a nad 2. Nejde o odmítnutí možnosti
    vypočítat 10^x s malou absolutní chybou. Úpravy 2019 odstraňují
    záměnu konečného prefixu a nekonečného zápisu 1,999...=2.
12. Monotónnost mocniny a dvě hodnoty v (8) ohraničují log_10 2
    mezi 0,30102999 a 0,30103000. Uvedených osm cifer je správně.
13. Znaménko v originálu je <=, nikoli přísná nerovnost v Markdownu;
    obecný důkaz v oddílu 1 zahrnuje rovnost při n=1.
14.–16. Logaritmus mocniny, podílu a změna základu plynou z inverze
    exponenciály: log_b(c^y)=y log_b c,
    log_b(x/y)=log_b x−log_b y, log_10 x=ln x/ln 10.
17. Odpovědi 5,1,1,0 a nedefinováno souhlasí s reálnými logaritmy.
18. Tvrzení s koeficientem 1/2 je úmyslně chybné; správně
    log_8 x=(lg x)/3. Už x=8 dává 1 proti 3/2.
19. Každé čtrnácticiferné kladné n je menší než 10^14, což je
    menší než 2^47=140737488355328. Samostatný znaménkový bit
    tudíž neubírá z uvedených 47 bitů pro velikost.
20. Log_10 2 a log_2 10 jsou převrácené hodnoty pravidlem změny základu.
21. Na společném reálném oboru b>1,x>1 je odpověď
    (ln ln x−ln ln b)/ln b správná. Pro 0<b<1 a 0<x<1 je levá
    strana rovněž definována, ale uvedené samostatné ln ln x a
    ln ln b nejsou reálné. Univerzální podoba je
    (ln|ln x|−ln|ln b|)/ln b, pokud log_b x>0. Zadání samo
    požaduje vyjádření pomocí ln ln b, čímž lze obor b>1 chápat
    jako implicitní; tento bod nevedeme jako samostatný potvrzený nález.
22. Pro x>0,x!=1 je relativní chyba nezávislá na x a rovná
    |1−ln(2)(1+1/ln(10))|. Racionální intervaly v kontrolním
    programu ji ohraničují kolem 0,005822824, tedy 0,5823 % <1 %.
    Při x=1 jsou obě strany přesně 0. Vytištěných přibližně 0,582 %
    je správně; nejde o přesnou konstantu.
23. Důkaz změnou měřítka je v oddílu 2; zahrnuje orientované plochy.
24. Při náhradě každé 10 dvojkou se tentýž algoritmus normalizuje
    do [1,2) a počítá bity log_2 x; důkaz je v navazující poznámce.

## 4. Úlohy 29–30

Pro pevné x>1 minimalizace b log_b x znamená minimalizaci b/ln b.
Derivace má znaménko ln b−1, takže reálné minimum je v b=e.
Mezi celými b>=2 připadají v úvahu 2 a 3; platí 3/ln3<2/ln2,
neboť 3ln2<2ln3 je ekvivalentní 8<9. Odpověď je 3.

Pro (b+1)/ln b má derivace znaménko ln b−1−1/b; tento výraz
striktně roste a jeho nula leží mezi 3 a 4. Například řada pro ln3
dává ln3<10/9<4/3, zatímco ln4>4/3>5/4. Celé minimum tedy
leží v 3 nebo 4. Nerovnost 5/ln4<4/ln3 odpovídá 3^5<4^4,
tj. 243<256, takže odpověď je 4. Všechny tři výsledky na s. 471 souhlasí.

Doplněná úloha 30 má výraz (ln n)^(ln n/ln ln n). Pro n>1,n!=e
je jeho logaritmus ln n, takže výsledek je n. V n=e vzniká dělení
nulou v exponentu, nikoli definovaný výraz; dodatečná podmínka
n!=e je zveřejněna 22. července 2011. Tato doplněná úloha je
vedena mimo 29 cvičení prvního dotisku, aby nezmizela z inventáře.

## 5. Přesný neuzavřený rozsah

Historické atribuce Oresme, Wallis, Newton, Napier, Briggs a Feynman,
citované články o číslicových algoritmech a změna atribuce značky lg
na Ernesta Trucca (errata 2015) ještě potřebují zdrojovou kontrolu.
Opravy drobných definic, oborů a rovnic z let 1997–2024 byly porovnány
se všemi řadami errat. Pomocný Markdown má chybný ostrý znak v úloze
13 a vypouští člen n v exponentu jmenovatele (19); originál je správný.
