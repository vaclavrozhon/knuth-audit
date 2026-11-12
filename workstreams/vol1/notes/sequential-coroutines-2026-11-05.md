# Souvislý průchod §1.4.2 — 5. listopadu 2026

Přímo přečteny originály193–200 a529. Porovnána celá poznámka
`parallel/subroutines/notes/coroutines.md`, pramenná recenze
`parallel/subroutines/notes/sources.md`, vlastní úplný encoder
`parallel/subroutines/results/inverse-encoder.mixal` a uložené
výsledky `parallel/subroutines/results/coroutines.json`.
9 398 úspěšných kontrol se neopakuje. Čtyři aktuální vrstvy errat
znovu porovnány v `sources/sequential-2026-11-05/subroutines-errata-extract.json`.

## Program a text

Invariant vazby: při předání A→B se změní pouze pokračování A;
slot B stále obsahuje jeho předchozí bod obnovení. Indukce platí
od počátečních A1/B1 a režie je4u včetně volajícího JMP.
NEXTCHAR udržuje neodebrané znaky v X a ukazatel dalšího slova v I6.
Nulové bajty jsou mezery; SLAX přesouvá nejbližší znak do vynulovaného A.
Čekání JBUS zajišťuje dokončení čtení před použitím nové karty.

Číslice d dává d+1 kopií následujícího znaku, i když je číslicí.
Vzorový řetězec i jeho tříznakové skupiny souhlasí; poslední znak
skupiny220 a první znak0PQ jsou nuly. První vydaná tečka končí
výpočet i uvnitř replikace. OUT po třech znacích posune I4 a po48
znacích vydá kartu; před opětovným nulováním bufferu počká JBUS.
Zachovává A, X, I5 a I6, ale mění I1 i I4. Chybějící I4 v popisu
je známé erratum2018, nikoli nový nález. Překrývající MOVE vyplní
buffer mezerami. Počáteční vstup do OUT připraví buffer dříve,
než IN předá první znak.

Uložení jediného A v(4) stačí, má-li je zachovat pouze IN; pro obě
korutiny jsou nutné dva samostatné snímky. Obr.22 správně zachovává
pořadí čtyř fází. Úspora mezilehlého I/O má uvedenou protiváhu ve
větším paměťovém nároku. Zpětná závislost na další fázi a potřeba
souhrnu celého vstupu výslovně omezují převod mezi průchody a
korutinami. Vtip a odkazy nevytvářejí další matematické tvrzení.

## Všech sedm úloh

1: „only once“ znamená jediné místo v programu, jak upřesňuje
následující věta. 2: při nesprávném prvním vstupu do IN se ztratí
první expandovaný znak; navržená předinicializace bufferu a první
vstup OUT na řádek39 to opravují. Ztratit se může i první tečka.

3: původní zkrácená rutina má neinitializovaný CI. A. s CI=equal
skončí po A; 0.A. s CI=less vydá .A. Známá oprava2006 přidává
počáteční CMPX PERIOD a CMPA PERIOD pro replikovaný znak. U přímého
znaku alespoň30 nastaví dřívější CMPA =10= rovnost právě pro
tečku40; znaky pod30 zachovají nerovný CI. Indukce potvrzuje celou
opravu i zachování CI mezi korutinami.

4: z přijaté recenze původních manuálů plyne přesná sémantika.
IBM650: prázdná datová adresa LDD se v SOAP doplní adresou další
zdrojové instrukce; STD uloží celé pokračovací slovo. IBM709:
TSX na p uloží dvojkový doplněk p; SXA a AXT jej uchovají a
TRA1,4 odečtením indexu vytvoří p+1. CDC1604: SLJ4 přepíše horní
adresu cílového slova a začne jeho dolní instrukcí; ALS0 a dolní
SLJ správně propojí dvě sousední slova. To není totéž jako
nesprávně předpokládaný skok do jejich horní půlky. Původní
manuály650/709/1604 a SOAP byly dříve přímo čteny, dnes přijata
jejich recenze; žádná nová emulace historického stroje.

5: dvě uložená A se při předání vymění ve správném pořadí.
6: každá orientovaná hrana má STJ a JMP, tedy2m slov a při úplné
síti2n(n−1). Konstrukce 3n+2 s rezervovaným I1 používá pro každé i
STJ0,1; ENT1Xi; Xi JMPstart_i a dvě inicializační instrukce.
Před uložením odchodu I1 stále ukazuje na starý aktivní slot;
teprve potom se nastaví nový. Libovolná posloupnost přechodů tak
zachovává invariant.

7: pro souvislý úsek n=10q+r stejných znaků je minimum
2 ceil(n/10) u číslice a2q+min(r,2) jinak. Jednotka kódu nepřejde
přes hranici dvou různých znaků. Dvojice vydá nejvýše10 znaků;
samostatný nečíselný znak právě1. Kód délky t proto vydá nejvýše
10 floor(t/2)+(t mod2) nečíselných znaků. Dolní mez je dosažena
bloky9c a optimálním zbytkem; samostatná číslice vyžaduje0c.
Tečka stojí1 a ukončí vstup. Encoder nevytváří přetečení délky
dlouhého běhu, protože každou desítku ihned vydá. PUTCHAR střídá
pět přípustných polí, čeká na výstup a po tečce přesně na hranici
karty nevydá prázdnou kartu. Nejkratší vzor je A2B5E3426FGZYW3210PQ89R.
Přijaté testy zahrnují nezávislou dynamickou optimalizaci délky.

## Stav a mapování

Žádný nový neopravený rozpor. Všech sedm úloh i hlavní text jsou
uzavřeny. X0212 mapuje skutečné opravy194,196,197,198,529;
pouhé rozšíření mezer195 není samo obsahová chyba a nebarví stránku
červeně. Na200 zůstává spodní začátek interpretů otevřen do dalšího
bloku. Strany193/527 sdílejí důkaz s okolními sekcemi; nezaměňuji
dokončenou úlohu s dokončenou celou stránkou. Odkazy na kapitoly8/10
jsou dobové plány, §1.4.4 a §2.2.5 platné vnitřní odkazy.
