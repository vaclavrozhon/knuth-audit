# MMIX-C0021 — rG neodečítá každý výskyt GREG

Confirmed, low, book; nezávislá kořenová revize přijata v X0074 dne12.11.2026.
Jde o první větu odpovědi§1.4.1′–10 na p114/file122.
Není to chyba assembleru ani nový nedostatek algoritmu maxima.

Věta určuje počáteční rG jako255 minus počet sestavených GREG
operací. V obyčejném výchozím MMIXAL se však opakované nenulové
počáteční hodnoty slučují do téhož globálního registru. Dva
takové řádky mohou tedy snížit rG jen jednou.

Úplný zdroj `sources/greg21-coalesced.mms` má dva různé labely:

```
A       GREG    1
B       GREG    1
        LOC     #100
Main    GET     $255,rG
        TRAP    0,Halt,0
```

Není zde žádná další GREG báze, future reference, změna rG
v programu ani opakovaná definice téhož symbolu. Nulové hodnoty,
které se záměrně neslučují, nejsou použity. Obě jedničky jsou
platné nenulové constant/base initializers a program je nemění.

Primární `mmixal-20131017.w` i`mmixal-20250620.w` v oddílu
`Allocate a global register` mají byteově stejnou rozhodovací
větev. Greg začíná255. Při prvním řádku je interval hledání
[greg,255) prázdný, takže se provede greg-- na254 a uloží
greg_val[254]=1. Při druhém řádku je hodnota opět nenulová;
jediná iterace j254 zjistí shodu obou32bitových polovin a
`goto got_greg` přeskočí decrement i nový zápis. Cur_greg
zůstane254, stejně jako celkové greg. A iB proto označují$254.

Závěrečný mmo postamble předává přesně greg a loader jím
nastaví G; tento přenos je přímo uveden v primární dokumentaci
GREG. Správné počáteční rG je **254**, zatímco vytištěná
formule pro dva GREG řádky dává **253**. GET by tento rozdíl
přímo zpřístupnil; pro důkaz není potřebný nový build ani běh.
Samotná dokumentace výslovně říká, že stejné nenulové báze
dostanou stejné číslo registru, a mluví o odlišných alokacích.

Pro posloupnost již známých konstant je obecný invariant:
každý nulový GREG přidá nový registr, každá dosud neviděná
nenulová hodnota také, opakovaná nenulová hodnota žádný. Proto
po z nulových řádcích a d různých nenulových hodnotách je
G=255−z−d, pokud sestavení nevyčerpá povolené globální registry.
Nejde o pouhý jeden číselný příklad nebo odhad chování.

Oprava věty: odečítat počet GREG operací, které **skutečně
alokují nový registr**, případně prostě říci, že počáteční rG
určují GREG deklarace. Druhá věta o počátečním rL2 je správná.
Další úvaha o zaměnitelnosti registrů vyžaduje vlastní přesné
podmínky inicializace; tento nález ji sám nevyvrací ani neuzavírá.

Originál file122 byl zobrazen jako
`images/recovery-subroutine-answers-122.png`; čitelná věta
opravdu nemá podmínku odlišnosti/neslučování. Vydání je původně
evidované digital release3, květen2023; fyzický výtisk zůstává
neprohlédnutý. Primární assembler2013 předchází tomuto vydání,
takže nejde o zpětné přisouzení nové změny z2025.

`results/errata-C0021.json` eviduje všech13 veřejných vrstev
s SHA256 a kontextem shod. Jediná věcná oprava odpovědi na114
je přidání PUT rJ do **odpovědi9**; správně je již v této sazbě.
Další GREG výskyty jsou kód semaforů, zarovnání odpovědi116,
index MMIXAL nebo ukázka rounding programu. MMIXware§114
opravuje stack-alert a rL, nikoli počet GREG. Ostatní svazkové
výskyty114 jsou matematické formule/bibliografie. Žádný
z těchto záznamů nedoplňuje slučování do zkoumané věty.
Nejde o tvrzení světové novosti a žádná zpráva nebyla odeslána.

Vzorové zásady: přesný přípustný vstup a všechny větve alokace;
oddělení vadné věty od správné implementace; originál a všechny
relevantní errata před confirmed. Žádný experiment či starý
verifier nebyl spuštěn.
