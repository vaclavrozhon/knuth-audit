# §1.3.2-22: Josefova úloha

Původní s.162,521–522 a obrázek17 zobrazeny; kontrola1.listopadu2026.
Pořadí vytištěné v knize znamená pořadové číslo vyřazení na každé
původní pozici, nikoli seznam postupně vyřazených pozic. Pro n=8,m=4
je tedy správně54613872. Pro požadované n=24,m=11 vychází

```
15 12 22 08 16 11 23 21 03 05 01 17 10 07 24 19 20 18 09 14 04 02 13 06
```

Poslední je původní pozice15. Všechny čtyři vrstvy errat byly
prohledány podle stran i Josephus/Ingalls/Ahrens; relevantní oprava
úlohy22 nenalezena. Křížový odkaz do svazku3 byl prověřen i tamními
čtyřmi vrstvami errat; opravy odpovědi7 se zdejších odpovědí2,5 netýkají.

## Původní program a čas

Pozice interně číslujeme0..n−1. Pro žijící osobu i uchovává X[i]
index další žijící osoby; vyřazené buňky místo toho obsahují dvě
poslední tiskové číslice pořadí. Inicializační smyčka nastaví
X[i]=i+1 pro i<n−1 a X[n−1]=0, tedy počáteční kruh.

Na začátku ROUND je I1 první počítaná osoba a A příští pořadí k.
Přesně m−2 přechodů přivede I1 k předchůdci m-té osoby. LD2 a LD3
zachytí odsouzeného a jeho následníka ještě před přepisem jeho buňky.
CHAR vytvoří desetinné číslice A:X; STX(4:5) uloží pořadí, NUM obnoví
číselné A a INCA je zvýší. ST3 přepojí předchůdce na následníka,
ENT1 nastaví tohoto následníka jako začátek dalšího počítání.
Tím se invariant kruhu induktivně zachovává. Po n−1 vyřazeních
zbývá jediná osoba; její buňka dostane pořadí n a celý výsledek se tiskne.

Předpoklad m>2 je v odpovědi výslovný. Původní zadání má n=24;
matematická smyčka navíc platí pro n>=2 při dostatečných strojových
mezích. Dvě číslice omezují formát na n<=99 a OUT tiskne právě24 slov.
Naše parametrické běhy pro n!=24 proto ověřují kruh a uložená pořadí,
neprohlašují nezměněný OUT za obecný tisk libovolného n. Testy n<=24,
m<=4097 respektují i nejmenší radix64, protože ENT2 potřebuje m−2<=4095.
Živé ukazatele a pozdější tiskové znaky se nikdy nezamění.

Ruční časový součet před OUT, kde u je základní časová jednotka MIX:

| Část | Čas v u |
|---|---:|
| ENT1, STZ a inicializační smyčka | 3+4(n−1) |
| ENTA1 | 1 |
| Jedno vyřazení včetně počítací smyčky | 1+4(m−2)+4+29=4m+26 |
| Poslední CHAR a STX | 12 |

Celkem16+(n−1)(4m+30)=4(n−1)(m+7.5)+16, přesně jako v knize.
Pro24,11 to je1718u. CHAR a NUM mají každý cenu10u; do uvedeného
času nevstupuje OUT ani HLT. Všechny strojové profily souhlasí.

## Ingallsovy tříslovné pakety

Kniha dává nápad, ne úplný program. `packet_program` je naše úplná
realizace včetně vytváření paketů za běhu. Osoba i má paket na
adrese P+3i: DEC2 1; J2P NEXT; JMP REMOVE. Pole NEXT vždy vede
na další živý paket. Samostatné pole BACK uchovává předchozí živý
paket. Při každém počítání se I2 nastaví na m; každý navštívený
paket jej sníží o1. Dokud je kladný, přeskočí se přímo na další
paket. Nulová hodnota vstoupí do REMOVE přes JMP, který uloží
adresu konce právě vyřazovaného paketu do J.

REMOVE z J získá adresu osoby, z NEXT a BACK oba sousedy, přepíše
NEXT předchůdce a BACK následníka. Indukčně tedy zachovává obě
orientace kruhu. Pořadí je v I6; jeho CHAR se ukládá do odděleného
pole RANK, které se nakonec zhutní do24slovného výstupního bufferu.
Platí i m=1 a n=1: tehdy mohou oba sousedé být stejná osoba, ale po
uložení posledního pořadí se kruh již nepoužije. Pole, pakety a
výstup jsou výslovně inicializovány, nikoli závislé na nulové paměti.

Naše varianta podporuje1<=n<=24,1<=m<=4095 ve všech radixech64..100.
Nejvyšší používaná adresa je1523, ukazatele jsou nejvýše572 a čítač
pořadí nejvýše25. Zápisy adres mění jen pole(0:2), takže příkazy
J2P zůstanou příkazy J2P. Asynchronní OUT následuje až po posledním
zápisu a jeho buffer už program nemění.

Její čas před OUT je2nm+61n+107: inicializace8+19n, počítání a
vyřazení n(2m+33), příprava a zhutnění výstupu99+9n. Pro24,11 je
2099u, tedy více než původních1718u; pro24,1000 je49571u proti92706u.
Nápad snižuje hlavní cenu přechodu ze4u na2u, ale režie se vyplatí
teprve u dostatečně velkého m. Netvrdíme optimálnost této realizace.

## Odkaz5.1.1-5 a obecné zrychlení

Originály svazku3 s.17–18 a591–592 zobrazeny a relevantní odpovědi
přečteny celé. Definujme a[i] jako pořadí vyřazení původní pozice i.
Inverzní tabulka b[j] zde znamená počet hodnot větších než j, které
stojí v a vlevo od hodnoty j. Při vyřazování je to právě počet
ještě živých pozic vlevo od j-té vyřazené osoby. Číslování j je od1.
První osoba má mezi n živými index(m−1) mod n. Po vyřazení se
začne na jejím následníku; mezi zbývajícími n−j osobami má další
vyřazený index

```
b[1]=(m−1) mod n,
b[j+1]=(b[j]+m−1) mod(n−j).
```

To dokazuje rekurenci odpovědi2 včetně přechodu přes konec řady.

Pár[g,v] představuje g prázdných míst následovaných hodnotou v;
řetězec párů je zakončen nekonečně mnoha prázdnými místy. Operace
alpha o beta vkládá celý řetězec beta do postupných prázdných míst
alpha. Jestliže první mezery obou řetězců mají délky g a h, pak
při g<=h první vyjde hodnota alpha a beta ztratí g úvodních mezer.
Při g>h první vyjde hodnota beta a alpha ztratí h+1 mezer. To jsou
přesně obě větve tištěné rekurence. Pozor: první nerovnost je <=,
nikoli ostrá <, kterou chybný OCR přepis naznačoval.

Pro důkaz asociativity označme f_alpha(k) polohu k-tého prázdného
místa alpha, počítanou od0. Po vložení beta odpovídají zbývající
prázdná místa zobrazení f_alpha(f_beta(k)). Hodnoty gamma se tedy
v obou uzávorkováních umístí na f_alpha(f_beta(p)), kde p byla
jejich poloha v gamma; hodnoty alpha a beta mají také stejná místa.
Operace je proto asociativní pro všechny konečné řetězce párů.

Součin[b[1],1] o ... o [b[n],n] postupně umisťuje hodnotu j do
b[j]-tého dosud volného místa. Podmínka0<=b[j]<=n−j zajišťuje,
že nevyjde z prvních n pozic; po n vloženích jsou všechny plné.
Výsledek je tudíž přesně[0,a[1]]...[0,a[n]]. Každé složení délek
r,s stojí O(r+s), protože každá větev odstraní jeden pár.
Vyvážené slučování sousedních dvojic vyžaduje nejvýše ceil(log2 n)
vrstev a O(n) práce v každé; celkem O(n log n) času a O(n) prostoru.
Samotná rekurence b potřebuje O(n) aritmetických operací.

Jde o počet operací nad strojovými čísly; pro neomezeně dlouhé m
je nutné započíst cenu víceciferné aritmetiky. Při konstantním m
může být původní O(nm) postup lepší, ale pro velké m uvedená metoda
odstraňuje jeho lineární závislost na m. Nezávislá implementace
vyváženého stromu s počty živých listů potvrzuje totéž: sestup podle
pořadí a odečtení po cestě stojí O(log n) na jednu osobu.

## Validace a prameny

Checker prošel153742 kontrolami:271 původních a327 paketových MIX
běhů, úplné výstupy, invarianty kruhu po každém vyřazení, oba časové
vzorce, všechny37 radixe a zpoždění tiskárny1000u. Paměť před
inicializací obsahovala nenulový odpad. Skládání inverzních tabulek
ověřeno pro všechny permutace do7 prvků, Josefova rekurence proti
přímému modelu do100 osob a stromová varianta navíc do10000 osob.
Obecné důkazy výše nejsou nahrazeny těmito konečnými testy.

Při vývoji vlastních paketů byly opraveny nepodporovaný násobící
literál a vlastní přehlédnutí pravidla MIXAL pro vyhodnocování
výrazů zleva doprava. Původní program těmito chybami netrpěl.
Úspěšný výsledný checker bez nové změny neopakovat.

Ahrens, *Mathematische Unterhaltungen und Spiele*, druhé rozšířené
vydání, svazekII, Leipzig:Teubner1918, je ověřen přímo z titulního
listu. KapitolaXV začíná na s.118; na s.118–120 byla přečtena
formulace legendy a její výslovné zpochybnění autorem. S.154–155
byly zobrazeny a přečteny v rozsahu úvodu a přesné obecné definice
úlohy, která odpovídá TAOCP. Zbylé historické a algebraické části
celé52stránkové kapitoly tím nejsou auditovány; knižní odkaz je
správný. [Původní sken1918](https://archive.org/download/mathematischeun00ahregoog/mathematischeun00ahregoog.pdf).
Uložený výňatek a metadata přesně rozlišují přečtené části.
