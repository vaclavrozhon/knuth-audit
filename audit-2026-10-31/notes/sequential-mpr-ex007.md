# D110 — celá MPR7: obecná přesně k-násobná nezávislost

6. listopadu 2026. Celé zadání13/file33 a odpověď372/file392
přímo zobrazeny; stejná matematika v autorově Pre-Fascicle5A,
13/file19 a28/file34. Níže je každý vytištěný polynom,
mezilehlá identita, nezápornost, normalizace i skutečný
řád nezávislosti. Použité binární momentové kritérium
je celé dokázané v D109; žádný výpočet se neopakuje.

## Rozsah a přesný tvar konstrukce

Je dáno celé k≥1. Pro ne-(k+1)-násobnou nezávislost
potřebujeme alespoň k+1 různých souřadnic; zvolme tedy
libovolné celé n≥k+1 a d=n+1−k≥2. Pro0≤m≤N definujme
tištěný polynom

```
f_m(N)=Σ_{j=0}^m (−1)^j binom(N,j)(N+1−m)^{m−j}.
```

Konstrukce „jako v odpovědi6“ znamená přesně

```
a_j=f_{k−j}(n−j) pro0≤j≤k, jinak a_j=0,
P(X=x)=a_{νx}/d^k.
```

Všechny hodnoty a_j s j≤k leží v rozsahu N≥m≥0
a denominator je kladný. Rozdělení závisí pouze
na počtu jedniček νx, jak zadání vyžaduje.
Nezápornost a normalizaci nyní dokážeme, nikoli předpokládáme.

## Vytištěná normalizační identita

Pro libovolná N≥m≥0 položme d_m=N+1−m. V součtu
f_{m−j}(N−j) je základ mocniny vždy tentýž d_m.
Roznásobením obou konečných součtů dostáváme

```
Σ_{j=0}^m binom(N,j)f_{m−j}(N−j)
 = Σ_{j=0}^m Σ_{l=0}^{m−j}
      binom(N,j)binom(N−j,l)(−1)^l d_m^{m−j−l}.
```

Položme h=j+l. Identita
binom(N,j)binom(N−j,h−j)=binom(N,h)binom(h,j)
plyne buď z faktoriálů, nebo z výběru h prvků a jejich
j-prvkové podmnožiny. Součet je tedy

```
Σ_{h=0}^m binom(N,h)d_m^{m−h}
               Σ_{j=0}^h binom(h,j)(−1)^{h−j}.
```

Vnitřní součet je(1−1)^h:1 pro h=0 a0 pro h>0.
Výsledkem je přesně(N+1−m)^m, což ověřuje celou
tištěnou identitu včetně prázdného případu m=0.
Pro N=n,m=k tak součet hmotností všech binárních
vektorů jeΣ_j binom(n,j)a_j/d^k=1.

## Převod f_m(N) na druhý alternující součet

Pro m≥1 nejprve oddělme N=m. Tehdy základ původního
součtu je1 a f_m(m)=(1−1)^m=0. Případ m=0 má
f₀(N)=1, včetně N=0. Zbývá N>m, takže t=N−m≥1.

Rozepišme(t+1)^{m−j} binomicky. Koeficient u t^{m−h}
v celém původním výrazu je

```
Σ_{j=0}^h (−1)^j binom(N,j)binom(m−j,h−j).
```

Tato suma je přesně binom(m−N,h). Pro úplný důkaz
stačí vzít koeficient z^h v identitě formálních řad

```
(1+z)^m Σ_{j=0}^N binom(N,j)(−z/(1+z))^j
 = (1+z)^m(1−z/(1+z))^N
 = (1+z)^{m−N}.
```

Členy s j>h nemají koeficient z^h, protože obsahují z^j;
pro j≤h≤m je zbývající koeficient přesně
binom(m−j,h−j). Všechny požadované koeficienty jsou
konečné součty a nepotřebují analytickou konvergenci.
Tím je vlastní důkaz identity citované v knize hotov.

Po dosazení dostáváme oba tištěné mezikroky:

```
f_m(N)=Σ_{h=0}^m binom(m−N,h)(N−m)^{m−h}
      =Σ_{h=0}^m (−1)^h binom(N−m−1+h,h)(N−m)^{m−h}.
```

Druhá rovnost používá binom(−t,h)=
(−1)^h binom(t+h−1,h), což plyne přímo rozepsáním
h činitelů v čitateli zobecněného binomického koeficientu.
Pro h=0 je na obou stranách1.

## Každý párovaný člen a nezápornost

Pro sudé h≤m−1 spojme h-tý a(h+1)-ní člen druhého
součtu. Jejich součet je

```
[t binom(t+h−1,h)−binom(t+h,h+1)]t^{m−h−1}
 = [t−(t+h)/(h+1)]binom(t+h−1,h)t^{m−h−1}
 = h binom(t+h−1,h+1)t^{m−h−1}.
```

Poslední rovnost plyne z
binom(t+h−1,h+1)=(t−1)binom(t+h−1,h)/(h+1).
Platí i pro t=1, kdy jsou obě strany příslušného
párovaného příspěvku0, a pro h=0, kdy příspěvek mizí.
Exponent m−h−1 je nezáporný. Pro t≥1 jsou všechny
zbývající činitele nezáporné celé hodnoty.

Je-li m sudé, zbývá nepárovaný poslední člen
binom(t+m−1,m)=binom(N−1,m). Je-li m liché,
všechny členy jsou již v párech. Výsledkem je přesně
celý vytištěný vzorec

```
f_m(N)
 = Σ_{h=0}^{m−1} h binom(N−m−1+h,h+1)
                   (N−m)^{m−h−1}[h sudé]
   +binom(N−1,m)[m sudé].
```

Koeficient h před binomickým členem je podstatný a je
zahrnut v kontrole. Nejde o pouhé konstatování, že se
alternující členy „hezky spárují“. Celá pravá strana
je nezáporná pro N>m. Spolu s oddělenými případy
N=m a m=0 to dokazuje f_m(N)≥0 pro celý požadovaný
rozsah N≥m≥0, bez nejasného dělení nulou nebo0^(-1).

## Všechny vytištěné malé polynomy

Z definice je f₀(N)=1 a f₁(N)=N−N=0. Pro m=2,
po označení t=N−1, dostáváme

```
f₂(N)=(N−1)²−N(N−1)+N(N−1)/2
     =(N−1)(N−2)/2=binom(N−1,2).
```

Pro m=3 je v nezáporném vzorci jediný nenulový pár
h=2, tedy f₃(N)=2binom(N−2,3). Hraniční N=3 dává0,
což souhlasí s přímým odděleným případem.

Pro m=4 dává tentýž vzorec

```
f₄(N)=2(N−4)binom(N−3,3)+binom(N−1,4).
```

Položme u=N−3. Oba členy po rozepsání faktoriálů mají
součet

```
u(u−1)/24 · [8(u−1)(u−2)+(u+2)(u+1)]
 = u(u−1)(3u²−7u+6)/8.
```

Také vytištěný tvar
3binom(u,4)+binom(u,2)² je

```
u(u−1)/8 · [(u−2)(u−3)+2u(u−1)]
 = u(u−1)(3u²−7u+6)/8.
```

Rovnost všech tvarů je tedy přesná. Pro N=4 má u=1
a obě strany0, takže tento hraniční bod není odvozen
z neplatného předpokladu N>m, ale přímo ověřen.
Všechny čtyři vytištěné příklady f₁,…,f₄ souhlasí.

## Všechny marginály a přesný řád nezávislosti

Zafixujme r různých jedničkových souřadnic,0≤r≤k.
Vektor s celkem j jedničkami se tak dá dokončit
binom(n−r,j−r) způsoby. Jejich celková pravděpodobnost je

```
d^(−k) Σ_{j=r}^k binom(n−r,j−r)f_{k−j}(n−j).
```

V právě dokázané normalizační identitě použijme
N=n−r,m=k−r a index h=j−r. Základ N+1−m je
znovu d, takže součet čitatele je d^{k−r} a výsledek
d^{−r}. Pro r=1 je tedy každý marginál Bernoulliho
s p=1/d; pro každé r≤k je jedničkový moment přesně p^r.

Celý důkaz MPR20 z D109 pak dává pro každý vzor
r jedniček a s nul,r+s≤k, pravděpodobnost
p^r(1−p)^s. To prokazuje úplnou k-násobnou nezávislost,
nejen shodu události samých jedniček. Pro k+1 určených
jedniček má konstrukce pravděpodobnost0, protože
nepodporuje váhu>k. Součin marginálů je však
p^{k+1}>0. Proto(k+1)-násobná nezávislost selhává.

Veškeré použité součty jsou konečné a rozdělení bylo
už před jejich použitím normalizováno a ověřeno jako
nezáporné. Tím nevzniká kruhový argument přes hypotetické
„pravděpodobnosti“ se zápornou hmotností.

## Okraje a návaznost na MPR6

Pro k=1 a libovolné n≥2 jsou a₀=0,a₁=1,d=n:
jde o rovnoměrné rozdělení vektorů s právě jednou
jedničkou. Každý marginál má1/n, ale dvě jedničky
současně jsou nemožné, jak má být.

Pro k=2 máme a₀=binom(n−1,2),a₁=0,a₂=1,d=n−1.
Nulový vektor má tedy(n−2)/(2n−2), a každý vektor
váhy2 má1/(n−1)²: přesně první distribuci MPR6.
Pro k=3 vyjdou a₀=2binom(n−2,3),a₁=binom(n−2,2),
a₂=0,a₃=1,d=n−2: přesně druhá distribuce MPR6.

V nejmenší dimenzi n=k+1 má d=2. Pro m=k−j
je N=n−j=m+1, a přímé doplnění posledního členu
binomické věty dává

```
f_m(m+1)
 = [Σ_{h=0}^{m+1}binom(m+1,h)(−1)^h 2^{m+1−h}
                                      −(−1)^{m+1}]/2
 = (1+(−1)^m)/2.
```

Je to1 pro sudé m a0 pro liché, včetně m=0.
Konstrukce je tedy rovnoměrná na2^k vektorech délky
k+1 s paritou νx shodnou s k. To dává konkrétní
existenci pro každý požadovaný k≥1 a kontroluje
nejmenší dostupný rozměr.

Pomocná identita dovoluje i n=k: pak by d=1,
všechny a_j pro j<k mizely a výsledkem by byl
konstantní vektor samých jedniček. Není to svědek
ne-(k+1)-násobné nezávislosti, protože tolik souřadnic
neexistuje; při konstrukci jsme proto výslovně použili
n≥k+1. Případy n<k do uvedeného zadání nezahrnujeme.

## Errata a bibliografická výjimka

Všech šest místních vrstev errat a tři dostupné původní
TeXy byly porovnány; oprava MPR7 nebyla nalezena.
Identita odkazovaná jako CMath(5.19) je výše dokázána
samostatně až na koeficienty, takže se nepřebírá jako
neověřené lemma. Lokální knihovní hledání neobsahovalo
Concrete Mathematics; ověření přesného čísla externího
odkazu a historické atribuce Ernstu Schulte-Geersovi
proto výslovně vynecháváme. To nevynechává žádný
matematický krok použitého důkazu.

D110 uzavírá celou úlohu7 a všechny věty odpovědi7.
File33 zůstává partial pro8–13 a file392 pro odpovědi8–19.
D109 je převzat pouze v přesném úplném rozsahu momentového
kritéria; žádný starý test, nový výpočet nebo census
neproběhl. Žádný nový nález nebo kandidát.
