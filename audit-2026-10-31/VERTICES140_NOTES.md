# DLX140: Langfordovy trojúhelníky s barevnými vrcholy

Kontrola 2. listopadu 2026. Zadání je na stranách 140–141, odpověď
na 453–454; v našem PDF jde o strany 160–161 a 473–474.
Matematická část a všechny její obrázky jsou prověřené. Celá úloha
zůstává `partial` kvůli dvěma přesně vymezeným historickým mezerám níže.

Nové nálezy jsou [F134, otočená dlaždice](F134_VERTEX_TRIANGLE.md),
a [F135, název citované knihy](F135_BOOK_TITLE.md). Oba jsou drobné;
**všechny vytištěné počty řešení souhlasí**.

## Model a úplnost

Dlaždice odpovídají cyklickým trojicím čtyř barev. Burnside dává
`(4³ + 2·4)/3 = 24` typů. U všech řešení se používá každý typ právě
jednou. Všechny výskyty téhož geometrického vrcholu mají společnou barvu.

Původní Knuthův DLX2 používá 24 primárních položek pro pozice, dalších
24 pro typy dlaždic a jednu sekundární barvenou položku pro každý vrchol.
Každé z 24 pozic odpovídá všech 64 uspořádaných barevných trojic:
celkem 1536 možností. Nenastavovali jsme žádné symetrické kotvy.

Nezávislý C++ program přiřazuje barvy přímo vrcholům. Jakmile se dokončí
trojúhelník, označí jeho cyklický typ v bitové masce; opakování odmítne.
Barvy zavádí v pořadí prvního výskytu. Deterministický výběr dalšího
vrcholu závisí jen na již přiřazených barvách, velikostech možností a
incidenci, takže přejmenování dosud nepoužitých barev nemění výběr.

Pro všech 21 desek se shodují **celé množiny** řešení. Nativní výčet má
dohromady 7536 různých úplně pojmenovaných modelů, po přejmenování barev
314. Každá barevná třída obsahuje přesně 24 modelů: všechny čtyři barvy
se v každém řešení vyskytují, takže stabilizátor přejmenování je triviální.
Každý model byl znovu přímo ověřen podle rohů a typů dlaždic.

Zbývající geometrické symetrie jsou všechny izometrie trojúhelníkové
mřížky, které zachovávají danou desku. Kontrolujeme uzavřenost množiny
řešení, celé orbity i Burnsideův součet pevných bodů. Zrcadlení je
přípustné: zrcadlí celou sadu všech cyklických trojic opět na tutéž sadu.

## Počty

| Obrázek | Plně pojmenované modely | Po přejmenování barev | Po všech symetriích desky |
|---|---:|---:|---:|
| a1: rovnoběžník 6 × 2 | 240 | 10 | 5 |
| a2: rovnoběžník 4 × 3 | 120 | 5 | 3 |
| a3: trojúhelník se seříznutým rohem | 144 | 6 | 3 |
| b1 | 192 | 8 | 4 |
| b2 | 96 | 4 | 4 |
| b3 | 72 | 3 | 3 |
| b4 | 96 | 4 | 1 |
| b5 | 24 | 1 | 1 |
| b6 | 48 | 2 | 1 |
| b7 | 48 | 2 | 1 |
| b8 | 48 | 2 | 1 |
| c1 | 1008 | 42 | 7 |
| c2 | 216 | 9 | 9 |
| c3 | 1152 | 48 | 48 |
| c4 | 192 | 8 | 2 |
| c5: vlna | 960 | 40 | 23 |
| c6 | 1344 | 56 | 28 |
| c7: tyč | 1536 | 64 | 18 |

Tři další zdvojené hexiamondy mají nula řešení v obou úplných výčtech.
Všech 12 volných hexiamondů bylo vygenerováno růstem přes sousední
buňku, s počty `1,1,1,3,4,12`. Tím se žádný souvislý tvar neztratí:
má kostru, jejíž list lze odstranit a zachovat souvislost. Stejný
argument pro hexagonální sousednost dává počty `1,1,3,7` tetrahexů.

Zvětšení každého hexiamondu zdvojením délek dává 24 trojúhelníků.
Devět tvarů odpovídá přesně a1 a b1–b8. Zbývající tři jsou nemožné,
takže odpověď na otázku o ostatních jedenácti tvarech je **osm**.
Sedm c-obrázků představuje všechny tetrahexy, bez opakování.

Tři malé původní siluety z odpovědi (b) byly porovnány přímo s obrysy
všech 12 hexiamondů. Jejich obrys má zaoblení a drobné odsazení hran;
po prodloužení přímých částí je každý tvar jednoznačný v toleranci
0,5 bodu PDF. Největší odchylky jsou 0,0004, 0,359 a 0,208 bodu,
zatímco ostatní kandidáti se liší o více než 2 body. Tato tolerance
slouží pouze k identifikaci miniatur; důkazy nemožnosti jsou přesné
výčty nad celočíselnou mřížkou.

Vytištěný prostřední obrázek (a2) přechází půlobratem v sebe při
záměnách `a ↔ c` a `b ↔ d`. Je to jediná z pěti barevných tříd s touto
symetrií, proto `(5+1)/2 = 3`. Vlna c5 má šest barevných i geometrických
tříd s centrální symetrií. Tyč c7 má osm barevných tříd, které tvoří
**čtyři** geometrické třídy. Tím jsou ověřena i obě vedlejší tvrzení (c).

Úprava Algorithm C podle úlohy 122 s počáteční barvou `a` vrací přesně
stejné množiny 10, 5 a 6 tříd. Primární položky pojmenované barvami
dílků mají bezpečný práh `e`: větví se na nich až po zavedení všech
čtyř barev. Pozice na desce jsou stále přípustné. Tento odůvodněný
práh je součást konkrétního kódování; nevydáváme jej za vyřešení
obecné interpretační otázky C031.

## Originální kresby a chyba F134

Ze tří stran PDF bylo získáno všech **1296 rohů 432 dlaždic v 18 obrázcích**.
V každém obrázku se vyskytuje správných 24 typů. Sedmnáct obrázků je
zcela platných; v c3 nesouhlasí dvě společná místa. Jediná oprava
otočením jednoho dílku je popsána u F134. Opravený obrázek patří
do úplných množin obou řešičů.

Autorův draft má na straně 158 všechny rohy sedmi tetrahexů stejné
jako naše PDF. Porovnání přesně zahrnuje i dva chybné vrcholy c3.
Samostatný `verify_f134.py` nepotřebuje žádný solver ani datový soubor;
jeho přepis všech rohů byl porovnán s původní vektorovou kresbou.

## Historické zdroje a přesné mezery

[Původní US patent 3608906](sources/vertices140/us3608906.pdf), udělený
28. září 1971 Marcu Odierovi, popisuje shodné hodnoty ve stýkajících se
vrcholech a odkazuje přímo na jeho dřívější francouzský patent 1582023.
Prohlédnuty byly původní strany 1 a 5; datum, autor a souvislost s
hlavolamem odpovídají citaci.

[Původní pravidla Triokeru](sources/vertices140/trioker-rules.pdf), strany
2–3 PDF, mají výslovné pravidlo rovnosti společných vrcholů, vyobrazení
téže sady a jméno Trioker. Okraj uvádí copyright 1968 Odier. Na třetí
straně je také správně napsané `SURPRENANTS TRIANGLES`. Spolu s
[národním katalogem BnF](https://catalogue.bnf.fr/ark:/12148/cb346060085)
jde o přímý doklad překlepu F135. Jméno Multimatch IV a stejnou sadu
24 dílků potvrzuje [stránka výrobce Kadon](https://www.gamepuzzles.com/edgemtch.htm).
Webový nástroj ji přečetl; přímé stažení HTML vrátilo 403, proto
netvrdíme, že máme archiv nezměněného HTML.

Zůstávají dvě mezery:

- Langfordův článek **„2829. Dominoes numbered in the corners“**, Gazette
  43(344), květen 1959, strany 120–122, DOI 10.2307/3610194, je ověřený
  na stránce vydavatele. Plný text ani obrázkový náhled se nepodařilo
  získat: odkaz PDF přesměroval na HTML s přístupovými možnostmi,
  obrázek vrátil 403. Samotná metadata nepotvrzují konkrétní připsání
  tohoto trojúhelníkového hlavolamu. Odpověď uložená pod původně
  požadovaným jménem `langford1959.pdf` je výslovně označena jako HTML,
  nikoli jako získaný článek.
- Nemáme původní francouzský patent. Index rozlišuje přihlášení
  8. ledna 1968 a zveřejnění 26. září 1969; rok 1968 v knize může
  odkazovat na přihlášení. Není to nový nález. Obsahovou souvislost
  potvrzuje získaný původní americký patent.

## Errata a reprodukce

Čtyři čerstvé oficiální originály z 19:14 UTC jsou beze změny.
Prohledáno šest vrstev pro 4B a Fascicle 5, podle čísel stran,
úlohy i pojmů. Osm zásahů patří jiným úlohám: Langfordovým párováním
na straně 112, DLX121 na 138 a MPR140(e) na 396. Žádný neopravuje
zdejší obrázek či název knihy. Fyzický výtisk ani prvenství neověřeny.

Hlavní záznamy: [přijetí výsledků](results/vertices140/accepted.json),
[úplné počty](results/vertices140/counts-checked.json),
[všechny barevné modely](results/vertices140/color-normalized-models.json),
[siluety](results/vertices140/icons-checked.json),
[Algorithm C](results/vertices140/algorithm122-checked.json),
[historické podklady](results/vertices140/source-status.json),
[errata](results/vertices140/errata-check.json).

Oba úplné výčty i dodatečná kontrola Algorithm C skončily řádně.
Hotová hledání se neopakují. Další sekvenční úloha je 141.
