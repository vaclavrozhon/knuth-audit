# Souvislý průchod §2.3.2 — 5. listopadu 2026

X0971 zahrnuje první dotisk 1997, tištěné334–348 a odpovědi571–575
(soubor +15). V aktuálním průchodu byly přečteny celé originální obrazy,
všechny obrázky, programové tabulky,22 zadání a jejich odpovědi. Začátek
§2.3.3 na348 a jeho odpovědi na575 ještě neuzavíráme. Dřívější úplné
důkazy v `parallel/binary-tree-representation/PROOFS.md`, zdrojová evidence
a kořenové revize `completed-tree-blocks-root-review.md` a
`tree-findings-root-review.md` byly porovnány s originály. Přijaté konečné
testy nebyly znovu spuštěny.

## Reprezentace a pořadí

Pro les F=(T1,T2,...) má B(F) kořen T1, levou větev B(děti T1)
a pravou B(zbytek F). Prázdný les odpovídá prázdnému binárnímu stromu.
Inverze sestaví první obyčejný strom z kořene a inverze levé větve,
za něj připojí inverzi pravé. Obě složení jsou identická indukcí podle
počtu uzlů. Samostatný neprázdný strom odpovídá binárnímu stromu
s prázdnou pravou větví kořene; přidání hlavy dává bijekci n binárních
uzlů a n+1 obyčejných uzlů.

Preorder lesa je preorder B(F), postorder lesa je inorder B(F).
Obrázky334–335 pro A(B,C(K)),D(E(H),F(J),G) dávají posloupnosti
A B C K D E H F J G a B K C A H E J F G D. Zkontrolovány všechny
nitě v obrázku335: B vlevo k hlavě; K vlevo k B a vpravo k C;
C vpravo k A; H vlevo k A a vpravo k E; J vlevo k E a vpravo k F;
G vlevo k F a vpravo k D; D vpravo k hlavě. Poslední sourozenec
směřuje pravou nití k rodiči, poslední kořen lesa k hlavě.
Závorkové zápisy(5),(6) a příklad obsahu knihy336 souhlasí.

Úlohy1–10: Deweyho a1.a2...ak přechází na binární cestu
1^a1 0 1^(a2−1) ... 0 1^(ak−1), např.2.2.1→11010. Lexikograficky
porovnáváme číselné složky, nikoli desetinné řetězce. Rozhodnutí,
zda prefix předchází svému prodloužení, rozlišuje pre/postorder;
cesty různých listů nejsou prefixem jedna druhé. Opačné uložení
sourozenců/dětí dává inorder binárního stromu=preorder lesa a binární
postorder=postorder lesa, bez obrácení rodin.

Považujeme-li binární T za obyčejný strom a znovu převedeme na T',
platí pre(T)=pre(T'), post(T)=in(T'). Pro kořen a a listy b,c je
in(T)=b,a,c, zatímco post(T')=c,b,a, takže další obecná rovnost neplatí.
Předci předcházejí potomkům právě v preorder a obráceném postorder;
opačné varianty vyvrací jediná hrana. Porovnání stromů v úloze8 je
lexikografické podle INFO a seznamu dětí. Po společném prefixu délky k
je podmínka k=n nebo (k<n a k<n' a T[k+1]≤T'[k+1]). Tištěná odpověď
572 neuvádí k<n' výslovně. Zachováváme dřívější čtení s implicitní
existencí indexovaných podstromů; nejde o nově potvrzenou algoritmickou
chybu. Výslovná mez je v našem důkazu zaznamenána.

Odpověď9 na572 **výslovně požaduje neprázdný les**. Nulové pravé
odkazy odpovídají posledním dětem všech vnitřních uzlů plus poslednímu
kořeni. Pro prázdný les jsou obě počítané množiny prázdné; nelze proti
této odpovědi namítat případ n=0. Úloha10 rekonstruuje podstrom prvním
prefixem se součtem (stupeň−1)=−1; další bloky jednoznačně určují les.

## Symbolická derivace a MIX

Typy0–8, dvouslovný formát, všechny uzly a pořadí(8),(9) na337
souhlasí. První slovo nese RTAG, R, TYPE a L, druhé INFO. Kořenové R
je kontextový odkaz, nikoli součást podstromu; to dovoluje jeho dočasné
použití pro uloženou derivaci. Kód, šablony, vstupní a výstupní hlavy,
živé uzly a volný seznam musejí být disjunktní. Adresa0 je null, oba
wordy uzlu se musejí vejít do0–3999.

Pravidla(11)–(19) jsou správné formální identity. Reálná interpretace
obecné mocniny vyžaduje kladný základ, logaritmus kladný argument,
podíl nenulový jmenovatel. Slepý výraz(20) obsahuje i ln(x)*0:
jeho doslovná reálná doména může být menší než doména původního výrazu.
Text338 výslovně připouští formální pojetí. Netvrdíme úplné zachování
definičního oboru ani použitelnost všech mezikroků na záporném x.
Při zachování podmínek výsledná derivace je 3/(x+1)+2a/x³.

D postupuje postorder. P1 ukazuje první dítě, Q1 jeho uloženou derivaci,
P2 původní poslední dítě, Q jeho derivaci. D3 u binárního operátoru
obnoví R(P1)=P2. D4 nejprve zjistí následující P a až poté přepíše
kontextový R právě zpracovaného levého operandu. D5 obnoví i poslední
vstupní odkazy a připojí výsledek k DY. DIFF staví disjunktní výstup;
nepotřebuje pomocný řídicí zásobník, ale velikost kopírovaných výrazů
může být kvadratická. Při OVERFLOW není slíbeno transakční obnovení.

TREE0/1/2 správně nastavují typ, INFO, dětské odkazy i poslední nit;
kořenové R nastaví volající. CONST0+1 se po výrobě exponentu v−1
znovu nuluje. ADD/SUB vracejí nadbytečné nulové listy do volného seznamu,
MULT a DIV kopírují původní operandy tam, kde je nutné zamezit sdílení.
Kontrola literálních instrukcí souhlasí s konstruktivním důkazem,
s výjimkou dvou následujících již potvrzených testů.

**C0042,345 — MULT.** Pro radix b, B=b^5 a c=−(B−1) se c vejde
do slova. Test DECA1 ale vytvoří −B a zápornou nulu; JANZ neodbočí
a TYPE=0 přijme c jako1. Derivace tříuzlového c*x je proto1 místo c.
Matematicky potřebný vstup i výsledek jsou reprezentovatelné. CMPA
CON1+1/JNE opraví oba testy rovnosti bez změny hodnoty a bez přetečení.

**C0043,574 — PWR.** Pro v=−(B−2) se v i v−1 vejdou. Pouze test
v−2 přeteče na zápornou nulu a JAZ zvolí větev v=2. Derivace x^v
je v*x místo v*x^(v−1), nezávisle na předchozí vadě MULT. Oprava
CMPA CON2+1, JE3F, DECA1 počítá skutečně potřebné v−1. Případy,
kdy je samotný výsledek mimo rozsah, vyžadují vlastní konvenci;
nejsou součástí tohoto protipříkladu.

**C0044,573 — COPY.** Uvedené četnosti dávají
6+2a+15(a+1)+3(n−1)+13(n−1−a)+11n+2(n−a)+5(n+1)+2(n−a)+4
=36n+14 pro064–103. STJ na063 a návrat104 přidají3u, tedy36n+17
pro celé COPY. Singleton trvá53u místo58u; volací JMP ani zvláštní
vstupy COPYP1/2 rozdíl nevysvětlují. Jde o chybnou konstantu, samotná
kopie, registrní kontrakt a obnova zdroje jsou správné. Podíly času
uvedené jako přibližné odpovídají četnostem.

Obecné argumenty byly znovu porovnány s originály. Dřívější1930
derivací,498 kopií a74 hraničních běhů jsou doplňkové certifikáty,
ne důkaz pro libovolný strom; nebyly znovu spuštěny.

## Zbývající úlohy11–22

11–12: e^(−x²) má šest uzlů plus hlavu; kresba a všechny nitě572
odpovídají. Ve vzorci mocniny v odpovědi12 původně chybí operand R,
což opravují veřejná errata2007.

13–16: ověřeny invariant COPY, vlastní varianta se soukromým polem,
časové součty a DIV218–244/PWR245–297. Soukromých500wordů obsahuje
250dvouslovných uzlů, což je konečný kapacitní kontrakt řešení, nikoli
neomezený algoritmus. Jeho čas59n−2a+15 zahrnuje návrat JSJ. DIFF7/8
odpovídají pravidlům mimo C0043; pomocná samomodifikovaná místa ani
kopírování nepoškozují živé vstupní registry.

17: přesný racionální normalizátor slučuje součty, součiny a stejné
celočíselné mocniny, používá pevné pořadí normalizovaných výrazů,
logaritmické pravidlo jen s doloženou kladností. Ukončení plyne ze
strukturální rekurze a konečných seznamů, nikoli z libovolného cyklu
přepisů. Požadované(20)/(21)→(22) je vyřešeno; nejde o úplný rozhodovač
všech funkčních identit. Podmínky původní domény musí uchovat volající.
Úloha je nyní checked s výslovně přeskočeným plným článkem Sammetové.

18: PARENT=(3,8,4,0,4,8,3,4) má kořen4, děti4=(3,5,8),3=(1,7),
8=(2,6), preorder4,3,1,7,5,8,2,6. Pole L=(3,8,4,6,7,2,1,5),
R=(7,6,1,3,8,4,5,2) v odpovědi souhlasí. Sestupně podle j se kružnice
komponenty j připojí hned za rodiče; menší sourozenci se vloží před
větší. j je stále kořenem nepřipojené komponenty, jinak by vznikl cyklus
v platném rodičovském stromu. n−1 spojení dává O(n), číslování rodičů
nemusí být topologické. Algoritmus není validátor libovolného pole.

19: šest rekurzivních pravidel pro volný svaz klesá podle součtu velikostí
dvojice výrazů. Překrývající se AND případy levého meet a pravého join
komutují; smíšený join/meet případ používá čtyři OR možnosti. Memoizace
má nejvýše m*n dvojic podvýrazů, s explicitním oddělením nákladů na
jejich reprezentaci. Nezávislé uzavření konečného souboru podvýrazů
a Dedekindovo–MacNeilleovo doplnění zachovávají existující meet/join,
takže poskytují oddělující modely. Distributivita se nepředpokládá:
diamant M3 dává a∧(b∨c)=a, ale (a∧b)∨(a∧c)=0. Obecný důkaz je
přijat; původní Skolemovy strany16–21 byly již přímo prověřeny.
Nedostupné plné Whitmanovy články jsou nyní bibliografická výjimka.

20: vlastní předek má menší preorder a větší postorder. Pro uzel se
sebou obě ostré nerovnosti selžou; známá oprava348 proto doplňuje
„proper“. Odpověď se čte s tímto opraveným zadáním.

21: zásobník hotových kořenů obslouží libovolnou aritu; odebere posledních
d kořenů ve správném pořadí operandů, vstup zůstává nezměněný. Knižní
varianta s dočasnými odkazy je rovněž možná při jejich následné obnově.

22: zachování obou pořadí zachovává vlastní předky a pořadí nesrovnatelných
uzlů. Složení vložení dokazuje tranzitivitu, obousměrná vložení konečných
stromů antisymetrii až na podobnost. V poslední větvi pravidla se kořen
mapuje na kořen T'; žádný uzel pravé části obrazu nekoliduje s kořenem,
protože již má vlastního předka. První dvě možnosti samy nestačí:
kořen se třemi listy se vloží do kořene s dětmi (uzel se dvěma listy,
list), ale nevejde se do levé ani pravé omezené části. Obrázek25 na348
a odpověď575 odpovídají této konstrukci.

## Fakta, bibliografie a veřejné opravy

Łukasiewiczův originál1931,p367 ukazuje prefixový Dαβ a autorovu
poznámku o nápadu1924 a dřívějším zveřejnění. To podporuje konkrétní
historické připsání; neprokazujeme globální prvenství proti všem pramenům.
Hopperové retrospektiva1978,p13 dokládá funkční diferenciátor před
Kahrimanianovou prací zkvětna1953, **ne přesné zahájení vroce1952**.
Nová rychlá rešerše našla jen opakování TAOCP; není to nezávislý důkaz.
Práce Temple1953 ani přesné strany6–14 ONR1954 nebyly získány. X0301
a hlavní text proto zůstávají partial. Také dobové tvrzení na339
o vybavenosti „most computer installations“ nebylo nezávisle doloženo.

Příklad nástupnictví336 je korektní model preorder při daném pořadí
rodin a filtru způsobilosti. Nelze však automaticky pokládat samotnou
živost za úplný právní filtr nebo pravidla koruny za pravidla všech
šlechtických titulů. Oficiální Royal Household a Act of Settlement
vymezují další náboženské a zákonné podmínky; House of Lords Library
rozlišuje běžné mužské dědění peerage a výjimky podle druhu titulu
a zakládacího aktu. Tyto konkrétní prameny byly přečteny, univerzální
tvrzení o všech dynastiích neověřujeme. Erratum2024 už příklad převádí
do historického času a vyžaduje vhodný rodokmen. Zůstává to výslovná
faktická kvalifikace na částečné336, nikoli nový právní nález.

Přeskočené plné bibliografické kontroly:

- Sammet, CACM9(8),1966,555–569, DOI10.1145/365758.365762: metadata
  ověřena, plný článek nepřístupný; matematika úlohy17 nezávislá.
- Whitman1941, Annals42(1),325–330, DOI10.2307/1969001 a1942,
  43(1),104–115, DOI10.2307/1968883: metadata/obsahy ročníků ověřeny,
  plné články nepřístupné. Nepřístupný abstrakt1939 v X0842 mezeru
  neuzavírá. Skolemův čtený původní důkaz se nezaměňuje za Whitmanův.

Čerstvý úplný výpis čtyř vrstev je v
`sources/sequential-2026-11-05/binary-representation-errata-extract.json`,
včetně hashů, tematického hledání a rozlišení hraničních stran.
Deset různých zásahů zahrnuje šest obsahových míst původní knihy:
339 jiný přesný strom výstupu při stejné algebraické hodnotě;
342 chybný registr;345 COPY2 místo COPYP2;346 chybějící pojem;
348 vlastní předek;572 chybějící operand. Právě tyto stránky jsou
mapovány červeně pod X0325. Směr45° na335 a rozšíření tree/forest337
jsou zpřesnění,336 historická aktualizace a574 nová bibliografie.
Neznamenají další chybné algoritmy. Erratum348 na začátku další sekce
a odpověď2 na575 převezme §2.3.3. C0042–C0044 v těchto vrstvách nemají
opravu. Potvrzení je závěr našich zdrojů, nikoli potvrzení od Knutha
či tvrzení o prvenství; fyzický výtisk není ověřen.

Stránky335,337,340–347 a odpovědi571–574 jsou matematicky/fakticky
prošlé v uvedeném rozsahu; již zkontrolovaná334 zůstává dokončená.
336,338,339 jsou partial pro výše přesně vymezená historická tvrzení,
348 a575 zatím pro navazující §2.3.3. Červená chyba má v UI přednost
před stavem pokrytí, ale nedělá z částečné stránky dokončenou.
