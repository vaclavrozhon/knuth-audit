# V2-C0095: konstanty časování v odpovědích §4.3.1-3 a8

**Confirmed v dostupném prvním dotisku třetího vydání1997.** Originály
[str.623](../images/vol2-p623.png) a [624](../images/vol2-p624.png)
vizuálně ověřeny; obě související opravy evidujeme jako jeden nález.

V odpovědi3 označuje M počet sčítanců, N jejich délku ve slovech a K počet
přetečení při sčítání slov. Přesný čas je `5MN+7N+K+5`, nikoli s konstantou4.
Tři úvodní instrukce ENN1,JOV,ENTX stojí3 cykly; poslední STX stojí2.
Po dosazení tištěného odhadu K=MN/2 je tedy `5.5MN+7N+5`.

Pro M=2,N=1 a slova b-1,1 (b je velikost slova MIX) je K=1=MN/2.
Přímý běh má23 cyklů, tištěný výraz22. Aproximace K není příčinou rozdílu.

V odpovědi8 je L počet vstupních pozic se součtem alespoň b a K počet
všech propagovaných přenosů. Čas je `9N+L+7K+4`, nikoli `...+3`;
ENT1,JOV,STZ stojí1+1+2. Odpovídající odhad je `13N+4`.
Pro N=1 a vstupy b-1,1 je L=K=1, a tedy21 cyklů místo20.

Instrukční přepis, skutečné návštěvy a obě úplné stopy jsou v
[classical-basic.json](../results/classical-basic.json), blok MIX.
[Důkazy a ruční četnosti](classical-basic.md) doložily zároveň správnost
programů. Všechny vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
prohledány2.11.2026 podle stran623–625 i výrazů, bez této opravy.
Aktuální změna624 se týká pouze číslování rovnice v odpovědi7.

Neověřen poslední fyzický dotisk, priorita ani nárok na odměnu.
[Návrh hlášení](../reports/C0095-classical-timing-draft.txt) nebyl odeslán.
