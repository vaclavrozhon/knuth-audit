# §3.5-20–21: délky mezer, jednoznačnost a minimax

Stav 1.11.2026. Zadání181 a odpovědi594–595 přečteny v původní sazbě
(třetí vydání, první tisk1997; pořadí stran DjVu je o12 vyšší).
Všechny vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální TeX
prohledány podle stran i témat Ramshaw a mezer; odpovídající opravy
nenalezeny. V2-C0064 a V2-C0065 jsou potvrzené v těchto zdrojích,
nikoli potvrzení prvenství, odměny či stavu posledního fyzického dotisku.
Nic nebylo odesláno.

Primární podklad: L. H. Ramshaw, *On the gap structure of sequences
modulo one*, Stanford CS-TR-77-637 (1977), vlastní zdroj
`sources/ramshaw-1977-gap-structure.pdf` s metadaty a SHA-256.
Text zprávy1–26 přečten; klíčové důkazy a obrázky na9–14,17–20,24–25
navíc vizuálně. OCR strany17 bylo prázdné, její obsah čten z obrazu.
Publikace1978 v Indagationes Math.40,527–541 odpovídá odkazu knihy;
plný časopisecký PDF jsme nečetli. Primární autorská zpráva výslovně
rozlišuje posloupnost bodů a strategii délek mezer.

## 1. Značení a význam majorizace

Stav S_n je sestupně seřazená n-tice délek mezer po vložení prvních n
bodů U_0,...,U_(n−1), přičemž U_0=0. Délky l_n^(1)>=...>=l_n^(n)>=0
mají součet1. Každý další bod rozdělí jednu mezeru na dvě; opakovaný
bod dovoluje nulovou délku. Největší a nejmenší mezera určují

```
L_upper = limsup n*l_n^(1),
L_lower = liminf n*l_n^(n).
```

Značíme lg logaritmus o základu2 a ln přirozený logaritmus.
Logaritmický profil je n-tice

```
L_n(j) = lg((n+j)/(n+j−1)),  j=1,...,n.
```

Pro dva stejně dlouhé sestupné vektory délek se stejným součtem píšeme
S >=_maj T, jestliže každý součet k největších souřadnic S je alespoň
odpovídající součet T. To je **majorizace**: S je v tomto smyslu méně
vyrovnané rozdělení. Pro různé délky použijeme lomenou čáru A_S(t),
která v bodech t=k/n nabývá součtu prvních k složek a mezi nimi je
lineární. Píšeme S >=_maj T, jestliže A_S(t)>=A_T(t) na[0,1].

Rozdělení každé složky na r stejných dílů nemění A_S. Tak lze dvě
různě dlouhé n-tice porovnat po rozdělení na společný počet dílů.
Předpoklady o funkcích f_n v21(c) tedy přesně říkají, že funkcionál
f(S)=f_n(S) zachovává majorizaci a nezmění se tímto rovnoměrným dělením.
Spojitost používáme vždy jen v jedné pevné konečné dimenzi.

## 2. Úloha20: obecné optimální meze

(a) U van der Corputovy posloupnosti jsou při n=2^r všechny mezery
rovny2^(−r). Následujících2^r vložení půlí po jedné dosavadní největší
mezery. Pro 2^r<n<2^(r+1) je maximum2^(−r) a minimum2^(−r−1).
Proto L_upper=2 a L_lower=1/2, jak uvádí odpověď.

(b) Prvních k největších mezer stavu n nelze všechny rozdělit k−1
novými body. Proto l_(n+k−1)^(1)>=l_n^(k). Položíme-li
p_n=max_(n<=m<=2n−1) m*l_m^(1), dostaneme

```
1 = sum_(k=1)^n l_n^(k)
  <= sum_(k=0)^(n−1) l_(n+k)^(1)
  <= p_n * sum_(k=0)^(n−1) 1/(n+k).
```

Poslední harmonický součet konverguje k ln2, takže L_upper>=1/ln2.

(c) Konečná mezera stavu2n s koncovými body U_m,U_m' vznikne nejpozději
ve stavu 1+max(m,m'). Definujme její opravený index

```
a = max(m+1−n,m'+1−n,1).
```

Je v{1,...,n}; daná mezera je alespoň tak dlouhá jako nejmenší mezera
stavu n+a. Když oba konce již existovaly ve stavu n+1, použijeme tento
stav. Jinak použijeme stav bezprostředně po vložení pozdějšího konce.
Každý index a=2,...,n patří nejvýše dvěma konečným mezerám: nově vložený
bod má nejvýše dva sousedy. U stejné polohy více bodů je toto tvrzení
platné i po pevném uspořádání podle indexů; nulové mezery nevadí.

Pro rho_n=min_(n+1<=m<=2n) m*l_m^(m) tedy platí

```
1 >= rho_n * sum_(k=1)^(2n) 1/(n+a_k)
  >= 2*rho_n * sum_(a=1)^n 1/(n+a).
```

Druhá nerovnost plyne z klesání vah1/(n+a): u každé hodnoty a>=2 jsou
nejvýše dva výskyty; minimální součet2n vah proto má dva výskyty každé
hodnoty1,...,n. Přebytek u a=1 může součet jen zvětšit. S H_n=sum1/j
vychází rho_n<=1/[2(H_(2n)−H_n)], a tedy L_lower<=1/(2ln2)=1/ln4.

**V2-C0065.** Tištěná odpověď594 místo toho používá
`max(m−n,m'−n,1)`. Pro n=2 a prefix

```
U_0=0, U_1=1/2, U_2=1/4, U_3=1/8
```

má konečná mezera mezi U_0 a U_3 délku1/8. Tištěný index a=1 ji
porovnává s nejmenší mezerou stavu3, která má délku1/4. Požadovaná
nerovnost1/8>=1/4 neplatí. Opravené a=2 ji porovnává se stavem4.
Totéž selhání nastává pro mezeru mezi U_3 a U_2. Hlavní věta20(c) platí;
chyba je v tomto pomocném indexu. Draft:
`reports/C0065-gap-birth-index-draft.txt`.

(d) Pro W_n=lg(2n+1) mod1 mají mezery po prvních n bodech štítky
j=n,...,2n−1 a délky lg((j+1)/j). Indukce: nový bod W_n rozdělí mezeru
se štítkem n mezi body lg(2n) mod1 a lg(2n+2) mod1 na mezery se štítky
2n a2n+1. Je to právě dosavadní největší mezera. Přechod přes kraj0
je kruhový, ale protože U_0=0, odpovídá i rozdělení jednotkového intervalu.
Sestupný profil je L_n a teleskopický součet jeho prvních k složek je

```
sum_(j=1)^k L_n(j) = lg((n+k)/n) = lg(1+k/n).
```

Z nerovností x/(1+x)<ln(1+x)<x pro x>0 dostaneme pro všechna n

```
n*L_n(1) < 1/ln2,
n*L_n(n) > 1/(2ln2).
```

Příslušné limity jsou rovny pravým stranám. W tedy dosahuje obou
optimálních asymptotických mezí a zároveň ostrých konečných nerovností.

## 3. Úloha21(a): logaritmická posloupnost není ekvidistribuovaná

Nechť nu(N) je počet j<N s W_j<1/2. Položme
N_m=2^m a A_m=ceil(2^(m−1/2)). V každém pásmu mezi po sobě jdoucími
mocninami2 lze podmínku zapsat jako nerovnost pro liché číslo2j+1.
V posledním pásmu již mezi A_m a N_m nepřibývá žádný příspěvek. Proto

```
nu(A_m) = nu(N_m)
        = (sqrt(2)−1)*2^m + O(m).
```

Odhad plyne sečtením polovin délek intervalů
[2^h,2^(h+1/2)), h=0,...,m; zaokrouhlení každého přidá nejvýše konstantu.
Tudíž nu(A_m)/A_m jde k2−sqrt(2), zatímco nu(N_m)/N_m jde ksqrt(2)−1.
Tyto hodnoty jsou různé. Sazba595 má správné stropy i chybový člen.

## 4. V2-C0064: úloha21(b) zaměňuje body a mezery

Podmínka v zadání181 je nerovnost součtů mezer <=lg(1+k/n).
Nedefinuje jednoznačně posloupnost bodů. Položme

```
Z_0=0,
Z_n=1−W_n  pro n>=1.
```

Pro n>=1 není liché číslo2n+1 mocninou2, takže0<W_n<1 a také0<Z_n<1.
Odraz x->1−x zachovává oba krajní body intervalu jako množinu a obrací
pořadí mezer. Proto W a Z mají pro každé n totožné seřazené mezery a
všechny uvedené nerovnosti splňují dokonce s rovností. Jsou však různé:
W_1=lg(3/2), kdežto Z_1=lg(4/3).

Správné tvrzení: každá posloupnost splňující nerovnosti má při každém n
seřazený profil L_n. Jednoznačná je tedy posloupnost **multimnožin délek
mezer**, ne jejich umístění jako bodů. To odpovídá větě2 primární
Ramshawovy zprávy, str.17, jejíž strategie jsou definovány právě délkami.
Draft: `reports/C0064-gap-sequence-uniqueness-draft.txt`.
Následující dva oddíly dokládají i kladnou část tvrzení21(b,c).

## 5. Ramshawovo srovnávací lemma a správná jednoznačnost

Perfektní úsek se skládá ze stavů P_(n,n),...,P_(n,2n): začneme
sestupnými délkami s_1,...,s_n, kde s_n>=s_1/2, a postupně jednou
rozpůlíme každou z původních mezer v sestupném pořadí. Po k rozděleních
je profil (s_(k+1),...,s_n,s_1/2,s_1/2,...,s_k/2,s_k/2), již seřazený.

Srovnávací lemma říká, že každý jiný úsek S_n,...,S_(2n) má některý
stav S_(n+k)>=_maj P_(n,n+k), 0<=k<n. Ramshawův důkaz na9–14 byl
zkontrolován; následuje jeho úplný mechanismus.

Rozdělení mezer v úseku tvoří les n kořenů a n vnitřních uzlů. Pokud
některá původní mezera a zůstala nerozdělena (atom), jiný kořen má
větev l_0>=l_1>=...>=l_p s p>=2; vybereme nejhlubší větev, takže
poslední rozdělení má dvě listové děti. Lze odstranit jeden atom a
současně všechny stavy jen zlepšit v majorizaci:

- Je-li a>=l_(p−1), provedeme poslední rozdělení v atomu a namísto
  v l_(p−1). Po něm se dvojice (a,l_p) změní na
  (l_(p−1),a+l_p−l_(p−1)); součet je stejný a oba nové členy leží mezi
  starými. Druhé listové dítě l_(p−1)−l_p je stejné. Dřívější stavy
  se nezmění a další rozdělení dotčených listů již v úseku nejsou.
- Je-li a<l_(p−1)<=l_1, změňme od začátku kořeny (a,l_0) na
  (l_1,a+l_0−l_1). Obě nové délky leží mezi a a l_0. V čase původního
  prvního dělení l_0 rozdělíme nový druhý kořen na a a l_0−l_1.
  Od této chvíle jsou všechny stavy stejné jako původně. Oba nové
  kořeny se během úseku rozdělí, protože p>=2.

Zlepšení dvojice se stejným součtem zachovává majorizaci i po přidání
ostatních délek. Po konečně mnoha úpravách nezbude atom, takže každá
původní mezera byla rozdělena právě jednou. Jejich délky t_1,...,t_n
indexujeme časem rozdělení, nikoli velikostí.

Protože sum(t_i−s_i)=0, cyklické posunutí za minimum prefixových součtů
má všechny částečné součty t alespoň stejně velké jako součty s.
Nechť posun začíná k+1. V koncové části nahradíme každé t_i dvěma
dětmi, větší dítě první; s_i nahradíme dvěma polovinami. Nerovnosti
ve sudých mezikrocích zůstávají stejné a v lichých plynou zprůměrováním
sousedních nerovností, protože větší dítě má délku alespoň t_i/2.
Cílový vektor je právě seřazený P_(n,n+k). Seřazení skutečného vektoru
zvětší součty největších složek. Srovnávací lemma je dokázáno.

Aplikujme je na s=L_n. Křivka perfektního stavu s m=n+k mezerami
interpoluje E(t)=lg(1+t) v uzlech

```
0, 1/m, ..., (2n−m)/m, (2n−m+2)/m, ..., (m−2)/m, 1.
```

Uvažujme posloupnost splňující21(b), tedy A_(S_m)<=E pro každé m.
Její polygon je tudíž nejvýše A_(L_m), protože je mezi vlastními uzly
lineární. Srovnávací lemma dává pro některé m z[n,2n−1]
L_m>=_maj S_m>=_maj P_(n,m).

Je-li m>n, krajní profily mají stejný součet dvou nejmenších složek
lg(m/(m−1)); díky shodě křivek v(m−2)/m jej má i S_m. Zpětné sloučení
skutečně rozdělené dvojice vytvoří mezeru ve S_(m−1), jehož maximum
je nejvýše lg(m/(m−1)). Sloučená dvojice proto musí být dvěma
nejmenšími délkami, až na shodné délky. Po jejich odstranění zůstane
majorizace ostatních délek a přidání společného součtu ji zachová.
Tak dostaneme S_(m−1)>=_maj P_(n,m−1), zatímco opačné omezení L_(m−1)
platí z předpokladu. Opakováním zpět do n získáme S_n=L_n. Pro m=n
je to ihned. Jelikož n bylo libovolné, správná jednoznačnost platí.

## 6. Úloha21(c): minimax pro celou třídu funkcí

Síť uzlů perfektních polygonů má mezery nejvýše2/m. Jejich křivky proto
konvergují rovnoměrně k E, rovnoměrně i pro všechny n<=m<=2n.
Pro pevné j a0<epsilon<1 zaveďme pozitivní profil

```
T_(j,epsilon) = (1−epsilon)*L_j + epsilon*(1/j,...,1/j).
```

Jeho křivka leží striktně pod E na(0,1), protože A_(L_j)<=E a t<E(t)
pro0<t<1. Stačí porovnat konečně mnoho vnitřních rohů k/j; rovnoměrná
konvergence dává pro všechna dostatečně velká n a n<=m<=2n
P_(n,m)>=_maj T_(j,epsilon). Mezi rohy plyne porovnání z konkávnosti
křivky P; v krajích mají obě křivky stejné hodnoty0 a1.

Srovnávací lemma pro libovolnou posloupnost S poskytne v každém takovém
úseku index m s S_m>=_maj P_(n,m)>=_maj T_(j,epsilon). Monotonicita f,
rozštěpení do společné dimenze a nekonečně mnoho takových m tedy dávají

```
limsup_m f_m(S_m) >= f_j(T_(j,epsilon)).
```

Spojitostí pro epsilon->0 dostaneme dolní mez f_j(L_j) pro každé j.
Označme B=sup_j f_j(L_j), případně+infinity. Pak limsup f(S)>=B.
Pro S=L je zároveň limsup f(L)<=B z definice suprema, takže je rovno B.
To je přesně F ze zadání a současně f_j(L_j)<=F pro všechna j.
Důkaz používá pouze uvedené předpoklady. Výrazy s dělením nejmenší
mezerou mají přirozeně obor pozitivních délek, případně nekonečnou
hodnotu na hranici; nevyžadují f konečné v bodě s nulovým jmenovatelem.

## 7. Přesné konečné kontroly a jejich rozsah

`verify_gap_structure.py` používá racionální argumenty logaritmů,
nikoli zaokrouhlené délky. Pro n=1,...,512 porovnává oba skutečně
seřazené bodové modely W,Z s teoretickými poměry a kontroluje131328
součinů odpovídajících součtům logaritmů. Dále vyčerpává3255 prefixů
na mřížce{0,1/5,...,4/5}, včetně opakovaných bodů:19260 kontrol
opraveného času vzniku a obecné harmonické nerovnosti, plus všechny
odpovídající kontroly největší mezery. Pro65536 bodů testuje
W_j<1/2 pomocí přesné celočíselné nerovnosti (2j+1)^2<2*2^(2h)
a porovnává16 dvojic prefixů s nezávislým počtem lichých čísel v pásmech.
Výstup `results/gap-structure.json`; všechny tři bloky prošly.

První spuštění skončilo okamžitě syntaktickou chybou chybějící závorky
v zápisu výsledku; žádná kontrola tehdy neběžela. Po opravě běh65448
skončil0. Log zachovává i tuto chybu. Konečné kontroly doplňují obecné
důkazy, nepředstírají vyčerpání všech posloupností ani náhradu minimax důkazu.
