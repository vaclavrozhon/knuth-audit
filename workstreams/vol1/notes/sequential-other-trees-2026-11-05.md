# Souvislý průchod §2.3.3 — 5. listopadu 2026

X0972: obrazově přečteny celé strany 348–362 a 575–577 prvního dotisku
1997, včetně všech 19 zadání, tabulek, diagramů a odpovědí. Přezkoušeny
obecné důkazy v `other-trees-sequential.md`, `other-trees-equivalence.md`
a `other-trees-polynomial-proofs.md`. Převzaté pramenné kolace jsou
`equivalence-originals-root-review.md`, `burks-original-root-review.md`
a `other-trees-originals-root-review.md`. Jejich přesný dřívější rozsah
četby zůstává zachován; není tím prohlašována nová četba celých pramenů.

## Reprezentace, F a úlohy 1–6, 16–19

Podstrom tvoří souvislý preorder interval. RLINK končí právě za tímto
intervalem, takže se jeho oblouky nekříží. List je posledním uzlem nebo
uzlem těsně před cílem některého RLINK. Tagy určují otevřené pravé odkazy
zásobníkem; po posledním listu již není žádný nevyplněný odkaz, který by
bylo třeba doplnit. Jde o rekonstrukci při průchodu, nikoli o příslib
konstantního náhodného přístupu z pouhých tagů.

SCOPE(P)=P+c právě pro list při délce uzlu c. Každý zvláštní linkový
uzel nahrazuje jeden nenulový RLINK; v neprázdném lese je jich méně
než původních uzlů. Pro prázdný les jsou oba počty nula. Příklad349
má nesprávné závorky, známé opravení odpovídá kresbě a předchozí sekci.
Po opravě jde stále o A(B,C(K)),D(E(H),F(J),G).

Všechna zobrazená pořadí a odkazy349–351 souhlasí: preorder
A B C K D E H F J G, postorder B K C A H E J F G D, family order
A D E F G J H B C K a level order A D B C E F G K H J. Family order
je obrácený binární postorder; používá zásobník nevyřízených rodin,
level order frontu. Fronta v úloze1 rekonstruuje LLINK podle konců rodin.

F pro podstrom zachová libovolný původní obsah zásobníku a přidá právě
hodnotu jeho kořene. Děti jsou vyhodnoceny zleva, takže na vrcholu jsou
zprava; odstranění jejich d hodnot a vložení výsledku dává indukci.
Obrácený preorder v úloze2 obrátí pořadí dětí i výsledných kořenů.
F4 a odpověď2 mají známou chybu adresového kroku: P±c, nikoli P±1.
Neprázdnost je v zadání F explicitní.

Úloha3 ukládá mezivýsledné derivace do vnějších RLINK jejich kořenů.
Po odebrání výsledků dětí lze volat DIFF nad původními nepoškozenými
operandy a výsledek vložit zpět. Kořenový vnější odkaz nepatří dovnitř
kopírovaného podstromu. Úloha4 má 2n odkazů v původním tvaru proti
(n−m)+(2n−m)=3n−2m v novém; INFO je stále n polí. Obrázek352 má
15 uzlů, z toho 10 informačních listů. Původní 6/60 bytů je známá chyba
proti pěti bytům INFO v MIX slově. Pravé nitě v úloze5 opakují PARENT;
levé mohou pomoci s předchozím sourozencem, zvlášť při vysokém stupni.
PARENT určuje orientovaný les, nikoli pořadí sourozenců.

V úloze6 je nutné uchovat původní následující Q před přepsáním RLINK(P).
Vložení P na začátek rodiny určené PARENT zpracuje každý uzel jednou
v O(n), bez topologického předpokladu o vstupním pořadí. Obrázek353
má chybějící rodičovský odkaz C→A; známá náhrada Fig.26 ho doplňuje.
Kruhové varianty Fig.27 a rozlišení 3²=9 kombinací linků jsou správné.

G v úloze17 navštíví při obráceném postorder rodiče před potomky.
Zásobník obsahuje hodnoty rodičů dosud nezačatých podstromů; po návštěvě
uzlu se vloží d kopií jeho hodnoty. Součet vložení je n−1. Paměť je
nejvýše lineární, není obecně omezena pouze výškou: hvězda vloží n−1
hodnot najednou. Původní P−1 je známě opraveno na P−c.

P1–P5 v úloze18 uchovává v I otevřené uzly, v D jejich dosavadní počty
dětí a v R pravé hranice podstromů. Horní hranice >j+1 znamená první
dítě, jinak se vydá dokončený uzel. Skutečný pravý sourozenec odstraní
svou hranici a zahájí další blok. Každý uzel se jednou otevře a vydá,
čas i nejhorší paměť jsou O(n). Počáteční n+1 a D=0 tvoří fiktivního
rodiče lesa; pro n=0 algoritmus skončí ještě před přístupem k poli.
Tabulky362 souhlasí, INFO místo INFO1 v P3 je známá oprava.

Úloha19: interval podstromu k je [k,k+d_k]. Podmínky k+d_k≤n a
j+d_j≤k+d_k pro k≤j≤k+d_k přesně vyjadřují vnoření. Inverze postupně
bere maximální blok prvního kořene a rozloží jej na dětské bloky;
je jednoznačná indukcí. Minimum dvou platných posloupností je platné,
protože každý jeho interval leží uvnitř obou původních intervalů.
Největší posloupnost (n−1,n−2,...,0) zaručuje společnou horní mez;
minimum všech horních mezí dává spojení. Souřadnicové maximum obecně
neplatí: (1,0,0) a (0,1,0) mají spojení (2,1,0), ne (1,1,0).

Inverze preorder čísel v postorder počítají právě vlastní potomky.
Postorder varianta má interval [k−c_k,k]. Převod první dítě/sourozenec
dává c_k velikost levého podstromu v inorder, duální převod dává d_k
pravou velikost. Dříve přijatý křížový odkaz V3 481/718 a převod
Pallo w_i=c_i+1 zůstávají zachovány, bez tvrzení o auditu celého V3.

## Ekvivalence a překryvy polí

E zachovává invariant: orientované stromy jsou přesně dosavadní třídy
ekvivalence. Spojení různých kořenů nevytvoří cyklus. Opakování E3
v originálu i dvě smyčky v nové formulaci skončí v kořenech. Vzorové
pole po všech dvojicích je (5,0,2,2,0,8,2,2,8); obrázky a tři třídy
před poslední dvojicí souhlasí. Nevyvážené dvojice (1,2),(1,3),...,(1,n)
vytvoří řetězec a (n−1)(n−2)/2 kroků hledání.

**Pozor na originál odpovědi10:** srovnává **absolutní hodnoty**
záporných kořenových velikostí, |PARENT[j]|>|PARENT[k]|. Sazba opravdu
obsahuje oba moduly; nejde o obrácené porovnání záporných čísel.
Po případné výměně je j menší strom, E4 ho připojí ke k. Při každém
zvýšení hloubky pevného uzlu se velikost komponenty alespoň zdvojnásobí,
tedy hloubka≤floor(log₂ n). Komprese cest zachová komponenty a kořenové
velikosti; v této části netvrdíme nedokázanou jemnější amortizovanou mez.

Úloha11 překládá index podél hrany o DELTA. Ve stejném kořeni musí
převedené indexy souhlasit; v různých kořenech nastaví DELTA(Q)=j−k
a posune minimum/maximum mezí. Interval [−5,14] má 20 míst, jedno
z nich je nedeklarovaná mezera za A[1], kterou souvislý blok vyžaduje.
Rovnice smějí obsahovat indexy mimo deklarovaný rozsah: určují posun,
nepřidávají nové deklarované buňky. T1–T3 i tabulka361 souhlasí.
Přímá kolace Galler–Fischer301–303/506 už dokládá jak tuto konstrukci,
tak atribuci E; vady jejich externí Fig.1 nejsou vadami TAOCP.

## Polynomy, A a úlohy12–15

Kanonický uzel je skalár, nebo řádek podle největší proměnné. Řádek
obsahuje povinný exponent0 a alespoň jeden nenulový kladný člen;
koeficienty obsahují jen menší proměnné. Všechny obousměrné a rodičovské
vazby i hodnoty Fig.28 byly porovnány s 3+x²+xyz+z³−3xz³. Pole EXP
v navržené MIX reprezentaci má omezenou šířku; abstraktní A pracuje
s přesnými koeficienty a předpokládá dostatek uzlů, neslibuje řešení
aritmetického přetečení či selhání alokace.

A1 porovnává proměnné a sestupuje po nulových koeficientech. A2 obalí
původní Q novou proměnnou, přemístí jeho obsah do koeficientu exponentu0
a opraví UP všech dětí. A4 prochází kladné exponenty P sestupně, A5
vloží chybějící koeficient do správného místa kružnice. A8 odstraní
právě nulový kladný skalár. Řádek s jediným nulovým exponentem se smí
zrušit až po dokončení kladných exponentů P; to zajišťují oba testy
v A8. A9 povýší koeficient, zachová vnější vazby rodiče a opraví UP
převzatých dětí. A10 správně synchronizuje rodičovský rámec P při
kaskádě vyrušení; A7/A11 vrátí oba ukazatele do původních kořenů.

Invariant dovoluje přechodné jednočlenné řádky a nuly čekající na
odstranění. Požadovat kanonicitu po každé instrukci by bylo chybně.
Rekurzivní specifikace klesá podle největší proměnné; konečné seznamy
a nulové zarážky zaručují ukončení všech vnitřních smyček. Knižní
příklad končí 3+xy a navštíví A1–A11. Úloha12 má obě odpovědi ano;
v A8 se nikdy neuvolní kořen exponentu0. Pro oba vstupy do A8 platí
EXP(P)=EXP(Q) a CV(UP(P))=CV(UP(Q)), jak vyžaduje úloha13.

Úloha15 násobí dvojice koeficientů podle největší proměnné, rekurzivně
v menších proměnných a sčítá stejný exponent e+f dokázaným A. Nulové
kladné koeficienty odstraní a řádek normalizuje. Pomocná tabulka
exponent→kořen a rekurze jsou dovolenou vlastností našeho řešení;
zadání nevyžaduje MIX ani provedení bez zásobníku.

### C0094 — vysvětlení A2 nesprávně nazývá vložený polynom nulovým

Na358 je nově vložený uzel R popsán jako „dummy zero polynomial“.
Samotné instrukce jsou správné, ale nastavují CV(R)=staré CV(Q)
a DOWN(R)=staré DOWN(Q), tedy zachovávají **původní polynom Q**.
EXP(R)=0 je exponent nové proměnné, nikoli hodnota koeficientu.

Nejmenší jasný příklad je P=x a Q=1. A1 zvolí A2. Nový R má
CV=1, DOWN=null, EXP=0; jeho polynom je1, nikoli0. Q nyní dočasně
reprezentuje 1*x⁰. Následné sčítání skončí správným x+1. Bezpečné
vysvětlení zní „move the old polynomial into an exponent-zero child“.
Jde o **confirmed, low**, chybu vysvětlení, ne výsledku algoritmu.

### C0095 — rozsah neformálního tvrzení o rychlosti

Na359 text slibuje výrazně rychlejší A než §2.2.4A při málo členech P
a mnoha členech Q. Vynechání velkých podstromů může pomoci, ale samotný
poměr počtů členů k tomu nestačí. Pro P=x a Q=x+x²+...+xⁿ sestoupí A
k povinným nulovým koeficientům, pak v A4 projde celý řádek Q od
exponentu n až k1. To je n levých odkazů. Seznamový algoritmus rovněž
navštíví všech n nenulových členů Q; oba jsou na této rodině Θ(n).

Tím se nevyvrací zrychlení na vhodně větvených vstupech ani se neurčuje
přesný poměr strojových časů. Protože „much faster“ je neformální,
zůstává **candidate, low** k posouzení rozsahu formulace. Bezpečné
znění by slibovalo možnost zrychlení, když se skutečně přeskakují
velké části Q. Main a stránka359 zůstávají partial kvůli této otázce;
správnost A a úlohy14 tím nejsou otevřeny.

Nový malý reproduktor `check_tree_addition_boundary_notes.py` používá
nezměněný doslovný `add_printed`. Trasováním přečte uzel po A2 a levé
odkazy A4; výsledek porovná s nezávislým plochým slovníkem. Sedm
případů, nejvýše n=64, proběhlo s nice15 za zlomek sekundy. Výstup je
`results/sequential-tree-addition-boundary-notes.json`. Dřívější celé
testy 6918 lesů,6962 sčítání,809 násobení a slučování se neopakovaly.

## Prameny, errata a uzavření

Přímé starší kolace Burks–Warren–Wright53–57 a Galler–Fischer301–303/506
zůstávají přijaté. Pallo1993 na341–343/348 podporuje převod w_i=c_i+1;
Tamari1964 na91–93/107 výslovně rozlišuje zavedení v disertaci1951
a pozdější důkaz. To nepředstírá četbu chybějících originálů.

Podle nového uživatelského pokynu výslovně přeskakujeme:

- Salton, CACM5(1962),103–114, DOI10.1145/366792.366828, a alternativní
  ISR-1/AFCRL-62-77, oddílII-1 ažII-44. Přesná metadata jsou známa,
  vlastní text s použitím level order dosud chybí.
- Přímý nezávislý pramen k soukromým atribucím McIlroy/Tritter
  v odpovědi10. Matematika obou úprav je vyřešená.
- Ward–Zedan, FAC26(2014),993–1031, DOI10.1007/s00165-013-0287-2,
  celý relevantní §5. Získaný fragment5.6 není celý důkaz. Úlohy14–15
  mají naše nezávislé obecné řešení.
- Pallo1986, Computer Journal29,171–175, DOI10.1093/comjnl/29.2.171,
  a souvislý text Tamariho disertace Paris1951. Úloha19 má obecný důkaz
  i uvedenou dílčí přímou historickou oporu.
- Budoucí §7.4.1.1 a kapitola8 nejsou v dodaných hotových svazcích;
  jde o výhledové odkazy, ne nezávisle přečtený obsah.

Čerstvé čtyři vrstvy s celými stránkovými bloky a tematickým hledáním
jsou v `sources/sequential-2026-11-05/other-trees-errata-extract.json`.
C0094 ani C0095 v nich nejsou opraveny. X0298 obsahuje 20 různých
zásahů, ale první dotisk barvíme červeně pouze na349,351,352,353,575,577
pro skutečné obsahové vady. Zbytky slov, formulace „pairs“, závorka
ARRAY, nové bibliografie, oprava jména až v doplněné odpovědi a výhledové
křížové odkazy se nezaměňují za další algoritmické chyby prvního dotisku.
Reformulace E3 nezměnila funkci původních opakování.

Všech19úloh je checked; nově jsou s bibliografickou výjimkou uzavřeny
10,14,15,19. Hlavní text zůstává partial pouze pro vymezenou otázku
C0095. Celé348–358,360–361 a575–577 mají nyní stránkové pokrytí;
359 je partial,362 dosud čeká na navazující úvod §2.3.4. Potvrzení
C0094 znamená závěr z našich pramenů, ne potvrzení od Knutha, ověření
fyzického výtisku ani prvenství. Žádná zpráva nebyla připravena či odeslána.
