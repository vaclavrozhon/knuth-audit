# §1.2.11.3–8 a s. 121: Tricomi, převzetí primárního pramene

**Celá úloha 8 je checked, se zachováním potvrzeného V1-C0017.**
Uzavřena je také konkrétní citace o komplexních argumentech na s. 121.
Koordinátor ověřil 31 členů manifestu
`parallel/asymptotic-primary-followup/results/tricomi-ex8-manifest.json`
a jeho 11 přímých závislostí. Devět společných vstupů knihy a errat
ověřil ve stejném převzetí X0756. Manifest má SHA-256
`86ca1386c876313d889e7fc249b9d89b6b4fdc4879b0819475e3beed3f0bca65`.

Agent přímo přečetl celý článek, tištěné 136–148, a čtyři úvodní
strany svazku. Koordinátor nezávisle přečetl titul, s. 136–137,
141–145 a knižní 121–122/505. Původní obrazy pocházejí z veřejného
IIIF GDZ, identifikátor PPN266833020_0053; přenosová metadata mají
URL a SHA každého obrazu. Nejde o získaný celý PDF svazku.
Titul uvádí 1950/51, ale záhlaví původního článku výslovně
53, Heft 2, 136–148 (1950). Knižní datace tedy souhlasí.

Rozhodná rovnice (12) na s. 141 definuje
`I(alpha,beta)=integral_0^beta exp(alpha*t)(1-t)^alpha dt`.
Knižní integrál označme J(x,f), kde x>0 a reálné f=f(x)=O(sqrt(x)).
Substituce t=-u/x dává přesně `J(x,f)=-x I(x,-f/x)`.
Tricomiho (15) a (21), s. 142–143, dávají

```text
I(x,-f/x) = sqrt(2/x) E(-f/sqrt(2x)) + O(1/x),
E(z) = integral_0^z exp(-t^2) dt.
```

Jeho symbol Erf označuje právě tuto nenormalizovanou funkci E.
V (21) se znaménko vybírá podle poloroviny beta; pro reálné beta
vzniká lichá funkce E. Záměna za běžnou normalizovanou erf by
ztratila faktor sqrt(pi)/2. Vynásobení -x a lichost E dávají
přesný knižní výsledek, s chybou O(1), pro obě znaménka f.
Pro f=0 je identita triviální; obecně se nevyžaduje existence
limity f/sqrt(x). Koeficienty na s. 142 jsou pro omezený poměr
omezené. Úplný moderní odhad zbytku již poskytuje přijatá poznámka
`asymptotic-gamma.md` a oprava V1-C0017.

Práce skutečně zahrnuje komplexní argumenty: s. 137 vymezuje
hlavní větev mocniny a integrační cestu, s. 141 podmínku argumentu
komplexního poměru, (24)–(25) na s. 144 rozdělují komplexní oblasti.
To přímo dokládá obsahovou citaci s. 121. Nevyvozujeme z toho
prvenství ani nezávislé prověření všech vedlejších formulí článku.

Všechny čtyři úplné vrstvy errat jsou prohledány ve společném
`results/errata-search.json`; originální obrazy byly zkontrolovány
v rozsahu popsaném u X0756 a v agentově poznámce. Žádná z nalezených
oprav nemění citaci nebo Gaussovský odhad. V1-C0017 nadále označuje
chybějící absolutní hodnotu v důkazu odpovědi 8, nikoli neplatnost
jejího závěru. Nový nález ani opakovaný matematický test nevznikl.
