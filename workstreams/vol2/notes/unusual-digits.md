# §4.1: neobvyklé číslice a rozklady nezáporných čísel

## Rozsah a značení

Úlohy 19–24 a 29 jsou prověřeny obecnými důkazy níže, včetně doplňujících
matematických tvrzení v odpovědích. Úloha 29 je zařazena před klasifikaci
v §7, protože právě její rozklad vysvětluje úplnost dvou rodin z úlohy 24.
V poznámce za odpovědí 24 je potvrzen nový nález **V2-C0079**; přesný
protipříklad a oprava jsou v §8. Klasifikace se tím nemění.

`b>=2` je celočíselný základ. Konečné slovo číslic z konečné množiny D
má hodnotu `sum(j=0..n) d_j b^j`. Úvodní nuly nerozlišujeme, pokud 0
patří do D. Nekonečná reprezentace má konečnou nejvyšší pozici n a
cifry ve všech pozicích `j<=n`; řada konverguje absolutně.
`S_D={sum(j>=1) d_j b^(−j): d_j in D}` označuje zlomkovou množinu.
Je kompaktní: ocasy jsou rovnoměrně omezené geometrickou řadou a z
posloupnosti zápisů lze diagonálně vybrat ustalující se cifry.

Původní strany 210–212 a 607–609 byly přečteny vizuálně.
Čtyři vrstvy errat (`all2-prepre`, `all2-pre`, `all2`, `err2`) a aktuální
TeX jsou zkontrolovány; [výňatek](../sources/positional-errata-excerpts.txt)
obsahuje také známé opravy odpovědi 21 a bibliografie odpovědi 24.
Vlastní [verifier](../verify_unusual_digits.py) má šest úspěšných bloků
v [JSON](../results/unusual-digits.json) a [logu](../results/unusual-digits.log).
Poslední blok byl přidán po objevu C0079; dřívější úspěšné bloky se
neopakovaly. Konečné testy nenahrazují důkazy existence a klasifikace.

## 1. Úloha 19: kritický interval

Předpokládejme, že D obsahuje právě jednoho reprezentanta každé třídy
zbytků modulo b. Pro celé m je poslední cifra `d(m)` nucena kongruencí
`d(m)=m (mod b)`. Označme `q(m)=(m−d(m))/b` a

```
l = −max(D)/(b−1),       u = −min(D)/(b−1).
```

Je-li `m>u`, potom `l<q(m)<m`; je-li `m<l`, potom `m<q(m)<u`.
To plyne přímým dosazením nejmenší a největší cifry. Dělení tedy mimo
uzavřený interval `[l,u]` snižuje celočíselnou vzdálenost od tohoto
intervalu a nemůže přeskočit z jedné strany na druhou. Po konečně mnoha
krocích vstoupí do intervalu. Zápis kteréhokoli jeho celého bodu pak
lze doplnit dosud vybranými ciframi. Nutnost kritéria je okamžitá;
tím je dokázáno obojí „právě tehdy“ v zadání.

Pokud je `0 in D`, je každý konečný zápis jednoznačný: poslední cifra
a podíl jsou nuceny a zápis nuly obsahuje jen nuly. Pokud `0 not in D`
a všechna celá čísla jsou reprezentovatelná, má nula neprázdný zápis w.
Připojení w vlevo k jakémukoli slovu dává další zápis stejné hodnoty.
Tištěný příklad `D={−3,−1,7}`, `b=3` používá
`(−3,7,7,−3)_3=0`, protože `−81+63+21−3=0`.

Pro `b=2` není řešení: pro každou nenulovou cifru a je nenulové číslo
`m=−a` pevným bodem q, neboť `−a=a (mod 2)` a `q(−a)=−a`.
Jeho dělení se nikdy nedostane k nule, takže nemá konečný zápis.

Pro `b>=3` a `|a|<b` musí cifrou zbytku 0 být 0. Cifry `b−1` a
`−(b−1)` jsou zakázány, protože dávají pevné body −1 a 1. Zbytky 1
resp. b−1 proto musí zastupovat 1 resp. −1. Každý z ostatních zbytků
`r=2,...,b−2` lze zastoupit r nebo r−b. V každé takto vzniklé soustavě
platí `−1<l<=u<1`, takže jediným kritickým celým bodem je 0.
Počet řešení je tudíž přesně `2^(b−3)`.

U delší tištěné rodiny zvolme `n>=1`, `epsilon_0=epsilon_1=0`,
`epsilon_(b−1)=1` a ostatní epsilon libovolně 0/1. Číslice jsou
`d_r=r−epsilon_r b^n`. Pro `0<=m<b^n` má obvyklý zápis n cifer r_j.
Identita

```
m = sum(j=0..n−1) d_(r_j) b^j
  + sum(j=0..n−1) epsilon_(r_j) b^(j+n)             (1)
```

je už platným zápisem délky nejvýše 2n: spodní a horní pozice se
nepřekrývají a 0,1 jsou povolené cifry. Přitom `max(D)<=b−2` a
`min(D)>=2−b^n`, takže všechny kritické
celé body leží v `[0,b^n)`. Kritérium proto dokazuje celou rodinu.

Verifier prošel 4094 sad omezených cifer pro b=2 až 12, 124 dlouhých
sad a všech jejich 61152 stavů z (1), dále 360 obecných sad reprezentantů.
U 75 platných sad z posledního soupisu zrekonstruoval 7575 celých čísel.
To zahrnuje i případy bez nulové cifry; zápis nuly zde musí být neprázdný.

Primární [Matulův technický report z června 1978](https://upload.wikimedia.org/wikipedia/commons/f/fe/Basic_digit_sets_for_radix_representation_%28IA_basicdigitsetsfo00matu%29.pdf)
byl přečten v Lemma 8, Corollary 8.1, Lemma 10, Corollary 10.1 a
Theorem 11, včetně vizuální kontroly stran 12–13 a 17–18. Obsahuje
kritický interval, počet omezených sad a speciální případ (1).
Nejde o tvrzení, že byl přečten celý report nebo pozdější článek JACM.

## 2. Úloha 20: devět reprezentací a obecná horní mez

Zde `D={−1,0,8,17,26,35,44,53,62,71}`. Kritické celé body jsou
−7 až 0. Pro `m=−j`, `1<=j<=7`, je vybraná cifra `9j−10` a
`q(−j)=1−j`; všechny tedy dojdou do nuly. Celá čísla mají jednoznačné
konečné zápisy.

Pro úplnost doložme i přechod k reálným číslům. Obecně pro soustavu s
konečnými zápisy všech celých čísel a nulovou cifrou položme
`A=max{|d|:d in D}`. Po k děleních platí

```
|q^k(m)| <= b^(−k)|m| + A/(b−1).
```

Pro `m_k=floor(b^k x)` je pravá strana omezená nezávisle na k. Zbývající
podíly proto patří do konečné množiny celých čísel, jejichž konečné
zápisy mají společnou délkovou mez L. Zápisy `m_k/b^k` mají nejvyšší
pozici nejvýše L−1, a tudíž patří do kompaktní množiny `b^L S_D`.
Jejich limita x tam patří také. Pro x v omezeném intervalu lze zvolit
stejné L, což dokonce dává interval kolem nuly uvnitř vhodného násobku S_D.

Číslo `x=−1/9` má devět zápisů. Pro `j=0,...,8` použijeme konečný
celočíselný prefix s hodnotou −j a opakovaný zlomkový digit `9j−1`:

```
−j + (9j−1)/9 = −1/9.                              (2)
```

Prefixy jsou postupně `0`, `−1`, `(−1,8)`, `(−1,8,17)`, ...,
`(−1,8,17,26,35,44,53,62)`. To přesně vysvětluje tištěné indexované
číslice, které OCR slévá do obyčejných desítkových čísel.

Vždy `S_D subset [−1/9,71/9]`, tedy má šířku nejvýše 8.
Deset různých reprezentací lze posunout o společných k pozic tak,
aby se jejich celé prefixy lišily. Hodnoty prefixů jsou díky jednoznačnosti
celých zápisů deset různých celých čísel. Krajní dvě se liší alespoň o 9,
ale jejich rozdíl musí být opačným rozdílem dvou zlomků z S_D,
tedy nejvýše 8. Spor dokazuje obecné maximum 9, a (2) jeho ostrost.

Pro nespočetně mnoho příkladů vezměme všechny zlomkové řady s ciframi
pouze −1 nebo 8. První odlišná cifra v pozici −k způsobí rozdíl
`9*10^(−k)`, který pozdější ocas může zmenšit nejvýše o `10^(−k)`.
Různé bitové posloupnosti tedy dávají různá reálná čísla. Pro každé
`j=0,...,7` přidáme ke každé cifře 9j a před čárku prefix hodnoty −j.
Hodnota se nezmění; všechny nové cifry stále leží v D. Každé takto
získané číslo má aspoň osm zápisů. Přesná kontrola 1024 periodických
příkladů dává 8192 shod, ale nespočetnost plyne z obecného argumentu.

## 3. Úloha 21: polocelé vyvážené cifry

Číslice `a_k` jsou `−9/2,−7/2,...,9/2`. Pro pevnou nejvyšší pozici n
položme `r_k=a_k+9/2`, takže r_k jsou běžné cifry 0 až 9. Potom

```
x = sum(k<=n) a_k 10^k
  = sum(k<=n) r_k 10^k − 5*10^n.                  (3)
```

Možné hodnoty tvoří celý interval `[-5*10^n,5*10^n]`. Libovolné reálné
x do něj patří pro všechna dost velká n; protože žádná povolená cifra
není nulová, různé nejvyšší pozice dávají různé zápisy. Každé reálné
číslo má tedy nekonečně mnoho reprezentací.

Pro nulu má běžné číslo v (3) hodnotu `5*10^n`. Jeho dva desítkové
zápisy dávají právě

```
+(1/2)*10^n + sum(k<n) (−9/2)*10^k,
−(1/2)*10^n + sum(k<n) (+9/2)*10^k,               n in Z.
```

Pro jednotku jsou přípustná právě n>=0 a vždy dva zápisy.
Pro n=0 jde o první cifru 3/2 s ocasem samých −9/2 nebo první cifru
1/2 s ocasem samých +9/2. Pro n>=1 je cifra na pozici n rovna 1/2,
na pozicích n−1 až 1 rovna −9/2, a zbytek je buď cifra −7/2 na
pozici 0 s ocasem −9/2, nebo cifra −9/2 na pozici 0 s ocasem +9/2.
Úplnost seznamu plyne z úplné klasifikace běžných desetinných zápisů.
Všechny tištěné první případy souhlasí. Známá errata opravují pouze
„test“ na „text“ (1999) a plurál „systems“ na „system“ (2007).

## 4. Úloha 22: hustota bez záporných mocnin

Nechť `alpha=−sum(r>=1) 10^(−r²)`. Povolené cifry jsou 0,1,alpha,
ale jen v nezáporných pozicích. Níže je přesná verze přibližného kroku
z odpovědi; nepředpokládá praktickou rychlost vzniklého zápisu.

Máme hotový konečný zápis P s nejvyšší pozicí N. Zvolme t>=1 a označme
`delta=10^(−t)`. Pro dost velké j položme `m=j²−t` tak, aby
`m>N` a `2j−1−t>N`. Na pozici m vložme alpha a na pozice
`m−r²`, `1<=r<j`, vložme jedničky. Všechny nové pozice jsou větší
než N, takže nenastává konflikt s dosavadními ciframi. Čistá změna je

```
10^m alpha + sum(r=1..j−1) 10^(m−r²)
    = −delta − sum(r>j) 10^(j²−t−r²).
```

Poslední kladný ocas je menší než
`(10/9)*10^(−t−2j−1)` a volbou j jej lze udělat menší než delta.
Krok tedy sníží hodnotu o číslo přísně mezi delta a 2delta.

Pro dané x a epsilon>0 vyberme P s ciframi 0/1 tak velké, že P>x,
a t tak, aby `2delta<epsilon`. Dokud `P−x>2delta`, provedeme uvedený
krok. Chyba zůstává přísně kladná a klesá aspoň o delta, takže po
konečně mnoha krocích leží v `(0,2delta]`. To dokazuje požadovanou
ostrou nerovnost `0<|P−x|<epsilon`, včetně případů, kdy by jiné
aproximační postupy zasáhly x přesně.
Verifier certifikuje 36 samostatných kroků racionálními obálkami alpha;
nepředstírá materializaci celého potenciálně astronomického zápisu.

## 5. Úloha 23: násobnost a míra

Mírou μ rozumíme Lebesgueovu délku množiny reálných čísel. Nechť D
obsahuje b reálných cifer a reprezentuje všechna kladná reálná čísla.
Protože reprezentovatelná čísla tvoří `union(n in Z) b^n S_D`, musí
mít S_D kladnou míru; jinak by spočetné sjednocení mělo míru nula.
Její míra je konečná díky omezenosti. Rovnost množin

```
b S_D = union(d in D) (d+S_D)
```

má vlevo míru `b μ(S_D)`, rovnou součtu měr všech b členů vpravo.
Proto každé dva různé členy mají průnik míry nula.

Pokud `0 in D`, lze dvě různé reprezentace zarovnat úvodními nulami.
V první odlišné pozici mají cifry d,e a společný vyšší prefix p.
Jejich společná hodnota proto patří do posunuté a škálované kopie
`(d+S_D) intersect (e+S_D)`. Prefixů, pozic a dvojic cifer je spočetně
mnoho; jejich sjednocení má míru nula. To dokazuje tvrzení o množině T
všech čísel s více zápisy. Bez nulové cifry dává §3 protipříklad `T=R`.

Doplňující tvrzení, že T není prázdná, lze doložit bez topologické
klasifikace rozkladů přímky. Z Baireovy věty (interval nelze pokrýt
spočetně mnoha uzavřenými množinami s prázdným vnitřkem) a pokrytí
`[1,2]` množinami `b^n S_D` plyne, že S_D obsahuje neprázdný interval.
Kdyby žádné dva zápisy neměly stejnou hodnotu, konečně mnoho kompaktních
cylindrů s prefixem délky r by bylo navzájem disjunktních. Souvislý
interval uvnitř S_D by musel celý ležet v jediném z nich. Jejich průměry
však jsou nejvýše `diam(S_D)/b^r -> 0`, což je spor.

Pro méně než b cifer dává nerovnost `b μ(S_D)<=|D| μ(S_D)` nulovou
míru S_D, a tedy všech reprezentovatelných čísel. Pro více než b cifer
při reprezentovatelnosti všech reálných čísel má S_D kladnou míru a
součet měr jeho prvních kopií převyšuje míru jejich sjednocení.
Některý průnik má proto kladnou míru a obsahuje dvě různé reprezentace.
Jeho libovolně velké násobky b^n také leží v T, takže `μ(T)=infinity`.
Tyto důkazy nevyžadují celočíselné cifry.

## 6. Úloha 29: úplný rozklad pomocí smíšených základů

Označme `N0={0,1,2,...}`. Zápis `A ⊕ B` znamená, že každý prvek
součtu množin A+B má právě jedno vyjádření `a+b`. Aditivní systém
zde znamená rodinu množin T_i obsahujících 0, pro kterou
`N0=⊕_i T_i`; v každém součtu je jen konečně mnoho nenulových členů.
To je Property B v zadání. Slučování několika složek do jejich součtu
zachovává existenci i jednoznačnost přímo podle definice.

Vyberme jedinou složku obsahující 1 a označme ji T_0. Nejprve uvažujme,
že `T_0 != N0`, a nechť b>=2 je nejmenší číslo, které v T_0 není.
Čísla 1 až b−1 leží pouze v T_0; samotné b proto musí ležet v některé
jiné složce T_h. Indukcí podle n dokážeme:

* Pokud `nb not in T_0`, žádné z `nb+1,...,nb+b−1` neleží v žádné T_i.
* Pokud `nb in T_0`, všechna tato čísla leží v T_0 a v žádné jiné složce.

Pro n=0 je tvrzení přímo volbou b. Předpokládejme nižší bloky hotové.
V reprezentaci nb jsou všechny členy z jiných složek násobky b: menší
členy podle indukce, případný člen rovný nb zřejmě také. Člen t_0
je tedy rovněž násobkem b.

Je-li `nb not in T_0`, máme t_0<nb a pro `0<r<b` dává indukce
`t_0+r in T_0`. Reprezentace `(t_0+r)+sum(i>0)t_i` čísla nb+r má
aspoň dva nenulové členy, takže toto číslo nesmí zároveň ležet v žádné
samotné T_i. Je-li `nb in T_0`, žádné nb+r nesmí ležet v jiné T_i:
jinak by `(nb)+b`, s b ve složce T_h, a `(b−r)+(nb+r)` byly dva
různé zápisy `(n+1)b`. V libovolné reprezentaci nb+r jsou proto členy
mimo T_0 opět násobky b. Je-li t_0 menší než nb+r, leží v nižším
bloku, a indukce dovolí odečíst od něj r. Dostali bychom druhý zápis nb,
což je spor. Tedy `t_0=nb+r` a ostatní členy jsou nulové.

Z obou případů dostáváme přesný rozklad

```
T_0 = {0,...,b−1} ⊕ b T'_0,       T_i=b T'_i (i>0).
```

Dělením reprezentací násobků b vidíme, že i rodina T'_i je aditivním
systémem. Jestliže naopak `T_0=N0`, jsou ostatní složky {0} a můžeme
použít stejný rozklad s b=2 a `T'_0=N0`. Tím je ošetřen případ, který
kniha přechází větou „we may assume“.

Rozklad opakujme, přičemž každá zbytková složka stále nese jméno
původní složky. Po r krocích je každá původní T_i přímým součtem
přidělených bloků `B_j {0,...,b_j−1}` a zbytku `B_r T_i^(r)`,
kde `B_0=1`, `B_(j+1)=B_j b_j`. Protože `B_r>=2^r`, pro každý
pevný prvek t původní T_i je při `B_r>t` zbytkový člen nutně nulový.
Tedy t je konečným součtem přidělených bloků. Naopak každý takový
konečný součet patří do T_i podle konečného invariantního rozkladu.
Bloky mají navzájem jednoznačný smíšený zápis; jejich přidělení původním
složkám je požadovaná partition indexů. Tím je doložen i nekonečný
limitní krok, nikoli jen první redukce.

Libovolný složený základ lze rozdělit na prvočinitele identitou
`{0,...,uv−1}={0,...,u−1} ⊕ u{0,...,v−1}`, přičemž obě části
ponecháme témuž vlastníkovi. Proto lze všechny bloky dále zjemnit na
prvočíselné základy. Použijeme to v §7. Také konečný analog plyne
přidáním složky `M N0` k přímému rozkladu intervalu `{0,...,M−1}`;
všechny původní konečné bloky pak leží před vahou M.

Pro kontrolu formulace a limitního kroku byly čteny Lemma 7 a Theorem 3
včetně důkazů na stranách 5–8 primárního článku
[M. B. Nathanson, *Additive systems and a theorem of de Bruijn*, arXiv:1301.6208v2](https://arxiv.org/abs/1301.6208v2).
Jeho reference potvrzuje citaci de Bruijnova článku `(3) 4 (1956), 15–17`.
Originál z roku 1956 a MacMahonovy stránky nebyly samostatně získány;
výše je úplný rozpis argumentu knihy, nikoli odkaz místo důkazu.

## 7. Úloha 24: konstrukce, celočíselnost a úplnost klasifikace

Obě rodiny v odpovědi jsou

```
D_k = {2 a 10^k + c : 0<=a<5, 0<=c<2},
E_k = {5 c 10^k + a : 0<=a<5, 0<=c<2},       k>=0.        (4)
```

Každá má deset různých nezáporných číslic, obsahuje 0 i 1 a má gcd 1.
Pro k=0 jsou obě běžnou sadou 0 až 9, jinak rostou jejich maxima.
Rozložme každou běžnou desítkovou cifru jako `2a+c` nebo `5c+a`.
Posuneme-li proud příslušných a nebo c o k pozic dolů a zvětšíme jejich
hodnotu faktorem `10^k`, dostaneme právě cifry (4) při nezměněné hodnotě.
To funguje pro libovolný nekonečný zlomek i konečný horní konec zápisu,
a dokazuje reprezentovatelnost všech kladných reálných čísel.
Verifier navíc přesně zrekonstruoval 10000 konečných příkladů.

Následující důkaz rozepisuje Odlyzkův argument z knihy a poté používá §6
k doplnění Grahamovy klasifikace. Nechť D je sada b nezáporných reálných
cifer, její dvě nejmenší cifry jsou 0 a 1 a všechny kladné reálné hodnoty
jsou reprezentovatelné. Nechť X je množina konečných celých prefixů a
`S=S_D`. Pak `X+S=[0,infinity)`, S je kompaktní a X je lokálně konečná:
prefix hodnoty nejvýše R má omezenou nejvyšší pozici a konečně mnoho cifer.
Různé prefixové buňky x+S mají průnik míry nula podle prvního rozdílného
digitu a §5. Stejný argument vylučuje dva různé konečné prefixy stejné
hodnoty, protože jinak by se překrývala celá kopie S kladné míry.
Protože nejmenší kladný prvek X je 1, pokrytí dává `[0,1] subset S`.

Indukcí dokážeme, že pro každé celé m>=0 existuje celé `x_m in X`,
`0<=x_m<=m`, s `[m,m+1] subset x_m+S`. Pro m=0 je to hotovo.
Před krokem m nemůže v X ležet žádné necelé x<=m: interval `[x,x+1]`
patří do x+S a pozitivně překrývá již hotovou buňku pro `floor(x)`.
Dále každá celočíselná buňka x+S, `0<x<=m`, která se s `(m,m+1)`
překrývá v kladné míře, obsahuje celý `[m,m+1]`: po odečtení x
indukce na `m−x<m` a disjunktnost měr nutí `[m−x,m−x+1] subset S`.

Z lokální konečnosti X lze vybrat buňku x+S, jež má kladný průnik
s `(m,m+epsilon)` pro každé epsilon>0. Má x<=m a x je celé.
Pokud x>0, předchozí odstavec krok uzavírá. Pokud x=0, žádná jiná
celočíselná buňka nemůže mít kladný průnik s `(m,m+1)`, neboť by
obsahovala celý interval a překrývala S u m. Pokud v `(m,m+1)` není
žádný prvek X, z pokrytí a uzavřenosti vyplývá `[m,m+1] subset S`.
Pokud tam prvek X je, vezměme nejmenší takový v. Do v mohou pokrytí
zajišťovat jen S a konečně mnoho buněk nulového průniku, takže
`[m,v] subset S`. Ale `1+S` pak obsahuje `[m+1,v+1]` a `v+S`
obsahuje `[v,v+1]`; jejich průnik má délku v−m>0. Spor. Indukce je hotova.
Každý necelý prvek X by opět překrýval buňku pro svou dolní celou část,
takže **všechny prvky X, a tedy všechny cifry D, jsou celé**.

Navíc `S=closure(interior S)`: každou bodovou reprezentaci aproximují
její prefixy, a vedle každého prefixu leží zmenšený interval z `[0,1]`.
Předchozí indukce a nulové průniky buněk proto dávají

```
S = union(j in J) [j,j+1],
N0 = J ⊕ X = J ⊕ D ⊕ 10D ⊕ 100D ⊕ ...,           (5)
```

kde J je konečná množina nezáporných celých čísel obsahující 0.
Pro obecnou celočíselnou sadu s gcd 1 nejprve dělíme její nejmenší
kladnou cifrou h. Právě dokázaná celočíselnost normalizované sady znamená,
že h dělí všechny původní cifry. Proto h=gcd(D)=1 a (5) platí přímo.

Nyní b=10. Zjemněme aditivní systém (5) podle §6 na prvočíselné bloky.
Složka D má deset prvků, takže dostane právě dva bloky s radicy
`p,q`, kde `{p,q}={2,5}`. Její nejmenší kladný prvek 1 nutí první
váhu 1. Proto

```
D = {0,...,p−1} ⊕ G{0,...,q−1},       p divides G.        (6)
```

Je-li G=p, jde o běžné cifry. Jinak G>p a p je nejmenší nezáporné
celé číslo chybějící v D. Každá složka `10^j D` má analogicky první
váhu `10^j` a první radix p. Proč právě p: dva její prvočíselné bloky
buď sousedí a tvoří běžný desetiprvkový interval, nebo mezi nimi
vzniká první mezera hned za prvním radixem; tento první chybějící
násobek `10^j` je podle (6) p.

Všechny váhy smíšené soustavy tvoří rostoucí řetězec dělitelnosti.
Váha G nemůže být `10^j`, protože tuto váhu už vlastní první blok
složky `10^j D`. Zvolme tedy k tak, že `10^k<G<10^(k+1)`.
Pak `10^k divides G divides 10^(k+1)`. Bezprostředně za vahou
`10^k` stojí váha `p*10^k`, takže také `p*10^k divides G`.
Jediným vlastním dělitelem 10, který je násobkem p a větší než 1,
je p. Tudíž `G=p*10^k`. Rovnice (6) dává přesně obě rodiny (4).
Tím je ověřena i nutnost klasifikace, nikoli pouze vytištěné příklady.

Citace Odlyzkova článku byla známým erratem z 22. 8. 2019 opravena
na *Proc. London Math. Soc.* (3) 37 (1978), 213–229. Souhlasí s
[autorským seznamem publikací](https://www-users.cse.umn.edu/~odlyzko/doc/numbertheory.html)
a [záznamem vydavatele](https://doi.org/10.1112/plms/s3-37.2.213).
Plný článek vrátil HTTP 403 a není vydáván za přečtený; výše je vlastní
úplný důkaz tvrzení potřebných pro audit.

## 8. Poznámka za úlohou 24 a nález V2-C0079

První dvě uvedené sady bez nuly jsou správné. Pro `D={1,...,10}`
tvoří zlomky interval `[1/9,10/9]`; jeho násobky mocninami 10 pokrývají
všechna kladná reálná čísla. Pro
`D={1,2,3,4,5,51,52,53,54,55}` je přesná zlomková množina
`[1/9,10/9] union [46/9,55/9]`, takže první interval stačí.

**Třetí sada `D={2,3,4,5,6,52,53,54,55,56}` nevyhovuje.**
Číslo 3/2 nemá reprezentaci. Nechť n je nejvyšší obsazená pozice.
Pro n>=0 je hodnota alespoň 2. Pro n<=−2 je hodnota nejvýše
`56 sum(k<=−2)10^k=28/45`. Pro n=−1 rozdělme první cifru:

```
a_(−1)<=6  => x <= 6/10 + 56/90 = 11/9 < 3/2,
a_(−1)>=52 => x >= 52/10 = 26/5 > 3/2.
```

Tím jsou vyčerpány všechny pozice a cifry. Argument zůstává platný,
i kdyby někdo navíc dovolil ukončení zápisu implicitními nulami vpravo.
Nejde tedy o spor o konvenci konečných zlomků.

Nezávislý přesný popis vychází ze sady
`B={0,1,2,3,4,50,51,52,53,54}`. Každou její cifru napišme `a+50c`.
První c dává posun 0 nebo 5, zatímco ostatní c se spojí s a do běžných
cifer 0 až 9. Proto `S_B=[0,1] union [5,6]`. Posun všech cifer o h
posune zlomky o h/9. Pro h=2 tedy

```
S_D = [2/9,11/9] union [47/9,56/9].                (7)
```

Verifier navíc přímo sjednotil všech dvacet intervalů `(d+S_D)/10`
a dostal přesně (7), obdobně pro h=0 a 1. To je nezávislá kontrola
celé oblasti, nikoli jen numerický pokus o zápis 3/2.

Poslední příklad s negativními ciframi
`D={−1,0,1,2,3,4,5,6,7,18}` je naopak správný v rozsahu zadání,
které vyžaduje **kladná** reálná čísla. Všechna nezáporná celá čísla
mají konečný zápis: nucené q pro m>0 splňuje `0<=q(m)<m`, s jedinou
výjimkou `m=8`, kdy q=−1 a další krok je 0. Kompaktní argument z §2
s nezápornými aproximacemi dokazuje všechna kladná reálná čísla.
Kritériu 19 pro všechna celá čísla sada nevyhovuje, neboť q(−2)=−2.
Tyto dvě vlastnosti se nesmějí zaměnit.

Původní sada pro C0079 je zřetelná na [straně 608](../images/vol2-p608.png).
Vyhledání stránky, číslic a pojmů ve všech čtyřech řadách errat i aktuálním
TeXu neodhalilo tuto opravu. Změna 2001 odstraňuje závorku, změna 2019
opravuje bibliografii; ani jedna cifry nemění. Doporučená minimální oprava
je třetí chybný příklad vypustit. [Návrh hlášení](../reports/C0079-nonzero-digit-set-draft.txt)
nebyl odeslán. Nejnovější fyzický dotisk, prvenství ani nárok na odměnu
nejsou ověřeny.
