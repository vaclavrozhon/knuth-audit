# Commafree kódy — 7.2.2, hlavní strany 37–46 a úlohy 34–48

Pracovní stav k 1. listopadu 2026. Nové nálezy F085–F087 jsou doloženy
v našem PDF druhého dotisku i v autorově PostScriptu Fascicle 5B z roku 2019.
Fyzický výtisk dosud ověřen nebyl. Návrhy hlášení nejsou odeslané.

## F085: výběr z nesprávné třídy v odpovědi 44(b), strana 404

Část (a) vybere třídu c s nejmenším počtem modrých slov. Část (b) však čte
MEM[CLOFF + 4 cl(ALF[x])], tedy třídu předchozího x. Správně má použít
MEM[CLOFF + 4c]. Případ r = 0 navíc potřebuje x ← −1, jak už vyžaduje zadání.

Konkrétní průběh pro m = 2, g = 3: první dvě volby jsou 0001 a 0011.
Na úrovni 3 má třída [0111] jediného modrého kandidáta 0111, proto r = 1
a c = 2. Původní výraz vrátí z uzavřené třídy [0011] již zelené 0011.
Část (c) se při r = 1 neprovádí, a proto to neopraví. Doslovný model tento
stav zachytil; po opravě souhlasí všechny binární výsledky s úplným výčtem
podmnožin a všechny ternární výsledky s původním C programem i SAT výčtem.

Zveřejněný BACK-COMMAFREE4 používá správně vybranou třídu. Jde o chybu
v knižním přepisu, ne o chybu tohoto zdrojového programu. Předchozí oprava
z 30. 5. 2020 mění pouze inicializaci r na 5 a tento problém neřeší.

## F086: velikost kódu v popisu Algorithm C, strany 45–46

Algoritmus vypisuje kódy s alespoň g slovy, zatímco úvod říká „sets of g“.
Například m = 2, g = 2 je dovolený vstup; první výsledek je
{0001,0011,0111}, který má tři slova. Celkem vznikne 15 dvouslovných
a 14 tříslovných výsledků. Při g = 1 přibudou ještě dva jednoslovné.

Příčina je v C2: při l > L se řešení navštíví bez ohledu na zbývající slack s.
Počet zelených slov je g+s, protože z L tříd se vynechalo L−g−s.
Nejmenší oprava popisu je „at least g“. Pokud má být velikost přesná,
stačí návštěvu v C2 podmínit s = 0. Oba nezávislé modely i autorův C program
potvrzují uvedené počty. Výpočty maxima 57 na čtyřpísmenné abecedě tím
nejsou dotčeny: větší kódy neexistují.

## F087: pravděpodobnost pro n = 9 v odpovědi 38, strana 404

Poslední pravděpodobnost 1−3/binom(m³−1,3) neodpovídá předchozí, správné
vytvářející funkci. Pro m = 2 je 504 aperiodických devítibitových slov.
Z nich 486 skončí v jednom kole, takže pravděpodobnost je 27/28, nikoli
32/35. Už 504·32/35 není celé číslo, což samo vyvrací vytištěnou hodnotu.

Pro m = 2 se správná funkce z knihy zjednoduší na G₂(z) = 2z³/(1−3z²).
Koeficient u z⁹ je 54 a 9·54 = 486. Obecně položme r = (m³−m)/3.
Správný výraz pro n = 9 je

    1 − 3(r³−r)/(m⁹−m³).

Počet r je počet třípísmenných dips. Dvě kola potřebují právě slova,
jejichž první rozklad má tři třípísmenné superdips; z těchto r symbolů
existuje (r³−r)/3 cyklických tříd. V původních slovech jde o
9(r³−r)/3 = 3(r³−r) aperiodických slov. Alternativně lze uvedený výraz
přímo získat rozvojem G_m do stupně 9; oba výpočty souhlasí.

Doslovný Algorithm O, nezávislé hledání cyklické faktorizace přes všechny
počáteční řezy a přesná vytvářející funkce dávají shodně:

| m | Aperiodických slov délky 9 | Jedno kolo | Pravděpodobnost |
|---:|---:|---:|---:|
| 2 | 504 | 486 | 27/28 |
| 3 | 19 656 | 18 144 | 12/13 |
| 4 | 262 080 | 238 140 | 189/208 |

Pro F085–F087 byly zkontrolovány err4b.textxt, err4f5.textxt a úplná
historická all4b.txt/all4f5.txt, podle umístění i matematického obsahu.
Oprava těchto tří tvrzení nebyla nalezena. Historická oprava z₂→z_{k−1}
v odpovědi 38 je v našem hlavním PDF již zapracována.

## Ověřený algoritmický a matematický obsah

`check_commafree.py` přepisuje C1–C6, všech sedm seznamů, inverzní indexy,
barvy, poison list a zásobník UNDO se značkami. Používá oddělená radix-m
a hexadecimální čísla. Oprava F085 dává přesně stejné kódy jako nezávislý
výčet všech vhodných podmnožin pro m = 2 a všechny dovolené cíle 1,2,3.
Ternární přepis dává 72 reprezentantů a shoduje se s autorovým programem.

Invarianta otevřeného seznamu: obsahuje právě modrá slova příslušného
prefixu, suffixu či cyklické třídy; inverzní ukazatele ukazují zpět.
Uzavřený seznam má alespoň jedno zelené slovo a sentinel HEAD−1.
Zčervenání odebírá položku pouze z otevřených seznamů; zazelenání uzavře
jejích sedm seznamů a vyloučí ostatní rotace. Každá zelená položka vloží
všechny tři zakázané překryvy. Poison list odmítne dvojici zelených stran,
nebo vyloučí modrou stranu proti zelené; prázdná strana dovolí záznam smazat.
Po každém úspěšném kroku tak zůstávají právě relevantní překryvové podmínky.
Návrat přes UNDO obnovuje stav před pokusem a slovo se pak trvale vyřadí
jen v příslušné větvi. Poslední volba prázdné třídy odpovídá jejímu vynechání.

Úloha 34: jediná maximální podmnožina má 11 slov a vypouští face a dada.
Úloha 35: saturující počitadla jsou správná. Neuchovávají přesné počty,
ale nulovost. Přidání a vrácení odmítnutého slova zobrazuje staré hodnoty
0,1,2 na 0,1,1, čímž zachovává tuto invariantu. Tři součiny prefixů a
suffixů zachytí právě všechny zakázané posuny každého přijatého slova.
Ověřeno 4096 trojicemi binárních vstupů a 400 proudy délky 50 pro m = 2–5.

Úloha 36: překryv ab|cd je bc, tedy odpovídá orientované cestě délky 3.
Cesty se zde smějí vracet do vrcholů; nejde o podmínku prosté cesty.
Bez cesty délky r musí být graf acyklický. Rozdělení podle nejdelší cesty
z vrcholu má r vrstev, hrany vedou do nižších vrstev a lze je všechny doplnit.
Počet hran je (m²−Σp_j²)/2; přesun z vrstvy o alespoň dva větší do menší
zvýší počet, takže optimum má vyrovnané velikosti floor((m+j)/r).
Všechny orientované grafy na nejvýše třech vrcholech, včetně smyček,
potvrdily ekvivalenci a maxima pro r = 1–5.

Úlohy 41–42: přepsáno a zkontrolováno všech 187 neprázdných buněk tabulky 1
a 125 buněk tabulky 2. Správné adresy jsou 4d,94,ad; nadbytečné nuly
v popiscích jsou již známé erratum z 27. 11. 2022, nikoli nový nález.
Zbývající poison pár po volbě 0010 obsahuje právě 1100 proti 1011.

Úloha 43: po přetečení stačí STAMP[:] = 0 a σ = 1. Nová značka se pak
nerovná žádné staré, a každý první zápis do adresy uloží předchozí hodnotu.
Stará UNDO data zůstávají platná; značky řídí jen nové zápisy. Varianta
STAMP[:] = −1, σ = 0 selže při pozdějším dosažení −1 u dosud nedotčené
adresy: první zápis se neuloží. Počet memů 5r oproti 2r+5 vychází přímo
z načtení a zápisu položek tabulek a zásobníku.

Příklady lookahead na stranách 38–39 souhlasí. Pozor: modrý kandidát nemusí
být slučitelný při plné kontrole. Po nucených pěti volbách stále zůstávají
modré 0012 a 2001, ale pokus o každé z nich vede ke sporu. První verze
našeho testu chybně ztotožnila tyto dva pojmy; šlo o opravený test, ne chybu
knihy. Totéž vysvětluje nucený pokus 1001 po 0001 a 0012.

## Úplné počty čtyřpísmenných kódů a úloha 47

Zdroje původních programů jsou archivované beze změn z
[Knuthovy stránky programů](https://www-cs-faculty.stanford.edu/~knuth/programs.html).
Každý vydaný kód byl ověřen přímo definicí přes všechny dvojice slov a posuny.

| m | g | Výstupů C | Všech označených kódů | Tříd izomorfismu |
|---:|---:|---:|---:|---:|
| 2 | 3 | 14 | 28 | 8 |
| 3 | 18 | 72 | 144 | 12 |
| 4 | 57 | 1152 | 2304 | 48 |

Nezávislá CNF zakazuje každý překryv a dovolí nanejvýš L−g prázdných tříd.
Úplný SAT výčet dává přesně stejné množiny pro všechny tři řádky.
Pro m = 4, g = 58 skončil SAT důkazem UNSAT. Jeho DRAT certifikát prošel
samostatným drat-trim: 746421 rezolučních kroků, výsledek `s VERIFIED`.
Použitá symetrie 0001∨0010 je pro neexistenci oprávněná: vynechat lze jen
dvě třídy, ale tříd tvaru aaab je dvanáct, takže některou lze přeznačit
a zrcadlit na povolený počáteční tvar.

Pro g = 60,59,58,57 souhlasí i autorova časování a velikosti stromů:
13 389 554; 176 994 263; 2 380 384 386; 22 785 292 928 memů a
13 940; 239 161; 3 691 130; 37 632 700 uzlů. Nejvyšší UNDO má 2804
položek a poison list 12 záznamů, přesně podle textu.

Rozdělení tříd v odpovědi 47(c) je rovněž správné: předepsaná první trojice
vynechaných cyklů dává 12 kódů v 12 třídách; druhá dává 72 kódů v 36
třídách, vždy dva reprezentanty každé třídy. Explicitní dlouhé příklady
a podrobnosti historických zdrojů se kontrolují zvlášť.

## Eastmanova konstrukce a zbývající rozsah

V `check_eastman.py` souhlasí příklad 37(a), nejhorší rodiny až po délku
3⁶ = 729, všechny binární třídy do délky 13 a ternární i čtyřpísmenné
třídy do délky 9. Všechny vzniklé množiny jsou commafree; výstup nezávislé
cyklické faktorizace je totožný. Pro binární případy a kratší ostatní
byly ověřeny také všechny rotace vstupu. Každý nový superdip obsahuje
nejméně tři staré faktory, takže počet kol je nejvýše floor(log₃ n).

Obecná konstrukce pracuje díky synchronizaci na konci dipu délky alespoň
tři. Vybrané hranice jsou jednoznačné v celém periodickém řetězci a jejich
počet zůstává lichý. Pokud by kódové slovo překrylo dvě jiná, jeho první
lichý dip synchronizuje rozklad; superdip hranice pak musejí souhlasit.
Přechodem na abecedu superdips se argument opakuje až do vrstvy, kde je
některé ze slov jediným superdipem, což takový překryv vylučuje.
Podrobnější primární rozbor má
[Perrin–Reutenauer, oddíly 5–6](https://arxiv.org/pdf/1609.05438).

Následné dočtení primárního rozboru odhalilo F101, popsaný níže.
Větší výsledky 46 a 48 se kontrolují samostatnými certifikovanými běhy;
jejich průběžný stav je v `results/commafree/large-wrapper.json`.

Výsledky, příkazy, logy a certifikáty jsou v `results/commafree/`.

Dodatek: všech 8 binárních a 12 ternárních explicitních reprezentantů odpovědi47 i obě dlouhé čtyřpísmenné ukázky a předepsaný zrcadlený obraz byly samostatně ověřeny (`examples-verified.json`). Jiggsův původní článek, strana184, přímo potvrzuje údaje o Laxdalově výpočtu a nemožnosti58 slov; PDF je archivováno v sources/commafree.

## F101: Scholtzova konstrukce nevybírá stejné kódové slovo

Strana404, závěr odpovědi37(e), říká, že Scholtz jinak definuje množinu
slov produkovanou Algorithm O. Perrin–Reutenauer, příklad17 na straně12,
výslovně ukazují rozdíl. Pro a<b<c položme

    A=a^12 c, B=a^10 c, C=a²c, D=a²b, x=A B C D C.

První kolo O ponechá pět hranic0,13,24,27,30. Faktory mají délky
13,11,3,3,3 a splňují A≥B≥C≥D<C. Jsou tedy jedním dipem délky5
v další abecedě; O vrátí x. Scholtzův výběr v obvyklém pořadí dá
B C D C A, tj. posun o13. Po eliminaci jednotlivých písmen se sloučí
D C, potom C(D C), potom (C D C)A a nakonec B(C D C A).
Rozhoduje přednost liché délky a pak délka a lexikografické pořadí.

`check_scholtz.py` ověřuje výsledek čtyřmi způsoby: doslovným O,
nezávislou cyklickou faktorizací, Melançonovým slučováním a samostatným
rekurzivním rozpoznávačem Hallových stromů. Poslední metoda zkouší
všechny binární řezy slova podle definice v §2.1 článku; nepoužívá
greedy slučování. Pro x nenajde žádný strom, pro posun najde právě jeden.
Ověřeno všech33 rotací. Doplňkový binární příklad délky27 rovněž dává
odlišné výsledky (při uvedeném standardním pořadí); nehlásíme jeho
minimalitu. Pro návrh hlášení používáme přímo publikovaný příklad33.

Stejná formulace byla vizuálně ověřena v PDF4B i v autorově PS5B,str.42.
Prohledána současná i historická errata4B/4F5 včetně mapování404→212;
oprava této identifikace nenalezena. Známé změny O3/O4/O5 a rekurence37(c)
jsou odlišné a v hlavním PDF už zapracované. Hashované doklady jsou
v `scholtz-verified.json`. Původní článek1969 nebyl dostupný přes veřejné
IEEE rozhraní; matematická definice a důkaz rozdílu pocházejí z primárního
výzkumu Perrina–Reutenauera, nikoli z neověřeného internetového shrnutí.

## Dokončení důkazu37 a odkaz40

Dočteny §5–6 Perrin–Reutenauer: konec dipu délky≥3 synchronizuje každý
rozklad, lichý počet písmen zaručí lichý počet lichých dips. V každém kole
se zachovají právě jejich začátky. Primitivita vylučuje konstantní
víceprvkový cyklus v další abecedě. Každý superdip obsahuje alespoň tři
staré symboly, proto počet kol nepřekročí floor(log₃n).
Při možném překryvu se synchronizují hranice superdips; po přechodu
na jejich abecedu se totéž opakuje, až vznikne spor v jednoprvkové vrstvě.
Tím se uzavírá obecný důkaz, vedle dřívějších konečných kontrol.

Pro n=1 je počáteční t již1 a konstrukce vrací totožné slovo bez kola.
Samotný nízkoúrovňový O2 hledá vzestup, takže před vstupem potřebuje
tuto triviální odbočku. Zadání výslovně označuje n=3 za první netriviální
případ a předepisuje výstup při t=1; bereme to jako konvenci vstupu do
rutinní části, ne jako samostatný nový nález. Tři singletony byly ověřeny.

Úloha40 byla přímo porovnána s naším svazkem1, §2.2.2, strany244–254:
jde o zásobníky, fronty a sdílení proměnně velkých souvislých tabulek,
včetně jejich přemisťování při přeplnění. Technické vysvětlení paměťového
kompromisu odpovídá textu. Autorovo vysvětlení volby tématu je historický
komentář; nejde o tvrzení, že moderní souvislé množiny nelze implementovat.

## Úlohy46 a48: nové přímé svědky a menší SAT kódování

Z autorova [zveřejnění2021](https://blog.aaw.io/2021/01/20/comma-free-codes.html)
jsou archivovány seznamy139,113,334 slov. Každý prošel doslovnou kontrolou
všech dvojic a všech posunů. Poslední opravdu vynechává jen třídu
[000011001011]. Vydavatelský náhled2023 má veřejný dodatek s týmiž seznamy;
hlavní placený text není součástí našich podkladů. Nový bibliografický odkaz
je známé doplnění18.2.2023, nikoli nový nález.

Nezávislé kódování zavádí indikátory přítomných prefixů a suffixů.
Pro každé kódové slovo z a řez k zakáže současně z, suffix z[:k]
a prefix z[k:]. Jde přesně o rozklad definice zakázaného překryvu:
oba indikátory mohou pocházet z téže položky a ta může být rovna z.
Definice OR jsou obousměrné. Počet vynechaných cyklických tříd omezuje
sekvenční počitadlo; nanejvýš jeden reprezentant třídy plyne i z překryvů.
Úplné podmnožiny binárních primitivních slov pro n2,3,4 (4,64,4096 případů)
potvrdily přesnou ekvivalenci s přímou definicí.

Symetrie používá pouze přeznačení abecedy a zrcadlení. Protože počet
vynechaných tříd je menší než m(m−1), některá třída a^(n−1)b je přítomna;
její zástupce lze převést na slovo s jedinou1 ve druhé polovině. Cyklický
posun všech slov se jako symetrie nepoužívá.

Nové SAT svědky potvrzují plná binární maxima pro n2,4,6,8,10:
1,3,9,30,99. Všechny výstupy byly doslovně ověřeny. Pro původní nerozložené
kódování vycházejí přesně8 582 382 záporné +99 kladných klauzulí při n10,
a175 005 084 +335 při n12; počty proměnných990 a4020 rovněž souhlasí.
Tyto počty jsou vypočteny součinem počtů prefixů/suffixů, nikoli odhadem.

Pro m3,n6 je114 slov UNSAT;75 194 224bytový binární DRAT certifikát už
ověřil samostatný drat-trim. Tím je maximum113 nezávisle uzavřeno.
Pro binární slova délky12 je nyní nezávisle uzavřeno také maximum334:
335 slov je UNSAT a samostatná kontrola důkazu skončila `s VERIFIED`.
Případ140 slov délky4 nad pětipísmennou abecedou je také dokončen:
UNSAT a samostatně ověřený DRAT uzavírají maximum139 (podrobnosti níže).
Historické memy původního SAT solveru nebyly tímto moderním během
reprodukovány a nesmějí se s ním zaměňovat.

### Dokončený důkaz pro 335 binárních slov délky 12

CaDiCaL 1.9.5 skončil 1. listopadu 2026 v 13:51 UTC s výsledkem UNSAT.
Výpočet trval 11638.966 sekund. Samostatný `drat-trim` následně ověřil
binární certifikát za 4391.209 sekund a vrátil úspěšný návratový kód 0.
CNF má 12543 proměnných a 163629 klauzulí; kontrola použila 4661223
důkazových lemmat a 820096052 rezolučních kroků. Jde o kontrolu uloženého
důkazu nezávislým programem, nikoli o opakování téhož SAT běhu.

- [Metadata výpočtu a kontrolní součty](results/commafree/compact-m2-n12-g335-cadical195-run.json)
- [Původní CNF](results/commafree/compact-m2-n12-g335-cadical195.cnf)
- [Úplný log ověření](results/commafree/compact-m2-n12-g335-cadical195-proof.log)
- [Bezeztrátově komprimovaný certifikát](results/commafree/compact-m2-n12-g335-cadical195.drat.gz)

Nezkrácený certifikát měl 1420024147 bytů a SHA256
`cc6c347b2570fc51226fdf2dd8d2c84bf9df98594053464fe0a2795dce4b7036`.
Gzip archiv má 749447859 bytů. Před odstraněním nekomprimované kopie
byl celý archiv rozbalen proudově a porovnán jeho počet bytů i SHA256;
ověřený obsah se shoduje přesně. Postup je v `archive_drat.py`.

Spolu s dříve doslovně ověřeným Windsorovým 334slovným svědkem to
uzavírá matematické maximum 334. Původní knižní memy zůstávají oddělenou
historickou mezerou; nový běh je neměří a úloha46 zůstává v úplném registru
částečně otevřená. Tato kontrola potvrzuje výsledek knihy, nepřidává nález.

### Dokončený důkaz pro 140 slov délky 4 nad pěti písmeny

Výpočet CaDiCaL 1.9.5 skončil 1. listopadu 2026 v 16:06:18 UTC po
3709.216 sekundách. Nezávislý `drat-trim` následně přečetl celý
934925204bytový binární důkaz a skončil `s VERIFIED`, návratový kód0,
po5421.268 sekundách. Ověřil6080058 důkazových lemmat a353664720
rezolučních kroků. CNF má2460 proměnných a9691 klauzulí.

- [Metadata, příkaz a kontrolní součty](results/commafree/compact-m5-n4-g140-cadical195-run.json)
- [Vstupní CNF](results/commafree/compact-m5-n4-g140-cadical195.cnf)
- [Úplný kontrolní log](results/commafree/compact-m5-n4-g140-cadical195-proof.log)
- [Komprimovaný úplný důkaz](results/commafree/compact-m5-n4-g140-cadical195.drat.gz)

SHA256 původního důkazu je
`ad7d6ff8d703e0d1e2468526657dbfe99ece5210494b71d89d5c966e58f874ef`.
Gzip má473058160 bytů a SHA256
`4d520f537d10ad46a99973d2e8c3e955b25cd64e4bdbebb1ffcf71c5a8f5fed8`.
`archive_drat.py` nejprve celý archiv proudově rozbalil a ověřil jeho
shodu s původními byty; teprve potom odstranil nekomprimovaný duplikát.

Spolu s již doslovně prověřeným139slovným svědkem to dokazuje maximum139.
Stejně jsou doloženy svědek113 a nemožnost114 pro ternární slova délky6.
Obě číselné identity odpovědi48 souhlasí: (625−25)/4−11=139 a
(729−27−9+3)/6−3=113. Zadání58 a odpověď406 znovu vizuálně přečteny.
Historické zveřejnění a rok2021 potvrzuje archivovaný Windsorův vlastní
text z20. ledna2021; nahrazení staré otevřené odpovědi je známá oprava
8. února2021 ve Fascicle5,str214. Slova o pomalosti Algorithm C jsou
historickým hodnocením tehdejšího postupu, nikoli novou časovou mezí.
Úloha48 je nyní v úplném registru uzavřena. Nejde o nový nález chyby.
