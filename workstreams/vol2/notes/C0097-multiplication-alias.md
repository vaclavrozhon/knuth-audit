# V2-C0097: index při překrytí paměti v §4.3.1-30

**Confirmed v dostupných zdrojích.** Originály zadání283 a odpovědi627
vizuálně přečteny. M má m-místný násobenec U a n-místný násobitel V;
m<=n není předpokládáno. Odpověď30 uvádí umístění v_j do w_(j+n).
Pro obecné m,n má být **w_(j+m)**.

Nejmenší délky demonstrující problém: m2,n1,U=(10)_b,V=1, b>=2.
Při tištěném umístění je v_0 na adrese w_1. Krok M1 však vynuluje
w_1 i w_0, tedy smaže celý násobitel. M2 zjistí nulu a vrátí součin0,
ačkoli U*V=b. Nejde o otázku pořadí dvou přiřazení uvnitř M4.

Správné umístění w_(j+m) ponechá V za nulovanými m slovy. Iterace j
používá v_j až do dokončení všech m součinů; teprve pak přepíše jeho
adresu konečným přenosem. Vyšší dosud nepřečtené číslice V nejsou dotčeny.
Tištěné umístění lze zachránit dodatečnou podmínkou m<=n, ale jednodušší
je opravit index na m a ponechat obecný algoritmus.

MIX model ověřil375 případů opraveného umístění pro m,n1–5 a tři
bajtové základy. Popsaný chybný případ reprodukován rovněž v MIX:
[classical-division.json](../results/classical-division.json), blok aliasing.
[Obecný důkaz](classical-division-exercises.md) používá jen pořadí čtení/zápisů.

Dne2.11.2026 prohledány `all2-prepre`, `all2-pre`, `all2`, `err2`
podle627/30 i obsahu překrytí paměti. Známá oprava627 mění konkávnost
v odpovědi28, žádná nalezená položka neopravuje index30. Poslední fyzický
dotisk ani priorita neověřeny. [Návrh](../reports/C0097-multiplication-alias-draft.txt)
nebyl odeslán.
