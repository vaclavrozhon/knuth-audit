# V2-C0133: dvě vady v opravě důkazu lemmatu M

Stav: **confirmed**. Oprava z 18. září 2011 k §4.5.3,
straně 367, obsahuje chybějící index a nesprávný závěr
o dvou pomocných limitách. Samotné lemma M i jeho aplikace
jsou správné; jde o místní opravu důkazu.

Značení knihy: I a J jsou sjednocení po dvou disjunktních
intervalů I_k a J_k v [0,1), jejichž společný doplněk K
v [0,1] má míru nula. Míra mu zde znamená délku. I_N a J_N
obsahují prvních N intervalů. Zbytek K_N je doplněk těchto
dvou konečných sjednocení. P_n={0,1/n,...,(n-1)/n} je
rovnoměrná síť a r_n,s_n,t_n počítají její body v I_N,J_N,K_N.

V první náhradě, pro řádek -8, má být

```
I_N subset I subset I_N union K_N,
```

nikoli tištěné I_N union K. Původní K neobsahuje žádný bod
vynechaných intervalů I_(N+1), I_(N+2), ... . Následující
nerovnost r_n <= |I intersect P_n| <= r_n+t_n je správná.

Druhá náhrada, pro řádek -5, tvrdí pro pevné epsilon a
zvolené N, že obě limity r_n/n a (r_n+t_n)/n jsou rovny
mu(I). Ve skutečnosti jsou tyto limity mu(I_N) a 1-mu(J_N).
Nemusejí se rovnat ani jedna druhé, ani mu(I).

## Přesný protipříklad pro každé konečné N

Pro k>=1 položme

```
I_k = [1-2^(-(2k-2)), 1-2^(-(2k-1))),
J_k = [1-2^(-(2k-1)), 1-2^(-2k)).
```

Tyto intervaly rozdělují [0,1), takže K={1}. Jejich délky
jsou 2^(-(2k-1)) a 2^(-2k), a proto

```
mu(I)   = 2/3,
mu(I_N) = (2/3)(1-4^-N),
mu(J_N) = (1/3)(1-4^-N),
mu(I_N)+mu(J_N) = 1-4^-N.
```

Pro každé epsilon>0 lze vybrat konečné N s 4^-N<=epsilon,
jak důkaz požaduje. Přesto pro toto pevné N platí

```
lim r_n/n       = 2/3 - (2/3)4^-N < 2/3,
lim (r_n+t_n)/n = 2/3 + (1/3)4^-N > 2/3.
```

Limity počtů pro konečné sjednocení intervalů plynou přímo
z odchylky nejvýše N bodů proti n-násobku délky. Tento
protipříklad tedy nevyužívá lemma, jehož důkaz kontrolujeme.
Současně kterýkoli vnitřní bod I_(N+1) vyvrací chybnou inkluzi.

## Opravený závěr

Označme a_n=|I intersect P_n|/n. Původní odhady a správná
inkluze dávají pro každé epsilon>0 jedno pevné N takové, že

```
mu(I)-epsilon-N/n <= a_n <= mu(I)+epsilon+N/n.
```

Nejprve necháme n růst při pevném N. Dostaneme
mu(I)-epsilon <= liminf a_n <= limsup a_n <= mu(I)+epsilon.
Potom necháme epsilon klesat k nule. To dokazuje požadovanou
limitu a_n->mu(I), bez nesprávného tvrzení o pomocných limitách.

## Doklady a rozsah

Vizuálně přečtena [původní strana 367](../images/vol2-p367.png)
i [strana 10 historických errat](../images/euclid-all2-pre-p10.png).
Prohledány all2-prepre, all2-pre, all2 a err2 dne 2026-11-03,
podle strany i obsahu důkazu. Pozdější oprava těchto dvou vad
v našich podkladech není. Původní důkaz už měl chybnou limitu
r_n/n; náhrada 2011 ji ponechala a přidala druhou pomocnou
limitu a chybnou inkluzi. Proto je nález výslovně k aktuální
historické náhradě, ne tvrzení, že známá oprava neexistuje.

Numerický výpočet není potřeba: všechny délky i obě limity
jsou explicitní geometrické součty. Poslední fyzický dotisk,
priorita a nárok na odměnu neověřeny. Návrh hlášení neodeslán.
