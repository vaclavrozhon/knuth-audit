# V2-C0150: párování modulů vynechává poslední modul

Stav: **confirmed**. §4.5.4, str.389, odstavec za algoritmem D.
Tištěný předpis nahrazuje m_k součinem m_(r-k)*m_k
pro 1<=k<=r/2. Moduly jsou přitom číslovány od1 do r.
Má být m_(r+1-k)*m_k; při lichém r se prostřední modul zachová.

Již pro r=2 předpis vytvoří m_1^2 a zcela vynechá m_2.
Nejde o sloučení obou dosavadních sít. Konkrétně pro
N=31,m_1=3,m_2=5 a kandidát x=7 je x^2-N=18.
Číslo18 je kvadratickým zbytkem modulo9, ale nikoli modulo5.
Původní dvojice sít kandidáta odmítne, vytištěná náhrada ho přijme.
N je nesoudělné s oběma moduly, takže příklad splňuje
všechny uvedené předpoklady.

Správné sloučení modulo15 zachovává predikát podle čínské
věty o zbytcích. Obecný důkaz a 11 610 přesných kontrol
opraveného párování jsou v `notes/factoring-fermat.md`
a `results/factoring-fermat.json`.
Tento nález se týká navrženého párování; samotný algoritmus D
s konečným testem celého čtverce je správný.

Původní strana389 vizuálně přečtena. Všechny čtyři řady errat
a současný `sources/err2.textxt` prohledány podle stránky
i obsahu; oprava párování nenalezena. Oprava2005 na390
mění pouze symbol AND. Kontrola3.11.2026.
Poslední fyzický dotisk a prvenství neověřeny, draft neodeslán.
