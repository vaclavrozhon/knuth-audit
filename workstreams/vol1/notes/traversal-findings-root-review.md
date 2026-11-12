# Kořenová revize dalších nálezů §2.3.1

Datum 2026-11-01. Root přímo zobrazil původní strany134,321,324,325,332,
565,566,567,568 a původní all1-prepre42. Přečetl samostatné podklady
podagenta i výsledky a doplnil vlastní ruční a analytický výpočet.
Globální označení jsou C0047–C0050; nejsou tvrzením o prvenství
ani o fyzické kontrole dalších dotisků.

## C0047: CMP5, confirmed

Na134 je výslovně dáno porovnání stejného pole a nulové bajty1–3
indexového registru; závorka dokonce uvádí pole1:2 jako příklad.
Na325 je RLINK=1:2. Původní568 skutečně tiskne CMP5 1,6(RLINK),
nikoli instrukci přenášející hodnotu indexu do tohoto pole.

Ruční průběh stromu s kořenem a levým listem tedy porovná nulu s nulou,
skočí na odstranění neexistující nitě, navštíví pouze kořen a skončí.
Nejmenší příklad nevyužívá žádný sporný výklad přetečení ani simulátor.
Oprava ST5/LD4/DEC4/J4Z má správný výběr cílového adresního pole;
rozdíl dvou platných adres se vejde do indexu. Původní další ENT4
obnoví pracovní Q při nerovnosti, při rovnosti staré I4 není potřeba.
Oprava zachovává původně nedotčené A,X,I1–I3. Její1454skutečných
MIXběhů se při revizi znovu nespouštělo.

## C0048: optimalizovaný čas, confirmed

Root přímo přečetl původníT i vložené dvě instrukce. Jediný uzel
obejde zásobník i oba neurčené upravené řádky10/11, přesto stojí12u,
kde obě formule dávají11u. Volací JMPkVISIT patří do knižního rozboru;
externí tělo a návrat do něj nepatří. DONE je koncová adresa, ne dalšíHLT.

Pro variantu ENT5 0,3; J5NZ T3 byly nezávisle sečteny četnosti:
inicializace4, nové testy3n, návštěvy a pravé přechody4n, testy zásobníkua.
Souvislé vložení/návrat/vyjmutí stojí(5+2+3)(a−1), spojové
(12+2+11)(a−1). Součty jsou7n+11a−6 a7n+26a−21.
Od knihy se obě liší on−a+1, počet nulových levých odkazů.
Prázdný strom má samostatně3u.

## C0049: kořenový postorder následník, candidate

Definice na321 při neexistujícím následníku používá LOC(T), na324
ztotožněné sHEAD. U singletonu AlgorithmF vrátí správněHEAD jako rodiče.
Prozaický popis na566 potom vidí P=LLINK(HEAD), postoupí inorderem
doP a zastaví na jeho pravém vlákně. VracíP místoHEAD.
Test Q=HEAD před rozlišením dítěte je dostatečná oprava.

Zachován statuscandidate: text se výslovně označuje jako základní
myšlenka a volající může konec u kořene ošetřit samostatně. Závěr
proto nerozšiřujeme na vadnost celé obecné konstrukce nebo samotnéhoF.

## C0050: veřejná oprava výškové asymptotiky, confirmed

Originál565 a erratum42 jsou jednoznačné; nejde oOCR ani změnu definice.
Průměr je přes všechny Catalanovy tvary s přesněnuzly. Kořen nezávisle
ověřil h=max(1+h(L),h(R)), rekurenci g_k=1/(1−z*g_(k−1)) i ocasový
součet. Při z=u/(1+u)^2 a D(u)=sum_{j≥1}u^j/(1−u^j) vychází
S(z)=(1/u−u)D(u)−(1+u). Tento výpočet nevyužívá žádnou asymptotiku
z citovaného článku ani žádné numerické přiblížení.

Pro t=−log(u) jsou Mellinovy pólyGamma(s)zeta(s)^2:
dvojný pól1 dává(gamma−logt)/t, pól0 dává1/4 a pól−1 dává−t/144.
Posun do libovolného pevného dalšího řádu je dovolen v sektoru
|argt|≤pi/2−epsilon díky exponenciálnímu poklesuGamma na svislicích.

Dále w=1−4z a t=2atanh(sqrtw). Root přepočetl
A(w)=sinh(t)/t=1/((1−w)*(atanh(sqrtw)/sqrtw))
=1+(2/3)w+O(w²). Členycosh(t), t*sinh(t) a další sudé mocninyt
jsou lokálně analytické v w. Neanalytická část je přesně
−A(w)logw+3sqrtw/(1−w), do libovolného potřebného konečného řádu;
analytické koeficientové funkce u logaritmu se expandují ještě o řád
dále, aby zbytek nebyl chybně odhadnut pouze hrubým O(w²logw).

Pro koeficientový přenos je zde komplexní oblast skutečně k dispozici:
u=(1−sqrt(1−4z))/(1+sqrt(1−4z)) má |u|<1 na rovině bez řezu
[1/4,infinity). Odvozený S je tam analytický. Kořeny jednotky u
se zobrazují na tentýž kladný řez, nikoli na jiné body kružnice
|z|=1/4. V oblasti s vynechaným klínem za1/4 má t požadovaný sektor.
Lokální Mellinův rozvoj proto podporuje přenos; samotná reálná
asymptotikaD by tuto část důkazu neposkytovala.

Kořen ručně přepočetl zvlášť koeficientn^(−5/2):
3sqrtw přispívá−9/(16sqrtpi), 3w^(3/2) přispívá9/(4sqrtpi),
tedy součet27/(16sqrtpi). Logaritmický člen dává
1/n−(2/3)n^(−2)+O(n^(−3)). Catalanova normalizace má korekci−9/(8n).
Po dělení je požadovaný koeficient9/8−2/3=11/24; člen1/n se přesně
zruší. Původní +11/24 je správně a zveřejněná náhrada−13/24+1/(2n)
změní výsledek o řád n^(−1/2), větší než povolená chyba n^(−3/2).

Druhý vlastní výpočet přes celočíselnou konvoluci počtů a[n,k]
a ocasový součet aždon=100 je uložen v results/height-root-recurrence.json.
Pro n=10 dává73149/16796 a pro n=100 stejný přesný zlomek jako nezávislý
Lambertův koeficient podagenta. Úspěšný velký výpočet n=10000 se neopakoval.
Numerika je podpůrná; potvrzení stojí na předchozím obecném důkazu.

Přechod k uspořádanému stromu s přidaným kořenem má přesněN=n+1,H=h+1.
Po jeho dosazení vyjde sqrt(piN)−1/2−(1/24)sqrt(pi/N)+O(N^(−3/2)).
Posun počtu uzlů tedy také nevysvětluje zveřejněnou náhradu.

## Errata a další hranice

Čtyři vrstvy byly prohledány podle stran i charakteristických výrazů.
Zobrazená all1-prepre42 obsahuje pouze ukončovací značku odpovědi22,
nikoli opravuCMP5, a přímo obsahuje spornou náhradu z13.11.1999.
Přesné výpisy jsou v results/morris-errata-search.txt,
results/optimization-errata-search.txt a v inventáři podagenta.
Žádná pozdější opravaC0050 či změna počítané veličiny nebyla nalezena.
Citace výškových článků mají nadále vlastní přesně vyznačený stav;
správnost našeho odvození automaticky neuzavírá jejich zdrojový audit.

