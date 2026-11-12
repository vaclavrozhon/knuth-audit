# Kořenové převzetí de Bruijna, Steffensena a Sekiho

2. listopadu 2026, X0691. Přijato samostatné zmrazené předání
`parallel/robson-tree-followup/HANDOFF-euler-primary.md`: 68 souborů,
45 673 499 bytů. Všechny kontrolní součty souhlasí; SHA-256 manifestu je
`e7e1f7b63c8a30ab063fcc636c4b39181c7eef67c1ae5c0bbd64b1b08d57223e`.
Podrobný soupis a přesný rozsah agenta zůstávají v jeho předání.
Kořenový manifest zaznamenává vlastní četbu a závislosti zvlášť.

## De Bruijn a konstanta A

Root přímo přečetl titul vydání 1958 a tištěné strany 40–42;
celý citovaný §3.7 je na s. 42. Institucionální kopie pochází
z Rice University, s původem a technickými podmínkami stažení
zapsanými v agentově logu. Pozdější vydání se tím nekolacionuje.

Označme `S(n)=sum(k log(k), k=1..n)`. Konstanta A v odpovědi
1.2.11.2-7 je určena asymptotikou součinu `exp(S(n))`.
De Bruijnova konstanta `C(z)` patří k součtu
`sum(k^(-z) log(k), k=1..n)` a má hodnotu
`C(z)=-(1-z)^(-2)-zeta'(z)`. Symbol `zeta'` znamená derivaci
Riemannovy funkce zeta. Pro `z=-1` platí

```text
integral(x log(x), x=1..n) = n^2 log(n)/2 - n^2/4 + 1/4,
C(-1) = -1/4 - zeta'(-1),
první korekce = (log(n)+1)/12.
```

Konstantní člen je tedy `log(A)=1/12-zeta'(-1)`. To přesně
odpovídá knižní normalizaci. Druhý knižní výraz pomocí `zeta'(2)`
není v §3.7 uveden doslova: potřebný přechod funkční rovnicí již
obsahuje přijatý důkaz P5 v `euler-products.md`. Tento rozdíl
nebrání věcné správnosti odkazu, ale je zachován v rozsahu četby.
Kniha s. 504 byla přímo porovnána; oprava krajního indexu z roku
2021 se shoduje s nynější normalizací. Úloha 7 je nově checked.

## Steffensen a znaménko zbytku

Root přímo přečetl titul a rub vydání Baltimore 1927, s. 129–133
a konec §14 na s. 138. Agent přečetl celý §14, tedy i s. 134–137;
tento dodatečný rozsah přebírám, nevydávám jej za vlastní četbu.
Knižní odpověď 1.2.11.2-3 na s. 503 byla přímo porovnána.

Pro sudé m označuje `B_m` Bernoulliho číslo, `P_m(x)` odpovídající
Bernoulliho polynom a `C_m` korekční člen řádu m v sumační formuli.
Zbytek po tomto členu označujeme `R_m`, podle kořenového důkazu E10.
Steffensenův integrál s jádrem `B_m-P_m({x})` je zbytek před
zahrnutím členu `C_m`; proto platí `R_(m-2)=C_m+R_m`.
Jeho rovnice (12) na s. 133 dává při pevném znaménku m-té derivace
interval pro `R_m` mezi `-C_m` a `(1-2^(1-m))*C_m`, právě jako E10.

Odstavec 149 na s. 133 výslovně požaduje stejné pevné znaménko
dvou sudých derivací, jejichž řády se liší o 2. Pak má zbytek
znaménko prvního nenulového vynechaného členu a menší velikost.
Posunem jeho `2r` na knižní `m+2` dostáváme přesně podmínku E11.
Steffensenovo `B_1=-1/2` nezmění použité sudé koeficienty ani
polynomy. Známá oprava roku 1937 na 1927 z 5. března 2013
je doložena titulem i rubem. Úloha 3 je nově checked.

## Seki: konkrétní obsah původního vydání

Root přímo porovnal kyótské obrazy 7, 26, 110 a 111 s předáním.
Na obr. 26 jsou u úrovní 2–12 pokyny odpovídající koeficientům
`1/2, 1/6, 0, -1/30, 0, 1/42, 0, -1/30, 0, 5/66, 0`.
V moderní indexaci jde o `B_1` až `B_11`; znak prázdného místa
se zde přepisuje nulou. První úroveň neinterpretuji jako `B_0=0`.
Na obr. 7 je první kniha a hlavička se Sekiho žáky, na obr. 110
úvod posmrtného doslovu a na obr. 111 tiráž s druhým rokem Shōtoku,
1712. Četba se omezuje na tyto identifikační, číselné a historické
údaje; úplný překlad starého japonského spisu nebyl proveden.

Původní tisk podporuje knižní datum a posmrtné vydání i kladné
`B_1` v dodatku 2021. Nejde o důkaz absolutní historické priority.
Agentův další rozsah včetně Ogawova výkladu je výslovně převzatý.
Vydání *Collected Works* 1974, s. 39–42, zůstává nepřečtené.
Katalogové Tokyo proti knižnímu Osaka bez tiráže nestačí k nálezu.

## Errata a otevřená citace Knuth–Vardi

Ověřeny hashe všech čtyř textových vrstev v agentově soupisu.
Root přímo četl all1-prepre PDF 11, all1-pre PDF 9 a 15:
atribuce Bernoulliho, konvence roku 2021 a rok Steffensenovy knihy.
Ostatní místní opravy a obecné důkazy již byly přijaty v dřívějších
blocích. Žádný nový nález; úspěšné matematické testy se neopakovaly.

Samostatné X0690 zaznamenává nové hledání původního řešení problému
6581 od Knutha a Vardiho. Knuthův autorský soupis Q106 potvrzuje
AMM 97 (1990), 629–630. Vardiho soupis a katalog časopisu nepřinesly
text řešení. Odkaz z OEIS vede na stejné známé JSTOR 2324649;
vrátil pouze technickou stránku bez článku. Ani DOI a nová cesta
přes ročník v Internet Archive původní článek nezpřístupnily.
Podrobnosti jsou v `sources/knuth-vardi-followup/read-scope.json`.
Matematika dyadických jmenovatelů je již prokázána, avšak tato
konkrétní citační mezera a úloha 9 zůstávají partial. Odlišný
rozsah stran v některých druhotných soupisech nebyl vyhodnocen
jako chyba bez původního článku.
