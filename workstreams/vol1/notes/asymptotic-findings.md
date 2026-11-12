# §1.2.11.3: čtyři opravy odpovědí

Kontrola 1. listopadu 2026. Vydání 3, první dotisk 1997. Originální
tištěné s. 122, 505–506 byly zobrazeny (strany souboru 137, 520–521).
Prohledány všechny čtyři řady errat i zdrojový `err1.textxt`, včetně
klíčových slov mimo původní stránkování. Relevantní změny jsou v
`sources/asymptotic-calculations-errata-extract.json`; aktuálnost zdrojů
dokládá `sources/errata-refresh-2026-11-01.json`. Níže uvedené opravy
v těchto podkladech nenalezeny. Prvenství ani fyzický výtisk neověřeny.

## V1-C0016: limita v odpovědi 4

Pro v≥r>0 označuje u kladné řešení rovnice v=u−ln(1+u).
Funkce na pravé straně je na u>0 ryze rostoucí, protože její derivace
je u/(1+u)>0, a roste do nekonečna. Proto u→∞ právě když v→∞.
Výraz 1+1/u tedy jde k **1**, nikoli k 0, jak říká první věta odpovědi.
Jeho omezenost a požadovaný odhad exponenciálního ocasu zůstávají správné:
`1+1/u(v) ≤ 1+1/u(r)` a integrál `∫_r^∞ x exp(−xv) dv=exp(−rx)`.
Stačí vyměnit slovo „zero“ za „one“. Jde o drobnou chybu zdůvodnění.

## V1-C0017: absolutní hodnota v odpovědi 8

Zde x→∞, f(x)=O(x^r), 0≤r<1, a m=ceil((s+2r)/(1−r)) je stupeň
Taylorova polynomu v exponentu. Odpověď definuje rozdíl R(x) dvou
integrálů s integrandy exp(−g) a exp(−h), kde
`g=u−x ln(1+u/x)` a `h=u²/(2x)−u³/(3x²)+…+(−1)^m u^m/(m x^(m−1))`.
Při odhadu absolutní chyby pak používá symetrický integrál
`∫_{−Mx^r}^{Mx^r} u^(m+1)/x^m du`. Ten je pro sudé m přesně nula.

Přípustná konkrétní volba je r=0, s=2, m=2, f(x)=1, M=1.
Pro u>0 platí `ln(1+u/x)>u/x−u²/(2x²)` (rozdíl má kladnou derivaci),
tedy g<h a exp(−g)>exp(−h). Proto R(x)>0 pro všechna x>1, zatímco
vytištěný integrál od −1 do 1 z u³/x² je nula. Výrok `R(x)=O(0)`
by nutil R být od jistého x identicky nulové.

Správný integrand je **|u|^(m+1)/x^m**. Taylorův zbytek je jím
rovnoměrně omezen na |u|≤Mx^r, protože Mx^r/x→0. Pro m≥2 je h≥0:
pro u<0 jsou všechny členy kladné, pro u>0 je to alternující součet
klesajících kladných velikostí, začínající kladně. Také g≥0, a proto
`|exp(−g)−exp(−h)|≤|g−h|`. Integrace dává
`|R|=O(x^((m+2)r−m))=O(x^(−s))`, jak požaduje zadání.
Pokud z volby parametrů vyjde m=1, je h=0 (prázdný součet) a stejný
argument s g=O(u²/x) platí. Pro m=0 a s≤−2r stačí triviální O(x^r).
Obvyklý požadavek s>0 žádné záporné m nepřipouští.
Věta samotná tedy platí; chyba je v jednom kroku důkazu.

## V1-C0018: chybějící exponenciální člen Q_x(n) pro záporné x

Pro celé n≥1 jsou funkce v úloze 11 definovány

```text
Q_x(n) = sum_{k=0}^{n−1} (n−1)!/(n−1−k)! · (x/n)^k,
R_x(n) = sum_{k≥0} n!/(n+k)! · (nx)^k.
```

Druhá řada konverguje pro každé reálné x. Rozdělení exponenciální řady
na prvních n členů a zbytek dává pro x≠0 přesnou identitu, kterou
správně uvádí i první řádek odpovědi 11:

`x Q_x(n)+R_(1/x)(n)=n! (x/n)^n exp(n/x)`.

Na s. 506 však větev označená x<1 tvrdí mimo jiné
`Q_x(n)=1/(1−x)+O(1/n)`. Volme **x=−4**. Řada R_(−1/4)(n)
je alternující, první člen je 1 a poměr sousedních absolutních hodnot
je n/[4(n+k+1)]<1/4. Odtud
`3/4 < R_(−1/4)(n) < 1` pro každé n≥1.
Přitom výraz `E_n=n!(−4/n)^n exp(−n/4)` má velikost rostoucí
exponenciálně. Skutečně

```text
ln(n!) ≥ integral_1^n ln(t) dt ≥ n ln n − n,
|E_n| ≥ (4 exp(−5/4))^n,
4 exp(−5/4) > 1, protože e<3 a e^5<243<256=4^4.
```

Z identity `Q_(−4)(n)=(R_(−1/4)(n)−E_n)/4` plyne, že podél sudých n
jde Q_(−4) k −∞ a podél lichých k +∞. Nemůže tedy mít tvrzenou limitu 1/5.
Jde o chybu samotného asymptotického výsledku, nejen jeho odvození.

**Oprava pro každé pevné x<0:** k algebraickému rozvoji Q_x(n) je nutno
přidat `T_x(n)=n! x^(n−1) exp(n/x)/n^n`, tedy týž člen jako ve větvi x>1.
Rozvoj R_x pro x<1 lze ponechat. Přímý důvod poskytují přesné integrály

```text
R_x(n) = n integral_0^1 exp(nxt) (1−t)^(n−1) dt,
Q_x(n) = integral_0^infty exp(−t) (1+xt/n)^(n−1) dt.
```

Pro x<0 rozdělíme druhý integrál v t=−n/x. Část za tímto bodem je přesně
T_x(n); část před ním je `−R_(1/x)(n)/x`. První integrál má pro x<1
maximum exponentu v levém krajním bodě a dává standardní rozvoj v 1/n.
Transformace `−R_(1/x)/x` dává právě vytištěné polynomy q_m:
jestliže `r_m(x)=sum_j A(m,j)x^(j+1)`, pak
`q_m(x)=x^(2m)r_m(1/x)=sum_j A(m,j)x^(2m−1−j)`.
Čísla A(m,j) jsou Eulerova čísla druhého řádu, definovaná v poznámce
`asymptotic-parameters.md`; zde je důležitá pouze uvedená vzájemná identita.

Po doplnění T_x lze zachovat i tvrzení o konstantě v O-členu nezávislé
na x<0; důkaz rovnoměrnosti je v téže poznámce. Bez T_x toto tvrzení
samozřejmě selhává už pro jediné pevné x=−4. V okolí x=−1 je T_x
exponenciálně malé, takže závěrečný zvláštní případ x=−1 zůstává správný.

## V1-C0019: znaménko v odpovědi 12

Zadání na s. 122 neomezuje x na nezáporné hodnoty. Funkce
`I(x)=∫_0^x exp(−t²/2) dt` je lichá a I(x)<0 pro x<0.
Vytištěná odpověď `γ(1/2,x²/2)/sqrt(2)` je naproti tomu sudá a kladná
pro x≠0. Například pro x=−1 mají obě strany opačná znaménka.
Definice γ(a,y)=∫_0^y exp(−t)t^(a−1)dt má zde a=1/2,y=x²/2>0,
takže nejde o spor způsobený volbou komplexní větve.

Substituce t²/2 přímo dává správnou odpověď
`I(x)=sgn(x) γ(1/2,x²/2)/sqrt(2)`, s I(0)=0. Funkce sgn(x) je
1 pro x>0, −1 pro x<0 a 0 pro x=0. Alternativně lze do zadání
doplnit x≥0. Odkaz na normální rozdělení sám x≥0 nestanoví.
