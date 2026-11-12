# DLX77–83 a barevné pokrývání na stranách87–90

Ověřeno 2. listopadu2026. Lokální 4B je první vydání, druhý dotisk2022.
Tištěné stránky87–90/132/433 jsou PDF107–110/152/453. Autorův
`fasc5c.ps.gz` má odpovídající stránky23–26/68/137 (PDF+6).
Originální stránky byly zobrazeny; OCR sloužilo pouze k navigaci.

## Výsledek a rozsah

77–82 mají dokončené důkazy i kontrolu odpovědí. U83 je doložena chyba
**F123**, která přetrvává i po známém erratu z1.1.2020; níže je úplný
protipříklad a obecný důkaz postačujícího doplnění předpokladů.
Barevné koncové položky jsou další interpretační mezera, ne druhý nález.

Hlavní strany88–90 jsou prověřeny včetně obou paměťových tabulek,
všech27 oválů obrázku72 a správnosti AlgorithmC. Strana87 zůstává
částečná: historická poznámka má kandidáta **C025** a nebyla ještě ověřena
úplnost výběru27 jmen vůči všem přispěvatelům Acta a rejstříkům TAOCP1–3.
Odpovědní strana433 začíná ještě úlohu84, kterou tento blok nepokrývá.

## F123: opakované zakrytí dřívější položky v odpovědi83

Primární položky jsou `p,q`, sekundární `a,b,c`. Vstup:

```text
p q | a b c
p a
p a b
p c
q a
```

Zvolme nejprve `p`, což zadání výslovně dovoluje. Jeho tři možnosti končí
navzájem různými sekundárními položkami `a,b,c`; každý řádek obsahuje
primární položku, žádný neobsahuje tutéž položku dvakrát a všechny barvy
jsou implicitní. Zadání nikde nezakazuje, aby se `a` objevilo také uvnitř
druhé možnosti pro `p`.

Požadovaný počet řešení je nula. První i druhá možnost pro `p` kolidují
s jedinou možností `q a`. Třetí možnost `p c` by sice dala obyčejné přesné
pokrytí, ale podmínka83 zakazuje použít dřívější položku `a`.

Doslovný algoritmus přesto vrátí `p c` a `q a`:

1. Po neúspěšné první větvi dodatečně zakryje `a`. Tím skryje uzel `q`
   posledního řádku. Toto zakrytí má přetrvat do všech dalších větví.
2. Druhá možnost `p a b` znovu zavolá `cover(a)`, ačkoli `a` už je
   zakryté. Při návratu běžné `uncover(a)` obnoví uzel `q`, který měl
   zůstat skrytý. Délka a samotný seznam se navíc rozcházejí.
3. Třetí větev najde obnovené `q a` a vypíše zakázané řešení.

Nezávislé kontroly:

- Doslovný interpret `colored_dlx.py`, včetně spacerů a C5/C6, ukládá celý
  sled operací a stav v okamžiku chybného řešení.
- Původní Knuthův DLX2 sestavený z archivovaného CWEB zdroje má pouze
  dvě výslovné úpravy: volbu `p` v kořeni a instrukci z odpovědi83 po
  běžném odkrývání. Také vrací `p c + q a`; tiskne dokonce `q a (1 of 0)`.
  Sestavení, oba upravené zdroje, vstupy, stdout/stderr a SHA‑256 jsou
  v `results/colored_basics/native/`.
- Explicitně rozšířený problém má třetí řádek `p a b c`. Přímá kontrola
  všech podmnožin, obyčejný interpret i původní DLX2 shodně dávají nulu.
  Druhý řádek už `a,b` obsahuje, takže nevzniká žádná duplicita položky.

Postačující oprava zadání: každá označená koncová položka `s_j` se mezi
možnostmi pro `p` vyskytuje pouze v té j-té a její výskyt je bez explicitní
barvy. Nemusí být unikátní mezi ostatními možnostmi vstupu.

Důkaz opravy: po větvích1…j−1 trvale zakryté položky s1…s(j−1)
odstraňují přesně nepřípustné zbývající možnosti. Všechny možnosti pro
`p` jsou od C4 skryté ve všech ostatních sloupcích, takže tato trvalá
zakrytí jejich seznam pro `p` nezmění. Nová podmínka brání tomu, aby
j-tá možnost znovu zakryla některou již trvale zakrytou položku. Běžné
rekurzivní volby se k takové položce nemohou dostat, protože každý jejich
řádek s ní je skrytý. Po zpětném návratu zůstává trvalá část nedotčená;
dodatečné `cover(s_j)` rozšíří invariant na další větev. Indukcí dostaneme
přesně požadované výsledky. Celkem1000 nezávisle generovaných instancí
s těmito předpoklady má totožné úplné množiny řešení s explicitním
rozšířením a přímým výčtem podmnožin. Nejde o důkaz bez uvedených podmínek.

Barevná mezera: pro `p a:A / p b / q a:A` barevný test v odpovědi83
trvalé zakrytí `a` přeskočí, a proto povolí i druhou větev. Zda název
`s_j` v zadání už implicitně znamená neobarvený výskyt, je otázka výkladu.
**F123 na této otázce nezávisí**, protože jeho protipříklad nemá barvy.

Autorův starší PS má v odpovědi83 ještě `j>N`; známá oprava **E042**
předepisuje `j>N1` a lokální4B ji obsahuje. F123 používá tuto opravenou
podmínku. Starý chybný práh není nový nález. Ve všech šesti relevantních
textových vrstvách errat nebyla nalezena oprava sdílených koncových položek.
Čtyři aktuální originály od autora byly znovu staženy a hashově souhlasily
s archivem. Tištěný exemplář ani soukromou evidenci autora nemáme ověřené.

## 77: vnoření grafu

Pro jednoduché neorientované grafy na n vrcholech zavedeme primární
položky v a v′. Možnost pro přiřazení v↦v′ obsahuje tyto dvě položky
a všechny sekundární dvojice ee′, kde e je hranaG incidentní s v a e′
nehranaH incidentní s v′. Vytištěný velký znak sjednocení není další
položka; přepis byl porovnán s původním obrazem odpovědi.

Primární položky vynutí bijekci. Dvě zvolené možnosti mohou sdílet ee′
pouze tehdy, když zobrazují oba konce e na oba konce e′; na stejný vrchol
nebo ze stejného vrcholu by už kolidovaly primárně. Sekundární omezení
tedy přesně zakazuje zobrazit hranu na nehranu. Obráceně žádné vnoření
takovou kolizi nemá. To dokazuje obě implikace i jednoznačnost kódování.

Všechny4166 dvojice grafů pro n0…4 byly zkontrolovány výčtem všech
permutací a nezávisle přes XC. Shodují se celé množiny přiřazení, včetně
prázdných grafů, izolovaných vrcholů a obou orientací hran. Historické
**E040** z2.3.2020 opravuje „vertices“ na „edges“ a doplňuje větu zadání;
obojí je v lokálním4B již správně.

## 78–79 a obrázky71–72

Všech12 vytištěných řádků odpovědi78 má přesně15 znaků. Každé z27 jmen
se v nich vyskytuje právě jednou zleva doprava. Překryvy jmen dávají
požadované184 znaků na180 polích; geometrie všech řádků byla ověřena.

Pro slovo délky k v n×n poli jsou čtyři vodorovné/svislé orientace,
každá s n(n+1−k) počátky. Čtyři diagonální orientace mají po
(n+1−k)² počátcích. Zde k4…11 a žádné slovo není palindrom; generování
všech souřadnic a barevných možností dává počty
1296,1144,1000,864,736,616,504,400. Četnosti délek
2,5,6,5,3,5,0,1 dávají přesně24320. Všech pět možností v(48) je
správných, včetně posledního slova psaného opačným směrem.

Z původních PDF vektorů bylo načteno450 znaků obou polí; obě matice
se přesně shodují s nezávislým ručním přepisem. Každé jméno má právě
jeden výskyt v osmi směrech. Jejich184 písmen zabírá135 různých polí;
střední R patří do přesně šesti vyjmenovaných jmen, sousední T do pěti.
Zbylých90 písmen dává přesně text na straně88, začínající **These**.
První vlastní test chybně očekával „Those“; originál i extrakce shodně
ukázaly „These“, takže šlo o opravu našeho přepisu, ne nález v knize.

Všech27 původních oválných křivek obrázku72 bylo samostatně načteno.
Členství středů písmen v každém oválu odpovídá právě jednomu celému
jménu a každé jméno má právě jeden ovál. Bézierovy křivky byly vzorkovány
40 body na segment; klasifikace je stejná pro tři malé posuny středu
písmena. Proto nejde pouze o vyřešení puzzle bez kontroly vytištěné kresby.

## 80: celá paměť, včetně skrytých uzlů

Generická inicializace z pěti možností(49) přesně reprodukuje všechny
definované položky tabulky2. MRV při rovnosti volí první primární sloupec.
Stopa: kořen q, uzel8; coverx, purifyy:A, coverp; r je prázdné.
Po zpětném odkrytí zkusíme uzel20, purifyx:A; dále p, uzel12,
coverr, již purifikované x přeskočit, covery. První řešení je [20,12].

Všechny vytištěné hodnoty L/R/T/U/D/C na straně433 souhlasí, také u
skrytých uzlů a spacerů. Pomlčky v hlavičkových barvách jsou úmyslně
nekontrolované, protože kniha je neurčuje: slouží pouze jako cache
pro výpis, nikoli jako podmínka algoritmu. Úplný výčet má jediné řešení
(druhá a čtvrtá vstupní možnost); potvrzuje je přímý výčet podmnožin
i původní nezměněný DLX2. **E041** sdružuje již zapracované opravy
barev spacerů/hlaviček, popisků LEN/TOP a terminologie commit.

## AlgorithmC: invariant a kontroly81–82

Na vstupu do C2 obsahuje každá aktivní primární hlavička právě dostupné
možnosti pro její pokrytí. Cover odstraní možnosti kolidující s právě
zvolenou primární nebo neobarvenou sekundární položkou. Purify odstraní
z ostatních sloupců právě možnosti s jinou barvou dané sekundární
položky; kompatibilní uzly označí −1, aby se nemusely znovu zpracovávat.
Zvolený kladný výskyt není v tomto okamžiku v seznamu sekundární
položky, protože byl skryt při zakrytí zvoleného primárního sloupce.
Zůstane tedy kladný a správně vlastní pozdější unpurify.

Uzel s−1 lze vynechat při hide/unhide: jeho barva už je vynucena
nadřazenou volbou a on nesmí provádět nové cover/purify. Ostatní uzly
skrytých řádků zůstávají korektně odstraněné. Opačné pořadí undo obnovuje
přesně původní sousedy, barvy a délky. Hlavičková barva se obnovovat
nemusí, protože se z ní nikdy nerozhoduje. C2 tudíž hlásí právě úplná
primární pokrytí s konzistentními sekundárními barvami. C3–C8 zkouší
všechny a každé právě jednou, neboť každá možnost obsahuje primární položku.

Interpret prošel3586 vstupními maticemi proti úplnému výčtu podmnožin:
všech1586 podmnožin velikosti0…5 z12 možností se dvěma primárními a
jednou sekundární položkou, plus2000 určených náhodných případů se dvěma
sekundárními položkami a až10 možnostmi. Každý případ používá dvě
politiky volby sloupce; shodují se celé množiny řešení a obnoví se veškerá
rozhodující paměť. Jde o doplněk obecného invariantu, ne důkaz pro všechny
instance pouze konečným testem.

81: nejsou-li explicitní barvy, žádné purify se nikdy nespustí, COLOR
zůstává nula a každý commit/uncommit je obyčejný cover/uncover.
Oba algoritmy mají tedy stejnou posloupnost operací a stejná čtení/zápisy
starých polí. Pokud TOP/COLOR sdílejí octabyte, nové čtení barvy není další
mem. Rozdíl je inicializace nulových barev. Toto je tvrzení o knižních
memech, nikoli o nanosekundách nebo počtu instrukcí procesoru. Všech306
neobarvených matic v uvedené sadě má shodné úplné stopy X/C při obou
politikách, včetně závěrečné paměti. Původní DLX2 také výslovně popisuje
toto společné účtování TOP/COLOR.

82: LEN se čte pro MRV jen v aktivním primárním seznamu. Cover,
purify i jejich inverze procházejí sekundární sloupce ukazateli a délku
ke svému rozhodování nepoužívají. Vynechání změn sekundárního LEN tedy
nemění žádnou volbu ani dostupnost, indukcí se celý výpočet shoduje.
U všech3586 matic jsou po této optimalizaci stejné celé stopy i profily.
Případný tisk sekundárních délek už samozřejmě neudává aktuální velikost.

## C025: historická poznámka o Acta Mathematica

Strana87 i autorův PS23 uvádějí21. výročí a tabulku vydanou1913.
Vydávající Institut Mittag-Leffler na své stránce datuje založení do1882.
Původní Domarův článek v Acta Mathematica148(1982),3–8, na poslední
straně dokládá předání prvního výtisku12.12.1882. Celý článek a jeho
strana8 jsou archivovány. Prosté1882+21=1903 s uvedeným1913 nesouhlasí.

Podařilo se získat také původní bibliografický bulletin z1913:
L'Enseignement Mathématique15, str.525–533, PDF s titulním listem10stran.
Strana528 výslovně potvrzuje179 stran Rieszovy tabulky svazků1–35,
autorský rejstřík a portréty. Původní výchozí odkaz vracel HTML ověření;
veřejně nabídnutý odkaz pro roboty s `bot=1` dodal skutečné PDF.
HTML není vydáváno za původní dokument a zůstává zvlášť v archivu.

Koornwinderovo osobní svědectví z knihovny z1995, dostupné přes webový
nástroj na NIST, potvrzuje rok1913 a životopisy; přímé stažení HTML
vrací403. Chybí však samotná Rieszova předmluva a ověření konkrétní
oslavované události. **C025 proto zůstává kandidátem**: neprohlašujeme,
zda má být30. výročí období1882–1912, nebo31. podle roku vydání.
Rovněž nebyla ověřena úplnost27 vybraných jmen vůči původní tabulce
a hlavním svazkům. Bibliografická mezera nebrání uzavřít matematické78–79.

Zdroje: [vydávající institut](https://www.mittag-leffler.se/publications/),
[Domarův celý článek](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6309-11511_2006_Article_BF02392722.pdf),
[původní bulletin1913](https://www.e-periodica.ch/cntmng?bot=1&pid=ens-001%3A1913%3A15%3A%3A304),
[Koornwinder1995](https://math.nist.gov/opsf/misc/op2616.html).

## Reprodukce

`python3 audit-2026-10-31/check_colored_basics.py` kontroluje celé
matematické jádro, tabulky,4166 dvojic grafů a validaci interpretu.
`check_wordsearch_vectors.py` kontroluje původní PDF vektory;
`check_colored_native.py` sestaví původní DLX2 a obě výslovné varianty;
`check_colored_errata.py` porovná aktuální originály s archivem.
`check_colored_sources.py` zachová dostupné zdroje i chyby přístupu.
Výsledky jsou v `results/colored_basics/`, historické prameny
v `sources/colored_basics/`. Úspěšné výčty není třeba opakovat.
