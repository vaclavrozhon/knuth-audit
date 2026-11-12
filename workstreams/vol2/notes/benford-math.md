# §4.2.4: matematický text a základní úlohy

Kontrola 2. 11. 2026. Originály str.253–264 a619–623 byly vizuálně přečteny;
20 původních úloh, žádná přidaná úloha ve čtyřech vrstvách errat.
Tento blok uzavírá matematické jádro Q/F a úlohy1,3–17,19. Úloha2
(experiment), úloha18 (axiomy částečně definované pravděpodobnosti), úloha20
(přesnější asymptotika) a historické doklady mají samostatné pokračování.
Následující bloky jsou nyní také dokončeny: [úloha18](benford-axioms.md),
[úloha20](benford-asymptotic.md), [experiment2](benford-addition-experiment.md)
a [vymezený kontext](benford-context.md). Celá sekce je uzavřena20/20.

## Notace, zdroje a rozsah kontrol

Základ zápisu je `b>=2`. Kladné reálné číslo píšeme `b^e f`, kde
`1/b <= f < 1`; `f` je normalizovaná zlomková část. Logaritmický zákon
znamená, že `X={log_b U}` je rovnoměrný na kružnici délky1; složené závorky
značí zlomkovou část. Ekvivalentně má `f` hustotu `l(x)=1/(x ln b)`.
V tomto modelu jde o spojitá, nezaokrouhlená čísla, nikoli konečnou množinu
strojových hodnot. Empirické tabulky jsou odhady pro konkrétní programy.

Pro desítkový zákon dále značí `r in [1,10]` hranici significandu,
`P0(k)` indikátor, že první normalizované číslice kladného celého k jsou
menší než r, a `Pm(k)` m-tý iterovaný aritmetický průměr podle(9).
Pro reálné `x>=1` používáme pro `m>=1` rozšíření
`Pm(x)=sum_{1<=k<=x} P(m-1)(k)/x`, které používá výpočet(8).
Rozšíření hodnotou v `floor(x)` mění výsledek nejvýše `1/x` a limity Q/F
nemění. Úloha8 je níže rozhodnuta na celočíselných argumentech, takže
nejednoznačnost rozšíření P0 nepotřebuje.

Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2`, podle stran i témat.
Relevantní známé opravy:

- Str.255: 19.9.2005 „many different sources“; 9.4.2015 „Dept. of“.
- Str.262: 18.9.2005 doplněn Berger–Bunimovich–Hill.
- Str.263, úloha12: 18.6.2024 `max` změněno na `sup`.
- Str.620, odpověď7: 25.2.2010 `m<=0` na `m<0`, `F(10^k 4^k)` na `F(4^k)`.
- Str.622, odpověď18: 22.3.2002 typografická oprava závorky.
- Str.622, odpověď19: 27.9.1999 dvě opravy základu logaritmu.

Historická stránka37 errat byla znovu zobrazena, ostatní příslušné stránky
jsou v `images/accuracy-errata-*`. Nové problémy s krajními body(8) a
s iterací faktoriálu od2 nejsou v těchto vrstvách opraveny.

[Ověřovač](../verify_benford_math.py), [výsledky](../results/benford-math.json):
100000 přesných porovnání počtu celých čísel, 228 kontrol integrálních
rekurencí a koeficientů generující funkce, 64 nezávislých Fourierových
porovnání s odhadem odříznutého ocasu, 360 přesných porovnání binomické
báze, 55 porovnání integrálů s dilogaritmem a20 vzorků druhého
asymptotického členu. Všech pět checkpointů prošlo; nejde o náhradu
obecných důkazů níže.

## Logaritmický zákon, str.254–257; úlohy3–7,11

**Změna měřítka.** Přenásobení U kladnou konstantou otáčí X na kružnici.
Pravděpodobnostní míra invariantní vůči všem otočením musí dávat každému
z n stejných půlotevřených intervalů míru1/n. Monotonicita a racionální
aproximace určují délku libovolného intervalu. To dává logaritmický zákon
bez potřeby dodatečně předpokládat spojitost. Rovnice(2)–(3) odpovídají
tomuto argumentu; při obecné atomové míře by bylo nutné hlídat otevřené
konce, ale invariance atomům nedovolí kladnou hmotnost.

Tvrzení o společném rozdělení F pro *všechny* celočíselné báze je odlišné
od existence zákona significandu pro jednu bázi. Pro jednu bázi lze vzít
U s hustotou `1/(u ln b)` na `[1,b)`; nejde o rozdělení invariantní vůči
násobení na celé kladné poloose.

**Úloha7.** Uvažujme dvě hranice `r=5^k` a `r=4^k` v bázi `10^k`.
Rozdíl pravých stran(5) je stále `log_10(5/4)>0`. Na levé straně se
sčítají pravděpodobnosti navzájem disjunktních intervalů
`(10^(km)4^k,10^(km)5^k]`. Pro `m<0` jsou všechny pod `2^-k`, pro
`m>=0` všechny nad `4^k`. Celková hmotnost je nejvýše
`F(2^-k)+1-F(4^k)`, což jde k0 pro každou kladnou konečnou náhodnou
veličinu U. Spor. Dvě zveřejněné opravy odpovědi7 jsou nutné a postačují.

**Úlohy3–6.** Pravděpodobnost prefixu23 je `log_10(24/23)`:
1.8483405694... procent. Při logaritmickém zákonu se do stejně širokých
intervalů argumentu antilogaritmické tabulky vstupuje stejně často.
Pro U rovnoměrné na(0,1) je naproti tomu
`Pr(10 f_U <= r)=sum_{j>=1}(r-1)10^-j=(r-1)/9`.
Každá první číslice má1/9; obecně každý prefix dané délky má stejnou
pravděpodobnost. Hexadecimální intervaly pro0,1,2,3 úvodní nulové bity
mají všechny logaritmickou délku1/4. Průměr je1.5 nulového bitu, tedy
p+.5 významového bitu; nejhorší případ má p−1. Se skrytým úvodním bitem
má binární formát p+1 významových bitů. Uvedené meze zaokrouhlení
`2^(1-p)` a `2^(-1-p)` souhlasí s §4.2.2. Platí samozřejmě pro přípustné
celé velikosti polí; tvrzení o rychlosti jsou dobová architektonická úvaha.

**Úloha11.** Převrácení čísla mapuje X na `(-X) mod 1`, což zachovává
rovnoměrnou míru. Bod0 má v tomto modelu nulovou pravděpodobnost.

Prvních100 členů každé ze tří uvedených posloupností `n!`, `2^n`, `F_n`
bylo spočteno přesnými celými čísly, bez logaritmického zaokrouhlení.
Všechny mají přesně30 členů začínajících1, jak tvrdí str.255.

## Lemma Q, Theorem F, rovnice(8)–(26), obrázek5

Nechť `Sm(s)` označuje limit `Pm(10^n s)` pro pevné m>=1 a `1<=s<=10`.
Rovnice(11) určují pomocné funkce Qm,Rm a
`Sm(s)=Qm(s)+Rm(s)[s>r]`. Výjimky bodových hodnot při m=0 neovlivňují
integrály. Přesný celočíselný počet pro m=1 je

```
A(x) = sum_{j>=0} max(0, min(floor(x)+1, ceil(r*10^j)) - 10^j).
P1(x) = A(x)/x.
```

Jen konečně mnoho členů je nenulových. Rozdíl od součtu délek příslušných
intervalů je `O(log x)` stejnoměrně v significandu. Proto

```
S1(s) = 1+(r-10)/(9s),       1<=s<=r,
      = 10(r-1)/(9s),        r<=s<=10.
```

Obě větve se shodují v r. První *přesná* rovnost(8) ale chybně zahrnuje
celé horní hraniční číslo, pokud `s=r` a `r10^n` je celé. Pro `r=s=2,n=1`
vrací12/20 místo11/20. Toto je [C0093](C0093-benford-boundaries.md);
asymptotický odhad i oba hlavní výsledky zůstávají správné.

Pro m>1 rozdělme součet(9) na úplné dekády a poslední neúplnou.
Indukční stejnoměrná chyba je po průměrování stále malá; finitně mnoho
počátečních dekád přispívá `O(10^-n)`. Na každé další dekádě jde o
Riemannův součet spojité funkce S(m−1), tedy o stejnoměrnou aproximaci
integrálu, i když poslední horní mez s kolísá. Geometrická suma vah
úplných dekád dává1/9. Dostáváme

```
Sm(s) = ( integral_1^10 S(m-1)(t) dt / 9
          + integral_1^s S(m-1)(t) dt ) / s.                (A)
```

To dokazuje Lemma Q, včetně stejnoměrnosti na uzavřeném intervalu.
Tištěný důkaz používá stejný argument; rozdíl inkluze posledního
mřížového bodu v plné dekádě je nejvýše `O(10^-j)` a absorbuje se do
Riemannovy chyby. Cílové Sm je spojité a `Sm(1)=Sm(10)`.

**Nezávislý důkaz Theorem F.** Pravá strana(A) je průměrovací operátor T
s jádrem

```
K(s,t) = 1/(9s) + [t<=s]/s,       1<=s,t<=10.
```

Integrál K podle t je1 a `K(s,t)>=1/90`. Lze tedy oddělit desetinu
rovnoměrného průměru a zbylých devět desetin jiného pravděpodobnostního
průměru. Rozpětí hodnot `Tf` je nejvýše0.9-násobek rozpětí f.
Míra `ds/(s ln10)` je invariantní: integrál K(s,t) podle této míry je
`1/(t ln10)`, protože
`integral_1^10 ds/(9s^2)+integral_t^10 ds/s^2=1/t`.
Počáteční indikátor má invariantní průměr `alpha=log_10 r`. Tudíž

```
sup_{1<=s<=10} |Sm(s)-alpha| <= (9/10)^m.
```

Dostáváme stejnoměrnou konvergenci přímo, bez generující funkce.
Související primární zdroj Janvresse–de la Rue2004 je uložen pro následný
historický audit; odhad zde plyne z explicitního výpočtu jádra.

**Tištěná algebra.** Opakovaná integrace dává

```
Rm(s) = -1 + (r/s) sum_{j=0}^{m-1} (ln(s/r))^j/j!,
Qm(s) = 1 + (1/s) sum_{j=0}^{m-1} c_(m-j) (ln s)^j/j!.
```

Dosazení do(A) dává přesně(23). Pro `C(z)=sum_{m>=1} c_m z^m` následně

```
C(z) = -z/(1-z) * ((10/r)^(z-1)-1)/(10^(z-1)-1).
```

Po odečtení pólu v1 je funkce analytická uvnitř kruhu s poloměrem
`|1+2*pi*i/ln10|>1`, takže `c_m -> alpha-1`. Taylorovy řady pro
exponenciálu konvergují stejnoměrně na omezených intervalech logaritmů;
konvoluce s omezenými c_m proto dává stejnoměrné limity Qm→alpha,Rm→0.
Žádná ze změn v C0093 tento výpočet neovlivňuje.

**Úloha10 a nekonvergence pro pevné m.** Položme `L=ln10`,
`w_k=2*pi*k/L`. Fourierův koeficient počátečního indikátoru na kružnici
logaritmů je `a_k=(1-exp(-2*pi*i*k*alpha))/(2*pi*i*k)` pro k≠0.
Z(A) plyne `(d/d(ln s)+1)Sm=S(m-1)`; periodická podmínka tedy dává

```
Sm(s) = alpha + sum_{k!=0} a_k * exp(i*w_k*ln s)/(1+i*w_k)^m. (B)
```

Pro m>=1 je řada absolutně a stejnoměrně konvergentní. Koeficient k=1
je nenulový právě když `1<r<10`; v tomto rozsahu Sm není konstantní,
a tedy Pm(n) nemá limitu. Pro r=1 nebo10 je posloupnost konstantní;
příslušné obecné věty o neexistenci limity musí tyto kraje vyloučit.

Protože `c_m=Sm(1)-1`, izolace k=±1 v(B) dává tištěný člen odpovědi10
s `theta=arctan(2*pi/L)` a jmenovatelem
`pi*(1+4*pi^2/L^2)^(m/2)`. Zbytek je
`O((1+16*pi^2/L^2)^(-m/2))`: po vytažení k=2 jej majorizuje konvergentní
řada konstant krát1/k^2. Rovnice platí i tehdy, kdy některé vyšší póly
C zaniknou v čitateli; pro r=sqrt(10) například zmizí sudé harmonické.
Větu „simple poles at the points“ je tedy třeba chápat jen pro neodstraněné
póly. Výsledná asymptotická formule odpovědi10 je správná.

Vzorky pro r=2,m=1,2,3 v JSON souhlasí s obr.5 včetně hodnot na1/10,
vrcholu S1 v2 a pořadí pravých konců. Nezávislá reprezentace(B) byla
porovnána s Qm+Rm při64 kombinacích parametrů; explicitní odhad ocasu
je uveden přímo v ověřovači.

**Úloha8.** Odpověď „ne“ platí pro `1<=r<10`, protože v bodě s=10 je
P0(10^(n+1))=1 pro r>1, zatímco S0(10)=0. Pro r=1 lze použít s=1,
kde P0=0,S0=1. Pro r=10 je ovšem všude P0=S0=1, tedy odpověď je „ano“.
Při r=2,s=2 navíc P0=0,S0=1 pro každé n. Obecné tvrzení v odpovědi8,
že spojitost limity plyne ze stejnoměrné konvergence, vyžaduje spojité
aproximující funkce; zde P0 po celočíselném rozšíření jsou schodovité.
Správný záporný výsledek má výše uvedený přímý bodový důkaz.

## Úlohy9,16,17: pořadí limit a harmonická pravděpodobnost

**9.** Pro libovolná konečná data existuje jednoznačný rozvoj
`P0(n)=sum_{j<=n} q_j binom(n-1,j-1)`; diagonála této trojúhelníkové
soustavy je1. Identita součtu binomických koeficientů ukazuje, že
průměrování násobí j-tý bázový vektor faktorem1/j. Proto
`Pm(n)=sum_{j<=n} q_j j^-m binom(n-1,j-1) -> q_1=P0(1)`.
Výsledek je pro pevné n; nezaměňuje dvě limity z Theorem F.

**16.** Dokážeme i obecnou nápovědu bez předpokladu omezenosti a_n.
Nechť `B(n)=sum_{k<=n} a_k=o(n)` a `a_(n+1)<=a_n+M/n`.
Pokud a_n neklesá v horní limitě k0, zvolme pevnou hodnotu λ>0, pro
kterou `a_n>λ` nastává nekonečněkrát. Zvolme malé pevné δ>0 tak, aby
`M*log(1/(1-δ))<λ/2`. Při takovém velkém n jsou všechna
`a_k`, `(1-δ)n<=k<=n`, nejméněλ/2, až na zanedbatelnou chybu
harmonického součtu. Součet tohoto intervalu je proto řádu n,
což odporuje `B(n)-B(floor((1-δ)n))=o(n)`.
Pokud `a_n<-λ` nekonečněkrát, použijeme místo toho interval dopředu
`n<=k<=(1+δ)n` a `M log(1+δ)<λ/2`; všechna a_k jsou záporná
nejvýše−λ/2. Opět spor. Tedy a_n→0. Argument platí i při nekonečné
horní/dolní limitě; tištěný důkaz má λ jako konečnou kladnou hladinu.

Je-li `P(m+1)(n)->c`, položíme `a_n=Pm(n)-c`. Pro m>=1 plyne z(9)
`Pm(n+1)-Pm(n)=(P(m-1)(n+1)-Pm(n))/(n+1)<=1/(n+1)`.
Nápověda tedy dává Pm→c a postupným sestupem P1→c. Kontrapozice je
požadovaný výsledek.

**17.** Harmonická pravděpodobnost množiny S je limita
`sum_{k<=N}[k in S]/k / H_N`, kde `H_N=sum_{k<=N}1/k`.
Na úplné dekádě `[10^j,10^(j+1))` má součet1/k přes prefixový interval
`[10^j,10^(j+alpha))` hodnotu `alpha ln10+O(10^-j)`.
Celková chyba přes dekády je omezená; poslední neúplná dekáda je rovněž
omezená. Proto čitatel je `alpha ln N+O(1)` a pravděpodobnost je alpha.
Při notaci zadání je alpha=r in[0,1].

Harmonická pravděpodobnost rozšiřuje obyčejnou: z `A(n)=cn+o(n)` dává
součtová per partes
`sum a_k/k=A(N)/N+sum_{k<N} A(k)/(k(k+1))=c ln N+o(ln N)`.
Pro omezenou posloupnost a navíc změna a na její Cesàrovy průměry
změní čitatel harmonického průměru pouze o O(1): prohoďme dvě sumy a
použijme `sum_{k=j}^N1/k^2=1/j-1/N+O(1/j^2)`.
To dokazuje i tvrzení z odpovědi17 o slabosti opakovaného průměrování:
pro každé pevné m leží dolní/horní harmonická limita mezi dolní/horní
limitou Pm; necháme-li m růst, obě se sevřou k uvedené λ.

Protipříklad v odpovědi17 je sada intervalů
`10^(k^2)<=n<10^(k^2+k)`, k>0. Na logaritmické ose má v k-tém
bloku délky2k+1 vybranou délku k; poměr kumulovaných délek jde k1/2
a poslední blok přispívá relativně O(1/k). Harmonická pravděpodobnost
je1/2. Pro každé pevné m však vnitřní body vybraných a nevybraných
bloků, například `N=floor(10^(k^2+k/2))` a
`N=floor(10^(k^2+3k/2))`, dávají Pm→1, respektive0.
Příspěvek předchozího bloku je nejvýše konstantní násobek
`10^(-k/2)*(1+ln N)^(m-1)`, což jde k0. Tento odhad plyne opakovaným
sčítáním1/j v pozitivním jádru Cesàrova operátoru. Obě tvrzení odpovědi
jsou tak ověřena přímo, bez spoléhání na bibliografii disertace.

## Úlohy1,12–15: výsledky aritmetických operací

**1.** Podle uvedeného modelu podmíněná pravděpodobnost přenosu je
`.07/(.5*.91)=.153846...`, tedy přibližně15 procent.

**12.** Při pevném f_U=x je transformace druhého zlomku na normalizovaný
součin buď `z=xy`, nebo `z=bxy`. Změna proměnné dává přesně dva
integrály odpovědi12. Po dělení referenční hustotou l je relativní
odchylka h váženým průměrem relativních odchylek g s vahami f(x)dx.
Proto její absolutní hodnota nepřesáhne `A(g)`, kde A je supremum
absolutní relativní odchylky. Symetrie dává i `A(f)`.
Pro nekonečné supremum je příslušná nerovnost triviální, pro konečné
platí bodový integrální odhad. Oprava max→sup je správná. U obecných
hustot lze pro verze definované jen skoro všude použít esenciální supremum;
při explicitním bodovém integrálním reprezentantu h funguje i tištěné sup.

**13.** Dva nezávislé rovnoměrné logaritmy X,Y∈[0,1) potřebují nulový
levý normalizační posun právě při `X+Y>=1`, s pravděpodobností1/2.
Pro dělení stačí dva nezávislé stejně rozdělené *spojité zlomky*, protože
pak `Pr(f_U>=f_V)=1/2`. Závěrečná poznámka odpovědi zůstává v tomto
spojitém modelu. U atomových zákonů by bylo třeba přidat polovinu
pravděpodobnosti shody; stejné rozdělení samotné mimo spojitý model
nestačí. To není důvod vydávat konečnou strojovou populaci za spojitou.

**14.** Definujme `Li2(t)=sum_{j>=1}t^j/j^2`, tj. dilogaritmus na[0,1],
a `q_k` jako pravděpodobnost přenosu při absolutním rozdílu exponentů k.
Přímá integrace oblasti `f_U+b^-k f_V>=1` dává pro každou bázi b>=2

```
q_0 = (pi^2/6 - 2 Li2(1/b)) / (ln b)^2,
q_k = (Li2(b^-k)-Li2(b^(-k-1))) / (ln b)^2,       k>=1.
Pr(carry) = sum_{k>=0} p_k q_k.
```

První vzorec vyjde odečtením dvou chybějících okrajových pásů od celého
rohového integrálu. Platí i pro b=2, kde q_0=1, a dává uvedenou identitu
pro Li2(1/2). Pro k>0 integrujeme
`-ln(1-b^-k v)/(v (ln b)^2)` od1/b do1. Hodnoty zaokrouhlené na str.621
souhlasí s tímto výpočtem, včetně .27154 pro b10k0.

Pokud bereme *zobrazené zaokrouhlené* položky tabulky1 jako přesné,
desítkový odhad je14.48735... procent a binární je mezi49.457 a49.799
procenty podle nevypsaného ocasu. Odpověď uvádí „about48 percent“.
Rozdíl sám není potvrzená chyba: vstupy jsou empirické a zaokrouhlené
na setiny; dolní konce těchto zaokrouhlovacích intervalů mohou dát
přibližně48 procent. Rekonstrukce původních statistik Sweeneyho je
samostatná kontextová kontrola. Ze zde uvedených tabulek nelze určit
přesnou výběrovou chybu.

**15.** Při k=0 má nezaokrouhlený desítkový součet úvodní1 právě při
přenosu, jehož pravděpodobnost je q_0<log_10(2). Nerovnost lze doložit
bez desetinného odhadu: `Li2(.1)>.1`, `pi^2<10`, `ln10>2.3`,
`ln2>.69` dávají `pi^2/6-2Li2(.1)<22/15<ln10 ln2`.
Pro k>0 položme `y=10^(1-k) f_V`, takže `10^-k<=y<10^(1-k)`.
Příslušný integrál přes x=10 f_U má vnitřní hodnotu

```
ln(2-y) - ln(1-y/10) < ln2,       0<y<=1.
```

To plyne z `(2-y)/(1-y/10)<2`. Zbývající logaritmický integrál má
celkovou hmotnost1, proto každé k dává přísně méně než log_10(2).
Totéž platí pro každou pravděpodobnostní směs p_k: alespoň jedna kladná
váha musí být přítomna. Úvaha explicitně ignoruje zaokrouhlení, stejně
jako zadání a poznámka o možném přenosu na úvodní2.

## Úloha19: Fibonacci a geometrické posloupnosti

Nechť `phi=(1+sqrt(5))/2`. Binetův vzorec dává
`log_10 F_n=n log_10 phi-log_10 sqrt(5)+O(phi^(-2n))`.
Číslo log_10 phi je iracionální: z případného `phi^q=10^p`, q>0,
přejdeme algebraickým sdružením na `(-1/phi)^q=10^p`, což je v absolutní
hodnotě v rozporu s první rovností. Rovnoměrné rozdělení násobků
iracionálního čísla modulo1 bylo prokázáno v §3.5-22.
Posun a odchylka jdoucí k0 jej zachovávají: hraniční členy přikryjeme
intervaly délky2ε a potom necháme ε→0. Tím je dokázána úloha19.

Pro celé b>1 platí totéž pro b^n, právě když b není mocnina10.
Pokud `b^q=10^p`, prvočíselné rozklady nutí stejné celočíselné exponenty
u2 a5 v b, tedy b=10^j. Dvě známé opravy zápisu logaritmu v odpovědi
jsou zapracovány. Doplňující tvrzení o faktoriálech/binomických
koeficientech/řetězových zlomcích se kontrolují s primárními zdroji
v kontextovém bloku; zde se jejich dokazování netvrdí.

Poznámka str.623 o iterovaných faktoriálech od2! má jiný problém:
2!=2 je pevný bod. [C0092](C0092-iterated-factorial-start.md) obsahuje
přesný protipříklad a vymezuje, co se tvrdí o zamýšlené opravě.

Úloha20 byla následně dokončena obecným důkazem v
[benford-asymptotic.md](benford-asymptotic.md); původní rozsah tohoto
prvního bloku se tím zpětně nerozšiřuje.

Úloha18 následně dokončena přímo ze slabých axiomů; viz
[benford-axioms.md](benford-axioms.md). Konečné výjimky nejsou
protipříklad věty. C0094 eviduje jiné, typografické znaménko.
