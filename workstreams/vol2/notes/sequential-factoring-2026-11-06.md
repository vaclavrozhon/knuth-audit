# §4.5.4 — souvislé argumenty: faktorizace a prvočíselnost

6. listopadu 2026, první blok V2-X0145. Přečtena původní sazba
379–396, zadání 412–414 a odpovědi 657–662. Toto předání uzavírá
párování prvních 18 stran hlavního textu a úloh 1–10, 17, 18, 21, 22;
další části přečtených odpovědí zatím nejsou tímto blokem přejaty.
Podrobné položky jsou v results/sequential-factoring-evidence.json.

Uzavřené starší důkazy a výpočty se přebírají. Zejména se znovu
nespouštěl rho census do miliardy, Carmichaelův census, velké
prvočíselné certifikáty, Dickmanova síť ani testy AKS. Nově se počítalo
jen šest řádků analytické tabulky na 382, s nice 15 a intervaly Arb.
Žádný nový potvrzený nález v tomto bloku.

## Převzaté matematické argumenty

`factoring-basic.md`: invariant, správnost a konečnost A, přesný
počet dělení t+k, celé příklady, primorialový test, kvadratické třídy,
opravené síto S, Mertensův součet a konstanta. Obrázek 11 má stejné
přechody jako A1–A7; větev A6 „Yes“ odpovídá q <= d_k.

`factoring-distribution.md`: existence všech potřebných limitních
rozdělení s chybou, rovnice F/G/H, jejich kraje, všechny kvantily
a obraz 12, spojitost s cykly permutací, normální zákon, variance
i konstanta počtu faktorů. Heuristická motivace není zaměněna za
důkaz; poznámka obsahuje samostatné obecné argumenty.

`factoring-rho.md`: kongruenční invariant B, přesná detekce cyklu,
selhání a složené výstupy, konečné očekávané meze, fázové oscilace,
vypuštění testů a Floydovo srovnání, všechny tabulkové hodnoty.
Předpověď rychlosti pevného x²+1 a praktické odhady pro 12/18 číslic
zůstávají modelové. Výzkumná úloha 21 nemá obecné požadované řešení:
nově je proto i její celkový stav `partial`. Audit formulace a konečné
výsledky zůstávají zachovány, nejsou vydávány za důkaz hypotézy.

`factoring-fermat.md` a `factoring-context.md`: úplné C/D, maximalita
nalezeného dělitele, konečnost, přesný počet hlavních kroků, všechny
zbytkové tabulky a číselné příklady, CRT a bitové síto, Lehmanova mez.
C0150 opravuje párovací index, C0151 počet slov při návratu indexu,
C0152 chybný převod rychlosti. Oprava C5 a změny jmen/AND jsou známá
errata a nevytvářejí naše karty.

`primality-basic.md`: Fermat, řádové kritérium a různé báze,
Korselt, Prattův strom a jeho velikost, všechny kongruence a rozklady
příkladu 2^214+1. `primality-extended.md` doplňuje BLS a přesný rozsah
externích APR a Adleman–Huangových vět. `primality-probabilistic.md`
má invariant P, všechny mocninné i bezčtvercové případy, ostrou
čtvrtinovou mez, oba číselné příklady a opakování nezávislých pokusů.
Pocklingtonův dopředný odkaz na 393–394 používá už uzavřený obecný
důkaz v `primality-deterministic.md`; vlastní párování celé úlohy 26
patří do následujícího bloku.

AKS dodatek: standardní kritérium a čas mají vlastní obecný důkaz
v `primality-aks.md`. Záměna parametru C0153 je potvrzený překlep.
C0155 zůstává kandidát: nadbytečnost obou vynechaných předtestů
není obecně dokázána ani vyvrácena. Absence protipříkladu v dřívějších
konečných testech tuto mezeru neuzavírá. Starý údaj o 250 číslicích
za několik hodin je dobové měření/odhad, ne ověřený univerzální čas.

## Doplnění k 379–382 a 391

Jednoznačnost (1): existence plyne indukcí podle N, rozdělením
složeného N na menší činitele. Je-li p prvočíslo a p nedělí a,
Bézoutova identita dává sa+tp=1; z p | ab pak plyne p | b.
Opakované použití tohoto lemmatu spáruje prvočinitele dvou rozkladů.
Seřazení odstraní permutace, N=1 má prázdný rozklad.

PNT v (3) přebíráme jako výslovný analytický vstup. Pro kontrolu
přesného tvaru byl přečten Platt–Trudgian, arXiv:1809.03134v2,
str. 3–4: Corollary 2 implikuje (3), protože pevnou mocninu ln x
lze absorbovat snížením kladné konstanty před sqrt(ln x).
Zmíněný Korobovův–Vinogradovův tvar má také správné exponenty.
Převod z psi na pi používá částečné sčítání; příspěvek vyšších
prvočíselných mocnin je O(sqrt(x) ln²x) a je menší než tento zbytek.
Nejde o nový důkaz celé analytické věty ani o kontrolu všech
historických priorit 1798/1899 či kapitoly Walfisze.

Vlastní odvození (4): pro pevné j je

    integral_2^x dt/(ln t)^j
      = x/(ln x)^j + j integral_2^x dt/(ln t)^(j+1) + konstanta.

Iterace dává všechny faktoriály. Poslední integrál je
O(x/(ln x)^(r+2)): rozdělíme jej v sqrt(x); dolní část je O(sqrt(x))
a horní má ln t >= (ln x)/2. Chyba (3) je menší než každá taková
pevná logaritmická mocnina. Jde o asymptotický rozvoj pro pevné r,
nikoli konvergentní nekonečnou řadu.

Riemannova (5) je v knize výslovně vyvrácená historická domněnka.
Konečný součet má horní mez floor(lg x), jak opravují známá errata.
Jeho členy od k=3 mají součet O(x^(1/3) ln x), zatímco k=2 dává
záporný člen −L(sqrt(x))/2 řádu sqrt(x)/ln x. Littlewoodova kladná
oscilace pi(x)−li(x) tedy domněnku skutečně vyvrací. Přesná formulace
Littlewoodovy věty je zde externí vstup, porovnaný s rovnicí na str. 9
Tahiřiny disertace MIMS EPrint 2010.97; originál 1914/1918 a jeho
důkaz nejsou znovu auditovány. Úvodní nepřesnou větu disertace, že
konečná numerická evidence něco dokázala pro všechna x, nepřebíráme.

Podmíněný důsledek RH: standardní explicitní formule pro psi,
s výškou T řádu x a počtem nul O(T ln T), dává za RH
psi(x)=x+O(sqrt(x) ln²x). Součet 1/|gamma| do T je O(ln²T);
jeho přesnější externí znění je také Lemma 2 Platt–Trudgian.
Vyšší prvočíselné mocniny mají tentýž nebo menší řád. Z identity
pi(x)=theta(x)/ln x + integral_2^x theta(t)/(t ln²t) dt
proto plyne pi(x)=L(x)+O(sqrt(x) ln x), přesně jak kniha uvádí.
Není to důkaz RH. Samotné explicitní formule a odhad počtu nul
jsou deklarované analytické vstupy, nikoli konečné numerické testy.

Pro tvrzení na 391 o podílu primitivních kořenů se přebírá
m/phi(m)=O(ln ln m) z `euclid-heilbronn.md` a z doplnění X0144.
Dosazení m=n−1 a n/(n−1)<=2 dává uvedenou mez. Přesný počet
phi(n−1) vyplývá z cyklické grupy: generátory g^a jsou právě
exponenty a nesoudělné s n−1.

## Nová kontrola tabulky a pramenů na 382

Všech šest řádků pi(10^e), e=3,6,9,12,15,18, souhlasí s tabulkou IV
na 766 článku Oliveira e Silva 2006. Tato původní tabulka byla
přečtena obrazově. Hodnoty do miliardy navíc kryje uložený dokončený
census; větší tři hodnoty jsou převzatý externí výpočet, neopakovaly se.

Nový malý výpočet certifikuje všech 12 desetinných buněk dvou dalších
sloupců v intervalech Arb s 90 desetinnými místy. Používá přesně
L(x)=Ei(ln x)−Ei(ln 2) a konečný součet mu(k)L(x^(1/k))/k.
Každý interval leží uvnitř buňky zaokrouhlení šířky 0.1; konec součtu
je získán celočíselně z bit_length(x)−1. Nezaměňuje se obecná Riemannova
R-funkce s konkrétní konečnou aproximací v knize.
Zdrojový program a výsledky: `verify_sequential_factoring_followups.py`,
`results/sequential-factoring-followups.json`.

Brent1979, str. 1361, přímo potvrzuje počet 75 milionů, horní výšku
32585736.4, jednoduchost nul i Lehmerovu metodu. Autorská stránka
uvádí pozdější opravy pomocné meze; podle autora tento výpočet
neovlivnily. Převzato jako historický výsledek s tímto omezením;
výpočet nul ani celý článek nebyly nově reprodukovány.
URL, otisky a rozsah čtení jsou v `sources/sequential-factoring-sources.json`.

## Drobné doménové podmínky a otevřené části

Zaznamenáváme dvě jednoduché kvalifikace bez přehánění dopadu:
na 384 platí 1<=t<=lg N pro N>=2; už definovaný N=1 má t=0.
Na 385 má x²+1 právě (p+1)/2 obrazů pro liché p; p=2 má dva.
V praktickém kontextu se faktor 2 předem odstraňuje a heuristika
velkých faktorů tím není narušena. Jsou to zapsané okrajové podmínky,
nikoli nové potvrzené chyby algoritmu. Stejně zachováváme dříve
zdokumentovanou podmínku p nesoudělné s N u zpřesnění síta na 388.

Praktické časové odhady, tvrzení o lidské ruční práci, historické
zkušenosti s pseudoprvočísly a dostupnost zdrojů mají přesné limity
ve výše uvedených původních poznámkách. Nekvantifikované „usually“
nepřepisujeme na uniformní větu. Nepotvrzená bibliografie je přeskočena.
Matematické mezery AKS a výzkumné úlohy 21 zůstávají otevřené.
Další kurzor: 396/file408, poslední odstavec o řetězových zlomcích,
pak 397; souvislé párování zbývajících úloh a odpovědí pokračuje.
