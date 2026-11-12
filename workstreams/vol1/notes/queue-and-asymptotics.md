# §2.2.1: základní operace, dvěma zásobníky a asymptotiky

Kontroly V1-X0014 až V1-X0016, 1. listopadu 2026. Hlavní text a obrázky
na s. 238–243, odpovědi na s. 536, 538–540. Skeny všech těchto stran
byly zobrazeny. **Nová chyba nebyla potvrzena.** Známé opravy se vedou
odděleně jako V1-X0017 a V1-X0018.

## 1. Definice a cvičení 1, 2, 6

Lineární seznam je konečná posloupnost uzlů, včetně prázdné posloupnosti.
Sken s. 238 správně píše n>=0; navigační přepis chybně ztrácí rovnost.
Zásobník vkládá i odebírá na stejném konci, fronta na opačných koncích,
oboustranná fronta na libovolném konci. Nejnovější prvek zásobníku a
nejstarší prvek fronty tedy skutečně odcházejí jako první. U jednoho
prvku oba konce splývají; prázdnost je výslovně vyloučena u odběru.

Železniční schémata na s. 240 umožňují právě popsané operace; uzavření
horní, respektive dolní větve omezuje právě vstupy, respektive výstupy.
Pojmenování konců a šipky na obrázku 3, s. 241, jsou konzistentní.
Definice vložení, odebrání a top(A) na s. 242 odpovídají textu. Drobné
terminologické doplnění „bottom“ na s. 242 je v `all1-pre` z 28. dubna 2012.
Opravy „cards“ na „cars“ a označení kroků cvičení 2–3 jsou v `all1-prepre`
z 21. července 1997 a 5. ledna 1998; nemění matematický obsah.

**Cvičení 1.** Výstupně omezenou oboustrannou frontu lze použít jako
zásobník při vkládání na výstupním konci a jako frontu při vkládání na
opačném konci. Platí i pro prázdnou strukturu a jediný prvek.

**Cvičení 2.** S označuje vložení na zásobník, X odebrání. Historie
SSSXXSSXSXXX vydává postupně 3,2,5,6,4,1. Pro požadované 154623 musí
být 3 vložena před prvním výstupem 5 a nemůže být odebrána před pozdějším
výstupem 2. Zůstává tedy nad 2 a blokuje ji. To je přesně překážka 312
v trojici 5,2,3. Uvedené odpovědi souhlasí s obecným důkazem
v `stack-permutations.md`.

**Cvičení 6.** Fronta zachovává vzájemné pořadí všech dosud přítomných
prvků a připojuje nové až za ně. Jediným úplným výstupem je 1,...,n,
včetně prázdného výstupu pro n=0.

Tím je prověřen matematický obsah hlavního textu §2.2.1 a cvičení 1,2,6.
Historický původ všech synonym a příklady z jiných sekcí nejsou samostatně
ověřeny tímto argumentem; příslušné odkazované algoritmy mají vlastní
položky v mapě svazku. Ze s. 242–243 je potvrzen soupis cvičení 1–14.

## 2. Fronta pomocí dvou zásobníků (cvičení 14)

Nechť R a S jsou zásobníky. Abstraktní fronta je posloupnost R čtená
od vrcholu ke dnu, za níž následuje S čtený ode dna k vrcholu. To je
invariant: rovnost platná před i po každé dokončené operaci.

Opravené instrukce z 7. července 2021 v `all1-pre`, s. 16:

1. Nový prvek vložit na vrchol S.
2. Při odběru a neprázdném R odebrat vrchol R.
3. Při odběru a prázdném R přemístit postupně všechny prvky S na R
   a pak odebrat vrchol R. Jsou-li oba prázdné, odběr není definován.

Vklad připojí prvek na konec abstraktní fronty. Odběr z R odstraní její
začátek. Přemístění obrací pořadí S, takže nové R čtené od vrcholu je
právě původní S čtený ode dna; invariant se zachová. To dokazuje správnost
indukcí podle operací, bez předpokladu různých hodnot prvků.

Každý konkrétní vložený prvek prochází nejvýše těmito čtyřmi akcemi:
vklad do S, odběr ze S, vklad do R, odběr z R. Z R se zpět nevrací.
Celkový počet zásobníkových akcí po i vkladech je tedy nejvýše 4i.
Jedna operace může stát lineárně mnoho akcí; konstantní je průměrná
cena na operaci přes libovolnou konečnou historii, ne nejhorší cena
jediného odběru. Alternativně potenciál 2|S| dává amortizovanou cenu
3 za vklad a 1 za odběr, pokud každé push/pop stojí jednotku.

Volitelně lze při obou prázdných zásobnících vkládat přímo do R.
Invariant i horní mez zůstávají platné. Podmínka musí být prázdnost obou:
samotné prázdné R se může v odložené variantě vyskytovat i s neprázdným S.
Staré znění kombinuje čas přemístění a výjimku pro vklad jen stručně;
evidujeme zveřejněné vyjasnění, nikoli nový protipříklad proti každé
rozumné interpretaci starého textu.

`check_queue_asymptotics.py` ověřil invariant, výstup a počet akcí na prvek
na všech 23 713 přípustných prefixech s nejvýše 9 vklady, pro každou
z obou variant zvlášť. Úplných historií velikosti 9 bylo 4862. Porovnává
se s přímou posloupností fronty; podklady jsou v `results/queue-asymptotics.json`.

## 3. Hlavní asymptotické vzorce (cvičení 12)

Označme a_n počet zásobníkových výstupů a b_n počet výstupů jedné
omezené oboustranné fronty. Již ověřené přesné vzorce jsou

```text
a_n = binom(2n,n)/(n+1),
sum b_n z^n = (3-z-sqrt(1-6z+z^2))/2.
```

Zápis O(g(n)) znamená chybu omezenou konstantním násobkem |g(n)| pro
všechna dostatečně velká n. Ze Stirlingova vzorce pro faktoriál přímo
plyne a_n=4^n/(sqrt(pi) n^(3/2)) (1+O(1/n)), jak uvádí kniha.

Pro druhý vzorec lze obejít sporné přeskupování nekonečných řad.
Položme u_n=[w^n]sqrt(1-w), kde [w^n] znamená koeficient u w^n.
Pro n>=1 platí přesně

```text
u_n = -binom(2n,n)/(4^n(2n-1))
    = -1/(2 sqrt(pi) n^(3/2)) (1+3/(8n)+O(1/n^2)).
```

Pro pevné |alpha|<1 má součin sqrt(1-w)sqrt(1-alpha w) koeficient
q_n=sum_(k=0)^n u_(n-k) u_k alpha^k. Rozdělme součet při k=n/2.
Horní část je exponenciálně malá, protože u_k jsou omezené a |alpha|<1.
V dolní části lze uvedený Stirlingův odhad použít rovnoměrně a rozvinout
(1-k/n)^(-3/2). Součty |u_k alpha^k| a k|u_k alpha^k| jsou konečné.
Proto

```text
q_n = -sqrt(1-alpha)/(2 sqrt(pi) n^(3/2)) + O(n^(-5/2)).
```

Položme lambda=3+2sqrt(2), rho=1/lambda a alpha=rho^2. Pak
1-6z+z^2=(1-lambda z)(1-rho z). Pro n>=2 je b_n=-lambda^n q_n/2.
Úpravou sqrt(1-rho^2)/4=(sqrt(2)-1)/2^(3/4) dostáváme

```text
b_n = (sqrt(2)-1) (3+2sqrt(2))^n
      / (2^(3/4) sqrt(pi) n^(3/2)) (1+O(1/n))
    = (sqrt(2)+1)^(2n-1)
      / (2^(3/4) sqrt(pi) n^(3/2)) (1+O(1/n)).
```

Obě knižní verze hlavního členu jsou správné. Uložené desetinné poměry
pro n=20,100,500,1000 pouze ilustrují konvergenci; nejsou důkazem meze.

## 4. Známá oprava mezivýpočtu a koeficientů

V1-X0017: `all1-prepre`, s. 40, 17. listopadu 1999, opravuje jednak
podmínku pro rozvoj podle alpha, jednak znaménka v gama faktoru a
v obecných koeficientech c_j asymptotické řady q_n.

Gama funkce Gamma rozšiřuje faktoriál: Gamma(x+1)=x Gamma(x),
Gamma(1/2)=sqrt(pi). Klesající součin (x)_[r] znamená
x(x-1)...(x-r+1), s hodnotou 1 pro r=0. Správná přesná identita je

```text
(-1)^n binom(k+1/2,n)
 = Gamma(n-k-1/2)/(Gamma(n+1) Gamma(-k-1/2)),
1/Gamma(-k-1/2) = (-1/2)_[k+1]/sqrt(pi).
```

První dotisk místo druhého čitatele používá -(k+1/2)_[k+1]. Pro k=1,
n=2 tak dává -3/8, zatímco koeficient [w^2](1-w)^(3/2) je +3/8.
Jde o nejjednodušší zde použitý přesný doklad; 2080 dalších dvojic
0<=k<n<=64 souhlasí s opravenou identitou.

Pro úplnou řadu stačí u konvoluce v oddílu 3 vzít libovolný pevný počet
členů Stirlingova a Taylorova rozvoje; součty všech pevných mocnin k
vážených |alpha|^k konvergují. Tím se oprávní chyba O(n^(-m-5/2))
po členech c_0,...,c_m pro každé pevné m. Označíme-li d_(k,r) koeficient
u n^(-r) v rozvoji Gamma(n-k-1/2)/Gamma(n) po vyjmutí
n^(-k-1/2), pak opravený obecný koeficient je

```text
c_j = sqrt((1-alpha)/pi)
      sum_(k=0)^j binom(1/2,k) (-1/2)_[k+1]
                    d_(k,j-k) (alpha/(1-alpha))^k.
```

To je přímo opravená knižní formule: podle §1.2.11.1-(16) je
d_(k,j-k) zobecněné Stirlingovo číslo prvního druhu s indexy
(-k-1/2,-j-1/2); dualita indexů ze §1.2.6-(58) jej přepisuje na
číslo druhého druhu s indexy (j+1/2,k+1/2), tedy knižní složené závorky.
Obecná definice těchto čísel se prověří ve vlastní sekci; zde se kontroluje
její použití a všechny posuny indexů. Nezávisle první dva členy jsou

```text
c_0 = -sqrt(1-alpha)/(2 sqrt(pi)),
c_1 = -3(1-3alpha)/(16 sqrt(pi) sqrt(1-alpha)).
```

Knižní nekonečný rozvoj kolem w=1 lze převést na koeficienty u w=0
přímo pro dostatečně malé |alpha|. Samotné |alpha|<1 pro tento konkrétní
přesun nestačí: například alpha=3/4 dává beta=alpha/(1-alpha)=3
a binomický rozvoj v beta(1-w) nekonverguje v okolí w=0.
Zde použitý konvoluční důkaz funguje pro každé pevné |alpha|<1.
Stejnou identifikaci všech c_j lze odůvodnit bez nekonečné záměny:
funkci sqrt(1-alpha w) nahradíme konečným Taylorovým polynomem kolem
w=1. Zbytek má tvar (1-w)^(m+1) v(w), kde v je analytická v kruhu
o poloměru větším než 1. Po vynásobení sqrt(1-w) má jeho koeficient
řád O(n^(-m-5/2)); plyne to stejným rozdělením konvoluce jako v oddílu 3,
tentokrát pro koeficienty (1-w)^(m+3/2) a exponenciálně klesající
koeficienty v. Konečný součet dává přesně výše uvedený vzorec pro c_j.

Relevantní stránky i témata byly prohledány ve všech pěti uložených
verzích errat. Kromě uvedených historických oprav a drobných změn
v oddílu 1 se k tomuto rozsahu nenašla další oprava. Úplná kontrola
výzkumného cvičení 13 je vedena samostatně.
