# §1.2.8-35: zápis v bázi zlatého řezu

Audit 1. listopadu 2026; zadání s. 86, odpověď s. 495
a opravy 1997 zobrazeny. Píšeme phi=(1+sqrt(5))/2,
psi=−1/phi. Zápis je součet sum_(j<=K)d_j phi^j,
kde d_j je 0 nebo 1 a největší index K je konečný.
Nuly vlevo nepovažujeme za změnu zápisu. Kanonický
zápis nemá sousední jedničky ani konečný začátek
následovaný nekonečným střídáním 010101... .

## Existence a jednoznačnost pro reálná čísla

Pro x>0 vybereme největší k s phi^k<=x. Pak
x−phi^k<phi^(k−1), takže další jednička může být
nejvýše v pozici k−2. Opakováním dostáváme konečný
nebo nekonečný zápis; zbývající hodnota jde k nule,
protože použité exponenty klesají k minus nekonečnu.
Nekonečný střídavý konec by měl hodnotu přesně
následující vyšší mocniny a porušil by největší
možnou hladovou volbu. Pro x=0 jsou všechny cifry 0.

Při dvou různých zápisech vezměme nejvyšší odlišnou
cifru k. Zápis s 0 na této pozici ji může dohnat
nižším ocasem nejvýše
phi^(k−1)+phi^(k−3)+...=phi^k. Rovnost by vyžadovala
právě zakázaný nekonečný střídavý konec. Každý další
kladný ocas v druhém zápisu rozdíl jen zvětší.
Tím je jednoznačnost dokázána i pro nekonečné zápisy.

Bez omezení existuje nekonečně mnoho zápisů 1:
phi^(−1)+phi^(−2)=1 a poslední mocninu lze stále
nahrazovat dvěma následujícími menšími mocninami.
Také sum_(j>=2)phi^(−j)=1 dává uvedené .011111... .

## Konečné zápisy všech nezáporných celých čísel

Lucasova čísla jsou L_j=phi^j+psi^j=F_(j+1)+F_(j−1).
Následující knižní pravidla po opravě 1997 jsou správná:

```text
L_(2n)+m = phi^(2n)+phi^(−2n)+m,
  0<=m<=L_(2n−1), n>=1;                              (P1)

L_(2n+1)+m = phi^(2n+1)+phi^(−2n−2)+(m−phi^(−2n)),
  0<m<L_(2n), n>=0.                                  (P2)
```

V (P1) i (P2) se místo poslední závorky dosadí její
kanonický zápis. Je nutné dokázat, že se cifry
nepřekryjí a postup skončí, nejen algebraickou rovnost.

Použijeme indukci po intervalech. Výchozí 0,1 mají
prázdný zápis a phi^0. Intervaly
[L_(2n),L_(2n+1)] a (L_(2n+1),L_(2n+2)) společně
pokrývají další celá čísla; první oddý interval n=0
obsahuje pouze 2=phi+phi^(−2), které ověříme přímo.
Pro následující intervaly n>=1 je indukční invariant:

- každé již reprezentované kladné celé číslo má
  konečný zápis s nejmenším exponentem sudým a <=0;
- pro M<=L_(2n−1) leží všechny jeho exponenty
  v [−2n+2,2n−2];
- pro M<L_(2n) leží v [−2n,2n−1].

Při (P1) první rozsah odděluje nový pár exponentů
±2n alespoň jednou nulou od zbytku. Výsledný rozsah
je [−2n,2n] a nejnižší exponent je sudý.
Při (P2) vezmeme nejnižší exponent j v zápisu m.
Je sudý, −2n<=j<=0. Odečtení phi^(−2n) nahradí
jeho poslední člen podle přesné identity

```text
phi^j−phi^(−2n)=phi^(j−1)+phi^(j−3)+...+phi^(−2n+1),   (P3)
```

přičemž při j=−2n je pravá strana prázdná. Ostatní
cifry byly nejméně v j+2, takže sousední jedničky
nevzniknou. Upravený zbytek má exponenty v
[−2n+1,2n−1]. Od nových členů 2n+1 a −2n−2 je
opět oddělen nulou; nový nejnižší exponent je sudý.
To dává potřebné rozsahy pro následující interval.
Indukce dokazuje současně konečnost, nezápornost,
kanonicitu a platnost obou rekurzivních pravidel.

V původní odpovědi bylo chybně m−phi^(2n) a v (P3)
chyběl druhý exponent j−3. Obě věci autor opravil
16. listopadu 1997; nejde o nové nálezy.

## Které řetězce mohou být před řádovou tečkou

Vezměme konečný řetězec a začínající 1, bez sousedních
jedniček. Jeho hodnota před tečkou je
A=sum_(j>=0)d_j phi^j. Přípustné ocasy zaplňují
interval [0,c), kde c=1 při d_0=0 a c=phi^(−1)
při d_0=1. To plyne z hladového důkazu výše; při
poslední cifře 1 musí být následující cifra 0.
Koncová hodnota c se nezahrnuje kvůli střídavému konci.
Interval [A,A+c) obsahuje nejvýše jedno celé číslo.
Při d_0=0 obsahuje vždy právě ceil(A).

Při d_0=1 je řetězec „1“ sám realizován číslem 1.
Jinak nechť j>=2 je nejnižší další jednička a
S=sum_(h>=1)d_h psi^h. Protože phi^h=L_h−psi^h,
je A celé číslo minus S, a tedy ceil(A)−A=S mod 1.
Máme −phi^(−2)<S<phi^(−1). Znaménko S určuje
nejnižší exponent j: opačné pozdější členy mají
součet absolutních hodnot nejvýše
phi^(−j−3)/(1−phi^(−2))=phi^(−j−2)<phi^(−j).
Při sudém j je tedy 0<S<phi^(−1), takže celé číslo
existuje. Při lichém j je S mod 1=1+S>phi^(−1),
takže v intervalu není žádné.

Lichý j přesně znamená konec řetězce 1 0^(2k) 1.
Tím je dokázáno celé tvrzení odpovědi: všechny ostatní
řetězce bez sousedních jedniček patří právě jednomu
kladnému celému číslu, uvedené konce žádnému.
Vlastní důkaz této klasifikace nenahrazuje historickou
četbu Bergmanova článku, vedenou zvlášť.
