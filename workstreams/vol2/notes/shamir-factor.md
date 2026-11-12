# §4.5.4-40: faktorizace v jednotkovém aritmetickém modelu

> Sekvenční doplnění6.11.2026: celá40 je nyní partial kvůli nevyřešeným závěrečným výzkumným otázkám. Hlavní konstrukce a její čas jsou dokázané.

Zadání416 a odpověď666 byly vizuálně přečteny. Hlavní tvrzení
o O(log n) krocích je správné; níže je vlastní úplná konstrukce
s pevným počtem registrů. [C0176](C0176-shamir-fibonacci-invariant.md)
dokládá chybný invariant ve vytištěné Fibonacciho variantě, nikoli
nepravdivost hlavního výsledku.

## 1. Model a balení koeficientů

Registr obsahuje jedno celé číslo bez omezení velikosti. Jednotkový
krok znamená jeden součet, rozdíl, součin nebo podlahu podílu;
větvení smí používat rovnost. Zbytek získáme jako
`x mod y=x-y*floor(x/y)`. Pro nenulové vstupní n získáme konstanty
0=n−n,1=floor(n/n),2=1+1. Test x>0 lze provést takto:
nejprve přijmout x=1, jinak testovat `floor(x/(x-1))!=0`.
Pro x<=0 je tento podíl v[0,1), pro x>=2 je nejméně1.
Větvení před dělením ošetří nulový jmenovatel při x=1.

Jsou-li všechny koeficienty polynomu P nezáporné a menší než A,
pak koeficient u z^j je přesně `floor(P(A)/A^j) mod A`.
Pro P(z)=(1+z)^q stačí A>2^q, neboť součet koeficientů je2^q.
Tím se v jediném velkém čísle uchová celý řádek Pascalova trojúhelníku.
Není to předpoklad bezplatného exponentování: potřebné mocniny
se budou aktualizovat jednotlivými povolenými operacemi.

## 2. Faktoriál v O(log n) krocích

Zaveďme `ell=floor(log_2 n)` a `k=2^ell`. Při opakovaném dělení
n dvěma současně zdvojujeme k a umocňujeme A na druhou.
Z počátečního A=4 dostaneme `A=2^(2^(ell+1))>2^n`.
Udržujeme pro dosavadní binární prefix m čísla n invariant

```
t=A^m, u=(A+1)^m, v=m!.                               (1)
```

Zdvojení m stojí konstantně mnoho kroků: nejprve u←u²,
potom `v←(floor(u/t) mod A)*v²`, nakonec t←t².
Vybraný koeficient je binom(2m,m), takže nové v je(2m)!.
Případné přičtení následujícího bitu1 se provede aktualizací
`m←m+1,t←At,u←(A+1)u,v←vm`. Bit získáme z
`floor(n/k) mod2` po k←floor(k/2). Všechny zpracované exponenty
jsou nejvýše n, takže nevzniká přenos mezi bloky v základu A.
Po ell kolech je m=n. Registrů je pevný počet a operací O(log n).

## 3. Který faktoriál odhalí faktor

Označme `h(n)=min{j>=1:n|j!}`. Existuje, protože n|n!.
Minimalita vynutí `gcd(h(n),n)>1`: invertibilita h(n) modulo n
by jinak dala n|(h(n)−1)!. Pro prvočíslo n je h(n)=n.
Pro složené n>4 platí dokonce h(n)<=n−2:
jestliže n=ab,2<=a<b, pak oba různé faktory leží v2,...,n−2;
jestliže n=a²,a>=3, stačí různé členy a a2a, jejichž součin
je násobkem n a oba jsou nejvýše n−2. Výjimka n=4 má h(4)=4.
Proto gcd(h(n),n) dává vlastní faktor každého složeného n!=4.

Pro rychlé hledání nejprve použijeme základ
`A=2^(2^(ell+2))>2^(2n)`, získaný stejným postupem z A=16.
Zdvojováním podle §2 počítáme postupně faktoriály mocnin2,
až najdeme b=2^k splňující

```
b! mod n !=0, (2b)! mod n=0.                           (2)
```

Platí b<h(n)<=2b a b<n. Tento průchod stojí O(log n) kroků
a nechá k dispozici `T=A^b,U=(A+1)^b,b!`.
Pokud g=gcd(n,b!)>1, je g<n díky(2), a skončíme.
Euclidův algoritmus stojí O(log n) aritmetických kroků: první
zbytek může mít obrovský dělenec, ale další čísla jsou nejvýše n.
Tato větev řeší i n=4.

Zbývá případ gcd(n,b!)=1. Pro každé celé0<=z<=b jsou z! i(z!)²
invertibilní modulo n, takže

```
n | binom(2z,z)  právě když  n | (2z)!.                (3)
```

V tomto intervalu je test monotónní: po prvním úspěchu už
zůstává úspěšný. První úspěšná hodnota je
`z_0=ceil(h(n)/2)` a leží v(b/2,b]. Mimo tento interval
se ekvivalence(3) a monotónnost nesmějí předpokládat.

## 4. Bezpečná Fibonacciho inicializace a sestup

Fibonacciho čísla jsou F_1=F_2=1, F_(j+1)=F_j+F_(j-1).
Postupným sčítáním najdeme sousední s=F_j,s'=F_(j+1)
tak, aby `s<=b<s'`. Současně násobením udržujeme

```
t=A^s, t'=A^s', u=(A+1)^(2s), u'=(A+1)^(2s').         (4)
```

Zvolme **m=b−s**. Jelikož s'>b a s'<=2s, je m<b/2<z_0.
Horní konec m+s=b je známý úspěch. Mocniny
`v=A^m=T/t` a `w=(A+1)^(2m)=U²/u` získáme přesným dělením.
Tím je celá inicializace provedena v O(log n) krocích,
včetně případů m=0 a b=1.

Pro pohodlný důkaz rozšiřme test na všechna z>=b hodnotou true.
Na0,...,b se vyhodnocuje(3). Rozšířený test je monotónní
a jeho první úspěch z_0 se nezmění. Nikdy není nutné extrahovat
binomický koeficient s indexem větším než b.

Udržujeme `m<z_0<=min(m+s,b)`. Pro s>1 přejdeme o Fibonacciho
stupeň zpět, s pravými stranami vždy ze starého stavu:

```
(s,s') <- (s'-s,s),
(t,t') <- (t'/t,t), (u,u') <- (u'/u,u).                (5)
```

Pak zkoušíme z=m+s. Pro z>=b je výsledek známý true;
jinak vybereme `binom(2z,z)=floor(w*u/(v*t)) mod A`
a spočteme jeho zbytek modulo n. Při neúspěchu nastavíme
`m←m+s,v←v*t,w←w*u`; při úspěchu m,v,w nezměníme.

Invariant se zachová. Při úspěchu je nový horní konec právě z.
Při neúspěchu je nové m menší než z_0; vzdálenost původního
horního konce od nového m je F_(j-2)<=F_(j-1), tedy nejvýše
nové s. Monotónní rozšíření dovoluje i virtuální horní konec
za b. Po O(log n) kolech je s=1, tedy z_0=m+1.

Číslo h(n) je buď2m+1, nebo2m+2. Alespoň jedno z
`gcd(2m+1,n),gcd(2m+2,n)` je proto větší než1; vezmeme první
takové. Pro složené n>4 jsou oba argumenty nejvýše h(n)+1<=n−1,
takže vyjde vlastní faktor. Pro prvočíslo n vrátíme n.
Všechny mocniny(4) se při sestupu aktualizují přesnými podíly.
Stačí zobrazené registry a pevný počet dočasných proměnných.
Celkový počet aritmetických kroků je O(log n).

## 5. Chybný invariant v původní odpovědi

V666 se navrhuje inicializace m=F_(j+1) a předpokládá se
`binom(2m,m) mod n!=0`, `binom(2(m+s),m+s) mod n=0`.
Následující aktualizace tyto podmínky obecně nezachová,
i po známé opravě s'←r z18.5.2002.

Pro n=35,b=4 je gcd(4!,35)=1 a8! je násobkem35.
Vezměme s=5,s'=8,m=8, jak dovoluje uvedená inicializace.
Počáteční zbytky jsou25 a0. Nové s=3 a s'=5;
test `binom(22,11) mod35=7` přesune m na11.
Nový horní konec je14, ale `binom(28,14) mod35=20`, nikoli0.
Základ A=2^128 je dostatečný pro všechny tyto koeficienty.
Nejde tedy o chybu přenosu ani o původní překlep s/s'.
Oprava v §4 výslovně používá platný interval(3).
Tento protipříklad neprohlašuje celé f(35) z tištěné heuristické
trajektorie za chybné; dokazuje konkrétní porušení deklarovaného
invariantu, na kterém má spočívat důkaz.

## 6. Další tvrzení, zdroje a rozsah

Úplnou faktorizaci dostaneme v O((log n)²) operacích, jak uvádí416.
Na jedné úrovni stromu rozkladů je součet logaritmů argumentů
nejvýše log n, protože jejich součin dělí n. Každé vlastní
rozštěpení zmenší argument na nejvýše polovinu; hloubka je
tedy nejvýše log_2 n. Počet úrovní krát cena úrovně dává tvrzení.

Robinsonova identita z666 je také správná. Pro
`B>(2n)^(n+1)` je

```
B^n/binom(B,n)=n!*product_(0<=j<n)(1-j/B)^(-1).
```

Součin v jmenovateli je nejméně1−S, kde
`S=n(n−1)/(2B)<1/2`. Rozdíl od n! je proto mezi0 a
`2n!S<n^n*n²/B<1`; poslední nerovnost plyne z n<2^(n+1).
Podlaha dává přesně n!. Ověřen je tento vzorec a jeho atribuce;
samostatnou rychlou implementaci této alternativy neodvozujeme.
Časový výsledek(a) má úplný přímý důkaz v §2.

Shamirův [původní report MIT z1977](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TM-091.pdf)
byl přečten vizuálně na stranách3–13: model, oba algoritmy,
závěrečné otázky a bibliografie. Výslovně omezuje binomický test
na interval mezi sousedními mocninami2; na11 uvádí Fibonacciho
variantu bez podrobné inicializace. [Vydavatelský záznam](https://www.sciencedirect.com/science/article/abs/pii/0020019079900875) potvrzuje
citaci časopisecké verze8(1979),28–31. Její samostatný sazební
text nebyl získán. [Davisův původní článek](https://www.math.umd.edu/~laskow/Pubs/713/Diophantine.pdf)
AMM80(1973),250–251,266
obsahuje identitu i připsání Julii Robinsonové; tyto stránky byly
přečteny, celý článek o Hilbertově problému není auditován.
Závěrečné výzkumné otázky o lepším čase a krajních prvočinitelích
nejsou tímto blokem vyřešeny; žádnou novou dolní mez netvrdíme.

Jednotkový čas se týká pouze zadaného modelu. Naše registry mohou
mít O(n²) bitů: ln A=O(n), exponenty v(1),(4) jsou O(n).
Vůči délce vstupu log n je to exponenciální prostor pro běžné
bitové uložení. Matematická část zadání nepředstírá praktickou
faktorizaci v O(log n) bitových operacích.

## 7. Přesné testy

`verify_shamir_factor.py` realizuje pouze povolené operace a rovnost.
Vestavěné factorial/comb/gcd, mocniny a zkušební dělení jsou oddělené
orákulum, které kontroluje každý relevantní stav. Počítadla a
ukládání testových stop nejsou součástí tvrzení o pevném počtu registrů.

- 159 faktoriálů n=2,...,160; každý prefix, mocniny a extrakce.
- 176 vstupů faktorizace:121 návratů přes gcd a55 Fibonacciho
  hledání;811 kroků vzestupu a sestupu. Zahrnuty2,3,4, prvočíselné
  mocniny,35 a větší příklady až527. Maximum508 modelových operací
  včetně rovností; největší zaznamenané číslo mělo772097 bitů.
- 39 Robinsonových identit při n=2,...,40,401 znaménkových testů
  a celý protipříklad porušeného invariantu pomocí balených čísel.

Tři checkpointy prošly za3.802s, session47950, exit0, limit300s.
Errata all2-prepre/all2-pre/all2/err2 a err2.textxt prohledána
pod416/666/40, Shamir/Robinson/Fibonacci a faktoriálem. Oprava
s'←r z2002 je zahrnuta; odpovídající oprava invariantu nenalezena.
Pozdější fyzický dotisk a prvenství neověřeny; hlášení neodesláno.
