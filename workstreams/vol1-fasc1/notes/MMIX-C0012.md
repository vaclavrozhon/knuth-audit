# MMIX-C0012 — GetReg opomíjí cenu marginal registrů

**Confirmed, low.** Odpověď §1.4.3′–2, p. 116 / file 124, poslední
věta: `μ+6υ+6υL`, kde `L=[$k is local]`. Související věta na p. 117
přidává 6υ pouze za local source. Kód je p. 80 / file 88, řádky 064–073.

Konkrétní dovolený stav: simulated rL=2, rG=32 a k=3. Register $3
je marginal, proto má odpověď L=0 a předpovídá μ+6υ. GetReg ale
větví podle k<G, nikoli k<rL. Pro k=3 se provede tato cesta:

| Řádek | Instrukce | Cena |
|---|---|---|
| 064 | CMPU | 1υ |
| 065 | BN, taken | 3υ |
| 068 | CMPU | 1υ |
| 069 | ADDU | 1υ |
| 070 | AND | 1υ |
| 071 | LDOU | μ+1υ |
| 072 | CSNN | 1υ |
| 073 | POP | 3υ |

Součet je **μ+12υ**. CSNN vrátí správnou nulu, ale nestojí méně,
protože jeho podmínka je splněna. Tentýž delší profil má každý
nonglobal registr, local i marginal. Správné jednoduché kritérium
ve vzorci je `[$k is not global]`, respektive `[k<G]`.

Nejde o zpomalení konkrétní cache ani o interpretaci skutečného hardware:
jsou to přímo časy tabulky 1, stejné jako v tvrzení. Funkční výsledek
GetReg je správný, mění se analytická cena a příslušná source-register
penalta při simulaci. Není potřeba program spouštět v simulátoru.

Původní sazba kódu i tvrzení zobrazena v images/file-088-p080.png a
images/file-124-p116.png; související věta také file-125-p117.png.
Prohledány errata/originals/err1f1.textxt a errata/text/{all1f1,err1f1}.txt
podle p. 80,116,117 i GetReg/local/marginal. Známá oprava komentáře
na řádku 068 (2009) upřesňuje znaménko t, nikoli tento časový vzorec;
opravena sazba answer 4 na p. 116 se týká jiného oddílu. Relevantní
oprava nalezena nebyla, viz results/errata-C0009-C0012.json.
