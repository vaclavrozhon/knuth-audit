# SAT 351: lopsidependencies a resamplovací záznamy

Kontrola 31. 10. 2026. Definice v odpovědi 351 je správná.
Níže je obecný důkaz podmiňovací vlastnosti, záměny kroků a meze
Theorem K pro jednu událost. Odkaz na FKG na str. 273 zůstává
otázkou výkladu důkazu, nikoli potvrzenou chybou výsledku.

## Definice skutečně dává potřebné podmiňování

Pracujeme se součinovým rozdělením nezávislých proměnných. Hrana
A—B je povinná, jestliže existuje stav, v němž A platí, B neplatí
a změna proměnných A může způsobit B, nebo obráceně.

Nechť S je libovolná množina nesousedů A. Pro P(A)>0 vyberme X
z původního rozdělení podmíněného A. Nezávisle překreslíme všechny
proměnné A a získáme Y. Proměnné mimo A měly i po podmínění své
původní součinové rozdělení, takže Y má celé původní rozdělení.

Jestliže X nevyhovuje žádné události z S, nevyhovuje jim ani Y:
jinak by překreslení pravdivého A vytvořilo dosud nepravdivého
nesouseda, což definice zakazuje. Proto

`P(avoid S) ≥ P(avoid S | A)`.

Bayesovým vzorcem dostaneme `P(A | avoid S) ≤ P(A)`. Případ
P(A)=0 je okamžitý; nulový podmiňovací jmenovatel není omezením
na realizovatelné stavy. Argument platí i pro nesymetrická a
degenerovaná rozdělení jednotlivých proměnných.

## Dva nesousední kroky lze zaměnit na stejné náhodné tabulce

Každá proměnná má vlastní předem vylosovanou posloupnost hodnot.
Resamplování posune její ukazatel o jeden. Uvažujme dva různé
nesousední štítky A a B a legální záznam AB.

Rozdělme proměnné na soukromé pro A, společné a soukromé pro B.
Počáteční hodnoty označme (a₀,s₀,b₀), první nové hodnoty
(a₁,s₁,b₁). Legálnost AB říká

`A(a₀,s₀)=1` a `B(s₁,b₀)=1`.

Musí také platit B(s₀,b₀)=1: opačný případ by vytvořil B
překreslením pravdivého A. A musí platit A(a₀,s₁)=1: jinak
by ve stavu (a₀,s₁,b₀) bylo B pravdivé a A nepravdivé, přičemž
překreslení B zpět na s₀ by A vytvořilo. To by rovněž vyžadovalo
hranu. Tím je legální i BA. Obrácená implikace je symetrická.

Po obou pořadích jsou konečné hodnoty (a₁,s₂,b₁), ukazatele
stejné. Tvrzení platí i při prázdném průniku proměnných a při
identických událostech s různými štítky.

## Pravděpodobnost pevného slova a jeho stopy

Pro pevné slovo A₁…Aₖ kontrolujeme, že aktuální událost platí,
a pak překreslíme všechny její proměnné. Žádnou buňku náhodné
tabulky nemohou číst dvě kontroly: po prvním čtení se ukazatel
dané proměnné posune. Testy tedy používají disjunktní nezávislé
buňky a pravděpodobnost legálnosti je přesně `Πᵢ P(Aᵢ)`.

Záměnou sousedních nesousedních štítků dostáváme všechna slova
téže stopy. Podle předchozího důkazu mají na pevné tabulce stejnou
legálnost, takže sjednocení přes reprezentanty nepřidává faktor
rovný jejich počtu. Jakákoli konkrétní strategie Algorithm M
může danou stopu vytvořit jen na těchto tabulkách. Proto má její
výskyt pravděpodobnost nejvýše součin pravděpodobností událostí.

## Theorem K přímo přes pyramidy

U každého výskytu štítku j v záznamu vezmeme jeho hlavní ideál
v uspořádání stopy: tento výskyt a všechny jeho předchůdce.
Vznikne pyramida s jediným maximem j. Zbytek předchozího záznamu
lze záměnami odsunout za ni, takže pyramida musí být legální na
původní náhodné tabulce. Její pravděpodobnost je nejvýše její
váha. Různé výskyty j dávají různé pyramidy, protože obsahují
postupně 1, 2, … výskytů j.

Označme H_G=1/M_G součet vah všech stop a P_j součet vah pyramid
s maximem j. Ke každé stopě připojíme j. Hlavní ideál tohoto j
je pyramida a zbytek obsahuje pouze štítky mimo uzavřené okolí j.
Rozklad je jednoznačný a vratný: j lze přes zbytek přesunout až
na konec. Proto

`p_j H_G = P_j H_(G\Γ⁺(j))`,

a tedy

`P_j = p_j M_(G\Γ⁺(j)) / M_G = E_j`.

Pro p∈R(G) tyto řady konvergují. Linearita střední hodnoty a
součinová mez pro jednotlivé pyramidy dávají `E N_j ≤ E_j`,
přesně jako (152). Není nutné předpokládat, že každé abstraktní
krajní rozdělení je realizováno konkrétními booleovskými proměnnými.

Dokonce dostaneme geometrickou mez na ocas N_j. Po označení
výskytů j proměnnou t je součet pyramid

`P_j(t)=t p_j M_(G\Γ⁺(j)) / (M_(G\j)−t p_j M_(G\Γ⁺(j)))`
`       = ρt/(1−ρt)`,

kde `ρ=p_j M_(G\Γ⁺(j))/M_(G\j)<1`. Pyramida k-tého výskytu
obsahuje právě k štítků j. Součtem jejich vah získáme
`P(N_j≥k)≤ρ^k`. Toto ověřuje tvrzení o počtu oprav jedné
události i jeho střední hodnotě; samostatné tvrzení o stochastické
dominanci celkového počtu kroků zde nedokazujeme.

## FKG na str. 273: C009, pouze nejasnost důkazu

Text správně říká, že nesousední události jsou pozitivně
korelované. To plyne už z podmiňovací nerovnosti výše. Samotná
pozitivní korelace však dává dolní, nikoli horní součinovou mez
pro společný výskyt. U dvou identických událostí daných jedním
férovým bitem je společná pravděpodobnost 1/2, součin 1/4.
Pravděpodobnost legálního resamplovacího slova AB je přesto 1/4,
protože mezi kontrolami dostane bit novou hodnotu.

Větě o horní mezi tedy rozumíme přes časový záznam a záměny,
nikoli jako mezi pro současný výskyt původních událostí. Pouhý
odkaz na FKG tento přechod nevysvětluje. Protože samotný výsledek
je správný a text explicitně netiskne nepravdivou mez pro současné
události, C009 není mezi potvrzenými nálezy a nemá návrh hlášení.
Znění je stejné ve vizuálně prohlédnutém PDF str. 273 a autorově
PS str. 89. Oprava nebyla nalezena v all4b ani all4f6.

## Nezávislá konečná kontrola a primární zdroj

`check_lopsidependencies.py` pracuje s obecnými pravdivostními
tabulkami, nikoli jen s klauzulemi. Skutečné podpory odvodí z
funkcí. Ověřil:

- všech 33 042 neuspořádaných dvojic událostí na 1–3 bitech;
- 1 071 nesousedních dvojic, jejich pozitivní korelaci a přesnou
  pravděpodobnost dvoukrokového slova;
- 518 280 tabulek náhodných hodnot pro záměnu AB↔BA, včetně
  shody konečných hodnot i pozic ukazatelů;
- 3 448 podmiňování na vyhnutí dvěma nesousedům při čtyřech
  součinových rozděleních, včetně nulových pravděpodobností;
- 27 třípísmenných slov a 13 824 tabulek pro tři překrývající se
  konjunkce, včetně opakovaných štítků.

Všechny kontroly prošly. Jsou kontrolou implementace argumentu,
obecné závěry vycházejí z důkazů uvedených výše.

Primární článek: Robin A. Moser, Gábor Tardos,
[A constructive proof of the general Lovász Local Lemma](https://arxiv.org/abs/0903.0544),
§6, zejména Lemma 6.2. Jeho definice je ekvivalentní odpovědi 351:
změny mimo průnik podpor nemohou ovlivnit druhou událost.
Také článek dokazuje legálnost záměn na pevných náhodných
posloupnostech. PDF, text a hash jsou uloženy v `sources/`.
