# V2-C0132: konvergence v pravděpodobnosti není téměř jistá asymptotika

Stav: **confirmed**, matematická chyba v dodatku odpovědi
§4.5.3-24, strana 652. Samotná odpověď „nekonečno“ na
střední hodnotu podílu je správná. Chybný je následující
výrok o součtu prvních n podílů a jeho atribuce Khinčinovi.

Nechť X je rovnoměrné reálné číslo v (0,1) a
X=[0;A_1,A_2,...] jeho pravidelný řetězový zlomek. Racionální
čísla mají pravděpodobnost nula a můžeme je vynechat.
Položme S_n=A_1+...+A_n. Kniha tvrdí S_n~n lg n pro
„for almost all X“, kde lg je logaritmus o základu 2.
To by znamenalo, že S_n(X)/(n lg n)→1 pro všechna X
mimo jednu množinu délky nula. **Ve skutečnosti má tento
poměr pro téměř všechna X nekonečnou horní limitu.**

Správný Khinčinův výsledek je konvergence v pravděpodobnosti:
pro každé epsilon>0 platí

```text
Pr(|S_n/(n lg n)-1| > epsilon) -> 0.                    (1)
```

Výjimečná množina v (1) smí být jiná pro každé n. Její
zmenšující se velikost nevylučuje, že téměř každé X do
výjimečných množin vstoupí nekonečněkrát. Rozdíl tedy není
jen terminologický nebo změna základu logaritmu.

## Nezávislý důkaz chyby a hlavní odpovědi

Válec délky n-1 je interval všech čísel se stejným prefixem
A_1,...,A_(n-1). Označme p/q a p'/q' poslední a předposlední
konvergent tohoto prefixu. Pro prázdný prefix používáme
p/q=0/1 a p'/q'=1/0. Zbývající zlomek t po odstranění
prefixu leží v (0,1) a platí

```text
X=(p+p't)/(q+q't),   |p'q-pq'|=1,
r=q'/q,             0<=r<=1.
```

Absolutní hodnota derivace zobrazení t→X je
1/(q+q't)². Po podmínění na tento válec má proto t hustotu

```text
w_r(t)=(1+r)/(1+rt)²,    0<t<1.                        (2)
```

Normalizace plyne z integral(0..1)(1+rt)^(-2)dt=1/(1+r),
včetně r=0. Následující podíl je A_n=floor(1/t). Pro celé
m>=1 tudíž přesně dostáváme

```text
Pr(A_n>=m | A_1,...,A_(n-1))
  = integral(0..1/m) w_r(t)dt
  = (1+r)/(m+r) >= 1/m.                               (3)
```

Hranice intervalů mají nulovou míru. Zprůměrováním (3)
a sečtením ocasových pravděpodobností dostaneme pro každé
pevné n>=1

```text
E[A_n] = sum(m>=1) Pr(A_n>=m) >= sum(m>=1)1/m = infinity.
```

To je úplný důkaz správné hlavní odpovědi 24 pro rovnoměrný
počáteční X; nepotřebuje přechod k limitnímu rozdělení.

Nyní zvolme libovolné pevné celé c>=1 a pro n>=2 nastavme
m_n=ceil(c n lg n). Podmíněná pravděpodobnost, že A_n<m_n,
je podle (3) nejvýše 1-1/m_n, ať byl dosavadní prefix jakýkoli.
Opakovaným podmíněním tedy pro každé N>=2 dostáváme

```text
Pr(A_n<m_n pro všechna N<=n<=M)
  <= product(n=N..M)(1-1/m_n)
  <= exp(-sum(n=N..M)1/m_n) -> 0.                      (4)
```

Poslední limitu dává divergence sum 1/(n log n); zaokrouhlení
m_n na celé číslo ji nemění. Průnik událostí vlevo přes
všechna M má proto pravděpodobnost nula. Sjednocení přes
spočetně mnoho N stále má pravděpodobnost nula. Skoro jistě
tedy nastane A_n>=c n lg n nekonečněkrát. Protože S_n>=A_n,
platí skoro jistě limsup S_n/(n lg n)>=c. Konečně průnik
těchto plnoměrných množin přes c=1,2,... dává

```text
limsup(n→infinity) S_n/(n lg n) = infinity
pro téměř všechna X.                                  (5)
```

Důkaz nepředpokládá nezávislost podílů ani nepoužívá
statistický experiment jako náhradu tvrzení o téměř všech X.

## Původní pramen a errata

Původní sazba knihy na 652 byla vizuálně přečtena. Citovaný
[Khinčinův článek z roku 1935](https://www.numdam.org/item/CM_1935__1__361_0/)
byl získán v originálu; **strany 377–381** byly vizuálně
přečteny. Na 377 je formulována přesně (1), označena jako
konvergence v míře. Tentýž odstavec výslovně říká, že ji
nelze zesílit na téměř jistou limitu, protože již
A_n/(n log n) má skoro jistě nekonečnou horní limitu.
Následující strany dokazují slabší větu pomocí ořezání
podílů, odhadů momentů a odhadu výjimečné množiny; samotná
kritická formulace a upozornění jsou na 377 vedle sebe.
Starší pomocná lemmata z dalších částí článku zde nejsou
vydávána za kompletně znovu ověřená. Důkaz (2)–(5) výše
je na nich nezávislý.

Další primární kontrolou je [Diamond–Vaaler 1986](https://msp.org/pjm/1986/122-1/pjm-v122-n1-p06-p.pdf),
strana 74, vizuálně přečtená. Jejich lemma 1 dává obecné
kritérium velkých podílů a text výslovně odlišuje konvergenci
v míře od téměř jisté. Navazující silnější ořezané věty
nejsou k tomuto protipříkladu potřebné.

Všechny čtyři vrstvy errat `all2-prepre`, `all2-pre`, `all2`,
`err2` byly 2026-11-03 prohledány podle 652, Khinchin,
Khintchine, sum, almost all, measure, probability a věcného
obsahu. Původní relevantní listy byly přečteny při inventáři.
Oprava odpovědi 29 na stejné straně tento odstavec nemění;
oprava této chyby nalezena nebyla. Obrazy, PDF a jejich
kontrolní součty jsou v `sources/euclid-metric-sums.json`.

Novější fyzický dotisk a prvenství nejsou ověřeny. Anglický
návrh opravy zůstává neodeslaný. Pro audit úlohy 24 jsou
hlavní odpověď i chyba v doprovodném tvrzení uzavřeny.

Další primární doklad nalezen při úloze35: Yao–Knuth,
STAN-CS-75-510 (1975), číslovaná strana10, opakuje stejné
nesprávné tvrzení o téměř všech reálných číslech. Celá
zpráva byla vizuálně přečtena; doklad je v
images/yao-knuth-1975-body10.png a metadata v
sources/euclid-heilbronn.json. Nejde o nový samostatný nález
a důkaz odečítacího algoritmu tento odstavec nepotřebuje.
