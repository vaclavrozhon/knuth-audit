# V2-C0016: původ Pearsonových ruletových dat

**Stav:** potvrzená historická nepřesnost v §3.3.1, str. 55. Kniha
připisuje Pearsonovi osobní zkušenost s příslušnými dvěma týdny rulety
v Monte Carlu roku 1892. Pearson sám popisuje zpracování publikovaných
záznamů. Stejná formulace zůstává ve vydavatelském náhledu z roku 2026.
Novější fyzický dotisk, prvenství ani případná odměna ověřeny nejsou.

## Knižní zdroj

Vizuálně přečtena [str. 55 prvního tisku](../images/vol2-p055.png),
strana souboru 67. Sporná je závorka „which he had experienced during
two weeks at Monte Carlo in 1892“. Tatáž závorka je ve
[vydavatelském náhledu](../images/publisher-preview-p055.png), PDF
strana 71 = tištěná 55. Identifikaci a hash náhledu obsahuje
`sources/publisher-preview-9780133488791.json`; jeho tiráž uvádí osmé
digitální vydání v červenci 2026. Z toho nevyvozujeme stav fyzických knih.

## Dva propojené primární prameny

Pearsonův článek z roku 1900, *On the criterion that a given system of
deviations from the probable in the case of a correlated system of
variables is such that it can be reasonably supposed to have arisen
from random sampling*, Philosophical Magazine, Series 5, 50, 157–175,
má na str. 169 příklad III. [Originální strana](../images/pearson-1900-p169.png)
uvádí 4274 sérií barev a odkazuje na *The Chances of Death*, vol. I,
str. 54. PDF je v `sources/pearson-1900-chi-square.pdf`,
[primární scan v Zenodu](https://zenodo.org/records/1430618/files/article.pdf?download=1).

Odkazovaná kniha *The Chances of Death and Other Studies in Evolution*
(1897), vol. I, obsahuje na str. 42–62 kapitolu *The Scientific Aspect
of Monte Carlo Roulette*, původně otištěnou v únoru 1894.
[Originální str. 45](../images/pearson-1897-p45.png) výslovně říká:

> To spend several months in Monte Carlo recording the spin of the
> roulettes was personally an impossibility.

Hned poté vysvětluje, že získal záznamy vydávané týdně v *Le Monaco*;
zpracoval přes 16 500 hodů z července a srpna 1892. Další čtyři týdny
zpracoval L. G. de Whalley. Poznámka na str. 45–46 zachycuje Pearsonův
dopis z února 1894, kterým ověřoval věrohodnost záznamů u vydavatele.
To vysvětluje původ dat přímo, bez domněnek o Pearsonově cestování.

Na [str. 54](../images/pearson-1897-p54.png) je právě tabulka 4274 sérií,
kterou přebírá článek 1900. Počty pro délky 1 až 12 a větší než 12 jsou

```
2462, 945, 333, 220, 135, 81, 43, 30, 12, 7, 5, 1, 0.
```

Shoda celé tabulky a výslovný odkaz spojují oba prameny. Označení
„my fortnight“ na str. 55 odkazuje na Pearsonovu část zpracovaných
záznamů; nevyvrací explicitní popis jejich získání na str. 45.
Přečtena celá kapitola 42–62, rozhodné strany 45 a 54 také obrazově.
Lokálně uložen pouze tento výřez; URL, mapování a SHA-256 jsou
v `sources/pearson-1897-monte-carlo.json`.
[Originál v Internet Archive](https://archive.org/details/cu31924097311579).

## Rozsah opravy

Stačí nahradit závorku například „reported in Le Monaco for two weeks
in July 1892“. Nejde o tvrzení, že Pearson nikdy Monte Carlo nenavštívil,
ani o zpochybnění autorství jeho analýzy.

Článek 1900 tiskne pravděpodobnost 14.5/10^30, jejíž převrácená hodnota
je přibližně 6.9*10^28; řád 10^29 u Knutha tedy odpovídá historickému
prameni. Nepotvrzujeme tím moderní přesnou kalibraci Pearsonovy
aproximace ani interpretaci p-hodnoty jako pravděpodobnosti poctivé rulety.
Tento nález je omezen na původ pozorování.

## Errata

Dne 1. listopadu 2026 prohledány `all2-prepre`, `all2-pre`, `all2`,
`err2` a aktuální původní TeX `sources/err2.textxt`: str. 55 a výrazy
Pearson, 1892, roulette, experienced, Monte Carlo. Oprava závorky
nenalezena. Nejbližší historická oprava je mikrosekundy na milisekundy
na str. 54 z 7. února 2000; týká se ENIACu. Nová digitální sazba
nezávisle potvrzuje přetrvávání formulace. Návrh hlášení není odeslán.
