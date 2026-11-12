# §2.2.1-13: úplný rozpis postačitelnosti Prattovy báze

Tento důkaz doplňuje otevřený směr v existující poznámce
`workstreams/vol1/notes/deque-basis.md`. Její obecný důkaz nemožnosti
zakázaných vzorů a úspěšný úplný konečný test se neopakují. Níže
dokazujeme pro každé n: není-li permutace vytvořitelná pomocí deque,
obsahuje jeden z vytištěných zakázaných vzorů.

Primární zdroj myšlenky zpětného sledování: V. R. Pratt, *Computing
Permutations with Double-Ended Queues, Parallel Stacks and Parallel
Queues*, STOC 1973, s. 271–274. Text je v již získaném
`workstreams/vol1/sources/pratt-1973-deques.pdf`. Následující rozpis
zpřesňuje výběr prvků, existenci každého dalšího článku řetězu,
časové nerovnosti i převod obou parit na vzory z knihy.

## 1. Definice a dvě elementární vlastnosti

Deque je posloupnost, do níž lze vkládat a z níž lze odebírat na
kterémkoli konci. Vstupní prvky 1,…,n přicházejí v tomto pořadí;
požadované pořadí výstupů je permutace P. Vzor znamená relativní
pořadí vybrané podposloupnosti výstupu, nikoli nutně sousedních členů.

Historii lze **redukovat** odložením každého vkladu, který není nutný
pro další požadovaný výstup. Pokud bezprostředně po vložení prvku u
odebíráme jiný prvek v, lze tyto dvě operace prohodit: vynechání u
nemůže zabránit odběru v. Opakováním dostaneme historii, v níž každá
sousední dvojice vklad–odběr pracuje s týmž prvkem. Takový pár nazveme
průchod; vkládaný prvek je nové maximum dosud přečteného vstupu.
Stejné prohazování platí i pro úspěšný prefix před prvním selháním.
Pořadí samotných vkladů a výstupů redukované historie je dáno P:
před dalším výstupem načteme právě dosud chybějící vstupy až k němu.

Druhá vlastnost je, že současný obsah deque má **tvar údolí**:
zleva nejprve klesá k nejmenšímu prvku a potom roste. Prázdná
posloupnost tuto podmínku splňuje. Nový prvek je větší než všechny
staré a lze jej přidat jen na konec; odběr konce podmínku rovněž
zachová. Žádná trojice v pořadí podél deque proto nemůže mít svůj
největší prvek uprostřed. Každý souvislý úsek má maximum na jednom
z konců.

## 2. Nejlepší neúspěšná historie a pevné jádro

Předpokládejme, že P nelze vytvořit. Mezi konečně mnoha redukovanými
historiemi vyberme takovou, která vypíše nejdelší možný prefix P.
Označme a příští požadovaný, ale zablokovaný prvek. Musí být již
vložen a ležet uvnitř deque: nové maximum lze vždy nechat projít,
a prvek na konci lze vždy odebrat. Ze všech historií se stejnou
délkou prefixu zvolme takovou, v níž je větší z obou bezprostředních
sousedů a co největší. Tohoto souseda označme c_0 a zrcadlově
orientujme deque tak, aby ležel napravo od a.

Tvar údolí dává c_0>a. Levý soused a je menší než c_0. Při vložení
c_0 už musí být a pravým koncem tehdejšího obsahu: starší prvek
mezi a a c_0 by nebylo možné odstranit před prvním odběrem a nebo
c_0, takže by c_0 nebyl nyní bezprostředním sousedem a.

Ze všech prvků přítomných při vložení c_0 vezměme ty, které zůstaly
do zablokování a. Tvoří souvislé **jádro**

```
B = b A a,
```

kde A může být prázdná posloupnost. Platí b≠a: jinak by současný
levý soused a musel být vložen později než c_0, a byl by tedy větší
než c_0. Žádný prvek B se v celém uvažovaném koncovém úseku
historie neodebírá. Položme M=max(a,b); všechny prvky B jsou ≤M.
Při zablokování má deque tvar

```
G' B c_0 G,                                      (1)
```

a všechny prvky G' a G byly vloženy až po c_0, tedy jsou >c_0.

**Lema o prázdných okolích jádra.** V žádném okamžiku po vložení
celého B a před vložením c_0 nesmí být na deque samotné B.

Důkaz: od takového okamžiku zaměňme levý a pravý konec ve všech
dalších operacích. Protože se z B nic neodebírá, všechny původní
operace mimo B zůstávají legální; vnější řetězce jen přejdou na
opačný konec a obrátí své pořadí. Místo (1) dostaneme

```
reverse(G) c_0 B reverse(G').
```

Je-li G' prázdná, a lze nyní odebrat, což prodlouží nejlepší prefix.
Jinak je pravý soused a prvek G', tedy >c_0, což zlepší druhé
kritérium volby historie. Obě možnosti jsou sporem. Stejný argument
platí i těsně před samotným vložením c_0.

## 3. Zpětný střídající se řetěz

Sledujme okamžik vložení c_i, začínaje i=0. Dokud c_i>M, je celé
jádro B už přítomné. Na konci, kam se c_i vložil, musí být B přímo
odkryté: c_i přežívá až do pozdějšího okamžiku, kdy je u B, a každý
starší prvek vložený mezi něj a B by odtud nemohl dříve odejít.
Na opačném konci musí být nějaký prvek mimo B, jinak by tam bylo
samotné B v rozporu s lematem. Zvolme jako c_(i+1) prvek na této
opačné straně bezprostředně u B.

Protože c_(i+1) byl přítomen už při vložení c_i, platí

```
c_(i+1) < c_i.
```

Řetěz tedy po konečně mnoha k≥1 krocích dosáhne prvního c_k<M.
Vklady c_i střídají strany: c_i je napravo pro sudé i a nalevo
pro liché i. Pro i<k je c_i>M, takže při jeho vložení je jádro celé.

Potřebujeme i přesné pořadí odběrů. c_1 se odebere před požadovaným a,
protože byl přítomen při vložení c_0 a nepatří mezi přeživší prvky B.
Obecně pro i≥1 platí

```
vložit c_i < odebrat c_(i+1) < vložit c_(i−1).    (2)
```

První nerovnost plyne z definice c_(i+1). Pro druhou: c_(i+1) je
na stejné straně B jako c_(i−1). Kdyby tam zůstal až do vložení
c_(i−1), ocitl by se mezi B a c_(i−1), a nemohl by být odstraněn
před ním. To odporuje tomu, že c_(i−1) je u B v okamžiku výběru
předchozího článku řetězu (pro c_0 v okamžiku zablokování a).

Redukovanost historie nyní v intervalu mezi vložením c_i a odběrem
c_(i+1) vynutí alespoň jeden průchod d_i. Stačí vzít první odběr
po vkladu c_i a poslední vklad bezprostředně před tímto odběrem.
Redukovanost zaručí průchod; nemůže jít o c_i, který musí přežít
do pozdějšího výběrového okamžiku. Proto d_i>c_i. Z (2) navíc plyne
d_i<c_(i−1) pro i≥1. Vybrané hodnoty tak mají pořadí

```
M < c_(k−1) < d_(k−1) < c_(k−2) < d_(k−2)
  < ... < c_0 < d_0.                             (3)
```

Na spodním konci řetězu máme dvě možnosti. Pro liché k se podél
deque vyskytuje c_k,b,a. Protože c_k<M, nemůže být b největší
z této trojice uprostřed; tedy b<a a M=a. Pro sudé k se vyskytuje
b,a,c_k, takže a<b a M=b. V obou případech jsou dva nejmenší
vybrané prvky c_k a min(a,b), v libovolném vzájemném pořadí;
třetí nejmenší je M.

## 4. Přesný vytištěný vzor

Ze zachovaných časových nerovností čteme v cílovém výstupu P
podposloupnost

```
d_(k−1), c_k, d_(k−2), c_(k−1), ..., d_0, c_1,
a, {c_0,b v jejich pořadí v P}.                   (4)
```

Poslední dva prvky dosud nebyly odebrány, proto se v P vyskytují až
po a; jejich vzájemné pořadí není předepsáno. (3) převádí první část
(4) na hodnoty 5,2,7,4,…,2k+3,2k, až na výměnu dvou nejmenších
hodnot 1 a 2.

Je-li k=2s−1 liché, pak a má relativní hodnotu 3, b jednu z hodnot
1,2 a c_0 hodnotu 4s. Dostáváme

```
5,2,7,4,...,4s+1,4s−2,3,4s,1.
```

Je-li k=2s sudé, pak b má relativní hodnotu 3, a jednu z hodnot
1,2 a c_0 hodnotu 4s+2. Dostáváme

```
5,2,7,4,...,4s+3,4s,1,4s+2,3.
```

V obou případech může být navíc zaměněno 1 s 2, poslední dva členy,
nebo obojí. To jsou přesně čtyři varianty každé z obou rodin na s. 539,
se s≥1. Každá nevytvořitelná permutace tedy obsahuje vytištěný vzor.
Spolu s již doloženým obecným opačným směrem je charakterizační věta
matematicky uzavřena. Důkaz nepotřebuje ani konečné testy, ani správnost
Rosenstiehlova–Tarjanova pozdějšího rozhodovacího programu.
