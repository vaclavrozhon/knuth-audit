# Úlohy 90–95: parita, výzkumné meze a oba protipříklady

Checkpoint X0111, P1040–P1048. Originály p91/file108
a p551/file568 včetně detailů všech tří nových sítí
prohlédnuty. Úlohy 93/94 již úplně pokrývá proof-078
a neopakují se. Žádný matematický program neběžel.

## Celý dvouvstupový modul 90 — P1040

Původní obrázek má přesně komparátor obou linií,
invertor na spodní, druhý komparátor a druhý spodní
invertor. Pro vstup (a,b) jsou stavy

    (a∧b,a∨b),
    (a∧b,¬(a∨b)),
    (0,(a∧b)∨¬(a∨b)),
    (0,a XOR b).

Nulový první výstup plyne z (a∧b)∧¬(a∨b)=0.
Druhý výstup před poslední negací je ekvivalence
a,b. To dokazuje celou mapu na obou bitech a
všechny čtyři nakreslené moduly.

## Obecná konstrukce i správné umístění parity — P1041

Pro t≥1 udržujme uspořádaný seznam aktivních linií.
Na každou sousední dvojici seznamu použijme souběžně
P1040; její horní linie je nyní nula a spodní nese
paritu celé dvojice. Při lichém počtu poslední
nepárovou linii ponechme. Nový seznam tvoří spodní
linie párů a případná nepárová poslední linie.

Invariant: aktivní linie nesou parity disjunktních
neprázdných skupin původních vstupů, které společně
tvoří všechny vstupy; ostatní linie jsou nuly a už
se nepoužijí. Po spojení párů invariant platí,
protože XOR parit disjunktních skupin je parita
jejich sjednocení. Počet aktivních linií klesne
z s na ceil(s/2), takže proces skončí jednou.

Poslední původní linie t zůstává vždy nejnižší
aktivní linií: je buď spodní z posledního páru,
nebo nepárová. Konečná parita je tedy přesně na
požadovaném výstupu y_t, všechny předchozí výstupy
jsou nula. Pro t=1 je identita hotová; t=0 nemá
indexovaný poslední výstup a není doménou tohoto
zadání.

## Úplné náklady a hloubka 90 — P1042

Jeden pár má dvě porovnání a dvě inverze, hloubku
4. Po r fázích je počet aktivních linií ceil(t/2^r),
takže hloubka je nejvýše 4 ceil(log2 t). Každý
pár sníží počet aktivních linií o 1; párů je proto
přesně t−1, modulů 4(t−1). Přímé vytváření seznamů
stojí O(t) práce a O(t) paměti včetně výstupu,
protože jejich délky tvoří klesající geometrický
součet do jediné poslední linie.

Také řád hloubky je nutný: hodnota na linii po h
úrovních modulů závisí nejvýše na 2^h původních
vstupech. Indukce používá nejvýše dva vstupy
komparátoru a jediný vstup invertoru. Parita
závisí na každém z t bitů, tedy h≥ceil(log2 t).
Tím je úloha 90 včetně lichých velikostí a ceny
dokončena bez enumerace vstupů.

## Přesný externí vstup k motivaci 91 — P1043

Primární Springer článek Ajtai–Komlós–Szemerédi,
*Sorting in c log n parallel steps*, Combinatorica
3 (1983), 1–19, DOI 10.1007/BF02579338, v abstraktu
výslovně uvádí O(n log n) komparátorů, O(log n)
paralelních kroků a pevné předem zvolené dvojice
registrů. To je přesně model sítě v knize.
Tuto hlubokou existenční větu bereme jako pojmenovaný
primární externí vstup; celý expanderový důkaz
nezávisle nerekonstruujeme.

Přívlastek „asymptotically optimum“ má i nutnou
dolní mez. Výstup maximum závisí na všech n
vstupech, takže předchozí argument dává Ω(log n)
hloubky. Pro libovolné různé hodnoty má síť m
porovnání nejvýše 2^m sekvencí výsledků a musí
rozlišit n! jejich vstupních pořadí. Proto
m≥log2(n!)=Ω(n log n); stačí n!≥(n/2)^(n/2)
pro velká n. Princip 0–1 P0997 přenáší správnost
booleovského třídění na všechny uspořádané hodnoty.
Obě horní meze externí věty jsou tudíž řádově
optimální i v relevantním modelu.

## Matematický kontext odpovědi 91 — P1044

Strom má jeden odlišný řez na každou hranu podle
P0929. Strom s t hranami má t+1 vrcholů a jeho
redukované štítky mají dimenzi t; to zdůvodňuje
tištěný počet vrcholů ve speciálním případě.

Neprázdná množina bitových štítků uzavřená na
AND/OR je svaz: tyto operace jsou přímo její
infimum/supremum pro souřadnicové uspořádání.
Distribuční identity platí po souřadnicích, tedy
jde o distributivní svaz. Corollary F/P1011
poskytuje po permutaci souřadnic síť bez invertorů.
Tato existence sama nedokazuje O(log t) hloubku.
P1039 naopak dokazuje obecnou horní mez O(t).
To je přesná souvislost tří tvrzení, která se
nesmějí zaměnit.

## Výzkumné úlohy 91 a 92 — P1045/P1046

P1045, partial: existence O(log t) CI retrakce
pro libovolné mediánové štítky, včetně případů
stromů a distributivních svazů, zde není vyřešena.
Věta v odpovědi o možné potřebě invertorů se týká
požadované malé hloubky; nevyvrací comparator-only
existenci z Corollary F. Není doložen konkrétní
případ, který by při optimální hloubce invertory
nutně vyžadoval. Současný výzkumný stav se nepodařilo
rychlou primární rešerší nezávisle ověřit; netvrdíme,
že je otázka otevřená i k dnešnímu dni.

P1046, partial: otázka 92, zda invertory dovolí
zmenšit celkový počet modulů třídicí sítě, zůstává
nevyřešena. Jde o počet všech modulů včetně
invertorů, nikoli jen komparátorů či hloubku.
Kniha ji označuje výzkumným hodnocením a samostatnou
odpověď 92 neuvádí. Absence nalezeného článku není
důkaz žádné z možností. Žádná enumerace optimálních
sítí ani náročné rozhodování nebyly spuštěny.

## První celý protipříklad v odpovědi 95 — P1047

Čtyřliniová síť vpravo má komparátory C14, C12,
C34, C13 v tomto pořadí a jediný invertor I4
mezi C14 a C34 (souběžný s C12). Při vstupu
(a,b,c,d) položme p=a∧d a q=a∨d. Po prvních
třech stupních jsou stavy

    (p,b,c,q),
    (p∧b,p∨b,c,¬q),
    (p∧b,p∨b,c∧¬q,c∨¬q).

Poslední C13 dává přesný obecný výstup

    (0, p∨b, (p∧b)∨(c∧¬q), c∨¬q),

protože p∧¬q=0. Dosazením vytištěných vstupů
dostaneme 0001→0000, 0010→0011 a 1101→0110.

Každý výstup splňuje y3≤y2∨y4: první člen
p∧b je nejvýše y2, druhý c∧¬q nejvýše y4.
Vektor 0010 tuto nutnou podmínku porušuje, takže
jej síť nevydá z žádného vstupu. Je však bitovým
mediánem tří uvedených výstupů 0000,0011,0110.
Obraz sítě není mediánový. To prokazuje všechny
konkrétní hodnoty i univerzální neexistenci
požadovaného výstupu, bez testování 16 vstupů.

## Celý protipříklad bez invertorů — P1048

Šestiliniová síť vlevo má v pořadí

    C13, C24, C35, (C13 a C46), C24, (C12 a C56).

Závorky označují disjunktní komparátory nakreslené
ve stejné fázi. To je všech osm modulů obrázku.
Vstup 000000 je zjevně fixován. Na 010101 každý
komparátor dostane buď stejné bity, nebo již
uspořádanou dvojici, takže jej také ponechá.
Na 101010 prvních šest komparátorů porovnává
shodné bity; poslední C12 a C56 mění dvojice
10 na 01, takže výstup je přesně 011001.

Po posledním C13 platí a≤c a po posledním C24
platí b≤d. Tyto c,d se už do konce nemění.
Poslední C12 dává y2=a∨b, a proto každý konečný
výstup splňuje y2≤y3∨y4. C56 se těchto souřadnic
nedotýká. Vektor 010001 tedy nemůže být výstupem,
protože má y2=1 a y3=y4=0.

Přitom je mediánem tří doložených výstupů
000000,010101,011001. Ani obraz čistě komparátorové
sítě tudíž nemusí být mediánovou množinou. Všechny
tištěné hodnoty i tvrzení „nothing maps to“ mají
obecný argument; nebylo procházeno 64 vstupů.

## Bibliografie, odkazy a přesné meze

Primární Elsevier záznam potvrzuje Mayr–Subramanian,
*The complexity of circuit value and network stability*,
JCSS 44(2) (1992), 302–323, DOI
10.1016/0022-0000(92)90024-D. Přesná historická
priorita a celý obsah článku se neprohlašují za
ověřené; matematika 90 je úplná bez něj.
Původ připsaný Federovi u druhé sítě nebyl ověřen
z jeho rukopisu nebo korespondence.

Odkazy §5.3.4–50 a –52 byly nalezeny a prohlédnuty
v originálu V3 p242/file253: opravdu pojednávají
o identitách souvisejících operací a obtížnosti
rozhodování správnosti komparátorové sítě. Nejde
o nový důkaz celých těchto úloh a protipříklady
P1047/P1048 na jejich řešení nezávisí.

Věta o zdánlivé absenci „easy characterization“
je neformální komentář, nikoli prokázaná dolní
mez složitosti. Nezaměňujeme ji s otázkami 91/92.
Všech pět relevantních vrstev 4A/F0 errat prověřeno;
známý dodatek k 88 byl již úplně zohledněn.
Žádný nový nález, program ani census. 90 a 95
jsou celé dokončeny; 91/92 mají přesné výzkumné
limity. Další matematický blok začíná textem
p75/file92 a související úlohou 96.
