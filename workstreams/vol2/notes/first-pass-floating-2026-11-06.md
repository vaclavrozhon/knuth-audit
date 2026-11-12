# §4.2.1 — první průchod plovoucí aritmetikou

6. listopadu 2026, V2-X0134. Přečteny celé strany 214–228 a odpovědi
§4.2.1 na 611–613. Převzaty uzavřené důkazy, modely MIX a kontrola
errat z `single-precision.md`, `mix-float.md`,
`single-precision-context.md`. Žádný nový nález, běh simulátoru,
enumerace ani nové dokazování maxima běhového času.

Posouzeny A/N/M, přenosy a zaokrouhlení, nuly, podtečení/přetečení,
převody, všech 19 zadání i odpovědí. Matematické kontroly a archivní
rozlišení abstraktních algoritmů od konkrétního MIX kódu se přebírají.
Známé opravy fyzikálních konstant, programů a odpovědí jsou pouze
zohledněny; nevytvářejí karty chyb. Hodnoty konstant jsou dobové příklady
s publikovanými aktualizacemi, nikoli nově objevená chyba.

C0082 zůstává **candidate**: odříznutí v pevném místě vyváženého
trojkového zlomku je správné zaokrouhlení tohoto zlomku, ale nemusí dát
nejbližší hodnotu přes hranici plovoucích exponentů. Rozhoduje zamýšlený
výklad odpovědi, proto z tohoto příkladu neděláme potvrzenou chybu.

Historické výjimky z `single-precision-context.md` zachovány: celý
originál WWG, některá prvenství raných počítačů a původní Zuseho patent
nebyly získány; přesný rok prvního vydání Torresova textu nebyl uzavřen.
Převzaté primární reprinty podporují popsané dílčí závěry, ne všechna
historická prvenství. Bibliografie není znovu plošně ověřována.

Strany214–228 jsou reviewed v rozsahu prvního průchodu. 611 zůstává
partial kvůli C0081 v předchozí sekci; 612 kvůli C0082; 613 kvůli
následujícím odpovědím §4.2.2. Kurzor229/file241.
