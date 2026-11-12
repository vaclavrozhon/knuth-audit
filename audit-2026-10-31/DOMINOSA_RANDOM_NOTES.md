# Dominosa: úlohy 7.2.2.1–72 až 74

Kontrola 1.–2. listopadu 2026, po checkpointu `1e8340f`.
Původní stránky 4B 131–132 a 431–432 byly zobrazeny. Srovnány také
autorovy stránky pre-fascicle5c 67, 135 a 136. Matematické výsledky níže
jsou odděleny od historických experimentů, pro které nemáme původní data.
Žádný nový potvrzený nález F v tomto bloku; C024 je kandidát na upřesnění.

## 72: přesné prostory náhodných voleb

Označme S(A) počet úplných řešení matice A. Množina všech matic obsahujících
osm výskytů každé číslice 0,…,6 má velikost

`M = 56!/(8!)^7 = 4104167472585675600759440022842715359250000`.

Geometrických rozkladů obdélníku 7×8 na domina je **1 292 697**. To bylo
ověřeno třemi samostatnými postupy: úplným souřadnicovým výčtem v C++,
řádkovou přenosovou rekurencí v obou orientacích obdélníku a původním DLX1.
Všech 1 292 697 modelů je uloženo v `tilings.u8.gz`; každá ze 56 buněk je
v každém modelu pokryta právě jednou a žádné dva modely nejsou stejné.

Každý takový rozklad lze obsadit 28 různými kameny `28!` způsoby. Dvacet
jedna nedvojitých kamenů má dvě orientace, sedm dvojitých jen jednu.
Počet úplných rozmístění tedy je

`N = 1292697 · 28! · 2^21 = 826546844419025634231504530388811776000000`.

Jde o dvojice (A,T), kde T je řešení A, takže `Σ_A S(A) = N`. Proto má
rovnoměrný model (i) přesně `E S = N/M = 0.20139208498192473…`, jak tvrdí
kniha. Hodnoty `4.10×10^42` a `8.27×10^41` jsou správně zaokrouhlené.

### C024: rovnoměrné matice versus rovnoměrná rozmístění

Zadání modelu (ii) říká, že každá matice získaná náhodným zamícháním domin
je stejně pravděpodobná. Je-li tím myšlena **různá výsledná matice číslic**,
neodpovídá to generátoru v odpovědi. Rovnoměrná volba geometrického rozkladu,
permutace kamenů a orientací dává `Pr(A) = S(A)/N`.

Přesný svědek už je v úloze 70: první matice má právě dvě řešení, druhá
právě jedno. Oba úplné výčty byly nezávisle ověřeny v předchozím bloku.
Generátor odpovědi 72 proto dává těmto dvěma maticím pravděpodobnosti
`2/N` a `1/N`. Rovnoměrná volba různých řešitelných matic by jim dávala
stejnou pravděpodobnost `1/K`, kde K je počet takových matic.

Doslovný rovnoměrný výběr řešitelných matic se rovná modelu (i)
podmíněnému existencí řešení. Naproti tomu zamýšlený model rozmístění
zvýhodňuje matice s více řešeními. Obecně platí

`Pr_ii(S=1) = Pr_i(S=1)/(N/M)`.

**Zatím candidate:** matematický rozdíl je dokázán, sporný je význam slova
„matrix“ v této větě. Může být použito jako zkratka pro rozmístění, ve kterém
jsou ještě viditelné hranice kamenů. Odpověď zamýšlený model dostatečně
objasňuje. Možné upřesnění zadání: rovnoměrně volit úplné rozmístění všech
28 kamenů do rámce a teprve potom zapomenout hranice domin. Nejde o chybu
vzorce N/M ani o nově prokázanou chybu historických vzorků.

Stejné znění je v PDF i autorově PS. Všech šest relevantních textů errat
bylo prohledáno podle čísel, slov a posunů stran; čtyři vzdálené originály
se hashově shodují s archivem. Odpovídající oprava formulace nebyla nalezena.

### Nový reprodukovatelný experiment

`check_dominosa_random.py` používá seed `202611020072`. V modelu (i) míchá
multiset číslic, v modelu odpovědi (ii) vybírá rovnoměrně jeden z uložených
geometrických rozkladů a nezávisle permutaci a orientace kamenů.
Všech **20 000** vstupů je uloženo. Každý počet řešení byl úplně a nezávisle
spočten souřadnicovým C++ DFS i nezměněným autorovým DLX1; všechny souhlasí.

| Údaj | Nový model (i) | Nový model (ii) |
|---|---:|---:|
| Vzorků | 10 000 | 10 000 |
| Alespoň jedno řešení | 204 | 10 000 |
| Právě jedno řešení | 22 | 98 |
| Nejvíce řešení | 704 | 3 168 |
| Součet počtů řešení | 2 372 | 525 996 |
| Součet čtverců | 556 988 | 159 845 124 |
| Průměr | 0.2372 | 52.5996 |
| Výběrová směrodatná odchylka | 7.45977 | 114.97442 |
| Odhad pravděpodobnosti jednoznačnosti | 0.22 % | 0.98 % |
| Wilsonův 95% interval | 0.145–0.333 % | 0.805–1.193 % |

Odchylky mezi vzorky nejsou chybou knihy; rozdělení má těžký ocas.
Z historických součtů knihy vycházejí průměry 0.2256 a 50.8506 a
výběrové směrodatné odchylky 3.08899 a 108.75383. Jejich uvedená
zaokrouhlení 3.1, 51 a 109 jsou správně.

Nové celkové počty memů včetně inicializace jsou 240 757 328 a 627 507 688.
Nejsou reprodukcí historických 250M a 650M: jiné vzorky, neurčené pořadí
a případné konvence počítání. Původní seed, vstupy a maxima 2652/četnosti
216,26,106 nejsou nezávisle reprodukovány. **X072 proto zůstává partial.**
Známé erratum E034 (1292687 → 1292697, 4.7.2020) už naše 4B obsahuje.

## 73: úplné přepočty rekordů a jejich aktualizace

Pro každé zadání byly porovnány tři úplné počty:

1. souřadnicový C++ DFS se zákazem opakování typu kamene;
2. nezávislý průchod všemi geometrickými rozklady a test jejich 28 typů;
3. nezměněný autorův DLX1.

První dvě metody navíc nezávisle spočítaly četnost každé z 97 hran.
Úplné množiny řešení jsou archivovány jako posloupnosti 28 indexů hran,
komprimované gzip. Při kontrole každého modelu jsou obsazené buňky a typy
kamenů jednoznačně určeny.

| Zadání | Řešení | Nejméně výskytů použitelné hrany | Nepoužitelné hrany |
|---|---:|---:|---:|
| Keller, příklad z knihy | 730 924 | 31 370 | 1 |
| Sermuliņš, zveřejněno 2005 | 793 648 | 33 410 | 0 |
| González-Morris, oprava 2023 | 807 752 | 35 082 | 0 |

U Kellerovy matice je jediná nepoužitelná hrana vodorovné `21` v úseku
`521` na třetím řádku, tedy buňky 17 a 18 při číslování od nuly.
Obě přesná tvrzení původní odpovědi o četnostech jsou správně.

**E036 je již známá aktualizace:** oficiální erratum z **10.8.2023**
nahrazuje celou odpověď 73 novým zadáním a údaji 807752/35082.
Oba údaje jsme úplně ověřili. PDF errat str.11 bylo zobrazeno; nejde
o nový nález. Náš druhý dotisk tuto náhradu ještě neobsahuje.

Současný [Kellerův přehled](https://www.solitairelaboratory.com/puzzlelaboratory/DominoGG.html)
uvádí obě matice. Jeho oba obrázky byly staženy a zobrazeny; číslice
odpovídají ověřeným vstupům. HTML se podařilo přečíst webovým nástrojem,
přímý archivní požadavek vrací HTTP406. Chyba stažení je v manifestu.

Ještě starší zlepšení dokládá [web lotyšské soutěže](https://www.lio.lv/neatdz/domlab.htm)
s datem 16.11.2005 a původní článek M. Opmanise, *Olympiads in Informatics*
3 (2009), 80–100, str.96/Fig.8, dostupný v
[původním svazku](https://ioi.te.lv/oi/files/volume3.pdf). Matice v článku
byla zobrazena a všech 56 číslic porovnáno. Původních 730924 tedy bylo
překonáno už před vydáním 4B; nepočítáme to podruhé jako nový nález,
protože oficiální náhrada stejný zastaralý rekord už odstraňuje.

Globální maximum není těmito výpočty stanoveno. Máme doloženou dolní mez
807752 a triviální horní mez 1292697. Úloha 73 je správně výzkumná,
nikoli tvrzení, že vytištěná konstrukce je optimální. V ověřených aktuálních
primárních zdrojích nebyla nalezena novější hodnota. Rok Kellerova objevu
2004 máme z knihy a autorova PS, ale nezávislý datovaný pramen k němu
zatím chybí; **X073 je matematicky a stavově ověřen, bibliograficky partial.**

## 74: obecný důkaz MCC konstrukce

Fixujme geometrické párování T. Pro jeho 28 hran vytvoříme primární položky
P; pro ostatních 69 sousedních dvojic položky Q. Primárních 28 položek xy
vynutí použití každého typu kamene právě jednou na hranách T. Sekundární
barevné položky t_u zaručí, že všechny možnosti zvolené kolem téže buňky
souhlasí v její číslici. Barevné možnosti jsou přesně ty v knize; pro x=y
musí být duplicitní orientace odstraněna.

Možnost s Q pro dvojici xy navíc obsahuje D_xy. Označme k_xy počet výskytů
tohoto typu mimo T a b_xy indikátor zvolení pomocné možnosti `# D_xy`.
Násobnost 3 u D_xy dává `k_xy + b_xy = 3`, kde b_xy je 0 nebo 1.
Po přidání jednoho skutečného kamene na T má tedy typ xy celkovou četnost
3 nebo 4. Položka # násobnosti 15 zajistí právě patnáct trojic a třináct
čtveřic. Totéž nutně plyne z `15·3 + 13·4 = 97`.

Obráceně každá taková matice řešitelná pomocí T určuje jednu možnost pro
každou hranu a pomocnou možnost právě pro typy s celkovou četností 3.
Tím se splní všechny primární násobnosti i barevná konzistence.
To dokazuje obě implikace a jednoznačnost rozšíření matice do MCC řešení.
**MCC samo nevynucuje jedinost řešení Dominosa**; ta se testuje až následně,
jak vyžaduje postup v odpovědi.

Výsledný úplný vstup má 154 primárních položek, 56 barevných sekundárních
a `97·49 + 28 = 4781` možností. Uložen je jako `74-full.mcc`.
Jediné řešení tištěného zadání bylo potvrzeno všemi třemi metodami výše.
Každý typ se v jeho zadání vyskytuje třikrát nebo čtyřikrát, v poměru 15:13.
DLX1 s typy kamenů před buňkami navštívil **přesně 572 uzlů**, jak uvádí
kniha. Jiné pořadí položek (buňky první) dává 547; nepovažujeme to za chybu.

Jedinečné řešení zároveň tvoří tatami párování: u žádného vnitřního vrcholu
se nesetkají čtyři různé kameny. Odkaz na 4A, 7.1.4–215, str.274, byl
ověřen v původním DjVu (souborová str.291; OCR pořadí je o dvě strany jiné).

Tištěná matice poskytuje konkrétní MCC svědek se 112 vybranými možnostmi,
z toho 15 pomocnými. Ověřeny všechny násobnosti, všech 56 barev a všechny
číslice. Po zafixování těchto barev nezměněný DLX3 našel právě tento model.

Dodatečné generování z úplného vstupu s novým seedem nepředstavuje
reprodukci autorových vzorků. První pokus skončil návratovým kódem143 bez
uchovaného výsledku; stav procesu byl ověřen jako ukončený. Následující
výslovně omezený pokus skončil na 500 001 229 memech bez nalezené matice.
Je uložen jako **limit**, nikoli UNSAT. Přesný obecný důkaz a zkontrolovaný
kladný svědek na tomto pokusu nezávisejí.

Keller na svém webu datuje položení problému do WGR7 (říjen1987,8–9) a svůj
jednoznačný příklad do 12.9.1996, později WGR12 (únor1998,9). Původní čísla
časopisu dosud nemáme. E037 (18.12.2021) opravuje adresu webového odkazu;
v naší 4B je zapracováno. Historických 10000 kandidátů, 2731 jednoznačných,
extrémní pořadí tvrdosti a průměr přibližně70M memů nemáme reprodukovány.
**X074 zůstává partial; konstrukce i konkrétní vytištěný příklad jsou ověřeny.**

## Reprodukce a další práce

Soubory jsou v `results/dominosa72/`, zdroje v `sources/dominosa72/`.
Samostatné skripty ověřují rekordy, nové náhodné vzorky, přesné rozlišení
pravděpodobnostních prostorů, MCC konstrukci, errata a původní dokumenty.
`random-checked.jsonl.gz` obsahuje vstup, oba úplné počty a profil DLX1
každého vzorku. Binárky byly sestaveny izolovaně; manifesty uchovávají
příkazy a hashe. Úspěšné výčty není třeba opakovat bez změny vstupů.

Další bezprostřední blok jsou úlohy 75–76 o semisymetrických kvazigrupách,
případně hlavní text od Polycubes na str.82. Historické mezery výše
zůstávají výslovně v evidenci; hotové matematické kontroly se neztrácejí.
