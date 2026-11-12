# V3-C0030 — vadná varianta Q selže už ve druhé fázi

Confirmed, low. Svazek 3, §5.2.2 odpověď 18, tištěná 631 / file 642,
poslední tři řádky odpovědi. Původní sazba odpovědi a algoritmu Q na
115–116 byla zobrazena. Fyzický výtisk ani prvenství neověřeny.

Odpověď správně varuje, že nahradit oba ostré scan testy Q3 a Q4
neostrými není bezpečné. Její konkrétní pokračování ale říká, že po
výměně R0/R1 přesune třetí partition původní R0 na R2. K této fázi
algoritmus nemusí vůbec definovaně dojít.

Stačí N=2, M=1, K0=−1, K1=K2=0, K3=1. To splňuje i zpřísněné (13).
Pro variantu uvedenou v odpovědi platí:

1. První Q2: l=1,r=2,K=0,i=1,j=3. Q3 se změní na opakování při
   K[i]≤K: i=2 projde, i=3 zastaví. Q4 opakuje při K≤K[j]: j=2,1
   projde, j=0 zastaví. Q5 zamění R1/R0. Nyní K0=0,K1=−1,K2=0.
2. Q7 má r−j=2>M≥j−l=−1, tedy nastaví l=j+1=1. Nová aktivní část
   je opět [1,2], nikoli [2,2].
3. Druhý Q2 vezme K=K1=−1. Q3 se zastaví na i=2. Q4 čte postupně
   K2=0, K1=−1, K0=0; všechny splňují K≤K[j]. Potom sníží j na −1
   a požaduje K[−1], který algoritmus nemá definován.

Tedy už druhá partition přejde pod dolní zarážku. Bez libovolného
dodatečného obsahu paměti není žádná třetí fáze určena; i s dodanou
pamětí by její výsledek závisel na údajích mimo zadání. Stejný argument
platí pro libovolné N>M a všechny vstupní klíče shodné c, s ostrými
vnějšími zarážkami. Není to jen nedostatek speciálního malého případu.

Krátká oprava poslední věty: po výměně R0/R1 již druhá partition
pokračuje pod index 0. Původní správné Q se nemění; hlavní varování
odpovědi je nadále správné. Vada se týká pouze jejího vysvětlujícího
průchodu nesprávnou variantou.

Všech pět dodaných vrstev je v
`sources/quicksort-equal-key-trace-errata-review.json`. Změna na 631
z 11.3.2016 přesouvá pouze čárku u uvozovek; tento průchod neopravuje.
