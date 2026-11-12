# §4.5.3: tabulka a elementární hlavní výklad

Tento blok uzavírá dosud neprověřenou číselnou tabulku na 358–359,
větu F a důsledek L na 360, model a součet zbytků na 361 a zaokrouhlenou
nejhorší mez ve shrnutí na 373. Všechny tyto původní strany byly znovu
vizuálně přečteny. Základní identity 357–359 jsou již dokázány v
[euclid-basic.md](euclid-basic.md); jejich úspěšné testy neopakujeme.
Historie a citované prameny mají samostatný pokračující blok.

## Tabulka konstant

Zápis [a_0;a_1,...] zahrnuje celou část a_0; knižní zápis //a_1,...//
celou část vynechává. Pro každý vypsaný prefix tvoří všechny jeho
iracionální hodnoty otevřený interval mezi p/q a (p+p')/(q+q').
Zde p/q je poslední konvergent a p'/q' předchozí konvergent, počítané
rekurzí p_i=a_i p_(i-1)+p_(i-2), q_i=a_i q_(i-1)+q_(i-2).
Počáteční dvojice jsou p_(-2)=0,p_(-1)=1,q_(-2)=1,q_(-1)=0.
Tento interval dále nazýváme válcem prefixu; vzniká dosazením
zbývajícího úplného podílu t z (1,infinity) do příslušné homografie.

Nový skript [verify_euclid_text.py](../verify_euclid_text.py) ověřuje
přesným racionálním porovnáním, že celý rigorózní interval konstanty
leží uvnitř válce **každého** vypsaného prefixu, nikoli jen posledního.

- `8/29`: zpětné dosazení do [0;3,1,1,1,2] vrací přesně 8/29.
- `sqrt(8/29)`: 30 podílů za celou částí. Celočíselná odmocnina
  dává racionální sevření délky 10^-100; obě ostré nerovnosti jsou
  ověřeny umocněním a násobením 29. Navíc přesná kvadratická aritmetika
  potvrzuje celý rozvoj [0;1, overline(1,9,2,2,3,2,2,9,1,2)]
  návratem do stejného algebraického stavu po periodě.
- `cube_root(2)`: všech 28 vypsaných podílů za celou částí.
  Binární hledání celočíselné třetí odmocniny dává interval délky
  10^-100 a obě koncové nerovnosti jsou ověřeny třetími mocninami.
- `pi`: všech 27 vypsaných podílů. Použita Machinova identita
  pi=16 atan(1/5)-4 atan(1/239), nikoli zaokrouhlené desetinné číslice.
  Střídavé řady s 80 a 25 členy dávají přesná racionální sevření.
  Identitu lze ověřit vzorcem pro tangens: tan(4 atan(1/5))=120/119,
  a po odečtení atan(1/239) dostaneme tangens 1. Úhel je v (0,pi/2),
  tedy se rovná pi/4; větev je určena například atan(t)<t a pi>3.
- `gamma`: 30 vypsaných podílů se shoduje s uloženým rigorózním
  9734členným prefixem z [euclid-gamma.md](euclid-gamma.md).
  Drahý výpočet se neopakoval.
- `e` a `phi=(1+sqrt(5))/2`: vypsané vzory souhlasí s obecnými
  důkazy v [euclid-analytic.md](euclid-analytic.md) a
  [euclid-quadratic.md](euclid-quadratic.md). Nekonečný rozvoj phi
  je také bezprostřední z phi=1+1/phi a 1<phi<2.

V tabulce nebyla nalezena nová chyba. Známá oprava množného čísla
„patterns that appear“ z 2024-07-29 se týká doprovodné věty, ne číslic.

## Věta F a horní meze počtu dělení

Nechť T(u,v) počítá všechna dělení v Eukleidově algoritmu, včetně
posledního nulového zbytku a případného počátečního nulového podílu.
Fibonacciho čísla zde mají F_0=0,F_1=1,F_(j+2)=F_(j+1)+F_j.
Continuant K(a_1,...,a_n) je polynom popsaný v `euclid-basic.md`:
rekurze K(a_1,...,a_n)=a_n K(a_1,...,a_(n-1))+K(a_1,...,a_(n-2)),
K(prázdný)=1, K jedné proměnné je tato proměnná.

Pro u>v>0 a T(u,v)=n mají podíly a_1,...,a_n kladné celočíselné
hodnoty a poslední a_n>=2. Podle knižního (17)
u=d K(a_1,...,a_n), v=d K(a_2,...,a_n), kde d=gcd(u,v)>=1.
Polynom K má nezáporné koeficienty a obsahuje součin všech proměnných.
Proto je na kladných vstupech **přísně** rostoucí v každé proměnné.
Jediné minimum u dostaneme pro d=1, a_1=...=a_(n-1)=1, a_n=2.
Rekurze potom dává u=F_(n+2),v=F_(n+1), včetně n=1.
To dokazuje celé tvrzení F i jedinečnost minimalizující dvojice.

Pro libovolné nezáporné u a kladné v po prvním kroku vzniká dvojice
(v,u mod v). Z věty F plyne při n=T(u,v)>=1 nerovnost v>=F_(n+1)
(případ n=1 je přímý). Uvažujme kladné **celé** N a 0<=v<N,
jak je používáno v konečných vstupních rozsazích oddílu. Pro n>=1
máme F_(n+1)<=N-1. Binetův vzorec dává

```text
phi^(n+1)/sqrt(5)
  = F_(n+1) + (-phi)^(-n-1)/sqrt(5) < F_(n+1)+1 <= N,
phi^n < (sqrt(5)/phi) N = (3-phi) N,
n < log_phi((3-phi)N).
```

Tedy n<=floor(log_phi((3-phi)N)), přesně jak je vytištěno v L.
Pro v=0 je počet n=0 a pravá strana je pro celé N>=1 nezáporná.
Zde nezaměňujeme L s chybnou jinou mezí v odpovědi na úlohu 38,
která je samostatně řešena v C0136.

**Rozsah parametru N:** V důsledku L není celočíselnost N zopakována.
Samotný uvedený důkaz ji potřebuje. Při čtení N jako libovolného
reálného parametru je formule nepravdivá: u=2,v=3,N=31/10 má T=3,
ale floor(log_phi((3-phi)N))=2. Tuto podmínku zde uvádíme výslovně;
samostatný nález nezakládáme, protože N je v okolním konečném modelu
celočíselná hranice. Nejde o důkaz formule pro reálná N.

Ze silnější ostré nerovnosti n<log_phi((3-phi)N) dostaneme

```text
n <= ceil(log_phi((3-phi)N)-1)
  <= ceil(4.8 log_10(N)-0.32).
```

Poslední krok používá N>=1, 1/log_10(phi)<4.8 a
log_phi(3-phi)-1<-0.32. Obě konstanty byly rigorózně sevřeny pomocí
Arb při 90 desetinných místech. Ve shrnutí na 373 je skutečně
**horní** celá část; v L na 360 je **dolní** celá část. Obojí správně.
Přibližné hodnoty 2.078,4.785 a .6723 v textu odpovídají.

Také slabší historické matematické meze souhlasí. Dva kroky zmenší
druhý vstup nejméně dvakrát: pokud prostřední zbytek není menší než
polovina, následující podíl je 1 a další zbytek už menší je.
Ekvivalentně F_(n+1)>=2^((n-1)/2), indukcí přes dva indexy, takže
pro u>v>0 platí n<=2 lg(v)+1. Zde lg značí logaritmus o základu 2.
Je-li d počet desítkových číslic v, tedy d=ceil(log_10(v+1)), pak
v<10^d. Pro d>=1 platí F_(5d+2)>10^d: základ F_7=13 a indukce
F_(j+5)=5F_(j+1)+3F_j>10F_j pro j>=2. Proto n>=5d+1 není možné
a n<=5d. Atribuce Finckovi a Lamému se kontrolují zvlášť.

## Floydův model a součet zbytků

T_n značí skutečný průměr T(k,n) pro k=0,...,n-1. S_n značí
hodnotu pomocného modelu, ve kterém se další zbytek znovu považuje
za rovnoměrný. Kniha tyto veličiny správně rozlišuje:

```text
S_0=0,  n S_n=n+sum_(k=0)^(n-1) S_k,
(n+1)S_(n+1)-nS_n=1+S_n,
S_(n+1)-S_n=1/(n+1),  S_n=H_n=sum_(j=1)^n 1/j.
```

Příklad T_5=(1+2+3+4+3)/5=13/5 souhlasí. Tvrzení T_n přibližně
S_n je na této straně pracovní heuristika, kterou další text zamítá,
nikoli chybná dokázaná věta.

Položme R_n=sum_(k=1)^n (n mod k). Při seskupení podle q=floor(n/k)
dostaneme po diskrétním sečtení rozdílů přesnou identitu

```text
R_n=n^2-sum_(q=1)^n binom(floor(n/q)+1,2).
```

Protože floor(x)(floor(x)+1)/2=x^2/2+O(x) rovnoměrně pro x>=1,
součet je (n^2/2) sum_(q<=n) q^-2+O(n H_n).
Ocas řady sum q^-2 za n je O(1/n), a H_n=O(log(n+1)), takže

```text
R_n/n=(1-pi^2/12)n+O(log(n+1)).
```

To je přesně (21), s konstantou přibližně .1775. Pro n rostoucí
je O(log(n+1)) totéž jako knižní O(log n). Porovnání s .25n je
asymptotické; skutečný průměr k/2 v tomto rozsahu je (n+1)/4.
Žádný nový nález.

## Výsledek kontrol

Běh PID1243456, limit120s, dokončen exit0 za .269s; protokol
[euclid-text.log](../results/euclid-text.log), úplné přesné intervaly
a válce v [euclid-text.json](../results/euclid-text.json).
Tři checkpointy prošly: tabulka a perioda, 256 harmonických rekurzí
a 256 přesných součtů zbytků, rigorózní logaritmické konstanty.
Drahé starší checkpointy se neopakovaly.
