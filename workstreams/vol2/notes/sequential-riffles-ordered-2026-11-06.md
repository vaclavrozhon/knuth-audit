# Souvislá revize §3.4.2: karty a seřazený výběr

6. listopadu 2026. Přezkoumány původní strany 145, 147–148 a odpovědi
na 592; souborové strany jsou o 12 vyšší. Karetní kontext a úloha 14
jsou uzavřené bez nového nálezu (X0127). Úloha 16 zůstává partial
(X0128): nyní máme obecný důkaz očekávané lineární ceny i pro tištěný
algoritmus v přesném konečném modelu, ale nikoli jeho konstantu 5n/2.
Předchozí S/R/P a ostatní základní úlohy jsou v X0125, známé opravy
v X0126. Dodatky 18 a 19 mají vlastní navazující revizi.

## Náhodné prokládání na straně 145

Původní věta skutečně tvrdí nutnost alespoň sedmi a postačitelnost
čtrnácti míchání. Sedm neoznačuje za postačující. Jde o totální variační
vzdálenost v citovaném GSR modelu: binomické rozdělení velikosti řezu
a následné upouštění karet úměrně velikosti zbývajících hromádek.
Nejde o garanci pro libovolné lidské míchání.

Obecný důkaz v `sampling-context.md` byl znovu přezkoumán. Inverzní
míchání je stabilní třídění podle nezávislých bitů. Po K krocích jsou
to rovnoměrné štítky z 0,…,a−1 pro a=2^K. Pro permutaci s d sestupy
je počet přípustných štítkování C(a+N−d−1,N), pokud a>d; jinak nula.
Odečteme povinný jednotkový růst na každém sestupu a spočítáme zbývající
neklesající posloupnosti. Eulerianova rekurence pak seskupí permutace
podle sestupů. Inverze i pořadí nezávislých identicky rozdělených
míchání zachovají příslušnou vzdálenost od rovnoměrného rozdělení.

Celý `verify_riffle_distance.py`, uložené zlomky a log byly přečteny.
V GSR modelu dávají vzdálenosti přibližně 0.61355 pro K=6, 0.33406
pro K=7, 0.16716 pro K=8, 0.08542 pro K=9 a 0.002689 pro K=14.
Přesný desetiprocentní práh je tedy devět; obě slabší meze knihy platí.
Kontrakce při dalším nezávislém kroku zaručuje monotonicitu vzdálenosti.
Pro K=14 navíc stačí jednodušší kolizní mez

    TV ≤ 1 − ∏_{i=0}^{51}(1−i/2^14) = přibližně 0.0778225.

Podmíněně na různých štítcích je jejich pořadí rovnoměrné, což tuto mez
přímo dokazuje. Archivovaných 6 669 štítkových historií a 15 malých
modelů se neopakovalo. Nově se zkontrolovala vnitřní konzistence
uložených přesných zlomků a jejich desetinné prezentace.

Primární Aldous–Diaconis 1986 byl znovu vizuálně přečten na stranách
335–336 a 343–345: definice vzdálenosti, lemma o silném rovnoměrném
čase, všechny tři definice modelu, Reedsův argument a obě citované meze.
Lokální textový výtah obsahuje pouze oddělovače stran; není důkazním OCR.
Celý článek nebyl v tomto bloku nově přečten. Historická pozorování
skutečných hráčů a absolutní priority objevů se samostatně neověřovala.

## Konkrétní balíčky v úloze 14

Znovu porovnáno všech 104 značek v obou přepisech s původními barvami
na 147. `verify_card_riffles.py` byl přečten celý, stejně jako uložené
kandidáty, všechny čtyři přímé svědky a výjimečné pozice.

Pro pozicovou permutaci p(i) původní karty i je D(p) počet cyklických
sestupů p(i−1)>p(i). Jedno sejmutí a proložení je možné právě při D≤2.
Nutnost D≤2^r po r krocích plyne z rostoucích celočíselných zvednutí:
nejmenší kladné přírůstky dávají P(i+N)=P(i)+ND(p), a složení zvednutí
má stupeň D(p)D(q). Minimální zvednutí složené permutace má nejvýše
tento stupeň. Tedy D(q∘p)≤D(q)D(p).

Postačitelnost: sejmeme původní kruh na začátku jednoho rostoucího
úseku, úsekům přiřadíme čísla 0,…,D−1. Stabilní rozdělení výsledného
balíčku podle r bitů těchto čísel od nejnižšího obnoví původní pořadí.
Obrácení rozdělení jsou požadovaná proložení; počáteční rotaci pohltí
první sejmutí. Prázdnou bitovou skupinu lze nahradit totožným krokem
se dvěma neprázdnými částmi, protože N≥2.

V (a) pouze srdcová dáma z pozice 10 sníží D ze 3 na 2. Jednoznačnost
se ztrácí právě při jejím vložení na pozice 1, 2, 3, 51, 52. V (b)
pouze kárová pětka z pozice 42 sníží D z 9 na 8. Obě odpovědi souhlasí.
Příklad 3890145267 při řezech x=3, y=8 zachovává podposloupnosti
34567 a 89012. Přímí svědci v JSON kontrolují pořadí obou hromádek
nezávisle na počtu sestupů. Starých 195 120 součinů malých permutací
nebylo opakováno; slouží jako konečná podpora implementace, ne obecný důkaz.

Citace Gardner, Mathematical Magic Show, kapitola 7 nebyla nyní
nezávisle otevřena. Stejně zůstává bibliografickou výjimkou přesný
pinpoint SIAM Review 3 (1961), 293–297 u úlohy 13, jejíž afinní grupa
byla matematicky ověřena v X0125.

## Seřazené vzorkování, úloha 16

Znovu přezkoumány všechny invarianty v `ordered-sampling.md`, celý
`verify_ordered_sampling.py`, log a všech 91 uložených přesných
součtů nákladů. Jejich součty a podíly jsou vnitřně konzistentní.
Původní výpočet 5 491 226 dotazů se neopakoval.

Primární Knuthův program v Bentleyho sloupku byl znovu přečten celý
(oddíly 1–14, 366–367), strana 367 vizuálně. Sondy jdou klesajícími
indexy; při střetu se menší klíč přenáší dál. Kanonická tabulka odpovídá
obyčejnému vložení od největšího klíče. Dva průchody při výstupu jsou
filtrované podle T[0], nikoli pouhé cyklické otočení nenulových položek.
Svazek 3 byl znovu vizuálně zkontrolován na 526 (směr sondování),
556 (zadání 66) a 741 (odpověď 66); tím se netvrdí kontrola ostatních
úloh na těchto stranách ani změna pokrytí svazku 3.

Četba Amble–Knuth, strany 7–9 v uloženém OCR, potvrzuje omezení
původní analýzy: nezávislé rovnoměrné domovské adresy, navíc předpoklad
zanedbatelné korelace s pořadím klíčů v příslušném kroku. Bez důkazu
nelze přenést přesnou konstantu do konečné populace s monotónní adresou.
Nový obecný argument níže tento problém pro řád O(n) obchází.

### Nový důkaz očekávané lineární ceny tištěného algoritmu

Předpokládáme 1≤n≤N/2, M=2n a h(x)=⌊M(x−1)/N⌋. Ostatní případy
řeší prázdný/plný výstup nebo doplněk, jak bylo doloženo dříve.
Stav po k úspěšných vloženích je rovnoměrná k-prvková podmnožina S.
Označme A_i počet jejích klíčů s domovskou adresou i, indexy modulo M.

Nechť B_i je počet klíčů, které při umisťování překročí hranu i→i−1.
V každé obsazené buňce zůstává jeden klíč; přebytek pokračuje dál.
Proto B_i=max(0,A_i+B_{i+1}−1). Existuje prázdná buňka, jelikož k<M;
rozvinutí této rekurence do poslední prázdné buňky dává

    B_i = max(0, max_{1≤l≤M}(A_i+…+A_{i+l−1}−l)).       (Q)

Prázdná buňka nemohla být během vkládání překročena. To zároveň dokládá,
že rovnice popisuje skutečné lineární sondování. Součet D(S)=Σ_i B_i
je celkový počet posunů klíčů od jejich domovských adres. Nezávisí na
pořadí vložení ani na prohazování klíčů při uspořádaném vkládání.

Každý cyklický interval l přihrádek obsahuje q≤⌈Nl/M⌉ čísel populace:
jeho velikost je rozdíl dvou stropů na rovnoměrné mřížce. Počet X jeho
vybraných klíčů má hypergeometrické rozdělení a střední hodnotu

    μ=kq/N ≤ kl/M+k/N ≤ (l+1)/2.

Pro z≥1 lze odhad momentové funkce dokázat přímo faktoriálními momenty:

    E z^X = Σ_j (z−1)^j C(k,j) (q)_j/(N)_j
          ≤ (1+(q/N)(z−1))^k ≤ exp(μ(z−1)).

Použili jsme (q)_j/(N)_j≤(q/N)^j, nikoli nezávislost výběru bez vracení.
Volbou z=2 a Markovovou nerovností dostaneme pro celá t≥1

    Pr(X≥l+t) ≤ exp(1/2) exp(−δl) 2^(−t),
    δ=log(2)−1/2 > 0.

Sjednocovací mez přes l v (Q) a součet ocasů přes t dávají konstantu
nezávislou na N, n, k a i:

    E B_i ≤ C := exp(1/2)/(exp(δ)−1) = e/(2−√e) < ∞,
    d_k := E D(S) ≤ CM.                                    (B)

Při úspěšném vložení x je počet sond 1+D(S∪{x})−D(S).
Každý krok neseného klíče zvýší D o jednu, výměna sama nikoli.
Při duplikátu x∈S je cena jedna plus jeho dosavadní posun; k výměně
před nalezením duplikátu nedojde. Přesná očekávaná cena fáze k je tedy

    N/(N−k) + d_{k+1}−d_k + d_k/(N−k).

Odmítnutí nemění S; dělení pravděpodobností úspěchu (N−k)/N plyne
z rovnice obnovy, bez předpokladu nezávislosti ceny a úspěchu téhož pokusu.
Sečtením fází dostaneme R+d_n+Σ_{k<n}d_k/(N−k), kde R<2n.
Protože Σ_{k<n}1/(N−k)<1 a M=2n, odhad (B) dokazuje

    E celkový počet sond < (2+4C)n = O(n).

Paměť tabulky a filtrovaný výstup jsou rovněž O(n). Důkaz používá
stejný jednotkový model přesné celočíselné aritmetiky a rovnoměrných
voleb jako úloha. **Tato hrubá konstanta nedokazuje tištěných 5n/2.**
Obecnou ostřejší mez ponecháváme výslovně otevřenou, bez tvrzení,
že byla vyvrácena.

Nový krátký `verify_ordered_queue.py` ověřil 3 648 podmnožin a 760
intervalů populace ve 32 modelech N≤12, n≤min(N/2,4). Porovnává (Q)
s nezávislým obyčejným vložením od největšího klíče; očekávané posuny
pak přesnou fázovou identitou reprodukují všechny odpovídající náklady
starého dotazového orákula. Běh s `nice -n 15` skončil za přibližně
0.3 sekundy, kód 0. Malé modely podporují nové identity; obecný důkaz
je analytický argument výše, nikoli extrapolace konečného soupisu.

## Errata a hranice pokrytí

Použity již obnovené vrstvy all2-prepre, all2-pre, all2, err2 a aktuální
TeX z 6. listopadu. Vyhledány strany 145–148/592 a termíny riffle,
shuffle, ordered, probing, Bentley, Aldous a Diaconis. Pro právě
kontrolované matematické výroky se nenašla nová změna; známé opravy
sousedních míst zůstávají v X0126. Nebylo nutné znovu stahovat stejné PDF.

Strany 145 a 147 mají nyní doloženou celou matematiku a fakta včetně
uvedených bibliografických výjimek. Strany 148 a 592 zůstávají partial:
konstanta úlohy 16 je otevřená, revize dodatků 18/19 navazuje a na 592
jsou navíc první odpovědi §3.5. Nový nález ani emailový návrh nevznikl.
