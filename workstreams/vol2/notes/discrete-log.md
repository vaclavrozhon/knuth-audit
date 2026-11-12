# Diskrétní logaritmus: §4.5.4-46

Zadání417 a odpověď671, první dotisk třetího vydání (1997), byly vizuálně
přečteny3.11.2026. Oprava posledního modulu z9.2.1998 je zahrnuta.
Nový nález C0173 se týká samotného výpočtu logaritmů malých prvočísel.
Níže je vlastní obecný důkaz subexponenciálního algoritmu; nepředpokládá
rovnoměrné náhodné matice ani neprokázanou hypotézu o hladkých číslech.

Nechť p je prvočíslo, M=p−1 a a **primitivní kořen**, tedy prvek, jehož
mocniny projdou všech M nenulových zbytků modulo p. **Diskrétní logaritmus**
b vůči a je exponent n s a^n=b modulo p, určený jednoznačně modulo M.
Kniha volí zástupce1≤n≤M; běžný zbytek0 proto na konci nahradíme M.
Případ p=2 je triviální. Dále používáme přirozený logaritmus ln.

## 1. Správné vztahy a C0173

Zvolíme mez B<p a **faktorovou bázi** q_1,…,q_d všech prvočísel≤B.
Číslo je **B-hladké**, pokud má všechny prvočinitele v této bázi.
Pro nalezené hladké hodnoty mocnin zapíšeme celé rozklady

```
a^r_i mod p = product_(j=1)^d q_j^e_ij.                     (1)
```

Exponenciální vektor e_i=(e_i1,…,e_id) je jeden řádek vztahů. Máme-li
pro každý k koeficienty c_ik, které současně pro všechna j splňují

```
sum_i c_ik e_ij + M t_jk = [j=k],                           (2)
```

pak logaritmus q_k je

```
N_k = sum_i c_ik r_i modulo M.                             (3)
```

Zápis [j=k] znamená1 při j=k a0 jinak. Důkaz (3) nepotřebuje znát
žádný logaritmus: umocníme vztahy (1) na celé exponenty c_ik, vynásobíme
a použijeme q_j^M=1 modulo p. Záporné exponenty jsou přípustné, protože
všechna q_j jsou jednotky modulo p.

**C0173:** tisk má místo r_i v součtu pro N_j výraz e_jk. Už pro p=7,
a=3, jedinou bázi q_1=2 a vztah r_1=2, e_11=1 lze vzít c_11=1,t_11=0.
Tištěný vzorec dává N_1=1, ale 3¹=3, zatímco správně3²=2 modulo7.
Nejde o nedostatek vztahů: jediný řádek[1] tvoří celou jednorozměrnou bázi.

Stejný odstavec navíc píše x_ijk místo společných c_ik. Kdyby se
koeficient mohl nezávisle měnit s j, řešily by se jednotlivé souřadnice
odděleně; to nedává jednu kombinaci řádků (2). Například jediný řádek(1,1)
má obě souřadnice invertibilní, ale negeneruje(1,0) modulo žádné M>1.
Opravu proto formulujeme souvisle jako (2)–(3), nikoli jen přejmenováním
jednoho chybného indexu. Obě vady evidujeme pod jedním algebraickým nálezem.

## 2. Výpočet nad složeným modulem

M=p−1 je obvykle složené, takže nelze obecně dělit nenulovým pivotem jako
nad tělesem. Použijeme celočíselnou mříž L generovanou řádky e_i a M krát
jednotkovými řádky. Slovo mříž zde znamená všechny jejich celočíselné
lineární kombinace. Rovnice (2) je řešitelná pro všechna k právě tehdy,
když L obsahuje všechny jednotkové řádky, tedy L=Z^d.

Udržujeme horní trojúhelníkovou celočíselnou bázi A mříže L. Na začátku
A=M I. Při vložení řádku v procházíme sloupce j. Je-li pivot h=A_jj
a nová souřadnice w=v_j, rozšířený Eukleidův algoritmus najde
g=gcd(h,w)=s h+t w. Nahradíme dvojici řádků A_j,v dvojicí

```
s A_j+t v,     −(w/g) A_j+(h/g) v.                         (4)
```

Tato dvouřádková transformace má determinant1, zachovává celočíselný obal
a v druhém řádku vynuluje sloupec j. Dřívější sloupce obou řádků jsou0.
Po všech sloupcích zbyde nulový řádek, který zahodíme. Odečtením celých
násobků pozdějších bázových řádků ještě zmenšíme položky nad diagonálou.
Současně vedeme koeficienty kombinací původních vztahů modulo M.

Součin kladných diagonálních prvků je index [Z^d:L], tedy počet zbytkových
tříd modulo L. Index1 znamená A=I po uvedeném zmenšení, a koeficienty
řádků jsou přesně c_ik. Nejde o faktorizaci M. Členství dalšího řádku
ověříme postupným celočíselným dělením pivoty; nepotřebné řádky lze zahazovat.

Mezilehlé celočíselné hodnoty mají polynomiální bitovou délku v d a ln M:
redukovaná báze obsahující M Z^d má diagonálu nejvýše M a položky nad ní
menší než odpovídající pivot. Při jednom vložení násobení nejvýše d-krát
zvětší bitovou délku o O(ln M); Bézoutovy koeficienty mají stejnou
polynomiální mez. Změnových řádků je nejvýše d log_2 M, viz oddíl3.
Konstrukce je tedy polynomiální v d a ln p na jeden pokus.

## 3. Proč dostatek vztahů opravdu vznikne

Označme H podgrupu (Z/MZ)^d generovanou dosavadními řádky. Podgrupa zde
znamená množinu uzavřenou na součet a opačný prvek. H je celá právě
při indexu1 z oddílu2. Pokud je vlastní, leží v nějaké maximální vlastní
podgrupě; příslušný jednoduchý abelovský podíl má prvočíselný řád ell|M.
Existuje tudíž nenulová lineární forma

```
f(e) = sum_j lambda_j e_j modulo ell
```

která je na H nulová. To je jen důkaz existence překážky; algoritmus ell
ani koeficienty lambda nehledá a rozklad M nepotřebuje.

Vyberme j s lambda_j≠0. Nechť S(X,B) je množina B-hladkých kladných
celých čísel≤X a Psi(X,B) její počet. Pro každé
v∈S(floor(M/B),B) jsou v i q_j v v S(M,B). Jejich exponentové vektory
se liší o j-tý jednotkový vektor, takže f na nich nemůže být zároveň0.
Aspoň jeden tedy leží mimo H. Každé číslo může být koncem nejvýše dvou
takových dvojic (jednou jako v, jednou jako q_j v). Proto

```
#{v in S(M,B): exponent vector outside H}
    >= Psi(floor(M/B),B)/2.                                (5)
```

Rovnoměrné r∈{0,…,M−1} dává přesně rovnoměrné a^r mod p v1,…,M.
Každý pokus tedy zvětší vlastní H s podmíněnou pravděpodobností alespoň

```
delta = Psi(floor(M/B),B)/(2M).                             (6)
```

Zvětšení H nejméně zdvojnásobí jeho velikost. Od nulové podgrupy do celé
grupy může nastat nejvýše d log_2 M takových zvětšení. I po podmínění
na libovolnou historii je čekání na další zvětšení shora ovládané
geometrickým rozdělením s parametrem delta. Očekávaný počet pokusů je
nejvýše d log_2 M / delta. Není potřeba předpokládat, že hladké exponentové
vektory jsou rovnoměrné v nějakém vektorovém prostoru.

## 4. Elementární subexponenciální odhad

Nejprve stručně odvodíme potřebný hrubý počet prvočísel. Označme
theta(x)=sum_(q prime≤x) ln q a psi(x)=sum_(q^h≤x) ln q; druhý součet
počítá prvočíslo znovu za každou jeho mocninu. Každá prvočíselná valuace
binom(2m,m) je součtem nul a jedniček přes mocniny≤2m, a proto
binom(2m,m) dělí lcm(1,…,2m). Z největšího členu binomického rozvoje plyne

```
psi(2m) >= ln binom(2m,m) >= 2m ln2−ln(2m+1).
```

Dále psi(x)−theta(x)≤sqrt(x) ln x: přispívají jen prvočísla≤sqrt(x),
každé celkem nejvýše ln x. Tudíž theta(x)≥c x pro pevné c>0 a velké x.
Počet prvočísel pi(x) pak splňuje pi(x)≥theta(x)/ln x≥c x/ln x.
Tento elementární důkaz nevyžaduje prvočíselnou větu.

Položme L=ln p a pro dostatečně velké p zvolme

```
B = ceil exp(sqrt(L ln L)),  d=pi(B),
X = floor(M/B),  k = floor(ln X / ln B).
```

Každý součin k různých prvočísel báze je nejvýše B^k≤X. Různé k-prvkové
podmnožiny mají různé součiny, takže pro velké p, kdy d≥k,

```
Psi(X,B) >= binom(d,k) >= (d/k)^k.
```

Máme d≥cB/ln B, k ln B≥ln X−ln B≥L−2ln B−O(1) a k≤L/ln B.
Proto

```
ln Psi(X,B) >= k(ln B−ln(k ln B)+ln c)
              >= L−O(ln B+(L/ln B)ln L)
               = L−O(sqrt(L ln L)).                       (7)
```

Zaokrouhlení mění pouze uvedené O(1) a O(ln B). Konečný počet malých p
lze vyřídit přímo. Z (6)–(7) plyne delta^(-1)=exp(O(sqrt(L ln L))).
Stejnou mez mají d i počet a cena pokusů z oddílu3. Bázi lze vytvořit
sítovým postupem, každý kandidát rozložit zkušebním dělením touto bází
a jeho mocninu vypočítat opakovaným čtvercováním. Celkový očekávaný počet
bitových operací je tedy

```
exp(O(sqrt(ln p * ln ln p))) = p^o(1).                      (8)
```

Výraz p^o(1) znamená růst pomalejší než p^epsilon pro každé pevné
epsilon>0. Z Markovovy nerovnosti navíc plyne požadované „almost always“:
zastavíme-li běh po p^epsilon operacích, pravděpodobnost nedokončení
je nejvýše p^(−epsilon/2) pro dostatečně velké p, protože očekávaný čas
je pak nejvýše p^(epsilon/2). Nesprávnou odpověď algoritmus nevydá.

## 5. Cílový logaritmus

Po zjištění N_j nezávisle volíme r a rozkládáme b a^r mod p. Tato hodnota
je také přesně rovnoměrná mezi nenulovými zbytky. Pravděpodobnost hladkosti
je Psi(M,B)/M≥2delta, takže dodatečný očekávaný čas má rovněž mez (8).
Je-li rozklad product_j q_j^f_j, pak

```
n = sum_j f_j N_j−r modulo M.                              (9)
```

Výsledek ověříme mocninou a^n=b. Tisk měl poslední kongruenci modulo p;
známá oprava9.2.1998 ji mění na p−1. Například p=7,a=3,b=2,n=2,r=5
dává b a^r=3, jehož logaritmus je1: 2+5=1 modulo6, ale ne modulo7.
Toto není nový nález a je odděleno od C0173.

## 6. Primární prameny a rozsah

[Adlemanův původní šestistránkový článek](https://pages.cs.wisc.edu/~cs812-1/adleman.pdf)
z FOCS1979,55–60, byl celý přečten vizuálně. Citace knihy souhlasí.
Autor nejprve rozkládá p−1 a používá závislosti cílových vztahů po jeho
prvočíselných mocninách; na59 výslovně rozlišuje okruhy od těles.
Naše argumentace (5) dokazuje silnější podmínku generování celé faktorové
báze, kterou používá knižní odpověď, a faktorizaci p−1 nepotřebuje.
Článek je zdrojem historické kontroly, nikoli náhradou za vlastní důkaz
této odlišné implementace. Jeho další kryptografické odhady a rozšíření
na složený modul nejsou předmětem úlohy46 ani nově potvrzenými výsledky.

[Coppersmith–Odlyzko–Schroeppel, Algorithmica1(1986),1–15](https://link.springer.com/article/10.1007/BF01840433)
odpovídá druhé citaci. Přečtena vydavatelská metadata a původní první
strana v oficiálním náhledu. Jejich lepší konstanta1 v exponentu je tam
výslovně heuristická; není použita v našem nepodmíněném důkazu (8).
Celý patnáctistránkový článek není označen za auditovaný.

## 7. Kontroly a evidence

`verify_discrete_log.py` obsahuje tři oddělené bloky. První porovnává
celočíselné řádkové transformace s úplně vyjmenovanými podgrupami malých
(Z/MZ)^d a kontroluje všechny koeficientové certifikáty. Výslovný příklad
modulo6 používá řádky(2,0),(3,0),(0,2),(0,3): žádná jejich nenulová
souřadnice není jednotkou, ale dohromady generují celou grupu.

Druhý blok prochází všechny nenulové lineární formy v omezených rozměrech
a ověřuje párování i dolní mez (5) přímým soupisem hladkých čísel.
Třetí rekonstruuje logaritmy z náhodných vztahů a porovnává je s úplnými
tabulkami mocnin; kontroluje i všechny vztahy (1) běžným celočíselným
součinem a certifikáty (2). Konečná implementace ponechává i nadbytečné
řádky pro kontrolu certifikátů; pro časový důkaz je lze zahazovat.
Přesné výsledky:1152 vložení řádků,112896 porovnání členství a5376
prvků certifikátů;15777 lineárních forem,116447 párových kontrol a39
hladkých mezí.108 předvýpočtů použilo1186 vztahů,2449 pokusů a659
zvětšení podgrupy;2872 dalších prvků certifikátů a599 gcd kroků s
neinvertibilními vstupy.13318 cílových logaritmů po31458 pokusech souhlasí
s úplnými tabulkami mocnin. Všechny tři bloky passed za2.654707808s,
PID1305146, obal1305145, session78527, limit180s, exit0.
Výsledky v `results/discrete-log.json` a logu; úspěšné bloky neopakovány.

Dne3.11.2026 prohledány všechny čtyři vrstvy errat i aktuální TeX podle
417/671,46, Adleman, Coppersmith, Schroeppel, discrete logarithm a indexů
vzorců. Oprava posledního modulu byla ověřena v all2-prepre, strana42.
Chybný součet pro N_j ani jeho koeficientové indexy opraveny nejsou.
Novější fyzický dotisk a priorita nálezu nejsou ověřeny. Hlášení neodesláno.
