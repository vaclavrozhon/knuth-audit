# §3.3.2 H a překrývající se t-tice

Dokončený audit 1.11.2026: text str.70, úlohy15–16,23–24 na str.77–78,
odpovědi564–566. Zdrojové obrazy byly prohlédnuty. Tato poznámka používá
opravy úlohy24 z3.2.2005 a odpovědí z3./5.2.2005; nejde o nové nálezy.

## 1. Maximum a překryvy: úlohy15–16

Pro t nezávislých rovnoměrných veličin na [0,1) má jejich maximum M
distribuční funkci F(x)=x^t, 0<=x<=1: všechny veličiny musí být <=x.
Transformace M^t je rovnoměrná, protože pro 0<=y<=1 platí
Pr(M^t<=y)=F(y^(1/t))=y. Maxima disjunktních bloků jsou nezávislá,
takže textový KS nebo ekvidistribuční test mají uvedenou kalibraci.
Známá oprava odkazu v odpovědi15 z10.5.2017 zahrnuta.

Položme Z_(j,t)=max(U_j,...,U_(j+t−1)). Úloha16(a) správně uvádí
Z_(j,t)=max(Z_(j,t−1),Z_(j+1,t−1)). Při přepisu jednoho pole je třeba
postupovat odleva: pravý soused ještě obsahuje původní hodnotu.
Poslední platný index se s každým zvýšením t zmenší o1.

Úloha16(b): shodná jednorozměrná distribuce nezajišťuje nezávislost.
Konkrétní kvantifikace: označme W_j indikátor Z_(j,t)<=x a p=x^t.
Pro 1<=k<t je společná pravděpodobnost W_j=W_(j+k)=1 rovna x^(t+k),
protože sjednocení oken obsahuje t+k nezávislých vstupů. Tudíž

```text
Cov(W_j,W_(j+k)) = x^(t+k) − x^(2t) > 0  (0<x<1).
```

Při k>=t je kovariance nulová. Asymptotický rozptyl součtu n indikátorů
dělený n je p(1−p)+2 sum_(k=1)^(t−1)(x^(t+k)−p²), větší než
binomický rozptyl. Pro dva stejně pravděpodobné intervaly, x=2^(−1/t),
se běžná Pearsonova statistika blíží násobku chí-kvadrát1, s násobkem

```text
lambda_t = 1 + 4 sum_(k=1)^(t−1) 2^(−k/t) − 2(t−1).
```

Například lambda_2=2 sqrt(2)−1=1.828427..., nikoli1.
Pro rostoucí t je lambda_t/t -> 2/ln(2)−2=0.885390....
To přesně vystihuje směr i řád efektu popsaného v odpovědi. Přirovnání
k opakování dat t-krát není tvrzením přesné rovnosti pro každé t.

## 2. Míchání: úloha23

Abeceda má d číslic; sčítáme po složkách modulo d. Posloupnosti Y,Y'
mají periody lambda a lambda'. Nezávisle volíme pozici n v jedné
periodě Y a posun r v jedné periodě Y'. Nechť P a P' jsou distribuce
jejich t-tic. Protože (n+r) modulo lambda' je při každém n rovnoměrné,
distribuce Q smíchané t-tice splňuje konvoluci
Q(x)=sum_y P'(y)P(x−y).

Označme u=d^(−t) rovnoměrnou hmotnost každého slova. Konvexita čtverce
dává (Q(x)−u)² <= sum_y P'(y)(P(x−y)−u)². Sečtením přes x dostaneme
žádanou kontrakci, protože překlad x -> x−y pouze permutuje konečnou
množinu slov. Důkaz nevyžaduje nesoudělné periody. Vyžaduje však právě
průměrování přes náhodný posun z formulace úlohy; netvrdí zlepšení pro
každý pevně zvolený posun.

## 3. Úloha24: přímý důkaz opravené statistiky

Číslice Y_j jsou nezávislé, s pravděpodobnostmi p_b>0, b=0,...,d−1,
jejichž součet je1. d a délka t jsou pevné, n roste. Pro slovo a
označuje P(a) součin pravděpodobností jeho číslic a N(a) počet jeho
výskytů v cyklickém vstupu délky n. Prázdné slovo má P=1 a N=n.
Kontext je zde slovo gamma délky t−1; b je následující číslice.

Opravená statistika je

```text
V = (1/n) sum_(|a|=t) N(a)²/P(a)
  − (1/n) sum_(|gamma|=t−1) N(gamma)²/P(gamma).
```

Protože sum_b N(gamma b)=N(gamma), lze ji přesně přepsat na

```text
V = sum_(gamma,b) [N(gamma b)−p_b N(gamma)]²
                   / [n P(gamma)p_b].                 (A)
```

Tento tvar ihned dokazuje nezápornost. Zároveň nabízí kratší důkaz
kalibrace. Pro necyklickou nekonečnou posloupnost definujme vektor
odchylek na pozici j složkami

```text
D_j(gamma,b) = [Y_(j−t+1)...Y_(j−1)=gamma] ([Y_j=b]−p_b).
```

Podmíněná střední hodnota při znalosti všech předchozích číslic je
nula. Příspěvky na dvou různých pozicích jsou proto nekorelované:
podmíníme na historii před pozdější z nich. Nezávislé jsou, pokud
jsou pozice vzdáleny alespoň t. Kovariance na stejné pozici je

```text
H_(gamma b,eta c) = [gamma=eta] P(gamma)
                    (p_b[b=c]−p_b p_c).                (B)
```

Společná normální limita součtů D_j/sqrt(n) plyne z blokového důkazu
pro omezené, konečně závislé veličiny v `run-tests.md`, části3.
Cyklické uzavření změní jen t−1 členů, což po dělení sqrt(n) zaniká.
Tudíž (N(gamma b)−p_b N(gamma))/sqrt(n) má limitní kovarianci H.

Po vydělení složky sqrt(P(gamma)p_b) dostaneme pro každý kontext
kovarianční blok I−vv^T, kde v=(sqrt(p_0),...,sqrt(p_(d−1))) má
jednotkovou délku. Tento blok je ortogonální projekce: na směru v
je nula a na jeho kolmém doplňku je identita. Má hodnost d−1.
Bloky pro rozdílné kontexty jsou v normální limitě nezávislé.
Součet čtverců v (A) proto má limitu chí-kvadrát s
d^(t−1)(d−1)=d^t−d^(t−1) stupni volnosti.

Nejde o režim s rostoucí délkou t ani o řídký režim n/d^t omezené.
Číslice s nulovou pravděpodobností je nutné z abecedy vypustit, jinak
jsou tištěné podíly nedefinované.

## 4. Kontrola knižního maticového důkazu

K(a,b)=[a=b]/P(a), včetně K(prázdné,prázdné)=1. Zápis k:a značí
prvních k číslic a, zatímco a:k posledních k číslic. Pro slova a,b
délky t je překryvový člen

```text
T_k(a,b) = K(t+k:a,b:t+k)−1,   k<=0;
           K(a:t−k,t−k:b)−1,   k>=0.
```

Položme C=Cov(N)/n. Při n>=2t−1 se okna nepřekrývají současně
z obou stran; přímé sjednocení pozic dává
C_ab=P(a)P(b) sum_(|k|<t) T_k(a,b). Pro limitní argument stačí
jakékoli pevné t a dostatečně velké n.

Matice L převádí N na odchylky N(gamma b)−p_b N(gamma). Píšeme-li
D pro diagonální matici s prvky P(a), knižní slabá inverze je
Cbar=L^T D^−1 L; její položky jsou K(a,b)−K(t−1:a,t−1:b).
Rovnice (B) znamená L C L^T=H. Platí H D^−1 H=H.

H má hodnost r=d^t−d^(t−1), takže rank(C)>=r. Na druhé straně
počty N splňují zachování toku v každém kontextu: počet příchozích
t-tic se rovná počtu odchozích, a navíc sum N=n. Graf kontextů
má hranu pro každé t-písmenné slovo, od jeho prefixu k jeho sufixu.
Je souvislý: opakovaným připojením číslic libovolného cílového kontextu
se do něj dostaneme. Jeho incidenční podmínky mají d^(t−1)−1
nezávislých rovnic; připočtením celkového součtu dostaneme
rank(C)<=r. Tím je hodnost určena. Pro t=1 je jediný kontext prázdný
a zbývá právě podmínka celkového součtu.

Také rovnost C Cbar C=C lze dovodit bez dlouhého součtu. Matice
D^−1/2 L C L^T D^−1/2 je projekce hodnosti r. Matice
C^1/2 Cbar C^1/2 má stejné nenulové vlastní hodnoty; protože má
hodnost r a je podporována na r-rozměrném obrazu C, je projekcí
na tento obraz. Násobením z obou stran C^1/2 dostaneme žádanou rovnost.

Knižní teleskopický mezikrok po opravě2005 rovněž odpovídá této
struktuře. V součtu T_k H T_l je výsledek nulový, jestliže k>0 nebo
l<0: poslední centrovaná číslice nemá partnera a její střední hodnota
je nula. Pro k<=0<=l položme i=min(t+k,t−l). Eliminace volných
číslic (součet jejich pravděpodobností je1) dává

```text
K(i:(a:i−k), i:(b:i+l))
 − K(i−1:(a:i−k), i−1:(b:i+l)).             (C)
```

První člen vyžaduje shodu společného bloku délky i; ve druhém chybí
jeho poslední, centrovaná číslice. Při pevném posunu delta=k+l mají
oba porovnávané bloky pevné začátky a i probíhá délky1,...,t−|delta|.
Součet (C) se proto zkrátí na T_delta(a,b). Sečtením přes delta
vznikne sum T_delta, jak vyžaduje C Cbar C=C. Původní vnořené
prefixy/sufixy z prvního dotisku tuto vlastnost nemají; opravuje je
již erratum3.2.2005.

## 5. Stav výpočetní kontroly

Program `verify_serial_overlap.py` ukládá dokončené bloky do
`results/serial-overlap.json`; navázání `--resume` je neopakuje.
Všech pět bloků dokončeno. Při prvním vstupu do
kovariančního bloku byla nalezena chyba pomocného programu: prázdný
součin vytvořil Python int a následné dělení float. SymPy pak odmítlo
strukturální rovnost Float(1/4) a Rational(1,4). Hodnota prázdného
součinu byla změněna na přesnou SymPy jedničku. Matematický vzorec
se nezměnil; navázání začalo až kovariancemi a skončilo0.

Výsledky:

- 63 972 přepisů pole maxim, všechny ternární vstupy do délky8.
- 15 376 dvojic period/délek t; přímé průměrování přes posuny
  souhlasí s konvolucí a kontrakcí. Ve12 160 případech je nerovnost ostrá.
- 16 přesných kovariančních modelů: binární t=1,...,5 a ternární
  t=1,...,3, vždy rovnoměrné i nerovnoměrné pravděpodobnosti.
  Ověřeny hodnosti, C Cbar C=C, L C L^T=H a L^T D^−1 L=Cbar.
- Úplná enumerace5 057 cyklických slov ve20 modelech ověřila
  střední hodnoty, přesnou kovarianci nC a shodu obou forem statistiky.
- Opravený teleskopický mezikrok ověřen ve116 190 položkách pro
  všechny posuny k,l v sedmi modelech. Souhlasí i číselný příklad
  a=01101,b=10101 zodpovědi565.

Nový nález v těchto čtyřech úlohách nevznikl. Původní úloha24 je
vedena jako `known_erratum`, ostatní jako `checked`.

## 6. Bibliografický rozsah

Nalezen primární technický report Wai Wan Tsang a Chi-yin Pang,
*The Mathematics of the Overlapping Chi-square Test*, HKU CS TR-2006-12.
[Institucionální odkaz](https://www.cs.hku.hk/data/techreps/document/TR-2006-12.pdf)
byl čitelný přes webový index až do části3; přímé stažení následně
vrátilo404 a další čtení timeout. Report výslovně rozpracovává
Knuthovy úlohy3.3.1-25 a3.3.2-24. Úplné čtení jeho důkazu netvrdíme.
Náš důkaz (A)–(B) vznikl nezávisle před jeho nalezením.

Marsagliova citace v odpovědi23 míří na str.5–6 příspěvku
*A current view of random number generators* v16. Interface Symposium.
Původní dvě strany se zde nepodařilo získat; netvrdíme jejich přímou
kontrolu ani novou bibliografickou opravu. Konvoluční věta je výše
dokázána bez odvolání na tuto citaci. Přesný rozsah přístupu je uložen
v `sources/serial-overlap-bibliography.json`.
