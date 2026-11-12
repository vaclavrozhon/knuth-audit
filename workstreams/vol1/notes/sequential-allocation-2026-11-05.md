# Souvislý průchod §2.2.2 — 5. listopadu 2026

Přečteny celé originály 244–254 a odpovědi540–545; na545 zatím
uzavíráme jen odpověď19. Na254 je zahrnut i úvodní odstavec a diagram
§2.2.3. Revidovány důkazy v `sequential-allocation.md`,
`sequential-addressing-queues.md`, `sequential-probability.md`, oba
úplné limitní důkazy v `parallel/sequential-probability/` a kořenové
převzetí Kozelky. Čtyři aktuální vrstvy errat mají nový výpis
`sources/sequential-2026-11-05/sequential-allocation-errata-extract.json`.
Žádný starší úspěšný výpočet ani Monte Carlo nebyl znovu spuštěn.

## Reprezentace, adresování a přesuny

Adresový vzorec L0+cj, počet prvků zásobníku T a velikost kruhové
fronty (R−F) mod M odpovídají originálům. Fronta rezervuje jednu
buňku, takže má kapacitu M−1. Stav po neobslouženém přetečení nelze
použít jako nový platný stav. Známé doplnění M>1 je odděleno od
samotné správnosti operací. V nula-originové variantě F označuje
první prvek a R následující volnou pozici; proto se mění pořadí
čtení/zápisu a posunu. Tři pevná dna nezaručují využití celé
společné paměti bez přesunů; argument neplatí obecně pro libovolnou
jinou reprezentaci.

Jednoduchý přesun doprava musí kopírovat sestupně, doleva vzestupně.
Známá oprava L<TOP[i] v levém případě je nutná, protože TOP[i]
už obsahuje dočasné navýšení před zápisem nového prvku. Obr.4 má
BASE=(0,3,5,6,20), TOP=(2,4,6,8); hvězdičky označují správné
operace. V úloze6 druhé D2 podteče; pokračování beze změny stavu
vede také k přeplnění posledního I2.

G2 má při skutečném přetečení INC>0: TOP[i]>BASE[i+1]≥OLDTOP[i].
Ideální příděly q_j=S/(10n)+9S D_j/(10 INC) jsou nezáporné a
sečtou se na S. Rozdíly podlah kumulativních součtů dávají alespoň
floor(S/(10n)) každému zásobníku a přesně zachovají celou kapacitu.
G6 odvolá dočasný nový vrchol před kopírováním a po R jej obnoví.
Životnosti OLDTOP[j],D[j],NEWBASE[j+1] dovolují sdílení buňky.
Směr průchodu R i vnitřního kopírování chrání nepřesunutá data;
známá tautologie v R4 se opravuje na NEWBASE[j]>BASE[j].

Rozšířené adresování3–5 bylo revidováno včetně neukončujících
nepřímých cyklů a přesné výjimky pro vnořené7:7. Algoritmus A
správně skládá čekající indexové součty a počet dereferencí v
povolené třídě; reset H vysvětluje uvedenou výjimku. Nulové buňky
0:0 v úloze4 neumožňují získat libovolný řetěz tří dereferencí
jednou instrukcí. ENT4 a LD4 se liší pro zápornou nulu. Přijaté
2960 testy ve všech použitých základech nenahrazují tento důkaz.

Pro fronty/deque lze každou kruhovou oblast normalizovat třemi
obráceními a potom použít bezpečné R. Každá fronta potřebuje
virtuální velikost q+1 včetně rezervované buňky; vkládaný prvek
se zapíše až do připraveného místa. Přijaté 3000 konfigurací a
10519 front doplňují invarianty. Tato konstrukce netvrdí
amortizovaný čas úlohy18 pro normalizaci všech front.

## Počty a pravděpodobnosti

Úlohy9–11: počet přesunů při pouhých vkladech je počet inverzí
slova a1…am. Jeho očekávání je binom(m,2)(n−1)/(2n), obecně
binom(m,2)(1−sum p_i²)/2. Tím se nezávisle potvrzuje přísná
mez j<k. Model prvních t bezplatných vkladů má přesně oba
opravené konečné součty i opravenou generující funkci z2005;
rovnost pro všechna m dokazuje rozdíl po posledním vkladu,
nikoli jen konečný test. Číselné příklady16 a12 souhlasí.

12: binomické teleskopování dává
m/2+m*binom(m−1,floor(m/2))/2^m. Stirling v obou paritách dává
m/2+sqrt(m/(2pi))+O(m^(-1/2)). Nové odvození z2024 zachovává
stejný výsledek; původní správná odpověď není novým nálezem.

13: rozlišeny tři různé limity. Pro pevné m a p→1 mají konce
absorpční hrany polovinu hmotnosti vnitřních bodů; pro m=4
souhlasí přesné racionální pravděpodobnosti. Vytištěný člen pro
liché m je 1/(4m), nikoli OCR1/4. Při p=1 k zaplnění nedojde.
Pro pevné p<1/2 nezávislé souřadnicové kroky a kontrola dotyků
os dávají zbytek O(log²(m)/sqrt(m)) uvedený v knize.

Pro p=1/2 půlčíselné rozvinutí přesně zachovává nulový krok při
odebrání z prázdné struktury. Po otočení je to diagonální
procházka ve čtverci; parita vylučuje rohy. Harmonická Fourierova
řada má správné hraniční hodnoty a stejnoměrnou konvergenci.
Stažení na r<1 dává chybu jednoho kroku O_r(h⁴), zatímco
E tau≤h^(-2); nejprve h→0 a pak r→1 ospravedlňuje limitu.
Greenův tok má normalizaci1, váha t umožňuje absolutní integraci
po členech. Obě analytické řady proto dávají tutéž konstantu
0.6753144833…; nejde pouze o číselnou shodu.

Pro každé pevné1/2<p<1 má kvadratický potenciál záporný drift
mimo konečnou množinu. Regenerace dává konečnou střední dobu
návratu; vratnost zastavené Greenovy funkce odhadne návrat z
hloubky L k plné paměti. Přesná normalizace H_m(j)=W_m(j)/sum W_m
pak dává rovnoměrnou limitu. Odhad W_m≤2 zvlášť kontroluje
koncové úseky. Je tudíž dokázáno také E max/m→3/4, bez chybné
záměny prvního zásahu za stacionární hmotnost.

14: lokální Stirlingův rozvoj, exponenciální odhad ocasů a
vážené Riemannovy součty dávají skutečný zbytek O(1).
Normální vektor (Z_i−Zbar)/sqrt(n) dává všechny čtyři konstanty.
Jacobián a faktor x1 poskytují I1=I2/n². Kozelkův původní článek
je přijat jako doklad c3; jeho vlastní chybný řádek(11) kniha
nepřebírá. Vyšší domnělé historické prvenství tím není dokázáno.

15: přijatý experiment má81 běhů a241554 operací s kontrolou
úplného obsahu. Měří kopírovaná slova, nikoli skutečný čas.
G není ve všech vzorcích lepší a experiment nedokazuje obecnou
pravděpodobnostní převahu. To odpovídá rozsahu zadání.

## Dva nálezy se neslučují

**C0034 zůstává confirmed, high.** Pro n=M=4 způsobí
I3 D3 I2 D2 I1 D1 I3 D3 I2 pět přeplnění při kapacitách
(0,0,0,4), ale žádné při (1,1,1,1). Neživí se více než jeden
prvek současně. Všechny přesuny berou volno zprava. Rodina
bloků P_(n−1)…P_r, r=1,…,n−1, má n(n−1)/2 proti0; oprava
less→more z2009 ji neopravuje. Skutečná vadná místa jsou zadání
na254 a odpověď544. Volnější odstavec248 o „fixed number“ tímto
není samostatně vyvrácen pro pevné n a M.

**C0035 zůstává candidate.** Po každém přebalení je účetní důkaz
platný: před dalším je p>S/(10n), a M≥n² zaplatí lineární průchod
tabulkami. Inicializace(11) však dovolí m=1,M=n² a okamžitou
cenu Ω(n) při alpha1=0. Rovnoměrná inicializace(13) tuto mezeru
odstraňuje: první přeplnění vyžaduje alespoň floor(M/n)+1≥n+1
vkladů, do nichž se první průchod amortizuje. Nová přímá četba
„as before“ na248 výhradnost(13) nevyjasnila. Bez ní nelze
prohlásit úlohu18 za uzavřenou ani tento kandidát povýšit.

## Pramenné výjimky a stránky

Podle pokynu uživatele se výslovně přeskakuje obsah plného
Yao1981, SIAM J. Comput.10,398–403, Wise–Watson1976, BIT16,
442–450, a Fraenkel1979, IPL8,9–10. Jejich dostupná metadata,
Yaoův přesný vydavatelský abstrakt, přečtený report1979 a
vlastní důkazy se nezaměňují s přečtením chybějících článků.
Úloha13 se tím může změnit partial→checked; úloha18 nikoli.
Připsání návrhu Garwickovi není výrokem ověřeného výlučného
prvenství. Anekdota o Dijkstrově počítání při hře na klavír na545
nemá samostatný doklad; zůstane uvedenou historickou mezerou.

Celé244–253 a540–544 mají vyznačený rozsah, s248/251 částečnými
kvůli výkladu inicializace či odkazované amortizace. Na254 je
zkontrolován také úvod následující sekce; stránka zůstává
částečná kvůli18. Strana545 je zatím pouze částečná, neboť
obsahuje i odpovědi§2.2.3. Známé obsahové opravy X0233 mapujeme
na245,247–249,252,540,542–544. Pouhá úprava rozestupů na541,
sazby max na253 a zjednodušení správného odvození12 nejsou
novou matematickou chybou těchto stran.

Výsledek:18 z19 úloh uzavřeno, hlavní text partial kvůli C0035.
Žádný nový neznámý nález. Následuje §2.2.3 od255; diagram254
už je přečten.
