# Důkazy a řešení §2.3.2

Zde **strom** znamená konečný neprázdný zakořeněný strom s uspořádanými
dětmi. **Les** je uspořádaná posloupnost takových stromů, případně prázdná.
**Binární strom** má u každého uzlu zvlášť levý a pravý podstrom, které
mohou být prázdné. **Preorder** navštěvuje nejprve rodiče a potom jeho
děti zleva; **postorder** nejprve děti a potom rodiče. Binární **inorder**
navštěvuje levý podstrom, kořen a pravý podstrom. Podobnost znamená stejný
uspořádaný tvar; ekvivalence navíc zachovává hodnoty INFO v odpovídajících
uzlech. Obecné důkazy níže nepoužívají konečné testy jako své premisy.

## Převod a průchody: hlavní text, úlohy 1–10

**1. Vzájemně inverzní definice.** Pro les F = (T1,T2,...) definujme B(F)
prázdný pro prázdný F; jinak má kořen T1, levý podstrom B(děti(T1)) a
pravý podstrom B((T2,...)). Inverze pro neprázdný binární strom b je
F(b) = ((kořen(b), F(levý(b))), následováno F(pravý(b))). Pro prázdný b
je F(b) prázdný. Obě rekurze volají pouze struktury s méně uzly.
Současná indukce podle počtu uzlů dává F(B(F)) = F a B(F(b)) = b:
kořen zůstává stejný, indukční předpoklad obnoví jeho děti i zbytek lesa.
Jde tedy o bijekci včetně prázdných struktur. Jeden obyčejný strom
odpovídá neprázdnému binárnímu stromu s prázdným pravým podstromem kořene.
Po odebrání přidaného kořene/listové hlavy dostáváme bijekci stromů
s n+1 uzly a binárních stromů s n uzly.

Otočení obrázku o 45 stupňů po směru hodinových ručiček je názorná
pomůcka k této definici, nikoli další podmínka bijekce. Příklad (1)–(6)
dává preorder A B C K D E H F J G a postorder B K C A H E J F G D.

**Průchody v hlavním textu.** Rekurence preorder(F) je kořen T1,
preorder(děti T1), preorder(zbytek F). To je přesně binární preorder
B(F). Rekurence postorder(F) je postorder(děti T1), kořen T1,
postorder(zbytek F), tedy binární inorder. Rovnosti pro obě části
rekurence plynou indukcí. Pravá vlákna (odkazy nahrazující chybějící
pravý podstrom) tak poslední dítě vedou k rodiči, což je jeho následující
uzel v postorder; poslední kořen lesa vede k listové hlavě.

**2. Deweyho zápis.** Pozitivní celá čísla a1.a2....ak určují pořadí
kořene v lese a potom pořadí dítěte v každé rodině. Binární cesta začíná
jedničkou, levá hrana připisuje 0 a pravá 1. Odpovídající slovo je
`1^a1 0 1^(a2-1) ... 0 1^(ak-1)`, kde `1^j` znamená j opakování
znaku 1, nikoli číselné mocnění. První rodina potřebuje a1−1 pravých
kroků za počáteční 1; každá další potřebuje jeden levý krok a ai−1
pravých. Počet nul je k−1. Například 2.2.1 dává 11010.

**3–4.** Deweyho cesty seřazené lexikograficky podle čísel dávají
preorder, když kratší počáteční úsek předchází svým prodloužením.
Postorder vznikne, když kratší úsek následuje až za nimi. U prvního
odlišného čísla obě pořadí navštíví nejprve menší větev; v případě
počátečního úseku rozhoduje pořadí rodiče a potomka. Tím jsou pokryty
všechny dvojice různých uzlů. Cesty různých listů nejsou počátečními
úseky jedna druhé, takže relativní pořadí listů je v obou průchodech stejné.

**5. Opačná orientace odkazů.** Alternativní binární kořen je kořen
posledního stromu lesa; levý podstrom reprezentuje předcházející stromy,
pravý podstrom děti posledního stromu. Binární inorder tedy dává
preorder lesa a binární postorder dává postorder lesa. Indukční důkaz
opět porovnává tři části definice: předchozí stromy, poslední kořen,
jeho děti. Pořadí dětí se v těchto rovnostech neobrací.

**6.** Původní binární strom T lze považovat za obyčejný uspořádaný
strom vynecháním prázdných podstromů; jeho převod označme T'. Definice
obyčejného preorder je stejná jako binární preorder T, a obyčejný
postorder stejný jako binární postorder T. Předchozí důkaz proto dává
pre(T) = pre(T') a post(T) = in(T'). Platí to i pro uzly s jedním dítětem.
Obecná rovnost zbývajících dvou průchodů neplatí: pro kořen a se dvěma
listy b,c je in(T)=b,a,c, kdežto post(T')=c,b,a.

**7.** Částečné uspořádání požaduje, aby každý předek předcházel svým
vlastním potomkům. Preorder i obrácený postorder toto splňují podle
definice; postorder a obrácený preorder nikoli. Pro záporné odpovědi
stačí strom s jednou hranou. Les tvořený jen listy samozřejmě vyhoví
všem čtyřem pořadím; otázka žádá obecnou platnost, nikoli vyloučení
takových degenerovaných příkladů. Obrácený preorder se rovná postorder
zrcadlově obráceného lesa.

**8. Stromové uspořádání.** Značme `<` ostré uspořádání hodnot INFO a
`<=` jeho neostrou verzi. Porovnáváme nejprve kořenové INFO; při jejich
rovnosti porovnáváme posloupnosti dětských stromů lexikograficky, přičemž
vlastní počáteční úsek je menší. Přesně: je-li k délka nejdelšího
ekvivalentního počátečního úseku dvou seznamů délek n,n', pak levý strom
je nejvýše pravý právě když k=n, nebo když k<n, k<n' a jeho (k+1)-ní
podstrom je menší než pravý. V druhé větvi nemohou být podstromy
ekvivalentní z maximality k, proto lze použít i neostré porovnání.
Rozvinutí B na dětský les dává stejnou posloupnost srovnání jako
§2.3.1-25: kořen, levý podstrom, pravý podstrom. To dokazuje požadovanou
reformulaci i linearitu na třídách ekvivalence.

V tištěné odpovědi není explicitní mez k<n' před indexem T'_(k+1).
Při čtení s implicitním požadavkem existence obou indexů jde o běžné
lexikografické pravidlo. Při doslovném čtení bez této konvence je výraz
pro n>n'=k nedefinovaný. Tento redakční detail zaznamenáváme v TRIAGE.md,
odděleně od tří strojových a časových reportů.

**9.** V neprázdném lese má každý vnitřní uzel právě jedno poslední
dítě; jeho pravý odkaz je v nevlákněné reprezentaci nulový. Navíc jej má
kořen posledního stromu lesa. Všechny ostatní uzly mají pravého sourozence.
Tato bijekce dává počet nulových pravých odkazů = počet vnitřních uzlů + 1.
Prázdný les je nutno vyjmout: obě čísla jsou tam nula.

**10. Jednoznačnost podle stupňů.** Stupeň d(u) je počet dětí uzlu u.
V preorder začíná podstrom v u jedním nevyplněným místem. Zpracovaný
uzel toto místo spotřebuje a otevře d(u) nových, takže změna je d(u)−1.
Konec tohoto podstromu je první prefix začínající v u, jehož součet
d−1 je −1; na všech dřívějších prefixech je počet nevyplněných míst
kladný. Tím se jednoznačně určí rozsah podstromu i jeho dětských bloků,
rekurzivně až k listům. Po uzavření jednoho stromu začne další strom
lesa. Dvě existující lesní struktury jsou tedy podobné právě když mají
stejný počet uzlů a stejnou posloupnost stupňů v preorder; ekvivalentní
jsou právě když navíc souhlasí posloupnost INFO. Implementace
`degree_decode` je explicitní rekonstrukce. Bez předpokladu platné
posloupnosti musí parser odmítnout nedostatek zbývajících uzlů.

## Algebraické stromy a diferenciátor: hlavní text, úlohy 11–17

**Reprezentace.** Každý uzel má dva MIXové wordy. První obsahuje v
znaménku RTAG (záporné znamená vlákno), RLINK v bytech 1:2, TYPE v
bytu 3 a LLINK v bytech 4:5. Druhý obsahuje INFO. TYPE=0 je celá
konstanta, TYPE=1 neprázdné abecední jméno proměnné, TYPE=2 až 8 jsou
ln, neg, +, −, ×, /, ↑. LLINK ukazuje na první dítě. RLINK je u všech
dětí kromě posledního odkaz na dalšího sourozence, u posledního vlákno
na rodiče. Samostatný podstrom smí mít ve svém kořeni libovolný RLINK
i RTAG; ty patří jeho vnějšímu kontextu. Hlavy Y a DY, vstup, volné
uzly, program i jeho pomocná data musejí být navzájem disjunktní.

Strom hlavního příkladu má kořen −, levé dítě ×(3,ln(+(x,1))) a pravé
dítě /(a,↑(x,2)). Pořadí v rovnicích (8),(9) je přesně preorder a
postorder tohoto stromu. Arity operací umožňují jednoznačné čtení
prefixového i postfixového zápisu; `neg` odlišuje unární znaménko od
binárního odčítání.

**11.** Strom pro y=e^(−x²) je `↑(e,neg(↑(x,2)))`, šest uzlů plus
hlava Y. Rodičovské hrany jsou ↑outer→e, ↑outer→neg, neg→↑inner,
↑inner→x, ↑inner→2. Pravé skutečné odkazy jsou e→neg a x→2; poslední
děti neg, ↑inner, 2 mají vlákna na své rodiče. Vnější ↑ má vlákno na Y.
Obrázek `images/exercise11.svg` zobrazuje oba tvary; přesné odkazy jsou
také v `results/exercise11.json`.

**Diferenciační pravidla a domény.** Pravidla (11)–(19) plynou z
derivace konstanty, součtu, součinu, podílu a řetězového pravidla.
Pro mocninu použijeme u^v=exp(v ln u), odkud
D(u^v)=D(u)*(v*u^(v−1))+((ln u)*D(v))*u^v. Jako reálný důkaz to
vyžaduje u>0; podíl vyžaduje nenulový jmenovatel a logaritmus kladný
argument. Kniha také výslovně dovoluje chápat pravidla jako formální
přepisování. Při konstantním celočíselném exponentu lze využít širší
doménu, ale obecné pravidlo s ln u ji samo nezaručuje.

Rovnice (20) odpovídá slepé rekurzivní aplikaci těchto pravidel.
Nulové derivace, jednotkové součiny a první mocniny dávají opravenou
(21). Sběr faktorů a součtů pak dává (22). `algebra.py` sestaví slepou
derivaci, derivaci se simplifikacemi knihy i požadovaný cílový výraz
nezávisle a normalizuje je do totožného přesného tvaru.

**Invariant řízení D.** Před DIFF pro uzel P jsou celé podstromy jeho
dětí již navštíveny. U listu není žádný výsledek k vyzvednutí; u
unární operace obsahuje Q derivaci jediného dítěte. U binární operace
P1=LLINK(P) ukazuje na původní levý operand, P2 na původní pravý operand,
Q1=RLINK(P1) na jeho uloženou derivaci a Q na derivaci P2. Vnitřek
obou původních operandů už má všechny své odkazy obnoveny. Jediný
dočasně přesměrovaný odkaz této úrovně je RLINK(P1), jehož původní
hodnota P2 je stále k dispozici. Nad touto úrovní mohou existovat
stejné dočasné odkazy pro levé operandy předků; řízení je nepotřebuje
k hledání dalšího uzlu uvnitř právě zpracovávaného pravého operandu.

DIFF vytvoří disjunktní strom požadované derivace podle příslušného
pravidla. D3 obnoví RLINK(P1)=P2; RTAG(P1) se nikdy neměnil a zůstává
nulový. D4 nejprve vypočte původního postorder následníka a teprve
potom případně uloží Q do pravého odkazu dokončeného levého operandu.
Má-li P pravého sourozence, další uzel je první postorder uzel jeho
podstromu; nemá-li jej, přejde se vláknem k rodiči. Tím invariant
pokračuje. Každý původní uzel se zpracuje jednou; po posledním kořeni
vede vlákno k Y. D5 připojí výsledný kořen k DY. Všechny původní
odkazy jsou v tuto chvíli obnovené, neboť všechny binární rodiče už
prošly D3. To je důkaz ukončení, správnosti i obnovení vstupu.

**TREE a MULT.** TREE0 vyjme jeden volný uzel, nastaví TYPE/INFO a
nulový LLINK. TREE1 navíc připojí jeden operand a vytvoří jeho koncové
vlákno; TREE2 vytvoří skutečný odkaz z levého operandu na pravý a
vlákno z pravého na nový kořen. Operandy jsou disjunktní a jejich
kořenové vnější odkazy nejsou součástí samostatných podstromů; proto
se nic neztratí. MULT odstraní jednotkový list a vrátí druhý operand,
nebo vytvoří součin. Porovnání musí být skutečnou rovností s konstantou
1; v tištěném MIXu selhává na záporné hranici slova, jak dokazuje
samostatný report. Uvolnění je oprávněné jen pro list TYPE=0, ne pro
operátor či proměnnou se shodným INFO.

**DIFF0–7.** Konstanty a proměnné vytvářejí 0 nebo 1. Ln a neg buď
ponechají nulový list, nebo připojí existující derivaci a případnou
kopii původního operandu. Součet a rozdíl uvolní nepotřebný nulový
list; když oba operandy přispívají, spojí oba již disjunktní výsledky.
U součinu se před spojením pořídí kopie v a u, aby žádný uzel výsledku
nebyl zároveň součástí vstupu. U podílu vzniká D(u)/copy(v) a
(copy(u)*D(v))/(copy(v)^2); DIFF5 následně odečte druhý člen. V každém
případě se používá každá nenulová derivace právě jednou a zahazují se
jen nulové či jednotkové listy. Žádný původní podstrom se neuvolní.

**12. DIFF8.** Je-li D(u) nenulové, zkopírujeme u do R. Pro konstantní
v=2 ponecháme R=u; pro jiné konstantní v jej nahradíme R^(v−1); pro
nekonstantní v vytvoříme R^(copy(v)−1). Pak první člen je
MULT(D(u), MULT(copy(v),R)). Je-li D(v) nenulové, druhý člen je
TREE(×, MULT(TREE(ln,copy(u)),D(v)), TREE(↑,copy(u),copy(v))).
Nakonec se použije DIFF4. Každá kopie má oddělenou paměť; žádný
operand se nesdílí. To realizuje (19) a zachovává invariant D.
Známý chybějící operand R v odpovědi 12 je doplněn. Tištěný strojový
test exponentu 2 má samostatně doloženou chybu pomocného přetečení.

**13. Tištěné COPY.** Pomocný uzel v řádku 068 má nulový pravý odkaz;
kopírovaný kořen se stane jeho levým dítětem. V okamžiku C3 ukazují
P a Q na odpovídající původní a nový uzel. Nově alokovaný levý uzel
má vlákno na svůj nový rodič; nově alokovaný pravý sourozenec zdědí
koncové vlákno svého předchůdce a nahradí je skutečným sourozeneckým
odkazem. TYPE a INFO se přenesou beze změny. C4 při existujícím levém
dítěti sestoupí do obou stromů, jinak výslovně nuluje LLINK kopie.
C5 postupuje po odpovídajících pravých odkazech a rozlišuje vlákna
podle znaménka nového stromu; první skutečný pravý odkaz zahájí
kopírování odpovídajícího sourozence. Po vláknu z nového kořene vede
ještě jeden krok přes pomocný uzel k nule, což přesně ukončí C6.

Indukcí po preorder každému původnímu uzlu odpovídá právě jeden nový
uzel, všechny jeho hotové odkazy mají správný protějšek, všechny
budoucí odkazy budou nastaveny při alokaci příslušného dítěte/sourozence.
Původní paměť se nikdy nezapisuje. Původní kořenový pravý odkaz se
může posledním LD1 načíst, ale potom se již nedereferencuje. Proto
smí obsahovat dočasně derivaci, jak vyžaduje D. rI2 a rI3 se obnoví;
rI4–rI6 se nemění. Po úspěchu je odebráno právě n volných uzlů.

**Vlastní COPY.** `own_programs.py` zvolí jiný postup: do privátní
fronty ukládá dvojice (původní uzel, jeho kopie). Při vyjmutí dvojice
projde rodinu původních dětí, alokuje kopii každého dítěte, spojí novou
rodinu zleva a přidá dvojice do fronty. Vždy platí, že každý nalezený
uzel má jedinou kopii, zpracované rodiny mají správné odkazy a fronta
obsahuje právě dosud nezpracované rodiny. Každý uzel má jediného
rodiče, proto se ve frontě objeví jednou. Fronta se konečně vyprázdní
a všechny rodiny jsou hotové. Zachovávají se rI2–rI6; příchozí rJ se
uloží a návrat vede na volajícího. Přesměrování COPY používá JSJ,
které příchozí rJ nepřepíše. Jde o skutečné MIX instrukce bez callbacků
do Pythonu. Cena nezávislosti je 500 slov privátní fronty, v této
konfiguraci nejvýše 250 uzlů kopírovaného podstromu.

**14. Čas tištěného COPY.** Označme n počet uzlů a a počet vnitřních
uzlů původního obyčejného stromu. V binární reprezentaci má každá
vnitřní rodina právě jednu levou hranu, tedy a levých hran; skutečných
pravých hran je n−1−a. Proto alokace levého uzlu (včetně kořene)
proběhne a+1 krát a pravého n−1−a krát. Přenos INFO a test LLINK
proběhnou n krát, nulování LLINK n−a krát. C5 má jednou každý dokončený
list a každé vracení přes vnitřní uzel plus pomocný uzel: celkem n+1.
Z C5 vystupujeme n−a krát. Zbývající inicializační a závěrečné řádky
se provedou jednou. To dává přesně počty uvedené v tištěné odpovědi.
Jejich součet je 36n+14 jednotek pro řádky 064–103, po přidání vstupu
STJ a návratu JMP **36n+17** pro úplné COPY. Volající JMP přidá 1;
COPYP1 přidá 2 a COPYP2 přidá 1. Podrobné rozdělení je v reportu.

Vlastní OCOPY má inicializaci 42, n+1 kontrol fronty po 5, n načtení
dvojice po 8, n−1 alokací dětí s navazující prací celkem
46(n−1)−4a, inicializace rodin 2a a závěr 13. Celkem je to
59n−2a+14; přesměrovací JSJ v COPY dává **59n−2a+15**, bez volajícího.
Nejde o alternativní výklad tištěného času, nýbrž o cenu jiného programu.

**15–16. Skutečné MIX DIV a PWR.** Číslované tištěné odpovědi jsou
v `programs.py` vloženy za základní program. V DIV řádky 218–224
vytvářejí první člen, 225–243 druhý člen a 244 přejde do SUB.
V PWR řádky 245–277 vytvářejí první člen, 278–296 druhý a 297
přejde do ADD. Dočasné adresy v instrukcích ukládají právě již
vytvořené kořeny; COPY zachová P/P1/P2 a TREE/MULT zachová zbývající
živé hodnoty. Šablona CON0+1 se po vytvoření v−1 znovu nuluje.
Z toho a invariantů podprogramů plyne korespondence s DIFF7/DIFF8.

Vlastní řešení v `own_programs.py` používá pojmenovaná paměťová místa
OU, OV, ODU, ODV, OT1–OT4, OR. Ta přímo představují u,v,D(u),D(v)
a mezivýsledky uvedené v odstavcích výše. Každé volání COPY, TREE
nebo MULT má stejné předpoklady a důsledek jako příslušný konstrukční
krok; mezivýsledky nejsou sdílené. Před SUB/ADD se obnoví původní
P,P1,P2. Test v=2 používá CMPA a v−1 se počítá přímo; skutečně
neuložitelný exponent zachytí JOV a vede do OVERFLOW. Vlastní program
používá rovněž opravené testy jednotky MULT.

**Meze stroje.** Všechny adresy jsou v rozsahu 0–3999 a oba wordy
každého uzlu se musejí vejít do paměti; nulová adresa znamená prázdný
odkaz. Dvoubytové indexy pojmou všechna použitá kladná čísla i rozdíly
adres pro každý radix 64–100. INFO konstanty leží mezi −(b^5−1) a
b^5−1. Hlavy, kód, šablony a volné bloky se nesmějí překrývat.
Potřebná paměť není omezena jen konečnou velikostí derivace, nýbrž
maximem současně živých mezivýsledků; při opakovaném kopírování může
být celková velikost kvadratická ve vstupu. Při vyčerpání volného
seznamu přejde knižní program do uživatelského OVERFLOW, který zde
nahrazuje HLT. Není slíbeno transakční obnovení nehotové derivace po
této chybě. Úspěšné běhy zkoušejí úplné rozdělení každého volného
uzlu na výstup nebo aktuální volný seznam, ne pouze shodu hodnoty.

**17. Vlastní zjednodušovač.** `algebra.py` pracuje s přesnými
racionálními koeficienty. Součet je normalizován na seřazený seznam
různých monomů s nenulovými koeficienty; součin na koeficient a
seřazené různé základy s nenulovými celočíselnými exponenty. Monomem
zde rozumíme libovolný již normalizovaný výraz násobený koeficientem,
nikoli jen polynom v původních proměnných. Ln a obecné mocniny mohou
tvořit neprůhledné základy. Odčítání, unární minus a dělení se převedou
na tyto operace. Stejné členy/faktory se sloučí; nuly, jednotky a
celočíselné mocniny součinů se upraví přesnými identitami. Ln(u^v)
se rozloží jen tehdy, je-li u prokazatelně kladné z explicitně zadaných
předpokladů, takže se nevnucuje neplatná obecná logaritmická identita.

Ukončení plyne ze strukturální rekurze do vlastních podvýrazů; pomocné
konstruktory zpracovávají konečné seznamy a slučují již normalizované
objekty, bez návratu do obecného přepisovacího cyklu. Konkrétní kód
používá lexikografické pořadí jednoznačných textových reprezentací jako
pevné celkové pořadí klíčů; není třeba, aby se shodovalo s číselným
pořadím INFO z úlohy 8. Každý krok zachovává
hodnotu na původní doméně; indukce tedy dokazuje správnost normalizace.
Tato konkrétní sada pravidel postačuje na požadované (20)/(21)→(22),
jak dokládá přesná shoda stromů. Neprohlašuje se úplnost pro všechny
identity elementárních funkcí ani zachování množiny bodů, kde je
výsledný kratší výraz definován; pro zachování domény musí volající
uchovat původní podmínky nenulovosti a kladnosti. To je výslovně
vymezené řešení otevřeného programového úkolu, nikoli nevyřešená úloha.

## Úlohy 18–22

**18. Seznam preorder z rodičovského pole.** Začneme jednoprvkovými
kružnicemi L[j]=R[j]=j. Pro j=n,n−1,...,1 spojíme kružnici s kořenem j
za jeho rodiče k=PARENT[j]; pro k=0 zapamatujeme kořen. U nenulového k
uložíme l=R[k], i=L[j] a přepíšeme L[j]=k, R[k]=j, L[l]=i, R[i]=l.
To je přesně spojení dvou disjunktních kružnic čtyřmi hraničními odkazy.

Invariant: zpracované rodičovské hrany tvoří les; každý jeho komponent
je v jedné kružnici v preorder a sourozenci, jejichž hrany již byly
připojeny, mají vzestupná čísla. Před zpracováním j ještě není připojena
jeho hrana k rodiči, takže j je kořen svého komponentu. Komponent
rodiče je jiný, jinak by původní orientovaný strom obsahoval cyklus.
Připojení vloží celý podstrom j bezprostředně za k a před již připojené
děti k. Ty mají větší čísla, protože se postupuje sestupně. Invariant
se tedy zachová i tehdy, má-li rodič menší nebo větší adresu než dítě.
Po n−1 spojeních je jediná kružnice v požadovaném pořadí. Čas i paměť
jsou O(n). Číselný příklad přesně dává pole i kořen 4 z tištěné odpovědi.
Předpokladem je platný orientovaný strom s jediným kořenem; algoritmus
není současně validátorem obecného pole s cykly.

**19. Volný svaz.** Term je proměnná nebo aplikace `meet` (průsek,
značka ∧) či `join` (spojení, ∨) na dva termy. Relace G(X,Y) má
znamenat X≥Y podle šesti pravidel zadání. Algoritmus nejprve rozdělí
levý meet konjunkcí, jinak pravý join konjunkcí; v případě levého
join a pravého meet použije disjunkci čtyř menších dvojic; v případech
proměnná/meet a join/proměnná disjunkci dvou dvojic; nakonec porovná
jména proměnných. Každé rekurzivní volání zmenší součet počtů uzlů.
Pokud jsou zároveň levý meet a pravý join, obě možné priority vedou
ke konjunkci stejných čtyř dvojic, takže pravidla nekolidují.

Silná indukce podle součtu velikostí nyní dokazuje, že vrácená booleovská
hodnota je přesně G. Ukládáním už spočtených dvojic podtermů se každá
z nejvýše m*n dvojic vyhodnotí jednou, přičemž má nejvýše čtyři přímé
závislosti. S identifikátory uzlů je čas i paměť O(m*n); zásobník
rekurze má hloubku nejvýše m+n. Pythonová demonstrace používá jako
klíče celé neměnné termy, takže její režie hashování není zahrnuta
do této abstraktní meze. Pro implementaci s touto mezí stačí klíče
nahradit dvojicemi čísel uzlů.

Nezávislá kontrola uzavírá konečnou množinu podtermů na reflexivitu,
tranzitivitu a definiční dolní/horní meze meet/join. Když relace v
uzávěru neplatí, kvocient podle obousměrné relace tvoří konečné
částečné uspořádání s předepsanými existujícími spojeními/průseky.
Jeho doplnění pomocí řezů (množiny rovnající se dolním mezím svých
horních mezí) zachová existující spojení i průseky a poskytne svazový
protimodel. Tím se vysvětluje úplnost této druhé metody, nikoli jen
náhodná shoda dvou rekurzí. Skolemův primární text §2 na pp. 16–21
obsahuje odpovídající konečný rozhodovací postup pro svůj
„Gruppenkalkul“, tedy svazový kalkul, nikoli algebraickou teorii grup.

Pro příklad zadání X=a∧(b∨c), Y=(a∧b)∨(a∧c) je X≥Y pravda, opačná
nerovnost nepravda. Přesný protimodel opačné nerovnosti je pětiprvkový
svaz se spodkem 0, vrškem 1 a třemi různými atomy a,b,c: pak X=a a
Y=0. Tři atomy jsou navzájem neporovnatelné; spojení různých atomů je
1, průsek 0. Není potřebné spoléhat na distributivní model, který by
obě strany chybně ztotožnil.

**20.** Uzly u,v různých stromů lesa mají v obou průchodech stejné
relativní pořadí. V témže stromu, není-li jeden předkem druhého,
oddělují je dvě různé větve jejich nejnižšího společného předka; ty
se opět v obou průchodech zpracují zleva stejně. Je-li u vlastním
předkem v, předchází mu v preorder a následuje ho v postorder.
Tyto případy vyčerpají všechny různé dvojice. Pro u=v neplatí ani
jedna ostrá časová nerovnost, proto je oprava „proper ancestor“ nutná.

**21. Vyšší arita.** Původní D ukládá jedinou levou derivaci do
pravého odkazu prvního operandu a pravý operand má zároveň jako
bezprostředně předcházející navštívený uzel; to se na více operandů
nepřenese pouhou změnou konstanty 2. Řetězec dočasných derivací
navržený v odpovědi je možný, ale vyžaduje další obnovování více
sourozeneckých odkazů.

Jednoduché obecné řešení nechá vstup beze změn a použije zásobník
kořenů hotových derivací. Při listu přidá jeho derivaci; při operátoru
arity d odebere posledních d kořenů, obrátí jejich pořadí do pořadí
operandů, vytvoří derivaci operátoru a vloží její kořen zpět. Vazby
zásobníku smějí být v kořenových RLINK hotových výsledků, které jsou
mimo jejich vlastní podstromy. Po každém postorder kroku zásobník
obsahuje právě výsledky úplných podstromů dosud nespotřebovaných
rodičem; indukce dává správnost pro libovolné konečné arity. Výsledná
hlava se připojí teprve na konci. Tím je podána explicitní obecná
technika odpovídající odkazu knihy na §2.3.3; sousední sekce se zde
znovu neaudituje.

**22. Vložení stromu.** Vložení je injektivní zobrazení zachovávající
preorder i postorder. Jeho složení je opět vložení. Vzájemná vložitelnost
vynutí stejný počet uzlů a bijekci zachovávající předky i relativní
pořadí nesrovnatelných uzlů podle úlohy 20; oba stromy tedy mají stejný
uspořádaný tvar. Zmíněné částečné uspořádání se chápe na těchto tvarech,
nikoli na identitách paměťových adres či na neporovnávaných hodnotách INFO.
Jednouzlový strom
se vloží do libovolného neprázdného stromu. Levý krajní podstrom l(T')
i zbytek r(T') po jeho odebrání mají v T' stejné relativní pořadí
svých uzlů; vložení do kterékoli z těchto částí tedy stačí.

V posledním dostatečném případě vezmeme vložení f_l z l(T) do l(T')
a f_r z r(T) do r(T'). Kořen T pošleme na kořen T', uzly l(T) pomocí
f_l a ostatní uzly pomocí f_r. Obrazy těchto dvou skupin jsou
disjunktní. Žádný nekořenový uzel r(T) se nemůže zobrazit kořenem T':
zachování obou průchodů by z něj učinilo předka obrazu kořene r(T),
což je nemožné. Přesunutí obrazu kořene výše na kořen T' tedy zachová
injektivitu. Preorder má bloky kořen, l(T), zbývající les; postorder
bloky l(T), zbývající les, kořen. Obrazy leží v týchž blocích T', a
uvnitř bloků pořadí zachovávají f_l,f_r. To dokončuje důkaz implikace.

Obrácení neplatí. T je kořen se třemi listy; T' je kořen, jehož první
dítě má dva listy a druhé dítě je list. Kořen T mapujeme na kořen T'
a tři listy na jeho tři listy zleva. Oba průchody jsou zachovány.
T se však nevejde ani do l(T') se třemi uzly, ani do r(T') se dvěma;
r(T) má tři uzly, takže se také nevejde do r(T'). Nesplní se žádná
ze tří podmínek. Jde přesně o lokální tvar b,b' z obrázku 25.

## Úloha konečných kontrol

`check_trees.py` prošel 2 056 lesních tvarů do osmi uzlů, 118 621
dvojic pro test vlastního předka, 32 055 očíslovaných vstupů rodičovského
algoritmu do šesti uzlů a 4 225 dvojic pro dostatečnou podmínku vložení.
Část rodičovských polí se může opakovat po různém výchozím uspořádání;
číslo je počet ověření, nikoli počet různých orientovaných stromů.
`check_tree_orders.py` navíc kontroluje úlohu 6 na 2 055 neprázdných
binárních tvarech a úlohu 8 na 10 404 dvojicích stromů s INFO v {0,1}.
`validate_mix.py` porovnává skutečný MIX s bezukazatelovou rekurzí,
kontroluje obnovení vstupu, vlákna, disjunktnost a všechny volné uzly.
Konečné rozsahy, seed a výsledky jsou v `results/*.json`. Doménově
nedefinované numerické příklady zjednodušovače jsou výslovně vynechány
a spočteny; nejsou vydávány za úspěšné numerické kontroly.
