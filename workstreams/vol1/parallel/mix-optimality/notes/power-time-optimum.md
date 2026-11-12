# §1.3.1-22: přesné časové minimum4u bez HLT

X je celé číslo v paměti2000 a |X|^13 se má vejít do jednoho MIX
slova. `Výsledek` zde znamená číselnou hodnotu X^13. Znaménka +0
a−0 představují stejné celé číslo; bitově silnější kontrakt
zachování znaménka nulového vstupu je oddělen níže. Program musí
skončit HLT. Nejhorší čas ostatních instrukcí je přesně4u;
při ceně1u za koncové HLT a bez čekání na I/O je celkem5u.

## Horní mez a obě nuly

Knižní lookup používá LD1 2000; LDA 3500,1; HLT0. V místech
3500+x je předem uloženo x^13. Platí6^13>100^5, takže stačí
x od−5 do5. Pro radix64 a65 se krajní vstupy±5 nevejdou a
odpovídající položky se vynechají; to je známá oprava17.11.2007.
Časy obou načtení jsou2u+2u.

Načtení rI1 zachovává obě znaménka nulového vstupu, ale indexovaná
adresa je v obou případech3500. Tabulka tedy vrátí+0 také pro−0.
Číselné zadání to splňuje. Kdyby bylo navíc předepsáno zachování
znaménkového bitu nuly, tato horní mez by nebyla doložena stejným
programem. Například LD1 2000; ST1 3500(0:0); LDA 3500,1; HLT0
splní i tento silnější kontrakt za6u bez HLT: mění jen znaménko
prostřední tabulkové položky, ostatní x^13 ponechává. Netvrdíme,
že6u je minimum silnějšího kontraktu.

## Dolní mez, včetně vykonávání vstupu jako kódu

Položme radix64, B=64^5, D=64^2−1=4095. Zvolme X=+3, jehož
výsledek1594323 se vejde do slova, ale je větší nežD+3.
Počáteční A,X-registry, indexy a příznaky můžeme vybrat nulové;
ostatní paměť a vnější stav jsou pevné nezávisle na vstupním X,
kromě libovolného kódu a konstant vlastního programu.

Před prvním pozorováním vstupního slova mají běhy se vstupy+2
a+3 stejný stav. Kdyby se rozdíl vůbec nepozoroval, nemohly by
dát rozdílné výsledky2^13 a3^13. Uvažujme program s časem všech
instrukcí kromě závěrečného HLT nejvýše3u.

Pouhé tvrzení „čtení stojí2u“ by zde nestačilo, protože instrukční
fetch sám stojí jen1u. Nezměněné slovo+3 má však číslice
(0,0,0,0,3), tedy operační kód MUL. Jeho vykonání stojí10u bez
ohledu na pole a není v rozpočtu. Předchozí změna jiných bajtů
než posledního kód3 nezmění. Přepsání posledního bajtu naopak
vymaže jediný rozdíl mezi vstupy+2 a+3, pokud už nebyl přečten
nebo zkopírován. STORE trvá2u, ale původní bajt nikam nekopíruje.
MOVE s alespoň jedním slovem trvá nejméně3u a nemění A; v tomto
rozpočtu již nezbývá žádná další instrukce, která by vypočetla
požadovaný velký výsledek. Žádná dřívější příprava vstupního
slova jako kódu tedy neobchází nutné pozorování vstupu.

OUT může vstup také pozorovat, ale jen jej předává zařízení,
nikoli do A nebo indexu. Zbudou-li po něm2u, lze buď načíst
nezměněný vstup, nebo pevné původní slovo paměti; není čas
současně na IN i následné načtení do A. Samotné OUT nemění
žádnou podmínku, podle které by CPU rozlišilo+2 a+3. Tato
možnost proto velký vstupně závislý výsledek neposkytne.

Zbývá běžné čtení do CPU za2u: LDA/LDAN, načtení jiného
registru, ADD/SUB nebo porovnání. MUL/DIV a plovoucí paměťová
aritmetika jsou dražší. Pole čteného slova+3 má velikost0 nebo3.
Z rozpočtu zůstává před nebo po tomto čtení nejvýše jedna
instrukce za1u. Ta může změnit A jen přičtením/odečtením adresy
velikosti nejvýše D, nebo nastavením takové adresy. Z počátečního
A=0 proto všechny možnosti dávají |A| nejvýšeD+3, nikoli1594323.
Načtení do indexu tuto mez nemění: ani pozdější ENTA nemůže
nastavit větší než dvoubajtovou efektivní adresu. Skok, I/O,
změna příznaku či paměti A samo nevypočítá.

Vnější zařízení neposkytuje vstupně závislý oracle. Jeho pevný
počáteční stav lze zvolit nezávisle na+2/+3; přenos na zařízení
sám A nemění a následné paměťové načtení opět stojí2u. Totéž
platí pro případné přepsání instrukcí z tohoto pevného zdroje.

Program s nejhorším časem nejvýše3u bez HLT tedy neexistuje.
S horní mezí4u jde o globální časové optimum číselného zadání,
bez omezení počtu konstant nebo samomodifikace.

## Zdroje a zbývající prostorová mez

Originály143 a509 přímo přečteny. Všechny čtyři vrstvy errat
již přímo přečteny v errata-additions; cílený výpis je
../../../sources/mix-description-errata-extract.json. Opravy
3.5.1999 zpřesňují znaménkovou větu Pattova programu,
28.9.1997 vylučují HLT z času54u a17.11.2007 kvalifikují±5.
Žádná z nich nemění tento čtyřjednotkový lookup.

Sedmislovná násobicí smyčka je správná horní mez prostoru,
včetně HLT a bez pomocné konstanty. Její minimálnost mezi všemi
programy se zde **neuzavírá**. Důkaz délky addition chain pro13
se netýká samomodifikace, lookupů ani vykonávání dat jako kódu,
a proto z něj dolní mez sedmi paměťových slov neplyne.
