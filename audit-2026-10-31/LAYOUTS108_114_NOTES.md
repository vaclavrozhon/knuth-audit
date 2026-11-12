# DLX108–114: slovní obrazce, kostky a automorfismy sudoku

Průchod 2. listopadu 2026. Rozsah: zadání na tištěných stranách136–137,
odpovědi440–444, autorův předfascikl5c na stranách144–148 a všechny šest
relevantních lokálních vrstev errat4B/4F5. Nové důkazy a terminální výsledky
jsou v `results/layouts108_114/`, primární prameny v `sources/layouts108_114/`.
Zobrazeny původní stránky PDF i příslušné autorovy PS stránky. Tiskový
exemplář nadále neověřen. Potvrzení neznamená prvenství či nárok na odměnu.

## Dva nové nálezy v odpovědi109

**F129, str.442, odstavec o souvislém větvení:** po umístění ZERO z možnosti
(*) jsou uvedeny H00,H20,V30. Předchozí strana definuje souřadnice od1,
takže žádná z těchto tří položek vůbec neexistuje. Správně H11,H31,V41.
Z je v11, E v21, R v31, O v41 a51 je prázdné. H11 nemůže pokračovat
slovem začínajícím Z, protože ZERO je již použito. H31 nemůže pokračovat
slovem začínajícím R, takové v seznamu není. V41 vede do prázdné buňky51.
`check_layout_details.py` vyřadí možnosti nekompatibilní s(*) a pro každou
opravenou hranu najde právě jednu zbývající pomocnou možnost. Stejné chybné
indexy jsou v autorově PS str.146. Jde o lokální záměnu nulového a
jedničkového číslování, nikoli o neplatnost obecného převodu.

**F130, str.442, první odstavec:** tvrzení, že nejmenší obdélník pro(i),(ii)
má rozměry5×11, je při minimalizaci plochy a doslovných podmínkách nepravdivé.
Jednořádkový svědek je

```
ZERO.ONE.TWO.THREE.FOUR.FIVE.SIX.SEVEN.EIGHT.NINE.TEN
```

Obsahuje43 písmen a10 oddělujících prázdných buněk: plocha53<55. Všechna
slova jdou doprava; každý pár sousedních písmen patří předepsanému slovu.
Žádná slova se nepřekrývají, tedy platí také(iv). Souvislost(iii) zde
výslovně požadována není; tento odstavec ji vypustil. Mřížka má11 komponent.
Původní DLX2 potvrzuje pevně umístěný svědek a samostatný geometrický
validátor kontroluje všechna slova a sousednosti. Text neurčuje dolní mez
obou rozměrů. Výsledek vyvrací tvrzené minimum55; **netvrdíme, že skutečné
minimum je53**. Souvislé příklady8×8 a7×9 tím nejsou zpochybněny. Stejná
věta je v autorově PS str.146. Případný zamýšlený dodatečný zákaz
jednořádkových obdélníků by bylo nutné do formulace doplnit.

`check_layout_errata.py` zaznamenal71 kontextů v šesti vrstvách. Čtyři
aktuální originály z autorova webu byly shodné s archivem. Pro obě místa
nebyla nalezena oprava; hledalo se i podle obsahu a posunutých fasciklových
stran, nikoli jen442. Náklady23G jsou jiná, již zveřejněná aktualizace.

##108: prezidentské word-search

Oficiální archiv Bílého domu obsahuje očíslované prezidenty1–44. Po
sjednocení příjmení a zápisu VANBUREN dává přesně38 jmen ze zadání,
včetně opakovaného Clevelandova čísla. `check_layout_history.py` porovnává
celou množinu. Nejde o seznam současných prezidentů; pořadí je omezeno44.

Z původního PDF byly získány všechny buňky obou řešení15×15 a5×43 a76
vyznačených obrysů. Každý obrys odpovídá právě jednomu předepsanému slovu,
v každém obrázku jsou všechna jména právě jednou a jejich graf překryvů je
souvislý. Kontroluje se všech osm povolených směrů. To dokládá uvedené
horní meze225 a215 buněk, nikoli jejich optimalitu. Kniha výslovně uvádí,
že důkaz minimality nemá; náš registr nesmí svědek zaměnit za důkaz.

Word Ways1994: získány primární stránky článků Ecklera a Gordona s
abstrakty; přímé PDF stránky63,147,252 nebyly dostupné. Není tedy uzavřeno
porovnání Gordonových původních mřížek ani poznámka, že do jeho obrázku
dodatečně zapadne OBAMA. Omezená aktuální rešerše nenašla primární důkaz
lepšího optima; neprohlašujeme tím úplnost rešerše. X108 zůstává partial.

##109: obecný převod a úplné modely

Položka#k vynutí právě jednu polohu každého slova. Barevné buňky X sjednotí
písmena a prázdné konce; barevné Q rozlišují obsazení. Každá hrana uvnitř
slova je primární a použije se právě jednou, takže není možný souběžný
kolineární překryv; kolmý překryv je dovolen, pokud souhlasí písmena.
Zbývající hrana má pomocnou možnost00,01 nebo10. Existuje tedy právě tehdy,
když alespoň jeden její konec není obsazen. Dvě sousední obsazené buňky
musí spojovat některé z předepsaných slov. Opačným směrem každé platné
rozložení dovolí doplnit pomocné možnosti. Rozšíření nemusí být jedinečné:
v prázdných oblastech může mít Q několik slučitelných voleb, jak kniha
správně upozorňuje. Proto se zvlášť počítají modely a skutečné polohy slov.

Pro čtverec lze první slovo položit horizontálně: transpozice páruje
vertikální a horizontální řešení. Použité instance mají odlišná slova
délky alespoň2; domény v našem generátoru jsou výslovné. Souvislost lze
ověřit na grafu překryvů slov, ekvivalentně na rookově grafu obsazených
buněk, protože(ii) zakazuje další kontakty.

| Rozměry | Nativní modely | Různé polohy | Souvislé modely | Souvislé polohy |
|---|---:|---:|---:|---:|
|8×8|9127|4368|20|3|
|7×9|9825|5560|7|3|
|5×11|2|1|0|0|

Veškeré modely byly nezávisle geometricky ověřeny. Vstup8×8 má1192
možností a123+128 položek; DLX2 se sharp preferencí dává23.443166234G
čistých hledacích mems. Odpovídá aktualizaci23G. Lokální PDF i starší PS
uvádějí29G, zatímco erratum má starý údaj20G; tento rozdíl starého znění
nezatajujeme ani nevydáváme za další nový nález. Obdélník5×11 má právě
jednu polohu se dvěma komponentami. Všechny vytištěné mřížky jsou členy
úplných výčtů. Také třísložkový příklad ze zadání je správně.

Windsorova podmínka: nechť s je součet délek a e počet průsečíků. Každá
buňka patří nejvýše dvěma kolmým slovům, takže obsazeno je s−e buněk.
Počet prázdných buněk je mn−s+e. Vybrat alespoň mn−s+w−1 položek E lze
právě když e≥w−1. Nesouvislý les na w slovních vrcholech má nejvýše w−2
hran. Výsledek je proto souvislý nebo obsahuje cyklus, jak kniha říká;
samotná podmínka není test souvislosti. Veškeré prázdné buňky lze označit
E, tedy argument nezávisí na náhodně zvoleném počtu pomocných možností.

Souvislé větvení je obecně možné takto: po deterministických nucených
volbách má každé souvislé dokončení dosavadní komponenty některé dosud
nezvolené slovo připojené k ní. Rozvětvit lze podle nejmenší takové
možnosti a ostatní menší možnosti v dané větvi zakázat. Tím vzniknou
disjunktní úplné větve. Samotný slovní náčrt knihy však neurčuje všechna
pořadí a účtování pro630M; tento konkrétní benchmark dosud nereprodukován.
X109 tedy zůstává partial, s oddělenými potvrzenými F129/F130.

##110–111: wordcross a černobílé diagramy

McDonaldova vytištěná20×20 mřížka byla kompletně přepsána z PDF:
205 písmen, všech38 příjmení, přičemž VAN BUREN tvoří dvě slova, celkem39.
Všechny maximální vodorovné a svislé běhy jsou právě předepsaná slova;
žádná další sousednost, izolované písmeno ani nepovolený překryv; jedna
komponenta. Je to horní mez20 pro stranu čtverce. Kniha označuje19×19
za nedokázaný případ. Nezávislé datované potvrzení atribuce2017 a celý
Gordonův článek o18×22 zatím chybějí; X110 partial.

Úloha111 přechází na slova AAA/AAAA/AAAAA, případně AAAAA/AA/AAAAAAAA,
s násobnostmi12/12/4 a12/8/4. Tatáž redukce s MCC pokrývá všechny diagramy;
odstraňuje se jen označení stejných slov. Nezávislý C++ program vyčerpá
všechny posloupnosti osmi binárních řádků. Průběžně zakazuje délky
ukončených běhů mimo zadání, nadbytečné počty, příliš málo bílých buněk a
nakonec izolované bílé buňky. Nevyžaduje rotační symetrii. Všechny pruning
podmínky jsou nutné: zejména bílé buňky musí být alespoň polovinou součtu
délek slov, protože jedna buňka je nejvýše v jednom řádku a jednom sloupci.

Výsledek(a):4 označené mřížky,2 třídy D4, s1 a3 komponentami.
Výsledek(b):10 označených mřížek,4 třídy D4, s1,1,2,3 komponentami.
Všech6 vytištěných obrazců, tedy384 černobílých buněk, odpovídá celému
seznamu tříd. Běžný DLX3 a varianta se zveřejněnou sharp preferencí jsou
vedeny odděleně; nativní benchmarky závisí na heuristice i pořadí možností.
Již dokončená sharp(b) dává stejných10 mřížek za4.173663072G hledacích
mems; není to přesná reprodukce tiskových5G. Dlouhé běhy nepovažujeme za
hotové před terminální zprávou. Známá errata doplňují definici diagramu
a mění591G na550G pro(a). Úplná matematika hotová, benchmarková mezera
zůstává v X111 výslovná.

##112: Torto

Položka Wkl vybere každý krok slova. Barevné Pkl sjednotí polohu písmene,
Qku je inverzní přiřazení pozice uvnitř slova: dva různé indexy nemohou
použít stejnou buňku. X sjednotí písmena různých slov. Nebarevné Dkv patří
středu jediné diagonální dvojice v daném2×2 čtverci; dovolí pro jedno
slovo nejvýše jednu z křížících se diagonál. Jiné druhy křížení krátkých
královských hran bez společného konce neexistují. Převod je tak obousměrný
a pro dané polohy jednoznačný. V textové poznámce o D11 se mluví o
zabránění dalšímu kroku2–4; to je doslova pravda, ale opakování stejné
hrany již vylučuje Q. Skutečná druhá diagonála je1–5. Tuto neobratnou
ilustraci **nepočítáme jako další potvrzenou chybu**.

`check_torto_small.py` porovnává celé množiny cest v1264 malých instancích
s nezávislým přímým generátorem; souhlasí všech6696 modelů. Zkouší obě
písmena, různé délky i několik dvojic slov. V6×3 je94 orientovaných
královských kroků. Střední krok prvního slova lze odrazit tak, aby jeho
začátek byl v horním levém kvadrantu a konec neležel vpravo: zbývá26
kroků a každá třída odrazů má reprezentanta. Není to přesný výběr jedné
čtvrtiny; střední svislá hrana může ponechat další odrazovou symetrii.
Proto dlouhé výčty rozlišují modely cest, mřížky a čtyři odrazové třídy.

Pět původních Torto mřížek z PDF má všechna uvedená slova i jejich cesty.
První obsahuje všech7 dlouhých slov odpovědi(a). Ve druhé je přesně24
pětipísmenných slov z WORDS(5757), včetně všech uvedených příkladů;
TORTO má přesně dvě cesty. Opravený pravý obrázek YTE místo ETV obsahuje
šest ordinálních slov a také FIFTY/SIXTY. Přesné cesty jsou ve výsledcích.

Fronta `run_torto112.py` využívá původní autorův `torto-dlx.w`. Cílové
počty tříd jsou10,1444,416,553,72853;416 je zveřejněná oprava starého140.
Teprve terminální výsledek a geometrická kontrola dovolují počet přijmout.
U dokončeného ONE–TEN se má navíc projít každá mřížka a hledat ELEVEN,
s povoleným doplněním dosud nepoužitých buněk. Nedokončená fronta ani
její průběžný počet nejsou důkazem nemožnosti přidat ELEVEN.

Získán původní Ricbitův Prolog s autorovým označením roku2011. Obsahově
opravdu sestavuje6×3 mřížku ze seznamu slov, zakazuje opakované buňky i
křížící se diagonály. Původní blog nebyl dostupný; obchodní známka1977,
první číslo časopisu a jeho pozdější periodicita nejsou ověřeny. X112 partial.

##113: alphabet blocks

Každé z25 slov má délku5 a používá všech pět kostek, takže množina písmen
každé kostky musí protínat množinu písmen každého slova. Má nejvýše6
prvků. Úplný nezávislý výčet podmnožin22 písmen proto dává všechny
možné kandidáty. Je jich3223, odABCDEI poLNRTUV, včetně čtyřprvkové ELRT.
Původní MCC se26 položkami a22 možnostmi má **celou stejnou množinu**,
za3917384 hledacích mems, tedy uvedené4M. Výstup MCC obsahuje explicitní
null volby; parser je po zjištěném selhání správně odlišuje od vstupních
možností. Byl přijat původní uložený výstup, hledání se neopakovalo.

Každé slovo vybere permutaci přiřazení písmen kostkám. Každá kostka vybere
jednu úplnou0/1 charakteristickou funkci kandidátní množiny. Barevné
položky zaručí, že všechny použité symboly skutečně leží na dané kostce.
Naopak každá sada kostek a všechny způsoby hláskování dávají model.
FIRST má pět odlišných písmen, proto jeho jediná zvolená permutace
normalizuje všech5! přeznačení kostek bez ztráty řešení.

Počet možností je2371 slovních +5×3223 kostkových =18486. Výskytů položek
je384871; s jedním spacerem na možnost je délka403357, jak uvádí kniha.
Počáteční srovnání bez spacerů bylo chybou našeho počítání, nikoli knihy;
opraveno před spuštěním dlouhého výpočtu.

Nativní výčet má8 modelů a jedinou normalizovanou sadu kostek:
EFGLOS, **CEIRUY**, ALMNQR, ABEPST, DHKTUV. Všechna slova mají jeden
způsob hláskování kromě TIMES,TREES,VALUE, která mají po dvou:2³=8.
Tiskové CETRUY je již opraveno oficiálním erratem. Náklad202.033645955G
odpovídá aktualizovaným202G místo225G. Každý model ověřen přímo.

Vedlejší poznámka, že každé slovo má v kapitole2 přes50 výskytů, dosud
není uzavřena. Casefold OCR dává jiná čísla při celých slovech a při
podřetězcích, zvlášť DEQUE/DEQUES; nutno také přesně oddělit odpovědi ke
kapitole a vydání. `word-frequency-diagnostic.json` je označen jen jako
diagnostika. Žádný nový nález z těchto OCR počtů; X113 zůstává partial.

##114: automorfismy sudoku

Položky u/v vyberou bijekci číslic π. Možnost buňky propojí barvou hodnotu
k v původní buňce s l=π(k) v její α-image. Protože α je permutace buněk,
jsou takto důsledně určeny všechny hodnoty. Původní verze současně
vynucuje sudoku jednotky na obou pohledech; u automorfismu jsou druhé
podmínky redundantní. Zveřejněná Weigelova varianta vynucuje p/r/c/b
přímo v obrazu α. Jelikož α je bijekce, každá buňka/řádek/sloupec/blok
je pokryt právě jednou. Obě formulace jsou bijektivní s požadovanými
mřížkami a jejich (jednoznačně určenými) permutacemi číslic.

Pevná buňka vyžaduje k=l; jinak by nesla dvě barvy. Normalizace prvního
řádku123456789 a zákaz jeho číslice j+1 níže ve sloupci jsou nutné
důsledky sudoku. Totéž v image souřadnicích. Smazání takových možností
neodstraní platný model. Každá mřížka má právě jedno přeznačení prvního
řádku; π se při tom konjuguje a symetrie zůstane zachována. Faktor9! je
proto správný. Vytištěné(28b) má π=(24)(37)(68), zatímco(28a),(28c)
mají konkrétní neslučitelná dvojí přiřazení, uložená v `details-checked.json`.

Nativní původní i opravená formulace4×4 mají stejné celé dvě mřížky.
Opravená9×9 má **30258432** modelů za171.281383015G čistých hledacích
mems, tedy zveřejněných171G. Všechny uložené periodické ukázky mají
platných27 jednotek, první řádek i transpoziční relaci. Počet nezávisle
potvrdil jiný C++ výčet, nikoli opakovaný běh DLX.

Nezávislý výčet: transpozice je involuce, takže π²=id; π(1)=1 kvůli
levému hornímu políčku. V každém diagonálním bloku jsou3 diagonální
políčka s pevnými číslicemi. Mimo diagonálu se hodnoty párují, a pevná
číslice tam být nemůže, jinak by byla v bloku dvakrát. Proto má π právě
3 pevné body. Vyčerpáno všech420 takových involucí s pevným1;180 je
slučitelných s prvním řádkem/sloupcem. MRV prochází horní trojúhelník,
dolní je nucen π; bitové masky kontrolují všechny jednotky. Je to
úplné jednoznačné generování. Výsledek30258432 při371122851 uzlech;
uložené svědky ověřuje samostatný validátor, zdrojové/binární/výstupní
hashes přijaty z terminálního běhu. Staré2.2T nebylo znovu spouštěno:
je nahrazeno konkrétním oficiálním zlepšením, které bylo reprodukováno.

Primární Russellova/Jarvisova stránka z7.9.2005 má v třídě37 počet
30258432 již dělený9!. Její reprezentant na0-based souřadnicích je
α(r,c)=(c+3 mod9,r+6 mod9). Pro β(r,c)=(r+3 mod9,c) platí
α=β∘transpose∘β⁻¹. β je povolená rotace pásů, takže jde o stejnou
konjugovanou třídu sudoku symetrií. Celých81 obrazů bylo porovnáno s
vypsanými cykly zdroje. X114 je úplně reviewed, včetně oficiální náhrady.

## Známé opravy a správa důkazů

- E051:111 doplnění definice černobílých diagramů,30.3.2023.
- E052:109 náklad aktualizován na23G,19.12.2022; staré znění errata20G
  se liší od29G v našich PDF/PS, obojí zaznamenáno.
- E053:111(a),591G→550G,4.11.2023.
- E054:112(c),140→416,8.4.2023; samotné zveřejnění není náš vlastní výčet.
- E055:pravý Torto obrázek ETV→YTE,8.4.2023; opravené cesty ověřeny.
- E056:113 náklad225G→202G,7.1.2023; reprodukován.
- E057:113 kostka CETRUY→CEIRUY,7.1.2023; celý výsledek ověřen.
- E058:114 Weigelova náhrada odpovědi,2.1.2023; důkaz i171G reprodukovány.

Historické dodatky109 z25.5.2021 a16.9.2021 jsou již v našem4B obsaženy.
Nic se neposílá a nevytvářejí se nové emailové návrhy. Nové UI karty jsou
anglicky; české důkazy i osobní poznámky zůstávají oddělené a zachované.
Živé logy dlouhých úloh se nestagují. Běžící zdroje se nemění. Další blok
začíná115; vedle něj se přijímají pouze nově terminální výsledky a doplňují
výslovně uvedené mezery. Tento blok není dokončením svazku4B.


## Pozorování přerušených procesů při integraci

2026-11-02T04:23:26.510858+00:00 — SAT wrapper892255 již není vps a nevytvořil
žádný terminální výsledek. Příčina není doložena. Původní metadata se
zachovávají; nejde oUNSAT ani úplný výčet. MCC111(b) wrapper901947
skončil143, ale vlastníDLX3 child901975 stále běží pod48h timeout901974.
Nebylo posláno žádné ukončení a nic se nerestartovalo. Jeho živý log a
případně neúplný gzip se necommitují ani nevydávají za plný výsledek.
Matematické diagramy(b) již mají celé shodné nezávislé a sharp množiny.
Podrobný stav je v process-observation.json.


2026-11-02T04:28:19.997360+00:00 — MCC111(b) osiřelý solver následně dokončil log s10 řešeními,
799098600906 hledacími mems. Wrapper však již skončil143, nemáme jeho
terminální návratový záznam. Výstup je zachován jako neúplně doložený běh
v diagrams111-b-orphan-terminal.json; nejde o patnáctý přijatý terminál.
Matematický výsledek již ověřila dokončená sharp varianta i nezávislý výčet.
V aktivním seznamu zůstává11živých úloh.

## Doplnění při checkpointu 115–117, 2. listopadu 2026

Sharp varianta 111(a) dokončila celé stejné čtyři mřížky jako nezávislý
výčet; 507.644708130 Gμ není přesná reprodukce historických 550 Gμ.
Nově přijaty obě první Torto sady: 18 modelů/10 tříd a 1877 modelů/1540
mřížek/1444 tříd. Všechny cesty a kanonizace ověřeny. Náklady 711.231759119
a 55.523877046 Gμ ponechávají přesné knižní benchmarky otevřené.

Fronta Torto ztratila řídicí proces během ONE–TEN; jeho child zůstal živý.
Původní metadata a částečný výstup nejsou přijatý terminál. Dvě dosud
nespouštěné pozdější sady pokračují v nové oddělené frontě. Podrobnosti,
nové doklady i přesný rozsah jsou v [navazujících poznámkách](GRAPHS115_120_NOTES.md).
