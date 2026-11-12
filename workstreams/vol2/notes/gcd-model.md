# §4.5.2: spojitý model, úlohy 23–29

Rozsah: definice (35)–(40), vztahy (44)–(46), (54)–(58), úlohy
23–29 a odpovědi 643–644. Originály 348–352,355,643–644 zobrazeny;
odpovědi 25/26/29 také ve zvětšení. Toto není uzavření celého textu
oddílu ani úloh 30–34. Čtyři vrstvy errat prohledány 2026-11-02.
Známé opravy: obor (36) je 0<x<=1; v (58) a odpovědi 27 je po
změně konvence Bernoulliho čísel nutný faktor (-1)^k.

## Model a úlohy 23/24

X=min(u,v)/max(u,v) je poměr neuspořádaných kladných operandů.
G_n(x)=Pr(X>=x) je jeho ocasová distribuční funkce po n cyklech
v Brentově spojitém modelu. Model bere počet posunů k nezávisle
s pravděpodobností 2^-k, k>=1. Není to přesný model konečné
množiny celočíselných vstupů; zejména zde nejsou atomy v rovnosti.

Pro pevné k další poměr je

```text
X' = min(2^k X/(1-X), (1-X)/(2^k X)).
X'>=x <=> x/(2^k+x) <= X <= 1/(1+2^k x),  0<x<=1.
```

Součet pravděpodobností těchto intervalů dává přesně (35), s
G_0(x)=1-x. Pokud existuje limit G, jeho rovnice je (36).
Definujme pro x>0

```text
S(x)=sum_{k>=1}2^-k G(1/(1+2^k x)).
G(x)=S(1/x)-S(x).
```

Druhá rovnost je pro 0<x<=1 pevná rovnice; pro x>1 definuje
pokračování G(x)=-G(1/x). Koncové hodnoty jsou G(0)=1,G(1)=0,
S(0)=0,S(+infinity)=1. Přeskupení je dovolené absolutní konvergencí.

Symetrie označení u,v dává pro x<=1
Pr(v/u<=x)=(1-G_n(x))/2. Pro x>=1 je pravděpodobnost
1/2+G_n(1/x)/2, tedy stejný vzorec po reciprokém pokračování.
Tím je 23 vyřešena v deklarovaném modelu. U 24, začínáme-li u>v,
nastane výměna pořadí právě při X>1/(1+2^k). Odpověď je proto
S(1). Uložený nezávislý výpočet dává 0.54325829588674532007;
tištěné zaokrouhlení 0.5432582959 souhlasí.

## Úloha 25: lokální rozvoje a Stirlingova čísla

Pišme rho(t)=G(1+t)=sum_{n>=1}rho_n t^n a lambda=-rho_1.
Funkce H(y)=G(exp(-y)) je lichá díky G(x)=-G(1/x).
Analyticita zde znamená lokální analytický rozvoj u každého reálného
y, nikoli celou funkci komplexní proměnné. Je důsledkem holomorfního
pokračování hustoty do pravé poloroviny v Morrisově větě 2, jehož
překlad a samostatný audit zadání 34 ještě navazují. Pro algebraický
závěr stačí lokální analytický rozvoj u y=0.

Označme H(y)=sum lambda_n y^n; sudé koeficienty jsou nulové.
Dosazení y=-ln(1+t) a t=exp(-y)-1 dává

```text
(-1)^n rho_n = sum_k [n k] (k!/n!) lambda_k,
lambda_n = -sum_k {n k} (k!/n!) rho_k.
```

[n k] je neznaménkové Stirlingovo číslo prvního druhu, počet permutací
n prvků s k cykly; {n k} je číslo druhého druhu, počet rozkladů n prvků
do k neprázdných bloků. Jejich exponenciální vytvářející funkce jsou
(-ln(1-z))^k/k! a (exp(z)-1)^k/k!. V druhé rovnosti syrové dosazení
dává faktor (-1)^n; zápis s minusem je přesto správný: pro sudá n
je celá pravá strana nulová. První vztahy jsou

```text
-rho_1=lambda, rho_2=lambda/2,
-rho_3=lambda/3+lambda_3,
rho_4=lambda/4+(3/2)lambda_3,
-rho_5=lambda/5+(7/4)lambda_3+lambda_5.
```

Tištěné čtyři desetimístné aproximace lambda_1,lambda_3,lambda_5,
lambda_7 odpovídají výpočtu níže. Domněnka o poměrech následujících
koeficientů tím dokázána není; její novější zadání patří do 31.

## Úloha 26 a C0124

Oddělení prvního členu S dává
`2S(x)=S(2x)-G(1+2x)`. Proto obě strany požadované identity jsou

```text
2S(1/x)-5S(1/(2x))+2S(1/(4x))-2S(x)+5S(2x)-2S(4x).
```

Obecná identita je správná. Poslední příklad odpovědi je chybný.
Pro zlatý řez phi=(1+sqrt(5))/2 platí phi²=phi+1, takže
1+2phi=phi³, 1+1/phi=phi, 1+1/(2phi)=phi²/2.
Po dosazení a odečtení 2G(phi) z obou stran musí být

```text
2G(4phi)-5G(2phi)+G(phi²/2)-G(phi³) = -2G(1+4phi).
```

Tištěná pravá strana je 2G(2phi²). Oba její argumenty i argument
opravené strany jsou >1. Brentovo G je pro x>1 záporné, neboť
G(x)=-G(1/x) a jeho hustota -G' je kladná na (0,1]. Tištěná
strana je tedy záporná, opravená kladná. Jde o přesný spor,
nikoli o nejistotu numerické aproximace. Viz C0124.

## Úloha 27: dvě nezávislé formule pro koeficienty

Psi je analytická funkce určená (55):
`psi(z)=(z+psi(z/2)+psi(z/(2+z)))/2`, psi(0)=0,psi'(0)=1.
Iterace dává absolutně konvergentní rozvoj v okolí nuly

```text
psi(z) = (z/2) sum_{j>=0}2^-j sum_{0<=a<2^j}1/(2^j+a z),
psi(z) = sum_{n>=1}(-1)^(n-1) psi_n z^n,
psi_n = (1/2) sum_{j>=0}2^(-j(n+1)) sum_{0<=a<2^j}a^(n-1).
```

Při n=1 užíváme 0^0=1; psi_1=1. Pro n>1 zmizí j=0.
Bernoulliho čísla B_k v současné konvenci jsou určena funkcí
t/(1-exp(-t)); B_1=+1/2. Ve Faulhaberově vzorci pro součet
od a=0 do M-1 tedy vstupují (-1)^k B_k:

```text
sum_{0<=a<M} a^(n-1) = (1/n) sum_{k=0}^{n-1} binom(n,k)(-1)^k B_k M^(n-k).
psi_n = (1/(2n))sum_{k=0}^{n-1}binom(n,k)(-1)^k B_k/(2^(k+1)-1)
        + [n=1]/2.
```

Použili jsme sum_{j>=1}2^(-j(k+1))=1/(2^(k+1)-1).
Naopak přímé porovnání koeficientů v (55) dává kladnou rekurenci

```text
psi_1=1,
psi_n=sum_{j=1}^{n-1}binom(n-1,j-1)psi_j / (2(2^n-1)), n>1.
```

Tato druhá metoda přesně ověřila všech prvních 64 koeficientů;
psi_2=1/6,psi_3=2/21. Rovnice (54), po záměně z=2x, má právě
řešení alpha(x)=(3/2)lambda psi(x): lineární člen splní rovnici
a zbývající koeficienty jsou určeny trojúhelníkově. Náhrada
Bernoulliho znaménka v erratu 2021 je správná.

## Úloha 28: rigorózní asymptotika a C0125

Pro n>=1 a celé m>=2 definujme
S_n(m)=sum_{k=1}^{m-1}(1-k/m)^n a T_n(m)=1/(exp(n/m)-1).
Z předchozího koeficientového součtu přesně plyne

```text
2psi_(n+1)=sum_{j>=1}4^-j S_n(2^j),
tau(n)=sum_{j>=1}4^-j T_n(2^j).
```

Při q=exp(-n/m) platí uniformně

```text
0 <= T_n(m)-S_n(m) <= (2n/m²) q(1+q)/(1-q)^3.                 (A)
```

Důkaz: pro t<=1/2 je
0<=exp(-nt)-(1-t)^n<=nt²exp(-nt), podle řady -ln(1-t).
Pro 1/2<t<1 platí stejná mez s faktorem 2, je-li n>=2.
Při n=1 rozdíl exp(-t)-1+t<=t²/2<=2t²exp(-t) pro 0<=t<=1.
Členy k>=m, chybějící v S, rovněž nepřesáhnou
2n(k/m)²exp(-nk/m). Sečtení k²q^k dává (A).

Po násobení m^-2 a položení t=n/m je pravá strana (A)
2n^-3 h(t), kde h(t)=t^4 exp(-t)(1+exp(-t))/(1-exp(-t))³.
Pro t<=1 je h(t)=O(t); pro t>=1 je h(t)=O(t^4 exp(-t)).
Součet h(n/2^j) je proto omezen absolutní konstantou, nezávisle
na n: malá t tvoří geometrickou řadu, velká t mají exponenciální
pokles po dyadických bodech. Dostáváme
`2psi_(n+1)=tau(n)+O(n^-3)` s řádně uniformní chybou.

Tištěné O(exp(-n/m)n/m²) pro S-T bez jmenovatele není uniformní
v m. Pro pevné n a m->infinity je rozdíl asymptotický
m/(n(n+1)), zatímco uvedená mez jde k nule. Při následném součtu
přes j ji tedy nelze přímo použít. Tuto mezeru opravuje (A).
Samostatný nález C0125 níže má ještě přímočařejší přesný spor.

Pro reálné x>0 definujme oboustranný součet

```text
Q(log2 x)=x² sum_{j in Z}4^-j/(exp(x/2^j)-1),
R(x)=sum_{r>=0}4^r/(exp(2^r x)-1).
tau(x)=x^-2 Q(log2 x)-R(x).                                 (B)
```

Q je kladná spojitá funkce periody 1. Na kompaktní periodě má
kladné minimum a konečné maximum; R(x)=O(exp(-x)) při x->infinity.
Z toho tau(n)=Theta(n^-2), a tedy i psi_n=Theta(n^-2).
Fourierovy koeficienty Q se získají integrací periodizovaného
součtu. Substituce u=2^t dává

```text
c_k=Gamma(2+2pi i k/ln2) zeta(2+2pi i k/ln2)/ln2,
Q(t)=pi²/(6ln2)+2 Re sum_{k>=1} c_k exp(-2pi i k t).
```

Gamma je Eulerův gama integrál, zeta Riemannova funkce; identita
integral_0^infinity u^(s-1)/(exp(u)-1)du=Gamma(s)zeta(s) pro
Re(s)>1 plyne rozvojem geometrické řady a Tonelliho/Fubiniho větou.
Fourierova řada konverguje absolutně díky exponenciálnímu poklesu
Gamma na svislici. Toto je přesně periodický člen v odpovědi.

Odpověď 28 však tvrdí, že její Mellinův integrál (rovný tau(n))
**je** součtem těchto reziduí, bez členu -R(n). Přesnou rovnost
vylučuje i její vlastní vztah

```text
4tau(2n)-tau(n)=1/(exp(n)-1)>0,
4(2n)^-2 Q(log2(2n))-n^-2 Q(log2 n)=0.
```

V (B) je chybějící člen výslovný a kladný před odečtením.
Hlavní asymptotika i periodický člen zůstávají správné.

## Úloha 29: Mellinův rozvoj první iterace

Označme f(x)=sum_{k>=1}2^-k/(1+2^k x), x>0. Pro G_0=1-x
je S_1=1-f a G_1(x)=f(x)-f(1/x). Mellinova transformace, tj.
integrál f(x)x^(s-1) přes kladnou osu, je

```text
f*(s)=pi/((2^(s+1)-1)sin(pi s)), 0<Re(s)<1.
```

Transformace 1/(1+x) je pi/sin(pi s); substituce v každém členu
f a absolutní konvergence ospravedlňují geometrický součet.
Posun inverzní kontury doleva při 0<x<1 dává:
reziduum 1 v s=0, dvojpól s=-1 s příspěvkem x log2 x+x/2,
a dvojice pólů -1+2pi i m/ln2 dávající **plus** xP(log2 x), kde

```text
P(t)=(2pi/ln2)sum_{m>=1} sin(2pi m t)/sinh(2m pi²/ln2).
```

Reziduum v s=-n, n>=2, je
(-1)^(n+1)2^(n-1)x^n/(2^(n-1)-1). Kontury lze vést mezi
celočíselnými reálnými póly a mezi výškami imaginární mřížky;
faktor 1/sin(pi s) dává exponenciální pokles ve výšce a x^N
zabije levý zbytek. Rozvoj je proto skutečnou konvergentní
rovností pro 0<x<1, na rozdíl od nesprávného zavření kontury
doprava u Gamma v úloze 28.

Definujme Phi(x)=sum_{j>=1}1/(2^j+x). Pro |x|<2 je též
sum_{k>=0}(-1)^k x^k/(2^(k+1)-1); první definice pokračuje
funkci na celou kladnou osu. Termínově f(1/x)=1-Phi(x), takže

```text
G_1(x)=x log2 x+x/2+xP(log2 x)-x²/(1+x)+(1-x²)Phi(x).
```

Identita pokračuje na x>0 reálnou analyticitou. Při
c=2pi²/ln2 dostáváme přímou geometrickou majorantu

```text
|P(t)| <= (4pi/ln2) exp(-c)/((1-exp(-c))(1-exp(-2c))) < 8e-12.
```

Originál na644 má v obou místech **plus** xP; podezření vyvolané
malým zobrazením bylo vyvráceno zvětšením a reziduovým výpočtem.

## Reprodukovatelnost a limity numeriky

`compute_gcd_distribution.py` implementuje lokální interpolaci stupně15
na rovnoměrné mřížce z=sqrt(-ln x), s G(exp(-z²)). Obě mřížky
2048/4096, z_max=8, 80 členů operátoru,45 iterací skončily úspěšně.
Jedná se o 63bitovou mantisu `longdouble`, nikoli o čtyřnásobnou
přesnost. Zbytek iterací klesl na přibližně 3e-19. Sedm extrapolací
lichoběžníkové kvadratury dává b=2.8329765709909285041 a
2/b=0.7059712461019163915. Zde b je očekávaný pokles log2(uv):

```text
b=2+(1/ln2) integral_0^1 G(x)/(1-x) dx
 =2+(1/ln2) integral_0^infinity 2z G(exp(-z²))/(exp(z²)-1) dz.
```

První rovnost plyne z poklesu k-log2(1-X), E[k]=2, a integrace
ocasové pravděpodobnosti. Koeficienty H(y)/y jsme získali zvlášť
polynomickým fitováním v y²; oba výsledky souhlasí s tištěným
zaokrouhlením. Hraniční podíl G(exp(-h²))/h² trpí odečítáním,
takže na jemnější mřížce nemusí být přesnější; tento horší výsledek
byl zachován v diagnostice a nenahrazen potichu.

Brentův původní report1999, v arXiv verzi2013, str.12–13 byl
vizuálně přečten. Popisuje obdobnou metodu a tiskne40 číslic;
naše výpočty potvrzují pouze odpovídající nižší přesnost, nikoli
rigorózní certifikát všech těchto číslic. Dvě mřížky jsou kontrola
konvergence jedné metody, nejsou dvě nezávislé metody.

`verify_gcd_model.py --resume` má pět úspěšných checkpointů:
přesné algebraické identity a4896 intervalových případů,64 přesných
koeficientů psi, kontrolu již uložených mřížek,8 hodnot G_1 při
80místné aritmetice a6 kontrol opraveného Mellinova vztahu plus30
kontrol uniformní meze. Běh82569 exit0; původní mřížky nebyly opakovány.
Číselné kontroly doplňují výše uvedené obecné důkazy a nenahrazují je.

Úlohy23/24/25/29 jsou checked,26 a28 confirmed podle C0124/C0125,
27 known_erratum. Poslední fyzický dotisk a priorita nálezů neověřeny;
návrhy hlášení neodeslány.
