# V3-C0023 — rozsah minima u tří přírůstků

**candidate / low**, nikoli potvrzená chyba.

Originál92/file103, dolní odstavec k tabulce5: věta připisuje
přírůstkům3,2,1 minimum průměrného počtu přesunů. Celý odstavec
je současně výslovně zasazen do tabulky5. Ta obsahuje pouze
trojice4,2,1;5,3,1;3,2,1, mezi nimiž má3,2,1 opravdu nejmenší
průměr. Implicitní rozsah tvrzení proto není jednoznačný.

Pro celé tříprůchodové třídění osmi prvků je konkrétní rozpor:

    E B_(5,2,1)=817/105 < 822/105=E B_(3,2,1),
    rozdíl=1/21.

Oba obecné analytické součty pro tento konečný model a jejich
nezávislá malá GF jsou odvozeny v
`insertion-proof-eight-items-table5.md`, P0835/P0843. První dva
průchody5,2,1 mají ručně3/2 a11/3; poslední183/70. Pro3,2,1
jsou hodnoty7/2,12/5,27/14. Žádný census permutací či statistický
odhad se nepoužívá.

Pět dodaných vrstev errat neobsahuje upřesnění této věty ani
srovnání5,2,1: `sources/three-pass-minimum-errata-review.json`.
Oprava274.42→274.41 z2023 je jiná, známá a mimo nálezy.

Možná lokální úprava: dodat „among the sequences in Table5“.
Při zamýšleném globálním tvrzení změnit optimum na5,2,1
a doplnit jeho průměr. Rozpor mění malé optimum přesunů,
nikoli správnost algoritmu či asymptotickou analýzu.
