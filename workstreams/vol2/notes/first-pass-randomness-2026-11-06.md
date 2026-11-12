# §3.5 C–G: rychlý první průchod

6. listopadu 2026, V2-X0131. Souvisle přečtena původní sazba 159–183
a zbývající odpovědi §3.5 na 594–599. A/B a odpovědi 1–18,22–25,28
navazují na X0130. Celá §3.5 tím prošla čtením; nejde o nové úplné
dokazování všech vět ani řešení výzkumných úloh.

Přebíráme uzavřené důkazy v `selection-randomness.md`,
`selection-extensions.md`, `gap-structure.md`, `white-parity.md`,
`finite-randomness.md`, `cryptographic.md`, `randomness-history.md`
a `C0070-r6-prefix-bias.md`. Staré programy/censy se neopakovaly.
Nový nález **žádný**. Kontrola errat převzata z těchto záznamů; místní
errata byla 6. listopadu ověřena proti zdroji a zůstala stejná.

Při čtení posouzeny definice R1–R6, řídké změny, Waldův strom,
měřitelnost/adaptivní výběr a důkaz plné míry, Q1/Q2, hybridní redukce,
algoritmus L a podmíněná redukce k faktorizaci. V P2 se rozlišuje
předpověď bitu a test správnosti předpovědi. Číselné tabulky a složitostní
výpočty mají archivní kontroly; nyní nejsou znovu reprodukovány.

Závažnost upravena podle skutečného dopadu:

- C0061 a C0063 **low**: chybné konečné odhady v pomocném důkazu,
  hlavní věty zůstávají pravdivé. Krátké protipříklady v původních poznámkách.
- C0064 **medium**: odraz bodů zachovává všechny délky mezer, takže
  tvrzená jednoznačnost bodové posloupnosti je nepravdivá; minimax platí.
- C0065 a C0066 **low**: posun indexu vzniku mezery a inicializace
  pomocné posloupnosti; opravy a důkazy hlavních tvrzení jsou uložené.
- C0067 a C0068 **low**: vynechané okrajové případy N=1 a nulový rozptyl.
- C0069 **medium**: skutečně chybná konstrukce předpovědi; už N=1,
  S={1}, A(B)=B dává vždy špatný výstup. Věta P2 přesto platí.
- C0062 zůstává **medium**: první výstup 1/2 porušuje požadavek
  úlohy 31 na převahu dolní poloviny. Vadu má odpověď, algoritmus W
  ve svém vlastním zadání chybný není.
- C0070 je **low**, výslovně aktualizace výzkumné poznámky o R6,
  nikoli nepravdivá věta ani nové vyřešení sázkové KL náhodnosti.

Známé opravy 162 (n≥k), 173 (příklad a název transformace), 176
(rok, numerické údaje a text), 177 (normalita), úloha 26 a 42(b),
a definice času v P4 se pouze zohledňují; nejsou nálezy.

Přeskočené/otevřené body: historické bibliografické a experimentální
údaje se znovu nedohledávaly. Zejména Lovelandova konkrétní oscilační
mez na 178, historický faktorizovací benchmark na 176 a připsání
konstrukcí nejsou nově nezávisle ověřeny. Výzkumné úlohy 17,27,38
zůstávají výzkumnými formulacemi; aktuální stav jejich řešení se nyní
nehledal. Pro 27 je archivně doloženo oznámení 7/8, nikoli vlastní
reprodukce této konstrukce. Tvrzení v 176 jsou podmíněna hypotézou
obtížné faktorizace, nejsou její dolní mezí. Varianta bez masky navazuje
na 4.5.4–43. Původní historická zpráva na 158 zůstává partial.

Celé stránky 159–183 a 594–598 mají rozsah `First-pass review`;
599 je partial, protože následují odpovědi §3.6. Další kurzor:
§3.6, tištěná 184 / souborová 196. Žádné nové výpočty ani emaily.
