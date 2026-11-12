# Čebyševova nerovnost: obsah ověřen, bibliografie otevřena

V1-X0751, 2. listopadu 2026. Matematický obsah původního článku
je checked; celá §1.2.3–31 zůstává partial kvůli přesnému významu
ročníku a datace v erratech. Nový kandidát chyby se zatím nezakládá.

Root ověřil všech 13 souborů zmrazeného MANIFEST-chebyshev31.json,
SHA-256 `ca728449e7ae402580748576059ad5211dfa030dcf0702cbd3a1b79e54da9056`.
Přečetl celou poznámku a předání, přímo všech šest původních stran
93–98, knižní s. 36 a 472 a erratum all1-pre, PDF 14.
Poté přečetl také uložená metadata MathNet včetně bibliografického
záznamu AMSBIB. Zmrazené agentovo předání se nemění; následující
rozlišení bibliografického stavu má přednost před jeho závěrem.

[Původní článek](https://www.mathnet.ru/php/getFT.phtml?jrnid=khmo&option_lang=eng&paperid=308&what=fullt)
má název o přibližném vyjádření jedněch integrálů pomocí jiných
se stejnými mezemi. Na s. 95 autor uvažuje váhu theta a rozvoj
pomocí ortogonálních polynomů, tedy polynomů s nulovým váženým
integrálem součinu pro různé stupně. Zbytek R_n má za uvedených
předpokladů znaménko součinu n-tých derivací obou funkcí.
Pro n=1 dostáváme

```text
integral(u*v*theta) = integral(u*theta)*integral(v*theta)
                     / integral(theta) + R_1.
```

Na s. 96 je theta=1 a interval [0,1]. Jsou-li u a v monotónní
stejným směrem, má součin jejich prvních derivací nezáporné znaménko,
a tedy integral(u*v) >= integral(u)*integral(v).

Převod na diskrétní tvrzení knihy doplňuje root: na i-tém intervalu
délky 1/n vezměme konstantní hodnoty u_i a v_i. Monotónní schodovité
funkce lze vyhladit monotónními přechody na množině celkové délky
nejvýše epsilon, při zachování společného omezení jejich hodnot.
Všechny tři integrály se změní nejvýše o konstantu krát epsilon.
Limitou proto dostaneme

```text
n * sum_i u_i*v_i >= (sum_i u_i)*(sum_i v_i).
```

Tento limitní převod je naše vysvětlení vztahu k úloze, nikoli tvrzení,
že autor v článku výslovně pracuje se schodovitými funkcemi.
S. 97–98 pokračují vyššími derivacemi a Legendreovými polynomy.
Na s. 98 stojí Petrohrad, 29. ledna 1883.

Erratum z 20. října 2011 cituje časopis jako 4, 2 (1882), 93–98.
[Uložená oficiální metadata](https://www.mathnet.ru/eng/khmo308)
uvádějí rok 1883 a číslo 2, zatímco 1882 je součástí názvu
časopisu. Také AMSBIB odděluje údaj `yr 1883` od názvu končícího
1882. To samo nedokazuje, zda 1882 je nominální ročník, označení
řady, nebo jiný údaj. Původní strany nemají titulní list celého čísla.
Pro uzavření bibliografie potřebujeme tento titul či obsah nebo
jednoznačný primární přetisk. Obsahová shoda proto zatím neuzavírá
celou úlohu. Úspěšný dřívější důkaz v sums-and-products.md se
neopakoval a nedostupný titul se nevydává za potvrzenou chybu.
