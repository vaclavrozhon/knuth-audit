# Audit §2.2.4 Circular Lists

Pracovní poznámky; vlastníkem integrace je kořenový agent. Sken je třetí
vydání, první dotisk (1997). Tištěná strana `p` má v DjVu pořadí `p+15`.
Všechny obrázky 273–280 a 551–553 byly zobrazeny. Fyzický exemplář ověřen
nebyl. Všechny zápisy tohoto bloku zůstávají v jeho vlastní složce.

## Inventář a errata

Hlavní text začíná dole na s. 273 a končí před cvičeními na s. 278.
Patří sem obrázky (1), (4), (5), příklad polynomu na s. 276,
Algoritmy A/M, Program A a jeho analýza. Obr. 10 je v prvním dotisku
na s. 279. Cvičení 1–4 jsou na s. 278, 5–13 na s. 279, 14–18 na s. 280;
následuje §2.2.5. Odpovědi 1–8 začínají na s. 551, odpověď 8 pokračuje
na s. 552; tam jsou 9–15, odpověď 15 pokračuje na s. 553, následovaná
16–18. Inventář je tedy **18 původních cvičení a náhrada cvičení 4 z roku 2021**.

Prohledány byly `all1-prepre`, `all1-pre`, `all1`, `err1`, podle stran,
klíčových slov a vzorců. Relevantní PDF stránky byly zobrazeny; úplné
dotazy s hashi jsou v [candidate-errata-search.json](results/candidate-errata-search.json).
Dne 2026-11-01 byly všechny čtyři původní soubory znovu staženy přímo
ze Stanfordu; jejich SHA-256 přesně souhlasí se sdíleným snapshotem.
Aktuální `all1` a `err1` mají HTTP Last-Modified 2026-05-31. Viz
[live-errata-hashes.json](results/live-errata-hashes.json).

| Místo | Datum | Změna a stav |
|---|---|---|
| 274, řádek 12 | 1997-11-17 | Zavírací uvozovka; známá oprava. |
| 275, za (4) | 1997-08-12 | `don't have a` → `there is no`; známá oprava. |
| 275, řádek 7 | 2012-09-06 | `list have` → `list must have`; stylistická změna. |
| 275, (4) a odstavec | 2021-08-16 | Pohyblivá hlava zachovává vložení zprava. Ověřeno. |
| 276, A4 | 2022-12-01 | Nejprve `Q <- LINK(Q)`, potom `LINK(Q1) <- Q`. Použito v důkazech. |
| 277, M2 | 1999-12-06 | Závorky kolem podmíněného výrazu. Ověřeno. |
| 277/279 | 2024-09-20 | Přesun Fig. 10 na začátek s. 277. Obsah diagramu souhlasí. |
| 278, úloha 4 | 2021-08-16 | X. Xie: deque s pohyblivou hlavou místo pouhého zásobníku. |
| 279, úloha 12 | 2001-12-19 | `Algorithm A` → `Program A`. |
| 551, odpověď 4 | 2021-08-17 | Nové operace s pohyblivou hlavou. Ověřeno. |
| 552, odpověď 12 | 2012-06-30 | `29p` → `27p`, `3/4` → `78%`. Ověřeno přesným MIX časem. |

Opravy sousedních §2.2.3 a §2.2.5 nejsou součástí tohoto bloku. Nové
kandidáty níže žádná z těchto změn neřeší.

## Reprezentace a základní operace

`LINK(v)` je adresa následníka uzlu `v`, `INFO(v)` jeho hodnota.
`null` označuje prázdný ukazatel, v MIXu adresu 0. Živé uzly jednoho
neprázdného kruhového seznamu tvoří jediný cyklus bez opakování.
`PTR` bez hlavy ukazuje na poslední prvek; posloupnost začíná v
`LINK(PTR)`. `AVAIL` je hlava odděleného lineárního zásobníku volných
uzlů. Odebrání z něj potřebuje neprázdný zásobník nebo úspěšný OVERFLOW;
vrácení uzlu přepíše jeho LINK starou hodnotou AVAIL.

Vložení vlevo nahradí hranu `PTR -> first` dvěma hranami
`PTR -> new -> first`. Vložení vpravo udělá totéž a posune PTR na `new`;
nový první uzel je pak původní `first`. Odebrání odstraní `first` a
spojí PTR s jeho následníkem. Pro jediný uzel musíme po vrácení nastavit
PTR na null; při prázdném vstupu je nutný UNDERFLOW. Nový jediný uzel
musí ukazovat sám na sebe. To jsou přesně opravy uvedené na s. 274.
Kombinace levého vložení a odebrání je zásobník (LIFO), pravého vložení
a levého odebrání fronta (FIFO).

**Smazání celého cyklu (2).** Pro libovolný uzel `v` cyklu záměna
`AVAIL <-> LINK(v)` převede pořadí `next(v),...,v` před starý AVAIL.
Vznikne lineární seznam všech a jen uvolněných uzlů následovaný starým
zásobníkem. Počet operací nezávisí na délce cyklu. Ukazatel majitele je
třeba zneplatnit, jak text připomíná.

**Zřetězení (3).** Pro dva oddělené neprázdné cykly je výměna jejich
posledních hran jediným cyklem v pořadí `L1,L2`, s posledním uzlem
původního L2. Nastavení PTR1 na PTR2 a PTR2 na null tedy má popsaný
význam. Je-li L1 prázdný, stačí převod ukazatele; je-li L2 prázdný,
neděje se nic. Tím je obecně ověřen i diagram odpovědi 2.

**Úloha 1.** Prázdný stav `PTR=LOC(PTR)` sám o sobě nezruší zvláštní
případy. Při prvním nezměněném levém vložení by nový uzel nadále
odkazoval na buňku PTR: ta se tak stane skutečným uzlem v cyklu.
Chceme-li takto postupovat, zavedli jsme list head (hlavu seznamu),
nikoli pouhou jinou hodnotu prázdného ukazatele. Odpověď je správná.

**Úloha 3.** Jsou-li ukazatele na témž uzlu, výměna je identita a
jen PTR2 se zneplatní. Jinak rozstřihneme dvě hrany jednoho cyklu.
Cyklus ponechaný v PTR1 obsahuje uzly navštívené *po opuštění*
původního PTR1 až po původní PTR2 včetně. Druhý cyklus je doplněk.
Toto upřesnění počátečního bodu souhlasí s odpovědí a brání nejasnosti
slova „traversed“.

**Hlavy a úloha 4.** Pevná hlava `H` má v prázdném seznamu `LINK(H)=H`.
Vložení a odebrání hned za H je zásobník; před odebráním testujeme
`LINK(H)=H`. V novém zadání má PTR význam pohyblivé hlavy. Levé
vložení a odebrání zůstávají stejné. Pravé vložení uloží Y do původní
hlavy, vloží prázdnou novou hlavu bezprostředně za ni a přesune PTR.
Při čtení od nové hlavy proto dostaneme původní prvky a nakonec Y.
Platí i pro prázdný seznam. Právě proto původní tvrzení o nemožnosti
operace (b) nyní omezuje erratum na **pevnou** hlavu.

**Úloha 5.** Odpověď používá null dočasně: nejprve přeruší hranu ze
startovního uzlu `s` nastavením `LINK(s)=null`. Po k iteracích
`1<=k<=n` ukazuje Q na k-tý uzel původního průchodu a z něj vede
obrácená cesta ke startu a pak do null; P je další původní uzel.
Po n iteracích je P opět s. Poslední, `(n+1)`-ní iterace přečte jeho
dočasné null a napojí s na původní poslední uzel. Tím vznikne obrácený
cyklus a Q=s=PTR. Pro prázdný seznam se neprovede nic; pro jediný
uzel proběhnou dvě iterace. Tento malý trik není nekonečnou smyčkou.

## Polynomy, Algoritmy A a M

Polynom je konečná celočíselná lineární kombinace monomů `x^A y^B z^C`.
Term je monom s nenulovým koeficientem. Uzel zabírá dva MIX wordy:
koeficient a word se znaménkem/3 byty exponentů/2 byty ukazatele.
`b` je radix bytu. Zabalený exponent je `e=A*b^2+B*b+C`.
Nenulové termy jsou v přísně klesajícím pořadí e. Hlava má koeficient
0 a zabalený exponent -1; její LINK míří na největší e, nebo na ni
samotnou. Pole LINK se vždy čte **bez znaménka** druhého wordu.

Obrázek na s. 276 správně reprezentuje `x^6-6xy^5+5y^6`.
Součin na s. 275 lze ověřit součtem tří posunutých posloupností
koeficientů: pro vnitřní stupně vyjde `(i+1)-2i+(i-1)=0`; okraje
jsou 1, -6, 5 ve stupních `x^6,xy^5,y^6`. Přímá nezávislá konvoluce
to rovněž ověřuje. Příklad s. 276 dává `x^2+x-y`.

**Úloha 6.** Pro `xz-3` je posloupnost dvojic `(e,koeficient)`
`(b^2+1,1),(0,-3),(-1,0)`; nula má pouze poslední hlavu se smyčkou.
Oba tištěné diagramy souhlasí. **Úloha 7:** seřazení dovolí jediný
slučovací průchod. Při vzestupném pořadí by sentinel -1 nebyl poslední
hodnotou pro stejné porovnávací větve.

**Důkaz A pro oddělené vstupy.** Na začátku A2 rozdělíme Q na hotový
prefix C a zbývající původní suffix R, jehož prvním uzlem je Q.
Q1 je poslední uzel C, případně hlava. Nezpracovaný suffix P označme S.
Všechny exponenty C jsou větší než zbývající exponenty R i S;
C už je kanonickým součtem zpracovaných vstupních prefixů.

Je-li první exponent S menší, přesune se první uzel R do C. Je-li
větší, vloží se jeho kopie před R a první term S je spotřebován.
Jsou-li exponenty stejné a nezáporné, termy se sloučí: nenulový
součet se přesune do C, nula se odstraní a vrátí do AVAIL. Všechny
tři případy zachovávají invariant a zmenší počet nezpracovaných
vstupních termů alespoň o 1. Rovnost sentinelů ukončí průchod;
oba ukazatele pak opět ukazují na své původní hlavy. Žádný vstupní
uzel P nebyl změněn. Konečnost i správnost jsou tedy obecné, nikoli
odvozené z testování.

**Úloha 8.** Q1 umožňuje přepsat předcházející hranu v O(1).
Alternativní smazání kopíruje následující uzel do Q a uvolní následníka;
alternativní vložení zamění obsahy nového uzlu a Q a vloží přesunutý
původní obsah za Q. Abstraktní pořadí hodnot souhlasí, ale adresy uzlů
nikoli. Při smazání posledního termu se hlava přesune do jeho adresy
a stará adresa hlavy je uvolněna. Externí ukazatele proto přestanou
označovat hlavu. Historické použití obou triků dokládá původní manuál
IPL-V P-1918 (1960), s. 46–47; viz bibliografie níže.

**Důkaz M.** Pro aktuální term `c*x^f` v M se každé e v P změní na
`e+f` a jeho koeficient na násobek c. Seřazení se zachová a žádný
nenulový koeficient se nezmění na nulu. Sentinel zůstane -1.
Přesně takový vstup A zpracovává. Po j cyklech je tedy
`Q = Q_initial + P_initial * (součet prvních j termů M)`.
Po návratu M na hlavu je výsledek požadovaný. Nulový P i M jsou
zahrnuty: prázdný M nemá žádný cyklus; prázdný P vede k průchodu
dosavadním Q až k sentinelům.

**Úloha 10 a rozsahy.** Programy pracují pouze se zabaleným e, takže
stejný kód reprezentuje jednorozměrný exponent až `b^3-1`.
Substituce je `f(x^(b^2),x^b,x)`. Při třech proměnných musí každý
dílčí součet exponentů zůstat menší než b; při jedné stačí součet
e menší než `b^3`. V obou případech se předpokládá, že koeficienty
i všechny součiny/součty, které program skutečně vytváří, mají
absolutní hodnotu nejvýše `b^5-1`. Vynulování přetékajícího součtu
není legitimní výjimkou ze vstupního předpokladu knihy.

## Úloha 9: sdílení seznamů a nový kandidát

Jednotlivé rovnosti níže chápeme jako případy, kdy zbývající seznam
je oddělený; současná rovnost všech tří ukazatelů není tvrzením těchto
oddělených analýz. Cyklické seznamy s jednou hlavou nemohou sdílet
jen část uzlů: společný uzel znamená stejný celý cyklus a tutéž hlavu.

* **A, P=Q:** oba kurzory ukazují na stejný term, jeho koeficient se
  zdvojnásobí a oba přejdou na jeho následníka. Nenulový celočíselný
  koeficient se tím nevynuluje. Indukce dává dvojnásobný polynom.
  Nedovolený vstup s nulovým koeficientem by smazal současně P a Q,
  proto kniha správně připomíná selhání pro tento anomální vstup.
* **M, P=M:** výstup Q je oddělený a zdrojové uzly se nemění. M i P
  jsou samostatné proměnné, takže návrat P na hlavu nenaruší kurzor M.
  Vzniká `Q_initial + P_initial^2`.
* **M, P=Q, aktuální term t s kladným exponentem:** posun e -> e+f
  ukládá příspěvek vždy před právě čtený uzel P. Jeho následníci se
  nemění. Již přečtené uzly se smějí změnit nebo smazat; P se k nim
  nevrátí. Tento cyklus tedy nahradí aktuální polynom výrazem `(1+t)P`.
  Má-li t exponent 0 a koeficient c odlišný od -1, čte a přepisuje
  stejný uzel; násobek `(1+c)` zůstává nenulový, takže kurzor je bezpečný.
  Indukce dává uvedený součin faktorů `(1+t_i)` **s touto výjimkou**.
* **M, M=Q:** před zpracováním termu M jsou všechny dříve vytvořené
  termy větší nebo rovny dřívějším exponentům M. Nezasáhnou tedy žádný
  ještě nezpracovaný menší term M. V aktuálním cyklu všechny kladné
  exponenty P zapisují před M; případný konstantní člen P se zpracuje
  poslední. Pokud není -1, M zůstane živý a jeho následník nezměněný.
  Indukce dává `Q_initial + Q_initial*P`. Pro konstantní člen P=-1
  se M uvolní a následující M1 sleduje přepsaný LINK, jak uvádí kniha.

**Kandidát `alias-pq-minus-one`.** Odpověď 9 u P=Q zapomíná analogicky
vyloučit konstantní člen **M** rovný -1. Nejkratší platný vstup má
P=Q=1 a oddělený M=-1, AVAIL=null. A3 vynuluje jediný term, A4 jej
uvolní a přepíše jeho LINK na null. Následné `P <- LINK(P)` tedy
nevrátí P na hlavu. Jde o přímé porušení invariantu na dvou jednočlenných
polynomech, nikoli o nedostatek počáteční paměti: správná operace by
jeden uzel uvolnila. Doslovný MIX následně zastaví v OVERFLOW a zanechá
neplatný běžný uzel s nulovým koeficientem. Výsledek reprodukován pro
všech 37 radiců; po prvním smazání je rI1=1002, AVAIL=1002,
LINK(1002)=0, pak rI1=0. Důkaz se týká i opraveného pořadí A4 z 2022.
Nulový vstupní P žádný běžný uzel nemá a je neškodnou výjimkou.

Podrobný ASCII návrh je v [reports/alias-pq-minus-one.txt](reports/alias-pq-minus-one.txt).
Kořenový agent rozhoduje klasifikaci a globální ID.

## MIX: provedení, časy a paměť

[programs.py](programs.py) přepisuje všechny instrukce ze skenů; lokální
číselné značky jsou pouze přejmenovány. Sestavení a exekuce používají
nezměněný společný MIX model. Vlastní řešení jsou navíc v
[solutions.py](solutions.py), ne pouze pseudokód.

**Program A.** Pole ABC je `(0:3)`, LINK `(4:5)`. Úplný word načtený
ve SW1 se porovnává přes ABC; jeho dolní dva byty se při vložení
přepíší správným LINK. Záporná hlava je detekována JAN, nezávisle
na jejím nezáporném ukazateli. STJ přepisuje adresu JAN v A3;
ostatní údaje instrukce zůstanou zachovány. Nulový součet s libovolným
znaménkem projde do odstranění, protože JANZ testuje číselnou hodnotu.

Označme `c=m'` počet rušících se dvojic, `n=m''` počet nerušících se
dvojic, `i=p'` počet termů pouze v P a `j=q'` počet termů pouze v Q.
Pak `m=c+n`, `p=m+i`, `q=m+j` a počet porovnání je `1+m+i+j`.
Každá větev spotřebuje právě termy uvedené v důkazu A. Tím dostaneme
všechny řádkové počty vytištěné u Programu A; společně s MIX cenami
load/store/add/compare=2u a branch/address-transfer=1u dávají

```
T_ADD = 27c + 18n + 27i + 8j + 13.
```

[check_mix.py](check_mix.py) ověřuje i jednotlivých 34 vykonatelných
řádků, ne pouze jejich součet. Základ 13u zahrnuje návrat, nikoli
volající JMP. Všechny uváděné časy jsou bez obsluhy OVERFLOW.

**Paměťový odhad.** Na začátku je živých `2+p+q` uzlů včetně dvou
hlav. Každá vložená kopie zvýší živý počet o 1, každé zrušení sníží
o 1. Přesné maximum je počáteční počet plus největší prefixový rozdíl
`#vložení-#zrušení` (včetně prázdného prefixu). Leží mezi 0 a p',
což dává obě tištěné meze. Horní mez nastane, když vložení předcházejí
zrušením, dolní například při p'=0 nebo při dostatečném dřívějším
uvolnění. Pool musí být oddělený od programu a všech zdrojových uzlů.

**COPY, úloha 11.** První kopírovaný uzel je hlava. I3 nejprve ukazuje
na instrukci návratu, takže její následující word funguje jako dočasný
ukazatel na novou hlavu; později ukazuje na poslední kopii. Každý cyklus
zkopíruje koeficient a ABC, připojí uzel, a posune I1 ve zdroji.
Negativní ABC po posunu znamená návrat na původní hlavu a konec.
I2 načte uloženou novou hlavu a uzavře nový cyklus. Kopíruje se p+1
uzlů, každý cyklus stojí 21u, ostatní instrukce 10u: `21p+31`.
Zdroj ani I1 se nemění. Platí pro p=0 i zápornou nulu v koeficientu hlavy.

**Úloha 12.** ADD do nulového Q má c=n=j=0, i=p, tedy `27p+13`.
Se ZERO za 18u je cena `27p+31`. Poměr COPY k této kombinaci je
`(21p+31)/(27p+31)`, pro p -> nekonečno jde k 7/9, přibližně 78 %.
Pro malá p je poměr blíže 1; formulace „about 78%“ je asymptotická.
Původní 29p a 3/4 jsou **známé erratum**, nikoli nový nález.

**ERASE, úloha 13.** Přesně výměna AVAIL a LINK(hlavy); do AVAIL
přejdou všechny termy a nakonec hlava. Cena je 11u nezávisle na p.
Prázdný polynom má stále jednu hlavu, takže případ null není vstupem.
Příklad přiřazení ERASE(Q);COPY(P) předpokládá oddělené P a Q;
sdílený zdroj by si volající sám uvolnil.

**ZERO, úloha 14.** Uvolněný uzel se odebere, I2 si uchová jeho adresu,
MOVE zkopíruje dva konstantní wordy (0 a -1 v ABC), I2 uzavře LINK.
MOVE změní I1, který dle smlouvy není zachováván. Cena
`2+2+1+2+2+1+5+2+1=18u`. Samotný sentinel má znaménko minus a jeho
LINK se doplní bez změny znaménka. Žádný aritmetický limit se nepřekročí.

**MULT, úloha 15.** Přepíše SW1 skokem do výpočtu posunutého exponentu
a součinu koeficientů. Výsledek MUL je v X, neboť podle předpokladu
se celý vejde do jednoho wordu. STX jej uchová, aby se k němu obě
větve A dostaly přes nové SW2/SW3. Pro hlavu se nepřičte exponent M;
SLA 2 umístí ABC zpět do horních tří bytů. I4 zůstává během ADD
nedotčen a M1 jím prochází M; před návratem se obnoví všechny tři
instrukce. I1,I2,I4 jsou opět původní hlavy. Program není deklarován
jako reentrantní; jeho návratové adresy a switche jsou v kódu.

**Vlastní řešení.** ZERO2 staví hlavu bez MOVE. COPY2 nejprve zavolá
ZERO2, pak kopíruje pouze běžné termy; I4 je kurzor zdroje a I3 poslední
kopie, nakonec se poslední LINK spojí s novou hlavou. ERASE2 používá
indexový registr pro první uzel místo plné kopie do A. MULT2 ukládá
exponent a koeficient aktuálního termu M před voláním ADD; jeho helper
ve SW1 nemultiplikuje sentinel a běžný součin ukládá zvlášť. Stejný
slučovací invariant proto platí. Kód opravdu běží v MIXu, bez háčků
do Pythonu při provádění instrukcí. Všechny registry požadované zadáním
a všechny původní switche byly ověřeny.
Vlastní COPY2 stojí `24p+30` jednotek, tedy oproti ZERO+ADD
asymptoticky 8/9 času; to je samostatná odpověď na úlohu 12 pro vlastní
volbu programu. Vlastní MULT2 má přesný čas
`25pr+31r+28+27 sum(m')+18 sum(m'')+27 sum(p')+8 sum(q')`.
Tyto odlišné konstanty nejsou zaměňovány za čas knižního řešení.

**OVERFLOW a hranice stroje.** Pro pokračování po nedostatku paměti
musí OVERFLOW zachovat živé registry, jak výslovně ukládá §2.2.3-4,
a vrátit se na vstupní rJ-2, aby se alokace zopakovala. Testy zahrnují
ukončující HLT i skutečnou MIX rutinu, která doplní rezervní řetězec
a zachová registry. Kód/data/uzly jsou disjunktní, každý uzel má dvě
adresy v 0..3999, nulová adresa není platný alokovaný uzel. Jeho konec
smí být nejvýše 3999. Oba adresní byty dostačují pro celé MIX pole
pro každé b=64..100. Obecný důkaz je nezávislý na fyzickém pořadí
uzlů; testy mají adresy promíchané. Coeficienty ±(b^5-1), e=b^3-1,
zrušení na nulu a nulové polynomy jsou v hraničních testech.

## Úloha 16: přesná analýza a nový kandidát

`r` je počet termů M a `p` neměnný počet termů zdrojového P. V jednom
volání ADD stojí nová SW1 větev proti původnímu LDA navíc 21u za
každý běžný term a 19u za sentinel (vynechané ADD za 2u). Jeden term
M stojí dalších 6u za LD4,LDA,JANN,JMP ADD. Vstup, poslední průchod
M1 a obnovení switchů dohromady stojí 29u. Po přičtení základu 13u
každého ADD tedy přesně vychází tištěný první vzorec:

```
T_MULT = 21pr + 38r + 29
         + 27 sum(m') + 18 sum(m'') + 27 sum(p') + 8 sum(q').
```

Počet termů Q se v jednom průchodu mění o `p'-m'`. Za předpokladů
`m'=0` a `p'=alpha*p` v každém cyklu jsou tedy součty postupně
`0`, `(1-alpha)pr`, `alpha*pr` a
`r*q'_0 + alpha*p*r*(r-1)/2`. Poslední tvrzení plyne z toho, že počet
společných termů je konstantní `(1-alpha)p` a velikost Q roste
v každém kroku o `alpha*p`.

**Kandidát `multiplication-time-simplification`.** Dosazení uvedených
součtů dává

```
4 alpha p r^2 + 39pr + 5 alpha pr + 8q'_0 r + 38r + 29,
```

nikoli tištěných `40pr+4 alpha pr` místo `39pr+5 alpha pr`.
Rozdíl tištěného a správného výrazu je `(1-alpha)pr`. Nejmenší
celočíselné počty s `0<alpha<1` mají p=2, r=1, alpha=1/2.
Realizuje je P=x+1,Q=x,M=1: jediná shoda se neruší, druhý term se
vloží, q'_0=0. Přesný vzorec i doslovný MIX dávají 154u, zjednodušený
tištěný vzorec 155u. To je chyba algebraického součtu, nikoli spor
o kvalitu statistického modelu nebo zaokrouhlení.

Doporučení volit menší počet termů u násobitele je v textu formulováno
jako vodítko této analýzy, nikoli jako univerzální optimum všech
vstupů. Odhad s konstantním alpha není probabilistická věta; změna rolí
P/M může změnit i alpha a q'_0. Opravený vedoucí člen `4 alpha p r^2`
heuristický závěr zachovává.

Podrobný ASCII návrh je v
[reports/multiplication-time-simplification.txt](reports/multiplication-time-simplification.txt).

## Úlohy 17 a 18

**17.** Lineární uspořádané seznamy dovolují stejný slučovací průchod;
sentinel je možné nahradit testem null. Neznáme-li jejich konec, úplné
vrácení do AVAIL vyžaduje nalezení posledního uzlu. Kruhový seznam
s ukazatelem na hlavu poskytne poslední hranu k přestřižení přímo.
Tato výhoda ERASE je správná. S druhým uloženým ukazatelem na konec
by ji měl i lineární seznam, což je v souladu s dřívějším srovnáním
jednoho kruhového a dvou lineárních ukazatelů.

**18.** Nechť `a_i` jsou adresy uzlů v cyklickém pořadí a `K` počet
hodnot dostupných v linkovém poli. Při bitovém XOR ukládáme
`L_i=a_(i-1) XOR a_(i+1)`. Z dvojice sousedů `(a_(i-1),a_i)`
dostaneme následníka jako `L_i XOR a_(i-1)` a předchůdce předchozího
uzlu jako `L_(i-1) XOR a_i`. Jde o identitu `(a XOR b) XOR a=b`,
nikoli o odhad složitosti závislý na délce seznamu.

Pro součet modulo K je `L_i=(a_(i-1)+a_(i+1)) mod K`; odečtení
známého souseda získá druhého. Pro rozdíl
`L_i=(a_(i+1)-a_(i-1)) mod K` použijeme při dopředném průchodu
`a_(i+1)=L_i+a_(i-1) mod K` a zpět
`a_(i-1)=a_(i+1)-L_i mod K`. Směr je součástí stavu průchodu,
proto nekomutativita rozdílu není problém. U MIXu lze vzít K=b^2;
modulární varianta nepotřebuje bitový radix. XOR adres 0..3999 má
hodnotu nejvýše 4095 a vejde se také pro všechna b=64..100.

Dvě sousední hlavy na známých adresách dávají první známou dvojici
i u prázdného seznamu. Ten má dva uzly a oba sousedé každého uzlu
jsou druhá hlava; vzorce stále platí. Neznámé původcovství této
techniky, uvedené v závorce knihy, nepovažujeme za prokázané negativní
historické tvrzení. Žádné konkrétní prvenství se zde nepřisuzuje.

## Primární podklady a meze

Historická věta v odpovědi 8 je přímo doložena:
Newell, Tonge, Feigenbaum, Mealy, Saber, Green a Wolf,
*Information Processing Language V Manual, Section II*, RAND P-1918,
31. března 1960. Osobní archiv Allena Newella poskytuje
[úplný scan](https://iiif.library.cmu.edu/file/Newell_box00003_fld00181_doc0001/Newell_box00003_fld00181_doc0001.pdf).
Na s. 46 jsou obě varianty vložení přes zachování obsahu uzlu;
na s. 47 smazání kopírováním následníka a problém koncového uzlu.
Uloženy jsou PDF, OCR, hash, titulní list a příslušné originální obrazy.
Jde o pozitivní doklad použití v IPL-V v roce 1960, ne o určení úplně
prvního použití v řadě IPL.

Připsání úlohy 4 X. Xie (2021) dokládá Knuthova vlastní publikovaná
vrstva `all1-pre`, s. 12 a 16. Samostatný veřejný článek není v knize
citován. Žádné další externí citace tato sekce neuvádí. Odkaz na
úlohu 5.2.3-29 je vnitroknižní odkaz na jinou, rychlejší metodu;
originální s. 157 svazku 3 opravdu obsahuje Brownovu úlohu o násobení
polynomů pomocí prioritní fronty; její celý audit není součástí
přiděleného §2.2.4. Význam „rychlejší“ lze zde ověřit přímo: r
seřazených proudů po p dílčích součinech sloučíme haldou velikosti r
za `O(pr log(r+1))`, stejné exponenty sečteme a proud výsledku
jednou sloučíme s Q za `O(pr+q)`. Tím se v příslušném režimu odstraní
opakované lineární průchody rostoucím Q. Nejde o tvrzení lepších
konstant na každém vstupu.

Technická část je uzavřena obecnými důkazy a reprodukcemi, s dvěma
novými kandidáty předanými ke kořenové revizi. Bibliograficky je
doložené uvedené použití v IPL a autorova atribuce Xie; původ XOR
techniky zůstává přesně v rozsahu knihy neurčen. Tato mez se nemá
zaměňovat za chybějící důkaz správnosti reprezentace.
