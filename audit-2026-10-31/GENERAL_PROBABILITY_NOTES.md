# Obecné pravděpodobnostní nerovnosti

## 59 a 61: four functions theorem a FKG

Základní čtyřfunkční nerovnost 59(a) se redukuje na smíšené členy.
Vynásobením jejich požadovaného rozdílu `c₀d₁+c₁d₀−a₀b₁−a₁b₀`
číslem `c₁d₀` dostaneme součet dvou nezáporných výrazů uvedený v knize.
Je-li násobitel nulový, oba smíšené členy vlevo jsou nulové a výsledek
platí přímo. Oba příklady rovnosti a ostré nerovnosti v odpovědi souhlasí.
Zkontrolováno také všech 17 788 přípustných osmiprvkových vektorů
s celočíselnými hodnotami od 0 do 3.

Pro konečný počet bitů rozdělíme indexy podle posledního bitu a na každou
ze čtyř dvojic použijeme indukční předpoklad. Tím vzniknou právě čtyři
nerovnosti potřebné pro základní dvouprvkový případ. Nekonečná verze
plyne monotónní limitou součtů s indexy menšími než `2^n`; všechny
sčítance jsou nezáporné, takže nevzniká problém podmíněné konvergence.

FKG pro nezáporné rostoucí f,g je přímé dosazení
`α=fμ`, `β=gμ`, `γ=fgμ`, `δ=μ` do čtyřfunkční nerovnosti.
Obecné konečné reálné f,g posuneme o jejich minimum; kovariance se
nezmění. Obrácené monotonicity získáme změnami znamének.

Lokální kritérium 61(c) je správné i při nulových vahách: nejprve stačí
uvažovat podporované S,T. Předpoklady vytvoří mřížku podporovaných
`U_(i,j)=S_i∪T_j` od průniku k sjednocení. Lokální nerovnosti porovnají
poměry podél hran; dvě teleskopická násobení dávají globální poměr.
Všechny jmenovatele v tomto kroku jsou kladné. Pokud původní S nebo T
podporované není, globální nerovnost platí triviálně.

Bernoulliho součinové míry splňují nerovnost s rovností. Příklady 61(e)
fungují postupně díky neklesajícím poměrům vah podle velikosti, úplnému
uspořádání podpory, součinu nerovností a submodularitě exponentu. V posledním
příkladu formulace podmínky na f vyžaduje, aby průnik a sjednocení byly
v jeho definičním oboru; nepředpokládáme možnost libovolně odstraňovat
body podpory a ponechat závěr.

Program `check_fkg_drift.py` enumeroval všechny nenulové váhy v `{0,1,2}`
na Booleových svazech dimenzí 1–3. Z nich 8, 55 a 763 vah splnilo globální
podmínku; všechny kovariance rostoucích booleovských funkcí byly
nezáporné (72 + 1980 + 305 200 kontrol). Lokální kritérium bylo ověřeno
na 8 + 51 + 654 vahách splňujících všechny jeho předpoklady.

Bez nového nálezu. Silnější graduovanou nerovnost z bibliografické
poznámky za odpovědí 59(c) tento audit nepokrývá.

## 98–99: klesající potenciál i při možném růstu stavu

Položme `H(j)=Σ_(k=1)^j 1/g_k`, `H(0)=0`. Protože g je kladné
a neklesající, pro každý celočíselný pokles d≤j, včetně záporného d,
platí

```
H(j−d) ≤ H(j)−d/g_j.
```

Je-li d kladné, odstraňujeme d členů nejméně `1/g_j`; je-li záporné,
přidáváme −d členů nejvýše `1/g_j`. Podmíněné očekávání poklesu d je
alespoň g_j, takže při každém neukončeném kroku potenciál v očekávání
klesne alespoň o 1.

Pro čas ukončení T a libovolné konečné m sečtením zastavených přírůstků
dostáváme

```
E H(X_(T∧m)) + E(T∧m) ≤ H(n).
```

Nezápornost H a monotónní konvergence tedy dávají `ET≤H(n)` a ukončení
s pravděpodobností 1. Nepoužíváme indukci podle stavu, která by při jeho
možném růstu nebyla odůvodněna. Integrabilita v jednom kroku plyne
z horní meze d≤j a předpokladu `Ed≥g_j>0`: záporná část d má konečné
očekávání a růst H je nejvýše lineární s koeficientem `1/g₁`.

To odpovídá důkazu přes `E min(m,T)` i supermartingalové poznámce v knize.
Její rozšířená konvence pro součet s obrácenými mezemi je správná;
nejde o chybu v indexu. Odhad může být ostrý: u náhodné procházky
s kroky ±1 a stálým kladným driftem δ je očekávaný čas z n roven n/δ.

Přesné lineární soustavy pro 156 konečných řetězců ověřily 1248 stavových
mezí i jednokrokovou potenciálovou nerovnost. Řetězce obsahovaly 1092
skutečně rostoucích přechodů. Tento výpočet potvrzuje model; obecný
důkaz pro nekonečný stavový prostor je argument se zastavením výše.
Bez nového nálezu.

## 50: podmíněná mez a metoda druhého momentu

Pro `X=ΣX_j` zaveďme `Y_j=X_j/X` na `X_j>0`, jinak nulu. Potom
`ΣY_j=[X>0]`, což dává první identitu. U binárních X_j Jensenova
nerovnost pro 1/x dává dolní mez

```
Pr(X>0) ≥ Σ_j p_j / E(X | X_j=1).
```

Značme jmenovatele t_j. Součet `Σp_j t_j` je přesně `EX²`.
Další Jensenovo použití s vahami `p_j/EX` dokazuje, že tato podmíněná
mez je alespoň `(EX)²/EX²`. Nulové marginální pravděpodobnosti se
vynechají; při `EX=0` je X jistě nulové a závěr řešíme přímo.
Není potřeba nezávislost proměnných.

Přesná enumerace prošla pro 6642 tabulek s nenulovou střední hodnotou
a šest nulových případů; vynecháno bylo 258 nulových marginálních členů.
Bez nového nálezu, viz `results/ross.json`.

## 28–29 a F016: vyrovnávání pravděpodobností

Nezávislé bity s pravděpodobnostmi a,b přispívají ke generující funkci
koeficienty `A=(1−a)(1−b)`, `B=a+b−2ab`, `C=ab`. Při transformaci
`a′=a+ε`, `b′=b−ε` se součin změní o

```
δ = ε(b−a)−ε²,
```

takže nové koeficienty jsou `A+δ,B−2δ,C+δ`. Vyrovnání dvojice přes
pevný průměr má δ>0 a zvětšuje očekávání každé konvexní funkce součtu.
Opakováním konečně mnoha takových kroků dostaneme stejné pravděpodobnosti.

Pro libovolnou funkci g existuje maximum na kompaktním průřezu krychle
daném součtem pravděpodobností. Má-li maximalizátor dvě různé vnitřní
pravděpodobnosti po obou stranách jejich průměru, kladný koeficient
`α−2β+γ` dovoluje zlepšení směrem k průměru a záporný směrem k hranici.
Musí tedy být nulový, takže vyrovnáváním beze změny hodnoty zbude jen
jedna vnitřní hodnota a případné nuly a jedničky. Tím platí 28(b).

**F016:** V záporném směru řešení na str. 374 říká
`δ=−min(p_(n−1),1−p_n)`. Toto je hodnota kroku **ε**, nikoli změny
součinu δ. Pro `a=1/4,b=3/4` je správně `ε=−1/4`, `δ=−3/16`.
Vytištěná hodnota δ by dala `A′=C′=−1/16`, tedy záporné pravděpodobnosti.
Stačí zaměnit označení δ za ε. PDF i původní autorův Pre-Fascicle 5A,
str. 31, mají tutéž záměnu; v erratech 4B ani Fascicle 5 nebyla nalezena.
Hlavní věta je správná.

Pro dolní ocas v 28(c) je koeficient vyrovnávání roven rozdílu dvou
sousedních pravděpodobností zbývajících n−2 bitů. Dosazení extremální
podoby `{0,a,1}` a poměr sousedních binomických pravděpodobností v knize
vylučují nuly; jedničky lze také odstranit, případně při rovnosti beze
změny cíle. Degenerovaný případ p=1 je triviální a řeší se před tímto
argumentem. Výsledná dolní-ocasová mez je správná.

Samuelsův odhad 29 lze zkontrolovat indukcí na m v pravém koncovém bodě
`p=(m+1)/n`, pomocí 28(c). Rozdíl levé a pravé strany Q má derivaci
uvedenou v knize; její znaménko řídí `A−F(p)`, kde F roste až do
`(m+1)/(n+1)` a poté klesá. Jelikož `Q(0)=Q(1)=0` a Q je na obou
krajích rostoucí, má mezi krajními body jeden lokální vrchol a jedno
lokální minimum. Nezápornost Q v indukčně vyřešeném bodě zaručí
nezápornost celého požadovaného úseku. Krajní případy m=0,n−1,n jsou
řešeny přímo. Bez dalšího nálezu.

`check_poisson_binomial.py` zkontroloval všech 1286 neklesajících vektorů
délky 1–8 s pravděpodobnostmi `{0,1/4,1/2,3/4,1}`. Obsahuje 7294
konvexních lomených funkcí, 3818 porovnání dolních ocasů a 6430 porovnání
s maximy v extremální třídě pro pět celočíselných funkcí g na každém n.
Dále prošlo 5950 přesných Samuelsových nerovností a 28 symbolických
identit pro derivaci Q. Konečné testy doplňují obecné argumenty;
nepředstavují prohledání všech reálných pravděpodobností.
