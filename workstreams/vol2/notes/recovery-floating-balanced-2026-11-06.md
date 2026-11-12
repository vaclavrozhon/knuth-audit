# Obnova celé §4.2.1–7: vyvážená trojková aritmetika

7. listopadu 2026, X0202. Zadání 227/file239 a celá odpověď
612/file624 znovu porovnány s originálem. Tisk má **ostré** meze
1/6<|f|<1/2. Starší zápis s ≤ na levém konci je pro konečné
zlomky ekvivalentní, ale není doslovným přepisem. Každá věta
odpovědi má níže vlastní rozsah. C0082 zůstává interpretačním
kandidátem; celý matematický smysl „rounding“ není bez výhrady
uzavřen. Žádný archivní výpočet nebyl opakován.

## Model, obě meze a normalizace

Nechť p≥1, h=3^−p a cifry jsou −1,0,1. Zlomek
f=Σ(j=1…p) d_j 3^−j je celočíselný násobek h. Největší
absolutní hodnota je c=(1−h)/2, dosažená samými 1 nebo −1.
S první cifrou +1 je nejmenší hodnota
1/3−Σ(j=2…p)3^−j = a=(1+3h)/6; ostatní cifry jsou −1.
Pro první −1 platí zrcadlový výsledek. První nenulová cifra
proto přesně určuje znaménko.

Je-li první cifra 0, velikost je nejvýše
Σ(j=2…p)3^−j=(1−3h)/6<1/6. Je-li první cifra ±1,
a≤|f|≤c, tedy právě 1/6<|f|<1/2. To dokazuje ekvivalenci
normalizace a nenulové první cifry. Pro p=1 jsou a=c=1/3,
takže argument zahrnuje i nejkratší mantisu. Nula je výslovně
normální a pro uložení se jí vyhradí jediné nulové slovo.

Meze 1/6 a 1/2 nemají konečný trojkový rozvoj: jejich jmenovatel
obsahuje faktor 2. Každý nenulový konečný trojkový zlomek proto
lze jednoznačně posouvat do tohoto otevřeného intervalu; násobení
f číslem 3 při zmenšení e o1 a opačný posun zachovávají f3^e.
Intervaly se sousedními exponenty se setkávají jen v neuložitelných
hraničních bodech. U přesného podílu se hrana vyskytnout může;
to již patří do samostatné zaokrouhlovací výjimky níže. Konečný
rozsah exponentů se kontroluje až u výsledku.

## Konečné odříznutí a výjimka dělení

Konec konečného rozvoje za p-tou cifrou má velikost nejvýše
Σ(j=p+1…m)3^−j = (h/2)(1−3^(p−m)) < h/2.
Ponechaný prefix je násobkem h; každý jiný násobek je vzdálen
nejméně h. Prefix je tedy jediný nejbližší bod **pevné mřížky hℤ**.
Argument je symetrický pro záporné konce a nezávisí na tom,
zda cifry vznikly sčítáním, odčítáním nebo násobením. Tyto tři
operace nad konečnými trojkovými čísly mají konečný přesný rozvoj.
Po případné přesné normalizaci proto stačí odříznout cifry.

Dělení může mít nekonečný rozvoj. Jeho konec má jen neostrou
mez h/2; při samých 1 či −1 nastane přesná půlka a je třeba
stanovit volbu mezi dvěma stejně blízkými body pevné mřížky.
Například p=2, u=.1(−1)_3=2/9, v=.11_3=4/9 dávají u/v=1/2
s rozvojem .111…_3. Tento podíl také leží přesně na otevřené
normalizační hraně; nejprve normalizovat přesný podíl do ostrého
intervalu nelze. To nevyvrací definici uložených konečných čísel,
ale vyžaduje společně určit zaokrouhlení a výsledný exponent.
Odpověď dělení z prostého odříznutí výslovně vyjímá; plný
jednoznačný algoritmus pro všechny takové půlky nepředepisuje.

## Proč stačí p+1 cifer akumulátoru

Následující konstrukce dokazuje přesný výstup postupu „normalizuj
přesný součet a zaokrouhli v jeho exponentovém pásmu“. Neprohlašuje
jej za globálně nejbližší plovoucí číslo. Akumulátor má p+1
vyvážených tritů; poloha čárky je podle větve známá. Exponent a
řízení se jako obvykle nepočítají do cifer významové části.
Odčítání se převede na sčítání negací všech cifer druhého vstupu.
Nulový operand se vrátí přímo. Dále e_u≥e_v, d=e_u−e_v≥0.

**Stejná znaménka.** Znaménkovou symetrií stačí kladné vstupy.
Nechť g=f_v3^−d a G je jeho prefix na p místech. Pak
|g−G|<h/2. Počítej přesně z=f_u+G v akumulátoru s pozicemi
0,−1,…,−p. Jeho celočíselný koeficient má velikost nejvýše
3^p−1, což se do p+1 vyvážených tritů vejde. Tím je zahrnut
přenos před řádovou čárkou, který starý stručný argument opomíjel.
G≥0 a z≥f_u>1/6, takže normalizace vlevo není nutná.

Protože z∈hℤ a 1/(2h)=3^p/2 je půlcelé číslo, vzdálenost z
od 1/2 je nejméně h/2. Chyba |(f_u+g)−z|<h/2 nemůže změnit
rozhodnutí o pravém posunu. Bez něj je nejbližším bodem hℤ
právě z. Při posunu vpravo je z/3∈(h/3)ℤ a chyba menší než
h/6. Každý bod této mřížky je od nejbližší půlky mezi body hℤ
vzdálen nejméně h/6: násobky 1/3 se od půlcelých čísel liší
nejméně o1/6. Zaokrouhlovací rozhodnutí se tedy nezmění ani zde.
Přesný součet je menší než1; jediný pravý posun již stačí.

**Opačná znaménka, d=0.** Rozdíl je přesný na p místech a má
velikost menší než1/2. P+1 tritů jej bezpečně uloží. Případná
normalizace vlevo pracuje s přesnou hodnotou; nulový rozdíl
je samostatný nulový výsledek. V nejmenším nenulovém případě
je velikost alespoň h, takže stačí nejvýše p−1 levých posunů.

**Opačná znaménka, d=1.** Součet je přesný na p+1 zlomkových
místech a nemá přenos před čárku: |f_u−|f_v|/3|<1/2.
Navíc a−c/3=2h/3>0, takže znaménko je znaménkem většího
exponentu a není to nula. Akumulátor s pozicemi −1,…,−p−1
uloží celý přesný součet. I nejmenší možná velikost 2h/3 po
nejvýše p−1 levých posunech dosáhne 2/9>1/6.

**Opačná znaménka, d≥2.** Přesná velikost w splňuje
w≥a−c/9=1/9+5h/9>1/9 a w<c<1/2. Znamená to nejvýše
jeden levý posun a žádný pravý. Menší operand odřízni na p+1
zlomkových místech. Jeho chyba má velikost <h/6; přesný součet
s prefixem z je násobkem h/3, rovněž bez celočíselného přenosu.
Znaménko se nemůže změnit (již w>1/9 a chyba<h/6≤1/18).

Číslo 1/6 je v jednotkách h/3 půlcelé, takže |z−1/6|≥h/6;
rozhodnutí o levém posunu se nezmění. Bez posunu jsou násobky
h/3 od půlek mřížky hℤ vzdáleny ≥h/6, což je více než chyba.
Po jediném levém posunu je 3z∈hℤ a chyba <h/2; zaokrouhlí se
právě na3z. To uzavírá všechny exponentové rozdíly i znaménka.

Argument nevyžaduje sticky bit navíc, protože všechny konečné
vyvážené konce mají striktní půlkovou mez. Neznamená to,
že libovolné bezmyšlenkovité odříznutí před normalizací je bezpečné;
konkrétní rozdělení větví a mřížkové vzdálenosti jsou podstatné.

## C0082: co tento výsledek neříká

Původní přesný příklad je převzat bez běhu. Pro p=2,q=0:
u=(0,.1(−1)_3)=2/9, v=(−2,.(−1)(−1)_3)=−4/81.
Oba uložené zlomky mají velikost v(1/6,1/2). Součet
14/81=.1(−1)(−1)(−1)_3 je stále v tomto pásmu; normalizace
nemění exponent. Dvouciferné odříznutí vrací2/9 s chybou4/81.
Soused 4/27=(−1,.11_3) má chybu2/81, tedy je přísně lepší.

Kladné dvouciferné normální koeficienty jsou přesně2,3,4
v jednotkách1/9. Proto jsou4/27 (největší v dolním pásmu)
a2/9 (nejmenší v horním) bezprostřední sousedé; mezi nimi není
skrytá alternativa. Jejich půlící bod je5/27=15/81 a přesný
součet14/81 leží pod ním. Jde o skutečný rozpor s **globální**
interpretací nejbližšího plovoucího čísla. Pevnou mřížku při
předem určeném exponentu tento příklad nevyvrací.

Výraz „rounding“ v této stručné návrhové odpovědi neurčuje,
který význam je požadován. C0082 proto zůstává candidate;
celá úloha je partial právě v tomto rozsahu a ve specifikaci
půlek dělení, nikoli kvůli mezerám ve výše uzavřených důkazech.

## Pořadí navrženého kódu

Uložme exponent e bez excess v pevné šířce k vyvážených tritů,
ve zvoleném konečném rozsahu. Jeho kód vložme mezi první trit
d_1 a zbylých p−1 tritů f. Je-li f záporné, změníme znaménka
všech exponentových tritů (vyvážený doplněk); trity f zůstanou.
Nulu uložíme jako celé nulové slovo. Žádná odlišná nula není
v tomto návrhu potřebná.

U konečných vyvážených slov odpovídá pořadí čísel lexikografickému
pořadí −1<0<1. V nejvyšší odlišné pozici je rozdíl nejméně1;
maximální rozdíl všech nižších m tritů je
2Σ(j=0…m−1)3^j=3^m−1<3^m, takže jej nemůže převrátit.
První ±1 proto odděluje kladná, záporná a jediné nulové slovo.

Pro kladné hodnoty je celý exponentový pás e pod pásmem e+1,
protože 3a−c=2h>0. Různé exponenty se tudíž porovnají správně
již vloženým kódem e; při stejném e rozhodne zbytek mantisy
stejně jako hodnota f. U záporných hodnot větší exponent znamená
menší hodnotu, proto doplněk e→−e přesně obrací pořadí pásem.
Při stejném exponentu je mantisa již záporná a její původní
trity zachovávají správné pořadí. Pro p=1 není žádný zbytkový
mantisový trit a stejné argumenty zůstávají platné. Výsledek
proto lze porovnávat jako pevná vyvážená slova bez dekódování
plovoucí hodnoty. Rozsah exponentů musí být společný a šířka
pevná; tento důkaz netvrdí nic o proměnlivých délkách kódů.

## Evidence a další práce

Osobně znovu přečten originál612 včetně ostrých mezí. Všechny
čtyři vrstvy errat a aktuální TeX prohledány podle612 a slov
balanced/ternary/truncat; změna odpovědi7 nenalezena. Oprava
odpovědi12 z roku2006 se úlohy7 netýká. C0082 se nepotvrzuje
ani neduplikuje. Hodnocení „pleasant“ je autorský úsudek.

Dále celá13 a15–18, historie225–227; FCMP vazba a průměr19
zůstávají výslovně otevřené. Dopředný418 je stále držen.
