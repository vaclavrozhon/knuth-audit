# §4.5.4: raná historie prvočísel na 407 a 412

Průběžný blok4.11.2026 místního času. Obě Knuthovy stránky vizuálně
přečteny. **C0186confirmed** opravuje překlad Mersennovy časové
poznámky; **C0187candidate** zaznamenává podezření u dvojice z1460.
Celý historický blok ještě není uzavřen.

## Matematický rámec a Mersenne1644

Pro celá u,v>1 platí

    2^(uv)−1 = (2^u−1)(1+2^u+...+2^((v−1)u)).

Tedy je-li 2^n−1 prvočíslo, je i n prvočíslo. Tato nutná podmínka
na407 je správná. **Mersennovo číslo** zde znamená 2^n−1;
**dokonalé číslo** znamená číslo rovné součtu svých kladných
vlastních dělitelů. Pro prvočíselné 2^p−1 dává Euclidův vzorec
2^(p−1)(2^p−1) dokonalé číslo: součet všech dělitelů je
(2^p−1)2^p, tedy dvojnásobek čísla samotného.

Získán původní tisk *Cogitata physico-mathematica*, ETH-Bibliothek,
Rar1522, [identifikátor](https://doi.org/10.3931/e-rara-15453).
Vizuálně přečten titul1644 (obraz5) a celý §XIX (začíná na obrazu27,
pokračuje na28). Výklad Mersennových jedenácti očekávaných případů
souhlasí se standardní interpretací uvedenou v knize: osm malých
případů do p31 a další67,127,257. Originál pracuje s dokonalými
čísly a starší konvencí exponentů; neobsahuje přímo dnešní seznam
ve tvaru moderní formule. Knuthova slova „in essence“ jsou proto
přiměřená. Některé tiskové chyby Mersennova seznamu nejsou novými
chybami v Knuthovi.

Závěrečná věta §XIX ale má celé století místo veškerého času;
přesné doklady a nejmenší oprava jsou v
[C0186](C0186-mersenne-century.md). V roce1644 nebyla dána
matematická nemožnost testu v libovolně dlouhém čase.

## Powers1911 a1914

Přečten celý [primární přepis článku1911](https://t5k.org/mersenne/literature/powers.txt),
*The Tenth Perfect Number*, AMM18, November1911,195–197.
Oznamuje prvočíselnost2^89−1 a obsahuje tabulku Lucasovy rekurence
končící nulou při88.členu. Datace na konci je Denver, June1911;
Knuth uvádí rok časopisu, takže zde není spor. Článek také cituje
Rouse Ballovu domněnku o záměně67za61; existence takové spekulace
je tím doložena dobovým pramenem.

[Přepis oznámení1914](https://t5k.org/mersenne/literature/powers2.html),
*On Mersenne's Numbers*, Proc. London Math. Soc.(2)13,xxxix,
končí nulovým106.členem a závěrem, že2^107−1 je prvočíslo.
Knuthovo „three years later“ tedy odpovídá uvedeným publikacím.
Jde o pozdější HTML/textové přepisy těchto původních sdělení,
nikoli získané facsimile časopisu. Matematická prvočíselnost obou
čísel již byla samostatně certifikována v `primality-lucas.md`;
rekurence se znovu nepočítaly. Všechny pomocné historické výroky
Powersových článků nejsou předmětem tohoto bloku.

## Dosud otevřené zdroje

- Eulerovo1772: archiv identifikuje E461, svazekza1772 vydaný1774,
  ale vlastní původní listy nebyly staženy. Rozdíl roku svazku
  a vydání sám nedokazuje chybu data objevu.
- Pervushin1883, citace1953p559, a Kraitchik1922/1924p21 dosud
  bez přímého přečtení rozhodných původních listů.
- Picutti1989: nově zjištěný rozpor abstraktu s17/19 je
  [C0187candidate](C0187-medieval-perfect-numbers.md). Williams1998
  Chapter2 doplněný v erratu2005 zůstává rovněž nepřečten.
- Obecné tvrzení o téměř nepřerušené historické řadě rekordů
  se zde neprohlašuje za úplně nezávisle rekonstruované.

Záznamy neúspěšných přístupů jsou uloženy; nedostupný PDF se
neoznačuje za přečtený. Další části §4.5.4 mají vlastní přesný
rozsah v `coverage.json`; tento blok nemění47/47úloh.
