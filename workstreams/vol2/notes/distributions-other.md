# §3.4.1 D/E: exponenciální a další spojitá rozdělení

Stav 1. listopadu 2026. Původní strany 132–136, 140, 586–587
vizuálně přečteny. Matematický blok D/E a úloha 16 jsou uzavřeny;
historické zdroje mimo níže vymezený rozsah budou zahrnuty do kontextového
bloku celé sekce. Numerické doklady: `verify_distributions_other.py`
a `results/distributions-other.json`. Žádný nový nález v tomto bloku.

## 1. Exponenciální zákon a algoritmus S

Exponenciální veličina s průměrem mu>0 má pravděpodobnost překročení x
rovnou exp(−x/mu), x>=0. Transformace −mu*ln U má tuto vlastnost,
protože Pr(U<exp(−x/mu))=exp(−x/mu). Dosazení za přesnou nulu je
implementační aproximace výslovně uvedená v textu, nikoli tvrzení
přesné spojité distribuce na konečné množině vstupů.

Pro S položme L=ln 2 a oddělme celočíselnou část J, počet jedniček
před první nulou. V ideálním nezávislém bitovém proudu
Pr(J=j)=2^(−j−1); zbylý zlomek U je rovnoměrný a nezávislý na J.
Tabulka Q má přírůstky p_k=L^k/k!, k>=1, a jejich součet je1.
Minimální hodnota k nezávislých uniformních veličin má hustotu
k(1−v)^(k−1), 0<v<1. Směs Z=L*min(U1,...,Uk) tedy má hustotu

```
sum_(k>=1) p_k*k/L*(1−z/L)^(k−1) = exp(L−z) = 2exp(−z),
                                                 0<z<L.       (1)
```

Větvi k=1 odpovídá původní U<L. Podmíněně je U/L rovnoměrné,
proto lze vrátit přímo Z=U a žádné další číslo negenerovat.
Po spojení s J má J*L+Z hustotu 2^(−j−1)*2exp(−z)=exp(−jL−z).
S4 a škálování mu jsou tedy správné. Střední počet dalších celých
uniformních vstupů je sum_(k>=2)k*p_k=L; včetně prvního jde o1+ln2.
Průměr odstraněných bitů v ideálním proudu je E(J+1)=2.

Pro konečný (t+1)-bitový zlomek je přirozená implementace doplněna
nulami: pokud jsou všechny uvedené bity1, první další bit je0 a zbytek
je0. Stejnou konvenci algoritmus F uvádí explicitně. Toto upřesnění
není zařazeno jako nový nález. Konečná přesnost samozřejmě dává
atomy a konečný ocas. Po alespoň jednom posunu je U<=1−2^(−t),
proto uvedená délka tabulky Q zaručuje ukončení S3. Certifikované
minimální délky jsou uloženy pro t=8,16,24,32,53,64,128.

## 2. Gamma rozdělení a odmítací algoritmus A

Gamma funkce je Gamma(a)=integral_0^infinity x^(a−1)exp(−x)dx,
a>0. Gamma rozdělení řádu a má tuto integrandovou hustotu dělenou
Gamma(a). Případy a=1 a a=1/2 odpovídají exponenciále a Z²/2
pro standardní normální Z, přímou substitucí.

Pro dva nezávislé gamma vstupy X,Y řádů a,b použijme souřadnice
R=X+Y a T=X/(X+Y); absolutní Jacobián je R. Společná hustota je

```
R^(a+b−1)exp(−R) * T^(a−1)(1−T)^(b−1) / (Gamma(a)Gamma(b)).
```

Integrace dává současně beta integrál
B(a,b)=Gamma(a)Gamma(b)/Gamma(a+b), gamma zákon součtu,
beta zákon poměru i jejich nezávislost. Součet celého počtu
exponenciál se proto může spočítat jako −ln součinu uniformních čísel;
upozornění na podtečení v textu je oprávněné.

Pro algoritmus A položme k=a−1>0 a b=sqrt(2k+1). Návrh Y=tan(pi U)
má Cauchyho hustotu 1/(pi(1+y²)); stejně funguje poměr souřadnic
rovnoměrného směru v rovině. X=k+bY. Pro X>0 je akceptační podíl

```
r(y)=(1+y²)*(1+by/k)^k*exp(−by).
(d/dy)ln r(y) = −y*(by−1)²/((1+y²)(k+by)).             (2)
```

Na definičním oboru y>−k/b tedy r roste k r(0)=1 a potom klesá.
Vynásobením návrhové hustoty a (2) dostaneme konstantu krát
x^k exp(−x); přijatý výstup má požadovaný gamma zákon. Počet pokusů
má průměr

```
C(k)=pi*sqrt(2k+1)*k^k*exp(−k)/Gamma(k+1).             (3)
```

Knižní mez C(k)<1.902 pro k>=2 není pouze vzorek hodnot. Zaveďme
psi(x)=(d/dx)ln Gamma(x). Integrální vyjádření rozdílu je

```
psi(k+1)−ln k
 = integral_0^infinity exp(−kt)*(1/t−1/(exp(t)−1))dt
 > 1/(2k)−1/(12k²).
```

Poslední krok plyne z coth z < 1/z+z/3 pro z>0. Po vynásobení
z*sinh z má rozdíl mocninné koeficienty
4n(n−1)/(3(2n+1)!), n>=2, všechny kladné. Proto
1/t−1/(exp(t)−1)>1/2−t/12. Integrální vyjádření psi plyne například
z její řady psi(k+1)=lim_N(ln N−sum_(j=1)^N 1/(k+j)).

Logaritmická derivace (3) je 1/(2k+1)+ln k−psi(k+1)<0 pro k>=2,
protože rozdíl dolní meze a 1/(2k+1) je
(4k−1)/(12k²(2k+1))>0. Nejvyšší hodnota je tedy při k=2:
2pi*sqrt5*exp(−2)=1.90141058262025..., certifikovaně pod1.902.

## 3. Malý gamma parametr: úloha 16

Pro 0<a<=1 jsou dvě větve obálky x^(a−1)/Gamma(a) na(0,1)
a exp(−x)/Gamma(a) na[1,infinity). Obálka převyšuje gamma hustotu,
protože exp(−x)<=1 v první části a x^(a−1)<=1 ve druhé.
Její integrál je c=(a+e)/(e*Gamma(a+1)). Normalizovaný návrh je směs
s pravděpodobností p=e/(a+e): v první větvi X=V^(1/a),
ve druhé X=1−ln V. Akceptační podíly jsou exp(−X) a X^(a−1).
Tím je G1–G3 doložen i na hranici a=1.

Původní U vybírající větev lze recyklovat. Podmíněně na U<p je U/p
uniformní, na U>=p je (U−p)/(1−p) uniformní, v obou případech
nezávisle na V. Proto jsou správné prahy p*exp(−X) a
p+(1−p)*X^(a−1). Při U<p/e přijímáme první větev bezpečně bez
exponenciály, protože X<1. Podíl 1/(a+e) se pohybuje od0.269 do0.368;
slovní přiblížení30 procent odpovídá tomuto rozsahu.

Mez c<1.4 byla certifikována intervaly pokrývajícími celé [0,1],
nikoli jen hodnotami v uzlech. Jde o200 intervalů délky1/200,
70cifernou outward intervalovou aritmetiku pro e a Gamma.
Numericky je jediné maximum poblíž a=0.79906875, c=1.38965704.
Jednoznačnost plyne z (ln c)''=−1/(a+e)²−psi'(1+a)<0;
numerická poloha maxima není potřebná pro intervalový důkaz meze.

## 4. Beta, chi-square, F a Studentovo t

Poměr gamma vstupů byl odvozen v §2. Jöhnkův další návrh používá
Y1=U1^(1/a), Y2=U2^(1/b). Hustota v jednotkovém čtverci je
ab*y1^(a−1)*y2^(b−1). Podmíněním na S=Y1+Y2<=1 a substitucí
T=Y1/S se hustota rozloží na S^(a+b−1) a
T^(a−1)(1−T)^(b−1). Poměr tedy opět má beta zákon;
pravděpodobnost přijetí je Gamma(a+1)Gamma(b+1)/Gamma(a+b+1).
Pro celočíselné parametry má a-tá nejmenší hodnota z a+b−1
uniformních vstupů beta(a,b); je to právě b-tá největší, jak říká text.
576 přesných momentových integrálů pro a,b=1..12 kontroluje pořadí
parametrů i normalizaci nezávislým rozvojem polynomů.

Chi-square s nu stupni volnosti je dvojnásobek gamma(nu/2).
Pro F rozdělení jsou A=nu1/2, B=nu2/2. Z beta vstupu T dostaneme
X=nu2*T/(nu1*(1−T)); inverze má derivaci
nu1*nu2/(nu2+nu1*x)². Dosazení beta hustoty dává přesně konstantu
i integrand rovnice(36). Ekvivalentní poměr nezávislých chi-square
vstupů proto také souhlasí.

Z=Y1/sqrt(Y2/nu), kde Y1 je standardní normální a Y2 nezávislé
chi-square(nu), má hustotu (37): podmíněnou normální hustotu násobíme
hustotou Y2 a integrujeme gamma integrálem. Pro alternativní
Studentovu metodu předpokládejme nu>2, k=nu−2. Vstup Y je normální,
E nezávislá exponenciála s průměrem2/k a z=Y²/k. Přijetí znamená

```
z<1 a E>−z−ln(1−z).
```

Pro |y|<sqrt(k) je pravděpodobnost přijetí
exp(k*z/2)*(1−z)^(k/2). Vynásobení normální hustotou zruší oba
exponenciální faktory; přijaté Y má hustotu úměrnou
(1−y²/k)^(k/2). Po známé opravě23.3.1999 je výstup

```
X=Y/sqrt((1−2/nu)*(1−z)) = sqrt(nu)*Y/sqrt(k−Y²).
```

Inverze y=sqrt(k)*x/sqrt(nu+x²) má derivaci
sqrt(k)*nu/(nu+x²)^(3/2). Výsledná hustota je úměrná
(1+x²/nu)^(-(nu+1)/2), tedy přesně (37). Původní faktor1−2nu
byl záporný; známá oprava problém úplně řeší.

## 5. Koule a normální aproximace gamma

Hustota n nezávislých normálních souřadnic závisí pouze na poloměru.
V polárních souřadnicích se proto rozloží na funkci poloměru krát
rovnoměrnou plošnou míru směru. Normalizace délky v(38) tak dává
rovnoměrný povrch; R=0 je nulová událost ideálního modelu. Násobení
nezávislým U^(1/n) dá objemové rozdělení, protože radiální CDF je r^n.
Terminologické opravy sphere→surface of ball z29.4.2014 jsou zahrnuty.

Ve třech rozměrech má rovnoměrný disk S=V1²+V2² uniformní na[0,1]
a nezávislý úhel. Z=2S−1 je uniformní na[−1,1], ostatní dvě souřadnice
mají čtverec poloměru4S(1−S)=1−Z². Plošný element jednotkové sféry
v souřadnicích (úhel,Z) je d(úhel)dZ, což potvrzuje uvedenou mapu.

Normální aproximace X≈a*W³ v textu je výslovně aproximace, není to
nepřesný odmítací test. Pro gamma X je
E((X/a)^r)=Gamma(a+r)/(Gamma(a)*a^r). Pro r=1/3 dává rozvoj
průměr1−1/(9a)+O(a^−2) a rozptyl1/(9a)+O(a^−2), v souladu s textem.
[Wilson a Hilferty1931](https://pmc.ncbi.nlm.nih.gov/articles/PMC1076144/)
byli přečteni na původních stranách686 a688: kubická transformace,
momentová motivace a výslovné omezení přibližné normality souhlasí.
Rok, strany a autoři jsou ověřeny v primárním archivu; celá jejich
číselná tabulka nebyla znovu auditována. Snímky i metadata uloženy.

Všechny čtyři řady errat byly prohledány podle stran133–142,586–590
včetně označení xPage, a hesel gamma/exponential/Student/1.902.
Další historické atribuce, výkonnostní srovnání závislá na dobových
počítačích a poznámka pod čarou k Marsagliově článku1977 pokračují
v kontextovém bloku; zde nejsou prohlášeny za nezávisle potvrzené.

[Sibuya1962](https://www.ism.ac.jp/editsec/aism/pdf/013_3_0231.pdf) byl
přečten celý vizuálně, str.231–237. §1–3 obsahují minimum a volbu ln2,
§4–5 související gamma/chi-square a polární konstrukce. Konkrétní
posunutý Cauchyho návrh algoritmu A zde uveden není; obecný knižní
odkaz tedy sám nepotvrzuje atribuci Ahrensovi. To není nový nález.
Původní obsah vydavatele zařazuje článek do13(3),1962, takže pozdější
metadata1961 nejsou důvodem opravovat knižní rok. Tabulky zdroje
nebyly nezávisle auditovány.
