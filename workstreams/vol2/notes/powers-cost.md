# §4.6.3, úlohy 30–32: odčítání a ceny sčítacích řetězců

Stav: 4. listopadu 2026. Zadání 484 a odpovědi 696 vizuálně přečteny.
Dva nové potvrzené nálezy: C0226, podhodnocený počet násobení v odpovědi 30;
C0227, chybějící lichost u asymptotického tvrzení v odpovědi 32.
Samotné řešení úlohy 30 s číslem 31 a věta požadovaná v úloze 32 jsou správné.

## 1. Úloha 30: první zlepšení pomocí odčítání

Obyčejný sčítací řetězec začíná 1 a přidává součty dříve dostupných
hodnot; jeho nejmenší délku pro n značíme l(n). Povolíme-li také
rozdíly, píšeme l_±(n). Pořadí pak nemusí být rostoucí a mezivýsledek
smí překročit konečné n. Tištěný řetězec

```
1,2,4,8,16,32,31
```

má šest kroků, kdežto l(31)=7. Druhá hodnota již byla dokázána
v předchozím přesném hledání; zde se znovu nepočítala.

Pro úplnost tvrzení „nejmenší příklad“ jsme nově prošli všechny
množiny hodnot dostupné po nejvýše šesti krocích sčítání a odčítání.
Stačí kladné absolutní hodnoty: při přechodu k absolutním hodnotám
každý původní krok přejde na součet nebo absolutní rozdíl. Nulu
a duplicity lze vypustit. Stav tvoří celá množina dostupných hodnot,
nikoli jen její maximum. Sloučení dvou cest se stejnou množinou
nemění možné pokračování. Neomezujeme velikost mezivýsledku cílem
ani nepožadujeme rostoucí pořadí.

Počty různých stavů v hloubkách 0–6 jsou 1,1,2,6,26,150,1118.
Pro všechna 1<=n<31 se žádná délka menší než uložené l(n) nevyskytla.
V tomto intervalu je l(n)<=7, takže pro vyloučení zlepšení stačí
právě hloubka 6. Pro 31 se poprvé objevil šestikrokový řetězec výše.
Tím jsou nezávisle doloženy oba požadované minimální údaje.

## 2. C0226: v počtu násobení může chybět jedna operace

Nechť lambda(n)=floor(log2(n)) a w(n) je nejmenší počet nenulových
cifer v zápisu n se ciframi −1,0,1. Kniha jej značí pruhem nad nu.
Odpověď 4.1–34 definuje alpha_n jako jediný takový zápis bez sousedních
nenulových cifer a dokazuje, že má váhu w(n); tento předchozí blok
je již uzavřen v [positional-basic.md](positional-basic.md).

Odpověď 30 slibuje lambda(n)+w(n)−1 násobení, jsou-li x a x^(−1)
předem dány. **Pro n=7 je tato mez 3, ale jsou nutná alespoň 4
násobení.** Platí 7=8−1, tedy w(7)=2 a lambda(7)=2.

Stačí uvažovat formální mocniny x, aby se různé exponenty neslévaly
náhodnou vlastností konkrétního x. Násobení sčítá exponenty.
Povolme dokonce zdarma exponenty −1,0,1. Po dvou násobeních je
největší absolutní hodnota exponentu nejvýše 4. Pokud se objeví
absolutní hodnota 4, obě operace musely postupovat přes absolutní
hodnoty 2 a 4, takže žádný exponent s absolutní hodnotou 3 dostupný
není. Pokud se 4 neobjeví, další operace nedosáhne 7, neboť oba
sčítanci mají absolutní hodnotu nejvýše 3. V prvním případě chybí
ke 4 potřebná 3. Proto třetí násobení nemůže dát exponent 7.
Čtyři násobení stačí: x^2, x^4, x^8, x^8*x^(−1).

Nezávislá enumerace všech množin exponentů po třech násobeních
z bezplatných −1,0,1 má počty stavů 1,2,5,16 a rovněž vyloučila 7.
Pro n=1,...,6 dávají tištěné počty 0,1,2,2,3,3 dosažitelné hodnoty;
7 je tedy i nejmenší protipříklad tomuto počtu.

Přesná oprava pro běžnou znaménkovou binární metodu zleva je

```
m+w(n)−1,
```

kde m je index nejvyšší cifry alpha_n. Začneme x, pro každou nižší
cifru umocníme na druhou a při nenulové cifře násobíme x nebo x^(−1).
Provede m umocnění na druhou a w(n)−1 dalších násobení.
Pro kladné n je m buď lambda(n), nebo lambda(n)+1. Příčina rozdílu
je přenos do nové vedoucí pozice v alpha_n. Například alpha_7 je
100(−1), s m=3. Univerzální horní mez lambda(n)+w(n) je tedy správná.
Tento nález se týká číselného počtu; k jeho vyvrácení není třeba
rozhodovat, jak přesně autor zamýšlel variantu zprava.

65535 znaménkových rozvojů pro 1<=n<=65535 prošlo přesnou kontrolou
hodnoty, zákazu sousedních nenulových cifer a posloupnosti exponentů
u opravené metody. V 43682 případech má alpha_n další vedoucí bit.
Tyto konstrukční kontroly znovu netestují již dokázanou obecnou
minimalitu váhy rozvoje.

Stejný chybný počet je v dodatku druhého vydání z 24. srpna 1996,
strana 638, odpověď 30. V dalších pěti vrstvách errat jeho oprava
nenalezena. Není to známá oprava této chyby: historický dodatek
chybnou větu sám zavádí. Fyzický novější dotisk nebyl ověřen;
[návrh hlášení](../reports/C0226-signed-power-count.txt) není odeslán.

## 3. Úloha 31: jak levné přičtení jedničky mění optimum

V této úloze jsou všechny řetězce opět rostoucí a jen sčítací.
Jednoduchý krok znamená a_i=a_(i−1)+1; jeho cena je epsilon>0.
Ostatní kroky mají cenu 1. Označme q počet jednoduchých kroků
v řetězci délky r a f=r−q. Celková cena je q*epsilon+f.
První krok 1->2 je jednoduchý, přestože je zároveň zdvojením.

Pro každé pevné n lze otázku přesně vyřešit konečným algoritmem:
projdeme všechny podmnožiny {1,...,n} obsahující 1,n, ve vzestupném
pořadí ověříme reprezentaci každého členu součtem dřívějších
hodnot a zapíšeme dvojici (q,f). Ponecháme jen dvojice, které nejsou
v obou souřadnicích alespoň tak velké jako jiná dvojice. To je
Paretoova množina: vyřazený bod nemůže být lepší pro žádné epsilon>0.
Minimum přímek q*epsilon+f je pak přesná optimální cena. Je spojitá,
po částech lineární a konkávní; všechny změny nastávají v racionálních
průsečících těchto přímek. Algoritmus je exponenciální, nikoli tvrzení
o efektivním řešení pro neomezeně velké n.

Stačí uchovávat množinu všech dostupných hodnot. Nelze použít prostou
rekurenci jen v poslední hodnotě: další krok může potřebovat konkrétní
starší člen. Naše enumerace zahrnuje i dlouhé řetězce; optimalita
počtu operací není předpokladem optimality vážené ceny.

Obecné jednoduché meze pro n>1 jsou

```
optimal_cost <= min(epsilon*(n−1), lambda(n)−1+epsilon*nu(n)),
```

kde nu(n) je počet obyčejných binárních jedniček. První možnost
postupuje po jedničkách, druhá je binární metoda zleva: má nu(n)
jednoduchých kroků, včetně prvního 1->2, a lambda(n)−1 ostatních.
Při 0<epsilon<1/(n−1) je první možnost optimální, protože jakýkoli
řetězec s ostatním krokem stojí alespoň 1. Pro epsilon=1 se vracíme
k obyčejnému l(n).

Pro n=15 vyšla úplná Paretoova množina

| q | f | Příklad řetězce |
|---|---|---|
| 14 | 0 | 1,2,...,15 |
| 7 | 1 | 1,2,...,8,15 |
| 4 | 2 | 1,2,3,4,5,10,15 |
| 2 | 3 | 1,2,3,5,10,15 |

Optima na 0<epsilon<=1 se střídají na hranicích 1/7,1/3,1/2;
na hranici jsou sousední konstrukce stejně drahé. Základní otázka
„explore“ tak má konkrétní přesné řešení pro každé zvolené n,
obecné krajní režimy a doložený příklad změn optimálního tvaru.
Netvrdíme novou všeobecnou klasifikaci optimálních řetězců.

## 4. Úloha 32: binární metoda minimalizuje součinovou cenu

Cenou kroku a_i=a_j+a_k je nyní a_j*a_k. Minimální celkovou cenu
pro n označme F(n). Cena binární metody G(n) splňuje

```
G(1)=0,
G(2m)=G(m)+m^2,
G(2m+1)=G(m)+m^2+2m.                                       (1)
```

Důkaz, že F=G, potřebuje trochu silnější vlastnost než samotnou
monotónnost. Nejprve ze (1) plyne pro N=2^t*u>=2, u liché,

```
G(N)−G(N−1)=t+u−1 >= 1.                                   (2)
```

Pro liché N je rozdíl N−1; při zdvojení argumentu se rozdíl zvýší
o 1. To dokazuje (2) indukcí, včetně N=2.
Druhý pomocný vztah je

```
G(n)−G(x) >= (n−x)^2+2x−n       if x+2<=n<=2x+1.             (3)
```

Zde podáváme všechny čtyři paritní případy, z nichž původní článek
podrobně rozepisuje pouze jeden. Pro x=1 je (3) přímo ze (1).
Napišme x=2X+e,n=2N+h, kde e,h jsou 0 nebo 1, a D=N−X.
Když D>=2, indukci pro (N,X) lze použít. Po dosazení (1) a odečtení
požadované pravé strany zbývají následující nezáporné výrazy:

| e,h | Rozdíl po použití indukční meze |
|---|---|
| 0,0 | (2D−1)(X−D) |
| 0,1 | (2D+1)(X−D) |
| 1,0 | (2D−3)(X−D+1) |
| 1,1 | (2D−1)(X−D+1) |

Pro e=0 platí D<=X, pro e=1 platí D<=X+1. Případ D=1 je možný
jen pro (e,h)=(0,0),(0,1),(1,1). Označíme-li
Delta=G(X+1)−G(X)>=1, jsou zbylé rozdíly postupně
Delta−1, Delta+2X−3 a Delta; všechny jsou nezáporné pro X>=1.
Tím je indukce (3) úplná.

Nyní indukujeme přímo podle cíle n. Libovolný řetězec můžeme seřadit
a odstranit duplicity i nepotřebné větší členy. Nechť poslední
součet je n=a+b, 1<=a<=b<n. Cena části do b je alespoň F(b)=G(b).

Pro n=2X při b=X stačí G(X)+X^2. Při b=X+1 použijeme (2),
takže cena je alespoň G(X)+1+(X−1)(X+1)=G(2X).
Při b>=X+2 dává (3) po přičtení b(2X−b) mez
G(X)+X^2+2X−b>=G(2X).

Pro n=2X+1 při b>=X+2 dává (3) po přičtení b(2X+1−b)
přesně dolní mez G(X)+X^2+2X=G(2X+1).
Zbývá a=X,b=X+1. Řetězec musí obsahovat oba tyto členy. Cena do X
je alespoň G(X). Samostatný krok vytvářející X+1 stojí u*v, kde
u+v=X+1 a u,v>=1, tedy u*v>=X. Poslední krok stojí X(X+1).
Celkem opět nejméně G(X)+X^2+2X. To zahrnuje i n=3.

Každý řetězec má tedy cenu alespoň G(n), kterou binární metoda
dosahuje. Důkaz nevyžaduje hvězdovost ani optimální délku řetězce.
Všechny kroky původního článku Graham–Yao–Yao, strany 115–119,
byly přečteny ve skenu; zde je důkaz přeorganizován jako přímá
indukce a chybějící paritní výpočty doplněny.

## 5. C0227: asymptotika součtové ceny potřebuje lichý cíl

Při ceně kroku a_j+a_k=a_i označme S(n) nejmenší součet a_1+...+a_r.
Počáteční 1 se nezapočítává. Odpověď 32 uvádí bez omezení n

```
S(n)=(5/2)n+O(sqrt(n)).                                    (4)
```

To je nepravdivé. Pro n=2^k má řetězec všech zdvojení cenu 2n−2.
Navíc pro každý krok platí a_i<=2a_(i−1), tedy

```
a_i >= 2(a_i−a_(i−1)),
S(n) >= 2(n−1).                                            (5)
```

Součet v (5) teleskopuje; rovnost vyžaduje všechna zdvojení.
Proto S(2^k)=2^(k+1)−2 přesně. Rozdíl od (5/2)2^k je
−2^(k−1)−2, který nemůže být O(2^(k/2)). Již explicitní horní
konstrukce by k vyvrácení (4) stačila; (5) potvrzuje přesné optimum.

Oprava: v (4) doplnit **pro lichá n**, nebo pro všechna n uvést
jen horní mez S(n)<=(5/2)n+O(sqrt(n)). Původní
[Zantemova zpráva RUU-CS-89-15](https://ics-archive.science.uu.nl/research/techreps/repo/CS-1989/1989-15.pdf),
definice 1 a přehled na straně 3, oba směry výslovně rozlišuje.
Autorův univerzitní záznam článku z roku 1991 potvrzuje lichost
i v abstraktu. Čten byl sken zprávy z června 1989, nikoli celý
vydavatelský článek z roku 1991.

Stejné neomezené tvrzení (4) přidala errata druhého vydání z
18. října 1996, strana 638, tehdejší odpověď 35. V ostatních pěti
vrstvách errat nenalezena oprava. Fyzický novější dotisk neověřen;
[návrh hlášení](../reports/C0227-additive-cost-parity.txt) není odeslán.

### Kontrola správné liché dolní meze a případu rovnosti

Pro liché n kniha dále tvrdí S(n)>=(5/2)(n−1), s rovností právě pro
součiny čísel 2^k+1. Zde je stručný algebraický rozbor; prázdný
součin zahrnuje n=1. Z (5) pro libovolný úsek řetězce máme

```
sum_(i=u+1)^v a_i >= 2(a_v−a_u),                            (6)
```

s rovností jen při samých zdvojeních v daném úseku. Indukujme
podle lichého cíle n a napišme poslední součet n=a_s+a_t, s<t<r.

Pokud a_t je sudé, a_s je liché. Cena do a_s je alespoň
(5/2)(a_s−1). Cena úseku od a_s do a_t je alespoň a_t a zároveň
alespoň 2(a_t−a_s), tedy alespoň jejich průměr
(3n−5a_s)/2. Závěr řetězce stojí alespoň n. Součet těchto tří
mezí je (5/2)(n−1). Rovnost v obou mezích úseku vynutí a_t=2a_s,
tedy n=3a_s, a předchozí lichý cíl musí také dosáhnout rovnosti.

Pokud a_t je liché a s<t−1, cena do a_s je alespoň 2(a_s−1).
Úsek do a_t stojí přísně více než a_s+a_t=n a zároveň alespoň
2(a_t−a_s). Průměr a závěrečný příspěvek n dávají celkem přísně
více než (5/2)n−2, a tedy i více než (5/2)(n−1).

Zbývá liché a_t s t=s+1. Napišme a_t=u+v, kde u je lichý dřívější
člen a v sudý dřívější člen. Do u stojí řetězec alespoň
(5/2)(u−1); od u do a_s použijeme (6); zbytek stojí alespoň a_t+n.
Výsledná mez je

```
(5/2)(u−1)+2(a_s−u)+a_t+n
= (5/2)(n−1)+(a_s−v)/2 >= (5/2)(n−1),
```

protože v<=a_s. Rovnost vyžaduje v=a_s a pouze zdvojení od u
do a_s, tedy a_s=2^k*u a n=(2^(k+1)+1)*u.
Tím jsou všechny možné rovnosti indukčně rozloženy na činitele
2^k+1. Obráceně, máme-li optimální řetězec končící lichým m s touto
rovností, připojení

```
2m,...,2^(k−1)m, (2^(k−1)+1)m, (2^k+1)m
```

přidá cenu (5/2)*2^k*m. Zachová tedy rovnost pro nový cíl
(2^k+1)m; pro k=1 je zdvojovací úsek prázdný a připojíme 2m,3m.
To dokazuje i postačující směr. Argument odpovídá Proposition 2
na stranách 6–8 zdrojové zprávy, jejichž všechny případy byly přečteny.

### Vlastní jednoduchý důkaz správné horní asymptotiky

Pro libovolné t dává binární metoda S(t)<4t: při sudém kroku
přidáme 2m, při lichém přidáme 2m a 2m+1; indukce s mezí 4t
je okamžitá. Pro t=0 jen nepožadujeme žádnou hodnotu a cena je 0.

Pro n>=4 zvolme mocninu dvou Q=2^k s sqrt(n)<=Q<2sqrt(n),
a napišme n=Q*m+a, 0<=a<Q. Máme m>0. Nejprve sestavíme m a a
samostatnými binárními řetězci a sloučíme jejich dostupné hodnoty.
Potom vytvoříme

```
2m,...,(Q/2)m, (Q/2)m+a, Qm+a=n.
```

Všechny sčítance jsou dostupné. Případné duplicity odstraníme
a seřadíme členy; tím se cena jen sníží. Cena připojené části
je nejvýše (5/2)n−2m−a/2. Proto

```
S(n) <= (5/2)n+2m+(7/2)a
     <  (5/2)n+9sqrt(n).                                   (7)
```

Malá n lze zahrnout přímou kontrolou. Kombinace (7) s lichou dolní
mezí dokazuje opravené (4) bez závislosti na původním výpočetním
ověření přesnější konstanty. V článku na straně 12 je silnější
konstanta (3/7)sqrt(29); zde ji znovu necertifikujeme.

## 6. Modely aritmetické ceny a historické odkazy

Součinová cena a_j*a_k odpovídá školskému násobení, pokud délky
čísel rostou úměrně jejich exponentům; přesné zaokrouhlení délky
nebo zvláštní hodnoty x tento idealizovaný model nezahrnuje.

Při dostupném násobení dvou L-bitových čísel v O(L^beta) operacích,
1<beta<=2, lze delší operand délky A rozdělit na bloky délky B<=A.
Po O(A/B) násobeních a posunutém sčítání vyjde cena O(A*B^(beta−1)).
To vysvětluje asymetrický model a_j*a_k^(beta−1), kde a_j>=a_k,
a odkaz na již prověřenou úlohu 4.3.3–13. Symetrický model
(a_j*a_k)^(beta/2) má pro stejné délky tutéž škálu, ale pro poměr
A/B má proti uvedené blokové horní mezi jinou závislost. Nejde
o univerzální přesný zákon skutečné implementace.

Graham–Yao–Yao: původní pětistránkový článek 115–119 (1978)
vizuálně přečten celý, včetně důkazu a závěrečného nejednoznačného
optima. Scan je uložen z archivu OEIS; obsah je původní článek,
ne komentář OEIS. URL vydavatele a DOI jsou
[10.1016/0012-365X(78)90111-5](https://www.sciencedirect.com/science/article/pii/0012365X78901115).

McCarthy: [Mathematics of Computation 46(174), 603–608 (1986)](https://www.jstor.org/stable/2007998).
Metadata a abstrakt potvrzují téma vlivu ceny násobení na výběr
řetězce. Plný text ani empirické tabulky nebyly získány (AMS403,
JSTOR420); jejich reprodukci netvrdíme. Pro matematické porovnání
modelů výše stačí vlastní blokový argument. Toto omezení zdroje
je odděleno od úplného důkazu požadované věty úlohy 32.

Zantema: primární zpráva RUU-CS-89-15 z června 1989, vizuálně
strany 1–3 a 5–12, zejména definice 1, Lemma 1, Proposition 2,
Lemma 2 a Proposition 5. Část důkazu přesnější konstanty využívá
konečný výpočet, který zde není opakován; pro knižní řád chyby
stačí vlastní důkaz (7). Záznam publikovaného článku z roku 1991
je uložen z autorovy univerzity a Crossref.

Erdősova původní poznámka na straně 81 článku z roku 1960 výslovně
připouští rozdíly, ruší rostoucí pořadí a uvádí platnost své věty
i pro tyto řetězce. Pasáž byla znovu vizuálně ověřena pro tento
konkrétní odkaz. Schönhageův primární abstrakt potvrzuje rozšíření
dolní meze na sčítání a odčítání s příslušnou náhradou počtu
jedniček; plný důkaz této silnější externí věty zde neprohlašujeme
za vlastní.

## 7. Přesné výpočty a rozsah

Tři samostatné bloky [verify_powers_cost.py](../verify_powers_cost.py)
prošly napoprvé:

- signed: úplná šestikroková enumerace bez rostoucího omezení,
  nezávislý protipříklad exponentu 7 a 65535 znaménkových konstrukcí;
- cost_models: všech 2190004 rostoucích řetězců s hodnotami do 24,
  bez omezení jejich délky; přesné minimum součinové i součtové ceny
  a všech 24 Paretoových množin;
- inequalities: 2047 přesných diferencí,523776 intervalových
  nerovností a 8192 algebraických kontrol čtyř paritních případů.

Výsledky: [JSON](../results/powers-cost.json), [log](../results/powers-cost.log).
První blok používá dříve uložená minima obyčejných řetězců; ta se
znovu nehledala. Ostatní úplné konečné výčty jsou nezávislé na
vzorcích, se kterými se porovnávají. Žádný konečný rozsah není
vydáván za důkaz obecné optimality; obecné důkazy jsou výše.

Celkem 4.821794260 s, session 22572, PID 1366707/1366709/1366716,
limit 300 s na blok, exit 0. Žádný úspěšný blok nebyl opakován.
Šest vrstev errat prověřeno včetně odlišného čísla úlohy 32 ve druhém
vydání (odpověď 35); oba chybné dodatky z 1996 jsou v evidenci zachovány.
