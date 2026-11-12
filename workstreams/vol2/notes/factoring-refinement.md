# §4.5.4-36/37: přesnější čas a symetrie periody

Zadání415, odpověď665 a související397–400 byly přečteny v původní
sazbě. Úlohy36/37 jsou auditovány v níže vymezeném rozsahu.
[C0174](C0174-factorization-rounded-parameter.md) je potvrzený problém
s podlahou v časovém odhadu. [C0175](C0175-contfrac-early-stop.md) zůstává
kandidátem: prosté předčasné zastavení může ztratit faktorizaci, ale
kniha tomuto volitelnému doporučení nedává výslovnou záruku úplnosti.
Samotná palindromická věta je správná.

## 1. Co přesně se minimalizuje

Číslo N je vstup faktorizace, m velikost báze prvních m prvočísel
a p_m její poslední prvočíslo. Zaveďme přirozené logaritmy

```
L=ln N, l=ln L, X=2sqrt(N), H=ln X, h=ln m,
rho=H/ln p_m, r=floor(rho), delta=H-r ln p_m.
```

Výraz(22) na399 je, až na pevnou volbu základu logaritmu,

```
B(N,m)=X*m²*L*r!/m^r.                                  (1)
```

Jde o horní odhad uvnitř knižního heuristického modelu, který považuje
hodnoty V za náhodné a potřebný počet relací za úměrný m. Následující
minimalizace(1) je přesná matematika tohoto modelu; nezaručuje skutečný
čas algoritmu E.

Tištěný rozvoj m-tého prvočísla je správný. Při u=ln m a v=ln u je

```
p_m=m*(u+v-1+(v-2)/u+O(v²/u²)).                       (2)
```

Koeficienty se získají inverzí rozvoje logaritmického integrálu
`li(x)=x/ln x*(1+1/ln x+2/(ln x)²+...)` v rovnici π(p_m)=m.
Vložení pravé strany(2) dává m s chybou O(m v²/u³), jejíž inverzní
chyba je O(m v²/u²). Analytický prvočíselný odhad je zde externí
standardní vstup z(4) hlavního textu, nikoli nový zdejší důkaz věty
o prvočíslech. Dále stačí slabší důsledek

```
ln p_m=h+ln h+O(ln h/h).                               (3)
```

## 2. Kde se ztrácí podlaha

Položme `h=(c/2)sqrt(L*l)`, přičemž c zůstává mezi dvěma pevnými
kladnými konstantami. Rozvoj(3) a geometrická řada dávají

```
rho=c^(-1)sqrt(L/l)-c^(-2)
    -c^(-2)*(ln l+2ln(c/2))/l+O(sqrt(l/L)).             (4)
```

To je vytištěný vzorec665, avšak jeho levá strana má být **rho, ne r**.
Pro r je nutné zachovat podlahu nebo přidat člen −{rho}, kde
`{rho}=rho-floor(rho)` je zlomková část. Zvětšení zbytku na O(1)
opraví tuto rovnost, ale nezachová následující přesnost času.

Nechme m růst přes celá čísla, `h=ln m`, `k=floor(h/ln h)` a

```
N=floor(p_m^(2k+1)/4), c=2h/sqrt((ln N)(ln ln N)).       (5)
```

Pak c→1, `rho=k+1/2-o(1)` a r=k. Pravá strana(4) se tedy od r
liší o `1/2+o(1)`, zatímco zobrazený zbytek jde k nule. To je
asymptotický protipříklad splňující i kompaktní rozsah c.

Při nahrazení r reálným rho a faktoriálu gama funkcí definujme
spojitou verzi `B_c=X*m²*L*Gamma(rho+1)/m^rho`. Gama funkce
rozšiřuje faktoriál rovností Gamma(j+1)=j!. Pro t={rho} platí

```
ln B-ln B_c=t*(h-ln rho)+O(1/rho).                     (6)
```

Rodina(5) má t→1/2. Chyba logaritmu času je tak řádu sqrt(L*l),
nikoli O(l). Obecná specializace(22) na665 proto neplatí pro
libovolné takto zvolené m. Konečný optimalizovaný odhad lze opravit.

## 3. Celočíselná optimalizace s chybou exp(O(log log N))

Zvolme celé r nejbližší číslu

```
r_0=sqrt(2H/(ln H-1)), u=H/r.                          (7)
```

Pro dost velké N je r>=3. Z(3) plyne, že pro dost velkou pevnou
konstantu K můžeme vzít

```
m=floor(exp(u-ln u-K*ln u/u)).                         (8)
```

Pak `ln p_m<=u` a `u-ln p_m=O(ln u/u)`. Proto
`delta=H-r ln p_m=O(r ln u/u)=O(1)`; protože ln p_m→∞,
skutečná podlaha v(1) je právě zvolené r. Zaokrouhlení m mění
jeho logaritmus pouze o O(1/m).

Doložme i optimalitu. Stirlingův vzorec znamená
`ln(r!)=r ln r-r+O(ln r)`. Pro `h=Theta(sqrt(H ln H))`
a `r=Theta(sqrt(H/ln H))` dává(1),(3)

```
ln B = delta+2h+r ln(rh)-r+O(ln H)
     = 2H/r+(ln H-1)r+delta*(1-2/r)+O(ln H).           (9)
```

Používáme `rh=H-delta-r ln h+O(1)` a
`0<=delta<ln p_m=O(h)`, tedy `r ln(rh)=r ln H+O(1)`.
Dále `h=H/r-ln h-delta/r+O(ln h/h)`; zbývající logaritmické
členy se vejdou do O(ln H).

Uvedený rozsah neztrácí globální minimum. Konstrukce(7),(8)
dává `ln B=O(sqrt(H ln H))`. Pro libovolného konkurenta jsou
`H-rh>=0` a `ln(r!)>=0`, takže z(1) plyne
`h=O(sqrt(H ln H))` a `r=O(sqrt(H/ln H))`.
Navíc `H-rh=O(sqrt(H ln H))` vynutí opačné dolní meze obou
parametrů. Konkurenti s větším logaritmem času minimum nezlepší.

Protože delta>=0 a r>=3, poslední explicitní člen(9) je nezáporný.
Funkce `g(r)=2H/r+(ln H-1)r` má minimum v(7) a hodnotu
`2sqrt(2H(ln H-1))`. Zaokrouhlení r o nejvýše1/2 mění g
o O((ln H)^(3/2)/sqrt(H))=o(1). Volba(8) má delta=O(1).
Horní i dolní odhad minima tedy dávají

```
min_m ln B(N,m)
 =2sqrt(2H(ln H-1))+O(ln H)
 =2sqrt(L*l)*sqrt(1-(1+ln2)/l)+O(l).                  (10)
```

To je zamýšlený konečný výsledek665. Jeho dosažení potřebuje
doladění(8), nikoli prosté dosazení tištěného c. Hlavní člen h
je `(1/2)sqrt(L*(l-1-ln2))`, s korekcemi O(l) a se zvlášť
kontrolovanou podlahou. Pro N=10^50 je hlavní exponent
`epsilon=0.32568220282579...`, tedy zaokrouhleně .33.

## 4. Milion podílů a hustota chyby aproximace

Pro `D=10^18+314159` je prvních milion **necelých** podílů
`a_1,...,a_1000000` spočteno dvěma celočíselnými rekurzemi:
přímou normovou rekurzí a bezdělicí aktualizací E2. Souhlasí každý
podíl i oba stavové parametry. Počty podílů1,2,3,4 jsou přesně
`415236,169719,93180,58606`, jak uvádí665. Zahrnutí celé části
a_0 by místo poslední jedničky snížilo první počet na415235;
standardní konvence, která celou část odděluje, text vysvětluje.

Jsou-li p_n/q_n konvergenty sqrt(D), definujme
`e_n=p_n-sqrt(D)q_n` a `theta_n=q_n|e_n|`.
Normová identita a `e_n=O(1/q_n)` dávají

```
V_(n+1)=|p_n²-Dq_n²|=2sqrt(D)*theta_n+O(q_n^(-2)).     (11)
```

Knižní pravděpodobnostní poznámka používá místo tohoto pevného D
náhodné reálné x. Primární článek Bosma–Jager–Wiedijk1983 byl získán
z [autorského webu](https://www.math.ru.nl/~bosma/pubs/IndagMath1983.pdf).
Vizuálně přečteny281–282,284–287, zvláště Theorem1 a celý jeho
důkaz284–286. Článek dokazuje limitní rozdělení pro skoro všechna x,
nikoli pro každé sqrt(D). Další zobecnění článku zde nejsou auditována.

Výpočet hustoty lze zkontrolovat přímo. Přirozené rozšíření Gaussovy
mapy má na čtverci0<x,y<1 invariantní hustotu
`1/(ln2*(1+xy)²)`. Nová proměnná t=x/(1+xy) má společně s y
konstantní hustotu1/ln2 v oblasti `0<t<1/(1+y)`.
Integrace přes y dává

```
f(t)=min(1,1/t-1)/ln2, 0<t<1.                          (12)
```

Je tedy konstantní na(0,1/2), jako v knize. Ergodicita znamená,
že dlouhodobé četnosti podél skoro každé trajektorie souhlasí
s invariantní mírou. Je zde externím vstupem(2.3) článku;
původní Nakadův důkaz nepřezkoumáváme. Převod obecného počátečního
y na y=0 pomocí kontrakce řetězových zlomků byl v článku přečten.
Použití(12) na pevnou kvadratickou iracionalitu zůstává heuristické,
jak naznačuje i formulace665.

## 5. Obecný důkaz palindromu

Pišme s=sqrt(D), R=floor(s), D kladné nečtvercové celé.
Kvadratické číslo x>1 nazveme redukované, když jeho sdružené
číslo x' vzniklé náhradou s za−s leží v(−1,0).
Mapa `T(x)=1/(x-floor(x))` zachovává redukovaná čísla daného D.
Jejich celočíselné stavy jsou konečné a mají jediného předchůdce;
úplný důkaz je v [euclid-quadratic.md](euclid-quadratic.md),12(b).

Číslo x_0=s+R je redukované, takže jeho rozvoj je periodický od
začátku. Délku nejkratší periody označme ell. Pak `a_0=2R`
a podíly x_1=T(x_0),...,x_(ell-1) jsou a_1,...,a_(ell-1).
Zaveďme involuci `I(x)=-1/x'`. Přímý výpočet dává
`I T I=T^(-1)` a `floor(I T x)=floor(x)`; v poslední identitě
je `I T x=floor(x)-x'` a −x'∈(0,1). Navíc
`I(x_0)=1/(s-R)=T(x_0)`. Proto

```
I T^(j+1)x_0=T^(-j)x_0,
a_j=a_(ell-j), 1<=j<ell.                              (13)
```

Rozvoj s má celou část R a opakující se blok
`a_1,...,a_(ell-1),2R`, jehož část před2R je palindrom.
Případ ell=1 má prázdný palindrom a je zahrnut.

Pro symetrii stavů napišme `x_j=(s+P_j)/Q_j`, `P_0=R,Q_0=1`.
Rekurze je `P_(j+1)=a_j Q_j-P_j`,
`Q_(j+1)=(D-P_(j+1)²)/Q_j`. Involuce dává

```
P_j=P_(1-j), Q_j=Q_(-j),                              (14)
```

s indexy modulo ell. To vysvětluje středové rovnosti U=U'
nebo V=V' v E. Samo o sobě to neurčuje P modulo N ani znaménko
relace, a neříká, že závěrečnou relaci V=1 lze zahodit.
Pro N=323,k=1 původní E po předčasném zastavení nedá žádný výstup,
zatímco celý průchod dá `18²=1 mod323` a faktor17. S opraveným E1
z2001 funguje podobný příklad N=323,k=2, viz C0175.

## 6. Přesné kontroly a errata

`verify_factoring_refinement.py` má tři uložené úspěšné bloky:

- 9900 nečtvercových D od2 do10000;280934 stavů, palindromy,
  obě symetrie(14) a nezávislá celočíselná matice celé periody.
  Oba příklady předčasného zastavení ověřeny plnými konvergenty.
- Milion podílů ve dvou modelech, včetně všech stavů a kontrolního
  SHA-256 celého proudu. Nejde pouze o porovnání čtyř četností.
- Čtyři přesné příklady podlahy a šest globálních minim(1) pro
  N=10^6,10^12,...,10^36. Všechny relevantní m porovnány racionálně;
  po r<=2 už nové minimum nevznikne. Sedmdesátimístné logaritmy
  slouží pouze jako ilustrace asymptotického důkazu.

Proces12356 skončil0 za6.947s; jednotlivé časy jsou v JSON/logu.
Primární PDF, odvozený text a přečtené stránky jsou uloženy.
Čtyři vrstvy errat a `err2.textxt` prohledány pod399/415/665,
36/37/38, jmény autorů, palindromem a ukončením.
Oprava665 z18.2.2004 patří k předchozí úloze35; změna E1 z2.7.2001
je zahrnuta ve druhém příkladu. Odpovídající oprava36/37 nenalezena.
Pozdější fyzický dotisk a prvenství neověřeny; nic neodesláno.
