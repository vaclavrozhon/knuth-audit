# Přesný běh Algorithm M: SAT 349–350, 353 a text u(150)

Kontrola 31. 10. 2026. Vzorce odpovědi349 jsou správné. Nový F043
je obrácené slovní porovnání rychlosti v hlavním textu na str.273.

## F043: Case1 je pomalejší

První věta odstavce na str.273 říká, že algoritmus běží rychleji
v Case1 než v Case2. Má být `slower`, případně prohodit označení
případů v této jedné větě. Následující vysvětlení i odpověď349 již
správně označují Case1 za horší případ.

Case1 odstraňuje sousední bity10, Case2 odstraňuje11. Při sedmi
férových bitech a výběru první vadné dvojice jsou přesné průměry
počtu resamplování **7** a **1139/729≈1,5624**. Rozptyly jsou
42 a1139726/531441. Byly odvozeny přímo ze128stavových řetězců,
bez převzetí vzorců z knihy, a pak s knihou porovnány.

Věta je vizuálně stejná v našem PDF a v autorově Pre-Fascicle6A
z23.9.2015, str.89. Ve stažených veřejných erratech nebyla oprava
nalezena. Tvrzení o „praxi“ se týká rychlosti vyjádřené počtem
resamplování, jak ji analyzuje celá tato pasáž; nejde o měření
strojového času konkrétní implementace.

## Úplné vytvářející funkce349

Pro každý řetězec x se ze skutečných čtyř výsledků prvního
resamplování sestavila rovnice

`g_x(z)=z Σ_y g_y(z)/4`, nebo `g_x(z)=1` u hotového řešení.

Graf přechodů se rozložil do silně souvislých komponent a soustavy
se vyřešily přesně nad tělesem racionálních funkcí Q(z). Všech
**256 funkcí** pak znovu splnilo všechny stavové rovnice.
Výsledky pro jednotlivé řetězce jsou v
`results/resampling_all_pgfs.json`.

Průměrováním přes rovnoměrný počáteční stav dostáváme

```
G₁(z)=1/((2−z)(8−8z+z²)),
G₂(z)=(1088−400z+42z²−z³)/(4−z)^6.
```

Souhlasí i oba konkrétní řádky odpovědi349 a seznam všech šesti
možných jmenovatelových faktorů pro Case1. V Case2 mají všechny
jmenovatele jen mocniny4−z. Výpočet je symbolický, ne interpolace
z několika numerických bodů.

Samostatně se z rovnic prvních a druhých momentů zkontrolovaly
oba případy pro n=1,…,9, celkem **2044 stavů**. V Case1 platí
průměr `n(n−1)/6` a rozptyl `(n+3)(n+2)n(n−1)/90` přesně.

## Obecné odvození momentů Case1

Události10 tvoří krajní rozdělení pro cestu: sousední události
nemohou nastat současně, nesousední používají disjunktní bity.
Möbiův polynom pro n−1událostí je

`P_n(z)=Σ_k binom(n−k,k)(−z/4)^k`.

Rekurence P_n=P_(n−1)−(z/4)P_(n−2), P₀=P₁=1 dává také

`P_n(z)=2^(−n) Σ_j binom(n+1,2j+1)(1−z)^j`.

Proto `P_n(1)=(n+1)/2^n`,
`−P'_n(1)/P_n(1)=n(n−1)/6` a
`P''_n(1)/P_n(1)=n(n−1)(n−2)(n−3)/60`.
Derivací G_n(z)=P_n(1)/P_n(z) dostaneme oba momenty z knihy.
To dokazuje obecný výsledek, který konečný výčet jen kontroluje.

## Nezávislé dvoustavové odvození Case2

Při výběru levé první dvojice11 se algoritmus posouvá zleva doprava.
Předchozí bit před opravovanou dvojicí musí být0, takže opravou
nemůže vzniknout nová vadná dvojice vlevo. Opakované resamplování
11 končí jednou z00,01,10; každá má vytvářející funkci z/(4−z).

Podle posledního již zpracovaného bitu0nebo1 má zpracování dalšího
férového bitu přechodovou matici

```
T(z) = [ 1/2                    1/2            ]
       [ (4+z)/(2(4−z))         z/(2(4−z))     ].
```

Počáteční řádek je(1/2,1/2) a závěrečný sloupec(1,1).
Stopa matice je2/(4−z), determinant−1/(4−z), tedy

`(4−z)G_n(z)=2G_(n−1)(z)+G_(n−2)(z), G₀=G₁=1`.

Tato rekurence dává funkci z odpovědi349 pro n=7. Její derivace
dává `3m_n=1+2m_(n−1)+m_(n−2)` a explicitně

`m_n=(n−1)/4 + (1−(−1/3)^(n−1))/16`.

Pro druhý faktoriální moment h_n platí
`3h_n=2m_n+2h_(n−1)+h_(n−2)`. `check_resampling_transfer.py`
porovnává maticový výpočet s rekurencí do n=40 a s nezávislými
stavovými momenty do n=9. Case2 má tedy lineární průměrnou dobu,
zatímco Case1 kvadratickou; směr F043 je potvrzen i asymptoticky.

##350: geometrické opakování a hvězdicový graf

Při jednotlivých opravách je počet pro proměnnou k geometrický
počet neúspěchů s parametrem ξ_k. Nezávislé proudy náhodných bitů
dávají součin generujících funkcí `(1−ξ_k)/(1−ξ_k z)`.
Průměr je Σξ_k/(1−ξ_k), rozptyl Σξ_k/(1−ξ_k)².
Všech pět explicitních průměrů v odpovědi350(a) souhlasí.

Když se vždy opravuje celé sjednocení, jde o geometrický počet
neúspěšných vektorů s pravděpodobností
`ξ=1−Π_k(1−ξ_k)`. Proto jsou průměr a rozptyl ξ/(1−ξ),
respektive ξ/(1−ξ)². U ξ_k=1/(n+k) součin teleskopuje na1/2;
u ξ_k=1/(n+k)² na(2n+1)/(2n+2). To dává přesné řádky(iv),(v).
U konstantních parametrů jsou zbývající součiny přímo mocniny.

Pro případy(ii)–(v) je max ξ_k=O(1/n), takže poměr rozptylu
a průměru v(a) je1+O(1/n), jak kniha tvrdí. Ostatní asymptotické
řádky v(b) plynou z expanze log(1−x). Zkontrolováno bylo přesně
**500 parametrických soustav**, n=1,…,100.

Pro hvězdu je `M_G=Π_k(1−ξ_k)−ξ=1−2ξ`. Každý indukovaný
podgraf se středem má alespoň tuto hodnotu; bez středu má kladný
součin. Proto p∈R právě pro ξ<1/2. Kritérium v350(c) je správné,
i když odkazuje na obecně chybné cografové tvrzení343: pro tuto
konkrétní hvězdu ho dokazuje výše uvedený přímý argument.
Výčet případů(ii),(iii),(v) se vztahuje k n≥2; pro n=1 jsou
(ii),(iii) na hranici. Otázka350 žádá asymptotiku, takže tento
malý parametr nevedeme jako samostatný nález.

##353: počet řešení

Case1 má n+1neklesajících řetězců0^k1^(n−k). Case2 má F_(n+2)
řetězců bez sousedních jedniček, podle rozkladu na začátek0 nebo10.
Polynom cesty dává v obou případech stejnou základní mez n+1.
Case2 však má prázdný lopsidependency graf: všechny klauzule
jsou stejného znaménka a vyhnutí dalším vadným11 nemůže zvýšit
pravděpodobnost nové11. Lepší mez je `2^n(3/4)^(n−1)`.
Přímý výčet řešení do n=9 souhlasí se všemi těmito tvrzeními.

## Navazující kontrola

Úloha 351, součinová mez pro stopy a očekávaný počet oprav v Theorem K
jsou nyní ověřeny v [LOPSIDEPENDENCY_NOTES.md](LOPSIDEPENDENCY_NOTES.md).
Odkaz na FKG zůstává jen otázkou výkladu C009; výsledek je správný.
