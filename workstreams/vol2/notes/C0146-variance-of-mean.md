# V2-C0146: rozptyl průměru v doplňku na stranu 373

Stav: **confirmed**, záměna označení veličiny a jejího průměru.
Erratum z 21. května 2005, `all2-prepre`, strana 20, přidává
za (62) tvrzení, že Hensley dokázal rozptyl tau_n úměrný log n.
Původní doplněk byl vizuálně přečten:
[doklad](../images/euclid-average-errata-p20.png).

Kniha však na straně 369 v (48) definuje

```
tau_n = (1/phi(n)) sum_(0<=m<n, gcd(m,n)=1) T(m,n),
```

kde phi(n) je počet přípustných čitatelů a T(m,n) počet
dělení algoritmu. Pro každé pevné n je tau_n určité racionální
číslo. Není to náhodná veličina počítající dělení. Pokud se
chápe jako konstantní náhodná veličina, její rozptyl
E[(tau_n-E tau_n)^2] je přesně nula, nikoli kladný násobek log n.
Definice (48) byla znovu přečtena z původní stránky.

Také pravděpodobnostní prostor je třeba uvést. Hensleyův
vydavatelský abstrakt popisuje rovnoměrné dvojice
1<=u<=v<=N, tedy současně proměnný čitatel i jmenovatel.
Nevyslovuje tam výsledek pro jediný pevný jmenovatel v=N.
Celý původní článek Hensley1994 nebyl získán.

Přesnou externí oporu pro vhodnou náhradu poskytuje Morrisův
preprint arXiv:1502.07616v1, Theorem 1 a §5. Definuje dvě
rovnoměrná rozdělení na 1<=u<v<=N, jedno s podmínkou gcd=1
a druhé bez ní. Pro počet obvyklých dělení D(u,v)=T(v,u)
uvádí momentovou konvergenci

```
E[(D-a ln N)/sqrt(ln N)] -> 0,
E[(D-a ln N)^2/ln N] -> sigma^2 > 0,
a=12 ln2/pi^2.
```

Odtud algebraicky Var(D)/ln N -> sigma^2. Konstantní posun
D+1=T(u,v) při u<v rozptyl nemění. Vhodná náhradní věta
tedy musí mluvit o rozptylu **počtu dělení pro náhodně vybrané
dvojice s oběma čísly omezenými N**, ne o rozptylu tau_n.
Přidání diagonály s O(N) dvojicemi nezmění limitu, protože
počty kroků jsou O(log N) a dvojic je řádu N^2.

Rozsah čtení Morrise: úvod a definice textově; původní strany
2–3, 14, 16–18 vizuálně, včetně (18) a převodu na všechny
dvojice. Momentová věta je zde externí opora; není deklarován
nový úplný důkaz všech analytických lemmat. Samotná vada tau_n
plyne přímo z knižní definice a žádnou externí větu nepotřebuje.

Všechny čtyři řady errat a aktuální TeX byly 3. listopadu 2026
prohledány podle 373, Hensley a rozptylu. Pozdější oprava
této věty nenalezena. Jde o chybu **v přidaném textu errat**,
ne o již opravenou chybu, kterou bychom pouze znovu nahlásili.
Poslední fyzický dotisk ani priorita nejsou ověřeny.
ASCII návrh je uložen, nikoli odeslán.

Metadata: [euclid-average.json](../sources/euclid-average.json).

