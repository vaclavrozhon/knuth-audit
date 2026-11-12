# §4.6.2: celočíselné rozklady, Hensel a koeficientové meze

Tento blok uzavírá matematiku úloh **18–20, 22–27 a 40**, základní
rekonstrukci F a modulární gcd na stranách 450–454. Úloha 21, LLL,
vícerozměrná část 455, úlohy 32–36, 38–39, 41 a zbývající historické
odkazy mají samostatný rozsah. Celá sekce proto ještě není hotova.

Potvrzené opravy: C0213 (výjimky diskriminantu), C0214 (znaménko
limity Gräffeho iterace), C0215 (předběžný filtr při slabé mezi).
C0216 je pouze kandidát týkající se poslední číslice tabulky.
Nový fyzický dotisk ani prvenství nejsou ověřeny; hlášení nebyla odeslána.

## 1. Značení a přechod na monický polynom (18, 19, 24)

Obsah nenulového celočíselného polynomu je kladný gcd jeho koeficientů.
Primitivní část pp(u) vznikne vydělením obsahem, se znaménkem zvoleným
pro kladný vedoucí koeficient. Ten značíme a = lc(u). Monický znamená
a=1. Ireducibilita v této sekci znamená nemožnost rozkladu na dva
polynomy kladných stupňů; číselný obsah se řeší odděleně. To je důležité
pro úlohu 19: například 2x+6 splňuje její podmínky pro p=3, ale má
číselný faktor 2. Nejde o vyvrácení uvedeného stupňového tvrzení.

Gaussovo lemma říká, že součin primitivních polynomů je primitivní.
Po vyčištění jmenovatelů proto faktorizace nad racionálními čísly
odpovídá faktorizaci primitivní části nad celými čísly. V úloze 24
nejprve vydělíme vstup vedoucím koeficientem, vynásobíme nejmenším
společným násobkem jmenovatelů a faktory nakonec normalizujeme na
monické; původní racionální vedoucí koeficient ponecháme před součinem.
Primitivita po minimálním vyčištění jmenovatelů plyne z minimality
tohoto násobku a z původního monického koeficientu.

Pro primitivní u stupně n je v(x)=a^(n-1)u(x/a) monický a celočíselný.
Substituce x -> ax je automorfismus racionálních polynomů, takže
pokud v=product p_j je úplný monický rozklad, faktory u jsou
pp(p_j(ax)), až na původní znaménko. U monického dělitele w stupně m
napišme w(ax)=c*bar_w(x), kde bar_w je primitivní. Jeho vedoucí
koeficient b dělí a, a současně cb=a^m. Tedy a^(m-1) dělí c a ze
w_k a^k=c*bar_w_k dostaneme a^(m-1-k) | w_k pro k<m. To dokazuje
i část 18(b). Příklad 6x^3-3x^2+2x-1 dává v=x^3-3x^2+12x-36
a faktory (3x^2+1)(2x-1).

Eisenstein (19): kdyby u=vw s oběma stupni kladnými, p nedělí jejich
vedoucí koeficienty. Jejich redukce mají součin a*x^n, a proto jsou
obě monomy kladných stupňů. Jejich konstanty jsou násobky p, takže
p^2 | u(0), spor. Obsah může být od p nesoudělný a tímto argumentem
se nevylučuje; nad Q je závěr správný bez přídavné primitivity.

## 2. Norma, Mahlerova míra a meze (20)

Pro u=sum u_j x^j položíme ||u||=(sum |u_j|^2)^(1/2).
Pokud u=a*product(x-alpha_i), jeho Mahlerova míra je
M(u)=|a|*product max(1,|alpha_i|). Měří součin velikostí kořenů
ležících vně jednotkové kružnice, s vedoucím koeficientem.
Je násobná: M(vw)=M(v)M(w).

Pro |z|=1 platí |z-alpha|=|conj(alpha)z-1|. Rozvoj čtverce absolutní
hodnoty u(e^(it)) a integrace členů e^(ikt) dává Parsevalovu identitu

    ||u||^2 = (1/(2*pi))*integral_0^(2*pi) |u(e^(it))|^2 dt.       (I1)

Záměna faktoru x-alpha za conj(alpha)x-1 tedy nemění normu.
Provedeme ji pro všechny |alpha|<1. Absolutní hodnota konstanty
výsledku je právě M(u), a proto M(u)<=||u||. Postup funguje i pro
nulový kořen: náhrada je konstanta -1. Není třeba dělit u(0).

Koeficient u_j je až na znaménko a-násobkem elementární symetrické
funkce řádu n-j v kořenech. Nahradíme |alpha_i| čísly
beta_i=max(1,|alpha_i|). Pro čísla beta_i>=1 s pevným součinem P
zvětšuje náhrada dvojice (b,c) dvojicí (1,bc) symetrickou funkci
řádu k o (b-1)(c-1) krát symetrickou funkci řádu k-1 ve zbytku
proměnných. Sloučením všech beta_i do jediného P dostaneme

    |u_j| <= binom(n-1,j) M(u) + binom(n-1,j-1)|a|.              (I2)

Binomické koeficienty s indexem mimo rozsah jsou nula.
Je-li u=vw nad Z, pak M(w)>=|lc(w)|>=1. Z (I2) pro v stupně m
a z M(v)<=M(u), |lc(v)|<=|a| vychází

    |v_j| <= binom(m-1,j)||u|| + binom(m-1,j-1)|a|.              (I3)

To dokazuje všechny části 20. Pro polynom (22) je ||u||=sqrt(113).
Pro faktor stupně nejvýše 4 je největší mez 3sqrt(113)+3<35:
celočíselné koeficienty jsou tedy nejvýše 34. U kvadratického
faktoru jsou |v_1|<=11, |v_0|<=10, jak používá odpověď 22.

Jensenův vzorec v polynomiálním případě dostaneme přímo z
průměru log|e^(it)-alpha|. Ten je log max(1,|alpha|), protože
rozvoj log(1-z) má nulový kruhový průměr pro |z|<1; pro kořen
na kružnici přejdeme limitou. Logaritmická singularita je
integrovatelná a lokálně ji dominuje konstanta plus |log|t||,
takže je tento přechod oprávněný. Součtem přes kořeny dostaneme
průměr log|u| = log M(u). Pro kladné celé k dá stejný rozvoj

    average e^(ikt) log|u(e^(it))|
      = -sum_i alpha_i^k / (2k*max(1,|alpha_i|)^(2k)).           (I4)

To ověřuje i doprovodnou Fourierovu formuli na 683.
Landau 1905, strany 254–258, obsahuje Parsevalovu identitu,
Jensenův vztah a srovnání geometrického a kvadratického průměru.
Vlastní důkazy (I1)–(I4) nejsou odvozeny z numerického testu.

## 3. Gräffeho iterace a její přesná limita

Definujme hat(u)(x)=u(sqrt(x))*u(-sqrt(x)); odmocniny se v součinu
vyruší. Při u(x)=u_even(x^2)+x*u_odd(x^2) je
hat(u)=u_even^2-x*u_odd^2. Kořeny se umocní na druhou a
M(hat(u))=M(u)^2. S U_0=u, U_(t+1)=hat(U_t) proto máme horní meze

    c_t = ||U_t||^(1/2^t) >= M(u).                             (I5)

Normalizovaná rekurze knihy počítá totéž. Základní měřítko M(u)
se totiž po každém kroku mění druhou mocninou, zatímco normalizace
normou je kladný skalár.

Pro kořeny mimo jednotkovou kružnici lze po vydělení dominantním
koeficientem napsat U_t jako součin faktorů x-alpha_i^(2^t)
u vnitřních kořenů a 1-x/alpha_i^(2^t) u vnějších. Pokud je
|alpha_i|<=rho<1 nebo |alpha_i|>=1/rho, je tento součin
x^m+O_n(rho^(2^t)) po koeficientech, kde m je počet vnitřních
kořenů. Tím je odůvodněna rychlost sbližování c_t k M(u).
Normování ale **neodstraňuje fázi dominantního koeficientu**.

Pro reálné koeficienty je po prvním kroku dominantní znaménko
(-1)^m. C0214: při u=2x-1 máme přesně
U_t=1-2^(2^t)x pro t>=1. Normalizovaný polynom konverguje k -x,
ačkoli věta na 683 uvádí x^m=x. Pro komplexní vedoucí koeficient
může fáze i nadále oscilovat. Oprava: konvergence k monomu po
vydělení jeho fází; v reálném případě k (-1)^m*x^m.
Horní meze (I5) tato chyba neovlivňuje. Pokud je k kořenů na kružnici,
koeficienty na pozicích m a m+k zůstávají v absolutní hodnotě
od nuly odděleny, zatímco nižší a vyšší pozice mizí; limitu fází
toto tvrzení nepotřebuje.

Tabulka (22): hodnoty c_t včetně ne-monotónnosti odpovídají definici,
až na otázku zaokrouhlení páté iterace. Vypočteno
c_5=6.62274769156185950148556..., nejbližší čtyřmístné zaokrouhlení
je 6.6227, tisk 6.6228. **C0216 zůstává candidate**, protože text
neuvádí konvenci zaokrouhlení a rozdíl je menší než jedna jednotka
posledního místa. Celé koeficienty U_t jsou přesné; odmocniny
pro tuto tabulku jsou vyhodnoceny s 80 desetinnými místy.

## 4. Henselovo zdvihání (22)

Nechť u=vw modulo q a av+bw=1 modulo r, kde r|q. Předpokládejme
v monický, deg v=m, deg w=k a deg u=m+k. Hledáme V=v+q*dv,
W=w+q*dw s deg dv<m a deg dw<=k. Položme
f=(u-vw)/q modulo r. Protože r|q, kvadratický člen q^2*dv*dw
zanikne modulo qr; stačí vyřešit

    w*dv + v*dw = f modulo r.                                 (I6)

Vydělme bf polynomem v: bf=t*v+dv. Pak dw=af+t*w splňuje (I6)
a má stupeň nejvýše k, protože f má stupeň nejvýše m+k.
Pro prvočíselné r jde o obvyklý důkaz nad tělesem; stejný
argument platí nad Z/rZ, má-li v invertibilní vedoucí koeficient.

Jednoznačnost: pro rozdíl dvou řešení platí
w*delta_v=-v*delta_w. Bezoutův vztah dává v | delta_v,
a menší stupeň vynutí delta_v=0. Násobení polynomem s jednotkovým
vedoucím koeficientem je prosté i nad Z/rZ, proto delta_w=0.
Prvočíselnost r k této silnější formulaci není nutná.
V monickém případě můžeme pro W zvolit vedoucí koeficient přesně
lc(u); potřebný zbytek je tím zachován a stupeň neklesne.

Pozor na OCR: původní 684 a 685 správně mají deg dw<=deg w
a deg f<=deg u. Přepis se znakem < by byl chybný. Zdánlivý
problém při změně vedoucího koeficientu w byl po zobrazení
sazby zamítnut. Známé erratum 2000 opravuje jiný detail, tečku
v c*lc(v).

Pro r=p a q=p^e zůstane původní Bezoutův vztah platný modulo p.
Při zdvojení exponentu r=q využijeme Bezoutův vztah modulo q a
po zvednutí faktorů řešíme ještě
delta_a*V+delta_b*W=(1-aV-bW)/q modulo q. Tentýž postup (I6)
dá vztah A*V+B*W=1 modulo q^2. Tím je dokázána akcelerace
p,p^2,p^4,...; tvrzení o výhodnosti konkrétní velikosti slova
je zvlášť otevřený praktický kontext, nikoli matematická mez.

Pro více monických vzájemně nesoudělných faktorů v_i použijeme
inverzi c_i součinu ostatních faktorů modulo v_i a nastavíme
dv_i=c_i*f mod v_i. Čínská věta o zbytcích a stupeň <sum deg v_i
zaručí sum_i dv_i*product_(j!=i) v_j=f. U nemonického u nejprve
normalizujeme pomocí lc(u)^(-1) modulo nového modulu; volíme
p nedělící lc(u).

Přepsané příklady jsou ověřeny proti původní sazbě:
modulo 169 faktory na 451 souhlasí. Modulo 16 vychází
v=x^2+3x-1 a
w=x^6-3x^5-5x^4-4x^3+4x^2-3x+5.
Čárka nad prostřední 4 je ve zdrojové sazbě skutečně přítomna;
náš první očekávaný vektor ji přehlédl. Omezení (I3) zanechá
jediného kandidáta v, který nedělí u nad Z. Tím je důkaz
ireducibility (22) modulo 2 dokončen.

## 5. Rekonstrukce F a nebezpečí slabé meze

Jestliže primitivní u=vw má vedoucí koeficient a=b*c, potom

    a*u = (c*v)*(b*w),

a oba faktory napravo mají vedoucí koeficient a. Pokud M=p^e>2B
a B omezuje všechny koeficienty těchto škálovaných faktorů,
jejich zbytky modulo M mají jediného souměrného reprezentanta.
Správná podmnožina monických modulárních faktorů proto v kroku F2
dá přesně c*v. Test dělitelnosti a*u a přechod na pp vrátí v.

Při procházení podmnožin podle jejich počtu je první nalezený
faktor ireducibilní: jeho případný vlastní faktor by odpovídal
menší podmnožině a už by byl nalezen. Po odstranění nalezených
modulárních faktorů pokračujeme při stejném počtu d. Stačí
d<=r/2; každá netriviální bipartice má takového zástupce. Při
rovnosti stačí podmnožiny obsahující první faktor. Pokud r<=1,
zbytek vstupu je již ireducibilní a procházení se vynechá.
Počáteční mez pro všechny dělitele a*u zůstává platná i po
odstraňování, protože nové škálované faktory dělí původní a*u.

Pro mez platnou jen pro stupně <=deg(u)/2 testujeme z každé
bipartice stranu s menším stupněm. Pro mez zaručenou pouze
alespoň jednomu vlastnímu faktoru musíme zkoušet obě strany.
Takto nalezený faktor nemusí být ireducibilní; pro úplný rozklad
je bezpečné rekurzivně rozložit oba výsledky s jejich novými
mezemi. Poznámka odpovědi 21(d) sama upozorňuje, že malý faktor
nemusí být ireducibilní. Základní F s mezí pro všechny faktory
tuto dodatečnou rekurzi nepotřebuje.

C0215: navazující předběžný test konstanty vybrané strany není
bezpodmínečně bezpečný při nejslabší z uvedených mezí. Vezměme

    u=(x+1)(x^2+x+100)=x^3+2x^2+101x+100,
    B=20, M=p=41,
    v_1=x^2+x+18, v_2=x+1 modulo 41.

M>2B; faktor x+1 má všechny koeficienty <=B. Kvadratický faktor
je modulo 41 ireducibilní (diskriminant 11 není čtverec).
Pro r=2,d=1 vybere F2 pouze v_1, protože požaduje i_1=1.
Jeho souměrná konstanta 18 nedělí u(0)=100. Předběžný filtr
tak odmítne bipartici ještě před zkouškou druhé strany, ačkoli
v_2=x+1 je pravý faktor. Tento příklad se netýká správnosti F
s plnou mezí; vyvrací společné použití slabé meze a uvedeného filtru.

Oprava: při testování obou stran nepřeskočit bipartici, pokud
projde konstantní test aspoň jedné strany. Alternativně udržovat
samostatnou mez M>2|a*u(0)|, která bezpečně rekonstruuje konstanty
všech skutečných škálovaných faktorů. Případ u(0)=0 řešíme nejprve
odstraněním x; totéž je třeba před použitím obráceného polynomu.

## 6. Diskriminant a modulární gcd (23)

Diskriminant primitivního f stupně n je
D=(-1)^(n(n-1)/2) Res(f,f')/lc(f); resultant Res je determinant
Sylvesterovy matice. Pro f bez násobných kořenů je D nenulové
celé číslo. Pokud p nedělí lc(f), je redukce bez násobných faktorů
právě tehdy, když p nedělí D. Bez zachování stupně tato
ekvivalence neplatí.

C0213: f=2x^2+2x+1 je primitivní, D=-4, ale modulo 2 je f=1,
bez násobného faktoru. Netriviální zbytek dává
f=2x^3+2x^2+x+1, D=-72 a f mod2=x+1. Odpověď 23 na 686
proto potřebuje výjimku pro p|lc(f), a pro neprimitivní vstup
také p|cont(u). Konečnost špatných prvočísel v zadání zůstává
správná: stačí vyloučit dělitele nenulového
cont(u)*lc(pp(u))*D(pp(u)).

Nejmenší vhodné p je O(n log(nN)) pro stupeň n a koeficienty
omezené N, s obvyklým přidáním konstanty pro malé vstupy.
Hadamardova determinantová nerovnost pro resultant dává
log|cont(u)*lc(f)*D(f)|=O(n log(nN)). Kdyby všechna prvočísla
do C*n log(nN) dělila toto číslo, jejich součin by byl příliš
velký: elementární Čebyševova mez sum_(p<=x) log p>=c*x pro
dostatečně velké x dává spor pro velké C. Tato mez byla
použita a doložena již v prvočíselném bloku; není předpokládána
prvočíselná věta.

Pro (22) vyšel D=-5869831203567, nezávisle jako diskriminant
a determinant resultantu. Jeho prvočíselní dělitelé jsou přesně
3,23,233,121702457, jak uvádí odpověď. U všech čtyř je gcd(u,u')
modulo p netriviální; protože u je monický, žádné výjimky ze
změny stupně zde nejsou.

Pro modulární gcd nechť d=gcd(u,v), u,v primitivní a
a=gcd(lc(u),lc(v)). Definujme bar_d=(a/lc(d))*d.
Pro p nedělící a má bar_d modulo p zachovaný stupeň a dělí
q=gcd(u modp,v modp). Proto deg q>=deg d. Pokud souměrný
reprezentant a*q má primitivní část dělící u i v nad Z,
musí být rovna d: má nejvýše stupeň d z dělitelnosti a nejméně
stupeň d z modulární nerovnosti.

Pro dostatečně velký modul a správný stupeň je reprezentant
přesně bar_d. Špatných prvočísel je konečně mnoho: pokud se
žádný vedoucí koeficient v přesném primitivním Eukleidově
řetězci nevynuluje, jeho redukce dává týž řetězec až na jednotky.
Při spojování více prvočísel udržujeme nejmenší dosud nalezený
stupeň, při jeho poklesu zahodíme staré zbytky a vyšší stupně
ignorujeme. Čínská věta o zbytcích potom rekonstruuje bar_d;
dělení nad Z je závěrečný certifikát. Pro Henselovu variantu
je navíc potřebná nesoudělnost d s alespoň jedním kofaktorem,
jak výslovně uvádí (27); její zajištění patří do úloh 34–35.

## 7. Konkrétní rozklad, stupně a rekonstrukce zlomků (25, 26, 40)

Úloha 25 má rozklad
(x^2+x+1)(x^3-x+2). První faktor je ireducibilní pro záporný
diskriminant -3; druhý nemá celočíselný kořen mezi +-1,+-2,
a kubický monický polynom je pak ireducibilní. Součin odpovídá
zadanému x^5+x^4+x^2+x+2. Modulární rozklady v odpovědi jsou
v souladu s těmito faktory.

Úloha 26: bit i značí, že i je dosažitelný součet již zpracovaných
stupňů. Začínáme bitem 0; přidání d_j mění D na D OR (D<<d_j),
protože podmnožina buď obsahuje nový prvek, nebo jej neobsahuje.
Důkaz invariantem zahrnuje násobnosti jako samostatné položky.
Stačí bity 0,...,floor(n/2), zbývající doplníme symetrií i<->n-i.
Známá errata 2005/2024 mění symbol/sazbu; samotná rekurze je správná.

Úloha 40: má-li skutečný faktor v všechny koeficienty |v_j|<=B,
jeho monický modulární obraz má koeficienty v_j/lc(v).
Jmenovatel je modulo p^e invertibilní, protože p nedělí lc(u).
Při M=p^e>2B^2 je každý redukovaný zlomek s čitatelem do B
v absolutní hodnotě a kladným jmenovatelem do B určen jednoznačně:
rozdíl křížových součinů je násobek M a má absolutní hodnotu
nejvýše 2B^2<M, tedy je nula. Zastavený rozšířený Eukleidův
algoritmus z [úlohy 4.5.3–51](euclid-reconstruction.md) jej nalezne.
Vyčištění jmenovatelů a pp dá původní faktor; dělitelnost nad Z
je nutné nakonec ověřit. V testu se importuje pouze již dokázaný
pomocník, starý audit úlohy 51 se neopakuje.

## 8. Přesný význam „téměř všechny“ (27)

Fixujeme stupeň n>=2 a vybíráme koeficienty monického polynomu
nezávisle z celých čísel [-H,H]. Pro konečnou množinu k různých
prvočísel se při H->infinity jejich zbytky blíží rovnoměrnému
součinovému rozdělení (čínská věta). Počet monických ireducibilních
polynomů stupně n nad F_p je a_(n,p); jeho vzorec byl dokázán
v [berlekamp.md](berlekamp.md). Pro všechna dost velká p je
a_(n,p)/p^n>=1/(2n). Racionálně reducibilní vstup je reducibilní
modulo každé p, takže horní asymptotická hustota takových vstupů
je nejvýše (1-1/(2n))^k pro každé k. Po H->infinity teprve
pustíme k->infinity. Hustota je nula.

Pro obecné koeficienty v krabici [-H,H]^(n+1) využijeme událost,
že vedoucí koeficient je modulo p nenulový a normalizovaný
polynom je ireducibilní. Její asymptotická pravděpodobnost je
(1-1/p)*a_(n,p)/p^n, opět zdola omezená kladnou konstantou.
Tím získáme hustotu nula pro reducibilitu kladných stupňů.
Primitivní polynomy mají kladnou hustotu 1/zeta(n+1): pro konečnou
množinu prvočísel plyne součin z CRT a zbytek se omezí součtem
O(sum_(p>P) p^(-n-1)); společný dělitel nenulového koeficientového
vektoru nepřesahuje H. Podmínění primitivitou tedy hustotu nula
nezmění. Případ n=1 je přímý.

Silnější větu odpovědi, že téměř všechny pevné polynomy jsou
ireducibilní modulo nekonečně mnoho prvočísel, **nelze získat
jen záměnou těchto limit** nebo spočetnou unií množin hustoty nula.
Lze ji doplnit přes generickou Galoisovu grupu a větu o rozdělení
Frobeniových tříd, jejichž historický kontext se řeší u 37.
Zadaný závěr o ireducibilitě nad Z má výše samostatný úplný důkaz.

## 9. Podklady a běhy

Původní strany 450–455, 457–460, 682–686 a 690 byly vizuálně
prohlédnuty; matematický rozsah uzavření je uveden v úvodu.
Landau 1905: titul/251 a254–259 primárně přečteny, včetně obecného
součinového výsledku na259; zbytek článku není tím uzavřen. Přístupové neúspěchy
Schönemann/Jensen jsou v sources/integer-factorization-downloads.json.
Odkazy Mignotte, Gräffe, Specht, Cerlienco–Mignotte–Piras,
historie Hensela a praktická srovnání zůstávají v historickém podbloku.
Vlastní matematické důkazy se neopírají o jejich nedostupný text.

Šest vrstev errat: původní polynomial-factorization-errata.txt
a nový cílený integer-factorization-errata.txt, oba s hashi.
Změny 1998 v úloze20(a), 2004 v odpovědi20(c), 2000 v Henselovi,
2009 v jeho atribuci, 2012 v součtu stupňů na453, 2005/2024 v
bitovém zápisu26 jsou známá errata. Pro C0213–C0216 nebyla
odpovídající oprava nalezena.

[Program](../verify_integer_factorization.py) a
[výsledky](../results/integer-factorization.json):
60 jedinečných zdvihů proti úplnému výčtu 2760 oprav, 108 zdvojování
modulu se zdviháním Bezoutova vztahu, 185 zdvihů více faktorů,
36 celočíselných rozkladů proti SymPy, 2766 přesných koeficientových
mezí, 50 komplexních normových identit, 100 modulárních gcd,
3279 množin stupňů a 120 rekonstrukcí faktorů / 524 zlomků.
Nejde o měření asymptotické rychlosti.

Dva počáteční problémy patřily validátoru: nenormalizované vstupy
do pomocníka pro gcd nad F_p a přehlédnutá záporná 4 v přepisu.
Třetí zastavení bylo při kontrole zaokrouhlení c_5; vznikl z něj
výše popsaný kandidát, nikoli tvrzení o selhání Gräffeho metody.
Dříve dokončené části obou kombinovaných bloků jsou uchovány jako
obnovené checkpointy s výslovně neznámým dílčím časem; po rozdělení
se neopakovaly. Logy neúspěšných pokusů zůstaly zachovány.
