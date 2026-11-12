# V3-C0026 — celkové časy M se spojováním:44.62N a41.89N

**confirmed / low**,2026-11-07. Tištěná101/file112, poslední odstavec:
časy po doplňujícím programu§5.2.1-35 mají být **44.62N,41.89N**,
nikoli44.99N,41.95N. Třetí údaj52.74N je správně zaokrouhlen.
Sazba101 i celý kód35 na625/file636 zobrazeny. Chybný je číselný
koeficient očekávaného času, nikoli třídění nebo jeho lineární řád.

Nechť E je počet prázdných z M seznamů. V kódu35 jsou četnosti/ceny:

    inicializace24–25                  2
    hlavička/test26–27                 3M
    připojení28 (ST3)                  2(M−E)
    sken29–31                         4N
    vnější cyklus32–33                 2M.

Proto **T_join=4N+7M−2E+2**. Původní klíče jsou iid s rovnoměrným
přiřazením intervalům; každá buňka je prázdná s pravděpodobností
(1−1/M)^N. Linearita dává E E=M(1−1/M)^N, bez předpokladu
nezávislosti prázdných buněk. Pro M=N/α tedy E T_join/N→
4+7/α−2e^(−α)/α.

Celý obecný důkaz37–40 v `insertion-proof-m-analysis-101-102-37-40.md`
nezávisle dává pro samotné M koeficient

    t(α)=31+7α/4+4/α−(3/α)∫₀^α(1−e^(−x))/x dx.

Při α=1 je t=34.3602012021… a spojování10.2642411177…,
celkem **44.6244423198…**. Při α=2 je t=34.5211049657… a
spojování7.3646647168…, celkem **41.8857696825…**. Krátké přesné
racionální Taylorovy intervaly s prvním vynechaným členem dokazují
zaokrouhlení; nejsou to numerické odhady z náhodných vstupů.
Pro α=10 zůstává52.7360494456…→52.74.

Vytištěné dva výsledky odpovídají odečtení pouze E místo2E.
Nejde o jiný povolený MIX model: právě ST3 vynechané prázdnou
buňkou stojí2u; totožný model dává správných94u u16 klíčů v36,
kde jsou všechny buňky neprázdné. Optimalizace s uloženými konci
seznamů není program35, jehož dodatečnou cenu text uvádí.

Pět vrstev v `sources/multiple-list-total-time-errata-review.json`
neobsahuje opravu těchto koeficientů. Známé LD4(2008), faktoriály37
a průměrný čas38(2000), typografie625/626 a historický chybějícíδ
jsou jiné opravy. Potvrzení je v dodaných zdrojích, bez záruky prvenství.
