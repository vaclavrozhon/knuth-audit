# V2-C0017: podezřelá znaménka v §3.3.1-(16)

**Stav: candidate.** Dvě dvojice čísel na str. 52 reprodukujeme
s opačnými znaménky. Výchozí stavy a začátek konkrétního historického
experimentu však tato strana neuvádí. Nenavrhujeme zatím definitivní
opravu a netvrdíme, že jsou chybné všechny grafy nebo všechna znaménka.

## Co přesně se porovnává

Pro seřazená čísla z_1,...,z_n v [0,1] definujeme

```
K+ = sqrt(n) * max_j (j/n - z_j),
K- = sqrt(n) * max_j (z_j - (j-1)/n).
```

To je knižní konvence (11), (13) po transformaci distribuční funkcí.
Pro maximum pěti nezávislých rovnoměrných čísel je tato funkce x^5.

Použijeme parametry a seedy výslovně uvedené na str. 47:

| Generátor | X_0 | a | c | m |
|---|---:|---:|---:|---:|
| B | 0 | 3141592653 | 2718281829 | 2^35 |
| F | 314159265 | 2^18+1 | 1 | 2^35 |

Rekurence je X_(j+1)=(aX_j+c) mod m. Z prvních 1000 členů X_1,...,X_1000
utvoříme 200 nepřekrývajících se maxim pěti hodnot X_j/m a zvýšíme je
na pátou. Výsledné statistiky jsou:

| Data | vlastní K+_200 | vlastní K-_200 | kniha K+_200 | kniha K-_200 |
|---|---:|---:|---:|---:|
| B | 0.816965302084... | 0.476919712327... | .477 | .817 |
| F | 0.057940305557... | 2.818900656745... | 2.819 | .058 |

Navíc chí-kvadrát s deseti stejně pravděpodobnými kategoriemi vychází
přesně 9.4 a 39.3, jako na str. 54. Shoda zaokrouhlených čísel i druhého
testu je silným vodítkem ke shodě vstupních dat, ale sama je nedokazuje.

## Nezávislé ověření výpočtu

`reproduce_general_test_figures.py` používá celočíselnou rekurenci,
racionální transformaci a vzorec pro uspořádané hodnoty.
`verify_ks_figure_signs.py` ověřuje každý z 1001 stavů B/F samostatným
umocněním afinního zobrazení a počítá supremum přímo v levých a pravých
limitech empirické distribuční funkce. Pro F navíc kontroluje uzavřený
vzorec (q=2^18):

```
X_j = X_0 + j*(q*X_0+1) + binom(j,2)*q  (mod 2^35).
```

Platí, protože q^2 je dělitelné 2^35. Přesná data i výsledky jsou
v `results/general-test-figures.json` a `results/ks-figure-signs.json`.
Oba běhy úspěšně dokončeny; nejsou to dvě opakování stejného algoritmu.

## Co zůstává neurčeno

Strana 52 popisuje dvacet dílčích testů po deseti pozorováních a následný
test jejich statistik. Zveřejněné vnější hodnoty se při našich
konvencích nereprodukují přesně. Pro F mají vnitřní K- kvalitativně
stejnou odchylku jako obrázek 4(c), vnitřní K+ opačnou. Prostá záměna
všech vnitřních znamének však nespraví B.

Neznáme původní zdrojový program, případné permutování skupin, přesnou
implementaci distribuční funkce ani výchozí místo tohoto experimentu.
Prověřeny začátky X_0 a X_1, oba směry vnitřní statistiky i dva vzorce
pro její distribuci. Výsledky se nezamlčují a žádná konvence není
dodatečně vydávána za doložené zadání. Pro potvrzení by pomohla původní
data nebo explicitní popis jejich výběru.

## Sazba a errata

Původní [str. 52](../images/vol2-p052.png) vizuálně zkontrolována;
zaokrouhlená čísla výše jsou skutečně ve vzorci (16). Stejné označení
má [vydavatelský náhled 2026](../images/publisher-preview-p052.png),
PDF strana 68. To dokládá sazbu, nikoli samo o sobě chybu.
Dne 1. listopadu 2026 prohledány všechny vrstvy `all2-prepre`,
`all2-pre`, `all2`, `err2` i aktuální TeX podle str. 52 a čísel .477,
.817, 2.819. Oprava (16) nenalezena. Fyzický nový tisk neověřen.
