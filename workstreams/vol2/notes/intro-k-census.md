# §3.1-21: úplný soupis cyklů algoritmu K

Kontrola 1. listopadu 2026: všech `10^10` desetimístných stavů bylo
zpracováno. Výsledek jsou přesně **sedm cyklů**, délek
`1,1,3,943,1024,1606,3178`. Shoduje se s opravou odpovědi z 8. 3. 1998
v `all2-prepre`, [str. 30](../images/all2-prepre-p30-direct.png).
Původní [odpověď str. 542](../images/vol2-p542.png) popisovala jen omezené
ověření domněnky o pěti cyklech. Jde o reprodukci známého pozdějšího
výsledku, nikoli nový nález. Upřesnění 6. listopadu 2026: původní zadání
výslovně žádá domněnku dokázat, nebo vyvrátit; jeho nepravdivá možnost
není sama chybou. Výsledek z roku 1998 je v erratech veden jako doplněk.

## Proč stačí projít jednodušší přechod

Nechť `g` je jeden průchod kroky K2–K12, s novým určením větve K2
z jeho vstupu; `f` je celé volání algoritmu K. Je-li `x` jeho vstup,
K1 nastaví počet průchodů na jednu plus nejvyšší desetinnou cifru,
tedy `r(x)=1+floor(x/10^9)`. Proto `f(x)=g^(r(x))(x)` a `r(x)>=1`.

Každý cyklus funkce `f` musí ležet na cyklu `g`: složením jeho
kladných skoků dostaneme `g^s(x)=x` pro nějaké `s>0`. Všechny cykly
`f` tak lze najít nejprve úplným průchodem grafu `g`, poté vyšetřením
mapy kladných skoků na jeho cyklických vrcholech. Větev K2 se při každém
průchodu skutečně určuje znovu, zatímco původní počet průchodů `r(x)`
se během jednoho volání `f` nemění.

## Úplnost průchodu a přesná aritmetika

[Program C++](../census_algorithm_k.cpp) prochází kořeny `0,...,10^10-1`.
Bitmapa eviduje navštívené stavy. Z dosud nenavštíveného kořene jde
po hranách až k navštívenému vrcholu. Je-li ten v aktuální cestě,
její koncový úsek je právě jeden nový cyklus; jinak cesta ústí do již
prozkoumané komponenty. Konečnost a jedna odchozí hrana z každého
vrcholu dokazují, že tím žádný cyklus nevynecháme ani nepočítáme dvakrát.
Čítač je zvýšen právě při první návštěvě každého vrcholu; závěrečná
kontrola vyžaduje přesně `10^10` návštěv.

Součiny až do `10^20` jsou počítány v `__uint128_t`; stavy v `uint64_t`.
Desetinné dělení je celočíselné. Úprava každé cifry v K9 je tabulkována
po pěti cifrách a nezávisí na okolní polovině. Nejde o aproximaci
plovoucí čárkou. Bitmapa zabírá 1.25 GB, běh měl jedno vlákno a sníženou
prioritu; úplný průchod trval podle interních hodin 2073.19 sekund.

Cyklů `g` je sedm, délek `2,5,7,5215,5699,8751,17345`, dohromady
37 024 vrcholů. Na každém z nich se `f` získá posunem o `r(x)` pozic
po příslušném cyklu `g`. Úplný průchod tohoto malého funkčního grafu
je druhá část programu.

## Nezávislá validace a doklady

- C++ implementace `g` před během porovnána s přímým nezávislým přepisem
  v Pythonu na 31 022 vstupech včetně hranic větví a obou malých povodí:
  [výsledek](../results/k-census-implementation-validation.json).
- Po dokončení Python znovu spočítal každou hranu všech uložených
  cyklů `g` a `f` a ověřil jejich jednoduchost a disjunktnost.
- Ze všech 37 024 cyklických vrcholů `g` nezávisle sestrojil graf `f`
  a odstraněním vrcholů s nulovým vstupním stupněm získal všechny
  cykly. Tato metoda se liší od hledání opakování v cestě v C++.
  Výsledné cykly se přesně shodují; [validace](../results/k-census-complete-validation.json).
- Úplnost desetimiliardového průchodu stojí na kontrole programu a jeho
  dokončeném běhu, nikoli na novém nezávislém druhém průchodu celé domény.
  Uložené cykly jsou certifikát správnosti jednotlivých cyklů; samy bez
  tohoto průchodu nejsou certifikát úplnosti celé domény.

[Plný výsledek](../results/k-census-full.json), [log](../results/k-census-full.log).
Řídicí tool session při pozdějším vyzvednutí vrátila kód 143; log už
obsahoval závěrečné `completed visited=10000000000` a celý uzavřený JSON.
Hodnocení dokončení proto vychází z těchto artefaktů, kontroly toku programu
a úspěšného následného validátoru; netvrdíme návratový kód 0 této session.

Samostatná [přesná inverze](intro-k-inversion.md) ověřila rovněž velikosti
597 a 128 obou povodí pevných bodů a jejich krajní hodnoty. Nový
třícyklus z errat je `0225923640 -> 2811514413 -> 0590051662 -> 0225923640`.

## Reprodukce

```sh
vol2_tmp=$(mktemp -d /tmp/knuth-vol2-XXXXXX)
g++ -O3 -std=c++17 -Wall -Wextra workstreams/vol2/census_algorithm_k.cpp -o "$vol2_tmp/census-k"
timeout 14400 nice -n 10 "$vol2_tmp/census-k" --full workstreams/vol2/results/k-census-full.json > workstreams/vol2/results/k-census-full.log 2>&1
python3 workstreams/vol2/verify_k_census.py --census workstreams/vol2/results/k-census-full.json
```

Limit čtyř hodin se týká jednoho reprodukčního běhu, nikoli celého auditu.
Úspěšný hotový běh bez nové pochybnosti neopakovat.
