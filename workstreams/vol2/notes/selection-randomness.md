# §3.5 C/D: výběrová pravidla a existence náhodných posloupností

Stav1.11.2026. Původní strany159–167 přečteny vizuálně; odpovědi19,31–34
na594,597–598 a zadání180–183 také. Tento blok uzavírá19,31–34 a matematiku
C/D kromě dopředné konstrukce reálných R6 posloupností v úloze36, která
bude ověřena zvlášť. Celá §3.5 zůstává rozpracovaná. Základní definice
hustoty a k-distribuce jsou v `distribution-foundations.md`, oddíl1.

Známé erratum5.10.2025 na162 opravuje n>=k−1 na n>=k při výběru po
slově délky k; je správné a zapracováno. Známá změna164 je bibliografická.
Nové V2-C0061,62,63 níže jsou doloženy ve třetím vydání/prvním tisku.
Všechny čtyři vrstvy errat a aktuální TeX prohledány podle stran i témat
Wald, W6 a podposloupností; opravy těchto tří míst nenalezeny.
Novější fyzický dotisk, prvenství ani odměna nejsou ověřeny; nic neodesláno.

## 1. Co požadují definice R1–R6

R1 je nekonečná distribuce: všechna pevná konečná okna mají správné
rovnoměrné četnosti. R2 požaduje každou vlastnost, která platí s
pravděpodobností1 při nezávislém rovnoměrném generování. To je nemožné:
pro každé pevné x má náhodná posloupnost s pravděpodobností1 všechny
členy různé od x. Dosazení x=U_0 vyloučí libovolnou konkrétní posloupnost.
Obdobně požadavek četnosti rovné míře pro každou Lebesgueovsky měřitelnou
množinu selže na spočetné množině všech hodnot dané posloupnosti.
Jednotlivé nulové množiny mají nulovou míru; jejich nespočetné sjednocení
není automaticky nulové. Kniha tuto překážku popisuje správně.

R3 požaduje nekonečnou distribuci každé nekonečné podposloupnosti.
Ekvidistribuovaná posloupnost má rostoucí podposloupnost konvergující k1:
postupně vybíráme členy z otevřených intervalů blížících se1. Tato
podposloupnost není ekvidistribuovaná, takže R3 je opět nemožná.

R4 omezuje výběr na algoritmicky vypočitatelnou injektivní posloupnost
indexů. Injektivní znamená bez opakování; indexy nemusí růst. R5 dovoluje
vybírat další člen podle již známé minulosti, ale v původním rostoucím
pořadí pozic. Výběrové pravidlo je posloupnost funkcí f_n, které z n
předchozích symbolů vracejí0 nebo1 podle toho, zda zařadit dosud neviděný
symbol X_n. R5 vyžaduje1-distribuci každého takto určeného nekonečného
výběru. Pro reálná U se požaduje tato vlastnost pro floor(b U_n) ve všech
celých základech b>=2; tak se vyhneme neřešitelným přesným porovnáním
libovolných reálných vstupů. R6 dovoluje i adaptivní změnu pořadí čtených
indexů: další dosud nečtený index závisí na dříve přečtených symbolech;
výsledná posloupnost má splňovat R5.

V textu „explicitní“ interpretujeme v bezprostředním kontextu jako
vypočitatelné algoritmem, ne jako libovolně definovatelné v teorii množin.
Vypočitatelná ekvidistribuovaná reálná posloupnost nemůže splňovat R4 ani
R5: spočtěme U_n s chybou nejvýše1/16 a vybírejme pozice s aproximací
pod1/4. Rozhodnutí je konečné, vybere všechny U_n<3/16 a žádné U_n>=5/16.
Výběr je tedy nekonečný a všechny jeho hodnoty leží v dolní polovině.
Tento argument nepotřebuje rozhodovat rovnost reálného čísla s1/2.

Výběr členu po prvním běhu n hodnot pod1/2 používá pouze minulost.
Časy těchto prvních běhů pro různé n přísně rostou, protože běh n+1
obsahuje běh n o jednu pozici dříve. Žádné opakované pozice zde nevznikají.
V nezávislém modelu čtení nového členu podle minulosti nezmění jeho zákon;
přesný obecný důkaz pro R6 je v oddílu5.

## 2. V2-C0061: počet změněných oken na str.160

Nahradíme-li U_(j^2) nulou, změníme řídkou množinu členů. Závěr, že
nekonečná distribuce zůstává zachována, je správný. Tištěný odhad počtu
změněných k-oken „at most sqrt(n)“ však vynechává vliv jednoho členu
na až k překrývajících se oken.

Přesný příklad: k=2,N=16 a U_0,...,U_16=3/4. Libovolný nekonečně
distribuovaný ocas lze připojit za tento prefix; změna konečného prefixu
nekonečnou distribuci nezničí. Před nulováním čtvercových indexů mají
všechny16 dvojice začínající v0,...,15 oba členy v[1/2,1). Potom tato
podmínka přestane platit pro začátky0,1,3,4,8,9,15: sedm změn místo
nejvýše sqrt(16)=4. I při počítání jen oken celých v prvních16 členech
jde o šest změn, takže nejde o volbu posledního okna.

Obecná bezpečná mez pro N začátků a pevné k je

```
k * (1 + floor(sqrt(N+k-2))).
```

Relevantní čtvercové indexy nepřekročí N+k−2 a každý leží v nejvýše k
oknech. Po dělení N jde mez k0 pro každé pevné k; původní závěr platí.
Stejný argument dokazuje zachování distribuce při libovolné změně na
množině indexů přirozené hustoty0. Draft je v `reports/C0061-sparse-window-count-draft.txt`.

## 3. R4 a úloha19; skládání výběrů a úlohy32–33

Tvrzení na161 o(theta^n mod1) pod libovolnou vypočitatelnou injektivní
posloupností indexů odpovídá větě Niederreiter–Tichy. Primární autorský
článek *Metric theorems on uniform distribution and approximation theory*,
Astérisque147–148 (1987),319–323, má přesně toto tvrzení jako větu1 na319.
[Primární PDF](https://www.numdam.org/item/AST_1987__147-148__319_0.pdf).
Str.319 přečtena vizuálně, text319–323 celý; vlastní důkaz obecné verze
s libovolnými permutovanými exponenty zde neopakujeme. Článek odkazuje
na úplný důkaz1985; přímé DOI1985 nebylo dostupné. Nejde tedy o tvrzení,
že bylo všech sedm původních stran1985 nezávisle zkontrolováno.
Kniha používá jen uvedenou větu a spočetnost algoritmů: sjednocení
spočetně mnoha výjimečných množin míry0 má míru0. Zahrnutí indexu0
může změnit jen jeden člen.

19. Oslabená R4 požaduje při každém takovém výběru jen1-distribuci.
Vezměme U splňující R4 a V_n=U_floor(n/2). Pro libovolné injektivní
vypočitatelné s_i se každý index floor(s_i/2) objeví nejvýše dvakrát.
Rozdělme je na první a druhé výskyty. V každé části jsou indexy různé
a algoritmicky vyčíslitelné; je-li část nekonečná, R4 zajišťuje její
1-distribuci, je-li konečná, limitu neovlivní. Sloučení podle původního
pořadí výběru má správnou četnost podle33. V tedy splňuje oslabenou R4.
Každá dvojice V_2n,V_(2n+1) je však stejná; hustota sousedních rovností
je alespoň1/2, zatímco2-distribuce by podle věty B dávala0. Oslabení je
opravdu slabší. Stačí dokonce U splňující už oslabenou R4, jak uvádí odpověď.

32. Pro dvě vypočitatelná pravidla R,R' lze z konečné původní minulosti
vypočítat vybranou minulost R a na ní rozhodnutí R'. Nový člen vybereme,
jen když ho vybere R a současně jej z dosavadní vybrané minulosti vybere R'.
Tak vzniká totální vypočitatelné složené pravidlo. Každý nekonečný výběr
z R-výběru proto musí mít správné1-četnosti. Samotný R-výběr splňuje R5.
Výběr vždy po daném slově a indukce dokazují k-distribuci pro všechna k:
pokud má slovo délky k četnost b^(−k), objevuje se nekonečněkrát a
četnost každého pokračujícího symbolu je1/b. Součin dá b^(−k−1).
Základ k=0 je pravidlo vybírající vše. V n-té pozici máme n známých
symbolů, takže podmínka n>=k z errata2025 je nutná.

33. Sloučené první N členů obsahují N_r prvků prvního a N_s druhého
výběru, N=N_r+N_s. Když oba výběry jsou nekonečné, jdou oba počty k nekonečnu,
a odchylka od společné hustoty p je váženým průměrem dvou odchylek
jdoucích k0. Konečná část má nulovou asymptotickou váhu. Důkaz platí
pro libovolně nerovnoměrné prokládání, bez předpokladu hustoty indexů.
To je přesně konečné slučování užité ve větáchC aW.

## 4. Lemma T a algoritmus W

Van der Corputova hodnota V_n vznikne obrácením binárních číslic n za
binární tečku. Pro dyadický interval I délky2^(−r), tj. jednu z buněk
[j/2^r,(j+1)/2^r), platí V_n v I právě tehdy, když n patří do jedné
zbytkové třídy modulo2^r. Každý úsek N po sobě jdoucích indexů obsahuje
v této třídě buď floor(N/2^r), nebo ceil(N/2^r) prvků. Chyba počtu
od N/2^r je nejvýše1. Platí to pro začátek0, pro knižní začátek1
v každém pomocném bloku i pro libovolný pevný posun. Tím je lemma T
a přechod přes větu A k ekvidistribuci dokázán.

W při každém kroku čte rozhodnutí pravidel R_1,R_2,... a jde po cestě
v binárním stromu. U uzlu a=(a_1,...,a_t) vede čítač C[a] s kapacitou
c_t=3*4^(t−1). První ještě nezaplněný uzel na cestě zvýší čítač na k
a vydá V_k. Výpočet každého členu skončí: po N dřívějších výstupech
nemůže být zaplněn uzel kapacity větší než N. Každý uzel B[a] tedy vydá
prefix V_1,...,V_C[a]. Není nutné fyzicky inicializovat nekonečný strom;
navštívené uzly stačí uchovávat s implicitním nulovým čítačem.

Pro pevný prefix a délky r označme A[a] výběr pozic se stejnými
rozhodnutími prvních r pravidel. Všechny kromě konečně mnoha jeho výstupů
pocházejí z uzlů v podstromu a. Výjimky mohou pocházet jen z r−1 předků;
jejich počet je nejvýše C_r=4^(r−1)−1. Jestliže se mezi prvními N výstupy
A[a] použil uzel hloubky t>=r, museli být jeho předkové od hloubky r do
t−1 zaplněni. Všechny jejich výstupy patří do A[a]. Proto

```
N >= sum_(j=r)^(t-1) 3*4^(j-1) + 1
   = 4^(t-1) - 4^(r-1) + 1.
```

Počet použitých uzlů podstromu je tedy nejvýše
2^(2−r)*sqrt(N+4^(r−1)). Každý přispívá k chybě četnosti libovolného
pevného dyadického intervalu nejvýše1 podle lemmatu T. Celková chyba
počtu je nejvýše C_r+2^(2−r)*sqrt(N+4^(r−1)), tedy o(N) pro pevné r.
Konečné sloučení A[a] s a_k=1 a libovolně jemné dyadické intervaly pak
dokazují větu W pro každé nekonečné R_k. To je úplný důkaz nezávislý
na nepřesné pomocné hloubkové mezi tištěného důkazu.

### V2-C0063: pomocná hloubková mez na165

Vezměme všechna pravidla stále rovna1, r=q=1 a N=16. Podmínka tištěného
důkazu 4^r<=4^q<N<=4^(q+1) platí. Uzel B[1] vydá první3 hodnoty,
B[1,1] dalších12; od U_15 se používá B[1,1,1]. Člen U_(s_N)=U_16
tedy leží v hloubce3, nikoli v tvrzené hloubce t<=q+1=2. Nejde jen
o výjimku pro malé N: totéž nastává při N=4^(q+1) pro každé q>=1.

Nález se týká tohoto pomocného tvrzení; není protipříkladem k větě W
ani tvrzením, že ostrá závěrečná konstanta2 musí být nepravdivá.
Bezpečná oprava t<=q+2 dává s odpovídajícím započtením konečných výjimek
chybu nejvýše4/sqrt(N)+O_r(1/N), která pro existenční větu zcela stačí.
Předchozí odstavec poskytuje i přesnější obecný odhad bez pomocného q.
Draft: `reports/C0063-wald-depth-bound-draft.txt`.

Seznam všech totálních vypočitatelných pravidel je spočetný, ale nelze
jej efektivně vyjmenovat tak, aby každé získané pravidlo vždy skončilo.
Vyjmenování syntaktických programů je možné; to je jiná otázka.
Proto použití všech pravidel vW dává existenci R5 posloupnosti, nikoli
efektivní generátor takové posloupnosti. Diagonalizace proti případnému
totálnímu vyčíslování booleovských funkcí tento rozdíl dokazuje.
Primitivně rekurzivní pravidla naproti tomu syntakticky vyčíslit lze;
jejich terminace plyne z omezené konstrukce pomocí kompozice a konečné rekurze.

Tvrzení o nespočetně mnoha výstupechW při uzlových posunech V_(k+t_a)
platí. Chyba dyadických počtů zůstává nejvýše1 pro každý uzel.
Každý běh musí navštívit nekonečně mnoho uzlů, protože kapacity jsou
konečné. Při první návštěvě nového uzlu lze nezávisle zvolit t_a=0
nebo1. Dvě větve, které se poprvé rozejdou, mají dosud shodnou historii
a stejný nový uzel, ale různé další V, protože obracení číslic je injektivní.
Tím vzniká injekce všech nekonečných binárních voleb do výstupůW.

## 5. Věta M: téměř každá binární posloupnost splňuje R6

Fixujme algoritmus S pro adaptivní čtení různých indexů a pravidlo R,
které z již čtené posloupnosti vybírá členy. V nezávislých spravedlivých
bitech má událost „existuje r-tý vybraný člen a první r vybraných bitů
je slovo a“ pravděpodobnost nejvýše2^(−r). Proč: při každém novém výběru
jsou index i rozhodnutí o zařazení určeny minulostí. Dosud nečtený bit
je stále nezávislý a spravedlivý. Dvě prodloužení téhož prefixu o0 a1
mají stejné pravděpodobnosti; jejich sjednocení může být jen podmnožinou
události existence předchozího prefixu, protože další výběr může chybět.
Indukce dává(32), včetně možnosti konečného výběru.

Každá taková událost je měřitelná: svědek existence r-tého výběru
používá konečně mnoho čtených bitů; jeho maximální index je konečný.
Jde o spočetné sjednocení konečných bitových válců, tedy množin
s pevně zadaným konečným prefixem, případně jeho konečným podvýběrem.
Nejednoznačné binární expanze dyadických racionálů tvoří nulovou množinu.

Pro r nezávislých bitů je pravděpodobnost odchylky počtu jedniček od r/2
alespoň epsilon*r nejvýše2*exp(−2*epsilon^2*r). Z exponenciální Markovovy
nerovnosti to plyne přes cosh(t/2)<=exp(t^2/8), aplikované zvlášť na oba
ocasy a optimalizované t=4*epsilon. To je silnější než tištěná mez(33)
2*exp(−epsilon^2*r). Součet přes r je konečný; míra výskytu takové
odchylky nekonečněkrát je0. Spočetné sjednocení přes epsilon=1/t,
t>=2, a všechny algoritmy S,R dokazuje M. Tím je existence binárních
R6 posloupností prokázána. Přechod na reálné bloky v úloze36 se tímto
nenahrazuje; bude zkontrolován samostatně.

## 6. V2-C0062 a úloha31: obrácená převaha v počátečních úsecích

Zadání31 požaduje R5 posloupnost, která má v každém neprázdném počátečním
úseku alespoň polovinu členů striktně pod1/2. Odpověď597 doporučujeW
s R_1 vybírajícím vše. W však zvyšuje C z0 na1 před vydáním V_k;
proto U_0=V_1=1/2 a počet hodnot pod1/2 v prvním členu je0. Podmínka
selže už pro n=1.

Ve skutečnosti každý uzlový prefix V_1,...,V_j má právě floor(j/2)
hodnot pod1/2: V_k<1/2 právě pro sudé k. Proto každý prefix celé
výstupní posloupnosti má nejvýše polovinu hodnot pod1/2. Nejde o
nevýznamný náhodný první člen, ale opačný směr přirozené prefixové nerovnosti.

Oprava pro tuto konstrukci: vW6 použít V_(k−1) místo V_k. Každý uzlový
prefix V_0,...,V_(j−1) má ceil(j/2) hodnot pod1/2; součtem přes všechny
uzly dostaneme alespoň n/2 pro každý prefix délky n. Věta W zůstává
platná, protože lemma T dává stejnou chybu1 i pro začátek0. Při použití
všech vypočitatelných pravidel tedy skutečně vznikne požadovaná R5
posloupnost. R_1 vybírající vše lze zachovat, i když opravená převaha
platí bez této zvláštní volby.

Erratum26.12.2002 opravuje jen index U_n na U_j v zadání182, nikoli
odpověď ani W6. V žádné vrstvě nebyla nalezena oprava konstrukce.
Draft: `reports/C0062-wald-prefix-bias-draft.txt`.
Závorka v odpovědi s Villeovým historickým odkazem a spekulací oR6 není
zde vydávána za ověřený stav výzkumu2026; vyžaduje samostatný kontext.

## 7. Úloha34: efektivní nekonečná distribuce

Vyjmenujme efektivně všechny dvojice b>=2 a konečné b-ární slovo w,
včetně prázdného slova. Příslušné pravidlo vybírá U_n právě tehdy,
když předchozí floor(b U) tvoří w; pro prázdné slovo vybere vše.
ProtožeW vydává racionální hodnoty, každé takové rozhodnutí je
konečně vypočitatelné. Neurčené indexy v tištěném unárním kódování
můžeme přiřadit pravidlu vybírajícímu vše; kódy všech přípustných slov
pak poskytují totální efektivní seznam.

Věta W zaručí ekvidistribuci celého výstupu a každého nekonečného výběru
po slově w. Indukce jako v oddílu3 dokáže všechny četnosti slov v každém
základu b. Věta A pak dá nekonečnou distribuci reálných U. To je úplný
důkaz existence efektivního R1 generátoru, bez tvrzení, že splňuje R4/R5.

## 8. Přesné kontroly a další postup

`verify_selection_randomness.py` a `results/selection-randomness.json`
obsahují čtyři dokončené bloky, exit0: přesný protipříkladC61;
129024 dyadických počtů s osmi různými počátky;4096 krokůW v osmi
scénářích včetně adaptivních pravidel a posunu−1;16384 úplných historií
adaptivního čtení12 bitů. Poslední soupis kontroluje rovnost obou
prodloužení a mez2^(−r) pro všechny vzniklé prefixy. U W jsou počty
nezávisle přepočítávány z minulých přiřazení; matematický důkaz pro
libovolná pravidla je v oddílu4. Hloubkový protipříkladC63 má svědky
N=16,64,256,1024,4096. Konečné výpočty nejsou vydávány za důkaz
nekonečné náhodnosti konkrétního konečného výstupu.

Následují úlohy20–21,26–27,29–30,35–44, textE/F a historický rozsah.
Ramshawův report1977 je stažen pro příští blok20–21, zatím nepřečten.
