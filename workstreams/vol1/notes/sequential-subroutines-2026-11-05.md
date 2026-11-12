# Souvislý průchod §1.4 a §1.4.1 — 5. listopadu 2026

Přímo porovnány originály 186–193 a odpovědi 527–528, přijaté obecné
důkazy v `parallel/subroutines/notes/subroutines.md`, pramenná recenze
`parallel/subroutines/notes/sources.md` a uložený výsledek
`parallel/subroutines/results/subroutines.json`. Nejde o nový běh
29 520 kontrol. Čtyři nynější vrstvy errat byly znovu prohledány;
výpis s otisky je v `sources/sequential-2026-11-05/subroutines-errata-extract.json`.

## Text a matematika

Maximum drží invariant nejpravějšího maxima již prošlého suffixu.
Úspora při m výskytech k instrukcí a základní vazbě je
(m−1)(k−1)−3 slov, takže při k=2 je kladná až pro m>4.
Volání, uložení návratu a návrat stojí 1+2+1=4u. Obecně pro c slov
volání a L slov vazby vychází (m−1)(k−c)−(c+L).
STJ musí předcházet skoku, který přepíše J; pomocný vstup MAX50
proto buď použije JSJ, nebo uloží J sám před obyčejným JMP.

Uchování I3 pomocí ST3 do pole (0:2) budoucího ENT3 zachovává
i zápornou nulu a stojí dvě instrukce, 3u. Tvrzení o nejkratší
úpravě se vztahuje k tomuto způsobu zachování registru dané rutiny,
nikoli ke globálně nejrychlejšímu algoritmu maxima. Argument za
voláním se přečte přes uložený návrat; posun výstupu o jednu buňku
jej správně přeskočí. Obal MAX100 musí uložit vlastní návrat
před zavoláním MAXN.

Ve variantě se dvěma výstupy zůstává I3=0 pro max≤0 nebo max≥X;
jinak se nastaví na1. Indexovaný návrat proto vybere správnou
ze dvou adres. Výslovná pomocná buňka TEMP je součástí konstrukce.
Při A→B→C→A se bez zásobníku přepíše první návrat A. Sdílení TEMPj
je bezpečné pro popsaný nerekurzivní graf: potomci mají nižší
intervaly než rodič, sourozenci nejsou současně aktivní.
Rady k návrhu a ladění jsou zkušenostní doporučení, nikoli
matematická záruka rychlosti či produktivity.

## Sedm úloh

1/2 odpovídají společným vstupům MAXN/MAX100 a uložení J před JMP.
5 správně předává návrat jiným registrem; A se ukládá do adresy
návratové instrukce dříve, než jej výpočet maxima přepíše.

**C0030 zůstává potvrzeno, high, původní odpověď527.** Zadání výslovně
žádá nekladné I1. Pro q=I1≤0 program M na145 neprovádí normalizaci
na n=1: přímo načte X[q], nastaví I2=q, sníží I3 na q−1 a skončí.
Při platných adresách a reprezentovatelném q−1 tedy A=X[q], I2=q,
I3=q−1, I1 a CI beze změny, J=EXIT+1. Pro q=0, X[0]=5, X[1]=7
dostaneme (5,0,−1), nikoli vytištěné (7,1,0). Pro q≥1 odpověď
včetně rozlišení posledního porovnání s X[1] platí. Neplatné adresy
nebo přetečení indexu nejsou dodatečně definovány domnělou opravou.

**C0031 zůstává potvrzeno, low, výstupní kontrakt528.** Při vstupu
SMAX1 se provede ENT1 1; vstupní podmínky přitom I1 neomezují.
Konvence na188 říká, že neuvedené registry zůstávají beze změny.
Již n=1, počáteční I1=2 poruší tento slib. Stačí uvést I1=1 pro
SMAX1; obecný vstup SMAX původní I1 zachovává. Maximum i konečný
I3=(n−1) mod r+1−r=−((-n) mod r) jsou správné. Není důvod tento
malý popisný nedostatek hodnotit stejně jako chybný výsledek C0030.

6: u MOVE se nejprve uloží A, I2 a návrat, efektivní adresa se
vyhodnotí s obnoveným I2 a původním I1. Při F=0 se nic nekopíruje;
jinak se čte a zapisuje v rostoucím pořadí, takže i překryv souhlasí
s nativním MOVE. Zdrojový i cílový konec nejvýše4000 se vejde do
dvoubajtového registru pro všechny povolené báze. A, I2, jejich
znaménka, CI a overflow se zachovají; změna J je dovolena. Známá
oprava zadání přidává spotřebu pomocného prostoru. 7 uvádí důvody
pro čistý sdílený kód v popsaném prostředí; není důkazem absolutní
nemožnosti synchronizovaného samomodifikujícího programu.

## Fakta, bibliografické výjimky a mapa

Přijata konkrétní pramenná recenze Wirth1971 a Dijkstra EWD249;
přesná sazba knižního přetisku1972 zůstává přeskočena. U Knuthova
Literate Programming ověřen rok, obsah a kapitola11; neprohlašuji
znovu přečtený celý deník chyb1978–1991. Původní Turingův strojopis,
strana18, byl znovu přímo zobrazen: citace odpovídá, [bugs] je
vyznačené redakční doplnění. Rozdíl1945/1946 mezi vznikem rukopisu
a předložením návrhu není prokázanou chybou. Odkazy na budoucí
kapitoly8/10 a MMIX odpovídají vydání1997, nikoli dnešnímu tvrzení
o dostupnosti těchto kapitol.

X0203: úprava slovního spojení na186 je stylistická; červeně se
mapují skutečné vady EXIT C na190 a příliš silné omezení zadání
MOVE na193. Žádná ze čtyř vrstev neopravuje C0030/C0031.
Celý oddíl a všech sedm úloh jsou v tomto vymezení uzavřeny.
Strana527 se uzavírá spolu s předchozí kontrolou permutací.
Nová neznámá chyba0; žádné emaily ani nové dlouhé výpočty.
