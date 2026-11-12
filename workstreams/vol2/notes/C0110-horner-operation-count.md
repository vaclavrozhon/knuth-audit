# V2-C0110: počet násobení v Hornerově převodu

**confirmed**, 2. listopadu 2026; drobná chyba počtu operací.
TAOCP2, třetí vydání, první dotisk 1997, §4.4, strana 323,
odstavec začínající „A trickier but perhaps faster method“.
[Původní stránka](../images/vol2-p323.png) byla zobrazena.

Vstup je `(u_m ... u_0)_10`, tedy má m+1 číslic. Program (6)
nastaví rA=u_m a j=m-1 a pro j=m-1,...,0 vykonává jediné
`MUL =10=` a přičtení další číslice. Počet násobení i přičtení
je proto m. Následující text však srovnává rychlejší postup
s „m-1 multiplications and additions“.

Nejmenší případ m=1 má dvě číslice: pro 12 je nutná operace
`1*10+2`, nikoli nula operací. Navržená oprava: m-1 změnit na m.
Odhad „about lg m“ je jen asymptotický orientační popis a tento
nález se jej netýká. Správnost programu se nemění.

Všechny čtyři řady errat byly prohledány. Změna strany 323
z 10. července 2018 nahrazuje až spodních 19 řádků, tedy jiný
odstavec o ručních převodech; tento počet neopravuje. Simulace
1520 vstupů ověřila i přesný počet iterací programu (6).
Nejnovější fyzický dotisk, priorita a odměna neověřeny. Neodesláno.
