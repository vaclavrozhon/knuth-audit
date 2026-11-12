# Kandidát: výlučná atribuce formule Katzovi, odpověď 17 na s. 590

**Stav: candidate, nikoli confirmed.** Existuje přímo přečtený
starší datovaný pramen se stejnou formulí. Není doloženo datum
Katzova soukromého objevu, a proto tento podklad nezaměňuje
datum přijetí článku za datum objevu.

## Přesný text knihy a jeho kontrola

Originál knihy na s. 590 byl přímo zobrazen:
`../../tree-enumeration/images/p590.png`. Poslední odstavec
odpovědi §2.3.4.4-17 říká:

> The formula m^(m-1)Q(m) was first obtained by L. Katz,

poté cituje jeho článek z roku 1955, 512–517. Exponent v této
krátké citaci je přepsán do ASCII. Matematická formule knihy
je správná; předmětem kandidáta je slovo „first“.

## Dvě primární evidence

**Katz 1955.** Všechny strany 512–517 byly přečteny, viz
`katz-1955.md`. Na 516 v §5 autor výslovně uvádí, že po přípravě
svého článku jej David Blackwell upozornil na memorandum Rubina
a Sitgreavesové, které jinými metodami získává jeho hlavní větu.
Na 517 je memorandum identifikováno jako Stanford Technical
Report 19A (1954). Na 512 je datum přijetí 8. listopadu 1954
a poznámka o přednesení v prosinci 1954.

**Rubin–Sitgreaves 1954.** H. Rubin a R. Sitgreaves,
*Probability Distributions Related to Random Transformations of
a Finite Set*, Technical Report No. 19A (final), Applied
Mathematics and Statistics Laboratory, Stanford University.

- Primární repozitář: <https://purl.stanford.edu/wp824ks6839>.
- Původní PDF:
  <https://stacks.stanford.edu/file/druid:wp824ks6839/wp824ks6839_SOL-ONR-19A.pdf>.
- Místně: `../sources/rubin-sitgreaves-1954.pdf`, 2 178 928 bajtů;
  SHA-256 `96d33478b8a072a9acb2c571c8bc874e9c92f922da89c408f6515fd9fa923c73`.
- Doklady stažení: `../sources/retrievals-21.json` a `-22.json`;
  oficiální záznamy repozitáře i katedry jsou uloženy pod
  `../sources/rubin-sitgreaves-purl*` a `-stats.html`.
- **Přečten titul a tištěné strany 1–9**, tedy obrazy
  `../images/rubin-sitgreaves-1954-file-01.png` až `-10.png`.
  Titul přímo udává **January 22, 1954**. Zbytek 51stránkového
  PDF nebyl čten a není označen za auditovaný; automaticky
  vykreslený obraz sám není dokladem přečtení.

Na stranách 1–2 zpráva definuje komponentu právě jako množinu
bodů, jejichž iterace se setkají, shodně s ekvivalencí v knize.
Na s. 6 je rovnice (3.8) pro počet `J` cyklických bodů při `n`
prvcích:

```text
P(J=j) = (n-1)! j / ((n-j)! n^j),  1<=j<=n.
```

Na s. 7 je podmíněný zákon počtu komponent roven zákonu počtu
cyklů rovnoměrné permutace `j` bodů. Pro jediný cyklus je tato
pravděpodobnost `1/j`. Proto (4.2) dává přesně

```text
P(one component) = sum_{j=1}^n (n-1)! / ((n-j)! n^j).
```

Navíc s. 8 tuto specializaci přímo tiskne při výpočtu velikosti
komponenty; nejde o netriviální nový důsledek, který by ve zprávě
nebyl rozpoznán. Vynásobení `n^n` a substituce `M=n-j` dává
`(n-1)! sum_{M=0}^{n-1} n^M/M! = n^(n-1)Q(n)`.
Obecný rozklad za (3.8) a (4.2) byl zkontrolován. Po podmínění
na množinu cyklických bodů lze libovolně měnit její permutaci,
aniž se mění připojený les, takže rovnoměrnost permutace a faktor
`1/j` jsou odůvodněny pro každé `n` a `j`.

## Co z toho lze a nelze uzavřít

Zpráva datovaná lednem 1954 obsahuje stejný výsledek před
Katzovým citovaným článkem a Katz tuto shodu sám potvrzuje.
Formulace knihy proto opomíjí konkrétní starší doložený zdroj.
Bez další evidence ale neznáme datum, kdy Katz svůj výsledek
poprvé soukromě získal, ani absolutní prvenství Rubina a
Sitgreavesové vůči veškeré starší literatuře.

Možná opatrná redakční úprava je odstranit „first“ a doplnit
odkaz na zprávu z 1954. Silnější nahrazení výlučného prvenství
Katzova výlučným prvenstvím jiné dvojice by přesahovalo zjištění.
Kandidát se předává rootu k nezávislému historickému posouzení.

## Všechny čtyři vrstvy errat

Texty `all1-prepre`, `all1-pre`, `all1`, `err1` byly prohledány
podle s. 590 a výrazů Katz, Rubin, Sitgreaves a first obtained;
výsledek je `../results/katz-priority-errata-search.json`.
Jediná položka s. 590 opravuje 8. 11. 2005 mez indexu v odpovědi
16 a netýká se atribuce.

Přímo prohlédnuty příslušné původní obrazy:

- `tree-enumeration/images/errata-all1-prepre-44.png` a `-45.png`;
- `tree-enumeration/images/errata-all1-pre-17.png` a
  `tree-history/images/all1-pre-18.png`;
- `tree-history/images/all1-15.png` (přechod 587 → 597);
- `doubly-linked/images/errata-err1-13.png` a
  `tree-history/images/err1-14.png` (stejný přechod).

V žádné vrstvě není oprava Katzovy historické priority. Jde
o nové konkrétní pramenné zjištění, nikoli znovuobjevení opravy.
Žádné globální ID nebylo přiděleno.
