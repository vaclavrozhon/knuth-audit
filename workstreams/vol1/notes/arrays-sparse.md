# §2.2.6: seznamy a řídké matice

Uzlem řídké matice rozumíme její nenulový prvek. Pole ROW,COL jsou
jeho indexy, VAL jeho hodnota; LEFT ukazuje na předchozí nenulový
sloupec ve stejném řádku a UP na předchozí nenulový řádek ve sloupci.
Řádky i sloupce jsou kruhové seznamy se zvláštní hlavičkou, jejíž
porovnávaný index je záporný. Každý datový uzel se nachází právě v jednom
řádkovém a jednom sloupcovém seznamu. Tato definice zahrnuje prázdné
řádky a sloupce: jejich hlavička ukazuje sama na sebe.

## Výběr osob a inicializace, úlohy 9–12 a 24

9. Algoritmus G prochází modrooké osoby v klesajícím pořadí adres.
Pro každou adresu x posune ostatní ukazatele, dokud jsou větší než x.
Pokud seznam skončí, jeho nulový ukazatel je menší než jakákoli osoba
a dál se nerozvíjí. Po posunu ukazatel buď je x, nebo již nikdy
nedosáhne x: všechny pozdější hodnoty jsou ještě menší. Průnik FEMALE,
BLOND, BLUE a sjednocení A21,A22,A23 je tedy vyhodnocen přesně.
Každý ukazatel projde svůj seznam nejvýše jednou. V G4 je „until“
stejně jako v G2/G3 podmíněný posun: pokud P1<=P6 již platí,
SEX(P1) se nečte. Pro tento výklad svědčí celý slévací invariant.
Prázdné seznamy ani již shodné adresy nemají být násilně posunuty.

10. Pro tento typ dotazu lze udržovat zvláštní seznam pro každou
kombinaci (pohlaví, barva očí, barva vlasů, věk). Vyhledání uvedené
kombinace v adresáři a spojení tří věkových seznamů stojí pouze
konstantu a počet výsledků; osoby nepatřící do výsledku se neprocházejí.
Při změně atributu se osoba přesune do odpovídajícího seznamu.
Adresář lze realizovat i víceúrovňovým stromem klíčů, takže se
nealokuje plný kartézský součin možných atributů. Jde o výměnu
nákladů na údržbu a paměť za rychlost dotazů; obecně není každý druh
indexu nejlepší pro každý dotaz. Citovaný §6.5 je kontrolován zvlášť.

11. Nejvýše 800 datových uzlů po 3 slovech a 400 hlaviček po jednom
slově, dohromady 2800. Program a jeho ostatní proměnné v této částce
nejsou zahrnuty; otázka se ptá na reprezentaci matice.

24. `n` je počet dosud navštívených indexů, `L[0..n-1]` jejich seznam
bez opakování, `V[k]` jejich potenciální pozice v L. Invariant je
`V[L[t]]=t` pro 0<=t<n a obsah A na těchto indexech je platný.
Pokud `0<=V[k]<n` a `L[V[k]]=k`, je k skutečně v inicializovaném
prefixu L, a tedy i A[k] je platné. Náhodný původní obsah V nemůže
vytvořit falešný kladný výsledek, protože celý prefix L obsahuje jen
skutečně navštívené indexy. Při záporném testu přidáme k na konec,
nastavíme V[k], A[k]=0 a zvýšíme n. Před indexováním L je nutné
nejprve otestovat rozsah V[k]. Za předpokladu disjunktních polí a
platného vstupního indexu jde o konstantně mnoho operací.

Pro obnovení původního obsahu A a V uložíme při prvním přístupu
k právě inicializovanému indexu jeho staré A[k],V[k] do dvou polí
paralelních s L. Nakonec projdeme tento prefix L a obnovíme obě
hodnoty. L samo se podle odpovědi obnovovat nemusí. Opakované zápisy
do stejného A[k] nepotřebují další zálohu; n lze poté vrátit na nulu.
Vše je lineární pouze v počtu použitých buněk, nikoli v délce A.

## Pivotování: obecný invariant algoritmu S

Pivot je nenulový prvek na pozici (i0,j0), jeho původní hodnota je a.
Původní prvky v témže řádku označme b_j, v témže sloupci c_i a mimo
ně d_ij. Výsledkem má být 1/a v pivotu, b_j/a v pivotním řádku,
-c_i/a v pivotním sloupci a d_ij-c_i*b_j/a jinde. Počítáme nejprve
v přesné racionální aritmetice, jak hlavní zadání výslovně dovoluje.
Paměť musí stačit na mezilehlé nově vložené uzly; OVERFLOW je řádně
rozlišen od dokončení. Numerická singularita nebo přetečení nejsou
slibem tohoto algoritmu vyřešeny.

S1 zapamatuje ALPHA=1/a ještě před přepsáním pivotu jedničkou.
S2 prochází každý nenulový prvek pivotního řádku právě jednou,
včetně pivotu. Po S2 jsou jejich hodnoty přesně b_j/a a 1/a;
pivotní řádek se později už nemění. PTR[j] je ukazatel do sloupce j,
ze kterého lze hledat předchůdce následujícího zpracovávaného řádku.
Je inicializován na sloupcovou hlavičku pro všechny použité j.

S3 prochází pivotní sloupec odspodu, vynechá i0. Tento sloupec se
nikdy strukturálně nemění, proto jeho původní nenulové řádky projde
právě jednou. Při zpracování řádku i zůstává VAL(Q0)=c_i až do konce
celého řádku. S4 současně prochází neměnný pivotní řádek, vynechá j0
a vybere další nenulový b_j. Pokud b_j nebo c_i původně je nula,
mimo pivotní řádek a sloupec se v dané pozici nic měnit nemá.

S5 udržuje P jako bezprostředního předchůdce P1 v řádku i; všechny
sloupce napravo od aktuálního j jsou již hotové a nebudou navštíveny
znovu. Posuny vynechají prvky se sloupcem větším než j. Při shodě
je P1 hledaný existující prvek. Při menším indexu patří nová pozice
mezi P a P1. Hlavička se záporným COL zaručuje ukončení.

Ve sloupci j ukazuje PTR[j] buď na hlavičku, nebo do již zpracovaného
řádku pod aktuálním i. S6/S8 jej posouvají pouze vzhůru. Pokud prvek
(i,j) není přítomen, S6 skončí před prvním řádkem menším než i;
nový uzel X vloží zároveň do obou seznamů. Dočasná hodnota nula
správně zastupuje původně chybějící d_ij. Žádný další seznam se nemění.

Proto na začátku S7 platí přesně odpověď 12:
`VAL(Q0)=c_i`, `VAL(P0)=b_j/a`, `VAL(P1)=d_ij` (případně 0).
Výpočet S7 dá požadovaný výsledek. Pokud je nenulový, PTR[j] se
nastaví na tento zpracovaný uzel a P pokračuje za ním. Pokud je
nulový, S8 najde jeho sloupcového předchůdce, odpojí uzel v obou
směrech a uvolní jej; P zůstane na vodorovném předchůdci. PTR[j]
potom stále smí sloužit dalšímu, výše ležícímu řádku. S8 tedy
neuvolní žádný ukazatel, který by bylo potřeba později dereferencovat.
Po průchodu řádku se změní i jeho pivotní prvek na -c_i/a.

Ukončení plyne z konečnosti seznamů a striktního poklesu zpracovávaných
řádkových a sloupcových indexů. Nové uzly se vkládají pouze na právě
zpracovávané pozice, takže nemohou vytvořit nový cyklus práce.
Invariant současně dokazuje správnost všech hodnot, zachování
pořadí obou seznamů i jejich shody o množině uzlů. Příklad (12) dává
přesně matici (14), včetně odstranění (4,3) a vložení (1,3).

13. Lineární varianta nahrazuje návrat na hlavičku nulovým ukazatelem.
Před čtením COL/ROW pak explicitně testuje null, jak uvádí odpověď;
po skončení pivotního řádku vrátí P0 na jeho hlavičku. V S8 není
potřeba nový null test: existující odstraňovaný uzel je v daném
sloupci a jeho předchůdce musí být nalezen dříve než konec. Zbývající
invariant je týž. Úspora ztraceného pole v hlavičce u MIX nezkrátí
jednoslovný uzel; složitější větvení tedy nepřináší paměťový zisk.

14. V hustě uložené matici vytvoříme LINK jako seznam sloupců s
nenulovým prvkem v pivotním řádku. Pro každý řádek s c_i!=0 pak
zpracujeme jen tyto j, pivotní sloupec až nakonec; samotný pivotní
řádek zpracujeme jednou předem. Totožné rovnice dokazují správnost,
i když fyzicky zůstávají všechny nulové buňky přítomné.

## Kopie, násobení a inverze, úlohy 16–19

16. Inicializujeme nové řádkové i sloupcové hlavičky. Původní řádky
procházíme odshora dolů; v každém jdeme od pravého prvku doleva.
Pro každý prvek vytvoříme nový uzel se stejnými ROW,COL,VAL a připojíme
jej za dosavadní konec právě budovaného řádku. Současně jej vložíme
na začátek jeho nového sloupce. Protože řádky zpracováváme vzestupně,
sloupce tak budou mít požadované sestupné pořadí ROW. Řádek na konci
uzavřeme odkazem na vlastní hlavičku. Žádné odkazy nesměřují do staré
matice. Čas je O(m+n+z), kde z je počet nenulových prvků.

17. Každý nenulový A[i,k] vynásobí celý řádek k matice B a ten
přičteme sléváním ke vznikajícímu řádku i matice C. Při shodných
sloupcích se koeficienty sečtou, nulový výsledek se vyřadí. Indukce
podle počtu použitých k dává `C[i,j]=sum_k A[i,k]B[k,j]`, bez
předpokladu kladnosti koeficientů. Při stavbě stačí řádkové LEFT
odkazy; sloupce UP vytvoříme jedním následným průchodem řádky odshora
dolů, vkládáním na začátek sloupce. Název „COL links“ v odpovědi
popisuje seznam řazený podle COL, nikoli nové pole struktury (11).
Algoritmus je správný, ale obecně není tvrzen jako asymptoticky nejlepší.

18. Ruční pivoty do sloupců 3,1,2 dávají postupně

```
 1/3  2/3  1/3       1/2  1/2  0       0  1  0
-2/3 -1/3 -2/3  ->  -3/2  1/2  1  ->  -2  1  1
-1/3 -2/3 -1/3      -1/2 -1/2  0       1 -2  0.
```

Po předepsaném přečíslování vyjde `(1,-2,1; 0,1,-2; 0,0,1)`.
Součin s původní horní trojúhelníkovou maticí je jednotková matice
na obou stranách. Rovnosti nejsou založeny na zaokrouhlených číslech.

Pro obecnou správnost definujme E_k jako elementární matici, která
při k-tém pivotu dělí řádek k číslem a a od každého jiného řádku i
odečte c_i/a násobek původního řádku k. Mimo pivotní sloupec je
S právě násobení zleva E_k; nový pivotní sloupec je E_k e_k,
kde e_k je k-tý sloupec jednotkové matice. Součin dřívějších E_j
pro j<k ponechává e_k beze změny, protože každé E_j se od jednotkové
matice liší pouze ve sloupci j. Proto jsou již pivotované sloupce
v pracovní matici vždy `E_k...E_1 e_j`, nepivotované pak
`E_k...E_1 A[:,l]`.

Současně transformované původní pivotní sloupce jsou e_1,...,e_k;
pozdější E je již nemění. Je-li C[k] sloupec zvolený v řádku k,
a P permutační matice s `P[k,C[k]]=1`, po posledním pivotu platí
`E_n...E_1 A=P` a pracovní matice je `B=E_n...E_1 P=P A^(-1) P`.
Přesun starého řádku k na C[k] a starého sloupce C[k] na k je
`P^T B P^T=A^(-1)`, přesně jak stanoví zadání. Jestliže žádný
nepoužitý sloupec v řádku k nemá nenulový prvek, transformovaná
původní matice má nulový řádek k, takže je singulární; jinak je
E_k invertibilní. To také dokazuje oprávněnost singularitního testu.

19. Použijeme S pro každý z n zvolených pivotů a uchováme C a jeho
inverzní permutaci D. Výběr maxima jde průchodem daného řídkého
řádku s testem, zda sloupec již byl použit. Závěrem u každého uzlu
přejmenujeme `ROW <- C[ROW]`, `COL <- D[COL]`. Pouhé přejmenování
by nezachovalo pořadí seznamů, proto je nutno je obnovit.

Lze to udělat bez porovnávacího třídění a bez mapy starých adres:
1. Projdeme ještě staré řádky; před změnou odkazů si vždy zapamatujeme
   následující LEFT. Pomocí UP rozdělíme přejmenované uzly do košů
   podle nového COL, s použitím sloupcových hlaviček.
2. Vyprázdníme řádkové hlavičky. Pro sloupce j=1,...,n projdeme
   příslušný koš a každý uzel vložíme na začátek jeho nového řádku.
   Vzniknou sestupné LEFT seznamy. Jejich odkazy nekazí UP košů.
3. Vyprázdníme sloupcové hlavičky. Pro řádky i=1,...,n projdeme
   hotové řádky a každý uzel vložíme na začátek svého sloupce.
   Vzniknou sestupné UP seznamy a LEFT zůstává beze změny.

Celá přestavba stojí O(n+z) a nezvětší počet datových uzlů. Pomocná
paměť je O(n) pro permutace a použité sloupce; koše využívají stávající
hlavičky. Funguje i pro prázdné řádky a sloupce, třebaže inverze
regulární matice je mít nemůže. Zvláštní fyzický přesun hodnot není nutný.
