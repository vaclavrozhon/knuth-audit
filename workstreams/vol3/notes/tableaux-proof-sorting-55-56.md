# Algorithm S, jeho cena a základ duality:55–56, úlohy10–12

Sazba: tableaux-file-066.png,067.png,619.png. Pět vrstev errat se
přebírá ze sources/tableaux-errata-review.json. C0005 má již hotový
důkaz špatné výstupní souřadnice; neopakuji jeho test ani rešerši.
V níže uvedených konstrukcích se používá skutečně uvolněná buňka,
nikoli chybný P_rs. Obecné věty C,D a involutivita celé dualizace
zatím čekají na vlastní argument; jejich uvedení není jejich důkaz.

## P0407–409: invariant, každá větev a konec S; úloha10

Aktuální(r,s) chápejme jako díru; hodnota, která je v ní fyzicky
uložena, se při zachování uspořádání ignoruje. Všude mimo tuto díru
platí původní sousední nerovnosti. Další invariant při S3 je: oba
prvky nad dírou a vlevo od ní jsou menší než oba kandidáti pod dírou
a vpravo od ní. Tím je přesně rozvinutá stručná odpověď10.

Na počátku jsou horní/levý soused0 a kandidáti jsou kladní nebo∞.
Vybere-li se pravý kandidát v, z testu plyne v<dolní kandidát. Po
jeho přesunu do díry jsou tedy zachovány všechny čtyři sousední
nerovnosti kolem vyplněné buňky. Novou dírou je původní místo v.
Jeho levý soused je nyní v; horní soused je<v podle původního
sloupcového pořadí. Oba noví kandidáti vpravo/dole jsou>v podle
původních nerovností mimo starou díru. Nový invariant je tak doložen
pro obě levé/horní a obě pravé/dolní hodnoty. Pro dolního kandidáta
je argument přesně transponovaný: nový horní soused je v, levý je<v
a oba další kandidáti jsou>v. Kromě díry žádná duplicita nepřetrvá.

Podstatné je číst v S3 zvláštní relaci z(6), nikoli prosté ostré<
z OCR. Při dvou∞ se vybere S5. S4 proto vždy přenáší konečný prvek:
pravé∞ by nemohlo být menší než dolní kandidát, a to ani při rovnosti
obou∞. Návrat S4 přímo do S3 bez testu S2 je tedy správný.

Dokud se posouvá konečný prvek, je nová díra uvnitř původního tvaru
a r+s se zvětší o1. V konečném tvaru nakonec musí mít díra oba
kandidáty∞, tedy být vnějším rohem. S5 ji zaplní∞, zvýší r a S2
skončí. Tvar ztratil jediný roh, ostatní prvky se jen posunuly podél
jednoduché monotónní cesty; z množiny zmizelo právě původní P11.
Je-li prázdný už vstup, S2 skončí hned bez změny. Singleton má jednu
S3 a zůstane prázdný. Koncové proměnné jsou o jeden řádek pod rohem,
jak již dokládá C0005; vlastní S pracuje správně.

Pro skutečný odstraněný roh(i,j) proběhne i+j−2 konečných posunů
a jedna závěrečná S3 s∞. Přesný počet S3 je tedy i+j−1. Při přímém
přístupu je čas Θ(i+j), pracovní paměť O(1) slov; nepočítá se tím
jiný model reprezentace či bitová cena klíče.

## P0410: řazení a srovnávací stromová mez

P0406 dokládá, že P11 je vždy minimum. Před každým S je lze přečíst;
P0407–409 zachovají tableau s ostatními klíči. Indukce tudíž vydá
všechny klíče vzestupně. Předchozí opakování I tableau správně vytvoří
podle P0388–390; pro případ duplicit se nejprve použije již doložené
rozlišení(K_j,j), jelikož zdejší algoritmy předpokládají různé prvky.

Textová zmínka o O(n log n) pomocí stromu má přímý obecný svědek:
úplný binární heap s rodičem≤potomci. Nový prvek se umístí na další
list a opakovaně vymění s větším rodičem; jediná možná porucha jde
nahoru, nejvýše po výšce floor(lg n). Při odebrání minima se poslední
list dá do kořene a vyměňuje s menším dítětem, dokud není menší než
obě; jediná porucha jde dolů. Kořen je minimum po každé opravě,
výška je O(log n), takže n vložení a n odebrání stojí O(n log n).
Toto ověřuje uvedené existenční srovnání, nikoli ještě nějaký pozdější
konkrétní MIX program.

## P0411: úloha11 — co je potřeba pro obrácení jednoho S

Pouhé konečné P a(r,s) neurčují ztracenou hodnotu: dva různé singletony
končí stejným prázdným P a(r,s)=(2,1). Je-li minimum a známo, vložíme
díru do skutečného uvolněného rohu(r−1,s) a postupujeme zpět. Do díry
přesunujeme většího z horního/levého souseda; při chybějícím sousedu
jej nahradí0. V(1,1) se nakonec zapíše a.

Proč je vybrán právě předchozí krok původní cesty? Při posunu dopředu
dolů byla původní hodnota v nové díry přesunuta do buňky nad ní.
Levý soused nové díry byl<v podle řádkové nerovnosti. Při reverzi je
tedy v větší z obou předchůdců. Při posunu doprava je analogicky
horní soused<v a v stojí vlevo. Zpětná indukce po cestě, jejíž již
zpracovaný konec byl obnoven, proto vrátí každou hodnotu na původní
místo. Tím je doložena jedinečnost i konkrétní konstrukce, nejen
nutnost znát ztracený klíč.

## P0412–413: úloha12, přesný součet a jeho minimum

Opakované S odstraní každou původní buňku právě jednou jako roh.
Počet S3 závisí jen na tvaru λ=(n_1,…,n_m), nikoli na vyplnění:

    C(λ)=Σ_(i=1)^m Σ_(j=1)^n_i (i+j−1)
        =Σ_i binom(n_i+i,2)−Σ_i binom(i,2)
        =Σ_i binom(n_i+i,2)−binom(m+1,3).

Druhý tvar dostaneme součtem aritmetické řady v řádku a poslední
rovnost teleskopováním Pascalovy identity. Je to přesně odpověď12.
Prázdný tvar dává0; singleton1, v souladu s algoritmem.

V celé kladné mřížce je přesně k buněk ceny i+j−1=k. Nejméně možné
C pro n buněk proto získáme výběrem n nejnižších cen. Tento výběr
lze uskutečnit Youngovým tvarem: všechny diagonály do ceny t jsou
plné a libovolných r buněk další diagonály lze přidat, protože všichni
jejich leví/horní předchůdci již leží v plné části. Pro
n=t(t+1)/2+r, 0≤r<t+1, je tedy přesné minimum

    C_min= t(t+1)(2t+1)/6 +(t+1)r
          =sqrt(8/9) n^(3/2)+O(n).

Tím je dokázán celý vytištěný posloupnostní i asymptotický závěr.
Takový tvar má výšku i šířku O(sqrt(n)). Theorem A zaručuje vstupní
permutaci pro kterékoli jeho vyplnění; všechny prefixové tvary jsou
jeho podmnožiny. Proto i všechna vstupní I dohromady stojí O(n^(3/2)).
Samotné následné S vždy stojí Ω(n^(3/2)), takže minimální čas celého
popsaného třídění je skutečně Θ(n^(3/2)), nejen dolní mez fáze S.

## P0414: průměr a „téměř všechna“ v dodatku odpovědi12

Dokládám dva obvyklé významy průměru, aby se nezaměnila rozdělení
rovnoměrné mezi tableaux a rovnoměrné mezi vstupními permutacemi.
V obou případech platí C(λ)≤n(w+h−1), kde w,h jsou šířka a výška.

Pro rovnoměrnou permutaci je w délka nejdelší rostoucí podposloupnosti
podle již dokázaného invariantu P0403. Pro pevnou množinu k pozic je
jejich relativní pořadí rovnoměrné, takže s pravděpodobností1/k! jsou
vzestupné. Sjednocovací odhad dává

    Pr(w≥k) ≤ binom(n,k)/k! ≤ n^k/(k!)² ≤ (e²n/k²)^k.

Poslední nerovnost plyne z ln(k!)≥∫_1^k ln x dx≥k ln k−k.
Pro k≥2e sqrt(n) je horní odhad≤4^(−k); sečtení ocasů dává E w=O(sqrt(n)).
Theorem A a transpozice obou tableaux zajišťují stejnou distribuci
w,h: transpozice je bijekce všech stejných párů dané velikosti.
Tedy E h=E w a E C=O(n^(3/2)). Deterministické minimum dává opačnou mez.
S exponenciálně malou výjimkou mají zároveň w,h≤ceil(2e sqrt(n)).

Pro rovnoměrné tableau označme jejich počet t_n. Corollary B a
rozdělení involucí podle pevnosti prvku n dávají t_0=t_1=1 a
t_n=t_(n−1)+(n−1)t_(n−2). Pro R_n=t_n/t_(n−1) indukcí platí
sqrt(n)≤R_n≤sqrt(n)+1: je-li x=sqrt(n−1), rekurence spolu s předchozí
mezí dává

    1+x²/(x+1) = x+1/(x+1) ≥ sqrt(x²+1),
    R_n ≤ 1+x ≤ 1+sqrt(n).

První nerovnost se po umocnění redukuje na x²/(x+1)²≥0; základ n=1
platí. Tableaux s první řádkou délky l je nejvýše binom(n,l)t_(n−l):
vyber její množinu hodnot, jejíž pořadí je vynuceno, a libovolně vyplň
dolní tableau. Některá taková spojení nesplňují sloupce, což pouze
zvyšuje horní odhad. Proto

    Pr(w=l) ≤ binom(n,l)t_(n−l)/t_n
            ≤ sqrt(n(n−1)…(n−l+1))/l! ≤ n^(l/2)/l!.

Pro l≥2e sqrt(n) je to≤2^(−l); opět E w=O(sqrt(n)), transpozicí
E h=E w a E C=Θ(n^(3/2)), s exponenciálně malým ocasem za uvedenou
šířkou/výškou. Nevyvozuji přesnou limitní konstantu průměru ani tím
neuzavírám jiné, ostřejší tvrzení úlohy29.

## P0415–417: příklady56, tvar duality a transpozice

Pro tableau(25) je každý konečný posun a skutečný koncový roh tento:

| Smazaný klíč | Přesunuté klíče v pořadí cesty | Uvolněná buňka |
|---|---|---|
|1|2,4,9,12|(4,2)|
|2|3,5,7,11,15|(1,6)|
|3|4,6,8,13|(3,3)|
|4|5,7,11,14|(2,4)|
|5|6,8,12|(3,2)|
|6|7,11,13|(2,3)|
|7|8,9,10,16|(5,1)|
|8|9,10,16|(4,1)|
|9|10,12|(2,2)|
|10|11,13,14,15|(1,5)|
|11|12,16|(3,1)|
|12|13,14,15|(1,4)|
|13|14,15|(1,3)|
|14|15|(1,2)|
|15|16|(2,1)|
|16|žádný|(1,1)|

První a třetí stav souhlasí s oběma mezilehlými obrázky. Zápis
smazaných klíčů do posledního sloupce tabulky dává přesně(26):
(16,14,13,12,10,2)/(15,9,6,4)/(11,5,3)/(8,1)/(7).
Jde o ruční cestový doklad, nikoli opakovanou enumeraci.

Obecně se tak zaplní každá původní buňka právě jednou. Buňka vlevo
nebo nahoře nemůže být odstraněna před svým pravým/dolním sousedem,
neboť odstraňujeme rohy. Dostane tedy pozdější, větší smazaný klíč.
Celý záznam E(P), označený v knize P^S, je proto duální tableau
stejného tvaru. Prázdný případ se mapuje na prázdný.

Operace odstranění i celý E komutují s transpozicí tvaru: při dvou
konečných kandidátech jsou různé, takže volba menšího je symetrická
mezi řádkem a sloupcem. Při dvou∞ je skutečný odstraňovaný roh také
transponovaný; asymetrická poslední změna proměnné r nemění zbylé
tableau. Tedy d(P^T)=d(P)^T a E(P^T)=E(P)^T v opravené konvenci
skutečného rohu. Tím se nepřebírá chybná výstupní souřadnice C0005.

Dva zobrazené kroky obráceného pořadí na(26) se rovněž ověří přímo:
odstranění16 přesouvá15,11,8,7 do rohu(5,1); odstranění15 pak
přesouvá14,13,12,10,2 do rohu(1,6). Aktivní část je přesně dolní
obrázek na56. Tvrzení, že opakování až do konce obecně obnoví P,
z těchto dvou kroků neplyne a zůstává zvlášť P0420 partial do důkazu.

## Přesné zbývající závislosti — P0418–420

Theorem C na55 a úloha13 vyžadují důkaz, že odstranění minima ze
vstupního slova odpovídá d(P). Odpověď608 používá v druhém případu
reverzní vložení z úlohy5, která zase odkazuje na úplnou invarianci
a kanonickou reprezentaci v úloze4. Tyto obecné argumenty zatím
nejsou zapsané. Kandidát C0007 je jen lokální přetížení P^S versus d(P);
platnost věty z něj nelze ani potvrdit, ani vyvrátit.

Theorem D na57 používá C a úlohu5. Jeho kroky a z nich odvozená
involutivita E proto zatím zůstávají partial. Přítomnost správného
známého tvrzení nebo stručné odpovědi není jeho individuální audit.
Následující blok doplní právě úlohy4–5 a navazující C/D; hook formula
se nebude považovat za prověřenou jen z dřívějšího rychlého čtení.
