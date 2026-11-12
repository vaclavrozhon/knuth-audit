# V2-C0107: bitová versus algebraická mez online násobení

Stav: **candidate**,2.11.2026. Lokace: erratum7.8.2020 k odpovědi
4.3.3-15,str.634. Viz [úplný rozbor a definice R_*](fast-online.md).
Erratum uvádí O(R_*(n)), kde R_* je zavedeno v citovaném článku2014
pro algebraický model. Jeho Theorem17 pro p-adické/bitové násobení
při p=2 dává navíc faktor (log log n)^2 log log log n.

Originál errata a autorské PDF str.2,3,4,7,8 byly přečteny.
Čtyři vrstvy errat byly prohledány podle stránky,jmen i vzorce;
pozdější upřesnění nebylo nalezeno. Není doloženo, že silnější mez
z errata je nepravdivá: může být dosažitelná specializací nebo
jiným argumentem. Proto candidate, nikoli confirmed. Potřebujeme
vyjasnit zdroj přesného bitového odhadu; formulace s konstantou
sqrt(ln4)+o(1) v exponentu je doložená i článkem2021,str.2.

Primární zdroj: [revidované PDF2014](../sources/vanderhoeven-2014-fastrelax.pdf),
[věta17](../images/fastrelax2014-p7.png),
[erratum](../images/accuracy-errata-all2-pre-14.png).
Poslední fyzický dotisk a priorita neověřeny. Neodesláno.
