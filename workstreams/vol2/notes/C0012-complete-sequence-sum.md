# V2-C0012: erratum ruší úplnost kombinace posloupností

**Confirmed, 1. listopadu 2026.** Ve veřejném erratu z 8. 7. 2001,
`all2-prepre`, str. 31 seznamu, je pro odpověď §3.2.2-21,
str. 556 řádek 14, předepsána změna `s*X_n+Y_n` na
`(X_n+Y_n) mod (r*s)` (modul je rs). Původní vzorec je správný;
náhrada neprodukuje tvrzenou posloupnost typu B.

## Nejkratší protipříklad

Typ B(m,k) znamená cyklickou posloupnost obsahující každou k-tici
nad {0,...,m-1} právě jednou; tím má periodu m^k a určuje rekurenci
řádu k. Vezměme nesoudělná r=2,s=3 a k=1:

```
n       0 1 2 3 4 5
X_n     0 1 0 1 0 1
Y_n     0 1 2 0 1 2
new Z   0 2 2 1 1 3
old Z   0 4 2 3 1 5
```

X je typu B(2,1), Y typu B(3,1). Nová Z vynechá 4 a 5, takže není
B(6,1). Navíc Z_1=Z_2=2, ale Z_2=2 a Z_3=1: žádná funkce f nemůže
splnit Z_(n+1)=f(Z_n). Nejmenší perioda Z je přesto6; nezpochybňujeme
proto správný součin period z úlohy 13. Ten pro potřeby úlohy 21 nestačí.

Obecně při r,s>=2 platí 0<=X_n+Y_n<=r+s-2<rs-1. Redukce modulo rs
nic nezmění a číslice rs-1 se nikdy nevyskytne. Nový vzorec tedy
nemůže dát úplnou posloupnost pro žádné k>=1.

## Oprava a důkaz

Stačí ponechat původní `s*X_n+Y_n`. Zobrazení (x,y)↦s*x+y je bijekce
z {0,...,r-1}×{0,...,s-1} na {0,...,rs-1}. Dvojice k-oken má
jedinečné společné časové umístění modulo r^k*s^k díky nesoudělnosti
r^k a s^k. Každé výstupní k-okno se proto objeví právě jednou.
Alternativou je skutečné čínské kódování s příslušnými koeficienty,
nikoli prostý součet nenásobených číslic.

## Zdroj a kontrola dosavadních oprav

- První tisk 1997, původní str. 555–556: definice a kontext A/B,
  `images/vol2-p555.png`, `images/vol2-p556.png`, vizuálně přečteny.
- Vlastní oprava vizuálně ověřena z původního seznamu:
  `images/all2-prepre-p31.png`, zdroj `sources/all2-prepre.ps.gz`.
  Jednoznačně odstraňuje koeficient s; nejde o ztrátu při OCR.
- Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální TeX,
  podle stránky556, odpovědi 21, Rees, typu B a obou vzorců.
  Oprava 5. 4. 2026 se týká pouze zatoulaného „(2)“ na str. 555.
  Žádná další matematická oprava této kombinace nalezena.
- Všechny vrstvy staženy1. 11. 2026. Autorův veřejný seznam:
  https://www-cs-faculty.stanford.edu/~knuth/all2-prepre.ps.gz
- Novější fyzický dotisk neověřen. Digitální náhled 2026 nemá odpověď
  na str. 556, takže jej nepoužíváme jako doklad tohoto konkrétního nálezu.

Přesný test a obecný důkaz: `verify_complete_sequences.py`,
`results/complete-sequences.json`, [poznámka](complete-sequences.md).
Návrh `reports/C0012-complete-sequence-sum-draft.txt` je neodeslán.
Netvrdíme prvenství ani nárok na odměnu.
