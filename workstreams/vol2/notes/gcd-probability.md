# §4.5.2: hustota nesoudělných dvojic a úlohy 10–14

Matematická část věty D na str. 342, zadání na 354 a odpovědi na 641
byly přečteny v originále. Výsledky jsou správné po zapracování známých
oprav z 18. února 2004 a nového znění úlohy 11 z 29. července 2024.
Historické podklady a skutečný rozsah jejich čtení jsou zaznamenány níže.

## Značení a význam pravděpodobnosti

U_n,V_n jsou nezávislá rovnoměrná kladná celá čísla z 1..n. Jejich gcd
označme D_n. „Náhodné celé číslo“ zde znamená limit tohoto konečného
modelu, nikoli rovnoměrnou míru na všech kladných celých číslech.
`q_n` je počet uspořádaných nesoudělných dvojic v tomto čtverci, q_0=0.
Möbiova funkce mu(d) je 0, pokud d obsahuje druhou mocninu prvočísla,
a jinak (-1)^r pro součin r různých prvočísel; mu(1)=1.
`zeta(s)=sum_{d>=1} d^(-s)` pro reálné s>1. Symbol O(h(n)) značí
veličinu omezenou konstantním násobkem h(n) pro dostatečně velké n.

## Úloha 10 a věta D

Inkluze a exkluze podle společných prvočíselných dělitelů dává přesně

```text
q_n = sum_{d<=n} mu(d) floor(n/d)^2.
```

Každá suma je konečná. Protože `|floor(x)^2-x^2|<=2x` pro x>=0,
chyba po nahrazení podlah je nejvýše `2n sum_{d<=n}1/d=O(n log(n+1))`.
Přidání ocasu za n stojí n² krát nejvýše `sum_{d>n}d^-2<=1/n`.
Tedy `q_n=n² sum_{d>=1}mu(d)/d²+O(n log(n+1))`.

Absolutní konvergence dovoluje násobit tuto řadu se zeta(2). Koeficient
u 1/m² je `sum_{d|m}mu(d)`: je 1 pro m=1 a pro m>1 je
`(1-1)^r=0`, kde r je počet různých prvočísel dělících m. Součin řad je
proto 1. Z `zeta(2)=pi²/6` vychází

```text
q_n = (6/pi²)n² + O(n log(n+1)),
Pr(D_n=1) -> 6/pi² = 0.6079271018540266...
```

Tentýž důkaz pro k>=2 souřadnic dává pravděpodobnost společného gcd=1
rovnou `1/zeta(k)`. „Relatively prime“ zde znamená společný gcd, nikoli
nesoudělnost každé dvojice. Pro k=1 je limit nuly třeba vyřídit přímo;
zeta(1) není konečné číslo.

## Známá oprava posunutých obdélníků

Původní dovětek odpovědi 10 připouští libovolné posuny f(m),g(n),
m<=n. To je příliš silné. Pro každý m zvolme m² navzájem různých
prvočísel p_(i,j), 0<=i,j<m. Čínská věta o zbytcích poskytne f,g takové,
že f+i i g+j jsou dělitelné p_(i,j). V celém m krát m obdélníku pak
není žádná nesoudělná dvojice. Hlavní člen řádu m² tedy nemůže mít
chybu jen O(m log m). Přesné konstrukce pro m=2..7 jsou ve výsledcích.

Erratum 2004 přidává f(m)=O(m),g(n)=O(n). Pro tyto posuny mají nenulové
hodnoty prvního argumentu velikost O(m), takže společné dělitele stačí
sčítat do K=O(m). Počet násobků d v intervalu délky m je m/d+O(1);
podobně n/d+O(1) v druhém intervalu. Součiny mají celkovou chybu
`O((m+n) sum_{d<=K}1/d+K)=O(n log m)` pro m rostoucí. Ocas hlavního
členu je O(mn/K)=O(n), pokud zvolíme K také alespoň m. Nulovou hodnotu
prvního argumentu lze vyřadit: pro gcd=1 přispěje nejvýše dvojicí hodnot
druhého argumentu ±1; v počtech násobků mění pouze O(1). Tak je zahrnut
i obor intervalů procházejících nulou. Oprava je dostačující; jde o
asymptotické tvrzení, ne o nulovou chybu pro m=1.

## Úloha 11: malé gcd a jeho střední hodnota

Pro pevné d platí přesně `Pr(D_n=d)=q_floor(n/d)/n²`. Proto
`Pr(D_n=d)->6/(pi² d²)` a

```text
Pr(D_n<=3) -> (6/pi²)(1+1/4+1/9)
            = 49/(6 pi²) = 0.8274563330790918...
```

Zde stačí konečný součet, bez výměny nekonečné sumy a limity. Pro
střední hodnotu použijeme nejprve jakýkoli pevný K:
`liminf E[D_n] >= (6/pi²) sum_{d<=K}1/d`. Pravá strana roste bez omezení
s K, a tak `E[D_n]->infinity`. Každý konečný n má samozřejmě konečný
průměr. O něco silněji, dosazením odhadu pro q do přesné identity
`E[D_n]=n^-2 sum_{d<=n} d*q_floor(n/d)` dostaneme
`E[D_n]=(6/pi²)ln n+O(1)`. Součet chyb je O(n²), protože
`sum_{d<=n} log(1+n/d)=O(n)`, například porovnáním s konečným integrálem
funkce log(1+1/x) na (0,1].

## Úloha 12: počet společných dělitelů

Označme tau(d) počet kladných dělitelů d; v odpovědi knihy je pro tuto
funkci použito sigma. Bodově `tau(D_n)=sum_{d>=1} [d|U_n a d|V_n]`,
kde hranatá závorka má hodnotu 1 při pravdivém tvrzení a 0 jinak. Tedy

```text
E[tau(D_n)] = sum_{d<=n} (floor(n/d)/n)^2 -> zeta(2)=pi²/6.
```

Každý člen je nejvýše 1/d², takže výměnu limity a sumy opravňuje
konvergentní dominující řada. Odpověď v knize je ekvivalentní:
`sum tau(d)/d²=zeta(2)^2`, jak plyne rozkladem d=ab.
Číselně je průměr 1.6449340668482264..., tedy méně než 2; pokud gcd>1,
počet dělitelů je opravdu vždy alespoň 2. Tyto výroky se nevylučují.

## Úloha 13: liché vstupy

Zvolme nyní U,V nezávisle rovnoměrně z prvních n kladných lichých čísel.
Pro liché d je podíl jeho násobků v této množině limitně 1/d; pro sudé
d je nula. Inkluze a exkluze dává limit

```text
sum_{d odd} mu(d)/d² = (1/zeta(2))/(1-1/4)
                     = 8/pi² = 0.8105694691387022...
```

Dominaci lze vzít jako 4/d²: pro d<=2n-1 je počet lichých násobků d
nejvýše n/d+1/2<=2n/d. Pro větší d je nula. To odůvodňuje nekonečný
součet bez předstírání nezávislosti nekonečně mnoha událostí.

## Úloha 14: logaritmus gcd

Pišme ln pro přirozený logaritmus a L pro limit E[ln D_n]. Identita

```text
ln D_n = sum_{p prime} (ln p) sum_{j>=1} [p^j divides both inputs]
```

a dominace konvergentní řadou `sum_{d>=2}(ln d)/d²` dávají

```text
L = sum_{p prime} ln(p)/(p²-1)
  = -zeta'(2)/zeta(2)
  = 0.5699609930945328...
```

Druhá rovnost plyne logaritmickým derivováním absolutně konvergentního
Eulerova součinu pro zeta v okolí s=2. Také přímo z rozdělení D_n dostaneme
`L=(6/pi²) sum_{d>=1} (ln d)/d²`: pravděpodobnost D_n=d je nejvýše 1/d²,
proto je výměna limity a sumy znovu oprávněná.

Pro liché vstupy chybí právě příspěvek p=2. Výsledek je
`L-ln(2)/3=0.3389119329078844...`, v souladu s knihou. Odpověď 14
v prvním dotisku má jmenovatel 2^p-1; známé erratum 2004 jej opravuje
na p²-1. Obě původně uvedené desetinné aproximace jsou již správné.

## Nezávislé konečné kontroly

`verify_gcd_probability.py --resume`, výsledky `results/gcd-probability.json`
a `.log`, relace 7933, exit 0. Přímé gcd histogramy pro čtverce do n=512
obsahují 262144 dvojic a 131328 kontrolovaných hodnot histogramů; byly
porovnány s Möbiovými součty, škálováním q_floor(n/d), součty počtů
dělitelů a identity pro průměr gcd. Dalších 65536 lichých dvojic prověřuje
lichou variantu. Šest CRT obdélníků dokládá známou chybu s posuny.
Číselné konstanty byly vyhodnoceny na 80 desetinných místech; nezávislý
prvočíselný součet do 10000 s analytickou horní mezí ocasu potvrzuje L.
Numerické vyhodnocení není zaměněno za intervalový certifikát všech 80 míst.

## Historické podklady

Mertensův článek *Ueber einige asymptotische Gesetze der Zahlentheorie*,
Crelle 77 (1874), má celý rozsah 289–338; citace knihy 289–291 míří na
příslušnou část a není chybná. V originálních obrázcích byly přečteny
všechny tři strany 289–291: definice phi a mu, součet phi přes podlahy,
vyhodnocení řady mu(d)/d² a explicitní chyba řádu G log G. Zde phi(n)
značí počet čísel z 1..n nesoudělných s n. Výsledek
`sum_{j<=G}phi(j)=(3/pi²)G²+O(G log G)` dává větu D přes přesnou
identitu `q_G=2 sum_{j<=G}phi(j)-1`. Mertens v úvodu výslovně připisuje
předchozí výsledek Dirichletovi 1849.
[Originální svazek GDZ](https://gdz.sub.uni-goettingen.de/id/PPN243919689_0077),
[bibliografický záznam článku](https://geodesic.mathdoc.fr/item/JRAM_1874__77_148241/).

Dirichletův článek *Über die Bestimmung der mittleren Werthe in der
Zahlentheorie* byl přečten v reprintu *Werke*, II (1897): titul na
str. 49, úvod na 51 a §6 na 60–64. Titul uvádí původní Abhandlungen
der Königlichen Akademie der Wissenschaften zu Berlin 1849, 69–83.
V §6 je odvozena stejná asymptotika součtu phi s chybou O(n^delta),
kde delta může být libovolné číslo nad kořenem gamma rovnice
`sum_{s>=2}s^(-gamma)=1`; lze zvolit delta<2. Závěr na str. 64 tak
opravňuje limit potřebný pro větu D. Převod na pravděpodobnost
nesoudělnosti pomocí uvedené identity je naše ekvivalentní formulace;
netvrdíme, že Dirichlet použil stejné pravděpodobnostní názvosloví.
Zbylé části článku nebyly celé auditovány.
[Primární PDF ETH/e-rara](https://www.e-rara.ch/download/pdf/5688101.pdf),
[katalog a DOI reprintu](https://doi.org/10.3931/e-rara-17606).

U Cesàrova článku o střední hodnotě gcd potvrzuje vydavatel autora,
rok 1885, *Annali di Matematica Pura ed Applicata* 13, 235–250 a DOI.
Vydavatelská stránka zpřístupnila pouze náhled pro předplatitele;
citované §3 a §12 proto nejsou vykázány jako přečtené. Matematické
výsledky 11/14 byly dokázány výše nezávisle. Absolutní historické
prvenství neověřujeme.
[Primární záznam vydavatele](https://link.springer.com/article/10.1007/BF02420800).

Zdrojové soubory, SHA-256, adresy a přesný rozsah čtení jsou v
`sources/gcd-probability-source-manifest.json`. Žádný nový nález;
známé opravy zůstávají odděleny od vlastních nálezů.
