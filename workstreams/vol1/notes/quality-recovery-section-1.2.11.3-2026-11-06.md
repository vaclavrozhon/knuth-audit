# §1.2.11.3 — všechny asymptotické výpočty a úlohy, 6. listopadu 2026

Přímo přečteny **celé původní116–123 a všechny odpovědi504–507**.
Nejde jen o20 čísel úloh: zahrnut každý hlavní výrok, všech26
hlavních rovnic, každá část14(a)–(e), všechny parametrické větve11
a všechny dodatky odpovědí. Původní checked nebylo přijato ze štítku.

Celé přečtené matematické důkazy:

- G: `asymptotic-gamma.md`, Taylor, neúplná gama, inverze,
  Theorem A, pohyblivé meze a Watsonovo lemma.
- P: `asymptotic-parameters.md`, obě přesné integrální reprezentace,
  všechny reálné větve, koeficienty a jednotnost pro x<0.
- S: `asymptotic-sums.md`, všech pět částí14, P a S se zbytky,
  konečné diference a Abelova rekurence.
- R: `ramanujan-bound.md`, celý konturový důkaz, každá konstanta,
  oba polynomy a všechny malé případy.
- F: `asymptotic-findings.md`, úplné argumenty C0016–C0019.

Přečteny také celé `asymptotic-calculations-scope.md`, příslušný
celý blok `sequential-asymptotics-2026-11-05.md`, oba programy,
uložené výsledky a všech devět pramenných revizí uvedených níže.
**Nové úplné doplnění** `quality-recovery-gaussian-real-powers-2026-11-06.md`
rozepisuje důkaz14(d) pro každý reálný exponent. Žádný checker
nebyl spuštěn; hashe čtyř matematických artefaktů jsou shodné
s původním manifestem úspěšného běhu.

## 1. Domény a každé hlavní tvrzení116–121

V definicích P,Q,R,S je n kladné celé a asymptotická limita jde
přes tato n. V neúplné gama funkci je a>0; pro x≥0 je mocnina
jednoznačná a u0 integrabilní. Záporné horní meze jsou výslovně
povoleny v9–10 jen s celočíselným exponentem, což je celé pokryto.
Ostatní parametry jsou pevné, není-li jednotnost dokázána zvlášť.

**(1)–(4),116–117.** Přepis konečných součinů přes faktoriály dává
přesně P=Σk0..n k^(n−k)k!/n!, Q=Σj1..n n_falling(j)/n^j a
R=Σj≥0 n!n^j/(n+j)!. U R je poměr sousedních členů n/(n+j+1)→0,
takže konverguje absolutně. Rozdělení exp(n) do indexů0..n−1
a n..∞ dává přesné Q+R=n!exp(n)/n^n. Stirling dává √(2πn)
pro součet; odhad každé poloviny je v tomto místě pouze výslovně
označeným odhadem, dokázaným později(25)–(26). P,Q,R mají nakonec
stejný hlavní člen, nikoli shodné konstantní členy.

**(5)–(9),117.** Taylorův integrální zbytek má základ n0 ze
základní věty integrálního počtu. Integrace po částech převádí
zbytek řádu n na člen f^(n+1)(0)x^(n+1)/(n+1)! plus zbytek
řádu n+1. Platí i orientovaně pro záporné x, když f má potřebné
derivace na celé úsečce. Identita Γ(a)=γ(a,∞) je celý již přijatý
Eulerův integrál. Exponenciální řada konverguje stejnoměrně
absolutně na konečném intervalu; faktor t^(a−1) je integrabilní.
To dává(7), včetně x0. Pro(8) lze přímo psát

`exp(x)γ(a,x)=x^a∫_0^1 exp(x(1−v))v^(a−1)dv`.

Rozvoj exponenciály a beta integrál dávají koeficient
1/[a(a+1)…(a+k)]. Ekvivalentní konvoluce(7) s exp(x) je
oprávněná absolutní konvergencí; její konečná binomická identita
je právě již dokázaná1.2.6–48. Dosazení a=x=n dává(9) se
správným (n−1)!, tedy podíl dvou kladných integrálů v[0,1].

**(10)–(12),117–118.** Rozdělení integrálu v x dává přesně
1−I1/Γ(x+1)+I2/Γ(x+1); pro pevné záporné y je x+y nakonec
kladné. V I1 jsou t=x(1+u), v=u−ln(1+u), u,v≥0. Derivace
v'=u/(1+u)>0 pro u>0 a v→∞ opravňují substituci i její
singulární, ale integrabilní počátek. Funkce
w(u)=u√(2(u−ln(1+u))/u²) má analytické odstranění singularity
a derivaci1 v0; analytická inverze proto existuje. Kladná větev
w=√(2v) je nyní výslovná i v erratech2024. Koeficienty jsou

```text
w = u−u²/3+7u³/36−73u⁴/540+1331u⁵/12960+O(u⁶),
u = w+w²/3+w³/36−w⁴/270+w⁵/4320+O(w⁶),
du/dv=1+1/u=1/w+2/3+w/12−2w²/135+w³/864+O(w⁴).
```

Poslední derivování je dovoleno analytickou řadou, nikoli
obecným pravidlem pro derivování libovolného O. Dosazení
w=√(2v) dává všech pět členů(12) včetně O(v²). Konečné
Lagrangeovy výpočty a zpětná kompozice v uloženém programu
nezávisle ověřují každý vytištěný koeficient.

**(13)–(15),118.** Na v≥r>0 je u(v)≥u(r)>0, proto
1+1/u(v)≤1+1/u(r) a ocas je nejvýše tato konstanta krát
exp(−rx). Limita výrazu je1, nikoli0: to je stávající C0016
v odpovědi4, nikoli chyba závěru. Substituce q=xv dává
∫x exp(−xv)v^αdv=Γ(α+1)x^−α pro α>−1. Rozdělíme integrál
v pevné malé r: lokální zbytek O(v²) integruje na O(x^−2),
ocasy konečně mnoha monomů jsou exponenciální. Tím skutečně
vznikne celý(15), ne dosazení lokální řady na celé poloose.
Konkrétně jsou koeficienty √(π/2),2/3,√(2π)/24,−4/135,
√(2π)/576 v řádech x^1/2,1,x^−1/2,x^−1,x^−3/2.

**(16)–(19),119.** V I2 substituce t=x+u dává integrand
exp(−u)(1+u/x)^x. Rozvoje logaritmu a exponenciály jsou
jednotné na **|u|≤|y|**, pro obě znaménka pevného y; základ
1+u/x je nakonec kladný. Integrál je
y−y³/(6x)+(y⁴/12+y⁵/40)/x²+O(x^−3). Předchozí úplný
reálný Stirlingův důkaz dává normalizaci(18), tedy
(2π)^−1/2(x^−1/2−x^−3/2/12+x^−5/2/288+O(x^−7/2)).
Součiny v1−I1/Γ+I2/Γ přesně ruší členy x^−1 a x^−2.
Výsledkem je celý Theorem A:

```text
γ(x+1,x+y)/Γ(x+1)
 = 1/2+(y−2/3)/√(2πx)
   +(23/270−y/12−y³/6)/(√(2π)x^(3/2))+O(x^−5/2).
```

Chyba I1 řádu x^−2 se násobí x^−1/2; tím je poslední
řád doložen. Odhady jsou jednotné na každé pevné kompaktní
množině y. Analytická inverze a Taylorovy zbytky do libovolného
pevného řádu dokazují i následující větu o pokračování rozvoje.
Samotné erratum0≤u≤|y| není důkazem záporného intervalu;
ten je pokryt uvedeným oboustranným odhadem.

**(20)–(23),119–120.** V konečném P má člen k0 hodnotu0
pro n≥1; před aplikací Stirlinga se tento člen vynechá.
Formule(20) se používá na k≥1. Její pravý zápis se spodní
mezí0 vyžaduje právě toto odstranění nulového členu, nikoli
samostatné dosazení1/(12·0) nebo O(0^−2). Původní funkce
členu má jednoznačné prodloužení0 a důkaz asymptotiky na
žádné silné nule proti divergentní sumě nezávisí.

Pro f(x)=x^(n+1/2)exp(−x) jsou f(0)=f'(0)=0 při n≥1,
f'(n)=f(n)/(2n). Eulerův vzorec řádu2 dává(21) s krajním
členem n^(n−1/2)exp(−n)/24. Znaménko R v knize je vlastní
označení zbytku, jeho absolutní mez se nemění. Jediná nula
f'' v(0,n) je r=n+1/2−√(n+1/2); derivace je před ní
kladná a za ní záporná. Proto
∫_0^n|f''|=2f'(r)−f'(0)−f'(n)=O(f(n)/√n).
Z f(r)/f(n)=O(1) a f'(r)/f(r)=O(n^−1/2) plyne
R=O(n^n exp(−n)), což dává(22). Opačné znaménko
kombinace uvnitř O v odpovědi5 je neškodné při absolutní
definici O; není novým protipříkladem.

Součet k^(n−1/2)exp(−k) se přesně rozdělí na případ n−1
a poslední člen. Pro pevné α,β rozvoj
(n+β)ln(1+α/n)=α+α(β−α/2)/n+O(n^−2) dává(23);
n+α je nakonec kladné. Tento hrubý Eulerův postup opravdu
stačí jen na první dva členy P. Vyšší členy dokazuje14 níže.

**(24)–(26),120.** S dokazuje pro C=√(π/2) a každé pevné α

```text
V_α(n)=Σ_(k=0)^n k^(n+α)e^−k /(n^(n+α)e^−n)
 = C√n−α−1/6+C(α²/2+α/2+1/12)n^−1/2
   +(−α³/3−α²/3+α/12+4/135)n^−1
   +C(α⁴/8+α³/12−α²/12−α/24+1/288)n^−3/2
   +O(n^−2).
```

Koeficienty vznikají z konečné rekurence A_j uvedené u14,
Gaussových momentů a Eulerových krajních členů. Stirlingovy
váhy V_(1/2)+V_(−1/2)/(12n)+V_(−3/2)/(288n²), násobené
1−1/(12n)+1/(288n²), dávají přesně všech pět členů P v(24).
Q+1=I1/(exp(−n)n^n) dává(25); odečtení od
√(2πn)(1+1/(12n)+1/(288n²)+O(n^−3)) dává(26).
Všechny tři zbytky jsou O(n^−2) s pevnými konstantami.
Proto se stejné hlavní členy, ale rozdílné konstanty
−2/3,−1/3,+1/3 vzájemně nevylučují. Hodnota
(11/24)√(π/2) leží mezi0.5744 a0.5745 podle již ověřených
racionálních mezíπ; nesouhlas s γ≈0.57721 je správnou
matematickou částí Knuthovy popsané vzpomínky.

**Další metody a tvrzení121.** Ramanujanovo substituování
t=x+u√(2x) dává lokálně exp(−u²) krát řadu polynomů v u
a x^−1/2. Ve zvětšujícím se okně u≤x^δ s dost malým δ
jsou Taylorovy zbytky jednotné; mimo ně klesá fáze
x(log(1+u√(2/x))−u√(2/x)) alespoň Gaussovsky, a vzdálený
ocas je exponenciální. To je platná alternativní metoda.
Integrace po částech aγ(a,x)=γ(a+1,x)+x^a exp(−x) dává
R(n)=1+exp(n)γ(n+1,n)/n^n; tedy stačí y0, bez I2.
Ramanujanova řada pro(R−Q)/2 má koeficient−16/8505,
jak opravuje známé erratum2000. Přijatý R odvozuje i další
členy, takže tento koeficient není pouhé převzetí citace.

Tvrzení, že diskrétní metoda14 může řešit i Q a R, má také
konkrétní argument. Člen Q je Πj0..k−1(1−j/n); jeho
logaritmus má hlavní část−k²/(2n)+k/(2n). Člen R je
Πj1..k(1+j/n)^−1, s hlavní částí−k²/(2n)−k/(2n).
V k≤n^(1/2+ε) mají oba libovolně dlouhé jednotné polynomiální
rozvoje pomocí konečných součtů mocnin. Ocas Q omezuje
exp(−k(k−1)/(2n)). Pro R a k≤n platí ln(1+j/n)≥j/(2n),
tedy Gaussův odhad; za n je každý další poměr≤1/2, takže
zbývající ocas je geometrický krát O(exp(−n/4)). Následuje
tentýž Eulerův výpočet Gaussových monomů. Není nutné
opakovat koeficienty již odvozené nezávislými integrály.
Odkazy na další svazky nejsou vydávány za audit jejich
celých kapitol; konkrétní metoda zde má vlastní důkaz.

## 2. Všechny úlohy1–12 a všechny větve odpovědí

**1–6.** Indukce Taylorova vzorce, obě gama řady, exponenciální
ocas, Eulerův zbytek a posunový rozvoj jsou plně dokázány v§1.
Pro1 je zahrnut n0, pro2–3 a>0 a integrabilita u0, pro4
r>0 a skutečná limita1. C0016 zůstává drobným původním
omylem zdůvodnění. Pro5 nejsou krajní derivace jen odhadnuty
grafem a pro6 není O-konstanta vydávána za jednotnou ve všech α,β.

**7.** Substituce u=x^1/4 v na pevné orientované úsečce0..y
dává exponent−v²x^−1/2/2+v³x^−5/4/3−v⁴x^−2/4+…
a jakobián x^1/4. Konečný Taylorův rozvoj má jednotný
zbytek; při integraci monomu u^a/x^b lze do O(x^−2)
zahrnout právě ty s4b−a≥9. Všech sedm nenulových členů
odpovědi505 je v G, shodných s originálem a nezávislou
koeficientovou rekurencí programu. Obě znaménka y, i y0,
jsou zahrnuta; nekonečná řada se zde neintegruje bez zbytku.

**8.** Pro |u|≤M x^r,0≤r<1, je nakonec |u|<x.
Položme g=u−xln(1+u/x) a h jeho Taylorův polynom po m.
Pro m≥2 jsou oba nezáporné: pro u<0 jsou všechny členy h
kladné, pro u>0 jde o alternující sumu klesajících velikostí.
Proto |exp(−g)−exp(−h)|≤|g−h|≤C|u|^(m+1)/x^m.
Integrace dává O(x^((m+2)r−m)); volba
m=ceil((s+2r)/(1−r)) zaručuje exponent≤−s. Pro m1 je
h0 a stejný důkaz začíná u²/x. Při m≤0 je Taylorův
součet prázdný a triviální mez O(x^r) postačí, protože
pak s≤−2r. Tím se nevsouvá nevyřčená podmínka s>0.

Původní odpověď integruje u^(m+1) symetricky bez absolutní
hodnoty. F dává platný protipříklad r0,s2,m2,f1: skutečný
rozdíl je kladný, tištěný integrál je0. To je C0017, nikoli
chyba výsledku úlohy. Tricomiho zvláštní případ r1/2,s0,m2
se po u=√(2x)t přesně redukuje na uvedený Gaussův integrál
s chybou O(1), i při záporné či oscilující f=O(√x).

**9.** p0 dává přesně0; p1 je Theorem A s y0. Pro pevné
p<1,p≠0 je t=px(1−u),v=−ln(1−u)−pu monotónní převod
0≤u<1 na0≤v<∞. Jakobián má lokální řadu
(1−p)^−1(1−v/(1−p)²+O(v²)) a jinde je omezený.
Watsonův argument dává přesně

```text
γ(x+1,px)/Γ(x+1)
 = p/(1−p) · (p exp(1−p))^x · exp(−x)x^x/Γ(x+1)
   ·(1−1/((p−1)²x)+O(x^−2)).
```

Pro p<0 je x celé a faktor p nese orientaci; velikost
nemusí klesat. Pro p>1 pracujeme s horním ocáskem přes
t=px(1+u),v=pu−ln(1+u); výsledkem je1 plus stejný výraz,
jehož hlavní prefaktor je záporný. Jen v této kladné větvi
platí0<p exp(1−p)<1. Známé x^z→x^x zachováno.
Jednotnost při p→1 nebyla tvrzena a neplyne z tohoto důkazu.

**10.** Pro p≠0,1 dosadíme t=px+pz/(p−1) a rozvineme na
pevné orientované úsečce0..y. Zbytek je jednotný pro obě
znaménka y. Integrály1 a z² proti exp(−z) dávají závorku
1−e^−y−e^−y(e^y−1−y−y²/2)/(x(p−1)²)+O(x^−2),
se správným prefaktorem p/(p−1)(p e^(1−p))^x e^−x x^x.
Pro p0 jsou oba původní integrály0 přímo. Celá odpověď505
souhlasí; zvláštní p1 je zadáním vyloučen.

**11: přesné identity a všechny reálné větve.** P dává

```text
Q_x=∫_0^∞ e^−t(1+xt/n)^(n−1)dt,
R_x=∫_0^n e^(xt)(1−t/n)^(n−1)dt,
xQ_x+R_(1/x)=n!(x/n)^n exp(n/x),             x≠0.
```

První integrand je polynom, druhá exponenciální řada má
absolutní konvergenci na konečném intervalu. Gama reprezentace
na505 jsou přímými substitucemi; pro x<0 je exponent celočíselný
a pro x0 jsou singularity odstranitelné, Q0=R0=1.
Pro pevné x<1 má R úplnou algebraickou asymptotiku; pro
0≤x<1 také Q. Pro x<0 má Q navíc **přesný** ocas
T_x=n!x^(n−1)exp(n/x)/n^n za bodem t=−n/x.
Zbytek Q_x−T_x=−R_(1/x)/x má uvedenou algebraickou řadu.
Pro x>1 reciproční identita dává obě větve s příslušnými
exponenciálními členy T_x a U_x=n!exp(nx)/(n^n x^n).

Existenci zbytků dokazuje rozdělení integrálů v n^δ,0<δ<1/2:
lokálně je chyba po m řádech majorována
C n^−m−1(1+t)^L exp(−ct); mimo lokální okno exponenciála
pohlcuje všechny mocniny. Koeficienty určuje přesná ODE
x∂R/∂x=n(1−(1−x)R), tedy a0=1/(1−x),
a_m=−x a'_(m−1)/(1−x). Její porovnání koeficientů lze
oprávnit také derivováním integrálního důkazu v pevném
kompaktním podintervalu x<1, které jen přidá faktor t
do stejného integrabilního majorantu. ODE sama by existenci
rozvoje nedokázala. Indukce dává přesně Eulerova čísla
druhého řádu, r_m=Σj A(m,j)x^(j+1) a
q_m=x^(2m)r_m(1/x). Základ A(1,0)=1 a obě hranice
trojúhelníku jsou explicitní v P; pořadí exponentů je správné.

Oba dvojité Stirlingovy zápisy na506 jsou koeficientové
formální řady: po pevném m suma v x konverguje pro |x|<1.
Nesměšují se s absolutní konvergencí obou nekonečných indexů
pro pevné n. Obecný asymptotický význam dodávají integrály,
nikoli neoprávněná změna pořadí nekonečného součtu.

Pro x<0 převede substituce oba neexponenciální zbytky na
1/(1−x) krát K(n,z),0≤z≤1, kde
K=∫_0^(n/z) exp((z−1)v)(1−zv/n)^(n−1)dv.
Pro n≥2 je integrand≤exp(−v/2); Taylorovy koeficienty
i majoranty jsou jednotné v kompaktním z-intervalu.
To skutečně dokazuje O-konstantu nezávislou na x<0 pro
R_x a **Q_x−T_x**. Vynechané T_x je starý C0018:
při x−4 je3/4<R_(−1/4)<1 a |n!(−4/n)^n e^−n/4|
≥(4e^−5/4)^n→∞. Q_(−4) střídavě diverguje, nemá
tištěnou limitu1/5. Pro x−1 je však rozdíl
R_(−1)−Q_(−1)=(−1)^n n!/(e^n n^n),
asymptoticky(−1)^n√(2πn)e^−2n; závěrečný komentář
odpovědi je správný po známé opravě závorek2008.

**12.** Substituce t²/2 dává pro všechna reálná x
∫_0^x exp(−t²/2)dt=sgn(x)γ(1/2,x²/2)/√2,
s hodnotou0 v x0. Zadání nemá omezení x≥0; původní
odpověď506 je sudá a při x−1 kladná místo záporné.
To je přesně stávající C0019. Žádná komplexní větev
se do tohoto protipříkladu nepřidává.

## 3. Úloha13: celá Ramanujanova nerovnost

R byl přečten celý, včetně obecného analytického odhadu;
nebyl přijat pouze Theorem7 z citovaného článku.
Ověřuje přesně

`2/3+8/(135(n+8/45)) ≤ D(n)=R(n)−Q(n) ≤ 2/3+8/(135(n+2/21))`.

Obě meze jsou nad2/3, takže jednoznačně určují požadované
θ(n) mezi2/21 a8/45. Dolní mez D(n) je větší než horní
mez D(n+1), protože n+8/45<n+1+2/21; tvrzená ostrá
monotonicita je tedy skutečným důsledkem.

Lagrangeova inverze y=z exp(y),y(0)=0 dává vytvářející
funkci Q jako−ln(1−y) v normalizaci Q(n)n^(n−1)/n!.
Proto D má funkci ln((1−y)²/(1−ez)). Přesný přechod
w=y−1 vede na Φ(w)=−ln h(w),
h(w)=2∫_0^1 t exp(−wt)dt. Koeficienty c1..c10 a
normalizované Lagrangeovy polynomy B_k(n) v R dávají
přesný D10, nikoli numerický fit.

Každý analytický předpoklad kontury je doložen. Rovnice
e^(a+ib)=1+a+ib nemá ve |b|≤π jinou nulu než0:
pro0<|b|<π by a=ln(b/sin b)>0, ale a=b cot b−1<0;
na |b|π je nemožná imaginární část a na reálné ose
platí e^a>1+a mimo0. Φ má tedy jednoznačný logaritmus
ve čtverci |Re w|,|Im w|≤π. Hranice má dolní i horní
modul R3, a sledování argumentu g=1−(1+w)e^−w dává
|ImΦ|≤2π. Na pravé hranici použitá nerovnost
(π+1)cos b+b sin b≤π+1 plyne z derivace
−πsin b+b cos b≤0. Na levé hranici jediný průchod
zápornou reálnou osou dává správné spojité navinutí;
není zaměněna hlavní větev argumentu za spojitou.

Cauchyho odhad pak dává |c_k|<11π^−k.
Po změně koeficientové kontury na y je integrand
(1−y)exp(ny)Φ(y−1)/y^(n+1). Je analytický mimo0
v oblasti deformace; globální prostota z=y exp(−y)
na nové kontuře není potřeba, jde o deformaci rezidua
již v rovině y. Svislice y=1+iτ,|τ|≤1 a delší
oblouk |y|√2,Re y≤1 leží v uvedeném čtverci.
Zbytek Taylorova polynomu má na |w|≤1 řád |w|^11,
což se s faktorem1−y mění na |τ|^12. Integrace a
Stirling dávají G n^−5,G<57; oblouk dává
H n^3/2 2^−n/2,H<14. Pro všechna celá n≥128
je oblouk<10^−7 n^−3, protože počáteční celočíselná
nerovnost a(129/128)^9<2 dokazují monotónnost ocasu.

Celý zbytek je tedy≤Δ=10^−7 n^−3+57n^−5.
Oba rozdíly D10−Δ−dolní_mez a horní_mez−D10−Δ
mají kladný jmenovatel a čitatele s **všemi kladnými
koeficienty po n=t+128**. Uložené celé polynomy,
posunuté koeficienty, jejich konstrukce a oba jmenovatele
byly přečteny. To je důkaz pro každé n≥128.

Přečteno také všech127 uložených intervalů1≤n≤127,
včetně obou kladných rezerv. Kód počítá Q konečnými
racionálními součiny a exp(n) opakovaným vnějším
intervalovým násobením již certifikovaného e. Vnější
zaokrouhlení i primitivy byly plně přijaty dříve;
žádné knihovní desetinné gamma či exp nenahrazuje meze.
Uložené konstanty jsou M<9.181,H<13.092,G<56.764,
tedy opravdu pod použitými11,14,57. Nejmenší poslední
horní rezerva je stále větší než2.09·10^−9.
Oba programy i výsledky jsou hashově identické
s původním úspěšným manifestem. Kontrola všech147
položek se neopakovala během tohoto recovery.

Ve zdrojovém článku jsou výslovně oddělené chyby
koeficientu n^−4: správně+17984/12629925. Nejde
o nový nález v TAOCP; vlastní přesný polynom používá
správnou hodnotu a obě jeho znaménkové kontroly platí.

## 4. Úlohy14(a)–(e),15–20, žádná podčást vynechána

**14(a).** Záměna k↔n−k v U_α přesně dává S1.
Pro n velké je n+α>0. V krajním k=n se f vyhodnotí
přes původní spojité vyjádření
(1−k/n)^(n+α)exp(k+k²/(2n)), tedy0. Pro záporné α
se samostatně nemultiplikuje0^α s exp(−∞).
Rozsah k zůstává0..n z původního konečného součtu.

**14(b).** Píšeme s=k/n,t=k³/n² a
f=F(s,t)=(1−s)^α exp(−tψ(s)),ψ(s)=Σj≥0s^j/(j+3).
Analytická Taylorova truncace celkového stupně j≤m
má monomy s^(j−i)t^i=k^(2i+j)n^−i−j,0≤i≤j.
Pro0<ε<1/6 je zbytek jednotně
O(n^((m+1)(−1/2+3ε))). Pro ε≥1/6 jsou požadované
meze slabší: každý monom je nejvýše uvedený řád
a samotné f je v0≤k≤n jednotně omezené. Pro α<0
to není odhad samotného faktoru(1−s)^α: S výslovně
omezuje log f=A L−n(L−s−s²/2),A=−α,L=−ln(1−s).
Na s≤1/2 použije L≤2s; na s≥1/2 platí
L−s−s²/2≥L/72, takže pro n≥72A je log f≤0.
Nevyvozuje se definiční obor k>n pro necelou mocninu
jen z pomocné horní meze n^(1/2+ε).

**14(c).** Gaussův součet má velikost O(√n), proto
suma lokální chyby je O(n^−m/2+3(m+1)ε).
Pro dané δ>0 zvolíme ε<min(1/6,δ/(3(m+1))).
Ocas za n^(1/2+ε) je omezen Cn exp(−n^(2ε)/2).
Konečně mnoho polynomiálních Gaussových ocasů lze
prodloužit do∞ se stejnou zanedbatelností; rozdělením
exp(−k²/(2n)) na dvě poloviny exponenciály pohltíme
každou mocninu k. Dostáváme přesně tvrzené O(n^−m/2+δ).

**14(d).** Pro celé t≥0 je x^t exp(−x²/2) hladká
a integrály absolutních hodnot všech derivací jsou
konečné; Euler na síti h=n^−1/2 tedy dává libovolný
pevný řád. Pro **necelé** t≥0 dodává nový úplný
`quality-recovery-gaussian-real-powers-2026-11-06.md`
funkcionálu Eulerova vzorce od1, koeficienty ζ(−t−2j)
a integrální odhad po rozdělení v x=√(2n). Výsledkem je
pro každé M≥1 přesný konečný rozvoj s chybou O(n^−M).
Žádná vysoká derivace necelé mocniny se v nule nepoužije.
Případ t0 má konstantu1+ζ(0)=1/2 podle0^0=1.

**14(e).** Pro h=n^−1/2,z=k/√n je lokální integrand
exp(−z²/2)exp(Σj≥1h^j E_j(z)), kde
E_j=−αz^j/j−z^(j+2)/(j+2). Konečná rekurence
A0=1,A_j=(1/j)Σr1..j r E_r A_(j−r) vytváří
každý koeficient. Moment ∫0∞z^d exp(−z²/2)dz
=2^((d−1)/2)Γ((d+1)/2) je přesná substituce.
První tři členy jsou tím
√(πn/2)−α−1/6+(1/12+α/2+α²/2)√(π/(2n)):
konstanta je∫A1+1/2=−α−2/3+1/2,
další člen je integrál A2. Vyšší rekurence s Eulerovými
krajními členy dává V_α v§1. Volba většího m v(c)
dokazuje každý požadovaný konečný řád, ne konvergenci
nekonečné asymptotické řady.

Při vážení Stirlingem pro P se jeho řada používá
jednotně jen v k=n+O(n^(1/2+ε)). Mimo toto okno
mají přesné členy po normalizaci majorantu
C√(k/n)exp(n(log(k/n)−k/n+1)). Pro k≤n platí
log r−r+1≤−(1−r)²/2. Konečný ocas je tedy
exponenciálně menší. To odůvodňuje přechod od14
k vyšším koeficientům P, včetně součtu chyb.

**15.** Konečný binomický rozvoj a ∫z^k e^−z dz=k!
dávají integrál1+Q(n); počet členů je n+1, není
zde otázka záměny dvou nekonečných operací.

**16.** Rozepsání Q a přeházení dvou konečných sum
dává pro pevné j vnitřní součet
(−1)^j n_falling(j)Σl0..n−j(−1)^l C(n−j,l)(l+j)^(n−j−1).
Pro j<n je to diference řádu n−j polynomu nižšího
stupně, tedy0. Pro j=n zbývá(−1)^n n!/n.
Krajní k0 je prázdný součet Q(0)=0; nevzniká
izolované0^−1. Zadané n>0 zahrnuje n1 přímo.

**17.** S konverguje, protože pro pevné n jsou členy
nejvýše polynom v k krát exp(−k). Přesné rozdělení
T(n)=Σk≥0 k^(n−k)k!/n! dává T(n)=P(n)+S(n+1).
Celý diskrétní výpočet kolem k=n se použije na obě
strany maxima; parita A_j ruší liché integrály
a krajní Eulerovy členy se při spojení zruší.
Pro k/n mezi1/2 a2 platí
log r−r+1≤−(r−1)²/8. Pro r≥2 je tato fáze≤−cr
s c=(1−ln2)/2>0; tím je i nekonečný pravý ocas
řádně zanedbatelný. Odečtení P a posun n↦n−1 dávají
všech pět členů odpovědi506, s koeficienty
√(π/2),2/3,−√(π/2)/24,−4/135,49√(π/2)/1152
v řádech√n,1,n^−1/2,n^−1,n^−3/2, plus O(n^−2).
Známá oprava zápisu indexu1998 nemění hodnotu.

**18.** Celý polynom H_n(X,Y) ze S má díky již dokázané
Abelově identitě rekurenci
H_n=(X+Y+n)^n+nH_(n−1)(X+1,Y),H0=1.
Při rekurzi se X+Y+n nemění, proto
H_n=Σk0..n C(n,k)k!(X+Y+n)^(n−k).
Polynomiální identita odstraňuje zdánlivé záporné
mocniny pomocného Abelova zápisu i při nulových
základnách. X=Y=0 a X1,Y0 dávají přesně
n^n(1+Q(n)) a(n+1)^n Q(n+1). Při n0 se obě
původní sumy vyhodnotí přímo jako1. Cauchyho
historická formule je přesně ztotožněna níže.

**19.** Konvergence C_N dává omezenou primitivní
F(t)=∫r..t exp(−Nu)f(u)du,|F|≤K. Pro n>N
integrace po částech a nulový krajní člen v∞
omezují ocas K exp(−(n−N)r). Lokální část je
nejvýše MΓ(α+1)n^−α−1,α>−1. To je důkaz celého
zadání i při **podmíněné** konvergenci na∞;
předpoklady analytických historických formulací
se sem nepřidávají. Lokální integrovatelnost
a běžný nevlastní význam integrálů jsou explicitní.

**20.** Z15, z=nx a v=x−ln(1+x) plyne
Q+1=n∫0∞exp(−nv)(dx/dv)dv. Analytická lokální
inverze x=Σk≥1c_k(2v)^(k/2) dovoluje derivovat;
dx/dv=Σk1..m−1 k c_k(2v)^(k/2−1)+O(v^(m/2−1)).
Pro každé celé m≥1 je exponent zbytku>−1
a na∞ je dx/dv=1+1/x omezené. Celé Watsonovo
lemma tedy dává přesně zadanou řadu a chybu
O(n^(1−m/2)), včetně m1 s prázdným součtem.
Faktor k v derivaci je známá oprava2006, nikoli
nový nález. Konkrétní článek Rousseau zůstává
výslovnou bibliografickou výjimkou.

## 5. Prameny, čtyři vrstvy, uložené výpočty a závěr

Celé přečtené pramenné revize a přijímaný přesný rozsah:

- `cauchy-asymptotic-root-review.md`: přesná rovnice22
  na68 a reziduální postup62–68, širší agentova četba62–73.
  Substituce ξ=Y+n,η=X+n dává právě H_n; nejde o pouhou
  shodu názvu ani přijetí všech vedlejších Cauchyho vět.
- `tricomi-asymptotic-root-review.md`: celý136–148 u agenta,
  přesné root pasáže a původní(12),(15),(21). Převod
  J(x,f)=−x I(x,−f/x), lichost nenormalizovaného E a
  komplexní oblasti dokazují citovaný obsah. Nejde
  o prohlášení absolutní priority nebo kontrolu celého svazku.
- `carlitz-asymptotic-root-review.md`: celý248–252 a
  CMath270–271, identické rekurence po posunu indexu
  h=j+1. Koeficienty jsou přijaty pro každý řád;
  nekontrolované komplexní oblasti Buckholtze se nepřebírají.
- `barnes-watson-root-review.md`: Barnesův§5 a celé
  Watsonovo lemma s důkazem na133; rozdíl předpokladů
  proti širší knižní úloze je výslovný. Rok1918
  není datum přednesení1916 a Barnese dokládá tisk1906.
- `ramanujan-originals-root-review.md`: původní zadání128,
  celé řešení151–152 a přesný převod θ=(R−Q)/2.
  Silnější nerovnost je doložena ve vymezeném reprintu,
  není jí připisován nedoložený přesný den prvního dopisu.
- `furch-root-review.md`: celý92–95, převod x=n−1,
  y=1−α a stejné(10a). Asymptotické půlení není
  vydáváno za přesný vzorec mediánu. Vedlejší Furchovo
  tiskové minus se nepřenáší do vzorců TAOCP.
- `debruijn-methods-root-review.md`: obsah1958§3.4,3.9
  přesně dokládá doporučené metody. Nesvědčí o doslovném
  původu všech podčástí14 ani o totožnosti sazby1961.
- `demuth-gould-root-status.md` a `rousseau-root-status.md`:
  doložené identity a přesné meze nedostupného obsahu
  jsou převzaty jako meze, nikoli jako důkazy textu.

Temme1975/1979, Odlyzkův seznam65 číslovaných příkladů,
Helen Keller1898 a Knuthovo vlastní svědectví mají přesný
dříve čtený rozsah v úplném scope. Nejde o audit všech
Odlyzkových důkazů ani uříznutého okraje Temmeho skenu.
**Výslovně přeskočeno:** Demuth67–68, Gould1019–1021,
Rousseau159–161 a přesná kolace de Bruijn1961.
Historické source-partial X0138/X0143/X0769/X0775/X0782
se tím nepřepisují na doložené původní články.

`results/quality-recovery-asymptotic-calculations-errata-2026-11-06.json`
fixuje16/4/8/8 relevantních bloků čtyř úplných vrstev,
jejich hashe a velikosti; sousední Eulerovy/MIX položky
jsou výslovně oddělený kontext. Původní obrazy all1 7,
all1-prepre12/36 a all1-pre16 byly přečteny v popsaných
revizích; all1 7 a all1-prepre12/36 také přímo v této
recovery předcházejícími bloky. Známé změny indexu,
16/8505, faktoru k, x^x, závorek, odkazu a oborů2024
zůstávají known_erratum. C0016–C0019 zůstávají čtyři
původní nesrovnalosti odpovědí, se stejnými důkazy
a omezením na dostupný první tisk, bez tvrzení prvenství.

Celé130řádkové `check_asymptotic_calculations.py` a124řádkové
`check_ramanujan.py` byly přečteny. První51 konečných
symbolických kontrol doplňuje obecné analytické důkazy;
nejsou náhradou zbytků. Druhý kombinuje nezávisle odvozené
koeficienty, obecné polynomiální certifikáty a všech127
malých intervalů. Všechny smyčky mají explicitní konečné
hranice; obecné rekurence koeficientů postupují striktně
po nižších indexech a končí pro každý zvolený řád.
Není zde deklarována složitost obecného numerického
výpočtu zvláštních funkcí. Žádný starý běh se nespouštěl.

Každé matematické tvrzení a každá podčást20 úloh má
dostatečný argument s uvedenými doménami a krajními
interpretacemi konečných členů. Nová matematická mezera0,
nový nález0, žádný matematický běh. Výslovné bibliografické
výjimky, známé opravy a čtyři starší nálezy zůstávají zachovány.
