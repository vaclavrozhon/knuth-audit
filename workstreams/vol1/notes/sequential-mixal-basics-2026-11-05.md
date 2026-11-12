# Souvislý průchod MIXALu: hlavní text a úlohy 1–9

Dne 5. listopadu 2026 přímo přečteny originály 145–158 a 511–512
(souborové strany 160–173, 526–527). Strana 144 byla přečtena v X0949.
Na 159 je již přečteno zadání dalšího bloku, ale jeho stránkové pokrytí
se uzavře až s příslušnými řešeními. Přijaty a porovnány obecné důkazy
v `mixal-basics.md`, `mixal-scope.md` a oprava vlastního sestavovače
v `mixal-end-label.md`. Starý úspěšný výpočet 52324 kontrol se neopakuje.

## Podstatná oprava našeho auditu: C0022 není chyba knihy

Na straně 512 je v komentáři vedle `J1NN BAD` jasně vytištěno
**C field ≥ 64?**. Spodní čárka je vidět již na celé stránce; pro
jednoznačný doklad byl původní DjVu list 527 znovu vykreslen v 600 dpi
a vytvořen detail zahrnující i sousední skutečně ostré nerovnosti.
Žádné doostřování, retuš ani generování obsahu se nepoužilo.

Doklad: `images/sequential-2026-11-05/vol1-p512-C0022-detail.png`.
Zdroj je nezměněný DjVu z inventáře; příkaz byl
`nice -n 15 ddjvu -format=ppm -page=527 -scale=600 ...`.
Rozměr renderu 4958 × 7000, výřez má relativní hranice
left=.74, top=.405, right=.90, bottom=.52, zaokrouhlené dolů.

Předchozí C0022 chybně přečetlo ≥ jako >. Stav je nyní **dismissed**;
program i komentář jsou v tomto bodě správně. Archivní text hlášení
se zachovává jako historie, není platným závěrem ani novou korespondencí.
Staré poznámky dostaly výslovné upozornění. Jde o opravu auditora,
nikoli o nově nalezené erratum. Strana 512 přesto obsahuje jinou,
již zveřejněnou chybu: skok plovoucí větve do GOOD místo MEMORY.

## Přijaté matematické a programové kontroly

- M vrací maximum a jeho nejpravější index. Při přísném zlepšení
  aktualizuje hodnotu i index; shoda zachová dosavadní výsledek.
  Samomodifikace závěrečného JMP zajišťuje návrat. Profil dává
  5+5n+3A jednotek u, včetně krajního n=1. Všechny vytištěné
  instrukční kódy a adresy souhlasí.
- Program P má platný test Q≤p po vyloučení nulového zbytku:
  N=pQ+R<p²+p<(p+1)². Další prvočíselný dělitel proto neexistuje.
  Dostatek dělitelů v tabulce zajišťuje Bertrandova věta; její zdejší
  použití je správné, není požadován nový důkaz samotné klasické věty.
- Smyčky tabulky a tisku, záporné indexování, deset sloupců po padesáti
  prvcích a oba buffery odpovídají invariantům. Každý OUT čeká na
  předchozí výstup téže tiskárny, takže se nezapisuje do používaného
  bufferu. Uložený výsledek potvrzuje 9538 dělení a 182144u pro výpočet
  bez tisku; byl přečten, nikoli nově spočítán. Tabulka končí 3571.
- Výrazy se vyhodnocují zleva; // násobí čitatele b⁵ před dělením.
  W-hodnoty zapisují postupně do určených polí. ORIG přidělí vlastnímu
  návěští starou adresu, END adresu až za doplněnými konstantami.
  Dopředný symbol není povolen ve výrazu; lokální dB/dF nikdy neodkazuje
  na vlastní řádek. Všechny vytištěné příklady těchto pravidel souhlasí.
- Úlohy 1–7: běhové přiřazení ENTX/STX, návrat, výběrové třídění,
  sestavení původního P, synchronizace tiskárny, dělitelé a kolize
  lokálních návěští mají správné odpovědi v uvedených předpokladech.
  Odkaz 5.2.3S je přijat z přesného dřívějšího obrazového dokladu.
- Úloha 8 se znovu řeší pouze vzorcem: po k blocích je k(k+3)/2 slov;
  poslední viditelné AAAAA je ve slově 2344, po něm 35 mezer na řádku 98,
  poslední dva řádky jsou prázdné. Neproběhla zakázaná simulace úlohy.
- Úloha 9: F=9q+r, 0≤r<9, je platné pole právě když q+r≤5;
  pak L=q, R=q+r. Adresové výjimky a nulová znaménka odpovídají zadání.
  Paměťový test plovoucí větve vyžaduje známou opravu 2002. Dvě úspory
  instrukcí z roku 2008 nemění výsledek. C0022 je zamítnuto výše.

První dotisk je konzistentní pro původní PRIME=−1. Změna na 99 je
potřeba pro sjednocení s později upřesněným zaváděním programu.
**C0021 je neúplné promítnutí errata 2022**, doplněného 2026:
negativní komentář 149, obrázek 152 a pět položek odpovědi 511
zůstávají staré. Konstanta −499 na 2051 je přitom nadále správná,
protože pochází z 1−L. Nález se nemá mapovat jako původní vada těchto
tří stran. UI má nyní kind=errata a pouze související lokace.

## Historie a errata

Přímo znovu přečteny tři uložené obrazy Knuthova CASE SOAP III (1958),
tištěné strany 1, 5 a 9. Poděkování Conwayovi je datováno 31. ledna
1958; abstrakt zmiňuje připravovaný UNISAP. Pravidla lokálních návěští
a jejich definic podporují technickou historii textu.

Přeskočené kontroly: samostatný manuál UNISAP a úplná historie prvenství;
nezávislý dobový doklad jugoslávského detergentu a autorovy vzpomínky
na rok 1971. Jde o bibliografické výjimky podle aktuálního zadání.
Příslib budoucí kapitoly PL/MIX je původní plán, následně z errat
odstraněný; neoznačuje se za matematickou chybu původního vydání.

Čtyři vrstvy errat jsou aktuální podle manifestu X0930. Celý místní
výtah MIXAL byl přečten, zobrazeny all1-prepre 13, 14 a 37 a all1-pre 11.
Aktuální opravy PRIME byly již přímo přečteny v obrazu all1, strana 7.
Na původní straně 145 je již správné „page 96“; pozdější erratum
„page 1“ se na tento sken nevztahuje. Obrácení zápisu ekvivalence
X[i] a paměti je konvence značení. Libovolné pořadí literálů je již
povoleno pravidlem 11(f), takže upřesnění příkladu není chybný výpočet.

Přesná červená mapa X0161 v tomto bloku: 148 (základ PRIME a loader),
154 a 155 (překlepy), 157 (chybějící ostrá dolní mez d>1),
512 (paměťový test FLOAT). Zbylé stylistické změny, doplněné příklady
a změny plánů se nevydávají za vady celých původních stránek.

Hlavní text §1.3.2 je uzavřen s uvedenými bibliografickými výjimkami.
Úlohy 1–9 zůstávají uzavřené. Další část sekce pokračuje od úlohy 10;
nevydáváme tyto kontroly za prověření všech odpovědí 513–522.
