# Celé file54/p46 a odpovědi file110–112/p102–104

Rozsah je každá vytištěná věta a každá část kódu na těchto stranách.
Nejde o kontrolu pouze vybraných příkladů. File109 je současně
aktualizována novým úplným maskovým důkazem úlohy17. Původní obrazy
file110,111,112 byly zobrazeny. Starší běhy se neopakovaly.

## File54: všechna čtyři zadání

Úloha17 a její doporučení tabulky jsou zpracovány v
`exercises-1.3.2-017-recovery.md`: obor adres, zarovnání, všech256
opcodes, libovolná XYZ, PUT dovětek, všechny návraty a náklady.
Octabyte varianta SR21/LDO vybírá přesně osmibytový slot; doporučení
tabulky není tvrzením univerzálního instrukčního minima.
Širší hodnotová/stavová interpretace legality zůstává přesně
vymezena jako partial, s konkrétními SAVE/PUTI/RESUME případy.

Zadání18: obě vytištěné matice adres souhlasí s A+8i+j:
první řádek A+9..16, druhý A+17..24, poslední A+73..80.
Signed byty mají hodnoty −128..127. Rovnost s řádkovým minimem
a sloupcovým maximem výslovně dovoluje shody; žádná z obou rutin
nesmí předpokládat jedinou polohu minima. Oba úplné důkazy níže
pokrývají tento obor i návrat nuly při absenci sedla.

Zadání19 rozlišuje rovnoměrných72! pořadí různých hodnot a všech
2^72 binárních matic; jejich důkazy se neslučují. Zadání20 požaduje
analýzu obou modelů a třetí naznačené metody. Vytištěný distinct
průměr není automaticky důkazem binary části ani celého zadání.
Nový C0018 vyvrací druhý vytištěný čas; zbývající úplné očekávané
analýzy jsou stále partial. Proto file54 není argumentově úplná.

## File110: závěr17 a celé Solution1

ODIF/POP závěr17 a obě explicitně přiznaná omezení odpovědi jsou
samostatně dokázány v maskové poznámce. Kód opravdu neodmítne
SAVE$0,0 a netestuje výslednou cílovou adresu skoku. Na této straně
se neobjevuje tvrzení, že by tyto případy odmítal.

### Solution1: vstup, invariant a všechny větve

A=Data_Segment, a00=A, a10=A+8. Matice A+9..80 je čitelná;
A+1..8 je zapisovatelná disjunktní pomocná oblast. Kód ani báze
se nemění. Pracovní GREG nekolizují s lokály ij=$0 a $1; t=$255
je scratch. Předpokládá se platný vstupní subroutine frame pro
POP1. Program nevolá žádnou další podprogramovou rutinu.

Před RowMin pro řádek i máme ij=8i, 1≤i≤9. SET j,8 a LDB
čtou a_i8, protože a10+ij=A+8i+8. První 2H/4H vynuluje k,
zvýší jej na1 a uloží sloupec8. Invariant po zpracování sloupců
j..8: x je jejich minimum; A+1..k obsahuje právě všechny jejich
indexy, kde se minimum vyskytuje, každý jednou, 1≤k≤9−j.

Přechod přes1H sníží ij a j. Při j=0 už nic nenačítá a jde
na ColMax. Jinak LDB čte další a_ij a t=x−y leží −255..255.
Pro y>x je t<0, PBN přejde zpět do1H a seznam se nemění.
Pro y<x je t>0: SET nahradí x, PBP přejde na2H, starý seznam
se resetuje a 4H uloží právě nový index. Pro y=x je t=0:
SET zachová x, PBP nepřejde, JMP4B přidá další index do seznamu.
Všechna tři pořadí jsou pokryta, staré neplatné buňky za k se
nikdy nečtou. Po n=8 sloupcích je ij=8(i−1), x=R_i a seznam
obsahuje všechny a pouze řádkové minimální indexy.

ColMax načte poslední index c∈1..8 do$1, j=c+64. LDB přes a10
čte nejprve a_9c. Invariant: všechny již navštívené nižší řádky
mají hodnotu≤x. CMP je přesné signed srovnání. Při x<y jde PBN
na No; tento sloupec nemůže mít maximum x. Jinak SUB j,8
postoupí o řádek nahoru. Pro poslední řádek1 skončí j=c−8≤0;
PBP nepřejde a byly prohlédnuty všechny řádky. Tehdy x=R_i=C_c.
ADD ij,ij,$1 a LDA přes a10 vrátí A+8i+c, správnou adresu sedla.

Na No se k sníží. Při k>0 BP zkusí další dosud neověřený index;
při k=0 byly odmítnuty všechny minimální polohy řádku. Pokud
ij>0, je i≥2 a RowMin začne správně předchozí řádek. Pokud ij=0,
byl poslední právě řádek1; všechny řádky jsou odmítnuty a POP1
vrátí přesně0. Je-li k>0, nemůže tento neúspěšný návrat nastat.

Vnější index řádku klesne nejvýše8krát, každý řádek má8 hodnot,
seznam nejvýše8 sloupců a každý sloupec nejvýše9 hodnot. To dává
ukončení i O(mn+mnm) přímý horní odhad pro zobecněnou m×n
tie verzi; globální optimálnost se netvrdí. V našem oboru se
indexy vejdou do−7..72, adresy doA+1..80, k/j do0..8; neexistuje
zápis do samotné matice nebo signed overflow. Všechny ukončovací
testy skutečně odpovídají registru≤0, jak tvrdí úvodní komentář.

### Přesná cena all-zero pro Solution1

V prvním řádku je každá hodnota rovna x a vznikne seznam8 indexů.
První zkoušený sloupec projde všech9 řádků a program skončí.

RowMin včetně počátečního SET ij: úvodních šest instrukcí stojí
6υ a2μ; každá ze sedmi dalších rovností stojí15υ a2μ; závěrečné
SUB ij,SUB j,taken BZ stojí5υ. Celkem116υ+16μ. ColMax výběr
LDB/ADD stojí2υ+μ. Devět sloupcových LDB,CMP,PBN(not-taken),SUB
stojí9·6υ+9μ; osm taken a jeden not-taken PBP stojí11υ.
Závěrečné ADD,LDA,POP stojí5υ. Celkem **26μ+188υ**.
Mispredicted PBN i PBP byly započítány jednotlivě; nejde o
převzetí vytištěného součtu nebo o nový běh.

## File111: celý minimax theorem a první část Solution2

Pišme R_i=min_j a_ij, C_j=max_i a_ij. Pro všechna i,j platí
R_i≤a_ij≤C_j, a tedy max R≤min C. Pokud a_i0,j0=s je sedlo,
R_i≤a_i,j0≤s=R_i0 pro každé i, takže R_i0=max R; obdobně
s=C_j0≤a_i0,j≤C_j pro každé j, takže C_j0=min C. Opačně
R_i0=C_j0 sevře a_i0,j0 mezi dvě shodná čísla, takže jde o sedlo.
Tím je dokázána celá vytištěná ekvivalence a též poslední věta:
sedlo neexistuje právě při max R<min C, tj. každý R_i<každé C_j.
Není použita odlišnost hodnot a m,n jsou kladná konečná čísla.

Solution2 má stejné disjunktní oblasti a data jako první řešení.
a20=A+16. Pro sloupec j dává ADD ij,j,56 a LDB přes a20 hodnotu
a_9j. Vnitřní smyčka přes a10 pak čte a_8j až a_1j; x je maximum
již přečtených hodnot. CMP/CSN ponechá větší z x,y i při shodě.
Po posledním SUB je ij=j−8≤0, STB uloží přesně C_j na A+j.
Inicializace z=1000 je větší než všech127; CMP/CSN proto udržuje
minimální C z dosud dokončených sloupců. Vnější smyčka provede
právě všech8 sloupců. Každá vytištěná poznámka této fáze souhlasí.

V Phase2 je na vstupu řádku ii=8(i−1), ij=ii+8,j=8. LDB přes
a10 čte a_i8 a dále se snižujícími indexy a_i7..a_i1. t=z−x
je bezpečný signed rozdíl. t>0 odmítne řádek, t<0 přeskočí
hlavičkový test, t=0 načte C_j a zapíše ans právě při C_j=z.
Všechny tři případy jsou jiné větve s úplně doloženým významem.
Pokračování a návraty jsou dokázány v následující části a v C0018.

## File112: pokračování18, celé19/20 a první řádek21

SUB j/SUB ij/PBP přesně pokračují po řádku. Pokud projde celý
řádek, všechny hodnoty jsou≥z a z=min C; minimax theorem dává
R_i=z. Navíc existuje j0 s C_j0=z; a_i,j0 musí být současně≥z
a≤C_j0=z, takže CSZ nejménějednou uložil platný index právě
z tohoto úspěšného řádku. LDA/POP tedy nezávisí na původní hodnotě
ans ani na neplatném kandidátu z dřívějšího řádku.

No sníží ii o8; PBNN zahrnuje i ii=0, tedy řádek1. Teprve ii=−8
ukončí neúspěšné hledání, SET ans,0/POP vrátí0. Známé erratum
PBP→PBNN z roku2012 už je v kontrolovaném programu použito.
Výše se tato opravená větev nepovyšuje na nový nález.

Úplný profil v `MMIX-C0018-saddlepoint-average-cost.md` dává pro
all-zero R=1,K=H=8,S=1 přesně **96μ+517υ**, včetně396υ první
fáze a121υ druhé. První fáze má80 mems, druhá16. To je současně
kontrola vytištěného pevného časového tvrzení, bez simulátoru.

Třetí návrh smí ponechat jen průnik množin řádků, kde každý
sloupec s minimálním C_j=z skutečně nabývá z. Každé sedlo má
row minimum z, takže z≤a_i,j≤C_j=z pro všechny tyto sloupce;
žádný skutečný kandidát se neztratí. Při odlišných hodnotách má
už první takový sloupec jediné maximum, takže zbude nejvýše
jeden řádek. Při ties může zůstat více řádků; pro nulovou matici
všech9. Slovo „usually“ tedy není použito jako univerzální věta
o nespecifikovaném rozdělení. Konkrétní třetí kód/náklad je v úloze20
dosud otevřen, nikoli odvozen z pouhé nutné podmínky.

Historické trial průměry147μ+863υ a95μ+510υ pro hodnoty−2..2
mají v textu pouze roli zprávy o několika měřeních. Není uveden
seed, počet pokusů ani celý vzorek. Původní experiment nebyl
reprodukován ani nahrazen novým náhodným během; přesné výsledky
obou all-zero případů jsou naopak dokázány výše.

AMM98(1991),418–419: primární bibliografické záznamy potvrzují
název a šest autorů, ale původní dvoustránkový článek zatím nebyl
získán (publisher přístup403). Tvrzení O(m+n) probes a O(m log n)
pomocných operací je **explicitní bibliografický skip**; pozdější
články, které jej jen citují, nejsou vydávány za přečtený důkaz.

### Úloha19: obě přesné pravděpodobnosti

Při různých hodnotách dávají společná hodnota všech sedel a disjunktní
možnosti jejich polohy P=m!n!/(m+n−1)!; úplný pořadový argument je
znovu uveden v C0018. Pro9×8 je to17/binom(17,8)=1/1430.

V binární matici je sedlo0 právě tehdy, když existuje nulový sloupec;
každá jeho buňka je současně řádkové minimum. Sedlo1 existuje právě
při jedničkovém řádku; každá jeho buňka je sloupcové maximum. Tyto
jevy se vylučují, protože průsečík takového sloupce a řádku by musel
být0i1. Jednotlivé sloupce jsou nezávislé, jednotlivé řádky také;
nepředpokládáme jejich vzájemnou nezávislost. Dostáváme přesně

`P=2−(1−2^−m)^n−(1−2^−n)^m`.

Pro9×8 je již uložená exact-fraction kontrola
`results/saddle19-probability.json`: 924744796234036231/2^64,
reciproční hodnota přibližně19.94793. Starý výpočet se neopakoval.
První union terms dávají n2^−m+m2^−n a absolutní chybu nanejvýš
binom(n,2)2^−2m+binom(m,2)2^−2n podle první Bonferroni nerovnosti
v každé rodině. Tím je zdůvodněna i vytištěná aproximace, ne pouze
jedno desetinné číslo. U všech kladných m,n funguje přesná formule.

### Úloha20 a přechod21

C0018 dává samostatný obecný rozpor druhého distinct časového výrazu,
originál a všech13 relevantních errata vrstev. Získaný14stránkový
autorský report Hofriho–Jacqueta výslovně nepočítá MMIX instrukční
koeficienty a nelze jím tyto koeficienty bez převodu ospravedlnit.
Jeho bibliografická verze a širší podmínky knižního rozvoje zůstávají
rozlišeny. Úplné očekávané počty pro druhý program, první průměrná
formule a binary/third-variant srovnání nejsou tímto nálezem uzavřeny.
Úloha20 zůstávápartial; historické označení checked se nepřenáší.

Poslední řádek odpovědi21 uvádí pouze Farey SET y,1;…POP, nikoli
celý program nebo důkaz. Přesný zbytek jejího zadání a řešení bude
mapován s file55/113. Tento úryvek nesmí sám zezelenat file112.

## Stránkový stav a použití kvalitativních vzorů

File110 a111 mají úplné argumentové pokrytí každého tvrzení zde
vytištěného, včetně pokračujících kódů přes hranici strany.
File54 a112 zůstávajípartial; file109 nadále explicitně odděluje
statický kód17 od silnější stavové interpretace zadání.

Vzor úplného invariantního důkazu byl použit na všechny tři větve
row minima, všechny shody maxima, kandidátní seznam, neinitializovaný
ans, final row a úplné vrácení výsledku. Vzor krátkého obecného
protipříkladu vedl u C0018 k asymptotické dolní mezi bez brute force;
ani přesný all-zero profil není použit jako důkaz průměrné formule.
Z modelového příkladu převzatých důkazů se zde používá jen uzavřený
POP kontrakt se stejnými vstupními předpoklady. Nová mathematically
silnější globální optimálnost ani hypotetické OS stavy nejsou přidány.


Následné doplnění20: oba distinct očekávané časy jsou nyní plně odvozeny v exercises-1.3.2-020-distinct-recovery.md, oba binární časy v exercises-1.3.2-020-binary-recovery.md. Obě vytištěné formule jsou chybné; C0018 byl rozšířen o první konstantu2υ. Výše uvedené starší otevřené očekávání obou programů je tím vyřešeno; zbývá konkrétní třetí varianta a její srovnatelné náklady.


Konečné doplnění20: exercises-1.3.2-020-third-recovery.md nyní dává úplný obecný MMIX kandidátní program, všechny větve a náklady, exact binary očekávání a rigorózní distinct9×8 srovnání. Třetí metoda je tím konkrétně realizována; v obou modelech má menší oba očekávané koeficienty než Solution2, a ta než Solution1. Úloha20 je argument_recorded; dřívější third-variant partial je vyřešeno. Globální optimum ani historické trial běhy se netvrdí.
