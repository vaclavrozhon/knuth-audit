# §7.1.1–1 až 4: řešení, dualita a skutečně nejkratší NAND formule

6. listopadu 2026, X0059. Zadání p79–80/file96–97; odpovědi p534/file551.
Originály images/file096.png, file097.png a proof-pages549-551-3.png;
pro čtení prvních odpovědí také rendery proof-answer1-detail.png a
proof-answer1-3-detail.png. Čísla úloh jsou vždy ze sekce 7.1.1.
Nenahrazuji nejkratší formule pouhou existenční konstrukcí P0514.
V tomto bloku nebyl spuštěn matematický program ani enumerace formulí.

## P0540: úloha 1 a všech šest odkazů „it“

Předpokládej x⇒y, tedy přípustné dvojice jsou 00,01,11.
Vezmi šest odkazů po řadě jako y,x,x,y,y,x, přesně jako v odpovědi.
Je-li y pravda, x může být pravda (11 je přípustné), ale nemusí (01).
Je-li x pravda, y musí být pravda (jediná přípustná dvojice je 11).
Není-li y pravda, není ani x (zbývá 00). To vysvětluje zvlášť
„might“, „would“ a poslední kontrapozici v citátu na p48.
Je to jeden konzistentní výklad proměnlivých zájmen, nikoli tvrzení,
že běžná anglická věta má jedinou formalizaci. Historická atribuce
Carroll/Sartena zůstává bibliografickou výjimkou.

## P0541–P0542: úloha 2 a dodatek o všech identitách

Pincus převádí pozemský bit x na ¬x a výsledek převádí zpět.
Pozemská funkce odpovídající operaci f je tudíž
D(f)(x,y)=¬f(¬x,¬y). Argumenty 00,01,10,11 se změní na 11,10,01,00;
pravdivostní vektor se obrátí a všechny jeho bity se doplní.

**P0541:** úplný převod všech šestnácti řádků je následující:

| původní | pozemská interpretace pincuského názvu |
|---|---|
| 0000 | 1111 |
| 0001 | 0111 |
| 0010 | 1011 |
| 0011 | 0011 |
| 0100 | 1101 |
| 0101 | 0101 |
| 0110 | 1001 |
| 0111 | 0001 |
| 1000 | 1110 |
| 1001 | 0110 |
| 1010 | 1010 |
| 1011 | 0010 |
| 1100 | 1100 |
| 1101 | 0100 |
| 1110 | 1000 |
| 1111 | 0000 |

Mapování symbolů v odpovědi je přesně toto mapování řádků Table 1.
Zvláště pincuské „or“ odpovídá pozemskému AND, jak ukazuje zadání.

**P0542:** pro libovolný term t změň každou jeho operaci na D té
operace, konstantu c na ¬c, proměnné ponech. Strukturální indukce
dává t*(x₁,…,xₙ)=¬t(¬x₁,…,¬xₙ). Na proměnné je to dvojí negace,
na konstantě definice; vnitřní uzel zruší dvě negace u každého dítěte.
Proto každá identita t=s přejde v identitu t*=s*. Negace sama je
svým duálem, AND a OR se vymění, stejně XOR a ekvivalence, 0 a 1.
De Morgan (11)/(12) i identity (3)/(4) se tedy skutečně vymění.
D(D(f))=f, takže se neztrácí žádná algebraická schopnost.
Výrok o stejné algebraické užitečnosti duálů není srovnáním rychlosti
konkrétních strojových instrukcí.

## P0543–P0548: všechny části a oba dodatky úlohy 3

Základní kódování je s=2b−1: −1 je false, +1 true.

- **P0543, (a):** zobrazení je rostoucí, proto max(s,t) převádí
  max(b,c), tedy OR.
- **P0544, (b):** totéž s minimem dává AND.
- **P0545, (c):** −s=2(1−b)−1 dává komplement.
- **P0546, (d):** st=+1 právě při stejných znaménkách a −1 při
  různých; výsledek kóduje ekvivalenci.
- **P0547, dodatek:** při obráceném kódu s=1−2b je −1 true.
  Součin je −1 právě při jednom pravdivém vstupu, tedy kóduje XOR.
  Netvrdí se, že jde obecně o lepší praktickou volbu kódování.
- **P0548, dodatek:** součet tří znamének je jeden z −3,−1,1,3,
  nikdy 0. Jeho znaménko je právě znaménko vyskytující se alespoň
  dvakrát. Proto sign(s+t+u) reprezentuje ternární většinu/medián
  při kterémkoli z obou kódování; případ nerozhodného sign(0) nevzniká.

## P0549 a P0551: všechny vytištěné NAND formule jsou platné

Piš N(a,b)=¬(a∧b). **Náklad je počet výskytů N ve stromu formule.**
Použité zkratky se při každém výskytu znovu rozvinou; nesdílejí se
jako uzly obvodu. Například N(Q,Q) má cenu 3, nikoli 2.

Pro část (a), bez konstant, polož
A=N(x,x)=¬x, B=N(y,y)=¬y, Q=N(x,y)=¬(xy),
I=N(x,Q)=¬x∨y, J=N(y,A)=x∨¬y,
V=N(B,A)=x∨y, T=N(x,A)=1.
Ceny A,B,Q jsou 1; I,J,T mají 2; V má 3.

Pro část (b), s konstantami, polož
A'=N(x,1)=¬x, B'=N(y,1)=¬y,
I'=N(B',x)=¬x∨y, J'=N(y,A')=x∨¬y,
V'=N(B',A')=x∨y a ponech Q=N(x,y).
Odpovědi po nahrazení zkratkami jsou přesně:

| tabulka | (a) původní formule | cena | (b) původní formule | cena | proměnné v (b) |
|---|---|---:|---|---:|---:|
| 0000 | N(T,T) | 5 | 0 | 0 | 0 |
| 0001 | N(Q,Q) | 3 | N(Q,1) | 2 | 2 |
| 0010 | N(I,I) | 5 | N(I',1) | 3 | 2 |
| 0011 | x | 0 | x | 0 | 1 |
| 0100 | N(J,J) | 5 | N(J',1) | 3 | 2 |
| 0101 | y | 0 | y | 0 | 1 |
| 0110 | N(J,I) | 5 | N(J',I') | 5 | 4 |
| 0111 | V | 3 | V' | 3 | 2 |
| 1000 | N(T,V) | 6 | N(1,V') | 4 | 2 |
| 1001 | N(Q,V) | 5 | N(Q,V') | 5 | 4 |
| 1010 | B | 1 | B' | 1 | 1 |
| 1011 | J | 2 | J' | 2 | 2 |
| 1100 | A | 1 | A' | 1 | 1 |
| 1101 | I | 2 | I' | 2 | 2 |
| 1110 | Q | 1 | Q | 1 | 2 |
| 1111 | T | 2 | 1 | 0 | 0 |

Již vypočtené významy zkratek ověřují většinu řádků okamžitě.
Pro XOR platí I∧J=(¬x∨y)∧(x∨¬y), což je právě ekvivalence;
negace dává XOR. Pro ekvivalenci je Q∧V=¬(xy)∧(x∨y), tedy XOR.
Zbývající dvojité NAND jsou negace I,J,Q,T nebo V.
Tím jsou ověřeny všechny konkrétní vytištěné formule a jejich ceny,
nejen jiní svědci existence.

## P0550 a P0552: obecné dolní meze, bez enumerace formulí

Nejprve několik vyčerpávajících strukturálních faktů.
S povolenými konstantami mohou cenu 0 mít jen 0,1,x,y.
Jediné funkce jednoho N nad takovými listy jsou
0,1,¬x,¬y,NAND. Při ceně 2 má kořen jeden list a jednoho
jednokrokového potomka. Z dosazení 0/1, záměny x/y a komutativity N
vznikají navíc pouze AND a obě implikace; například
N(1,Q)=AND, N(x,¬y)=¬x∨y, N(y,¬x)=x∨¬y.
Zbylé možnosti jsou konstanty, projekce nebo již uvedené negace/NAND.
OR proto potřebuje alespoň 3 kroky i s konstantami.
Negace a NAND potřebují ≥1, obě implikace ≥2.
Bez konstant potřebuje 1 alespoň 2 kroky, protože mezi třemi
možnostmi N(x,x),N(x,y),N(y,y) konstanta není.

V kořeni N(a,b)=f musí být množina jedniček průniku a∧b přesně
množinou nul f. Každý z a,b je proto jedničkovou nadmnožinou ¬f.

- Pro f=0 musí být a=b=1. Bez konstant cena ≥2+2+1=5.
- Pro f=AND je ¬f=1110; jeho jedničkovými nadmnožinami jsou
  pouze NAND a 1. Alespoň jeden potomek musí být NAND.
  Bez konstant je cena ≥1+1+1=3; s konstantami ≥1+0+1=2.
- Pro f=0010 je ¬f=1101; nadmnožiny jsou příslušná implikace
  a 1. Alespoň jeden potomek je implikace. Bez konstant je cena
  ≥2+2+1=5, s konstantami ≥2+0+1=3. Záměna vstupů dává
  stejnou mez pro 0100.
- Pro f=NOR je ¬f=OR=0111; potomci jsou pouze OR a 1, přičemž
  alespoň jeden je OR. Bez konstant je cena ≥3+2+1=6,
  s konstantami ≥3+0+1=4.

Zbývají XOR a ekvivalence. Vezmi nejkratší formuli mezi oběma
funkcemi a její cenu m. Její bezprostřední potomek nemůže počítat
ani jednu z nich: měl by cenu ≥m, zatímco celý strom stojí více.

Je-li kořenová funkce XOR, potomci musí obsahovat jedničky 1001.
Možnosti jsou ekvivalence, obě implikace a 1. Po vyloučení
ekvivalence musí být potomci právě dvě různé implikace; jinak
jejich průnik nebude 1001. Cena je alespoň 2+2+1=5.
Je-li kořenová funkce ekvivalence, potomci obsahují 0110.
Možnosti jsou XOR, OR, NAND a 1. Po vyloučení XOR musí být
potomci OR a NAND, takže cena ≥3+1+1=5.
Proto m≥5, a tedy **obě** funkce vyžadují ≥5. Argument platí
s konstantami i bez nich a není kruhový.

Projekce a povolené konstanty mají triviální dolní mez 0.
Tím jsou doloženy všechny dolní meze obou šestnáctiřádkových tabulek;
horní svědci P0549/P0551 jim odpovídají ve všech případech.

## P0553: sekundární minimum výskytů proměnných v (b)

Konstanta nepotřebuje proměnnou; nekonstantní unární funkce potřebuje
alespoň jednu a funkce závislá na obou vstupech alespoň po jednom.
Tyto meze dosahují všechny řádky kromě XOR a ekvivalence, které
mají ve vytištěných formulích po dvou výskytech x i y.

Proč čtyři výskyty nelze zlepšit: objeví-li se proměnná ve stromu
NAND právě jednou, podél její jediné cesty ke kořeni se při každém
NAND mění polarita. S ostatními vstupy fixovanými je tedy celá
funkce v této proměnné monotónní vždy ve stejném směru daném
paritou délky cesty, případně konstantní. XOR i ekvivalence ale
mění směr závislosti na x podle y a na y podle x. Každá proměnná
proto musí být přítomna nejméně dvakrát. Minimum čtyř je dosaženo.
Bez konstant má strom s k binárními uzly vždy k+1 listů, takže
tam sekundární volba nemění počet výskytů.

## P0554: korektnost postupu v odpovědi 4

Generovat formule po jejich ceně a pro každou pravdivostní tabulku
uchovat nejlevnější svědectví je korektní: libovolný strom v kořeni
rozpadne na dva menší. Nahradit podstrom levnějším se stejnou
funkcí zachová výsledek, takže optimální strom lze složit z
optimálních podstromů. Při shodné ceně totéž platí pro počet
výskytů proměnných, protože obě ceny se sčítají a kořen přidá
právě jeden N. Indukce po počtu uzlů dává úplnost všech cenových
úrovní; vytištěné horní svědky zaručují dosažení všech 16 tabulek
nejpozději při ceně 6 v (a) a 5 v (b).
Je to důkaz popsaného algoritmu a konečnosti zdejšího úkolu.
Algoritmus nebyl spuštěn a kniha zde neslibuje asymptotické optimum
doby takové syntaktické enumerace.

## Meze a další práce

Všechna zadání 1–4, podčásti i matematické dodatky odpovědí jsou
pokryty P0540–P0554. Primární sazba přečtena, známá errata pro
p48/49 zohledněna už v proof-028. Žádný nový rozpor ani kandidát.
Historické priority, Carroll/Sartena a Shefferův bibliografický
údaj se nepovyšují na nezávisle ověřené.
Další jednotlivá úloha 5: jiná základní operace, opět požadovaná
minima. Hlavní text zůstává na p54/file71 a parity P0526 partial.
