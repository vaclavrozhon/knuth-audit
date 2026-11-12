# §2.3.3: Algorithm A a úlohy 12–15

Přečteny originály pp. 355–359, 361–362 a 576–577 i čtyři vrstvy errat.
Důkaz níže je vlastní; neodvozuje se z testů ani z neúplně získaného
článku Warda a Zedana, na který odkazují doplněné odpovědi 14–15.

## 1. Definice a smlouva

Koeficienty mají přesné sčítání, násobení a test nuly; v implementaci jde
o celá a racionální čísla. Proměnné mají pevné úplné pořadí, exponenty
jsou nezáporné celé a polynomy konečné. Přetečení a zaokrouhlování
nejsou součástí tohoto abstraktního algoritmu. Nulová adresa znamená
chybějící odkaz, nikoli uzel.

**Definice 1.** Uzel p s DOWN=0 je skalár hodnoty CV. Jinak CV obsahuje
proměnnou v a DOWN ukazuje na koeficient exponentu 0 v kruhovém
obousměrném seznamu. Další exponenty přísně rostou. Hodnota p je součet
value(c)*v^EXP(c) přes jeho koeficienty c. LEFT a RIGHT jsou vzájemně
inverzní, UP každého koeficientu je p a všechny jeho proměnné jsou menší
než v. Podstromy jsou disjunktní. Kořen má UP=0, EXP=0 a boční samoodkazy.

**Definice 2.** Kanonický strom má každý řádek alespoň dvoučlenný, každý
koeficient kanonický a všechny koeficienty kladných exponentů nenulové.
Nulový exponent je povinný a jeho koeficient smí být nula. Nula samotná
je skalární list. Rozklad podle největší přítomné proměnné je jednoznačný.

**Smlouva.** P0,Q0 jsou disjunktní kanonické stromy, volné uzly jsou
oddělené a je jich dost. A má zachovat celý první strom a oba kořenové
uzly, nahradit hodnotu Q0 součtem původních hodnot, normalizovat výsledek
a vrátit pracovní P,Q na P0,Q0. Přechodně dovolujeme slabý tvar: jednočlenný
řádek exponentu 0 a nulový kladný koeficient čekající na odstranění.
Kanonicita po každé jednotlivé instrukci není správný invariant.

## 2. Abstraktní ADD

Definujme nejprve rekurzivní sčítání s prvním argumentem jen ke čtení:

1. Skalár prvního argumentu přičti ke skaláru na nulové větvi druhého.
2. Je-li první argument v proměnné x a druhý ve větší y, přičti první
   argument rekurzivně pouze k nulovému koeficientu y.
3. Je-li druhý argument skalár nebo v menší proměnné, obal jej řádkem
   v x s jediným nulovým exponentem a jeho původní hodnotou jako koeficientem.
4. Při společné proměnné přičítej odpovídající koeficienty: nejprve
   exponent 0, potom kladné exponenty prvního argumentu sestupně.
   Chybějící koeficient druhého začíná nulou. Nulové kladné výsledky
   odstraň a dokončený řádek s pouhým nulovým exponentem zruš povýšením
   jeho koeficientu.

Rekurze končí podle největší proměnné obou aktuálních argumentů, v konečné
uspořádané množině vstupních proměnných. Při bodu 2 největší proměnná y
zmizí; při společné proměnné x oba koeficienty obsahují jen menší proměnné.
Obalení z bodu 3 počítáme společně s následujícím sestupem z bodu 4:
vlastní koeficient prvního i původní druhý argument mají proměnné menší
než x. Skaláry tvoří základ. Seznam koeficientů a nulové větve jsou konečné.

Indukce podle tohoto měřítka dokazuje správnost. Skalární případ je
sčítání čísel. Přičtení polynomu bez y změní jen nulový koeficient y;
obalení hodnotu zachová. Při společné proměnné indukční předpoklad
sečte přesně koeficienty stejné mocniny. Odstranění nulových členů
a povýšení osamoceného nulového koeficientu zachovává hodnotu a dává
Definici 2. Žádný krok nepíše do prvního argumentu.

## 3. Simulace rekurze tištěným A

Rámcem rozumíme aktivní sčítání dvou koeficientů společné proměnné
s informací, které exponenty již byly zpracovány. Rámce nenese explicitní
zásobník, nýbrž řetězce UP a poloha P v neměnném prvním stromu.

**Invariant I.** Aktivní rámce v P a Q mají stejné proměnné a exponenty;
Q navíc smí mít mezilehlé proměnné exponentu 0. Dokončené větve Q jsou
součty, nedotčené větve mají původní hodnotu a aktivní větve mají slabý
tvar. Mimo přechod A9–A10 mají P,Q shodný součin nenulových mocnin
na cestě ke kořeni. Samotná rovnost tohoto součinu by nestačila:
invariant zahrnuje i korespondenci nulových rámců.

A1 provádí body 1–2 ADD sestupy po nulových koeficientech. Při stejné
proměnné sestoupí oba ukazatele a otevře společný rámec. Potřebné obalení
předá A2. Na vstupu A3 jsou oba uzly skaláry se stejným kontextem.

A2 přemístí staré CV,DOWN uzlu Q do nového R exponentu 0. Každému
původnímu dítěti opraví UP=R, vytvoří samoodkazy R a ponechá Q na místě
jako novou proměnnou s jediným dítětem. To zachová hodnotu, vnější vazby
i všechny podstromy. Návrat do A1 umožní společný sestup.

A3 provede skalární součet. Kladný nenulový koeficient je dokončen
a pokračuje A4; nulový kladný koeficient pokračuje A8. Exponent 0 se
nesmí odstranit a vede do A7, který přes dodatečné nulové proměnné
obnoví odpovídající rámec.

A4 posune P doleva. Z exponentu 0 tím přejde na největší exponent,
pak pokračuje sestupně až na návrat k 0, který označí dokončený řádek.
Q postupuje doleva až po exponent nejvýše EXP(P); povinná nula zaručuje
zarážku. Rovnost vede do A1, jinak A5 vloží nulový koeficient za nalezeného
předchůdce. Čtyři boční vazby a UP v A5 zachovávají kružnici a pořadí.

A6 opustí dokončený řádek P. A7 odstraní z aktuální cesty Q pouze další
nulové proměnné až ke společnému rodičovskému rámci. Ten existuje
podle I. Je-li P již v kořeni, místo hledání neexistujícího rámce jde
do A11. Jinak pokračuje A4.

A8 je bezpečné díky vztahům dokázaným v §4: oba exponenty jsou stejné
a kladné a obě rodičovské proměnné jsou stejné. Q je nulový skalární
list. Propojení jeho sousedů a uvolnění listu zachová ostatní podstromy.
Nové Q je pravý soused odstraněného uzlu, takže další LEFT(Q) začne
správným dosud nezpracovaným úsekem. Jediný zbylý nulový exponent lze
povýšit až po vyčerpání kladných exponentů P. Právě to testují
EXP(LEFT(P))=0 a Q=S. Jinak se přechodně jednočlenný řádek musí zachovat
pro další členy P.

A9 povýší obsah zbylého nulového koeficientu R do rodiče Q. Přenese
CV,DOWN, opraví UP všech převzatých dětí a uvolní pouze R. Vnější
EXP,UP,LEFT,RIGHT uzlu Q se nemění. To je normalizace z bodu 4 ADD.

A10 při nulovém povýšeném koeficientu kladného vnějšího exponentu
posune P=UP(P): odstraní tím právě protějšek rámce odstraněného v Q.
Oba ukazatele opět označují odpovídající koeficienty a A8 propaguje
vyrušení výše. Jinak A6 uskuteční normální návrat. Tím se I obnoví
po výjimce A9. A11 už jen vystoupá k zachovanému kořeni Q0.

Počáteční stav splňuje I s prázdným seznamem rámců. Rozbor pokryl
všechny přechody a ukazuje přesnou simulaci ADD z §2. I interní smyčky
končí: A1 striktně sestupuje, A4 má nulovou zarážku, A2/A9 projdou
jednou konečnou kružnici a A7/A11 striktně stoupají. A2 bezprostředně
umožní nový sestup P; A5 zahájí další dosud nezpracovaný koeficient P;
A10 odstraní dokončený rámec. Mezi dvěma kroky konečné rekurze ADD
tedy nevznikne nekonečná posloupnost interních kroků. Dokázali jsme
ukončení, zachování všech potřebných vazeb i celou smlouvu algoritmu.

## 4. Úlohy 12 a 13

**12(a).** Q0 nelze uvolnit: A8 odstraňuje jen kladný exponent, kdežto
Q0 má exponent 0. A9 uvolňuje dítě a zachovává rodiče. Právě opravy
všech UP v A2/A9 umožní zachovat pevnou kořenovou adresu. **12(b).**
A7 jde do A11 jen pro UP(P)=0, tedy P=P0; A11 vrátí Q do Q0.
Obě tištěné odpovědi ano jsou správné.

**13.** Do A8 vedou jen A3 a A10. V A3 je společný rámec dokončeným
skalárním součtem. Aktuální hrana Q nemůže být dodatečnou nulovou hranou
z I, protože test do A8 požaduje EXP(Q) nenulové. Má tedy protějšek
v P se stejnou rodičovskou proměnnou i exponentem. V A10 byl v A9
odstraněn dokončený společný rámec Q a posun P=UP(P) odstraní jeho
protějšek v P; opět se testuje nenulový exponent. V obou případech
jsou UP(P),UP(Q) nenulové a platí
EXP(P)=EXP(Q), CV(UP(P))=CV(UP(Q)).
Důkaz se vztahuje i na kaskádu několika úplných vyrušení.

## 5. Úloha 15: vlastní násobení

Funkce multiply v tree_polynomials.py používá šestipolové uzly, vstupy
pouze čte a vrací nový disjunktní strom. Pomocný slovník obsahuje jen
exponenty a adresy koeficientů, nikoli převedené monomy polynomů.

Pro skaláry vytvoří list jejich součinu. Jinak zvolí největší proměnnou
v obou kořenech; argument bez této proměnné chápe jako jediný koeficient
exponentu 0. Pro každou dvojici koeficientů exponentů e,f rekurzivně
vytvoří součin a přičte jej algoritmem A do výsledného koeficientu e+f.
Pomocný součin pak uvolní. Nakonec odstraní nulové kladné koeficienty
a znormalizuje řádek podle Definice 2.

Ve skutečných rekurzivních voláních jsou všechny proměnné menší než
právě zvolená; hloubka tedy klesá v konečné množině vstupních proměnných.
Seznam dvojic je konečný. Indukce, distributivita a dokázaná smlouva A
dávají správný koeficient každé mocniny součinu. Vstupy se nemění,
každý dočasný strom se stane výsledným koeficientem nebo celý uvolní.
Rekurze a pomocná tabulka jsou výslovnou vlastností tohoto řešení:
úloha nepožaduje MIX ani provedení bez zásobníku.

## 6. Konečné ověření

check_tree_polynomials.py má nezávislý plochý slovník monomů jako
aritmetický oracle a samostatný konstruktor stromů. Prošlo 6 962 sčítání,
včetně všech 81² dvojic nad 1,x,y,xy s koeficienty −1,0,1, a 809 násobení.
Knižní příklad končí 3+xy a sám navštíví A1–A11. Náhodné dávky zahrnují
až osm proměnných, racionální koeficienty a úplná i částečná vyrušení.

Kontroly sledují přesnou hodnotu, všechny boční a rodičovské vazby,
kanonicitu, zachování vstupu a kořenů, disjunktnost a úplné rozdělení
přidělených uzlů na živé a volné. Při A8 se kontrolují oba vztahy
z úlohy 13 i celý nenulový kontext. Výsledky jsou v
results/tree-polynomials.json; konečné kontroly nenahrazují důkaz výše.


