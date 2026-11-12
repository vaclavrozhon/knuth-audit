# V2-C0191: posunutý index v události úplného poklesu stupňů

**confirmed**, poslední odstavec odpovědi na §4.6.1–4, horní část 673.

Zadání a předchozí část odpovědi označují stupně zbytků jako
`n>n1>...>nt>=0`, po nichž následuje nulový zbytek stupně −infinity.
Pravděpodobnost `(1−1/p)^n` patří události t=n, tedy
`n_j=n−j` pro `1<=j<=n`. V posledním odstavci je místo toho
`n_(j+1)=n_j−1` pro `1<=j<=t=n`.

Poslední rovnost tak odkazuje na stupeň až za posledním nenulovým
zbytkem. Při n=1 má zamýšlená událost jediný nenulový zbytek stupně
n1=0, následovaný nulou; napsaná podmínka by požadovala n2=−1.
Podle konvence knihy však nulový polynom má stupeň −infinity.

Přímá oprava je `n_j=n−j for 1<=j<=t=n`; případně lze zavést n0=n
a psát sousední poklesy pro 0<=j<n. Hodnota pravděpodobnosti i tři
střední hodnoty v hlavní odpovědi jsou správné. Jejich obecný důkaz
a 13678 přesných případů jsou v poznámkách k bloku a výsledcích.

## Podklady a rozsah

Kontrola 4. listopadu 2026. Sazba 3. vydání, 1. dotisku (1997) byla
vizuálně přečtena; strana souboru je tištěná strana plus 12. Všech pět
vrstev errat (`all2-prepre`, `all2-pre`, `all2`, `err2`, `err2.textxt`)
bylo prohledáno podle stránek i matematických výrazů; relevantní oprava
nebyla nalezena. Log je `sources/polynomial-division-basic-errata.txt`.
Nejnovější fyzický dotisk ani historické prvenství nálezu nejsou ověřeny.
Žádné hlášení nebylo odesláno.
