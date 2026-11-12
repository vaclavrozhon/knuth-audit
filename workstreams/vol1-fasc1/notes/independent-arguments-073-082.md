# MMIX — interpret, argumenty p. 73–82

**V0141, p. 73 — pojem interpretu a historie, partial bibliografie.**
Vymezení „machine-like“ je výslovně neostrá definice; není tvrzena věta
s nutnými a postačujícími podmínkami. Změna hostitelského stroje vyžaduje
převést interpret a jeho závislé rozhraní; virtuální program při zachování
stejné sémantiky zůstane stejný. Historické priority prvních interpretů
a obecná tvrzení o jejich rozšíření nebyly doloženy primárními statistikami.

**V0142, p. 74 — tabulka ad hoc programů.** Deset možností levého
operandu a deset pravého dává 10²=100 uspořádaných případů. Jednobajtový
kód má 256 možných operací a octabyte pojme osm instrukcí; je tedy
možné použít tabulku 100 krátkých slov, pokud jednotlivé programy mají
nejvýše osm takových instrukcí. „Ideally“ v textu je podmíněný návrh,
nikoli obecný důkaz této meze pro jakýkoli jazyk či aritmetiku.

**V0143, p. 74–75 — příklady DVI a bibliografie, partial.** Popisuje se
řetězec zdroj→TeX/DVI→dvips/PostScript→tiskový interpret. Zachování
významu takové kompozice plyne ze správnosti každého převodu, kterou
však tato kapitola neimplementuje. Nezískány nové úplné zdroje CACM 6
(1963),555–563; Randell–Russell 1964; Evans 1964,87–124; TeX: The Program,
část 31/§545; PostScript Language Reference 1999. Datace D. R. Fuchs
1979, konkrétní výrobní workflow této knihy a osobní pětinásobné
zrychlení autora nejsou vydávány za nezávisle ověřené údaje.

**V0144, p. 76 — rozsah a hodiny, partial původního benchmarku.**
Simulátor výslovně ignoruje pipeline/cache/virtual translation a odmítá
privilegované instrukce. Proto nemá dokládat celé skutečné MMIX OS.
Číselné kódování `2^32 μ+υ` dává pro vypsaný příklad high #3228=12840,
low #bb091=766097. To ověřuje převod, nikoli dříve přeskočený počet
instrukcí Programu P. U dlouhého běhu se nízká část může přenést do
vysoké; clock je jedna číselná lineární kombinace, ne dvě neomezená
samostatná počitadla. První 32 pozic Global stačí na special registers,
protože G≥32; nedochází k překrytí s dostupnými globals.

**V0145, p. 77 — rozložení.** Global má 256*8=2048 bajtů, Local při
ρ=256 dalších 2048 a IOArgs dva octabytes. Chunk0 je tedy na
Data_Segment+4112; žádné z těchto polí se nepřekrývá. Samotných 2^64
bajtů nelze injektivně uložit do 2^61 bajtů bez dalšího předpokladu o
obsazenosti; simulátor ukládá pouze přístupné chunky a čerstvé považuje
za nuly. Fyzická kapacita tak závisí na počtu různých chunků.

**V0146, p. 77 — rozklad adresy.** Pro Chunk=2^12 je jednoznačně
`A=key+offset`, key=A & ~4095, offset=A & 4095. Key obsahuje horních
52 bitů a offset spodních 12. Node má KEY 8, LINK 8, DATA 4096 a padding
8 bajtů, celkem 4120. DATA i node jsou zarovnány na 8; zaokrouhlení
výsledné adresy R dolů na octabyte odpovídá stejnému zaokrouhlení A.
Proto M8[A] nikdy nepřekročí hranici DATA při jeho platném zarovnání.

**V0147, p. 78 — MemFind funkční invariant.** Při vstupu obsahuje
list každý dosud založený key právě jednou; head je poslední nalezený
a curkey=KEY(head). Shoda key tedy dovolí okamžitý návrat. Při neshodě
začne search až druhým uzlem. p vždy míří na předchůdce head; neúspěch
postoupí po LINK, úspěch nebo čerstvý alloc skončí na 3H. Čerstvý node
má KEY nově zapsaný a ostatní pole nulová z dosud nepoužité paměti.

Při přesunu nalezeného M s předchůdcem P a následníkem N se provede
M.LINK=old_head a P.LINK=N, head=M. Tím vznikne přesně move-to-front,
bez ztráty nebo zdvojení jiného uzlu. U nové položky je N=0 a P starý
poslední uzel, tedy stejná úprava funguje. tail vrátí head+16+offset;
PUSHJ/POP předává výsledek v $0. Platí do vyčerpání dostupné nulové
paměti; konkrétní výhrada ke kapacitě je v úlohách a C0010.

**V0148, p. 78 — odmítnutí záporných adres.** Zpočátku curkey=0.
Každý nový ne-head key s high bitem 1 musí projít BN addr,Error před
vložením do seznamu. Indukčně tedy žádný takový key není cached a
rychlá větev PBZ nemůže kontrolu záporné adresy obejít. Instrukce 032
se provede ještě před zápisem newlink do $3; při jejím Error má MemFind
přesně lokály $0,$1. Počty rámců řeší potvrzený C0013.

**V0149, p. 79 — kruhové přeznačení.** Logická položka na pozici O+k
leží v l[(O+k) mod ρ]. Po schování X+1 položek se O zvýší o X+1:
nové $k je fyzicky staré $(k+X+1). POP vrátí O a tím původní indexy.
ρ je mocnina dvou, takže modulo je bitová maska; ρ≥256 pojme všech
nejvýše 255 lokálních registrů a jednu přechodovou položku.

**V0150, p. 79 — intervalový invariant ringu.** V octabyte jednotkách
je cached souvislý interval [S,O+L), kde [S,O) je pushed a [O,O+L)
jsou current locals. Je-li jeho délka menší než ρ, zobrazení modulo ρ
je na tomto intervalu prosté a zbytek ringu volný. Proto α=O modρ,
β=(O+L) modρ a γ=S modρ dávají přesně tři oblouky obrázku. rO/rS
obsahují byteové adresy, tedy rovnice (3) vyžadují dělení 8.
Zvětšení S o jednu položku po store převádí nejstarší cached položku
do paměti; snížení S a load ji z paměti opět připojí. StackStore běžně
vyžaduje γ≠α, aby neodstranil current local, a StackLoad volné místo.
Transientní úplný ring při L=256 je zvláštní případ V0153.

**V0151, p. 80 — GetReg.** Vstup je k*8. Pro k≥G se čte g+k*8.
Jinak se vypočte `(8k+rO)&(8ρ−1)`, tedy přesně slot local register.
CMP před přičtením uchová informaci k<L; CSNN vrátí 0 právě při
marginal k≥L. Čtení libovolného starého obsahu ringu pro marginal
je bezpečné v přiděleném fyzickém poli a následně se zahodí. Funkce je
správná pro všech 256 k. Časová formulace má potvrzenou chybu C0012:
obě nonglobal větve stojí μ+12υ, global μ+6υ.

**V0152, p. 80–81 — StackStore a StackLoad.** Store uloží l[S modρ]
na virtuální adresu rS přes MemFind a zvýší rS o 8. Load nejprve sníží
rS o 8, načte tentýž octabyte a zapíše do l[S modρ]. Jde o navzájem
opačné přesuny hranice cached intervalu, pokud je slot při loadu volný.
Skutečné $0 uchová skutečné rJ a $1 uchová přenášenou hodnotu;
PUSHJ res=$2 chrání oba před MemFind. Simulated rJ je naproti tomu
v Global[4], takže se tyto dva návratové mechanismy nezaměňují.

**V0153, p. 81 — StackRoom a výjimka L=256.** Testuje
`(rS−rO−8L)&(8ρ−1)`, což je nula právě když β=γ. Je-li po růstu
ring plný a L≤255<ρ, obsahuje nejméně jednu pushed položku, tedy
γ≠α a store ji může bezpečně odložit. Pro ρ=256 může global PUSH
nebo SAVE přechodně přidat marker a vytvořit L=256, α=β=γ. Nejstarší
current local se tehdy uloží do paměti, ale bezprostředně potom jsou
všechny lokály pushed a L=0; hodnota zůstává dostupná pro pozdější load.
To je přesná výjimka, kterou uvádí odpověď §1.4.3′–3, nikoli obecný
zákaz takového stavu. Čerstvý dest před voláním StackRoom nesmí dále
narůst bez uvolnění slotu; kód ho volá po každém přírůstku.

**V0154, p. 81 — Fetch.** Normální větev zachová původní inst_ptr
jako loc, načte M4[loc] přes MemFind a zvýší inst_ptr o 4. Vložená
RESUME instrukce naopak použije pravou tetrabyte g[rX] (offset +4),
přiřadí jí logickou pozici inst_ptr−4 a následující adresu nezmění.
CMPU s g=Data_Segment odmítne všechny loc mimo text, včetně záporných
unsigned hodnot. Drobné bity adres respektují obecné zarovnání LDTU;
není potřebný jejich přenos do samotných bitů načtené instrukce.

**V0155, p. 82 — rozbalení polí.** inst je zero-extended tetrabyte
OP X Y Z. MOR s #8,#4,#2,#1 vybere z jeho čtyř nenulových byteových
pozic postupně OP,X,Y,Z do nejnižšího bajtu; jiné bajty výsledku jsou 0.
ANDN s −#10000 ponechá spodních 16 bitů YZ. SLU xx,3 a op,3 násobí
byteové hodnoty osmi bez přetečení. Vstupy x,y,z a exc jsou nulovány
pro každý nový cyklus, takže absent operand nepřebírá předchozí hodnotu.

**V0156, p. 82 — tabulka Info a oddělené special registers.** Osmibajtové
položky pro 256 opcodes zabírají 2048 bajtů od #1000 do #17ff, takže
Done=#1800. Flag bity #1,#2,#4,#8,#10,#20,#40,#80 jsou disjunktní;
jednotlivé testy nezávisle identifikují příslušný zdroj/cíl/address/memory
atribut. Všech 256 konkrétních položek se tím ještě nepovažuje za
ověřené; budou přiřazeny ke skupinám instrukcí v následujícím bloku.
Sedm oddělených ss,oo,ll,gg,aa,ii,uu jsou právě uvedené simulated
special registers; cc je další vlastní clock simulátoru, nikoli osmý
z těchto architektonických registrů.

Konkrétní nové analýzy jsou v C0009/C0012/C0013; C0003 byl uzavřen
samostatnou krátkou kontrolou primárního MMIXware zdroje. Žádný program
ani starý census nebyl kvůli tomuto bloku spuštěn.
