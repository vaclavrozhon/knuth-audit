# C0094: znaménko v závěrečném sevření odpovědi4.2.4-18

**Confirmed**, 2.11.2026. TAOCP2,3.vydání,1.dotisk1997,
tištěná str.622 (DjVu634), poslední řádek důkazu před poznámkou o Cohenovi.
[Originál](../images/vol2-p622.png) vizuálně ověřen.

Značme `p(a,b)=sum_{a<=k<b}P(L_k)`, jak činí odpověď.
Bezprostředně před závěrečným sevřením jsou definována celá
`m=floor(log10(a^n))`, `m'=floor(log10(b^n))` a správně odvozeno

```
p(a^n,b^n) <= p(10^m,10^(m'+1)) = m'-m+1.
```
Také je dokázáno `p(a^n,b^n)=n p(a,b)`. V následujícím řádku se
však horní mez tiskne jako

```
floor(log10(b^n)) + floor(log10(a^n)) + 1.
```
**První znaménko + zde má být −.** Pak po vydělení n obě meze
konvergují k `log10(b/a)`, jak důkaz požaduje. Například pro a10,b100
správné sevření je `n-1<=n p(10,100)<=n+1`; tištěná horní mez je
`3n+1`. Tištěná slabší nerovnost sama není nepravdivá, ale nevyjadřuje
odvozené sevření a nestačí k uvedenému limitnímu závěru.

Obecný důkaz výsledku včetně konečných výjimek při zdvojení L_a je
v [benford-axioms.md](benford-axioms.md). Tento nález se týká jen
znaménka, nikoli neplatnosti hlavního tvrzení nebo těchto množinových výjimek.

Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální
`err2.textxt` podle622, answer18 a souvisejících výrazů. Historická
oprava22.3.2002 mění závorku v řádku s `p(b^(n-1)a,b^n)`, nikoli
toto znaménko. Příslušná původní stránka errat37 byla vizuálně
přečtena v bloku4.2.4. Oprava znaménka nebyla nalezena.

Poslední fyzický dotisk, prvenství a odměna nejsou ověřeny.
[Anglický návrh](../reports/C0094-benford-proof-sign-draft.txt) není odeslán.
