# Souvislá revize: základ spektrálního testu

Revize 6. listopadu 2026, třetí vydání / první dotisk 1997. Znovu byly
vizuálně přečteny původní strany 93–104, 115–116 a 577–580; tato uzávěrka
pokrývá A–C, správnost S1–S10 a úlohy 1–7, 9–10, 12–15. Číselný příklad
103–104, úloha 8, Watermanova konstrukce a následující úlohy se dokončují
v navazujícím bloku. Zobrazení celé stránky není kontrolou všech jejích úloh.

Přečteny celé `spectral.py`, `verify_spectral_foundations.py`, všechny čtyři
výsledkové bloky a dokončovací log. Výsledky přijaty bez opakování běhu:
1 103 modelů / 5 515 minim, 650 modelů potence 2, 15 600 intervalových
případů a 48 racionálních redukcí. Nezávislý řešič skutečně prochází kouli
v původních souřadnicích; nepřebírá redukovanou bázi S. Úplné množiny
minimalizátorů byly porovnány pouze v dimenzích 3–6. V dimenzi 2 se
kontrolovalo minimum a jeho svědek, nikoli výpis všech minimalizátorů.

První historická chyba logu je neúspěch původní meze úlohy 6, nikoli
nedokončená současná validace. Čtyři následné bloky jsou úspěšné.
Nový dlouhý výpočet ani pomocný proces nebyl spuštěn.

## Mříž, definice a obrázek 8

Pro množinu všech stavů je periodické rozšíření `L = V0 + Lambda`,
kde `V1=(1,a,...,a^(t-1))/m`, ostatní řádky jsou souřadnicové jednotky
a `V0=(c/m)(0,1,1+a,...)`. Průnik s jednotkovou krychlí je přesně
m původních bodů, determinant Lambda je 1/m. Duální mříž tvoří přesně
celočíselné vektory splňující `sum u_j a^(j-1) = 0 mod m`.
Pro nenulový duální vektor jsou roviny `U.X=U.V0+q`, q celé,
vzdálené `1/||U||`. Minimum délky duálního vektoru tedy určuje největší
rozestup pro pokrytí **celé periodické mříže**. Posunutí V0 jej nemění.

Nový **C0243, pouze candidate / low**, odděluje tuto správnou větu od
doslovného úvodu na 94–95, který mluví o pokrytí konečné množiny bodů.
Pro plně periodický generátor `m=2,a=1,c=1` jsou dvojice `(0,1/2)` a
`(1/2,0)`. Obě leží na přímce `x+y=1/2`. Rodina
`x+y=1/2+kR`, k celé, je pokrývá pro libovolné kladné R, s rozestupem
R/sqrt(2); konečné maximum neexistuje. Naproti tomu duální kongruence
`u+v=0 mod 2` má nejmenší nenulovou normu sqrt(2), kterou vrátí S.
Stačí do úvodní definice zahrnout všechny celočíselné posuny bodů.
Pozdější strany 96–98 už periodickou mříž výslovně zavádějí: proto
nejde o potvrzenou chybu algoritmu a interpretační otázka zůstává otevřená.

Srovnávací autorský zdroj LatticeTester uvádí definici přes celou mříž:
[průvodce 2025](https://www.iro.umontreal.ca/~lecuyer/myftp/papers/lattester-guide-2025.pdf).
K dispozici byl pouze indexovaný úvod; přímé otevření i stažení vrátilo
ochrannou HTML stránku. Plný PDF nebyl získán ani přečten. Vlastní
dvoubodový argument výše na tomto externím prameni nezávisí.

Obrázek 8 byl prohlédnut v původní sazbě jako geometrická ilustrace.
Jeho parametry 137,187,256 dávají plnou periodu (137=1 mod4, 187 liché).
Vektory `(-7,15)` a `(11,13)` mají determinant -256, normy na druhou
274 a 290 a skalární součin 118. Protože `2*118 <= 274 <= 290`,
Gaussovo kritérium níže dává přesně nu_2^2=274. Jejich rozdíl `(18,-2)`
má normu na druhou 328. Odpovídají vytištěným směrnicím a rozestupům.
Přijatý přesný soupis všech 256 stavů potvrzuje tři uvedené počty
obsazených přímek 20,21,24; ty se nesmějí zaměnit s počty všech přímek
protínajících krychli. Neprováděla se automatická rekonstrukce jednotlivých
drobných značek perspektivního obrázku. Výrok připisovaný Givensovi nemá
samostatný dohledaný pramen a je zaznamenán jako bibliografická výjimka.

Úvodní historické hodnocení na 93, že všechny tehdy známé špatné generátory
testem neprojdou a že jde o nejmocnější test, nemá vymezený seznam generátorů
ani srovnávací kritérium. Není tímto blokem nezávisle ověřeno. Praktické
výroky na 95 o významu velkých dimenzí jsou doporučení v dobovém kontextu,
nikoli dokázaná záruka nezávislosti konečných bitových bloků.

## Redukce a správnost S

Z `Y=sum x_i U_i` a duality plyne `x_k=Y.V_k`. Cauchyho nerovnost
dává Lemma A a konečnou množinu kandidátů pod libovolnou známou horní
mezí. To zároveň dokazuje existenci kladného minima pro nesingulární U.
Pro singulární `U=((1,0),(alpha,0))` s iracionálním alpha dává princip
přihrádek nenulová celočíselná x,y s `0<|x+alpha*y|<1/N` pro libovolné N.
Odpověď 13 je matematicky správná; její zadání odkazuje chybně na (19)
místo definiční rovnice (17), **C0040**.

Transformace (23) má determinant 1, zachovává dualitu i mříž. Reálná
q minimalizující jednotlivé nové řádky V současně minimalizují nový
řádek U: kolmost jednoho řádku ke všem ostatním v jedné duální bázi
je ekvivalentní odpovídající kolmosti v druhé. Gradient v úloze 12
je správný; Hessova matice je kladně definitní Gramova matice, takže
stacionární bod je skutečné jediné minimum. Po celočíselném zaokrouhlení
se U může prodloužit; S správně uchovává nejlepší dřívější mez s.

Při podmínce S5 `2|Vi.Vj|>||Vj||^2` se Vi přísně zkrátí. Délky
ostatních řádků V nerostou. Řádky zůstávají v pevné diskrétní mříži
a omezené kouli, která má konečně mnoho bodů, takže redukce skončí.
Tento důvod platí i pro obecné reálné nesingulární U; nemusíme chybně
předpokládat, že všechny jeho čtverce délek jsou celá čísla.

V dimenzi 2 tvoří dva duální celočíselné řádky s determinantem ±m
bázi všech duálních řešení. Pokud A=||u||^2, B=||v||^2, C=u.v
a `2|C|<=A<=B`, pak
`||xu+yv||^2 >= A*(x^2+y^2-|xy|) >= A` pro celočíselnou nenulovou dvojici.
To potvrzuje úlohu 4 a minimální bázi obrázku 8 výše.

V S2 zůstává determinant ±m, h-a*p a h'-a*p' jsou násobky m,
`p*p'<=0`, `|p'|<=|p|` a `||(h'+h,p'+p)||^2>=h^2+p^2=s`.
Při úspěšném kroku h klesá, ale nemůže být nula: nulový zbytek má
absolutní druhou souřadnici m a nepřinesl by přísné zlepšení.
Nejbližší projekční celočíselné q', pokud zkrátí druhý řádek pod s,
není 0 ani -1 a musí být `floor(h'/h)` nebo o 1 větší.
První možnost zkouší S2, druhou S3. Po selhání první a úspěchu druhé
platí Gaussovo kritérium s novým kratším vektorem; po selhání obou
platí s dosavadním vektorem a nejbližší projekcí. Tištěný důkaz 578
i rozepsané invarianty staré poznámky jsou v tomto rozsahu správné.

S4 rozšíří duální bázi o novou souřadnici a zachovává determinant m;
vytištěné V je škálováno tak, že `U*V^T=mI`. Proto S7 správně
omezuje `|x_j| <= floor(sqrt(s*||Vj||^2)/m)`. Vnořené celočíselné
odmocniny jsou ekvivalentní. S8–S10 procházejí právě polovinu nenulového
symetrického kvádru, jeden z vektorů x,-x. Žádný minimalizátor se neztratí.
Kód odpovídá těmto krokům; přidaný výpis minimálních vektorů v kódu
neznamená, že odpověď k úloze 17 je už zkontrolovaná (navazuje zvlášť).

Úloha 14 souhlasí s přesným uloženým trasováním: tři eukleidovské
kroky, čtyři průchody indexem j, obě vytištěné matice a `z=(0,0,1)`;
`nu_2^2=50`, `nu_3^2=6`. Tvrzení 102 o obvyklé velikosti mezivýsledků
je empirické, nikoli dokázaná mez pro bezpečný strojový datový typ.
Frekvence výjimek S7 v opravě 1999 nebyla nezávisle reprodukována.

## Pět starších nálezů znovu posouzeno

**C0036, chyba náhradního textu errat 2003.** Pro potenci 2 je
b=a-1 nenulové modulo m a b^2=0 modulo m, tedy a^j=1+j*b modulo m.
Vektory `(1,-2,1)` a `(1,-1,-1,1)` dávají obecné meze 6 a 4.
Je-li d=gcd(b,m), pak m dělí d^2 a pro plnou periodu je d>=4,
s jedinou výjimkou m=9,d=3. V dimenzi 3 má vektor normy na druhou
menší než 6 součet absolutních složek nejvýše 3. Jeho součet musí
být nula modulo d, a proto je pro d>=4 nulový: zbývají pouze
`e_i-e_j`. Rozdíl indexů 2 vyžaduje b=m/2, čili rodinu
`m=8q,a=4q+1`; v ní jsou obě minima 2. V dimenzi 4 přibývá rozdíl
indexů 3 a ternární rodiny `m=9q,a=3q+1 nebo6q+1`. Pro m=9 jsou
nu_3^2=5 a nu_4^2=2. Tím je stará úplná klasifikace znovu doložena.

Původní poslední tři řádky 577 obsahují binární rodinu s chybějícím
`1+`. Obraz errat 32 výslovně nahrazuje všechny tři řádky dvěma
ternárními: binární rodina proto v opravě opravdu chybí. Původní
přepsaný text a chyba nové opravy jsou v UI odděleny. C0036 má druh
`errata`; původní 577 je související stránka, ne místo nového opomenutí.

**C0037, neplatná dolní mez úlohy 6.** Pro prvočíslo m=131 a
primitivní a=97 jsou podíly 1,2,1,5,1,4, tedy A=5. Vektor (5,4)
splňuje kongruenci a má normu na druhou 41. Přesně
`41*31=1271 < 1310=10*131`, takže `41*pi/131 < 2*pi/(5+1+1/5)`.
Primitivitu dokládají tři uložené modulární mocniny pro prvočinitele
130=2*5*13. Nejde o příklad vyloučený předpoklady sekce.
Chybný mezikrok odpovědi je odhad `131/20 < 5+1+1/5`.
Platná slabší mez má jmenovatel A+2: v determinantové identitě pro
nenulové zbytky a jmenovatele konvergentů jsou oba sousední poměry
nejvýše 1 a druhý přísně menší než 1; AM–GM dokončí důkaz.
Počáteční kandidát m^2 není minimální, protože `a^2+1<m^2` pro 0<a<m.
Přechod S3 přes q+1, pokud zlepší normu, odpovídá následujícímu
běžnému konvergentu s dalším podílem 1. Konečný soupis není náhradou
tohoto důkazu. Závažnost medium: chybná záruka, samotné S se nemění.

**C0038, posun může změnit počet rovin.** Obraz krychle při X->U.X
má konce M=sum záporných složek a P=sum kladných. Dolní je zahrnut
právě při M=0, horní právě při P=0. Počet hladin rho+q je proto
`sum|u_j| - [smíšená znaménka a rho celé]`. Pro neposunutou mříž
je hlavní odpověď správná; hranatá poznámka o nezávislosti na c není.
Příklad m=4,a=1,U=(1,-1) mění jednu protínající přímku L0 na dvě
při c=1. Srovnání dvou plně periodických přírůstků u m=256,a=137
navíc mění obsazené přímky normály (18,-2) z 19 na 20.
Posun neovlivní rozestup ani hodnotu spektrálního testu. Závažnost medium.

**C0039, hraniční formulace Minkowského věty.** Otevřená krychle
(-1,1)^t má objem 2^t a žádný nenulový celočíselný bod. Vytištěná
obecná formulace vyžaduje přísný objem nebo uzavřenost. Důkaz Hermitovy
meze v úloze 9 je správný: primitivní minimalizátor lze doplnit na
unimodulární bázi, oddělit jeho směr a zaokrouhlit první souřadnici.
Indukce dá `theta <= (4/3)^((t-1)/2)*|det U|^(2/t)`.
Minkowského důsledek `mu_t<=2^t` také zůstává platný přes větší koule
a konečnost množiny mřížových bodů v omezené oblasti. Porovnání
s Hermitovou mezí pro všechna t>=9 plyne z ověřených základů 9,10
a rostoucího dvoukrokového poměru
`pi*(4/3)^(t+1/2)/(2*(t+2))`. Závažnost low, hlavní meze nejsou chybné.

Úloha 10 je správná: primitivnost y a kongruence dávají gcd(y2,m)=1;
Bézout a přičtení násobku y poskytují komplementární u. Normalizace
alpha=|u.y|/m, beta=||u||^2/m, gamma=||y||^2/m dává
`beta*gamma=1+alpha^2`, `alpha<=gamma/2`, `gamma<2/sqrt(3)`.
Předpoklad alpha>beta/2 by dal
`alpha>gamma-sqrt(gamma^2-1)>gamma/2`, spor. Oba řádky proto splňují
Gaussovo kritérium ve vhodném pořadí.

**C0040** je pouze chybný odkaz popsaný výše, závažnost low.
Nový potvrzený matematický nález v tomto bloku nevznikl.

## Errata, neověřené prameny a další kurzor

Čtyři vrstvy errat a aktuální TeX znovu prohledány v odpovídajících
stránkách i pomocí matematických pojmů. Snapshot z 6. listopadu 05:47 UTC
je byteově shodný s dřívějším; znovu se nestahoval. Relevantní položky:
103/S7 (1999), 115/úloha 8 (1999), 577/odpověď 3 (2003),
578/odpověď 8 (1999), 579/Hermitův bibliografický svazek (2012).
Žádná nenapravuje C0037–C0040 ani úvodní definici C0243.

Gauss §171, Gramův článek 1883, Kaib–Schnorr 1996, původní Hermitův
text a osobní atribuce Gosper/Dieter nebyly nově získány; matematika
má nezávislé důkazy a konkrétní citace jsou výslovné bibliografické výjimky.
Nejnovější fyzický dotisk ani prvenství nálezů nejsou ověřeny.
Žádná zpráva ani nový emailový návrh nevznikl.

Další kurzor: dokončit číselný příklad 103–104, D/E od 104–105,
tabulky 106–107, úlohy 8 a 11; pak rozšíření algoritmu, discrepancy
a historický konec sekce. Přetrvávající mezery §3.3.3 se tím neuzavírají.
