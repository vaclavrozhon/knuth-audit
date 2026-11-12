# V2-C0087: nadbytečná nula v erratu pro nenormalizované Avogadrovo číslo

**Confirmed.** Erratum28.6.2020 pro str.238, řádky−12 až−8,
v `all2-pre`, str.6. Vizuálně znovu přečten originál errata i původní
str.238. Osmiciferný desetinný formát zde nemá exponentový exces.

Erratum nahrazuje příklad nenormalizovaného Avogadrova čísla dvojicí

```text
(26,+.000602214).
```

Tento zlomek má devět míst, a tedy není slovem deklarovaného
osmiciferného formátu. I při ignorování délky by jeho hodnota byla
.000602214·10^26=6.02214·10^22, tedy přibližně desetkrát menší,
než odpovídá uvedené konstantě. Normalizovaný zápis ve stejném
erratu je(24,+.60221408), přibližně6.02214·10^23.
Oficiální [definice SI molu uBIPM](https://www.bipm.org/en/si-base-units/mole)
potvrzuje přesnou číselnou hodnotu6.02214076·10^23.

Odstranění jedné úvodní nuly dává zamýšlený zápis

```text
(26,+.00602214).
```

Ten má osm míst a hodnotu6.02214·10^23. Právě tento správný
zápis uvádí tentýž list errat níže jako součetN⊕h; opravené
nenormalizované násobení s h=(−30,+.00066261) také reprodukuje
tištěný výsledek(−6,+.00039903). Změna exponentu na27 by sice
opravila velikost, ale ponechala by devět míst a neodpovídala by
zamýšlenému osmicifernému příkladu.

Čtyři vrstvy errat a aktuálníTeX prohledány2.11.2026 podle238,
Avogadro a obou zlomků. Pozdější oprava této nuly nenalezena.
Nejde o záměnu s opravou jednotek Planckovy konstanty ani o novou
fyzikální definici; chyba je uvnitř nového textu errata2020.
Novější fyzický tisk/prvenství neověřeny, neodesláno.

Reprodukce: `verify_unnormalized.py`, blokspecial_examples;
`results/unnormalized.json`. Originál:
`images/accuracy-errata-all2-pre-6.png`. Primární kontrolaSI:
`sources/bipm-avogadro-2026-11-02.json`.
