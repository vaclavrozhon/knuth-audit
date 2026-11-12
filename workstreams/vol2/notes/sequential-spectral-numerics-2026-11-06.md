# Souvislá revize: spektrální příklad a tabulka

6. listopadu 2026. Původní 103–109, zadání 8/11 na 115–116 a odpovědi
578–580 byly porovnány s uloženými důkazy, programy, výsledky a erraty.
Strana 110 byla zobrazena pro orientaci; navazující Fourierův důkaz zde
není uzavřen. Základ S má předchozí souvislou poznámku.

Přečteny celé `spectral_independent.py`, `verify_spectral_table.py`,
`verify_spectral_details.py`, `verify_waterman.py`, jejich dokončovací logy
a relevantní výsledkové bloky. Žádná stará enumerace se neopakovala.
Nový krátký validátor `verify_sequential_spectral_certificates.py` kontroluje
pouze uložené certifikáty a několik doplňujících modulárních svědků.
Výsledek: **145 certifikátů, 336 minimálních vektorů, 303 intervalů**, osm
svědků silnější kongruence RANDU. Běh s `nice -n 15`, exit 0,
0.240 sekundy podle vlastního časování. Nespouštěl LLL ani hledání mřížových bodů.

## Proč přijímáme numerické výsledky

Všechny parametry a vytištěné položky tabulky 106–107 byly znovu porovnány
s přepisem ve validačním programu, včetně znaménka rekurence řádku 25,
efektivních modulů a vynechávání kroků v řádcích 28/29. První metoda je
doslovné S; druhá používá jinou redukci a přesný průchod koulí.
Pro řádek 25, který není generátorem prvního řádu, se porovnává upravený
duální kvádr s koulí. Jeho duální báze má determinant p^2.

Nová kontrola ověřuje násobením uloženou změnu báze, její determinant ±1,
determinant nové báze, přesné Gramovy–Schmidtovy normy, normu každého
vráceného vektoru a příslušnou jednu či dvě kongruence. Samotný svědek
dokazuje pouze horní mez; dolní mez stále pochází z přezkoumané úplné
enumerace, nikoli z toho, že uložený vektor splňuje kongruenci.

V jejím kódu se větvení řídí identitou

```
||sum x_i B_i||^2 = sum d_k (x_k + sum_(j>k) mu_jk*x_j)^2.
```

Všechny normy a projekce jsou racionální. Pro střed A/B a zbývající
čtverec poloměru C/D se hranice získá z celočíselné nerovnosti
`(B*x-A)^2 <= C*B^2/D`; celočíselná odmocnina proto bezpečně zahrnuje
i rovnost na hranici. Přísnější dosavadní minimum může větve pouze
vyřadit, pokud už nemohou dosáhnout tohoto minima. Vlastní LLL pro velké
vstupy používá celočíselné zaokrouhlení; její kvalita není předpokladem
úplnosti následujícího průchodu koulí. Uložený nejtěžší tabulkový případ
má 46 navštívených souřadnicových uzlů.

Historický pád SymPy po části řádku 28 není úspěšným výsledkem. Log
zachovává následné dokončení zbývajících položek vlastní racionální
redukcí. Podobně časný limit desetimilionového kvádru RANDU nebyl
zaměněn za dolní mez: konečný výsledek nese přesná koule a nezávislé
srovnání PARI. Pilotní chybu continuantového validátoru opravuje podmínka
gcd(R,S)=1 před velkým soupisem; úspěšný dokončovací blok je přítomen.

Všechny přesné celočíselné tabulkové hodnoty souhlasí. Z 290 logaritmů
a skóre je původní známá chyba v řádku 25: lg(nu_4) je 14.6 místo 15.6.
Intervalová data ji již opravují. Nová kontrola ověřila, že všechny
uložené intervaly leží přísně uvnitř správných zaokrouhlovacích intervalů;
hodnoty funkcí se znovu nepřepočítávaly. Dalších 13 intervalů pokrývá
pět horních mezí, dvě odmocniny příkladu, RANDU mu_9 a pět skóre opravy 2004.

**C0042 zůstává candidate / low.** Řádek 29, nu_5^2, má přesně
`2.6503385745833175... * 10^165`, ale tisk uvádí `2 * 10^165`.
Běžné zaokrouhlení na jednu platnou cifru by bylo `3 * 10^165`.
Konvence velmi hrubých aproximací není určena; navazující lg(nu_5)=275
a mu_5=1.15 jsou správné. Nejde o doložené chybné mřížové minimum.

## Příklad 104, RANDU a úplné konečné soupisy

Šest eukleidovských kroků příkladu 103–104 a všech 15 průchodů S5
odpovídá vytištěné trase; ověřeny obě počáteční, první změněné i konečné
matice a z=(0,0,1). Výsledky jsou nu_2^2=4577114792 a
nu_3^2=1034718; vytištěné odmocniny mají správné zaokrouhlení.
Příklad a=464680339,m=2^29,t=5 zlepší mez 2398 na 2338 a řádek 21
v dimenzi 6 zlepší 1501 na 1438. Slovo „vzácně“ není oprávnění kvádr
vynechat; další doložená zlepšení jsou i v řádcích 26 a 29.
Historické autorství Carling/Levine 1982 nebylo nezávisle dohledáno.

U RANDU je nutné oddělit několik tvrzení. Uložená numerika s modulem
2^29 má minima 536936458,118,116,...,116 v dimenzích 2–9.
Pro t>=3 dává polynomialní identita `(a-3)^2 = 0 mod 2^31`
vytištěný krátký vztah; pro t>=4 lze použít vektor (-9,-3,5,-1)
a doplňovat nuly. V dimenzi 2 svědek (-16387,-16383) splňuje také
kongruenci modulo 2^30. Všechny doložené minimalizátory vybrané jako
svědci 2–9 mají tuto silnější vlastnost, kterou nový validátor ověřil.
Silnější mříž je podmnožinou slabší: nižší minima nemá a díky svědkům
nemá ani vyšší. **Hodnoty nu se proto nezmění.**

To samo neopravuje obecné tvrzení odpovědi 20 o m/4 ani neprokazuje,
že skutečná orbita vyplňuje jedinou posunutou mříž této hustoty.
Nález C0046 se přezkoumá s úlohou 20. Hodnota mu_9=11.98 je aritmeticky
správná při knižní normalizaci 2^29; nezaměňujeme ji s hodnotou, která
by vznikla normalizací celého afinního mřížového obalu hustoty 2^30.
Historické tvrzení 107 o většině světových výpočetních center a délce
používání RANDU není tímto numerickým blokem nezávisle doloženo.

Úplný starý continuantový soupis je přijat po kontrole jeho konečnosti:
rozdělí každý kanonický zlomek s podíly 1/2 za prvním prefixem P>sqrt(m).
Pro sousední Q a suffix R,S platí m=P*R+Q*S, gcd(R,S)=1, 1<=S<R;
prázdný suffix se řeší zvlášť. Rozsah R a kongruence modulo Q vyjmenují
všechny možnosti. Test na všech modulech 2–250 souhlasí s přímým výčtem.
Pro m=10^10 a a=1 mod20 bylo 407132 prefixů a 128879 suffixových
kandidátů, žádné řešení. Řádek 8 má 35 podílů a právě jeden je 3.
Tento již dokončený soupis se nerestartoval.

Oprava 2004 s a=2650845021,m=2^32 má doložená minima a skóre.
Její historické tvrzení o úplném hledání 2^30 násobitelů se znovu
nereprodukovalo, jak uživatel dovolil. Tabulková minima jednotlivých
násobitelů nejsou důkazem jejich globální optimality v celém prostoru.

## Úlohy 8 a 11

Vložením nulové souřadnice je nu_3<=nu_2. Vzorce (35)–(36) proto dávají
`mu_3 <= (4/3)*sqrt(m/pi)*mu_2^(3/2)`. Pro ilustrativní parametry
v zadání vychází `0.00007522527780636...`. Odpověď je platná horní mez;
nedokazuje dosažení rovnosti skutečným generátorem. Doslovně přesná
rovnost mu_2=10^-6 při m=10^10 by navíc vyžadovala celočíselné
nu_2^2=10000/pi, což není možné. Zadání zde čteme jako kvantitativní
odhad při přibližném skóre, ne jako přesně realizovatelnou diskrétní
optimalizační úlohu. Tento interpretační rozsah je zachován v evidenci;
nový potvrzený nález se z něj nevyvozuje. Známé opravy řádku 18→10
a odkazu (39)→(40) jsou zapracovány.

Watermanova konstrukce je správná v popsaném rozsahu. Pro m=2^e,
a=1 mod4 a primitivní y jsou obě souřadnice y liché. Substituce
y1=x1+x2, y2=x1-x2 dává nesoudělné x1 sudé a x2 liché,
`a=(x1+x2)/(x2-x1) mod m`; jmenovatel je invertibilní.
Rovnost `a-1=2*x1/(x2-x1) mod m` dává vztah ke zbytku x1 modulo4.
Primitivní reprezentace N=x1^2+x2^2 existují právě tehdy, když všechny
prvočinitele lichého N mají tvar 1 mod4. Gaussovský Eukleidův algoritmus
rozštěpí každý takový prvočinitel; aby řešení zůstalo primitivní, jeho
celá mocnina musí připadnout jedné z konjugovaných stran. Pro r různých
prvočinitelů a N>1 je po ztotožnění znamének a pořadí 2^(r-1) možností.

Starý program navíc nezávisle vyjmenoval sudé x1 a ověřil soupis
reprezentací přímo. Prvních 16 kandidátů končí přesně u
N=2479700521-68; všechny vytištěné faktorizace, reprezentace a násobitele
souhlasí. Invertovaný násobitel odpovídá změně znaménka a obrácení
souřadnic spektrálního vektoru, takže nevytváří jiné spektrální skóre.
„Best“ není vymezeno jednou cílovou funkcí: knižní a=1566083941 má
z těchto 16 největší mu_2; maximum nejmenšího ze skóre 2–6 má jiné a.
Žádný další kandidát jej nezlepší ve všech pěti skóre. Historickou
volbu proto neoznačujeme za prokázanou chybu ani za globální optimum.

**C0043 potvrzen, low.** Přímé násobení v odpovědi 11 dává

```
(7+2i)(2203+10202i) = -4983+75820i,
(7+2i)(2203-10202i) = 35825-67008i.
```

Použitelná imaginární část je u prvního součinu. „Former“ a „latter“
jsou prohozené; zápis s absolutními hodnotami navíc potřebuje volbu
znamének/jednotek. Následná hodnota a=4160984121 je správná. Pětinásobek
práce u desetinné varianty je heuristika dodatečné kongruence, nikoli
obecná dokázaná časová konstanta.

## Mřížová měřítka a periody

Objem elipsoidu 105 je objem t-koule dělený determinantem duální báze m.
Všechny vytištěné koeficienty pro t=2–6 i poločíselný faktoriál souhlasí.
Hranice „passes“ jsou autorova navržená kritéria, ne absolutní záruka
kvality generátoru. Tvrzení 105, že řádek 4 prošel mnoha empirickými
testy, nemá zde úplný seznam pokusů a není znovu doloženo.

**C0041 potvrzen, medium.** Dva vektory délky l s úhlem 60 stupňů
mají determinant l^2*sqrt(3)/2. Vytištěná délka `2/sqrt(3m)` na 109
dává `2/(sqrt(3)*m)`, místo požadovaného 1/m. Správně je
`sqrt(2/(sqrt(3)*m))`. Ve třech dimenzích mají uvedené řádky determinant
4v^3=1/m; jejich duální minimum je `1/(sqrt(2)*v)=2^(1/6)*m^(1/3)`.

Hermitovy konstanty (41) byly porovnány s čerstvě získaným autorským
článkem [Neumaier 2017](https://doi.org/10.1007/s10623-016-0273-9).
Přečtena definice na 240, úvod dodatku 256 a tabulka 1 na 257;
240 a 257 navíc vizuálně. Hodnoty gamma_t^t pro t=2–8 souhlasí:
4/3,2,4,8,64/3,64,256. Nejde o nový nezávislý důkaz optimality
v dimenzích 3–8; tabulka je použitý odborný doklad. Definice i
přepočet na konvenci knihy jsou zkontrolovány.

Primitivní kořeny řádků 17–19 byly nově doloženy krátkými modulárními
svědky pro všechny prvočinitele p-1. Řádky 20/21 již mají úplné
certifikáty řádů v `spectral-details.json`. Vytištěný násobitel (38)
splňuje obě CRT kongruence, gcd(p1-1,p2-1)=62 a společná perioda
je 74382023826798534. Platí také pro výstup Z, nejen pro dvojici stavů:
při nenulových seedech a periodě T výstupu máme modulo p1

```
(a1^T-1)*X_n = Y_(n+T)-Y_n.
```

Porovnání n a n+p2-1 zachová pravou stranu a změní X_n nenulovým
násobkem, protože a1^(p2-1) není 1 modulo p1. Musí tedy a1^T=1.
Potom Y_(n+T)=Y_n i jako celá čísla, neboť obě leží mezi 1 a p2-1<p1;
proto a2^T=1. T je násobkem obou period a jejich nejmenší společný
násobek skutečně nastává. Krátký nový svědek v certifikátu dokládá
potřebnou nerovnost mocniny. Nulové seedy by tvrzení změnily.

Pro rekurenci (39) má diskriminant charakter -1 a uložené mocniny
prvku x v kvadratickém tělese prokazují řád p^2-1 pro nenulový stav.
Řádek 27 odpovídá přesně vícecifernému stavu z dříve prověřené redukce;
28/29 používají b^(-389), resp. b^(-400), modulo b^r-b^s+1.
Skóre se netýkají přímo jednotlivých výstupních cifer, což kniha uvádí.

## Zdroje, omezení a pokračování

Z archivovaného Park–Miller 1988 znovu přečten odstavec o 23093
přenosných násobitelích a dvojici 48271/69621; ze zdroje L’Ecuyer 1988
parametry 40692/2147483399 a rozdílná druhá složka jeho vlastní
kombinace. Z Lüscherova preprintu znovu přečtena tabulka pro krok 389
a doporučení 223/389: řádek 28 knihy má stejných pět skóre.
Historické experimenty těchto autorů se nereprodukovaly.

Nedostupné osobní atribuce, přesný Marsagliův citát, datum nasazení
v IMSL a specifikace knihovny Cray zůstávají bibliografickými výjimkami.
Tvrzení o plošném rozšíření RANDU a úplnosti nevymezených empirických
testů jsou zvlášť otevřené faktické otázky. Globální historická hledání
nebyla restartována; jejich neprovedení je výslovně povolené.

Čtyři vrstvy errat i aktuální TeX znovu prohledány: zahrnuty změny
106 (2004), 107 (1998), 109 (2002), 115/578 (1999), 579 (2012).
Žádná nalezená položka neopravuje C0041/C0043 ani neurčuje konvenci C0042.
Nejnovější fyzický dotisk a prvenství nálezů nadále nejsou ověřeny.
Žádný email nevznikl ani nebyl odeslán.

Další blok: úlohy 16–24 a původní odpovědi 580–582, poté F/G od 109–110.
