# C032 — „zbývající 1 %“ u Drive Ya Nuts

**Kandidát, nízká závažnost.** TAOCP 4B, odpověď 7.2.2.1–137(c),
tištěná strana 452 / PDF 472. Kniha uvádí podíly přibližně 93 %, 5 %,
1 % a zbývající 1 % podle počtu řešení 0, 1, 2 a alespoň 3.

Úplný výpočet pro všech **59 487 568 920** sedmic různých matic dává
pro poslední kategorii přesně **205 252 200 sedmic**, tedy
**0,3450337671 %**. Pravděpodobnost jednoznačnosti je 5,3456885493 %.

| Kategorie | Knižní údaj | Přesný podíl, zaokrouhlený na 6 míst |
|---|---:|---:|
| Bez řešení | asi 93 % | 93,195198 % |
| Jedno řešení | asi 5 % | 5,345689 % |
| Dvě řešení | asi 1 % | 1,114080 % |
| Tři a více | zbývající 1 % | 0,345034 % |

Kniha pracuje s hrubými procenty a poslední kategorii doplňuje do
100 %. Proto nález není veden jako potvrzená matematická chyba.
Otázkou pro posouzení je, zda čtenář chápe 1 % jako samostatný odhad
vzácných případů, nebo jako zbytek po hrubém zaokrouhlení ostatních řádků.
Přesnější čtyřčíselný údaj je 93,20 %, 5,35 %, 1,11 %, 0,35 %
(samostatné zaokrouhlení dává 100,01 %).

Doklady:

- [Vykreslená původní strana 452](images/vol4b-p452.png).
- [Stejné znění v autorově draftu z roku 2019](images/fasc5c-p156-nuts137.png).
- [Úplný přesný cenzus a důkaz úplnosti](results/nuts137/census/accepted.json).
- [Podrobná metoda a všechny zdroje](NUTS137_NOTES.md).
- [Šest vrstev errat, znovu ověřených 2. listopadu 2026](results/nuts137/errata-check.json).

Celý cenzus má 5 623 238 tříd podle přejmenování čísel. U každé třídy
je druhým úplným čítačem ověřen počet řešení a všemi 720 přejmenováními
ověřen stabilizátor i kanonické minimum. Samostatný výčet přes šest
sdílených hran dává stejný celkový počet řešení. Vedle toho souhlasí
454 úplných kontrolních výčtů DLX2/Python z milionového vzorku a
dalších pět příkladů zahrnujících maximum 20 řešení.

Příkaz `python3 accept_nuts137_census.py` ověří uložené koncové výsledky,
hashe a agregaci celého cenzu. Nespouští znovu hledání. Pro fyzické
vydání zatím nemáme samostatný doklad; lokální PDF a autorův původní
draft mají shodné znění. Nic nebylo Knuthovi odesláno.
