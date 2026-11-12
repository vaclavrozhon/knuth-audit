# §3.2.1.2: volba násobitele a perioda

Kontrola 1. listopadu 2026. Text str. 16–21, úlohy 1–22 na str. 21–23,
odpovědi str. 547–550. Originály byly vizuálně přečteny, například
[str. 17](../images/vol2-p017.png), [str. 23](../images/vol2-p023.png)
a [str. 549](../images/vol2-p549.png). Inventář má přesně 22 úloh,
bez dodatečné úlohy v erratech. Úloha 22 má samostatnou
[poznámku](lagged-periods.md); zde jsou věty a úlohy 1–21.

## Notace

Modul m je kladné celé číslo. Kongruenční generátor je posloupnost
`X_(n+1)=(a X_n+c) mod m`, se zbytky mezi 0 a m−1. Délka počátečního
úseku před cyklem je mu, nejmenší kladná délka cyklu lambda.
**Jednotka modulo m** je číslo nesoudělné s m. Jeho **řád** ord_m(a)
je nejmenší kladné s s `a^s=1 mod m`. **Primitivní prvek** zde znamená
jednotku největšího řádu; nemusí generovat všechny jednotky. Největší řád
značíme L(m), kniha lambda(m). Počet jednotek je Eulerova funkce phi(m).
Pro prvočíslo p značí v_p(z) exponent p v rozkladu nenulového z.
Nejmenší společný násobek je lcm; prázdný lcm je 1.
Čínská věta o zbytcích jednoznačně určuje zbytek modulo součin
nesoudělných modulů z jeho zbytků modulo jednotlivé činitele.

Modul m=1 má jediný stav a periodu 1. Jinak předpokládáme normalizaci
0<=a<m podle §3.2.1. Degenerace a=0 je konstantní zobrazení.
Normalizace odstraňuje zdánlivý problém nutnosti a=1 modulo 4 v odpovědi 2
při m=2: jediná lichá přípustná hodnota je a=1. Perioda multiplikativního
generátoru se rovná řádu a, pokud je počáteční stav nesoudělný s m.

## Lemma P: zdvih exponentu prvočísla

Je-li x=1+q p^e, p nedělí q a p^e>2, binomický rozvoj dává
`x^p = 1+q p^(e+1) + násobek p^(e+2)`.
Pro členy 2 až p−1 obsahuje binomický koeficient faktor p; poslední člen
má exponent pe alespoň e+2. To platí i pro p=2, protože tehdy e>=2.
Proto v_p(x^p−1)=e+1 a opakováním v_p(x^(p^j)−1)=e+j.
Umocnění na r nesoudělné s p zachová původní valuaci stejným rozvojem.

## Lemma Q a počáteční úsek

Při m=product p_j^e_j promítneme generátor do jednotlivých modulů.
Rovnost globálních stavů je ekvivalentní rovnosti všech složek.
Po čase max mu_j se proto posloupnost opakuje s periodou lcm lambda_j.
Každá její perioda musí být násobkem každé lambda_j, což dokazuje rovnost.
Stejná ekvivalence dává mu=max mu_j: dřívější vstup do globálního cyklu
by znamenal dřívější vstup ve všech složkách.

## Věta A a lemma R: plná perioda

Perioda je m právě když gcd(c,m)=1, každé prvočíslo p|m dělí a−1
a při 4|m také 4|a−1. Plný cyklus obsahuje 0, takže lze začít X_0=0.
Pak X_n=c S_n mod m, kde S_0=0 a S_n=1+a+...+a^(n−1).
Pokud c není jednotka, stav 1 nenastane. Podle Q stačí m=p^e.
Pro a=1 je S_n=n. Pro a=1 modulo liché p, nebo a=1 modulo 4 při p=2,
lemma P dává v_p(S_n)=v_p(n), tedy první návrat v čase p^e.
Modulo 2 má každé liché a požadovaný cyklus při lichém c.

Pokud p|a, S_n je vždy 1 modulo p. Pokud p nedělí a(a−1),
Fermatova věta dává S_(p−1)=0 modulo p, tedy periodu menší než p.
Pro a=3 modulo 4 a e>=2 je S_(2^(e−1))=0 modulo 2^e (úloha 8).
Všechny nepřípustné případy tedy selžou v některé složce.
Tím je dokázána A i obsah R; pro a=0 se konstantní zobrazení vyloučí přímo.
Je-li m součin různých prvočísel, zbývá pouze normalizovaný násobitel a=1.
Dlouhá perioda sama není kritériem statistické kvality, což úvod sekce říká.

## Věty B a C: multiplikativní perioda

```
L(1)=L(2)=1, L(4)=2,
L(2^e)=2^(e−2)                         pro e>=3,
L(p^e)=p^(e−1)(p−1)                    pro liché p,
L(product p_j^e_j)=lcm_j L(p_j^e_j).
```

Existence maximálního prvku modulo liché p plyne bez kruhu z úloh 15–16,
zdvih z úloh 12 a 14; binární případ z úlohy 11. Řády dělí uvedené L
a čínská věta sestaví prvek maximálního řádu ve všech složkách současně.
Při c=0 a nesoudělném X_0 je perioda ord_m(a). Obecné stavy nedají více:
při p|a složka po čase zanikne; při jednotce a a v_p(X_0)=f<e má periodu
ord_(p^(e−f))(a), která dělí L(p^e). Nulová složka má periodu 1.
Vzorec pro phi(p^(e−f)) na str. 20 se používá v nenulovém případě f<e.

Kritéria C: modulo 2 je a liché; modulo 4 je a=3; modulo 8 je a=3,5,7;
modulo 2^e, e>=4, je a=3 nebo 5 modulo 8. Pro liché p je a jednotka a
`a^((p−1)/q)!=1 mod p` pro všechna prvočísla q|p−1. Pro e>1 přibývá
`a^(p−1)!=1 mod p^2`. Primitivita v každé složce je postačující,
ne nutná pro primitivitu modulo součin, jak ukazuje úloha 17.

## Věta D: desetinný modul

Pro m=10^e, e>=5, je L(m)=2^(e−2) 5^(e−1)=5*10^(e−2).
Faktor 2^(e−2) musí dodat binární složka: řád modulo 5^e má nejvýše
dva faktory 2. Proto a=3 nebo 5 modulo 8. Faktor 5^(e−1) dostaneme
právě pro jednotky a modulo 5 s a^4!=1 modulo 25. Šestnáct zbytků je:

| Řád modulo 5^e | Zbytky modulo 25 |
|---|---|
| 4*5^(e−1) | 2,3,8,12,13,17,22,23 |
| 2*5^(e−1) | 4,9,14,19 |
| 5^(e−1) | 6,11,16,21 |

Spojení s oběma zbytky modulo 8 dává všech 32 čísel vytištěných na str. 21;
program porovnal celý uspořádaný seznam. Předpoklad e>=5 je podstatný:
pro e=4 může celý potřebný faktor 2^2 dodat složka modulo 5^e.

## Úlohy 1–8

**1.** a−1=3141592620 je násobek 20 a c=2718281829 je nesoudělné s 10.
Perioda je 10^10 pro každý X_0, tedy i uvedený 5772156648.

**2–3.** Binární podmínky jsou A; případ m=2 je vysvětlen výše.
Pro 10^e, e>=2, musí a−1 být násobkem 4 i 5, tedy 20. Podmínky na c
jsou přesně gcd(c,10)=1.

**4.** Označme h=2^(e−1). Plná perioda modulo h dává X_h=0 mod h,
plná perioda modulo 2h dává X_h!=0 mod 2h. Proto X_h=h.
Identita X_(n+h)=a^n X_h+X_n mod 2h a lichost a pak dávají
X_(n+h)=X_n+h mod 2h, včetně e=1.

**5–6.** [Certifikovaná tabulka](../results/modulus-table.json) ukazuje,
že 2^35+1 je součin pěti různých prvočísel, takže a=1.
Pro 10^6−1 je součin různých prvočísel 3*7*11*13*37=111111.
Všechna řešení jsou a=1+111111k, **0<=k<=8**, přesně jak stojí na str. 548.

**7.** Rovnost mu=max mu_j je výše. Pokud p nedělí a, zobrazení
je permutace a mu_j=0. Pokud p|a, má jediný pevný bod
z=c/(1−a) mod p^e; 1−a je jednotka. Rozdíl od z se násobí a,
takže zmizí nejpozději po e krocích. Meze mu=max e_j dosáhneme
s c=0, X_0=1 a a rovným součinu různých prvočísel dělících m.
Při čtvercově volném m použijeme jeho normalizovaný zbytek a=0.

**8.** Pro a=3 modulo 4 je v_2(a−1)=1 a a^2=1 modulo 8.
Čtvercováním dostaneme a^(2^(e−1))=1 modulo 2^(e+1) pro e>=2.
Dělení a−1 odebere právě jeden faktor 2, tedy 2^e dělí S_(2^(e−1)).
Jde o dělitelnost, nikoli tvrzení o nejmenší periodě.

## Úlohy 9–16

**9.** Dosazením X_n=4Y_n+1 do násobení 4c+1 vyjde
Y_(n+1)=(4c+1)Y_n+c mod 2^(e−2). Dosazením
X_n=(-1)^n(4Y_n+1) mod 2^e do násobení 4c−1 vyjde
Y_(n+1)=(1−4c)Y_n−c mod 2^(e−2). Liché c v obou případech
zaručuje větu A pro redukovaný generátor. Pro lichý počáteční stav
se zbytkem 3 modulo 4 se nejprve změní znaménko všech X, jak uvádí odpověď.
Sudým počátečním stavům se plná perioda nepřisuzuje. Poznámka o náhodnosti
je interpretací této ekvivalence, nikoli univerzální statistickou větou.

**10.** L(m)=phi(m) nastává pro 1,2,4,p^e,2p^e s lichým p.
Pro dvě různá lichá prvočísla se v součinu phi opakuje faktor 2,
který lcm nesčítá. Vyšší mocnina 2 má buď sama L<phi, nebo při spojení
s lichým prvočíslem opět způsobí opakovaný faktor 2. To vylučuje zbytek.

**11.** U lichého x>1 je právě jedno z x−1,x+1 dělitelné 4. Jeho
valuace f>1 určuje znaménko i f v x=2^f±1 mod 2^(f+1).
Při 1<x<2^e−1 je f<e. Pro x=1 modulo 4 dává P řád 2^(e−f).
Pro x=−1 modulo 4 má −x valuaci f po odečtení 1, zatímco x^2−1
má valuaci f+1. Řád x je tedy 2^(e−f), včetně f=e−1, kdy je 2.
Hodnoty x=1 a x=2^e−1 se ošetří zvlášť. Dostáváme binární případy C.
Erratum 2018 správně mění „maximum period“ na „maximum order“.

**12–14.** Má-li a modulo p řád d|p−1 a v_p(a^d−1)=f, P dává řád
modulo p^e rovný d p^max(0,e−f). Maximum vyžaduje d=p−1 a f=1.
Pro degeneraci a=1 je řád vždy 1; a^d−1=0 nehodnotíme valuací
nenulového čísla. Rovnost a^d=1 řeší přímo kongruence bez valuace nuly.
Pokud d<p−1, některé prvočíslo q|(p−1)/d dává
a^((p−1)/q)=1 modulo p, což je úloha 13. Pokud a je primitivní
modulo p, ale a^(p−1)=1 modulo p^2, binomický rozvoj dává

```
(a+kp)^(p−1) = a^(p−1)+(p−1)a^(p−2)kp mod p^2.
```

Pro 1<=k<p druhý člen není násobkem p^2. Všechny tyto zdvihy jsou
primitivní modulo každé p^e; zvlášť postačí a nebo a+p (úloha 14).

**15.** Jednotky tvoří komutativní grupu: násobení je asociativní,
má neutrální prvek a inverze a nezávisí na pořadí činitelů.
Z řádů r,s rozdělíme prvočíselné mocniny tak, aby maximální mocnina
každého prvočísla zůstala právě v jedné složce. Odpovídající umocnění
a_1,a_2 odstraní z druhé složky celou její mocninu tohoto prvočísla.
Nové řády R,S jsou nesoudělné a RS=lcm(r,s).
Součin komutujících prvků nesoudělných řádů má řád RS: jeho řád d
dělí RS; umocněním (uv)^d=1 na R dostaneme S|dR, tedy S|d,
a obdobně R|d. To je opravený důkaz z errat 2005.
Pokud řád nějakého prvku nedělí největší řád, tato konstrukce vyrobí
prvek ještě většího řádu. Tím je dokázána i část (b).

**16.** Nad zbytky modulo prvočíslo p lze dělit nenulovým prvkem.
Polynom f stupně n s kořenem a má rozklad f=(x−a)q modulo p
(odečtením f(a), nebo vytištěnou identitou). Jiný kořen f je kořenem q,
takže indukcí má nenulový polynom stupně n nejvýše n kořenů.
Podle úlohy 15 má x^L(p)−1 všech p−1 nenulových zbytků za kořeny.
Proto L(p)>=p−1, zatímco Fermat dává L(p)<=p−1. Existuje prvek
řádu p−1. Lagrangeova historická citace v erratech není předpokladem důkazu.

## Úlohy 17–21

**17–18.** Protože v_5(11−1)=1, má 11 řád 5^(e−1) modulo 5^e.
Modulo 2^e má řád 2^(e−2); lcm je L(10^e), přestože 11 není
primitivní modulo 5^e. Primitivní v obou složkách jsou ze seznamu D
přesně 3,13,27,37,53,67,77,83,117,123,133,147,163,173,187,197.
Důkaz D i tabulka tříd modulo 25 jsou výše.

**19.** [Výsledek](../results/multiplier-periods.json) obsahuje pro každý
z 92 modulů tabulky tři nejmenší násobitele >=2 s maximálním řádem,
hodnotu řádu a všechny jeho prvočíselné dělitele. Ověřujeme a^L=1 mod m
a a^(L/q)!=1 mod m pro každé prvočíslo q|L. Rozklady modulů i těchto q
mají dřívější rekurzivní certifikáty. Jde o vhodnost **z hlediska periody**;
malé násobitele tím neoznačujeme za statisticky kvalitní.
Odpověď odkazuje na řádky 17–20 tabulky §3.3.4:
[originál](../images/vol2-p106.png), m=2^31−1, a=314159269,62089911,16807,48271.
Maximální řády všech čtyř jsou přesně ověřeny v
[lagged-periods-small.json](../results/lagged-periods-small.json).
Spektrální hodnoty té pozdější tabulky zůstávají součástí kontroly §3.3.4;
zde uzavřená kontrola se vztahuje k periodám a správnosti tohoto odkazu.

**20.** Položme A=(a−1)X_0+c, Y_n=S_n a m'=m/gcd(A,m).
Identita X_n=A Y_n+X_0 mod m plyne z geometrického součtu a platí
i pro a=1. Dvě hodnoty X se rovnají právě když se odpovídající hodnoty Y
rovnají modulo m'. Proto mají stejnou periodu i délku počátečního úseku.
Na str. 549 je **správně m'**: vizuálně vyřešená pochybnost z OCR.

Modulo p^e: při p|a se Y ustálí na pevném bodě a perioda je 1.
Pro a=1 modulo p mimo binární výjimku dává A periodu p^e.
Pro jednotku a−1 je S_n=0 ekvivalentní a^n=1, takže perioda je ord_(p^e)(a).
Pro p=2,e>=2,a=3 modulo 4 je S_n=0 modulo 2^e ekvivalentní a^n=1
modulo 2^(e+1). Pokud a!=−1 modulo 2^e, P zdvojnásobí řád;
pokud a=−1 modulo 2^e, S_2=a+1=0 a perioda je přesně 2.

**21.** Pro plnou periodu, X_0=0, s=ord_m(a), je s ve složce p^e
mocninou p dělící p^e podle A a P. Globálně tedy s|m.
Dále X_(n+s)=X_n+X_s mod m a X_(qs)=q X_s mod m.
Nejmenší kladné q vracející nulu je m/s. Současně je tento aditivní
řád X_s roven m/gcd(X_s,m). Porovnání dává gcd(X_s,m)=s.

## Errata a výpočetní doklad

Prověřeny all2-prepre, all2-pre, all2, err2 i originální err2.textxt
ve stažení z 1. 11. 2026. Relevantní změny:

- str. 17: Greenbergerovy stránky 163–167 (3. 1. 2002), typografie
  „then“ (21. 5. 1998), označení začátku důkazu (13. 3. 2014);
- str. 18: doplnění „period of“ (26. 1. 2001);
- str. 20: typografie definice řádu (8. 11. 2005), kladnost nejmenšího
  exponentu a výslovná prvočíselnost p (13. 5. 2016);
- str. 548: „maximum order“ v odpovědi 11 (1. 11. 2018);
- str. 549: opravený důkaz odpovědi 15 (8. 11. 2005), historická
  Lagrangeova citace v odpovědi 16 (28. 3. 2005).

[Program](../verify_multiplier_periods.py) porovnává přímé trajektorie
s nezávislými algebraickými kritérii. Prošlo 278 784 trajektorií
i kontrol čínské věty, 6 447 případů C, 30 881 konstrukcí lcm řádů,
5 456 binárních substitucí, 1 198 373 hodnot v posunutých polovinách periody,
18 174 identit gcd(X_s,m)=s a 3 734 polynomů pro mez počtu kořenů.
Přesná tabulka 92 modulů a seznam D souhlasí. Konečné výčty doplňují
obecné důkazy, nenahrazují je. Nová chyba zde nebyla potvrzena.
Oprava důkazu úlohy 15 je známé erratum.

Bibliografická kontrola: [Hull–Dobell 1962](../sources/hull-dobell-1962.pdf),
str. 233, věta 1, skutečně uvádí tři postačující podmínky; stránka byla
také vizuálně přečtena. U Greenbergera potvrzují
[metadata vydavatele](../sources/greenberger-1961-crossref.json)
JACM 8(2), str. 163–167. Jeho plný text z ACM nebyl dostupný;
historické prvenství tím nově neprokazujeme. Matematický důkaz je vlastní.
