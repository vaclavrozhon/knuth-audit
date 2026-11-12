# §1.2.3: determinanty a inverzní matice, úlohy 36–47

Kontrola 1. listopadu 2026, V1-X0036. Původní s. 37–39 a odpovědi
473–475 byly zobrazeny. Není-li uvedeno jinak, n je kladné celé číslo
a pracujeme nad reálnými nebo komplexními čísly. Inverzní matice B
k matici A splňuje AB=BA=I, kde I je jednotková matice.
Determinant definujeme jako součet součinů po všech permutacích
sloupců se znaménkem parity permutace. Tato definice přímo dává
linearitu v každém řádku, změnu znaménka při záměně řádků a nulový
determinant při dvou stejných řádcích. Totéž platí pro sloupce.

## 1. Operace s determinantem a kombinatorická matice

Z linearity a střídavosti plyne vytýkání z řádku i přičítání
násobku jiného řádku bez změny determinantu. Seskupení permutací
podle volby sloupce v jednom řádku dává rozvoj podle kofaktorů.
Kofaktor prvku (i,j) je (−1)^(i+j) krát determinant po odstranění
řádku i a sloupce j. Pro matici řádu 1 je tento kofaktor 1,
jak výslovně doplnila oprava 2020; odpovídá determinantu prázdné
matice, který je prázdným součinem 1.

Matice kofaktorů po transpozici, označená adj(A), splňuje
A adj(A)=adj(A) A=det(A) I. Diagonální členy jsou kofaktorové
rozvoje; mimodiagonální členy jsou rozvoje determinantu se dvěma
stejnými řádky či sloupci. Je-li det(A)!=0, dělení dává
B_ij=cofactor(A_ji)/det(A). To ověřuje celý úvod druhé sady úloh.

Pro úlohy 36,39,42 nechť J značí matici samých jedniček a
A=xI+yJ. Vektor samých jedniček má vlastní hodnotu x+ny;
podprostor vektorů se součtem souřadnic 0 má rozměr n−1 a vlastní
hodnotu x. Proto det(A)=x^(n−1)(x+ny), včetně n=1.
Také knižní sloupcové a řádkové operace dávají horní trojúhelník
s diagonálou x+ny,x,...,x.

Protože J^2=nJ, platí
(xI+yJ)((x+ny)I−yJ)=x(x+ny)I. Při x(x+ny)!=0 je inverze
B=((x+ny)I−yJ)/(x(x+ny)), přesně podle zadání. Pro n>=2
jsou tyto nenulové podmínky ekvivalentní invertibilitě.
Pro n=1 stačí x+y!=0: skalární vzorec se zkrátí na 1/(x+y)
a takto se rozšíří i na x=0,y!=0. Nevyhodnocujeme nezkrácené 0/0.
Ze součtu jednoho řádku B, který je 1/(x+ny), vychází celkový
součet n/(x+ny); platí i v uvedeném skalárním okrajovém případě.

## 2. Vandermondova matice, úlohy 37,40,43

Zde A_ij=x_j^i pro i,j=1,...,n; první řádek má exponent 1, nikoli 0.
Z každého sloupce vytkneme x_j. Zbylý determinant je polynom
stupně n(n−1)/2, který mizí při x_i=x_j, a tedy je dělitelný
každým faktorem x_j−x_i. Tyto různé lineární faktory mají dohromady
právě tentýž stupeň. Koeficient monomu x_1^0 x_2^1 ... x_n^(n−1)
je 1 z identické permutace. Proto

```text
det A = (product_j x_j) product_(i<j)(x_j−x_i).
```

Argument pokrývá i nulové či stejné uzly; determinant je pak 0.
Inverze existuje právě pro navzájem různá nenulová x_j.

Definujme interpolační polynom
L_i(t)=product_(k!=i)(x_k−t)/(x_k−x_i). Má hodnoty L_i(x_j)=[i=j].
Koeficienty B_ij určené rovností
sum_(j=1)^n B_ij t^j=(t/x_i)L_i(t) splňují BA=I, tedy dávají
inverzi. Koeficient t^(j−1) v čitateli L_i je
(−1)^(j−1) krát součet všech součinů n−j různých uzlů kromě x_i.
To je vytištěný vzorec 40. **Jmenovatel obsahuje x_k−x_i**;
pomocný Markdown má obrácené znaménko a při sudém n je chybný.
Případ j=n má koeficient (−1)^(n−1), v souladu s opravou 2020
později přidané vysvětlující věty. První dotisk tuto větu ještě nemá.

Pro součet prvků inverze položme g(t)=sum_(i,j) B_ij t^j.
Jeho stupeň je nejvýše n, g(0)=0 a g(x_k)=1 pro všechna k.
Proto g(t)=1−product_k(1−t/x_k): rozdíl má n+1 různých nul.
Hodnota v t=1 dává odpověď 43,

```text
sum_(i,j) B_ij = 1−product_k(1−1/x_k).
```

Důkaz zahrnuje i uzel x_k=1. Vytištěná pomocná věta o řádku či
sloupci jedniček je rovněž správná: například e_i^T A=1^T
implikuje 1^T B 1=e_i^T 1=1. Oprava 2011 upřesňuje alternativní
knižní důkaz použitím úlohy 33 na uzly 0,1,x_1,...,x_n.

## 3. Cauchyho matice, úlohy 38,41,44

Nechť A_ij=1/(x_i+y_j), přičemž všechny x_i+y_j jsou nenulové.
První dotisk má nad maticí na s. 37 chybně y_i místo y_j;
samotná matice je správná. Oprava je zveřejněna od 15. července 1997.

Od každého sloupce j>1 odečteme první. Z řádku i vytkneme
1/(x_i+y_1), ze sloupce j>1 faktor y_1−y_j. První sloupec se
stane sloupcem jedniček, ostatní mají prvky 1/(x_i+y_j).
Od každého řádku i>1 odečteme první; pak z něj vytkneme x_1−x_i
a ze sloupce j>1 faktor 1/(x_1+y_j). Po rozvoji podle prvního
sloupce zbývá Cauchyho determinant na x_2,...,x_n a y_2,...,y_n.
Indukce, počínaje n=1, dává

```text
det A = product_(i<j)(x_j−x_i)(y_j−y_i) / product_(i,j)(x_i+y_j).
```

Odvození lze nejprve provést pro různé uzly; při shodných uzlech
jsou dva řádky nebo sloupce stejné a obě strany jsou 0.
Inverze proto existuje právě když jsou zvlášť všechna x_i různá
a všechna y_i různá, při stále nenulových součtech x_i+y_j.

Dosazením minorů do transponované kofaktorové formule dostaneme

```text
B_ij = product_k (x_j+y_k)(x_k+y_i)
       / [(x_j+y_i) product_(k!=j)(x_j−x_k) product_(k!=i)(y_i−y_k)].
```

První součin rozdílů je indexován x_j, druhý y_i; záměna i,j by
porušila inverzi. Knižní druhý důkaz (s. 474) ověřuje AB=I pomocí
polynomu v pomocném t: vyjádří levý součet jako polynom stupně
nejvýše n−1, porovná jej s product_(k!=i)(x_j−x_k−t)/
product_(k!=j)(x_j−x_k) v n uzlech t=x_j+y_s a pak dosadí t=0.
Uzly jsou různé díky různým y_s, a výsledkem je [i=j].
Žádná limita v náhodně zvolených číselných vzorcích tuto argumentaci nenahrazuje.

Pro součet sloupce j vyjmutí společných faktorů dává

```text
sum_i B_ij = [product_k(x_j+y_k)/product_(k!=j)(x_j−x_k)]
             · sum_i product_(k!=j)(x_k+y_i)/product_(k!=i)(y_i−y_k).
```

Poslední součet je 1 podle úlohy 33: jeho čitatel je monický polynom
stupně n−1 v y_i. Další aplikace téže úlohy na monický polynom
product_k(t+y_k)=t^n+(sum y_k)t^(n−1)+... dává
sum_(i,j) B_ij=sum x_k+sum y_k, přesně jako na s. 474.

Dodatek 2024 cituje [Grinbergův článek](https://arxiv.org/abs/2301.09777).
Jeho Lemma 2.2 a Theorem 2.1 byly přečteny: roznásobení levé strany
identity sum_(i,j)(x_i+y_j) A_ij B_ji =
sum_i x_i(AB)_ii+sum_j y_j(BA)_jj je přímá distribuce a záměna
konečných součtů. Pro B=A^(-1) a Cauchyho A dostáváme stejný
výsledek, protože (x_i+y_j) A_ij=1. Citace v erratech je matematicky
správná; [autorův seznam](https://darijgrinberg.gitlab.io/w-elementary.html)
potvrzuje publikaci v Mathematical Intelligencer 46(1), 2024, 46–48.
Ověřen byl i autorův opravený text z 6. června 2026; uvedené lemma
a jeho aplikace souhlasí. Tím nekontrolujeme všechny další varianty v článku.

## 4. Hilbertova matice, úloha 45

Hilbertova matice H má H_ij=1/(i+j−1). Je to předchozí případ
x_i=i,y_j=j−1, a tedy součet prvků její inverze je
(1+...+n)+(0+...+(n−1))=n^2. Kofaktorová formule se zjednoduší na

```text
B_ij = (−1)^(i+j) (i+n−1)! (j+n−1)!
       / [(i+j−1) (i−1)!^2 (j−1)!^2 (n−i)! (n−j)!].
```

Faktoriál k! je součin 1,...,k, s 0!=1. Binomický koeficient
C(u,k)=u(u−1)...(u−k+1)/k!, k>=0, je pro nezáporná celá u počet
k-prvkových podmnožin, a pro záporné u platí
C(−u,k)=(−1)^k C(u+k−1,k), u>0. Dosazení těchto definic ověřuje
všechny tři další formy vytištěné na s. 474–475. Zvláště

```text
B_ij = (−1)^(i+j) j C(i+j−2,i−1) C(i+n−1,i−1)
                         · C(j+n−1,n−i) C(n,j)
     = (i+j−1) C(i+j−2,i−1)^2 C(−i−j,n−i) C(−i−j,n−j).
```

Z druhé formy je okamžitě vidět celočíselnost a dělitelnost i+j−1.
První forma dává dělitelnost j; symetrie B_ij=B_ji dává i.
Identita j C(n,j)=n C(n−1,j−1) dává dělitelnost n;
j C(n,j)=(n−j+1) C(n,j−1) dává dělitelnost n−j+1.
Dále n C(i+n−1,i−1)=(i+n−1) C(i+n−2,i−1), takže první
z těchto přepisů dokazuje dělitelnost i+n−1. Symetrie doplní
j+n−1 a n−i+1. Tím jsou dokázány všechny dělitelnosti s. 475,
nejen celočíselnost z několika numerických příkladů.

Výraz „numerical instability“ v úloze popisuje špatnou podmíněnost
rodiny H, nikoli vadu konkrétního algoritmu. Pro reálný vektor v
platí v^T H v=integral_0^1 (sum_(k=0)^(n−1) v_(k+1)t^k)^2 dt>0,
pokud v!=0. H je tedy pozitivně definitní. Označme lambda_min,
lambda_max její nejmenší a největší vlastní hodnotu; číslo podmíněnosti
v eukleidovské normě je kappa_2(H)=lambda_max/lambda_min.

Zvolme koeficienty v polynomu (1−t)^(n−1). Pak
v^T H v=1/(2n−1) a v^T v=C(2n−2,n−1); druhá rovnost plyne
z koeficientu t^(n−1) v (1+t)^(2n−2). Rayleighův podíl dává
lambda_min<=1/[(2n−1)C(2n−2,n−1)], zatímco lambda_max>=H_11=1.
Proto kappa_2(H)>=(2n−1)C(2n−2,n−1), což s n roste alespoň
jako 2^(n−1). Pro inverzi je číslo podmíněnosti stejné, neboť její
vlastní hodnoty jsou převrácené. To dokazuje matematický obsah
poznámky o citlivosti i bez experimentů s plovoucí čárkou.

Při zaokrouhleném vstupu H+E se skutečně řeší jiná úloha:
(H+E)^(-1)−H^(-1)=−H^(-1) E (H+E)^(-1), pokud obě inverze
existují. Proto se při vyhodnocení numerické chyby musí oddělit
změna vstupu od chyby výpočtu. Navržené invertování celočíselné
inverze dovoluje přesný vstup, má-li formát dostatečný rozsah.

## 5. Binetova–Cauchyho identita, úloha 46

Nechť A je m×n, B je n×m. Řádek i součinu AB je lineární
kombinace řádků B s koeficienty A_ik. Multilinearita determinantu
tedy dává sum_(k_1,...,k_m) product_i A_(i,k_i) · det(B_(k_1,...,k_m)).
Pokud se dva k_i rovnají, determinant je 0. Pro pevnou rostoucí
m-tici j_1<...<j_m seskupíme všech m! pořadí vybraných řádků;
jejich znaménka vytvoří det(A_(j_1,...,j_m)). Dostáváme přesně
součet součinů minorů z úlohy. Důkaz platí i pro m>n, kdy je
pravá strana prázdná a všechny levé rozvojové členy mají opakovaný index.

Případy m=n a m=1 dávají det(AB)=det A det B a skalární součin.
Pro B=A^T je det(AA^T) součtem čtverců minorů; pro reálné A jsou
nezáporné. Případ m=2 je identita z úlohy 30. U komplexních matic
se pro nezápornost používá konjugovaná transpozice; samotná knižní
rovnost s A^T zůstává algebraicky správná.

Odpověď na s. 475 má v jednom mezikroku chybně k_i<=m místo k_i<=n.
Pro m=1,n=2,A=(0,1),B=(0,1)^T by tento mezikrok dal 0 místo 1.
Jde o známou opravu z 15. prosince 2001, nikoli nový nález.

## 6. Krattenthalerův determinant, úloha 47

Položme P_j(t)=product_(k<j)(t+p_k) product_(k>j)(t+q_k)
a A_ij=P_j(x_i), pro i,j=1,...,n. Parametry jsou x_1,...,x_n,
p_1,...,p_(n−1),q_2,...,q_n. Dokážeme obecný vzorec

```text
det A = product_(i<j)(x_i−x_j)(p_i−q_j).
```

Matice A je součinem Vandermondovy matice s mocninami 0,...,n−1
a matice koeficientů polynomů P_j. Označme determinant druhé matice D.
Jeho stupeň v parametrech p,q je nejvýše n(n−1)/2. Pokud p_i=q_j
pro i<j, všechny P_k mají společný faktor t+p_i: pro k>i pochází
z prvního součinu, pro k<=i z druhého, protože k<j. Tyto polynomy
pak leží v podprostoru rozměru n−1, takže D=0. Každý z odlišných
lineárních faktorů p_i−q_j tedy dělí D; jejich celkový stupeň je
právě n(n−1)/2. D je proto jejich součin krát konstanta.

Při p_i=0,q_j=1 je P_j=t^(j−1)(t+1)^(n−j); koeficientová
matice je trojúhelníková s diagonálou 1, tedy D=1. Součin rozdílů
je (−1)^(n(n−1)/2). Vynásobení determinantem první matice,
product_(i<j)(x_j−x_i), proto dává tvrzené znaménko i vzorec.
Jde o polynomiální identitu, platnou i při shodných parametrech.

Dosazení p_i=q_i=y_i na společných indexech i=2,...,n−1 dává
A_ij=product_(k!=j)(x_i+y_k), tedy Cauchyho matici s řádkem i
vynásobeným product_k(x_i+y_k). Pro n>=2 je nových nezávislých
parametrů n−2: právě tolik rovností bylo třeba zavést. Původní
odpověď uváděla n−1; oprava 15. října 2007 dává správných n−2.

Primární [Krattenthalerův článek](https://www.mat.univie.ac.at/~kratt/artikel/generat.pdf),
Lemma 2.2 na s. 177–178, byl zobrazen i přečten. Jeho A_j=q_j,
B_i=p_(i−1) dávají stejný vzorec; důkaz postupnými rozdíly sloupců
souhlasí s odpovědí knihy. Citované stránky a autorství jsou ověřeny.
Náš výše uvedený důkaz přes determinant koeficientů nezávisle
určuje i konstantu a znaménko. Zbytek článku o rovinných rozkladech
se tím neprohlašuje za prověřený.

## 7. Výpočty a přesné meze bibliografického ověření

`check_matrices.py` porovnává uzavřené formule s přesnou Gaussovou
eliminací nad zlomky; ověřuje také přímo součin AB.
Prošlo 343 kombinatorických, 210 Vandermondových a 210 Cauchyho
případů, 650 prvků Hilbertových inverzí pro n=1,...,12,
360 obdélníkových případů Binetovy–Cauchyho identity a 350
Krattenthalerových determinantů včetně singularit. Je to kontrola
přepisu a znamének, nikoli náhrada obecných důkazů výše.

Doplňující historické odkazy na de Moivra a Cauchyho původní spisy,
a datum společného přednesení Binetovy a Cauchyho práce v roce 1812,
ještě nejsou uzavřeny. Celočíselnost a citlivost Hilbertovy matice
jsou dokázány výše nezávisle na ověření těchto historických pramenů.

[Toddův primární článek z roku 1961](https://nvlpubs.nist.gov/nistpubs/jres/65B/jresv65Bn1p19_A1b.pdf),
s. 19–20, popisuje explicitní inverzi i zkušenosti s numerickým
invertováním Hilbertových matic. Identita článku, název, autor,
ročník 65 a rozsah 19–22 souhlasí s citací knihy. Stažení přes
urllib vrátilo 403; text byl dostupný přes webový náhled.
Tento bibliografický bod je ověřen, původní Cauchyho text zůstává
samostatnou zdrojovou závislostí.
