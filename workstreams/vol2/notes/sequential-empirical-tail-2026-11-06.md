# Souvislá revize konce §3.3.2 — 6. listopadu 2026

Původní sazba 73–75, 79–80 a 570–572 znovu vizuálně porovnána
s důkazy, čtyřmi programy a dokončenými výsledky. Na 571 byl navíc
vykreslen větší originál, aby byly čitelné všechny exponenty.
Výsledky rozsáhlých starých experimentů nebyly znovu počítány.
Otisky a rozsah přijetí jsou v `results/sequential-empirical-tail-review.json`.

## Podposloupnosti a historické odstavce

Při cyklu délky N má výběr každého q-tého stavu periodu
N/gcd(N,q). Pro afinní generátor je nový krok
a^q X+c(1+a+…+a^(q−1)) modulo M; nevyžaduje dělení a−1.
Pro plnou binární periodu a kroky q<16 má největší společný
dělitel krok 8; pro desítkovou krok 10. Identita
v_2(a^q−1)=v_2(a−1)+v_2(q), a≡1 mod4, vysvětluje pokles
potence. Předchozí obecné důkazy v `multiplier-periods.md`
a `potency.md` se tímto použitím neopakují výčtem.

Praktická zkušenost s kvalitou podposloupností není univerzální
zárukou jejich náhodnosti. Stejně tak nulová korelace v odstavci K
není obecnou charakterizací nezávislosti; výpočet korelace a jeho
přesné meze byly vypořádány v předchozím bloku. Strana 73 je nyní
celá zkontrolovaná v tomto rozsahu.

Pro pořadové testy stačí i jiné spojité rozdělení než rovnoměrné,
pokud jsou pozorování nezávislá a stejně rozdělená. Každá permutace
pořadí má pravděpodobnost 1/n!. Samotná absence shod bez tohoto
předpokladu nestačí; text na 74 čteme v kontextu nulové hypotézy.
Kendallova historická kalibrace překrývajících se párů je skutečně
problematická: pro deset symbolů dává vlastní kovarianční důkaz
limitu chi²_81+2 chi²_9, nikoli obyčejné chi²_90.

Přijaty dřívější přesně vymezené zdrojové kontroly v
`empirical-history.md`, nikoli znovu tvrzeno přečtení všech článků.
Nově byly vizuálně přečteny oba relevantní obsahy původního svazku
Proceedings 57: samostatné vydání 10. června a 5. října 1937 a
počátky 228/332 i následující položky od 241/377 potvrzují knižní
rok a rozsahy. Katalogový rok 1938 s tím není v rozporu.
Přijaty metadatové záznamy Greenwooda 1955, Levene–Wolfowitze 1944,
Bartona–Mallowse 1965 a Lindholma 1968 v rozsahu jmen, let a stran.

Výslovně přeskočená bibliografie: přesný dešťový citát a použitá
statistika Kermacka–McKendricka, nedostupná plná historická pojednání,
prvenství kupónové varianty, soukromý Christiansenův podklad 1975,
široce formulované prvenství kolizního testu mezi testy této sekce.
Dobový přetisk Bienaymého byl dříve přečten v zaznamenaném rozsahu;
jeho původní empirická data znovu nepočítáme.

Na 74 ještě navazují matematické odkazy 3.3.3–23/24 a 3.5–26;
na 75 odkaz 3.6–14. Jejich propojení zůstává ve frontě příslušných
sekcí. Středněkvadratický a maximum-of-t příklad na 75 ani tvrzení
o lepším generátoru 69069 mod2^30 nemají kompletní parametry
a historická data. Nejsou označeny za reprodukované. Proto 74–75
zatím zůstávají partial, nezávisle na bibliografických výjimkách.

## Procházky 31–33

Pro 55/24 tvoří prvních 79 výstupů 24 disjunktních trojic
(A,B,A xor B) a sedm dalších nezávislých bitů. Váhový polynom
je ((1+z)/2)^7((1+3z²)/4)^24; po vyloučení nulového počátečního
stavu se normalizuje (2^55 F−1)/(2^55−1). Stupeň 55 uvedený
v knize je správný, přestože okno obsahuje 79 bitů. Počet stavů
s převahou jedniček je přesně 18509401282464000, tedy
pravděpodobnost .5137390868954483523… .

Přezkoumána konstrukce lineárních forem, rozklad jejich podpor
na nezávislé komponenty a úplný malý výčet uvnitř každé komponenty.
Všechny čtyři uvedené polynomiální faktory odpovídají sazbě,
včetně sedmi pětibitových komponent po 86 výstupech. Uložených
7512 stavů ve 20 malých modelech navíc ověřuje obecný trojicový
rozklad pro k>2l. Každý druhý bit má totéž rozdělení konečného
okna: Frobeniovo umocnění zachová rekurenci a gcd(2,2^k−1)=1
permutuje fáze. U lichého multiplikativního generátoru je
(1+2a)(1+2b)≡1+2(a+b) mod4, což vysvětluje druhý nejnižší bit.

Obrázek pro 11/2 byl znovu porovnán s uloženou rekonstrukcí.
Počet 1306/2047 při délce 445 dává uváděných 64 %. Úplný soupis
2047 délek zůstává přijatý bez nového výpočtu. Nově zachyceno
**C0241, candidate, low**: pro délku 2045 je pravděpodobnost
1535/2047≈.74988, takže větu o převaze nul po polovině periody
nelze číst univerzálně. Důkaz vynechá dvě znaménka z celoperiodového
součtu 1. Původní graf návrat sám ukazuje a odstavec zmiňuje výjimku
celé periody; proto jde zatím jen o otázku rozsahu formulace.
Úloha 31 a strana 570 zůstávají v tomto bodě partial.

Úloha 32 má správný původní tříbodový protipříklad: při epsilon=1/10
je E X=0, Pr(X>0)=3/5 a Pr(X+Y>0)=9/25. Pro malé kladné epsilon
jsou právě součty dvou kladných bodů kladné, což dává
(1/2+epsilon)^2<1/2. Zjednodušení z errata 2005 s hodnotami
−b,a a pravděpodobnostmi a/(a+b),b/(a+b) funguje pro
a<b<(1+sqrt(2))a. Obě strany Coverova původního článku 277–278
byly nově vizuálně přečteny: související obrácení preference
dvou kol i rozdíl průměru od pravděpodobnosti výhry skutečně uvádí.
Další konstrukce článku nejsou součástí tohoto auditu.

Hlavní uniformní asymptotika 33 byla znovu odvozena ze
S=2W−L, a=k−2l≥1, b=l, L=a+3b. Charakteristická funkce je

    phi(t)=cos(t)^a (cos(t)^3+i sin(t)^3)^b.

Přesná znaménková Fourierova identita integruje Im(phi) proti
1/sin(t) pro liché L, cot(t) pro sudé L na [0,pi/2]. U nuly
je log phi=−Lt²/2+i b t³+O(Lt^4)+i O(b t^5). Integrace dává

    Pr(S>0)+Pr(S=0)/2
      =1/2+b/(sqrt(2pi)L^(3/2))+O(L^(−3/2)).

Zbytky po jádru 1/t mají integrály řádů b L^(−5/2),
Lb L^(−7/2) a b³ L^(−9/2), všechny O(L^(−3/2)). Druhý konec
intervalu nelze bez důkazu zanedbat. Pro a≥2 stačí faktor u²,
u=pi/2−t; pro a=1 dodá druhý faktor buď cot(t), nebo v závislosti
na paritě b první imaginární člen O(bu³). Střed je exponenciálně
malý. Stejný argument pro reálnou část dává pro sudé L
Pr(S=0)=sqrt(2/(pi L))+O(L^(−3/2)). Vyloučení nulového stavu
mění výsledek o O(2^(−k)). Tím je pokryta i obtížná oblast k≈2l.

**C0031 potvrzen**, čtyři pomocné vady na 571: úvodní koeficient
počítá opačný chvost, lineární člen g má být kladný, normalizovaný
Gaussův integrál má faktor 1/sqrt(2pi) a poslední zbytek potřebuje
m+3n, nikoli m−3n. Kontrola většího originálu zároveň potvrzuje,
že c_k=epsilon² theta^k g(1)/k! a mocniny epsilon^(k−2) jsou
vzájemně konzistentní; žádná další chyba těchto exponentů nepřibyla.
První integrál vedený přes +1 je správný. Výsledná asymptotika
zůstává správná nezávislým důkazem výše.

## Momenty 35 a rozsah experimentů

Nad nenulovými stavy dává každá nenulová binární lineární forma
součet znaků −1. Proto ΣZ_i=1 a pro různé pozice ΣZ_i Z_j=−1.
Pro m≤N plyne E S_m=m/N a E S_m²=m−m(m−1)/N. Trojice forem
má součet součinů 1, pokud je její xor nenulový, jinak −N.
Po odlišení všech šesti permutací různých trojic tedy

    E S_m³=[m³−6B(N+1)]/N.

Posun první pozice na nulu dává váhu m−j v definici B.
Zobrazení prvku tělesa pomocí k po sobě jdoucích výstupů je prosté;
rovnost posledních k−1 souřadnic u různých prvků znamená rozdíl
(1,0,…,0), což odpovídá 1+xi^i=xi^j. Tím je ověřena i méně
zjevná knižní definice B z projekcí stavů. Pro 55/24 jsou první
dvojice (31,55),(62,110), B_79=24. Nezávislé momenty z polynomu
souhlasí s přibližně −144; uložených 6977 oken 51 malých primitivních
rekurencí pokrývá všechny tři momenty.

**C0029 potvrzen:** v jednom řádku odpovědi 572 chybí /N u m³.
Již k=2,m=1 dává 1/3 oproti vytištěné 1. Zadání a zbytek důkazu
mají správný výsledek. Chybějící 2 před smíšeným součtem v části (c)
nemění danou rovnost, protože všechny tyto členy jsou nulové;
nezakládáme kvůli němu další nález. Změna 2024 jen rozepisuje m≪N.

Staré experimenty 200000 počátečních stavů na délku mají správný
55bitový posun, maskování, stride/discard a zpracování mod4. Nově
krátce regenerovány pouze SHAKE vstupní bajty podle uložených tagů:
oba SHA-256 přesně souhlasí s manifesty. Žádné vlastní procházky
znovu spuštěny. Data podporují delší okna i výběr sudých hodnot,
nejsou však historickými semeny nebo univerzálním důkazem.

Nově přečteny relevantní textové pasáže autorských preprintů
Vattulainena 1994 (soubor 3–7, tištěné 1–5) a Matsumota–Kurity
1992/1994/1996. Potvrzují kontext dvourozměrného testu, selhání
váhových testů i dlouhé úseky malé hustoty. Jejich experimenty
a celá konstrukce generátorů nebyly nezávisle znovu provedeny.
Vattulainen 1995 byl dříve čten na 214–219; tato zdrojová evidence
je přijata v daném rozsahu, nikoli rozšířena na celý článek.

## Monkey test 34 a numerika na 75

Šest generujících funkcí bylo znovu odvozeno ze slov končících
jedním ze zvláštních písmen: L_j=z(F−Σ_(ij zakázáno)L_i),
F=1+(m−d)zF+ΣL_j. Jsou to nejvýše čtyři lineární rovnice.
Potvrzeny také ekvivalence zakázaných dvojic. **C0030 potvrzen:**
případ ab,bc má čitatel 1, nikoli 1+z; koeficient z jinak dává
m+1 přípustných jednopísmenných slov místo m.

První moment počtu chybějících dvojic používá m smyček a (m)_2
různopísmenných hran. Pro dvě různé dvojice jsou násobnosti
6(m)_2, třikrát 2(m)_3 a (m)_4. To přesně reprodukuje oba
knižní momenty; podtržené mocniny jsou klesající součiny.
Přijatých 80979 slov ve 21 modelech potvrzuje funkce i momenty
nezávislým přímým počtem.

Pro normalizovaný pól s0 vychází tau=−log s0,
c=−A(s0)/(s0 D'(s0)). Všechny vytištěné koeficienty c a tau
souhlasí; případ 5 už ve sloupcích asymptotik používá správný
čitatel. Ostatní kořeny leží uvnitř jednotkového disku. Pro
kubický případ 4 to plyne ze znamének v −1,0,1; pro případ 5
z Rouchého věty s dominantním −mr² na |r|=1, m>4. V režimu
n≈2m² jsou případné polynomiální meze reziduí pohlceny poklesem
ostatních kořenů, takže lze zachovat absolutní zbytek O(1).

Přezkoumán celý 160bitový intervalový maticový certifikát.
Pravděpodobnosti přechodů a počátečního stavu jsou přesné dyadické
zlomky; nezáporné součiny se zaokrouhlují ven. Oba momenty mají
kladné koeficienty; rozptyl se omezí odečtením správných krajů
intervalu E X²−(E X)^2. Výsledky potvrzují

    E X = 141909.32995500691890740108161117408…,
    Var X = 84368.32646163049085579893634725520…,
    sd X = 290.46226340375179768668162964087… .

Čtverce mezí 290.455 a 290.465, nikoli plovoucí odmocnina,
certifikují zaokrouhlení. Šest historických pokusů má počty
141395,140909,141449,141066,141398,141219; všechny skutečně leží
1.5 až 3.5 směrodatné odchylky pod průměrem. Přečten C++ průchod
rekurencí i nezávislý NumPy model afinních mocnin. Oba používají
n hodnot a n−1 překrývajících se párů; hranice mezi pokusy se
nepočítá. Celočíselné produkty se vejdou do 64 bitů. Uložená shoda
šesti výsledků není vydávána za souborové porovnání každé hodnoty.

Perioda 2^29 plyne z lichého přírůstku a násobitele 1 mod4;
podíl vzorku je 1/256. Navržená příčina zploštění je v knize
výslovně hypotetická. Tvrzení o generátoru 69069 není bez dalších
parametrů nově reprodukováno. Úloha 34 má matematiku uzavřenou,
ale strana 75 jako celek proto zůstává partial.

## Errata, pokrytí a další kurzor

Použity čtyři čerstvě porovnané vrstvy z 6. listopadu. Výpis pro
celou sekci je `sources/sequential-2026-11-06/empirical-tests-errata.json`.
Na 74 jsou známé bibliografické a závorkové opravy. Odpověď 32
z roku 2005 je zjednodušení správného protipříkladu, změna 572
z roku 2024 jen notace. Pro C0029–C0031 ani C0241 oprava nenalezena.
Poslední fyzický dotisk a novost nálezů nejsou ověřeny.

Nově celé vypořádané původní strany: 73, 79 a 571. Strany 74,
75 a 570 mají výše vyjmenované zbytky. Strany 80 a 572 jsou
sdílené se začínající §3.3.3 a zůstávají partial do její kontroly.
Úloha 25 je nadále matematicky otevřená v dříve vymezeném rozsahu.
Další kurzor: §3.3.3, od původní 80 a odpovědí 572.
