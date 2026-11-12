# Langfordovy páry: ceny a lexikografické extrémy

## F077: údajné lexikografické maximum není maximální

Strana 476, odpověď 7.2.2.1–229, označuje posloupnost (108) za
lexikograficky největší Langfordovo párování řádu 16. Stejné tvrzení je
v původním autorově Pre-Fascicle 5C, strana 180. Obě stránky byly
vykresleny a přečteny; v all4b ani all4f5 nebyla nalezena odpovídající oprava.

Skutečné maximum je:

```
16 14 15 11 9 7 13 4 2 12 10 2 4 7 9 11
14 16 15 8 13 10 12 5 6 1 3 1 8 5 3 6
```

Každé i se vyskytuje právě dvakrát ve vzdálenosti i+1. Na čtvrté pozici
je 11, kdežto (108) má 9; první tři pozice jsou totožné. To samo stačí
jako protipříklad. Maximálnost nové posloupnosti navíc nezávisle potvrzují
přímé DFS v lexikografickém pořadí a inkrementální SAT, který postupně
vylučuje všechny větší hodnoty v každém dosud nevyplněném slotu.

Lexikografické minimum v knize je správné. Jeho tři ceny jsou
5240, 119192 a 60324. Nové maximum má ceny 3888, 76800 a 38876.
Tvrzení o minimálních cenách (108) je jiná otázka; F077 je nevyvrací.

Doklady: [přímý výčet](check_langford_costs.py),
[SAT ověření](verify_langford_lex.py),
[výsledky DFS](results/langford_costs/basics.json),
[úplná stopa SAT prefixů](results/langford_costs/sat-lex.json),
[PDF](images/vol4b-p476.png), [PS](images/fasc5c-p180.png).

## Identity 226–228 a rozsah výpočtu

Pro n=3,4,7,8,11 byly vyčísleny všechny posloupnosti a ověřeny identity
pro obrácení, obě identity prvních výskytů a uvedené četnosti pro n=7.
Obecné identity plynou přímo z nahrazení pozice j hodnotou 2n+1−j
nebo ze součtů prvních a druhých mocnin všech 2n pozic.

Všechny tři minimální ceny pro n=16 potvrdily původní DLX5 a nezávislý
HiGHS: 3708, 68880 a 37552. První dvě mají přesně 12 016 řešení a jejich
optimální množiny jsou totožné; třetí má právě jediné řešení (108).
Následující vyšší ceny jsou 3720, 69048 a 37556.

Nezávislý validátor přečetl všech 163 997 průběžně přijatých modelů DLX5,
ověřil rozestupy, přesné celočíselné ceny i jedinečnost a porovnal celé
optimální množiny. HiGHS našel shodné optimum s nulovou hlášenou mezerou;
jeho numerické meze nejsou samostatným přesným certifikátem. Přesné
úplné prohledání větví zajišťuje DLX5. Celkový počet všech párování řádu16
jsme zde znovu nevyčíslovali.

Doklady: [kontrola modelů](verify_langford_costs.py),
[výsledky](results/langford_costs/verified.json), jednotlivé `.log`, `.out`
a `*-milp.json` v adresáři `results/langford_costs/`.
