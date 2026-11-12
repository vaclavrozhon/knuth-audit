# MPR 130–137: důkazy a protipříklady

## F010 a F011: Cauchyho rozdělení, odpověď 130(e), str. 393

Z transformace `Z=pX+qY` plyne společná hustota dvojice `(Z,Y)`

```
1 / [π² p (1+((z−qy)/p)²)(1+y²)].
```

**F010:** Ve vytištěném jmenovateli je `(z−qy/p)²`, tedy p dělí jen qy.
Má dělit celý rozdíl z−qy. Pro `p=q=1/2,z=1,y=0` dává tisk `1/π²`,
zatímco změna proměnné z předcházejícího řádku dává `2/(5π²)`.

**F011:** Další integrál už používá správné závorky, ale výsledek postrádá π:

```
∫[−∞,∞] dy / [(p²+(z−qy)²)(1+y²)] = π / [p(1+z²)],  p+q=1.
```

Pro `p=q=1/2,z=0` je integrál `4∫(1+y²)^(−2)dy=2π`; vytištěný
výsledek dává 2. Substituce `y=tan t` dává `∫cos²(t)dt=π/2`, takže jde
o přesný elementární protipříklad.

Nezávislý symbolický součet reziduí pro obecná kladná p,q vychází
`π(p+q)/(p((p+q)²+z²))`. Ve splývajícím případě pólů výsledek platí
spojitostí; přímý výpočet výše jej pokrývá také. Dvanáct numerických
integrálů s 50 ciframi souhlasí s opraveným výrazem.

Oba zápisy byly potvrzeny v PDF a autorově Pre-Fascicle 5A, str. 49:
`images/vol4b-p393.png`, `images/fasc5a-p49.png`. V erratech 4B ani
Fascicle 5 odpovídající opravy nalezeny nebyly. Stabilita Cauchyho
rozdělení je pravdivá; chyby jsou v mezikrocích jejího důkazu.

## 131: diskrétní Cauchyho rozdělení souhlasí

Je-li `c=1/(π coth π)`, pak pro nenulové celé n platí
`Pr(X+Y=n)=2c/(n²+4)`. Racionální rozklad s
`A=1/(n²+4)`, `B=2/(n(n²+4))` je

```
1/[(1+k²)(1+(n−k)²)]
 = (A+Bk)/(1+k²) + (A+B(n−k))/(1+(n−k)²).
```

Po symetrickém součtu a limitě liché členy vymizí. Pro n=0 dává
diferencování známého součtu `Σ(a²+k²)^(−1)=π coth(πa)/a` jiný výsledek:

```
Pr(X+Y=0) = c² [π coth π + π² csch² π]/2
          = 1−c(π coth 2π−1/2) ≈ 0.162282600666356.
```

V knize je správně **polovina** `Pr(2Z=n)` pro nenulové sudé n; OCR
zlomek na první čtení znejasnilo. Žádný nový nález v 131.

## F012 a F013: hypergeometrické rozdělení, odpověď 132, str. 393

Urna obsahuje N kuliček, z toho K zelených; vybíráme n bez vracení.
Příklad `N=4,K=2,n=1` je férové Bernoulliho rozdělení: vytvářející funkce
je `(1+z)/2` a rozptyl `1/4`.

**F012:** Horní parametr hypergeometrické funkce má být `−n`, nikoli
vytištěné `−N`. Tisk v našem příkladu dává
`(1/2) F(−2,−4;2;z)=1/2+2z+z²`, což ani nemá součet koeficientů 1.
Správně je `F(−K,−n;N−K−n+1;z)` s vytištěným prefaktorem.
Toto porovnání se týká regulárního rozsahu `n≤N−K`; singularity zápisu
při jiných parametrech zde neklasifikujeme jako samostatnou chybu.

**F013:** Ve vzorci pro rozptyl chybí faktor K. Správně

```
Var(Q) = n K (N−n)(N−K) / [N²(N−1)].
```

V uvedeném příkladu tisk dává `1/8`. Obecný vzorec lze přímo odvodit ze
součtu indikátorů: každý má rozptyl `p(1−p)` a každá dvojice kovarianci
`−p(1−p)/(N−1)`, kde `p=K/N`.

Přesné součty všech 3306 distribucí pro `2≤N≤20`, `0≤K,n≤N`
potvrdily střední hodnotu, opravený rozptyl a oba vytištěné vzorce pro
módy. Z nich 1767 regulárních vytvářejících polynomů odpovídá opravenému
hypergeometrickému parametru. Výsledky: `results/cauchy_hypergeometric.json`.

**Doklad je zatím pouze vykreslené PDF.** Stažený autorův draft 5A končí
úlohou 131 a tyto pozdější úlohy neobsahuje. V aktuálních ani historických
erratech nebyly příslušné opravy nalezeny; fyzická kniha nebyla prohlédnuta.

## F014: nesprávná pravděpodobnostní mez v 134(b), str. 27 a 394

Vezměme jedinou událost A s pravděpodobností `1/2` a dva nezávislé vzorky
velikosti `m=1`. Jejich empirické pravděpodobnosti jsou dva nezávislé
férové bity. Pro `ε=9/10` je tedy

```
Pr(|P̂′−P̂″|>ε) = 1/2 > 2 exp(−81/50) ≈ 0.3957973982.
```

Není to numerický artefakt: z kladných členů exponenciální řady plyne
`exp(81/50)>1+81/50+(81/50)²/2+(81/50)³/6=1160197/250000>4`.
U větších vzorků tvrzení také selhává: `m=100,ε=1/5,p=1/2` dává
přesnou binomickou pravděpodobnost přibližně `0.00363494795`, zatímco
vytištěná mez je přibližně `0.000670925256`.

Při podmínění na sdružený vzorek nechť K značí celkový počet výskytů A
a k jejich počet v prvním vzorku. Potom

```
|P̂′−P̂″| = |k/m−(K−k)/m| = 2|k−K/2|/m.
```

V odpovědi tedy musí být práh `εm/2`, nikoli `εm`. Postupem podle
nápovědy 132 dostaneme mez `2 exp(−ε²m/2)`. Pro nepodmíněnou
pravděpodobnost lze z nezávislosti všech 2m bitů odvodit i silnější
`2 exp(−ε²m)`. Původní `2 exp(−2ε²m)` je však nepravdivá.

### Proč 134(c) přesto platí

Při `E(X)>ε` vyberme podle X konkrétní událost j, která tuto odchylku
dosahuje. Nezávislý druhý vzorek má podmíněně pravděpodobnost alespoň
`1−1/(mε²)≥1/2`, že pro tuto j udělá chybu nejvýše `ε/2`.
Tedy `Pr(E(X)>ε)≤2 Pr(max_j |P̂′_j−P̂″_j|>ε/2)`.

Po podmínění na 2m pozorování je nejvýše `Δ_(2m)(A)` různých sloupců.
Každý z nich má při náhodném rozdělení pozorování na dvě poloviny
pravděpodobnost odchylky nejvýše `2 exp(−mε²/8)`, podle právě opravené
podmíněné meze. Sjednocení událostí proto dává vytištěný výsledek
`4 Δ_(2m)(A) exp(−mε²/8)`. Volba j v prvním kroku závisí na X;
v krátkém vytištěném důkazu není tato závislost vysvětlena.

Znění zadání i odpovědi bylo vizuálně ověřeno v PDF. Autorův stažený
draft tyto úlohy neobsahuje. Errata 4B a Fascicle 5 odpovídající opravu
neobsahují. Program `check_two_sample_bound.py` ukládá přesné zlomky,
důkaz exponenciálního porovnání a 300 dalších kontrol opravené meze.

## F015: mezikrok důkazu o mediánu, odpověď 137(d), str. 395

Pro `c<m` definujeme `Δ_x=|x−c|−|x−m|`. Je-li `x<m`, správně je
`Δ_x=c−m+2 max(0,x−c)`, nikoli vytištěné `c−m+2(x−c)`.
Vezměme X s pravděpodobnostmi `Pr(X=−1)=1/4`, `Pr(X=1)=3/4`.
Jeho jediný medián je m=1. Pro c=0 a x=−1 je skutečná hodnota −1,
ale vytištěná rovnost dává −3.

Věta o minimalizaci očekávané absolutní odchylky i navazující dolní mez
jsou správné; oprava se týká pouze tohoto mezikroku. Zatím doklad PDF,
bez fyzického výtisku a bez nezávislého autorova PS pro tuto pozdější úlohu.
V erratech odpovídající oprava nalezena nebyla.

Při čtení 137(f) bylo odmítnuto podezření vzniklé OCR: odmocnina skutečně
patří k větvi `x≤3`, následovaná větví x. Uvedený příklad C-funkce tímto
podezřením napaden není.
