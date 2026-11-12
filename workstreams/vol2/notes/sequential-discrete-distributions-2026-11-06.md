# Souvislá revize §3.4.1 F a navazujících úloh

6. listopadu 2026, X0121/X0122. Přímo přečteny původní136–142
a587–590; tento blok uzavírá F a úlohy17–19,22–23,25–30,32–33
v níže vymezeném rozsahu. G, logistická24 a Wallaceova31 pokračují
samostatně. C0056 a C0057 znovu potvrzeny, obě nyní **low** podle
skutečného dopadu. Nový nález nepřibyl. Stránkování je printed+12.

Přečteny byly celé [starší důkazy](discrete-distributions.md), celý
`verify_discrete_distributions.py` a všechny tři PASS bloky protokolu.
Výsledky přijímáme bez opakování výpočtu:2184 integračních kontrol
binomického dělení,630 hodnot spojité binomické CDF,1386 přesných
bitových modelů,361812 přechodů,80 průměrů,126 logických výrazů
s10920 řádky,1694 krajních modelů elipsoidu a1530 bitových modelů
exponenciály. Čtyři numerické ukázky asymptotiky jsou orientační,
nikoli intervalové certifikáty; obecný důkaz na nich nezávisí.

## Důkazy a jejich předpoklady

Geometrická(39) je počet pokusů včetně úspěchu: pro0<p<1,
q=1−p, událost N=n odpovídá q^n≤U<q^(n−1). To platí i na
přesných dyadických hranicích. p=1 se vrací zvlášť jako N=1;
p=0 nemá konečný čekací čas. CDF, PGF, střed1/p a rozptyl q/p²
v odpovědi17 souhlasí. Pomocný lineární polynom H s q=1/p
nemusí být PGF; užité formální derivace reciproku jsou přesto správné.

Úloha18 plyne z PGF dvou geometrických veličin a odečtení1.
Pro negativně binomickou19 je pro libovolné t>0 koeficientová
rekurence p_(n+1)=p_n*q*(t+n)/(n+1), p0=p^t. Z ní plyne
inverzní algoritmus, pro celé t také součet geometrických veličin.
Gamma–Poissonova směs je doložena úplným gamma integrálem a platí
i pro necelé t. U t=p=1/2 je průměr1/2 a očekávaný počet
navštívených hmotností1.5.

Binomické dělení používá a-tou nejmenší, tedy b-tou největší
z a+b−1=t uniformních hodnot. Podmíněné počty pod a nad ní jsou
binomické; obě integrace vracejí přesnou původní hmotnost.
a=1+floor(t/2) půlí zbylý parametr v každé větvi. Nejde o
tvrzení nezávislosti již seřazených hodnot; nezávislé jsou hodnoty
před zapomenutím pořadí v příslušných intervalech.

Poissonova konstrukce příchody, součinový test a střed μ+1
spotřebovaných U souhlasí. V(40) se při n=0 čte druhý ocas jako
nula, protože S0=0 nemůže překročit1. Není potřeba číselně počítat
(−1)!. Pro μ=0 vracíme přímo0.

Rychlejší rekurze s X~gamma(m) je přesná v obou větvích:
X<μ dává m+Poisson(μ−X), X≥μ dává Bin(m−1,μ/X).
Samostatné beta/gamma integrace dokazují každou výslednou hmotnost.
Normalizované exponenciální mezery mají konstantní hustotu na
simplexu a jejich součty jsou uniformní pořadové statistiky.
Faktory μ exp(−t/μ) v pomocném f na137 nejsou normalizované
hustoty, ale společná konstanta se v poměru f/f(1,…,1) zruší;
nejde o novou chybu výsledného podmíněného zákona.

O(log μ) čteme jako očekávanou cenu. Pro m≥1 dává Cauchyho
nerovnost Pr(X≥m/2)≥m²/(4(m²+m))≥1/8. Při pevném0<α<1
a dostatečném μ platí m=floor(αμ)≥αμ/2. Každý takový úspěšný
krok skončí binomickou větví nebo sníží μ alespoň faktorem1−α/4.
Podmíněná pravděpodobnost úspěchu zůstává nejméně1/8, tedy celková
očekávaná cena je O(log μ); binomická větev nastane nanejvýš jednou.
Nejde o deterministickou mez nejdelšího možného běhu. Dobové
experimentální doporučení α=7/8 na137 není znovu doložené měřením.

Úloha22: spojitá Poissonova CDF je rostoucí gamma ocas jako funkce
parametru; její rozdíl v sousedních celých bodech dává Poissonovu
hmotnost. Pro opravenou binomickou CDF platí obdobná beta identita
G(k)=Pr(Bin(t,p)≤k−1); monotonie plyne z monotónního poměru hustot.
Předpokládaná aproximace g musí mít |Z−Y|<ε s0<ε<1/2.
Potom interval chyby protne nejvýše jeden celý práh M a korekce
M−[F(X)<G(M)] je přesná. Mimo tento případ stačí floor(Y).
Při zásahu korekce leží Z ve vzdálenosti nejvýše2ε od celého čísla;
pro spojitý Z pravděpodobnost tohoto jevu jde k0 s ε→0.
To vysvětluje malý podíl korekcí při dostatečně dobré aproximaci.
Kniha zde dává princip pod výslovným předpokladem rychlé g, nikoli
konkrétní globální aproximační polynom. Žádná taková g, její
náročnost ani jednotná lineární aproximace nekonečných ocasů se
tímto auditem neprohlašuje za zkonstruovanou. U binomického zákona
vyžaduje normální aproximace velký rozptyl, nikoli jen velké t.

Úlohy23/25/26: obě konstrukce mají CDF2 arcsin(x)/π; OR/AND
rekurence dává21/32 a obecný dyadický zápis; Poissonův součet
plyne z PGF a rozdíl má pro μ2>0 kladnou pravděpodobnost záporného
výsledku. Výjimka μ2=0 je v původní odpovědi správně uvedená.

Úloha27: invariant počtu již menších a dosud nerozhodnutých
bitových proudů dokazuje B1–B3. Pro nekončící p je počet sloupců
maximum geometrických čekání; ocasový součet dává
`A_n=1+sum_(k=1)^n binom(n,k)(−1)^(k+1)/(2^k−1)` pro n≥1.
Exponenciální vytvořující funkce, Mellinův integrand
Γ(s)n^(−s)/(2^s−1), znaménka reziduí, periodický člen a zbytek
O(1/n) souhlasí. Přechod z exp(−nq) na(1−q)^n má součtovou
chybu O(1/n) podle odhadu n*q²*exp(−nq), q≤1/2.
Přímo přečteny také svazek3/2.vydání137 a636: A_n=1+V_(n+1)/(n+1)
a f0=−δ0 jsou správné. První vydání svazku3 není k dispozici;
pozdější změna označení sama nezakládá chybu svazku2 z1997.

Úloha28 má úplný důkaz globální obálky. Radiální plošný Jacobián
je J(y)=sqrt(yᵀA²y)/(yᵀAy)^((n+1)/2). Pro m=a_n, M=a_1
platí q≤(M+m)s−Mm a rovnost je dosažitelná směsí krajních os.
Minimalizace s^(n+1)/((M+m)s−Mm) dává přesně oba tištěné případy
K²; podmínka M≤nm je správná. Krajní numerické modely nenahrazují
tento obecný důkaz.

Úloha29: podmíněné maximum k uniformních bodů dává
X_k=X_(k+1)*U^(1/k); součin hustot se zkrátí na n! na seřazeném
simplexu. Inverzní monotónní transformace zachovává pořadí a zákon.
Poznámka o rychlosti třídění je výslovně nejistá a závisí na stroji;
není to tvrzení asymptotické dolní meze. Úloha30 je Poissonův proces
a míru zachovávající bitová mapa. Poissonova směs binomických počtů
v obdélníku má parametr μ krát jeho plocha. Konečná mřížka má
místo přesné plochy podíl svých bodů; toto omezení zůstává explicitní.

Úloha32: gamma součet a nezávislý uniformní poměr dokazují(a),
dva inverzní příspěvky s Jacobiánem1/2 dokazují(b).
Bijekce v(a) a dvojí násobnost v(b) se pro hustoty používají
skoro všude; na osách či diagonále jsou výjimky nulové míry.
U(c) mají všechny konečné množiny binárních cifer exponenciály
produktový zákon s Pr(bit_ℓ=1)=1/(1+exp(2^ℓ)). Prohazování
stejných bitových pozic proto zachová celý společný zákon.
Tištěné postupné j-flips není nutné chápat jako bodovou konvergenci
každého proudu; požadována je konvergence rozdělení. Produktový
důkaz přímo určuje zákon výsledného nekonečného proložení.

Úloha33: seedování dalšího generátoru dává praktickou deterministickou
funkci jednoho vstupu. Změna násobitele sama nedokazuje nezávislost.
Přesný ideální výklad má konstrukci nezávislých bitových proudů
na pozicích2^(i−1)(2j−1); konečný seed nemá nekonečnou entropii.

## Nálezy, errata a zdroje

**C0056:** původní588 má exponent n−x namísto t−x v beta integrálu.
Pro t=1,p=1/2,x=1 je správně1/2; libovolně přidané n=2 by dalo1/8.
Detail sazby znovu přímo přečten. Jediná změna parametru opraví
vzorec; low odpovídá lokálnímu tiskovému překlepu, nikoli selhání
celého kvantilového principu.

**C0057:** původní589 má A_m namísto A_n. A1=2 a A2=8/3
ukazují, že index nemůže být nezávislý. Rekurence, konečný součet,
asymptotika a generátor jsou správné. Závažnost low.

Všechny čtyři vrstvy errat a aktuální TeX byly znovu prohledány
podle stran136–142/587–590 a názvů zákonů, CDF, průměrů a iterací.
Oprava C0056 ani C0057 nebyla nalezena. Nejnovější fyzický dotisk
a prvenství zůstávají neověřené. Nová korespondence nevznikla.

X0122 odděluje známou opravu N2 z29.6.1999 (≥ a explicitní návrat),
přejmenování B→N z6.1.2011 a opravu jména v odpovědi29 z25.3.2006.
Bitové značky2005/2024, doplnění Find1997, odkaz7.1.3 z2006
a formulace integer-valued2009 jsou zkontrolované redakční změny,
nikoli další nové matematické nálezy. Vizuálně porovnány
all2-prepre8/33 a all2/3, včetně aktuálního TeXu k bitovým operacím.

Rychlá bibliografická kontrola ověřila metadata Ahrens–Dieter1980
na [stránce vydavatele](https://link.springer.com/article/10.1007/BF02241999)
a [institucionálním záznamu](https://tugraz.elsevierpure.com/de/publications/sampling-from-binomial-and-poisson-distributions-a-method-with-bo/).
Jde o alternativní odmítací konstrukci; přečten byl abstrakt, nikoli
placený plný text. Nepotvrzuje konstrukci g v knižním kvantilovém
návodu. [Záznam gamma článku1982](https://tugraz.elsevierpure.com/en/publications/generating-gamma-variates-by-a-modified-rejection-technique/)
potvrzuje autory, rok a47–54; přímý PDF pokus ACM vrátil403.
Tím se neuzavírá dobové časování na134.

Další bibliografické výjimky: osobní atribuce Ahrens/Léger/Brent/Wallace,
plný Tocher1954 a původní zdroje k Seneschalově prioritě a Bentley–Saxe
nebyly nezávisle auditovány. Neověřený experiment s α=7/8 zůstává
faktickou mezerou na137. Žádná stará simulace ani výpočet neběží.
