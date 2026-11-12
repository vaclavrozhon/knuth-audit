# §2.4: obecné důkazy a úplné algoritmy

Rozsah: hlavní text 424–433, všech 15 úloh 433–434 a odpovědi 605–607.
Všechny tyto stránky byly přímo přečteny z originálních obrazů. K úloze 15
není v knize vytištěna odpověď. Níže je vlastní řešení. Známé opravy
aplikujeme podle `errata.md`. Nová chyba odpovědi 13 má samostatný stabilní
podklad `scope-builder-eof.md`; kořen ji nezávisle potvrdil jako C0061.

Dokazujeme strukturální model výslovně definovaný knihou. Není to úplná
specifikace všech dialektů COBOL: další jazyková omezení a přesný rozsah
porovnání dobových manuálů jsou v `sources.md`. Zejména úloha 8 sama říká
„according to the definition in the text“.

## 1. Model a význam odkazů

Les je posloupnost kořenových stromů, v nichž jsou děti každého vrcholu
uspořádány. Vrchol představuje jednu deklarovanou datovou položku, má jméno
a kladné číslo úrovně. **Skupina** je vrchol s alespoň jedním dítětem;
**elementární položka** je list. Předchůdce znamená striktního předka,
nikoli samotný vrchol. Přidáme virtuální kořen 0 pro celý les; jeho děti
jsou skutečné kořeny. Má úroveň 0 a je předkem každého skutečného vrcholu.
Hodnota NULL je také zapisována 0, ale nejde o alokovaný datový záznam.

Pořadí **preorder** navštíví nejprve vrchol a pak postupně celé podstromy
jeho dětí. V sekvenční reprezentaci očíslujeme skutečné vrcholy podle tohoto
pořadí 1,...,N. Jednotková velikost záznamu odpovídá sčítání 1 v odpovědích;
při velikosti c slov se adresové přírůstky násobí c.

Pro vrchol v značí `par(v)` jeho rodiče, `name(v)` jméno a `child(v)` první
dítě, případně 0. `sib(v)` je následující sourozenec, případně 0.
`prev(v)` je nejbližší dřívější výskyt stejného jména, případně 0.
Tabulka symbolů obsahuje `link(a)`, poslední výskyt jména a. Řetězec PREV
od `link(a)` obsahuje právě všechny výskyty a, bez opakování, odzadu.

Reference `(a0,a1,...,ar)`, r >= 0, označuje vrchol v, pokud name(v)=a0
a na cestě od jeho rodiče ke kořeni lze v tomto pořadí najít a1,...,ar.
Některé předky lze vynechat. Reference je jednoznačná právě tehdy, když ji
splňuje jediný vrchol. **Úplná kvalifikace** vrcholu je celé jeho jméno
následované jmény všech rodičů až po skutečný kořen, bez vynechání.

Pravidlo (a) knihy požaduje, aby všechny děti jednoho rodiče měly stejné
číslo úrovně, větší než číslo rodiče. Stejné zacházení se skutečnými kořeny
je zahrnuto virtuálním kořenem. PL/I varianta v úloze 3 nahrazuje rovnost
čísel sourozenců jejich nerostoucím pořadím.

## 2. Algoritmus A, preorder a čas: úlohy 1–2

Po zpracování libovolného neprázdného prefixu obsahuje zásobník A odspodu
sentinel `(0,0)` a přesně cestu ke právě přidanému vrcholu. Čísla úrovní
na této cestě přísně rostou. Každý záznam na cestě má SIB=0: budoucí pravý
sourozenec ještě nebyl přečten. Odkazy k již přečteným dětem, rodičům a
sourozencům jsou konečné; PREV a symbolové LINK přesně odpovídají prefixu.

Je-li nová úroveň L vyšší než vrchol zásobníku, nová položka je jeho první
dítě. Žádné předchozí dítě ještě neměl, neboť jinak by na zásobníku byl
poslední přečtený potomek. Krok A4 tedy správně nastaví CHILD. Je-li
zásobník pouze sentinel, nastaví FIRST.

Jinak A5 odebere všechny záznamy s úrovní vyšší než L. Jejich podstromy
jsou dokončeny a už nedostanou dalšího sourozence: nový záznam se nachází
výše. Narazí-li A5 na úroveň rovnou L, právě nalezený vrchol je předchozí
sourozenec nové položky. Po jeho odebrání je na vrcholu společný rodič.
SIB, PARENT a následné vložení do zásobníku tedy zachovají invariant.
Narazí-li na menší úroveň, byly by poslední uzavřený podstrom a nová
položka sourozenci s různými čísly; to právě porušuje pravidlo (a).
Žádný platný vstup proto není odmítnut a každý přijatý vstup pravidlo (a)
splňuje. Sentinel nemůže být při běžném kladném L odebrán.

Všechny potomky jedné položky čteme před následujícím sourozencem, takže
jde přesně o preorder, jak odpovídá úloha 1. Každý skutečný záznam se
jednou vloží a nejvýše jednou odebere. Vše ostatní stojí konstantní počet
operací na záznam; běh A je tedy Θ(N+1), případně Θ(t+1) do odmítnutí
prefixu délky t. Předpokládáme konstantní čas alokace a již nalezené
symbolové odkazy, jak stanoví kontrakt A. Zásobník má O(h+1) záznamů,
kde h je výška lesa. Případné hledání nebo čtení celých názvů v tabulce
symbolů není skrytou částí tohoto odhadu.

Tabulka (5) byla porovnána se skutečným vstupem (4), ne s ručně přiděleným
stromem: souhlasí všech 15 řádků všech pěti polí i osm symbolových LINK.
Například G4 je dítě F3, zatímco G8 je dítě F5; pozdější G9 je dítě C5.

## 3. PL/I úrovně: úloha 3

V PL/I je rodičem nového vrcholu poslední dosud otevřený vrchol s úrovní
menší než L. Je-li L větší než vrchol zásobníku, A4 se nemění. Jinak
odebíráme záznamy, dokud nové čelo nemá úroveň menší než L; poslední
odebraný záznam je bezprostředně předchozí sourozenec. Jeho SIB nastavíme
na novou položku. To je právě vytištěné A5'.

Po sobě jdoucí sourozenci mají nutně nerostoucí úrovně: při růstu by nová
položka byla potomkem předchozího sourozence. Naopak jakákoli posloupnost
kladných úrovní je tímto pravidlem jednoznačně rozložena na les; sentinel
zaručuje zastavení odebírání. V rámci skutečného PL/I začíná hlavní
struktura úrovní 1, což je omezení vstupní syntaxe navíc. Vzor
`1 A, 3 B, 5 C, 4 D, 2 E` dává děti B,E u A a děti C,D u B,
stejně jako normalizované úrovně `1,2,3,3,2`.

## 4. Vynucení pravidla (c): úloha 4

Nejdříve přesně odvodíme tvrzení v odpovědi. Vrchol v lze jednoznačně
pojmenovat právě tehdy, když je jednoznačná jeho úplná kvalifikace.
Jeden směr je okamžitý. Pro druhý: jakákoli platná reference k v je
podposloupností jeho úplné kvalifikace; pokud celou kvalifikaci splňuje
také w != v, stejnou podposloupnost splňuje i w. Žádné zkrácení nepomůže.

Pravidlo (c) je dále ekvivalentní následující lokální podmínce:

```
Pro žádné různé stejně pojmenované vrcholy x,y není par(x) předkem y.
```

Pokud par(x) je předkem y, úplnou kvalifikaci x splňuje také y; virtuální
rodič 0 znamená prosté jméno x. Obráceně zvolme nejednoznačný vrchol x
s nejmenší hloubkou. Jeho rodič u má jednoznačnou úplnou kvalifikaci
(nebo u=0). Výskyt úplné kvalifikace x u jiného y obsahuje předka z vrcholu
y, který splňuje úplnou kvalifikaci u. Jednoznačnost dává z=u, tedy u je
předkem y. Pro kořen x je stejné tvrzení automatické s u=0.

Při přidání nové položky v stačí projít všechny staré výskyty u stejného
jména přes PREV a zkontrolovat obě možnosti: par(v) je předkem u,
nebo par(u) je předkem v. První zjistíme cestou PARENT od u, druhou
členstvím par(u) v zásobníku předků v. Virtuální kořen se počítá vždy.
Všechny páry starých položek již byly zkontrolovány; žádné rodičovství
starých položek se nezmění. Indukce podle délky vstupu dokazuje jak
úplnost, tak nepřítomnost falešných odmítnutí.

Poznámka odpovědi, že pozdější B chybu odhalí při pokusu použít
nepojmenovatelnou položku, je správná: každá reference, kterou splňuje,
má alespoň druhého kandidáta. C naproti tomu může do takových podstromů
vstoupit přes kořenové reference. Neplyne z toho, že C má správně
zpracovávat libovolné porušení předpokladů, například duplicitní sourozence.

## 5. Algoritmus B a seznam kvalifikátorů: úloha 5

Vnější smyčka B bere všechny výskyty a0 přes PREV. Pro pevného kandidáta
v hledá v cestě rodičů postupně nejbližší výskyt a1, potom a2 atd.
Tento hladový výběr je úplný: proti libovolnému úspěšnému vložení
kvalifikátorů leží první hladová volba stejně nízko nebo níže. Indukcí
platí totéž pro každou další volbu, takže hladová volba nikdy neztratí
možnost pokračovat výše. Každý nalezený kandidát referenci skutečně
splňuje. Q tedy po prozkoumaném prefixu kandidátů obsahuje jedinou dosud
nalezenou shodu, nebo 0; druhá shoda správně způsobí hlášení nejednoznačnosti.
Při vyčerpání PREV znamená Q=0 neexistenci, jinak jedinou shodu.

Pro r=0 se ihned provede B3, jak je potřebné pro nekvalifikované jméno.
U každého kandidáta se S pohybuje jen k rodiči; konečnost obou cest
dokazuje zastavení. Při f výskytech jména a0 a maximální výšce h je čas
O(f(h+1)+r), včetně načtení reference. Nevyžaduje pravidlo (c) celé tabulky:
umí korektně hlásit i konkrétní nejednoznačnou referenci.

V úloze 5 je vstup neprázdný konečný seznam, jehož záznamy mají pole INFO
(symbolový odkaz) a RLINK (následník, poslední má 0). Uchováváme jeho
počátek T. Při každém novém kandidátovi nastavíme K=T; test k<r nahradíme
RLINK(K)!=0, zvýšení k nahrazuje K=RLINK(K) a ak je INFO(K).
Počáteční kandidát je LINK(INFO(T)). Tak K přesně označuje k-tý
kvalifikátor v původním důkazu. Není nutná žádná souvislost adres členů
seznamu ani jeho předem známá délka.

## 6. Přednost úplné kvalifikace v PL/I: úloha 6

První průchod použije B s dvěma změnami: každý další kvalifikátor musí
sedět hned u rodiče (při neshodě kandidáta opustíme), a po posledním
kvalifikátoru musí mít právě nalezený vrchol rodiče 0. Tím se rozpoznají
přesně úplné kvalifikace. Nejsou-li nalezeny, spustí se původní B.

Za předpokladu různých jmen sourozenců včetně kořenů je úplná kvalifikace
jednoznačná: z kořene je každá další jmenná volba jediná. První průchod
proto má nanejvýš jednu shodu. Její přednost před libovolnými neúplnými
shodami je přesně požadované PL/I pravidlo. Pokud úplná shoda není,
jednoznačnost/neexistenci rozhodne druhý průchod podle části 5.
Příklad `1 A,2 A,3 A` dává postupně A, A.A a A.A.A při skutečném
PL/I zápisu od kořene s tečkami. Dobový manuál z července 1965 obsahuje
právě toto pravidlo i tento příklad; viz `sources.md`.

## 7. CORRESPONDING: hlavní definice, úlohy 7–9

Pro dvojici vrcholů (u,v) definujme její **relativní jmennou cestu**:
pro potomka x vrcholu u je to posloupnost jmen od dítěte u po x.
U x=u je cesta prázdná. Odpovídající dvojice (x,y) mají stejné relativní
cesty v obou podstromech a alespoň jeden z x,y je list. Po aplikaci
známé opravy z 15.10.2007 jde přesně o definici (8). Nulová délka cesty
je přípustná a je nutná pro elementární kořen.

Při různých jménech sourozenců má tento požadavek rekurzivní podobu:

```
F(u,v):
    pokud je u nebo v list: vypiš (u,v) a skonči;
    jinak pro každé jméno a společné přímým dětem u a v:
        F(jediné dítě u se jménem a, jediné dítě v se jménem a).
```

Pokud je některý kořen list, žádná delší společná cesta neexistuje.
Jinak každá společná neprázdná cesta začíná společným jménem dítěte a
zbývající úsek je právě menší rekurzivní problém. To dokazuje rovnocennost
rekurze s definicí, včetně úplnosti a neopakování výstupních dvojic.

C je přímá implementace této rekurze s návratem přes PARENT. Invariant
C2: P,Q představují právě zvolenou dvojici se stejnou relativní cestou.
Je-li jeden list, C2 vypíše jediný přípustný výstup pro tuto rekurzivní
větev a C5 ji opustí. Jinak C2 vstoupí do prvních dětí. V C3 je P
aktuální dítě prvního rodiče, Q postupně prochází druhou rodinu od jejího
počátku. Předchozí neshodná jména nebyla použitelná. Jediná shoda spustí
menší rekurzivní problém; jeho návrat má opět tytéž P,Q.

Krok C4 buď vybere následující P a vrátí Q na CHILD(PARENT(Q)), nebo,
je-li rodina P hotova, vrátí oba ukazatele na jejich rodiče. PARENT(Q)
je tentýž rodič i po neúspěšném prohledání celé druhé rodiny. Žádný
podstrom se po návratu znovu neprochází. Indukce podle součtu velikostí
obou podstromů tedy dokazuje výpis F(u,v) a návrat se stejnými u,v.
Na nejvyšší úrovni C5 rozpozná P=P0 a skončí. Výpis je v preorder
prvního stromu. Zásobník simulují existující PARENT; v pracovních
registrech stačí konstantní prostor.

Čas odpovídá součtu d(u)d(v) přes páry vnitřních vrcholů, kam rekurze
vstoupí, plus počet navštívených a vypsaných párů; d je počet dětí.
Vyhledávání celé druhé rodiny pro každé první dítě může být kvadratické.
Text sám na tuto jedinou vyhledávací část upozorňuje a úloha 11 ji zlepšuje.

V úloze 7 jsou kořeny SALES a PURCHASES. Jejich společné první děti jsou
DATE a TRANSACTION. Pod DATE vyjdou právě MONTH,DAY,YEAR bez ohledu na
rozdílné pořadí MONTH a DAY; pod TRANSACTION právě ITEM,QUANTITY,PRICE,TAX.
BUYER a SHIPPER se neshodují, a proto se NAME ani ADDRESS pod nimi
nekopírují. Celkem vznikne sedm vytištěných MOVE. Ve druhém skutečném
příkladu (4) vzniknou přesně B3→B5 a G4→G8.

Úloha 8 porovnává expanzi do dvojic MOVE podle knihovní definice. Obsahuje
právě jedinou dvojici (u,v), pokud jeden z kořenů je list. Jsou-li oba
skupiny, (u,v) vůbec nevyhovuje podmínce elementárnosti, a tudíž expanze
není totožná s příkazem MOVE u TO v. Toto není tvrzení o nemožnosti
náhodně stejného účinku na bajty u dvou konkrétních formátů; formáty
kniha již na 424 výslovně vynechala. Ani nejde o tvrzení, že všechny
dobové kompilátory dovolovaly elementární operand CORRESPONDING.

## 8. Odstranění NAME: úloha 10

Test name(S)=a lze nahradit hledáním S v celém PREV řetězci od link(a).
Řetězec obsahuje přesně všechny a; dosažení 0 znamená neúspěch.
Test name(P)=name(Q) lze nahradit porovnáním prvních výskytů jejich
PREV řetězců. Výskyty téhož jména mají stejný první vrchol, různá jména
mají disjunktní řetězce. Nenulovost vstupních P,Q je zde součástí C3.

Při monotónních adresách je rychlejší slučování obou klesajících řetězců:
dokud jsou oba ukazatele nenulové a různé, posuneme ten větší na PREV.
Pokud jména souhlasí, menší ukazatel je na řetězci většího a nemůže být
přeskočen; nastane rovnost kladných adres. U různých jmen taková rovnost
nemůže nastat. Dosažení 0 znamená neúspěch. Konečnost a správnost jsou
tedy nezávislé na případném rozdílu délek obou řetězců.

## 9. Zrychlení: úloha 11

Pole SIB1(P)=CHILD(PARENT(P)) nahradí dvě dereference jednou; jde skutečně
jen o konstantní zlepšení C4. Podstatnější je seřadit každou rodinu podle
symbolových odkazů NAME (libovolné pevné úplné uspořádání jmen stačí).
Úplná konstrukce této varianty může nejprve provést A, potom pro každou
rodinu seřadit seznam jejích členů a přepsat CHILD a SIB. PARENT, NAME a
PREV zůstávají platné; fyzické pořadí položek se nemění. Čas této přípravy
je O(N log N) porovnáním, nebo přesněji součet O(d log(d+1)) po rodinách.
Další informace určující rozložení dat nesmí být odvozována z nového
pořadí SIB; od počátku jde o alternativní strategii reprezentace.

Vyhledávání společných dětí se nyní provádí takto:

```
Merged(u,v):
    pokud je jeden list: vypiš (u,v); vrať se;
    P = CHILD(u); Q = CHILD(v)
    dokud P != 0 a Q != 0:
        pokud NAME(P) < NAME(Q): P = SIB(P)
        jinak pokud NAME(Q) < NAME(P): Q = SIB(Q)
        jinak:
            Merged(P,Q)
            P = SIB(P); Q = SIB(Q)
```

Menší jméno už nemůže mít protějšek dále ve druhém seřazeném seznamu,
proto se bezpečně přeskočí. Rovné dvojice jsou přesně společné členy.
Indukce z části 7 dokazuje celý algoritmus. Každá rodina se nyní projde
jednou, O(d(u)+d(v)); protože unikátní jména sourozenců určují pro každý
první vrchol nejvýše jeden druhý, celkový čas dotazu je O(Nu+Nv), kde Nu,Nv
jsou velikosti vstupních podstromů. Konečné seřazení odstraňuje opakované
vyhledávání, nikoli samotnou nutnost porovnat jména nebo vypsat výsledky.
Úloha požaduje zrychlit B nebo C; tím je úplně vyřešena pro C.

## 10. Dvě pole a intervaly: úloha 12 a odkaz §2.3.3

V preorder tvoří podstrom v souvislý interval. Důkaz indukcí: po v jdou
souvislé, navazující intervaly všech jeho dětí, a před jejich dokončením
se žádný vrchol mimo podstrom nenavštíví. Poslední vrchol podstromu je
list: kdyby měl dítě, po něm by následoval další vrchol. Definujeme
`scope(v)` jako jeho adresu. Potom přesně platí:

```
v je list              <=> scope(v)=v
u je striktní předek v <=> u < v <= scope(u).
```

Neostrá pravá nerovnost je skutečně v originálu 434 i 606; OCR ji často
ztrácí. PREV zůstává zachováno. Řetězce tedy implicitně uchovávají
příslušnost ke jménům, intervaly celou stromovou strukturu.

B'' z odpovědi 12 pro každý další kvalifikátor a prochází jeho PREV
řetězec od posledního výskytu a hledá první R se `R<S<=scope(R)`.
To jsou přesně předci S s daným jménem. Předci jednoho vrcholu tvoří
cestu a jejich adresy rostou s hloubkou. První nalezené R má největší
adresu, tedy je nejbližší vhodný předek. B'' tak vybírá přesně tytéž
kvalifikátory jako B; důkaz části 5 se přenáší beze změny. Nevyužívá
skryté NAME ani PARENT.

Větu „This algorithm does not adapt to the PL/I convention“ je třeba
číst ve vztahu k jednoduché modifikaci B z úlohy 6: samotný intervalový
test rozpoznává předka, nikoli bezprostředního rodiče. Není to
informační nemožnost reprezentace. Například rodiče v lze získat jako
největší u<v se scope(u)>=v, a tak s dodatečným průchodem testovat i
úplnou kvalifikaci. Nevytváříme z této zkratky nový nález nemožnosti.

Přímé přečtení originálu §2.3.3, p350, (5), uzavírá křížový odkaz:
tam SCOPE ukazuje na první adresu **za** podstromem; v úloze 2.4-12 na
poslední adresu **v** podstromu. Pro shodnou normalizaci adres tedy
`scope_2.3.3(v)=scope_2.4(v)+c`. Tvrzení pro list se mění z v+c na v,
test potomka z `< scope_2.3.3` na `<= scope_2.4`. Nejde o rozpor;
obě konvence jsou v místě definice výslovné. Odkaz „Compare with (5)“
i opačný odkaz z 350 míří na správnou techniku.

Všech 15 hodnot SCOPE v příkladu 434 souhlasí se skutečnými podstromy
příkladu (4), stejně jako všechny PREV; viz model a uložený výsledek.

## 11. Konstrukce SCOPE: úloha 13

Běžná část odpovědi je správná: při odebrání skutečného vrcholu ze
zásobníku v A5 je nová položka Q první položkou mimo jeho podstrom,
takže poslední uvnitř je Q−1. To platí jak pro opakované odstraňování
vyšších úrovní, tak pro poslední odebrání stejné úrovně.

Vytištěné EOF ukončení ovšem odebere i `(0,NULL)` a zapisuje do
SCOPE(NULL); viz samostatný nález C0061. Úplná oprava je přímá větev
v A2: při konci vstupu vezmi N jako adresu poslední skutečné položky,
odebírej jen kladné úrovně a všem odebraným p nastav scope(p)=N;
potom skonči. Nealokuje se fiktivní položka ani se nepoužije A3.

Invariant cesty z části 2 ukazuje, že právě zbylé skutečné vrcholy mají
podstrom končící v N. Všechny dříve uzavřené vrcholy již dostaly správný
scope. Každý záznam je uzavřen jednou, proto opravená konstrukce stojí
Θ(N+1) času a O(h+1) pomocného prostoru. Pro prázdný vstup se neodebere
nic. `build_scope` výslovně obsahuje tuto opravu; jeho úspěšný test není
vydáván za úspěch původního chybného EOF.

## 12. CORRESPONDING pouze z PREV a SCOPE: úloha 14

Při neelementárním p je první dítě p+1. Má-li p rodiče u, následující
sourozenec existuje právě když scope(p)<scope(u), a tehdy má adresu
scope(p)+1. Při rovnosti scope(p)=scope(u) je p poslední dítě. Tato
tvrzení jsou přímými důsledky navazujících intervalů v části 10.

C' ukládá na pomocný zásobník páry právě rozevřených rodičů (u,v).
V C2' tedy používá p+1,q+1 místo CHILD. V C3' se shoda jmen zjistí
výhradně z PREV podle části 8; při neshodě se Q posune na scope(Q)+1,
pokud ještě neopustí rodinu vrcholu v na čele zásobníku. C4' obdobně
posune P, vrátí Q na v+1, nebo po dokončení rodiny vyzvedne pár (u,v)
ze zásobníku a pokračuje návratem.

Zásobník tedy přesně uchovává informace, které C získával z PARENT;
každý krok C' odpovídá stejnému kroku C. Část 7 dokazuje správnost,
úplnost i zastavení. Test prázdného zásobníku v C5' funguje také při
elementárním kořeni: C2' vypíše pár ještě před jakýmkoli vložením.
Žádný jiný krok nečte vrchol prázdného zásobníku, protože do C3'/C4'
se poprvé vstoupí až po vložení rodičů. Cena navíc spočívá v hledání
stejného jména přes PREV; prostor zásobníku je O(min(hu,hv)+1).

## 13. A bez zvláštního zásobníku: úloha 15

Využijeme invariant, že každý aktivní záznam na cestě A má dosud SIB=0.
Do jeho pole SIB dočasně uložíme číslo úrovně. Jeho odkaz PARENT současně
plní úlohu odkazu na předchozí položku zásobníku. Registr TOP ukazuje na
čelo této cesty, TOP=0 znamená prázdnou cestu s virtuální úrovní 0.
Aktivní a dokončené záznamy rozlišujeme samotnou cestou od TOP; netřeba
značkového bitu ani nerozlišitelného čtení SIB jako úrovně či adresy.

Úplný algoritmus pro novou dvojici (L,a) a nově alokovaný Q:

```
PREV(Q)=LINK(a); LINK(a)=Q; NAME(Q)=a; CHILD(Q)=0
oldlevel = (SIB(TOP), pokud TOP!=0; jinak 0)
pokud oldlevel < L:
    pokud TOP!=0: CHILD(TOP)=Q; jinak FIRST=Q
    parent=TOP
jinak:
    dokud TOP!=0 a SIB(TOP)>L:
        old=TOP; TOP=PARENT(old); SIB(old)=0
    pokud (SIB(TOP), nebo 0 při TOP=0) < L: chyba smíšených úrovní
    old=TOP; parent=PARENT(old); SIB(old)=Q
PARENT(Q)=parent; SIB(Q)=L; TOP=Q
```

Na konci vstupu opakujeme `old=TOP; TOP=PARENT(old); SIB(old)=0`, dokud
TOP není 0. Tím se všechny zbývající dočasné úrovně změní na konečné
prázdné sourozenecké odkazy. Na počátku jsou TOP=FIRST=0 a symbolové
LINK nulové. Úrovně a adresy se jako v knižním slovním modelu musí vejít
do jednoho příslušného pole.

Indukcí po každém vstupu je PARENT cesta od TOP přesně původní zásobník
bez sentinelu a SIB na ní obsahuje původní čísla úrovní. Při odstranění
vyšší úrovně je podstrom dokončen bez dalšího sourozence, takže finální
SIB=0 je správně. Při nalezení stejné úrovně se předchozí sourozenec
odstraní z aktivní cesty a SIB=Q je jeho správný konečný odkaz. Při růstu
zůstane dosavadní čelo aktivním rodičem. Ostatní pole mají stejnou hodnotu
jako v A. EOF převede všechny zbývající dočasné hodnoty na jejich správná
nulová SIB, a výstup proto zcela souhlasí s A.

Počet vložení a odstranění je opět O(N); pomocný prostor tvoří pouze
konstantní počet registrů. Nepoužíváme dodatečný zásobník, rekurzi ani
uložené pole úrovní mimo pět předepsaných polí výsledné tabulky.

## 14. Redundantní pole v hlavním textu 432–433

Tvrzení o možnosti rekonstruovat některá pole má přímé algoritmy.
Při odstranění PARENT můžeme poslední SIB v každé rodině nahradit
odkazem na rodiče, označeným bitem. Rodiče libovolného dítěte najdeme
postupem přes sourozence až k tomuto poslednímu odkazu. V preorder
sekvenční tabulce všechny skutečné sourozenecké odkazy míří na vyšší
adresu a rodičovské vlákno na nižší (nebo na NULL=0); značku proto může
nahradit test směru adres. Průchod rodinou je konečný, ale vyhledání
rodiče může stát až její velikost; text správně uvádí zpomalení B5.
Pro C lze rodiče místo toho udržovat pomocným zásobníkem, jak konkrétně
dokládá úloha 14.

První dítě v preorder, pokud existuje, leží ihned po rodiči. CHILD tedy
lze nahradit jediným bitem list/skupina. Máme-li PARENT a známý konec N,
platí `v má dítě <=> v<N a PARENT(v+1)=v`. Hraniční test zabraňuje čtení
za tabulkou u posledního záznamu; tvrzení textu o sousední položce je
v této běžné konvenci platné. NAME lze odstranit postupy úlohy 10.
Žádná z těchto úspor neznamená, že všechny odkazy lze odstranit současně
se zachováním stejných kroků: konkrétní úplnou dvoupolovou alternativou
jsou až úlohy 12–14. Výroky o praktickém významu a obvyklém zpomalení
nejsou kvantifikovaným tvrzením o nejhorším poměru dob běhu.

## 15. Reprodukovatelná doplňková kontrola

`algorithms.py` obsahuje vykonatelné varianty výše, `check_algorithms.py`
porovnává jejich výstupy s nezávislými definicemi rodičů, předků a cest.
Jeden úspěšný běh je uložen v `results/algorithms.json` a nebyl opakován.
Pro úrovně 1–4 a délku 0–6 prošlo všech 5461 posloupností včetně
odmítnutí neplatných COBOL vstupů a přijetí PL/I vstupů. Dále prošlo
10066 všech lesů do šesti vrcholů se jmény A/B, 362376 dotazů,
46462 dvojic kořenů pro obě C, 341706 porovnání jmen a 10066 kontrol
pravidla (c). Testy obsahují skutečné tabulky a příklady knihy.

Srovnávací model rodiče hledá přímo v celém dřívějším prefixu; kvalifikace
vyjmenovává podposloupnosti celé cesty, odpovídající dvojice vyjmenovává
všechny páry vrcholů a porovnává jejich relativní cesty. Tyto oracle
neopakují smyčky B ani C. Obecnou správnost však dokládají výše uvedené
důkazy, nikoli konečný rozsah výpočtu.
