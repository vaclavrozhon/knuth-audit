# V4A-F0009 — tautologické smyčky v odpovědi 85

**Confirmed, low.** §7.1.1–85, odpověď p550/file567,
první odstavec: „Thus the digraph must be acyclic.“
Nutná podmínka platí až po odstranění smyček.

## Přesný protipříklad

Vezměme dvouproměnnou 2CNF (x∨y)∧(x∨¬x).
Konstrukce na p62 dává oblouky ¬x→y, ¬y→x,
x→x a ¬x→¬x. Každá má svou kontrapozici, takže
jde přesně o antisymetrický digraf z domény úlohy.

Modely X={01,10,11} jsou redukované: x dosvědčuje
01–11 a y dvojice 10–11. Jsou mediánové podle
Theorem S, i přímo: medián 00 by vyžadoval aspoň
dva vstupy s x=0 a aspoň dva s y=0, takže jeden
ze tří vstupů by byl 00, spor.

Digraf však má dvě orientované smyčky, tedy cykly
délky 1. Každá silná komponenta je singleton a
žádná cesta nevede z literálu do jeho doplňku.
Správná předchozí věta odpovědi o silných komponentách
tedy neimplikuje vytištěnou acykličnost.

## Doména a původní sazba

- P18/file35 výslovně dovoluje self-loops v digrafech,
  i v jednoduchých digrafech.
- P62/file79 překládá každou dvouliterálovou klauzuli
  u∨v na ¬u→v a ¬v→u; nevyžaduje odstranění
  tautologií. P0807 již tuto doménu doložila.
- Zadání 85 na p91/file108 nemá předpoklad bez smyček.
- Odkázaná definice V1 §2.3.4.2, p372/file387,
  výslovně zahrnuje orientované cykly délky 1.
  Originál zobrazen. Známá oprava z 25. července 2008
  mění walk/path, ale smyčka stále splňuje definici
  orientovaného cyklu; také sazba této opravy zobrazená.

## Oprava a její rozsah

Požadovat acykličnost **po odstranění smyček**, nebo
ponechat přesnou podmínku „každá silná komponenta má
jediný vrchol“. Zákaz cesty k doplňku se nemění.
Smyčky vyjadřují tautologie a nemění modely.

`notes/proof-080-reduced-implication-graphs.md`
dokazuje nutnost i postačitelnost opraveného znění
pro všechny počty proměnných a konstruuje oba svědky
každé souřadnice. Výsledek pro grafy bez smyček je
správný. Theorem F není dotčena: její relace jsou
od počátku mezi různými souřadnicemi.

## Errata a důkazy

7. listopadu 2026 prověřeny `errata/text/all4a-pre.txt`,
`all4a.txt`, `err4a.txt`, `all4f0.txt`, `err4f0.txt`.
Hledání p550/odpovědi 85, tautologií, acykličnosti,
smyček a redukovaných množin nenašlo příslušnou opravu.
Kvůli definici cyklu navíc prověřeny `all1-prepre`,
`all1-pre`, `all1`, `err1`. Relevantní oprava p372
z roku 2008 byla uplatněna a protipříklad zachovává.

Originály: `images/proof-file567.png`, `file108.png`,
`file035.png`, `file079.png`,
`vol1-cycle-definition-file387.png` a
`vol1-cycle-definition-erratum.png`. Žádný matematický
výpočet. Potvrzení vůči těmto zdrojům není tvrzení
o prvenství; tištěný exemplář nebyl ověřen.
