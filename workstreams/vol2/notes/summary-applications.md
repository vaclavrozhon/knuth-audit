# §3.6: úlohy 1–6 a zbývající kontext

Přečtena celá původní sazba 184–193 a odpovědi 599–604. Implementace
generátorů a úlohy 8–15 jsou doloženy v `summary-generators.md` a
`discarded-bits.md`; úloha 7 samostatně v `truncated-lcg.md`. Tento blok
uzavírá zbývající programovací zadání, komentáře a vymezené historické
ověření. Úlohy 3–6 nemají v knize jednotnou vytištěnou odpověď.

## 1. RANDI a téměř rovnoměrné celé číslo

Nechť B je počet hodnot MIXového bytu a M=B^5 rozsah kladného slova.
Uvažujeme binární B=64 a desetinné B=100. Konstanta multiplikátoru se
v pěti bytech chápe modulo M; pro B=64 je to 994108973, pro B=100
3141592621. Audit níže ověřuje aritmetiku instrukcí. Nebyl spuštěn
konkrétní assembler a netvrdíme, jak diagnostikuje příliš velkou
číselnou konstantu. Samotná potřeba redukce není vedena jako chyba.

Při vstupu obsahuje A kladné k<5000. STJ uloží návratovou adresu a
STA uloží k, takže pozdější změna registru J instrukcí JOV návrat
neporuší. Po LDA a MUL je v A:X desetibytový součin aX. INCX 1009
přičte c=1009 pouze k dolním pěti bytům a při překročení rozsahu
ponechá zbytek modulo M. JOV na následující instrukci odstraní jak
nové, tak případné staré nastavení přetečení. SLAX 5 přesune dolní
slovo do A, STA jej uloží jako nový stav a další MUL k vloží do A
podíl floor(kX/M). INCA 1 dá výsledek 1..k a znovu nepřeteče.

V obou uvažovaných soustavách je perioda M: c je nesoudělné s M,
a−1 je násobkem 4 a v desetinném případě i 5. Používáme již ověřenou
větu 3.2.1.2A. Za celou periodu tedy každé j=1..k nastane právě

```
ceil(jM/k) − ceil((j−1)M/k)
```

krát. Tyto počty se liší nejvýše o 1. To je přesný význam tvrzení
„about equally probable“ v jednorozměrném modelu; nejde o nezávislost
sousedních návratů ani o záruku vyrovnanosti libovolného krátkého běhu.

Nezávislý model násobí po jednotlivých bytech pomocí školního
násobení, provádí přenos při INCX a skládá horní a dolní poloviny.
1400 případů zahrnuje obě soustavy, k=1/2/4095/4096/4999, oba vstupní
stavy přetečení a cílené hranice těsně před a při přetečení X.
Souhlasí s přímým celočíselným výrazem pro stav i výstup. Nepřidáváme
záruku maximální periody pro všechny hypotetické velikosti bytu 65–99.

## 2. Překvapivý výstup a C0078: rok Lovelace

Úloha vybízí k diskusi, nikoli k důkazu, že náhoda řeší otázku
strojové tvořivosti. Pevný pseudonáhodný program s pevným vstupem má
určený výstup, ale programátor jej nemusí umět předem odvodit bez
výpočtu. Skutečný náhodný vstup navíc mění samotný pravděpodobnostní
model. Ani jedno není totéž jako matematická nebo kryptografická
nepředvídatelnost; úloha 7 naopak ukazuje nutnost rozlišovat tyto pojmy.
Odpověď na 599 čteme jako tento epistemický komentář a nadsázku,
nikoli jako bezpečnostní větu o libovolném generátoru.

Turingův původní článek *Computing Machinery and Intelligence* (1950),
strany 449–451, byl přečten v uchovaném výňatku; strana 450 také
vizuálně. Přisouzení komentáře o překvapení odpovídá původnímu textu.
Turing na 451 výslovně rozlišuje znalost předpokladů od okamžité
znalosti všech jejich důsledků. Nejde o kontrolu celého jeho článku.

V zadání na 189 je rok **1844**. Citovaná pasáž však pochází z poznámky
G na straně 722 v *Scientific Memoirs*, svazek III, **1843**. Původní
strana 722 i titulní strana s rokem 1843 byly přečteny vizuálně.
Uchovány jsou pouze příslušná strana a titulní obraz, s URL a kontrolními
součty v `sources/lovelace-1843.json`. Samostatné hlášení C0078 se týká
roku; nečiní dodatečná tvrzení o přesném dni sepsání, autorství jiných
částí či prvenství algoritmů.

## 3. Kostková hra

Program pracuje se stavem „první hod“ nebo s bodem s v množině
{4,5,6,8,9,10}; výhra a prohra jsou koncové stavy. Při první sedmičce
či jedenáctce vyhraje, při 2/3/12 prohraje, jinak uloží bod. V dalším
stavu je výhrou opakování bodu, prohrou sedmička, vše ostatní stav
nemění. Přesně to požaduje zadání. Deset reprodukovatelných her včetně
každé dvojice cifer a komentáře je v `results/craps-ten-games.txt`.

Pro nezávislé spravedlivé kostky označme w_s počet z 36 uspořádaných
hodů se součtem s. Po založení bodu s je pravděpodobnost výhry
w_s/(w_s+6): z rovnice P=w_s/36+(1−(w_s+6)/36)P. Střední počet dalších
hodů je 36/(w_s+6), protože každý další hod ukončí hru právě s
pravděpodobností (w_s+6)/36. Proto

```
Pr(výhra)=8/36 + sum_s (w_s/36) w_s/(w_s+6) = 244/495,
E(počet hodů)=1 + sum_s (w_s/36) 36/(w_s+6) = 557/165.
```

Součet běží přes šest možných bodů. Nezávisle se ze všech 252
přechodů (sedm nekoncových stavů krát 36 hodů) sestavila matice
přechodových pravděpodobností. Její přesné řešení dalo stejné dvě
hodnoty. Uložených deset her je ukázka programu; nepoužívá se jako
důkaz těchto pravděpodobností nebo kvality pseudonáhodného zdroje.

## 4. Hodinový pasiáns jako konkrétní realizace otevřeného zadání

Zvolena je běžná hra se 13 hromádkami po 4 kartách. Hodnosti jsou
eso,2,...,10,spodek,dáma,král; každá určuje jednu hromádku, král
střední. Program promíchá 52 rozlišitelných karet pomocí již ověřeného
Fisherova–Yatesova postupu a rozdá je do hromádek. Začíná odkrytím
karty ve středu. Každá odkrytá karta se odloží jako zahraná a určí
hromádku pro příští odkrytí. Prázdná hromádka ukončí hru; výhra
znamená, že byly odkryty všechny karty. Zobrazení počtu odkrytých karet
a zbývajících karet v každé hromádce určuje, kolik chybělo do výhry.
Program uchovává histogram těchto výsledků i kumulativní počet výher.
Volitelné podvádění zadání nevyžaduje.

Hra se může zastavit pouze ve středu. Pro jinou hromádku je každá
návštěva způsobena odkrytou kartou dané hodnosti; pátá návštěva by
vyžadovala pátou kartu téže hodnosti, která neexistuje. Střed má navíc
počáteční návštěvu, proto zastavení nastane právě po odkrytí čtvrtého
krále. V každém kroku přibude jedna odkrytá karta; algoritmus tedy
skončí po nejvýše 52 krocích a žádnou kartu neduplikuje.

Při rovnoměrném náhodném rozdání je každá dosud neodkrytá pozice
podmíněně rovnoměrnou kartou ze zbytku balíčku. Platí to i tehdy,
když pozici určíme podle dosavadních odkrytých karet: podmínění
neodlišuje zbývající pozice. Můžeme po skončení hry zbytek odkrýt
v pevném pořadí; celý sled odkrytých hodností má rozdělení náhodného
uspořádání. Pro r hodností s c kopiemi, N=rc, má tedy čas T odkrytí
posledního krále rozdělení

```
Pr(T=t)=binom(t−1,c−1)/binom(N,c),  c<=t<=N.
```

Jmenovatel počítá možné pozice c králů; čitatel vybírá předchozích
c−1 pozic, poslední je t. Výhra má pravděpodobnost c/N=1/r, tedy
u plné hry 1/13. Důkaz nevyžaduje simulaci. Úplný výčet 4296 malých
rozdání pro (r,c)=(2,2),(3,2),(4,2),(3,3) ověřil celé rozdělení T,
nejen četnost výher. Sto uložených deterministicky inicializovaných
ukázkových plných her dalo 13 výher; tento počet nemá sloužit jako
test rovnoměrnosti nebo odhad s nárokovanou statistickou přesností.

## 5. Tvořivé psaní a historická omezení

Zadání umožňuje otevřenou konstrukci, proto nemá jedinou správnou
implementaci. Konečný stav může zaznamenávat polohy osob, předměty
v rukách a obsazené pozice. Přípustné akce jsou přechody, které tento
stav aktualizují; náhodný výběr z nich poskytuje kostru vyprávění.
Předání předmětu například vyžaduje, aby jej předávající držel a
přijímající měl volnou ruku. Tím vzniká konstruktivní vysvětlení, jak
lze splnit mechanická omezení scénářů, bez tvrzení, že výstupy musí
mít literární hodnotu. Zvyšování pravděpodobností po pití je další
stavová závislost, nikoli nový typ výpočetní operace.

U obou původních scénářů na 190–191 byly sledovány pohyby rukou,
předmětů a osob; žádná nevyhnutelná kolize typu dvou předmětů v jedné
ruce nalezena nebyla. Druhé nalití v prvním scénáři je možné, protože
sklenice předtím přešla do levé ruky; v druhém scénáři může stát
sklenice při nalévání na stole. Neuvedené množství whisky, délku
pohybu nebo zásobu nábojů nepovažujeme za nulové. Upravené televizní
scénáře jsou výslovně oddělené verze; jejich rozdíly nejsou chyba.

Archivní inventář Computer History Museum, kolekce X3495.2006,
strany 3–4 a 9, potvrzuje datum 26. října 1960, CBS, TX-0 a uložení
výpisu i schématu programu v jednotce 102648892. Samotná tato
archivní jednotka nebyla přečtena; přesné znění výpisů a osobní
komunikaci uvedenou Knuthem tedy nezávisle nereprodukujeme. Záznam
[ACMI](https://www.acmi.net.au/works/73700--tomorrow-the-thinking-machine/)
potvrzuje producenta Thomase Wolfa a CBS; je to katalog vlastního
filmového exempláře, nikoli naše zhlédnutí pořadu.

Stracheyho článek *The “Thinking” Machine*, Encounter 3(4), 25–31
(1954), byl identifikován přes odkaz na facsimile; získání skenu
skončilo HTTP 403. Proto letní datování 1952, původní hardware a
přesné znění dopisu zůstávají přiznaně Knuthovou historickou zprávou,
ne nezávisle přečteným dokladem. Nekopírujeme tvrzení ze sekundárních
webů jako náhradu chybějícího primárního ověření. Známá změna obtížnosti
úlohy 5 z [46] na [45] z 15. listopadu 2023 je započtena.

## 6. Knihovní generátory a obecný text 184–189

Úloha 6 je organizační projekt. Znění v knize samo neopravňuje měnit
knihovny cizích instalací. Pro tento audit je její obsah prověřen
kontrolou všech skutečně uvedených implementací a jejich testovacích
výstupů v předchozím bloku. Zásadní rozdíl: délka periody a shoda
implementace jsou dokázatelné vlastnosti; vhodnost pro libovolnou
simulaci z nich neplyne. Při změně generátoru je nutné určit, zda
má zůstat zachována bitová reprodukovatelnost starých výpočtů. Jde
o analýzu zadání; žádná organizační síť zde nebyla prohledávána ani
upravována.

Osm doporučení pro lineární generátory je posouzeno v návaznosti na
již prověřené §3.2.1 a §3.3: podmínky periody, vysoká potence, krátké
cykly nízkých bitů, škálování na interval a m^(1/t) jako řád prostorové
přesnosti. Čísla .01m/.99m či m/1000 jsou heuristická doporučení,
nikoli obecné meze chyby. Volba seeda z hodin neposkytuje nezávislost
ani kryptografickou bezpečnost. Tvrzení o dobré kvalitě v dimenzi
menší než 100 je v knize samo označeno jako pravděpodobné. Oddělení
bloků po inicializaci, perioda kombinace a přesnost operací byly
ověřeny v `summary-generators.md`; neztotožňujeme oddělení bloků
s pravděpodobnostní nezávislostí.

Rok obsahuje méně než 2^55 nanosekund (i 366 dní má 31622400*10^9
nanosekund), takže tento přepočet na 187 souhlasí. Upozornění na
dvojkový doplněk a rozdíly mezi C a FORTRAN odpovídají analyzovaným
operacím. Tvrzení „no known defects“ u vynechávání interpretujeme
historicky; vlastní úloha 14 ukazuje nutnost analyzovat konkrétní
vazby i po vynechávání, nikoli záruku náhodnosti.

Vydavatelský abstrakt Ferrenberg–Landau–Wong 1992 potvrzuje obecný
příklad selhání při simulaci Wolffovým algoritmem kvůli korelacím.
Plný článek nebyl získán (APS API HTTP 401), takže údaj o pátém
desetinném místě a přesný průběh s multiplikátorem 16807 se zde
nezávisle neověřují. Nejde o nově zopakovaný fyzikální experiment.
Historická literatura a přehledové knihy na 189 jsou odkazy k dalšímu
čtení, nikoli předmětem tvrzení, že byly všechny přečteny. Známá
oprava citovaného rozsahu Los Alamos Science 125–136 na 125–137
(12. listopadu 2007) je započtena. Dříve získané Eckhardtovo PDF
obsahuje jen 131–136; jeho název s „131--141“ nepoužíváme jako důkaz
rozsahu článku.

Původní souhrn uzavření byl při obnově důkladné kontroly odvolán.
Aktuální rozsah určuje `results/quality-recovery-2026-11-06.json`
a navazující poznámky `recovery-*.md`, zejména
`recovery-summary-projects-2026-11-06.md`. RANDI má přesný instrukční
důkaz pro uvedené dvě soustavy, ale neuzavřený rozsah všech velikostí
bytu a překladu velké konstanty. Další matematické mezery zahrnují
náklady úlohy 13 a adaptivní pravděpodobnostní model úlohy 14;
nejde pouze o nedostupnou historickou bibliografii. Skutečně uzavřené
důkazy a archivní výsledky zůstávají platné ve svém přesném rozsahu.
Fyzický pozdější tisk a prvenství nových nálezů nejsou ověřeny.
Žádné hlášení nebylo odesláno.
