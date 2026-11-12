# §1.2.6–62: Dougallův původní článek

Kořenová revize 2. listopadu 2026, V1-X0730. Konkrétní citace
Dougalla je checked; celá úloha 62 zůstává partial pouze pro
MacMahonův článek 1902, s. 274–288. Dřívější matematické důkazy
a úspěšné testy se neopakovaly.

Root ověřil všech 43 souborů, 4 923 093 bajtů, a 12 vstupů
zmrazeného paketu `parallel/binomial-summation-sources/dougall/`.
Hash jeho MANIFEST.json je
`4f5aa5db38f71072d06d9c5f08d850e82c90cc71c6610af2d1081a580c50c407`.
Přečetl celé předání, podrobnou poznámku a výpis čtyř vrstev errat.
Přímo obrazově četl původní titul 1907 a strany 114, 123, 124, 132,
ve vydavatelském facsimile také 121–122 a titul přetisku 1964,
a znovu porovnal knižní 490. Agentovo čtení celého facsimile 114–132
je převzato; nejde o root audit všech jeho analytických vět.

Původní titul svazku XXV, session 1906–1907, uvádí vydavatele
John Lindsay a rok 1907. Začátek článku Johna Dougalla
*On Vandermonde's Theorem, and some more general Expansions*
na 114 uvádí přednesení 8. března 1907. Na 132 vlastní článek
končí před názvy dvou jiných sdělení. Cambridge poskytuje facsimile
stejné sazby; jeho titulní část je výslovně Kraus Reprint 1964.
Rok původního tisku je tedy ověřen samostatným původním exemplářem,
nikoli odvozen z moderního katalogového data.

Pro nezáporná celá l, m, n označme C(u,v) binomický koeficient,
nulový pro celé v mimo 0 až u. Knižní součet je

```text
S = sum_k (-1)^k C(l+m,l+k) C(m+n,m+k) C(n+l,n+k).
```

Položme h=min(l,m,n). Po rozepsání faktoriálů jsou nenulové jen
indexy −h až h a členy k=j, k=−j jsou stejné. Člen pro k=0 je

```text
B = (l+m)!(m+n)!(n+l)! / (l!^2 m!^2 n!^2).
```

Označme (a)_j rostoucí součin a(a+1)…(a+j−1), a_down(j) klesající
součin a(a−1)…(a−j+1), oba rovny 1 pro j=0. Pro j>=1 je každý
ze spárovaných členů roven

```text
B * (-1)^j * l_down(j)m_down(j)n_down(j)
            / ((l+1)_j(m+1)_j(n+1)_j).
```

Dougallova Pi(x) znamená Gamma(x+1), rozšíření faktoriálu, tedy
Pi(t)=t! pro nezáporná celá t. Jeho formule (10) na 123 po
dosazení x=l, y=m, z=n dává

```text
l!m!n!(l+m+n)! / ((m+n)!(n+l)!(l+m)!)
 = 1 + 2 sum_(j=1)^h (-1)^j l_down(j)m_down(j)n_down(j)
                         / ((l+1)_j(m+1)_j(n+1)_j).
```

Vynásobení B dává přesně S=(l+m+n)!/(l!m!n!). Je-li některý
parametr nulový, h=0 a pomocná suma je prázdná. Zahrnut je
i případ l=m=n=0. Původní podmínka Re(x+y+z)>−1 je splněna.

Také přechod od (9) k (10) je pro tyto parametry bez obtíží:
v každém členu s j>=1 faktor `(c+2j)(c)_j/(c*j!)` má pro c->0
limitu 2, zatímco člen j=0 zůstává 1. Klesající součiny
u nezáporných celých parametrů řadu ukončí pro j>h, takže se zde limituje
pouze konečný počet členů. Nevyžaduje to nový audit obecného
komplexního pokračování dokazovaného v původním článku.

Na 124 je i obecná Dixonova formule (14) a explicitní odkaz na
Dixonovu stranu 284, v souladu se známou knižní opravou 2023.
V žádné ze čtyř vrstev errat se neobjevila změna Dougallovy citace.
Sousední opravy q-vzorce a výrazu factorial factors jsou odlišeny.
Dougall zde není pramenem q-analogie; její dosavadní matematický
důkaz a Rogersova revize X0726 zůstávají samostatné.

Celý původní zdrojový svazek s hashem
`95e54a627169ce82b5a20376d3703484332c63f17798d7cc6e00483d9f8bf763`
je archivován spolu s již zmrazeným výňatkem. Archivace celého
svazku nerozšiřuje tvrzený rozsah četby. Nová chyba TAOCP nevznikla.
