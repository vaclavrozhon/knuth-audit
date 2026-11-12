# MMIX-C0016 — Program P: jedna paměťová operace přiřazena nesprávné fázi

**Stav:** confirmed v doloženém digitálním vydání; kořenová revize přijata
v X0072 dne12.11.2026. **Závažnost:** low. **Rozsah:** knižní vytištěná
analýza, nikoli chyba doprovodného programu.

§1.3.2′, tištěná strana 37, souborová 45: místo
`10036μ + 641543υ` a `2804μ + 124559υ` pro fáze P1–P8 a P9–P11
mají být koeficienty μ **10037** a **2803**. Oba koeficienty υ i celkový
součet zůstávají správné. Nejde o rozdíl cache, překryvů pipeline ani
práce operačního systému; počítají se explicitně deklarované mems.

## Krátký rozpor, který nepotřebuje žádný běh

Podle strany 22 je mem počet load/store instrukcí. V řádcích 19–33
Programu P jsou právě dvě takové instrukce: STWU v řádku 21 a LDWU
v řádku 26. Každému DIV v řádku 27 bezprostředně předchází právě
jedno LDWU; neexistuje vstup nebo větev přímo na DIV. Text sám uvádí
9538 provedení tohoto DIV. STWU ukládá postupně PRIME[2] až PRIME[500],
tedy 499 hodnot; PRIME[1]=2 je sestavené datum, které sem nepočítáme.

Proto i při pouhém převzetí vytištěného počtu DIV musí být první
paměťový koeficient `9538+499=10037`, nikoli 10036. Ani chybně předem
uvedený počet DIV by nemohl zachránit vzájemnou konzistenci textu.
Následující úplný profil navíc potvrzuje, že právě 9538 je správně.

## Přesná kontrola všech profilových počtů bez spuštění MMIX

Správnost a ukončení generátoru, bezpečnost indexů a obou výstupních
cyklů se přebírají z V0086/V0089–V0092 v
`independent-arguments-028-032.md` a `independent-arguments-033-040.md`.
Podrobné argumenty pokrývají malé kladné n,pk, signed DIV, všechny
větve q/r, 500 prvků bez přístupu PRIME[501], a 1–4 decimal digits
bez zásahu do mezery či NUL. Zápisy probíhají jen v datovém segmentu,
globální báze jsou konstantní a dvouoperandové LDA se překládají do
jediné ADDU, protože potřebné offsety jsou 0,4,25,27. Nenastává
skryté rozšíření instrukce assemblerem.

`results/printed-prime-indices.json` již obsahoval úplný certifikát
všech prvočísel do 3571 a nejmenšího prvočíselného dělitele každého
kompozita. Síto se neopakovalo. Pro každé liché n=5,7,…,3571 určíme
počet testů takto:

* Je-li n složené a p jeho nejmenší prvočíselný dělitel, P6 se zastaví
  na p. Žádné menší testované prvočíslo r jej nedělí a nemůže dříve
  vyvolat P7, protože `n≥p²≥(r+1)²>r(r+1)`. Počet je π(p)−1.
* Je-li n prvočíslo, zbytek při testovaných dělitelích nikdy není nula.
  P7 nastane u prvního lichého prvočísla p splňujícího
  `floor(n/p)≤p`, ekvivalentně `n<p(p+1)`. Počet je opět π(p)−1.
  Hodnota p je menší než n a již byla uložena, jak zaručuje původní
  důkaz dostupnosti tabulky. Prime 3 se vloží bez takového testu.

Je 1784 kandidátů, z toho C=1286 kompozitů a A=498 nových prvočísel
(kromě 2 a 3). Součet uvedených uzavřených počtů je T=9538. Pro
každého kandidáta je rozhodovací certifikát uložen ve výsledku;
nejde o simulaci programu nebo o časově náročný nový benchmark.

Všech 15 řádků první fáze má následující počet. Normální větev je
předpovězena jako not-taken; chyba předpovědi přidá 2υ.

| Řádek | Počet provedení | Chybné předpovědi |
|---|---:|---:|
| 19,20 | každý 1 | 0 |
| 21,22,23 | každý 499 | u 23 právě 1 |
| 24,25 | každý A+C=1784 | 0 |
| 26,27,28,29 | každý T=9538 | u 29 právě C=1286 |
| 30,31 | každý T−C=8252 | u 31 právě A=498 |
| 32,33 | každý T−C−A=7754 | 0 |

DIV stojí 60υ, všechny ostatní zde 1υ plus zmíněné miss penalties,
LDWU/STWU navíc μ. Celkový počet υ lze zapsat

`641543 = 4 + 3·499 + 67T + 2A`.

To je nezávisle odvozený součet vytištěných instrukčních cest, včetně
úvodních dvou SET a závěrečné taken BZ. JSON obsahuje i jednotlivé
řádkové ceny; první fáze je přesně **10037μ+641543υ**.

Pro druhou fázi mají první čtyři prvočísla jednu cifru, dalších 21
dvě cifry, dalších 143 tři a posledních 332 čtyři. Počet všech cifer je

`D = 4 + 2·21 + 3·143 + 4·332 = 1803`.

Čte se 500 prvočísel pomocí LDWU, každý buffer se připraví jedním
STOU a každá cifra se zapíše jedním STBU. To jsou jediné load/store
instrukce této fáze, takže přesně `500+500+D=2803` mems.
TRAP má deklarovanou cenu 5υ a samotný handler se podle textu nepočítá.

V úvodní části jsou LDA/TRAP/NEG po jednom, v každém z 50 řádků
ADD/LDA/TRAP a pak deset položek. U položky jsou LDWU, STOU, LDA
jednou; DIV/GET/INCL/STBU/SUB/PBNZ pro každou cifru, s jedním chybným
PBNZ na položku. Následují LDA/TRAP/INCL a sloupcové PBN, chybné
jednou na řádek. Na konci řádku LDA/TRAP/CMP a PBNZ, chybné pouze
na posledním řádku; nakonec TRAP Halt. Všechny větve jsou tím
vyčerpány a dávají

`7 + 7·50 + 3·500 + (65D+2·500) + 7·500`
`  + (500+2·50) + 7·50 + (50+2) + 5 = 124559`.

Druhá fáze je tedy přesně **2803μ+124559υ**. Celkem zůstává
`12840μ+766102υ`. Oprava přerozdělí právě jeden mem mezi fázemi;
nepoškozuje správnost tabulky ani celkový čas.

## Reprodukce, originál a všechny vrstvy errat

Jediný nový cílený výpočet:

```
nice -n 15 python3 workstreams/vol1-fasc1/verify_program_p_profile.py
```

Skript jen sečetl výše dokázané profily z uložených certifikátů.
Výstup `results/program-p-profile.json`: T=9538, D=1803, obě fáze
podle opravených vzorců. Nebyl spuštěn MMIX, assembler ani opakované
síto, žádný starý běh se nerestartoval.

Zobrazeny originály file 41/p33, 42/p34 a 45/p37. Původní knižní PDF
je digital release 3 z května 2023, SHA256
`16f86d86839647a0c99be829a537a7516577704393ad8f95492ab42119905666`.
Fyzický dotisk nebyl prohlédnut. Strana 22 a primární MMIX doc
3235–3273 explicitně rozlišují počet mems, cenu DIV/branch/TRAP a
vyloučení instruction fetches; nelze zde přičíst assemblerová data,
instruction fetch nebo skrytý hostitelský výstup.

`results/errata-C0016.json` zaznamenává SHA256 a konkrétní kontexty
deseti vrstev: původní zdroj, krátká a dlouhá fasciklová errata;
MMIXware errata, current package, upstream bugs, rounding notes a
aktuální warnings changefile; navíc dlouhá i zdrojová errata svazku 1
kvůli možnému přesunu z příbuzného MIX Programu P. Žádná neobsahuje
odpovídající opravu. Změna p34 řádku 40 pouze zpřesňuje komentář
`mm←−2` a je již v naší sazbě; p37 mění pojmenování znaku #.
Oprava MIX Programu P na p148 mění EQU −1 na EQU 99 a těchto MMIX
časů se netýká. Výskyty p148 v MMIXware jsou memory-mapped I/O;
výskyty section37 jsou gramatická oprava či typ Char. Všechny tyto
kontexty byly přečteny, nikoli jen vyhledány podle čísla.

Doplňkový dotaz na autorově a MMIX primárním webu podle přesných
čísel nevrátil související opravu. Netvrdí se světové prvenství,
jen doložený rozpor v našich zdrojích a absence ve zkontrolovaných
veřejných vrstvách. Návrh opravy je pouze dvě změny koeficientů μ.
