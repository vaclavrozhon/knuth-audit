# MPR 9–10: maximální nerovnosti a omezené rozdíly

D100–D101, 6. listopadu 2026. Zobrazeny celé původní file29–30,
celá zadání 86,90,91 na file40 a celé odpovědi na file403. Dále byl
zobrazen přesně používaný vzorec (*) v odpovědi35 na file396 a
Taylorův vzorec 1.2.11.3–(5) ve svazku1, tištěná117/file132.
Tyto vzdálené stránky nejsou automaticky celé reviewed.

## D100 — str.9, každý maximální odhad a celý důkaz Azumy

**(33) a celá MPR86.** Předchozí D099 již dokázal tvrzení zastavením
nezáporného submartingalu při prvním Zj≥x, nejpozději v čase n.
Pro přesný tištěný zápis odpovědi86 zvolíme m=n+1. Pravidlo

```
N_{j+1} = [max(Z0,…,Zj)<x and j+1<m]
```

je funkcí známé historie. Jakmile jednou selže práh nebo časová
podmínka, nemůže se vrátit z0 na1: dosavadní maximum ani čas neklesají.
Počet provedených kroků N je nejvýše m−1=n. Pokud je Z0≥x,
je N=0; pokud se práh dosáhne poprvé v čase j≤n, je N=j;
pokud se nedosáhne vůbec, je N=n. Tím se pokryjí všechny okraje.

Události {max_{0≤j≤n}Zj≥x} a {ZN≥x} jsou stejné. Nezápornost
ZN a x>0 opravňují Markova; omezené zastavení submartingalu dává
EZN≤EZn. Odtud (33). Tištěný výskyt m−1 v prvních dvou větách
a n v závěru je tedy konzistentní volbou m=n+1, nikoli další chyba.
Celé zadání i odpověď86 jsou tím uzavřeny.

**(34),(35), jejich předpoklady a (36).** Funkce |z| a z² jsou
konvexní; úplný důkaz převodu na submartingale v D099 už používá
správné dvojí podmínění. Jsou nezáporné, a proto (33) dává přesně
(34) a (35), včetně všech indexů0,…,n a stejného prahu x>0.
Pro druhý vztah se předpokládá potřebný konečný druhý moment.
Je-li pravá strana +∞, samotná číselná nerovnost je triviální;
netvrdíme tím integrabilitu libovolné čtvercové transformace.

Pro Zj=Σk=1..j Xk, Z0=0, nezávislost a EXk=0 dávají
E(Xj+1|X1,…,Xj)=0; jde o martingale. Rozvinutí konečného
čtverce dává

```
E Zn² = Σk E Xk² + 2Σi<j E(XiXj)
      = Σk σk² = σ²,
```

protože každý smíšený moment je EXi EXj=0. Konečné druhé momenty
zajišťují integrabilitu každého součinu (například 2|XiXj|≤Xi²+Xj²).
V (35) dosadíme x=t²σ² a přejdeme ke komplementu. Pro t>0 a
0<σ²<∞ je {max Zj²<t²σ²} právě průnik všech |Zj|<tσ, což dává
(36) se striktními znaménky přesně tak, jak jsou vytištěna.

Tento normalizovaný přepis má tedy doménu σ>0 z pozitivního prahu
původní věty. Pro σ=0 jsou všechny Xk=0 skoro jistě; nenahrazujeme
kladný práh nulou v přepisu se striktním `<`. Přímé tvrzení pak je
max|Zj|=0 skoro jistě. Stejně se rozumí t>0; pro0<t≤1 je dolní mez
netriviální nejvýše0. Jde o výslovné vymezení domény normalizace,
nikoli novou kartu založenou na nepřípustné substituci.

Chebyshev ovládá jen poslední součet. Událost omezení všech částečných
součtů je podmnožinou události omezení posledního. Inkluze může být
ostrá: u pěti nezávislých férových ±1 má cesta +++−− kladnou
pravděpodobnost1/32, konečný součet1, ale průběžné maximum3.
Pro práh5/2 proto patří do druhé události a ne do první. To vysvětluje
konkrétně tvrzenou silnější informaci, bez předpokladu nezávislosti
samotných částečných součtů.

**MPR90(a): exponenciální Markov.** Pišme S=Σk=1..n Yk. Pro
λ>0 je exponenciála striktně rostoucí, takže {S≥x}={e^{λS}≥e^{λx}}.
Markovova nerovnost pro nezáporné e^{λS} dává
P(S≥x)≤e^{−λx}E e^{λS}. Při pevných konečných šířkách níže je S
omezené, a proto toto očekávání existuje. Bez této podmínky by byl
výrok stále pravdivý s nekonečnou pravou stranou, ale neužitečný.
Písmeno λ zde značí t z úlohy90, aby se nepletlo s počtem objektů
v následujícím hašovacím příkladu.

**MPR90(b): každá váha a algebra.** Pro p∈[0,1], q=1−p a
−p≤y≤q platí

```
y = (q−y)(−p) + (y+p)q,
(q−y)+(y+p)=1,
q−y≥0, y+p≥0.
```

Konvexita exponenciály dává

```
e^{λy} ≤ (q−y)e^{−pλ}+(y+p)e^{qλ}
       = e^{−pλ}(q+pe^λ) + y e^{−pλ}(e^λ−1)
       = e^{f(λ)} + y e^{g(λ)}.
```

To jsou všechny tištěné mezikroky. Logaritmus v g je konečný,
protože λ>0; q+pe^λ je vždy kladné, i pro p=0 nebo p=1.
Rovnost na obou koncích intervalu souhlasí s konstrukcí sečny.

**MPR90(c): obě derivace a přesná konstanta.** Přímá derivace dává

```
f′(λ)=−p+pe^λ/(q+pe^λ),
f″(λ)=pq e^λ/(q+pe^λ)².
```

V nule jsou f(0)=f′(0)=0. Nerovnost (u+v)²≥4uv pro
u=q,v=pe^λ plyne z (u−v)²≥0, tedy 0≤f″≤1/4. Platí také
na krajích p=0,1, kdy f≡0. Originál 1.2.11.3–(5) na p.117
má integrální Taylorův zbytek; pro řád1 přesně dává

```
f(λ)=∫0^λ u f″(λ−u) du ≤ ∫0^λ u/4 du = λ²/8.
```

Tato potřebná instance se dá rovněž přímo získat dvojím integrováním
f″ s nulovými počátečními hodnotami. Nejde o pouhé citování odhadu.
Zkontrolován byl odkaz a tento konkrétní argument, nikoli celá cizí
strana nebo celá Taylorova kapitola.

**MPR90(d): škálování a nulová šířka.** Férovost na každé kladné
historii nutí a≤0≤b, lze tedy položit c=b−a, p=−a/c, q=b/c.
Pro c>0, y=Y/c a T=cλ je y∈[−p,q]. Z(b,c) dostaneme

```
e^{λY} ≤ e^{c²λ²/8} + Y h(λ),
h(λ) = e^{g(cλ)}/c = (e^{bλ}−e^{aλ})/(b−a).
```

Každá změna měřítka v odpovědi90(d) souhlasí. Při c=0 implikuje
podmíněná nula a=b=Y=0, takže příslušný faktor je1 a z důkazu lze
vynechat; nezavádí se dělení nulou. Pokud by a,b v izolovaném
znění(d) neobsahovaly0, samotné tvrzení stále platí, i když se
tištěné škálování s p∈[0,1] nepoužije. Pro a≥0 vezmeme
h(λ)=λe^{λb}. Identita

```
e^{λY}−1 = λY ∫0^1 e^{sλY} ds
```

a vztah0≤Y≤b dávají e^{λY}−1≤λY e^{λb}=Yh(λ).
Pro b≤0 vezmeme h(λ)=λe^{λa}. Pak e^{sλY}≥e^{λa};
násobení záporným λY obrátí nerovnost a znovu dostaneme
e^{λY}−1≤Yh(λ). V obou případech1≤e^{(b−a)²λ²/8},
takže vzniká požadovaná nerovnost(d). To zahrnuje i a=b≠0.
Tím je doloženo také samostatné obecné znění(d), nejen intervaly
v jeho následné férové aplikaci. Tento krátký doplněk vznikl
při nezávislé kontrole koordinátora; nejde o chybu v knize.

**MPR90(e): součin, podmínění a F161.** Nechť ck jsou pevné šířky,
popřípadě pevné horní meze šířek. Podmíněním(d) podle historie
Hk−1 a použitím E(Yk|Hk−1)=0 dostaneme

```
E(e^{λYk}|Hk−1) ≤ exp(ck²λ²/8).
```

Pravá strana je deterministická. S_{k−1} je funkcí Hk−1, proto

```
E e^{λSk}
 = E[e^{λS_{k−1}} E(e^{λYk}|Hk−1)]
 ≤ exp(ck²λ²/8) E e^{λS_{k−1}}.
```

Konečná indukce z S0=0 vede k exp(Vλ²/8), V=Σck².
V označení úlohy c=V/2 je to exp(cλ²/4), jak zadání žádá.

Tištěná odpověď místo jednotlivých exp(ck²λ²/8) používá
exp(ck²λ²/4), ale součin pak chybně označí za exp(cλ²/4).
To je samostatný lokální nález F161. Přesný dvouatomový příklad
a oprava pouze individuálních jmenovatelů jsou v jeho poznámce.

Po této opravě je také původní metoda rozvinutím součinu platná.
Faktory exp(ck²λ²/8)+Yk hk jsou kladné, protože shora omezují
e^{λYk}>0. Lze je tedy násobit. V každém nekonstantním členu
rozvoje vezmeme největší použitý index j; všechny ostatní faktory
jsou funkcemi minulosti před Yj a E(Yj hj|minulost)=0. Člen tedy
vymizí. To platí i pro předvídatelná hj při pevných ck, protože
žádné budoucí náhodné exponenciální koeficienty nezůstávají.

**MPR90(f) a (37),(38).** Pro x>0,V>0 minimalizujeme
Vλ²/8−xλ. Doplnění čtverce nebo derivace dává λ=4x/V=2x/c,
a hodnotu −2x²/V=−x²/c. Přesně tím vzniká (37). Při x=0
jednostranná mez1 platí přímo; při V=0 jsou všechny přírůstky0
a kladný ocas má pravděpodobnost0. Záporný práh není doména
této optimalizované horní odchylky a nedosazuje se do ní.

Posloupnost −Y je opět férová a její intervaly [−bk,−ak] mají
stejné šířky. To dává druhý jednostranný ocas. Pro x>0 jsou
události S≥x a S≤−x disjunktní, takže součet jejich mezí dává
(38); unijní mez by stačila i bez disjunktnosti. Faktor2 je proto
odůvodněný. Je-li výsledná mez větší než1, zůstává platnou mezí.

**F160, co selže při libovolných náhodných šířkách.** Přesný
tříatomový příklad v `notes/F160-predictable-azuma-widths.md` má
všechny intervaly s kladnou šířkou a všechny kladné atomy. Je férový,
ale P(S2≥1)=4/5, zatímco bodová mez na jednom vlákně je exp(−8/17).
Dokonce průměr dvou tištěných exponenciál je menší než
11106/14167<4/5. Nelze proto libovolná předvídatelná ak,bk vložit
do (37), jak tvrdí věta za(38). Potřebná deterministická konstanta
chybí i při nejpřirozenějším pokusu zprůměrovat pravou stranu.

Správné rozšíření používá kompenzovaný nezáporný supermartingale

```
Mj=exp(λSj − λ²Σk≤j(bk−ak)²/8), M0=1.
```

Podmíněná verze(d) dává E(Mj|Hj−1)≤Mj−1, tedy EMn≤1.
Je-li Σ(bk−ak)²≤v pro pevné v>0, na události Sn≥x je
Mn≥exp(λx−λ²v/8). Markov a λ=4x/v dávají požadovaný odhad.
Stejný důkaz dává obecně P(Sn≥x,Σšířek²≤v)≤exp(−2x²/v).
Tím je doložena oprava a přesně odděleno, co z hlavního textu
zůstává pravdivé. Následující aplikace mají pevné ck a jsou platné.

**(39) a celá MPR91: Doobova konstrukce.** Pro integrabilní Q
definujme Zn=E(Q|Hn), Hn=(X0,…,Xn). Je funkcí Hn. Bodová
trojúhelníková nerovnost v každém podmíněném součtu dává
|Zn|≤E(|Q||Hn), a tedy E|Zn|≤E|Q|<∞. Věžová identita z D098
dává

```
E(Zn+1|Hn)=E(E(Q|Hn+1)|Hn)=E(Q|Hn)=Zn.
```

To je přesně výpočet odpovědi91. Odkaz na (*) v odpovědi35 byl
porovnán s původní sazbou na376: E(E(X|Y,Z)|Z)=E(X|Z), který
je totožnou podmíněnou věžovou identitou. MPR77 dovoluje přechod
na vlastní historii Z. Nezávislost X není nikde použita; podstatná
je rostoucí informace a integrabilita Q. Celé zadání a odpověď91
jsou tím doloženy, celá úloha35 se tím nepřebírá.

## D101 — str.10, všechny mezikroky hašovacího příkladu

**Pravděpodobnostní model a krajní Zn.** Pro m≥1,t≥1 je
prostor všech m^t sekvencí adres rovnoměrný. Každé Xn je proto
rovnoměrné na1,…,m a souřadnice jsou nezávislé: pravděpodobnost
libovolné úplné sekvence je součin t faktorů1/m. Po fixaci prefixu
délky n zůstává přesně m^{t−n} stejně pravděpodobných suffixů.
Q je počet prázdných seznamů, tedy0≤Q≤m a je integrabilní.
Z0 je E Q a Zt=Q, protože po všech t adresách je Q určeno.
Při t=0 je Q=m deterministické; koncentrační vzorec s dělením t
se v tomto triviálním případě nepoužívá.

**(40), každý průměr a role nezávislosti.** Pro pevný prefix
u=(x1,…,xn−1) a suffix v=(xn+1,…,xt) označme q_v(z)=Q(u,z,v).
Pak

```
Zn(u,z)   = average_v q_v(z),
Zn−1(u)   = average_v Σz′ p_n(z′) q_v(z′),
Yn(u,z)   = average_v [q_v(z)−Σz′ p_n(z′)q_v(z′)].
```

V rovnoměrném modelu p_n(z′)=1/m. Protože Σp_n=1, výraz
v hranaté závorce je přesně tištěné Δ v(40), včetně správného
indexu nahrazované souřadnice a všech vah. Průměr má m^{t−n}
členů; pro n=t je to jediný prázdný suffix, pro n=1 prázdný
prefix. Váhy suffixu nezávisí na z ani na prefixu právě díky
nezávislosti. Férovost Yn vůči historii X plyne buď z tohoto
průměru přímo, nebo z již dokázané Doobovy konstrukce.

**(41), všechny možné změny obsazenosti.** Přesunutí jednoho
objektu z adresy i na j při i=j nezmění nic. Pro i≠j může
vyprázdnit původní seznam právě tehdy, pokud v něm byl jediný
objekt; může zaplnit dosud prázdný cílový seznam právě tehdy,
pokud byl prázdný. Změna Q je tedy

```
[old count at i = 1] − [old count at j = 0] ∈ {−1,0,1}.
```

Tím jsou pokryty všechny čtyři dvojice indikátorů, včetně případu,
kdy obě změny nastanou a navzájem se zruší. Žádná změna druhého
seznamu nemůže dát absolutní rozdíl2. To dokazuje(41).

**(42) a potřebná mez po průměrování.** Pro pevné u,v je
Δ(u,z,v)=q_v(z)−μ_v, kde μ_v=Σp_n(z′)q_v(z′) nezávisí na z.
Rozdíl dvou Δ je tedy q_v(z)−q_v(z′); podle(41) je nejvýše1.
Maximální a minimální Δ proto splňují přesně(42).

Ještě je třeba skutečně přejít od Δ k Yn, nikoli bez důkazu
zaměnit max a průměr. Pro libovolná z,z′ použijeme stejné suffixy:

```
fn(u,z)−fn(u,z′)
 = average_v (q_v(z)−q_v(z′)) ≤ 1.
```

Podmíněný rozsah Yn na dané historii má tedy šířku nejvýše1.
Jeho střed či endpoints mohou záviset na u, ale horní mez šířky1
je pevná. Přesně opravená podoba Azumy z D100 proto platí vůči
historii X a dává V=t. Není nutné, aby min/max byly funkcemi
už ztrátové vlastní historie přírůstků; důkaz funguje přímo pro
adaptovanou původní informaci, která jejich férovost zajišťuje.

**(43), přesné E Q a (44).** Teleskopicky Zt−Z0=ΣYn, takže
všechny rovnosti a nerovnost(43) mají právě získaný exponent
−2x²/t, pro x>0. Pro pevný seznam k jej vynechává (m−1)^t
sekvencí, tedy P(k prázdný)=((m−1)/m)^t. Linearita očekávání
indikátorů dává

```
E Q = m(m−1)^t/m^t = (m−1)^t/m^{t−1}.
```

Nevyžaduje nezávislost událostí prázdnosti různých seznamů.
Při m=1,t≥1 dává0 a Q je skutečně0; při t=1 dává m−1,
rovněž deterministickou hodnotu.

Dosazení x=sqrt(t ln f(t)) je reálné pro f(t)≥1. Pro f(t)>1
je práh kladný a exp(−2x²/t)=exp(−2 ln f(t))=1/f(t)².
To dává každý člen(44), včetně přesného přepisu Z0. Pro f(t)=1
je mez1 triviální. Spodní ocas má stejnou mez podle již ověřeného
argumentu s −Y. Žádná nezadaná asymptotika funkce f není nutná
pro samotné(44); pozdější a.s./q.s. výklady jsou další strana.

**(45), obecné omezené rozdíly.** Nechť nezávislé Xn mají libovolné
diskrétní rozdělení p_n; nemusí být stejné. Je-li změna souřadnice n
omezena pevným cn≥0, pak funkce

```
gn(u,z)=E_v Q(u,z,v)
```

má pro každá z,z′ rozdíl v absolutní hodnotě≤cn. Váhy v tomto
průměru jsou stejné pro obě z díky nezávislosti a sčítají se na1.
Přírůstek je gn(u,Xn)−Σz p_n(z)gn(u,z), takže odečtení společné
konstanty nezmění šířku. Má podmíněný rozsah≤cn a podmíněnou
střední hodnotu0. D100 dává přesně exp(−2x²/Σcn²), jak tvrdí
text. Pokud některé cn=0, přírůstek je0. Při všech cn=0 je Q
na produktu podpor konstantní a kladný odchylkový ocas je0.
Při konečných cn a konečném t je celková oscilace Q nejvýšeΣcn
postupnou výměnou souřadnic, takže existenci očekávání lze navíc
odvodit přímo z těchto předpokladů.

Definice zde kontrolované Lipschitzovy podmínky je tedy přesně
omezení po jednotlivých souřadnicích, nikoli metrický odhad ve
zcela jiné normě. Poslední dvě řádky str.10 jen zavádějí model
dalšího příkladu s celočíselnými velikostmi1≤Xn≤m; jeho tvrzení
o bin packing pokračují na11 a zatím se neuzavírají.

## Přesný rozsah a výjimky

- File29: každé matematické tvrzení posouzeno; F160 je oprava
  příliš obecné věty o předvídatelných mezích. Ostatní odhady mají
  úplný důkaz s výslovnými doménami normalizace.
- File30: každý matematický mezikrok(40)–(45), každý okraj a
  každá podmíněná šířka doloženy. Hlavní aplikace zůstávají správné.
- MPR86 a91: celá zadání i celé odpovědi reviewed.
- MPR90: všech šest částí a odpovídajících odpovědí reviewed s
  lokální opravou F161; základní věta platí pro pevné šířky a
  správné rozšíření je dokázáno zvlášť. MPR35 nepřebíráme celé.
- Bibliograficky vynechány Kolmogorov1928, Hoeffding1963,
  Azuma1967, Doob1953/1940, Lipschitz1864 a McDiarmid1989.
  Matematický obsah použitý z těchto tvrzení je odvozen zde;
  samotná historie/atribuce není označena jako ověřená.
- Dva přesné drobné svědky byly zkontrolovány s racionální
  aritmetikou nice15. Žádné staré testy ani dlouhé výpočty,
  censusy či přerušené úlohy se nespouštěly.
