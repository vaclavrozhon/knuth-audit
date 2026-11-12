# V2-C0142: obrácené krajní podmínky v odpovědi4.5.3-50

Stav: **confirmed**. Tištěná odpověď656 vrací nesprávný
index pro povolené reálné kraje intervalu. Při převodu
na převrácenou rotaci musí rekurze prohodit zahrnutí
levého a pravého kraje. Úloha379 i odpověď656 byly
vizuálně přečteny. Všechny čtyři řady errat a aktuální
TeX byly prohledány; oprava tohoto problému nenalezena.
Poslední fyzický dotisk a priorita nejsou ověřeny.

## Přesný protipříklad

Zlomková část čísla t je {t}=t-floor(t). Funkce f(alpha,
beta,gamma) v zadání vrací nejmenší celé n>=0 splňující
beta<={n alpha}<gamma. Vezměme

```
alpha=sqrt(2)-1,
beta=alpha/2,
gamma=alpha.                                           (R1)
```

Všechny předpoklady0<beta<gamma<1 jsou splněny.
Knižní k=ceil(beta/alpha)=1. Test k alpha<gamma
neprojde kvůli rovnosti. Rekurzivní volání je

```
f({1/alpha},0,1/2)=0.
```

Vnější vzorec proto vrátí k-1+ceil(0/alpha)=0.
To není řešení, protože beta>0.

Správný výsledek je3. Platí2/5<alpha<1/2; tyto dvě
nerovnosti lze ověřit umocněním kladných stran.
Index0 je pod intervalem, index1 přesně na vyloučeném
pravém kraji a index2 má zlomkovou část2alpha>gamma.
Pro index3 je zlomková část3alpha-1 a

```
alpha/2 < 3alpha-1 < alpha.
```

Stejný protipříklad funguje pro každé iracionální
alpha v (2/5,1/2), s beta=alpha/2 a gamma=alpha.

## Dvě varianty funkce

Aby rekurze byla uzavřená, definujme pro
0<=beta<gamma<=1 dvě funkce:

```
F_L(alpha,beta,gamma): první n>=0 s beta<={n alpha}<gamma,
F_R(alpha,beta,gamma): první n>=0 s beta<{n alpha}<=gamma.
```

Písmeno L znamená zahrnutý levý kraj a R zahrnutý pravý.
Rozšíření gamma<=1 slouží pomocným voláním. Zlomková
část nikdy není1, takže zahrnutí samotné1 nepřidá zásah.
Původní úloha žádá F_L pro gamma<1.

Pro F_L nastavíme k=ceil(beta/alpha) a při
k alpha<gamma vrátíme k. Pro F_R nastavíme
k=floor(beta/alpha)+1 a při k alpha<=gamma vrátíme k.
V obou případech je k první přípustný index bez oběhu
přes1; menší indexy mají n alpha pod levým krajem,
případně na jeho vyloučené hodnotě.

Pokud přímý test neprojde, položme

```
alpha'={1/alpha},
beta'=k-gamma/alpha,
gamma'=k-beta/alpha.                                   (R2)
```

Správná rekurze je

```
F_L = k-1+ceil(F_R(alpha',beta',gamma')/alpha),
F_R = k-1+ceil(F_L(alpha',beta',gamma')/alpha).           (R3)
```

Knižní odpověď má v první rovnici vpravo opět F_L.
To je konkrétní chyba.

## Proč rekurze zachovává všechny zásahy i minimum

Při neúspěšném přímém testu neexistuje zásah s
floor(n alpha)=0. Zároveň0<=beta'<gamma'<=1.
U F_L je beta'>=0 a gamma'<1; u F_R je beta'>0
a gamma'<=1. Tyto vztahy plynou přímo z definice k
a z opačné nerovnosti v neúspěšném testu.

Každý původní zásah má tedy celé m=floor(n alpha)>=1.
Napišme m/alpha=L+t s celým L=floor(m/alpha) a
0<t<1. Nenulovost t plyne z iracionality alpha.
Protože {m/alpha}={m alpha'}, je t zlomkovou částí
pomocné rotace. Pro první typ intervalu dostaneme

```
m+beta <= n alpha < m+gamma
  <=> L+k+t-gamma' <= n < L+k+t-beta'.                 (R4)
```

Vzhledem k0<=beta'<gamma'<=1 je jediný možný celý
index n=L+k. Existuje právě když beta'<t<=gamma',
tedy při zásahu typu F_R. U druhého typu se obě
nerovnosti v (R4) obrátí na ostrou/neostrou v opačném
pořadí a dostaneme beta'<=t<gamma', tedy F_L.
To dokazuje přesné prohození krajů.

Pomocný první zásah má vždy m>=1: v první větvi je
nula vyloučená otevřeným levým krajem, ve druhé
beta'>0. Proto ceil(m/alpha)=L+1 a návratová hodnota
(R3) je opravdu L+k. Navíc L+k přísně roste s m,
protože1/alpha>1. Bijekce (R4) tedy zachovává pořadí
i nejmenší přípustný index, nikoli jen existenci zásahu.

## Ukončení bez předpokládaného výsledku

Délku intervalu označme w=gamma-beta>0. Každý
neúspěšný přímý test mění její délku na w/alpha.
Všechny pomocné intervaly mají délku nejvýše1.
Je-li h=floor(1/alpha)>=1, pak

```
alpha*alpha'=1-h alpha < 1/(h+1) <= 1/2.               (R5)
```

Dvě po sobě jdoucí rekurzivní větve tedy zvětší
šířku více než dvojnásobně. Nemohou se opakovat
nekonečně; počet volání je O(1+log(1/w)).
V nejhlubším volání přímý test uspěje. Indukce
pomocí (R4) pak dokazuje správnost všech návratů
a zároveň existenci prvního zásahu. Není nutné
použít hustotu rotace jako nedoloženou podmínku ukončení.

Jde o počet přesných reálných aritmetických operací;
netvrdíme takto automaticky stejnou bitovou mez pro
libovolný způsob zadání reálných vstupů. Konečný
validátor používá jen přesná kvadratická čísla.

## Nezávislá kontrola

`verify_euclid_rotation.py` porovnává (R3) s přímým
sledováním rotace: opakovaně přičte alpha a při dosažení1
jedničku odečte. Orákulum nepoužívá rekurzivní vzorec.
Čísla mají tvar a+b sqrt(D), a,b racionální; znaménka
se porovnávají přesně pomocí racionálních druhých mocnin.
Pro podlahy se používají racionální uzávěry odmocniny
z již prověřeného modulu `verify_euclid_quadratic.py`.

Kontroly zahrnují racionální mřížky, kraje přímo na
orbitech rotace, oba typy zahrnutí krajů a velmi úzké
intervaly. Konečný neúspěšný průchod orákula by byl
chybou rozsahu testu, nikoli důkazem neexistence zásahu.
Běh PID1235492, relace39718, limit180, skončil s exit0.
Prošlo21 členů protipříkladové rodiny,12096 porovnání
pro16 kvadratických rotací a4074 rekurzivních přechodů.
Osm úzkých intervalů má první zásahy100,1000,4096,9999
a nejvýše10 úrovní rekurze. Hlavní porovnání17.52s,
úzké intervaly3.31s. Původní formule se odlišila v684
testovaných intervalech; tento soubor zahrnuje i pomocný
obor gamma=1. Protipříklad(R1) leží v původním oboru.

Návrh hlášení je neodeslaný.
