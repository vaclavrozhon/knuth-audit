# Primární prameny: přesně přečtený rozsah

## Galton 1889

Francis Galton, *Natural Inheritance* (Macmillan, 1889), zdroj `sources/galton1889.pdf`, URL a SHA-256 v sousedním metadata JSON. Přesně přečteno: začátek Appendix G na tištěné straně 248 a celá strana 249, obrazy PDF 255 a 256; strana 247 a první část 248 byly pouze orientačně zobrazeny při hledání přílohy. Strana 249 obsahuje explicitní binární číslování 1, 10, 11, 100, 101, 110, 111 a tabulku generací i převodů do desítkové soustavy. Výslovně zavádí také F/M a skládání rodových označení. Tím je potvrzen přesný obsah citace v odpovědi §2.3-15. Neklademe nárok na historické prvenství proti všem starším genealogickým systémům. Galtonův text o dědičnosti mimo tento rozsah nebyl auditován.

## Brent a Kung 1980

R. P. Brent a H. T. Kung, *On the Area of Binary Tree Layouts*, Information Processing Letters 11(1), 46–48, 29. srpna 1980. Primární PDF z webu spoluautora H. T. Kunga: `sources/brent-kung1980.pdf`, metadata JSON s URL a SHA-256. Všechny tři stránky byly přečteny obrazově (`images/brent-kung1980-001.png` až `003.png`), včetně obrázků, modelu, důkazů a závěru.

Strana 46 výslovně porovnává běžné rozložení s plochou řádu n log n a H-rozložení s plochou řádu n, kde n je počet listů úplného binárního stromu. Model vyžaduje jednotkovou vzdálenost uzlů a jednotkovou šířku vodičů. H-rozložení je tedy asymptoticky optimální bez dodatečného požadavku přístupu ke všem listům z okraje: lineární dolní mez plyne již z potřebného prostoru pro n odlišných uzlů. Samotný článek zkoumá omezení s listy na konvexním okraji a dokazuje v něm naopak nezbytnou plochu řádu n log n (Theorem 1 na 48). Slova „most efficient“ v odpovědi §2.3-22 tak mají tento prostorový a asymptotický význam; nejde o tvrzení optimálních konstant nebo všech možných omezení VLSI. Citace je věcně relevantní, bez nového nálezu.

## Výškové články k odpovědi §2.3.1-11

de Bruijn, Knuth, Rice, *The Average Height of Planted Plane Trees* (1972): [univerzitní kopie](https://pure.tue.nl/ws/files/2382241/597601.pdf), místně `sources/debruijn-knuth-rice1972.pdf`. Přečteny všechny původní strany 15–22 (PDF 2–9; první strana je repozitářová obálka), včetně definice výšky, přesných počtů, Mellinova výpočtu a konečné formule (34). Počítají obecné uspořádané stromy s N uzly a výšku počtem uzlů cesty. Pro zásobník knihy je N=n+1 a H=h+1. Vyšší člen kandidáta je odvozen samostatně v `height-erratum-candidate.md`; konečná věta článku jej neuvádí.

Flajolet, Odlyzko, *The Average Height of Binary Trees and Other Simple Trees* (1982): [autorská kopie](https://algo.inria.fr/flajolet/Publications/FlOd82height.pdf), místně `sources/flajolet-odlyzko1982.pdf`. Přečteny původní strany 171–173 a 200–207: definice rovnoměrného průměru a věty B/G/S, celá §6 s definicí jednoduchých rodin, analytickým zobecněním a konkrétními důsledky, začátek §7 o momentech. Nebyl znovu auditován úplný důkaz §§2–5 ani zbytek §7. Článek opravdu zahrnuje běžnou binární výšku a další rodiny; její hlavní konstanta 2*sqrt(pi*n) se nesmí zaměnit za zásobníkové h z knihy.

Flajolet, Gao, Odlyzko, Richmond, *The Distribution of Heights of Binary Trees and Other Simple Trees* (1993): [autorská kopie](https://algo.inria.fr/flajolet/Publications/FlGaOdRi93.pdf), místně `sources/flajolet-gao-odlyzko-richmond1993.pdf`. Přečteny původní strany 145–149 a 155–156: definice, úplná znění vět 1.1–1.4, podmínky jednoduchých rodin, škálování a začátek důkazu, dále §4 a reference. Strany 150–154 s prostředními důkazy nebyly přečteny. Původní věty potvrzují odkaz knihy na asymptotická rozdělení i zobecnění; neověřují sporný člen průměru v erratu. U obou posledních článků je toto uzavření bibliografického odkazu, nikoli tvrzení, že jsme nezávisle zrevidovali veškeré jejich výsledky.

## Swainson 1835 a známé erratum citátu na 330

První pokus o Darwin Online skončil HTTP 522; tento neúspěch zůstává v metadatech. [Wellcome Collection](https://wellcomecollection.org/works/nwkxgj34) poskytuje samostatné veřejné katalogové a IIIF API, v katalogu výslovně označené jako otevřené. Z nich byly získány manifest, OCR a původní obrazy. Nepoužíval se neveřejný přístup ani obcházení přihlašování.

Přečteny celé původní strany 193–195, tj. §§250–252 (`images/swainson1835-p193.jpg` až `p195.jpg`). Citovaná věta je první větou §250 na 193. Původní slovosled je „have been ever invented“, jak požaduje známé erratum; ve zbytku citátu rozdíl nalezen nebyl. Kontext kritizuje dichotomické zoologické klasifikace, nikoli algoritmické binární stromy. Další stažené obrazy obsahu, 132 a 365 sloužily pouze navigaci a nebyly věcně čteny.

## Fig. 18(b): Genesis 10

Přečten text Genesis 10:1–25 v [elektronickém vydání KJV](https://www.biblegateway.com/passage/?search=Genesis+10&version=KJV%3BESV%3BNKJV) a znovu přímo prohlédnuta celá Fig. 18 na 310. Všechny zobrazené rodičovské hrany a jména souhlasí po známé opravě Meschech na Meshech. Obrázek neukazuje odbočku k Philistim z vedlejší věty 10:14; netvrdí však úplnost všech jmen, a proto to není nález. Ověřena je shoda se zněním literárního pramene v této anglické edici, nikoli historická existence osob ani textová kritika hebrejských rukopisů. Genealogie Fig. 18(a) tím není ověřena.

Přesný zbývající seznam je v `remaining-primary-sources.md`. Žádná nedostupnost původní citace nebyla zaměněna za chybu jejího technického obsahu.
