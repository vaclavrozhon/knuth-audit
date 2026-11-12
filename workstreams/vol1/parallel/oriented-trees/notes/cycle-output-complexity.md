# Odpověď §2.3.4.2-11: časové meze nezahrnují délku výstupu

Stav: `candidate` před nezávislou kořenovou revizí. Popisný štítek
`fundamental-cycle-output-complexity`; globální ID zde nepřiděluji.
Podklad: TAOCP 1, vydání 3, dotisk 1 (1997), úloha na s. 377, odpověď na
s. 581. Původní obrazy obou stran a podpůrné s. 576 byly zobrazeny.
Fyzický výtisk kontrolován nebyl. Správnost nalezené kostry a cyklů není
zpochybněna; problém je ve dvou tvrzených časových mezích poznámky.

## 1. Přesný kontrakt a tvrzení

Úloha žádá algoritmus, který vedle kostry také „prints out the fundamental
cycles“. Knižní C5 vytiskne `CYCLE` a vstupní oblouk `(a,b)`. Krok C6 pak
jde po řetězu rodičů z b do a a za každou navštívenou stromovou hranu
vytiskne její uspořádané konce se znaménkem určeným tabulkou S. Jde tedy
výslovně o jednotlivý výpis všech hran každého cyklu.

Bezprostřední poznámka na s. 581 tvrdí:

> This algorithm will take at most O(m log n) steps if we incorporate the
> suggestion of McIlroy in answer 2.3.3-10.

Následuje tvrzení o řešení v O(m) krocích pomocí prohledávání do hloubky,
„palm tree“ a jednoho fundamentálního cyklu za každou nestromovou hranu
(„frond“). Zde n znamená počet vrcholů a m počet vstupních oblouků. Zápis
jedné hrany stojí alespoň jeden krok i ve standardním modelu, který umí
zapsat libovolné číslo vrcholu v konstantním čase.

## 2. Protipříklad k O(m log n)

Pro každé n≥4 dejme na vstup postupně oblouky

```
(1,2), (2,3), ..., (n-1,n),
(1,3), (1,4), ..., (1,n).
```

Je jich `m=2n-3`. Každá z prvních n−1 hran spojuje dvě různé komponenty,
takže algoritmus přijme přesně cestu `1—2—...—n`. Všechny pozdější oblouky
se odmítnou jako nestromové. Přeorientování stromu mění pouze rodiče, nikoli
tuto přijatou množinu hran. Fundamentální cyklus oblouku `(1,k)` má k hran:
oblouk `(1,k)` a k−1 hran cesty z k zpět do 1. Celkem se proto vytiskne

```
L = sum_{k=3}^n k = n(n+1)/2 - 3
```

hran v cyklech, navíc k již vytištěné kostře. Čas je alespoň Ω(n²), zatímco
`m log n = Θ(n log n)`. To platí pro všechny n této rodiny, nejde o úsudek
z konečného časového měření.

Odkazovaná McIlroyova úprava na s. 576 připojuje menší komponentu pod větší
v pomocné struktuře pro ekvivalence. Může zkrátit dotazy na souvislost,
ale nemůže zkrátit explicitně požadovaný výstup. Její rodičovské odkazy
navíc nemusejí být původními hranami grafu, zatímco C1–C6 právě tento invariant
potřebuje. Nález se netýká správnosti McIlroyovy úpravy v její původní úloze.

## 3. Stejný řídký graf a libovolná DFS kostra

**DFS kostra** je strom hran, jimiž prohledávání do hloubky poprvé objeví
vrcholy; „fundamentální cyklus“ nestromové hrany je tato hrana spolu
s jedinou cestou mezi jejími konci ve stromu. Podkladový graf výše je vějíř:
vrchol 1 sousedí se všemi ostatními a vrcholy 2,…,n tvoří cestu.

Tvrdím, že vrchol 1 má v libovolné DFS kostře T stupeň nejvýše tři.
Před prvním dosažením 1 vede zásobníková cesta DFS jen po cestě 2,…,n;
její vrcholy tvoří souvislý interval této cesty. Po odstranění tohoto
intervalu zbývají nejvýše dvě dosud nenavštívené souvislé části. První
rekurzivní volání z 1 do kterékoli takové části ji navštíví celou, protože
je to cesta a žádný další neznámý vrchol neleží mimo ni. Vrchol 1 proto má
nejvýše dva syny a jednoho rodiče. Jestliže je 1 počátečním kořenem DFS,
má dokonce jediného syna. Argument nezávisí na pořadí sousedů ani na
počátečním vrcholu.

Po odstranění 1 ze stromu T tedy zbývá nejvýše tři komponenty, každá cesta
o velikosti s_i, a každá je připojena k 1 právě v jednom svém vrcholu.
Pro cestu o s vrcholech připojenou v pozici a je součet vzdáleností od 1

```
s + sum_{j=1}^s |j-a| >= s + (s²-1)/4 >= s²/4.
```

Jelikož součet s_i je n−1, Cauchyova nerovnost dává

```
sum_{v=2}^n distance_T(1,v) >= (n-1)²/12.
```

Nejvýše tři hrany `(1,v)` leží v T; jejich vzdálenost je 1. Všechny ostatní
hrany `(1,v)` jsou nestromové a jejich fundamentální cykly mají délku
`1+distance_T(1,v)`. Samotné tyto cykly tedy mají celkovou délku alespoň
`(n-1)²/12 + (n-1) - 6 = Ω(n²)`. Ani pečlivá volba DFS kořene a pořadí
sousedů tedy na této rodině nedovolí explicitní výpis v O(m).

To **netvrdí**, že každá cyklová báze tohoto grafu má kvadratickou délku.
Například hvězdová kostra dává krátké trojúhelníky, ale není DFS kostrou
tohoto vějíře. Tvrzení je přesně o původním algoritmu a o navržené DFS variantě.

## 4. Primární Tarjanův text a oprava

Získán [Tarjanův původní článek](https://www.cs.cmu.edu/~cdm/resources/Tarjan1972-sccs.pdf),
lokálně `../sources/tarjan-1972.pdf/.txt`, DOI 10.1137/0201010.
Přečteno citované rozpětí 146–150, včetně celého §2 a Theorem 1;
prohlédnuty originální strany 148 a 150. Program na s. 148 vytváří každou
hranu stromu či „frond“ jednou a netiskne její cyklus po jednotlivých
hranách. Jeho lineární mez je správná pro tento kompaktní výstup.
Rozpětí 146–150 v TAOCP přesně pokrývá relevantní část většího článku
146–160, takže jeho zkrácení není další bibliografický nález.

Oprava má výslovně odlišit dvě podoby výsledku. DFS vytvoří kostru
a seznam nestromových hran v čase O(n+m); dvojice konců nestromové hrany
spolu s uloženou kostrou určuje cyklus implicitně. Chceme-li všechny
tyto cykly vypsat po hranách, potřebujeme a stačí `O(n+m+L)`, kde L je
součet jejich délek. U souvislých grafů s aspoň dvěma vrcholy lze n
v této mezi pohltit do m. Původní tvrzení O(m log n) pro C1–C6 je třeba
odstranit nebo formulovat pro jiný, přesně vymezený kontrakt.

## 5. Errata

K 1. 11. 2026 prohledány všechny textové vrstvy
`errata/text/{all1-prepre,all1-pre,all1,err1}.txt` podle s. 377, 576, 581
a podle cycle, fundamental, McIlroy/Mcllroy, Tarjan, palm, log n.
Relevantní původní obrazy všech vrstev byly prohlédnuty: all1-prepre
25, 26, 43, 44; all1-pre 13; all1 10; err1 8, 9. Jsou v `../images/`.
Na s. 377 se opravují F→P v úloze 10 a terminologie úlohy 14. Na s. 581
se opravují odpovědi 15–17; žádná vrstva nemění poznámku odpovědi 11,
její výstupní kontrakt ani uvedené časové meze. Obecné změny
path/walk a circuit/trail se problému netýkají. Aktuálnost těchto vrstev
ve stejný den ověřil kořen.

## English ASCII draft

Page 581, answer 2.3.4.2-11, Note: The stated time bounds do not account
for explicitly printing the fundamental cycles, as steps C5 and C6 require.
Feed the algorithm the arcs (1,2),(2,3),...,(n-1,n), followed by
(1,3),(1,4),...,(1,n). There are m=2n-3 input arcs. The accepted spanning
tree is the path, and the subsequently printed cycles have lengths
3,4,...,n. Their total length is n(n+1)/2-3, precluding an O(m log n)
bound regardless of union-by-size bookkeeping.

The DFS alternative also needs an output-length qualification. It can
construct a spanning tree and the list of non-tree arcs in O(n+m) time,
implicitly representing the cycles. Explicitly printing the resulting
cycles takes O(n+m+L) time, where L is their total length. In fact, on
the same fan graph every DFS spanning tree yields L=Omega(n^2), although
m=O(n). The cited Tarjan algorithm constructs the compact palm tree;
it does not print every arc of each fundamental cycle.
