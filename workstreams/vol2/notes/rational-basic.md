# §4.5.1: přesné zlomky, úlohy 1–9 a 11

Audit 2. listopadu 2026; původní strany 330–333,638–640 přečteny
v sazbě. Základní algoritmy jsou správné. Výjimka N=2 v odpovědi 7
je confirmed C0113; formulace o nezměněné rutině při dělení nulou
je oddělený interpretační candidate C0114. Slash formáty a další
úlohy mají navazující bloky, touto poznámkou se celá sekce neuzavírá.

## Kanonický zápis a čtyři operace

Zlomek reprezentujeme dvojicí (u,a), kde a>0 a gcd(u,a)=1.
Funkce gcd je nezáporný největší společný dělitel. U nuly z toho
plyne a=1. Rovnost u/a=v/b dává ub=va. Nesoudělnost u,a znamená
a|b a obdobně b|a; kladnost tedy a=b a potom u=v. Zápis je jednoznačný.
U nenulové dvojice čísel (r,s) a d=gcd(r,s)>0 platí
gcd(r/d,s/d)=1: společný dělitel c>1 by dal společný dělitel cd>d.
V aplikaci úlohy 2 není dvojice (0,0), protože jmenovatele jsou kladné.

**Porovnání 1.** Vynásobení kladným ab zachovává pořadí, takže stačí
ub<va. Součiny mohou vyžadovat dvojnásobnou přesnost. Doplněk errata
15. ledna 2002 odkazuje na §4.5.3-39, která nabízí porovnání pomocí
řetězových zlomků; správnost základního porovnání se nemění.

**Násobení 3.** Platí

```text
gcd(uv,ab) = gcd(u,b)*gcd(a,v),                       (1)
```

jestliže gcd(u,a)=gcd(v,b)=1. Pro každé prvočíslo nemohou mít
kladný exponent současně u,a ani v,b. Společná mocnina ve dvou
součinech tedy může vzniknout jen křížem u,b nebo a,v; tyto dva
případy se navzájem vylučují. To dokazuje (1) i přesné exponenty.
Nulový čitatel se ověří zvlášť: je-li u=0, pak a=1 a obě strany
jsou b. Totéž platí při v=0.

Označíme-li d=gcd(u,b),e=gcd(a,v), výsledkem je
((u/d)(v/e),(a/e)(b/d)). Všechny podíly jsou celé a jmenovatel
kladný; (1) dokazuje redukovanost. Před posledními dvěma součiny
se velikosti pouze zmenšují. Žádný větší součin tedy nevzniká,
pokud se obě složky výsledku vejdou do původního slova.
Poznámka o rychlosti dvou gcd je kvalitativní porovnání podobně
velkých vstupů, nikoli rovnost počtu iterací pro každou konkrétní dvojici.

**Dělení 4.** Pro v!=0 nejprve d=gcd(u,v),e=gcd(a,b), potom

```text
w = (u/d)*(b/e)*sign(v),      c = abs((a/e)*(v/d)).
```

Zde sign(v)=1 pro v>0 a -1 pro v<0; hodnotu v=0 řeší samostatná
chyba před těmito výpočty. Jde o násobení převráceným zlomkem
a převod znaménka do čitatele. Výstupní jmenovatel je kladný.

**Sčítání, odčítání a 6.** Nechť g=gcd(a,b), A=a/g,B=b/g a
t=uB+s*vA, kde s=1 pro součet a -1 pro rozdíl. Máme gcd(A,B)=1.
Každé prvočíslo dělící A nedělí ani u, ani B, a proto nedělí t;
obdobně pro B. Tedy gcd(t,AB)=1, odkud

```text
gcd(ub+s*va,ab) = g*gcd(t,g),
výsledek = (t/h, A*(b/h)),   h=gcd(t,g).              (2)
```

To je tištěný vzorec. Platí i při t=0: tehdy předchozí nesoudělnost
vynutí A=B=1, takže h=g a výsledek je (0,1). V případě g=1 není
další krácení nutné. Identita gcd(t,g)=gcd(t mod g,g) umožňuje
počítat poslední gcd na malých číslech, přestože t může být velké.
Časový přínos není tvrzení, že se do jednoho slova vejde i příliš
velký výsledný jmenovatel; text dále požaduje kontroly přetečení.
Hodnota přibližně 61 % odkazuje na asymptotický model nezávislých
rovnoměrných kladných jmenovatelů, nikoli na libovolná aplikační data.
Příslušná věta bude samostatně prověřena v §4.5.2.

Příklad textu: g=6,t=201,h=3 dává 67/44. Úloha 5: g=10,t=-205,h=5
dává -41/168. Všechny mezikroky v sazbě souhlasí.

## 7: ostrá mez pro mezivýsledek t

Nechť N>=2 je celé a X=N-1. Čitatele mají absolutní hodnotu
nejvýše X, jmenovatele jsou mezi 1 a X. Z trojúhelníkové nerovnosti
stačí maximalizovat |u|b+|v|a, děleno g=gcd(a,b).

Pokud g>=2, je |t|<=2X²/g<=X². Při g=1 a X>=2 rozlišíme dvě
možnosti. Je-li jeden součin X², například |u|b=X², jsou |u|=b=X.
Nesoudělnost vstupních zlomků nutí a<=X-1 a |v|<=X-1, takže druhý
součin je nejvýše (X-1)². Není-li ani jeden součin X², každý je
nejvýše X(X-1), a jejich součet je menší než X²+(X-1)².
Proto pro N>=3

```text
max |t| = (N-1)^2+(N-2)^2.
```

Mez se nabývá na u/a=(N-1)/(N-2),v/b=(N-2)/(N-1), protože
sousední celá čísla jsou nesoudělná. Při N=2 však existují jen
zlomky -1/1,0/1,1/1. Vstupy 1/1 a 1/1 dávají t=2, kdežto tištěná
formule dává 1. Oprava je výjimka N=2 nebo předpoklad N>=3;
viz [C0113](C0113-rational-small-bound.md). Pro N=2^n,n>=3 je
maximum opravdu mezi 2^(2n) a2^(2n+1), takže může potřebovat
2n+1 bitů velikosti. Tato část odpovědi není chybná.

## 8: nekonečna, neurčená hodnota a přetečení

Rozšíříme dvojice o +inf=(1,0),-inf=(-1,0) a neurčenou hodnotu
U=(0,0). U propagujeme každou aritmetickou operací. Pro konečné
nenulové x jsou platná tištěná pravidla násobení a dělení s nekonečny;
součin0*inf,inf/inf,0/0 a součet opačných nekonečen vracejí U.
Při dělení konečného nenulového x kanonickou nulou0/1 volíme
sign(x)*inf. Podepsané nuly tento formát neobsahuje. Sčítání
a odčítání nekonečen se větví podle jejich znamének.

Implementace `extended_op` provede toto rozlišení před konečnými
rutinami. Její výstup je pro konečné operandy původní přesný vzorec;
pro zvláštní hodnoty konečná tabulka. Ověřeno 144 kombinací operací
na šesti zástupcích, včetně U a obou nekonečen, proti nezávislé
aritmetice rozšířených reálných hodnot a explicitní konvenci x/0.

Doslovné „without change to the algorithms described“ v odpovědi 8
je přinejmenším nutné kvalifikovat: odpověď 4 výslovně vyžaduje
chybové hlášení při v=0. Původní konečná rutina proto na 1/0 vrátí
chybu, zatímco její rozšířená verze +inf. Navíc sign(v) v konečném
vzorci není definováno pro tento případ. **C0114 zůstává candidate**,
protože autor mohl mít na mysli pouze aritmetické jádro při přirozené
úpravě výjimek; samotná zamýšlená rozšířená pravidla jsou konzistentní.

Použije-li se U pro přetečení paměťově omezené přesné aritmetiky,
nesmí být přetečení zaměněno za skutečné nekonečno: jinak 1/overflow
vrátí falešně přesnou nulu. Propagace U je konzervativní. Neznamená,
že matematická hodnota celé původní formule neexistuje nebo je velká;
mezivýsledek může přetéct před pozdějším zkrácením. Text chápeme
jako určení spolehlivých výsledků provedeného výpočtu.

## 9: odlišení zlomků počátečními binárními místy

Pro rozdílné u/a,v/b s 1<=a,b<2^n je ub-va nenulové celé číslo.
Tedy |u/a-v/b|>=1/(ab)>2^(-2n), a po násobení2^(2n) je rozdíl
větší než1. Dvě reálná čísla se stejnou podlahou mají rozdíl menší
než1. To dokazuje tvrzení bez požadavku na znaménko, velikost
čitatelů nebo redukovanost. Příklad 1/13 a1/14 má při n=4 stejnou
podlahu po násobení 128, totiž 9, takže obecně nestačí 2n-1 míst.
Ověřeno 87372 vstupů pro n=1,...,8 a čitatele mezi -a a a; počet
kontrol konečné mřížky nepředstírá celý neomezený obor čitatelů.

## 11 a další číselná tělesa

Číslo (a+b*sqrt(5))/c má celé koeficienty,gcd(a,b,c)=1,c>0.
Nenulové a+b*sqrt(5) má a²-5b²!=0: rovnost by z lichého exponentu
prvočísla 5 udělala sudý, pokud by b nebylo 0; pak musí být také a=0.
Převrácená hodnota je c*(a-b*sqrt(5))/(a²-5b²). Po vynásobení
čitatelem druhého zlomku, změně znaménka záporného jmenovatele
a vydělení gcd tří koeficientů dostaneme opět kanonický tvar.
Jeho jednoznačnost plyne z iracionality sqrt(5), a tedy z nezávislosti
1,sqrt(5) nad racionálními čísly. Nulové číslo má trojici (0,0,1).
Příklad 1/(1+sqrt(5))=(-1+sqrt(5))/4 souhlasí.

Také kubický příklad textu je správný. Pro alpha=cuberoot(2)
platí alpha³=2 a polynom X³-2 nemá racionální kořen, takže je
nerozložitelný nad racionálními čísly. Báze je 1,alpha,alpha².
Pro z=a+b*alpha+c*alpha² je

```text
z * [(a²-2bc)+(2c²-ab)*alpha+(b²-ac)*alpha²]
  = a³+2b³+4c³-6abc.
```

Matice násobení prvkem z v uvedené bázi je
[[a,2c,2b],[b,a,2c],[c,b,a]]; přímý rozvoj jejího determinantu
dává pravou stranu. Pro z!=0 je násobení v tělese invertibilní,
a proto je tento determinant nenulový.
Vzorec tedy dává celočíselné koeficienty převrácené hodnoty se
společným jmenovatelem; následuje stejné krácení. Nenaznačujeme,
že obecně postačuje běžný gcd pouze dvou čísel pro všechny koeficienty.

## Kontroly a stav

`verify_rational_basic.py`, `results/rational-basic.json` a `.log`:
91809 úplných malých dvojic, 1000 dvojic až 512bitových operandů,
77764 dvojic pro ostrá maxima N=2,...,16,87372 binárních identifikací,
4000 dělení v Q(sqrt(5)) a 144 případů rozšířených operací.
Každá konečná operace se porovnává s nezávislým Fraction orákulem;
kvadratické dělení navíc s koeficientovou aritmetikou a zpětným součinem.
Relace 52548 exit 0; následně doplněn pouze checkpoint extended,
spuštěn --resume s přeskočením všech čtyř předchozích bloků, exit 0.

Čtyři vrstvy errat prohledány podle 330–333,638–640, vzorců i klíčových
slov. Doplněk odkazu u 1 je zahrnut; oprava malé meze 7 ani upřesnění
formulace 8 nebyly nalezeny. Poslední fyzický dotisk a priorita
neověřeny, nic neodesláno. Úlohy 10, 12–16, slash text a historický
kontext zůstávají pro navazující bloky.
