# V3-C0017 — izolované prvky v konstrukci cyklů

Status: candidate, low. Odpověď §5.1.2-11, s.599 / souborová610,
první odstavec; originál images/multisets-file-610.png.

Konstrukce přiřazuje x_k cyklus tvořený všemi dvojicemi(i,j),
pro něž x_i≺x_j a k∈{i,j}. Pro antichain {x_1,x_2} nejsou
žádné takové dvojice; oba vzniklé seznamy jsou prázdné. V obvyklé
konvenci, kde prvočinitel musí být neprázdný cyklus, to nesplňuje
požadovaný výstup. Pokud bychom oba seznamy četli jako jednotku ε,
dvě topologická pořadí dávají stejné slovo faktorů ε,ε, což není
očekávaná bijekce s různými prvočíselnými faktorizacemi.

Oprava je jednoduchá: izolovanému x_k přiřadit jednočlenný cyklus
na soukromém písmenu z_k. Lze také přidat soukromé písmeno každému
cyklu. Pak dva různé cykly sdílejí písmeno právě tehdy, jsou-li
příslušné vrcholy porovnatelné; žádný cyklus není prázdný. Samotné
tvrzení o existenci reprezentace libovolného posetu zůstává platné.

Candidate místo confirmed: je třeba rozhodnout, zda kontext již
implicitně vyjímá izolované vrcholy nebo připouští zvláštní zacházení
s prázdnými cykly. Nejde o protipříklad k existenčnímu tvrzení, nýbrž
o chybějící případ uvedené konkrétní konstrukce. Koordinátor tento
opatrný status výslovně potvrdil; další rešerše se kvůli drobnosti nedělá.

Všech pět lokálních vrstev errat zkontrolováno: all3-prepre,
all3-pre,all3,err3,err3-1e. Oprava1.1.2006 v odpovědi11 řeší
zachování pořadí identických neprázdných cyklů, nikoli izolované
vrcholy. Chybějící „topological sorting“ v zadání je rovněž známé
erratum a není nález. Přesné odkazy v sources/isolated-poset-errata-review.json.

Nález se týká zdejšího prvního dotisku a nebyl ověřen v tištěném
exempláři. Nejde o tvrzení prvenství ani příslib odměny.
