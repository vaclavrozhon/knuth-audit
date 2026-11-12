# §3.3.4 D–E: příklady, tabulka a konstrukce násobitelů

Stav 2026-11-01. Původní sazba104–109 a odpovědi578–580 přečteny
vizuálně. Navazuje [mřížový základ](spectral-foundations.md).
Zde uzavřena matematika a numerika D–E, úlohy8 a11. Historické priority,
kritéria starých počítačových hledání a navazující F se prověřují dále.

## 1. Nezávislé ověření všech29 řádků tabulky1

Spektrální hodnota nu_t je délka nejkratšího nenulového vektoru celočíselné
mříže řešení u1+a*u2+...+a^(t-1)*ut=0 mod m. Pro t=2,...,6 bylo
vypočteno všech **145 přesných čtverců nu_t**, dvěma způsoby:

- Doslovný algoritmus S, včetně vyčerpávajícího průchodu jeho kvádru.
- Nezávislá celočíselná redukce LLL a přesný průchod koule po ortogonálních
  souřadnicích. LLL je zde pouze prostředek ke zrychlení: správnost minima
  nezávisí na kvalitě její redukce. Celočíselná transformační matice má
  ověřený determinant±1 a násobením se kontroluje nová báze.

Po Gramově–Schmidtově ortogonalizaci báze B_i označme B_i* kolmé vektory,
d_i=||B_i*||^2 a mu_ij jejich projekční koeficienty. Pro celé x platí

```
||sum x_i B_i||^2 = sum_k d_k*(x_k+sum_(j>k) mu_jk*x_j)^2.
```

Všechny d_i,mu_ij jsou přesné zlomky. Enumerace jde od poslední souřadnice
a omezuje zbývající normu již nalezeným vektorem. Je-li střed intervalu
A/B a zbývající čtverec poloměru C/D, podmínka pro x je přesně
(B*x-A)^2<=C*B^2/D. Proto stačí celočíselná odmocnina
floor(sqrt(floor(C*B^2/D))); žádné rozhodnutí o vyřazení větve nepoužívá float.
Při zlepšení minima se hranice jen zmenšuje. Všechny minimalizátory
zůstávají zahrnuté, včetně rovnosti na hranici. Nejtěžší tabulkový případ
potřeboval v této enumeraci jen46 navštívených souřadnicových uzlů.

Pro řádek25, generátor druhého řádu x_(n+2)=a*x_(n+1)+b*x_n mod p,
vyjádříme x_j=f_j*x_0+g_j*x_1. Duální báze má první dva řádky p*e1,p*e2,
další řádek (-f_j,-g_j,e_j); determinant je p^2. Použita samostatná
duální redukce a kvádr proti LLL/kouli. Obě metody souhlasí i ve všech
minimalizátorech. U ostatních řádků byly úplné množiny minim srovnány
v dimenzích3–6; v dimenzi2 minimum a jeho svědci.

V řádcích28,29 je b základ číselných cifer a modul je b^r-b^s+1.
Násobitel je b^(-389), respektive b^(-400), počítaný přesně modulo m.
Jsou to spektrální hodnoty víceslovných stavů, jak kniha výslovně uvádí;
nepřisuzujeme je přímo jednotlivým vydávaným cifrám.

Výsledky obsahují celé minimální vektory, redukované báze, unimodulární
transformace a přesné ortogonální normy. Největší modul má1376 bitů.
První běh dokončil27 řádků a první dimenzi28; pak selhala vnitřní
kontrola LLL v SymPy. Jeho zaokrouhlování volá `math.floor` na velkých
racionálních číslech. Pro zbývající případy byla použita vlastní zlomková
LLL s celočíselným zaokrouhlením. Hotové výsledky se neopakovaly.
Zjištění se týká pomocného softwaru, nikoli algoritmu knihy.

Všechny přesné celé položky tabulky souhlasí. Také všech145 logaritmů
lg(nu_t),145 hodnot mu_t a pět teoretických mezí prošlo intervalovou
aritmetikou s90 desetinnými místy, s přesnými racionálními konci intervalů.
Známá oprava1998 mění řádek25, sloupec lg(nu_4), z15.6 na14.6.
**C0042 zůstává jen kandidát:** jediná hrubá vědecká aproximace
nu_5^2 v řádku29 je vytištěna2*10^165, zatímco přesná hodnota je
2.6503385745833175...*10^165. Běžné zaokrouhlení na jednu platnou cifru
by dalo3*10^165. Jeho logaritmus275 a mu_5=1.15 jsou správné.
Konvence těchto velmi hrubých aproximací není výslovně stanovena;
neoznačujeme to za chybu výpočtu spektrálního minima.

## 2. Příklady a nové hodnoty z errat

Na104 souhlasí všech šest eukleidovských kroků, obě počáteční matice,
první změněné matice, všech15 redukcí, obě konečné matice i z=(0,0,1).
Zaokrouhlení nu_2=67654.37748 a nu_3=1017.21089 mají intervalové doklady.
Příklad z1982 s a=464680339,m=2^29,t=5 zlepší kvádrovým hledáním
čtverec normy2398 na2338; nezávislá koule potvrdila výsledek.
Řádek21,t=6 zlepší1501 na1438, jak kniha uvádí. Další zlepšení jsou
řádek26,t=4 a řádek29,t=6; slovo „vzácně“ neznamená, že se smějí vynechat.

Pro RANDU s efektivním modulem2^29 byly nové dimenze7,8,9 ověřeny
racionální koulí a samostatně PARI2.15.4 `qfminim` s robustním příznakem2
a100 desetinnými místy. Všechny vrácené vektory mají navíc přesně ověřenou
celočíselnou normu a kongruenci. Minim je8,10,12 včetně opačných znamének,
vždy s čtvercem116. Intervalový výpočet dává mu_9 zaokrouhlené11.98.
Původní pokus obecného duálního kvádru překročil limit10milionů bodů;
nebyl vydáván za úspěšný výpočet. Konečný přesný důkaz minima nese
racionální enumerace, PARI poskytuje nezávislé srovnání.

Oprava2004: a=2650845021,m=2^32 skutečně dává čtverce
4938969760,2646962,68342,8778,1506 a skóre3.61,4.20,5.37,8.85,4.11.
Všech pět minim ověřily obě metody, skóre má intervalové meze.
Historický úplný soupis2^30 násobitelů nebyl znovu proveden.
Oprava1999 k S7 výslovně připouští z_j>1; původní historickou zkušenost
nezaměňujeme za obecnou mez a všechny enumerace dovolují libovolná z_j.

## 3. Řetězové zlomky řádku8

Kanonický konečný řetězový zlomek a/m má poslední podíl aspoň2.
Pro řádek8 má všech35 podílů hodnoty1,2,3 a právě jeden je3.
Úplným soupisem potvrzeno také tvrzení, že pro m=10^10 žádné
a=1 mod20 nemá pouze podíly1,2. Nejde o náhodný pokus.

Definujme continuant K(q1,...,qs) jako jmenovatel řetězového zlomku
[0;q1,...,qs]. Pro prázdný seznam K=1; postupné hodnoty splňují
P_new=q*P+Q, Q_new=P. Rozdělíme seznam za prvním prefixem s
P>sqrt(m). Jeho předchozí hodnota Q<=sqrt(m), a P<=3*sqrt(m).
Má-li prefix čitatel A a předchozí čitatel B, a suffix continuant R
a continuant po vynechání jeho první položky S, platí

```
m=P*R+Q*S,   a=A*R+B*S,   gcd(R,S)=1,   1<=S<R.
```

Prázdný suffix (R,S)=(1,0) je ošetřen zvlášť. Pro každý prefix jsou
R omezeny mezi ceil((m+Q)/(P+Q)) a floor((m-Q)/P) a splňují
R=m*P^(-1) mod Q. Všechny možnosti se proto vyjmenují bez ztráty;
Eukleidův algoritmus na R,S rozhodne, zda má suffix jen podíly1,2.
Srovnání proti přímému Eukleidovi prošlo pro všech249 modulů2–250.
Velký soupis měl407132 prefixů a128879 suffixových kandidátů, žádné řešení.
První pilot odhalil chybějící podmínku gcd(R,S)=1 v kontrolním programu;
oprava byla provedena před velkým soupisem, předchozí bloky zachovány.

## 4. Úlohy8 a11: geometrická mez a Watermanova konstrukce

Připojení nulové složky k duálnímu vektoru dává nu_(t+1)<=nu_t.
Dosazením mu_2=pi*nu_2^2/m a mu_3=4*pi*nu_3^3/(3m) plyne

```
mu_3 <= (4/3)*sqrt(m/pi)*mu_2^(3/2).
```

Pro ilustrativní parametry m=10^10,mu_2=10^-6 je horní mez
0.00007522527780636... Odpověď je odhad, nikoli konstrukce dosahující
rovnosti. U velkých m převládne univerzální mez(40). Errata mění zadání
Line18 naLine10 a odkaz v odpovědi(39) na(40); obě změny zahrnuty.

V úloze11 je m=2^e a hledáme a=1 mod4. Primitivní řešení y1+a*y2=0 mod m
(primitivní znamená gcd(y1,y2)=1) má obě souřadnice liché. Substituce
y1=x1+x2,y2=x1-x2 dává nesoudělná x1,x2 opačné parity; vybereme x1 sudé.
Potom ||y||^2=2*(x1^2+x2^2) a
a=(x1+x2)/(x2-x1) mod2^e, kde jmenovatel je lichý, tedy invertibilní.
Odtud a-1=2*x1/(x2-x1); zejména a=1 mod4 a největší potence se získá
při x1=2 mod4. Pro k<e platí a=1 mod2^(k+1) právě tehdy, když
x1=0 mod2^k. Úloha10 dává z velké hodnoty ||y||^2 blízko2m/sqrt(3)
zaručenou dolní mez nu_2^2>sqrt(3)*m/2, ale ne vždy téměř optimum.

Hledáme N=x1^2+x2^2 těsně pod m/sqrt(3), N=1 mod4. Celá Gaussova
čísla jsou a+bi pro celá a,b, s normou a^2+b^2. Dělení zaokrouhlením
obou souřadnic zbytku zmenší normu, takže funguje Eukleidův algoritmus
a jednoznačný rozklad. Prvočíslo p=3 mod4 dělící normu musí dělit obě
souřadnice, a proto primitivní řešení neexistuje. Každé p=1 mod4 se
rozštěpí na (u+iv)(u-iv); kořen z^2=-1 mod p a gcd(z+i,p) jeho rozklad
spočítají. Aby řešení zůstalo primitivní, musí celá mocnina každého p
přejít na jednu z konjugovaných stran. Pro r různých prvočinitelů N>1
tak vznikne2^(r-1) řešení po ztotožnění znamének a výměny souřadnic.

Program ověřil Gaussův rozklad nezávislým přímým výčtem všech sudých
x1<=sqrt(N). Faktory byly vynásobeny zpět, prvočíselnost ověřena dělením.
Prvních16 řešení pro2^32 končí na N=2479700521-68, jak kniha uvádí.
Všechny vytištěné faktorizace, čtyři počáteční dvojice a jejich násobitele
i případ N-8 souhlasí. Spektrální hodnoty všech16 kandidátů mají dvě
nezávislé kontroly; řádek14 byl převzat z již dokončené tabulky.

Přívlastek „best“ není definován. Vybraný a=1566083941 maximalizuje mu_2
mezi těmito16 kandidáty. Největší min(mu_2,...,mu_6) má a=4249579229.
Žádný z ostatních kandidátů nezlepšuje všech pět hodnot zvoleného a.
Tuto nejednoznačnost proto neklasifikujeme jako chybu.

**C0043:** v desetinném příkladu580 jsou prohozené „former“ a „latter“:

```
(7+2i)*(2203+10202i) = -4983+75820i,
(7+2i)*(2203-10202i) = 35825-67008i.
```

První, nikoli druhý součin má použitelnou imaginární část75820.
Rovnost se zápisem |x2|+i|x1| navíc potřebuje zohlednit znaménka;
bezpečně se mají vzít absolutní hodnoty reálné a imaginární složky
součinu. Následná volba x1=75820,x2=-4983 a násobitel4160984121 jsou správné.
Pětinásobnou práci pro10^e chápeme jako heuristické vyjádření dodatečné
podmínky x1=0 mod10, nikoli dokázaný univerzální faktor času.

## 5. Normalizace mříže a periody

Hustota m znamená determinant primalní mříže1/m. Dva stejně dlouhé
vektory délky l s úhlem60 stupňů mají determinant l^2*sqrt(3)/2.
**C0041:** na109 je délka2/sqrt(3m); dává determinant2/(sqrt(3)*m),
nikoli1/m. Správná délka je sqrt(2/(sqrt(3)*m)). Třírozměrný příklad
(v,v,-v),(v,-v,v),(-v,v,v), v=(4m)^(-1/3), naopak má správný
determinant4v^3=1/m a duální minimum2^(1/6)*m^(1/3).

Konstanty gamma_t v(41) souhlasí s přesnými hodnotami v tabulce1
[Neumaierovy práce](https://pmc.ncbi.nlm.nih.gov/articles/PMC6743704/),
v jejím dodatku: gamma_t^t=4/3,2,4,8,64/3,64,256 pro t=2,...,8.
Naše kontrola přepočtu do nu_t a mu_t a důkaz t=2 jsou vlastní;
nepředstíráme nový důkaz globální optimality mříží v dimenzích3–8.
Metadata a přesný rozsah čtení jsou v `sources/spectral-hermite-reference.json`.

V(38) byla přesně ověřena prvočíselnost obou modulů a úplné řády
48271,40692 pomocí všech prvočinitelů p-1. Čínská věta dává vytištěné
a=1431853894371298687, společná perioda je74382023826798534, neboť
gcd(p1-1,p2-1)=62. V(39) má diskriminant472526882 kvadratický charakter-1
mod p=2^31-1; polynom je tedy ireducibilní. Mocniny prvku x v tělese
F_p[x]/(x^2-271828183*x+314159269) prokazují řád p^2-1. Všechny
testované podíly tohoto řádu a jejich nenuloví svědci jsou v JSON.

## 6. Evidence a errata

`spectral-table.json`:145 minim, původní i opravené tištěné hodnoty;
`spectral-details.json`:290 intervalových položek, pět mezí, matice,
RANDU, úplný continuantový soupis, errata a periody;
`waterman.json`:16 kandidátů, úplné reprezentace a spektrální certifikáty.
Čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální TeX
prohledány1.11.2026 podle106,107,109,580 a výrazů hexagonal,length,165,
67008,75820,10202,former,latter. Nalezené změny jsou výše zohledněny;
žádná neopravuje C0041 ani C0043. Nejnovější fyzický dotisk a prvenství
zůstávají neověřeny. Návrhy hlášení jsou neodeslané.
