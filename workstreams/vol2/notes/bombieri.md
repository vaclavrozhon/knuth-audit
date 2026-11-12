# §4.6.2–21: Bombieriho norma a malé faktory

Rozsah: všechny části úlohy 21 na straně 458 a odpověď na 683–684.
Níže jsou vlastní obecné důkazy; přesné kontroly slouží k ověření
přepisů, normalizací a krajních případů. Hlavní koeficientová mez
platí. Nový nález C0217 opravuje mocninu pi v pomocném integrálním
vyjádření; C0218 opravuje svazek bibliografického odkazu. Známé
opravy 1998, 1999 a 2005 se nepočítají znovu.

## 1. Značení a představa normy

Multiindex j=(j_1,...,j_t) je tice nezáporných celých čísel.
Píšeme |j|=sum j_i, j!=product j_i! a x^j=product x_i^(j_i).
Nerovnosti mezi multiindexy platí po souřadnicích. Homogenní polynom
u=sum u_j x^j stupně n má všechny nenulové členy s |j|=n.
Jeho vážený čtverec velikosti a Bombieriho norma jsou

    B(u) = sum_j j! |u_j|^2,     [u]^2 = B(u)/n!.               (B1)

Tato norma snižuje váhu smíšených členů. Například u=3xy^3-z^2w^2
má [u]^2=9/4+1/6=29/12. U nehomogenního polynomu stupně n přidáme
proměnnou y a každý člen doplníme na stupeň n. Tak má
4x^3+x-2 normu na druhou 16+1/3+4=61/3. Nulovému polynomu
přiřazujeme normu nula; následující tvrzení jsou pak triviální.

Jiná představa je rozdělit koeficient u_j rovnoměrně mezi všech
n!/j! slov délky n s danými počty jednotlivých proměnných.
Čtverce těchto nových koeficientů se sečtou na
(n!/j!)*|u_j/(n!/j!)|^2=j!|u_j|^2/n!. To dokazuje vysvětlení
pomocí nekomutujících proměnných na 684, včetně tištěného příkladu.

## 2. Identita ze součtu binomických koeficientů (a)

Uvažujme čtyři konečná pole koeficientů a_p,b_q,c_r,d_s.
Ve vytištěné levé straně je koeficient jejich součinu nulový,
pokud p+s není q+r. Jinak jsou j,k spojeny rovností k=q-p+j.
Každý sčítanec je

    p! q! r! s! / (j! k! (p-j)! (r-j)!).

Neplatné indexy znamenají nulový sčítanec. Po dosazení pro k je
součet roven

    q! r! sum_j binom(p,j) binom(s,r-j)
      = q! r! binom(p+s,r) = (p+s)!.                          (B2)

Vícerozměrný binomický koeficient je součin jednorozměrných.
Použitá rovnost v každé souřadnici počítá r-prvkové podmnožiny
disjunktního sjednocení p-prvkové a s-prvkové množiny podle počtu
prvků z první části. (B2) je přesně koeficient na pravé straně.
Tím je dokázána celá identita pro libovolné koeficienty, včetně
komplexních, bez předpokladu homogenity.

## 3. Dolní nerovnost pro součin (b), (c)

Položme a_p=v_p,b_q=conj(w_q),c_r=conj(v_r),d_s=w_s.
Pravá strana identity je B(vw). Levá strana je součtem
|S_jk|^2/(j!k!), kde

    S_jk = sum_(p-j=q-k>=0) v_p conj(w_q) p! q!/(p-j)!.

Každý člen je nezáporný. Je-li v homogenní stupně m, pro |j|=m
musí p=j a q=k. Tyto členy tedy samy dávají B(v)B(w).
Odtud B(vw)>=B(v)B(w). Je-li součin homogenní a nenulový,
jsou homogenní i oba faktory: součet nejnižších stupňů se rovná
součtu nejvyšších a rozdíly jednotlivých stupňů jsou nezáporné.

Pro deg(v)=m,deg(w)=k, n=m+k dostáváme

    [v][w] <= sqrt(binom(n,m))*[vw].                         (B3)

Homogenizace v a w jednou společnou proměnnou zachovává součin,
protože stupeň součinu nenulových polynomů nad C je součtem stupňů.
Proto (B3) platí i v nehomogenním případě s příslušnými definicemi.

## 4. Gaussovo vyjádření a C0217

Pro nezáporná celá a,b platí polární integrací v komplexní rovině

    integral_C exp(-|z|^2) z^a conj(z)^b dx dy
      = 0             pokud a != b,
      = pi*a!         pokud a = b.                         (B4)

Úhlová integrace zruší různé mocniny. Pro stejné mocniny zbude
2*pi*integral_0^infinity r^(2a+1)exp(-r^2)dr=pi*Gamma(a+1).
Gamma je rozšíření faktoriálu dané integrálem
Gamma(s)=integral_0^infinity r^(s-1)exp(-r)dr pro s>0.
Integrací po částech dostaneme Gamma(a+1)=a!.

Rozvojem |u|^2 a součinem t integrálů (B4) tedy vychází

    [u]^2 = 1/(n!*pi^t) * integral_(R^t x R^t)
              exp(-sum x_i^2-sum y_i^2)|u(x+i*y)|^2 dx dy.  (B5)

Na 684 je ve jmenovateli **pi^n**, ač n je stupeň a t počet
proměnných. Pro u(z)=z^2 máme t=1,n=2,[u]^2=1 a integrál 2*pi;
tištěná pravá strana je 1/pi. Pro u(z_1,z_2)=z_1 je naopak pi.
Nejde o konvenci normy, neboť (B1) a slovní příklad ji určují.
Chyba se týká pomocného vzorce; důkaz (B3) jej nepotřebuje.

## 5. Existence faktoru s malými koeficienty (d)

Výška H(v) znamená maximum absolutních hodnot koeficientů v.
Pro reálné s>=0 zde s! znamená Gamma(s+1). Logaritmus Gamma
je konvexní: pro 0<theta<1 aplikujeme Hölderovu nerovnost na
integrandy r^(a-1)exp(-r) a r^(b-1)exp(-r). Dostaneme
Gamma(theta*a+(1-theta)*b)<=Gamma(a)^theta*Gamma(b)^(1-theta).

Pro multiindex j s |j|=m tak j! >= (m/t)!^t, a z (B1)

    H(v)^2 <= m! [v]^2 / (m/t)!^t =: A(v).                 (B6)

Nechť u=vw je netriviální rozklad na stupně m a k=n-m.
Zvolme z těchto dvou faktorů ten s menší hodnotou A. Každý jeho
koeficient má čtverec nejvýše

    min(A(v),A(w)) <= sqrt(A(v)A(w))
      <= sqrt(n!)*[u] / ((m/t)!*(k/t)!)^(t/2)
      <= sqrt(n!)*[u] / (n/(2t))!^t.                       (B7)

První nerovnost je geometrický průměr, druhá používá (B3), třetí
opět logaritmickou konvexitu Gamma. Odmocněním je výška jednoho
faktoru nejvýše

    K_t(n)*sqrt([u]),    K_t(n)=n!^(1/4)/(n/(2t))!^(t/2).   (B8)

Jedna původní proměnná po homogenizaci znamená t=2. To je přesně
zadaná mez n!^(1/4)*sqrt([u])/(n/4)!.
Využijeme-li jen dosud nevyloučené stupně m, můžeme maximalizovat
předchozí výraz v (B7) přes tuto menší množinu. Důkaz netvrdí,
že takto vybraný faktor je ireducibilní; případné další rozdělení
se řeší znovu. Tuto výhradu obsahuje i kniha.

Ze Stirlingova vzorce Gamma(s+1)=sqrt(2*pi*s)*(s/e)^s*(1+O(1/s))
pro pevné t a n rostoucí plyne

    K_t(n)=c_t*(2t)^(n/4)*n^(-(2t-1)/8)*(1+O(1/n)),
    c_t=2^(1/8)*pi^(-(2t-1)/8)*t^(t/4).                   (B9)

Konstanta i exponenty na 684 jsou správné; c_2 je přibližně 1.004.
Asymptotika není tvrzení stejnoměrné pro t rostoucí s n.

## 6. Přesná rodina a horní nerovnost (e), (f)

Pro u=(x^2-1)^n po homogenizaci do stupně 2n dává (B1)

    [u]^2 = sum_k binom(n,k)^2/binom(2n,2k)
          = sum_k binom(2k,k)*binom(2n-2k,n-k)/binom(2n,n)
          = 4^n/binom(2n,n).                              (B10)

Poslední konvoluce je koeficient z^n v součinu dvou řad
(1-4z)^(-1/2); jejich součin je (1-4z)^(-1). Stirling pak dává
[u]^2=sqrt(pi*n)*(1+1/(8n)+O(n^-2)); zejména odpověď
sqrt(pi*n)+O(n^-1/2) platí. Norma sama je (pi*n)^(1/4)*(1+O(1/n)).
Pro v=(x-1)^n a w=(x+1)^n je [v]^2=[w]^2=2^n. Tak je (B3)
rovností. Vynechané čtverce v prvním tisku jsou **známé erratum
z 3. února 2005**, nikoli nový nález.

Pro horní nerovnost označme C_m(j)=m!/j! pro |j|=m a n=m+k.
Koeficient součinu je sum_j v_j w_(h-j). Trojúhelníková a
Cauchyova nerovnost dávají

    |sum_j v_j w_(h-j)|^2
      <= (sum_j |v_j|^2 |w_(h-j)|^2/(C_m(j) C_k(h-j)))
         *sum_j C_m(j) C_k(h-j).

Poslední součet je C_n(h), podle koeficientu x^h v
(x_1+...+x_t)^m (x_1+...+x_t)^k. Po vydělení C_n(h) a sečtení
přes h zbude [v]^2[w]^2. Tedy

    [vw] <= [v][w].                                      (B11)

Také (B11) lze chápat jako zmenšení eukleidovské normy při
průměrování koeficientů slov se stejnými počty písmen. Nerovnosti
(B3) a (B11) mají různé faktoriálové konstanty a nejsou ve sporu.

## 7. Porovnání s Mahlerovou mírou (g)

Pro u(x)=a*product_(i=1)^n(x-alpha_i) je Mahlerova míra
M(u)=|a|*product_i max(1,|alpha_i|). Norma ||u|| je obyčejná
eukleidovská norma koeficientů. Důkaz M(u)<=||u|| již máme
v [integer-factorization.md, §2](integer-factorization.md#2-norma-mahlerova-míra-a-meze-20).
Z definice homogenizované normy plyne

    M(u)^2/binom(n,floor(n/2)) <= ||u||^2/binom(n,floor(n/2))
                              <= [u]^2.                  (B12)

Protože binom(n,floor(n/2))<=2^n, je to požadovaná dolní mez.
Horní mez dostaneme z (B11) po rozkladu na lineární faktory:

    [u]^2 <= |a|^2*product_i(1+|alpha_i|^2)
           <= 2^n*M(u)^2.                                (B13)

Alternativně |u_j|<=binom(n,j)M(u), protože každý součin kořenů
v elementární symetrické funkci má absolutní hodnotu nejvýše
M(u)/|a|; po dosazení do (B1) zbude sum_j binom(n,j)=2^n.
Nulové kořeny ani konstantní polynomy nezpůsobují výjimku.
Označení „zhruba odmocnina“ v závěru úlohy je kvalitativní;
kvůli faktorům 2^(n/2) nejde o asymptotickou ekvivalenci všech vstupů.

## 8. Zdroje, známé opravy a bibliografie

Původní sazba 458/683/684 byla vizuálně prohlédnuta. Šest vrstev
errat je prohledáno v [cíleném záznamu](../sources/bombieri-errata.txt).
Oprava 14.4.1998 mění v_j na u_j v definici homogenity; 6.6.1999
doplňuje čtverec 1 v příkladu; 3.2.2005 opravuje výše uvedené normy.
Vzorec s chybným pi^n je už v rozšíření druhého vydání na straně 627.

Primární autorský [Zeilbergerův text](https://arxiv.org/pdf/math/9307202)
byl přečten jako textový výstup obou stran: identita, její důsledek,
koeficientový důkaz a bibliografie souhlasí s (a),(b). Jeho norma
je sqrt(B), bez dělení stupňovým faktoriálem. Metadata arXivu uvádějí
1993, text obsahuje revizi 1994 a vydání AMM101(1994),894–896;
dvoustránkový autorský soubor není původní třístránková časopisecká sazba.

Autorský [Beauzamy–Dégotův preprint](https://www.scmsa.eu/BB_Publications/BB_Degot_Differential_Identities.pdf)
je datován říjnem1993, má titul a11číslovaných stran. Textově byly
přečteny definice na1–2 a §4 na5–9, včetně Theorem12 a obou jeho
důkazů. Nejde o vizuální audit celého časopiseckého článku.
Jeho symetrická reprezentace a diferenciální identita jsou konzistentní
s naším koeficientovým důkazem, který nevyžaduje další výsledky článku.

**C0218:** na683 je Trans. Amer. Math. Soc. **345**(1995),2607–2619.
Autorův [seznam prací, položka74 na8](https://www.scmsa.eu/cvbb.pdf)
uvádí **347**, stejně jako hlavička autorova plného textu
[vložena na ResearchGate](https://www.researchgate.net/publication/265259474_Differential_identities).
DOI je 10.1090/S0002-9947-1995-1277095-1. Chybný svazek je i
v přídavku druhého vydání; odpovídající oprava nebyla nalezena.

U Beauzamyho článku1992 uvádí [vydavatel](https://www.sciencedirect.com/science/article/pii/S0747717110800069)
celý rozsah **463–472**. Odkaz knihy465–472 u Proposition5 může
být užší rozsah, proto samotnou odlišnost počáteční strany nepovažujeme
bez dalšího za nový nález. Plný text Proposition5 se nepodařilo získat;
nerovnost má úplný vlastní důkaz v §6. Autorský přehled Beauzamy–Enflo–Wang
z června1992 byl textově čten jen v relevantní části strany10
s definicí normy a produktovou mezí; nenahrazuje tento článek1992.

Lokální stahování v tomto bloku selhalo na DNS; přes webový nástroj
byly dostupné uvedené texty. Webové screenshoty nepředaly obrazová data,
proto se **nepočítají jako vizuální čtení**. Výpisy chyb a přesné rozsahy
jsou v manifestu. Fyzický dotisk a prvenství zůstávají neověřeny;
návrhy hlášení jsou neodeslané. Historické priority nevyplývají pouze
z data preprintu a neoznačujeme je tímto blokem všechny za ověřené.

## 9. Kontroly

[Program](../verify_bombieri.py) ověřuje čtyřpolynomovou identitu
odděleným koeficientovým modelem, komplexní součiny i jejich nezáporný
rozvoj, tištěné normy, rodinu (B10), a integrál (B5) nezávisle pomocí
reálných Gaussových momentů. Výškové meze používají přesná minima
celočíselných součinů faktoriálů, porovnání s Mahlerovou mírou vstupy
se známými komplexními kořeny. Numerická hodnota c_2 a Stirlingovy
poměry jsou pouze ilustrace; nejsou důkazem obecné asymptotiky.
Počty, PID a časy jsou v [uložených výsledcích](../results/bombieri.json).
První běh části norms zachytil naši záměnu komplexního sdružení
ve váženém rozvoji: druhé pole musí být conj(w), nikoli w.
Původní sazba má sdružení správně. Program i tento zápis byly opraveny;
samostatný již úspěšný blok identity se neopakoval. Původní chybový
log zůstává uložen pod názvem bombieri-norms-conjugation.log.
