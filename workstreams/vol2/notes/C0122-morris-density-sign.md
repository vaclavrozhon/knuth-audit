# V2-C0122 — znaménko Morrisovy hustoty v erratu 2016

Stav: **confirmed**. Náhradní odpověď §4.5.2-34 k tištěné straně645,
erratum z 8. února2016, `all2-pre.pdf`, str.15. Originál byl zobrazen:
v citaci Morrise se píše, že jeho funkce xi(z) je G'(z).

Kniha na348–349 definuje G jako limit pravděpodobnosti, že poměr menšího
a většího vstupu je alespoň x. Jde o klesající funkci ocasu s G(0)=1,
G(1)=0. Pro hustotu xi téhož rozdělení tedy platí

```text
G(x) = integral from x to 1 of xi(t) dt,
G'(x) = -xi(x),
xi(x) = -G'(x).
```

V Morrisově větě2 je xi normalizována integrálem1 a je kladná na(0,1].
Vizuálně přečteno v původním preprintu arXiv1409.0729v1, str.7;
stejná normalizace i kladnost jsou ve vydaném článku na str.80,
ověřeno v indexovaném textu primárního institucionálního PDF.
Preprint a publikovanou verzi nezaměňujeme: úplný vydaný PDF nebyl
stažen a má například opravené znaménko v jiné rovnici(8).
[Preprint autora](https://arxiv.org/abs/1409.0729),
[institucionální záznam vydané verze](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/A-rigorous-version-of-RP-Brents/99514592602346).

Rovnost xi=G' je tedy v přímém rozporu se znaménkem i normalizací:
integrál G' přes(0,1) je -1, zatímco integrál xi je1. V koncovém bodě
navíc kniha sama má G'(1)=-lambda<0 a Morris xi(1)=lambda>0.
Po opravě na xi(z)=-G'(z) je převod konzistentní. Holomorfní pokračování
do pravé poloroviny má stejný vztah identitou analytických funkcí.

Kontrola všech čtyř vrstev errat2026-11-02: `all2-prepre` obsahuje
starší odpověď Vallée; `all2-pre` zavádí tento převod; `all2` a `err2`
opravují roku2022 jen rozsah Morrisova článku73–145 na73–143.
Oprava znaménka nebyla nalezena. Nález se týká převodu značení,
nikoli platnosti Morrisovy analýzy nebo hlavní asymptotiky knihy.
Aktuální fyzický dotisk a prvenství neověřeny, návrh neodeslán.
