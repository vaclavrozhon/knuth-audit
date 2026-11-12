# P0127 — šest jednotlivých izomorfismů v (16)

6. listopadu 2026. P14/file31, všech šest kreseb (16). **Checked** pro
každý diagram samostatně. Zdroj je již uložený přímý PDF výřez původního
DjVu `sources/proof-file031.pdf`, čitelný render
`images/proof-cube-drawings.png` a detail čtvrtého obrázku
`images/proof-cube-drawing4.png`. Renderováno pomocí `pdftoppm -q`.

## Jednoznačné pojmenování původních vrcholů

Diagramy číslujeme 1,…,6 zleva. Značky A,…,H označují výhradně osm
malých kroužků, nikoli další průsečíky čar.

* V diagramech **1, 2, 4, 5** jsou čtyři výškové úrovně, na každé dva
  vrcholy. Shora dolů a vždy zleva doprava je označ A,B; C,D; E,F; G,H.
* V diagramu **3** je nahoře A,B, uprostřed zleva C,D,E,F, dole G,H.
* V diagramu **6** je horní řada zleva A,B,C,D a dolní E,F,G,H.

## Přesný seznam všech hran po jednotlivých kresbách

V každém řádku následující tabulky tvoří U a V dvě disjunktní čtveřice
v cyklickém pořadí. Čtyři zbývající hrany jsou výslovně vypsány vpravo.
To je úplný seznam dvanácti čar daného diagramu, nikoli jen jeho podgraf.
Oblé horní/dolní čáry v diagramu 6 jsou vždy jedinou hranou.

| diagram | cyklus U₀U₁U₂U₃U₀ | cyklus V₀V₁V₂V₃V₀ | zbývající čtyři hrany U_iV_i |
|---|---|---|---|
| 1 | A–B–F–E–A | C–D–H–G–C | AC, BD, FH, EG |
| 2 | A–B–D–C–A | G–H–F–E–G | AG, BH, DF, CE |
| 3 | A–B–F–E–A | C–D–H–G–C | AC, BD, FH, EG |
| 4 | A–B–C–F–A | H–E–G–D–H | AH, BE, CG, FD |
| 5 | A–B–D–C–A | G–H–F–E–G | AG, BH, DF, CE |
| 6 | A–B–C–D–A | E–F–G–H–E | AE, BF, CG, DH |

Pro překřížený diagram 4 lze stejný přepis ověřit ještě přímo v detailu:

    A: B,F,H       B: A,C,E       C: B,F,G       D: F,G,H
    E: B,G,H       F: A,C,D       G: C,D,E       H: A,D,E.

Vnitřní průsečíky nejsou kroužky a nezavádějí další incidenci.
Diagonála E–B například nekončí na průsečíku s C–G; její konce jsou
právě dva označené kroužky. Tím se i nejméně přehledná kresba ověřuje
celým seznamem sousedností, nikoli vizuálním dojmem.

## Izomorfismus na Q₃

Pro **každý řádek tabulky** zvol g₀=00, g₁=01, g₂=11, g₃=10 a definuj

    U_i ↦ 0g_i,      V_i ↦ 1g_i,      i=0,1,2,3.

Je to bijekce na osm bitových trojic. Po každém cyklu se mění právě
jeden z posledních dvou bitů, také na uzavírací hraně 10–00. Čtyři
hrany U_iV_i mění pouze první bit. Naopak sousední trojice Q₃ buď mění
první bit (právě jedna z těchto čtyř hran), nebo zachovávají první bit
a mění jeden ze dvou dalších (právě hrana příslušného čtyřcyklu).
Bijekce tedy zachovává hrany v obou směrech pro všech šest diagramů.

Tento argument ověřuje přesně tvrzení u (16). Vlastnosti Q₃ ani jeho
48 automorfismů z P0128 se znovu neodvozují. Žádný matematický program
nebo census; nové obrázky jsou pouze rendery původní sazby. Nový nález
nevznikl. Následující samostatná mapa vymezuje pokrytí celé p14.

## Doplnění P0504 a přesná mapa p14

Na p14 jsou také tři explicitní kladná tvrzení o rovinnosti. P_n pro
n≥1 lze nakreslit n body na přímce se spojnicemi po sobě jdoucích bodů.
C_n pro n≥3 lze nakreslit jako obvod pravidelného n-úhelníku. U Q₃
vyber dva soustředné souhlasně orientované čtverce a odpovídající rohy
spoj radiálně; žádné dvě hrany se mimo společné konce neprotínají.
Jde právě o krychlový model dvou C₄ s odpovídajícím matchingem z důkazu
výše a o Fig. 2(d). Hraniční C₁/C₂ ze známé terminologické opravy jsou
multigrafy, ne další jednoduché grafy; ani jejich obvyklé smyčkové/
dvojhranové kresby nepřidávají křížení. Tato tři kladná tvrzení jsou
nově výslovně vedena jako P0504, nezakryta pouhými počty vrcholů.

Po uzavření P0127/P0504 má **každé matematické tvrzení p14/file31**
následující konkrétní krytí:

| Rozsah původní stránky | Přesný argument |
|---|---|
| Dokončení definice izomorfismu, konvence stejného grafu a začátek definice automorfismu | P0125, proof-007: bijekce vrcholů s ekvivalencí sousednosti; konečnost umožňuje ekvivalentní zachování hran |
| Šest grafů Fig. 2, všech šest počtů vrcholů/hran a následné stupně/regularita | P0126 v proof-007; úplný Chvátalův seznam P0397 v proof-016 doplňuje všech 24 hran |
| Průsečíky čar nejsou další vrcholy, konkrétně střed Fig. 2(f) | Přímé rozlišení dvanácti kroužků a přesný seznam P0397 |
| Rovinnost P_n, C_n a krychle | P0504 výše, konkrétní geometrická realizace bez křížení |
| Nerovinnost K₅ kvůli počtu hran | P0151/P0152, proof-007: 10>3·5−6, Eulerův argument i relevantní §7–46/47 doloženy; chybný pomocný krok jiné odpovědi oddělen jako F0001 |
| Každá ze šesti kreseb (16) je Q₃ | P0127: šest úplných hranových certifikátů a bijekcí v této poznámce |
| Symetrie Chvátalova rozložení zmíněné v závěru stránky | Přesné dihedrální mapy i horní mez P0132/P0148, proof-022; nejde o pouhý dojem z kresby |

Historické údaje Petersen 1898, Chvátal 1970 a Bondyho původ rozložení
nejsou matematickým vstupem těchto důkazů; dřívější bibliografické
výjimky zůstávají výslovně uvedeny. Toto je podklad pro jediné nové
celostránkové `review_depth: argument`, **file31/p14**. Nezavírá okolní
strany, sekvenční prefix ani neověřené datové/symetrické otázky na p15.
