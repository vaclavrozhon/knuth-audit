# §2.2.2-13: náhodné vkládání a odebírání

Aktualizace 1. listopadu 2026: všechny níže původně otevřené
matematické kroky jsou uzavřeny v
`../parallel/sequential-probability/critical-proof.md` a
`../parallel/sequential-probability/contracting-proof.md`.
Kořenová revize je v `sequential-probability-root-review.md`.
Starší označení částečnosti níže dokumentují stav před tímto
doplněním; jedinou zbývající mezí úlohy je plný časopisecký Yao1981.

m je kapacita společné paměti, p pravděpodobnost odebrání. Každý ze dvou
zásobníků se vybírá s pravděpodobností1/2. Stav(x,y) jsou jejich velikosti;
proces se zastaví při x+y=m. Pokus odebrat z prázdného zásobníku ponechá
stav. Pro0≤p<1 je zastavení téměř jisté: z libovolného stavu m po sobě
jdoucích vložení do prvního zásobníku zaručí dosažení hranice, s kladnou
pravděpodobností((1−p)/2)^m. Neúspěch po k takových blocích má nejvýše
geometricky klesající pravděpodobnost. Při p=1 se proces nezastaví;
věta knihy je výslovně limita p→1, nikoli hodnota pro p=1.

## Přesný příklad m=4

Pro každý cílový bod(j,m−j) definujme h_j(x,y) jako pravděpodobnost
zastavení právě tam. Na absorpční hranici je indikátorem daného bodu;
uvnitř je váženým průměrem čtyř následníků, se smyčkou na prázdných
zásobnících. Tyto lineární rovnice mají jediné řešení: rozdíl dvou
řešení je omezená harmonická funkce s nulovou hranicí a zastavení je
téměř jisté. Maticově jde o(I−Q)H=R, kde Q obsahuje přechody uvnitř
 a R přechody na hranici.

`check_sequential_probability.py` vyřešil všech10 přechodných stavů
pro m=4 symbolicky v p. Výsledky přesně souhlasí se všemi pěti
racionálními funkcemi na253; nejde jen o několik numerických hodnot.
Dále byly nezávisle dosazeny přesné racionální pravděpodobnosti pro
m=1..8 a p=0,1/3,1/2,2/3; součet1, symetrie a nezápornost souhlasí.

## Pevné m, limita p→1

Položme rho=(1−p)/p. Nezastavený proces na celé nezáporné kvadrantě
má pro p>1/2 stacionární pravděpodobnosti
pi(x,y)=(1−rho)^2*rho^(x+y): každá vodorovná i svislá hrana splňuje
rovnováhu protisměrných toků. Regeneračním cyklem rozumíme úsek od
návštěvy(0,0) k další návštěvě(0,0), případně jedinou smyčku.
Střední počet návštěv(x,y) v cyklu je pi(x,y)/pi(0,0)=rho^(x+y).

Před zásahem hranice m se očekávané počty návštěv vrstvy m−1 od těchto
hodnot liší oO(rho^m). Zásah totiž nastane s pravděpodobnostíO(rho^m)
na cyklus, a po něm je očekávaný počet návratů do této vrstvy omezen
pro pevné m a rho→0. Poslední tvrzení plyne z převahy kroků dolů
na každé neprázdné hladině; jejich pravděpodobnost je alespoň p/2,
zatímco celková pravděpodobnost kroku nahoru je1−p. Doba návratu do0
má tedy rovnoměrně omezenou střední hodnotu pro dost malé rho.

Každý vnitřní bod absorpční hrany má dva předchůdce ve vrstvě m−1,
krajní body mají po jednom. Toky prvního zásahu jsou proto v poměru
1:2:...:2:1, s relativní chybouO(rho). Po normalizaci má limita
hmotnost1/(2m) na obou koncích a1/m vevnitř. To je přesný význam
„essentially uniform“. Trapezoidový součet kusově lineární funkce
max(j,m−j) dává

lim_(p→1) E max = 3m/4 + [m odd]/(4m).                  (1)

Originál253 má skutečně **1/(4m)**, nikoli1/4: OCR ztratilo m ve
jmenovateli. Vzorec byl navíc přesně ověřen pro m=1..100, ale obecný
důkaz je vážený součet výše.

## Pevné0<p<1/2, m→∞

Zde delta=1−2p>0 a jde o rostoucí náhodnou procházku. Po C log(m)
krocích mají s pravděpodobností1−O(m^(−K)) oba zásobníky velikosti
mezi c log(m) a C log(m). Dolní mez plyne z Chernoffovy nerovnosti
pro nezávislé čisté počty vložení minus odebrání do každého zásobníku;
odrazy na nule velikost pouze zvětší. Konstanty volíme podle pevného p
 a libovolně velkého K. V tomto úseku ještě nelze dosáhnout m.

Z takových počátečních velikostí a,b je pravděpodobnost dalšího zásahu
některé osy nejvýše(p/(1−p))^a+(p/(1−p))^b, tedyO(m^(−K)).
Můžeme proto odstranit odrazy. Chyba středního maxima jeO(m^(1−K)):
při prvním návratu na osu zbývá z bodu(0,j),0≤j≤m, dokončit buď
odraženou procházku s maximem≤m, nebo neodraženou procházku, jejíž
střední maximum je≤m+O(sqrt(m)). Tento poslední odhad plyne z níže
uvedeného rozkladu a nerovnosti E|W_tau|≤sqrt(E tau). Silná Markovova
vlastnost tím zajišťuje uniformní chybu, bez nesprávného předpokladu,
že neodražené konečné maximum je bodově omezeno m.

Bez odrazů má celková velikost kroky±1 s driftem delta a potřebuje
urazit m'=m−a−b. Její doba prvního průchodu tau má
E tau=m'/delta a Var(tau)=4p(1−p)m'/delta³. Například to plyne
diferencováním generující funkce [G(z)]^m', kde
G(z)=(1−sqrt(1−4p(1−p)z²))/(2pz).

Podmíněně na tau je rozdíl velikostí a−b+W_tau, kde W je jednoduchá
symetrická procházka nezávislá na posloupnosti kroků celkové velikosti.
Z binomických koeficientů a Stirlinga,
E|d+W_t|=sqrt(2t/pi)+O((d²+1)/sqrt(t)) pro|d|=O(log m),t≥m'.
Protože tau≥m' a Var(tau)=O(m), Taylorův rozvoj odmocniny dává
E sqrt(tau)=sqrt(m'/delta)+O(m^(−1/2)). Dosazení m'=m−O(log m) uzavírá

E max = m/2 + sqrt(m/(2*pi*(1−2p)))
              +O(m^(−1/2)*(log m)^2).                            (2)

Jde o vlastní úplný rozpis argumentu, s potřebným chybovým členem
knihy. Původní autorův reportSTAN-CS-79-708 byl přečten v celém
technickém textu1–17 (PDF3–19), zvlášť obrazy4 a17. Report uvádí
silnější chybuO(log m/sqrt(m)); časopisecký abstrakt1981 a kniha mají
log²m. Verze se nezaměňují; pro kontrolu knihy postačuje(2).

## Kritický případ a další otevřené kroky

Pro p=1/2 lze limitní odraženou Brownovu procházku na trojúhelníku
rozvinout odrazy do kosočtverce|x|+|y|≤1 a otočit na čtverec
−1≤u,v≤1. Při výstupu je maximum původních souřadnic
(1+|druhá souřadnice výstupu|)/2. Řešení Dirichletovy úlohy ve čtverci
pomocí kosinových módů a_k=(k+1/2)pi dává konstantu

alpha_square = 1−2 sum_(k≥0) 1/(a_k² cosh(a_k)).                   (3)

Na svislých stranách má funkce1−|v| rozvoj
sum2/a_k² cos(a_k v); příspěvek obou svislých stran v počátku je
sum2/(a_k²cosh a_k). Přidáme obě vodorovné strany a faktor1/2 výše,
čímž dostaneme(3). Toto odvození je odděleno od ještě potřebného
přesného zdůvodnění přechodu z diskrétního procesu a ekvivalence(3)
s tištěnou řadou

alpha_book = 1/2 + 4/pi² sum_(n≥1) sin(n*pi/2)/(n²*sinh(n*pi/2)).  (4)

Obě exponenciálně konvergentní řady numericky dávají
0.675314483313567611597758668255117756950853449779064019497914.
Výsledek odpovídá číslicím knihy. Numerická shoda však sama nedokazuje
equivalenci řad. Přesná ekvivalence a limitní přechod zůstávají otevřené.

Flajoletův původní článek1986 byl čten v úvodu, kombinatorické redukci
 a příslušných větách2/3, včetně obrazů336–337. Používá jiné p: jeho
pravděpodobnost jednoho vložení je(1−p_knihy)/2. Věta3 potvrzuje
rovnoměrnou limitu pro pevné p_knihy>1/2, tedyEmax~3m/4. Článek detailní
asymptotický výpočet vynechává; jeho úplná nezávislá rekonstrukce zde
ještě není provedena. Původní numerické0.67526 na336 se liší od správné
hodnoty v knize a z tohoto rozdílu nevzniká nález vTAOCP.

Výsledky symbolických a numerických kontrol jsou v
`results/sequential-probability.json`. Koeficienty úlohy14 jsou obecně
dokázány v `sequential-allocation.md`; zde provedená samostatná integrace
normální hustoty je pouze doplňková kontrola jejich číselných hodnot.
