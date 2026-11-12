# §4.6.3: Hansenova struktura, věty H/F a úlohy 19–22

Stav: **checked v níže vymezeném rozsahu**, 4. listopadu 2026.
Kontrolovány strany 473 od odstavce o Hansenovi až 477 první odstavec,
zadání 19–22 na 483 a odpovědi 694–695. Definice označeného řetězce
na 479 je zahrnuta, věta G a pozdější historická tvrzení zatím nikoli.
Původní sazba všech uvedených stran byla zobrazena. Tištěný exemplář
ověřen není. Nový **C0225 zůstává pouze kandidátem** na doplnění oboru
Dirichletovy řady; žádná z vět H/F tím není dotčena.

## 1. Značení a multisety

Sčítací řetězec je rostoucí posloupnost `1 = a_0 < ... < a_r = n`,
v níž je každý nový člen součtem dvou dřívějších. Jeho délka je r.
Hvězdový řetězec navíc používá bezprostředně předchozí člen:
`a_i = a_(i-1) + a_k`. Označení `l(n)` a `l*(n)` znamenají nejmenší
délku obecného a hvězdového řetězce. Dále `lambda(n) = floor(log_2 n)`
a `nu(n)` je počet jedniček v binárním zápisu kladného celého n.
Malý krok nezvyšuje lambda; jejich počet je `s = r - lambda(n)`.

**Multiset** zaznamenává prvky i jejich násobnosti. Formálně násobnost
`mu_A(x)` udává počet výskytů x v A. V tomto důkazu jsou všechny multisety
konečné. Sjednocení A union B má násobnost max, průnik min a disjunktní
součet A uplus B součet obou násobností. Posun A+h posune každý výskyt
o h; součet přes multiset počítá každý výskyt zvlášť.

Úloha 19(a): prvočíselné rozklady převádějí gcd na minimum násobností,
lcm na maximum a násobení na jejich součet. Číslo 1 odpovídá prázdnému
multisetu. V části (b) platí totéž pro kořeny monických komplexních
polynomů, protože každý takový polynom je součin faktorů `z-alpha`.
Konstantní monický polynom je 1; nulový polynom do oboru nepatří.

Všechny identity 19(c) jsou bodové identity nezáporných celých čísel:
komutativita a asociativita +/min/max; obě distributivity min/max;
`a+min(b,c)=min(a+b,a+c)` a analogie pro max; idempotence a absorpce;
`min(a,0)=0`, `max(a,0)=a`, `a+0=a`; a konečně
`a+b=min(a,b)+max(a,b)`. Poslední vztah je uvedený počítací zákon.
Také `A subset B` právě když min(mu_A,mu_B)=mu_A, ekvivalentně
max(mu_A,mu_B)=mu_B. Nejde o pouhé ověření několika příkladů.

## 2. Rozložení hvězdového řetězce

Nechť d_i je počet zdvojení do kroku i, d=d_r a f=r-d. Definujeme
`S_0={0}`. Zdvojení posune všechny exponenty o 1; při jiném kroku
`a_(i+1)=a_i+a_k`, k<i, položíme `S_(i+1)=S_i uplus S_k`.
Indukcí dostáváme

```
a_i = sum_(x in S_i) 2^x,
max S_i = d_i,
|S_r| <= 2^f.
```

Při nezdvojení je `d_k <= d_i`, takže se maximum nemění. Počet výskytů
se zdvojením nemění a jiným krokem se nejvýše zdvojnásobí.

Pišme `n = 2^e_0 + ... + 2^e_t`, kde `e_0 > ... > e_t >= 0`.
Seřazený S_r lze rozdělit do po sobě jdoucích skupin M_t,...,M_0,
jejichž váhy jsou po řadě `2^e_t,...,2^e_0`; váha je součet `2^x`.
Pro přesné zdůvodnění nejnižší skupiny vezměme první člen `2^x`, při
jehož přidání dosáhneme nebo překročíme `2^e_t`. Předchozí součet S
je menší než tento cíl a n-S je dělitelné `2^x`, protože všechny
zbývající členy jsou alespoň tak velké. Pokud x<=e_t, je S násobkem
`2^x` a překročení není možné. Pokud x>e_t, zbytek n modulo `2^x`
je alespoň `2^e_t`, ale měl by se rovnat S, což je spor. Odstraníme
tuto skupinu a opakujeme pro další jedničku n.

Položme `m_j=|M_j|`. Všechny t+1 skupiny jsou neprázdné, proto
`m_j <= 2^f-t`. Platí přesně knižní (39):

```
e_j >= x > e_j-m_j  pro každý výskyt x v M_j.
```

Důkaz dolní meze: při zápisu jediné mocniny jako součtu m mocnin
lze opakovaně spojit dva nejmenší stejné členy. Nejmenší člen má
vždy sudou násobnost, není-li už jediný. Tím vznikne binární strom
s m listy a kořenem `2^e`. Cesta k listu `2^x` má délku e-x;
každé její větvení vyžaduje alespoň jeden další list, takže
`e-x <= m-1`. Horní mez plyne přímo z kladnosti sčítanců.

Skupiny `M_(i,j)` se zpětně přenesou až k S_0: při zdvojení
odečteme 1 od exponentů; při součtu odstraníme výskyty S_k,
při nejednoznačnosti vždy ze skupiny s největším j. Tím každý
S_i zůstává disjunktním součtem svých skupin. Každý přeživší výskyt
skupiny j je předkem některého výskytu M_j, posunutým o `d_i-d`.
Odtud (40), a navíc užitečná mez na celou váhu W_(i,j):

```
e_j+d_i-d >= x > e_j+d_i-d-m_j,
W_(i,j) = sum_(x in M_(i,j)) 2^x <= 2^(e_j+d_i-d).
```

Také `d_i in M_(i,0)`, tedy (41). V koncové řadě leží maximum
v nejvyšší skupině. Při zpětném zdvojení se toto tvrzení zachová.
Při odstraňování zůstane v S_i alespoň jeden výskyt maxima d_i;
pravidlo odstraňování od největšího j zajistí, že zůstane ve skupině 0.

Má-li celé číslo x výskyt v M_(i,j) i M_(u,v), spojení obou mezí (40)
dává přesně lemma K:

```
-m_v < (e_j-e_v)-(d_u-d_i) < m_j.
```

Tabulka pro řetězec `1,2,3,5,10,20,23` byla zkontrolována po všech
výskytech, včetně dvou kopií 2 v M_(4,0). Žádná z rovností (38)–(42)
nevyžaduje dodatečnou podmínku nebo opravu.

## 3. Věta H: úplný důkaz včetně přenosů

Pro t>=3 položme `m = 2^floor(3.271(t-1))-t`. Předpoklady jsou

```
e_0 > 2e_1 + 2.271(t-1),
e_(j-1) >= e_j + 2m  pro 1<=j<=t.
```

Druhá nerovnost je v původní sazbě **neostrá**. Při t<=2 dává
`l*(n)=e_0+t` již předchozí rozbor B/C. Binární metoda dává stejnou
horní mez pro všechna t. Pro spor proto uvažujme hvězdový řetězec
délky `r<=e_0+t-1`, takže `s<=t-1`. Důsledek A, již samostatně
dokázaný v `powers-structure.md`, dává `f<=floor(3.271s)` a tím
`m_j<=m` pro všechny j.

Nejdříve zdůvodníme (44). Skupina M_(i,0) je neprázdná podle (41).
Nechť L je její nejmenší exponent a W její váha. Součet ostatních
vah je menší než `2^(e_1+d_i-d+1)`, neboť e_j jsou různé klesající
celé exponenty. Z (40), m_0<=m a mezery e_0-e_1>=2m plyne, že
tento součet je menší než `2^L`. Číslo W je násobkem `2^L` a W>=2^L.
Přidání méně než `2^L` proto nemůže překročit následující mocninu dvou.
Tedy `lambda(a_i)=lambda(W)` a

```
a_i >= W_(i,0) >= 2^lambda(a_i).
```

Pro každé j>=1 vyberme první i, kdy M_(i,j) není prázdná. Takové i
existuje, protože na konci je M_j neprázdná, kdežto S_0={0} patří
celá skupině 0. Krok i je nezdvojení `a_i=a_(i-1)+a_u`, u<i-1.
Všechny nové výskyty skupiny j pocházejí ze S_u. Vyberme jeden x_j
a jeho skupinu M_(u,v). Kdyby `d_i-d_u<=m`, dává lemma K
`|e_j-e_v|<2m`. Mezery exponentů vynutí v=j, což odporuje volbě i.
Máme tedy `d_i-d_u>m`, rovnost (45).

S_u nemá žádný exponent společný s M_(i,0). Kdyby společný x
existoval, z dolní meze (40) pro M_(i,0) a z e_0-e_1>=2m plyne
`x>e_1+d_i-d>=e_1+d_u-d`, takže ve S_u může patřit jen M_(u,0).
Lemma K s j=v=0 by však dalo `|d_i-d_u|<m`, spor. Odtud také každý
x v S_u splňuje `x<=e_1+d_i-d`. Nejvyšší skupina se při kroku i
nezmění, tedy (44) dává `a_(i-1)>=2^lambda(a_i)`. Krok i je malý.

Klíčově všechny výskyty S_u patří do M_(u,0). Kdyby některý patřil
jinam, jeho nezápornost a (40) by daly `e_1>=d-d_u`. Protože
`e_0=r-s=f+d-s`, dostáváme

```
e_0 <= 2.271s+d <= 2.271(t-1)+e_1+d_u.
```

První předpoklad H nyní vynucuje d_u>e_1. Ale `d_u in S_u` podle
(41) a předchozí odstavec dává `d_u<=e_1+d_i-d<=e_1`, spor.

Vybraný x_j proto podle (40) leží v intervalu
`(e_0+d_u-d-m_0, e_0+d_u-d]`, tedy splňuje (46). Pokud by dva různé
indexy j,j' měly stejný první krok i, měly by i stejné u. Jejich
vybrané exponenty by se lišily o méně než m. Naproti tomu (40),
m_j<=m a odstup nejméně 2m mezi e_j a e_j' dávají rozdíl větší
než m. Každé j proto potřebuje vlastní malý krok. Je jich alespoň t,
v rozporu se s<=t-1. To uzavírá důkaz H i pro rovnost v mezerné podmínce.

## 4. Věta F a označené řetězce (úloha 22)

Nechť x,y jsou kladná celá čísla a A nezáporné celé číslo s
`lambda(x)+lambda(y)<=A`. Označme sestupně exponenty jedniček x
jako x_1,...,x_u a y jako y_1,...,y_v. Věta tvrdí

```
l(2^A+xy) <= A+u+v-1.
```

Sestrojíme všechny mocniny dvou do `P=2^(A-y_1)` a u-1 částečných
součtů x, budovaných od nejnižšího bitu. Jejich společný seznam
seřadíme. Každý částečný součet vzniká přičtením dřívější mocniny
k dřívějšímu částečnému součtu; všechny potřebné mocniny jsou přítomny.
Pokud `lambda(x)+lambda(y)=A` a u>1, leží poslední součet x **až za P**.
To není překážka: první další člen P+x je větší než oba. Tím je
ošetřen i hraniční případ, který formulace „in between“ stručně přechází.

Počínaje P opakujeme pro každý bit y: přičti x a zdvoj výsledek
tolikrát, kolik je mezera k následujícímu bitu; za poslední bit
formálně připojíme exponent 0. Hornerův invariant dává na konci
přesně `2^A+xy`. Mocniny v úvodní části vyžadují A-y_1 kroků,
pozdější zdvojení celkem y_1, vložené součty u-1 a přičtení x
celkem v. Celkem je to A+u+v-1 kroků. Platí i x=y=1, A=0.

**Označený neboli l^0-řetězec** má některé členy podtržené a každý
nový člen je součtem posledního menšího podtrženého členu a nějakého
dřívějšího členu. Označení `l^0(n)` je jeho nejmenší možná délka.
Podtrhneme všechny členy konstrukce F kromě u-1 vložených součtů x.
U vloženého součtu s nejvyšším bitem x_j je předchozí podtržený člen
`2^x_j` a rozdíl je předchozí částečný součet. Následující mocnina
vzniká zdvojením předchozí podtržené mocniny. V Hornerově části
jsou všechny kroky podtržené a hvězdové. Důkaz platí i když x>P.
Tím je plně ověřena odpověď 22 a silnější mez pro l^0.

Příklad na 476–477 má exponenty 6103,3048,2032,1016,0, tedy t=4
a m=508. Nejmenší mezery jsou **rovny** 2m=1016, což H dovoluje;
`6103>6096+6.813`. F s x=2^1016+1 a y=2^2032+1 dává 6106,
H dává hvězdové minimum 6107. Obecné minimum 6106 se zde netvrdí.

## 5. Úlohy 20 a 21

V úloze 20 jsou A,C,D parametry typů jednosmall řetězců ze strany 468.
Typ 3 má A>=1, C>=2: po mocninách do 2^A následují
`3*2^(A-1),5*2^(A-1),2^(A+2),...,2^(A+C)`. Koncové číslo je mocnina,
takže všechny S_i jsou M_(i,0). Jejich poslední trojice vzorů je
`{A-1,A}`, `{A-1,A,A}` a poté zdvojované posuny
`{A-1,A-1,A,A,A}`. To je přesně tištěný pětivýskytový poslední člen.

Typ 5 má A>=1, C>=1, D>=0: po `3*2^(A-1)` následuje C zdvojení,
pak `2^(A+C+1)+2^(A+C-2)` a D zdvojení. Nejnižší koncová skupina
se poprvé objeví při posledním nezdvojení, jako `{A+C-2}`.
Nejvyšší skupina se tehdy změní z `{A+C-1,A+C}` na
`{A+C-1,A+C-1,A+C}`. Další řádky jsou jen posuny. To dokazuje obě
tištěné řady včetně C=1 a D=0.

Pro úlohu 21 nechť q>=1 a `u=2^(8q+5)`. Položme

```
x = 1+2^u+...+2^(qu),   y = 1+2^((q+1)u),
n = 2^(4(q+1)u) + xy.
```

Součin xy má bez přenosů právě bity `0,u,...,(2q+1)u`, tedy 2q+2
jedniček. Pro n je proto t=2q+2. F dává délku nejvýše
`4(q+1)u+q+2`. Pro H stačí ověřit mezery a první podmínku:

```
2m < 2^(6.542q+4.271) <= 2^(8q+5) = u,
e_0-2e_1 = 2u > 2.271(2q+1).
```

Poslední nerovnost například plyne z `2^(8q)>=q+1`, tedy
`2u>=64(q+1)`. H dává `l*(n)=4(q+1)u+2q+2`, takže
`l*(n)-l(n)>=q`. Jde o obecný důkaz pro všechna q, nikoli extrapolaci
prvních sta parametrů ověřených programem.

## 6. Poznámky k úloze 19 a kandidát C0225

Součet a součin obyčejných generujících řad dávají uvedené operace
na multisetech přímo porovnáním koeficientů. Pro Dirichletovy řady
`g(z)=sum_(n in A) n^(-z)` odpovídá součin řad multisetu párových
součinů AB, pokud A a B obsahují kladná celá čísla. Pro konečné
multisety není otázka konvergence; pro nekonečné používáme formální
řady, případně obor absolutní konvergence.

**C0225, candidate, minor:** odstavec na 695 nejprve výslovně dovoluje
nezáporné prvky A, potom bez nového omezení píše Dirichletovu řadu.
Při A={0} a z=1 obsahuje nedefinované 1/0. Doplňující podmínka
`0 notin A,B` je proto matematicky nutná. Neoznačujeme to zatím
za potvrzenou chybu: slova „If we form“ lze rozumně číst jako implicitní
omezení na případy, kdy příslušnou Dirichletovu řadu vůbec lze utvořit.
Ve všech šesti vrstvách errat nebyla nalezena odpovídající oprava.

Pro tvrzení o gramatikách je násobností **počet rozborových stromů**,
nikoli počet všech pořadí přepisovacích kroků. U konečné bezkontextové
gramatiky bez cyklu `A =>+ A` má každý terminální řetězec konečně mnoho
rozborů: na cestě stromem nelze zopakovat stejný neterminál se stejným
intervalem výsledného slova, protože boční větve by pak vytvořily
prázdné slovo a vznikl by zakázaný cyklus. Počet neterminálů i intervalů
je konečný, takže je omezená hloubka i velikost stromu. Množina místo
multisetu tedy vzniká právě při jednoznačnosti gramatiky.

Primární autorův preprint P139, *Context-Free Multilanguages*, byl
stažen z jeho [seznamu preprintů](https://www-cs-faculty.stanford.edu/~knuth/preprints.html).
Přečteny řádky 1–240 a 321–330: definice násobností, součinová operace,
rozbory a přesný význam necirkularity souhlasí. Rok, editor a strany
1992, Ullman, 1–13 souhlasí s autorovou publikací P139 v jeho
[bibliografii](https://cs.stanford.edu/~knuth/vita.pdf).
Soukromé rozhovory o názvu „multiset“ a připsání de Bruijnovi bereme
jako autorovo historické svědectví; nezískali jsme samostatný dobový
zápis těchto rozhovorů a netvrdíme nezávislý důkaz prvenství názvu.

## 7. Primární Hansenův článek a errata

Celý původní článek *Zum Scholz-Brauerschen Problem*, Crelle 202 (1959),
129–136, byl získán z [Göttingenské digitální knihovny](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0202/LOG_0011.pdf)
a všech osm stran vizuálně přečteno. Soubor má úvodní knihovní list,
takže souborová strana 2 je tištěná 129. Textový výstup obsahuje pouze
knihovní metadata, nikoli OCR článku. Na 136 je datum přijetí 29. 5. 1958;
1959 je rok vydání. Jeho pomocná věta používá hrubší meze s 16^N,
Satz 1–2 dávají neomezené rozdíly a konstrukci předcházející F,
Satz 3 předchází G. Knuthovu ostřejší verzi H jsme dokázali výše;
nepřipisujeme původnímu článku doslova konstanty 3.271 a 2.271.
Satz 3 je nyní přečten, jeho podrobný audit patří do navazujícího bloku.

Porovnány `all2-prepre`, `all2-pre`, `all2`, `err2`, `err2-2e`
a původní `err2.textxt`, pomocí `sources/powers-basic-errata.txt`
i hledání souvisejících termínů. Relevantní známá oprava 23. 10. 2006
na 475 doplňuje M_j do úvodního seznamu multisetů. Je přijata jako
**known_erratum**, nikoli nový nález. Další známá oprava z 18. 12. 2000
na 483 doplňuje chybějící faktor p za součinové znaménko v zadání 19(a).
Původní sken tuto drobnou vadu potvrzuje; správná formule je
`product_(p in N) p = n`. Tato položka byla při zápisu prvního checkpointu
opomenuta a doplněna při kontrole navazujícího bloku, bez opakování testů.
Žádná oprava H/F nebo 20–22
nenalezena. OCR záměny >= za > nejsou chyby knihy.

## 8. Reprodukovatelné kontroly a přesný rozsah

`verify_powers_hansen.py` má tři oddělené bloky s ochranou proti opakování
již úspěšného běhu. Vše prošlo napoprvé, session 23733, limit každého
bloku 240 s, PID 1351343/1351345/1351347, všechny exit 0:

- `partition`: 43 757 multisetů s 1–10 výskyty a exponenty 0–7,
  183 090 výsledných skupin; váhy, úplnost a ostrá mez (39).
- `structure`: všech 46 234 hvězdových řetězců délky nejvýše 8,
  nezávislé váhy všech řádků, (40)/(41), 6 204 228 porovnání K,
  celá tištěná tabulka a 56+576 parametrů obou rodin odpovědi 20.
- `construction`: 49 152 řetězců pro 1<=x,y<=128, z toho 16 384
  přesně na hranici A=lambda(x)+lambda(y); samostatná kontrola
  všech sčítanců, délky a podtržení. Dále skutečný 6106krokový
  velký příklad a exponentová kontrola q=1,...,100 pro úlohu 21.

Časy jsou 1.150820814, 6.095253995 a 1.024878870 s, celkem
8.270953679 s. Nepočítáme znovu žádná dříve ověřená minima řetězců.
Konečné testy doplňují výše uvedené obecné důkazy, nenahrazují je.
Další práce: číslo 12509, van Leeuwen, text 477–481 a úlohy 23–43.
