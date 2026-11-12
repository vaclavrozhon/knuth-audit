# Partridge: čtverce s předepsanými násobnostmi

Kontrola 1. 11. 2026. Úlohy 154–156, str. 144 a 460; hlavní text
str. 92. Jde o dva různé inventáře: běžný má k čtverců velikosti k×k,
„authentic“ má n+1−k takových čtverců.

## 154: všechny čtvercové plochy autentického inventáře

Platí P(n)=n(n+1)^2(n+2)/12. Je-li P(n)=m^2, pak
3n(n+2)=(6m/(n+1))^2. Celočíselná racionální druhá mocnina je druhou
mocninou celého čísla, které je zde dělitelné třemi. Tedy
n(n+2)=3u^2 a (n+1)^2−3u^2=1. Obráceně každé takové řešení dává
P(n)=((n+1)u/2)^2; součin (n+1)u je sudý, jak plyne z parity
Pellovy rovnice.

Všechna nezáporná řešení x^2−3u^2=1 jsou x+u√3=(2+√3)^k.
Úplnost plyne z klesání (x,u)→(2x−3u,2u−x), které pro u>0 vede
k menšímu nezápornému u a zachovává rovnici. Označíme-li řešení
(a_k,b_k), dostáváme pro sudé a liché k právě formule knihy:

```
a_(2m)−1 = 6 b_m^2,
a_(2m+1)−1 = (a_m+3b_m)^2.
```

Jde tedy o úplnou klasifikaci. Přímý test všech n do milionu je
samostatně uložen v `results/partridge/pell.json`.

## 155: úplný výčet autentického n=6

Nezávislý program `partridge.cpp` vyplňuje první volnou buňku shora
zleva a zkouší všechny zbývající velikosti čtverce. Nepojmenovává
stejně velké kopie, takže každé geometrické pokrytí vzniká právě jednou.
Kontrola na 34 malých inventářích do 5×5 souhlasí s původním DLX3
ve všech 521 modelech. Každý model kontroluje ještě samostatný Python
výpočet buněk, násobností, symetrií a skóre.

Pro inventář (6,5,4,3,2,1) na desce 14×14 vzniklo přesně **60 568**
pokrytí, tedy tiskovaných 8·7571. Skóre má minimum **5** a maximum
**35**, jak uvádí kniha. Minimum nastává v 64 polohách, maximum v 16.
Všech 60 568 modelů bylo uloženo a samostatně ověřeno; histogram skóre
se v obou implementacích shoduje. Hledání navštívilo 47 998 224 uzlů.

Přesný počet tříd při osmi symetriích čtverce je **7 585**: 7 557 tříd
velikosti 8 a 28 tříd velikosti 4. Samotný zápis 8·7571 tedy neznamená,
že všechna pokrytí mají osm různých symetrických obrazů. Kniha uvádí
správný celkový počet; tento rozdíl nehlásíme jako chybu.
Vytištěné ilustrace extrémních pokrytí nebyly v tomto bloku přepsány;
vlastní nezávislé extrémní modely jsou součástí uloženého výčtu.

## 156: běžné n=8 — dokončeno

Pro n=8 je deska 36×36. Jediný jednotkový čtverec omezujeme na
r<18 a c≥35−r; tato výseč obsahuje alespoň jeden obraz každé polohy
při D4. Na diagonále neaplikujeme další pravidlo pro kontext jednotky.
Výpočet našel přesně 2 566 poloh, z toho 468 s jednotkovým dílkem
na diagonále, a po úplné kanonizaci 2 332 tříd. Každá třída má osm
různých obrazů, takže celkem je 18 656 poloh. Všech 2 566 modelů bylo
samostatně geometricky ověřeno; všechny počty souhlasí s knihou.

Naše hledání navštívilo 15 107 260 582 uzlů za přibližně 550 sekund.
To není stejná varianta jako Knuthův menší strom. Úplnost rozdělení
plyne z toho, že každou buňku sudého čtverce lze symetrií převést
do r<18,c≥35−r. Každé pokrytí má jedinou jednotku. Kanonizace pak
odstraní dvojí reprezentanty na diagonále.

MCC vstup má 1 304 položek a 7 367 možností. Přímo počítaných výskytů
položek je 198 386. Číslo 205 753 uvedené v knize obsahuje navíc jednu
oddělovací položku (spacer) na každou možnost: 198 386+7 367=205 753.
Přesně tak počítá „entries“ také původní DLX3 při načítání vstupu
(last_node−last_itm). Tento rozdíl konvence nehlásíme jako chybu.

## 157: optimum pro n=6 a n=7

K vyloučení pokrytí s méně než osmi prázdnými buňkami stačí vyloučit
přesné pokrytí inventářem (5,1,3,4,...,n). Při ztrátě plochy menší než
8 nelze vynechat žádný čtverec velikosti ≥3 ani oba čtverce 2×2.
Jsou-li přítomny oba, jeden nahradíme čtyřmi jednotkovými buňkami.
Případné mezery také doplníme jednotkami. Tím bychom z každého lepšího
pokrytí dostali uvedený inventář.

Úplný výčet tohoto inventáře skončil bez řešení:

| n | Deska | Navštívené uzly | Výsledek |
|---:|---:|---:|---|
| 6 | 21×21 | 21 084 107 | žádné řešení |
| 7 | 28×28 | 3 344 467 429 | žádné řešení |

Naopak inventář (9,0,3,4,...,n) řešení má pro oba rozměry. Z devíti
jednotek ponecháme jednu jako skutečný dílek a ostatních osm polí
vyprázdníme. Samostatná geometrická kontrola potvrdila oba uložené
svědky. Jejich hledání skončilo po prvním řešení (`complete:false`),
nejde o úplné počty optimálních pokrytí. Maxima pokryté plochy jsou
433 a 776. Vytištěné obrázky 157 nebyly přepsány.

Úplnost backtrackingu plyne z první volné buňky: čtverec, který ji
pokryje, musí mít právě tam levý horní roh, jinak by překryl už
obsazené buňky. Zkoušíme všechny zbývající velikosti a každé pokrytí
tím vzniká právě jednou.

## 158 a F068: lepší obdélník pro n=6

Vykreslený prostřední obrázek odpovědi 158 má 30×15: pravý sloupec
obsahuje tři čtverce 5×5 a horní pás má šířky 7+6+6+6+5. Jeho plocha
je 450 a devět buněk je prázdných. Text všechny tři obrázky prohlašuje
za optimální. V PDF str. 461 i původním PS str. 165 je stejné tvrzení.
V all4b ani historickém all4f5 (str. 269) příslušná oprava není.

Pro n=6 však existuje **28×16 = 448**, pouze se sedmi prázdnými buňkami.
Všech 21 skutečných dílků má požadované násobnosti a jejich 441 buněk
bylo nezávisle ověřeno geometrickým výčtem. Souřadnice jsou v
`results/partridge_rectangles/n6-better-witness.json` a v ASCII návrhu
`knuth-report-f068-draft.txt`. Obrázek řešení:

![Lepší obdélník 28×16](results/partridge_rectangles/n6-better-28x16.svg)

Tento explicitní svědek sám vyvrací tvrzenou optimalitu původního
obrázku, nezávisle na dalších negativních výpočtech.

### Úplné hledání menších obdélníků

`pack_squares.cpp` používá první volnou buňku a ukládá již vyvrácené
stavy: zbývající násobnosti, číslo první nevyplněné řady a obsazení
nejvýše k dalších řad. Dřívější řady už jsou plné; žádný dříve položený
čtverec nemůže zasahovat hlouběji než k−1 řad pod aktuální řadu. Tento
klíč proto úplně určuje zbývající podproblém. Omezení velikosti cache
jen zastaví ukládání dalších stavů, nevylučuje žádné větve.

Na 56 malých obdélníkových inventářích souhlasí výsledek s původním
DLX3, a to s cache i bez ní. Bylo skutečně využito 27 zásahů cache;
nejde jen o test cest bez opakovaných stavů. Každý nalezený model
kontroluje samostatný geometrický výčet buněk a násobností.

Prázdná pole se reprezentují jako dodatečné jednotky. Pro plochu A
je jejich celkový počet 1+A−(n(n+1)/2)^2; jednu jednotku považujeme
za skutečný dílek, ostatní za mezery. Tato záměna zachovává existenci
pokrytí oběma směry.

Pro každé celé A od součtu ploch dílků do testovaného horního odhadu
se prohlédnou všechny dělitele šířky n≤w≤√A. Menší šířka nepojme
největší čtverec; otočení desky nevynechá další případ.

- n=5: svědek 26×9 = 234, všech 10 menších obdélníků vyvráceno.
- n=6: svědek 28×16 = 448, všech 7 obdélníků s plochou pod 448
  vyvráceno. Ostatní tři rozměry s plochou 448 také nemají řešení.
- n=7: svědek 44×18 = 792, všech 7 menších obdélníků vyvráceno.

Nalezená minima jsou tedy 234, 448 a 792. Pro n=5 a n=7 se shodují
s obrázky knihy. Všech sedm negativních případů n=6 navíc dokončil původní autorův
DLX3 se stejným výsledkem: žádné řešení. Jednotlivé běhy trvaly od
0,04 do 7,27 sekundy, žádný neskončil časovým limitem. Vstupy a logy
jsou archivované a `n6-dlx3-summary.json` je shrnuje. Minimum 448
proto potvrzují dvě odlišné implementace úplného hledání.
