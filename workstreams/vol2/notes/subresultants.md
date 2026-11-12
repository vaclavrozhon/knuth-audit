# §4.6.1: subresultanty a kořeny na konečné mřížce

Rozsah: algoritmus C a matematika na stranách 428–433, úlohy 11–16 a 24,
odpovědi 673–675. Sken 3. vydání, 1. dotisk, 1997. Obrázky těchto stran
byly přečteny; OCR slouží pouze k navigaci. Historické odkazy mají níže
samostatně vymezený rozsah. Celá §4.6.1 ještě není hotova.

## 1. Význam posloupnosti a správnost C

S je obor s jednoznačným rozkladem a K jeho podílové těleso. Symbol lc(f)
označuje vedoucí koeficient nenulového polynomu f. Pseudodělení násobí
dělenec mocninou lc(dělitele), aby se vyhnulo zlomkům; jeho správnost byla
prokázána v `polynomial-division-basic.md`.

Nejprve pracujeme v K a teprve determinantovým důkazem v oddílech 2–3
ukážeme, že normalizované hodnoty patří do S. Tím se vyhneme kruhovému
předpokladu dělitelnosti v C3. Označme vstupní primitivní polynomy u_1,u_2,
jejich pokračování u_i a stupně n_i. Předpokládáme n_1>=n_2; dále jsou
stupně nenulových zbytků přísně klesající. Položme

```
delta_i = n_i - n_(i+1),
g_1 = h_1 = 1,  g_i = lc(u_i) pro i>=2,
h_(i+1) = h_i^(1-delta_i) g_(i+1)^delta_i.

g_(i+1)^(delta_i+1) u_i
    = q_i u_(i+1) + g_i h_i^delta_i u_(i+2).             (A)
```

Předpis pro h používá již aktualizované g. Každý krok (A) zachovává gcd
v K[x] až na nenulovou konstantu. Poslední nenulový člen proto určuje
primitivní gcd v S[x]; společný obsah se vrátí v C4. Při konstantním zbytku
je primitivní gcd roven 1 a C2 oprávněně končí dříve. Pro determinantovou
analýzu je vhodné připojit také tento normalizovaný konstantní zbytek.

Tabulka (15) má po vstupních stupních 8,6 další členy

```
-15x^4 + 3x^2 - 9,
65x^2 + 125x - 245,
-9326x + 12300,
260708.
```

Postupné páry (g,h) před dělením jsou (1,1),(3,9),(-15,25),(65,169).
Vytištěné řádky souhlasí. Konstantu 260708 skutečný C již nemusí ukládat.

## 2. Koeficienty jako determinanty; úlohy 11 a 24

Minor zde znamená determinant čtvercové podmatice vybrané z obdélníkové
matice. Pro j>=2 položíme d=n_j a sestavíme M z koeficientových řádků

```
x^s u_1,  s=n_2-d,...,0;
x^s u_2,  s=n_1-d,...,0.
```

Sloupce jsou v sestupném pořadí stupňů D,...,0, kde D=n_1+n_2-d.
Počet řádků je H=n_1+n_2-2d+2. Zavedeme

```
alpha_i = g_(i+1)^(delta_i+1)/(g_i h_i^delta_i),
z_i = g_i h_i.
```

Z rekurence h plyne přesná identita alpha_i=z_(i+1)/z_i.
Při nahrazení řádku x^s u_i podle (A) se násobí tento řádek alpha_i
a odečte se příslušná kombinace existujících řádků x^t u_(i+1).
Potřebné posuny jsou přítomny: jejich nejvyšší index je
n_(i+1)-d+delta_i=n_i-d. V kroku i se nahrazuje
n_(i+1)-d+1 řádků. Vyšší řádky u_(i+1) se zachovají.

Po krocích i=1,...,j-1 a permutaci řádků zbývají skupiny

```
u_i: posuny n_(i-1)-d,...,n_(i+1)-d+1,  2<=i<j;
u_j: posuny n_(j-1)-d,...,0;
u_(j+1): posun 0.
```

Vedoucí stupně všech řádků kromě posledního jsou přesně D,D-1,...,d.
Pro koeficient r_t=[x^t]u_(j+1), t<d, vybereme prvních H-1 sloupců
a sloupec stupně t. Transformovaný minor je trojúhelníkový, s determinantem

```
±L r_t,
L = product_(i=2)^(j-1) g_i^(delta_(i-1)+delta_i)
    * g_j^(delta_(j-1)+1).
```

Celkový násobek původního minoru je

```
A = product_(i=1)^(j-1) alpha_i^(n_(i+1)-d+1)
  = z_j * product_(i=2)^(j-1) z_i^delta_i
  = L.                                                   (B)
```

První zjednodušení teleskopuje poměry z; druhé používá
h_i^delta_i=g_(i+1)^delta_i*h_i/h_(i+1) a h_2=g_2^delta_1.
Proto det(Minor)=±r_t. Všechny vstupní koeficienty jsou v S, tedy i r_t.
To je obecný důkaz (19)->(20), včetně nenormálních poklesů stupňů.

**Úloha 11.** Při stupních 9,6,5,2,-infinity potřebujeme pro poslední
nenulový zbytek j=3,d=5: A_1,A_0; B_4,...,B_0; C_1,C_0; D_0.
Nulový další člen nevyžaduje pokračování tabulky.

## 3. Pomocné h jako determinanty

Pro j>=2 nyní M obsahuje řádky u_1 s posuny n_2-n_j-1,...,0
a u_2 s posuny n_1-n_j-1,...,0. Prázdnou skupinu vynecháme.
Vybereme prvních H=n_1+n_2-2n_j sloupců; případ H=0 má determinant 1.
Stejná eliminace končí skupinou u_j. Její násobek je

```
T = product_(i=1)^(j-2) alpha_i^(n_(i+1)-n_j)
  = product_(i=2)^(j-1) z_i^delta_i,
Lh = product_(i=2)^(j-1) g_i^(delta_(i-1)+delta_i)
     * g_j^delta_(j-1).
```

Trojúhelníkový determinant je ±Lh. Z (B) vychází g_j h_j T=g_j Lh,
tedy det(M)=±h_j. Pro j=2 jde přímo o g_2^delta_1. To dokazuje
(23)->(24), integritu všech h i oprávněnost C3. Jde zároveň o druhou
část úlohy 24.

Známé opravy jsou nutné: p432 po (22) jen dva faktory b_6^3 (1998),
p431 Table 1 u C_1,C_0 exponent d_2^3, u D_0 e_1^2 (2022),
p432 před (23) C_(n_2-n_j-1), nikoli součet v indexu (2022).
Obecné počty řádků výše nezávisle určují správné faktory.

## 4. Resultant a odpověď 12

Sylvesterova matice je čtvercová matice řádků x^(n-1)u,...,u,
x^(m-1)v,...,v, kde m=deg(u),n=deg(v). Její determinant R(u,v) se
nazývá resultant. Nad K je nulový právě při společném faktoru kladného
stupně: matice popisuje mapu (A,B)->Au+Bv pro deg(A)<n,deg(B)<m.
Společný faktor w dává nenulové jádro (v/w,-u/w). Naopak při coprimalitě
Au=-Bv implikuje u|B, což kvůli stupni nutí B=A=0.

Když poslední člen u_k je konstanta, konstrukce oddílu 3 má n_k=0
a je přesně Sylvesterovou maticí. Proto R=±h_k. Rozvinutím rekurence h:

```
R = ± product_(j=2)^k g_j^e_j,
e_j = delta_(j-1) product_(i=j)^(k-1) (1-delta_i).           (C)
```

To souhlasí s opravou odpovědi 12 z 8. prosince 2022. Starý vzorec
se při větších poklesech stupňů použít nesmí. Pro případ konce nulovým
zbytkem máme přímý důkaz jádrem matice; nemusíme dosazovat 0 do výrazů
s případnými zápornými exponenty.

Nad oborem S se tím detekují faktory kladného stupně; společné konstantní
neinvertibilní faktory samotný resultant nedetekuje. V kontextu primitivních
vstupů C to nezpůsobuje chybu.

**Dovětek 674.** V algebraickém uzávěru K pišme
u=a product_i(x-alpha_i), v=b product_j(x-beta_j). Po přechodu do
K[x]/(u) je determinant násobení polynomem v roven product_i v(alpha_i)
(nejprve pro různé kořeny; obecně jde o polynomiální identitu). S vedoucími
koeficienty Sylvesterovy matice dostaneme

```
R(u,v) = a^n product_i v(alpha_i)
       = (-1)^(mn) b^m product_j u(beta_j)
       = a^n b^m product_(i,j)(alpha_i-beta_j).
```

Diskriminant v charakteristice nula je
(-1)^(m(m-1)/2) R(u,u')/a; roven je
a^(2m-2) product_(i<j)(alpha_i-alpha_j)^2.
V kladné charakteristice je třeba pro univerzální diskriminant zachovat
formální stupeň derivace m-1, i když skutečný stupeň klesne.

Dosazení do součinového vzorce dává resultanty v x s kořeny v y
alpha_i+beta_j, alpha_i-beta_j, alpha_i beta_j a alpha_i/beta_j
pro u(y-x),u(y+x),x^m u(y/x),u(yx). U podílů je nutné v(0)!=0.
U součinů použijeme polynomiální tvar a product_i(y-alpha_i x), takže
není třeba dělit nulovým beta_j. Případný pokles stupně v x mění jen
nenulový konstantní násobek resultantu, nikoli jeho mn kořenů s násobností.

Menší determinant popsaný na p674 je také správný. Náhrada A_i uvedenou
lineární kombinací násobí plný determinant b_0^n. V posledních n sloupcích
mají upravené A-řádky i vysoké B-řádky nuly, zatímco spodní blok B má
determinant b_0^n. Po vykrácení zbývá přesně vytištěný m×m determinant.
Při b_0=0 platnost plyne jako polynomiální identita, bez neplatného dělení
nulou. Přesné kontroly zahrnují i tuto degeneraci.

## 5. Násobení společným primitivním faktorem; úloha 13

Nechť w je primitivní společný faktor s vedoucím koeficientem ell.
Porovnáváme posloupnost pro původní dvojici u_1,u_2 a pro w u_1,w u_2;
značení této druhé posloupnosti je U_i,G_i,H_i. Položme
p_j=n_1+n_2-2n_j. Správná transformace je

```
U_(j+1) = ell^(1+p_j) w u_(j+1),
G_(j+1) = ell^(2+p_j) g_(j+1),
H_j     = ell^p_j h_j,                    j>=2.           (D)
```

Důkaz je indukcí z pseudodělení:
prem(a w u,b w v)=a b^(delta+1) ell^(delta+1) w prem(u,v).
První krok má U_3=ell^(delta_1+1)w u_3 a H_2=ell^delta_1 h_2;
dosazení (D) do (A) a rekurence h dokončí indukci. Při všech delta_i=1
jde o mocniny ell^2,ell^4,ell^6,..., jak tvrdí (28).

**C0193 confirmed:** v odpovědi 13 jsou na pravé straně u_j,g_j;
mají být u_(j+1),g_(j+1). Už w=x, u_1=x^3+x+1,u_2=x^2+1 dává
u_3=1 a U_3=x, zatímco tištěný předpis by dal x^3+x. Pro chybný
index g stačí místo toho u_1=x^3+3x+1: u_3=2x+1, takže g_3=2,
ale g_2=1. Totéž w=x opět nechává vedoucí koeficient beze změny.

## 6. Dělitelnost při dvou větších poklesech; úloha 14

Položme s=deg(u)-deg(v)>=2 a předpokládejme deg(r)<=deg(v)-2.
Pro každý prvočinitel p vedoucího koeficientu v označme k jeho exponent,
P=p^k a j exponent p v předposledním koeficientu v_(n-1); n=deg(v).
Pokud v_(n-1)=0, použijeme větev j>=k. Pracujeme lokálně v p, takže
v_n/P je jednotka. Algoritmus R dává
q=a_0+P a_1 x+...+P^s a_s x^s.

Koeficienty x^(n+1),x^n,x^(n-1) součinu vq jsou násobky P^3.
První, po dělení P^2, dává

```
p^min(j,k) | a_1.
```

Je-li j>=k, druhý koeficient modulo P^2 rovnou dává P|a_0.
Je-li j<k a exponent t p v a_0 by byl menší než k, má první člen
a_0 v_(n-1) ve třetím koeficientu exponent t+j<k+j<2k;
druhý člen P a_1 v_(n-2) má exponent alespoň k+j a další členy alespoň
2k. První člen by tak měl jednoznačně nejmenší exponent a součet by
nemohl být násobkem P^3. Opět P|a_0, tedy P|q a P|r.
Pro všechna p dohromady to dává lc(v)|r.

**C0196 confirmed:** odpověď bez rozlišení případů tvrdí p^j|a_1.
To nemusí platit ani pro primitivní vstupy. Vezměme

```
u=2x^5+10x^4+11x^3+x^2,
v=2x^3+8x^2+4x+1,
q=8x^2+8x-4, r=8x+4;  8u=vq+r.
```

Pro p=2 máme j=3,k=1,P=2,a_1=4, ale 8 nedělí 4. Samotné zadání
úlohy zůstává pravdivé. Oprava výše pouze doplňuje vynechaný případ.

Při s=1 lze stejným rozborem koeficientů dokázat p^ceil(k/2)|r.
Pokud t=val_p(a_0)<k, koeficient x^n vynucuje
t=val_p(a_1)+j. Koeficient x^(n-1) pak vynucuje
t+j>=k+val_p(a_1), tedy 2t>=k+2val_p(a_1)>=k.
Vytištěný příklad u=x^3+1,v=4x^2+2x+1 má r=18 a ukazuje,
že plná dělitelnost lc(v) už neplatí.

Silnější závěrečný vztah je rovněž správný. Položme k_0=deg(r),
gamma=n-k_0. V matici z oddílu 2 použijme d=k_0+1, ale proveďme jen
náhrady A-řádků za x^s r, s=gamma-1,...,0. Trojúhelníkový minor
pro koeficient r_t dává

```
det(M_t) = ±lc(r)^(gamma-1) r_t / lc(v)^(s(gamma-1)).       (E)
```

Máme gamma náhrad, každou s faktorem lc(v)^(s+1), a zbývá s+gamma
vedoucích koeficientů lc(v) a gamma-1 koeficientů lc(r). Po vykrácení
vyjde (E), tedy přesně dělitelnost uvedená v poslední větě odpovědi 14.

## 7. Hadamard a koeficientové meze; úloha 15

Hadamardova nerovnost říká, že absolutní determinant je nejvýše součin
eukleidovských délek řádků. Gramova matice C=A A^T obsahuje jejich
skalární součiny. Postupné odečítání ortogonálních projekcí zachovává
determinant a nezvětšuje délky; na konci je determinant na druhou roven
součinu čtverců délek kolmých řádků. Při lineární závislosti je determinant
nula a nerovnost okamžitá; tím je ošetřen i nulový mezilehlý pivot.
Výpočet c_ii -> c_ii-c_ij^2/c_jj z odpovědi je správný, chápe-li se
současná operace na řádku a sloupci jako C -> E C E^T.

Minory v oddílech 2–3 mají nejvýše n řádků z u a m řádků z v.
Pokud vstupní koeficienty mají velikost nejvýše N>=1, jejich délky jsou
nejvýše N sqrt(m+1) a N sqrt(n+1). Normalizované u_i,g_i,h_i proto
splňují (26). Koeficienty primitivních zbytků algoritmu E jsou koeficienty
odpovídajících u_i vydělené jejich nenulovým celočíselným obsahem, takže
splňují tutéž mez. Samotná věta o obecných polynomiálních dělitelích by
takový závěr neumožňovala; zde jde o konstantní násobky.

**C0198 candidate:** tvrzení p432 o všech vypočítaných prvcích je nutné
číst jako tvrzení o normalizované posloupnosti. Pro
u=x^4+x^3+x^2+1,v=x^3-x^2-x+1 dostáváme normalizované zbytky
4x^2+x-1,-7x+11,32, ale poslední syrový zbytek C2 je 512.
Zde N=1,m=4,n=3 a čtverec (26) je 32000<512^2. Přímé certifikáty:

```
u = (x+2)v + (4x^2+x-1),
16v = (4x-5)(4x^2+x-1) + (-7x+11),
49(4x^2+x-1) = (-28x-51)(-7x+11) + 512.
```

Jde o rozsah formulace, ne o selhání algoritmu nebo determinantové meze
pro normalizované hodnoty. Proto zůstává kandidátem.

**C0197 confirmed:** tvrzení p433 o mezích N^3,N^7,N^17 pro obyčejné
pseudodělení bez normalizace opomíjí součty členů. Pro
u=x^3+x^2+x+1,v=x^2-x-1 máme N=1, ale

```
u = (x+2)v + (4x+3).
```

Následující zbytek je konstanta 5, takže všechny poklesy jsou skutečně 1.
Doslovná první mez N^3=1 tedy neplatí. Při poklesu 1 má každý koeficient
zbytku nejvýše čtyři trojné součiny: je-li velikost koeficientů u nejvýše
A a v nejvýše B, dostáváme mez 4AB^2. Položíme-li

```
alpha_1=alpha_2=1, alpha_i=2alpha_(i-1)+alpha_(i-2),
H_i=(2N)^alpha_i/2,
```

pak H_1=H_2=N a 4H_(i-2)H_(i-1)^2=H_i. Toto je platná obecná
mez pro normální posloupnost. Přesné řešení je
alpha_i=((1+sqrt(2))^(i-1)+(1-sqrt(2))^(i-1))/2.
Kvalitativní exponenciální růst počtu cifer zůstává správný; (27) je
pouze přibližný popis. Nepřidáváme nález za jeho index: exponent n
odpovídá poslednímu nekonstantnímu uloženému členu u_(n+1).

Také generičnost poklesu o 1 na p433 je správná. Podmínka většího poklesu
je vynulování příslušného vedoucího minoru. Tento minor není identicky
nulový: opačnou konstrukcí Eukleidovy posloupnosti s lineárními podíly
lze vytvořit posloupnost se všemi poklesy 1. Nad nekonečným tělesem jde
o vlastní algebraickou podmnožinu prostoru vstupů; pro konečné náhodné
množiny kvantifikuje pravděpodobnost (F), pro spojité rozdělení je nulová
množina pravděpodobnosti nula. Tvrzení se nevztahuje na libovolně zvolené
diskrétní rozdělení soustředěné na výjimečných vstupech.

## 8. Mřížkové kořeny; úloha 16

Nechť f není nulový polynom nad oborem integrity. Množiny S_j jsou
konečné neprázdné množiny a d_j<=|S_j| jsou meze stupňů v proměnné x_j.
Označme r množinu nulových vektorů v kartézském součinu S_1×...×S_n.
Rozepišme f=sum_k x_1^k g_k a vyberme nenulový g_k. Mimo kořeny g_k
má jednorozměrný polynom nejvýše d_1 kořenů, na kořenech g_k nejvýše
|S_1|. Indukce proto dává

```
|r| <= product_j |S_j| - product_j (|S_j|-d_j).             (F)
```

Rovnost nastává pro součin faktorů x_j-s_jk s d_j různými prvky
s_jk v každém S_j. Zde se použije známá oprava indexu z 17. ledna 2022.

Lze postupně volit f_(j+1) jako libovolný nenulový koeficient f_j
v proměnné x_j a d_j=deg_(x_j)(f_j). Stejná indukce dokazuje (F).
Pro dodatečný závěr sum d_j<=d, kde d je celkový stupeň f, však zvolíme
**vedoucí koeficient**: odebráním x_j^d_j klesne zbývající celkový
stupeň alespoň o d_j. Tím dostáváme pravděpodobnostní mez d/|S|.

**C0194 confirmed:** na p675 je jako jmenovatel počtu nulových vektorů
vytištěno |S| místo |S|^n. Pro f=x_1,S={0,1},n=2 jsou dva kořeny:
tištěná levá strana je 1, zatímco následující pravá strana je 1/2.

**C0195 candidate:** věta o sum d_j<=d bez upřesnění volby může být
čtena univerzálně, což vyvrací f=x+y a volba koeficientu x^0 rovného y:
d_1=d_2=1>d/2, d=1. Existenční čtení „můžeme vybrat koeficienty tak,
aby…“ je správné. Proto nejde o tvrzení, že Schwartzův–Zippelův odhad
je chybný; jde o navržené zpřesnění důkazu, ponechané jako kandidát.

Při 50 **nezávislých uniformních** vstupech a pravděpodobnosti nuly
nejvýše 1/2 je pro pevný nenulový f pravděpodobnost 50 nul nejvýše
2^-50. To je jednostranná chyba testu. Doslovné podmíněné tvrzení
P(f je nulový | všech 50 výsledků je nula) vyžaduje apriorní model pro f;
bez něj nevychází z uvedeného důkazu. Větu knihy lze číst jako obvyklou
zkratku pro spolehlivost testu; samostatný potvrzený nález zde nepřidáváme.

**Řídký polynom.** Jestliže f_j=x_j^e f_(j+1) a e>0, stačí d_j=1.
Je-li e=0, stačí d_j=0. Při více různých mocninách vybereme koeficient
s nejmenším počtem členů; má nejvýše polovinu členů f_j. Proto při m
nenulových členech nastane nejvýše floor(log_2 m) takových větvení,
a alespoň n-log_2 m proměnných má d_j<=1. Jde o jinou volbu cesty
koeficientů než u vedoucích koeficientů; obě zesílení se nemusejí současně
realizovat touž cestou. Konkrétní příklad na p675 d_1=3,d_2=1 je správný.

**Výpočet modulo prvočísla.** Nechť |f(x)|<=L, L>=1, a všechna
prvočísla z množiny P jsou alespoň q>1. Nenulová hodnota f(x) má
nejvýše log_q L různých prvočíselných dělitelů z P. Z (F) je nejméně
K=product_j(|S_j|-d_j) nenulových hodnot. Je-li |P|>=log_q L,
součtem přes hodnoty dostaneme horní mez

```
product_j |S_j| * |P| - K (|P|-log_q L).
```

V opačném případě je pravá strana alespoň velikost celého prostoru,
takže nerovnost platí triviálně. Tím je ošetřeno znaménko faktoru,
které by při pouhém násobení nerovností mohlo změnit směr.

## 9. Přesné kontroly a limity pramenů

`verify_subresultants.py` ukládá checkpointy do `results/subresultants.json`.
241 dvojic zahrnuje původní příklad, stejné počáteční stupně, větší poklesy,
společné faktory a různé vedoucí koeficienty. Koeficienty a h se nezávisle
porovnávají s determinanty původních vstupů; gcd má racionální Bézoutův
certifikát. Dalších 120 dvojic ověřuje (D). Dělitelnost má obecný důkaz
výše a přesné příklady; 600 konstruovaných dvojic je pouze podpůrná
kontrola pseudodělení, nikoli náhrada obecného důkazu.

240 vícerozměrných polynomů se vyhodnocuje na celých mřížkách; kontrolují
se čtyři druhy mezí. Další blok ověřuje 100 redukovaných determinantů
včetně b_0=0 a 60 součinových vzorců z explicitních celočíselných kořenů.
Úspěšné checkpointy se při doplnění nových otázek neopakují.

Brownův–Traubův původní článek je uložen ze sbírky CMU; zatím byl
přečten úvod a příslušné bibliografické údaje, nikoli znovu celý článek.
Matematický důkaz algoritmu je vlastní důkaz výše. Loosův záznam u Springeru
potvrzuje kapitolu o algebraických rozšířeních, Computing Supplementum 4,
173–187 (1982); abstrakt výslovně popisuje aritmetiku algebraických čísel
pomocí resultantů. Celá kapitola zatím přečtena není.
Schwartzův článek 701–717 (1980) se nepodařilo získat: indexované
odkazy PDF při stažení vracejí 404, ACM vrací 403. Nezaměňujeme
náhled za přečtený článek. Navazující [fast-sturm.md](fast-sturm.md)
již dává úplný matematický důkaz rychlé kompaktní reprezentace,
nezávislý na dostupnosti tohoto historického originálu.

Relevantní vrstvy errat: all2-prepre, all2-pre, all2, err2, aktuální TeX;
historická errata 2. vydání byla také prohledána podle tématu, s vědomím
odlišného stránkování. Náhrada odpovědi 16 pro starou stranu 620
z 20. dubna 1995 již obsahuje chybný jmenovatel i neupřesněnou volbu
koeficientu; nejde o jejich opravu. Staré změny odpovědi 15 jsou ve
3. vydání již zapracovány. Opravy C0193,C0194,C0196,C0197 v těchto
pramenech nenalezeny; nejnovější fyzický dotisk a prvenství neověřeny.
Nic neodesláno.
