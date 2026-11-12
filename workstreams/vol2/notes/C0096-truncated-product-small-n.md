# V2-C0096: malé délky v odpovědi §4.3.1-15

**Confirmed v dostupných zdrojích, drobná chybějící podmínka.** Zadání
[str.282](../images/vol2-p282.png) neomezuje kladný počet číslic n;
[odpověď625](../images/vol2-p625.png) tvrdí, že chyba je nezáporná
„and less than (n-2)b^(-n-1)“. Oba originály vizuálně přečteny.

Chybou E rozumíme součet vynechaných členů u_i v_j b^(-i-j) pro i+j>n+2,
před závěrečným zaokrouhlením; b>=2 je základ a i,j jsou1,...,n.
Pro n=1,2 není vynechán žádný člen, E=0. Při n=1 je tištěná horní mez
záporná, při n=2 dává neplatnou ostrou nerovnost0<0. Oprava: n>=3,
resp. samostatně uvést nulovou chybu pro n<=2.

Všechna váhová znaménka jsou kladná, proto se maximum dosáhne při všech
číslicích b-1. Přesná hodnota

```
E_max = (n-2)b^(-n-1) - (n-1)b^(-n-2) + b^(-2n)
```

je pro n>=3 ostře pod uvedenou mezí, pro n=1,2 je0.
Odvození a870 přesných kontrol plus1069 dvojic z přímého součinu:
[classical-basic.md](classical-basic.md),
[classical-basic.json](../results/classical-basic.json).

Dovětek pro i+j>n+3 obdobně vyžaduje nulový případ n<=3; jeho mez
(n-3)b^(-n-2) je pro n<3 záporná. Hlavní závěr o zkrácení násobení
pro velká n zůstává správný.

Dne2.11.2026 prohledány všechny vrstvy `all2-prepre`, `all2-pre`, `all2`,
`err2` podle stran282/625 i obsahu. Nalezena jen jiná sousední errata;
žádná oprava délky15. Poslední fyzický dotisk a priorita neověřeny.
[Návrh hlášení](../reports/C0096-truncated-product-small-n-draft.txt) neodeslán.
