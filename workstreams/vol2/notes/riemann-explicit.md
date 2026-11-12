# §4.5.4-25: Riemannova explicitní formule

Zadání414, odpověď663 a definice pi na381 byly přečteny obrazově.
Potvrzeny [C0179](C0179-riemann-real-part.md), chybějící reálná část,
a [C0180](C0180-riemann-jump-sign.md), opačné znaménko půlskoku.
Tištěná konstanta je správná na všech40 uvedených desetinných míst.
Oprava n→x z10.12.2011 je známá a obě nové chyby neodstraňuje.

Analytickou větu o konvergenci párované řady přebíráme od von Mangoldta;
neprohlašujeme celý jeho51stránkový důkaz za nezávisle znovu dokázaný.
Vlastní práce níže přesně převádí jeho formulaci, dokazuje korekce,
kontroluje konstantu a odvozuje skutečnou divergenci nepárované řady
z další klasické, výslovně uvedené Landauovy věty.

## 1. Tři konvence pro hodnotu ve skoku

Kniha381 definuje pi(x) jako počet prvočísel **p<=x**;
uvádí výslovně pi(2)=1. Pro reálné x>1 označme

```
J(x) = sum_(k>=1) pi(x^(1/k))/k
     = sum_(p^k<=x) 1/k,
J_<(x) = sum_(p^k<x) 1/k,
J_0(x) = (J(x)+J_<(x))/2.                                (R1)
```

Součty jsou konečné: pro k>log(x)/log2 není žádný člen.
Jedno číslo může být mocninou nejvýše jednoho prvočísla;
je-li x=p^k, příslušný skok má velikost1/k. Tedy

```
J(x) = J_0(x)+delta(x),
delta(x) = 1/(2k) pro x=p^k, jinak0.                      (R2)
```

J_0 je symetrická hodnota ve skoku, která vzniká při Fourierově
nebo Mellinově inverzi. Například J(2)=1,J_0(2)=1/2,J_<(2)=0.
Znaménko minus by patřilo J_<, nikoli knižnímu J.

## 2. Přesná analytická formule a větve integrálů

Zeta(s) je analytické pokračování řady sum_(n>=1)n^(−s), původně
konvergentní pro Re(s)>1. Písmeno i značí odmocninu z−1.
Netriviální nuly zapisujeme rho=sigma+i*tau, 0<sigma<1;
zahrnujeme násobnosti. Kladné tau řadíme podle velikosti.
Pro takovou nulu a L=log x>0 definujeme

```
I_rho(x) = integral_(-infty)^sigma exp((t+i*tau)L)/(t+i*tau) dt.
```

Každý tento horizontální integrál je absolutně konvergentní.
Při tau>0 platí

```
I_rho(x)=Ei(rho*L)-i*pi,                                 (R3)
```

kde Ei je analytické pokračování exponenciálního integrálu
s obvyklým řezem na záporné reálné ose. Člen −i*pi zajišťuje
právě nulovou limitu primitivní funkce při t→−infty v horní
polorovině. V dolní polorovině je znaménko opačné.
Konjugovaná nula proto přispívá komplexně sdruženým integrálem.

Definujme ještě reálný logarithmický integrál
li(x)=PV integral_0^x dt/log t; PV znamená symetrickou hlavní
hodnotu kolem pólu t=1. Dále kladný zbytek

```
R(x)=integral_x^infty dt/((t^2-1)*t*log t).
```

Von Mangoldtova rigorózní formule, s konvergencí v pořadí výšek nul, je

```
J_0(x) = li(x)-log2+R(x)
         -2 lim_(T→infty) sum_(0<tau<=T) Re I_rho(x).       (R4)
```

Zde Re značí reálnou část. Musí být uvnitř limitního procesu:
nejde o reálnou část již sečtené nepárované komplexní řady.
Ekvivalentní je sečíst obě poloroviny symetricky a vynechat2.
Riemannova hypotéza, tedy sigma=1/2 pro všechny nuly, se nepředpokládá.
Ve von Mangoldtově zápisu jsou spárovány rho a1−rho; díky symetrii
množiny nul vůči reálné ose a přímce Re(s)=1/2 je to tentýž
součet všech nul pod danou výškou, i bez Riemannovy hypotézy.

Pro orientaci v důkazu: Eulerův součin dává pro Re(s)>1

```
log zeta(s)=sum_(p,k>=1) 1/(k*p^(ks)),
log zeta(s)/s=integral_1^infty J(x)*x^(-s-1) dx.            (R5)
```

Druhá rovnost plyne integrací každé skokové funkce zvlášť;
absolutní konvergence dovoluje záměnu. Inverze tohoto Mellinova
transformátu, což je Fourierova inverze po substituci x=exp(u),
vrací právě J_0. Pól zety v1 dává li(x), její netriviální nuly
dávají záporné párované integrály a triviální nuly −2,−4,...
dávají R(x). Konstanta je log|zeta(0)|=−log2.
Rigorózní vyhodnocení a konvergence této inverze jsou analytický
vstup z citovaného článku, nikoli důsledek konečných testů níže.

Přečteny byly zejména jeho definice střední hodnoty na295,
integrace parametru na296–299 a úplný převod na li a obě komplexní
větve na300–302. Rovnice(64) na299 obsahuje správné −log2.
Její poznámka výslovně opravuje historické log xi(0) v Riemannově
původní publikaci; knižní konstanta tuto starší chybu nemá.

## 3. Převod na zadání, konstanta a omezený zbytek

Jelikož li(x)=integral_2^x dt/log t+li(2), z(R2) a(R4) plyne

```
J(x) = integral_2^x dt/log t
       -2 lim_(T→infty) sum_(0<tau<=T) Re I_rho(x)
       + C+R(x)+delta(x),
C = li(2)-log2.                                          (R6)
```

To je opravené zadání i přesný výklad jeho O(1). Je třeba
vložit reálnou část a v odpovědi nahradit minus půlskok znaménkem plus.
Pro x=2 vrací výraz bez delta hodnotu1/2; plus dává1,
vytištěné minus dává0. Pro x=p^k je rozdíl mezi tištěnou
a správnou přesnou odpovědí1/k. Samotné asymptotické O(1)
samozřejmě půlskok pohltí; C0180 se týká jeho výslovně udané hodnoty.

Eulerovu konstantu gamma definujeme jako limitu
sum_(j=1)^n 1/j−log n. Z rozvoje Ei(z) pro kladné z dostaneme

```
C = gamma+log(log2)+sum_(n>=2) (log2)^n/(n*n!)
  = 0.3520165995575474754273567677364365684471154437909...
```

Člen n=1 je právě log2 a odečte se. Všechny členy zbývajícího
součtu jsou kladné. Po100členech je ocas menší než8.893*10^(−179),
jak plyne z poměru po sobě jdoucích členů; intervalový výpočet
zahrnuje navíc zaokrouhlení základních funkcí.

Pro R(x) lze geometrickou řadu integrovat člen po členu,
protože všechny její členy jsou kladné:

```
R(x)=sum_(m>=1) E1(2m*log x),
E1(z)=integral_z^infty exp(-t)/t dt,  z>0.                 (R7)
```

Z E1(z)<=exp(−z)/z plyne

```
0<R(x)<=-log(1-x^(-2))/(2log x).
```

R(x) je klesající, R(2)=0.140010101143286926686917305234299733...
a 0<=delta<=1/2. Pro všechna x>=2 je tudíž zbytek v(R6)
kladný a menší než C+R(2)+1/2<1. Zejména je rovnoměrně O(1).

## 4. Proč chybějící reálná část skutečně vadí

Použijeme **Landauovu formuli** jako druhý externí analytický vstup.
Pro pevné reálné x>1 označme Lambda(x)=log p, je-li x=p^k,
a0 jinak. Pak

```
A_x(T):=sum_(0<tau<=T) x^rho
       = -Lambda(x)*T/(2*pi)+O_x(log T).                   (R8)
```

Primárně ověřeno na první straně Gonekova článku; jeho vzorec(1)
je nepodmíněný, Riemannova hypotéza se objevuje až v další větě.
Dolní index x u O připouští závislost konstanty na pevném x.

Následující odvození je vlastní. Integrací I_rho per partes máme

```
I_rho(x)=x^rho/(rho*L)+E_rho,
|E_rho|<=x^sigma/(L^2*tau^2).
```

Protože 0<sigma<1, je také
1/rho=1/(i*tau)+O(tau^(−2)). Počet nul do výšky T je
O(Tlog T), takže suma tau^(−2) konverguje; chyby výše tedy
tvoří absolutně konvergentní řadu. Parciální sumace(R8) dává

```
sum_(0<tau<=T) x^rho/tau
 = A_x(T)/T+integral^T A_x(t)/t^2 dt
 = -Lambda(x)/(2*pi)*log T+K_x+o(1).
```

Dolní mez integrálu je libovolná pevná kladná hodnota pod první
nulou; její příspěvek je zahrnut do konstanty K_x. Ocas integrálu
O_x(log t)/t^2 je integrabilní. Dostáváme tedy

```
sum_(0<tau<=T) I_rho(x)
 = i*Lambda(x)/(2*pi*log x)*log T+K'_x+o(1).               (R9)
```

Pro x=p^k je koeficient i/(2*pi*k) nenulový. Zejména při x=2
roste imaginární část jako log T/(2*pi). Nepárovaná řada v zadání
nekonverguje; nelze ji opravit přičtením konečného O(1).
Výpočet konečného počtu nul pro tento závěr není potřeba.

## 5. Doklady, hranice kontroly a testy

Primární zdroje:

* [Von Mangoldt1895](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0114/LOG_0020.pdf):
  stažen původní sken255–305 s obalem, vizuálně255–258 a294–302.
  Nejde o kontrolu všech51stran ani všech předchozích konvergenčních odhadů.
  Bibliografie114(1895),255–305 souhlasí s EuDML a knihovními metadaty.
* [Riemann1859, překlad Wilkins1998](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf):
  tištěné4–8, souborové5–9, definice střední hodnoty a obě komplexní větve.
  Jeho původní nedoložené konvergenční kroky nenahrazují Mangoldtův důkaz.
* [Gonek, A Formula of Landau and Mean Values of zeta(s)](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/8-landau-form.pdf):
  souborové1–2, vzorec(1) a oddělení nepodmíněné věty od pozdějších výsledků s RH.
  Landauova věta je použitý externí výsledek, její úplný důkaz zde neopakujeme.

Karatsubův autorův seznam uvádí CRC1995; Shallitova stránka
uvádí MIT srpen1996 a obsah8.3–8.5 výslovně RH/ERH/aplikace.
Tyto bibliografické odkazy souhlasí. Obě celé monografie nejsou
v tomto bloku prohlášeny za přečtené. Google Books uvádí u Karatsuby
datum distribuce1994; neoznačujeme to za rozpor s autorskou citací1995.

Prohledány celé čtyři řady all2-prepre,all2-pre,all2,err2 a aktuální
TeX. Jediná nalezená oprava25 je n→x na663 z10.12.2011,
obrazově ověřena. Historická řada druhého vydání přidává minus
půlskok na staré614 dne24.10.1995; nepředstavuje opravu znaménka.
Poslední fyzický dotisk ani priorita nových nálezů nejsou ověřeny.

Přesné a intervalové kontroly `verify_riemann_explicit.py`:

* Konstanta přes Ei a samostatný kladný rozvoj s explicitním ocasem;
  certifikováno všech40tištěných desetinných míst.
* 19999 celých x od2 do20000: součet přes prvočíselné mocniny
  proti nezávislému výpočtu pi(celá k-tá odmocnina)/k;
  2328skoků a znaménko každé korekce přesnými zlomky.
* 36horizontálních integrálů pro racionální sigma,tau a x=2,4,10,100:
  validovaná kvadratura proti Ei−i*pi, s explicitním ocasem od−infty.
  Zvolené body se nevydávají za nuly zety; kontrolují příslušnou větev.
* 4hodnoty R(x): validovaná kvadratura proti100členům(R7)
  s explicitní geometrickou horní mezí ocasu.

Všechny4bloky passed1.808s,PID1312147/1312148,session41395,
limit180,exit0,256bitová intervalová aritmetika. Neprováděl se
nekonečný součet nul numerickým odříznutím a výsledek se neopakoval.
