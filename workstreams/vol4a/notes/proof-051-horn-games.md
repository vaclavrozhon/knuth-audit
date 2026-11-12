# Úloha 7.1.1–51: vítězné strategie jako Hornův core

Checkpoint X0080, P0753–P0757. Zadání p86/file103 a odpověď
p543/file560, images/proof-file103.png a proof-file560.png.
Konečný orientovaný graf, příznak hráče na tahu je součástí stavu.
Žádný běh nebo herní census.

Přebíráme obecný rankový důkaz a analýzu čítačů z
workstreams/vol1/parallel/linked-allocation/notes/game-analysis.md,
část „Obecný algoritmus a jeho důkaz“. Nepřebíráme z něj vojenský
census ani konkrétní strategii. Následující argument doplňuje přesně
čtyři propozice, volitelnou remízu C a druhou návštěvu stejného stavu.

## Překlad všech stavů a pravidel — P0753

Stav (v,A) znamená Alice na tahu; (v,B) Bob na tahu.
Význam čtyř propozic je:

| propozice | počáteční stav | kdo vynutí konečné vítězství |
|---|---|---|
| A+(v) | (v,A) | Alice |
| A−(v) | (v,A) | Bob |
| B+(v) | (v,B) | Bob |
| B−(v) | (v,B) | Alice |

Znaménko − tedy není booleovská negace +: při remíze mohou být
obě propozice pro stejný stav mimo core.

Při značce A hra ihned končí výhrou Alice, nezávisle na hráči
na tahu, takže vložíme fakta A+(v), B−(v). Při značce B jsou
fakta A−(v), B+(v). Výstupní hrany terminálů se nevyužívají;
slovo „otherwise“ v odpovědi je zde nezbytné a správné.

Pro každý neterminální v a každou hranu v→u vložíme

    A−(u) ⇒ B+(v),       B−(u) ⇒ A+(v).

Jde o vlastní volbu vítězného tahu: Bob jde do stavu, kde
Alice musí prohrát, respektive Alice jde do Bobova prohraného stavu.

Pro každý neoznačený v s následníky u_1,…,u_k navíc vložíme

    A+(u_1)∧…∧A+(u_k) ⇒ B−(v),
    B+(u_1)∧…∧B+(u_k) ⇒ A−(v).

Hráč na tahu totiž prohraje, pokud každý legální tah dá soupeři
vynutitelnou výhru. Pro k=0 jsou to fakta B−(v), A−(v), přesně
podle pravidla, že aktivní hráč bez tahu prohraje. U v označeného
C univerzální pravidla chybějí: aktivní hráč může přijmout remízu
i tehdy, když všechny tahy vedou k prohře. Existenciální pravidla
zůstávají, protože vítězný tah si může zvolit místo remízy.
C s nulovým stupněm proto správně nevynucuje prohru ani výhru.

## Správnost odvozených vítězství a opakování — P0754

Fakta z terminálů a nulového stupně mají rank 0. Každá nově
odvozená propozice má rank o 1 větší než rank použitého předpokladu
u existenciálního pravidla, respektive o 1 větší než maximum všech
předpokladů u neprázdného univerzálního pravidla. Hornův core
vzniká konečnými odvozeními, takže tyto ranky existují pro každou
jeho propozici; konkrétní minimální rank není potřebný.

Indukce podle odvození dokazuje vítěznou strategii. Na vlastním
tahu vítěz zvolí doloženého následníka s nižším rankem. Na tahu
soupeře vedou všichni následníci k nižším rankům; soupeř nemůže
přijmout C-remízu, protože univerzální pravidlo v C není přítomné.
Při vlastním tahu v C vítěz odmítne remízu a použije vítěznou hranu.

Rank klesá po každém tahu až k terminálu nebo prohře aktivního
hráče bez tahu. Stejný stav (v,hráč) se tedy nemůže opakovat.
Pravidlo o druhé návštěvě proto nepřeruší tuto strategii remízou.
Opakování samotného v s opačným hráčem není stejné opakování
a nebylo v tomto důkazu neprávem zakázáno.

Tím jsou správné všechny čtyři typy odvozených propozic. Obě
propozice pro týž stav nemohou být současně pravdivé: jejich dvě
vynucující strategie by v jedné partii požadovaly opačné výsledky.
Z absence + však ještě neplyne −; remízy jsou samostatné.

## Úplnost: co znamená neodvozená propozice — P0755

Označme W_A množinu stavů Alice-výhry popsanou core:
(v,A) pro A+(v) a (v,B) pro B−(v). Mimo W_A má Bob tuto
strategii, která zabrání Alicině výhře:

* Na tahu Alice mimo W_A nemůže žádná hrana vést do W_A,
  jinak by existenciální pravidlo zařadilo už aktuální stav.
  Jestliže přijme remízu C nebo nemá tah, Alice nevyhraje.
* Na neoznačeném Bobově tahu mimo W_A existuje následník
  mimo W_A, jinak by platilo univerzální pravidlo. Nulový stupeň
  zde není možný, protože by už šlo o fakt B−. Bob zvolí takového
  následníka.
* Na Bobově tahu v C může Bob rovnou přijmout remízu.
  Terminál A je celý ve W_A, terminál B Alici samozřejmě nevyhrává.

Pokud se nedosáhne terminálu nebo remízy C, konečnost 2|V|
stavů vynutí opakování stejného stavu; podle zadání je to remíza.
Alice tedy mimo W_A nemůže vynutit výhru. Symetrický argument
pro W_B dokazuje úplnost A− a B+ také. Společně s P0754 máme
všechny čtyři požadované ekvivalence, ne pouze lokální podmínky.

Opakování se zde hodnotí od čerstvého počátečního stavu, jak
požaduje zadání. U libovolné již rozehrané partie může být pro
rozhodování nutné přidat její dosavadní historii do stavu; nepřenášíme
výsledek bez této podmínky na hry s jinou pamětí opakování.

## Konstrukce, invariant C a náklady — P0756

Pro v vrcholů máme 4v propozic. Označme t počet A/B terminálů,
u počet neoznačených vrcholů a e' počet hran z neterminálů.
Máme 2t faktů, 2e' unárních klauzulí a 2u univerzálních klauzulí,
včetně nulových. Jejich celková délka včetně hlav je

    N = 2t + 4e' + 2u + 2Σ_{neoznačené x} outdegree(x)
      ≤ 2v + 6e.

Při duplicitních hranách se jejich násobnosti započítají do obou
stran stejně; lze je také předem odstranit. Konstrukce stojí O(v+e).
P0737–P0742 pak dávají korektní core v O(v+e) času i paměti.
Každá propozice se odvodí nejvýše jednou a C zpracuje všechny
předpoklady podle svých prokázaných invariantů, bez opakované
prohlídky všech herních pozic. Vnější obecná věta o determinaci
her není potřebná: strategie byly přímo zkonstruovány výše.

## Dodatek o šachu — P0757 partial v přesném rozsahu

Algoritmický princip je správný pro každou konečnou verzi
šachového stavového grafu, v níž stav obsahuje postavení, hráče
na tahu a všechny další údaje rozhodující o legálních tazích
a výsledku, případně relevantní historii opakování. Výhry,
prohry a povolené remízy lze reprezentovat terminály a volbami
jako výše. Proto je „v principu lze rozhodnout vynucenou výhru“
důsledkem P0753–P0756, při uvedeném úplném stavovém modelu.

Neztotožňujeme pravidlo druhé návštěvy z této úlohy automaticky
se všemi skutečnými šachovými pravidly. Dodatek nemá přesný
číselný odhad, definici velikosti ani fyzikální jednotku pro
srovnání grafu s vesmírem. Toto kvantitativní přirovnání nebylo
nezávisle doloženo; nečiníme z něj chybu algoritmu ani novou kartu.
P0757 zůstává partial pouze pro tuto vnější velikostní interpretaci.

## P0747 a stránkový stav

Primární [vydavatelská stránka](https://link.springer.com/chapter/10.1007/978-3-322-84809-3_5)
potvrzuje kapitolu Horn-Logik, s217–313, rok1994 a oba autory,
ale plné znění je předplatné. Náhled nedává argument §5.6 o
efektivním hledání XOR přeznačení. P0747 proto zůstává matematická
mezera; samotná ověřená bibliografie ji neuzavírá. Další dlouhé
hledání se nyní neprovádí.

Žádná celá stránka se nepovyšuje: p86 čeká na52–54 a p543 má
P0747 i přesně vymezený dodatek P0757. Základní matematická
část51 a všechny její hraniční případy jsou uzavřeny. Další52,
main-text frontier p60/file77 a čtení p218/file235 odděleně.
