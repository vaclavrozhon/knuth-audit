# DLX 131: skládání s doplňkovými hranami — rozpracováno

Původní strany 139, 449 a 450 byly zobrazeny 2. listopadu 2026.
Úloha má dvě části, jigsaw/Trifolia a triple-three triminoes.
Její audit zatím **není dokončený**. Aktuální běhy, přijaté počty
a případná přerušení uvádí `results/mating131/queue.json`.

V části (a) se párují hrany `a↔a, b↔b, c↔d`. V části (b)
`a↔b, c↔d`; c a d představují 0 a 3 tečky, a a b představují 1 a 2.
Každá vnitřní hrana sousedí s jedním nečárkovaným a jedním
čárkovaným trojúhelníkem. Pokud možnosti čárkovaných buněk uvádějí
místo skutečné barvy její protějšek, běžná shoda barev v Algorithm C
je přesně podmínka těchto doplňkových hran. Cyklus tří skutečných
barev před touto záměnou určuje původní typ dílku.

`mating131.py` sestavuje takový model a obsahuje obě doslovně
vytištěné možnosti `01' abc`. U (a) používá knižní kotvu
aaa na 02; důkaz této normalizace je nyní uveden níže.
U (b) nastavuje kódované obvodové hrany `/` a `\` na a, `-` na b.
Samostatný validátor vzorků spojuje skutečné koncové vrcholy hran,
ověřuje doplňkovost fyzických barev a použití všech 24 typů.

Naplánovaný nativní průchod: (a) s kotvou a bez záměny c/d,
potom s potlačením c/d; (b) pevné případy půlobratu a hornodolního
zrcadlení, nakonec úplný počet bez odstranění symetrií. Poslední
počet 3 419 736 176 může běžet dlouho. Každý případ má zaznamenaný
PID, příkaz, limit 48 hodin a log; neúplný výstup není přijatý počet.

Předběžná kontrola pomocné položky půlobratu odhalila chybu pouze
v našem assertu: deterministický generátor zvolil název `#/20`,
kniha `#/23`. Oba označují stejnou rovnici mezi `/20` a `/23`.
Matematická omezení ani první dva běhy se tím nemění. Původní
zdroje jsou uložené jako `initial-mating131.py` a
`initial-run_mating131.py`; zdroje načtené živým procesem neměníme.
Po dosažení této kontroly má být navázáno výslovnou opravenou
frontou a již dokončené terminály pouze převzaty, nikoli přepočítány.

První wrapper 1013539 poté skutečně skončil právě v této přípravné
kontrole, až po obou dokončených bězích (a). Jeho nepřítomnost byla
ověřena přímo procesním seznamem a uložena v `setup-interruption.json`.
Assert byl opraven na náš ekvivalentní název, všechny čtyři varianty
modelu prošly přípravou. Výslovné pokračování 1015840 pod
`--resume-after-label-fix` oba hotové výpočty přeskočilo. Nejde o
restart kvůli pozorovacímu timeoutu ani o opakování úspěšného hledání.

Přijaté terminály první části:

| Model | Řešení | Validované vzorky | Čisté hledací mems |
|---|---:|---:|---:|
| aaa na 02, bez záměny c/d | 4 463 448 | 4 463 | 44 692 654 181 |
| aaa na 02, s potlačením c/d | 2 231 724 | 2 231 | 23 195 290 015 |

Knižní počet 2 231 724 souhlasí. Dva nativní běhy nejsou dva
nezávislé algoritmy. Hrubý náklad druhého běhu je 26 572 053 023
memů, po odečtení unmems 23 195 290 015; otázku přesné konvence
a zaokrouhlení knižních 30 Gμ zatím nepovažujeme za uzavřenou.
Původní zdroje validace a jejich hashe zůstávají u přijatých záznamů.

Případ půlobratu v (b) je nyní potvrzen dvěma odlišnými algoritmy:
**18 656 řešení**, a dokonce celé shodné množiny všech modelů.
Nativní model přidává 15 primárních selektorů a 60 možností.
Nezávislý bitsetový řešič místo selektorů přímo identifikuje dvojice
barevných hran a ponechá 49 primárních položek. To je ekvivalentní:
pro každou shodnou dvojici existuje právě jedna volba jejího selektoru.
Validátor přitom obnovuje skutečné doplňkové barvy na čárkovaných
trojúhelnících. Terminály, kontrolní součty a úplná shoda množin jsou
v `first-accepted.json`.

Další přijatý snapshot `followup-accepted.json` doplňuje nezávislý
počet **4 463 448** pro (a) s kotvou. Hornodolní případ (b) dává
**169 368** u obou algoritmů; celé množiny všech 42hranových vektorů
se shodují, nejsou to jen souhlasné čítače. Nativní náklad tohoto
případu je 1 699 395 937 čistých memů. Původní `first-accepted.json`
zůstává beze změny jako dřívější datovaný bod ověření.

## Proč normalizace a symetrie platí

V inventáři mají počty hran a rozdělení 11, 9, 3, 1 dílků s 0, 1, 2,
3 výskyty. Celkem je jich 18; na obvodu je 12, takže uvnitř jsou právě
tři bílé hrany. Pokud by aaa ležel uvnitř, všechny tři by s ním
sousedily. Každý ze tří dílků s dvojicí a by proto musel být jeho
sousedem a současně mít druhou bílou hranu na obvodu. Žádná vnitřní
buňka ale nemá tři sousedy na obvodu. aaa tedy leží na obvodu.
Dvanáct obvodových buněk tvoří jedinou volnou orbitu D6, a proto je
kotva 02 jednoznačným zástupcem geometrických symetrií.

Záměna c/d je další volná involuce: oba symboly jsou v každém
řešení použity. Celá skupina D6 × C2 tedy působí volně a každá třída
má 24 uspořádání. Po kotvě zbývá dělit dvěma, což dává 2 231 724.
Odraz je třeba interpretovat přesně jako v odpovědi: obrácení
orientovaného průběhu hrany změní vlnu na antivlnu; přechod na
protikus obnoví vlnu a vymění hrby a prohlubně. Množina všech
cyklických typů je uzavřená. Netvrdíme, že lze každý fyzický dílek
nezávisle převracet a stále používat tutéž čtyřprvkovou abecedu hran.
Samostatný `check_mating131_profiles.py` navíc ověřuje všechny řídicí
body v jednotně orientované soustavě: každý ze čtyř profilů se vyskytuje
18krát a uvedené vztahy odrazu/protikusu platí do zaokrouhlení PDF
(největší odchylka menší než 0,0001 délky hrany).

V části (b) působí na kódovaných hranách čtyři geometrické akce
identita, půlobrat, levopravý a hornodolní odraz, každá s volitelnou
záměnou c/d. Při změně orientace trojúhelníku je fyzická záměna
barev `a↔b, c↔d`; volitelná záměna c/d dává stejné generátory,
které uvádí kniha. Tabulka počtů pevných typů a buněk je:

| Geometrie | Záměna c/d | Pevné typy dílků | Pevné buňky |
|---|---|---:|---:|
| identita | ne | 24 | 24 |
| identita | ano | 4 | 24 |
| půlobrat | ne | 0 | 0 |
| půlobrat | ano | 4 | 0 |
| levopravý odraz | ne | 16 | 4 |
| levopravý odraz | ano | 8 | 4 |
| hornodolní odraz | ne | 0 | 0 |
| hornodolní odraz | ano | 8 | 0 |

Každý pevný typ se používá právě jednou, takže musí obsadit pevnou
buňku. Čtyři neidentické řádky jsou tak vyloučené nerovností počtů;
samotná záměna c/d nemůže zachovat ohodnocení všech hran. Zůstávají
pouze půlobrat a hornodolní odraz bez kódované záměny. Nemohou
současně fixovat řešení, protože jejich součin je vyloučený
levopravý odraz. Všechna symetrická řešení tedy mají orbitu velikosti
4. Přímá kontrola všech 18 656 + 169 368 modelů dává 4 664 + 42 342
disjunktních orbit; potvrzuje také přesné stabilizátory.

Burnsideův vzorec je `(N + 18 656 + 169 368)/8`. Dosazením knižního
N dostaneme 427 490 525. **Úplné N zatím není ověřené**; jde o
obecný důkaz vzorce a obou neidentických příspěvků, nikoli o přijetí
celého výsledného počtu. Certifikát je `symmetry-proofs.json`.

## Originální obrázky, prameny a errata

`extract_mating131.py` čte vektorový originál, ne OCR. U skládanky
ověřil všech 72 výskytů stran: 18 rovných, 18 vln a 36 hrbů nebo
prohlubní. Třicet vnitřních dvojic souhlasí i ve všech Bézierových
řídicích bodech. Všech 24 cyklických typů je právě jednou, okraj je a.
U druhého obrázku přiřadil všech **108 teček** k 72 výsečím; sousední
počty dávají tři, okraj odpovídá předepsanému vzoru a je použit každý
typ. Obrázek má právě zobrazený půlobrat. Úplné souřadnice, barvy,
typy a hashe jsou v `original-figures-checked.json`.

MacMahon, *New Mathematical Pastimes* (1921), str. 6–7, oddíly 3–4,
obsahuje přesně oba kontaktní systémy. Str. 54 a 56 vysvětlují převod
na doplňkové tvary hran; zobrazená konkrétní starší varianta má jeden
degenerovaný dílek, není to doslova moderní zakřivený obrázek. Titulní
strana a příslušné originály byly zobrazené. [Primární scan](https://archive.org/download/newmathematicalp00macmuoft/newmathematicalp00macmuoft.pdf)
je už archivován u úloh 124–126, nové rendery u `sources/mating131/`.

[Výrobce Kadon](https://gamepuzzles.com/edgmtch4.htm) potvrzuje název
Trifolia a čtyři uvedené tvary hran. [Historické poznámky výrobce](https://gamepuzzles.com/1990notes.htm)
uvádějí jiný externí počet 2 320 810 pro prodávaný dvoubarevný set.
Přesné podmínky převracení a ekvivalence původního výpočtu nemáme;
rozdíl 89 086 proto **není novým nálezem v knize**. Oba naše
algoritmy potvrzují knižní model. Odkaz na Gottfriedův TriMatch vede
k jinému hlavolamu s barvami vrcholů; stránka Trifolia Designs má
příklady, ale původní výčet nedokládá. Primární HTML a hashe jsou
uložené, omezení srovnání výslovně zaznamenává `history-checked.json`.

Šest vrstev errat 4B a historického Fascicle 5 bylo prohledáno podle
všech názvů, počtů a posunutých stran. Jediné tři zásahy jsou stejná
oprava **odpovědi 133**, nikoli 131, z 16. ledna 2023. Lokální hashe
souhlasí s kontrolou oficiálních souborů proti webu z 2. listopadu
08:06 UTC; viz `errata-check.json` a uložené kontexty.

## Co zbývá

Nativní wrapper 1015840 i nezávislý 1016888 nyní počítají úplné (b);
jejich živost byla ověřena skutečným procesním seznamem. Neúplné
výstupy nejsou přijaté a necommitují se. Zdroje živých front a jejich
sdílené závislosti jsou zmrazené. Zbývá úplný počet, návazné finální
dosazení Burnsideova součtu a přesná reprodukce či zdůvodnění konvence
historických nákladů 30 Gμ a 20,6 Tμ. Úloha proto zůstává `partial`.
