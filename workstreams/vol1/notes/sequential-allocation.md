# §2.2.2: sekvenční ukládání, stav rozpracované kontroly

> Aktualizace5.11.2026: souvislá revize a aktuální pramenné výjimky jsou v [novém zápisu](sequential-allocation-2026-11-05.md). Starší stav otevřených kroků níže je historický; úloha13 je nyní uzavřena, C0035 zůstává otevřený.


Kontrolovaný zdroj je první dotisk třetího vydání (1997). Tištěné strany
244–254 odpovídají souborovým259–269; odpovědi540–545 souborovým555–560.
Inventář potvrzen:19 původních cvičení. Originality obrázků jsou v
`images/vol1-file*-p*.png`. OCR slouží pouze k vyhledávání.

## 1. Rozhraní a základní invarianty

Kapacita M znamená počet slov společné paměti. U jednoho zásobníku T
udává počet uložených prvků; platné položky jsou X[1] až X[T]. Vložení
zvýší T a zapíše nový vrchol, odstranění čte původní vrchol a sníží T.
Kontroly T=0 a T>M přesně rozlišují podtečení a přeplnění. Stav po
neobslouženém OVERFLOW se nepovažuje za platný stav pro další operace.

Kruhová fronta má ukazatel F na pozici bezprostředně před prvním prvkem
 a R na poslední prvek. Oba ukazatele jsou v1..M. Počet prvků je
(R−F) mod M; rovnost ukazatelů označuje prázdnost, a proto lze uložit
nejvýše M−1 prvků (§2.2.2-1). Předpoklad M>1 byl do textu přidán
2.května2024. Operace na opačných koncích (§2.2.2-2) mají přesně tištěný
směr změn: odstranění vzadu čte X[R] a sníží R cyklicky; vložení vpředu
zapíše X[F] a sníží F cyklicky. Totéž pořadí zachovává invariant fronty.
Příslušné nula-originové operace (§2.2.2-19) mají F na prvním prvku a R
na první volné pozici. Vysvětluje to oba posuny pořadí čtení/zápisu a
změn ukazatelů, nikoli jen mechanické nahrazení čísel.

Dva zásobníky s pevnými dny mohou růst proti sobě a využijí všech M
slov. Pro tři pevná dna již nějaký interval leží mezi dvěma dny; vhodnou
volbou zásobníku, do něhož se vkládá, jej zaplníme, zatímco za jiným dnem
je volno. Bez přesunů či změny reprezentace tudíž totéž není možné.
Obdobná záruka pro fronty (§2.2.2-16) selže: odstranění vytváří volné
pozice u čela, zatímco další vložení potřebuje pozici u opačného konce.
Kruhové obtékání v celém společném prostoru by narušilo druhý seznam;
pevná hranice kruhové oblasti by naopak zablokovala využití jeho volna.
Tvrzení se týká daného sekvenčního ukládání bez přesunů, nikoli všech
možných datových struktur.

Pro n zásobníků definujeme b_j=BASE[j], t_j=TOP[j] a velikost s_j=t_j−b_j.
Platný obsah j leží v (b_j,t_j], kapacita j je b_(j+1)−b_j, b_1=L0,
b_(n+1)=L∞. Základní invariant je b_j≤t_j≤b_(j+1). Při volání obsluhy
přeplnění je t_i již zvýšeno o1, ale nový prvek ještě není zapsán.

Jednoduchý přesun nejprve vyhledá nejbližší volné místo napravo.
Mezilehlé zásobníky jsou těsně zaplněné, takže posunutý souvislý blok
obsahuje právě jejich platná data. Kopíruje se zprava doleva. Není-li
volno napravo, hledá se nejbližší volno nalevo a kopíruje se zleva doprava.
Horní mez druhého kopírování musí být **L<t_i**, protože t_i je dočasně
zvýšené; známá oprava6.ledna2011 přesně tento problém řeší. Posun b_j a
t_j o stejnou jednotku zachová velikost i obsah. Nenajde-li se volno ani
na jedné straně, součet skutečných velikostí je M a vložení není možné.

## 2. Algoritmy G a R

G přiděluje volno podle kombinace rovnoměrného podílu a nedávného růstu.
Po dočasném započtení nového prvku označme N=sum s_j, S=M−N,
D_j=max(t_j−OLDTOP[j],0), I=sum D_j. BASE se od posledního přebalení
nezměnilo. Přetečení zásobníku i proto znamená

t_i > b_(i+1) >= OLDTOP[i].

Tedy D_i>0 a I>0: dělení vG4 je definováno (§2.2.2-7). Je-li S<0,
paměť nestačí. Jinak nechť a=S/(10n), beta=9S/(10I). Ideální podíl
volna zásobníku j je q_j=a+beta D_j. Je nezáporný a sum q_j=S.
G5 používá rozdíly celých částí kumulativních součtů q_j. Příděly jsou
nezáporná celá čísla, jejich součet včetně posledního zbytku je přesně S,
a každý příděl je alespoň floor(a). Vlastní model používá přesné zlomky;
praktická plovoucí implementace musí uhlídat celkové celočíselné meze.

G6 před skutečným kopírováním odvolá dočasné zvýšení t_i, takže nekopíruje
nezapsané slovo cizího zásobníku. Po R je obnoví a OLDTOP uloží už nové
fyzické adresy. Tabulky OLDTOP[j],D[j],NEWBASE[j+1] mohou sdílet buňku:
G2 přepíše OLDTOP až po čtení; vG5 je D[j] naposledy přečteno těsně před
zápisem NEWBASE[j+1].

R nejprve kopíruje zásobníky posouvané dolů ve vzrůstajícím pořadí j,
potom zásobníky posouvané nahoru v klesajícím pořadí. Uvnitř zásobníku
volí shodný směr kopírování jako změna adresy. Zde je obecný důvod,
proč nepřepíše živá data. Při kopírování dolů je pravý konec cíle menší
než starý pravý konec, proto neleze do ještě nepřesunutých pravých
zásobníků. Levé zásobníky již mají konečné adresy, jsou-li také
posouvané dolů; ostatní mají starý pravý konec nejvýše svůj konečný
pravý konec. V obou případech končí před novým dnem právě přesouvaného
zásobníku. Pro fázi nahoru platí zrcadlový argument; zásobníky už
přesunuté dolů jsou v cílových disjunktních intervalech. Prázdný
zásobník nevyvolá žádné kopírování. Zásobník1 nikdy měnit dno nemusí.
Tištěná tautologická podmínka vR4 je známá chyba opravená6.března1998:
NEWBASE[j]>BASE[j].

## 3. Průměrný počet přesunů (§2.2.2-9–12)

Zde se pouze vkládá, počáteční kapacita je celá u zásobníku n. Pro
posloupnost a_1,...,a_m se každý dříve vložený prvek v zásobníku a_j
posune právě při pozdějším vložení do menšího zásobníku a_k<a_j.
Počet přesunů je tedy počet dvojic j<k s a_j>a_k. Taková dvojice se
nazývá inverze. Pro rovnoměrné nezávislé volby je pravděpodobnost
inverze (n−1)/(2n), a střední počet je

E = binom(m,2)(n−1)/(2n) = (n−1)m(m−1)/(4n).              (1)

Pro pravděpodobnosti p_i je odpovídající vzorec

E = binom(m,2) sum_(i<j) p_i p_j
  = binom(m,2) (1−sum_i p_i²)/2.                        (2)

Nezávisí na vzájemném pořadí seznamů. Tištěná mez i≤j je známá chyba
opravená10.září2008; zahrnutí diagonály by započítávalo neexistující
přesuny uvnitř téhož zásobníku.

Ve cvičení11 se prvních t vložení do každého zásobníku účtuje zdarma.
Pro pozici k a dřívější pozici j<k se přesun účtuje právě tehdy, když
a_j>a_k a mezi zbývajícími k−2 pozicemi před k je nejméně t výskytů a_k.
Volba hodnot a_j>a_k má n(n−1)/2 možností. Sečtením přes k a j dostáváme
přímo první opravený vzorec ze4.října2005:

E_mnt = n(n−1)/(2 n^m) * sum_(k=2..m) (k−1)n^(m−k)
           *sum_(r=t..k−2) binom(k−2,r)(n−1)^(k−2−r).              (3a)

Definujme f(k)=max(binom(k,2)−binom(t+1,2),0). Pro K~Bin(m,1/n)
platí alternativní tvar

E_mnt = n(n−1)/2 * E f(K)
       = n(n−1)/(2 n^m) * sum_(k>t) binom(m,k)(n−1)^(m−k)
                              *(binom(k,2)−binom(t+1,2)).           (3b)

Pro důkaz shody stačí rozdíl po přidání poslední pozice:
f(k+1)−f(k)=k*[k>t]. Binomická identita pak dává z(3b)
E_m−E_(m−1)=(n−1)(m−1)/(2n)*P(Bin(m−2,1/n)≥t), právě poslední člen
(3a). Oba počáteční členy jsou0. Toto dokazuje rovnost pro všechna m,
nikoli jen pro konečné kontrolované případy.

Formální generující funkce F(u)=sum_k f(k)u^k splňuje
F(u)=u^(t+2)((t+1)−t*u)/(1−u)^3. Z binomické transformace tedy plyne

sum_m E_mnt z^m = (n−1)z/(2n(1−z)^3)
                  *(z/(n−(n−1)z))^(t+1)
                  *(z+n(t+1)(1−z)).                              (3c)

To je přesně opravená generující funkce. Pro n=1 jsou všechny hodnoty0;
pro m=0,1 rovněž. Uvedený model je aproximací pevné počáteční kapacity,
nikoli totožným procesem: stejně to výslovně říká zadání.

Pro dva zásobníky je K~Bin(m,1/2) počet vložení do prvního a
max(K,m−K)=m/2+|K−m/2|. Párování členů K a m−K a identita
k binom(m,k)=m binom(m−1,k−1) dávají teleskopicky pro m≥1

E max = m/2 + m*binom(m−1,floor(m/2))/2^m.              (4)

Výsledek souhlasí s tištěným konečným vzorcem i s novým jednodušším
odvozením20.září2024. Stirlingův vzorec v obou paritách dává
m/2+sqrt(m/(2*pi))+O(m^(−1/2)). Pro m=0 je maximum0 přímo.

## 4. Úloha14: maximum multinomických četností

K_i je počet výskytů hodnoty i mezi m nezávislými rovnoměrnými volbami
z1..n; n je pevné. Položme X_i=(K_i−m/n)/sqrt(m). Oprava prvního řádku
odpovědi14 z18.11.1999 je nutná: střed je m/n a měřítko sqrt(m).
Pro nezávislé standardní normální veličiny Z_i a jejich průměr Zbar
má limitní vektor podobu G_i=(Z_i−Zbar)/sqrt(n). Jeho kovarianční
matice má diagonálu(n−1)/n² a mimodiagonální prvky−1/n², přesně jako X.

Zde potřebujeme také chybový člen O(1), nikoli jen slabou konvergenci.
Zapišme multinomickou hmotnost pomocí Stirlingova vzorce v oblasti
||X||≤m^(1/12). Taylorův rozvoj logaritmu kolem m/n dává gaussovskou
hustotu na nadrovině sum X_i=0, násobenou krokem m^(-(n−1)/2), s
bodovou chybou nejvýše

C_n*m^(−1/2)*(1+||X||^3)*exp(−c_n'||X||²)

v jednotkách této mřížkové hmotnosti. Taylorův zbytek je v dané oblasti
omezený a lze jej pohltit mírně širší gaussovskou funkcí; konstanty
zde závisí jen na pevném n. Mimo oblast má multinomické i normální
rozdělení exponenciálně malý ocas podle binomických Chernoffových mezí.
Po vynásobení max_i X_i a sečtení je tedy chyba O(m^(−1/2)). Riemannův
součet pro kusově hladkou funkci max_i x_i krát gaussovská hustota
má rovněž chybu O(m^(−1/2)): na buňkách využijeme Lipschitzovu mez pro
maximum a integrabilitu hustoty i jejích derivací. Proto

E max K_i = m/n + c_n*sqrt(m) + O(1),
c_n = E max G_i = E max Z_i / sqrt(n).                            (5)

Tím je doplněna přesná rychlost, kterou samotné tvrzení o přiblížení
Riemannova součtu do libovolného epsilon ještě neposkytuje.

Nechť phi je standardní normální hustota a Phi její distribuční
funkce. Integrace po částech dává

E max Z_i = n(n−1) integral phi(z)^2 Phi(z)^(n−2) dz.

Protože phi² je1/(2sqrt(pi)) krát hustota N(0,1/2), dostáváme
c_n=(n−1)sqrt(n)/(2sqrt(pi))*a_n, kde a_n je pravděpodobnost, že n−2
standardních normálních veličin jsou všechny nejvýše nezávislé
W~N(0,1/2). Rozdíly W−Z_i mají vzájemnou korelaci1/3. Pro n=2 a3
je a_2=1, a_3=1/2. Pro dvě souřadnice dává kruhová symetrie
P(U>0,V>0)=1/4+arcsin(rho)/(2*pi); pro tři souřadnice symetrie
znamének a rozvoj součinu(1+sgn U_i)/2 dává1/8+sum arcsin(rho_ij)/(4*pi).
Dosazením rho=1/3 tedy

a_4 = atan(sqrt(2))/pi,
a_5 = 1/8+3/(4*pi)*atan(1/sqrt(8)).                                (6)

To souhlasí s oběma netriviálními konstantami tištěné odpovědi.
Samostatně byl přezkoušen její převod y→x: determinant je1/n a x_1
přidává další faktor1/n. Proto I1=I2/n², jak opravují errata18.11.1999.
Další mez3≤j≤n a faktor m^((1−n)/2) jsou další známé tiskové opravy.

## 5. Úloha18: účetní odhad po prvním přebalení

Správná tištěná podmínka je M≥n² (OCR přečetlo >) a ratingM30.
Po přebalení je N obsazených a S=M−N volných buněk. Každý zásobník
má alespoň floor(S/(10n)) volných pozic. Pokud do dalšího přebalení
proběhne p vložení a q odebrání, pak p>S/(10n), protože i samotný
přetékající zásobník musí překonat svou celou počáteční rezervu.
Má-li vložení základní cenu a a přebalení cenu nejvýše bN'+cn,
platí N'≤N+p. Každému z p vložení účtujme

a+b+10c+10(b+c)nN/S.

Přebytek účtu nad pa+qd je větší než
pb+cS/n+(b+c)N ≥ pb+bN+cn,
protože S/n+N=M/n+N(1−1/n)≥n. Tím zaplatí skutečné přebalení.
Součet účtů dává požadovaný tvar **pro intervaly po prvním přebalení**.
S=0 znamená plnou paměť a nekonečný pravý odhad je pouze prázdnou mezí.

Počáteční interval se samostatně prověřuje: inicializace(11) nedává
u všech zásobníků minimální rezervu. Jediné první vložení do zásobníku1
může spustit smyčkyG/R délky n, zatímco všechny předchozí alpha jsou0.
To je otevřený kandidát na chybějící počátečníO(n) člen či předpoklad
počátečního rovnoměrného rozdělení; dosavadní důkaz jej nepokrývá.

## 6. Úloha15: vykonaný experiment

Soubor `results/sequential-allocation.json` obsahuje81 běhů se seedem
20261101: dvojice(n,M)=(2,40),(5,200),(10,1000), rovnoměrnou, vychýlenou
 a postupně měněnou distribuci zásobníků, cílovou obsazenost50%,90%,99%
 a tři replikace každé kombinace. Pravděpodobnost vkladu je0.8 pod
cílem a0.2 nad ním; při prázdné/plné paměti je volba omezena přípustností.
Neprovedená odebrání z prázdného zásobníku se nepočítají jako operace.
Bylo vykonáno241554 operací; po každé se porovnal úplný obsah obou
algoritmů s nezávislými seznamy a ověřily se adresové invarianty.
PřídělyG se počítají přesnými zlomky. Počítá se počet fyzicky
kopírovaných slov, nikoli skutečný čas Pythonu.

Samostatné konečné kontroly:6688 vkladových posloupností včetně všech
n≤4,m≤6;6608 legálních relokací s neprázdnými i prázdnými seznamy;
719146 prefixů pro srovnání inicializací. Poslední kontrola odhalila
nepravdivost úlohy17, evidovanou a obecně vyvrácenou vC0034. Nevydáváme
ji za úspěšný důkaz původní nerovnosti. Obrázek4 i obě číselné ukázky
úloh9/11 souhlasí přesně.

Souhrn sdružuje tři distribuce a tři replikace. Poměr je součet přesunů G
vydělený součtem přesunů jednoduchého algoritmu, nikoli průměr poměrů.

| n | M | Cílová obsazenost | Jednoduchý algoritmus | G | Poměr G/jednoduchý |
|---:|---:|---:|---:|---:|---:|
| 2 | 40 | 50% | 515 | 868 | 1.685 |
| 2 | 40 | 90% | 12298 | 8663 | 0.704 |
| 2 | 40 | 99% | 36283 | 36333 | 1.001 |
| 5 | 200 | 50% | 23176 | 14503 | 0.626 |
| 5 | 200 | 90% | 98481 | 160493 | 1.630 |
| 5 | 200 | 99% | 254680 | 312106 | 1.225 |
| 10 | 1000 | 50% | 531343 | 6093 | 0.011 |
| 10 | 1000 | 90% | 1543653 | 352591 | 0.228 |
| 10 | 1000 | 99% | 2096647 | 1446964 | 0.690 |

Výsledek není univerzální dominance G: u malých konfigurací může mít
více přesunů, zvlášť když jednoduchý algoritmus téměř nic přesouvat
nemusí. Pro n=10,M=1000 při poloviční cílové obsazenosti je rozdíl velký
ve prospěch G; blízko úplnému zaplnění jeho výhoda slábne. Tyto konkrétní
vzorky odpovídají kvalitativnímu varování textu o téměř plné paměti,
ale nedokazují tvrzení o všech možných zátěžích. Cvičení žádá experiment,
ne univerzální pravděpodobnostní zákon. Časy výpočtu podílů a průchodu
n seznamy nejsou započítané v počtu přesunutých slov.

## 7. Otevřené kroky tohoto bloku

Nepřímé adresování3–5 a kruhové fronty8 jsou dokončené v samostatné
poznámce sequential-addressing-queues.md; kontrola3000 rozložení front
provedla i skutečné otáčení oblastí a bezpečné kopírování. Otevřené
zůstávají dva limitní kroky úlohy13, počáteční interval18 (C0035)
a část bibliografie. Úloha17 je vyvrácena vC0034. Přesný stav pramenů
a známých oprav je v sequential-sources-errata.md.
