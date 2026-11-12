# §7.1.1–28/29: pokrývací funkce a lineární buddy scan

6. listopadu 2026, X0069. Původní zadání p82/file99 a odpovědi
p538/file555. Bez programu. Přesné seznamy prime krychlí a minima
z P0599/P0600 se přebírají, nikoli znovu počítají.

## P0648: celý konkrétní příklad pokrývací funkce

Prvoimplikanty p_1,…,p_5 z (29)/(30) jsou postupně
000*,0*00,*100,*111,11**. Pro osm pravdivých bodů v jejich původním
pořadí jsou množiny pokrývajících indexů

    {1,2}, {1}, {2,3}, {4}, {3,5}, {5}, {5}, {4,5}.

Každá z osmi klauzulí g proto přesně souhlasí se zadáním. Jednotkové
klauzule vynutí y_1,y_4,y_5; zbývá jen y_2∨y_3. Tedy

    g=y_1 y_4 y_5 (y_2∨y_3)
     =y_1 y_2 y_4 y_5 ∨ y_1 y_3 y_4 y_5.

Oba termy tvoří kladný antichain, takže jsou právě všechny prime
implikanty g podle P0611. Souhlasí oba vytištěné rozvoje. V odpovědi
uvedené obecné ilustrační nastavení y_1=y_4=y_6=1 znamená vybrat
p_1,p_4,p_6 v případu q≥6; není to další hodnota konkrétního
pětiimplikantového příkladu zadání.

## P0649: přesná korespondence a její doména

Pro libovolné S⊆{1,…,q} položme D_S=∨_(j∈S)p_j a
T_S=∧_(j∈S)y_j. Každé p_j implikuje f, takže D_S≤f. Definice g
říká, že S zasahuje každý seznam prime krychlí pokrývajících
pravdivý bod právě když D_S=f. Ekvivalentně g(1_S)=1.
Protože g je monotónní, platí

    D_S=f ⇔ g(1_S)=1 ⇔ T_S je kladný implikant g.

Různé S dávají různé seznamy prime členů a různé kladné termy.
Pořadí a opakování členů se zde stejně jako u rodin prime členů
nepočítá jako jiná DNF. Inkluzní minimalita S znamená současně
irredundantní cover a prime implikant g. Tím jsou oba směry
prime/irredundant korespondence doloženy.

Pomocná věta odpovědi doslova říká „every implicant of g“.
Přesná bijekce výše je s **kladnými** implikanty. Obecné konzistentní
termy mohou obsahovat záporné literály: v knižním příkladu jsou
y_1 y_2 y_4 y_5 a y_1 y_2 ¬y_3 y_4 y_5 různé implikanty se stejným
kladným supportem a stejným D_S. Záporný literál lze díky monotónnosti
odstranit, ale to není injektivní operace. Tento doménový limit
zaznamenáváme výslovně; bez rozhodnutí o implicitně kladném významu
pomocné věty z něj nevzniká karta nálezu. Prime korespondence ani
zadání o nejkratších DNF tím nejsou zpochybněny.

## P0650: nejkratší DNF, nikoli libovolný minimální počet termů

Každý konzistentní term DNF lze rozšířit do prime implikantu f.
Pokud jím ještě není, odstraní se alespoň jeden literál, a tím se
výraz opravdu zkrátí. V nejkratší DNF tedy všechny členy jsou prime.
Žádný nemůže být redundantní, jinak by šel celý vypustit. P0649 proto
přiřadí nejkratší DNF prime implikant g, což je přesně zadání28.

Je zde použit význam nejkratšího výrazu s počítanými literály/operacemi,
nikoli pouze minimalizace počtu termů s ignorováním jejich délky.
Například x∨(¬x∧y) má minimální počet dvou termů pro x∨y, ale není
nejkratším výrazem a druhý člen není prime. Tento rozdíl se nepřenáší
do hlavního tvrzení. Irredundantní cover navíc nemusí být globálně
nejkratší: zpětná implikace z libovolného prime g do optima f se
netvrdí. Pro uvedený příklad obě možnosti mají čtyři členy a jedenáct
literálů, přesné minimum už doložené v P0600.

Pro f=0 je q=0 a g prázdná konjunkce1; prázdný term g odpovídá
prázdné DNF f. Pro f=1 je jediný prime f prázdný term a g=y_1.
Okraje proto korespondenci nenarušují.

## P0651: orientace a hlavní invariant algoritmu B

Vstup jsou různé vzestupně seřazené n-bitové hodnoty v_0,…,v_(m−1)
a bit 0≤j<n. Při dvojici s k<k' a v_k'=v_k⊕2^j musí bit j hodnoty
v_k být0. Pak je partner roven v_k+2^j, bez přenosu do jiného bitu.
Proto B2 správně vynechává všechny dolní kandidáty s bitem1.

Hlavní invariant: všechny indexy menší než k už byly vyřešeny;
pro současný nulový bit je k' dolní vyhledávací mez a všechny
indexy l<k' mají v_l<v_k+2^j. Inicializace jej splňuje. Zvětšení k
zvyšuje cíl, takže staré vyloučené indexy zůstávají vyloučené.
B3 může přeskočit do k+1, protože hodnoty na indexech≤k jsou pod
cílem. B4 se zastaví přesně na prvním v_k'≥v_k+2^j, nebo na m.

Je-li k'=m, nemá partner současný ani žádný pozdější nulový kandidát:
jeho cíl by byl ještě vyšší. B6 při rovnosti vypíše jediného partnera;
při ostré nerovnosti partner neexistuje. B7 uzavře právě tento index
a invariant platí dále. Výpis je podle rostoucího k, bez duplicit.

## P0652: proč je správný také netriviální skok B5

Položme H=2^(j+1). Cíl v_k+2^j zůstává ve stejném H-bloku jako
v_k, v jeho horní polovině. Pokud v_k⊕v_k'≥H, jsou oba údaje v
různých H-blocích a v_k' leží v pozdějším bloku. Přitom podle B4
mají všechny indexy l<k' hodnotu pod původním cílem.

Každý další nulový kandidát r s k≤r<k' proto leží ve spodní polovině
téhož původního bloku. Jeho partner by byl v horní polovině tohoto
bloku, nejméně roven původnímu cíli, ale menší než v_k'. Žádná taková
hodnota na vstupu není, protože k' byl první index nad původním cílem.
Lze tedy bezpečně položit k=k'. To zdůvodňuje právě optimalizaci,
kterou by samotný argument dvou ukazatelů bez B5 nepokryl.

## P0653: ukončení, deklarovaný čas a okraje B

Oba ukazatele se pouze zvětšují. B5 má k'>k, B7 zvyšuje k o1,
a B2/B4 provádějí dohromady nejvýše m zvýšení každého ukazatele.
Počet návratů do hlavní smyčky je také O(m), stejně jako počet
výstupů. Při konstantním čase n-bitových operací je tedy celý čas
O(m), jak zadání požaduje. Extra pracovní paměť je konstantní počet
slov, nepočítáme-li vstup a vypisované páry.

Pro m=0 skončí B2 před přístupem ke v_0; pro m=1 nevznikne dvojice.
Při j=n−1 je podmínka B5 vždy nepravdivá, protože XOR dvou n-bitových
hodnot je menší než2^n; nemusí se materializovat přetékající n-bitová
konstanta. Aritmetika pseudokódu jinak používá přesné celočíselné
meze. B3 je volitelná optimalizace, protože B4 by tytéž indexy
přeskočilo; B5 lze také vypustit a standardní invariant i lineární
čas dvou ukazatelů zůstávají. Tím jsou doloženy i oba dodatky odpovědi.

## Rozsah a errata

P0648–P0653 mají argument v uvedených doménách. Relevantní řady
all4a-pre/all4a/err4a/all4f0/err4f0 neobsahují změnu28/29 ani
upřesnění pomocné bijekce; prohlédnuty byly navíc all4f1/err4f1.
Historické Quine/Cutler/Muroga odkazy nebyly bibliograficky ověřeny.
Odkaz na podobný postup v úloze 5.2.4–19 není použit jako premise.
Další část X0069 je vlastní generátor podkrychlí v30.
