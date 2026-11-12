# V2-C0141: chybná normalizace gcd v úloze4.5.3-49

Stav: **confirmed** v našich zdrojích. Zadání379 s
 theta=sqrt(lambda*mu*v/d), d=gcd(u,v), je nepravdivé
pro d>1. Odpověď656 vynechává faktor d v součinu
obsahujícím zbytek rozšířeného Eukleidova algoritmu.
Poslední fyzický dotisk a priorita nejsou ověřeny.

## Přesný malý protipříklad

Vektory T_j=(x_j,y_j,z_j) mají x_j u+y_j v=z_j.
Vezměme u=4, v=2, d=2. Poslední podíl2 rozdělíme
na1,1, přesně jak zadání dovoluje. Počet kroků n=2
je sudý a algoritmus dává

```
T_0=( 1, 0,4),
T_1=( 0, 1,2),
T_2=( 1,-1,2),
T_3=(-1, 2,0).
```

Pro lambda=9/4, mu=1 má knižní theta hodnotu3/2.
Absolutní hodnoty lambda*x_j+mu*z_j-[j sudé]*theta
pro j=1,2,3 jsou postupně

```
2, 11/4, 9/4.
```

Jejich minimum2 je větší než3/2. Nejde o numerické
zaokrouhlení ani o zakázanou paritu.

Stejná rodina funguje pro u=2d, v=d a každé celé d>=2.
Dvě prostřední kladné složky z jsou nyní d; při stejných
vahách zůstává theta=3/2 a absolutní hodnoty jsou
 d, d+3/4, 9/4, všechny větší nežtheta.

Pro případ bez úpravy posledního podílu lze vzít
u=6,v=4,lambda=mu=1. Kanonické podíly1,2 dávají
T_1=(0,1,4),T_2=(1,-1,2),T_3=(-2,3,0).
Hodnoty4,3-sqrt(2),2 jsou všechny větší nežsqrt(2),
protože3>2sqrt(2).

## Přesné místo chyby a oprava

Kontinuant K je definován v [euclid-basic.md](euclid-basic.md)
a v úloze48. Tam již bylo obecně dokázáno

```
x_j=(-1)^j K(a_2,...,a_(j-1)),
z_j=d K(a_(j+1),...,a_n).
```

Z toho plyne pro1<=k<=n

```
|x_(k+1) z_k|
 = d K(a_2,...,a_k) K(a_(k+1),...,a_n)
 <= d K(a_2,...,a_n)
 = v.                                                   (W1)
```

Nerovnost je supermultiplikativita kontinuantu na
kladných blocích: K(A,B)=K(A)K(B)+nezáporný člen.
Prázdný blok má kontinuant1. Možný počáteční nulový
podíl a_1 se v (W1) nevyskytuje.

Knižní odpověď v prvním součinu faktor d nemá a končí
mezí v/d. Navíc předchozí řádek používá rovnost
2lambda*mu*v/theta=2theta, která s knižním theta
platí pouze pro d=1.

Jedna úplná oprava zachová vektory a všechny váhy,
ale v zadání nahradí theta hodnotou

```
Theta=sqrt(lambda*mu*v).                               (W2)
```

V odpovědi je potom třeba vrátit faktor d do obou
kontinuantových výrazů v (W1) a poslední v/d nahradit v.
Alternativně lze ponechat původní theta a ve váženém
výrazu všude použít normalizované z_j/d. To je stejná
opravená věta po náhradě mu hodnotou mu/d.
Přidání předpokladu d=1 je další, ale zbytečně omezující,
možnost. Netvrdíme, která z nich nejlépe vyjadřuje
původní autorský úmysl.

## Obecný důkaz opravené věty

Položme S_j=lambda*x_j+mu*z_j a použijme Theta z (W2).
Na lichých indexech x_j<=0, na sudých x_j>0;
všechny z_j jsou nezáporné. Krajní liché hodnoty
jsou S_1=mu*v>0 a S_(n+1)=-lambda*v/d<0.
Proto existuje liché j s S_j>=0 a S_(j+2)<=0.

Je-li jedna z těchto dvou hodnot v [-Theta,Theta],
požadovaná nerovnost už platí na tomto lichém indexu.
Jinak S_j>Theta a S_(j+2)<-Theta. Odtud

```
mu > Theta/z_j,
lambda > -Theta/x_(j+2).
```

Dělitele mají potřebná znaménka: z_j>0 a x_(j+2)<0.
Na mezilehlém sudém indexu pak máme

```
0 < S_(j+1)
  < lambda*mu * (x_(j+1)z_j-z_(j+1)x_(j+2))/Theta
  <= 2lambda*mu*v/Theta
  = 2Theta.                                             (W3)
```

Pro poslední nerovnost použijeme (W1) s k=j a k=j+1.
Tedy |S_(j+1)-Theta|<Theta, což je právě sudá větev
požadovaného tvrzení. Obě možnosti dohromady dokazují
opravu pro libovolné kladné reálné lambda,mu a všechny
povolené celočíselné vstupy. Důkaz není omezen na
soudělné či nesoudělné vstupy z konečného výčtu.

## Zdroje a nezávislá kontrola

Originály379 a656 byly vizuálně přečteny, včetně
rozsahu odmocniny a vynechaného d v kontinuantu.
Prohledány all2-prepre,all2-pre,all2,err2 a aktuální
TeX; žádná oprava49 ani této normalizace nenalezena.
Historická řada druhého vydání má stejný text odpovědi
pod starým číslem46; není to nová oprava našeho vydání.

Lenstrův citovaný článek *Divisors in residue classes*,
Math.Comp.42(1984),331–340 byl získán z autorovy stránky.
Strany332–334 byly přečteny i obrazově. Lemma1.6 používá
obdobný přechod mezi znaménky; sousední determinant na333
obsahuje celý počáteční modul s. Náš protipříklad se
netýká Lenstrovy věty. Zbytek článku není tímto blokem
prohlášen za prověřený.

Běh `verify_euclid_weighted.py`, PID1233741, relace79219,
limit120, exit0,15.65s, ověřil9216 vstupních dvojic,
41068 přesných součinových certifikátů a101376 voleb vah.
Obě opravené formulace prošly; původní neplatila v12983
zvolených případech. Dále prošlo127 členů obecné rodiny.
Kontrolují se racionální druhé mocniny: na lichém indexu
S_j^2<=Theta^2, na sudém0<=S_j a S_j^2<=4Theta^2.
Proto není rozhodování závislé na přesnosti odmocniny.
Výpočet vektorů a kontrola kontinuantového součinu jsou
samostatné metody; obecný důkaz je v (W1)–(W3).

Návrh hlášení je neodeslaný.
