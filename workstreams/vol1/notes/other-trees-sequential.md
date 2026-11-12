# §2.3.3: sekvenční reprezentace a úlohy 1–6, 16–19

Originály hlavního textu pp. 348–353, úloh pp. 359–362 a odpovědí
pp. 575–577 byly přečteny v OCR i obrazech. Známé opravy rozlišuje
notes/other-trees-sources.md; numerické výsledky jsou v
results/other-trees.json. Polynomy a ekvivalence mají samostatné důkazy.

## Definice a hlavní reprezentace

Strom je zde konečný zakořeněný strom s uspořádanými dětmi; les je
uspořádaná posloupnost stromů. Preorder navštíví kořen před jeho dětmi,
postorder po nich; děti vždy zleva doprava. Stupeň uzlu je počet dětí.
RLINK označuje následujícího sourozence a LLINK první dítě; nula je
chybějící odkaz. RTAG, respektive LTAG, označuje, že příslušný odkaz
chybí. Kořeny lesa tvoří také jednu rodinu. Stride c je počet paměťových
míst mezi dvěma po sobě uloženými uzly; pořadové číslo uzlu není
obecně jeho paměťová adresa.

Indukce podle stromu ukazuje, že jeho uzly tvoří v preorder souvislý
blok. RLINK míří těsně za blok svého zdrojového podstromu; zevnitř
tohoto bloku nemůže vést odkaz za jeho hranici. Oblouky RLINK se proto
nekříží. Uzel je list právě tehdy, když je poslední v lese nebo po něm
bezprostředně následuje cíl nějakého RLINK: první uzel dalšího podstromu
předchází poslední list dokončeného bloku. Obráceně za nelistem následuje
jeho první dítě, které nemůže být cílem sourozeneckého odkazu.

Samotné oba tagy postačují: procházej pořadí, při nenulovém pravém
odkazu vlož jeho zdroj na zásobník nevyplněných RLINK; po listu vyplň
poslední takový zdroj adresou následujícího uzlu. Rodiny jsou vnořené,
proto se dokončují v opačném pořadí než začaly. Na konci posledního
stromu už zásobník nemá nevyřízený zdroj. Získávání chybějící informace
takto vyžaduje průchod; tvrzení knihy není příslib konstantního náhodného
přístupu z pouhých tagů.

SCOPE uzlu je adresa těsně za jeho podstromem. List má SCOPE=P+c.
Při reprezentaci s vloženými zvláštními uzly označenými * potřebujeme
nejvýše jeden za každý nenulový RLINK, tedy méně než n dalších uzlů
pro neprázdný les s n obyčejnými uzly. Text p. 350 mluví o počtu
ne-* uzlů, nikoli o počtu nelistů; OCR této fráze není nový nález.

Rodinné pořadí navštíví celou rodinu zleva a další nevyřízenou rodinu
vybírá zásobníkem. Je to obrácený binární postorder při převodu
první dítě / následující sourozenec. Jeho rekurze je kořen, ostatní
kořeny, děti; odpovídá obrácení pořadí pravý podstrom / levý podstrom
v binárním postorder. Pořadí po úrovních používá místo zásobníku frontu.

Opravený příklad je les (A(B,C(K)), D(E(H),F(J),G)).
Preorder je A B C K D E H F J G; postorder B K C A H E J F G D;
stupně v postorder jsou 0,0,1,2,0,1,0,1,0,3. Rodinné pořadí je
A D E F G J H B C K, pořadí po úrovních A D B C E F G K H J.
Všechny tyto údaje vycházejí z jednoho společného opraveného lesa.

## Úlohy 1–6

**1.** V pořadí po úrovních RTAG vyznačí konce rodin. U každého nelistu
vlož jeho adresu do fronty budoucích rodičů. Na konci právě čtené rodiny
bude následující rodina patřit nejstaršímu rodiči ve frontě: nastav jeho
LLINK na následující uzel a vyjmi ho. Jeho děti se při dalším čtení
případně samy přidají do fronty. To je přesně pořadí rodin po úrovních,
takže indukcí po rodinách rekonstruujeme všechny LLINK. Prázdná fronta
na konci znamená, že žádné další děti nechybějí.

**2 a 16.** Lokální funkce f uzlu závisí pouze na něm a na hodnotách jeho
dětí. Pro obecný důkaz F použijeme silnější invariant: průchod libovolným
podstromem T změní jakýkoli dosavadní zásobník S na S následovaný jedinou
hodnotou f(root(T)), aniž zasáhne S. List jen vloží svou hodnotu. U uzlu
s d dětmi indukční předpoklad vloží jejich hodnoty zleva; z vršku dolů
jsou tedy f(x_d),...,f(x_1). F2 spočítá rodiče, F3 odstraní právě d
hodnot a vloží novou. To dokazuje invariant i tvrzení pro celý les.

Při obráceném preorder se nejprve zpracují podstromy dětí zprava.
Na vršku jsou pak f(x_1),...,f(x_d); změněné F2 bere toto pořadí.
Nakonec jsou z vršku dolů hodnoty kořenů lesa zleva. Posun adres je
P−c, respektive P+c pro původní F; známá oprava odstraňuje předpoklad c=1.

**3.** Diferenciátor z §2.3.2 může nechat vstupní strom beze změn:
zásobník S obsahuje kořeny hotových derivací dosud nespotřebovaných
rodičem. Odkaz zásobníku je ve vnějším RLINK každého takového kořene,
který není součástí jeho vlastního podstromu. U unárního uzlu odeber
jednu derivaci, u binárního nejprve pravou Q, potom levou Q1. Původní
operandy jsou P1=LLINK(P), P2=RLINK(P1); DIFF může podle potřeby
kopírovat jejich neporušené podstromy. Výsledný kořen vlož na S a
přejdi na původního postorder následníka P. Finální kořen připoj k DY
a obnov jeho vnější vlákno na DY. Invariant F dokazuje správnost
i pro operátory libovolné konečné arity d, kde odebereme d výsledků.
Nejde o požadavek nového MIX programu; je to úplná změna algoritmu D.

**4.** Pro n uzlů a m listů má obvyklý tvar 2n odkazových polí.
Varianta se společným prostorem LLINK/INFO a dodatečným informačním
listem každého vnitřního uzlu má n−m LLINK a 2n−m RLINK, celkem
3n−2m, tedy o n−2m více. INFO polí je stále n. Knižní porovnání závisí
i na šířkách INFO a odkazu; známé opravy 6→5 a 60→50 jsou zahrnuty.

**5.** U posledního dítěte by pravé vlákno ukazovalo právě na rodiče,
kterého už máme v PARENT. Levá vlákna mohou urychlit pohyb doleva
a obrácené či rodinné průchody: bez nich může hledání předcházejícího
sourozence vyžadovat průchod celou rodinou. Zisk je tedy podstatný
hlavně u vysokých stupňů, jak uvádí odpověď.

**6.** PARENT určuje zakořeněnou strukturu, nikoli pořadí sourozenců.
Požaduje se libovolné kompatibilní uspořádání. Zachovej Q=RLINK(P)
z původního seznamu dřív, než RLINK(P) přepíšeš. U kořene přidej P
na začátek seznamu kořenů FIRST; jinak na začátek LCHILD jeho rodiče.
Pokračuj uloženým Q. Po k iteracích jsou právě první k původních uzlů
jednou v příslušné rodině. Předpoklad platného rodičovského lesa
vylučuje cyklus; každý uzel původního seznamu se zpracuje právě jednou.
Výsledek má všechny rodičovské vazby a čas O(n), bez požadavku, aby
původní seznam respektoval předky.

## Úlohy 17–19

**17.** Pro horní lokální funkci závisí f(x) na x a hodnotě u jeho
rodiče; kořenová hodnota je dána zvlášť. Při obráceném postorder
navštívíme rodiče před potomky a jeho dětské podstromy zprava.
Zásobník obsahuje hodnoty rodičů pro dosud nezačaté dětské podstromy
v pořadí jejich budoucích návštěv. Po vyhodnocení uzlu vložíme d kopií
jeho hodnoty, kde d je jeho stupeň. Další uzel odebere právě hodnotu
svého rodiče. Indukce po průchodu dokazuje G1–G4; poslední uzel je
list a zásobník je prázdný. Celkem se vloží n−1 hodnot, tedy mimo
výpočet f je čas O(n). Prostor může být n−1, například pro hvězdu;
není obecně omezen jen výškou stromu. Posun v G3 je P−c.

**18.** P1–P5 převádí preorder s RLINK na postorder se stupni. Zásobník
I uchovává otevřené uzly, D jejich dosud započtené děti a R hranice
ještě neuzavřených podstromů, tj. adresy pravých sourozenců. Počáteční
hranice n+1 uzavírá celý les a počáteční D=0 počítá kořeny.

Před P2 je j poslední otevřený preorder uzel; nejbližší hranice top(R)
určuje první pozici, která už není v jeho levém lese. Nerovnost
top(R)>j+1 právě znamená, že zbývá první dítě, které otevře P5.
P5 přidá jeden do počtu dětí dosavadního rodiče, otevře nový uzel
s nulovým počtem dětí a případně uloží jeho pravou hranici.

Když žádné dítě nezbývá, P3 uzavře vrchní uzel, vydá jeho INFO1
a úplný počet dětí. Má-li skutečného pravého sourozence, P4 odstraní
právě jeho hranici a P5 zahájí sourozence; jinak P3 uzavírá rodiče.
Tím se každý uzel vydá právě po všech svých dětech. Každý se otevře
a uzavře jednou, každá hranice se jednou vloží a odstraní: čas i nejhorší
prostor jsou O(n). Sentinel funguje i pro n=0. Známé INFO→INFO1
v odpovědi 18 je opraveno, nikoli počítáno jako nový nález.

**19(a).** Očíslujme preorder uzly 1,...,n a nechť d_k je počet vlastních
potomků uzlu k. Jeho podstrom má interval [k,k+d_k]. Proto k+d_k≤n
a pro každé j v tomto intervalu je j+d_j≤k+d_k. Včetně j=k jde
o totožnou nerovnost; OCR často ztrácí neostré znaky.

**19(b).** Naopak předpokládejme tyto dvě podmínky a nezáporná celá d_k.
První strom musí mít blok [1,1+d_1]. Jeho děti postupně vytvoříme
z prvního dosud nepoužitého j blokem [j,j+d_j]; druhá podmínka jej
udrží uvnitř rodiče. Stejnou konstrukci použijeme rekurzivně uvnitř
bloku a po jeho konci pokračujeme následujícím kořenem lesa. Každý
rekurzivní blok má méně uzlů, bloky se nepřekrývají a všechny pozice
se spotřebují. Získáme jednoznačný les se zadanými čísly.

**19(c).** Pro dvě platné posloupnosti d,e položme t_k=min(d_k,e_k).
Je-li k≤j≤k+t_k, leží j v obou podstromech. Pak
j+t_j≤j+d_j≤k+d_k a současně j+t_j≤j+e_j≤k+e_k,
tedy j+t_j≤k+t_k. Platí i koncová mez n, takže (b) dává hledaný les.

**Poznámky odpovědi.** Nechť p_i je preorder číslo i-tého uzlu
v postorder. Větší číslo j předchází k v této permutaci právě tehdy,
když je j vlastním potomkem k: v různých větvích se obě pořadí shodují,
u předka a potomka se obrátí. Proto d_k počítá právě uvedené inverze.

Pro počty potomků c_k v postorder je analogický interval [k−c_k,k].
Podmínky jsou 0≤c_k<k a j−c_j≥k−c_k pro k−c_k≤j≤k.
Obrácená bloková konstrukce dokazuje jejich postačitelnost.
Převod první dítě / následující sourozenec má binární inorder roven
postorder lesa a levý podstrom právě všechny potomky daného uzlu.
Proto c_k je velikost příslušného levého podstromu. Duální převod
předchozí sourozenec / poslední dítě má inorder roven preorder lesa
a pravý podstrom právě potomky; proto d_k je pravá velikost.

Souřadnicové uspořádání d≤e je konečný svaz: souřadnicové minimum
je největší dolní mez podle (c). Existuje největší posloupnost
(n−1,n−2,...,0), odpovídající řetězci, takže množina společných horních
mezí je neprázdná. Jejich opakované minimum je nejmenší horní mez.
Ta obecně není souřadnicové maximum: pro (1,0,0) a (0,1,0) maximum
(1,1,0) nevyhoví podmínce (a), kdežto spojení je (2,1,0).
Tím je tvrzení o svazu dokázáno nezávisle na historické atribuci
Tamarimu, jejíž primární pramen zůstává samostatně otevřen.

## Konečné kontroly a meze

check_other_trees.py nezávisle generuje 6 918 lesů do devíti uzlů jako
vnořené n-tice. Ověřuje rekonstrukce z tagů, oba směry F, G, celý P1–P5,
inverze permutací a charakterizace potomků. Podmínky (a) a (b) porovná
také na všech 874 omezených celočíselných posloupnostech do délky šest,
nikoli jen na již známých lesích. V těchto velikostech projde 19 415
dvojic pro souřadnicové minimum. Kompatibilní rodičovské uspořádání
zkouší v 14 162 pořadích seznamu. Jde o konečné doplnění uvedených
obecných důkazů, nikoli důkaz historické priority.


