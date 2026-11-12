# V1-X0784: Dickmanův původní výpočet konstanty

Původní Dickman1930 přímo dokládá historický výrok na TAOCP525:
stejnou konstantu vypočítal v souvislosti s největším prvočíselným
dělitelem. Tato část §1.3.3–23 je checked. Mitchellovo vyčíslení
a přesná časopisecká strana Knuth–Trabb Pardo jsou samostatné body.

Root přečetl celý předaný důkaz převodu značení, stav a přístupové
údaje. Ověřil39souborů a8přímých závislostí manifestu
`parallel/permutation-cycle-originals/results/dickman1930-manifest.json`,
SHA-256 `df4bc531c1fc09f5515583aeec4d8cb9c02b6b4d823073891fdf2dda16d2f910`,
a navíc všech14vstupů v přiloženém `results/readonly-inputs.json`.
Celý získaný svazek knihovny Iași má696stran a SHA-256
`58992e72d7337271e30ae2cb2749c158f628e30cf54831871a41a6d367d861a9`.
Institucionální záznam: https://dspace.bcu-iasi.ro/handle/123456789/43798.

Agent přímo četl všech14stran článku, PDF199–212. Root zvlášť
přečetl titul a definici na1, rekurenci na6, definici průměrované
veličiny v dolní části8, celé odvození a tabulku9, úvod10 před
částíII, tiskové datum v patičce14 a seznam vydání sešitů naPDF6.
Zbytek tabulek na8/14 byl zobrazen, ale root ho nezávisle
nepřepočítával; další články svazku nebyly auditovány.

Titul uvádí Arkiv22A, číslo10, a sdělení12.března1930. Patička
uvádí tisk25.července1930, seznam vydání publikaci sešitu sA9–A16
dne11.prosince1930. Tato data nejsou zaměňována; titulní rozsah
svazku1930–1932 nevyvrací datum citovaného článku1930.

Nechť P(t) označuje největší prvočíselný dělitel čísla t>=2.
Dickmanova f(a) je limitní podíl čísel s P(t)>t^a. Její původní
rekurence po intervalech 1/(n+1)<=a<1/n se s f(a)=0 pro a>=1
zapisuje jednotně

```text
f(a) = integral_a^1 [1-f(y/(1-y))] dy/y.
```

Strany8–9 průměrují log(P(t))/log(t) a dostávají
`mu=integral_0^1 [1-f(y/(1-y))] dy`. V tabulce9 je součet
0,62432998; úvod10 jej shrnuje přibližně jako0,62433000.
Je tedy doložen skutečný výpočet, nikoli jen podobná definice.
Tyto dobové desetinné aproximace nevydáváme za osmimístný
intervalový certifikát; TAOCP jim takovou přesnost nepřipisuje.

Definujme rho(u)=1 pro0<=u<=1 a rho(u)=1-f(1/u) pro u>1.
Derivace rekurence na každém příslušném intervalu dává

```text
rho'(u) = f'(1/u)/u² = -rho(u-1)/u.
```

Počáteční úsek a tato rovnice jednoznačně určují spojitou rho:
na každém následujícím jednotkovém intervalu integrujeme již
známou pravou stranu. S R(Y)=rho(Y-1) a substitucí u=(1-y)/y
tedy dostaneme přesně

```text
mu = integral_0^infinity rho(u)/(1+u)² du
   = integral_1^infinity R(Y)/Y² dY = lambda.
```

Poslední reprezentace lambda, konstanty pro očekávanou délku
nejdelšího permutačního cyklu dělenou počtem prvků, je již přijata
ze Stanfordského reportu Knutha a Trabb Parda. Substituce i derivace
byly kořenově zkontrolovány; numerická shoda není jejich důkazem.
Konvergence plyne z0<=rho<=1. Netvrdíme zde nový úplný moderní
důkaz všech Dickmanových přechodů od prvočíselných hustot k integrálům.

Root přímo přečetl TAOCP525 a relevantní all1-prepre38 a all1-14.
Paket obsahuje prohledání všech čtyř vrstev errat. Známé změny
Gourdon2003 a373→343 z10.listopadu2022 jsou zachovány; Dickmanovu
citaci nemění. Fyzický výtisk TAOCP neověřen. Nový nález nevznikl,
staré matematické testy se neopakovaly a celá23zatím zůstává partial.
