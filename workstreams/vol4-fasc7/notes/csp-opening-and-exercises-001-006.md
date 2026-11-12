# §7.2.2.3, p. 1–2 a úlohy 1–6 s odpověďmi

6. listopadu 2026. První digitální vydání 2025. Hlavní text file 16–17,
zadání file 128 / p. 113, odpovědi file 173 / p. 158. Sazba file 16–17,
128 a 173 prohlédnuta. Matematika file 17 byla posouzena samostatně;
typografický výpis `oi=oj` v OCR je třeba číst jako originální `oi≠oj`.
Neuzavírají se celé vzdálené stránky úloh/odpovědí, pouze uvedená čísla.

## C-P01. Definice CSP, počet nastavení a úloha 1

Konečné domény D1,…,Dn určují kartézský součin všech přiřazení.
Každá podmínka vybere podmnožinu přiřazení, řešení jsou průniky těchto
podmnožin. Bez podmínek je to celý součin; jeho velikost je součinem
velikostí domén, protože k libovolné volbě prvních i−1 souřadnic je
právě |Di| možností i-té. Pro n=0 je jedna prázdná n-tice; pokud je
některá doména prázdná a n>0, nejsou přiřazení žádná.

V (1) jsou velikosti 2,2,3,2,2, jejich součin je 48. Při přirozeném
abecedním pořadí souřadnic je první BCAED, poslední SLUON. Při spojení
R1 a R3 se musí rovnat hodnota x5. Řádek BAN z R1 připouští jen CON
z R3, tedy BCAON. Řádek BUD připouští COD nebo LED, tedy BCUOD
nebo BLUED. Řádek SIN připouští jen CON, tedy SCION. To jsou všechny
možnosti, protože byly vyčerpány všechny tři řádky R1 a všechny řádky
R3 se správným x5. R2 odmítne obě slova s (x1,x4)=BO a přijme BE
a SO. Výsledkem jsou přesně **BLUED, SCION**.

Tištěný pomocný seznam odpovědi 1 tak souhlasí po známé opravě BCU0D
na BCUOD. Tuto drobnost již výslovně uvádí seznam malých oprav na konci
`errata/originals/err4f7.textxt`, nejde o nález. Ověřeny jsou jak celý
výsledek, tak mezikrok se čtyřmi kandidáty.

## C-P02. SAT→CSP a čtyři tabulky v (3)

Každé Booleanovo ohodnocení je přiřazení z domén {0,1}. Pro každou
klauzuli vezmeme relaci všech n-tic jejích proměnných, které ji splňují.
Konjunkce klauzulí a konjunkce odpovídajících podmínek jsou tím totožné.
Prázdná klauzule dává nepravdivou nullární relaci, tautologie plnou
relaci; opakování proměnné se vyhodnotí jednou konzistentně.

Vlastní tabulky (3) lze ověřit odečtením jediné zakázané n-tice:
`x1∨¬x2` zakazuje 01, `x2∨x3` zakazuje 00, `¬x1∨¬x3` zakazuje 11
a `¬x1∨¬x2∨x3` zakazuje 110. Zbývající vytištěné trojice a sedmice
jsou přesně doplňky. Původní formule je potvrzena i v lokálním
`text/vol4b.txt`, §7.2.2.2–(3), p. 186; nepřevzal se jen její název.

## C-P03. CSP→SAT: všechny tři jmenované kódovací způsoby

Přejmenujme d prvků neprázdné domény na 0,…,d−1. Log kód má
`l=ceil(lg d)` bitů; zakážeme každé bitové číslo ≥d. Pro d=1 stačí
nula bitů s jedinou prázdnou reprezentací. Direct kód má d indikátorů
a přesně jeden z nich je 1: jedna klauzule „aspoň jeden“ a klauzule
`¬xa∨¬xb` pro každé a<b. Order kód má d−1 indikátorů `xj=[x≥j]`,
1≤j<d, s klauzulemi `¬x_(j+1)∨x_j`. Ty přesně vynutí řetězec
jedniček a pak nul, tj. jednu hodnotu x od 0 do d−1. Každé kódování
je po těchto doménových omezeních bijekcí na dovolené hodnoty.

Libovolnou relaci lze vyjádřit zákazem každé n-tice, která v ní není.
V log kódu rovnost x=a určuje všechny bity, v direct kódu je to právě
kladný indikátor xa. V order kódu je rovnost pro vnitřní a určena
`x_a∧¬x_(a+1)`, na krajích jen `¬x_1` nebo `x_(d−1)`; při d=1
jde o prázdnou konjunkci. Negace konjunkce těchto specifikací celé
zakázané n-tice je v každém případě jedna klauzule. Konjunkce všech
takových zákazů je s relací
ekvivalentní, protože žádnou dovolenou n-tici nezakáže a každou
nedovolenou zakáže její vlastní klauzule. Jde o existenční převod,
nikoli tvrzení o úspornosti; explicitní seznam může být exponenciální.
Prázdná doména nebo nepravdivá nullární relace se přeloží na prázdnou
klauzuli. Pro plnou relaci není třeba přidat nic. Tím jsou pokryty
i degenerované případy mimo vzorec log d pro d>0.

## C-P04. XCC→CSP a zpět, včetně neobarvených položek

Primární definice XCC v 4B p. 88 výslovně požaduje, aby každá možnost
obsahovala aspoň jednu primární položku. Dále přiřazuje neobarvenému
sekundárnímu výskytu jedinečnou implicitní barvu, neslučitelnou se
stejnou položkou v jiné možnosti. Oba předpoklady jsou přímo v
`text/vol4b.txt` kolem řádků 8090–8105.

Zaveďme proměnnou xi pro každou primární položku i s doménou možností
obsahujících i. Z řešení XCC získáme xi jako jedinou vybranou možnost
pokrývající i; různé zvolené možnosti nesdílejí primární položku ani
rozdílně zbarvenou sekundární položku, takže všechna párová omezení
v knize platí. Obráceně z řešení CSP vezmeme množinu vybraných možností
{xi}. Každou i pokrývá aspoň xi. Kdyby ji pokrývala další různá vybraná
možnost xj, byly by xi,xj konfliktní přes i. Pokrytí je tedy právě
jednou a stejný párový argument řeší všechny sekundární barvy. Shodné
možnosti xi=xj jsou dovoleny a v množině se zvolí jen jednou.
Protože každá možnost má primární položku, žádná zvolená možnost se
při opačném převodu neztratí. Převody jsou navzájem inverzní.
Prázdná doména xi znamená nepokrytou povinnou položku a správně UNSAT.
Při nulovém počtu primárních položek nejsou žádné možnosti a obě
formulace mají jediné prázdné řešení.

Opačný převod z 4B, odpověď §7.2.2.1–100(c), skutečně přiděluje
primární položku každému omezení Rj a sekundární položku každé
proměnné. Pro každý povolený řádek Rj je jedna možnost: primární Rj
a barvy dotčených proměnných rovné tomuto řádku. Výběr právě jedné
možnosti každého Rj a barevná shoda znamenají přesně splnění všech
relací. Zcela neomezené proměnné se zachovají přidáním tautologické
unární relace xi∈Di; to řeší i prázdnou Di a zachovává celé přiřazení,
nejen rozhodnutí. Nullární pravda má jednu možnost s primární položkou
samotnou, nullární nepravda žádnou. Tím je obecné tvrzení o vzájemné
redukovatelnosti CSP, SAT a XCC doloženo i na okrajích. Tištěná úloha
4 má všechny proměnné pokryté již svými původními omezeními.

## E002(a). Výběr literálu z každé klauzule

Pro každou klauzuli Ci má proměnná ci její literály jako doménu.
Mezi ci,cj zakážeme právě dvojice (a,¬a). Z ohodnocení splňujícího
SAT vybereme libovolný pravdivý literál každé klauzule; takový výběr
nemůže obsahovat opačné literály. Naopak konzistentní výběr určuje
částečné ohodnocení, které všechny vybrané literály učiní pravdivými;
zbývající proměnné doplníme libovolně a všechny klauzule jsou splněné.
To dokazuje ekvisplnitelnost v obou směrech a také nejednoznačnost
počtů. Jedna klauzule se třemi různými proměnnými má 2³−1=7
Booleanových řešení, ale pouze 3 volby literálu, jak říká odpověď.

Přesné „ternární domény“ platí pro obvyklou normalizaci na tři
různé literály v klauzuli. Pro kratší klauzuli má přirozená doména
nejvýše tři prvky; vyžaduje-li se přesně tříprvková, lze opakované
výskyty označit třemi různými štítky se stejným literálovým významem.
Prázdná klauzule se pozná předem jako UNSAT (nebo dá prázdnou doménu
v režimu „nejvýše tři“). Nulový počet klauzulí dává prázdný CSP,
správně splnitelný. Redukce netvrdí zachování počtu všech Booleanových
ohodnocení, a proto ani nepoužité SAT proměnné nevadí.

## E002(b). Všech 21 relací a přesný počet v příkladu R′

Originální R′ v §7.2.2.2–(7), 4B p. 188, má klauzule

```
C1=(1,2,−3)      C2=(2,3,−4)      C3=(3,4,1)
C4=(4,−1,2)     C5=(−1,−2,3)     C6=(−2,−3,4)
C7=(−3,−4,−1).
```

To jsou přesně domény c1,…,c7. Pro každou z binom(7,2)=21 dvojic
je relace `Ci×Cj \ {(a,−a)}`. Dvojice (1,5), (2,6), (3,7) mají
všechny tři literály opačné, proto po třech zákazech zbývá 6 dvojic.
Každá z ostatních 18 dvojic má právě jeden opačný pár, proto zbývá
8 dvojic. Například pro c1,c5 je to
`(1,−2),(1,3),(2,−1),(2,3),(−3,−1),(−3,−2)`;
pro c1,c7 se vynechá jen (1,−1). Tím je ověřen celý pomocný údaj
o počtu i typu všech 21 relací, včetně dvou tištěných příkladů.

SAT řešení lze odvodit bez výčtu. Pokud x1=1 a x2=0, C4 vynutí
x4=1, C2 pak x3=1 a C7 je nesplněná. Pokud x1=x2=1, C5 vynutí
x3=1, C6 x4=1 a C7 je opět nesplněná. Tedy x1=0. Kdyby x4=0,
C3 vynutí x3=1, C1 x2=1 a C6 je nesplněná; tedy x4=1. Nyní
C1 a C2 společně vynutí x2=1. Obě hodnoty x3 skutečně splňují
všech sedm klauzulí, tedy SAT řešení jsou přesně 0101 a 0111.

Při ohodnocení 0101 je počet pravdivých voleb v jednotlivých klauzulích
`(2,1,1,3,1,2,2)`, jejich součin 24. Při 0111 je to
`(1,2,2,3,2,1,1)`, opět 24. Tyto dvě množiny výběrů však mají průnik:
výběry, v nichž není ani 3, ani −3. V nich jsou c1=c2=2,
c3=c6=4, c5=c7=−1 a c4 může být 4,−1 nebo 2, tedy právě 3 výběry.
Každý konzistentní výběr se rozšíří na některé z obou SAT řešení,
proto inkluze–exkluze dává přesně **24+24−3=45** CSP řešení.

Tištěných 48 je tedy chybně i v originální sazbě. Jde ovšem přesně
o **známé erratum z 10. září 2026**, `4f7.158`, odpověď 2(b),
`48→45`, řádky 849–851 plného TeXu. Nejde o nový nález, kartu ani
červené zbarvení. Malý cílený výpočet 3⁷=2187 literálových výběrů
(nice15, jednou) potvrdil 45, oba SAT modely i všechny uvedené párové
počty; obecný argument i přesná hodnota již plynou z výše uvedeného
důkazu. Výstup v `results/exercise-002-exact.json`.

## E002(c,d). Přidané Booleanovy proměnné a všechny nové relace

Přidejme x1,…,xn∈{0,1}. Pro každý ze tří výskytů literálu a v Ci
přidáme mezi ci a x_|a| relaci: pokud ci=a, Booleanova hodnota musí
být pravdivostní hodnotou a; pro ostatní dvě volby ci jsou dovoleny
obě Booleanovy hodnoty. Je to 1+2+2=5 ze 6 možných dvojic.
Na tři výskyty v každé z m normalizovaných klauzulí připadá přesně
3m binárních omezení. Pokud se v krátké klauzuli výskyty opakují,
mohou být některá omezení totožná a postačí nejvýše 3m.

Každé řešení těchto relací vybralo v každé klauzuli jeden pravdivý
literál svého Booleanova ohodnocení, takže SAT je splněn. Každé SAT
řešení naopak dovoluje takový výběr. Přímá omezení mezi ci,cj nejsou
třeba: opačné vybrané literály by vyžadovaly oba různé bity téhož xj.

Pro R′ jsou domény c1,…,c7 přesně ty vypsané v (b), navíc čtyři bity
x1,…,x4. Pro každý řádek Ci a každý jeho ze tří literálů se použije
právě pravidlo předchozího odstavce; tím je všech 21 relací určeno
jednoznačně. Například c1,x1 mají dovolené dvojice
`(1,1),(2,0),(2,1),(−3,0),(−3,1)`, přesně jako odpověď. Zde na rozdíl
od (b) je celkem 48 úplných přiřazení: ke každému ze dvou různých
Booleanových vektorů je 24 výběrů. Tři výběry bez literálu ±3 jsou
dvakrát, avšak jejich hodnoty x3 je rozlišují. Není to rozpor s 45 v (b).

## E003. Každá klauzule vytištěného SAT kódování

Zaveďme indikátory x1B,x1S; x2C,x2L; x3A,x3I,x3U;
x4E,x4O; x5D,x5N. Pro čtyři dvouprvkové domény mají vždy jednu
kladnou klauzuli a jednu zápornou dvojici; pro tříprvkovou doménu
jednu kladnou trojici a tři záporné dvojice. Celkem 12 klauzulí
v odpovědi vyjadřuje přesně jednu hodnotu každé proměnné.

Pro každou z relací R1,R2,R3 zaveďme tři indikátory řádků Rj1,Rj2,Rj3.
Kladná trojice vybere aspoň jeden řádek a každá implikace
`¬Rjt∨x_(i,a)` zaručí příslušnou hodnotu jeho dotčené souřadnice.
Obráceně splňující tuple dovoluje vybrat svůj skutečný řádek.
Samostatné klauzule „nejvýše jeden řádek“ nejsou potřeba: dva různé
řádky téže relace se liší v některé souřadnici, takže by jejich současný
výběr odporoval doménovému one-hot omezení. Všechny vytištěné implikace
R1 a poslední R33 souhlasí s (2); prostřední elipsa má stejnou přesnou
definici pro všechny zbývající řádky. 9 indikátorů řádků přidá 27
klauzulí, tedy výsledná konstrukce má 20 Booleanových proměnných
a 39 klauzulí. Projekce řešení jsou přesně BLUED a SCION, nikoli
neověřený spoleh na správný konečný počet.

## E004. Každá možnost vytištěného XCC kódování

Primární položky jsou R1,R2,R3 a sekundární x1,…,x5. Všech devět
možností je určeno následujícím úplným seznamem barevných tuple:

* R1: (x1,x3,x5)=(B,A,N),(B,U,D),(S,I,N);
* R2: (x1,x4)=(B,E),(S,E),(S,O);
* R3: (x2,x4,x5)=(C,O,D),(C,O,N),(L,E,D).

Každé řešení vybere přesně jeden řádek z každé skupiny a stejné barvy
u všech opakovaných proměnných. Každá z pěti proměnných se v aspoň
jedné skupině vyskytuje, a proto žádná hodnota nezůstane nevyjádřena.
Obě implikace a jednoznačnost převodu jsou tím přímo doloženy:
řešení XCC a původního CSP jsou v bijekci. Výsledek opět tvoří právě
BLUED a SCION podle již dokázané E001.

## C-P05 a E005. Relace, kartézský součin a nullární hranice

k-ární relace je podle definice podmnožina součinu D1×…×Dk.
Při velikostech d1,…,dk má součin q=∏di tuple a každé lze nezávisle
zařadit či nezařadit do relace, tedy existuje 2^q relací. Pro stejné
domény je q=d^k. Pro k=0 jde o prázdný součin {ε} s jedním prvkem,
i když D=∅, tedy existují přesně dvě nullární relace: ∅ a {ε}.
První podmínka v libovolném CSP zničí všechna řešení, druhá nezmění nic.

U k>0 s prázdnou některou doménou je q=0, a tedy jediná relace ∅.
Prázdná a plná podmnožina prázdného součinu pak splývají. Počítací
vzorce odpovědi zůstávají správné; formulace „another is always true“
označuje odlišnou relaci pouze při neprázdném součinu. Tento malý
okrajový rozsah pomocné věty je výslovně vymezen a nepředstírá se
ověření nevyřčeného předpokladu neprázdných domén. Hlavní nullární
otázka je plně uzavřena; doslovná různost dvou obecných relací pro
prázdné domény zůstává evidována jako scope exception, nikoli nález.

Binární/ternární/quaternární/unární označení na p. 2 jsou definice
arit 2/3/4/1. Jediná binární relace A⊆V×V je právě orientovaný graf
(v této množinové konvenci bez rozlišování paralelních kopií oblouku);
smyčky jsou dovoleny. Toto je překlad definice, ne algoritmická věta.

## E006. Domain/range a oddělená historická tvrzení

Je třeba rozlišit doménu celkové funkce h, její kodoménu a obraz.
Pro h:A→B je argumentový obor A a obraz h[A]⊆B; „range“ se v různých
konvencích užívá pro B nebo h[A]. U binární relace R⊆A×B jsou projekce
prvních a druhých souřadnic její relační doména a range. Pro přiřazení
CSP je funkční doménou množina indexů proměnných. Každé Di ale určuje
dovolené hodnoty jedné proměnné, nikoli argumenty této funkce; omezení
je h(i)∈Di. Kodoména může být sjednocení Di, případně jejich označená
disjunktní kopie. Stejný termín tedy pojmenovává dva různé objekty
a nevzniká matematický rozpor. U samotné relace Ri jsou přípustné
hodnoty vstupními argumenty, což také vysvětluje větu odpovědi.

Historická tvrzení o Mackworthovi 1977, Fikesovi 1970 a inspiraci
computer vision nejsou z tohoto pojmového argumentu dokázána. Primární
prameny nebyly rychle otevřeny, jsou explicitní bibliografickou výjimkou.
Stejně se vynechává Cohn 1965 (p.2), Bennaceur 1996, Järvisalo–Niemelä
2004 (odpověď2) a úvodní literární citáty p.1/158. Neomezuje to výše
uvedené vlastní matematické důkazy.
