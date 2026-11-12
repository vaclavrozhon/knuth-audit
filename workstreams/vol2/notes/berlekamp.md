# §4.6.2: konečná tělesa, Berlekamp a první úlohy

Stav: 4. listopadu 2026. Tento blok uzavírá matematickou kontrolu úloh
**1–14, 16 a 17**, nikoli celou §4.6.2. Vlastní důkazy níže pokrývají
algoritmy B/N a text stran 439–446. Další rozklad podle stupňů,
odmocniny, celočíselné polynomy a historické odkazy se dokončují odděleně.
Inventář všech 41 úloh byl vizuálně ověřen na stranách 455–461;
strana 461 tedy patří koncem první úlohové sady i následující sekci.

Čtyři nové nálezy C0203–C0206 se týkají doprovodných vzorců a dolní meze
stupně. Algoritmy B/N ani výsledné rozklady nejsou těmito nálezy vyvráceny.
Nový fyzický dotisk a prvenství nálezů nejsou ověřeny. Nic nebylo odesláno.

## 1. Značení a rozsah zdrojů

`F_p` je těleso zbytků modulo prvočíslo p. Monický polynom má vedoucí
koeficient 1; ireducibilní polynom kladného stupně nemá rozklad na dva
polynomy kladných stupňů. Počty faktorů v pravděpodobnostních úlohách
zahrnují násobnost, pokud výslovně neřekneme „různých“.
Polynom je bez násobných faktorů, pokud se žádný ireducibilní faktor
nevyskytuje dvakrát. `gcd` volíme monický. `a[n,p]` označuje počet
monických ireducibilních polynomů stupně n nad F_p. Jeho vzorec dokážeme
v oddílu 3. Proměnné z,w v generujících funkcích jsou formální;
`[z^n]` znamená koeficient u z^n.

Původní sazba: strany 439–446, 455–457 a odpovědi 678–682 byly čteny
vizuálně, včetně všech matic. Strany 458–461 byly čteny kvůli inventáři
a návaznosti dalších úloh. Vektorové přepisy matic a tabulek jsou v
`sources/berlekamp-printed-data.json`. Je v něm výslovně rozlišeno pořadí
koeficientů: obvykle vzestupné, u tabulky posuvného registru sestupné.

Všech šest vrstev errat bylo prohledáno podle stránek, §4.6.2 a jmen/pojmů:
`all2-prepre`, `all2-pre`, `all2`, `err2`, `err2-2e` a TeX `err2.textxt`.
Pro druhé vydání byly zahrnuty posunuté strany 420–441 a 623–633.
Pro TeX byl zahrnut formát `2.679`. Úplný záznam s hashi a kontextem:
`sources/polynomial-factorization-errata.txt`.

Relevantní známé změny:

- 6. března 1998 oprava českého názvu časopisu na straně 442;
  6. června 1999 čárka v seznamu indexů na téže straně.
- 6. ledna 2011 doplnění slovních názvů kroků B1–B4; nejde o změnu
  matematického postupu.
- 30. června 2002 doplnění závorky na straně 680, řádek 3. Originální
  stránka errat 42 je zobrazena. **Neopravuje záporný exponent z^(-m).**
- 17. srpna 2024 výměna rolí v,w v poznámce k odpovědi 2 na straně 679.
  Původní konvence `u=v*w^r`, v bez r-tých mocnin, je sama správná;
  změna ji sjednocuje s předcházejícím zadáním `u=v^r*w`.
- Druhé vydání, strana 625, 26. června 1997: opravy znamének ve vzorcích
  úlohy 13 jsou již zapracovány v našem třetím vydání.

Berlekampův původní článek z roku 1967 byl získán jako sken BSTJ,
1853–1859, a celý vizuálně přečten. Strany 1854–1857 přímo dokládají
matici Frobeniovy mocniny, rozklad přes gcd, dimenzi jádra a úplnost
oddělování faktorů. Vlastní důkaz níže je úplný a nezávislý na přepisu
autorových příkladů. Jeho dvě číselné tabulky zde nejsou zvlášť auditovány.
Na straně 1859 je v uvedeném seznamu báze vynechána konstanta 1;
jde o okraj původního článku, nikoli nález v Knuthově knize.

Bibliografický kontext Petr/Butler/Schwarz, Gaussův odkaz u úlohy 4,
Lagrange 1771, Weinbergerův odkaz a původní Swinnertonův příklad
zůstávají v historickém podbloku sekce. Matematické výsledky příslušných
úloh jsou zde odvozeny; ověření těchto odkazů se tím neprohlašuje za hotové.

## 2. Úloha 1: lineární a kvadratické faktory

Pro k různých zadaných lineárních faktorů je počet monických násobků
stupně n roven p^(n-k), pokud k<=n. Princip inkluze a exkluze proto dává

```text
P(alespoň jeden lineární faktor)
  = 1 - sum_{0<=k<=min(n,p)} (-1)^k binom(p,k) p^(-k).
```

Pro n>=p je to `1-(1-1/p)^p`. První dvě, resp. tři nenulové členy
pro sjednocení událostí dávají meze `(1+1/p)/2` a `(2+1/p²)/3`.
Pro n=2 je třetí průnik prázdný; horní mez stále platí. Střední počet
lineárních faktorů s násobností je součet pravděpodobností, že každý
z p faktorů dělí u alespoň j-krát:

```text
E L = p * sum_{j=1..n} p^(-j) = p/(p-1) * (1-p^(-n)).
```

Podle oddílu 3 je počet ireducibilních kvadratik `A=p(p-1)/2`. Stejným
postupem, nyní s poklesem stupně o 2 při každém zadaném faktoru, dostáváme

```text
P(Q>=1) = 1 - sum_{0<=k<=min(floor(n/2),A)}
                   (-1)^k binom(A,k) p^(-2k),
E Q = A * sum_{j=1..floor(n/2)} p^(-2j)
    = p/(2(p+1)) * (1-p^(-2 floor(n/2))).
```

Zde Q je počet ireducibilních kvadratických faktorů s násobností.
**C0203:** v prvním tištěném vzorci chybí `1-`; vyjadřuje pravděpodobnost
žádného takového faktoru. **C0204:** ve druhém vzorci chybí násobitel
`p/(p+1)`. Pro p=n=2 je jedinou ireducibilní kvadratikou x²+x+1;
ze čtyř monických polynomů ji obsahuje jediný. Pravděpodobnost i průměr
tedy jsou 1/4, zatímco tištěné vzorce dávají 3/4 a 3/8.

Ostatní kvadratické odhady jsou správné. Bonferroniho dolní mez je
`A/p²-binom(A,2)/p⁴ = 3/8-1/(4p)+(p-2)/(8p³)`, pokud n>=4;
pro n=2,3 je přesná pravděpodobnost ještě větší. To implikuje tištěnou
dolní mez `3/8-1/(4p)`. Horní mez je `A/p²=1/2-1/(2p)`.
Při pevném p a dostatečně velkém n je přesná pravděpodobnost
`1-(1-p^(-2))^A`. Její rozvoj při p rostoucím do nekonečna je
`1-exp(-1/2)(1+1/(2p))+O(p^(-2))`. Je třeba rozlišit oba limity;
tištěný O-člen vyjadřuje rozvoj v p, nikoli rychlost konvergence v n.

Poznámka o pevném celočíselném polynomu na přelomu 678/679 používá
Čebotarevovu větu o hustotě Frobeniových tříd, tedy hlubší externí vstup.
Její konečný grupový krok lze dokázat přímo: pro grupu G působící na
kořenech Ω platí `sum_g |Fix(g)| = sum_a |Stab(a)| = |G|*počet orbit`.
U ireducibilního polynomu kladného stupně je jedna orbita a průměr je 1.
U součinu se průměry sečtou, včetně násobností. Vlastní důkaz zde
nepředstírá důkaz Čebotarevovy věty ani kontrolu citovaného článku.

## 3. Úlohy 2, 4, 5: jednoznačný rozklad a generující funkce

Úloha 2(a): moničnost v UFD zaručuje, že každý vedoucí koeficient faktoru
je jednotka, a tedy lze všechny faktory normalizovat na monické.
V rozkladu `u=prod f_i^e_i` je nutně
`v=prod f_i^floor(e_i/2)`, `w=prod f_i^(e_i mod 2)`.
To dokazuje existenci i jednoznačnost, včetně u=1.

Pro 2(b) je generující funkce všech monických polynomů `1/(1-pz)`;
funkce jejich čtverců je `1/(1-pz²)`. Počet polynomů bez násobných
faktorů má tedy funkci `(1-pz²)/(1-pz)`: počty jsou 1,p a
`p^n-p^(n-1)` pro n>=2. Obecně pro zákaz r-té mocniny, r>=2,
je funkce `(1-pz^r)/(1-pz)` a počet `p^n-p^(n-r+1)` pro n>=r.

Úloha 4: jednoznačný rozklad dává formální Eulerův součin

```text
1/(1-pz) = prod_{d>=1} (1-z^d)^(-a[d,p]).
```

Po logaritmování a porovnání koeficientu u z^n vyjde
`p^n = sum_{d|n} d*a[d,p]`. Möbiova inverze, kde μ je Möbiova funkce,
tedy dává

```text
a[n,p] = (1/n) sum_{d|n} μ(n/d) p^d,
G_p(z) = sum_{m>=1} μ(m)/m * log(1/(1-pz^m)).
```

Inverze v nápovědě plyne po přeskupení koeficientů z identity
`sum_{d|k} μ(d)=[k=1]`. Je legitimní formálně: pro libovolný koeficient
se sečte jen konečně mnoho členů. Při pevném n máme
`a[n,p]/p^n -> 1/n`. Navíc a[n,p]>0 pro všechna n>=1: pro n>=2 je
`n*a[n,p] >= p^n-sum_{j=1..floor(n/2)} p^j > 0`.
Tím je doložena i existence těles v úloze 16, bez kruhového odkazu.

Pro úlohu 5 nechť `A[n,p]` je střední celkový počet ireducibilních
faktorů. Funkce zaznamenávající současně stupeň a počet faktorů je

```text
H_p(z,w) = prod_{d>=1} (1-wz^d)^(-a[d,p])
         = exp(sum_{k>=1} G_p(z^k) w^k/k).
```

Kniha ji značí kaligrafickým G. Počty `a[d,w]` lze chápat jako
polynomy ve w dané Möbiovým vzorcem. Platí také **Wittova symetrie**

```text
H_p(z,w) = exp(sum_{m>=1} a[m,w] log(1/(1-pz^m))).
```

Nejde o chybu v prohození p,w: koeficient z^n v n-násobku logaritmu
má tvar `sum_{abc=n} μ(a) p^b w^c`, který je symetrický v p,w.
**C0205:** tištěný exponent je však `z^(-m)`, nikoli z^m.
Pro w=1 je a[1,1]=1 a a[m,1]=0 pro m>1. Tištěná pravá strana
pak dává `1/(1-p/z)`, zatímco H_p(z,1) musí být `1/(1-pz)`.
Známá oprava závorky z roku 2002 tuto samostatnou chybu nemění.

Derivací podle w v bodě 1 a substitucí z/p dostáváme přesně

```text
sum_{n>=0} A[n,p] z^n
  = (1/(1-z)) sum_{d>=1} φ(d)/d * log(1/(1-p^(1-d)z^d)),
```

kde φ(d) je Eulerův počet zbytků nesoudělných s d. Přeskupení používá
`sum_{k|d} μ(k)/k = φ(d)/d`. Člen d=1 dává harmonické číslo
`H_n=sum_{j=1..n}1/j`; člen d=2,k=1 dává 1/(2p) pro n>=2.
Zbývající kladné členy mají celkový součet O(p^(-2)), i jednotně v n.
Tištěný odhad střední hodnoty je tedy správný.

Wittova symetrie pro w=2 dává
`H_p(z/p,2)=(1-z)^(-2)(1-z²/p)^(-1)*R(z)`, kde zbylé koeficienty
R jsou nezáporné a `R(1)=1+O(p^(-2))`. Proto
`E(2^r)=n+1+(n-1)/p+O(n/p²)` pro n>=2. Při p->nekonečno je to n+1.
Obdobně `E(4^r)->binom(n+3,3)`, takže limitní rozptyl 2^r má řád n³.
Také pro pevné p je rozptyl řádu n³: zbývající Eulerův součin je
analytický a kladný v okolí z=1, zatímco pól má řád 4; čtverec průměru
má jen řád n². Tyto asymptotiky nejsou odvozeny z konečného testu.

## 4. Úlohy 3, 6, 7 a správnost B

Úloha 3: pro navzájem nesoudělné polynomy u_j nad tělesem nastavme
`U=prod_j u_j`, `U_j=U/u_j`. Rozšířený Eukleidův algoritmus dává
`b_j U_j = 1 mod u_j`. Polynom `sum_j w_j b_j U_j mod U`
má požadované zbytky a stupeň menší než deg U. Rozdíl dvou řešení
je dělitelný každým u_j, tedy U; stupňové omezení jej nutí být nulový.
Nad celými čísly gcd=1 nezaručuje Bézoutovu identitu s hodnotou 1:
pro u_1=x,u_2=x-2 a zbytky 1,0 by v=ax+1 musel mít a=-1/2.

Úloha 6: každý prvek F_p je kořenem x^p-x; oba monické polynomy
`x^p-x` a `prod_{s in F_p}(x-s)` stupně p jsou proto stejné.
Koeficienty padající mocniny x podtržené p jsou se znaménky Stirlingova
čísla prvního druhu. Z identity plyne jejich nulovost modulo p
kromě krajních stupňů 1,p. Inverzní převod mezi obyčejnými a padajícími
mocninami pak dává stejné tvrzení pro druhý druh: rozdíl x^p-x
je právě padající mocnina p, a základna nižších padajících mocnin
je trojúhelníková s jednotkami na diagonále.

Úloha 7: jestliže `v^p=v mod u`, každý ireducibilní mocninný faktor u
dělí právě jeden v-s, protože dva různé v-s se liší nenulovou konstantou.
Součin `prod_s gcd(u,v-s)` je tedy přesně u. Tento argument platí
i pro násobné faktory; squarefree předpoklad není pro identitu potřebný.

V B1 je `gcd(u,u')=1` právě tehdy, je-li u bez násobných faktorů.
Nulová derivace znamená `u=v(x^p)=v(x)^p`, protože pracujeme nad F_p.
V ostatních případech d=gcd(u,u') a u/d snižují stupeň; násobnosti
lze zpracovat pomocí navazujících úloh 34/36. Konstantu 1 oddělujeme
před začátkem faktorizace; nemá žádné faktory.

Pro squarefree `u=prod_{i=1..r} f_i` čínská věta o zbytcích ztotožní
polynomy modulo u se součinem těles F_p[x]/(f_i). V každém z nich má
rovnice y^p-y=0 právě p kořenů, prvky F_p. Řešení `v^p=v mod u`
tedy tvoří vektorový prostor dimenze r a odpovídají všem r-ticím
konstant. Frobeniova mocnina v->v^p je F_p-lineární a její matice v
řádkové konvenci je Q z (12). Proto dimenze levého jádra Q-I je r.

Pro libovolné dva různé faktory f_i,f_j existuje řešení s různými
konstantami na těchto dvou souřadnicích. Některý vektor libovolné báze
je tudíž také rozlišuje; jinak by je nerozlišovala žádná lineární
kombinace. Postupné gcd v B4 proto skončí přesně r ireducibilními
faktory. Konstantní první vektor žádné rozdělení nepřináší.

## 5. Algoritmus N, úlohy 8–11 a 14

V N označuje c_j již vybraný řádek pivotu ve sloupci j, nebo -1.
Invariant: pivotový řádek c_j je záporný jednotkový řádek ve sloupci j;
všechny dříve zpracované řádky mají nuly v dosud volných sloupcích.
Nový pivot v řádku k má proto nad sebou nuly. Jeho normalizace na -1
a přičtení násobků jeho sloupce do ostatních sloupců zachovají staré
řádky i levé jádro: jde o násobení vpravo invertibilní maticí.

Pokud nový pivot neexistuje, je řádek k kombinací pivotových řádků:
`row_k + sum_j a[k,j] row_{c_j}=0`. To je přesně vektor (18).
Každý takový vektor má 1 na své nepivotové souřadnici k a nuly
na všech ostatních nepivotových souřadnicích. Proto jsou nezávislé
(úloha 8). Počet pivotů je hodnost, takže nalezené vektory tvoří celou
bázi jádra. Důkaz platí beze změny i pro obdélníkové matice.

V tištěném příkladu byly přesně ověřeny všechny řádky tabulky mocnin,
Q, Q-I, pět následných matic, tři výstupní vektory i všech 26 gcd.
Výsledný rozklad má stupně 4,3,1. V úlohách 10 a 11 souhlasí celé
matice i faktorizace stupňů 6+2 modulo 2 a 1+2+5 modulo 5.
Úloha 9: aktualizace x<-2x,y<-51y zachovává xy=1 modulo 101,
protože 2*51=1. Primitivnost 2 znamená, že projdeme všech 100
nenulových zbytků právě jednou; celý cyklus byl také přesně ověřen.

Úloha 14: zbytek v modulo f_i je konstanta s_i. Pro libovolný polynom
w(T) platí `u|w(v)` právě tehdy, když `w(s_i)=0` pro všechna i.
Nejmenší monický takový polynom je tedy
`w(T)=prod_{s in {s_1,...,s_r}} (T-s)`; jeho stupeň k je počet
různých hodnot s_i. Řádky `1,v,v²,...` modulo u mají první lineární
závislost právě v řádku k. Algoritmus N ji najde, včetně vedoucí
jedničky v (18). Nemusíme znát r předem.

**C0206:** tištěné `2<=k<=r` vyžaduje nekonstantní v, které zadání
nepředpokládá. Pro `F_2,u=x(x+1),v=1` je k=1 a w(T)=T+1.
Obecně správně `1<=k<=min(p,r)`; spodní mez 2 platí právě tehdy,
když v není konstantní. Samotný postup N zde vrátí správný výsledek.

## 6. Úlohy 12, 13, 16 a 17

Pro p=2 platí x⁴+1=(x+1)⁴. Pro liché p je polynom bez násobných
faktorů a ve vztahu x⁴=-1 závisí Q jen na p modulo 8. Čtyři vytištěné
matice Q-I jsou správné: pro p=1 mod 8 mají hodnost 0, jinak 2.
Počet faktorů je tedy 4, resp. 2. V druhém případě nemohou být lineární,
protože nenulový kořen by měl řád 8, který nedělí p-1. Jde o dvě
ireducibilní kvadratiky. Kvadratická reciprocita určuje existenci
odmocnin -1,2,-2; prosté vynásobení všech vzorců v odpovědi 13 dává
x⁴+1. Výpočet ověřil všechny liché prvočíselné moduly pod 200.

Ireducibilitu x⁴+1 nad Q lze dokázat bez číselného odhadu z úlohy 20:
po substituci x+1 dostaneme x⁴+4x³+6x²+4x+2, na který platí
Eisensteinovo kritérium pro 2. Polynom je monický, takže také ireducibilní
nad Z. U Swinnertonova příkladu součin osmi faktorů s kořeny
`±sqrt(2)±sqrt(3)±i` dává přesně `x^8-16x^6+88x^4+192x²+144`.
Tři nezávislé kvadratické odmocniny generují rozšíření Q stupně 8;
jejich podepsané součty jsou různé, tedy polynom je ireducibilní.
Modulo každé liché p lze všechny tři odmocniny nalézt ve F_(p²);
všechny faktory proto mají stupeň nejvýše 2. Modulo 2 je to x^8.
Pro obecný stupeň 2^k použijeme k nezávislých prvočíselných
kvadratických odmocnin; stejný argument funguje i v ramifikovaných
modulech, protože součin je polynomiální identita s celočíselnými
koeficienty. Původní atribuce z roku 1970 se ověřuje zvlášť.

Úloha 16(a): pro ireducibilní f stupně n je každý nenulový zbytek g
nesoudělný s f a Bézoutova identita dává jeho inverzi. Je přesně p^n
zbytků, tedy těleso o p^n prvcích. Existence f byla doložena v oddílu 3.
Pro (b) nechť M je nejmenší společný násobek řádů nenulových prvků.
Pro každou prvočíselnou mocninu v M vybereme prvek, jehož řád ji
obsahuje, a vhodnou mocninou odstraníme ostatní prvočinitele.
Součin takto získaných prvků má řád M, protože grupa je komutativní
a dílčí řády jsou nesoudělné. Všechny nenulové prvky jsou kořeny
T^M-1, takže p^n-1<=M. Lagrangeova věta dává opačnou dělitelnost;
M=p^n-1 a tento prvek generuje celou multiplikativní grupu.

Pro (c) je Frobeniova mocnina F(a)=a^p automorfismus. Pokud F^m
fixuje třídu x, fixuje všechny polynomy v ní, a tedy celé těleso.
Pak p^n-1 dělí p^m-1, což nastává právě pro n|m: po vydělení
m=qn+r je zbytek p^r-1 a pro 0<r<n je příliš malý. Opačná
implikace plyne z F^n=identita. Důkaz zahrnuje také f=x; zkratka
`x=ξ^k` v tištěné odpovědi vynechává nulovou třídu x, ale pro ni
je závěr bezprostřední, protože n=1.

Test ireducibility v zadání: dělitelnost x^(p^n)-x vylučuje násobnosti
a nutí stupně faktorů dělit n. Každý vlastní dělitel d čísla n dělí
n/q pro vhodné prvočíslo q|n. Podmínky nesoudělnosti pak vyloučí
všechny faktory stupně menšího než n. Obrácení je již část (c).

Úloha 17: cyklická grupa řádu 168 má φ(d) prvků každého řádu d|168
a žádné jiné řády. Nula nemá multiplikativní řád. Celá tištěná tabulka
souhlasí, součet je 168. Nezávislý model F_13[t]/(t²+2) skutečně
prošel všech 168 nenulových prvků opakovaným násobením a nalezl stejné
počty; -2=11 není čtverec modulo 13, takže jde o těleso.

## 7. Složitost, přesné kontroly a pokračování

Pro squarefree vstup stupně n stojí B1 O(n²) operací v F_p. Posuvný
registr v B2 má (n-1)p kroků po O(n) operacích. N stojí O(n³).
Při pevném v,s je součet cen gcd přes všechny současné faktory
O(n*sum deg faktorů)=O(n²). Celá B4 tedy stojí O(prn²), kde r je
počet různých ireducibilních faktorů. To dává O(n³+prn²).
Pro velké p a školskou bitovou aritmetiku potřebuje první mocnina x^p
O(n² log³p), další řádky Q O(n³ log²p), stejně jako eliminace.
Meze na straně 446 jsou správné. Úsporné zpracování násobností B1
a navazující náhodné rozdělování se uzavřou v dalších podblocích;
náš jednoduchý validační program není implementací optimální časové meze.

`verify_berlekamp.py` má oddělené checkpointy; úspěšné bloky nebyly
opakovány. Přesná aritmetika používá již existující pomocnou třídu Ring,
ale nespouští žádný starší test. Nezávislá kontrola je rozklad zkoušením
všech možných malých ireducibilních dělitelů, konvenční řádková eliminace,
úplný výčet vektorů a navíc SymPy na vybraných instancích.

Výsledky v `results/berlekamp.json`:

- 14 řádků registru, 561 položek tištěných matic, 26 gcd, všechny tři
  úplné tištěné faktorizace, 100 převrácených hodnot modulo 101.
- 833 matic, z toho 697 úplných porovnání jádra s výčtem všech vektorů.
- 2 052 monických polynomů úplně faktorizováno, 122 kontrol přes SymPy.
- 27 úplných rozdělení počtu faktorů, celkem 4 321 polynomů; přesně
  ověřeny průměry, pravděpodobnosti, Eulerův součin i Wittova symetrie.
- 45 prvočísel pro x⁴+1, 168 prvků F_169, 862 Frobeniových dělitelností.
- 614 minimálních polynomů úlohy 14 a symbolický součin osmi kořenů
  Swinnertonova příkladu.

Všech šest bloků prošlo; jednotlivé časy, PID, limity 180 sekund a logy
jsou v výsledku a RUN_STATE. Jde o ověření konkrétních dat a implementace;
obecná správnost a asymptotiky jsou dokázány výše.

Další práce: úloha 15 a známá oprava její pravděpodobnosti; poté strany
447–449 a úlohy 28–31,37; následně Hensel a celočíselná část.
Předběžná podezření pro další blok: tvrzení „gcd will be 1“ v odpovědi 15
má pro p=5,u=1 protipříklad; oprava z roku 2001 má v první formuli sx+t,
ale dále počítá úspěšné posuny x+s. Tyto položky zatím nejsou novými
nálezy tohoto bloku. U úlohy 19 je třeba vyjasnit primitivnost vstupu.
