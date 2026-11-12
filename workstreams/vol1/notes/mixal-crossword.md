# §1.3.2-23: vstup, číslování a tisk křížovky

Originál s.163 s obrázky18–19 a všemi pěti vzory vnějšího pole byl
zobrazen1.listopadu2026. Čtyři řady errat potvrzují dvě známé opravy:
10.7.1997 what→white v podmínce pro vodorovné slovo;18.1.2008
upřesnění, že příklad vstupní karty odpovídá hornímu řádku matice.
Kniha nedává hotovou odpověď23. `mixal_crossword.py` je náš úplný
MIX program podle předepsaného postupu, nikoli přepis autorova řešení.

## Odstranění vnější černé oblasti

Vstupní čtverec řádu n obsahuje0 pro bílé a1 pro černé pole.
Přidáme obvod z−1 a opakovaně měníme1 na−1, má-li takové pole
souseda−1 přes společnou stranu. Pouhý dotyk rohem není sousednost.
Záporné pole označuje část mimo výsledný obrazec, nikoli černé pole.

Indukčně každá změněná jednička patří do černé oblasti spojené
s obvodem: změna vždy prodlužuje již nalezenou cestu. Naopak vezměme
nejkratší cestu od obvodu k libovolné černé buňce této oblasti.
Po nejvýše tolika úplných průchodech, kolik má cesta černých buněk,
je celá cesta záporná. Aktualizace během jednoho průchodu to může
pouze urychlit. Po zastavení tedy zbývají právě uzavřené černé oblasti.

Počet kladných buněk při každém neprázdném průchodu klesne; nejvýše
n² změn a jeden poslední průchod bez změny dokazují ukončení. Tím
je pokryta i klikatá cesta proti směru procházení, nikoli jen černé
buňky na původním okraji. Jednoduchá realizace má hrubou obecnou mez
O(n^4); účelem není optimální vyplňovací algoritmus. Nezávislý
validátor používá frontu a prochází každou černou buňku nejvýše jednou.

## Čísla začátků slov

Slovo zde znamená maximální vodorovný nebo svislý souvislý úsek
alespoň dvou bílých polí. Jeho začátek má další bílé pole ve směru
čtení a nemá bílé pole bezprostředně před sebou. To je přesně
opravená místní podmínka v zadání. Očíslujeme sjednocení obou množin
začátků, po řádcích shora dolů a uvnitř řádku zleva doprava.
Začátek obou slov se započte pouze jednou. Hodnoty matice při
číslování neměníme; čísla ukládáme do samostatného pole LABELS.

Pro obrázek18 vychází14 čísel; nula v této pomocné tabulce znamená
pouze nečíslované pole, bez rozlišení jeho barvy:

```
00 01 00 02 03 00
04 00 00 05 00 06
07 00 08 00 00 00
00 00 09 00 10 00
11 12 00 00 13 00
00 14 00 00 00 00
```

Samotný příklad6×6 se pro požadovaných23 vstupních karet doplní
černými jedničkami vpravo a dole. Po odstranění vnějšku se výsledný
obrazec nezmění. První karta má100001 následované17 jedničkami,
což souhlasí s příkladem zadání po známém upřesnění2008.

## Pětiznakové dlaždice a obrys

Jedno pole reprezentují tři tiskové řádky po pěti znacích. Bílé
pole má v prvních dvou řádcích čtyři mezery a plus, ve třetím pět
plusů. Černé pole má všechny znaky plus. První řádek číslovaného
bílého pole navíc obsahuje číslo od prvního znaku. Popisky1..99
píšeme dvojciferně, jako v obrázku19; větší číslo zabere tři ze
čtyř vnitřních sloupců. Symbol nn v zadání je zde vzor popisku,
ne omezení rozsahu: platný23×23 vstup může mít více než99 začátků.
Například64 oddělených bílých bloků2×2 má192 začátků. Nejvýše529
čísel se stále vejde do tří číslic a předepsaných pěti sloupců.

U záporného pole označme R,B,D tvrzení, že soused napravo, pod ním,
respektive vpravo dole není záporný. První dva tiskové řádky mají
poslední znak plus právě při R. Spodní řádek je celý z plusů při B;
jinak má jen poslední plus při R nebo D a je prázdný v ostatních
případech. To dává přesně pět vzorů z původní stránky. Diagonální
soused je potřeba k rozhodnutí mezi posledními dvěma vzory.

Proč toto pravidlo kreslí správný obrys: svislá hrana uvnitř
záporné dlaždice odděluje její pravého viditelného souseda; vodorovná
hrana odděluje dolního souseda. Jejich společný koncový bod musí být
plus i tehdy, když jediným viditelným sousedem je diagonální pole.
Každá hrana a každý roh viditelného obdélníku jsou tedy pokryty,
a žádná jiná čára se nepřidá. Bílá a černá dlaždice obdobně pokrývají
své vlastní pravé a dolní hrany. Nezávislý validátor místo těchto
místních pravidel kreslí celé obdélníky všech viditelných polí a
sjednocuje jejich hrany; porovnání se týká každého výstupního znaku.

Vlevo je nutný jeden pomocný sloupec dlaždic;23 polí proto vyžaduje
24×5=120 znaků, přesně šířku tiskárny. Z pomocného horního řádku
se tiskne pouze dolní linka, protože jeho první dva řádky jsou
prázdné. Zcela vnější spodní řádky se vynechají podle posledního
viditelného řádku; prázdné řádky uvnitř obrazce se zachovají.
Je-li celý vstup černý, po odstranění vnějšku se netiskne nic.
Výstup příkladu má19 řádků, úplný23řádkový obrazec nejvýše70 řádků.

## Strojové invarianty a meze

Program podporuje1<=n<=23; n=23 je požadovaná úloha. Rozšířená
matice má krok S=n+2 a leží od X=500; samostatná stejně velká
matice čísel od LABELS=1200. Celá rozšířená matice je před čtením
nastavena na−1, všechna čísla na0. Každá vstupní karta přinese
16 slov po pěti znacích. IN a následné JBUS zajišťují, že data
jsou hotová před čtením. Rozvinuté načítání prvních n znaků odečte
od jejich kódů30 a uloží přesně0 nebo1; ostatní sloupce karty ignoruje.

Procházení používá jediný index od S+1 do nS+n včetně. Výplňové
okrajové buňky mezi řádky zůstávají záporné a přeskočí se. Sousedé
se načítají jen u vnitřních kladných/bílých buněk; při kreslení
jsou indexy0..nS+n a nejvzdálenější čtení přidává S+1. Všechna
čtení proto leží uvnitř (n+2)² buněk včetně obvodu.

Při23 je nejvyšší index624, číslo nejvýše529 a nejvyšší adresa
použitých polí1824. Tři tiskové buffery mají po24 slovech od2200,
2224 a2248; vstup začíná2300. Kód včetně konstant končí pod500.
Indexy se vejdou do dvou nejmenších MIX bajtů, protože624<64².
Dělení při výpočtu posledního řádku má nulovou horní polovinu A
 a malý kladný dělitel S, takže nemůže přetéct. CHAR a zápisy
vybraných polí přenášejí poslední dvě/tři číslice na začátek dlaždice.

Před vytvářením dalšího řádku se čeká na skončení tisku, všechny
72 výstupní buňky se výslovně nulují, a OUT jednotlivých řádků
odděluje JBUS. Žádný aktivní vstupní či výstupní buffer se nepřepisuje.
Po posledním OUT je pouze ukončení; hostitelský model nechá poslední
výstupní operaci doběhnout. Nepředpokládá se počáteční nulová paměť.

## Výsledek kontroly

4212 kontrol v601 úplných MIX bězích prošlo napoprvé. Všechny37
radixe64..100 byly ověřeny na požadovaném23×23 formátu s příkladem.
Vyčerpány byly všechny binární vstupy řádů1,2,3; dále24 náhodných
případů a oba krajní radixe s dlouhou vnější cestou, uzavřeným
černým ostrovem,192 čísly a zcela bílým/černým vstupem. U těchto
mezních případů měly periférie zpoždění1000u. Celá výsledná matice,
všechna čísla i celý tisk souhlasí s nezávislými konstrukcemi.
Úspěšný checker bez změny neopakovat. Nová chyba knihy nezjištěna.
