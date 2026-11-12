# V2-C0154: ostrá nerovnost v opravě odpovědi 22

**Confirmed.** Oprava z 3. 5. 2002 k §4.5.4, str. 661, řádky 3–4
odpovědi 22, zavádí indikátor `[n nonprime]`: jedničku pro složený
vstup a nulu pro prvočíslo. Indikátorem násobí obě strany ostré
nerovnosti. Pro každé prvočíslo se tím dostává nepravdivé `0 < 0`.

Nejmenší dovolený příklad je `n=3`. Algoritmus P nikdy nechybuje,
takže `p_3=0`. Přijme obě základny 1 a 2, tedy `b_3=2`.
Opravený řetězec má hodnoty `0 = 0 < 0`.

Minimální oprava: změnit `<` mezi dvěma výrazy s indikátorem na `<=`.
Pro složené vstupy je nerovnost stále ostrá; pro prvočíselné je rovnost.
Závěr `p_n < 1/4` se nemění, jak ukazuje vlastní obecný důkaz
v [primality-probabilistic.md](primality-probabilistic.md), §3.

Původní erratum je vizuálně doloženo na
[PDF straně 41](../images/all2-prepre-primality-p41.png).
První dotisk na str. 661 ještě tuto konkrétní chybu nemá, protože
výslovně omezuje původní výpočet na ne-prvočísla. Oprava řeší jeho
jiné formulační problémy, ale přidává tento nový hraniční problém.

Všechny čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
a aktuální `err2.textxt` prohledány 3. 11. 2026 podle stránky,
úlohy, indikátoru a tématu; další oprava nenalezena. Fyzický nejnovější
dotisk a priorita nálezu nejsou ověřeny. Návrh hlášení není odeslán.
