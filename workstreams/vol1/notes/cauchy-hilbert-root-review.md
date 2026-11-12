# Cauchyho původní determinant a uzavření §1.2.3–45

V1-X0752, 2. listopadu 2026. Celá úloha je checked společně
s dříve přijatým důkazem v matrices.md, oddílu 4, a Toddovým
článkem. Převzetí nevyvolalo nové matematické testy ani nový nález.

Root ověřil 21 souborů a dvě zachovaná vstupní PDF v předání
MANIFEST-cauchy45.json, SHA-256
`558da4d3bf2da6ec9ccc8759547a2b62ee30f83012025173f5a4ba3c9a0cbd1f`.
Přečetl celou agentovu poznámku, přímo titul a celý původní článek
v *Exercices d'analyse et de physique mathématique*, 2 (1841),
151–159. V přetisku *Œuvres complètes*, II, XII (1916), přímo četl
titul a s. 173, 176–177, 182. Zbytek tohoto přetisku se znovu celý
nečetl. Porovnal také knižní s. 38, 474–475, známá errata na
all1-prepre PDF 31 a dříve přijatý důkaz inverze a citlivosti.

[První vydání](https://archive.org/download/exercicesdanalys02cauc/exercicesdanalys02cauc.pdf)
na s. 151–152 definuje alternující funkci: záměna dvou proměnných
změní její znaménko. Alternující polynom je dělitelný každým jejich
rozdílem, a tedy součinem P=product_(i<j)(x_i-x_j).
Na s. 153 se alternuje product_i 1/(x_i-a_i), což je determinant
matice s prvky 1/(x_i-a_j). Po uvedení na společný jmenovatel
V=product_(i,j)(x_i-a_j) je čitatel U dělitelný P i analogickým
Phi=product_(i<j)(a_i-a_j). Stupeň U je n²−n, stejně jako stupeň
P*Phi, proto U=k*P*Phi s konstantou k.

S. 154 určuje k dosazením x_i=a_i **po odstranění jmenovatelů**.
Nejde o dosazení do singulárního zlomku. Rovnice (10) dává

```text
det[1/(x_i-a_j)] = (-1)^(n(n-1)/2)
                  product_(i<j)(x_i-x_j)(a_i-a_j)
                  / product_(i,j)(x_i-a_j).
```

Vzorec pro matici používáme při nenulových jmenovatelích.
Dosazením a_j=-y_j se v čitateli objeví dalších n(n−1)/2
záporných znamének, která zruší úvodní znaménko. Obrácení obou
rozdílů v každém páru už znaménko nemění. Výsledek přesně odpovídá
Cauchyho determinantu úlohy 38. Pro x_i=i a y_j=j−1 dostáváme
Hilbertovu matici H_ij=1/(i+j−1). Její inverze vzniká podílem
kofaktoru a determinantu; koefaktor zahrnuje příslušné znaménko
a determinant matice po vyškrtnutí řádku a sloupce. Vlastní
binomické formule, celočíselnost, dělitelnosti a citlivost jsou
již dokázány v matrices.md. Netvrdíme, že Cauchy tiskne všechny
pozdější knižní formule pro Hilbertovu inverzi.

[Primární přetisk 1916](https://archive.org/download/oeuvresdaugusti212caucrich/oeuvresdaugusti212caucrich.pdf)
má stejné určení konstanty na s. 176–177 a stejný vzorec (10)
na s. 177. Identita textu tedy není doložena jen katalogovým názvem.

Erratum z 13. ledna 2003 přidává k Toddovi právě Œuvres II, XII,
173–182. Poznámka ve stejné historické vrstvě uvádí od 24. dotisku
změnu na první vydání 1841, 151–159; oba cíle jsou ověřeny.
Oprava z 15. října 2007 správně rozlišuje matice od jejich determinantů
v tvrzení o kofaktorech. Agentův extrakt a závislosti zachycují
všechny čtyři vrstvy veřejných errat. Pozdější fyzický dotisk
se tímto neprohlašuje za kolacionovaný.
