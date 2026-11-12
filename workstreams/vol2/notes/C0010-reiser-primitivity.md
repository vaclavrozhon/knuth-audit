# V2-C0010: chybějící primitivita v Reiserově domněnce

**Stav: confirmed, 1. listopadu 2026.** Úloha §3.2.2-26 na
[str.39](../images/vol2-p039.png) připisuje Reiserovi domněnku pro
libovolné celočíselné koeficienty lineární rekurence. Primitivita
charakteristického polynomu modulo p, výslovná v primárním prameni,
v zadání chybí. Bez ní neplatí ani k=3, který poznámka označuje za ověřený.
Nejde o vyřešení zamýšleného otevřeného problému: úloha sama žádá důkaz
nebo vyvrácení, ale uvedená obecnost nesouhlasí s připsaným výsledkem.

## Přesný protipříklad

Nechť p=3, k=3 a alpha je libovolné kladné celé číslo. Označme
lambda_alpha nejmenší periodu a N_alpha počet nul v jejím jednom
opakování. Pevné koeficienty a_1=a_2=0, a_3=4 a pevné počáteční
hodnoty X_0=X_1=0, X_2=1 dávají

```
X_n = 4 X_(n-3) modulo 3^alpha,
X_(3t)=X_(3t+1)=0,    X_(3t+2)=4^t modulo 3^alpha.
```

Multiplikativní řád čísla 4 modulo 3^alpha, tedy nejmenší kladné r
s 4^r≡1, je 3^(alpha-1). Pro alpha=1 je to přímo 1. Pro vyšší alpha
binomická formule indukcí dává v_3(4^(3^j)-1)=j+1, kde v_3 označuje
počet faktorů 3 v čísle. První mocnina kongruentní k 1 modulo 3^alpha
má proto exponent 3^(alpha-1): řád je mocninou 3, protože 4 leží
v podgrupě 1+3Z o velikosti 3^(alpha-1), a předchozí mocnina nestačí.

Každá perioda celé posloupnosti musí zachovat polohy nenulových členů,
tedy je dělitelná 3. Následně musí její třetina být násobkem tohoto
multiplikativního řádu. Proto přesně

```
lambda_alpha=3^alpha,    N_alpha=2·3^(alpha-1).
```

Pro k=3 vytištěná domněnka požaduje N_alpha<=c·3^(alpha/2).
Při alpha=2r je podíl levé strany a mocniny roven 2·3^(r-1),
což je neomezené. Žádná konstanta c neexistuje. Neměníme koeficienty
ani počáteční hodnoty s alpha; přechod je invertibilní, nemá přechodný
úvod a počáteční vektor není nulový modulo p. Dvě počáteční nuly
následované jednotkou také vylučují homogenní rekurenci nižšího řádu
platnou od jejích počátečních indexů.

Charakteristický polynom je t³-4, modulo 3 tedy (t-1)³. Není
primitivní. Primitivní polynom stupně k nad F_p je ireducibilní
polynom, jehož kořen generuje multiplikativní grupu tělesa s p^k
prvky, a má tak řád p^k-1. Tento předpoklad uvedený příklad vyloučí.

## Primární pramen a rozsah opravy

John F. Reiser, *Analysis of Additive Random Number Generators*,
Stanford CS-TR-77-601, únor 1977:

- [Str.1](../images/reiser-p01.png) zavádí rekurenci (1.1) s výslovně
  primitivním polynomem modulo p a nenulovým počátečním vektorem modulo p.
- [Str.24](../images/reiser-p24.png) a [25](../images/reiser-p25.png)
  obsahují rozbor stupně 3 a větu 4.4, opět s primitivním polynomem.
- [Str.26](../images/reiser-p26.png), domněnka 4.1, se odvolává na (1.1)
  a nedegenerovanou periodu, čímž přebírá její předpoklady.

[PDF a metadata](../sources/reiser-1977.json) pocházejí ze zrcadla
původní Stanfordské technické zprávy. Nejde o sekundární převyprávění.
Vlastní korekce má obnovit tyto předpoklady; samostatné tvrzení o
discrepancy potřebuje navíc ošetřit růst period, viz [C0009](C0009-period-search-termination.md).

Vedlejší formální detaily stejného zadání: při povoleném k=1 není
exponent (k-2)/(k-1) definován; seznam zadaných x_1,...,x_k nesouhlasí
s prvními indexy rekurence x_0,...,x_(k-1). Nevedeme je jako další nálezy.

## Reprodukce a kontrola oprav

[Validátor](../verify_reiser_hypotheses.py) prošel přímo 88 572 stavů
pro alpha=1,...,10. Každý člen nezávisle porovnal s modulární mocninou
4^t a ověřil nejmenší řád. [Výsledky](../results/reiser-hypotheses.json)
a [log](../results/reiser-hypotheses.log). Obecný důkaz je uveden výše.

Prohledány all2-prepre, all2-pre, all2, err2 a err2.textxt z 1.11.2026,
podle str.39, odpovědí 555–557, jména Reiser a formulace domněnky.
Zásahy na str.39 z let 2001,2016,2024 patří úlohám 21,19,27, nikoli 26.
Relevantní oprava nebyla nalezena. Zadání bylo znovu vizuálně ověřeno
i na [str.39 digitálního vydání z července 2026](../images/publisher-preview-p039.png);
[tiráž](../images/publisher-preview-copyright.png) a
[metadata](../sources/publisher-preview-9780133488791.json) jsou uloženy.

Novější fyzický dotisk ani prvenství neověřeny. Omezená rešerše k
Reiserově jménu, domněnce a počtu nul nedala primární pozdější řešení;
z toho nevyvozujeme úplný stav otevřenosti v roce 2026.
[Anglický ASCII draft](../reports/C0010-reiser-primitivity-draft.txt) neodeslán.
