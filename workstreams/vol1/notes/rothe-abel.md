# §1.2.6: Rotheho a Abelovy identity a příklady

Značení `C(r,k)` a základní identity (5)–(25) jsou definovány
a dokázány v [binomial-identities.md](binomial-identities.md).
Indexy rovnic odkazují na knihu. Zde dokazujeme zejména (26),(30),
příklady 1–5 a úlohy 22–28,30–31,33–34. Historické atribuce
nejsou automaticky uzavřeny matematickým důkazem.

## Polynomy bez dělení nulou

Pro celé k>=1 definujme

```text
A_k(r,t) = r/k! product_{j=1}^{k−1}(r−tk−j),
A_0(r,t) = 1,   A_k(r,t)=0 pro k<0.                   (R1)
```

Pro r≠tk jde právě o `C(r−tk,k) r/(r−tk)`. Toto vyjádření
proto rozšiřujeme do bodů r=tk polynomem (R1). U k=0 se krátí
vnější poměr r/r; u k>=1 první faktor binomického součinu.
Nikde není potřeba definovat číslo 0/0. Pozdější odstranění
podmínky k>=0 u součtu (26) v září 2025 je v tomto smyslu
neškodné: k<0 přispívá nulovým polynomem.

Značme levou stranu (26) jako
`F_n(r,s,t)=sum_{k=0}^n A_k(r,t) C(s−t(n−k),n−k)`
pro n>=0 a F_n=0 pro n<0. Cílem je

```text
F_n(r,s,t)=C(r+s−tn,n).                               (R2)
```

## Úlohy 22–24: elementární důkaz (R2)

Pro n=0 jsou obě strany 1, pro n<0 jsou obě 0.
Pro n>0 začněme speciální hodnotou s=n−1−r+tn. Pomocí (17)
a (20) je k-tý sčítanec přesně

```text
r/n! (−1)^(n−k) C(n,k)
       product_{j=1}^{n−1}(r−tk−j).                  (R3)
```

Součin je polynom v k stupně nejvýše n−1, takže jeho n-tá
diference je 0 podle (34). Pravá strana (R2) je C(n−1,n)=0.
Výpočet zahrnuje k=0 i r=0 díky polynomiální definici.
Odpověď 22 má postupně opravy faktoru r (2000), celého
vyjádření a dělení r−tk (2013) a znaménka (2023); náš zápis
(R3) nevyužívá žádné dělení, které by zůstalo singularitou.

Pascalovo pravidlo ve druhém faktoru dává rekurenci

```text
F_n(r,s+1,t)=F_n(r,s,t)+F_(n−1)(r,s−t,t).              (R4)
```

Pravá strana (R2) splňuje stejnou rekurenci. Indukcí podle n
máme tedy shodu pro s=n−1−r+tn+j, j=0,1,2,...: počáteční
bod je (R3), postup o 1 je (R4). Pro pevná r,t jsou obě strany
polynomy v s stupně nejvýše n a shodují se v nekonečně mnoha
bodech. Jsou proto totožné. Tím je (26) dokázáno pro všechna
reálná i komplexní r,s,t a všechna celá n.

## Příklad 4: konvoluce polynomů A_k

Prozatím předpokládejme r−tk, s−t(n−k) a r+s−tn nenulové.
Poslední podmínka byla v knize výslovně doplněna v roce 2021.
Elementární rozklad

```text
1/[(r−tk)(s−t(n−k))]
 = [1/(r−tk)+1/(s−t(n−k))]/(r+s−tn)
```

změní součet `sum_k A_k(r,t)A_(n−k)(s,t)` na součet dvou
výrazů (R2), s prefaktory s/(r+s−tn) a r/(r+s−tn).
Výsledek je `(r+s)C(r+s−tn,n)/(r+s−tn)=A_n(r+s,t)`.
Obě původní strany jsou polynomy, proto shoda platí i na
vyloučených nadrovinách. Tím je doloženo (30), včetně n=0.

## Úlohy 25–27: konvergentní generující řady

Generující řada posloupnosti a_k je mocninná řada sum a_k z^k.
Pro pevná r,t mají obě posloupnosti A_k(r,t), C(r−tk,k)
nejvýše exponenciální růst v k. Skutečně každý činitel má
absolutní hodnotu nejvýše Dk, kde D=|r|+|t|+1, a
k!>=(k/e)^k podle již dokázané faktoriálové meze. Proto obě
řady konvergují pro dost malé |z|.

Označme komplexní mocniny x^a poblíž x=1 jako exp(a Log x),
s analytickou větví Log(1)=0. Pro
`z=(x−1)x^t` je derivace podle x v x=1 rovna 1; převod x↔z
je tedy v dost malém okolí invertibilní. Knižní podmínka
„z dost malé“ sama neurčovala větev; od roku 2013 správně
požaduje x dost blízko 1. Pro t=r=1, x=0 má staré zadání
z=0, ale řada hodnotu 1 a x^r hodnotu 0.

Pro každé k>=1 je
`C(r−tj,k)r/(r−tj)` polynom v j stupně nejvýše k−1.
K-tá diference tedy dává nápovědu úlohy 25:

```text
sum_{j=0}^k (−1)^j C(k,j) C(r−tj,k)r/(r−tj) = [k=0].
```

Každý zdánlivý podíl zde interpretujeme polynomem, jak výslovně
doplňuje erratum 2022. Vynásobme w^k a sečtěme přes k>=0.
Záměna součtů je oprávněná pro malé |w|: j<=k, jednotlivé
součiny mají výše uvedenou exponenciální mez a
sum_j C(k,j)=2^k. Použití (20) a binomické věty dává

```text
1 = sum_{j>=0} (−1)^j A_j(r,t)w^j(1+w)^(r−tj−j)
  = (1+w)^r sum_{j>=0} A_j(r,t)[−w/(1+w)^(t+1)]^j.
```

Položením x=1/(1+w), z=−w/(1+w)^(t+1) dostáváme

```text
sum_{k>=0} A_k(r,t)z^k=x^r.                           (R5)
```

To zdůvodňuje i konvergenci a záměny, které knižní důkaz pouze
stručně naznačuje; holomorfnost pravé strany sama o sobě by
neidentifikovala dosud neověřené koeficienty levé strany.

Pro r≠0 platí `C(r−tk,k)=(1−tk/r)A_k(r,t)`. Derivací (R5)
a využitím `dz/dx=x^(t−1)((t+1)x−t)` tedy dostáváme

```text
sum_{k>=0} C(r−tk,k)z^k = x^(r+1)/((t+1)x−t).         (R6)
```

Rovnost pro r=0 plyne spojitostí v r, nebo porovnáním
polynomiálních koeficientů. Jmenovatel má v x=1 hodnotu 1.
Součin dvou řad (R5) dokazuje (30); součin (R6) s (R5)
pro druhý parametr s dokazuje (26), po případné výměně k↔n−k.
To ověřuje i alternativní postupy úlohy 27.

## Příklady 1–3,5 a úloha 30

Příklad 1. Pro celé r>=0 je podle (7),(22)
`sum_k k C(r,k)C(s,k)=s C(r+s−1,r−1)`.
Také při r=0 jsou obě strany 0. Dodatek m=0 při použití
(22) v erratech 2004 upřesňuje správné dosazení.

Příklad 2. Pro celé n>=0 převod (20),(7) dává

```text
sum_{k>=0} C(n+k,2k)C(2k,k)(−1)^k/(k+1)
 = 1/(n+1) sum_{k>=0} C(n+k,k)C(n+1,k+1)(−1)^k.
```

Negace horního indexu prvního faktoru a (22) dají
`C(0,n)/(n+1)=[n=0]`, což je (28).
Druhý knižní postup, posun j=k+1 a (23), dá
`C(n−1,n)/(n+1)` se stejným výsledkem. Chybějící prefaktor
1/(n+1) na jednom mezikroku byl opraven v říjnu 1997.
Omezení k>=0 v počátečním výrazu je známá oprava z 2021;
k=−1 jinak obsahuje samostatné dělení nulou.

Příklad 3. Pro kladná celá m,n použití (25) s parametry
`(r,m,s,n)=(n−1,m−1,k,2k)` převádí první faktor na

```text
C(n+k,m+2k)=sum_{j=0}^{n−1} C(n−1−j,m−1)C(k+j,2k).
```

Podmínka 0<=k<=2k platí pro celé k>=0. Násobení
C(2k,k)(−1)^k/(k+1), záměna konečných součtů a (28)+ponechají jen j=0. Výsledek je C(n−1,m−1).
Toto je opravený důkaz z 2016/2021. I starý postup lze
odůvodnit: po výměně j↔n−1−j se dostane ke stejné rovnici;
vně n zůstávají nulové členy s nezáporným horním indexem.

Úloha 30 má od roku 2023 kratší řešení platné pro všechna
celá n>=0 a všechna celá m. Označme N=n−m. Symetrie (6)
a negace (17) změní původní součet na

```text
sum_{k>=0} C(n+k,N−k) C(−k−1,k)/(k+1).
```

Jde o (R2) s (r,s,t,n')=(−1,2n−m,1,N), takže výsledek je
`C(n−1,n−m)`. Při N<0 jsou všechny členy 0. Pro n>0 je
výsledek roven C(n−1,m−1), ale pro n=0 se musí zachovat
nový tvar. Tím je prověřena i poslední poznámka opravené odpovědi.

Příklad 5. Trojúhelníkový systém
`n!=sum_{k=0}^n C(n,k)k!a_k` má jediné řešení, protože
koeficient a_n je n!≠0. Binomická inverze (33), s konečnou
výměnou součtů, dává
`m!a_m=sum_{n=0}^m (−1)^(m−n)C(m,n)n!`.
Po dělení m! a změně n↔m−n dostáváme
`a_m=sum_{n=0}^m (−1)^n/n!`. To souhlasí s předchozí sekcí;
její kontrolní program se znovu nespouští.

## Úlohy 28,31,33–34 a Abelova formule (16)

28. Nechť `G_n(r,s,t)=sum_k C(r+tk,k)C(s−tk,n−k)`.
Rozdělení 1=r/(r+tk)+tk/(r+tk), následované (R2) a posunem
k→k+1 ve druhé části, dává

```text
G_n(r,s,t)=C(r+s,n)+t G_(n−1)(r+t−1,s−t,t).
```

Opakováním vyjde `sum_{j=0}^n t^j C(r+s−j,n−j)`, jak žádá
zadání. Zdánlivé singularity se odstraňují polynomiálně; n=0 dává 1.
Původní opačná znaménka posunů r−t−1,s+t v odpovědi jsou
známé erratum z 24. května 2000.

31. Položme a=m−r+s, b=n+r−s, takže a+b=m+n.
Rozvineme C(r+k,m+n) podle (21) v indexu j; (20) a další
konvoluce pak dávají

```text
sum_k C(a,k)C(b,n−k)C(r+k,m+n)
 = sum_j C(a,j)C(r,m+n−j)C(m+n−j,n−j)
 = C(r,m) sum_j C(a,j)C(r−m,n−j)
 = C(r,m)C(s,n).
```

Nenulový rozsah je 0<=j<=k<=n, takže všechny součty jsou konečné.
Symetrie v prostředním koeficientu je legitimní, protože
m+n−j>=m>=0. Historický odkaz na Pfaffa zůstává oddělen.

Errata z 11. října 2001 rozšiřují m,n na všechna celá čísla.
Pro n<0 jsou oba činitelé C(a,k),C(b,n−k) současně nenulové
nikde, a pravá strana je také 0. Pro n>=0 a m+n<0 je nulový
třetí činitel. Zbývá m<0<=m+n=M. Po rozvinutí posledního
koeficientu stačí sčítat přes 0<=j<=M; vnitřní konvoluce
dá C(M−j,n−j)=0, protože n>M. Celý součet i pravá strana
jsou opět 0. Tím je ověřeno i rozšířené zadání.

33. Vynásobení (21) číslem n! dává binomickou formuli pro
padající mocniny; dosazení −x,−y a vytažení (−1)^n dává
rostoucí mocniny. Všechny parametry x,y jsou libovolné,
n nezáporné celé. Náhrada atribuce Capelli→Vandermonde v 2005
není novým matematickým nálezem.

34. Do (R2) dosadíme r=x, s=y−1+nz, t=z−1. Po vynásobení
n! a převrácení pořadí činitelů dostáváme přesně

```text
(x+y)^(rising n)
 = sum_{k=0}^n C(n,k) x (x−kz+1)^(rising(k−1))
                         (y+kz)^(rising(n−k)).
```

Člen k=0 znamená 1 krát (y)^(rising n), po odstranění
společného faktoru x, nikoli nevyhodnocené dělení nulou.
Dosazení −x,−y,−z dává variantu s padajícími mocninami
v odpovědi, včetně posunu x−kz−1.

(16) lze dokázat také přímo z (R2) porovnáním nejvyšších
mocnin pomocné proměnné h po dosazení
`r=h x, s=h(y+nz), t=h z`. Koeficient h^n po vynásobení n!
je na pravé straně (x+y)^n a na levé
`sum_k C(n,k)x(x−kz)^(k−1)(y+kz)^(n−k)`.
To je Abelova formule; k=0 se opět krátí. Knižní podmínka
x≠0 je dostačující. Alternativní důkazy úloh 50–52 jsou
v `binomial-exercises.md`; další formule odpovědí jsou
dokázány v `abel-extensions.md`.
