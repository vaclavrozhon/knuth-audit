# C003: dosažitelná pravděpodobnostní mez v odpovědi 200(b)

Stav 3. listopadu 2026: **confirmed**, původní identifikátor C003 ponechán.
Knižní strana 471, §7.2.2.1, odpověď 200(b); autorský draft Fascicle 5c,
strana 175. Závažnost střední: nesprávná mez v důkazu, konečný algoritmus
a jeho garance pod 1/2 jsou správné. Fyzický výtisk ani prvenství neověřeny.

## Nejkratší pohodlný protipříklad

Použijme n=2 a právě dvě možnosti a1 b1 c1, a2 b2 c2, s proměnnými x,y.
Existuje jediné dokonalé párování, takže S=xy. M=2 a prvočíslo p=5
splňuje požadavek p>2M. Z 25 stejně pravděpodobných dvojic je součin
nulový právě v pěti dvojicích s x=0 a pěti s y=0, s jedním překryvem:

    Pr(s=0 | pevný nenulový polynom S) = (5+5−1)/25 = 9/25
                                     = 1−(1−1/5)^2.

První mez tedy musí být neostrá. Nezávisí to na sporném výkladu slova
„pravděpodobnost“ jako důvěry v odpověď. Už odpověď 4.6.1–16 ve svazku 2
uvádí neostrou mez a její dosažitelnost součinem lineárních polynomů.

Původní věta navíc podmiňuje závěr tím, že byl pozorován výsledek s=0.
U pevného vstupu však S není náhodná hypotéza. Správná jednostranná
garance je pravděpodobnost nulového **vyhodnocení za předpokladu, že
polynom je nenulový**, nikoli posteriorní pravděpodobnost řešitelnosti
bez modelu náhodného vstupu. Tuto výhradu uvádíme odděleně: samotná
ostrá nerovnost již dává jednoznačný protipříklad.

## Opravené tvrzení

Je-li S nenulový, při nezávislých rovnoměrných dosazeních platí

    Pr(s=0) ≤ 1−(1−1/p)^M ≤ M/p < 1/2.

Pro M≥2 je prostřední nerovnost ostrá, pro M=1 je rovností; M=0 lze
vyřešit přímo. Je-li s nenulové, párování jistě existuje. Po r nezávislých
pokusech je pravděpodobnost přehlédnutí existujícího párování <2^(−r).
Neexistující párování algoritmus nikdy neohlásí jako existující.

## Zdroj a zachování evidence

- [Knižní stránka](images/vol4b-p471.png) a
  [autorský draft](images/fasc5c-p175.png) byly přímo zobrazeny.
  Obě verze obsahují stejné znění.
- [Dřívější přesný výsledek](results/determinant_matching.json) obsahuje
  rovnost 9/25 již od prvního auditu. Výčet se neopakoval.
- Svazek 2: [zadání 436](images/matching199-201-vol2-436.png),
  [odpověď 674](images/matching199-201-vol2-674.png) a
  [dosažitelnost 675](images/matching199-201-vol2-675.png).
  Jde jen o křížový zdroj, bez změn cizího pracovního proudu.
- [Šest vrstev errat](results/matching199_201/errata-check.json),
  včetně původního TeXu 4B a Fascicle 5: odpovídající oprava nenalezena.
  Poslední živé porovnání Fascicle 5 je doložené v předchozím bloku.
- Původní kandidátská poznámka i anglická karta jsou uchované v záznamu
  změny a výchozím snímku tohoto bloku. Nová karta ani nové F číslo
  nevznikají; osobní poznámky tak zůstávají u stejného nálezu.

Úplný obecný důkaz, bitová složitost a primární Björklundův článek jsou
v [poznámkách k 199–201](MATCHING199_201_SOURCE_NOTES.md).
