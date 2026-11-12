# §4.5.4–27: úplnost seznamů a původní prameny

> Sekvenční doplnění6.11.2026: uvedená uzavřenost platí pro zde popsané důkazy, certifikáty a externí seznam; celá27 má nyní partial kvůli zvlášť vymezené záruce hledání svědka v jednoslovním rozsahu.

Audit 3. listopadu 2026. Úloha 27 je uzavřena v následujícím rozsahu:
vlastní obecný důkaz a 57 konkrétních prvočíselných certifikátů jsou v
[primality-deterministic.md](primality-deterministic.md). Úplnost seznamu
exponentů do 300000 je **externí výsledek projektu Proth Search**;
nevydáváme ji za vlastní nový vyčerpávající výpočet.

## 1. Primární seznam Ballingera a Kellera

Přímý [projektový seznam](http://www.prothsearch.com/riesel1.html),
uložený v [HTML](../sources/prothsearch-riesel1-http.html), uvádí své
sestavitele Raye Ballingera a Wilfrida Kellera a aktualizaci 18. července
2026. V úvodu přesně definuje zápis `[Lim]`: část seznamu před touto
značkou je úplná pro exponenty `n<=Lim`. Podtržené `<` v původním HTML
znamená neostrou nerovnost; zploštěný text tento detail ztrácí.

Pro koeficient `k=3` je uvedena hranice 23737900, pro `k=5` hranice
9000000. Obě převyšují knižních 300000. Přesné stažené bajty jsou zachovány v gzip; čitelná kopie HTML má jen
sjednocené konce řádků a odstraněné koncové mezery. Záznam také popisuje následné
systematické kontroly projektu PrimeGrid. Tento audit nepřezkoumává
všechny historické výsledkové soubory těchto projektů.

[Porovnávací program](../verify_proth_sources.py) načetl oba řádky
přímo z uloženého HTML a porovnal exponenty nejvýše 300000 s naším
již dokončeným souborem certifikátů. Shoda je přesná: **36 hodnot pro
k=3 a 21 hodnot pro k=5**. [Výsledek](../results/proth-source-comparison.json)
obsahuje celé porovnávané seznamy a otisk zdroje. Prvočíselné testy se
neopakovaly. Původní knižní seznam pro k=3 má o jeden exponent méně;
**54792** doplňuje již známé erratum z 29. července 2024.

Proth Search byl přes HTTPS nedostupný kvůli chybě TLS; veřejná původní
adresa HTTP fungovala. OEIS posloužilo k nalezení primárního odkazu;
samotnou shodu se sekundární posloupností nepoužíváme jako důkaz úplnosti.

## 2. Proth 1878: konečně získaný originál

Veřejný archiv obsahuje [číslo z 9. prosince 1878](https://archive.org/details/comptes-rendus-hebdomadaires-academie-des-sciences_1878-12-09_87_24).
V [lokálním PDF](../sources/proth-1878-cr87-24.pdf) je tištěná strana 926
na straně souboru 38; byla vizuálně přečtena celá Prothova poznámka.
[Obraz](../images/proth-1878-p926.png) potvrzuje název, svazek 87,
stranu 926 a třetí kritérium. Článek jen uvádí tvrzení, ne jejich důkazy.

**Oprava našeho dřívějšího úsudku:** v původní sazbě bodu III skutečně
stojí `N=m*2^n`, bez potřebného `+1`. Nejde tedy pouze o chybu přepisu
na Wikisource, jak jsme předběžně předpokládali. Také záhlaví tiskne
iniciálu E. Tento zdrojový detail nepovažujeme za chybu Knuthovy správné
formy `k*2^n+1` ani za nový nález v jeho knize. Naše matematická kontrola
používá výslovně úplnou formu a vlastní důkaz.

První stažené archivní číslo z 18. listopadu obsahovalo strany 765–812,
ne hledanou poznámku; jeho nerelevantní PDF a text nebyly ponechány.
Neúspěšné přímé pokusy a správné stažení zaznamenává
[historie získávání](../sources/proth-history-downloads.json).

## 3. Robinson 1958 a rozsah bibliografické kontroly

OEIS poskytuje dvě různé kopie. [První soubor](../sources/robinson-1958-oeis-compilation.pdf)
je převážně fax pozdějších Rieselových tabulek z roku 1994 a teprve
na straně souboru 33 obsahuje Robinsonovu tištěnou 673. Nelze jej
popisovat jako úplný Robinsonův článek. [Druhý soubor](../sources/robinson-1958-selected.pdf)
obsahuje sedm fotografií stran 674–680; část sousední 681 je oříznutá.

Přímo přečteny rozhodné části stran 673, 674 a 676. Autor uvádí výpočty
na SWAC v letech 1956–1957, popis Prothova testu a tabulku exponentů.
Na 676 výslovně zaznamenává dokončené hranice `n<1280` pro k=3
a `n<2005` pro k=5 a kontrolu druhým během. Řádek k=3 na 674 končí
534, řádek k=5 končí 1947, ve shodě s příslušnými prefixy knižního
seznamu. Další části článku jsou pouze navigačně prohlédnuty; všechny
jeho věty a historické tabulky zde znovu nedokazujeme.

Cormackův [autorský seznam](https://cormack.uwaterloo.ca/PAPERSx.html)
potvrzuje práci s H. C. Williamsem, Math. Comp. 35 (1980), 1419–1421.
Dubner–Kellerův článek má DOI
[10.1090/S0025-5718-1995-1270618-1](https://doi.org/10.1090/S0025-5718-1995-1270618-1).
Youngovu dokončenou citaci 67 (1998), 1735–1738, uvádí knižní erratum
z 23. listopadu 1998; souhlasí s DOI
[10.1090/S0025-5718-98-00989-2](https://doi.org/10.1090/S0025-5718-98-00989-2)
a bibliografickým záznamem. Plné texty těchto tří prací nebyly získány.
Jejich konkrétní původní výpočetní logy nepoužíváme jako ověřená data;
úplnost potřebného rozsahu je doložena současným primárním seznamem §1.

Archivované Kellerovy stránky o faktorech Fermatových čísel z roku
2001 jsou uloženy jako historické podklady. Samy nedokazují úplnost
seznamu všech prvočísel `k*2^n+1`, a proto nenahrazují §1.

Žádný nový knižní nález tímto zdrojovým blokem nepřibyl. Platí dříve
potvrzená výjimka N=3 (**C0157**) a známé doplnění 54792. Fyzický
nejnovější dotisk ani prvenství nálezu nejsou ověřeny; nic se neodeslalo.
