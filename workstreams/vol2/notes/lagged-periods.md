# §3.2.1.2-22: velké moduly a periody generátorů s přenosem

Kontrola 1. listopadu 2026. Zadání na str. 23 žádá diskusi o dlouhých
periodách pro moduly b^k±b^l±1. Odpověď je na
[str. 549](../images/vol2-p549.png) a [550](../images/vol2-p550.png).
Obě původní stránky byly vizuálně přečteny. První dotisk skutečně uvádí
**30** konkrétních prvočísel při b=2^32; neúplný počet odhadnutý z OCR
se do inventáře výsledků nepřebírá. V erratech jsou jen jazykové opravy
„isn't feasible“ (3. 6. 2001) a „finding“ (13. 1. 1998).
Prověřeny all2-prepre, all2-pre, all2, err2 a originální err2.textxt.

## Co se dokazuje

Základ b je celé číslo >=2, k>l>0 jsou zpoždění generátoru a jeho
výstupy x_n jsou cifry 0 až b−1. **Perioda** je nejmenší kladná délka
opakování posloupnosti. **Řád b modulo m** je nejmenší kladné r
s b^r=1 mod m; zde je gcd(b,m)=1. Je-li m prvočíslo, maximální možný
řád je m−1. Zápis H_j(n) znamená číslo s j ciframi
(x_(n−1)...x_(n−j)) v základu b. Převod mezi výstupem a celočíselným
stavem X_n je dokázán v [poznámce o přenosu](carry-generators.md).

Kniha odděluje přesné číselné příklady od doporučení, jak vybrat
zpoždění a jak ředit výstupy. Dlouhá perioda není důkaz statistické
kvality. Úloha je diskusní, ne tvrzení o optimálnosti všech parametrů.

## Příklad Marsaglii a Zamana

Pro b=2^32−5 a m=b^43−b^22+1 ověřujeme prvočíselnost b i m a přesný
řád b rovný m−1. Jejich článek má DOI
[10.1214/aoap/1177005878](https://doi.org/10.1214/aoap/1177005878),
Annals of Applied Probability 1(3), 1991, str. 462–480; metadata vydavatele
jsou uložena přes Crossref v [souboru](../sources/marsaglia-zaman-1991-crossref.json).
Plný text se z veřejných adres Project Euclid nepodařilo získat
([záznam](../sources/marsaglia-zaman-1991-access.json)). Netvrdíme tedy,
že jsme v primárním článku přečetli jeho str. 474–475. Číselné tvrzení
v TAOCP ověřujeme vlastním důkazem a certifikáty.

Algebraický rozklad je

```
m−1 = b^22 (b−1) (b^6+b^5+...+b+1) (b^14+b^7+1).
```

[Program](../verify_lagged_periods.py) ověřil jeho rovnost i úplný
prvočíselný rozklad. Ten má **17 různých prvočíselných faktorů**,
největší má **99 desetinných číslic**, přesně jako v knize.
Úplná čísla a doklady jsou v [marsaglia-zaman-factors.json](../results/marsaglia-zaman-factors.json).
Faktorizaci navrhl PARI; důvěra v jeho faktorizaci není předpokladem:
součin kontroluje Python a každý faktor má samostatný certifikát prvočíselnosti.

Ověřeno b^(m−1)=1 modulo m a pro každý prvočíselný faktor q|m−1
dokonce gcd(b^((m−1)/q)−1,m)=1. Jakmile je m prvočíslo, tyto nerovnosti
dokazují řád m−1: každý vlastní dělitel m−1 dělí některé (m−1)/q.
Samotnou prvočíselnost m lze také odvodit už z faktoru b^22:
pro každé prvočíslo r|m musí řád b modulo r obsahovat celý faktor b^22,
neboť právě ten poslední test s q=b zkrátit nedovoluje. Proto b^22|r−1.
Ale b^44>m, takže r>sqrt(m), což u složeného m není možné.
Tento Pocklingtonův argument je vedle certifikátu m další doklad.

Pro daný generátor s výpůjčkou platí při počáteční výpůjčce c_0=0
X_0=H_43(0)−H_22(0). Rozepišme H_43=b^21 H_22+L, 0<=L<b^21.
Pak X_0=(b^21−1)H_22+L je 0 právě pro samé nulové cifry; jinak
1<=X_0<=b^43−b^22=m−1. Každá nenulová povolená inicializace tedy
má celočíselnou periodu m−1.

Výstupní cifry mají tutéž periodu, nejen její dělitel. Invariant je
b X_(n+1)=X_n+m x_n. Pokud by výstupy měly periodu d, rozdíly
D_n=X_(n+d)−X_n by splňovaly b D_(n+1)=D_n. Celé D_0 by pak bylo
dělitelné všemi mocninami b, tedy by bylo 0; stejně pro všechny n.
Perioda ciferné posloupnosti musí být periodou X. Opačná implikace plyne
ze vzorce pro x_n. Délka je řádu 10^414, jak uvádí kniha.

## Třicet velkých prvočísel

Transkripce originálu je v TABLE programu
[certify_lagged_primes.py](../certify_lagged_primes.py). Každý řádek
obsahuje k,l, znaménko u b^l, konstantu ±1 a autorovo slovní hodnocení
míchání. Je zde 14 doporučenějších a 16 méně doporučených variant.
Zvlášť byly zachovány snadno přehlédnutelné hodnoty k=73, k=93
a celá skupina b^k−b^l+1 u méně doporučených variant.

Pro všech 30 čísel a navíc m z předchozího oddílu vytváří PARI/GP
2.15.4 certifikáty metodou ECPP, tj. důkazy prvočíselnosti založené na
eliptických křivkách. [Dokumentace formátu](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Arithmetic_functions.html#primecert)
určuje význam položek certifikátu. Každý certifikát je trvale uložen
v `results/lagged-prime-certificates/`; výsledek konstrukce sám není
zaměněn za nezávislé ověření.

[Nezávislý validátor](../verify_ecpp.py) nepoužívá PARI ani knihovnu
eliptických křivek. Pro každý článek certifikátu pracuje s křivkou
y^2=x^3+a x+b modulo N. Eliptická křivka nad prvočíselným tělesem má
operaci sčítání bodů s neutrálním bodem O. Pomocí přesných celočíselných
operací validátor kontroluje diskriminant nesoudělný s N, inverzibilitu
všech použitých jmenovatelů a bod S s qS=O a S!=O modulo každé prvočíslo
dělící N. Číslo q už je dokázané prvočíslo z dalšího článku řetězce.

Stačí q>(N^(1/4)+1)^2. Pro prvočíslo r|N by řád S byl q a Hasseova
mez počtu bodů na křivce by dávala q<=(sqrt(r)+1)^2. Z toho r>sqrt(N),
takže N musí být prvočíslo. Hasseovu větu znovu nedokazujeme; validujeme
konkrétní certifikát na základě tohoto standardního kritéria.
Program používá bezpečně silnější celočíselnou mez s horním zaokrouhlením
čtvrté odmocniny. Všechny koncové prvočísla pod 2^64 prokazuje zvlášť
rekurzivními Lucasovými certifikáty: rozklad p−1, modulární mocniny a gcd.
SymPy pouze navrhuje rozklady, nerozhoduje o přijetí prvočíselnosti.

**Nezávislé ověření dokončeno:** všech 31 cílů a navíc 17 faktorů
velkého m−1 prošlo, celkem 2870 článků ECPP a 237 koncových Lucasových
certifikátů. [Úplný výsledek](../results/lagged-primes-validation.json)
a [finální log](../results/lagged-primes-validation.log) obsahují závěrečné
ALL 31. Součet všech uložených článků byl zvlášť porovnán s výsledkem.
Úloha 22 a tím celá §3.2.1.2 jsou uzavřeny.

Provozní poznámka: dodatečné převzetí ukončené tool session 35809
vrátilo 143. Netvrdíme tedy systémový exit 0. Úplný JSON se v kódu
vytváří až po všech kontrolách včetně faktorů a koncových certifikátů,
závěrečný log vzniká až po zápisu JSON; oba existují a proces již neběží.
Jde o doložené dokončení validace, nikoli úsudek z timeoutu.

Provozní detail reprodukce: první běh generátoru použil výchozích osm
vláken PARI. Nastavení parisizemax totiž zahodilo zbytek stejného vstupního
řádku, včetně požadavku nbthreads=1. Toto chování bylo samostatně ověřeno;
budoucí běh skriptu nastavuje nbthreads na novém řádku. Osvědčení ani
matematický obsah výsledků tato změna neovlivňuje.

## Čtyři desetinné příklady

[Přesný výsledek](../results/lagged-periods-small.json) obsahuje rozklady,
řády i rekurzivní prvočíselné certifikáty. Pro základ 10 platí:

| m | Rozklad | Řád 10 modulo m |
|---|---|---|
| 9999998999 | 439*22779041 | lcm(219,11389520)=2494304880 |
| 9999999001 | prvočíslo | 4999999500 |
| 10000000999 | prvočíslo | 5000000499 |
| 10000001001 | 3*17*2687*72973 | lcm(1,16,2686,12162)=130668528 |

U každého uvedeného řádu R se kontroluje 10^R=1 a 10^(R/q)!=1
pro každý prvočíselný dělitel q|R v příslušném modulu. Žádné z čísel
není přijato jen na základě pravděpodobnostního testu.

## Diskusní a statistická část

Algoritmus §4.5.4P, na který odpověď odkazuje, je pravděpodobnostní test;
v tomto auditu nenahrazuje certifikát prvočíselnosti. Speciální tvar modulu
umožňuje rychlou redukci pomocí mocnin b; podrobnosti algoritmu P patří
do pozdější systematické kontroly §4.5.4.

Částečné podíly řetězového zlomku l/k jsou celá čísla vznikající
Eukleidovým algoritmem při postupném dělení. Malé první podíly zde
slouží jako heuristika míchání. Kniha nedává kvantitativní definici
„prvních několika“ ani mez hodnoty „malé“; nevzniká zde přesná
optimalizační věta, kterou by bylo možné z této formulace vyvozovat.
Odkazy na narozeninový test (§3.3.2J) a Lüscherovo ředění (§3.2.2)
zůstávají v inventáři příslušných sekcí, nikoli jako už otestovaná
statistická kvalita zdejších generátorů.

Pravděpodobnost 1/q pro b^((m−1)/q)=1 má přesný smysl při rovnoměrné
volbě jednotky b v cyklické grupě modulo prvočíslo m. Zde jsou b a m
speciálně svázané; text používá tento model jako heuristické vodítko,
nikoli náhodný experiment s dokázanou distribucí. Závěrečné doporučení
k=1000,l=619,b=2^16 rovněž není tvrzením o prvočíselnosti ani konkrétní
periodě tohoto modulu. Pro složené m může nesoudělnost počátečního
stavu s m ovlivnit periodu; upozornění knihy je v souladu s §3.2.1.2B.

Rozsah uzavření: přesné příklady a jejich periody, logika navrženého
postupu a rozlišení důkazů od heuristik. Netvrdí se vyřešení faktorizace
m−1 pro všech 30 velkých modulů ani statistická nezávadnost všech výstupů.
