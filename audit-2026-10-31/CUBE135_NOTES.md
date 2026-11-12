# Úloha DLX135: MacMahonovy čtverce na krychli

Kontrola 2. listopadu 2026. Zadání je na straně 139, odpověď na
450–451; strany PDF jsou o 20 vyšší. Pracujeme s druhým dotiskem 4B
z listopadu 2022. V tomto bloku zatím nevznikl nový nález.

## Co je přesně doložené

Knižní obrázek je platné řešení. Z původních vektorů PDF jsme přečetli
všech **96 barevných výsečí**, složili síť šesti stěn a zkontrolovali
všech **48 společných krátkých hran**. Všech 24 cyklických typů dílků
se vyskytuje právě jednou, každá z 12 velkých hran krychle je jednobarevná
a otočení o 120° cyklicky mění barvy. Tím je existence požadovaná
v zadání prokázaná bez statistiky a bez důvěry v řešič.

Počet **61** v odpovědi také souhlasí. Přesný význam:

| Co rozlišujeme | Počet |
|---|---:|
| Pevná tělesová úhlopříčka, pevný směr cyklu barev, označená krychle | 732 |
| Všechny čtyři úhlopříčky a oba směry cyklu | 5 856 |
| Třídy při otáčení krychle a přejmenování barev | 122 |
| Třídy navíc ztotožňující zrcadlový obraz | **61** |

Nejde o povolení libovolně převracet jednotlivé dílky. Při globálním
zrcadlení se chirální typy vymění s jejich protějšky, které úplná sada
obsahuje; každý takto získaný výsledek jsme znovu ověřili.

## Proč je výčet úplný

Středy 24 čtverců mají zdvojené souřadnice tvaru
`(±2, ±1, ±1)` a jejich permutace. Středy krátkých hran jednoznačně
identifikují 48 spojů. Na 12 velkých hranách spojíme dvojice krátkých
hran stejné barvy, takže zbývá 36 barevných proměnných.

Zvolme otočení `R(x,y,z)=(y,z,x)` a barvy `a→b→c→a`. Všech 36
proměnných se rozpadne na 12 trojic. V každé stačí určit jednu barvu;
ostatní dvě jsou vynucené. Doslovný výčet všech **3¹² = 531 441**
přiřazení ponechá přesně 732, která používají všech 24 různých typů.
Žádná heuristická hranice se nepoužívá.

Druhý algoritmus staví úlohu XCC z **osmi orbit pozic a osmi orbit
typů dílků**. Jeho 540 voleb, 16 primárních a 12 barevných sekundárních
položek zpracuje původní Knuthův DLX2. Úplná množina jeho 732 výsledků
se přesně rovná prvnímu výčtu. Je to jiný algoritmus i jiná úroveň
modelování; sdílenou geometrii dále kontroluje nezávislé skládání sítě
a párování trojrozměrných koncových bodů hran.

Každé otočení krychle řádu tři vede kolem některé tělesové úhlopříčky;
ty jsou navzájem geometricky ekvivalentní. Pokud by cyklus barev
doprovázela nepřímá symetrie řádu šest, její druhá mocnina opět dává
takové otočení. Vyčerpání jedné osy a barevného směru tedy stačí.

Působení všech **48 × 6 = 288** geometrických a barevných transformací
dává u každého řešení stabilizátor řádu tři. Každá úplná orbita má 96
prvků a protíná původní výčet ve 12 prvcích: `732/12=61`.
Orbita se rozpadá do dvou disjunktních rotačních orbit po 48 prvcích.
Program kontroluje množiny i stabilizátory, nikoli jen toto dělení.

## Obecná rozmístění a Monte Carlo

Tři jednobarevné dílky různých barev nemohou sousedit hranou.
Zbývá **1 104 neuspořádaných trojic pozic**, tedy **6 624** po přiřazení
tří různých barev. Vůči všem symetriím krychle a přejmenování barev
tvoří **27 tříd**. Čísla orbit jsou 20×48, 5×24, 1×16 a 1×8.

Pro všech 27 tříd je předem předepsán milion náhodných průchodů
obecným stromem hledání, s uloženými semeny a přímým výstupem.
V uzlu vybíráme pozici s nejmenší doménou a rovnoměrně jednu z jejích
možností. Úspěšný list přispěje součinem navštívených velikostí domén;
neúspěšný průchod nulou. Pravděpodobnost zvolení konkrétního listu
je převrácená hodnota tohoto součinu, takže střední hodnota příspěvku
je přesný počet listů. Deterministické MRV větvení a používání každého
typu právě jednou zajišťují, že se skládání nepočítá vícekrát.

Implementace prošla šesti přesnými kalibracemi s pevným zbytkem
knižního obrázku. Původní DLX2 nezávisle potvrzuje počty
**1, 1, 2, 6, 84, 65**. První nalezené úplné skládání z každé třídy
se samostatně validuje.

Knižní údaj přibližně 900 milionů je odhad. Ani náš Monte Carlo
výstup není přesný počet; empirická standardní chyba není
rigorózní interval spolehlivosti pro těžkoocasé rozdělení.
Pilot pro třídu 0 je úvodní částí jejího milionového běhu a
nesmí se připočítat jako další nezávislý vzorek.

**Všech 27 běhů už je dokončených a přijatých**, celkem 27 milionů
průchodů. Odhady leží mezi **795 167 455** a **1 056 424 443**;
empirické standardní chyby u těchto dvou krajních případů jsou
10 704 982 a 13 244 136. Čísla pro jednotlivé polohy tedy nejsou
stejná. Formulaci „přibližně 900 milionů“ zde vyhodnocujeme jako hrubý
řádový odhad, nikoli přesnou rovnost nebo předepsanou relativní chybu.
Samotnou tuto odchylku nezařazujeme mezi chyby knihy.

Všech 27 uložených svědků prošlo také nezávislou geometrií složené
sítě. Díky vyčerpání tříd je tím přesně dokázáno, že se dá dokončit
**každé rozmístění tří různobarevných jednobarevných dílků, které
nesdílejí hranu**. Odhad jejich počtu dokončení zůstává statistický.
Souhrn je v `results/cube135/accepted.json`, celá tabulka v `estimates.csv`
a konkrétní svědci v `mono-witnesses.json` ve stejné složce.

## Primární prameny a otevřené části

Šest úplných/krátkých/historických vrstev errat bylo prohledáno
podle čísel úloh, obou sad stránkování, jmen a tvrzení. Všech
28 odpovídajících kontextů patří jiným úlohám nebo nesouvisejícím
citacím. Oprava DLX135 nebyla nalezena; přilehlá oprava matic136
je zaznamenaná pro následující blok.

[Uriho původní report](https://www.uriland.it/tessere-di-mac-mahon-su-superfici-tridimensionali/)
obsahuje příslušné typy hlavolamů a přímé obrázky rozvinutých sítí.
Stažené originální fotografie byly prohlédnuté. Počet 30 kosočtverců
odpovídá autorově vratné rodině D5: `5·4·3·2/4`; 60 rovnoramenných
trojúhelníků jedné strany odpovídá rodině B5: `5·4·3`.

Samotný rok 2010 v hlavičce webu neověřuje ani nevyvrací rok vzniku
1993. Stránka oznamuje 39 problémů, ale v získaném textu je pouze
číslovaný seznam 1–38. Obrázek s úryvkem Knuthovy knihy není nezávislý
historický doklad. Proto z toho nevytváříme další nález.

[Indexovaný záznam katalogu University of Calgary](https://searcharchives.ucalgary.ca/harry-l-nelson)
uvádí Nelsonovu a Philpottovu korespondenci z let 1972–1978 se složkou
o pokrytí krychle MacMahonovými čtverci. Korespondence ani původní
Philpottův článek JRM7 (1974), 266–275 však nebyly získané. Rok 1970
a přesné zásluhy Nelsona, Finka a Risueña tak ještě nejsou nezávisle
uzavřené. U dvou malých doprovodných fotografií mnohostěnů nejsou
všechny hrany viditelné; úplná rekonstrukce jejich barvení zbývá.
Přímé otevření archivního katalogu vrátilo HTTP429; zachovaná metadata
pocházejí z výsledku vyhledávání a slouží jako vodítko k originálu.

**Celá úloha proto zůstává `partial`.** To neomezuje úplný důkaz
existence ani přesný výčet 61 tříd. Dokončení celé knihy zatím
netvrdíme.

## Evidence a pokračování

- `results/cube135/figure-checked.json`: původní obrázek a složení sítě.
- `cyclic-exhaustive.json`, `xcc-accepted.json`, `symmetry-checked.json`
  ve stejné složce: dva úplné výčty a všechny skupinové orbity.
- `results/cube135/sampling/`: uložené vstupy, semena, výstupy,
  výsledky, kalibrace a průběžná či dokončená fronta.
- `results/cube135/source-status.json`: zdrojové hashe, URL a mezery.
- `results/cube135/errata-check.json`: přesný rozsah kontroly errat.

Nespouštět znovu úspěšné výčty. Existující dlouhé výpočty131 běží
bez změny jejich modulů. Další sekvenční úloha je136.
