# §1.2.6: dodatky v odpovědích 51–52

Audit 1. listopadu 2026; zobrazeny s. 488–489. Základní
Abelova identita a původní zadání 50–52 jsou dokázány
v `rothe-abel.md` a `binomial-exercises.md`. Zde jsou
samostatně prověřeny další matematické výroky odpovědí.

## Vážené stromy a Hurwitzův polynom

Strom je souvislý graf bez cyklů. V zakořeněném stromu
orientujeme každou hranu k určenému kořeni. Přiřadíme
vrcholům váhy w_v a každé orientované hraně u→v váhu w_v;
váha stromu je součin vah jeho hran.

Pro a běžných vrcholů s vahami z_1,...,z_a a kořen
s vahou x je součet vah všech těchto stromů

```text
x(x+z_1+...+z_a)^(a−1),       a>=1.                      (H1)
```

Krátký důkaz používá Prüferův kód: opakovaně odstraníme
nejmenší list a zapíšeme jeho souseda, až zbude hrana.
Vznikne posloupnost délky a−1; vrchol v se v ní vyskytne
právě deg(v)−1-krát. Inverze vždy připojí nejmenší dosud
nepoužitý vrchol, který se již nevyskytuje ve zbývajícím
kódu, k první značce kódu; na konci spojí poslední dva
vrcholy. To dokazuje bijekci se všemi posloupnostmi.
Při orientaci ke kořeni je jeho počet příchozích hran
deg(root), u ostatních deg(v)−1. Váha stromu je tedy
x krát součin vah značek kódu. Součet přes všechny kódy
je (H1). Pro a=0 je jediný prázdný strom a váha je 1;
výraz x*x^−1 se v tomto případě zkrátí před dosazováním.

Nyní vezměme n běžných vrcholů a dvě zvláštní značky
X,U s vahami x,u. Každému běžnému vrcholu nezávisle
zvolíme jednu cílovou značku z n+2 možností, včetně jeho
samého. Celkový součet vah všech takových funkcí je
`(x+u+Z)^n`, kde Z=sum_{i=1}^n z_i.

Nechť A je množina vrcholů, jejichž opakované následování
cíle dojde do X. Na A spolu s X vznikne právě zakořeněný
strom; nemůže obsahovat cyklus a každá cesta dojde do X.
Jeho váha má součet `x(x+Z_A)^(|A|−1)` podle (H1), kde
Z_A=sum_{i in A} z_i. Každý vrchol mimo A smí volit
jen cíle mimo A a značku U, proto zbytek přispěje
`(u+Z−Z_A)^(n−|A|)`.

Rozdělení všech funkcí podle jednoznačně určené A dává
Hurwitzovu identitu po dosazení y=u+Z:

```text
sum_{A subset {1,...,n}} x(x+Z_A)^(|A|−1)(y−Z_A)^(n−|A|)
 = (x+y)^n.                                               (H2)
```

Vše je polynomiální v x,u,z_i a substituce y=u+Z je
invertibilní. Důkaz tedy není omezen na kladné váhy;
platí pro reálné či komplexní parametry po odstranění
zdánlivé singularity členu A=prázdná množina.
Položení všech z_i=−z dává Abelovu formuli (16).

## Symetrická forma v odpovědi 51

V (H1) dejme každému běžnému vrcholu váhu z a kořeni
váhu x+y. U každé hrany vstupující do kořene rozepíšeme
její váhu jako x+y; při volbě x ji připojíme ke kořeni X,
při volbě y ke kořeni Y. Dostaneme dva zakořeněné stromy,
jejichž běžné vrcholy tvoří rozklad množiny do A a jejího
doplňku. Obráceně sloučení kořenů X,Y vždy vrátí původní
strom s vyznačenými volbami. Proto

```text
sum_{k=0}^n C(n,k)x(x+kz)^(k−1)
                    y(y+(n−k)z)^(n−k−1)
 = (x+y)(x+y+nz)^(n−1).                                  (H3)
```

Oba prázdné podstromy se interpretují podle konvence u (H1).
Pro n=0 je pravá strana také 1 po zkrácení. Stejnou
identitu lze získat jako nejvyšší homogenní část Rotheho
konvoluce z `rothe-abel.md`. Odkazy do §2.3.4.4 jsou tak
matematicky podpořeny nezávislým důkazem; přesné znění
odkazovaných úloh se ověří při kontrole příslušné sekce.

## Ocas nekonečné Abelovy řady v odpovědi 52

Pro obecné komplexní n a z!=0 označme k-tý člen

```text
t_k=C(n,k)x(x−kz)^(k−1)(y+kz)^(n−k),    k>=0,             (H4)
```

s t_0=y^n po zkrácení. Mocniny s necelým exponentem
vyžadují souhlasnou místní větev logaritmu; jednotlivé
konečné členy musejí být definované. Analytický obor tedy
nezahrnuje například y+kz=0 s neodstranitelným záporným
exponentem. Tvrzení o konvergenci ocasu takové singularity
neodstraní. Pro nezáporné celé n je řada konečná.

Pro ostatní n platí
`C(n,k)=(−1)^k Gamma(k−n)/(Gamma(−n)Gamma(k+1))`.
Asymptotika podílu Gamma a rozvoje log(1+v) u v=0 dávají

```text
C(n,k) = (−1)^k k^(−n−1)/Gamma(−n) * (1+O(1/k)),
(1−x/(kz))^(k−1) = exp(−x/z)(1+O(1/k)),
(1+y/(kz))^(n−k) = exp(−y/z)(1+O(1/k)),
t_k = −x z^(n−1)exp(−(x+y)/z)/Gamma(−n)
                       * k^(−2)(1+O(1/k)).               (H5)
```

Celočíselné exponenty umožňují přesně vykrátit všechny
mocniny k z. Logaritmus z je pevný na zvolené místní
oblasti; pro velké k je log(kz)=log k+Log z.
Odhady jsou stejnoměrné na kompaktních množinách parametrů
uvnitř analytického oboru, zvláště v kladné vzdálenosti
od z=0. V blízkosti nezáporných celých n použijeme
Gamma podíl krát celistvou 1/Gamma(−n), takže majoranta
O(k^−2) zůstává platná i přes ukončené případy.

Tím je doložena absolutní konvergence a lokální stejnoměrná
konvergence. Součet je holomorfní na uvedených oblastech
a lze jej derivovat po členech. „Uniform in bounded regions“
z odpovědi je nutné chápat uvnitř takové oblasti, nikoli
pro libovolné omezené množiny přibližující se k singularitě.

## Dvě derivace a závislost na z

Při z=1 označme součet f(x,y,n). Identita
`(n−k)C(n,k)=n C(n−1,k)` okamžitě dává
`partial_y f=n f(x,y,n−1)`.
Pro k>=1 je polynomiálně

```text
d/dx [x(x−k)^(k−1)] = k(x−1)(x−k)^(k−2),
```

s odstraněním zdánlivé singularity při k=1.
Člen k=0 má derivaci 0. Použijeme
`k C(n,k)=n C(n−1,k−1)` a posun k→k+1; dostaneme
`partial_x f=n f(x−1,y+1,n−1)`, jak tvrdí opravená odpověď.
Oba překlepy r→n jsou známé erratum z 26. ledna 1998.

Závislost na z není identicky nulová. Například pro
n=x=−1,y=1 a reálné z>0 je (H4) přesně `(1+kz)^−2`.
Derivace součtu je `−2 sum_{k>=1} k/(1+kz)^3<0`.
To dokládá poznámku o obecné závislosti na z bez potřeby
neurčitého zacházení s 0^−1 na levé straně Abelovy formule.
Věta odpovědi, že shoda s (x+y)^n se „zdá“ vzácná,
je pozorování, nikoli přesně formulovaná klasifikační věta.

Atribuce Hurwitzovi a Hautusovi vyžadují samostatné prameny;
matematické důkazy výše samy historickou prioritu nepotvrzují.


## Recovery scope correction, 6 November 2026

The compact-domain proof above remains accepted. The original phrase
“uniform in bounded regions” is now separately partial: the exact witness
x=n=-1,y=1,0<z≤1 has t_k=(1+kz)^(-2) with supremum1. The implicit
compact-domain reading is possible but not established by the printed
wording alone. See `quality-recovery-section-1.2.6-2026-11-06.md` §1.
No new confirmed finding or candidate card is created.
