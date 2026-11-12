# Nezávislá revize: doslovná strategie na616 překročí faktor6

Pro živý rozpočet N, tedy součet délek současně rezervovaných bloků,
označme A_m(N) největší pravý konec dosažitelný doslovnou strategií
odpovědi §2.5–40 při maximální délce bloku m. Strategie vybírá
nejmenší nezáporný začátek p dělitelný a(s)=2^floor(lg s), pro který
je celý interval [p,p+s) volný. Počáteční paměť je prázdná a uvolňuje
se vždy celý živý blok; přesuny rezervovaných bloků se nepoužívají.

Přijímám matematický nález C0091:

~~~
liminf_(N→infinity) A_32(N)/N >= 4709347/783360
                            = 6+9187/783360 > 6.
~~~

Tím padá tvrzení, že právě vytištěná strategie dokazuje faktor r+1
pro maximum2^r. Knižní N(m) optimalizuje také volbu strategie;
nerovnost N(32)<=6 ani Robsonův jiný algoritmus vyvráceny nejsou.
Celá úloha40 zůstává partial kvůli dalším tvrzením a pramenům.
Není určeno nejmenší problematické maximum; konkrétně m16 zůstává
otevřené. Současně se netvrdí prvenství ani kontrola fyzického tisku.

Přečetl jsem celý obecný důkaz, zdroj generátoru, pramenné srovnání
a návrh nálezu. Vedle vlastní matematické revize jsem vytvořil
nezávislý doslovný validátor a jednou přehrál úplnou novou stopu.
Samostatný druhý pracovník zkontroloval obecný důkaz; jeho konečný
záznam je připojen v kořenovém manifestu. Neopakují se dříve úspěšné
testy a obecný závěr se neodvozuje extrapolací z konečného běhu.

Konečný druhý posudek `parallel/aligned-m32-independent-review/REVIEW.md`
jsem přečetl celý, včetně vlastního odvození konstanty, výslovných
počtů okrajů a porovnání konečné autorské verze. Jeho manifest má
SHA-256 40bbf43ab7f04acb1c442cc5fd23427e8c4397768082582b69d64e0d866ba361.
Autorský manifest má SHA-256
477678f7ec62d681208bc3f7beb9e0f702842a29ee9aa28be1c033aae42a3598.
Oba posudky potvrzují stejný matematický rozsah; druhý pracovník
výslovně nepřebírá cizí validaci stopy za svůj vlastní běh.

## Převzatý řídký ocas a základ indukce

Pro pevné m=2^(K+1) a dost velké celé h volíme n=18mh, N=n+m.
Konce etap mají objem nejvýše n; přídavek m kryje dočasnou mocninu
vloženou před půlením. O_m(log n) znamená absolutní chybu omezenou
konstantou závislou jen na m krát log n. m je po celou limitu pevné.

Přijatý X0853 dává pro a>=2, t=a+1, liché P/a a prefix blokující
všechny t-kandidáty před P ocas o kapacitě M s koncem
P+(3a/t)M+O(a log(2+M/t)). Pomocná délka je2a a objem nepřekročí
prefix plus M. Dávky počtů J přecházejí na floor((J-2)/3), dokud
J>=5, a poslední mají nejvýše4 bloky. Z velké dávky na U zůstává
levý strážce U, řetězec U+2a+3aj, 0<=j<=2floor((J-2)/3), a nejvýše
dva další pravé bloky. Každá dávka tedy přidá jeden řetězec a
konstantně mnoho okrajů. Poslední blok zachová pravou mez.

Základní prefix má jednotky na4j do n a dvojice na n+4j do5n/3;
jejich objem je7n/12. První trojkový ocas začíná na5n/3-2.
Je-li L_k koeficient konce, w_k koeficient živého objemu nové
délky a+1 a q_k koeficient souhrnu jednotek a dvojic při a=2^k,
dostáváme L_1=5/2, w_1=5/12, q_1=7/12. Dělitelnost n zaručuje
celé počty a správné fáze obou starých řetězců.

## Lokální převod a půlení

Pět bloků t=a+1 na p,p+3a,p+6a,p+9a,p+12a lze změnit na čtyři
na p,p+4a,p+8a,p+12a bez zvýšení objemu. Po odstranění p+9a
je první volba p+8a; po odstranění p+6a,p+3a je první p+2a,
další p+4a, a dočasný blok p+2a se uvolní. Před těmito novými
volbami příslušní leví strážci končí na p+7a+1, p+a+1 a p+3a+1.
Dosavadní mezera délky2a-1 neobsahuje dřívější zarovnaný t-blok:
její první zarovnaný začátek by zasáhl následující blok.

Pro p==a modulo2a se zachová přesně sjednocení obsazených slotů
[2ai,2a(i+1)). První čtyři staré bloky obsadí2,1,2,1 slotu,
první tři nové2,2,2; pravý strážce je společný. V řetězci po3a
je mezi prvními čtyřmi začátky jeden s p==-a modulo4a. Použité
skupiny mají základy po12a a provádějí se sestupně, takže nově
uvolněná t-místa leží až napravo od každé následující operace.
Zbytky na obou koncích zůstávají. Nový řetězec má krok4a,
fázi -a a objem3/4 původního s chybou O_m(log n).

Starší řetězce před půlením leží buď na2aj pro jednotky/dvojice,
nebo na2aj-b pro délku b+1, kde2<=b<a. Každý jejich blok zasahuje
právě kandidáty délky2a+1 s indexy j-1,j. Zachování sudých
**globálních** j a obou konců proto zachová celé původní sjednocení
kandidátů. Řetězec má poté krok4a, fázi0 či -b a poloviční objem
s konstantní okrajovou chybou. Pro b+1 se navíc zachová sjednocení
obsazených 2a-slotů; jednotky/dvojice tento silnější závěr nemají.

Kontrola implementace: halve_older bere first_marker=(start+offset)/(2a),
kde offset je0 nebo b. Ponechá lokální index j shodný modulo2
s first_marker, tedy právě globální sudé značky. Neponechané krajní
bloky se přesunou do inventáře okrajů, neuvolní se. Nejde o libovolnou
paritu zvolenou zvlášť v každém řetězci.

## Indukční krok, rozpočet a uniformní chyba

Na konci etapy a=2^k jsou všechny a+1-kandidáty před dalším volným
začátkem blokované. Každý celý 2a-slot před pravým koncem E musí
obsahovat živou buňku, jinak by v něm byl volný kandidát a+1.
Poslední neúplný slot obsahuje poslední živou buňku. Lokální převod
tyto obsazené sloty zachová. Proto je Q=2a*ceil(E/(2a)) první volný
slot i první volný kandidát délky2a+1.

Je-li Q/(2a) sudé, vloží se na Q blok2a a položí P=Q+2a;
jinak P=Q. Tento krok stojí nejvýše n+2a<=N a zaručí liché
P/(2a). Následné půlení všech starších řetězců zachová pokrytí
kandidátů2a+1. Okraje i vložená mocnina zůstávají. Nový prefix má

~~~
V=(1/2+w_k/4)n+O_m(log n).
~~~

Při4a<=m se připojí ocas délky2a+1 s pomocnou délkou4a do objemu n.
Tím vzniknou přesné rekurence hlavních koeficientů

~~~
w_(k+1)=1/2-w_k/4,
q_(k+1)=q_k/2=7/(12a),
L_(k+1)=L_k+(6a/(2a+1))*w_(k+1).
~~~

Nový ocas má O(log n) dávek. Každý převod přidává nejvýše konstantně
mnoho okrajových bloků na řetězec a půlení nejvýše dva. Při pevném
K tak zůstává počet řetězců i okrajů O_m(log n). Jejich délky jsou
nejvýše m. To odůvodňuje všechny objemové a délkové chyby uniformně
v h. Interval[19/48,5/12] je invariantní pro rekurenci w; kapacita
nového ocasu je proto kladná lineárně v n a pro dost velké h převáží
všechny okraje. Každý konec etapy se od n liší o méně než její nová
délka. Dočasné pomocné bloky v řídkém ocasu již kryje X0853.

V poslední etapě m=2a se po lokálním převodu půlí pouze starší
délky b+1; jednotky/dvojice zůstávají všechny. Tím se zachovají
všechny obsazené m-sloty. Prefix má

~~~
V_top=(1/2+q_k/2+w_k/4)n+O_m(log n).
~~~

Bloky m se potom vkládají na Q,Q+m,... do objemu n. Jejich konec má
koeficient L_k+1/2-q_k/2-w_k/4, ekvivalentně L_k+w_(k+1)-7/(12a).
Jde o jednu legální historii, nikoli součet oddělených maxim.

Pro k=1,2,3,4 jsou w_k rovny5/12,19/48,77/192,307/768 a L_k
rovny5/2,69/20,1627/360,69133/12240. Při m32, a16 je w_5=1229/3072,
q_4=7/96 a výsledný koeficient4709347/783360. N=576h+32 se od n
liší jen o32. Zaokrouhlení obecného rozpočtu dolů na tuto posloupnost
ztrácí nejvýše575; monotónnost A_32(N) dává uvedenou mez liminf.

## Nezávislá doslovná validace

Generátor vytváří adresy podle důkazu, ale netestuje první volbu
ani překryvy. Proto byl napsán samostatný C++ validátor, který
neobsahuje žádnou z fází konstrukce, řetězcové rekurence ani makra.
Vede bitovou mapu skutečně obsazených buněk a délku bloku na každém
živém začátku. Pro každou délku1..32 vede také všechny zarovnané
volné kandidáty. Hierarchická bitová shrnutí umožní přesně vybrat
nejmenšího kandidáta bez meze na počet prohledaných adres.

Po změně intervalu[p,p+s) se pro délku t a zarovnání a(t) přepočítají
přesně kandidáti s indexy od max(0,floor((p-t)/a(t))+1) do
floor((p+s-1)/a(t)), omezení jen pravou hranicí celé sledované paměti.
Tato nerovnost je ekvivalentní průniku obou polouzavřených intervalů.
Volnost se vždy znovu určí z buněk, nikoli z dřívější předpovědi.
Každá rezervace musí souhlasit s první volbou, být nepřekrývající
a nepřekročit N. Každé uvolnění musí odpovídat celému živému bloku.

Sledovaný rozsah je maximum všech zaznamenaných konců. Omezení
nezakryje menšího kandidáta téže délky: má-li menší začátek, má i
menší konec než ověřovaný záznam, a leží tedy v rozsahu. Kandidáti
napravo od zaznamenaného místa nemohou ovlivnit první volbu.

Nový validátor prošel dvěma ručně zadanými legálními historiemi
včetně přechodu přes hranici64 bitů a tří pater shrnutí. Pět dalších
historií správně odmítl: ne první místo, překryv, nesprávný celý blok
při uvolnění, překročení rozpočtu a přehlédnutou dřívější mezeru.
Poté jednou ověřil celou novou stopu pro r5,h2048:

| veličina | nezávislý výsledek |
|---|---:|
| počet operací | 5 554 555 |
| rezervace / uvolnění | 2 851 455 / 2 703 100 |
| největší délka | 32 |
| dovolený živý objem N | 1 179 680 |
| skutečný největší živý objem | 1 179 648 |
| poslední začátek a délka | 7 088 896 a32 |
| největší pravý konec | 7 088 928 |
| 6N | 7 078 080 |
| přesah | 10 848 |

Běh trval20,5 sekundy. Zdroj, vstup, výstup a příkaz jsou vázány
SHA-256 v záznamu běhu; stopa má SHA-256
6afccbdd66dcbedada0d78f62d8a0a264c3f4e2378957c315a7e3cce580dbdca.
Konečný důkaz se doplňuje s obecnou indukcí; sám konečný přesah by
neprokazoval asymptotické porušení.

Metadata generátoru v mezifázi before_tail používají end pro první
nový začátek P, nikoli vždy pro fyzický konec E. Konečné end a peak
jsou správně ověřené. Archivovaný parser připouští r8, avšak bytearray
neumí délku256; deklarovaný běh je výhradně r5 a délky nejvýše32.
Původní metadata s tehdejším awaiting-status jsou zachována, pozdější
úspěch eviduje samostatný výstup. Tyto kvalifikace nemění obecný důkaz.

## Zdrojová kolace a rozsah opravy

Přímo byly porovnány původní strany456 a616 svazku ed3print1,
Robsonovy strany418–419 v reprintu článku1971 a relevantní původní
obrazy errat. Podrobný záznam čerstvé kontroly je
`aligned-m32-source-review.md`. Doslovná dolní mocnina a požadavek
jen s volných buněk nejsou artefaktem OCR.

Robson pro žádost s vyžaduje celý volný slot délky2^ceil(lg s),
zarovnaný na tuto délku, a s buněk obsadí na jeho začátku. Slot je
podmínkou volnosti, nikoli trvale obsazeným zaokrouhleným blokem.
Právě na tuto strategii se vztahuje původní důkaz. Oprava musí
zahrnout zarovnání i délku testovaného volného slotu.

Všechny čtyři oficiální komprimované PostScripty byly2.11.2026
staženy znovu, HTTP200, a byly bajtově shodné s archivem. Opravy456
se týkají limitních proměnných; jediná relevantní položka616
z7.7.2023 mění Krogdahlovy stránky96–97 na96–99. Oprava této
strategie nebyla nalezena. Anglický ASCII report C0091 se ukládá
lokálně; žádné hlášení nebylo nikomu odesláno.
