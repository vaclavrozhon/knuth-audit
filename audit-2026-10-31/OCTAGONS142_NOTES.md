# DLX 142: smíšené osmiúhelníkové dílky Doris

**Rozsah:** 4B, §7.2.2.1, úloha 142 na straně 141 a odpověď na straně
454. PDF 161/474; autorův draft Fascicle 5C, strany 77/158.
Celá úloha je **partial**. Nový doložený nález: **F136**.

## Hotové kontroly

Původní obrázky mají 72 dílků a 288 barevných sektorů. Všechny jsou
přímo dekódovány z PDF, stejně jako 72 žlutých značek určujících
orientaci. V každé sadě je všech 24 cyklických typů právě jednou;
všechny společné hrany souhlasí. Výsledky se přesně shodují s autorovým
draftem. Obrázek (i) má shodné obě dvojice protějších okrajů, (ii)
levý a pravý okraj, (iii) žádnou dvojici.

Model používá osm půlhran každé čtvercové buňky. Sektory V jsou
dolní levý, dolní pravý, horní pravý, horní levý; sektory E jsou
dolní, pravý, horní, levý. Případ (i) má levou polovinu V, (ii)
dolní polovinu V, (iii) severozápadní a jihovýchodní čtvrtinu V.
Přesný příklad položky v odpovědi souhlasí: knižní souřadnice se
čtou jako řádek/sloupec, naše jako vodorovná/svislá souřadnice.

Nezávislý přímý barevný CSP a původní i normalizovaný DLX2 prošly
**29 porovnáními celých množin** s prostým výčtem barev: jednotlivé
dílky, obě smíšené dvojice, všech 16 orientací mřížky 2 × 2,
tříbarevná šachovnice, pět úplných dvoubarevných sad a tři periodické
případy. Teprve poté byly zdroje zmrazeny a spuštěny velké výčty.

Dosud přijaté úplné dvojí výčty:

| Případ | Počet po přejmenování barev | Po zrcadlení/půlobratu | Kniha |
|---|---:|---:|---|
| (i), obě dvojice okrajů | 192 | 96 | souhlas |
| (i), levý/pravý okraj | 21 024 | 10 512 | souhlas |
| (ii), levý/pravý okraj | **111 960** | **55 980** | **F136: vytištěno 11 960** |
| (iii), horní/dolní okraj | 0 | 0 | souhlas |
| (iii), levý/pravý okraj | 0 | 0 | souhlas |

U všech řádků jsou porovnány celé množiny a každý model přímo ověřen.
Nejde jen o shodu počtu. Soubor `accepted/ii-lr.json` odlišuje
nesouhlas s knihou od úspěšné validace. Knižní chybná očekávaná hodnota
11960 zůstává beze změny ve zmrazeném popisu úloh.

Samostatný krátký [verifier F136](verify_f136.py) s 44kB certifikátem
dokazuje dolní mez 11962, která sama vyvrací knižních 11960.
Nepoužívá žádný modul auditu ani řešič. Přesnou hodnotu 111960 dokládají
oba výčty. Podrobnosti v [F136_OCTAGON_CYLINDERS.md](F136_OCTAGON_CYLINDERS.md).

## Symetrie a ostatní tvrzení

Každý ze tří vzorů má právě dvě obdélníkové symetrie: identitu a
zrcadlení shora/dolů u (i), zleva/doprava u (ii), půlobrat u (iii).
Netriviální symetrie nemá pevnou buňku. Kdyby zachovala řešení až na
permutaci barev π, po dvojím použití by platilo π² = id. Involuce tří
barev má pevnou barvu a. Jediný celo-a dílek by musel být v pevné buňce,
což nelze. Faktor 2 je proto volný u všech řešení i periodických podmnožin.

Tvrzení o kontaktu mimo čtvercovou mřížku má přesný lokální svědek:
středy tří pravidelných osmiúhelníků jsou (0,0), (2,0), (−√2,√2).
Vzájemné kontakty s prvním leží na x=1 a −x+y=√2, ostatní dva se
nepřekrývají. Různé typy V/aaaa, E/bbba a V/bacc mají na obou kontaktech
barvu a. Středy nepatří do žádné otočené ani škálované čtvercové mřížky:
podíl dvou nenulových komplexních posunů má iracionální složky, zatímco
podíl gaussovských celých čísel má složky racionální. Je to lokální
svědek tří dílků, nikoli úplný výčet sestav všech 24 dílků mimo mřížku.

Primární [Gottfriedův web](https://www.gottfriedville.net/puzzles/octagons/index.html)
a [historie vydavatele](https://www.gamepuzzles.com/moredge.htm) potvrzují
Zdravka Zivkovice, jméno Doris a vydání Kadon v roce 2008. Vydavatel
rozlišuje vznik v roce 2007 a premiéru v roce 2008; datum v knize není
tímto rozporem. Z jeho galerie bylo přímo ověřeno všech **483** uložených
svědků, včetně pozic jednobarevných dílků. Galerie rohů má jiné vzory než
knižní (iii), a počet ukázek není úplným počtem řešení. Galerie se nepoužívá
jako důkaz F136. Přímý archivní požadavek produktové stránky Kadon skončil
HTTP403; tělo chyby je tak označeno, nikoli vydáváno za původní stránku.

## Co zbývá

Hlavní dvojí výčty (i)/(ii)/(iii) a zbývající periodické případy se
přijímají pouze po skutečném terminálu. Nezávislý CSP již ukončil (iii)
s 239198 řešeními, (i) horní/dolní s 387840 a (ii) horní/dolní s nulou;
v tomto checkpointu se jejich celé množiny s druhým řešičem ještě
neporovnaly. U obrovských hlavních (i)/(ii) se ukládají jen vzorky;
ani po dokončení nebudeme tvrdit přímou rovnost celých uložených množin.

Knižní historické náklady 2607/10223/77 Gmems dosud přesně nereprodukovány.
Jsou citlivé na pořadí vstupu a volby algoritmu. Samotný rozdíl nákladů
není nový nález. Fronty 1157664/1157665 a starší 141/1147292 se
nespouštějí znovu. Stav výše je datovaný checkpoint; další přijaté
terminály budou uvedeny v navazujícím záznamu.

Důkazy: `results/octagons142/{figures,claims,sources}-checked.json`,
`small/checked.json`, `accepted/*.json`, `errata-check.json`, oba vstupy
a terminální logy. První předpoklad při dekódování cizí rohové galerie
zaměnil trojdílné rohové L za blok 2×2; kontrola jej odmítla. Původní
neúspěšný skript i log zůstaly archivované a oprava se netýkala modelů
knižních úloh ani již spuštěných výčtů. Žádné nové emailové návrhy.
