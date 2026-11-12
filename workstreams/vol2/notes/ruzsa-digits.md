# §4.1-32: současně omezené trojkové a pětkové cifry

Kontrola 2. listopadu 2026. Zadání na straně 213 žádá nekonečně mnoho
celých čísel, která mají v základu 3 jen cifry 0 a 1 a v základu 5
jen cifry 0, 1 a 2. Odpověď na straně 610 odkazuje na Math. Comp. 29
(1975), 84–86; jde o relevantní část článku Erdőse, Grahama, Ruzsy
a Strause, který jako celek zabírá strany 83–92. **Rozsah 84–86 není
chybná citace:** označuje přesně důkaz použitého výsledku.

Primární [článek](https://static.renyi.hu/~p_erdos/1975-27.pdf) získán
z Erdősova archivu; strany 84–85 a dokončení první věty na 86 přečteny
vizuálně. První věta pokrývá i obecné dvojice základů `p,q` a meze cifer
`A,B` s `A/(p-1)+B/(q-1) >= 1`. Níže je úplná specializace potřebná
pro úlohu, doplněná explicitním důkazem ukončení. Zbývající věty článku
nejsou v tomto bloku auditovány. Žádný nový nález.

## 1. Zaokrouhlení na přípustné trojkové číslo

Nazveme číslo **trojkově přípustným**, má-li v základu 3 jen cifry 0,1;
**pětkově přípustným**, má-li v základu 5 jen cifry 0,1,2. Jde vždy
o nezáporná celá čísla s konečným zápisem.

Pro každé celé `x >= 1` existuje trojkově přípustné `U` v `[x,2x)`.
Důkaz: seřazená trojkově přípustná čísla vzniknou nahrazením základu 2
základem 3 v obyčejných binárních číslech. U dvou sousedních hodnot
`V<U` proto existuje `m >= 0` a nezáporný vyšší prefix `H` tak, že

```
V = H + (3^m-1)/2,     U = H + 3^m.
```

Platí `U <= 2V+1`. Je-li `U` nejmenší přípustné číslo alespoň `x`
a není-li `U=x`, pak `V<x`, a tudíž `U<=2x-1`. Je-li `U=x`, je
závěr bezprostřední. Algoritmus pro `U` najde nejvyšší trojkovou cifru 2,
přenese ji do nejbližší vyšší nuly a všechny nižší cifry vynuluje.

## 2. Jeden opravný krok zachovávající trojkové cifry

Nechť `N` je trojkově přípustné a má v pětkovém zápisu nejvyšší chybnou
cifru na pozici `j`, tedy cifru 3 nebo 4. Předpokládejme, že nad ní
existuje cifra menší než 2. Označme `i` nejbližší takovou pozici nad `j`
a `b_i` její cifru. Mezi `j` a `i` jsou samé dvojky. Napišme

```
N = P + T,      P = floor(N/5^i) 5^i,      T = N mod 5^i.
M_i = (5^i-1)/2 = (22...22)_5   (i cifer).
```

První odlišná cifra ocasu `T` od samých dvojek je větší, takže `T>M_i`.
Nejnižší nenulová trojková pozice `m` čísla `N` určuje rozdíl k jeho
přípustnému předchůdci:

```
S = (3^m+1)/2.
```

**Je-li `T>=S`,** položíme `N_new=N-S`. Je trojkově přípustné, zachovává
všechny pětkové cifry na pozicích alespoň `i` a je alespoň `P`.

**Je-li `T<S`,** položíme `x=5^i-T`. Z celočíselnosti a `T>M_i` plyne
`1<=x<=M_i`; z `M_i<T<S` plyne `5^i<3^m`. Podle části 1 vybereme
nejmenší trojkově přípustné `U>=x`, takže

```
x <= U < 2x <= 5^i-1 < 3^m.
```

Číslo `N` má pod pozicí `m` trojkové nuly. Přičtení `U<3^m` tedy
nezpůsobí trojkový přenos a `N_new=N+U` zůstane trojkově přípustné.
Jeho pětkové cifry nad `i` se nemění, cifra `b_i` vzroste o 1 a nový
ocas pod `i` je `U-x`, splňující `0<=U-x<M_i`. Ten je buď přípustný,
nebo před jeho první chybnou cifrou stojí cifra menší než 2.

Oba kroky tak zachovají možnost další opravy a nikdy neklesnou pod `P`.

## 3. Proč se opravy zastaví

Pro nepřípustný aktuální výsledek definujme trojici

```
(i, 2-b_i, N).
```

Porovnáváme ji lexikograficky, tedy podle první rozdílné složky.
Po každém kroku přísně klesne:

- Při odečítání je nová pozice `i_new<=i`. Pokud je stejná, její cifra
  se nezmění a klesne `N`.
- Při přičítání a `i_new=i` vzroste `b_i`. Jakmile dosáhne 2,
  první nižší cifra odlišná od 2 je menší než 2, takže buď jsme hotovi,
  nebo `i_new<i`.

Všechny složky jsou nezáporná celá čísla. Lexikografické pořadí na
pevně dlouhých takových trojicích nedovoluje nekonečný přísný sestup.
Algoritmus proto skončí číslem přípustným v obou základech. Tento
argument nevyžaduje, aby samotné `N` při všech krocích klesalo.

## 4. Nekonečně mnoho různých výsledků

Existují libovolně velké exponenty `a` takové, že nejvyšší pětková cifra
`3^a` je 1. Stačí, aby zlomková část `a log_5(3)` ležela v otevřeném
intervalu `(0,log_5(2))`. Číslo `log_5(3)` je iracionální, jinak by
kladné mocniny 3 a 5 byly stejné.

Použitou hustotu násobků iracionálního čísla lze získat přímo z principu
přihrádek: pro libovolné `epsilon>0` najdeme kladné `q`, jehož násobek
má vzdálenost `delta` od celého čísla v `(0,epsilon)`. Násobky `q` pak
obcházejí kružnici kroky `delta` v jednom ze dvou směrů; prvních
`floor(1/delta)+1` bodů má mezery nejvýše `delta`. Totéž platí po posunu
libovolným počátečním násobkem. Každý otevřený interval je tedy navštíven
i po libovolně pozdním začátku, a tudíž nekonečně často.

Pro takový počáteční vstup `N=3^a` označme `r` jeho nejvyšší pětkovou
pozici. Počáteční cifra 1 stojí nad každou případnou chybnou cifrou,
takže předpoklad opravného kroku platí s `i<=r`. Vyšší prefix na pozici
`r` se nikdy nezmenší; výsledek je alespoň `5^r`. S rostoucími `a`
roste i `r`, tedy výsledky nejsou omezené. To je požadovaná konstrukce
nekonečně mnoha různých čísel. Lze ji provádět čistě celočíselným
prohledáváním mocnin 3, bez výpočtu logaritmů.

## 5. Propojení s binomickými koeficienty

Známý doplněk errat z 22. července 2024 odkazuje na úlohu 1.2.6-11
a OEIS A129508. Souvislost je přesná: exponent prvočísla `p` v
`binom(2N,N)` je počet přenosů při sčítání `N+N` v základu `p`.
Krátké odvození: pro součet cifer `s_p(N)` dává součet počtů násobků
`p,p^2,...` ve faktoriálu

```
v_p(N!) = (N-s_p(N))/(p-1),
v_p(binom(2N,N)) = (2s_p(N)-s_p(2N))/(p-1).
```

Každý přenos sníží součet cifer právě o `p-1`. U lichého `p` nenastane
žádný přenos právě tehdy, když každá cifra `N` je nejvýše `(p-1)/2`.
Pro `p=3,5` dostaneme přesně zadání. Odkaz na úlohu svazku 1 byl
porovnán s jejím textem a odpovědí na straně 484; zde používáme vlastní
odvození, nikoli závěr cizího pracovního proudu.

## 6. Reprodukovatelné kontroly

[Ověřovač](../verify_ruzsa_digits.py) porovnal 100000 zaokrouhlení
s nezávislým seřazeným výčtem. Opravný krok prošel pro 8814 přípustných
vstupů s nejvýše 14 trojkovými ciframi a nejvyšší pětkovou cifrou 1:
49 přičtení, 8590 odečtení a 175 již hotových vstupů. V každém kroku
se kontroluje zachování cifer a sestup trojice z části 3.

Pro všechny vhodné mocniny `3^a`, `1<=a<=40`, vzniklo 18 samostatných
konstrukcí. Největší doložený výsledek je `16416111755922375250`,
získaný devíti kroky z `3^40`. Všechny jeho cifry v obou soustavách,
stejně jako u dalších příkladů, jsou uloženy v
[výsledcích](../results/ruzsa-digits.json).

Z původního zobrazení [OEIS b-file](https://oeis.org/A129508/b129508.txt)
bylo uchováno prvních 48 položek. Každá splňuje obě ciferné podmínky
a nezávislý faktoriálový výpočet valuací. Úplný nezávislý průnik dvou
výčtů do 20011 obsahuje právě prvních 47 uvedených položek. Úplných
1000 položek b-file není vydáváno za ověřené: přímé stažení vrátilo
HTTP 403 a pozdější otevření nebylo dostupné. [Metadata](../sources/oeis-A129508.json)
toto omezení výslovně zaznamenávají.

Běh 31544 dokončil matematické konstrukce a zastavil se na chybějícím
souboru b-file. Po uložení dostupného výňatku byl obnoven pouze poslední
blok, exit 0; úspěšné bloky se neopakovaly. [Log](../results/ruzsa-digits.log)
zachovává oba výsledky. Všechny relevantní vrstvy errat byly prověřeny
v rámci soupisu §4.1; doplněk 2024 je správný.
