# DLX171: původní slova, náhrada2025 a symetrie

Kontrola 3. listopadu 2026. Přečteno celé zadání na str. 145 a odpověď
na str. 463 až k následujícímu číslu 172 na str. 464. Stejný rozsah
ověřen v autorském draftu na str. 81 a 167–168. Výčet slov v posledních
dvou řádcích je přímo odečten i z jejich souřadnic ve zdroji:

`muddy, thumb, books, knock, ended, apply, fifth, grass, civil, (refer or fewer)`.

Obě verze obsahují přesně tatáž slova a obě množiny se shodují se starými
ověřenými svědky. Původní textová extrakce posunovala čtyři slova na konec
strany; souřadnicové čtení i zobrazená stránka odstraňují tuto nejasnost.
Při parsování bbox byly v paměti odstraněny neplatné XML řídicí znaky
z nesouvisejících šachových glyfů níže na stránce. Surové bbox zůstalo zachované.

## E009: co je opravené a kde

Celá náhrada odpovědi z **2. ledna 2025** je už evidovaná jako E009.
Tentýž den se změnilo hodnocení úlohy z [25] na [35]. Jde o známou opravu,
nikoli nový nález. **Naše PDF ani draft ji neobsahují.** Správnou novou
konstrukci používá přijatý kontrolní model. Staré stručné „zapracováno“
proto v přehledu upřesňujeme; původní záznam i anglická karta jsou archivované
v [E009-before-source-review.json](results/petersen171/E009-before-source-review.json).

Původní nebarvené konce hran nejsou slučitelné s barevnými výskyty ve
zvolených slovech. Náhrada jim dává barvu 1 a každé hranové položce #uv
přesnou násobnost jedna. Opravuje také tvrzení o přesném násobku 120,
nahrazuje pokyny k odstranění symetrie a vypouští historický náklad 3,5 Tμ.
Údaj o dvou řešeních ve WORDS(834) zůstává stejný. Celé příslušné znění
errata je v [replacement-2025.textxt](sources/petersen171/replacement-2025.textxt).

## Správnost opraveného převodu

Petersenův graf má 10 vrcholů, 15 hran a 30 nehran. Primární položky
tvoří 10 vrcholů a 15 hran, sekundární položky 260 dvojic písmeno/vrchol,
780 dvojic písmeno/nehrana a jedno jméno pro každé slovo. Možností je
390 hranových a deset pro každé slovo.

Přiřazení slova vrcholu určí všech jeho 26 barev podle přítomnosti písmene.
U nehrany společné písmeno způsobí dva nebarvené výskyty téže sekundární
položky, což je zakázáno. U hrany se musí vybrat jedno písmeno s barvou 1
v obou koncích, tedy písmeno společné. Návrat od libovolného pokrytí proto
dává právě žádané „hrana právě tehdy, když společné písmeno“.

Obráceně lze pro každé platné přiřazení na každé hraně zvolit libovolné
společné písmeno a získat pokrytí. Více hran smí používat stejné písmeno
u téhož vrcholu, protože barevné sekundární výskyty s barvou 1 souhlasí.
Volby písmen jednotlivých hran jsou nezávislé. Počet rozšíření je tedy
součin velikostí patnácti průniků; nejde obecně o jednu jedinou MCC možnost.

Sekundární jméno slova vyloučí jeho opakování. U Petersenova grafu tím
žádné platné přiřazení neztratíme ani při čtení zadání bez výslovného
požadavku různých slov: dvě stejná neprázdná slova by tvořila sousední
vrcholy se stejnými sousedy mimo tuto dvojici. To tento trojúhelníků prostý
graf stupně tři nemá.

Příklad `added` má tři různá písmena a,d,e. Nesousedé vrcholu 0 jsou
2,3,6,7,8,9, přesně podle opravené možnosti. Ve starém omezeném vstupu
s 11 slovy je přímo ověřeno 25 primárních, 1051 sekundárních položek
a 500 možností. Původní dokončený počet 1920 zůstává přijatý bez opakování.

## Symetrie bez nového slovního výčtu

Starých 120 automorfismů působí pravidelně na orientovaných jednoduchých
cestách délky tři. Je jich 10·3·2·2. Slova jsou různá, proto je působení
na přiřazeních volné a každá orbita má přesně 120 označení vrcholů.
Každé z našich dvou přiřazení má navíc osm nezávislých výběrů hranových
písmen. Proto omezený MCC počet je `2·120·8 = 1920`, v souladu s opraveným
„at least 120“.

Nově je zkontrolovaná právě trojice **0,1,3** z náhradní odpovědi:
stabilizátor 0 a 1 má čtyři prvky a orbitu vrcholu 3 tvoří {3,7,8,9}.
Po zafixování 3 zbude pouze identita. Vrchol 2 je totiž jediný společný
soused 1 a 3; trojice tím určuje celou cestu délky tři.

Konkrétní správné pořadí můžeme vynutit těmito 14 nerovnostmi rangů:

- r0 je menší než všech ostatních devět rangů;
- r1 je menší než r4 a r5;
- r3 je menší než r7, r8 a r9.

V každé orbitě nejprve jednoznačně umístíme nejnižší rang na 0,
nejnižšího jeho souseda na 1 a nejnižší ze zbývající čtyřčlenné orbity
na 3. Nezbude žádná symetrie. Tento argument platí pro libovolných deset
různých rangů; u obou přijatých modelů byl navíc přímo prověřen přes všech
120 automorfismů. Starý slovní CSP používal jiné, rovněž dokázané pořadí
0,1,2,3. Jeho úplnost se tím nemění.

Pokyn o dodatečných sekundárních položkách je konstruktivní: pro každou
zakázanou dvojici slov porušující požadované pořadí zavedeme jednu
nebarvenou sekundární položku do obou příslušných vrcholových možností.
Zakáže právě společný výběr té dvojice. Přípustné dvojice se tím nemění.
Tento přímý důkaz nevyžaduje postavit velký rozšířený vstup.
Alternativní úprava řízení Algorithm C může tutéž podmínku kontrolovat
při volbě prvních tří vrcholových položek. Odkaz na 122 proto neznamená,
že by pouhá změna pořadí bez kontroly rangů odstranila symetrie, ani tím
neuzavíráme dřívější obecnou interpretační otázku C031 v úloze 122.

## Přijaté výčty a výslovné vynechání

Úplný dřívější CSP nad prvními 834 slovy našel dvě třídy. Obě obsahují
muddy s rangem 834, proto žádná není v prvních 833 slovech. Dřívější
nezávislý MCC běžel pouze na sjednocení 11 slov, nikoli na všech 834.
To je kontrola převodu a násobností, nikoli druhý úplný slovní výčet.
Oba rozsahy jsou zachovány přesně, žádný z těchto běhů se neopakoval.

Historický údaj **3,5 Tμ** z původní odpovědi znovu neměříme; oprava2025
jej navíc zcela vypouští. Je evidovaný jako výslovně vynechaná reprodukce,
nikoli jako nově ověřený údaj. Nová kontrola se týká zdrojového seznamu
a malé automorfismové grupy; nespouští hledání slov ani MCC řešič.

Celá 171 je **reviewed** s již známým E009. Strana 463 je tím celá
zrevidovaná; strana 464 zůstává částečná kvůli úloze 172. Další krok
je úplná kontrola obrázků a obecných tvrzení o šachových hadech.

- [Zdrojový seznam a báze 0,1,3](results/petersen171/source-checked.json)
- [Kontrola vrstev errat](results/petersen171/errata-check.json)
- [Původní matematické výsledky](PETERSEN_WORDS_NOTES.md)
