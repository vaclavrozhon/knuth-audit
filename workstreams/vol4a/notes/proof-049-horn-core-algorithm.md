# Algoritmus C, všechny jeho vrstvy oprav a úlohy 47–48

Checkpoint X0078, P0737–P0745. Originál p59–60/file76–77,
zadání 47–48 na p85–86/file102–103, odpovědi p543/file560.
Doklady: images/file076.png, file077.png, proof-file102.png,
file103.png a proof-file560.png. Žádný matematický program.

## Původní reprezentace a inicializace — P0737

Nechť n=|P|, r=|C|, L je celkový počet výskytů předpokladů
a N=L+r celková délka definite klauzulí včetně hlav. Vstup je
explicitně rozvinutý, s indexovanými proměnnými a konstantní cenou
přístupu k poli/odkazu. Parametrická schémata nejsou tímto vstupem.

Každý výskyt u_j na levé straně pravidla dostane vlastní záznam h,
i pokud se stejná proměnná opakuje. CLAUSE(h) ukazuje na vlastní
pravidlo; PREV(h) propojí všechny a jen výskyty stejné proměnné.
Indukce přes vkládání v C1 dokazuje úplnost seznamů LAST(p), jejich
bezcykličnost a disjunktnost. COUNT(c) se inicializuje na přesný
počet těchto záznamů. Pole seznamů se po inicializaci nemění.

TRUTH a zásobník jsou nejprve prázdné. Každé pravidlo s k=0 je
fakt; jeho hlava se označí a vloží právě při první takové příležitosti.
Při opakovaném faktu větev „otherwise, for 1≤j≤k“ pouze provede
prázdnou smyčku. Žádné chybějící pole nulového pravidla se později
nečte. Duplicitní pravidla i hypotézy jsou přípustné.

## Invariant, úplnost a ukončení původního C — P0738

TRUTH označuje přesně již odvozené propozice. Zásobník obsahuje
právě odvozené propozice, jejichž seznam ještě nebyl zpracován,
každou jednou. Během průchodu jednoho seznamu je aktuální p již
vyjmut; po skončení tohoto průchodu je celý invariant opět platný.
COUNT(c) je počáteční počet hypotéz minus počet už zpracovaných
záznamů daného pravidla. Z toho plyne nezápornost; nula nastane
právě po posledním záznamu, a každá jeho hypotéza tehdy má TRUTH=1.

C4 tedy nemůže odvodit neplatnou hlavu. C5 vloží novou propozici
jen při změně TRUTH z 0 na 1. Žádná propozice ani její seznam
nemohou být zpracovány podruhé. Přepsání lokálního p v C5 je
bezpečné: pokračování seznamu používá h a PREV(h), nikoli p.

Při prázdném zásobníku byly zpracovány všechny pravdivé propozice.
Má-li pravidlo všechny předpoklady pravdivé, každý jeho záznam
byl odečten, a jeho hlava je tedy také pravdivá. Výsledná množina
je uzavřená. P0735 (proof-048) pak dává přesně nejmenší model/core;
jeho abstraktní argument se zde nepřepočítává.

Nejvýše n vložení a konečné seznamy dokazují ukončení. Pravidla
s vlastní hlavou mezi předpoklady nic neoprávněně nespustí; cyklus
bez faktu zůstane celý nepravdivý. Při C=∅ je core prázdný, také
pro n=0, kdy žádné pravidlo s hlavou v P ani nemůže existovat.

## Náklady původního algoritmu — P0739

C1 stojí O(n+r+L); každý z L záznamů je vytvořen jednou.
V C2 se odebere nejvýše n propozic. V C3–C6 se každý záznam
zpracuje nejvýše jednou a každý navštívený záznam vyžaduje O(1)
práce. Výstup z pole TRUTH stojí O(n). Celkem O(N+n) času
a O(N+n) slov paměti. Prázdný vstup má konstantní režii;
žádné hledání celého seznamu klauzulí není skryto v jednom kroku.

## Složená opravená verze — P0740

Byly porovnány relevantní vrstvy all4a-pre, all4a, err4a,
all4f0 a err4f0, včetně hledání podle C, START, CONCLUSION a Horn,
nejen podle čísla stránky. F0 na p60 obsahuje bibliografický dodatek;
další relevantní algoritmická oprava v něm není. F1 je jiná část knihy.
Sazba oprav je uložena v images/proof-errata-pre-p7.png,
proof-errata-pre-p8.png, proof-errata-current-03.png a -04.png.

Je nutné složit všechny následující změny:

1. 28.7.2016 (all4a-pre p7–8) nahradilo seznamy výskytů
   seznamy klauzulí čekajících na jednu vybranou hypotézu;
   jejich předpoklady jsou v souvislém poli MEM.
2. 28.2.2022 (all4a/err4a) doplnilo v C1 **START(c)←l před l←l+k**.
   Bez tohoto doplnění by přepis z roku 2016 neměl definované
   počátky bloků. Jde o výslovně známou opravu, nikoli nový nález.
3. 30.5.2023 nahrazuje C3: nejprve uložit c′=PREV(c),
   q=CONCLUSION(c), při TRUTH(q)=1 jít rovnou do C6; jinak
   l=START(c), k=COUNT(c)−1. Nové C5 bez dalšího testu nastaví
   TRUTH(q)=1 a vloží q na zásobník.

Pole q se v C4 nemění; mezi jeho testem v C3 a vložením v C5
se neprovádí jiné odvození. Nový C5 proto nemůže zdvojit vložení.
Původní verze z prvního dotisku byla správná sama o sobě; její
pozdější výměna není důkazem původní chyby.

## Invariant čekající klauzule — P0741

Pro každou dosud neodloženou klauzuli c je COUNT(c)=k>0 délka
aktivního prefixu MEM[START(c)+1..START(c)+k]. Všechny hypotézy
za tímto prefixem už mají TRUTH=1. Klauzule čeká na poslední
prvek prefixu w a je právě v seznamu LAST(w). Tento w ještě
nebyl zpracován; smí již být pravdivý a čekat na zásobníku.
Prefix může obsahovat i jiné již pravdivé hypotézy: COUNT zde
není počet nulových hodnot TRUTH v celé klauzuli.

C1 tento invariant nastaví. I pokud je poslední hypotéza již
faktem z dřívějšího pravidla, žádná propozice ještě nebyla vyjmuta
ze zásobníku, takže její seznam se teprve zpracuje.

Při probuzení klauzule je čekající w pravdivé. C3 je odstraní
z aktivního prefixu. C4 pak zezadu odstraňuje další pravdivé
hypotézy. Narazí-li na nepravdivé p, uloží kratší prefix a přepojí
klauzuli do LAST(p). Toto p není ani zpracované, ani na zásobníku;
pokud se někdy stane pravdivým, probudí tuto klauzuli. Je-li prefix
prázdný, všechny původní hypotézy jsou pravdivé a C5 smí odvodit q.
Je-li q už pravdivé v C3, celou klauzuli lze trvale odložit:
její implikace už nemůže být porušena.

Je podstatné uložit c′ před změnou PREV(c). Dosud neprošlé uzly
aktuálního seznamu čekají na původní w; přepojení navštívené
klauzule na nepravdivé p≠w žádný jejich odkaz nemění. C6 tedy
přejde na správného původního následníka. Starý LAST zpracované
propozice smí obsahovat zastaralé odkazy: nikdy se už nečte.
Invariant seznamů je požadován pouze pro nezpracované propozice.

Při ukončení nemůže nepravdivá hlava mít všechny předpoklady
pravdivé: její dosud živá klauzule by čekala na pravdivé w,
které by při prázdném zásobníku již muselo být zpracováno.
Znovu tedy dostáváme uzavřenou a pouze platnými dedukcemi
vytvořenou množinu; P0735 určí core. Opakované hypotézy se
odstraní přes TRUTH, vlastní závislosti a cykly bez faktů zůstanou
neaktivní. Nulové klauzule a prázdný vstup fungují jako původně.

## Náklady opravené verze — P0742

Inicializace přečte/zapíše L hypotéz a r hlav. Každé probuzení
živé klauzule zmenší její prefix alespoň o čekající hypotézu;
nebo klauzuli trvale odloží kvůli již pravdivé hlavě. Klauzule
s k původními hypotézami proto může být probuzena nejvýše k krát.
Každý úspěšný test TRUTH v C4 odstraní další pozici jednou provždy;
neúspěšný test je nejvýše jeden na probuzení. Součet práce C3–C6
je tedy O(L+r), nikoli délka seznamu násobená počtem propozic.
Zásobník stále přijme nejvýše n prvků. Čas i paměť jsou O(N+n).
To uzavírá P0736 pro obě konkrétní verze, v uvedeném modelu slov.

## Úloha 47: přesný vztah k topologickému řazení — P0743

Použitý dřívější důkaz T je
workstreams/vol1/parallel/linked-allocation/notes/topological-sort.md,
část 1: invariant zbylých vstupních stupňů, fronta, cyklický zbytek
a varianta se zásobníkem. Nepřebírá se zde MIX časová konstanta
ani konkrétní výstupní permutace.

Zadání vytváří právě jednu klauzuli s hlavou x_k, jejíž předpoklady
jsou všichni přímí předchůdci k ve vstupních relacích. Zdroje jsou
fakty. Každé zařazení k do core následuje až po zařazení všech
jeho předchůdců. Pořadí prvních změn TRUTH na 1 je proto
topologické na zařazené množině. Je-li vstup acyklický, nezbyde
nezařazený vrchol: jinak každý vrchol zbytku má ve zbytku
předchůdce a konečným sledováním vznikne cyklus.

Na cyklickém vstupu dostaneme pouze odstraněnou část, nikoli
topologické pořadí všech n vrcholů; úplnost lze testovat |core|=n.
Smyčka je správně neodvoditelná a opakované vstupní relace nemění
výslednou množinu. Toto je přesná doména přirovnání k T.

Původní C používá zásobník místo fronty T, takže pořadí může být
jiné. U nového C se již pravdivé předpoklady mohou přeskočit před
jejich vyjmutím ze zásobníku. Doslovné slovo „asserted“ v původní
odpovědi se proto v nové verzi musí číst jako „already known true“;
potřebné pořadí změn TRUTH a vlastní výsledek zůstávají platné.
Pořadí vyjímání ze zásobníku není u této optimalizace totéž tvrzení.

## Úloha 48: obecné Hornovy klauzule — P0744

Přidej čerstvou proměnnou ⊥ do každé čistě negativní klauzule;
ostatní klauzule ponech. Vznikne definite systém G. Dosazení ⊥=0
jej vrací přesně na původní F, včetně případné prázdné klauzule,
která se změní na fakt ⊥. Je-li ⊥ v core G, každý model G ji má
pravdivou, a F tedy nemá model. Není-li tam, nejmenší model G má
⊥=0 a po omezení na staré proměnné dává model F. To dokazuje
obě implikace i bezpečné předčasné ukončení při odvození ⊥.

Přidá se jedna proměnná a nejvýše jeden literál na původní
klauzuli. Pro explicitně zapsaný CNF tedy příprava i C stojí
O(N+n), s N zahrnujícím také oddělovače/počet prázdných klauzulí.
Konstantní true/false, nepoužité proměnné i opakované klauzule
nevyžadují výjimku. Tím je Hornova část P0729 doložena; Kromova
část bude mít samostatný důkaz algoritmu K.

## Quickova alternativa a její potřebná doména — P0745

Odpověď odkazuje na konstrukci z 45(a), tedy na **indefinite** F,
pro něž F(1,…,1)=0. Definite vstup je už automaticky splnitelný;
nejprve ho přijmeme. Potom G=F∨(x_1∧…∧x_n) přidá právě
horní bod k množině modelů F. Všechny proměnné jsou v core G
právě tehdy, když G má jediný model, tento horní bod, tedy právě
když F nemá žádný model. Předpoklad indefinite je potřebný:
bez něj by např. F=x_1∧…∧x_n nebylo nesplnitelné, přestože
jeho core obsahuje všechny proměnné. Odkaz na bijekci 45(a)
dává přirozenou doménu alternativy; nejde zde o novou kartu.
Pro n=0 má tato doména pouze F=0 a argument nadále platí.

Převod do CNF plyne distributivitou přes všechny původní klauzule.
Definite klauzule se nemění. Čistě negativní klauzule
c=∨_{i∈R} ¬x_i se změní na ∧_{j∉R}(c∨x_j), protože členy
pro j∈R jsou tautologie. To je přesně vytištěný příklad pro R={w,y}.
Na vstupu jediné klauzule ¬x_1 vznikne n−1 odlišných klauzulí
¬x_1∨x_j, j=2,…,n. Žádnou z nich nelze vypustit: nastavení
x_1=1, x_j=0 a všech ostatních proměnných na 1 poruší pouze ji.
Zvětšení počtu klauzulí může být tedy Θ(n), jak text uvádí.
Nejde o dolní mez všech možných reprezentací s novými proměnnými;
právě jediné nové ⊥ takovému zvětšení v hlavním řešení zabrání.

## Úplná mapa p59 a přesné meze

P59: celý přepis (35) do CNF a význam gramatického core jsou P0731,
P0733–P0735; konkrétní (-, ++, *- mají P0734. Obecná odvoditelnost
je P0735; slib O(N+n), data a úplné C1 nyní P0737–P0742, včetně
pokračování na p60 a všech jeho známých nahrazení. Omezení na
explicitně rozvinuté klauzule je součástí důkazu, nevynechaný vstup.
Celý matematický obsah p59 má tedy argumentovou mapu.

P60 zůstává částečná: algoritmus a vazby 47/48 jsou hotové, příklad
sedmi komiků a Kromova část čekají. P85 nelze uzavřít kvůli přesně
vymezené P0713; odpovědi 49–51 na p543 dosud čekají. Bibliografii
Dowling–Gallier a Scutellà zde nepoužíváme jako důkaz a její přesné
historické údaje zůstávají výslovně neověřené. Žádný nový nález.
