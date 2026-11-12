# V4A-F0008 — prime flip potřebuje n≥2

**Confirmed, low.** §7.1.1–70, zadání p89/file106 a odpověď
p547/file564. Původní sazba zkontrolována v `images/file106.png`
a `images/proof-median-answer-1.png`; definice/projekční větev
také p63–64 v `proof-median-1.png` a `file081.png`.

Zadání bere libovolnou monotónní selfduální booleovskou funkci
f(x_1,...,x_n), vybere prime implikant s indexovým vektorem t
a tvrdí, že

    g(x)=(f(x) AND [x≠t]) OR [x=¬t]

zůstává monotónní a selfduální. Žádná podmínka n≥2 ani
netriviality zde není; projekce jsou v okolních definicích
a v důkazu Theorem P na p64 výslovně zahrnuté.

Vezměme **n=1, f(x)=x, t=1**. f je monotónní, selfduální
a x je jeho jediný prime implikant. Přímé dosazení dává

| x | f(x) | [x≠t] | [x=¬t] | g(x) |
|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 |

Tedy 0<1, ale g(0)>g(1). Výsledkem je negace, která je
selfduální, avšak není monotónní. V odpovědi je přesně
vadná větev „if ... y=t, we have g(x)=0“ při x=0,y=1.

**Oprava:** doplnit n≥2. Dostatečnost má obecný důkaz v
`notes/proof-067-y-representation-flip.md`, P0914: prime
vektor t pak obsahuje 0 i 1, a proto je neporovnatelný
s ¬t. Odstranění minimálního pravdivého t a přidání maximálního
nepravdivého ¬t tak zachová monotónnost. Tento důkaz zahrnuje
i projekce s dalšími nepodstatnými proměnnými.

**Errata, 2026-11-07:** prohledány všechny relevantní vrstvy
`errata/text/all4a-pre.txt`, `all4a.txt`, `err4a.txt`,
`all4f0.txt`, `all4f1.txt` podle stran, čísla úlohy i pojmů
prime/self-dual/Meyerowitz/Bioch/Ibaraki. Neobsahují opravu
domény ani vzorce 70. P547 line −5 z 2. 1. 2012 patří
k 75(b), přesuny 67 z 8. 7. 2011 jsou jiná úloha. Jejich
původní sazba je v `images/proof-y-errata08.png` a
`images/proof-y-errata22.png`. F0 doplňuje 68, nikoli 70.

Žádný výpočetní program, žádný závěr o prvenství nebo odměně.
Tištěný fyzický exemplář není nezávisle ověřen. Vada je pouze
jednobitová doména; obecný flip pro n≥2 je matematicky správný.
