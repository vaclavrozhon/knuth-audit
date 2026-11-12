# V2-C0112: tři překlepy v opraveném příkladu převodu tam a zpět

**confirmed**, 2. listopadu 2026. Historické erratum `all2-prepre`,
strana souboru 39, položka **Page 638 last two lines of answer 18,
15 Apr 1999**; jde o §4.4-18 třetího vydání TAOCP2.
Původní [sazba errata](../images/radix-all2-prepre-39.png) a
[odpověď 1997](../images/vol2-p638.png) byly vizuálně přečteny.

Erratum uvádí při binární přesnosti 10 a desítkové přesnosti 4:

```text
round((.1111111001)_2 * 2^784) = .1011 * 10^236,
round(.1011 * 10^235) = (.11111110010)_2 * 2^784.
```

V obou desítkových zápisech má být exponent **237** a výsledná
binární mantisa má být **1111111010** (deset číslic).

Položme u=1017*2^774 a U=1011*10^233. Následující dvě přesná
celočíselná porovnání certifikují správné zaokrouhlení v obou směrech:

```text
2021*10^233 < 2u < 2023*10^233,
2035*2^774  < 2U < 2037*2^774.
```

První interval je vymezen dvojnásobky středů sousedních čtyřmístných
desítkových čísel kolem U. Druhý je vymezen dvojnásobky středů
desetimístných binárních čísel kolem 1018*2^774. Obě volby jsou
tedy jednoznačné a nezávislé na pravidle pro přesné poloviny.
Správný výsledek je

```text
round_10(u,4) = .1011 * 10^237,
round_2(.1011 * 10^237,10) = (.1111111010)_2 * 2^784.
```

Tištěná jedenáctimístná mantisa 11111110010 představuje přesně
stejné číslo jako původní desetimístná 1111111001, protože pouze
připojuje koncovou nulu. Nemůže tedy demonstrovat zamýšlenou změnu
hodnoty. Chyba není důsledkem OCR, odlišné normalizace ani vazby
v přesné polovině.

Výraz „smallest example“ navrhujeme upřesnit na „smallest positive
integer example“. Mezi libovolnými kladnými reálnými vstupy
nejmenší protipříklad neexistuje, viz obecný důkaz v
[radix-round.md](radix-round.md). V celočíselném rozsahu jde
skutečně o první selhání: úplný průchod všech 397304 menších
kladných celých čísel s nejvýše deseti významnými binárními číslicemi
neselhal; další vstup je právě u. Toto je konečný vyčerpávající
certifikát v explicitně uvedeném rozsahu, nikoli samotný náhodný test.

Zdroj a výsledky: `verify_radix_round.py`, bloky examples/minimum
v `results/radix-round.json`; přesné nerovnosti jsou kontrolovány
samostatně od funkce zaokrouhlení. Úspěšné checkpointy nebyly
opakovaně spouštěny. Podrobnosti relací uvádí hlavní poznámka.

Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2`, včetně
638,784,235,236,237,Tydeman a číslic mantisy. Původní oprava
z roku 1999 je známá; její tři překlepy jsou zde potvrzený nález.
Pozdější oprava nebyla nalezena. Poslední fyzický dotisk a priorita
neověřeny; [návrh hlášení](../reports/C0112-radix-roundtrip-example-draft.txt)
zůstává neodeslaný. Nález nevyvrací správnou Matulovu větu.
