# V2-C0135: chybná minima ve vícevstupovém Eukleidově algoritmu

Stav: **confirmed**, §4.5.3-36, odpověď654. Obě uvedená
minima jsou obecně nesprávná. Knižní konstrukce poskytují
možné vstupy, ale nedosahují minima. Níže je krátký
protipříklad i úplný důkaz opravené odpovědi.

Pracujeme s kladnými vstupy u_1,...,u_n. Algoritmus4.5.2C
začíná d=u_n a zpracovává u_(n-1),...,u_1 zprava doleva:
pokud d!=1, vypočítá gcd(u_k,d), jinak skončí. N znamená
celkový počet eukleidovských dělení, včetně posledního
dělení s nulovým zbytkem v každém volání. Fibonacciho
čísla jsou F_0=0,F_1=1,F_(k+2)=F_(k+1)+F_k.

## 1. Dva krátké protipříklady

Pro n=3,N=4 použijme u=(5,3,3). První volání je
gcd(3,3), druhé gcd(5,3):

```
3 = 1*3 + 0,                     jedno dělení, d=3;
5 = 1*3 + 2,
3 = 1*2 + 1,
2 = 2*1 + 0.                     další tři dělení, d=1.
```

Celkem jsou přesně čtyři dělení a u_3=3, zatímco
kniha tvrdí minimum 2F_(N-n+2)=2F_3=4. Vstupy jsou
navíc seřazeny sestupně; není započten žádný počáteční
nulový podíl. Knižní minimum u_1=2F_(N-n+3)+1=7
rovněž vyvrací u_1=5.

Pro samotné druhé tvrzení stačí ještě menší případ
n=N=3, u=(3,2,2). Po děleních2/2,3/2,2/1 má C hotovo;
u_1=3 je menší než tištěné minimum2F_3+1=5.

## 2. Opravené minimum posledního vstupu

Pro N>=n>=3 je správná odpověď

```
min u_n = F_(N-n+3).                                (B1)
```

**Myšlenka důkazu.** Každé volání gcd vyžaduje určitý
Fibonacciho faktor mezi starým a novým gcd. Součin
těchto faktorů je nejmenší, soustředíme-li všechny
nadbytečné kroky do posledního volání. Předchozí volání
mohou mít shodné argumenty, stát jedno dělení a nechat
gcd nezměněný. Předčasný konec tedy nic nenaruší.

Nechť C skutečně provede s<=n-1 volání s počty dělení
j_1,...,j_s>=1 a s postupnými hodnotami d_0=u_n,
d_1,...,d_s. Součet j_i je N. Standardní zpětná
eukleidovská nerovnost dává pro každé volání

```
d_(i-1)>=F_(j_i+1)d_i.                              (B2)
```

Pro j_i=1 je d_(i-1)=d_i a F_2=1. Pro delší volání
poslední dva nenulové zbytky jsou alespoň2d_i,d_i;
všechny dřívější zbytky jsou alespoň součtem dalších
dvou. To dokazuje(B2), i když první argument volání
je menší než druhý.

Pro a,b>=2 platí součinová nerovnost

```
F_a F_b >= F_(a+b-2).                               (B3)
```

Důkaz: Fibonacciho součtový vzorec dává
F_(a+b-2)=F_a F_(b-1)+F_(a-1)F_(b-2), což je nejvýše
F_a(F_(b-1)+F_(b-2)). Opakované použití(B2),(B3) vede k

```
u_n>=d_s product_(i=1..s)F_(j_i+1)
    >=F_(N-s+2)>=F_(N-n+3).                         (B4)
```

Odhad výslovně zahrnuje i s<n-1, tedy předčasné zastavení.

Rovnost dosáhneme pro k=N-n+2>=2 vstupy

```
u_1=F_(k+2), u_2=...=u_n=F_(k+1).                   (B5)
```

Prvních n-2 volání dělí číslo samo sebou, stojí po jednom
dělení a ponechává d=F_(k+1)>=2. Poslední volání
gcd(F_(k+2),F_(k+1)) vyžaduje přesně k dělení a vrátí1.
Celkem je (n-2)+k=N. Tím jsou obě strany(B1) dokázány.

V pomocné parametrizaci knihy lze tedy zvolit
t_1=N-n+3, t_2=...=t_(n-1)=2. Je splněno t_1>=3,
součet t_i=N+n-1 i všechny kongruence uvedené v odpovědi.
Volba t_1=3 s velkým posledním t není optimální.

## 3. Opravené minimum při seřazených vstupech

Při u_1>=u_2>=...>=u_n>0 je správné minimum

```
min u_1 = F_(N-n+4).                                (B6)
```

Konstrukce(B5) ho dosahuje současně s(B1). Pro dolní
mez uvažujme první skutečně provedené volání s j_i>=2;
existuje, neboť N>=n>s. Předchozí volání mají j=1.
Díky seřazení je jeho první argument u_k alespoň u_n,
a tedy alespoň jeho druhý argument d_(i-1). Zpětné
nerovnosti nyní dávají navíc

```
u_k>=F_(j_i+2)d_i.                                  (B7)
```

Pro j_i>=2 má první obyčejné dělení kladný zbytek;
jeho nejmenší dividend je součet dvou příslušných
Fibonacciho mezí. Pro j=1 by(B7) neplatila, což je
důvod výběru prvního delšího volání.

Zbývající d_i omezíme zdola pomocí(B2). Položme e_l=j_l-1.
Pro a,b>=0 další součtový vzorec dává

```
F_(a+3)F_(b+2)>=F_(a+b+3),                          (B8)
```

protože pravá strana je
F_(a+3)F_(b+1)+F_(a+2)F_b. Sloučením všech pozdějších
faktorů v(B7) podle(B8) dostaneme

```
u_1>=u_k>=F_(sum_l e_l+3)d_s
             >=F_(N-s+3)>=F_(N-n+4).                 (B9)
```

Před prvním delším voláním jsou e_l=0, takže součet
skutečně zahrnuje všechna s volání. Tím je(B6) dokázána
bez předpokladu, že algoritmus vždy projde všech n-1 pozic.

## 4. Prameny, errata a konečné kontroly

Vizuálně přečteno zadání378, definice C na341 a odpověď654.
Čtyři řady all2-prepre, all2-pre, all2 a err2 byly
prohledány dne2026-11-03 podle stránek, čísla úlohy,
Bradleyho jména a souvisejících formulí. Oprava k tomuto
minimu v nich není. Starší errata druhého vydání obsahují
zásah z1997-06-18 k odpovědi36 na606, který již zavádí
zdejší chybnou hodnotu2F_(N-n+2). Existence tohoto zásahu
není důkazem správnosti výsledné minimality.

Bradleyho citovaný článek CACM13(1970),433–436 je doložen
vydavatelskými metadaty; pokus o stažení PDF vrátil403.
Jeho originál nebyl čten a netvrdíme, že obsahuje stejnou
chybu. Důkaz výše používá přímo algoritmus vytištěný
v TAOCP. Poslední fyzický dotisk a priorita neověřeny.
Návrh hlášení je ASCII a zůstává neodeslán.

Konečné kontroly jsou v verify_euclid_multi.py. Kromě
stop protipříkladů a dosažení mezí se používá nezávislý
model: pro dané d>1 stačí zkoumat všechny zbytky u mod d,
tedy konečně mnoho přechodů, i když původní u není omezeno.
Výsledky jsou v results/euclid-multi.json. Číselné kontroly
nenahrazují obecné důkazy(B1) a(B6).

Běh PID1215651, limit120s, exit0:854 rodin dosahujících
obě meze;2576 různých zbytkových přechodů a7886 kontrol
dosažitelných nákladů pro u_n<=144 a nejvýše8 volání;
320400 mezí pro druhý argument,314918 pro první a12961
Fibonacciho součinových nerovností. Výsledek dále uchovává
dokončený pilot66705 s252525 seřazenými vstupními vektory;
ten se znovu nespouštěl. Strana113 starších errat byla
vizuálně přečtena a uložena jako další primární doklad.
