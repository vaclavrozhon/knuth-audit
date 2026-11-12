# C038: kladné rozměry v úlohách 184–185

Stav **candidate**, nízká závažnost. Jde pouze o otázku výslovného
vymezení domény, nikoli o zpochybnění výsledků pro kladné rozměry.
4B 7.2.2.1–184–185, zadání str. 147, odpovědi str. 468; stejné znění
je v autorově draftu. Definice na str. 71 požaduje alespoň jednu
primární položku v každé možnosti. Definice strict na str. 98 zakazuje
stejné řádky a stejné sloupce.

**184, n=0.** Bellovo číslo B0 je jedna. Doslovný interval 0≤t≤B0
tedy připouští t=0. Bez položek ale není žádná legální možnost;
existuje právě jedna prázdná podmnožina možností a ta je přesným
pokrytím. Jediná přípustná matice 0×0 má tedy jedno řešení, nikoli nulu.
Konstrukce odpovědi s prvky {1,…,n−1} ostatně předpokládá n≥1.
Stačí tento obvyklý předpoklad napsat.

**185, N1=0 a N2≥2.** Bez primárních položek opět neexistuje legální
možnost. Dva či více sekundárních sloupců jsou pak stejné prázdné
sloupce, takže žádná taková instance není strict. Maximum přes
prázdnou třídu není počet jedna vrácený formulí. Pro N1=0,N2≤1
je instance strict a jediné prázdné řešení odpovídá vzorci (s 0^0=1).
Pro N1≥1 je plná rodina možností strict a původní důkaz platí.
Možná formulace: N1≥1, případně zvlášť vyjmenovat přípustné nulové okraje.

Oba případy jsou přímé důsledky definic; žádné hledání ani solver se
nespouštěly. Dřívějších 1162 předepsaných počtů v 184 má n≥1.
Třicet kontrol primárních/sekundárních položek ověřilo počet pokrytí;
u N1=0,N2≥2 však vstup nesplňuje dodatečnou podmínku strict. Tyto
početní výsledky se nemění a nejsou důkazem existence strict instance.

Proč pouze kandidát: kniha může kladnost rozměrů považovat za implicitní.
Nejde o potvrzenou chybu v zamýšleném rozsahu a z tohoto okraje
neodvozujeme další F záznam. Celé 184–185 zůstávají do rozhodnutí
o doméně označené partial. Nenulová matematika je hotová.

Doklady: `images/mcc175-179-original-167.png`,
`images/extreme180-188-original-488.png`,
`images/extreme180-188-draft-178.png`,
`images/extreme180-188-original-91.png`,
`images/extreme180-188-original-118.png` a
`results/extreme180_188/errata-check.json`. Související dřívější otázky
C018 a C037 mají jiné konstrukce; zde jde o existenci přípustné instance.
