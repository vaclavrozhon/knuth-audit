# Faktorizace hlavolamů: 7.2.2–62 až 69

Průběžný audit 1. listopadu 2026. Zdroj: 4B, první vydání, druhý dotisk,
strany 52–53, 59–60, 409–411; autorův `fasc5b.ps`, 11. září 2019.
Původní PDF i relevantní autorovy stránky byly zobrazeny. Fyzický výtisk
neověřen. Nic nebylo odesláno.

## 62: náhodné kostky, F093 a kandidát C016

Pro n kostek je každá protější dvojice barev neorientovanou hranou multigrafu.
Smyčka přispívá stupněm dva. Volíme jednu ze tří hran každé kostky tak, aby
každá barva měla stupeň dva. Dva takové výběry musejí být disjunktní po
kostkách. Hrany se rozlišují i při shodných barvách.

Pár faktorů s počty komponent a,b má 2^(a+b+1) fyzických orientací:
nezávislé orientace cyklů a přiřazení obou faktorů oběma protějším stranám.
Proto silná jednoznačnost znamená jediný pár a oba faktory souvislé.
Samostatný Python skládá skutečné rotace krychle (24 matic s determinantem1)
a pro 450 náhodných případů n=2..5 souhlasí s grafovou formulí. Vytištěný
příklad hlavního textu i úlohy63 má tři faktory, jediný disjunktní pár a osm
fyzických orientací, tedy jedno řešení po celkových otočeních řady.

F093: řádek procent pro 0,1,...,9,≥10 párů v odpovědi62 obsahuje
74.4,4.3,8.7,1.3,6.2,0.2,1.5,0.1,2.0,0.0,12.2. Součet je110.9%,
což nelze vysvětlit zaokrouhlováním jedenácti položek na desetiny procenta.
Pět milionů rovnoměrných případů dává poslední položku1.2105%; oprava je
pravděpodobně1.2%. Chybu potvrzuje PDFp409 i autorův PSp47.

Přesně E(počet faktorů)=3^4·8!/(2!^4·4^8)=25515/8192=3.1146240234375,
v souladu s3.115. E(počet párů)=6^4/2·[8!/(2!^4·4^8)]²;
už Markovova nerovnost vylučuje12.2% pro alespoň deset párů.

Přesná silná jednoznačnost byla počítána ukotvením jednoho Hamiltonova
4-cyklu. Pro druhý je72 přiřazení hran, skryté hrany mají10^4 možností;
nesmyčky se váží dvěma. Ze720000 kanonických případů je vážených101680
silně jednoznačných a15040 navíc s každou barvou alespoň pětkrát.
Násobitel pro fyzické barvy je6^4·1152·16/2=11943936: volby dvojic os,
1152 orientovaných prvních Hamiltonových cyklů, orientace druhého faktoru
a dělení dvěma za jeho záměnu s prvním.

Celkem vychází1214459412480/2^48=0.4314626567%.
Po podmínění alespoň pěti výskyty každé barvy vychází
179636797440/58001290611264=0.3097117246%.
Kniha uvádí přibližně0.3% a0.4% v opačném pořadí. C016 zůstává kandidátem:
neznáme velikost autorova náhodného vzorku, nejde o tvrzení přesných hodnot.
Úplná vážená enumerace 100290905 multisetů čtyř typů kostek doběhla a dává přesně stejné počty. Jde o jiný prostor enumerace; používá tentýž lokální grafový řešič, který byl navíc ověřen fyzickými rotacemi.

První běh této enumerace doběhl všemi multisety, ale skončil na naší chybné
kontrolní konstantě: C(223,4)=100290905, nikoli100291905. Opraveno;
původní metadata s chybovým návratem zůstávají uložena. Nešlo o chybu knihy.

## 63: pět kostek

Vytištěné protější dvojice (12,13,34),(02,03,14),(01,14,24),
(04,13,23),(01,12,34) jsou silně jednoznačné, s počty barev5,8,5,6,6.
Pět milionů náhodných pětikostek obsahuje590194 případů s každou barvou
alespoň pětkrát. Z nich je48875 slabě jednoznačných (8.28117%) a3167
silně jednoznačných (0.53660%); souhlasí s orientačními8.4% a0.5%.

Při přesně šesti výskytech každé barvy zůstane po odečtení dvou disjunktních
2-faktorů opět 2-faktor, protože stupně jsou6−2−2=2. Každé dva ze tří
faktorů dávají řešení s jinými skrytými osami. To dokazuje závěrečné tvrzení.

## 64: písmenové kostky

`check_letter_cubes.py` skládá každou síť v celočíselných 3D souřadnicích,
rotuje ji všemi24 vlastními rotacemi a čte písmena podle skutečné orientace.
MuPDF trace potvrdil natočená G,R,W a obrácené U; prostý text PDF toto ztrácí.
Pracuje se slovníkem5757 slov Stanford GraphBase použitým v předchozím bloku.

Každá kostka má16 platných orientací. Celkové rotace zachovávající osu řady
mají osm prvků, první kostka tedy dva reprezentanty. Ze131072 konfigurací
je6144 kompatibilních. Po všech120 permutacích vychází jedno řešení se
čtyřmi slovy RIGHT,UNION,WRONG,CYNIC; jedno se třemi a39 se dvěma.
Všechny počty souhlasí s knihou. Doplňkové příklady také souhlasí: jedno umístění má UNTIL vedle HOURS, čtyři mají SYRUP proti ECHOS. Vytištěné GRHTI,NCICY a obrácené NWRGO,OUNNI odpovídají vypočtenému řešení před přerovnáním. Pro každé písmeno z uvedené množiny CHINOUXZ lze při každém čtvrtotočení zvolit směr čtení, což dokazuje tvrzení o24 orientacích.

Původní model dovoloval navíc W otočené o180° jako M; tak vyšlo6849.
Po odstranění této nadbytečné konvence vychází6144. Není to nález v knize;
písmena nelze při modelování zaměňovat jen podle neformální podobnosti.

## 65: NP-úplnost

Archivován primární článek Demaine et al., Variations on Instant Insanity
(2013), z autorova webu. Přečtena redukce Positive-NAE-SAT na čtyřboké
hranoly s osmi přípustnými rotacemi a úplné důkazy převodu partial→complete.
Doplnění na kostky je jednoduché: každému hranolu přidat dvě protější čelní
stěny nové barvy c a přidat jednu celou kostku barvy c. Tato kostka obsadí c
na všech viditelných stranách, takže ostatní kostky musejí mít c skryté.
Tím zůstává přesně osm rotací původních hranolů. Původních m barev a m
hranolů se změní na m+1 barev a m+1 kostek. Ekvivalence je obousměrná;
příslušnost do NP má certifikát s jednou z24 orientací každé kostky.
Historické tvrzení o konkrétní redukci z exact cover v Robertson–Munro1978
zatím nelze uzavřít: plný originální článek ještě nemáme.

## 66: kruhový hlavolam, F094

Čtyři prstence jsou přepsány od severu po směru hodinových ručiček;
číselné vstupy jsou v `results/factor_puzzles/verified.json`.
Úplný výčet8³ možností s pevným prvním prstencem dává jedinou čtveřici
otočení v osminách kruhu (0,3,4,5), po směru hodinových ručiček.

Podmínka N+E+S+W=48 nechá parity(0,0,0,0),(0,1,0,1), jak uvádí kniha.
Podmínka N+S=24 potom nechá **čtyři**, nikoli dvě konfigurace modulo180°:

| Otočení v osminách | N+S | NE+SW | E+W | SE+NW |
|---|---:|---:|---:|---:|
| (0,2,0,2) |24|19|24|29|
| (0,2,2,2) |24|20|24|28|
| (0,3,0,1) |24|24|24|24|
| (0,3,2,1) |24|25|24|23|

F094: p410 říká, že9+(6nebo7)+(4nebo4)+(7nebo4) nemůže dát24;
ale9+7+4+4=24. První dvě možnosti v tabulce se vyloučí až požadavkem
NE+SW=24. Opravený důkaz tedy může zůstat faktorizovaný; konečné řešení
knihy platí. Stejné znění má autorův PSp48. Známé erratum18.2.2023
opravuje pouze „pages28“ na „page28“, tento mezikrok neopravuje.
Historické publikace Ernst–Goldstein1982 a Slocum–Botermans1992 ještě
nebyly dočteny; věta o prvočíselném počtu paprsků se vztahuje k této
faktorizaci cyklické grupy, nikoli k nemožnosti jakéhokoli zjednodušení.

## 67: devět kartiček

Všech18 orientovaných kartiček dává144 platných uspořádaných řádků.
Skládání tří disjunktních řádků a kontrola šesti sloupcových součtů dává
právě72 řešení; vytištěné8473,2515,3454;4245,2547,7452;7755,1351,5537
je mezi nimi. 72=6·6·2 odpovídá permutacím řádků, sloupců a společnému
půlotočení všech karet. Redukce modulo2 a následné nucené orientace jsou
správné. Historická citace byla přesně ověřena na straně219 dobového skenu (Jim Storer, druhá varianta obálky, PDF122). Původní sken Internet Archive má strany219–220 vynechané; proto se citace v jeho OCR nedala najít. Nový úplný sken byl archivován a stránka zobrazena.

## Co ještě zbývá v tomto bloku

Gridgemanových434 typů; uvedené historické prameny; doplňky64;
šipková propagace68 a oficiální náhrada odpovědi69 z14.3.2023.
Nálezy nejsou zárukou prvenství, pouze potvrzením rozporu v našich zdrojích.

## Přesná distribuce čtyř kostek

Úplné výsledky jsou v `distribution-exact.jsonl` a `distribution-summary.json`.
Všechny váhy se sečtou na 2^48. Podmíněný počet souhlasí s nezávislým
multinomickým součtem přes počty barev nejméně pět.

| Počet párů | Bez podmínění (%) | Každá barva nejméně 5× (%) |
|---|---:|---:|
| 0 | 74.38068089 | 37.24547845 |
| 1 | 4.32182645 | 6.56087428 |
| 2 | 8.77055166 | 17.43283242 |
| 3 | 1.29121165 | 4.09885483 |
| 4 | 6.26722565 | 16.25543219 |
| 5 | 0.19213731 | 0.87608880 |
| 6 | 1.45358611 | 5.30216052 |
| 7 | 0.07315091 | 0.31545704 |
| 8 | 2.00766063 | 6.74354124 |
| 9 | 0.03150201 | 0.15129078 |
| ≥10 | 1.21046671 | 5.01798944 |

Podmíněná střední hodnota počtu faktorů je 4.895637891051609.

## F095: údajně nemožný vzor kostky v odpovědi64

Zobrazený vzor má B, A otočené po směru hodinových ručiček, D na třech
sousedních čtvercích v řadě. PDFp409 i autorův PSp47 to potvrzují; natočení
písmen také odpovídá transformačním maticím MuPDF.

Tento vzor není nemožný. Doplňme ostatní tři stěny písmenem O a skryjme
stěnu A spolu s její protější stěnou. B a D budou viditelné na protějších
stranách, jedno pro běžné a druhé pro obrácené čtení; zbývající viditelné
stěny mají O. Slova na různých stranách přitom smějí mít různou orientaci,
jak ukazuje i vlastní úplné řešení knihy.

Přesný model ve standardním pravotočivém rámci, před rotací:
B: normála+z, horní směr+y; A: normála+x, horní směr−z;
D: normála−z, horní směr+y. Zbývající O mají normály−y,−x,+y.
Při ose řady+x se tedy A a jedno O skryjí. Úplný výčet dává8 platných
orientací. Po otočení D v síti o90° jich je0: horní směry tří nesymetrických
písmen pak zakážou všechny tři možné osy řady. To je možná oprava obrázku.

Errata4B iFascicle5, současná i úplná, žádnou opravu odpovědi64 neobsahují.
Jde o chybu doplňkového příkladu; vlastní pětikostkový hlavolam i všechny
jeho číselné výsledky v knize jsou správné.

## 68: šipkové domény

`check_arrows.py` získává100 směrů a32 nápověd přímo z vektorových obrysů
a souřadnic glyfů PDF. Stejně načte100 číslic řešení z p410; směr všech
šipek v obou obrázcích souhlasí. Nápovědy tvoří prvních32 číslicπ a jsou
vůči středu symetrické. Každá ze100 výsledných hodnot přesně počítá různé
číslice na příslušném paprsku.

Doslovná lokální procedura refine s množinami g_l byla porovnána s
nezávislým přímým součinem domén pro1000 náhodných případů. Souhlasí i
idempotence: další stejné zpřesnění už žádnou doménu nezmění.
Důvod bezpečnosti řezu: počet různých prvků v prefixu může každým dalším
prvkem vzrůst jen o0 nebo1. Množina g_l proto zahrnuje každý dosažitelný
prefixový počet; na konci g_n=a_0 testuje přesnou přípustnou hodnotu.
Sjednocení podpor přes všechny přijaté n-tice odstraní pouze hodnoty,
které nemohou patřit k žádnému řešení. To je obecný důkaz korektnosti.

Při všech čtyřech vyzkoušených přirozených variantách řazení a evidence
změněných parametrů se všechny domény zúží na jediné číslice vytištěného
řešení. Tím je prokázána i jednoznačnost. Počty zpřesnění262,264,292,302
a4–5 kol závisely na jiném plánování aktualizací. Dodatečně nalezený
původní `back-pi-day.w` reprodukoval přesně **301 zpřesnění, 6 kol
a 6 865 501 memů**. Jeho všech 100 směrů, 32 nápověd i konečné
řešení souhlasí s nezávislou extrakcí PDF a přímým hodnotitelem.
Původní program udržuje frontu aktivovaných vrcholů, nejprve volí
nejstarší kolo, pak nejmenší aktuální součin velikostí domén; při shodě
rozhoduje pořadí ve frontě. Doklad `results/questionnaires/pi-day-verified.json`
a reprodukce `run_questionnaires.py`. Výkonnostní metrika je tedy uzavřená.
Citace původu v Puzzler128(1992)p75 ještě nebyla dočtena.

## 69: aktualizované řešení z roku2023

Oficiální náhrada odpovědi69 ze14.3.2023 obsahuje hlavolam Germána
Gonzáleze-Morrise s35 nápovědami. Všech100 šipek a35 číslic je získáno
z vektorového PDF errat (all4b, PDF10), které bylo také zobrazeno.
Čteny po řádcích tvoří přesně31415926535897932384626433832795028.
Nápověda0 v posledním řádku, šestém sloupci míří mimo desku;
to umožňuje překonat32číslicový limit vnitřních šipek. Několik dalších
nezadaných okrajových polí také míří ven a má hodnotu0.

Po přidání triviálního pravidla pro vrchol bez následníků dá stejná
bezpečná propagace ze68 jediné řešení ve2kolech/156zpřesněních.
Všech100 rovnic i35 nápověd bylo následně přímo překontrolováno.
Odpověď69 je tedy matematicky uzavřena s použitím již zveřejněného
doplnění, nikoli novým nálezem. Otázka navíc o souměrném rozmístění
prázdných polí zůstává v aktuálních oficiálních erratech otevřená;
netvrdíme, že by byla vyřešena.
