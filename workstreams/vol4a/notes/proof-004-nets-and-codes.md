# Individuální audit §7–20 až24: sítě a kódy

6. listopadu2026. Zadání file54–55/str.37–38, odpovědi file535–536/518–519.
Na519 cíleně auditovány23–24, odpovědi25 a další jsou další kurzor.
Původní sazba prohlédnuta, pět relevantních4A/F0 vrstev errat prohledáno.
Žádný nový program. Nález C0001 se přebírá beze změny; žádný další nález.

## §7–20: kořeny jednotky

Pro n>1 polož ω=exp(2πi/n). Dvě řádky OA obsahují všechny dvojice(j,k)
právě jednou, takže bilineární součet je Σω^(j+k)=(Σω^j)²=0.
Pro hermitovský skalární součin dostaneme analogicky Σω^(j−k)=0.
Geometrický součet je0 právě díky ω≠1 a ω^n=1. Hranice n1 je již
zachycena v C0001; důkaz ani errata se neopakovaly jako nový nález.

## §7–21(a,b,c)

(a) Tranzitivita: jestliže L∥M a M∥N, ale různé L,N se protínají v p,
jsou přes p dvě různé rovnoběžky s M, v rozporu s axiomemiii. Reflexivita
rovnosti a symetrie disjunktnosti jsou přímé; dostáváme třídy rovnoběžnosti.

(b) Každým bodem prochází právě jedna přímka každé třídy: pokud bod není
na zvolené přímce třídy, použije seiii. Přímka M jiné třídy protne každou
přímku L původní třídy právě jednou a tím vyčerpá své body. Existuje tedy
bijekce mezi body M a přímkami libovolné jiné třídy. Počet bodů je tudíž
stejný na všech přímkách téže třídy. Argument funguje i pro nekonečné množiny.

(c) Při alespoň třech třídách srovnáme dvě přes třetí. Všechny přímky pak
mají společnou velikost n a všechny třídy n přímek. Každý bod leží na m
přímkách, jedné z každé třídy. Dvě zvolené třídy určují bijekci bodů
s dvojicemi jejich přímek, tedy celkem n² bodů. To ověřuje i dodatek odpovědi.

## §7–22 a projektivní dovětek19

Pro běžný nedegenerovaný rozsah n>1,m≥2 jsou body sloupce OA; přímka
(řádek,symbol) je množina jeho výskytů. Každý řádek je rozklad na n přímek.
Dvě různé řádky dávají právě jeden průsečík libovolných dvou takových přímek,
protože každá dvojice symbolů nastává právě jednou. Axiomy sítě i m tříd
tedy platí. Degeneraci n1, kde pojmenované třídy mohou splývat, tato kontrola
neprohlašuje za vyřešenou; kvůli prioritě úlohy se nerozšiřuje stávající C0001.

Obráceně konečná síť s m≥3 třídami má podle21 n přímek v každé třídě a n²
bodů. Označ přímky každé třídy čísly0..n−1 a zapisuj u každého bodu jeho
příslušnost. Každá dvojice symbolů ve dvou řádcích má jediný průsečík,
takže vznikne OA. Pro jednu třídu mohou být části rozkladu nestejně velké;
pro dvě třídy obecně vznikne obdélník n×n′, nikoli nutně n×n. Proto obecný
obrácený výrok bez omezení neplatí, přesně jak odpověď uvádí.

Maximální hloubka n+1 dává afinní rovinu: přes pevný bod jde n+1 přímek
s disjunktními zbylými n−1 body. Pokrývají všech(n+1)(n−1)=n²−1 ostatních
bodů, takže libovolné dva body mají právě jednu spojku. Přidáním jednoho
bodu v nekonečnu ke každé třídě a jedné společné přímky v nekonečnu vznikne
projektivní rovina: dvě rovnoběžky se potkají v příslušném novém bodu,
ostatní průsečíky a spojky jsou jednoznačné. Obráceně odstranění jedné
přímky projektivní roviny dává uvedenou afinní síť a OA. Pro n>1 jsou
splněny i běžné nedegenerační požadavky roviny. Historické citace přeskočeny.

## §7–23(a,b,c)

(a) Pokud minimální Hammingova vzdálenost d>2t, koule poloměru t okolo
různých kódových slov jsou disjunktní trojúhelníkovou nerovností. Naopak
při vzdálenosti s≤2t rozděl s rozdílných souřadnic na dvě části velikosti
nejvýše t. Slovo, které se na jedné části shoduje s x a na druhé s x′,
je od obou vzdálené nejvýše t. Jednoznačná korekce tedy není možná.

(b) Délka je4 a počet slov b². Oprava jedné chyby je ekvivalentní vzdálenosti
alespoň3, tedy dvě slova se shodují nejvýše v jedné souřadnici. Každá dvojice
souřadnic proto obsahuje b² různých dvojic symbolů, právě všechny. Slova
jsou sloupce OA hloubky4 a podle18 jsou ekvivalentní dvojici OLS.

(c) Stejný argument pro délku m=r+2 říká, že vzdálenost≥r+1 je ekvivalentní
OA hloubky r+2, tedy r vzájemně ortogonálním čtvercům. Pro b>1 skutečně
nastane rovnost minimální vzdálenosti r+1: v pevné souřadnici jsou dvě
různá slova se stejným symbolem, protože b²>b. Není tak nepozorovaně
nahrazeno „distance r+1“ slabší podmínkou. Abeceda b1 je degenerovaný
případ s jediným slovem; zde se předpokládá obvyklé b≥2.
Známý dodatek2024 mění bibliografii a vysvětluje standardní notaci kódu;
matematický argument tím není dotčen.

## §7–24(a,b) a příklad25 bodů

(a) Liší-li se informační části v l≥1 bodech, vyber jeden z nich p. Z m
přímek přes p se nejvýše l−1 dotkne jiného změněného bodu (dva body sdílí
nejvýše jednu přímku). Nejméně m−l+1 kontrolních bitů se tedy změní.
Celková vzdálenost≥l+(m−l+1)=m+1; pro l>m je mez triviální již z dat.
Změna jediného informačního bitu změní právě m kontrolních bitů, takže
minimální vzdálenost je přesně m+1.

(b) Pro bod p tvoří svědky jeho přijatý bit y_p a pro každou přímku přes p
součet jejího kontrolního bitu se všemi ostatními datovými bity na ní.
Bez chyby mají všechny m+1 hodnot hodnotu x_p. Podpory svědků jsou
disjunktní: přímky přes p sdílejí jen p, který byl ze součtů vynechán;
kontrolní bity jsou vlastní každé přímce. Každá přenosová chyba tak ovlivní
nejvýše jednoho svědka. Pro m=2t je většina2t+1 svědků správná při≤t
chybách. Po opravě dat se kontrolní bity mohou znovu spočítat.

Efektivní implementace nejprve spočítá syndrom S_l jako XOR celé přijaté
přímky a jejího kontrolního bitu. Svědek pro p je y_p XOR S_l; y_p se
obrátí právě tehdy, když více než t jeho syndromů je1. Náklady jsou
O(Nm+R) bitových operací při seznamu incidencí, protože se součty přímek
nepočítají znovu pro každý bod.

Pro N25,R30,m6 jsou podpory sedmi vytištěných svědků x1 přesně:

    {1}
    {26,2,3,4,5}
    {31,6,11,16,21}
    {36,10,14,18,22}
    {41,9,12,20,23}
    {46,8,15,17,24}
    {51,7,13,19,25}.

Vycházejí z nulových symbolů šesti řádků OA v19, jsou disjunktní a souhlasí
s původní sazbou. Poslední kontrolní bit55 odpovídá {5,6,12,18,24},
tedy symbolu4 v poslední řádce. Vynechání posledních10, resp.20 kontrolních
bitů odstraní dvě, resp.čtyři celé třídy: m4 dává vzdálenost5/opraví2 chyby,
m2 dává vzdálenost3/opraví1. Indexace i tvrzené dekódování souhlasí.
Citace Hsiao/Bossen/Chien se samostatně neověřovala.
