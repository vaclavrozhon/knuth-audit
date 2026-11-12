# Stromy 202–207 a hlavní text 104–105

3. listopadu 2026. Celá zadání a odpovědi202–207 přečteny a zobrazeny
v knize i autorském draftu. Zdrojový průchod202–206 je dokončený.
207 zůstává **partial**: lokální příklady a algebra aktivity jsou
ověřené, obecné chování celé prohlídky mnoha kopií(92) není dokázané.
Tato mezera se neskrývá za povolené vynechání drahých benchmarků.

Nové nálezy: [F143](F143_NONBIPARTITE_TOY_MATCHING.md), nesprávné
označení obecného párování jako2DM; [F144](F144_ACTIVITY_ITEM_INDEX.md),
nesprávné číslo položky04 místo03 v příkladu aktivity. Oba mají krátký
ruční důkaz, nízkou závažnost, stejný doklad v PDF i PS. E094 je známá
oprava měření207(d), již obsažená v knize. Prvenství ani fyzický výtisk
u nových nálezů nebyly ověřeny.

## Co bylo nově přímo porovnáno

- Hlavní text104–105, PDF124–125; autor40–41, PDF46–47.
- Zadání202–203 na149 a204–207 na150; autor85–86.
- Odpovědi202–206 a207(a) na471,207(b–d) na472; autor175–176.
- Křížový odkaz na přímý součet matic: 4A, kap.7, rovnice(40),
  str.27, DjVu44. Pouze tento odkaz, nikoli celá stránka4A.
- Křížový odkaz na aktivitu v SAT Algorithm C: knižní251, PDF271,
  příslušný výklad ACT a škálování. Ostatní tvrzení stránky251 tím
  nezískávají stav dokončeného auditu.

Nový checker dekóduje **14 stromů,89 uzlů,75 hran a58 písmenných
glyfů na verzi**. Zahrnuje(91),(93), oba vstupy202 a odpověď202,
všech šest dílčích stromů203(b) a tři stromy204. Čtvercové konce
řešení jsou rozlišeny od kruhových slepých listů. Oba malé vstupy
(90),(92) jsou nově spočítány, dohromady28 uzlů na verzi; žádný dlouhý
výčet. Předchozích122 obecných stromů,14884 dvojic a10000 trojic
z results/focus_theory/verified.json se jen přebírá, bez opakování.

## Hlavní text104: malé příklady a libovolný počet kopií

Příklad(90) je nesplnitelný už paritou sedmi vrcholů; všech13 řádků
má délku2. Obsahuje trojúhelník1–4–5–1, takže nejde o2DM ve zde
definovaném významu. Správně X2C: **F143**. MRV nejprve volí0,
pak v každé větvi třícestné rozdělení. Přímá kontrola celého tvaru
souhlasí se všemi19 zdrojovými uzly(91).

Pro n≥1 nezávislých kopií, s položkami komponent v uvedeném pořadí,
MRV nejprve vyčerpá n dvoucestných kořenů. To vytvoří2^n−1 vnitřních
uzlů. U každého z2^n stavů pak zpracuje devítiuzlový zbytek první
komponenty a zjistí nesplnitelnost. Celkem10·2^n−1 uzlů.
Přednost celé první komponentě by skutečně stačila na19 uzlů.

Příklad(92) má11 možností,9 uzlů a jediné řešení, tvořené01 a2345.
Po každé z kořenových voleb má zbytek4uzlový strom. Po01 je jeden
z jeho tří listů řešením, po02 jsou všechny slepé. Souhlasí všech9
uzlů i označený prostřední list v levé větvi(93).

Při n nezávislých kopiích opět nejprve vznikne úplný binární úsek.
Je-li první kořenová volba02 v komponentě j (číslujeme j=1,…,n),
zbytek má3j+1 uzlů a takových kořenových slov je2^(n−j). Slovo samých
01 má3n+1 uzlů. Proto

    (2^n−1)+sum_{j=1}^n 2^(n−j)(3j+1)+(3n+1)=8·2^n−7.

Při dokončování komponent po jedné nahrazujeme jejich jediný úspěšný
list dalším devítiuzlovým stromem:8n+1 uzlů. Poznámka o „moderních
počítačích“ a n≈30 je kvalitativní dobový komentář, nikoli univerzální
časová garance; žádný nový výkonový test tím není tvrzen.

## Hlavní text105: definice a dominance

Přímý součet incidenčních matic má nulové mimodiagonální bloky,
takže operace v jedné komponentě nemění délky položek druhé. MRV
volí menší ze dvou kořenových stupňů, při rovnosti první komponentu.
Tím se obecně odvodí obě větve(96) i neutrální úspěšný list v(95).
Prázdný neúspěšný list má stupeň0, úspěšný stupeňnekonečno.
Číslování a popisky(94–96) byly přímo porovnány v obou verzích.

Dvojice uzlů určuje stav obou zbytkových stromů. Při každém kroku
se změní právě jedna souřadnice; párový uzel má stupeň minima.
Páry se nemohou opakovat na různých cestách: od kořenů ke zvolené
dvojici jsou obě souřadnicové cesty jednoznačné a jejich prokládání
určuje pravidlo stupňů a levé remízy. Formulace o předcích proto platí.

V(91) dominují kořen stupně2 a jeho dvě děti stupně3, celkem3 uzly.
V(93) navíc úspěšný list stupněnekonečno, celkem4.

Tvrzení o minimální dominanci u dam má krátký důkaz: po k volbách
má každá aktivní řádková položka nejvýše n−k možností; kořenové
minimum je n. Sekundární diagonály se pro minimum nevybírají.

Pro Langfordovy páry je kořenové minimum n−1, dosažené číselnou
položkou n. Po k vybraných dvojicích zbývá největší nepoužité číslo
j≥n−k. Je-li j=n, jeho délka už od počátku nepřesahuje n−1.
Jinak j≤n−1 a graf možných dvojic vzdálenosti j+1 na2n pozicích
nemá izolované vrcholy. Obsazených2k pozic proto odstraní alespoň
k z původních2n−j−1 možností pro j. Zbývá nejvýše
2n−j−1−k≤n−1. Žádný vnitřní uzel tedy nepřekročí kořenové minimum.
Případ n=1 má již neúspěšný kořen, a je triviální. Nejde o tvrzení
vyvozené pouze z konečného Langfordova výčtu.

## 202: konkrétní součet i všechny popisky

Levý strom má9 uzlů a úspěšné listy d,h, pravý7 uzlů a úspěšný list F.
Při rovnosti se pokračuje vlevo. Výsledek má21 uzlů,20 hran a právě
dvě řešení dF,hF. Pro každý uzel checker porovnává dvojici písmen,
pořadí dětí i označení řešení s přímým rekurzivním provedením(95–96).
Odpovídá všech42 písmen odpovědi a16 písmen zadání, v obou verzích.
Starší poznámka u X203, že obrázek202 není ověřen, zůstává archivem
dřívějšího rozsahu; nový X202 tento obrázek samostatně uzavírá.

## 203: asociativita a nekomutativita

U tří stromů obě uzávorkování zvolí nejlevější kořen s globálně
nejmenším stupněm. Indukce přes součet zbývajících výšek dokáže
shodu všech uspořádaných větví; úspěšné listy jsou neutrální.
Stejný důkaz platí přes přímý součet matic, jak uvádí kniha.

Vytištěný protipříklad používá neúspěšné unární řetězce délky2 a3
uzly. Jejich součet v prvním pořadí skončí po2 uzlech, v opačném
po3, protože opakovaná levá remíza dovede první složku na stupeň0.
Všech šest nakreslených řetězců a obě rovnosti byly přímo dekódovány.
To je jiný konkrétní svědek než starý test s úspěšným listem; oba platí.

## 204–206: obecné důkazy

Je-li dvojice(a,b) dominantní, při opuštění každého vlastního předka
a_k byl stupeň tehdejšího páru přesně deg(a_k), a tedy menší než
min(deg(a),deg(b)). Proto je a dominantní; symetricky b.
Obrácená implikace neplatí. Vytištěný levý strom má unární kořen,
za ním binární uzel se dvěma slepými listy. Pravý je unární kořen
se slepým listem. Po prvním levém kroku jsou obě složky dominantní,
ale dvojice má stupeň1 stejně jako původní kořen. Výsledný součet
je tříuzlový řetězec. Celý tento obrázek byl zkontrolován.

Pro Lemma D vezměme hypotetický pár(a,b), v němž ani jedna složka
není dominantní. Maximální stupně A,B na jejich cestách se už
vyskytly na vlastních předcích. Při opuštění levého předka stupně A
musel mít pravý aktuální uzel stupeň≥A, tedy B≥A. Při opuštění
pravého předka stupně B musel mít levý uzel stupeň>B, tedy A>B.
Spor. Nekonečný stupeň nevadí, protože úspěšný list je dominantní.
Tento přímý důkaz doplňuje porovnání podrobného knižního důkazu
pomocí minimálního l+l'. Žádná chybějící opačná nerovnost nenalezena.

V206 všechny neúspěšné uzly minimálně dominantního T mají stupeň
nejvýše kořenový. Je-li ten≤kořenového stupně T', algoritmus nikdy
nepřejde do T' před úspěchem v T. Výsledkem je tedy přesně nahrazení
každého úspěšného listu T kopií T'. Platí i pro samotný úspěšný
nebo neúspěšný kořen. Dřívější obecné důkazy a14884 párů se nemění.

## 207(a,b): skóre a škálovaná implementace

Pro LEN(j)=0,1,2,3,4 vychází po řadě preference j,j,j,remíza,i.
Konkrétně poslední dva případy dávají3=3 a7/2<11/3. Mu=0 přidá1
všem stupňům≥2 a ponechá0,1, tedy zachová pořadí MRV i remízy.
Pro μ≥0 zůstávají nulové a jednotkové větve před každou větví stupně≥2.

V přesné aritmetice je invariant alpha_i=ACT(i)/BUMP. Posun hodin
BUMP←BUMP/ρ vynásobí každý podílρ. První změna položky v daném
tiknutí ACT←ACT+BUMP přidá1; STAMP brání dvojímu přičtení za stejný
čas. Společné dělení všech ACT a BUMP stejnou kladnou konstantou
podíly nemění. Pro 0<ρ≤.999 je geometrický součet nejvýše1000,
jak odpověď uvádí. ACT a STAMP se při backtrackingu **nevracejí**
k dřívějším hodnotám; mají měřit skutečnou historii výpočtu.

Časy se posouvají na začátku X4,X5,X6,X7; při pokrývání, odkrývání
a změně LEN se zaznamená událost dané položky. Po prvním X4 a X5
proto vyjdou přesně alpha00=alpha02=ρ, alpha01=1+ρ a popsané
jednotkové aktivity dalších změněných položek. U(90) je to04,05,06;
u(92)03,04,05. Odkaz na obdobné škálování SAT Algorithm C je správný.

Toto je algebraický důkaz schématu. Úplný implementační audit IEEE
zaokrouhlování, podtečení a přetečení32bitového času se zde netvrdí.
Při případné realizaci je potřeba výslovně rozhodnout, jak řešit staré
STAMP při oběhu hodin; samotný důkaz invariantu používá rozlišené časy.
Nejde zde o nově potvrzený nález ani o provedený dlouhý časový test.

## 207(c): co lokální argument dokazuje

U(90) po první volbě01 má položka05 stupeň3 a aktivitu1, zatímco
nová komponenta má dvoucestný kořen s aktivitou0. Preference aktuální
komponenty tedy platí pro μ>1/2. Po libovolné další zvolené dvojici
zbývají tři vrcholy; existuje stupeň≤2, který má kladnou čerstvou
aktivitu, nebo již0/1. Jeho klíč je menší než3, takže novou komponentu
nezačínáme. Po dokončení druhé kořenové větve02 stále existuje položka
05 nebo06 s aktivitou≥1 a stupněm3. Celý neřešitelný první blok se
tedy dokončí bez dotyku ostatních. Počet uzlů je omezen konstantou
nezávislou na n; skenování položek ovšem může stát O(n) na uzel.

U(92) po01 jsou stupně02,03,04,05 rovny3,4,5,4. Třícestné02 má
aktivituρ a překoná čerstvou dvoucestnou komponentu pro μ>1/(2ρ).
Čtyřcestné03 a05 mají aktivitu1 a překonají ji pro μ>1. Text ale
uvádí04, jehož stupeň je5 a podmínka je μ>3/2: **F144**.

Každá volba řádku po následném rozvětvení uvnitř této komponenty
buď lokálně dokončí jediné řešení, nebo zanechá okamžitě nulovou
položku. To vysvětluje průchod dosud nedotčenými komponentami.
Po návratu z dalších komponent ale jejich aktivity nejsou nulové.
Kniha přechází k tvrzení o celé prohlídce a vysvětluje preferenci
položek k3. **Obecnou mez pro libovolné n a uvedené parametry při
této historii zatím nemáme.** Malý experiment by nebyl náhradou důkazu;
část(c) pro(92) proto ponecháváme otevřenou, nikoli potvrzeně chybnou.

## 207(d): známá oprava a povolené vynechání dlouhého měření

Kniha uvádí212 řešení, běžný Algorithm X92G mems a54M uzlů;
modifikace při μ=1/8,ρ=.99 má51G mems a26M uzlů, při μ=1/2,ρ=.9
pak62G mems. Draft má pro základní běh96G/55M. Publikovaná změna
6.11.2020, Fascicle5 str.280, opravuje právě96→92 a55→54: **E094**.
Zobrazená strana14 úplných errat to potvrzuje. Nejde o nový nález.

V souladu s pokynem uživatele z3.11.2026 **nespouštíme tři velké
výčty Y-pentomin jen kvůli této rychlostní tabulce**. Výkonnostní
čísla, všechny212 modely a relativní úspora z těchto konkrétních běhů
zde nejsou nezávisle reprodukované. Záznam v registru má verified:false,
konkrétní údaje, dostupné zdroje a důvod. Samotné vynechání nemusí
bránit dokončení auditu; otevřená matematická mezera207(c) tím nezmizí.
Samostatná formulace a vážený počet z úlohy208 budou další blok.

Poznámka o typické aktivitě blízko1/(1−ρ) je heuristická: přesný
geometrický limit nastává při změně položky v každém tiknutí. Při
méně častých událostech je aktivita nižší. Jako obecnou rovnost ani
záruku zrychlení ji kniha neformuluje, takže nevzniká další erratum.

## Errata, zachování starých výsledků a pokračování

Šest relevantních vrstev errat, včetně originálního TeXu4B aFascicle5,
prohledáno podle obou číslování, stránek i obsahových výrazů. F143/F144
nemají nalezenou opravu. Souvislá změna207(d) je E094. Novější
bitově shodný archiv Fascicle5 je doložen živým porovnáním z předchozího
bloku; nestahovali jsme znovu stejné soubory.

770 již přijatých programů zůstává zmrazených. Nový zdrojový checker
nejprve narazil na dvě kolineární hrany vykreslené jedním segmentem
a poté na zvláštní glyfy číslic v draftu; obě věci opraveny před
přijetím výsledku. Žádný obecný starý výčet se neopakoval.
Další blok208–214 zahrnuje Y-pentomina a lokální výměny.
