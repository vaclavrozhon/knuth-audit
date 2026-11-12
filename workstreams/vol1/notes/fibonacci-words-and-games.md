# §1.2.8-36–38,40: řetězce, hra a minimaxová rekurence

Audit 1. listopadu 2026; zadání s. 86 a odpovědi 495–496
zobrazeny. F_n,phi,psi jsou jako v `fibonacci-basic.md`.
Zeckendorfova reprezentace a posuny jsou dokázány
v `fibonacci-representations.md`.

## Úloha 36: nekonečné Fibonacciho slovo

Definujeme S_1=a,S_2=b,S_(n+2)=S_(n+1)S_n,
kde součin znamená zřetězení. Pro n>=2 je S_n prefixem
S_(n+1), takže existuje nekonečné slovo S. Náhrada
sigma(b)=ba,sigma(a)=b posílá S_n na S_(n+1), což
plyne indukcí a slučitelností se zřetězením. S je
jediný nekonečný pevný bod této náhrady začínající b.
Délka S_n je F_n, počty a,b jsou F_(n−2),F_(n−1)
pro n>=2 (pro S_1 také s konvencí F_(−1)=1).

Žádný obraz sigma nemá aa; každé a je poslední
písmeno obrazu b a další obraz začíná b. Proto S
nemá aa. Mezi dvěma obrazy b je nejvýše jeden obraz
a, takže mezi sousedními a jsou jedna nebo dvě b;
nevyskytuje se bbb.

Nyní definujme slovo W, jehož b jsou v pozicích
floor(m phi), m=1,2,... . Počet b v prvních k
pozicích je B(k)=floor((k+1)/phi). Iracionalita phi
vylučuje rovnost na hranici. Proto

```text
W_k=b iff floor((k+1)/phi)−floor(k/phi)=1.               (W1)
```

Doplňkové pozice a jsou floor(m phi²): pro každé k
součet počtů těchto dvou posloupností je
floor((k+1)/phi)+floor((k+1)/phi²)=k, protože
phi^(−1)+phi^(−2)=1. Rozdíly po sobě jdoucích počtů
jsou 0 nebo 1 a dávají přesně jedno písmeno v každé pozici.

V sigma(W) se a objeví na konci každého obrazu b.
Pro k=floor(m phi) je délka obrazu prvních k písmen
k+B(k)=floor(m phi)+m=floor(m phi²). To jsou právě
pozice a ve W. Tedy sigma(W)=W, a W=S. Tím jsou
obě podlahové formule odpovědi obecně dokázány;
hustota b je lim B(k)/k=1/phi.

Pro podmínku pomocí Zeckendorfova zápisu položme
n=m−1 a D=sum psi^(k_j). Z posunu (Z2) plyne
n/phi+D celé a 0<phi^(−1)−D<1. Podle (W1) je m-té
písmeno a právě když D>2/phi−1=phi^(−3).
Pokud nejnižší index je 2, potom
D>phi^(−2)−phi^(−5)/(1−phi^(−2))=phi^(−3).
Pokud je nejnižší index >=3, pak
D<phi^(−4)/(1−phi^(−2))=phi^(−3).
Konečnost zajišťuje ostrost. Pro n=0 je D=0 a první
písmeno je b. To vysvětluje i prázdnou reprezentaci,
u níž se žádný nejnižší index neurčuje.

## Úloha 37: vítězná strategie a všechny vítězné tahy

Pro n>0 označme mu(n) nejmenší člen v jeho
Zeckendorfově reprezentaci; mu(0)=infinity.
Herní stav (n,q) znamená n zbývajících kamenů a
možnost odebrat 1,...,min(n,q) kamenů. Odebrání t
vede na (n−t,2t); poslední kámen vyhrává.

Nejprve dva obecné fakty:

```text
mu(n−mu(n))>2mu(n), n>0;                               (N1)
mu(m)<=2(F_k−m), 0<m<F_k, k>=2.                       (N2)
```

(N1) plyne z rozestupu aspoň 2 a F_(j+2)>2F_j pro j>=2;
pro prázdný zbytek platí díky infinity. Pro (N2)
indukujeme podle k. Základy k=2,3 jsou přímé.
Při m<F_(k−1) použijeme indukci pro k−1.
Při m=F_(k−1)+r, 0<=r<F_(k−2), máme pro r>0
mu(m)=mu(r)<=2(F_(k−2)−r)=2(F_k−m). Při r=0
stačí F_(k−1)<=2F_(k−2), platné pro k>=4.

Jestliže 0<t<mu(n)=F_j, reprezentace n−t obsahuje
nezměněný vyšší prefix a nový nenulový konec F_j−t.
Ten má indexy nejvýše j−1 a prefix nejméně j+2,
tedy se neovlivní. Z (N2) plyne

```text
mu(n−t)=mu(F_j−t)<=2t.                                (N3)
```

Indukce podle n nyní ukazuje, že (n,q) je vítězný
právě když q>=mu(n). Při q<mu(n) každý legální tah
podle (N3) dává protivníkovi vítězný stav. Při q>=mu(n)
odebereme mu(n): buď vyhrajeme hned, nebo (N1) zanechá
protivníkovi stav s limitem menším než jeho mu.
Pro n=0 není tah a stav je pro hráče na tahu prohraný.

Ověříme i silnější tvrzení knihy o **všech** vítězných
tazích. Při n=sum F_(k_i) může vyhrát pouze odebrání
celého konce t=F_(k_j)+...+F_(k_r). Důkaz nutnosti:
porovnáme zápisy n a n−t a vezmeme nejvyšší odlišný
index k. Mají společný prefix H, pak n=H+F_k+L,
n−t=H+M, kde 0<=M<F_k. Pokud M>0, (N2) dává
mu(n−t)=mu(M)<=2(F_k−M)<=2t, tedy protivník vyhrává.
Jediná zbývající možnost je M=0, přesně odebrání konce.
Pro tento tah je podmínkou j=1 (vezmeme vše) nebo
F_(k_(j−1))>2t. Samozřejmě ještě musí platit t<=q.

První tah má q=n−1. Proto první hráč prohraje právě
pro Fibonacciho n (včetně n=1, kdy není legální tah).
Protože 1000=F_16+F_7=987+13, jediný legální vítězný
konec je 13: 987>26, zatímco 1000 je v prvním tahu
zakázáno. Ukázkový průběh n=11 na s. 86 je legální;
při posledních třech kamenech protivník vezme 1 nebo 2
a první hráč poté může dobrat zbytek.

Program pro úlohu 38 může používat celočíselný
hladový rozklad a brát mu(n), je-li dostupné. V prohrané
pozici je každý tah proti bezchybnému hráči prohrávající,
takže legální deterministická volba 1 je optimální také.
Konečný nezávislý validátor řeší hru přímo přes všechny
tahy, bez použití tohoto vzorce.

## Úloha 40: maximální počet listů při omezené ceně

Rekurence odpovídá binárnímu stromu s n listy; levá
hrana má cenu 1, pravá 2. Cena stromu je největší
součet cen na cestě od kořene k listu. Jediný list
má cenu 0. Nechť A_m je největší počet listů stromu
s cenou nejvýše m. A_0=A_1=1 a pro m>=2
A_m=A_(m−1)+A_(m−2)=F_(m+1).

Indukcí lze realizovat každý počet listů od 1 do A_m:
počet 1 je samostatný list a součty rozsahů
[1,A_(m−1)]+[1,A_(m−2)] pokrývají [2,A_m].
Proto je hledaná hodnota

```text
f(n)=min{m>=0:n<=F_(m+1)}.
```

Ekvivalentně f(n)=m pro F_m<n<=F_(m+1), s n=1,m=0;
interval m=1 je prázdný. To dokazuje celou minimaxovou
rekurenci a správně ošetřuje její základ f(1)=0.
Konkrétní odkaz na Fibonacciho stromy v jiném svazku
zůstává samostatnou referenční kontrolou.
