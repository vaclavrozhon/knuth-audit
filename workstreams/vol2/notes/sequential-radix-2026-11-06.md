# §4.4 — převody soustav, jednotlivé argumenty a 19 úloh

6. listopadu 2026, V2-X0141. Původní text 319–329 a odpovědi
635–638 jsou přečteny. Jednotlivá matematická tvrzení a každá úloha
mají odkaz na již uzavřený argument v
`results/sequential-radix-evidence.json`. Staré simulace, census
nejmenšího celočíselného protipříkladu ani benchmarky se neopakovaly.

Přebíráme invarianty čtyř základních metod, smíšených základů,
nejkratšího přesného výstupu, konečných rozvojů a BCD operací
(`radix-basic.md`). Záporný základ včetně krajů zlomkového intervalu,
ruční převody a jejich tabulky mají obecný argument v
`radix-hand-negative.md`. Kontrola devítkou není bezpodmínečná
89% záruka; vyžaduje model rovnoměrných zbytků. Půlení při hledání
chyby také může minout chybný mezivýsledek dělitelný devíti.

Blokové metody a aritmetický invariant tiskového programu jsou
v `radix-print.md`. Převod s přesným zaokrouhlením a Matulova nutná
i postačující podmínka mají vlastní obecné důkazy v `radix-round.md`,
včetně hustoty násobků iracionálního logaritmu a nerovnoměrného
rozestupu sousedů u mocnin základu. Optimální implementace Dragon4
ani Bellerophon se tím neprohlašují za nezávisle ověřené.

Úlohy 14 a 16 mají důkaz časové meze a explicitní místní automaty
v `radix-fast.md`. **Úloha 15 zůstává partial:** audit modelů a
známých horních mezí není řešením výzkumné otázky. Dosavadní důkazy
zůstávají platné; opravuje se pouze příliš široký stav „checked“.
Sekce má nyní 18/19 úloh uzavřených v doloženém rozsahu.

Pět již doložených vad zůstává potvrzených, bez nového nálezu:

- C0108 **low**: postačující mez konstanty je mylně označena jako
  nutná. Správná dolní mez je D−gcd(w,D); původní program funguje.
- C0109 **medium**: převod bez dělení používá dolní aproximaci 1/10
  a v dalších iteracích starý vstup. Již u=10 vytvoří neplatnou
  číslici 10. Oprava obou míst a její důkaz zůstávají uloženy.
- C0110 **low**: Hornerův program pro m+1 číslic provádí m operací
  každého druhu, nikoli m−1.
- C0111 **medium**: dva dvacetislovné buffery neodpovídají
  čtyřiadvacetislovnému bloku tiskárny. Druhý výstup čte instrukce;
  první se může překrýt s přípravou druhého. Aritmetika je správná.
- C0112 **low**: tři překlepy v číselném příkladu přidaném erratem
  z roku 1999. Jde o vady náhradního textu, nikoli o původní již
  opravenou chybu. Matulova obecná věta je správná.

Všechny relevantní vrstvy errat byly prověřeny v původních blocích;
jejich důkazy přebíráme. Známé náhrady úloh 9 a 11 ani oprava roku
Goldstine–von Neumann 1946→1947 nejsou naše nálezy a nejsou kartami.
Bibliografie má přesně omezený rozsah v `radix-context.md`: například
Legendreho výpočet a Koonsův–Lubkinův teleskopický argument jsou
ověřeny, nedostupná původní vydání a tvrzení o prvenství zůstávají
výslovně neověřena. Nejnovější fyzický dotisk nebyl zkontrolován.

Strana 328 zůstává partial kvůli výzkumné úloze 15; strana 638
kvůli začátku odpovědí následující sekce. Strana 635 je nyní
spárována z obou stran hranice sekcí. Další kurzor je 330/file342,
§4.5 a §4.5.1, racionální aritmetika a zlomky.
