# §4.5.3-41: skládání řetězových zlomků

Tištěné zadání378 a odpověď655–656 byly přečteny v originále.
Kontrola zahrnuje obecnou skládací identitu, všech20 indexových
případů prvního čísla, Liouvilleovy rozvoje pro každý základ
l>=3 i odstranění nul pro l=2. Matematické vzorce jsou správné,
pokud k v posledním odstavci znamená exponent dvojky; slovní
vymezení tohoto k je samostatný interpretační kandidát C0140.

## 1. Značení a dvě algebraické identity

Slovo W=(x_1,...,x_n) je konečný seznam podílů; rev(W)
je jeho obrácení, W[:-j] odstraní posledních j členů a
zápis [0;W] znamená obyčejný řetězový zlomek. Pro kladné
podíly je jeho hodnota p/q v základním tvaru. Předchozí
konvergent označíme p'/q'. Kontinuant K(W) je horní levý
prvek součinu matic M(x)=(x,1;1,0); K(prázdné)=1.
Tedy q=K(W), p=K(x_2,...,x_n) a

```
p q' - p' q = (-1)^(n-1).                             (F1)
```

Kontinuanty jsou polynomy, takže jejich identity platí
i pro záporné či nulové argumenty. Než se taková slova
interpretují jako obyčejné kladné rozvoje, musí se normalizovat.

Pro A=(x_1,...,x_(m-1)), B=(y_n,...,y_1) napišme
první řádek M(A) jako (a,b) a první sloupec M(B)
jako (c,d). Přímé násobení dává

```
M(x-1) M(1) M(y-1) = (xy-1,x;y,1),
M(z) M(0) M(w) = M(z+w).                              (F2)
```

První identita ukazuje, že levá strana první knižní
kontinuantové identity je x_m a c + b c - a d.
První sloupec M(-B) je ((-1)^n c,(-1)^(n-1)d).
Proto její pravá strana, x_m K(A)K(B)+(-1)^n K(A,0,-B),
je přesně totéž. Druhá identita (F2) dokazuje knižní
odstranění vnitřní nuly: sousední z,0,w se nahradí z+w.
Důkaz je obecný v m,n i ve všech argumentech.

## 2. Skládací lemma a znaménko

Z obrácení kontinuantu máme [x_n;x_(n-1),...,x_1]=q/q'.
Úplný podíl

```
T=[r-1;1,x_n-1,x_(n-1),...,x_1]=r-q'/q
```

tedy při připojení za W dává

```
[0;W,r-1,1,x_n-1,x_(n-1),...,x_1]
  = (p T+p')/(q T+q')
  = p/q + (-1)^n/(r q^2).                            (F3)
```

Poslední rovnost plyne z (F1) a qT+q'=rq. Krajní případ,
kdy některý pomocný převrácený výraz není konečný, se
čte pomocí matic (F2), tedy bez dělení nulou.

Každé racionální číslo v (0,1) má obě parity délky:
kanonický konec x_n>=2 lze nahradit x_n-1,1. Tím lze
v (F3) zvolit znaménko. Nuly pro r=1 nebo x_n=1 se
odstraní pomocí (F2). U dvou konkrétních řad níže je
vždy zachován kladný rozvoj sudé délky.

U obecné řady z knihy mají jmenovatele rekurzi
D_1=l_1, D_(j+1)=D_j^2 l_(j+1). Čitatel nového součtu
je P_j D_j l_(j+1)+(-1)^e a je nesoudělný s novým
jmenovatelem, protože modulo každý jeho prvočinitel je
roven +1 nebo -1. Proto (F3) skutečně skládá její konečné
součty s r=l_(j+1). Výrok o nekonečné hodnotě se vztahuje
na konvergentní řady; libovolná volba jednotkových l_j
s libovolnými znaménky sama konvergenci nezajišťuje.

## 3. Dračí posloupnost a její reflexe

Definujme d_0=1. Pro n>0 napišme n=2^s u, kde u je
liché; s=nu_2(n) je exponent nejvyšší dělící mocniny
2^s. Potom

```
d_n = 0 pro u=1 mod4,     d_n = 1 pro u=3 mod4.        (F4)
```

To je přesně knižní rekurze d_(2n)=d_n,
d_(4n+1)=0, d_(4n+3)=1. Pro Q=2^h, h>=1, a 0<t<Q
platí

```
d_Q=0,
nu_2(Q+t)=nu_2(Q-t),
d_(Q+t)+d_(Q-t)=1.                                   (F5)
```

Odečteme společnou mocninu dvojky z t a Q. Pokud
nu_2(t)<=h-2, liché zbytky Q+t a Q-t jsou modulo4
opačné. V jediném zbývajícím případě t=Q/2 jsou
liché zbytky3 a1. To dokazuje (F5).

Erratum z21.7.2009 přidává vztah k Jacobiho symbolu.
V jeho standardním oboru, tedy pro kladné liché n,
je (-1/n)=(-1)^((n-1)/2)=1-2d_n přímo z (F4).
Dračí posloupnost je definována i na sudých indexech,
což samo nerozšiřuje obor Jacobiho symbolu. Poloha
otočení draka navazuje na již prověřenou úlohu4.1-18.

## 4. Číslo s podíly1 a2

Označme c_k=sum_(j=1)^k 2^(-(2^j-1)). Jeho jmenovatel
q_k=2^(2^k-1), protože čitatel je lichý, a
c_(k+1)-c_k=1/(2q_k^2). Skládáme tedy s r=2.
Sudé rozvoje prvních čtyř součtů jsou

```
W_1=(1,1),
W_2=(1,1,1,2),
W_3=(1,1,1,2,1,1,1,1,1,1),
W_4=(1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1).
```

Od W_3 končí slova dvojicí1,1. Jediná vzniklá nula
v (F3) se sloučí se sousedy1,1, a tak

```
W_(k+1)=W_k,(1,2),rev(W_k[:-2])       pro k>=3.        (F6)
```

Délka W_k je20*2^(k-4) pro k>=4. Každé W_k je
prefixem následujících slov a má pouze členy1,2.
Limita řady je iracionální: její binární zápis má
jedničky přesně na pozicích2^j-1, tedy nekonečně mnoho
jedniček a neomezeně dlouhé mezery nul. Takový zápis
není od jistého místa periodický. Nekonečný kladný
řetězový zlomek určený (F6) proto dává právě tuto limitu.

Pro kontrolu explicitního knižního vzorce napišme
n-1=20q+r, 0<=r<20. Definujme A(n) přesně jeho tabulkou:

```
r=3,16:                         A=2,
r=8,11:                         A=1+((q+r) mod2),
r=1:                            A=2-d_q,
r=18:                           A=1+d_(q+1),
ostatní r:                      A=1.                 (F7)
```

Prvních20 hodnot je W_4. Stačí dokázat reflexi (F6)
pro m=20Q, Q mocninu dvojky. Hodnoty A(m+1)=1,
A(m+2)=2 plynou z d_Q=0. Pro další indexy párujeme
n a n'=2m+1-n. Jejich zbytky jsou r'=19-r a
q'=2Q-1-q. Konstantní případy se párují se stejnou
konstantou. V páru8/11 mají q+r a q'+r' stejnou paritu.
Pár1/18 vyžaduje d_q+d_(2Q-q)=1, případně totéž
s q+1. To je (F5). Kraj s indexem0 používá d_0=1
proti d_(2Q)=0. Jediný neplatný střed q=Q v prvním
páru je přesně již oddělený index m+2. Všechny
indexové případy jsou tím vyčerpány a (F7) dokázána.

## 5. Liouvilleovy rozvoje pro l>=3

Definujme L_l=sum_(j>=1) l^(-j!) a S_m jeho součet
prvních m členů. Pro m>=2 má S_m jmenovatel l^(m!),
neboť jeho čitatel je1 modulo l. Nový přírůstek je

```
S_(m+1)-S_m = 1/(q_m^2 r_m),
r_m=l^(m!(m-1)).                                      (F8)
```

Začínáme W_2=(l-1,l+1). Pro l>=3 jsou všechny členy
(F3) kladné a

```
W_(m+1)=W_m,(r_m-1,1,last(W_m)-1),rev(W_m[:-1]).       (F9)
```

Délka W_m je2^m-2; pro m>=3 končí W_m číslem l-1.
Prvních6 členů je (l-1,l+1,l^2-1,1,l,l-1).
Zejména pátý člen je písmeno l, nikoli číslice1;
OCR tento rozdíl na655 nezachovává.

Položme E_l(k)=l^(k!(k-1))-1. Pro n>=1 knižní
vzorec, s přesným určením exponentu k, zní

```
n mod4 =1: l-2+d_(n-1)+(floor(n/2) mod4),
n mod4 =2: l+2-d_(n+2)-(floor(n/2) mod4),
n mod4 =0: 1 při d_n=0, jinak E_l(nu_2(n)),
n mod4 =3: E_l(nu_2(n+1)) při d_(n+1)=0, jinak1.       (F10)
```

Ověření všech indexů: prvních6 členů odpovídá W_3.
Při přechodu ze slova délky N=2^m-2, m>=3, jsou
nové střední členy na pozicích2^m-1,2^m,2^m+1
rovny E_l(m),1,l-2. To plyne přímo z (F4) a (F10).
Zbytek má být obrácením W_m[:-1], tedy se párují
n a n'=2^(m+1)-1-n pro
2^m+2<=n<=2^(m+1)-2. Zbytky modulo4 se párují
0/3 a1/2. U páru0/3 jsou argumenty dračí posloupnosti
n a n'+1, popřípadě n+1 a n'; jejich součet je
2^(m+1). Podle (F5) mají stejnou valuaci a opačné
hodnoty d, takže se oba výrazy rovnají. U páru1/2
mají argumenty n-1 a n'+2 opět součet2^(m+1),
hodnoty d tedy součet1. Zbytky floor(n/2) mod4
u obou indexů mají součet3. Dosazením se rovná i tento
pár. Tím (F10) splňuje přesně (F9) a je obecně dokázána.

Iracionalita L_l plyne z neperiodického zápisu v základu l,
kde jedničky stojí na pozicích1!,2!,3!,... . Délky prefixů
rostou a zůstávají kladné, takže konečné identity (F9)
opět určují požadovaný nekonečný rozvoj.

## 6. Základ2 a explicitní normalizovaný vzorec

Pro l=2 smí (F10) obsahovat nuly. Odstranění nul
vždy použije (F2), nikoli svévolné vynechání členu.
Například sudé rozvoje jsou

```
V_3=(1,3,3,1,2,1),
V_4=(1,3,3,1,2,1,4095,3,1,3,3,1).
```

Pro m>=4 má V_m délku3*2^(m-2), končí3,1 a skládání
po sloučení prostředního 1,0,3 dává

```
V_(m+1)=V_m,(E_2(m),4),rev(V_m[:-2]).                  (F11)
```

Tím už máme jednoduchý obecný konstruktivní vzorec.
Pro úplnost lze index n-1=12q+r, 0<=r<12, zpracovat
přímo následující tabulkou. Její parita q znamená právě
rozlišení tříd modulo24, o kterém kniha mluví.

| r | Normalizovaný podíl |
|---|---|
| 0 | E_2(nu_2(q)+4), pokud q>0 a d_q=0; jinak1 |
| 1 | 4-d_q |
| 2 nebo9 | 3 |
| 3 nebo8 | 1 |
| 4 | 2+(q mod2) |
| 5 | 1 pro sudé q; 4095 pro liché q |
| 6 | 4095 pro sudé q; 1 pro liché q |
| 7 | 3-(q mod2) |
| 10 | 3+d_(q+1) |
| 11 | E_2(nu_2(q+1)+4), pokud d_(q+1)=1; jinak1 |

První blok je V_4. V reflexi délky12Q, Q=2^h, jsou
nové střední členy E_2(h+4),4. Ostatní indexy mají
r'=11-r, q'=2Q-1-q. Pár0/11 používá stejné valuace
a opačné hodnoty d z (F5); kraj q'=0 se shoduje
pomocí d_0=1. Pár1/10 používá stejnou komplementaritu.
Páry4/7 a5/6 využívají opačnou paritu q,q'. Ostatní
páry jsou konstantní. To dokazuje (F11) pro celou
tabulku, nikoli jen pro konečný vypočtený prefix.

## 7. Transcendence a rozsah pramenů

Transcendentní znamená, že číslo není kořenem žádného
nenulového polynomu s celočíselnými koeficienty. Pro
Liouvilleova čísla tento doplňkový výrok dokážeme přímo.
Z (F8) máme pro q_m=l^(m!)

```
0 < L_l-S_m < 2/q_m^(m+1).                            (F12)
```

Pokud by L_l bylo algebraické stupně D, zvolme jeho
ireducibilní celočíselný polynom P. Iracionalita zčásti5
zajišťuje P(S_m)!=0. Celé číslo q_m^D P(S_m) má
absolutní hodnotu nejméně1. Derivace P je omezená na
pevném okolí L_l, takže věta o střední hodnotě dává
|L_l-S_m|>=c/q_m^D pro pevné c>0. Pro m>D je to
v rozporu s (F12). Tím je transcendence dokázána.

Liouvilleův článek1851,133–142 byl získán z Numdam;
začátek výslovně odkazuje na jeho dvě poznámky zkvětna1844.
Strana135 uvádí právě řadu s faktoriály v exponentu.
Citace knihy na rozšířený článek1851 proto není tvrzením,
že objev pochází až zroku1851.

Shallitův autorský přepis článku1979 byl získán a přečten
v částech o skládání včetně věty11 a případu 2B(2,infinity).
Jeho B(2,infinity)=sum_(j>=0) 2^(-2^j) splňuje
c_infinity=2B(2,infinity)-1. Jde o autorský přepis
stran1–9, nikoli o obraz původních časopiseckých209–217.
Vlastní důkazy výše jeho nevypsané indukce doplňují.

Allouche–Lubiw–Mendès France–van der Poorten–Shallit1996
byl získán; v úvodu a §2 je potvrzen rozšířený rámec
znamének a skládání. Jeho celý dvacetistránkový výzkumný
obsah zde netvrdíme prověřený. Autorova stránka navíc
obsahuje vlastní corrigenda k článku; nejde o errata Knuthovy
úlohy ani o předpoklady našich důkazů.

Kempnerův originál1916 nebyl stažen: AMS vrací403,
JSTOR poskytl metadata476–482, ale odkaz naPDF vrátil jiný obsah. Jeho historická priorita
a původní důkaz transcendence prvního čísla zůstávají
výslovně v kontextové frontě oddílu; neodvozujeme je
z pouhé omezenosti podílů1,2. Ta sama transcendenci
obecného čísla nezaručuje.

## 8. Nezávislé ověření

Program `verify_euclid_folding.py` porovnává skládací
pravidla s přímým Eukleidovým rozvojem přesných racionálních
částečných součtů. Jeho checkpointy ověřily:

- 4096 kontinuantových identit se znaménky a nulami
  a5460 skládání všech slov délky1–6 nad1,2,3 a r=1–5;
- prvních13 přesných součtů prvního čísla, celkem20476
  podílů, a81920členný prefix podle explicitní tabulky;
- 54 přesných Liouvilleových součtů pro základy2–10
  a délky2–7, celkem2108 podílů;
- 491414 symbolických členů do16. součtu a normalizaci
  131036 surových binárních členů; obrovské mocniny jsou
  přesně reprezentovány indexem svého exponentu;
- 65519 reflexí dračí posloupnosti a5000 lichých
  vstupů identity s Jacobiho symbolem.

První běh PID1231463 dokončil první tři checkpointy,
pak odhalil chybu vlastního symbolického validátoru:
E_2(2)=3 porovnával jako formální značku proti číslu3.
Druhý běh po opravě této reprezentace použil `--resume`,
takže úspěšné přesné výpočty neopakoval. PID1231692,
relace6005, limit180, exit0; symbolická část16.53s.
Původní chybový log je zachován odděleně. Všechny
univerzální závěry výše mají vlastní obecný důkaz.
