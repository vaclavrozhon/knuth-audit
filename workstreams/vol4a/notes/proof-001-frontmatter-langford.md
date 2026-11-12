# Individuální kontrola argumentů — začátek

6. listopadu2026, nový rozsah výslovně vyžádaný uživatelem. Starý první
průchod není úplná důkazová kontrola. Uzavřené konkrétní výsledky se přebírají.

## Předmluva a ukázkové úlohy

- Součty slov na str.v přebírám z `results/first-pass-sanity.json`; argument:
  n^k slov délkyk, součet přes1≤k≤n. Opravené znění známého errata je
  zohledněno. Notační příklady nax přebírám z první poznámky.
- Věta Stockmeyera–Meyera na str.viii je explicitní externí vstup; její
  konkrétní použití v §7.1.2/124 bude rozebráno u příslušného místa. Není
  součástí nynějšího uzavřeného důkazu ani důvod rekonstruovat celý obor.
- Ukázková úloha1 naxiii: M znamená matematicky zaměřeno a15 leží mezi
  jednoduchou10 a střední20. Odpověď514 „moderately easy ... mathematically
  inclined“ souhlasí přímo s definicemi. Zvláštní výpočet není potřebný.
- Ukázková úloha2: pedagogická otevřená otázka, odpověď514 je žert o odměně.
  Není to tvrzení s matematickým důkazem. Známý pozdější dodatek o obezřetnosti
  a současné podmínky odměn nejsou předmětem této matematické kontroly.
- Ukázková úloha3: odpověď514 nedává důkaz, pouze odkazy na Poincarého,
  Binga a Perelmana. Jako externí vstup se přijímá 3rozměrná Poincarého věta
  pro uzavřenou jednoduše souvislou varietu. Primární arXiv záznamy
  [0211159](https://arxiv.org/abs/math/0211159),
  [0303109](https://arxiv.org/abs/math/0303109),
  [0307245](https://arxiv.org/abs/math/0307245) byly6.11.2026 otevřeny:
  autor, předmět, roky2002/2003 a39/22/7 stran odpovídají opravené citaci.
  Ricciho tok, surgery a přechod mezi topologickou a hladkou kategorií se
  nezávisle nerekonstruují. To je přesná mez externího vstupu, ne nový nález.
  Známé úpravy citace514 z2019/2022 byly zohledněny.

## §7, str.1: L3=L4=1 až na obrácení

Pozice čísluji od1; dvě značkyk mají rozdíl pozic k+1.

**n=3.** Značky3 mohou být jen na(1,5) nebo(2,6); případy se zrcadlí.
Zvolme(2,6). Pro2 zbývá z možných(1,4),(2,5),(3,6) pouze(1,4).
Zbylé pozice(3,5) mají správný rozdíl2 pro1. Jediné řešení této orientace
je231213. Tím je existence i jednoznačnost do obrácení dokázána.

**n=4.** Značky4 leží na(1,6),(2,7) nebo(3,8). První a třetí případ
jsou zrcadlové.

1. Při4 na(1,6) může3 ležet na(3,7) nebo(4,8).
   V prvním podřípadu zbydou2,4,5,8. Dvojka na(2,5) ponechá pro1
   nesprávné(4,8); dvojka na(5,8) ponechá správné(2,4). Dostaneme41312432.
   V druhém podřípadu zbydou2,3,5,7: jediná možnost2 je(2,5), která ponechá
   nesprávné(3,7). Jiná řešení nejsou.
2. Při4 na(2,7) jsou možnosti3 na(1,5) a(4,8) zrcadlové. Pro(1,5)
   zbydou3,4,6,8. Jediná dvojka(3,6) ponechá1 na(4,8), což nevyhovuje.

Tedy existuje právě41312432 a jeho obrácení23421314. Jde o krátký rozbor
všech vynucených případů, nikoli výpočetní enumeraci. Původní str.1 byla
znovu otevřena kvůli přesné formulaci; důkaz dosud uložen nebyl.

## Převzaté výsledky a další závazky

Nutnost n≡0 nebo3(mod4) na str.2 je již dokázána v první poznámce;
neopakuji ji. Svědci na str.3 a šířka7 jsou rovněž uzavřeny dřívějšími
výsledky a cílenou odpovědí515. Jejich optimalita5268/počet12016 však ne.

Nejbližší nová povinnost je **str.2/file19 a §7–1/odpověď514: Daviesova
obecná konstrukce pro n=4m−1 a4m**. Tabulka L7 ažL24 zatím zůstává
partial: velká enumerace se nespouští. Následují oddělené závazky pro
heuristický odhad, polynomial counting a asymptotické srovnání.

Odpověď514 byla přečtena celá jako stránka, ale argumenty §7–1 až5 na ní
ještě nejsou všechny prověřeny. Celostránkové reading coverage se výslovně
neslučuje s důkazovými závazky; důkazový stav této stránky zůstává partial.

Zdroje: `images/file014.png`, `images/file018-detail.png`,
`images/file531.png`, `sources/file531-ocr.txt`, `sources/file531.pdf`.
