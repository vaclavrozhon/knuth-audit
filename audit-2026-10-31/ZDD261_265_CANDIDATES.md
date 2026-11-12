# Otevřené interpretace v úloze 7.2.2.1–261

## C043 — co zahrnuje „main options“ v části (b)

Obě zdrojové odpovědi na str. 482/186 byly prohlédnuty. Část (a)
nazývá hlavními možnosti pro hrany a pak samostatně přidává nulové
možnosti pro nepoužitý vrchol. Část (b) žádá převzít položky a hlavní
možnosti z (a). Pokud to znamená jen hrany, nemůže žádný vnitřní
vrchol zůstat nepoužitý. Nulové možnosti je nutné zachovat.

Krátký svědek: vrcholy s,v,t, hrany s→t, s→v, v→t; požadována cesta
s→t. Existují dvě cesty. Samotné hranové možnosti připouštějí jen
s→v→t, protože přímá cesta nepokryje primární v− a v+.
Stačí doplnit možnosti `v− v:0` a `v+ v:0`.

Slovo „main“ může být neformálním odkazem na hlavní konstrukci
včetně nulových možností, na rozdíl od dodatečného číslovacího řetězu.
Proto jde o kandidáta na zpřesnění, nikoli potvrzenou chybu algoritmu.
Podrobnosti: `results/zdd261_264/main-options-witness.json`.
Barva `0` je zde skutečná shodovatelná barva, nikoli neobarvený výskyt;
její záměna za interní bezbarvý sentinel by byla chybou našeho modelu.

## C044 — zdroje trojúhelníku mají podle doslovného seznamu vstupní hrany

V části (c) zadané hrany obsahují například (0,2)→(0,1) i
(1,n)→(2,n). Jejich cíle patří do S. Pro skutečné zdroje a pro
rozdělení původního čtvercového příkladu je třeba všechny hrany do S
vynechat. Slovo „sources“ to může implicitně požadovat.

Při doslovném povolení těchto okrajových hran vychází pro n=3 deset
rodin a pro n=4 šedesát čtyři. Při zamýšlených skutečných zdrojích
je to pět a šestnáct. Úplné malé množiny hran jsou uloženy v
`results/zdd261_264/literal-boundary-paths.json`; nové malé počty
se po přijetí neopakují. Chyba parametru F154 je od tohoto kandidáta
oddělená: již n=2 vyvrací knižní součin v obou interpretacích.

## Souvislost s C041

Tvrzení části (c) o 2M_n uzlech je také schematické při započtení
obou společných terminálů. Sériové spojení dvou dokončených ZDD
má 2M_n−2 uzlů. Nový samostatný nález nezakládáme: stejná otázka
přesného versus schematického účtování je již otevřená v C041.

Obě nové interpretace mají kontexty ve všech šesti vrstvách errat;
odpovídající oprava nenalezena. Publikovaná k→m oprava 261(b) je
evidovaná samostatně jako E110 a naše kniha ji již obsahuje.
