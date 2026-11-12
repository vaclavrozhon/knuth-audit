# §3.1-20: přesná inverze algoritmu K

Kontrola 1. listopadu 2026. Potvrzeno všech 597 vstupů končících v bodě
6065038420, jak uvádí [odpověď na str. 542](../images/vol2-p542.png).
Potvrzeno také všech 128 vstupů končících v bodě 5008502835 z opravy
odpovědi §3.1-21 z 8. března 1998 (`all2-prepre`, strana knihy 542).
Jde o kontrolu známých výsledků, nikoli o nový nález.

## Co se invertuje

Položme `M=10^10`, `B=10^5`. Stavem je celé číslo `0<=x<M`, včetně
případných úvodních nul v desetinném zápisu. Funkce `g(x)` znamená jeden
průchod K2–K12; K13 se zde interpretuje jako návrat výsledku tohoto průchodu.
Celý algoritmus K definuje funkci

```text
f(x) = g^(1+floor(x/10^9))(x),
```

kde exponent označuje počet opakovaných aplikací funkce, nikoli mocninu
číselné hodnoty. Počet průchodů se určí z původního vstupu v K1.
K2 volí první vykonaný krok `3+d`, kde `d=floor(x/10^8) mod 10` je druhá
cifra zleva. Za ním se vykonají všechny kroky až po K12.

Pro každý výstup `y` program postupně invertuje K12, K11, ..., K3. Po
inverzi kroku `s` uloží pouze ty kandidáty `x`, jejichž druhá cifra volí
právě `s`. Tím pokrývá všechny možné vstupy do větvení K2. Sjednocení je
množinové, takže opakovaně nalezený vstup se započte pouze jednou.

## Úplnost jednotlivých inverzí

Všechny níže uvedené kandidáty omezujeme podmínkou `0<=x<M`.

* K3: pro `y>=M/2` jsou předchůdci `y` a `y-M/2`; jinak žádný.
* K4: hledají se všechna `x` s `floor(x^2/B) mod M=y`, postupem v dalším
  odstavci.
* K5 a K8: násobení číslem 1001001001 modulo `M` je bijekce. Jeho inverzní
  násobitel je 9999999001; součin těchto dvou čísel je 1 modulo `M`.
* K6: kandidát `M-y` platí pro `y>0` a `M-y>=10^8`. Druhý kandidát
  `y-9814055677` platí pro `9814055677<=y<9914055677`.
* K7: výměna dvou pěticiferných polovin je sama sobě inverzí.
* K9: každá výstupní nula má vstupní cifru 0 nebo 1; cifra `d` od 1 do 8
  má vstupní cifru `d+1`; výstupní cifra 9 není možná. Kartézský součin
  těchto možností dává všechny vstupy.
* K10: kandidát `y+99999` musí ležet v `[B,M)`. Druhá větev existuje právě
  tehdy, když `y-99999` je čtverec celého čísla `x` v `[0,B)`.
* K11: výstup musí ležet v `[10^9,M)`. Předchůdci jsou `y` a všechna jeho
  celočíselná dělení mocninami deseti. Po prvním dělení už je hodnota menší
  než `10^9`, takže ji normalizace opravdu vrátí až na `y`. Nulový vstup
  není dosažitelný z algoritmu K, viz [důkaz ukončení](intro-cycles.md).
* K12: hledají se všechna `x` s `floor(x*(x-1)/B) mod M=y`.

Pro K4, respektive K12, označme příslušný kvadratický výraz `q(x)`.
Podmínka na výstup je přesně disjunkcí celočíselných intervalů

```text
B*(y+k*M) <= q(x) <= B*(y+k*M)+B-1,   k=0,1,2,... .
```

Program projde každý takový interval až do maxima `q(M-1)`, najde první
možný celočíselný kořen a projde všechny následující kořeny uvnitř intervalu.
Výraz `x*(x-1)` je rostoucí od `x=1`; případ `x=0` se přidá samostatně.
Odmocnina v plovoucí čárce slouží pouze jako počáteční odhad: výsledek se
opraví pomocí přesných nerovností `r^2<=z<(r+1)^2` v 128bitové aritmetice.
Všechna použitá čísla se do tohoto typu vejdou. Zaokrouhlovací chyba tedy
nemůže vynechat kořen ani přidat falešný kořen.

## Od zpětného uzávěru k úplnému povodí

Povodím bodu `t` rozumíme všechny vstupy, jejichž iterace funkce `f`
někdy dosáhne `t`. Začneme množinou `{t}` a opakovaně přidáváme všechny
předchůdce podle `g`, dokud žádný nový nepřibude. Úplnost inverze dokazuje,
že výsledná množina `S` obsahuje právě stavy dosahující `t` iterací `g`.

Protože každá aplikace `f` je kladný počet aplikací `g`, celé povodí podle
`f` je podmnožinou `S`. Opačné zahrnutí není automatické: přeskakování po
cyklu může některé body míjet. Proto samostatný Pythonový validátor pro
**každý** vrchol `S` ověřuje iteraci skutečné funkce `f` až do `t`. Ověřuje
také `f(t)=t`. Obě zahrnutí společně dokazují přesnost hledaného povodí.

| Pevný bod | Počet vstupů | Nejmenší vstup | Největší vstup | Nejvíce iterací `f` do bodu |
|---|---:|---:|---:|---:|
| 6065038420 | 597 | 0009612809 | 9995371004 | 11 |
| 5008502835 | 128 | 0008502835 | 9944390948 | 4 |

Certifikáty obsahují všechny inverzní hrany. Nezávislý dopředný validátor
zkontroloval všech 725 hran a všechny jejich vrcholy; úplnost se opírá o
výše popsaný výčet intervalů a větví, nikoli pouze o úspěch validátoru.

## Reprodukce

```sh
vol2_tmp=$(mktemp -d /tmp/knuth-vol2-XXXXXX)
g++ -O3 -std=c++17 -Wall -Wextra workstreams/vol2/invert_algorithm_k.cpp -o "$vol2_tmp/invert-k"
"$vol2_tmp/invert-k" 6065038420 workstreams/vol2/results/k-basin-6065038420.json
"$vol2_tmp/invert-k" 5008502835 workstreams/vol2/results/k-basin-5008502835.json
python3 workstreams/vol2/verify_intro_extra.py
```

Zdroj: [invert_algorithm_k.cpp](../invert_algorithm_k.cpp).
Certifikáty: [597 vstupů](../results/k-basin-6065038420.json),
[128 vstupů](../results/k-basin-5008502835.json).
Validátor: [verify_intro_extra.py](../verify_intro_extra.py),
[výsledek](../results/intro-extra.json).

Tato kontrola sama neurčuje všechny ostatní cykly K. Jejich úplný soupis
je samostatná položka V2-X0008; byl dokončen a nezávisle validován,
viz [úplný soupis](intro-k-census.md).
