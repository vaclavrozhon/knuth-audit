# §4.5.4-42: dělitelé v předepsané zbytkové třídě

Zadání416 a odpověď667–668 byly přečteny obrazově. Hlavní existenční
a časové tvrzení platí. V tištěném algoritmu jsou dvě doložené chyby:
[C0177](C0177-lenstra-denominator.md), chybný jmenovatel vypisující
například4 jako dělitele14, a [C0178](C0178-lenstra-floor-bound.md),
nepravdivá pomocná nerovnost po zaokrouhlení dolů.
Níže je vlastní úplný důkaz varianty s oběma opravami.
U samotného zaokrouhlení netvrdíme nalezení chybného výstupu.

## 1. Vstup a převod na dvě rovnice

N je kladné celé číslo, s modul a r hledaná zbytková třída;
0<r<s<N a gcd(r,s)=gcd(N,s)=1. Označme rbar inverzi r modulo s,
zvolenou mezi1 a s−1. Všechna další `mod s` znamenají nejmenší
nezáporný zbytek. Definujeme

```
r' = N*rbar mod s,
u  = r'*rbar mod s,
w  = ((N-r*r')/s)*rbar mod s,
Theta = ceil(sqrt(N/s)).                                  (L1)
```

Podíl v definici w je celé číslo, protože rr'≡N modulo s.
Čísla r',u jsou jednotky modulo s, tedy nenulová a nesoudělná se s.
Každý kladný dělitel d≡r má právě jeden tvar d=lambda*s+r,
lambda>=0. Jeho doplněk N/d je kongruentní s r', takže
N/d=mu*s+r' pro jediné mu>=0. Hledáme tedy přesně řešení

```
(lambda*s+r)(mu*s+r')=N,
lambda*u+mu ≡ w (mod s).                                  (L2)
```

Druhá rovnice plyne z první po odečtení rr', dělení s a násobení
rbar modulo s. Pro lambda,mu>0 platí

```
lambda*mu*s < N/s <= Theta^2.                             (L3)
```

Původní floor místo ceil poslední nerovnost nezajišťuje.
Knižní malé n v definici r' a w čteme jako vstup N.

## 2. Eukleidovy vektory a nalezení malé lineární kombinace

Použijeme dvojice (x_j,z_j) tvořené první a třetí složkou
rozšířeného Eukleidova algoritmu: první dvě jsou (1,u),(0,s)
a každá další je předpředchozí minus celočíselný podíl krát předchozí.
Jde o dvojici `(v1,v3)` z odpovědi. Platí z_j≡u*x_j modulo s,
a proto ze (L2)

```
lambda*z_j+mu*x_j ≡ w*x_j (mod s).                        (L4)
```

Sousední determinant má absolutní hodnotu s. Koeficienty x_j
střídají znaménko a z_j jsou nezáporné klesající zbytky.
Při přesném posledním dělení a x_j<0 se podíl sníží o1;
následuje ještě podíl1. Tím se poslední nulový zbytek vyskytne
u záporného x_j. Protože gcd(u,s)=1, poslední dvojice je (−s,0).
První zpracovávaná dvojice je (0,s). Úprava přidá nejvýše jeden krok
k obvyklému algoritmu, takže počet dvojic je O(log s).

Pro úplnost zde přímo dokazujeme potřebnou váženou mez.
Položme T=sqrt(lambda*mu*s), při lambda,mu>0, a
S_j=lambda*z_j+mu*x_j. Na subsekvenci s x_j<=0 začíná S_j
hodnotou lambda*s>0 a končí hodnotou −mu*s<0.
Existují sousední členy této subsekvence, mezi nimiž se změní
znaménko. Označme jejich dvojice (x,a) a (z,c), prostřední
kladnou dvojici (y,b). Tedy x<=0, z<0, y>0, a,b>0, c>=0.
Pokud jeden kraj splňuje |S_j|<=T, jsme hotovi. Jinak

```
lambda*a+mu*x > T,     lambda*c+mu*z < -T,
lambda > T/a,         mu > T/(-z).
```

Sousední determinanty dávají ya−xb=s a yc−bz=s.
Odtud ya<=s a −bz<=s, protože x<=0 a c>=0.
Proto na prostředním indexu

```
0 < lambda*b+mu*y
  < lambda*mu*(a*y-b*z)/T
  <= 2*lambda*mu*s/T = 2T.                               (L5)
```

Tedy některá dvojice splní |S_j|<=T při x_j<=0,
nebo 0<S_j<=2T při x_j>0. Díky (L3) lze T nahradit Theta.
To je přesné pokrytí intervaly kroku L2. Je to také zvláštní případ
opravené vážené věty v [C0141](C0141-weighted-euclid-gcd-factor.md);
zde je gcd(u,s)=1, takže dřívější chyba normalizace gcd nezasahuje.

V krajním prvním případě S=lambda*s, takže lambda<=Theta/s.
V posledním případě S=−mu*s, takže mu<=Theta/s.
Nulové lambda se vždy zachytí na začátku jako d=r, nulové mu
na konci jako d=N/r'. Proto v ostatních větvích stačí vyžadovat
obě neznámé kladné. Krajní testy dělitelnosti rovnou zajistí
správnost i předepsanou zbytkovou třídu výstupu.

## 3. Kvadratická eliminace a chyba jmenovatele

Fixujme jednu nekrajní dvojici (v1,v3) a číslo
z=w*v1+k*s v příslušném intervalu. Hledáme (L2) a
lambda*v3+mu*v1=z. Položme

```
A = v3*(lambda*s+r),
B = v1*(mu*s+r'),
H = z*s+v3*r+v1*r'.
```

Pak A+B=H a AB=v1*v3*N. Čísla A,B jsou oba kořeny
t^2−Ht+v1*v3*N. S diskriminantem D=H^2−4v1*v3*N
a sigma∈{−1,+1} dostáváme

```
lambda = (z*s-v3*r+v1*r'+sigma*sqrt(D))/(2*v3*s),
mu     = (z*s+v3*r-v1*r'-sigma*sqrt(D))/(2*v1*s).           (L6)
```

V druhém jmenovateli má být v1, nikoli vytištěné v3.
Je-li D nezáporný čtverec a obě hodnoty kladná celá čísla,
odvození je vratné: obě rovnice skutečně platí a lambda*s+r
je požadovaný dělitel. Obráceně každé řešení dává jeden z obou
kořenů, takže se neztratí. D=0 je povolen a jen může zdvojit výstup.
Záporné v1 nevadí: jeho znaménko je zahrnuto ve jmenovateli mu.

Knižní závěrečná poznámka správně připouští opakované výstupy.
Množinu lze sestavit následně; důkaz časové meze se týká proudu
výstupů s případnými opakováními, stejně jako odpověď.

## 4. Čas a velikost čísel

Interval pro z má délku nejvýše2Theta, přičemž z leží v jedné
třídě modulo s. Na jednu dvojici proto připadne O(1+Theta/s)
hodnot k, a tedy tolik řešení kvadratické rovnice. Krajní větve
mají stejnou mez. Jelikož

```
1+Theta/s = O(1+sqrt(N/s^3))
          = O(sqrt(ceil(N/s^3))),
```

celkem je to O(sqrt(ceil(N/s^3))*log s) aritmetických kroků,
včetně původního výpočtu rbar. Zobrazené ceil v zadání416
skutečně uzavírá N/s^3 před umocněním na1/2.

Počítáme celočíselnou odmocninu mezi aritmetické operace,
stejně jako Lenstrův rozbor na335. Nejde o bitové jednotkové
náklady: při realizaci odmocniny základními operacemi se musí
přičíst její cena. Počet bitů všech mezivýsledků je O(log N).
Například |v1|,v3<=s<N, |z|<=2Theta a |H|=O(N^2),
tedy |D|=O(N^4). Knižní formulaci o lgNbitových číslech
čteme asymptoticky, nikoli jako tvrzení, že každý diskriminant
je menší než N. Není potřeba aritmetika neomezených čísel
s exponenciální délkou, jako v předchozí úloze40.

## 5. Rozsah zdrojů a kontroly

Lenstra, *Divisors in Residue Classes*, Math.Comp.42(1984),331–340,
[autorova kopie](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1984b/art.pdf):
vizuálně přečteny331–335, tedy úvod a celý algoritmický §1.
Soubor má11stran včetně úvodního obalu; tištěná331 je druhá.
Jeho kvadratická formulace na333 je správná a nepoužívá chybný
knižní jmenovatel ani zaokrouhlenou pomocnou nerovnost.
Kombinatorický důkaz meze11 dělitelů v §2–3 není součástí
této úlohy ani tohoto auditu. Zdrojové SHA a obrazové strany
jsou v `sources/lenstra-residues.json`.

Prohledány celé texty all2-prepre,all2-pre,all2,err2 a aktuální
TeX; sousední opravy667–668 patří41 a43, pro42 nebyla nalezena
oprava obou zde uvedených míst. Historický text err2-2e,
nová odpověď42 na staré616 z11.10.1995, už obsahuje obě místa;
jde o historii stejného problému, nikoli opravu. Tato historická
vrstva zde byla čtena textově, neprohlašujeme její obrazovou kontrolu.
Fyzický poslední dotisk ani prvenství nálezu nejsou ověřeny.

`verify_lenstra_residues.py` používá přesné celé odmocniny a
nezávisle získané seznamy dělitelů. Tři checkpointy prošly:

* Přímé protipříklady14/36 včetně úplné stopy algoritmu14.
* Všech293751 povolených trojic (N,r,s) pro3<=N<=160,
  z toho260545 tříd bez výsledku;35483 výstupů porovnáno
  s přímým dělením do sqrt(N).1919937 stavů a722390 kandidátů.
* 616 tříd pro12 plně rozložených84–109bitových čísel.
  Všechny dělitele vytváří nezávislý součin mocnin2,3,5,7;
  porovnává se úplný výsledek, nikoli jen známý zasazený faktor.

Běh PID1310967/1310968,session13908,limit180,exit0;
čas14.267s. Opravená varianta bez změny floor byla v malém
výčtu také porovnána a nevynechala žádného dělitele.
To **není obecný důkaz** této úspornější varianty.
Předběžná kontrola106921 deterministicky náhodných rozkladů
také nenašla selhání pokrytí s floor; byla průzkumná a její
výstup není používán jako certifikát. Důkaz výše používá ceil.
