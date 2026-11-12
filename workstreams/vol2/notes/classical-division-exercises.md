# §4.3.1: matematika úloh17–30

Blok navazuje na [dřívější důkaz D](division.md) a
[instrukční program](classical-division-mix.md). Všechny původní úlohy282–283
a odpovědi625–627 byly vizuálně přečteny. Základ b je celé číslo alespoň2,
v je n-místný dělitel s `n>=2` a nejvyšší číslicí `a=v_(n-1)>0`.
Lokální dělenec `0<=u<bv` má n+1 číslic. Označme

```
q=floor(u/v), R=u-qv,
a=v_(n-1), c=v_(n-2), T=u_n b+u_(n-1), z=u_(n-2),
h=zkoušený celočíselný odhad q, rh=T-ha, A=ab+c.
```

R je pravý zbytek; rh je pomocný zbytek z odhadu, může být záporný.
Odhad h nazveme horním, pokud h>=q. Tato podmínka je pro20/21 podstatná.

## 17 a18: jednostranné odhady

Pokud `u_n=a>=floor(b/2)`, pak
`u/v > a b/(a+1) = b-b/(a+1) > b-2`, protože `a+1>b/2`.
Z u/v<b plyne q v {b-2,b-1}. To zahrnuje liché základy.

Dolní odhad18 je `floor(T/(a+1))`. Protože
`T b^(n-1)<=u` a `v<(a+1)b^(n-1)`, je `T/(a+1)<=u/v`.
Podlahy zachovávají pořadí. Pro u=0 obě strany rovny0; ostré mezikroky
v tištěné odpovědi je třeba v tomto triviálním případě číst neostře.

## 19–21: druhá číslice dělitele a rozsah h

Test `h c> b rh+z` je ekvivalentní `h A>Tb+z`. Pro celočíselné h tedy
`h A>=Tb+z+1`. Z `u<(Tb+z+1)b^(n-2)` a `v>=A b^(n-2)` plyne
`u<hv`, a proto q<h. Pokud by h bylo záporné, antecedent testu ani
nemůže platit. Tím je úloha19 obecně dokázána.

Obrácená nerovnost říká `h<=floor((Tb+z)/A)`. Tento dvojčíselný horní
odhad Q2 splňuje `q<=Q2<=q+1`; obecný důkaz je již v division.md a
nepotřebuje normalizované a. Proto test dává pouze **q>=h-1**.
Abychom dostali q=h nebo h-1, potřebujeme navíc **q<=h**. Algoritmus D
tento invariant zaručuje od prvního odhadu a zachovává jej při každém
snížení. Pro obecnou „aproximaci“ zavedenou v úloze19 to automatické není.
Erratum3.2.2005 přidává h<b, ale dolní odhad tím nevylučuje.

Doslovný protipříklad k20 a21: b10,n2,u100,v50,h1. Pak q2,R0,
a5,c0,T10,z0,rh5. Platí h<b a `h c=0<=50=b rh+z`, ale q není1 ani0.
Také a>=b/2 a h!=q, avšak `R=0<(1-2/b)v=40`. Záměr úloh v kontextu
D je zřejmý; zda je převzetí horního odhadu dostatečně implicitní, ponecháváme
jako [interpretační kandidát C0098](C0098-division-upper-estimate.md).
Nejde o protipříklad k samotnému D.

Za správného invariantního předpokladu je21 snadná. Je-li h!=q, pak
h=q+1. Z testu plyne `h A b^(n-2)<=u`. Napišme
`v=A b^(n-2)+t`, kde `0<=t<b^(n-2)`. Potom

```
0 < hv-u <= h t < (b-1)b^(n-2),
R = v-(hv-u) > v-(b-1)b^(n-2)
  >= (1-(b-1)/(ab))v >= (1-2/b)v,
```

protože `a>=floor(b/2)>=(b-1)/2`. Formulace neostrou mezí tedy platí.
Pravděpodobnost přibližně2/b se v textu týká **nutné události** o velkém
zbytku, pokud je zbytek přibližně rovnoměrný. Nedokazuje, že samotná oprava
D6 má pro libovolná vstupní data pravděpodobnost přesně2/b.

## 22–24: příklady, normalizace a její četnost

Příklad4100/588: první odhad8 se změní druhým testem na7, ale7*588=4116,
tedy D6 musí snížit podíl na6; zbytek572. Přidaný příklad z errat2003
má b=2^16,U=(7fff800100000000)_16,V=(800080020005)_16. Byl ověřen
celým algoritmem D a nezávislým divmod; skutečně vyvolá D6. Čísla a
čítače obou běhů jsou v JSON. Nejde o opakování dřívějšího plošného censu.

Opravená úloha23 používá `d=floor(b/(a+1))`. Platí
`a d < (a+1)d <= b` a `a d>=floor(b/2)`. Poslední nerovnost má obecný
důkaz už v division.md. Tištěný náhradní důkaz1998 je také správný:
pro a<b/2 podlaha d>= (b-a)/(a+1), protože zbytek po dělení je nejvýše a;

```
a(b-a)/(a+1) >= (b-1)/2,
```

což je ekvivalentní `(a-1)(b-2a-1)>=0`. Oba faktory jsou nezáporné.
Pro a>=b/2 je d=1 a mez bezprostřední.

Pro24 použijeme Benfordův model vedoucí číslice: její pravděpodobnost
při hodnotě a je `log_b((a+1)/a)`. U opraveného normalizátoru je d=1
právě pro `a>=floor(b/2)`. Součet teleskopuje na
`log_b(b/floor(b/2))`. Pro sudé b jde přesně o tištěné log_b2; pro liché b
jde o jeho aproximaci s rozdílem řádu1/(b log b). Pro b=2^32 vychází1/32.
Je to důsledek zvoleného modelu vstupů, nikoli univerzální zákon pro všechna
čísla generovaná programem.

## 25–27 a29

D1/D8 v MIX, přetečení i časové konstanty jsou plně doloženy v
[classical-division-mix.md](classical-division-mix.md). Pro27 je normalizovaný
zbytek `d(U mod V)`, přesně násobek d. Pro29 platí na začátku D7
`(u_(j+n)...u_j)_b < v < b^n`, takže u_(j+n)=0. Tvrzení se týká původního
D; při úpravě30, která na stejnou adresu již uložila podíl, zůstává platný
matematický zbytek, nikoli původní význam přepsané adresy.

## 28: Svobodova normalizace, obecný důkaz tří iterací

Po vydělení v číslem b^n můžeme pracovat s racionálním x, jehož původní
hodnota je v intervalu[1/b,1). Označme a=floor(bx), tedy jeho první
číslici za čárkou. N1 v případě a<b/2 násobí x číslem
`floor((b+1)/(a+1))`. Horní mez výsledku je1+1/b. Pro dolní mez použijeme

```
f(a)=a(b+1-a)/(b(a+1)).
```

Tato funkce má druhou derivaci `-2(b+2)/(b(a+1)^3)<0`, je tedy konkávní
(známá oprava „convex“ na „concave“ z25.2.1998). Na intervalu[1,b/2]
jsou obě krajní hodnoty1/2, takže f>=1/2. Pokud se N1 neprovádí, x>=1/2
už platí. Po N1 tudíž `1/2<=x<1+1/b`.

Jestliže x<1, krok N2 lze psát

```
x <- x * floor(b(b+1)/(a+1))/b.
```

To je přesně přepis `x + floor(b(b-a)/(a+1))*x/b`, nikoli aproximace.
Horní mez1+1/b zůstává zachována. S `a>=floor(b/2)>=(b-1)/2` dostáváme
po první iteraci dolní mez

```
g(a)=a(b(b+1)-a)/(b^2(a+1)).
```

Také g je konkávní: druhá derivace je
`-2(b^2+b+1)/(b^2(a+1)^3)`. Na intervalu[(b-1)/2,b-1] stačí zkontrolovat
konce. Jejich rozdíly od `1-3/(2b)` jsou postupně

```
(3b-1)/(2b^2(b+1)),  (b^2+2b-2)/(2b^3),
```

oba kladné. To dává jednoduchý obecný důkaz i pro liché b; není třeba
předpokládat a>=b/2 při minimalizaci mezikroku, jak naznačuje tištěný
výběr t=b/2+1. Platný výsledný odhad z knihy je zachován.

Každá další provedená iterace násobí x alespoň1+1/b. Pro b>=5

```
(1-3/(2b))(1+1/b)^2 -1 = (b^2-4b-3)/(2b^3) >0.
```

Po nejvýše třech iteracích je proto x>=1. Pro b2 je při x<1 faktor3/2,
a dvě iterace stačí; pro b3 je faktor2 při a1 a4/3 při a2, rovněž stačí
dvě. Pro b4 je faktor3/2 při a2 a5/4 při a3; nejhorší posloupnost dolních
mezí je1/2,3/4,15/16,75/64, tedy nejvýše tři iterace. Protože celou dobu
x<1+1/b, konečné první dvě číslice jsou1 a0, jak požaduje úloha.

Násobení původního dělence stejnými racionálními faktory zachovává podíl.
Dělitel s prvními číslicemi10 dovoluje přímý vedoucí odhad popsaný v poznámce
zadání; výjimka vedoucí dvojice dělence10 opět vyžaduje omezení na b-1.
Samostatná priorita a celý původní Svobodův článek patří historickému
kontextu, nikoli tomuto algebraickému důkazu.

## 30: překryvy paměti

A a S mohou ukládat výsledek přímo přes jeden ze vstupů, pokud oba
vstupní údaje a starý přenos načtou před zápisem w_j. Proto úprava A2
s dočasným t v odpovědi dává smysl; instrukční A/S to už dělají.
Dosud nepřečtené vyšší pozice se nepoškodí. To bylo navíc ověřeno pro
W=U i W=V v obou programech.

U M je bezpečné umístit `v_j` na `w_(j+m)`: M1 nuluje pouze pozice<m;
při iteraci j se zapisují pozice j,...,j+m-1 a nakonec j+m, teprve když
byla dokončena všechna čtení v_j. Budoucí v_(j+1),... zůstávají nedotčené.
Tištěné `w_(j+n)` funguje například při m=n nebo obecně m<=n, ale nikoli
pro obecné délky. Pro m2,n1,U=(10)_b,V=1 inicializace smaže v_0 a výsledek
je0 místo b. [C0097](C0097-multiplication-alias.md) opravuje tento index.
Překrytí podílu v D je doloženo v instrukční poznámce včetně nutné úpravy D6.

## Rozsah kontrol

[verify_classical_division_exercises.py](../verify_classical_division_exercises.py)
a [JSON](../results/classical-division-exercises.json) doplňují obecné důkazy
30000 novými lokálními případy,216195 úplnými vstupy Svobodova postupu
pro b2–30,n1–3 a2000 dalšími většími vstupy, pěti symbolickými identitami
a1920 přímými běhy aliasů A/S. Všechny tři checkpointy prošly. Úspěšné starší kontroly
normalizace a algoritmu D se neopakovaly. Konkrétní počty jsou v JSON;
hlavní matematické závěry nezávisí na úplnosti konečného vzorku.

Relevantní errata všech čtyř vrstev prohledána podle stránek i obsahu;
originály all2-prepre17/37/38 a all2-pre14 přečteny. Opravy20/23/25/26/28
jsou započteny. Pro index odpovědi30 ani doplnění h>=q nebyla nalezena
položka. Poslední fyzický dotisk a priority nálezů neověřeny.
