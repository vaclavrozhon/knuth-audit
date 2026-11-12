# Souvislý průchod §1.2.8 — 5. listopadu 2026

Přímo přečteny původní strany79–86 a493–496, soubor94–101 a508–511.
Harmonický obsah společných stran79/493 byl uzavřen předchozím X0941;
generující funkce v dolní části496 ještě ne. Přečteno všech pět
matematických poznámek: `fibonacci-basic.md`, `fibonomial.md`,
`fibonacci-representations.md`, `phi-number-system.md`,
`fibonacci-words-and-games.md`. Přijaty přesné dřívější pramenné
recenze X0100,X0705–06,X0711–12,X0910 a oba uložené výsledkové soubory.
Žádný úspěšný výčet ani prvočíselný certifikát se znovu negeneroval.

## Zkontrolované části a jejich obory

Všechny matematické části hlavního textu a42 úloh jsou pokryty.
Matice Q má determinant−1, takže maticové identity, Cassiniho vztah,
sčítání indexů a Binetův vzorec přecházejí na všechny celé indexy.
Gcd věta používá nezáporné indexy; případ(0,0) buď konvenci gcd=0,
nebo výslovné vyloučení. Zaokrouhlení phi^n/sqrt(5) platí pro n>=0,
nikoli obecně pro záporné indexy. Formální vytvořující funkce má
invertibilní jmenovatel; analytický poloměr je přesně1/phi.

Prověřeny všechny nehomogenní rekurence, polynomiální součty včetně
odstranitelných singularit, tridiagonální determinant, kongruence
ve čtyřech třídách indexu, binomické součty a tabulka fibonomických
koeficientů. Celočíselnost má obecný rekurentní důkaz; rekurence
mocnin vzniká konečným q-binomickým rozkladem charakteristického
polynomu. Znaménko je opravdu ceil((m−k)/2); při m=1 je nultá
mocnina konstantní polynom1, také v0. Nejde o použití sporné
nekonečné q-řady z C0006.

Zeckendorfovy reprezentace rozdělují interval[0,F_(K+1)−1] na dva
disjunktní intervaly podle nejvyššího indexu. Posuny využívají ostré
meze −phi^(-2)<sum psi^k<phi^(-1), a tím řeší i hraniční zaokrouhlení.
Společná reprezentace dvojice(m,n) existuje právě při m+phi*n>=0;
rovnost znamená prázdný součet. Originál496 má správně neostrou mez.
Zápis báze phi má jednoznačnost po vyloučení sousedních jedniček
a nekonečného střídavého konce. Konečnost všech celočíselných zápisů
vyžaduje intervalový indukční invariant; samotná algebra pravidel
by nestačila. Opravené pravidlo jej zachovává.

Fibonacciho slovo je jediný pevný bod b->ba,a->b začínající b.
Beattyho pozice, hustota a pravidlo nejnižšího indexu souhlasí.
Herní důkaz pokrývá všechny vítězné tahy, nejen doporučený nejmenší
člen: musí se odebrat celý konec reprezentace a předchozí člen musí
být větší než dvojnásobek odebraného součtu. Pro1000 je jediný
legální vítězný první tah13. Minimax úlohy40 má kapacitu
F_(m+1) listů při ceně nejvýše m, s A_0=A_1=1; všechny menší
počty listů jsou dosažitelné. Přesný odkaz na stromy V3 byl již přijat.

Racionální intervaly potvrzují obě tištěná logaritmická zaokrouhlení
a209 číslic F_1000 s první číslicí4. Rekurzivní19uzlový certifikát
dokládá prvočíselnost2^127−1 nezávisle na jeho historickém připsání.
Výsledky300053 a1618567 konečných kontrol jsou podpůrná evidence,
nikoli náhrada obecných důkazů či nově spuštěné výpočty.

## Opravy a mapa

Nový nález nevznikl. Všech pět dnešních erratových zdrojů má hash
shodný s přijatými vrstvami. X0099 mapujeme na původní79,80,81,83,
85,86,493,495: překlad názvu a rozsahy citací; jména a bibliografická
značka; quadratic equation/polynomial a historická atribuce;
meze úloh22/23/25/31 a značka determinantu; G(z) v odpovědi12;
obě chyby phi-rekurence a bibliografie na495.

Samotné F_k|F_(nk) na81 je pravdivé stejně jako nové F_n|F_(nk).
Původní horní mez k+1 pro Eukleidův algoritmus je pravdivá; nové
k−1 je silnější a teprve toto znění potřebuje k>1. Změny značek
posloupnosti na80/82, doplnění −1/phi, širší tabulka29, trigonometrický
dodatek19 a nové křížové odkazy nejsou novými matematickými vadami.
Původní odpovědi14 a21 jsou algebraicky ekvivalentní náhradám;
odpověď31 s odkazy8 a11 není chybná jen proto, že nyní stačí11.
Tyto redakční změny samy nevytvářejí červenou stránku.

## Bibliografické výjimky a otevřená fakta

Úlohy30,34,41 se uzavírají s přesně uvedenými výjimkami:
Riordan1962,5–12; časopisecké originály Lekkerkerker1952,190–195
a Zeckendorf1972,179–182; konkrétní provenance Matiyasevichova údaje1990.
Poslední výjimka nepopírá autorství: původní článek1968 má přesně
požadovanou formuli a byl již přečten. Starší publikace sama nevyvrací
dataci soukromého sdělení. Jardenovy citované30–33 a dobový
Lekkerkerkerův report1951 jsou doloženy, nikoli vydávány za jiné texty.
Pramenné záznamy se tím nepřepisují na ověřené.

Hlavní historické výroky na79–81 zůstávají partial: Liber Abaci1202
a citované znění, životopis, indická chronologie, Keplerova historie,
Légerovo prvenství1837, Lucasovo pojmenování a historický důkaz,
Simon Jacob, původ značky phi, Keplerův dopis a Cassiniho prvenství,
Lucasova atribuce1876. Hodnotící soud o estetice není matematická věta.
Bibliografické detaily Boncompagni, Singh, Kepler, Conway–Guy, Coxeter,
Gardner, Markowsky, Schreiber, Cook a Dickson nebyly v tomto bloku
nezávisle dočteny. Přesné starší pramenné mezery jsou zachovány v X0101.

Strany82–86,493–495 mají dokončený obsahový průchod s těmito
bibliografickými výjimkami; mapované vady mají přednost před zelenou.
Strana496 čeká na navazující §1.2.9. Celkem859/932 původních úloh
uzavřeno,73 partial; celý svazek dokončen není.
