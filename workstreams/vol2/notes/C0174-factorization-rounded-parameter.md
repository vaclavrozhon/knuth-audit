# V2-C0174: zanedbaná podlaha v přesném časovém odhadu

**Stav: confirmed.** Odpověď §4.5.4-36 na665 používá pro r
rozvoj s chybou O(sqrt(log log N/log N)), ačkoli r je v(22)
na399 podlahou log(2sqrt N)/log p_m. Obě původní stránky byly
vizuálně přečteny.

Podrobné značení, vlastní důkaz a oprava jsou v
[factoring-refinement.md](factoring-refinement.md),§1–3.
Tištěný rozvoj platí pro nezaokrouhlené rho, nikoli pro r.
Pro celá m→∞ položme h=ln m, k=floor(h/ln h),
`N=floor(p_m^(2k+1)/4)` a `c=2h/sqrt(ln N ln ln N)`.
Pak c→1, rho=k+1/2−o(1), r=k. Rozdíl levé a pravé strany
tištěného rozvoje jde k1/2, zatímco uváděný zbytek jde k0.

V čase(22) způsobí ztracená zlomková část chybu logaritmu
řádu sqrt(log N log log N). Nelze ji zahrnout do následujícího
O(log log N). Konečný optimalizovaný výsledek lze zachovat:
nejprve volit celé r poblíž sqrt(2H/(ln H−1)), H=ln(2sqrt N),
pak upravit m tak, aby `0<=H-r ln p_m=O(1)`.
Vlastní důkaz optimality s chybou O(log log N) je v poznámce.

Nejde o popření heuristických předpokladů faktorizace ani o tvrzení,
že konečný hlavní člen musí být jiný. Chybná je algebraická
specializace konkrétního výrazu se zadanou podlahou.

Errata: all2-prepre, all2-pre, all2, err2 a zdrojové err2.textxt;
hledáno3.11.2026 pod399/415/665/36 a souvisejícími vzorci,
Schroeppel, logaritmy. Relevantní oprava nenalezena; oprava665
z18.2.2004 řeší úlohu35. Pozdější fyzický dotisk a priorita
neověřeny. Anglický návrh hlášení je neodeslán.
