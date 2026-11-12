# §4.5.4: Lehmanova mez a historie Fermatova síta

Kontrola 3. listopadu 2026. Navazuje na matematiku algoritmů C/D
v [factoring-fermat.md](factoring-fermat.md). Uzavírá tvrzení o počtu
operací na str. 387 a historické odstavce na 386–391 v rozsahu níže.
Nový nález [C0152](C0152-sieve-rate-conversion.md): při uvedené rychlosti
hardwarového síta trvá 256 iterací přibližně 42 ns, nikoli 5.2 ns.

## 1. Proč stačí O(n^(1/3)) aritmetických operací

Myšlenka je hledat rozdíl čtverců pro několik malých násobků n.
Po odstranění malých prvočinitelů zůstane nejvýše součin dvou
prvočísel p,q. Vhodná racionální aproximace q/p zajistí, že některé
dvě hodnoty ap a bq budou blízko sebe; jejich součin je abn.
Proto pro k=ab najdeme čtverec x² těsně nad 4kn.

Počítáme aritmetické operace s celými čísly včetně celočíselné
odmocniny. Toto není počet bitových operací. Konstanty ani parity
v původním Lehmanově optimalizovaném programu zde nereprodukujeme;
dokazujeme přesně knižní řád nejhoršího případu.

Nechť n>=64 je liché. Položme mu=n^(1/3) a L=ceil(mu).
Čísla menší než 64 vyřešíme přímým dělením. Vyzkoušíme dělitele
do L a samostatně poznáme dokonalý čtverec. Pokud n je složené
a ještě jsme faktor nenašli, musí být

```
n=pq,   mu<p<q,
```

kde p,q jsou prvočísla: tři faktory větší než mu by měly součin
větší než n. Nyní položme Q=floor(p/mu)>=1.

Použijeme následující elementární aproximační lemma. Pro každé
reálné alpha a celé Q>=1 existují celá a,b s 1<=b<=Q a
`|b*alpha-a|<=1/(Q+1)`. Důkaz: seřaďme Q+1 zlomkových částí
0,alpha,...,Q*alpha na kružnici délky 1. Některá mezera je nejvýše
1/(Q+1); její krajní body dávají požadovaný rozdíl. Při shodných
bodech je chyba nula. Zahrnutí mezery přes nulu je podstatné.

Pro alpha=q/p dostaneme kladná a,b taková, že

```
y := |ap-bq| <= p/(Q+1) < mu.
k := ab <= (q/p)b² + b/(Q+1)
         <= (q/p)Q² + Q/(Q+1) < mu+1,
```

protože `(q/p)*(p/mu)^2=n/mu²=mu`. Tedy 1<=k<=L.
Dále b<p a `a<=q/mu+1/2<q`. Pro `x=ap+bq` máme

```
x²-y²=4kn,
0 <= x-2sqrt(kn) = y²/(x+2sqrt(kn))
                   < n^(1/6)/(4sqrt(k)).                    (L1)
```

Rozklad se získá z `gcd((x+y)/2,n)`, kde gcd označuje největšího
společného dělitele. Jeho hodnota je p nebo q, protože a<q a b<p.

Je tedy dostatečné projít k=1,...,L a všechna celá x v intervalu
(L1). Program používá o něco širší interval s přesnými celočíselnými
kraji:

```
A_k = ceil(sqrt(4kn)),
W_k = ceil(sqrt(L/(16k))),
x = A_k,...,A_k+W_k.                                        (L2)
```

Je-li `x²-4kn` čtverec y², získáme faktor jedním gcd. Tento test
nemá falešné úspěchy ani pro prvočísla. Opravdu, všechny zkoušené
hodnoty splňují x<n. Pro mu>=4 totiž

```
x < 2sqrt((mu+1)mu³)+2+sqrt(mu+1)/4
  <= sqrt(5)mu²+2+mu/4 < (5/2)mu² < mu³=n.
```

Ve druhé ostré nerovnosti jsme použili sqrt(5)<9/4 a
`2+mu/4<=mu²/4`. Z x²-y²=4kn plyne shodná parita x,y.
Celá čísla u=(x+y)/2 a v=(x-y)/2 jsou kladná, menší než n,
a uv=kn. Pokud by gcd(u,n)=1, muselo by n dělit v; pokud by gcd
bylo n, muselo by n dělit u. Obojí je nemožné. Pro prvočíslo n
tedy žádný takový čtverec neexistuje; pro složené n je gcd vlastní
dělitel. Po prvním čtverci můžeme skončit.

Počet testovaných x je nejvýše

```
sum_(k=1)^L (W_k+1)
 < 2L + sqrt(L)/4 * sum_(k=1)^L 1/sqrt(k)
 <= (5/2)L.                                                 (L3)
```

Použili jsme integrální odhad součtu nejvýše 2sqrt(L).
Každý test stojí konstantní počet aritmetických operací. Dělení
do L také stojí O(L); jediné gcd stojí O(log n), což se do O(L)
vejde. Výpočet L půlením intervalu stojí O(log n) a nic nemění.
To dokazuje požadovanou mez O(n^(1/3)).

Pokud chceme celý rozklad, při prvním průchodu dělitele do L
odstraňujeme včetně násobností. Dodatečných úspěšných dělení je
nejvýše log2(n). Zbytek je prvočíslo nebo součin dvou prvočísel
větších než původní L; jeden popsaný průchod jej rozloží.
Celková mez zůstává stejná.

## 2. Nezávislé konečné kontroly

`verify_factoring_lehman.py` počítá odmocniny a všechny kraje pouze
celočíselně. Konečný test je doplňkem obecného důkazu, nikoli jeho náhradou.

- Všech 99 999 vstupů 2<=n<=100000 bylo porovnáno s nezávislým
  Eratosthenovým sítem. Správně odlišeny prvočíslo a vlastní dělitel;
  5739 vstupů skutečně použilo druhou fázi Lehmanova hledání.
- Pro všech 42 914 vhodných dvojic různých lichých prvočísel
  p<q<=2000 byly nezávisle sestrojeny a,b z aproximačního lemmatu.
  Ověřeny všechny meze, identity, netriviálnost gcd a zahrnutí
  svědka do (L2). Největší Q bylo 12.
- U všech prvních vstupů platila i přesná mez (L3). Nejvyšší počet
  zkoušených čtverců byl 96, například pro n=99991.

Běh: obal PID 1266404, Python 1266405, session 19600, limit 120 s,
exit 0, 3.191155255 s. Dva dokončené kontrolní bloky jsou v
`results/factoring-lehman.json`; opakování nebylo zapotřebí.

Lehmanův původní článek, Math. Comp. 28 (1974), 637–646,
DOI 10.1090/S0025-5718-1974-0340163-2, se nepodařilo získat jako
čitelný lokální PDF: AMS 403, veřejné zrcadlo nedostupné, domnělá
cesta u Bernsteina 404. Bibliografii potvrzuje obsah původního čísla
[v archivu časopisu](https://www.jstor.org/stable/i334549).
OCR na neoficiální stránce bylo jen navigací. Původní důkaz ani jeho
Algol program proto neoznačujeme za přečtené; §1 dává vlastní úplný
důkaz tvrzení, které je skutečně uvedeno v Knuthově knize.

## 3. Fermat, Nārāyaṇa a Jevons

Dickson, *History of the Theory of Numbers*, svazek 1 (1919),
str. 357, byl zobrazen z původního skenu. Skutečně obsahuje anglický
překlad Fermatova postupu: zkoušení rozdílu čtverců přičítáním lichých
čísel, odmítání podle posledních číslic a následné určení faktorů.
Poznámka pod čarou odkazuje na fragment dopisu kolem roku 1643
a na náznak metody v dopisu z roku 1638. Knižní citace i rozlišení
Fermatova ručního postupu od algoritmu C jsou podložené.
Citovaný pozdější přetisk *Oeuvres* nebyl v tomto bloku znovu získán.

Známý dodatek z roku 2005 připomíná Nārāyaṇu (1356). Výklad
M. D. Srinivase v institucionálním kurzu NPTEL, přednáška 27,
obsahuje na snímcích 12–15 původní verše i jejich matematický výklad.
Po rozkladu N=a²+r se zkouší `(a+1)²-N`, poté se přičítají
2a+3,2a+5,... až do čtverce. To je týž faktorizující princip.
Příklady 1161=43*27 a 1001=77*13 s mezilehlými hodnotami sedí.
Datum kolem 1356 uvádějí snímky 3–4. Vizuálně přečteny snímky
1,3–4,12–15; celý sanskrtský rukopis ani moderní edici nepovažujeme
za samostatně přeložené či zkontrolované. Zdroj:
[NPTEL](https://archive.nptel.ac.in/content/storage2/courses/111101080/Downloads/27%20Ganitakaumudi%20III%20(MDS).pdf).

Jevons, *The Principles of Science* (Macmillan, 1874), svazek I,
str. 141, kapitola VII, byl ověřen v původním skenu včetně titulní
strany. Obsahuje citovanou výzvu s číslem 8616460799; kniha vypouští
pokračování za středníkem a sjednocuje „any one“ na „anyone“, což
nemění význam. Novější Gutenbergův přepis má jiné stránkování
i lehce upravený slovosled; neopírali jsme kontrolu vydání o něj.
Výpočet faktorů 89681*96079 byl ověřen již ve Fermatově bloku.
Odhad méně než deseti minut je ilustrativní tvrzení o ruční práci,
nikoli matematická mez; novým měřením lidského výkonu nebyl testován.

## 4. Síta a rozsah historických zdrojů

Lukesova disertace (1995) byla vizuálně přečtena v úsecích
10–18,23–24,30,38,41–42. Historická část dokládá Lawrenceův návrh,
Carissanův dokončený stroj z roku 1919 se 14 moduly, Lehmerovy
řetězové a fotoelektrické stroje i zpožďovací síto z roku 1965
s milionem čísel za sekundu. Tabulka na 24 datuje publikaci DLS-127
do 1966, zatímco vlastní text na 17 výslovně uvádí stavbu 1965;
nejde o protipříklad knižního roku zahájení provozu.

Hardwarová část primárně popisuje samotnou sestavu MSSU, kterou
Lukes vyvinul. Její parametry potvrzují knižních 6144 milionů/s,
ale vyvracejí následující převod na 5.2 ns: viz C0152.
Příbuzný článek Lukes–Patterson–Williams (1996) byl přečten pouze
na 361 a 366; jeho tabulky pseudočtverců zde přepočítány nejsou.
Původní citovaný článek týchž autorů v Nieuw Archief (1995),
113–139, byl potvrzen bibliograficky, nikoli přečten celý.

Williams–Shallit, *Factoring Integers Before Computers* (1994),
byl získán z autorova univerzitního webu. Vizuálně přečteny
481 a 520–529, včetně bibliografie: Lawrence28(1896),285–311
a Lehmer40(1933),401–406 sedí. Výsledky o pseudočtvercích na
520–524 nebyly tímto blokem nezávisle auditovány. Zbývající části
článku nebyly přečteny. Citaci Shallit–Williams–Morain17(3),41–47
a samotné znovunalezení Carissanova stroje potvrzuje také
[autorská stránka článku](https://cs.uwaterloo.ca/~shallit/Papers/carissan.html).
Historický přehled není nezávislým soupisem všech strojů v letech 1926–1989.

Wunderlichova citace JACM14(1967),10–19 byla ověřena v obsahu
časopisu vedeném ACM SIGMOD a MIT; plný článek nebyl dostupný
přes vydavatelský DOI (403). Tvrzení, že síta mají další použití,
je obecně správné: pro libovolné předepsané množiny zbytků se
stejným průnikem periodických bitových tabulek řeší soustava
kongruenčních podmínek. Není omezeno na test rozdílu čtverců.
Citace Lehmer–Lehmer, Math. Comp.28(1974),625–635 na začátku391
byla potvrzena v původním obsahu čísla; jejich další algoritmus
není v tomto odstavci specifikován, a proto zde není nový audit jeho důkazu.

Všechny čtyři relevantní vrstvy errat byly prohledány a známé
změny uplatněny. Nārāyaṇa je známý doplněk; C0152 je samostatný
nový rozpor v našem skenu. Nic nebylo odesláno ani publikováno.
