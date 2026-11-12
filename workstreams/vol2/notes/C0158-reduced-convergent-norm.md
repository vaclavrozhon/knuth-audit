# V2-C0158: přesná normová rovnost neplatí pro redukované P

**Stav: confirmed.** TAOCP 2, §4.5.4, krok E3 na str. 398;
táž rovnost na str. 400. Odpověď úlohy 4.5.4-14 na str. 660
potřebuje v důkazu stejný nezkrácený čitatel. Původní sazba
všech tří stran byla zobrazena. Závěr se týká našeho třetího
vydání, prvního dotisku 1997, a dostupných errat, nikoli
ověřeného posledního tištěného dotisku nebo priority nálezu.

E1 výslovně definuje P jako čitatel konvergenty modulo N a E5
jej takto redukuje. E3 přesto tvrdí přesnou celočíselnou rovnost
`P²-kNQ²=(-1)^S V` pro vhodné celé Q nesoudělné s P.

Protipříklad je přímo v tabulce na téže straně:

```
N=197209, k=1, P=159316, V=720, S=0.
Q²=(159316²-720)/197209=128704.
358²=128164 < 128704 < 128881=359².
```

Žádné takové celé Q proto neexistuje. Přesná konvergenta má
čitatel 750943 a jmenovatel 1691:

```
750943²-197209*1691²=720,
750943 mod 197209=159316.
```

Algoritmus E tím není vyvrácen: správná kongruence
`P²=(-1)^S V (mod N)` nadále platí. Oprava má rozlišit
nezkrácený čitatel `p_n` a uložený zbytek P. Přesnou rovnost
a nesoudělnost je třeba psát pro `p_n,q_n`; P stačí v závěrečné
kongruenci modulo N. Pouhá výměna rovnítka za kongruenci
modulo N by nestačila pro následný argument modulo prvočísla
z faktorové báze, která N obecně nedělí.

Oprava E1 z 2. července 2001 na str. 22–23 `all2-prepre`
byla vizuálně přečtena. Pouze mění začátek rekurze; uvedený
řádek i problém zůstávají. Dne 3. listopadu 2026 byly prohledány
`all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální TeX
`err2.textxt` podle stran, E3, příslušné rovnosti a konvergentů.
Oprava tohoto rozlišení v nich nebyla nalezena.

Dva nezávislé modely — tištěná rekurze E a přesné konvergenty
s dělením `(D-C²)/V` — dávají uvedené hodnoty. Přímé celočíselné
čtverce uzavírají protipříklad bez numerické aproximace.
Doklady: `verify_factoring_contfrac.py`, checkpoint
`counterexamples` v `results/factoring-contfrac.json`,
`images/vol2-p398.png`, `images/vol2-p400.png`,
`images/vol2-p660.png` a `sources/factoring-contfrac.json`.
