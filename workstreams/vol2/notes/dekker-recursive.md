# §4.2.3-9: proč prostá rekurze nedává čtyřnásobnou přesnost

**Stav: checked v níže přesně vymezeném smyslu.** Úloha žádá studium
rekurzivního použití postupu. Neobsahuje tvrzení, že prosté dosazení musí
fungovat; níže uvedený protipříklad tedy **není nový nález chyby v knize**.
Vyšetřujeme doslovnou rekurzi uvedeného sčítání, její přesnost a počet operací.
Neprohlašujeme všechny možné zdokonalené algoritmy pro čtyři složky za prověřené.

## Význam operací

Nechť `p>=2` je počet významových bitů a `epsilon=2^-p`. Symbol `R(x)`
znamená zaokrouhlení reálného čísla x k nejbližšímu binárnímu p-bitovému číslu.
Exponent zde není omezen; problém nevzniká přetečením ani podtečením.
V půlících případech mohou být zvoleny obě možnosti.

Dvouslovné číslo `(h,t)` má přesnou hodnotu `h+t`; h je hlavní část a t
malá opravná část. Kniha předpokládá `|t|<=epsilon|h|`.
Označme `D(X,Y)` výsledek uvedeného algoritmu pro dvě dvojice:

```
X=(u,u'), Y=(v,v'), po výměně celých dvojic |u|>=|v|;
w = R(u+v),             r = R(R(u-w)+v),
s = R(R(r+v')+u'),
z = R(w+s),             z' = R(R(w-z)+s),
D(X,Y) = (z,z').
```

Zápornou dvojici získáme změnou obou znamének. Máme osm základních
sčítání/odčítání; společný výraz `w+s` se vypočítá jen jednou.

Doslovná rekurze `D2` uchovává dvojici dvojic `((h,t),(h',t'))`. Ve vzorci
pro D nahradí každou základní operaci odpovídajícím voláním D. Porovnání
velikostí hlavních dvojic bereme **přesně**, podle jejich skutečné hodnoty;
protipříklad tedy nevzniká chybným výběrem pořadí.

Počet základních sčítání/odčítání je64, uložené složky jsou čtyři.
Obecně k úrovní takové rekurze použije `8^k` operací pro `2^k` složek,
tedy třetí mocninu počtu složek. Nezapočítáváme kopírování, změny znamének,
porovnání ani případné optimalizace pro nuly.

## Obecný protipříklad bez odečítání vstupů

Položme `a=epsilon^2/4` a vezměme kladné vstupy

```
U = ((2,a),(0,0)),
V = ((1,epsilon),(0,0)).
```

Oba splňují malé opravné části na obou úrovních. Dokonce jejich nenulové
hlavní dvojice splňují silnější Dekkerovu podmínku(7.2),
`|t|<=|h+t| epsilon/(1+epsilon)`. Všechny složky jsou p-bitová čísla.
Celé přesné vstupy i součet mají nejvýše `2p+4<=4p` významových bitů.
Běžná 4p-bitová aritmetika by tedy součet vrátila přesně.

První vnější operace dá

```
W = D((2,a),(1,epsilon)) = (3,epsilon).
```

Důvod: hlavní součet2+1 je přesný; `R(epsilon+a)=epsilon`, protože další
číslo nad epsilon je `epsilon+2epsilon^2` a `a<epsilon^2`. Dále
`R(3+epsilon)=3`, neboť vzdálenost sousedních p-bitových čísel u3 je
`4epsilon`. Závěrečná opravná část je přesně epsilon.

Vnější vzorec se nyní pokusí dopočítat ztracený člen a jako zbytek po
součtu. Potřebuje však dvojité odčítání:

```
T = D((2,a),-(3,epsilon)).
```

Hlavní části dají přesně-1. Opravná část před posledním rozdělením je
`R(a-epsilon)=-epsilon`, protože soused směrem k nule je
`-epsilon+epsilon^2` a `a<epsilon^2/2`. Podle půlení tedy T je jedna z

```
(-1,-epsilon),          (-1-2epsilon,+epsilon).
```

Obě mají hodnotu `-1-epsilon`: člen a již zmizel i z tohoto odčítání.
Přičtení `(1,epsilon)` pak dá v obou případech `(0,0)`. V druhém případě
se nejprve přesně sečtou hlavní části na `-2epsilon` a opravné části na
`+2epsilon`, takže se opět vyruší. Vnější vypočtený zbytek je tedy0.

Zbývající dolní vstupy jsou nulové a všechny další operace zachovají W.
Výsledkem je

```
D2(U,V) = ((3,epsilon),(0,0)),
přesný součet = 3+epsilon+epsilon^2/4,
absolutní chyba = -epsilon^2/4.
```

To platí pro každé `p>=2`, nezávisle na volbě v půlících případech.
Relativní chyba má řád `2^(-2p)`, přestože vstupy jsou kladné a dobře
podmíněné. Poměr absolutní chyby k `2^(-4p)` je `2^(2p-2)`, bez omezení
rostoucí s p. Pro tento přímý rekurzivní algoritmus tedy neexistuje
rovnoměrná konstanta v obvyklé 4p-bitové chybové mezi.

## Už jedna úroveň může ztratit relativní přesnost při vyrušení

Dvojice `(1,epsilon)` a `(-1,a)` mají součet `epsilon+a`, ale D vrátí
`(epsilon,0)`. Hlavní části se vyruší a při sčítání obou oprav se a ztratí.
Relativní chyba je `epsilon/(4+epsilon)`, řádu jedné základní přesnosti.
To souhlasí s Dekkerovým rozlišením absolutní chyby vůči velikostem vstupů
od relativní chyby výsledku při silném vyrušení.

Na druhé úrovni je problém vážnější: první protipříklad ztrácí přesnost
i při sčítání kladných operandů. Identita umožňující přesně obnovit zbytek
u jednotlivých p-bitových čísel se na D automaticky nepřenáší. Zachování
zbytků na nižší úrovni vyžaduje jiný algoritmus nebo silnější aritmetické
operace. Zde žádný takový zdokonalený balík neimplementujeme ani mu
nepřisuzujeme nedokázané meze.

## Primární pramen a ověření

T. J. Dekker, *A Floating-Point Technique for Extending the Available
Precision*, Numerische Mathematik18(1971),224–242,
[DOI](https://doi.org/10.1007/BF01397083),
[použitý sken](https://csclub.uwaterloo.ca/~pbarfuss/dekker1971.pdf).
Sken a metadata jsou v `sources/dekker-1971.*`. Bibliografické údaje souhlasí.

Vizuálně přečteny str.226–228 (definice čísel, operací a přesného zbytku),
235–237 (definice dvojice a sčítání) a240 (omezení a kód add2), tedy
souborové strany3/4/5/12/13/14/17. Úvod225 přečten jako extrahovaný text.
Článek nepředstírá, že jeho operace nad dvojicemi jsou správně zaokrouhlené;
na240 výslovně rozlišuje jejich vlastnosti od operace vracející vždy jedno
ze dvou sousedních čísel. Jeho poznámka o čtyřnásobné přesnosti na235
začíná nativní dvojnásobnou přesností splňující předpoklady, nikoli nutně
rekurzí vlastního add2.

Stažen také [původní institucionální report1970](https://ir.cwi.nl/pub/9158/9158D.pdf),
uložen v `sources/dekker-1970-cwi.*`; jeho úplné porovnání s článkem
nebylo provedeno a není podkladem uvedeného důkazu.

- [Doslovný model](../dekker_recursive.py) používá přesné zlomky a prověřený
  binární zaokrouhlovač, nikoli hostitelské floating point operace.
- [Průzkum](../explore_dekker.py),
  [výstup](../results/dekker-recursive-exploration.json):1800 vstupních
  dvojic v šesti formátech; odhalil chybu v získávání vnějšího zbytku.
  Údaje o nejhorší chybě jsou pouze maxima tohoto vzorku.
- [Kontrola rodiny](../verify_dekker_recursive.py),
  [výstup](../results/dekker-recursive-family.json):33 instancí pro11 hodnot
  p od2 do113 a tři půlící pravidla. Uloženy všechny mezivýsledky,64 operací,
  přesná chyba a samostatný příklad vyrušení. Obecný důkaz je výše;
  konečné kontroly jej nenahrazují.
