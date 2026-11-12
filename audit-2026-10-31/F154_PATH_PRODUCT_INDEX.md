# F154 — součin v odpovědi 261(c) má posunutý parametr

Stav: confirmed, střední závažnost, knižní text. Sekce 7.2.2.1,
odpověď 261(c), tištěná str. 482 (PDF 502); autorův draft str. 186 (PDF 192).
Obě stránky byly vykresleny a prohlédnuty. Fyzický výtisk neověřen.

Nejkratší důkaz je případ n = 2. Trojúhelník má právě zdroje (0,1),
(1,2) a jediný cíl (1,1). Požadovaná jedna cesta má dvě možnosti,
tedy P₂ = 2. Vytištěný součin přes 1 ≤ i ≤ j ≤ k ≤ n však dává 5.
Tento protipříklad nezávisí na sporné interpretaci okrajových hran C044.

Pro zamýšlené zdroje, do kterých žádná hrana nevstupuje, je správně

    P_n = ∏_{1 ≤ i ≤ j ≤ k ≤ n−1} (i+j+k−1)/(i+j+k−2).

Proto P₁₆ = 10606175914819584. Číslo 992340657705109416 vytištěné
jako P₁₆ je P₁₇. Přesný výpočet využívá malé matice, ne rozsáhlý výčet.

Nezávislé podklady:

- Pro n = 2,3,4,5 přímé množiny cest i XCC v původním DLX6 dávají
  2,5,16,66 a shodují se v každé zvolené hraně.
- DAG dynamika spočítá A_si, počet jednotlivých cest ze zdroje s do
  diagonálního cíle t_i. Zdroje se řadí po vnějším okraji a cíle po diagonále.
  Rovinné uspořádání znemožňuje překřížené párování disjunktních cest.
  Pfaffian matice Q_ij = Σ_(s<t)(A_si A_tj − A_sj A_ti) tedy podle
  zrušení protínajících se dvojic počítá rodiny disjunktních cest.
  Při lichém počtu cílů doplníme řádek/sloupec se součty Σ_s A_si.
  Uložené přesné matice pro n = 16,17 dávají uvedená celá čísla.
- [Knuthova původní poznámka z února 2019](https://cs.stanford.edu/~knuth/papers/noncr-conj.pdf)
  používá n cest ve čtverci (n+1) × (n+1), s produktem končícím n.
  Kniha používá n−1 cest ve čtverci n × n. Poznámka a její dodatek
  přímo dokládají Beluhovovu bijekci a vysvětlují posun parametru.
- [Stembridge, Adv. Math. 83 (1990), věta 3.1](https://www.mat.univie.ac.at/~kratt/bedlewo/stemb-nonint.pdf)
  je obecný primární podklad Pfaffianové metody; příslušná strana 106
  byla prohlédnuta. Výše popsaná aplikace na tuto síť je naše odvození.

Soubory: `results/zdd261_264/path-pfaffians.json`, `triangle261-*.json`,
`cases-checked.json`; program `check_zdd261_265_cases.py`.
Dokončené výpočty se neopakují. Hodnoty M₁₆ = 3803972 a 7 gigamemů
nebyly reprodukovány; není doloženo, zda i u nich autor zaměnil parametr.

Šest relevantních historických/aktuálních vrstev errat bylo prohledáno
podle obou číslování, autora, tématu a čísel; odpovídající oprava nenalezena.
Otisky a kontexty jsou v `results/zdd261_264/errata-search.json` a
`errata-supplement.json`. To není tvrzení o prvenství.
