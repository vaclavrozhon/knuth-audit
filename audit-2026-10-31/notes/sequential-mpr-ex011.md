# D114 — celá MPR11 a lokální chyba F162

6. listopadu 2026. Celé zadání na p13/file33 a celá
odpověď na p372/file392 přímo zobrazeny; stejně
autorův Pre-Fascicle 5A, p13/file19 a p29/file35.
Výsledná věta zadání je pravdivá. Jedna rovnost
v důkazu je chybná; její přesný rozsah je F162.

## Redukce na dvě stejně rozdělené veličiny

Položme A=(X₁+⋯+X_n)/n a B=(X_(n+1)+⋯+X_(2n))/n.
Každá je funkcí jedné ze dvou disjunktních skupin
nezávislých veličin. Pro libovolné množiny hodnot
funkcí se proto společná pravděpodobnost rozloží
na součin: stačí sečíst součinové pravděpodobnosti
původních konečných vektorů. Také rozdělení A a B
je stejné, neboť obě skupiny mají stejný součinový
zákon. Jsou diskrétní: konečný kartézský součin
spočetných nosičů je spočetný a jeho obraz součtem
rovněž. Žádný předpoklad o existenci střední hodnoty
nebo konečném rozptylu se nepoužívá.

Původní levá strana je přesně
P(|(A+B)/2−α|≤|A−α|). Tvrzení pro n=1 a libovolnou
diskrétní distribuci A,B tedy dokazuje všechny n≥1.
Redukce v knize je správná; nejde o nahrazení
původních proměnných jejich očekáváním.

## Každý tištěný krok před chybnou rovností

Pro n=1 definujme D_i=|X_i−α|. Trojúhelníková
nerovnost dává bodově

    |X₁+X₂−2α| ≤ D₁+D₂.

Jev D₁+D₂≤2D₁ je proto podmnožinou jevu
|X₁+X₂−2α|≤2D₁. Při přechodu k pravděpodobnostem
má tištěný vztah správný směr ≥. Dále
D₁+D₂≤2D₁ je přesně totéž jako D₂≤D₁.
Ani odečtení, ani trojúhelníková nerovnost nevyžadují
D₁>0. Celý dosavadní řetězec tedy platí i při X₁=α.

D₁,D₂ jsou stejně rozdělené a nezávislé. Záměna
indexů je bijekce prostorů se zachováním jejich
součinových pravděpodobností. Označíme-li
t=P(D₁=D₂), oba ostré jevy D₁<D₂ a D₂<D₁ mají
stejnou pravděpodobnost (1−t)/2. Proto přesně

    P(D₂≤D₁)=(1+t)/2.

## F162: v tištěném t se ztratily absolutní hodnoty

Kniha místo posledního t používá P(X₁=X₂). Tyto
události nejsou obecně stejné: protilehlé hodnoty
kolem α mají rovné vzdálenosti, i když se nerovnají.

Přesný svědek: α=0 a X₁,X₂ nezávisle nabývají −1,+1
s pravděpodobnostmi 1/2,1/2. Každá ze čtyř dvojic má
hmotnost 1/4. Ve všech D₁=D₂=1, takže P(D₂≤D₁)=1.
Pouze dvojice (−1,−1) a (+1,+1) mají X₁=X₂, tudíž
(1+P(X₁=X₂))/2=(1+1/2)/2=3/4. Vytištěná rovnost
tak porovnává 1 a 3/4 v platném nedegenerovaném
konečném prostoru. Nejde o podmiňování nulou,
limitní okraj ani otázku implicitního n.

V témže příkladu má průměr hodnotu −1,0,+1, a jeho
absolutní hodnota nikdy nepřesáhne 1. Pravděpodobnost
v původním zadání je tedy 1>1/2: svědek vyvrací
právě lokální rovnost, nikoli hlavní větu.

## Nejmenší oprava a dokončení přísné meze

Jev X₁=X₂ je podmnožinou D₁=D₂. Proto lze buď
vložit správné absolutní hodnoty do t, nebo nejmenším
zásahem nahradit chybnou rovnost znakem ≥:

    P(D₂≤D₁)
      =(1+P(D₁=D₂))/2
      ≥(1+P(X₁=X₂))/2
      >1/2.

Poslední přísnost potřebuje diskrétnost a nezávislost.
Je-li společný nosič S a P(X_i=x)=p_x, pak
P(X₁=X₂)=Σ_(x∈S) p_x². Součet je nanejvýš 1
a je kladný, protože aspoň jedno p_x>0: jinak by
celková hmotnost spočetné distribuce byla 0.
Je tedy dovoleno použít i nekonečný spočetný nosič;
všechny sčítané členy jsou nezáporné. Degenerovaná
jednobodová distribuce má tuto pravděpodobnost 1
a důkaz rovněž funguje pro každé α.

Alternativně je diskrétní i D_i, a proto t>0 přímo.
Pro samotnou hlavní větu není třeba žádná
nekonstanta ve vztahu mezi α a nosičem.

Kombinace s trojúhelníkovým krokem a redukcí A,B
dokazuje celé zadání pro libovolný reálný α a n≥1.
Všechna tištěná tvrzení mají tímto důkaz, jediný
neplatný mezikrok je přesně opraven.

## Originály, errata a bibliografická výjimka

V původním PDF p372 je výslovně
(1+Pr(X₁=X₂))/2, bez absolutních hodnot.
Stejný výraz a rovnost má autorův PS, p29/file35.
Čtena celá okolní odpověď i zadání, žádný jiný
předpoklad nevylučuje dvoubodový symetrický nosič.

Čerstvá cílená kontrola všech šesti lokálních vrstev
errat a všech tří TeX zdrojů nenalezla použitelnou
opravu. P372 obsahuje pouze bibliografickou změnu
odpovědi18; Fascicle5 p13 mění otázku5(b). Změna
odpovědi11 na Fascicle6 p186 se týká SAT trojic
a není tímto MPR11. Hashe, hledané výrazy a všechny
lokální zásahy jsou v
`results/sequential/mpr-011-mean-errata.json`.
Lokální all4b má datum 16. dubna 2026; netvrdíme
ověření živého webového stavu nebo fyzického výtisku.

Poznámka o tom, že úlohu navrhl T. M. Cover,
nemá zde uvedený pramen; její historická atribuce
je výslovně vynechána. Žádná část matematického
důkazu na této atribuci nezávisí.

D114 uzavírá celou úlohu11 jako reviewed s lokální
opravou F162 nízké závažnosti. Žádný numerický běh
není potřeba; čtyři atomy jsou úplně vypsány.
Nález se lokalizuje pouze na odpověď p372/file392,
nikoli na platné zadání p13/file33.
