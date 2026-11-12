# Euler, Waring a Sylvester: uzavření §1.2.3–33

V1-X0750, 2. listopadu 2026. Celá úloha je checked společně s dříve
přijatým důkazem v sums-and-products.md a návazností v generating-symmetric.md.
Úspěšné matematické testy se neopakovaly. Nový nález nevznikl.

Root ověřil 41 souborů a čtyři zachované vstupní PDF zmrazeného
MANIFEST-euler-waring-sylvester33.json, SHA-256
`3099194069ca37876e6a4b723b7970573cf45ad462c62746af6d25e4a90bd794`.
Přečetl celou agentovu poznámku a předání, přímo porovnal knižní s. 36,
472–473 a rozhodné erratum all1-prepre, PDF 31. Agentův extrakt
zachycuje všechny čtyři vrstvy veřejných errat.

Pro různé uzly x_1,...,x_n nechť D_i je součin rozdílů x_i-x_j přes
j odlišná od i a S_r=sum_i x_i^r/D_i. Úplný homogenní symetrický
polynom h_d je součet všech monomů stupně d s koeficientem 1;
h_0=1 a h_d=0 pro záporné d. Přijatý obecný výsledek je
S_r=h_(r-n+1), včetně n=1. Následující kontrola doplňuje prameny,
nikoli nový důkaz této identity.

## Euler a Waring

Eulerův dopis Goldbachovi CLXXII má na s. 663 datum Berlín
9. listopadu 1762. Použitá Fussova tištěná edice korespondence
1843–1845 je primární edice, nikoli obraz rukopisu.
Root přímo četl s. 663 a 665–666; agent celý dopis 663–666
a identifikační list ETH. [Dochovaný výřez](https://www.e-rara.ch/download/pdf/15664117.pdf)
obsahuje rozklad z^r/product(z-a_i) na jednoduché zlomky
s koeficienty a_i^r/product_(j!=i)(a_i-a_j). Připojením z jako
dalšího uzlu dostáváme S_r=0 pro r<n-1. Celý obecný vzorec h_d
tomuto dopisu nepřipisujeme.

Root přímo četl titul prvního vydání *Institutionum Calculi
Integralis*, II, Petrohrad 1769, a s. 432–435, §§1169–1171
a začátek §1172. [První vydání](https://archive.org/download/bub_gb_XR-zzDxJJ-0C/bub_gb_XR-zzDxJJ-0C.pdf)
potvrzuje produkty rozdílů a nulový součet v §1169; §1171
doplňuje mezní hodnotu S_(n-1)=1 z polynomiální části zlomku.
Poslední uzel z se započítává do počtu uzlů, nikoli jako nulový
faktor z-z ve jmenovateli. Normalizace 1/N v §1170 pochází
z předcházející diferenciální rovnice a není hodnotou našeho S_r.
Toto vydání se nezaměňuje s pozdějším tiskem 1827.

Waringův článek *Problems concerning Interpolations*, Phil. Trans.
69 (1779), 59–67, má na s. 59 datum čtení 9. ledna 1779.
Root přímo četl s. 59 a citované s. 64–67; agent celý článek.
[Institucionální kopie původní sazby](https://www.math.unipd.it/~alvise/TALKS/LINCEI/ALTRO/WARING/WARING_Waring-ProblemsconcerningInterpolations-1779.pdf)
obsahuje interpolační polynomy product_(j!=i)(t-x_j)/(x_i-x_j).
Porovnáním jejich koeficientů autor získává nulové hodnoty a
S_(n-1)=1 se stejným pořadím rozdílů jako v knize. Další formule
pracují s elementárními symetrickými součty vynechaných uzlů;
netvrdíme, že zde stojí celý obecný vzorec h_d pro libovolné r.

## Přesný rozsah Sylvesterova dokladu

Použit primární přetisk *Collected Mathematical Papers*, II,
Cambridge 1908. Root přímo četl titul, s. 90–91, 119 a 155–157;
agent navíc celý článek 18 na s. 90–99. Záhlaví článku 18 uvádí
Quarterly Journal of Mathematics 1 (1857), 141–152 a paralelní
tisk v Tortoliniho Annali 8 (1857), 12–21. Samostatný ročník
1857 není v této kontrole přímo kolacionován.

Na s. 90–91 Sylvester výslovně popisuje větu vyjadřující součty
homogenních mocnin a součinů pomocí parciálních zlomků, pro různé
i splývající proměnné. Připomíná Cayleyho a Terquemův návrh použít
Cauchyho rezidua. Je to obsahově relevantní doklad atribuce a metody,
ale nikoli samostatně vysázená formule S_r=h_(r-n+1) s úplným důkazem.

Výslovné formule pro dva, tři a čtyři uzly jsou v šesté přednášce
článku 26, s. 156. Předchází jim definice H_d jako našeho h_d;
exponent v čitateli je d+n-1, takže převod na knižní r je přesný.
Následující s. 157 pojednává o splývání uzlů. S. 155 datuje přednes
4. července 1859; předmluva na s. 119 rozlišuje soukromé osnovy
připravené před přednáškami a první veřejný tisk v Proc. London
Math. Soc. 28 (1897), 33–96. Soukromý tisk 1859 nebyl získán.
Tyto explicitní formule tedy nepřipisujeme článku 1857. Rozlišení
nemění relevantní odkaz v TAOCP na automatický nález chybné citace.

## Známé opravy a návaznost

Oprava z 6. ledna 2009 upřesňuje symetrické koeficienty polynomu
P, které nezávisí na indexu j, a přidává odkaz na §1.2.9–10.
Druhý dodatek odkazuje na rovnici (33): slabě rostoucí posloupnosti
indexů jsou právě násobnosti proměnných v monomech h_d.
Obě návaznosti pokrývá již přijatá generating-symmetric.md.
Kontrola uzavírá konkrétní úlohu a její citace; není průzkumem
absolutní historické priority ani auditem celých externích článků.
