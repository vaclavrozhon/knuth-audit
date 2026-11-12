# §1.2.11.3–18: převzetí Cauchyho původní identity

**Celá úloha 18 je checked.** K již přijatému důkazu v
`asymptotic-sums.md` přibyla kontrola přesné citované formule
a reziduální metody. Nový nález nevznikl.

Koordinátor ověřil 17 členů zmrazeného manifestu
`parallel/asymptotic-primary-followup/results/cauchy-ex18-manifest.json`,
jeho 17 přímých závislostí a devět vstupů knihy a úplných čtyř
vrstev errat. Manifest má SHA-256
`b825944f6e68c9d72081a8025a76c8ea780642d7881c86b2ebb15821b55f642b`.
Úplný sken Œuvres, řada II, svazek VI (1887), reprodukující
Exercices z roku 1826, byl identifikován už v předchozím převzetí.
Jeho data se neměnila.

Agent přímo přečetl celý citovaný rozsah 62–73. Koordinátor
nezávisle přímo přečetl 62–68 (PDF 72–78), zadání TAOCP s. 123
a odpověď s. 506. Tento rozdíl v rozsahu čtení se zachovává.
Původní s. 62–65 skutečně přecházejí od dvou postupných reziduí
k derivační identitě (16). Reziduum zde znamená koeficient
mocniny minus jedna v Laurentově rozvoji. Substituce na s. 66–67
a exponenciální funkce vedou k (21), pak přímo k (22) na s. 68.

Pro nezáporná celá n,j s j<=n pišme
`n_under(j)=n(n-1)...(n-j+1)`, s `n_under(0)=1`. Přejmenujeme-li
Cauchyho proměnné na xi,eta, jeho (22) přesně říká

```text
sum_(k=0)^n binom(n,k)(xi-k)^(n-k)(eta-n+k)^k
 = sum_(j=0)^n n_under(j)(xi+eta-n)^(n-j).
```

Dosazení `xi=Y+n`, `eta=X+n` dává knižní polynom
`H_n(X,Y)=sum_(k=0)^n binom(n,k)(X+k)^k(Y+n-k)^(n-k)`
a pravou stranu `sum_(j=0)^n binom(n,j)j!(X+Y+n)^(n-j)`.
Jde o polynomiální identitu; monom s nulovým exponentem je 1
i při nulové základně. Nevzniká omezení z dělení proměnnými.

Knižní `Q(n)=sum_(j=1)^n n_under(j)/n^j` je zde užita pro n>=1.
Dosazení X=Y=0 dává `n^n(1+Q(n))`. Pro X=1,Y=0 dává
`(n+1)^n Q(n+1)`: po posunu indexu v definici Q(n+1) je
koeficient `((n+1)_under(j+1))/(n+1)=n_under(j)`.
Obecnou identitu již nezávisle dokazuje přijatá Abelova rekurence
`H_n=(X+Y+n)^n+n H_(n-1)(X+1,Y)`, s H_0=1.

Všechny čtyři úplné vrstvy errat byly prohledány v agentově
`results/errata-search.json`. Koordinátor přímo zkontroloval
all1-prepre PDF 12/36, all1-pre PDF 16 a all1 PDF 7;
další dvě relevantní stránky přímo četl agent. Sousední opravy
odpovědí 11 a 20 se této identity ani citace netýkají.
Žádný dříve úspěšný matematický test se neopakoval.

Tento závěr nepotvrzuje obecnou správnost každého vedlejšího
Cauchyho vzorce pro libovolné funkce nebo komplexní větve.
Pokrývá celou knižní úlohu, její odpověď a konkrétní historickou
citaci. Přesný soupis je v
`results/cauchy-asymptotic-root-manifest.json`.
