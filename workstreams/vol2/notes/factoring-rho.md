# §4.5.4: Pollardovo rho, úlohy 4 a 21

Audit 3. listopadu 2026. Kniha, 3. vydání, první dotisk: str. 385–386,
412–413, odpovědi 657–658 a 661, všechny vizuálně přečteny.
Algoritmus B a konečné pravděpodobnostní meze jsou správné. Konstanty
v poznámce k úloze 4 platí v uvedené aproximaci; pevný rozvrh mocnin dvou
má drobné oscilace, které nelze zaměnit za jedinou asymptotickou konstantu.
Výzkumná úloha 21 je auditována jako výzkumná otázka, nikoli vyřešena.
Nový nález v tomto bloku není.

Úplně přepočtena původní experimentální tvrzení pro prvočísla pod milionem.
Rozšíření z errat na miliardu bylo dokončeno 3. listopadu 2026;
nezávislé síto potvrdilo počty všech999nových úseků. Oba rekordy i
mez16sqrt(p) souhlasí. Přesný rozsah kontroly a výsledky jsou v §9.

## 1. Iterace a invariant algoritmu B

Pišme `f(x)=x²+1`, `x_0=2`, `x_(j+1)=f(x_j)`. Tyto celočíselné
iterace jsou jen definicí; implementace je počítá modulo nezpracovaný
zbytek čísla. Pro každý dělitel p čísla N platí
`(f(x) mod N) mod p = f(x mod p) mod p`. Indukce dává vztah (11).
Stejný argument platí pro každý polynom s celočíselnými koeficienty.

Definujme `ell(m)` jako největší mocninu dvou nejvýše m. Před krokem B3
je n dosud nerozložený zbytek, `x ≡ x_m (mod n)`,
`x' ≡ x_(ell(m)-1) (mod n)`, `l=ell(m)` a `k=2l-m`.
Součin n a dosud vypsaných faktorů je N. Inicializace vyhovuje;
počáteční x=5 nemusí být kanonickým zbytkem pro malá N, ale kongruence
stačí. Při snížení k na nulu je m=2l-1: staré x se stane novou kotvou,
l se zdvojnásobí a následující umocnění vytvoří x_(m+1).
Jinak se mění jen m a k o jednotku opačnými směry.

Je-li `g=gcd(x'-x,n)>1`, jde vždy o skutečný dělitel n. Při g<n
se invariant zachová po dělení n a redukci obou zbytků. B2 korektně
ukončí výpočet prvočíselným zbytkem; B3 při g=n výslovně hlásí neúspěch.
Složený vypsaný g není certifikované prvočíslo a kniha požaduje jeho test.

Proč tentýž algoritmus složený g nerozloží: po každém dřívějším zásahu
prvočísla q krok B3, opakovaný bez posunu m, odstraní všechny jeho
zbývající mocniny (nebo B2 ukončí celý výpočet). Žádné prvočíslo
aktuálního g tedy nemělo dřívější zásah. Při samostatném běhu na g
jsou dřívější gcd rovny 1 a v nynějším kroku je rozdíl dělitelný celým g.
Výsledek je g=n a neúspěch. Pomoci může jiný polynom, počáteční bod
nebo metoda, nikoli opakování stejného B.

Pro konečnou posloupnost definujme mu jako délku neperiodického začátku
a lambda>=1 jako délku následujícího cyklu. Položme t=mu+lambda.
Z důkazu v [intro-cycles.md](intro-cycles.md) plyne první detekce

```
L = nejmenší mocnina 2 >= max(mu+1, lambda),
T = L - 1 + lambda.                                      (R1)
```

Kotva musí ležet v cyklu, tedy L-1>=mu, a blok musí pojmout lambda
posunů. To také dokazuje minimalitu L. Modulo p je t<=p a T<3t,
takže detekce vždy nastane v konečném čase. Její rychlost řádu sqrt(p)
pro konkrétní f je další, heuristický předpoklad, ne důsledek konečnosti.

V příkladu N=25852 dostáváme 4 při m=3, 23 při m=9 a zbytek 281.
Mezi oběma faktory je šest posunů B4, ale sedm dalších volání B3:
jedno je okamžitě opakováno po dělení čtyřmi. Knižní popis je správný.
První vlastní test zaměnil tyto počty; jeho neúspěšný log je zachován.

## 2. Úloha 4: přesná konečná mez

Nyní je f rovnoměrně náhodné zobrazení množiny m prvků do sebe.
Definujme `p_j=prod_(k=1..j)(1-k/m)` a
`Q(m)=sum_(j=0..m-1) p_j`. Předchozí audit náhodných zobrazení
v [intro-random-maps.md](intro-random-maps.md) dokazuje

```
P(mu=a, lambda=b) = p_(a+b-1)/m,  a>=0, b>=1, a+b<=m;
E(t)=Q(m),  E(lambda)=(Q(m)+1)/2.                         (R2)
```

Při pevném t=s sečtěme L z (R1) přes lambda=1,...,s; součet označme
F(s), aby se nepletl s iterovaným polynomem f. Je-li
`q=2^floor(log2(s))`, mají `2q-s` možností hodnotu L=q
a zbývající `2(s-q)` možnosti hodnotu L=2q. Proto

```
F(s)=q(3s-2q)=s² h(theta),
theta=log2(s)-floor(log2(s)),
h(theta)=3*2^(-theta)-2*2^(-2theta).                       (R3)
```

Kvadratický polynom `3u-2u²`, `1/2<=u<=1`, má minimum 1
a maximum 9/8 v u=3/4. Z (R2) tak plyne
`Q(m)<=E(L)<=9Q(m)/8`. Dosazení do `T=L-1+lambda` dává přesně

```
3Q(m)/2 - 1/2 <= E(T) <= 13Q(m)/8 - 1/2.                 (R4)
```

To dokazuje požadavek úlohy i silnější formulaci s konstantním členem.
Argument nepotřebuje asymptotiku ani rovnoměrné rozdělení theta.
Vlastní nezávislé součty ověřily (R3) pro 512 hodnot a (R4)
pro všech 96 prvních m s přesnými racionálními pravděpodobnostmi.

## 3. Význam přibližných konstant

Označme `C=sqrt(pi/2)`, kde pi je kruhová konstanta, a ln přirozený
logaritmus. Průměr h(theta) přes rovnoměrnou theta v [0,1] je
`3/(4 ln 2)`. Model s takto zprůměrovanou logaritmickou fází dává
koeficient `(3/(4 ln 2)+1/2)C = 1.98276963659...` před sqrt(m).
Brentův článek z roku 1980 tento dodatečný náhodný posun fáze zavádí
explicitně. Kniha píše „approximately“ a známá oprava z 22. května 2015
navíc mění = a ~ na přibližné rovnosti v obou číselných výrazech.

Pevná fáze není asymptoticky rovnoměrná. To lze doložit přímo z (R2–R3),
bez simulace. Je-li `a` zlomková část log2(sqrt(m)), subsekvenční limita
`E(T)/sqrt(m)` při pevné a je

```
H(a)=C/2 + sum_(j in Z) integral_(q_j)^(2q_j)
                              q_j(3x-2q_j) exp(-x²/2) dx,
q_j=2^(j-a).                                             (R5)
```

Riemannovy součty přejdou k integrálu, protože
`p_(s-1) -> exp(-x²/2)` pro s/sqrt(m)->x. Dominaci na ocase dává
`p_(s-1)<=exp(-s(s-1)/(2m))` a `F(s)<=9s²/8`.
Integrál v (R5) je

```
3q(exp(-q²/2)-exp(-2q²))
 - 2q² C (erf(sqrt(2)q)-erf(q/sqrt(2))),                 (R6)
```

kde `erf(z)=2/sqrt(pi) integral_0^z exp(-u²)du`.
Sečteny byly intervaly j=-50,...,5. Dolní vynechaný ocas je nejvýše
`3b³/8`, b=2^(-50-a); horní nejvýše
`(9/8)(B+1/B) exp(-B²/2)`, B=2^(6-a), integrací per partes.
Intervalová aritmetika Arb při 90 desetinných místech dokazuje

```
H(0)   = 1.98239280973714171854...   (m=4^j),
H(1/2) = 1.98314591294982762128...   (m=2*4^j).
```

Obaly jsou disjunktní; chyby ocasů jsou pod 3e-46. Proto by tvrzení
o jediné přesné limitě bylo nepravdivé. Současná knižní aproximace
takové tvrzení nedělá a toto pozorování není nový nález.
Optimální zobecněný poměr 2.4771366 a konstanta 1.92600 už byly
ověřeny v `results/brent-optimum.json`; úspěšný výpočet se neopakoval.

## 4. Vynechání první poloviny bloku a Floydovo srovnání

První test při m=1 se zachová. V následujících blocích se B3 provádí
jen při `k<=l/2`; jde o známou Brentovu úpravu, jejíž připsání Cohenovi
opravují errata z 14. května 1998. Pro (mu,lambda)!=(0,1) položme

```
L=next_power_of_two(max(mu+1,lambda,2)), h=L/2,
delta=lambda*ceil((h+1)/lambda).
```

První úspěch je při `m=L-1+delta`, počet gcd testů včetně prvního je
delta a počet kroků bez gcd je L-1. Pro (0,1) nastane úspěch hned
v prvním testu. Oproti (R1) je přírůstek
`ell(mu)-(ell(mu) mod lambda)`, s konvencí ell(0)=0:
pokud lambda>L/2, není co přidávat; jinak mu>=L/2 a ell(mu)=L/2.
Nezávislá posloupnost značek ocasu a cyklu ověřila všech 16384 párů
0<=mu<128, 1<=lambda<=128 včetně počátečního pevného bodu.

Následující asymptotické koeficienty patří opět modelu s náhodnou fází.
Škálované mu a lambda mají společnou hustotu
`exp(-(mu+lambda)²/2)` na kladném kvadrantu. Pak
`E(lambda)=C/2`, `E(L)=3C/(4 ln 2)` a

```
E(delta)=C/2 + C/(2 ln 2) sum_(k>=1)
                    integral_k^(2k) dv/[v(1+v)²].        (R7)
```

Například (R7) plyne ze
`delta=lambda+lambda*sum_(k>=1)[L>2k lambda]` po integraci
náhodné fáze a substituci v=mu/lambda; hranaté závorky jsou indikátor.
Integrál je
`ln(2(k+1)/(2k+1))+1/(2k+1)-1/(k+1)`. Součet logaritmů do K
je `ln(4^K K!(K+1)!/(2K+1)!)`, součet druhých členů
je `H_(2K+1)-3H_K/2-1/(K+1)`, kde H_K je harmonický součet.
Stirlingův vzorec a `H_K=ln K+gamma+o(1)`, s Eulerovou konstantou gamma,
dávají celkovou limitu `(ln pi-gamma)/2`. Tedy počet kroků bez gcd
má koeficient 1.35611256794... a s gcd 0.88319479116...,
jak je vytištěno.

Pro Floydovu metodu je první detekční index nejmenší kladný násobek
lambda nejvýše mu+lambda a alespoň mu. V témže spojitém limitním
modelu lze psát `J=lambda+lambda*sum_(k>=1)[mu>k lambda]`;
hranice mají nulovou míru. Integrace dává
`E(J)/C=1/2+sum_(k>=1)1/(2(k+1)²)=pi²/12`.
Proto koeficient gcd je 1.03080956047... a počet umocnění má trojnásobek
3.09242868140.... Porovnání s původním B dává poměr ceny gcd/umocnění
`(3F-B)/(B-F)=1.16565712432...`, kde F=1.03080956... a B=1.98276964....
Knižní zaokrouhlení 1.17 je správné. Všechna uvedená zaokrouhlení
byla certifikována intervalovou aritmetikou.

## 5. Experimenty a hranice interpretace

`verify_factoring_rho_census.cpp` pro každé z 78498 prvočísel pod 10^6
počítá m(p) dvěma metodami: přímo dyadickým detektorem a nezávisle
tabulkou první návštěvy každého stavu, z níž získá mu,lambda a (R1).
Python následně nezávislým sítem ověřuje úplnost seznamu, oba extrémy,
nerovnost `m(p)²<144p` a všech deset tištěných dvojic z tabulky 386.
Největší m je 7685 u p=874771; největší poměr m/sqrt(p) je u
p=290047, m=6251. Součet všech m je 100343902.

Odděleně byly přímo potvrzeny obě hodnoty nového experimentu:
m(850112303)=416784, m(695361131)=406244; obě p jsou nezávisle
ověřená prvočísla. To samo nedokazuje jejich globální extremalitu do 10^9.
Tu spolu s mezí 16sqrt(p) již potvrdil dokončený segmentovaný přepočet (§9).
Definice m(p) je počet iterací detektoru: doslovný B spuštěný na prvočísle
p by skončil již v B2. Takto je experiment v knize míněn.

Odhady počtu iterací pro „almost all“ 12/18ciferná čísla jsou
modelové praktické odhady, nikoli kvantifikované věty o všech vstupech.
Podobně odhad pomocí druhého největšího prvočinitele na385
neřeší výjimečné společné detekce či opakované faktory uniformní zárukou.

Gcd ze součinu několika rozdílů zachytí každý prvočinitel, který dělí
některý rozdíl. Lze tedy dávkovat deset testů a devět gcd nahradit
modulárními násobeními. Při výsledku n může být potřeba projít dávku
znovu jednotlivě; tvrzení o jen malém nárůstu neúspěchu je empirické.
Počáteční vynechání testů je rovněž praktická varianta, ne záruka
rychlosti bez předpokladů o rozdělení faktorů.

Výjimky c=0,-2 mají algebraický důvod: pro c=0 je
`x_j=A^(2^j)`; pro c=-2 a A=r+r^(-1) je
`x_j=r^(2^j)+r^(-2^j)`. Druhou identitu dokazuje umocnění a odečtení 2;
r lze vzít v kvadratickém rozšíření konečného tělesa. Nejde obecně
o nezávislé náhodné hodnoty. „Slightly better than random“ u kvadratické
mapy na385 je výslovná heuristika; citace Arney–Bender doplněná roku1998
se týká modelu zobrazení s omezenými počty vzorů.

## 6. Fermatovo číslo a primární zdroje

Pro `F_8=2^256+1` byl nezávisle ověřen dělitel
`p=1238926361552897` a dokázána jeho prvočíselnost. Použit úplný
certifikát faktorizace n-1: svědek a splňuje `a^(n-1)=1 mod n`
a pro každý prvočinitel q čísla n-1 také
`gcd(a^((n-1)/q)-1,n)=1`. Pro každý prvočinitel r čísla n pak řád a
modulo r obsahuje všechny mocniny z n-1; tedy n-1 dělí r-1 a r>=n.
Tím je n prvočíslo. Konkrétní certifikáty:

```
3853149761 - 1 = 2^6 * 5 * 719 * 16747, svědek 6;
p - 1 = 2^11 * 157 * 3853149761, svědek 3.
```

Malá prvočísla jsou ověřena úplným zkoušením dělitelů.
Druhý, 62ciferný faktor F_8 je spočten přesným dělením, ale jeho
prvočíselnost tento vlastní výpočet netestoval: knižní tvrzení na386
vyžaduje jen prvočíselnost uvedeného p. Brent1982 podává i jeho certifikát;
jeho tabulka byla přečtena, nikoli celá nezávisle přepočtena.

Primární zdroje a přesný rozsah čtení:

- [Pollard1975](https://pages.cs.wisc.edu/~cs812-1/pollardrho.pdf),
  všechny str.331–334: původní metoda, náhodný model, dávkování,
  výjimky c=0,-2. Citace BIT15,331–334 sedí.
- [Brent1980](https://maths-people.anu.edu.au/~brent/pd/rpb051i.pdf),
  všechny str.176–184: explicitní náhodná fáze, optimalizace,
  §7 vynechání první poloviny bloku a §8 Guyova otázka.
- [Brent–Pollard1981](https://maths-people.anu.edu.au/~brent/pd/rpb061.pdf),
  všechny str.627–630: skutečná modifikace polynomu, nalezený faktor,
  výpočet roku1980. Bibliografie a tvrzení knihy odpovídají.
- [Brent1982](https://maths-people.anu.edu.au/~brent/pd/rpb066.pdf),
  všechny str.253–255: certifikáty obou faktorů a podpůrných prvočísel.

## 7. Výzkumná úloha 21

Guyova požadovaná mez `m(p)=O(sqrt(p log p))` je silnější než
obecná konečná mez z (R1). Z experimentu do milionu ani miliardy
neplyne důkaz pro všechna prvočísla. Knižní odpověď na661 pouze odkazuje
na relevantní teorii Erica Bacha; netvrdí, že otázku řeší.

Bachova bibliografie byla potvrzena u
[vydavatele](https://www.sciencedirect.com/science/article/pii/089054019190001I):
Information and Computation90(1991),139–155,
DOI10.1016/0890-5401(91)90001-I. Abstrakt dokládá, že jde právě o
pravděpodobnost úspěchu rho; plné původní PDF nebylo dostupné (403).
Nečitelným OCR z cizího zrcadla nenahrazujeme kontrolu úplného důkazu.
Tento externí důkaz není v auditu reprodukován ani prohlášen za přečtený.

[Heath-Brown2017](https://arxiv.org/abs/1701.02707), v2,
byl vizuálně přečten na str.1–5 včetně věty1 a důsledku2.
Pro pevné kladné celočíselné A,C dává pro `AX²+C` délku každého ocasu
a celkovou délku cyklů `O(p/log log p)`. Aplikace A=C=1 a (R1)
dává stejnou horní mez pro m(p); to je vlastní jednoduchý převod
externí věty, nikoli nový důkaz jejího jádra. Celý článek přečten nebyl.
Tato mez Guyův požadavek nesplňuje.

V primárním preprintu
[Rudolph2025](https://arxiv.org/abs/2506.12844), v1, byly přečteny
str.1–2 a15: hlavní rychlostní odhad je výslovně podmíněn Heuristic1,
tedy nahrazením iterované mapy náhodným zobrazením. Preprint není
důkazem požadavku úlohy21; §7.3 také správně odkazuje na Bachovu teorii.
Rešerše provedena 3. listopadu 2026. Nenašla řešení Guyovy otázky,
ale neúplnost rešerše nedokazuje její aktuální nevyřešenost.

Úloha21 je tedy uzavřena **jako audit výzkumné formulace a odpovědi**,
s vlastní obecnou konečnou mezí, přesnými experimenty a doloženým
rozsahem novějších výsledků. Není uzavřena jako vyřešený otevřený problém.

## 8. Reprodukce a evidence

`verify_factoring_rho.py` dokončil šest bloků: 49999 vstupů B,
512 součtů a96 přesných očekávání,16384 párů pro vynechávání,
validaci celého malého censu, prvočíselné certifikáty a intervalové
konstanty. Zaznamenáno1424 očekávaných terminálních neúspěchů B;
všech83 různých složených výstupů při opakování stejného B selže
podle důkazu v §1. Nejde o1424 chyby knihy.

První vlastní chybný test počtu volání B3 je v
`results/factoring-rho-initial.log`. Opravený běh:
obal PID1260961, Python PID1260962, session42767, limit180s,
exit0,3.259737991s. Úplný malý census: session46245, exit0,
PID tohoto krátkého běhu nebyl zachycen. Zdroje, hashe a vymezení
dlouhého běhu jsou v `sources/factoring-rho.json` a `RUN_STATE.json`.

Všechny čtyři vrstvy errat byly prohledány. Uplatněny opravy385
(Arney–Bender1998),386 (experiment2000),658 (Brentova priorita1998,
přibližné rovnosti2015). Výpočet nového experimentu byl následně uzavřen v §9. Historické komentáře k Fermatovu sítu387–390 ani
zbývající části §4.5.4 se touto poznámkou neuzavírají.

Doplnění 3. listopadu: Arney–Bender1982 získán od vydavatele;
vizuálně přečteny269–273 (PDF2–6), definice a tabulky náhodných map.
Potvrzuje relevanci citace v erratu385; další důkazy článku nepřečteny.
Podrobnosti a odkaz v [factoring-distribution.md](factoring-distribution.md#9-primární-a-bibliografické-podklady).

## 9. Dokončený census pod miliardou

Běh [verify_factoring_rho_extended.cpp](../verify_factoring_rho_extended.cpp)
zpracoval všech999po sobě jdoucích intervalů `[10^6,2*10^6)`, …,
`[999*10^6,10^9)`. [CSV](../results/factoring-rho-extended.csv) uchovává
počty prvočísel, součty iterací, oba lokální rekordy, kontrolní otisky
a časy; [log](../results/factoring-rho-extended.log) končí potvrzením
všech segmentů. Nový rozsah obsahuje **50769036 prvočísel**.

Nezávislý [program](../verify_rho_prime_counts.cpp) používá jediné síto
lichých čísel v celém rozsahu, zatímco dlouhý běh používal segmentované
síto všech čísel. Přesné počty souhlasí v každém z999intervalů.
Tato kontrola trvala7.02155s a **nepočítala žádnou Pollardovu iteraci**.
Prvočísla pod milionem i jejich iterace byla již nezávisle ověřena v §5.

[Souhrnný validátor](../verify_rho_aggregate.py) kontroluje souvislé
pokrytí, všechny počty a přesné porovnání lokálních rekordů. Spolu
s dřívějším rozsahem tak dostáváme:

```
počet prvočísel p < 10^9:             50847534
součet všech m(p):                    2086324158209
maximum m(p):                        416784 při p=850112303
maximum m(p)/sqrt(p):                 406244/sqrt(695361131)
čtverec posledního poměru:            165034187536/695361131 < 256
```

Poslední řádek je přesná celočíselná kontrola globální meze
`m(p)<16sqrt(p)`. Poměr je přibližně15.40571127257629; zaokrouhlení
se při rozhodování nepoužívá. Jedinečnost míst dosažení rekordů
netvrdíme, protože souhrny neukládají seznam všech případných shod.

Popisný poměr `sum_p m(p) / sum_p sqrt(p)` vyšel přibližně
**1.9825438081**, v souladu s knižním „about2sqrt(p)“. Není to
průměr jednotlivých poměrů `m(p)/sqrt(p)` ani důkaz asymptotiky.
Odmocniny a tento popisný podíl jsou plovoucí aproximace; přesný počet,
součet, rekordy a mez na nich nezávisí. Dvě implementace součtu
odmocnin (double a longdouble) se na jednom segmentu lišily nejvýše
0.00002821342.

Dlouhý běh počítal nové iterace jednou. Správnost dyadického detektoru
plyne z invariantu a (R1) v §1; dřívější nezávislý detektor prověřil
všech78498prvočísel pod milionem. Pro celý nový rozsah netvrdíme dva
nezávislé výpočty každé iterace. Výsledné globální rekordy navíc souhlasí
s externím experimentem Oliveiry e Silvy v erratu z28.prosince2000.

Při kontrole implementace ověřeno, že `x*x+1<10^18` pro nový rozsah
vejde do64bitového bezznaménkového slova. Pro porovnání poměrů
`m1²*p2` versus `m2²*p1` program používá128bitovou aritmetiku;
pythonový souhrn libovolně velká celá čísla. Síto obsahuje všechna
potřebná prvočísla do sqrt(10^9). Souhrnný validátor znovu žádné
úspěšné iterace nepočítal.

Součet časů999úseků je **26796.612924714s**, asi7h26min37s.
PID1260603, dítě1260604, session15357, limit28800s. Obal výslovně
vypsal `extended census exit 0`; nástroj při pozdějším vyzvednutí
vrátil143. Tento rozdíl nepřepisujeme na údaj o selhání aritmetiky:
všech999checkpointů, terminální log a následná nezávislá kontrola
jsou kompletní. Běh se neopakoval. Kontrolní síto: PID1317745/1317746,
session75977, limit180s, exit0. [Souhrnný JSON](../results/rho-aggregate.json)
obsahuje otisky všech vstupních dat.
