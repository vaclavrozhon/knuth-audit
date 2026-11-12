# Quicksort: variance, nenormální limita a přesné optimum prahu

2026-11-07. Dokončení P1067 a horního nákladového bloku 121. Sazba
120–121 a odpovědi 22 na 631–632 zobrazena v předchozím bloku.
Nový primární zdroj: Uwe Rösler, *A limit theorem for “quicksort”*,
RAIRO25(1991),85–100, [originál](https://www.numdam.org/item/ITA_1991__25_1_85_0/).
Lokální PDF/text a obrazy tvrzení jsou v `sources/roesler-1991-quicksort.*`
a `images/quicksort-roesler-*.png`. Níže je výslovně odlišen převzatý
limitní teorém od vlastního přenosu na Q, výpočtu konstanty a důkazu
nenormality. Jeden nový malý arithmetic run nice15 ověřil jen dvě
tištěné desetinné konstanty; žádné simulace, enumerace ani optimalizační
hledání.

## P1068 — rozptyl počtu fází pro M=1 a přesný rozdíl nákladů

Označme A_n náhodný počet partition fází, a_n jeho střední hodnotu.
Z P1062 platí a_0=a_1=0 a a_n=(2n−1)/3 pro n≥2. Po podmínění
uniformním levým rozměrem k=0..n−1 jsou oba následné počty nezávislé,
takže zákon celkové variance dává

    v_n=(2/n)sum_(k<n)v_k + Var(a_k+a_(n−1−k)),  n≥2.

V n=2 je A=1 konstantní; v n=3 má A hodnotu 1 s pravděpodobností
1/3 a 2 s pravděpodobností 2/3. Tedy v_0=v_1=v_2=0,v_3=2/9.
Pro n≥4 je a_k+a_(n−1−k)−(a_n−1) rovno +1/3 pro k=0,n−1,
−1/3 pro k=1,n−2 a nule jinde. Čtyři místa jsou různá. Proto
variance kořenového průměru je 4/(9n). Z toho v_4=2/9 a použitím
P1060 s f_n=4/(9n) dostáváme přesně

    Var A_n=2(n+1)/45,   n≥4.

Nechť X_n je počet guarded porovnání z P1065 s M=1 a C_n skutečný
počet Q. Na stejném partition stromě platí bodově C_n=X_n+2A_n.
Po centrování je L2 norma rozdílu obou normalizací /n rovna
2 sqrt(2(n+1)/45)/n→0. Nestačilo by jen |C−X|≤2n: takový odhad
neprokazuje shodnou centrovanou limitu ani rozptylovou konstantu.

## P1069 — přesná aplikace vnějšího limitního teorému

Röslerovy Theorems2.1/3.1, tištěné 91–92, dávají Wasserstein-L2
konvergenci (X_n−E X_n)/n k jedinému centrovanému konečně rozptylovému
řešení

    Y =d U Y1+(1−U)Y2+g(U),
    g(u)=1+2u ln u+2(1−u)ln(1−u),

kde U je uniformní na [0,1] a U,Y1,Y2 nezávislé, Y1,Y2 mají zákon Y.
Konvergence, její síla L2 a existence/jedinečnost řešení jsou zde
pojmenovanou vnější větou, nikoli námi znovu přezkoušeným celým článkem.

Aplikovatelnost není jen podobnost názvu algoritmu: jeho rovnice(1.1)
má báze X0=X1=0, X2=1, kořenový toll n−1 a nezávislé děti rozměrů
s−1,n−s s uniformním s. Přesně tutéž rekurenci a nezávislost jsme
dokázali pro X v P1056/P1065. Indukcí po n jsou proto stejné celé
zákony, ať se uniformní pivot získá náhodnou volbou v článku, nebo
prvním prvkem náhodné permutace v knize. Centrovat je nutné skutečnou
střední hodnotou, normalizace je n. P1068 přenáší tutéž L2 limitu na
tištěný C_n. Vnější věta se netýká pouze slabé konvergence bez momentů.

## P1070 — vlastní odvození celé rozptylové konstanty na 120

Položme h(u)=u ln u+(1−u)ln(1−u), tedy g=1+2h. Z
integrálu u ln u je E h=−1/2, takže E g=0. Označíme-li
sigma²=E Y², nezávislost v rovnici P1069 odstraní všechny křížové
členy a dává

    sigma²=(2/3)sigma²+integral_0^1 g(u)² du.

Nechť J=integral u(1−u)ln u ln(1−u) du. Dvě diferenciace
integrálu u^a (nebo integrace per partes) dávají
integral u²ln²u du=2/27. Pro J rozvineme −ln(1−u) v kladnou řadu
a použijeme Tonelliho větu; integrand po násobení −ln u je nezáporný.
Tím

    J=sum_(k≥1) (1/k)(1/(k+2)²−1/(k+3)²).

Pro celé a>0 má pomocná suma díky rozkladu na parciální zlomky tvar

    sum_(k≥1)1/(k(k+a)²)=H_a/a²−(zeta(2)−H_a^(2))/a.

Dosadíme a=2,3: první suma je 1−zeta(2)/2, druhá
71/108−zeta(2)/3. Proto J=37/108−pi²/36. Nyní postupně

    E h² = 4/27+2J = 5/6−pi²/18,
    E g² = 1+4E h+4E h² = 7/3−2pi²/9,
    sigma² = 3E g² = 7−2pi²/3 = (21−2pi²)/3.

Konstanta je kladná, protože g je nekonstantní spojitá funkce s
nulovým průměrem. Wasserstein-L2 konvergence z P1069 implikuje
konvergenci druhých momentů; ekvivalentně lze použít trojúhelníkovou
nerovnost pro L2 normy a přenos P1068. Dostáváme přesně

    sd(C_n) ~ sqrt((21−2pi²)/3) n.

Střední hodnota má pro M=1 vedoucí člen 2n ln n, takže relativní
směrodatná odchylka je asymptoticky sigma/(2ln n)→0. To dokládá
i větu, že je „reasonably small compared to(24)“. Nezaměňuji finite-n
variance C a X: stejné jsou zde pouze vedoucí konstanty.

## P1071 — vlastní krátký důkaz nenormality

Předpokládejme pro spor Y~Normal(0,sigma²). Podmíněný momentový
generátor pravé strany pevného bodu v P1069 je Gaussovský. Po dělení
exp(sigma² t²/2) by pro každé t>0 muselo platit

    1=integral_0^1 exp(t g(u)−sigma² t² u(1−u)) du.

Funkce g je spojitá i v nule, g(0)=1. Pro dostatečně velké t má tedy
na 0≤u≤t^(−2) hodnotu alespoň 1/2. Na témže intervalu je
t²u(1−u)≤1. Pravá strana proto je alespoň
t^(−2)exp(t/2−sigma²), což jde do nekonečna, spor. Normální zákon
tedy není možný. Nenormalita tak není převzata jen z názvu citace
ani z numerické simulace či prvních několika momentů.

## P1072 — změna pevného cut-off nemění centrovanou limitu

Kdyby byl dovětek odpovědi 22 čten pro libovolné *pevné* M, lze jeho
rozsah také doložit. Spřáhněme úplný guarded Quicksort X s variantou
X^(M), která zastaví v částech délky ≤M. Rozdíl Z se sčítá přes
konečné listy; jeho báze Z_k=X_k pro k≤M mají konečné všechny momenty.
Pro n>M má rekurenci s nulovým kořenovým tollem. Z P1060 je jeho
průměr mu_n=c(n+1), kde
c=2 sum_(k=0..M)mu_k/((M+1)(M+2)).

Položme delta_k=mu_k−c(k+1) pro k≤M a nulu jinak. Součet malých
delta je nula. Pro n≥2M+2 nemohou být obě děti zároveň malé, takže
variance jejich podmíněného průměru je přesně
K/n, K=2sum_(k=0..M)delta_k². Celková variance Z_n proto opět
splňuje rekurenci P1060 s tollem K/n a od 2M+2 je násobkem n+1.
Tedy centrované Z_n/n→0 v L2.

Také počet A^(M) má affine průměr 2(n+1)/(M+2)−1 pro n>M.
Odchylky báze od této přímky jsou delta_k=1−2(k+1)/(M+2),
jejich součet je nula a stejný výpočet dává Var A^(M)=O_M(n).
Proto ani dodatečný toll 2A^(M) tištěného Q po centrování /n limitu
nemění. Tím je rozsah všech pevných M pokryt, bez tvrzení pro práh
rostoucí s n. Dobová věta „not yet fully analyzed“ nepopisuje zde
ověřený současný stav výzkumu; zbývající dvě citace jsou bibliograficky
vynechány, matematický obsah nahrazuje výše doložený argument.

## P1073 — všechny koeficienty střední ceny a rovnice (26)

P1054 dává přesnou cenu 24A+11B+4C+3D+8E+7N+9S. Pro N>2M+1
dosadíme všech šest průměrů P1061–1064. Koeficient H_(N+1) je
11/3+8=35/3. Konstantní členy mimo násobek N+1 jsou
−24+11/2−7−9=−34.5. Použitím
M(M−1)/(M+2)=M−3+6/(M+2) dostáváme přesně

    T_N=(35/3)(N+1)H_(N+1)+(N+1)f(M)/6−34.5,
    f(M)=8M−70H_(M+2)+71−36H_(M+1)/(M+2)
         +270/(M+2)+54/(2M+3).

Například koeficient 270/(M+2) před dělením šesti vznikne jako
48−11+8=45. Všechny členy tedy mají určený původ; žádný konstanta
nespadla do přibližného O(N).

## P1074 — přesné globální celočíselné minimum M=9 bez hledání

Označme d_m=f(m+1)−f(m). Přímé odečtení dává

    d_m=8−70/(m+3)+(36H_(m+1)−306)/((m+2)(m+3))
        −108/((2m+3)(2m+5)),
    d_(m+1)−d_m=(70m+788−72H_(m+1))/((m+2)(m+3)(m+4))
        +432/((2m+3)(2m+5)(2m+7)).

Pro m≥1 máme H_(m+1)≤1+m/2, takže první čitatel je nejméně
34m+716>0. Tedy d_m je striktně rostoucí pro všechny celočíselné
prahy, nikoli jen na prohledané tabulce. Dále přesně

    d_8=−1691/7700−36/133<0,
    d_9=5981/9240−36/161>0

(poslední první zlomek je >3/5 a druhý <1/4). Jediné minimum f je
proto m=9. To je silnější doložení než tištěná zmínka o počítačovém
výpočtu.

Pro každé N≥20 je M=9 i minimum mezi všemi parametry 1≤M<N,
nejen těmi, pro které se přímo uplatní N>2M+1. Ostatní průměry platí
pro N>M, pouze S_N se pro příliš velké M nahradí nulou. Formální
výraz (N+1)/(2M+3)−1 je tam záporný; tedy f-formule skutečnou cenu
jen podhodnocuje. Její minimum už je cena M=9, kde je formule přesná.
Na strojovém MIX se navíc použije jen podmnožina přípustných prahů
z P1048; obsahuje M=9, takže minimum tím nezmizí. Netvrdím optimální
M=9 pro drobná N ani jiný strojový nákladový model.

## P1075 — obě desetinné konstanty, 1/6 a interpretace smyček

Přesně f(9)=−704923/13860. Pro pevné M=9 použijeme
H_(N+1)=ln N+gamma+3/(2N)+O(N^(−2)). Rovnice P1073 pak dává

    T_N=(35/3)(N+1)ln N+beta N+(beta−17)+O(1/N),
    beta=(35/3)gamma+f(9)/6.

Jediné přímé dosazení v `results/quicksort-m9-coefficients.py/.json`
použilo racionální H100, 80místný log a Euler–Maclaurinův interval

    g−1/(120*100^4) < gamma < g,
    g=H100−ln100−1/200+1/120000,

s rezervou 10^(−60) pro zaokrouhlení. Dostáváme
−1.742524794524 < beta < −1.742524793550, takže tištěné −1.74 a
−18.74 jsou správná zaokrouhlení. 35/3 se správně zaokrouhluje na
11.667; takto zaokrouhlený vedoucí koeficient je přibližný, ne tvrzený
zbytek O(1/N).

Přesné průměry také dávají
B_N=C_N/6−(N+1)/(M+2)+1/2. Pro pevné M tedy B_N/C_N→1/6.
Q3 a Q4 mají skutečně po třech MIX instrukcích, viz P1049. Test i:j
se dělá B+A-krát místo po každém z C porovnání; A=O(N), C~2Nln N,
takže i tento poměr jde k 1/6. To je přesný početní podklad cenového
komentáře, nikoli nový univerzální benchmark.

## Uzavření a zbývající rozsah

P1067 je tím uzavřena. Celé argumenty 120 a matematický obsah odpovědi
22 nyní mají doklady, včetně správné normalizace a přenosu z n−1 na n+1.
Vnější limitní věta je výslovná a její přesné předpoklady byly porovnány;
celý Röslerův článek ani aktuální stav výzkumu tím není auditován.
Dolní část 121 (nejhorší vstupy,25–27, náhodný pivot(27)) a pokračování
Quicksortu teprve následují. Žádný nový nález ani změna C0031.
