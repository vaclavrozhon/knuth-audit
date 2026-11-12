# Rogersův obecnější součet: kořenová kontrola úlohy 1.2.6–62

Konkrétní Rogersova citace je **checked**. Celá úloha 62 zatím zůstává
partial kvůli samostatným odkazům na MacMahona a Dougalla. Nová chyba
TAOCP nevzniká. Původní matematický důkaz úlohy ani jeho úspěšné testy
se tímto pramenným převzetím neopakují.

## Co bylo skutečně přečteno

Root ověřil všech 23 souborů zmrazeného paketu
`parallel/binomial-summation-sources/rogers/`, celkem 7 944 657 bajtů,
a všech osm vstupů. Manifest má SHA-256
`d46e9edeb0c77a31632878aed1691f0a5d2212731c7578e7d58c176416b7d846`.
Přečetl celé předání, rozbor a výpis čtyř vrstev knižních errat.

Přímo obrazově root četl titul svazku 26, Rogersovy strany **15, 17–20,
28–29**, svazková errata **559** a TAOCP **490–491**. Agentův širší
rozsah 15–20 a 28–32 je doložen jeho předáním; root si jej nepřipisuje.
Celý veřejný [původní svazek](https://archive.org/details/london-mathematical-society-proceedings_november-1894-november-1895_26)
je archivován v nadřazeném `sources/plms26.pdf`; kořenový manifest jej
zahrnuje výslovně. Titul má rok 1895, zatímco článek na 15 uvádí přijetí
31. října a přednesení 8. listopadu 1894. Knižní rok je v pořádku.

## Obsah a vady samotného pramene

V agentově rozboru značí `(a;q)_j` součin faktorů `1-a*q^h` pro
`0<=h<j`; nekonečný index znamená příslušný nekonečný součin.
Rogersovy `L_j` a `M_j` jsou koeficientové polynomy definované na
15 a 17, s parametry lambda a mu. Jeho §2 na 18 dává jejich lineární
převod. Konstantní člen při tomto převodu a §3(2) na 20 vedou k §8
na 28–29 a k obecné identitě **(R)** v agentově rozboru.

Root přímo porovnal jmenovatele: §3(2) obsahuje parametr mu;
stejný rozvoj v polynomech L má místo něj lambda. Sazba prvního
součtu §8 na 29 však příslušné lambda vynechává a v prvním členu
tiskne také `v-sqrt(q)` místo `1-lambda*v*sqrt(q)`. Jde o vadu tohoto
pramene, ne jeho moderního OCR. Konečná specializace
`q=1/4, lambda=1/2, mu=1/8, u=v=1` dává podle doslovné sazby `2/7`,
zatímco součin nalevo i rekonstruované odvození dávají `4/9`.
Vyšší členy zmizí díky `mu-lambda*q=0`. Svazková errata na 559
cílovou stranu neopravují. Kniha tento chybný řádek nepřetiskuje.

## Kontrola mostu ke knižní identitě

Root algebraicky ověřil klíčové kroky úplného převodu v agentově
poznámce. Z identity (R) se volbou `d=sqrt(a)` získá (RD), neboť

```
[(1-a*q^(2j))/(1-a)] * (sqrt(a);q)_j/(q*sqrt(a);q)_j
    = (1+sqrt(a)*q^j)/(1+sqrt(a)).
```

Nechť `l,m,n` jsou nezáporné celé parametry z knihy. Součin tří
q-binomických koeficientů je v nich symetrický; lze tedy vzít
`l=min(l,m,n)`. Pro `l>0` dosadíme `b=q^(-l-m), c=q^(-l-n)` a
necháme `a` dojít k `q^(-2l)`. Parametry b,c ukončují řadu již
před limitou a spodní konečné součiny nemají nulové faktory.
Po posunu `j=k+l` je normalizovaný člen `H_j=T_(j-l)/T_(-l)`, kde
T_k je přesně knižní sumand včetně znaménka a mocniny
`q^((3*k^2-k)/2)`. Kontrola exponentu dává
`3*j^2/2-(3*l+1/2)*j` na obou stranách.

Rovnost `T_(-k)=q^k*T_k` převádí dodatečný faktor v (RD) na
`2/(1+q^(-l))`. Poměr nulových faktorů na součinové straně má
limitu **2**, nikoli 1:

```
(1-a*q^(2l))/(1-sqrt(a)*q^l) -> 2.
```

Zbytek tohoto poměru je
`(-1)^l*q^(-l*(3*l-1)/2)*(q;q)_(2l)/[(q;q)_l*(1+q^l)]`.
Ostatní součiny a normalizace T_(-l) přesně ponechají
`(q;q)_(l+m+n)/[(q;q)_l*(q;q)_m*(q;q)_n]`, tedy knižní pravou
stranu. Případ `l=0` má jediný nenulový člen. Z rovnosti pro
`0<q<1` plyne polynomická identita; limitou q k 1 dostaneme
obyčejný Dixonův součet. Nulové podíly jsou odstraněny před dosazením.

Tím je doloženo, že Rogersova práce obsahuje obecnější výsledek,
jak uvádí TAOCP. Audit všech ostatních identit celého článku ani
samostatné prvenství q-Pfaffovy formule se zde netvrdí.

Známé knižní opravy z let 1998, 2021 a 2023 mění exponent sousední
q-Pfaffovy identity, výraz factorial factors a počátek Dixonova článku.
Žádná nemění Rogersovu citaci. Přesné vstupy a uložené soubory
zachycuje `results/rogers-primary-root-manifest.json`.
