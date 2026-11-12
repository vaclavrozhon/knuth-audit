# Kořenová revize §2.3.4.6

1. listopadu 2026. Kořen přečetl celé předání, strojový inventář,
poznámky k pramenům, inventář errat a oba obecné matematické důkazy
v `parallel/tree-history/notes/`. Před převzetím ověřil všech
248 hashů zmrazeného manifestu. Úspěšné matematické testy se
neopakovaly. Rozsah přímého čtení pramenů podagentem zůstává
přesně vymezen v jeho `notes/sources.md`; převzetí není tvrzením
o druhém úplném čtení všech těchto pramenů.

## Obecné důkazy

Kořen ověřil bijekci triangulací s binárními stromy včetně
formálního prázdného základu. Pro Kirkmanovu formuli je počet
vrcholů příslušného rovinného stromu `N=r+k`: má `r-1` listů
a `k+1` vnitřních vrcholů. Rozdělení jejich stupňů a cyklické
lemma dávají oba binomické koeficienty a dělitel `N`.

U nekřížících se rozkladů je ověřena inverze kódu přes levé
a pravé odkazy, Narayanova čísla, příslušné svazy a dodatek
o rovinných rozkladech. Při převodu špatných binárních slov
se používá poslední globální minimum, inverzně první minimum.
Upřesnění čtení důkazu: jeho podslova označená jako „good“
v této části mají nezáporné prefixové součty; nemusejí mít
celkový součet nula. Toto se nesmí zaměnit s dříve definovaným
vyváženým Dyckovým slovem. Počet sousedních dvojic 01 se při
uvedeném převodu skutečně zachovává.

U vlysů je ověřena čtyřbodová identita indukcí, odvození
periodicity, mazání a vkládání ucha triangulace, interpretace
maticemi s determinantem 1, inverze slov L/R odečítáním
uspořádaných sloupců, znaménka kontinuantů a párovací
interpretace. V indukční míře `(w-t)m+u-t+w-v` je vedlejší
část nejvýše `w-t`; zmenšení hlavního rozpětí proto stačí.
Platnost těchto důkazů pro skutečné mnohoúhelníky `m>=3`
neodstraňuje následující chybějící kvalifikaci v knize.

## C0070: prázdný strom a jednorádkový vlys

Kořen přímo prohlédl originální 408, 599, 600 a 601.
Označme `n` počet uzlů binárního stromu a `m=n+2` parametr
řešení, tedy vlys má `m-1` kladných řad. Pro `n=0`, `m=2`
je celý vlys jediná řada jedniček; podmínka sousedních
kosočtverců je v původní jediné řadě prázdná. Řešení na599
výslovně pracuje se základem `m=2`, dvěma rovnoběžnými
hranami a identickou maticí. Nejde tedy pouze o svévolné
rozšíření mimo záměr řešení.

Na600 se připojují nulové řady 0 a m. U `m=2` je řada2
nulová, takže neobsahuje jedničku. Argument dokáže existenci
hodnoty menší než2, ale její kladnost v této krajní řadě
neplatí. Na601 je základní oblast
`0 <= u < v-1 < m-1`, s vynechanou dvojicí `(0,m-1)`.
Pro `m=2` nemá žádnou celočíselnou dvojici: oba počty
jsou0, nikoli `m-3=n-1=-1`.

Obě pomocná tvrzení stačí kvalifikovat `m>=3`, tedy `n>=1`.
Jednorádkový vlys se zpracuje zvlášť. Hlavní bijekce včetně
prázdného stromu zůstává správná. Podagent po nezávislé
revizi souhlasil a potvrdil, že jeho podmínka `m>=3` byla
doplněním důkazu, nikoli citací výslovného omezení v knize.

Čtyři vrstvy veřejných errat porovnány. Známé změny na408
a600 řeší konvexitu jiné úlohy, pořadí argumentů v důkazu
a rok publikace. Nové `n>0` na597 patří úloze3.
Výpis je v `results/frieze-boundary-errata.json`, anglický
návrh v `reports/V1-C0070-frieze-empty-tree.txt`.
Pozdější fyzické dotisky nebyly prohlédnuty, nic se neodeslalo.

Zmrazené předání původně uvádí žádný nový matematický nález;
tato kořenová revize jeho závěr doplňuje. Zmrazené soubory
se kvůli tomu neupravují. Pramenné mezery úlohy4 zůstávají
samostatně otevřené.

## Přesné mezisvazkové odkazy

Kořen přímo prohlédl originály Volume2 na357, 377 a653
(souborové369, 389, 665). Na357 je definice kontinuantů
s kladným znaménkem rekurence, na377 úloha4.5.3-32,
na653 její odpověď včetně obecnější Eulerovy identity.
Při substituci proměnných `x_j=i*a_j`, kde `i^2=-1`,
a přepisu pomocí `F(j,k)=i^{-(k-j-1)}K_{k-j-1}` se
znaménko druhého sčítance změní na minus: rozdíl celkových
stupňů je `2k+2` a `(-1)^k*i^{-(2k+2)}=-1`.
Výsledkem je právě čtyřbodová identita použitá v řešení
svazku1. Přesný cíl i význam odkazu tedy souhlasí.

Přímo prohlédnuty také originály Volume4A na473–476
(souborové490–493). Úlohy7.2.1.6-26 až34 skutečně tvoří
odkazované pokračování: Krewerasův, Tamariho a Stanleyho
svaz, jejich vztahy, asociédry, doplňkové prvky, semidistributivita,
permutační reprezentace a maximální řetězce. To potvrzuje
cíl dodatku z2017. Nejde o audit všech jejich důkazů ani
o převzetí sousedních svazků. Sedm originálních obrazů je
uloženo jako `images/tree-history-vol*.png`.

## Doplněk k citátu na422

Kořen převzal také přesný doklad původního pořadí slov
ve Wildeovi připisovaném aforismu; oba originály již přímo
porovnal. Dobový text1894 má „that nowadays“, kniha má
„nowadays / that“. Přímé čtení uzavírá otázku znění tohoto
konkrétního tisku, nikoli samostatnou atribuci nepodepsaného
článku nebo historii dalších autorizovaných přetisků.
Jako navrhované erratum tedy jde o C0072 candidate, ne o nový
potvrzený problém. Význam věty se přesunem slov zásadně nemění.
Podrobný původní doklad zůstává ve zmrazené poznámce
`parallel/tree-history/notes/wilde-quotation.md`.
