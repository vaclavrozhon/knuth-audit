# §3.3.4: mřížový základ a první úlohy

Stav 2026-11-01. Původní strany93–105,115–116,577–580 byly vizuálně
přečteny. Tato poznámka uzavírá základ A–C, správnost algoritmu S a úlohy
1–7,9,10,12–15; číselný příklad104, tabulky, historie a další úlohy
pokračují samostatně. Konečné testy nejsou náhradou obecných důkazů níže.

## 1. Body, mříž a duální mříž; úlohy1,2

Generátor má přechod s(x)=(ax+c) mod m. Předpokládáme buď plnou periodu m,
nebo prvočíselné m, c=0 a primitivní a; v druhém případě přidáváme nulový
stav. Mříž je množina všech celočíselných kombinací lineárně nezávislých
vektorů. Periodické rozšíření všech t-tic generátoru je L=V0+Lambda, kde

```
V0 = (c/m)(0,1,1+a,...,1+a+...+a^(t-2)),
V1 = (1/m)(1,a,...,a^(t-1)),  Vj=e_j pro j>=2.
```

Zde e_j je j-tý souřadnicový vektor. Determinant báze Lambda je1/m.
První souřadnice určuje stav modulo m, ostatní souřadnice se nezávisle
upraví o celé číslo; průnik s [0,1)^t proto obsahuje právě všech m stavů.

Duální mříž Lambda* obsahuje vektory U, jejichž skalární součin s každým
prvkem Lambda je celé číslo. Explicitně to jsou právě celočíselné vektory

```
u1+a*u2+...+a^(t-1)*ut = 0 (mod m).                  (D)
```

Báze je (m,0,...,0) a (-a^(j-1),e_j), j>=2. Pro obecnou bázi V_i
určují duální bázi U_i rovnosti U_i.V_j=delta_ij, kde delta_ij je1 pro i=j
a0 jinak. Roviny U.X=rho+q, q celé, s rho=U.V0 mají rozestup1/||U||.
Naopak libovolná rovnoměrná rodina rovin pokrývající celou mříž po vhodném
škálování normály dává prvek Lambda*. Maximální rozestup je tedy1/nu_t,
kde nu_t je délka nejkratšího nenulového vektoru Lambda*. Toto tvrzení
se týká periodické mříže, nikoli libovolného pokrytí konečné množiny bodů.

Píšeme f(x)=||sum x_i U_i||^2. Je-li Y=sum x_i U_i, pak x_k=Y.V_k.
Cauchyho nerovnost dává x_k^2<=f(x)||V_k||^2 (Lemma A). V každé kouli
je tedy jen konečně mnoho celočíselných souřadnic x; kladné minimum existuje.
Pro t=1 je nu_1=m. Normalizovaný objem mu_t je objem koule poloměru nu_t
dělený m, tedy mu_t=pi^(t/2)*nu_t^t/(Gamma(1+t/2)*m); mu_1=2.

## 2. Redukce bází; úlohy7,12,13

Pro pevné j měníme V_i na V_i-q_i V_j pro i!=j, V_j neměníme.
Současně měníme U_j na U_j+sum_(i!=j) q_i U_i. Přímé vynásobení
zachovává dualitu. Celočíselná q dávají celočíselnou invertibilní změnu
báze s determinantem1; tedy stejnou mříž. Souřadnice se mění na
x_i'=x_i-q_i*x_j pro i!=j a x_j'=x_j.

Pro reálná q minimalizuje ||V_i-q_i V_j||^2 jednoznačně
q_i=(V_i.V_j)/||V_j||^2. Po změně je V_i kolmé na V_j pro všechna i!=j.
Z duality plyne ekvivalence této podmínky s U_j kolmým na ostatní U_i:
rozepišme U_j=sum alpha_i V_i; alpha_k=U_j.U_k, takže při kolmosti
U_j=alpha_j V_j a alpha_j!=0. Obráceně prohodíme U,V. Tudíž stejná q
minimalizují ||U_j+sum q_i U_i||^2. Jeho gradient má k-tou složku
2(U_j+sum q_i U_i).U_k a Hessova matice je dvojnásobek Gramovy matice
nezávislých ostatních U_i, tedy kladně definitní. Minimum existuje a je
jediné; nejde jen o nutnou podmínku stacionarity.

Celočíselná q vybíráme zaokrouhlením na nejbližší celé číslo. Podmínka
2|V_i.V_j|>||V_j||^2 zaručuje přísné zkrácení V_i. U_j se přechodně
prodloužit smí; uchovává se nejlepší již nalezená hodnota. Celý proces
končí: každý V_i leží v původní diskrétní mříži, jeho délka neroste a
součet čtverců délek při každé netriviální operaci přísně klesá v konečné
množině dostupných bází. Rovnost nesmí spouštět operaci; úloha19 následuje.

Úloha13: pro iracionální alpha vezměme U=((1,0),(alpha,0)), tedy
f(x,y)=(x+alpha*y)^2. Na nenulových celočíselných dvojicích je f>0.
Rozdělením N+1 zlomkových částí 0,alpha,...,N*alpha do N intervalů
délky1/N získáme nenulovou dvojici s |x+alpha*y|<1/N; minimum neexistuje.
**C0040:** odkaz na kvadratickou formu (19) ve zadání má být (17).

## 3. Dvě dimenze a algoritmus S; úlohy4,5,14

Jsou-li dva celočíselné řádky u,v řešení (D) a det(u,v)=m, tvoří bázi
všech řešení: inverzní matice má jmenovatel m a pro jiné řešení y jsou
oba čitatelé Cramerova pravidla dělitelné m díky (D). Označme
A=||u||^2, B=||v||^2, C=u.v. Pokud 2|C|<=A<=B, pak

```
||x*u+y*v||^2 >= A*(x^2+y^2-|xy|) >= A
```

pro každou nenulovou celočíselnou dvojici. To je redukční kritérium úlohy4.

V S2 platí h-a*p=hp-a*pp=0 mod m, |h*pp-hp*p|=m, h>0,
p*pp<=0, |pp|<=|p| a ||(hp+h,pp+p)||^2>=s=h^2+p^2.
Po úspěšném kroku h přísně klesá. Nemůže klesnout na0: při gcd(a,m)=1
by nulový zbytek měl |p|=m a normu aspoň dosavadní s.

Nejlepší celočíselný násobek q' pro zkrácení (hp,pp) vektorem (h,p)
je round((hp*h+pp*p)/s). Pokud výsledná norma klesne pod s, q' není0
(předchozí vektor nebyl kratší) ani -1 (poslední invariant). Pro každé
jiné celé q' je |pp-q'*p|>=|p|. Proto |hp-q'*h|<h, čili
q' je q=floor(hp/h) nebo q+1. S2 testuje q. Pro u=hp-q*h,
v=pp-q*p máme h*u+p*v>=-s/2, neboť q<=q' a zaokrouhlená projekce
má zbytek skalárního součinu v [-s/2,s/2]. Pokud u^2+v^2<s,
z toho plyne zachování invariantu pro součet nové a předchozí dvojice.

Když q selže, ale q+1 uspěje, je
2|(h,p).(u-h,v-p)| <= ||(u-h,v-p)||^2 <= s:
skalární součin je záporný, neboť h-u>0 a p*(p-v)>0, a jeho dvojnásobná
absolutní hodnota je ||(u-h,v-p)||^2+s-||(u,v)||^2.
Úloha4 pak potvrzuje nové minimum. Když selžou obě možnosti, nejbližší
projekce q' dává druhý řádek normy aspoň s a skalární součin nejvýše s/2;
opět platí úloha4. Tím jsou S1–S3 správné pro všechna přípustná a,m.

S4 připojí novou souřadnici a řádek (-a^(t-1),0,...,0,1), zachová
determinant m a (škálovanou) dualitu U*V^T=mI; celočíselné úpravy nové
souřadnice jsou stejné změny báze jako výše. S5–S6 končí podle oddílu2.
S7 používá Lemma A se škálováním1/m: |x_j|<=floor(sqrt(s||V_j||^2)/m).
S8–S10 projdou jednu z dvojic x,-x ve vymezeném celočíselném kvádru,
bez nulového vektoru. Kvadr obsahuje všechny minimalizátory, a proto
algoritmus vrací přesné minimum, i když samotné zkracování je jen heuristika.

`spectral.py` přepisuje všechny kroky doslova a kontroluje dualitu i pokles.
Nezávislý řešič `shortest_direct` prochází kouli v původních souřadnicích
u2,...,ut a dopočte všechny přípustné u1 z kongruence (D); nepřebírá
redukovanou bázi ani kvádr. Srovnáno1103 modelů,5515 minim v dimenzích2–6;
v dimenzích3–6 i úplné množiny minimalizátorů. Ruční příklad úlohy14
souhlasí včetně tří eukleidovských kroků, všech čtyř transformací a obou
vytištěných matic. Výsledek je nu_2^2=50, nu_3^2=6, z=(0,0,1).

## 4. Potence2; úloha3 a C0036

Potence2 znamená b=a-1!=0 mod m a b^2=0 mod m. Potom a^j=1+j*b mod m,
takže vektory (1,-2,1) a (1,-1,-1,1) dávají obecné horní meze6 a4.
Pro d=gcd(b,m) je m dělitelem d^2. Plná perioda dále vyžaduje, aby každý
prvočinitel m dělil b a aby4 dělilo b, pokud4 dělí m. Z toho d>=4,
s jedinou výjimkou m=9,d=3. Každý krátký vektor musí mít součet složek
dělitelný d. Při normě^2<6 v dimenzi3 je absolutní součet složek nejvýše3;
pro d>=4 proto musí být součet0. Jediné možnosti jsou normy2, s vektorem
e_i-e_j. Podmínka (D) pak vyžaduje b=m/2 a rozdíl indexů2, tedy

```
m=8q, a=4q+1 (q>=1): nu_3^2=nu_4^2=2.
```

V dimenzi4 a při normě^2<4 přibývá rozdíl indexů3, který dává
m=9q, a=3q+1 nebo6q+1, nu_4^2=2. Vektory s normou3 mají lichý
součet; jediná možná výjimka d=3 již patří k m=9. Pro m=9,a=4,7
není norma2 ani3 v dimenzi3 možná a norma4 by byla jediná složka±2;
normu5 dávají (1,2,0), respektive (2,1,0). Jinde platí původní hodnoty6,4.

Původní odpověď577 má v binární výjimce nesmyslné sudé a, chybí1+.
Erratum4.7.2003 však přepisuje poslední tři řádky a uvádí pouze ternární
výjimky; **binární rodinu úplně vynechává**. C0036 proto hlásí problém
i po této opravě, nikoli samostatně již přepsaný překlep. Nejmenší příklad
m=8,a=5,c=1 má orbitu 0,1,6,7,4,5,2,3. Vektor (1,0,-1) má normu^2=2,
jednotkový vektor nikdy nesplní(D). Úplný soupis650 modelů m<=512
potvrdil klasifikaci a64 chybějících binárních případů.

## 5. Neplatná mez řetězového zlomku; úloha6 a C0037

Nechť A je největší podíl Eukleidova algoritmu pro m,a. Původní mez je
mu_2>2*pi/(A+1+1/A). Pro prvočíslo m=131 a primitivní a=97 jsou
podíly (1,2,1,5,1,4), A=5. Primitivitu dokládají
a^65=130, a^26=89, a^10=80 mod131. Vektor (5,4) splňuje(D), takže

```
mu_2 <= 41*pi/131 < 10*pi/31 = 2*pi/(5+1+1/5).
```

Jde o přesný protipříklad uvnitř předpokladů sekce. Nezávislé minimum
je41. Plně periodický smíšený příklad je m=405,a=151,c=1, nu_2^2=113,
A=6. Chyba odpovědi578 je v odhadu sousedních podílů: při a_j=5 je
m/(r_j*p_(j-1))=131/20=6.55, nikoli méně než5+1+1/5=6.2.

Platná slabší oprava je **mu_2>2*pi/(A+2)**. Minimum v dimenzi2 je
nejmenší hodnota r_j^2+p_(j-1)^2 mezi zbytky a jmenovateli běžných
konvergentů: pokud S3 zlepší výsledek krokem q+1, z nerovností
(v-p)^2>v^2 a (u-h)^2<u^2 plyne u>h/2, takže další běžný podíl je1
a tento vektor se mezi konvergenty vyskytne. Identita determinantů dává

```
m/(r_j*p_(j-1))
  = a_j+p_(j-2)/p_(j-1)+r_(j+1)/r_j < A+2.
```

Předposlední podíl je nejvýše1, poslední je menší než1 (na krajích mohou být0), a proto
m<(A+2)*r_j*p_(j-1)<=(A+2)*(r_j^2+p_(j-1)^2)/2.
Po vynásobení pi/m dostáváme opravu. Konečný test ji ověřil na všech
1103 modelech; původní mez selhala v8 z nich. První běh skončil právě
na její chybném tvrzení; druhý zaznamenává výjimky a kontroluje opravu.

## 6. Hermite a komplementární vektor; úlohy9,10

Označme theta nejmenší hodnotu f na nenulových celočíselných vektorech.
Minimalizátor má nesoudělné souřadnice, jinak jej vydělíme jejich společným
dělitelem. Eukleidovými operacemi jej doplníme na celočíselnou matici
determinantu1. Touto změnou báze a ortogonální změnou souřadnic získáme

```
f(x)=theta*(x1+beta2*x2+...+betat*xt)^2+h(x2,...,xt),
```

kde h je kladně definitní a determinant její kořenové matice je
|det U|/sqrt(theta). Indukční minimum h je nejvýše
(4/3)^((t-2)/2)*|det U|^(2/(t-1))*theta^(-1/(t-1)).
Zvolíme nejbližší celé x1, první člen je nejvýše theta/4.
Z theta<=theta/4+h plyne
theta<=(4/3)^((t-1)/2)*|det U|^(2/t). Základ t=1 je rovnost;
v t=2 dosahuje rovnosti hexagonální báze (1,0),(1/2,sqrt(3)/2).

**C0039:** poznámka na579 formuluje Minkowského větu pro libovolnou
symetrickou konvexní množinu objemu>=2^t. Otevřená krychle (-1,1)^t
má přesně tento objem a obsahuje z celých bodů pouze nulu. Je nutno
požadovat objem>2^t nebo uzavřenost. Pro přísnou nerovnost důkaz plyne
ze dvou bodů polovičního tělesa se stejnou zlomkovou částí; jejich rozdíl
je nenulový celočíselný bod v původním symetrickém konvexním tělese.
Hermitova mez pro mu_t je H_t=pi^(t/2)*(4/3)^(t*(t-1)/4)/Gamma(1+t/2).
Pro t=9,10 dává pi>3.14 a sqrt(4/3)>1.154 hodnoty H_t/2^t>1.140
a>1.607. Poměr (H_(t+2)/2^(t+2))/(H_t/2^t) je
pi*(4/3)^(t+1/2)/(2*(t+2)); od t=9 je větší než1 a roste.
Tedy Minkowského mez je silnější pro všechna t>=9, jak kniha uvádí.
Mez mu_t<=2^t zůstává správná: použijeme větší koule a přejdeme k limitě,
v pevné ohraničené oblasti je jen konečně mnoho mřížových bodů.

Úloha10: primitivní y=(y1,y2) splňující(D) má gcd(y2,m)=1, neboť společný
prvočinitel by dělil také y1. Bézout dává u s det(u,y)=m. Přičtením
celého násobku y zaručíme 2|u.y|<=||y||^2; invertibilita y2 modulo m
z determinantové rovnice dává také(D) pro u. Položme
alpha=|u.y|/m, beta=||u||^2/m, gamma=||y||^2/m. Pak alpha<=gamma/2,
beta*gamma=1+alpha^2 a gamma<2/sqrt(3). Kdyby alpha>beta/2, vyšlo by
2*alpha*gamma>1+alpha^2, a proto gamma>1 a
alpha>gamma-sqrt(gamma^2-1)>gamma/2; poslední nerovnost plyne z
gamma<2/sqrt(3). Spor. Obě normy tedy splňují kritérium úlohy4
(v odpovídajícím pořadí) a jejich součin je aspoň m^2.

## 7. Počet rovin; úloha15 a C0038

Nechť M je součet záporných složek U, P součet kladných a rho=U.V0.
Obraz [0,1)^t při X -> U.X je interval s krajními hodnotami M,P.
Dolní konec se zahrnuje právě při M=0, horní právě při P=0. U smíšených
znamének jsou oba konce otevřené. Počet hladin rho+q, q celé, je proto

```
sum |u_j| - [U má obě znaménka a rho je celé].
```

Pro L0 (rho=0) je odpověď knihy správná. Tvrzení v hranaté poznámce,
že se počet při změně c nemění, je nepravdivé: pro m=4,a=1,U=(1,-1)
má L0 jen hladinu0 uvnitř čtverce, ale při c=1 má L hladiny -1/4,3/4,
obě skutečně obsazené. Rozestup rovin a samotné nu_t se nemění.

Obsazené roviny je třeba rozlišit od všech protínajících krychli.
I mezi plně periodickými c se počet obsazených rovin může měnit:
m=256,a=137,U=(18,-2) dává19 při c=1 a20 při c=187. Původní tři
počty20,21,24 v obr.8 pro c=187 souhlasí. Ověřeno15600 přesných
intervalových případů a odděleně konkrétní hladiny všech bodů.

## 8. Evidence a rozsah

`results/spectral-foundations.json` má čtyři úspěšné checkpointy:
1103/5515 modelů/minim,650 modelů potence2,15600 intervalů a48 přesných
racionálních kontrol redukcí v dimenzích2–5. Výpočty používají celá čísla
a zlomky. Úspěšné bloky se neopakují při `--resume`.

Pro C0036–40 byly prohledány `all2-prepre`, `all2-pre`, `all2`, `err2`
i aktuální `sources/err2.textxt`, podle stránek i matematických výrazů.
C0036 vyžaduje výše popsané zohlednění opravy2003; doklad její sazby je
`images/all2-prepre-p32.png`. Oprava2012 na579 mění bibliografické číslo
svazku5 na13, nikoli C0039. Opravy úlohy8 a pozdějších úloh nezaměňujeme
za opravy zdejších tvrzení. Žádná nalezená položka neopravuje C0037–40.
Nejnovější fyzický dotisk, prvenství a odměna nejsou ověřeny; drafty nejsou
odeslány. Historické atribuce a obecné hodnoticí výroky se prověřují dále.
