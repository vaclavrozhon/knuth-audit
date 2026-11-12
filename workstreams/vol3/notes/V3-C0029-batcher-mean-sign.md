# V3-C0029 — chybné znaménko v lineární konstantě průměru

Stav: **confirmed, low**, knižní nález. Volume3,2. vydání,
1. tisk1998, tištěná630/file641, §5.2.2 odpověď16, jediný
velký asymptotický vzorec. Zobrazen originál i detail
`images/batcher-mean-formula-1.png`.

Za A=lg(Γ(1/4)²/(2π)) kniha uvádí lineární koeficient

    A+1/4+(γ+2)/(4ln2)+δ(n), |δ(n)|<.0005.

Správně je

    A+1/4−(γ+2)/(4ln2)+δ(n).

Oprava mění pouze znaménko před zlomkem. Vedoucí člen
(n/4)lg n, periodická mez, zbytek O(√n log n) a závěr
o podílu výměn1/4 jsou správné. Algoritmus tím není dotčen.

## Obecný důkaz

Celý samostatný důkaz všech částí16 je v
`notes/exchanging-proof-batcher-mean-16.md`, P1020–P1031.
Jeho rozhodující kroky jsou:

1. Přesné počítání cest a Pascalova identita dávají
   B_n=n/2+(1/(2c_n))Σ_(1≤j<n)c_j b_j, kde
   c_j=binom(2j,j)/4^j a b_j=Σ_(k≥1)binom(2j,j−k)Δf(k)/binom(2j,j).
2. Absolutní Gaussian odhad a plně zdůvodněný přesun Mellinovy
   kontury dávají b_j=¼lg j+A−1/4−γ/(4ln2)+ε(j)+O(j^(−1/2)).
   Záporné γ pochází přímo z Γ(z)=1/z−γ+O(z).
3. Přesná suma c_j přenese konstantu beze změny. Logaritmický
   integrál2√n ln n−4√n přidá další **−n/(2ln2)**;
   počáteční n/2 změní−1/4 na+1/4. Výsledný koeficient je
   proto A+1/4−(γ+2)/(4ln2).
4. Periodická Fourierova řada je absolutně konvergentní a
   vlastní analytický ocas plus jediný malý intervalový výpočet
   dokazují |δ|<.000499399<.0005. Výsledek je v
   `results/batcher-mean-periodic-bound.json`; běh nice15.

Tištěný a správný koeficient se liší o Δ=(γ+2)/(2ln2)>1.
Ani dvě libovolné periodické funkce s uvedenou mezí nemohou
rozdíl změnit o více než.001. Po vydělení n je deklarovaný
zbytek O(log n/√n)→0. Rozpor tedy platí obecně a také podél
mocnin2 předepsaných zadáním. Nejde jen o nesoulad citací
nebo o konečný číselný příklad bez kontroly asymptotického zbytku.

## Originál, zdroj a errata

Primární článek Roberta Sedgewicka, *Data Movement in Odd-Even
Merging*, SICOMP7(1978),239–272, Theorem3 na266, má správné
záporné znaménko. Stažen přímo od autora:
https://sedgewick.io/wp-content/themes/sedgewick/papers/1978Batcher.pdf
Lokálně `sources/sedgewick-1978-batcher.pdf`, zobrazená sazba
`images/batcher-sedgewick-mean-28.png`. Vnější analytické
identity a jejich platné předpoklady jsou výslovně uvedeny
v obecném důkazu; článek nenahrazuje vlastní kontrolu znaménka.

Pětivrstvá kontrola je v `sources/batcher-mean-sign-errata-review.json`.
Moderní vrstvy nemají odpovídající opravu. Err3-1e na své
PDF straně76, pod původní tištěnou607, tuto chybnou kladnou
verzi **opakuje** v náhradě odpovědi16 z29.11.1977; sazba
zobrazena v `images/batcher-mean-old-errata-076.png`.
Nejde o již opravenou známou chybu. Známý programový skok629
a dodatek630 k odpovědi15 se týkají jiných tvrzení.

Potvrzení platí pro dodaný sken a všechny dodané vrstvy errat.
Tištěný exemplář není ověřen; prvenství ani odměna se netvrdí.
